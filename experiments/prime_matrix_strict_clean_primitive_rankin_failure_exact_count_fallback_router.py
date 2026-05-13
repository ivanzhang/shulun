#!/usr/bin/env python3
"""生成 clean primitive Rankin 失败的精确计数 fallback 路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_clean_primitive_rankin_failure_exact_count_fallback_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-clean-primitive-rankin-failure-exact-count-fallback-router.json

输出：
  docs/monograph/prime-matrix-strict-clean-primitive-rankin-failure-exact-count-fallback-router.json
  docs/monograph/prime-matrix-strict-clean-primitive-rankin-failure-exact-count-fallback-router.md
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DATA = ROOT / "data"
OUT_JSON = DOCS / "prime-matrix-strict-clean-primitive-rankin-failure-exact-count-fallback-router.json"
OUT_MD = DOCS / "prime-matrix-strict-clean-primitive-rankin-failure-exact-count-fallback-router.md"

HARDPOINT = "CleanPrimitiveDispersionRankinFailureExclusionOrSigmaPass"
EXACT_FALLBACK = "ExactPrimitiveBlockCountP018FallbackTable"
FAILURE_PACKET = "PrimitiveProductRankinFailureReturnPacketLedger"
ACTUAL_PAYLOAD = "ActualPrimitiveProductRankinFailurePacketPayloadTable"
SIGMA_TABLE = "PerBlockRankinSigmaSelectionTable"
RETURN_ABSORB = "CarrierLCMCompatibilityReturnBranchExclusionOrAbsorption"
SPARSE_BUDGET = "SparseHistoryDemandExceedsNonpersistentSupplyBudget"
PERSISTENT_TERMINAL = "IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    DOCS / "prime-matrix-strict-primitive-product-rankin-failure-return-packet-router.json",
    DOCS / "prime-matrix-strict-primitive-product-rankin-p018-table-router.json",
    DOCS / "prime-matrix-strict-no-return-actual-dyadic-block-enumerator-router.json",
    DATA / "primitive-product-rankin-p018-sample-table.json",
    DATA / "primitive-product-rankin-weight-sample-ledger.json",
]


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
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
        "experiments/prime_matrix_strict_clean_primitive_rankin_failure_exact_count_fallback_router.py": sha256(
            Path(__file__).resolve()
        )
    }
    for path in SOURCE_FILES:
        if path.exists():
            result[str(path.relative_to(ROOT))] = sha256(path)
    return result


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
    """读取精确计数 fallback 需要的导入。"""
    packet = load_json(DOCS / "prime-matrix-strict-primitive-product-rankin-failure-return-packet-router.json")
    p018 = load_json(DOCS / "prime-matrix-strict-primitive-product-rankin-p018-table-router.json")
    enum_doc = load_json(DOCS / "prime-matrix-strict-no-return-actual-dyadic-block-enumerator-router.json")
    sample = load_json(DATA / "primitive-product-rankin-p018-sample-table.json")
    return {
        "clean_residual_target_imported": packet.get("next_direct_attack_target") == HARDPOINT,
        "failure_packet_schema_closed": packet.get(
            "primitive_product_rankin_failure_return_packet_schema_closed"
        )
        is True,
        "p018_table_schema_closed": p018.get("p018_table_schema_closed") is True,
        "dyadic_enumerator_rule_closed": enum_doc.get(
            "actual_dyadic_cold_product_block_enumerator_for_no_return_h0_closed"
        )
        is True,
        "diagnostic_fail_rows_present": bool(sample.get("sample_fail_rows")),
    }


def refined_verdict_rows() -> list[dict[str, str]]:
    """给出 clean primitive 下的判定细化。"""
    return [
        {
            "verdict": "rankin_pass",
            "condition": "there exists sigma with rankin_bound<=P^0.18",
            "effect": "直接由 Rankin 证书支付该块。",
        },
        {
            "verdict": "exact_count_pass",
            "condition": "rankin_bound>P^0.18 but exact block count<=P^0.18",
            "effect": "Rankin 失败只是上界松弛，不生成 return packet。",
        },
        {
            "verdict": "named_return",
            "condition": "exact block count>P^0.18 and one of the five packet triggers fires",
            "effect": f"进入 {FAILURE_PACKET} 的命名回流包。",
        },
        {
            "verdict": "clean_exact_overbudget",
            "condition": "exact block count>P^0.18 and no named trigger fires",
            "effect": "这才是真正 clean primitive 残项，进入精确计数表或推出矛盾。",
        },
        {
            "verdict": "payload_missing",
            "condition": "actual source_tuple/block/divisor list is absent",
            "effect": f"不能判定，转入 {EXACT_FALLBACK}。",
        },
    ]


def diagnostic_rows() -> list[dict[str, Any]]:
    """用诊断样本展示 Rankin 失败不等于实际支撑失败。"""
    sample = load_json(DATA / "primitive-product-rankin-p018-sample-table.json")
    rows: list[dict[str, Any]] = []
    for item in sample.get("sample_fail_rows", []):
        count = int(item["actual_count_diagnostic_only"])
        budget = float(item["p018_budget"])
        rows.append(
            {
                "sample_row_id": item["sample_row_id"],
                "P": item["P"],
                "h0": item["h0"],
                "Y": item["Y"],
                "rankin_bound": item["rankin_bound"],
                "p018_budget": budget,
                "rankin_overbudget_ratio": float(item["rankin_bound"]) / budget,
                "exact_count_diagnostic_only": count,
                "integer_budget_floor": math.floor(budget),
                "exact_count_passes_p018": count <= budget,
                "refined_diagnostic_verdict": "exact_count_pass" if count <= budget else "diagnostic_overbudget",
            }
        )
    return rows


def fallback_schema_rows() -> list[dict[str, str]]:
    """定义 actual fallback 表字段。"""
    return [
        {
            "field": "source_tuple_hash",
            "role": "绑定早期零行反例 formal unit，防止诊断样本冒充 actual row。",
        },
        {
            "field": "block_id",
            "role": "绑定 dyadic 产品块 `(Y,2Y]` 和 no-return/cold guard。",
        },
        {
            "field": "divisor_count_exact_or_certified_cap",
            "role": "给出精确块计数，或给出可复核上界证书。",
        },
        {
            "field": "rankin_certificate_hash",
            "role": "保留原 Rankin 失败证书，说明 fallback 是处理上界松弛。",
        },
        {
            "field": "packet_trigger_vector",
            "role": "若精确计数仍超预算，登记五类回流触发是否发生。",
        },
        {
            "field": "refined_verdict",
            "role": "`rankin_pass`、`exact_count_pass`、`named_return` 或 `clean_exact_overbudget`。",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        row(
            "CleanPrimitiveResidualTargetImported",
            result["clean_residual_target_imported"],
            result["clean_residual_target_imported"],
            "上一层已把无名失败残项压成 clean primitive Rankin 失败。",
            HARDPOINT,
        ),
        row(
            "RankinFailureNotSupportFailureSeparated",
            result["rankin_failure_not_equivalent_to_support_failure_closed"],
            result["rankin_failure_not_equivalent_to_support_failure_closed"],
            "Rankin 上界失败只说明证书松弛，不等价于实际块计数超预算。",
            "verdict refinement",
        ),
        row(
            "ExactCountFallbackSchemaClosed",
            result["exact_count_fallback_schema_closed"],
            result["exact_count_fallback_schema_closed"],
            "actual clean primitive 行必须先提交精确计数或可复核计数上界。",
            EXACT_FALLBACK,
        ),
        row(
            "DiagnosticRankinFailRowsExactCountPass",
            result["diagnostic_rankin_fail_rows_exact_count_pass"],
            result["diagnostic_rankin_fail_rows_exact_count_pass"],
            "当前诊断样本的 Rankin 失败行全部由 exact_count_pass 消解，不需要回流包。",
            "diagnostic only",
        ),
        row(
            "GlobalExactPrimitiveBlockCountP018FallbackTableProved",
            False,
            False,
            "尚未给出全体 actual clean primitive 块的精确计数 fallback 表。",
            EXACT_FALLBACK,
        ),
        row(
            "CleanPrimitiveDispersionRankinFailureExcludedOrSigmaPass",
            False,
            False,
            "本步只删除 Rankin 失败=支撑失败 的错误等价；全局 clean exact overbudget 仍未排除。",
            f"{EXACT_FALLBACK} OR {SIGMA_TABLE}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "仍未得到排除早期零行反例链的终端矛盾。",
            f"{EXACT_FALLBACK} AND {RETURN_ABSORB} AND {SPARSE_BUDGET} AND {PERSISTENT_TERMINAL} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造精确计数 fallback 路由证书。"""
    flags = imported_flags()
    diagnostic = diagnostic_rows()
    all_diagnostic_exact_pass = bool(diagnostic) and all(item["exact_count_passes_p018"] for item in diagnostic)
    schema_closed = (
        flags["failure_packet_schema_closed"]
        and flags["p018_table_schema_closed"]
        and flags["dyadic_enumerator_rule_closed"]
    )
    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_strict_clean_primitive_rankin_failure_exact_count_fallback_router",
        "status": "clean_primitive_rankin_failure_reduced_to_exact_count_fallback_table",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        **flags,
        "rankin_failure_not_equivalent_to_support_failure_closed": True,
        "exact_count_fallback_schema_closed": schema_closed,
        "diagnostic_rankin_fail_rows_exact_count_pass": all_diagnostic_exact_pass,
        "clean_primitive_false_return_guard_closed": True,
        "exact_primitive_block_count_p018_fallback_table_proved": False,
        "clean_primitive_dispersion_rankin_failure_excluded_or_sigma_pass_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": HARDPOINT,
        "hardpoint_after_router": f"{EXACT_FALLBACK} OR {SIGMA_TABLE}",
        "next_direct_attack_target": EXACT_FALLBACK,
        "parallel_attack_targets": [
            SIGMA_TABLE,
            ACTUAL_PAYLOAD,
            FAILURE_PACKET,
            RETURN_ABSORB,
            SPARSE_BUDGET,
            PERSISTENT_TERMINAL,
            DSTRUCTURE,
        ],
        "refined_verdict_rows": refined_verdict_rows(),
        "fallback_schema_rows": fallback_schema_rows(),
        "diagnostic_exact_count_rows": diagnostic,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "clean primitive 残项中必须先区分 Rankin 上界失败和实际支撑失败："
            "`rankin_bound>P^0.18` 只说明该 Rankin 证书太松；若实际块计数仍不超过 `P^0.18`，"
            "该行应判为 `exact_count_pass`，不能生成回流包。当前诊断失败行全部属于这种情形。"
            "因此 `CleanPrimitiveDispersionRankinFailureExclusionOrSigmaPass` 被压缩为 "
            f"`{EXACT_FALLBACK}` 或逐块 sigma 表；全体 actual fallback 表仍未完成。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写出 Markdown 摘要。"""
    lines: list[str] = [
        "# Prime Matrix strict clean primitive Rankin 失败精确计数 fallback 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"rankin_failure_not_equivalent_to_support_failure_closed={fmt_bool(result['rankin_failure_not_equivalent_to_support_failure_closed'])}",
        f"exact_count_fallback_schema_closed={fmt_bool(result['exact_count_fallback_schema_closed'])}",
        f"diagnostic_rankin_fail_rows_exact_count_pass={fmt_bool(result['diagnostic_rankin_fail_rows_exact_count_pass'])}",
        f"exact_primitive_block_count_p018_fallback_table_proved={fmt_bool(result['exact_primitive_block_count_p018_fallback_table_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 判定细化",
        "",
        "| verdict | condition | effect |",
        "| --- | --- | --- |",
    ]
    for item in result["refined_verdict_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(item['verdict'])}`",
                    table_cell(item["condition"]),
                    table_cell(item["effect"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 2. fallback 表字段",
            "",
            "| field | role |",
            "| --- | --- |",
        ]
    )
    for item in result["fallback_schema_rows"]:
        lines.append(f"| `{table_cell(item['field'])}` | {table_cell(item['role'])} |")
    lines.extend(
        [
            "",
            "## 3. 诊断样本校验",
            "",
            "| sample_row_id | Y | h0 | rankin_ratio | exact_count | floor(P^0.18) | refined_verdict |",
            "| --- | ---: | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for item in result["diagnostic_exact_count_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    table_cell(item["sample_row_id"]),
                    str(item["Y"]),
                    str(item["h0"]),
                    f"{item['rankin_overbudget_ratio']:.6f}",
                    str(item["exact_count_diagnostic_only"]),
                    str(item["integer_budget_floor"]),
                    f"`{table_cell(item['refined_diagnostic_verdict'])}`",
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 4. 判定表",
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
            "## 5. 下一步最窄点",
            "",
            f"- 主攻：`{result['next_direct_attack_target']}`。",
            "- 目标：对 actual clean primitive 块给出精确计数或可复核计数上界；只有 exact count 超预算且五类回流均不触发时，才是真正 clean residual。",
            "- 边界：本步不把诊断 exact pass 升级为全体证明，不声明行/列命题无条件闭合。",
            "",
            "## 6. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for file_name, digest in sorted(result["source_hashes"].items()):
        lines.append(f"| `{table_cell(file_name)}` | `{digest}` |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """入口。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    write_markdown(result)
    print(json.dumps({"status": result["status"], "next": result["next_direct_attack_target"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
