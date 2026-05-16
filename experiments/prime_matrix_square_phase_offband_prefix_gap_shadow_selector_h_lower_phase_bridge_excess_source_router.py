#!/usr/bin/env python3
"""追踪相位桥超标的 margin/rho/slot 来源。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_phase_bridge_excess_source_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-phase-bridge-excess-source-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-selector-h-lower-phase-bridge-excess-source-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-phase-bridge-excess-source-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-phase-bridge-excess-source-router.md
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

EXCESS_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-phase-bridge-excess-atom-ledger.json"
PAIR_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-gap-fill-pair-ledger.json"
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-phase-bridge-excess-source-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-phase-bridge-excess-source-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-phase-bridge-excess-source-router.md"

NEXT_TARGET = "GeneratorMarginRhoSlotAbsorptionBoundOrSourcePDECExclusion"


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def source_key(row: dict[str, Any]) -> str:
    """构造更短的超标来源键。"""
    return "|".join(
        [
            f"dir={row['endpoint_direction']}",
            f"gap={row['gap_ell']}",
            f"rho={row['rho_jump']}",
            f"gm={row['generator_margin']}",
            f"db={row['delta_b']}",
            f"slack={row['absorbing_spare_after_bridge_excess']}",
        ]
    )


def build_source_rows(excess_rows: list[dict[str, Any]], pair_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """把超标原子与原始 gap-fill pair 对齐。"""
    pairs_by_key = {str(row["gap_fill_pair_key"]): row for row in pair_rows}
    rows = []
    for atom in excess_rows:
        pair = pairs_by_key[str(atom["source_gap_fill_pair_key"])]
        rho_jump = int(pair["fill_rho"]) - int(pair["generator_rho"])
        row = {
            "gap_ell": int(atom["gap_ell"]),
            "endpoint_direction": str(atom["endpoint_direction"]),
            "generator_ell": int(atom["generator_ell"]),
            "fill_ell": int(atom["fill_ell"]),
            "phase_bridge_gap": int(atom["phase_bridge_gap"]),
            "phase_bridge_gap_excess": int(atom["phase_bridge_gap_excess"]),
            "generator_margin": int(pair["generator_margin"]),
            "fill_margin": int(pair["fill_margin"]),
            "generator_rho": int(pair["generator_rho"]),
            "fill_rho": int(pair["fill_rho"]),
            "rho_jump": rho_jump,
            "three_rho_jump": 3 * rho_jump,
            "delta_b": int(pair["delta_b"]),
            "delta_u": int(pair["delta_u"]),
            "delta_residue": int(pair["delta_residue"]),
            "absorbing_spare_after_bridge_excess": int(atom["absorbing_spare_after_bridge_excess"]),
            "generator_right_depth_spare": int(atom["generator_right_depth_spare"]),
            "fill_left_depth_spare": int(atom["fill_left_depth_spare"]),
            "excess_equals_generator_margin": int(atom["phase_bridge_gap_excess"]) == int(pair["generator_margin"]),
            "excess_equals_three_rho_jump": int(atom["phase_bridge_gap_excess"]) == 3 * rho_jump,
            "post_absorption_slack_equals_abs_delta_b": int(atom["absorbing_spare_after_bridge_excess"]) == abs(int(pair["delta_b"])),
            "source_phase_bridge_excess_atom_key": str(atom["phase_bridge_excess_atom_key"]),
            "source_gap_fill_pair_key": str(pair["gap_fill_pair_key"]),
        }
        row["phase_bridge_excess_source_key"] = source_key(row)
        rows.append(row)
    return rows


def build_result(excess_ledger: Path, pair_ledger: Path) -> dict[str, Any]:
    """构造超标来源账本。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    excess = load_json(excess_ledger)
    pair = load_json(pair_ledger)
    rows = build_source_rows(excess["phase_bridge_excess_atom_rows"], pair["gap_fill_pair_rows"])
    keys = [row["phase_bridge_excess_source_key"] for row in rows]
    aggregate = {
        "excess_ledger": str(excess_ledger.relative_to(ROOT)),
        "pair_ledger": str(pair_ledger.relative_to(ROOT)),
        "phase_bridge_excess_source_count": len(rows),
        "unique_phase_bridge_excess_source_key_count": len(set(keys)),
        "repeated_phase_bridge_excess_source_key_count": len(keys) - len(set(keys)),
        "all_excess_equals_generator_margin": all(row["excess_equals_generator_margin"] for row in rows),
        "all_excess_equals_three_rho_jump": all(row["excess_equals_three_rho_jump"] for row in rows),
        "all_post_absorption_slack_equals_abs_delta_b": all(
            row["post_absorption_slack_equals_abs_delta_b"] for row in rows
        ),
        "generator_margin_rho_slot_absorption_bound_proved": False,
        "phase_bridge_excess_source_pdec_excluded_globally": False,
        "row_column_unconditional_closed": False,
    }
    ledger = {
        "aggregate": aggregate,
        "phase_bridge_excess_source_rows": rows,
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    result = {
        "certificate_type": (
            "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_"
            "phase_bridge_excess_source_router"
        ),
        "status": "phase_bridge_excess_source_identity_closed_current_sweep_global_bound_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_sweep_not_used_as_global_proof": True,
        "aggregate": aggregate,
        "phase_bridge_excess_source_rows": rows,
        "generator_margin_rho_slot_absorption_bound_proved": False,
        "phase_bridge_excess_source_pdec_excluded_globally": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": "PhaseBridgeExcessAbsorptionBoundOrExcessPDECExclusion",
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "本步把唯一 phase bridge 超标的来源继续压缩：超标量等于生成端 margin，"
            "也等于 `3*rho_jump`；超标被吸收后的剩余 slack 等于 `|delta_b|`。"
            "因此当前超标不是自由相位漂移，而是由 margin、rho 翻转和 b 槽位移锁定的单原子。"
            "全局剩余是证明该来源身份的吸收界，或排斥持久 Source-PDEC/SAE。"
        ),
    }
    result["source_hashes"] = {
        "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_phase_bridge_excess_source_router.py": sha256(
            Path(__file__).resolve()
        ),
        "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-phase-bridge-excess-atom-ledger.json": sha256(
            excess_ledger
        ),
        "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-gap-fill-pair-ledger.json": sha256(
            pair_ledger
        ),
        "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-phase-bridge-excess-source-ledger.json": sha256(
            OUT_LEDGER
        ),
    }
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow selector H lower phase bridge excess source router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"phase_bridge_excess_source_count={agg['phase_bridge_excess_source_count']}",
        f"unique_phase_bridge_excess_source_key_count={agg['unique_phase_bridge_excess_source_key_count']}",
        f"repeated_phase_bridge_excess_source_key_count={agg['repeated_phase_bridge_excess_source_key_count']}",
        f"all_excess_equals_generator_margin={fmt_bool(agg['all_excess_equals_generator_margin'])}",
        f"all_excess_equals_three_rho_jump={fmt_bool(agg['all_excess_equals_three_rho_jump'])}",
        f"all_post_absorption_slack_equals_abs_delta_b={fmt_bool(agg['all_post_absorption_slack_equals_abs_delta_b'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 来源身份",
        "",
        "| gap ell | excess | generator margin | 3*rho jump | slack after | |delta b| | source key |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in result["phase_bridge_excess_source_rows"]:
        lines.append(
            f"| {row['gap_ell']} | {row['phase_bridge_gap_excess']} | {row['generator_margin']} | "
            f"{row['three_rho_jump']} | {row['absorbing_spare_after_bridge_excess']} | "
            f"{abs(row['delta_b'])} | `{row['phase_bridge_excess_source_key']}` |"
        )
    lines.extend(
        [
            "",
            "## 2. 结构结论",
            "",
            "- 当前唯一超标量被生成端 margin 精确解释，同时由 `rho` 从 2 到 7 的翻转给出。",
            "- 超标吸收后剩余的 13 不是松散余量，而是等于 `b` 槽位移的绝对值。",
            "- 若全局出现不可吸收超标，必须破坏这些来源身份或复现更短的 Source-PDEC 键。",
            "",
            "## 3. 下一步",
            "",
            f"- 主攻：`{result['next_direct_attack_target']}`。",
            "- 将 `excess=generator_margin=3*rho_jump` 与 `slack=|delta_b|` 作为硬约束，继续排斥持久来源原子。",
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
    parser.add_argument("--excess-ledger", type=Path, default=EXCESS_LEDGER)
    parser.add_argument("--pair-ledger", type=Path, default=PAIR_LEDGER)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    excess_ledger = args.excess_ledger if args.excess_ledger.is_absolute() else ROOT / args.excess_ledger
    pair_ledger = args.pair_ledger if args.pair_ledger.is_absolute() else ROOT / args.pair_ledger
    result = build_result(excess_ledger, pair_ledger)
    write_markdown(result)
    result["source_hashes"][
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-phase-bridge-excess-source-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "phase_bridge_excess_source_count": result["aggregate"]["phase_bridge_excess_source_count"],
                "all_excess_equals_generator_margin": result["aggregate"]["all_excess_equals_generator_margin"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
