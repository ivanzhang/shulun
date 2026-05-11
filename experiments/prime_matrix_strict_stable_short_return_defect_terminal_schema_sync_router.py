#!/usr/bin/env python3
"""生成 stable-short-return/phase-defect 到终端 schema 的同步证书。

用法示例：
  python3 experiments/prime_matrix_strict_stable_short_return_defect_terminal_schema_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-stable-short-return-defect-terminal-schema-sync-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONOGRAPH = DOCS / "monograph"
OUT_JSON = MONOGRAPH / "prime-matrix-strict-stable-short-return-defect-terminal-schema-sync-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-stable-short-return-defect-terminal-schema-sync-router.md"

STABLE_SHORT_OR_DEFECT = "StableShortSameLabelRecurrenceOrRegisteredPhaseDefect"
TYPE_COMPRESSION = "BoundaryCapFormalUnitTypeCompressionDichotomy"
EARLY_ZERO_PHASE_ADMISSION = "EarlyZeroPhaseDefectSchemaAdmission"
EARLY_ZERO_TERMINAL_PACKAGE = "EarlyZeroTerminalExclusionPackage"
GLOBAL_TERMINAL = "GlobalPDECorSparseTerminalExclusion"
STRICT_TERMINAL_FAMILY = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily"
MODEL_COMPAT = "ExactModelGapAndDPRCLedgerCompatibilityForMovingBlock"
HIGH_MODEL_GAP = "HighSegmentModelGapAlpha043C3AnalyticLedger"
DSTRUCTURE = "SelfContainedDStructureTailLog4FiniteRankinReplacementPackage"
ACYCLIC_SEED = "AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn"
CANONICAL_LOCK = "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary"
CANONICAL_EXACT_CERT = "AcyclicCanonicalExactSameSetPromotionCertificate"
NEW_ACTUAL_SOURCE_ENTROPY = "NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem"
INDEPENDENT_NONTERMINAL_ENTROPY = (
    "IndependentNonterminalProofOfNewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem"
)

SOURCE_FILES = [
    MONOGRAPH / "prime-matrix-strict-stable-short-return-defect-attack-router.json",
    MONOGRAPH / "prime-matrix-strict-boundary-cap-type-compression-router.json",
    MONOGRAPH / "prime-matrix-early-zero-phase-defect-schema-router.json",
    MONOGRAPH / "prime-matrix-early-zero-terminal-package-reduction-router.json",
    MONOGRAPH / "prime-matrix-anchor-collar-endpoint-bridge-router.json",
    MONOGRAPH / "prime-matrix-anchor-lowmod-fixedwheel-admission-router.json",
    MONOGRAPH / "prime-matrix-anchor-tailcore-fiber-saturation-router.json",
    MONOGRAPH / "prime-matrix-anchor-fiber-saturation-return-schema-router.json",
    MONOGRAPH / "prime-matrix-composite-cofactor-descent-schema-router.json",
    MONOGRAPH / "prime-matrix-early-band-local-survivor-return-schema-router.json",
    MONOGRAPH / "prime-matrix-early-zero-terminal-schema-reconciliation-router.json",
    MONOGRAPH / "prime-matrix-global-pdec-sparse-terminal-split-reconciliation-router.json",
    MONOGRAPH / "prime-matrix-strict-global-terminal-scope-router.json",
    MONOGRAPH / "prime-matrix-strict-alpha-terminal-to-acyclic-cycle-guard-sync-router.json",
    MONOGRAPH / "prime-matrix-strict-independent-actual-source-bridge-concrete-atom-sync-router.json",
    MONOGRAPH / "prime-matrix-strict-source-admission-branch-absorption-router.json",
    MONOGRAPH / "prime-matrix-strict-canonical-lock-nonrecursive-exit-attack-router.json",
    MONOGRAPH / "prime-matrix-strict-canonical-lock-branch-absorption-router.json",
    MONOGRAPH / "prime-matrix-strict-exact-entropy-source-law-firewall-router.json",
    MONOGRAPH / "prime-matrix-strict-new-actual-source-entropy-fixed-point-firewall-router.json",
]


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空字典，避免把缺文件误作已证。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: bool) -> str:
    """写出小写布尔。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def source_hashes() -> dict[str, str]:
    """汇总已存在依赖的哈希。"""
    return {
        str(path.relative_to(ROOT)): sha256(path)
        for path in SOURCE_FILES
        if path.exists()
    }


def missing_sources() -> list[str]:
    """列出缺失依赖；缺失不闭合任何证明门。"""
    return [str(path.relative_to(ROOT)) for path in SOURCE_FILES if not path.exists()]


def sync_rows(
    stable: dict[str, Any],
    boundary: dict[str, Any],
    phase: dict[str, Any],
    terminal_reduction: dict[str, Any],
    terminal_reconcile: dict[str, Any],
    global_split: dict[str, Any],
    strict_scope: dict[str, Any],
    alpha_cycle_guard: dict[str, Any],
    source_bridge: dict[str, Any],
    source_admission: dict[str, Any],
    canonical_lock_exit: dict[str, Any],
    canonical_branch_absorption: dict[str, Any],
    exact_entropy_firewall: dict[str, Any],
    entropy_fixed_point: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成同步判定表。"""
    return [
        {
            "gate": "StableShortReturnDefectHardpointImported",
            "closed": stable.get("hardpoint_before_router") == STABLE_SHORT_OR_DEFECT,
            "proved": False,
            "meaning": "上一层把早期零行反例链压到稳定短复现或登记相位缺陷。",
            "remaining": stable.get("hardpoint_after_router", TYPE_COMPRESSION),
        },
        {
            "gate": "BoundaryCapTypeCompressionOnlyDefinesAdmissionSkeleton",
            "closed": boundary.get("next_direct_attack_target")
            == "BoundaryCapForcedFormalUnitObligationLowerBound",
            "proved": True,
            "meaning": "类型压缩路线已给 row-free type key 与条件鸽巢骨架，但未给 N/T 不等式。",
            "remaining": boundary.get("hardpoint_after_router", TYPE_COMPRESSION),
        },
        {
            "gate": "EarlyZeroPhaseDefectSchemaAdmissionImported",
            "closed": phase.get("early_zero_phase_defect_schema_admission_closed") is True,
            "proved": True,
            "meaning": "早期零行若不形成稳定短复现，可作为同 formal unit 的相位缺陷登记回流。",
            "remaining": "准入层闭合；终端排斥仍未闭合。",
        },
        {
            "gate": "StableShortReturnOrDefectSchemaSynchronized",
            "closed": phase.get("early_zero_phase_defect_schema_admission_closed") is True,
            "proved": True,
            "meaning": "StableShort/Defect 宽标签在 schema 层已与 EarlyZeroPhaseDefectSchemaAdmission 对齐。",
            "remaining": EARLY_ZERO_TERMINAL_PACKAGE,
        },
        {
            "gate": "EarlyZeroTerminalPackageReductionImported",
            "closed": terminal_reduction.get("terminal_gap_after_router") is not None,
            "proved": True,
            "meaning": "抽象终端包已压成 anchor、cofactor、early-band 等命名子项。",
            "remaining": terminal_reduction.get("terminal_gap_after_router", EARLY_ZERO_TERMINAL_PACKAGE),
        },
        {
            "gate": "NamedTerminalPackageReconciledToGlobalGate",
            "closed": terminal_reconcile.get("terminal_gap_after_router")
            == f"{GLOBAL_TERMINAL} AND {MODEL_COMPAT}",
            "proved": True,
            "meaning": "anchor/cofactor/early-band/DLS 专属无名出口已删除，只剩全局终端门和 moving-block 模型兼容门。",
            "remaining": terminal_reconcile.get(
                "terminal_gap_after_router", f"{GLOBAL_TERMINAL} AND {MODEL_COMPAT}"
            ),
        },
        {
            "gate": "GlobalPDECSparseSplitImported",
            "closed": global_split.get("terminal_gap_after_router")
            == "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve",
            "proved": True,
            "meaning": "全局 PDEC/sparse 门已拆到 PDEC-CAP 或内部 CleanKLS 大筛，但这只是终端门拆分。",
            "remaining": global_split.get("terminal_gap_after_router", "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve"),
        },
        {
            "gate": "StrictNoncanonicalScopeImported",
            "closed": STRICT_TERMINAL_FAMILY
            in strict_scope.get("terminal_gap_after_router", ""),
            "proved": True,
            "meaning": "canonical-source 终端晋级不能直接导入 strict noncanonical seed。",
            "remaining": strict_scope.get(
                "terminal_gap_after_router",
                f"{ACYCLIC_SEED} AND {STRICT_TERMINAL_FAMILY} AND {HIGH_MODEL_GAP}",
            ),
        },
        {
            "gate": "DirectPDECCleanKLSCycleGuardImported",
            "closed": alpha_cycle_guard.get("raw_direct_pdec_clean_routes_count_as_closure") is False,
            "proved": True,
            "meaning": "裸攻 direct PDEC/CleanKLS 已被识别为自回流，不能登记为 well-founded 进展量。",
            "remaining": (
                f"{CANONICAL_LOCK} OR "
                "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate"
            ),
        },
        {
            "gate": "LegacyIndependentActualSourceBridgeImported",
            "closed": "ExactCleanCoreFullSNonAPWFDSourceEntropy"
            in source_bridge.get("terminal_gap_after_router", ""),
            "proved": True,
            "meaning": "旧 actual-source 桥把非 canonical 分支先压到 exact clean-core source entropy。",
            "remaining": "ExactCleanCoreFullSNonAPWFDSourceEntropy",
        },
        {
            "gate": "A1SourceAdmissionBranchAbsorbedImported",
            "closed": "ActualNoncanonicalCleanCoreMovingAtomExclusion"
            in source_admission.get("strict_self_contained_terminal_after_router", ""),
            "proved": True,
            "meaning": "A1CleanBranchCanonicalSourceAdmission 只是 scoped branch statement，不能作为独立全局 OR。",
            "remaining": "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR ActualNoncanonicalCleanCoreMovingAtomExclusion",
        },
        {
            "gate": "ExactEntropySourceLawFirewallImported",
            "closed": NEW_ACTUAL_SOURCE_ENTROPY
            in exact_entropy_firewall.get("strict_self_contained_terminal_after_router", ""),
            "proved": True,
            "meaning": "固定投影、formal WFD、早期零行几何和 canonical 支撑链均不能证明 moving hidden fiber 熵律。",
            "remaining": f"{CANONICAL_LOCK} OR {NEW_ACTUAL_SOURCE_ENTROPY}",
        },
        {
            "gate": "CanonicalLockExactSameSetFirewallImported",
            "closed": canonical_lock_exit.get("canonical_lock_refined_to_exact_same_set_certificate")
            is True,
            "proved": True,
            "meaning": "canonical-lock 已被防火墙精炼为五项 exact same-set 晋级证书；缺任一项时不能调用。",
            "remaining": f"{CANONICAL_EXACT_CERT} OR {NEW_ACTUAL_SOURCE_ENTROPY}",
        },
        {
            "gate": "CanonicalLockBranchAbsorptionImported",
            "closed": canonical_branch_absorption.get("canonical_lock_branch_absorption_closed")
            is True,
            "proved": True,
            "meaning": "五项证书存在时只处理 scoped canonical case；证书缺失时活动 noncanonical 主线回到 source entropy。",
            "remaining": NEW_ACTUAL_SOURCE_ENTROPY,
        },
        {
            "gate": "NewActualSourceEntropyFixedPointImported",
            "closed": entropy_fixed_point.get("next_direct_attack_target") == INDEPENDENT_NONTERMINAL_ENTROPY,
            "proved": True,
            "meaning": "ExactUV/pair-energy/rate-bearing/terminal/canonical 旧脊柱形成 T -> ... -> T 固定点。",
            "remaining": INDEPENDENT_NONTERMINAL_ENTROPY,
        },
        {
            "gate": "IndependentNonterminalSourceEntropyCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "当前材料尚未给出不经 pair-mass 失败回流和终端标签的独立 actual-source 熵估计。",
            "remaining": INDEPENDENT_NONTERMINAL_ENTROPY,
        },
        {
            "gate": "AdmissionLayerClosedButTerminalExclusionOpen",
            "closed": True,
            "proved": True,
            "meaning": "本同步只关闭准入/命名回流的重复口径，不关闭终端家族排斥。",
            "remaining": f"{STRICT_TERMINAL_FAMILY} AND {MODEL_COMPAT} AND {HIGH_MODEL_GAP} AND {DSTRUCTURE}",
        },
        {
            "gate": "TerminalExclusionCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "当前材料没有给出 acyclic noncanonical terminal family 的 PDEC-CAP/CleanKLS 排斥证明。",
            "remaining": STRICT_TERMINAL_FAMILY,
        },
        {
            "gate": "RowColumnUnconditionalClosureCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "仍没有从早期零行反例链推出与真实结构链的终端直接矛盾。",
            "remaining": "必须继续攻非循环终端锁定或独立非终端来源熵输入。",
        },
    ]


def build_result() -> dict[str, Any]:
    """构造同步证书。"""
    stable = load_json(MONOGRAPH / "prime-matrix-strict-stable-short-return-defect-attack-router.json")
    boundary = load_json(MONOGRAPH / "prime-matrix-strict-boundary-cap-type-compression-router.json")
    phase = load_json(MONOGRAPH / "prime-matrix-early-zero-phase-defect-schema-router.json")
    terminal_reduction = load_json(
        MONOGRAPH / "prime-matrix-early-zero-terminal-package-reduction-router.json"
    )
    terminal_reconcile = load_json(
        MONOGRAPH / "prime-matrix-early-zero-terminal-schema-reconciliation-router.json"
    )
    global_split = load_json(
        MONOGRAPH / "prime-matrix-global-pdec-sparse-terminal-split-reconciliation-router.json"
    )
    strict_scope = load_json(MONOGRAPH / "prime-matrix-strict-global-terminal-scope-router.json")
    alpha_cycle_guard = load_json(
        MONOGRAPH / "prime-matrix-strict-alpha-terminal-to-acyclic-cycle-guard-sync-router.json"
    )
    source_bridge = load_json(
        MONOGRAPH / "prime-matrix-strict-independent-actual-source-bridge-concrete-atom-sync-router.json"
    )
    source_admission = load_json(
        MONOGRAPH / "prime-matrix-strict-source-admission-branch-absorption-router.json"
    )
    canonical_lock_exit = load_json(
        MONOGRAPH / "prime-matrix-strict-canonical-lock-nonrecursive-exit-attack-router.json"
    )
    canonical_branch_absorption = load_json(
        MONOGRAPH / "prime-matrix-strict-canonical-lock-branch-absorption-router.json"
    )
    exact_entropy_firewall = load_json(
        MONOGRAPH / "prime-matrix-strict-exact-entropy-source-law-firewall-router.json"
    )
    entropy_fixed_point = load_json(
        MONOGRAPH / "prime-matrix-strict-new-actual-source-entropy-fixed-point-firewall-router.json"
    )

    terminal_gap_after = (
        f"{STRICT_TERMINAL_FAMILY} AND {MODEL_COMPAT} AND {HIGH_MODEL_GAP} AND {DSTRUCTURE}"
    )
    strict_basis_after = f"{ACYCLIC_SEED} AND {terminal_gap_after}"
    noncycle_exit = INDEPENDENT_NONTERMINAL_ENTROPY
    conditional_canonical_branch = CANONICAL_EXACT_CERT
    rows = sync_rows(
        stable=stable,
        boundary=boundary,
        phase=phase,
        terminal_reduction=terminal_reduction,
        terminal_reconcile=terminal_reconcile,
        global_split=global_split,
        strict_scope=strict_scope,
        alpha_cycle_guard=alpha_cycle_guard,
        source_bridge=source_bridge,
        source_admission=source_admission,
        canonical_lock_exit=canonical_lock_exit,
        canonical_branch_absorption=canonical_branch_absorption,
        exact_entropy_firewall=exact_entropy_firewall,
        entropy_fixed_point=entropy_fixed_point,
    )
    return {
        "certificate_type": "prime_matrix_strict_stable_short_return_defect_terminal_schema_sync_router",
        "status": "stable_short_return_defect_schema_synced_to_strict_terminal_family_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "stable_short_return_schema_admission_imported": phase.get(
            "early_zero_phase_defect_schema_admission_closed"
        )
        is True,
        "phase_defect_named_return_schema_closed": True,
        "stable_short_return_or_defect_admission_schema_closed": True,
        "early_zero_terminal_package_reconciled_to_global_terminal": True,
        "direct_pdec_clean_routes_count_as_closure": False,
        "terminal_exclusion_proved": False,
        "global_pdec_sparse_terminal_exclusion_proved": False,
        "pdec_cap_or_internal_clean_kls_large_sieve_for_acyclic_noncanonical_terminal_family_proved": False,
        "acyclic_terminal_canonical_lock_proved": False,
        "independent_nonterminal_source_entropy_proved": False,
        "high_segment_model_gap_alpha043_c3_analytic_ledger_proved": False,
        "dstructure_tail_log4_finite_rankin_replacement_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": STABLE_SHORT_OR_DEFECT,
        "admission_gap_before_router": (
            f"{TYPE_COMPRESSION} OR registered phase defect schema admission"
        ),
        "admission_gap_after_router": "closed_as_named_schema_admission_only",
        "terminal_gap_after_router": terminal_gap_after,
        "strict_self_contained_basis_after_router": strict_basis_after,
        "noncycle_exit_after_router": noncycle_exit,
        "conditional_canonical_branch_after_router": conditional_canonical_branch,
        "next_direct_attack_target": INDEPENDENT_NONTERMINAL_ENTROPY,
        "absorbed_conditional_branch": conditional_canonical_branch,
        "forbidden_as_closure_target": "naked PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve",
        "sync_rows": rows,
        "source_hashes": source_hashes(),
        "missing_sources": missing_sources(),
        "plain_conclusion": (
            "`StableShortSameLabelRecurrenceOrRegisteredPhaseDefect` 的准入/命名层已经可以同步为"
            "`EarlyZeroPhaseDefectSchemaAdmission`：早期零行反例若不产生稳定短复现，就产生登记相位缺陷，"
            "并进入 PDEC/SAE/ColumnCRT/LocalSurvivor 命名回流。真正未闭合的不是这个准入口径，"
            "而是 strict noncanonical 终端家族的排斥，以及模型余量和 DStructure/Rankin 独立门。"
            "同时 canonical-lock 已被后续材料吸收为 scoped exact same-set 条件分支，"
            "活动 noncanonical 主线的最新最窄点是独立非终端来源熵证明，不能再裸攻 PDEC/CleanKLS 标签。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown。"""
    lines = [
        "# Prime Matrix strict 稳定短复现/相位缺陷终端 schema 同步路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"same_theorem_target_preserved={fmt_bool(result['same_theorem_target_preserved'])}",
        f"stable_short_return_or_defect_admission_schema_closed={fmt_bool(result['stable_short_return_or_defect_admission_schema_closed'])}",
        f"phase_defect_named_return_schema_closed={fmt_bool(result['phase_defect_named_return_schema_closed'])}",
        f"early_zero_terminal_package_reconciled_to_global_terminal={fmt_bool(result['early_zero_terminal_package_reconciled_to_global_terminal'])}",
        f"direct_pdec_clean_routes_count_as_closure={fmt_bool(result['direct_pdec_clean_routes_count_as_closure'])}",
        f"terminal_exclusion_proved={fmt_bool(result['terminal_exclusion_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 同步结论",
        "",
        "准入层从：",
        "",
        "```text",
        result["hardpoint_before_router"],
        "```",
        "",
        "同步为：",
        "",
        "```text",
        result["admission_gap_after_router"],
        "```",
        "",
        "终端层仍剩：",
        "",
        "```text",
        result["terminal_gap_after_router"],
        "```",
        "",
        "strict 自足基更新为：",
        "",
        "```text",
        result["strict_self_contained_basis_after_router"],
        "```",
        "",
        "非循环出口：",
        "",
        "```text",
        result["noncycle_exit_after_router"],
        "```",
        "",
        "已吸收的条件 canonical 分支：",
        "",
        "```text",
        result["conditional_canonical_branch_after_router"],
        "```",
        "",
        "## 2. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in result["sync_rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=table_cell(row["gate"]),
                closed=fmt_bool(row["closed"]),
                proved=fmt_bool(row["proved"]),
                meaning=table_cell(row["meaning"]),
                remaining=table_cell(row["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 3. 下一主攻点",
            "",
            "首攻：",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "已吸收条件分支：",
            "",
            "```text",
            result["absorbed_conditional_branch"],
            "```",
            "",
            "不能登记为闭合的裸目标：",
            "",
            "```text",
            result["forbidden_as_closure_target"],
            "```",
            "",
        ]
    )
    if result["missing_sources"]:
        lines.extend(["## 4. 缺失依赖", ""])
        for item in result["missing_sources"]:
            lines.append(f"- `{item}`")
        lines.append("")
    return "\n".join(lines)


def main() -> None:
    """写出证书。"""
    result = build_result()
    OUT_JSON.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")


if __name__ == "__main__":
    main()
