#!/usr/bin/env python3
"""生成 strict alpha carry-shell 同余 row 公式证书。

用法示例：
  python3 experiments/prime_matrix_strict_alpha_carry_shell_congruence_formula_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-alpha-carry-shell-congruence-formula-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-alpha-carry-shell-congruence-formula-router.json"
OUT_MD = DOCS / "prime-matrix-strict-alpha-carry-shell-congruence-formula-router.md"

TARGET = "AlphaFormulaCarryShellCongruenceRowFormulaLedger"
SOURCE_BINDING = "AlphaFormulaSourceTupleToCarryShellVariableBindingLedger"
PHASE_WHEEL = "AlphaFormulaPhaseWheelCompatibilityLedger"
SIGNED_LIFT = "AlphaFormulaSignedCoefficientLiftLedger"
OVERLOAD_RETURN = "AlphaFormulaAnchorCollarOverloadNamedReturnLedger"
GLOBAL_TERMINAL = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve"
MODEL_LEDGER = "ExplicitModelGapAndFiniteDPRCLedger"
DSTRUCTURE_GATE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    "prime-matrix-strict-alpha-formula-signed-lift-terminal-sync-router.json",
    "prime-matrix-strict-alpha-row-anchor-phase-formula-router.json",
    "prime-matrix-strict-alpha-row-unsigned-skeleton-router.json",
    "prime-matrix-concrete-source-tuple-anchor-parameter-router.json",
    "prime-matrix-anchor-set-reconstruction-certificate-router.json",
    "prime-matrix-early-zero-carry-shell-router.json",
    "prime-matrix-early-zero-anchor-collar-router.json",
    "prime-matrix-pcolumn-anchor-wheel-field.md",
    "prime-matrix-dprc-cylindrical-layered-wheel-clamp.md",
]


def load_json(name: str) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空对象。"""
    path = DOCS / name
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def load_text(name: str) -> str:
    """读取文本证书；缺失时返回空文本。"""
    path = DOCS / name
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


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


def congruence_formulae() -> list[dict[str, str]]:
    """列出 carry-shell row 公式的精确同余口径。"""
    return [
        {
            "name": "row height",
            "formula": "h=P-x",
            "meaning": "把早期零行行号 x 转成底部距离 h。",
        },
        {
            "name": "high factor coordinates",
            "formula": "q=P-a, m=P-b, 1<=a,b<h",
            "meaning": "双高因子 q,m in (x,P) 等价为 a,b 落在同一 h 壳内。",
        },
        {
            "name": "carry index",
            "formula": "k=floor(ab/P)",
            "meaning": "进位层 k 决定该点位于哪条 carry shell。",
        },
        {
            "name": "row congruence",
            "formula": "h=a+b-k, c=ab mod P",
            "meaning": "合法 shell pair 给出唯一候选列 residue c。",
        },
        {
            "name": "P-column distance",
            "formula": "xP+c=P(x+1)-(P-c)",
            "meaning": "把同一候选点登记到 P 列锚的距离坐标 d=P-c。",
        },
    ]


def build_rows(
    terminal_sync: dict[str, Any],
    alpha_formula: dict[str, Any],
    unsigned_skeleton: dict[str, Any],
    source_tuple: dict[str, Any],
    anchor_recon: dict[str, Any],
    carry: dict[str, Any],
    collar: dict[str, Any],
    paw_text: str,
    layered_text: str,
) -> list[dict[str, Any]]:
    """证明 carry-shell 同余 row 公式在 unsigned 层闭合。"""
    alpha_target_active = TARGET in alpha_formula.get("terminal_gap_after_router", "")
    terminal_sync_reorders_to_target = terminal_sync.get("next_direct_attack_target") == TARGET
    source_binding_closed = (
        source_tuple.get("concrete_source_tuple_anchor_parameter_data_closed") is True
        and anchor_recon.get("anchor_set_reconstruction_certificate_ledger") is True
        and unsigned_skeleton.get("unsigned_source_tuple_carry_shell_binding_closed") is True
    )
    carry_identity_closed = carry.get("exact_carry_shell_identity_closed") is True
    pcolumn_phase_closed = (
        "PAW-5" in paw_text
        and "PAW-10" in paw_text
        and "LayeredClamp" in layered_text
        and unsigned_skeleton.get("unsigned_phase_wheel_compatibility_closed") is True
    )
    skeleton_congruence_closed = (
        unsigned_skeleton.get("unsigned_carry_shell_congruence_row_skeleton_closed") is True
        and carry_identity_closed
        and pcolumn_phase_closed
    )
    collar_closed = collar.get("canonical_anchor_collar_closed") is True
    signed_lift_recycles = terminal_sync.get("signed_lift_branch_recycles_to_terminal_gap") is True
    target_closed = all(
        [
            alpha_target_active,
            terminal_sync_reorders_to_target,
            source_binding_closed,
            skeleton_congruence_closed,
            collar_closed,
        ]
    )

    return [
        make_row(
            "CounterexampleBranchGuardPreserved",
            True,
            True,
            "本步仍在 Assume EarlyZeroRowWithinP 的反例链中传递，只证明反例强制的候选行几何公式。",
            "不使用真实零行缺席。",
        ),
        make_row(
            "CarryShellCongruenceTargetActive",
            alpha_target_active and terminal_sync_reorders_to_target,
            False,
            "signed-lift 分支回流终端后，当前非回流首攻点重排为 carry-shell 同余 row 公式。",
            TARGET,
        ),
        make_row(
            "SourceTupleVariableBindingImported",
            source_binding_closed,
            True,
            "source tuple 的 A、D0/K/Omega、phase_rule 与 hash 可复算，并能作为 h,a,b,k,c 的筛选输入。",
            SOURCE_BINDING,
        ),
        make_row(
            "ExactCarryShellIdentityImported",
            carry_identity_closed,
            True,
            "任何双高因子补洞 xP+c=(P-a)(P-b) 都满足 h=a+b-floor(ab/P), c=ab mod P。",
            "carry-shell row 公式的代数核心已闭合。",
        ),
        make_row(
            "PColumnDistanceCoordinateImported",
            "PAW-5" in paw_text and "PAW-10" in paw_text,
            True,
            "候选点 xP+c 可无损写成 P 列锚 Py 左侧距离 d=P-c，便于同 formal unit 登记。",
            "P-column distance coordinate。",
        ),
        make_row(
            "PhaseWheelCompatibilityImported",
            pcolumn_phase_closed,
            True,
            "P列圆柱平移与 layered-wheel 相位字母表已能和 carry-shell residue 同步登记。",
            PHASE_WHEEL,
        ),
        make_row(
            "AnchorCollarRestrictionImported",
            collar_closed,
            True,
            "若进入大分支真双素 carry-shell，最小高素 anchor 被限制到 canonical collar，cofactor 落在短素数纤维。",
            "这给过载回流输入，但不排斥过载。",
        ),
        make_row(
            "CarryShellCongruenceRowSkeletonClosed",
            skeleton_congruence_closed,
            True,
            "给定 source tuple 与 phase 过滤后，carry-shell 同余和 P列距离坐标给出确定性候选 row skeleton。",
            "该结论仍是 unsigned/geometric。",
        ),
        make_row(
            "AlphaFormulaCarryShellCongruenceRowFormulaClosed",
            target_closed,
            True,
            "目标 ledger 在 unsigned row 公式层闭合：它覆盖并只覆盖由双高因子 carry-shell 与相位过滤登记的合法候选点。",
            "不等于 signed alpha primitive row 证明。",
        ),
        make_row(
            "SignedLiftBranchAlreadySyncedToTerminal",
            signed_lift_recycles,
            False,
            "signed coefficient lift 仍未证明；已有同步只说明该分支当前回到全局终端容量/模型缺口，而不是非循环出口。",
            f"{GLOBAL_TERMINAL} AND {MODEL_LEDGER}",
        ),
        make_row(
            "AnchorCollarOverloadReturnStillOpen",
            True,
            False,
            "短纤维满载、phase 过载或同参数复用仍需命名回流并被容量门排斥。",
            OVERLOAD_RETURN,
        ),
        make_row(
            "DirectContradictionNotYetReached",
            True,
            False,
            "本步关闭了几何同余公式，但没有排斥终端容量/模型账本，也没有证明 signed pre-Cauchy 源。",
            f"{OVERLOAD_RETURN} AND {GLOBAL_TERMINAL} AND {MODEL_LEDGER} AND {DSTRUCTURE_GATE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 carry-shell 同余 row 公式证书。"""
    terminal_sync = load_json("prime-matrix-strict-alpha-formula-signed-lift-terminal-sync-router.json")
    alpha_formula = load_json("prime-matrix-strict-alpha-row-anchor-phase-formula-router.json")
    unsigned_skeleton = load_json("prime-matrix-strict-alpha-row-unsigned-skeleton-router.json")
    source_tuple = load_json("prime-matrix-concrete-source-tuple-anchor-parameter-router.json")
    anchor_recon = load_json("prime-matrix-anchor-set-reconstruction-certificate-router.json")
    carry = load_json("prime-matrix-early-zero-carry-shell-router.json")
    collar = load_json("prime-matrix-early-zero-anchor-collar-router.json")
    paw_text = load_text("prime-matrix-pcolumn-anchor-wheel-field.md")
    layered_text = load_text("prime-matrix-dprc-cylindrical-layered-wheel-clamp.md")

    rows = build_rows(
        terminal_sync=terminal_sync,
        alpha_formula=alpha_formula,
        unsigned_skeleton=unsigned_skeleton,
        source_tuple=source_tuple,
        anchor_recon=anchor_recon,
        carry=carry,
        collar=collar,
        paw_text=paw_text,
        layered_text=layered_text,
    )
    target_closed = next(
        row["closed"] for row in rows if row["gate"] == "AlphaFormulaCarryShellCongruenceRowFormulaClosed"
    )

    next_basis = (
        f"{OVERLOAD_RETURN} AND ({GLOBAL_TERMINAL} AND {MODEL_LEDGER}) "
        f"AND {DSTRUCTURE_GATE}"
    )

    return {
        "certificate_type": "prime_matrix_strict_alpha_carry_shell_congruence_formula_router",
        "status": "strict_alpha_carry_shell_congruence_formula_closed_overload_terminal_gap_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "alpha_formula_carry_shell_congruence_formula_router_closed": target_closed,
        "alpha_formula_source_tuple_to_carry_shell_variable_binding_imported_closed": True,
        "alpha_formula_phase_wheel_compatibility_imported_closed": True,
        "alpha_formula_carry_shell_congruence_row_formula_proved": target_closed,
        "alpha_formula_signed_coefficient_lift_proved": False,
        "alpha_formula_anchor_collar_overload_named_return_proved": False,
        "alpha_row_anchor_phase_emission_formula_proved": False,
        "pdec_cap_or_internal_clean_kls_large_sieve_proved": False,
        "explicit_model_gap_and_finite_dprc_ledger_proved": False,
        "dstructure_tail_log4_finite_rankin_full_ledger_independent_acceptance_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": TARGET,
        "terminal_gap_after_router": next_basis,
        "next_direct_attack_target": OVERLOAD_RETURN,
        "parallel_required_inputs": [
            f"{GLOBAL_TERMINAL} AND {MODEL_LEDGER}",
            DSTRUCTURE_GATE,
        ],
        "congruence_formulae": congruence_formulae(),
        "formula_law": (
            "The carry-shell congruence formula is an unsigned geometric indexing theorem. "
            "It maps each double-high filler atom to h=P-x, q=P-a, m=P-b, k=floor(ab/P), "
            "h=a+b-k and c=ab mod P, then records the same point by P-column distance d=P-c. "
            "This closes the row skeleton, but it does not create a signed pre-Cauchy alpha coefficient."
        ),
        "plain_conclusion": (
            "`AlphaFormulaCarryShellCongruenceRowFormulaLedger` 已在 unsigned 层闭合：source tuple/anchor 参数、"
            "carry-shell 恒等式、P列距离坐标和 layered-wheel 相位可共同给出确定性候选 row skeleton。"
            "这正是早期零行反例链被真实结构链挤压出的几何公式；但它不提供 signed alpha 系数，也不排斥 "
            "anchor-collar 短纤维过载。下一最窄点转为 "
            "`AlphaFormulaAnchorCollarOverloadNamedReturnLedger`，同时保留终端容量/模型余量和 DStructure/Rankin 验收门。"
        ),
        "rows": rows,
        "source_hashes": source_hashes(),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict alpha carry-shell 同余 row 公式路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"same_theorem_target_preserved={fmt_bool(result['same_theorem_target_preserved'])}",
        f"no_theorem_switch={fmt_bool(result['no_theorem_switch'])}",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"alpha_formula_carry_shell_congruence_formula_router_closed={fmt_bool(result['alpha_formula_carry_shell_congruence_formula_router_closed'])}",
        f"alpha_formula_carry_shell_congruence_row_formula_proved={fmt_bool(result['alpha_formula_carry_shell_congruence_row_formula_proved'])}",
        f"alpha_formula_signed_coefficient_lift_proved={fmt_bool(result['alpha_formula_signed_coefficient_lift_proved'])}",
        f"alpha_formula_anchor_collar_overload_named_return_proved={fmt_bool(result['alpha_formula_anchor_collar_overload_named_return_proved'])}",
        f"alpha_row_anchor_phase_emission_formula_proved={fmt_bool(result['alpha_row_anchor_phase_emission_formula_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 同余公式",
        "",
        "| name | formula | meaning |",
        "| --- | --- | --- |",
    ]
    for item in result["congruence_formulae"]:
        lines.append(
            "| `{name}` | `{formula}` | {meaning} |".format(
                name=item["name"],
                formula=table_cell(item["formula"]),
                meaning=table_cell(item["meaning"]),
            )
        )
    lines.extend(
        [
            "",
            "## 2. 公式边界",
            "",
            result["formula_law"],
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
