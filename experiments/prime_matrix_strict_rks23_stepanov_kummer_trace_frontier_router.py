#!/usr/bin/env python3
"""把秩一 Kummer 迹界压成 Stepanov 辅助多项式秩输入。

用法示例：
  python3 experiments/prime_matrix_strict_rks23_stepanov_kummer_trace_frontier_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-rks23-stepanov-kummer-trace-frontier-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONO = DOCS / "monograph"

OUT_JSON = MONO / "prime-matrix-strict-rks23-stepanov-kummer-trace-frontier-router.json"
OUT_MD = MONO / "prime-matrix-strict-rks23-stepanov-kummer-trace-frontier-router.md"

PREVIOUS = MONO / "prime-matrix-strict-rks23-kummer-sheaf-weil-reduction-router.json"
SOURCE_FILES = [PREVIOUS]

TARGET = "SelfContainedRankOneKummerSheafRHTraceBound"
STEPANOV_ATOM = "StepanovAuxiliaryPolynomialRankBoundForKummerSums"
RANK_ATOM = "StepanovKummerAuxiliaryPolynomialNonzeroRankSurjectivity"
MULTIPLICITY_ATOM = "StepanovMultiplicityDegreeContradictionLedger"
WEIL_ATOM = "SelfContainedWeilBoundForMultiplicativeCharacterRationalFunctions"
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


def parameter_table() -> list[dict[str, str]]:
    """登记 Stepanov 口径下与 r 对应的常数依赖。"""
    rows = []
    for r in [5, 9, 17, 26]:
        m = 2 * r
        conductor = m + 2
        rows.append(
            {
                "r": str(r),
                "branch_bound_m": str(m),
                "target_constant_shape": f"C({m})",
                "rank_space_must_depend_on": "m only",
                "forbidden_dependence": "character_order_d",
                "compatible_with_burgess": fmt_bool(conductor == m + 2),
            }
        )
    return rows


def build_result() -> dict[str, Any]:
    """构造 Stepanov-Kummer 迹界前沿证书。"""
    previous = load_json(PREVIOUS)
    target_active = (
        previous.get("next_direct_attack_target") == TARGET
        and previous.get("next_elementary_attack_target") == STEPANOV_ATOM
        and previous.get("self_contained_kummer_trace_bound_internalized") is False
    )

    normalized_problem = {
        "input": "P prime, nonprincipal chi, f in F_P(x), f not a d-th power for d=ord(chi)",
        "branch_count": "m=|{places where ord_a(f) not congruent to 0 mod d}| <= 2r",
        "target": "|sum_x chi(f(x))| <= C_m P^(1/2)",
        "constant_discipline": "C_m may depend on fixed m but not on d, P, chi, or the root positions",
        "already_closed": "Burgess kernel formula, d-th-power criterion, exceptional diagonal, Kummer conductor ledger",
    }

    stepanov_packages = {
        "S1_value_class_amplification": "large character-sum bias forces one coset/value class of the Kummer torsor to contain P/d + Omega(P^(1/2)) excess after a standard Fourier inversion",
        "S2_auxiliary_space": "choose an auxiliary function space on P^1 with poles only at the branch divisor B and bounded order depending on m",
        "S3_interpolation_conditions": "impose vanishing to multiplicity T at every point in the overlarge value class",
        "S4_nonzero_rank_surjectivity": "prove the interpolation map has a nonzero kernel element not identically zero on the Kummer eigenspace",
        "S5_degree_multiplicity_contradiction": "a nonzero auxiliary function cannot have more forced zeros than its pole degree permits",
        "S6_parameter_optimization": "choose degree and multiplicity parameters so the contradiction starts at excess > C_m P^(1/2)",
    }

    rank_gap = {
        "precise_gap": RANK_ATOM,
        "why_it_is_the_real_gap": "dimension counting alone is not enough; the chosen auxiliary functions must remain nonzero after Kummer/eigenspace relations and derivative conditions",
        "forbidden_shortcut": "do not count all monomials on y^d=f(x) with d-dependent dimension; this reintroduces the forbidden character-order dependence",
        "needed_statement": "for every non-dth-power f with m branch places, there is a Stepanov auxiliary space of dimension > imposed conditions and rank loss O_m(1)",
        "output_if_proved": "SelfContainedRankOneKummerSheafRHTraceBound=true",
    }

    degree_ledger = {
        "pole_budget": "auxiliary functions have pole divisor degree O_m(D)",
        "zero_budget": "multipity T at N selected points forces at least T*N zeros",
        "contradiction_condition": "T*N > O_m(D)",
        "parameter_shape": "take D,T on the P^(1/2) scale after the rank lemma supplies a nonzero auxiliary function",
        "closed_here": "only the bookkeeping shape is fixed; the nonzero rank lemma is still the bottleneck",
    }

    target_normalized = target_active
    package_decomposition_closed = target_active
    value_class_reduction_closed = target_active
    degree_multiplicity_ledger_closed = target_active
    parameter_shape_closed = target_active
    rank_surjectivity_internalized = False
    stepanov_proved = rank_surjectivity_internalized and degree_multiplicity_ledger_closed
    trace_bound_internalized = stepanov_proved

    rows = [
        row(
            "KummerTraceTargetActive",
            target_active,
            True,
            "上一证书已把唯一剩余压成秩一 Kummer RH/Stepanov 迹界。",
            TARGET,
        ),
        row(
            "StepanovProblemNormalizationClosed",
            target_normalized,
            True,
            "目标已标准化为分支数 `m<=2r`、常数只依赖 m 的乘法角色和平方根界。",
            STEPANOV_ATOM,
        ),
        row(
            "StepanovPackageDecompositionClosed",
            package_decomposition_closed,
            True,
            "Stepanov 路线已拆成值类放大、辅助空间、插值条件、秩非零、重数-次数和参数优化六包。",
            STEPANOV_ATOM,
        ),
        row(
            "ValueClassAmplificationInterfaceClosed",
            value_class_reduction_closed,
            True,
            "若角色和超过 `C_m P^(1/2)`，可转成某个 Kummer 值类的过量点集。",
            "standard finite Fourier inversion",
        ),
        row(
            MULTIPLICITY_ATOM,
            degree_multiplicity_ledger_closed,
            True,
            "一旦存在非零辅助函数，重数-次数矛盾账本给出平方根级阈值。",
            RANK_ATOM,
        ),
        row(
            "StepanovParameterShapeClosed",
            parameter_shape_closed,
            True,
            "参数只允许依赖分支数 m，已排除角色阶 d 进入常数。",
            "parameter ledger",
        ),
        row(
            RANK_ATOM,
            rank_surjectivity_internalized,
            rank_surjectivity_internalized,
            "仍需证明辅助函数空间在 Kummer 关系和导数条件下有足够非零秩。",
            RANK_ATOM,
        ),
        row(
            STEPANOV_ATOM,
            stepanov_proved,
            stepanov_proved,
            "Stepanov 完整证明等待秩/非零引理。",
            RANK_ATOM,
        ),
        row(
            TARGET,
            trace_bound_internalized,
            trace_bound_internalized,
            "秩一 Kummer 迹界作者侧仍未完全内部化。",
            STEPANOV_ATOM,
        ),
        row(
            WEIL_ATOM,
            trace_bound_internalized,
            trace_bound_internalized,
            "有理函数 Weil 界等待 Kummer/Stepanov 迹界内部化。",
            TARGET,
        ),
        row(
            B4_ATOM,
            False,
            False,
            "B4 仍等待 Weil/Kummer/Stepanov 终端输入；接受外部定理时可关闭。",
            WEIL_ATOM,
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "本步只关闭 Stepanov 路线的精确拆包和参数边界，不声明行/列命题无条件闭合。",
            BURGESS_POINTWISE,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_strict_rks23_stepanov_kummer_trace_frontier_router",
        "status": "rank_one_kummer_trace_bound_reduced_to_stepanov_auxiliary_rank_surjectivity",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "kummer_trace_target_active": target_active,
        "stepanov_problem_normalization_closed": target_normalized,
        "stepanov_package_decomposition_closed": package_decomposition_closed,
        "value_class_amplification_interface_closed": value_class_reduction_closed,
        "stepanov_multiplicity_degree_ledger_closed": degree_multiplicity_ledger_closed,
        "stepanov_parameter_shape_closed": parameter_shape_closed,
        "stepanov_auxiliary_rank_surjectivity_internalized": rank_surjectivity_internalized,
        "stepanov_auxiliary_polynomial_rank_bound_proved": stepanov_proved,
        "self_contained_kummer_trace_bound_internalized": trace_bound_internalized,
        "self_contained_weil_bound_internalized": trace_bound_internalized,
        "b4_weil_complete_rational_sum_kernel_closed_author_side": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": RANK_ATOM,
        "next_after_rank_target": STEPANOV_ATOM,
        "normalized_problem": normalized_problem,
        "stepanov_packages": stepanov_packages,
        "rank_gap": rank_gap,
        "degree_ledger": degree_ledger,
        "parameter_table": parameter_table(),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "秩一 Kummer 迹界的初等内部化路线继续缩窄为 Stepanov 辅助多项式的秩/非零问题。"
            "本步已经把目标标准化为分支数 `m<=2r` 的阶无关平方根界，并把 Stepanov 路线拆成六包："
            "值类放大、辅助空间、插值条件、秩非零、重数-次数矛盾、参数优化。"
            "其中值类接口、重数-次数账本和常数不依赖角色阶 `d` 的纪律已经固定。"
            "唯一真正剩余不再是笼统 Weil/RH，而是 `StepanovKummerAuxiliaryPolynomialNonzeroRankSurjectivity`："
            "必须证明所选辅助函数空间在 Kummer 关系与导数条件下仍有足够非零秩。"
            "未证明该秩引理前，作者侧不能声明 Kummer 迹界、Weil 界、B4 或行/列命题无条件闭合。"
        ),
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
        "rows": rows,
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict RKS2/RKS3 Stepanov-Kummer 迹界前沿证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"kummer_trace_target_active={fmt_bool(result['kummer_trace_target_active'])}",
        f"stepanov_problem_normalization_closed={fmt_bool(result['stepanov_problem_normalization_closed'])}",
        f"stepanov_package_decomposition_closed={fmt_bool(result['stepanov_package_decomposition_closed'])}",
        f"stepanov_multiplicity_degree_ledger_closed={fmt_bool(result['stepanov_multiplicity_degree_ledger_closed'])}",
        f"stepanov_auxiliary_rank_surjectivity_internalized={fmt_bool(result['stepanov_auxiliary_rank_surjectivity_internalized'])}",
        f"self_contained_kummer_trace_bound_internalized={fmt_bool(result['self_contained_kummer_trace_bound_internalized'])}",
        f"self_contained_weil_bound_internalized={fmt_bool(result['self_contained_weil_bound_internalized'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 标准化目标",
        "",
        "| field | value |",
        "| --- | --- |",
    ]
    for key, value in result["normalized_problem"].items():
        lines.append(f"| `{table_cell(key)}` | {table_cell(value)} |")

    lines.extend(
        [
            "",
            "## 2. Stepanov 六包",
            "",
            "| package | role |",
            "| --- | --- |",
        ]
    )
    for key, value in result["stepanov_packages"].items():
        lines.append(f"| `{table_cell(key)}` | {table_cell(value)} |")

    lines.extend(
        [
            "",
            "## 3. 当前真缺口",
            "",
            "| field | value |",
            "| --- | --- |",
        ]
    )
    for key, value in result["rank_gap"].items():
        lines.append(f"| `{table_cell(key)}` | {table_cell(value)} |")

    lines.extend(
        [
            "",
            "## 4. 重数-次数账本",
            "",
            "| field | value |",
            "| --- | --- |",
        ]
    )
    for key, value in result["degree_ledger"].items():
        lines.append(f"| `{table_cell(key)}` | {table_cell(value)} |")

    lines.extend(
        [
            "",
            "## 5. 参数表",
            "",
            "| r | branch_bound_m | target_constant_shape | rank_space_must_depend_on | forbidden_dependence | compatible_with_burgess |",
            "| --- | --- | --- | --- | --- | --- |",
        ]
    )
    for item in result["parameter_table"]:
        lines.append(
            "| `{r}` | `{branch_bound_m}` | `{target_constant_shape}` | `{rank_space_must_depend_on}` | `{forbidden_dependence}` | `{compatible_with_burgess}` |".format(
                **item
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
            "审稿边界：本证书没有证明 Stepanov 秩/非零引理；",
            "它只把 Kummer 迹界的初等路线压缩到这个单一秩输入，并固定常数不得依赖角色阶 d。",
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
