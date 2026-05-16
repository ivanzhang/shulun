#!/usr/bin/env python3
"""登记相位桥超标原子与吸收预算。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_phase_bridge_excess_atom_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-phase-bridge-excess-atom-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-selector-h-lower-phase-bridge-excess-atom-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-phase-bridge-excess-atom-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-phase-bridge-excess-atom-router.md
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

PHASE_BUDGET_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-corridor-phase-budget-ledger.json"
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-phase-bridge-excess-atom-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-phase-bridge-excess-atom-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-phase-bridge-excess-atom-router.md"

NEXT_TARGET = "PhaseBridgeExcessAbsorptionBoundOrExcessPDECExclusion"


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def excess_atom_key(row: dict[str, Any]) -> str:
    """构造相位桥超标原子键。"""
    excess = int(row["component_excess"]["phase_bridge_gap_excess"])
    return "|".join(
        [
            f"dir={row['endpoint_direction']}",
            f"gap={row['gap_ell']}",
            f"gen={row['generator_ell']}",
            f"fill={row['fill_ell']}",
            f"bridge={row['phase_bridge_gap']}",
            f"excess={excess}",
            f"gr={row['generator_right_depth']}",
            f"fl={row['fill_left_depth']}",
            f"slack={row['corridor_3gap_slack']}",
        ]
    )


def atom_row(row: dict[str, Any]) -> dict[str, Any]:
    """压缩一条超标相位桥行。"""
    gap = int(row["gap_ell"])
    bridge_excess = int(row["component_excess"]["phase_bridge_gap_excess"])
    right_spare = int(row["component_spare"]["generator_right_depth_spare"])
    left_spare = int(row["component_spare"]["fill_left_depth_spare"])
    absorbing_spare = right_spare + left_spare
    return {
        "gap_ell": gap,
        "endpoint_direction": str(row["endpoint_direction"]),
        "generator_ell": int(row["generator_ell"]),
        "fill_ell": int(row["fill_ell"]),
        "generator_p": int(row["generator_p"]),
        "fill_p": int(row["fill_p"]),
        "generator_phase": list(row["generator_phase"]),
        "fill_phase": list(row["fill_phase"]),
        "phase_bridge_gap": int(row["phase_bridge_gap"]),
        "phase_bridge_gap_excess": bridge_excess,
        "generator_right_depth": int(row["generator_right_depth"]),
        "fill_left_depth": int(row["fill_left_depth"]),
        "generator_right_depth_spare": right_spare,
        "fill_left_depth_spare": left_spare,
        "absorbing_depth_spare": absorbing_spare,
        "absorbing_spare_after_bridge_excess": absorbing_spare - bridge_excess,
        "corridor_3gap_slack": int(row["corridor_3gap_slack"]),
        "excess_absorbed_current_sweep": absorbing_spare >= bridge_excess,
        "phase_bridge_excess_atom_key": excess_atom_key(row),
        "source_gap_fill_pair_key": str(row["gap_fill_pair_key"]),
    }


def build_result(phase_budget_ledger: Path) -> dict[str, Any]:
    """构造相位桥超标原子账本。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    budget = load_json(phase_budget_ledger)
    atom_rows = [
        atom_row(row)
        for row in budget["phase_budget_rows"]
        if int(row["component_excess"]["phase_bridge_gap_excess"]) > 0
    ]
    keys = [row["phase_bridge_excess_atom_key"] for row in atom_rows]
    aggregate = {
        "phase_budget_ledger": str(phase_budget_ledger.relative_to(ROOT)),
        "phase_bridge_excess_atom_count": len(atom_rows),
        "unique_phase_bridge_excess_atom_key_count": len(set(keys)),
        "repeated_phase_bridge_excess_atom_key_count": len(keys) - len(set(keys)),
        "all_excess_atoms_absorbed_current_sweep": all(row["excess_absorbed_current_sweep"] for row in atom_rows),
        "min_absorbing_spare_after_bridge_excess": min(
            (row["absorbing_spare_after_bridge_excess"] for row in atom_rows),
            default=0,
        ),
        "max_phase_bridge_gap_excess": max((row["phase_bridge_gap_excess"] for row in atom_rows), default=0),
        "phase_bridge_excess_absorption_bound_proved": False,
        "phase_bridge_excess_pdec_excluded_globally": False,
        "row_column_unconditional_closed": False,
    }
    ledger = {
        "aggregate": aggregate,
        "phase_bridge_excess_atom_rows": atom_rows,
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    result = {
        "certificate_type": (
            "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_"
            "phase_bridge_excess_atom_router"
        ),
        "status": "phase_bridge_excess_atom_materialized_current_sweep_global_bound_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_sweep_not_used_as_global_proof": True,
        "aggregate": aggregate,
        "phase_bridge_excess_atom_rows": atom_rows,
        "phase_bridge_excess_absorption_bound_proved": False,
        "phase_bridge_excess_pdec_excluded_globally": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": "CorridorPhaseBudgetBoundOrPhaseBridgePDECExclusion",
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "本步把唯一相位桥超标登记为显式原子：`gap_ell=31` 的 phase bridge "
            "超出一个 gap 的量为 15，而左右深度余量合计为 28，吸收后仍余 13。"
            "当前没有重复超标原子。全局剩余是证明这种超标总能被深度余量吸收，"
            "或排斥持久 PhaseBridgeExcess-PDEC/SAE。"
        ),
    }
    result["source_hashes"] = {
        "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_phase_bridge_excess_atom_router.py": sha256(
            Path(__file__).resolve()
        ),
        "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-corridor-phase-budget-ledger.json": sha256(
            phase_budget_ledger
        ),
        "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-phase-bridge-excess-atom-ledger.json": sha256(
            OUT_LEDGER
        ),
    }
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow selector H lower phase bridge excess atom router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"phase_bridge_excess_atom_count={agg['phase_bridge_excess_atom_count']}",
        f"unique_phase_bridge_excess_atom_key_count={agg['unique_phase_bridge_excess_atom_key_count']}",
        f"repeated_phase_bridge_excess_atom_key_count={agg['repeated_phase_bridge_excess_atom_key_count']}",
        f"all_excess_atoms_absorbed_current_sweep={fmt_bool(agg['all_excess_atoms_absorbed_current_sweep'])}",
        f"max_phase_bridge_gap_excess={agg['max_phase_bridge_gap_excess']}",
        f"min_absorbing_spare_after_bridge_excess={agg['min_absorbing_spare_after_bridge_excess']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 超标原子",
        "",
        "| gap ell | bridge gap | excess | right spare | left spare | spare after excess | key |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in result["phase_bridge_excess_atom_rows"]:
        lines.append(
            f"| {row['gap_ell']} | {row['phase_bridge_gap']} | {row['phase_bridge_gap_excess']} | "
            f"{row['generator_right_depth_spare']} | {row['fill_left_depth_spare']} | "
            f"{row['absorbing_spare_after_bridge_excess']} | `{row['phase_bridge_excess_atom_key']}` |"
        )
    lines.extend(
        [
            "",
            "## 2. 结构结论",
            "",
            "- 当前 phase bridge 超标只有一个原子，且已被左右深度余量吸收。",
            "- 这个原子是 `3*gap_ell` 短走廊余量最紧来源；若全局复现或失控，就是下一层 PDEC 入口。",
            "- 全局闭合仍需证明超标吸收界，而不是把当前单例直接外推。",
            "",
            "## 3. 下一步",
            "",
            f"- 主攻：`{result['next_direct_attack_target']}`。",
            "- 对 phase bridge excess 的可吸收性建立全局不等式，或证明重复 excess key 不可持久。",
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
    parser.add_argument("--phase-budget-ledger", type=Path, default=PHASE_BUDGET_LEDGER)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    phase_budget_ledger = (
        args.phase_budget_ledger
        if args.phase_budget_ledger.is_absolute()
        else ROOT / args.phase_budget_ledger
    )
    result = build_result(phase_budget_ledger)
    write_markdown(result)
    result["source_hashes"][
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-phase-bridge-excess-atom-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "phase_bridge_excess_atom_count": result["aggregate"]["phase_bridge_excess_atom_count"],
                "all_excess_atoms_absorbed_current_sweep": result["aggregate"][
                    "all_excess_atoms_absorbed_current_sweep"
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
