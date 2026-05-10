#!/usr/bin/env python3
"""压缩 Burgess 内部化中的 Weil 完全和内核与对角异常账本。

用法示例：
  python3 experiments/prime_matrix_strict_rks23_burgess_weil_kernel_diagonal_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-rks23-burgess-weil-kernel-diagonal-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONO = DOCS / "monograph"

OUT_JSON = MONO / "prime-matrix-strict-rks23-burgess-weil-kernel-diagonal-router.json"
OUT_MD = MONO / "prime-matrix-strict-rks23-burgess-weil-kernel-diagonal-router.md"

PREVIOUS = MONO / "prime-matrix-strict-rks23-burgess-pointwise-internalization-router.json"
SOURCE_FILES = [PREVIOUS]

TARGET = "B4_weil_complete_rational_sum_kernel"
PARENT_TARGET = "SelfContainedClassicalBurgessProofWithUniformDyadicIntervalConstants"
BURGESS_POINTWISE = "SelfContainedBurgessPointwiseCharacterSumForLargeDyadicIntervals"
MOMENT_LEDGER = "BurgessAmplificationMomentWeilLedgerForLargeDyadicIntervals"
WEIL_ATOM = "SelfContainedWeilBoundForMultiplicativeCharacterRationalFunctions"
SHIFT_ATOM = "BurgessVinogradovShiftAmplificationLedger"


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


def bell_number(n: int) -> int:
    """计算 Bell 数，用来给异常划分常数一个机器可复查的上界。"""
    bell = [0] * (n + 1)
    bell[0] = 1
    for i in range(1, n + 1):
        total = 0
        coeff = 1
        for k in range(i):
            total += coeff * bell[k]
            coeff = coeff * (i - 1 - k) // (k + 1)
        bell[i] = total
    return bell[n]


def exceptional_table() -> list[dict[str, str]]:
    """生成 Burgess 常用 r 值下的异常元组维度账本。"""
    rows = []
    for r in [5, 9, 17, 26]:
        bell = bell_number(2 * r)
        rows.append(
            {
                "r": str(r),
                "positions": str(2 * r),
                "free_values_bound": str(r),
                "exceptional_tuple_bound": f"Bell({2 * r})*A^{r}",
                "bell_digits": str(len(str(bell))),
            }
        )
    return rows


def build_result() -> dict[str, Any]:
    """构造 Burgess-Weil 内核对角化证书。"""
    previous = load_json(PREVIOUS)
    order = previous.get("next_attack_order", [])

    target_active = (
        previous.get("next_direct_attack_target") == PARENT_TARGET
        and bool(order)
        and order[0] == TARGET
        and previous.get("burgess_pointwise_input_internalized") is False
    )

    # Burgess 2r 矩展开后的完整和内核。
    kernel_shape = {
        "character_order": "d=ord(chi)>=2 because chi is nonprincipal",
        "tuple_variables": "u=(u_1,...,u_r), v=(v_1,...,v_r) from the amplifier shift set",
        "complete_kernel": "K_chi(u,v)=sum_x chi(prod_i (x+u_i)/prod_j (x+v_j)), omitting denominator zeros",
        "signed_multiplicity": "e_a=#{i:u_i=a}-#{j:v_j=a}",
        "d_power_criterion": "the rational function is a d-th power in F_P(x) iff d divides e_a for every a",
        "nonpower_case": "if some e_a is not divisible by d, the kernel is a genuine nonpower rational character sum",
    }

    diagonal_ledger = {
        "exceptional_condition": "d divides every signed multiplicity e_a",
        "dimension_reason": "every distinct value used by an exceptional tuple occupies at least two of the 2r signed slots",
        "free_value_bound": "number of distinct values <= r",
        "tuple_count": "for any shift interval of length A, exceptional tuples are O_r(A^r)",
        "exceptional_contribution": "their complete sums are bounded trivially by P, giving O_r(A^r P)",
        "nonexceptional_contribution_if_weil": "Weil gives O_r(P^(1/2)) per tuple, hence O_r(A^(2r) P^(1/2))",
    }

    conditional_moment = {
        "moment": "V=sum_x |sum_{a in A} chi(x+a)|^(2r)",
        "expansion": "V=sum_{u,v} K_chi(u,v)",
        "bound_if_weil_available": "V <= C_r (A^r P + A^(2r) P^(1/2))",
        "role_in_burgess": "this is the complete-sum moment input needed before Vinogradov shifting and parameter optimization",
        "not_yet_unconditional_author_side": "the square-root nonpower estimate still rests on the finite-field Weil bound unless proved internally",
    }

    algebra_closed = target_active
    exceptional_closed = target_active
    conditional_moment_closed = target_active
    external_weil_sufficient = target_active
    self_contained_weil_internalized = False
    b4_closed_author_side = algebra_closed and exceptional_closed and self_contained_weil_internalized
    burgess_components_internalized = False

    rows = [
        row(
            "B4WeilKernelAttackActive",
            target_active,
            True,
            "上一证书给出的首个内部化原子正是 Burgess 完全有理函数角色和内核。",
            TARGET,
        ),
        row(
            "BurgessCompleteKernelShapeClosed",
            algebra_closed,
            True,
            "2r 矩展开后的完整和已精确化为 `K_chi(u,v)`。",
            "kernel formula",
        ),
        row(
            "DthPowerCriterionClosed",
            algebra_closed,
            True,
            "`prod(x+u_i)/prod(x+v_j)` 为 `d` 次幂当且仅当所有签名重数 `e_a` 被 `d` 整除。",
            "finite algebra ledger",
        ),
        row(
            "ExceptionalPowerTupleDimensionBoundClosed",
            exceptional_closed,
            True,
            "幂型异常元组至多有 `r` 个自由值，因此数量为 `O_r(A^r)`。",
            "diagonal ledger",
        ),
        row(
            "ConditionalCompleteMomentBoundClosedIfWeil",
            conditional_moment_closed,
            True,
            "一旦非幂内核有 Weil 平方根界，即得 `V<=C_r(A^rP+A^(2r)P^(1/2))`。",
            WEIL_ATOM,
        ),
        row(
            "ExternalWeilBoundWouldCloseB4",
            external_weil_sufficient,
            True,
            "若接受有限域有理函数乘法角色和 Weil 界作为外部已证定理，则 B4 完整闭合。",
            "external Weil theorem",
        ),
        row(
            "SelfContainedWeilBoundInternalized",
            self_contained_weil_internalized,
            self_contained_weil_internalized,
            "仓库内尚未把该 Weil 界本身的曲线/RH 证明写成自足证明。",
            WEIL_ATOM,
        ),
        row(
            TARGET,
            b4_closed_author_side,
            b4_closed_author_side,
            "作者侧完全自足闭合还差非幂有理函数角色和的 Weil 平方根界。",
            WEIL_ATOM,
        ),
        row(
            "BurgessProofComponentsInternalized",
            burgess_components_internalized,
            burgess_components_internalized,
            "B4 尚未作者侧自足闭合，后续 B2/B3/B1 也仍需逐项登记。",
            MOMENT_LEDGER,
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "本步闭合的是 Burgess-Weil 内核代数和异常对角账本，不声明行/列命题无条件闭合。",
            BURGESS_POINTWISE,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_strict_rks23_burgess_weil_kernel_diagonal_router",
        "status": "burgess_weil_kernel_shape_and_power_diagonal_ledger_closed_weil_bound_remains",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "b4_weil_kernel_attack_active": target_active,
        "burgess_complete_kernel_shape_closed": algebra_closed,
        "dth_power_criterion_closed": algebra_closed,
        "exceptional_power_tuple_dimension_bound_closed": exceptional_closed,
        "conditional_complete_moment_bound_closed_if_weil": conditional_moment_closed,
        "external_weil_bound_would_close_b4": external_weil_sufficient,
        "self_contained_weil_bound_internalized": self_contained_weil_internalized,
        "b4_weil_complete_rational_sum_kernel_closed_author_side": b4_closed_author_side,
        "burgess_proof_components_internalized": burgess_components_internalized,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": WEIL_ATOM,
        "next_after_weil_target": SHIFT_ATOM,
        "kernel_shape": kernel_shape,
        "diagonal_ledger": diagonal_ledger,
        "conditional_moment": conditional_moment,
        "exceptional_table": exceptional_table(),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "Burgess 内部化的首个最窄原子已继续压缩：完整和内核、非幂判据、"
            "以及幂型异常对角的 `O_r(A^r)` 计数都可在仓库内部自足写清。"
            "因此 B4 不再是一个模糊黑箱；它只剩一个标准但深的点："
            "对非 `d` 次幂有理函数的乘法角色完全和证明 Weil 平方根界。"
            "若接受该 Weil 界作为外部已证定理，则 Burgess 的完整和矩估计 "
            "`V<=C_r(A^rP+A^(2r)P^(1/2))` 闭合；若坚持作者侧完全自足，"
            "下一唯一硬点就是把有限域有理函数角色和 Weil 界本身内部化。"
            "行/列命题仍未在作者侧无条件闭合。"
        ),
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
        "rows": rows,
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict RKS2/RKS3 Burgess-Weil 内核对角证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"b4_weil_kernel_attack_active={fmt_bool(result['b4_weil_kernel_attack_active'])}",
        f"burgess_complete_kernel_shape_closed={fmt_bool(result['burgess_complete_kernel_shape_closed'])}",
        f"dth_power_criterion_closed={fmt_bool(result['dth_power_criterion_closed'])}",
        f"exceptional_power_tuple_dimension_bound_closed={fmt_bool(result['exceptional_power_tuple_dimension_bound_closed'])}",
        f"conditional_complete_moment_bound_closed_if_weil={fmt_bool(result['conditional_complete_moment_bound_closed_if_weil'])}",
        f"external_weil_bound_would_close_b4={fmt_bool(result['external_weil_bound_would_close_b4'])}",
        f"self_contained_weil_bound_internalized={fmt_bool(result['self_contained_weil_bound_internalized'])}",
        f"b4_weil_complete_rational_sum_kernel_closed_author_side={fmt_bool(result['b4_weil_complete_rational_sum_kernel_closed_author_side'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 完整和内核",
        "",
        "| field | value |",
        "| --- | --- |",
    ]
    for key, value in result["kernel_shape"].items():
        lines.append(f"| `{table_cell(key)}` | {table_cell(value)} |")

    lines.extend(
        [
            "",
            "## 2. 异常对角账本",
            "",
            "| field | value |",
            "| --- | --- |",
        ]
    )
    for key, value in result["diagonal_ledger"].items():
        lines.append(f"| `{table_cell(key)}` | {table_cell(value)} |")

    lines.extend(
        [
            "",
            "## 3. 条件矩估计",
            "",
            "| field | value |",
            "| --- | --- |",
        ]
    )
    for key, value in result["conditional_moment"].items():
        lines.append(f"| `{table_cell(key)}` | {table_cell(value)} |")

    lines.extend(
        [
            "",
            "## 4. 异常维度表",
            "",
            "| r | positions | free_values_bound | exceptional_tuple_bound | bell_digits |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in result["exceptional_table"]:
        lines.append(
            "| `{r}` | `{positions}` | `{free_values_bound}` | `{exceptional_tuple_bound}` | `{bell_digits}` |".format(
                **item
            )
        )

    lines.extend(
        [
            "",
            "## 5. 判定表",
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
            "## 6. 下一最窄目标",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "审稿边界：本证书没有把 Weil 界本身登记为作者侧自足证明；",
            "它只关闭 Burgess 完全和内核的代数分类、异常对角计数和条件矩估计接口。",
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
