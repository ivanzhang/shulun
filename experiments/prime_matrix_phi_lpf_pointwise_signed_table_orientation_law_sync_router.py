#!/usr/bin/env python3
"""生成 Phi-LPF 逐点 signed 表到取向/local-factor 律的同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_pointwise_signed_table_orientation_law_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-pointwise-signed-table-orientation-law-sync-router.json

输出：
  data/prime-matrix-phi-lpf-pointwise-signed-table-orientation-law-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-pointwise-signed-table-orientation-law-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-pointwise-signed-table-orientation-law-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-pointwise-signed-table-orientation-law-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

SIGNED_SPLIT = DOCS / "prime-matrix-phi-lpf-moving-atom-signed-injection-split-router.json"
PHI_POINTWISE = DOCS / "prime-matrix-phi-lpf-pointwise-signed-value-table-frontier-router.json"
ALPHA_VALUE = DOCS / "prime-matrix-strict-pointwise-signed-alpha-value-table-router.json"
ALPHA_WEIGHT = DOCS / "prime-matrix-strict-pointwise-signed-alpha-weight-formula-router.json"
SUMMAND_EXPR = DOCS / "prime-matrix-strict-primitive-summand-signed-expression-router.json"
ORIGIN_ID = DOCS / "prime-matrix-strict-primitive-summand-origin-identity-router.json"
SIGNED_VALUE_CYCLE = DOCS / "prime-matrix-strict-acyclic-signed-value-cycle-sync-router.json"
FIXED_POINT_BREAKER = DOCS / "prime-matrix-strict-signed-source-fixed-point-breaker-router.json"
ORIENTATION_LAW = DOCS / "prime-matrix-strict-row-level-noncircular-orientation-law-router.json"

POINTWISE_VALUE_TABLE = "PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward"
SIGNED_ALPHA_VALUE_TABLE = "PointwiseSignedAlphaValueTableBeforePushforward"
SIGNED_ALPHA_WEIGHT = "PointwiseNonrecursiveSignedAlphaWeightFormula"
PRIMITIVE_SUMMAND = "ActualNoncanonicalPrimitiveSummandSignedWeightExpressionBeforePushforward"
ORIGIN_IDENTITY = "PrimitiveSummandSignedCoefficientOriginIdentityBeforePushforward"
ROW_TABLE = "RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands"
NONCIRCULAR_KERNEL = "NoncircularPreCauchySignedCoefficientEmissionKernelForActualNoncanonicalPrimitiveRows"
ORIENTATION = "PrimitiveOrientationLocalFactorProductLawBeforePushforward"
CONSTRUCTOR_LINE = "ActualNoncanonicalPrimitiveConstructorFormulaLineForEmitter"
ORIENTATION_BIT = "ExactPrimitiveOrientationBitLaw"
LOCAL_FACTOR = "ExactPrimitiveLocalFactorProductIdentity"
SUM_IDENTITY = "PrepushforwardSignedSumIdentity"
SIGNED_SURVIVAL = "NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward"
ROW_MASS = "SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 依赖；缺失视为未闭合。"""
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
    """登记本层依赖哈希。"""
    paths = [
        Path(__file__).resolve(),
        SIGNED_SPLIT,
        PHI_POINTWISE,
        ALPHA_VALUE,
        ALPHA_WEIGHT,
        SUMMAND_EXPR,
        ORIGIN_ID,
        SIGNED_VALUE_CYCLE,
        FIXED_POINT_BREAKER,
        ORIENTATION_LAW,
    ]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def build_rows(deps: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """生成同步判定表。"""
    signed_split = deps["signed_split"]
    phi_pointwise = deps["phi_pointwise"]
    alpha_value = deps["alpha_value"]
    alpha_weight = deps["alpha_weight"]
    summand_expr = deps["summand_expr"]
    origin_id = deps["origin_id"]
    signed_cycle = deps["signed_cycle"]
    fixed_breaker = deps["fixed_breaker"]
    orientation = deps["orientation"]

    latest_imported = signed_split.get("next_primary_attack_target") == POINTWISE_VALUE_TABLE
    phi_pointwise_open = phi_pointwise.get("next_direct_attack_target") == POINTWISE_VALUE_TABLE
    alpha_value_reduced = (
        alpha_value.get("status") == "pointwise_signed_alpha_value_table_reduced_to_nonrecursive_row_weight_formula_open"
    )
    alpha_weight_reduced = (
        alpha_weight.get("status") == "pointwise_signed_alpha_weight_formula_reduced_to_primitive_summand_expression_open"
    )
    summand_reduced = (
        summand_expr.get("status") == "primitive_summand_signed_expression_reduced_to_origin_identity_open"
    )
    origin_reduced = (
        origin_id.get("status") == "primitive_summand_origin_identity_reduced_to_row_level_origin_generation_table_open"
    )
    signed_cycle_detected = (
        signed_cycle.get("status") == "acyclic_signed_value_cycle_synced_to_noncircular_row_level_generation_open"
    )
    fixed_breaker_imported = "NoncircularPreCauchySignedCoefficientEmissionKernel" in (
        fixed_breaker.get("frontier_reduction", "") + fixed_breaker.get("plain_conclusion", "")
    )
    orientation_law_imported = (
        orientation.get("status") == "row_level_noncircular_origin_reduced_to_orientation_local_factor_law_open"
    )
    return [
        row(
            "LatestPointwisePhiLPFSignedTableImported",
            latest_imported and phi_pointwise_open,
            False,
            "moving-atom signed 注入拆分后，最新直接主攻是 Phi-LPF support 上的逐点 signed value table。",
            POINTWISE_VALUE_TABLE,
        ),
        row(
            "PointwiseTableReducedToSignedAlphaWeight",
            alpha_value_reduced,
            False,
            "既有 pointwise signed alpha value table 路由说明：Phi atom/收费/积分只验证已给定 signed weight，首缺口是逐行 signed alpha weight。",
            SIGNED_ALPHA_WEIGHT,
        ),
        row(
            "SignedAlphaWeightReducedToPrimitiveSummandExpression",
            alpha_weight_reduced,
            False,
            "逐行 signed alpha weight 继续压到 actual noncanonical primitive summand 的推前前 signed expression。",
            PRIMITIVE_SUMMAND,
        ),
        row(
            "PrimitiveSummandExpressionReducedToOriginIdentity",
            summand_reduced,
            False,
            "primitive summand 表达式本身不是证明；必须给 pre-Cauchy 来源恒等式。",
            ORIGIN_IDENTITY,
        ),
        row(
            "OriginIdentityReducedToRowLevelGeneration",
            origin_reduced,
            False,
            "来源恒等式等价于逐行 clean-core 原始 signed coefficient 生成表。",
            ROW_TABLE,
        ),
        row(
            "SignedValueCycleDetected",
            signed_cycle_detected,
            True,
            "从 row-level 表经 signed slot/value-map/source identity 又回到 row-level 表；该回路不能自证。",
            NONCIRCULAR_KERNEL,
        ),
        row(
            "NoncircularEmissionKernelImported",
            fixed_breaker_imported,
            False,
            "signed-source fixed-point breaker 要求新增不读取下游 payment/来源表/早期零行覆盖的 pre-Cauchy signed coefficient 发射核。",
            NONCIRCULAR_KERNEL,
        ),
        row(
            "OrientationLocalFactorLawImportedAsFirstField",
            orientation_law_imported,
            False,
            "row-level 非循环取向律路由把发射核的首个不可替代字段压成 orientation/local-factor 乘积律。",
            ORIENTATION,
        ),
        row(
            "UnsignedLPFPhiCannotDetermineOrientation",
            orientation_law_imported,
            True,
            "LPF/Phi、P列锚、CRT skeleton、ExactUV support 都是偶几何数据；它们不能决定反变号 signed coefficient。",
            ORIENTATION,
        ),
        row(
            "OrientationLocalFactorLawCurrentCorpusProved",
            False,
            False,
            "当前材料没有提交 Cauchy/Phi/payment 推前前的 primitive orientation 与 local-factor 乘积律。",
            f"{CONSTRUCTOR_LINE} AND {ORIENTATION_BIT} AND {LOCAL_FACTOR} AND {SUM_IDENTITY}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本层只是把逐点 signed 表同步到更窄取向律，不是三目标命题无条件闭合。",
            f"{ORIENTATION} AND {SIGNED_SURVIVAL} AND {ROW_MASS} AND {RATE} AND {DSTRUCTURE}",
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """组装同步证书。"""
    deps = {
        "signed_split": load_json(SIGNED_SPLIT),
        "phi_pointwise": load_json(PHI_POINTWISE),
        "alpha_value": load_json(ALPHA_VALUE),
        "alpha_weight": load_json(ALPHA_WEIGHT),
        "summand_expr": load_json(SUMMAND_EXPR),
        "origin_id": load_json(ORIGIN_ID),
        "signed_cycle": load_json(SIGNED_VALUE_CYCLE),
        "fixed_breaker": load_json(FIXED_POINT_BREAKER),
        "orientation": load_json(ORIENTATION_LAW),
    }
    rows = build_rows(deps)
    strict_basis = f"{ORIENTATION} AND {SIGNED_SURVIVAL} AND {ROW_MASS} AND {RATE} AND {DSTRUCTURE}"
    retained_basis = (
        f"({ORIENTATION} OR {NONCIRCULAR_KERNEL} OR {ROW_TABLE} OR {POINTWISE_VALUE_TABLE} OR {PDEC_SCOPE}) "
        f"AND {SIGNED_SURVIVAL} AND {ROW_MASS} AND {RATE} AND {DSTRUCTURE}"
    )
    sync_chain = [
        {
            "from": POINTWISE_VALUE_TABLE,
            "to": SIGNED_ALPHA_VALUE_TABLE,
            "meaning": "Phi-LPF 逐点 signed 表在 alpha 侧表现为逐点 signed alpha value table。",
        },
        {
            "from": SIGNED_ALPHA_VALUE_TABLE,
            "to": SIGNED_ALPHA_WEIGHT,
            "meaning": "value table 的几何/收费字段只能验证，首要生成字段是 signed alpha weight。",
        },
        {
            "from": SIGNED_ALPHA_WEIGHT,
            "to": PRIMITIVE_SUMMAND,
            "meaning": "signed alpha weight 必须由 primitive summand 级推前前 signed expression 给出。",
        },
        {
            "from": PRIMITIVE_SUMMAND,
            "to": ORIGIN_IDENTITY,
            "meaning": "signed expression 必须给 pre-Cauchy source origin identity。",
        },
        {
            "from": ORIGIN_IDENTITY,
            "to": ROW_TABLE,
            "meaning": "来源恒等式等价于逐行 clean-core 原始生成表。",
        },
        {
            "from": ROW_TABLE,
            "to": NONCIRCULAR_KERNEL,
            "meaning": "row-level 内部 signed-source 链形成固定点，必须新增非循环发射核。",
        },
        {
            "from": NONCIRCULAR_KERNEL,
            "to": ORIENTATION,
            "meaning": "非循环发射核的首个奇数据字段是 primitive orientation/local-factor 乘积律。",
        },
    ]
    return {
        "certificate_type": "prime_matrix_phi_lpf_pointwise_signed_table_orientation_law_sync_router",
        "status": "phi_lpf_pointwise_signed_table_synced_to_orientation_law_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "target_input_before_router": POINTWISE_VALUE_TABLE,
        "latest_pointwise_phi_lpf_signed_table_imported": rows[0]["closed"],
        "pointwise_table_reduced_to_signed_alpha_weight": rows[1]["closed"],
        "signed_alpha_weight_reduced_to_primitive_summand_expression": rows[2]["closed"],
        "primitive_summand_expression_reduced_to_origin_identity": rows[3]["closed"],
        "origin_identity_reduced_to_row_level_generation": rows[4]["closed"],
        "signed_value_cycle_detected": rows[5]["closed"],
        "noncircular_emission_kernel_imported": rows[6]["closed"],
        "orientation_local_factor_law_imported_as_first_field": rows[7]["closed"],
        "orientation_local_factor_law_proved": False,
        "row_column_unconditional_closed": False,
        "next_primary_attack_target": ORIENTATION,
        "parallel_primary_attack_targets": [
            CONSTRUCTOR_LINE,
            ORIENTATION_BIT,
            LOCAL_FACTOR,
            SUM_IDENTITY,
            SIGNED_SURVIVAL,
            ROW_MASS,
            RATE,
            DSTRUCTURE,
            PDEC_SCOPE,
        ],
        "strict_basis_after_router": strict_basis,
        "latest_retained_basis_after_router": retained_basis,
        "sync_chain": sync_chain,
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            f"本步把最新 `{POINTWISE_VALUE_TABLE}` 接到已有 signed-value 深层路由。逐点表不是最终单点："
            "它先压到逐行 signed alpha weight，再压到 primitive summand signed expression、pre-Cauchy "
            "origin identity 和 row-level clean-core 原始生成表；继续沿 signed slot/value-map 展开会回到 "
            "row-level 表固定点。真正非循环破坏输入必须是 pre-Cauchy signed coefficient 发射核，而该核的"
            f"首个不可替代字段是 `{ORIENTATION}`。LPF/Phi 只给偶几何与容量，不能决定反变号取向。"
            "行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix Phi-LPF pointwise signed table orientation-law sync 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"latest_pointwise_phi_lpf_signed_table_imported={fmt_bool(cert['latest_pointwise_phi_lpf_signed_table_imported'])}",
        f"pointwise_table_reduced_to_signed_alpha_weight={fmt_bool(cert['pointwise_table_reduced_to_signed_alpha_weight'])}",
        f"signed_alpha_weight_reduced_to_primitive_summand_expression={fmt_bool(cert['signed_alpha_weight_reduced_to_primitive_summand_expression'])}",
        f"primitive_summand_expression_reduced_to_origin_identity={fmt_bool(cert['primitive_summand_expression_reduced_to_origin_identity'])}",
        f"origin_identity_reduced_to_row_level_generation={fmt_bool(cert['origin_identity_reduced_to_row_level_generation'])}",
        f"signed_value_cycle_detected={fmt_bool(cert['signed_value_cycle_detected'])}",
        f"noncircular_emission_kernel_imported={fmt_bool(cert['noncircular_emission_kernel_imported'])}",
        f"orientation_local_factor_law_imported_as_first_field={fmt_bool(cert['orientation_local_factor_law_imported_as_first_field'])}",
        f"orientation_local_factor_law_proved={fmt_bool(cert['orientation_local_factor_law_proved'])}",
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
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in cert["gates"]:
        lines.append(
            f"| {cell(item['gate'])} | `{fmt_bool(item['closed'])}` | `{fmt_bool(item['proved'])}` | "
            f"{cell(item['meaning'])} | {cell(item['remaining'])} |"
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
            "行/列命题仍未无条件闭合。",
            "",
            "## 5. 依赖哈希",
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
