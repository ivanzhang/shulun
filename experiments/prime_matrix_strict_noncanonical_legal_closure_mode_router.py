#!/usr/bin/env python3
"""生成 strict noncanonical 合法闭合模式过滤路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_noncanonical_legal_closure_mode_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-noncanonical-legal-closure-mode-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-noncanonical-legal-closure-mode-router.json"
OUT_MD = DOCS / "prime-matrix-strict-noncanonical-legal-closure-mode-router.md"


SOURCE_FILES = [
    "prime-matrix-strict-terminal-leaf-firewall-current-instance-router.md",
    "prime-matrix-noncanonical-complement-trilemma-router.md",
    "prime-matrix-noncanonical-complement-input-contract-router.md",
    "prime-matrix-noncanonical-two-lane-final-input-router.md",
    "prime-matrix-actual-source-antiatom-lane-audit-router.md",
    "prime-matrix-triad-a1-dibfi-self-contained-closure-taxonomy-router.md",
    "prime-matrix-triad-a1-dibfi-actual-source-provenance-ledger-router.md",
    "prime-matrix-triad-a1-dibfi-full-s-kls-ext-specialization-router.md",
    "prime-matrix-strict-acyclic-canonical-lock-router.md",
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
    """构造 strict noncanonical 合法闭合模式过滤证书。"""
    source_hashes = {
        f"docs/monograph/{name}": sha256(DOCS / name)
        for name in SOURCE_FILES
        if (DOCS / name).exists()
    }

    legal_mode = "NoncanonicalFullSComplementLegalClosureMode"
    canonical_lock = "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary"
    source_identity = "ProveActualFullSNonAPSourceIsCanonicalRIWBuchstab"
    actual_antiatom = "FullSNonAPStrengthenedSourceAntiAtomForActualSource"
    external_contract = "AcceptOrProveExactFullS-KLS-ext"
    source_bridge = "ActualA1FullSSourceLockOrStrengthenedAntiAtomTheoremInput"
    strict_terminal_after = f"{canonical_lock} OR {source_identity} OR {actual_antiatom}"
    strict_terminal_after_compressed = f"{canonical_lock} OR {source_bridge}"
    conditional_terminal_after = f"{strict_terminal_after} OR {external_contract}"
    high_tail = (
        "SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000 AND "
        "SelfContainedMeisselMertensConstantIntervalLedgerAt20000"
    )
    strict_basis = (
        f"({strict_terminal_after_compressed}) AND ({high_tail}) AND "
        "SelfContainedDStructureTailLog4FiniteRankinReplacementPackage"
    )
    conditional_basis = (
        f"({conditional_terminal_after}) AND ({high_tail}) AND "
        "SelfContainedDStructureTailLog4FiniteRankinReplacementPackage"
    )
    external_mertens_basis = (
        f"({strict_terminal_after_compressed}) AND "
        "SelfContainedDStructureTailLog4FiniteRankinReplacementPackage"
    )

    rows = [
        {
            "gate": "NoncanonicalLegalClosureModeActive",
            "closed": True,
            "proved": False,
            "meaning": "上一层当前活动叶子已经压到 canonical-lock 或 noncanonical 合法闭合模式。",
            "remaining": f"{canonical_lock} OR {legal_mode}",
        },
        {
            "gate": "NoncanonicalTrilemmaBoundaryImported",
            "closed": True,
            "proved": True,
            "meaning": "扣除 canonical 分支后，只剩实际源恒等、实际源强化反原子、外部 FullS-KLS 三歧。",
            "remaining": f"{source_identity} OR {actual_antiatom} OR {external_contract}",
        },
        {
            "gate": "GenericWFDSelfContainedTemplateRejected",
            "closed": True,
            "proved": True,
            "meaning": "unrestricted generic WFD 自足反原子被 moving-delta 模型阻断，不能再作为闭合路径。",
            "remaining": "必须进入 actual-source theorem 或外部谱合同。",
        },
        {
            "gate": "CanonicalRestrictedBranchClosedButScoped",
            "closed": True,
            "proved": True,
            "meaning": "canonical RIW/Buchstab 分支来源账本闭合，但只覆盖被 pre-Cauchy 声明为 canonical 的分支。",
            "remaining": "不能静默导入 acyclic/noncanonical 分支。",
        },
        {
            "gate": "ActualSourceIdentityCurrentBranchProved",
            "closed": True,
            "proved": False,
            "meaning": "当前材料没有证明假设反例链生成的 actual full-S non-AP 源就是 canonical RIW/Buchstab。",
            "remaining": source_identity,
        },
        {
            "gate": "ActualSourceStrengthenedAntiAtomProved",
            "closed": True,
            "proved": False,
            "meaning": "当前材料只把实际源反原子精确成最终容量测度无 moving same-(u,v) 原子；没有证明该定理。",
            "remaining": actual_antiatom,
        },
        {
            "gate": "ExternalFullSKLSContractClosedIfAccepted",
            "closed": True,
            "proved": False,
            "meaning": "FullS-KLS-ext 合同版可条件闭合 noncanonical 数学线，但不是 strict 自足证明。",
            "remaining": "DIBFIPrimarySourceSpecializationProof or explicit external acceptance。",
        },
        {
            "gate": "StrictSelfContainedExternalFiltered",
            "closed": True,
            "proved": True,
            "meaning": "严格自足线中过滤外部 FullS-KLS 黑箱；它只能保留在条件定理线。",
            "remaining": f"{source_identity} OR {actual_antiatom}",
        },
        {
            "gate": "ActualSourceBridgePinned",
            "closed": True,
            "proved": False,
            "meaning": "严格自足 noncanonical 叶子已经精确压成实际源锁定或强化反原子。",
            "remaining": source_bridge,
        },
        {
            "gate": "CanonicalLockStillParallel",
            "closed": True,
            "proved": False,
            "meaning": "acyclic terminal canonical-lock 仍是并行替代路线，但需要同集推前和无 payload 残留。",
            "remaining": canonical_lock,
        },
        {
            "gate": "NoncanonicalLegalClosureModeCurrentCorpusProved",
            "closed": True,
            "proved": False,
            "meaning": "边界已过滤到实际源桥，但两条自足桥定理均未证明。",
            "remaining": strict_terminal_after_compressed,
        },
        {
            "gate": "RowColumnUnconditionalClosureCurrentCorpusProved",
            "closed": True,
            "proved": False,
            "meaning": "仍缺 strict terminal actual-source/canonical-lock 输入、高段自足尾项或外部接受、DStructure/Rankin 替代包。",
            "remaining": strict_basis,
        },
    ]

    return {
        "certificate_type": "prime_matrix_strict_noncanonical_legal_closure_mode_router",
        "status": "strict_noncanonical_legal_mode_filtered_to_actual_source_bridge_open",
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "noncanonical_legal_closure_boundary_refined": True,
        "generic_wfd_self_contained_template_rejected": True,
        "canonical_restricted_branch_closed_but_scoped": True,
        "strict_self_contained_external_fulls_kls_filtered": True,
        "external_fulls_kls_contract_closed_if_accepted": True,
        "dibfi_primary_source_specialization_proved": False,
        "actual_source_identity_current_branch_proved": False,
        "actual_source_strengthened_antiatom_proved": False,
        "actual_source_bridge_theorem_closed": False,
        "noncanonical_legal_closure_mode_proved": False,
        "acyclic_terminal_canonical_lock_proved": False,
        "strict_acyclic_terminal_family_proved": False,
        "strict_terminal_family_proved": False,
        "self_contained_mertens_tail_proved": False,
        "self_contained_dstructure_rankin_replacement_proved": False,
        "row_column_unconditional_closed": False,
        "legal_mode_before_router": legal_mode,
        "strict_self_contained_terminal_after_router": strict_terminal_after_compressed,
        "strict_self_contained_terminal_expanded_after_router": strict_terminal_after,
        "conditional_external_terminal_after_router": conditional_terminal_after,
        "strict_self_contained_math_basis_after_router": strict_basis,
        "conditional_external_math_basis_after_router": conditional_basis,
        "with_external_mertens_high_tail_removed_basis": external_mertens_basis,
        "next_attack_contract": {
            "name": "ActualA1FullSSourceLockOrStrengthenedAntiAtomTheoremInput",
            "must_prove": [
                "证明假设反例链生成的 actual full-S non-AP 源在 Cauchy/dispersion 前就是 canonical RIW/Buchstab 决策树源",
                "或证明该 actual source 的最终容量测度满足无 moving same-(u,v) 大原子强化反原子界",
                "若走外部线，明确接受/证明 exact FullS-KLS-ext，并把它标为条件线而非 strict 自足线",
                "若走 canonical-lock，并行证明 acyclic terminal 同集推前和无 noncanonical payload 残留",
            ],
            "cannot_use_as_proof": [
                "重新使用 unrestricted generic WFD 自足反原子模板",
                "把 canonical restricted 分支的来源闭合推广到 noncanonical 补集",
                "从后验 payment/覆盖图反推出 pre-Cauchy actual source identity",
                "把 FullS-KLS-ext 外部合同冒充为 strict 自足证明",
                "把 actual-source 反原子合同的命名当作该反原子已经证明",
            ],
        },
        "rows": rows,
        "source_hashes": source_hashes,
        "plain_conclusion": (
            "本步继续硬攻 `NoncanonicalFullSComplementLegalClosureMode`："
            "三歧边界本身已经闭合，generic WFD 自足模板已被 moving-delta 反例排除，"
            "canonical RIW/Buchstab 分支只在被 pre-Cauchy 声明为 canonical 的口径内闭合。"
            "因此 strict 自足线不能使用外部 FullS-KLS 黑箱，也不能偷导 canonical 分支；"
            "真正剩余被压成 `ActualA1FullSSourceLockOrStrengthenedAntiAtomTheoremInput`，"
            "即实际源锁定到 canonical RIW/Buchstab，或证明实际源强化反原子。"
            "并行替代仍是 `AcyclicTerminalCanonicalLockToCanonicalSourceBoundary`。"
            "两者均未证明，行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict noncanonical 合法闭合模式过滤路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"noncanonical_legal_closure_boundary_refined={fmt_bool(result['noncanonical_legal_closure_boundary_refined'])}",
        f"generic_wfd_self_contained_template_rejected={fmt_bool(result['generic_wfd_self_contained_template_rejected'])}",
        f"canonical_restricted_branch_closed_but_scoped={fmt_bool(result['canonical_restricted_branch_closed_but_scoped'])}",
        f"strict_self_contained_external_fulls_kls_filtered={fmt_bool(result['strict_self_contained_external_fulls_kls_filtered'])}",
        f"external_fulls_kls_contract_closed_if_accepted={fmt_bool(result['external_fulls_kls_contract_closed_if_accepted'])}",
        f"actual_source_identity_current_branch_proved={fmt_bool(result['actual_source_identity_current_branch_proved'])}",
        f"actual_source_strengthened_antiatom_proved={fmt_bool(result['actual_source_strengthened_antiatom_proved'])}",
        f"actual_source_bridge_theorem_closed={fmt_bool(result['actual_source_bridge_theorem_closed'])}",
        f"noncanonical_legal_closure_mode_proved={fmt_bool(result['noncanonical_legal_closure_mode_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"strict_self_contained_terminal_after_router={result['strict_self_contained_terminal_after_router']}",
        "```",
        "",
        "## 1. 过滤链",
        "",
        "```text",
        "NoncanonicalFullSComplementLegalClosureMode",
        "  -> source identity OR strengthened actual-source anti-atom OR exact FullS-KLS-ext",
        "  -> strict self-contained filters out external FullS-KLS black box",
        "  -> generic WFD self-contained anti-atom is refuted",
        "  -> canonical restricted branch cannot be silently imported",
        "  -> ActualA1FullSSourceLockOrStrengthenedAntiAtomTheoremInput",
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
