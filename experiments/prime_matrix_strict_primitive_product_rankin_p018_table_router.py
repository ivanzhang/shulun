#!/usr/bin/env python3
"""生成 strict primitive product Rankin P^0.18 不等式表路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_primitive_product_rankin_p018_table_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-primitive-product-rankin-p018-table-router.json

输出：
  data/primitive-product-rankin-p018-sample-table.json
  docs/monograph/prime-matrix-strict-primitive-product-rankin-p018-table-router.json
  docs/monograph/prime-matrix-strict-primitive-product-rankin-p018-table-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DATA = ROOT / "data"
OUT_JSON = DOCS / "prime-matrix-strict-primitive-product-rankin-p018-table-router.json"
OUT_MD = DOCS / "prime-matrix-strict-primitive-product-rankin-p018-table-router.md"
OUT_LEDGER = DATA / "primitive-product-rankin-p018-sample-table.json"

HARDPOINT = "PrimitiveProductRankinP018InequalityTable"
LOCAL_FORMULA = "PrimitiveProductLocalRankinWeightFormula"
ACTUAL_BLOCK_LEDGER = "ActualColdProductBlockParameterLedgerForP018Table"
FAILURE_RETURN = "PrimitiveProductRankinFailureReturnPacketLedger"
WEIGHT_COMPARISON = "PrimitiveProductRankinWeightP018Comparison"
CANDIDATE_BOUND = "ColdProductBlockCandidateCountOrSymbolicBound"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    DOCS / "prime-matrix-strict-primitive-product-rankin-weight-comparison-router.json",
    DOCS / "prime-matrix-strict-cold-product-block-inventory-router.json",
    DATA / "primitive-product-rankin-weight-sample-ledger.json",
]


def load_json(path: Path) -> dict[str, Any]:
    """读取依赖 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


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
        "experiments/prime_matrix_strict_primitive_product_rankin_p018_table_router.py": sha256(
            Path(__file__).resolve()
        ),
        "data/primitive-product-rankin-p018-sample-table.json": sha256(OUT_LEDGER),
    }
    for path in SOURCE_FILES:
        if path.exists():
            result[str(path.relative_to(ROOT))] = sha256(path)
    return result


def imported_flags() -> dict[str, bool]:
    """读取 P^0.18 表需要的导入。"""
    weight = load_json(DOCS / "prime-matrix-strict-primitive-product-rankin-weight-comparison-router.json")
    inventory = load_json(DOCS / "prime-matrix-strict-cold-product-block-inventory-router.json")
    return {
        "local_rankin_formula_imported": bool(weight.get("primitive_product_local_rankin_weight_formula_closed")),
        "euler_profile_bound_imported": bool(weight.get("primitive_product_euler_profile_sum_bound_closed")),
        "cold_block_schema_imported": bool(inventory.get("cold_product_dyadic_block_inventory_schema_closed")),
        "cold_candidate_generator_imported": bool(
            inventory.get("cold_product_candidate_set_generator_rule_closed")
        ),
    }


def p018_table_schema() -> list[dict[str, str]]:
    """定义完整 P^0.18 表的最小字段。"""
    return [
        {"field": "source_tuple_hash", "role": "绑定实际 early-zero 反例链 formal unit。"},
        {"field": "P", "role": "给出当前周期基准和 P^0.18 预算。"},
        {"field": "h0", "role": "给出产品除数域和局部 Euler product。"},
        {"field": "registered_common_kernel", "role": "删除已回流共同核素因子。"},
        {"field": "Y", "role": "指定 dyadic 产品块 (Y,2Y]。"},
        {"field": "sigma", "role": "给出该块 Rankin 权重参数。"},
        {"field": "rankin_bound", "role": "计算 min(Y^{-s}Z_+(s),(2Y)^sZ_-(s))。"},
        {"field": "p018_budget", "role": "计算 P^0.18 或同参数剩余预算。"},
        {"field": "verdict", "role": "pass 或 return_required。"},
        {"field": "return_packet", "role": "失败时指向热窗口、共同核、PDEC/SAE、固定历史或 ColumnCRT。"},
    ]


def verdict_rule_rows() -> list[dict[str, str]]:
    """定义表行判定规则。"""
    return [
        {
            "rule": "rankin_pass",
            "condition": "rankin_bound <= p018_budget",
            "effect": "该块支撑进入 P^0.18 预算。",
        },
        {
            "rule": "rankin_fail_return",
            "condition": "rankin_bound > p018_budget",
            "effect": "该块不能留在 primitive dispersion，必须有 return_packet。",
        },
        {
            "rule": "missing_actual_row",
            "condition": "缺 source_tuple_hash/P/h0/Y/sigma",
            "effect": "表不存在，不能宣称权重比较闭合。",
        },
        {
            "rule": "sample_row",
            "condition": "来自诊断样本而非全体实际块",
            "effect": "只用于检验计算规则，不升级为证明。",
        },
    ]


def build_sample_table() -> dict[str, Any]:
    """把 Rankin 权重样本转为 P^0.18 判定样表。"""
    source = load_json(DATA / "primitive-product-rankin-weight-sample-ledger.json")
    rows = []
    for index, item in enumerate(source.get("rows", []), start=1):
        passes = bool(item["passes_p018_on_sample_grid"])
        rows.append(
            {
                "sample_row_id": f"sample-{index}",
                "P": item["P"],
                "h0": item["h0"],
                "Y": item["Y"],
                "block": item["block"],
                "registered_common_kernel": item["registered_common_kernel"],
                "sigma": item["best_sigma_grid"],
                "rankin_bound": item["best_bound_grid"],
                "p018_budget": item["p018_budget"],
                "actual_count_diagnostic_only": item["actual_count_diagnostic_only"],
                "verdict": "pass" if passes else "return_required",
                "return_packet": None if passes else "missing_in_current_corpus",
                "diagnostic_only": True,
            }
        )
    return {
        "ledger_type": "primitive_product_rankin_p018_sample_table",
        "diagnostic_only": True,
        "source": "data/primitive-product-rankin-weight-sample-ledger.json",
        "rows": rows,
        "sample_table_executable": bool(rows),
        "sample_fail_rows": [row for row in rows if row["verdict"] == "return_required"],
        "all_sample_rows_pass": all(row["verdict"] == "pass" for row in rows) if rows else False,
    }


def obstruction_rows(sample_table: dict[str, Any]) -> list[dict[str, str]]:
    """列出 P^0.18 表的阻断点。"""
    fail_count = len(sample_table["sample_fail_rows"])
    return [
        {
            "obstruction": "actual_block_rows_missing",
            "meaning": "已有产品块 schema，但没有全体实际 source_tuple/P/h0/Y 行。",
            "next": ACTUAL_BLOCK_LEDGER,
        },
        {
            "obstruction": "sample_fail_rows_need_return",
            "meaning": f"诊断样表中有 {fail_count} 个失败行；这说明失败回流包是必要字段。",
            "next": FAILURE_RETURN,
        },
        {
            "obstruction": "budget_is_rowwise_not_global_constant",
            "meaning": "P^0.18 比较依赖每行 h0、Y、共同核和 sigma，不能用单个固定常数替代。",
            "next": ACTUAL_BLOCK_LEDGER,
        },
        {
            "obstruction": "old_inventory_schema_not_actual_table",
            "meaning": "cold 产品块清单当前只闭合 schema 与候选生成规则，尚未给出实际参数表。",
            "next": ACTUAL_BLOCK_LEDGER,
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


def decision_rows(flags: dict[str, bool], sample_table: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    schema_closed = (
        flags["local_rankin_formula_imported"]
        and flags["euler_profile_bound_imported"]
        and flags["cold_block_schema_imported"]
        and flags["cold_candidate_generator_imported"]
    )
    return [
        decision_row(
            "PrimitiveProductRankinP018TableTargetImported",
            True,
            flags["local_rankin_formula_imported"],
            "上一层已闭合局部 Rankin 权重公式，当前目标是逐块 P^0.18 表。",
            HARDPOINT,
        ),
        decision_row(
            "P018TableSchemaClosed",
            schema_closed,
            schema_closed,
            "表字段和 pass/return 判定规则已闭合。",
            "schema closed",
        ),
        decision_row(
            "DiagnosticP018SampleTableExecutable",
            True,
            sample_table["sample_table_executable"],
            "诊断样表可生成；它只检验判定规则，不代表全体实际块。",
            "diagnostic only",
        ),
        decision_row(
            "DiagnosticP018SampleAllRowsPass",
            True,
            sample_table["all_sample_rows_pass"],
            "诊断样本是否全部通过；失败行说明必须有 return_packet。",
            FAILURE_RETURN,
        ),
        decision_row(
            "ActualColdProductBlockParameterLedgerPresent",
            False,
            False,
            "尚未列出全体实际 source tuple / P / h0 / Y / common-kernel 参数行。",
            ACTUAL_BLOCK_LEDGER,
        ),
        decision_row(
            "PrimitiveProductRankinFailureReturnPacketLedgerClosed",
            False,
            False,
            "尚未为所有 P^0.18 失败行给出目标专用回流包。",
            FAILURE_RETURN,
        ),
        decision_row(
            "PrimitiveProductRankinP018InequalityTablePresent",
            False,
            False,
            "只有 schema 与诊断样表，缺全体实际行和失败回流，因此完整表不存在。",
            f"{ACTUAL_BLOCK_LEDGER} AND {FAILURE_RETURN}",
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
            "权重比较未闭合，cold 产品候选计数/符号界仍未闭合。",
            CANDIDATE_BOUND,
        ),
        decision_row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "仍未得到排除早期零行反例链的终端矛盾。",
            f"{ACTUAL_BLOCK_LEDGER} AND {FAILURE_RETURN} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 P^0.18 表路由证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    sample_table = build_sample_table()
    OUT_LEDGER.write_text(json.dumps(sample_table, indent=2, sort_keys=True), encoding="utf-8")
    flags = imported_flags()
    decisions = decision_rows(flags, sample_table)
    return {
        "certificate_type": "prime_matrix_strict_primitive_product_rankin_p018_table_router",
        "status": "p018_table_schema_closed_actual_block_rows_and_failure_returns_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hardpoint_before_router": HARDPOINT,
        "hardpoint_after_router": f"{ACTUAL_BLOCK_LEDGER} AND {FAILURE_RETURN}",
        "next_direct_attack_target": ACTUAL_BLOCK_LEDGER,
        "imported_flags": flags,
        "p018_table_schema": p018_table_schema(),
        "verdict_rules": verdict_rule_rows(),
        "obstruction_rows": obstruction_rows(sample_table),
        "decision_table": decisions,
        "p018_table_schema_closed": bool(
            next(item for item in decisions if item["gate"] == "P018TableSchemaClosed")["proved"]
        ),
        "diagnostic_p018_sample_table_executable": sample_table["sample_table_executable"],
        "diagnostic_p018_sample_all_rows_pass": sample_table["all_sample_rows_pass"],
        "actual_cold_product_block_parameter_ledger_present": False,
        "primitive_product_rankin_failure_return_packet_ledger_closed": False,
        "primitive_product_rankin_p018_inequality_table_present": False,
        "primitive_product_rankin_weight_p018_comparison_proved": False,
        "cold_product_block_candidate_count_or_symbolic_bound_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "plain_conclusion": (
            "`PrimitiveProductRankinP018InequalityTable` 的表结构和判定规则已闭合："
            "每行必须给出 `source_tuple_hash,P,h0,Y,common_kernel,sigma,rankin_bound,p018_budget`，"
            "并按 `rankin_bound<=p018_budget` 判定 pass，否则必须附回流包。"
            "但当前只有 schema 与诊断样表，没有全体实际 cold 产品块参数行；"
            "且诊断样表中已有失败行，说明失败回流包不能省略。"
            "最新最窄点转为 `ActualColdProductBlockParameterLedgerForP018Table`。"
        ),
        "source_hashes": source_hashes(),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix strict primitive product Rankin P^0.18 表路由器",
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
        f"p018_table_schema_closed={fmt_bool(result['p018_table_schema_closed'])}",
        f"primitive_product_rankin_p018_inequality_table_present={fmt_bool(result['primitive_product_rankin_p018_inequality_table_present'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 表字段",
        "",
        "| 字段 | 作用 |",
        "|---|---|",
    ]
    for item in result["p018_table_schema"]:
        lines.append(f"| `{table_cell(item['field'])}` | {table_cell(item['role'])} |")
    lines.extend(["", "## 判定规则", "", "| 规则 | 条件 | 效果 |", "|---|---|---|"])
    for item in result["verdict_rules"]:
        lines.append(
            f"| `{table_cell(item['rule'])}` | {table_cell(item['condition'])} | {table_cell(item['effect'])} |"
        )
    lines.extend(["", "## 阻断点", "", "| 阻断 | 含义 | 下一步 |", "|---|---|---|"])
    for item in result["obstruction_rows"]:
        lines.append(
            f"| `{table_cell(item['obstruction'])}` | {table_cell(item['meaning'])} | `{table_cell(item['next'])}` |"
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
            "## 样表",
            "",
            f"- 路径：`{OUT_LEDGER.relative_to(ROOT)}`",
            "- 用途：只检验 P^0.18 表判定规则，不作为全体实际块证明。",
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
    """生成 JSON、Markdown 与样表账本。"""
    DOCS.mkdir(parents=True, exist_ok=True)
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, indent=2, sort_keys=True), encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"status={result['status']}")
    print(f"p018_table_schema_closed={fmt_bool(result['p018_table_schema_closed'])}")
    print(
        "primitive_product_rankin_p018_inequality_table_present="
        f"{fmt_bool(result['primitive_product_rankin_p018_inequality_table_present'])}"
    )
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
