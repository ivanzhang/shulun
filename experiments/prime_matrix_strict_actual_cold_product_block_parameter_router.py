#!/usr/bin/env python3
"""生成 strict actual cold 产品块参数账本路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_actual_cold_product_block_parameter_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-actual-cold-product-block-parameter-router.json

输出：
  data/actual-cold-product-block-parameter-scan.json
  docs/monograph/prime-matrix-strict-actual-cold-product-block-parameter-router.json
  docs/monograph/prime-matrix-strict-actual-cold-product-block-parameter-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DATA = ROOT / "data"
OUT_JSON = DOCS / "prime-matrix-strict-actual-cold-product-block-parameter-router.json"
OUT_MD = DOCS / "prime-matrix-strict-actual-cold-product-block-parameter-router.md"
OUT_SCAN = DATA / "actual-cold-product-block-parameter-scan.json"

HARDPOINT = "ActualColdProductBlockParameterLedgerForP018Table"
H0_EMITTER = "ActualProductDivisorDomainH0EmitterForFormalUnit"
BLOCK_ENUMERATOR = "ActualDyadicColdProductBlockEnumeratorForH0"
KERNEL_REGISTER = "PerBlockRegisteredCommonKernelLedger"
P018_TABLE = "PrimitiveProductRankinP018InequalityTable"
FAILURE_RETURN = "PrimitiveProductRankinFailureReturnPacketLedger"
WEIGHT_COMPARISON = "PrimitiveProductRankinWeightP018Comparison"
CANDIDATE_BOUND = "ColdProductBlockCandidateCountOrSymbolicBound"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    DOCS / "prime-matrix-strict-primitive-product-rankin-p018-table-router.json",
    DOCS / "prime-matrix-concrete-source-tuple-anchor-parameter-router.json",
    DOCS / "prime-matrix-formal-unit-source-record-router.json",
    DOCS / "prime-matrix-canonical-formal-unit-hash-stability-router.json",
    DOCS / "prime-matrix-strict-cold-product-block-inventory-router.json",
    DOCS / "prime-matrix-strict-primitive-product-projection-rule-router.json",
    DOCS / "prime-matrix-strict-common-kernel-return-cycle-descent-router.json",
]


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失或损坏时返回空对象。"""
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}


def sha256(path: Path) -> str:
    """计算文件 SHA256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def source_hashes() -> dict[str, str]:
    """汇总依赖证据哈希。"""
    result = {
        "experiments/prime_matrix_strict_actual_cold_product_block_parameter_router.py": sha256(
            Path(__file__).resolve()
        ),
        "data/actual-cold-product-block-parameter-scan.json": sha256(OUT_SCAN),
    }
    for path in SOURCE_FILES:
        if path.exists():
            result[str(path.relative_to(ROOT))] = sha256(path)
    return result


def imported_flags() -> dict[str, bool]:
    """读取 actual 参数账本需要的导入。"""
    p018 = load_json(DOCS / "prime-matrix-strict-primitive-product-rankin-p018-table-router.json")
    source = load_json(DOCS / "prime-matrix-concrete-source-tuple-anchor-parameter-router.json")
    formal = load_json(DOCS / "prime-matrix-formal-unit-source-record-router.json")
    hash_doc = load_json(DOCS / "prime-matrix-canonical-formal-unit-hash-stability-router.json")
    inventory = load_json(DOCS / "prime-matrix-strict-cold-product-block-inventory-router.json")
    projection = load_json(DOCS / "prime-matrix-strict-primitive-product-projection-rule-router.json")
    kernel = load_json(DOCS / "prime-matrix-strict-common-kernel-return-cycle-descent-router.json")
    return {
        "p018_table_schema_imported": bool(p018.get("p018_table_schema_closed")),
        "source_tuple_data_imported": bool(source.get("concrete_source_tuple_anchor_parameter_data_closed")),
        "source_tuple_schema_imported": bool(source.get("source_tuple_anchor_parameter_schema_closed")),
        "formal_unit_source_record_imported": bool(formal.get("concrete_formal_unit_source_record_closed")),
        "hash_stability_imported": bool(hash_doc.get("canonical_formal_unit_hash_stability_closed")),
        "cold_block_schema_imported": bool(inventory.get("cold_product_dyadic_block_inventory_schema_closed")),
        "cold_candidate_generator_imported": bool(
            inventory.get("cold_product_candidate_set_generator_rule_closed")
        ),
        "primitive_projection_imported": bool(
            projection.get("primitive_product_projection_rule_executable_hash_closed")
        ),
        "common_kernel_return_discipline_imported": bool(
            kernel.get("common_kernel_return_cycle_descent_or_pdec_proved")
        ),
    }


def has_actual_parameter_rows(payload: dict[str, Any]) -> bool:
    """判断 JSON 是否含真正 actual cold 产品块参数行。"""
    row_keys = [
        "actual_cold_product_block_parameter_rows",
        "cold_product_block_parameter_rows",
        "primitive_product_p018_actual_rows",
        "actual_p018_block_rows",
    ]
    for key in row_keys:
        value = payload.get(key)
        if isinstance(value, list) and value:
            required = {"source_tuple_hash", "P", "h0", "Y", "registered_common_kernel"}
            return all(isinstance(row, dict) and required <= set(row) for row in value)
    return False


def scan_actual_parameter_ledgers() -> dict[str, Any]:
    """扫描仓库中是否已有全体 actual 参数账本。"""
    hits: list[dict[str, Any]] = []
    for root in [DOCS, DATA]:
        for path in sorted(root.rglob("*.json")):
            if path == OUT_JSON or path == OUT_SCAN:
                continue
            payload = load_json(path)
            if not payload:
                continue
            if has_actual_parameter_rows(payload):
                hits.append(
                    {
                        "path": str(path.relative_to(ROOT)),
                        "status": payload.get("status"),
                        "certificate_type": payload.get("certificate_type"),
                    }
                )
    return {
        "scan_type": "actual_cold_product_block_parameter_ledger_scan",
        "required_fields": ["source_tuple_hash", "P", "h0", "Y", "registered_common_kernel"],
        "hits": hits,
        "actual_parameter_ledger_found": bool(hits),
    }


def bridge_rows() -> list[dict[str, str]]:
    """列出从 source tuple 到 P^0.18 表的字段桥。"""
    return [
        {
            "field": "source_tuple_hash",
            "source_status": "imported_closed",
            "gap": "none",
            "meaning": "同一 formal unit/source tuple 的哈希稳定性已闭合。",
        },
        {
            "field": "P_or_P_range",
            "source_status": "schema_imported",
            "gap": "actual P row or uniform range policy",
            "meaning": "source tuple 记录 P 或 P-range，但 P^0.18 表需逐行 P 或全区间统一预算规则。",
        },
        {
            "field": "h0",
            "source_status": "absent_from_source_tuple_schema",
            "gap": H0_EMITTER,
            "meaning": "现有 source tuple 字段只含 A、D0/K/Omega、phase 等锚参数，不含产品除数域 h0。",
        },
        {
            "field": "Y",
            "source_status": "block_schema_only",
            "gap": BLOCK_ENUMERATOR,
            "meaning": "cold 产品块 schema 有 dyadic (Y,2Y]，但没有实际 Y 列表。",
        },
        {
            "field": "registered_common_kernel",
            "source_status": "return_discipline_imported",
            "gap": KERNEL_REGISTER,
            "meaning": "共同核回流纪律已闭合，但每个产品块的已登记 kernel 仍需参数行给出。",
        },
        {
            "field": "sigma/rankin_bound",
            "source_status": "formula_imported",
            "gap": "depends_on_h0_Y_kernel",
            "meaning": "Rankin 公式已闭合，但没有 h0/Y/kernel 无法计算表行。",
        },
    ]


def reduction_rows() -> list[dict[str, str]]:
    """给出该硬点的最小剩余分解。"""
    return [
        {
            "atom": H0_EMITTER,
            "role": "从同一 formal unit 的早期零行 witness/source tuple 生成产品除数域 h0。",
            "why_first": "没有 h0，Y 块、Euler product、projection profile 和 Rankin bound 全部无法生成。",
        },
        {
            "atom": BLOCK_ENUMERATOR,
            "role": "对给定 h0 与 cold/no-return guard 枚举实际 dyadic 产品块 Y。",
            "why_first": "依赖 h0；在 h0 发射器之后攻。",
        },
        {
            "atom": KERNEL_REGISTER,
            "role": "为每个实际产品块登记已吸收共同核，保证 primitive 分支不重复计数。",
            "why_first": "依赖 block 行；与失败回流包同步。",
        },
        {
            "atom": FAILURE_RETURN,
            "role": "为 Rankin/P^0.18 失败块登记热窗口、共同核、PDEC/SAE、固定历史或 ColumnCRT 回流。",
            "why_first": "样表已有失败行，不能省略。",
        },
    ]


def decision_row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def decision_rows(flags: dict[str, bool], scan: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    upstream_ready = (
        flags["p018_table_schema_imported"]
        and flags["source_tuple_data_imported"]
        and flags["formal_unit_source_record_imported"]
        and flags["hash_stability_imported"]
        and flags["cold_block_schema_imported"]
        and flags["primitive_projection_imported"]
    )
    return [
        decision_row(
            "ActualBlockParameterTargetImported",
            True,
            flags["p018_table_schema_imported"],
            "上一层已把 P^0.18 表缺口压成 actual cold 产品块参数账本。",
            HARDPOINT,
        ),
        decision_row(
            "SourceTupleContainerAndHashImported",
            True,
            flags["source_tuple_data_imported"] and flags["hash_stability_imported"],
            "source tuple、formal unit record 和 canonical hash 可作为参数账本的行键。",
            "source_tuple_hash ready",
        ),
        decision_row(
            "ColdBlockSchemaAndProjectionImported",
            True,
            flags["cold_block_schema_imported"] and flags["primitive_projection_imported"],
            "cold 产品块 schema 与 primitive projection hash 已可引用。",
            "block schema ready",
        ),
        decision_row(
            "ActualParameterLedgerFoundInCorpus",
            True,
            scan["actual_parameter_ledger_found"],
            "扫描仓库是否存在含 source_tuple_hash/P/h0/Y/kernel 的实际参数行账本。",
            HARDPOINT,
        ),
        decision_row(
            "ActualProductDivisorDomainH0EmitterPresent",
            False,
            False,
            "source tuple schema 不含 h0；当前没有同 formal unit 的产品除数域发射器。",
            H0_EMITTER,
        ),
        decision_row(
            "ActualDyadicColdProductBlockEnumeratorPresent",
            False,
            False,
            "没有 h0 发射器，也没有实际 dyadic Y 列表。",
            BLOCK_ENUMERATOR,
        ),
        decision_row(
            "PerBlockRegisteredCommonKernelLedgerPresent",
            False,
            False,
            "共同核纪律已闭合，但每个块的 registered kernel 参数未成行。",
            KERNEL_REGISTER,
        ),
        decision_row(
            "ActualColdProductBlockParameterLedgerPresent",
            False,
            False,
            "上游 schema/hash 已齐，但缺 h0、Y 和 per-block kernel 的实际行。",
            f"{H0_EMITTER} AND {BLOCK_ENUMERATOR} AND {KERNEL_REGISTER}",
        ),
        decision_row(
            "PrimitiveProductRankinP018InequalityTablePresent",
            False,
            False,
            "actual 参数账本不存在，P^0.18 表无法升级为全体实际块表。",
            P018_TABLE,
        ),
        decision_row(
            "PrimitiveProductRankinWeightP018ComparisonProved",
            False,
            False,
            "P^0.18 表未闭合，Rankin 权重比较仍未闭合。",
            WEIGHT_COMPARISON,
        ),
        decision_row(
            "ColdProductBlockCandidateCountOrSymbolicBoundProved",
            False,
            False,
            "Rankin 权重比较未闭合，候选计数符号界仍未闭合。",
            CANDIDATE_BOUND,
        ),
        decision_row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "仍未得到反例链与真实结构链的终端矛盾。",
            f"{H0_EMITTER} AND {FAILURE_RETURN} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 actual cold 产品块参数账本证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    scan = scan_actual_parameter_ledgers()
    OUT_SCAN.write_text(json.dumps(scan, indent=2, sort_keys=True), encoding="utf-8")
    flags = imported_flags()
    rows = decision_rows(flags, scan)
    return {
        "certificate_type": "prime_matrix_strict_actual_cold_product_block_parameter_router",
        "status": "actual_cold_product_block_parameter_reduced_to_h0_emitter_block_enumerator_kernel_register",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hardpoint_before_router": HARDPOINT,
        "hardpoint_after_router": f"{H0_EMITTER} AND {BLOCK_ENUMERATOR} AND {KERNEL_REGISTER}",
        "next_direct_attack_target": H0_EMITTER,
        "parallel_attack_targets": [BLOCK_ENUMERATOR, KERNEL_REGISTER, FAILURE_RETURN, DSTRUCTURE],
        "imported_flags": flags,
        "bridge_rows": bridge_rows(),
        "minimal_reduction_rows": reduction_rows(),
        "decision_table": rows,
        "actual_parameter_ledger_scan": scan,
        "source_tuple_container_and_hash_imported": bool(
            next(item for item in rows if item["gate"] == "SourceTupleContainerAndHashImported")["proved"]
        ),
        "cold_block_schema_and_projection_imported": bool(
            next(item for item in rows if item["gate"] == "ColdBlockSchemaAndProjectionImported")["proved"]
        ),
        "actual_cold_product_block_parameter_ledger_present": False,
        "actual_product_divisor_domain_h0_emitter_present": False,
        "actual_dyadic_cold_product_block_enumerator_present": False,
        "per_block_registered_common_kernel_ledger_present": False,
        "primitive_product_rankin_p018_inequality_table_present": False,
        "primitive_product_rankin_weight_p018_comparison_proved": False,
        "cold_product_block_candidate_count_or_symbolic_bound_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "plain_conclusion": (
            "`ActualColdProductBlockParameterLedgerForP018Table` 不能由已有 source tuple 自动推出。"
            "已有证书只给出 `source_tuple_hash`、P/P-range、锚参数和 cold 产品块 schema；"
            "P^0.18 表还需要实际 `h0` 产品除数域、dyadic `Y` 块列表和每块 registered common kernel。"
            "仓库扫描没有发现覆盖这些字段的实际参数账本。"
            "因此最新最窄点压成 `ActualProductDivisorDomainH0EmitterForFormalUnit`。"
        ),
        "source_hashes": source_hashes(),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix strict actual cold 产品块参数账本路由器",
        "",
        "## 结论",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"status={result['status']}",
        f"hardpoint_before={result['hardpoint_before_router']}",
        f"hardpoint_after={result['hardpoint_after_router']}",
        f"next_direct_attack_target={result['next_direct_attack_target']}",
        f"actual_cold_product_block_parameter_ledger_present={fmt_bool(result['actual_cold_product_block_parameter_ledger_present'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 字段桥",
        "",
        "| 字段 | 来源状态 | 缺口 | 含义 |",
        "|---|---|---|---|",
    ]
    for item in result["bridge_rows"]:
        lines.append(
            "| `{}` | `{}` | `{}` | {} |".format(
                table_cell(item["field"]),
                table_cell(item["source_status"]),
                table_cell(item["gap"]),
                table_cell(item["meaning"]),
            )
        )
    lines.extend(["", "## 最小分解", "", "| 原子 | 作用 | 攻坚顺序理由 |", "|---|---|---|"])
    for item in result["minimal_reduction_rows"]:
        lines.append(
            f"| `{table_cell(item['atom'])}` | {table_cell(item['role'])} | {table_cell(item['why_first'])} |"
        )
    lines.extend(
        [
            "",
            "## 判定表",
            "",
            "| Gate | Closed | Proved | Meaning | Remaining |",
            "|---|---:|---:|---|---|",
        ]
    )
    for item in result["decision_table"]:
        lines.append(
            "| `{}` | `{}` | `{}` | {} | `{}` |".format(
                table_cell(item["gate"]),
                fmt_bool(item["closed"]),
                fmt_bool(item["proved"]),
                table_cell(item["meaning"]),
                table_cell(item["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 扫描账本",
            "",
            f"- 路径：`{OUT_SCAN.relative_to(ROOT)}`",
            f"- actual 参数账本命中：`{fmt_bool(result['actual_parameter_ledger_scan']['actual_parameter_ledger_found'])}`",
            "",
            "## 依赖哈希",
            "",
            "| 文件 | SHA256 |",
            "|---|---|",
        ]
    )
    for path, digest in result["source_hashes"].items():
        lines.append(f"| `{table_cell(path)}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """生成 JSON、Markdown 与扫描账本。"""
    DOCS.mkdir(parents=True, exist_ok=True)
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, indent=2, sort_keys=True), encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"status={result['status']}")
    print(
        "actual_cold_product_block_parameter_ledger_present="
        f"{fmt_bool(result['actual_cold_product_block_parameter_ledger_present'])}"
    )
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
