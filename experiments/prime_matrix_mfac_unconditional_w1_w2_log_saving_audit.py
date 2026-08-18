"""截断 Möbius--log 系数族的有限形式恒等式工具。

用法示例：
  from experiments.prime_matrix_mfac_unconditional_w1_w2_log_saving_audit import (
      formal_mobius_lambda,
  )
  assert formal_mobius_lambda(6) == {2: Fraction(-1, 1), 3: Fraction(-1, 1)}
"""

from __future__ import annotations

import argparse
from collections.abc import Mapping
from fractions import Fraction
import json
from math import log
from pathlib import Path
import sys

if __package__ in (None, ""):
    # 直接用脚本路径启动时，把仓库根目录加入导入路径。
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from experiments.prime_matrix_mfac_mobius_tail_l2_audit import (
    euler_phi_square_energy_float,
    limit_kernel_energy_float,
    truncated_mobius_log_limit_coefficients,
)
from experiments.prime_matrix_mfac_truncated_mobius_log_coercivity_audit import (
    mobius_value,
)


FORBIDDEN_SOURCES = frozenset(
    {
        "Mertens",
        "PNT",
        "RH",
        "zeta_zero",
        "zero_free_region",
        "explicit_formula",
        "Mellin",
        "Chebyshev_error",
        "target_w1_upper",
    }
)
"""无条件有限义务不得援引的来源名称。"""

ALLOWED_SOURCES = frozenset(
    {
        "finite_dirichlet_convolution",
        "abel_summation_identity",
        "euler_phi_identity",
        "classical_sieve_bound",
    }
)
"""无条件有限义务允许登记的来源名称。"""

DEFAULT_JSON = Path(
    "docs/monograph/prime-matrix-mfac-unconditional-w1-w2-log-saving-audit.json"
)
"""默认 JSON 证书路径。"""

DEFAULT_MARKDOWN = Path(
    "docs/monograph/prime-matrix-mfac-unconditional-w1-w2-log-saving-audit.md"
)
"""默认 Markdown 证书路径。"""


def _require_index(index: object) -> int:
    """验证形式恒等式使用的正内建整数索引。"""
    if type(index) is not int or index < 1:
        raise ValueError("index 必须是至少为 1 的内建整数")
    return index


def _prime_factor_exponents(index: int) -> dict[int, int]:
    """以试除法返回正整数的素因子指数。"""
    remaining = index
    factors: dict[int, int] = {}
    divisor = 2
    while divisor * divisor <= remaining:
        exponent = 0
        while remaining % divisor == 0:
            remaining //= divisor
            exponent += 1
        if exponent:
            factors[divisor] = exponent
        divisor += 1
    if remaining > 1:
        factors[remaining] = 1
    return factors


def formal_negative_mobius_log(index: object) -> dict[int, Fraction]:
    """把 -μ(n) log n 表示为按素数分组的精确有理形式系数。"""
    checked_index = _require_index(index)
    mobius = mobius_value(checked_index)
    if checked_index == 1 or mobius == 0:
        return {}
    return {
        prime: Fraction(-mobius * exponent, 1)
        for prime, exponent in _prime_factor_exponents(checked_index).items()
    }


def formal_mobius_lambda(index: object) -> dict[int, Fraction]:
    """计算 (μ*Λ)(n) 的按素数对数分组的精确形式系数。"""
    checked_index = _require_index(index)
    coefficients: dict[int, Fraction] = {}
    for divisor in range(1, checked_index + 1):
        if checked_index % divisor:
            continue
        mobius = mobius_value(divisor)
        if mobius == 0:
            continue
        quotient_factors = _prime_factor_exponents(checked_index // divisor)
        if len(quotient_factors) != 1:
            continue
        prime = next(iter(quotient_factors))
        coefficients[prime] = coefficients.get(prime, Fraction(0, 1)) + Fraction(
            mobius, 1
        )
    return {
        prime: coefficient
        for prime, coefficient in coefficients.items()
        if coefficient != 0
    }


def _checked_fraction_mapping(
    mapping: Mapping[int, Fraction],
    name: str,
) -> dict[int, Fraction]:
    """验证 Abel 恒等式的一组非空正整数有理数数据。"""
    if not isinstance(mapping, Mapping) or not mapping:
        raise ValueError(f"{name} 必须是非空 Mapping")
    checked: dict[int, Fraction] = {}
    for index, value in mapping.items():
        _require_index(index)
        if not isinstance(value, Fraction):
            raise ValueError(f"{name} 的值必须是 Fraction")
        checked[index] = value
    return checked


def abel_sum_by_parts(
    values: Mapping[int, Fraction],
    weights: Mapping[int, Fraction],
) -> dict[str, Fraction]:
    """精确验证同一有限索引集上的 Abel 分部求和恒等式。"""
    checked_values = _checked_fraction_mapping(values, "values")
    checked_weights = _checked_fraction_mapping(weights, "weights")
    if checked_values.keys() != checked_weights.keys():
        raise ValueError("values 与 weights 必须具有相同的非空索引集")

    ordered_indices = sorted(checked_values)
    direct = sum(
        (
            checked_values[index] * checked_weights[index]
            for index in ordered_indices
        ),
        Fraction(0, 1),
    )
    prefix = Fraction(0, 1)
    summation_by_parts = Fraction(0, 1)
    for position, index in enumerate(ordered_indices):
        prefix += checked_values[index]
        if position + 1 == len(ordered_indices):
            summation_by_parts += prefix * checked_weights[index]
        else:
            next_index = ordered_indices[position + 1]
            summation_by_parts += prefix * (
                checked_weights[index] - checked_weights[next_index]
            )

    return {
        "direct": direct,
        "summation_by_parts": summation_by_parts,
        "residual": direct - summation_by_parts,
    }


def default_contract() -> dict[str, object]:
    """返回只登记有限恒等式且保持开放结论的默认合同。

    用法示例：
      contract = default_contract()
      assert contract["rh_proved"] is False
    """
    return {
        "uses": (
            "finite_dirichlet_convolution",
            "abel_summation_identity",
            "euler_phi_identity",
        ),
        "uniformity_variable": "truncation",
        "constant_dependency": (),
        "w1_l2_upper_status": "open",
        "balanced_remainder_status": "open",
        "rh_proved": False,
    }


def _require_open_status(contract: Mapping[str, object], field: str) -> None:
    """拒绝把尚未解决的义务登记为已证明。"""
    status = contract.get(field)
    if type(status) is not str or status != "open":
        raise ValueError(f"{field} 必须登记为 open，禁止提升为证明")


def audit_unconditional_w1_contract(
    contract: Mapping[str, object],
) -> dict[str, object]:
    """核验无条件 W1 合同仅登记有限来源与开放状态。

    用法示例：
      result = audit_unconditional_w1_contract(default_contract())
      assert result["w1_l2_upper_status"] == "open"
    """
    if not isinstance(contract, Mapping):
        raise ValueError("contract 必须是 Mapping")

    uses = contract.get("uses")
    if type(uses) is not tuple or not uses:
        raise ValueError("uses 必须是非空 tuple")
    checked_uses: list[str] = []
    for source in uses:
        if type(source) is not str:
            raise ValueError("uses 的元素必须是内建 str")
        if source in FORBIDDEN_SOURCES:
            raise ValueError(f"禁止使用来源：{source}")
        if source not in ALLOWED_SOURCES:
            raise ValueError(f"未知来源：{source}")
        checked_uses.append(source)

    uniformity_variable = contract.get("uniformity_variable")
    if type(uniformity_variable) is not str or uniformity_variable != "truncation":
        raise ValueError("uniformity_variable 必须是 truncation")

    constant_dependency = contract.get("constant_dependency")
    if type(constant_dependency) is not tuple or constant_dependency:
        raise ValueError("constant_dependency 必须是空 tuple")

    _require_open_status(contract, "w1_l2_upper_status")
    _require_open_status(contract, "balanced_remainder_status")

    rh_proved = contract.get("rh_proved")
    if type(rh_proved) is not bool or rh_proved is not False:
        raise ValueError("rh_proved 必须是内建 bool False，禁止声称 RH 已证明")

    return {
        "uses": tuple(checked_uses),
        "uniformity_variable": "truncation",
        "constant_dependency": (),
        "w1_l2_upper_status": "open",
        "balanced_remainder_status": "open",
        "rh_proved": False,
    }


def _require_cutoff(cutoff: object) -> int:
    """验证能量诊断使用的截断点。"""
    if type(cutoff) is not int or cutoff < 3:
        raise ValueError("cutoff 必须是至少为 3 的内建整数")
    return cutoff


def audit_log_saving_diagnostic(cutoff: object) -> dict[str, object]:
    """生成有限截断的数值能量诊断，不升级为统一对数节省定理。

    用法示例：
      certificate = audit_log_saving_diagnostic(64)
      assert certificate["w1_l2_upper_status"] == "open"
    """
    checked_cutoff = _require_cutoff(cutoff)
    for index in range(1, checked_cutoff):
        if formal_mobius_lambda(index) != formal_negative_mobius_log(index):
            raise RuntimeError(f"形式 Möbius--Lambda 恒等式在 index={index} 失败")

    coefficients = truncated_mobius_log_limit_coefficients(checked_cutoff)
    direct_energy = limit_kernel_energy_float(coefficients)
    euler_phi_energy = euler_phi_square_energy_float(coefficients)
    mass = sum(value * value / index for index, value in coefficients.items())
    return {
        "certificate_type": "prime_matrix_mfac_unconditional_w1_w2_log_saving_audit",
        "cutoff": checked_cutoff,
        "formal_convolution_status": "verified_finite",
        "actual_log_window_status": "numerical_only",
        "limit_kernel_energy": direct_energy,
        "euler_phi_square_energy": euler_phi_energy,
        "euler_phi_energy_residual": abs(direct_energy - euler_phi_energy),
        "mass": mass,
        "log_scaled_ratio": log(float(checked_cutoff)) * euler_phi_energy / mass,
        "baseline_bound_status": "not_proved",
        "balanced_remainder_status": "open",
        "w1_l2_upper_status": "open",
        "rh_proved": False,
    }


def render_markdown(certificate: Mapping[str, object]) -> str:
    """渲染诊断证书，并明确保留未证明的数学边界。

    用法示例：
      markdown = render_markdown(audit_log_saving_diagnostic(64))
      assert "rh_proved=false" in markdown
    """
    return (
        "# MFAC 无条件 W1 对数节省缺口有限审计\n\n"
        f"- 截断：`D={certificate['cutoff']}`\n"
        f"- 极限核能量：`{certificate['limit_kernel_energy']}`\n"
        f"- Euler--phi 能量：`{certificate['euler_phi_square_energy']}`\n"
        f"- Euler--phi 残差：`{certificate['euler_phi_energy_residual']}`\n"
        f"- 质量：`{certificate['mass']}`\n"
        f"- log 缩放比率：`{certificate['log_scaled_ratio']}`\n\n"
        "```text\n"
        "formal_convolution_status="
        f"{certificate['formal_convolution_status']}\n"
        "actual_log_window_status="
        f"{certificate['actual_log_window_status']}\n"
        "baseline_bound_status="
        f"{certificate['baseline_bound_status']}\n"
        "balanced_remainder_status="
        f"{certificate['balanced_remainder_status']}\n"
        f"w1_l2_upper_status={certificate['w1_l2_upper_status']}\n"
        f"rh_proved={str(certificate['rh_proved']).lower()}\n"
        "```\n\n"
        "该证书仅核验有限形式卷积恒等式并记录固定截断的浮点数值；"
        "不证明统一对数节省、W2 或 RH。\n"
    )


def write_certificate(
    certificate: Mapping[str, object], json_path: Path, markdown_path: Path
) -> None:
    """写出排序 JSON 与 Markdown 证书，并自动创建父目录。

    用法示例：
      certificate = audit_log_saving_diagnostic(64)
      write_certificate(certificate, Path("audit.json"), Path("audit.md"))
    """
    json_path.parent.mkdir(parents=True, exist_ok=True)
    markdown_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(
        json.dumps(certificate, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    markdown_path.write_text(render_markdown(certificate), encoding="utf-8")


def main() -> None:
    """命令行入口：生成无条件 W1 对数节省缺口有限证书。"""
    parser = argparse.ArgumentParser(description="生成 MFAC 无条件 W1 对数节省缺口审计")
    parser.add_argument("--cutoff", type=int, default=4096)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--markdown-out", type=Path, default=DEFAULT_MARKDOWN)
    args = parser.parse_args()

    certificate = audit_log_saving_diagnostic(args.cutoff)
    write_certificate(certificate, args.json_out, args.markdown_out)
    print(f"wrote {args.json_out}")
    print(f"wrote {args.markdown_out}")


if __name__ == "__main__":
    main()
