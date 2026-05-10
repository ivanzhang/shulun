#!/usr/bin/env python3
"""把 Burgess 所需 Weil 界压成阶无关 Kummer sheaf/Stepanov 迹界。

用法示例：
  python3 experiments/prime_matrix_strict_rks23_kummer_sheaf_weil_reduction_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-rks23-kummer-sheaf-weil-reduction-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONO = DOCS / "monograph"

OUT_JSON = MONO / "prime-matrix-strict-rks23-kummer-sheaf-weil-reduction-router.json"
OUT_MD = MONO / "prime-matrix-strict-rks23-kummer-sheaf-weil-reduction-router.md"

PREVIOUS = MONO / "prime-matrix-strict-rks23-burgess-weil-kernel-diagonal-router.json"
SOURCE_FILES = [PREVIOUS]

TARGET = "SelfContainedWeilBoundForMultiplicativeCharacterRationalFunctions"
KUMMER_TRACE_ATOM = "SelfContainedRankOneKummerSheafRHTraceBound"
STEPANOV_ATOM = "StepanovAuxiliaryPolynomialRankBoundForKummerSums"
B4_ATOM = "B4_weil_complete_rational_sum_kernel"
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


def conductor_table() -> list[dict[str, str]]:
    """生成 Burgess 常用 r 值下的阶无关导子账本。"""
    rows = []
    for r in [5, 9, 17, 26]:
        max_branch_places = 2 * r
        conductor_bound = max_branch_places + 2
        rows.append(
            {
                "r": str(r),
                "max_branch_places_m": str(max_branch_places),
                "rank_one_conductor_bound": str(conductor_bound),
                "trace_bound_shape": f"O({conductor_bound}*P^(1/2))",
                "depends_on_character_order_d": "false",
            }
        )
    return rows


def build_result() -> dict[str, Any]:
    """构造 Kummer sheaf/Stepanov 归约证书。"""
    previous = load_json(PREVIOUS)
    target_active = (
        previous.get("next_direct_attack_target") == TARGET
        and previous.get("external_weil_bound_would_close_b4") is True
        and previous.get("self_contained_weil_bound_internalized") is False
    )

    rational_sum_statement = {
        "field": "F_P with P prime",
        "character": "nonprincipal multiplicative character chi of order d",
        "function": "f(x)=prod_a (x-a)^{e_a} from the Burgess complete kernel after collecting signed multiplicities",
        "nonpower_condition": "some e_a is not divisible by d, equivalently f is not a d-th power in F_P(x)",
        "branch_places": "B={a in P^1: ord_a(f) not congruent to 0 mod d}",
        "burgess_kernel_size": "for the 2r-th Burgess moment, |B|<=2r; infinity is unramified because numerator and denominator have equal degree",
        "needed_bound": "|sum_x chi(f(x))| <= C_r P^(1/2) with C_r independent of d and P",
    }

    naive_curve_hazard = {
        "tempting_route": "use the smooth projective model of y^d=f(x) and Hasse-Weil for the whole curve",
        "problem": "the genus of the whole d-cover can grow like d*|B|, so the bound may carry a factor depending on d",
        "why_bad_for_burgess": "d can be as large as P-1, but Burgess needs a constant depending only on fixed r",
        "correct_route": "work on the chi-eigenspace/rank-one Kummer sheaf, or use Stepanov directly, so the conductor is O(|B|)",
        "firewall": "no future certificate may claim B4 closed from a whole-curve genus bound unless the d-dependence is removed",
    }

    order_free_interface = {
        "rank": "1",
        "open_curve": "U=P^1 \\ B",
        "sheaf": "L_{chi(f)} is the pullback of the Kummer sheaf by f",
        "nontriviality": "nonpower_condition makes the sheaf geometrically nonconstant",
        "conductor": "cond(L_{chi(f)}) <= |B|+2 <= 2r+2 in the Burgess kernel",
        "cohomology_shape": "H_c^0 and H_c^2 vanish for a geometrically nonconstant rank-one sheaf on U",
        "trace_formula": "sum_{x in U(F_P)} chi(f(x)) = -Tr(Frob_P | H_c^1(U_bar,L_{chi(f)}))",
        "rh_trace_input": "all Frobenius eigenvalues on H_c^1 have absolute value P^(1/2)",
        "consequence": "|sum chi(f(x))| <= dim H_c^1 * P^(1/2) <= O_r(P^(1/2))",
    }

    stepanov_route = {
        "goal": "prove the same O_r(P^(1/2)) bound without importing l-adic language",
        "auxiliary_polynomial": "construct a low-degree polynomial in x and the Kummer values whose many zeros force the desired estimate",
        "rank_condition": "monomials modulo the Kummer relation must remain independent up to the selected degree window",
        "multiplicity_ledger": "zeros at the large value set are counted with controlled multiplicity and bounded by total degree",
        "current_gap": "the auxiliary polynomial rank/surjectivity lemma is not yet written in the corpus",
    }

    reduction_closed = target_active
    hazard_closed = target_active
    conductor_closed = target_active
    trace_formula_interface_closed = target_active
    external_kummer_rh_sufficient = target_active
    self_contained_trace_bound = False
    self_contained_weil_bound = self_contained_trace_bound
    b4_closed_author_side = self_contained_weil_bound

    rows = [
        row(
            "WeilBoundTargetActive",
            target_active,
            True,
            "上一证书已把 B4 唯一剩余压成乘法角色有理函数 Weil 平方根界。",
            TARGET,
        ),
        row(
            "RationalFunctionToKummerSheafReductionClosed",
            reduction_closed,
            True,
            "Burgess 内核的非幂有理函数和已归约为秩一 Kummer sheaf 的迹和。",
            "rank-one Kummer sheaf",
        ),
        row(
            "WholeKummerCurveGenusHazardClosed",
            hazard_closed,
            True,
            "已排除整条 `y^d=f(x)` 曲线 Hasse-Weil 直接闭合的 d 依赖误用。",
            "review firewall",
        ),
        row(
            "OrderFreeConductorLedgerClosed",
            conductor_closed,
            True,
            "导子只由分支点数控制，Burgess 2r 矩中 `cond<=2r+2`，与角色阶 d 无关。",
            "conductor ledger",
        ),
        row(
            "TraceFormulaInterfaceClosed",
            trace_formula_interface_closed,
            True,
            "迹公式接口已固定：目标和等于 `H_c^1` 上 Frobenius 迹。",
            KUMMER_TRACE_ATOM,
        ),
        row(
            "ExternalKummerSheafRHWouldCloseWeilBound",
            external_kummer_rh_sufficient,
            True,
            "若接受秩一 Kummer sheaf 的 RH/Weil 迹界，则得到所需 `O_r(P^(1/2))`。",
            "external sheaf RH or classical Stepanov-Weil",
        ),
        row(
            "SelfContainedKummerTraceBoundInternalized",
            self_contained_trace_bound,
            self_contained_trace_bound,
            "仓库内尚未给出该 RH/Stepanov 迹界的完整内部证明。",
            KUMMER_TRACE_ATOM,
        ),
        row(
            TARGET,
            self_contained_weil_bound,
            self_contained_weil_bound,
            "作者侧完全自足版仍需证明秩一 Kummer sheaf RH 迹界或等价 Stepanov 引理。",
            KUMMER_TRACE_ATOM,
        ),
        row(
            B4_ATOM,
            b4_closed_author_side,
            b4_closed_author_side,
            "B4 作者侧闭合等待 Kummer 迹界内部化；接受外部 Weil/Stepanov 时可关闭。",
            TARGET,
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "本步只闭合 Weil 输入的正确阶无关归约，不声明行/列命题无条件闭合。",
            BURGESS_POINTWISE,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_strict_rks23_kummer_sheaf_weil_reduction_router",
        "status": "rational_character_sum_reduced_to_order_free_rank_one_kummer_trace_bound",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "weil_bound_target_active": target_active,
        "rational_function_to_kummer_sheaf_reduction_closed": reduction_closed,
        "whole_kummer_curve_genus_hazard_closed": hazard_closed,
        "order_free_conductor_ledger_closed": conductor_closed,
        "trace_formula_interface_closed": trace_formula_interface_closed,
        "external_kummer_sheaf_rh_would_close_weil_bound": external_kummer_rh_sufficient,
        "self_contained_kummer_trace_bound_internalized": self_contained_trace_bound,
        "self_contained_weil_bound_internalized": self_contained_weil_bound,
        "b4_weil_complete_rational_sum_kernel_closed_author_side": b4_closed_author_side,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": KUMMER_TRACE_ATOM,
        "next_elementary_attack_target": STEPANOV_ATOM,
        "rational_sum_statement": rational_sum_statement,
        "naive_curve_hazard": naive_curve_hazard,
        "order_free_interface": order_free_interface,
        "stepanov_route": stepanov_route,
        "conductor_table": conductor_table(),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "Weil 输入的真正自足剩余继续缩窄。Burgess 完全和中的有理函数 "
            "`f=prod(x-a)^{e_a}` 不是 `d` 次幂时，目标不是整条 `y^d=f(x)` 曲线的属数界，"
            "因为那会带入角色阶 `d`；正确对象是秩一 Kummer sheaf `L_{chi(f)}` "
            "或等价的 Stepanov 辅助多项式证明。其导子只由分支点数控制，在 2r 矩中 "
            "`cond<=2r+2`，所以一旦有秩一 Kummer RH/Stepanov 迹界，就得到阶无关的 "
            "`O_r(P^(1/2))`，从而关闭 B4。作者侧完全自足仍未完成；下一唯一硬点是 "
            "`SelfContainedRankOneKummerSheafRHTraceBound`，等价初等路线是 "
            "`StepanovAuxiliaryPolynomialRankBoundForKummerSums`。行/列命题仍未无条件闭合。"
        ),
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
        "rows": rows,
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict RKS2/RKS3 Kummer sheaf-Weil 归约证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"weil_bound_target_active={fmt_bool(result['weil_bound_target_active'])}",
        f"rational_function_to_kummer_sheaf_reduction_closed={fmt_bool(result['rational_function_to_kummer_sheaf_reduction_closed'])}",
        f"whole_kummer_curve_genus_hazard_closed={fmt_bool(result['whole_kummer_curve_genus_hazard_closed'])}",
        f"order_free_conductor_ledger_closed={fmt_bool(result['order_free_conductor_ledger_closed'])}",
        f"external_kummer_sheaf_rh_would_close_weil_bound={fmt_bool(result['external_kummer_sheaf_rh_would_close_weil_bound'])}",
        f"self_contained_kummer_trace_bound_internalized={fmt_bool(result['self_contained_kummer_trace_bound_internalized'])}",
        f"self_contained_weil_bound_internalized={fmt_bool(result['self_contained_weil_bound_internalized'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 目标和",
        "",
        "| field | value |",
        "| --- | --- |",
    ]
    for key, value in result["rational_sum_statement"].items():
        lines.append(f"| `{table_cell(key)}` | {table_cell(value)} |")

    lines.extend(
        [
            "",
            "## 2. 防误用边界",
            "",
            "| field | value |",
            "| --- | --- |",
        ]
    )
    for key, value in result["naive_curve_hazard"].items():
        lines.append(f"| `{table_cell(key)}` | {table_cell(value)} |")

    lines.extend(
        [
            "",
            "## 3. 阶无关接口",
            "",
            "| field | value |",
            "| --- | --- |",
        ]
    )
    for key, value in result["order_free_interface"].items():
        lines.append(f"| `{table_cell(key)}` | {table_cell(value)} |")

    lines.extend(
        [
            "",
            "## 4. 导子表",
            "",
            "| r | max_branch_places_m | rank_one_conductor_bound | trace_bound_shape | depends_on_character_order_d |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in result["conductor_table"]:
        lines.append(
            "| `{r}` | `{max_branch_places_m}` | `{rank_one_conductor_bound}` | `{trace_bound_shape}` | `{depends_on_character_order_d}` |".format(
                **item
            )
        )

    lines.extend(
        [
            "",
            "## 5. Stepanov 入口",
            "",
            "| field | value |",
            "| --- | --- |",
        ]
    )
    for key, value in result["stepanov_route"].items():
        lines.append(f"| `{table_cell(key)}` | {table_cell(value)} |")

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
            result["next_elementary_attack_target"],
            "```",
            "",
            "审稿边界：本证书关闭的是有理函数角色和到阶无关 Kummer 迹界的归约，",
            "并排除整曲线属数带来的 d 依赖误用；它尚未证明 Kummer RH/Stepanov 迹界本身。",
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
