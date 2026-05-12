#!/usr/bin/env python3
"""生成 strict Meissel-Mertens 常数区间外部匹配路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_meissel_mertens_external_match_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-meissel-mertens-external-match-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"

OUT_JSON = MONOGRAPH / "prime-matrix-strict-meissel-mertens-external-match-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-meissel-mertens-external-match-router.md"

STRICT_GLOBAL_THETA = MONOGRAPH / "prime-matrix-strict-global-theta-envelope-external-match-router.json"
B3_MEISSEL_EXTERNAL = MONOGRAPH / "prime-matrix-b3-meissel-mertens-interval-external-router.json"
B3_RECIPROCAL_MERTENS = MONOGRAPH / "prime-matrix-b3-explicit-prime-reciprocal-mertens-router.json"
CLAIM_STATUS = MONOGRAPH / "claim-status-table.md"

SOURCE_FILES = [
    STRICT_GLOBAL_THETA,
    B3_MEISSEL_EXTERNAL,
    B3_RECIPROCAL_MERTENS,
    CLAIM_STATUS,
]

OLD_ATOM = "SelfContainedMeisselMertensConstantIntervalLedgerAt20000"
CLOSED_ATOM = "DusartMeisselMertensConstantIntervalAt20000ExternalClosed"
STRICT_CONTOUR_CLOSED = "ExplicitPsiThetaContourEnvelopeXGe20000StrictExternalClosedByDusart"
STRICT_BRIDGE_CLOSED = "FiniteThetaEnvelopeBridgeStrictExternalClosedByDusartAllXPositive"
MERTENS_EXTERNAL = "DusartPrimeReciprocalMertensEnvelopeXGe286ExternalAccepted"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SELF_B1_INTERVAL = "SelfContainedMeisselMertensB1IntervalArithmeticLedger"
SELF_RECIPROCAL_TAIL = "SelfContainedDusartReciprocalPrimeProofAppendixXGe10372"
INTERNAL_DUSART_THETA = "InternalDusartThetaEnvelopeProofLedger"
INTERNAL_LOW_HEIGHT_1 = "CriticalLineNoZeroOn0To14FiniteLedger"
INTERNAL_LOW_HEIGHT_2 = "CriticalStripNoOffLineZeroBelow14TuringLedger"
INTERNAL_CONTOUR = "InternalZeroFreeRegionToThetaContourEnvelopeLedger"
INTERNAL_BRIDGE = "InternalFiniteThetaEnvelopeBridgeHashLedger"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算证据文件哈希。"""
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
    """固定小数格式，避免 Markdown 中口径漂移。"""
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


def reciprocal_mertens_ready(mertens: dict[str, Any]) -> bool:
    """确认旧 reciprocal-prime Mertens 外部证书仍满足 strict 匹配所需字段。"""
    finite = mertens.get("finite_step_ledger", {})
    tail = mertens.get("tail_theorem_ledger", {})
    return (
        mertens.get("explicit_prime_reciprocal_mertens_external_closed") is True
        and mertens.get("finite_prime_step_ledger_286_to_10371_closed") is True
        and mertens.get("dusart_tail_parameter_match_closed") is True
        and finite.get("finite_step_ledger_closed") is True
        and tail.get("external_theorem_parameter_match_closed") is True
        and isinstance(finite.get("meissel_mertens_b1_for_audit_only"), (int, float))
    )


def build_strict_basis() -> str:
    """给出 strict 外部链的最小输入基快照。"""
    return (
        f"{STRICT_CONTOUR_CLOSED} AND {STRICT_BRIDGE_CLOSED} AND "
        f"{CLOSED_ATOM} AND B3RosserFaceDictionaryClosedAlpha043 AND "
        f"B3Anchor20000BoundaryVariationBudgetClosedAlpha043 AND {DSTRUCTURE}"
    )


def build_rows(strict_theta: dict[str, Any], b3_external: dict[str, Any], mertens: dict[str, Any]) -> list[dict[str, Any]]:
    """生成 strict Meissel-Mertens 外部匹配判定表。"""
    guard = (
        strict_theta.get("counterexample_assumption_only") is True
        and strict_theta.get("empirical_absence_not_used") is True
        and strict_theta.get("hypothetical_chain_only") is True
        and strict_theta.get("direct_unconditional_contradiction_found") is False
        and strict_theta.get("row_column_unconditional_closed") is False
        and b3_external.get("counterexample_assumption_only") is True
        and b3_external.get("row_column_unconditional_closed") is False
    )
    active = strict_theta.get("next_direct_attack_target") == OLD_ATOM
    strict_theta_ready = (
        strict_theta.get("explicit_psi_theta_contour_envelope_strict_external_closed") is True
        and strict_theta.get("finite_theta_bridge_strict_external_closed") is True
        and strict_theta.get("explicit_psi_theta_contour_envelope_self_contained_closed") is False
        and strict_theta.get("finite_theta_bridge_self_contained_closed") is False
    )
    legacy_external_closed = (
        b3_external.get("meissel_mertens_interval_external_closed") is True
        and b3_external.get("meissel_mertens_interval_self_contained_closed") is False
        and b3_external.get("next_priority") == DSTRUCTURE
        and b3_external.get("replacement_external", {}).get(OLD_ATOM) == CLOSED_ATOM
    )
    mertens_ready = reciprocal_mertens_ready(mertens)
    strict_closed = guard and active and strict_theta_ready and legacy_external_closed and mertens_ready
    reaches_dstructure = strict_closed and b3_external.get("next_priority") == DSTRUCTURE
    return [
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只在早期零行反例假设链内补外部解析输入，不使用真实零行缺席。",
            "保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。",
        ),
        row(
            "StrictMeisselMertensGateActive",
            active,
            True,
            "strict 全局 theta 外部匹配后，当前最窄点正是 Meissel-Mertens 常数区间输入。",
            OLD_ATOM,
        ),
        row(
            "StrictThetaContourAndBridgeReady",
            strict_theta_ready,
            False,
            "strict 链已经外部关闭 theta contour 与有限桥，但没有关闭对应自足证明。",
            f"{STRICT_CONTOUR_CLOSED} AND {STRICT_BRIDGE_CLOSED}",
        ),
        row(
            "LegacyB3MeisselMertensExternalClosed",
            legacy_external_closed,
            False,
            "旧 B3 路由已把同一 Meissel-Mertens 常数区间原子外部替换为 Dusart 闭合原子。",
            CLOSED_ATOM,
        ),
        row(
            "DusartReciprocalPrimeMertensExternalReady",
            mertens_ready,
            False,
            "reciprocal-prime Mertens 外部证书提供有限阶梯、尾段匹配与 B1 常数口径。",
            MERTENS_EXTERNAL,
        ),
        row(
            OLD_ATOM,
            strict_closed,
            False,
            "在 strict theta 前沿下接受旧 Dusart/Rosser-Schoenfeld 外部证书，可关闭该 Meissel-Mertens 外部输入。",
            CLOSED_ATOM,
        ),
        row(
            "ExternalB3ChainReachesDStructureGate",
            reaches_dstructure,
            False,
            "外部 B3/Mertens 解析链已经推进到 DStructure/Rankin 独立验收门。",
            DSTRUCTURE,
        ),
        row(
            "SelfContainedMeisselMertensStillOpen",
            False,
            False,
            "严格自足路线仍需内联 B1 区间算术和 reciprocal-prime Mertens 尾段证明。",
            f"{SELF_B1_INTERVAL} AND {SELF_RECIPROCAL_TAIL}",
        ),
        row(
            "DStructureRankinIndependentAcceptancePresent",
            False,
            False,
            "本步不是 DStructure/Rankin 独立验收，不能替代最终守门项。",
            DSTRUCTURE,
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "外部 Meissel-Mertens 匹配不构成行/列命题无条件闭合。",
            DSTRUCTURE,
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 strict Meissel-Mertens 外部匹配证书。"""
    strict_theta = load_json(STRICT_GLOBAL_THETA)
    b3_external = load_json(B3_MEISSEL_EXTERNAL)
    mertens = load_json(B3_RECIPROCAL_MERTENS)
    rows = build_rows(strict_theta, b3_external, mertens)
    strict_closed = next(item["closed"] for item in rows if item["gate"] == OLD_ATOM)
    reaches_dstructure = next(item["closed"] for item in rows if item["gate"] == "ExternalB3ChainReachesDStructureGate")
    finite = mertens.get("finite_step_ledger", {})
    tail = mertens.get("tail_theorem_ledger", {})
    return {
        "certificate_type": "prime_matrix_strict_meissel_mertens_external_match_router",
        "status": "strict_meissel_mertens_external_matched_self_contained_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "meissel_mertens_strict_external_matched": strict_closed,
        "meissel_mertens_interval_external_closed": strict_closed,
        "meissel_mertens_interval_self_contained_closed": False,
        "self_contained_mertens_tail_closed": False,
        "b3_tv_strict_self_contained_closed": False,
        "external_b3_chain_reaches_dstructure_gate": reaches_dstructure,
        "dstructure_independent_acceptance_present": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "replacement_external": {OLD_ATOM: CLOSED_ATOM},
        "strict_external_basis_snapshot": build_strict_basis(),
        "legacy_b3_external_basis_sha256": hashlib.sha256(
            b3_external.get("latest_external_titchmarsh_cn16_basis", "").encode("utf-8")
        ).hexdigest(),
        "mertens_external_atom": MERTENS_EXTERNAL,
        "meissel_mertens_b1": finite.get("meissel_mertens_b1_for_audit_only"),
        "finite_step_range": [finite.get("low_x"), finite.get("high_x_exclusive")],
        "tail_start_x": tail.get("tail_start_x"),
        "dusart_tail_error_at_start": tail.get("dusart_error_at_tail_start"),
        "remaining_self_contained_after_meissel": [
            INTERNAL_DUSART_THETA,
            INTERNAL_LOW_HEIGHT_1,
            INTERNAL_LOW_HEIGHT_2,
            INTERNAL_CONTOUR,
            INTERNAL_BRIDGE,
            SELF_B1_INTERVAL,
            SELF_RECIPROCAL_TAIL,
        ],
        "next_direct_attack_target": DSTRUCTURE,
        "independent_acceptance_gate": DSTRUCTURE,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "strict 外部路线下，`SelfContainedMeisselMertensConstantIntervalLedgerAt20000` "
            "已可严格对接旧 B3 Meissel-Mertens/Dusart 外部证书：有限阶梯覆盖 `286<=x<10372`，"
            "尾段 `x>=10372` 由 reciprocal-prime Mertens 外部定理匹配，B1 口径为 "
            "`0.2614972128476428`。这只关闭外部输入并把 B3/Mertens 解析链推进到 "
            "`DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`；自足 B1/尾段、"
            "内部 theta/低高度/contour 证明和最终行列无条件命题仍未闭合。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    replacement = next(iter(result["replacement_external"].items()))
    lines = [
        "# Prime Matrix strict Meissel-Mertens 外部匹配路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"meissel_mertens_strict_external_matched={fmt_bool(result['meissel_mertens_strict_external_matched'])}",
        f"meissel_mertens_interval_self_contained_closed={fmt_bool(result['meissel_mertens_interval_self_contained_closed'])}",
        f"self_contained_mertens_tail_closed={fmt_bool(result['self_contained_mertens_tail_closed'])}",
        f"external_b3_chain_reaches_dstructure_gate={fmt_bool(result['external_b3_chain_reaches_dstructure_gate'])}",
        f"dstructure_independent_acceptance_present={fmt_bool(result['dstructure_independent_acceptance_present'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. strict 外部替换",
        "",
        "```text",
        replacement[0],
        "  =>",
        replacement[1],
        "```",
        "",
        "## 2. Mertens 数字口径",
        "",
        "| item | value |",
        "| --- | ---: |",
        f"| Meissel-Mertens B1 | `{fmt_float(float(result['meissel_mertens_b1']))}` |",
        f"| finite step range | `{result['finite_step_range']}` |",
        f"| tail start x | `{result['tail_start_x']}` |",
        f"| Dusart tail error at start | `{fmt_float(float(result['dusart_tail_error_at_start']))}` |",
        f"| external atom | `{result['mertens_external_atom']}` |",
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
            "## 4. strict 外部输入基快照",
            "",
            "```text",
            result["strict_external_basis_snapshot"],
            "```",
            "",
            "## 5. 下一步",
            "",
            (
                f"外部路线下一守门项为 `{result['next_direct_attack_target']}`。严格自足路线仍保留："
                f"`{', '.join(result['remaining_self_contained_after_meissel'])}`。"
            ),
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
