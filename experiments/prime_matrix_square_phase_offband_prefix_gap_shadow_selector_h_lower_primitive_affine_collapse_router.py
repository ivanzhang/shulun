#!/usr/bin/env python3
"""把 slot-depth primitive 身份压成当前仿射整数型。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_primitive_affine_collapse_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-primitive-affine-collapse-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-selector-h-lower-primitive-affine-collapse-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-primitive-affine-collapse-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-primitive-affine-collapse-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

PRIMITIVE_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-margin-slot-primitive-identity-ledger.json"
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-primitive-affine-collapse-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-primitive-affine-collapse-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-primitive-affine-collapse-router.md"

NEXT_TARGET = "PrimitiveAffineCollapseGlobalBoundOrAffinePDECExclusion"


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def affine_row(row: dict[str, Any]) -> dict[str, Any]:
    """构造仿射塌缩行。"""
    gap = int(row["gap_ell"])
    abs_db = abs(int(row["delta_b"]))
    abs_du = abs(int(row["delta_u"]))
    margin = int(row["generator_margin"])
    ell_step = int(row["fill_ell"]) - int(row["generator_ell"])
    return {
        "gap_ell": gap,
        "generator_ell": int(row["generator_ell"]),
        "fill_ell": int(row["fill_ell"]),
        "ell_step": ell_step,
        "generator_margin": margin,
        "abs_delta_b": abs_db,
        "abs_delta_u": abs_du,
        "rho_jump": int(row["rho_jump"]),
        "gap_equals_fill_ell": gap == int(row["fill_ell"]),
        "generator_ell_equals_gap_minus_2": int(row["generator_ell"]) == gap - 2,
        "margin_equals_gap_minus_1_over_2": 2 * margin == gap - 1,
        "abs_delta_b_equals_gap_minus_5_over_2": 2 * abs_db == gap - 5,
        "abs_delta_u_equals_gap_minus_3_over_4": 4 * abs_du == gap - 3,
        "rho_jump_equals_2_ell_step_plus_1": int(row["rho_jump"]) == 2 * ell_step + 1,
        "margin_equals_2_abs_delta_u_plus_1": margin == 2 * abs_du + 1,
        "abs_delta_b_equals_2_abs_delta_u_minus_1": abs_db == 2 * abs_du - 1,
        "affine_key": "|".join(
            [
                f"gap={gap}",
                f"ell={gap-2}->{gap}",
                f"m={(gap-1)//2}",
                f"db={(gap-5)//2}",
                f"du={(gap-3)//4}",
            ]
        ),
        "source_primitive_key": str(row["primitive_key"]),
    }


def build_result(primitive_ledger: Path) -> dict[str, Any]:
    """构造仿射塌缩结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    primitive = load_json(primitive_ledger)
    rows = [affine_row(row) for row in primitive["primitive_rows"]]
    flags = [
        "gap_equals_fill_ell",
        "generator_ell_equals_gap_minus_2",
        "margin_equals_gap_minus_1_over_2",
        "abs_delta_b_equals_gap_minus_5_over_2",
        "abs_delta_u_equals_gap_minus_3_over_4",
        "rho_jump_equals_2_ell_step_plus_1",
        "margin_equals_2_abs_delta_u_plus_1",
        "abs_delta_b_equals_2_abs_delta_u_minus_1",
    ]
    keys = [row["affine_key"] for row in rows]
    aggregate = {
        "primitive_ledger": str(primitive_ledger.relative_to(ROOT)),
        "affine_row_count": len(rows),
        "unique_affine_key_count": len(set(keys)),
        "repeated_affine_key_count": len(keys) - len(set(keys)),
        "all_affine_collapse_identities_closed": all(
            all(bool(row[flag]) for flag in flags) for row in rows
        ),
        "affine_identity_flags": flags,
        "primitive_affine_collapse_global_bound_proved": False,
        "affine_pdec_excluded_globally": False,
        "row_column_unconditional_closed": False,
    }
    ledger = {
        "aggregate": aggregate,
        "affine_rows": rows,
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = {
        "certificate_type": (
            "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_"
            "primitive_affine_collapse_router"
        ),
        "status": "primitive_affine_collapse_closed_current_sweep_global_bound_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_sweep_not_used_as_global_proof": True,
        "aggregate": aggregate,
        "affine_rows": rows,
        "primitive_affine_collapse_global_bound_proved": False,
        "affine_pdec_excluded_globally": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": "SlotDepthPrimitiveIdentityBoundOrPrimitivePDECExclusion",
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "本步把当前唯一 primitive 身份组压成仿射整数型：`fill_ell=gap`、"
            "`generator_ell=gap-2`、`margin=(gap-1)/2`、`|delta_b|=(gap-5)/2`、"
            "`|delta_u|=(gap-3)/4`。当前行全部闭合。全局剩余是证明此类仿射塌缩"
            "受全局约束，或排斥持久 Affine-PDEC/SAE。"
        ),
    }
    result["source_hashes"] = {
        "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_primitive_affine_collapse_router.py": sha256(
            Path(__file__).resolve()
        ),
        "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-margin-slot-primitive-identity-ledger.json": sha256(
            primitive_ledger
        ),
        "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-primitive-affine-collapse-ledger.json": sha256(
            OUT_LEDGER
        ),
    }
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow selector H lower primitive affine collapse router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"affine_row_count={agg['affine_row_count']}",
        f"unique_affine_key_count={agg['unique_affine_key_count']}",
        f"repeated_affine_key_count={agg['repeated_affine_key_count']}",
        f"all_affine_collapse_identities_closed={fmt_bool(agg['all_affine_collapse_identities_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 仿射塌缩行",
        "",
        "| gap ell | ell step | margin | |db| | |du| | rho jump | key |",
        "| ---: | --- | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in result["affine_rows"]:
        lines.append(
            f"| {row['gap_ell']} | `{row['generator_ell']}->{row['fill_ell']}` | "
            f"{row['generator_margin']} | {row['abs_delta_b']} | {row['abs_delta_u']} | "
            f"{row['rho_jump']} | `{row['affine_key']}` |"
        )
    lines.extend(
        [
            "",
            "## 2. 闭合的仿射身份",
            "",
            "- `fill_ell=gap_ell`。",
            "- `generator_ell=gap_ell-2`。",
            "- `generator_margin=(gap_ell-1)/2`。",
            "- `|delta_b|=(gap_ell-5)/2`。",
            "- `|delta_u|=(gap_ell-3)/4`。",
            "- `rho_jump=2*(fill_ell-generator_ell)+1`。",
            "",
            "## 3. 下一步",
            "",
            f"- 主攻：`{result['next_direct_attack_target']}`。",
            "- 证明这种仿射塌缩无法持久复现，或把复现登记为 Affine-PDEC/SAE。",
            "",
            "## 4. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in result["source_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--primitive-ledger", type=Path, default=PRIMITIVE_LEDGER)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    primitive_ledger = args.primitive_ledger if args.primitive_ledger.is_absolute() else ROOT / args.primitive_ledger
    result = build_result(primitive_ledger)
    write_markdown(result)
    result["source_hashes"][
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-primitive-affine-collapse-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "affine_row_count": result["aggregate"]["affine_row_count"],
                "all_affine_collapse_identities_closed": result["aggregate"][
                    "all_affine_collapse_identities_closed"
                ],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
