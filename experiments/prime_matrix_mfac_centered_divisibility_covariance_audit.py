"""MFAC 中心化整除协方差的有限谱审计。

用法示例::

    python3 experiments/prime_matrix_mfac_centered_divisibility_covariance_audit.py \
        --limit 4096 --theta 0.25

所有输出均为有限尺度诊断，不构成统一强制性、Mellin 收缩或 RH 证明。
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from math import atan2, cos, floor, gcd, isfinite, sin, sqrt
from pathlib import Path
from typing import Any, Mapping


def _require_limit(limit: object) -> int:
    """验证有限整数区间上界。"""
    if type(limit) is not int or limit < 2:
        raise ValueError("limit 必须是至少为 2 的内建整数")
    return limit


def _require_index(index: object, limit: int) -> int:
    """验证参与协方差的整除索引。"""
    if type(index) is not int or not 2 <= index <= limit:
        raise ValueError("索引必须是位于 [2, limit] 的内建整数")
    return index


def _checked_coefficients(limit: int, coefficients: Mapping[int, Fraction]) -> dict[int, Fraction]:
    """验证并规范化非空的精确系数字典。"""
    if not isinstance(coefficients, Mapping) or not coefficients:
        raise ValueError("coefficients 必须为非空 Mapping")
    checked: dict[int, Fraction] = {}
    for index, value in coefficients.items():
        checked_index = _require_index(index, limit)
        if not isinstance(value, Fraction):
            raise ValueError("系数必须为 Fraction")
        checked[checked_index] = value
    return checked


def centered_covariance_entry(limit: int, left: int, right: int) -> Fraction:
    """返回中心化整除特征的精确协方差核条目。"""
    checked_limit = _require_limit(limit)
    checked_left = _require_index(left, checked_limit)
    checked_right = _require_index(right, checked_limit)
    left_count = checked_limit // checked_left
    right_count = checked_limit // checked_right
    overlap = checked_limit // (checked_left * checked_right // gcd(checked_left, checked_right))
    return Fraction(overlap, 1) - Fraction(left_count * right_count, checked_limit)


def covariance_quadratic_form(limit: int, coefficients: Mapping[int, Fraction]) -> Fraction:
    """计算精确中心化协方差二次型。"""
    checked_limit = _require_limit(limit)
    checked = _checked_coefficients(checked_limit, coefficients)
    return sum(
        left_value * right_value * centered_covariance_entry(checked_limit, left_index, right_index)
        for left_index, left_value in checked.items()
        for right_index, right_value in checked.items()
    )


def centered_divisibility_variance(limit: int, coefficients: Mapping[int, Fraction]) -> Fraction:
    """按整数点直接求和，以核对中心化方差恒等式。"""
    checked_limit = _require_limit(limit)
    checked = _checked_coefficients(checked_limit, coefficients)
    mean = Fraction(
        sum(value * (checked_limit // index) for index, value in checked.items()),
        checked_limit,
    )
    return sum(
        (sum(value for index, value in checked.items() if number % index == 0) - mean) ** 2
        for number in range(1, checked_limit + 1)
    )


def _require_cutoff(limit: int, cutoff: object) -> int:
    """验证中心化核的最大索引。"""
    if type(cutoff) is not int or not 2 <= cutoff <= limit:
        raise ValueError("cutoff 必须是位于 [2, limit] 的内建整数")
    return cutoff


def _symmetric_jacobi_eigendecomposition(
    matrix: list[list[float]],
) -> tuple[list[float], list[list[float]], float]:
    """分解有限实对称矩阵，并返回最大本征残差。"""
    size = len(matrix)
    if size == 0 or any(len(row) != size for row in matrix):
        raise ValueError("matrix 必须为非空方阵")
    values = [row[:] for row in matrix]
    vectors = [[1.0 if row == column else 0.0 for column in range(size)] for row in range(size)]
    for _ in range(128 * size * size):
        left, right = max(
            ((row, column) for row in range(size) for column in range(row + 1, size)),
            key=lambda pair: abs(values[pair[0]][pair[1]]),
            default=(0, 0),
        )
        if size == 1 or abs(values[left][right]) <= 1e-12:
            break
        off_diagonal = values[left][right]
        angle = 0.5 * atan2(
            2.0 * off_diagonal,
            values[right][right] - values[left][left],
        )
        cosine, sine = cos(angle), sin(angle)
        left_diagonal = values[left][left]
        right_diagonal = values[right][right]
        for position in range(size):
            if position in (left, right):
                continue
            left_value = values[position][left]
            right_value = values[position][right]
            values[position][left] = values[left][position] = cosine * left_value - sine * right_value
            values[position][right] = values[right][position] = sine * left_value + cosine * right_value
        values[left][left] = (
            cosine**2 * left_diagonal
            - 2.0 * sine * cosine * off_diagonal
            + sine**2 * right_diagonal
        )
        values[right][right] = (
            sine**2 * left_diagonal
            + 2.0 * sine * cosine * off_diagonal
            + cosine**2 * right_diagonal
        )
        values[left][right] = values[right][left] = 0.0
        for position in range(size):
            left_value = vectors[position][left]
            right_value = vectors[position][right]
            vectors[position][left] = cosine * left_value - sine * right_value
            vectors[position][right] = sine * left_value + cosine * right_value
    else:
        raise RuntimeError("Jacobi 迭代未在规定步数内收敛")
    eigenvalues = [values[position][position] for position in range(size)]
    order = sorted(range(size), key=eigenvalues.__getitem__)
    ordered_values = [eigenvalues[position] for position in order]
    ordered_vectors = [[vectors[row][position] for row in range(size)] for position in order]
    residual = max(
        abs(
            sum(matrix[row][column] * vector[column] for column in range(size))
            - eigenvalue * vector[row]
        )
        for eigenvalue, vector in zip(ordered_values, ordered_vectors)
        for row in range(size)
    )
    return ordered_values, ordered_vectors, residual


def weighted_coercivity_profile(limit: int, cutoff: int) -> dict[str, Any]:
    """给出有限中心化协方差的加权最小强制比读数。"""
    checked_limit = _require_limit(limit)
    checked_cutoff = _require_cutoff(checked_limit, cutoff)
    indices = list(range(2, checked_cutoff + 1))
    covariance = [
        [centered_covariance_entry(checked_limit, left, right) for right in indices]
        for left in indices
    ]
    normalized = [
        [
            sqrt(left * right) * float(covariance[row][column]) / checked_limit
            for column, right in enumerate(indices)
        ]
        for row, left in enumerate(indices)
    ]
    eigenvalues, eigenvectors, residual = _symmetric_jacobi_eigendecomposition(normalized)
    minimum_vector = eigenvectors[0]
    support = sorted(
        (
            {"index": index, "coefficient_estimate": sqrt(index / checked_limit) * value}
            for index, value in zip(indices, minimum_vector)
        ),
        key=lambda item: abs(item["coefficient_estimate"]),
        reverse=True,
    )[:3]
    return {
        "status": "finite_profile_only",
        "limit": checked_limit,
        "cutoff": checked_cutoff,
        "indices": indices,
        "minimum_ratio_estimate": eigenvalues[0],
        "maximum_eigen_residual": residual,
        "covariance_diagonal_exact": [str(covariance[position][position]) for position in range(len(indices))],
        "near_degenerate_support": support,
        "uniform_weighted_coercivity_proved": False,
    }


def cutoff_from_theta(limit: int, theta: float) -> int:
    """将有限尺度指数转为审计索引上界。"""
    checked_limit = _require_limit(limit)
    if type(theta) not in (int, float) or isinstance(theta, bool) or not isfinite(theta):
        raise ValueError("theta 必须是有限数值")
    if not 0.0 < theta < 1.0:
        raise ValueError("theta 必须严格位于 0 与 1 之间")
    return max(2, min(checked_limit, floor(checked_limit**theta)))


def compare_dyadic_profiles(limit: int, theta: float) -> dict[str, Any]:
    """比较相邻 dyadic 尺度的有限谱剖面，禁止外推为统一定理。"""
    checked_limit = _require_limit(limit)
    current = weighted_coercivity_profile(
        checked_limit,
        cutoff_from_theta(checked_limit, theta),
    )
    following_limit = 2 * checked_limit
    following = weighted_coercivity_profile(
        following_limit,
        cutoff_from_theta(following_limit, theta),
    )
    return {
        "status": "finite_dyadic_diagnostic_only",
        "theta": theta,
        "current": current,
        "next": following,
        "minimum_ratio_change": following["minimum_ratio_estimate"] - current["minimum_ratio_estimate"],
        "uniform_weighted_coercivity_proved": False,
        "actual_mellin_contraction_present": False,
        "rh_proved": False,
    }


def audit_centered_divisibility_covariance(limit: int, theta: float) -> dict[str, Any]:
    """生成中心化整除协方差的有限谱证书数据。"""
    checked_limit = _require_limit(limit)
    cutoff = cutoff_from_theta(checked_limit, theta)
    return {
        "certificate_type": "prime_matrix_mfac_centered_divisibility_covariance_audit",
        "status": "finite_covariance_profile_not_uniform_theorem",
        "parameters": {"limit": checked_limit, "theta": theta, "cutoff": cutoff},
        "profile": weighted_coercivity_profile(checked_limit, cutoff),
        "dyadic_diagnostic": compare_dyadic_profiles(checked_limit, theta),
        "finite_covariance_identity_available": True,
        "uniform_weighted_coercivity_proved": False,
        "actual_chebyshev_energy_bridge_proved": False,
        "actual_mellin_contraction_present": False,
        "rh_proved": False,
        "next_positive_gate": "UniformCenteredDivisibilityCoercivityAndNoncircularChebyshevEnergyBridge",
    }


def write_certificate(certificate: Mapping[str, Any], json_path: Path, markdown_path: Path) -> None:
    """写出机器证书和人读边界说明。"""
    json_path = Path(json_path)
    markdown_path = Path(markdown_path)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    markdown_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(
        json.dumps(certificate, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    profile = certificate["profile"]
    markdown_path.write_text(
        "# MFAC 中心化整除协方差有限谱审计\n\n"
        "对 `2 <= d,e <= D`，本审计使用精确核\n\n"
        "\\[C_X(d,e)=\\lfloor X/[d,e]\\rfloor-"
        "\\lfloor X/d\\rfloor\\lfloor X/e\\rfloor/X.\\]\n\n"
        "其二次型等于中心化整除总负载的有限平方和。\n\n"
        f"- 参数：`X={certificate['parameters']['limit']}`，`D={profile['cutoff']}`，"
        f"`theta={certificate['parameters']['theta']}`\n"
        f"- 有限加权最小强制比读数：`{profile['minimum_ratio_estimate']}`\n"
        f"- 最大特征残差：`{profile['maximum_eigen_residual']}`\n"
        f"- 近退化支持：`{profile['near_degenerate_support']}`\n\n"
        "```text\n"
        "uniform_weighted_coercivity_proved=false\n"
        "actual_chebyshev_energy_bridge_proved=false\n"
        "actual_mellin_contraction_present=false\n"
        "rh_proved=false\n"
        "```\n\n"
        "有限谱读数不构成跨尺度统一强制性。即使未来得到该强制性，仍须独立建立非循环的 "
        "Chebyshev 能量桥接和 dyadic 到 Mellin 的可和性；本证书**不构成 RH 证明**。\n",
        encoding="utf-8",
    )


def main() -> None:
    """解析 CLI 参数并写出默认有限证书。"""
    parser = argparse.ArgumentParser(description="生成 MFAC 中心化整除协方差有限谱证书")
    parser.add_argument("--limit", type=int, default=4096)
    parser.add_argument("--theta", type=float, default=0.25)
    parser.add_argument(
        "--json-out",
        type=Path,
        default=Path("docs/monograph/prime-matrix-mfac-centered-divisibility-covariance-audit.json"),
    )
    parser.add_argument(
        "--markdown-out",
        type=Path,
        default=Path("docs/monograph/prime-matrix-mfac-centered-divisibility-covariance-audit.md"),
    )
    args = parser.parse_args()
    write_certificate(
        audit_centered_divisibility_covariance(args.limit, args.theta),
        args.json_out,
        args.markdown_out,
    )


if __name__ == "__main__":
    main()
