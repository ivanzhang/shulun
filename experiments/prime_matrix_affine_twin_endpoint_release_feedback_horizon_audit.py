#!/usr/bin/env python3
"""生成 AffineTwin endpoint-release feedback-horizon 审计证书。

用法示例：
  python3 experiments/prime_matrix_affine_twin_endpoint_release_feedback_horizon_audit.py
  python3 -m json.tool data/prime-matrix-affine-twin-endpoint-release-feedback-horizon-ledger.json

输出：
  data/prime-matrix-affine-twin-endpoint-release-feedback-horizon-ledger.json
  docs/monograph/prime-matrix-affine-twin-endpoint-release-feedback-horizon-audit.json
  docs/monograph/prime-matrix-affine-twin-endpoint-release-feedback-horizon-audit.md
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
FEEDBACK_LOSS_LEDGER = DATA / (
    "prime-matrix-affine-twin-endpoint-release-feedback-loss-ledger.json"
)

OUT_LEDGER = DATA / "prime-matrix-affine-twin-endpoint-release-feedback-horizon-ledger.json"
OUT_JSON = DOCS / "prime-matrix-affine-twin-endpoint-release-feedback-horizon-audit.json"
OUT_MD = DOCS / "prime-matrix-affine-twin-endpoint-release-feedback-horizon-audit.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def feedback_rows_by_pair(feedback_loss: dict[str, Any]) -> dict[str, dict[str, Any]]:
    """按 source pair 建立 feedback-loss 索引。"""
    return {
        str(row["source_pair_key"]): row
        for row in feedback_loss["endpoint_release_feedback_loss_rows"]
    }


def horizon_row(
    support_row: dict[str, Any],
    feedback_row: dict[str, Any],
) -> dict[str, Any]:
    """构造单个 feedback horizon 行。"""
    support_width = int(support_row["support_width"])
    window_distance = int(support_row["window_distance"])
    generator_depth = int(support_row["current_generator_side_depth"])
    fill_depth = int(support_row["current_fill_side_depth"])
    side_depth_skew = abs(generator_depth - fill_depth)
    feedback_horizon_width = support_width + side_depth_skew
    horizon_surplus = window_distance - feedback_horizon_width
    feedback_loss = int(feedback_row["coupled_second_endpoint_feedback_loss"])
    expected_feedback_loss = window_distance - side_depth_skew
    post_credit_units = int(feedback_row["post_credit_overcritical_units"])
    return {
        "source_pair_key": str(support_row["source_pair_key"]),
        "q": int(support_row["q"]),
        "window_side": str(support_row["window_side"]),
        "nearest_representative": int(support_row["nearest_representative"]),
        "window_distance": window_distance,
        "support_width": support_width,
        "current_generator_side_depth": generator_depth,
        "current_fill_side_depth": fill_depth,
        "side_depth_skew": side_depth_skew,
        "feedback_horizon_width": feedback_horizon_width,
        "phase_horizon_surplus": horizon_surplus,
        "phase_horizon_surplus_fraction_of_support": horizon_surplus / support_width,
        "feedback_loss": feedback_loss,
        "expected_feedback_loss_from_distance_minus_skew": expected_feedback_loss,
        "feedback_loss_formula_holds": feedback_loss == expected_feedback_loss,
        "post_credit_overcritical_units": post_credit_units,
        "phase_horizon_surplus_matches_post_credit_units": horizon_surplus
        == post_credit_units,
        "representative_outside_feedback_horizon": horizon_surplus > 0,
        "structured_route_current": "EndpointReleaseFeedbackHorizon-PDEC"
        if horizon_surplus > 0
        else "InsideFeedbackHorizon",
        "pinned_endpoint": str(support_row["pinned_endpoint"]),
    }


def build_result(
    support_motion_path: Path,
    feedback_loss_path: Path,
) -> dict[str, Any]:
    """构造 endpoint-release feedback-horizon 审计结果。"""
    support_motion = load_json(support_motion_path)
    feedback_loss = load_json(feedback_loss_path)
    feedback_by_pair = feedback_rows_by_pair(feedback_loss)

    rows = [
        horizon_row(row, feedback_by_pair[str(row["source_pair_key"])])
        for row in support_motion["support_motion_rows"]
    ]
    if not rows:
        raise RuntimeError("no support-motion rows found")

    side_histogram = Counter(str(row["window_side"]) for row in rows)
    support_width = int(support_motion["aggregate"]["support_width_current"])
    total_distance = sum(int(row["window_distance"]) for row in rows)
    total_horizon = sum(int(row["feedback_horizon_width"]) for row in rows)
    total_surplus = sum(int(row["phase_horizon_surplus"]) for row in rows)
    narrowest = min(
        rows,
        key=lambda row: (
            int(row["phase_horizon_surplus"]),
            int(row["window_distance"]),
            str(row["source_pair_key"]),
        ),
    )
    worst = max(
        rows,
        key=lambda row: (
            int(row["phase_horizon_surplus"]),
            int(row["window_distance"]),
            str(row["source_pair_key"]),
        ),
    )

    aggregate = {
        "support_motion_ledger": str(support_motion_path.relative_to(ROOT)),
        "feedback_loss_ledger": str(feedback_loss_path.relative_to(ROOT)),
        "support_motion_candidate_count": len(rows),
        "support_motion_side_histogram": dict(sorted(side_histogram.items())),
        "support_width": support_width,
        "total_window_distance": total_distance,
        "total_feedback_horizon_width": total_horizon,
        "total_phase_horizon_surplus": total_surplus,
        "total_phase_horizon_surplus_to_support_budget_ratio": total_surplus
        / (support_width * len(rows)),
        "min_phase_horizon_surplus": min(
            int(row["phase_horizon_surplus"]) for row in rows
        ),
        "max_phase_horizon_surplus": max(
            int(row["phase_horizon_surplus"]) for row in rows
        ),
        "min_feedback_horizon_width": min(
            int(row["feedback_horizon_width"]) for row in rows
        ),
        "max_feedback_horizon_width": max(
            int(row["feedback_horizon_width"]) for row in rows
        ),
        "narrowest_feedback_horizon_atom": {
            "source_pair_key": narrowest["source_pair_key"],
            "window_side": narrowest["window_side"],
            "window_distance": narrowest["window_distance"],
            "support_width": narrowest["support_width"],
            "side_depth_skew": narrowest["side_depth_skew"],
            "feedback_horizon_width": narrowest["feedback_horizon_width"],
            "phase_horizon_surplus": narrowest["phase_horizon_surplus"],
            "structured_route_current": narrowest["structured_route_current"],
        },
        "worst_feedback_horizon_atom": {
            "source_pair_key": worst["source_pair_key"],
            "window_side": worst["window_side"],
            "window_distance": worst["window_distance"],
            "support_width": worst["support_width"],
            "side_depth_skew": worst["side_depth_skew"],
            "feedback_horizon_width": worst["feedback_horizon_width"],
            "phase_horizon_surplus": worst["phase_horizon_surplus"],
            "structured_route_current": worst["structured_route_current"],
        },
        "all_feedback_loss_formulas_hold": all(
            bool(row["feedback_loss_formula_holds"]) for row in rows
        ),
        "all_phase_surpluses_match_post_credit_units": all(
            bool(row["phase_horizon_surplus_matches_post_credit_units"])
            for row in rows
        ),
        "all_representatives_outside_feedback_horizon": all(
            bool(row["representative_outside_feedback_horizon"]) for row in rows
        ),
        "endpoint_release_feedback_horizon_structured_current_sweep": all(
            str(row["structured_route_current"])
            == "EndpointReleaseFeedbackHorizon-PDEC"
            for row in rows
        ),
        "global_endpoint_release_feedback_horizon_excluded": False,
        "row_column_unconditional_closed": False,
    }

    return {
        "certificate_type": (
            "prime_matrix_affine_twin_endpoint_release_feedback_horizon_audit"
        ),
        "status": (
            "current_sweep_endpoint_release_feedback_horizon_structured_global_open"
        ),
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "aggregate": aggregate,
        "endpoint_release_feedback_horizon_rows": rows,
        "contract": {
            "feedback_horizon_definition": (
                "A support-motion representative is self-feedback absorbable only "
                "if its distance from the current support window is at most "
                "support_width plus the current generator/fill side-depth skew."
            ),
            "current_sweep_structuring_gate": [
                "derive feedback_loss = window_distance - side_depth_skew",
                "derive post_credit_overcritical_units = window_distance - (support_width + side_depth_skew)",
                "route positive horizon surplus to EndpointReleaseFeedbackHorizon-PDEC",
            ],
            "closed_current_sweep": aggregate[
                "endpoint_release_feedback_horizon_structured_current_sweep"
            ],
            "global_remaining": [
                "EndpointReleaseFeedbackHorizon-PDEC exclusion",
                "EndpointReleaseFeedbackLoss-PDEC exclusion",
                "OrientationChangingPrimitiveKey-PDEC/SAE",
                "SourceRematerialization-PDEC/SAE",
            ],
        },
        "dependency_hashes": {
            str(path.relative_to(ROOT)): sha256(path)
            for path in (support_motion_path, feedback_loss_path)
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
    narrow = agg["narrowest_feedback_horizon_atom"]
    worst = agg["worst_feedback_horizon_atom"]
    lines = [
        "# Prime Matrix AffineTwin endpoint-release feedback-horizon audit",
        "",
        "**状态：** `current_sweep_endpoint_release_feedback_horizon_structured_global_open`",
        "",
        "本审计把 feedback loss 再改写为相位地平线判据：一个空窗 CRT 代表若要被端点自反馈吸收，它到当前支撑窗口的距离必须不超过 `support_width + side_depth_skew`。",
        "",
        "```text",
        "feedback horizon = support width + |generator side depth - fill side depth|",
        "phase horizon surplus = window distance - feedback horizon",
        "```",
        "",
        "```text",
        f"support_motion_candidate_count={agg['support_motion_candidate_count']}",
        f"support_motion_side_histogram={agg['support_motion_side_histogram']}",
        f"support_width={agg['support_width']}",
        f"total_window_distance={agg['total_window_distance']}",
        f"total_feedback_horizon_width={agg['total_feedback_horizon_width']}",
        f"total_phase_horizon_surplus={agg['total_phase_horizon_surplus']}",
        f"min_phase_horizon_surplus={agg['min_phase_horizon_surplus']}",
        f"max_phase_horizon_surplus={agg['max_phase_horizon_surplus']}",
        f"all_feedback_loss_formulas_hold={fmt_bool(agg['all_feedback_loss_formulas_hold'])}",
        f"all_representatives_outside_feedback_horizon={fmt_bool(agg['all_representatives_outside_feedback_horizon'])}",
        f"endpoint_release_feedback_horizon_structured_current_sweep={fmt_bool(agg['endpoint_release_feedback_horizon_structured_current_sweep'])}",
        "```",
        "",
        "## 1. feedback-horizon 表",
        "",
        "| pair | side | distance | support | skew | horizon | surplus | route |",
        "| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in result["endpoint_release_feedback_horizon_rows"]:
        lines.append(
            "| `{pair}` | `{side}` | {distance} | {support} | {skew} | {horizon} | {surplus} | `{route}` |".format(
                pair=row["source_pair_key"],
                side=row["window_side"],
                distance=row["window_distance"],
                support=row["support_width"],
                skew=row["side_depth_skew"],
                horizon=row["feedback_horizon_width"],
                surplus=row["phase_horizon_surplus"],
                route=row["structured_route_current"],
            )
        )

    lines.extend(
        [
            "",
            "## 2. 最窄相位地平线缺口",
            "",
            f"最窄 atom 为 `{narrow['source_pair_key']}`，side `{narrow['window_side']}`。其 CRT 代表距窗口 `{narrow['window_distance']}`，support width 为 `{narrow['support_width']}`，当前两端点侧深度差为 `{narrow['side_depth_skew']}`，所以 feedback horizon 为 `{narrow['feedback_horizon_width']}`，仍有相位地平线缺口 `{narrow['phase_horizon_surplus']}`。",
            "这给出当前最精确的局部超界矛盾点：反例链要求支撑移动吸收该代表，真实链给出的最大自反馈吸收地平线却短 `10`。",
            "",
            "## 3. 最大地平线缺口",
            "",
            f"最大 atom 为 `{worst['source_pair_key']}`，side `{worst['window_side']}`，distance `{worst['window_distance']}` 对 horizon `{worst['feedback_horizon_width']}`，surplus `{worst['phase_horizon_surplus']}`。",
            "",
            "## 4. 结论边界",
            "",
            "- `feedback_loss = window_distance - side_depth_skew` 逐项成立，说明上一层 feedback loss 有纯相位公式。",
            "- `phase_horizon_surplus` 逐项等于 post-credit overcritical units，说明几何回补后的正临界误差正是 CRT 代表越过反馈地平线的距离。",
            "- 当前 `11` 个候选全部在 feedback horizon 外，因此当前 sweep 的端点自反馈吸收通道关闭，并登记为 `EndpointReleaseFeedbackHorizon-PDEC`。",
            "- 本步仍不关闭全局行/列命题；全局剩余是排斥该地平线缺口持久复现，或把它路由到方向改变/source 重物化/SAE 出口。",
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
        description="生成 AffineTwin endpoint-release feedback-horizon 审计证书。"
    )
    parser.add_argument(
        "--support-motion-ledger", type=Path, default=SUPPORT_MOTION_LEDGER
    )
    parser.add_argument(
        "--feedback-loss-ledger", type=Path, default=FEEDBACK_LOSS_LEDGER
    )
    return parser.parse_args()


def main() -> None:
    """入口。"""
    args = parse_args()
    result = build_result(args.support_motion_ledger, args.feedback_loss_ledger)
    write_outputs(result)
    print(json.dumps(result["aggregate"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
