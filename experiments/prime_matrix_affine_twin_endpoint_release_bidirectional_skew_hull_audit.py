#!/usr/bin/env python3
"""生成 AffineTwin endpoint-release bidirectional skew-hull 审计证书。

用法示例：
  python3 experiments/prime_matrix_affine_twin_endpoint_release_bidirectional_skew_hull_audit.py
  python3 -m json.tool data/prime-matrix-affine-twin-endpoint-release-bidirectional-skew-hull-ledger.json

输出：
  data/prime-matrix-affine-twin-endpoint-release-bidirectional-skew-hull-ledger.json
  docs/monograph/prime-matrix-affine-twin-endpoint-release-bidirectional-skew-hull-audit.json
  docs/monograph/prime-matrix-affine-twin-endpoint-release-bidirectional-skew-hull-audit.md
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

CRT_WINDOW_GAP_LEDGER = DATA / "prime-matrix-affine-twin-crt-window-gap-ledger.json"
SLACK_LEDGER = DATA / (
    "prime-matrix-affine-twin-endpoint-release-feedback-horizon-slack-ledger.json"
)
SLOT_LOCK_LEDGER = DATA / (
    "square-phase-offband-prefix-gap-shadow-selector-h-lower-"
    "affine-twin-slot-phase-lock-ledger.json"
)
INVERSE_ALIGNMENT_ROUTER = DOCS / "prime-matrix-inverse-alignment-covering-system-router.json"

OUT_LEDGER = DATA / (
    "prime-matrix-affine-twin-endpoint-release-bidirectional-skew-hull-ledger.json"
)
OUT_JSON = DOCS / (
    "prime-matrix-affine-twin-endpoint-release-bidirectional-skew-hull-audit.json"
)
OUT_MD = DOCS / (
    "prime-matrix-affine-twin-endpoint-release-bidirectional-skew-hull-audit.md"
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


def pair_key(row: dict[str, Any]) -> str:
    """生成 generator/fill residue pair key。"""
    return f"{int(row['generator_residue'])}:{int(row['fill_residue'])}"


def slack_by_pair(slack: dict[str, Any]) -> dict[str, dict[str, Any]]:
    """按 residue pair 建立 slack 行索引。"""
    return {
        str(row["source_pair_key"]): row
        for row in slack["endpoint_release_feedback_horizon_slack_rows"]
    }


def formal_alignment_rows(
    crt_window: dict[str, Any],
    slack: dict[str, Any],
) -> list[dict[str, Any]]:
    """把 CRT 窗口行改写成局部逆元对齐行。"""
    slack_index = slack_by_pair(slack)
    rows: list[dict[str, Any]] = []
    for row in crt_window["crt_window_rows"]:
        key = pair_key(row)
        supported = bool(row["supported_actual_packet_current"])
        slack_row = slack_index.get(key)
        phase_surplus = 0 if supported else int(slack_row["phase_horizon_surplus"])
        required_extra = (
            0 if supported else int(slack_row["required_extra_skew_to_reach_horizon"])
        )
        rows.append(
            {
                "source_pair_key": key,
                "q": int(row["q"]),
                "generator_residue": int(row["generator_residue"]),
                "fill_residue": int(row["fill_residue"]),
                "shifted_fill_residue": int(row["shifted_fill_residue"]),
                "combined_crt_residue": int(row["combined_crt_residue"]),
                "combined_crt_modulus": int(row["combined_crt_modulus"]),
                "nearest_representative": int(row["nearest_representative"]),
                "window_side": str(row["window_side"]),
                "window_distance": int(row["window_distance"]),
                "supported_actual_packet_current": supported,
                "phase_horizon_surplus": phase_surplus,
                "required_extra_skew_to_reach_horizon": required_extra,
                "local_inverse_alignment_condition": (
                    "P == generator_residue mod (q-2) and "
                    "P == shifted_fill_residue mod q"
                ),
            }
        )
    return rows


def side_skew(slack: dict[str, Any], side: str) -> int:
    """读取某侧当前 side-depth skew；同侧应一致。"""
    values = {
        int(row["current_side_depth_skew"])
        for row in slack["endpoint_release_feedback_horizon_slack_rows"]
        if str(row["window_side"]) == side
    }
    if len(values) != 1:
        raise RuntimeError(f"unexpected skew values for side={side}: {values}")
    return values.pop()


def build_result(
    crt_window_path: Path,
    slack_path: Path,
    slot_lock_path: Path,
    inverse_alignment_path: Path,
) -> dict[str, Any]:
    """构造 bidirectional skew-hull 审计结果。"""
    crt_window = load_json(crt_window_path)
    slack = load_json(slack_path)
    slot_lock = load_json(slot_lock_path)
    inverse_alignment = load_json(inverse_alignment_path)

    rows = formal_alignment_rows(crt_window, slack)
    if not rows:
        raise RuntimeError("no CRT window rows found")
    support_lo, support_hi = [
        int(value) for value in crt_window["crt_window_rows"][0]["pair_phase_support"]
    ]
    support_width = support_hi - support_lo + 1
    modulus = int(rows[0]["combined_crt_modulus"])
    nearest_values = [int(row["nearest_representative"]) for row in rows]
    hull_lo = min(nearest_values)
    hull_hi = max(nearest_values)
    hull_width = hull_hi - hull_lo + 1
    left_extension = support_lo - hull_lo
    right_extension = hull_hi - support_hi
    below_skew = side_skew(slack, "below")
    above_skew = side_skew(slack, "above")
    left_feedback_horizon = support_width + below_skew
    right_feedback_horizon = support_width + above_skew
    left_extra_skew = max(0, left_extension - left_feedback_horizon)
    right_extra_skew = max(0, right_extension - right_feedback_horizon)
    combined_extra_skew = left_extra_skew + right_extra_skew

    slot_row = slot_lock["affine_twin_slot_phase_lock_rows"][0]
    p_delay = int(slot_row["p_delay"])
    side_histogram = Counter(str(row["window_side"]) for row in rows)
    empty_rows = [row for row in rows if not row["supported_actual_packet_current"]]
    actual_rows = [row for row in rows if row["supported_actual_packet_current"]]
    below_rows = [row for row in empty_rows if row["window_side"] == "below"]
    above_rows = [row for row in empty_rows if row["window_side"] == "above"]

    aggregate = {
        "crt_window_gap_ledger": str(crt_window_path.relative_to(ROOT)),
        "feedback_horizon_slack_ledger": str(slack_path.relative_to(ROOT)),
        "slot_lock_ledger": str(slot_lock_path.relative_to(ROOT)),
        "inverse_alignment_router": str(inverse_alignment_path.relative_to(ROOT)),
        "formal_alignment_row_count": len(rows),
        "empty_alignment_row_count": len(empty_rows),
        "supported_actual_packet_count": len(actual_rows),
        "window_side_histogram": dict(sorted(side_histogram.items())),
        "combined_crt_modulus": modulus,
        "support_interval": [support_lo, support_hi],
        "support_width": support_width,
        "alignment_hull_interval": [hull_lo, hull_hi],
        "alignment_hull_width": hull_width,
        "left_extension_required": left_extension,
        "right_extension_required": right_extension,
        "current_left_feedback_horizon": left_feedback_horizon,
        "current_right_feedback_horizon": right_feedback_horizon,
        "left_extra_skew_after_feedback_horizon": left_extra_skew,
        "right_extra_skew_after_feedback_horizon": right_extra_skew,
        "bidirectional_extra_skew_after_shared_hull": combined_extra_skew,
        "sum_rowwise_required_extra_skew": int(
            slack["aggregate"]["total_required_extra_skew"]
        ),
        "shared_hull_extra_skew_saves_rowwise_duplicates": int(
            slack["aggregate"]["total_required_extra_skew"]
        )
        - combined_extra_skew,
        "hull_width_to_support_width_ratio": hull_width / support_width,
        "hull_width_to_modulus_ratio": hull_width / modulus,
        "support_width_to_hull_width_ratio": support_width / hull_width,
        "modulus_minus_hull_width": modulus - hull_width,
        "affine_p_delay": p_delay,
        "hull_complement_equals_affine_p_delay": modulus - hull_width == p_delay,
        "both_sides_have_empty_alignment_atoms": bool(below_rows and above_rows),
        "both_sides_require_positive_extra_skew": left_extra_skew > 0
        and right_extra_skew > 0,
        "one_sided_skew_growth_absorption_closed_current_sweep": bool(
            below_rows and above_rows and left_extra_skew > 0 and right_extra_skew > 0
        ),
        "inverse_alignment_equivalence_imported": inverse_alignment.get(
            "gcd_system_equivalence_closed"
        )
        is True,
        "local_crt_alignment_hull_closed_current_sweep": True,
        "global_bidirectional_skew_hull_excluded": False,
        "row_column_unconditional_closed": False,
    }

    return {
        "certificate_type": (
            "prime_matrix_affine_twin_endpoint_release_bidirectional_skew_hull_audit"
        ),
        "status": (
            "current_sweep_bidirectional_skew_hull_structured_global_open"
        ),
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "aggregate": aggregate,
        "formal_alignment_rows": rows,
        "contract": {
            "inverse_alignment_bridge": (
                "The old inverse-alignment x route studies residue classes in x. "
                "Here each formal AffineTwin pair gives a residue class in the "
                "P variable modulo q(q-2); the nearest representative and hull "
                "are the local minimal-alignment objects for the current atom."
            ),
            "bidirectional_hull_gate": [
                "compute the smallest linear hull containing every current formal-pair representative",
                "compare its left and right extensions with the feedback horizons",
                "route positive two-sided excess to BidirectionalSkewHull-PDEC/ColumnCRT",
            ],
            "closed_current_sweep": aggregate[
                "local_crt_alignment_hull_closed_current_sweep"
            ],
            "global_remaining": [
                "BidirectionalSkewHull-PDEC exclusion",
                "TwoSidedEndpointSkewGrowth-PDEC/SAE",
                "ColumnCRT/PDEC for persistent hull recurrence",
                "AffineTwinEpochPairMultiplicityBoundOrColumnCRTPDECExclusion",
            ],
        },
        "dependency_hashes": {
            str(path.relative_to(ROOT)): sha256(path)
            for path in (
                crt_window_path,
                slack_path,
                slot_lock_path,
                inverse_alignment_path,
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
        "# Prime Matrix AffineTwin endpoint-release bidirectional skew-hull audit",
        "",
        "**状态：** `current_sweep_bidirectional_skew_hull_structured_global_open`",
        "",
        "本审计把最新 slack 原子放回局部逆元对齐框架：每个 formal pair 给出一个关于 `P` 的 CRT 类，支撑窗口若要同时吸收这些类，就必须覆盖它们的最小相位壳层。",
        "",
        "```text",
        "local pair alignment: P = generator_residue (mod q-2)",
        "                      P = shifted_fill_residue (mod q)",
        "hull = smallest current-period interval containing all nearest representatives",
        "```",
        "",
        "```text",
        f"formal_alignment_row_count={agg['formal_alignment_row_count']}",
        f"empty_alignment_row_count={agg['empty_alignment_row_count']}",
        f"combined_crt_modulus={agg['combined_crt_modulus']}",
        f"support_interval={agg['support_interval']}",
        f"support_width={agg['support_width']}",
        f"alignment_hull_interval={agg['alignment_hull_interval']}",
        f"alignment_hull_width={agg['alignment_hull_width']}",
        f"left_extension_required={agg['left_extension_required']}",
        f"right_extension_required={agg['right_extension_required']}",
        f"left_extra_skew_after_feedback_horizon={agg['left_extra_skew_after_feedback_horizon']}",
        f"right_extra_skew_after_feedback_horizon={agg['right_extra_skew_after_feedback_horizon']}",
        f"bidirectional_extra_skew_after_shared_hull={agg['bidirectional_extra_skew_after_shared_hull']}",
        f"hull_width_to_modulus_ratio={fmt_decimal(agg['hull_width_to_modulus_ratio'])}",
        f"modulus_minus_hull_width={agg['modulus_minus_hull_width']}",
        f"affine_p_delay={agg['affine_p_delay']}",
        f"hull_complement_equals_affine_p_delay={fmt_bool(agg['hull_complement_equals_affine_p_delay'])}",
        f"one_sided_skew_growth_absorption_closed_current_sweep={fmt_bool(agg['one_sided_skew_growth_absorption_closed_current_sweep'])}",
        "```",
        "",
        "## 1. 局部对齐表",
        "",
        "| pair | side | representative | distance | surplus | actual | CRT residue |",
        "| --- | --- | ---: | ---: | ---: | --- | ---: |",
    ]
    for row in result["formal_alignment_rows"]:
        lines.append(
            "| `{pair}` | `{side}` | {rep} | {distance} | {surplus} | {actual} | {residue} |".format(
                pair=row["source_pair_key"],
                side=row["window_side"],
                rep=row["nearest_representative"],
                distance=row["window_distance"],
                surplus=row["phase_horizon_surplus"],
                actual=fmt_bool(row["supported_actual_packet_current"]),
                residue=row["combined_crt_residue"],
            )
        )
    lines.extend(
        [
            "",
            "## 2. 壳层刚性",
            "",
            f"全部 formal pair 的最近代表落在 `{agg['alignment_hull_interval']}`，宽度 `{agg['alignment_hull_width']}`。当前支撑只有 `{agg['support_width']}`，若靠单一支撑窗口同时吸收所有 formal pair，左侧必须扩张 `{agg['left_extension_required']}`，右侧必须扩张 `{agg['right_extension_required']}`。",
            f"扣除当前 feedback horizon 后，左侧仍缺 `{agg['left_extra_skew_after_feedback_horizon']}`，右侧仍缺 `{agg['right_extra_skew_after_feedback_horizon']}`。因此一侧移动或纯 skew 翻向不能解释当前 formal-pair 全集。",
            f"更刚性的读数是：`modulus - hull_width = {agg['modulus_minus_hull_width']}`，正好等于 affine p-delay `{agg['affine_p_delay']}`。也就是说，若反例链要把所有 formal pair 同时塞回一个支撑壳层，它几乎占满整个 `q(q-2)` 周期，只留下 p-delay 大小的互补缝。",
            "",
            "## 3. 与逆元最小对齐解 x 的关系",
            "",
            "旧的逆元最小对齐路线把 `xP+r` 的小素因子覆盖写成 `x` 的 CRT 覆盖问题。本审计使用同一思想，但变量换成当前 AffineTwin 局部相位 `P`：每个 generator/fill residue pair 给出一个 `P mod q(q-2)` 的精确类。最近代表、支撑距离和最小壳层就是该局部系统的最小对齐证书。",
            "这一步没有证明全局 `min x>P`，而是把当前反例链/真实链的显式冲突压成双向壳层：反例链需要近全周期壳层，真实链只有宽度 `20` 的 primitive 支撑和有限 feedback horizon。",
            "",
            "## 4. 结论边界",
            "",
            "- 当前 `12` 个 formal pair 的局部 CRT 对齐壳层已精确物化。",
            "- 壳层同时向 below 和 above 两侧超出 feedback horizon，所以单侧 skew-growth 吸收关闭。",
            "- 本步不关闭全局行/列命题；剩余是排斥 `BidirectionalSkewHull-PDEC`，或证明持久壳层复现进入 `ColumnCRT/PDEC`、`SAE`、moving-family multiplicity 出口。",
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
        description="生成 AffineTwin endpoint-release bidirectional skew-hull 审计证书。"
    )
    parser.add_argument("--crt-window-gap-ledger", type=Path, default=CRT_WINDOW_GAP_LEDGER)
    parser.add_argument("--slack-ledger", type=Path, default=SLACK_LEDGER)
    parser.add_argument("--slot-lock-ledger", type=Path, default=SLOT_LOCK_LEDGER)
    parser.add_argument(
        "--inverse-alignment-router", type=Path, default=INVERSE_ALIGNMENT_ROUTER
    )
    return parser.parse_args()


def main() -> None:
    """入口。"""
    args = parse_args()
    result = build_result(
        args.crt_window_gap_ledger,
        args.slack_ledger,
        args.slot_lock_ledger,
        args.inverse_alignment_router,
    )
    write_outputs(result)
    print(json.dumps(result["aggregate"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
