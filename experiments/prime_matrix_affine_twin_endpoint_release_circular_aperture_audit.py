#!/usr/bin/env python3
"""生成 AffineTwin endpoint-release circular-aperture 审计证书。

用法示例：
  python3 experiments/prime_matrix_affine_twin_endpoint_release_circular_aperture_audit.py
  python3 -m json.tool data/prime-matrix-affine-twin-endpoint-release-circular-aperture-ledger.json

输出：
  data/prime-matrix-affine-twin-endpoint-release-circular-aperture-ledger.json
  docs/monograph/prime-matrix-affine-twin-endpoint-release-circular-aperture-audit.json
  docs/monograph/prime-matrix-affine-twin-endpoint-release-circular-aperture-audit.md
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

BIDIRECTIONAL_HULL_LEDGER = DATA / (
    "prime-matrix-affine-twin-endpoint-release-bidirectional-skew-hull-ledger.json"
)

OUT_LEDGER = DATA / (
    "prime-matrix-affine-twin-endpoint-release-circular-aperture-ledger.json"
)
OUT_JSON = DOCS / (
    "prime-matrix-affine-twin-endpoint-release-circular-aperture-audit.json"
)
OUT_MD = DOCS / (
    "prime-matrix-affine-twin-endpoint-release-circular-aperture-audit.md"
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


def sorted_alignment_rows(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """按 CRT residue 排序，并保留当前最近代表。"""
    return sorted(rows, key=lambda row: int(row["combined_crt_residue"]))


def circular_gap_rows(rows: list[dict[str, Any]], modulus: int) -> list[dict[str, Any]]:
    """计算相邻 CRT 类之间的圆周空弧。"""
    ordered = sorted_alignment_rows(rows)
    gaps: list[dict[str, Any]] = []
    for index, row in enumerate(ordered):
        next_row = ordered[(index + 1) % len(ordered)]
        residue = int(row["combined_crt_residue"])
        next_residue = int(next_row["combined_crt_residue"])
        delta = (next_residue - residue) % modulus
        if delta == 0:
            delta = modulus
        gaps.append(
            {
                "from_pair": str(row["source_pair_key"]),
                "to_pair": str(next_row["source_pair_key"]),
                "from_residue": residue,
                "to_residue": next_residue,
                "from_representative": int(row["nearest_representative"]),
                "to_representative": int(next_row["nearest_representative"]),
                "from_supported_actual": bool(row["supported_actual_packet_current"]),
                "to_supported_actual": bool(next_row["supported_actual_packet_current"]),
                "from_side": str(row["window_side"]),
                "to_side": str(next_row["window_side"]),
                "cyclic_delta": delta,
                "open_gap_width": delta - 1,
            }
        )
    return gaps


def lifted_arc_from_gap(
    gap: dict[str, Any],
    rows: list[dict[str, Any]],
    modulus: int,
) -> dict[str, Any]:
    """删去指定最大空弧后，给出覆盖全部点的最小圆弧。"""
    start_residue = int(gap["to_residue"])
    end_residue = int(gap["from_residue"])
    residue_to_row = {int(row["combined_crt_residue"]): row for row in rows}
    start_rep = int(residue_to_row[start_residue]["nearest_representative"])
    end_rep = int(residue_to_row[end_residue]["nearest_representative"])
    while end_rep < start_rep:
        end_rep += modulus
    width = end_rep - start_rep + 1
    return {
        "arc_start_pair": str(gap["to_pair"]),
        "arc_end_pair": str(gap["from_pair"]),
        "arc_start_representative": start_rep,
        "arc_end_representative": end_rep,
        "arc_width": width,
    }


def optimal_shifted_support(
    support: list[int],
    arc_start: int,
    arc_end: int,
    modulus: int,
) -> dict[str, Any]:
    """选择最优周期平移的支撑窗口，使覆盖圆弧所需扩张最小。"""
    support_lo, support_hi = support
    candidates: list[dict[str, Any]] = []
    for shift in range(-3, 5):
        lo_value = support_lo + shift * modulus
        hi_value = support_hi + shift * modulus
        left_extension = max(0, lo_value - arc_start)
        right_extension = max(0, arc_end - hi_value)
        total_extension = left_extension + right_extension
        candidates.append(
            {
                "support_shift_periods": shift,
                "shifted_support_interval": [lo_value, hi_value],
                "left_extension_required": left_extension,
                "right_extension_required": right_extension,
                "total_extension_required": total_extension,
                "covers_arc_without_extension": total_extension == 0,
            }
        )
    return min(
        candidates,
        key=lambda row: (
            int(row["total_extension_required"]),
            max(int(row["left_extension_required"]), int(row["right_extension_required"])),
            abs(int(row["support_shift_periods"])),
        ),
    )


def build_result(bidirectional_hull_path: Path) -> dict[str, Any]:
    """构造 circular-aperture 审计结果。"""
    hull = load_json(bidirectional_hull_path)
    rows = hull["formal_alignment_rows"]
    aggregate_in = hull["aggregate"]
    modulus = int(aggregate_in["combined_crt_modulus"])
    support = [int(value) for value in aggregate_in["support_interval"]]
    support_width = int(aggregate_in["support_width"])
    p_delay = int(aggregate_in["affine_p_delay"])
    left_feedback_horizon = int(aggregate_in["current_left_feedback_horizon"])
    right_feedback_horizon = int(aggregate_in["current_right_feedback_horizon"])
    best_single_side_feedback = max(left_feedback_horizon, right_feedback_horizon)

    gaps = circular_gap_rows(rows, modulus)
    largest_gap = max(
        gaps,
        key=lambda row: (
            int(row["open_gap_width"]),
            bool(row["from_supported_actual"]),
            str(row["from_pair"]),
        ),
    )
    arc = lifted_arc_from_gap(largest_gap, rows, modulus)
    support_choice = optimal_shifted_support(
        support,
        int(arc["arc_start_representative"]),
        int(arc["arc_end_representative"]),
        modulus,
    )
    p_delay_gaps = [row for row in gaps if int(row["open_gap_width"]) == p_delay]
    sorted_gaps = sorted(gaps, key=lambda row: int(row["open_gap_width"]), reverse=True)
    p_delay_gap_rank = None
    for index, row in enumerate(sorted_gaps, start=1):
        if int(row["open_gap_width"]) == p_delay:
            p_delay_gap_rank = index
            break

    total_extension = int(support_choice["total_extension_required"])
    conservative_extra_after_feedback = max(0, total_extension - best_single_side_feedback)
    exact_left_extra = max(
        0, int(support_choice["left_extension_required"]) - left_feedback_horizon
    )
    exact_right_extra = max(
        0, int(support_choice["right_extension_required"]) - right_feedback_horizon
    )

    aggregate = {
        "bidirectional_hull_ledger": str(bidirectional_hull_path.relative_to(ROOT)),
        "formal_alignment_row_count": len(rows),
        "combined_crt_modulus": modulus,
        "support_interval": support,
        "support_width": support_width,
        "linear_hull_width_from_previous_audit": int(
            aggregate_in["alignment_hull_width"]
        ),
        "largest_circular_open_gap_width": int(largest_gap["open_gap_width"]),
        "largest_circular_gap_delta": int(largest_gap["cyclic_delta"]),
        "largest_gap_from_pair": str(largest_gap["from_pair"]),
        "largest_gap_to_pair": str(largest_gap["to_pair"]),
        "largest_gap_from_supported_actual": bool(
            largest_gap["from_supported_actual"]
        ),
        "largest_gap_to_supported_actual": bool(largest_gap["to_supported_actual"]),
        "minimal_circular_alignment_arc": [
            int(arc["arc_start_representative"]),
            int(arc["arc_end_representative"]),
        ],
        "minimal_circular_alignment_arc_width": int(arc["arc_width"]),
        "minimal_circular_arc_width_to_support_width_ratio": int(arc["arc_width"])
        / support_width,
        "minimal_circular_arc_width_to_modulus_ratio": int(arc["arc_width"])
        / modulus,
        "optimal_support_shift_periods": int(support_choice["support_shift_periods"]),
        "optimal_shifted_support_interval": support_choice[
            "shifted_support_interval"
        ],
        "optimal_left_extension_required": int(
            support_choice["left_extension_required"]
        ),
        "optimal_right_extension_required": int(
            support_choice["right_extension_required"]
        ),
        "optimal_total_extension_required": total_extension,
        "left_feedback_horizon": left_feedback_horizon,
        "right_feedback_horizon": right_feedback_horizon,
        "best_single_side_feedback_horizon": best_single_side_feedback,
        "exact_left_extra_after_feedback": exact_left_extra,
        "exact_right_extra_after_feedback": exact_right_extra,
        "conservative_extra_after_best_single_side_feedback": (
            conservative_extra_after_feedback
        ),
        "affine_p_delay": p_delay,
        "p_delay_open_gap_present": bool(p_delay_gaps),
        "p_delay_open_gap_is_largest_gap": int(largest_gap["open_gap_width"])
        == p_delay,
        "p_delay_gap_rank_by_width": p_delay_gap_rank,
        "p_delay_gap_pairs": [
            {
                "from_pair": row["from_pair"],
                "to_pair": row["to_pair"],
                "from_side": row["from_side"],
                "to_side": row["to_side"],
            }
            for row in p_delay_gaps
        ],
        "largest_gap_anchored_at_supported_actual_packet": bool(
            largest_gap["from_supported_actual"] or largest_gap["to_supported_actual"]
        ),
        "circular_aperture_refines_linear_hull": int(arc["arc_width"])
        < int(aggregate_in["alignment_hull_width"]),
        "one_sided_circular_absorption_closed_current_sweep": (
            conservative_extra_after_feedback > 0
        ),
        "global_circular_aperture_excluded": False,
        "row_column_unconditional_closed": False,
    }

    return {
        "certificate_type": (
            "prime_matrix_affine_twin_endpoint_release_circular_aperture_audit"
        ),
        "status": "current_sweep_circular_aperture_structured_global_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "aggregate": aggregate,
        "circular_gap_rows": gaps,
        "contract": {
            "linear_to_circular_refinement": (
                "The previous bidirectional hull is a current-period linear hull. "
                "This audit also computes the true circular aperture by deleting "
                "the largest empty arc in the q(q-2) period."
            ),
            "current_sweep_gate": [
                "compute the circular gap spectrum of all formal-pair CRT classes",
                "remove the largest open gap to obtain the minimal circular arc",
                "compare the optimal shifted support interval with that arc",
                "route the remaining one-sided excess to CircularAperture-PDEC/ColumnCRT",
            ],
            "closed_current_sweep": aggregate[
                "one_sided_circular_absorption_closed_current_sweep"
            ],
            "global_remaining": [
                "CircularAperture-PDEC exclusion",
                "ColumnCRT/PDEC for persistent aperture recurrence",
                "AffineTwinEpochPairMultiplicityBoundOrColumnCRTPDECExclusion",
            ],
        },
        "dependency_hashes": {
            str(bidirectional_hull_path.relative_to(ROOT)): sha256(
                bidirectional_hull_path
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
    lines = [
        "# Prime Matrix AffineTwin endpoint-release circular-aperture audit",
        "",
        "**状态：** `current_sweep_circular_aperture_structured_global_open`",
        "",
        "本审计把上一张线性壳层证书再精炼为圆周相位口径：在模 `q(q-2)` 的圆上删除最大的空弧，得到真正的最小 circular alignment arc。",
        "",
        "```text",
        f"formal_alignment_row_count={agg['formal_alignment_row_count']}",
        f"combined_crt_modulus={agg['combined_crt_modulus']}",
        f"support_width={agg['support_width']}",
        f"linear_hull_width_from_previous_audit={agg['linear_hull_width_from_previous_audit']}",
        f"largest_circular_open_gap_width={agg['largest_circular_open_gap_width']}",
        f"largest_gap_from_pair={agg['largest_gap_from_pair']}",
        f"largest_gap_to_pair={agg['largest_gap_to_pair']}",
        f"minimal_circular_alignment_arc={agg['minimal_circular_alignment_arc']}",
        f"minimal_circular_alignment_arc_width={agg['minimal_circular_alignment_arc_width']}",
        f"minimal_circular_arc_width_to_modulus_ratio={fmt_decimal(agg['minimal_circular_arc_width_to_modulus_ratio'])}",
        f"optimal_shifted_support_interval={agg['optimal_shifted_support_interval']}",
        f"optimal_total_extension_required={agg['optimal_total_extension_required']}",
        f"conservative_extra_after_best_single_side_feedback={agg['conservative_extra_after_best_single_side_feedback']}",
        f"p_delay_open_gap_present={fmt_bool(agg['p_delay_open_gap_present'])}",
        f"p_delay_open_gap_is_largest_gap={fmt_bool(agg['p_delay_open_gap_is_largest_gap'])}",
        f"p_delay_gap_rank_by_width={agg['p_delay_gap_rank_by_width']}",
        f"one_sided_circular_absorption_closed_current_sweep={fmt_bool(agg['one_sided_circular_absorption_closed_current_sweep'])}",
        "```",
        "",
        "## 1. 圆周 gap spectrum",
        "",
        "| from | to | from side | to side | open gap | delta |",
        "| --- | --- | --- | --- | ---: | ---: |",
    ]
    for row in sorted(
        result["circular_gap_rows"],
        key=lambda item: int(item["open_gap_width"]),
        reverse=True,
    ):
        lines.append(
            "| `{}` | `{}` | `{}` | `{}` | {} | {} |".format(
                row["from_pair"],
                row["to_pair"],
                row["from_side"],
                row["to_side"],
                row["open_gap_width"],
                row["cyclic_delta"],
            )
        )
    lines.extend(
        [
            "",
            "## 2. 圆弧修正",
            "",
            f"上一张证书的 `[2304,3122]` 是当前周期线性壳层，宽度 `{agg['linear_hull_width_from_previous_audit']}`。圆周上真正的最小壳层应删除最大空弧 `{agg['largest_gap_from_pair']} -> {agg['largest_gap_to_pair']}`，其 open gap 宽度为 `{agg['largest_circular_open_gap_width']}`，得到圆弧 `{agg['minimal_circular_alignment_arc']}`，宽度 `{agg['minimal_circular_alignment_arc_width']}`。",
            f"这仍是 support width `{agg['support_width']}` 的 `{fmt_decimal(agg['minimal_circular_arc_width_to_support_width_ratio'])}` 倍。即使把 support 平移到最优周期位置 `{agg['optimal_shifted_support_interval']}`，仍需总扩张 `{agg['optimal_total_extension_required']}`；扣除最有利单侧 feedback horizon 后仍缺 `{agg['conservative_extra_after_best_single_side_feedback']}`。",
            "",
            "## 3. p-delay 子缝",
            "",
            f"`p_delay={agg['affine_p_delay']}` 的空缝确实存在，但它不是最大圆周空弧；其宽度排名为 `{agg['p_delay_gap_rank_by_width']}`。因此最新刚性不是“近全周期最小圆弧”，而是更精确的：最大空弧锚定在 actual packet 附近，删除它后仍留下宽度 `{agg['minimal_circular_alignment_arc_width']}` 的大圆弧，远超当前支撑和反馈地平线。",
            "",
            "## 4. 结论边界",
            "",
            "- 本步修正并细化上一层线性壳层：圆周最小弧已物化。",
            "- 即使采用最优圆周切口，当前 formal-pair 系统仍不能由单侧 skew-growth 加 feedback horizon 吸收。",
            "- 本步不关闭全局行/列命题；剩余是排斥 `CircularAperture-PDEC`，或证明持久圆弧复现进入 `ColumnCRT/PDEC`、`SAE` 或 moving-family multiplicity 出口。",
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


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(
        description="生成 AffineTwin endpoint-release circular-aperture 审计证书。"
    )
    parser.add_argument(
        "--bidirectional-hull-ledger",
        type=Path,
        default=BIDIRECTIONAL_HULL_LEDGER,
    )
    return parser.parse_args()


def main() -> None:
    """入口。"""
    args = parse_args()
    result = build_result(args.bidirectional_hull_ledger)
    write_outputs(result)
    print(json.dumps(result["aggregate"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
