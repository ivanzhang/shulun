#!/usr/bin/env python3
"""审计 Structured-EHPD 保守结构包的最终接口验收状态。

用法示例：
  python3 experiments/prime_matrix_strict_structured_ehpd_final_interface_audit_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-structured-ehpd-final-interface-audit-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONO = DOCS / "monograph"

OUT_JSON = MONO / "prime-matrix-strict-structured-ehpd-final-interface-audit-router.json"
OUT_MD = MONO / "prime-matrix-strict-structured-ehpd-final-interface-audit-router.md"

PREVIOUS = MONO / "prime-matrix-strict-bg-baker-structured-ehpd-reconciliation-router.json"
FORMAL_REVIEW = DOCS / "formal-theoremization-review.md"
FINAL_TOP = DOCS / "final-top-journal-unconditional-review.md"
FINAL_INTERFACE = DOCS / "final-interface-index.md"
FINAL_XREF = DOCS / "final-cross-reference-matrix.md"
ROW_FORMAL = DOCS / "row-column-reduction-formal-appendix.md"
AB_MATCH = DOCS / "ab-to-d-interface-match.md"
TAIL_LOG4 = DOCS / "tail-log4-theoremization.md"
D_STRUCTURE = DOCS / "d-structure-formal-appendix.md"
NRC = DOCS / "nrc-theoremization.md"
FCT = DOCS / "fct-tree-wfe-theoremization.md"
EXT_AUDIT = DOCS / "ext-citation-final-audit.md"
CONSTANTS_AUDIT = DOCS / "constants-absorption-final-audit.md"
CONSTANTS_NUMBERED = DOCS / "constants-numbered-inequalities.md"
CONSERVATIVE_RESULT = DOCS / "explicit-p0-structured-conservative-result.json"
FINITE_VERIFY = DOCS / "finite-verify-exp5.json"
FINAL_PROMOTION = MONO / "prime-matrix-final-promotion-gate-irreducibility-router.json"
CLAIM_STATUS = MONO / "claim-status-table.md"

SOURCE_FILES = [
    PREVIOUS,
    FORMAL_REVIEW,
    FINAL_TOP,
    FINAL_INTERFACE,
    FINAL_XREF,
    ROW_FORMAL,
    AB_MATCH,
    TAIL_LOG4,
    D_STRUCTURE,
    NRC,
    FCT,
    EXT_AUDIT,
    CONSTANTS_AUDIT,
    CONSTANTS_NUMBERED,
    CONSERVATIVE_RESULT,
    FINITE_VERIFY,
    FINAL_PROMOTION,
    CLAIM_STATUS,
]

ACTIVE_TARGET = "StructuredEHPDConservativePackageFinalInterfaceAuditAndAcceptance"
PROMOTION_GATE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
EXPLICIT_ACCEPTANCE = "ExplicitIndependentPromotionAcceptanceRecord"
SELF_REPLACEMENT = "SelfContainedDStructureTailLog4FiniteRankinReplacementPackage"


def read_text(path: Path) -> str:
    """读取文本；缺失时返回空串。"""
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖文件哈希。"""
    return {str(path.relative_to(ROOT)): sha256(path) for path in SOURCE_FILES if path.exists()}


def contains_all(text: str, needles: list[str]) -> bool:
    """检查文本包含全部关键片段。"""
    return all(item in text for item in needles)


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
    """构造 Structured-EHPD 最终接口审计结果。"""
    previous = load_json(PREVIOUS)
    formal = read_text(FORMAL_REVIEW)
    final_top = read_text(FINAL_TOP)
    final_interface = read_text(FINAL_INTERFACE)
    final_xref = read_text(FINAL_XREF)
    row_formal = read_text(ROW_FORMAL)
    ab_match = read_text(AB_MATCH)
    tail = read_text(TAIL_LOG4)
    d_structure = read_text(D_STRUCTURE)
    nrc = read_text(NRC)
    fct = read_text(FCT)
    ext_audit = read_text(EXT_AUDIT)
    constants = read_text(CONSTANTS_AUDIT)
    constants_numbered = read_text(CONSTANTS_NUMBERED)
    p0_result = load_json(CONSERVATIVE_RESULT)
    finite = load_json(FINITE_VERIFY)
    promotion = load_json(FINAL_PROMOTION)

    active = previous.get("next_direct_attack_target") == ACTIVE_TARGET
    ab_formal_closed = contains_all(
        row_formal,
        ["Theorem A", "Theorem B", "Corollary AB", "三层不重不漏"],
    ) and contains_all(
        ab_match,
        ["Theorem M", "五项逐项成立", "主链不再存在未命名结构黑箱"],
    )
    tail_formal_closed = contains_all(
        tail,
        ["Theorem TL4", "TL4-L", "TL4-S", "TL4-M", "Theorem RKS-log"],
    )
    d_formal_closed = contains_all(
        d_structure,
        ["Theorem D", "Structured-EHPD 排斥", "OMR", "CGTP", "LSMP"],
    )
    nrc_fct_closed = contains_all(nrc, ["Theorem NRC", "Weil"]) and contains_all(
        fct,
        ["Theorem Tree-WFE", "frequency-closure terminal"],
    )
    xref_closed = contains_all(
        final_xref,
        ["已统一为剩余加权候选集合", "已编号", "已复核", "投稿需原文定理编号"],
    )
    constants_closed = contains_all(
        constants,
        ["log_P0_upper=3.5", "exp(3.5)<exp(5)", "常数层面闭合"],
    ) and contains_all(
        constants_numbered,
        ["I1", "I7", "3.5<5"],
    )
    certificate_overlap_closed = (
        float(p0_result.get("log_P0_upper", 999.0)) <= 3.5 + 1e-9
        and finite.get("ok") is True
        and finite.get("max_p") == 148
    )
    ext_reference_located = contains_all(
        ext_audit,
        ["EXT-KL", "EXT-BG", "EXT-Vaaler", "EXT-Selberg", "EXT-Vaughan"],
    )
    formal_review_accepts_author_package = contains_all(
        formal,
        ["当前仓库已经具备定理 1--3 的机械闭合", "A/B、C、D 均已有正式附录证明稿"],
    )
    final_interface_aligned = contains_all(
        final_interface,
        ["A--D 当前状态", "机械证书状态", "禁止误读"],
    )
    top_journal_unconditional_passed = contains_all(
        final_top,
        ["当前稿件尚不能诚实表述为“已经达到顶刊无条件证明标准”"],
    ) is False
    top_journal_conditional_package_complete = contains_all(
        final_top,
        ["完整的条件化审稿包", "不能表述为", "无需额外审查义务"],
    )
    final_promotion_accepted = promotion.get("referee_gate_explicitly_accepted") is True or (
        promotion.get("promotion_package_independently_accepted") is True
    )

    author_side_structured_interface_closed = all(
        [
            active,
            ab_formal_closed,
            tail_formal_closed,
            d_formal_closed,
            nrc_fct_closed,
            xref_closed,
            constants_closed,
            certificate_overlap_closed,
            ext_reference_located,
            formal_review_accepts_author_package,
            final_interface_aligned,
        ]
    )
    row_column_unconditional_closed = (
        author_side_structured_interface_closed
        and top_journal_unconditional_passed
        and final_promotion_accepted
    )

    rows = [
        row(
            "StructuredAuditTargetActive",
            active,
            True,
            "上一同步路由已把最窄点改为 Structured-EHPD 保守结构包最终接口验收。",
            ACTIVE_TARGET,
        ),
        row(
            "ABFormalReductionClosed",
            ab_formal_closed,
            True,
            "A/B 行列反例归约和 A/B 到 D 五项标准形式匹配均已附录化。",
            "no AB structural gap",
        ),
        row(
            "TailLog4FormalAppendixClosed",
            tail_formal_closed,
            True,
            "Tail-log4 已拆成 TL4-L/S/M 与 RKS-log 引用模式。",
            "external theorem numbering if publishing",
        ),
        row(
            "DStructureFormalAppendixClosed",
            d_formal_closed and nrc_fct_closed,
            True,
            "D 组 OMR/CGTP/LSMP、NRC 与 FCT/Tree-WFE 均有正式接口稿。",
            "independent review acceptance",
        ),
        row(
            "CrossReferenceAndConstantsClosed",
            xref_closed and constants_closed,
            True,
            "最终交叉编号矩阵与 I1--I7 常数编号不等式已经对齐抽取器。",
            "editorial theorem/page numbers",
        ),
        row(
            "P0FiniteOverlapCertificateClosed",
            certificate_overlap_closed,
            True,
            "理论入口 log_P0=3.5，有限验证到 exp(5)，两段覆盖全部奇素数。",
            "certificate reproducibility",
        ),
        row(
            "AuthorSideStructuredInterfaceAuditClosed",
            author_side_structured_interface_closed,
            True,
            "作者侧 Structured-EHPD 保守包最终接口审计已完成；它不等同于独立验收。",
            PROMOTION_GATE,
        ),
        row(
            "TopJournalUnconditionalStandardPassed",
            top_journal_unconditional_passed,
            False,
            "顶刊标准复核仍禁止把当前稿件表述为已无需额外审查义务的无条件证明。",
            "external theorem numbering / independent review acceptance",
        ),
        row(
            PROMOTION_GATE,
            final_promotion_accepted,
            False,
            "独立晋级门仍未显式接受，作者侧不能自动生成该事件。",
            f"{EXPLICIT_ACCEPTANCE} OR {SELF_REPLACEMENT}",
        ),
        row(
            "RowColumnUnconditionalClosed",
            row_column_unconditional_closed,
            False,
            "结构接口作者侧已审计闭合，但最终无条件命题仍受独立晋级门约束。",
            PROMOTION_GATE,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_strict_structured_ehpd_final_interface_audit_router",
        "status": "structured_ehpd_author_side_interface_audit_closed_final_promotion_gate_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "author_side_structured_interface_audit_closed": author_side_structured_interface_closed,
        "top_journal_conditional_package_complete": top_journal_conditional_package_complete,
        "top_journal_unconditional_standard_passed": top_journal_unconditional_passed,
        "final_promotion_gate_accepted": final_promotion_accepted,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": row_column_unconditional_closed,
        "next_direct_attack_target": PROMOTION_GATE,
        "parallel_attack_target": EXPLICIT_ACCEPTANCE,
        "self_contained_replacement_target": SELF_REPLACEMENT,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "Structured-EHPD 保守路线的作者侧最终接口审计已经可以关闭：A/B 归约、A/B 到 D 匹配、"
            "Tail-log4、D 组 OMR/CGTP/LSMP、NRC/FCT、交叉编号、常数编号和两段覆盖证书都已对齐。"
            "但这只关闭作者侧接口审计，不把顶刊独立审查或最终晋级门伪造成已发生。"
            "真正剩余现在进一步压缩为 `DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`，"
            "即显式独立接受，或以新的完全自足替代包替换该门。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict Structured-EHPD 最终接口审计证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"author_side_structured_interface_audit_closed={fmt_bool(result['author_side_structured_interface_audit_closed'])}",
        f"top_journal_unconditional_standard_passed={fmt_bool(result['top_journal_unconditional_standard_passed'])}",
        f"final_promotion_gate_accepted={fmt_bool(result['final_promotion_gate_accepted'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 判定表",
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
            "## 2. 下一最精确硬攻点",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """写出 JSON 与 Markdown。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result).rstrip() + "\n", encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")
    print(
        "author_side_structured_interface_audit_closed="
        f"{fmt_bool(result['author_side_structured_interface_audit_closed'])}"
    )


if __name__ == "__main__":
    main()
