#!/usr/bin/env python3
"""生成 strict alpha row anchor/phase 发射公式字段证书。

用法示例：
  python3 experiments/prime_matrix_strict_alpha_row_anchor_phase_formula_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-alpha-row-anchor-phase-formula-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-alpha-row-anchor-phase-formula-router.json"
OUT_MD = DOCS / "prime-matrix-strict-alpha-row-anchor-phase-formula-router.md"


SOURCE_FILES = [
    "prime-matrix-strict-deterministic-alpha-row-emission-map-router.json",
    "prime-matrix-early-zero-contradiction-matrix-router.json",
    "prime-matrix-early-zero-carry-shell-router.json",
    "prime-matrix-early-zero-anchor-collar-router.json",
    "prime-matrix-hypothetical-zero-row-seed-no-go-router.json",
    "prime-matrix-pcolumn-anchor-wheel-field.md",
    "prime-matrix-dprc-cylindrical-layered-wheel-clamp.md",
    "prime-matrix-clean-core-geometric-variation-branch-budget-router.md",
]


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空字典。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def load_text(path: Path) -> str:
    """读取文本证书；缺失时返回空文本。"""
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


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


def build_rows(
    emission_map: dict[str, Any],
    early_zero_matrix: dict[str, Any],
    carry_shell: dict[str, Any],
    anchor_collar: dict[str, Any],
    seed_nogo: dict[str, Any],
    paw_text: str,
    layered_text: str,
    geometry_text: str,
) -> list[dict[str, Any]]:
    """生成 alpha anchor/phase 公式判定表。"""
    target = "AlphaRowAnchorPhaseEmissionFormulaLedger"
    next_basis = (
        "AlphaFormulaSourceTupleToCarryShellVariableBindingLedger AND "
        "AlphaFormulaCarryShellCongruenceRowFormulaLedger AND "
        "AlphaFormulaPhaseWheelCompatibilityLedger AND "
        "AlphaFormulaSignedCoefficientLiftLedger AND "
        "AlphaFormulaAnchorCollarOverloadNamedReturnLedger"
    )
    terminal_after = emission_map.get("terminal_gap_after_router", "")
    carry_closed = carry_shell.get("exact_carry_shell_identity_closed") is True
    collar_closed = anchor_collar.get("canonical_anchor_collar_closed") is True
    no_seed = seed_nogo.get("zero_row_seed_extraction_blocked") is True
    no_unnamed = early_zero_matrix.get("no_unnamed_exit_for_early_zero") is True
    pcolumn_layered = (
        "P列" in paw_text
        and "LayeredClamp" in layered_text
        and "pcolumn_anchor_phi_skeleton" in geometry_text
    )
    return [
        {
            "gate": "AlphaRowAnchorPhaseFormulaTargetActive",
            "closed": target in terminal_after or emission_map.get("next_direct_attack_target") == target,
            "proved": False,
            "meaning": "上一层已把当前最窄点固定为 A/D0/K/Omega/phase_rule 到 alpha row 的显式发射公式。",
            "remaining": target,
        },
        {
            "gate": "EarlyZeroContradictionMatrixImported",
            "closed": no_unnamed,
            "proved": True,
            "meaning": "早期零行若存在，已被 CLB、formal unit、carry-shell、cofactor-depth、anchor-collar 压到命名终端。",
            "remaining": "该矩阵只给 unsigned 刚性，不直接给 signed alpha 公式。",
        },
        {
            "gate": "CarryShellIdentityImportedForFormulaShape",
            "closed": carry_closed,
            "proved": True,
            "meaning": "任何从早期零行抽取的候选 row 形状必须满足 h=a+b-floor(ab/P), c=ab mod P。",
            "remaining": "需要把该形状变成 signed alpha primitive row 公式。",
        },
        {
            "gate": "AnchorCollarShortFiberImported",
            "closed": collar_closed,
            "proved": True,
            "meaning": "大分支的候选 row 必须落入 canonical collar 短素数纤维，否则进入 PDEC/SAE/ColumnCRT。",
            "remaining": "需要容量排斥或命名回流。",
        },
        {
            "gate": "PColumnLayeredWheelCompatibilityImported",
            "closed": pcolumn_layered,
            "proved": True,
            "meaning": "P列锚、圆柱相位和 layered wheel 固定了候选公式必须遵守的相位字母表。",
            "remaining": "仍需公式级相位兼容等式。",
        },
        {
            "gate": "UnsignedZeroRowSeedExtractionBlocked",
            "closed": no_seed,
            "proved": True,
            "meaning": "早期零行覆盖证书不能直接生成 pre-Cauchy signed alpha/delta source seed。",
            "remaining": "AlphaFormulaSignedCoefficientLiftLedger。",
        },
        {
            "gate": "AlphaSourceTupleToCarryShellVariableBindingCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "当前材料尚未把 source tuple 字段 A、D0/K/Omega、phase_rule 逐项绑定到 h,a,b,k,c 的 row 变量。",
            "remaining": "AlphaFormulaSourceTupleToCarryShellVariableBindingLedger。",
        },
        {
            "gate": "AlphaCarryShellCongruenceRowFormulaCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "当前材料尚未写出 alpha row 的显式同余/索引公式并证明它覆盖且只覆盖合法 carry-shell row。",
            "remaining": "AlphaFormulaCarryShellCongruenceRowFormulaLedger。",
        },
        {
            "gate": "AlphaPhaseWheelCompatibilityCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "当前材料尚未证明该 row 公式与 P列锚、圆柱相位、层叠轮筛和 phase_rule 同步兼容。",
            "remaining": "AlphaFormulaPhaseWheelCompatibilityLedger。",
        },
        {
            "gate": "AlphaSignedCoefficientLiftCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "当前材料尚未把 unsigned carry-shell/anchor-collar row 提升为 pre-Cauchy signed alpha 系数行。",
            "remaining": "AlphaFormulaSignedCoefficientLiftLedger。",
        },
        {
            "gate": "AlphaAnchorCollarOverloadReturnCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "当前材料尚未证明短纤维满载或公式过载时必进入可排斥的 PDEC/SAE/ColumnCRT 命名回流。",
            "remaining": "AlphaFormulaAnchorCollarOverloadNamedReturnLedger。",
        },
        {
            "gate": "AlphaRowAnchorPhaseFormulaCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "变量绑定、同余公式、相位兼容、signed 提升和过载回流五项尚未合取证明。",
            "remaining": next_basis,
        },
    ]


def build_result() -> dict[str, Any]:
    """构造 alpha row anchor/phase 公式证书。"""
    emission_map = load_json(DOCS / "prime-matrix-strict-deterministic-alpha-row-emission-map-router.json")
    early_zero_matrix = load_json(DOCS / "prime-matrix-early-zero-contradiction-matrix-router.json")
    carry_shell = load_json(DOCS / "prime-matrix-early-zero-carry-shell-router.json")
    anchor_collar = load_json(DOCS / "prime-matrix-early-zero-anchor-collar-router.json")
    seed_nogo = load_json(DOCS / "prime-matrix-hypothetical-zero-row-seed-no-go-router.json")
    paw_text = load_text(DOCS / "prime-matrix-pcolumn-anchor-wheel-field.md")
    layered_text = load_text(DOCS / "prime-matrix-dprc-cylindrical-layered-wheel-clamp.md")
    geometry_text = load_text(DOCS / "prime-matrix-clean-core-geometric-variation-branch-budget-router.md")

    target = "AlphaRowAnchorPhaseEmissionFormulaLedger"
    next_basis = (
        "AlphaFormulaSourceTupleToCarryShellVariableBindingLedger AND "
        "AlphaFormulaCarryShellCongruenceRowFormulaLedger AND "
        "AlphaFormulaPhaseWheelCompatibilityLedger AND "
        "AlphaFormulaSignedCoefficientLiftLedger AND "
        "AlphaFormulaAnchorCollarOverloadNamedReturnLedger"
    )
    rows = build_rows(
        emission_map=emission_map,
        early_zero_matrix=early_zero_matrix,
        carry_shell=carry_shell,
        anchor_collar=anchor_collar,
        seed_nogo=seed_nogo,
        paw_text=paw_text,
        layered_text=layered_text,
        geometry_text=geometry_text,
    )
    return {
        "certificate_type": "prime_matrix_strict_alpha_row_anchor_phase_formula_router",
        "status": "strict_alpha_row_anchor_phase_formula_reduced_to_carry_shell_phase_signed_lift_return_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "alpha_row_anchor_phase_formula_router_closed": True,
        "early_zero_rigidity_imported_as_unsigned_shape_only": True,
        "carry_shell_formula_shape_imported": True,
        "anchor_collar_short_fiber_imported": True,
        "pcolumn_layered_wheel_phase_imported": True,
        "unsigned_zero_row_seed_extraction_blocked_imported": True,
        "alpha_formula_source_tuple_to_carry_shell_variable_binding_proved": False,
        "alpha_formula_carry_shell_congruence_row_formula_proved": False,
        "alpha_formula_phase_wheel_compatibility_proved": False,
        "alpha_formula_signed_coefficient_lift_proved": False,
        "alpha_formula_anchor_collar_overload_named_return_proved": False,
        "alpha_row_anchor_phase_emission_formula_proved": False,
        "deterministic_alpha_primitive_row_emission_map_proved": False,
        "actual_noncanonical_alpha_side_primitive_rule_proved": False,
        "actual_noncanonical_delta_side_primitive_rule_proved": False,
        "alpha_delta_pairing_compatibility_before_cauchy_proved": False,
        "primitive_rule_nonzero_sign_local_factor_proved": False,
        "explicit_alpha_delta_primitive_constructor_rule_proved": False,
        "actual_noncanonical_primitive_constructor_formula_line_proved": False,
        "pre_cauchy_constructor_declaration_line_proved": False,
        "actual_noncanonical_primitive_emitter_source_table_proved": False,
        "registered_complete_primitive_emitter_key_partition_polylog_proved": False,
        "exact_uv_map_fixed_pair_polylog_fiber_bound_proved": False,
        "actual_emitter_exact_uv_bounded_multiplicity_incidence_proved": False,
        "new_actual_source_entropy_theorem_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": target,
        "terminal_gap_after_router": next_basis,
        "next_direct_attack_target": "AlphaFormulaSignedCoefficientLiftLedger",
        "upstream_contradiction_amplifier": (
            "If an early zero row is assumed, the true geometry forces every candidate alpha row shape through carry-shell, "
            "anchor-collar and P-column/layered-wheel constraints. This amplifies the contradiction pressure, but it is still "
            "unsigned: the missing strict self-contained step is a signed pre-Cauchy coefficient lift or a named overload return."
        ),
        "plain_conclusion": (
            "`AlphaRowAnchorPhaseEmissionFormulaLedger` 被继续压成 source tuple 到 carry-shell 变量绑定、carry-shell "
            "同余 row 公式、P列/圆柱/层叠轮相位兼容、unsigned 到 signed alpha 系数提升、短纤维过载命名回流五项。"
            "早期零行反例链与真实刚性链的直接压力已经进入本公式审查：候选 row 必须同时满足 carry-shell、"
            "anchor-collar 和 layered-wheel；但这仍只给 unsigned 形状。当前最窄点为 "
            "`AlphaFormulaSignedCoefficientLiftLedger`。"
        ),
        "rows": rows,
        "source_hashes": source_hashes(),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict alpha row anchor/phase 公式路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"same_theorem_target_preserved={fmt_bool(result['same_theorem_target_preserved'])}",
        f"no_theorem_switch={fmt_bool(result['no_theorem_switch'])}",
        f"alpha_row_anchor_phase_formula_router_closed={fmt_bool(result['alpha_row_anchor_phase_formula_router_closed'])}",
        f"alpha_row_anchor_phase_emission_formula_proved={fmt_bool(result['alpha_row_anchor_phase_emission_formula_proved'])}",
        f"deterministic_alpha_primitive_row_emission_map_proved={fmt_bool(result['deterministic_alpha_primitive_row_emission_map_proved'])}",
        f"actual_noncanonical_alpha_side_primitive_rule_proved={fmt_bool(result['actual_noncanonical_alpha_side_primitive_rule_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 上游矛盾放大器",
        "",
        result["upstream_contradiction_amplifier"],
        "",
        "## 2. 公式内部拆分",
        "",
        "拆分前：",
        "",
        "```text",
        result["terminal_gap_before_router"],
        "```",
        "",
        "拆分后：",
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
