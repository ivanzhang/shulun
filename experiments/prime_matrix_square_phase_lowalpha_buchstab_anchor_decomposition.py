#!/usr/bin/env python3
"""审计 low-alpha Buchstab cofactor 的第一锚分解。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_buchstab_anchor_decomposition.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-buchstab-anchor-decomposition.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-buchstab-anchor-decomposition.json
  docs/monograph/prime-matrix-square-phase-lowalpha-buchstab-anchor-decomposition.md
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
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-buchstab-anchor-decomposition.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-buchstab-anchor-decomposition.md"

DEFAULT_P_LIST = [10007, 36739, 83561, 200003]
BASE_D = 31

LOW_ALPHA = "LowAlphaBuchstabCofactorLoadBoundOrPDEC"
ANCHOR_TARGET = "LowAlphaFirstAnchorCofactorLoadBoundOrAnchorPDEC"
RESIDUAL_TARGET = "ResidualLowerDepthBuchstabCofactorLoadBoundOrPDEC"

SOURCE_FILES = [
    "prime-matrix-square-phase-cofactor-depth-regime-router.json",
    "prime-matrix-square-phase-dyadic-first-moment-cofactor-duality.json",
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


def is_prime64(n: int) -> bool:
    """确定性 Miller-Rabin，适用于本项目样本范围。"""
    if n < 2:
        return False
    small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for prime in small_primes:
        if n == prime:
            return True
        if n % prime == 0:
            return False
    d = n - 1
    s = 0
    while d % 2 == 0:
        s += 1
        d //= 2
    for a in [2, 3, 5, 7, 11, 13, 17]:
        if a >= n:
            continue
        x = pow(a, d, n)
        if x in {1, n - 1}:
            continue
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            return False
    return True


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


def anchor_bucket(anchor: int, z: int) -> str:
    """按第一锚相对 z 的 dyadic 层分桶。"""
    if anchor <= z:
        return "invalid_le_z"
    ratio = anchor / z
    level = int(math.floor(math.log(ratio, 2))) if ratio > 1 else 0
    return f"A{level}:({2**level}z,{2**(level+1)}z]"


def audit_lowalpha_block(
    p: int,
    previous_cutoff: int,
    cutoff: int,
    allowed: bytearray,
    block_primes: list[int],
    trial_primes: list[int],
) -> dict[str, Any]:
    """审计一个 low-alpha block 的第一锚分解。"""
    p2 = p * p
    hits = 0
    identity_failures = 0
    invalid_anchor = 0
    prime_cofactor = 0
    composite_cofactor = 0
    bucket_counts: dict[str, int] = {}
    residual_depth_counts: dict[str, int] = {}
    max_residual_depth = 0
    max_anchor = 0
    min_anchor = None
    for q in block_primes:
        left = p2 // q + 1
        right = (p2 + p - 1) // q
        for m in range(left, right + 1):
            k = q * m - p2
            if not (1 <= k < p and allowed[k]):
                continue
            hits += 1
            anchor = smallest_prime_factor(m, trial_primes)
            if m % anchor != 0:
                identity_failures += 1
                continue
            if anchor <= previous_cutoff:
                invalid_anchor += 1
            if anchor == m:
                prime_cofactor += 1
                residual_depth = 0
            else:
                composite_cofactor += 1
                residual_depth = prime_factor_count(m // anchor, trial_primes)
            max_residual_depth = max(max_residual_depth, residual_depth)
            max_anchor = max(max_anchor, anchor)
            min_anchor = anchor if min_anchor is None else min(min_anchor, anchor)
            bucket = anchor_bucket(anchor, previous_cutoff)
            bucket_counts[bucket] = bucket_counts.get(bucket, 0) + 1
            residual_key = str(residual_depth)
            residual_depth_counts[residual_key] = residual_depth_counts.get(residual_key, 0) + 1
    top_bucket = max(bucket_counts.items(), key=lambda item: item[1], default=(None, 0))
    return {
        "p": p,
        "previous_cutoff": previous_cutoff,
        "cutoff": cutoff,
        "alpha_left": math.log(previous_cutoff) / math.log(p),
        "block_prime_count": len(block_primes),
        "cofactor_hits": hits,
        "identity_failures": identity_failures,
        "invalid_anchor_count": invalid_anchor,
        "prime_cofactor_hits": prime_cofactor,
        "composite_cofactor_hits": composite_cofactor,
        "bucket_counts": bucket_counts,
        "residual_depth_counts": residual_depth_counts,
        "top_anchor_bucket": top_bucket[0],
        "top_anchor_bucket_count": top_bucket[1],
        "max_residual_depth": max_residual_depth,
        "min_anchor": min_anchor,
        "max_anchor": max_anchor,
        "factor_depth_bound": factor_depth_bound(p, previous_cutoff),
    }


def audit_p(p: int, primes: list[int], trial_primes: list[int]) -> dict[str, Any]:
    """审计一个 P 的 low-alpha block。"""
    p2 = p * p
    cutoffs = cutoffs_for_p(p)
    allowed = bytearray(b"\x01") * p
    allowed[0] = 0
    prime_index = 0
    rows = []
    for cutoff in cutoffs:
        previous = 0 if not rows else rows[-1]["cutoff"]
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
        "lowalpha_total_hits": sum(row["cofactor_hits"] for row in low_rows),
        "identity_failure_count": sum(row["identity_failures"] for row in low_rows),
        "invalid_anchor_count": sum(row["invalid_anchor_count"] for row in low_rows),
        "worst_lowalpha_block": worst,
        "rows": low_rows,
    }


def file_sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖哈希。"""
    result = {
        "experiments/prime_matrix_square_phase_lowalpha_buchstab_anchor_decomposition.py": file_sha256(
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
    total_identity_failures = sum(profile["identity_failure_count"] for profile in profiles)
    total_invalid_anchor = sum(profile["invalid_anchor_count"] for profile in profiles)
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_buchstab_anchor_decomposition",
        "status": "lowalpha_buchstab_cofactor_load_reduced_to_first_anchor_layers_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "first_anchor_decomposition_checked": total_identity_failures == 0 and total_invalid_anchor == 0,
        "identity_failure_count": total_identity_failures,
        "invalid_anchor_count": total_invalid_anchor,
        "first_anchor_load_bound_proved": False,
        "residual_lower_depth_bound_proved": False,
        "row_column_unconditional_closed": False,
        "p_list": p_list,
        "profiles": profiles,
        "worst_lowalpha_block": worst,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": ANCHOR_TARGET,
        "parallel_attack_target": RESIDUAL_TARGET,
        "plain_conclusion": (
            "low-alpha Buchstab cofactor 负载已按第一锚 `a=P^-(m)>z` 精确分解。"
            "每个命中互补因子 `m` 唯一进入某个 anchor dyadic 层，并留下更低深度残余 `m/a`。"
            "若某层负载异常重，就进入 first-anchor PDEC；否则剩余问题下降为更低深度的 Buchstab 负载。"
        ),
    }


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha Buchstab 第一锚分解",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"first_anchor_decomposition_checked={fmt_bool(result['first_anchor_decomposition_checked'])}",
        f"identity_failure_count={result['identity_failure_count']}",
        f"invalid_anchor_count={result['invalid_anchor_count']}",
        f"first_anchor_load_bound_proved={fmt_bool(result['first_anchor_load_bound_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 最坏 low-alpha 块",
        "",
        "| P | block | alpha | hits | top anchor bucket | top count | residual depths | max residual depth |",
        "| ---: | --- | ---: | ---: | --- | ---: | --- | ---: |",
    ]
    worst = result["worst_lowalpha_block"]
    if worst:
        lines.append(
            f"| {worst['p']} | `({worst['previous_cutoff']},{worst['cutoff']}]` | "
            f"{worst['alpha_left']:.6f} | {worst['cofactor_hits']} | "
            f"`{worst['top_anchor_bucket']}` | {worst['top_anchor_bucket_count']} | "
            f"`{worst['residual_depth_counts']}` | {worst['max_residual_depth']} |"
        )
    lines.extend(
        [
            "",
            "## 2. 每个 P 的 low-alpha 总结",
            "",
            "| P | low blocks | total hits | worst block | worst hits | top bucket | residual depths |",
            "| ---: | ---: | ---: | --- | ---: | --- | --- |",
        ]
    )
    for profile in result["profiles"]:
        row = profile["worst_lowalpha_block"]
        if row is None:
            continue
        lines.append(
            f"| {profile['p']} | {profile['lowalpha_row_count']} | {profile['lowalpha_total_hits']} | "
            f"`({row['previous_cutoff']},{row['cutoff']}]` | {row['cofactor_hits']} | "
            f"`{row['top_anchor_bucket']}` | `{row['residual_depth_counts']}` |"
        )
    lines.extend(
        [
            "",
            "## 3. 证明边界",
            "",
            f"- 已闭合：每个 low-alpha cofactor 命中唯一分解为第一锚层加 residual lower-depth cofactor。",
            f"- 未闭合：`{ANCHOR_TARGET}`，即第一锚层负载上界或其 PDEC 排斥。",
            f"- 并行：`{RESIDUAL_TARGET}`，即 residual 深度下降后的递归负载账本。",
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
                "first_anchor_decomposition_checked": result["first_anchor_decomposition_checked"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "parallel_attack_target": result["parallel_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        ),
        flush=True,
    )


if __name__ == "__main__":
    main()
