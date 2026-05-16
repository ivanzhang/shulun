#!/usr/bin/env python3
"""把 phase bridge 超标吸收压成 margin/slot 正规形。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_margin_slot_absorption_normal_form_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-margin-slot-absorption-normal-form-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-selector-h-lower-margin-slot-absorption-normal-form-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-margin-slot-absorption-normal-form-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-margin-slot-absorption-normal-form-router.md
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

SOURCE_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-phase-bridge-excess-source-ledger.json"
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-margin-slot-absorption-normal-form-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-margin-slot-absorption-normal-form-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-margin-slot-absorption-normal-form-router.md"

NEXT_TARGET = "MarginSlotAbsorptionNormalFormBoundOrNormalFormPDECExclusion"


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def normal_form_row(row: dict[str, Any]) -> dict[str, Any]:
    """构造 margin/slot 吸收正规形行。"""
    absorbing_depth_spare = int(row["generator_right_depth_spare"]) + int(row["fill_left_depth_spare"])
    margin_plus_abs_delta_b = int(row["generator_margin"]) + abs(int(row["delta_b"]))
    right_spare_decomposition = int(row["generator_margin"]) + abs(int(row["delta_u"])) + int(row["fill_left_depth_spare"])
    return {
        "gap_ell": int(row["gap_ell"]),
        "endpoint_direction": str(row["endpoint_direction"]),
        "generator_margin": int(row["generator_margin"]),
        "delta_b": int(row["delta_b"]),
        "delta_u": int(row["delta_u"]),
        "rho_jump": int(row["rho_jump"]),
        "absorbing_depth_spare": absorbing_depth_spare,
        "margin_plus_abs_delta_b": margin_plus_abs_delta_b,
        "absorbing_spare_identity_closed": absorbing_depth_spare == margin_plus_abs_delta_b,
        "post_absorption_slack": int(row["absorbing_spare_after_bridge_excess"]),
        "post_absorption_slack_equals_abs_delta_b": int(row["absorbing_spare_after_bridge_excess"]) == abs(int(row["delta_b"])),
        "generator_right_depth_spare": int(row["generator_right_depth_spare"]),
        "fill_left_depth_spare": int(row["fill_left_depth_spare"]),
        "right_spare_decomposition": right_spare_decomposition,
        "right_spare_decomposition_closed": int(row["generator_right_depth_spare"]) == right_spare_decomposition,
        "normal_form_key": "|".join(
            [
                f"gap={row['gap_ell']}",
                f"margin={row['generator_margin']}",
                f"db={row['delta_b']}",
                f"du={row['delta_u']}",
                f"rho={row['rho_jump']}",
            ]
        ),
        "source_key": str(row["phase_bridge_excess_source_key"]),
    }


def build_result(source_ledger: Path) -> dict[str, Any]:
    """构造 margin/slot 正规形账本。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    source = load_json(source_ledger)
    rows = [normal_form_row(row) for row in source["phase_bridge_excess_source_rows"]]
    keys = [row["normal_form_key"] for row in rows]
    aggregate = {
        "source_ledger": str(source_ledger.relative_to(ROOT)),
        "normal_form_row_count": len(rows),
        "unique_normal_form_key_count": len(set(keys)),
        "repeated_normal_form_key_count": len(keys) - len(set(keys)),
        "all_absorbing_spare_identities_closed": all(row["absorbing_spare_identity_closed"] for row in rows),
        "all_post_absorption_slack_equals_abs_delta_b": all(
            row["post_absorption_slack_equals_abs_delta_b"] for row in rows
        ),
        "all_right_spare_decompositions_closed": all(row["right_spare_decomposition_closed"] for row in rows),
        "margin_slot_absorption_normal_form_bound_proved": False,
        "normal_form_pdec_excluded_globally": False,
        "row_column_unconditional_closed": False,
    }
    ledger = {
        "aggregate": aggregate,
        "normal_form_rows": rows,
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = {
        "certificate_type": (
            "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_"
            "margin_slot_absorption_normal_form_router"
        ),
        "status": "margin_slot_absorption_normal_form_closed_current_sweep_global_bound_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_sweep_not_used_as_global_proof": True,
        "aggregate": aggregate,
        "normal_form_rows": rows,
        "margin_slot_absorption_normal_form_bound_proved": False,
        "normal_form_pdec_excluded_globally": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": "GeneratorMarginRhoSlotAbsorptionBoundOrSourcePDECExclusion",
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "本步把 phase bridge 超标吸收写成 margin/slot 正规形："
            "`absorbing_depth_spare = generator_margin + |delta_b|`，且 "
            "`generator_right_spare = generator_margin + |delta_u| + fill_left_spare`。"
            "当前唯一行两个身份均闭合。全局剩余是证明该正规形预算界，"
            "或排斥持久 NormalForm-PDEC/SAE。"
        ),
    }
    result["source_hashes"] = {
        "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_margin_slot_absorption_normal_form_router.py": sha256(
            Path(__file__).resolve()
        ),
        "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-phase-bridge-excess-source-ledger.json": sha256(
            source_ledger
        ),
        "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-margin-slot-absorption-normal-form-ledger.json": sha256(
            OUT_LEDGER
        ),
    }
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow selector H lower margin slot absorption normal form router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"normal_form_row_count={agg['normal_form_row_count']}",
        f"unique_normal_form_key_count={agg['unique_normal_form_key_count']}",
        f"repeated_normal_form_key_count={agg['repeated_normal_form_key_count']}",
        f"all_absorbing_spare_identities_closed={fmt_bool(agg['all_absorbing_spare_identities_closed'])}",
        f"all_post_absorption_slack_equals_abs_delta_b={fmt_bool(agg['all_post_absorption_slack_equals_abs_delta_b'])}",
        f"all_right_spare_decompositions_closed={fmt_bool(agg['all_right_spare_decompositions_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 正规形行",
        "",
        "| gap ell | margin | delta b | delta u | absorbing spare | margin+|db| | right spare decomposition | key |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in result["normal_form_rows"]:
        lines.append(
            f"| {row['gap_ell']} | {row['generator_margin']} | {row['delta_b']} | {row['delta_u']} | "
            f"{row['absorbing_depth_spare']} | {row['margin_plus_abs_delta_b']} | "
            f"{row['right_spare_decomposition']} | `{row['normal_form_key']}` |"
        )
    lines.extend(
        [
            "",
            "## 2. 结构结论",
            "",
            "- 超标吸收不再依赖自由三分量预算，而被压成 margin 与槽位位移的两个等式。",
            "- 剩余 slack 精确等于 `|delta_b|`，说明 `b` 槽位移是最终余量来源。",
            "- 全局失败必须破坏这些等式或复现同一 NormalForm-PDEC 键。",
            "",
            "## 3. 下一步",
            "",
            f"- 主攻：`{result['next_direct_attack_target']}`。",
            "- 证明 margin/slot 正规形在端点缺口修复中全局成立，或排斥持久正规形原子。",
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
    parser.add_argument("--source-ledger", type=Path, default=SOURCE_LEDGER)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    source_ledger = args.source_ledger if args.source_ledger.is_absolute() else ROOT / args.source_ledger
    result = build_result(source_ledger)
    write_markdown(result)
    result["source_hashes"][
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-margin-slot-absorption-normal-form-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "normal_form_row_count": result["aggregate"]["normal_form_row_count"],
                "all_absorbing_spare_identities_closed": result["aggregate"][
                    "all_absorbing_spare_identities_closed"
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
