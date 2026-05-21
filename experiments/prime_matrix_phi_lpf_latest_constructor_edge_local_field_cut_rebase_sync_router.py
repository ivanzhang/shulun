#!/usr/bin/env python3
"""生成 latest constructor edge-local field-cut 的 rebase 同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_latest_constructor_edge_local_field_cut_rebase_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-latest-constructor-edge-local-field-cut-rebase-sync-router.json

输出：
  data/prime-matrix-phi-lpf-latest-constructor-edge-local-field-cut-rebase-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-latest-constructor-edge-local-field-cut-rebase-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-latest-constructor-edge-local-field-cut-rebase-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-latest-constructor-edge-local-field-cut-rebase-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

LATEST_REBASE_CERT = (
    DOCS / "prime-matrix-phi-lpf-latest-constructor-two-prime-no-swap-rebase-sync-router.json"
)
OLD_CONSTRUCTOR_FIELD_CUT_CERT = DOCS / "prime-matrix-phi-lpf-latest-constructor-edge-local-field-cut-sync-router.json"
FIELD_CUT_CERT = DOCS / "prime-matrix-phi-lpf-edge-local-two-prime-field-cut-router.json"
SOURCE_PACKET_CERT = DOCS / "prime-matrix-phi-lpf-source-packet-cycle-guard-sync-router.json"

EDGE_LOCAL_FORMULA = "PhiLPFEdgeLocalTwoPrimeSignedInteractionFormulaOrReturnBeforePushforward"
UNSIGNED_EDGE_LABEL = "PhiLPFEdgeLocalTwoPrimeClosedUnsignedEdgeLabelLedgerBeforePushforward"
SIGNED_ATOM_FIELDS = "PhiLPFEdgeLocalTwoPrimeSignedAtomFieldsOrNamedReturnTagBeforePushforward"
OFFDIAG_ORIENTATION = "PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward"
OFFDIAG_EXACTUV = "PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward"
INTERNAL_TRANSITION = "PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward"
POINTWISE_TABLE = "PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward"
ALPHA_ANCHOR = "AlphaRowAnchorPhaseEmissionFormulaLedger"
ARITH_ID = "IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger"
RANK_CERT = "SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows"
SIGNED_SURVIVAL = "NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward"
ROW_MASS = "SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
COMPLETE_KEY = "CompletePrimitiveEmitterKeyPartitionLedger"
FIXED_KEY = "FixedKeyExactUVLocalMultiplicityO1Ledger"
SOURCE_EXACTUV = "ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
HARMONIC = "HarmonicWindowAlpha043PGe3001Upper0850Ledger"
SKELETON = "DynamicRoughSkeletonAlpha043PGe3001Lower401Ledger"
TERMINAL_WFD = "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate"
BRANCH_TRACE = "ExactActualNoncanonicalPrimitiveBranchTraceFormulaOrReturn"
ATOMIC_TRACE = "ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn"
NEW_JOINT = "NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact"
SEED_CYCLE_CUT = "AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失不能当成闭合证明。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """把布尔值格式化为小写文本。"""
    return "true" if bool(value) else "false"


def cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def dependency_paths() -> list[Path]:
    """列出本层依赖证书。"""
    return [LATEST_REBASE_CERT, OLD_CONSTRUCTOR_FIELD_CUT_CERT, FIELD_CUT_CERT, SOURCE_PACKET_CERT]


def missing_sources() -> list[str]:
    """列出缺失依赖文件。"""
    return [str(path.relative_to(ROOT)) for path in dependency_paths() if not path.exists()]


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    paths = [Path(__file__).resolve(), *dependency_paths()]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def source_atoms() -> str:
    """返回 source-packet 三原子。"""
    return f"{ALPHA_ANCHOR} AND {ARITH_ID} AND {RANK_CERT}"


def retained_basis() -> str:
    """给出本层同步后的完整保留基。"""
    return (
        f"(({source_atoms()} AND {SIGNED_ATOM_FIELDS} AND {OFFDIAG_ORIENTATION} "
        f"AND {OFFDIAG_EXACTUV} AND {INTERNAL_TRANSITION} AND {ROW_MASS}) OR "
        f"{POINTWISE_TABLE} OR {BRANCH_TRACE} OR {ATOMIC_TRACE} OR {SEED_CYCLE_CUT} "
        f"OR {PDEC_SCOPE} OR {TERMINAL_WFD} OR {NEW_JOINT}) AND {SIGNED_SURVIVAL} "
        f"AND {SOURCE_EXACTUV} AND {COMPLETE_KEY} AND {FIXED_KEY} AND {HARMONIC} "
        f"AND {SKELETON} AND {RATE} AND {DSTRUCTURE}"
    )


def largest_sample(field_cut: dict[str, Any]) -> dict[str, Any]:
    """抽取 field-cut 证书最大样本读数。"""
    samples = field_cut.get("sample_edge_local_field_audit", [])
    if not samples:
        return {}
    return max(samples, key=lambda item: item.get("N", 0))


def build_rows(
    latest: dict[str, Any],
    old_field: dict[str, Any],
    field_cut: dict[str, Any],
    source_packet: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 edge-local field-cut rebase 判定表。"""
    latest_edge_active = (
        latest.get("next_primary_attack_target") == EDGE_LOCAL_FORMULA
        and latest.get("two_prime_no_swap_rebased") is True
    )
    old_field_reusable = (
        old_field.get("target_input_before_router") == EDGE_LOCAL_FORMULA
        and old_field.get("latest_constructor_basis_replaces_edge_local_formula_with_signed_atom_fields") is True
        and old_field.get("next_primary_attack_target") == SIGNED_ATOM_FIELDS
    )
    field_imported = (
        field_cut.get("target_input_before_router") == EDGE_LOCAL_FORMULA
        and field_cut.get("edge_local_closed_unsigned_label_ledger_proved") is True
    )
    unsigned_closed = (
        field_cut.get("lpf_bucket_product_fields_proved") is True
        and field_cut.get("ferrers_rank_degree_fields_proved") is True
        and field_cut.get("edge_atom_multiplicity_one_proved") is True
        and field_cut.get("edge_label_bijection_proved") is True
    )
    source_cycle_guard = (
        source_packet.get("common_packet_self_proof_blocked") is True
        or source_packet.get("common_packet_self_proof_rejected_after_lpf") is True
    )
    rebase_closed = latest_edge_active and old_field_reusable and field_imported and unsigned_closed
    return [
        row(
            "LatestRebasedEdgeLocalFormulaImported",
            latest_edge_active,
            False,
            "上一层 rebase 已把最新 constructor 窄口压到 canonical edge-local signed formula 或 return。",
            EDGE_LOCAL_FORMULA,
        ),
        row(
            "ExistingConstructorFieldCutReusable",
            old_field_reusable,
            False,
            "旧 constructor edge-local field-cut 同步证书输入相同，可在新 rebase 前沿复用。",
            f"{UNSIGNED_EDGE_LABEL} AND {SIGNED_ATOM_FIELDS}",
        ),
        row(
            "FieldCutRouterImported",
            field_imported,
            True,
            "field-cut 证书剥离 canonical edge 的 closed unsigned label ledger。",
            UNSIGNED_EDGE_LABEL,
        ),
        row(
            "ClosedUnsignedEdgeFieldsExhausted",
            unsigned_closed,
            True,
            "owner、product、LPF bucket、Ferrers rank/degree 和 multiplicity-one 均已由无符号账本支付。",
            UNSIGNED_EDGE_LABEL,
        ),
        row(
            "UnsignedLabelDoesNotEmitSignedAtom",
            field_cut.get("signed_atom_field_table_proved") is False,
            True,
            "closed unsigned edge label 不产生 signed value、local factor、orientation、ExactUV return 或 source-row coefficient。",
            SIGNED_ATOM_FIELDS,
        ),
        row(
            "SourceAtomsCarriedForward",
            source_atoms() in latest.get("paired_required_attack_targets", []) and source_cycle_guard,
            False,
            "source 三原子仍作为 carried input 保留，不能由 field-cut 自证。",
            source_atoms(),
        ),
        row(
            "EdgeLocalFieldCutRebased",
            rebase_closed,
            False,
            "最新 edge-local formula 已同步为 signed atom fields 或 named return tag。",
            SIGNED_ATOM_FIELDS,
        ),
        row(
            "SignedAtomFieldsStillOpen",
            field_cut.get("signed_atom_field_table_proved") is False,
            False,
            "当前材料没有给出 signed atom field table 或 named return tag。",
            SIGNED_ATOM_FIELDS,
        ),
        row(
            "OrientationExactUVTransitionStillOpen",
            field_cut.get("orientation_parity_branch_side_proved") is False
            and field_cut.get("exactuv_fixed_pair_return_tag_proved") is False
            and field_cut.get("paired_required_attack_targets", [])[:3]
            == [OFFDIAG_ORIENTATION, OFFDIAG_EXACTUV, INTERNAL_TRANSITION],
            False,
            "orientation、ExactUV return 与 internal transition 仍是独立门。",
            f"{OFFDIAG_ORIENTATION} AND {OFFDIAG_EXACTUV} AND {INTERNAL_TRANSITION}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本层只做 rebase 同步；未证明 signed atom fields、orientation、ExactUV、internal transition 或 source 三原子。",
            retained_basis(),
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造同步证书。"""
    latest = load_json(LATEST_REBASE_CERT)
    old_field = load_json(OLD_CONSTRUCTOR_FIELD_CUT_CERT)
    field_cut = load_json(FIELD_CUT_CERT)
    source_packet = load_json(SOURCE_PACKET_CERT)
    rows = build_rows(latest, old_field, field_cut, source_packet)
    return {
        "certificate_type": "prime_matrix_phi_lpf_latest_constructor_edge_local_field_cut_rebase_sync_router",
        "status": "phi_lpf_latest_constructor_edge_local_field_cut_rebased_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "counterexample_assumption_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "missing_sources": missing_sources(),
        "latest_rebased_edge_local_formula_imported": rows[0]["closed"],
        "existing_constructor_field_cut_reusable": rows[1]["closed"],
        "field_cut_router_imported": rows[2]["closed"],
        "closed_unsigned_edge_fields_exhausted": rows[3]["closed"],
        "unsigned_label_does_not_emit_signed_atom": rows[4]["closed"],
        "source_atoms_carried_forward": rows[5]["closed"],
        "edge_local_field_cut_rebased": rows[6]["closed"],
        "signed_atom_field_table_proved": False,
        "orientation_parity_branch_side_proved": False,
        "exactuv_fixed_pair_return_tag_proved": False,
        "internal_prime_adjoin_signed_transition_law_proved": False,
        "alpha_row_anchor_phase_emission_formula_proved": False,
        "independent_noncanonical_arithmetic_identity_proved": False,
        "same_unit_exactuv_rank_multiplicity_proved": False,
        "nonzero_signed_row_survival_proved": False,
        "same_formal_unit_row_mass_normalization_proved": False,
        "row_column_unconditional_closed": False,
        "target_input_before_router": EDGE_LOCAL_FORMULA,
        "closed_unsigned_subledger": UNSIGNED_EDGE_LABEL,
        "next_primary_attack_target": SIGNED_ATOM_FIELDS,
        "paired_required_attack_targets": [
            OFFDIAG_ORIENTATION,
            OFFDIAG_EXACTUV,
            INTERNAL_TRANSITION,
            ROW_MASS,
            source_atoms(),
        ],
        "parallel_constructor_side_gates": f"{SIGNED_SURVIVAL} AND {ROW_MASS}",
        "parallel_direct_bypass": POINTWISE_TABLE,
        "latest_retained_basis_after_router": retained_basis(),
        "imported_largest_sample": largest_sample(field_cut),
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步把最新 rebase 后的 constructor `PhiLPFEdgeLocalTwoPrimeSignedInteractionFormulaOrReturnBeforePushforward` "
            "接入 edge-local field-cut 证书。canonical edge 的 owner、product、LPF bucket、Ferrers rank/degree "
            "和 multiplicity-one label 已由无符号账本关闭；剩余推进到 "
            "`PhiLPFEdgeLocalTwoPrimeSignedAtomFieldsOrNamedReturnTagBeforePushforward`。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF latest constructor edge-local field-cut rebase sync 证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"latest_rebased_edge_local_formula_imported={fmt_bool(result['latest_rebased_edge_local_formula_imported'])}",
        f"existing_constructor_field_cut_reusable={fmt_bool(result['existing_constructor_field_cut_reusable'])}",
        f"field_cut_router_imported={fmt_bool(result['field_cut_router_imported'])}",
        f"closed_unsigned_edge_fields_exhausted={fmt_bool(result['closed_unsigned_edge_fields_exhausted'])}",
        f"unsigned_label_does_not_emit_signed_atom={fmt_bool(result['unsigned_label_does_not_emit_signed_atom'])}",
        f"source_atoms_carried_forward={fmt_bool(result['source_atoms_carried_forward'])}",
        f"edge_local_field_cut_rebased={fmt_bool(result['edge_local_field_cut_rebased'])}",
        f"signed_atom_field_table_proved={fmt_bool(result['signed_atom_field_table_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"next_primary_attack_target={result['next_primary_attack_target']}",
        "```",
        "",
        "## 1. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in result["gates"]:
        lines.append(
            f"| `{cell(item['gate'])}` | `{fmt_bool(item['closed'])}` | `{fmt_bool(item['proved'])}` | "
            f"{cell(item['meaning'])} | {cell(item['remaining'])} |"
        )
    sample = result.get("imported_largest_sample", {})
    if sample:
        lines.extend(
            [
                "",
                "## 2. 导入样本读数",
                "",
                "| N | canonical edges | unique labels | closed fields/edge | open fields/edge | ok |",
                "| --- | ---: | ---: | ---: | ---: | --- |",
                (
                    f"| {sample['N']} | {sample['canonical_edges']} | {sample['unique_edge_labels']} | "
                    f"{sample['closed_unsigned_field_count_per_edge']} | {sample['open_signed_field_count_per_edge']} | "
                    f"`{fmt_bool(sample['lpf_bucket_identity_holds'] and sample['row_degree_formula_holds'] and sample['column_degree_formula_holds'] and sample['atom_multiplicity_one_holds'])}` |"
                ),
            ]
        )
    lines.extend(
        [
            "",
            "## 3. 最新保留基",
            "",
            "```text",
            result["latest_retained_basis_after_router"],
            "```",
            "",
            "下一直接主攻：",
            "",
            "```text",
            result["next_primary_attack_target"],
            "```",
            "",
            "配套仍需：",
            "",
            "```text",
            "\n".join(result["paired_required_attack_targets"]),
            "```",
            "",
            "行/列命题仍未无条件闭合。",
            "",
            "## 4. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in result["source_hashes"].items():
        lines.append(f"| `{cell(path)}` | `{digest}` |")
    return "\n".join(lines) + "\n"


def main() -> None:
    """写出 ledger、JSON 与 Markdown 证书。"""
    result = build_result()
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    text = json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    OUT_LEDGER.write_text(text, encoding="utf-8")
    OUT_JSON.write_text(text, encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(OUT_LEDGER.relative_to(ROOT))
    print(OUT_JSON.relative_to(ROOT))
    print(OUT_MD.relative_to(ROOT))


if __name__ == "__main__":
    main()
