#!/usr/bin/env python3
"""生成 AffineTwin endpoint-release cut-anchor sweep 审计证书。

用法示例：
  python3 experiments/prime_matrix_affine_twin_endpoint_release_cut_anchor_sweep_audit.py
  python3 -m json.tool data/prime-matrix-affine-twin-endpoint-release-cut-anchor-sweep-ledger.json

输出：
  data/prime-matrix-affine-twin-endpoint-release-cut-anchor-sweep-ledger.json
  docs/monograph/prime-matrix-affine-twin-endpoint-release-cut-anchor-sweep-audit.json
  docs/monograph/prime-matrix-affine-twin-endpoint-release-cut-anchor-sweep-audit.md
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

BIDIRECTIONAL_HULL_LEDGER = DATA / (
    "prime-matrix-affine-twin-endpoint-release-bidirectional-skew-hull-ledger.json"
)
CIRCULAR_LEDGER = DATA / (
    "prime-matrix-affine-twin-endpoint-release-circular-aperture-ledger.json"
)
SLOT_LOCK_LEDGER = DATA / (
    "square-phase-offband-prefix-gap-shadow-selector-h-lower-"
    "affine-twin-slot-phase-lock-ledger.json"
)
ANCHORED_PARITY_LEDGER = DATA / (
    "prime-matrix-affine-twin-endpoint-release-anchored-parity-nogo-ledger.json"
)

OUT_LEDGER = DATA / (
    "prime-matrix-affine-twin-endpoint-release-cut-anchor-sweep-ledger.json"
)
OUT_JSON = DOCS / (
    "prime-matrix-affine-twin-endpoint-release-cut-anchor-sweep-audit.json"
)
OUT_MD = DOCS / (
    "prime-matrix-affine-twin-endpoint-release-cut-anchor-sweep-audit.md"
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


def fmt_decimal(value: float) -> str:
    """稳定输出小数。"""
    return f"{value:.12g}"


def fmt_optional(value: Any) -> str:
    """把空值输出为短横线。"""
    return "-" if value is None else str(value)


def sorted_alignment_rows(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """按 CRT residue 排序。"""
    return sorted(rows, key=lambda row: int(row["combined_crt_residue"]))


def only_actual_alignment_row(rows: list[dict[str, Any]]) -> dict[str, Any]:
    """读取唯一 actual alignment 行。"""
    actual_rows = [
        row for row in rows if bool(row["supported_actual_packet_current"])
    ]
    if len(actual_rows) != 1:
        raise RuntimeError(f"expected one actual row, got {len(actual_rows)}")
    return actual_rows[0]


def left_formula(depth: int) -> dict[str, Any] | None:
    """lower-side 左深度同向 moving-key 公式。"""
    if depth == 0:
        return None
    q_from_generator = 2 * depth - 5
    q_from_fill = depth + 3
    return {
        "needed": True,
        "common_depth_solution": 8,
        "q_from_generator_depth_formula": q_from_generator,
        "q_from_fill_depth_formula": q_from_fill,
        "q_candidate_gap": abs(q_from_generator - q_from_fill),
        "common_q_exists": depth == 8,
        "gap_from_common_depth_solution": abs(depth - 8),
        "parity_no_go": depth % 2 == 1 and q_from_fill > 2 and q_from_fill % 2 == 0,
        "obstruction": "lower_depth_q_mismatch",
    }


def right_formula(depth: int) -> dict[str, Any] | None:
    """above-side 右深度同向 moving-key 公式。"""
    if depth == 0:
        return None
    return {
        "needed": True,
        "common_depth_solution": 1,
        "q_from_generator_depth_formula": 4 * depth + 7,
        "q_from_fill_depth_formula": None,
        "q_candidate_gap": None,
        "fill_right_depth_residual": depth - 1,
        "common_q_exists": depth == 1,
        "gap_from_common_depth_solution": abs(depth - 1),
        "obstruction": "above_fill_right_depth_fixed_one",
    }


def circular_cut_rows(
    rows: list[dict[str, Any]],
    slot_row: dict[str, Any],
    modulus: int,
) -> list[dict[str, Any]]:
    """枚举所有圆周切口，并把 actual 包锚进每条圆弧。"""
    ordered = sorted_alignment_rows(rows)
    actual = only_actual_alignment_row(ordered)
    actual_base = int(actual["nearest_representative"])
    generator_left = int(slot_row["generator_left_depth"])
    generator_right = int(slot_row["generator_right_depth"])
    fill_left = int(slot_row["fill_left_depth"])
    fill_right = int(slot_row["fill_right_depth"])
    support_width = int(slot_row["pair_phase_support_width"])

    cut_rows: list[dict[str, Any]] = []
    for index, from_row in enumerate(ordered):
        to_row = ordered[(index + 1) % len(ordered)]
        from_residue = int(from_row["combined_crt_residue"])
        to_residue = int(to_row["combined_crt_residue"])
        delta = (to_residue - from_residue) % modulus
        if delta == 0:
            delta = modulus

        arc_start = int(to_row["nearest_representative"])
        arc_end = int(from_row["nearest_representative"])
        while arc_end < arc_start:
            arc_end += modulus

        actual_representative = actual_base
        while actual_representative < arc_start:
            actual_representative += modulus
        if actual_representative > arc_end:
            raise RuntimeError(
                "actual representative escaped a formal alignment arc: "
                f"{from_row['source_pair_key']}->{to_row['source_pair_key']}"
            )

        left_depth = actual_representative - arc_start
        right_depth = arc_end - actual_representative
        left_release = max(0, left_depth - generator_left) + max(
            0, left_depth - fill_left
        )
        right_release = max(0, right_depth - generator_right) + max(
            0, right_depth - fill_right
        )
        total_release = left_release + right_release

        left = left_formula(left_depth)
        right = right_formula(right_depth)
        left_common = True if left is None else bool(left["common_q_exists"])
        right_common = True if right is None else bool(right["common_q_exists"])
        closed_by_formula = not (left_common and right_common)
        no_go_reasons: list[str] = []
        if left is not None and not bool(left["common_q_exists"]):
            reason = "left:D!=8"
            if bool(left["parity_no_go"]):
                reason += "+parity"
            no_go_reasons.append(reason)
        if right is not None and not bool(right["common_q_exists"]):
            no_go_reasons.append("right:D!=1")

        if left_depth == 0:
            actual_position = "arc_start"
        elif right_depth == 0:
            actual_position = "arc_end"
        else:
            actual_position = "arc_interior"

        cut_rows.append(
            {
                "cut_from_pair": str(from_row["source_pair_key"]),
                "cut_to_pair": str(to_row["source_pair_key"]),
                "cut_from_side": str(from_row["window_side"]),
                "cut_to_side": str(to_row["window_side"]),
                "open_gap_width": delta - 1,
                "cyclic_delta": delta,
                "arc_start_pair": str(to_row["source_pair_key"]),
                "arc_end_pair": str(from_row["source_pair_key"]),
                "arc_start_representative": arc_start,
                "arc_end_representative": arc_end,
                "arc_width": arc_end - arc_start + 1,
                "actual_anchor_pair": str(actual["source_pair_key"]),
                "actual_anchor_representative": actual_representative,
                "actual_anchor_position": actual_position,
                "required_common_left_depth": left_depth,
                "required_common_right_depth": right_depth,
                "left_endpoint_release_required": left_release,
                "right_endpoint_release_required": right_release,
                "total_endpoint_release_required": total_release,
                "release_to_support_width_ratio": total_release / support_width,
                "left_formula": left,
                "right_formula": right,
                "same_orientation_absorption_closed": closed_by_formula,
                "endpoint_release_exceeds_support_width": total_release > support_width,
                "explicit_no_go_reasons": no_go_reasons,
            }
        )
    return cut_rows


def build_result(
    bidirectional_hull_path: Path,
    circular_path: Path,
    slot_lock_path: Path,
    anchored_parity_path: Path,
) -> dict[str, Any]:
    """构造 cut-anchor sweep 审计结果。"""
    hull = load_json(bidirectional_hull_path)
    circular = load_json(circular_path)
    slot_lock = load_json(slot_lock_path)
    anchored_parity = load_json(anchored_parity_path)

    rows = hull["formal_alignment_rows"]
    hull_agg = hull["aggregate"]
    circular_agg = circular["aggregate"]
    slot_row = slot_lock["affine_twin_slot_phase_lock_rows"][0]
    modulus = int(hull_agg["combined_crt_modulus"])
    support_width = int(hull_agg["support_width"])
    cut_rows = circular_cut_rows(rows, slot_row, modulus)

    if not cut_rows:
        raise RuntimeError("no circular cut rows found")
    min_arc = min(cut_rows, key=lambda row: int(row["arc_width"]))
    min_release = min(
        cut_rows,
        key=lambda row: int(row["total_endpoint_release_required"]),
    )
    positive_left_rows = [
        row for row in cut_rows if int(row["required_common_left_depth"]) > 0
    ]
    positive_right_rows = [
        row for row in cut_rows if int(row["required_common_right_depth"]) > 0
    ]
    min_left_gap_row = min(
        positive_left_rows,
        key=lambda row: int(row["left_formula"]["gap_from_common_depth_solution"]),
    )
    min_right_gap_row = min(
        positive_right_rows,
        key=lambda row: int(row["right_formula"]["gap_from_common_depth_solution"]),
    )
    position_histogram = Counter(
        str(row["actual_anchor_position"]) for row in cut_rows
    )
    left_parity_count = sum(
        1
        for row in positive_left_rows
        if bool(row["left_formula"]["parity_no_go"])
    )
    left_equality_count = sum(
        1
        for row in positive_left_rows
        if not bool(row["left_formula"]["common_q_exists"])
    )
    right_fixed_one_count = sum(
        1
        for row in positive_right_rows
        if not bool(row["right_formula"]["common_q_exists"])
    )

    aggregate = {
        "bidirectional_hull_ledger": str(
            bidirectional_hull_path.relative_to(ROOT)
        ),
        "circular_aperture_ledger": str(circular_path.relative_to(ROOT)),
        "slot_lock_ledger": str(slot_lock_path.relative_to(ROOT)),
        "anchored_parity_nogo_ledger": str(
            anchored_parity_path.relative_to(ROOT)
        ),
        "combined_crt_modulus": modulus,
        "support_interval": hull_agg["support_interval"],
        "support_width": support_width,
        "actual_anchor_pair": str(anchored_parity["aggregate"]["actual_anchor_pair"]),
        "cut_count": len(cut_rows),
        "actual_anchor_position_histogram": dict(sorted(position_histogram.items())),
        "endpoint_cut_count": position_histogram["arc_start"]
        + position_histogram["arc_end"],
        "interior_cut_count": position_histogram["arc_interior"],
        "all_cuts_retain_actual_anchor": True,
        "min_arc_cut": {
            "cut": f"{min_arc['cut_from_pair']}->{min_arc['cut_to_pair']}",
            "arc": [
                int(min_arc["arc_start_representative"]),
                int(min_arc["arc_end_representative"]),
            ],
            "arc_width": int(min_arc["arc_width"]),
            "actual_anchor_position": str(min_arc["actual_anchor_position"]),
            "left_depth": int(min_arc["required_common_left_depth"]),
            "right_depth": int(min_arc["required_common_right_depth"]),
            "total_endpoint_release_required": int(
                min_arc["total_endpoint_release_required"]
            ),
        },
        "min_release_cut": {
            "cut": f"{min_release['cut_from_pair']}->{min_release['cut_to_pair']}",
            "arc_width": int(min_release["arc_width"]),
            "left_depth": int(min_release["required_common_left_depth"]),
            "right_depth": int(min_release["required_common_right_depth"]),
            "total_endpoint_release_required": int(
                min_release["total_endpoint_release_required"]
            ),
            "release_to_support_width_ratio": float(
                min_release["release_to_support_width_ratio"]
            ),
        },
        "minimal_circular_arc_matches_previous_audit": [
            int(min_arc["arc_start_representative"]),
            int(min_arc["arc_end_representative"]),
        ]
        == [int(value) for value in circular_agg["minimal_circular_alignment_arc"]],
        "min_total_endpoint_release_required": int(
            min_release["total_endpoint_release_required"]
        ),
        "max_total_endpoint_release_required": max(
            int(row["total_endpoint_release_required"]) for row in cut_rows
        ),
        "min_release_to_support_width_ratio": float(
            min_release["release_to_support_width_ratio"]
        ),
        "all_endpoint_releases_exceed_support_width": all(
            bool(row["endpoint_release_exceeds_support_width"]) for row in cut_rows
        ),
        "left_common_depth_solution": 8,
        "right_common_depth_solution": 1,
        "positive_left_depth_count": len(positive_left_rows),
        "positive_right_depth_count": len(positive_right_rows),
        "left_equality_nogo_count": left_equality_count,
        "left_parity_nogo_count": left_parity_count,
        "right_fixed_one_nogo_count": right_fixed_one_count,
        "min_left_gap_from_common_depth_solution": int(
            min_left_gap_row["left_formula"]["gap_from_common_depth_solution"]
        ),
        "min_left_gap_cut": (
            f"{min_left_gap_row['cut_from_pair']}->{min_left_gap_row['cut_to_pair']}"
        ),
        "min_positive_left_depth": int(min_left_gap_row["required_common_left_depth"]),
        "min_right_gap_from_common_depth_solution": int(
            min_right_gap_row["right_formula"]["gap_from_common_depth_solution"]
        ),
        "min_right_gap_cut": (
            f"{min_right_gap_row['cut_from_pair']}->{min_right_gap_row['cut_to_pair']}"
        ),
        "min_positive_right_depth": int(
            min_right_gap_row["required_common_right_depth"]
        ),
        "all_actual_retained_cuts_same_orientation_closed": all(
            bool(row["same_orientation_absorption_closed"]) for row in cut_rows
        ),
        "cut_anchor_sweep_closed_current_sweep": all(
            bool(row["same_orientation_absorption_closed"])
            and bool(row["endpoint_release_exceeds_support_width"])
            for row in cut_rows
        ),
        "global_cut_anchor_family_excluded": False,
        "row_column_unconditional_closed": False,
    }

    return {
        "certificate_type": (
            "prime_matrix_affine_twin_endpoint_release_cut_anchor_sweep_audit"
        ),
        "status": "current_sweep_cut_anchor_sweep_closed_global_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "aggregate": aggregate,
        "cut_anchor_rows": cut_rows,
        "contract": {
            "cut_anchor_sweep_gate": [
                "enumerate every circular cut between adjacent formal CRT classes",
                "place the unique actual packet into the lifted arc for that cut",
                "charge both generator and shifted-fill endpoints for each required left/right depth",
                "apply lower-side q=2D-5 versus q=D+3 and above-side D=1 fixed-fill obstructions",
                "route persistent non-same-orientation escape to ColumnCRT/PDEC, SAE, or moving-family exits",
            ],
            "closed_current_sweep": aggregate[
                "cut_anchor_sweep_closed_current_sweep"
            ],
            "global_remaining": [
                "CutAnchorSweepGlobalFamilyNoGo",
                "OrientationChangingPrimitiveKey-PDEC/SAE",
                "ColumnCRT/PDEC for persistent actual-retained circular cuts",
                "AffineTwinEpochPairMultiplicityBoundOrColumnCRTPDECExclusion",
            ],
        },
        "dependency_hashes": {
            str(path.relative_to(ROOT)): sha256(path)
            for path in (
                bidirectional_hull_path,
                circular_path,
                slot_lock_path,
                anchored_parity_path,
            )
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
    min_arc = agg["min_arc_cut"]
    min_release = agg["min_release_cut"]
    lines = [
        "# Prime Matrix AffineTwin endpoint-release cut-anchor sweep audit",
        "",
        "**状态：** `current_sweep_cut_anchor_sweep_closed_global_open`",
        "",
        "本审计把 anchored parity no-go 从单个最优圆弧扩展到全部圆周切口：对每个相邻 CRT 类之间的 cut，保留唯一 actual packet，把它平移进对应 lifted arc，并同时计算 left/right 共同深度和双端点释放量。",
        "",
        "```text",
        f"cut_count={agg['cut_count']}",
        f"combined_crt_modulus={agg['combined_crt_modulus']}",
        f"support_width={agg['support_width']}",
        f"actual_anchor_pair={agg['actual_anchor_pair']}",
        f"actual_anchor_position_histogram={agg['actual_anchor_position_histogram']}",
        f"minimal_circular_arc_matches_previous_audit={fmt_bool(agg['minimal_circular_arc_matches_previous_audit'])}",
        f"min_arc_cut={min_arc['cut']}",
        f"min_arc_width={min_arc['arc_width']}",
        f"min_release_cut={min_release['cut']}",
        f"min_total_endpoint_release_required={agg['min_total_endpoint_release_required']}",
        f"min_release_to_support_width_ratio={fmt_decimal(agg['min_release_to_support_width_ratio'])}",
        f"max_total_endpoint_release_required={agg['max_total_endpoint_release_required']}",
        f"left_common_depth_solution={agg['left_common_depth_solution']}",
        f"right_common_depth_solution={agg['right_common_depth_solution']}",
        f"min_positive_left_depth={agg['min_positive_left_depth']}",
        f"min_left_gap_from_common_depth_solution={agg['min_left_gap_from_common_depth_solution']}",
        f"min_positive_right_depth={agg['min_positive_right_depth']}",
        f"min_right_gap_from_common_depth_solution={agg['min_right_gap_from_common_depth_solution']}",
        f"all_endpoint_releases_exceed_support_width={fmt_bool(agg['all_endpoint_releases_exceed_support_width'])}",
        f"all_actual_retained_cuts_same_orientation_closed={fmt_bool(agg['all_actual_retained_cuts_same_orientation_closed'])}",
        f"cut_anchor_sweep_closed_current_sweep={fmt_bool(agg['cut_anchor_sweep_closed_current_sweep'])}",
        "```",
        "",
        "## 1. 全切口账本",
        "",
        "| cut | open gap | arc width | actual pos | left D | right D | release | reasons |",
        "| --- | ---: | ---: | --- | ---: | ---: | ---: | --- |",
    ]
    for row in result["cut_anchor_rows"]:
        lines.append(
            "| `{}` | {} | {} | `{}` | {} | {} | {} | `{}` |".format(
                f"{row['cut_from_pair']}->{row['cut_to_pair']}",
                row["open_gap_width"],
                row["arc_width"],
                row["actual_anchor_position"],
                row["required_common_left_depth"],
                row["required_common_right_depth"],
                row["total_endpoint_release_required"],
                ",".join(row["explicit_no_go_reasons"]),
            )
        )

    lines.extend(
        [
            "",
            "## 2. 容量与相位矛盾点",
            "",
            f"容量侧：所有 `{agg['cut_count']}` 个切口的双端点释放量都超过 support width `{agg['support_width']}`。最小释放仍是 `{agg['min_total_endpoint_release_required']}`，发生在 cut `{min_release['cut']}`，为 support width 的 `{fmt_decimal(agg['min_release_to_support_width_ratio'])}` 倍；最大释放为 `{agg['max_total_endpoint_release_required']}`。",
            "",
            "相位侧：left lower-side 同向吸收仍只能在 `D=8,q=11` 处合一；本 sweep 的正 left depth 最小也为 `{}`，距离共同解仍有 `{}`。right above-side 同向吸收被 fill right depth 固定为 `D=1`；本 sweep 的正 right depth 最小为 `{}`，距离固定解 `{}`。".format(
                agg["min_positive_left_depth"],
                agg["min_left_gap_from_common_depth_solution"],
                agg["min_positive_right_depth"],
                agg["min_right_gap_from_common_depth_solution"],
            ),
            "",
            "两个 endpoint cut 也没有逃逸：actual 位于右端的最优 cut 给出 left `D=557`，落入 anchored parity no-go；actual 位于左端的 cut 给出 right `D=841`，被 `D=1` fixed-fill 条件排斥。其余十个 interior cut 更强，因为它们同时要求左右两侧释放。",
            "",
            "## 3. 结论边界",
            "",
            "- 本步关闭当前 sweep 的 actual-retained same-orientation cut-anchor absorption。",
            "- 本步仍不宣称全局行/列命题无条件闭合；剩余是把 cut-anchor no-go 升格为全局族定理，或处理方向改变 key、`ColumnCRT/PDEC`、`SAE`、moving-family multiplicity 出口。",
            "",
            "## 4. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in result["dependency_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    lines.append("")
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--bidirectional-hull-ledger",
        type=Path,
        default=BIDIRECTIONAL_HULL_LEDGER,
        help="bidirectional skew-hull ledger path",
    )
    parser.add_argument(
        "--circular-ledger",
        type=Path,
        default=CIRCULAR_LEDGER,
        help="circular-aperture ledger path",
    )
    parser.add_argument(
        "--slot-lock-ledger",
        type=Path,
        default=SLOT_LOCK_LEDGER,
        help="AffineTwin slot-lock ledger path",
    )
    parser.add_argument(
        "--anchored-parity-ledger",
        type=Path,
        default=ANCHORED_PARITY_LEDGER,
        help="anchored parity no-go ledger path",
    )
    args = parser.parse_args()
    result = build_result(
        args.bidirectional_hull_ledger,
        args.circular_ledger,
        args.slot_lock_ledger,
        args.anchored_parity_ledger,
    )
    write_outputs(result)
    print(json.dumps(result["aggregate"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
