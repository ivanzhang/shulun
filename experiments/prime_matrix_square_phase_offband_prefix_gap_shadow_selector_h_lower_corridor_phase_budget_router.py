#!/usr/bin/env python3
"""把短走廊填充界分解为相位桥三分量预算。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_corridor_phase_budget_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-corridor-phase-budget-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-selector-h-lower-corridor-phase-budget-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-corridor-phase-budget-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-corridor-phase-budget-router.md
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

PAIR_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-gap-fill-pair-ledger.json"
CORRIDOR_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-gap-repair-corridor-ledger.json"
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-corridor-phase-budget-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-corridor-phase-budget-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-corridor-phase-budget-router.md"

NEXT_TARGET = "CorridorPhaseBudgetBoundOrPhaseBridgePDECExclusion"


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def phase_budget_row(row: dict[str, Any]) -> dict[str, Any]:
    """构造一条相位桥预算行。"""
    gap = int(row["gap_ell"])
    generator_p = int(row["generator_p"])
    fill_p = int(row["fill_p"])
    gen_left, gen_right = map(int, row["generator_depth"])
    fill_left, fill_right = map(int, row["fill_depth"])
    generator_phase_lo = generator_p - gen_left
    generator_phase_hi = generator_p + gen_right
    fill_phase_lo = fill_p - fill_left
    fill_phase_hi = fill_p + fill_right
    phase_bridge_gap = fill_phase_lo - generator_phase_hi
    p_delay = fill_p - generator_p
    identity_total = gen_right + phase_bridge_gap + fill_left
    component_spare = {
        "generator_right_depth_spare": gap - gen_right,
        "phase_bridge_gap_spare": gap - phase_bridge_gap,
        "fill_left_depth_spare": gap - fill_left,
    }
    component_excess = {
        "generator_right_depth_excess": max(0, gen_right - gap),
        "phase_bridge_gap_excess": max(0, phase_bridge_gap - gap),
        "fill_left_depth_excess": max(0, fill_left - gap),
    }
    row_out = {
        "gap_ell": gap,
        "endpoint_direction": str(row["endpoint_direction"]),
        "generator_ell": int(row["generator_ell"]),
        "fill_ell": int(row["fill_ell"]),
        "generator_p": generator_p,
        "fill_p": fill_p,
        "generator_phase": [generator_phase_lo, generator_phase_hi],
        "fill_phase": [fill_phase_lo, fill_phase_hi],
        "generator_right_depth": gen_right,
        "phase_bridge_gap": phase_bridge_gap,
        "fill_left_depth": fill_left,
        "p_delay": p_delay,
        "phase_budget_identity_total": identity_total,
        "phase_budget_identity_closed": identity_total == p_delay,
        "corridor_3gap_budget": 3 * gap,
        "corridor_3gap_slack": 3 * gap - p_delay,
        "component_spare": component_spare,
        "component_excess": component_excess,
        "total_component_excess_over_gap": sum(component_excess.values()),
        "other_component_spare_after_excess": (
            sum(max(0, value) for value in component_spare.values())
            - sum(component_excess.values())
        ),
        "all_three_components_below_gap": gen_right <= gap and phase_bridge_gap <= gap and fill_left <= gap,
        "phase_bridge_within_2gap": phase_bridge_gap <= 2 * gap,
        "gap_fill_pair_key": str(row["gap_fill_pair_key"]),
    }
    return row_out


def build_result(pair_ledger: Path, corridor_ledger: Path) -> dict[str, Any]:
    """构造相位桥预算结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    pair = load_json(pair_ledger)
    rows = [phase_budget_row(row) for row in pair["gap_fill_pair_rows"]]
    aggregate = {
        "pair_ledger": str(pair_ledger.relative_to(ROOT)),
        "corridor_ledger": str(corridor_ledger.relative_to(ROOT)),
        "phase_budget_row_count": len(rows),
        "all_phase_budget_identities_closed": all(row["phase_budget_identity_closed"] for row in rows),
        "all_corridor_3gap_slack_positive": all(row["corridor_3gap_slack"] > 0 for row in rows),
        "min_corridor_3gap_slack": min(row["corridor_3gap_slack"] for row in rows) if rows else 0,
        "max_phase_bridge_gap_over_gap": max(row["phase_bridge_gap"] / row["gap_ell"] for row in rows) if rows else 0.0,
        "all_phase_bridges_within_2gap": all(row["phase_bridge_within_2gap"] for row in rows),
        "all_three_components_below_gap_count": sum(1 for row in rows if row["all_three_components_below_gap"]),
        "component_excess_row_count": sum(1 for row in rows if row["total_component_excess_over_gap"] > 0),
        "max_total_component_excess_over_gap": max(row["total_component_excess_over_gap"] for row in rows) if rows else 0,
        "min_other_component_spare_after_excess": min(row["other_component_spare_after_excess"] for row in rows) if rows else 0,
        "corridor_phase_budget_bound_proved": False,
        "phase_bridge_pdec_excluded_globally": False,
        "row_column_unconditional_closed": False,
    }
    ledger = {
        "aggregate": aggregate,
        "phase_budget_rows": rows,
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    result = {
        "certificate_type": (
            "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_"
            "corridor_phase_budget_router"
        ),
        "status": "corridor_phase_budget_identity_closed_current_sweep_global_bound_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_sweep_not_used_as_global_proof": True,
        "aggregate": aggregate,
        "phase_budget_rows": rows,
        "corridor_phase_budget_bound_proved": False,
        "phase_bridge_pdec_excluded_globally": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": "ShortGapRepairCorridorBoundOrCorridorPDECExclusion",
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "本步把短走廊不等式分解为精确三分量身份 "
            "`p_delay = generator_right_depth + phase_bridge_gap + fill_left_depth`。"
            f"当前三条身份全部闭合，`3*gap_ell` 最小余量为 {aggregate['min_corridor_3gap_slack']}。"
            "唯一分量超标发生在 `gap_ell=31` 的 phase bridge，但被另两个深度分量余量吸收。"
            "全局剩余是证明三分量预算界，或把 phase bridge 超标登记并排斥为 PhaseBridge-PDEC/SAE。"
        ),
    }
    result["source_hashes"] = {
        "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_corridor_phase_budget_router.py": sha256(
            Path(__file__).resolve()
        ),
        "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-gap-fill-pair-ledger.json": sha256(
            pair_ledger
        ),
        "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-gap-repair-corridor-ledger.json": sha256(
            corridor_ledger
        ),
        "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-corridor-phase-budget-ledger.json": sha256(
            OUT_LEDGER
        ),
    }
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow selector H lower corridor phase budget router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"phase_budget_row_count={agg['phase_budget_row_count']}",
        f"all_phase_budget_identities_closed={fmt_bool(agg['all_phase_budget_identities_closed'])}",
        f"all_corridor_3gap_slack_positive={fmt_bool(agg['all_corridor_3gap_slack_positive'])}",
        f"min_corridor_3gap_slack={agg['min_corridor_3gap_slack']}",
        f"max_phase_bridge_gap_over_gap={agg['max_phase_bridge_gap_over_gap']:.12f}",
        f"all_phase_bridges_within_2gap={fmt_bool(agg['all_phase_bridges_within_2gap'])}",
        f"component_excess_row_count={agg['component_excess_row_count']}",
        f"min_other_component_spare_after_excess={agg['min_other_component_spare_after_excess']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 三分量身份",
        "",
        "| gap ell | generator phase | fill phase | gen right | bridge gap | fill left | total | 3gap slack | excess |",
        "| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in result["phase_budget_rows"]:
        lines.append(
            f"| {row['gap_ell']} | `{row['generator_phase']}` | `{row['fill_phase']}` | "
            f"{row['generator_right_depth']} | {row['phase_bridge_gap']} | {row['fill_left_depth']} | "
            f"{row['phase_budget_identity_total']} | {row['corridor_3gap_slack']} | "
            f"{row['total_component_excess_over_gap']} |"
        )
    lines.extend(
        [
            "",
            "## 2. 预算解释",
            "",
            "- `p_delay` 被完全解释为生成相位右深度、两相位区间间隙、填充相位左深度三项之和。",
            "- `gap_ell=31` 是唯一出现单分量超标的行：phase bridge 超过一个 `gap_ell`，但总预算仍保留 13 余量。",
            "- 若全局出现短走廊失效，必须表现为三分量预算无法吸收的 phase bridge/深度超标，可登记为 PhaseBridge-PDEC/SAE。",
            "",
            "## 3. 下一步",
            "",
            f"- 主攻：`{result['next_direct_attack_target']}`。",
            "- 对 phase bridge gap 建立 CRT/slot 控制：证明其总能被左右深度余量吸收，或登记不可吸收超标原子。",
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
    parser.add_argument("--pair-ledger", type=Path, default=PAIR_LEDGER)
    parser.add_argument("--corridor-ledger", type=Path, default=CORRIDOR_LEDGER)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    pair_ledger = args.pair_ledger if args.pair_ledger.is_absolute() else ROOT / args.pair_ledger
    corridor_ledger = args.corridor_ledger if args.corridor_ledger.is_absolute() else ROOT / args.corridor_ledger
    result = build_result(pair_ledger, corridor_ledger)
    write_markdown(result)
    result["source_hashes"][
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-corridor-phase-budget-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "phase_budget_row_count": result["aggregate"]["phase_budget_row_count"],
                "all_phase_budget_identities_closed": result["aggregate"]["all_phase_budget_identities_closed"],
                "min_corridor_3gap_slack": result["aggregate"]["min_corridor_3gap_slack"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
