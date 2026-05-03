#!/usr/bin/env python3
"""生成 RPZ first-grid-fail seam 标准形证书。

用法示例：
  python3 experiments/prime_matrix_rpz_first_grid_fail_seam_certificate.py

若相邻下降 `p -> r` 在 `p` 行号 `a` 处发生首个 grid_fail，令 `g=p-r` 且

  delta = -(a-1)g mod r。

grid_fail 等价于 `g < delta < r`。此时 `p` 行不是未结构化坏窗，而是跨相邻两条
`r` 行的双帽 seam：

- 前一条 `r` 行的右帽长度为 `delta`；
- 下一条 `r` 行的左帽长度为 `r+g-delta`；
- 两侧缺口长度分别为 `r-delta` 与 `delta-g`，总缺口恒为 `r-g`；
- `r`-筛幸存者至多为右端点 `ap`。

该脚本材料化这些 seam 相位行，供后续 `PDEC/ColumnCRT` 证书使用。
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def inverse_mod(value: int, modulus: int) -> int:
    """返回模素数 `modulus` 下的乘法逆元。"""
    return pow(value % modulus, -1, modulus)


def residue_for_delta(p: int, r: int, delta: int) -> int:
    """由 `delta=-(a-1)(p-r) mod r` 反解 `a mod r`。"""
    gap = p - r
    return (1 - delta * inverse_mod(gap, r)) % r


def seam_row(p: int, r: int, delta: int, modulus: int) -> dict[str, Any]:
    """生成单个 seam 相位行。"""
    gap = p - r
    row_residue = residue_for_delta(p, r, delta)
    left_cap_length = delta
    right_cap_length = r + gap - delta
    left_missing_length = r - delta
    right_missing_length = delta - gap
    return {
        "p": p,
        "r": r,
        "gap": gap,
        "Q": modulus,
        "delta": delta,
        "row_residue_mod_r": row_residue,
        "full_phase_cardinality_in_Q": modulus // r,
        "left_cap_length": left_cap_length,
        "right_cap_length": right_cap_length,
        "total_seam_length": left_cap_length + right_cap_length,
        "left_missing_length": left_missing_length,
        "right_missing_length": right_missing_length,
        "missing_mass": left_missing_length + right_missing_length,
        "missing_mass_expected": r - gap,
        "endpoint_survivor_position": "right_endpoint_ap_only",
        "pdec_support_description": (
            "row phases a mod Q with a mod r equal to row_residue_mod_r"
        ),
        "columncrt_hook": [
            "right endpoint ap is the only possible r-rough survivor",
            "persistent seam fixes delta and adjacent lower-row cap lengths",
            "any repeated endpoint/label displacement should enter ColumnCRT",
        ],
    }


def build(source_path: Path) -> dict[str, Any]:
    """构造 first-grid-fail seam 证书。"""
    source = json.loads(source_path.read_text(encoding="utf-8"))
    seam_rows = []
    transition_rows = []
    for item in source["transition_summaries"]:
        p = item["p"]
        r = item["r"]
        gap = p - r
        modulus = item["phase_modulus_primorial_r"]
        deltas = list(range(gap + 1, r))
        rows = [seam_row(p, r, delta, modulus) for delta in deltas]
        seam_rows.extend(rows)
        transition_rows.append(
            {
                "p": p,
                "r": r,
                "gap": gap,
                "Q": modulus,
                "grid_fail_delta_count": len(deltas),
                "grid_fail_deltas": deltas,
                "grid_fail_residues_mod_r": [
                    row["row_residue_mod_r"] for row in rows
                ],
                "full_Q_grid_fail_cardinality": sum(
                    row["full_phase_cardinality_in_Q"] for row in rows
                ),
                "source_grid_fail_count": item["counts"].get("grid_fail", 0),
                "count_matches_source": sum(
                    row["full_phase_cardinality_in_Q"] for row in rows
                )
                == item["counts"].get("grid_fail", 0),
            }
        )

    return {
        "status": "rpz_first_grid_fail_seam_normal_form_certificate",
        "source": str(source_path),
        "summary": {
            "transition_count": len(transition_rows),
            "transitions_with_grid_fail": sum(
                1 for row in transition_rows if row["grid_fail_delta_count"] > 0
            ),
            "seam_phase_row_count": len(seam_rows),
            "full_Q_grid_fail_cardinality": sum(
                row["full_phase_cardinality_in_Q"] for row in seam_rows
            ),
            "count_mismatches": sum(
                1 for row in transition_rows if not row["count_matches_source"]
            ),
        },
        "transition_rows": transition_rows,
        "seam_phase_rows": seam_rows,
        "review_boundary": [
            "first-grid-fail 已压成双帽 seam 标准形",
            "该证书不排除 seam 相位",
            "后续仍需 PDEC/ColumnCRT 排斥或全局相位避开证明",
        ],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 证书报告。"""
    summary = result["summary"]
    lines = [
        "# RPZ First-Grid-Fail Seam 标准形证书",
        "",
        "**状态：** `rpz_first_grid_fail_seam_normal_form_certificate`",
        "",
        "## 标准形",
        "",
        "设 `g=p-r`，`delta=-(a-1)g mod r`。首个 `grid_fail` 当且仅当 `g<delta<r`。此时 `p` 行跨相邻两条 `r` 行：",
        "",
        "```text",
        "left cap length  = delta；",
        "right cap length = r+g-delta；",
        "left missing     = r-delta；",
        "right missing    = delta-g；",
        "missing mass     = r-g。",
        "```",
        "",
        "该 seam 内的 `r`-筛幸存者至多为右端点 `ap`。",
        "",
        "## 总结",
        "",
        f"- 转换数：`{summary['transition_count']}`。",
        f"- 含 grid_fail 的转换数：`{summary['transitions_with_grid_fail']}`。",
        f"- seam 相位行数：`{summary['seam_phase_row_count']}`。",
        f"- 完整 `Q` 中 grid_fail 相位基数：`{summary['full_Q_grid_fail_cardinality']}`。",
        f"- 与源账本计数不一致数：`{summary['count_mismatches']}`。",
        "",
        "## 转换表",
        "",
        "| p | r | Q | gap | fail deltas | fail residues mod r | source fail count | count ok |",
        "|---:|---:|---:|---:|---|---|---:|---|",
    ]
    for row in result["transition_rows"]:
        lines.append(
            "| {p} | {r} | {Q} | {gap} | `{deltas}` | `{residues}` | {count} | {ok} |".format(
                p=row["p"],
                r=row["r"],
                Q=row["Q"],
                gap=row["gap"],
                deltas=row["grid_fail_deltas"],
                residues=row["grid_fail_residues_mod_r"],
                count=row["source_grid_fail_count"],
                ok="yes" if row["count_matches_source"] else "no",
            )
        )

    lines.extend(
        [
            "",
            "## 证书意义",
            "",
            "first-grid-fail seam 不是任意坏窗。它具有固定双帽结构、固定缺口守恒 `r-g`，且最多只有右端点 `ap` 一个 `r`-rough 幸存者。持久出现时，相位 `delta` 和行号余类 `a mod r` 被固定，适合进入 `PDEC`；若右端点幸存者携带稳定列位移或吸收标签，则进入 `ColumnCRT`。",
            "",
            "本证书只完成标准形抽取，不排除这些 seam 相位。下一步需要提交 `PDEC/ColumnCRT` 排斥证书，或证明正式反例族不能命中这些 seam 相位。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source",
        type=Path,
        default=Path(
            "docs/monograph/prime-matrix-rpz-lower-descent-obstruction-ledger.json"
        ),
    )
    parser.add_argument(
        "--out-prefix",
        type=Path,
        default=Path("docs/monograph/prime-matrix-rpz-first-grid-fail-seam-certificate"),
    )
    args = parser.parse_args()
    result = build(args.source)
    args.out_prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.out_prefix.with_suffix(".md"))
    print(json.dumps(result["summary"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
