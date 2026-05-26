#!/usr/bin/env python3
"""归档 product-window signed expression 到 row-level origin table 的同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_product_window_signed_expression_origin_table_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-product-window-signed-expression-origin-table-sync-router.json

输出：
  data/prime-matrix-phi-lpf-product-window-signed-expression-origin-table-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-product-window-signed-expression-origin-table-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-product-window-signed-expression-origin-table-sync-router.md

本证书承接 product-window explicit alpha/delta signed-summand sync。它把当前第一硬点
`ActualNoncanonicalPrimitiveSummandSignedWeightExpressionBeforePushforward`
接入 strict primitive summand signed-expression router、strict origin-identity router
和 Phi-LPF signed-survival origin-table sync。结论只是一条非循环前沿同步：signed
expression 不能作为证明终点，必须被 row-level clean-core 原始生成表正向产生。
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-product-window-signed-expression-origin-table-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS = DOCS / "prime-matrix-phi-lpf-product-window-explicit-alpha-delta-signed-summand-sync-router.json"
SIGNED_EXPR_ROUTER = DOCS / "prime-matrix-strict-primitive-summand-signed-expression-router.json"
ORIGIN_IDENTITY_ROUTER = DOCS / "prime-matrix-strict-primitive-summand-origin-identity-router.json"
SIGNED_SURVIVAL_ORIGIN_ROUTER = DOCS / "prime-matrix-phi-lpf-signed-survival-origin-table-sync-router.json"
LPF_CANDIDATE_ROUTER = DOCS / "prime-matrix-lpf-candidate-row-map-alpha-rule-router.json"

SIGNED_EXPR = "ActualNoncanonicalPrimitiveSummandSignedWeightExpressionBeforePushforward"
ORIGIN_IDENTITY = "PrimitiveSummandSignedCoefficientOriginIdentityBeforePushforward"
ROW_TABLE = "RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands"
NONZERO_SIGNED_SURVIVAL = "NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward"
ROW_MASS = "SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger"
POINTWISE_TABLE = "PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward"
COMPLETE_KEY = "CompletePrimitiveEmitterKeyPartitionLedger"
ALPHA_DOMAIN = "ActualNoncanonicalAlphaSourceTupleDomainLedger"
ALPHA_WEIGHT = "AlphaPrimitiveCoefficientWeightFormulaLedger"
ALPHA_OUTPUT = "AlphaPrimitiveRowUVKeySignLocalFactorOutputLedger"
ALPHA_RETURN = "AlphaPrimitiveRuleFailureNamedReturnLedger"
DELTA_SIDE = "ActualNoncanonicalSourceTupleToDeltaSidePrimitiveRuleLedger"
PAIRING_COMPAT = "AlphaDeltaPairingCompatibilityBeforeCauchyLedger"
NONZERO_LOCAL = "PrimitiveRuleNonzeroSignLocalFactorLedger"
FIXED_KEY_O1 = "FixedKeyExactUVLocalMultiplicityO1Ledger"
ORIENTATION = "PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward"
EXACTUV_RETURN = "PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward"
INTERNAL_TRANSITION = "PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空字典。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """布尔值小写输出。"""
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
    """登记依赖哈希。"""
    paths = [
        Path(__file__).resolve(),
        PREVIOUS,
        SIGNED_EXPR_ROUTER,
        ORIGIN_IDENTITY_ROUTER,
        SIGNED_SURVIVAL_ORIGIN_ROUTER,
        LPF_CANDIDATE_ROUTER,
    ]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def build_sync_chain() -> list[dict[str, str]]:
    """列出 product-window signed expression 到 row-level table 的同步链。"""
    return [
        {
            "from": SIGNED_EXPR,
            "to": ORIGIN_IDENTITY,
            "meaning": "signed expression 不是证明；必须给 pre-Cauchy signed coefficient 来源恒等式。",
        },
        {
            "from": ORIGIN_IDENTITY,
            "to": ROW_TABLE,
            "meaning": "来源恒等式等价于同一 formal unit 的逐行 clean-core 原始生成表。",
        },
        {
            "from": "LPF/Phi candidate row ownership",
            "to": "unsigned candidate address only",
            "meaning": "最小素因子分桶继续支付候选 row 地址，但不产生 signed coefficient origin。",
        },
        {
            "from": ROW_TABLE,
            "to": "signed coefficient, local factor, exact (u,v), branch key, prepushforward sum identity, named return",
            "meaning": "row-level 表必须正向同时给出 actual primitive summand 的所有 signed 字段。",
        },
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """生成判定表。"""
    previous = data["previous"]
    signed_expr = data["signed_expr"]
    origin_identity = data["origin_identity"]
    signed_survival_origin = data["signed_survival_origin"]
    lpf_candidate = data["lpf_candidate"]

    previous_active = (
        previous.get("next_primary_attack_target") == SIGNED_EXPR
        and previous.get("primitive_summand_signed_expression_still_open") is True
        and previous.get("explicit_alpha_delta_removed_from_product_window_first_target") is True
    )
    signed_expr_imported = (
        signed_expr.get("primitive_summand_signed_expression_router_closed") is True
        and signed_expr.get("next_direct_attack_target") == ORIGIN_IDENTITY
        and signed_expr.get("primitive_summand_signed_coefficient_origin_identity_proved") is False
    )
    origin_identity_imported = (
        origin_identity.get("primitive_summand_origin_identity_router_closed") is True
        and origin_identity.get("next_direct_attack_target") == ROW_TABLE
        and origin_identity.get("row_level_clean_core_origin_generation_table_proved") is False
    )
    signed_survival_origin_imported = (
        signed_survival_origin.get("primitive_expression_reduced_to_origin_identity") is True
        and signed_survival_origin.get("origin_identity_reduced_to_row_level_generation") is True
        and signed_survival_origin.get("next_primary_attack_target") == ROW_TABLE
    )
    lpf_candidate_carried = (
        previous.get("lpf_candidate_row_map_closed") is True
        and lpf_candidate.get("lpf_candidate_row_emission_map_closed") is True
        and signed_survival_origin.get("phi_lpf_candidate_capacity_remains_closed") is True
    )

    return [
        row(
            "ProductWindowSignedExpressionActiveBeforeSync",
            previous_active,
            False,
            "上一层 product-window explicit alpha/delta 同步把第一硬点推进到 signed primitive summand expression。",
            SIGNED_EXPR,
        ),
        row(
            "StrictSignedExpressionRouterImported",
            signed_expr_imported,
            False,
            "strict signed-expression 证书说明表达式名不能自证；必须给 signed coefficient 来源恒等式。",
            ORIGIN_IDENTITY,
        ),
        row(
            "StrictOriginIdentityRouterImported",
            origin_identity_imported,
            False,
            "strict origin-identity 证书把来源恒等式继续压到 row-level clean-core 原始生成表。",
            ROW_TABLE,
        ),
        row(
            "PhiLPFSignedSurvivalOriginTableSyncImported",
            signed_survival_origin_imported,
            False,
            "Phi-LPF signed-survival 线已经独立确认同一压缩：候选容量不能生成 signed origin。",
            ROW_TABLE,
        ),
        row(
            "LPFCandidateOwnershipCarriedButNotSignedOrigin",
            lpf_candidate_carried,
            True,
            "LPF/Phi 最小素因子候选 row ownership 继续可用，但只给无符号地址和 skeleton。",
            ROW_TABLE,
        ),
        row(
            "RowLevelCleanCoreOriginGenerationStillOpen",
            True,
            False,
            "当前材料还没有逐 actual noncanonical primitive summand 的 signed coefficient 原始生成表。",
            ROW_TABLE,
        ),
        row(
            "NonzeroSignedSurvivalStillOpen",
            True,
            False,
            "没有 row-level signed origin table，候选 row 的非零 signed survival 仍不能推出。",
            NONZERO_SIGNED_SURVIVAL,
        ),
        row(
            "SameFormalUnitRowMassStillIndependent",
            True,
            False,
            "即使 row-level 表存在，仍需同一 formal unit 的 row-mass/no-heavy-row 归一化账本。",
            ROW_MASS,
        ),
        row(
            "ProductWindowSignedExpressionRemovedFromFirstTarget",
            all([previous_active, signed_expr_imported, origin_identity_imported, signed_survival_origin_imported]),
            False,
            "product-window 第一主攻不应停在 signed expression 字段名；应推进到 row-level origin generation table。",
            ROW_TABLE,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本证书只同步 signed expression 的来源表前沿，不证明该表、row-mass、ExactUV、orientation 或终端排斥。",
            "row_column_unconditional_closed=false",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造证书对象。"""
    data = {
        "previous": load_json(PREVIOUS),
        "signed_expr": load_json(SIGNED_EXPR_ROUTER),
        "origin_identity": load_json(ORIGIN_IDENTITY_ROUTER),
        "signed_survival_origin": load_json(SIGNED_SURVIVAL_ORIGIN_ROUTER),
        "lpf_candidate": load_json(LPF_CANDIDATE_ROUTER),
    }
    rows = build_rows(data)
    parallel = [
        NONZERO_SIGNED_SURVIVAL,
        ROW_MASS,
        POINTWISE_TABLE,
        COMPLETE_KEY,
        ALPHA_DOMAIN,
        ALPHA_WEIGHT,
        ALPHA_OUTPUT,
        ALPHA_RETURN,
        DELTA_SIDE,
        PAIRING_COMPAT,
        NONZERO_LOCAL,
        FIXED_KEY_O1,
        ORIENTATION,
        EXACTUV_RETURN,
        INTERNAL_TRANSITION,
        RATE,
        DSTRUCTURE,
    ]
    latest_open_basis = f"{ROW_TABLE} AND " + " AND ".join(parallel)
    return {
        "certificate_type": "prime_matrix_phi_lpf_product_window_signed_expression_origin_table_sync_router",
        "status": "product_window_signed_expression_reduced_to_row_level_origin_table_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "counterexample_absence_not_used": True,
        "old_primary_attack_target": SIGNED_EXPR,
        "primitive_expression_reduced_to_origin_identity": data["signed_expr"].get(
            "primitive_summand_signed_expression_router_closed"
        )
        is True,
        "origin_identity_reduced_to_row_level_generation": data["origin_identity"].get(
            "primitive_summand_origin_identity_router_closed"
        )
        is True,
        "phi_lpf_signed_survival_origin_table_imported": data["signed_survival_origin"].get(
            "origin_identity_reduced_to_row_level_generation"
        )
        is True,
        "lpf_candidate_ownership_carried": rows[4]["closed"],
        "product_window_signed_expression_removed_from_first_target": rows[-2]["closed"],
        "row_level_clean_core_origin_generation_table_proved": False,
        "primitive_summand_signed_coefficient_origin_identity_proved": False,
        "primitive_summand_signed_weight_expression_proved": False,
        "nonzero_signed_row_survival_proved": False,
        "same_formal_unit_row_mass_normalization_proved": False,
        "next_primary_attack_target": ROW_TABLE,
        "parallel_primary_attack_targets": parallel,
        "latest_open_basis_summary": latest_open_basis,
        "row_column_unconditional_closed": False,
        "plain_conclusion": (
            "本步把 product-window 最新第一硬点 "
            "`ActualNoncanonicalPrimitiveSummandSignedWeightExpressionBeforePushforward` "
            "接入 strict signed-expression、strict origin-identity 与 Phi-LPF signed-survival origin-table "
            "证书。结论是：signed expression 不能作为证明终点；它必须正向给出 pre-Cauchy signed "
            "coefficient 来源恒等式，而该来源恒等式又等价于逐行 clean-core 原始生成表。LPF/Phi "
            "候选 row ownership 继续保留，但仍不能生成 signed coefficient origin。"
        ),
        "sync_chain": build_sync_chain(),
        "gates": rows,
        "source_hashes": source_hashes(),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix Phi-LPF product-window signed-expression origin-table sync 证书",
        "",
        f"**状态：** `{result['status']}`",
        "**核验日期：** `2026-05-26`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"primitive_expression_reduced_to_origin_identity={fmt_bool(result['primitive_expression_reduced_to_origin_identity'])}",
        f"origin_identity_reduced_to_row_level_generation={fmt_bool(result['origin_identity_reduced_to_row_level_generation'])}",
        f"phi_lpf_signed_survival_origin_table_imported={fmt_bool(result['phi_lpf_signed_survival_origin_table_imported'])}",
        f"lpf_candidate_ownership_carried={fmt_bool(result['lpf_candidate_ownership_carried'])}",
        f"product_window_signed_expression_removed_from_first_target={fmt_bool(result['product_window_signed_expression_removed_from_first_target'])}",
        f"next_primary_attack_target={result['next_primary_attack_target']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 下游同步链",
        "",
        "| from | to | meaning |",
        "| --- | --- | --- |",
    ]
    for item in result["sync_chain"]:
        lines.append(f"| `{cell(item['from'])}` | `{cell(item['to'])}` | {cell(item['meaning'])} |")

    lines.extend(
        [
            "",
            "## 2. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in result["gates"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
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
            "## 3. 最新保留基",
            "",
            "```text",
            result["latest_open_basis_summary"],
            "```",
            "",
            "下一直接主攻：",
            "",
            "```text",
            result["next_primary_attack_target"],
            "```",
            "",
            "并行仍需：",
            "",
            "```text",
            "\n".join(result["parallel_primary_attack_targets"]),
            "```",
            "",
            "严格含义：本证书只同步 signed expression 到 row-level origin table，不证明行/列命题。",
            "",
            "## 4. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in sorted(result["source_hashes"].items()):
        lines.append(f"| `{path}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """生成 JSON 与 Markdown 证书。"""
    result = build_result()
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    OUT_LEDGER.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(
        "product_window_signed_expression_removed_from_first_target="
        f"{fmt_bool(result['product_window_signed_expression_removed_from_first_target'])}"
    )
    print(f"next_primary_attack_target={result['next_primary_attack_target']}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
