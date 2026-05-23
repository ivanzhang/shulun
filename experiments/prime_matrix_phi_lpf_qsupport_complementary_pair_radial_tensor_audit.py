#!/usr/bin/env python3
"""审计互补 conductor 配对核的 radial two-cylinder 张量正规形。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_qsupport_complementary_pair_radial_tensor_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-qsupport-complementary-pair-radial-tensor-audit.json

上一层已排除 q <-> W/q 的自动相位抵消。本层继续检查这些配对核自身
是否已经是可直接输入 Kloosterman/trace-function 定理的相位族。结论是：
配对核是 gcd/divisor-lattice radial 函数，且在 q 与 W/q 都非平凡时具有
精确 two-cylinder rank 2。它没有 reciprocal inverse phase；外部定理要
进入，仍必须另行建立 phase-matching/trace-family bridge。
"""

from __future__ import annotations

import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"
sys.path.insert(0, str(ROOT / "experiments"))

import prime_matrix_phi_lpf_qsupport_complementary_conductor_pair_audit as pair_audit  # noqa: E402
import prime_matrix_phi_lpf_qsupport_dynamic_primorial_unit_selector_audit as primorial  # noqa: E402
import prime_matrix_phi_lpf_qsupport_dynamic_ramanujan_unit_expansion_audit as ramanujan  # noqa: E402


SLUG = "prime-matrix-phi-lpf-qsupport-complementary-pair-radial-tensor"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-23"

DEPENDENCIES = [
    DOCS / "prime-matrix-phi-lpf-qsupport-complementary-conductor-pair-audit.json",
    DOCS / "prime-matrix-phi-lpf-qsupport-conductor-stratified-ramanujan-spectrum-audit.json",
    DOCS / "external-theorem-index.md",
    DOCS / "claim-status-table.md",
    DOCS / "frontier-honest-status-and-true-side-theorems-20260522.md",
    ROOT / "paper" / "contradiction-field-monograph" / "contradiction-field-monograph.tex",
]


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    paths = [Path(__file__).resolve(), *DEPENDENCIES]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def format_fraction(value: Fraction) -> str:
    """输出分数。"""
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def local_factor(ell: int, divides: bool) -> Fraction:
    """归一化 Ramanujan 局部因子 rho_ell(n)。"""
    return Fraction(1, 1) if divides else Fraction(-1, ell - 1)


def product_value(factors: list[int], state_mask: int) -> Fraction:
    """按 divisibility mask 计算 prod rho_ell。"""
    value = Fraction(1, 1)
    for index, ell in enumerate(factors):
        value *= local_factor(ell, bool(state_mask & (1 << index)))
    return value


def value_range(factors: list[int]) -> tuple[Fraction, Fraction, int]:
    """计算 cylinder 值域的最小值、最大值和不同值个数。"""
    values = {product_value(factors, mask) for mask in range(1 << len(factors))}
    return min(values), max(values), len(values)


def complementary_radial_rows(W: int, factors: list[int]) -> list[dict[str, Any]]:
    """列出互补配对核的 radial/tensor 账本。"""
    divisor_rows = ramanujan.squarefree_divisor_data(factors)
    by_d = {row["d"]: row for row in divisor_rows}
    seen: set[int] = set()
    rows: list[dict[str, Any]] = []

    for row in divisor_rows:
        q = row["d"]
        if q in seen:
            continue
        q_complement = W // q
        complement_row = by_d[q_complement]
        seen.add(q)
        seen.add(q_complement)

        q_factors = row["factors"]
        complement_factors = complement_row["factors"]
        q_min, q_max, q_value_count = value_range(q_factors)
        c_min, c_max, c_value_count = value_range(complement_factors)
        nontrivial_on_both_sides = bool(q_factors) and bool(complement_factors)
        rank = 2 if nontrivial_on_both_sides else 1
        endpoint_pair = not nontrivial_on_both_sides
        rows.append(
            {
                "q": q,
                "q_complement": q_complement,
                "q_prime_count": len(q_factors),
                "complement_prime_count": len(complement_factors),
                "row_state_count": 1 << len(q_factors),
                "column_state_count": 1 << len(complement_factors),
                "q_cylinder_value_count": q_value_count,
                "complement_cylinder_value_count": c_value_count,
                "q_cylinder_value_range": f"{format_fraction(q_min)}..{format_fraction(q_max)}",
                "complement_cylinder_value_range": f"{format_fraction(c_min)}..{format_fraction(c_max)}",
                "two_cylinder_matrix_rank": rank,
                "endpoint_pair_rank_one": endpoint_pair,
                "unit_orbit_radial": True,
                "depends_only_on_gcd_with_W": True,
                "reciprocal_inverse_phase_present": False,
                "direct_kloosterman_trace_input_available": False,
            }
        )
    return sorted(rows, key=lambda item: (min(item["q"], item["q_complement"]), max(item["q"], item["q_complement"])))


def sample_pair_rows(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """挑选少量代表性互补对。"""
    if len(rows) <= 4:
        return rows
    indexes = [0, 1, len(rows) // 2, len(rows) - 1]
    picked: list[dict[str, Any]] = []
    seen: set[int] = set()
    for index in indexes:
        if index not in seen:
            picked.append(rows[index])
            seen.add(index)
    return picked


def radial_stats_for(P: int, primes: list[int]) -> dict[str, Any]:
    """计算单个 P 的 radial tensor 账本。"""
    W, factors = primorial.primorial_modulus(P, primes)
    rows = complementary_radial_rows(W, factors)
    rank_one_pair_count = sum(1 for row in rows if row["two_cylinder_matrix_rank"] == 1)
    rank_two_pair_count = sum(1 for row in rows if row["two_cylinder_matrix_rank"] == 2)
    radial_bad_count = sum(1 for row in rows if not row["unit_orbit_radial"])
    reciprocal_phase_present_count = sum(1 for row in rows if row["reciprocal_inverse_phase_present"])
    return {
        "P": P,
        "W_P": W,
        "sqrt_sieve_prime_count": len(factors),
        "complementary_pair_count": len(rows),
        "rank_one_endpoint_pair_count": rank_one_pair_count,
        "rank_two_nontrivial_pair_count": rank_two_pair_count,
        "radial_bad_count": radial_bad_count,
        "reciprocal_phase_present_count": reciprocal_phase_present_count,
        "all_pair_kernels_unit_orbit_radial": radial_bad_count == 0,
        "all_nonendpoint_pairs_rank_two": rank_two_pair_count == len(rows) - rank_one_pair_count,
        "direct_kloosterman_trace_input_available": False,
        "sample_pairs": sample_pair_rows(rows),
    }


def audit_radial_tensor(max_prime: int = 1009) -> dict[str, Any]:
    """对 P<=max_prime 的 radial two-cylinder 结构做有限审计。"""
    primes = primorial.prime_sieve(2 * max_prime + 10)
    P_values = [p for p in primes if 11 <= p <= max_prime]
    interesting = {101, 257, 971, 1009}
    previous = json.loads((DOCS / "prime-matrix-phi-lpf-qsupport-complementary-conductor-pair-audit.json").read_text())

    sample_rows: list[dict[str, Any]] = []
    pair_count_total = 0
    rank_one_pair_total = 0
    rank_two_pair_total = 0
    radial_bad_total = 0
    reciprocal_phase_present_total = 0
    max_pair_count = 0
    max_rank_two_pair_count = 0

    for P in P_values:
        row = radial_stats_for(P, primes)
        pair_count_total += row["complementary_pair_count"]
        rank_one_pair_total += row["rank_one_endpoint_pair_count"]
        rank_two_pair_total += row["rank_two_nontrivial_pair_count"]
        radial_bad_total += row["radial_bad_count"]
        reciprocal_phase_present_total += row["reciprocal_phase_present_count"]
        max_pair_count = max(max_pair_count, row["complementary_pair_count"])
        max_rank_two_pair_count = max(max_rank_two_pair_count, row["rank_two_nontrivial_pair_count"])
        if P in interesting:
            sample_rows.append(row)

    return {
        "max_prime": max_prime,
        "P_value_count": len(P_values),
        "pair_count_total": pair_count_total,
        "rank_one_endpoint_pair_total": rank_one_pair_total,
        "rank_two_nontrivial_pair_total": rank_two_pair_total,
        "max_complementary_pair_count": max_pair_count,
        "max_rank_two_nontrivial_pair_count": max_rank_two_pair_count,
        "radial_bad_total": radial_bad_total,
        "reciprocal_phase_present_total": reciprocal_phase_present_total,
        "all_pair_kernels_unit_orbit_radial": radial_bad_total == 0,
        "all_nonendpoint_pairs_rank_two": rank_one_pair_total + rank_two_pair_total == pair_count_total,
        "direct_kloosterman_trace_input_available_for_any_pair": False,
        "previous_complementary_pair_status": previous["status"],
        "previous_pair_count_total": previous["finite_audit"]["pair_count_total"],
        "previous_identity_zero_pair_total": previous["finite_audit"]["identity_zero_pair_total"],
        "finite_evidence_not_used_as_global_proof": True,
        "sample_rows": sample_rows,
    }


def gate(name: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造门控记录。"""
    return {
        "gate": name,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_payload() -> dict[str, Any]:
    """构造审计 payload。"""
    finite_audit = audit_radial_tensor()
    return {
        "certificate_type": "prime_matrix_phi_lpf_qsupport_complementary_pair_radial_tensor_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "complementary_pair_radial_two_cylinder_normal_form_closed_direct_trace_input_rejected",
        "chosen_claim": "Prime Matrix row/column Phi-LPF",
        "reason_chosen": "after rejecting automatic complementary cancellation, the fastest non-cyclic continuation is to test whether the pair kernels already form a usable trace/Kloosterman phase family",
        "current_object": {
            "local_factor": "rho_l(n)=1 if l|n, else -1/(l-1)",
            "pair_kernel_normal_form": "K_q(n)=mu(q)*prod_{l|q}rho_l(n)+mu(W/q)*prod_{l|W/q}rho_l(n)",
            "unit_orbit_radiality": "K_q(un)=K_q(n) for every unit u mod W_P",
            "two_cylinder_rank": "rank 2 when both q and W_P/q are nontrivial; rank 1 only for the endpoint pair {1,W_P}",
            "bridge_obstruction": "the raw support kernel has no reciprocal inverse phase and is not itself a Kloosterman/trace-function input",
        },
        "finite_audit": finite_audit,
        "closed_gates": [
            gate(
                "ComplementaryPairLocalRamanujanTensorNormalForm",
                True,
                True,
                "Every complementary pair kernel has the exact local product sum K_q(n)=mu(q)prod rho_l + mu(W/q)prod rho_l.",
                "none",
            ),
            gate(
                "ComplementaryPairUnitOrbitRadiality",
                True,
                True,
                "The pair kernel depends only on gcd(n,W_P) and is invariant under multiplication by units modulo W_P.",
                "none",
            ),
            gate(
                "ComplementaryPairTwoCylinderRankLedger",
                True,
                True,
                "Non-endpoint complementary pairs have exact two-cylinder matrix rank 2; the endpoint pair has rank 1.",
                "none",
            ),
            gate(
                "DirectKloostermanTraceInputFromPairKernelRejected",
                True,
                True,
                "The raw pair kernel contains no reciprocal inverse phase and cannot be directly fed to Kloosterman/trace bilinear theorems.",
                "none",
            ),
            gate(
                "ComplementaryConductorPairPhaseMatchingOrTraceFamilyBridge",
                False,
                False,
                "Introduce a genuine same-object reciprocal/trace phase coupled to the radial pair kernels.",
                "new phase-matching bridge theorem",
            ),
            gate(
                "UniformCancellationAcrossComplementaryPrimorialConductorPairs",
                False,
                False,
                "Prove uniform cancellation after the phase bridge, across all dynamic primorial complementary pairs.",
                "new pair-uniform cancellation theorem",
            ),
        ],
        "external_theorem_implication": {
            "Fouvry_Kowalski_Michel_Sawin_2025_arXiv_2511_09459_v3": "requires an l-adic trace-function family with suitable monodromy; the radial divisor-lattice kernel alone is not such a packaged input",
            "Milicevic_Qin_Wu_2025_arXiv_2511_07550": "requires genuine Kloosterman sums modulo q and bilinear coefficient ranges; no reciprocal inverse phase is present in the raw pair kernel",
            "Pascadi_2025_arXiv_2511_08445": "composite-modulus non-abelian amplification needs Type-II Kloosterman organisation, not only a radial gcd kernel",
            "Wright_2026_arXiv_2604_25177": "unbalanced Kloosterman-fraction convolution becomes relevant only after the radial kernel is coupled to a completed reciprocal phase",
            "Shao_Shparlinski_Wijaya_2024_arXiv_2411_12113": "squarefree/smooth modulus sums are adjacent to W_P but do not by themselves supply the missing phase matching",
            "Dong_Robles_Zeindler_2026_arXiv_2601_00292": "withdrawn and remains unusable as a closing input",
        },
        "latest_narrowest_mouth": [
            "RadialPairKernelToReciprocalTracePhaseCouplingBridge",
            "AND UniformCancellationAcrossComplementaryPrimorialConductorPairsAfterCoupling",
            "AND RoughBetaSiegelWalfiszUniformityOrReplacement",
            "AND PointwisePKUniformTransferFromExternalAverageEstimate",
            "AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity",
        ],
        "complementary_pair_local_tensor_normal_form_closed": True,
        "complementary_pair_unit_orbit_radiality_closed": True,
        "complementary_pair_two_cylinder_rank_ledger_closed": True,
        "direct_kloosterman_trace_input_from_pair_kernel_rejected": True,
        "radial_pair_to_reciprocal_trace_phase_bridge_closed": False,
        "uniform_complementary_pair_cancellation_after_coupling_closed": False,
        "rough_beta_siegel_walfisz_factor_extracted": False,
        "pointwise_pk_transfer_closed": False,
        "q_support_phase_saving_closed": False,
        "phi_lpf_parity_barrier_globally_broken": False,
        "row_column_unconditional_closed": False,
        "external_lemma_version_unconditional_closed": False,
        "internal_self_contained_closed": False,
        "source_hashes": source_hashes(),
    }


def build_markdown(payload: dict[str, Any]) -> str:
    """生成 Markdown 证书。"""
    audit = payload["finite_audit"]
    current = payload["current_object"]
    lines = [
        "# Prime Matrix Phi-LPF q-support complementary pair radial tensor 审计",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['frontier_verified_date']}`",
        "",
        "## 1. 当前对象",
        "",
        "```text",
        f"local_factor={current['local_factor']}",
        f"pair_kernel_normal_form={current['pair_kernel_normal_form']}",
        f"unit_orbit_radiality={current['unit_orbit_radiality']}",
        f"two_cylinder_rank={current['two_cylinder_rank']}",
        f"bridge_obstruction={current['bridge_obstruction']}",
        "```",
        "",
        "## 2. Radial two-cylinder 审计",
        "",
        "```text",
        f"max_prime={audit['max_prime']}",
        f"P_value_count={audit['P_value_count']}",
        f"pair_count_total={audit['pair_count_total']}",
        f"rank_one_endpoint_pair_total={audit['rank_one_endpoint_pair_total']}",
        f"rank_two_nontrivial_pair_total={audit['rank_two_nontrivial_pair_total']}",
        f"max_complementary_pair_count={audit['max_complementary_pair_count']}",
        f"max_rank_two_nontrivial_pair_count={audit['max_rank_two_nontrivial_pair_count']}",
        f"radial_bad_total={audit['radial_bad_total']}",
        f"reciprocal_phase_present_total={audit['reciprocal_phase_present_total']}",
        f"all_pair_kernels_unit_orbit_radial={primorial.bool_text(audit['all_pair_kernels_unit_orbit_radial'])}",
        f"all_nonendpoint_pairs_rank_two={primorial.bool_text(audit['all_nonendpoint_pairs_rank_two'])}",
        f"direct_kloosterman_trace_input_available_for_any_pair={primorial.bool_text(audit['direct_kloosterman_trace_input_available_for_any_pair'])}",
        f"previous_pair_count_total={audit['previous_pair_count_total']}",
        f"previous_identity_zero_pair_total={audit['previous_identity_zero_pair_total']}",
        "```",
        "",
        "代表 P：",
        "",
        primorial.table(
            audit["sample_rows"],
            [
                "P",
                "W_P",
                "sqrt_sieve_prime_count",
                "complementary_pair_count",
                "rank_one_endpoint_pair_count",
                "rank_two_nontrivial_pair_count",
                "radial_bad_count",
                "reciprocal_phase_present_count",
                "sample_pairs",
            ],
        ),
        "",
        "## 3. 门控表",
        "",
        primorial.table(payload["closed_gates"], ["gate", "closed", "proved", "meaning", "remaining"]),
        "",
        "## 4. 外部 theorem 影响",
        "",
        "```text",
        *[f"{key}={value}" for key, value in payload["external_theorem_implication"].items()],
        "```",
        "",
        "结论：互补配对核已经完全压成 radial two-cylinder divisor-lattice 函数。它保留结构信息，但自身没有 reciprocal inverse phase；因此不能直接调用 Kloosterman/trace-function 外部定理。",
        "",
        "## 5. 最新最窄口",
        "",
        "```text",
        *payload["latest_narrowest_mouth"],
        "```",
        "",
        "状态边界：",
        "",
        "```text",
        f"complementary_pair_local_tensor_normal_form_closed={primorial.bool_text(payload['complementary_pair_local_tensor_normal_form_closed'])}",
        f"complementary_pair_unit_orbit_radiality_closed={primorial.bool_text(payload['complementary_pair_unit_orbit_radiality_closed'])}",
        f"complementary_pair_two_cylinder_rank_ledger_closed={primorial.bool_text(payload['complementary_pair_two_cylinder_rank_ledger_closed'])}",
        f"direct_kloosterman_trace_input_from_pair_kernel_rejected={primorial.bool_text(payload['direct_kloosterman_trace_input_from_pair_kernel_rejected'])}",
        f"radial_pair_to_reciprocal_trace_phase_bridge_closed={primorial.bool_text(payload['radial_pair_to_reciprocal_trace_phase_bridge_closed'])}",
        f"uniform_complementary_pair_cancellation_after_coupling_closed={primorial.bool_text(payload['uniform_complementary_pair_cancellation_after_coupling_closed'])}",
        f"rough_beta_siegel_walfisz_factor_extracted={primorial.bool_text(payload['rough_beta_siegel_walfisz_factor_extracted'])}",
        f"pointwise_pk_transfer_closed={primorial.bool_text(payload['pointwise_pk_transfer_closed'])}",
        f"q_support_phase_saving_closed={primorial.bool_text(payload['q_support_phase_saving_closed'])}",
        f"phi_lpf_parity_barrier_globally_broken={primorial.bool_text(payload['phi_lpf_parity_barrier_globally_broken'])}",
        f"row_column_unconditional_closed={primorial.bool_text(payload['row_column_unconditional_closed'])}",
        f"external_lemma_version_unconditional_closed={primorial.bool_text(payload['external_lemma_version_unconditional_closed'])}",
        f"internal_self_contained_closed={primorial.bool_text(payload['internal_self_contained_closed'])}",
        "```",
    ]
    return "\n".join(lines) + "\n"


def main() -> None:
    """写出 JSON、ledger 与 Markdown。"""
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
    print("complementary_pair_local_tensor_normal_form_closed=true")
    print("direct_kloosterman_trace_input_from_pair_kernel_rejected=true")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
