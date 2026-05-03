#!/usr/bin/env python3
"""扫描显式阈值账本的敏感参数。

用法示例：
  python3 experiments/threshold_sensitivity_scan.py
  python3 experiments/threshold_sensitivity_scan.py --max-log-p 300 --json
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import math
from pathlib import Path
from typing import Any

LEDGER_PATH = Path(__file__).with_name("explicit_threshold_ledger.py")


def load_ledger():
    """动态载入阈值账本模块，避免复制公式。"""
    spec = importlib.util.spec_from_file_location("explicit_threshold_ledger", LEDGER_PATH)
    if spec is None or spec.loader is None:
        raise SystemExit(f"无法载入 {LEDGER_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def current_constants(ledger: Any) -> dict[str, Any]:
    """返回当前压缩账本默认常数。"""
    constants = dict(ledger.TEMPLATE)
    constants["C_Cheb"] = 1.0 + 1.0 / 36260.0
    constants["A1"] = 8.0
    constants["low_moment_uncapped"] = True
    constants["low_moment_C"] = 4.0
    constants["A_row"] = 4.0
    constants["delta_row"] = 0.25
    return constants


def threshold(ledger: Any, constants: dict[str, Any], max_log_p: float) -> dict[str, Any]:
    """计算阈值与报告。"""
    derived = ledger.derived_constants(constants)
    result = ledger.bisect_threshold(constants, derived, max_log_p)
    return {
        "log_P": result["log_P_tail"],
        "report": result["report"],
        "derived": derived,
    }


def safe_threshold(ledger: Any, constants: dict[str, Any], max_log_p: float) -> dict[str, Any]:
    """失败时保留错误，便于扫描表不中断。"""
    try:
        return threshold(ledger, constants, max_log_p)
    except SystemExit as exc:
        return {"error": str(exc)}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-log-p", type=float, default=300.0)
    parser.add_argument("--json", action="store_true", help="输出 JSON，便于后续归档")
    args = parser.parse_args()

    ledger = load_ledger()
    base = current_constants(ledger)

    scans: dict[str, list[dict[str, Any]]] = {}
    for name, values in {
        "A_row": [6, 5, 4, 3, 2, 1.5, 1, 0.5],
        "delta_row": [0.1, 0.2, 0.25, 1 / 3, 0.5, 0.75, 1.0],
        "delta_col": [0.1, 0.125, 0.2, 0.25, 1 / 3, 0.5, 0.75, 1.0],
        "mu_col": [0.125, 0.2, 0.25, 1 / 3, 0.5, 0.75, 1.0],
        "low_moment_C": [6, 5, 4, 3.5, 3.2, 3.1, 3.0],
    }.items():
        rows = []
        for value in values:
            constants = dict(base)
            constants[name] = value
            item = {name: value, **safe_threshold(ledger, constants, args.max_log_p)}
            rows.append(item)
        scans[name] = rows

    derived = ledger.derived_constants(base)
    targets = []
    for x in [84.25449700383089, 80, 75, 72.89494933376204, 70, 60, 50]:
        row_prob = ledger.best_log_probability(
            x,
            0.5,
            base["mu_row"],
            base["a_row"],
            base["delta_row"],
            derived["C_USC"],
            derived["c0"],
            base["low_moment_C"],
            base["low_moment_cutoff"],
            base["low_moment_uncapped"],
        )
        col_prob = ledger.best_log_probability(
            x,
            1.0,
            base["mu_col"],
            base["a_col"],
            base["delta_col"],
            derived["C_USC"],
            derived["c0"],
            base["low_moment_C"],
            base["low_moment_cutoff"],
            base["low_moment_uncapped"],
        )
        targets.append(
            {
                "log_P_target": x,
                "required_A_row_at_current_row_tail": -row_prob["log_prob"] / math.log(x),
                "col_margin_at_current_col_tail": -col_prob["log_prob"] - x,
                "row_log_bracket": row_prob["log_bracket"],
                "col_log_bracket": col_prob["log_bracket"],
            }
        )

    arow2 = dict(base)
    arow2["A_row"] = 2.0
    derived_arow2 = ledger.derived_constants(arow2)
    column_floor_targets = []
    for x in [73.7964348428418, 72.89494933376204, 70, 65, 60, 55, 50]:
        row_prob = ledger.best_log_probability(
            x,
            0.5,
            arow2["mu_row"],
            arow2["a_row"],
            arow2["delta_row"],
            derived_arow2["C_USC"],
            derived_arow2["c0"],
            arow2["low_moment_C"],
            arow2["low_moment_cutoff"],
            arow2["low_moment_uncapped"],
        )
        col_prob = ledger.best_log_probability(
            x,
            1.0,
            arow2["mu_col"],
            arow2["a_col"],
            arow2["delta_col"],
            derived_arow2["C_USC"],
            derived_arow2["c0"],
            arow2["low_moment_C"],
            arow2["low_moment_cutoff"],
            arow2["low_moment_uncapped"],
        )
        row_margin = -row_prob["log_prob"] - arow2["A_row"] * math.log(x)
        col_margin = -col_prob["log_prob"] - x
        deficit = max(0.0, -col_margin)
        column_floor_targets.append(
            {
                "log_P_target": x,
                "row_margin_with_A_row_2": row_margin,
                "col_margin": col_margin,
                "required_delta_col_ratio_if_only_delta_changes": math.exp(deficit / 4.0),
                "required_mu_col_ratio_if_only_mu_changes": math.exp(deficit / 2.0),
                "required_a_col_drop_if_only_a_changes": deficit / (2.0 * math.log(x)),
            }
        )

    combo_cases = []
    for arow in [2.0, 1.8, 1.5, 1.28, 1.0]:
        for delta_col, mu_col, a_col in [
            (0.1, 0.125, 1.0),
            (0.2, 0.125, 1.0),
            (0.1, 0.25, 1.0),
            (0.2, 0.25, 1.0),
            (0.1, 0.125, 0.75),
        ]:
            constants = dict(base)
            constants.update({"A_row": arow, "delta_col": delta_col, "mu_col": mu_col, "a_col": a_col})
            item = {"A_row": arow, "delta_col": delta_col, "mu_col": mu_col, "a_col": a_col, **safe_threshold(ledger, constants, args.max_log_p)}
            combo_cases.append(item)

    delta_row_cases = []
    for delta_row in [0.25, 0.3, 1 / 3, 0.4, 0.5, 0.6, 0.75, 1.0]:
        constants = dict(base)
        constants.update({"A_row": 2.0, "delta_col": 0.2, "delta_row": delta_row})
        item = {"A_row": 2.0, "delta_col": 0.2, "delta_row": delta_row, **safe_threshold(ledger, constants, args.max_log_p)}
        delta_row_cases.append(item)

    safe_gap_cases = []
    for arow, delta_col in [(4.0, 0.1), (2.0, 0.2)]:
        for delta_row in [0.04541149432351807, 0.058753479006055, 0.09082298864703614, 0.117506958012111, 0.25]:
            constants = dict(base)
            constants.update({"A_row": arow, "delta_col": delta_col, "delta_row": delta_row})
            safe_gap_cases.append({"A_row": arow, "delta_col": delta_col, "delta_row": delta_row, **safe_threshold(ledger, constants, args.max_log_p)})

    output = {"base": threshold(ledger, base, args.max_log_p), "scans": scans, "target_requirements": targets, "A_row_2_column_floor": column_floor_targets, "sub70_combo_cases": combo_cases, "delta_row_sub70_cases": delta_row_cases, "safe_gap_cases": safe_gap_cases}
    if args.json:
        print(json.dumps(output, ensure_ascii=False, indent=2))
    else:
        print(f"当前阈值: log_P={output['base']['log_P']:.6f}")
        print("A_row 扫描:")
        for row in scans["A_row"]:
            if "error" in row:
                print(f"  A_row={row['A_row']}: {row['error']}")
            else:
                report = row["report"]
                print(f"  A_row={row['A_row']}: log_P={row['log_P']:.6f}, row_margin={report['row_tail_margin']:.3g}, col_margin={report['col_tail_margin']:.3g}")
        print("目标阈值反推:")
        for row in targets:
            print(
                "  log_P={log_P_target:.3f}: 需 A_row≤{required_A_row_at_current_row_tail:.3f}, 列余量={col_margin_at_current_col_tail:.3f}".format(**row)
            )
        print("A_row=2 后的列侧/行侧余量:")
        for row in column_floor_targets:
            print(
                "  log_P={log_P_target:.3f}: 行余量={row_margin_with_A_row_2:.3f}, 列余量={col_margin:.3f}, 若只改列需 delta×{required_delta_col_ratio_if_only_delta_changes:.2f}/mu×{required_mu_col_ratio_if_only_mu_changes:.2f}/a降{required_a_col_drop_if_only_a_changes:.2f}".format(**row)
            )
        print("低于 70 的组合诊断候选:")
        for row in combo_cases:
            if "log_P" in row and row["log_P"] <= 70.1:
                print(
                    "  A_row={A_row:g}, delta_col={delta_col:g}, mu_col={mu_col:g}, a_col={a_col:g}: log_P={log_P:.3f}".format(**row)
                )
        print("delta_row 诊断路线（含不可直接证明的大阈值）:")
        for row in delta_row_cases:
            if "log_P" in row:
                print(
                    "  A_row=2, delta_col=0.2, delta_row={delta_row:g}: log_P={log_P:.3f}".format(**row)
                )
        print("安全间隙对齐用例:")
        for row in safe_gap_cases:
            if "log_P" in row:
                print(
                    "  A_row={A_row:g}, delta_col={delta_col:g}, delta_row={delta_row:.4g}: log_P={log_P:.3f}".format(**row)
                )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
