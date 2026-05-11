#!/usr/bin/env python3
"""生成 strict actual-source 桥终端障碍路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_actual_source_bridge_terminal_obstruction_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-actual-source-bridge-terminal-obstruction-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-actual-source-bridge-terminal-obstruction-router.json"
OUT_MD = DOCS / "prime-matrix-strict-actual-source-bridge-terminal-obstruction-router.md"


SOURCE_FILES = [
    "prime-matrix-strict-noncanonical-legal-closure-mode-router.md",
    "prime-matrix-strict-actual-source-support-seed-router.md",
    "prime-matrix-triad-a1-source-lock-contract-router.md",
    "prime-matrix-triad-a1-dibfi-full-s-source-antiatom-router.md",
    "prime-matrix-clean-core-moving-atom-sharp-input-router.md",
    "prime-matrix-strict-acyclic-seed-canonical-embedding-router.md",
    "prime-matrix-hypothetical-zero-row-seed-no-go-router.md",
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
    """构造 strict actual-source 桥终端障碍证书。"""
    source_hashes = {
        f"docs/monograph/{name}": sha256(DOCS / name)
        for name in SOURCE_FILES
        if (DOCS / name).exists()
    }

    bridge = "ActualA1FullSSourceLockOrStrengthenedAntiAtomTheoremInput"
    canonical_lock = "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary"
    source_admission = "A1CleanBranchCanonicalSourceAdmission"
    moving_atom = "ActualNoncanonicalCleanCoreMovingAtomExclusion"
    strict_terminal_after = f"{canonical_lock} OR {source_admission} OR {moving_atom}"
    high_tail = (
        "SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000 AND "
        "SelfContainedMeisselMertensConstantIntervalLedgerAt20000"
    )
    strict_basis = (
        f"({strict_terminal_after}) AND ({high_tail}) AND "
        "SelfContainedDStructureTailLog4FiniteRankinReplacementPackage"
    )
    external_mertens_basis = (
        f"({strict_terminal_after}) AND "
        "SelfContainedDStructureTailLog4FiniteRankinReplacementPackage"
    )

    rows = [
        {
            "gate": "ActualSourceBridgeActive",
            "closed": True,
            "proved": False,
            "meaning": "上一层 strict noncanonical 叶子已过滤到实际源锁定或实际源强化反原子。",
            "remaining": bridge,
        },
        {
            "gate": "SourceLockConcreteAtomImported",
            "closed": True,
            "proved": False,
            "meaning": "source-lock 合同显示 canonical 源头链只在 clean A1 分支被证明准入 canonical RIW/Buchstab 时可用。",
            "remaining": source_admission,
        },
        {
            "gate": "SourceLockFreeUpgradeBlocked",
            "closed": True,
            "proved": True,
            "meaning": "不能从 canonical restricted 分支闭合、KZ-E 泛 well-factorable 记录或后验 payment 图免费推出 source lock。",
            "remaining": "必须给 pre-Cauchy 分支准入证明。",
        },
        {
            "gate": "ZeroRowGeometryCannotGenerateSourceLock",
            "closed": True,
            "proved": True,
            "meaning": "早期零行假设、斜线覆盖、圆柱环绕和层叠筛只给 unsigned 覆盖/预算形状，不能反推 signed pre-Cauchy source。",
            "remaining": source_admission,
        },
        {
            "gate": "StrengthenedAntiAtomConcreteAtomImported",
            "closed": True,
            "proved": False,
            "meaning": "source anti-atom 合同已精确为最终 full-S non-AP 容量测度无 moving same-(u,v) 大原子。",
            "remaining": moving_atom,
        },
        {
            "gate": "AntiAtomFreeUpgradeBlocked",
            "closed": True,
            "proved": True,
            "meaning": "formal WFD、Type/Fourier、K4/K6、朴素 incidence 和 canonical 支撑导入均不能推出该反原子。",
            "remaining": moving_atom,
        },
        {
            "gate": "SupportEnergyLemmaOnlyFormal",
            "closed": True,
            "proved": True,
            "meaning": "支撑能量/Cauchy 引理只说明最大 pair 原子界可推出支撑下界，不证明 actual source 的最大原子界。",
            "remaining": "ExactUVPairMassDispersionOrMaxAtomBoundLedger / clean-core moving atom exclusion。",
        },
        {
            "gate": "MovingAtomSharpInputPinned",
            "closed": True,
            "proved": False,
            "meaning": "过强的低支撑 packet 排斥已校准为 sharp moving-atom 排斥；该排斥尚未证明。",
            "remaining": moving_atom,
        },
        {
            "gate": "CanonicalLockStillParallel",
            "closed": True,
            "proved": False,
            "meaning": "acyclic terminal canonical-lock 仍可作为替代路线，但其同集推前与无 payload 残留仍开放。",
            "remaining": canonical_lock,
        },
        {
            "gate": "ActualSourceBridgeCurrentCorpusProved",
            "closed": True,
            "proved": False,
            "meaning": "实际源桥已压到两个具体原子，但没有一个已由当前材料证明。",
            "remaining": f"{source_admission} OR {moving_atom}",
        },
        {
            "gate": "RowColumnUnconditionalClosureCurrentCorpusProved",
            "closed": True,
            "proved": False,
            "meaning": "仍缺 terminal 三选一、高段自足尾项或外部接受、DStructure/Rankin 替代包。",
            "remaining": strict_basis,
        },
    ]

    return {
        "certificate_type": "prime_matrix_strict_actual_source_bridge_terminal_obstruction_router",
        "status": "strict_actual_source_bridge_reduced_to_source_admission_or_moving_atom_open",
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "actual_source_bridge_boundary_sharp": True,
        "source_lock_free_upgrade_blocked": True,
        "zero_row_geometry_source_lock_blocked": True,
        "antiatom_free_upgrade_blocked": True,
        "support_energy_formal_only": True,
        "source_lock_concrete_atom_proved": False,
        "actual_noncanonical_clean_core_moving_atom_exclusion_proved": False,
        "actual_source_bridge_theorem_closed": False,
        "acyclic_terminal_canonical_lock_proved": False,
        "strict_acyclic_terminal_family_proved": False,
        "strict_terminal_family_proved": False,
        "self_contained_mertens_tail_proved": False,
        "self_contained_dstructure_rankin_replacement_proved": False,
        "row_column_unconditional_closed": False,
        "bridge_before_router": bridge,
        "strict_self_contained_terminal_after_router": strict_terminal_after,
        "strict_self_contained_math_basis_after_router": strict_basis,
        "with_external_mertens_high_tail_removed_basis": external_mertens_basis,
        "next_attack_contract": {
            "name": "A1CleanBranchCanonicalSourceAdmission_OR_ActualNoncanonicalCleanCoreMovingAtomExclusion",
            "must_prove": [
                "源锁定线：在 Cauchy/dispersion 前证明 clean A1 反例分支选择 canonical RIW/Buchstab 决策树权重",
                "反原子线：证明通过全部回流测试后的 actual noncanonical clean-core 容量测度没有 moving same-(u,v) 大原子",
                "若任一失败态出现，必须回到 PDEC/SAE/ColumnCRT/CleanKLS 或外部 FullS-KLS 条件线，不能生成第四终端",
                "同步保留 DStructure/Rankin 与高段 Mertens/PNT 自足尾项为独立门",
            ],
            "cannot_use_as_proof": [
                "从真实零行缺席、数值样本或覆盖图直接反推 source",
                "从 canonical 分支闭合静默推出 noncanonical 分支 source lock",
                "把 Cauchy 支撑能量形式引理当成 actual 最大原子界",
                "把低支撑 packet 排斥口径替代 sharp moving-atom 排斥而不证明逆否账本",
                "把外部 FullS-KLS 条件线写成 strict 自足闭合",
            ],
        },
        "rows": rows,
        "source_hashes": source_hashes,
        "plain_conclusion": (
            "本步直接攻击 `ActualA1FullSSourceLockOrStrengthenedAntiAtomTheoremInput`。"
            "源锁定线的具体原子是 `A1CleanBranchCanonicalSourceAdmission`：必须在 Cauchy/dispersion 前证明 "
            "clean A1 反例分支已经选择 canonical RIW/Buchstab 决策树源，不能从后验覆盖图或 canonical restricted "
            "分支闭合反推。强化反原子线的具体原子是 `ActualNoncanonicalCleanCoreMovingAtomExclusion`："
            "必须排斥通过全部回流测试后的 actual noncanonical clean-core 容量大原子，不能由 formal WFD、"
            "Type/Fourier、K4/K6 或支撑能量形式引理免费推出。因此最新 strict 自足终端剩余为 "
            "`AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR A1CleanBranchCanonicalSourceAdmission OR "
            "ActualNoncanonicalCleanCoreMovingAtomExclusion`。这些原子均未证明，行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict actual-source 桥终端障碍路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"actual_source_bridge_boundary_sharp={fmt_bool(result['actual_source_bridge_boundary_sharp'])}",
        f"source_lock_free_upgrade_blocked={fmt_bool(result['source_lock_free_upgrade_blocked'])}",
        f"zero_row_geometry_source_lock_blocked={fmt_bool(result['zero_row_geometry_source_lock_blocked'])}",
        f"antiatom_free_upgrade_blocked={fmt_bool(result['antiatom_free_upgrade_blocked'])}",
        f"support_energy_formal_only={fmt_bool(result['support_energy_formal_only'])}",
        f"source_lock_concrete_atom_proved={fmt_bool(result['source_lock_concrete_atom_proved'])}",
        f"actual_noncanonical_clean_core_moving_atom_exclusion_proved={fmt_bool(result['actual_noncanonical_clean_core_moving_atom_exclusion_proved'])}",
        f"actual_source_bridge_theorem_closed={fmt_bool(result['actual_source_bridge_theorem_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"strict_self_contained_terminal_after_router={result['strict_self_contained_terminal_after_router']}",
        "```",
        "",
        "## 1. 终端障碍链",
        "",
        "```text",
        "ActualA1FullSSourceLockOrStrengthenedAntiAtomTheoremInput",
        "  -> A1CleanBranchCanonicalSourceAdmission",
        "  OR ActualNoncanonicalCleanCoreMovingAtomExclusion",
        "",
        "plus parallel:",
        "  AcyclicTerminalCanonicalLockToCanonicalSourceBoundary",
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
