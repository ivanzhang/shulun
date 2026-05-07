#!/usr/bin/env python3
"""审计 FO-PDEC 跨 q 复用是否只是同一物理候选的坐标图重叠。

用法示例：
  python3 experiments/prime_matrix_wsh_fo_pdec_cross_q_chart_overlap_audit.py

输出：
  docs/monograph/prime-matrix-wsh-fo-pdec-cross-q-chart-overlap-audit.json
  docs/monograph/prime-matrix-wsh-fo-pdec-cross-q-chart-overlap-audit.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from itertools import combinations
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_STITCHING = DOCS / "prime-matrix-wsh-fo-pdec-stitching-feasibility-audit.json"
DEFAULT_LOWMOD = DOCS / "prime-matrix-wsh-fo-pdec-lowmod-audit.json"
DEFAULT_JSON = DOCS / "prime-matrix-wsh-fo-pdec-cross-q-chart-overlap-audit.json"
DEFAULT_MD = DOCS / "prime-matrix-wsh-fo-pdec-cross-q-chart-overlap-audit.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def lowmod_key(row: dict[str, Any]) -> tuple[Any, ...]:
    """生成低模方程唯一键。"""
    return (
        row["q"],
        row["source_row"],
        row["candidate_row"],
        row["column"],
        row["offset"],
        row["candidate"],
        row["explaining_factor"],
        row["target_residue"],
    )


def source_key(row: dict[str, Any]) -> tuple[Any, ...]:
    """生成 stitching source 对应的低模方程键。"""
    return (
        row["q"],
        row["source_row"],
        row["candidate_row"],
        row["column"],
        row["offset"],
        row["candidate"],
        row["factor"],
        row["target_residue"],
    )


def enrich_source(
    source: dict[str, Any],
    lowmod_by_key: dict[tuple[Any, ...], dict[str, Any]],
) -> dict[str, Any]:
    """补充 source 的物理坐标字段。"""
    lowmod = lowmod_by_key[source_key(source)]
    q = int(source["q"])
    row = int(source["candidate_row"])
    column = int(source["column"])
    base = (row - 1) * q
    candidate = int(source["candidate"])
    return {
        **source,
        "semiprime": lowmod["semiprime"],
        "tail_factors": lowmod["tail_factors"],
        "row_base": base,
        "row_interval": [base + 1, base + q],
        "row_coordinate_identity_ok": base + column == candidate,
    }


def interval_overlap(first: list[int], second: list[int]) -> int:
    """计算两个闭区间重叠长度。"""
    left = max(first[0], second[0])
    right = min(first[1], second[1])
    return max(0, right - left + 1)


def pair_diagnostics(first: dict[str, Any], second: dict[str, Any]) -> dict[str, Any]:
    """比较两个 q 坐标图。"""
    base_gap = int(second["row_base"]) - int(first["row_base"])
    column_gap = int(second["column"]) - int(first["column"])
    candidate_gap = int(second["candidate"]) - int(first["candidate"])
    overlap = interval_overlap(first["row_interval"], second["row_interval"])
    same_physical = (
        first["candidate"] == second["candidate"]
        and first["semiprime"] == second["semiprime"]
        and first["offset"] == second["offset"]
        and first["factor"] == second["factor"]
    )
    chart_shift_identity = base_gap + column_gap == candidate_gap == 0
    return {
        "q_pair": [first["q"], second["q"]],
        "row_pair": [first["candidate_row"], second["candidate_row"]],
        "base_pair": [first["row_base"], second["row_base"]],
        "column_pair": [first["column"], second["column"]],
        "base_gap": base_gap,
        "column_gap": column_gap,
        "candidate_gap": candidate_gap,
        "row_interval_overlap": overlap,
        "same_physical_candidate_semiprime_offset_factor": same_physical,
        "chart_shift_identity": chart_shift_identity,
        "row_residue_pair": [first["target_residue"], second["target_residue"]],
        "row_residue_changes": first["target_residue"] != second["target_residue"],
        "status": (
            "same_physical_candidate_in_overlapping_q_charts"
            if same_physical and chart_shift_identity and overlap > 0
            else "needs_case_split"
        ),
    }


def audit_reuse(
    reuse: dict[str, Any],
    lowmod_by_key: dict[tuple[Any, ...], dict[str, Any]],
) -> dict[str, Any]:
    """审计一组跨 q 复用。"""
    sources = [enrich_source(source, lowmod_by_key) for source in reuse["sources"]]
    pair_rows = [
        pair_diagnostics(first, second)
        for first, second in combinations(sources, 2)
    ]
    all_chart_overlap = all(
        pair["status"] == "same_physical_candidate_in_overlapping_q_charts"
        for pair in pair_rows
    )
    row_residues = [
        {
            "q": source["q"],
            "row": source["candidate_row"],
            "residue": source["target_residue"],
            "base": source["row_base"],
            "column": source["column"],
        }
        for source in sources
    ]
    return {
        "candidate": reuse["candidate"],
        "factor": reuse["factor"],
        "integer_factorization": reuse["integer_factorization"],
        "multiplicity": reuse["multiplicity"],
        "q_layers": reuse["q_layers"],
        "row_residues": row_residues,
        "sources": sources,
        "pair_diagnostics": pair_rows,
        "all_pairs_chart_overlap": all_chart_overlap,
        "persistence_status": (
            "blocked_as_independent_coordinate_persistence"
            if all_chart_overlap
            else "cross_q_persistence_needs_external_proof"
        ),
        "counting_rule": (
            "physical_candidate_quotient_or_explicit_persistence_theorem_required"
            if all_chart_overlap
            else "case_split_required"
        ),
    }


def build_audit(
    stitching: dict[str, Any],
    lowmod: dict[str, Any],
    stitching_path: Path,
    lowmod_path: Path,
) -> dict[str, Any]:
    """构造跨 q 图重叠审计。"""
    lowmod_by_key = {lowmod_key(row): row for row in lowmod["equations"]}
    rows = [
        audit_reuse(reuse, lowmod_by_key)
        for reuse in stitching["cross_level_reuses"]
    ]
    all_blocked = all(
        row["persistence_status"] == "blocked_as_independent_coordinate_persistence"
        for row in rows
    )
    factor_199_rows = [row for row in rows if int(row["factor"]) == 199]
    factor_199_blocked = bool(factor_199_rows) and all(
        row["persistence_status"] == "blocked_as_independent_coordinate_persistence"
        for row in factor_199_rows
    )
    return {
        "certificate_type": "fo_pdec_cross_q_chart_overlap_audit",
        "status": "cross_q_coordinate_persistence_blocked_not_global_proof",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "stitching_feasibility_audit": file_sha256(stitching_path),
            "lowmod_audit": file_sha256(lowmod_path),
        },
        "cross_level_reuse_count": len(rows),
        "all_cross_level_reuses_chart_overlap_blocked": all_blocked,
        "factor_199_cross_level_reuse_blocked": factor_199_blocked,
        "audited_reuses": rows,
        "closed_subgate": (
            "CrossQCoordinatePersistenceRejectedForAuditedFO-PDEC"
            if all_blocked
            else "CrossQPersistenceStillNeedsCaseSplit"
        ),
        "remaining_after_subgate": [
            "physical/primitive PDEC threshold U_CRT < 1.9997507790353146",
            "SAE/Endpoint absorption for physical cross-chart reuses",
            "future non-overlap cross-q persistence theorem, if a non-chart-overlap family appears",
        ],
        "review_conclusion": (
            "当前 FO-PDEC 的全部 cross-q reuses 都是同一物理候选在重叠 q-row 坐标图中的表示。"
            "两层行起点与列号满足 base_gap + column_gap = 0，候选、semiprime、offset 与解释因子相同。"
            "因此它们不能作为独立 coordinate persistence 计入同一 PDEC 下界；必须物理去重，或提交新的"
            " 非重叠 cross-q persistence theorem。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 审计报告。"""
    lines = [
        "# FO-PDEC cross-q 坐标图重叠审计",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 子门裁定",
        "",
        "```text",
        f"closed_subgate: {result['closed_subgate']}",
        f"cross_level_reuse_count: {result['cross_level_reuse_count']}",
        (
            "all_cross_level_reuses_chart_overlap_blocked: "
            f"{str(result['all_cross_level_reuses_chart_overlap_blocked']).lower()}"
        ),
        (
            "factor_199_cross_level_reuse_blocked: "
            f"{str(result['factor_199_cross_level_reuse_blocked']).lower()}"
        ),
        "```",
        "",
        "## 2. 逐复用审计",
        "",
        "| candidate | factor | q layers | residues | base gaps | column gaps | status |",
        "| ---: | ---: | --- | --- | --- | --- | --- |",
    ]
    for row in result["audited_reuses"]:
        base_gaps = [pair["base_gap"] for pair in row["pair_diagnostics"]]
        column_gaps = [pair["column_gap"] for pair in row["pair_diagnostics"]]
        residues = [
            [residue["q"], residue["residue"]]
            for residue in row["row_residues"]
        ]
        lines.append(
            "| "
            + " | ".join(
                table_cell(value)
                for value in [
                    row["candidate"],
                    row["factor"],
                    row["q_layers"],
                    residues,
                    base_gaps,
                    column_gaps,
                    row["persistence_status"],
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 3. 证明读法",
            "",
            "同一物理整数 `n` 在两个宽度为 `q_1,q_2` 的行坐标中写成",
            "",
            "\\[",
            "n=(r_1-1)q_1+c_1=(r_2-1)q_2+c_2。",
            "\\]",
            "",
            "若 `(r_2-1)q_2-(r_1-1)q_1 = -(c_2-c_1)`，则两个坐标只是同一整数的图变换。"
            "当前全部跨 `q` 复用均满足这个恒等式，并且物理候选、半素数核心、offset 与解释因子相同。",
            "",
            "所以这类复用不能同时提供两个独立 PDEC 事件。若要把它们合并成 coordinate-cap 阈值，"
            "必须额外证明非坐标图意义上的 cross-q persistence；当前样本没有这种结构。",
            "",
            "## 4. 剩余",
            "",
        ]
    )
    for item in result["remaining_after_subgate"]:
        lines.append(f"- `{item}`")
    lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stitching", type=Path, default=DEFAULT_STITCHING)
    parser.add_argument("--lowmod", type=Path, default=DEFAULT_LOWMOD)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    stitching = load_json(args.stitching)
    lowmod = load_json(args.lowmod)
    result = build_audit(stitching, lowmod, args.stitching, args.lowmod)
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(result["status"])
    print(result["closed_subgate"])


if __name__ == "__main__":
    main()
