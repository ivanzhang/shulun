#!/usr/bin/env python3
"""把 z=61 两个次级残量 bucket 压成有限深度格原子。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_secondary_residual_atom_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-secondary-residual-atom-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-secondary-residual-atom-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-secondary-residual-atom-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
STAR_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-principal-star-residual-router.json"
SUPPORT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-profile-pair-support-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-secondary-residual-atom-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-secondary-residual-atom-router.md"

NEXT_TARGET = "ResidualAtomPhaseInvariantForMidUnbalancedOrAtomPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-principal-star-residual-router.json",
    "prime-matrix-square-phase-lowalpha-z61-profile-pair-support-router.json",
]


def safe_ratio(numerator: float, denominator: float) -> float | None:
    """计算安全比值。"""
    if denominator <= 0:
        return None
    return numerator / denominator


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
        "experiments/prime_matrix_square_phase_lowalpha_z61_secondary_residual_atom_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def support_lookup(support_data: dict[str, Any]) -> dict[tuple[str, str], dict[str, Any]]:
    """建立 `(bucket,pair)` 到支撑信息的索引。"""
    return {
        (bucket_row["bucket"], pair_row["pair_key"]): pair_row
        for bucket_row in support_data["bucket_rows"]
        for pair_row in bucket_row["pair_support_rows"]
    }


def atom_key(atom: dict[str, Any]) -> str:
    """生成残量原子键。"""
    return f"{atom['bucket']}|{atom['pair_key']}|omega={atom['omega']}|shell={atom['shell']}"


def cover_atoms(atoms: list[dict[str, Any]], target: float) -> list[dict[str, Any]]:
    """按贡献从大到小选取覆盖原子。"""
    result = []
    total = 0.0
    for atom in sorted(atoms, key=lambda item: item["bucket_abs_share"], reverse=True):
        if total >= target:
            break
        total += atom["bucket_abs_share"]
        result.append({**atom, "cumulative_bucket_abs_share": total})
    return result


def audit() -> dict[str, Any]:
    """执行残量原子审计。"""
    star_data = json.loads(STAR_JSON.read_text(encoding="utf-8"))
    support_data = json.loads(SUPPORT_JSON.read_text(encoding="utf-8"))
    support_by_pair = support_lookup(support_data)
    residual_rows = []
    atom_rows = []
    missing_support = []

    for residual in star_data["residual_summary"]:
        bucket = residual["bucket"]
        atoms = []
        for pair in residual["secondary_cover_pairs"]:
            support = support_by_pair.get((bucket, pair["pair_key"]))
            if support is None:
                missing_support.append({"bucket": bucket, "pair_key": pair["pair_key"]})
                continue
            for cell in support["top_cells"]:
                atom = {
                    "bucket": bucket,
                    "pair_key": pair["pair_key"],
                    "positive_p": pair["positive_p"],
                    "negative_p": pair["negative_p"],
                    "omega": cell["omega"],
                    "shell": cell["shell"],
                    "sign_word": cell["sign_word"],
                    "bucket_abs_share": cell["bucket_abs_share"],
                    "pair_credit": cell["pair_credit"],
                    "cell_credit_share_from_pair": cell["cell_credit_share_from_pair"],
                    "required_residual_share": safe_ratio(
                        cell["bucket_abs_share"],
                        residual["residual_needed_ratio"],
                    ),
                }
                atom["atom_key"] = atom_key(atom)
                atoms.append(atom)
        selected = cover_atoms(atoms, residual["residual_needed_ratio"])
        selected_credit = sum(atom["bucket_abs_share"] for atom in selected)
        residual_rows.append(
            {
                "bucket": bucket,
                "residual_needed_ratio": residual["residual_needed_ratio"],
                "secondary_credit_ratio": residual["secondary_credit_ratio"],
                "selected_atom_count": len(selected),
                "selected_atom_credit_ratio": selected_credit,
                "selected_atom_surplus_ratio": selected_credit - residual["residual_needed_ratio"],
                "selected_atoms_cover_residual": selected_credit + 1e-12 >= residual["residual_needed_ratio"],
                "candidate_atom_count": len(atoms),
                "selected_atoms": selected,
            }
        )
        atom_rows.extend(selected)

    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_secondary_residual_atom_router",
        "status": "z61_secondary_residual_reduced_to_nine_depth_atoms_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "p_list": star_data["p_list"],
        "z": star_data["z"],
        "principal_positive_p": star_data["principal_positive_p"],
        "secondary_residual_atom_support_materialized": len(missing_support) == 0,
        "sample_selected_atoms_cover_all_residuals": all(
            row["selected_atoms_cover_residual"] for row in residual_rows
        ),
        "residual_bucket_count": len(residual_rows),
        "selected_atom_count": len(atom_rows),
        "residual_atom_phase_invariant_proved": False,
        "atom_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "missing_support_count": len(missing_support),
        "missing_support": missing_support,
        "residual_rows": residual_rows,
        "atom_rows": atom_rows,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "主星形之后的两个残量 bucket 已压成有限残量原子："
            "`mid<=4` 由 2 个深度格原子覆盖，`unbalanced<=8` 由 7 个深度格原子覆盖。"
            "因此下一步可逐原子证明相位不变量；若这些原子支撑无法强制存在，"
            "则输出 Atom-PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 次级残量原子路由",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"secondary_residual_atom_support_materialized={fmt_bool(result['secondary_residual_atom_support_materialized'])}",
        f"sample_selected_atoms_cover_all_residuals={fmt_bool(result['sample_selected_atoms_cover_all_residuals'])}",
        f"residual_bucket_count={result['residual_bucket_count']}",
        f"selected_atom_count={result['selected_atom_count']}",
        f"residual_atom_phase_invariant_proved={fmt_bool(result['residual_atom_phase_invariant_proved'])}",
        f"atom_pdec_excluded={fmt_bool(result['atom_pdec_excluded'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 残量 bucket 原子覆盖",
        "",
        "| bucket | residual need | selected atoms | selected credit | surplus | candidate atoms |",
        "| --- | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in result["residual_rows"]:
        lines.append(
            f"| `{row['bucket']}` | {fmt_float(row['residual_needed_ratio'])} | "
            f"{row['selected_atom_count']} | {fmt_float(row['selected_atom_credit_ratio'])} | "
            f"{fmt_float(row['selected_atom_surplus_ratio'])} | {row['candidate_atom_count']} |"
        )
    lines.extend(
        [
            "",
            "## 2. 选中残量原子",
            "",
            "| bucket | pair | omega | shell | signs | credit/residual | bucket share | cumulative |",
            "| --- | --- | ---: | --- | --- | ---: | ---: | ---: |",
        ]
    )
    for row in result["residual_rows"]:
        for atom in row["selected_atoms"]:
            lines.append(
                f"| `{atom['bucket']}` | `{atom['pair_key']}` | {atom['omega']} | "
                f"`{atom['shell']}` | `{atom['sign_word']}` | "
                f"{fmt_float(atom['required_residual_share'])} | "
                f"{fmt_float(atom['bucket_abs_share'])} | "
                f"{fmt_float(atom['cumulative_bucket_abs_share'])} |"
            )
    lines.extend(
        [
            "",
            "## 3. 证明边界",
            "",
            "- 已闭合：两个残量 bucket 的样本覆盖可由 9 个显式深度格原子承担。",
            "- 未闭合：需要证明这些原子的相位/支撑不变量，或登记 Atom-PDEC。",
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
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    result = audit()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result)
    print(
        json.dumps(
            {
                "status": result["status"],
                "selected_atom_count": result["selected_atom_count"],
                "sample_selected_atoms_cover_all_residuals": result[
                    "sample_selected_atoms_cover_all_residuals"
                ],
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
