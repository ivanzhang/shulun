#!/usr/bin/env python3
"""把四可见分支交比硬点压成二阶超几何迹界原子。

用法示例：
  python3 experiments/prime_matrix_strict_rks23_four_branch_hypergeometric_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-rks23-four-branch-hypergeometric-router.json
"""

from __future__ import annotations

import cmath
import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONO = DOCS / "monograph"

OUT_JSON = MONO / "prime-matrix-strict-rks23-four-branch-hypergeometric-router.json"
OUT_MD = MONO / "prime-matrix-strict-rks23-four-branch-hypergeometric-router.md"

PREVIOUS = MONO / "prime-matrix-strict-rks23-three-branch-jacobi-router.json"
SOURCE_FILES = [PREVIOUS]

OLD_TARGET = "FourVisibleBranchCrossRatioJetPivotLemma"
NEW_TARGET = "RankTwoCrossRatioHypergeometricTraceBoundInternalizationLemma"
PAIR_GATE = "FourBranchResiduePairSelectorOrQuadraticCoreLemma"
JACOBI_GATE = "JacobiKernelExtractionForFourBranchCrossRatio"
JET_GATE = "BoundedBranchSignatureHasseJetIndependenceLemma"
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


def factor(n: int) -> list[int]:
    """返回 n 的不同素因子。"""
    factors: list[int] = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            factors.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors


def primitive_root(prime: int) -> int:
    """寻找素数模下原根。"""
    factors = factor(prime - 1)
    for g in range(2, prime):
        if all(pow(g, (prime - 1) // q, prime) != 1 for q in factors):
            return g
    raise ValueError(f"no primitive root for {prime}")


def log_table(prime: int, generator: int) -> dict[int, int]:
    """生成离散对数表，仅用于有限审计。"""
    table: dict[int, int] = {}
    value = 1
    for k in range(prime - 1):
        table[value] = k
        value = (value * generator) % prime
    return table


def char_value(prime: int, logs: dict[int, int], order: int, exponent: int, x: int) -> complex:
    """计算固定阶乘法角色的幂值；零点按扩展角色取 0。"""
    x %= prime
    if x == 0:
        return 0j
    angle = 2.0 * math.pi * ((exponent * logs[x]) % order) / order
    return cmath.exp(1j * angle)


def jacobi_sum(prime: int, logs: dict[int, int], order: int, a_exp: int, b_exp: int) -> complex:
    """有限审计用 Jacobi 和。"""
    return sum(
        char_value(prime, logs, order, a_exp, x)
        * char_value(prime, logs, order, b_exp, 1 - x)
        for x in range(prime)
    )


def four_branch_sum(
    prime: int,
    logs: dict[int, int],
    order: int,
    a_exp: int,
    b_exp: int,
    c_exp: int,
    lamb: int,
) -> complex:
    """审计四分支交比和 S_lambda(A,B,C)。"""
    return sum(
        char_value(prime, logs, order, a_exp, x)
        * char_value(prime, logs, order, b_exp, 1 - x)
        * char_value(prime, logs, order, c_exp, 1 - lamb * x)
        for x in range(prime)
    )


def residue_pair_type(order: int, residues: list[int]) -> str:
    """判定四分支残基是否有非平凡 Jacobi 配对。"""
    normalized = [r % order for r in residues]
    for i, first in enumerate(normalized):
        for second in normalized[i + 1 :]:
            if (first + second) % order != 0:
                return "has_nontrivial_pair_product"
    return "pure_quadratic_all_pair_products_trivial"


def hypergeometric_audit(cases: list[dict[str, int]]) -> list[dict[str, Any]]:
    """有限审计四分支和的归一化大小；不作为证明使用。"""
    rows: list[dict[str, Any]] = []
    for case in cases:
        prime = case["prime"]
        order = case["order"]
        a_exp = case["a"]
        b_exp = case["b"]
        c_exp = case["c"]
        lamb = case["lambda"]
        generator = primitive_root(prime)
        logs = log_table(prime, generator)
        infinity_exp = (-(a_exp + b_exp + c_exp)) % order
        residues = [a_exp % order, b_exp % order, c_exp % order, infinity_exp]
        pair_type = residue_pair_type(order, residues)
        total = four_branch_sum(prime, logs, order, a_exp, b_exp, c_exp, lamb)
        jacobi = jacobi_sum(prime, logs, order, a_exp, b_exp)
        jacobi_abs = abs(jacobi)
        # 纯二次例外不走 Jacobi 核抽取，归一化列只给非平凡配对支路使用。
        normalized = (
            abs(total) / jacobi_abs
            if pair_type == "has_nontrivial_pair_product" and (a_exp + b_exp) % order != 0 and jacobi_abs > 1e-12
            else None
        )
        rows.append(
            {
                "prime": prime,
                "order": order,
                "lambda": lamb,
                "residues_a_b_c_inf": residues,
                "pair_type": pair_type,
                "abs_sum_over_sqrt_p": round(abs(total) / math.sqrt(prime), 12),
                "abs_jacobi_ab": round(jacobi_abs, 12),
                "abs_sum_over_abs_jacobi_ab": None if normalized is None else round(normalized, 12),
            }
        )
    return rows


def build_result() -> dict[str, Any]:
    """构造四分支超几何前沿证书。"""
    previous = load_json(PREVIOUS)
    active = (
        previous.get("next_direct_attack_target") == OLD_TARGET
        and previous.get("selector_scope_restricted_to_four_visible_branches") is True
        and previous.get("order_free_signature_selector_internalized") is False
    )

    four_branch_normal_form = {
        "support": "exactly four projective visible branches after previous low-support and exact-three closures",
        "pgl2_normalization": "send three visible branches to 0, 1, infinity; the fourth is the cross-ratio parameter lambda not in {0,1}",
        "normal_form": "f(x)=c*x^a*(1-x)^b*(1-lambda*x)^c*h(x)^d",
        "visibility_conditions": "a,b,c,a+b+c are all nonzero modulo d, with infinity residue -(a+b+c)",
        "free_parameter": "all branch-position dependence is compressed into one cross-ratio lambda",
    }

    residue_pair_selector = {
        "statement": "among four visible residues, either some pair has nontrivial product, or all pair products are trivial",
        "nontrivial_pair_case": "choose that pair as a Jacobi sqrt(p) kernel after a PGL2 relabeling",
        "exception": "if every pair product is trivial, then all four residues are the same order-two residue; this is the pure quadratic Legendre core",
        "why_order_free": "the dichotomy uses only four residues and does not depend on d, P, or branch positions",
        "closed_here": "the finite residue dichotomy is closed; the trace bound for the remaining rank-two core is not",
    }

    jacobi_kernel_extraction = {
        "sum": "S_lambda(A,B,C)=sum_x A(x)B(1-x)C(1-lambda*x)",
        "kernel": "when AB is nontrivial, J(A,B)=sum_x A(x)B(1-x) has size sqrt(p)",
        "normalized_trace": "H_lambda(A,B;C)=S_lambda(A,B,C)/J(A,B)",
        "remaining_bound": "prove |H_lambda(A,B;C)|<=C_m uniformly, including special cross-ratio collisions",
        "quadratic_core": "if every pair product is trivial, the remaining sum is the Legendre elliptic trace sum chi(x(1-x)(1-lambda*x))",
    }

    remaining_rank_two_atom = {
        "old_atom": OLD_TARGET,
        "new_atom": NEW_TARGET,
        "rank_two_meaning": "the four-branch cross-ratio problem is now a normalized rank-two trace problem, not a free d-ladder rank problem",
        "required_trace_output": "uniform O_m(sqrt(p)) for S_lambda, or equivalently O_m(1) for normalized H_lambda",
        "required_pivot_output": "translate the same rank-two bound into an order-free pivot block with Hasse-jet loss O_m(TN)",
        "why_not_closed": "the corpus still lacks a self-contained proof of the rank-two cross-ratio trace bound in all special and generic lambda cases",
    }

    rejected_shortcuts = {
        "generic_lambda": "lambda cannot be assumed generic; lambda values with extra automorphisms must be included",
        "jacobi_only": "Jacobi closes the extracted kernel, not the normalized cross-ratio trace H_lambda",
        "elliptic_known_bound": "the pure quadratic Legendre case may be recognized as elliptic, but an internal trace proof is still required",
        "d_ladder": "using y^0,...,y^{d-1} remains forbidden because it reintroduces d-dependent constants",
    }

    normal_form_closed = active
    pair_selector_closed = active
    jacobi_extraction_closed = active
    selector_internalized = False
    rank_closed = selector_internalized
    stepanov_closed = rank_closed

    rows = [
        row(
            "PreviousFourVisibleTargetActive",
            active,
            active,
            "上一证书已把唯一剩余压到四可见分支交比 pivot。",
            OLD_TARGET,
        ),
        row(
            "FourBranchPGL2CrossRatioNormalFormClosed",
            normal_form_closed,
            normal_form_closed,
            "四个投影可见分支已归一为 0、1、∞ 与一个交比参数 lambda。",
            "closed",
        ),
        row(
            PAIR_GATE,
            pair_selector_closed,
            pair_selector_closed,
            "四个残基要么有非平凡 Jacobi 配对，要么落入纯二次 Legendre 核。",
            NEW_TARGET,
        ),
        row(
            JACOBI_GATE,
            jacobi_extraction_closed,
            jacobi_extraction_closed,
            "非平凡配对支路可抽出 sqrt(p) Jacobi 核，剩余为归一化二阶交比迹。",
            NEW_TARGET,
        ),
        row(
            "PureQuadraticLegendreCoreIsolated",
            pair_selector_closed,
            pair_selector_closed,
            "所有配对平凡的例外被唯一定位为四个二次残基的 Legendre 交比核。",
            NEW_TARGET,
        ),
        row(
            OLD_TARGET,
            False,
            False,
            "四分支 pivot 已正规化并抽核，但 rank-two 交比迹界仍未内部证明。",
            NEW_TARGET,
        ),
        row(
            NEW_TARGET,
            False,
            False,
            "仍需自足证明归一化二阶超几何/Legendre 交比迹的统一有界性。",
            "RankTwoTraceBoundOrStepanovPivotBlock",
        ),
        row(
            JET_GATE,
            False,
            False,
            "Hasse-jet 秩下界仍等待 rank-two 交比 pivot 块。",
            NEW_TARGET,
        ),
        row(
            SELECTOR_GATE,
            False,
            False,
            "完整阶无关 selector 仍等待 rank-two 交比迹界或等价 pivot 证明。",
            NEW_TARGET,
        ),
        row(
            RANK_TARGET,
            rank_closed,
            rank_closed,
            "Stepanov-Kummer 非零秩仍等待完整 selector。",
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
            "秩一 Kummer 迹界仍等待 rank-two 交比输入内部化。",
            STEPANOV_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "本步只关闭四分支正规形与 Jacobi 抽核，不声明行/列命题作者侧无条件闭合。",
            BURGESS_POINTWISE,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_strict_rks23_four_branch_hypergeometric_router",
        "status": "four_branch_crossratio_reduced_to_rank_two_hypergeometric_trace_atom",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "finite_audit_not_used_as_proof": True,
        "previous_four_visible_target_active": active,
        "four_branch_pgl2_crossratio_normal_form_closed": normal_form_closed,
        "four_branch_residue_pair_selector_closed": pair_selector_closed,
        "jacobi_kernel_extraction_closed": jacobi_extraction_closed,
        "pure_quadratic_legendre_core_isolated": pair_selector_closed,
        "rank_two_crossratio_trace_bound_internalized": False,
        "order_free_signature_selector_internalized": selector_internalized,
        "stepanov_kummer_auxiliary_rank_surjectivity_proved": rank_closed,
        "stepanov_auxiliary_polynomial_rank_bound_proved": stepanov_closed,
        "self_contained_kummer_trace_bound_internalized": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NEW_TARGET,
        "next_subatom": "RankTwoTraceBoundOrStepanovPivotBlock",
        "four_branch_normal_form": four_branch_normal_form,
        "residue_pair_selector": residue_pair_selector,
        "jacobi_kernel_extraction": jacobi_kernel_extraction,
        "remaining_rank_two_atom": remaining_rank_two_atom,
        "rejected_shortcuts": rejected_shortcuts,
        "hypergeometric_audit": hypergeometric_audit(
            [
                {"prime": 17, "order": 4, "a": 1, "b": 1, "c": 1, "lambda": 3},
                {"prime": 29, "order": 7, "a": 1, "b": 2, "c": 3, "lambda": 5},
                {"prime": 31, "order": 5, "a": 1, "b": 1, "c": 2, "lambda": 3},
                {"prime": 41, "order": 8, "a": 1, "b": 3, "c": 2, "lambda": 6},
                {"prime": 43, "order": 2, "a": 1, "b": 1, "c": 1, "lambda": 7},
            ]
        ),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本轮没有证明完整四分支 pivot，但把四可见分支交比硬点进一步压成 rank-two 迹界原子。"
            "四个投影可见分支经 PGL2 可固定为 `0,1,∞,lambda`，函数化为 "
            "`c*x^a*(1-x)^b*(1-lambda*x)^c*h(x)^d`，所有位置自由度只剩一个交比 `lambda`。"
            "残基层面闭合了一个有限二分：若存在一对残基乘积非平凡，则可抽出 Jacobi 核 "
            "`J(A,B)`，把四分支和写成 `J(A,B)*H_lambda(A,B;C)`；若所有配对都平凡，"
            "则唯一例外是四个同一二次残基的 Legendre 交比核。于是当前真正剩余不再是自由的 "
            "d 阶梯 selector，而是 `RankTwoCrossRatioHypergeometricTraceBoundInternalizationLemma`："
            "自足证明归一化二阶交比迹 `H_lambda` 以及纯二次 Legendre 核在所有特殊和一般 `lambda` 下统一有界，"
            "或给出等价的 order-free Stepanov pivot 块。未完成该 rank-two 输入前，"
            "Stepanov、Kummer 迹界、Burgess B4 与行/列命题仍不能作者侧无条件闭合。"
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
        "# Prime Matrix strict RKS2/RKS3 四分支超几何前沿证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"previous_four_visible_target_active={fmt_bool(result['previous_four_visible_target_active'])}",
        f"four_branch_pgl2_crossratio_normal_form_closed={fmt_bool(result['four_branch_pgl2_crossratio_normal_form_closed'])}",
        f"four_branch_residue_pair_selector_closed={fmt_bool(result['four_branch_residue_pair_selector_closed'])}",
        f"jacobi_kernel_extraction_closed={fmt_bool(result['jacobi_kernel_extraction_closed'])}",
        f"rank_two_crossratio_trace_bound_internalized={fmt_bool(result['rank_two_crossratio_trace_bound_internalized'])}",
        f"order_free_signature_selector_internalized={fmt_bool(result['order_free_signature_selector_internalized'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
    ]

    render_key_value_section(lines, "## 1. 四分支交比正规形", result["four_branch_normal_form"])
    render_key_value_section(lines, "## 2. 残基配对二分", result["residue_pair_selector"])
    render_key_value_section(lines, "## 3. Jacobi 核抽取", result["jacobi_kernel_extraction"])
    render_key_value_section(lines, "## 4. 当前 rank-two 原子", result["remaining_rank_two_atom"])
    render_key_value_section(lines, "## 5. 禁止捷径", result["rejected_shortcuts"])

    lines.extend(
        [
            "",
            "## 6. 交比迹数值审计",
            "",
            "| prime | order | lambda | residues_a_b_c_inf | pair_type | abs_sum_over_sqrt_p | abs_jacobi_ab | abs_sum_over_abs_jacobi_ab |",
            "| --- | --- | --- | --- | --- | --- | --- | --- |",
        ]
    )
    for item in result["hypergeometric_audit"]:
        lines.append(
            "| `{prime}` | `{order}` | `{lambda}` | `{residues_a_b_c_inf}` | {pair_type} | `{abs_sum_over_sqrt_p}` | `{abs_jacobi_ab}` | `{abs_sum_over_abs_jacobi_ab}` |".format(
                **{key: table_cell(value) for key, value in item.items()}
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
            "```",
            "",
            "审稿边界：本证书关闭四分支 PGL2 正规形、残基配对二分和 Jacobi 核抽取，",
            "但没有证明 rank-two 交比迹界或完整 Stepanov selector；",
            "因此不声明 Kummer 迹界、Burgess B4 或行/列命题作者侧无条件闭合。",
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
