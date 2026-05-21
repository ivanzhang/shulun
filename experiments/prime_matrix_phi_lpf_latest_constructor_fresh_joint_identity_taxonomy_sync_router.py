#!/usr/bin/env python3
"""生成 Phi-LPF latest constructor fresh-joint identity taxonomy 同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_latest_constructor_fresh_joint_identity_taxonomy_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-latest-constructor-fresh-joint-identity-taxonomy-sync-router.json

输出：
  data/prime-matrix-phi-lpf-latest-constructor-fresh-joint-identity-taxonomy-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-latest-constructor-fresh-joint-identity-taxonomy-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-latest-constructor-fresh-joint-identity-taxonomy-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-latest-constructor-fresh-joint-identity-taxonomy-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PAYLOAD_LOOP_CUT_CERT = (
    DOCS / "prime-matrix-phi-lpf-latest-constructor-source-entropy-payload-loop-cut-sync-router.json"
)
JOINT_FIELD_CERT = DOCS / "prime-matrix-strict-joint-emitter-formula-field-atom-router.json"
IDENTITY_TAXONOMY_CERT = (
    DOCS / "prime-matrix-strict-independent-identity-statement-taxonomy-router.json"
)
ALPHA_WEIGHT_LAW_CERT = DOCS / "prime-matrix-strict-alpha-signed-weight-law-router.json"
SOURCE_TABLE_CERT = DOCS / "prime-matrix-strict-actual-emitter-source-table-router.json"

FRESH_JOINT_DECL = "FreshIndependentPreCauchyJointDeclarationLineOutsideConstructorPayloadLoop"
JOINT_DECL = "PreCauchyJointWordCoefficientEmitterDeclarationLineForActualNoncanonicalSourceTuple"
INDEPENDENT_IDENTITY = "IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger"
MOVING_BLOCK = "ActualNoncanonicalMovingBlockSpreadNCBLKForCounterexampleBranchAndReturn"
JOINT_ROWS = "JointEmitterPrimitiveSummandRowsFormulaBeforePushforward"
JOINT_IDENTITY = "JointEmitterPrepushforwardWordCoefficientIdentityLedger"
JOINT_RETURN = "JointEmitterNoDownstreamRecoveryAndNamedReturnLedger"
ALPHA_ROW = "AlphaRowAnchorPhaseEmissionFormulaLedger"
SAME_UNIT_MULT = "SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows"
ROW_MASS = "SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger"
SIGNED_SURVIVAL = "NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward"
POINTWISE_TABLE = "PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward"
COMPLETE_KEY = "CompletePrimitiveEmitterKeyPartitionLedger"
FIXED_KEY_MULT = "FixedKeyExactUVLocalMultiplicityO1Ledger"
CANONICAL_LOCK = "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary"
INDEPENDENT_BRIDGE = "IndependentActualSourceBridgeNotFactoredThroughExactUVPairEnergyOrJointConstructorLoop"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
EXTERNAL_DIBFI = "ExternalDIBFIKuznetsovDispersionTheoremMatch"
EXACTUV_PAIR = "ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger"
MODEL = "ExplicitModelGapAndFiniteDPRCLedger"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失时不当作证明。"""
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


def source_hashes() -> dict[str, str]:
    """登记本证书依赖哈希。"""
    paths = [
        Path(__file__).resolve(),
        PAYLOAD_LOOP_CUT_CERT,
        JOINT_FIELD_CERT,
        IDENTITY_TAXONOMY_CERT,
        ALPHA_WEIGHT_LAW_CERT,
        SOURCE_TABLE_CERT,
    ]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def build_rows(
    loop_cut: dict[str, Any],
    joint_field: dict[str, Any],
    taxonomy: dict[str, Any],
    alpha_weight: dict[str, Any],
    source_table: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 fresh-joint identity taxonomy 同步判定表。"""
    fresh_imported = (
        loop_cut.get("next_primary_attack_target") == FRESH_JOINT_DECL
        and loop_cut.get("constructor_payload_source_entropy_loop_detected") is True
        and loop_cut.get("raw_constructor_payload_loop_counts_as_closure") is False
    )
    joint_field_imported = (
        joint_field.get("next_direct_attack_target") == JOINT_DECL
        and joint_field.get("joint_productive_field_decomposition_pinned") is True
        and joint_field.get("pre_cauchy_joint_declaration_line_proved") is False
    )
    independent_identity_active = (
        alpha_weight.get("next_direct_attack_target") == INDEPENDENT_IDENTITY
        and alpha_weight.get("independent_noncanonical_precauchy_arithmetic_identity_statement_proved") is False
    )
    taxonomy_imported = (
        taxonomy.get("next_direct_attack_target") == MOVING_BLOCK
        and taxonomy.get("strict_identity_statement_taxonomy_adapter_closed") is True
    )
    source_table_first_line_open = (
        source_table.get("pre_cauchy_constructor_declaration_line_proved") is False
        and source_table.get("primitive_summand_emitter_formula_rows_proved") is False
    )
    reduced_to_moving_block = (
        fresh_imported and joint_field_imported and independent_identity_active and taxonomy_imported
    )
    return [
        row(
            "FreshJointDeclarationImported",
            fresh_imported,
            False,
            "上一层已切掉 constructor payload/source-entropy 自证环，留下新鲜独立 joint declaration。",
            FRESH_JOINT_DECL,
        ),
        row(
            "StrictJointFieldAtomImported",
            joint_field_imported,
            True,
            "strict joint 字段原子化已说明：声明行之前，rows、identity、prepushforward sum 与 return ledger 都不能开始。",
            f"{JOINT_DECL} AND {JOINT_ROWS} AND {JOINT_IDENTITY} AND {JOINT_RETURN}",
        ),
        row(
            "FreshnessDeletesConstructorAntisplitRoute",
            fresh_imported,
            True,
            "fresh 条件禁止再次使用 joint declaration -> built-in pairing -> payload 的 constructor 内部路线。",
            INDEPENDENT_IDENTITY,
        ),
        row(
            "DeclarationLineRequiresIndependentArithmeticIdentity",
            independent_identity_active,
            False,
            "不经 payload 回环的 declaration line 必须作为独立 noncanonical pre-Cauchy 算术恒等式陈述进入。",
            INDEPENDENT_IDENTITY,
        ),
        row(
            "IdentityStatementTaxonomyImported",
            taxonomy_imported,
            True,
            "strict 独立恒等式分类已穷尽 canonical/generic/AP/external/actual-source 类，strict 自足剩余为 moving-block/NC-BLK。",
            MOVING_BLOCK,
        ),
        row(
            "ActualEmitterSourceTableStillNeedsFirstLine",
            source_table_first_line_open,
            False,
            "actual emitter 源表仍缺 pre-Cauchy constructor declaration line 和 primitive rows 公式。",
            f"{MOVING_BLOCK} AND {JOINT_ROWS}",
        ),
        row(
            "FreshJointDeclarationReducedToMovingBlock",
            reduced_to_moving_block,
            False,
            "fresh joint declaration 的独立性要求把黑箱压成 actual noncanonical moving-block spread/NC-BLK。",
            MOVING_BLOCK,
        ),
        row(
            "ActualMovingBlockSpreadNCBLKCurrentCorpusProved",
            False,
            False,
            "当前语料尚未证明 actual noncanonical moving-block spread/NC-BLK。",
            MOVING_BLOCK,
        ),
        row(
            "JointRowsIdentityReturnStillParallel",
            False,
            False,
            "即使 moving-block 输入给出，还需 rows formula、word/coefficient identity 与 no-downstream return ledger。",
            f"{JOINT_ROWS} AND {JOINT_IDENTITY} AND {JOINT_RETURN}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步只把 fresh joint declaration 继续压成 moving-block/NC-BLK；未证明三命题无条件闭合。",
            "row/column theorem still open",
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """组装 fresh-joint identity taxonomy 同步证书。"""
    loop_cut = load_json(PAYLOAD_LOOP_CUT_CERT)
    joint_field = load_json(JOINT_FIELD_CERT)
    taxonomy = load_json(IDENTITY_TAXONOMY_CERT)
    alpha_weight = load_json(ALPHA_WEIGHT_LAW_CERT)
    source_table = load_json(SOURCE_TABLE_CERT)
    rows = build_rows(loop_cut, joint_field, taxonomy, alpha_weight, source_table)
    retained_basis = (
        f"(({ALPHA_ROW} AND {MOVING_BLOCK} AND {SAME_UNIT_MULT} AND {ROW_MASS} "
        f"AND {JOINT_ROWS} AND {JOINT_IDENTITY} AND {JOINT_RETURN}) "
        f"OR {CANONICAL_LOCK} OR {INDEPENDENT_BRIDGE} OR {PDEC_SCOPE} "
        f"OR {POINTWISE_TABLE} OR {EXTERNAL_DIBFI}) AND {SIGNED_SURVIVAL} "
        f"AND {COMPLETE_KEY} AND {FIXED_KEY_MULT} AND {EXACTUV_PAIR} "
        f"AND {MODEL} AND {RATE} AND {DSTRUCTURE}"
    )
    return {
        "certificate_type": "prime_matrix_phi_lpf_latest_constructor_fresh_joint_identity_taxonomy_sync_router",
        "status": "phi_lpf_latest_constructor_fresh_joint_declaration_reduced_to_moving_block_ncb_lk_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "fresh_joint_declaration_imported": rows[0]["closed"],
        "strict_joint_field_atom_imported": rows[1]["closed"],
        "freshness_deletes_constructor_antisplit_route": rows[2]["closed"],
        "declaration_line_requires_independent_arithmetic_identity": rows[3]["closed"],
        "identity_statement_taxonomy_imported": rows[4]["closed"],
        "fresh_joint_declaration_reduced_to_moving_block": rows[6]["closed"],
        "actual_noncanonical_moving_block_spread_ncb_lk_proved": False,
        "joint_emitter_rows_formula_proved": False,
        "joint_word_coefficient_identity_proved": False,
        "joint_emitter_no_downstream_named_return_ledger_proved": False,
        "row_column_unconditional_closed": False,
        "target_input_before_router": FRESH_JOINT_DECL,
        "absorbed_to": MOVING_BLOCK,
        "next_primary_attack_target": MOVING_BLOCK,
        "underlying_joint_declaration_target": JOINT_DECL,
        "latest_retained_basis_after_router": retained_basis,
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步把上一层的 `FreshIndependentPreCauchyJointDeclarationLineOutsideConstructorPayloadLoop` "
            "接到 strict joint 字段原子化与独立恒等式分类。fresh 条件删除 constructor "
            "joint-declaration -> built-in -> payload 旧路线，因此 declaration line 若要成立，必须作为"
            "独立 noncanonical pre-Cauchy 算术恒等式陈述进入。既有 strict 分类已说明该黑箱在自足线中"
            "只能落到 `ActualNoncanonicalMovingBlockSpreadNCBLKForCounterexampleBranchAndReturn`；"
            "该 moving-block/NC-BLK 输入、joint rows、identity 与 return ledger 仍未证明。"
            "行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF latest constructor fresh-joint identity taxonomy sync 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"fresh_joint_declaration_imported={fmt_bool(cert['fresh_joint_declaration_imported'])}",
        f"strict_joint_field_atom_imported={fmt_bool(cert['strict_joint_field_atom_imported'])}",
        f"freshness_deletes_constructor_antisplit_route={fmt_bool(cert['freshness_deletes_constructor_antisplit_route'])}",
        f"declaration_line_requires_independent_arithmetic_identity={fmt_bool(cert['declaration_line_requires_independent_arithmetic_identity'])}",
        f"identity_statement_taxonomy_imported={fmt_bool(cert['identity_statement_taxonomy_imported'])}",
        f"fresh_joint_declaration_reduced_to_moving_block={fmt_bool(cert['fresh_joint_declaration_reduced_to_moving_block'])}",
        f"actual_noncanonical_moving_block_spread_ncb_lk_proved={fmt_bool(cert['actual_noncanonical_moving_block_spread_ncb_lk_proved'])}",
        f"joint_emitter_rows_formula_proved={fmt_bool(cert['joint_emitter_rows_formula_proved'])}",
        f"joint_word_coefficient_identity_proved={fmt_bool(cert['joint_word_coefficient_identity_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        f"next_primary_attack_target={cert['next_primary_attack_target']}",
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
            "## 2. 最新非循环主攻",
            "",
            "```text",
            cert["next_primary_attack_target"],
            "```",
            "",
            "底层 joint declaration 原子：",
            "",
            "```text",
            cert["underlying_joint_declaration_target"],
            "```",
            "",
            "## 3. 最新保留基",
            "",
            "```text",
            cert["latest_retained_basis_after_router"],
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
    for path, digest in cert["source_hashes"].items():
        lines.append(f"| `{cell(path)}` | `{digest}` |")
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
    print(OUT_LEDGER.relative_to(ROOT))
    print(OUT_JSON.relative_to(ROOT))
    print(OUT_MD.relative_to(ROOT))


if __name__ == "__main__":
    main()
