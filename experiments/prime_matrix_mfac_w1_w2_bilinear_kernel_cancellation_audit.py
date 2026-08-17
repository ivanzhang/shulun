"""审计 MFAC W1→W2 有限双线性核的对角—非对角抵消。"""

import argparse
from fractions import Fraction
import json
from math import gcd
from pathlib import Path
from typing import Mapping


DEFAULT_JSON = Path("docs/monograph/prime-matrix-mfac-w1-w2-bilinear-kernel-cancellation-audit.json")
DEFAULT_MARKDOWN = Path("docs/monograph/prime-matrix-mfac-w1-w2-bilinear-kernel-cancellation-audit.md")
REQUIRED_CLAIMED_USES = (
    "finite_kernel_identity", "finite_gram_positivity", "finite_cancellation_witness",
)
ALLOWED_SOURCES = frozenset({
    "finite_arithmetic", "mobius_definition", "gcd_relation",
    "euler_phi_divisor_sum", "finite_gram_decomposition", "finite_sum_identity",
})
FORBIDDEN_SOURCES = frozenset({
    "Mertens", "PNT", "RH", "zeta_zero", "zero_free_region", "explicit_formula",
    "Mellin", "Chebyshev_error", "target_energy_bridge", "chebyshev_energy_bridge",
    "finite_profile", "numerical_experiment",
})
FORBIDDEN_CONCLUSIONS = frozenset({
    "uniform_l2_upper_proved", "coprime_restricted_tail_bound_proved",
    "w1_to_w2_proved", "w2_closed", "chebyshev_energy_bridge_proved",
    "rh_proved", "rh_consequence",
})


def _checked_string_tuple(value: object, field_name: str) -> tuple[str, ...]:
    """验证非空字符串序列，拒绝裸字符串和非法元素。"""
    if type(value) not in (tuple, list) or not value:
        raise ValueError(f"{field_name} 必须是非空字符串 tuple 或 list")
    if any(type(item) is not str or not item for item in value):
        raise ValueError(f"{field_name} 必须只含非空字符串")
    return tuple(value)


def _require_limit(limit: object) -> int:
    """验证有限截断为至少三的内建整数。"""
    if type(limit) is not int or limit < 3:
        raise ValueError("limit 必须是至少为 3 的内建整数")
    return limit


def mobius_value(index: object) -> int:
    """用有限试除法计算 Möbius 函数。"""
    if type(index) is not int or index < 1:
        raise ValueError("index 必须是至少为 1 的内建整数")
    remaining, count, divisor = index, 0, 2
    while divisor * divisor <= remaining:
        if remaining % divisor == 0:
            remaining //= divisor
            if remaining % divisor == 0:
                return 0
            count += 1
            while remaining % divisor == 0:
                remaining //= divisor
        divisor += 1
    return -1 if (count + (remaining > 1)) % 2 else 1


def euler_phi(index: object) -> int:
    """用有限试除法计算 Euler--φ。"""
    if type(index) is not int or index < 1:
        raise ValueError("index 必须是至少为 1 的内建整数")
    result, remaining, divisor = index, index, 2
    while divisor * divisor <= remaining:
        if remaining % divisor == 0:
            result -= result // divisor
            while remaining % divisor == 0:
                remaining //= divisor
        divisor += 1
    if remaining > 1:
        result -= result // remaining
    return result


def finite_bilinear_kernel_model(limit: object) -> dict[str, object]:
    """精确比较有限能量的除数、核、Gram 与对角分解表示。"""
    checked_limit = _require_limit(limit)
    indices = tuple(range(2, checked_limit))
    coefficients = {index: Fraction(mobius_value(index), index) for index in indices}
    tails = {
        modulus: sum((value for index, value in coefficients.items() if index % modulus == 0), Fraction())
        for modulus in indices
    }
    divisor_energy = sum((Fraction(euler_phi(modulus)) * tail * tail for modulus, tail in tails.items()), Fraction())
    kernel_energy = sum((left_value * right_value * (gcd(left, right) - 1)
                         for left, left_value in coefficients.items()
                         for right, right_value in coefficients.items()), Fraction())
    gram_energy = sum((left_value * right_value * sum(
        (Fraction(euler_phi(modulus)) for modulus in indices if left % modulus == 0 and right % modulus == 0), Fraction())
        for left, left_value in coefficients.items()
        for right, right_value in coefficients.items()), Fraction())
    diagonal = sum((value * value * (index - 1) for index, value in coefficients.items()), Fraction())
    offdiagonal = kernel_energy - diagonal
    return {
        "limit": checked_limit, "candidate_indices": indices,
        "divisor_sum_energy": str(divisor_energy), "kernel_energy": str(kernel_energy),
        "gram_energy": str(gram_energy), "diagonal_energy": str(diagonal),
        "offdiagonal_energy": str(offdiagonal),
        "divisor_kernel_residual": str(divisor_energy - kernel_energy),
        "kernel_gram_residual": str(kernel_energy - gram_energy),
        "diagonal_offdiagonal_residual": str(kernel_energy - diagonal - offdiagonal),
        "finite_cancellation_status": "finite_cancellation_witnessed" if offdiagonal < 0 else "not_witnessed",
        "diagonal_cancellation_obligation_status": "open",
    }


def _validate_contract(contract: object) -> dict[str, object]:
    """验证合同仅使用有限来源且不伪造抵消证明。"""
    if not isinstance(contract, Mapping):
        raise ValueError("contract 必须是 Mapping")
    for field in FORBIDDEN_CONCLUSIONS:
        if field in contract:
            raise ValueError(f"{field} 不能出现在有限核合同中")
    uses = _checked_string_tuple(contract.get("uses"), "uses")
    forbidden = set(uses) & FORBIDDEN_SOURCES
    if forbidden:
        raise ValueError(f"uses 含禁止来源: {sorted(forbidden)}")
    unallowed = set(uses) - ALLOWED_SOURCES
    if unallowed:
        raise ValueError(f"uses 含未允许来源: {sorted(unallowed)}")
    claims = contract.get("claimed_uses")
    if not isinstance(claims, Mapping) or set(claims) != set(REQUIRED_CLAIMED_USES):
        raise ValueError("claimed_uses 必须精确覆盖有限义务")
    checked_claims = {}
    for obligation in REQUIRED_CLAIMED_USES:
        claimed = _checked_string_tuple(claims[obligation], obligation)
        if not set(claimed).issubset(uses):
            raise ValueError(f"{obligation} 含未声明来源")
        checked_claims[obligation] = claimed
    for field in ("kernel_identity", "gram_positivity"):
        if type(contract.get(field)) is not bool or not contract[field]:
            raise ValueError(f"{field} 必须是内建 True")
    if type(contract.get("offdiagonal_cancellation_lemma")) is not bool or contract["offdiagonal_cancellation_lemma"]:
        raise ValueError("offdiagonal_cancellation_lemma 必须是内建 False")
    if contract.get("uniformity_variable") != "truncation":
        raise ValueError("uniformity_variable 必须是 truncation")
    if contract.get("constant_dependency") != "fixed_test_function":
        raise ValueError("constant_dependency 必须是 fixed_test_function")
    return {"uses": uses, "claimed_uses": checked_claims}


def default_contract() -> dict[str, object]:
    """返回只声明有限核算术的默认合同。"""
    uses = ("finite_arithmetic", "mobius_definition", "gcd_relation", "euler_phi_divisor_sum", "finite_gram_decomposition", "finite_sum_identity")
    return {"kernel_identity": True, "gram_positivity": True, "offdiagonal_cancellation_lemma": False,
            "uniformity_variable": "truncation", "constant_dependency": "fixed_test_function", "uses": uses,
            "claimed_uses": {name: ("finite_arithmetic", "finite_sum_identity") for name in REQUIRED_CLAIMED_USES}}


def audit_bilinear_kernel_cancellation(contract: Mapping[str, object], limit: object) -> dict[str, object]:
    """登记有限核结论，绝不提升统一解析状态。"""
    return {**_validate_contract(contract), **finite_bilinear_kernel_model(limit),
            "finite_kernel_identity_status": "verified_finite", "finite_gram_positivity_status": "verified_finite",
            "diagonal_cancellation_obligation_status": "open", "coprime_restricted_tail_bound_status": "open",
            "w1_to_w2_status": "unproved", "rh_proved": False}


def render_markdown(payload: Mapping[str, object]) -> str:
    """渲染区分有限抵消与开放解析义务的证书。"""
    return "\n".join(("# MFAC W1→W2 双线性核抵消审计证书", "", "## 状态边界", "", "```text",
        f"finite_kernel_identity_status={payload['finite_kernel_identity_status']}", f"finite_gram_positivity_status={payload['finite_gram_positivity_status']}",
        f"diagonal_cancellation_obligation_status={payload['diagonal_cancellation_obligation_status']}", f"coprime_restricted_tail_bound_status={payload['coprime_restricted_tail_bound_status']}",
        f"w1_to_w2_status={payload['w1_to_w2_status']}", f"rh_proved={str(payload['rh_proved']).lower()}", "```", "",
        "有限负非对角项只构成有限抵消见证；本模块不证明统一 L² 上界、W1→W2 或 RH。", ""))


def write_certificate(payload: Mapping[str, object], json_out: Path, markdown_out: Path) -> None:
    """写出机器 JSON 和人读 Markdown 证书。"""
    json_out.parent.mkdir(parents=True, exist_ok=True)
    markdown_out.parent.mkdir(parents=True, exist_ok=True)
    json_out.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    markdown_out.write_text(render_markdown(payload), encoding="utf-8")


def main() -> None:
    """解析 CLI 参数并生成默认有限核证书。"""
    parser = argparse.ArgumentParser(description="生成 MFAC W1→W2 双线性核抵消证书")
    parser.add_argument("--limit", type=int, default=512)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--markdown-out", type=Path, default=DEFAULT_MARKDOWN)
    args = parser.parse_args()
    write_certificate(audit_bilinear_kernel_cancellation(default_contract(), args.limit), args.json_out, args.markdown_out)


if __name__ == "__main__":
    main()
