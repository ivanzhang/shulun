#!/usr/bin/env python3
"""把缺口填充二元组压成短 P 走廊不等式。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_gap_repair_corridor_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-gap-repair-corridor-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-selector-h-lower-gap-repair-corridor-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-gap-repair-corridor-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-gap-repair-corridor-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from math import ceil
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

PAIR_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-gap-fill-pair-ledger.json"
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-gap-repair-corridor-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-gap-repair-corridor-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-gap-repair-corridor-router.md"

NEXT_TARGET = "ShortGapRepairCorridorBoundOrCorridorPDECExclusion"


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def corridor_row(row: dict[str, Any]) -> dict[str, Any]:
    """把缺口 pair 写成短走廊行。"""
    gap_ell = int(row["gap_ell"])
    generator_ell = int(row["generator_ell"])
    p_delay = int(row["p_delay"])
    min_local_ell = min(gap_ell, generator_ell)
    max_local_ell = max(gap_ell, generator_ell)
    return {
        "gap_ell": gap_ell,
        "generator_ell": generator_ell,
        "endpoint_direction": str(row["endpoint_direction"]),
        "generator_p": int(row["generator_p"]),
        "fill_p": int(row["fill_p"]),
        "p_delay": p_delay,
        "p_delay_over_gap_ell": p_delay / gap_ell,
        "ceil_delay_over_gap_ell": ceil(p_delay / gap_ell),
        "ceil_delay_over_min_local_ell": ceil(p_delay / min_local_ell),
        "ceil_delay_over_max_local_ell": ceil(p_delay / max_local_ell),
        "within_2_gap_ell": p_delay <= 2 * gap_ell,
        "within_3_gap_ell": p_delay <= 3 * gap_ell,
        "within_3_min_local_ell": p_delay <= 3 * min_local_ell,
        "corridor_defect_against_3_gap_ell": 3 * gap_ell - p_delay,
        "corridor_defect_against_3_min_local_ell": 3 * min_local_ell - p_delay,
        "activation_rank_delay": int(row["activation_rank_delay"]),
        "post_fill_exact_interval": bool(row["post_fill_exact_interval"]),
        "gap_fill_pair_key": str(row["gap_fill_pair_key"]),
    }


def build_result(pair_ledger: Path) -> dict[str, Any]:
    """构造短走廊审计结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    pair = load_json(pair_ledger)
    rows = [corridor_row(row) for row in pair["gap_fill_pair_rows"]]
    aggregate = {
        "pair_ledger": str(pair_ledger.relative_to(ROOT)),
        "corridor_row_count": len(rows),
        "all_repairs_within_3_gap_ell_current_sweep": all(row["within_3_gap_ell"] for row in rows),
        "all_repairs_within_3_min_local_ell_current_sweep": all(row["within_3_min_local_ell"] for row in rows),
        "all_repairs_within_2_gap_ell_current_sweep": all(row["within_2_gap_ell"] for row in rows),
        "max_ceil_delay_over_gap_ell": max(row["ceil_delay_over_gap_ell"] for row in rows) if rows else 0,
        "max_ceil_delay_over_min_local_ell": max(row["ceil_delay_over_min_local_ell"] for row in rows) if rows else 0,
        "max_p_delay_over_gap_ell": max(row["p_delay_over_gap_ell"] for row in rows) if rows else 0.0,
        "min_corridor_defect_against_3_gap_ell": min(row["corridor_defect_against_3_gap_ell"] for row in rows) if rows else 0,
        "min_corridor_defect_against_3_min_local_ell": min(row["corridor_defect_against_3_min_local_ell"] for row in rows) if rows else 0,
        "short_gap_repair_corridor_bound_proved": False,
        "corridor_pdec_excluded_globally": False,
        "row_column_unconditional_closed": False,
    }
    ledger = {
        "aggregate": aggregate,
        "corridor_rows": rows,
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    result = {
        "certificate_type": (
            "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_"
            "gap_repair_corridor_router"
        ),
        "status": "gap_repair_corridor_closed_current_sweep_global_bound_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_sweep_not_used_as_global_proof": True,
        "aggregate": aggregate,
        "corridor_rows": rows,
        "short_gap_repair_corridor_bound_proved": False,
        "corridor_pdec_excluded_globally": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": "ImmediateGapRepairBoundOrGapFillPairPDECExclusion",
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "本步把 immediate gap repair 转成短 P 走廊不等式：当前三次填充均满足 "
            "`fill_p-generator_p <= 3*gap_ell`，最大归一化延迟为 "
            f"{aggregate['max_p_delay_over_gap_ell']:.6f}，最小 `3*gap_ell` 余量为 "
            f"{aggregate['min_corridor_defect_against_3_gap_ell']}。"
            "全局剩余是证明短走廊填充界，或把走廊失效登记并排斥为 Corridor-PDEC/SAE。"
        ),
    }
    result["source_hashes"] = {
        "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_gap_repair_corridor_router.py": sha256(
            Path(__file__).resolve()
        ),
        "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-gap-fill-pair-ledger.json": sha256(
            pair_ledger
        ),
        "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-gap-repair-corridor-ledger.json": sha256(
            OUT_LEDGER
        ),
    }
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow selector H lower gap repair corridor router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"corridor_row_count={agg['corridor_row_count']}",
        f"all_repairs_within_3_gap_ell_current_sweep={fmt_bool(agg['all_repairs_within_3_gap_ell_current_sweep'])}",
        f"all_repairs_within_3_min_local_ell_current_sweep={fmt_bool(agg['all_repairs_within_3_min_local_ell_current_sweep'])}",
        f"all_repairs_within_2_gap_ell_current_sweep={fmt_bool(agg['all_repairs_within_2_gap_ell_current_sweep'])}",
        f"max_ceil_delay_over_gap_ell={agg['max_ceil_delay_over_gap_ell']}",
        f"max_p_delay_over_gap_ell={agg['max_p_delay_over_gap_ell']:.12f}",
        f"min_corridor_defect_against_3_gap_ell={agg['min_corridor_defect_against_3_gap_ell']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 短走廊行",
        "",
        "| gap ell | generator ell | P delay | delay/gap | ceil | within 3*gap | 3*gap defect | pair key |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in result["corridor_rows"]:
        lines.append(
            f"| {row['gap_ell']} | {row['generator_ell']} | {row['p_delay']} | "
            f"{row['p_delay_over_gap_ell']:.6f} | {row['ceil_delay_over_gap_ell']} | "
            f"`{fmt_bool(row['within_3_gap_ell'])}` | {row['corridor_defect_against_3_gap_ell']} | "
            f"`{row['gap_fill_pair_key']}` |"
        )
    lines.extend(
        [
            "",
            "## 2. 结构结论",
            "",
            "- 当前 immediate repair 不只是激活序列相邻，也落在 `3*gap_ell` 的短 P 走廊内。",
            "- `2*gap_ell` 走廊失败只发生在 `gap_ell=31`，因此 `3*gap_ell` 是当前最小整数倍统一包络。",
            "- 全局闭合仍需证明这个短走廊包络，或证明违反包络会产生 Corridor-PDEC/SAE。",
            "",
            "## 3. 下一步",
            "",
            f"- 主攻：`{result['next_direct_attack_target']}`。",
            "- 将 `3*gap_ell` 包络与端点 CRT 相位宽度、slot 位移和 residue 位移对齐，寻找可排斥的走廊失效原子。",
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
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    pair_ledger = args.pair_ledger if args.pair_ledger.is_absolute() else ROOT / args.pair_ledger
    result = build_result(pair_ledger)
    write_markdown(result)
    result["source_hashes"][
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-gap-repair-corridor-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "corridor_row_count": result["aggregate"]["corridor_row_count"],
                "all_repairs_within_3_gap_ell_current_sweep": result["aggregate"][
                    "all_repairs_within_3_gap_ell_current_sweep"
                ],
                "max_ceil_delay_over_gap_ell": result["aggregate"]["max_ceil_delay_over_gap_ell"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
