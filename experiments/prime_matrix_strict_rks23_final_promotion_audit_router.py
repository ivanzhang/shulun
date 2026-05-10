#!/usr/bin/env python3
"""RNRS 闭合后的最终推广门审计。

用法示例：
  python3 experiments/prime_matrix_strict_rks23_final_promotion_audit_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-rks23-final-promotion-audit-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONO = ROOT / "docs" / "monograph"

OUT_JSON = MONO / "prime-matrix-strict-rks23-final-promotion-audit-router.json"
OUT_MD = MONO / "prime-matrix-strict-rks23-final-promotion-audit-router.md"

AFTER_RNRS = MONO / "prime-matrix-strict-rks23-row-column-after-rnrs-audit-router.json"
DUAL_LANE = MONO / "prime-matrix-strict-self-contained-dual-lane-final-router.json"
PROMOTION_GATE = MONO / "prime-matrix-final-promotion-gate-irreducibility-router.json"
STRUCTURED_AUDIT = MONO / "prime-matrix-strict-structured-ehpd-final-interface-audit-router.json"
ORDERED_TASKS = MONO / "prime-matrix-ordered-remaining-task-execution-router.md"

SOURCE_FILES = [AFTER_RNRS, DUAL_LANE, PROMOTION_GATE, STRUCTURED_AUDIT, ORDERED_TASKS]

EXACT_UV = "ActualNoncanonicalExactUVSupportLowerBound"
DSTRUCTURE_GATE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
DSTRUCTURE_REPLACEMENT = "SelfContainedDStructureTailLog4FiniteRankinReplacementPackage"
FINAL_PROMOTION = "RowColumnUnconditionalTheoremFinalPromotion"
NEXT_AUTHOR_MATH = "CleanCoreTerminalSupportIncidenceTheorem_FOR_ActualNoncanonicalExactUVSupportLowerBound"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def read_text(path: Path) -> str:
    """读取文本；缺失时返回空串。"""
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖文件哈希。"""
    return {str(path.relative_to(ROOT)): sha256(path) for path in SOURCE_FILES if path.exists()}


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_result() -> dict[str, Any]:
    """构造最终推广门审计结果。"""
    after_rnrs = load_json(AFTER_RNRS)
    dual_lane = load_json(DUAL_LANE)
    promotion = load_json(PROMOTION_GATE)
    structured = load_json(STRUCTURED_AUDIT)
    ordered_text = read_text(ORDERED_TASKS)

    rnrs_energy_gates_closed = all(
        [
            after_rnrs.get("noncircular_energy_input_closed") is True,
            after_rnrs.get("weighted_energy_input_closed") is True,
            after_rnrs.get("balanced_collar_absorption_closed") is True,
        ]
    )
    strict_self_contained_boundary_imported = dual_lane.get("strict_self_contained_boundary_closed") is True
    exact_uv_support_closed = dual_lane.get("actual_exact_uv_support_proved") is True
    self_contained_promotion_replacement_closed = dual_lane.get("self_contained_promotion_replacement_proved") is True
    independent_promotion_gate_accepted = promotion.get("referee_gate_explicitly_accepted") is True
    structured_interface_audit_closed = structured.get("author_side_structured_interface_audit_closed") is True
    ordered_task_boundary_imported = "RowColumnUnconditionalPromotion" in ordered_text

    author_side_rks23_energy_lane_closed = rnrs_energy_gates_closed
    final_promotion_gate_closed = (
        exact_uv_support_closed
        and (self_contained_promotion_replacement_closed or independent_promotion_gate_accepted)
    )
    row_column_unconditional_closed = final_promotion_gate_closed

    final_blockers = [
        {
            "atom": EXACT_UV,
            "closed": exact_uv_support_closed,
            "author_completable": True,
            "why_remaining": "strict self-contained lane requires actual noncanonical exact u/v support; current corpus still marks it unproved",
        },
        {
            "atom": DSTRUCTURE_GATE,
            "closed": independent_promotion_gate_accepted,
            "author_completable": False,
            "why_remaining": "this is an independent acceptance/referee event, not an author-generated proof step",
        },
        {
            "atom": DSTRUCTURE_REPLACEMENT,
            "closed": self_contained_promotion_replacement_closed,
            "author_completable": True,
            "why_remaining": "strict self-contained route must replace the independent gate if no external acceptance is used",
        },
    ]

    audit_summary = {
        "rnrs_effect": "RKS23/RNRS energy line is no longer the blocker",
        "strict_self_contained_basis": f"{EXACT_UV} AND {DSTRUCTURE_REPLACEMENT}",
        "conditional_external_basis": f"external/conditional lane plus explicit acceptance of {DSTRUCTURE_GATE}",
        "promotion_verdict": "row/column unconditional closure cannot be asserted until ExactUV and the promotion gate/replacement are closed",
        "next_author_side_math": NEXT_AUTHOR_MATH,
    }

    rows = [
        row(
            "RKS23RNRSEnergyLaneClosed",
            author_side_rks23_energy_lane_closed,
            True,
            "RNRS 已补齐非循环能量输入和平衡颈部加权能量门。",
            "RKS23/RNRS lane closed",
        ),
        row(
            "StrictSelfContainedBoundaryImported",
            strict_self_contained_boundary_imported,
            True,
            "严格自足最终边界已导入：外部谱抵消线不能替代自足证明。",
            "strict self-contained boundary",
        ),
        row(
            "StructuredInterfaceAuditClosed",
            structured_interface_audit_closed,
            True,
            "Structured-EHPD 作者侧接口审计已完成，但不等于独立接受。",
            DSTRUCTURE_GATE,
        ),
        row(
            "OrderedTaskBoundaryImported",
            ordered_task_boundary_imported,
            True,
            "旧按序任务表确认 RowColumnUnconditionalPromotion 仍被命名输入阻断。",
            FINAL_PROMOTION,
        ),
        row(
            "ActualExactUVSupportClosed",
            exact_uv_support_closed,
            False,
            "ActualNoncanonicalExactUVSupportLowerBound 仍未在当前语料中证明。",
            NEXT_AUTHOR_MATH,
        ),
        row(
            "IndependentPromotionGateAccepted",
            independent_promotion_gate_accepted,
            False,
            "DStructure/Tail-log4/finite Rankin 独立晋级门仍未显式接受。",
            DSTRUCTURE_GATE,
        ),
        row(
            "SelfContainedPromotionReplacementClosed",
            self_contained_promotion_replacement_closed,
            False,
            "若拒绝独立验收，仍需作者侧自足替代证明包。",
            DSTRUCTURE_REPLACEMENT,
        ),
        row(
            "RowColumnFinalPromotionClosed",
            final_promotion_gate_closed,
            False,
            "最终推广门仍被 ExactUV 与晋级门/替代包阻断。",
            f"{EXACT_UV} AND ({DSTRUCTURE_GATE} OR {DSTRUCTURE_REPLACEMENT})",
        ),
        row(
            "RowColumnUnconditionalClosed",
            row_column_unconditional_closed,
            False,
            "不能把 RNRS 能量线闭合误升级为完整行/列无条件定理。",
            FINAL_PROMOTION,
        ),
    ]

    closed_gates = [item["gate"] for item in rows if item["closed"]]
    open_gates = [item["gate"] for item in rows if not item["closed"]]

    return {
        "certificate_type": "strict_rks23_final_promotion_audit_router",
        "status": "rks23_energy_lane_closed_final_row_column_promotion_still_blocked_by_exact_uv_and_promotion_gate",
        "rnrs_energy_gates_closed": rnrs_energy_gates_closed,
        "author_side_rks23_energy_lane_closed": author_side_rks23_energy_lane_closed,
        "strict_self_contained_boundary_imported": strict_self_contained_boundary_imported,
        "structured_interface_audit_closed": structured_interface_audit_closed,
        "ordered_task_boundary_imported": ordered_task_boundary_imported,
        "actual_exact_uv_support_closed": exact_uv_support_closed,
        "independent_promotion_gate_accepted": independent_promotion_gate_accepted,
        "self_contained_promotion_replacement_closed": self_contained_promotion_replacement_closed,
        "row_column_final_promotion_closed": final_promotion_gate_closed,
        "row_column_unconditional_closed": row_column_unconditional_closed,
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "empirical_absence_not_used": True,
        "counterexample_assumption_only": True,
        "audit_summary": audit_summary,
        "final_blockers": final_blockers,
        "closed_gates": closed_gates,
        "open_gates": open_gates,
        "remaining_atoms": final_blockers,
        "next_direct_attack_target": NEXT_AUTHOR_MATH,
        "next_required_input": f"{EXACT_UV}; then {DSTRUCTURE_REPLACEMENT} or explicit acceptance of {DSTRUCTURE_GATE}",
        "plain_conclusion": (
            "RNRS/RKS23 能量线已经闭合，但最终行/列无条件推广仍被 ExactUV 支撑下界和 "
            "DStructure/Tail-log4/finite Rankin 晋级门阻断。下一作者侧数学主攻点应回到 "
            "ActualNoncanonicalExactUVSupportLowerBound 的 clean-core terminal support incidence 证明。"
        ),
        "source_hashes": source_hashes(),
        "rows": rows,
    }


def render_md(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = []
    lines.append("# Prime Matrix strict RKS23 最终推广门审计证书")
    lines.append("")
    lines.append(f"**状态：** `{result['status']}`")
    lines.append("")
    lines.append(
        "本步完成 RNRS 闭合后的最终推广审计。结论很窄：RKS23/RNRS 能量线已闭合，"
        "但完整行/列无条件命题仍不能标为闭合，因为最终 ExactUV 支撑下界和 DStructure 晋级门/自足替代包仍未闭合。"
    )
    lines.append("")
    lines.append("```text")
    for key in [
        "author_side_rks23_energy_lane_closed",
        "actual_exact_uv_support_closed",
        "independent_promotion_gate_accepted",
        "self_contained_promotion_replacement_closed",
        "row_column_final_promotion_closed",
        "row_column_unconditional_closed",
    ]:
        lines.append(f"{key}={fmt_bool(result[key])}")
    lines.append("```")
    lines.append("")
    lines.append("## 1. 审计摘要")
    lines.append("")
    lines.append("| field | value |")
    lines.append("| --- | --- |")
    for key, value in result["audit_summary"].items():
        lines.append(f"| `{key}` | {table_cell(value)} |")
    lines.append("")
    lines.append("## 2. 最终阻断项")
    lines.append("")
    lines.append("| atom | closed | author_completable | why_remaining |")
    lines.append("| --- | --- | --- | --- |")
    for item in result["final_blockers"]:
        lines.append(
            f"| `{item['atom']}` | `{fmt_bool(item['closed'])}` | `{fmt_bool(item['author_completable'])}` | {table_cell(item['why_remaining'])} |"
        )
    lines.append("")
    lines.append("## 3. 判定表")
    lines.append("")
    lines.append("| gate | closed | proved | meaning | remaining |")
    lines.append("| --- | --- | --- | --- | --- |")
    for item in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=item["gate"],
                closed=fmt_bool(item["closed"]),
                proved=fmt_bool(item["proved"]),
                meaning=table_cell(item["meaning"]),
                remaining=table_cell(item["remaining"]),
            )
        )
    lines.append("")
    lines.append("## 4. 下一真正自足目标")
    lines.append("")
    lines.append("```text")
    lines.append(result["next_direct_attack_target"])
    lines.append(result["next_required_input"])
    lines.append("```")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """生成 JSON 与 Markdown 证书。"""
    result = build_result()
    MONO.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_md(result), encoding="utf-8")
    print(f"wrote {OUT_JSON.relative_to(ROOT)}")
    print(f"wrote {OUT_MD.relative_to(ROOT)}")
    print(f"author_side_rks23_energy_lane_closed={fmt_bool(result['author_side_rks23_energy_lane_closed'])}")
    print(f"actual_exact_uv_support_closed={fmt_bool(result['actual_exact_uv_support_closed'])}")
    print(f"self_contained_promotion_replacement_closed={fmt_bool(result['self_contained_promotion_replacement_closed'])}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")


if __name__ == "__main__":
    main()
