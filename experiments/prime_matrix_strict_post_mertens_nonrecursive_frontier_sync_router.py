#!/usr/bin/env python3
"""生成 strict post-Mertens 非递归前沿同步证书。

用法示例：
  python3 experiments/prime_matrix_strict_post_mertens_nonrecursive_frontier_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-post-mertens-nonrecursive-frontier-sync-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-post-mertens-nonrecursive-frontier-sync-router.json"
OUT_MD = DOCS / "prime-matrix-strict-post-mertens-nonrecursive-frontier-sync-router.md"

PDEC_KLS_PACKET = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_rate_bearing_packet"
PDEC_KLS = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
CANONICAL_LOCK = "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary"
WINDOWED_DLS = "AcyclicWindowedKloostermanDLSInternalEstimate"
SOURCE_ENTROPY = "NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem"
BREAKER = "NonrecursiveActualNoncanonicalPreCauchyConstructorRuleAndSignedLiftPackage"
KERNEL = "SameFormalUnitPreCauchyAlphaDeltaKernelIdentityWithSignedPhiAndFiberDispersion"
SCOPE_MATCH = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
KZ_DLS = "SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks"
MODEL_GAP = "ExplicitModelGapAndFiniteDPRCLedger"

SOURCE_FILES = [
    "prime-matrix-strict-rate-bearing-tail-mertens-latest-sync-router.json",
    "prime-matrix-strict-rate-bearing-frontier-drilldown-router.json",
    "prime-matrix-strict-mainline-canonical-lock-drilldown-router.json",
    "prime-matrix-strict-rate-bearing-terminal-recurrence-firewall-router.json",
    "prime-matrix-strict-canonical-lock-branch-absorption-router.json",
    "prime-matrix-strict-self-contained-cycle-obstruction-router.json",
    "prime-matrix-strict-nonrecursive-constructor-signed-lift-breaker-router.json",
    "prime-matrix-strict-alpha-row-formula-terminal-frontier-sync-router.json",
    "prime-matrix-strict-pdec-clean-kls-terminal-hardpoint-router.json",
    "prime-matrix-dstructure-rankin-promotion-acceptance-router.json",
]


def load_json(name: str) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空对象以暴露同步缺口。"""
    path = DOCS / name
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def source_hashes() -> dict[str, str]:
    """登记本同步证书引用的证据哈希。"""
    hashes: dict[str, str] = {}
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            hashes[f"docs/monograph/{name}"] = sha256(path)
    return hashes


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_result() -> dict[str, Any]:
    """合并最新主线证书，给出 post-Mertens 的真正非递归前沿。"""
    mertens = load_json("prime-matrix-strict-rate-bearing-tail-mertens-latest-sync-router.json")
    rate_frontier = load_json("prime-matrix-strict-rate-bearing-frontier-drilldown-router.json")
    mainline = load_json("prime-matrix-strict-mainline-canonical-lock-drilldown-router.json")
    recurrence = load_json("prime-matrix-strict-rate-bearing-terminal-recurrence-firewall-router.json")
    canonical_absorb = load_json("prime-matrix-strict-canonical-lock-branch-absorption-router.json")
    cycle = load_json("prime-matrix-strict-self-contained-cycle-obstruction-router.json")
    breaker = load_json("prime-matrix-strict-nonrecursive-constructor-signed-lift-breaker-router.json")
    alpha_frontier = load_json("prime-matrix-strict-alpha-row-formula-terminal-frontier-sync-router.json")
    pdec_split = load_json("prime-matrix-strict-pdec-clean-kls-terminal-hardpoint-router.json")
    dstructure = load_json("prime-matrix-dstructure-rankin-promotion-acceptance-router.json")

    mertens_removed = (
        mertens.get("strict_self_contained_mertens_tail_proved") is True
        and mertens.get("next_direct_attack_target") == PDEC_KLS_PACKET
    )
    rate_packet_active = (
        rate_frontier.get("next_direct_attack_target") == PDEC_KLS_PACKET
        and rate_frontier.get("rate_bearing_moving_atom_packet_exclusion_proved") is False
    )
    mainline_terminal_reduced = (
        mainline.get("terminal_family_reduced_back_to_canonical_lock_or_windowed_dls") is True
        and mainline.get("acyclic_terminal_canonical_lock_proved") is False
        and mainline.get("acyclic_windowed_dls_proved") is False
    )
    terminal_recurrence = (
        recurrence.get("terminal_recurrence_firewall_closed") is True
        and recurrence.get("terminal_route_returns_to_source_entropy_target") is True
    )
    canonical_scoped = (
        canonical_absorb.get("canonical_lock_branch_absorption_closed") is True
        and canonical_absorb.get("strict_active_noncanonical_terminal_after_absorption") == SOURCE_ENTROPY
    )
    cycle_fixed = (
        cycle.get("current_internal_route_is_fixed_point") is True
        and cycle.get("next_direct_attack_target") == BREAKER
    )
    breaker_to_kernel = (
        breaker.get("current_route_still_fixed_point_without_new_kernel_identity") is True
        and breaker.get("next_direct_attack_target") == KERNEL
    )
    alpha_local_recycles = (
        alpha_frontier.get("alpha_row_formula_local_frontier_synced_to_terminal") is True
        and alpha_frontier.get("next_direct_attack_target") == PDEC_KLS
    )
    pdec_split_open = (
        pdec_split.get("terminal_split_router_closed") is True
        and pdec_split.get("pdec_cap_or_internal_clean_kls_large_sieve_proved") is False
    )
    dstructure_open = (
        dstructure.get("promotion_package_boundary_closed") is True
        and dstructure.get("promotion_package_independently_accepted") is False
    )

    sync_closed = all(
        [
            mertens_removed,
            rate_packet_active,
            mainline_terminal_reduced,
            terminal_recurrence,
            canonical_scoped,
            cycle_fixed,
            breaker_to_kernel,
            alpha_local_recycles,
            pdec_split_open,
            dstructure_open,
        ]
    )

    rows = [
        row(
            "MertensTailRemoved",
            mertens_removed,
            True,
            "速率尾段的 theta/PNT 与 Meissel-Mertens B1 自足输入已闭合，解析尾段不再是活动硬点。",
            PDEC_KLS_PACKET,
        ),
        row(
            "RateBearingPacketStillActive",
            rate_packet_active,
            False,
            "moving-atom 终端包排斥仍未证明，且需要保存 log-power 速率字段。",
            f"{PDEC_KLS_PACKET} AND {RATE}",
        ),
        row(
            "TerminalTagExpansionIsNotProof",
            mainline_terminal_reduced and terminal_recurrence,
            True,
            "PDEC/CleanKLS 终端标签继续展开会回到 canonical-lock 或 actual-source 熵目标，形成回流防火墙。",
            f"{CANONICAL_LOCK} OR {WINDOWED_DLS} OR {SOURCE_ENTROPY}",
        ),
        row(
            "CanonicalLockAbsorbedAsScopedCase",
            canonical_scoped,
            True,
            "canonical-lock 若五项 exact same-set 证书齐全，只是 canonical-source scoped 晋级；证书缺失则不可调用。",
            SOURCE_ENTROPY,
        ),
        row(
            "InternalRouteFixedPointDetected",
            cycle_fixed,
            True,
            "从 PDEC/CleanKLS 出发经 KZ/NCBLK、source entropy、ExactUV/source table、alpha signed lift 又回同一终端门。",
            BREAKER,
        ),
        row(
            "BreakerReducedToKernelIdentity",
            breaker_to_kernel,
            False,
            "六腿 constructor/signed-lift 破环包不能碎片化逐腿证明；当前唯一真正破环原子是同 formal unit pre-Cauchy 核恒等式。",
            KERNEL,
        ),
        row(
            "AlphaLocalFrontierRecycles",
            alpha_local_recycles,
            True,
            "alpha row 局部 unsigned/signed-lift 分支已同步回终端门，不能作为独立非循环出口。",
            PDEC_KLS,
        ),
        row(
            "DirectTerminalParallelArmsStillOpen",
            pdec_split_open,
            False,
            "直接终端手臂仍可并行攻，但当前均未证明：PDEC 需同集作用域匹配，CleanKLS 需自足 KZ/DLS 大筛。",
            f"{SCOPE_MATCH} OR {KZ_DLS}",
        ),
        row(
            "RatePreservationStillOpen",
            False,
            False,
            "即使给出某个终端排斥，也必须证明速率型 packet 到 moving atom 的 log-power 阈值保持。",
            RATE,
        ),
        row(
            "DStructureGateStillOpen",
            dstructure_open,
            False,
            "DStructure/Tail-log4/finite Rankin 晋级包边界已命名，但仍未独立接受。",
            DSTRUCTURE,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "当前只完成最新前沿同步和伪出口删除；尚未得到排除早期零行反例链的终端矛盾。",
            f"{KERNEL} AND {RATE} AND {DSTRUCTURE}",
        ),
    ]

    strict_active_basis = f"{KERNEL} AND {RATE} AND {DSTRUCTURE}"
    parallel_direct_basis = (
        f"({SCOPE_MATCH} OR {KZ_DLS}) AND {MODEL_GAP} AND {RATE} AND {DSTRUCTURE}"
    )

    return {
        "certificate_type": "prime_matrix_strict_post_mertens_nonrecursive_frontier_sync_router",
        "status": "post_mertens_frontier_synced_to_kernel_identity_rate_dstructure_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "post_mertens_nonrecursive_frontier_sync_closed": sync_closed,
        "mertens_tail_removed_from_active_basis": mertens_removed,
        "terminal_tag_expansion_rejected_as_proof": mainline_terminal_reduced and terminal_recurrence,
        "canonical_lock_absorbed_as_scoped_case": canonical_scoped,
        "internal_route_fixed_point_detected": cycle_fixed,
        "same_formal_unit_kernel_identity_proved": False,
        "rate_preservation_ledger_proved": False,
        "dstructure_independent_gate_closed": False,
        "direct_terminal_parallel_arms_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "strict_active_basis_after_sync": strict_active_basis,
        "parallel_direct_terminal_basis": parallel_direct_basis,
        "next_direct_attack_target": KERNEL,
        "parallel_attack_targets": [SCOPE_MATCH, KZ_DLS, RATE, DSTRUCTURE],
        "kernel_identity_role": (
            "该核恒等式必须在同一 formal unit、Cauchy/dispersion/terminal extraction 之前，"
            "一次性给出 actual noncanonical alpha/delta primitive constructor、signed source measure、"
            "pre-Cauchy 权重律、Phi 推前、变差预算和 exact-UV fiber 分散；不得回调 PDEC/CleanKLS、"
            "canonical scoped case、source entropy 自身或早期零行 unsigned cover。"
        ),
        "if_kernel_not_proved": (
            "若该核恒等式不给出，当前内部自足链只能回到 PDEC/CleanKLS 固定点；"
            "不能声明行/列命题无条件自足闭合。"
        ),
        "rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "Mertens/解析尾段已移出活动剩余后，不能再把 `PDEC_CAP_OR_INTERNAL_CleanKLS...` "
            "当作可直接闭合的黑箱标签。现有证书显示：终端标签展开会回到 canonical-lock/source entropy，"
            "canonical-lock 又只是 scoped case；继续沿内部链下钻会形成 PDEC/CleanKLS 固定点。"
            "因此最新真正最窄自足主攻点同步为 "
            "`SameFormalUnitPreCauchyAlphaDeltaKernelIdentityWithSignedPhiAndFiberDispersion`，"
            "并行保留 RatePreservation 与 DStructure 验收门；行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix strict post-Mertens 非递归前沿同步证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"same_theorem_target_preserved={fmt_bool(result['same_theorem_target_preserved'])}",
        f"no_theorem_switch={fmt_bool(result['no_theorem_switch'])}",
        f"post_mertens_nonrecursive_frontier_sync_closed={fmt_bool(result['post_mertens_nonrecursive_frontier_sync_closed'])}",
        f"mertens_tail_removed_from_active_basis={fmt_bool(result['mertens_tail_removed_from_active_basis'])}",
        f"terminal_tag_expansion_rejected_as_proof={fmt_bool(result['terminal_tag_expansion_rejected_as_proof'])}",
        f"canonical_lock_absorbed_as_scoped_case={fmt_bool(result['canonical_lock_absorbed_as_scoped_case'])}",
        f"internal_route_fixed_point_detected={fmt_bool(result['internal_route_fixed_point_detected'])}",
        f"same_formal_unit_kernel_identity_proved={fmt_bool(result['same_formal_unit_kernel_identity_proved'])}",
        f"rate_preservation_ledger_proved={fmt_bool(result['rate_preservation_ledger_proved'])}",
        f"dstructure_independent_gate_closed={fmt_bool(result['dstructure_independent_gate_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 同步后严格基",
        "",
        "```text",
        result["strict_active_basis_after_sync"],
        "```",
        "",
        "并行直接终端手臂：",
        "",
        "```text",
        result["parallel_direct_terminal_basis"],
        "```",
        "",
        "## 2. 判定表",
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
            "## 3. 核恒等式角色",
            "",
            result["kernel_identity_role"],
            "",
            result["if_kernel_not_proved"],
            "",
            "## 4. 下一步",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    """写出 JSON 和 Markdown 证书。"""
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
