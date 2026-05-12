#!/usr/bin/env python3
"""生成 strict post-finite-theta 当前前沿同步路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_post_finite_theta_frontier_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-post-finite-theta-frontier-sync-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"

OUT_JSON = MONOGRAPH / "prime-matrix-strict-post-finite-theta-frontier-sync-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-post-finite-theta-frontier-sync-router.md"

FINITE_THETA = MONOGRAPH / "prime-matrix-strict-finite-theta-bridge-self-contained-router.json"
LOW_HEIGHT = MONOGRAPH / "prime-matrix-strict-finite-low-height-external-match-router.json"
MEISSEL = MONOGRAPH / "prime-matrix-strict-meissel-mertens-external-match-router.json"
CLAIM_STATUS = MONOGRAPH / "claim-status-table.md"

SOURCE_FILES = [FINITE_THETA, LOW_HEIGHT, MEISSEL, CLAIM_STATUS]

INTERNAL_CONTOUR = "InternalZeroFreeRegionToThetaContourEnvelopeLedger"
LOW_HEIGHT_SELF = "CriticalLineNoZeroOn0To14FiniteLedger AND CriticalStripNoOffLineZeroBelow14TuringLedger"
SELF_B1 = "SelfContainedMeisselMertensB1IntervalArithmeticLedger"
SELF_RECIPROCAL = "SelfContainedDusartReciprocalPrimeProofAppendixXGe10372"
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


def build_rows(finite: dict[str, Any], low: dict[str, Any], meissel: dict[str, Any]) -> list[dict[str, Any]]:
    """生成 post-finite-theta 前沿判定表。"""
    guard = (
        finite.get("counterexample_assumption_only") is True
        and finite.get("direct_unconditional_contradiction_found") is False
        and finite.get("row_column_unconditional_closed") is False
        and meissel.get("row_column_unconditional_closed") is False
    )
    finite_closed = (
        finite.get("theta_target_at_20000_self_contained_closed") is True
        and finite.get("finite_theta_bridge_below_20000_self_contained_closed") is True
    )
    contour_open = finite.get("internal_zero_free_region_to_theta_contour_closed") is False
    low_external = low.get("finite_low_height_strict_external_matched") is True
    low_self_open = low.get("finite_low_height_self_contained_closed") is False
    meissel_external = meissel.get("meissel_mertens_strict_external_matched") is True
    meissel_self_open = meissel.get("meissel_mertens_interval_self_contained_closed") is False
    external_at_gate = meissel.get("external_b3_chain_reaches_dstructure_gate") is True
    return [
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步只同步已关闭输入和剩余输入，不使用真实零行缺席。",
            "保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。",
        ),
        row(
            "FiniteThetaAnchorAndBridgeSelfContainedClosed",
            finite_closed,
            True,
            "theta@20000 锚点和 0<x<=20000 有限桥已经由素数 log 有限证书自足关闭。",
            "从自足剩余中移除 theta@20000 与有限桥。",
        ),
        row(
            "InternalThetaContourStillOpen",
            contour_open,
            False,
            "x>=20000 的内部 theta/PNT contour 包络仍未关闭，是新的自足主攻点。",
            INTERNAL_CONTOUR,
        ),
        row(
            "LowHeightExternalOnly",
            low_external and low_self_open,
            False,
            "低高度零点核验已有外部匹配，但文内 Turing/无零证明仍开放。",
            LOW_HEIGHT_SELF,
        ),
        row(
            "MeisselExternalOnly",
            meissel_external and meissel_self_open,
            False,
            "Meissel-Mertens 外部匹配已到位，但 B1 区间和 reciprocal-prime 尾段仍非自足。",
            f"{SELF_B1} AND {SELF_RECIPROCAL}",
        ),
        row(
            "ExternalB3ChainAtDStructureGate",
            external_at_gate,
            False,
            "外部条件链仍停在 DStructure/Rankin 独立验收门。",
            DSTRUCTURE,
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "有限 theta 桥同步后，行/列无条件命题仍未闭合。",
            DSTRUCTURE,
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 post-finite-theta 前沿同步证书。"""
    finite = load_json(FINITE_THETA)
    low = load_json(LOW_HEIGHT)
    meissel = load_json(MEISSEL)
    rows = build_rows(finite, low, meissel)
    remaining = [INTERNAL_CONTOUR, LOW_HEIGHT_SELF, SELF_B1, SELF_RECIPROCAL]
    return {
        "certificate_type": "prime_matrix_strict_post_finite_theta_frontier_sync_router",
        "status": "post_finite_theta_frontier_synced_next_internal_contour",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "finite_theta_anchor_and_bridge_self_contained_closed": next(
            item["closed"] for item in rows if item["gate"] == "FiniteThetaAnchorAndBridgeSelfContainedClosed"
        ),
        "internal_zero_free_region_to_theta_contour_closed": False,
        "finite_low_height_self_contained_closed": False,
        "meissel_mertens_interval_self_contained_closed": False,
        "self_contained_mertens_tail_closed": False,
        "b3_tv_strict_self_contained_closed": False,
        "external_b3_chain_reaches_dstructure_gate": meissel.get("external_b3_chain_reaches_dstructure_gate") is True,
        "dstructure_independent_acceptance_present": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": INTERNAL_CONTOUR,
        "remaining_self_contained_inputs": remaining,
        "frontier_rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "有限 theta 桥闭合后，严格自足解析线的 theta@20000 锚点和阈值以下有限桥已移出剩余。"
            "新的自足最窄点是 `InternalZeroFreeRegionToThetaContourEnvelopeLedger`，即 `x>=20000` 的内部 "
            "theta/PNT contour 包络；并行仍需低高度 Turing/无零证明、B1 区间和 reciprocal-prime Mertens 尾段。"
            "外部路线仍在 DStructure/Rankin 独立验收门，不能据此宣布行列无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict post-finite-theta 前沿同步路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"finite_theta_anchor_and_bridge_self_contained_closed={fmt_bool(result['finite_theta_anchor_and_bridge_self_contained_closed'])}",
        f"internal_zero_free_region_to_theta_contour_closed={fmt_bool(result['internal_zero_free_region_to_theta_contour_closed'])}",
        f"finite_low_height_self_contained_closed={fmt_bool(result['finite_low_height_self_contained_closed'])}",
        f"meissel_mertens_interval_self_contained_closed={fmt_bool(result['meissel_mertens_interval_self_contained_closed'])}",
        f"self_contained_mertens_tail_closed={fmt_bool(result['self_contained_mertens_tail_closed'])}",
        f"b3_tv_strict_self_contained_closed={fmt_bool(result['b3_tv_strict_self_contained_closed'])}",
        f"external_b3_chain_reaches_dstructure_gate={fmt_bool(result['external_b3_chain_reaches_dstructure_gate'])}",
        f"dstructure_independent_acceptance_present={fmt_bool(result['dstructure_independent_acceptance_present'])}",
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
            "## 2. 下一最窄点",
            "",
            "```text",
            result["next_direct_attack_target"],
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
    print("next_direct_attack_target=", result["next_direct_attack_target"])


if __name__ == "__main__":
    main()
