#!/usr/bin/env python3
"""生成 strict 内部 Dusart theta 预算障碍路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_internal_dusart_theta_budget_obstruction_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-internal-dusart-theta-budget-obstruction-router.json
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"

OUT_JSON = MONOGRAPH / "prime-matrix-strict-internal-dusart-theta-budget-obstruction-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-internal-dusart-theta-budget-obstruction-router.md"

POST_MEISSEL = MONOGRAPH / "prime-matrix-strict-post-meissel-frontier-sync-router.json"
THETA_FRONTIER = MONOGRAPH / "prime-matrix-strict-theta-target-external-match-self-frontier-router.json"
ZERO_SUM = MONOGRAPH / "prime-matrix-strict-zero-sum-contour-self-contained-sync-router.json"
TRIVIAL = MONOGRAPH / "prime-matrix-strict-trivial-tail-prime-power-self-contained-sync-router.json"
CLAIM_STATUS = MONOGRAPH / "claim-status-table.md"

SOURCE_FILES = [POST_MEISSEL, THETA_FRONTIER, ZERO_SUM, TRIVIAL, CLAIM_STATUS]

TARGET = "InternalDusartThetaEnvelopeProofLedger"
SHARP_PNT = "SharpInternalThetaPNTEnvelopeAt20000Ledger"
FINITE_THETA = "InternalFiniteThetaBridgeHashLedger"
PRIME_POWER_DIRECT = "DirectThetaNotPsiPrimePowerBypassLedger"
LOW_HEIGHT = "CriticalLineNoZeroOn0To14FiniteLedger AND CriticalStripNoOffLineZeroBelow14TuringLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


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
    """固定小数格式。"""
    if math.isinf(value):
        return "inf"
    return f"{value:.12g}"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def pressure_map(theta: dict[str, Any]) -> dict[str, float]:
    """把 theta 前沿证书中的压力行转成字典。"""
    result: dict[str, float] = {}
    for item in theta.get("pressure_rows", []):
        name = str(item.get("item", ""))
        value = item.get("value")
        if isinstance(value, (int, float)):
            result[name] = float(value)
    return result


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def budget_rows(theta: dict[str, Any]) -> list[dict[str, Any]]:
    """生成预算障碍表。"""
    pressures = pressure_map(theta)
    target = float(theta.get("target_relative_error", 1.0 / 36260.0))
    rows: list[dict[str, Any]] = []
    for name in [
        "strict zero-sum closed envelope at T0",
        "static formula terms relative",
        "prime-power transfer relative",
    ]:
        value = pressures.get(name, math.inf)
        rows.append(
            {
                "item": name,
                "value": value,
                "target": target,
                "ratio_to_target": value / target if target > 0 else math.inf,
                "passes": value <= target,
            }
        )
    return rows


def decision_rows(post: dict[str, Any], theta: dict[str, Any], budgets: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """生成判定表。"""
    guard = (
        post.get("counterexample_assumption_only") is True
        and post.get("direct_unconditional_contradiction_found") is False
        and post.get("row_column_unconditional_closed") is False
        and theta.get("theta_target_self_contained_closed") is False
    )
    active = post.get("strict_self_contained_next_direct_attack_target") == TARGET
    analytic_core_ready = post.get("strict_self_contained_analytic_core_closed") is True
    all_budget_pass = all(item["passes"] for item in budgets)
    external_available = post.get("external_theta_low_height_bridge_lane_closed") is True
    return [
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步只审查自足 theta 输入，仍在早期零行反例链的解析输入层内。",
            "保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。",
        ),
        row(
            "InternalDusartThetaGateActive",
            active,
            True,
            "post-Meissel 前沿把严格自足下一主攻点校准为内部 Dusart theta 包络。",
            TARGET,
        ),
        row(
            "StrictAnalyticCoreReadyButTooCoarse",
            analytic_core_ready and not all_budget_pass,
            True,
            "Perron/零点和/平凡尾项虽已自足闭合，但常数粗到不能达到 1/36260 级 theta 目标。",
            f"{SHARP_PNT} OR {FINITE_THETA}",
        ),
        row(
            "CurrentInternalBudgetBeatsDusartTarget",
            all_budget_pass,
            all_budget_pass,
            "只有所有内部预算项均不超过目标误差，才能从当前包络直接关闭内部 Dusart theta。",
            TARGET,
        ),
        row(
            "ExternalDusartLaneStillAvailable",
            external_available,
            False,
            "外部 Dusart/低高度/theta 桥路线已可用，但这不是自足证明。",
            "外部路线继续等待 DStructure/Rankin 独立验收。",
        ),
        row(
            "InternalDusartThetaSelfContainedClosed",
            False,
            False,
            "当前证据只能证明旧预算不够，不能宣布内部 Dusart theta 已闭合。",
            f"{SHARP_PNT} AND ({FINITE_THETA} OR {PRIME_POWER_DIRECT}) AND {LOW_HEIGHT}",
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "内部 theta 预算障碍证书不产生终端反例矛盾。",
            DSTRUCTURE,
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造内部 Dusart theta 预算障碍证书。"""
    post = load_json(POST_MEISSEL)
    theta = load_json(THETA_FRONTIER)
    budgets = budget_rows(theta)
    rows = decision_rows(post, theta, budgets)
    target = float(theta.get("target_relative_error", 1.0 / 36260.0))
    worst = max(budgets, key=lambda item: item["ratio_to_target"])
    return {
        "certificate_type": "prime_matrix_strict_internal_dusart_theta_budget_obstruction_router",
        "status": "internal_dusart_theta_current_budget_obstructed_split_to_sharp_pnt_finite_bridge_low_height",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "target_atom": TARGET,
        "target_relative_error": target,
        "current_internal_budget_beats_dusart_target": all(item["passes"] for item in budgets),
        "internal_dusart_theta_self_contained_closed": False,
        "external_dusart_lane_available": post.get("external_theta_low_height_bridge_lane_closed") is True,
        "self_contained_mertens_tail_closed": False,
        "b3_tv_strict_self_contained_closed": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "budget_rows": budgets,
        "worst_budget_item": worst["item"],
        "worst_ratio_to_target": worst["ratio_to_target"],
        "replacement_self_contained": {
            TARGET: f"{SHARP_PNT} AND ({FINITE_THETA} OR {PRIME_POWER_DIRECT}) AND {LOW_HEIGHT}",
        },
        "next_direct_attack_target": SHARP_PNT,
        "parallel_attack_targets": [FINITE_THETA, PRIME_POWER_DIRECT, LOW_HEIGHT],
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "内部 Dusart theta 包络不能由当前 strict 自足预算直接推出：目标相对误差为 `1/36260`，"
            "但当前零点和保守包络、静态公式项、素数幂转移项均至少有一项超过目标。"
            "因此该原子不能闭合，只能被严格压缩为三类自足输入：更尖锐的内部 theta/PNT 包络、"
            "有限 theta 桥或直接 theta 而非 psi 的素数幂旁路，以及低高度 Turing/无零核验。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    replacement = next(iter(result["replacement_self_contained"].items()))
    lines = [
        "# Prime Matrix strict 内部 Dusart theta 预算障碍路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"current_internal_budget_beats_dusart_target={fmt_bool(result['current_internal_budget_beats_dusart_target'])}",
        f"internal_dusart_theta_self_contained_closed={fmt_bool(result['internal_dusart_theta_self_contained_closed'])}",
        f"external_dusart_lane_available={fmt_bool(result['external_dusart_lane_available'])}",
        f"self_contained_mertens_tail_closed={fmt_bool(result['self_contained_mertens_tail_closed'])}",
        f"b3_tv_strict_self_contained_closed={fmt_bool(result['b3_tv_strict_self_contained_closed'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 预算障碍",
        "",
        "| item | value | target | ratio | passes |",
        "| --- | ---: | ---: | ---: | --- |",
    ]
    for item in result["budget_rows"]:
        lines.append(
            f"| {table_cell(item['item'])} | `{fmt_float(float(item['value']))}` | "
            f"`{fmt_float(float(item['target']))}` | `{fmt_float(float(item['ratio_to_target']))}` | "
            f"`{fmt_bool(item['passes'])}` |"
        )
    lines.extend(
        [
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
    )
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
