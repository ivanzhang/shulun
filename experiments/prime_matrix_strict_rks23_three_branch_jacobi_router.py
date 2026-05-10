#!/usr/bin/env python3
"""闭合精确三可见分支的 Jacobi/Gauss 退化支路。

用法示例：
  python3 experiments/prime_matrix_strict_rks23_three_branch_jacobi_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-rks23-three-branch-jacobi-router.json
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

OUT_JSON = MONO / "prime-matrix-strict-rks23-three-branch-jacobi-router.json"
OUT_MD = MONO / "prime-matrix-strict-rks23-three-branch-jacobi-router.md"

PREVIOUS = MONO / "prime-matrix-strict-rks23-order-free-signature-selector-router.json"
SOURCE_FILES = [PREVIOUS]

OLD_TARGET = "ThreeVisibleBranchOrderFreeJetPivotLemma"
NEW_TARGET = "FourVisibleBranchCrossRatioJetPivotLemma"
JACOBI_GATE = "ExactThreeVisibleBranchJacobiGaussClosure"
SELECTOR_GATE = "OrderFreeKummerSignatureSelectorAndHasseJetRankLemma"
JET_GATE = "BoundedBranchSignatureHasseJetIndependenceLemma"
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


def jacobi_sum(prime: int, order: int, a_exp: int, b_exp: int) -> complex:
    """有限审计用 Jacobi 和。"""
    generator = primitive_root(prime)
    logs = log_table(prime, generator)
    total = 0j
    for x in range(prime):
        total += char_value(prime, logs, order, a_exp, x) * char_value(prime, logs, order, b_exp, 1 - x)
    return total


def jacobi_audit(cases: list[tuple[int, int]]) -> list[dict[str, Any]]:
    """审计 |J(A,B)|=sqrt(p) 的数值形态；证明仍以 Gauss/Jacobi 恒等式为准。"""
    rows: list[dict[str, Any]] = []
    for prime, order in cases:
        checked = 0
        max_error = 0.0
        max_abs = 0.0
        for a_exp in range(1, order):
            for b_exp in range(1, order):
                if (a_exp + b_exp) % order == 0:
                    continue
                value = jacobi_sum(prime, order, a_exp, b_exp)
                checked += 1
                abs_value = abs(value)
                max_abs = max(max_abs, abs_value)
                max_error = max(max_error, abs(abs_value - math.sqrt(prime)))
        rows.append(
            {
                "prime": prime,
                "order": order,
                "checked_nontrivial_pairs": checked,
                "sqrt_prime": round(math.sqrt(prime), 12),
                "max_abs_jacobi": round(max_abs, 12),
                "max_abs_error": f"{max_error:.3e}",
                "identity_shape_verified": max_error < 1e-10,
            }
        )
    return rows


def build_result() -> dict[str, Any]:
    """构造三分支 Jacobi/Gauss 闭合证书。"""
    previous = load_json(PREVIOUS)
    active = (
        previous.get("next_direct_attack_target") == OLD_TARGET
        and previous.get("selector_scope_restricted_to_three_visible_branches") is True
        and previous.get("order_free_signature_selector_internalized") is False
    )

    exact_three_normal_form = {
        "visible_support": "exactly three projective visible places",
        "pgl2_normalization": "send the three visible places to 0, 1, infinity",
        "residue_condition": "f is represented by c*x^a*(1-x)^b*h(x)^d with a,b,a+b nonzero modulo d",
        "invisible_places": "zeros and poles of h only delete O_m(1) affine points and do not affect the conductor constant",
        "order_free_feature": "the reduction depends on support size 3, not on the character order d",
    }

    gauss_jacobi_identity = {
        "characters": "A=chi^a, B=chi^b, with A, B, and AB all nontrivial",
        "jacobi_sum": "J(A,B)=sum_x A(x)B(1-x)",
        "gauss_relation": "J(A,B)=G(A)G(B)/G(AB)",
        "gauss_magnitude": "|G(Psi)|=sqrt(p) for every nontrivial multiplicative character Psi",
        "consequence": "|J(A,B)|=sqrt(p), plus O_m(1) deleted invisible/singular points",
        "self_contained_inputs": "multiplicative/additive character orthogonality and one-line Gauss norm calculation",
    }

    chain_effect = {
        "closed_case": "exactly three projective visible branches no longer needs the Stepanov selector gate",
        "old_frontier_split": "ThreeVisibleBranchOrderFreeJetPivotLemma = exact-three Jacobi branch + four-or-more visible branch pivot branch",
        "new_frontier": NEW_TARGET,
        "new_required_output": "after fixing 0,1,infinity, use at least one remaining cross-ratio branch to build an order-free pivot block and prove Hasse-jet rank loss O_m(TN)",
        "not_claimed": "the four-or-more branch pivot and full selector are not proved here",
    }

    rejected_shortcuts = {
        "jacobi_overextension": "Jacobi/Gauss closes only exact three visible branches; it does not bound arbitrary four-branch rational character sums",
        "generic_cross_ratio": "the four-branch proof must include special cross-ratio collisions and cannot assume generic branch positions",
        "d_ladder": "the y^0,...,y^{d-1} ladder remains forbidden because it makes constants depend on d",
        "audit": "finite Jacobi audits are consistency checks only; the proof object is the Gauss/Jacobi identity",
    }

    exact_three_closed = active
    four_branch_scope = active and exact_three_closed
    selector_internalized = False
    rank_closed = selector_internalized
    stepanov_closed = rank_closed

    rows = [
        row(
            "PreviousThreeVisibleTargetActive",
            active,
            active,
            "上一证书已把 selector 硬点压到至少三处投影可见分支。",
            OLD_TARGET,
        ),
        row(
            "ExactThreeVisiblePGL2NormalFormClosed",
            exact_three_closed,
            exact_three_closed,
            "精确三可见分支可由 PGL2 固定到 0、1、∞，残基化为 Jacobi 型。",
            JACOBI_GATE,
        ),
        row(
            "InternalGaussJacobiIdentityClosed",
            exact_three_closed,
            exact_three_closed,
            "用角色正交和 Gauss 和范数给出 |J(A,B)|=sqrt(p)，常数不依赖 d。",
            JACOBI_GATE,
        ),
        row(
            JACOBI_GATE,
            exact_three_closed,
            exact_three_closed,
            "精确三可见分支 trace 支路闭合，只留下 O_m(1) 奇点删项。",
            "closed",
        ),
        row(
            "SelectorScopeRestrictedToFourVisibleBranches",
            four_branch_scope,
            four_branch_scope,
            "剩余 selector 问题已进一步缩窄到至少四处投影可见分支。",
            NEW_TARGET,
        ),
        row(
            OLD_TARGET,
            False,
            False,
            "原三分支及以上表述已拆分；exact-three 已闭合，但 four-or-more pivot 仍未证明。",
            NEW_TARGET,
        ),
        row(
            NEW_TARGET,
            False,
            False,
            "仍需利用第四分支交比构造阶无关 pivot 块并证明 Hasse-jet 秩下界。",
            "CrossRatioPivotBlockIndependenceLemma",
        ),
        row(
            JET_GATE,
            False,
            False,
            "Hasse-jet 记账接口仍等待四分支 pivot 块实际秩下界。",
            NEW_TARGET,
        ),
        row(
            SELECTOR_GATE,
            False,
            False,
            "完整阶无关 selector 仍等待四分支交比 pivot 引理。",
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
            "秩一 Kummer 迹界仍等待四分支 selector/Stepanov rank gate。",
            STEPANOV_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "本步只关闭 exact-three 退化支路，不声明行/列命题作者侧无条件闭合。",
            BURGESS_POINTWISE,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_strict_rks23_three_branch_jacobi_router",
        "status": "exact_three_visible_branch_closed_by_internal_jacobi_gauss",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "finite_audit_not_used_as_proof": True,
        "previous_three_visible_target_active": active,
        "exact_three_visible_pgl2_normal_form_closed": exact_three_closed,
        "internal_gauss_jacobi_identity_closed": exact_three_closed,
        "exact_three_visible_branch_trace_bound_closed": exact_three_closed,
        "selector_scope_restricted_to_four_visible_branches": four_branch_scope,
        "order_free_signature_selector_internalized": selector_internalized,
        "stepanov_kummer_auxiliary_rank_surjectivity_proved": rank_closed,
        "stepanov_auxiliary_polynomial_rank_bound_proved": stepanov_closed,
        "self_contained_kummer_trace_bound_internalized": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NEW_TARGET,
        "next_subatom": "CrossRatioPivotBlockIndependenceLemma",
        "exact_three_normal_form": exact_three_normal_form,
        "gauss_jacobi_identity": gauss_jacobi_identity,
        "chain_effect": chain_effect,
        "rejected_shortcuts": rejected_shortcuts,
        "jacobi_identity_audit": jacobi_audit([(17, 4), (29, 7), (31, 5), (41, 8)]),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本轮没有闭合完整阶无关 selector，但关闭了当前最窄线中的精确三可见分支支路。"
            "若投影可见支撑正好为三，经 PGL2 可归一到 0、1、∞，函数写成 "
            "`c*x^a*(1-x)^b*h(x)^d`，其中 `a,b,a+b` 均非零模 `d`。于是主和是 Jacobi 和 "
            "`J(chi^a,chi^b)`；用内部 Gauss/Jacobi 恒等式 "
            "`J(A,B)=G(A)G(B)/G(AB)` 与 `|G(Psi)|=sqrt(p)` 得到 `sqrt(p)` 界，"
            "不可见奇点只贡献 `O_m(1)`。该证明只用角色正交，不用整条 Kummer 曲线的 d 阶梯。"
            "因此真正剩余从三可见分支 pivot 缩为四可见分支交比 pivot：必须利用第四分支的交比自由度，"
            "构造常数只依赖 `m` 的 pivot 块并证明 Hasse-jet 秩下界。未完成四分支 pivot 前，"
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
        "# Prime Matrix strict RKS2/RKS3 三分支 Jacobi 前沿证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"previous_three_visible_target_active={fmt_bool(result['previous_three_visible_target_active'])}",
        f"exact_three_visible_pgl2_normal_form_closed={fmt_bool(result['exact_three_visible_pgl2_normal_form_closed'])}",
        f"internal_gauss_jacobi_identity_closed={fmt_bool(result['internal_gauss_jacobi_identity_closed'])}",
        f"exact_three_visible_branch_trace_bound_closed={fmt_bool(result['exact_three_visible_branch_trace_bound_closed'])}",
        f"selector_scope_restricted_to_four_visible_branches={fmt_bool(result['selector_scope_restricted_to_four_visible_branches'])}",
        f"order_free_signature_selector_internalized={fmt_bool(result['order_free_signature_selector_internalized'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
    ]

    render_key_value_section(lines, "## 1. 精确三分支正规形", result["exact_three_normal_form"])
    render_key_value_section(lines, "## 2. 内部 Gauss/Jacobi 恒等式", result["gauss_jacobi_identity"])
    render_key_value_section(lines, "## 3. 链条影响", result["chain_effect"])
    render_key_value_section(lines, "## 4. 禁止捷径", result["rejected_shortcuts"])

    lines.extend(
        [
            "",
            "## 5. Jacobi 恒等式数值审计",
            "",
            "| prime | order | checked_nontrivial_pairs | sqrt_prime | max_abs_jacobi | max_abs_error | identity_shape_verified |",
            "| --- | --- | --- | --- | --- | --- | --- |",
        ]
    )
    for item in result["jacobi_identity_audit"]:
        lines.append(
            "| `{prime}` | `{order}` | `{checked_nontrivial_pairs}` | `{sqrt_prime}` | `{max_abs_jacobi}` | `{max_abs_error}` | `{identity_shape_verified}` |".format(
                **{key: table_cell(value) for key, value in item.items()}
            )
        )

    lines.extend(
        [
            "",
            "## 6. 判定表",
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
            "## 7. 下一最窄目标",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "审稿边界：本证书关闭 exact-three Jacobi 支路，",
            "但没有证明四可见分支交比 pivot 或完整 Stepanov selector；",
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
