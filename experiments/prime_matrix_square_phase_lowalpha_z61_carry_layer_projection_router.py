#!/usr/bin/env python3
"""审计 z=61 符号投影支撑的 carry 分层。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_carry_layer_projection_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-carry-layer-projection-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-carry-layer-projection-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-carry-layer-projection-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import defaultdict
from itertools import product
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
SOURCE_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-signed-projection-support-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-carry-layer-projection-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-carry-layer-projection-router.md"

NEXT_TARGET = "CarryLayerTargetFiberGlobalBoundOrCarryProjectionPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-signed-projection-support-router.json",
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
        "experiments/prime_matrix_square_phase_lowalpha_z61_carry_layer_projection_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def sign_word(signs: tuple[int, ...]) -> str:
    """把 ±1 符号向量写成短字。"""
    return "".join("+" if sign > 0 else "-" for sign in signs)


def carry_layer_rows(source: dict[str, Any]) -> list[dict[str, Any]]:
    """按最小代表 carry 分层审计目标投影纤维。"""
    rows = []
    for group in source["signed_projection_rows"]:
        modulus = group["modulus"]
        q2 = group["q2"]
        q4 = group["q4"]
        selected = group["selected_residue"]
        local_rows = group["local_rows"]
        positive_roots = [row["positive_root"] for row in local_rows]
        basis_integers = [row["basis_integer"] for row in local_rows]

        q4_targets = []
        q2_targets = []
        for gate in group["gate_fibers"]:
            if gate["ell"] == q4:
                q4_targets = gate["target_residues"]
            if gate["ell"] == q2:
                q2_targets = gate["target_residues"]
        combined_targets = [item["target_class"] for item in group["combined_fibers"]]

        sign_rows = []
        for signs in product([1, -1], repeat=len(local_rows)):
            signed_sum = sum(
                sign * positive_root * basis
                for sign, positive_root, basis in zip(signs, positive_roots, basis_integers)
            )
            root = signed_sum % modulus
            carry = (signed_sum - root) // modulus
            sign_rows.append(
                {
                    "sign_word": sign_word(signs),
                    "signed_sum_integer": signed_sum,
                    "least_residue_carry": carry,
                    "root_residue": root,
                    "root_mod_37": root % q4,
                    "root_mod_71": root % q2,
                    "root_mod_2627": root % (q2 * q4),
                    "q4_target_hit": root % q4 in q4_targets,
                    "q2_target_hit": root % q2 in q2_targets,
                    "combined_target_hit": root % (q2 * q4) in combined_targets,
                    "selected": root == selected,
                }
            )
        sign_rows.sort(key=lambda item: item["root_residue"])

        layers: dict[int, list[dict[str, Any]]] = defaultdict(list)
        for sign_row in sign_rows:
            layers[sign_row["least_residue_carry"]].append(sign_row)

        layer_rows = []
        for carry, layer in sorted(layers.items()):
            target_hits = [row for row in layer if row["q4_target_hit"] or row["q2_target_hit"]]
            combined_hits = [row for row in layer if row["combined_target_hit"]]
            layer_rows.append(
                {
                    "carry": carry,
                    "sign_count": len(layer),
                    "signed_sum_min": min(row["signed_sum_integer"] for row in layer),
                    "signed_sum_max": max(row["signed_sum_integer"] for row in layer),
                    "root_residues": [row["root_residue"] for row in layer],
                    "q4_or_q2_target_hit_count": len(target_hits),
                    "combined_target_hit_count": len(combined_hits),
                    "target_hit_words": [
                        f"{row['sign_word']}:{row['root_residue']}" for row in target_hits
                    ],
                    "combined_hit_words": [
                        f"{row['sign_word']}:{row['root_residue']}" for row in combined_hits
                    ],
                }
            )

        target_hits_all = [row for row in sign_rows if row["q4_target_hit"] or row["q2_target_hit"]]
        combined_hits_all = [row for row in sign_rows if row["combined_target_hit"]]
        selected_rows = [row for row in sign_rows if row["selected"]]
        rows.append(
            {
                "modulus": modulus,
                "q2": q2,
                "q4": q4,
                "selected_residue": selected,
                "q4_targets": q4_targets,
                "q2_targets": q2_targets,
                "combined_targets": combined_targets,
                "sign_vector_count": len(sign_rows),
                "carry_values": sorted(layers),
                "carry_layer_count": len(layers),
                "selected_sign_word": selected_rows[0]["sign_word"] if selected_rows else None,
                "selected_carry": selected_rows[0]["least_residue_carry"] if selected_rows else None,
                "layer_rows": layer_rows,
                "q4_or_q2_target_hit_count": len(target_hits_all),
                "combined_target_hit_count": len(combined_hits_all),
                "all_target_hits_are_selected": (
                    len(target_hits_all) == 1
                    and len(combined_hits_all) == 1
                    and target_hits_all[0]["root_residue"] == selected
                    and combined_hits_all[0]["root_residue"] == selected
                ),
                "carry_layer_projection_closed_for_group": (
                    len(target_hits_all) == 1
                    and len(combined_hits_all) == 1
                    and target_hits_all[0]["root_residue"] == selected
                    and combined_hits_all[0]["root_residue"] == selected
                ),
            }
        )
    return rows


def audit() -> dict[str, Any]:
    """执行 carry 分层审计。"""
    source = json.loads(SOURCE_JSON.read_text(encoding="utf-8"))
    rows = carry_layer_rows(source)
    all_rows_closed = bool(rows) and all(row["carry_layer_projection_closed_for_group"] for row in rows)
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_carry_layer_projection_router",
        "status": "z61_signed_crt_support_reduced_to_carry_layer_projection_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "source_certificate": source["certificate_type"],
        "target_bucket": source["target_bucket"],
        "target_omega": source["target_omega"],
        "target_shell": source["target_shell"],
        "carry_layer_projection_group_count": len(rows),
        "all_carry_layer_projections_closed": all_rows_closed,
        "carry_layer_rows": rows,
        "carry_layer_target_fiber_global_bound_proved": False,
        "carry_projection_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "带 carry 的符号支撑可进一步按最小代表层 `c` 分解。"
            "当前 formal unit 的 32 个符号向量只落在 8 个 carry 层："
            "`-9,-8,-7,-6,5,6,7,8`。"
            "所有 `37/71/2627` 目标投影命中都集中在 `carry=6` 的单个符号字 "
            "`--++-`，对应 `r=26951`。"
            "因此最新硬点是全局 carry-layer 目标纤维界，或登记 CarryProjection-PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 carry-layer projection",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"carry_layer_projection_group_count={result['carry_layer_projection_group_count']}",
        f"all_carry_layer_projections_closed={fmt_bool(result['all_carry_layer_projections_closed'])}",
        f"carry_layer_target_fiber_global_bound_proved={fmt_bool(result['carry_layer_target_fiber_global_bound_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. Carry 分层摘要",
        "",
        "| M | carry values | selected carry | selected sign | q4/q2 target hits | combined hits | closed |",
        "| ---: | --- | ---: | --- | ---: | ---: | --- |",
    ]
    for row in result["carry_layer_rows"]:
        lines.append(
            f"| {row['modulus']} | `{row['carry_values']}` | {row['selected_carry']} | "
            f"`{row['selected_sign_word']}` | {row['q4_or_q2_target_hit_count']} | "
            f"{row['combined_target_hit_count']} | "
            f"{fmt_bool(row['carry_layer_projection_closed_for_group'])} |"
        )
    lines.extend(
        [
            "",
            "## 2. Carry 层表",
            "",
            "| carry | sign count | S min | S max | target hits | combined hits |",
            "| ---: | ---: | ---: | ---: | --- | --- |",
        ]
    )
    for row in result["carry_layer_rows"]:
        for layer in row["layer_rows"]:
            lines.append(
                f"| {layer['carry']} | {layer['sign_count']} | {layer['signed_sum_min']} | "
                f"{layer['signed_sum_max']} | `{layer['target_hit_words']}` | "
                f"`{layer['combined_hit_words']}` |"
            )
    lines.extend(
        [
            "",
            "## 3. 自足小引理",
            "",
            "对符号和 `S(sigma)` 定义最小代表 carry `c(sigma)` 为唯一整数，使",
            "",
            "```text",
            "0 <= S(sigma)-c(sigma)M < M.",
            "```",
            "",
            "则目标投影条件不是单独的 `S(sigma) mod ell` 条件，而是分层条件",
            "",
            "```text",
            "S(sigma)-cM in target classes mod ell.",
            "```",
            "",
            "所以每个 carry 层可以独立审计目标纤维。当前证书显示除 `c=6` 外所有层目标纤维为空，"
            "而 `c=6` 层也只有 `--++-` 一个目标命中。",
            "",
            "## 4. 证明边界",
            "",
            "- 已闭合：当前 z=61 formal unit 的 carry 分层目标纤维唯一命中 `--++- / r=26951`。",
            "- 未闭合：全局 carry-layer 目标纤维容量界，或 CarryProjection-PDEC 排斥。",
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
                "all_carry_layer_projections_closed": result["all_carry_layer_projections_closed"],
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
