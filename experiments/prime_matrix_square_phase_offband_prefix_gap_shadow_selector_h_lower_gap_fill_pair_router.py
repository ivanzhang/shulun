#!/usr/bin/env python3
"""把端点运动缺口压成生成-填充二元组。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_gap_fill_pair_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-gap-fill-pair-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-selector-h-lower-gap-fill-pair-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-gap-fill-pair-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-gap-fill-pair-router.md
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

MOTION_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-endpoint-motion-gap-ledger.json"
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-gap-fill-pair-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-gap-fill-pair-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-gap-fill-pair-router.md"

NEXT_TARGET = "ImmediateGapRepairBoundOrGapFillPairPDECExclusion"


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def parse_slot(record: dict[str, Any]) -> tuple[int, int, int]:
    """解析单槽键 `b:u:ell`。"""
    return tuple(map(int, record["slot_keys"][0].split(":")))  # type: ignore[return-value]


def gap_pair_key(row: dict[str, Any]) -> str:
    """生成缺口二元组 PDEC 键。"""
    return "|".join(
        [
            f"dir={row['endpoint_direction']}",
            f"gen={row['generator_ell']}",
            f"gap={row['gap_ell']}",
            f"fill={row['fill_ell']}",
            f"sides={row['generator_side']}->{row['fill_side']}",
            f"dp={row['p_delay']}",
            f"db={row['delta_b']}",
            f"du={row['delta_u']}",
            f"dr={row['delta_residue']}",
        ]
    )


def build_pair_rows(motion: dict[str, Any]) -> list[dict[str, Any]]:
    """按首次激活序列构造缺口生成-填充二元组。"""
    activations = motion["activation_rows"]
    by_ell = {int(row["ell"]): row for row in activations}
    index_by_ell = {int(row["ell"]): index for index, row in enumerate(activations)}
    active: set[int] = set()
    rows = []
    for index, generator in enumerate(activations):
        ell = int(generator["ell"])
        previous_min = min(active) if active else None
        previous_max = max(active) if active else None
        active.add(ell)
        snapshot = motion["activation_snapshots"][index]
        missing = list(map(int, snapshot["missing_internal_prime_ells"]))
        if not missing:
            continue
        if previous_max is not None and ell > previous_max:
            direction = "upper"
            previous_endpoint = previous_max
        elif previous_min is not None and ell < previous_min:
            direction = "lower"
            previous_endpoint = previous_min
        else:
            direction = "internal"
            previous_endpoint = None
        for gap_ell in missing:
            filler = by_ell[gap_ell]
            filler_index = index_by_ell[gap_ell]
            gen_b, gen_u, gen_slot_ell = parse_slot(generator)
            fill_b, fill_u, fill_slot_ell = parse_slot(filler)
            row = {
                "gap_ell": gap_ell,
                "endpoint_direction": direction,
                "previous_endpoint_ell": previous_endpoint,
                "generator_activation_index": index,
                "fill_activation_index": filler_index,
                "activation_rank_delay": filler_index - index,
                "generator_p": int(generator["p"]),
                "fill_p": int(filler["p"]),
                "p_delay": int(filler["p"]) - int(generator["p"]),
                "generator_ell": ell,
                "fill_ell": int(filler["ell"]),
                "generator_side": str(generator["side"]),
                "fill_side": str(filler["side"]),
                "generator_rho": int(generator["rho"]),
                "fill_rho": int(filler["rho"]),
                "generator_residue": int(generator["crt_residue"]),
                "fill_residue": int(filler["crt_residue"]),
                "delta_residue": int(filler["crt_residue"]) - int(generator["crt_residue"]),
                "generator_slot": list(generator["slot_keys"]),
                "fill_slot": list(filler["slot_keys"]),
                "generator_b": gen_b,
                "generator_u": gen_u,
                "generator_slot_ell": gen_slot_ell,
                "fill_b": fill_b,
                "fill_u": fill_u,
                "fill_slot_ell": fill_slot_ell,
                "delta_b": fill_b - gen_b,
                "delta_u": fill_u - gen_u,
                "generator_margin": int(generator["margin"]),
                "fill_margin": int(filler["margin"]),
                "generator_depth": [int(generator["left_depth"]), int(generator["right_depth"])],
                "fill_depth": [int(filler["left_depth"]), int(filler["right_depth"])],
                "post_fill_exact_interval": motion["activation_snapshots"][filler_index]["is_exact_prime_interval"],
            }
            row["gap_fill_pair_key"] = gap_pair_key(row)
            rows.append(row)
    return rows


def build_result(motion_ledger: Path) -> dict[str, Any]:
    """构造缺口填充二元组结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    motion = load_json(motion_ledger)
    pair_rows = build_pair_rows(motion)
    keys = [row["gap_fill_pair_key"] for row in pair_rows]
    rank_delays = [int(row["activation_rank_delay"]) for row in pair_rows]
    p_delays = [int(row["p_delay"]) for row in pair_rows]
    aggregate = {
        "motion_ledger": str(motion_ledger.relative_to(ROOT)),
        "gap_pair_count": len(pair_rows),
        "unique_gap_fill_pair_key_count": len(set(keys)),
        "repeated_gap_fill_pair_key_count": len(keys) - len(set(keys)),
        "all_gaps_have_unique_pair_key_current_sweep": len(keys) == len(set(keys)),
        "all_gaps_are_next_activation_repairs": all(delay == 1 for delay in rank_delays),
        "all_repairs_restore_exact_interval": all(bool(row["post_fill_exact_interval"]) for row in pair_rows),
        "max_activation_rank_delay": max(rank_delays) if rank_delays else 0,
        "max_p_delay": max(p_delays) if p_delays else 0,
        "gap_ells": sorted({int(row["gap_ell"]) for row in pair_rows}),
        "endpoint_directions": sorted({str(row["endpoint_direction"]) for row in pair_rows}),
        "gap_fill_pair_bound_proved": False,
        "gap_fill_pair_pdec_excluded_globally": False,
        "row_column_unconditional_closed": False,
    }
    ledger = {
        "aggregate": aggregate,
        "gap_fill_pair_rows": pair_rows,
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    result = {
        "certificate_type": (
            "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_"
            "gap_fill_pair_router"
        ),
        "status": "gap_fill_pairs_materialized_immediate_repair_current_sweep_global_bound_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_sweep_not_used_as_global_proof": True,
        "aggregate": aggregate,
        "gap_fill_pair_rows": pair_rows,
        "immediate_gap_repair_bound_proved": False,
        "gap_fill_pair_pdec_excluded_globally": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": "EndpointMotionGapFillBoundOrGapPDECExclusion",
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "本步把三次端点运动缺口都压成生成-填充二元组。当前扫描中每个缺口都由下一次 `ell` "
            "首次激活立刻修复，且修复后活跃 `ell` 集合重新成为连续素数带；三个完整 pair key 互异，"
            "没有当前复现。全局剩余是证明 immediate repair 机制，或排斥持久 GapFillPair-PDEC。"
        ),
    }
    result["source_hashes"] = {
        "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_gap_fill_pair_router.py": sha256(
            Path(__file__).resolve()
        ),
        "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-endpoint-motion-gap-ledger.json": sha256(
            motion_ledger
        ),
        "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-gap-fill-pair-ledger.json": sha256(
            OUT_LEDGER
        ),
    }
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow selector H lower gap fill pair router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"gap_pair_count={agg['gap_pair_count']}",
        f"unique_gap_fill_pair_key_count={agg['unique_gap_fill_pair_key_count']}",
        f"repeated_gap_fill_pair_key_count={agg['repeated_gap_fill_pair_key_count']}",
        f"all_gaps_are_next_activation_repairs={fmt_bool(agg['all_gaps_are_next_activation_repairs'])}",
        f"all_repairs_restore_exact_interval={fmt_bool(agg['all_repairs_restore_exact_interval'])}",
        f"max_activation_rank_delay={agg['max_activation_rank_delay']}",
        f"max_p_delay={agg['max_p_delay']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 缺口生成-填充二元组",
        "",
        "| gap ell | direction | generator | filler | rank delay | P delay | slot delta | residue delta | post-fill interval |",
        "| ---: | --- | --- | --- | ---: | ---: | --- | ---: | ---: |",
    ]
    for row in result["gap_fill_pair_rows"]:
        lines.append(
            f"| {row['gap_ell']} | `{row['endpoint_direction']}` | "
            f"`{row['generator_p']}:{row['generator_side']}:{row['generator_ell']}` | "
            f"`{row['fill_p']}:{row['fill_side']}:{row['fill_ell']}` | "
            f"{row['activation_rank_delay']} | {row['p_delay']} | "
            f"`db={row['delta_b']},du={row['delta_u']}` | {row['delta_residue']} | "
            f"`{fmt_bool(row['post_fill_exact_interval'])}` |"
        )
    lines.extend(
        [
            "",
            "## 2. PDEC 键",
            "",
            "| gap ell | key |",
            "| ---: | --- |",
        ]
    )
    for row in result["gap_fill_pair_rows"]:
        lines.append(f"| {row['gap_ell']} | `{row['gap_fill_pair_key']}` |")
    lines.extend(
        [
            "",
            "## 3. 结构结论",
            "",
            "- 当前缺口没有形成长链：所有缺口的激活序列延迟均为 1。",
            "- 每次填充后立即恢复连续素数带，因此持久缺口若存在，必须破坏 immediate-repair 机制。",
            "- 三个完整 pair key 当前互异；全局复现将进入显式 GapFillPair-PDEC。",
            "",
            "## 4. 下一步",
            "",
            f"- 主攻：`{result['next_direct_attack_target']}`。",
            "- 将 `rank delay=1` 的局部事实提升为端点跳跃的结构约束，或证明违反者必产生重复 pair key / SAE 稀疏化。",
            "",
            "## 5. 依赖哈希",
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
    parser.add_argument("--motion-ledger", type=Path, default=MOTION_LEDGER)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    motion_ledger = args.motion_ledger if args.motion_ledger.is_absolute() else ROOT / args.motion_ledger
    result = build_result(motion_ledger)
    write_markdown(result)
    result["source_hashes"][
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-gap-fill-pair-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "gap_pair_count": result["aggregate"]["gap_pair_count"],
                "all_gaps_are_next_activation_repairs": result["aggregate"]["all_gaps_are_next_activation_repairs"],
                "all_repairs_restore_exact_interval": result["aggregate"]["all_repairs_restore_exact_interval"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
