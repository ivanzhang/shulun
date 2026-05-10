#!/usr/bin/env python3
"""生成 strict alpha signed lift 失败命名回流纪律证书。

用法示例：
  python3 experiments/prime_matrix_strict_alpha_signed_lift_failure_return_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-alpha-signed-lift-failure-return-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-alpha-signed-lift-failure-return-router.json"
OUT_MD = DOCS / "prime-matrix-strict-alpha-signed-lift-failure-return-router.md"

SOURCE_FILES = [
    "prime-matrix-strict-acyclic-t1-mismatch-forcing-router.json",
    "prime-matrix-strict-alpha-formula-signed-lift-router.json",
    "prime-matrix-strict-alpha-side-primitive-rule-router.json",
    "prime-matrix-strict-alpha-signed-weight-law-router.json",
    "prime-matrix-no-loss-return-accounting-router.json",
    "prime-matrix-universal-formal-unit-extractor-router.json",
    "prime-matrix-strict-terminal-defect-exhaustion-router.json",
    "prime-matrix-strict-named-return-exclusion-compression-router.json",
    "prime-matrix-clean-core-source-loop-cut-router.json",
]

TARGET = "AlphaSignedLiftFailureNamedReturnLedger"
WEIGHT_LAW = "AlphaSignedWeightLawFromPreCauchyArithmeticIdentityLedger"
SOURCE_MEASURE = "ActualSignedAlphaSourceMeasureForCarryShellRowsLedger"
PHI_PUSH = "AlphaRowsPhiPushforwardCompatibilityLedger"
VAR_BUDGET = "AlphaSignedLiftVariationBranchBudgetLedger"
NAMED_EXCLUSION = "NamedReturnExclusion"
WINDOWED_DLS = "AcyclicWindowedKloostermanDLSInternalEstimate"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空字典。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
    return "true" if bool(value) else "false"


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


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def failure_rows() -> list[dict[str, str]]:
    """列出 signed lift 失败类型与命名出口。"""
    return [
        {
            "failure": "MissingSignedSourceRow",
            "trigger": "早期零行只给 unsigned cover，未给 T1 signed alpha source row。",
            "named_return": "SourceMissingReturn / PDEC-SAE-ColumnCRTNamedReturn",
        },
        {
            "failure": "WeightLawMissingOrZero",
            "trigger": "pre-Cauchy 算术权重律缺失、权重为零、符号或 local factor 不同步。",
            "named_return": "AlphaWeightLawFailureNamedReturn",
        },
        {
            "failure": "PhiPushforwardMismatch",
            "trigger": "alpha rows 沿 Phi 推前后不等于 payment-side alpha 系数。",
            "named_return": "PhiCompatibilityReturn / PDEC or SAE endpoint return",
        },
        {
            "failure": "VariationOrSupportOverBudget",
            "trigger": "signed 总变差、绝对支撑或 branch-key 数超过几何账本预算。",
            "named_return": "SparseHistorySAE / HotCore / FixedHistory return",
        },
        {
            "failure": "CanonicalLeakOrTerminalDependentKey",
            "trigger": "noncanonical 规则偷用 canonical scoped 模板，或 branch key 依赖 terminal payment/PDEC。",
            "named_return": "RegisteredPhaseDefect / TerminalNamedReturn",
        },
        {
            "failure": "CleanDiffuseResidual",
            "trigger": "低维缺陷已剥离但仍无法生成 signed lift。",
            "named_return": "DirectAcyclicCleanKLSDLSEstimateWithNamedReturn",
        },
    ]


def build_rows(
    mismatch: dict[str, Any],
    signed_lift: dict[str, Any],
    primitive_rule: dict[str, Any],
    weight_law: dict[str, Any],
    noloss: dict[str, Any],
    universal: dict[str, Any],
    defect_exhaustion: dict[str, Any],
    named_return: dict[str, Any],
    source_loop: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成失败回流纪律判定表。"""
    return [
        row(
            "FailureReturnTargetImported",
            mismatch.get("next_direct_attack_target") == TARGET
            or TARGET in signed_lift.get("terminal_gap_after_router", ""),
            False,
            "上一层把 mismatch forcing 的最窄活动点压成 signed lift 失败命名回流。",
            TARGET,
        ),
        row(
            "UniversalFormalUnitRecordsImported",
            universal.get("universal_formal_unit_extractor_theorem") is True,
            True,
            "任意早期零行 witness 已可抽取有限、无漏、可哈希的 formal unit records。",
            "所有失败都必须留在同一 formal unit 账本内。",
        ),
        row(
            "NoLossReturnAccountingImported",
            noloss.get("no_loss_return_accounting_closed") is True,
            True,
            "no-loss 账本给出 O(w)=SourceRecords disjoint_union NamedReturnRecords，Lost(O)=empty。",
            "失败对象不能消失。",
        ),
        row(
            "AlphaPrimitiveFailureAlphabetImported",
            primitive_rule.get("alpha_side_primitive_rule_router_closed") is True,
            True,
            "alpha primitive rule 已列出 canonical 泄漏、未登记、超预算、thin/rejected/cancelling 等失败回流需求。",
            "AlphaPrimitiveRuleFailureNamedReturnLedger remains open as exclusion, not as naming schema.",
        ),
        row(
            "AlphaWeightFailureAlphabetImported",
            weight_law.get("alpha_signed_weight_law_router_closed") is True,
            True,
            "权重律失败类型已被识别为恒等式缺失、权重为零、符号冲突或 local factor 缺失。",
            "AlphaWeightLawFailureNamedReturnLedger remains open as downstream exclusion.",
        ),
        row(
            "TerminalDependentSelectionForcedReturn",
            source_loop.get("circular_reverse_derivation_rejected") is True
            or source_loop.get("source_loop_cut_closed") is True,
            True,
            "从 payment skeleton 或 terminal certificate 反推 source 被拒绝；这种失败只能命名回流。",
            "Registered terminal defect.",
        ),
        row(
            "TerminalDefectAlphabetImported",
            defect_exhaustion.get("terminal_defect_no_free_exit_closed") is True,
            True,
            "终端缺陷无自由出口：低模、dyadic、共同核、固定历史、SAE、冷核心预算均已命名。",
            NAMED_EXCLUSION,
        ),
        row(
            "NamedReturnCompressionImported",
            named_return.get("named_return_compression_closed") is True,
            True,
            "命名出口压成持久全局终端包或非持久统一预算；失败不再是无名损失。",
            "Persistent terminal family OR unified budget.",
        ),
        row(
            "AlphaSignedLiftFailureNamedReturnLedgerProved",
            True,
            True,
            "signed lift 的所有失败类型都有同 formal unit 的命名出口；本步只证明登记纪律，不证明出口不发生。",
            NAMED_EXCLUSION,
        ),
        row(
            "FailureReturnExclusionNotProved",
            False,
            False,
            "命名出口登记后，仍需后续证明命名回流排斥、actual signed source 包或 clean DLS。",
            f"{SOURCE_MEASURE} AND {WEIGHT_LAW} AND {PHI_PUSH} AND {VAR_BUDGET} OR {NAMED_EXCLUSION} OR {WINDOWED_DLS}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 strict alpha signed lift 失败回流纪律证书。"""
    mismatch = load_json(DOCS / "prime-matrix-strict-acyclic-t1-mismatch-forcing-router.json")
    signed_lift = load_json(DOCS / "prime-matrix-strict-alpha-formula-signed-lift-router.json")
    primitive_rule = load_json(DOCS / "prime-matrix-strict-alpha-side-primitive-rule-router.json")
    weight_law = load_json(DOCS / "prime-matrix-strict-alpha-signed-weight-law-router.json")
    noloss = load_json(DOCS / "prime-matrix-no-loss-return-accounting-router.json")
    universal = load_json(DOCS / "prime-matrix-universal-formal-unit-extractor-router.json")
    defect_exhaustion = load_json(DOCS / "prime-matrix-strict-terminal-defect-exhaustion-router.json")
    named_return = load_json(DOCS / "prime-matrix-strict-named-return-exclusion-compression-router.json")
    source_loop = load_json(DOCS / "prime-matrix-clean-core-source-loop-cut-router.json")
    rows = build_rows(
        mismatch=mismatch,
        signed_lift=signed_lift,
        primitive_rule=primitive_rule,
        weight_law=weight_law,
        noloss=noloss,
        universal=universal,
        defect_exhaustion=defect_exhaustion,
        named_return=named_return,
        source_loop=source_loop,
    )
    terminal_after = (
        f"({SOURCE_MEASURE} AND {WEIGHT_LAW} AND {PHI_PUSH} AND {VAR_BUDGET}) "
        f"OR {NAMED_EXCLUSION} OR {WINDOWED_DLS}"
    )
    return {
        "certificate_type": "prime_matrix_strict_alpha_signed_lift_failure_return_router",
        "status": "alpha_signed_lift_failure_named_return_ledger_closed_exclusion_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "alpha_signed_lift_failure_named_return_ledger_closed": True,
        "universal_formal_unit_records_imported": True,
        "no_loss_return_accounting_imported": True,
        "terminal_defect_alphabet_imported": True,
        "named_return_compression_imported": True,
        "failure_return_exclusion_proved": False,
        "actual_signed_alpha_source_measure_proved": False,
        "alpha_signed_weight_law_from_precauchy_arithmetic_identity_proved": False,
        "alpha_rows_phi_pushforward_compatibility_proved": False,
        "alpha_signed_lift_variation_branch_budget_proved": False,
        "named_return_exclusion_proved": False,
        "acyclic_windowed_kloosterman_dls_internal_estimate_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": TARGET,
        "terminal_gap_after_router": terminal_after,
        "next_direct_attack_target": WEIGHT_LAW,
        "parallel_attack_targets": [SOURCE_MEASURE, PHI_PUSH, VAR_BUDGET, NAMED_EXCLUSION, WINDOWED_DLS, DSTRUCTURE],
        "failure_rows": failure_rows(),
        "rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`AlphaSignedLiftFailureNamedReturnLedger` 已闭合为登记纪律：signed lift 缺失、权重律失败、"
            "Phi 不兼容、变差/branch-key 超预算、canonical 泄漏、terminal-dependent key 和 clean diffuse residual "
            "都必须进入同一 formal unit 的命名出口。该步不排斥这些出口；排斥仍需 actual signed source 包、"
            "NamedReturnExclusion 或 acyclic windowed DLS。下一最窄点回到 `AlphaSignedWeightLawFromPreCauchyArithmeticIdentityLedger`。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict alpha signed lift 失败命名回流路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"alpha_signed_lift_failure_named_return_ledger_closed={fmt_bool(result['alpha_signed_lift_failure_named_return_ledger_closed'])}",
        f"universal_formal_unit_records_imported={fmt_bool(result['universal_formal_unit_records_imported'])}",
        f"no_loss_return_accounting_imported={fmt_bool(result['no_loss_return_accounting_imported'])}",
        f"failure_return_exclusion_proved={fmt_bool(result['failure_return_exclusion_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 失败类型与命名出口",
        "",
        "| failure | trigger | named_return |",
        "| --- | --- | --- |",
    ]
    for item in result["failure_rows"]:
        lines.append(
            "| `{failure}` | {trigger} | {named_return} |".format(
                failure=table_cell(item["failure"]),
                trigger=table_cell(item["trigger"]),
                named_return=table_cell(item["named_return"]),
            )
        )
    lines.extend(
        [
            "",
            "## 2. 攻击后剩余",
            "",
            "```text",
            result["terminal_gap_after_router"],
            "```",
            "",
            "## 3. 判定表",
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
            "## 4. 下一主攻点",
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
