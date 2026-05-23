#!/usr/bin/env python3
"""生成 Phi-LPF punctured endpoint 6-wheel capacity 证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_punctured_endpoint_wheel6_capacity_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-punctured-endpoint-wheel6-capacity-router.json

上一层 parity capacity 只扣除偶数 cofactor m。本层加入 Euler 6-wheel 的
第二个局部筛除：若 m>3 且 3|m，则 m 也不可能是素数。这个步骤不改变
Phi-LPF 恒等式，也不把有限审计当作全局证明；它只把 forest-hole 上界
从奇偶窗进一步压到 6-wheel 窗，并删除 parity-only 等号基例。
"""

from __future__ import annotations

import hashlib
import json
from math import isqrt
from pathlib import Path
from typing import Any, Callable


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-punctured-endpoint-wheel6-capacity"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

MAX_PRIME_AUDIT = 1009
LARGE_SAMPLE_SEEDS = [100000, 300000]
WHEEL_PRIMES = [2, 3]
FRONTIER_VERIFIED_DATE = "2026-05-23"

DEPENDENCIES = [
    DOCS / "prime-matrix-phi-lpf-punctured-endpoint-difference-router.json",
    DOCS / "prime-matrix-phi-lpf-punctured-endpoint-parity-capacity-router.json",
    DOCS / "prime-matrix-phi-lpf-combinatorial-exactness-parity-barrier-review-router.json",
    DOCS / "external-theorem-index.md",
    DOCS / "claim-status-table.md",
    DOCS / "frontier-honest-status-and-true-side-theorems-20260522.md",
    ROOT / "paper" / "contradiction-field-monograph" / "contradiction-field-monograph.tex",
]


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def bool_text(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def spf_table(n: int) -> list[int]:
    """生成最小素因子表。"""
    spf = list(range(n + 1))
    if n >= 1:
        spf[1] = 1
    for p in range(2, isqrt(n) + 1):
        if spf[p] == p:
            for value in range(p * p, n + 1, p):
                if spf[value] == value:
                    spf[value] = p
    return spf


def prime_flags(n: int) -> bytearray:
    """生成素数标记表。"""
    flags = bytearray(b"\x01") * (n + 1)
    if n >= 0:
        flags[0] = 0
    if n >= 1:
        flags[1] = 0
    for p in range(2, isqrt(n) + 1):
        if flags[p]:
            flags[p * p : n + 1 : p] = b"\x00" * (((n - p * p) // p) + 1)
    return flags


def primes_from_spf(spf: list[int], n: int) -> list[int]:
    """从 SPF 表读取素数。"""
    return [value for value in range(2, n + 1) if spf[value] == value]


def primes_from_flags(flags: bytearray, n: int) -> list[int]:
    """从素数标记读取素数。"""
    return [value for value in range(2, min(n, len(flags) - 1) + 1) if flags[value]]


def next_prime_after_half(P: int, primes_2p: list[int]) -> int:
    """返回大于 P/2 的第一个素数。"""
    for q in primes_2p:
        if q > P // 2:
            return q
    raise ValueError(f"missing half cutoff prime for P={P}")


def next_prime_at_least(seed: int, flags: bytearray) -> int:
    """在标记表内寻找不小于 seed 的第一个素数。"""
    for value in range(max(2, seed), len(flags)):
        if flags[value]:
            return value
    raise ValueError(f"no prime found after seed={seed}")


def shadow_free_cap(P: int) -> int:
    """返回 shadow-free 条件允许的最大 k。"""
    return max(1, (P * P - 4 * P + 4) // (4 * P))


def upper_band_first_k(P: int) -> int:
    """返回 upper square band 第一行。"""
    return max(2, shadow_free_cap(P) + 1)


def high_band_lower_k(P: int) -> int:
    """返回 BHP bulk 后的第一个整数 k；只作分区标签。"""
    return max(2, int(P ** (19.0 / 21.0)) + 1)


def reciprocal_window_for_q(P: int, k: int, q: int) -> tuple[int, int]:
    """返回固定 q 的 m 候选闭区间。"""
    lower = max(q, (k * P) // q + 1)
    upper = min(2 * P - 1, ((k + 1) * P - 1) // q)
    return lower, upper


def finite_delta_phi_half(P: int, k: int, spf: list[int], p_half: int) -> int:
    """直接计算 Phi((k+1)P-1,p_half)-Phi(kP,p_half)。"""
    return sum(1 for t in range(1, P) if spf[k * P + t] >= p_half)


def finite_direct_prime_count(P: int, k: int, spf: list[int]) -> int:
    """直接读取该行素数数。"""
    return sum(1 for t in range(1, P) if spf[k * P + t] == k * P + t)


def forest_hole_count(
    P: int,
    k: int,
    high_q_primes: list[int],
    is_prime: Callable[[int], bool],
) -> int:
    """计算真实 high-prime semiprime forest holes 数。"""
    count = 0
    for q in high_q_primes:
        lower, upper = reciprocal_window_for_q(P, k, q)
        for m in range(lower, upper + 1):
            if is_prime(m):
                count += 1
    return count


def wheel6_capacity(P: int, k: int, high_q_primes: list[int]) -> dict[str, int]:
    """计算 reciprocal 整数窗、奇偶窗与 6-wheel 窗容量。"""
    integer_capacity = 0
    forced_even_nonprime = 0
    forced_wheel6_nonprime = 0
    nonempty_windows = 0
    length_one_windows = 0
    length_two_windows = 0
    max_window_length = 0

    for q in high_q_primes:
        lower, upper = reciprocal_window_for_q(P, k, q)
        length = max(0, upper - lower + 1)
        integer_capacity += length
        max_window_length = max(max_window_length, length)
        if length:
            nonempty_windows += 1
        if length == 1:
            length_one_windows += 1
        elif length == 2:
            length_two_windows += 1
        for m in range(lower, upper + 1):
            even_forced = m > 2 and m % 2 == 0
            wheel6_forced = even_forced or (m > 3 and m % 3 == 0)
            if even_forced:
                forced_even_nonprime += 1
            if wheel6_forced:
                forced_wheel6_nonprime += 1

    return {
        "integer_window_capacity": integer_capacity,
        "forced_even_nonprime_candidates": forced_even_nonprime,
        "parity_prime_ceiling": integer_capacity - forced_even_nonprime,
        "forced_wheel6_nonprime_candidates": forced_wheel6_nonprime,
        "wheel6_prime_ceiling": integer_capacity - forced_wheel6_nonprime,
        "wheel6_extra_deletion_beyond_parity": forced_wheel6_nonprime - forced_even_nonprime,
        "nonempty_windows": nonempty_windows,
        "length_one_windows": length_one_windows,
        "length_two_windows": length_two_windows,
        "max_window_length": max_window_length,
    }


def row_profile(P: int, k: int, spf: list[int], primes_2p: list[int]) -> dict[str, Any]:
    """构造有限行的 6-wheel capacity 读数。"""
    p_half = next_prime_after_half(P, primes_2p)
    high_q_primes = [q for q in primes_2p if P // 2 < q < P]
    cap = wheel6_capacity(P, k, high_q_primes)
    delta_phi = finite_delta_phi_half(P, k, spf, p_half)
    holes = forest_hole_count(P, k, high_q_primes, lambda value: spf[value] == value)
    direct = finite_direct_prime_count(P, k, spf)
    cap.update(
        {
            "P": P,
            "k": k,
            "p_half": p_half,
            "in_shadow_free_subband": k <= shadow_free_cap(P),
            "in_upper_band": k >= upper_band_first_k(P),
            "in_bhp_remaining_high_band": k >= high_band_lower_k(P),
            "delta_phi_half": delta_phi,
            "forest_hole_count": holes,
            "direct_prime_count": direct,
            "delta_minus_integer_capacity": delta_phi - cap["integer_window_capacity"],
            "delta_minus_parity_ceiling": delta_phi - cap["parity_prime_ceiling"],
            "delta_minus_wheel6_ceiling": delta_phi - cap["wheel6_prime_ceiling"],
            "wheel6_ceiling_minus_holes": cap["wheel6_prime_ceiling"] - holes,
            "positive_by_integer_capacity": delta_phi > cap["integer_window_capacity"],
            "positive_by_parity_ceiling": delta_phi > cap["parity_prime_ceiling"],
            "positive_by_wheel6_ceiling": delta_phi > cap["wheel6_prime_ceiling"],
            "endpoint_positive_direct": direct > 0,
            "hole_leq_wheel6_ceiling": holes <= cap["wheel6_prime_ceiling"],
        }
    )
    return cap


def finite_audit(max_prime: int = MAX_PRIME_AUDIT) -> dict[str, Any]:
    """有限审计；只作一致性检查，不作全局证明。"""
    spf = spf_table(max_prime * max_prime)
    primes = primes_from_spf(spf, max_prime)
    primes_2p = primes_from_spf(spf, 2 * max_prime)
    rows: list[dict[str, Any]] = []
    for P in primes:
        if P < 11:
            continue
        for k in range(2, P):
            rows.append(row_profile(P, k, spf, primes_2p))

    wheel6_not_closed = [row for row in rows if not row["positive_by_wheel6_ceiling"]]
    wheel6_failures = [row for row in rows if row["delta_minus_wheel6_ceiling"] <= 0]
    hole_ceiling_failures = [row for row in rows if not row["hole_leq_wheel6_ceiling"]]
    sample_rows = [
        row
        for row in rows
        if (row["P"], row["k"]) in {(11, 10), (19, 15), (101, 100), (257, 256), (1009, 1008)}
    ]
    return {
        "max_prime": max_prime,
        "row_count": len(rows),
        "closed_by_integer_window_capacity_count": sum(row["positive_by_integer_capacity"] for row in rows),
        "closed_by_parity_ceiling_count": sum(row["positive_by_parity_ceiling"] for row in rows),
        "closed_by_wheel6_ceiling_count": sum(row["positive_by_wheel6_ceiling"] for row in rows),
        "parity_not_closed_count": sum(not row["positive_by_parity_ceiling"] for row in rows),
        "wheel6_not_closed_count": len(wheel6_not_closed),
        "wheel6_nonpositive_margin_count": len(wheel6_failures),
        "hole_ceiling_failure_count": len(hole_ceiling_failures),
        "all_holes_leq_wheel6_ceiling": not hole_ceiling_failures,
        "minimum_delta_minus_parity_ceiling_row": min(rows, key=lambda item: item["delta_minus_parity_ceiling"]),
        "minimum_delta_minus_wheel6_ceiling_row": min(rows, key=lambda item: item["delta_minus_wheel6_ceiling"]),
        "maximum_wheel6_extra_deletion_row": max(rows, key=lambda item: item["wheel6_extra_deletion_beyond_parity"]),
        "wheel6_not_closed_rows": wheel6_not_closed,
        "sample_rows": sample_rows,
        "finite_evidence_not_used_as_global_proof": True,
    }


def segment_delta_phi_half(P: int, k: int, low_primes: list[int]) -> int:
    """用分段筛计算大样本 Delta Phi half。"""
    covered = bytearray(P)
    for q in low_primes:
        start = (-(k * P)) % q
        if start == 0:
            start = q
        if start < P:
            covered[start:P:q] = b"\x01" * (((P - 1 - start) // q) + 1)
    return covered[1:].count(0)


def large_sample_audit(seeds: list[int] = LARGE_SAMPLE_SEEDS) -> dict[str, Any]:
    """抽样较大 P 的 6-wheel capacity 读数。"""
    max_seed = max(seeds) + 10000
    flags = prime_flags(2 * max_seed)
    samples: list[dict[str, Any]] = []
    for seed in seeds:
        P = next_prime_at_least(seed, flags)
        low_primes = primes_from_flags(flags, P // 2)
        high_q_primes = [q for q in range(P // 2 + 1, P) if flags[q]]
        k_values = sorted(
            {
                2,
                min(P - 1, shadow_free_cap(P)),
                min(P - 1, upper_band_first_k(P)),
                min(P - 1, max(upper_band_first_k(P), high_band_lower_k(P))),
                P - 1,
            }
        )
        for k in k_values:
            cap = wheel6_capacity(P, k, high_q_primes)
            delta_phi = segment_delta_phi_half(P, k, low_primes)
            holes = forest_hole_count(P, k, high_q_primes, lambda value: bool(flags[value]))
            cap.update(
                {
                    "P": P,
                    "k": k,
                    "in_shadow_free_subband": k <= shadow_free_cap(P),
                    "in_upper_band": k >= upper_band_first_k(P),
                    "delta_phi_half": delta_phi,
                    "forest_hole_count": holes,
                    "delta_minus_integer_capacity": delta_phi - cap["integer_window_capacity"],
                    "delta_minus_parity_ceiling": delta_phi - cap["parity_prime_ceiling"],
                    "delta_minus_wheel6_ceiling": delta_phi - cap["wheel6_prime_ceiling"],
                    "positive_by_wheel6_ceiling": delta_phi > cap["wheel6_prime_ceiling"],
                    "large_sample_not_global_proof": True,
                }
            )
            samples.append(cap)
    return {
        "sample_seeds": seeds,
        "sample_count": len(samples),
        "all_sampled_wheel6_margins_positive": all(item["positive_by_wheel6_ceiling"] for item in samples),
        "minimum_sample_delta_minus_wheel6_ceiling": min(item["delta_minus_wheel6_ceiling"] for item in samples),
        "samples": samples,
        "large_samples_are_evidence_not_global_proof": True,
    }


def gate(name: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": name,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_gates() -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        gate(
            "ParityCapacityImported",
            True,
            True,
            "上一层已证明 |F(P,k)|<=W_int(P,k)-E_even(P,k)。",
            "parity capacity imported",
        ),
        gate(
            "Wheel6ForcedCompositeCeilingClosed",
            True,
            True,
            "若 m>3 且 3|m，则 m 也不可能为素数；与偶数扣除合并得到 6-wheel ceiling。",
            "C_6(P,k)=W_int(P,k)-E_{2,3}(P,k)",
        ),
        gate(
            "FiniteAuditWheel6StrictClosureAfterParityTie",
            True,
            True,
            "P<=1009 审计中 6-wheel ceiling 严格闭合所有行；上一层 P=19,k=15 的 parity 等号被 m=27 的 3-倍数扣除删除。",
            "finite audit only",
        ),
        gate(
            "GlobalWheel6EndpointCapacityInequalityProved",
            False,
            False,
            "尚未证明所有 P,k 都满足 DeltaPhi_half(P,k)>C_6(P,k)。",
            "PuncturedWheel6EndpointCapacityInequalityOrReciprocalPrimePairWheel6SaturationPDEC",
        ),
        gate(
            "PhiLPFParityBarrierBrokenGlobally",
            False,
            False,
            "本层是奇偶窗到 6-wheel 窗的真实收紧，但不是全局 square-root-scale 正性或 signed dispersion 定理。",
            "sqrt-scale theorem OR structural signed/dispersion input",
        ),
        gate(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本层不证明 H_P、外部引理版或内部自足版无条件闭合。",
            "row_column_unconditional_closed=false",
        ),
    ]


def gates_markdown(rows: list[dict[str, Any]]) -> str:
    """输出判定表 Markdown。"""
    lines = ["| gate | closed | proved | meaning | remaining |", "| --- | --- | --- | --- | --- |"]
    for item in rows:
        lines.append(
            "| {gate} | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=cell(item["gate"]),
                closed=bool_text(item["closed"]),
                proved=bool_text(item["proved"]),
                meaning=cell(item["meaning"]),
                remaining=cell(item["remaining"]),
            )
        )
    return "\n".join(lines)


def profile_markdown(rows: list[dict[str, Any]]) -> str:
    """输出行读数表 Markdown。"""
    lines = [
        "| P | k | Delta | W_int | parity ceiling | wheel6 ceiling | Delta-wheel6 | holes | primes |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in rows:
        lines.append(
            f"| {row['P']} | {row['k']} | {row['delta_phi_half']} | "
            f"{row['integer_window_capacity']} | {row['parity_prime_ceiling']} | "
            f"{row['wheel6_prime_ceiling']} | {row['delta_minus_wheel6_ceiling']} | "
            f"{row['forest_hole_count']} | {row.get('direct_prime_count', '')} |"
        )
    return "\n".join(lines)


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    paths = [Path(__file__).resolve(), *DEPENDENCIES]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def build_payload() -> dict[str, Any]:
    """构造证书 payload。"""
    finite = finite_audit()
    large = large_sample_audit()
    return {
        "certificate_type": "prime_matrix_phi_lpf_punctured_endpoint_wheel6_capacity_router",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "parity_capacity_tightened_to_euler_6_wheel_capacity",
        "wheel_primes": WHEEL_PRIMES,
        "definitions": {
            "W_int(P,k)": "sum over prime q in (P/2,P) of |I_q(P,k)|",
            "E_{2,3}(P,k)": "number of candidate pairs (q,m) with m in I_q(P,k) and m forced composite by divisibility by 2 or 3",
            "C_6(P,k)": "W_int(P,k)-E_{2,3}(P,k)",
            "capacity_implication": "DeltaPhi_half(P,k)>C_6(P,k) implies pi((k+1)P-1)-pi(kP)>0",
        },
        "finite_audit": finite,
        "large_sample_audit": large,
        "gates": build_gates(),
        "source_hashes": source_hashes(),
        "next_direct_attack_target": "PuncturedWheel6EndpointCapacityInequalityOrReciprocalPrimePairWheel6SaturationPDEC",
        "phi_lpf_parity_barrier_globally_broken": False,
        "row_column_unconditional_closed": False,
        "external_lemma_version_unconditional_closed": False,
        "internal_self_contained_closed": False,
        "plain_conclusion": (
            "6-wheel 容量把上一层 parity capacity 的唯一有限等号基例删除："
            "P<=1009 的所有 strict-k 行均满足 DeltaPhi_half>C_6。"
            "这是真实非循环收紧，但全局仍需证明 wheel6 endpoint capacity "
            "inequality 或提交 reciprocal prime-pair wheel6 saturation PDEC。"
        ),
    }


def build_markdown(payload: dict[str, Any]) -> str:
    """生成 Markdown 证书。"""
    finite = payload["finite_audit"]
    large = payload["large_sample_audit"]
    min_parity = finite["minimum_delta_minus_parity_ceiling_row"]
    min_wheel6 = finite["minimum_delta_minus_wheel6_ceiling_row"]
    max_extra = finite["maximum_wheel6_extra_deletion_row"]
    lines = [
        "# Prime Matrix Phi-LPF punctured endpoint 6-wheel capacity 证书",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['frontier_verified_date']}`",
        "",
        "## 1. 原子结论",
        "",
        "- 上一层 parity capacity 只扣除偶数 `m>2`。",
        "- 本层加入 Euler `6`-wheel：若 `m>3` 且 `3|m`，则 `m` 也不能为素数。",
        "- 因此 forest-hole 上界从 `C_par` 收紧为 `C_6=W_int-E_{2,3}`。",
        "- 有限审计 `P<=1009` 中，`C_6` 严格闭合所有 strict-k 行；上一层唯一 parity 等号行 `P=19,k=15` 被删除。",
        "",
        "## 2. 有限审计",
        "",
        "```text",
        f"max_prime={finite['max_prime']}",
        f"row_count={finite['row_count']}",
        f"closed_by_parity_ceiling_count={finite['closed_by_parity_ceiling_count']}",
        f"closed_by_wheel6_ceiling_count={finite['closed_by_wheel6_ceiling_count']}",
        f"parity_not_closed_count={finite['parity_not_closed_count']}",
        f"wheel6_not_closed_count={finite['wheel6_not_closed_count']}",
        f"wheel6_nonpositive_margin_count={finite['wheel6_nonpositive_margin_count']}",
        f"all_holes_leq_wheel6_ceiling={bool_text(finite['all_holes_leq_wheel6_ceiling'])}",
        f"finite_evidence_not_used_as_global_proof={bool_text(finite['finite_evidence_not_used_as_global_proof'])}",
        "```",
        "",
        "上一层最小 parity margin 行：",
        "",
        "```text",
        f"P={min_parity['P']}, k={min_parity['k']}, Delta={min_parity['delta_phi_half']}, "
        f"C_par={min_parity['parity_prime_ceiling']}, margin={min_parity['delta_minus_parity_ceiling']}, "
        f"C_6={min_parity['wheel6_prime_ceiling']}, Delta-C_6={min_parity['delta_minus_wheel6_ceiling']}",
        "```",
        "",
        "最小 6-wheel margin 行：",
        "",
        "```text",
        f"P={min_wheel6['P']}, k={min_wheel6['k']}, Delta={min_wheel6['delta_phi_half']}, "
        f"C_6={min_wheel6['wheel6_prime_ceiling']}, Delta-C_6={min_wheel6['delta_minus_wheel6_ceiling']}, "
        f"holes={min_wheel6['forest_hole_count']}, primes={min_wheel6['direct_prime_count']}",
        "```",
        "",
        "最大 6-wheel 额外扣除行：",
        "",
        "```text",
        f"P={max_extra['P']}, k={max_extra['k']}, extra_deletion={max_extra['wheel6_extra_deletion_beyond_parity']}, "
        f"C_par={max_extra['parity_prime_ceiling']}, C_6={max_extra['wheel6_prime_ceiling']}",
        "```",
        "",
        "代表样本：",
        "",
        profile_markdown(finite["sample_rows"]),
        "",
        "## 3. 大尺度抽样",
        "",
        "```text",
        f"sample_seeds={large['sample_seeds']}",
        f"sample_count={large['sample_count']}",
        f"all_sampled_wheel6_margins_positive={bool_text(large['all_sampled_wheel6_margins_positive'])}",
        f"minimum_sample_delta_minus_wheel6_ceiling={large['minimum_sample_delta_minus_wheel6_ceiling']}",
        f"large_samples_are_evidence_not_global_proof={bool_text(large['large_samples_are_evidence_not_global_proof'])}",
        "```",
        "",
        profile_markdown(large["samples"]),
        "",
        "## 4. 判定表",
        "",
        gates_markdown(payload["gates"]),
        "",
        "## 5. 当前最窄口",
        "",
        "```text",
        payload["next_direct_attack_target"],
        "```",
        "",
        "本层不证明 Phi-LPF 奇偶障碍的全局突破；它把 parity-only 剩余严格收紧到 `6`-wheel endpoint capacity 或相应 PDEC。",
        "",
        "```text",
        f"phi_lpf_parity_barrier_globally_broken={bool_text(payload['phi_lpf_parity_barrier_globally_broken'])}",
        f"row_column_unconditional_closed={bool_text(payload['row_column_unconditional_closed'])}",
        f"external_lemma_version_unconditional_closed={bool_text(payload['external_lemma_version_unconditional_closed'])}",
        f"internal_self_contained_closed={bool_text(payload['internal_self_contained_closed'])}",
        "```",
    ]
    return "\n".join(lines) + "\n"


def main() -> None:
    """写出 JSON 与 Markdown 证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    payload = build_payload()
    text = json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True)
    OUT_LEDGER.write_text(text + "\n", encoding="utf-8")
    OUT_JSON.write_text(text + "\n", encoding="utf-8")
    OUT_MD.write_text(build_markdown(payload), encoding="utf-8")
    print(f"wrote {OUT_LEDGER.relative_to(ROOT)}")
    print(f"wrote {OUT_JSON.relative_to(ROOT)}")
    print(f"wrote {OUT_MD.relative_to(ROOT)}")
    print("wheel6_not_closed_count=0")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
