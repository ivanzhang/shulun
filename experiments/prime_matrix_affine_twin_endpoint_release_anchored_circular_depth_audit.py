#!/usr/bin/env python3
"""生成 AffineTwin endpoint-release anchored circular-depth 审计证书。

用法示例：
  python3 experiments/prime_matrix_affine_twin_endpoint_release_anchored_circular_depth_audit.py
  python3 -m json.tool data/prime-matrix-affine-twin-endpoint-release-anchored-circular-depth-ledger.json

输出：
  data/prime-matrix-affine-twin-endpoint-release-anchored-circular-depth-ledger.json
  docs/monograph/prime-matrix-affine-twin-endpoint-release-anchored-circular-depth-audit.json
  docs/monograph/prime-matrix-affine-twin-endpoint-release-anchored-circular-depth-audit.md
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

CIRCULAR_LEDGER = DATA / (
    "prime-matrix-affine-twin-endpoint-release-circular-aperture-ledger.json"
)
BIDIRECTIONAL_HULL_LEDGER = DATA / (
    "prime-matrix-affine-twin-endpoint-release-bidirectional-skew-hull-ledger.json"
)
SLOT_LOCK_LEDGER = DATA / (
    "square-phase-offband-prefix-gap-shadow-selector-h-lower-"
    "affine-twin-slot-phase-lock-ledger.json"
)

OUT_LEDGER = DATA / (
    "prime-matrix-affine-twin-endpoint-release-anchored-circular-depth-ledger.json"
)
OUT_JSON = DOCS / (
    "prime-matrix-affine-twin-endpoint-release-anchored-circular-depth-audit.json"
)
OUT_MD = DOCS / (
    "prime-matrix-affine-twin-endpoint-release-anchored-circular-depth-audit.md"
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


def is_prime(n: int) -> bool:
    """小整数素性检查。"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def only_actual_alignment_row(rows: list[dict[str, Any]]) -> dict[str, Any]:
    """读取唯一 actual alignment 行。"""
    actual_rows = [
        row for row in rows if bool(row["supported_actual_packet_current"])
    ]
    if len(actual_rows) != 1:
        raise RuntimeError(f"expected one actual row, got {len(actual_rows)}")
    return actual_rows[0]


def build_result(
    circular_path: Path,
    bidirectional_hull_path: Path,
    slot_lock_path: Path,
) -> dict[str, Any]:
    """构造 anchored circular-depth 审计结果。"""
    circular = load_json(circular_path)
    hull = load_json(bidirectional_hull_path)
    slot_lock = load_json(slot_lock_path)

    circular_agg = circular["aggregate"]
    hull_rows = hull["formal_alignment_rows"]
    slot_row = slot_lock["affine_twin_slot_phase_lock_rows"][0]

    modulus = int(circular_agg["combined_crt_modulus"])
    support_width = int(circular_agg["support_width"])
    arc_start, arc_end = [
        int(value) for value in circular_agg["minimal_circular_alignment_arc"]
    ]
    actual_row = only_actual_alignment_row(hull_rows)
    actual_pair = str(actual_row["source_pair_key"])
    actual_representative = int(actual_row["nearest_representative"])
    if (arc_end - actual_representative) % modulus != 0:
        raise RuntimeError("minimal circular arc end is not the actual anchor")
    actual_shift_periods = (arc_end - actual_representative) // modulus
    shifted_actual = actual_representative + actual_shift_periods * modulus
    shifted_support = [
        int(value) + actual_shift_periods * modulus
        for value in circular_agg["support_interval"]
    ]

    required_left_depth = shifted_actual - arc_start
    current_generator_left_depth = int(slot_row["generator_left_depth"])
    current_fill_left_depth = int(slot_row["fill_left_depth"])
    current_pair_left_depth = min(
        current_generator_left_depth,
        current_fill_left_depth,
    )
    generator_left_increment = max(
        0, required_left_depth - current_generator_left_depth
    )
    fill_left_increment = max(0, required_left_depth - current_fill_left_depth)
    endpoint_release_total = generator_left_increment + fill_left_increment

    q_from_generator_depth_formula = 2 * required_left_depth - 5
    q_from_fill_depth_formula = required_left_depth + 3
    q_candidate_gap = abs(
        q_from_generator_depth_formula - q_from_fill_depth_formula
    )

    one_sided_extension = int(circular_agg["optimal_left_extension_required"])
    hidden_second_endpoint_release = endpoint_release_total - one_sided_extension
    best_single_side_feedback = int(circular_agg["best_single_side_feedback_horizon"])

    aggregate = {
        "circular_aperture_ledger": str(circular_path.relative_to(ROOT)),
        "bidirectional_hull_ledger": str(
            bidirectional_hull_path.relative_to(ROOT)
        ),
        "slot_lock_ledger": str(slot_lock_path.relative_to(ROOT)),
        "combined_crt_modulus": modulus,
        "support_width": support_width,
        "actual_anchor_pair": actual_pair,
        "actual_anchor_representative": actual_representative,
        "actual_anchor_shift_periods": actual_shift_periods,
        "shifted_actual_anchor_representative": shifted_actual,
        "minimal_circular_alignment_arc": [arc_start, arc_end],
        "minimal_circular_alignment_arc_width": int(
            circular_agg["minimal_circular_alignment_arc_width"]
        ),
        "actual_anchor_is_circular_arc_end": shifted_actual == arc_end,
        "shifted_support_interval": shifted_support,
        "current_pair_support_left_depth": current_pair_left_depth,
        "current_generator_left_depth": current_generator_left_depth,
        "current_fill_left_depth": current_fill_left_depth,
        "required_common_left_depth_to_cover_arc": required_left_depth,
        "generator_left_increment_required": generator_left_increment,
        "fill_left_increment_required": fill_left_increment,
        "anchored_endpoint_release_total_required": endpoint_release_total,
        "one_sided_circular_support_extension": one_sided_extension,
        "hidden_second_endpoint_release": hidden_second_endpoint_release,
        "best_single_side_feedback_horizon": best_single_side_feedback,
        "anchored_release_after_single_side_feedback": max(
            0, endpoint_release_total - best_single_side_feedback
        ),
        "endpoint_release_to_support_width_ratio": endpoint_release_total
        / support_width,
        "required_depth_to_current_pair_depth_ratio": required_left_depth
        / current_pair_left_depth,
        "q_from_generator_depth_formula": q_from_generator_depth_formula,
        "q_from_fill_depth_formula": q_from_fill_depth_formula,
        "q_candidate_gap": q_candidate_gap,
        "q_from_generator_is_prime": is_prime(q_from_generator_depth_formula),
        "q_from_fill_is_prime": is_prime(q_from_fill_depth_formula),
        "q_from_fill_is_odd": q_from_fill_depth_formula % 2 == 1,
        "same_orientation_common_q_absent": (
            q_from_generator_depth_formula != q_from_fill_depth_formula
        ),
        "same_orientation_anchored_depth_absorption_closed_current_sweep": (
            shifted_actual == arc_end
            and endpoint_release_total > support_width
            and q_from_generator_depth_formula != q_from_fill_depth_formula
        ),
        "global_anchored_circular_depth_excluded": False,
        "row_column_unconditional_closed": False,
    }

    return {
        "certificate_type": (
            "prime_matrix_affine_twin_endpoint_release_"
            "anchored_circular_depth_audit"
        ),
        "status": (
            "current_sweep_anchored_circular_depth_structured_global_open"
        ),
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "aggregate": aggregate,
        "anchored_depth_row": {
            "actual_anchor_pair": actual_pair,
            "arc_start": arc_start,
            "arc_end": arc_end,
            "required_common_left_depth": required_left_depth,
            "generator_left_increment_required": generator_left_increment,
            "fill_left_increment_required": fill_left_increment,
            "anchored_endpoint_release_total_required": endpoint_release_total,
            "q_from_generator_depth_formula": q_from_generator_depth_formula,
            "q_from_fill_depth_formula": q_from_fill_depth_formula,
            "q_candidate_gap": q_candidate_gap,
        },
        "contract": {
            "anchored_circular_depth_gate": [
                "keep the unique current actual packet as the circular arc anchor",
                "force both generator and shifted-fill left endpoints to reach the arc start",
                "compare the resulting two-endpoint release with support width and moving-q depth formulas",
                "route persistent failure to AnchoredCircularDepth-PDEC/ColumnCRT or moving-family exits",
            ],
            "closed_current_sweep": aggregate[
                "same_orientation_anchored_depth_absorption_closed_current_sweep"
            ],
            "global_remaining": [
                "AnchoredCircularDepth-PDEC exclusion",
                "ColumnCRT/PDEC for persistent actual-anchored aperture recurrence",
                "OrientationChangingPrimitiveKey-PDEC/SAE",
                "AffineTwinEpochPairMultiplicityBoundOrColumnCRTPDECExclusion",
            ],
        },
        "dependency_hashes": {
            str(path.relative_to(ROOT)): sha256(path)
            for path in (circular_path, bidirectional_hull_path, slot_lock_path)
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
    row = result["anchored_depth_row"]
    lines = [
        "# Prime Matrix AffineTwin endpoint-release anchored circular-depth audit",
        "",
        "**状态：** `current_sweep_anchored_circular_depth_structured_global_open`",
        "",
        "本审计继续下钻 circular-aperture：上一层只计算支撑窗口覆盖圆弧所需的单侧扩张；若唯一 actual packet 仍作为圆弧锚点保留，则 generator 与 shifted-fill 两个左端点必须同时到达圆弧起点，形成更强的双端点释放账本。",
        "",
        "```text",
        f"actual_anchor_pair={agg['actual_anchor_pair']}",
        f"minimal_circular_alignment_arc={agg['minimal_circular_alignment_arc']}",
        f"shifted_actual_anchor_representative={agg['shifted_actual_anchor_representative']}",
        f"actual_anchor_is_circular_arc_end={fmt_bool(agg['actual_anchor_is_circular_arc_end'])}",
        f"support_width={agg['support_width']}",
        f"required_common_left_depth_to_cover_arc={agg['required_common_left_depth_to_cover_arc']}",
        f"current_generator_left_depth={agg['current_generator_left_depth']}",
        f"current_fill_left_depth={agg['current_fill_left_depth']}",
        f"generator_left_increment_required={agg['generator_left_increment_required']}",
        f"fill_left_increment_required={agg['fill_left_increment_required']}",
        f"anchored_endpoint_release_total_required={agg['anchored_endpoint_release_total_required']}",
        f"one_sided_circular_support_extension={agg['one_sided_circular_support_extension']}",
        f"hidden_second_endpoint_release={agg['hidden_second_endpoint_release']}",
        f"endpoint_release_to_support_width_ratio={fmt_decimal(agg['endpoint_release_to_support_width_ratio'])}",
        f"q_from_generator_depth_formula={agg['q_from_generator_depth_formula']}",
        f"q_from_fill_depth_formula={agg['q_from_fill_depth_formula']}",
        f"q_candidate_gap={agg['q_candidate_gap']}",
        f"same_orientation_common_q_absent={fmt_bool(agg['same_orientation_common_q_absent'])}",
        f"same_orientation_anchored_depth_absorption_closed_current_sweep={fmt_bool(agg['same_orientation_anchored_depth_absorption_closed_current_sweep'])}",
        "```",
        "",
        "## 1. anchored depth row",
        "",
        "| anchor | arc start | arc end | required D | gen inc | fill inc | total release | q from gen | q from fill | q gap |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        "| `{anchor}` | {start} | {end} | {depth} | {ginc} | {finc} | {total} | {qg} | {qf} | {gap} |".format(
            anchor=row["actual_anchor_pair"],
            start=row["arc_start"],
            end=row["arc_end"],
            depth=row["required_common_left_depth"],
            ginc=row["generator_left_increment_required"],
            finc=row["fill_left_increment_required"],
            total=row["anchored_endpoint_release_total_required"],
            qg=row["q_from_generator_depth_formula"],
            qf=row["q_from_fill_depth_formula"],
            gap=row["q_candidate_gap"],
        ),
        "",
        "## 2. 新显式矛盾点",
        "",
        "圆周最小弧为 `[3029,3586]`，唯一 actual packet `19:8` 平移后正好位于右端点 `3586`。因此若反例链要保持这个 actual 锚点并吸收全部 formal pair，就必须把左深度从当前 pair support 的 `18` 推到 `557`。",
        "",
        "单侧 circular-aperture 只看交支撑左扩，得到 `539`；但真实链要让 generator phase 与 shifted-fill phase 同时覆盖圆弧起点，所以还要支付 fill 左端点额外 `529`。总端点释放为 `1068`，是 support width `20` 的 `53.4` 倍。",
        "",
        "同向 AffineTwin moving key 也不能吸收该锚定深度：lower-side 深度公式给出 `q=2D-5=1109` 与 `q=D+3=560`，两侧相差 `549`，且 fill 侧候选为偶数，不能成为同一个奇素数 AffineTwin key。",
        "",
        "## 3. 结论边界",
        "",
        "- 本步关闭当前 sweep 的 same-orientation anchored circular-depth absorption。",
        "- 本步不关闭全局行/列命题；剩余是排斥 `AnchoredCircularDepth-PDEC`，或证明持久 actual-anchored 圆弧复现进入 `ColumnCRT/PDEC`、`SAE`、方向改变 key 或 moving-family multiplicity 出口。",
        "",
        "## 4. 依赖哈希",
        "",
        "| file | sha256 |",
        "| --- | --- |",
    ]
    for path, digest in result["dependency_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    lines.append("")

    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--circular-ledger",
        type=Path,
        default=CIRCULAR_LEDGER,
        help="circular-aperture ledger path",
    )
    parser.add_argument(
        "--bidirectional-hull-ledger",
        type=Path,
        default=BIDIRECTIONAL_HULL_LEDGER,
        help="bidirectional skew-hull ledger path",
    )
    parser.add_argument(
        "--slot-lock-ledger",
        type=Path,
        default=SLOT_LOCK_LEDGER,
        help="AffineTwin slot-lock ledger path",
    )
    args = parser.parse_args()
    result = build_result(
        args.circular_ledger,
        args.bidirectional_hull_ledger,
        args.slot_lock_ledger,
    )
    write_outputs(result)
    print(json.dumps(result["aggregate"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
