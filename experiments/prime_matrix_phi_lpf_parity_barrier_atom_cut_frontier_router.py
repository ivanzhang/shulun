#!/usr/bin/env python3
"""生成 Phi-LPF 奇偶性障碍到 signed atom-cut 前沿的同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_parity_barrier_atom_cut_frontier_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-parity-barrier-atom-cut-frontier-router.json

输出：
  data/prime-matrix-phi-lpf-parity-barrier-atom-cut-frontier-ledger.json
  docs/monograph/prime-matrix-phi-lpf-parity-barrier-atom-cut-frontier-router.json
  docs/monograph/prime-matrix-phi-lpf-parity-barrier-atom-cut-frontier-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-parity-barrier-atom-cut-frontier"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PARITY_CONTRACT = DOCS / "prime-matrix-phi-lpf-parity-barrier-prime-distribution-contract-router.json"
MINIMAL_ROUTE = DOCS / "prime-matrix-phi-lpf-minimal-parity-breaker-route-forcing-router.json"
LPF_BUCKET_AUDIT = DOCS / "prime-matrix-phi-lpf-lpf-bucket-count-formula-audit.json"
LPF_ENDPOINT_AUDIT = DOCS / "prime-matrix-phi-lpf-exact-bucket-endpoint-equivalence-audit.json"
OFFDIAG_PURE_ATOM = DOCS / "prime-matrix-phi-lpf-latest-offdiagonal-pure-pair-atom-sync-router.json"
CONSTRUCTOR_EDGE_FIELD = DOCS / "prime-matrix-phi-lpf-latest-constructor-edge-local-field-cut-sync-router.json"
POINTWISE_FRONTIER = DOCS / "prime-matrix-phi-lpf-pointwise-signed-value-table-frontier-router.json"
EXTERNAL_INDEX = DOCS / "external-theorem-index.md"
SYNTHESIS = DOCS / "three-claims-breakthrough-route-synthesis-20260525.md"
ACTUAL_LOAD = DOCS / "three-claims-actual-load-closure-contracts.md"
FORMAL_FRONTIER = DOCS / "three-claims-formal-to-actual-critical-load-frontier.md"
FRONTIER_HONEST = DOCS / "frontier-honest-status-and-true-side-theorems-20260522.md"
PAPER = ROOT / "paper" / "contradiction-field-monograph" / "contradiction-field-monograph.tex"

SOURCE_FILES = [
    Path(__file__).resolve(),
    PARITY_CONTRACT,
    MINIMAL_ROUTE,
    LPF_BUCKET_AUDIT,
    LPF_ENDPOINT_AUDIT,
    OFFDIAG_PURE_ATOM,
    CONSTRUCTOR_EDGE_FIELD,
    POINTWISE_FRONTIER,
    EXTERNAL_INDEX,
    SYNTHESIS,
    ACTUAL_LOAD,
    FORMAL_FRONTIER,
    FRONTIER_HONEST,
    PAPER,
]

PURE_ATOM = "PhiLPFOffDiagonalPureSemiprimePairSignedSeedAtomBeforePushforward"
EDGE_FIELDS = "PhiLPFEdgeLocalTwoPrimeSignedAtomFieldsOrNamedReturnTagBeforePushforward"
ORIENTATION = "PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward"
EXACTUV_RETURN = "PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward"
INTERNAL_TRANSITION = "PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward"
POINTWISE_TABLE = "PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward"
ALPHA_ANCHOR = "AlphaRowAnchorPhaseEmissionFormulaLedger"
ARITH_ID = "IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger"
RANK_CERT = "SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows"
NONZERO_SURVIVAL = "NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward"
ROW_MASS = "SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失文件只能给空字典，不能当作证明。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记本证书依赖哈希。"""
    return {str(path.relative_to(ROOT)): sha256(path) for path in SOURCE_FILES if path.exists()}


def fmt_bool(value: Any) -> str:
    """渲染小写布尔值。"""
    return "true" if bool(value) else "false"


def cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def source_atoms() -> str:
    """返回 source packet 三原子。"""
    return f"{ALPHA_ANCHOR} AND {ARITH_ID} AND {RANK_CERT}"


def corrected_lpf_rows() -> list[dict[str, Any]]:
    """列出 LPF 计数公式的精确修正。"""
    return [
        {
            "object": "all values with least prime factor p, prime p included",
            "exact_formula": "A_p(N)=Phi(floor(N/p); primes<p)",
            "why": "write m=p*a; the cofactor a may be divisible by p, but may not contain primes below p",
        },
        {
            "object": "composites with least prime factor p",
            "exact_formula": "C_p(N)=Phi(floor(N/p); primes<p)-1",
            "why": "subtract the unit cofactor a=1, i.e. the prime value p itself",
        },
        {
            "object": "Legendre-Phi expansion",
            "exact_formula": "Phi(y; primes<p)=sum_{d divides Q_<p} mu(d)*floor(y/d)",
            "why": "the finite Euler product appears only after replacing floors by y/d",
        },
        {
            "object": "periodic boundary",
            "exact_formula": "Phi(y; primes<p)=y*prod_{ell<p}(1-1/ell)+E_p(y)",
            "why": "E_p is a primorial-periodic floor boundary, not a universal half-main error term",
        },
        {
            "object": "rejected heuristic",
            "exact_formula": "(N-p^2)*prod_{ell<=p}(1-1/ell)",
            "why": "wrong scale, wrong endpoint, and wrongly removes cofactor multiples of p",
        },
    ]


def distribution_contract_rows() -> list[dict[str, Any]]:
    """列出真正能突破奇偶性的精确分布合同。"""
    return [
        {
            "contract": "Pointwise theta at sqrt row scale",
            "formula": "theta((kP,(k+1)P))>0 for every 1<=k<P",
            "breaks_parity": True,
            "current_state": "not proved",
            "blocker": "requires pointwise prime existence in every length-P row near P^2",
        },
        {
            "contract": "Psi beyond prime-power tail",
            "formula": "psi(I_{P,k})>PrimePowerTail(I_{P,k})",
            "breaks_parity": True,
            "current_state": "tail identity closed; lower bound not proved",
            "blocker": "pure prime-power tail is bounded, but no rowwise positive psi main term is available",
        },
        {
            "contract": "Signed divisor / Type-I-II family",
            "formula": "source-key consistent Lambda/Mobius decomposition with factorable coefficients",
            "breaks_parity": True,
            "current_state": "not constructed",
            "blocker": "LPF ownership is still an unsigned support ledger before signed atom emission",
        },
        {
            "contract": "Trace/Kloosterman/Kuznetsov family",
            "formula": "completed source-keyed trace family with conductor and coefficient control",
            "breaks_parity": True,
            "current_state": "not admissible yet",
            "blocker": "formal finite trace ledgers lack a uniform source-keyed signed family",
        },
        {
            "contract": "Named PDEC/SAE return",
            "formula": "failure of a uniform signed law returns to a controlled contradiction packet",
            "breaks_parity": True,
            "current_state": "interfaces named, global return not closed",
            "blocker": "current atom failures are not yet converted to a theorem-level contradiction",
        },
    ]


def atom_cut_rows(offdiag: dict[str, Any], edge: dict[str, Any]) -> list[dict[str, Any]]:
    """列出当前最细非循环 signed atom 硬点。"""
    atoms = source_atoms()
    return [
        {
            "frontier": "seed-side pure-pair atom",
            "closed_unsigned": "unique tail=1 atom pq and Phi(floor(N/(pq)),q)-1 tail lift",
            "open_signed_atom": PURE_ATOM,
            "paired_gates": f"{ORIENTATION} AND {EXACTUV_RETURN} AND {INTERNAL_TRANSITION} AND {atoms}",
            "active": offdiag.get("next_primary_attack_target") == PURE_ATOM,
        },
        {
            "frontier": "constructor edge-local field table",
            "closed_unsigned": "owner p, first q, product pq, Ferrers rank/degree and multiplicity-one edge label",
            "open_signed_atom": EDGE_FIELDS,
            "paired_gates": f"{ORIENTATION} AND {EXACTUV_RETURN} AND {INTERNAL_TRANSITION} AND {ROW_MASS} AND {NONZERO_SURVIVAL} AND {atoms}",
            "active": edge.get("next_primary_attack_target") == EDGE_FIELDS,
        },
        {
            "frontier": "internal tail continuation",
            "closed_unsigned": "tail continuation mass is assigned to the same first seed, not a new first seed",
            "open_signed_atom": INTERNAL_TRANSITION,
            "paired_gates": "step multiplier compatibility along the ordered LPF word",
            "active": True,
        },
        {
            "frontier": "single-table bypass",
            "closed_unsigned": "Phi-LPF support keys are fixed",
            "open_signed_atom": POINTWISE_TABLE,
            "paired_gates": "complete prepushforward signed value table on all support keys",
            "active": True,
        },
    ]


def bypass_rows(minimal: dict[str, Any]) -> list[dict[str, Any]]:
    """汇总可绕开 LPF 无符号障碍的路线。"""
    rows = []
    for row in minimal.get("route_forcing_rows", []):
        rows.append(
            {
                "route": row.get("route"),
                "minimal_object": row.get("minimal_object"),
                "open_atom": row.get("open_atom"),
                "chosen_next": row.get("chosen_next", False),
                "directly_breaks_parity": row.get("directly_breaks_parity", False),
            }
        )
    return rows


def build_certificate() -> dict[str, Any]:
    """组装 atom-cut 前沿同步证书。"""
    parity = load_json(PARITY_CONTRACT)
    minimal = load_json(MINIMAL_ROUTE)
    lpf_bucket = load_json(LPF_BUCKET_AUDIT)
    lpf_endpoint = load_json(LPF_ENDPOINT_AUDIT)
    offdiag = load_json(OFFDIAG_PURE_ATOM)
    edge = load_json(CONSTRUCTOR_EDGE_FIELD)
    pointwise = load_json(POINTWISE_FRONTIER)

    rows = atom_cut_rows(offdiag, edge)
    atom_cut_frontier_synced = all(
        [
            parity.get("lpf_correction_closed") is True,
            parity.get("unsigned_lpf_bucket_count_sufficient_for_prime_extraction") is False,
            minimal.get("minimal_route_forcing_closed") is True,
            offdiag.get("next_primary_attack_target") == PURE_ATOM,
            edge.get("next_primary_attack_target") == EDGE_FIELDS,
            offdiag.get("pure_semiprime_pair_signed_seed_atom_proved") is False,
            edge.get("signed_atom_field_table_proved") is False,
            pointwise.get("pointwise_phi_lpf_bucket_signed_value_table_proved") is False,
        ]
    )

    latest_open_gate = (
        "(ParityBarrierContractPinned AND MinimalRouteForcingClosed AND "
        f"{PURE_ATOM} AND {EDGE_FIELDS} AND {ORIENTATION} AND {EXACTUV_RETURN} "
        f"AND {INTERNAL_TRANSITION} AND {source_atoms()} AND {ROW_MASS} AND "
        f"{NONZERO_SURVIVAL}) OR {POINTWISE_TABLE} OR ExactActualNoncanonicalPrimitiveBranchTraceFormulaOrReturn "
        "OR ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn OR NamedPDECOrSAEReturn"
    )

    return {
        "certificate_type": "prime_matrix_phi_lpf_parity_barrier_atom_cut_frontier_router",
        "status": "phi_lpf_parity_barrier_synced_to_atom_cut_frontier_open",
        "verified_date": "2026-05-26",
        "frontier_sync_only": True,
        "same_theorem_target_preserved": True,
        "finite_evidence_not_used_as_global_proof": True,
        "atom_cut_frontier_synced": atom_cut_frontier_synced,
        "parity_barrier_essence": parity.get("parity_barrier_essence"),
        "corrected_lpf_formula": parity.get("lpf_bucket_exact_formula"),
        "lpf_bucket_audit_status": lpf_bucket.get("status"),
        "lpf_endpoint_audit_status": lpf_endpoint.get("status"),
        "legendre_periodic_boundary_not_half_main": parity.get("legendre_periodic_boundary_not_half_main"),
        "unsigned_lpf_bucket_count_sufficient_for_prime_extraction": False,
        "more_wheel_or_lpf_refinement_rejected_as_first_break": minimal.get(
            "more_wheel_or_lpf_refinement_rejected_as_first_break"
        ),
        "corrected_lpf_rows": corrected_lpf_rows(),
        "distribution_contract_rows": distribution_contract_rows(),
        "atom_cut_rows": rows,
        "bypass_rows": bypass_rows(minimal),
        "external_frontier_rows": minimal.get("external_frontier_rows", []),
        "next_seed_side_attack_target": PURE_ATOM,
        "next_constructor_side_attack_target": EDGE_FIELDS,
        "paired_required_attack_targets": [
            ORIENTATION,
            EXACTUV_RETURN,
            INTERNAL_TRANSITION,
            source_atoms(),
            ROW_MASS,
            NONZERO_SURVIVAL,
        ],
        "parallel_direct_bypass": POINTWISE_TABLE,
        "row_column_unconditional_closed": False,
        "latest_open_gate": latest_open_gate,
        "plain_conclusion": (
            "LPF/Phi 的精确计数错误已经修正，但这只关闭了无符号粗数账本。"
            "奇偶性障碍的本质仍是缺少能区分素数与 P2/P3 粗合数的有符号信息。"
            "当前非循环路线已经从 rough cofactor transport 继续压到两个最细 signed atom："
            "offdiagonal pure-pair seed atom 与 constructor edge-local signed fields。"
            "若不改走点态 theta/psi 平方根行分布定理或外部 admissible trace/Type-II family，"
            "下一步必须正面提交这些 atom 的 signed formula、orientation、ExactUV return 和 internal transition。"
        ),
        "source_hashes": source_hashes(),
    }


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix Phi-LPF parity barrier atom-cut frontier 路由",
        "",
        f"**状态：** `{cert['status']}`",
        f"**核验日期：** `{cert['verified_date']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"atom_cut_frontier_synced={fmt_bool(cert['atom_cut_frontier_synced'])}",
        f"corrected_lpf_formula={cert['corrected_lpf_formula']}",
        f"legendre_periodic_boundary_not_half_main={fmt_bool(cert['legendre_periodic_boundary_not_half_main'])}",
        f"unsigned_lpf_bucket_count_sufficient_for_prime_extraction={fmt_bool(cert['unsigned_lpf_bucket_count_sufficient_for_prime_extraction'])}",
        f"more_wheel_or_lpf_refinement_rejected_as_first_break={fmt_bool(cert['more_wheel_or_lpf_refinement_rejected_as_first_break'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. LPF 精确计数修正",
        "",
        "| object | exact formula | why |",
        "| --- | --- | --- |",
    ]
    for row in cert["corrected_lpf_rows"]:
        lines.append(
            f"| {cell(row['object'])} | `{cell(row['exact_formula'])}` | {cell(row['why'])} |"
        )

    lines.extend(
        [
            "",
            "## 2. 真正需要的精确分布合同",
            "",
            "| contract | formula | breaks parity | current state | blocker |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for row in cert["distribution_contract_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    cell(row["contract"]),
                    f"`{cell(row['formula'])}`",
                    f"`{fmt_bool(row['breaks_parity'])}`",
                    cell(row["current_state"]),
                    cell(row["blocker"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 3. 当前 atom-cut 前沿",
            "",
            "| frontier | closed unsigned | open signed atom | paired gates | active |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for row in cert["atom_cut_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    cell(row["frontier"]),
                    cell(row["closed_unsigned"]),
                    f"`{cell(row['open_signed_atom'])}`",
                    cell(row["paired_gates"]),
                    f"`{fmt_bool(row['active'])}`",
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 4. 可绕行路线",
            "",
            "| route | minimal object | open atom | breaks parity | chosen next |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for row in cert["bypass_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    cell(row.get("route", "")),
                    cell(row.get("minimal_object", "")),
                    cell(row.get("open_atom", "")),
                    f"`{fmt_bool(row.get('directly_breaks_parity'))}`",
                    f"`{fmt_bool(row.get('chosen_next'))}`",
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 5. 下一手",
            "",
            "```text",
            f"next_seed_side_attack_target={cert['next_seed_side_attack_target']}",
            f"next_constructor_side_attack_target={cert['next_constructor_side_attack_target']}",
            f"parallel_direct_bypass={cert['parallel_direct_bypass']}",
            "paired_required_attack_targets=" + " AND ".join(cert["paired_required_attack_targets"]),
            "```",
            "",
            "最新开放口：",
            "",
            "```text",
            cert["latest_open_gate"],
            "```",
            "",
            "行/列命题仍未无条件闭合。",
            "",
            "## 6. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in sorted(cert["source_hashes"].items()):
        lines.append(f"| `{path}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """写出 JSON、ledger 与 Markdown。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    cert = build_certificate()
    text = json.dumps(cert, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    OUT_LEDGER.write_text(text, encoding="utf-8")
    OUT_JSON.write_text(text, encoding="utf-8")
    OUT_MD.write_text(render_markdown(cert), encoding="utf-8")
    print(f"atom_cut_frontier_synced={fmt_bool(cert['atom_cut_frontier_synced'])}")
    print(f"next_seed_side_attack_target={cert['next_seed_side_attack_target']}")
    print(f"next_constructor_side_attack_target={cert['next_constructor_side_attack_target']}")
    print(f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
