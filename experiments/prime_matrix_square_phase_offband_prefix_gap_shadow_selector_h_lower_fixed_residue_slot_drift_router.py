#!/usr/bin/env python3
"""审计固定残基复现包是否退化为槽位漂移。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_fixed_residue_slot_drift_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-fixed-residue-slot-drift-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-selector-h-lower-fixed-residue-slot-drift-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-fixed-residue-slot-drift-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-fixed-residue-slot-drift-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SPLIT_LEDGER = DATA / (
    "square-phase-offband-prefix-gap-shadow-selector-h-lower-"
    "unique-representative-persistence-split-ledger.json"
)
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-fixed-residue-slot-drift-ledger.json"
OUT_JSON = DOCS / (
    "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-"
    "fixed-residue-slot-drift-router.json"
)
OUT_MD = DOCS / (
    "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-"
    "fixed-residue-slot-drift-router.md"
)

MAIN_TARGET = "UniqueRepresentativePersistenceSplitToFixedResiduePDECOrMovingResidueSAE"
NEXT_TARGET = "FixedResidueSlotDriftColumnCRTOrMovingResidueShapeSAE"


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


def parse_slot(slot_key: str) -> tuple[int, int, int]:
    """解析 b:u:ell 槽键。"""
    b_value, u_value, ell_value = slot_key.split(":")
    return int(b_value), int(u_value), int(ell_value)


def recurrence_pair(packet: dict[str, Any]) -> dict[str, Any]:
    """把一个固定残基复现包写成两点槽漂移记录。"""
    examples = sorted(packet["examples"], key=lambda item: int(item["p"]))
    if len(examples) != 2:
        raise ValueError(f"expected two examples for {packet['key']}")
    left, right = examples
    left_slot = parse_slot(left["slot_keys"][0])
    right_slot = parse_slot(right["slot_keys"][0])
    ell = int(left["ell_tuple"][0])
    p_gap = int(right["p"]) - int(left["p"])
    phase_lo_gap = int(right["phase_p_lo"]) - int(left["phase_p_lo"])
    phase_hi_gap = int(right["phase_p_hi"]) - int(left["phase_p_hi"])
    return {
        "residue_packet_key": packet["key"],
        "ell": ell,
        "crt_residue": int(left["crt_residue"]),
        "p_values": [int(left["p"]), int(right["p"])],
        "p_gap": p_gap,
        "p_gap_over_ell": p_gap // ell,
        "p_gap_divisible_by_ell": p_gap % ell == 0,
        "same_side": str(left["side"]) == str(right["side"]),
        "same_rho": int(left["rho"]) == int(right["rho"]),
        "rho_values": [int(left["rho"]), int(right["rho"])],
        "left_slot_key": left["slot_keys"][0],
        "right_slot_key": right["slot_keys"][0],
        "same_slot_key": left["slot_keys"][0] == right["slot_keys"][0],
        "b_values": [left_slot[0], right_slot[0]],
        "u_values": [left_slot[1], right_slot[1]],
        "b_gap": right_slot[0] - left_slot[0],
        "u_gap": right_slot[1] - left_slot[1],
        "phase_left": [int(left["phase_p_lo"]), int(left["phase_p_hi"])],
        "phase_right": [int(right["phase_p_lo"]), int(right["phase_p_hi"])],
        "phase_lo_gap": phase_lo_gap,
        "phase_hi_gap": phase_hi_gap,
        "phase_lo_gap_minus_p_gap": phase_lo_gap - p_gap,
        "phase_hi_gap_minus_p_gap": phase_hi_gap - p_gap,
        "depth_left": [int(left["left_depth"]), int(left["right_depth"])],
        "depth_right": [int(right["left_depth"]), int(right["right_depth"])],
        "same_depth_signature": [
            int(left["left_depth"]),
            int(left["right_depth"]),
        ]
        == [
            int(right["left_depth"]),
            int(right["right_depth"]),
        ],
        "min_margin": int(packet["min_margin"]),
        "min_crt_minus_phase_width": int(packet["min_crt_minus_phase_width"]),
    }


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "fixed_slot_persistence_empty_current_sweep",
            "status": "closed_on_current_sweep",
            "statement": "After physical deduplication every fixed-slot packet occurs once in the current selector sweep.",
        },
        {
            "name": "fixed_residue_recurrence_is_slot_drift_current_sweep",
            "status": "closed_on_current_sweep",
            "statement": "Every recurrent fixed-residue packet changes its slot key, so recurrence is residue-fixed but slot-moving.",
        },
        {
            "name": "slot_drift_columncrt_exclusion_open",
            "status": "open",
            "statement": "A global proof must exclude the slot-drift family by ColumnCRT/PDEC or transfer it to SAE/Rankin.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    agg = result["aggregate"]
    return [
        {
            "gate": "FixedSlotPersistenceEmpty",
            "closed": agg["fixed_slot_recurrence_count"] == 0,
            "proved": False,
            "meaning": "当前扫描内没有同一 fixed-slot packet 的物理复现。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "FixedResidueRecurrenceIsSlotDrift",
            "closed": agg["all_fixed_residue_recurrences_are_slot_drift"],
            "proved": False,
            "meaning": "12 个固定残基复现包全部换槽，不能作为固定槽图样处理。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "SlotDriftColumnCRTExcluded",
            "closed": False,
            "proved": False,
            "meaning": "仍需证明槽漂移族不能全局持久，或登记明确 ColumnCRT/PDEC。",
            "remaining": "FixedResidueSlotDriftColumnCRT",
        },
        {
            "gate": "MovingResidueShapeSAEBounded",
            "closed": False,
            "proved": False,
            "meaning": "移动残基 shape 仍需 SAE/Rankin 全局界。",
            "remaining": "MovingResidueShapeSAE/Rankin",
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步仍是路由压缩，不关闭全局行/列命题。",
            "remaining": result["next_direct_attack_target"],
        },
    ]


def build_result(split_ledger: Path) -> dict[str, Any]:
    """构造固定残基槽漂移审计结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    split = load_json(split_ledger)
    split_agg = split["aggregate"]
    fixed_packets = split["top_fixed_residue_recurrent_packets"]
    expected_count = int(split_agg["recurrent_fixed_residue_packet_count_distinct_p"])
    if len(fixed_packets) != expected_count:
        raise RuntimeError("fixed residue packet list is truncated; rerun split router with a larger tight limit")

    pair_rows = [recurrence_pair(packet) for packet in fixed_packets]
    p_gap_hist = Counter(str(row["p_gap_over_ell"]) for row in pair_rows)
    ell_hist = Counter(str(row["ell"]) for row in pair_rows)
    aggregate = {
        "split_ledger": str(split_ledger.relative_to(ROOT)),
        "raw_record_count": int(split_agg["raw_record_count"]),
        "physical_record_count": int(split_agg["physical_record_count"]),
        "slot_packet_count": int(split_agg["slot_packet_count"]),
        "fixed_slot_recurrence_count": int(split_agg["physical_record_count"]) - int(split_agg["slot_packet_count"]),
        "fixed_residue_recurrent_packet_count": expected_count,
        "pair_row_count": len(pair_rows),
        "all_fixed_residue_recurrences_are_one_slot": all(row["ell"] == parse_slot(row["left_slot_key"])[2] for row in pair_rows),
        "all_fixed_residue_recurrences_are_slot_drift": all(not row["same_slot_key"] for row in pair_rows),
        "all_p_gaps_divisible_by_ell": all(row["p_gap_divisible_by_ell"] for row in pair_rows),
        "same_rho_pair_count": sum(1 for row in pair_rows if row["same_rho"]),
        "same_depth_signature_pair_count": sum(1 for row in pair_rows if row["same_depth_signature"]),
        "min_p_gap_over_ell": min(row["p_gap_over_ell"] for row in pair_rows),
        "max_p_gap_over_ell": max(row["p_gap_over_ell"] for row in pair_rows),
        "p_gap_over_ell_histogram": {key: p_gap_hist[key] for key in sorted(p_gap_hist, key=int)},
        "ell_histogram": {key: ell_hist[key] for key in sorted(ell_hist, key=int)},
        "fixed_residue_slot_drift_excluded_globally": False,
        "moving_residue_sae_rankin_bound_proved": False,
        "row_column_unconditional_closed": False,
    }

    ledger = {
        "aggregate": aggregate,
        "fixed_residue_slot_drift_pairs": pair_rows,
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    result = {
        "certificate_type": (
            "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_"
            "fixed_residue_slot_drift_router"
        ),
        "status": "fixed_residue_recurrence_reduced_to_slot_drift_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_sweep_not_used_as_global_proof": True,
        "aggregate": aggregate,
        "fixed_residue_slot_drift_pairs": pair_rows,
        "fixed_residue_slot_drift_excluded_globally": False,
        "moving_residue_sae_rankin_bound_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "plain_conclusion": (
            "本步检查固定残基复现包的槽位持久性：物理记录数等于 fixed-slot packet 数，"
            "因此当前扫描内没有 fixed-slot 复现。12 个跨不同 P 复现的固定残基包全部换槽，"
            f"`p` 间距均为对应 `ell` 的整数倍，最小倍数 {aggregate['min_p_gap_over_ell']}，"
            f"最大倍数 {aggregate['max_p_gap_over_ell']}。剩余硬点进一步压成固定残基但槽位漂移的 "
            "ColumnCRT/PDEC，外加移动残基 shape 的 SAE/Rankin 界。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    result["source_hashes"] = {
        "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_fixed_residue_slot_drift_router.py": sha256(
            Path(__file__).resolve()
        ),
        "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-unique-representative-persistence-split-ledger.json": sha256(
            split_ledger
        ),
        "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-fixed-residue-slot-drift-ledger.json": sha256(
            OUT_LEDGER
        ),
    }
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow selector H lower fixed-residue slot-drift router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"physical_record_count={agg['physical_record_count']}",
        f"slot_packet_count={agg['slot_packet_count']}",
        f"fixed_slot_recurrence_count={agg['fixed_slot_recurrence_count']}",
        f"fixed_residue_recurrent_packet_count={agg['fixed_residue_recurrent_packet_count']}",
        f"all_fixed_residue_recurrences_are_slot_drift={fmt_bool(agg['all_fixed_residue_recurrences_are_slot_drift'])}",
        f"all_p_gaps_divisible_by_ell={fmt_bool(agg['all_p_gaps_divisible_by_ell'])}",
        f"p_gap_over_ell_histogram={agg['p_gap_over_ell_histogram']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 复现对",
        "",
        "| residue packet | ell | p values | gap/ell | rho | slots | b gap | u gap | depth | margin |",
        "| --- | ---: | --- | ---: | --- | --- | ---: | ---: | --- | ---: |",
    ]
    for row in result["fixed_residue_slot_drift_pairs"]:
        lines.append(
            f"| `{row['residue_packet_key']}` | {row['ell']} | `{row['p_values']}` | "
            f"{row['p_gap_over_ell']} | `{row['rho_values']}` | "
            f"`{row['left_slot_key']} -> {row['right_slot_key']}` | "
            f"{row['b_gap']} | {row['u_gap']} | `{row['depth_left']} -> {row['depth_right']}` | "
            f"{row['min_margin']} |"
        )

    lines.extend(
        [
            "",
            "## 2. 结构判断",
            "",
            "- 固定残基复现不是 fixed-slot 复现；每一对都改变 `b:u:ell` 槽键。",
            "- 固定残基只说明 `P` 落在同一个低模余类；真正需要排斥的是槽位随 `P` 漂移时的 ColumnCRT 兼容链。",
            "- 当前没有获得终端矛盾，仍需全局证明 slot-drift 不能无限复现，或把失败形态登记为明确 PDEC。",
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
            "- 对 12 个固定残基换槽对建立 ColumnCRT 相位宽度上界。",
            "- 并行保留 37 个移动残基 shape 的 SAE/Rankin 汇总账本。",
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
    parser.add_argument("--split-ledger", type=Path, default=SPLIT_LEDGER)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    split_ledger = args.split_ledger if args.split_ledger.is_absolute() else ROOT / args.split_ledger
    result = build_result(split_ledger)
    write_markdown(result)
    result["source_hashes"][
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-fixed-residue-slot-drift-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "fixed_slot_recurrence_count": result["aggregate"]["fixed_slot_recurrence_count"],
                "fixed_residue_recurrent_packet_count": result["aggregate"][
                    "fixed_residue_recurrent_packet_count"
                ],
                "all_fixed_residue_recurrences_are_slot_drift": result["aggregate"][
                    "all_fixed_residue_recurrences_are_slot_drift"
                ],
                "p_gap_over_ell_histogram": result["aggregate"]["p_gap_over_ell_histogram"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
