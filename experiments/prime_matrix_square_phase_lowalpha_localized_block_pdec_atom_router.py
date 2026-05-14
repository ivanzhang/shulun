#!/usr/bin/env python3
"""把双线性块 signed budget 剩余原子化为 LocalizedBlock-PDEC。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_localized_block_pdec_atom_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-localized-block-pdec-atom-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-localized-block-pdec-atom-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-localized-block-pdec-atom-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
BUDGET_JSON = DOCS / "prime-matrix-square-phase-lowalpha-bilinear-block-budget-contract-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-localized-block-pdec-atom-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-localized-block-pdec-atom-router.md"

NEXT_TARGET = "LocalizedBlockPDECAtomExclusionOrSignedRatioBudgetTable"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-bilinear-block-budget-contract-router.json",
]


def fmt_float(value: float | None) -> str:
    """格式化浮点数。"""
    if value is None:
        return "n/a"
    return f"{value:.6f}"


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def file_sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖哈希。"""
    result = {
        "experiments/prime_matrix_square_phase_lowalpha_localized_block_pdec_atom_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def classify_bucket(bucket: str) -> str:
    """把块类型映射到证明路线。"""
    if bucket in {"balanced<=2", "mid<=4"}:
        return "BilinearDispersion"
    return "EndpointPDEC"


def audit() -> dict[str, Any]:
    """执行局部块原子化。"""
    budget = json.loads(BUDGET_JSON.read_text(encoding="utf-8"))
    atoms = []
    for block in budget["block_rows"]:
        if float(block["abs_contribution"]) <= 0:
            continue
        route = classify_bucket(block["bucket"])
        atoms.append(
            {
                "atom_label": f"LocalizedBlockPDEC(z={block['z']},bucket={block['bucket']})",
                "z": block["z"],
                "bucket": block["bucket"],
                "route": route,
                "abs_share": block["abs_share"],
                "signed_over_abs": block["signed_over_abs"],
                "weighted_budget": block["weighted_budget"],
                "signed_contribution": block["signed_contribution"],
                "abs_contribution": block["abs_contribution"],
                "proved": False,
            }
        )
    route_summaries: dict[str, dict[str, Any]] = {}
    for atom in atoms:
        row = route_summaries.setdefault(
            atom["route"],
            {
                "route": atom["route"],
                "atom_count": 0,
                "total_weighted_budget": 0.0,
                "max_weighted_budget": 0.0,
                "sample_atoms": [],
            },
        )
        row["atom_count"] += 1
        row["total_weighted_budget"] += float(atom["weighted_budget"])
        row["max_weighted_budget"] = max(row["max_weighted_budget"], float(atom["weighted_budget"]))
        if len(row["sample_atoms"]) < 8:
            row["sample_atoms"].append(atom["atom_label"])
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_localized_block_pdec_atom_router",
        "status": "localized_block_pdec_atoms_materialized_exclusion_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "localized_block_pdec_atoms_materialized": True,
        "bilinear_dispersion_atoms_routed": True,
        "endpoint_pdec_atoms_routed": True,
        "signed_ratio_budget_table_proved": False,
        "localized_block_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "atom_count": len(atoms),
        "route_summaries": sorted(route_summaries.values(), key=lambda row: -row["total_weighted_budget"]),
        "top_atoms": sorted(atoms, key=lambda row: -float(row["weighted_budget"]))[:24],
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "双线性块 signed budget 的剩余现在原子化为具体 `LocalizedBlockPDEC(z,bucket)`。"
            "balanced/mid 原子进入 BilinearDispersion 证明路线，unbalanced/far 原子进入 EndpointPDEC 路线。"
            "因此下一步不再需要处理整块总和，只需给出这些原子的 signed ratio 预算表，"
            "或逐个排斥局部块 PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha LocalizedBlock-PDEC 原子",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"localized_block_pdec_atoms_materialized={fmt_bool(result['localized_block_pdec_atoms_materialized'])}",
        f"bilinear_dispersion_atoms_routed={fmt_bool(result['bilinear_dispersion_atoms_routed'])}",
        f"endpoint_pdec_atoms_routed={fmt_bool(result['endpoint_pdec_atoms_routed'])}",
        f"signed_ratio_budget_table_proved={fmt_bool(result['signed_ratio_budget_table_proved'])}",
        f"localized_block_pdec_excluded={fmt_bool(result['localized_block_pdec_excluded'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 路线汇总",
        "",
        "| route | atoms | total weighted budget | max weighted budget | sample atoms |",
        "| --- | ---: | ---: | ---: | --- |",
    ]
    for row in result["route_summaries"]:
        lines.append(
            f"| `{row['route']}` | {row['atom_count']} | {fmt_float(row['total_weighted_budget'])} | "
            f"{fmt_float(row['max_weighted_budget'])} | `{row['sample_atoms']}` |"
        )
    lines.extend(
        [
            "",
            "## 2. 最大原子",
            "",
            "| atom | route | signed/abs | weighted budget | abs share |",
            "| --- | --- | ---: | ---: | ---: |",
        ]
    )
    for atom in result["top_atoms"]:
        lines.append(
            f"| `{atom['atom_label']}` | `{atom['route']}` | "
            f"{fmt_float(atom['signed_over_abs'])} | {fmt_float(atom['weighted_budget'])} | "
            f"{fmt_float(atom['abs_share'])} |"
        )
    lines.extend(
        [
            "",
            "## 3. 证明边界",
            "",
            "- 已物化：所有局部块 PDEC 原子。",
            "- 未闭合：BilinearDispersion 原子的 signed ratio 预算。",
            "- 未闭合：EndpointPDEC 原子的排斥或吸收。",
            "- 未闭合：统一 signed ratio budget 表。",
            f"- 下一目标：`{result['next_direct_attack_target']}`。",
            "",
            "## 4. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for name, digest in sorted(result["source_hashes"].items()):
        lines.append(f"| `{name}` | `{digest}` |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    result = audit()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result)
    print(
        json.dumps(
            {
                "status": result["status"],
                "atom_count": result["atom_count"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        ),
        flush=True,
    )


if __name__ == "__main__":
    main()
