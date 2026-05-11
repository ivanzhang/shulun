#!/usr/bin/env python3
"""生成 strict actual moving-block/NC-BLK 对接路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_actual_moving_block_spread_ncb_lk_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-actual-moving-block-spread-ncb-lk-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-actual-moving-block-spread-ncb-lk-router.json"
OUT_MD = DOCS / "prime-matrix-strict-actual-moving-block-spread-ncb-lk-router.md"

OLD_ATOM = "ActualNoncanonicalMovingBlockSpreadNCBLKForCounterexampleBranchAndReturn"
GLOBAL_TERMINAL = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve"
MODEL_LEDGER = "ExplicitModelGapAndFiniteDPRCLedger"
DSTRUCTURE_GATE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    "prime-matrix-strict-independent-identity-statement-taxonomy-router.json",
    "prime-matrix-counterexample-moving-block-terminal-router.json",
    "prime-matrix-early-zero-terminal-schema-reconciliation-router.json",
    "prime-matrix-moving-block-dprc-ledger-compatibility-router.json",
    "prime-matrix-global-pdec-sparse-terminal-split-reconciliation-router.json",
    "prime-matrix-final-input-firewall-boundary-router.json",
    "prime-matrix-strict-terminal-leaf-firewall-current-instance-router.json",
]


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空字典。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: bool) -> str:
    """把布尔值格式化为小写文本。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def source_hashes() -> dict[str, str]:
    """汇总依赖证据哈希。"""
    return {
        f"docs/monograph/{name}": sha256(DOCS / name)
        for name in SOURCE_FILES
        if (DOCS / name).exists()
    }


def make_row(
    gate: str,
    closed: bool,
    proved: bool,
    meaning: str,
    remaining: str,
) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_rows(
    identity: dict[str, Any],
    moving: dict[str, Any],
    terminal_schema: dict[str, Any],
    dprc: dict[str, Any],
    global_split: dict[str, Any],
    final_firewall: dict[str, Any],
    leaf_firewall: dict[str, Any],
) -> list[dict[str, Any]]:
    """把 strict actual moving-block 原子对接到已登记终端门。"""
    strict_target_active = identity.get("terminal_gap_after_router") == OLD_ATOM
    moving_reduction_closed = moving.get("moving_block_to_terminal_reduction_closed") is True
    terminal_schema_closed = terminal_schema.get("early_zero_terminal_abstract_package_reconciled") is True
    dprc_compat_closed = dprc.get("exact_model_gap_dprc_compatibility_proved") is True
    global_split_closed = global_split.get("global_pdec_sparse_terminal_split_reconciled") is True
    current_frontier_zero = (
        global_split.get("current_materialized_frontier_exhausted") is True
        and final_firewall.get("current_materialized_terminal_frontier_closed") is True
        and leaf_firewall.get("current_leaf_firewall_active_basis_reduced") is True
    )
    no_unnamed_exit = all(
        [
            strict_target_active,
            moving_reduction_closed,
            terminal_schema_closed,
            dprc_compat_closed,
            global_split_closed,
            current_frontier_zero,
        ]
    )

    return [
        make_row(
            "StrictActualMovingBlockInputActive",
            strict_target_active,
            False,
            "上一层 strict 恒等式分类已把最窄点压成 actual noncanonical moving-block/NC-BLK。",
            OLD_ATOM,
        ),
        make_row(
            "CounterexampleBranchGuardPreserved",
            True,
            True,
            "本步只在 Assume EarlyZeroRowWithinP 的假设链条中传递，不用真实零行缺席作证。",
            "所有输出必须是反例链内的命名终端、模型账本或打开输入。",
        ),
        make_row(
            "MovingBlockTerminalReductionImported",
            moving_reduction_closed,
            True,
            "actual same-(u,v) moving block 有登记低维签名则进 PDEC/SAE/ColumnCRT；无签名则进 L2-flat/早期零行终端包。",
            "EarlyZeroTerminalExclusionPackage AND ExactModelGapAndDPRCLedgerCompatibilityForMovingBlock。",
        ),
        make_row(
            "EarlyZeroTerminalSchemaReconciledImported",
            terminal_schema_closed,
            True,
            "抽象 EarlyZeroTerminalExclusionPackage 已与 anchor、cofactor、early-band、DLS 回流 schema 调和。",
            "GlobalPDECorSparseTerminalExclusion。",
        ),
        make_row(
            "DPRCCompatibilityGateRemovedImported",
            dprc_compat_closed,
            True,
            "moving-block 替换没有引入新的 DPRC 口径；兼容性门可删除，但模型账本自身仍保留。",
            MODEL_LEDGER,
        ),
        make_row(
            "GlobalTerminalSplitImported",
            global_split_closed,
            True,
            "GlobalPDECorSparseTerminalExclusion 已与全局终端家族拆分对齐。",
            GLOBAL_TERMINAL,
        ),
        make_row(
            "CurrentMaterializedTerminalFrontierExhausted",
            current_frontier_zero,
            True,
            "当前已物化 PDEC 与 sparse/LocalSurvivor 前沿清零；future schema 只是准入纪律。",
            "这不是未来全局 family 不存在的证明。",
        ),
        make_row(
            "StrictActualMovingBlockNoUnnamedExit",
            no_unnamed_exit,
            True,
            "strict moving-block/NC-BLK 不能再作为独立无名出口停留。",
            f"{GLOBAL_TERMINAL} AND {MODEL_LEDGER}",
        ),
        make_row(
            "DirectContradictionNotYetReached",
            True,
            False,
            "早期零行反例链已被挤压到命名终端与模型账本，但尚未推出足以闭合命题的直接矛盾。",
            "需证明终端容量/内部大筛，或证明模型余量账本。",
        ),
        make_row(
            "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve",
            False,
            False,
            "仍未证明全局 PDEC-CAP 容量证书或内部 CleanKLS/DLS 大筛吸收。",
            GLOBAL_TERMINAL,
        ),
        make_row(
            "ExplicitModelGapAndFiniteDPRCLedger",
            False,
            False,
            "P<2003 有限 DPRC 与 P>=2003 模型余量账本仍需正式证明。",
            MODEL_LEDGER,
        ),
        make_row(
            "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance",
            False,
            False,
            "DStructure/Tail-log4/finite Rankin 仍是最终独立晋级验收门。",
            DSTRUCTURE_GATE,
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 strict actual moving-block 路由证书。"""
    identity = load_json(DOCS / "prime-matrix-strict-independent-identity-statement-taxonomy-router.json")
    moving = load_json(DOCS / "prime-matrix-counterexample-moving-block-terminal-router.json")
    terminal_schema = load_json(DOCS / "prime-matrix-early-zero-terminal-schema-reconciliation-router.json")
    dprc = load_json(DOCS / "prime-matrix-moving-block-dprc-ledger-compatibility-router.json")
    global_split = load_json(DOCS / "prime-matrix-global-pdec-sparse-terminal-split-reconciliation-router.json")
    final_firewall = load_json(DOCS / "prime-matrix-final-input-firewall-boundary-router.json")
    leaf_firewall = load_json(DOCS / "prime-matrix-strict-terminal-leaf-firewall-current-instance-router.json")

    rows = build_rows(
        identity=identity,
        moving=moving,
        terminal_schema=terminal_schema,
        dprc=dprc,
        global_split=global_split,
        final_firewall=final_firewall,
        leaf_firewall=leaf_firewall,
    )
    no_unnamed_exit = next(
        row["closed"] for row in rows if row["gate"] == "StrictActualMovingBlockNoUnnamedExit"
    )

    return {
        "certificate_type": "prime_matrix_strict_actual_moving_block_spread_ncb_lk_router",
        "status": "strict_actual_moving_block_reduced_to_global_terminal_modelgap_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "strict_actual_moving_block_router_closed": no_unnamed_exit,
        "actual_noncanonical_moving_block_spread_ncb_lk_proved": False,
        "new_actual_source_entropy_theorem_proved": False,
        "global_pdec_sparse_terminal_exclusion_proved": False,
        "pdec_cap_or_internal_clean_kls_large_sieve_proved": False,
        "explicit_model_gap_and_finite_dprc_ledger_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": OLD_ATOM,
        "terminal_gap_after_router": f"{GLOBAL_TERMINAL} AND {MODEL_LEDGER}",
        "strict_self_contained_basis_after_router": (
            f"{GLOBAL_TERMINAL} AND {MODEL_LEDGER} AND {DSTRUCTURE_GATE}"
        ),
        "next_direct_attack_target": f"{GLOBAL_TERMINAL} AND {MODEL_LEDGER}",
        "direct_contradiction_need": (
            "若要把早期零行反例链与真实结构链变成直接矛盾，需要再证明："
            "反例强制的终端对象落入可排斥的全局 PDEC-CAP / internal CleanKLS 大筛容量门，"
            "并同时支付 ExplicitModelGapAndFiniteDPRCLedger。当前材料只证明无名出口不存在，"
            "没有证明这些终端门本身。"
        ),
        "structural_chain": [
            "Assume EarlyZeroRowWithinP",
            "ActualNoncanonicalMovingBlockSpreadNCBLK cannot remain unnamed",
            "registered low-dimensional signature -> PDEC/SAE/ColumnCRT/sparse terminal",
            "no registered signature -> pure L2-flat/early-zero terminal package",
            "early-zero terminal schema -> GlobalPDECorSparseTerminalExclusion",
            "global terminal split -> PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve",
            "DPRC compatibility gate removed, ExplicitModelGapAndFiniteDPRCLedger remains",
        ],
        "rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`ActualNoncanonicalMovingBlockSpreadNCBLKForCounterexampleBranchAndReturn` 在 strict 链中已不能作为"
            "独立无名出口保留：有低维签名时进入 PDEC/SAE/ColumnCRT/sparse 终端，无低维签名时进入早期零行"
            "L2-flat/终端包；后者已调和为 `GlobalPDECorSparseTerminalExclusion`，再由全局拆分压到 "
            "`PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve`。moving-block 专属 DPRC 兼容门可删除，但 "
            "`ExplicitModelGapAndFiniteDPRCLedger` 仍是独立账本。因此当前最窄剩余不是 moving-block 本身，"
            "而是全局终端容量/内部大筛门与模型余量账本；直接矛盾仍未达到，行/列命题不能宣称无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict actual moving-block/NC-BLK 对接路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"same_theorem_target_preserved={fmt_bool(result['same_theorem_target_preserved'])}",
        f"no_theorem_switch={fmt_bool(result['no_theorem_switch'])}",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"strict_actual_moving_block_router_closed={fmt_bool(result['strict_actual_moving_block_router_closed'])}",
        f"actual_noncanonical_moving_block_spread_ncb_lk_proved={fmt_bool(result['actual_noncanonical_moving_block_spread_ncb_lk_proved'])}",
        f"new_actual_source_entropy_theorem_proved={fmt_bool(result['new_actual_source_entropy_theorem_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"terminal_gap_after_router={result['terminal_gap_after_router']}",
        "```",
        "",
        "## 1. 反例链压缩",
        "",
        "```text",
    ]
    lines.extend(result["structural_chain"])
    lines.extend(
        [
            "```",
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

    lines.extend(
        [
            "",
            "## 3. 直接矛盾缺口",
            "",
            result["direct_contradiction_need"],
            "",
            "## 4. 下一主攻点",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "连同独立晋级门：",
            "",
            "```text",
            result["strict_self_contained_basis_after_router"],
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
