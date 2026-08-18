"""审计截断 Möbius--log 系数族的 Möbius 尾和整体 L² 门槛。"""

import argparse
from fractions import Fraction
import json
from math import gcd, isfinite, log
from pathlib import Path
import sys
from typing import Mapping

if __package__ in (None, ""):
    # 直接用脚本路径启动时，把仓库根目录加入导入路径。
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from experiments.prime_matrix_mfac_truncated_mobius_log_coercivity_audit import (
    mobius_value,
)


DEFAULT_JSON = Path("docs/monograph/prime-matrix-mfac-mobius-tail-l2-audit.json")
DEFAULT_MARKDOWN = Path("docs/monograph/prime-matrix-mfac-mobius-tail-l2-audit.md")
ANALYTIC_MOBIUS_DEPENDENCIES = frozenset(
    {
        "PNT",
        "Mertens_cancellation",
        "zero_free_region",
        "zeta_zero",
        "explicit_formula",
        "Mellin",
        "RH",
    }
)


def _checked_fraction_coefficients(
    coefficients: Mapping[int, Fraction],
) -> dict[int, Fraction]:
    """验证有限有理系数，避免代数审计隐式接受错误输入。"""
    if not isinstance(coefficients, Mapping) or not coefficients:
        raise ValueError("coefficients 必须是非空 Mapping")
    checked: dict[int, Fraction] = {}
    for index, value in coefficients.items():
        if type(index) is not int or index < 2:
            raise ValueError("系数指标必须是至少为 2 的内建整数")
        if not isinstance(value, Fraction):
            raise ValueError("系数必须是 Fraction")
        checked[index] = value
    return checked


def _checked_float_coefficients(coefficients: Mapping[int, float]) -> dict[int, float]:
    """验证有限浮点系数，拒绝非有限值和非内建数值类型。"""
    if not isinstance(coefficients, Mapping) or not coefficients:
        raise ValueError("coefficients 必须是非空 Mapping")
    checked: dict[int, float] = {}
    for index, value in coefficients.items():
        if type(index) is not int or index < 2:
            raise ValueError("系数指标必须是至少为 2 的内建整数")
        if type(value) not in (int, float) or not isfinite(float(value)):
            raise ValueError("系数必须是有限内建数值")
        checked[index] = float(value)
    return checked


def _require_cutoff(cutoff: object) -> int:
    """验证截断点，确保线性窗口和对数分母有效。"""
    if type(cutoff) is not int or cutoff < 3:
        raise ValueError("cutoff 必须是至少为 3 的内建整数")
    return cutoff


def _checked_string_tuple(value: object, field_name: str) -> tuple[str, ...]:
    """验证合同中的字符串序列，拒绝裸字符串和非字符串元素。"""
    if type(value) not in (tuple, list):
        raise ValueError(f"{field_name} 必须是字符串 tuple 或 list")
    if any(type(item) is not str or not item for item in value):
        raise ValueError(f"{field_name} 必须只含非空字符串")
    return tuple(value)


def euler_phi(index: object) -> int:
    """以有限试除法计算 Euler phi，用于精确代数审计。"""
    if type(index) is not int or index < 1:
        raise ValueError("index 必须是至少为 1 的内建整数")
    value = index
    remaining = index
    divisor = 2
    while divisor * divisor <= remaining:
        if remaining % divisor == 0:
            value -= value // divisor
            while remaining % divisor == 0:
                remaining //= divisor
        divisor += 1
    if remaining > 1:
        value -= value // remaining
    return value


def limit_kernel_energy(coefficients: Mapping[int, Fraction]) -> Fraction:
    """以精确有理数计算 sum a_d a_e ((d,e)-1)/(de)。"""
    checked = _checked_fraction_coefficients(coefficients)
    return sum(
        left_value * right_value * Fraction(gcd(left, right) - 1, left * right)
        for left, left_value in checked.items()
        for right, right_value in checked.items()
    )


def divisor_tail_sum(coefficients: Mapping[int, Fraction], divisor: int) -> Fraction:
    """返回 T(r)=sum_{r|d} a_d/d 的精确有限尾和。"""
    checked = _checked_fraction_coefficients(coefficients)
    if type(divisor) is not int or divisor < 2:
        raise ValueError("divisor 必须是至少为 2 的内建整数")
    return sum(value / index for index, value in checked.items() if index % divisor == 0)


def euler_phi_square_energy(coefficients: Mapping[int, Fraction]) -> Fraction:
    """以 sum_{r>=2} phi(r) T(r)^2 计算极限核能量。"""
    checked = _checked_fraction_coefficients(coefficients)
    cutoff = max(checked)
    return sum(
        Fraction(euler_phi(divisor), 1) * divisor_tail_sum(checked, divisor) ** 2
        for divisor in range(2, cutoff + 1)
    )


def truncated_mobius_log_limit_coefficients(cutoff: object) -> dict[int, float]:
    """构造固定线性窗口下的截断 Möbius--log 系数族。"""
    checked_cutoff = _require_cutoff(cutoff)
    logarithmic_cutoff = log(float(checked_cutoff))
    return {
        index: -mobius * log(float(index)) * (
            1.0 - log(float(index)) / logarithmic_cutoff
        )
        for index in range(2, checked_cutoff)
        if (mobius := mobius_value(index)) != 0
    }


def limit_kernel_energy_float(coefficients: Mapping[int, float]) -> float:
    """以浮点数直接计算有限极限核，供分解残差审计。"""
    checked = _checked_float_coefficients(coefficients)
    return sum(
        left_value * right_value * (gcd(left, right) - 1) / (left * right)
        for left, left_value in checked.items()
        for right, right_value in checked.items()
    )


def mobius_log_tail_sum(cutoff: object, divisor: object) -> float:
    """返回目标系数族的 T_D(r)；非平方自由 r 精确返回零。"""
    checked_cutoff = _require_cutoff(cutoff)
    if type(divisor) is not int or not 2 <= divisor < checked_cutoff:
        raise ValueError("divisor 必须是位于 [2, cutoff) 的内建整数")
    if mobius_value(divisor) == 0:
        return 0.0
    logarithmic_cutoff = log(float(checked_cutoff))
    return -mobius_value(divisor) / divisor * sum(
        mobius_value(multiplier)
        * log(float(divisor * multiplier))
        / multiplier
        * (1.0 - log(float(divisor * multiplier)) / logarithmic_cutoff)
        for multiplier in range(1, checked_cutoff // divisor + 1)
        if divisor * multiplier < checked_cutoff and gcd(divisor, multiplier) == 1
    )


def euler_phi_square_energy_float(coefficients: Mapping[int, float]) -> float:
    """以浮点系数计算 Euler--phi 分解能量，供有限诊断使用。"""
    checked = _checked_float_coefficients(coefficients)
    cutoff = max(checked) + 1
    return sum(
        euler_phi(divisor)
        * sum(value / index for index, value in checked.items() if index % divisor == 0)
        ** 2
        for divisor in range(2, cutoff)
    )


def audit_mobius_tail_l2(cutoff: object) -> dict[str, object]:
    """输出固定 D 的 L² 门槛数值诊断，不升级为 L2--Upper 定理。"""
    checked_cutoff = _require_cutoff(cutoff)
    coefficients = truncated_mobius_log_limit_coefficients(checked_cutoff)
    direct_energy = limit_kernel_energy_float(coefficients)
    numerator = euler_phi_square_energy_float(coefficients)
    mass = sum(value * value / index for index, value in coefficients.items())
    return {
        "certificate_type": "prime_matrix_mfac_mobius_tail_l2_audit",
        "status": "numerical_only_mobius_tail_l2_profile",
        "cutoff": checked_cutoff,
        "coefficient_support_size": len(coefficients),
        "limit_kernel_energy": direct_energy,
        "euler_phi_square_energy": numerator,
        "energy_identity_residual": abs(direct_energy - numerator),
        "mass": mass,
        "normalized_ratio": numerator / mass,
        "log_scaled_ratio": log(float(checked_cutoff)) * numerator / mass,
        "l2_upper_status": "unproved",
        "mass_lower_status": "unproved",
        "mobius_cancellation_dependency_status": "unresolved",
        "rh_proved": False,
    }


def audit_l2_upper_contract(contract: Mapping[str, object]) -> dict[str, object]:
    """分类 L2--Upper 的外部 Möbius 消去依赖，不允许隐式读取。"""
    if not isinstance(contract, Mapping):
        raise ValueError("contract 必须为 Mapping")
    uses = _checked_string_tuple(contract.get("uses", ()), "uses")
    claimed = _checked_string_tuple(
        contract.get("claimed_bound_uses", uses), "claimed_bound_uses"
    )
    undeclared = tuple(sorted(set(claimed).difference(uses)))
    if undeclared:
        raise ValueError("claimed_bound_uses 含未声明输入: " + ", ".join(undeclared))
    dependencies = tuple(sorted(set(uses).intersection(ANALYTIC_MOBIUS_DEPENDENCIES)))
    return {
        "classification": (
            "conditional_on_named_mobius_estimate"
            if dependencies
            else "no_external_mobius_estimate_declared"
        ),
        "analytic_dependencies": dependencies,
    }


def render_markdown(certificate: Mapping[str, object]) -> str:
    """渲染有限 L² 诊断，并保留未证明边界。"""
    return (
        "# MFAC Möbius 尾和整体 L² 有限审计\n\n"
        f"- 截断：`D={certificate['cutoff']}`\n"
        f"- 有限比率：`{certificate['normalized_ratio']}`\n"
        f"- log 缩放比率：`{certificate['log_scaled_ratio']}`\n"
        f"- Euler--phi 残差：`{certificate['energy_identity_residual']}`\n\n"
        "```text\n"
        f"l2_upper_status={certificate['l2_upper_status']}\n"
        f"mass_lower_status={certificate['mass_lower_status']}\n"
        "mobius_cancellation_dependency_status="
        f"{certificate['mobius_cancellation_dependency_status']}\n"
        f"rh_proved={str(certificate['rh_proved']).lower()}\n"
        "```\n\n"
        "该证书只验证有限代数分解与数值剖面；不构成 L2--Upper、Mass--Lower、"
        "统一强制性、Chebyshev 能量桥、Mellin 收缩、零自由区域或 RH 证明。\n"
    )


def write_certificate(
    certificate: Mapping[str, object], json_path: Path, markdown_path: Path
) -> None:
    """写出有限 L² 诊断 JSON 与 Markdown，并自动创建父目录。"""
    json_path.parent.mkdir(parents=True, exist_ok=True)
    markdown_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(
        json.dumps(certificate, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    markdown_path.write_text(render_markdown(certificate), encoding="utf-8")


def main() -> None:
    """命令行入口：生成 Möbius 尾和 L² 有限证书。"""
    parser = argparse.ArgumentParser(description="生成 MFAC Möbius 尾和 L² 有限审计")
    parser.add_argument("--cutoff", type=int, default=4096)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--markdown-out", type=Path, default=DEFAULT_MARKDOWN)
    args = parser.parse_args()

    certificate = audit_mobius_tail_l2(args.cutoff)
    certificate["l2_upper_contract"] = audit_l2_upper_contract(
        {"uses": ("finite_divisor_identity", "euler_phi_identity")}
    )
    write_certificate(certificate, args.json_out, args.markdown_out)
    print(f"wrote {args.json_out}")
    print(f"wrote {args.markdown_out}")


if __name__ == "__main__":
    main()
