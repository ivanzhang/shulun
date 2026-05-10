#!/usr/bin/env python3
"""把三奇点标量塌缩排除压成纯二次 Legendre Wronskian 原子。

用法示例：
  python3 experiments/prime_matrix_strict_rks23_scalar_collapse_residue_matrix_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-rks23-scalar-collapse-residue-matrix-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONO = DOCS / "monograph"

OUT_JSON = MONO / "prime-matrix-strict-rks23-scalar-collapse-residue-matrix-router.json"
OUT_MD = MONO / "prime-matrix-strict-rks23-scalar-collapse-residue-matrix-router.md"

PREVIOUS = MONO / "prime-matrix-strict-rks23-pivot-determinant-normal-form-router.json"
ORDER_FREE = MONO / "prime-matrix-strict-rks23-order-free-signature-selector-router.json"
THREE_BRANCH = MONO / "prime-matrix-strict-rks23-three-branch-jacobi-router.json"
FOUR_BRANCH = MONO / "prime-matrix-strict-rks23-four-branch-hypergeometric-router.json"
LEGENDRE = MONO / "prime-matrix-strict-rks23-legendre-subsumption-router.json"
SOURCE_FILES = [PREVIOUS, ORDER_FREE, THREE_BRANCH, FOUR_BRANCH, LEGENDRE]

OLD_TARGET = "RankTwoScalarMonodromyCollapseExclusionLemma"
OLD_SUBATOM = "ThreeSingularityScalarMonodromyExclusionByResidueSignature"
NEW_TARGET = "PureQuadraticLegendreScalarCollapseExclusionLemma"
NEW_SUBATOM = "LegendrePicardFuchsHasseWronskianNonzeroLemma"

RESIDUE_MATRIX_GATE = "ThreeSingularityResidueScalarEquationMatrix"
NON_QUADRATIC_GATE = "NonQuadraticResidueScalarCollapseExcluded"
LOW_SUPPORT_GATE = "LowSupportAndExactThreeFirewallImported"
QUADRATIC_GATE = "PureQuadraticLegendreOnlySurvivingScalarChannel"
SCALAR_GATE = "RankTwoScalarMonodromyCollapseExclusionLemma"
DETERMINANT_GATE = "RankTwoPivotNonzeroDeterminant"
PIVOT_GATE = "RankTwoElementaryStepanovPivotNonzeroDeterminantLemma"
STEPANOV_PIVOT_GATE = "ElementaryStepanovPivotForRankTwoTraceLemma"
SELECTOR_GATE = "OrderFreeKummerSignatureSelectorAndHasseJetRankLemma"
RANK_TARGET = "StepanovKummerAuxiliaryPolynomialNonzeroRankSurjectivity"
STEPANOV_TARGET = "StepanovAuxiliaryPolynomialRankBoundForKummerSums"
KUMMER_TRACE_TARGET = "SelfContainedRankOneKummerSheafRHTraceBound"
BURGESS_POINTWISE = "SelfContainedBurgessPointwiseCharacterSumForLargeDyadicIntervals"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖文件哈希。"""
    return {str(path.relative_to(ROOT)): sha256(path) for path in SOURCE_FILES if path.exists()}


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def scalar_solution_audit(limit: int = 80) -> list[dict[str, Any]]:
    """有限枚举残基方程；只作为符号推导的一致性审计。"""
    records: list[dict[str, Any]] = []
    for order in range(2, limit + 1):
        visible_solutions: list[list[int]] = []
        for a in range(order):
            for b in range(order):
                for c in range(order):
                    inf = (-(a + b + c)) % order
                    visible = all(value % order != 0 for value in [a, b, c, inf])
                    if not visible:
                        continue
                    local_scalar = (
                        (a + c) % order == 0
                        and (b + c) % order == 0
                        and (c + inf) % order == 0
                    )
                    if local_scalar:
                        visible_solutions.append([a, b, c, inf])
        records.append(
            {
                "order": order,
                "visible_scalar_solutions": len(visible_solutions),
                "solutions": visible_solutions[:4],
                "all_solutions_pure_quadratic": all(order % 2 == 0 and solution == [order // 2] * 4 for solution in visible_solutions),
                "audit_only_not_proof": True,
            }
        )
    return records


def build_result() -> dict[str, Any]:
    """构造标量塌缩 residue 矩阵证书。"""
    previous = load_json(PREVIOUS)
    order_free = load_json(ORDER_FREE)
    three_branch = load_json(THREE_BRANCH)
    four_branch = load_json(FOUR_BRANCH)
    legendre = load_json(LEGENDRE)

    active = (
        previous.get("next_direct_attack_target") == OLD_TARGET
        and previous.get("next_subatom") == OLD_SUBATOM
        and previous.get("rank_two_scalar_monodromy_collapse_excluded") is False
        and previous.get("rank_two_pivot_nonzero_determinant_proved") is False
    )
    imported_firewalls = (
        order_free.get("projective_low_visible_support_exact_pgl2_closure_proved") is True
        and three_branch.get("exact_three_visible_branch_trace_bound_closed") is True
        and four_branch.get("four_branch_residue_pair_selector_closed") is True
        and legendre.get("legendre_core_independent_gate_eliminated") is True
    )

    residue_matrix = {
        "projective_residues": "a,b,c,delta with delta=-(a+b+c) modulo d",
        "normal_form": "x^a*(1-x)^b*(1-lambda*x)^c has infinity residue delta",
        "lambda_infinity_edge": "a+c == 0 mod d",
        "lambda_one_edge": "b+c == 0 mod d",
        "lambda_zero_edge": "c+delta == 0 mod d",
        "visibility": "a,b,c,delta are nonzero in the exact four-visible rank-two channel",
    }

    symbolic_derivation = {
        "from_lambda_infinity": "a == -c",
        "from_lambda_one": "b == -c",
        "infinity_residue": "delta=-(a+b+c)==c after substituting a=b=-c",
        "from_lambda_zero": "c+delta==2c==0",
        "visible_consequence": "c is nonzero of order two, so d is even and a=b=c=delta=d/2",
        "closed_nonquadratic_case": "if the residue pattern is not pure quadratic, the all-three scalar collapse equations cannot hold",
    }

    imported_closed_inputs = {
        "low_support": "support size <3 is already a PGL2 one-coordinate degeneration, not a rank-two scalar channel",
        "exact_three": "exactly three visible branches are Jacobi/Gauss and already closed",
        "four_branch_pairing": "four visible residues either have a Jacobi pair or reduce to pure quadratic Legendre",
        "legendre_status": "Legendre is not an independent gate, but its internal Wronskian nonzero proof is still needed here",
    }

    remaining_legendre_atom = {
        "new_atom": NEW_TARGET,
        "new_subatom": NEW_SUBATOM,
        "statement": "for the pure quadratic pattern a=b=c=delta=d/2, the Legendre rank-two local system is not globally scalar and has a nonzero Hasse-Wronskian pivot seed",
        "equivalent_curve_form": "E_lambda: y^2=x(1-x)(1-lambda*x), lambda not in {0,1}",
        "needed_internal_input": "derive the Picard-Fuchs/Hasse derivative relation and prove its two local solutions are not proportional",
        "why_this_is_narrower": "all non-quadratic residue scalar-collapse channels are now excluded by three linear congruences",
        "must_not_use": "external Hasse, Deligne, Katz irreducibility, or a finite point-count audit as a proof",
    }

    rejected_shortcuts = {
        "finite_audit": "the residue enumeration checks the congruence algebra only; it is not the proof of the Legendre Wronskian",
        "legendre_subsumed_means_closed": "previous subsumption removed Legendre as a separate trace gate, but did not prove this internal Wronskian",
        "generic_lambda": "lambda values with j=0 or j=1728 are smooth and still must be covered",
        "external_hasse": "the elliptic Hasse bound would close an external route, not this author-side pivot determinant route",
    }

    residue_matrix_closed = active
    nonquadratic_excluded = active and imported_firewalls
    low_support_imported = imported_firewalls
    pure_quadratic_survives = nonquadratic_excluded
    legendre_scalar_excluded = False
    scalar_excluded = legendre_scalar_excluded
    determinant_closed = scalar_excluded
    pivot_internalized = determinant_closed
    selector_internalized = False
    rank_closed = selector_internalized
    stepanov_closed = rank_closed

    rows = [
        row(
            "PreviousScalarCollapseTargetActive",
            active,
            active,
            "上一证书已把唯一内部剩余压成三奇点 residue signature 标量塌缩排除。",
            OLD_TARGET,
        ),
        row(
            RESIDUE_MATRIX_GATE,
            residue_matrix_closed,
            residue_matrix_closed,
            "三处局部标量塌缩已写成 a+c、b+c、c+delta 三条线性同余。",
            NEW_TARGET,
        ),
        row(
            LOW_SUPPORT_GATE,
            low_support_imported,
            low_support_imported,
            "低支撑、exact-three、四分支配对与 Legendre 并入证书已作为防火墙接入。",
            NEW_TARGET,
        ),
        row(
            NON_QUADRATIC_GATE,
            nonquadratic_excluded,
            nonquadratic_excluded,
            "三条标量同余强制 a=b=c=delta=d/2，因此所有非二次残基塌缩被排除。",
            NEW_TARGET,
        ),
        row(
            QUADRATIC_GATE,
            pure_quadratic_survives,
            pure_quadratic_survives,
            "唯一还能通过三条标量同余的模式是纯二次 Legendre 型。",
            NEW_TARGET,
        ),
        row(
            NEW_TARGET,
            legendre_scalar_excluded,
            legendre_scalar_excluded,
            "仍需内部证明 Legendre 二次特化的 Picard-Fuchs/Hasse-Wronskian 非零。",
            NEW_SUBATOM,
        ),
        row(
            SCALAR_GATE,
            scalar_excluded,
            scalar_excluded,
            "rank-two 标量塌缩排除等待纯二次 Legendre Wronskian 原子。",
            NEW_TARGET,
        ),
        row(
            DETERMINANT_GATE,
            determinant_closed,
            determinant_closed,
            "pivot 行列式非零等待标量塌缩排除。",
            SCALAR_GATE,
        ),
        row(
            PIVOT_GATE,
            pivot_internalized,
            pivot_internalized,
            "初等 rank-two Stepanov pivot 仍等待 determinant atom。",
            DETERMINANT_GATE,
        ),
        row(
            STEPANOV_PIVOT_GATE,
            pivot_internalized,
            pivot_internalized,
            "rank-two trace 的内部 Stepanov pivot 尚未闭合。",
            DETERMINANT_GATE,
        ),
        row(
            SELECTOR_GATE,
            selector_internalized,
            selector_internalized,
            "完整阶无关 selector 仍等待 pivot 非零证明与下游粘合。",
            DETERMINANT_GATE,
        ),
        row(
            RANK_TARGET,
            rank_closed,
            rank_closed,
            "Stepanov-Kummer 非零秩仍未闭合。",
            SELECTOR_GATE,
        ),
        row(
            STEPANOV_TARGET,
            stepanov_closed,
            stepanov_closed,
            "Stepanov 完整内部证明仍未闭合。",
            RANK_TARGET,
        ),
        row(
            KUMMER_TRACE_TARGET,
            False,
            False,
            "秩一 Kummer 迹界仍等待内部 pivot/selector 链条闭合或外部路线被接受。",
            STEPANOV_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "本步只排除非二次标量塌缩，不声明行/列命题作者侧无条件闭合。",
            BURGESS_POINTWISE,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_strict_rks23_scalar_collapse_residue_matrix_router",
        "status": "scalar_collapse_reduced_to_pure_quadratic_legendre_wronskian_nonzero",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "finite_audit_not_used_as_proof": True,
        "previous_scalar_collapse_target_active": active,
        "three_singularity_residue_scalar_equation_matrix_closed": residue_matrix_closed,
        "low_support_and_exact_three_firewall_imported": low_support_imported,
        "nonquadratic_residue_scalar_collapse_excluded": nonquadratic_excluded,
        "pure_quadratic_legendre_only_surviving_scalar_channel": pure_quadratic_survives,
        "pure_quadratic_legendre_scalar_collapse_excluded": legendre_scalar_excluded,
        "rank_two_scalar_monodromy_collapse_excluded": scalar_excluded,
        "rank_two_pivot_nonzero_determinant_proved": determinant_closed,
        "elementary_stepanov_pivot_internalized": pivot_internalized,
        "order_free_signature_selector_internalized": selector_internalized,
        "stepanov_kummer_auxiliary_rank_surjectivity_proved": rank_closed,
        "stepanov_auxiliary_polynomial_rank_bound_proved": stepanov_closed,
        "self_contained_kummer_trace_bound_internalized": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NEW_TARGET,
        "next_subatom": NEW_SUBATOM,
        "residue_matrix": residue_matrix,
        "symbolic_derivation": symbolic_derivation,
        "imported_closed_inputs": imported_closed_inputs,
        "remaining_legendre_atom": remaining_legendre_atom,
        "rejected_shortcuts": rejected_shortcuts,
        "scalar_solution_audit": scalar_solution_audit(),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本轮把三奇点标量塌缩剩余进一步算术化。设四个投影残基为 "
            "`a,b,c,delta`，其中 `delta=-(a+b+c)`。三处 lambda 奇点的标量塌缩对应 "
            "`a+c=0`、`b+c=0`、`c+delta=0` 三条线性同余。前两条给出 `a=b=-c`，"
            "代回 `delta` 得 `delta=c`，第三条给出 `2c=0`。在四可见支路中 `c` 非零，"
            "故唯一可能是 `d` 为偶数且 `a=b=c=delta=d/2`，即纯二次 Legendre 型。"
            "因此所有非二次残基标量塌缩通道被排除；当前唯一内部自足剩余压缩为 "
            "`PureQuadraticLegendreScalarCollapseExclusionLemma`：必须在不调用外部 Hasse/Deligne/Katz 的前提下，"
            "用 Legendre 二次特化的 Picard-Fuchs 或 Hasse-Wronskian 计算证明两维局部解不全局成比例。"
            "未完成该 Wronskian 非零原子前，pivot determinant、Stepanov、Kummer 迹界、Burgess B4 与行/列命题仍不能作者侧无条件闭合。"
        ),
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
        "rows": rows,
    }


def render_key_value_section(lines: list[str], title: str, mapping: dict[str, Any]) -> None:
    """追加键值表。"""
    lines.extend(["", title, "", "| field | value |", "| --- | --- |"])
    for key, value in mapping.items():
        lines.append(f"| `{table_cell(key)}` | {table_cell(value)} |")


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict RKS2/RKS3 标量塌缩 residue 矩阵证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"three_singularity_residue_scalar_equation_matrix_closed={fmt_bool(result['three_singularity_residue_scalar_equation_matrix_closed'])}",
        f"nonquadratic_residue_scalar_collapse_excluded={fmt_bool(result['nonquadratic_residue_scalar_collapse_excluded'])}",
        f"pure_quadratic_legendre_only_surviving_scalar_channel={fmt_bool(result['pure_quadratic_legendre_only_surviving_scalar_channel'])}",
        f"pure_quadratic_legendre_scalar_collapse_excluded={fmt_bool(result['pure_quadratic_legendre_scalar_collapse_excluded'])}",
        f"rank_two_pivot_nonzero_determinant_proved={fmt_bool(result['rank_two_pivot_nonzero_determinant_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
    ]

    render_key_value_section(lines, "## 1. residue 标量矩阵", result["residue_matrix"])
    render_key_value_section(lines, "## 2. 符号推导", result["symbolic_derivation"])
    render_key_value_section(lines, "## 3. 已接入防火墙", result["imported_closed_inputs"])
    render_key_value_section(lines, "## 4. 唯一剩余 Legendre 原子", result["remaining_legendre_atom"])
    render_key_value_section(lines, "## 5. 禁止捷径", result["rejected_shortcuts"])

    lines.extend(
        [
            "",
            "## 6. 有限一致性审计",
            "",
            "| order | visible_scalar_solutions | sample_solutions | all_solutions_pure_quadratic |",
            "| --- | --- | --- | --- |",
        ]
    )
    for item in result["scalar_solution_audit"]:
        if item["visible_scalar_solutions"] == 0 and item["order"] > 12:
            continue
        lines.append(
            "| `{order}` | `{visible_scalar_solutions}` | `{solutions}` | `{all_solutions_pure_quadratic}` |".format(
                order=table_cell(item["order"]),
                visible_scalar_solutions=table_cell(item["visible_scalar_solutions"]),
                solutions=table_cell(item["solutions"]),
                all_solutions_pure_quadratic=fmt_bool(item["all_solutions_pure_quadratic"]),
            )
        )

    lines.extend(
        [
            "",
            "## 7. 判定表",
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
            "## 8. 下一最窄目标",
            "",
            "```text",
            result["next_direct_attack_target"],
            result["next_subatom"],
            "```",
            "",
            "审稿边界：本证书只排除非二次 residue 标量塌缩；",
            "没有证明纯二次 Legendre Wronskian 非零，也没有声明 pivot、Stepanov、Kummer 迹界或行/列命题作者侧无条件闭合。",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """生成 JSON 和 Markdown 证书。"""
    MONO.mkdir(parents=True, exist_ok=True)
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
