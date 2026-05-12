#!/usr/bin/env python3
"""生成 strict moving-atom 到 exact entropy 标准形路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_moving_atom_entropy_normal_form_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-moving-atom-entropy-normal-form-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-moving-atom-entropy-normal-form-router.json"
OUT_MD = DOCS / "prime-matrix-strict-moving-atom-entropy-normal-form-router.md"


SOURCE_FILES = [
    "prime-matrix-strict-source-admission-branch-absorption-router.md",
    "prime-matrix-clean-core-terminal-normal-form-router.md",
    "prime-matrix-clean-core-moving-atom-sharp-input-router.md",
    "prime-matrix-triad-a1-dibfi-self-contained-antiatom-nogo-router.md",
    "prime-matrix-triad-a1-moving-block-spread-obstruction.md",
    "prime-matrix-self-contained-narrowest-core-router.md",
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
    """构造 moving-atom exact entropy 标准形证书。"""
    source_hashes = {
        f"docs/monograph/{name}": sha256(DOCS / name)
        for name in SOURCE_FILES
        if (DOCS / name).exists()
    }

    canonical_lock = "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary"
    moving_atom = "ActualNoncanonicalCleanCoreMovingAtomExclusion"
    exact_entropy = "ExactCleanCoreFullSNonAPWFDSourceEntropy"
    completed_kls = "ModulusDependentCompletedFullSKLSInput"
    before = f"{canonical_lock} OR {moving_atom}"
    strict_after = f"{canonical_lock} OR {exact_entropy}"
    conditional_after = f"{canonical_lock} OR {exact_entropy} OR {completed_kls}"
    high_tail = (
        "SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000 AND "
        "SelfContainedMeisselMertensConstantIntervalLedgerAt20000"
    )
    strict_basis = (
        f"({strict_after}) AND ({high_tail}) AND "
        "SelfContainedDStructureTailLog4FiniteRankinReplacementPackage"
    )
    conditional_basis = (
        f"({conditional_after}) AND ({high_tail}) AND "
        "SelfContainedDStructureTailLog4FiniteRankinReplacementPackage"
    )
    external_mertens_basis = (
        f"({strict_after}) AND "
        "SelfContainedDStructureTailLog4FiniteRankinReplacementPackage"
    )

    rows = [
        {
            "gate": "MovingAtomStrictLeafActive",
            "closed": True,
            "proved": False,
            "meaning": "上一层已删除 A1 分支陈述伪终端，活动 strict 叶子为 canonical-lock 或 clean-core moving atom 排斥。",
            "remaining": before,
        },
        {
            "gate": "MovingAtomSharpInputPinned",
            "closed": True,
            "proved": False,
            "meaning": "moving atom 是通过所有回流测试后仍承载最终 M_{u,v} 大原子的 actual clean-core block。",
            "remaining": moving_atom,
        },
        {
            "gate": "MovingAtomEqualsExactEntropy",
            "closed": True,
            "proved": False,
            "meaning": "无 moving 大原子等价于 max_b M_b/M <= log^{-2A} 的 exact clean-core source entropy。",
            "remaining": exact_entropy,
        },
        {
            "gate": "CompletedKLSExternalNormalFormImported",
            "closed": True,
            "proved": False,
            "meaning": "外部替代标准形是 completed、modulus-dependent 的 full-S KLS 输入，不是泛称 DI/BFI。",
            "remaining": completed_kls,
        },
        {
            "gate": "StrictSelfContainedExternalFiltered",
            "closed": True,
            "proved": True,
            "meaning": "严格自足线过滤 completed KLS 外部黑箱；它只能保留在条件定理线。",
            "remaining": strict_after,
        },
        {
            "gate": "GenericAntiAtomNoGoRetained",
            "closed": True,
            "proved": True,
            "meaning": "moving-delta 反模型说明 formal/generic WFD 版反原子为假；exact entropy 必须是 actual-source 定理。",
            "remaining": exact_entropy,
        },
        {
            "gate": "FixedProjectionDiffuseInsufficient",
            "closed": True,
            "proved": True,
            "meaning": "固定投影 diffuse 不能推出 moving-block 非集中；hidden same-(u,v) fiber 可随尺度移动。",
            "remaining": exact_entropy,
        },
        {
            "gate": "ExactEntropyCurrentCorpusProved",
            "closed": True,
            "proved": False,
            "meaning": "当前材料尚未证明 actual clean-core exact source entropy。",
            "remaining": exact_entropy,
        },
        {
            "gate": "CanonicalLockStillParallel",
            "closed": True,
            "proved": False,
            "meaning": "canonical-lock 仍是并行替代路线，但同集推前和无 payload 残留仍未证。",
            "remaining": canonical_lock,
        },
        {
            "gate": "RowColumnUnconditionalClosureCurrentCorpusProved",
            "closed": True,
            "proved": False,
            "meaning": "仍缺 canonical-lock 或 exact entropy、高段自足尾项或外部接受、DStructure/Rankin 替代包。",
            "remaining": strict_basis,
        },
    ]

    return {
        "certificate_type": "prime_matrix_strict_moving_atom_entropy_normal_form_router",
        "status": "strict_moving_atom_reduced_to_exact_entropy_open",
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "moving_atom_entropy_normal_form_closed": True,
        "strict_self_contained_external_completed_kls_filtered": True,
        "generic_antiatom_no_go_retained": True,
        "fixed_projection_diffuse_insufficient": True,
        "exact_clean_core_source_entropy_proved": False,
        "external_completed_kls_accepted": False,
        "actual_noncanonical_clean_core_moving_atom_exclusion_proved": False,
        "acyclic_terminal_canonical_lock_proved": False,
        "strict_acyclic_terminal_family_proved": False,
        "strict_terminal_family_proved": False,
        "self_contained_mertens_tail_proved": False,
        "self_contained_dstructure_rankin_replacement_proved": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": before,
        "strict_self_contained_terminal_after_router": strict_after,
        "conditional_external_terminal_after_router": conditional_after,
        "strict_self_contained_math_basis_after_router": strict_basis,
        "conditional_external_math_basis_after_router": conditional_basis,
        "with_external_mertens_high_tail_removed_basis": external_mertens_basis,
        "next_attack_contract": {
            "name": "ExactCleanCoreFullSNonAPWFDSourceEntropy_OR_AcyclicTerminalCanonicalLock",
            "must_prove": [
                "证明 actual clean-core full-S non-AP WFD 源满足 max_b M_b/M <= log^{-2A}",
                "或证明 canonical-lock 的同集推前与无 noncanonical payload 残留",
                "若走外部线，必须明确接受或证明 ModulusDependentCompletedFullSKLSInput",
                "保留高段 Mertens/PNT 与 DStructure/Rankin 为独立门",
            ],
            "cannot_use_as_proof": [
                "用 fixed-projection diffuse 代替 moving-block entropy",
                "用 unrestricted generic WFD/Type/Fourier 模板代替 actual source entropy",
                "把 completed KLS 外部条件线写成 strict 自足证明",
                "把 canonical-source 分支支撑下界导入 noncanonical exact entropy",
            ],
        },
        "rows": rows,
        "source_hashes": source_hashes,
        "plain_conclusion": (
            "`ActualNoncanonicalCleanCoreMovingAtomExclusion` 已经可以替换成更精确的内部标准形 "
            "`ExactCleanCoreFullSNonAPWFDSourceEntropy`：无 moving same-(u,v) 大原子等价于 "
            "`max_b M_b/M <= log^{-2A}`。外部替代标准形是 "
            "`ModulusDependentCompletedFullSKLSInput`，但 strict 自足线不能使用它。"
            "因此当前 strict 活动终端从 `canonical-lock OR moving-atom` 更新为 "
            "`AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR ExactCleanCoreFullSNonAPWFDSourceEntropy`。"
            "exact entropy 和 canonical-lock 均未证明，行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict moving-atom exact entropy 标准形路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"moving_atom_entropy_normal_form_closed={fmt_bool(result['moving_atom_entropy_normal_form_closed'])}",
        f"strict_self_contained_external_completed_kls_filtered={fmt_bool(result['strict_self_contained_external_completed_kls_filtered'])}",
        f"generic_antiatom_no_go_retained={fmt_bool(result['generic_antiatom_no_go_retained'])}",
        f"fixed_projection_diffuse_insufficient={fmt_bool(result['fixed_projection_diffuse_insufficient'])}",
        f"exact_clean_core_source_entropy_proved={fmt_bool(result['exact_clean_core_source_entropy_proved'])}",
        f"external_completed_kls_accepted={fmt_bool(result['external_completed_kls_accepted'])}",
        f"acyclic_terminal_canonical_lock_proved={fmt_bool(result['acyclic_terminal_canonical_lock_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"strict_self_contained_terminal_after_router={result['strict_self_contained_terminal_after_router']}",
        "```",
        "",
        "## 1. 标准形链",
        "",
        "```text",
        "ActualNoncanonicalCleanCoreMovingAtomExclusion",
        "  <=> ExactCleanCoreFullSNonAPWFDSourceEntropy",
        "      max_b M_b/M <= log^{-2A}",
        "",
        "external alternative:",
        "  ModulusDependentCompletedFullSKLSInput",
        "",
        "strict self-contained active terminal:",
        "  AcyclicTerminalCanonicalLockToCanonicalSourceBoundary",
        "  OR ExactCleanCoreFullSNonAPWFDSourceEntropy",
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
