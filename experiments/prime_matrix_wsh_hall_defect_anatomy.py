#!/usr/bin/env python3
"""审计 WSH-Hall 被强行压缩半径时的缺陷解剖。

用法示例：
  python3 experiments/prime_matrix_wsh_hall_defect_anatomy.py
  python3 experiments/prime_matrix_wsh_hall_defect_anatomy.py --max-records 60

该脚本读取 WSH-Hall 相位证书中的最紧行，故意把匹配半径压到最小半径以下，
然后寻找 Hall 缺陷区间并输出三类压力：

  1. 端点素数亏损：半素数块的半径邻域内素数少于半素数；
  2. 尾标签集中：同一尾素因子或尾因子对承载过多半素数；
  3. 轮筛/固定偏移相位集中：同一小轮相位或同一偏移通道负载过高。

注意：这是缺陷形态审计，不是全局 WSH-Hall 证明。
"""

from __future__ import annotations

import argparse
import bisect
import json
import math
from collections import Counter, defaultdict
from pathlib import Path

from prime_matrix_wsh_hall_phase_certificate import (
    build_tail_data,
    collect_rows,
    fixed_offset_ratio,
    next_prime_after,
    primes_from_table,
    sieve_bool,
    wheel_allowed_offset,
    wheel_modulus,
)


def merge_intervals(intervals: list[tuple[int, int]]) -> list[list[int]]:
    """合并整数闭区间。"""
    if not intervals:
        return []
    sorted_intervals = sorted(intervals)
    merged = [[sorted_intervals[0][0], sorted_intervals[0][1]]]
    for left, right in sorted_intervals[1:]:
        if left <= merged[-1][1] + 1:
            merged[-1][1] = max(merged[-1][1], right)
        else:
            merged.append([left, right])
    return merged


def primes_in_union(prime_values: list[int], intervals: list[list[int]]) -> list[int]:
    """提取落在区间并集中的素数。"""
    neighbors: list[int] = []
    for left, right in intervals:
        left_index = bisect.bisect_left(prime_values, left)
        right_index = bisect.bisect_right(prime_values, right)
        neighbors.extend(prime_values[left_index:right_index])
    return neighbors


def exact_hall_defect(
    semiprimes: list[int],
    prime_values: list[int],
    radius: int,
) -> dict | None:
    """在一维区间图中寻找精确连续 Hall 缺陷块。"""
    best_defect: dict | None = None
    for start_index in range(len(semiprimes)):
        intervals: list[tuple[int, int]] = []
        for end_index in range(start_index, len(semiprimes)):
            semi_value = semiprimes[end_index]
            intervals.append((semi_value - radius, semi_value + radius))
            merged = merge_intervals(intervals)
            neighbors = primes_in_union(prime_values, merged)
            semiprime_count = end_index - start_index + 1
            excess = semiprime_count - len(neighbors)
            if excess <= 0:
                continue
            span = merged[-1][1] - merged[0][0] + 1
            candidate = {
                "semi_index_range": [start_index, end_index],
                "semiprime_count": semiprime_count,
                "prime_count": len(neighbors),
                "excess": excess,
                "neighbor_intervals": merged,
                "span": span,
                "neighbor_primes_sample": neighbors[:20],
            }
            if best_defect is None:
                best_defect = candidate
                continue
            better = (candidate["excess"], -candidate["span"], candidate["semiprime_count"])
            current = (best_defect["excess"], -best_defect["span"], best_defect["semiprime_count"])
            if better > current:
                best_defect = candidate
    return best_defect


def row_data_for_prime(
    base_prime: int,
    is_prime: bytearray,
    prime_values: list[int],
    y_ratio: float,
) -> tuple[int, dict[int, list[int]], list[list[int]], list[list[int]]]:
    """重建某个 `p` 的行数据。"""
    next_base = next_prime_after(base_prime, prime_values)
    y_cutoff = max(2, int(math.floor(y_ratio * base_prime)))
    low_primes = [prime_value for prime_value in prime_values if prime_value <= y_cutoff]
    tail_primes = [prime_value for prime_value in prime_values if y_cutoff < prime_value <= base_prime]
    low_rough, tail_omega, tail_labels = build_tail_data(next_base, low_primes, tail_primes)
    primes_by_row, semis_by_row, _ = collect_rows(
        next_base,
        low_rough,
        tail_omega,
        tail_labels,
        is_prime,
    )
    return next_base, tail_labels, primes_by_row, semis_by_row


def chosen_radii(matching_radius: int) -> list[dict]:
    """给最小半径选择强制失败半径。"""
    if matching_radius <= 0:
        return []
    candidates = {
        "critical_minus_one": matching_radius - 1,
        "half_radius": max(1, matching_radius // 2),
        "quarter_radius": max(1, matching_radius // 4),
    }
    radii = []
    seen = set()
    for kind, radius in candidates.items():
        if radius <= 0 or radius >= matching_radius or radius in seen:
            continue
        seen.add(radius)
        radii.append({"kind": kind, "radius": radius})
    return radii


def analyze_defect(
    p: int,
    q: int,
    row: int,
    semiprimes: list[int],
    prime_values: list[int],
    tail_labels: dict[int, list[int]],
    radius: int,
    kind: str,
    wheel_primes: list[int],
) -> dict | None:
    """对单个强制缺陷做结构解剖。"""
    defect = exact_hall_defect(semiprimes, prime_values, radius)
    if defect is None:
        return None

    start_index, end_index = defect["semi_index_range"]
    defect_semis = semiprimes[start_index : end_index + 1]
    modulus = wheel_modulus(wheel_primes)
    tail_counter: Counter[int] = Counter()
    pair_counter: Counter[tuple[int, int]] = Counter()
    phase_counter: Counter[int] = Counter()
    allowed_offset_counter: Counter[int] = Counter()
    actual_edge_offset_counter: Counter[int] = Counter()
    total_allowed_offsets = 0
    total_actual_edges = 0

    for semi_value in defect_semis:
        labels = tail_labels.get(semi_value, [])
        tail_counter.update(labels)
        if len(labels) == 2:
            pair_counter.update([tuple(labels)])
        phase_counter.update([semi_value % modulus])
        for offset in range(-radius, radius + 1):
            if offset == 0:
                continue
            if wheel_allowed_offset(semi_value, offset, wheel_primes):
                allowed_offset_counter.update([offset])
                total_allowed_offsets += 1

    for prime_value in defect["neighbor_primes_sample"]:
        for semi_value in defect_semis:
            offset = prime_value - semi_value
            if abs(offset) <= radius:
                actual_edge_offset_counter.update([offset])
                total_actual_edges += 1

    span_left = min(interval[0] for interval in defect["neighbor_intervals"])
    span_right = max(interval[1] for interval in defect["neighbor_intervals"])
    left_index = bisect.bisect_left(prime_values, span_left)
    right_index = bisect.bisect_right(prime_values, span_right)
    previous_prime = prime_values[left_index - 1] if left_index > 0 else None
    next_prime = prime_values[right_index] if right_index < len(prime_values) else None
    max_tail_load = max(tail_counter.values(), default=0)
    max_phase_load = max(phase_counter.values(), default=0)
    max_allowed_offset_load = max(allowed_offset_counter.values(), default=0)
    tail_threshold = max(2, math.ceil(math.sqrt(len(defect_semis))))
    phase_threshold = tail_threshold
    exits = ["Endpoint-deficit"]
    if max_tail_load >= tail_threshold:
        exits.append("Tail-anchor-candidate")
    if max_phase_load >= phase_threshold or max_allowed_offset_load >= phase_threshold:
        exits.append("PDEC/fixed-offset-candidate")

    return {
        "p": p,
        "q": q,
        "row": row,
        "radius_kind": kind,
        "forced_radius": radius,
        "defect": {
            **defect,
            "semiprime_values_sample": defect_semis[:20],
            "q_square_mirror_span": [q * q - span_right, q * q - span_left],
        },
        "pressure": {
            "exit_candidates": exits,
            "tail_threshold": tail_threshold,
            "max_tail_load": max_tail_load,
            "max_pair_load": max(pair_counter.values(), default=0),
            "max_wheel_phase_load": max_phase_load,
            "max_allowed_offset_load": max_allowed_offset_load,
            "total_allowed_offsets": total_allowed_offsets,
            "total_actual_edges_in_sample": total_actual_edges,
            "previous_prime_gap": None if previous_prime is None else span_left - previous_prime,
            "next_prime_gap": None if next_prime is None else next_prime - span_right,
        },
        "top_tail_labels": [
            {"label": label, "load": load} for label, load in tail_counter.most_common(10)
        ],
        "top_tail_pairs": [
            {"labels": list(labels), "load": load} for labels, load in pair_counter.most_common(10)
        ],
        "top_wheel_phases": [
            {"residue": residue, "load": load} for residue, load in phase_counter.most_common(10)
        ],
        "top_allowed_offsets": [
            {
                "offset": offset,
                "load": load,
                "rho_z_offset": fixed_offset_ratio(offset, wheel_primes),
            }
            for offset, load in allowed_offset_counter.most_common(10)
        ],
        "top_actual_edge_offsets": [
            {
                "offset": offset,
                "load": load,
                "rho_z_offset": fixed_offset_ratio(offset, wheel_primes),
            }
            for offset, load in actual_edge_offset_counter.most_common(10)
        ],
    }


def write_markdown(result: dict, path: Path) -> None:
    """写 Markdown 审计报告。"""
    params = result["parameters"]
    summary = result["summary"]
    lines = [
        "# WSH-Hall 缺陷解剖审计",
        "",
        "**状态：** `forced_defect_anatomy_not_global_proof`",
        "",
        "本文档故意把已知可匹配行的半径压到最小 Hall 半径以下，观察缺陷如何显形。目标是为全局证明准备三出口模板：端点素数亏损、尾标签集中、轮筛/固定偏移相位集中。",
        "",
        "## 参数",
        "",
        f"- `source_certificate`: `{params['source_certificate']}`",
        f"- `max_records`: `{params['max_records']}`",
        f"- `wheel_primes`: `{params['wheel_primes']}`",
        "",
        "## 摘要",
        "",
        f"- 输入证书行数：`{summary['input_certificate_rows']}`。",
        f"- 分析行数：`{summary['analyzed_rows']}`。",
        f"- 强制半径场景数：`{summary['forced_radius_scenarios']}`。",
        f"- 找到 Hall 缺陷数：`{summary['defect_records']}`。",
        f"- 最大缺陷超额：`{summary['max_excess']}`。",
        f"- 最大尾标签负载：`{summary['max_tail_load']}`。",
        f"- 最大轮筛相位负载：`{summary['max_wheel_phase_load']}`。",
        f"- 最大允许偏移负载：`{summary['max_allowed_offset_load']}`。",
        "",
        "## 最大缺陷样本",
        "",
        "| p | q | row | kind | R | semis | primes | excess | exits | mirror span |",
        "| ---: | ---: | ---: | --- | ---: | ---: | ---: | ---: | --- | --- |",
    ]
    for record in result["defect_records"][:30]:
        defect = record["defect"]
        pressure = record["pressure"]
        lines.append(
            "| {p} | {q} | {row} | {kind} | {radius} | {semis} | {primes} | {excess} | {exits} | {mirror} |".format(
                p=record["p"],
                q=record["q"],
                row=record["row"],
                kind=record["radius_kind"],
                radius=record["forced_radius"],
                semis=defect["semiprime_count"],
                primes=defect["prime_count"],
                excess=defect["excess"],
                exits=",".join(pressure["exit_candidates"]),
                mirror=defect["q_square_mirror_span"],
            )
        )
    lines.extend(
        [
            "",
            "## 结构解释",
            "",
            "一维 Hall 失败不是抽象坏事件：它必然给出连续半素数块 `B`，其半径邻域 `N_R(B)` 中素数数量小于 `|B|`。这已经是端点素数亏损。若同一块中尾标签或尾因子对负载过高，则它进入 Tail-anchor；若块集中在少数小轮相位或依赖少数固定偏移通道，则进入 PDEC/固定偏移 CRT 缺陷。",
            "",
            "镜像列 `q^2-n` 在报告中作为 `q_square_mirror_span` 记录。它不把缺陷变成更小方阵零行，但把终端缺陷转成早期非零类块，供端点/PDEC 分支使用。这是当前路线中可用的镜像关系，不能误用为短周期复现。",
            "",
            "## 下一步严格目标",
            "",
            "把本审计中的观察升级为定理时，必须证明：任意正式反例诱导的 Hall 缺陷块，要么满足显式尾标签负载阈值，要么满足显式固定偏移/轮筛相位负载阈值，要么端点素数亏损达到 PDEC 可吸收下界。有限样本只帮助确定证书字段和阈值形状。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def audit(args: argparse.Namespace) -> dict:
    """执行缺陷解剖审计。"""
    source_path = Path(args.source_certificate)
    source = json.loads(source_path.read_text(encoding="utf-8"))
    wheel_primes = [int(part) for part in args.wheel_primes.split(",") if part]
    rows = source["certificate_rows"][: args.max_records]
    max_p = max(row["p"] for row in rows)
    is_prime = sieve_bool(max_p * max_p + max_p * 20 + 10000)
    prime_values = primes_from_table(is_prime)
    rows_by_prime: dict[int, list[dict]] = defaultdict(list)
    for row in rows:
        rows_by_prime[row["p"]].append(row)

    defect_records = []
    forced_radius_scenarios = 0
    for base_prime, certificate_rows in rows_by_prime.items():
        q, tail_labels, primes_by_row, semis_by_row = row_data_for_prime(
            base_prime,
            is_prime,
            prime_values,
            source["parameters"]["y_ratio"],
        )
        for certificate_row in certificate_rows:
            row_number = certificate_row["row"]
            semiprimes = semis_by_row[row_number]
            row_primes = primes_by_row[row_number]
            for radius_spec in chosen_radii(certificate_row["matching_radius"]):
                forced_radius_scenarios += 1
                record = analyze_defect(
                    base_prime,
                    q,
                    row_number,
                    semiprimes,
                    row_primes,
                    tail_labels,
                    radius_spec["radius"],
                    radius_spec["kind"],
                    wheel_primes,
                )
                if record is not None:
                    defect_records.append(record)

    defect_records.sort(
        key=lambda item: (
            item["defect"]["excess"],
            item["defect"]["semiprime_count"],
            item["pressure"]["max_tail_load"],
            item["pressure"]["max_allowed_offset_load"],
        ),
        reverse=True,
    )
    summary = {
        "input_certificate_rows": len(source["certificate_rows"]),
        "analyzed_rows": len(rows),
        "forced_radius_scenarios": forced_radius_scenarios,
        "defect_records": len(defect_records),
        "max_excess": max((item["defect"]["excess"] for item in defect_records), default=0),
        "max_tail_load": max(
            (item["pressure"]["max_tail_load"] for item in defect_records),
            default=0,
        ),
        "max_wheel_phase_load": max(
            (item["pressure"]["max_wheel_phase_load"] for item in defect_records),
            default=0,
        ),
        "max_allowed_offset_load": max(
            (item["pressure"]["max_allowed_offset_load"] for item in defect_records),
            default=0,
        ),
    }
    return {
        "parameters": {
            "source_certificate": args.source_certificate,
            "max_records": args.max_records,
            "wheel_primes": wheel_primes,
        },
        "summary": summary,
        "defect_records": defect_records,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source-certificate",
        default="docs/monograph/prime-matrix-wsh-hall-phase-certificate.json",
    )
    parser.add_argument("--max-records", type=int, default=44)
    parser.add_argument("--wheel-primes", default="2,3,5,7,11,13")
    parser.add_argument(
        "--out-prefix",
        default="docs/monograph/prime-matrix-wsh-hall-defect-anatomy",
    )
    args = parser.parse_args()
    result = audit(args)
    out_prefix = Path(args.out_prefix)
    out_prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, out_prefix.with_suffix(".md"))
    print(json.dumps(result["summary"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
