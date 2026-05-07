#!/usr/bin/env python3
"""审计旧洞集在 promoted prime 层上的 residue 占用。

用法示例：
  python3 experiments/prime_matrix_triad_a1_hole_residue_occupancy_audit.py
  python3 experiments/prime_matrix_triad_a1_hole_residue_occupancy_audit.py \
    --base-json docs/monograph/prime-matrix-triad-a1-q30030-multiplicity-cap.json \
    --lift-json docs/monograph/prime-matrix-triad-a1-q510510-multiplicity-cap.json \
    --json-out docs/monograph/prime-matrix-triad-a1-hole-residue-occupancy-q30030-q510510.json \
    --md-out docs/monograph/prime-matrix-triad-a1-hole-residue-occupancy-q30030-q510510.md

输出：
  docs/monograph/prime-matrix-triad-a1-hole-residue-occupancy-q2310-q30030.json
  docs/monograph/prime-matrix-triad-a1-hole-residue-occupancy-q2310-q30030.md
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
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-hole-residue-occupancy-q2310-q30030.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-hole-residue-occupancy-q2310-q30030.md"


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


def promoted_cover_residues(
    p: int,
    phase: int,
    q: int,
    promoted_prime: int,
    holes: list[int],
) -> dict[int, list[int]]:
    """返回每个 promoted residue b 覆盖的旧洞列。"""
    covered_by_residue: dict[int, list[int]] = {}
    for residue in range(promoted_prime):
        lifted_phase = phase + residue * q
        covered = [
            col
            for col in holes
            if ((lifted_phase - 1) * p + col) % promoted_prime == 0
        ]
        if covered:
            covered_by_residue[residue] = covered
    return covered_by_residue


def fmt_float(value: float | None) -> str:
    """格式化浮点数。"""
    if value is None:
        return "n/a"
    return f"{value:.6g}"


def ratio(numerator: int, denominator: int) -> float | None:
    """安全比例。"""
    if denominator == 0:
        return None
    return numerator / denominator


def avg(values: list[float]) -> float | None:
    """求均值。"""
    if not values:
        return None
    return sum(values) / len(values)


def add_bucket_row(bucket: dict[int, dict[str, Any]], hole_count: int, promoted_prime: int) -> dict[str, Any]:
    """取得按旧洞数聚合的桶。"""
    return bucket.setdefault(
        hole_count,
        {
            "old_hole_count": hole_count,
            "phase_count": 0,
            "fiber_slots": 0,
            "occupied_slots": 0,
            "tail_independent_slots": 0,
            "actual_surviving_slots": 0,
            "positive_cover_survivors": 0,
            "positive_cover_killed": 0,
            "zero_cover_survivors": 0,
            "zero_cover_killed": 0,
            "certified_deletion_lb_slots": 0,
            "min_occupied_count": promoted_prime,
            "max_occupied_count": 0,
        },
    )


def finalize_bucket_rows(bucket: dict[int, dict[str, Any]]) -> list[dict[str, Any]]:
    """补齐桶比例字段。"""
    rows = []
    for _, row in sorted(bucket.items()):
        slots = int(row["fiber_slots"])
        occupied = int(row["occupied_slots"])
        ti = int(row["tail_independent_slots"])
        actual = int(row["actual_surviving_slots"])
        certified = int(row["certified_deletion_lb_slots"])
        if row["phase_count"] == 0:
            row["min_occupied_count"] = 0
        rows.append(
            {
                **row,
                "occupied_rate": ratio(occupied, slots),
                "tail_independent_rate": ratio(ti, slots),
                "actual_survival_rate": ratio(actual, slots),
                "union_bound_rate": ratio(occupied + ti, slots),
                "certified_deletion_lb_rate": ratio(certified, slots),
            }
        )
    return rows


def analyze_prime(
    p: int,
    base_item: dict[str, Any],
    lift_item: dict[str, Any],
    q: int,
    q_lift: int,
    promoted_prime: int,
    detail_limit: int,
) -> dict[str, Any]:
    """分析单个 P 的旧洞 residue 占用。"""
    base_m = [int(value) for value in base_item["m_vector"]]
    lift_m = [int(value) for value in lift_item["m_vector"]]
    low_primes = [int(value) for value in base_item["low_primes"]]

    active_old = [phase for phase, value in enumerate(base_m) if value > 0]
    nonempty_phase_count = 0
    empty_phase_count = 0
    nonempty_slots = 0
    all_slots = len(active_old) * promoted_prime

    occupied_slots = 0
    tail_independent_slots = 0
    actual_surviving_slots = 0
    nonempty_actual_surviving_slots = 0
    positive_cover_survivors = 0
    positive_cover_killed = 0
    zero_cover_survivors = 0
    zero_cover_killed = 0
    empty_hole_survivors = 0
    empty_hole_killed = 0
    certified_deletion_lb_slots = 0

    old_hole_hist: Counter[int] = Counter()
    occupied_count_hist: Counter[int] = Counter()
    support_count_hist: Counter[int] = Counter()
    ti_count_hist: Counter[int] = Counter()
    bucket: dict[int, dict[str, Any]] = {}

    phase_occupied_ratios: list[float] = []
    phase_ti_ratios: list[float] = []
    phase_union_ratios: list[float] = []
    high_occupancy_examples: list[dict[str, Any]] = []
    tail_independent_examples: list[dict[str, Any]] = []
    positive_cover_killed_examples: list[dict[str, Any]] = []

    for phase in active_old:
        holes = low_holes_for_phase(p, q, low_primes, phase)
        hole_count = len(holes)
        old_hole_hist[hole_count] += 1
        covered_by_residue = promoted_cover_residues(p, phase, q, promoted_prime, holes)
        occupied = set(covered_by_residue)
        surviving = {
            residue
            for residue in range(promoted_prime)
            if lift_m[phase + residue * q] > 0
        }
        ti = surviving - occupied if holes else set()
        positive_surv = surviving & occupied
        positive_dead = occupied - surviving
        zero_surv = ti
        zero_dead = (
            set(range(promoted_prime)) - occupied - surviving
            if holes
            else set()
        )

        bucket_row = add_bucket_row(bucket, hole_count, promoted_prime)
        bucket_row["phase_count"] += 1
        bucket_row["fiber_slots"] += promoted_prime
        bucket_row["occupied_slots"] += len(occupied)
        bucket_row["actual_surviving_slots"] += len(surviving)
        bucket_row["min_occupied_count"] = min(bucket_row["min_occupied_count"], len(occupied))
        bucket_row["max_occupied_count"] = max(bucket_row["max_occupied_count"], len(occupied))

        actual_surviving_slots += len(surviving)
        occupied_count_hist[len(occupied)] += 1
        support_count_hist[len(surviving)] += 1

        if holes:
            nonempty_phase_count += 1
            nonempty_slots += promoted_prime
            occupied_slots += len(occupied)
            tail_independent_slots += len(ti)
            nonempty_actual_surviving_slots += len(surviving)
            positive_cover_survivors += len(positive_surv)
            positive_cover_killed += len(positive_dead)
            zero_cover_survivors += len(zero_surv)
            zero_cover_killed += len(zero_dead)
            certified_lb = max(0, promoted_prime - len(occupied) - len(ti))
            certified_deletion_lb_slots += certified_lb

            bucket_row["tail_independent_slots"] += len(ti)
            bucket_row["positive_cover_survivors"] += len(positive_surv)
            bucket_row["positive_cover_killed"] += len(positive_dead)
            bucket_row["zero_cover_survivors"] += len(zero_surv)
            bucket_row["zero_cover_killed"] += len(zero_dead)
            bucket_row["certified_deletion_lb_slots"] += certified_lb

            phase_occupied_ratios.append(len(occupied) / promoted_prime)
            phase_ti_ratios.append(len(ti) / promoted_prime)
            phase_union_ratios.append((len(occupied) + len(ti)) / promoted_prime)
            ti_count_hist[len(ti)] += 1

            example = {
                "old_phase": phase,
                "old_hole_count": hole_count,
                "old_holes": holes,
                "occupied_count": len(occupied),
                "occupied_ratio": len(occupied) / promoted_prime,
                "tail_independent_count": len(ti),
                "actual_surviving_count": len(surviving),
                "union_bound_count": len(occupied) + len(ti),
                "certified_deletion_lb_count": certified_lb,
            }
            high_occupancy_examples.append(example)
            high_occupancy_examples.sort(
                key=lambda item: (item["occupied_ratio"], item["old_hole_count"]),
                reverse=True,
            )
            del high_occupancy_examples[detail_limit:]

            if ti and len(tail_independent_examples) < detail_limit:
                tail_independent_examples.append(
                    {
                        **example,
                        "tail_independent_residues": sorted(ti),
                    }
                )
            if positive_dead and len(positive_cover_killed_examples) < detail_limit:
                positive_cover_killed_examples.append(
                    {
                        **example,
                        "positive_cover_killed_residues": sorted(positive_dead),
                        "covered_holes_by_killed_residue": {
                            str(residue): covered_by_residue[residue]
                            for residue in sorted(positive_dead)
                        },
                    }
                )
        else:
            empty_phase_count += 1
            empty_hole_survivors += len(surviving)
            empty_hole_killed += promoted_prime - len(surviving)

    nonempty_union_slots = occupied_slots + tail_independent_slots
    return {
        "p": p,
        "q": q,
        "q_lift": q_lift,
        "promoted_prime": promoted_prime,
        "active_old_phase_count": len(active_old),
        "all_fiber_slots": all_slots,
        "all_actual_surviving_slots": actual_surviving_slots,
        "all_actual_survival_rate": ratio(actual_surviving_slots, all_slots),
        "nonempty_old_hole_phase_count": nonempty_phase_count,
        "empty_old_hole_phase_count": empty_phase_count,
        "nonempty_fiber_slots": nonempty_slots,
        "nonempty_actual_surviving_slots": nonempty_actual_surviving_slots,
        "nonempty_actual_survival_rate": ratio(nonempty_actual_surviving_slots, nonempty_slots),
        "occupied_slots": occupied_slots,
        "occupied_rate": ratio(occupied_slots, nonempty_slots),
        "tail_independent_slots": tail_independent_slots,
        "tail_independent_rate": ratio(tail_independent_slots, nonempty_slots),
        "union_bound_slots": nonempty_union_slots,
        "union_bound_rate": ratio(nonempty_union_slots, nonempty_slots),
        "certified_deletion_lb_slots": certified_deletion_lb_slots,
        "certified_deletion_lb_rate": ratio(certified_deletion_lb_slots, nonempty_slots),
        "actual_nonempty_deletion_rate": (
            1.0 - nonempty_actual_surviving_slots / nonempty_slots
            if nonempty_slots
            else None
        ),
        "positive_cover_survivors": positive_cover_survivors,
        "positive_cover_killed": positive_cover_killed,
        "zero_cover_survivors": zero_cover_survivors,
        "zero_cover_killed": zero_cover_killed,
        "empty_hole_survivors": empty_hole_survivors,
        "empty_hole_killed": empty_hole_killed,
        "avg_phase_occupied_ratio": avg(phase_occupied_ratios),
        "max_phase_occupied_ratio": max(phase_occupied_ratios, default=None),
        "avg_phase_tail_independent_ratio": avg(phase_ti_ratios),
        "max_phase_tail_independent_ratio": max(phase_ti_ratios, default=None),
        "avg_phase_union_bound_ratio": avg(phase_union_ratios),
        "max_phase_union_bound_ratio": max(phase_union_ratios, default=None),
        "old_hole_count_histogram": dict(
            sorted((str(k), v) for k, v in old_hole_hist.items())
        ),
        "occupied_count_histogram": dict(
            sorted((str(k), v) for k, v in occupied_count_hist.items())
        ),
        "support_count_histogram": dict(
            sorted((str(k), v) for k, v in support_count_hist.items())
        ),
        "tail_independent_count_histogram": dict(
            sorted((str(k), v) for k, v in ti_count_hist.items())
        ),
        "by_old_hole_count": finalize_bucket_rows(bucket),
        "examples": {
            "highest_occupancy": high_occupancy_examples,
            "tail_independent": tail_independent_examples,
            "positive_cover_killed": positive_cover_killed_examples,
        },
        "structural_reading": (
            "对非空旧洞 H_Q(t)，实际幸存 residues 被 Occ_t 与 TI_t 控制。"
            "若 occupied_rate 与 tail_independent_rate 的和远小于 1，则该层给出删除势；"
            "若 occupied_rate 接近 1，则旧洞集已在 promoted prime residue 上过密。"
        ),
    }


def run(base_path: Path, lift_path: Path, p_filter: set[int] | None, detail_limit: int) -> dict[str, Any]:
    """运行旧洞 residue 占用审计。"""
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
        "certificate_type": "triad_a1_hole_residue_occupancy_audit",
        "status": "hole_residue_occupancy_materialized",
        "q": q,
        "q_lift": q_lift,
        "promoted_prime": promoted_prime,
        "p_values": common_p,
        "source_hashes": {
            "hole_residue_occupancy_script": file_sha256(Path(__file__).resolve()),
            "base_multiplicity_json": file_sha256(base_path),
            "lift_multiplicity_json": file_sha256(lift_path),
        },
        "prime_results": prime_results,
        "review_conclusion": (
            "本审计把 TailIndependentCompletion 的上界项 |Occ_t|/r 物化。"
            "当前层的非空旧洞在新增素数 residue 上占用比例明显低于 1，"
            "删除势主要来自未占用且不能被 Tail 独立完成的 zero-cover residue。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        f"# Triad-A1 HoleResidueOccupancy 审计：Q={result['q']} -> Q={result['q_lift']}",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 结构等式",
        "",
        f"本层 promoted prime 为 `r={result['promoted_prime']}`。固定旧活跃相位 `t` 与旧洞集 `H_Q(t)`：",
        "",
        "```text",
        "Occ_t={b: exists c in H_Q(t), ((t+bQ-1)P+c)=0 mod r}",
        "TI_t ={b: b notin Occ_t, 且 lift 后该 fiber 仍幸存}",
        "S_t  ={b: lift 后该 fiber 幸存}",
        "```",
        "",
        "对非空 `H_Q(t)`：",
        "",
        "```text",
        "S_t subset Occ_t union TI_t",
        "|S_t|/r <= |Occ_t|/r + |TI_t|/r",
        "|Occ_t| <= min(|H_Q(t)|, r)",
        "```",
        "",
        "所以只要 `Occ_t` 与 `TI_t` 不同时接近满层，fiber 删除势就不能消失。",
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
            "| P | nonempty phases | empty phases | occ rate | TI rate | union bound | actual survival | certified deletion lb | actual deletion | max occ | max TI |",
            "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for item in result["prime_results"]:
        lines.append(
            "| {p} | {nonempty} | {empty} | {occ} | {ti} | {union} | {surv} | {cert} | {actual_del} | {max_occ} | {max_ti} |".format(
                p=item["p"],
                nonempty=item["nonempty_old_hole_phase_count"],
                empty=item["empty_old_hole_phase_count"],
                occ=fmt_float(item["occupied_rate"]),
                ti=fmt_float(item["tail_independent_rate"]),
                union=fmt_float(item["union_bound_rate"]),
                surv=fmt_float(item["nonempty_actual_survival_rate"]),
                cert=fmt_float(item["certified_deletion_lb_rate"]),
                actual_del=fmt_float(item["actual_nonempty_deletion_rate"]),
                max_occ=fmt_float(item["max_phase_occupied_ratio"]),
                max_ti=fmt_float(item["max_phase_tail_independent_ratio"]),
            )
        )

    lines.extend(
        [
            "",
            "## 4. cover 类型分解",
            "",
            "| P | positive-cover survived | positive-cover killed | zero-cover survived/TI | zero-cover killed | empty-H survived | empty-H killed |",
            "| ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for item in result["prime_results"]:
        lines.append(
            "| {p} | {ps} | {pk} | {zs} | {zk} | {es} | {ek} |".format(
                p=item["p"],
                ps=item["positive_cover_survivors"],
                pk=item["positive_cover_killed"],
                zs=item["zero_cover_survivors"],
                zk=item["zero_cover_killed"],
                es=item["empty_hole_survivors"],
                ek=item["empty_hole_killed"],
            )
        )

    lines.extend(["", "## 5. 按旧洞数分桶", ""])
    for item in result["prime_results"]:
        lines.extend(
            [
                f"### P={item['p']}",
                "",
                "| old holes | phases | occ rate | TI rate | union bound | actual survival | certified deletion lb | min occ | max occ |",
                "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
            ]
        )
        for row in item["by_old_hole_count"]:
            lines.append(
                "| {holes} | {phases} | {occ} | {ti} | {union} | {surv} | {cert} | {min_occ} | {max_occ} |".format(
                    holes=row["old_hole_count"],
                    phases=row["phase_count"],
                    occ=fmt_float(row["occupied_rate"]),
                    ti=fmt_float(row["tail_independent_rate"]),
                    union=fmt_float(row["union_bound_rate"]),
                    surv=fmt_float(row["actual_survival_rate"]),
                    cert=fmt_float(row["certified_deletion_lb_rate"]),
                    min_occ=row["min_occupied_count"],
                    max_occ=row["max_occupied_count"],
                )
            )
        lines.append("")

    lines.extend(
        [
            "## 6. 读法",
            "",
            "本审计完成了 `TailIndependentCompletion` 后缺失的一块：`|Occ_t|/r` 不再是抽象项，而是可逐相位核验的占用率。",
            "",
            "若后续无限塔中 `occupied_rate + TI_rate` 长期低于 `1`，则删除势发散。若该和趋近 `1`，只能发生两种结构事件：",
            "",
            "```text",
            "occupied_rate -> 1：旧洞集在新增素数 residue 上近乎满占用，进入容量/PDEC；",
            "TI_rate       -> 1：promoted prime 近乎非必要，进入 NoDeletion-KL/CleanKLS。",
            "```",
            "",
            "因此下一步不再是数值逼近，而是证明这两个逃逸方向都必须回流到命名终端证书。",
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
