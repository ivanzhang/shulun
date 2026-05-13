#!/usr/bin/env python3
"""生成 strict 原始分散产品支撑 Rankin 账本路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_primitive_product_support_rankin_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-primitive-product-support-rankin-router.json

输出：
  docs/monograph/prime-matrix-strict-primitive-product-support-rankin-router.json
  docs/monograph/prime-matrix-strict-primitive-product-support-rankin-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-primitive-product-support-rankin-router.json"
OUT_MD = DOCS / "prime-matrix-strict-primitive-product-support-rankin-router.md"

HARDPOINT = "PrimitiveProductSupportRankinLedger"
TARGET_MANIFEST = "PrimitiveProductRankinEmbeddingManifestAndWeightTable"
WEIGHT_COMPARISON = "PrimitiveProductRankinWeightP018Comparison"
RETURN_PACKET = "PrimitiveProductRankinFailureReturnPacketLedger"
HOT_DENSITY = "ShortWindowHotDivisorDensityPDECorSAEReturnExclusion"
COMMON_KERNEL = "CommonKernelReturnCycleDescentOrPDECLedger"
SPARSIFICATION = "ColdProductSupportSparsificationBeyondTauLedger"
SUPPORT_ENV = "ColdFilteredDivisorSupportP018Envelope"
FULL_RANKIN = "FullRankinLedgerStillOpen"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
UNIFIED_BUDGET = "UnifiedTerminalBudgetStrictInequality"

SOURCE_FILES = [
    DOCS / "prime-matrix-strict-cold-product-support-sparsification-router.json",
    DOCS / "prime-matrix-full-rankin-ledger-inventory-router.json",
    DOCS / "prime-matrix-batch-rankin-pass-return-router.json",
    DOCS / "prime-matrix-concrete-rankin-manifest-data-router.json",
    DOCS / "prime-matrix-per-color-rankin-certificate-file-router.json",
    DOCS / "prime-matrix-dstructure-rankin-promotion-acceptance-router.json",
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
        "experiments/prime_matrix_strict_primitive_product_support_rankin_router.py": sha256(
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
    """读取 Rankin 相关导入。"""
    sparse = load_json(DOCS / "prime-matrix-strict-cold-product-support-sparsification-router.json")
    full = load_json(DOCS / "prime-matrix-full-rankin-ledger-inventory-router.json")
    batch = load_json(DOCS / "prime-matrix-batch-rankin-pass-return-router.json")
    concrete = load_json(DOCS / "prime-matrix-concrete-rankin-manifest-data-router.json")
    per_color = load_json(DOCS / "prime-matrix-per-color-rankin-certificate-file-router.json")
    promotion = load_json(DOCS / "prime-matrix-dstructure-rankin-promotion-acceptance-router.json")
    return {
        "primitive_rankin_target_imported": bool(
            not sparse.get("primitive_product_support_rankin_ledger_proved", True)
            and sparse.get("overload_block_structural_split_closed")
        ),
        "full_rankin_subledger_closed": bool(full.get("full_rankin_ledger_still_open_closed")),
        "batch_rankin_pass_or_return_closed": bool(batch.get("batch_rankin_pass_or_return_closed")),
        "concrete_rankin_manifest_data_closed": bool(concrete.get("concrete_rankin_batch_manifest_data_closed")),
        "per_color_rankin_certificate_schema_closed": bool(
            per_color.get("per_color_rankin_certificate_file_ledger_closed")
        ),
        "promotion_package_boundary_closed": bool(promotion.get("promotion_package_boundary_closed")),
        "promotion_package_independently_accepted": bool(
            promotion.get("promotion_package_independently_accepted")
        ),
    }


def rankin_reuse_rows() -> list[dict[str, str]]:
    """列出现有 Rankin 账本可复用与不可复用部分。"""
    return [
        {
            "component": "verifier_schema",
            "reuse": "yes",
            "status": "closed",
            "meaning": "单证书、批量 manifest、pass-or-return 字段可复用。",
        },
        {
            "component": "existing_colored_corridor_manifest",
            "reuse": "no_direct_import",
            "status": "scope_mismatch",
            "meaning": "旧 manifest 覆盖 formal colored corridors，不自动覆盖当前 cold 产品 dyadic 块。",
        },
        {
            "component": "failure_return_discipline",
            "reuse": "yes",
            "status": "closed_schema_open_exclusion",
            "meaning": "失败行必须回流 PDEC/SAE/常数缺口；但回流排斥仍在下游。",
        },
        {
            "component": "independent_promotion_acceptance",
            "reuse": "no_author_side_upgrade",
            "status": "referee_open",
            "meaning": "DStructure/Tail-log4/finite Rankin 晋级仍需独立验收。",
        },
    ]


def target_manifest_rows() -> list[dict[str, str]]:
    """定义当前目标专用 manifest 必须包含的字段。"""
    return [
        {
            "field": "formal_unit_id",
            "role": "锁定同一 h_0、同一反例链 source tuple。",
            "required": "yes",
        },
        {
            "field": "dyadic_product_block",
            "role": "记录 Y<d<=2Y 的过载块。",
            "required": "yes",
        },
        {
            "field": "cold_key",
            "role": "绑定 cold/nonpersistent/no-return 过滤条件和规范窗口键。",
            "required": "yes",
        },
        {
            "field": "primitive_rank_profile",
            "role": "逐素数记录 primitive factor/rank 贡献，避免全局 tau 因子偷渡。",
            "required": "yes",
        },
        {
            "field": "rankin_weight",
            "role": "给出每行 Rankin 权重和总和。",
            "required": "yes",
        },
        {
            "field": "allowed_P018_budget",
            "role": "同参数比较目标，必须小于 P^0.18 的剩余支撑预算。",
            "required": "yes",
        },
        {
            "field": "verdict_or_return",
            "role": "每行要么 pass，要么回流热窗口、共同核、PDEC/SAE 或常数缺口。",
            "required": "yes",
        },
    ]


def decision_rows(flags: dict[str, bool]) -> list[dict[str, Any]]:
    """生成判定表。"""
    rankin_schema_reusable = (
        flags["full_rankin_subledger_closed"]
        and flags["batch_rankin_pass_or_return_closed"]
        and flags["per_color_rankin_certificate_schema_closed"]
    )
    return [
        row(
            "PrimitiveRankinTargetImported",
            True,
            flags["primitive_rankin_target_imported"],
            "上一层已把分散 cold 产品支撑压成原始 Rankin/Euler 账本。",
            HARDPOINT,
        ),
        row(
            "ExistingRankinVerifierSchemaReusable",
            rankin_schema_reusable,
            rankin_schema_reusable,
            "现有 Rankin 子账本提供可复用的单证书、批量 manifest 和 pass-or-return schema。",
            "schema closed",
        ),
        row(
            "ExistingColoredCorridorManifestCoversCurrentProducts",
            False,
            False,
            "旧 concrete manifest 覆盖 formal colored corridors；当前 cold 产品 dyadic 块尚无嵌入映射，不能直接导入为已 pass。",
            TARGET_MANIFEST,
        ),
        row(
            "TargetPrimitiveProductManifestPresent",
            False,
            False,
            "尚未列出当前 formal unit / dyadic block / cold key / primitive rank profile 的目标专用 manifest。",
            TARGET_MANIFEST,
        ),
        row(
            "PrimitiveProductRankinWeightP018ComparisonProved",
            False,
            False,
            "尚未证明目标 manifest 的 Rankin 权重总和低于 P^0.18 支撑预算。",
            WEIGHT_COMPARISON,
        ),
        row(
            "PrimitiveProductRankinFailureReturnClosed",
            False,
            False,
            "若目标 Rankin 行失败，尚未给出目标专用回流包。",
            RETURN_PACKET,
        ),
        row(
            "PrimitiveProductSupportRankinLedgerProved",
            False,
            False,
            "Rankin 验收格式可复用，但当前产品支撑缺目标专用 manifest、权重比较和失败回流。",
            f"{TARGET_MANIFEST} AND {WEIGHT_COMPARISON} AND {RETURN_PACKET}",
        ),
        row(
            "ColdProductSupportSparsificationBeyondTauLedgerProved",
            False,
            False,
            "原始分散支撑 Rankin 未闭合，故 cold 稀疏化仍未闭合。",
            f"{HARDPOINT} AND {HOT_DENSITY} AND {COMMON_KERNEL}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "仍未得到早期零行反例链终端矛盾。",
            f"{TARGET_MANIFEST} AND {UNIFIED_BUDGET} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造原始产品支撑 Rankin 证书。"""
    flags = imported_flags()
    decisions = decision_rows(flags)
    return {
        "certificate_type": "prime_matrix_strict_primitive_product_support_rankin_router",
        "status": "primitive_product_rankin_schema_reusable_target_manifest_weight_table_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hardpoint_before_router": HARDPOINT,
        "hardpoint_after_router": f"{TARGET_MANIFEST} AND {WEIGHT_COMPARISON} AND {RETURN_PACKET}",
        "next_direct_attack_target": TARGET_MANIFEST,
        "imported_flags": flags,
        "rankin_reuse_table": rankin_reuse_rows(),
        "target_manifest_schema": target_manifest_rows(),
        "decision_table": decisions,
        "existing_rankin_verifier_schema_reusable": bool(
            next(item for item in decisions if item["gate"] == "ExistingRankinVerifierSchemaReusable")["proved"]
        ),
        "existing_colored_corridor_manifest_covers_current_products": False,
        "target_primitive_product_manifest_present": False,
        "primitive_product_rankin_weight_p018_comparison_proved": False,
        "primitive_product_rankin_failure_return_closed": False,
        "primitive_product_support_rankin_ledger_proved": False,
        "cold_product_support_sparsification_beyond_tau_ledger_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "plain_conclusion": (
            "`PrimitiveProductSupportRankinLedger` 不能由旧 full Rankin 子账本直接关闭。"
            "可复用的是 Rankin 验收 schema 与 pass-or-return 纪律；不可复用的是旧 formal colored corridor manifest，"
            "因为当前对象是 cold 产品 dyadic 块。故最新剩余被压成目标专用三件套："
            "当前产品支撑到 Rankin 行的 embedding manifest、Rankin 权重对 `P^0.18` 的比较表、"
            "以及失败行回流包。"
        ),
        "source_hashes": source_hashes(),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = []
    lines.append("# Prime Matrix strict 原始产品支撑 Rankin 路由器")
    lines.append("")
    lines.append(f"**状态：** `{result['status']}`")
    lines.append("")
    lines.append(result["plain_conclusion"])
    lines.append("")
    lines.append("```text")
    for key in [
        "existing_rankin_verifier_schema_reusable",
        "existing_colored_corridor_manifest_covers_current_products",
        "target_primitive_product_manifest_present",
        "primitive_product_rankin_weight_p018_comparison_proved",
        "primitive_product_support_rankin_ledger_proved",
        "row_column_unconditional_closed",
    ]:
        lines.append(f"{key}={fmt_bool(result[key])}")
    lines.append("```")
    lines.append("")

    lines.append("## 1. Rankin 复用边界")
    lines.append("")
    lines.append("| component | reuse | status | meaning |")
    lines.append("| --- | --- | --- | --- |")
    for item in result["rankin_reuse_table"]:
        lines.append(
            "| "
            + " | ".join(table_cell(item[key]) for key in ["component", "reuse", "status", "meaning"])
            + " |"
        )
    lines.append("")

    lines.append("## 2. 目标 manifest schema")
    lines.append("")
    lines.append("| field | role | required |")
    lines.append("| --- | --- | --- |")
    for item in result["target_manifest_schema"]:
        lines.append(
            "| "
            + " | ".join(table_cell(item[key]) for key in ["field", "role", "required"])
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
    lines.append(f"- 同步：`{WEIGHT_COMPARISON}` 与 `{RETURN_PACKET}`。")
    lines.append(f"- 边界：本步不把旧 Rankin manifest 直接套到当前产品支撑。")
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
    print(f"existing_rankin_verifier_schema_reusable={fmt_bool(result['existing_rankin_verifier_schema_reusable'])}")
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
