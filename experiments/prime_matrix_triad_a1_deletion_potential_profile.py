#!/usr/bin/env python3
"""审计 Triad-A1 升层中的 promoted-prime 删除势剖面。

用法示例：
  python3 experiments/prime_matrix_triad_a1_deletion_potential_profile.py
  python3 experiments/prime_matrix_triad_a1_deletion_potential_profile.py \
    --base-json docs/monograph/prime-matrix-triad-a1-q30030-multiplicity-cap.json \
    --lift-json docs/monograph/prime-matrix-triad-a1-q510510-multiplicity-cap.json \
    --json-out docs/monograph/prime-matrix-triad-a1-deletion-potential-profile-q30030-q510510.json \
    --md-out docs/monograph/prime-matrix-triad-a1-deletion-potential-profile-q30030-q510510.md

输出：
  docs/monograph/prime-matrix-triad-a1-deletion-potential-profile-q2310-q30030.json
  docs/monograph/prime-matrix-triad-a1-deletion-potential-profile-q2310-q30030.md
"""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
import math
from pathlib import Path
from typing import Any

from prime_matrix_bpn_low_hole_bucket_capacity import low_holes_for_phase


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_BASE = DOCS / "h4-pdec-lhb-multiplicity-cap-certificate.json"
DEFAULT_LIFT = DOCS / "prime-matrix-triad-a1-q30030-multiplicity-cap.json"
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-deletion-potential-profile-q2310-q30030.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-deletion-potential-profile-q2310-q30030.md"


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


def neg_log(value: float | None) -> float | None:
    """计算删除势 -log(value)。"""
    if value is None or value <= 0:
        return None
    return -math.log(value)


def promoted_residue_holes(p: int, phase: int, q: int, promoted_prime: int, holes: list[int], residue: int) -> list[int]:
    """返回 promoted prime 在指定 fiber residue 下覆盖的旧洞。"""
    lifted_phase = phase + residue * q
    return [
        col
        for col in holes
        if ((lifted_phase - 1) * p + col) % promoted_prime == 0
    ]


def avg(values: list[float]) -> float | None:
    """求均值。"""
    if not values:
        return None
    return sum(values) / len(values)


def analyze_prime(
    p: int,
    base_item: dict[str, Any],
    lift_item: dict[str, Any],
    q: int,
    q_lift: int,
    promoted_prime: int,
    detail_limit: int,
) -> dict[str, Any]:
    """分析单个 P 的 promoted-prime 删除势剖面。"""
    base_m = [int(value) for value in base_item["m_vector"]]
    lift_m = [int(value) for value in lift_item["m_vector"]]
    low_primes = [int(value) for value in base_item["low_primes"]]

    active_old = [phase for phase, value in enumerate(base_m) if value > 0]
    total_slots = len(active_old) * promoted_prime
    surviving_slots = 0
    killed_slots = 0
    full_fibers = 0
    partial_fibers = 0
    singleton_fibers = 0

    support_hist: Counter[int] = Counter()
    old_hole_hist: Counter[int] = Counter()
    killed_removed_hist: Counter[int] = Counter()
    survived_removed_hist: Counter[int] = Counter()
    survival_by_hole_count: dict[int, dict[str, int]] = {}
    killed_by_removed_examples: list[dict[str, Any]] = []
    full_fiber_examples: list[dict[str, Any]] = []
    singleton_examples: list[dict[str, Any]] = []

    phase_deletion_rates: list[float] = []
    survived_removed_values: list[float] = []
    killed_removed_values: list[float] = []

    for phase in active_old:
        holes = low_holes_for_phase(p, q, low_primes, phase)
        old_hole_hist[len(holes)] += 1
        surviving_residues: list[int] = []
        killed_residues: list[int] = []
        removed_by_residue: dict[int, int] = {}

        for residue in range(promoted_prime):
            lifted_phase = phase + residue * q
            survives = lift_m[lifted_phase] > 0
            removed_count = len(
                promoted_residue_holes(p, phase, q, promoted_prime, holes, residue)
            )
            removed_by_residue[residue] = removed_count
            bucket = survival_by_hole_count.setdefault(
                len(holes),
                {"slots": 0, "surviving": 0, "killed": 0},
            )
            bucket["slots"] += 1
            if survives:
                surviving_slots += 1
                surviving_residues.append(residue)
                survived_removed_hist[removed_count] += 1
                survived_removed_values.append(float(removed_count))
                bucket["surviving"] += 1
            else:
                killed_slots += 1
                killed_residues.append(residue)
                killed_removed_hist[removed_count] += 1
                killed_removed_values.append(float(removed_count))
                bucket["killed"] += 1
                if len(killed_by_removed_examples) < detail_limit:
                    killed_by_removed_examples.append(
                        {
                            "old_phase": phase,
                            "old_hole_count": len(holes),
                            "killed_residue": residue,
                            "promoted_removed_count": removed_count,
                            "surviving_residues": surviving_residues[:],
                        }
                    )

        support_count = len(surviving_residues)
        support_hist[support_count] += 1
        deletion_rate = 1.0 - support_count / promoted_prime
        phase_deletion_rates.append(deletion_rate)

        if support_count == promoted_prime:
            full_fibers += 1
            if len(full_fiber_examples) < detail_limit:
                full_fiber_examples.append(
                    {
                        "old_phase": phase,
                        "old_hole_count": len(holes),
                        "removed_count_hist": dict(Counter(removed_by_residue.values())),
                    }
                )
        elif support_count == 1:
            singleton_fibers += 1
            if len(singleton_examples) < detail_limit:
                singleton_examples.append(
                    {
                        "old_phase": phase,
                        "old_hole_count": len(holes),
                        "surviving_residue": surviving_residues[0],
                        "surviving_removed_count": removed_by_residue[surviving_residues[0]],
                        "killed_count": len(killed_residues),
                    }
                )
        else:
            partial_fibers += 1

    survival_rate = surviving_slots / total_slots if total_slots else None
    deletion_rate = killed_slots / total_slots if total_slots else None
    survival_by_hole_rows = []
    for hole_count, data in sorted(survival_by_hole_count.items()):
        slots = data["slots"]
        survival_by_hole_rows.append(
            {
                "old_hole_count": hole_count,
                "slots": slots,
                "surviving": data["surviving"],
                "killed": data["killed"],
                "survival_rate": data["surviving"] / slots if slots else None,
                "deletion_rate": data["killed"] / slots if slots else None,
            }
        )

    zero_cover_survived = survived_removed_hist.get(0, 0)
    zero_cover_killed = killed_removed_hist.get(0, 0)
    positive_cover_survived = sum(
        count for removed, count in survived_removed_hist.items() if removed > 0
    )
    positive_cover_killed = sum(
        count for removed, count in killed_removed_hist.items() if removed > 0
    )
    zero_cover_slots = zero_cover_survived + zero_cover_killed
    positive_cover_slots = positive_cover_survived + positive_cover_killed

    return {
        "p": p,
        "q": q,
        "q_lift": q_lift,
        "promoted_prime": promoted_prime,
        "active_old_phase_count": len(active_old),
        "total_fiber_slots": total_slots,
        "surviving_slots": surviving_slots,
        "killed_slots": killed_slots,
        "survival_rate": survival_rate,
        "deletion_rate": deletion_rate,
        "deletion_potential": neg_log(survival_rate),
        "fiber_counts": {
            "full_fibers": full_fibers,
            "partial_fibers": partial_fibers,
            "singleton_fibers": singleton_fibers,
            "support_count_histogram": dict(sorted((str(k), v) for k, v in support_hist.items())),
            "old_hole_count_histogram": dict(sorted((str(k), v) for k, v in old_hole_hist.items())),
        },
        "promoted_prime_effect": {
            "survived_removed_count_histogram": dict(
                sorted((str(k), v) for k, v in survived_removed_hist.items())
            ),
            "killed_removed_count_histogram": dict(
                sorted((str(k), v) for k, v in killed_removed_hist.items())
            ),
            "zero_cover_survived_slots": zero_cover_survived,
            "zero_cover_killed_slots": zero_cover_killed,
            "zero_cover_survival_rate": (
                zero_cover_survived / zero_cover_slots if zero_cover_slots else None
            ),
            "positive_cover_survived_slots": positive_cover_survived,
            "positive_cover_killed_slots": positive_cover_killed,
            "positive_cover_survival_rate": (
                positive_cover_survived / positive_cover_slots if positive_cover_slots else None
            ),
            "avg_removed_count_survived_slots": avg(survived_removed_values),
            "avg_removed_count_killed_slots": avg(killed_removed_values),
            "avg_phase_deletion_rate": avg(phase_deletion_rates),
        },
        "survival_by_old_hole_count": survival_by_hole_rows,
        "examples": {
            "killed_slots": killed_by_removed_examples,
            "full_fibers": full_fiber_examples,
            "singleton_fibers": singleton_examples,
        },
        "structural_reading": (
            "killed_slots / total_slots 是 promoted prime residue choice 的必要性比例；"
            "若该比例沿无限塔不可求和，则删除势发散。若趋零，则 promoted prime 在多数活跃相位上近乎非必要，进入 NoDeletion-KL。"
        ),
    }


def run(base_path: Path, lift_path: Path, p_filter: set[int] | None, detail_limit: int) -> dict[str, Any]:
    """运行删除势剖面审计。"""
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
        "certificate_type": "triad_a1_deletion_potential_profile",
        "status": "promoted_prime_essentiality_profile_materialized",
        "q": q,
        "q_lift": q_lift,
        "promoted_prime": promoted_prime,
        "p_values": common_p,
        "source_hashes": {
            "deletion_profile_script": file_sha256(Path(__file__).resolve()),
            "base_multiplicity_json": file_sha256(base_path),
            "lift_multiplicity_json": file_sha256(lift_path),
        },
        "prime_results": prime_results,
        "review_conclusion": (
            "本审计把 fiber 删除势解释为 promoted prime residue choice 的必要性比例。"
            "当前层 killed residue choices 很多，因此仍在 FiberDeletion；若未来该比例趋零，"
            "则 promoted prime 近乎非必要，必须转入 NoDeletion-KL。"
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
        f"# Triad-A1 删除势剖面：Q={result['q']} -> Q={result['q_lift']}",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 结构语义",
        "",
        f"本层 promoted prime 为 `{result['promoted_prime']}`。对旧活跃相位 `t`，它的每个 fiber residue 只覆盖旧洞集中的一个模 `r` 残基类。",
        "",
        "```text",
        "survival_rate = surviving residue choices / all residue choices；",
        "deletion_rate = killed residue choices / all residue choices；",
        "deletion_potential = -log(survival_rate)。",
        "```",
        "",
        "若删除率长期不小，则删除势发散；若删除率趋零，则 promoted prime 在多数相位上近乎非必要，进入 NoDeletion-KL。",
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
            "| P | active phases | survival | deletion | D=-log(survival) | full | partial | singleton | support hist | avg removed survived | avg removed killed |",
            "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: |",
        ]
    )
    for item in result["prime_results"]:
        counts = item["fiber_counts"]
        effect = item["promoted_prime_effect"]
        lines.append(
            "| {p} | {active} | {surv} | {dele} | {pot} | {full} | {partial} | {single} | `{hist}` | {survrem} | {killrem} |".format(
                p=item["p"],
                active=item["active_old_phase_count"],
                surv=fmt_float(item["survival_rate"]),
                dele=fmt_float(item["deletion_rate"]),
                pot=fmt_float(item["deletion_potential"]),
                full=counts["full_fibers"],
                partial=counts["partial_fibers"],
                single=counts["singleton_fibers"],
                hist=counts["support_count_histogram"],
                survrem=fmt_float(effect["avg_removed_count_survived_slots"]),
                killrem=fmt_float(effect["avg_removed_count_killed_slots"]),
            )
        )

    lines.extend(["", "## 4. 按旧洞数分桶", ""])
    for item in result["prime_results"]:
        lines.extend(
            [
                f"### P={item['p']}",
                "",
                "| old holes | slots | surviving | killed | survival | deletion |",
                "| ---: | ---: | ---: | ---: | ---: | ---: |",
            ]
        )
        for row in item["survival_by_old_hole_count"]:
            lines.append(
                "| {holes} | {slots} | {surv} | {killed} | {sr} | {dr} |".format(
                    holes=row["old_hole_count"],
                    slots=row["slots"],
                    surv=row["surviving"],
                    killed=row["killed"],
                    sr=fmt_float(row["survival_rate"]),
                    dr=fmt_float(row["deletion_rate"]),
                )
            )
        lines.append("")

    lines.extend(
        [
            "## 5. promoted prime 命中旧洞的效果",
            "",
            "| P | zero-cover survival | zero-cover killed | positive-cover survival | positive-cover killed | zero-cover survival rate | positive-cover survival rate |",
            "| ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for item in result["prime_results"]:
        effect = item["promoted_prime_effect"]
        lines.append(
            "| {p} | {zs} | {zk} | {ps} | {pk} | {zrate} | {prate} |".format(
                p=item["p"],
                zs=effect["zero_cover_survived_slots"],
                zk=effect["zero_cover_killed_slots"],
                ps=effect["positive_cover_survived_slots"],
                pk=effect["positive_cover_killed_slots"],
                zrate=fmt_float(effect["zero_cover_survival_rate"]),
                prate=fmt_float(effect["positive_cover_survival_rate"]),
            )
        )

    lines.extend(
        [
            "",
            "## 6. 读法",
            "",
            "本审计不证明删除势无限发散；它把每层删除势拆成 promoted prime residue choice 的必要性比例。",
            "后续若某层 `deletion_rate` 很小，不能视为失败，而是自动触发 NoDeletion-KL 门控。",
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
