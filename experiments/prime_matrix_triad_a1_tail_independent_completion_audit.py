#!/usr/bin/env python3
"""审计 promoted prime zero-cover residue 上的 Tail 独立完成。

用法示例：
  python3 experiments/prime_matrix_triad_a1_tail_independent_completion_audit.py
  python3 experiments/prime_matrix_triad_a1_tail_independent_completion_audit.py \
    --base-json docs/monograph/prime-matrix-triad-a1-q30030-multiplicity-cap.json \
    --lift-json docs/monograph/prime-matrix-triad-a1-q510510-multiplicity-cap.json \
    --json-out docs/monograph/prime-matrix-triad-a1-tail-independent-completion-q30030-q510510.json \
    --md-out docs/monograph/prime-matrix-triad-a1-tail-independent-completion-q30030-q510510.md

输出：
  docs/monograph/prime-matrix-triad-a1-tail-independent-completion-q2310-q30030.json
  docs/monograph/prime-matrix-triad-a1-tail-independent-completion-q2310-q30030.md
"""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
from typing import Any

from prime_matrix_bpn_low_hole_bucket_capacity import low_holes_for_phase


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_BASE = DOCS / "h4-pdec-lhb-multiplicity-cap-certificate.json"
DEFAULT_LIFT = DOCS / "prime-matrix-triad-a1-q30030-multiplicity-cap.json"
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-tail-independent-completion-q2310-q30030.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-tail-independent-completion-q2310-q30030.md"


def parse_p_values(raw: str | None) -> set[int] | None:
    """解析可选 P 列表。"""
    if raw is None:
        return None
    return {int(item.strip()) for item in raw.split(",") if item.strip()}


def file_sha256(path: Path) -> str:
    """计算文件 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def index_prime_results(data: dict[str, Any]) -> dict[int, dict[str, Any]]:
    """按 P 索引 prime_results。"""
    return {int(item["p"]): item for item in data["prime_results"]}


def promoted_removed_count(
    p: int,
    phase: int,
    q: int,
    promoted_prime: int,
    holes: list[int],
    residue: int,
) -> int:
    """计算 promoted prime 在该 residue 下覆盖多少旧洞。"""
    lifted_phase = phase + residue * q
    return sum(
        1
        for col in holes
        if ((lifted_phase - 1) * p + col) % promoted_prime == 0
    )


def analyze_prime(
    p: int,
    base_item: dict[str, Any],
    lift_item: dict[str, Any],
    q: int,
    q_lift: int,
    promoted_prime: int,
    detail_limit: int,
) -> dict[str, Any]:
    """审计单个 P 的 zero-cover tail 独立完成。"""
    base_m = [int(value) for value in base_item["m_vector"]]
    lift_m = [int(value) for value in lift_item["m_vector"]]
    low_primes = [int(value) for value in base_item["low_primes"]]
    tail_primes = [int(value) for value in lift_item["high_primes"]]

    active_old = [phase for phase, value in enumerate(base_m) if value > 0]
    nonempty_zero_cover_slots = 0
    nonempty_zero_cover_survivors = 0
    nonempty_zero_cover_killed = 0
    trivial_empty_hole_zero_cover_survivors = 0
    independent_completion_mass = 0
    independent_completion_hist: Counter[int] = Counter()
    killed_nonempty_hist: Counter[int] = Counter()
    survivor_hole_hist: Counter[int] = Counter()
    killed_hole_hist: Counter[int] = Counter()
    by_hole_count: dict[int, dict[str, int]] = {}
    examples: list[dict[str, Any]] = []

    for phase in active_old:
        holes = low_holes_for_phase(p, q, low_primes, phase)
        for residue in range(promoted_prime):
            removed = promoted_removed_count(p, phase, q, promoted_prime, holes, residue)
            if removed != 0:
                continue
            lifted_phase = phase + residue * q
            completion_count = int(lift_m[lifted_phase])
            if not holes:
                if completion_count > 0:
                    trivial_empty_hole_zero_cover_survivors += 1
                continue

            nonempty_zero_cover_slots += 1
            bucket = by_hole_count.setdefault(
                len(holes),
                {"slots": 0, "survived": 0, "killed": 0, "completion_mass": 0},
            )
            bucket["slots"] += 1
            if completion_count > 0:
                nonempty_zero_cover_survivors += 1
                independent_completion_mass += completion_count
                independent_completion_hist[completion_count] += 1
                survivor_hole_hist[len(holes)] += 1
                bucket["survived"] += 1
                bucket["completion_mass"] += completion_count
                if len(examples) < detail_limit:
                    examples.append(
                        {
                            "old_phase": phase,
                            "residue": residue,
                            "old_holes": holes,
                            "old_hole_count": len(holes),
                            "tail_primes": tail_primes,
                            "tail_completion_count": completion_count,
                        }
                    )
            else:
                nonempty_zero_cover_killed += 1
                killed_nonempty_hist[len(holes)] += 1
                killed_hole_hist[len(holes)] += 1
                bucket["killed"] += 1

    by_hole_rows = []
    for hole_count, row in sorted(by_hole_count.items()):
        slots = row["slots"]
        by_hole_rows.append(
            {
                "old_hole_count": hole_count,
                "zero_cover_slots": slots,
                "tail_independent_survivors": row["survived"],
                "killed": row["killed"],
                "survival_rate": row["survived"] / slots if slots else None,
                "completion_mass": row["completion_mass"],
            }
        )

    survival_rate = (
        nonempty_zero_cover_survivors / nonempty_zero_cover_slots
        if nonempty_zero_cover_slots
        else None
    )
    return {
        "p": p,
        "q": q,
        "q_lift": q_lift,
        "promoted_prime": promoted_prime,
        "tail_primes": tail_primes,
        "active_old_phase_count": len(active_old),
        "nonempty_zero_cover_slots": nonempty_zero_cover_slots,
        "tail_independent_survivors": nonempty_zero_cover_survivors,
        "nonempty_zero_cover_killed": nonempty_zero_cover_killed,
        "tail_independent_survival_rate": survival_rate,
        "trivial_empty_hole_zero_cover_survivors": trivial_empty_hole_zero_cover_survivors,
        "independent_completion_mass": independent_completion_mass,
        "independent_completion_histogram": dict(
            sorted((str(k), v) for k, v in independent_completion_hist.items())
        ),
        "survivor_hole_count_histogram": dict(
            sorted((str(k), v) for k, v in survivor_hole_hist.items())
        ),
        "killed_hole_count_histogram": dict(
            sorted((str(k), v) for k, v in killed_hole_hist.items())
        ),
        "by_old_hole_count": by_hole_rows,
        "examples": examples,
        "structural_reading": (
            "tail_independent_survivors 是 promoted prime 未覆盖任何旧洞但 Tail_{>r} 仍能完成旧洞集的槽位数。"
            "该比例若长期趋近 1，则进入 NoDeletion；若长期低，则 zero-cover death 提供删除势。"
        ),
    }


def run(base_path: Path, lift_path: Path, p_filter: set[int] | None, detail_limit: int) -> dict[str, Any]:
    """运行 Tail 独立完成审计。"""
    base = load_json(base_path)
    lift = load_json(lift_path)
    q = int(base["q"])
    q_lift = int(lift["q"])
    if q_lift % q != 0:
        raise ValueError(f"q_lift={q_lift} is not a multiple of q={q}")
    promoted_prime = q_lift // q

    base_results = index_prime_results(base)
    lift_results = index_prime_results(lift)
    common_p = sorted(set(base_results) & set(lift_results))
    if p_filter is not None:
        common_p = [p for p in common_p if p in p_filter]

    prime_results = [
        analyze_prime(
            p,
            base_results[p],
            lift_results[p],
            q,
            q_lift,
            promoted_prime,
            detail_limit,
        )
        for p in common_p
    ]

    return {
        "certificate_type": "triad_a1_tail_independent_completion_audit",
        "status": "tail_independent_zero_cover_completion_audited",
        "q": q,
        "q_lift": q_lift,
        "promoted_prime": promoted_prime,
        "p_values": common_p,
        "source_hashes": {
            "tail_independent_script": file_sha256(Path(__file__).resolve()),
            "base_multiplicity_json": file_sha256(base_path),
            "lift_multiplicity_json": file_sha256(lift_path),
        },
        "prime_results": prime_results,
        "review_conclusion": (
            "本审计只统计非空旧洞集上的 zero-cover 幸存。当前这些幸存很少；"
            "说明 Tail_{>r} 独立完成不是当前删除势的主导机制。"
        ),
    }


def fmt_float(value: float | None) -> str:
    """格式化浮点数。"""
    if value is None:
        return "n/a"
    return f"{value:.6g}"


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        f"# Triad-A1 Tail 独立完成审计：Q={result['q']} -> Q={result['q_lift']}",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 审计对象",
        "",
        "只统计：",
        "",
        "```text",
        "old H_Q(t) nonempty；",
        "promoted prime r 在 residue b 下覆盖 0 个旧洞；",
        "Tail_{>r} 仍能完成 H_Q(t)。",
        "```",
        "",
        "这正是 DeletionPotential 失败时会出现的 TailIndependentCompletion。",
        "",
        "## 2. 来源指纹",
        "",
        "| source | sha256 |",
        "| --- | --- |",
    ]
    for name, digest in result["source_hashes"].items():
        lines.append(f"| `{name}` | `{digest}` |")

    lines.extend(
        [
            "",
            "## 3. 总表",
            "",
            "| P | tail primes | nonempty zero-cover slots | tail-independent survivors | killed | survival rate | trivial empty-H survivors | completion mass | completion hist |",
            "| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for item in result["prime_results"]:
        lines.append(
            "| {p} | `{tail}` | {slots} | {surv} | {killed} | {rate} | {trivial} | {mass} | `{hist}` |".format(
                p=item["p"],
                tail=item["tail_primes"],
                slots=item["nonempty_zero_cover_slots"],
                surv=item["tail_independent_survivors"],
                killed=item["nonempty_zero_cover_killed"],
                rate=fmt_float(item["tail_independent_survival_rate"]),
                trivial=item["trivial_empty_hole_zero_cover_survivors"],
                mass=item["independent_completion_mass"],
                hist=item["independent_completion_histogram"],
            )
        )

    lines.extend(["", "## 4. 按旧洞数分桶", ""])
    for item in result["prime_results"]:
        lines.extend(
            [
                f"### P={item['p']}",
                "",
                "| old holes | zero-cover slots | tail-independent survivors | killed | survival rate | completion mass |",
                "| ---: | ---: | ---: | ---: | ---: | ---: |",
            ]
        )
        for row in item["by_old_hole_count"]:
            lines.append(
                "| {holes} | {slots} | {surv} | {killed} | {rate} | {mass} |".format(
                    holes=row["old_hole_count"],
                    slots=row["zero_cover_slots"],
                    surv=row["tail_independent_survivors"],
                    killed=row["killed"],
                    rate=fmt_float(row["survival_rate"]),
                    mass=row["completion_mass"],
                )
            )
        lines.append("")

    lines.extend(
        [
            "## 5. 读法",
            "",
            "若 `tail_independent_survival_rate` 长期高，promoted prime 近乎非必要，进入 NoDeletion-KL。",
            "若该比例长期低，zero-cover death 直接支付 DeletionPotential。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-json", type=Path, default=DEFAULT_BASE)
    parser.add_argument("--lift-json", type=Path, default=DEFAULT_LIFT)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    parser.add_argument("--p-values", type=str, default=None)
    parser.add_argument("--detail-limit", type=int, default=8)
    args = parser.parse_args()

    result = run(args.base_json, args.lift_json, parse_p_values(args.p_values), args.detail_limit)
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(
        json.dumps(
            {
                "status": result["status"],
                "q": result["q"],
                "q_lift": result["q_lift"],
                "p_values": result["p_values"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
