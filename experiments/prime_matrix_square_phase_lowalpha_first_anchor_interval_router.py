#!/usr/bin/env python3
"""审计 low-alpha 第一锚区间化与 prime/composite 回流。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_first_anchor_interval_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-first-anchor-interval-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-first-anchor-interval-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-first-anchor-interval-router.md
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
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-first-anchor-interval-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-first-anchor-interval-router.md"

DEFAULT_P_LIST = [10007, 36739, 83561, 200003]
BASE_D = 31

PRIME_ANCHOR_TARGET = "PrimeAnchorRFPOrSelbergDistributionLedger"
COMPOSITE_TARGET = "CompositeFirstAnchorIntervalLoadBoundOrPDEC"
RESIDUAL_TARGET = "ResidualLowerDepthBuchstabCofactorLoadBoundOrPDEC"

SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-buchstab-anchor-decomposition.json",
    "prime-matrix-square-phase-cofactor-depth-regime-router.json",
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


def smallest_prime_factor(n: int, trial_primes: list[int]) -> int:
    """返回 n 的最小素因子；n 为素数时返回 n。"""
    if n < 2:
        return n
    for prime in trial_primes:
        if prime * prime > n:
            break
        if n % prime == 0:
            return prime
    return n


def prime_factor_count(n: int, trial_primes: list[int]) -> int:
    """返回 n 的素因子重数。"""
    if n < 2:
        return 0
    count = 0
    value = n
    for prime in trial_primes:
        if prime * prime > value:
            break
        while value % prime == 0:
            count += 1
            value //= prime
    if value > 1:
        count += 1
    return count


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


def interval_capacity(p2: int, p: int, q: int, anchor: int) -> int:
    """固定 q 和第一锚 a 时，残余 n 的整数区间容量。"""
    left = p2 // (q * anchor) + 1
    right = (p2 + p - 1) // (q * anchor)
    return max(0, right - left + 1)


def bucket_for_anchor(anchor: int, z: int) -> str:
    """按第一锚相对 z 的 dyadic 层分桶。"""
    ratio = anchor / z
    level = int(math.floor(math.log(ratio, 2))) if ratio > 1 else 0
    return f"A{level}:({2**level}z,{2**(level+1)}z]"


def register_top(mapping: dict[str, int], key: str) -> None:
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
    """审计一个 low-alpha block 的第一锚区间化。"""
    p2 = p * p
    hits = 0
    prime_anchor_hits = 0
    composite_anchor_hits = 0
    formula_failures = 0
    residual_rough_failures = 0
    anchor_not_prime_failures = 0
    pair_hits: dict[str, int] = {}
    pair_capacity: dict[str, int] = {}
    bucket_counts: dict[str, int] = {}
    residual_depth_counts: dict[str, int] = {}
    max_pair_hits = 0
    max_pair_capacity = 0
    total_active_pair_capacity = 0
    for q in block_primes:
        left = p2 // q + 1
        right = (p2 + p - 1) // q
        for m in range(left, right + 1):
            k = q * m - p2
            if not (1 <= k < p and allowed[k]):
                continue
            hits += 1
            anchor = smallest_prime_factor(m, trial_primes)
            if smallest_prime_factor(anchor, trial_primes) != anchor:
                anchor_not_prime_failures += 1
            residual = m // anchor
            cap = interval_capacity(p2, p, q, anchor)
            if not (p2 // (q * anchor) < residual <= (p2 + p - 1) // (q * anchor)):
                formula_failures += 1
            if residual == 1:
                prime_anchor_hits += 1
            else:
                composite_anchor_hits += 1
                residual_anchor = smallest_prime_factor(residual, trial_primes)
                if residual_anchor < anchor:
                    residual_rough_failures += 1
            pair_key = f"{q}:{anchor}"
            if pair_key not in pair_capacity:
                pair_capacity[pair_key] = cap
                total_active_pair_capacity += cap
                max_pair_capacity = max(max_pair_capacity, cap)
            pair_hits[pair_key] = pair_hits.get(pair_key, 0) + 1
            max_pair_hits = max(max_pair_hits, pair_hits[pair_key])
            register_top(bucket_counts, bucket_for_anchor(anchor, previous_cutoff))
            register_top(residual_depth_counts, str(prime_factor_count(residual, trial_primes)))
    top_pair = max(pair_hits.items(), key=lambda item: item[1], default=(None, 0))
    top_bucket = max(bucket_counts.items(), key=lambda item: item[1], default=(None, 0))
    return {
        "p": p,
        "previous_cutoff": previous_cutoff,
        "cutoff": cutoff,
        "alpha_left": math.log(previous_cutoff) / math.log(p),
        "block_prime_count": len(block_primes),
        "cofactor_hits": hits,
        "prime_anchor_hits": prime_anchor_hits,
        "composite_anchor_hits": composite_anchor_hits,
        "prime_anchor_share": None if hits == 0 else prime_anchor_hits / hits,
        "composite_anchor_share": None if hits == 0 else composite_anchor_hits / hits,
        "active_anchor_pair_count": len(pair_hits),
        "total_active_pair_capacity": total_active_pair_capacity,
        "active_pair_hit_density": None if total_active_pair_capacity == 0 else hits / total_active_pair_capacity,
        "max_pair_hits": max_pair_hits,
        "max_pair_capacity": max_pair_capacity,
        "top_anchor_pair": top_pair[0],
        "top_anchor_pair_hits": top_pair[1],
        "top_anchor_bucket": top_bucket[0],
        "top_anchor_bucket_count": top_bucket[1],
        "bucket_counts": bucket_counts,
        "residual_depth_counts": residual_depth_counts,
        "formula_failure_count": formula_failures,
        "residual_rough_failure_count": residual_rough_failures,
        "anchor_not_prime_failure_count": anchor_not_prime_failures,
        "factor_depth_bound": factor_depth_bound(p, previous_cutoff),
    }


def audit_p(p: int, primes: list[int], trial_primes: list[int]) -> dict[str, Any]:
    """审计一个 P 的 low-alpha 第一锚区间化。"""
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
        "prime_anchor_hits": sum(row["prime_anchor_hits"] for row in low_rows),
        "composite_anchor_hits": sum(row["composite_anchor_hits"] for row in low_rows),
        "formula_failure_count": sum(row["formula_failure_count"] for row in low_rows),
        "residual_rough_failure_count": sum(row["residual_rough_failure_count"] for row in low_rows),
        "anchor_not_prime_failure_count": sum(row["anchor_not_prime_failure_count"] for row in low_rows),
        "worst_lowalpha_block": worst,
        "rows": low_rows,
    }


def file_sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖哈希。"""
    result = {
        "experiments/prime_matrix_square_phase_lowalpha_first_anchor_interval_router.py": file_sha256(
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
    low_rows = [row for profile in profiles for row in profile["rows"]]
    worst = max(low_rows, key=lambda item: item["cofactor_hits"], default=None)
    formula_failures = sum(profile["formula_failure_count"] for profile in profiles)
    residual_rough_failures = sum(profile["residual_rough_failure_count"] for profile in profiles)
    anchor_prime_failures = sum(profile["anchor_not_prime_failure_count"] for profile in profiles)
    total_hits = sum(profile["total_hits"] for profile in profiles)
    prime_hits = sum(profile["prime_anchor_hits"] for profile in profiles)
    composite_hits = sum(profile["composite_anchor_hits"] for profile in profiles)
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_first_anchor_interval_router",
        "status": "lowalpha_first_anchor_intervalized_prime_composite_split_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "first_anchor_interval_formula_closed": formula_failures == 0,
        "residual_lower_depth_identity_closed": residual_rough_failures == 0,
        "anchor_primality_checked": anchor_prime_failures == 0,
        "formula_failure_count": formula_failures,
        "residual_rough_failure_count": residual_rough_failures,
        "anchor_not_prime_failure_count": anchor_prime_failures,
        "total_lowalpha_hits": total_hits,
        "prime_anchor_hits": prime_hits,
        "composite_anchor_hits": composite_hits,
        "prime_anchor_share": None if total_hits == 0 else prime_hits / total_hits,
        "composite_anchor_share": None if total_hits == 0 else composite_hits / total_hits,
        "prime_anchor_return_to_rfp_closed": True,
        "composite_anchor_lower_depth_reduction_closed": residual_rough_failures == 0,
        "composite_anchor_load_bound_proved": False,
        "prime_anchor_distribution_proved": False,
        "row_column_unconditional_closed": False,
        "p_list": p_list,
        "profiles": profiles,
        "worst_lowalpha_block": worst,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": COMPOSITE_TARGET,
        "parallel_attack_targets": [PRIME_ANCHOR_TARGET, RESIDUAL_TARGET],
        "plain_conclusion": (
            "第一锚分解已进一步区间化：每个 low-alpha 命中唯一写成 "
            "`P^2+k=q*a*n`，其中 `a=P^-(m)>z`，`n=m/a` 落入长度约 `P/(qa)` "
            "的短区间。`n=1` 正是素互补因子，回到 RFP/Selberg 分布线；"
            "`n>1` 时 `n` 自动为 `a`-rough，因子深度严格下降。"
        ),
    }


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha 第一锚区间路由",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"first_anchor_interval_formula_closed={fmt_bool(result['first_anchor_interval_formula_closed'])}",
        f"residual_lower_depth_identity_closed={fmt_bool(result['residual_lower_depth_identity_closed'])}",
        f"anchor_primality_checked={fmt_bool(result['anchor_primality_checked'])}",
        f"prime_anchor_return_to_rfp_closed={fmt_bool(result['prime_anchor_return_to_rfp_closed'])}",
        f"composite_anchor_load_bound_proved={fmt_bool(result['composite_anchor_load_bound_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 全局分裂",
        "",
        "| total hits | prime anchor | composite anchor | prime share | composite share |",
        "| ---: | ---: | ---: | ---: | ---: |",
        (
            f"| {result['total_lowalpha_hits']} | {result['prime_anchor_hits']} | "
            f"{result['composite_anchor_hits']} | {result['prime_anchor_share']:.6f} | "
            f"{result['composite_anchor_share']:.6f} |"
        ),
        "",
        "## 2. 最坏 low-alpha 块",
        "",
        "| P | block | hits | prime | composite | active pairs | active density | top pair | top pair hits | top bucket |",
        "| ---: | --- | ---: | ---: | ---: | ---: | ---: | --- | ---: | --- |",
    ]
    worst = result["worst_lowalpha_block"]
    if worst:
        lines.append(
            f"| {worst['p']} | `({worst['previous_cutoff']},{worst['cutoff']}]` | "
            f"{worst['cofactor_hits']} | {worst['prime_anchor_hits']} | "
            f"{worst['composite_anchor_hits']} | {worst['active_anchor_pair_count']} | "
            f"{worst['active_pair_hit_density']:.6f} | `{worst['top_anchor_pair']}` | "
            f"{worst['top_anchor_pair_hits']} | `{worst['top_anchor_bucket']}` |"
        )
    lines.extend(
        [
            "",
            "## 3. 每个 P 的总结",
            "",
            "| P | low blocks | total hits | prime | composite | worst block | worst top pair |",
            "| ---: | ---: | ---: | ---: | ---: | --- | --- |",
        ]
    )
    for profile in result["profiles"]:
        row = profile["worst_lowalpha_block"]
        if row is None:
            continue
        lines.append(
            f"| {profile['p']} | {profile['lowalpha_row_count']} | {profile['total_hits']} | "
            f"{profile['prime_anchor_hits']} | {profile['composite_anchor_hits']} | "
            f"`({row['previous_cutoff']},{row['cutoff']}]` | `{row['top_anchor_pair']}` |"
        )
    lines.extend(
        [
            "",
            "## 4. 证明边界",
            "",
            "- 已闭合：第一锚短区间公式、anchor 素性、residual `a`-rough 降深。",
            f"- 素互补分支：`n=1` 已严格回流 `{PRIME_ANCHOR_TARGET}`。",
            f"- 复合分支：剩余为 `{COMPOSITE_TARGET}`，失败必须表现为第一锚 PDEC。",
            f"- 递归分支：`n>1` 时继续进入 `{RESIDUAL_TARGET}`。",
            "",
            "## 5. 依赖哈希",
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
                "first_anchor_interval_formula_closed": result["first_anchor_interval_formula_closed"],
                "residual_lower_depth_identity_closed": result["residual_lower_depth_identity_closed"],
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
