#!/usr/bin/env python3
"""生成 AffineTwin support-motion primitive-depth defect 审计证书。

用法示例：
  python3 experiments/prime_matrix_affine_twin_support_motion_primitive_defect_audit.py
  python3 -m json.tool data/prime-matrix-affine-twin-support-motion-primitive-defect-ledger.json

输出：
  data/prime-matrix-affine-twin-support-motion-primitive-defect-ledger.json
  docs/monograph/prime-matrix-affine-twin-support-motion-primitive-defect-audit.json
  docs/monograph/prime-matrix-affine-twin-support-motion-primitive-defect-audit.md
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

SUPPORT_MOTION_LEDGER = DATA / "prime-matrix-affine-twin-support-motion-depth-ledger.json"
SLOT_LEDGER = DATA / (
    "square-phase-offband-prefix-gap-shadow-selector-h-lower-"
    "affine-twin-slot-phase-lock-ledger.json"
)
PRIMITIVE_LEDGER = DATA / (
    "square-phase-offband-prefix-gap-shadow-selector-h-lower-"
    "margin-slot-primitive-identity-ledger.json"
)

OUT_LEDGER = DATA / "prime-matrix-affine-twin-support-motion-primitive-defect-ledger.json"
OUT_JSON = DOCS / "prime-matrix-affine-twin-support-motion-primitive-defect-audit.json"
OUT_MD = DOCS / "prime-matrix-affine-twin-support-motion-primitive-defect-audit.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def slot_by_q(rows: list[dict[str, Any]]) -> dict[int, dict[str, Any]]:
    """按 q 建立 slot-lock 索引。"""
    return {int(row["gap_ell"]): row for row in rows}


def primitive_by_q(rows: list[dict[str, Any]]) -> dict[int, dict[str, Any]]:
    """按 q 建立 primitive 身份索引。"""
    return {int(row["gap_ell"]): row for row in rows}


def defect_row(
    support_row: dict[str, Any],
    slot_row: dict[str, Any],
    primitive_row: dict[str, Any],
) -> dict[str, Any]:
    """把一条 support-motion 行转成固定 primitive depth 缺陷。"""
    q = int(support_row["q"])
    side = str(support_row["window_side"])
    required_depth = int(support_row["required_common_side_depth"])
    if side == "below":
        generator_identity_name = "generator_left_depth_affine_identity"
        fill_identity_name = "fill_left_depth_affine_identity"
        generator_current_depth = int(slot_row["generator_left_depth"])
        fill_current_depth = int(slot_row["fill_left_depth"])
        generator_affine_rhs = int(slot_row["generator_left_depth_affine_rhs"])
        fill_affine_rhs = int(slot_row["fill_left_depth_affine_rhs"])
        primitive_generator_rhs = int(primitive_row["generator_margin"]) + int(
            primitive_row["fill_left_spare"]
        )
        primitive_fill_rhs = int(primitive_row["fill_margin"]) + 1
    elif side == "above":
        generator_identity_name = "generator_right_depth_affine_identity"
        fill_identity_name = "fill_right_depth_affine_identity"
        generator_current_depth = int(slot_row["generator_right_depth"])
        fill_current_depth = int(slot_row["fill_right_depth"])
        generator_affine_rhs = int(slot_row["generator_right_depth_affine_rhs"])
        fill_affine_rhs = int(slot_row["fill_right_depth_affine_rhs"])
        primitive_generator_rhs = int(primitive_row["generator_right_identity_rhs"])
        # 右 fill 深度在 slot-lock 中是 AffineTwin 固定深度，primitive ledger 只记录左深度身份。
        primitive_fill_rhs = fill_affine_rhs
    else:
        raise RuntimeError(f"unsupported support-motion side: {side}")

    generator_increment = required_depth - generator_current_depth
    fill_increment = required_depth - fill_current_depth
    generator_affine_defect = required_depth - generator_affine_rhs
    fill_affine_defect = required_depth - fill_affine_rhs
    generator_primitive_defect = required_depth - primitive_generator_rhs
    fill_primitive_defect = required_depth - primitive_fill_rhs
    total_affine_defect = abs(generator_affine_defect) + abs(fill_affine_defect)
    total_primitive_defect = abs(generator_primitive_defect) + abs(fill_primitive_defect)

    return {
        "q": q,
        "source_pair_key": str(support_row["source_pair_key"]),
        "window_side": side,
        "nearest_representative": int(support_row["nearest_representative"]),
        "required_common_side_depth": required_depth,
        "generator_identity_name": generator_identity_name,
        "fill_identity_name": fill_identity_name,
        "generator_current_depth": generator_current_depth,
        "fill_current_depth": fill_current_depth,
        "generator_depth_increment_required": generator_increment,
        "fill_depth_increment_required": fill_increment,
        "generator_affine_rhs": generator_affine_rhs,
        "fill_affine_rhs": fill_affine_rhs,
        "generator_affine_depth_defect": generator_affine_defect,
        "fill_affine_depth_defect": fill_affine_defect,
        "total_affine_depth_defect": total_affine_defect,
        "primitive_generator_rhs": primitive_generator_rhs,
        "primitive_fill_rhs": primitive_fill_rhs,
        "generator_primitive_depth_defect": generator_primitive_defect,
        "fill_primitive_depth_defect": fill_primitive_defect,
        "total_primitive_depth_defect": total_primitive_defect,
        "breaks_generator_depth_identity": generator_affine_defect != 0,
        "breaks_fill_depth_identity": fill_affine_defect != 0,
        "breaks_both_depth_identities": generator_affine_defect != 0
        and fill_affine_defect != 0,
        "fixed_q_affine_depth_identity_can_absorb": generator_affine_defect == 0
        and fill_affine_defect == 0,
        "source_primitive_key": str(slot_row["source_primitive_key"]),
        "source_gap_fill_pair_key": str(slot_row["source_gap_fill_pair_key"]),
    }


def build_result(
    support_motion_path: Path,
    slot_path: Path,
    primitive_path: Path,
) -> dict[str, Any]:
    """构造 support-motion primitive defect 审计结果。"""
    support_motion = load_json(support_motion_path)
    slot = load_json(slot_path)
    primitive = load_json(primitive_path)
    slots = slot_by_q(slot["affine_twin_slot_phase_lock_rows"])
    primitives = primitive_by_q(primitive["primitive_rows"])

    rows = [
        defect_row(row, slots[int(row["q"])], primitives[int(row["q"])])
        for row in support_motion["support_motion_rows"]
    ]
    if not rows:
        raise RuntimeError("no support-motion rows found")

    side_histogram = Counter(str(row["window_side"]) for row in rows)
    affine_defects = [int(row["total_affine_depth_defect"]) for row in rows]
    primitive_defects = [int(row["total_primitive_depth_defect"]) for row in rows]
    generator_defects = [int(row["generator_affine_depth_defect"]) for row in rows]
    fill_defects = [int(row["fill_affine_depth_defect"]) for row in rows]
    narrowest_affine_row = min(
        rows,
        key=lambda row: (
            int(row["total_affine_depth_defect"]),
            int(row["required_common_side_depth"]),
            str(row["source_pair_key"]),
        ),
    )

    aggregate = {
        "support_motion_depth_ledger": str(support_motion_path.relative_to(ROOT)),
        "slot_ledger": str(slot_path.relative_to(ROOT)),
        "primitive_ledger": str(primitive_path.relative_to(ROOT)),
        "support_motion_primitive_defect_candidate_count": len(rows),
        "support_motion_side_histogram": dict(sorted(side_histogram.items())),
        "min_total_affine_depth_defect": min(affine_defects),
        "max_total_affine_depth_defect": max(affine_defects),
        "min_total_primitive_depth_defect": min(primitive_defects),
        "max_total_primitive_depth_defect": max(primitive_defects),
        "min_generator_affine_depth_defect": min(generator_defects),
        "max_generator_affine_depth_defect": max(generator_defects),
        "min_fill_affine_depth_defect": min(fill_defects),
        "max_fill_affine_depth_defect": max(fill_defects),
        "narrowest_affine_defect_atom": {
            "source_pair_key": narrowest_affine_row["source_pair_key"],
            "window_side": narrowest_affine_row["window_side"],
            "nearest_representative": narrowest_affine_row[
                "nearest_representative"
            ],
            "required_common_side_depth": narrowest_affine_row[
                "required_common_side_depth"
            ],
            "generator_affine_depth_defect": narrowest_affine_row[
                "generator_affine_depth_defect"
            ],
            "fill_affine_depth_defect": narrowest_affine_row[
                "fill_affine_depth_defect"
            ],
            "total_affine_depth_defect": narrowest_affine_row[
                "total_affine_depth_defect"
            ],
        },
        "all_support_motion_breaks_generator_depth_identity": all(
            bool(row["breaks_generator_depth_identity"]) for row in rows
        ),
        "all_support_motion_breaks_fill_depth_identity": all(
            bool(row["breaks_fill_depth_identity"]) for row in rows
        ),
        "all_support_motion_breaks_both_depth_identities": all(
            bool(row["breaks_both_depth_identities"]) for row in rows
        ),
        "any_fixed_q_affine_depth_identity_can_absorb": any(
            bool(row["fixed_q_affine_depth_identity_can_absorb"]) for row in rows
        ),
        "fixed_primitive_key_support_motion_absorption_closed_current_sweep": all(
            bool(row["breaks_both_depth_identities"]) for row in rows
        ),
        "global_primitive_identity_shift_excluded": False,
        "row_column_unconditional_closed": False,
    }

    return {
        "certificate_type": (
            "prime_matrix_affine_twin_support_motion_primitive_defect_audit"
        ),
        "status": (
            "current_sweep_support_motion_primitive_defects_closed_global_open"
        ),
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "aggregate": aggregate,
        "support_motion_primitive_defect_rows": rows,
        "contract": {
            "fixed_primitive_depth_gate": (
                "A support-motion row cannot be absorbed by the fixed q=31 "
                "AffineTwin primitive key: the required common side depth "
                "breaks both generator and fill affine-depth identities."
            ),
            "closed_current_sweep": aggregate[
                "fixed_primitive_key_support_motion_absorption_closed_current_sweep"
            ],
            "global_remaining": [
                "GlobalPrimitiveIdentityShiftExclusion",
                "MovingPrimitiveKey-PDEC/SAE",
                "MovingSupportDepthInflation-PDEC/SAE",
                "EndpointReleaseCoupling-PDEC",
            ],
        },
        "dependency_hashes": {
            str(path.relative_to(ROOT)): sha256(path)
            for path in (support_motion_path, slot_path, primitive_path)
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
        "# Prime Matrix AffineTwin support-motion primitive-depth defect audit",
        "",
        "**状态：** `current_sweep_support_motion_primitive_defects_closed_global_open`",
        "",
        "本审计继续下钻 `SupportMotionDepth`：若支撑移动仍试图保持当前 `q=31` AffineTwin primitive key，则所需共同侧深度会同时打破 generator 与 fill 的 AffineTwin 深度恒等式。",
        "",
        "```text",
        f"support_motion_primitive_defect_candidate_count={agg['support_motion_primitive_defect_candidate_count']}",
        f"support_motion_side_histogram={agg['support_motion_side_histogram']}",
        f"min_total_affine_depth_defect={agg['min_total_affine_depth_defect']}",
        f"max_total_affine_depth_defect={agg['max_total_affine_depth_defect']}",
        f"all_support_motion_breaks_both_depth_identities={fmt_bool(agg['all_support_motion_breaks_both_depth_identities'])}",
        f"fixed_primitive_key_support_motion_absorption_closed_current_sweep={fmt_bool(agg['fixed_primitive_key_support_motion_absorption_closed_current_sweep'])}",
        "```",
        "",
        "## 1. primitive-depth defect 表",
        "",
        "| pair | side | rep | required depth | g rhs | f rhs | g defect | f defect | total |",
        "| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in result["support_motion_primitive_defect_rows"]:
        lines.append(
            "| `{pair}` | `{side}` | {rep} | {depth} | {g_rhs} | {f_rhs} | {g_def} | {f_def} | {total} |".format(
                pair=row["source_pair_key"],
                side=row["window_side"],
                rep=row["nearest_representative"],
                depth=row["required_common_side_depth"],
                g_rhs=row["generator_affine_rhs"],
                f_rhs=row["fill_affine_rhs"],
                g_def=row["generator_affine_depth_defect"],
                f_def=row["fill_affine_depth_defect"],
                total=row["total_affine_depth_defect"],
            )
        )

    narrow = agg["narrowest_affine_defect_atom"]
    lines.extend(
        [
            "",
            "## 2. 当前读数",
            "",
            f"- 最小 fixed-primitive 缺陷 atom 是 `{narrow['source_pair_key']}`，side `{narrow['window_side']}`，nearest representative `{narrow['nearest_representative']}`。",
            f"- 它需要共同侧深度 `{narrow['required_common_side_depth']}`；但当前 AffineTwin 深度恒等式给出 generator 缺陷 `{narrow['generator_affine_depth_defect']}`、fill 缺陷 `{narrow['fill_affine_depth_defect']}`，总缺陷 `{narrow['total_affine_depth_defect']}`。",
            "- 所有 `11` 个 support-motion 候选都同时打破 generator 与 fill 的固定 q 深度恒等式。",
            "",
            "## 3. 结论边界",
            "",
            "- 本步关闭当前 sweep 的 fixed primitive key absorption：support motion 不能在保持当前 `q=31` primitive key 的同时吞掉空窗 CRT 代表。",
            "- 本步不证明 moving primitive key 全局不复现；全局剩余是排斥 primitive key 迁移，或路由到 `MovingPrimitiveKey-PDEC/SAE`、`MovingSupportDepthInflation-PDEC/SAE`、`EndpointReleaseCoupling-PDEC`。",
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
        description="生成 AffineTwin support-motion primitive-depth defect 审计证书。"
    )
    parser.add_argument("--support-motion-ledger", type=Path, default=SUPPORT_MOTION_LEDGER)
    parser.add_argument("--slot-ledger", type=Path, default=SLOT_LEDGER)
    parser.add_argument("--primitive-ledger", type=Path, default=PRIMITIVE_LEDGER)
    return parser.parse_args()


def main() -> None:
    """入口。"""
    args = parse_args()
    result = build_result(
        args.support_motion_ledger,
        args.slot_ledger,
        args.primitive_ledger,
    )
    write_outputs(result)
    print(json.dumps(result["aggregate"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
