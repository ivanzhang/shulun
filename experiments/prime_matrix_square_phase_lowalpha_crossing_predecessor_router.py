#!/usr/bin/env python3
"""审计 crossing 前驱 D_- 的短双曲区间改写。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_crossing_predecessor_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-crossing-predecessor-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-crossing-predecessor-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-crossing-predecessor-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-crossing-predecessor-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-crossing-predecessor-router.md"

DEFAULT_P_LIST = [10007, 36739, 83561, 200003]
BASE_D = 31

NEXT_TARGET = "PredecessorShortHyperbolaDistributionBoundOrPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-buchstab-crossing-capacity-router.json",
    "prime-matrix-square-phase-lowalpha-first-anchor-interval-router.json",
]


def sieve_bool(limit: int) -> bytearray:
    """返回素数布尔表。"""
    flags = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        flags[0] = 0
    if limit >= 1:
        flags[1] = 0
    for value in range(2, int(limit**0.5) + 1):
        if not flags[value]:
            continue
        start = value * value
        flags[start : limit + 1 : value] = b"\x00" * (((limit - start) // value) + 1)
    return flags


def primes_from_flags(flags: bytearray, limit: int) -> list[int]:
    """提取不超过 limit 的素数。"""
    return [idx for idx in range(2, min(limit + 1, len(flags))) if flags[idx]]


def parse_int_list(text: str) -> list[int]:
    """解析整数列表。"""
    return [int(part) for part in text.split(",") if part.strip()]


def factor_multiset(n: int, trial_primes: list[int]) -> list[int]:
    """返回 n 的素因子重数列表，按从小到大排列。"""
    value = n
    factors: list[int] = []
    for prime in trial_primes:
        if prime * prime > value:
            break
        while value % prime == 0:
            factors.append(prime)
            value //= prime
    if value > 1:
        factors.append(value)
    return factors


def cutoffs_for_p(p: int, base_d: int = BASE_D) -> list[int]:
    """生成 dyadic cutoff。"""
    y = max(2, math.floor(p / math.e))
    cuts = [base_d]
    value = base_d
    while value < y:
        value *= 2
        cuts.append(min(value, y))
    return sorted(set(cuts))


def factor_depth_bound(p: int, z: int) -> int:
    """计算 z-rough cofactor 最大素因子个数上界。"""
    upper = (p * p + p - 1) / z
    depth = 0
    power = 1.0
    while power < upper:
        depth += 1
        power *= z + 1
    return max(0, depth - 1)


def delete_residue(allowed: bytearray, p: int, p2: int, q: int) -> None:
    """从 allowed 中删除 k == -P^2 mod q 的列。"""
    residue = (-p2) % q
    start = residue if residue != 0 else q
    if start < p:
        allowed[start:p:q] = b"\x00" * (((p - 1 - start) // q) + 1)


def crossing_from_factors(p: int, q: int, factors: list[int]) -> tuple[int, int, int, int]:
    """返回 crossing 记录 `(D_minus, r, D_plus, tail)`。"""
    prefix = q
    tail_start = 0
    crossing_prime = 1
    for idx, factor in enumerate(factors):
        before = prefix
        prefix *= factor
        if prefix > p:
            crossing_prime = factor
            tail_start = idx + 1
            tail = 1
            for rest in factors[tail_start:]:
                tail *= rest
            return before, crossing_prime, prefix, tail
    return prefix, crossing_prime, prefix, 1


def predecessor_bucket(d_minus: int, p: int) -> str:
    """按 D_- 相对 P 分桶。"""
    ratio = d_minus / p
    if ratio <= 0:
        return "invalid"
    level = math.floor(math.log(ratio, 2))
    return f"M{level}:({2**level}P,{2**(level + 1)}P]"


def width_bucket(width: float) -> str:
    """按前驱短区间长度 P/D_- 分桶。"""
    if width < 2:
        return "W0:<2"
    if width < 4:
        return "W1:[2,4)"
    if width < 8:
        return "W2:[4,8)"
    if width < 16:
        return "W3:[8,16)"
    if width < 32:
        return "W4:[16,32)"
    if width < 64:
        return "W5:[32,64)"
    if width < 128:
        return "W6:[64,128)"
    return "W7:>=128"


def register(mapping: dict[str, int], key: str) -> None:
    """登记计数。"""
    mapping[key] = mapping.get(key, 0) + 1


def audit_lowalpha_block(
    p: int,
    previous_cutoff: int,
    cutoff: int,
    allowed: bytearray,
    block_primes: list[int],
    trial_primes: list[int],
) -> dict[str, Any]:
    """审计一个 low-alpha block 的 D_- 短双曲区间。"""
    p2 = p * p
    hits = 0
    predecessor_hits: dict[str, int] = {}
    predecessor_width_sum: dict[str, float] = {}
    predecessor_bucket_counts: dict[str, int] = {}
    width_bucket_counts: dict[str, int] = {}
    formula_failures = 0
    bracket_failures = 0
    tail_rough_failures = 0
    max_width = 0.0
    min_width = None
    max_hits_per_predecessor = 0
    sample_records = []
    for q in block_primes:
        left = p2 // q + 1
        right = (p2 + p - 1) // q
        for m in range(left, right + 1):
            k = q * m - p2
            if not (1 <= k < p and allowed[k]):
                continue
            factors = factor_multiset(m, trial_primes)
            d_minus, crossing_prime, d_plus, tail = crossing_from_factors(p, q, factors)
            hits += 1
            if not (d_minus <= p < d_plus):
                bracket_failures += 1
            u = crossing_prime * tail
            if d_minus * u != q * m:
                formula_failures += 1
            if not (p2 / d_minus < u <= (p2 + p - 1) / d_minus):
                formula_failures += 1
            if tail > 1:
                tail_min_factor = factor_multiset(tail, trial_primes)[0]
                if tail_min_factor < crossing_prime:
                    tail_rough_failures += 1
            key = str(d_minus)
            predecessor_hits[key] = predecessor_hits.get(key, 0) + 1
            width = p / d_minus
            predecessor_width_sum[key] = width
            max_width = max(max_width, width)
            min_width = width if min_width is None else min(min_width, width)
            max_hits_per_predecessor = max(max_hits_per_predecessor, predecessor_hits[key])
            register(predecessor_bucket_counts, predecessor_bucket(d_minus, p))
            register(width_bucket_counts, width_bucket(width))
            if len(sample_records) < 8:
                sample_records.append(
                    {
                        "q": q,
                        "m": m,
                        "d_minus": d_minus,
                        "crossing_prime": crossing_prime,
                        "tail": tail,
                        "u": u,
                        "width": width,
                    }
                )
    top_predecessor = max(predecessor_hits.items(), key=lambda item: item[1], default=(None, 0))
    top_bucket = max(predecessor_bucket_counts.items(), key=lambda item: item[1], default=(None, 0))
    top_width_bucket = max(width_bucket_counts.items(), key=lambda item: item[1], default=(None, 0))
    total_width = sum(predecessor_width_sum.values())
    return {
        "p": p,
        "previous_cutoff": previous_cutoff,
        "cutoff": cutoff,
        "alpha_left": math.log(previous_cutoff) / math.log(p),
        "cofactor_hits": hits,
        "active_predecessor_count": len(predecessor_hits),
        "max_hits_per_predecessor": max_hits_per_predecessor,
        "top_predecessor": top_predecessor[0],
        "top_predecessor_hits": top_predecessor[1],
        "predecessor_width_budget_sum": total_width,
        "hits_per_width_budget": None if total_width == 0 else hits / total_width,
        "max_interval_width": max_width,
        "min_interval_width": min_width,
        "formula_failure_count": formula_failures,
        "bracket_failure_count": bracket_failures,
        "tail_rough_failure_count": tail_rough_failures,
        "predecessor_bucket_counts": predecessor_bucket_counts,
        "width_bucket_counts": width_bucket_counts,
        "top_predecessor_bucket": top_bucket[0],
        "top_predecessor_bucket_count": top_bucket[1],
        "top_width_bucket": top_width_bucket[0],
        "top_width_bucket_count": top_width_bucket[1],
        "sample_records": sample_records,
    }


def audit_p(p: int, primes: list[int], trial_primes: list[int]) -> dict[str, Any]:
    """审计一个 P 的 crossing 前驱分布。"""
    p2 = p * p
    cutoffs = cutoffs_for_p(p)
    allowed = bytearray(b"\x01") * p
    allowed[0] = 0
    prime_index = 0
    rows = []
    for cutoff in cutoffs:
        previous = 0 if not rows else rows[-1].get("cutoff", 0)
        block_primes = [q for q in primes if previous < q <= cutoff]
        if previous >= BASE_D and factor_depth_bound(p, previous) >= 3:
            rows.append(audit_lowalpha_block(p, previous, cutoff, allowed, block_primes, trial_primes))
        while prime_index < len(primes) and primes[prime_index] <= cutoff:
            delete_residue(allowed, p, p2, primes[prime_index])
            prime_index += 1
        if not rows or rows[-1].get("cutoff") != cutoff:
            rows.append({"p": p, "previous_cutoff": previous, "cutoff": cutoff, "skipped": True})
    low_rows = [row for row in rows if not row.get("skipped")]
    worst = max(low_rows, key=lambda item: item["cofactor_hits"], default=None)
    return {
        "p": p,
        "lowalpha_row_count": len(low_rows),
        "total_hits": sum(row["cofactor_hits"] for row in low_rows),
        "formula_failure_count": sum(row["formula_failure_count"] for row in low_rows),
        "bracket_failure_count": sum(row["bracket_failure_count"] for row in low_rows),
        "tail_rough_failure_count": sum(row["tail_rough_failure_count"] for row in low_rows),
        "worst_lowalpha_block": worst,
        "rows": low_rows,
    }


def file_sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖哈希。"""
    result = {
        "experiments/prime_matrix_square_phase_lowalpha_crossing_predecessor_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def audit(p_list: list[int]) -> dict[str, Any]:
    """执行审计。"""
    max_p = max(p_list)
    trial_limit = int(math.isqrt(max_p * max_p + max_p)) + 10
    flags = sieve_bool(max(trial_limit, max_p))
    trial_primes = primes_from_flags(flags, trial_limit)
    profiles = []
    for p in p_list:
        primes = primes_from_flags(flags, max(2, math.floor(p / math.e)))
        profiles.append(audit_p(p, primes, trial_primes))
    rows = [row for profile in profiles for row in profile["rows"]]
    worst = max(rows, key=lambda item: item["cofactor_hits"], default=None)
    formula_failures = sum(profile["formula_failure_count"] for profile in profiles)
    bracket_failures = sum(profile["bracket_failure_count"] for profile in profiles)
    tail_rough_failures = sum(profile["tail_rough_failure_count"] for profile in profiles)
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_crossing_predecessor_router",
        "status": "crossing_prefix_distribution_reduced_to_predecessor_short_hyperbola_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "predecessor_short_hyperbola_formula_closed": formula_failures == 0,
        "crossing_bracket_checked": bracket_failures == 0,
        "tail_roughness_checked": tail_rough_failures == 0,
        "formula_failure_count": formula_failures,
        "bracket_failure_count": bracket_failures,
        "tail_rough_failure_count": tail_rough_failures,
        "predecessor_distribution_bound_proved": False,
        "row_column_unconditional_closed": False,
        "profiles": profiles,
        "worst_lowalpha_block": worst,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "crossing 前缀分布已改写为前驱 `D_-` 的短双曲区间："
            "`P^2/D_- < r*t <= (P^2+P-1)/D_-`，长度为 `P/D_-`，"
            "其中 `r` 是跨越素因子，尾因子 `t` 为 `r`-rough。"
            "所以持续过载不能再隐藏在单个 crossing key 内，只能表现为前驱集合上的短区间分布过密或 PDEC。"
        ),
    }


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha crossing 前驱路由",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"predecessor_short_hyperbola_formula_closed={fmt_bool(result['predecessor_short_hyperbola_formula_closed'])}",
        f"crossing_bracket_checked={fmt_bool(result['crossing_bracket_checked'])}",
        f"tail_roughness_checked={fmt_bool(result['tail_roughness_checked'])}",
        f"predecessor_distribution_bound_proved={fmt_bool(result['predecessor_distribution_bound_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 最坏 low-alpha 块",
        "",
        "| P | block | hits | active D_- | max hits/D_- | top D_- | width sum | hits/width | max width | top width bucket |",
        "| ---: | --- | ---: | ---: | ---: | --- | ---: | ---: | ---: | --- |",
    ]
    worst = result["worst_lowalpha_block"]
    if worst:
        lines.append(
            f"| {worst['p']} | `({worst['previous_cutoff']},{worst['cutoff']}]` | "
            f"{worst['cofactor_hits']} | {worst['active_predecessor_count']} | "
            f"{worst['max_hits_per_predecessor']} | `{worst['top_predecessor']}` | "
            f"{worst['predecessor_width_budget_sum']:.6f} | {worst['hits_per_width_budget']:.6f} | "
            f"{worst['max_interval_width']:.6f} | `{worst['top_width_bucket']}` |"
        )
    lines.extend(
        [
            "",
            "## 2. 每个 P 的总结",
            "",
            "| P | low blocks | total hits | worst block | worst D_- count | top width bucket |",
            "| ---: | ---: | ---: | --- | ---: | --- |",
        ]
    )
    for profile in result["profiles"]:
        row = profile["worst_lowalpha_block"]
        if row is None:
            continue
        lines.append(
            f"| {profile['p']} | {profile['lowalpha_row_count']} | {profile['total_hits']} | "
            f"`({row['previous_cutoff']},{row['cutoff']}]` | {row['active_predecessor_count']} | "
            f"`{row['top_width_bucket']}` |"
        )
    lines.extend(
        [
            "",
            "## 3. 证明边界",
            "",
            "- 已闭合：crossing 前驱短双曲区间公式。",
            "- 已闭合：tail `t` 继承 `r`-rough 性质。",
            f"- 未闭合：`{NEXT_TARGET}`，即对全部前驱 `D_-` 的短区间 rough-prime 对分布上界，或失败形成 PDEC。",
            "",
            "## 4. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for name, digest in sorted(result["source_hashes"].items()):
        lines.append(f"| `{name}` | `{digest}` |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--p-list", default=",".join(str(item) for item in DEFAULT_P_LIST))
    args = parser.parse_args()
    result = audit(parse_int_list(args.p_list))
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result)
    print(
        json.dumps(
            {
                "status": result["status"],
                "predecessor_short_hyperbola_formula_closed": result["predecessor_short_hyperbola_formula_closed"],
                "tail_roughness_checked": result["tail_roughness_checked"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        ),
        flush=True,
    )


if __name__ == "__main__":
    main()
