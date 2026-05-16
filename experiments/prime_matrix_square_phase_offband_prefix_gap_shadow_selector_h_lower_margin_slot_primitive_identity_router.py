#!/usr/bin/env python3
"""把 margin/slot 吸收正规形继续压成 slot-depth primitive 身份。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_margin_slot_primitive_identity_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-margin-slot-primitive-identity-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-selector-h-lower-margin-slot-primitive-identity-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-margin-slot-primitive-identity-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-margin-slot-primitive-identity-router.md
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

NORMAL_FORM_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-margin-slot-absorption-normal-form-ledger.json"
SOURCE_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-phase-bridge-excess-source-ledger.json"
PAIR_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-gap-fill-pair-ledger.json"
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-margin-slot-primitive-identity-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-margin-slot-primitive-identity-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-margin-slot-primitive-identity-router.md"

NEXT_TARGET = "SlotDepthPrimitiveIdentityBoundOrPrimitivePDECExclusion"


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def primitive_row(normal_form: dict[str, Any], source: dict[str, Any], pair: dict[str, Any]) -> dict[str, Any]:
    """构造 primitive 身份行。"""
    gap = int(pair["gap_ell"])
    gm = int(pair["generator_margin"])
    db = int(pair["delta_b"])
    du = int(pair["delta_u"])
    generator_ell = int(pair["generator_ell"])
    fill_ell = int(pair["fill_ell"])
    gen_left, gen_right = map(int, pair["generator_depth"])
    fill_left, _fill_right = map(int, pair["fill_depth"])
    fill_left_spare = int(normal_form["fill_left_depth_spare"])
    row = {
        "gap_ell": gap,
        "generator_ell": generator_ell,
        "fill_ell": fill_ell,
        "generator_margin": gm,
        "fill_margin": int(pair["fill_margin"]),
        "delta_b": db,
        "delta_u": du,
        "rho_jump": int(normal_form["rho_jump"]),
        "phase_bridge_gap": int(source["phase_bridge_gap"]),
        "phase_bridge_excess": int(source["phase_bridge_gap_excess"]),
        "generator_left_depth": gen_left,
        "generator_right_depth": gen_right,
        "fill_left_depth": fill_left,
        "fill_left_spare": fill_left_spare,
        "fill_left_spare_identity_rhs": fill_ell - generator_ell + 1,
        "fill_left_spare_equals_ell_step_plus_one": fill_left_spare == fill_ell - generator_ell + 1,
        "generator_left_minus_margin": gen_left - gm,
        "generator_left_minus_margin_equals_fill_left_spare": gen_left - gm == fill_left_spare,
        "generator_right_identity_rhs": abs(du) - 1,
        "generator_right_equals_abs_delta_u_minus_one": gen_right == abs(du) - 1,
        "fill_margin_identity_rhs": gm + abs(db) - 1,
        "fill_margin_equals_generator_margin_plus_abs_delta_b_minus_one": int(pair["fill_margin"]) == gm + abs(db) - 1,
        "fill_left_identity_rhs": int(pair["fill_margin"]) + 1,
        "fill_left_equals_fill_margin_plus_one": fill_left == int(pair["fill_margin"]) + 1,
        "phase_bridge_identity_rhs": gap + gm,
        "phase_bridge_gap_equals_gap_plus_generator_margin": int(source["phase_bridge_gap"]) == gap + gm,
        "primitive_key": "|".join(
            [
                f"gap={gap}",
                f"eg={generator_ell}->{fill_ell}",
                f"gm={gm}",
                f"db={db}",
                f"du={du}",
                f"fls={fill_left_spare}",
            ]
        ),
    }
    return row


def build_result(normal_form_ledger: Path, source_ledger: Path, pair_ledger: Path) -> dict[str, Any]:
    """构造 primitive 身份结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    normal = load_json(normal_form_ledger)
    source = load_json(source_ledger)
    pair = load_json(pair_ledger)
    normal_rows = normal["normal_form_rows"]
    source_rows = source["phase_bridge_excess_source_rows"]
    pair_rows_by_key = {row["gap_fill_pair_key"]: row for row in pair["gap_fill_pair_rows"]}
    rows = []
    for index, normal_row in enumerate(normal_rows):
        source_row = source_rows[index]
        pair_row = pair_rows_by_key[source_row["source_gap_fill_pair_key"]]
        rows.append(primitive_row(normal_row, source_row, pair_row))
    keys = [row["primitive_key"] for row in rows]
    identity_flags = [
        "fill_left_spare_equals_ell_step_plus_one",
        "generator_left_minus_margin_equals_fill_left_spare",
        "generator_right_equals_abs_delta_u_minus_one",
        "fill_margin_equals_generator_margin_plus_abs_delta_b_minus_one",
        "fill_left_equals_fill_margin_plus_one",
        "phase_bridge_gap_equals_gap_plus_generator_margin",
    ]
    aggregate = {
        "normal_form_ledger": str(normal_form_ledger.relative_to(ROOT)),
        "source_ledger": str(source_ledger.relative_to(ROOT)),
        "pair_ledger": str(pair_ledger.relative_to(ROOT)),
        "primitive_row_count": len(rows),
        "unique_primitive_key_count": len(set(keys)),
        "repeated_primitive_key_count": len(keys) - len(set(keys)),
        "all_primitive_identities_closed": all(
            all(bool(row[flag]) for flag in identity_flags) for row in rows
        ),
        "identity_flags": identity_flags,
        "slot_depth_primitive_identity_bound_proved": False,
        "primitive_pdec_excluded_globally": False,
        "row_column_unconditional_closed": False,
    }
    ledger = {
        "aggregate": aggregate,
        "primitive_rows": rows,
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = {
        "certificate_type": (
            "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_"
            "margin_slot_primitive_identity_router"
        ),
        "status": "margin_slot_primitive_identities_closed_current_sweep_global_bound_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_sweep_not_used_as_global_proof": True,
        "aggregate": aggregate,
        "primitive_rows": rows,
        "slot_depth_primitive_identity_bound_proved": False,
        "primitive_pdec_excluded_globally": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": "MarginSlotAbsorptionNormalFormBoundOrNormalFormPDECExclusion",
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "本步把 margin/slot 吸收正规形继续压成六个 slot-depth primitive 身份："
            "`fill_left_spare=fill_ell-generator_ell+1`、`generator_left-margin=fill_left_spare`、"
            "`generator_right=|delta_u|-1`、`fill_margin=generator_margin+|delta_b|-1`、"
            "`fill_left=fill_margin+1`、`phase_bridge_gap=gap_ell+generator_margin`。"
            "当前唯一行全部闭合。全局剩余是证明这些 primitive 身份稳定成立，"
            "或排斥持久 Primitive-PDEC/SAE。"
        ),
    }
    result["source_hashes"] = {
        "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_margin_slot_primitive_identity_router.py": sha256(
            Path(__file__).resolve()
        ),
        "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-margin-slot-absorption-normal-form-ledger.json": sha256(
            normal_form_ledger
        ),
        "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-phase-bridge-excess-source-ledger.json": sha256(
            source_ledger
        ),
        "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-margin-slot-primitive-identity-ledger.json": sha256(
            OUT_LEDGER
        ),
    }
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow selector H lower margin slot primitive identity router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"primitive_row_count={agg['primitive_row_count']}",
        f"unique_primitive_key_count={agg['unique_primitive_key_count']}",
        f"repeated_primitive_key_count={agg['repeated_primitive_key_count']}",
        f"all_primitive_identities_closed={fmt_bool(agg['all_primitive_identities_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. primitive 身份",
        "",
        "| gap ell | ell step | margin | db | du | fill spare | gen right | fill margin | bridge | key |",
        "| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in result["primitive_rows"]:
        lines.append(
            f"| {row['gap_ell']} | `{row['generator_ell']}->{row['fill_ell']}` | "
            f"{row['generator_margin']} | {row['delta_b']} | {row['delta_u']} | "
            f"{row['fill_left_spare']} | {row['generator_right_depth']} | {row['fill_margin']} | "
            f"{row['phase_bridge_gap']} | `{row['primitive_key']}` |"
        )
    lines.extend(
        [
            "",
            "## 2. 闭合的等式",
            "",
            "- `fill_left_spare=fill_ell-generator_ell+1`。",
            "- `generator_left_depth-generator_margin=fill_left_spare`。",
            "- `generator_right_depth=|delta_u|-1`。",
            "- `fill_margin=generator_margin+|delta_b|-1`。",
            "- `fill_left_depth=fill_margin+1`。",
            "- `phase_bridge_gap=gap_ell+generator_margin`。",
            "",
            "## 3. 下一步",
            "",
            f"- 主攻：`{result['next_direct_attack_target']}`。",
            "- 将这些 primitive 身份转成全局 slot-depth 约束，或登记违反身份的 Primitive-PDEC/SAE。",
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
    parser.add_argument("--normal-form-ledger", type=Path, default=NORMAL_FORM_LEDGER)
    parser.add_argument("--source-ledger", type=Path, default=SOURCE_LEDGER)
    parser.add_argument("--pair-ledger", type=Path, default=PAIR_LEDGER)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    normal_form_ledger = args.normal_form_ledger if args.normal_form_ledger.is_absolute() else ROOT / args.normal_form_ledger
    source_ledger = args.source_ledger if args.source_ledger.is_absolute() else ROOT / args.source_ledger
    pair_ledger = args.pair_ledger if args.pair_ledger.is_absolute() else ROOT / args.pair_ledger
    result = build_result(normal_form_ledger, source_ledger, pair_ledger)
    write_markdown(result)
    result["source_hashes"][
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-margin-slot-primitive-identity-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "primitive_row_count": result["aggregate"]["primitive_row_count"],
                "all_primitive_identities_closed": result["aggregate"]["all_primitive_identities_closed"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
