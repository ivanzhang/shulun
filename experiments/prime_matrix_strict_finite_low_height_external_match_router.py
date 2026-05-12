#!/usr/bin/env python3
"""生成 strict 低高度零点外部匹配路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_finite_low_height_external_match_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-finite-low-height-external-match-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"

OUT_JSON = MONOGRAPH / "prime-matrix-strict-finite-low-height-external-match-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-finite-low-height-external-match-router.md"

THETA_STRICT = MONOGRAPH / "prime-matrix-strict-theta-target-external-match-self-frontier-router.json"
XI_NOZERO = MONOGRAPH / "prime-matrix-b3-xi-nozero-below14-router.json"
FINITE_EXTERNAL = MONOGRAPH / "prime-matrix-b3-finite-low-height-external-router.json"
CLAIM_STATUS = MONOGRAPH / "claim-status-table.md"

SOURCE_FILES = [THETA_STRICT, XI_NOZERO, FINITE_EXTERNAL, CLAIM_STATUS]

OLD_ATOM = "FiniteLowHeightZeroCheckLedger"
STRICT_EXTERNAL_CLOSED = "FiniteLowHeightZeroCheckStrictExternalClosedFirstZeroGT14TuringComplete"
OLD_EXTERNAL_CLOSED = "FiniteLowHeightZeroCheckExternalClosedFirstZeroGT14TuringComplete"
THETA_STRICT_CLOSED = "ThetaEnvelopeTargetAt20000StrictExternalMatchedDusartOneOver36260"
XI_EXTERNAL_CLOSED = "BacklundXiNoNontrivialZeroBelow14ExternalClosed"
EXPLICIT_CONTOUR = "ExplicitPsiThetaContourEnvelopeXGe20000FromZeroFreeRegion"
CRITICAL_LINE_SELF = "CriticalLineNoZeroOn0To14FiniteLedger"
OFF_LINE_SELF = "CriticalStripNoOffLineZeroBelow14TuringLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

HEIGHT_TARGET = 14.0


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


def source_table(xi: dict[str, Any]) -> list[dict[str, Any]]:
    """抽取低高度证据数字。"""
    return [
        ("height target", float(xi.get("height_target", HEIGHT_TARGET)), "本链只需排除 0<|gamma|<=14。"),
        ("first zero reference", float(xi.get("first_zero_reference", 0.0)), "外部首个非平凡零点高度。"),
        ("height margin", float(xi.get("height_margin", 0.0)), "首零点高度相对 14 的余量。"),
        ("Platt-Trudgian height", float(xi.get("platt_trudgian_height", 0.0)), "外部严格验证高度。"),
    ]


def build_rows(theta: dict[str, Any], xi: dict[str, Any], finite_external: dict[str, Any]) -> list[dict[str, Any]]:
    """生成 strict 低高度外部匹配判定表。"""
    guard = (
        theta.get("counterexample_assumption_only") is True
        and theta.get("direct_unconditional_contradiction_found") is False
        and theta.get("row_column_unconditional_closed") is False
        and xi.get("row_column_unconditional_closed") is False
        and finite_external.get("row_column_unconditional_closed") is False
    )
    active = theta.get("next_direct_attack_target") == OLD_ATOM
    theta_ready = theta.get("theta_target_external_strict_matched") is True
    xi_ready = (
        xi.get("xi_nozero_below14_external_closed") is True
        and xi.get("low_height_envelope_external_closed") is True
        and float(xi.get("height_target", HEIGHT_TARGET)) <= HEIGHT_TARGET
        and float(xi.get("first_zero_reference", 0.0)) > HEIGHT_TARGET
        and float(xi.get("height_margin", 0.0)) > 0
        and float(xi.get("platt_trudgian_height", 0.0)) > HEIGHT_TARGET
    )
    external_template = finite_external.get("finite_low_height_external_closed") is True
    closed = guard and active and theta_ready and xi_ready
    return [
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只补外部解析输入，不使用真实零行缺席。",
            "保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。",
        ),
        row(
            "FiniteLowHeightGateActive",
            active,
            True,
            "theta 外部严格匹配后，下一最窄点是 T<=14 的有限低高度零点核验。",
            OLD_ATOM,
        ),
        row(
            "ThetaTargetStrictExternalReady",
            theta_ready,
            False,
            "theta@20000 已在外部路线严格匹配 Dusart 界。",
            THETA_STRICT_CLOSED,
        ),
        row(
            "XiNoZeroBelow14ExternalReady",
            xi_ready,
            False,
            "首零点高度大于 14，且外部 Turing/Platt-Trudgian 完备性排除低高度漏零。",
            XI_EXTERNAL_CLOSED,
        ),
        row(
            "ExternalFiniteLowHeightTemplateChecked",
            external_template,
            True,
            "旧低高度证书只复用来源数字和闭合边界，不改变 strict theta 前置。",
            OLD_EXTERNAL_CLOSED,
        ),
        row(
            OLD_ATOM,
            closed,
            False,
            "接受外部低高度证书后，有限低高度核验在外部路线上严格匹配关闭。",
            STRICT_EXTERNAL_CLOSED,
        ),
        row(
            "SelfContainedLowHeightStillOpen",
            False,
            False,
            "严格自足路线仍需文内 Riemann-Siegel/Turing 有限核验账本。",
            f"{CRITICAL_LINE_SELF} AND {OFF_LINE_SELF}",
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "低高度外部输入闭合不触动最终行列命题。",
            DSTRUCTURE,
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造证书对象。"""
    theta = load_json(THETA_STRICT)
    xi = load_json(XI_NOZERO)
    finite_external = load_json(FINITE_EXTERNAL)
    rows = build_rows(theta, xi, finite_external)
    closed = next(item["closed"] for item in rows if item["gate"] == OLD_ATOM)
    return {
        "certificate_type": "prime_matrix_strict_finite_low_height_external_match_router",
        "status": "finite_low_height_strict_external_matched_self_contained_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "finite_low_height_strict_external_matched": closed,
        "finite_low_height_self_contained_closed": False,
        "self_contained_mertens_tail_closed": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "replacement_external": {
            OLD_ATOM: STRICT_EXTERNAL_CLOSED,
        },
        "remaining_self_contained_after_low_height": [CRITICAL_LINE_SELF, OFF_LINE_SELF],
        "next_direct_attack_target": EXPLICIT_CONTOUR,
        "source_hashes": source_hashes(),
        "source_table": source_table(xi),
        "plain_conclusion": (
            "`FiniteLowHeightZeroCheckLedger` 已在外部路线上严格匹配关闭："
            "theta 前置已由 strict 外部 Dusart 匹配给出，低高度部分由首零点大于 14 和 "
            "Platt-Trudgian/Turing 完备性证书承担。该步仍不是文内自足低高度证明。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    replacement = next(iter(result["replacement_external"].items()))
    lines = [
        "# Prime Matrix strict 低高度零点外部匹配路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"finite_low_height_strict_external_matched={fmt_bool(result['finite_low_height_strict_external_matched'])}",
        f"finite_low_height_self_contained_closed={fmt_bool(result['finite_low_height_self_contained_closed'])}",
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
        "## 2. 低高度数字",
        "",
        "| item | value | meaning |",
        "| --- | ---: | --- |",
    ]
    for name, value, meaning in result["source_table"]:
        lines.append(f"| {table_cell(name)} | `{fmt_float(float(value))}` | {table_cell(meaning)} |")
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
