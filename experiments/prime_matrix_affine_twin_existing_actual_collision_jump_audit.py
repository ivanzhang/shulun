#!/usr/bin/env python3
"""生成 AffineTwin existing-actual collision CRT 跳跃审计证书。

用法示例：
  python3 experiments/prime_matrix_affine_twin_existing_actual_collision_jump_audit.py
  python3 -m json.tool data/prime-matrix-affine-twin-existing-actual-collision-jump-ledger.json

输出：
  data/prime-matrix-affine-twin-existing-actual-collision-jump-ledger.json
  docs/monograph/prime-matrix-affine-twin-existing-actual-collision-jump-audit.json
  docs/monograph/prime-matrix-affine-twin-existing-actual-collision-jump-audit.md
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

OUT_LEDGER = DATA / (
    "prime-matrix-affine-twin-existing-actual-collision-jump-ledger.json"
)
OUT_JSON = DOCS / (
    "prime-matrix-affine-twin-existing-actual-collision-jump-audit.json"
)
OUT_MD = DOCS / (
    "prime-matrix-affine-twin-existing-actual-collision-jump-audit.md"
)


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


def build_result(
    edge_path: Path,
    crt_path: Path,
    slot_path: Path,
) -> dict[str, Any]:
    """构造 existing-actual collision 的 CRT 跳跃审计结果。"""
    edge = load_json(edge_path)
    crt = load_json(crt_path)
    slot = load_json(slot_path)

    crt_rows = {
        pair_key(int(row["generator_residue"]), int(row["fill_residue"])): row
        for row in crt["crt_window_rows"]
    }
    slot_by_q = slot_index(slot["affine_twin_slot_phase_lock_rows"])

    rows: list[dict[str, Any]] = []
    for edge_row in edge["edge_collision_rows"]:
        if edge_row["edge_collision_route"] != "ExistingActualResidueCollisionNeeded":
            continue

        q = int(edge_row["q"])
        source_key = pair_key(
            int(edge_row["generator_residue"]),
            int(edge_row["fill_residue"]),
        )
        target_key = pair_key(
            int(edge_row["target_generator_residue"]),
            int(edge_row["target_fill_residue"]),
        )
        source_row = crt_rows[source_key]
        target_row = crt_rows[target_key]
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

        rows.append(
            {
                "q": q,
                "source_pair_key": source_key,
                "target_existing_actual_pair_key": target_key,
                "source_generator_residue": int(edge_row["generator_residue"]),
                "source_fill_residue": int(edge_row["fill_residue"]),
                "target_generator_residue": int(edge_row["target_generator_residue"]),
                "target_fill_residue": int(edge_row["target_fill_residue"]),
                "generator_delta_to_existing_actual": generator_delta,
                "fill_delta_to_existing_actual": fill_delta,
                "residue_l1_displacement": int(
                    edge_row["min_l1_residue_displacement_to_window"]
                ),
                "source_nearest_representative": source_nearest,
                "target_actual_p": target_p,
                "target_actual_representatives": target_row[
                    "representatives_in_pair_support"
                ],
                "support_interval": source_row["pair_phase_support"],
                "support_width": support_width,
                "combined_modulus": steps["combined_modulus"],
                "generator_unit_step": steps["generator_unit_step"],
                "fill_unit_step": steps["fill_unit_step"],
                "signed_crt_jump_to_existing_actual": signed_crt_jump,
                "observed_signed_jump_to_existing_actual": observed_signed_jump,
                "crt_jump_identity_closed": signed_crt_jump
                == observed_signed_jump,
                "abs_crt_jump_to_existing_actual": abs(signed_crt_jump),
                "jump_minus_support_width": abs(signed_crt_jump) - support_width,
                "crt_jump_exceeds_support_width": abs(signed_crt_jump)
                > support_width,
                "source_window_distance": int(source_row["window_distance"]),
                "source_window_side": source_row["window_side"],
            }
        )

    if not rows:
        raise RuntimeError("no ExistingActualResidueCollisionNeeded rows found")

    l1_values = [int(row["residue_l1_displacement"]) for row in rows]
    jump_values = [int(row["abs_crt_jump_to_existing_actual"]) for row in rows]
    jump_margins = [int(row["jump_minus_support_width"]) for row in rows]
    target_histogram = Counter(
        str(row["target_existing_actual_pair_key"]) for row in rows
    )
    narrowest_l1_row = min(
        rows,
        key=lambda row: (
            int(row["residue_l1_displacement"]),
            int(row["abs_crt_jump_to_existing_actual"]),
            str(row["source_pair_key"]),
        ),
    )
    minimum_jump_row = min(
        rows,
        key=lambda row: (
            int(row["abs_crt_jump_to_existing_actual"]),
            int(row["residue_l1_displacement"]),
            str(row["source_pair_key"]),
        ),
    )

    aggregate = {
        "edge_collision_ledger": str(edge_path.relative_to(ROOT)),
        "crt_window_gap_ledger": str(crt_path.relative_to(ROOT)),
        "slot_ledger": str(slot_path.relative_to(ROOT)),
        "existing_actual_collision_candidate_count": len(rows),
        "existing_actual_target_pair_count": len(target_histogram),
        "existing_actual_target_pair_histogram": dict(sorted(target_histogram.items())),
        "min_existing_actual_residue_l1": min(l1_values),
        "max_existing_actual_residue_l1": max(l1_values),
        "min_abs_crt_jump_to_existing_actual": min(jump_values),
        "max_abs_crt_jump_to_existing_actual": max(jump_values),
        "min_jump_minus_support_width": min(jump_margins),
        "max_jump_minus_support_width": max(jump_margins),
        "support_width_current": int(rows[0]["support_width"]),
        "combined_modulus_current": int(rows[0]["combined_modulus"]),
        "generator_unit_step_current": int(rows[0]["generator_unit_step"]),
        "fill_unit_step_current": int(rows[0]["fill_unit_step"]),
        "narrowest_l1_atom": {
            "source_pair_key": narrowest_l1_row["source_pair_key"],
            "target_existing_actual_pair_key": narrowest_l1_row[
                "target_existing_actual_pair_key"
            ],
            "residue_l1_displacement": narrowest_l1_row["residue_l1_displacement"],
            "abs_crt_jump_to_existing_actual": narrowest_l1_row[
                "abs_crt_jump_to_existing_actual"
            ],
            "jump_minus_support_width": narrowest_l1_row[
                "jump_minus_support_width"
            ],
        },
        "minimum_crt_jump_atom": {
            "source_pair_key": minimum_jump_row["source_pair_key"],
            "target_existing_actual_pair_key": minimum_jump_row[
                "target_existing_actual_pair_key"
            ],
            "residue_l1_displacement": minimum_jump_row[
                "residue_l1_displacement"
            ],
            "abs_crt_jump_to_existing_actual": minimum_jump_row[
                "abs_crt_jump_to_existing_actual"
            ],
            "jump_minus_support_width": minimum_jump_row["jump_minus_support_width"],
        },
        "all_crt_jump_identities_closed": all(
            bool(row["crt_jump_identity_closed"]) for row in rows
        ),
        "all_existing_actual_crt_jumps_exceed_support_width_current_sweep": all(
            bool(row["crt_jump_exceeds_support_width"]) for row in rows
        ),
        "existing_actual_collision_jump_closed_current_sweep": all(
            bool(row["crt_jump_identity_closed"])
            and bool(row["crt_jump_exceeds_support_width"])
            for row in rows
        ),
        "global_existing_actual_collision_excluded": False,
        "row_column_unconditional_closed": False,
    }

    return {
        "certificate_type": (
            "prime_matrix_affine_twin_existing_actual_collision_jump_audit"
        ),
        "status": (
            "current_sweep_existing_actual_collision_jumps_closed_global_open"
        ),
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "aggregate": aggregate,
        "existing_actual_collision_rows": rows,
        "contract": {
            "existing_actual_collision_gate": (
                "An empty formal pair whose nearest target is an existing "
                "actual pair must pay the full CRT phase jump induced by its "
                "residue displacement."
            ),
            "closed_current_sweep": aggregate[
                "existing_actual_collision_jump_closed_current_sweep"
            ],
            "global_remaining": [
                "GlobalExistingActualCollisionNonPersistence",
                "RepeatedResidue-ColumnCRT-PDEC",
                "SupportMotionEscape-PDEC/SAE",
                "UnusedTargetResidueArrival-PDEC/SAE",
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
        "# Prime Matrix AffineTwin existing-actual collision CRT jump audit",
        "",
        "**状态：** `current_sweep_existing_actual_collision_jumps_closed_global_open`",
        "",
        "本审计继续下钻 `WindowEdgeCollision` 中最窄的 existing-actual 分支：空窗 formal pair 若要撞向已经实现的 actual pair，必须支付 residue 位移对应的完整 CRT 相位跳跃。",
        "",
        "```text",
        f"existing_actual_collision_candidate_count={agg['existing_actual_collision_candidate_count']}",
        f"existing_actual_target_pair_count={agg['existing_actual_target_pair_count']}",
        f"min_existing_actual_residue_l1={agg['min_existing_actual_residue_l1']}",
        f"max_existing_actual_residue_l1={agg['max_existing_actual_residue_l1']}",
        f"min_abs_crt_jump_to_existing_actual={agg['min_abs_crt_jump_to_existing_actual']}",
        f"max_abs_crt_jump_to_existing_actual={agg['max_abs_crt_jump_to_existing_actual']}",
        f"support_width_current={agg['support_width_current']}",
        f"generator_unit_step_current={agg['generator_unit_step_current']}",
        f"fill_unit_step_current={agg['fill_unit_step_current']}",
        f"existing_actual_collision_jump_closed_current_sweep={fmt_bool(agg['existing_actual_collision_jump_closed_current_sweep'])}",
        "```",
        "",
        "## 1. existing-actual CRT 跳跃表",
        "",
        "| source | target actual | delta g | delta f | L1 | source rep | target P | CRT jump | jump-width | closed |",
        "| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in result["existing_actual_collision_rows"]:
        lines.append(
            "| `{source}` | `{target}` | {dg} | {df} | {l1} | {rep} | {target_p} | {jump} | {margin} | `{closed}` |".format(
                source=row["source_pair_key"],
                target=row["target_existing_actual_pair_key"],
                dg=row["generator_delta_to_existing_actual"],
                df=row["fill_delta_to_existing_actual"],
                l1=row["residue_l1_displacement"],
                rep=row["source_nearest_representative"],
                target_p=row["target_actual_p"],
                jump=row["abs_crt_jump_to_existing_actual"],
                margin=row["jump_minus_support_width"],
                closed=fmt_bool(
                    row["crt_jump_identity_closed"]
                    and row["crt_jump_exceeds_support_width"]
                ),
            )
        )

    narrow = agg["narrowest_l1_atom"]
    minimum = agg["minimum_crt_jump_atom"]
    lines.extend(
        [
            "",
            "## 2. 当前读数",
            "",
            f"- 双模 CRT 单位步长为 `generator_unit={agg['generator_unit_step_current']}`、`fill_unit={agg['fill_unit_step_current']}`，共同窗口宽度为 `{agg['support_width_current']}`。",
            f"- 最窄 residue atom 是 `{narrow['source_pair_key']} -> {narrow['target_existing_actual_pair_key']}`，`L1={narrow['residue_l1_displacement']}`，但 CRT 跳跃为 `{narrow['abs_crt_jump_to_existing_actual']}`，比窗口宽度多 `{narrow['jump_minus_support_width']}`。",
            f"- 最小 CRT 跳跃 atom 是 `{minimum['source_pair_key']} -> {minimum['target_existing_actual_pair_key']}`，跳跃 `{minimum['abs_crt_jump_to_existing_actual']}`，仍比窗口宽度多 `{minimum['jump_minus_support_width']}`。",
            "- 因此当前 existing-actual 碰撞不是窗口边缘的微小滑入；若要全局复现，必须移动支撑/残基结构并进入 repeated-residue、ColumnCRT、PDEC 或 SAE 出口。",
            "",
            "## 3. 结论边界",
            "",
            "- 本步关闭当前 sweep 的 existing-actual collision CRT 跳跃账本。",
            "- 本步不证明全局 existing-actual collision 不复现；全局剩余是排斥持久复现，或把复现登记为 `RepeatedResidue-ColumnCRT-PDEC` / `SupportMotionEscape-PDEC/SAE`。",
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
        description="生成 AffineTwin existing-actual collision CRT 跳跃审计证书。"
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
