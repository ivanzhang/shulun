#!/usr/bin/env python3
"""生成 strict source-admission 分支吸收路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_source_admission_branch_absorption_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-source-admission-branch-absorption-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-source-admission-branch-absorption-router.json"
OUT_MD = DOCS / "prime-matrix-strict-source-admission-branch-absorption-router.md"


SOURCE_FILES = [
    "prime-matrix-strict-actual-source-bridge-terminal-obstruction-router.md",
    "prime-matrix-triad-a1-canonical-branch-admission-router.md",
    "prime-matrix-actual-source-bridge-global-reconciliation-router.md",
    "prime-matrix-triad-a1-dibfi-self-contained-final-closure-router.md",
    "prime-matrix-strict-acyclic-canonical-lock-router.md",
    "prime-matrix-clean-core-moving-atom-sharp-input-router.md",
]


def sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: bool) -> str:
    """把布尔值格式化为小写文本。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def build_result() -> dict[str, Any]:
    """构造 source-admission 分支吸收证书。"""
    source_hashes = {
        f"docs/monograph/{name}": sha256(DOCS / name)
        for name in SOURCE_FILES
        if (DOCS / name).exists()
    }

    canonical_lock = "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary"
    source_admission = "A1CleanBranchCanonicalSourceAdmission"
    branch_statement = "A1CanonicalSourceBranchStatementAndCoverage"
    moving_atom = "ActualNoncanonicalCleanCoreMovingAtomExclusion"
    before = f"{canonical_lock} OR {source_admission} OR {moving_atom}"
    after = f"{canonical_lock} OR {moving_atom}"
    external_after = f"{after} OR AcceptOrProveExactFullS-KLS-ext"
    high_tail = (
        "SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000 AND "
        "SelfContainedMeisselMertensConstantIntervalLedgerAt20000"
    )
    strict_basis = (
        f"({after}) AND ({high_tail}) AND "
        "SelfContainedDStructureTailLog4FiniteRankinReplacementPackage"
    )
    conditional_basis = (
        f"({external_after}) AND ({high_tail}) AND "
        "SelfContainedDStructureTailLog4FiniteRankinReplacementPackage"
    )
    external_mertens_basis = (
        f"({after}) AND "
        "SelfContainedDStructureTailLog4FiniteRankinReplacementPackage"
    )

    rows = [
        {
            "gate": "TripleTerminalInputActive",
            "closed": True,
            "proved": False,
            "meaning": "上一层把 strict 终端写成 canonical-lock、A1 源准入或 moving-atom 排斥三选一。",
            "remaining": before,
        },
        {
            "gate": "A1SourceAdmissionReducedToBranchStatement",
            "closed": True,
            "proved": True,
            "meaning": "A1CleanBranchCanonicalSourceAdmission 已被既有路由压成 canonical 内部分支与 generic 外部分支的陈述覆盖合同。",
            "remaining": branch_statement,
        },
        {
            "gate": "CanonicalBranchSelfContainedClosedWithScope",
            "closed": True,
            "proved": True,
            "meaning": "canonical RIW/Buchstab source branch 的内部链条已经闭合，但陈述边界限定在 canonical-source 分支。",
            "remaining": "不覆盖 unrestricted generic/noncanonical complement。",
        },
        {
            "gate": "A1SourceAdmissionNotStandaloneGlobalContradiction",
            "closed": True,
            "proved": True,
            "meaning": "该准入只说明 canonical 分支可内部处理；若反例落在 noncanonical 分支，仍需 moving-atom 排斥或外部谱线。",
            "remaining": moving_atom,
        },
        {
            "gate": "OROverclaimRemoved",
            "closed": True,
            "proved": True,
            "meaning": "把 A1CleanBranchCanonicalSourceAdmission 作为独立 OR 终端会把分支陈述误当全局排斥，因此从活动 OR 中吸收掉。",
            "remaining": after,
        },
        {
            "gate": "CanonicalLockStillStrongerParallelRoute",
            "closed": True,
            "proved": False,
            "meaning": "canonical-lock 仍保留，因为它要求 acyclic terminal 证书同集推前且无 noncanonical payload，强于单纯 A1 分支陈述。",
            "remaining": canonical_lock,
        },
        {
            "gate": "MovingAtomNowUniqueNoncanonicalStrictLeaf",
            "closed": True,
            "proved": False,
            "meaning": "删除分支陈述伪终端后，strict noncanonical 活动叶子只剩 actual clean-core moving atom 排斥。",
            "remaining": moving_atom,
        },
        {
            "gate": "RowColumnUnconditionalClosureCurrentCorpusProved",
            "closed": True,
            "proved": False,
            "meaning": "仍缺 canonical-lock 或 moving-atom 排斥、高段自足尾项或外部接受、DStructure/Rankin 替代包。",
            "remaining": strict_basis,
        },
    ]

    return {
        "certificate_type": "prime_matrix_strict_source_admission_branch_absorption_router",
        "status": "strict_source_admission_absorbed_as_branch_statement_moving_atom_open",
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "source_admission_reduced_to_branch_statement": True,
        "canonical_branch_self_contained_closed_with_scope": True,
        "source_admission_standalone_global_contradiction": False,
        "source_admission_absorbed_from_active_or": True,
        "moving_atom_unique_noncanonical_strict_leaf": True,
        "source_lock_concrete_atom_proved": False,
        "actual_noncanonical_clean_core_moving_atom_exclusion_proved": False,
        "acyclic_terminal_canonical_lock_proved": False,
        "strict_acyclic_terminal_family_proved": False,
        "strict_terminal_family_proved": False,
        "self_contained_mertens_tail_proved": False,
        "self_contained_dstructure_rankin_replacement_proved": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": before,
        "strict_self_contained_terminal_after_router": after,
        "conditional_external_terminal_after_router": external_after,
        "strict_self_contained_math_basis_after_router": strict_basis,
        "conditional_external_math_basis_after_router": conditional_basis,
        "with_external_mertens_high_tail_removed_basis": external_mertens_basis,
        "next_attack_contract": {
            "name": "ActualNoncanonicalCleanCoreMovingAtomExclusion_OR_AcyclicTerminalCanonicalLock",
            "must_prove": [
                "若走 noncanonical 主线，证明 actual clean-core 容量测度没有 moving same-(u,v) 大原子",
                "若走 canonical-lock 备用线，证明 acyclic terminal 证书同集推前且 canonical 投影后无 noncanonical payload",
                "继续把 A1 canonical 分支陈述作为边界纪律使用，不再把它当独立全局排斥原子",
                "保留外部 FullS-KLS 为条件线，保留高段 Mertens/PNT 与 DStructure/Rankin 为独立门",
            ],
            "cannot_use_as_proof": [
                "把 canonical-source 分支闭合写成 unrestricted global 闭合",
                "把 A1CleanBranchCanonicalSourceAdmission 作为单独 OR 关闭全局反例",
                "用后验覆盖图或数值缺席生成 pre-Cauchy source",
                "用 formal WFD/Type/Fourier/K4/K6 推出 moving-atom 排斥",
                "把外部 FullS-KLS 条件线写成 strict 自足闭合",
            ],
        },
        "rows": rows,
        "source_hashes": source_hashes,
        "plain_conclusion": (
            "`A1CleanBranchCanonicalSourceAdmission` 继续下压后不是一个能独立排斥全局反例的终端原子。"
            "既有 A1 canonical branch admission 路由已经把它化为分支陈述：canonical RIW/Buchstab 分支由内部链条闭合，"
            "generic/noncanonical 分支必须外部化或回流。因此把它放在 strict 终端 OR 中会过强；"
            "本步将它吸收为分支边界纪律，并把当前 strict 活动终端从三选一压成 "
            "`AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR ActualNoncanonicalCleanCoreMovingAtomExclusion`。"
            "这不是命题闭合；moving atom 排斥和 canonical-lock 仍未证明。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict source-admission 分支吸收路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"source_admission_reduced_to_branch_statement={fmt_bool(result['source_admission_reduced_to_branch_statement'])}",
        f"canonical_branch_self_contained_closed_with_scope={fmt_bool(result['canonical_branch_self_contained_closed_with_scope'])}",
        f"source_admission_standalone_global_contradiction={fmt_bool(result['source_admission_standalone_global_contradiction'])}",
        f"source_admission_absorbed_from_active_or={fmt_bool(result['source_admission_absorbed_from_active_or'])}",
        f"moving_atom_unique_noncanonical_strict_leaf={fmt_bool(result['moving_atom_unique_noncanonical_strict_leaf'])}",
        f"actual_noncanonical_clean_core_moving_atom_exclusion_proved={fmt_bool(result['actual_noncanonical_clean_core_moving_atom_exclusion_proved'])}",
        f"acyclic_terminal_canonical_lock_proved={fmt_bool(result['acyclic_terminal_canonical_lock_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"strict_self_contained_terminal_after_router={result['strict_self_contained_terminal_after_router']}",
        "```",
        "",
        "## 1. 吸收链",
        "",
        "```text",
        "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary",
        "OR A1CleanBranchCanonicalSourceAdmission",
        "OR ActualNoncanonicalCleanCoreMovingAtomExclusion",
        "",
        "A1CleanBranchCanonicalSourceAdmission",
        "  -> A1CanonicalSourceBranchStatementAndCoverage",
        "  -> canonical branch closed with scope; generic branch still external/noncanonical",
        "  -> not a standalone global contradiction",
        "",
        "therefore active strict terminal:",
        "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary",
        "OR ActualNoncanonicalCleanCoreMovingAtomExclusion",
        "```",
        "",
        "## 2. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=table_cell(row["gate"]),
                closed=fmt_bool(row["closed"]),
                proved=fmt_bool(row["proved"]),
                meaning=table_cell(row["meaning"]),
                remaining=table_cell(row["remaining"]),
            )
        )

    contract = result["next_attack_contract"]
    lines.extend(
        [
            "",
            "## 3. 最新严格基",
            "",
            "严格自足基更新为：",
            "",
            "```text",
            result["strict_self_contained_math_basis_after_router"],
            "```",
            "",
            "条件外部线可写为：",
            "",
            "```text",
            result["conditional_external_math_basis_after_router"],
            "```",
            "",
            "若明确接受外部 Mertens/theta 显式输入，高段尾项可暂时移出活动缺口，剩：",
            "",
            "```text",
            result["with_external_mertens_high_tail_removed_basis"],
            "```",
            "",
            "## 4. 下一主攻合同",
            "",
            f"下一数学主攻点：`{contract['name']}`。",
            "",
            "必须证明：",
        ]
    )
    for item in contract["must_prove"]:
        lines.append(f"- {item}。")

    lines.extend(["", "不能作为证明使用："])
    for item in contract["cannot_use_as_proof"]:
        lines.append(f"- {item}。")

    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """命令行入口。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(OUT_JSON)
    print(OUT_MD)


if __name__ == "__main__":
    main()
