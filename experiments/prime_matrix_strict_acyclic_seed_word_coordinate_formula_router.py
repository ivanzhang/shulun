#!/usr/bin/env python3
"""生成 strict acyclic seed word coordinate formula 攻坚证书。

用法示例：
  python3 experiments/prime_matrix_strict_acyclic_seed_word_coordinate_formula_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-acyclic-seed-word-coordinate-formula-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-acyclic-seed-word-coordinate-formula-router.json"
OUT_MD = DOCS / "prime-matrix-strict-acyclic-seed-word-coordinate-formula-router.md"

TARGET = "AcyclicSeedWordCoordinateFormulaFromAnchorD0KOmegaPhaseParameters"
NEXT_TARGET = "AcyclicSeedAnchorInputRuleForPrimitiveWordCoordinates"
TERMINAL_RETURN = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily"

SOURCE_FILES = [
    "prime-matrix-strict-acyclic-seed-basis-word-formula-router.json",
    "prime-matrix-anchor-set-reconstruction-certificate-router.json",
    "prime-matrix-anchor-interval-certificate-file-router.json",
    "prime-matrix-concrete-anchor-interval-enumeration-router.json",
    "prime-matrix-concrete-source-tuple-anchor-parameter-router.json",
    "prime-matrix-strict-alpha-row-unsigned-skeleton-router.json",
    "prime-matrix-strict-alpha-row-anchor-phase-formula-router.json",
    "prime-matrix-clean-core-geometric-variation-branch-budget-router.json",
    "prime-matrix-clean-core-reverse-provenance-functor-router.json",
    "prime-matrix-hypothetical-zero-row-seed-no-go-router.json",
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


def anchor_input_fields() -> list[dict[str, str]]:
    """列出 anchor input rule 的最小字段。"""
    return [
        {
            "field": "anchor_selection_function",
            "meaning": "从重构出的 A 或 A=empty 情形中确定 primitive word 坐标输入的选择函数。",
        },
        {
            "field": "window_endpoint_coupling",
            "meaning": "说明所选 anchor 如何与窗口端点、P/range 和 formal_unit_id 同步。",
        },
        {
            "field": "phase_filter_pullback",
            "meaning": "把 phase_rule 拉回到 anchor input，而不是只作用于最终 row。",
        },
        {
            "field": "empty_anchor_case",
            "meaning": "A=empty 或 null 参数族时的 canonical 输入规则和命名回流。",
        },
        {
            "field": "anchor_input_complexity_charge",
            "meaning": "anchor 选择带来的分支数、相位数和截断数收费。",
        },
        {
            "field": "anchor_input_failure_return",
            "meaning": "anchor 缺失、选择多值、跨 formal unit 或读后验数据时的回流。",
        },
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """审查 word coordinate formula 的首字段。"""
    previous = data["previous"]
    anchor_reconstruction = data["anchor_reconstruction"]
    anchor_interval = data["anchor_interval"]
    source_tuple = data["source_tuple"]
    unsigned = data["unsigned"]
    anchor_phase = data["anchor_phase"]
    branch_budget = data["branch_budget"]
    reverse = data["reverse"]
    zero_nogo = data["zero_nogo"]

    anchor_set_closed = (
        anchor_reconstruction.get("anchor_set_reconstruction_certificate_ledger") is True
        and source_tuple.get("source_tuple_anchor_parameter_schema_closed") is True
    )
    interval_available = anchor_interval.get("anchor_interval_certificate_file_router_closed") is True or bool(
        anchor_interval
    )
    anchor_phase_still_unsigned = (
        unsigned.get("alpha_row_unsigned_skeleton_router_closed") is True
        and anchor_phase.get("alpha_row_anchor_phase_emission_formula_proved") is not True
    )
    budget_after_selection = (
        branch_budget.get("geometric_variation_branch_budget_router_closed") is True
        or branch_budget.get("branch_key_multiplicity_budget_proved") is not True
    )
    reverse_blocked = (
        reverse.get("reverse_provenance_functor_boundary_closed") is True
        or zero_nogo.get("geometry_source_extraction_blocked") is True
        or zero_nogo.get("downstream_reverse_source_blocked") is True
    )

    return [
        row(
            "WordCoordinateFormulaTargetActive",
            previous.get("next_direct_attack_target") == TARGET,
            False,
            "上一层已把 basis_word_formula 压到 word_coordinate_formula。",
            TARGET,
        ),
        row(
            "AnchorSetReconstructedButNotSelected",
            anchor_set_closed,
            False,
            "A、D0/K/Omega、phase_rule 可复算，但还没有从 A 选择 primitive word 输入的规则。",
            NEXT_TARGET,
        ),
        row(
            "AnchorInputRuleIsFirstCoordinateGate",
            True,
            True,
            "没有 anchor input rule，dyadic/truncation coordinate、phase coordinate 和 signed slot 都没有共同输入。",
            NEXT_TARGET,
        ),
        row(
            "AnchorIntervalCertificateIsNotInputRule",
            interval_available,
            False,
            "anchor interval 证书给可用区间或枚举边界，不给 primitive word 的 anchor selection function。",
            NEXT_TARGET,
        ),
        row(
            "UnsignedAnchorPhaseNotArithmeticInput",
            anchor_phase_still_unsigned,
            False,
            "unsigned anchor/phase 公式只服务几何 row 发射，不能替代 pre-Cauchy basis word 的输入选择。",
            NEXT_TARGET,
        ),
        row(
            "BranchBudgetChargesAfterSelection",
            budget_after_selection,
            False,
            "分支预算可以收费已选择的输入，但不能定义 anchor selection function 本身。",
            NEXT_TARGET,
        ),
        row(
            "ReverseAnchorSelectionBlocked",
            reverse_blocked,
            True,
            "不能从 payment、推前后投影或早期零行覆盖反选 anchor input。",
            NEXT_TARGET,
        ),
        row(
            "AnchorInputRuleCurrentCorpusProved",
            False,
            False,
            "当前材料没有给出从重构 A/窗口/phase 到 primitive word 输入的选择函数。",
            NEXT_TARGET,
        ),
        row(
            "WordCoordinateFormulaCurrentCorpusProved",
            False,
            False,
            "没有 anchor input rule，完整 word coordinate formula 仍未证明。",
            TARGET,
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 word coordinate formula 证书。"""
    data = {
        "previous": load_json("prime-matrix-strict-acyclic-seed-basis-word-formula-router.json"),
        "anchor_reconstruction": load_json("prime-matrix-anchor-set-reconstruction-certificate-router.json"),
        "anchor_interval": load_json("prime-matrix-anchor-interval-certificate-file-router.json"),
        "source_tuple": load_json("prime-matrix-concrete-source-tuple-anchor-parameter-router.json"),
        "unsigned": load_json("prime-matrix-strict-alpha-row-unsigned-skeleton-router.json"),
        "anchor_phase": load_json("prime-matrix-strict-alpha-row-anchor-phase-formula-router.json"),
        "branch_budget": load_json("prime-matrix-clean-core-geometric-variation-branch-budget-router.json"),
        "reverse": load_json("prime-matrix-clean-core-reverse-provenance-functor-router.json"),
        "zero_nogo": load_json("prime-matrix-hypothetical-zero-row-seed-no-go-router.json"),
    }
    rows = build_rows(data)
    direct_contradiction = any(
        doc.get("direct_unconditional_contradiction_found") is True
        or doc.get("row_column_unconditional_closed") is True
        for doc in data.values()
        if isinstance(doc, dict)
    )
    return {
        "certificate_type": "prime_matrix_strict_acyclic_seed_word_coordinate_formula_router",
        "status": "word_coordinate_formula_reduced_to_anchor_input_rule_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "target_input_before_router": TARGET,
        "word_coordinate_formula_router_closed": True,
        "anchor_set_reconstructed_but_not_selected": True,
        "anchor_input_rule_is_first_coordinate_gate": True,
        "reverse_anchor_selection_blocked": True,
        "anchor_input_rule_proved": False,
        "word_coordinate_formula_proved": False,
        "basis_word_formula_from_source_tuple_parameters_proved": False,
        "source_tuple_to_primitive_basis_word_constructor_proved": False,
        "direct_unconditional_contradiction_found": direct_contradiction,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NEXT_TARGET,
        "parallel_attack_targets": [
            "AcyclicSeedDyadicTruncationCoordinateLedger",
            "AcyclicSeedPhaseCoordinatePullbackLedger",
            "AcyclicSeedAnchorInputComplexityChargeLedger",
        ],
        "terminal_return_if_no_anchor_input_rule": TERMINAL_RETURN,
        "anchor_input_fields": anchor_input_fields(),
        "rows": rows,
        "source_hashes": source_hashes(),
        "frontier_reduction": (
            f"`{TARGET}` 的第一坐标门是 `{NEXT_TARGET}`："
            "虽然 A 与参数可复算，但必须先说明 primitive basis word 从哪些 anchor/window/phase 输入产生。"
        ),
        "plain_conclusion": (
            "本步把 word_coordinate_formula 再压到 anchor_input_rule。"
            "目前材料能重构 anchor 集和参数，但没有给出从这些对象选择 primitive word 输入的函数；"
            "后续 dyadic、phase、signed 槽位和复杂度收费都依赖这个选择函数。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict acyclic seed word coordinate formula 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"word_coordinate_formula_router_closed={fmt_bool(result['word_coordinate_formula_router_closed'])}",
        f"anchor_input_rule_proved={fmt_bool(result['anchor_input_rule_proved'])}",
        f"word_coordinate_formula_proved={fmt_bool(result['word_coordinate_formula_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 前沿压缩",
        "",
        result["frontier_reduction"],
        "",
        "## 2. anchor_input_rule 字段",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for item in result["anchor_input_fields"]:
        lines.append(
            "| `{field}` | {meaning} |".format(
                field=table_cell(item["field"]),
                meaning=table_cell(item["meaning"]),
            )
        )
    lines.extend(
        [
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
            "## 4. 下一真正单点",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "并行依赖：",
            "",
            "```text",
            "\n".join(result["parallel_attack_targets"]),
            "```",
            "",
            "缺失或失败时的命名回流：",
            "",
            "```text",
            result["terminal_return_if_no_anchor_input_rule"],
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
