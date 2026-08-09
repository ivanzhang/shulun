"""MFAC 实际 LCM Gram 核中的有限维去常数强制性审计。

用法示例::

    python3 experiments/prime_matrix_mfac_uniform_offconstant_coercivity_audit.py

本模块只提供有限范围的精确证书，不声称统一谱隙、Mellin 收缩或 RH 证明。
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from fractions import Fraction
from math import atan2, cos, gcd, sin
from pathlib import Path
from typing import Any, Mapping


FORBIDDEN_CANDIDATE_DEPENDENCIES = frozenset(
    {"psi(X)-X", "Chebyshev_error", "Mellin", "zeta_zero", "explicit_formula"}
)


@dataclass(frozen=True)
class Candidate:
    """相对于常数方向 `e_1` 正交化的有限维候选。"""

    limit: int
    index: int
    coefficient: Fraction
    constant_inner_product: Fraction


def lcm_gram_entry(limit: int, left: int, right: int) -> Fraction:
    """返回实际整数 LCM Gram 核的精确条目。"""
    if type(limit) is not int or limit < 2:
        raise ValueError("limit 必须是至少为 2 的内建整数")
    if type(left) is not int or type(right) is not int or left < 1 or right < 1:
        raise ValueError("核索引必须是正的内建整数")
    least_common_multiple = left * right // gcd(left, right)
    return Fraction(limit // least_common_multiple, 1)


def e2_offconstant_candidate(limit: int) -> Candidate:
    """以 `e_2-K_X(1,2)e_1/K_X(1,1)` 构造非循环候选。"""
    kernel_11 = lcm_gram_entry(limit, 1, 1)
    kernel_12 = lcm_gram_entry(limit, 1, 2)
    coefficient = kernel_12 / kernel_11
    return Candidate(
        limit=limit,
        index=2,
        coefficient=coefficient,
        constant_inner_product=kernel_12 - coefficient * kernel_11,
    )


def offconstant_candidate(limit: int, index: int) -> Candidate:
    """将任意固定整数方向 `e_index` 相对常数方向精确正交化。"""
    kernel_11 = lcm_gram_entry(limit, 1, 1)
    kernel_index_1 = lcm_gram_entry(limit, index, 1)
    coefficient = kernel_index_1 / kernel_11
    return Candidate(
        limit=limit,
        index=index,
        coefficient=coefficient,
        constant_inner_product=kernel_index_1 - coefficient * kernel_11,
    )


def candidate_inner_product(left: Candidate, right: Candidate) -> Fraction:
    """计算两个去常数候选在实际 LCM Gram 核下的精确内积。"""
    if left.limit != right.limit:
        raise ValueError("候选必须来自同一个 limit")
    limit = left.limit
    return (
        lcm_gram_entry(limit, left.index, right.index)
        - left.coefficient * lcm_gram_entry(limit, 1, right.index)
        - right.coefficient * lcm_gram_entry(limit, left.index, 1)
        + left.coefficient * right.coefficient * lcm_gram_entry(limit, 1, 1)
    )


def _checked_positive_integer_sequence(values: object, name: str) -> tuple[int, ...]:
    """验证有限扫描的整数参数。"""
    if isinstance(values, (str, bytes)):
        raise ValueError(f"{name} 必须为非字符串可迭代对象")
    try:
        checked = tuple(values)
    except TypeError as error:
        raise ValueError(f"{name} 必须为可迭代对象") from error
    if not checked or any(type(value) is not int or value < 2 for value in checked):
        raise ValueError(f"{name} 必须包含至少一个不小于 2 的内建整数")
    return checked


def _symmetric_min_eigenvalue_estimate(matrix: list[list[Fraction]]) -> float:
    """用 Jacobi 旋转给出有限对称 Gram 矩阵的最小特征值读数。"""
    size = len(matrix)
    values = [[float(entry) for entry in row] for row in matrix]
    if size == 1:
        return values[0][0]
    for _ in range(64 * size * size):
        left, right = max(
            ((row, column) for row in range(size) for column in range(row + 1, size)),
            key=lambda pair: abs(values[pair[0]][pair[1]]),
        )
        off_diagonal = values[left][right]
        if abs(off_diagonal) < 1e-14:
            break
        angle = 0.5 * atan2(2.0 * off_diagonal, values[right][right] - values[left][left])
        cosine, sine = cos(angle), sin(angle)
        for position in range(size):
            if position in (left, right):
                continue
            left_value = values[position][left]
            right_value = values[position][right]
            values[position][left] = values[left][position] = cosine * left_value - sine * right_value
            values[position][right] = values[right][position] = sine * left_value + cosine * right_value
        left_diagonal = values[left][left]
        right_diagonal = values[right][right]
        values[left][left] = cosine**2 * left_diagonal - 2.0 * sine * cosine * off_diagonal + sine**2 * right_diagonal
        values[right][right] = sine**2 * left_diagonal + 2.0 * sine * cosine * off_diagonal + cosine**2 * right_diagonal
        values[left][right] = values[right][left] = 0.0
    return min(values[position][position] for position in range(size))


def audit_finite_family(limits: object, indices: object) -> dict[str, Any]:
    """扫描有限候选族；结果绝不升级为全尺度强制性定理。"""
    checked_limits = _checked_positive_integer_sequence(limits, "limits")
    checked_indices = _checked_positive_integer_sequence(indices, "indices")
    scans: list[dict[str, Any]] = []
    for limit in checked_limits:
        candidates = [offconstant_candidate(limit, index) for index in checked_indices]
        gram = [[candidate_inner_product(left, right) for right in candidates] for left in candidates]
        diagonal = [gram[position][position] for position in range(len(candidates))]
        principal_minors = [
            gram[left][left] * gram[right][right] - gram[left][right] ** 2
            for left in range(len(candidates))
            for right in range(left + 1, len(candidates))
        ]
        gershgorin_lower_bound = min(
            gram[row][row] - sum(abs(gram[row][column]) for column in range(len(candidates)) if column != row)
            for row in range(len(candidates))
        )
        scans.append(
            {
                "limit": limit,
                "indices": list(checked_indices),
                "constant_orthogonality_holds": all(candidate.constant_inner_product == 0 for candidate in candidates),
                "diagonal_energies": [str(value) for value in diagonal],
                "two_by_two_principal_minors": [str(value) for value in principal_minors],
                "gershgorin_lower_bound": str(gershgorin_lower_bound),
                "minimum_eigenvalue_estimate": _symmetric_min_eigenvalue_estimate(gram),
            }
        )
    return {
        "certificate_type": "prime_matrix_mfac_uniform_offconstant_coercivity_audit",
        "status": "finite_coercivity_scan_not_uniform_theorem",
        "parameters": {"limits": list(checked_limits), "indices": list(checked_indices)},
        "scans": scans,
        "uniform_coercivity_proved": False,
        "actual_mellin_contraction_present": False,
        "rh_proved": False,
        "next_positive_gate": "UniformOffConstantCoercivityAndActualChebyshevEnergyBridgeBeforeMellin",
    }


def write_certificate(certificate: Mapping[str, Any], json_path: Path, markdown_path: Path) -> None:
    """写出机器可读证书和人读边界说明。"""
    json_path.parent.mkdir(parents=True, exist_ok=True)
    markdown_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(certificate, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    markdown_path.write_text(
        "# MFAC 有限维去常数强制性审计\n\n"
        "本文件仅扫描明确的有限整数尺度和候选索引。它不证明统一强制性、Mellin 收缩或 RH。\n\n"
        "```text\n"
        "uniform_coercivity_proved=false\n"
        "actual_mellin_contraction_present=false\n"
        "rh_proved=false\n"
        "```\n",
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="生成 MFAC 有限维去常数强制性审计证书")
    parser.add_argument("--limits", nargs="+", type=int, default=[12, 18, 24])
    parser.add_argument("--indices", nargs="+", type=int, default=[2, 3])
    parser.add_argument(
        "--json-out",
        type=Path,
        default=Path("docs/monograph/prime-matrix-mfac-uniform-offconstant-coercivity-audit.json"),
    )
    parser.add_argument(
        "--markdown-out",
        type=Path,
        default=Path("docs/monograph/prime-matrix-mfac-uniform-offconstant-coercivity-audit.md"),
    )
    args = parser.parse_args()
    write_certificate(audit_finite_family(args.limits, args.indices), args.json_out, args.markdown_out)


def audit_candidate_contract(contract: Mapping[str, Any]) -> dict[str, Any]:
    """拒绝任何读取目标误差或 Mellin/零点数据的候选合同。"""
    if not isinstance(contract, Mapping):
        raise ValueError("contract 必须为 Mapping")
    uses = contract.get("uses", ())
    if isinstance(uses, str):
        raise ValueError("uses 必须为非裸字符串的可迭代对象")
    try:
        checked_uses = tuple(uses)
    except TypeError as error:
        raise ValueError("uses 必须为非裸字符串的可迭代对象") from error
    if not all(type(value) is str for value in checked_uses):
        raise ValueError("uses 的所有元素必须为内建 str")
    forbidden = tuple(value for value in checked_uses if value in FORBIDDEN_CANDIDATE_DEPENDENCIES)
    return {
        "status": "forbidden_target_dependency" if forbidden else "independent_candidate_contract",
        "forbidden_dependencies": forbidden,
        "uses_target_error": "psi(X)-X" in forbidden or "Chebyshev_error" in forbidden,
        "uses_mellin_or_zero_input": any(
            value in {"Mellin", "zeta_zero", "explicit_formula"} for value in forbidden
        ),
    }


if __name__ == "__main__":
    main()
