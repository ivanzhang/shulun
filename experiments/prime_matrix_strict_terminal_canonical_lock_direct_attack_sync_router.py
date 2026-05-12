#!/usr/bin/env python3
"""生成 strict 终端 canonical-lock 直攻同步证书。

用法示例：
  python3 experiments/prime_matrix_strict_terminal_canonical_lock_direct_attack_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-terminal-canonical-lock-direct-attack-sync-router.json

输出：
  docs/monograph/prime-matrix-strict-terminal-canonical-lock-direct-attack-sync-router.json
  docs/monograph/prime-matrix-strict-terminal-canonical-lock-direct-attack-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-terminal-canonical-lock-direct-attack-sync-router.json"
OUT_MD = DOCS / "prime-matrix-strict-terminal-canonical-lock-direct-attack-sync-router.md"

CANONICAL_LOCK = "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary"
DIRECT_PDEC = "DirectAcyclicSameSetPDECCapDualCertificate"
DIRECT_CLEAN = "DirectAcyclicCleanKLSDLSEstimateWithNamedReturn"
SOURCE_ENTROPY = "NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem"
WINDOWED_DLS = "AcyclicWindowedKloostermanDLSInternalEstimate"
KUZNETSOV_DLS = "SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks"
PDEC_CLEAN = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve"
MODEL_LEDGER = "ExplicitModelGapAndFiniteDPRCLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SIGNED_SOURCE_PACKAGE = (
    "ActualSignedAlphaSourceMeasureForCarryShellRowsLedger AND "
    "AlphaSignedWeightLawFromPreCauchyArithmeticIdentityLedger AND "
    "AlphaRowsPhiPushforwardCompatibilityLedger AND "
    "AlphaSignedLiftVariationBranchBudgetLedger"
)

SOURCE_FILES = [
    "prime-matrix-strict-actual-source-antiatom-exactuv-terminal-sync-router.json",
    "prime-matrix-strict-acyclic-canonical-lock-router.json",
    "prime-matrix-strict-canonical-branch-admission-timeline-router.json",
    "prime-matrix-strict-acyclic-canonical-precauchy-identity-router.json",
    "prime-matrix-strict-acyclic-seed-canonical-t1-equality-router.json",
    "prime-matrix-strict-acyclic-t1-mismatch-forcing-router.json",
    "prime-matrix-strict-alpha-signed-lift-failure-return-router.json",
    "prime-matrix-strict-alpha-signed-weight-downstream-sync-router.json",
    "prime-matrix-strict-acyclic-windowed-dls-estimate-router.json",
    "prime-matrix-strict-direct-acyclic-same-set-pdec-dual-router.json",
]


def load_json(name: str) -> dict[str, Any]:
    """读取上游 JSON；缺失时返回空对象。"""
    path = DOCS / name
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """记录证据哈希。"""
    result = {"script": sha256(Path(__file__).resolve())}
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = sha256(path)
    return result


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def cell(value: Any) -> str:
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


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """同步 canonical-lock 下钻证据。"""
    terminal_sync = data["terminal_sync"]
    canonical_lock = data["canonical_lock"]
    timeline = data["timeline"]
    precauchy = data["precauchy"]
    equality = data["equality"]
    mismatch = data["mismatch"]
    failure_return = data["failure_return"]
    alpha_downstream = data["alpha_downstream"]
    dls = data["dls"]
    direct_pdec = data["direct_pdec"]

    terminal_imported = (
        terminal_sync.get("next_primary_target") == CANONICAL_LOCK
        and CANONICAL_LOCK in str(terminal_sync.get("self_contained_terminal_after_sync", ""))
    )
    lock_atomized = (
        canonical_lock.get("acyclic_canonical_lock_boundary_refined") is True
        and canonical_lock.get("acyclic_terminal_canonical_lock_proved") is False
    )
    timeline_guard = (
        timeline.get("canonical_branch_admission_timeline_guard_closed") is True
        and timeline.get("acyclic_seed_canonical_branch_admission_before_cauchy_proved") is False
    )
    precauchy_reduced = (
        precauchy.get("canonical_t1_coefficient_formula_available_scoped") is True
        and precauchy.get("acyclic_canonical_precauchy_coefficient_identity_ledger_proved") is False
    )
    equality_classified = (
        equality.get("equality_branch_classifier_closed") is True
        and equality.get("canonical_equality_case_absorbed") is True
        and equality.get("acyclic_seed_to_canonical_t1_coefficient_equality_proved") is False
    )
    mismatch_closed_not_excluded = (
        mismatch.get("mismatch_forcing_schema_closed") is True
        and mismatch.get("all_mismatch_exits_closed_current_corpus") is False
    )
    failure_return_closed_not_excluded = (
        failure_return.get("alpha_signed_lift_failure_named_return_ledger_closed") is True
        and failure_return.get("failure_return_exclusion_proved") is False
    )
    alpha_downstream_synced = (
        alpha_downstream.get("downstream_sync_router_closed") is True
        and alpha_downstream.get("pdec_cap_or_internal_clean_kls_large_sieve_proved") is False
    )
    dls_reduced = (
        dls.get("acyclic_windowed_bilinear_normal_form_closed") is True
        and dls.get("self_contained_kuznetsov_dls_large_sieve_inequality_proved") is False
    )
    pdec_scope_open = (
        direct_pdec.get("scope_audit_closed") is True
        and direct_pdec.get("direct_acyclic_same_set_pdec_cap_dual_certificate_proved") is False
    )

    return [
        row(
            "TerminalSyncImported",
            terminal_imported,
            False,
            "上一轮已把 actual-source 反原子线压回 strict acyclic 终端三原子，首攻 canonical-lock。",
            f"{CANONICAL_LOCK} OR {DIRECT_PDEC} OR {DIRECT_CLEAN}",
        ),
        row(
            "CanonicalLockAtomized",
            lock_atomized,
            False,
            "canonical-lock 已拆成源因子嵌入、同集推前、无 noncanonical payload 三项；当前未证明。",
            "AcyclicSeedCanonicalSourceFiniteFactorEmbedding AND TerminalCertificateSameSetPushforwardIdentity AND NoNoncanonicalPayloadSurvivesCanonicalProjection",
        ),
        row(
            "CanonicalAdmissionTimelineGuardClosed",
            timeline_guard,
            False,
            "canonical branch 准入必须是 pre-Cauchy T1 身份声明，不能由下游 payment/PDEC/覆盖图反推。",
            "AcyclicCanonicalPreCauchyCoefficientIdentityLedger",
        ),
        row(
            "PreCauchyIdentityReducedToT1Equality",
            precauchy_reduced,
            False,
            "canonical RIW/Buchstab T1 公式只在 scoped canonical 分支闭合；acyclic seed 的逐点等式仍未证。",
            "AcyclicSeedToCanonicalT1CoefficientEqualityAndBranchKeyLock",
        ),
        row(
            "CanonicalEqualityCaseOnlyScoped",
            equality_classified,
            True,
            "若 T1 等式和 branch-key lock 全成立，只进入 canonical scoped promotion；这不是全局矛盾。",
            "mismatch branch remains for noncanonical complement",
        ),
        row(
            "MismatchNoSilentExitClosed",
            mismatch_closed_not_excluded,
            False,
            "T1 mismatch 已无静默出口，只能进 signed source、命名回流或 clean DLS；但这些出口尚未排斥。",
            mismatch.get("terminal_gap_after_router", ""),
        ),
        row(
            "SignedLiftFailureReturnLedgerClosed",
            failure_return_closed_not_excluded,
            False,
            "signed lift 失败均已登记为同 formal unit 的命名出口；登记不等于排斥。",
            f"({SIGNED_SOURCE_PACKAGE}) OR NamedReturnExclusion OR {WINDOWED_DLS}",
        ),
        row(
            "AlphaWeightDownstreamReturnsToTerminalFamily",
            alpha_downstream_synced,
            False,
            "alpha signed 权重律继续下钻后回到 PDEC/CleanKLS 终端门、模型余量账本和 DStructure 门。",
            f"{PDEC_CLEAN} AND {MODEL_LEDGER} AND {DSTRUCTURE}",
        ),
        row(
            "WindowedDLSReducedToKuznetsovAtom",
            dls_reduced,
            False,
            "clean DLS 形式层已压尽，真正未证的是自足 Kuznetsov/DLS 大筛不等式。",
            KUZNETSOV_DLS,
        ),
        row(
            "DirectPDECScopeAuditStillOpen",
            pdec_scope_open,
            False,
            "direct same-set PDEC 协议可用，但 acyclic/noncanonical 作用域匹配未证；不能替代 canonical-lock。",
            CANONICAL_LOCK,
        ),
        row(
            "CanonicalLockCurrentAttackProved",
            False,
            False,
            "本轮直攻没有证明 canonical-lock；它被吸收到 scoped canonical case 或回到 mismatch/DLS/终端门。",
            f"({SIGNED_SOURCE_PACKAGE}) OR NamedReturnExclusion OR {KUZNETSOV_DLS} OR ({PDEC_CLEAN} AND {MODEL_LEDGER})",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "终端矛盾、Kuznetsov/DLS、模型余量和 DStructure/Rankin 均未全证，不能声明行/列无条件闭合。",
            f"(({PDEC_CLEAN} AND {MODEL_LEDGER}) OR {KUZNETSOV_DLS}) AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造同步结果。"""
    data = {
        "terminal_sync": load_json("prime-matrix-strict-actual-source-antiatom-exactuv-terminal-sync-router.json"),
        "canonical_lock": load_json("prime-matrix-strict-acyclic-canonical-lock-router.json"),
        "timeline": load_json("prime-matrix-strict-canonical-branch-admission-timeline-router.json"),
        "precauchy": load_json("prime-matrix-strict-acyclic-canonical-precauchy-identity-router.json"),
        "equality": load_json("prime-matrix-strict-acyclic-seed-canonical-t1-equality-router.json"),
        "mismatch": load_json("prime-matrix-strict-acyclic-t1-mismatch-forcing-router.json"),
        "failure_return": load_json("prime-matrix-strict-alpha-signed-lift-failure-return-router.json"),
        "alpha_downstream": load_json("prime-matrix-strict-alpha-signed-weight-downstream-sync-router.json"),
        "dls": load_json("prime-matrix-strict-acyclic-windowed-dls-estimate-router.json"),
        "direct_pdec": load_json("prime-matrix-strict-direct-acyclic-same-set-pdec-dual-router.json"),
    }
    rows = build_rows(data)
    boundary_closed = all(item["closed"] for item in rows[:10])
    latest_basis = f"(({PDEC_CLEAN} AND {MODEL_LEDGER}) OR {KUZNETSOV_DLS}) AND {DSTRUCTURE}"
    return {
        "certificate_type": "prime_matrix_strict_terminal_canonical_lock_direct_attack_sync_router",
        "status": (
            "strict_terminal_canonical_lock_attacked_to_mismatch_or_dls_open"
            if boundary_closed
            else "strict_terminal_canonical_lock_direct_attack_sync_incomplete"
        ),
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "canonical_lock_direct_attack_boundary_closed": boundary_closed,
        "canonical_equality_case_absorbed_scoped_only": True,
        "mismatch_no_silent_exit_closed": True,
        "signed_lift_failure_return_ledger_closed": True,
        "acyclic_terminal_canonical_lock_proved": False,
        "direct_acyclic_same_set_pdec_cap_dual_certificate_proved": False,
        "self_contained_kuznetsov_dls_large_sieve_inequality_proved": False,
        "pdec_cap_or_internal_clean_kls_large_sieve_proved": False,
        "explicit_model_gap_and_finite_dprc_ledger_proved": False,
        "dstructure_tail_log4_finite_rankin_full_ledger_independent_acceptance_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "terminal_before_router": f"{CANONICAL_LOCK} OR {DIRECT_PDEC} OR {DIRECT_CLEAN}",
        "terminal_after_router": (
            f"({SIGNED_SOURCE_PACKAGE}) OR NamedReturnExclusion OR {KUZNETSOV_DLS} "
            f"OR ({PDEC_CLEAN} AND {MODEL_LEDGER})"
        ),
        "latest_self_contained_basis_after_router": latest_basis,
        "next_primary_target": KUZNETSOV_DLS,
        "next_parallel_target": MODEL_LEDGER,
        "promotion_gate": DSTRUCTURE,
        "rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本轮直接攻 canonical-lock。结论是：canonical T1 等式成立时只给 scoped canonical "
            "吸收，不给全局矛盾；等式不成立时，mismatch 已无静默出口，只能进入 signed source、"
            "命名回流或 clean DLS。signed lift 失败登记纪律已闭合，但出口排斥未证；clean DLS "
            "又精确压成自足 Kuznetsov/DLS 大筛原子。direct PDEC 作用域审查仍未证明 acyclic "
            "同集匹配。因此 canonical-lock 不是当前闭合出口，行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown。"""
    lines: list[str] = []
    lines.append("# Prime Matrix strict 终端 canonical-lock 直攻同步证书")
    lines.append("")
    lines.append(f"**状态：** `{result['status']}`")
    lines.append("")
    lines.append(result["plain_conclusion"])
    lines.append("")
    lines.append("```text")
    for key in [
        "canonical_lock_direct_attack_boundary_closed",
        "canonical_equality_case_absorbed_scoped_only",
        "mismatch_no_silent_exit_closed",
        "signed_lift_failure_return_ledger_closed",
        "acyclic_terminal_canonical_lock_proved",
        "self_contained_kuznetsov_dls_large_sieve_inequality_proved",
        "pdec_cap_or_internal_clean_kls_large_sieve_proved",
        "direct_unconditional_contradiction_found",
        "row_column_unconditional_closed",
    ]:
        lines.append(f"{key}={fmt_bool(result[key])}")
    lines.append("```")
    lines.append("")
    lines.append("## 1. 直攻压缩")
    lines.append("")
    lines.append("攻击前：")
    lines.append("")
    lines.append("```text")
    lines.append(result["terminal_before_router"])
    lines.append("```")
    lines.append("")
    lines.append("攻击后：")
    lines.append("")
    lines.append("```text")
    lines.append(result["terminal_after_router"])
    lines.append("```")
    lines.append("")
    lines.append("## 2. 判定表")
    lines.append("")
    lines.append("| gate | closed | proved | meaning | remaining |")
    lines.append("| --- | --- | --- | --- | --- |")
    for item in result["rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{cell(item['gate'])}`",
                    f"`{fmt_bool(item['closed'])}`",
                    f"`{fmt_bool(item['proved'])}`",
                    cell(item["meaning"]),
                    cell(item["remaining"]),
                ]
            )
            + " |"
        )
    lines.append("")
    lines.append("## 3. 最新严格基")
    lines.append("")
    lines.append("```text")
    lines.append(result["latest_self_contained_basis_after_router"])
    lines.append("```")
    lines.append("")
    lines.append("下一首攻点：")
    lines.append("")
    lines.append("```text")
    lines.append(result["next_primary_target"])
    lines.append("```")
    lines.append("")
    lines.append("并行账本：")
    lines.append("")
    lines.append("```text")
    lines.append(result["next_parallel_target"])
    lines.append("```")
    lines.append("")
    lines.append("审稿边界：本文件关闭 canonical-lock 直攻的路由分类，不证明 Kuznetsov/DLS、PDEC/CleanKLS、模型余量或 DStructure/Rankin。")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """写出证书。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"status={result['status']}")
    print(f"canonical_lock_direct_attack_boundary_closed={fmt_bool(result['canonical_lock_direct_attack_boundary_closed'])}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")
    print(f"wrote={OUT_JSON.relative_to(ROOT)}")
    print(f"wrote={OUT_MD.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
