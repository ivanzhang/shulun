#!/usr/bin/env python3
"""生成 strict 内部 theta contour 预算缺口路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_internal_theta_contour_budget_gap_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-internal-theta-contour-budget-gap-router.json
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"

OUT_JSON = MONOGRAPH / "prime-matrix-strict-internal-theta-contour-budget-gap-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-internal-theta-contour-budget-gap-router.md"

POST_FINITE_THETA = MONOGRAPH / "prime-matrix-strict-post-finite-theta-frontier-sync-router.json"
ZERO_SUM = MONOGRAPH / "prime-matrix-strict-zero-sum-contour-self-contained-sync-router.json"
FINITE_THETA = MONOGRAPH / "prime-matrix-strict-finite-theta-bridge-self-contained-router.json"
CLAIM_STATUS = MONOGRAPH / "claim-status-table.md"

SOURCE_FILES = [POST_FINITE_THETA, ZERO_SUM, FINITE_THETA, CLAIM_STATUS]

TARGET = "InternalZeroFreeRegionToThetaContourEnvelopeLedger"
SHARP_CONTOUR = "SharpInternalThetaContourStartBudgetLedger"
EXTENDED_FINITE = "RaisedAnalyticThresholdFiniteThetaBridgeExtensionLedger"
LOW_HEIGHT = "CriticalLineNoZeroOn0To14FiniteLedger AND CriticalStripNoOffLineZeroBelow14TuringLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

ANCHOR_X = 20_000.0
DENOMINATOR = 36_260.0
TARGET_RELATIVE = 1.0 / DENOMINATOR


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记本步依赖文件哈希。"""
    return {str(path.relative_to(ROOT)): sha256(path) for path in SOURCE_FILES if path.exists()}


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def fmt_float(value: float) -> str:
    """固定数值格式。"""
    return f"{value:.12g}"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def zero_sum_anchor_row(zero_sum: dict[str, Any]) -> dict[str, Any]:
    """取 T=14, x=20000 的当前 contour 预算行。"""
    for item in zero_sum.get("pressure_rows", []):
        if abs(float(item.get("x", 0.0)) - ANCHOR_X) < 1e-9 and abs(float(item.get("T", 0.0)) - 14.0) < 1e-9:
            return item
    return {}


def solve_log_threshold(c_zero_sum: float, c_region: float, t0: float) -> dict[str, float]:
    """估算固定 T0 当前粗 contour 需要多大 x 才能降到目标量级。"""
    log_t = math.log(t0 + 3.0)
    a = 1.0 / (c_region * log_t)
    log_shift = math.log(t0 + 3.0)

    def f(y: float) -> float:
        # y=log(x(T0+3)); c*y^2*exp(-a*(y-log_shift)) = target
        return math.log(c_zero_sum / TARGET_RELATIVE) + 2.0 * math.log(y) - a * (y - log_shift)

    y = 160_000.0
    for _ in range(30):
        derivative = 2.0 / y - a
        y -= f(y) / derivative
    log_x = y - log_shift
    return {
        "a": a,
        "log_threshold_x": log_x,
        "log10_threshold_x": log_x / math.log(10.0),
    }


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_result() -> dict[str, Any]:
    """构造内部 theta contour 预算缺口证书。"""
    post = load_json(POST_FINITE_THETA)
    zero_sum = load_json(ZERO_SUM)
    finite = load_json(FINITE_THETA)
    anchor = zero_sum_anchor_row(zero_sum)
    closed_relative = float(anchor.get("closed_relative", math.inf))
    ratio = closed_relative / TARGET_RELATIVE
    threshold = solve_log_threshold(
        float(zero_sum.get("C_zero_sum", 65536.0)),
        float(zero_sum.get("C_region", 1280.0)),
        float(zero_sum.get("T0", 14.0)),
    )
    finite_ready = (
        finite.get("finite_theta_bridge_below_20000_self_contained_closed") is True
        and finite.get("theta_target_at_20000_self_contained_closed") is True
    )
    active = post.get("next_direct_attack_target") == TARGET
    contour_budget_passes_at_anchor = closed_relative <= TARGET_RELATIVE
    rows = [
        row(
            "CounterexampleBranchGuardPreserved",
            post.get("counterexample_assumption_only") is True and post.get("row_column_unconditional_closed") is False,
            True,
            "本步只审查高段内部 theta contour 输入，不使用真实零行缺席。",
            "保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。",
        ),
        row(
            "InternalThetaContourGateActive",
            active,
            True,
            "有限 theta 桥闭合后，新的自足最窄点正是 x>=20000 的内部 theta/PNT contour。",
            TARGET,
        ),
        row(
            "FiniteThetaBridgeReadyAtInterface",
            finite_ready,
            True,
            "0<x<=20000 的有限桥与锚点已自足闭合，高段 contour 只需从接口向右接上。",
            "接口值已闭合。",
        ),
        row(
            "CurrentC65536ContourBeatsDusartAtAnchor",
            contour_budget_passes_at_anchor,
            contour_budget_passes_at_anchor,
            "当前 C=65536、C_region=1280 的粗 contour 在 x=20000 接口处远不能达到 1/36260。",
            SHARP_CONTOUR,
        ),
        row(
            "RaisedThresholdAlternativeFeasibleOnlyAsHugeFiniteBridge",
            False,
            False,
            "若不尖锐化 contour，只能把有限桥延长到天文阈值后再接当前粗衰减。",
            EXTENDED_FINITE,
        ),
        row(
            "InternalThetaContourSelfContainedClosed",
            False,
            False,
            "当前证据压缩出明确缺口，但不关闭内部高段 theta contour。",
            f"{SHARP_CONTOUR} OR {EXTENDED_FINITE}; plus {LOW_HEIGHT}",
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "该预算缺口证书不产生最终反例矛盾。",
            DSTRUCTURE,
        ),
    ]
    return {
        "certificate_type": "prime_matrix_strict_internal_theta_contour_budget_gap_router",
        "status": "internal_theta_contour_budget_gap_reduced_to_sharp_contour_or_huge_finite_bridge",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "finite_theta_bridge_ready_at_interface": finite_ready,
        "current_c65536_contour_beats_dusart_at_anchor": contour_budget_passes_at_anchor,
        "internal_theta_contour_self_contained_closed": False,
        "self_contained_mertens_tail_closed": False,
        "b3_tv_strict_self_contained_closed": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "target_relative_error": TARGET_RELATIVE,
        "anchor_closed_relative_bound": closed_relative,
        "anchor_ratio_to_target": ratio,
        "coarse_contour_threshold_estimate": threshold,
        "replacement_self_contained": {
            TARGET: f"{SHARP_CONTOUR} OR {EXTENDED_FINITE}",
        },
        "next_direct_attack_target": SHARP_CONTOUR,
        "parallel_attack_targets": [EXTENDED_FINITE, LOW_HEIGHT],
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "有限 theta 桥已经把 `0<x<=20000` 关上；真正剩余是从 `x=20000` 往右接内部 theta/PNT contour。"
            "现有自足零点和预算 `C_Z=65536, C_region=1280` 在接口处的相对包络约为目标 `1/36260` 的 "
            f"`{ratio:.3g}` 倍，不能闭合。若不改进 contour 常数，只能把有限桥延长到约 "
            f"`10^{threshold['log10_threshold_x']:.0f}` 量级后才可能接上，实际不可作为当前闭合路径。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    threshold = result["coarse_contour_threshold_estimate"]
    replacement = next(iter(result["replacement_self_contained"].items()))
    lines = [
        "# Prime Matrix strict 内部 theta contour 预算缺口路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"finite_theta_bridge_ready_at_interface={fmt_bool(result['finite_theta_bridge_ready_at_interface'])}",
        f"current_c65536_contour_beats_dusart_at_anchor={fmt_bool(result['current_c65536_contour_beats_dusart_at_anchor'])}",
        f"internal_theta_contour_self_contained_closed={fmt_bool(result['internal_theta_contour_self_contained_closed'])}",
        f"self_contained_mertens_tail_closed={fmt_bool(result['self_contained_mertens_tail_closed'])}",
        f"b3_tv_strict_self_contained_closed={fmt_bool(result['b3_tv_strict_self_contained_closed'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 接口预算",
        "",
        "| item | value |",
        "| --- | ---: |",
        f"| target relative error | `{fmt_float(result['target_relative_error'])}` |",
        f"| C=65536 contour relative bound at x=20000 | `{fmt_float(result['anchor_closed_relative_bound'])}` |",
        f"| ratio to target | `{fmt_float(result['anchor_ratio_to_target'])}` |",
        f"| estimated log10 threshold if constants unchanged | `{fmt_float(threshold['log10_threshold_x'])}` |",
        "",
        "## 2. 自足替换",
        "",
        "```text",
        replacement[0],
        "  =>",
        replacement[1],
        "```",
        "",
        "## 3. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=table_cell(item["gate"]),
                closed=fmt_bool(item["closed"]),
                proved=fmt_bool(item["proved"]),
                meaning=table_cell(item["meaning"]),
                remaining=table_cell(item["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 下一最窄点",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """写出 JSON 和 Markdown 证书。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")
    print(result["status"])
    print("next_direct_attack_target=", result["next_direct_attack_target"])


if __name__ == "__main__":
    main()
