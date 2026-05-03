#!/usr/bin/env python3
"""审计 RPZ unit endpoint 的 ColumnCRT 阈值硬障碍。

用法示例：
  python3 experiments/prime_matrix_rpz_columncrt_threshold_obstruction.py

前一步已经证明 unit endpoint seam 会路由到固定非零 `ColumnCRT` 位移余类。
本脚本继续检查：能否仅靠给定阈值 `L_D` 排除这些门控行。

结论是一个负面但严格的审稿事实：在每条 unit gate 中，全部 unit 端点相位已经落在同一
`(label=p, displacement=d mod p)` 负载类。因此任何不依赖额外结构的阈值都至少要达到
该 unit support size；否则当前相位支持本身就超过阈值，只能登记为 ColumnCRTDefect，
不能被排除。
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any


def asymptotic_unit_formula(r: int) -> int:
    """返回固定 `a mod r` 非零类中的 `Q`-unit 数量。"""
    result = 1
    for value in range(2, r):
        if all(value % divisor for divisor in range(2, int(math.sqrt(value)) + 1)):
            result *= value - 1
    return result


def build(gate_path: Path, displacement_threshold: int) -> dict[str, Any]:
    """构造 ColumnCRT 阈值障碍审计。"""
    gate = json.loads(gate_path.read_text(encoding="utf-8"))
    rows = []
    for row in gate["gate_rows"]:
        unit_load = row["unit_endpoint_support_size"]
        minimal_threshold = unit_load
        threshold_passes_without_new_input = displacement_threshold >= minimal_threshold
        rows.append(
            {
                "p": row["p"],
                "r": row["r"],
                "delta": row["delta"],
                "rho": row["row_residue_mod_r"],
                "label": row["columncrt_label"],
                "displacement_mod_label": row["columncrt_displacement_mod_p"],
                "unit_endpoint_load": unit_load,
                "unit_load_formula_for_r": "prod_{ell<r}(ell-1)",
                "unit_load_formula_value": asymptotic_unit_formula(row["r"]),
                "minimal_L_D_to_avoid_declaring_this_gate_a_defect": minimal_threshold,
                "tested_L_D": displacement_threshold,
                "tested_threshold_passes_without_new_input": threshold_passes_without_new_input,
                "verdict": (
                    "threshold_large_enough_but_no_exclusion"
                    if threshold_passes_without_new_input
                    else "tested_threshold_forces_ColumnCRTDefect_not_exclusion"
                ),
            }
        )

    failing_rows = [
        row for row in rows if not row["tested_threshold_passes_without_new_input"]
    ]
    return {
        "status": "rpz_columncrt_threshold_obstruction_certificate",
        "source": str(gate_path),
        "tested_displacement_threshold_L_D": displacement_threshold,
        "summary": {
            "gate_row_count": len(rows),
            "unit_endpoint_phase_count": sum(row["unit_endpoint_load"] for row in rows),
            "max_intrinsic_single_residue_load": max(
                row["unit_endpoint_load"] for row in rows
            ),
            "rows_exceeding_tested_L_D": len(failing_rows),
            "phases_exceeding_tested_L_D": sum(
                row["unit_endpoint_load"] for row in failing_rows
            ),
            "all_rows_have_formula_match": all(
                row["unit_endpoint_load"] == row["unit_load_formula_value"]
                for row in rows
            ),
        },
        "rows": rows,
        "obstruction_theorem": [
            "固定 unit endpoint gate 中，label=p 与 displacement=d mod p 对全部 unit residues 相同。",
            "因此 ColumnCRT 负载 R_{p,d} 至少等于该 gate 的 unit endpoint support size。",
            "若 L_D 小于该 support size，结论只能是进入 ColumnCRTDefect，而不是排除 gate。",
            "由于 support size=prod_{ell<r}(ell-1) 随 r 无界增长，不存在固定小 L_D 可全局排除 unit endpoint seam。",
        ],
        "remaining_valid_routes": [
            "证明正式反例族避开 unit endpoint gate rows",
            "提交 endpoint-PDEC 的 U_CRT<L_PDEC 上界",
            "给出独立 ColumnCRTDefect 排斥定理，而不是仅调小 L_D",
        ],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 审计报告。"""
    summary = result["summary"]
    threshold = result["tested_displacement_threshold_L_D"]
    lines = [
        "# RPZ ColumnCRT 阈值硬障碍审计",
        "",
        "**状态：** `rpz_columncrt_threshold_obstruction_certificate`",
        "",
        "## 结论",
        "",
        "固定非零 ColumnCRT 位移门控本身不是排斥定理。对每条 unit endpoint gate，全部 unit residues 已经落在同一个 `(label=p, displacement=d mod p)` 类中，所以该类的内禀负载等于 unit support size。",
        "",
        "因此：若阈值 `L_D` 小于这个 support size，得到的是 `ColumnCRTDefect` 被触发，而不是矛盾；若阈值 `L_D` 至少等于这个 support size，又不能排除该 gate。单靠阈值调参无法闭合全局命题。",
        "",
        "## 总结",
        "",
        f"- 测试阈值 `L_D`：`{threshold}`。",
        f"- 门控行数：`{summary['gate_row_count']}`。",
        f"- unit endpoint 相位总数：`{summary['unit_endpoint_phase_count']}`。",
        f"- 最大单个位移类内禀负载：`{summary['max_intrinsic_single_residue_load']}`。",
        f"- 超过测试阈值的行数：`{summary['rows_exceeding_tested_L_D']}`。",
        f"- 超过测试阈值的相位数：`{summary['phases_exceeding_tested_L_D']}`。",
        f"- `prod_(ell<r)(ell-1)` 公式逐行匹配：`{summary['all_rows_have_formula_match']}`。",
        "",
        "## 阈值表",
        "",
        "| p | r | delta | label | d mod label | unit load | min L_D | tested verdict |",
        "|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for row in result["rows"]:
        lines.append(
            "| {p} | {r} | {delta} | {label} | {disp} | {load} | {min_ld} | `{verdict}` |".format(
                p=row["p"],
                r=row["r"],
                delta=row["delta"],
                label=row["label"],
                disp=row["displacement_mod_label"],
                load=row["unit_endpoint_load"],
                min_ld=row["minimal_L_D_to_avoid_declaring_this_gate_a_defect"],
                verdict=row["verdict"],
            )
        )

    lines.extend(
        [
            "",
            "## 审稿定理",
            "",
            "**Theorem RPZ-CCRT-OB（ColumnCRT 阈值障碍）。** 固定相邻下降 `p->r` 的 unit endpoint gate。若 `a` 遍历该 gate 的 `Q`-unit 支持，则端点标签恒为 `p`，同列见证位移余类恒为同一个非零 `d mod p`。于是",
            "",
            "```text",
            "R_{p,d} >= # {a mod Q: a≡rho mod r, gcd(a,Q)=1}",
            "        = prod_{ell<r}(ell-1).",
            "```",
            "",
            "所以任何 `L_D < prod_{ell<r}(ell-1)` 的阈值只会把该 gate 登记为 `ColumnCRTDefect`，不能排除它；而取更大的 `L_D` 又失去排斥力。",
            "",
            "## 剩余合法路线",
            "",
            "1. 证明正式反例族避开 unit endpoint gate rows；",
            "2. 提交 endpoint-PDEC 的 `U_CRT<L_PDEC` 上界；",
            "3. 给出独立的 `ColumnCRTDefect` 排斥定理。仅调小 `L_D` 不是有效闭合方案。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--gate",
        type=Path,
        default=Path("docs/monograph/prime-matrix-rpz-unit-endpoint-columncrt-gate.json"),
    )
    parser.add_argument("--displacement-threshold", type=int, default=2)
    parser.add_argument(
        "--out-prefix",
        type=Path,
        default=Path("docs/monograph/prime-matrix-rpz-columncrt-threshold-obstruction"),
    )
    args = parser.parse_args()
    result = build(args.gate, args.displacement_threshold)
    args.out_prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.out_prefix.with_suffix(".md"))
    print(json.dumps(result["summary"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
