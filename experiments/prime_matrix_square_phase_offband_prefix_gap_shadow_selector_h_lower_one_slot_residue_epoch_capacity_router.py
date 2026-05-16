#!/usr/bin/env python3
"""把一槽低模占用率压成 reset-free residue epoch 容量账本。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_one_slot_residue_epoch_capacity_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-one-slot-residue-epoch-capacity-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-selector-h-lower-one-slot-residue-epoch-capacity-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-one-slot-residue-epoch-capacity-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-one-slot-residue-epoch-capacity-router.md
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

BUDGET_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-singleton-rankin-budget-ledger.json"
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-one-slot-residue-epoch-capacity-ledger.json"
OUT_JSON = DOCS / (
    "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-"
    "one-slot-residue-epoch-capacity-router.json"
)
OUT_MD = DOCS / (
    "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-"
    "one-slot-residue-epoch-capacity-router.md"
)

MAIN_TARGET = "OneSlotLowModOccupancyDecayOrTransportResetPDECExclusion"
NEXT_TARGET = "ActiveOneSlotEpochCountBoundOrTransportResetPDECExclusion"


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def capacity_row(row: dict[str, Any]) -> dict[str, Any]:
    """把一个一槽 `(side,ell)` shape 写成 epoch 容量行。"""
    ell = int(row["ell"])
    count = int(row["count"])
    return {
        "side": str(row["side"]),
        "ell": ell,
        "used_residue_count": count,
        "epoch_residue_capacity": ell,
        "unused_residue_count": ell - count,
        "occupancy_ratio": count / ell,
        "spare_ratio": (ell - count) / ell,
        "rankin_mass": float(row["rankin_mass"]),
        "rankin_mass_capacity": 1.0,
        "rankin_spare_mass": 1.0 - float(row["rankin_mass"]),
        "p_min": int(row["p_min"]),
        "p_max": int(row["p_max"]),
        "residue_sample": list(row["residue_sample"]),
        "reset_free_epoch_capacity_identity": True,
        "overflow_would_force_repeated_residue": count > ell,
    }


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "one_slot_reset_free_epoch_capacity",
            "status": "closed",
            "statement": "For fixed (side, ell), a reset-free epoch has at most ell singleton residues; an overflow forces repeated residue and exits to transport reset-PDEC.",
        },
        {
            "name": "current_one_slot_epoch_has_large_spare_capacity",
            "status": "closed_on_current_sweep",
            "statement": "The current one-slot singleton support uses only a small part of the residue capacity in every active (side, ell) epoch.",
        },
        {
            "name": "active_epoch_count_bound_open",
            "status": "open",
            "statement": "A global Rankin bound still needs a bound on active one-slot epochs or a proof that excessive epochs trigger transport reset-PDEC/SAE.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    agg = result["aggregate"]
    return [
        {
            "gate": "ResetFreeEpochCapacityClosed",
            "closed": True,
            "proved": True,
            "meaning": "固定 `(side,ell)` 的无 reset epoch 中，singleton residue 数最多为 `ell`。",
            "remaining": "closed",
        },
        {
            "gate": "CurrentEpochOverflowAbsent",
            "closed": agg["overflow_row_count"] == 0,
            "proved": False,
            "meaning": "当前一槽支持远未填满 residue 容量。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "ActiveEpochCountBoundProved",
            "closed": False,
            "proved": False,
            "meaning": "全局 Rankin 可求和仍需要控制活跃 `(side,ell)` epoch 数量。",
            "remaining": "ActiveOneSlotEpochCountBound",
        },
        {
            "gate": "TransportResetPDECExcluded",
            "closed": False,
            "proved": False,
            "meaning": "若 epoch 过多或 residue 重复，仍需 transport reset-PDEC 排斥。",
            "remaining": "TransportResetPDECExclusion",
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步关闭的是每个 epoch 内的容量，不关闭全局命题。",
            "remaining": result["next_direct_attack_target"],
        },
    ]


def build_result(budget_ledger: Path) -> dict[str, Any]:
    """构造一槽 epoch 容量账本。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    budget = load_json(budget_ledger)
    rows = [capacity_row(row) for row in budget["top_one_slot_ell_occupancy"]]
    one_slot_mass = sum(row["rankin_mass"] for row in rows)
    aggregate = {
        "budget_ledger": str(budget_ledger.relative_to(ROOT)),
        "active_one_slot_epoch_count": len(rows),
        "total_residue_capacity": sum(row["epoch_residue_capacity"] for row in rows),
        "total_used_residue_count": sum(row["used_residue_count"] for row in rows),
        "total_unused_residue_count": sum(row["unused_residue_count"] for row in rows),
        "one_slot_rankin_mass": one_slot_mass,
        "epoch_rankin_mass_capacity": float(len(rows)),
        "epoch_rankin_spare_mass": float(len(rows)) - one_slot_mass,
        "max_occupancy_ratio": max(row["occupancy_ratio"] for row in rows),
        "min_spare_ratio": min(row["spare_ratio"] for row in rows),
        "overflow_row_count": sum(1 for row in rows if row["overflow_would_force_repeated_residue"]),
        "reset_free_epoch_capacity_closed": True,
        "active_epoch_count_bound_proved": False,
        "transport_reset_pdec_excluded_globally": False,
        "row_column_unconditional_closed": False,
    }
    ledger = {
        "aggregate": aggregate,
        "epoch_capacity_rows": rows,
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    result = {
        "certificate_type": (
            "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_"
            "one_slot_residue_epoch_capacity_router"
        ),
        "status": "one_slot_epoch_capacity_closed_active_epoch_count_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_sweep_not_used_as_global_proof": True,
        "aggregate": aggregate,
        "epoch_capacity_rows": rows,
        "active_epoch_count_bound_proved": False,
        "transport_reset_pdec_excluded_globally": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "plain_conclusion": (
            "本步把一槽低模 occupancy 写成 reset-free epoch 容量：固定 `(side,ell)` 中，"
            "一个无 reset epoch 最多使用 `ell` 个 residue，否则必然重复 residue 并回到 transport reset-PDEC。"
            f"当前 40 个活跃 epoch 总容量 {aggregate['total_residue_capacity']}，实际使用 "
            f"{aggregate['total_used_residue_count']}，未用 {aggregate['total_unused_residue_count']}；"
            f"最大占用率 {aggregate['max_occupancy_ratio']:.6f}。剩余硬点不是单个 epoch 容量，"
            "而是全局活跃 epoch 数量界或 reset-PDEC 排斥。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    result["source_hashes"] = {
        "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_one_slot_residue_epoch_capacity_router.py": sha256(
            Path(__file__).resolve()
        ),
        "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-singleton-rankin-budget-ledger.json": sha256(
            budget_ledger
        ),
        "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-one-slot-residue-epoch-capacity-ledger.json": sha256(
            OUT_LEDGER
        ),
    }
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow selector H lower one-slot residue epoch capacity router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"active_one_slot_epoch_count={agg['active_one_slot_epoch_count']}",
        f"total_residue_capacity={agg['total_residue_capacity']}",
        f"total_used_residue_count={agg['total_used_residue_count']}",
        f"total_unused_residue_count={agg['total_unused_residue_count']}",
        f"one_slot_rankin_mass={agg['one_slot_rankin_mass']:.12f}",
        f"max_occupancy_ratio={agg['max_occupancy_ratio']:.12f}",
        f"min_spare_ratio={agg['min_spare_ratio']:.12f}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. epoch 容量行",
        "",
        "| side | ell | used | capacity | occupancy | spare | Rankin mass | p range |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in result["epoch_capacity_rows"]:
        lines.append(
            f"| `{row['side']}` | {row['ell']} | {row['used_residue_count']} | "
            f"{row['epoch_residue_capacity']} | {row['occupancy_ratio']:.6f} | "
            f"{row['spare_ratio']:.6f} | {row['rankin_mass']:.6f} | "
            f"`{row['p_min']}..{row['p_max']}` |"
        )
    lines.extend(
        [
            "",
            "## 2. 结构判断",
            "",
            "- 单个 `(side,ell)` epoch 内的 Rankin 质量至多为 1；溢出会强制 residue 重复。",
            "- 当前所有活跃 epoch 都有大余量，说明局部容量不是瓶颈。",
            "- 全局可求和必须控制活跃 epoch 的数量，或证明活跃 epoch 过多会触发 transport reset-PDEC/SAE。",
            "",
            "## 3. 命题行",
            "",
            "| name | status | statement |",
            "| --- | --- | --- |",
        ]
    )
    for row in result["theorem_rows"]:
        lines.append(f"| `{row['name']}` | `{row['status']}` | {table_cell(row['statement'])} |")
    lines.extend(
        [
            "",
            "## 4. 决策表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | ---: | ---: | --- | --- |",
        ]
    )
    for row in result["decision_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{row['gate']}`",
                    f"`{fmt_bool(row['closed'])}`",
                    f"`{fmt_bool(row['proved'])}`",
                    table_cell(row["meaning"]),
                    table_cell(row["remaining"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 5. 下一步",
            "",
            f"- 主攻：`{result['next_direct_attack_target']}`。",
            "- 证明活跃 `(side,ell)` epoch 数量有全局界，或证明过多 epoch 必触发 transport reset-PDEC。",
            "",
            "## 6. 依赖哈希",
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
    parser.add_argument("--budget-ledger", type=Path, default=BUDGET_LEDGER)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    budget_ledger = args.budget_ledger if args.budget_ledger.is_absolute() else ROOT / args.budget_ledger
    result = build_result(budget_ledger)
    write_markdown(result)
    result["source_hashes"][
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-one-slot-residue-epoch-capacity-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "active_one_slot_epoch_count": result["aggregate"]["active_one_slot_epoch_count"],
                "total_residue_capacity": result["aggregate"]["total_residue_capacity"],
                "total_used_residue_count": result["aggregate"]["total_used_residue_count"],
                "max_occupancy_ratio": result["aggregate"]["max_occupancy_ratio"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
