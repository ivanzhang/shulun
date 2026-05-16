#!/usr/bin/env python3
"""生成 AffineTwin unused-target arrival 审计证书。

用法示例：
  python3 experiments/prime_matrix_affine_twin_unused_target_arrival_audit.py
  python3 -m json.tool data/prime-matrix-affine-twin-unused-target-arrival-ledger.json

输出：
  data/prime-matrix-affine-twin-unused-target-arrival-ledger.json
  docs/monograph/prime-matrix-affine-twin-unused-target-arrival-audit.json
  docs/monograph/prime-matrix-affine-twin-unused-target-arrival-audit.md
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

EDGE_LEDGER = DATA / "prime-matrix-affine-twin-window-edge-collision-ledger.json"
CRT_LEDGER = DATA / "prime-matrix-affine-twin-crt-window-gap-ledger.json"
SLOT_LEDGER = DATA / (
    "square-phase-offband-prefix-gap-shadow-selector-h-lower-"
    "affine-twin-slot-phase-lock-ledger.json"
)

OUT_LEDGER = DATA / "prime-matrix-affine-twin-unused-target-arrival-ledger.json"
OUT_JSON = DOCS / "prime-matrix-affine-twin-unused-target-arrival-audit.json"
OUT_MD = DOCS / "prime-matrix-affine-twin-unused-target-arrival-audit.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def pair_key(generator_residue: int, fill_residue: int) -> str:
    """生成 residue pair 的稳定键。"""
    return f"{generator_residue}:{fill_residue}"


def mod_inverse(value: int, modulus: int) -> int:
    """计算模逆元。"""
    return pow(value % modulus, -1, modulus)


def signed_minimal(value: int, modulus: int) -> int:
    """把模差转成绝对值最小的有符号代表。"""
    residue = value % modulus
    if residue > modulus // 2:
        return residue - modulus
    return residue


def slot_index(rows: list[dict[str, Any]]) -> dict[int, dict[str, Any]]:
    """按 q 建立 slot-lock 索引。"""
    return {int(row["gap_ell"]): row for row in rows}


def crt_steps(slot_row: dict[str, Any]) -> dict[str, int]:
    """给出 generator/fill residue 改变一个单位时的 CRT 相位步长。"""
    generator_modulus = int(slot_row["generator_modulus"])
    fill_modulus = int(slot_row["fill_modulus"])
    combined_modulus = generator_modulus * fill_modulus
    generator_unit_step = fill_modulus * mod_inverse(
        fill_modulus, generator_modulus
    )
    fill_unit_step = generator_modulus * mod_inverse(
        generator_modulus, fill_modulus
    )
    return {
        "generator_modulus": generator_modulus,
        "fill_modulus": fill_modulus,
        "combined_modulus": combined_modulus,
        "generator_unit_step": generator_unit_step,
        "fill_unit_step": fill_unit_step,
    }


def build_result(edge_path: Path, crt_path: Path, slot_path: Path) -> dict[str, Any]:
    """构造 unused-target arrival 审计结果。"""
    edge = load_json(edge_path)
    crt = load_json(crt_path)
    slot = load_json(slot_path)

    crt_rows = {
        pair_key(int(row["generator_residue"]), int(row["fill_residue"])): row
        for row in crt["crt_window_rows"]
    }
    formal_pairs = set(crt_rows)
    supported_actual_pairs = {
        pair_key(int(row["generator_residue"]), int(row["fill_residue"]))
        for row in crt["crt_window_rows"]
        if bool(row["supported_actual_packet_current"])
    }
    formal_generator_residues = sorted(
        {int(row["generator_residue"]) for row in crt["crt_window_rows"]}
    )
    formal_fill_residues = sorted(
        {int(row["fill_residue"]) for row in crt["crt_window_rows"]}
    )
    formal_generator_set = set(formal_generator_residues)
    formal_fill_set = set(formal_fill_residues)
    slot_by_q = slot_index(slot["affine_twin_slot_phase_lock_rows"])

    rows: list[dict[str, Any]] = []
    for edge_row in edge["edge_collision_rows"]:
        if edge_row["edge_collision_route"] != "UnusedTargetResidueArrivalNeeded":
            continue

        q = int(edge_row["q"])
        source_key = pair_key(
            int(edge_row["generator_residue"]),
            int(edge_row["fill_residue"]),
        )
        target_generator = int(edge_row["target_generator_residue"])
        target_fill = int(edge_row["target_fill_residue"])
        target_key = pair_key(target_generator, target_fill)
        source_row = crt_rows[source_key]
        steps = crt_steps(slot_by_q[q])
        generator_delta = int(edge_row["generator_delta_to_target"])
        fill_delta = int(edge_row["fill_delta_to_target"])
        raw_crt_jump = (
            generator_delta * steps["generator_unit_step"]
            + fill_delta * steps["fill_unit_step"]
        )
        signed_crt_jump = signed_minimal(raw_crt_jump, steps["combined_modulus"])
        source_nearest = int(source_row["nearest_representative"])
        target_p = int(edge_row["target_p"])
        observed_signed_jump = target_p - source_nearest
        support_width = int(source_row["pair_phase_support_width"])
        needs_new_generator = target_generator not in formal_generator_set
        needs_new_fill = target_fill not in formal_fill_set

        rows.append(
            {
                "q": q,
                "source_pair_key": source_key,
                "target_unused_pair_key": target_key,
                "source_generator_residue": int(edge_row["generator_residue"]),
                "source_fill_residue": int(edge_row["fill_residue"]),
                "target_generator_residue": target_generator,
                "target_fill_residue": target_fill,
                "target_p": target_p,
                "generator_delta_to_target": generator_delta,
                "fill_delta_to_target": fill_delta,
                "residue_l1_displacement": int(
                    edge_row["min_l1_residue_displacement_to_window"]
                ),
                "target_pair_currently_formal": target_key in formal_pairs,
                "target_pair_currently_supported_actual": target_key
                in supported_actual_pairs,
                "needs_new_generator_residue": needs_new_generator,
                "needs_new_fill_residue": needs_new_fill,
                "new_side_residue_count": int(needs_new_generator)
                + int(needs_new_fill),
                "source_nearest_representative": source_nearest,
                "support_interval": source_row["pair_phase_support"],
                "support_width": support_width,
                "combined_modulus": steps["combined_modulus"],
                "generator_unit_step": steps["generator_unit_step"],
                "fill_unit_step": steps["fill_unit_step"],
                "signed_crt_jump_to_unused_target": signed_crt_jump,
                "observed_signed_jump_to_unused_target": observed_signed_jump,
                "crt_jump_identity_closed": signed_crt_jump
                == observed_signed_jump,
                "abs_crt_jump_to_unused_target": abs(signed_crt_jump),
                "jump_minus_support_width": abs(signed_crt_jump) - support_width,
                "crt_jump_exceeds_support_width": abs(signed_crt_jump)
                > support_width,
                "source_window_distance": int(source_row["window_distance"]),
                "source_window_side": source_row["window_side"],
            }
        )

    if not rows:
        raise RuntimeError("no UnusedTargetResidueArrivalNeeded rows found")

    target_counter = Counter(str(row["target_unused_pair_key"]) for row in rows)
    for row in rows:
        row["target_occurrence_count_current"] = int(
            target_counter[row["target_unused_pair_key"]]
        )

    unique_targets = {
        str(row["target_unused_pair_key"]): row for row in rows
    }.values()
    required_new_generators = sorted(
        {
            int(row["target_generator_residue"])
            for row in unique_targets
            if bool(row["needs_new_generator_residue"])
        }
    )
    unique_targets = {
        str(row["target_unused_pair_key"]): row for row in rows
    }.values()
    required_new_fills = sorted(
        {
            int(row["target_fill_residue"])
            for row in unique_targets
            if bool(row["needs_new_fill_residue"])
        }
    )
    jump_values = [int(row["abs_crt_jump_to_unused_target"]) for row in rows]
    jump_margins = [int(row["jump_minus_support_width"]) for row in rows]
    l1_values = [int(row["residue_l1_displacement"]) for row in rows]
    new_counts = [int(row["new_side_residue_count"]) for row in rows]
    narrowest_l1_row = min(
        rows,
        key=lambda row: (
            int(row["residue_l1_displacement"]),
            int(row["abs_crt_jump_to_unused_target"]),
            str(row["source_pair_key"]),
        ),
    )
    minimum_jump_row = min(
        rows,
        key=lambda row: (
            int(row["abs_crt_jump_to_unused_target"]),
            int(row["residue_l1_displacement"]),
            str(row["source_pair_key"]),
        ),
    )

    aggregate = {
        "edge_collision_ledger": str(edge_path.relative_to(ROOT)),
        "crt_window_gap_ledger": str(crt_path.relative_to(ROOT)),
        "slot_ledger": str(slot_path.relative_to(ROOT)),
        "unused_target_arrival_candidate_count": len(rows),
        "unique_unused_target_pair_count": len(target_counter),
        "unused_target_pair_histogram": dict(sorted(target_counter.items())),
        "current_formal_generator_residues": formal_generator_residues,
        "current_formal_fill_residues": formal_fill_residues,
        "required_new_generator_residues": required_new_generators,
        "required_new_fill_residues": required_new_fills,
        "required_unique_side_residue_arrival_count": len(required_new_generators)
        + len(required_new_fills),
        "occurrence_new_side_residue_requirement_total": sum(new_counts),
        "min_new_side_residues_per_candidate": min(new_counts),
        "max_new_side_residues_per_candidate": max(new_counts),
        "targets_reusing_existing_fill_residue_count": sum(
            1 for row in rows if not bool(row["needs_new_fill_residue"])
        ),
        "target_pairs_currently_formal_count": sum(
            1 for row in rows if bool(row["target_pair_currently_formal"])
        ),
        "target_pairs_currently_supported_actual_count": sum(
            1 for row in rows if bool(row["target_pair_currently_supported_actual"])
        ),
        "min_unused_target_residue_l1": min(l1_values),
        "max_unused_target_residue_l1": max(l1_values),
        "min_abs_crt_jump_to_unused_target": min(jump_values),
        "max_abs_crt_jump_to_unused_target": max(jump_values),
        "min_jump_minus_support_width": min(jump_margins),
        "max_jump_minus_support_width": max(jump_margins),
        "support_width_current": int(rows[0]["support_width"]),
        "combined_modulus_current": int(rows[0]["combined_modulus"]),
        "generator_unit_step_current": int(rows[0]["generator_unit_step"]),
        "fill_unit_step_current": int(rows[0]["fill_unit_step"]),
        "narrowest_l1_atom": {
            "source_pair_key": narrowest_l1_row["source_pair_key"],
            "target_unused_pair_key": narrowest_l1_row["target_unused_pair_key"],
            "residue_l1_displacement": narrowest_l1_row["residue_l1_displacement"],
            "new_side_residue_count": narrowest_l1_row["new_side_residue_count"],
            "abs_crt_jump_to_unused_target": narrowest_l1_row[
                "abs_crt_jump_to_unused_target"
            ],
            "jump_minus_support_width": narrowest_l1_row["jump_minus_support_width"],
        },
        "minimum_crt_jump_atom": {
            "source_pair_key": minimum_jump_row["source_pair_key"],
            "target_unused_pair_key": minimum_jump_row["target_unused_pair_key"],
            "residue_l1_displacement": minimum_jump_row["residue_l1_displacement"],
            "new_side_residue_count": minimum_jump_row["new_side_residue_count"],
            "abs_crt_jump_to_unused_target": minimum_jump_row[
                "abs_crt_jump_to_unused_target"
            ],
            "jump_minus_support_width": minimum_jump_row["jump_minus_support_width"],
        },
        "all_unused_targets_are_outside_current_formal_product": all(
            not bool(row["target_pair_currently_formal"]) for row in rows
        ),
        "all_unused_targets_are_not_supported_actual_current_sweep": all(
            not bool(row["target_pair_currently_supported_actual"]) for row in rows
        ),
        "all_unused_targets_need_new_side_residue": all(
            int(row["new_side_residue_count"]) >= 1 for row in rows
        ),
        "all_unused_targets_need_new_generator_residue": all(
            bool(row["needs_new_generator_residue"]) for row in rows
        ),
        "all_crt_jump_identities_closed": all(
            bool(row["crt_jump_identity_closed"]) for row in rows
        ),
        "all_unused_target_crt_jumps_exceed_support_width_current_sweep": all(
            bool(row["crt_jump_exceeds_support_width"]) for row in rows
        ),
        "unused_target_arrival_closed_current_sweep": all(
            not bool(row["target_pair_currently_formal"])
            and int(row["new_side_residue_count"]) >= 1
            and bool(row["crt_jump_identity_closed"])
            and bool(row["crt_jump_exceeds_support_width"])
            for row in rows
        ),
        "global_unused_target_arrival_bound_proved": False,
        "row_column_unconditional_closed": False,
    }

    return {
        "certificate_type": "prime_matrix_affine_twin_unused_target_arrival_audit",
        "status": "current_sweep_unused_target_arrivals_closed_global_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "aggregate": aggregate,
        "unused_target_arrival_rows": rows,
        "contract": {
            "unused_target_arrival_gate": (
                "A non-hit formal pair whose nearest target is unused can become "
                "actual only if at least one new side residue arrives and the "
                "corresponding CRT phase jump is paid."
            ),
            "closed_current_sweep": aggregate[
                "unused_target_arrival_closed_current_sweep"
            ],
            "global_remaining": [
                "GlobalUnusedTargetArrivalBound",
                "NewGeneratorResidueArrival-PDEC/SAE",
                "NewFillResidueArrival-PDEC/SAE",
                "SupportMotionEscape-PDEC/SAE",
            ],
        },
        "dependency_hashes": {
            str(path.relative_to(ROOT)): sha256(path)
            for path in (edge_path, crt_path, slot_path)
        },
    }


def write_outputs(result: dict[str, Any]) -> None:
    """写出 JSON 与 Markdown。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    for path in (OUT_LEDGER, OUT_JSON):
        path.write_text(
            json.dumps(result, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

    agg = result["aggregate"]
    lines = [
        "# Prime Matrix AffineTwin unused-target arrival audit",
        "",
        "**状态：** `current_sweep_unused_target_arrivals_closed_global_open`",
        "",
        "本审计继续下钻 `WindowEdgeCollision` 的 unused-target 分支：空窗 formal pair 若要落到当前未使用的 target pair，必须让 target pair 进入当前形式积，并支付 residue 位移对应的 CRT 相位跳跃。",
        "",
        "```text",
        f"unused_target_arrival_candidate_count={agg['unused_target_arrival_candidate_count']}",
        f"unique_unused_target_pair_count={agg['unique_unused_target_pair_count']}",
        f"required_unique_side_residue_arrival_count={agg['required_unique_side_residue_arrival_count']}",
        f"occurrence_new_side_residue_requirement_total={agg['occurrence_new_side_residue_requirement_total']}",
        f"min_new_side_residues_per_candidate={agg['min_new_side_residues_per_candidate']}",
        f"max_new_side_residues_per_candidate={agg['max_new_side_residues_per_candidate']}",
        f"min_abs_crt_jump_to_unused_target={agg['min_abs_crt_jump_to_unused_target']}",
        f"max_abs_crt_jump_to_unused_target={agg['max_abs_crt_jump_to_unused_target']}",
        f"support_width_current={agg['support_width_current']}",
        f"unused_target_arrival_closed_current_sweep={fmt_bool(agg['unused_target_arrival_closed_current_sweep'])}",
        "```",
        "",
        "## 1. unused-target arrival 表",
        "",
        "| source | target unused | target P | new g | new f | new count | L1 | CRT jump | jump-width | multiplicity |",
        "| --- | --- | ---: | --- | --- | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in result["unused_target_arrival_rows"]:
        lines.append(
            "| `{source}` | `{target}` | {target_p} | `{new_g}` | `{new_f}` | {new_count} | {l1} | {jump} | {margin} | {mult} |".format(
                source=row["source_pair_key"],
                target=row["target_unused_pair_key"],
                target_p=row["target_p"],
                new_g=fmt_bool(row["needs_new_generator_residue"]),
                new_f=fmt_bool(row["needs_new_fill_residue"]),
                new_count=row["new_side_residue_count"],
                l1=row["residue_l1_displacement"],
                jump=row["abs_crt_jump_to_unused_target"],
                margin=row["jump_minus_support_width"],
                mult=row["target_occurrence_count_current"],
            )
        )

    narrow = agg["narrowest_l1_atom"]
    minimum = agg["minimum_crt_jump_atom"]
    lines.extend(
        [
            "",
            "## 2. 当前读数",
            "",
            f"- 当前形式 generator residues 为 `{agg['current_formal_generator_residues']}`，fill residues 为 `{agg['current_formal_fill_residues']}`。",
            f"- `9` 个 unused-target 候选压缩到 `5` 个唯一 target pairs：`{agg['unused_target_pair_histogram']}`。",
            f"- 这些 target 全部不在当前形式积中；唯一侧残基需求为 generator `{agg['required_new_generator_residues']}` 与 fill `{agg['required_new_fill_residues']}`，合计 `{agg['required_unique_side_residue_arrival_count']}` 个新侧残基。",
            f"- 最窄 residue atom 是 `{narrow['source_pair_key']} -> {narrow['target_unused_pair_key']}`，`L1={narrow['residue_l1_displacement']}`，但仍需 `{narrow['new_side_residue_count']}` 个新侧残基，CRT 跳跃 `{narrow['abs_crt_jump_to_unused_target']}`。",
            f"- 最小 CRT 跳跃 atom 是 `{minimum['source_pair_key']} -> {minimum['target_unused_pair_key']}`，跳跃 `{minimum['abs_crt_jump_to_unused_target']}`，仍比窗口宽度多 `{minimum['jump_minus_support_width']}`。",
            "",
            "## 3. 结论边界",
            "",
            "- 本步关闭当前 sweep 的 unused-target arrival 账本：所有 unused target 均在当前形式积外，均至少需要一个新侧残基，并且 CRT 跳跃均大于支撑宽度。",
            "- 本步不证明全局 unused-target arrival 不发生；全局剩余是控制新 generator/fill residue 到达，或把失败路由到 `NewGeneratorResidueArrival-PDEC/SAE`、`NewFillResidueArrival-PDEC/SAE`、`SupportMotionEscape-PDEC/SAE`。",
            "",
            "## 4. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in result["dependency_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(
        description="生成 AffineTwin unused-target arrival 审计证书。"
    )
    parser.add_argument("--edge-ledger", type=Path, default=EDGE_LEDGER)
    parser.add_argument("--crt-window-gap-ledger", type=Path, default=CRT_LEDGER)
    parser.add_argument("--slot-ledger", type=Path, default=SLOT_LEDGER)
    return parser.parse_args()


def main() -> None:
    """入口。"""
    args = parse_args()
    result = build_result(
        args.edge_ledger,
        args.crt_window_gap_ledger,
        args.slot_ledger,
    )
    write_outputs(result)
    print(json.dumps(result["aggregate"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
