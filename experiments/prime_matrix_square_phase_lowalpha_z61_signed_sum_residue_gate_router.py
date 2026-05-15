#!/usr/bin/env python3
"""审计 z=61 carry 层的 signed-sum 同余门。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_signed_sum_residue_gate_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-signed-sum-residue-gate-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-signed-sum-residue-gate-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-signed-sum-residue-gate-router.md
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
CARRY_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-carry-layer-projection-router.json"
SIGNED_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-signed-projection-support-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-signed-sum-residue-gate-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-signed-sum-residue-gate-router.md"

NEXT_TARGET = "FiveTermSignedSumIntervalResidueGlobalBoundOrSumResiduePDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-carry-layer-projection-router.json",
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
        "experiments/prime_matrix_square_phase_lowalpha_z61_signed_sum_residue_gate_router.py": file_sha256(
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


def signed_sum_rows(carry_source: dict[str, Any], signed_source: dict[str, Any]) -> list[dict[str, Any]]:
    """把 carry 目标纤维改写成五项 signed-sum 区间同余门。"""
    rows = []
    signed_groups = {
        (row["modulus"], row["selected_residue"]): row
        for row in signed_source["signed_projection_rows"]
    }
    for carry_group in carry_source["carry_layer_rows"]:
        modulus = carry_group["modulus"]
        q2 = carry_group["q2"]
        q4 = carry_group["q4"]
        selected = carry_group["selected_residue"]
        signed_group = signed_groups[(modulus, selected)]
        local_rows = signed_group["local_rows"]
        coefficients = [
            row["positive_root"] * row["basis_integer"]
            for row in local_rows
        ]
        local_moduli = [row["local_modulus"] for row in local_rows]
        q4_targets = carry_group["q4_targets"]
        q2_targets = carry_group["q2_targets"]
        combined_targets = carry_group["combined_targets"]

        sign_rows = []
        for signs in product([1, -1], repeat=len(coefficients)):
            signed_sum = sum(sign * coefficient for sign, coefficient in zip(signs, coefficients))
            root = signed_sum % modulus
            carry = (signed_sum - root) // modulus
            sign_rows.append(
                {
                    "sign_word": sign_word(signs),
                    "signed_sum_integer": signed_sum,
                    "least_residue_carry": carry,
                    "root_residue": root,
                    "sum_mod_37": signed_sum % q4,
                    "sum_mod_71": signed_sum % q2,
                    "sum_mod_2627": signed_sum % (q2 * q4),
                    "root_mod_37": root % q4,
                    "root_mod_71": root % q2,
                    "root_mod_2627": root % (q2 * q4),
                    "selected": root == selected,
                }
            )
        sign_rows.sort(key=lambda item: item["root_residue"])

        layer_rows = []
        by_carry: dict[int, list[dict[str, Any]]] = defaultdict(list)
        for sign_row in sign_rows:
            by_carry[sign_row["least_residue_carry"]].append(sign_row)
        for carry in sorted(by_carry):
            layer = by_carry[carry]
            shifted_q4_targets = sorted({(target + carry * modulus) % q4 for target in q4_targets})
            shifted_q2_targets = sorted({(target + carry * modulus) % q2 for target in q2_targets})
            shifted_combined_targets = sorted(
                {(target + carry * modulus) % (q2 * q4) for target in combined_targets}
            )
            q4_hits = [row for row in layer if row["sum_mod_37"] in shifted_q4_targets]
            q2_hits = [row for row in layer if row["sum_mod_71"] in shifted_q2_targets]
            combined_hits = [
                row for row in layer if row["sum_mod_2627"] in shifted_combined_targets
            ]
            layer_rows.append(
                {
                    "carry": carry,
                    "interval_start": carry * modulus,
                    "interval_stop_exclusive": (carry + 1) * modulus,
                    "sign_count": len(layer),
                    "shifted_q4_sum_targets": shifted_q4_targets,
                    "shifted_q2_sum_targets": shifted_q2_targets,
                    "shifted_combined_sum_targets": shifted_combined_targets,
                    "q4_hit_words": [f"{row['sign_word']}:{row['root_residue']}" for row in q4_hits],
                    "q2_hit_words": [f"{row['sign_word']}:{row['root_residue']}" for row in q2_hits],
                    "combined_hit_words": [
                        f"{row['sign_word']}:{row['root_residue']}" for row in combined_hits
                    ],
                    "q4_hit_count": len(q4_hits),
                    "q2_hit_count": len(q2_hits),
                    "combined_hit_count": len(combined_hits),
                }
            )

        combined_hits_all = [
            row
            for row in sign_rows
            if row["sum_mod_2627"]
            in {
                (target + row["least_residue_carry"] * modulus) % (q2 * q4)
                for target in combined_targets
            }
        ]
        selected_rows = [row for row in sign_rows if row["selected"]]
        rows.append(
            {
                "modulus": modulus,
                "q2": q2,
                "q4": q4,
                "selected_residue": selected,
                "local_moduli": local_moduli,
                "signed_coefficients": coefficients,
                "coefficient_mod_37": [coefficient % q4 for coefficient in coefficients],
                "coefficient_mod_71": [coefficient % q2 for coefficient in coefficients],
                "coefficient_mod_2627": [coefficient % (q2 * q4) for coefficient in coefficients],
                "carry_values": sorted(by_carry),
                "selected_sign_word": selected_rows[0]["sign_word"] if selected_rows else None,
                "selected_signed_sum": selected_rows[0]["signed_sum_integer"] if selected_rows else None,
                "selected_carry": selected_rows[0]["least_residue_carry"] if selected_rows else None,
                "selected_sum_mod_2627": selected_rows[0]["sum_mod_2627"] if selected_rows else None,
                "layer_rows": layer_rows,
                "combined_hit_count": len(combined_hits_all),
                "combined_hit_words": [
                    f"{row['sign_word']}:{row['root_residue']}" for row in combined_hits_all
                ],
                "signed_sum_residue_gate_closed_for_group": (
                    len(combined_hits_all) == 1 and combined_hits_all[0]["root_residue"] == selected
                ),
            }
        )
    return rows


def audit() -> dict[str, Any]:
    """执行 signed-sum 同余门审计。"""
    carry_source = json.loads(CARRY_JSON.read_text(encoding="utf-8"))
    signed_source = json.loads(SIGNED_JSON.read_text(encoding="utf-8"))
    rows = signed_sum_rows(carry_source, signed_source)
    all_rows_closed = bool(rows) and all(row["signed_sum_residue_gate_closed_for_group"] for row in rows)
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_signed_sum_residue_gate_router",
        "status": "z61_carry_layer_projection_reduced_to_five_term_signed_sum_residue_gate_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "source_certificate": carry_source["certificate_type"],
        "target_bucket": carry_source["target_bucket"],
        "target_omega": carry_source["target_omega"],
        "target_shell": carry_source["target_shell"],
        "signed_sum_residue_gate_group_count": len(rows),
        "all_signed_sum_residue_gates_closed": all_rows_closed,
        "signed_sum_rows": rows,
        "five_term_signed_sum_interval_residue_global_bound_proved": False,
        "sum_residue_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "carry-layer 目标纤维可写成五项 signed-sum 的区间同余门："
            "`S=±14421±19228±36708±382536±12540`，"
            "`cM<=S<(c+1)M`，且 `S mod 2627` 落在随 carry 平移的目标类中。"
            "当前 formal unit 中唯一命中为 `S=373055`、`c=6`、"
            "`S mod 2627=21`、符号字 `--++-`，对应 `r=26951`。"
            "因此最新硬点成为五项 signed-sum 区间同余纤维的全局界，"
            "或登记 SumResidue-PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 signed-sum residue gate",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"signed_sum_residue_gate_group_count={result['signed_sum_residue_gate_group_count']}",
        f"all_signed_sum_residue_gates_closed={fmt_bool(result['all_signed_sum_residue_gates_closed'])}",
        f"five_term_signed_sum_interval_residue_global_bound_proved={fmt_bool(result['five_term_signed_sum_interval_residue_global_bound_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. Signed-Sum 摘要",
        "",
        "| M | coefficients | selected S | selected carry | selected S mod 2627 | selected sign | combined hits | closed |",
        "| ---: | --- | ---: | ---: | ---: | --- | --- | --- |",
    ]
    for row in result["signed_sum_rows"]:
        lines.append(
            f"| {row['modulus']} | `{row['signed_coefficients']}` | "
            f"{row['selected_signed_sum']} | {row['selected_carry']} | "
            f"{row['selected_sum_mod_2627']} | `{row['selected_sign_word']}` | "
            f"`{row['combined_hit_words']}` | "
            f"{fmt_bool(row['signed_sum_residue_gate_closed_for_group'])} |"
        )
    lines.extend(
        [
            "",
            "## 2. Carry 层同余门",
            "",
            "| carry | S interval | shifted q4 targets | shifted q2 targets | shifted mod 2627 targets | q4 hits | q2 hits | combined hits |",
            "| ---: | --- | --- | --- | --- | --- | --- | --- |",
        ]
    )
    for row in result["signed_sum_rows"]:
        for layer in row["layer_rows"]:
            lines.append(
                f"| {layer['carry']} | `[{layer['interval_start']},{layer['interval_stop_exclusive']})` | "
                f"`{layer['shifted_q4_sum_targets']}` | `{layer['shifted_q2_sum_targets']}` | "
                f"`{layer['shifted_combined_sum_targets']}` | `{layer['q4_hit_words']}` | "
                f"`{layer['q2_hit_words']}` | `{layer['combined_hit_words']}` |"
            )
    lines.extend(
        [
            "",
            "## 3. 自足小引理",
            "",
            "令",
            "",
            "```text",
            "S(sigma)=sum_i sigma_i A_i,  A=[14421,19228,36708,382536,12540].",
            "r=S-cM, 0<=r<M.",
            "```",
            "",
            "则 `r mod L` 落在目标类 `T` 等价于",
            "",
            "```text",
            "S mod L in T+cM mod L",
            "and cM<=S<(c+1)M.",
            "```",
            "",
            "因此 carry-layer 目标纤维完全转化为有限项 signed-sum 的区间同余纤维。",
            "",
            "## 4. 证明边界",
            "",
            "- 已闭合：当前 z=61 formal unit 的五项 signed-sum 区间同余门唯一命中 `--++- / S=373055 / r=26951`。",
            "- 未闭合：全局五项 signed-sum 区间同余纤维容量界，或 SumResidue-PDEC 排斥。",
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
                "all_signed_sum_residue_gates_closed": result["all_signed_sum_residue_gates_closed"],
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
