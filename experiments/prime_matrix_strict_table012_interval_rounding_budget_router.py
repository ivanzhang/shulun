#!/usr/bin/env python3
"""生成 strict table_012 theta 归档区间误差预算证书。

用法示例：
  python3 experiments/prime_matrix_strict_table012_interval_rounding_budget_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-table012-interval-rounding-budget-router.json

本证书只关闭“误差预算能否吸收归档数值误差”的传递层：
若每个 log(p) 的数值贡献由外向区间包含，且累计 theta/RHS 传播误差被
runner 登记的 numeric_error_bound 覆盖，则 34 行归档的最小保护余量足以
推出 table_012 的 theta 上界。它不声称 log(p) 外向区间 oracle 已经自足实现。
"""

from __future__ import annotations

import hashlib
import json
from decimal import Decimal, getcontext
from pathlib import Path
from typing import Any


getcontext().prec = 80

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DATA = ROOT / "data"

OUT_JSON = DOCS / "prime-matrix-strict-table012-interval-rounding-budget-router.json"
OUT_MD = DOCS / "prime-matrix-strict-table012-interval-rounding-budget-router.md"

EXTREMAL_ROUTER = DOCS / "prime-matrix-strict-table012-extremal-runner-frontier-router.json"
ARCHIVE = DATA / "theta-table012-extremal-archive.jsonl"
SEGMENT_LEDGER = DATA / "theta-table012-extremal-segments.jsonl"
ARCHIVE_AUDIT = ROOT / "experiments" / "prime_matrix_table012_theta_extremal_archive_audit.py"
RUNNER = ROOT / "experiments" / "prime_matrix_table012_theta_extremal_runner.cpp"

FULL_ARCHIVE = "FullTable012ThetaExtremalArchiveRunAndHashLedger"
ROUNDING = "Table012DirectedRoundingAndIntervalPropagationLedger"
LOG_INTERVAL = "CertifiedLogSummationIntervalArithmeticForThetaLedger"
LOG_ORACLE = "LogOracleOutwardIntervalImplementationOrFormalUlpCertificate"
INDEPENDENT_ARCHIVE = "IndependentThetaExtremalArchiveForTable012IntervalsLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def sha256(path: Path) -> str:
    """计算文件 SHA256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    """读取 JSONL 记录。"""
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def dec(value: Any) -> Decimal:
    """把归档中的科学计数字符串转成 Decimal。"""
    return Decimal(str(value))


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def numeric_error_bound(row: dict[str, Any]) -> Decimal:
    """读取 runner 已登记的统一数值保护误差。"""
    return dec(row["numeric_error_bound"])


def row_budget(row: dict[str, Any], index: int) -> dict[str, Any]:
    """构造单行误差预算判定。"""
    max_defect = dec(row["max_defect"])
    bound = numeric_error_bound(row)
    margin_after_guard = -(max_defect + bound)
    recorded_margin = dec(row["margin_after_guard"])
    # Decimal 复核归档中的 margin_after_guard 公式是否一致。
    # C++ 对 max_defect、numeric_error_bound、margin_after_guard 分别格式化；
    # 因此允许远小于最小 55 余量的尾数打印误差。
    formula_ok = abs(margin_after_guard - recorded_margin) <= Decimal("1e-12")
    return {
        "index": index,
        "label": row["label"],
        "left": row["left"],
        "right": row["right"],
        "max_x": row["max_x"],
        "max_kind": row["max_kind"],
        "global_prime_count": row["global_prime_count"],
        "max_defect": str(max_defect),
        "numeric_error_bound": str(bound),
        "margin_after_guard": str(recorded_margin),
        "formula_margin_after_guard": str(margin_after_guard),
        "formula_ok": formula_ok,
        "derivative_lower_bound": row["rhs_derivative_lower_bound"],
        "monotone_rhs_certified": dec(row["rhs_derivative_lower_bound"]) > Decimal("0"),
        "passed_under_contract": margin_after_guard > 0 and formula_ok and row.get("passed_with_guard") is True,
    }


def build_result() -> dict[str, Any]:
    """生成证书对象。"""
    extremal = load_json(EXTREMAL_ROUTER)
    rows = load_jsonl(ARCHIVE)
    budgets = [row_budget(row, idx) for idx, row in enumerate(rows)]

    archive_hash = sha256(ARCHIVE) if ARCHIVE.exists() else None
    segment_hash = sha256(SEGMENT_LEDGER) if SEGMENT_LEDGER.exists() else None
    all_rows_present = len(rows) == 34
    full_archive_closed = (
        extremal.get("full_table012_theta_extremal_archive_run_hash_closed") is True
        and all_rows_present
        and archive_hash == extremal.get("full_archive", {}).get("sha256")
    )
    all_budget_passed = bool(budgets) and all(item["passed_under_contract"] for item in budgets)
    all_monotone = bool(budgets) and all(item["monotone_rhs_certified"] for item in budgets)
    min_budget = min(budgets, key=lambda item: dec(item["margin_after_guard"])) if budgets else {}
    max_error = max((dec(item["numeric_error_bound"]) for item in budgets), default=Decimal(0))

    # 这里关闭的是“若 log oracle 外向包含成立，则误差传递足够”的命题。
    # log oracle 本身仍是下一原子，不在本证书中冒充闭合。
    conditional_interval_propagation_closed = full_archive_closed and all_budget_passed and all_monotone

    return {
        "certificate_type": "prime_matrix_strict_table012_interval_rounding_budget_router",
        "status": (
            "table012_interval_budget_reduced_to_log_oracle_outward_certificate"
            if conditional_interval_propagation_closed
            else "table012_interval_budget_open"
        ),
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "full_table012_theta_extremal_archive_run_hash_closed": full_archive_closed,
        "table012_directed_rounding_and_interval_propagation_closed": conditional_interval_propagation_closed,
        "certified_log_summation_interval_arithmetic_closed": False,
        "independent_theta_extremal_archive_closed": False,
        "theta_less_than_identity_to_8e11_self_contained_closed": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "contract": {
            "log_oracle_required": LOG_ORACLE,
            "defect_enclosure_rule": "actual_defect(x) <= archived_defect(x) + numeric_error_bound(row)",
            "runner_numeric_error_bound": "1 + 1e-12 * global_prime_count(row_right)",
            "meaning": (
                "只要每个 log(p) 与 RHS log(x) 的外向区间、累计求和误差和舍入传播"
                "都被 numeric_error_bound 覆盖，归档中的正保护余量即推出严格 theta 上界。"
            ),
        },
        "archive": {
            "path": str(ARCHIVE.relative_to(ROOT)),
            "sha256": archive_hash,
            "row_count": len(rows),
            "expected_rows": 34,
            "segment_ledger_path": str(SEGMENT_LEDGER.relative_to(ROOT)),
            "segment_ledger_sha256": segment_hash,
            "segment_count": len(load_jsonl(SEGMENT_LEDGER)),
        },
        "budget_summary": {
            "min_margin_after_guard": min_budget.get("margin_after_guard"),
            "min_margin_label": min_budget.get("label"),
            "min_margin_max_x": min_budget.get("max_x"),
            "max_numeric_error_bound": str(max_error),
            "all_rows_passed_under_contract": all_budget_passed,
            "all_rhs_derivatives_positive": all_monotone,
        },
        "proof_reduction": [
            {
                "gate": FULL_ARCHIVE,
                "closed": full_archive_closed,
                "meaning": "完整 34 行极值归档与 hash 已由上一证书登记。",
                "remaining": "closed" if full_archive_closed else "rerun full archive and audit hash",
            },
            {
                "gate": "ThetaStepFunctionPrimeJumpReduction",
                "closed": all_monotone,
                "meaning": "R_b(x)=x+b*x/log(x) 在每个 table_012 区间单调递增，theta 只在素数跳点后上升。",
                "remaining": "closed" if all_monotone else "positive derivative check",
            },
            {
                "gate": "UniformDefectErrorBudgetDominatesAllRows",
                "closed": all_budget_passed,
                "meaning": "每行 max_defect + numeric_error_bound < 0；最小保护余量仍约 55。",
                "remaining": "closed" if all_budget_passed else "increase certified error budget or rerun exact interval scan",
            },
            {
                "gate": ROUNDING,
                "closed": conditional_interval_propagation_closed,
                "meaning": "误差预算传递层已闭合为一个明确 log-oracle 输入；不再需要重跑 34 行极值搜索。",
                "remaining": LOG_ORACLE,
            },
            {
                "gate": LOG_INTERVAL,
                "closed": False,
                "meaning": "仍需给 log(p)、log(x) 与累计 theta 求和一个真正外向区间实现或形式化 ulp 证明。",
                "remaining": LOG_ORACLE,
            },
            {
                "gate": INDEPENDENT_ARCHIVE,
                "closed": False,
                "meaning": "独立归档已完成运行/hash和误差预算传递；最后缺 log-oracle 外向包含。",
                "remaining": f"{LOG_INTERVAL}",
            },
            {
                "gate": "RowColumnUnconditionalClosed",
                "closed": False,
                "meaning": "本证书仍只是 table_012 低段自足输入推进，不产生早期零行反例链终端矛盾。",
                "remaining": DSTRUCTURE,
            },
        ],
        "rows": budgets,
        "source_hashes": {
            str(path.relative_to(ROOT)): sha256(path)
            for path in [EXTREMAL_ROUTER, ARCHIVE, SEGMENT_LEDGER, ARCHIVE_AUDIT, RUNNER]
            if path.exists()
        },
        "next_direct_attack_target": LOG_ORACLE,
        "parallel_attack_targets": [LOG_INTERVAL, DSTRUCTURE],
        "plain_conclusion": (
            "table_012 完整归档后的下一层已收缩：34 行极值搜索和 hash 已闭合，"
            "误差预算传递也足以吸收所有行，最薄行仍有正保护余量。"
            "严格自足版现在只剩 log(p)/log(x) 外向区间 oracle 或等价 ulp 证书；"
            "在补齐该原子前，不能声称 theta 表自足闭合，更不能声称行/列命题无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    summary = result["budget_summary"]
    lines = [
        "# Prime Matrix strict table_012 区间误差预算证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"full_table012_theta_extremal_archive_run_hash_closed={fmt_bool(result['full_table012_theta_extremal_archive_run_hash_closed'])}",
        f"table012_directed_rounding_and_interval_propagation_closed={fmt_bool(result['table012_directed_rounding_and_interval_propagation_closed'])}",
        f"certified_log_summation_interval_arithmetic_closed={fmt_bool(result['certified_log_summation_interval_arithmetic_closed'])}",
        f"independent_theta_extremal_archive_closed={fmt_bool(result['independent_theta_extremal_archive_closed'])}",
        f"theta_less_than_identity_to_8e11_self_contained_closed={fmt_bool(result['theta_less_than_identity_to_8e11_self_contained_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 预算结论",
        "",
        "| field | value |",
        "| --- | --- |",
        f"| `archive_sha256` | `{table_cell(result['archive']['sha256'])}` |",
        f"| `row_count` | `{result['archive']['row_count']}` |",
        f"| `segment_count` | `{result['archive']['segment_count']}` |",
        f"| `min_margin_after_guard` | `{table_cell(summary.get('min_margin_after_guard'))}` |",
        f"| `min_margin_label` | `{table_cell(summary.get('min_margin_label'))}` |",
        f"| `min_margin_max_x` | `{table_cell(summary.get('min_margin_max_x'))}` |",
        f"| `max_numeric_error_bound` | `{table_cell(summary.get('max_numeric_error_bound'))}` |",
        f"| `next_direct_attack_target` | `{result['next_direct_attack_target']}` |",
        "",
        "## 2. 传递定理",
        "",
        "设 `R_b(x)=x+b*x/log(x)`。每个 table_012 行中 `b<0` 且 `R_b'(x)>0`，"
        "而 `theta(x)` 只在素数跳点后增加。因此每行只需检查左端点和素数跳点。"
        "归档给出这些点上的最大数值缺陷 `D_i`；若真实缺陷被包含在"
        "`D_i + numeric_error_bound_i` 之下，则 `D_i+numeric_error_bound_i<0` "
        "直接推出整行 `theta(x)<=R_b(x)<x`。",
        "",
        "本证书已经逐行复核 `D_i+numeric_error_bound_i<0`；唯一未闭合的是"
        "`numeric_error_bound_i` 对所有 `log(p)`、`log(x)` 和累计求和舍入的外向包含证明。",
        "",
        "## 3. 判定表",
        "",
        "| gate | closed | meaning | remaining |",
        "| --- | --- | --- | --- |",
    ]
    for item in result["proof_reduction"]:
        lines.append(
            "| `{}` | `{}` | {} | {} |".format(
                table_cell(item["gate"]),
                fmt_bool(item["closed"]),
                table_cell(item["meaning"]),
                table_cell(item["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 最薄行附近",
            "",
            "| index | label | max_x | max_kind | numeric_error_bound | margin_after_guard |",
            "| ---: | --- | ---: | --- | ---: | ---: |",
        ]
    )
    sorted_rows = sorted(result["rows"], key=lambda item: dec(item["margin_after_guard"]))[:8]
    for row in sorted_rows:
        lines.append(
            "| `{}` | `{}` | `{}` | `{}` | `{}` | `{}` |".format(
                row["index"],
                table_cell(row["label"]),
                table_cell(row["max_x"]),
                table_cell(row["max_kind"]),
                table_cell(row["numeric_error_bound"]),
                table_cell(row["margin_after_guard"]),
            )
        )
    lines.extend(
        [
            "",
            "## 5. 下一最窄点",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """写出 JSON 与 Markdown。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result) + "\n", encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")
    print(
        "table012_directed_rounding_and_interval_propagation_closed="
        f"{fmt_bool(result['table012_directed_rounding_and_interval_propagation_closed'])}"
    )
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")


if __name__ == "__main__":
    main()
