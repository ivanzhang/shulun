#!/usr/bin/env python3
"""生成 Phi-LPF signed-survival 到 row-level origin table 的同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_signed_survival_origin_table_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-signed-survival-origin-table-sync-router.json

输出：
  data/prime-matrix-phi-lpf-signed-survival-origin-table-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-signed-survival-origin-table-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-signed-survival-origin-table-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-signed-survival-origin-table-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

SIGNED_SURVIVAL_CERT = DOCS / "prime-matrix-phi-lpf-source-entropy-signed-survival-router.json"
PRIMITIVE_EXPR_CERT = DOCS / "prime-matrix-strict-primitive-summand-signed-expression-router.json"
ORIGIN_ID_CERT = DOCS / "prime-matrix-strict-primitive-summand-origin-identity-router.json"
PHI_LPF_CERT = DOCS / "prime-matrix-phi-recursive-lpf-ownership-router.json"
LPF_CANDIDATE_CERT = DOCS / "prime-matrix-lpf-candidate-row-map-alpha-rule-router.json"

SIGNED_EXPR = "ActualNoncanonicalPrimitiveSummandSignedWeightExpressionBeforePushforward"
ORIGIN_ID = "PrimitiveSummandSignedCoefficientOriginIdentityBeforePushforward"
ROW_TABLE = "RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands"
PHI_CANDIDATE_CAPACITY = "PhiLPFCandidateRowCapacityLowerBoundLedger"
SIGNED_SURVIVAL = "NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward"
ROW_MASS = "SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger"
POINTWISE_TABLE = "PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward"
TERMINAL_DESCENT = "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
COMPLETE_KEY = "CompletePrimitiveEmitterKeyPartitionLedger"
FIXED_KEY_MULT = "FixedKeyExactUVLocalMultiplicityO1Ledger"
EXACTUV_PAIR = "ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空对象，不能把缺失当作证明。"""
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
    """汇总本证书依赖哈希。"""
    paths = [
        Path(__file__).resolve(),
        SIGNED_SURVIVAL_CERT,
        PRIMITIVE_EXPR_CERT,
        ORIGIN_ID_CERT,
        PHI_LPF_CERT,
        LPF_CANDIDATE_CERT,
    ]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def sync_chain() -> list[dict[str, str]]:
    """列出本层同步链条。"""
    return [
        {
            "from": PHI_CANDIDATE_CAPACITY,
            "to": "closed unsigned candidate capacity",
            "meaning": "LPF/Phi 精确桶只支付候选 row 数量与 owner 地址。",
        },
        {
            "from": SIGNED_SURVIVAL,
            "to": SIGNED_EXPR,
            "meaning": "要让候选 row 成为 actual signed row，必须先给推前前 signed summand 表达式。",
        },
        {
            "from": SIGNED_EXPR,
            "to": ORIGIN_ID,
            "meaning": "表达式本身不是证明；必须说明 signed coefficient 的 pre-Cauchy 来源恒等式。",
        },
        {
            "from": ORIGIN_ID,
            "to": ROW_TABLE,
            "meaning": "来源恒等式等价于同一 formal unit 的逐行 clean-core 原始生成表。",
        },
    ]


def build_rows(
    signed_survival: dict[str, Any],
    primitive_expr: dict[str, Any],
    origin_id: dict[str, Any],
    phi_lpf: dict[str, Any],
    lpf_candidate: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 signed-survival 到 origin table 的判定表。"""
    return [
        row(
            "PhiLPFSignedSurvivalFrontierImported",
            signed_survival.get("next_primary_attack_target") == SIGNED_EXPR,
            False,
            "上一层已把 source entropy 的 signed-survival 侧压到 primitive summand signed expression。",
            SIGNED_EXPR,
        ),
        row(
            "PhiLPFCandidateCapacityRemainsClosed",
            phi_lpf.get("phi_recursive_lpf_bucket_formula_proved") is True
            and lpf_candidate.get("lpf_candidate_row_emission_map_closed") is True,
            True,
            "LPF/Phi 候选容量和候选 row owner 地址继续闭合。",
            PHI_CANDIDATE_CAPACITY,
        ),
        row(
            "PrimitiveExpressionRouterImported",
            primitive_expr.get("next_direct_attack_target") == ORIGIN_ID
            and primitive_expr.get("primitive_summand_signed_expression_router_closed") is True,
            False,
            "strict primitive expression 证书已说明 signed expression 必须是来源恒等式。",
            ORIGIN_ID,
        ),
        row(
            "ExpressionNameCannotServeAsProof",
            primitive_expr.get("expression_must_be_origin_identity") is True,
            True,
            "只命名 signed expression 不能产生系数；必须给 pre-Cauchy source tuple 的正向来源。",
            ORIGIN_ID,
        ),
        row(
            "OriginIdentityRouterImported",
            origin_id.get("next_direct_attack_target") == ROW_TABLE
            and origin_id.get("primitive_summand_origin_identity_router_closed") is True,
            False,
            "strict origin identity 证书已把来源恒等式压到逐行 clean-core 原始生成表。",
            ROW_TABLE,
        ),
        row(
            "OriginIdentityEqualsRowLevelGeneration",
            origin_id.get("origin_identity_is_row_level_origin_generation") is True,
            True,
            "若逐行原始生成表存在，它同时给 signed coefficient、local factor、UV key 与推前前求和恒等式。",
            ROW_TABLE,
        ),
        row(
            "UnsignedPhiLPFStillCannotEmitOriginTable",
            signed_survival.get("candidate_rows_are_actual_signed_rows") is False,
            True,
            "LPF/Phi 候选 row 不含 signed coefficient 来源表，不能反推 row-level origin generation。",
            ROW_TABLE,
        ),
        row(
            "RowLevelOriginTableStillOpen",
            origin_id.get("row_level_clean_core_origin_generation_table_proved") is False,
            False,
            "当前材料没有逐 actual noncanonical primitive summand 的原始生成表。",
            ROW_TABLE,
        ),
        row(
            "NonzeroSignedSurvivalStillOpen",
            signed_survival.get("nonzero_signed_row_survival_proved") is False,
            False,
            "没有 row-level signed origin table，Phi-LPF 候选 row 的非零 signed survival 仍未证明。",
            SIGNED_SURVIVAL,
        ),
        row(
            "RowMassStillIndependent",
            signed_survival.get("same_formal_unit_row_mass_normalization_proved") is False,
            False,
            "即使 row-level table 提交，仍需同一表内 row-mass/no-heavy-row 账本。",
            ROW_MASS,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步只把 signed-survival 的表达式缺口同步到 row-level origin table，不证明该表、row-mass、complete key、fixed-key multiplicity 或最终晋级门。",
            f"{ROW_TABLE} AND {SIGNED_SURVIVAL} AND {ROW_MASS}",
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """组装同步证书。"""
    signed_survival = load_json(SIGNED_SURVIVAL_CERT)
    primitive_expr = load_json(PRIMITIVE_EXPR_CERT)
    origin_id = load_json(ORIGIN_ID_CERT)
    phi_lpf = load_json(PHI_LPF_CERT)
    lpf_candidate = load_json(LPF_CANDIDATE_CERT)
    rows = build_rows(signed_survival, primitive_expr, origin_id, phi_lpf, lpf_candidate)
    latest_basis = (
        f"({ROW_TABLE} AND {SIGNED_SURVIVAL} AND {ROW_MASS}) "
        f"OR {POINTWISE_TABLE} OR {TERMINAL_DESCENT} OR {PDEC_SCOPE}; "
        f"parallel: {COMPLETE_KEY} AND {FIXED_KEY_MULT} AND {EXACTUV_PAIR} AND {DSTRUCTURE}"
    )
    return {
        "certificate_type": "prime_matrix_phi_lpf_signed_survival_origin_table_sync_router",
        "status": "phi_lpf_signed_survival_reduced_to_row_level_origin_table_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "phi_lpf_candidate_capacity_remains_closed": any(
            item["gate"] == "PhiLPFCandidateCapacityRemainsClosed" and item["closed"]
            for item in rows
        ),
        "primitive_expression_reduced_to_origin_identity": any(
            item["gate"] == "PrimitiveExpressionRouterImported" and item["closed"]
            for item in rows
        ),
        "origin_identity_reduced_to_row_level_generation": any(
            item["gate"] == "OriginIdentityRouterImported" and item["closed"]
            for item in rows
        ),
        "row_level_clean_core_origin_generation_table_proved": False,
        "nonzero_signed_row_survival_proved": False,
        "same_formal_unit_row_mass_normalization_proved": False,
        "row_column_unconditional_closed": False,
        "target_input_before_router": SIGNED_EXPR,
        "absorbed_to": ROW_TABLE,
        "next_primary_attack_target": ROW_TABLE,
        "parallel_attack_targets": [
            SIGNED_SURVIVAL,
            ROW_MASS,
            POINTWISE_TABLE,
            COMPLETE_KEY,
            FIXED_KEY_MULT,
            EXACTUV_PAIR,
            DSTRUCTURE,
        ],
        "sync_chain": sync_chain(),
        "gates": rows,
        "latest_retained_basis_after_router": latest_basis,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步把 Phi-LPF signed-survival 线的 `ActualNoncanonicalPrimitiveSummandSignedWeightExpressionBeforePushforward` "
            "同步到既有 strict 路由：signed expression 必须给出 pre-Cauchy signed coefficient 来源恒等式，"
            "而该来源恒等式又等价于逐行 clean-core 原始生成表。LPF/Phi 桶恒等式仍完整支付候选容量，"
            "但不能生成 signed coefficient origin。当前直接硬点压到 "
            "`RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands`；"
            "行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix Phi-LPF signed-survival origin-table sync 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"phi_lpf_candidate_capacity_remains_closed={fmt_bool(cert['phi_lpf_candidate_capacity_remains_closed'])}",
        f"primitive_expression_reduced_to_origin_identity={fmt_bool(cert['primitive_expression_reduced_to_origin_identity'])}",
        f"origin_identity_reduced_to_row_level_generation={fmt_bool(cert['origin_identity_reduced_to_row_level_generation'])}",
        f"row_level_clean_core_origin_generation_table_proved={fmt_bool(cert['row_level_clean_core_origin_generation_table_proved'])}",
        f"nonzero_signed_row_survival_proved={fmt_bool(cert['nonzero_signed_row_survival_proved'])}",
        f"same_formal_unit_row_mass_normalization_proved={fmt_bool(cert['same_formal_unit_row_mass_normalization_proved'])}",
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
            f"| `{cell(item['gate'])}` | `{fmt_bool(item['closed'])}` | `{fmt_bool(item['proved'])}` | "
            f"{cell(item['meaning'])} | {cell(item['remaining'])} |"
        )
    lines.extend(
        [
            "",
            "## 3. 最新保留基",
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
            "并行出口：",
            "",
            "```text",
            "\n".join(cert["parallel_attack_targets"]),
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
    """写出同步证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    cert = build_certificate()
    text = json.dumps(cert, ensure_ascii=False, indent=2, sort_keys=True)
    OUT_LEDGER.write_text(text + "\n", encoding="utf-8")
    OUT_JSON.write_text(text + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(cert), encoding="utf-8")
    print(OUT_LEDGER.relative_to(ROOT))
    print(OUT_JSON.relative_to(ROOT))
    print(OUT_MD.relative_to(ROOT))


if __name__ == "__main__":
    main()
