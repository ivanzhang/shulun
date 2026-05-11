#!/usr/bin/env python3
"""生成 strict 内部路线全局循环前沿同步证书。

用法示例：
  python3 experiments/prime_matrix_strict_global_internal_cycle_frontier_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-global-internal-cycle-frontier-sync-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"
OUT_JSON = MONOGRAPH / "prime-matrix-strict-global-internal-cycle-frontier-sync-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-global-internal-cycle-frontier-sync-router.md"

NONCANONICAL_LEGAL = "NoncanonicalFullSComplementLegalClosureMode"
ACTUAL_SOURCE_BRIDGE = "ActualA1FullSSourceLockOrStrengthenedAntiAtomTheoremInput"
MOVING_ATOM = "ActualNoncanonicalCleanCoreMovingAtomExclusion"
NEW_SOURCE_ENTROPY = "NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem"
INDEPENDENT_SOURCE_ENTROPY = (
    "IndependentNonterminalProofOfNewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem"
)
ROW_TABLE = "RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands"
SIGNED_SOURCE_BREAKER = "NoncircularPreCauchySignedCoefficientEmissionKernelForActualNoncanonicalPrimitiveRows"
TERMINAL_DESCENT = "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate"
POINTWISE_KERNEL_TABLE = "PointwiseSameFormalUnitPrimitiveAlphaDeltaKernelTableWithNonzeroRankCertificate"
KERNEL_IDENTITY = "SameFormalUnitPreCauchyAlphaDeltaKernelIdentityWithSignedPhiAndFiberDispersion"
CANONICAL_EXACT = "AcyclicCanonicalExactSameSetPromotionCertificate"
FULLS_KLS_EXT = "AcceptFullSKLSExtExternalContract"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    "prime-matrix-strict-joint-alpha-signed-source-fixed-point-sync-router.json",
    "prime-matrix-strict-terminal-leaf-firewall-current-instance-router.json",
    "prime-matrix-strict-noncanonical-legal-closure-mode-router.json",
    "prime-matrix-strict-actual-source-bridge-terminal-obstruction-router.json",
    "prime-matrix-strict-source-admission-branch-absorption-router.json",
    "prime-matrix-strict-exact-entropy-source-law-firewall-router.json",
    "prime-matrix-strict-new-actual-source-entropy-fixed-point-firewall-router.json",
    "prime-matrix-strict-independent-nonterminal-source-entropy-atomization-router.json",
    "prime-matrix-strict-signed-source-fixed-point-breaker-router.json",
    "prime-matrix-strict-nonrecursive-constructor-signed-lift-breaker-router.json",
    "prime-matrix-strict-same-formal-unit-kernel-identity-attack-router.json",
    "prime-matrix-strict-pointwise-primitive-kernel-table-router.json",
    "prime-matrix-fulls-kls-ext-acceptance-match-audit.json",
]


def load_json(name: str) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空对象。"""
    path = MONOGRAPH / name
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """写出小写布尔。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def source_hashes() -> dict[str, str]:
    """汇总实际存在的依赖哈希。"""
    return {
        f"docs/monograph/{name}": sha256(MONOGRAPH / name)
        for name in SOURCE_FILES
        if (MONOGRAPH / name).exists()
    }


def missing_sources() -> list[str]:
    """列出缺失依赖，缺失不会被解释为证明。"""
    return [
        f"docs/monograph/{name}"
        for name in SOURCE_FILES
        if not (MONOGRAPH / name).exists()
    ]


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def internal_cycle_edges() -> list[dict[str, str]]:
    """记录当前内部路线的闭环。"""
    return [
        {"from": TERMINAL_DESCENT, "to": "TerminalLeafFirewallInputs_OR_CanonicalLock"},
        {"from": "TerminalLeafFirewallInputs_OR_CanonicalLock", "to": NONCANONICAL_LEGAL},
        {"from": NONCANONICAL_LEGAL, "to": ACTUAL_SOURCE_BRIDGE},
        {"from": ACTUAL_SOURCE_BRIDGE, "to": "A1CleanBranchCanonicalSourceAdmission OR " + MOVING_ATOM},
        {"from": "A1CleanBranchCanonicalSourceAdmission", "to": MOVING_ATOM},
        {"from": MOVING_ATOM, "to": NEW_SOURCE_ENTROPY},
        {"from": NEW_SOURCE_ENTROPY, "to": INDEPENDENT_SOURCE_ENTROPY},
        {"from": INDEPENDENT_SOURCE_ENTROPY, "to": "PreTerminalActualFullSFactorSupportCapacityTheorem"},
        {"from": "PreTerminalActualFullSFactorSupportCapacityTheorem", "to": "PreTerminalExactUVFiberAbsoluteMassDispersionTheorem"},
        {"from": "PreTerminalExactUVFiberAbsoluteMassDispersionTheorem", "to": "ActualPreCauchySourceDomainRankAndExactUVNoCollapseLedger"},
        {"from": "ActualPreCauchySourceDomainRankAndExactUVNoCollapseLedger", "to": ROW_TABLE},
        {"from": ROW_TABLE, "to": SIGNED_SOURCE_BREAKER},
        {"from": SIGNED_SOURCE_BREAKER, "to": KERNEL_IDENTITY},
        {"from": KERNEL_IDENTITY, "to": POINTWISE_KERNEL_TABLE},
        {"from": POINTWISE_KERNEL_TABLE, "to": ROW_TABLE},
        {"from": ROW_TABLE, "to": TERMINAL_DESCENT},
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """同步各路由结论并判定最新真正前沿。"""
    joint = data["joint"]
    leaf = data["leaf"]
    legal = data["legal"]
    bridge = data["bridge"]
    source_admission = data["source_admission"]
    entropy_firewall = data["entropy_firewall"]
    entropy_fixed = data["entropy_fixed"]
    independent_entropy = data["independent_entropy"]
    signed_breaker = data["signed_breaker"]
    nonrecursive_breaker = data["nonrecursive_breaker"]
    kernel_identity = data["kernel_identity"]
    pointwise = data["pointwise"]
    external = data["external"]

    return [
        row(
            "TerminalRouteReturnsToActualSourceBridge",
            joint.get("next_direct_attack_target") == TERMINAL_DESCENT
            and leaf.get("terminal_gap_after_current_instance_router")
            == "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR NoncanonicalFullSComplementLegalClosureMode"
            and legal.get("strict_self_contained_terminal_after_router")
            == "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR ActualA1FullSSourceLockOrStrengthenedAntiAtomTheoremInput",
            True,
            "terminal descent 叶子压缩后，活动 noncanonical 叶子回到 actual-source bridge。",
            ACTUAL_SOURCE_BRIDGE,
        ),
        row(
            "ActualSourceBridgeReturnsToSourceEntropy",
            bridge.get("strict_self_contained_terminal_after_router")
            == "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR A1CleanBranchCanonicalSourceAdmission OR ActualNoncanonicalCleanCoreMovingAtomExclusion"
            and source_admission.get("source_admission_absorbed_from_active_or") is True
            and entropy_firewall.get("strict_self_contained_terminal_after_router")
            == "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem",
            True,
            "A1 source admission 只是 scoped 分支，活动 noncanonical 路线回到 moving atom / new actual-source entropy。",
            NEW_SOURCE_ENTROPY,
        ),
        row(
            "SourceEntropyReturnsToIndependentNonterminalInput",
            entropy_fixed.get("next_direct_attack_target") == INDEPENDENT_SOURCE_ENTROPY
            and independent_entropy.get("next_direct_attack_target")
            == "PreTerminalActualFullSFactorSupportCapacityTheorem",
            True,
            "ExactUV/pair/terminal/canonical 旧脊柱形成固定点，合法内部推进必须走独立非终端源熵输入。",
            INDEPENDENT_SOURCE_ENTROPY,
        ),
        row(
            "IndependentSourceEntropyHitsSignedSourceFixedPoint",
            signed_breaker.get("current_internal_route_is_signed_source_fixed_point") is True
            and signed_breaker.get("next_direct_attack_target") == SIGNED_SOURCE_BREAKER,
            True,
            "source-domain/rank/row-level 下钻已登记为 signed-source 固定点。",
            SIGNED_SOURCE_BREAKER,
        ),
        row(
            "NonrecursiveBreakerReducesToKernelIdentity",
            nonrecursive_breaker.get("next_direct_attack_target") == KERNEL_IDENTITY
            and nonrecursive_breaker.get("same_formal_unit_kernel_identity_proved") is False,
            True,
            "非递归 constructor/signed-lift 破环包的诚实核心是同 formal-unit pre-Cauchy alpha/delta 核恒等式。",
            KERNEL_IDENTITY,
        ),
        row(
            "KernelIdentityReducesToPointwisePrimitiveTable",
            kernel_identity.get("next_direct_attack_target") == POINTWISE_KERNEL_TABLE
            and pointwise.get("pointwise_primitive_kernel_table_proved") is False,
            True,
            "核恒等式本身等价于先提交逐 primitive row 的同 formal-unit alpha/delta 核表。",
            POINTWISE_KERNEL_TABLE,
        ),
        row(
            "PointwisePrimitiveTableCurrentlyLoopsToRowLevel",
            pointwise.get("next_direct_attack_target") == "AlphaRowAnchorPhaseEmissionFormulaLedger"
            and signed_breaker.get("row_level_clean_core_origin_generation_table_proved") is False,
            True,
            "逐点核表的三输入继续展开会回到 row-level signed-source 固定点；不能把现有内部拆分当证明。",
            POINTWISE_KERNEL_TABLE,
        ),
        row(
            "ExternalFullSKLSExtLaneAcceptedOnlyAsExternal",
            external.get("external_math_lane_closed_after_acceptance") is True,
            True,
            "FullS-KLS-ext 可作为外部黑箱合同关闭 noncanonical full-S 数学线，但不是 strict 自足内部证明。",
            f"{FULLS_KLS_EXT} AND {DSTRUCTURE}",
        ),
        row(
            "PointwiseKernelTableCurrentCorpusProved",
            False,
            False,
            "当前材料没有给出不自回流的逐 primitive alpha/delta 核表。",
            POINTWISE_KERNEL_TABLE,
        ),
        row(
            "RowColumnUnconditionalClosureCurrentCorpusProved",
            False,
            False,
            "内部路线仍是闭环；外部合同即使接受，也还需 DStructure/Rankin 独立验收。",
            f"({POINTWISE_KERNEL_TABLE} OR {FULLS_KLS_EXT}) AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造全局内部循环同步证书。"""
    data = {
        "joint": load_json("prime-matrix-strict-joint-alpha-signed-source-fixed-point-sync-router.json"),
        "leaf": load_json("prime-matrix-strict-terminal-leaf-firewall-current-instance-router.json"),
        "legal": load_json("prime-matrix-strict-noncanonical-legal-closure-mode-router.json"),
        "bridge": load_json("prime-matrix-strict-actual-source-bridge-terminal-obstruction-router.json"),
        "source_admission": load_json("prime-matrix-strict-source-admission-branch-absorption-router.json"),
        "entropy_firewall": load_json("prime-matrix-strict-exact-entropy-source-law-firewall-router.json"),
        "entropy_fixed": load_json("prime-matrix-strict-new-actual-source-entropy-fixed-point-firewall-router.json"),
        "independent_entropy": load_json("prime-matrix-strict-independent-nonterminal-source-entropy-atomization-router.json"),
        "signed_breaker": load_json("prime-matrix-strict-signed-source-fixed-point-breaker-router.json"),
        "nonrecursive_breaker": load_json("prime-matrix-strict-nonrecursive-constructor-signed-lift-breaker-router.json"),
        "kernel_identity": load_json("prime-matrix-strict-same-formal-unit-kernel-identity-attack-router.json"),
        "pointwise": load_json("prime-matrix-strict-pointwise-primitive-kernel-table-router.json"),
        "external": load_json("prime-matrix-fulls-kls-ext-acceptance-match-audit.json"),
    }
    rows = build_rows(data)
    return {
        "certificate_type": "prime_matrix_strict_global_internal_cycle_frontier_sync_router",
        "status": "strict_internal_terminal_source_cycle_synced_to_pointwise_kernel_table_or_external_fulls_kls_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "internal_terminal_source_cycle_detected": True,
        "existing_internal_route_counts_as_proof": False,
        "pointwise_primitive_kernel_table_proved": False,
        "external_fulls_kls_ext_accepted_as_external_blackbox": data["external"].get(
            "external_math_lane_closed_after_acceptance"
        )
        is True,
        "dstructure_rankin_independent_acceptance_completed": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "latest_strict_internal_break_input": POINTWISE_KERNEL_TABLE,
        "conditional_external_break_input": FULLS_KLS_EXT,
        "final_gate_still_independent": DSTRUCTURE,
        "next_direct_attack_target": POINTWISE_KERNEL_TABLE,
        "strict_internal_basis_after_router": f"{POINTWISE_KERNEL_TABLE} AND {DSTRUCTURE}",
        "external_conditional_basis_after_router": f"{FULLS_KLS_EXT} AND {DSTRUCTURE}",
        "cycle_edges": internal_cycle_edges(),
        "rows": rows,
        "source_hashes": source_hashes(),
        "missing_sources": missing_sources(),
        "plain_conclusion": (
            "当前 strict 内部路线已经形成 terminal-source 大闭环：终端叶子回到 actual-source bridge，"
            "actual-source bridge 回到 new actual-source entropy，source entropy 下钻到 signed-source 固定点，"
            "固定点又回到 terminal descent。这个闭环不能作为证明。若坚持严格自足，真正破环输入必须是"
            f"`{POINTWISE_KERNEL_TABLE}`；若接受外部黑箱，则 FullS-KLS-ext 可关闭外部数学线，但仍需"
            "DStructure/Rankin 独立验收。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown。"""
    lines = [
        "# Prime Matrix strict 内部终端/source 大循环前沿同步路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"internal_terminal_source_cycle_detected={fmt_bool(result['internal_terminal_source_cycle_detected'])}",
        f"existing_internal_route_counts_as_proof={fmt_bool(result['existing_internal_route_counts_as_proof'])}",
        f"pointwise_primitive_kernel_table_proved={fmt_bool(result['pointwise_primitive_kernel_table_proved'])}",
        f"external_fulls_kls_ext_accepted_as_external_blackbox={fmt_bool(result['external_fulls_kls_ext_accepted_as_external_blackbox'])}",
        f"dstructure_rankin_independent_acceptance_completed={fmt_bool(result['dstructure_rankin_independent_acceptance_completed'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 闭环链条",
        "",
        "| from | to |",
        "| --- | --- |",
    ]
    for edge in result["cycle_edges"]:
        lines.append(
            "| `{}` | `{}` |".format(
                table_cell(edge["from"]),
                table_cell(edge["to"]),
            )
        )
    lines.extend(
        [
            "",
            "## 2. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
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
            "## 3. 最新前沿",
            "",
            "严格自足首攻：",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "严格自足基：",
            "",
            "```text",
            result["strict_internal_basis_after_router"],
            "```",
            "",
            "外部条件基：",
            "",
            "```text",
            result["external_conditional_basis_after_router"],
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
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
