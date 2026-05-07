#!/usr/bin/env python3
"""审计 FO-PDEC 嵌套块重复能否按单位权独立计数。

用法示例：
  python3 experiments/prime_matrix_wsh_fo_pdec_nested_duplicate_dominance_audit.py

输出：
  docs/monograph/prime-matrix-wsh-fo-pdec-nested-duplicate-dominance-audit.json
  docs/monograph/prime-matrix-wsh-fo-pdec-nested-duplicate-dominance-audit.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_STITCHING = DOCS / "prime-matrix-wsh-fo-pdec-stitching-feasibility-audit.json"
DEFAULT_JSON = DOCS / "prime-matrix-wsh-fo-pdec-nested-duplicate-dominance-audit.json"
DEFAULT_MD = DOCS / "prime-matrix-wsh-fo-pdec-nested-duplicate-dominance-audit.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算文件 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def support_relation(geometries: list[dict[str, Any]]) -> dict[str, Any]:
    """判断两个嵌套 Hall 块的半素数支撑是否包含。"""
    if len(geometries) < 2:
        return {
            "nested": False,
            "relation": "insufficient_block_geometry",
            "sizes": [],
        }

    supports = [set(map(int, geom["semiprime_values"])) for geom in geometries]
    sizes = [len(support) for support in supports]
    first_subset_second = supports[0] <= supports[1]
    second_subset_first = supports[1] <= supports[0]
    if first_subset_second and second_subset_first:
        relation = "equal_support"
    elif first_subset_second:
        relation = "block_1_support_subset_block_2_support"
    elif second_subset_first:
        relation = "block_2_support_subset_block_1_support"
    else:
        relation = "not_nested"
    return {
        "nested": first_subset_second or second_subset_first,
        "relation": relation,
        "sizes": sizes,
        "surpluses": [geom.get("surplus") for geom in geometries],
    }


def audit_duplicate(row: dict[str, Any]) -> dict[str, Any]:
    """审计一条 exact nested duplicate。"""
    relation = support_relation(row.get("block_geometry", []))
    same_coordinate = bool(row.get("same_formal_coordinate"))
    unit_weight_independence_blocked = same_coordinate and relation["nested"]
    return {
        "key": row["key"],
        "block_ids": row["block_ids"],
        "multiplicity": row["multiplicity"],
        "same_formal_coordinate": same_coordinate,
        "support_relation": relation,
        "unit_weight_independence_status": (
            "blocked_by_same_coordinate_nested_support"
            if unit_weight_independence_blocked
            else "not_blocked_by_this_audit"
        ),
        "counting_rule": (
            "coordinate_quotient_or_fractional_weighted_dual_required"
            if unit_weight_independence_blocked
            else "separate_independence_proof_required"
        ),
        "sources": row.get("sources", []),
    }


def build_audit(stitching: dict[str, Any], stitching_path: Path) -> dict[str, Any]:
    """构造嵌套重复支配审计。"""
    duplicates = [audit_duplicate(row) for row in stitching["exact_nested_duplicates"]]
    all_blocked = all(
        row["unit_weight_independence_status"]
        == "blocked_by_same_coordinate_nested_support"
        for row in duplicates
    )
    factor_199_rows = [
        row for row in duplicates if int(row["key"][6]) == 199
    ]
    factor_199_blocked = bool(factor_199_rows) and all(
        row["unit_weight_independence_status"]
        == "blocked_by_same_coordinate_nested_support"
        for row in factor_199_rows
    )
    raw_best = stitching["summary"]["raw_best"]
    return {
        "certificate_type": "fo_pdec_nested_duplicate_dominance_audit",
        "status": "audited_nested_full_multiplicity_blocked_not_global_proof",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "stitching_feasibility_audit": file_sha256(stitching_path),
        },
        "raw_best_factor": raw_best["factor"],
        "raw_best_frequency": raw_best["frequency"],
        "raw_best_fourier": raw_best["fourier"],
        "exact_nested_duplicate_count": len(duplicates),
        "all_exact_nested_duplicates_unit_weight_blocked": all_blocked,
        "factor_199_nested_duplicate_unit_weight_blocked": factor_199_blocked,
        "audited_duplicates": duplicates,
        "closed_subgate": (
            "NestedBlockFullMultiplicityRejectedForAuditedFO-PDEC"
            if all_blocked
            else "NestedBlockMultiplicityStillNeedsCaseSplit"
        ),
        "remaining_after_subgate": [
            "fractional Weighted Hall dual independence, if one wants to keep weighted multiplicity",
            "coordinate quotient / primitive PDEC threshold after removing duplicate unit mass",
            "exact duplicate SAE/Endpoint absorption",
            "cross-q persistence theorem for cross-level reuses",
        ],
        "review_conclusion": (
            "当前 FO-PDEC 有限审计中的 exact nested duplicates 全部是同一正式坐标上的嵌套支撑重复。"
            "因此它们不能按单位权作为两个独立 PDEC 事件计数；若要保留权重，必须提交同口径的"
            " fractional Weighted Hall dual 证书，否则应坐标商掉或回流 SAE/Endpoint。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 审计报告。"""
    lines = [
        "# FO-PDEC 嵌套重复支配审计",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 子门裁定",
        "",
        "```text",
        f"closed_subgate: {result['closed_subgate']}",
        f"raw_best_factor: {result['raw_best_factor']}",
        f"raw_best_frequency: {result['raw_best_frequency']}",
        f"raw_best_fourier: {result['raw_best_fourier']}",
        (
            "all_exact_nested_duplicates_unit_weight_blocked: "
            f"{str(result['all_exact_nested_duplicates_unit_weight_blocked']).lower()}"
        ),
        (
            "factor_199_nested_duplicate_unit_weight_blocked: "
            f"{str(result['factor_199_nested_duplicate_unit_weight_blocked']).lower()}"
        ),
        "```",
        "",
        "## 2. 逐重复审计",
        "",
        "| key | blocks | multiplicity | support relation | sizes | unit status |",
        "| --- | --- | ---: | --- | --- | --- |",
    ]
    for row in result["audited_duplicates"]:
        relation = row["support_relation"]
        lines.append(
            "| "
            + " | ".join(
                table_cell(value)
                for value in [
                    row["key"],
                    row["block_ids"],
                    row["multiplicity"],
                    relation["relation"],
                    relation["sizes"],
                    row["unit_weight_independence_status"],
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 3. 证明含义",
            "",
            "同一正式坐标给出的整数、解释因子、CRT 行相位和双线性方程完全相同。"
            "若两个 Hall 块的半素数支撑又是嵌套关系，则第二个块没有自动产生第二个算术事件。"
            "因此单位权重复计数不合法；合法选择只有三类：",
            "",
            "1. 提交同一多重 formal unit 上的 fractional Weighted Hall dual，并保证每个坐标的对偶权重总和受控；",
            "2. 对 exact duplicate 取坐标商，转入 primitive PDEC 阈值；",
            "3. 把不能持久化的重复视作 SAE/Endpoint 局部逃逸并吸收。",
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
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    stitching = load_json(args.stitching)
    result = build_audit(stitching, args.stitching)
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(result["status"])
    print(result["closed_subgate"])


if __name__ == "__main__":
    main()
