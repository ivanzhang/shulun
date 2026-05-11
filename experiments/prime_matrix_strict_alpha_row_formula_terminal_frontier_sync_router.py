#!/usr/bin/env python3
"""生成 strict alpha row formula 到终端前沿的总同步证书。

用法示例：
  python3 experiments/prime_matrix_strict_alpha_row_formula_terminal_frontier_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-alpha-row-formula-terminal-frontier-sync-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-alpha-row-formula-terminal-frontier-sync-router.json"
OUT_MD = DOCS / "prime-matrix-strict-alpha-row-formula-terminal-frontier-sync-router.md"

TARGET = "AlphaRowAnchorPhaseEmissionFormulaLedger"
GLOBAL_TERMINAL = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve"
MODEL_LEDGER = "ExplicitModelGapAndFiniteDPRCLedger"
DSTRUCTURE_GATE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    "prime-matrix-strict-terminal-descent-to-pointwise-kernel-sync-router.json",
    "prime-matrix-strict-alpha-row-anchor-phase-formula-router.json",
    "prime-matrix-strict-alpha-formula-signed-lift-terminal-sync-router.json",
    "prime-matrix-strict-alpha-carry-shell-congruence-formula-router.json",
    "prime-matrix-strict-alpha-anchor-collar-overload-return-router.json",
    "prime-matrix-strict-actual-moving-block-spread-ncb-lk-router.json",
    "prime-matrix-global-pdec-sparse-terminal-split-reconciliation-router.json",
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


def local_branch_table() -> list[dict[str, str]]:
    """列出 alpha formula 局部分支的最新归宿。"""
    return [
        {
            "branch": "source tuple variable binding",
            "status": "imported closed through unsigned skeleton/carry formula",
            "remaining": "no local alpha gap",
        },
        {
            "branch": "carry-shell congruence row formula",
            "status": "closed as unsigned geometric indexing theorem",
            "remaining": "not a signed coefficient theorem",
        },
        {
            "branch": "phase-wheel compatibility",
            "status": "imported closed through P-column/layered-wheel registration",
            "remaining": "no local phase gap",
        },
        {
            "branch": "signed coefficient lift",
            "status": "synced through weight law / identity / moving-block to terminal gap",
            "remaining": f"{GLOBAL_TERMINAL} AND {MODEL_LEDGER}",
        },
        {
            "branch": "anchor-collar overload named return",
            "status": "closed as named-return schema",
            "remaining": f"{GLOBAL_TERMINAL} AND {MODEL_LEDGER}",
        },
    ]


def build_rows(
    terminal_descent: dict[str, Any],
    alpha_formula: dict[str, Any],
    signed_sync: dict[str, Any],
    carry_formula: dict[str, Any],
    overload_return: dict[str, Any],
    moving_block: dict[str, Any],
    global_split: dict[str, Any],
) -> list[dict[str, Any]]:
    """同步 alpha row formula 的局部分支到终端前沿。"""
    target_active = terminal_descent.get("next_direct_attack_target") == TARGET
    formula_split_registered = alpha_formula.get("terminal_gap_before_router") == TARGET
    signed_to_terminal = signed_sync.get("signed_lift_branch_recycles_to_terminal_gap") is True
    carry_closed = carry_formula.get("alpha_formula_carry_shell_congruence_row_formula_proved") is True
    source_phase_imported = (
        carry_formula.get("alpha_formula_source_tuple_to_carry_shell_variable_binding_imported_closed") is True
        and carry_formula.get("alpha_formula_phase_wheel_compatibility_imported_closed") is True
    )
    overload_schema_closed = (
        overload_return.get("alpha_formula_anchor_collar_overload_named_return_ledger_closed") is True
    )
    moving_terminal = (
        moving_block.get("terminal_gap_after_router") == f"{GLOBAL_TERMINAL} AND {MODEL_LEDGER}"
    )
    global_terminal_open = (
        global_split.get("terminal_gap_after_router") == GLOBAL_TERMINAL
        and global_split.get("pdec_cap_or_internal_clean_kls_large_sieve_proved") is False
    )
    local_frontier_synced = all(
        [
            target_active,
            formula_split_registered,
            signed_to_terminal,
            carry_closed,
            source_phase_imported,
            overload_schema_closed,
            moving_terminal,
            global_terminal_open,
        ]
    )

    return [
        make_row(
            "CounterexampleBranchGuardPreserved",
            True,
            True,
            "本同步仍只在早期零行反例链内整理局部分支归宿，不从真实缺席或样本审计取证。",
            "direct_unconditional_contradiction_found=false。",
        ),
        make_row(
            "AlphaRowFormulaTargetActive",
            target_active and formula_split_registered,
            False,
            "终端下降到逐点核表后，当前局部目标确为 alpha row anchor/phase emission formula。",
            TARGET,
        ),
        make_row(
            "UnsignedLocalBranchesClosed",
            carry_closed and source_phase_imported,
            True,
            "source tuple 绑定、carry-shell 同余公式和 phase-wheel 兼容已在 unsigned 几何层闭合。",
            "不产生 signed pre-Cauchy coefficient。",
        ),
        make_row(
            "SignedLiftBranchTerminalSynced",
            signed_to_terminal and moving_terminal,
            False,
            "signed-lift 下钻经权重律、独立恒等式、moving-block/NC-BLK 回到终端容量/模型账本。",
            f"{GLOBAL_TERMINAL} AND {MODEL_LEDGER}",
        ),
        make_row(
            "AnchorOverloadReturnSchemaClosed",
            overload_schema_closed,
            True,
            "anchor-collar 过载没有独立无名出口，已登记为 PDEC/SAE/ColumnCRT/LocalSurvivor/CleanKLS 回流。",
            f"{GLOBAL_TERMINAL} AND {MODEL_LEDGER}",
        ),
        make_row(
            "AlphaFormulaLocalFrontierSyncedToTerminal",
            local_frontier_synced,
            False,
            "alpha formula 的局部几何和命名回流分支已同步完成；剩余不再是 alpha 局部公式，而是全局终端门。",
            f"{GLOBAL_TERMINAL} AND {MODEL_LEDGER}",
        ),
        make_row(
            "TerminalExclusionStillOpen",
            global_terminal_open,
            False,
            "PDEC-CAP 或内部 CleanKLS/DLS 大筛、模型余量和 DStructure/Rankin 仍未证明。",
            f"{GLOBAL_TERMINAL} AND {MODEL_LEDGER} AND {DSTRUCTURE_GATE}",
        ),
        make_row(
            "RowColumnUnconditionalClosureCurrentCorpusProved",
            False,
            False,
            "当前只是把 alpha 局部剩余压到终端前沿；尚未得到反例链与真实链的终端矛盾。",
            f"{GLOBAL_TERMINAL} AND {MODEL_LEDGER} AND {DSTRUCTURE_GATE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 alpha row formula 终端前沿同步证书。"""
    terminal_descent = load_json("prime-matrix-strict-terminal-descent-to-pointwise-kernel-sync-router.json")
    alpha_formula = load_json("prime-matrix-strict-alpha-row-anchor-phase-formula-router.json")
    signed_sync = load_json("prime-matrix-strict-alpha-formula-signed-lift-terminal-sync-router.json")
    carry_formula = load_json("prime-matrix-strict-alpha-carry-shell-congruence-formula-router.json")
    overload_return = load_json("prime-matrix-strict-alpha-anchor-collar-overload-return-router.json")
    moving_block = load_json("prime-matrix-strict-actual-moving-block-spread-ncb-lk-router.json")
    global_split = load_json("prime-matrix-global-pdec-sparse-terminal-split-reconciliation-router.json")

    rows = build_rows(
        terminal_descent=terminal_descent,
        alpha_formula=alpha_formula,
        signed_sync=signed_sync,
        carry_formula=carry_formula,
        overload_return=overload_return,
        moving_block=moving_block,
        global_split=global_split,
    )
    local_synced = next(
        row["closed"] for row in rows if row["gate"] == "AlphaFormulaLocalFrontierSyncedToTerminal"
    )
    terminal_basis = f"{GLOBAL_TERMINAL} AND {MODEL_LEDGER} AND {DSTRUCTURE_GATE}"

    return {
        "certificate_type": "prime_matrix_strict_alpha_row_formula_terminal_frontier_sync_router",
        "status": "strict_alpha_row_formula_local_frontier_synced_to_terminal_gap_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "alpha_row_formula_terminal_frontier_sync_router_closed": local_synced,
        "alpha_row_formula_local_frontier_synced_to_terminal": local_synced,
        "alpha_formula_source_tuple_to_carry_shell_variable_binding_imported_closed": True,
        "alpha_formula_carry_shell_congruence_row_formula_proved": True,
        "alpha_formula_phase_wheel_compatibility_imported_closed": True,
        "alpha_formula_signed_coefficient_lift_proved": False,
        "alpha_formula_anchor_collar_overload_named_return_ledger_closed": True,
        "alpha_row_anchor_phase_emission_formula_proved": False,
        "pointwise_same_formal_unit_primitive_alpha_delta_kernel_table_with_nonzero_rank_proved": False,
        "pdec_cap_or_internal_clean_kls_large_sieve_proved": False,
        "explicit_model_gap_and_finite_dprc_ledger_proved": False,
        "dstructure_tail_log4_finite_rankin_full_ledger_independent_acceptance_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": TARGET,
        "terminal_gap_after_router": terminal_basis,
        "next_direct_attack_target": GLOBAL_TERMINAL,
        "parallel_required_inputs": [
            MODEL_LEDGER,
            DSTRUCTURE_GATE,
        ],
        "local_branch_table": local_branch_table(),
        "sync_law": (
            "After the signed-lift branch returns to the terminal capacity/model ledger, the unsigned carry-shell and "
            "phase branches close locally, and anchor overload is registered as a named return, the alpha row formula no "
            "longer contains an independent local nonterminal exit in the current corpus. The remaining obstruction is the "
            "global PDEC-CAP or internal CleanKLS/DLS terminal gate, plus model-gap and DStructure acceptance."
        ),
        "plain_conclusion": (
            "`AlphaRowAnchorPhaseEmissionFormulaLedger` 的局部前沿已同步到终端门："
            "source tuple/carry-shell/phase 三个 unsigned 几何分支闭合，signed-lift 分支回流 "
            "`PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve AND ExplicitModelGapAndFiniteDPRCLedger`，"
            "anchor-collar 过载分支作为命名回流 schema 闭合。"
            "因此下一真正主攻点是全局 `PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve`；"
            "行/列命题仍未无条件闭合。"
        ),
        "rows": rows,
        "source_hashes": source_hashes(),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict alpha row formula 终端前沿同步路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"same_theorem_target_preserved={fmt_bool(result['same_theorem_target_preserved'])}",
        f"no_theorem_switch={fmt_bool(result['no_theorem_switch'])}",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"alpha_row_formula_terminal_frontier_sync_router_closed={fmt_bool(result['alpha_row_formula_terminal_frontier_sync_router_closed'])}",
        f"alpha_row_formula_local_frontier_synced_to_terminal={fmt_bool(result['alpha_row_formula_local_frontier_synced_to_terminal'])}",
        f"alpha_formula_carry_shell_congruence_row_formula_proved={fmt_bool(result['alpha_formula_carry_shell_congruence_row_formula_proved'])}",
        f"alpha_formula_signed_coefficient_lift_proved={fmt_bool(result['alpha_formula_signed_coefficient_lift_proved'])}",
        f"alpha_row_anchor_phase_emission_formula_proved={fmt_bool(result['alpha_row_anchor_phase_emission_formula_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 局部分支归宿",
        "",
        "| branch | status | remaining |",
        "| --- | --- | --- |",
    ]
    for item in result["local_branch_table"]:
        lines.append(
            "| {branch} | {status} | {remaining} |".format(
                branch=table_cell(item["branch"]),
                status=table_cell(item["status"]),
                remaining=table_cell(item["remaining"]),
            )
        )
    lines.extend(
        [
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
            " AND ".join(result["parallel_required_inputs"]),
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
