#!/usr/bin/env python3
"""生成 strict no-return Rankin P^0.18 pass/return 同步证书。

用法示例：
  python3 experiments/prime_matrix_strict_no_return_rankin_p018_pass_return_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-no-return-rankin-p018-pass-return-sync-router.json

输出：
  docs/monograph/prime-matrix-strict-no-return-rankin-p018-pass-return-sync-router.json
  docs/monograph/prime-matrix-strict-no-return-rankin-p018-pass-return-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DATA = ROOT / "data"
OUT_JSON = DOCS / "prime-matrix-strict-no-return-rankin-p018-pass-return-sync-router.json"
OUT_MD = DOCS / "prime-matrix-strict-no-return-rankin-p018-pass-return-sync-router.md"

HARDPOINT = "PrimitiveProductRankinP018InequalityTable"
PASS_RETURN = "NoReturnPrimitiveProductRankinP018PassOrFailureReturnTable"
SIGMA_TABLE = "PerBlockRankinSigmaSelectionTable"
FAILURE_RETURN = "PrimitiveProductRankinFailureReturnPacketLedger"
RETURN_ABSORB = "CarrierLCMCompatibilityReturnBranchExclusionOrAbsorption"
SPARSE_BUDGET = "SparseHistoryDemandExceedsNonpersistentSupplyBudget"
PERSISTENT_TERMINAL = "IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    "prime-matrix-strict-no-return-actual-dyadic-block-enumerator-router.json",
    "prime-matrix-strict-primitive-product-rankin-p018-table-router.json",
    "prime-matrix-strict-primitive-product-rankin-weight-comparison-router.json",
    "prime-matrix-strict-primitive-product-projection-rule-router.json",
    "prime-matrix-strict-carrier-lcm-return-branch-frontier-router.json",
]


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件 SHA256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖证据哈希。"""
    result = {
        "experiments/prime_matrix_strict_no_return_rankin_p018_pass_return_sync_router.py": sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = sha256(path)
    sample = DATA / "primitive-product-rankin-p018-sample-table.json"
    if sample.exists():
        result["data/primitive-product-rankin-p018-sample-table.json"] = sha256(sample)
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
    """读取 no-return Rankin pass/return 同步需要的导入。"""
    enum_doc = load_json(DOCS / "prime-matrix-strict-no-return-actual-dyadic-block-enumerator-router.json")
    p018 = load_json(DOCS / "prime-matrix-strict-primitive-product-rankin-p018-table-router.json")
    weight = load_json(DOCS / "prime-matrix-strict-primitive-product-rankin-weight-comparison-router.json")
    projection = load_json(DOCS / "prime-matrix-strict-primitive-product-projection-rule-router.json")
    return_branch = load_json(DOCS / "prime-matrix-strict-carrier-lcm-return-branch-frontier-router.json")
    sample = load_json(DATA / "primitive-product-rankin-p018-sample-table.json")
    return {
        "no_return_enumerator_imported": enum_doc.get(
            "actual_dyadic_cold_product_block_enumerator_for_no_return_h0_closed"
        )
        is True,
        "rankin_target_imported": enum_doc.get("next_direct_attack_target") == HARDPOINT,
        "p018_schema_closed": p018.get("p018_table_schema_closed") is True,
        "rankin_formula_closed": weight.get("primitive_product_local_rankin_weight_formula_closed") is True
        and weight.get("primitive_product_euler_profile_sum_bound_closed") is True,
        "primitive_projection_closed": projection.get("primitive_product_projection_rule_executable_hash_closed")
        is True,
        "return_branch_frontier_closed": return_branch.get("return_branch_alphabet_frontier_closed") is True,
        "sample_table_executable": sample.get("sample_table_executable") is True,
        "diagnostic_sample_all_rows_pass": sample.get("all_sample_rows_pass") is True,
        "diagnostic_fail_rows_present": bool(sample.get("sample_fail_rows")),
    }


def pass_return_rows() -> list[dict[str, str]]:
    """列出 pass/return 表规则。"""
    return [
        {
            "row_type": "rankin_pass",
            "condition": "there exists an admitted sigma with rankin_bound(P,h0,Y,kernel,sigma)<=P^0.18 budget",
            "effect": "block support is charged to primitive Rankin budget",
        },
        {
            "row_type": "rankin_return",
            "condition": "all admitted sigma choices fail the P^0.18 budget, or kernel/profile is not primitive-clean",
            "effect": "block must carry a return_packet",
        },
        {
            "row_type": "sigma_missing",
            "condition": "block has h0/Y but no sigma selection or finite sigma grid certificate",
            "effect": f"route to {SIGMA_TABLE}",
        },
        {
            "row_type": "return_packet_missing",
            "condition": "rankin_bound exceeds budget and return_packet is absent",
            "effect": f"route to {FAILURE_RETURN}",
        },
        {
            "row_type": "global_return",
            "condition": "source-defect or valuation-overflow branch",
            "effect": f"route to {RETURN_ABSORB}",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    schema_closed = result["no_return_rankin_p018_pass_or_return_schema_closed"]
    return [
        row(
            "NoReturnEnumeratorImported",
            result["no_return_enumerator_imported"],
            result["no_return_enumerator_imported"],
            "no-return 分支已有 h0^car 和唯一 dyadic 产品块枚举规则。",
            "ActualDyadicColdProductBlockEnumeratorForH0",
        ),
        row(
            "RankinFormulaAndProjectionImported",
            result["rankin_formula_closed"] and result["primitive_projection_closed"],
            result["rankin_formula_closed"] and result["primitive_projection_closed"],
            "候选 d 的 primitive projection 与局部 Rankin/Euler 权重公式可用。",
            "PrimitiveProductRankinWeightP018Comparison",
        ),
        row(
            "P018PassReturnSchemaClosed",
            schema_closed,
            schema_closed,
            "每个 no-return 枚举块必须二分为 pass 或带 return_packet 的失败行。",
            PASS_RETURN,
        ),
        row(
            "DiagnosticFailRowsRequireReturn",
            result["diagnostic_fail_rows_present"],
            result["diagnostic_fail_rows_present"],
            "诊断样表已有失败行，说明失败回流包是必要项。",
            FAILURE_RETURN,
        ),
        row(
            "AllNoReturnRankinRowsPassProved",
            False,
            False,
            "尚未证明所有 no-return 枚举块都存在通过 P^0.18 的 sigma。",
            SIGMA_TABLE,
        ),
        row(
            "PrimitiveProductRankinFailureReturnPacketLedgerClosed",
            False,
            False,
            "尚未为所有失败块给出热窗口、共同核、PDEC/SAE 或固定历史回流包。",
            FAILURE_RETURN,
        ),
        row(
            "PrimitiveProductRankinP018InequalityTablePresent",
            False,
            False,
            "pass/return schema 已闭合，但缺全体块的 sigma/pass/return 实表。",
            f"{SIGMA_TABLE} AND {FAILURE_RETURN}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "仍未得到早期零行反例链的最终矛盾。",
            f"{FAILURE_RETURN} AND {RETURN_ABSORB} AND {SPARSE_BUDGET} AND {PERSISTENT_TERMINAL} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 no-return Rankin P^0.18 pass/return 同步证书。"""
    flags = imported_flags()
    schema_closed = (
        flags["no_return_enumerator_imported"]
        and flags["rankin_target_imported"]
        and flags["p018_schema_closed"]
        and flags["rankin_formula_closed"]
        and flags["primitive_projection_closed"]
        and flags["return_branch_frontier_closed"]
    )
    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_strict_no_return_rankin_p018_pass_return_sync_router",
        "status": "no_return_rankin_p018_pass_return_schema_closed_sigma_failure_return_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        **flags,
        "no_return_rankin_p018_pass_or_return_schema_closed": schema_closed,
        "all_no_return_rankin_rows_pass_proved": False,
        "per_block_rankin_sigma_selection_table_proved": False,
        "primitive_product_rankin_failure_return_packet_ledger_closed": False,
        "primitive_product_rankin_p018_inequality_table_present": False,
        "carrier_lcm_compatibility_return_branch_exclusion_or_absorption_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": HARDPOINT,
        "hardpoint_after_router": f"{SIGMA_TABLE} AND {FAILURE_RETURN} AND {RETURN_ABSORB}",
        "next_direct_attack_target": FAILURE_RETURN,
        "parallel_attack_targets": [
            SIGMA_TABLE,
            RETURN_ABSORB,
            SPARSE_BUDGET,
            PERSISTENT_TERMINAL,
            DSTRUCTURE,
        ],
        "pass_return_rows": pass_return_rows(),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "no-return dyadic 块枚举器关闭后，`PrimitiveProductRankinP018InequalityTable` 的缺口不再是 h0/Y "
            "字段来源，而是逐块 pass-or-return：每个枚举块必须给出 sigma 使 Rankin bound 不超过 P^0.18，"
            "否则必须附热窗口、共同核、PDEC/SAE、固定历史或 carrier-lcm return 的命名回流包。"
            "诊断样表已有失败行，因此不能只靠公式层宣称全部通过。本步关闭 pass/return schema，"
            "但不关闭 sigma 选择表、失败回流包或全局行/列命题。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写出 Markdown 摘要。"""
    lines: list[str] = [
        "# Prime Matrix strict no-return Rankin P^0.18 pass/return 同步路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"no_return_rankin_p018_pass_or_return_schema_closed={fmt_bool(result['no_return_rankin_p018_pass_or_return_schema_closed'])}",
        f"all_no_return_rankin_rows_pass_proved={fmt_bool(result['all_no_return_rankin_rows_pass_proved'])}",
        f"per_block_rankin_sigma_selection_table_proved={fmt_bool(result['per_block_rankin_sigma_selection_table_proved'])}",
        f"primitive_product_rankin_failure_return_packet_ledger_closed={fmt_bool(result['primitive_product_rankin_failure_return_packet_ledger_closed'])}",
        f"primitive_product_rankin_p018_inequality_table_present={fmt_bool(result['primitive_product_rankin_p018_inequality_table_present'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. Pass/Return 规则",
        "",
        "| row_type | condition | effect |",
        "| --- | --- | --- |",
    ]
    for item in result["pass_return_rows"]:
        lines.append(
            "| "
            + " | ".join([table_cell(item["row_type"]), table_cell(item["condition"]), table_cell(item["effect"])])
            + " |"
        )
    lines.extend(
        [
            "",
            "## 2. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in result["decision_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(item['gate'])}`",
                    f"`{fmt_bool(item['closed'])}`",
                    f"`{fmt_bool(item['proved'])}`",
                    table_cell(item["meaning"]),
                    table_cell(item["remaining"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 3. 下一步",
            "",
            f"- 主攻：`{result['next_direct_attack_target']}`。",
            "- 并行保留：",
        ]
    )
    for target in result["parallel_attack_targets"]:
        lines.append(f"  - `{target}`")
    lines.extend(
        [
            "",
            "## 4. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for name, digest in sorted(result["source_hashes"].items()):
        lines.append(f"| `{table_cell(name)}` | `{digest}` |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """生成 JSON 与 Markdown 证书。"""
    DOCS.mkdir(parents=True, exist_ok=True)
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result)
    print(result["status"])
    print(
        "no_return_rankin_p018_pass_or_return_schema_closed="
        + fmt_bool(result["no_return_rankin_p018_pass_or_return_schema_closed"])
    )
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
