#!/usr/bin/env python3
"""生成 strict concrete primitive product Rankin data ledger 路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_concrete_primitive_product_rankin_data_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-concrete-primitive-product-rankin-data-router.json

输出：
  docs/monograph/prime-matrix-strict-concrete-primitive-product-rankin-data-router.json
  docs/monograph/prime-matrix-strict-concrete-primitive-product-rankin-data-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-concrete-primitive-product-rankin-data-router.json"
OUT_MD = DOCS / "prime-matrix-strict-concrete-primitive-product-rankin-data-router.md"

HARDPOINT = "ConcretePrimitiveProductRankinEmbeddingDataLedger"
SOURCE_CONTAINER = "FormalUnitSourceTupleContainerForPrimitiveProductRankin"
PRODUCT_BLOCK_INVENTORY = "ColdProductDyadicBlockInventoryLedger"
PROJECTION_RULE = "PrimitiveProductProjectionRuleExecutableHash"
CONCRETE_DATA = "ConcretePrimitiveProductRankinEmbeddingDataLedger"
WEIGHT_COMPARISON = "PrimitiveProductRankinWeightP018Comparison"
FAILURE_RETURN = "PrimitiveProductRankinFailureReturnPacketLedger"
SUPPORT_RANKIN = "PrimitiveProductSupportRankinLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    DOCS / "prime-matrix-strict-primitive-product-rankin-manifest-router.json",
    DOCS / "prime-matrix-concrete-source-tuple-anchor-parameter-router.json",
    DOCS / "prime-matrix-formal-unit-source-record-router.json",
    DOCS / "prime-matrix-canonical-formal-unit-hash-stability-router.json",
    DOCS / "prime-matrix-strict-cold-product-support-sparsification-router.json",
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
        "experiments/prime_matrix_strict_concrete_primitive_product_rankin_data_router.py": sha256(
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
    """读取 concrete data 需要的导入。"""
    manifest = load_json(DOCS / "prime-matrix-strict-primitive-product-rankin-manifest-router.json")
    tuple_doc = load_json(DOCS / "prime-matrix-concrete-source-tuple-anchor-parameter-router.json")
    formal = load_json(DOCS / "prime-matrix-formal-unit-source-record-router.json")
    hash_doc = load_json(DOCS / "prime-matrix-canonical-formal-unit-hash-stability-router.json")
    return {
        "manifest_schema_imported": bool(
            manifest.get("primitive_product_rankin_embedding_manifest_schema_closed")
        ),
        "source_tuple_data_closed": bool(tuple_doc.get("concrete_source_tuple_anchor_parameter_data_closed")),
        "formal_unit_source_record_closed": bool(formal.get("concrete_formal_unit_source_record_closed")),
        "canonical_formal_unit_hash_stability_closed": bool(
            hash_doc.get("canonical_formal_unit_hash_stability_closed")
        ),
    }


def data_component_rows() -> list[dict[str, str]]:
    """列出 concrete data ledger 的组成部分。"""
    return [
        {
            "component": "source_container",
            "status": "closed",
            "meaning": "formal_unit_id/source_tuple_hash/source records 已由既有证书闭合。",
            "remaining": "none",
        },
        {
            "component": "cold_product_block_inventory",
            "status": "open",
            "meaning": "尚未列出每个 source tuple 下的 cold dyadic 产品块与候选 d 集合。",
            "remaining": PRODUCT_BLOCK_INVENTORY,
        },
        {
            "component": "primitive_projection_rule",
            "status": "open",
            "meaning": "尚未给出从产品 d 到 primitive rank profile 的可执行规则与 hash。",
            "remaining": PROJECTION_RULE,
        },
        {
            "component": "rankin_row_emitter",
            "status": "blocked_on_projection",
            "meaning": "没有产品块清单和投影规则，就不能发射 Rankin 行。",
            "remaining": f"{PRODUCT_BLOCK_INVENTORY} AND {PROJECTION_RULE}",
        },
    ]


def product_inventory_schema_rows() -> list[dict[str, str]]:
    """给出产品块清单最小字段。"""
    return [
        {"field": "source_tuple_hash", "role": "继承 formal unit 与参数账本。"},
        {"field": "block_id", "role": "稳定编号 dyadic 产品块。"},
        {"field": "Y_left_Y_right", "role": "记录产品范围 Y<d<=2Y。"},
        {"field": "cold_key_hash", "role": "锁定 cold/no-return/非持久过滤条件。"},
        {"field": "candidate_product_rule", "role": "定义哪些 d|h0 进入该块。"},
        {"field": "candidate_count_or_symbolic_bound", "role": "给出可复算计数或符号上界。"},
        {"field": "return_filter_hash", "role": "记录被热窗口/共同核/命名回流剔除的部分。"},
    ]


def decision_rows(flags: dict[str, bool]) -> list[dict[str, Any]]:
    """生成判定表。"""
    source_container_closed = (
        flags["manifest_schema_imported"]
        and flags["source_tuple_data_closed"]
        and flags["formal_unit_source_record_closed"]
        and flags["canonical_formal_unit_hash_stability_closed"]
    )
    return [
        row(
            "ConcreteDataTargetImported",
            True,
            flags["manifest_schema_imported"],
            "上一层已把目标 Rankin manifest schema 闭合，下一步需要 concrete embedding data。",
            HARDPOINT,
        ),
        row(
            "FormalUnitSourceTupleContainerClosed",
            source_container_closed,
            source_container_closed,
            "formal_unit_id、source_tuple_hash 与 source records 可稳定继承到产品 Rankin 数据。",
            SOURCE_CONTAINER,
        ),
        row(
            "ColdProductDyadicBlockInventoryPresent",
            False,
            False,
            "尚未生成当前 source tuple 下的 cold 产品 dyadic 块清单。",
            PRODUCT_BLOCK_INVENTORY,
        ),
        row(
            "PrimitiveProductProjectionRuleExecutableHashClosed",
            False,
            False,
            "尚未定义并哈希化 d -> primitive rank profile 的可执行投影规则。",
            PROJECTION_RULE,
        ),
        row(
            "ConcretePrimitiveProductRankinEmbeddingDataLedgerProved",
            False,
            False,
            "来源容器已闭合，但产品块 inventory 和 primitive 投影规则未闭合。",
            f"{PRODUCT_BLOCK_INVENTORY} AND {PROJECTION_RULE}",
        ),
        row(
            "PrimitiveProductRankinWeightP018ComparisonProved",
            False,
            False,
            "没有 concrete data 就不能计算或证明权重表。",
            WEIGHT_COMPARISON,
        ),
        row(
            "PrimitiveProductSupportRankinLedgerProved",
            False,
            False,
            "concrete embedding data 未完成，Rankin 支撑门仍未闭合。",
            SUPPORT_RANKIN,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "仍未得到早期零行反例链终端矛盾。",
            f"{PRODUCT_BLOCK_INVENTORY} AND {PROJECTION_RULE} AND {WEIGHT_COMPARISON} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 concrete data ledger 证书。"""
    flags = imported_flags()
    decisions = decision_rows(flags)
    return {
        "certificate_type": "prime_matrix_strict_concrete_primitive_product_rankin_data_router",
        "status": "source_tuple_container_closed_product_block_inventory_projection_rule_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hardpoint_before_router": HARDPOINT,
        "hardpoint_after_router": f"{PRODUCT_BLOCK_INVENTORY} AND {PROJECTION_RULE}",
        "next_direct_attack_target": PRODUCT_BLOCK_INVENTORY,
        "imported_flags": flags,
        "data_components": data_component_rows(),
        "product_inventory_schema": product_inventory_schema_rows(),
        "decision_table": decisions,
        "formal_unit_source_tuple_container_closed": bool(
            next(item for item in decisions if item["gate"] == "FormalUnitSourceTupleContainerClosed")["proved"]
        ),
        "cold_product_dyadic_block_inventory_present": False,
        "primitive_product_projection_rule_executable_hash_closed": False,
        "concrete_primitive_product_rankin_embedding_data_ledger_proved": False,
        "primitive_product_rankin_weight_p018_comparison_proved": False,
        "primitive_product_support_rankin_ledger_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "plain_conclusion": (
            "`ConcretePrimitiveProductRankinEmbeddingDataLedger` 已关闭来源容器部分："
            "formal unit、source tuple 和 canonical hash 都可稳定继承。"
            "但当前还没有 cold 产品 dyadic 块清单，也没有可执行的 primitive 投影规则；"
            "因此无法发射目标 Rankin 行或比较 `P^0.18` 权重。"
            "最新最窄点是 `ColdProductDyadicBlockInventoryLedger`。"
        ),
        "source_hashes": source_hashes(),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = []
    lines.append("# Prime Matrix strict concrete primitive product Rankin data 路由器")
    lines.append("")
    lines.append(f"**状态：** `{result['status']}`")
    lines.append("")
    lines.append(result["plain_conclusion"])
    lines.append("")
    lines.append("```text")
    for key in [
        "formal_unit_source_tuple_container_closed",
        "cold_product_dyadic_block_inventory_present",
        "primitive_product_projection_rule_executable_hash_closed",
        "concrete_primitive_product_rankin_embedding_data_ledger_proved",
        "primitive_product_support_rankin_ledger_proved",
        "row_column_unconditional_closed",
    ]:
        lines.append(f"{key}={fmt_bool(result[key])}")
    lines.append("```")
    lines.append("")

    lines.append("## 1. 数据组成")
    lines.append("")
    lines.append("| component | status | meaning | remaining |")
    lines.append("| --- | --- | --- | --- |")
    for item in result["data_components"]:
        lines.append(
            "| "
            + " | ".join(table_cell(item[key]) for key in ["component", "status", "meaning", "remaining"])
            + " |"
        )
    lines.append("")

    lines.append("## 2. 产品块清单字段")
    lines.append("")
    lines.append("| field | role |")
    lines.append("| --- | --- |")
    for item in result["product_inventory_schema"]:
        lines.append(f"| {table_cell(item['field'])} | {table_cell(item['role'])} |")
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
    lines.append(f"- 同步：`{PROJECTION_RULE}` 与 `{WEIGHT_COMPARISON}`。")
    lines.append("- 边界：本步只关闭 source tuple 容器，不生成产品块数据。")
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
    print(f"formal_unit_source_tuple_container_closed={fmt_bool(result['formal_unit_source_tuple_container_closed'])}")
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
