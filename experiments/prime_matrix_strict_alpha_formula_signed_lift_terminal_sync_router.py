#!/usr/bin/env python3
"""生成 strict alpha formula signed-lift 终端同步证书。

用法示例：
  python3 experiments/prime_matrix_strict_alpha_formula_signed_lift_terminal_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-alpha-formula-signed-lift-terminal-sync-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-alpha-formula-signed-lift-terminal-sync-router.json"
OUT_MD = DOCS / "prime-matrix-strict-alpha-formula-signed-lift-terminal-sync-router.md"

ALPHA_ROW_FORMULA = "AlphaRowAnchorPhaseEmissionFormulaLedger"
SIGNED_LIFT = "AlphaFormulaSignedCoefficientLiftLedger"
SIGNED_WEIGHT = "AlphaSignedWeightLawFromPreCauchyArithmeticIdentityLedger"
IDENTITY = "IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger"
MOVING_BLOCK = "ActualNoncanonicalMovingBlockSpreadNCBLKForCounterexampleBranchAndReturn"
GLOBAL_TERMINAL = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve"
MODEL_LEDGER = "ExplicitModelGapAndFiniteDPRCLedger"
DSTRUCTURE_GATE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    "prime-matrix-strict-terminal-descent-to-pointwise-kernel-sync-router.json",
    "prime-matrix-strict-alpha-row-anchor-phase-formula-router.json",
    "prime-matrix-strict-alpha-formula-signed-lift-router.json",
    "prime-matrix-strict-alpha-signed-weight-law-router.json",
    "prime-matrix-strict-independent-identity-statement-taxonomy-router.json",
    "prime-matrix-strict-actual-moving-block-spread-ncb-lk-router.json",
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


def sync_chain() -> list[dict[str, str]]:
    """列出 signed-lift 分支回流到终端账本的同步链。"""
    return [
        {"from": ALPHA_ROW_FORMULA, "to": SIGNED_LIFT},
        {"from": SIGNED_LIFT, "to": SIGNED_WEIGHT},
        {"from": SIGNED_WEIGHT, "to": IDENTITY},
        {"from": IDENTITY, "to": MOVING_BLOCK},
        {"from": MOVING_BLOCK, "to": f"{GLOBAL_TERMINAL} AND {MODEL_LEDGER}"},
    ]


def build_rows(
    terminal_sync: dict[str, Any],
    alpha_formula: dict[str, Any],
    signed_lift: dict[str, Any],
    signed_weight: dict[str, Any],
    identity: dict[str, Any],
    moving_block: dict[str, Any],
) -> list[dict[str, Any]]:
    """同步 signed-lift 下游证书并重新排序 alpha formula 剩余。"""
    terminal_sync_active = terminal_sync.get("next_direct_attack_target") == (
        "AlphaRowAnchorPhaseEmissionFormulaLedger"
    )
    alpha_formula_to_signed_lift = (
        alpha_formula.get("next_direct_attack_target") == SIGNED_LIFT
        or SIGNED_LIFT in alpha_formula.get("terminal_gap_after_router", "")
    )
    signed_lift_to_weight = signed_lift.get("next_direct_attack_target") == SIGNED_WEIGHT
    signed_weight_to_identity = signed_weight.get("next_direct_attack_target") == IDENTITY
    identity_to_moving = identity.get("terminal_gap_after_router") == MOVING_BLOCK
    moving_to_terminal = (
        moving_block.get("strict_actual_moving_block_router_closed") is True
        and moving_block.get("actual_noncanonical_moving_block_spread_ncb_lk_proved") is False
        and moving_block.get("terminal_gap_after_router") == f"{GLOBAL_TERMINAL} AND {MODEL_LEDGER}"
    )
    signed_lift_branch_recycles = all(
        [
            alpha_formula_to_signed_lift,
            signed_lift_to_weight,
            signed_weight_to_identity,
            identity_to_moving,
            moving_to_terminal,
        ]
    )

    non_recycling_basis = (
        "AlphaFormulaSourceTupleToCarryShellVariableBindingLedger OR "
        "AlphaFormulaCarryShellCongruenceRowFormulaLedger OR "
        "AlphaFormulaPhaseWheelCompatibilityLedger OR "
        "AlphaFormulaAnchorCollarOverloadNamedReturnLedger OR "
        f"({GLOBAL_TERMINAL} AND {MODEL_LEDGER})"
    )

    return [
        make_row(
            "CounterexampleBranchGuardPreserved",
            True,
            True,
            "本证书只在早期零行反例链内同步已有路由，不用真实零行缺席或数值实验替代证明。",
            "direct_unconditional_contradiction_found=false。",
        ),
        make_row(
            "TerminalDescentPointwiseKernelImported",
            terminal_sync_active,
            False,
            "上一同步已把终端下降压到逐点同 formal unit primitive alpha-delta 核表，再首攻 alpha row anchor/phase 公式。",
            ALPHA_ROW_FORMULA,
        ),
        make_row(
            "AlphaRowFormulaSignedLiftBranchActive",
            alpha_formula_to_signed_lift,
            False,
            "alpha row anchor/phase 公式的五项拆分中，当前首攻子项是 signed coefficient lift。",
            SIGNED_LIFT,
        ),
        make_row(
            "SignedLiftReducedToSignedWeightLaw",
            signed_lift_to_weight,
            False,
            "signed lift 不能由 unsigned carry-shell 覆盖反推，当前首攻被压成 alpha signed 权重律。",
            SIGNED_WEIGHT,
        ),
        make_row(
            "SignedWeightReducedToIndependentIdentity",
            signed_weight_to_identity,
            False,
            "权重律必须是 Cauchy/dispersion 之前的正向算术恒等式，不能由零行几何或 payment 反推。",
            IDENTITY,
        ),
        make_row(
            "IndependentIdentityTaxonomyReducedToMovingBlock",
            identity_to_moving,
            False,
            "恒等式陈述没有第五来源类；canonical/generic/AP/external 被排除后，实际内容是 actual moving-block/NC-BLK。",
            MOVING_BLOCK,
        ),
        make_row(
            "MovingBlockNoUnnamedExitImported",
            moving_to_terminal,
            True,
            "moving-block/NC-BLK 已不能作为独立无名出口停留，只能回到全局终端容量门与模型余量账本。",
            f"{GLOBAL_TERMINAL} AND {MODEL_LEDGER}",
        ),
        make_row(
            "SignedLiftBranchIsTerminalReturnNotAcyclicExit",
            signed_lift_branch_recycles,
            False,
            "signed-lift 当前内部下钻没有给出非循环自足出口，而是回流到全局终端门；不能据此宣称 alpha row 公式闭合。",
            f"{GLOBAL_TERMINAL} AND {MODEL_LEDGER}",
        ),
        make_row(
            "AlphaFormulaRemainingNonRecyclingBasisReordered",
            signed_lift_branch_recycles,
            False,
            "signed-lift 分支已回流后，alpha formula 的非回流候选应转到 source tuple、carry-shell congruence、phase-wheel 或 anchor-collar 回流纪律。",
            non_recycling_basis,
        ),
        make_row(
            "DirectContradictionNotYetReached",
            True,
            False,
            "反例链已被进一步压缩，但终端容量/模型余量账本仍未排斥，尚未显出可闭合行/列命题的直接矛盾。",
            f"{GLOBAL_TERMINAL} AND {MODEL_LEDGER} AND {DSTRUCTURE_GATE}",
        ),
        make_row(
            "RowColumnUnconditionalClosureCurrentCorpusProved",
            False,
            False,
            "当前材料仍不能宣称作者侧无条件闭合；必须继续攻终端容量/模型余量或 alpha formula 其他非回流子项。",
            non_recycling_basis,
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 signed-lift 终端同步证书。"""
    terminal_sync = load_json("prime-matrix-strict-terminal-descent-to-pointwise-kernel-sync-router.json")
    alpha_formula = load_json("prime-matrix-strict-alpha-row-anchor-phase-formula-router.json")
    signed_lift = load_json("prime-matrix-strict-alpha-formula-signed-lift-router.json")
    signed_weight = load_json("prime-matrix-strict-alpha-signed-weight-law-router.json")
    identity = load_json("prime-matrix-strict-independent-identity-statement-taxonomy-router.json")
    moving_block = load_json("prime-matrix-strict-actual-moving-block-spread-ncb-lk-router.json")

    rows = build_rows(
        terminal_sync=terminal_sync,
        alpha_formula=alpha_formula,
        signed_lift=signed_lift,
        signed_weight=signed_weight,
        identity=identity,
        moving_block=moving_block,
    )
    signed_lift_recycles = next(
        row["closed"] for row in rows if row["gate"] == "SignedLiftBranchIsTerminalReturnNotAcyclicExit"
    )
    reordered_basis = next(
        row["remaining"] for row in rows if row["gate"] == "AlphaFormulaRemainingNonRecyclingBasisReordered"
    )

    return {
        "certificate_type": "prime_matrix_strict_alpha_formula_signed_lift_terminal_sync_router",
        "status": "strict_alpha_formula_signed_lift_branch_synced_to_terminal_gap_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "alpha_formula_signed_lift_terminal_sync_router_closed": signed_lift_recycles,
        "signed_lift_branch_recycles_to_terminal_gap": signed_lift_recycles,
        "alpha_formula_signed_coefficient_lift_proved": False,
        "alpha_signed_weight_law_from_precauchy_arithmetic_identity_proved": False,
        "independent_noncanonical_precauchy_arithmetic_identity_statement_proved": False,
        "actual_noncanonical_moving_block_spread_ncb_lk_proved": False,
        "alpha_row_anchor_phase_emission_formula_proved": False,
        "pointwise_same_formal_unit_primitive_alpha_delta_kernel_table_with_nonzero_rank_proved": False,
        "pdec_cap_or_internal_clean_kls_large_sieve_proved": False,
        "explicit_model_gap_and_finite_dprc_ledger_proved": False,
        "dstructure_tail_log4_finite_rankin_full_ledger_independent_acceptance_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": SIGNED_LIFT,
        "terminal_gap_after_router": f"{GLOBAL_TERMINAL} AND {MODEL_LEDGER}",
        "alpha_formula_remaining_non_recycling_basis": reordered_basis,
        "next_direct_attack_target": "AlphaFormulaCarryShellCongruenceRowFormulaLedger",
        "secondary_attack_targets": [
            "AlphaFormulaSourceTupleToCarryShellVariableBindingLedger",
            "AlphaFormulaPhaseWheelCompatibilityLedger",
            "AlphaFormulaAnchorCollarOverloadNamedReturnLedger",
            f"{GLOBAL_TERMINAL} AND {MODEL_LEDGER}",
            DSTRUCTURE_GATE,
        ],
        "sync_chain": sync_chain(),
        "sync_law": (
            "The signed-lift branch is not an acyclic self-contained exit in the present corpus. "
            "Its weight-law subbranch returns through the independent identity taxonomy and actual moving-block/NC-BLK "
            "to the registered global terminal capacity and explicit model-gap ledgers."
        ),
        "plain_conclusion": (
            "`AlphaFormulaSignedCoefficientLiftLedger` 的当前首攻链条已同步回流：signed lift -> signed weight law "
            "-> independent pre-Cauchy identity -> actual moving-block/NC-BLK -> "
            "`PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve AND ExplicitModelGapAndFiniteDPRCLedger`。"
            "因此 signed-lift 分支不是新的非循环自足出口；下一步应改攻 alpha formula 内的非回流候选，"
            "优先 `AlphaFormulaCarryShellCongruenceRowFormulaLedger`，同时保留终端容量/模型余量和 DStructure/Rankin 验收门。"
        ),
        "rows": rows,
        "source_hashes": source_hashes(),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict alpha formula signed-lift 终端同步路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"same_theorem_target_preserved={fmt_bool(result['same_theorem_target_preserved'])}",
        f"no_theorem_switch={fmt_bool(result['no_theorem_switch'])}",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"alpha_formula_signed_lift_terminal_sync_router_closed={fmt_bool(result['alpha_formula_signed_lift_terminal_sync_router_closed'])}",
        f"signed_lift_branch_recycles_to_terminal_gap={fmt_bool(result['signed_lift_branch_recycles_to_terminal_gap'])}",
        f"alpha_formula_signed_coefficient_lift_proved={fmt_bool(result['alpha_formula_signed_coefficient_lift_proved'])}",
        f"alpha_row_anchor_phase_emission_formula_proved={fmt_bool(result['alpha_row_anchor_phase_emission_formula_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 同步链",
        "",
        "```text",
    ]
    for item in result["sync_chain"]:
        lines.append(f"{item['from']} -> {item['to']}")
    lines.extend(
        [
            "```",
            "",
            "## 2. signed-lift 回流律",
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
            "保留并行验收门：",
            "",
            "```text",
            f"{GLOBAL_TERMINAL} AND {MODEL_LEDGER} AND {DSTRUCTURE_GATE}",
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
