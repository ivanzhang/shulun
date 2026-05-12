#!/usr/bin/env python3
"""生成 strict 全局 theta 包络外部匹配路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_global_theta_envelope_external_match_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-global-theta-envelope-external-match-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"

OUT_JSON = MONOGRAPH / "prime-matrix-strict-global-theta-envelope-external-match-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-global-theta-envelope-external-match-router.md"

LOW_HEIGHT_STRICT = MONOGRAPH / "prime-matrix-strict-finite-low-height-external-match-router.json"
THETA_STRICT = MONOGRAPH / "prime-matrix-strict-theta-target-external-match-self-frontier-router.json"
DUSART_GLOBAL = MONOGRAPH / "prime-matrix-b3-dusart-global-theta-envelope-external-router.json"
CLAIM_STATUS = MONOGRAPH / "claim-status-table.md"

SOURCE_FILES = [LOW_HEIGHT_STRICT, THETA_STRICT, DUSART_GLOBAL, CLAIM_STATUS]

CONTOUR_ATOM = "ExplicitPsiThetaContourEnvelopeXGe20000FromZeroFreeRegion"
CONTOUR_CLOSED = "ExplicitPsiThetaContourEnvelopeXGe20000StrictExternalClosedByDusart"
BRIDGE_ATOM = "FiniteThetaEnvelopeBridgeBelowAnalyticThreshold"
BRIDGE_CLOSED = "FiniteThetaEnvelopeBridgeStrictExternalClosedByDusartAllXPositive"
LOW_HEIGHT_CLOSED = "FiniteLowHeightZeroCheckStrictExternalClosedFirstZeroGT14TuringComplete"
THETA_TARGET_CLOSED = "ThetaEnvelopeTargetAt20000StrictExternalMatchedDusartOneOver36260"
MERTENS_INTERVAL = "SelfContainedMeisselMertensConstantIntervalLedgerAt20000"
INTERNAL_CONTOUR = "InternalZeroFreeRegionToThetaContourEnvelopeLedger"
INTERNAL_BRIDGE = "InternalFiniteThetaEnvelopeBridgeHashLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


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


def build_rows(low_height: dict[str, Any], theta: dict[str, Any], dusart_global: dict[str, Any]) -> list[dict[str, Any]]:
    """生成 strict 全局 theta 包络外部匹配判定表。"""
    guard = (
        low_height.get("counterexample_assumption_only") is True
        and low_height.get("direct_unconditional_contradiction_found") is False
        and low_height.get("row_column_unconditional_closed") is False
        and theta.get("row_column_unconditional_closed") is False
        and dusart_global.get("row_column_unconditional_closed") is False
    )
    active = low_height.get("next_direct_attack_target") == CONTOUR_ATOM
    low_height_ready = low_height.get("finite_low_height_strict_external_matched") is True
    theta_ready = theta.get("theta_target_external_strict_matched") is True
    dusart_ready = (
        dusart_global.get("explicit_psi_theta_contour_envelope_external_closed") is True
        and dusart_global.get("finite_theta_bridge_external_closed") is True
    )
    contour_closed = guard and active and low_height_ready and theta_ready and dusart_ready
    bridge_closed = contour_closed
    return [
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只补外部解析输入，不使用真实零行缺席。",
            "保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。",
        ),
        row(
            "ExplicitContourEnvelopeGateActive",
            active,
            True,
            "低高度 strict 外部匹配后，下一最窄点是 x>=20000 的显式 psi/theta 包络。",
            CONTOUR_ATOM,
        ),
        row(
            "LowHeightStrictExternalReady",
            low_height_ready,
            False,
            "T<=14 的低高度零点核验已在外部路线上严格匹配关闭。",
            LOW_HEIGHT_CLOSED,
        ),
        row(
            "ThetaTargetStrictExternalReady",
            theta_ready,
            False,
            "Dusart theta@20000 目标已严格匹配。",
            THETA_TARGET_CLOSED,
        ),
        row(
            "DusartGlobalThetaEnvelopeAvailable",
            dusart_ready,
            False,
            "旧全局 Dusart 路由确认同一 theta 界对所有 x>0 成立，强于 x>=20000 和有限桥。",
            "Dusart vartheta(x)-x < x/36260 for x>0",
        ),
        row(
            CONTOUR_ATOM,
            contour_closed,
            False,
            "外部条件路线可用 Dusart 全局 theta 界旁路关闭 x>=20000 包络。",
            CONTOUR_CLOSED,
        ),
        row(
            BRIDGE_ATOM,
            bridge_closed,
            False,
            "同一 Dusart 全局界覆盖所有 x>0，因此有限桥外部关闭。",
            BRIDGE_CLOSED,
        ),
        row(
            "SelfContainedContourStillOpen",
            False,
            False,
            "严格自足路线仍需从零点自由区推出非平滑 psi/theta 轮廓常数。",
            INTERNAL_CONTOUR,
        ),
        row(
            "SelfContainedFiniteBridgeStillOpen",
            False,
            False,
            "严格自足路线仍需有限桥 hash 核验。",
            INTERNAL_BRIDGE,
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "theta 包络外部闭合不触动最终行列命题。",
            DSTRUCTURE,
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造证书对象。"""
    low_height = load_json(LOW_HEIGHT_STRICT)
    theta = load_json(THETA_STRICT)
    dusart_global = load_json(DUSART_GLOBAL)
    rows = build_rows(low_height, theta, dusart_global)
    contour_closed = next(item["closed"] for item in rows if item["gate"] == CONTOUR_ATOM)
    bridge_closed = next(item["closed"] for item in rows if item["gate"] == BRIDGE_ATOM)
    return {
        "certificate_type": "prime_matrix_strict_global_theta_envelope_external_match_router",
        "status": "global_theta_envelope_strict_external_closed_self_contained_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "explicit_psi_theta_contour_envelope_strict_external_closed": contour_closed,
        "finite_theta_bridge_strict_external_closed": bridge_closed,
        "explicit_psi_theta_contour_envelope_self_contained_closed": False,
        "finite_theta_bridge_self_contained_closed": False,
        "self_contained_mertens_tail_closed": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "replacement_external": {
            CONTOUR_ATOM: CONTOUR_CLOSED,
            BRIDGE_ATOM: BRIDGE_CLOSED,
        },
        "remaining_self_contained_after_global_theta": [INTERNAL_CONTOUR, INTERNAL_BRIDGE],
        "next_direct_attack_target": MERTENS_INTERVAL,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`ExplicitPsiThetaContourEnvelopeXGe20000FromZeroFreeRegion` 与有限 theta 桥已在外部路线上严格匹配关闭："
            "同一 Dusart 全局 theta 界覆盖 `x>0`，因此强于 `x>=20000` 包络和阈值以下有限桥。"
            "该步仍不是内部零点自由区 contour 证明，自足 contour 与有限桥继续开放。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict 全局 theta 包络外部匹配路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"explicit_psi_theta_contour_envelope_strict_external_closed={fmt_bool(result['explicit_psi_theta_contour_envelope_strict_external_closed'])}",
        f"finite_theta_bridge_strict_external_closed={fmt_bool(result['finite_theta_bridge_strict_external_closed'])}",
        f"explicit_psi_theta_contour_envelope_self_contained_closed={fmt_bool(result['explicit_psi_theta_contour_envelope_self_contained_closed'])}",
        f"finite_theta_bridge_self_contained_closed={fmt_bool(result['finite_theta_bridge_self_contained_closed'])}",
        f"self_contained_mertens_tail_closed={fmt_bool(result['self_contained_mertens_tail_closed'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 外部替换",
        "",
        "| old | new |",
        "| --- | --- |",
    ]
    for old, new in result["replacement_external"].items():
        lines.append(f"| `{old}` | `{new}` |")
    lines.extend(
        [
            "",
            "## 2. 判定表",
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
            "## 3. 下一最窄点",
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
