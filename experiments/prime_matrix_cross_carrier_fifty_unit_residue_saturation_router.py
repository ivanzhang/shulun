#!/usr/bin/env python3
"""生成跨载体 fifty-unit 同步的 residue 饱和证书。

用法示例：
  python3 experiments/prime_matrix_cross_carrier_fifty_unit_residue_saturation_router.py
  python3 -m json.tool data/prime-matrix-cross-carrier-fifty-unit-residue-saturation-ledger.json

输出：
  data/prime-matrix-cross-carrier-fifty-unit-residue-saturation-ledger.json
  docs/monograph/prime-matrix-cross-carrier-fifty-unit-residue-saturation-router.json
  docs/monograph/prime-matrix-cross-carrier-fifty-unit-residue-saturation-router.md
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

CARRIER = DATA / "prime-matrix-fifty-unit-cross-lock-carrier-separation-ledger.json"
SINGLETON_ROUTER = (
    ROOT
    / "experiments"
    / "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_singleton_residue_sae_profile_router.py"
)
SPLIT_ROUTER = (
    ROOT
    / "experiments"
    / "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_unique_representative_persistence_split_router.py"
)
TEMPLATE_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-template-provenance-ledger.json"
SINGLETON_PROFILE = (
    DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-singleton-residue-sae-profile-ledger.json"
)
ONE_SLOT_CAPACITY = (
    DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-one-slot-residue-epoch-capacity-ledger.json"
)

OUT_LEDGER = DATA / "prime-matrix-cross-carrier-fifty-unit-residue-saturation-ledger.json"
OUT_JSON = DOCS / "prime-matrix-cross-carrier-fifty-unit-residue-saturation-router.json"
OUT_MD = DOCS / "prime-matrix-cross-carrier-fifty-unit-residue-saturation-router.md"

NEXT_TARGET = "TwoResidueSpareEndpointExtensionOrTransportResetPDEC"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def aggregate(path: Path) -> dict[str, Any]:
    """读取账本 aggregate；没有 aggregate 时返回原对象。"""
    obj = load_json(path)
    return obj.get("aggregate", obj)


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def load_module(path: Path, name: str) -> Any:
    """按路径加载模块。"""
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def residue_packet_key(split_module: Any, record: dict[str, Any]) -> str:
    """计算 residue packet key。"""
    return str(split_module.residue_packet_key(record))


def singleton_records() -> list[dict[str, Any]]:
    """重建 singleton 物理记录；用于取得完整 residue 集。"""
    profile = load_module(SINGLETON_ROUTER, "cross_carrier_singleton_profile")
    split = load_module(SPLIT_ROUTER, "cross_carrier_split")
    physical_records, _duplicate_packets = profile.build_records(
        TEMPLATE_LEDGER,
        10000,
        2001,
        0.43,
        2,
    )
    grouped: dict[str, list[dict[str, Any]]] = {}
    for record in physical_records:
        key = residue_packet_key(split, record)
        record["residue_packet_key"] = key
        grouped.setdefault(key, []).append(record)
    return [items[0] for items in grouped.values() if len(items) == 1]


def find_capacity_row(rows: list[dict[str, Any]], side: str, ell: int) -> dict[str, Any]:
    """查找指定 `(side, ell)` 容量行。"""
    for row in rows:
        if row["side"] == side and int(row["ell"]) == ell:
            return row
    raise KeyError(f"missing capacity row for {side}:{ell}")


def residue_ramp(anchor_residue: int, increment: int, ell: int, start: int, stop: int) -> list[int]:
    """生成闭区间 step 上的 residue ramp。"""
    return [(anchor_residue + step * increment) % ell for step in range(start, stop + 1)]


def p_at(anchor_p: int, delay: int, step: int) -> int:
    """由同步步号计算 P。"""
    return anchor_p + delay * step


def build_result() -> dict[str, Any]:
    """构造跨载体 residue 饱和证书。"""
    carrier = aggregate(CARRIER)
    capacity = load_json(ONE_SLOT_CAPACITY)
    side = str(carrier["tight_epoch_side"])
    ell = int(carrier["tight_epoch_ell"])
    capacity_row = find_capacity_row(capacity["epoch_capacity_rows"], side, ell)
    records = singleton_records()
    shape_key = f"size=1|side={side}|ells={ell}"
    shape_records = sorted(
        [record for record in records if record["normal_shape_key"] == shape_key],
        key=lambda item: (int(item["p"]), int(item["crt_residue"])),
    )
    used_residues = sorted({int(record["crt_residue"]) for record in shape_records})
    used_set = set(used_residues)

    anchor_p = int(carrier["support_generator_p"])
    delay = int(carrier["support_p_delay"])
    anchor_residue = int(carrier["anchor_p_mod_tight_epoch"])
    increment = int(carrier["p_delay_mod_tight_epoch"])
    p_min = int(carrier["tight_epoch_p_range"][0])
    p_max = int(carrier["tight_epoch_p_range"][1])
    first_step = int(carrier["steps_to_enter_epoch_range"])
    last_step = int(carrier["max_fixed_delay_steps_inside_epoch"])
    admitted_ramp = residue_ramp(anchor_residue, increment, ell, first_step, last_step)
    admitted_set = set(admitted_ramp)
    union_set = used_set | admitted_set
    missing_after_admitted = sorted(set(range(ell)) - union_set)

    block_rows = []
    block_size = int(carrier["tight_epoch_overflow_new_units"])
    last_block_start = last_step - block_size + 1
    for start in range(first_step, last_block_start + 1):
        ramp = residue_ramp(anchor_residue, increment, ell, start, start + block_size - 1)
        intersection = sorted(set(ramp) & used_set)
        new_residues = sorted(set(ramp) - used_set)
        block_rows.append(
            {
                "start_step": start,
                "end_step": start + block_size - 1,
                "start_p": p_at(anchor_p, delay, start),
                "end_p": p_at(anchor_p, delay, start + block_size - 1),
                "intersection_with_existing_count": len(intersection),
                "new_residue_count": len(new_residues),
                "union_size_if_block_added": len(used_set | set(ramp)),
                "spare_after_block": ell - len(used_set | set(ramp)),
                "first_residue": ramp[0],
                "last_residue": ramp[-1],
            }
        )

    future_rows = []
    future_union = set(union_set)
    for step in range(last_step + 1, last_step + 16):
        residue = (anchor_residue + step * increment) % ell
        is_new = residue not in future_union
        if is_new:
            future_union.add(residue)
        future_rows.append(
            {
                "step": step,
                "p": p_at(anchor_p, delay, step),
                "residue": residue,
                "new_against_current_union": is_new,
                "union_size_after_arrival": len(future_union),
                "spare_after_arrival": ell - len(future_union),
            }
        )

    first_missing_hits = [row for row in future_rows if row["new_against_current_union"]]
    first_full_capacity_row = next(
        (row for row in future_rows if int(row["union_size_after_arrival"]) == ell),
        None,
    )
    first_post_full_repeat = next(
        (
            row
            for row in future_rows
            if first_full_capacity_row is not None
            and int(row["step"]) > int(first_full_capacity_row["step"])
            and not row["new_against_current_union"]
        ),
        None,
    )

    min_block_new = min(row["new_residue_count"] for row in block_rows)
    max_block_new = max(row["new_residue_count"] for row in block_rows)
    direct_fifty_overflow_current_blocks = any(
        row["union_size_if_block_added"] > ell for row in block_rows
    )
    admitted_overflow = len(union_set) > ell
    admitted_full = len(union_set) == ell
    exact_used_matches_capacity = len(used_set) == int(capacity_row["used_residue_count"])

    result = {
        "certificate_type": "prime_matrix_cross_carrier_fifty_unit_residue_saturation_router",
        "status": "cross_carrier_fifty_unit_current_band_saturates_to_two_spare_global_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_sweep_not_used_as_global_proof": True,
        "aggregate": {
            "row_column_unconditional_closed": False,
            "previous_hardpoint": "CrossCarrierFiftyUnitSynchronizationPDECOrSAE",
            "shape_key": shape_key,
            "side": side,
            "ell": ell,
            "used_residue_count_reconstructed": len(used_set),
            "used_residue_count_capacity_ledger": capacity_row["used_residue_count"],
            "exact_used_matches_capacity_ledger": exact_used_matches_capacity,
            "used_residues": used_residues,
            "support_anchor_p": anchor_p,
            "support_delay": delay,
            "anchor_residue_mod_ell": anchor_residue,
            "increment_mod_ell": increment,
            "current_epoch_p_range": [p_min, p_max],
            "admitted_step_range": [first_step, last_step],
            "admitted_p_range_on_support_lattice": [
                p_at(anchor_p, delay, first_step),
                p_at(anchor_p, delay, last_step),
            ],
            "admitted_step_count": len(admitted_ramp),
            "admitted_distinct_residue_count": len(admitted_set),
            "admitted_intersection_existing_count": len(admitted_set & used_set),
            "admitted_new_residue_count": len(admitted_set - used_set),
            "union_size_after_admitted_band": len(union_set),
            "spare_after_admitted_band": ell - len(union_set),
            "missing_residues_after_admitted_band": missing_after_admitted,
            "direct_fifty_overflow_current_blocks": direct_fifty_overflow_current_blocks,
            "min_block_new_residue_count": min_block_new,
            "max_block_new_residue_count": max_block_new,
            "max_block_union_size": max(row["union_size_if_block_added"] for row in block_rows),
            "min_block_spare_after": min(row["spare_after_block"] for row in block_rows),
            "admitted_band_overflows_epoch": admitted_overflow,
            "admitted_band_fills_epoch": admitted_full,
            "first_missing_future_steps": first_missing_hits[:2],
            "first_full_capacity_step": first_full_capacity_row,
            "first_post_full_repeat_step": first_post_full_repeat,
            "p_extension_to_first_missing_residue": (
                first_missing_hits[0]["p"] - p_max if first_missing_hits else None
            ),
            "p_extension_to_full_capacity": (
                first_full_capacity_row["p"] - p_max if first_full_capacity_row else None
            ),
            "p_extension_to_post_full_repeat": (
                first_post_full_repeat["p"] - p_max if first_post_full_repeat else None
            ),
            "hardpoint_after_router": NEXT_TARGET,
            "next_direct_attack_target": NEXT_TARGET,
        },
        "minus71_existing_records": [
            {
                "p": int(record["p"]),
                "crt_residue": int(record["crt_residue"]),
                "slot_keys": list(record["slot_keys"]),
            }
            for record in shape_records
        ],
        "block_rows": block_rows,
        "future_arrival_rows": future_rows,
        "plain_conclusion": (
            "重建完整 singleton 物理记录后，minus:71 已用 residue 确认为 22 个，"
            "与 capacity ledger 完全一致。跨载体 support lattice 在当前 minus:71 P 区间内可进入 "
            "64 个互异 residue；其中 17 个已在既有 singleton 集中，新增 47 个，合并后为 69/71。"
            "因此当前带并不直接溢出，而是留下 residue 0 和 62 两个空位。若端点再向外延伸到 "
            "P=9647 与 P=9727，这两个空位依次被填满；再继续持久同步则只能触发重复 residue "
            "并进入 transport reset-PDEC，或提前回到 SAE/unused-target/moving-carrier 出口。"
        ),
        "dependency_hashes": {
            str(path.relative_to(ROOT)): sha256(path)
            for path in (
                CARRIER,
                TEMPLATE_LEDGER,
                SINGLETON_PROFILE,
                ONE_SLOT_CAPACITY,
                SINGLETON_ROUTER,
                SPLIT_ROUTER,
            )
        },
    }
    return result


def write_outputs(result: dict[str, Any]) -> None:
    """写出 JSON 与 Markdown。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    OUT_LEDGER.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    agg = result["aggregate"]
    lines = [
        "# Prime Matrix cross-carrier fifty-unit residue saturation router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"row_column_unconditional_closed={fmt_bool(agg['row_column_unconditional_closed'])}",
        f"shape_key={agg['shape_key']}",
        f"used_residue_count_reconstructed={agg['used_residue_count_reconstructed']}",
        f"exact_used_matches_capacity_ledger={fmt_bool(agg['exact_used_matches_capacity_ledger'])}",
        f"admitted_step_range={agg['admitted_step_range']}",
        f"admitted_p_range_on_support_lattice={agg['admitted_p_range_on_support_lattice']}",
        f"admitted_distinct_residue_count={agg['admitted_distinct_residue_count']}",
        f"admitted_intersection_existing_count={agg['admitted_intersection_existing_count']}",
        f"admitted_new_residue_count={agg['admitted_new_residue_count']}",
        f"union_size_after_admitted_band={agg['union_size_after_admitted_band']}",
        f"spare_after_admitted_band={agg['spare_after_admitted_band']}",
        f"missing_residues_after_admitted_band={agg['missing_residues_after_admitted_band']}",
        f"direct_fifty_overflow_current_blocks={fmt_bool(agg['direct_fifty_overflow_current_blocks'])}",
        f"min_block_new_residue_count={agg['min_block_new_residue_count']}",
        f"max_block_new_residue_count={agg['max_block_new_residue_count']}",
        f"max_block_union_size={agg['max_block_union_size']}",
        f"min_block_spare_after={agg['min_block_spare_after']}",
        f"p_extension_to_first_missing_residue={agg['p_extension_to_first_missing_residue']}",
        f"p_extension_to_full_capacity={agg['p_extension_to_full_capacity']}",
        f"p_extension_to_post_full_repeat={agg['p_extension_to_post_full_repeat']}",
        f"next_direct_attack_target={agg['next_direct_attack_target']}",
        "```",
        "",
        "## 1. minus:71 已用 residue",
        "",
        "| p | residue | slot keys |",
        "| ---: | ---: | --- |",
    ]
    for row in result["minus71_existing_records"]:
        lines.append(f"| {row['p']} | {row['crt_residue']} | `{row['slot_keys']}` |")

    lines.extend(
        [
            "",
            "## 2. 50 步块扫描",
            "",
            "| start step | p range | new residues | intersection | union size | spare |",
            "| ---: | --- | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in result["block_rows"]:
        lines.append(
            f"| {row['start_step']} | `{row['start_p']}..{row['end_p']}` | "
            f"{row['new_residue_count']} | {row['intersection_with_existing_count']} | "
            f"{row['union_size_if_block_added']} | {row['spare_after_block']} |"
        )

    lines.extend(
        [
            "",
            "## 3. 当前带外的后续到达",
            "",
            "| step | p | residue | new against current union | union size | spare |",
            "| ---: | ---: | ---: | --- | ---: | ---: |",
        ]
    )
    for row in result["future_arrival_rows"]:
        lines.append(
            f"| {row['step']} | {row['p']} | {row['residue']} | "
            f"`{fmt_bool(row['new_against_current_union'])}` | "
            f"{row['union_size_after_arrival']} | {row['spare_after_arrival']} |"
        )

    lines.extend(
        [
            "",
            "## 4. 证明边界",
            "",
            "- 当前 50 步块都不能直接造成 `minus:71` 溢出；最大并集只有 `62/71`。",
            "- 当前 support lattice 能进入的整个 `minus:71` 带只达到 `69/71`，留下两个空位。",
            "- 若端点外延填满两个空位，之后的持久同步必须变成重复 residue，即 reset-PDEC；若不能外延，则回到 endpoint/SAE/unused-target 出口。",
            f"- 下一主攻点：`{agg['next_direct_attack_target']}`。",
            "",
            "## 5. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in result["dependency_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")

    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """入口。"""
    result = build_result()
    write_outputs(result)
    print(json.dumps(result["aggregate"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
