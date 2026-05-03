#!/usr/bin/env python3
"""生成 WSH-Hall/PDEC 的有限相位证书。

用法示例：
  python3 experiments/prime_matrix_wsh_hall_phase_certificate.py --max-p 1000
  python3 experiments/prime_matrix_wsh_hall_phase_certificate.py --max-p 2000 --rows-per-class 20

证书目标：
  1. 对 Distributed-RCI 中的平衡双尾半素数行计算局部 Hall 最小匹配半径；
  2. 对最紧行物化“半素数 -> 附近素数”的匹配对；
  3. 检查每个匹配偏移满足小素数轮筛允许条件；
  4. 输出固定偏移负载和轮筛相位负载，供 PDEC/Tail-anchor 分支审查。

注意：这是有限材料化证书，不是 WSH-Hall 的全局证明。
"""

from __future__ import annotations

import argparse
import bisect
import json
import math
from collections import Counter, defaultdict
from pathlib import Path
from typing import Iterable


def sieve_bool(limit_value: int) -> bytearray:
    """返回 `0..limit_value` 的素数布尔表。"""
    is_prime = bytearray(b"\x01") * (limit_value + 1)
    if limit_value >= 0:
        is_prime[0] = 0
    if limit_value >= 1:
        is_prime[1] = 0
    for divisor in range(2, int(limit_value**0.5) + 1):
        if is_prime[divisor]:
            start_value = divisor * divisor
            is_prime[start_value : limit_value + 1 : divisor] = b"\x00" * (
                ((limit_value - start_value) // divisor) + 1
            )
    return is_prime


def primes_from_table(is_prime: bytearray) -> list[int]:
    """从布尔表提取素数列表。"""
    return [number for number, flag in enumerate(is_prime) if flag]


def next_prime_after(base_prime: int, primes: list[int]) -> int:
    """返回严格大于 `base_prime` 的下一素数。"""
    for prime_value in primes:
        if prime_value > base_prime:
            return prime_value
    raise ValueError("素数表范围不足，无法找到下一素数")


def build_tail_data(
    next_base: int,
    low_primes: list[int],
    tail_primes: list[int],
) -> tuple[bytearray, bytearray, dict[int, list[int]]]:
    """构造低筛骨架、尾素数命中重数和尾标签。"""
    next_square = next_base * next_base
    low_rough = bytearray(b"\x01") * (next_square + 1)
    low_rough[0] = 0
    low_rough[1] = 0
    low_rough[next_square] = 0
    for low_prime in low_primes:
        low_rough[0 : next_square + 1 : low_prime] = b"\x00" * (
            (next_square // low_prime) + 1
        )

    tail_omega = bytearray(next_square + 1)
    tail_labels: dict[int, list[int]] = {}
    for tail_prime in tail_primes:
        for position in range(tail_prime, next_square + 1, tail_prime):
            if not low_rough[position]:
                continue
            tail_omega[position] += 1
            tail_labels.setdefault(position, []).append(tail_prime)
    return low_rough, tail_omega, tail_labels


def collect_rows(
    next_base: int,
    low_rough: bytearray,
    tail_omega: bytearray,
    tail_labels: dict[int, list[int]],
    is_prime: bytearray,
) -> tuple[list[list[int]], list[list[int]], int]:
    """按 `next_base` 宽度收集无尾素数和平衡双尾半素数。"""
    primes_by_row: list[list[int]] = [[] for _ in range(next_base + 1)]
    semis_by_row: list[list[int]] = [[] for _ in range(next_base + 1)]
    prime_verification_failures = 0
    for number in range(2, next_base * next_base):
        if not low_rough[number]:
            continue
        row_number = (number - 1) // next_base + 1
        omega_value = tail_omega[number]
        if omega_value == 0:
            primes_by_row[row_number].append(number)
            if not is_prime[number]:
                prime_verification_failures += 1
        elif omega_value == 2:
            labels = tail_labels[number]
            if labels[0] * labels[1] == number:
                semis_by_row[row_number].append(number)
    return primes_by_row, semis_by_row, prime_verification_failures


def greedy_match(
    semiprimes: list[int],
    prime_values: list[int],
    radius: int,
) -> list[tuple[int, int]] | None:
    """在给定半径内执行一维 Hall 贪心匹配。"""
    matched_pairs: list[tuple[int, int]] = []
    prime_index = 0
    for semi_value in semiprimes:
        lower_bound = semi_value - radius
        upper_bound = semi_value + radius
        while prime_index < len(prime_values) and prime_values[prime_index] < lower_bound:
            prime_index += 1
        if prime_index >= len(prime_values) or prime_values[prime_index] > upper_bound:
            return None
        matched_pairs.append((semi_value, prime_values[prime_index]))
        prime_index += 1
    return matched_pairs


def min_matching_radius(semiprimes: list[int], prime_values: list[int]) -> int | None:
    """计算半素数到同一行素数的一维最小最大匹配半径。"""
    if not semiprimes:
        return 0
    if len(semiprimes) > len(prime_values):
        return None
    lower_radius = 0
    upper_radius = max(
        abs(semiprimes[0] - prime_values[-1]),
        abs(semiprimes[-1] - prime_values[0]),
    )
    while lower_radius < upper_radius:
        mid_radius = (lower_radius + upper_radius) // 2
        if greedy_match(semiprimes, prime_values, mid_radius) is not None:
            upper_radius = mid_radius
        else:
            lower_radius = mid_radius + 1
    return lower_radius


def hall_defect_interval(
    semiprimes: list[int],
    prime_values: list[int],
    radius: int,
) -> dict | None:
    """若给定半径匹配失败，寻找一个连续 Hall 缺陷区间。"""
    if greedy_match(semiprimes, prime_values, radius) is not None:
        return None
    best_defect: dict | None = None
    for start_index, start_value in enumerate(semiprimes):
        interval_left = start_value - radius
        for end_index in range(start_index, len(semiprimes)):
            interval_right = semiprimes[end_index] + radius
            semi_count = end_index - start_index + 1
            prime_count = bisect.bisect_right(prime_values, interval_right) - bisect.bisect_left(
                prime_values, interval_left
            )
            excess = semi_count - prime_count
            if excess <= 0:
                continue
            candidate = {
                "semi_index_range": [start_index, end_index],
                "interval": [interval_left, interval_right],
                "semiprime_count": semi_count,
                "prime_count": prime_count,
                "excess": excess,
            }
            if best_defect is None or candidate["excess"] > best_defect["excess"]:
                best_defect = candidate
    return best_defect


def wheel_modulus(wheel_primes: Iterable[int]) -> int:
    """计算轮筛模数。"""
    modulus = 1
    for wheel_prime in wheel_primes:
        modulus *= wheel_prime
    return modulus


def wheel_allowed_offset(
    semi_value: int,
    offset_value: int,
    wheel_primes: list[int],
) -> bool:
    """检查偏移是否避开所有小素数给出的禁同余类。"""
    return all((semi_value + offset_value) % wheel_prime != 0 for wheel_prime in wheel_primes)


def fixed_offset_ratio(offset_value: int, wheel_primes: list[int]) -> float:
    """固定偏移在小素数轮中同时保持双单位的理论比例。"""
    ratio = 1.0
    for wheel_prime in wheel_primes:
        if offset_value % wheel_prime == 0:
            continue
        ratio *= (wheel_prime - 2) / (wheel_prime - 1)
    return ratio


def min_allowed_abs_offset(
    semi_value: int,
    radius: int,
    wheel_primes: list[int],
) -> int | None:
    """计算轮筛在给定半径内允许的最小非零绝对偏移。"""
    for distance in range(1, radius + 1):
        if wheel_allowed_offset(semi_value, -distance, wheel_primes):
            return distance
        if wheel_allowed_offset(semi_value, distance, wheel_primes):
            return distance
    return None


def phase_loads(values: list[int], modulus: int, limit: int) -> list[dict]:
    """返回模 `modulus` 的最高负载相位。"""
    residue_counter = Counter(value % modulus for value in values)
    return [
        {"residue": residue, "load": load}
        for residue, load in residue_counter.most_common(limit)
    ]


def summarize_matching_pairs(
    matched_pairs: list[tuple[int, int]],
    tail_labels: dict[int, list[int]],
    wheel_primes: list[int],
    pair_limit: int,
) -> tuple[list[dict], list[dict], bool]:
    """汇总匹配对和固定偏移负载。"""
    pair_rows = []
    offset_counter: Counter[int] = Counter()
    all_wheel_allowed = True
    for semi_value, prime_value in matched_pairs:
        offset_value = prime_value - semi_value
        allowed = wheel_allowed_offset(semi_value, offset_value, wheel_primes)
        all_wheel_allowed = all_wheel_allowed and allowed
        offset_counter[offset_value] += 1
        if len(pair_rows) < pair_limit:
            pair_rows.append(
                {
                    "semiprime": semi_value,
                    "tail_labels": tail_labels.get(semi_value, []),
                    "matched_prime": prime_value,
                    "offset": offset_value,
                    "wheel_allowed": allowed,
                    "rho_z_offset": fixed_offset_ratio(offset_value, wheel_primes),
                }
            )
    fixed_offset_loads = [
        {
            "offset": offset_value,
            "load": load,
            "rho_z_offset": fixed_offset_ratio(offset_value, wheel_primes),
        }
        for offset_value, load in offset_counter.most_common()
    ]
    return pair_rows, fixed_offset_loads, all_wheel_allowed


def scan_rows(
    max_prime: int,
    min_prime: int,
    y_ratio: float,
    candidate_radius_factor: float,
) -> tuple[dict, list[dict], bytearray, list[int]]:
    """扫描全部目标行，返回汇总与行级概要。"""
    sieve_limit = max_prime * max_prime + max_prime * 20 + 10000
    is_prime = sieve_bool(sieve_limit)
    prime_values = primes_from_table(is_prime)
    target_primes = [prime_value for prime_value in prime_values if min_prime <= prime_value <= max_prime]

    row_summaries: list[dict] = []
    prime_verification_failures = 0

    for base_prime in target_primes:
        next_base = next_prime_after(base_prime, prime_values)
        y_cutoff = max(2, int(math.floor(y_ratio * base_prime)))
        low_primes = [prime_value for prime_value in prime_values if prime_value <= y_cutoff]
        tail_primes = [prime_value for prime_value in prime_values if y_cutoff < prime_value <= base_prime]
        low_rough, tail_omega, tail_labels = build_tail_data(next_base, low_primes, tail_primes)
        primes_by_row, semis_by_row, local_prime_failures = collect_rows(
            next_base,
            low_rough,
            tail_omega,
            tail_labels,
            is_prime,
        )
        prime_verification_failures += local_prime_failures
        candidate_radius = math.ceil(candidate_radius_factor * math.log(next_base) ** 2)
        for row_number in range(1, next_base + 1):
            semiprimes = semis_by_row[row_number]
            if not semiprimes:
                continue
            row_primes = primes_by_row[row_number]
            matching_radius = min_matching_radius(semiprimes, row_primes)
            row_ratio = len(semiprimes) / len(row_primes) if row_primes else float("inf")
            row_summaries.append(
                {
                    "p": base_prime,
                    "q": next_base,
                    "y": y_cutoff,
                    "row": row_number,
                    "row_interval": [(row_number - 1) * next_base + 1, row_number * next_base],
                    "prime_count": len(row_primes),
                    "balanced_semiprime_count": len(semiprimes),
                    "semiprime_to_prime_ratio": row_ratio,
                    "matching_radius": matching_radius,
                    "candidate_radius": candidate_radius,
                    "candidate_pass": (
                        matching_radius is not None and matching_radius <= candidate_radius
                    ),
                    "prime_minus_semiprime_margin": len(row_primes) - len(semiprimes),
                }
            )

    finite_rows = [row for row in row_summaries if row["matching_radius"] is not None]
    for row in finite_rows:
        log_next = math.log(row["q"])
        row["radius_over_log2_q"] = row["matching_radius"] / (log_next * log_next)

    summary = {
        "prime_record_count": len(target_primes),
        "row_with_semiprime_count": len(row_summaries),
        "matching_failure_rows": sum(1 for row in row_summaries if row["matching_radius"] is None),
        "candidate_radius_failure_rows": sum(1 for row in row_summaries if not row["candidate_pass"]),
        "prime_verification_failures": prime_verification_failures,
        "global_min_prime_minus_semiprime_margin": min(
            (row["prime_minus_semiprime_margin"] for row in row_summaries),
            default=0,
        ),
        "global_max_matching_radius": max(
            (row["matching_radius"] for row in finite_rows),
            default=0,
        ),
        "global_max_radius_over_log2_q": max(
            (row["radius_over_log2_q"] for row in finite_rows),
            default=0,
        ),
        "global_max_semiprime_ratio": max(
            (row["semiprime_to_prime_ratio"] for row in row_summaries),
            default=0,
        ),
    }
    return summary, row_summaries, is_prime, prime_values


def select_certificate_keys(row_summaries: list[dict], rows_per_class: int) -> list[tuple[int, int]]:
    """选出最大半径、最大比例和候选失败行作为证书行。"""
    selected: dict[tuple[int, int], None] = {}
    finite_rows = [row for row in row_summaries if row["matching_radius"] is not None]
    candidate_failures = [row for row in row_summaries if not row["candidate_pass"]]
    selection_groups = [
        sorted(finite_rows, key=lambda item: item["matching_radius"], reverse=True),
        sorted(finite_rows, key=lambda item: item["radius_over_log2_q"], reverse=True),
        sorted(row_summaries, key=lambda item: item["semiprime_to_prime_ratio"], reverse=True),
        candidate_failures,
    ]
    for group in selection_groups:
        for row in group[:rows_per_class]:
            selected[(row["p"], row["row"])] = None
    return list(selected.keys())


def build_certificate_rows(
    selected_keys: list[tuple[int, int]],
    row_summaries: list[dict],
    is_prime: bytearray,
    prime_values: list[int],
    y_ratio: float,
    wheel_primes: list[int],
    pair_limit: int,
) -> list[dict]:
    """对选中行生成相位证书。"""
    summary_by_key = {(row["p"], row["row"]): row for row in row_summaries}
    rows_by_prime: dict[int, list[int]] = defaultdict(list)
    for base_prime, row_number in selected_keys:
        rows_by_prime[base_prime].append(row_number)

    certificates: list[dict] = []
    modulus = wheel_modulus(wheel_primes)
    for base_prime in sorted(rows_by_prime):
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
        for row_number in sorted(rows_by_prime[base_prime]):
            row_summary = summary_by_key[(base_prime, row_number)]
            semiprimes = semis_by_row[row_number]
            row_primes = primes_by_row[row_number]
            matching_radius = row_summary["matching_radius"]
            matched_pairs = (
                None
                if matching_radius is None
                else greedy_match(semiprimes, row_primes, matching_radius)
            )
            if matched_pairs is None:
                pair_rows: list[dict] = []
                fixed_offset_loads: list[dict] = []
                all_wheel_allowed = False
            else:
                pair_rows, fixed_offset_loads, all_wheel_allowed = summarize_matching_pairs(
                    matched_pairs,
                    tail_labels,
                    wheel_primes,
                    pair_limit,
                )
            min_allowed_offsets = [
                min_allowed_abs_offset(semi_value, row_summary["candidate_radius"], wheel_primes)
                for semi_value in semiprimes
            ]
            certificates.append(
                {
                    **row_summary,
                    "wheel_modulus": modulus,
                    "all_pairs_wheel_allowed": all_wheel_allowed,
                    "semiprime_phase_loads": phase_loads(semiprimes, modulus, 12),
                    "prime_phase_loads": phase_loads(row_primes, modulus, 12),
                    "fixed_offset_loads": fixed_offset_loads[:12],
                    "matching_pairs_sample": pair_rows,
                    "matching_pair_count": 0 if matched_pairs is None else len(matched_pairs),
                    "min_wheel_allowed_abs_offset_min": min(
                        (value for value in min_allowed_offsets if value is not None),
                        default=None,
                    ),
                    "min_wheel_allowed_abs_offset_max": max(
                        (value for value in min_allowed_offsets if value is not None),
                        default=None,
                    ),
                    "candidate_hall_defect": hall_defect_interval(
                        semiprimes,
                        row_primes,
                        row_summary["candidate_radius"],
                    ),
                }
            )
    return certificates


def write_markdown(result: dict, output_path: Path) -> None:
    """写入 Markdown 证书报告。"""
    parameters = result["parameters"]
    summary = result["summary"]
    certificate_rows = result["certificate_rows"]
    lines = [
        "# WSH-Hall 相位证书",
        "",
        "**状态：** `finite_phase_certificate_not_global_proof`",
        "",
        "本文档把 `Distributed-RCI => WSH-Hall/PDEC` 的最窄接口物化为有限相位证书。它只说明指定范围内的最紧样本满足轮筛允许的局部 Hall 匹配；全局证明仍需证明该结构在无限族中持续成立，或证明失败必进入 `PDEC/Tail-anchor/Endpoint` 出口。",
        "",
        "## 参数",
        "",
        f"- `max_p`: `{parameters['max_p']}`",
        f"- `min_p`: `{parameters['min_p']}`",
        f"- `y_ratio`: `{parameters['y_ratio']}`",
        f"- `candidate_radius_factor`: `{parameters['candidate_radius_factor']}`",
        f"- `wheel_primes`: `{parameters['wheel_primes']}`",
        f"- `rows_per_class`: `{parameters['rows_per_class']}`",
        "",
        "## 全量扫描摘要",
        "",
        f"- 检查素数记录数：`{summary['prime_record_count']}`。",
        f"- 含平衡半素数的行数：`{summary['row_with_semiprime_count']}`。",
        f"- 完全匹配失败行数：`{summary['matching_failure_rows']}`。",
        f"- 候选半径失败行数：`{summary['candidate_radius_failure_rows']}`。",
        f"- 无尾项素性核验失败数：`{summary['prime_verification_failures']}`。",
        f"- 最小 `prime_count-semi_count`：`{summary['global_min_prime_minus_semiprime_margin']}`。",
        f"- 最大最小匹配半径：`{summary['global_max_matching_radius']}`。",
        f"- 最大 `radius/log²(q)`：`{summary['global_max_radius_over_log2_q']}`。",
        f"- 最大半素数/素数比值：`{summary['global_max_semiprime_ratio']}`。",
        "",
        "## 证书行",
        "",
        "| p | q | row | primes | semis | ratio | min radius | R/log²q | candidate R | wheel ok | interval |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |",
    ]
    for row in certificate_rows:
        lines.append(
            "| {p} | {q} | {row_num} | {prime_count} | {semi_count} | {ratio:.6f} | {radius} | {rlog:.6f} | {candidate} | {wheel_ok} | {interval} |".format(
                p=row["p"],
                q=row["q"],
                row_num=row["row"],
                prime_count=row["prime_count"],
                semi_count=row["balanced_semiprime_count"],
                ratio=row["semiprime_to_prime_ratio"],
                radius=row["matching_radius"],
                rlog=row.get("radius_over_log2_q", 0.0),
                candidate=row["candidate_radius"],
                wheel_ok=row["all_pairs_wheel_allowed"],
                interval=row["row_interval"],
            )
        )
    lines.extend(
        [
            "",
            "## 固定偏移负载样本",
            "",
            "每行只列最高负载偏移。`rho_z(d)` 是固定偏移在小素数轮中保持双单位的理论比例；它用于发现相位超载，而不是单独构成全局证明。",
            "",
            "| p | row | top offsets `(d:load;rho)` | min/max wheel-only offset |",
            "| ---: | ---: | --- | --- |",
        ]
    )
    for row in certificate_rows[:20]:
        offset_text = ", ".join(
            f"{item['offset']}:{item['load']};{item['rho_z_offset']:.6f}"
            for item in row["fixed_offset_loads"][:6]
        )
        min_max = "{}/{}".format(
            row["min_wheel_allowed_abs_offset_min"],
            row["min_wheel_allowed_abs_offset_max"],
        )
        lines.append(f"| {row['p']} | {row['row']} | {offset_text} | {min_max} |")
    lines.extend(
        [
            "",
            "## 审稿解释",
            "",
            "本证书补上的不是新的全局筛定理，而是一个可复核的接口：在所有扫描行中，平衡双尾半素数到同一行素数的 Hall 匹配存在；在最紧样本中，实际匹配偏移逐项满足轮筛允许条件。若未来全局证明中某行无法匹配，则脚本会输出 Hall 缺陷区间，该区间正是 `PDEC/Tail-anchor/Endpoint` 分支需要吸收的对象。",
            "",
            "因此最新硬点应表述为：证明 `WSH-Hall` 在一般行中成立，或证明任一 Hall 缺陷必然产生持久相位缺陷、尾因子集中或端点素数亏损。当前文件只固定有限证书与失败出口格式。",
        ]
    )
    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def audit(args: argparse.Namespace) -> dict:
    """执行完整审计并返回结果。"""
    wheel_primes = [int(part) for part in args.wheel_primes.split(",") if part]
    summary, row_summaries, is_prime, prime_values = scan_rows(
        args.max_p,
        args.min_p,
        args.y_ratio,
        args.candidate_radius_factor,
    )
    selected_keys = select_certificate_keys(row_summaries, args.rows_per_class)
    certificate_rows = build_certificate_rows(
        selected_keys,
        row_summaries,
        is_prime,
        prime_values,
        args.y_ratio,
        wheel_primes,
        args.pair_sample_limit,
    )
    certificate_rows.sort(
        key=lambda row: (
            row["matching_radius"] if row["matching_radius"] is not None else math.inf,
            row["semiprime_to_prime_ratio"],
        ),
        reverse=True,
    )
    return {
        "parameters": {
            "max_p": args.max_p,
            "min_p": args.min_p,
            "y_ratio": args.y_ratio,
            "candidate_radius_factor": args.candidate_radius_factor,
            "wheel_primes": wheel_primes,
            "rows_per_class": args.rows_per_class,
            "pair_sample_limit": args.pair_sample_limit,
        },
        "summary": summary,
        "certificate_rows": certificate_rows,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-p", type=int, default=2000)
    parser.add_argument("--min-p", type=int, default=17)
    parser.add_argument("--y-ratio", type=float, default=1 / math.e)
    parser.add_argument("--candidate-radius-factor", type=float, default=3.0)
    parser.add_argument("--wheel-primes", default="2,3,5,7,11,13")
    parser.add_argument("--rows-per-class", type=int, default=20)
    parser.add_argument("--pair-sample-limit", type=int, default=40)
    parser.add_argument(
        "--out-prefix",
        default="docs/monograph/prime-matrix-wsh-hall-phase-certificate",
    )
    args = parser.parse_args()
    result = audit(args)
    output_prefix = Path(args.out_prefix)
    output_prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, output_prefix.with_suffix(".md"))
    print(json.dumps(result["summary"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
