#!/usr/bin/env python3
"""生成 strict descent 叶子防火墙与 alpha 回流同步证书。

用法示例：
  python3 experiments/prime_matrix_strict_descent_leaf_firewall_alpha_return_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-descent-leaf-firewall-alpha-return-sync-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-descent-leaf-firewall-alpha-return-sync-router.json"
OUT_MD = DOCS / "prime-matrix-strict-descent-leaf-firewall-alpha-return-sync-router.md"

DESCENT = "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate"
CANONICAL_LOCK = "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary"
LEAF_INPUTS = (
    "AcyclicTerminalLeafFirewallInputs"
    "[FutureExplicitPrimitivePDECSchema_if_new OR "
    "FutureExplicitSparsePacketExtractorSchema_if_new OR "
    "NoncanonicalFullSComplementLegalClosureMode]"
)
NONCANONICAL_MODE = "NoncanonicalFullSComplementLegalClosureMode"
ACTUAL_SOURCE_BRIDGE = "ActualA1FullSSourceLockOrStrengthenedAntiAtomTheoremInput"
INDEPENDENT_ACTUAL_SOURCE_BRIDGE = (
    "IndependentActualSourceBridgeNotFactoredThroughAlphaReturn"
)
POINTWISE_KERNEL = "PointwiseSameFormalUnitPrimitiveAlphaDeltaKernelTableWithNonzeroRankCertificate"
ALPHA_FORMULA = "AlphaRowAnchorPhaseEmissionFormulaLedger"
GLOBAL_TERMINAL = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve"
MODEL_LEDGER = "ExplicitModelGapAndFiniteDPRCLedger"
DSTRUCTURE_GATE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
HIGH_TAIL = (
    "SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000 AND "
    "SelfContainedMeisselMertensConstantIntervalLedgerAt20000"
)
SELF_CONTAINED_DSTRUCTURE = "SelfContainedDStructureTailLog4FiniteRankinReplacementPackage"

SOURCE_FILES = [
    "prime-matrix-strict-alpha-terminal-to-acyclic-cycle-guard-sync-router.json",
    "prime-matrix-strict-acyclic-terminal-descent-firewall-router.json",
    "prime-matrix-strict-terminal-descent-to-pointwise-kernel-sync-router.json",
    "prime-matrix-strict-alpha-row-formula-terminal-frontier-sync-router.json",
    "prime-matrix-strict-terminal-leaf-firewall-current-instance-router.json",
    "prime-matrix-strict-noncanonical-legal-closure-mode-router.json",
    "prime-matrix-strict-canonical-lock-branch-absorption-router.json",
]


def load_json(name: str) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空对象。"""
    path = DOCS / name
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算证据文件哈希，便于审稿追踪。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def source_hashes() -> dict[str, str]:
    """登记本证书读取到的来源文件哈希。"""
    result: dict[str, str] = {}
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = sha256(path)
    return result


def make_row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def backedge_chain() -> list[dict[str, str]]:
    """列出旧 descent 下钻经 alpha 回到终端门的回边链。"""
    return [
        {"from": DESCENT, "to": "TerminalLeafFirewallInputs_OR_CanonicalLock"},
        {"from": "TerminalLeafFirewallInputs_OR_CanonicalLock", "to": f"{NONCANONICAL_MODE}_OR_CanonicalLock"},
        {"from": NONCANONICAL_MODE, "to": ACTUAL_SOURCE_BRIDGE},
        {"from": ACTUAL_SOURCE_BRIDGE, "to": "NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem"},
        {"from": "NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem", "to": "PreTerminalActualFullSFactorSupportCapacityTheorem"},
        {"from": "PreTerminalActualFullSFactorSupportCapacityTheorem", "to": "NonterminalExactUVFiberAperiodicityEstimateForActualPreCauchySource"},
        {"from": "NonterminalExactUVFiberAperiodicityEstimateForActualPreCauchySource", "to": "ActualPreCauchySourceDomainRankAndExactUVNoCollapseLedger"},
        {"from": "ActualPreCauchySourceDomainRankAndExactUVNoCollapseLedger", "to": POINTWISE_KERNEL},
        {"from": POINTWISE_KERNEL, "to": ALPHA_FORMULA},
        {"from": ALPHA_FORMULA, "to": f"{GLOBAL_TERMINAL} AND {MODEL_LEDGER}"},
        {"from": GLOBAL_TERMINAL, "to": f"{CANONICAL_LOCK} OR {DESCENT}"},
    ]


def build_rows(
    alpha_cycle: dict[str, Any],
    descent_firewall: dict[str, Any],
    descent_to_kernel: dict[str, Any],
    alpha_frontier: dict[str, Any],
    leaf_firewall: dict[str, Any],
    noncanonical: dict[str, Any],
    canonical_absorb: dict[str, Any],
) -> list[dict[str, Any]]:
    """同步 descent 叶子防火墙与 alpha 回流，压出当前真正剩余。"""
    descent_schema_closed = descent_firewall.get("terminal_return_well_founded_descent_schema_closed") is True
    hidden_cycle_removed = descent_firewall.get("hidden_terminal_cycle_removed") is True
    leaf_inputs_open = descent_firewall.get("terminal_leaf_firewall_inputs_proved_or_accepted") is False
    old_route_to_alpha = (
        descent_to_kernel.get("next_direct_attack_target") == ALPHA_FORMULA
        or descent_to_kernel.get("pointwise_kernel_table_is_common_variable_table") is True
    )
    alpha_returns_terminal = (
        alpha_frontier.get("alpha_row_formula_local_frontier_synced_to_terminal") is True
        and alpha_cycle.get("alpha_terminal_to_acyclic_cycle_guard_sync_router_closed") is True
    )
    alpha_not_descent = old_route_to_alpha and alpha_returns_terminal
    leaf_current_reduced = leaf_firewall.get("current_leaf_firewall_active_basis_reduced") is True
    noncanonical_to_actual = (
        noncanonical.get("strict_self_contained_terminal_after_router")
        == f"{CANONICAL_LOCK} OR {ACTUAL_SOURCE_BRIDGE}"
    )
    canonical_scoped_only = (
        canonical_absorb.get("canonical_lock_branch_absorption_closed") is True
        and canonical_absorb.get("acyclic_terminal_canonical_lock_proved") is False
    )
    sync_closed = all(
        [
            descent_schema_closed,
            hidden_cycle_removed,
            leaf_inputs_open,
            old_route_to_alpha,
            alpha_returns_terminal,
            leaf_current_reduced,
            noncanonical_to_actual,
            canonical_scoped_only,
        ]
    )

    return [
        make_row(
            "CounterexampleBranchGuardPreserved",
            True,
            True,
            "本同步仍只在早期零行反例链内工作，不使用真实样本缺席或数值前沿清零替代假设链证明。",
            "direct_unconditional_contradiction_found=false。",
        ),
        make_row(
            "DescentFirewallSchemaImported",
            descent_schema_closed and hidden_cycle_removed,
            True,
            "无隐藏终端循环已由下降防火墙 schema 删除；固定 PDEC、new-layer、cofactor 与 SAE/ColumnCRT 回流已命名。",
            LEAF_INPUTS,
        ),
        make_row(
            "TerminalLeafInputsStillOpen",
            leaf_inputs_open,
            False,
            "下降防火墙只关掉无名循环，不排斥叶子防火墙输入。",
            f"{CANONICAL_LOCK} OR {LEAF_INPUTS}",
        ),
        make_row(
            "OldPointwiseAlphaRouteDetected",
            old_route_to_alpha,
            False,
            "旧的 descent 下钻链把 actual-source/rank 包继续展开到逐点 alpha/delta 核表和 alpha row formula。",
            f"{POINTWISE_KERNEL} -> {ALPHA_FORMULA}",
        ),
        make_row(
            "AlphaRouteReturnsToTerminal",
            alpha_returns_terminal,
            False,
            "alpha row formula 的局部前沿已同步回 PDEC-CAP/CleanKLS，并被 acyclic 循环守卫判为终端回流。",
            f"{GLOBAL_TERMINAL} -> {CANONICAL_LOCK} OR {DESCENT}",
        ),
        make_row(
            "PointwiseAlphaRouteCannotBeProgressMeasure",
            alpha_not_descent,
            True,
            "若把旧 pointwise/alpha 展开当作 well-founded descent，它的终端又回到同一终端家族，故只能记为回边，不能记为严格下降量。",
            "必须改攻叶子输入或提交新的严格下降势函数。",
        ),
        make_row(
            "CurrentLeafFirewallInstanceReduced",
            leaf_current_reduced,
            True,
            "当前已物化 PDEC/sparse 前沿被清到准入纪律后，活动叶子从 future schema 压到 noncanonical full-S 或 canonical-lock。",
            f"{CANONICAL_LOCK} OR {NONCANONICAL_MODE}",
        ),
        make_row(
            "NoncanonicalModeFilteredToActualSourceBridge",
            noncanonical_to_actual,
            False,
            "严格自足线过滤外部 FullS-KLS 与 generic WFD 后，noncanonical 叶子压到 actual-source 锁定或强化反原子。",
            f"{CANONICAL_LOCK} OR {ACTUAL_SOURCE_BRIDGE}",
        ),
        make_row(
            "CanonicalLockScopedButNotGlobal",
            canonical_scoped_only,
            False,
            "canonical-lock 若证书齐备只进入 scoped canonical case；证书缺失时不可调用，不能作为 unrestricted noncanonical 矛盾。",
            CANONICAL_LOCK,
        ),
        make_row(
            "IndependentActualSourceBridgeRequired",
            alpha_not_descent and noncanonical_to_actual,
            False,
            "actual-source 桥若继续经 exact-UV/rank/alpha 展开会回到终端；因此必须在进入 alpha 回边前独立证明源恒等或强化反原子。",
            INDEPENDENT_ACTUAL_SOURCE_BRIDGE,
        ),
        make_row(
            "DescentLeafAlphaReturnSyncClosed",
            sync_closed,
            False,
            "本同步关闭的是路线分类：旧 alpha 下钻不再算进展；当前最窄数学输入被钉到独立 actual-source 桥或 canonical-lock。",
            f"{CANONICAL_LOCK} OR {INDEPENDENT_ACTUAL_SOURCE_BRIDGE}",
        ),
        make_row(
            "RowColumnUnconditionalClosureCurrentCorpusProved",
            False,
            False,
            "尚未提交独立 actual-source 桥、canonical-lock 全证书、高段自足尾项或 DStructure/Rankin 替代包。",
            (
                f"({CANONICAL_LOCK} OR {INDEPENDENT_ACTUAL_SOURCE_BRIDGE}) "
                f"AND ({HIGH_TAIL}) AND {SELF_CONTAINED_DSTRUCTURE}"
            ),
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 descent/alpha 回流同步证书。"""
    alpha_cycle = load_json("prime-matrix-strict-alpha-terminal-to-acyclic-cycle-guard-sync-router.json")
    descent_firewall = load_json("prime-matrix-strict-acyclic-terminal-descent-firewall-router.json")
    descent_to_kernel = load_json("prime-matrix-strict-terminal-descent-to-pointwise-kernel-sync-router.json")
    alpha_frontier = load_json("prime-matrix-strict-alpha-row-formula-terminal-frontier-sync-router.json")
    leaf_firewall = load_json("prime-matrix-strict-terminal-leaf-firewall-current-instance-router.json")
    noncanonical = load_json("prime-matrix-strict-noncanonical-legal-closure-mode-router.json")
    canonical_absorb = load_json("prime-matrix-strict-canonical-lock-branch-absorption-router.json")

    rows = build_rows(
        alpha_cycle=alpha_cycle,
        descent_firewall=descent_firewall,
        descent_to_kernel=descent_to_kernel,
        alpha_frontier=alpha_frontier,
        leaf_firewall=leaf_firewall,
        noncanonical=noncanonical,
        canonical_absorb=canonical_absorb,
    )
    sync_closed = next(row["closed"] for row in rows if row["gate"] == "DescentLeafAlphaReturnSyncClosed")
    strict_basis = (
        f"({CANONICAL_LOCK} OR {INDEPENDENT_ACTUAL_SOURCE_BRIDGE}) "
        f"AND ({HIGH_TAIL}) AND {SELF_CONTAINED_DSTRUCTURE}"
    )
    external_high_tail_basis = (
        f"({CANONICAL_LOCK} OR {INDEPENDENT_ACTUAL_SOURCE_BRIDGE}) "
        f"AND {SELF_CONTAINED_DSTRUCTURE}"
    )
    conditional_external_basis = (
        f"({CANONICAL_LOCK} OR ProveActualFullSNonAPSourceIsCanonicalRIWBuchstab "
        "OR FullSNonAPStrengthenedSourceAntiAtomForActualSource "
        "OR AcceptOrProveExactFullS-KLS-ext) "
        f"AND ({HIGH_TAIL}) AND {SELF_CONTAINED_DSTRUCTURE}"
    )

    return {
        "certificate_type": "prime_matrix_strict_descent_leaf_firewall_alpha_return_sync_router",
        "status": "strict_descent_leaf_firewall_alpha_return_synced_active_bridge_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "descent_leaf_firewall_alpha_return_sync_router_closed": sync_closed,
        "terminal_return_well_founded_descent_schema_closed": True,
        "hidden_terminal_cycle_removed": True,
        "old_pointwise_alpha_descent_route_reclassified_as_backedge": True,
        "pointwise_alpha_route_counts_as_well_founded_descent": False,
        "terminal_leaf_firewall_inputs_proved_or_accepted": False,
        "actual_source_bridge_theorem_closed": False,
        "independent_actual_source_bridge_proved": False,
        "acyclic_terminal_canonical_lock_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": DESCENT,
        "terminal_gap_after_router": f"{CANONICAL_LOCK} OR {INDEPENDENT_ACTUAL_SOURCE_BRIDGE}",
        "strict_self_contained_math_basis_after_router": strict_basis,
        "with_external_mertens_high_tail_removed_basis": external_high_tail_basis,
        "conditional_external_math_basis_after_router": conditional_external_basis,
        "next_direct_attack_target": INDEPENDENT_ACTUAL_SOURCE_BRIDGE,
        "parallel_attack_targets": [
            CANONICAL_LOCK,
            MODEL_LEDGER,
            DSTRUCTURE_GATE,
        ],
        "backedge_chain": backedge_chain(),
        "next_attack_contract": {
            "name": INDEPENDENT_ACTUAL_SOURCE_BRIDGE,
            "must_prove": [
                "在进入 exact-UV/rank/alpha 回边前，证明 actual full-S non-AP 源就是 canonical RIW/Buchstab 决策树源",
                "或直接证明 actual source 的强化反原子：最终容量测度不存在 moving same-(u,v) 大原子",
                "若走 canonical-lock，并行提交 acyclic 同集推前、有限因子图和无 noncanonical payload 残留五项证书",
                "高段 Mertens/PNT 自足尾项与 DStructure/Rankin 替代包继续独立验收",
            ],
            "cannot_use_as_proof": [
                "把旧 pointwise/alpha 展开当作终端下降量",
                "把 alpha 局部公式回流终端当成终端矛盾",
                "把当前 PDEC/sparse 前沿为零说成未来 family 全局不存在",
                "把 canonical scoped 分支推广成 unrestricted noncanonical 闭合",
                "把外部 FullS-KLS 合同写成 strict 自足证明",
            ],
        },
        "rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步直接下钻 `AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate` 的最新最窄处："
            "下降防火墙已经删除无隐藏循环，但旧的 pointwise/alpha 展开路线会经 alpha row formula 回到 "
            "`PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve`，再被 acyclic 循环守卫送回终端家族。"
            "因此该路线只能登记为回边，不能算 well-founded descent。当前 strict 自足线的活动剩余被压成 "
            "`AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR "
            "IndependentActualSourceBridgeNotFactoredThroughAlphaReturn`。"
            "后者要求在进入 alpha 回边前独立证明 actual-source 恒等或强化反原子。"
            "尚未发现终端直接矛盾，行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict descent 叶子防火墙 alpha 回流同步路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"same_theorem_target_preserved={fmt_bool(result['same_theorem_target_preserved'])}",
        f"no_theorem_switch={fmt_bool(result['no_theorem_switch'])}",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"descent_leaf_firewall_alpha_return_sync_router_closed={fmt_bool(result['descent_leaf_firewall_alpha_return_sync_router_closed'])}",
        f"terminal_return_well_founded_descent_schema_closed={fmt_bool(result['terminal_return_well_founded_descent_schema_closed'])}",
        f"old_pointwise_alpha_descent_route_reclassified_as_backedge={fmt_bool(result['old_pointwise_alpha_descent_route_reclassified_as_backedge'])}",
        f"pointwise_alpha_route_counts_as_well_founded_descent={fmt_bool(result['pointwise_alpha_route_counts_as_well_founded_descent'])}",
        f"independent_actual_source_bridge_proved={fmt_bool(result['independent_actual_source_bridge_proved'])}",
        f"acyclic_terminal_canonical_lock_proved={fmt_bool(result['acyclic_terminal_canonical_lock_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"terminal_gap_after_router={result['terminal_gap_after_router']}",
        "```",
        "",
        "## 1. 回边链",
        "",
        "```text",
    ]
    for item in result["backedge_chain"]:
        lines.append(f"{item['from']} -> {item['to']}")

    lines.extend(
        [
            "```",
            "",
            "这条链说明：继续沿旧 pointwise/alpha 路线下钻，会回到同一个终端家族；它是审稿意义上的回边，不是下降量。",
            "",
            "## 2. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for row in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=row["gate"],
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
            "条件外部线可写为：",
            "",
            "```text",
            result["conditional_external_math_basis_after_router"],
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
