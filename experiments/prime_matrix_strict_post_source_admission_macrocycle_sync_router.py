#!/usr/bin/env python3
"""生成 post-source-admission 非循环宏循环同步证书。

用法示例：
  python3 experiments/prime_matrix_strict_post_source_admission_macrocycle_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-post-source-admission-macrocycle-sync-router.json

输出：
  data/prime-matrix-strict-post-source-admission-macrocycle-sync-ledger.json
  docs/monograph/prime-matrix-strict-post-source-admission-macrocycle-sync-router.json
  docs/monograph/prime-matrix-strict-post-source-admission-macrocycle-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-strict-post-source-admission-macrocycle-sync-ledger.json"
OUT_JSON = DOCS / "prime-matrix-strict-post-source-admission-macrocycle-sync-router.json"
OUT_MD = DOCS / "prime-matrix-strict-post-source-admission-macrocycle-sync-router.md"

SOURCE_FILES = [
    "prime-matrix-strict-post-kze-direct-source-bridge-sync-router.json",
    "prime-matrix-strict-source-admission-branch-absorption-router.json",
    "prime-matrix-strict-acyclic-canonical-precauchy-identity-router.json",
    "prime-matrix-strict-acyclic-seed-canonical-t1-equality-router.json",
    "prime-matrix-strict-acyclic-t1-mismatch-forcing-router.json",
    "prime-matrix-strict-alpha-signed-lift-failure-return-router.json",
    "prime-matrix-strict-alpha-signed-weight-downstream-sync-router.json",
    "prime-matrix-strict-self-contained-cycle-obstruction-router.json",
    "prime-matrix-strict-acyclic-terminal-family-latest-saturation-router.json",
    "prime-matrix-strict-nonrecursive-breaker-latest-cycle-sync-router.json",
    "prime-matrix-strict-post-pdec-new-joint-noncycle-sync-router.json",
    "prime-matrix-strict-post-new-joint-kz-nocycle-gate-sync-router.json",
]

A1 = "A1CleanBranchCanonicalSourceAdmission"
MISMATCH = "AcyclicSeedT1MismatchForcesActualSignedSourceOrRegisteredDefect"
PDEC_CLEAN = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve"
SEED_CYCLE_CUT = "AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
NEW_PRIMITIVE = "NewPrimitiveJointPayloadArtifactOutsideSignedLaneCycle"
EXTERNAL_KZ = "ExactExternalDIBFIKuznetsovNoProjectionCertificate_FOR_NONCIRCULAR_KZ_ONLY"
HIGH_MODEL = "HighSegmentModelGapAlpha043C3AnalyticLedger"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(name: str) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    path = DOCS / name
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记脚本和上游证据哈希。"""
    paths = [Path(__file__).resolve()] + [DOCS / name for name in SOURCE_FILES]
    return {
        str(path.relative_to(ROOT)): sha256(path)
        for path in paths
        if path.exists()
    }


def missing_sources() -> list[str]:
    """列出缺失依赖。"""
    return [
        f"docs/monograph/{name}"
        for name in SOURCE_FILES
        if not (DOCS / name).exists()
    ]


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
    """把 A1 source-admission 接回既有深层链并审查是否成环。"""
    post_kze = data["post_kze"]
    absorption = data["absorption"]
    precauchy = data["precauchy"]
    t1eq = data["t1eq"]
    mismatch = data["mismatch"]
    failure = data["failure"]
    downstream = data["downstream"]
    cycle = data["cycle"]
    terminal = data["terminal"]
    nonrecursive = data["nonrecursive"]
    new_joint = data["new_joint"]
    kz_nocycle = data["kz_nocycle"]

    post_kze_a1_active = (
        post_kze.get("next_direct_attack_target") == A1
        and post_kze.get("kze_direct_current_internal_route_reduced_to_source_admission") is True
    )
    source_admission_absorbed = (
        absorption.get("source_admission_reduced_to_branch_statement") is True
        and absorption.get("source_admission_standalone_global_contradiction") is False
    )
    precauchy_membership_open = (
        precauchy.get("source_lock_closed_only_after_branch_membership") is True
        and precauchy.get("acyclic_seed_to_canonical_t1_coefficient_equality_proved") is False
    )
    t1_classifier_closed = (
        t1eq.get("equality_branch_classifier_closed") is True
        and t1eq.get("canonical_equality_case_absorbed") is True
        and t1eq.get("all_mismatches_force_registered_defect_or_actual_source_proved") is False
    )
    mismatch_schema_closed = (
        mismatch.get("mismatch_forcing_schema_closed") is True
        and mismatch.get("all_mismatch_exits_closed_current_corpus") is False
    )
    failure_schema_closed = (
        failure.get("alpha_signed_lift_failure_named_return_ledger_closed") is True
        and failure.get("failure_return_exclusion_proved") is False
    )
    downstream_to_terminal = (
        downstream.get("downstream_sync_router_closed") is True
        and downstream.get("next_direct_attack_target") == PDEC_CLEAN
        and downstream.get("pdec_cap_or_internal_clean_kls_large_sieve_proved") is False
    )
    cycle_obstruction = (
        cycle.get("cycle_edges_closed") is True
        and cycle.get("cycle_returns_to_pdec_clean_kls_terminal_gate") is True
        and cycle.get("current_internal_route_is_fixed_point") is True
    )
    terminal_saturated = (
        terminal.get("internal_terminal_cycle_obstruction_closed") is True
        and terminal.get("strict_acyclic_terminal_family_proved") is False
    )
    nonrecursive_cycle = (
        nonrecursive.get("current_nonrecursive_attack_chain_synced") is True
        and nonrecursive.get("seed_coordinate_source_cycle_detected") is True
        and nonrecursive.get("current_chain_contains_nonproof_cycle") is True
    )
    new_joint_saturated = (
        new_joint.get("new_joint_current_internal_route_saturated") is True
        and new_joint.get("next_direct_attack_target")
        == "NonCircularSelfContainedKuznetsovDLSLargeSieveWithoutNCBLKSourceRootReuse"
    )
    kz_returns_to_kze = (
        kz_nocycle.get("latest_kz_nocycle_gate_active") is True
        and kz_nocycle.get("next_direct_attack_target")
        == "AcyclicKZEWellFactorableDispersionLogSavingWithoutNCBLKProjection"
    )

    macrocycle_detected = all(
        [
            post_kze_a1_active,
            source_admission_absorbed,
            precauchy_membership_open,
            t1_classifier_closed,
            mismatch_schema_closed,
            failure_schema_closed,
            downstream_to_terminal,
            cycle_obstruction,
            terminal_saturated,
            nonrecursive_cycle,
            new_joint_saturated,
            kz_returns_to_kze,
        ]
    )

    return [
        row(
            "PostKZESourceAdmissionActive",
            post_kze_a1_active,
            False,
            "最新 KZ-E direct no-projection 门把内部路线压到 A1 source-admission。",
            A1,
        ),
        row(
            "SourceAdmissionScopedNotGlobal",
            source_admission_absorbed,
            True,
            "A1 source-admission 已知只是 canonical 分支边界纪律，不是独立全局排斥原子。",
            "canonical scoped absorption; noncanonical complement still active",
        ),
        row(
            "PreCauchyMembershipGateImported",
            precauchy_membership_open,
            False,
            "要使用 canonical source，必须在 T1 证明 acyclic seed 逐点等于 canonical 系数并锁定 branch key。",
            "AcyclicSeedToCanonicalT1CoefficientEqualityAndBranchKeyLock",
        ),
        row(
            "T1EqualityClassifierImported",
            t1_classifier_closed,
            False,
            "canonical 等式 case 被 scoped 吸收；非等式 case 必须进入 mismatch forcing。",
            MISMATCH,
        ),
        row(
            "MismatchNoSilentExitButOpen",
            mismatch_schema_closed,
            False,
            "T1 mismatch 已无静默第五出口，但 signed source、命名回流排斥和 clean DLS 均未闭合。",
            "signed source package OR NamedReturnExclusion OR AcyclicWindowedDLS",
        ),
        row(
            "SignedLiftFailureReturnOnlyRegisters",
            failure_schema_closed,
            False,
            "signed lift 失败登记纪律已闭合；登记不等于排斥，下一层回到 alpha signed weight law。",
            "AlphaSignedWeightLawFromPreCauchyArithmeticIdentityLedger",
        ),
        row(
            "AlphaWeightDownstreamReturnsToTerminal",
            downstream_to_terminal,
            False,
            "alpha weight law 下游同步回 PDEC/CleanKLS 终端门和模型余量账本。",
            "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve AND model gap",
        ),
        row(
            "InternalPDECCleanKLSCycleImported",
            cycle_obstruction,
            True,
            "PDEC/CleanKLS -> KZ/NCBLK -> source entropy -> ExactUV/source table -> signed lift -> PDEC/CleanKLS 是固定点。",
            "need a nonrecursive breaker outside the cycle",
        ),
        row(
            "TerminalFamilySaturated",
            terminal_saturated,
            False,
            "strict acyclic terminal family 的 canonical、PDEC、CleanKLS 三臂均已展开但未闭合。",
            terminal.get("terminal_gap_after_router", "terminal family still open"),
        ),
        row(
            "NonrecursiveBreakerHitsSeedCycle",
            nonrecursive_cycle,
            False,
            "非递归 constructor/signed-lift 包已下钻到 seed coordinate-source 闭环。",
            SEED_CYCLE_CUT,
        ),
        row(
            "NewJointAndKZReturnToA1Gate",
            new_joint_saturated and kz_returns_to_kze,
            False,
            "旧 new-joint 内部路线饱和到 KZ no-cycle；KZ no-cycle 又压回 KZ-E direct source-admission。",
            "new primitive/external KZ input required",
        ),
        row(
            "A1PDECKZMacrocycleDetected",
            macrocycle_detected,
            True,
            "A1 source-admission 深挖后回到 PDEC/CleanKLS/new-joint/KZ/KZ-E/A1 宏循环；这只排除伪出口，不给终端矛盾。",
            "outside-cycle break input",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "仍没有从反例链与真实结构链推出全局无条件矛盾。",
            f"({SEED_CYCLE_CUT} OR {PDEC_SCOPE} OR {NEW_PRIMITIVE} OR {EXTERNAL_KZ}) AND {HIGH_MODEL} AND {RATE} AND {DSTRUCTURE}",
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造同步证书。"""
    data = {
        "post_kze": load_json("prime-matrix-strict-post-kze-direct-source-bridge-sync-router.json"),
        "absorption": load_json("prime-matrix-strict-source-admission-branch-absorption-router.json"),
        "precauchy": load_json("prime-matrix-strict-acyclic-canonical-precauchy-identity-router.json"),
        "t1eq": load_json("prime-matrix-strict-acyclic-seed-canonical-t1-equality-router.json"),
        "mismatch": load_json("prime-matrix-strict-acyclic-t1-mismatch-forcing-router.json"),
        "failure": load_json("prime-matrix-strict-alpha-signed-lift-failure-return-router.json"),
        "downstream": load_json("prime-matrix-strict-alpha-signed-weight-downstream-sync-router.json"),
        "cycle": load_json("prime-matrix-strict-self-contained-cycle-obstruction-router.json"),
        "terminal": load_json("prime-matrix-strict-acyclic-terminal-family-latest-saturation-router.json"),
        "nonrecursive": load_json("prime-matrix-strict-nonrecursive-breaker-latest-cycle-sync-router.json"),
        "new_joint": load_json("prime-matrix-strict-post-pdec-new-joint-noncycle-sync-router.json"),
        "kz_nocycle": load_json("prime-matrix-strict-post-new-joint-kz-nocycle-gate-sync-router.json"),
    }
    rows = build_rows(data)
    macrocycle_detected = next(item for item in rows if item["gate"] == "A1PDECKZMacrocycleDetected")[
        "closed"
    ]

    strict_basis = (
        f"({SEED_CYCLE_CUT} OR {PDEC_SCOPE} OR {NEW_PRIMITIVE} OR {EXTERNAL_KZ}) "
        f"AND {HIGH_MODEL} AND {RATE} AND {DSTRUCTURE}"
    )
    plain = (
        "本步把最新 KZ-E direct source-admission 前沿接入仓库中已有的 "
        "A1/T1/signed-lift/PDEC/KZ 深层链。结论是：A1 source-admission 不是尚未展开的"
        "孤立证明点；canonical 等式 case 只被 scoped 吸收，mismatch case 经 signed lift "
        "登记、alpha weight law、PDEC/CleanKLS、new-joint 与 KZ no-cycle 后回到 KZ-E/A1 门。"
        "因此当前内部路线形成非证明宏循环。继续无条件化必须提交循环外输入：无环 seed "
        "cycle-cut primitive source、direct PDEC same-set 作用域匹配、真正新的 joint/payload "
        "工件，或明确外部 no-projection KZ/DI/BFI 证书；并且仍需高段模型、RatePreservation "
        "和 DStructure/Rankin。"
    )

    return {
        "certificate_type": "prime_matrix_strict_post_source_admission_macrocycle_sync_router",
        "status": "post_source_admission_route_synced_to_a1_pdec_kz_macrocycle_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "post_kze_source_admission_active": rows[0]["closed"],
        "a1_source_admission_scoped_not_global": rows[1]["closed"],
        "t1_mismatch_no_silent_exit_imported": rows[4]["closed"],
        "signed_lift_failure_return_only_registers": rows[5]["closed"],
        "alpha_weight_downstream_returns_to_terminal": rows[6]["closed"],
        "internal_pdec_clean_kls_cycle_imported": rows[7]["closed"],
        "nonrecursive_breaker_hits_seed_cycle": rows[9]["closed"],
        "new_joint_and_kz_return_to_a1_gate": rows[10]["closed"],
        "a1_pdec_kz_macrocycle_detected": macrocycle_detected,
        "a1_source_admission_proved_as_global_contradiction": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": SEED_CYCLE_CUT,
        "parallel_break_inputs": [PDEC_SCOPE, NEW_PRIMITIVE, EXTERNAL_KZ],
        "strict_internal_basis_after_router": strict_basis,
        "decision_rows": rows,
        "missing_sources": missing_sources(),
        "source_hashes": source_hashes(),
        "plain_conclusion": plain,
    }


def write_md(cert: dict[str, Any]) -> None:
    """写 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix strict post-source-admission macrocycle 同步证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"post_kze_source_admission_active={fmt_bool(cert['post_kze_source_admission_active'])}",
        f"a1_source_admission_scoped_not_global={fmt_bool(cert['a1_source_admission_scoped_not_global'])}",
        f"t1_mismatch_no_silent_exit_imported={fmt_bool(cert['t1_mismatch_no_silent_exit_imported'])}",
        f"signed_lift_failure_return_only_registers={fmt_bool(cert['signed_lift_failure_return_only_registers'])}",
        f"alpha_weight_downstream_returns_to_terminal={fmt_bool(cert['alpha_weight_downstream_returns_to_terminal'])}",
        f"internal_pdec_clean_kls_cycle_imported={fmt_bool(cert['internal_pdec_clean_kls_cycle_imported'])}",
        f"nonrecursive_breaker_hits_seed_cycle={fmt_bool(cert['nonrecursive_breaker_hits_seed_cycle'])}",
        f"new_joint_and_kz_return_to_a1_gate={fmt_bool(cert['new_joint_and_kz_return_to_a1_gate'])}",
        f"a1_pdec_kz_macrocycle_detected={fmt_bool(cert['a1_pdec_kz_macrocycle_detected'])}",
        "a1_source_admission_proved_as_global_contradiction=false",
        "row_column_unconditional_closed=false",
        "```",
        "",
        "## 1. 宏循环链",
        "",
        "```text",
        "A1CleanBranchCanonicalSourceAdmission",
        "  -> T1 canonical equality classifier",
        "  -> mismatch forcing / signed lift failure registration",
        "  -> alpha signed weight downstream",
        "  -> PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve",
        "  -> self-contained terminal cycle / nonrecursive breaker",
        "  -> new-joint saturation",
        "  -> non-circular KZ/DLS gate",
        "  -> KZ-E direct source bridge",
        "  -> A1CleanBranchCanonicalSourceAdmission",
        "```",
        "",
        "该链说明当前内部路线是固定点，不是下降到矛盾的单向链。",
        "",
        "## 2. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in cert["decision_rows"]:
        lines.append(
            "| {gate} | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=cell(item["gate"]),
                closed=fmt_bool(item["closed"]),
                proved=fmt_bool(item["proved"]),
                meaning=cell(item["meaning"]),
                remaining=cell(item["remaining"]),
            )
        )

    lines.extend(
        [
            "",
            "## 3. 最新非循环破环基",
            "",
            "```text",
            cert["strict_internal_basis_after_router"],
            "```",
            "",
            "下一直接主攻：",
            "",
            "```text",
            cert["next_direct_attack_target"],
            "```",
            "",
            "并行破环输入：",
            "",
            "```text",
            " OR ".join(cert["parallel_break_inputs"]),
            "```",
            "",
            "## 4. 诚实边界",
            "",
            "- 本证书不证明 A1 source-admission 的全局排斥。",
            "- 本证书不证明 PDEC/CleanKLS、外部 KZ/DI/BFI、高段模型、RatePreservation 或 DStructure/Rankin。",
            "- 本证书只关闭一条当前内部路线的非循环性审查：该路线回到自身，不能作为无条件证明。",
            "",
            "## 5. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in sorted(cert["source_hashes"].items()):
        lines.append(f"| `{path}` | `{digest}` |")

    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """入口。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    cert = build_certificate()
    OUT_LEDGER.write_text(json.dumps(cert, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    OUT_JSON.write_text(json.dumps(cert, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    write_md(cert)
    print(f"wrote {OUT_JSON.relative_to(ROOT)}")
    print(f"wrote {OUT_MD.relative_to(ROOT)}")
    print(f"wrote {OUT_LEDGER.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
