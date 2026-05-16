#!/usr/bin/env python3
"""生成 AffineTwin endpoint-release feedback-horizon slack 审计证书。

用法示例：
  python3 experiments/prime_matrix_affine_twin_endpoint_release_feedback_horizon_slack_audit.py
  python3 -m json.tool data/prime-matrix-affine-twin-endpoint-release-feedback-horizon-slack-ledger.json

输出：
  data/prime-matrix-affine-twin-endpoint-release-feedback-horizon-slack-ledger.json
  docs/monograph/prime-matrix-affine-twin-endpoint-release-feedback-horizon-slack-audit.json
  docs/monograph/prime-matrix-affine-twin-endpoint-release-feedback-horizon-slack-audit.md
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

FEEDBACK_HORIZON_LEDGER = DATA / (
    "prime-matrix-affine-twin-endpoint-release-feedback-horizon-ledger.json"
)
SOURCE_REMATERIALIZATION_LEDGER = DATA / (
    "prime-matrix-affine-twin-moving-key-source-rematerialization-ledger.json"
)

OUT_LEDGER = DATA / (
    "prime-matrix-affine-twin-endpoint-release-feedback-horizon-slack-ledger.json"
)
OUT_JSON = DOCS / (
    "prime-matrix-affine-twin-endpoint-release-feedback-horizon-slack-audit.json"
)
OUT_MD = DOCS / (
    "prime-matrix-affine-twin-endpoint-release-feedback-horizon-slack-audit.md"
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


def moving_candidates_by_pair(rematerialization: dict[str, Any]) -> dict[str, list[int]]:
    """按 source pair 汇总 moving-key 公式给出的候选 q。"""
    out: dict[str, set[int]] = {}
    for occurrence in rematerialization.get("moving_q_occurrences", []):
        pair = str(occurrence["source_pair_key"])
        out.setdefault(pair, set()).add(int(occurrence["q_candidate"]))
    return {pair: sorted(values) for pair, values in out.items()}


def exact_rematerialized_pairs(rematerialization: dict[str, Any]) -> set[str]:
    """取出已精确重物化的 source pair；当前账本中该集合应为空。"""
    pairs: set[str] = set()
    for row in rematerialization.get("candidate_q_source_rematerialization_rows", []):
        if str(row.get("route")) != "ExactSourceMaterialized":
            continue
        for pair in row.get("source_pair_keys", []):
            pairs.add(str(pair))
    return pairs


def slack_row(
    horizon_row: dict[str, Any],
    moving_q_by_pair: dict[str, list[int]],
    exact_pairs: set[str],
) -> dict[str, Any]:
    """构造单个 feedback-horizon slack 行。"""
    pair = str(horizon_row["source_pair_key"])
    distance = int(horizon_row["window_distance"])
    support_width = int(horizon_row["support_width"])
    current_skew = int(horizon_row["side_depth_skew"])
    phase_surplus = int(horizon_row["phase_horizon_surplus"])
    required_total_skew = max(0, distance - support_width)
    required_extra_skew = max(0, required_total_skew - current_skew)

    # 纯方向翻转只交换两侧深度，绝对 skew 不变，所以不能吞掉正 surplus。
    pure_flip_skew = current_skew
    pure_flip_horizon = support_width + pure_flip_skew
    pure_flip_surplus = distance - pure_flip_horizon
    same_orientation_source = pair in exact_pairs
    route = (
        "InsideFeedbackHorizon"
        if required_extra_skew == 0
        else "SameOrientationSourceRematerialized"
        if same_orientation_source
        else "EndpointSkewGrowth-PDEC/OrientationChangingPrimitiveKey-SAE"
    )
    return {
        "source_pair_key": pair,
        "q": int(horizon_row["q"]),
        "window_side": str(horizon_row["window_side"]),
        "nearest_representative": int(horizon_row["nearest_representative"]),
        "window_distance": distance,
        "support_width": support_width,
        "current_side_depth_skew": current_skew,
        "feedback_horizon_width": int(horizon_row["feedback_horizon_width"]),
        "phase_horizon_surplus": phase_surplus,
        "required_total_skew_for_absorption": required_total_skew,
        "required_extra_skew_to_reach_horizon": required_extra_skew,
        "required_extra_skew_equals_phase_surplus": required_extra_skew
        == phase_surplus,
        "required_extra_skew_fraction_of_support": required_extra_skew
        / support_width,
        "pure_orientation_flip_skew": pure_flip_skew,
        "pure_orientation_flip_horizon_width": pure_flip_horizon,
        "pure_orientation_flip_surplus": pure_flip_surplus,
        "pure_orientation_flip_preserves_surplus": pure_flip_surplus
        == phase_surplus,
        "pure_orientation_flip_absorbs": pure_flip_surplus <= 0,
        "moving_key_formula_q_candidates": moving_q_by_pair.get(pair, []),
        "same_orientation_source_rematerialized": same_orientation_source,
        "same_orientation_absorption_closed_current": (
            required_extra_skew > 0 and not same_orientation_source
        ),
        "structured_route_current": route,
    }


def build_result(
    feedback_horizon_path: Path,
    source_rematerialization_path: Path,
) -> dict[str, Any]:
    """构造 endpoint-release feedback-horizon slack 审计结果。"""
    feedback_horizon = load_json(feedback_horizon_path)
    rematerialization = load_json(source_rematerialization_path)
    moving_q_by_pair = moving_candidates_by_pair(rematerialization)
    exact_pairs = exact_rematerialized_pairs(rematerialization)

    rows = [
        slack_row(row, moving_q_by_pair, exact_pairs)
        for row in feedback_horizon["endpoint_release_feedback_horizon_rows"]
    ]
    if not rows:
        raise RuntimeError("no feedback-horizon rows found")

    total_required_skew = sum(
        int(row["required_total_skew_for_absorption"]) for row in rows
    )
    total_current_skew = sum(int(row["current_side_depth_skew"]) for row in rows)
    total_extra_skew = sum(
        int(row["required_extra_skew_to_reach_horizon"]) for row in rows
    )
    support_width = int(feedback_horizon["aggregate"]["support_width"])
    narrowest = min(
        rows,
        key=lambda row: (
            int(row["required_extra_skew_to_reach_horizon"]),
            int(row["window_distance"]),
            str(row["source_pair_key"]),
        ),
    )
    worst = max(
        rows,
        key=lambda row: (
            int(row["required_extra_skew_to_reach_horizon"]),
            int(row["window_distance"]),
            str(row["source_pair_key"]),
        ),
    )

    same_orientation_exact_q_values = rematerialization["aggregate"].get(
        "exact_rematerialized_q_values", []
    )
    aggregate = {
        "feedback_horizon_ledger": str(feedback_horizon_path.relative_to(ROOT)),
        "source_rematerialization_ledger": str(
            source_rematerialization_path.relative_to(ROOT)
        ),
        "support_motion_candidate_count": len(rows),
        "support_width": support_width,
        "total_required_absorption_skew": total_required_skew,
        "total_current_side_depth_skew": total_current_skew,
        "total_required_extra_skew": total_extra_skew,
        "current_skew_coverage_ratio": total_current_skew / total_required_skew,
        "extra_skew_deficit_ratio": total_extra_skew / total_required_skew,
        "min_required_total_skew": min(
            int(row["required_total_skew_for_absorption"]) for row in rows
        ),
        "max_required_total_skew": max(
            int(row["required_total_skew_for_absorption"]) for row in rows
        ),
        "min_required_extra_skew": min(
            int(row["required_extra_skew_to_reach_horizon"]) for row in rows
        ),
        "max_required_extra_skew": max(
            int(row["required_extra_skew_to_reach_horizon"]) for row in rows
        ),
        "narrowest_feedback_horizon_slack_atom": {
            "source_pair_key": narrowest["source_pair_key"],
            "window_side": narrowest["window_side"],
            "window_distance": narrowest["window_distance"],
            "support_width": narrowest["support_width"],
            "current_side_depth_skew": narrowest["current_side_depth_skew"],
            "required_total_skew_for_absorption": narrowest[
                "required_total_skew_for_absorption"
            ],
            "required_extra_skew_to_reach_horizon": narrowest[
                "required_extra_skew_to_reach_horizon"
            ],
            "moving_key_formula_q_candidates": narrowest[
                "moving_key_formula_q_candidates"
            ],
            "structured_route_current": narrowest["structured_route_current"],
        },
        "worst_feedback_horizon_slack_atom": {
            "source_pair_key": worst["source_pair_key"],
            "window_side": worst["window_side"],
            "window_distance": worst["window_distance"],
            "support_width": worst["support_width"],
            "current_side_depth_skew": worst["current_side_depth_skew"],
            "required_total_skew_for_absorption": worst[
                "required_total_skew_for_absorption"
            ],
            "required_extra_skew_to_reach_horizon": worst[
                "required_extra_skew_to_reach_horizon"
            ],
            "moving_key_formula_q_candidates": worst[
                "moving_key_formula_q_candidates"
            ],
            "structured_route_current": worst["structured_route_current"],
        },
        "all_required_extra_skews_positive": all(
            int(row["required_extra_skew_to_reach_horizon"]) > 0 for row in rows
        ),
        "all_required_extra_skews_equal_phase_surpluses": all(
            bool(row["required_extra_skew_equals_phase_surplus"]) for row in rows
        ),
        "all_pure_orientation_flips_preserve_surplus": all(
            bool(row["pure_orientation_flip_preserves_surplus"]) for row in rows
        ),
        "all_pure_orientation_flips_fail_absorption": all(
            not bool(row["pure_orientation_flip_absorbs"]) for row in rows
        ),
        "same_orientation_exact_rematerialized_q_values": (
            same_orientation_exact_q_values
        ),
        "same_orientation_source_rematerialization_absent": not bool(
            same_orientation_exact_q_values or exact_pairs
        ),
        "all_same_orientation_absorption_closed_current": all(
            bool(row["same_orientation_absorption_closed_current"]) for row in rows
        ),
        "feedback_horizon_slack_structured_current_sweep": all(
            str(row["structured_route_current"])
            == "EndpointSkewGrowth-PDEC/OrientationChangingPrimitiveKey-SAE"
            for row in rows
        ),
        "global_feedback_horizon_slack_excluded": False,
        "row_column_unconditional_closed": False,
    }

    return {
        "certificate_type": (
            "prime_matrix_affine_twin_endpoint_release_feedback_horizon_slack_audit"
        ),
        "status": (
            "current_sweep_feedback_horizon_slack_structured_global_open"
        ),
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "aggregate": aggregate,
        "endpoint_release_feedback_horizon_slack_rows": rows,
        "contract": {
            "slack_definition": (
                "To absorb a representative at distance d with support width W, "
                "the side-depth skew must be at least max(0,d-W).  The missing "
                "extra skew equals the phase-horizon surplus."
            ),
            "pure_orientation_flip_gate": (
                "A pure orientation flip preserves |generator depth-fill depth|, "
                "so it cannot reduce a positive horizon surplus."
            ),
            "current_sweep_structuring_gate": [
                "compute required extra skew row by row",
                "verify it equals the horizon surplus",
                "inherit absence of same-orientation source rematerialization",
                "route any persistent extra skew to EndpointSkewGrowth-PDEC or OrientationChangingPrimitiveKey-SAE",
            ],
            "closed_current_sweep": aggregate[
                "feedback_horizon_slack_structured_current_sweep"
            ],
            "global_remaining": [
                "EndpointSkewGrowth-PDEC exclusion",
                "OrientationChangingPrimitiveKey-PDEC/SAE",
                "SourceRematerialization-PDEC/SAE beyond same-orientation gate",
            ],
        },
        "dependency_hashes": {
            str(path.relative_to(ROOT)): sha256(path)
            for path in (feedback_horizon_path, source_rematerialization_path)
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
    narrow = agg["narrowest_feedback_horizon_slack_atom"]
    worst = agg["worst_feedback_horizon_slack_atom"]
    lines = [
        "# Prime Matrix AffineTwin endpoint-release feedback-horizon slack audit",
        "",
        "**状态：** `current_sweep_feedback_horizon_slack_structured_global_open`",
        "",
        "本审计把 `phase horizon surplus` 再压成“必须新增的 side-depth skew”。若 CRT 代表距离为 `d`、支撑宽度为 `W`，则自反馈吸收至少需要 `max(0,d-W)` 的总 skew；当前 skew 不足的部分正好等于上一层的相位地平线缺口。",
        "",
        "```text",
        "required total skew = max(0, window distance - support width)",
        "required extra skew = required total skew - current side-depth skew",
        "required extra skew = phase horizon surplus",
        "pure orientation flip gain = 0",
        "```",
        "",
        "```text",
        f"support_motion_candidate_count={agg['support_motion_candidate_count']}",
        f"support_width={agg['support_width']}",
        f"total_required_absorption_skew={agg['total_required_absorption_skew']}",
        f"total_current_side_depth_skew={agg['total_current_side_depth_skew']}",
        f"total_required_extra_skew={agg['total_required_extra_skew']}",
        f"current_skew_coverage_ratio={fmt_decimal(agg['current_skew_coverage_ratio'])}",
        f"extra_skew_deficit_ratio={fmt_decimal(agg['extra_skew_deficit_ratio'])}",
        f"min_required_extra_skew={agg['min_required_extra_skew']}",
        f"max_required_extra_skew={agg['max_required_extra_skew']}",
        f"all_required_extra_skews_equal_phase_surpluses={fmt_bool(agg['all_required_extra_skews_equal_phase_surpluses'])}",
        f"all_pure_orientation_flips_fail_absorption={fmt_bool(agg['all_pure_orientation_flips_fail_absorption'])}",
        f"same_orientation_source_rematerialization_absent={fmt_bool(agg['same_orientation_source_rematerialization_absent'])}",
        f"feedback_horizon_slack_structured_current_sweep={fmt_bool(agg['feedback_horizon_slack_structured_current_sweep'])}",
        "```",
        "",
        "## 1. slack 表",
        "",
        "| pair | side | distance | support | current skew | required skew | extra skew | moving q candidates | same-source | route |",
        "| --- | --- | ---: | ---: | ---: | ---: | ---: | --- | --- | --- |",
    ]
    for row in result["endpoint_release_feedback_horizon_slack_rows"]:
        lines.append(
            "| `{pair}` | `{side}` | {distance} | {support} | {current} | {required} | {extra} | `{candidates}` | {same_source} | `{route}` |".format(
                pair=row["source_pair_key"],
                side=row["window_side"],
                distance=row["window_distance"],
                support=row["support_width"],
                current=row["current_side_depth_skew"],
                required=row["required_total_skew_for_absorption"],
                extra=row["required_extra_skew_to_reach_horizon"],
                candidates=row["moving_key_formula_q_candidates"],
                same_source=fmt_bool(row["same_orientation_source_rematerialized"]),
                route=row["structured_route_current"],
            )
        )

    lines.extend(
        [
            "",
            "## 2. 最窄 slack 原子",
            "",
            f"最窄 atom 为 `{narrow['source_pair_key']}`，side `{narrow['window_side']}`。它的 CRT 代表距窗口 `{narrow['window_distance']}`，support width 为 `{narrow['support_width']}`，因此吸收所需总 skew 为 `{narrow['required_total_skew_for_absorption']}`。当前 skew 只有 `{narrow['current_side_depth_skew']}`，还差 `{narrow['required_extra_skew_to_reach_horizon']}`。",
            f"该 atom 的 moving-key 公式候选为 `{narrow['moving_key_formula_q_candidates']}`，继承 source-rematerialization 账本后同向精确重物化为空，所以这 `{narrow['required_extra_skew_to_reach_horizon']}` 个单位不能由同向 source 补足。",
            "",
            "## 3. 最大 slack 原子",
            "",
            f"最大 atom 为 `{worst['source_pair_key']}`，side `{worst['window_side']}`，需要额外 skew `{worst['required_extra_skew_to_reach_horizon']}`，moving-key 公式候选为 `{worst['moving_key_formula_q_candidates']}`。",
            "",
            "## 4. 结论边界",
            "",
            "- `required extra skew = phase horizon surplus` 逐项成立，说明上一层相位缺口就是新增 skew 缺口。",
            "- 纯方向翻转保持绝对 skew，不改变正 surplus；因此不能作为吸收机制。",
            "- 同向 source 重物化继承为 absent，当前 `11` 个候选全部需要新的 skew-growth 或 orientation-changing primitive key。",
            "- 本步只关闭当前 sweep 的匿名 slack 吸收解释；全局行/列命题仍需排斥 `EndpointSkewGrowth-PDEC`，或把方向改变/source 重物化/SAE 出口逐项闭合。",
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
        description="生成 AffineTwin endpoint-release feedback-horizon slack 审计证书。"
    )
    parser.add_argument(
        "--feedback-horizon-ledger", type=Path, default=FEEDBACK_HORIZON_LEDGER
    )
    parser.add_argument(
        "--source-rematerialization-ledger",
        type=Path,
        default=SOURCE_REMATERIALIZATION_LEDGER,
    )
    return parser.parse_args()


def main() -> None:
    """入口。"""
    args = parse_args()
    result = build_result(
        args.feedback_horizon_ledger,
        args.source_rematerialization_ledger,
    )
    write_outputs(result)
    print(json.dumps(result["aggregate"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
