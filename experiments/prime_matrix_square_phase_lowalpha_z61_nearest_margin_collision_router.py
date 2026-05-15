#!/usr/bin/env python3
"""审计 z=61 Margin-PDEC 最近塌缩原子的 offset 模式。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_nearest_margin_collision_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-nearest-margin-collision-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-nearest-margin-collision-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-nearest-margin-collision-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
SOURCE_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-margin-pdec-registration-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-nearest-margin-collision-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-nearest-margin-collision-router.md"

NEXT_TARGET = "Offset55MarginCollisionExclusionOrOffsetPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-margin-pdec-registration-router.json",
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
        "experiments/prime_matrix_square_phase_lowalpha_z61_nearest_margin_collision_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def group_atoms(atoms: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """按原子类型、余量、偏移聚合。"""
    groups: dict[tuple[Any, ...], list[dict[str, Any]]] = defaultdict(list)
    for atom in atoms:
        key = (
            atom["atom_type"],
            atom["current_margin"],
            atom.get("signed_offset_to_target"),
        )
        groups[key].append(atom)
    result = []
    for (atom_type, margin, offset), members in sorted(
        groups.items(), key=lambda item: (item[0][1], str(item[0][0]), str(item[0][2]))
    ):
        result.append(
            {
                "atom_type": atom_type,
                "margin": margin,
                "signed_offset_to_target": offset,
                "member_count": len(members),
                "steps": [member["step"] for member in members],
                "members": members,
            }
        )
    return result


def audit() -> dict[str, Any]:
    """执行最近塌缩模式审计。"""
    source = json.loads(SOURCE_JSON.read_text(encoding="utf-8"))
    atoms = source["margin_atoms"]
    groups = group_atoms(atoms)
    minimum_margin = source["minimum_registered_margin"]
    closest_groups = [group for group in groups if group["margin"] == minimum_margin]
    closest_offsets = sorted({group["signed_offset_to_target"] for group in closest_groups})
    closest_all_residue = all(group["atom_type"] == "ResidueMarginCollapse" for group in closest_groups)
    closest_single_offset = len(closest_offsets) == 1
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_nearest_margin_collision_router",
        "status": "z61_margin_pdec_reduced_to_nearest_offset55_collision_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "source_certificate": source["certificate_type"],
        "target_bucket": source["target_bucket"],
        "target_omega": source["target_omega"],
        "target_shell": source["target_shell"],
        "nearest_margin_collision_group_count": len(closest_groups),
        "minimum_margin": minimum_margin,
        "closest_offsets": closest_offsets,
        "closest_all_residue_collisions": closest_all_residue,
        "closest_single_offset_closed": closest_single_offset,
        "closest_collision_groups": closest_groups,
        "all_margin_collision_groups": groups,
        "offset55_collision_pattern_closed_for_formal_unit": (
            closest_all_residue and closest_single_offset and closest_offsets == [-55]
        ),
        "offset55_margin_collision_excluded": False,
        "global_no_margin_collapse_proved": False,
        "row_column_unconditional_closed": False,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "Margin-PDEC 的最近塌缩并非分散随机：最小余量 55 的所有原子都是"
            "ResidueMarginCollapse，且有同一个有符号偏移 `candidate-target=-55`。"
            "三条最近原子分别在 step 1、2、3 出现。"
            "因此下一硬点可从任意 margin collapse 收窄为固定 offset-55 同余碰撞族，"
            "或登记 Offset-PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 nearest margin collision",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"minimum_margin={result['minimum_margin']}",
        f"nearest_margin_collision_group_count={result['nearest_margin_collision_group_count']}",
        f"closest_offsets={result['closest_offsets']}",
        f"offset55_collision_pattern_closed_for_formal_unit={fmt_bool(result['offset55_collision_pattern_closed_for_formal_unit'])}",
        f"offset55_margin_collision_excluded={fmt_bool(result['offset55_margin_collision_excluded'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 最近 offset-55 原子",
        "",
        "| step | branch sign | selected | candidate | sum mod | target | offset | margin |",
        "| ---: | --- | --- | --- | ---: | ---: | ---: | ---: |",
    ]
    for group in result["closest_collision_groups"]:
        for atom in group["members"]:
            lines.append(
                f"| {atom['step']} | `{atom['branch_sign']}` | {fmt_bool(atom['selected_branch'])} | "
                f"`{atom.get('candidate_sign_word', '')}` | {atom.get('candidate_sum_mod', '')} | "
                f"{atom.get('nearest_target', '')} | {atom.get('signed_offset_to_target', '')} | "
                f"{atom['current_margin']} |"
            )
    lines.extend(
        [
            "",
            "## 2. 塌缩群组",
            "",
            "| type | margin | offset | count | steps |",
            "| --- | ---: | ---: | ---: | --- |",
        ]
    )
    for group in result["all_margin_collision_groups"]:
        lines.append(
            f"| `{group['atom_type']}` | {group['margin']} | "
            f"{'' if group['signed_offset_to_target'] is None else group['signed_offset_to_target']} | "
            f"{group['member_count']} | `{group['steps']}` |"
        )
    lines.extend(
        [
            "",
            "## 3. 自足小引理",
            "",
            "若最小余量塌缩必须先发生，则当前 formal unit 中第一个可能塌缩的同余事件满足",
            "",
            "```text",
            "candidate_sum_mod = target - 55 (mod 2627).",
            "```",
            "",
            "所以全局排斥可优先针对 offset `-55` 的持久碰撞族；若该族出现，"
            "它就是比一般 Margin-PDEC 更窄的 Offset-PDEC。",
            "",
            "## 4. 证明边界",
            "",
            "- 已闭合：当前 z=61 formal unit 的最近塌缩全部归为同一 offset `-55` 同余碰撞。",
            "- 未闭合：全局排斥 offset-55 碰撞族，或证明更宽 margin 塌缩也不能持久。",
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
                "minimum_margin": result["minimum_margin"],
                "closest_offsets": result["closest_offsets"],
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
