#!/usr/bin/env python3
"""审计 OccupancySaturation 后的 Tail 容量压力。

用法示例：
  python3 experiments/prime_matrix_triad_a1_tail_capacity_pressure_audit.py
  python3 experiments/prime_matrix_triad_a1_tail_capacity_pressure_audit.py \
    --base-json docs/monograph/prime-matrix-triad-a1-q30030-multiplicity-cap.json \
    --lift-json docs/monograph/prime-matrix-triad-a1-q510510-multiplicity-cap.json \
    --json-out docs/monograph/prime-matrix-triad-a1-tail-capacity-pressure-q30030-q510510.json \
    --md-out docs/monograph/prime-matrix-triad-a1-tail-capacity-pressure-q30030-q510510.md

输出：
  docs/monograph/prime-matrix-triad-a1-tail-capacity-pressure-q2310-q30030.json
  docs/monograph/prime-matrix-triad-a1-tail-capacity-pressure-q2310-q30030.md
"""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
import math
from math import prod
from pathlib import Path
from typing import Any

from prime_matrix_bpn_low_hole_bucket_capacity import (
    high_completion_stats,
    low_holes_for_phase,
)


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_BASE = DOCS / "h4-pdec-lhb-multiplicity-cap-certificate.json"
DEFAULT_LIFT = DOCS / "prime-matrix-triad-a1-q30030-multiplicity-cap.json"
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-tail-capacity-pressure-q2310-q30030.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-tail-capacity-pressure-q2310-q30030.md"


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


def promoted_removed_holes(
    p: int,
    phase: int,
    q: int,
    promoted_prime: int,
    holes: list[int],
    residue: int,
) -> list[int]:
    """返回 promoted prime 在该 fiber residue 下删除的旧洞。"""
    lifted_phase = phase + residue * q
    return [
        col
        for col in holes
        if ((lifted_phase - 1) * p + col) % promoted_prime == 0
    ]


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


def load_ratio(residual_count: int, simple_capacity_sum: int) -> float | None:
    """残余洞数相对简单容量的负载比例。"""
    if simple_capacity_sum == 0:
        return None
    return residual_count / simple_capacity_sum


def bucket_template(key: int) -> dict[str, Any]:
    """创建按残余洞数聚合的桶。"""
    return {
        "residual_hole_count": key,
        "slots": 0,
        "surviving_slots": 0,
        "dead_slots": 0,
        "capacity_deficit_dead_slots": 0,
        "hall_certified_dead_slots": 0,
        "completion_mass": 0,
        "max_completion_count": 0,
        "max_simple_capacity_sum": 0,
        "survivor_kl_floor_sum": 0.0,
        "max_survivor_kl_floor": 0.0,
    }


def finalize_buckets(buckets: dict[int, dict[str, Any]]) -> list[dict[str, Any]]:
    """补齐桶比例。"""
    rows = []
    for _, row in sorted(buckets.items()):
        slots = int(row["slots"])
        rows.append(
            {
                **row,
                "survival_rate": ratio(int(row["surviving_slots"]), slots),
                "capacity_deficit_dead_rate": ratio(
                    int(row["capacity_deficit_dead_slots"]), slots
                ),
                "hall_certified_dead_rate": ratio(
                    int(row["hall_certified_dead_slots"]), slots
                ),
                "avg_survivor_kl_floor": (
                    float(row["survivor_kl_floor_sum"]) / int(row["surviving_slots"])
                    if int(row["surviving_slots"])
                    else None
                ),
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
    """分析单个 P 的 Tail 容量压力。"""
    base_m = [int(value) for value in base_item["m_vector"]]
    lift_m = [int(value) for value in lift_item["m_vector"]]
    low_primes = [int(value) for value in base_item["low_primes"]]
    lift_low_primes = [int(value) for value in lift_item["low_primes"]]
    tail_primes = [int(value) for value in lift_item["high_primes"]]
    tail_high_period = prod(tail_primes) if tail_primes else 1

    active_old = [phase for phase, value in enumerate(base_m) if value > 0]
    nonempty_slots = 0
    empty_hole_slots = 0
    surviving_slots = 0
    dead_slots = 0
    capacity_deficit_dead_slots = 0
    hall_certified_dead_slots = 0
    hall_uncertified_dead_slots = 0
    consistency_mismatches: list[dict[str, Any]] = []

    completion_hist: Counter[int] = Counter()
    removed_hist: Counter[int] = Counter()
    residual_hist: Counter[int] = Counter()
    simple_capacity_hist: Counter[int] = Counter()
    max_single_cover_hist: Counter[int] = Counter()
    load_values: list[float] = []
    survivor_load_values: list[float] = []
    dead_load_values: list[float] = []
    survivor_kl_floor_values: list[float] = []
    buckets: dict[int, dict[str, Any]] = {}

    capacity_deficit_examples: list[dict[str, Any]] = []
    hall_examples: list[dict[str, Any]] = []
    survivor_pressure_examples: list[dict[str, Any]] = []

    for phase in active_old:
        holes = low_holes_for_phase(p, q, low_primes, phase)
        if not holes:
            empty_hole_slots += promoted_prime
            continue
        nonempty_slots += promoted_prime

        for residue in range(promoted_prime):
            lifted_phase = phase + residue * q
            removed = promoted_removed_holes(
                p, phase, q, promoted_prime, holes, residue
            )
            removed_set = set(removed)
            residual_holes = [col for col in holes if col not in removed_set]
            direct_lift_holes = low_holes_for_phase(
                p, q_lift, lift_low_primes, lifted_phase
            )
            stats = high_completion_stats(
                p, q_lift, lifted_phase, residual_holes, tail_primes
            )
            completion_count = int(stats["completion_count"])
            lift_count = int(lift_m[lifted_phase])
            if (
                completion_count != lift_count
                or sorted(residual_holes) != sorted(direct_lift_holes)
            ) and len(consistency_mismatches) < detail_limit:
                consistency_mismatches.append(
                    {
                        "old_phase": phase,
                        "residue": residue,
                        "lifted_phase": lifted_phase,
                        "residual_holes": residual_holes,
                        "direct_lift_holes": direct_lift_holes,
                        "computed_completion": completion_count,
                        "lift_m_vector_completion": lift_count,
                    }
                )

            residual_count = len(residual_holes)
            simple_capacity = int(stats["simple_capacity_sum"])
            max_single_cover = int(stats["max_single_residue_class_cover"])
            load = load_ratio(residual_count, simple_capacity)
            if load is not None:
                load_values.append(load)

            survives = completion_count > 0
            kl_floor = (
                math.log(tail_high_period / completion_count)
                if completion_count > 0
                else None
            )
            if survives:
                surviving_slots += 1
                if load is not None:
                    survivor_load_values.append(load)
                if kl_floor is not None:
                    survivor_kl_floor_values.append(kl_floor)
            else:
                dead_slots += 1
                if load is not None:
                    dead_load_values.append(load)

            is_capacity_deficit = residual_count > simple_capacity
            is_hall_certified = (not survives) and int(stats["best_hall_deficit"]) > 0
            if is_capacity_deficit and not survives:
                capacity_deficit_dead_slots += 1
            if is_hall_certified:
                hall_certified_dead_slots += 1
            if (not survives) and not is_hall_certified:
                hall_uncertified_dead_slots += 1

            completion_hist[completion_count] += 1
            removed_hist[len(removed)] += 1
            residual_hist[residual_count] += 1
            simple_capacity_hist[simple_capacity] += 1
            max_single_cover_hist[max_single_cover] += 1

            bucket = buckets.setdefault(residual_count, bucket_template(residual_count))
            bucket["slots"] += 1
            bucket["completion_mass"] += completion_count
            bucket["max_completion_count"] = max(bucket["max_completion_count"], completion_count)
            bucket["max_simple_capacity_sum"] = max(
                bucket["max_simple_capacity_sum"], simple_capacity
            )
            if survives:
                bucket["surviving_slots"] += 1
                if kl_floor is not None:
                    bucket["survivor_kl_floor_sum"] += kl_floor
                    bucket["max_survivor_kl_floor"] = max(
                        bucket["max_survivor_kl_floor"], kl_floor
                    )
            else:
                bucket["dead_slots"] += 1
            if is_capacity_deficit and not survives:
                bucket["capacity_deficit_dead_slots"] += 1
            if is_hall_certified:
                bucket["hall_certified_dead_slots"] += 1

            example = {
                "old_phase": phase,
                "residue": residue,
                "lifted_phase": lifted_phase,
                "old_holes": holes,
                "removed_holes": removed,
                "residual_holes": residual_holes,
                "residual_hole_count": residual_count,
                "tail_primes": tail_primes,
                "simple_capacity_sum": simple_capacity,
                "max_single_residue_class_cover": max_single_cover,
                "completion_count": completion_count,
                "load_ratio": load,
                "kl_floor_to_uniform_tail": kl_floor,
                "best_hall_deficit": stats["best_hall_deficit"],
                "min_hall_subset_holes": stats["min_hall_subset_holes"],
            }

            if is_capacity_deficit and len(capacity_deficit_examples) < detail_limit:
                capacity_deficit_examples.append(example)
            if is_hall_certified and len(hall_examples) < detail_limit:
                hall_examples.append(example)
            if survives:
                survivor_pressure_examples.append(example)
                survivor_pressure_examples.sort(
                    key=lambda item: (
                        item["residual_hole_count"],
                        item["load_ratio"] if item["load_ratio"] is not None else -1,
                        item["completion_count"],
                    ),
                    reverse=True,
                )
                del survivor_pressure_examples[detail_limit:]

    return {
        "p": p,
        "q": q,
        "q_lift": q_lift,
        "promoted_prime": promoted_prime,
        "tail_primes": tail_primes,
        "tail_high_period": tail_high_period,
        "active_old_phase_count": len(active_old),
        "nonempty_fiber_slots": nonempty_slots,
        "empty_hole_slots": empty_hole_slots,
        "surviving_slots": surviving_slots,
        "dead_slots": dead_slots,
        "survival_rate": ratio(surviving_slots, nonempty_slots),
        "deletion_rate": ratio(dead_slots, nonempty_slots),
        "capacity_deficit_dead_slots": capacity_deficit_dead_slots,
        "capacity_deficit_dead_rate": ratio(capacity_deficit_dead_slots, nonempty_slots),
        "hall_certified_dead_slots": hall_certified_dead_slots,
        "hall_certified_dead_rate": ratio(hall_certified_dead_slots, nonempty_slots),
        "hall_uncertified_dead_slots": hall_uncertified_dead_slots,
        "avg_load_ratio": avg(load_values),
        "avg_survivor_load_ratio": avg(survivor_load_values),
        "avg_dead_load_ratio": avg(dead_load_values),
        "max_load_ratio": max(load_values, default=None),
        "avg_survivor_kl_floor_to_uniform_tail": avg(survivor_kl_floor_values),
        "max_survivor_kl_floor_to_uniform_tail": max(survivor_kl_floor_values, default=None),
        "min_positive_survivor_kl_floor_to_uniform_tail": min(
            (value for value in survivor_kl_floor_values if value > 0),
            default=None,
        ),
        "completion_count_histogram": dict(
            sorted((str(k), v) for k, v in completion_hist.items())
        ),
        "removed_hole_count_histogram": dict(
            sorted((str(k), v) for k, v in removed_hist.items())
        ),
        "residual_hole_count_histogram": dict(
            sorted((str(k), v) for k, v in residual_hist.items())
        ),
        "simple_capacity_sum_histogram": dict(
            sorted((str(k), v) for k, v in simple_capacity_hist.items())
        ),
        "max_single_cover_histogram": dict(
            sorted((str(k), v) for k, v in max_single_cover_hist.items())
        ),
        "by_residual_hole_count": finalize_buckets(buckets),
        "consistency_mismatches": consistency_mismatches,
        "examples": {
            "capacity_deficit": capacity_deficit_examples,
            "hall_certified": hall_examples,
            "survivor_pressure": survivor_pressure_examples,
        },
        "structural_reading": (
            "每个 fiber 的幸存完全等价于 Tail_{>r} 完成 residual_holes。"
            "若 residual_holes 的简单容量或 Hall 条件失败，则该 fiber 必死；"
            "若在高残余负载下仍大量幸存，则进入 Tail 条件分布/KL 压力。"
        ),
    }


def run(base_path: Path, lift_path: Path, p_filter: set[int] | None, detail_limit: int) -> dict[str, Any]:
    """运行 Tail 容量压力审计。"""
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

    mismatches = sum(len(item["consistency_mismatches"]) for item in prime_results)
    return {
        "certificate_type": "triad_a1_tail_capacity_pressure_audit",
        "status": (
            "tail_capacity_pressure_materialized"
            if mismatches == 0
            else "tail_capacity_pressure_has_consistency_mismatches"
        ),
        "q": q,
        "q_lift": q_lift,
        "promoted_prime": promoted_prime,
        "p_values": common_p,
        "source_hashes": {
            "tail_capacity_pressure_script": file_sha256(Path(__file__).resolve()),
            "capacity_script": file_sha256(
                ROOT / "experiments" / "prime_matrix_bpn_low_hole_bucket_capacity.py"
            ),
            "base_multiplicity_json": file_sha256(base_path),
            "lift_multiplicity_json": file_sha256(lift_path),
        },
        "prime_results": prime_results,
        "consistency_mismatch_count": mismatches,
        "review_conclusion": (
            "本审计把每个 promoted fiber 的残余洞集交给同一 Tail CRT set-cover DP。"
            "容量/Hall 失败直接证明 fiber 死亡；高负载仍幸存的槽位则是 KL/PDEC 压力输入。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        f"# Triad-A1 Tail 容量压力审计：Q={result['q']} -> Q={result['q_lift']}",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 审计语义",
        "",
        f"本层 promoted prime 为 `r={result['promoted_prime']}`。对旧洞集 `H_Q(t)` 和 residue `b`：",
        "",
        "```text",
        "R_b(H)={c in H_Q(t): ((t+bQ-1)P+c)=0 mod r}",
        "Residual_b=H_Q(t)\\R_b(H)",
        "b 幸存 <=> Tail_{>r} 能完成 Residual_b",
        "```",
        "",
        "审计对每个 `(t,b)` 重新调用同一 `high_completion_stats`，并校验它与 lift 层 `M(t+bQ)` 一致。",
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
            f"- `consistency_mismatch_count={result['consistency_mismatch_count']}`。",
            "",
            "| P | tail primes | M_tail | slots | survival | deletion | cap-def dead | Hall dead | Hall uncert dead | avg load | avg survivor load | avg KL floor | max KL floor |",
            "| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for item in result["prime_results"]:
        lines.append(
            "| {p} | `{tail}` | {mtail} | {slots} | {surv} | {dele} | {cap} | {hall} | {uncert} | {avgload} | {survload} | {avgkl} | {maxkl} |".format(
                p=item["p"],
                tail=item["tail_primes"],
                mtail=item["tail_high_period"],
                slots=item["nonempty_fiber_slots"],
                surv=fmt_float(item["survival_rate"]),
                dele=fmt_float(item["deletion_rate"]),
                cap=fmt_float(item["capacity_deficit_dead_rate"]),
                hall=fmt_float(item["hall_certified_dead_rate"]),
                uncert=item["hall_uncertified_dead_slots"],
                avgload=fmt_float(item["avg_load_ratio"]),
                survload=fmt_float(item["avg_survivor_load_ratio"]),
                avgkl=fmt_float(item["avg_survivor_kl_floor_to_uniform_tail"]),
                maxkl=fmt_float(item["max_survivor_kl_floor_to_uniform_tail"]),
            )
        )

    lines.extend(["", "## 4. 按残余洞数分桶", ""])
    for item in result["prime_results"]:
        lines.extend(
            [
                f"### P={item['p']}",
                "",
                "| residual holes | slots | survival | cap-def dead | Hall dead | completion mass | max completion | max simple cap | avg KL floor | max KL floor |",
                "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
            ]
        )
        for row in item["by_residual_hole_count"]:
            lines.append(
                "| {holes} | {slots} | {surv} | {cap} | {hall} | {mass} | {maxcomp} | {maxcap} | {avgkl} | {maxkl} |".format(
                    holes=row["residual_hole_count"],
                    slots=row["slots"],
                    surv=fmt_float(row["survival_rate"]),
                    cap=fmt_float(row["capacity_deficit_dead_rate"]),
                    hall=fmt_float(row["hall_certified_dead_rate"]),
                    mass=row["completion_mass"],
                    maxcomp=row["max_completion_count"],
                    maxcap=row["max_simple_capacity_sum"],
                    avgkl=fmt_float(row["avg_survivor_kl_floor"]),
                    maxkl=fmt_float(row["max_survivor_kl_floor"]),
                )
            )
        lines.append("")

    lines.extend(
        [
            "## 5. 读法",
            "",
            "若 `cap-def dead` 或 `Hall dead` 占主导，则 Tail 容量不足直接支付删除势。",
            "若高残余洞数、高负载下仍有大量 `survival`，则正式质量被迫落入很小的 Tail 完成集合；",
            "相对 Tail 均匀基准的单槽 KL 下界为 `log(M_tail/completion_count)`，因此进入 `NoDeletion-KL/PDEC/CleanKLS`。",
            "",
            "本审计不声称终端闭合；它把 `OccupancySaturation` 的后续义务压成了可复用的 Tail set-cover 容量证书。",
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
                "consistency_mismatch_count": result["consistency_mismatch_count"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
