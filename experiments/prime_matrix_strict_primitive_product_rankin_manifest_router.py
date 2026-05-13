#!/usr/bin/env python3
"""生成 strict 原始产品 Rankin embedding manifest/权重表路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_primitive_product_rankin_manifest_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-primitive-product-rankin-manifest-router.json

输出：
  docs/monograph/prime-matrix-strict-primitive-product-rankin-manifest-router.json
  docs/monograph/prime-matrix-strict-primitive-product-rankin-manifest-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-primitive-product-rankin-manifest-router.json"
OUT_MD = DOCS / "prime-matrix-strict-primitive-product-rankin-manifest-router.md"

HARDPOINT = "PrimitiveProductRankinEmbeddingManifestAndWeightTable"
SCHEMA = "PrimitiveProductRankinEmbeddingManifestSchema"
CONCRETE_DATA = "ConcretePrimitiveProductRankinEmbeddingDataLedger"
WEIGHT_COMPARISON = "PrimitiveProductRankinWeightP018Comparison"
FAILURE_RETURN = "PrimitiveProductRankinFailureReturnPacketLedger"
SUPPORT_RANKIN = "PrimitiveProductSupportRankinLedger"
SPARSIFICATION = "ColdProductSupportSparsificationBeyondTauLedger"
SUPPORT_ENV = "ColdFilteredDivisorSupportP018Envelope"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    DOCS / "prime-matrix-strict-primitive-product-support-rankin-router.json",
    DOCS / "prime-matrix-strict-cold-product-support-sparsification-router.json",
    DOCS / "prime-matrix-batch-rankin-pass-return-router.json",
    DOCS / "prime-matrix-full-rankin-ledger-inventory-router.json",
]


def load_json(path: Path) -> dict[str, Any]:
    """读取依赖 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件 SHA256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖证据哈希。"""
    result = {
        "experiments/prime_matrix_strict_primitive_product_rankin_manifest_router.py": sha256(
            Path(__file__).resolve()
        )
    }
    for path in SOURCE_FILES:
        if path.exists():
            result[str(path.relative_to(ROOT))] = sha256(path)
    return result


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
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


def imported_flags() -> dict[str, bool]:
    """读取 manifest 路由所需的导入。"""
    primitive = load_json(DOCS / "prime-matrix-strict-primitive-product-support-rankin-router.json")
    batch = load_json(DOCS / "prime-matrix-batch-rankin-pass-return-router.json")
    return {
        "primitive_rankin_schema_reusable": bool(primitive.get("existing_rankin_verifier_schema_reusable")),
        "old_manifest_scope_mismatch_recorded": not bool(
            primitive.get("existing_colored_corridor_manifest_covers_current_products")
        ),
        "batch_rankin_pass_or_return_closed": bool(batch.get("batch_rankin_pass_or_return_closed")),
    }


def embedding_schema_rows() -> list[dict[str, str]]:
    """定义产品支撑到 Rankin 行的目标嵌入字段。"""
    return [
        {
            "name": "source_tuple",
            "definition": "(formal_unit_id, h0, parameter_id, counterexample_branch_id)",
            "purpose": "固定同一反例链和同参数账本。",
        },
        {
            "name": "support_block",
            "definition": "(Y,2Y] with d|h0 and d cold-admissible",
            "purpose": "锁定一个 dyadic 产品块，禁止跨块拼接预算。",
        },
        {
            "name": "primitive_projection",
            "definition": "d -> squarefree/local primitive profile after removing registered common kernels",
            "purpose": "把分散支撑写成逐素数 rank 贡献，而不是全局 tau(d)。",
        },
        {
            "name": "local_rank_weight",
            "definition": "rho_l(d), w_l(rho_l), and product/Euler aggregate",
            "purpose": "提供 Rankin 权重的可复算局部因子。",
        },
        {
            "name": "cold_no_return_guard",
            "definition": "not hot-density, not common-kernel return, not named PDEC/SAE/ColumnCRT",
            "purpose": "确保 manifest 只覆盖 primitive dispersion branch。",
        },
        {
            "name": "budget_row",
            "definition": "rankin_sum(block) <= allowed_P018(block)",
            "purpose": "直接对接 P^0.18 支撑预算。",
        },
        {
            "name": "return_row",
            "definition": "failed rows point to hot-density/common-kernel/PDEC/SAE/constant-gap packet",
            "purpose": "保证失败行不形成第四出口。",
        },
    ]


def missing_data_rows() -> list[dict[str, str]]:
    """列出仍缺的具体数据。"""
    return [
        {
            "missing": "concrete_source_tuple_inventory",
            "why_needed": "需要列出当前 cold 产品块来自哪些 formal unit 与参数行。",
            "next": CONCRETE_DATA,
        },
        {
            "missing": "primitive_projection_rule_hash",
            "why_needed": "必须可复算地移除共同核并生成 primitive rank profile。",
            "next": CONCRETE_DATA,
        },
        {
            "missing": "rankin_weight_formula",
            "why_needed": "需要明确局部 rank 权和 Euler/Rankin 聚合常数。",
            "next": WEIGHT_COMPARISON,
        },
        {
            "missing": "P018_allowed_budget_table",
            "why_needed": "每个 dyadic 块必须有同参数允许预算，而不是总量口头估计。",
            "next": WEIGHT_COMPARISON,
        },
        {
            "missing": "failure_return_packet_map",
            "why_needed": "未通过 Rankin 的行必须指向热窗口、共同核或 PDEC/SAE 回流包。",
            "next": FAILURE_RETURN,
        },
    ]


def decision_rows(flags: dict[str, bool]) -> list[dict[str, Any]]:
    """生成判定表。"""
    schema_closed = (
        flags["primitive_rankin_schema_reusable"]
        and flags["old_manifest_scope_mismatch_recorded"]
        and flags["batch_rankin_pass_or_return_closed"]
    )
    return [
        row(
            "PrimitiveProductManifestTargetImported",
            True,
            flags["primitive_rankin_schema_reusable"],
            "上一层已确认 Rankin 验收 schema 可复用，但目标产品 manifest 缺失。",
            HARDPOINT,
        ),
        row(
            "OldManifestScopeMismatchGuardClosed",
            True,
            flags["old_manifest_scope_mismatch_recorded"],
            "明确禁止把旧 colored corridor manifest 直接套入当前 cold 产品块。",
            "guard closed",
        ),
        row(
            "PrimitiveProductRankinEmbeddingManifestSchemaClosed",
            schema_closed,
            schema_closed,
            "目标 manifest 字段、预算行和失败回流行已经定义为可审查 schema。",
            SCHEMA,
        ),
        row(
            "ConcretePrimitiveProductRankinEmbeddingDataLedgerProved",
            False,
            False,
            "尚未生成当前 formal unit / dyadic block / primitive rank profile 的具体数据清单。",
            CONCRETE_DATA,
        ),
        row(
            "PrimitiveProductRankinWeightP018ComparisonProved",
            False,
            False,
            "尚未给出 Rankin 权重总和与 P^0.18 预算的逐块比较。",
            WEIGHT_COMPARISON,
        ),
        row(
            "PrimitiveProductRankinFailureReturnPacketLedgerClosed",
            False,
            False,
            "尚未为目标产品 Rankin 失败行生成回流包。",
            FAILURE_RETURN,
        ),
        row(
            "PrimitiveProductRankinEmbeddingManifestAndWeightTableProved",
            False,
            False,
            "schema 已闭合，具体数据、权重比较和失败回流仍未完成。",
            f"{CONCRETE_DATA} AND {WEIGHT_COMPARISON} AND {FAILURE_RETURN}",
        ),
        row(
            "PrimitiveProductSupportRankinLedgerProved",
            False,
            False,
            "目标 manifest/权重表未完成，故原始产品 Rankin 门仍未闭合。",
            SUPPORT_RANKIN,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "仍未形成排除早期零行反例链的终端矛盾。",
            f"{CONCRETE_DATA} AND {WEIGHT_COMPARISON} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造目标 manifest/权重表证书。"""
    flags = imported_flags()
    decisions = decision_rows(flags)
    return {
        "certificate_type": "prime_matrix_strict_primitive_product_rankin_manifest_router",
        "status": "primitive_product_rankin_manifest_schema_closed_concrete_data_weight_table_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hardpoint_before_router": HARDPOINT,
        "hardpoint_after_router": f"{CONCRETE_DATA} AND {WEIGHT_COMPARISON} AND {FAILURE_RETURN}",
        "next_direct_attack_target": CONCRETE_DATA,
        "imported_flags": flags,
        "embedding_schema": embedding_schema_rows(),
        "missing_data": missing_data_rows(),
        "decision_table": decisions,
        "primitive_product_rankin_embedding_manifest_schema_closed": bool(
            next(item for item in decisions if item["gate"] == "PrimitiveProductRankinEmbeddingManifestSchemaClosed")[
                "proved"
            ]
        ),
        "concrete_primitive_product_rankin_embedding_data_ledger_proved": False,
        "primitive_product_rankin_weight_p018_comparison_proved": False,
        "primitive_product_rankin_failure_return_packet_ledger_closed": False,
        "primitive_product_rankin_embedding_manifest_and_weight_table_proved": False,
        "primitive_product_support_rankin_ledger_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "plain_conclusion": (
            "`PrimitiveProductRankinEmbeddingManifestAndWeightTable` 的 schema 层已闭合："
            "manifest 必须锁定 source tuple、dyadic 产品块、cold/no-return 守卫、primitive rank profile、"
            "Rankin 权重、`P^0.18` 预算行和失败回流行。"
            "但当前还没有具体 source/block 数据、权重比较表和失败回流映射；"
            "因此 Rankin 门仍未闭合，最新最窄点是生成目标专用 concrete embedding data ledger。"
        ),
        "source_hashes": source_hashes(),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = []
    lines.append("# Prime Matrix strict 原始产品 Rankin manifest/权重表路由器")
    lines.append("")
    lines.append(f"**状态：** `{result['status']}`")
    lines.append("")
    lines.append(result["plain_conclusion"])
    lines.append("")
    lines.append("```text")
    for key in [
        "primitive_product_rankin_embedding_manifest_schema_closed",
        "concrete_primitive_product_rankin_embedding_data_ledger_proved",
        "primitive_product_rankin_weight_p018_comparison_proved",
        "primitive_product_rankin_embedding_manifest_and_weight_table_proved",
        "primitive_product_support_rankin_ledger_proved",
        "row_column_unconditional_closed",
    ]:
        lines.append(f"{key}={fmt_bool(result[key])}")
    lines.append("```")
    lines.append("")

    lines.append("## 1. Embedding Schema")
    lines.append("")
    lines.append("| name | definition | purpose |")
    lines.append("| --- | --- | --- |")
    for item in result["embedding_schema"]:
        lines.append(
            "| "
            + " | ".join(table_cell(item[key]) for key in ["name", "definition", "purpose"])
            + " |"
        )
    lines.append("")

    lines.append("## 2. 仍缺数据")
    lines.append("")
    lines.append("| missing | why needed | next |")
    lines.append("| --- | --- | --- |")
    for item in result["missing_data"]:
        lines.append(
            "| "
            + " | ".join(table_cell(item[key]) for key in ["missing", "why_needed", "next"])
            + " |"
        )
    lines.append("")

    lines.append("## 3. 判定表")
    lines.append("")
    lines.append("| gate | closed | proved | meaning | remaining |")
    lines.append("| --- | --- | --- | --- | --- |")
    for item in result["decision_table"]:
        lines.append(
            f"| `{table_cell(item['gate'])}` | `{fmt_bool(item['closed'])}` | "
            f"`{fmt_bool(item['proved'])}` | {table_cell(item['meaning'])} | {table_cell(item['remaining'])} |"
        )
    lines.append("")

    lines.append("## 4. 下一步最窄点")
    lines.append("")
    lines.append(f"- 主攻：`{result['next_direct_attack_target']}`。")
    lines.append(f"- 同步：`{WEIGHT_COMPARISON}` 与 `{FAILURE_RETURN}`。")
    lines.append("- 边界：本步只闭合 schema，不提供具体 Rankin pass 证明。")
    lines.append("")

    lines.append("## 5. 依赖哈希")
    lines.append("")
    lines.append("| file | sha256 |")
    lines.append("| --- | --- |")
    for file, digest in sorted(result["source_hashes"].items()):
        lines.append(f"| `{table_cell(file)}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """生成 JSON 与 Markdown 文件。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"status={result['status']}")
    print(
        "primitive_product_rankin_embedding_manifest_schema_closed="
        f"{fmt_bool(result['primitive_product_rankin_embedding_manifest_schema_closed'])}"
    )
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
