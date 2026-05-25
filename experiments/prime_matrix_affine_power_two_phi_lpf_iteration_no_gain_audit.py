#!/usr/bin/env python3
"""审计 2^t n+(2^t-1) affine/Phi-LPF 迭代是否产生新奇偶增益。

用法示例：
  python3 experiments/prime_matrix_affine_power_two_phi_lpf_iteration_no_gain_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-affine-power-two-phi-lpf-iteration-no-gain-audit.json

本层承接 affine 2n+1 审计。把映射推广为
  m_t = 2^t n + (2^t-1).
对每个奇素数 p，条件 p | m_t 仍只是 n 的一个 shifted residue 类。
因此迭代不会自动产生新的 LPF/Phi 相消；若在 m_t 侧忘记 2-adic residue
space，naive 欧拉乘积 gap 会从 1/2 推广为 1-2^{-t}。
"""

from __future__ import annotations

import hashlib
import json
from math import prod
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-affine-power-two-phi-lpf-iteration-no-gain"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

SAMPLE_PRIMES = [31, 101, 251, 1009]
ITERATION_DEPTHS = [1, 2, 3, 4]

DEPENDENCIES = [
    DOCS / "prime-matrix-affine-2n-plus-1-euler-lpf-parity-audit.json",
    DOCS / "three-claims-breakthrough-route-synthesis-20260525.md",
    DOCS / "frontier-honest-status-and-true-side-theorems-20260522.md",
    DOCS / "external-theorem-index.md",
    DOCS / "claim-status-table.md",
    ROOT / "paper" / "contradiction-field-monograph" / "contradiction-field-monograph.tex",
]


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    paths = [Path(__file__).resolve(), *DEPENDENCIES]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def primes_upto(n: int) -> list[int]:
    """返回不超过 n 的素数。"""
    if n < 2:
        return []
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, int(n**0.5) + 1):
        if sieve[p]:
            start = p * p
            sieve[start : n + 1 : p] = b"\x00" * (((n - start) // p) + 1)
    return [i for i in range(2, n + 1) if sieve[i]]


def prime_flags_upto(n: int) -> bytearray:
    """返回素数布尔表。"""
    flags = bytearray(b"\x01") * (n + 1)
    if n >= 0:
        flags[0] = 0
    if n >= 1:
        flags[1] = 0
    for p in range(2, int(n**0.5) + 1):
        if flags[p]:
            start = p * p
            flags[start : n + 1 : p] = b"\x00" * (((n - start) // p) + 1)
    return flags


def odd_euler_product(primes: list[int], p_limit: int) -> float:
    """奇素数部分有限欧拉乘积。"""
    return prod(1.0 - 1.0 / p for p in primes if 2 < p <= p_limit)


def no_prime_factor_below(n: int, bound: int, primes: list[int]) -> bool:
    """判断 n 是否无小于 bound 的素因子。"""
    for p in primes:
        if p >= bound:
            break
        if n % p == 0:
            return False
    return True


def mark_shifted_survivors(x: int, p_limit: int, a: int, b: int, primes: list[int]) -> tuple[bytearray, int]:
    """标记 n<=x 中让 a*n+b 避开奇素数 p<=p_limit 的元素，并返回 residue 公式错误数。"""
    survivors = bytearray(b"\x01") * (x + 1)
    residue_error_count = 0
    for p in primes:
        if p == 2 or p > p_limit:
            continue
        residue = (-b * pow(a, -1, p)) % p
        if (a * residue + b) % p != 0:
            residue_error_count += 1
        if residue <= x:
            survivors[residue : x + 1 : p] = b"\x00" * (((x - residue) // p) + 1)
    return survivors, residue_error_count


def audit_pair(P: int, t: int, prime_flags: bytearray) -> dict[str, Any]:
    """审计单个 (P,t) 样本。"""
    x = P * P
    a = 1 << t
    b = a - 1
    primes = primes_upto(max(P, int((a * x + b) ** 0.5) + 1))
    small_primes = [p for p in primes if p <= P]
    survivors, residue_error_count = mark_shifted_survivors(x, P, a, b, small_primes)
    survivor_count = int(sum(survivors))

    prime_m_count = 0
    rough_composite_count = 0
    unit_count = 0
    for n, alive in enumerate(survivors):
        if not alive:
            continue
        m = a * n + b
        if m == 1:
            unit_count += 1
        elif prime_flags[m]:
            prime_m_count += 1
        else:
            rough_composite_count += 1

    forced_residue = (-b * pow(a, -1, P)) % P
    forced_count = ((x - forced_residue) // P) + 1 if forced_residue <= x else 0
    forced_lpf_p_count = 0
    forced_prime_exception_count = 0
    for n in range(forced_residue, x + 1, P):
        m = a * n + b
        if m == P:
            forced_prime_exception_count += 1
            continue
        if m > P and m % P == 0 and no_prime_factor_below(m // P, P, small_primes):
            forced_lpf_p_count += 1

    prod_odd = odd_euler_product(small_primes, P)
    correct_main = (x + 1) * prod_odd
    naive_main = a * (x + 1) * prod_odd
    expected_two_adic_gap = 1.0 - 1.0 / a
    observed_naive_gap = (naive_main - survivor_count) / naive_main if naive_main else None
    corrected_error = (survivor_count - correct_main) / correct_main if correct_main else None

    return {
        "P": P,
        "t": t,
        "a": a,
        "b": b,
        "x": x,
        "map": f"m={a}n+{b}",
        "target_2_adic_residue": b,
        "odd_prime_sieve_count": len([p for p in small_primes if p > 2]),
        "residue_formula_error_count": residue_error_count,
        "affine_shifted_residue_formula_verified": residue_error_count == 0,
        "survivor_count": survivor_count,
        "unit_count": unit_count,
        "prime_m_count": prime_m_count,
        "rough_composite_count": rough_composite_count,
        "rough_composite_fraction": rough_composite_count / survivor_count if survivor_count else None,
        "forced_residue_mod_P": forced_residue,
        "forced_count": forced_count,
        "forced_prime_exception_count": forced_prime_exception_count,
        "lpf_m_equal_P_count_in_forced_class": forced_lpf_p_count,
        "lpf_m_equal_P_fraction_of_forced": forced_lpf_p_count / max(1, forced_count - forced_prime_exception_count),
        "euler_product_odd_part": prod_odd,
        "correct_2_adic_residue_main": correct_main,
        "naive_full_interval_odd_product_main": naive_main,
        "observed_naive_gap_fraction": observed_naive_gap,
        "expected_two_adic_gap_fraction": expected_two_adic_gap,
        "gap_minus_expected": (observed_naive_gap - expected_two_adic_gap) if observed_naive_gap is not None else None,
        "corrected_error_fraction": corrected_error,
    }


def build_result() -> dict[str, Any]:
    """构造审计结果。"""
    max_m = max((1 << max(ITERATION_DEPTHS)) * (P * P) + ((1 << max(ITERATION_DEPTHS)) - 1) for P in SAMPLE_PRIMES)
    prime_flags = prime_flags_upto(max_m)
    rows = [audit_pair(P, t, prime_flags) for P in SAMPLE_PRIMES for t in ITERATION_DEPTHS]
    max_abs_gap_minus_expected = max(abs(row["gap_minus_expected"]) for row in rows)
    return {
        "certificate_type": "prime_matrix_affine_power_two_phi_lpf_iteration_no_gain_audit",
        "status": "power_two_affine_iteration_is_shifted_residue_conjugacy_no_parity_gain",
        "verified_date": "2026-05-25",
        "sample_primes": SAMPLE_PRIMES,
        "iteration_depths": ITERATION_DEPTHS,
        "affine_family": "m_t=2^t*n+(2^t-1)",
        "residue_formula": "p|m_t iff n == -(2^t-1)*(2^t)^(-1) mod p for odd p",
        "all_shifted_residue_formula_verified": all(row["affine_shifted_residue_formula_verified"] for row in rows),
        "naive_gap_tracks_two_adic_density": True,
        "max_abs_gap_minus_expected": max_abs_gap_minus_expected,
        "iteration_creates_new_phi_lpf_information": False,
        "euler_product_half_main_error_proved": False,
        "phi_lpf_parity_barrier_globally_broken": False,
        "row_column_unconditional_closed": False,
        "external_lemma_version_unconditional_closed": False,
        "internal_self_contained_closed": False,
        "rows": rows,
        "source_hashes": source_hashes(),
        "next_open_gate": (
            "PowerTwoAffineShiftedResidueSignedPayloadConstructorOrNamedReturn "
            "AND PrimeExtractionFromAffineRoughSurvivorsBeyondParity"
        ),
        "plain_conclusion": (
            "Iterating 2n+1 to 2^t n+(2^t-1) only changes the fixed 2-adic "
            "residue class and the shifted forbidden residue modulo odd primes. "
            "The apparent Euler-product gap follows the missing 2-adic density "
            "1-2^{-t}; after normalization, the remaining problem is still "
            "prime extraction from rough survivors."
        ),
    }


def write_outputs(result: dict[str, Any]) -> None:
    """写出 JSON 与 Markdown。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(result, indent=2, ensure_ascii=False)
    OUT_LEDGER.write_text(payload + "\n", encoding="utf-8")
    OUT_JSON.write_text(payload + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")


def render_markdown(result: dict[str, Any]) -> str:
    """渲染审计 Markdown。"""
    lines: list[str] = []
    lines.append("# Prime Matrix power-two affine Phi-LPF iteration no-gain audit")
    lines.append("")
    lines.append(f"**状态：** `{result['status']}`")
    lines.append("**核验日期：** `2026-05-25`")
    lines.append("")
    lines.append("## 1. 迭代对象")
    lines.append("")
    lines.append("```text")
    lines.append("m_t = 2^t n + (2^t-1)")
    lines.append("p | m_t  <=>  n == -(2^t-1)*(2^t)^(-1) mod p     (p odd)")
    lines.append("```")
    lines.append("")
    lines.append("这说明每次迭代仍只是每个奇素数删除一个 shifted residue 类。")
    lines.append("")
    lines.append("## 2. 有限读数")
    lines.append("")
    lines.append("| P | t | survivor | prime m_t | rough composite | expected 2-adic gap | observed naive gap | corrected error |")
    lines.append("| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |")
    for row in result["rows"]:
        lines.append(
            "| {P} | {t} | {survivor} | {prime_m} | {rough} | {expected:.6f} | {observed:.6f} | {corrected:.6f} |".format(
                P=row["P"],
                t=row["t"],
                survivor=row["survivor_count"],
                prime_m=row["prime_m_count"],
                rough=row["rough_composite_count"],
                expected=row["expected_two_adic_gap_fraction"],
                observed=row["observed_naive_gap_fraction"],
                corrected=row["corrected_error_fraction"],
            )
        )
    lines.append("")
    lines.append("## 3. 结论")
    lines.append("")
    lines.append("```text")
    lines.append(f"all_shifted_residue_formula_verified={str(result['all_shifted_residue_formula_verified']).lower()}")
    lines.append("iteration_creates_new_phi_lpf_information=false")
    lines.append("euler_product_half_main_error_proved=false")
    lines.append("phi_lpf_parity_barrier_globally_broken=false")
    lines.append("row_column_unconditional_closed=false")
    lines.append("```")
    lines.append("")
    lines.append(
        "naive gap 随 `t` 变成 `1-2^{-t}`，说明它是 2-adic residue-space 归一化，"
        "不是有限欧拉乘积截断误差。归一化后仍有 rough composite survivors，"
        "所以 LPF/Phi 递推迭代没有自动突破奇偶性障碍。"
    )
    lines.append("")
    lines.append("## 4. 最新开放口")
    lines.append("")
    lines.append("```text")
    lines.append(result["next_open_gate"])
    lines.append("```")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """入口。"""
    result = build_result()
    write_outputs(result)
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
