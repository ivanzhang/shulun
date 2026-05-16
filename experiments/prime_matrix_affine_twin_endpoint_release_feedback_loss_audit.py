#!/usr/bin/env python3
"""生成 AffineTwin endpoint-release feedback-loss 审计证书。

用法示例：
  python3 experiments/prime_matrix_affine_twin_endpoint_release_feedback_loss_audit.py
  python3 -m json.tool data/prime-matrix-affine-twin-endpoint-release-feedback-loss-ledger.json

输出：
  data/prime-matrix-affine-twin-endpoint-release-feedback-loss-ledger.json
  docs/monograph/prime-matrix-affine-twin-endpoint-release-feedback-loss-audit.json
  docs/monograph/prime-matrix-affine-twin-endpoint-release-feedback-loss-audit.md
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

SUPPORT_MOTION_LEDGER = DATA / "prime-matrix-affine-twin-support-motion-depth-ledger.json"
ENDPOINT_CRITICAL_LEDGER = DATA / (
    "prime-matrix-affine-twin-endpoint-release-critical-error-ledger.json"
)

OUT_LEDGER = DATA / "prime-matrix-affine-twin-endpoint-release-feedback-loss-ledger.json"
OUT_JSON = DOCS / "prime-matrix-affine-twin-endpoint-release-feedback-loss-audit.json"
OUT_MD = DOCS / "prime-matrix-affine-twin-endpoint-release-feedback-loss-audit.md"


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


def critical_rows_by_pair(endpoint_critical: dict[str, Any]) -> dict[str, dict[str, Any]]:
    """按 source pair 建立端点临界误差索引。"""
    return {
        str(row["source_pair_key"]): row
        for row in endpoint_critical["endpoint_release_critical_error_rows"]
    }


def feedback_row(
    support_row: dict[str, Any],
    critical_row: dict[str, Any],
) -> dict[str, Any]:
    """构造单个端点释放反馈损耗行。"""
    support_width = int(support_row["support_width"])
    endpoint_load = int(support_row["endpoint_release_total_required"])
    geometric_gain_credit = int(support_row["endpoint_release_max_required"])
    feedback_loss = endpoint_load - geometric_gain_credit
    post_credit_overcritical_units = feedback_loss - support_width
    return {
        "source_pair_key": str(support_row["source_pair_key"]),
        "q": int(support_row["q"]),
        "window_side": str(support_row["window_side"]),
        "nearest_representative": int(support_row["nearest_representative"]),
        "support_width": support_width,
        "actual_endpoint_release_load": endpoint_load,
        "geometric_support_gain_credit": geometric_gain_credit,
        "coupled_second_endpoint_feedback_loss": feedback_loss,
        "post_credit_overcritical_units": post_credit_overcritical_units,
        "post_credit_feedback_error": post_credit_overcritical_units / support_width,
        "feedback_loss_to_support_width_ratio": feedback_loss / support_width,
        "feedback_loss_to_gain_ratio": feedback_loss / geometric_gain_credit,
        "load_to_geometric_gain_ratio": endpoint_load / geometric_gain_credit,
        "generator_endpoint_release_required": int(
            support_row["generator_endpoint_release_required"]
        ),
        "fill_endpoint_release_required": int(
            support_row["fill_endpoint_release_required"]
        ),
        "feedback_loss_equals_smaller_endpoint_release": feedback_loss
        == min(
            int(support_row["generator_endpoint_release_required"]),
            int(support_row["fill_endpoint_release_required"]),
        ),
        "original_endpoint_critical_error": float(
            critical_row["endpoint_release_critical_error"]
        ),
        "original_structured_route": str(critical_row["structured_route_current"]),
        "post_credit_feedback_loss_positive": feedback_loss > 0,
        "post_credit_feedback_loss_supercritical": feedback_loss > support_width,
        "self_feedback_absorption_possible_current": feedback_loss <= 0,
        "structured_route_current": "EndpointReleaseFeedbackLoss-PDEC"
        if feedback_loss > support_width
        else "EndpointReleaseFeedbackLoss-Borderline",
        "pinned_endpoint": str(support_row["pinned_endpoint"]),
    }


def build_result(
    support_motion_path: Path,
    endpoint_critical_path: Path,
) -> dict[str, Any]:
    """构造 endpoint-release feedback-loss 审计结果。"""
    support_motion = load_json(support_motion_path)
    endpoint_critical = load_json(endpoint_critical_path)
    critical_by_pair = critical_rows_by_pair(endpoint_critical)

    rows = [
        feedback_row(row, critical_by_pair[str(row["source_pair_key"])])
        for row in support_motion["support_motion_rows"]
    ]
    if not rows:
        raise RuntimeError("no support-motion rows found")

    support_width = int(support_motion["aggregate"]["support_width_current"])
    total_load = sum(int(row["actual_endpoint_release_load"]) for row in rows)
    total_gain_credit = sum(int(row["geometric_support_gain_credit"]) for row in rows)
    total_feedback_loss = sum(
        int(row["coupled_second_endpoint_feedback_loss"]) for row in rows
    )
    total_support_budget = support_width * len(rows)
    narrowest = min(
        rows,
        key=lambda row: (
            int(row["coupled_second_endpoint_feedback_loss"]),
            int(row["actual_endpoint_release_load"]),
            str(row["source_pair_key"]),
        ),
    )
    worst = max(
        rows,
        key=lambda row: (
            float(row["post_credit_feedback_error"]),
            int(row["coupled_second_endpoint_feedback_loss"]),
            str(row["source_pair_key"]),
        ),
    )

    aggregate = {
        "support_motion_ledger": str(support_motion_path.relative_to(ROOT)),
        "endpoint_critical_ledger": str(endpoint_critical_path.relative_to(ROOT)),
        "support_motion_candidate_count": len(rows),
        "support_width": support_width,
        "total_endpoint_release_load": total_load,
        "total_geometric_support_gain_credit": total_gain_credit,
        "total_coupled_second_endpoint_feedback_loss": total_feedback_loss,
        "total_support_width_budget": total_support_budget,
        "total_feedback_loss_to_support_budget_ratio": total_feedback_loss
        / total_support_budget,
        "total_post_credit_feedback_error": total_feedback_loss
        / total_support_budget
        - 1,
        "min_feedback_loss": min(
            int(row["coupled_second_endpoint_feedback_loss"]) for row in rows
        ),
        "max_feedback_loss": max(
            int(row["coupled_second_endpoint_feedback_loss"]) for row in rows
        ),
        "min_post_credit_feedback_error": min(
            float(row["post_credit_feedback_error"]) for row in rows
        ),
        "max_post_credit_feedback_error": max(
            float(row["post_credit_feedback_error"]) for row in rows
        ),
        "min_feedback_loss_to_gain_ratio": min(
            float(row["feedback_loss_to_gain_ratio"]) for row in rows
        ),
        "max_feedback_loss_to_gain_ratio": max(
            float(row["feedback_loss_to_gain_ratio"]) for row in rows
        ),
        "narrowest_feedback_loss_atom": {
            "source_pair_key": narrowest["source_pair_key"],
            "window_side": narrowest["window_side"],
            "actual_endpoint_release_load": narrowest[
                "actual_endpoint_release_load"
            ],
            "geometric_support_gain_credit": narrowest[
                "geometric_support_gain_credit"
            ],
            "coupled_second_endpoint_feedback_loss": narrowest[
                "coupled_second_endpoint_feedback_loss"
            ],
            "support_width": narrowest["support_width"],
            "post_credit_feedback_error": narrowest[
                "post_credit_feedback_error"
            ],
            "structured_route_current": narrowest["structured_route_current"],
        },
        "worst_feedback_loss_atom": {
            "source_pair_key": worst["source_pair_key"],
            "window_side": worst["window_side"],
            "actual_endpoint_release_load": worst["actual_endpoint_release_load"],
            "geometric_support_gain_credit": worst[
                "geometric_support_gain_credit"
            ],
            "coupled_second_endpoint_feedback_loss": worst[
                "coupled_second_endpoint_feedback_loss"
            ],
            "support_width": worst["support_width"],
            "post_credit_feedback_error": worst["post_credit_feedback_error"],
            "structured_route_current": worst["structured_route_current"],
        },
        "all_feedback_losses_positive": all(
            int(row["coupled_second_endpoint_feedback_loss"]) > 0 for row in rows
        ),
        "all_feedback_losses_exceed_support_width": all(
            int(row["coupled_second_endpoint_feedback_loss"]) > support_width
            for row in rows
        ),
        "all_feedback_losses_equal_smaller_endpoint_release": all(
            bool(row["feedback_loss_equals_smaller_endpoint_release"]) for row in rows
        ),
        "endpoint_release_self_feedback_absorption_closed_current_sweep": all(
            not bool(row["self_feedback_absorption_possible_current"]) for row in rows
        ),
        "endpoint_release_feedback_loss_structured_current_sweep": all(
            str(row["structured_route_current"]) == "EndpointReleaseFeedbackLoss-PDEC"
            for row in rows
        ),
        "global_endpoint_release_feedback_loss_excluded": False,
        "row_column_unconditional_closed": False,
    }

    return {
        "certificate_type": (
            "prime_matrix_affine_twin_endpoint_release_feedback_loss_audit"
        ),
        "status": (
            "current_sweep_endpoint_release_feedback_loss_structured_global_open"
        ),
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "aggregate": aggregate,
        "endpoint_release_feedback_loss_rows": rows,
        "contract": {
            "feedback_loss_definition": (
                "After crediting the maximum endpoint movement as geometric support "
                "gain, the remaining load is the smaller synchronized endpoint release."
            ),
            "current_sweep_structuring_gate": [
                "credit all possible one-sided geometric support gain",
                "measure the unrecovered coupled second-endpoint release",
                "if that residual still exceeds the original support width, route it to EndpointReleaseFeedbackLoss-PDEC",
            ],
            "closed_current_sweep": aggregate[
                "endpoint_release_feedback_loss_structured_current_sweep"
            ],
            "global_remaining": [
                "EndpointReleaseFeedbackLoss-PDEC exclusion",
                "EndpointReleaseCoupling-PDEC exclusion",
                "OrientationChangingPrimitiveKey-PDEC/SAE",
                "SourceRematerialization-PDEC/SAE",
            ],
        },
        "dependency_hashes": {
            str(path.relative_to(ROOT)): sha256(path)
            for path in (support_motion_path, endpoint_critical_path)
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
    narrow = agg["narrowest_feedback_loss_atom"]
    worst = agg["worst_feedback_loss_atom"]
    lines = [
        "# Prime Matrix AffineTwin endpoint-release feedback-loss audit",
        "",
        "**状态：** `current_sweep_endpoint_release_feedback_loss_structured_global_open`",
        "",
        "本审计继续下钻端点释放临界误差：即使把端点移动造成的几何支撑扩张全部记作容量回补，双端点同步仍留下不可回收的第二端点反馈损耗。",
        "",
        "```text",
        "feedback loss = endpoint release load - geometric support gain credit",
        "geometric support gain credit = max(generator release, fill release)",
        "feedback loss = min(generator release, fill release)",
        "post-credit feedback error = feedback loss / support width - 1",
        "```",
        "",
        "```text",
        f"support_motion_candidate_count={agg['support_motion_candidate_count']}",
        f"support_width={agg['support_width']}",
        f"total_endpoint_release_load={agg['total_endpoint_release_load']}",
        f"total_geometric_support_gain_credit={agg['total_geometric_support_gain_credit']}",
        f"total_coupled_second_endpoint_feedback_loss={agg['total_coupled_second_endpoint_feedback_loss']}",
        f"total_post_credit_feedback_error={fmt_decimal(agg['total_post_credit_feedback_error'])}",
        f"min_feedback_loss={agg['min_feedback_loss']}",
        f"max_feedback_loss={agg['max_feedback_loss']}",
        f"min_post_credit_feedback_error={fmt_decimal(agg['min_post_credit_feedback_error'])}",
        f"all_feedback_losses_exceed_support_width={fmt_bool(agg['all_feedback_losses_exceed_support_width'])}",
        f"endpoint_release_feedback_loss_structured_current_sweep={fmt_bool(agg['endpoint_release_feedback_loss_structured_current_sweep'])}",
        "```",
        "",
        "## 1. feedback-loss 表",
        "",
        "| pair | side | load | gain credit | feedback loss | support width | post-credit error | route |",
        "| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in result["endpoint_release_feedback_loss_rows"]:
        lines.append(
            "| `{pair}` | `{side}` | {load} | {gain} | {loss} | {width} | {err} | `{route}` |".format(
                pair=row["source_pair_key"],
                side=row["window_side"],
                load=row["actual_endpoint_release_load"],
                gain=row["geometric_support_gain_credit"],
                loss=row["coupled_second_endpoint_feedback_loss"],
                width=row["support_width"],
                err=fmt_decimal(row["post_credit_feedback_error"]),
                route=row["structured_route_current"],
            )
        )

    lines.extend(
        [
            "",
            "## 2. 最窄反馈损耗点",
            "",
            f"最窄 atom 为 `{narrow['source_pair_key']}`，side `{narrow['window_side']}`。端点释放负载为 `{narrow['actual_endpoint_release_load']}`，其中可全部记作几何支撑扩张的最大信用为 `{narrow['geometric_support_gain_credit']}`，仍余不可回收反馈损耗 `{narrow['coupled_second_endpoint_feedback_loss']}`。",
            f"由于当前 support width 为 `{narrow['support_width']}`，即便在全额回补后，post-credit feedback error 仍为 `{fmt_decimal(narrow['post_credit_feedback_error'])}`。这把 `EndpointReleaseCoupling` 继续压成 `{narrow['structured_route_current']}`。",
            "",
            "## 3. 最大反馈损耗波",
            "",
            f"最大 atom 为 `{worst['source_pair_key']}`，side `{worst['window_side']}`，反馈损耗 `{worst['coupled_second_endpoint_feedback_loss']}` 对 support width `{worst['support_width']}`，post-credit feedback error `{fmt_decimal(worst['post_credit_feedback_error'])}`。",
            "",
            "## 4. 结论边界",
            "",
            "- 当前 `11` 个 support-motion 候选在全额几何支撑回补后，反馈损耗仍全部超过原 support width。",
            "- 反馈损耗逐项等于较小端点释放量，说明它是双端点同步耦合的真实结构税，不是 formal envelope 重复记账。",
            "- 本步不关闭全局行/列命题；它把持久端点耦合的剩余硬点进一步压成 `EndpointReleaseFeedbackLoss-PDEC` 的全局排斥或路由。",
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
        description="生成 AffineTwin endpoint-release feedback-loss 审计证书。"
    )
    parser.add_argument(
        "--support-motion-ledger", type=Path, default=SUPPORT_MOTION_LEDGER
    )
    parser.add_argument(
        "--endpoint-critical-ledger", type=Path, default=ENDPOINT_CRITICAL_LEDGER
    )
    return parser.parse_args()


def main() -> None:
    """入口。"""
    args = parse_args()
    result = build_result(args.support_motion_ledger, args.endpoint_critical_ledger)
    write_outputs(result)
    print(json.dumps(result["aggregate"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
