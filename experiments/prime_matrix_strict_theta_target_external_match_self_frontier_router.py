#!/usr/bin/env python3
"""生成 strict theta@20000 外部匹配与自足前沿路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_theta_target_external_match_self_frontier_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-theta-target-external-match-self-frontier-router.json
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"

OUT_JSON = MONOGRAPH / "prime-matrix-strict-theta-target-external-match-self-frontier-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-theta-target-external-match-self-frontier-router.md"

TRIVIAL_SYNC = MONOGRAPH / "prime-matrix-strict-trivial-tail-prime-power-self-contained-sync-router.json"
ZERO_SUM_SYNC = MONOGRAPH / "prime-matrix-strict-zero-sum-contour-self-contained-sync-router.json"
THETA_EXTERNAL = MONOGRAPH / "prime-matrix-b3-theta-target-dusart-router.json"
CLAIM_STATUS = MONOGRAPH / "claim-status-table.md"

SOURCE_FILES = [TRIVIAL_SYNC, ZERO_SUM_SYNC, THETA_EXTERNAL, CLAIM_STATUS]

OLD_ATOM = "ThetaEnvelopeTargetAt20000NumericalBudgetLedger"
EXTERNAL_CLOSED = "DusartThetaEnvelopeTargetAt20000ExternalClosedOneOver36260"
STRICT_EXTERNAL_CLOSED = "ThetaEnvelopeTargetAt20000StrictExternalMatchedDusartOneOver36260"
SELF_INPUT = "InternalDusartThetaEnvelopeProofLedger"
FINITE_BRIDGE = "FiniteThetaEnvelopeBridgeBelowAnalyticThreshold"
FINITE_LOW_HEIGHT = "FiniteLowHeightZeroCheckLedger"
MERTENS_TAIL = "SelfContainedDusartReciprocalPrimeProofAppendixXGe10372"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

ANCHOR_X = 20_000.0
DENOMINATOR = 36_260.0
TARGET_RELATIVE_ERROR = 1.0 / DENOMINATOR


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记证据文件哈希。"""
    return {str(path.relative_to(ROOT)): sha256(path) for path in SOURCE_FILES if path.exists()}


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def fmt_float(value: float) -> str:
    """固定小数格式。"""
    return f"{value:.12f}"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def pressure_rows(zero_sum: dict[str, Any], trivial: dict[str, Any]) -> list[dict[str, Any]]:
    """比较当前自足预算和 theta 目标。"""
    zero_pressure = zero_sum.get("pressure_rows", [{}])[0]
    static = trivial.get("static_formula_pressure", {})
    prime_power = trivial.get("prime_power_pressure", {})
    rows = [
        {
            "item": "target relative error",
            "value": TARGET_RELATIVE_ERROR,
            "beats_target": True,
            "meaning": "Dusart 目标所需相对误差。",
        },
        {
            "item": "strict zero-sum closed envelope at T0",
            "value": float(zero_pressure.get("closed_relative", math.inf)),
            "beats_target": float(zero_pressure.get("closed_relative", math.inf)) <= TARGET_RELATIVE_ERROR,
            "meaning": "当前内部零点自由区预算的保守相对包络。",
        },
        {
            "item": "static formula terms relative",
            "value": float(static.get("static_relative_to_x", math.inf)),
            "beats_target": float(static.get("static_relative_to_x", math.inf)) <= TARGET_RELATIVE_ERROR,
            "meaning": "公式常数和平凡零点项的相对压力。",
        },
        {
            "item": "prime-power transfer relative",
            "value": float(prime_power.get("relative_to_x", math.inf)),
            "beats_target": float(prime_power.get("relative_to_x", math.inf)) <= TARGET_RELATIVE_ERROR,
            "meaning": "锚点素数幂低阶项的相对压力。",
        },
    ]
    return rows


def build_rows(trivial: dict[str, Any], zero_sum: dict[str, Any], theta_external: dict[str, Any]) -> list[dict[str, Any]]:
    """生成 theta 目标判定表。"""
    guard = (
        trivial.get("counterexample_assumption_only") is True
        and trivial.get("direct_unconditional_contradiction_found") is False
        and trivial.get("row_column_unconditional_closed") is False
        and theta_external.get("row_column_unconditional_closed") is False
    )
    active = trivial.get("next_direct_attack_target") == OLD_ATOM
    trivial_ready = trivial.get("trivial_tail_prime_power_budget_self_contained_closed") is True
    external_match = theta_external.get("theta_target_external_closed") is True
    external_anchor_valid = ANCHOR_X > 0 and abs(TARGET_RELATIVE_ERROR - 1.0 / 36_260.0) < 1e-18
    pressure = pressure_rows(zero_sum, trivial)
    current_internal_sufficient = all(item["beats_target"] for item in pressure[1:])
    return [
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只补解析输入，不使用真实零行缺席或实验替代证明。",
            "保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。",
        ),
        row(
            "ThetaTargetGateActive",
            active,
            True,
            "平凡尾项 strict 同步后，下一最窄点正是 theta@20000 小误差目标。",
            OLD_ATOM,
        ),
        row(
            "StrictTrivialTailReady",
            trivial_ready,
            trivial_ready,
            "同口径初等尾项已 strict 自足归账，theta 目标可作为独立 Chebyshev 显式界输入处理。",
            "PerronTrivialZeroPrimePowerTailBudgetSelfContainedClosedElementaryXGe20000",
        ),
        row(
            "DusartExternalThetaTargetStrictlyMatches",
            external_match and external_anchor_valid,
            False,
            "外部 Dusart 命题给 vartheta(x)-x < x/36260；因 20000>0，形式上严格匹配本目标。",
            STRICT_EXTERNAL_CLOSED,
        ),
        row(
            "CurrentInternalZeroFreeBudgetBeatsThetaTarget",
            current_internal_sufficient,
            current_internal_sufficient,
            "当前自足 Perron/零点自由区常数不能达到 1/36260 级小误差，不能据此关闭 theta 目标。",
            SELF_INPUT,
        ),
        row(
            "ThetaTargetSelfContainedClosed",
            False,
            False,
            "严格自足线仍需文内 Dusart 型显式 theta 证明或可核验有限桥，不能由当前 C=1280 轮廓预算推出。",
            f"{SELF_INPUT} OR {FINITE_BRIDGE}",
        ),
        row(
            "ExternalRouteNextFiniteLowHeight",
            external_match and external_anchor_valid,
            False,
            "若接受外部 Dusart，则 theta 目标在外部路线上关闭，下一步进入低高度核验。",
            FINITE_LOW_HEIGHT,
        ),
        row(
            "SelfContainedMertensTailStillOpen",
            False,
            False,
            "自足 Mertens 尾段仍未闭合；theta 自足证明、低高度、有限桥和 B1 区间仍是独立输入。",
            MERTENS_TAIL,
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "本步不产生早期零行反例链与真实结构链的终端矛盾。",
            DSTRUCTURE,
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造证书对象。"""
    trivial = load_json(TRIVIAL_SYNC)
    zero_sum = load_json(ZERO_SUM_SYNC)
    theta_external = load_json(THETA_EXTERNAL)
    rows = build_rows(trivial, zero_sum, theta_external)
    external_closed = next(item["closed"] for item in rows if item["gate"] == "DusartExternalThetaTargetStrictlyMatches")
    internal_sufficient = next(item["closed"] for item in rows if item["gate"] == "CurrentInternalZeroFreeBudgetBeatsThetaTarget")
    return {
        "certificate_type": "prime_matrix_strict_theta_target_external_match_self_frontier_router",
        "status": "theta_target_external_strict_matched_self_contained_frontier_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "theta_target_external_strict_matched": external_closed,
        "current_internal_zero_free_budget_beats_theta_target": internal_sufficient,
        "theta_target_self_contained_closed": False,
        "self_contained_mertens_tail_closed": False,
        "b3_tv_strict_self_contained_closed": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "target_x": ANCHOR_X,
        "target_denominator": DENOMINATOR,
        "target_relative_error": TARGET_RELATIVE_ERROR,
        "replacement_external": {
            OLD_ATOM: STRICT_EXTERNAL_CLOSED,
        },
        "remaining_self_contained_after_theta_frontier": [
            SELF_INPUT,
            FINITE_LOW_HEIGHT,
            FINITE_BRIDGE,
            "SelfContainedMeisselMertensConstantIntervalLedgerAt20000",
        ],
        "next_direct_attack_target": FINITE_LOW_HEIGHT,
        "parallel_self_contained_attack_target": SELF_INPUT,
        "source_hashes": source_hashes(),
        "pressure_rows": pressure_rows(zero_sum, trivial),
        "plain_conclusion": (
            "`ThetaEnvelopeTargetAt20000NumericalBudgetLedger` 在外部路线上可严格匹配 Dusart `x/36260` 界关闭；"
            "但当前自足零点自由区/Perron 常数远不足以推出该小误差，严格自足线仍必须另证 "
            "`InternalDusartThetaEnvelopeProofLedger` 或有限 theta 桥。"
            "该步不关闭自足 Mertens 尾段，也不关闭行/列无条件命题。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    replacement = next(iter(result["replacement_external"].items()))
    lines = [
        "# Prime Matrix strict theta@20000 外部匹配与自足前沿路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"theta_target_external_strict_matched={fmt_bool(result['theta_target_external_strict_matched'])}",
        f"current_internal_zero_free_budget_beats_theta_target={fmt_bool(result['current_internal_zero_free_budget_beats_theta_target'])}",
        f"theta_target_self_contained_closed={fmt_bool(result['theta_target_self_contained_closed'])}",
        f"self_contained_mertens_tail_closed={fmt_bool(result['self_contained_mertens_tail_closed'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 外部替换",
        "",
        "```text",
        replacement[0],
        f"  => {replacement[1]}",
        "```",
        "",
        "## 2. 目标压力",
        "",
        "| item | value | beats target | meaning |",
        "| --- | ---: | --- | --- |",
    ]
    for item in result["pressure_rows"]:
        lines.append(
            "| {item} | `{value}` | `{beats}` | {meaning} |".format(
                item=table_cell(item["item"]),
                value=fmt_float(float(item["value"])),
                beats=fmt_bool(item["beats_target"]),
                meaning=table_cell(item["meaning"]),
            )
        )
    lines.extend(
        [
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
            "自足并行目标：",
            "",
            "```text",
            result["parallel_self_contained_attack_target"],
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
