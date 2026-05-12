#!/usr/bin/env python3
"""生成 strict post-Meissel 当前前沿同步路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_post_meissel_frontier_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-post-meissel-frontier-sync-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"

OUT_JSON = MONOGRAPH / "prime-matrix-strict-post-meissel-frontier-sync-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-post-meissel-frontier-sync-router.md"

UNSMOOTHED_JSON = MONOGRAPH / "prime-matrix-strict-unsmoothed-perron-final-sync-router.json"
ZERO_SUM_JSON = MONOGRAPH / "prime-matrix-strict-zero-sum-contour-self-contained-sync-router.json"
TRIVIAL_JSON = MONOGRAPH / "prime-matrix-strict-trivial-tail-prime-power-self-contained-sync-router.json"
THETA_TARGET_JSON = MONOGRAPH / "prime-matrix-strict-theta-target-external-match-self-frontier-router.json"
LOW_HEIGHT_JSON = MONOGRAPH / "prime-matrix-strict-finite-low-height-external-match-router.json"
GLOBAL_THETA_JSON = MONOGRAPH / "prime-matrix-strict-global-theta-envelope-external-match-router.json"
MEISSEL_JSON = MONOGRAPH / "prime-matrix-strict-meissel-mertens-external-match-router.json"
CLAIM_STATUS = MONOGRAPH / "claim-status-table.md"

SOURCE_FILES = [
    UNSMOOTHED_JSON,
    ZERO_SUM_JSON,
    TRIVIAL_JSON,
    THETA_TARGET_JSON,
    LOW_HEIGHT_JSON,
    GLOBAL_THETA_JSON,
    MEISSEL_JSON,
    CLAIM_STATUS,
]

DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
INTERNAL_DUSART_THETA = "InternalDusartThetaEnvelopeProofLedger"
CRITICAL_LINE_LOW = "CriticalLineNoZeroOn0To14FiniteLedger"
CRITICAL_STRIP_LOW = "CriticalStripNoOffLineZeroBelow14TuringLedger"
INTERNAL_CONTOUR = "InternalZeroFreeRegionToThetaContourEnvelopeLedger"
INTERNAL_BRIDGE = "InternalFiniteThetaEnvelopeBridgeHashLedger"
SELF_B1 = "SelfContainedMeisselMertensB1IntervalArithmeticLedger"
SELF_RECIPROCAL = "SelfContainedDusartReciprocalPrimeProofAppendixXGe10372"


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


def lane_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """生成当前双路线前沿判定表。"""
    unsmoothed = data["unsmoothed"]
    zero_sum = data["zero_sum"]
    trivial = data["trivial"]
    theta = data["theta"]
    low = data["low"]
    global_theta = data["global_theta"]
    meissel = data["meissel"]
    guard = all(
        item.get("counterexample_assumption_only") is True
        and item.get("direct_unconditional_contradiction_found") is False
        and item.get("row_column_unconditional_closed") is False
        for item in data.values()
    )
    self_core_closed = (
        unsmoothed.get("unsmoothed_perron_strict_self_contained_closed") is True
        and zero_sum.get("zero_sum_contour_budget_self_contained_closed") is True
        and trivial.get("trivial_tail_prime_power_budget_self_contained_closed") is True
    )
    external_theta_lane_closed = (
        theta.get("theta_target_external_strict_matched") is True
        and low.get("finite_low_height_strict_external_matched") is True
        and global_theta.get("explicit_psi_theta_contour_envelope_strict_external_closed") is True
        and global_theta.get("finite_theta_bridge_strict_external_closed") is True
    )
    strict_theta_self_open = (
        theta.get("theta_target_self_contained_closed") is False
        and low.get("finite_low_height_self_contained_closed") is False
        and global_theta.get("explicit_psi_theta_contour_envelope_self_contained_closed") is False
        and global_theta.get("finite_theta_bridge_self_contained_closed") is False
    )
    meissel_external = meissel.get("meissel_mertens_strict_external_matched") is True
    meissel_self_open = (
        meissel.get("meissel_mertens_interval_self_contained_closed") is False
        and meissel.get("self_contained_mertens_tail_closed") is False
    )
    external_at_gate = (
        meissel.get("external_b3_chain_reaches_dstructure_gate") is True
        and meissel.get("next_direct_attack_target") == DSTRUCTURE
    )
    dstructure_absent = meissel.get("dstructure_independent_acceptance_present") is False
    return [
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "所有输入仍处于早期零行反例假设链审查，不使用真实零行缺席。",
            "保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。",
        ),
        row(
            "StrictSelfContainedAnalyticCoreClosed",
            self_core_closed,
            True,
            "非平滑 Perron 常数、高高度零点和预算、平凡零点/素数幂尾项已在 strict 自足线上闭合。",
            "不包含 theta@20000、低高度 Turing、有限桥和 B1 区间。",
        ),
        row(
            "ExternalThetaLowHeightBridgeLaneClosed",
            external_theta_lane_closed,
            False,
            "theta@20000、低高度零点、theta contour 与有限桥已由外部 Dusart/低高度证书严格匹配。",
            "对应自足证明仍开放。",
        ),
        row(
            "StrictThetaLowHeightContourSelfContainedStillOpen",
            strict_theta_self_open,
            False,
            "内部 Dusart theta、低高度 Turing、内部 contour 和有限桥尚未自足闭合。",
            f"{INTERNAL_DUSART_THETA} AND {CRITICAL_LINE_LOW} AND {CRITICAL_STRIP_LOW} AND {INTERNAL_CONTOUR} AND {INTERNAL_BRIDGE}",
        ),
        row(
            "StrictMeisselMertensExternalMatched",
            meissel_external,
            False,
            "Meissel-Mertens B1 区间已严格对接旧 B3/Dusart 外部证书。",
            "外部匹配不是自足 B1 证明。",
        ),
        row(
            "StrictMeisselMertensSelfContainedStillOpen",
            meissel_self_open,
            False,
            "B1 区间算术和 reciprocal-prime Mertens 尾段仍未在文内自足证明。",
            f"{SELF_B1} AND {SELF_RECIPROCAL}",
        ),
        row(
            "ExternalB3MertensChainAtDStructureGate",
            external_at_gate,
            False,
            "外部 B3/Mertens 解析链当前已经到达 DStructure/Rankin 独立验收门。",
            DSTRUCTURE,
        ),
        row(
            "DStructureIndependentAcceptanceAbsent",
            dstructure_absent,
            True,
            "独立验收事件缺席；作者侧外部匹配不能替代最终守门项。",
            DSTRUCTURE,
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "当前 post-Meissel 前沿仍不是行/列命题无条件闭合。",
            "必须补自足输入或独立验收 DStructure/Rankin。",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 post-Meissel 前沿同步证书。"""
    data = {
        "unsmoothed": load_json(UNSMOOTHED_JSON),
        "zero_sum": load_json(ZERO_SUM_JSON),
        "trivial": load_json(TRIVIAL_JSON),
        "theta": load_json(THETA_TARGET_JSON),
        "low": load_json(LOW_HEIGHT_JSON),
        "global_theta": load_json(GLOBAL_THETA_JSON),
        "meissel": load_json(MEISSEL_JSON),
    }
    rows = lane_rows(data)
    self_contained_open = [
        INTERNAL_DUSART_THETA,
        CRITICAL_LINE_LOW,
        CRITICAL_STRIP_LOW,
        INTERNAL_CONTOUR,
        INTERNAL_BRIDGE,
        SELF_B1,
        SELF_RECIPROCAL,
    ]
    return {
        "certificate_type": "prime_matrix_strict_post_meissel_frontier_sync_router",
        "status": "post_meissel_frontier_synced_external_at_dstructure_self_contained_inputs_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "strict_self_contained_analytic_core_closed": next(
            item["closed"] for item in rows if item["gate"] == "StrictSelfContainedAnalyticCoreClosed"
        ),
        "external_theta_low_height_bridge_lane_closed": next(
            item["closed"] for item in rows if item["gate"] == "ExternalThetaLowHeightBridgeLaneClosed"
        ),
        "meissel_mertens_strict_external_matched": data["meissel"].get("meissel_mertens_strict_external_matched") is True,
        "external_b3_chain_reaches_dstructure_gate": data["meissel"].get("external_b3_chain_reaches_dstructure_gate") is True,
        "dstructure_independent_acceptance_present": False,
        "self_contained_mertens_tail_closed": False,
        "b3_tv_strict_self_contained_closed": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "external_next_direct_attack_target": DSTRUCTURE,
        "strict_self_contained_next_direct_attack_target": INTERNAL_DUSART_THETA,
        "remaining_self_contained_inputs": self_contained_open,
        "frontier_rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "post-Meissel 前沿已经分成两条清楚路线：外部路线中，theta/低高度/contour/有限桥/"
            "Meissel-Mertens 都已严格匹配，B3/Mertens 解析链到达 DStructure/Rankin 独立验收门；"
            "严格自足路线中，Perron 常数、零点和预算和平凡尾项已闭合，但内部 Dusart theta、"
            "低高度 Turing、内部 contour、有限桥、B1 区间与 reciprocal-prime Mertens 尾段仍开放。"
            "因此下一步不能宣称行列无条件闭合；最窄选择是外部验收 DStructure/Rankin，或自足线先攻 "
            "`InternalDusartThetaEnvelopeProofLedger`。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict post-Meissel 前沿同步路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"strict_self_contained_analytic_core_closed={fmt_bool(result['strict_self_contained_analytic_core_closed'])}",
        f"external_theta_low_height_bridge_lane_closed={fmt_bool(result['external_theta_low_height_bridge_lane_closed'])}",
        f"meissel_mertens_strict_external_matched={fmt_bool(result['meissel_mertens_strict_external_matched'])}",
        f"external_b3_chain_reaches_dstructure_gate={fmt_bool(result['external_b3_chain_reaches_dstructure_gate'])}",
        f"dstructure_independent_acceptance_present={fmt_bool(result['dstructure_independent_acceptance_present'])}",
        f"self_contained_mertens_tail_closed={fmt_bool(result['self_contained_mertens_tail_closed'])}",
        f"b3_tv_strict_self_contained_closed={fmt_bool(result['b3_tv_strict_self_contained_closed'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in result["frontier_rows"]:
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
            "## 2. 下一步",
            "",
            "外部路线：",
            "",
            "```text",
            result["external_next_direct_attack_target"],
            "```",
            "",
            "严格自足路线：",
            "",
            "```text",
            result["strict_self_contained_next_direct_attack_target"],
            "```",
            "",
            "仍开放的自足输入：",
            "",
            "```text",
            " AND ".join(result["remaining_self_contained_inputs"]),
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
    print("external_next_direct_attack_target=", result["external_next_direct_attack_target"])
    print("strict_self_contained_next_direct_attack_target=", result["strict_self_contained_next_direct_attack_target"])


if __name__ == "__main__":
    main()
