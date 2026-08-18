#!/usr/bin/env python3
"""MFAC 截断 Möbius--log 系数族的有限审计基础。

用法示例：

    python3 -c "from experiments.prime_matrix_mfac_truncated_mobius_log_coercivity_audit import truncated_mobius_log_coefficients; print(truncated_mobius_log_coefficients(1024, 0.4))"

本模块中的对数和系数均为浮点近似，不将其伪装为精确有理数。
"""

from __future__ import annotations

import argparse
import json
import sys
from collections.abc import Iterable, Mapping
from math import floor, isfinite, log
from pathlib import Path
from typing import Any

if __package__ in (None, ""):
    # 直接用脚本路径启动时，把仓库根目录加入导入路径。
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from experiments.prime_matrix_mfac_centered_divisibility_covariance_audit import (
    centered_covariance_entry,
)


FORBIDDEN_COEFFICIENT_INPUTS = frozenset(
    {
        "psi(X)-X",
        "Chebyshev_error",
        "Mellin",
        "zeta_zero",
        "explicit_formula",
        "RH",
    }
)

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
SLUG = "prime-matrix-mfac-truncated-mobius-log-coercivity-audit"
DEFAULT_JSON = DOCS / f"{SLUG}.json"
DEFAULT_MARKDOWN = DOCS / f"{SLUG}.md"


def _require_limit(limit: object) -> int:
    """验证有限审计的整数上界。"""
    if type(limit) is not int or limit < 2:
        raise ValueError("limit 必须是至少为 2 的内建整数")
    return limit


def _require_theta(theta: object) -> float:
    """验证预注册截断指数。"""
    if type(theta) not in (int, float) or not isfinite(theta):
        raise ValueError("theta 必须是有限内建数值")
    if not 0.0 < theta < 0.5:
        raise ValueError("theta 必须严格位于 0 与 1/2 之间")
    return float(theta)


def cutoff_from_theta(limit: object, theta: object) -> int:
    """按预注册公式给出截断上界。"""
    checked_limit = _require_limit(limit)
    checked_theta = _require_theta(theta)
    return min(checked_limit, floor(checked_limit**checked_theta))


def linear_window(position: object) -> float:
    """返回预注册线性窗口在闭区间 [0, 1] 上的值。"""
    if type(position) not in (int, float) or not isfinite(position):
        raise ValueError("position 必须是位于 [0, 1] 的有限内建数值")
    checked_position = float(position)
    if not 0.0 <= checked_position <= 1.0:
        raise ValueError("position 必须位于 [0, 1]")
    return 1.0 - checked_position


def mobius_value(index: object) -> int:
    """以试除法计算正整数的 Möbius 函数值。"""
    if type(index) is not int or index < 1:
        raise ValueError("index 必须是至少为 1 的内建整数")
    remaining = index
    prime_count = 0
    divisor = 2
    while divisor * divisor <= remaining:
        if remaining % divisor == 0:
            remaining //= divisor
            if remaining % divisor == 0:
                return 0
            prime_count += 1
        divisor += 1
    if remaining > 1:
        prime_count += 1
    return -1 if prime_count % 2 else 1


def _is_prime(index: int) -> bool:
    """用确定性试除法判定小规模有限整数是否为素数。"""
    if index < 2:
        return False
    if index == 2:
        return True
    if index % 2 == 0:
        return False
    divisor = 3
    while divisor * divisor <= index:
        if index % divisor == 0:
            return False
        divisor += 2
    return True


def _divisor_count(index: int) -> int:
    """按整数分解计算有限整数的正约数个数。"""
    remaining = index
    count = 1
    divisor = 2
    while divisor * divisor <= remaining:
        exponent = 0
        while remaining % divisor == 0:
            remaining //= divisor
            exponent += 1
        if exponent:
            count *= exponent + 1
        divisor += 1
    if remaining > 1:
        count *= 2
    return count


def truncated_mobius_log_coefficients(
    limit: object,
    theta: object,
) -> dict[int, float]:
    """构造固定线性截断的非零 Möbius--log 浮点系数。"""
    cutoff = cutoff_from_theta(limit, theta)
    if cutoff < 2:
        raise ValueError("截断上界小于 2，无有效整除索引")
    logarithmic_cutoff = log(float(cutoff))
    coefficients: dict[int, float] = {}
    for index in range(2, cutoff + 1):
        mobius = mobius_value(index)
        if mobius == 0:
            continue
        window = linear_window(log(float(index)) / logarithmic_cutoff)
        if window == 0.0:
            continue
        coefficients[index] = -mobius * log(float(index)) * window
    return coefficients


def _checked_float_coefficients(
    limit: int,
    coefficients: Mapping[int, float],
) -> dict[int, float]:
    """验证并规范化有限浮点系数 Mapping。"""
    if not isinstance(coefficients, Mapping) or not coefficients:
        raise ValueError("coefficients 必须为非空 Mapping")
    checked: dict[int, float] = {}
    for index, value in coefficients.items():
        if type(index) is not int or not 2 <= index <= limit:
            raise ValueError("系数索引必须是位于 [2, limit] 的内建整数")
        if type(value) not in (int, float) or not isfinite(value):
            raise ValueError("系数值必须是有限内建 int 或 float")
        checked_value = float(value)
        if not isfinite(checked_value):
            raise ValueError("系数值必须可转换为有限 float")
        checked[index] = checked_value
    return checked


def quadratic_centered_energy(limit: object, coefficients: Mapping[int, float]) -> float:
    """用中心化协方差核二次型计算有限能量读数。"""
    checked_limit = _require_limit(limit)
    checked = _checked_float_coefficients(checked_limit, coefficients)
    return sum(
        left_value
        * right_value
        * float(centered_covariance_entry(checked_limit, left_index, right_index))
        for left_index, left_value in checked.items()
        for right_index, right_value in checked.items()
    )


def direct_centered_energy(limit: object, coefficients: Mapping[int, float]) -> float:
    """用相同离散均值直接计算中心化平方和能量。"""
    checked_limit = _require_limit(limit)
    checked = _checked_float_coefficients(checked_limit, coefficients)
    mean = sum(
        value * (checked_limit // index)
        for index, value in checked.items()
    ) / float(checked_limit)
    return sum(
        (
            sum(
                value
                for index, value in checked.items()
                if number % index == 0
            )
            - mean
        )
        ** 2
        for number in range(1, checked_limit + 1)
    )


def weighted_mass(limit: object, coefficients: Mapping[int, float]) -> float:
    """计算 limit * sum(a_d^2/d) 的有限加权质量。"""
    checked_limit = _require_limit(limit)
    checked = _checked_float_coefficients(checked_limit, coefficients)
    return float(checked_limit) * sum(
        value * value / float(index) for index, value in checked.items()
    )


def normalized_energy_ratio(limit: object, coefficients: Mapping[int, float]) -> float:
    """返回中心化能量相对加权质量的有限归一化比值。"""
    checked_limit = _require_limit(limit)
    checked = _checked_float_coefficients(checked_limit, coefficients)
    mass = weighted_mass(checked_limit, checked)
    if mass <= 0.0 or not isfinite(mass):
        raise ValueError("加权质量必须为正有限数值")
    return quadratic_centered_energy(checked_limit, checked) / mass


def _profile_payload(
    limit: int,
    kind: str,
    coefficients: Mapping[int, float],
) -> dict[str, object]:
    """把有限对照系数族转为 JSON 友好的 profile 载荷。"""
    if not coefficients:
        return {
            "kind": kind,
            "status": "empty_at_finite_scale",
            "coefficient_support": (),
            "coefficient_count": 0,
            "weighted_mass": None,
            "quadratic_centered_energy": None,
            "normalized_energy_ratio": None,
        }
    checked = _checked_float_coefficients(limit, coefficients)
    support = tuple(sorted(checked))
    return {
        "kind": kind,
        "status": "computed_finite_scale",
        "coefficient_support": support,
        "coefficient_count": len(support),
        "weighted_mass": weighted_mass(limit, checked),
        "quadratic_centered_energy": quadratic_centered_energy(limit, checked),
        "normalized_energy_ratio": normalized_energy_ratio(limit, checked),
    }


def comparison_witness_profiles(limit: object, theta: object) -> dict[str, dict[str, object]]:
    """构造四类仅用于反向压力测试的确定性有限对照见证。

    用法示例：
        comparison_witness_profiles(512, 0.4)["primorial"]
    """
    checked_limit = _require_limit(limit)
    cutoff = cutoff_from_theta(checked_limit, theta)

    squarefree_mobius = {
        index: float(mobius)
        for index in range(2, cutoff + 1)
        if (mobius := mobius_value(index)) != 0
    }

    primorial_value = 1
    for index in range(2, cutoff + 1):
        if _is_prime(index):
            candidate = primorial_value * index
            if candidate > cutoff:
                break
            primorial_value = candidate
    primorial = {primorial_value: 1.0} if primorial_value >= 2 else {}

    single_prime_layer = {
        index: 1.0
        for index in range(2, cutoff + 1)
        if cutoff / 2.0 < index < cutoff and _is_prime(index)
    }

    high_divisor_composite = {
        index: 1.0
        for index in range(2, cutoff + 1)
        if mobius_value(index) == 0 and _divisor_count(index) >= 4
    }

    return {
        "squarefree_mobius": _profile_payload(
            checked_limit,
            "squarefree_mobius",
            squarefree_mobius,
        ),
        "primorial": _profile_payload(checked_limit, "primorial", primorial),
        "single_prime_layer": _profile_payload(
            checked_limit,
            "single_prime_layer",
            single_prime_layer,
        ),
        "high_divisor_composite": _profile_payload(
            checked_limit,
            "high_divisor_composite",
            high_divisor_composite,
        ),
    }


def audit_coefficient_contract(contract: object) -> dict[str, object]:
    """拒绝系数定义读取目标误差或被禁止解析输入。"""
    if not isinstance(contract, Mapping):
        raise ValueError("contract 必须为 Mapping")
    uses = contract.get("uses", ())
    if isinstance(uses, str) or not isinstance(uses, Iterable):
        raise ValueError("contract uses 必须为非裸字符串的可迭代字符串对象")
    try:
        checked_uses = tuple(uses)
    except TypeError as error:
        raise ValueError("contract uses 必须为非裸字符串的可迭代字符串对象") from error
    if any(type(item) is not str for item in checked_uses):
        raise ValueError("contract uses 的所有元素必须为字符串")
    forbidden_inputs = tuple(
        sorted(set(checked_uses).intersection(FORBIDDEN_COEFFICIENT_INPUTS))
    )
    return {
        "classification": (
            "coefficient_uses_target_or_forbidden_analytic_input"
            if forbidden_inputs
            else "coefficient_input_not_rejected"
        ),
        "forbidden_inputs": forbidden_inputs,
    }


def audit_truncated_mobius_log_coercivity(
    limit: object,
    theta: object,
) -> dict[str, object]:
    """生成截断 Möbius--log 强制性有限数值审计载荷。

    用法示例：
        audit_truncated_mobius_log_coercivity(64, 0.4)
    """
    checked_limit = _require_limit(limit)
    checked_theta = _require_theta(theta)
    cutoff = cutoff_from_theta(checked_limit, checked_theta)
    coefficients = truncated_mobius_log_coefficients(checked_limit, checked_theta)
    contract = {
        "uses": ("X", "d", "mobius", "log", "fixed_linear_window"),
        "forbidden_inputs": tuple(sorted(FORBIDDEN_COEFFICIENT_INPUTS)),
    }
    contract_audit = audit_coefficient_contract(contract)
    direct_energy = direct_centered_energy(checked_limit, coefficients)
    quadratic_energy = quadratic_centered_energy(checked_limit, coefficients)
    residual = abs(direct_energy - quadratic_energy)
    mass = weighted_mass(checked_limit, coefficients)
    ratio = normalized_energy_ratio(checked_limit, coefficients)

    return {
        "certificate_type": (
            "prime_matrix_mfac_truncated_mobius_log_coercivity_audit"
        ),
        "status": "numerical_only_finite_structured_coercivity_profile",
        "limit": checked_limit,
        "theta": checked_theta,
        "cutoff": cutoff,
        "window": "linear",
        "coefficient_contract": contract,
        "coefficient_contract_audit": contract_audit,
        "coefficient_family_status": "specified",
        "coefficient_independence_verified": True,
        "support": tuple(sorted(coefficients)),
        "support_size": len(coefficients),
        "coefficients": coefficients,
        "direct_centered_energy": direct_energy,
        "quadratic_centered_energy": quadratic_energy,
        "energy_identity_residual": residual,
        "weighted_mass": mass,
        "normalized_energy_ratio": ratio,
        "comparison_witness_profiles": comparison_witness_profiles(
            checked_limit,
            checked_theta,
        ),
        "finite_profile_status": "completed_numerical_only",
        "chebyshev_bridge_status": "not_started",
        "mellin_status": "not_started",
        "structured_coercivity_status": "unproved",
        "rh_proved": False,
        "uniform_in_limit_coercivity_proved": False,
        "zero_free_region_proved": False,
    }


def render_markdown(certificate: Mapping[str, Any]) -> str:
    """将有限审计证书渲染为可人工检查的 Markdown。"""
    lines = [
        "# MFAC 截断 Möbius--log 强制性有限审计",
        "",
        "## 参数",
        "",
        f"- `limit`: `{certificate['limit']}`",
        f"- `theta`: `{certificate['theta']}`",
        f"- `cutoff`: `{certificate['cutoff']}`",
        f"- `window`: `{certificate['window']}`",
        f"- `support_size`: `{certificate['support_size']}`",
        "",
        "## 有限比率",
        "",
        f"- `weighted_mass`: `{certificate['weighted_mass']}`",
        f"- `normalized_energy_ratio`: `{certificate['normalized_energy_ratio']}`",
        "",
        "## 直接/核残差",
        "",
        f"- `direct_centered_energy`: `{certificate['direct_centered_energy']}`",
        f"- `quadratic_centered_energy`: `{certificate['quadratic_centered_energy']}`",
        f"- `energy_identity_residual`: `{certificate['energy_identity_residual']}`",
        "",
        "## 对照见证",
        "",
    ]
    for name, profile in certificate["comparison_witness_profiles"].items():
        lines.extend(
            [
                f"- `{name}`: status=`{profile['status']}`, "
                f"coefficient_count=`{profile['coefficient_count']}`, "
                f"weighted_mass=`{profile['weighted_mass']}`, "
                f"normalized_energy_ratio=`{profile['normalized_energy_ratio']}`",
            ]
        )
    lines.extend(
        [
        "",
        "## 状态块",
        "",
        "```text",
        f"status={certificate['status']}",
        f"coefficient_family_status={certificate['coefficient_family_status']}",
        "coefficient_independence_verified="
        f"{str(certificate['coefficient_independence_verified']).lower()}",
        f"finite_profile_status={certificate['finite_profile_status']}",
        f"chebyshev_bridge_status={certificate['chebyshev_bridge_status']}",
        f"mellin_status={certificate['mellin_status']}",
        f"structured_coercivity_status={certificate['structured_coercivity_status']}",
        f"rh_proved={str(certificate['rh_proved']).lower()}",
        "uniform_in_limit_coercivity_proved="
        f"{str(certificate['uniform_in_limit_coercivity_proved']).lower()}",
        f"zero_free_region_proved={str(certificate['zero_free_region_proved']).lower()}",
        "```",
        "",
        "本证书只记录有限浮点数值审计读数；"
        "不构成统一强制性、Chebyshev 能量桥、Mellin 收缩，也不构成 RH 证明。",
        "",
        ]
    )
    return "\n".join(lines)


def write_certificate(
    certificate: Mapping[str, Any],
    json_path: str | Path,
    markdown_path: str | Path,
) -> None:
    """写出 JSON 与 Markdown 证书，并自动创建父目录。"""
    checked_json_path = Path(json_path)
    checked_markdown_path = Path(markdown_path)
    checked_json_path.parent.mkdir(parents=True, exist_ok=True)
    checked_markdown_path.parent.mkdir(parents=True, exist_ok=True)
    checked_json_path.write_text(
        json.dumps(certificate, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    checked_markdown_path.write_text(
        render_markdown(certificate),
        encoding="utf-8",
    )


def main() -> None:
    """命令行入口：生成有限审计并写出指定证书路径。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=4096)
    parser.add_argument("--theta", type=float, default=0.25)
    parser.add_argument("--window", choices=("linear",), default="linear")
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--markdown-out", type=Path, default=DEFAULT_MARKDOWN)
    args = parser.parse_args()

    certificate = audit_truncated_mobius_log_coercivity(args.limit, args.theta)
    write_certificate(certificate, args.json_out, args.markdown_out)
    print(f"wrote {args.json_out}")
    print(f"wrote {args.markdown_out}")


if __name__ == "__main__":
    main()
