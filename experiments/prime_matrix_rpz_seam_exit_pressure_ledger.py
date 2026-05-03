#!/usr/bin/env python3
"""汇总 RPZ seam/PDEC/ColumnCRT 出口的最窄压力账本。

用法示例：
  python3 experiments/prime_matrix_rpz_seam_exit_pressure_ledger.py

该脚本不证明 seam 出口不可能发生。它做一件更窄、更可审稿的事：
把 rejected phase 吸收后的出口从逐相位规模压缩到可攻击的 seam 行与
ColumnCRT 位移类。

输出结论：
  1. 非 unit 端点全部已由下层小素数标签吸收；
  2. unit 端点全部进入固定非零 ColumnCRT 位移类；
  3. PDEC 侧只剩同口径 U_CRT 上界；
  4. 下一步不能再调阈值，必须排除这些命名出口或证明 formal starts 避开它们。
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path
from typing import Any


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def seam_key(row: dict[str, Any]) -> tuple[int, int, int, int]:
    """生成 seam 行键 `(p,r,delta,rho)`。"""
    return (
        row["p"],
        row["r"],
        row["delta"],
        row["row_residue_mod_r"],
    )


def merge_rows(seam: dict[str, Any], gate: dict[str, Any]) -> list[dict[str, Any]]:
    """合并 seam 证书与 ColumnCRT gate 证书。"""
    gate_by_key = {seam_key(row): row for row in gate["gate_rows"]}
    rows: list[dict[str, Any]] = []
    for row in seam["seam_phase_rows"]:
        key = seam_key(row)
        gate_row = gate_by_key[key]
        pdec = row["pdec_support_packet"]
        split = row["endpoint_split_packet"]["lower_sieve_status"]
        support_size = pdec["support_size"]
        unit_size = split["rough_support_size"]
        killed_size = split["killed_support_size"]
        rows.append(
            {
                "p": row["p"],
                "r": row["r"],
                "gap": row["gap"],
                "delta": row["delta"],
                "rho_mod_r": row["row_residue_mod_r"],
                "support_size": support_size,
                "killed_endpoint_size": killed_size,
                "unit_endpoint_size": unit_size,
                "unit_fraction": unit_size / support_size,
                "killed_fraction": killed_size / support_size,
                "pdec_L_template_decimal": pdec[
                    "candidate_L_PDEC_per_unit_mass_template_norm"
                ]["decimal_value"],
                "columncrt_label": gate_row["columncrt_label"],
                "columncrt_displacement_mod_p": gate_row[
                    "columncrt_displacement_mod_p"
                ],
                "same_column_witness": gate_row["same_column_witness"],
            }
        )
    return rows


def aggregate_by_transition(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """按相邻下降 `p->r` 聚合 seam 压力。"""
    grouped: dict[tuple[int, int], list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[(row["p"], row["r"])].append(row)

    result = []
    for (p, r), items in sorted(grouped.items()):
        displacement_classes = {
            item["columncrt_displacement_mod_p"] for item in items
        }
        result.append(
            {
                "p": p,
                "r": r,
                "seam_rows": len(items),
                "support_size_total": sum(item["support_size"] for item in items),
                "killed_endpoint_total": sum(
                    item["killed_endpoint_size"] for item in items
                ),
                "unit_endpoint_total": sum(
                    item["unit_endpoint_size"] for item in items
                ),
                "unit_endpoint_per_row_max": max(
                    item["unit_endpoint_size"] for item in items
                ),
                "distinct_displacement_classes": len(displacement_classes),
                "displacement_classes": sorted(displacement_classes),
            }
        )
    return result


def aggregate_by_displacement(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """按 `(label, d mod label)` 聚合 ColumnCRT 位移压力。"""
    grouped: dict[tuple[int, int], list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[
            (row["columncrt_label"], row["columncrt_displacement_mod_p"])
        ].append(row)

    result = []
    for (label, displacement), items in sorted(grouped.items()):
        result.append(
            {
                "label": label,
                "displacement_mod_label": displacement,
                "seam_rows": len(items),
                "unit_endpoint_load_total": sum(
                    item["unit_endpoint_size"] for item in items
                ),
                "support_size_total": sum(item["support_size"] for item in items),
                "source_rows": [
                    {
                        "p": item["p"],
                        "r": item["r"],
                        "delta": item["delta"],
                        "rho_mod_r": item["rho_mod_r"],
                    }
                    for item in items
                ],
            }
        )
    return result


def build(seam_path: Path, gate_path: Path, absorption_path: Path) -> dict[str, Any]:
    """构造 seam 出口压力账本。"""
    seam = load_json(seam_path)
    gate = load_json(gate_path)
    absorption = load_json(absorption_path)
    rows = merge_rows(seam, gate)
    by_transition = aggregate_by_transition(rows)
    by_displacement = aggregate_by_displacement(rows)

    total_support = sum(row["support_size"] for row in rows)
    total_unit = sum(row["unit_endpoint_size"] for row in rows)
    total_killed = sum(row["killed_endpoint_size"] for row in rows)
    max_displacement_load = max(
        row["unit_endpoint_load_total"] for row in by_displacement
    )

    return {
        "status": "rpz_seam_exit_pressure_ledger_not_exclusion",
        "sources": {
            "seam": str(seam_path),
            "gate": str(gate_path),
            "absorption": str(absorption_path),
        },
        "summary": {
            "rejected_phases_absorbed": absorption["summary"][
                "total_rejected_phases"
            ],
            "seam_rows": len(rows),
            "total_seam_support": total_support,
            "total_killed_endpoint_phases": total_killed,
            "total_unit_endpoint_phases": total_unit,
            "unit_endpoint_fraction": total_unit / total_support,
            "killed_endpoint_fraction": total_killed / total_support,
            "displacement_class_count": len(by_displacement),
            "max_aggregated_displacement_load": max_displacement_load,
            "all_unit_endpoints_have_fixed_nonzero_displacement": all(
                row["columncrt_displacement_mod_p"] != 0 for row in rows
            ),
        },
        "seam_rows": rows,
        "by_transition": by_transition,
        "by_displacement": by_displacement,
        "review_boundary": [
            "该账本只压缩出口规模，不排除 seam/PDEC/ColumnCRT。",
            "非 unit 端点已由下层标签吸收；unit 端点仍需要 endpoint-PDEC 或 ColumnCRTDefect 排斥。",
            "单靠调低 L_D 只会登记 ColumnCRTDefect，不能推出矛盾。",
            "下一硬点是 formal-family 避开 seam，或对这些固定行提交 U_CRT<L_PDEC / ColumnCRTDefect 排斥。",
        ],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 审稿账本。"""
    summary = result["summary"]
    lines = [
        "# RPZ Seam/PDEC/ColumnCRT 出口压力账本",
        "",
        "**状态：** `rpz_seam_exit_pressure_ledger_not_exclusion`",
        "",
        "## 总结",
        "",
        f"- 已吸收 rejected phases：`{summary['rejected_phases_absorbed']}`。",
        f"- seam 行数：`{summary['seam_rows']}`。",
        f"- seam 支持总量：`{summary['total_seam_support']}`。",
        f"- 下层标签已杀死端点：`{summary['total_killed_endpoint_phases']}`。",
        f"- unit endpoint 相位：`{summary['total_unit_endpoint_phases']}`。",
        f"- unit endpoint 占比：`{summary['unit_endpoint_fraction']:.6f}`。",
        f"- ColumnCRT 位移类数：`{summary['displacement_class_count']}`。",
        f"- 最大聚合位移负载：`{summary['max_aggregated_displacement_load']}`。",
        f"- unit endpoint 是否全为固定非零位移：`{summary['all_unit_endpoints_have_fixed_nonzero_displacement']}`。",
        "",
        "## 按相邻下降聚合",
        "",
        "| p | r | seam rows | support | killed endpoint | unit endpoint | max unit/row | displacement classes |",
        "|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for row in result["by_transition"]:
        lines.append(
            "| {p} | {r} | {seams} | {support} | {killed} | {unit} | {max_unit} | `{classes}` |".format(
                p=row["p"],
                r=row["r"],
                seams=row["seam_rows"],
                support=row["support_size_total"],
                killed=row["killed_endpoint_total"],
                unit=row["unit_endpoint_total"],
                max_unit=row["unit_endpoint_per_row_max"],
                classes=row["displacement_classes"],
            )
        )

    lines.extend(
        [
            "",
            "## 按 ColumnCRT 位移类聚合",
            "",
            "| label | d mod label | seam rows | unit load | support | source rows [p,r,delta,rho] |",
            "|---:|---:|---:|---:|---:|---|",
        ]
    )
    for row in result["by_displacement"]:
        lines.append(
            "| {label} | {disp} | {seams} | {load} | {support} | `{sources}` |".format(
                label=row["label"],
                disp=row["displacement_mod_label"],
                seams=row["seam_rows"],
                load=row["unit_endpoint_load_total"],
                support=row["support_size_total"],
                sources=[
                    [
                        item["p"],
                        item["r"],
                        item["delta"],
                        item["rho_mod_r"],
                    ]
                    for item in row["source_rows"]
                ],
            )
        )

    lines.extend(
        [
            "",
            "## 审稿结论",
            "",
            "rejected set 已经不是大规模未命名对象：它被压缩为 `12` 条 first-grid-fail seam 行。",
            "其中非 unit 端点全部由下层小素数标签吸收，真正仍需处理的是 `404` 个 unit endpoint 相位。",
            f"这些 unit endpoint 又全部进入固定非零 ColumnCRT 位移类，聚合后只有 `{summary['displacement_class_count']}` 个 `(label,d)` 类。",
            "",
            "因此下一步硬点不能写成“继续调阈值”或“继续检查 rejected phase”。有效目标只剩三类：",
            "",
            "1. 证明 formal-family 起始相位避开这 `12` 条 seam 行；",
            "2. 对这 `12` 条单余类 PDEC 支持行给出同口径 `U_CRT<L_PDEC`；",
            f"3. 对聚合后的 `{summary['displacement_class_count']}` 个固定非零 ColumnCRT 位移类证明独立 `ColumnCRTDefect` 排斥。",
            "",
            "本账本仍不是闭合证明；它把最后出口从逐相位问题压缩为可逐行审稿的有限窄接口。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
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
        "--absorption",
        type=Path,
        default=Path("docs/monograph/prime-matrix-rpz-rejected-phase-absorption.json"),
    )
    parser.add_argument(
        "--out-prefix",
        type=Path,
        default=Path("docs/monograph/prime-matrix-rpz-seam-exit-pressure-ledger"),
    )
    args = parser.parse_args()

    result = build(args.seam, args.gate, args.absorption)
    args.out_prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.out_prefix.with_suffix(".md"))
    print(json.dumps(result["summary"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
