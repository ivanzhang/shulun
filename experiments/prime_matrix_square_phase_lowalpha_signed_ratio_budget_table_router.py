#!/usr/bin/env python3
"""把 LocalizedBlock-PDEC 原子压成 signed-ratio cap 预算表。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_signed_ratio_budget_table_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-signed-ratio-budget-table-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-signed-ratio-budget-table-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-signed-ratio-budget-table-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
BUDGET_JSON = DOCS / "prime-matrix-square-phase-lowalpha-bilinear-block-budget-contract-router.json"
ATOM_JSON = DOCS / "prime-matrix-square-phase-lowalpha-localized-block-pdec-atom-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-signed-ratio-budget-table-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-signed-ratio-budget-table-router.md"

NEXT_TARGET = "Z31Z61LocalizedBlockSignedRatioCapsOrPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-bilinear-block-budget-contract-router.json",
    "prime-matrix-square-phase-lowalpha-localized-block-pdec-atom-router.json",
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
        "experiments/prime_matrix_square_phase_lowalpha_signed_ratio_budget_table_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def audit() -> dict[str, Any]:
    """生成 signed-ratio cap 预算表。"""
    budget = json.loads(BUDGET_JSON.read_text(encoding="utf-8"))
    atoms = json.loads(ATOM_JSON.read_text(encoding="utf-8"))
    target_by_z = {
        int(row["z"]): row["target_angle"]
        for row in budget["rows"]
        if row["target_angle"] is not None
    }
    atom_rows = []
    for atom in atoms["top_atoms"]:
        z = int(atom["z"])
        target = target_by_z.get(z)
        if target is None:
            cap = None
            proof_class = "no-active-block"
            closed_by_trivial_bound = True
        elif target >= 1.0:
            cap = 1.0
            proof_class = "trivial-signed-ratio"
            closed_by_trivial_bound = True
        else:
            cap = target
            proof_class = "nontrivial-localized-cap"
            closed_by_trivial_bound = False
        observed = float(atom["signed_over_abs"])
        atom_rows.append(
            {
                "atom_label": atom["atom_label"],
                "z": z,
                "bucket": atom["bucket"],
                "route": atom["route"],
                "target_angle": target,
                "required_signed_ratio_cap": cap,
                "observed_signed_ratio": observed,
                "observed_cap_slack": None if cap is None else cap - observed,
                "proof_class": proof_class,
                "closed_by_trivial_bound": closed_by_trivial_bound,
                "sample_passes_cap": cap is None or observed <= cap,
                "weighted_budget": atom["weighted_budget"],
                "abs_share": atom["abs_share"],
            }
        )
    nontrivial = [row for row in atom_rows if not row["closed_by_trivial_bound"]]
    trivial = [row for row in atom_rows if row["closed_by_trivial_bound"]]
    failures = [row for row in atom_rows if not row["sample_passes_cap"]]
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_signed_ratio_budget_table_router",
        "status": "signed_ratio_budget_table_materialized_nontrivial_z31_z61_caps_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "signed_ratio_budget_table_materialized": True,
        "z13_atoms_closed_by_trivial_signed_ratio": all(
            row["closed_by_trivial_bound"] for row in atom_rows if row["z"] == 13
        ),
        "z31_z61_nontrivial_caps_materialized": True,
        "signed_ratio_budget_table_proved": False,
        "localized_block_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "atom_count": len(atom_rows),
        "trivial_atom_count": len(trivial),
        "nontrivial_atom_count": len(nontrivial),
        "sample_failure_count": len(failures),
        "atom_rows": sorted(atom_rows, key=lambda row: (row["closed_by_trivial_bound"], row["z"], row["bucket"])),
        "nontrivial_atoms": nontrivial,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "块级 signed-ratio 预算表进一步压缩了 LocalizedBlock-PDEC："
            "`z=13` 的目标角度大于 `1`，而任何块天然满足 `|signed|/abs<=1`，"
            "所以 `z=13` 四个原子由平凡界闭合。"
            "真正非平凡剩余只有 `z=31` 与 `z=61` 的 8 个局部块 cap："
            "`z=31` 需 `signed/abs<=0.591273`，`z=61` 需 `signed/abs<=0.221522`。"
            "若这些 cap 失败，失败块就是明确的 LocalizedBlock-PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha signed-ratio 预算表",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"signed_ratio_budget_table_materialized={fmt_bool(result['signed_ratio_budget_table_materialized'])}",
        f"z13_atoms_closed_by_trivial_signed_ratio={fmt_bool(result['z13_atoms_closed_by_trivial_signed_ratio'])}",
        f"z31_z61_nontrivial_caps_materialized={fmt_bool(result['z31_z61_nontrivial_caps_materialized'])}",
        f"signed_ratio_budget_table_proved={fmt_bool(result['signed_ratio_budget_table_proved'])}",
        f"localized_block_pdec_excluded={fmt_bool(result['localized_block_pdec_excluded'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 原子预算表",
        "",
        "| atom | route | target | required cap | observed | slack | proof class |",
        "| --- | --- | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in result["atom_rows"]:
        lines.append(
            f"| `{row['atom_label']}` | `{row['route']}` | {fmt_float(row['target_angle'])} | "
            f"{fmt_float(row['required_signed_ratio_cap'])} | {fmt_float(row['observed_signed_ratio'])} | "
            f"{fmt_float(row['observed_cap_slack'])} | `{row['proof_class']}` |"
        )
    lines.extend(
        [
            "",
            "## 2. 非平凡剩余",
            "",
            "| atom | cap | observed | route |",
            "| --- | ---: | ---: | --- |",
        ]
    )
    for row in result["nontrivial_atoms"]:
        lines.append(
            f"| `{row['atom_label']}` | {fmt_float(row['required_signed_ratio_cap'])} | "
            f"{fmt_float(row['observed_signed_ratio'])} | `{row['route']}` |"
        )
    lines.extend(
        [
            "",
            "## 3. 证明边界",
            "",
            "- 已闭合：`z=13` 原子由 `signed/abs<=1` 平凡界通过。",
            "- 已物化：`z=31,z=61` 的 8 个非平凡 signed-ratio cap。",
            "- 未闭合：证明这些 cap，或排斥相应 LocalizedBlock-PDEC。",
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
                "nontrivial_atom_count": result["nontrivial_atom_count"],
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
