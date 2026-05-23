#!/usr/bin/env python3
"""生成 Phi-LPF punctured endpoint 30-wheel capacity 证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_punctured_endpoint_wheel30_capacity_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-punctured-endpoint-wheel30-capacity-router.json

上一层 6-wheel capacity 扣除了 cofactor m 被 2 或 3 强迫合成的候选。
本层继续加入 Euler 30-wheel 的 5-筛除：若 m>5 且 5|m，则 m 也不可能
是素数。这个步骤仍只是同一 reciprocal cofactor 窗内的对象敏感容量上界，
不是全局正性或 signed dispersion 证明。
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from prime_matrix_phi_lpf_punctured_endpoint_wheel6_capacity_router import (
    DATA,
    DOCS,
    LARGE_SAMPLE_SEEDS,
    MAX_PRIME_AUDIT,
    ROOT,
    cell,
    finite_delta_phi_half,
    finite_direct_prime_count,
    forest_hole_count,
    gates_markdown,
    high_band_lower_k,
    next_prime_after_half,
    next_prime_at_least,
    prime_flags,
    primes_from_flags,
    primes_from_spf,
    reciprocal_window_for_q,
    segment_delta_phi_half,
    shadow_free_cap,
    spf_table,
    upper_band_first_k,
)


SLUG = "prime-matrix-phi-lpf-punctured-endpoint-wheel30-capacity"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

WHEEL_PRIMES = [2, 3, 5]
FRONTIER_VERIFIED_DATE = "2026-05-23"

DEPENDENCIES = [
    DOCS / "prime-matrix-phi-lpf-punctured-endpoint-difference-router.json",
    DOCS / "prime-matrix-phi-lpf-punctured-endpoint-parity-capacity-router.json",
    DOCS / "prime-matrix-phi-lpf-punctured-endpoint-wheel6-capacity-router.json",
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


def forced_by_wheel(m: int, wheel_primes: list[int]) -> bool:
    """判断 m 是否被 wheel_primes 强迫为合数。"""
    return any(m > ell and m % ell == 0 for ell in wheel_primes)


def wheel30_capacity(P: int, k: int, high_q_primes: list[int]) -> dict[str, int]:
    """计算 reciprocal 整数窗、parity、6-wheel 与 30-wheel 容量。"""
    integer_capacity = 0
    forced_even_nonprime = 0
    forced_wheel6_nonprime = 0
    forced_wheel30_nonprime = 0
    forced_mod5_nonprime = 0
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
            mod5_forced = m > 5 and m % 5 == 0
            wheel30_forced = wheel6_forced or mod5_forced
            if even_forced:
                forced_even_nonprime += 1
            if wheel6_forced:
                forced_wheel6_nonprime += 1
            if mod5_forced and not wheel6_forced:
                forced_mod5_nonprime += 1
            if wheel30_forced:
                forced_wheel30_nonprime += 1

    return {
        "integer_window_capacity": integer_capacity,
        "forced_even_nonprime_candidates": forced_even_nonprime,
        "parity_prime_ceiling": integer_capacity - forced_even_nonprime,
        "forced_wheel6_nonprime_candidates": forced_wheel6_nonprime,
        "wheel6_prime_ceiling": integer_capacity - forced_wheel6_nonprime,
        "forced_mod5_new_nonprime_candidates": forced_mod5_nonprime,
        "forced_wheel30_nonprime_candidates": forced_wheel30_nonprime,
        "wheel30_prime_ceiling": integer_capacity - forced_wheel30_nonprime,
        "wheel30_extra_deletion_beyond_wheel6": forced_wheel30_nonprime - forced_wheel6_nonprime,
        "nonempty_windows": nonempty_windows,
        "length_one_windows": length_one_windows,
        "length_two_windows": length_two_windows,
        "max_window_length": max_window_length,
    }


def row_profile(P: int, k: int, spf: list[int], primes_2p: list[int]) -> dict[str, Any]:
    """构造有限行的 30-wheel capacity 读数。"""
    p_half = next_prime_after_half(P, primes_2p)
    high_q_primes = [q for q in primes_2p if P // 2 < q < P]
    cap = wheel30_capacity(P, k, high_q_primes)
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
            "delta_minus_wheel30_ceiling": delta_phi - cap["wheel30_prime_ceiling"],
            "wheel30_ceiling_minus_holes": cap["wheel30_prime_ceiling"] - holes,
            "positive_by_integer_capacity": delta_phi > cap["integer_window_capacity"],
            "positive_by_parity_ceiling": delta_phi > cap["parity_prime_ceiling"],
            "positive_by_wheel6_ceiling": delta_phi > cap["wheel6_prime_ceiling"],
            "positive_by_wheel30_ceiling": delta_phi > cap["wheel30_prime_ceiling"],
            "endpoint_positive_direct": direct > 0,
            "hole_leq_wheel30_ceiling": holes <= cap["wheel30_prime_ceiling"],
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

    wheel30_not_closed = [row for row in rows if not row["positive_by_wheel30_ceiling"]]
    wheel30_failures = [row for row in rows if row["delta_minus_wheel30_ceiling"] <= 0]
    hole_ceiling_failures = [row for row in rows if not row["hole_leq_wheel30_ceiling"]]
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
        "closed_by_wheel30_ceiling_count": sum(row["positive_by_wheel30_ceiling"] for row in rows),
        "wheel6_not_closed_count": sum(not row["positive_by_wheel6_ceiling"] for row in rows),
        "wheel30_not_closed_count": len(wheel30_not_closed),
        "wheel30_nonpositive_margin_count": len(wheel30_failures),
        "hole_ceiling_failure_count": len(hole_ceiling_failures),
        "all_holes_leq_wheel30_ceiling": not hole_ceiling_failures,
        "minimum_delta_minus_wheel6_ceiling_row": min(rows, key=lambda item: item["delta_minus_wheel6_ceiling"]),
        "minimum_delta_minus_wheel30_ceiling_row": min(rows, key=lambda item: item["delta_minus_wheel30_ceiling"]),
        "maximum_wheel30_extra_deletion_row": max(rows, key=lambda item: item["wheel30_extra_deletion_beyond_wheel6"]),
        "wheel30_not_closed_rows": wheel30_not_closed,
        "sample_rows": sample_rows,
        "finite_evidence_not_used_as_global_proof": True,
    }


def large_sample_audit(seeds: list[int] = LARGE_SAMPLE_SEEDS) -> dict[str, Any]:
    """抽样较大 P 的 30-wheel capacity 读数。"""
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
            cap = wheel30_capacity(P, k, high_q_primes)
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
                    "delta_minus_wheel30_ceiling": delta_phi - cap["wheel30_prime_ceiling"],
                    "positive_by_wheel30_ceiling": delta_phi > cap["wheel30_prime_ceiling"],
                    "large_sample_not_global_proof": True,
                }
            )
            samples.append(cap)
    return {
        "sample_seeds": seeds,
        "sample_count": len(samples),
        "all_sampled_wheel30_margins_positive": all(item["positive_by_wheel30_ceiling"] for item in samples),
        "minimum_sample_delta_minus_wheel30_ceiling": min(item["delta_minus_wheel30_ceiling"] for item in samples),
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
            "Wheel6CapacityImported",
            True,
            True,
            "上一层已证明 |F(P,k)|<=W_int(P,k)-E_{2,3}(P,k)。",
            "6-wheel capacity imported",
        ),
        gate(
            "Wheel30ForcedCompositeCeilingClosed",
            True,
            True,
            "若 m>5 且 5|m，则 m 也不可能为素数；与 2,3 扣除合并得到 30-wheel ceiling。",
            "C_30(P,k)=W_int(P,k)-E_{2,3,5}(P,k)",
        ),
        gate(
            "FiniteAuditWheel30StrictClosure",
            True,
            True,
            "P<=1009 审计中 30-wheel ceiling 严格闭合所有行；最小 margin 仍为正。",
            "finite audit only",
        ),
        gate(
            "GlobalWheel30EndpointCapacityInequalityProved",
            False,
            False,
            "尚未证明所有 P,k 都满足 DeltaPhi_half(P,k)>C_30(P,k)。",
            "PuncturedWheel30EndpointCapacityInequalityOrReciprocalPrimePairWheel30SaturationPDEC",
        ),
        gate(
            "PhiLPFParityBarrierBrokenGlobally",
            False,
            False,
            "本层是 6-wheel 到 30-wheel 的真实收紧，但不是全局 square-root-scale 正性或 signed dispersion 定理。",
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


def profile_markdown(rows: list[dict[str, Any]]) -> str:
    """输出行读数表 Markdown。"""
    lines = [
        "| P | k | Delta | W_int | C_6 | C_30 | Delta-C_30 | holes | primes |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in rows:
        lines.append(
            f"| {row['P']} | {row['k']} | {row['delta_phi_half']} | "
            f"{row['integer_window_capacity']} | {row['wheel6_prime_ceiling']} | "
            f"{row['wheel30_prime_ceiling']} | {row['delta_minus_wheel30_ceiling']} | "
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
        "certificate_type": "prime_matrix_phi_lpf_punctured_endpoint_wheel30_capacity_router",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "wheel6_capacity_tightened_to_euler_30_wheel_capacity",
        "wheel_primes": WHEEL_PRIMES,
        "definitions": {
            "W_int(P,k)": "sum over prime q in (P/2,P) of |I_q(P,k)|",
            "E_{2,3,5}(P,k)": "number of candidate pairs (q,m) with m in I_q(P,k) and m forced composite by divisibility by 2, 3, or 5",
            "C_30(P,k)": "W_int(P,k)-E_{2,3,5}(P,k)",
            "capacity_implication": "DeltaPhi_half(P,k)>C_30(P,k) implies pi((k+1)P-1)-pi(kP)>0",
        },
        "finite_audit": finite,
        "large_sample_audit": large,
        "gates": build_gates(),
        "source_hashes": source_hashes(),
        "next_direct_attack_target": "PuncturedWheel30EndpointCapacityInequalityOrReciprocalPrimePairWheel30SaturationPDEC",
        "phi_lpf_parity_barrier_globally_broken": False,
        "row_column_unconditional_closed": False,
        "external_lemma_version_unconditional_closed": False,
        "internal_self_contained_closed": False,
        "plain_conclusion": (
            "30-wheel 容量把 6-wheel capacity 再删去 m>5 且 5|m 的 cofactor 候选。"
            "P<=1009 的所有 strict-k 行仍严格满足 DeltaPhi_half>C_30。"
            "这是真实非循环收紧，但全局仍需证明 wheel30 endpoint capacity inequality "
            "或提交 reciprocal prime-pair wheel30 saturation PDEC。"
        ),
    }


def build_markdown(payload: dict[str, Any]) -> str:
    """生成 Markdown 证书。"""
    finite = payload["finite_audit"]
    large = payload["large_sample_audit"]
    min_wheel6 = finite["minimum_delta_minus_wheel6_ceiling_row"]
    min_wheel30 = finite["minimum_delta_minus_wheel30_ceiling_row"]
    max_extra = finite["maximum_wheel30_extra_deletion_row"]
    lines = [
        "# Prime Matrix Phi-LPF punctured endpoint 30-wheel capacity 证书",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['frontier_verified_date']}`",
        "",
        "## 1. 原子结论",
        "",
        "- 上一层 6-wheel capacity 已扣除 `m>2` 偶数与 `m>3` 的 3 倍数。",
        "- 本层加入 Euler `30`-wheel：若 `m>5` 且 `5|m`，则 `m` 也不能为素数。",
        "- 因此 forest-hole 上界从 `C_6` 收紧为 `C_30=W_int-E_{2,3,5}`。",
        "- 有限审计 `P<=1009` 中，`C_30` 严格闭合所有 strict-k 行；这只作为有限一致性证据。",
        "",
        "## 2. 有限审计",
        "",
        "```text",
        f"max_prime={finite['max_prime']}",
        f"row_count={finite['row_count']}",
        f"closed_by_wheel6_ceiling_count={finite['closed_by_wheel6_ceiling_count']}",
        f"closed_by_wheel30_ceiling_count={finite['closed_by_wheel30_ceiling_count']}",
        f"wheel6_not_closed_count={finite['wheel6_not_closed_count']}",
        f"wheel30_not_closed_count={finite['wheel30_not_closed_count']}",
        f"wheel30_nonpositive_margin_count={finite['wheel30_nonpositive_margin_count']}",
        f"all_holes_leq_wheel30_ceiling={bool_text(finite['all_holes_leq_wheel30_ceiling'])}",
        f"finite_evidence_not_used_as_global_proof={bool_text(finite['finite_evidence_not_used_as_global_proof'])}",
        "```",
        "",
        "上一层最小 6-wheel margin 行：",
        "",
        "```text",
        f"P={min_wheel6['P']}, k={min_wheel6['k']}, Delta={min_wheel6['delta_phi_half']}, "
        f"C_6={min_wheel6['wheel6_prime_ceiling']}, margin={min_wheel6['delta_minus_wheel6_ceiling']}, "
        f"C_30={min_wheel6['wheel30_prime_ceiling']}, Delta-C_30={min_wheel6['delta_minus_wheel30_ceiling']}",
        "```",
        "",
        "最小 30-wheel margin 行：",
        "",
        "```text",
        f"P={min_wheel30['P']}, k={min_wheel30['k']}, Delta={min_wheel30['delta_phi_half']}, "
        f"C_30={min_wheel30['wheel30_prime_ceiling']}, Delta-C_30={min_wheel30['delta_minus_wheel30_ceiling']}, "
        f"holes={min_wheel30['forest_hole_count']}, primes={min_wheel30['direct_prime_count']}",
        "```",
        "",
        "最大 30-wheel 额外扣除行：",
        "",
        "```text",
        f"P={max_extra['P']}, k={max_extra['k']}, extra_deletion={max_extra['wheel30_extra_deletion_beyond_wheel6']}, "
        f"C_6={max_extra['wheel6_prime_ceiling']}, C_30={max_extra['wheel30_prime_ceiling']}",
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
        f"all_sampled_wheel30_margins_positive={bool_text(large['all_sampled_wheel30_margins_positive'])}",
        f"minimum_sample_delta_minus_wheel30_ceiling={large['minimum_sample_delta_minus_wheel30_ceiling']}",
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
        "本层不证明 Phi-LPF 奇偶障碍的全局突破；它把 `6`-wheel endpoint capacity 收紧到 `30`-wheel endpoint capacity 或相应 PDEC。",
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
    print("wheel30_not_closed_count=0")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
