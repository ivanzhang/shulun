#!/usr/bin/env python3
"""审计 terminal sibling q-spine kernel 是否继续降为整数守恒。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_terminal_sibling_qspine_integer_balance_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-terminal-sibling-qspine-integer-balance-router.json

上一层已经证明 m773 terminal double-Awrap debt 等于已支付 sibling m769 tail
加一个 P-scaled q-spine 三分母 kernel。本层只做更细的有限降阶：

  295/(461*467)
    = 203/(439*467) + 60/(439*461) + 18/(461*467)

乘以 439*461*467 后变成整数守恒

  295*439 = 203*461 + 60*467 + 18*439.

同时，m769 与 m773 的 endpoint collar 系数都由同一公式给出：

  coeff = (461*467 - D_start*467 - A_end*461)/607.

这仍不是无条件闭合；它把 terminal collar payment 门从有理 kernel
进一步压成整数 balance payment/exclusion 或 PDEC。
"""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-terminal-sibling-qspine-integer-balance"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

SIBLING_KERNEL_JSON = DOCS / "prime-matrix-phi-lpf-terminal-double-awrap-sibling-qspine-kernel-router.json"

PIVOT_LAW = "BridgeRootQSpinePivotEnclosureLawOrPDEC"
INTEGER_BALANCE_LAW = "TerminalSiblingQSpineIntegerBalancePaymentOrPDEC"
MASS_RATIO_LAW = "BoundaryAdjacentRunMassRatioLawOrPDEC"
ORIENTATION_LAW = "PrimitiveOrientationLocalFactorProductLawBeforePushforward"
MOVING_BEATTY_SAVING = "SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving"
TRACE_FAMILY = "AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily"
GROUP_ORBIT_INPUT = "AdmissibleFiniteGroupOrbitExpansionOrThinGroupSieveFamily"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    paths = [Path(__file__).resolve(), SIBLING_KERNEL_JSON]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def frac_record(value: Fraction) -> dict[str, Any]:
    """稳定输出分数。"""
    return {
        "fraction": f"{value.numerator}/{value.denominator}",
        "decimal": f"{float(value):.12f}",
        "numerator": value.numerator,
        "denominator": value.denominator,
    }


def frac_from_record(record: dict[str, Any]) -> Fraction:
    """从 JSON 分数记录恢复 Fraction。"""
    return Fraction(int(record["numerator"]), int(record["denominator"]))


def fmt_bool(value: Any) -> str:
    """布尔值小写渲染。"""
    return "true" if bool(value) else "false"


def cell(value: Any) -> str:
    """Markdown 表格单元转义。"""
    return str(value).replace("|", r"\|")


def render_fraction(record: dict[str, Any]) -> str:
    """表格用分数摘要。"""
    return f"{record['decimal']} ({record['fraction']})"


def endpoint_coefficient(q_mid: int, q_right: int, p: int, d_start: int, a_end: int) -> dict[str, Any]:
    """计算 endpoint collar 的 P-scaled 系数。"""
    numerator = q_mid * q_right - d_start * q_right - a_end * q_mid
    return {
        "numerator": numerator,
        "divisible_by_P": numerator % p == 0,
        "coefficient": numerator // p if numerator % p == 0 else None,
        "formula": f"({q_mid}*{q_right} - {d_start}*{q_right} - {a_end}*{q_mid})/{p}",
    }


def build_certificate() -> dict[str, Any]:
    """组装 integer-balance 证书。"""
    sibling_kernel = load_json(SIBLING_KERNEL_JSON)

    p = int(sibling_kernel["P"])
    q_path = [int(q) for q in sibling_kernel["target_signature"]["q_path"]]
    q_mid = q_path[0]
    q_right = q_path[-1]

    paid_tail = frac_from_record(sibling_kernel["paid_sibling_tail_mass"])
    middle_kernel = frac_from_record(sibling_kernel["sibling_final_minus_paid"])
    endpoint_offset = frac_from_record(sibling_kernel["sibling_endpoint_offset"])
    target_tail = frac_from_record(sibling_kernel["target_final_tail_mass"])
    sibling_final = frac_from_record(sibling_kernel["sibling_final_collar_mass"])

    if paid_tail.denominator % q_right != 0:
        raise ValueError("paid tail denominator is not q_prefix*q_right")
    q_prefix_from_paid = paid_tail.denominator // q_right
    if middle_kernel.denominator % q_mid != 0:
        raise ValueError("middle kernel denominator is not q_prefix*q_mid")
    q_prefix_from_middle = middle_kernel.denominator // q_mid
    q_prefix = q_prefix_from_paid

    coefficients = sibling_kernel["p_scaled_coefficients"]
    paid_coeff = int(coefficients["paid_sibling_tail"])
    middle_coeff = int(coefficients["sibling_final_minus_paid"])
    offset_coeff = int(coefficients["sibling_endpoint_offset"])
    target_coeff = int(coefficients["target_final_tail"])
    sibling_final_coeff = int(coefficients["sibling_final_collar"])

    normalized_identity = target_tail / p == (
        Fraction(paid_coeff, q_prefix * q_right)
        + Fraction(middle_coeff, q_prefix * q_mid)
        + Fraction(offset_coeff, q_mid * q_right)
    )
    integer_balance_left = target_coeff * q_prefix
    integer_balance_terms = {
        "paid_tail_term": paid_coeff * q_mid,
        "middle_kernel_term": middle_coeff * q_right,
        "endpoint_offset_term": offset_coeff * q_prefix,
    }
    integer_balance_right = sum(integer_balance_terms.values())
    integer_balance_closed = integer_balance_left == integer_balance_right

    sibling_sig = sibling_kernel["sibling_signature"]
    target_sig = sibling_kernel["target_signature"]
    sibling_endpoint = endpoint_coefficient(
        q_mid=q_mid,
        q_right=q_right,
        p=p,
        d_start=int(sibling_sig["D_path"][0]),
        a_end=int(sibling_sig["A_path"][-1]),
    )
    target_endpoint = endpoint_coefficient(
        q_mid=q_mid,
        q_right=q_right,
        p=p,
        d_start=int(target_sig["D_path"][0]),
        a_end=int(target_sig["A_path"][-1]),
    )
    endpoint_coefficients_closed = (
        sibling_endpoint["coefficient"] == sibling_final_coeff
        and target_endpoint["coefficient"] == target_coeff
    )
    offset_formula_numerator = (
        (int(sibling_sig["D_path"][0]) - int(target_sig["D_path"][0])) * q_right
        + (int(sibling_sig["A_path"][-1]) - int(target_sig["A_path"][-1])) * q_mid
    )
    offset_formula_closed = (
        offset_formula_numerator % p == 0
        and offset_formula_numerator // p == offset_coeff
        and target_coeff - sibling_final_coeff == offset_coeff
    )

    denominators_closed = (
        q_prefix_from_paid == q_prefix_from_middle == q_prefix
        and paid_tail.denominator == q_prefix * q_right
        and middle_kernel.denominator == q_prefix * q_mid
        and endpoint_offset.denominator == q_mid * q_right
        and target_tail.denominator == q_mid * q_right
        and sibling_final.denominator == q_mid * q_right
    )
    inherited_kernel_closed = (
        sibling_kernel.get("terminal_double_awrap_sibling_qspine_kernel_closed") is True
        and sibling_kernel.get("terminal_double_awrap_sibling_qspine_kernel_payment_law_proved") is False
    )
    reduction_closed = all(
        [
            inherited_kernel_closed,
            denominators_closed,
            normalized_identity,
            integer_balance_closed,
            endpoint_coefficients_closed,
            offset_formula_closed,
        ]
    )

    latest_open_gate = (
        f"{PIVOT_LAW} AND {INTEGER_BALANCE_LAW} AND {MASS_RATIO_LAW} AND "
        f"{ORIENTATION_LAW} AND {MOVING_BEATTY_SAVING} AND {TRACE_FAMILY} AND {GROUP_ORBIT_INPUT}"
    )
    return {
        "certificate_type": "prime_matrix_phi_lpf_terminal_sibling_qspine_integer_balance_router",
        "status": "terminal_sibling_qspine_integer_balance_closed_payment_law_open",
        "verified_date": "2026-05-25",
        "previous_sibling_qspine_kernel_closed": inherited_kernel_closed,
        "P": p,
        "q_prefix": q_prefix,
        "q_mid": q_mid,
        "q_right": q_right,
        "q_spine_for_balance": [q_prefix, q_mid, q_right],
        "q_path_from_double_awrap": q_path,
        "coefficients": {
            "target_final_tail": target_coeff,
            "paid_sibling_tail": paid_coeff,
            "middle_kernel": middle_coeff,
            "endpoint_offset": offset_coeff,
            "sibling_final_collar": sibling_final_coeff,
        },
        "kernel_masses": {
            "target_final_tail_mass": frac_record(target_tail),
            "sibling_final_collar_mass": frac_record(sibling_final),
            "paid_sibling_tail_mass": frac_record(paid_tail),
            "middle_kernel_mass": frac_record(middle_kernel),
            "endpoint_offset_mass": frac_record(endpoint_offset),
        },
        "denominators_closed": denominators_closed,
        "normalized_identity_closed": normalized_identity,
        "normalized_identity": (
            f"{target_coeff}/({q_mid}*{q_right}) = "
            f"{paid_coeff}/({q_prefix}*{q_right}) + "
            f"{middle_coeff}/({q_prefix}*{q_mid}) + "
            f"{offset_coeff}/({q_mid}*{q_right})"
        ),
        "integer_balance_closed": integer_balance_closed,
        "integer_balance": {
            "left": integer_balance_left,
            "right": integer_balance_right,
            "formula": (
                f"{target_coeff}*{q_prefix} = {paid_coeff}*{q_mid} "
                f"+ {middle_coeff}*{q_right} + {offset_coeff}*{q_prefix}"
            ),
            "terms": integer_balance_terms,
        },
        "sibling_endpoint_coefficient": sibling_endpoint,
        "target_endpoint_coefficient": target_endpoint,
        "endpoint_coefficients_closed": endpoint_coefficients_closed,
        "endpoint_coefficient_formula": (
            f"coeff=(q_mid*q_right - D_start*q_right - A_end*q_mid)/{p}"
        ),
        "endpoint_offset_formula": {
            "numerator": offset_formula_numerator,
            "coefficient": offset_formula_numerator // p if offset_formula_numerator % p == 0 else None,
            "closed": offset_formula_closed,
            "formula": (
                f"(({sibling_sig['D_path'][0]}-{target_sig['D_path'][0]})*{q_right} + "
                f"({sibling_sig['A_path'][-1]}-{target_sig['A_path'][-1]})*{q_mid})/{p}"
            ),
        },
        "terminal_sibling_qspine_integer_balance_closed": reduction_closed,
        "terminal_sibling_qspine_integer_balance_payment_law_proved": False,
        "admissible_trace_or_typeii_family_constructed": False,
        "finite_group_orbit_expansion_family_constructed": False,
        "phi_lpf_parity_barrier_globally_broken": False,
        "row_column_unconditional_closed": False,
        "latest_open_gate": latest_open_gate,
        "next_primary_attack_target": INTEGER_BALANCE_LAW,
        "gate_rows": [
            {
                "gate": "SiblingQSpineKernelImported",
                "closed": inherited_kernel_closed,
                "proved": inherited_kernel_closed,
                "meaning": "上一层 P-scaled sibling q-spine kernel 已有限闭合，支付律仍未证明。",
                "remaining": "finite sibling-kernel ledger",
            },
            {
                "gate": "QSpineDenominatorAlignment",
                "closed": denominators_closed,
                "proved": denominators_closed,
                "meaning": "三个分母精确落在 right-side q-spine [439,461,467] 的三条二点边上。",
                "remaining": "finite denominator ledger",
            },
            {
                "gate": "IntegerBalanceIdentity",
                "closed": integer_balance_closed,
                "proved": integer_balance_closed,
                "meaning": "三分母 kernel 等价于整数守恒 295*439=203*461+60*467+18*439。",
                "remaining": "finite integer identity",
            },
            {
                "gate": "EndpointCoefficientFormula",
                "closed": endpoint_coefficients_closed,
                "proved": endpoint_coefficients_closed,
                "meaning": "m769 与 m773 的 endpoint collar 系数服从同一 D_start/A_end 公式。",
                "remaining": "finite endpoint coefficient ledger",
            },
            {
                "gate": "EndpointOffsetFormula",
                "closed": offset_formula_closed,
                "proved": offset_formula_closed,
                "meaning": "m773 相对 m769 的 offset 系数 18 来自两个 endpoint 数据的差分公式。",
                "remaining": "finite endpoint difference ledger",
            },
            {
                "gate": "TerminalSiblingQSpineIntegerBalancePaymentLaw",
                "closed": False,
                "proved": False,
                "meaning": "仍需一个 uniform law 支付或排除该整数 balance，而不能只在 m773 有限点成立。",
                "remaining": INTEGER_BALANCE_LAW,
            },
            {
                "gate": "RowColumnUnconditionalClosureReached",
                "closed": False,
                "proved": False,
                "meaning": "这是 finite integer-balance reduction，不是全局奇偶性突破定理。",
                "remaining": f"{PIVOT_LAW} AND {MASS_RATIO_LAW} AND {ORIENTATION_LAW} AND {MOVING_BEATTY_SAVING}",
            },
        ],
        "plain_conclusion": (
            "The terminal sibling q-spine kernel is equivalent to the integer balance "
            "295*439 = 203*461 + 60*467 + 18*439, and both m769/m773 endpoint collar "
            "coefficients are given by the same D_start/A_end formula. The remaining task "
            "is a uniform integer-balance payment/exclusion law or PDEC."
        ),
        "source_hashes": source_hashes(),
    }


def render_markdown(payload: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF terminal sibling q-spine integer-balance 证书",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['verified_date']}`",
        "",
        "本证书把上一层 P-scaled q-spine 三分母 kernel 继续压成一个整数守恒。",
        "",
        "```text",
        f"q_spine_for_balance={payload['q_spine_for_balance']}",
        f"q_path_from_double_awrap={payload['q_path_from_double_awrap']}",
        f"denominators_closed={fmt_bool(payload['denominators_closed'])}",
        f"normalized_identity_closed={fmt_bool(payload['normalized_identity_closed'])}",
        f"integer_balance_closed={fmt_bool(payload['integer_balance_closed'])}",
        f"endpoint_coefficients_closed={fmt_bool(payload['endpoint_coefficients_closed'])}",
        f"endpoint_offset_formula_closed={fmt_bool(payload['endpoint_offset_formula']['closed'])}",
        f"terminal_sibling_qspine_integer_balance_closed={fmt_bool(payload['terminal_sibling_qspine_integer_balance_closed'])}",
        f"terminal_sibling_qspine_integer_balance_payment_law_proved={fmt_bool(payload['terminal_sibling_qspine_integer_balance_payment_law_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(payload['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. integer balance",
        "",
        "```text",
        payload["normalized_identity"],
        payload["integer_balance"]["formula"],
        f"{payload['integer_balance']['left']} = {payload['integer_balance']['right']}",
        "```",
        "",
        "## 2. exact kernel masses",
        "",
        "| quantity | value | coefficient |",
        "| --- | --- | ---: |",
        f"| `target_final_tail_mass` | {render_fraction(payload['kernel_masses']['target_final_tail_mass'])} | {payload['coefficients']['target_final_tail']} |",
        f"| `sibling_final_collar_mass` | {render_fraction(payload['kernel_masses']['sibling_final_collar_mass'])} | {payload['coefficients']['sibling_final_collar']} |",
        f"| `paid_sibling_tail_mass` | {render_fraction(payload['kernel_masses']['paid_sibling_tail_mass'])} | {payload['coefficients']['paid_sibling_tail']} |",
        f"| `middle_kernel_mass` | {render_fraction(payload['kernel_masses']['middle_kernel_mass'])} | {payload['coefficients']['middle_kernel']} |",
        f"| `endpoint_offset_mass` | {render_fraction(payload['kernel_masses']['endpoint_offset_mass'])} | {payload['coefficients']['endpoint_offset']} |",
        "",
        "## 3. endpoint coefficients",
        "",
        "```text",
        payload["endpoint_coefficient_formula"],
        f"m769: {payload['sibling_endpoint_coefficient']['formula']} = {payload['sibling_endpoint_coefficient']['coefficient']}",
        f"m773: {payload['target_endpoint_coefficient']['formula']} = {payload['target_endpoint_coefficient']['coefficient']}",
        f"offset: {payload['endpoint_offset_formula']['formula']} = {payload['endpoint_offset_formula']['coefficient']}",
        "```",
        "",
        "## 4. 门控表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in payload["gate_rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=cell(row["gate"]),
                closed=fmt_bool(row["closed"]),
                proved=fmt_bool(row["proved"]),
                meaning=cell(row["meaning"]),
                remaining=cell(row["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 5. 最新开放口",
            "",
            "```text",
            payload["latest_open_gate"],
            "```",
            "",
            "## 6. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in sorted(payload["source_hashes"].items()):
        lines.append(f"| `{path}` | `{digest}` |")
    lines.extend(["", "行/列命题仍未无条件闭合。", ""])
    return "\n".join(lines)


def write_outputs(payload: dict[str, Any]) -> None:
    """写出 JSON、ledger 与 Markdown。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    text = json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True)
    OUT_LEDGER.write_text(text + "\n", encoding="utf-8")
    OUT_JSON.write_text(text + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(payload), encoding="utf-8")


def main() -> None:
    """命令入口。"""
    payload = build_certificate()
    write_outputs(payload)
    print(
        "terminal_sibling_qspine_integer_balance_closed="
        f"{fmt_bool(payload['terminal_sibling_qspine_integer_balance_closed'])}"
    )
    print(f"integer_balance_closed={fmt_bool(payload['integer_balance_closed'])}")
    print(f"row_column_unconditional_closed={fmt_bool(payload['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
