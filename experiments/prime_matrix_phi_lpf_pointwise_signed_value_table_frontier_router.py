#!/usr/bin/env python3
"""生成 Phi-LPF 逐点 signed value table 前沿同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_pointwise_signed_value_table_frontier_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-pointwise-signed-value-table-frontier-router.json

输出：
  data/prime-matrix-phi-lpf-pointwise-signed-value-table-frontier-ledger.json
  docs/monograph/prime-matrix-phi-lpf-pointwise-signed-value-table-frontier-router.json
  docs/monograph/prime-matrix-phi-lpf-pointwise-signed-value-table-frontier-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-pointwise-signed-value-table-frontier"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

SUPPORT_CERT = DOCS / "prime-matrix-phi-lpf-support-stripped-signed-kernel-router.json"
TRANSPORT_CERT = DOCS / "prime-matrix-phi-lpf-bucket-signed-transport-router.json"
UNIT_SEED_CERT = DOCS / "prime-matrix-phi-lpf-signed-transport-unit-seed-router.json"
SQUARE_PACKET_CERT = DOCS / "prime-matrix-phi-lpf-square-base-source-packet-reduction-router.json"
CYCLE_GUARD_CERT = DOCS / "prime-matrix-phi-lpf-source-packet-cycle-guard-sync-router.json"
POINTWISE_ALPHA_CERT = DOCS / "prime-matrix-strict-pointwise-signed-alpha-value-table-router.json"
PRIMITIVE_EXPR_CERT = DOCS / "prime-matrix-strict-primitive-summand-signed-expression-router.json"
NONRECURSIVE_SYNC_CERT = DOCS / "prime-matrix-strict-nonrecursive-breaker-latest-cycle-sync-router.json"

POINTWISE_PHI_TABLE = "PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward"
PRIMITIVE_WEIGHT_EXPR = "ActualNoncanonicalPrimitiveSummandSignedWeightExpressionBeforePushforward"
PRIMITIVE_ORIGIN_ID = "PrimitiveSummandSignedCoefficientOriginIdentityBeforePushforward"
SEED_CYCLE_CUT = "AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
NEW_JOINT_FORMULA = "NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact"
EXACTUV_PAIR = "ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger"
STEP_UPDATE = "PhiLPFRoughCofactorStepLocalFactorUpdateLawBeforePushforward"
ORDERED_COHERENCE = "PhiLPFRoughCofactorOrderedFactorizationCoherenceBeforePushforward"
MODEL_LEDGER = "ExplicitModelGapAndFiniteDPRCLedger"
RATE_LEDGER = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算证据文件哈希。"""
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


def source_hashes() -> dict[str, str]:
    """汇总本证书依赖哈希。"""
    paths = [
        Path(__file__).resolve(),
        SUPPORT_CERT,
        TRANSPORT_CERT,
        UNIT_SEED_CERT,
        SQUARE_PACKET_CERT,
        CYCLE_GUARD_CERT,
        POINTWISE_ALPHA_CERT,
        PRIMITIVE_EXPR_CERT,
        NONRECURSIVE_SYNC_CERT,
    ]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """生成 Phi-LPF pointwise table 前沿判定表。"""
    support = data["support"]
    transport = data["transport"]
    unit_seed = data["unit_seed"]
    square_packet = data["square_packet"]
    cycle_guard = data["cycle_guard"]
    pointwise_alpha = data["pointwise_alpha"]
    primitive_expr = data["primitive_expr"]
    nonrecursive = data["nonrecursive"]

    return [
        row(
            "PhiLPFSupportAndCapacityImported",
            support.get("support_and_capacity_components_closed") is True,
            True,
            "Phi/LPF 已把 `(p,m)` support key、容量和 p>sqrt(N) 零质量全部闭合。",
            "support no longer a signed gap",
        ),
        row(
            "BucketSignedLawAlreadySplit",
            transport.get("unsigned_cofactor_split_identity_proved") is True
            and transport.get("signed_bucket_sum_partition_identity_proved") is True,
            False,
            "bucket signed law 已被拆成 rough-cofactor signed transport 或逐点 signed value table。",
            POINTWISE_PHI_TABLE,
        ),
        row(
            "UnitSeedAndSquareBaseBoundaryImported",
            unit_seed.get("phi_minus_one_prime_row_guard_imported") is True
            and unit_seed.get("unit_preimage_square_seed_identity_proved") is True
            and square_packet.get("no_square_base_private_signed_escape_proved") is True,
            True,
            "Phi 公式中的 `-1` 排除了 prime row；square-base root 也没有私有 signed 出口。",
            POINTWISE_PHI_TABLE,
        ),
        row(
            "CommonPacketSelfProofBlocked",
            cycle_guard.get("common_packet_self_proof_rejected_after_lpf") is True,
            True,
            "若逐点表经 common packet 展开，已有 signed-lane cycle 会把证明带回自身。",
            "new non-circular artifact or controlled exit",
        ),
        row(
            "PointwisePhiLPFTableIsDirectArtifactOnly",
            True,
            False,
            "逐 Phi-LPF bucket signed table 仍是合法旁路，但必须正向给 signed value，不能从 support/count 反推。",
            POINTWISE_PHI_TABLE,
        ),
        row(
            "PointwiseTableFirstFieldIsSignedWeight",
            pointwise_alpha.get("next_direct_attack_target")
            == "PointwiseNonrecursiveSignedAlphaWeightFormulaForEachCarryShellSkeletonRow",
            False,
            "既有逐点 alpha 表审查表明，表的首字段是 signed weight；Phi atom 和变差收费只能随后验证。",
            PRIMITIVE_WEIGHT_EXPR,
        ),
        row(
            "PrimitiveExpressionRequiresOriginIdentity",
            primitive_expr.get("next_direct_attack_target") == PRIMITIVE_ORIGIN_ID,
            False,
            "signed weight expression 本身还不是证明，必须给 pre-Cauchy source-origin 恒等式。",
            PRIMITIVE_ORIGIN_ID,
        ),
        row(
            "ExistingExpansionHitsSignedSourceFixedPoint",
            nonrecursive.get("seed_coordinate_source_cycle_detected") is True
            and nonrecursive.get("current_chain_contains_nonproof_cycle") is True,
            False,
            "沿现有 row-level/source-origin/assignment 展开会回到 signed-source 固定点。",
            f"{SEED_CYCLE_CUT} OR {PDEC_SCOPE} OR {NEW_JOINT_FORMULA}",
        ),
        row(
            "ExactUVAndTransportRemainIndependent",
            True,
            False,
            "即使 signed value 表作为新工件提交，ExactUV entropy/fiber 与 rough-cofactor step coherence 仍是独立门。",
            f"{EXACTUV_PAIR} AND {STEP_UPDATE} AND {ORDERED_COHERENCE}",
        ),
        row(
            "PointwisePhiLPFTableCurrentCorpusProved",
            False,
            False,
            "当前材料没有逐 Phi-LPF key 的 signed coefficient、local factor 和 prepushforward sum identity 表。",
            POINTWISE_PHI_TABLE,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步只同步 direct table 旁路和 signed-source 固定点，不证明三命题无条件闭合。",
            f"({POINTWISE_PHI_TABLE} OR {SEED_CYCLE_CUT} OR {PDEC_SCOPE} OR {NEW_JOINT_FORMULA})",
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """组装 Phi-LPF pointwise signed value table 前沿证书。"""
    data = {
        "support": load_json(SUPPORT_CERT),
        "transport": load_json(TRANSPORT_CERT),
        "unit_seed": load_json(UNIT_SEED_CERT),
        "square_packet": load_json(SQUARE_PACKET_CERT),
        "cycle_guard": load_json(CYCLE_GUARD_CERT),
        "pointwise_alpha": load_json(POINTWISE_ALPHA_CERT),
        "primitive_expr": load_json(PRIMITIVE_EXPR_CERT),
        "nonrecursive": load_json(NONRECURSIVE_SYNC_CERT),
    }
    rows = build_rows(data)
    retained_basis = (
        f"({POINTWISE_PHI_TABLE} OR {SEED_CYCLE_CUT} OR {PDEC_SCOPE} OR {NEW_JOINT_FORMULA}) "
        f"AND {EXACTUV_PAIR} AND {STEP_UPDATE} AND {ORDERED_COHERENCE} "
        f"AND {MODEL_LEDGER} AND {RATE_LEDGER} AND {DSTRUCTURE}"
    )
    return {
        "certificate_type": "prime_matrix_phi_lpf_pointwise_signed_value_table_frontier_router",
        "status": "phi_lpf_pointwise_signed_value_table_synced_to_source_fixed_point_or_new_artifact_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "phi_lpf_pointwise_signed_value_table_frontier_router_closed": True,
        "phi_lpf_support_and_capacity_imported": rows[0]["closed"],
        "bucket_signed_law_downstream_imported": rows[1]["closed"],
        "unit_seed_square_base_boundary_imported": rows[2]["closed"],
        "common_packet_self_proof_blocked": rows[3]["closed"],
        "pointwise_phi_lpf_bucket_signed_value_table_proved": False,
        "primitive_summand_signed_weight_expression_proved": False,
        "primitive_summand_origin_identity_proved": False,
        "seed_cycle_cut_input_proved": False,
        "acyclic_same_set_scope_match_proved": False,
        "new_explicit_joint_constructor_formula_artifact_present": False,
        "exactuv_entropy_fiber_pair_proved": False,
        "rough_cofactor_step_local_factor_update_law_proved": False,
        "rough_cofactor_ordered_factorization_coherence_proved": False,
        "row_column_unconditional_closed": False,
        "target_input_before_router": POINTWISE_PHI_TABLE,
        "next_direct_attack_target": POINTWISE_PHI_TABLE,
        "nonrecursive_breaker_alternatives": [
            SEED_CYCLE_CUT,
            PDEC_SCOPE,
            NEW_JOINT_FORMULA,
        ],
        "parallel_independent_gates": [
            EXACTUV_PAIR,
            f"{STEP_UPDATE} AND {ORDERED_COHERENCE}",
            MODEL_LEDGER,
            RATE_LEDGER,
            DSTRUCTURE,
        ],
        "retained_basis_after_router": retained_basis,
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "Phi/LPF 已经完全支付 support、capacity、candidate-row 和 square-base/root 字段。"
            "因此 direct 旁路 `PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward` "
            "若要闭合，必须作为真正新的 prepushforward signed value artifact 正向给出每个 `(p,m)` key "
            "的 signed coefficient、local factor、alpha/delta side、ExactUV 输出和求和恒等式。"
            "若把该表沿现有 signed-source/source-origin 链展开，会回到已登记的非证明固定点；"
            "所以最新非循环选择是提交这张新表，或转入 seed cycle-cut、same-set PDEC、new joint formula 三个破环口。"
        ),
    }


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix Phi-LPF pointwise signed value table frontier 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"phi_lpf_support_and_capacity_imported={fmt_bool(cert['phi_lpf_support_and_capacity_imported'])}",
        f"bucket_signed_law_downstream_imported={fmt_bool(cert['bucket_signed_law_downstream_imported'])}",
        f"unit_seed_square_base_boundary_imported={fmt_bool(cert['unit_seed_square_base_boundary_imported'])}",
        f"common_packet_self_proof_blocked={fmt_bool(cert['common_packet_self_proof_blocked'])}",
        f"pointwise_phi_lpf_bucket_signed_value_table_proved={fmt_bool(cert['pointwise_phi_lpf_bucket_signed_value_table_proved'])}",
        f"primitive_summand_signed_weight_expression_proved={fmt_bool(cert['primitive_summand_signed_weight_expression_proved'])}",
        f"seed_cycle_cut_input_proved={fmt_bool(cert['seed_cycle_cut_input_proved'])}",
        f"acyclic_same_set_scope_match_proved={fmt_bool(cert['acyclic_same_set_scope_match_proved'])}",
        f"new_explicit_joint_constructor_formula_artifact_present={fmt_bool(cert['new_explicit_joint_constructor_formula_artifact_present'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in cert["gates"]:
        lines.append(
            f"| {cell(item['gate'])} | `{fmt_bool(item['closed'])}` | `{fmt_bool(item['proved'])}` | "
            f"{cell(item['meaning'])} | {cell(item['remaining'])} |"
        )
    lines.extend(
        [
            "",
            "## 2. 最新保留基",
            "",
            "```text",
            cert["retained_basis_after_router"],
            "```",
            "",
            "直接可攻输入：",
            "",
            "```text",
            cert["next_direct_attack_target"],
            "```",
            "",
            "非循环破环替代：",
            "",
            "```text",
            "\n".join(cert["nonrecursive_breaker_alternatives"]),
            "```",
            "",
            "独立守门项：",
            "",
            "```text",
            "\n".join(cert["parallel_independent_gates"]),
            "```",
            "",
            "行/列命题仍未无条件闭合。",
            "",
            "## 3. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in cert["source_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """写出 JSON、ledger 与 Markdown。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    cert = build_certificate()
    text = json.dumps(cert, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    OUT_JSON.write_text(text, encoding="utf-8")
    OUT_LEDGER.write_text(text, encoding="utf-8")
    OUT_MD.write_text(render_markdown(cert), encoding="utf-8")
    print(OUT_LEDGER.relative_to(ROOT))
    print(OUT_JSON.relative_to(ROOT))
    print(OUT_MD.relative_to(ROOT))


if __name__ == "__main__":
    main()
