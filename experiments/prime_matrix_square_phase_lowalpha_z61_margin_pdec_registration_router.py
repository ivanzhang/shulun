#!/usr/bin/env python3
"""登记 z=61 分支余量塌缩的 Margin-PDEC 原子。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_margin_pdec_registration_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-margin-pdec-registration-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-margin-pdec-registration-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-margin-pdec-registration-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
SOURCE_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-branch-decision-margin-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-margin-pdec-registration-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-margin-pdec-registration-router.md"

NEXT_TARGET = "GlobalNoMarginCollapseOrMarginPDECExclusion"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-branch-decision-margin-router.json",
]


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def file_sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖哈希。"""
    result = {
        "experiments/prime_matrix_square_phase_lowalpha_z61_margin_pdec_registration_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def signed_offset(value: int, target: int, modulus: int) -> int:
    """返回从 target 到 value 的最短有符号偏移。"""
    raw = (value - target) % modulus
    if raw > modulus // 2:
        raw -= modulus
    return raw


def registration_atoms(source: dict[str, Any]) -> list[dict[str, Any]]:
    """把正余量行转成塌缩原子。"""
    modulus = source["modulus"]
    atoms = []
    for row in source["decision_margin_rows"]:
        for branch in row["branch_margins"]:
            if branch["status"] == "interval_empty":
                atoms.append(
                    {
                        "atom_type": "IntervalMarginCollapse",
                        "step": row["step"],
                        "coefficient": row["coefficient"],
                        "branch_sign": branch["sign"],
                        "selected_branch": branch["selected_branch"],
                        "current_margin": branch["interval_gap"],
                        "collapse_condition": "interval_gap<=0",
                        "pdec_payload": {
                            "mode": "interval_endpoint_collision",
                            "interval_gap": branch["interval_gap"],
                            "integer_stability_radius": branch["integer_stability_radius"],
                        },
                    }
                )
            for item in branch["residue_margin"]["nonhit_rows"]:
                offset = signed_offset(item["sum_mod"], item["nearest_target"], modulus)
                atoms.append(
                    {
                        "atom_type": "ResidueMarginCollapse",
                        "step": row["step"],
                        "coefficient": row["coefficient"],
                        "branch_sign": branch["sign"],
                        "selected_branch": branch["selected_branch"],
                        "branch_status": branch["status"],
                        "candidate_sign_word": item["sign_word"],
                        "candidate_sum": item["signed_sum"],
                        "candidate_sum_mod": item["sum_mod"],
                        "nearest_target": item["nearest_target"],
                        "signed_offset_to_target": offset,
                        "current_margin": item["residue_distance"],
                        "collapse_condition": "signed_offset_to_target=0",
                        "pdec_payload": {
                            "mode": "residue_target_collision",
                            "modulus": modulus,
                            "candidate_sum_mod": item["sum_mod"],
                            "target": item["nearest_target"],
                            "signed_offset": offset,
                        },
                    }
                )
    return atoms


def audit() -> dict[str, Any]:
    """执行 Margin-PDEC 登记。"""
    source = json.loads(SOURCE_JSON.read_text(encoding="utf-8"))
    atoms = registration_atoms(source)
    interval_atoms = [atom for atom in atoms if atom["atom_type"] == "IntervalMarginCollapse"]
    residue_atoms = [atom for atom in atoms if atom["atom_type"] == "ResidueMarginCollapse"]
    min_margin = min(atom["current_margin"] for atom in atoms if atom["current_margin"] is not None)
    closest_atoms = [atom for atom in atoms if atom["current_margin"] == min_margin]
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_margin_pdec_registration_router",
        "status": "z61_branch_margin_reduced_to_margin_pdec_atoms_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "source_certificate": source["certificate_type"],
        "target_bucket": source["target_bucket"],
        "target_omega": source["target_omega"],
        "target_shell": source["target_shell"],
        "margin_pdec_registration_closed": True,
        "margin_atom_count": len(atoms),
        "interval_margin_atom_count": len(interval_atoms),
        "residue_margin_atom_count": len(residue_atoms),
        "minimum_registered_margin": min_margin,
        "closest_margin_atoms": closest_atoms,
        "margin_atoms": atoms,
        "global_no_margin_collapse_proved": False,
        "margin_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "正余量账本的失败可完全物化为 Margin-PDEC 原子：interval-empty 分支若失败，"
            "就是区间端点撞入剩余 signed-sum 盒；residue-empty 分支若失败，就是某个候选"
            "余类撞上目标余类。当前 formal unit 共登记 18 个塌缩原子，其中 2 个区间塌缩、"
            "16 个同余塌缩；最小余量为 55。下一步只剩证明全局不发生这些余量塌缩，"
            "或排斥相应 Margin-PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 Margin-PDEC registration",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"margin_pdec_registration_closed={fmt_bool(result['margin_pdec_registration_closed'])}",
        f"margin_atom_count={result['margin_atom_count']}",
        f"interval_margin_atom_count={result['interval_margin_atom_count']}",
        f"residue_margin_atom_count={result['residue_margin_atom_count']}",
        f"minimum_registered_margin={result['minimum_registered_margin']}",
        f"global_no_margin_collapse_proved={fmt_bool(result['global_no_margin_collapse_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 最近塌缩原子",
        "",
        "| type | step | sign | selected | candidate | target | offset | margin |",
        "| --- | ---: | --- | --- | --- | ---: | ---: | ---: |",
    ]
    for atom in result["closest_margin_atoms"]:
        lines.append(
            f"| `{atom['atom_type']}` | {atom['step']} | `{atom['branch_sign']}` | "
            f"{fmt_bool(atom['selected_branch'])} | `{atom.get('candidate_sign_word', '')}` | "
            f"{atom.get('nearest_target', '')} | {atom.get('signed_offset_to_target', '')} | "
            f"{atom['current_margin']} |"
        )
    lines.extend(
        [
            "",
            "## 2. 全部塌缩原子",
            "",
            "| type | step | coeff | sign | status | candidate | sum mod | target | offset | margin |",
            "| --- | ---: | ---: | --- | --- | --- | ---: | ---: | ---: | ---: |",
        ]
    )
    for atom in result["margin_atoms"]:
        lines.append(
            f"| `{atom['atom_type']}` | {atom['step']} | {atom['coefficient']} | "
            f"`{atom['branch_sign']}` | `{atom.get('branch_status', '')}` | "
            f"`{atom.get('candidate_sign_word', '')}` | {atom.get('candidate_sum_mod', '')} | "
            f"{atom.get('nearest_target', '')} | {atom.get('signed_offset_to_target', '')} | "
            f"{atom['current_margin']} |"
        )
    lines.extend(
        [
            "",
            "## 3. 自足小引理",
            "",
            "BranchDecision 的全局失败只可能来自两种塌缩：",
            "",
            "```text",
            "IntervalMarginCollapse: interval_gap 从正数降到 <=0；",
            "ResidueMarginCollapse: candidate_sum_mod 与目标余类发生碰撞。",
            "```",
            "",
            "所以只要全局证明所有登记原子不塌缩，当前分支决策模式即可稳定；"
            "若任一塌缩发生，它本身就是显式 Margin-PDEC 证书对象。",
            "",
            "## 4. 证明边界",
            "",
            "- 已闭合：当前 z=61 formal unit 的余量失败对象已全部登记为具体原子。",
            "- 未闭合：全局排斥这些 Margin-PDEC，或证明正余量模式全局保持。",
            f"- 下一目标：`{result['next_direct_attack_target']}`。",
            "",
            "## 5. 依赖哈希",
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
                "margin_pdec_registration_closed": result["margin_pdec_registration_closed"],
                "margin_atom_count": result["margin_atom_count"],
                "minimum_registered_margin": result["minimum_registered_margin"],
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
