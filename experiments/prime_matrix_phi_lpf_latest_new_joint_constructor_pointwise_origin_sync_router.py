#!/usr/bin/env python3
"""生成 Phi-LPF latest constructor 逐点 signed 表到来源恒等式的同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_latest_new_joint_constructor_pointwise_origin_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-latest-new-joint-constructor-pointwise-origin-sync-router.json

输出：
  data/prime-matrix-phi-lpf-latest-new-joint-constructor-pointwise-origin-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-latest-new-joint-constructor-pointwise-origin-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-latest-new-joint-constructor-pointwise-origin-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-latest-new-joint-constructor-pointwise-origin-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

CURRENT_CONSTRUCTOR_POINTWISE = DOCS / (
    "prime-matrix-phi-lpf-latest-new-joint-constructor-moving-atom-signed-table-sync-router.json"
)
GENERAL_POINTWISE_ORIGIN = DOCS / (
    "prime-matrix-phi-lpf-latest-new-joint-pointwise-table-origin-sync-router.json"
)
POINTWISE_FRONTIER = DOCS / "prime-matrix-phi-lpf-pointwise-signed-value-table-frontier-router.json"
SOURCE_SURVIVAL = DOCS / "prime-matrix-phi-lpf-source-entropy-signed-survival-router.json"
ALPHA_WEIGHT = DOCS / "prime-matrix-strict-pointwise-signed-alpha-weight-formula-router.json"
PRIMITIVE_EXPR = DOCS / "prime-matrix-strict-primitive-summand-signed-expression-router.json"
NONRECURSIVE_BREAKER = DOCS / "prime-matrix-strict-nonrecursive-breaker-latest-cycle-sync-router.json"

POINTWISE_TABLE = "PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward"
SIGNED_WEIGHT = "PointwiseNonrecursiveSignedAlphaWeightFormulaForEachCarryShellSkeletonRow"
SIGNED_EXPR = "ActualNoncanonicalPrimitiveSummandSignedWeightExpressionBeforePushforward"
ORIGIN_IDENTITY = "PrimitiveSummandSignedCoefficientOriginIdentityBeforePushforward"
SIGNED_SURVIVAL_ATOM = "NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward"
ROW_MASS = "SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger"
BUCKET_SIGNED_LAW = "PhiLPFBucketSignedCoefficientLawBeforePushforward"
PRIMITIVE_SIGNED_LAW = "AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward"
CYCLE_CUT = "AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
NEW_JOINT = "NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact"
TERMINAL_DESCENT = "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate"
EXACTUV_PAIR = "ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger"
TRANSPORT_COHERENCE = (
    "PhiLPFRoughCofactorStepLocalFactorUpdateLawBeforePushforward AND "
    "PhiLPFRoughCofactorOrderedFactorizationCoherenceBeforePushforward"
)
MODEL = "ExplicitModelGapAndFiniteDPRCLedger"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失不能当作证明。"""
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
    """构造判定行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def dependency_paths() -> list[Path]:
    """列出本层依赖。"""
    return [
        CURRENT_CONSTRUCTOR_POINTWISE,
        GENERAL_POINTWISE_ORIGIN,
        POINTWISE_FRONTIER,
        SOURCE_SURVIVAL,
        ALPHA_WEIGHT,
        PRIMITIVE_EXPR,
        NONRECURSIVE_BREAKER,
    ]


def missing_sources() -> list[str]:
    """列出缺失依赖。"""
    return [str(path.relative_to(ROOT)) for path in dependency_paths() if not path.exists()]


def source_hashes() -> dict[str, str]:
    """登记本脚本和依赖哈希。"""
    paths = [Path(__file__).resolve(), *dependency_paths()]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def sync_chain() -> list[dict[str, str]]:
    """给出 constructor 口径同步链。"""
    return [
        {
            "from": POINTWISE_TABLE,
            "to": SIGNED_WEIGHT,
            "meaning": "constructor 链上的逐点 Phi-LPF signed 表首先必须给每条 carry-shell skeleton row 的 signed weight。",
        },
        {
            "from": SIGNED_WEIGHT,
            "to": SIGNED_EXPR,
            "meaning": "逐行 signed weight 不是 LPF/Phi support 字段；它需要推前前 primitive summand signed expression。",
        },
        {
            "from": SIGNED_EXPR,
            "to": ORIGIN_IDENTITY,
            "meaning": "primitive summand signed expression 还必须由 pre-Cauchy source tuple 来源恒等式正向生成。",
        },
        {
            "from": ORIGIN_IDENTITY,
            "to": f"{CYCLE_CUT} OR {PDEC_SCOPE} OR {NEW_JOINT}",
            "meaning": "沿现有来源链继续展开会回到 signed 坐标-来源闭环；非循环证明只能走破环输入。",
        },
    ]


def build_rows(
    current: dict[str, Any],
    general: dict[str, Any],
    pointwise: dict[str, Any],
    survival: dict[str, Any],
    alpha_weight: dict[str, Any],
    primitive: dict[str, Any],
    breaker: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        row(
            "CurrentConstructorPointwiseTableImported",
            current.get("next_primary_attack_target") == POINTWISE_TABLE
            and current.get("pointwise_signed_table_proved") is False,
            False,
            "最新 constructor moving-atom 层已经把直接主攻推进到逐点 Phi-LPF signed 表。",
            POINTWISE_TABLE,
        ),
        row(
            "GeneralPointwiseOriginRouterImported",
            general.get("target_input_before_router") == POINTWISE_TABLE
            and general.get("absorbed_to") == ORIGIN_IDENTITY
            and general.get("next_primary_attack_target") == ORIGIN_IDENTITY,
            False,
            "既有 latest new-joint pointwise-origin router 已给出逐点表到 primitive origin identity 的非循环拆分模板。",
            ORIGIN_IDENTITY,
        ),
        row(
            "PointwiseFrontierImported",
            pointwise.get("target_input_before_router") == POINTWISE_TABLE
            and pointwise.get("pointwise_phi_lpf_bucket_signed_value_table_proved") is False
            and pointwise.get("common_packet_self_proof_blocked") is True,
            False,
            "LPF/Phi 只支付 support、capacity、owner/root；不能从 common packet 反推逐点 signed coefficient。",
            f"{SIGNED_WEIGHT} OR {CYCLE_CUT} OR {PDEC_SCOPE} OR {NEW_JOINT}",
        ),
        row(
            "PointwiseTableFirstFieldIsSignedWeightImported",
            alpha_weight.get("target_input_before_router") == SIGNED_WEIGHT
            and alpha_weight.get("next_direct_attack_target") == SIGNED_EXPR,
            False,
            "逐点 signed 表的第一可验证字段是 skeleton row 的 signed alpha weight。",
            SIGNED_EXPR,
        ),
        row(
            "PhiLPFSignedSurvivalBoundaryImported",
            survival.get("next_primary_attack_target") == SIGNED_EXPR
            and survival.get("nonzero_signed_row_survival_proved") is False
            and survival.get("same_formal_unit_row_mass_normalization_proved") is False,
            False,
            "候选 LPF/Phi support 不等于 actual signed row 存活；signed survival 与 row-mass 仍是独立边界。",
            f"{SIGNED_SURVIVAL_ATOM} AND {ROW_MASS}",
        ),
        row(
            "PrimitiveExpressionToOriginIdentityImported",
            primitive.get("target_input_before_router") == SIGNED_EXPR
            and primitive.get("next_direct_attack_target") == ORIGIN_IDENTITY
            and primitive.get("expression_must_be_origin_identity") is True,
            False,
            "primitive signed expression 必须升级成逐 summand 的来源恒等式，才是 actual signed coefficient 公式。",
            ORIGIN_IDENTITY,
        ),
        row(
            "ReverseRecoveryBlockedImported",
            primitive.get("zero_row_or_payment_reverse_recovery_blocked") is True
            and primitive.get("canonical_scoped_formula_not_importable") is True,
            True,
            "零行覆盖、payment skeleton、canonical scoped 公式和外部谱估计不能反向恢复 actual signed coefficient。",
            ORIGIN_IDENTITY,
        ),
        row(
            "ExistingExpansionHitsBreakerTriad",
            breaker.get("current_chain_contains_nonproof_cycle") is True
            and breaker.get("seed_cycle_cut_input_proved") is False
            and breaker.get("acyclic_same_set_scope_match_proved") is False
            and breaker.get("new_explicit_joint_constructor_formula_artifact_present") is False,
            False,
            "来源恒等式沿现有 row-level/source-coordinate 链展开会回到 signed-source 固定点。",
            f"{CYCLE_CUT} OR {PDEC_SCOPE} OR {NEW_JOINT}",
        ),
        row(
            "ConstructorPointwiseSignedTableCurrentCorpusProved",
            False,
            False,
            "当前语料仍没有逐 Phi-LPF key 的 signed coefficient、local factor、alpha/delta side 与求和恒等式表。",
            POINTWISE_TABLE,
        ),
        row(
            "ConstructorPrimitiveOriginIdentityCurrentCorpusProved",
            False,
            False,
            "当前语料仍没有每个 actual primitive summand 的 signed coefficient 来源恒等式。",
            ORIGIN_IDENTITY,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本层只完成 constructor 口径的 pointwise-to-origin 同步，不是三目标命题无条件闭合。",
            f"{ORIGIN_IDENTITY} AND {SIGNED_SURVIVAL_ATOM} AND {ROW_MASS}",
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """组装同步证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    current = load_json(CURRENT_CONSTRUCTOR_POINTWISE)
    general = load_json(GENERAL_POINTWISE_ORIGIN)
    pointwise = load_json(POINTWISE_FRONTIER)
    survival = load_json(SOURCE_SURVIVAL)
    alpha_weight = load_json(ALPHA_WEIGHT)
    primitive = load_json(PRIMITIVE_EXPR)
    breaker = load_json(NONRECURSIVE_BREAKER)
    rows = build_rows(
        current=current,
        general=general,
        pointwise=pointwise,
        survival=survival,
        alpha_weight=alpha_weight,
        primitive=primitive,
        breaker=breaker,
    )
    strict_basis = (
        f"({ORIGIN_IDENTITY} AND {SIGNED_SURVIVAL_ATOM} AND {ROW_MASS}) "
        f"OR ({CYCLE_CUT} OR {PDEC_SCOPE} OR {NEW_JOINT})"
    )
    retained_basis = (
        f"(({ORIGIN_IDENTITY} OR {CYCLE_CUT} OR {PDEC_SCOPE} OR {NEW_JOINT} OR "
        f"{TERMINAL_DESCENT}) AND {SIGNED_SURVIVAL_ATOM} AND {ROW_MASS}) AND "
        f"{EXACTUV_PAIR} AND ({TRANSPORT_COHERENCE}) AND {MODEL} AND {RATE} AND {DSTRUCTURE}"
    )
    cert = {
        "certificate_type": "prime_matrix_phi_lpf_latest_new_joint_constructor_pointwise_origin_sync_router",
        "status": "phi_lpf_latest_constructor_pointwise_table_synced_to_origin_identity_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "counterexample_assumption_only": True,
        "missing_sources": missing_sources(),
        "current_constructor_pointwise_table_imported": rows[0]["closed"],
        "general_pointwise_origin_router_imported": rows[1]["closed"],
        "pointwise_frontier_imported": rows[2]["closed"],
        "pointwise_table_first_field_signed_weight_imported": rows[3]["closed"],
        "phi_lpf_signed_survival_boundary_imported": rows[4]["closed"],
        "primitive_expression_to_origin_identity_imported": rows[5]["closed"],
        "reverse_recovery_blocked_imported": rows[6]["closed"],
        "existing_expansion_hits_breaker_triad": rows[7]["closed"],
        "pointwise_signed_table_proved": False,
        "primitive_summand_signed_weight_expression_proved": False,
        "primitive_summand_origin_identity_proved": False,
        "signed_survival_and_row_mass_proved": False,
        "row_column_unconditional_closed": False,
        "target_input_before_router": POINTWISE_TABLE,
        "absorbed_to": ORIGIN_IDENTITY,
        "next_primary_attack_target": ORIGIN_IDENTITY,
        "parallel_primary_attack_targets": [
            SIGNED_SURVIVAL_ATOM,
            ROW_MASS,
            CYCLE_CUT,
            PDEC_SCOPE,
            NEW_JOINT,
            TERMINAL_DESCENT,
            BUCKET_SIGNED_LAW,
            PRIMITIVE_SIGNED_LAW,
            EXACTUV_PAIR,
            TRANSPORT_COHERENCE,
            MODEL,
            RATE,
            DSTRUCTURE,
        ],
        "strict_basis_after_router": strict_basis,
        "latest_retained_basis_after_router": retained_basis,
        "sync_chain": sync_chain(),
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            f"本步把 current constructor 链的 `{POINTWISE_TABLE}` 继续拆到来源字段。"
            "LPF/Phi 桶恒等式只支付 owner/support/capacity/root，不支付 signed coefficient、"
            "local factor 或 orientation。逐点 signed 表若要闭合，必须先给 "
            f"`{SIGNED_WEIGHT}`，再给 `{SIGNED_EXPR}`，最终正向提交 `{ORIGIN_IDENTITY}`。"
            "沿现有来源链展开会回到 signed 坐标-来源闭环，因此非循环出口仍是 "
            f"`{CYCLE_CUT}`、`{PDEC_SCOPE}` 或 `{NEW_JOINT}`；signed survival、row-mass、"
            "ExactUV、rough-cofactor transport/coherence、模型、Rate 和 DStructure 仍开放。"
            "行/列命题仍未无条件闭合。"
        ),
    }
    OUT_LEDGER.write_text(json.dumps(cert, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_JSON.write_text(json.dumps(cert, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(cert), encoding="utf-8")
    return cert


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF latest constructor pointwise-origin sync 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        (
            "current_constructor_pointwise_table_imported="
            f"{fmt_bool(cert['current_constructor_pointwise_table_imported'])}"
        ),
        f"general_pointwise_origin_router_imported={fmt_bool(cert['general_pointwise_origin_router_imported'])}",
        f"pointwise_frontier_imported={fmt_bool(cert['pointwise_frontier_imported'])}",
        f"pointwise_table_first_field_signed_weight_imported={fmt_bool(cert['pointwise_table_first_field_signed_weight_imported'])}",
        f"phi_lpf_signed_survival_boundary_imported={fmt_bool(cert['phi_lpf_signed_survival_boundary_imported'])}",
        f"primitive_expression_to_origin_identity_imported={fmt_bool(cert['primitive_expression_to_origin_identity_imported'])}",
        f"reverse_recovery_blocked_imported={fmt_bool(cert['reverse_recovery_blocked_imported'])}",
        f"existing_expansion_hits_breaker_triad={fmt_bool(cert['existing_expansion_hits_breaker_triad'])}",
        f"pointwise_signed_table_proved={fmt_bool(cert['pointwise_signed_table_proved'])}",
        f"primitive_summand_origin_identity_proved={fmt_bool(cert['primitive_summand_origin_identity_proved'])}",
        f"signed_survival_and_row_mass_proved={fmt_bool(cert['signed_survival_and_row_mass_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        f"next_primary_attack_target={cert['next_primary_attack_target']}",
        "```",
        "",
        "## 1. 同步链",
        "",
        "| from | to | meaning |",
        "| --- | --- | --- |",
    ]
    for item in cert["sync_chain"]:
        lines.append(f"| `{cell(item['from'])}` | `{cell(item['to'])}` | {cell(item['meaning'])} |")
    lines.extend(
        [
            "",
            "## 2. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | ---: | ---: | --- | --- |",
        ]
    )
    for item in cert["gates"]:
        lines.append(
            "| `{gate}` | {closed} | {proved} | {meaning} | {remaining} |".format(
                gate=cell(item["gate"]),
                closed=fmt_bool(item["closed"]),
                proved=fmt_bool(item["proved"]),
                meaning=cell(item["meaning"]),
                remaining=cell(item["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 3. strict 基",
            "",
            "```text",
            cert["strict_basis_after_router"],
            "```",
            "",
            "## 4. 最新保留基",
            "",
            "```text",
            cert["latest_retained_basis_after_router"],
            "```",
            "",
            "下一直接主攻：",
            "",
            "```text",
            cert["next_primary_attack_target"],
            "```",
            "",
            "并行主攻：",
            "",
            "```text",
            "\n".join(cert["parallel_primary_attack_targets"]),
            "```",
            "",
            "## 5. 依赖哈希",
            "",
            "```json",
            json.dumps(cert["source_hashes"], ensure_ascii=False, indent=2),
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """命令行入口。"""
    cert = build_certificate()
    print(json.dumps(cert, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
