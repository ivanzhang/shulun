#!/usr/bin/env python3
"""生成 strict alpha 终端前沿到 acyclic 循环守卫的同步证书。

用法示例：
  python3 experiments/prime_matrix_strict_alpha_terminal_to_acyclic_cycle_guard_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-alpha-terminal-to-acyclic-cycle-guard-sync-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-alpha-terminal-to-acyclic-cycle-guard-sync-router.json"
OUT_MD = DOCS / "prime-matrix-strict-alpha-terminal-to-acyclic-cycle-guard-sync-router.md"

GLOBAL_TERMINAL = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve"
STRICT_TERMINAL = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily"
CANONICAL_LOCK = "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary"
DESCENT = "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate"
MODEL_LEDGER = "ExplicitModelGapAndFiniteDPRCLedger"
DSTRUCTURE_GATE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    "prime-matrix-strict-alpha-row-formula-terminal-frontier-sync-router.json",
    "prime-matrix-strict-global-terminal-scope-router.json",
    "prime-matrix-strict-acyclic-terminal-cycle-guard-router.json",
    "prime-matrix-strict-direct-acyclic-same-set-pdec-dual-router.json",
    "prime-matrix-strict-acyclic-windowed-dls-estimate-router.json",
    "prime-matrix-strict-canonical-lock-branch-absorption-router.json",
    "prime-matrix-strict-terminal-descent-to-pointwise-kernel-sync-router.json",
]


def load_json(name: str) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空对象。"""
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
    """登记本证书读取到的证据哈希。"""
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


def cycle_chain() -> list[dict[str, str]]:
    """列出裸 direct 终端路线的自回流链。"""
    return [
        {"from": STRICT_TERMINAL, "to": "DirectAcyclicSameSetPDECCapDualCertificate"},
        {"from": "DirectAcyclicSameSetPDECCapDualCertificate", "to": "AcyclicFiniteArcCapMassBoundsOrNamedReturn"},
        {"from": "AcyclicFiniteArcCapMassBoundsOrNamedReturn", "to": "DirectAcyclicCleanKLSDLSEstimateWithNamedReturn"},
        {"from": "DirectAcyclicCleanKLSDLSEstimateWithNamedReturn", "to": "AcyclicWindowedKloostermanDLSInternalEstimate"},
        {"from": "AcyclicWindowedKloostermanDLSInternalEstimate", "to": "SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks"},
        {"from": "SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks", "to": "AcyclicNCBLKActualBlockNonconcentrationOrStrengthenedSourceAntiAtom"},
        {"from": "AcyclicNCBLKActualBlockNonconcentrationOrStrengthenedSourceAntiAtom", "to": "GlobalPDECorSparseTerminalExclusion"},
        {"from": "GlobalPDECorSparseTerminalExclusion", "to": STRICT_TERMINAL},
    ]


def build_rows(
    alpha_terminal: dict[str, Any],
    strict_scope: dict[str, Any],
    cycle_guard: dict[str, Any],
    direct_pdec: dict[str, Any],
    clean_dls: dict[str, Any],
    canonical_absorb: dict[str, Any],
    terminal_descent: dict[str, Any],
) -> list[dict[str, Any]]:
    """同步 alpha 终端前沿与 acyclic 终端循环守卫。"""
    alpha_to_global = alpha_terminal.get("next_direct_attack_target") == GLOBAL_TERMINAL
    strict_scope_active = STRICT_TERMINAL in strict_scope.get("terminal_gap_after_router", "")
    cycle_reduced = cycle_guard.get("terminal_gap_after_router") == f"{CANONICAL_LOCK} OR {DESCENT}"
    raw_pdec_rejected = (
        direct_pdec.get("direct_acyclic_same_set_pdec_cap_dual_certificate_proved") is False
        and direct_pdec.get("next_direct_attack_target") == CANONICAL_LOCK
    )
    clean_reduced_to_dls = (
        clean_dls.get("terminal_gap_before_router") == "AcyclicWindowedKloostermanDLSInternalEstimate"
        and clean_dls.get("self_contained_kuznetsov_dls_large_sieve_inequality_proved") is False
    )
    canonical_scoped_only = (
        canonical_absorb.get("canonical_lock_branch_absorption_closed") is True
        and canonical_absorb.get("acyclic_terminal_canonical_lock_proved") is False
    )
    descent_recycles = (
        terminal_descent.get("terminal_gap_after_router", "").endswith(
            "PointwiseSameFormalUnitPrimitiveAlphaDeltaKernelTableWithNonzeroRankCertificate"
        )
        or terminal_descent.get("next_direct_attack_target") == "AlphaRowAnchorPhaseEmissionFormulaLedger"
    )
    sync_closed = all(
        [
            alpha_to_global,
            strict_scope_active,
            cycle_reduced,
            raw_pdec_rejected,
            clean_reduced_to_dls,
            canonical_scoped_only,
        ]
    )

    return [
        make_row(
            "CounterexampleBranchGuardPreserved",
            True,
            True,
            "本同步仍只整理早期零行反例链中的终端路线，不用真实样本缺席或当前物化前沿清零替代全局证明。",
            "row_column_unconditional_closed=false。",
        ),
        make_row(
            "AlphaLocalFrontierReachedGlobalTerminal",
            alpha_to_global,
            False,
            "alpha row formula 局部前沿已清完，下一目标进入全局 PDEC-CAP / internal CleanKLS 终端门。",
            GLOBAL_TERMINAL,
        ),
        make_row(
            "StrictScopeRequiresAcyclicTerminalFamily",
            strict_scope_active,
            False,
            "canonical-source 终端晋级不能直接导入 strict noncanonical；必须使用 acyclic terminal family 口径。",
            STRICT_TERMINAL,
        ),
        make_row(
            "AcyclicTerminalCycleGuardImported",
            cycle_reduced,
            False,
            "裸 direct PDEC 与裸 direct CleanKLS 路线已经识别为自回流，不能作为证明进展量。",
            f"{CANONICAL_LOCK} OR {DESCENT}",
        ),
        make_row(
            "DirectPDECNotProgressMeasure",
            raw_pdec_rejected,
            False,
            "direct acyclic same-set PDEC 只完成作用域审查；若要复用 canonical same-set，必须先证明 canonical-lock。",
            CANONICAL_LOCK,
        ),
        make_row(
            "DirectCleanNotProgressMeasure",
            clean_reduced_to_dls,
            False,
            "direct clean residual 被压到 windowed DLS/Kuznetsov 大筛原子，但该原子继续接回 NC-BLK/终端家族。",
            DESCENT,
        ),
        make_row(
            "CanonicalLockScopedOnly",
            canonical_scoped_only,
            False,
            "canonical-lock 若五项 exact same-set 证书齐备，只是 scoped canonical case；缺证书时不能调用。",
            CANONICAL_LOCK,
        ),
        make_row(
            "PriorDescentReturnedThroughAlphaFormula",
            descent_recycles,
            False,
            "上一轮 well-founded descent 下钻已进入逐点核表和 alpha formula；本轮已把 alpha 局部前沿同步回终端门。",
            "需要真正下降量，而不是再次走同一路由。",
        ),
        make_row(
            "TerminalCycleSyncClosed",
            sync_closed,
            False,
            "当前 PDEC/CleanKLS 终端门已压成 canonical-lock 精确证书或非循环严格下降证书；裸终端标签删除。",
            f"{CANONICAL_LOCK} OR {DESCENT}",
        ),
        make_row(
            "RowColumnUnconditionalClosureCurrentCorpusProved",
            False,
            False,
            "尚未证明 canonical-lock 五项证书，也未提交跨 PDEC/SAE/ColumnCRT/CleanKLS 回流的下降复杂度。",
            f"({CANONICAL_LOCK} OR {DESCENT}) AND {MODEL_LEDGER} AND {DSTRUCTURE_GATE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造终端循环同步证书。"""
    alpha_terminal = load_json("prime-matrix-strict-alpha-row-formula-terminal-frontier-sync-router.json")
    strict_scope = load_json("prime-matrix-strict-global-terminal-scope-router.json")
    cycle_guard = load_json("prime-matrix-strict-acyclic-terminal-cycle-guard-router.json")
    direct_pdec = load_json("prime-matrix-strict-direct-acyclic-same-set-pdec-dual-router.json")
    clean_dls = load_json("prime-matrix-strict-acyclic-windowed-dls-estimate-router.json")
    canonical_absorb = load_json("prime-matrix-strict-canonical-lock-branch-absorption-router.json")
    terminal_descent = load_json("prime-matrix-strict-terminal-descent-to-pointwise-kernel-sync-router.json")

    rows = build_rows(
        alpha_terminal=alpha_terminal,
        strict_scope=strict_scope,
        cycle_guard=cycle_guard,
        direct_pdec=direct_pdec,
        clean_dls=clean_dls,
        canonical_absorb=canonical_absorb,
        terminal_descent=terminal_descent,
    )
    sync_closed = next(row["closed"] for row in rows if row["gate"] == "TerminalCycleSyncClosed")

    terminal_basis = f"({CANONICAL_LOCK} OR {DESCENT}) AND {MODEL_LEDGER} AND {DSTRUCTURE_GATE}"
    return {
        "certificate_type": "prime_matrix_strict_alpha_terminal_to_acyclic_cycle_guard_sync_router",
        "status": "strict_alpha_terminal_synced_to_acyclic_cycle_guard_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "alpha_terminal_to_acyclic_cycle_guard_sync_router_closed": sync_closed,
        "raw_direct_pdec_clean_routes_count_as_closure": False,
        "acyclic_terminal_canonical_lock_proved": False,
        "acyclic_noncanonical_terminal_return_well_founded_descent_proved": False,
        "pdec_cap_or_internal_clean_kls_large_sieve_proved": False,
        "explicit_model_gap_and_finite_dprc_ledger_proved": False,
        "dstructure_tail_log4_finite_rankin_full_ledger_independent_acceptance_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": GLOBAL_TERMINAL,
        "terminal_gap_after_router": terminal_basis,
        "next_direct_attack_target": DESCENT,
        "parallel_attack_targets": [
            CANONICAL_LOCK,
            MODEL_LEDGER,
            DSTRUCTURE_GATE,
        ],
        "cycle_chain": cycle_chain(),
        "sync_law": (
            "Once the alpha local frontier has returned to PDEC-CAP/CleanKLS, the direct terminal labels do not give a "
            "proof. Direct PDEC routes to finite arcs and then clean KLS; direct clean KLS routes through windowed DLS, "
            "Kuznetsov/NC-BLK and back to the global terminal family. Therefore the strict acyclic terminal family can only "
            "advance by an actual canonical-lock certificate or by a well-founded descent measure that strictly decreases "
            "across every named terminal return."
        ),
        "plain_conclusion": (
            "本步把本轮 alpha 局部闭合后的 `PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve` 接回 strict acyclic "
            "终端循环守卫。结论是：direct PDEC / direct CleanKLS 裸路线会自回流，不能当作闭合；"
            "当前真正最窄点是 `AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate`，"
            "并行备用为 `AcyclicTerminalCanonicalLockToCanonicalSourceBoundary`。"
            "仍未发现终端直接矛盾，行/列命题不能宣称无条件闭合。"
        ),
        "rows": rows,
        "source_hashes": source_hashes(),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict alpha 终端到 acyclic 循环守卫同步路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"same_theorem_target_preserved={fmt_bool(result['same_theorem_target_preserved'])}",
        f"no_theorem_switch={fmt_bool(result['no_theorem_switch'])}",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"alpha_terminal_to_acyclic_cycle_guard_sync_router_closed={fmt_bool(result['alpha_terminal_to_acyclic_cycle_guard_sync_router_closed'])}",
        f"raw_direct_pdec_clean_routes_count_as_closure={fmt_bool(result['raw_direct_pdec_clean_routes_count_as_closure'])}",
        f"acyclic_terminal_canonical_lock_proved={fmt_bool(result['acyclic_terminal_canonical_lock_proved'])}",
        f"acyclic_noncanonical_terminal_return_well_founded_descent_proved={fmt_bool(result['acyclic_noncanonical_terminal_return_well_founded_descent_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 自回流链",
        "",
        "```text",
    ]
    for item in result["cycle_chain"]:
        lines.append(f"{item['from']} -> {item['to']}")
    lines.extend(
        [
            "```",
            "",
            "## 2. 同步律",
            "",
            result["sync_law"],
            "",
            "## 3. 判定表",
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
    lines.extend(
        [
            "",
            "## 4. 下一主攻点",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "并行保留：",
            "",
            "```text",
            " AND ".join(result["parallel_attack_targets"]),
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
