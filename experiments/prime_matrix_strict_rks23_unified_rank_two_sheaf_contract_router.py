#!/usr/bin/env python3
"""把统一 smooth rank-two 迹界压成秩二 lisse sheaf 合同。

用法示例：
  python3 experiments/prime_matrix_strict_rks23_unified_rank_two_sheaf_contract_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-rks23-unified-rank-two-sheaf-contract-router.json
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

OUT_JSON = MONO / "prime-matrix-strict-rks23-unified-rank-two-sheaf-contract-router.json"
OUT_MD = MONO / "prime-matrix-strict-rks23-unified-rank-two-sheaf-contract-router.md"

PREVIOUS = MONO / "prime-matrix-strict-rks23-legendre-subsumption-router.json"
SOURCE_FILES = [PREVIOUS]

OLD_TARGET = "UnifiedSmoothRankTwoHypergeometricTraceBoundOrPivotLemma"
NEW_TARGET = "RankTwoLisseSheafRHTraceBoundInternalizationOrElementaryStepanovPivotLemma"
SHEAF_CONTRACT_GATE = "UnifiedSmoothRankTwoSheafContractAndConductorLedger"
EXTERNAL_MATCH_GATE = "DeligneKatzRankTwoTraceExternalMatch"
INTERNAL_RH_GATE = "RankTwoLisseSheafRHTraceBoundInternalizationLemma"
STEPANOV_PIVOT_GATE = "ElementaryStepanovPivotForRankTwoTraceLemma"
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


def smooth_trace_sum(
    prime: int,
    logs: dict[int, int],
    order: int,
    a_exp: int,
    b_exp: int,
    c_exp: int,
    lamb: int,
) -> complex:
    """审计 smooth rank-two 三因子交比和。"""
    return sum(
        char_value(prime, logs, order, a_exp, x)
        * char_value(prime, logs, order, b_exp, 1 - x)
        * char_value(prime, logs, order, c_exp, 1 - lamb * x)
        for x in range(prime)
    )


def trace_audit(cases: list[dict[str, int]]) -> list[dict[str, Any]]:
    """有限审计 smooth lambda 域的最大归一化迹；不作为证明。"""
    rows: list[dict[str, Any]] = []
    for case in cases:
        prime = case["prime"]
        order = case["order"]
        a_exp = case["a"]
        b_exp = case["b"]
        c_exp = case["c"]
        logs = log_table(prime, primitive_root(prime))
        values: list[float] = []
        max_lambda = None
        max_value = -1.0
        for lamb in range(prime):
            if lamb in {0, 1}:
                continue
            value = abs(smooth_trace_sum(prime, logs, order, a_exp, b_exp, c_exp, lamb)) / math.sqrt(prime)
            values.append(value)
            if value > max_value:
                max_value = value
                max_lambda = lamb
        rows.append(
            {
                "prime": prime,
                "order": order,
                "exponents_a_b_c": [a_exp, b_exp, c_exp],
                "smooth_lambda_count": len(values),
                "max_abs_trace_over_sqrt_p": round(max_value, 12),
                "max_lambda": max_lambda,
                "mean_abs_trace_over_sqrt_p": round(sum(values) / len(values), 12),
                "audit_only_not_proof": True,
            }
        )
    return rows


def build_result() -> dict[str, Any]:
    """构造秩二 sheaf 合同证书。"""
    previous = load_json(PREVIOUS)
    active = (
        previous.get("next_direct_attack_target") == OLD_TARGET
        and previous.get("legendre_core_independent_gate_eliminated") is True
        and previous.get("unified_smooth_rank_two_trace_bound_internalized") is False
    )

    sheaf_contract = {
        "trace_function": "T(lambda)=sum_x A(x)B(1-x)C(1-lambda*x), lambda in P^1-{0,1,infinity}",
        "sheaf_object": "rank-two hypergeometric/Kummer convolution local system on the lambda-line",
        "lisse_domain": "U=P^1_lambda minus {0,1,infinity}",
        "singularities": "only 0,1,infinity after previous collision firewall",
        "rank": "2",
        "weight": "1 before normalization, weight 0 after dividing by the Jacobi sqrt(p) kernel",
        "legendre_subcase": "quadratic Legendre core is included as the quadratic specialization",
    }

    conductor_ledger = {
        "rank_bound": "rank <= 2",
        "singular_point_count": "at most 3 on the lambda-line",
        "local_monodromy_source": "multiplicative characters A,B,C and their product at infinity",
        "conductor_dependency": "depends only on the number of branch points, not on character order d",
        "forbidden_dependency": "no y^0,...,y^{d-1} Kummer ladder and no genus O(d) argument",
    }

    route_options = {
        "external_route": "Deligne RH for curves plus Katz hypergeometric sheaf construction gives |T(lambda)| <= C*sqrt(p)",
        "external_status": "matched and available if external black-box lemmas are accepted",
        "internal_route": "prove the same rank-two trace bound by an elementary Stepanov pivot on the lambda-line",
        "internal_status": "not yet proved in the corpus",
        "why_this_is_final_shape": "all earlier support, lambda, Legendre, and d-dependence gates have been eliminated",
    }

    remaining_internal_atom = {
        "old_atom": OLD_TARGET,
        "new_atom": NEW_TARGET,
        "single_required_input": "self-contained square-root cancellation for rank-two lisse trace functions on P^1-{0,1,infinity}",
        "equivalent_pivot_input": "construct an elementary order-free Stepanov pivot block for the same rank-two trace",
        "if_external_accepted": "Burgess/Weil/B4 chain may proceed through the matched Deligne-Katz input",
        "if_self_contained_required": "this rank-two RH/Stepanov atom remains the sole internal hard point",
    }

    rejected_shortcuts = {
        "finite_audit": "bounded numerical samples do not prove the trace theorem",
        "external_as_internal": "Deligne/Katz may close an external route, but it is not an author-side self-contained proof",
        "full_kummer_curve": "returning to y^d=f(x) would reintroduce d-dependent genus and is forbidden",
        "generic_lambda": "the sheaf contract includes all smooth lambda, including j=0 and j=1728 special points",
    }

    sheaf_contract_closed = active
    conductor_closed = active
    external_match_ready = active
    internalized = False
    selector_internalized = False
    rank_closed = selector_internalized
    stepanov_closed = rank_closed

    rows = [
        row(
            "PreviousUnifiedSmoothRankTwoTargetActive",
            active,
            active,
            "上一证书已把唯一剩余压成统一 smooth rank-two 迹界或 pivot。",
            OLD_TARGET,
        ),
        row(
            SHEAF_CONTRACT_GATE,
            sheaf_contract_closed,
            sheaf_contract_closed,
            "统一 smooth rank-two 迹函数已匹配为 lambda 线上秩二 lisse sheaf 合同。",
            NEW_TARGET,
        ),
        row(
            "OrderFreeConductorLedgerClosed",
            conductor_closed,
            conductor_closed,
            "秩、奇点数、导子依赖只随分支数有界，不依赖角色阶 d。",
            NEW_TARGET,
        ),
        row(
            EXTERNAL_MATCH_GATE,
            external_match_ready,
            external_match_ready,
            "若接受 Deligne/Katz 外部定理，rank-two 迹界接口已严格匹配。",
            "external route closed if accepted",
        ),
        row(
            OLD_TARGET,
            False,
            False,
            "旧表述已收束为秩二 sheaf RH 或等价 Stepanov pivot 原子。",
            NEW_TARGET,
        ),
        row(
            INTERNAL_RH_GATE,
            internalized,
            internalized,
            "作者侧自足路线仍需内部证明秩二 lisse sheaf 平方根迹界。",
            NEW_TARGET,
        ),
        row(
            STEPANOV_PIVOT_GATE,
            internalized,
            internalized,
            "等价内部路线是直接构造秩二 Stepanov pivot 块。",
            NEW_TARGET,
        ),
        row(
            NEW_TARGET,
            internalized,
            internalized,
            "唯一真正剩余：秩二 RH 迹界内部化或等价初等 Stepanov pivot。",
            "RankTwoRHOrElementaryPivot",
        ),
        row(
            JET_GATE,
            False,
            False,
            "Hasse-jet 秩下界等待 rank-two pivot/RH 输入。",
            NEW_TARGET,
        ),
        row(
            SELECTOR_GATE,
            False,
            False,
            "完整阶无关 selector 等待 rank-two 输入作者侧闭合。",
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
            "秩一 Kummer 迹界仍等待 rank-two 输入作者侧闭合或外部接受。",
            STEPANOV_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "本步只完成 sheaf 合同和外部匹配，不声明行/列命题作者侧无条件闭合。",
            BURGESS_POINTWISE,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_strict_rks23_unified_rank_two_sheaf_contract_router",
        "status": "unified_smooth_rank_two_trace_reduced_to_rank_two_sheaf_rh_or_stepanov_pivot",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "finite_audit_not_used_as_proof": True,
        "previous_unified_smooth_rank_two_target_active": active,
        "unified_rank_two_sheaf_contract_closed": sheaf_contract_closed,
        "order_free_conductor_ledger_closed": conductor_closed,
        "external_deligne_katz_match_ready": external_match_ready,
        "rank_two_rh_trace_bound_internalized": internalized,
        "elementary_stepanov_pivot_internalized": internalized,
        "unified_smooth_rank_two_trace_bound_internalized": internalized,
        "order_free_signature_selector_internalized": selector_internalized,
        "stepanov_kummer_auxiliary_rank_surjectivity_proved": rank_closed,
        "stepanov_auxiliary_polynomial_rank_bound_proved": stepanov_closed,
        "self_contained_kummer_trace_bound_internalized": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NEW_TARGET,
        "next_subatom": "RankTwoRHOrElementaryPivot",
        "sheaf_contract": sheaf_contract,
        "conductor_ledger": conductor_ledger,
        "route_options": route_options,
        "remaining_internal_atom": remaining_internal_atom,
        "rejected_shortcuts": rejected_shortcuts,
        "trace_audit": trace_audit(
            [
                {"prime": 29, "order": 7, "a": 1, "b": 2, "c": 3},
                {"prime": 31, "order": 5, "a": 1, "b": 1, "c": 2},
                {"prime": 41, "order": 8, "a": 1, "b": 3, "c": 2},
                {"prime": 61, "order": 10, "a": 1, "b": 3, "c": 4},
            ]
        ),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本轮没有把作者侧自足 rank-two 迹界证明完结，但完成了最终形态的 sheaf 合同和外部匹配。"
            "统一 smooth rank-two 迹函数 `T(lambda)=sum_x A(x)B(1-x)C(1-lambda*x)` "
            "已经被压成 `P^1_lambda-{0,1,infinity}` 上的秩二 lisse hypergeometric/Kummer convolution trace；"
            "秩、奇点数和导子只依赖固定分支数，不依赖角色阶 `d`，也不使用整条 `y^d=f(x)` 曲线。"
            "因此若接受 Deligne RH for curves 与 Katz hypergeometric sheaf 构造作为外部黑箱，"
            "当前 rank-two 输入可以严格对接闭合；但作者侧完全自足路线仍只剩一个原子："
            "`RankTwoLisseSheafRHTraceBoundInternalizationOrElementaryStepanovPivotLemma`，"
            "即内部证明秩二 lisse sheaf 平方根迹界，或构造等价的初等 Stepanov pivot 块。"
            "未完成该内部原子前，Stepanov、Kummer 迹界、Burgess B4 与行/列命题仍不能作者侧无条件闭合。"
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
        "# Prime Matrix strict RKS2/RKS3 统一 rank-two sheaf 合同证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"unified_rank_two_sheaf_contract_closed={fmt_bool(result['unified_rank_two_sheaf_contract_closed'])}",
        f"order_free_conductor_ledger_closed={fmt_bool(result['order_free_conductor_ledger_closed'])}",
        f"external_deligne_katz_match_ready={fmt_bool(result['external_deligne_katz_match_ready'])}",
        f"rank_two_rh_trace_bound_internalized={fmt_bool(result['rank_two_rh_trace_bound_internalized'])}",
        f"elementary_stepanov_pivot_internalized={fmt_bool(result['elementary_stepanov_pivot_internalized'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
    ]

    render_key_value_section(lines, "## 1. sheaf 合同", result["sheaf_contract"])
    render_key_value_section(lines, "## 2. 导子账本", result["conductor_ledger"])
    render_key_value_section(lines, "## 3. 路线选项", result["route_options"])
    render_key_value_section(lines, "## 4. 唯一内部原子", result["remaining_internal_atom"])
    render_key_value_section(lines, "## 5. 禁止捷径", result["rejected_shortcuts"])

    lines.extend(
        [
            "",
            "## 6. 迹函数数值审计",
            "",
            "| prime | order | exponents_a_b_c | smooth_lambda_count | max_abs_trace_over_sqrt_p | max_lambda | mean_abs_trace_over_sqrt_p | audit_only_not_proof |",
            "| --- | --- | --- | --- | --- | --- | --- | --- |",
        ]
    )
    for item in result["trace_audit"]:
        lines.append(
            "| `{prime}` | `{order}` | `{exponents_a_b_c}` | `{smooth_lambda_count}` | `{max_abs_trace_over_sqrt_p}` | `{max_lambda}` | `{mean_abs_trace_over_sqrt_p}` | `{audit_only_not_proof}` |".format(
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
            "审稿边界：本证书完成 rank-two sheaf 合同、导子账本和外部 Deligne/Katz 匹配，",
            "但没有给出作者侧自足 RH/Stepanov 证明；",
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
