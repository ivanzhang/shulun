#!/usr/bin/env python3
"""统一审计 RPZ unit endpoint 后的三条闭合路线。

用法示例：
  python3 experiments/prime_matrix_rpz_three_route_closure_audit.py

三条路线是：

1. formal-family avoidance：证明正式反例族避开 unit endpoint gate；
2. endpoint-PDEC：提交同一坏窗族的 `U_CRT<L_PDEC`；
3. ColumnCRTDefect exclusion：排除固定非零位移 `ColumnCRTDefect(p,d)`。

脚本不尝试伪造闭合。它把每条路线当前已经具备的证书输入、硬障碍和下一步可攻点写成
机器可复现审计包。
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def route_formal_avoidance(lower_grid: dict[str, Any]) -> dict[str, Any]:
    """构造 formal-family 避开路线审计。"""
    summary = lower_grid["summary"]
    current_ledger_closed = summary["actual_grid_fail_nodes"] == 0
    return {
        "route_id": "A_formal_family_avoidance",
        "current_status": (
            "current_ledger_avoids_all_grid_fail"
            if current_ledger_closed
            else "current_ledger_has_grid_fail"
        ),
        "current_ledger_inputs": {
            "actual_transition_nodes": summary["actual_transition_nodes"],
            "actual_grid_fail_nodes": summary["actual_grid_fail_nodes"],
            "formula_count_mismatches": summary["formula_count_mismatches"],
            "formula_delta_mismatches": summary["formula_delta_mismatches"],
        },
        "global_closed": False,
        "why_not_closed": [
            "当前账本实际下降节点全部避开 grid_fail，但正式反例族尚未证明必须落入同一相位轨道。",
            "需要把 formal counterexample family 的下降相位映射到已审计的 delta<=p-r 结构。",
        ],
        "next_atomic_target": "prove formal-family phase inequality delta<=p-r or formal-family avoids unit endpoint gate rows",
        "priority_rank": 1,
        "priority_reason": "当前有限账本支持该路线，且没有被内禀负载障碍直接证伪。",
    }


def route_endpoint_pdec(seam: dict[str, Any]) -> dict[str, Any]:
    """构造 endpoint-PDEC 路线审计。"""
    pdec_values = []
    for row in seam["seam_phase_rows"]:
        packet = row["pdec_support_packet"]
        pdec_values.append(
            packet["candidate_L_PDEC_per_unit_mass_template_norm"]["decimal_value"]
        )
    return {
        "route_id": "B_endpoint_PDEC",
        "current_status": "support_and_test_function_materialized_upper_bound_missing",
        "current_inputs": {
            "pdec_support_rows": seam["summary"]["pdec_support_rows_with_fourier_packet"],
            "seam_phase_rows": seam["summary"]["seam_phase_row_count"],
            "endpoint_unit_phases": seam["summary"]["endpoint_rough_phase_count"],
            "L_PDEC_per_unit_mass_min": min(pdec_values),
            "L_PDEC_per_unit_mass_max": max(pdec_values),
        },
        "global_closed": False,
        "why_not_closed": [
            "PDEC 支持集、测试函数和 Fourier 支持已材料化。",
            "尚未给出同一正式坏窗族上的 admissible CRT upper bound U_CRT。",
            "缺少 A,b,E,e 结构约束来源，不能套用 PDEC 模板直接闭合。",
        ],
        "next_atomic_target": "derive admissible U_CRT upper bound for the same unit endpoint bad-window family",
        "priority_rank": 2,
        "priority_reason": "输入已规范化，但核心上界仍是全新不等式。",
    }


def route_columncrt(
    gate: dict[str, Any], obstruction: dict[str, Any]
) -> dict[str, Any]:
    """构造 ColumnCRTDefect 路线审计。"""
    gate_summary = gate["summary"]
    obstruction_summary = obstruction["summary"]
    return {
        "route_id": "C_columnCRT_defect_exclusion",
        "current_status": "routes_to_defect_threshold_tuning_obstructed",
        "current_inputs": {
            "gate_rows": gate_summary["gate_row_count"],
            "unit_endpoint_phases": gate_summary["unit_endpoint_phase_count"],
            "rows_with_nonzero_displacement": gate_summary[
                "rows_with_nonzero_displacement"
            ],
            "max_intrinsic_single_residue_load": obstruction_summary[
                "max_intrinsic_single_residue_load"
            ],
            "rows_exceeding_tested_L_D": obstruction_summary[
                "rows_exceeding_tested_L_D"
            ],
            "phases_exceeding_tested_L_D": obstruction_summary[
                "phases_exceeding_tested_L_D"
            ],
        },
        "global_closed": False,
        "why_not_closed": [
            "固定非零位移入口已闭合。",
            "但同一 gate 的 unit residues 已全部落在同一 (p,d) 类，内禀负载随 prod_{ell<r}(ell-1) 增长。",
            "调小 L_D 只会触发 ColumnCRTDefect，不能排除它。",
        ],
        "next_atomic_target": "prove an independent ColumnCRTDefect exclusion theorem, not a smaller L_D threshold",
        "priority_rank": 3,
        "priority_reason": "该路线已转成独立大定理，短期不能靠现有账本闭合。",
    }


def build(
    lower_grid_path: Path,
    seam_path: Path,
    gate_path: Path,
    obstruction_path: Path,
) -> dict[str, Any]:
    """构造三路线统一审计。"""
    lower_grid = load_json(lower_grid_path)
    seam = load_json(seam_path)
    gate = load_json(gate_path)
    obstruction = load_json(obstruction_path)
    routes = [
        route_formal_avoidance(lower_grid),
        route_endpoint_pdec(seam),
        route_columncrt(gate, obstruction),
    ]
    return {
        "status": "rpz_three_route_closure_audit",
        "sources": {
            "lower_grid": str(lower_grid_path),
            "seam": str(seam_path),
            "unit_gate": str(gate_path),
            "columncrt_obstruction": str(obstruction_path),
        },
        "summary": {
            "route_count": len(routes),
            "closed_routes": sum(1 for route in routes if route["global_closed"]),
            "recommended_first_route": min(
                routes, key=lambda route: route["priority_rank"]
            )["route_id"],
            "hard_boundary": "none_closed_yet",
        },
        "routes": routes,
        "review_boundary": [
            "三条路线已同口径比较，但没有任何一条达到全局无条件闭合。",
            "当前最优先继续攻击 formal-family avoidance。",
            "endpoint-PDEC 与 ColumnCRTDefect 可并行保留，但不能替代 formal-family 缺口。",
        ],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 审计报告。"""
    summary = result["summary"]
    lines = [
        "# RPZ 三路线闭合审计",
        "",
        "**状态：** `rpz_three_route_closure_audit`",
        "",
        "## 总结",
        "",
        f"- 路线数：`{summary['route_count']}`。",
        f"- 已全局闭合路线数：`{summary['closed_routes']}`。",
        f"- 当前推荐优先路线：`{summary['recommended_first_route']}`。",
        f"- 硬边界：`{summary['hard_boundary']}`。",
        "",
        "## 三路线表",
        "",
        "| rank | route | status | next atomic target |",
        "|---:|---|---|---|",
    ]
    for route in sorted(result["routes"], key=lambda item: item["priority_rank"]):
        lines.append(
            "| {rank} | `{route}` | `{status}` | {target} |".format(
                rank=route["priority_rank"],
                route=route["route_id"],
                status=route["current_status"],
                target=route["next_atomic_target"],
            )
        )

    lines.extend(
        [
            "",
            "## 路线 A：formal-family avoidance",
            "",
            "当前有限下降账本中，`20` 个实际转换节点全部避开 `grid_fail`，闭式判据无计数或相位不一致。这说明避开路线与已有证据一致。未闭合点是：还没有证明正式反例族必须落入这些已审计相位轨道，或必须满足 `delta<=p-r`。",
            "",
            "因此路线 A 的最小目标是：证明 formal-family 的下降相位不命中 unit endpoint gate rows，或直接证明其每步满足 `delta<=p-r`。",
            "",
            "## 路线 B：endpoint-PDEC",
            "",
            "PDEC 输入已经具备：`12` 条单余类支持行、测试函数 `F=1_rho-1/r`、Fourier 支持频率。缺口是同一正式坏窗族上的 `U_CRT` 上界与合法线性约束来源。该路线可并行推进，但当前不能闭合。",
            "",
            "## 路线 C：ColumnCRTDefect",
            "",
            "固定非零位移入口已经具备；但阈值障碍证书显示，调小 `L_D` 只会触发 `ColumnCRTDefect`，不是排除。该路线必须升级为独立 `ColumnCRTDefect` 排斥定理，短期不应作为最快闭合路线。",
            "",
            "## 执行结论",
            "",
            "三选一并进后，当前应优先攻路线 A。路线 B 保留为备选上界路线；路线 C 已被压成独立深定理，不再尝试靠阈值调参闭合。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--lower-grid",
        type=Path,
        default=Path(
            "docs/monograph/prime-matrix-rpz-lower-grid-fail-avoidance-certificate.json"
        ),
    )
    parser.add_argument(
        "--seam",
        type=Path,
        default=Path("docs/monograph/prime-matrix-rpz-first-grid-fail-seam-certificate.json"),
    )
    parser.add_argument(
        "--gate",
        type=Path,
        default=Path("docs/monograph/prime-matrix-rpz-unit-endpoint-columncrt-gate.json"),
    )
    parser.add_argument(
        "--obstruction",
        type=Path,
        default=Path("docs/monograph/prime-matrix-rpz-columncrt-threshold-obstruction.json"),
    )
    parser.add_argument(
        "--out-prefix",
        type=Path,
        default=Path("docs/monograph/prime-matrix-rpz-three-route-closure-audit"),
    )
    args = parser.parse_args()
    result = build(args.lower_grid, args.seam, args.gate, args.obstruction)
    args.out_prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.out_prefix.with_suffix(".md"))
    print(json.dumps(result["summary"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
