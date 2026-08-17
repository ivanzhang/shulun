"""审计 MFAC W1→W2 非循环 Möbius 尾和 L² 桥的有限缺口。"""

import argparse
from fractions import Fraction
import json
from math import gcd
from pathlib import Path
from typing import Mapping


DEFAULT_JSON = Path(
    "docs/monograph/prime-matrix-mfac-w1-w2-noncircular-mobius-tail-l2-audit.json"
)
DEFAULT_MARKDOWN = Path(
    "docs/monograph/prime-matrix-mfac-w1-w2-noncircular-mobius-tail-l2-audit.md"
)
REQUIRED_OBLIGATIONS = (
    "coprime_restricted_tail_bound",
    "euler_phi_l2_aggregation",
    "chebyshev_energy_transfer",
)
ALLOWED_INPUTS = frozenset(
    {
        "finite_arithmetic",
        "mobius_definition",
        "coprimality_relation",
        "finite_sum_identity",
    }
)
FORBIDDEN_INPUTS = frozenset(
    {
        "RH",
        "Mertens",
        "PNT",
        "zeta_zero",
        "zero_free_region",
        "explicit_formula",
        "Mellin",
        "Chebyshev_error",
        "target_energy_bridge",
        "chebyshev_energy_bridge",
        "finite_profile",
        "numerical_experiment",
    }
)
FORBIDDEN_CONCLUSION_FIELDS = frozenset(
    {
        "w1_to_w2_proved",
        "w2_closed",
        "chebyshev_energy_bridge_proved",
        "rh_proved",
        "rh_consequence",
    }
)


def _checked_string_tuple(value: object, field_name: str) -> tuple[str, ...]:
    """验证字符串序列，拒绝裸字符串和非字符串元素。"""
    if type(value) not in (tuple, list):
        raise ValueError(f"{field_name} 必须是字符串 tuple 或 list")
    if any(type(item) is not str or not item for item in value):
        raise ValueError(f"{field_name} 必须只含非空字符串")
    return tuple(value)


def _require_limit(limit: object) -> int:
    """验证有限模型截断长度。"""
    if type(limit) is not int or limit < 3:
        raise ValueError("limit 必须是至少为 3 的内建整数")
    return limit


def mobius_value(index: object) -> int:
    """以有限试除法计算 Möbius 函数。"""
    if type(index) is not int or index < 1:
        raise ValueError("index 必须是至少为 1 的内建整数")
    remaining = index
    prime_factor_count = 0
    divisor = 2
    while divisor * divisor <= remaining:
        if remaining % divisor == 0:
            remaining //= divisor
            if remaining % divisor == 0:
                return 0
            prime_factor_count += 1
            while remaining % divisor == 0:
                remaining //= divisor
        divisor += 1
    if remaining > 1:
        prime_factor_count += 1
    return -1 if prime_factor_count % 2 else 1


def euler_phi(index: object) -> int:
    """以有限试除法计算 Euler--φ。"""
    if type(index) is not int or index < 1:
        raise ValueError("index 必须是至少为 1 的内建整数")
    result = index
    remaining = index
    divisor = 2
    while divisor * divisor <= remaining:
        if remaining % divisor == 0:
            result -= result // divisor
            while remaining % divisor == 0:
                remaining //= divisor
        divisor += 1
    if remaining > 1:
        result -= result // remaining
    return result


def finite_coprime_mobius_tail_model(limit: object) -> dict[str, object]:
    """核验有限 Möbius 尾和重排，不声明任何渐近或解析结论。"""
    checked_limit = _require_limit(limit)
    coefficients = {
        index: Fraction(mobius_value(index), 1)
        for index in range(2, checked_limit)
    }
    divisor_tails = {
        modulus: sum(
            (value / index for index, value in coefficients.items() if index % modulus == 0),
            start=Fraction(0, 1),
        )
        for modulus in range(2, checked_limit)
    }
    coprime_tails = {
        modulus: (
            Fraction(mobius_value(modulus), modulus)
            * sum(
                (
                    Fraction(mobius_value(multiplier), multiplier)
                    for multiplier in range(1, checked_limit // modulus + 1)
                    if modulus * multiplier < checked_limit
                    and gcd(modulus, multiplier) == 1
                ),
                start=Fraction(0, 1),
            )
            if mobius_value(modulus) != 0
            else Fraction(0, 1)
        )
        for modulus in range(2, checked_limit)
    }
    direct_energy = sum(
        (
            left_value
            * right_value
            * Fraction(gcd(left_index, right_index) - 1, left_index * right_index)
            for left_index, left_value in coefficients.items()
            for right_index, right_value in coefficients.items()
        ),
        start=Fraction(0, 1),
    )
    euler_phi_energy = sum(
        (
            Fraction(euler_phi(modulus), 1) * tail * tail
            for modulus, tail in divisor_tails.items()
        ),
        start=Fraction(0, 1),
    )
    energy_residual = direct_energy - euler_phi_energy
    coprime_tail_residual = max(
        (
            abs(divisor_tails[modulus] - coprime_tails[modulus])
            for modulus in divisor_tails
        ),
        default=Fraction(0, 1),
    )
    return {
        "finite_model_status": (
            "verified_finite"
            if energy_residual == 0 and coprime_tail_residual == 0
            else "failed"
        ),
        "limit": checked_limit,
        "candidate_moduli": tuple(divisor_tails),
        "direct_finite_energy": str(direct_energy),
        "euler_phi_finite_energy": str(euler_phi_energy),
        "energy_identity_residual": str(energy_residual),
        "coprime_tail_identity_residual": str(coprime_tail_residual),
    }


def _validate_contract(contract: Mapping[str, object]) -> dict[str, object]:
    """验证只允许有限算术来源的 W1→W2 缺口登记合同。"""
    if not isinstance(contract, Mapping):
        raise ValueError("contract 必须是 Mapping")
    forbidden_fields = tuple(
        field for field in FORBIDDEN_CONCLUSION_FIELDS if field in contract
    )
    if forbidden_fields:
        raise ValueError(f"contract 含目标结论循环字段：{', '.join(forbidden_fields)}")

    obligations = _checked_string_tuple(contract.get("obligations"), "obligations")
    if obligations != REQUIRED_OBLIGATIONS:
        raise ValueError("obligations 必须精确匹配 REQUIRED_OBLIGATIONS")
    uses = _checked_string_tuple(contract.get("uses"), "uses")
    forbidden = tuple(source for source in uses if source in FORBIDDEN_INPUTS)
    if forbidden:
        raise ValueError(f"uses 含禁止循环依赖：{', '.join(forbidden)}")
    unallowed = tuple(source for source in uses if source not in ALLOWED_INPUTS)
    if unallowed:
        raise ValueError(f"uses 含未允许来源：{', '.join(unallowed)}")
    claimed_uses = contract.get("claimed_uses")
    if not isinstance(claimed_uses, Mapping):
        raise ValueError("claimed_uses 必须是 Mapping")
    if set(claimed_uses) != set(REQUIRED_OBLIGATIONS):
        raise ValueError("claimed_uses 必须精确覆盖 REQUIRED_OBLIGATIONS")
    checked_claimed_uses: dict[str, tuple[str, ...]] = {}
    for obligation in REQUIRED_OBLIGATIONS:
        if obligation not in claimed_uses:
            raise ValueError(f"claimed_uses 缺少义务：{obligation}")
        claimed = _checked_string_tuple(claimed_uses[obligation], obligation)
        forbidden_claimed = tuple(
            source for source in claimed if source in FORBIDDEN_INPUTS
        )
        if forbidden_claimed:
            raise ValueError(
                f"{obligation} 含禁止循环依赖：{', '.join(forbidden_claimed)}"
            )
        undeclared = tuple(source for source in claimed if source not in uses)
        if undeclared:
            raise ValueError(
                f"{obligation} 含未声明依赖：{', '.join(undeclared)}"
            )
        checked_claimed_uses[obligation] = claimed
    if contract.get("uniformity_variable") != "truncation":
        raise ValueError("uniformity_variable 必须是 truncation")
    if contract.get("constant_dependency") != "fixed_test_function":
        raise ValueError("constant_dependency 必须是 fixed_test_function")
    return {
        "obligations": obligations,
        "uses": uses,
        "claimed_uses": checked_claimed_uses,
        "uniformity_variable": "truncation",
        "constant_dependency": "fixed_test_function",
    }


def audit_noncircular_mobius_tail_l2(
    contract: Mapping[str, object], limit: object
) -> dict[str, object]:
    """登记非循环缺口，绝不生成 W1→W2 或 RH 证明结论。"""
    checked = _validate_contract(contract)
    finite_model = finite_coprime_mobius_tail_model(limit)
    return {
        **checked,
        **finite_model,
        "coprime_restricted_tail_bound_status": "open",
        "euler_phi_l2_aggregation_status": "open",
        "chebyshev_energy_transfer_status": "open",
        "w1_to_w2_status": "unproved",
        "rh_proved": False,
    }


def default_contract() -> dict[str, object]:
    """返回只含有限算术来源的默认合同。"""
    return {
        "uses": (
            "finite_arithmetic",
            "mobius_definition",
            "coprimality_relation",
            "finite_sum_identity",
        ),
        "obligations": REQUIRED_OBLIGATIONS,
        "claimed_uses": {
            obligation: ("finite_arithmetic", "finite_sum_identity")
            for obligation in REQUIRED_OBLIGATIONS
        },
        "uniformity_variable": "truncation",
        "constant_dependency": "fixed_test_function",
    }


def render_markdown(payload: Mapping[str, object]) -> str:
    """渲染同时展示有限核验与解析缺口的人读证书。"""
    return "\n".join(
        (
            "# MFAC W1→W2 非循环 Möbius 尾和 L² 桥有限审计",
            "",
            "## 有限模型",
            "",
            f"- 截断：`{payload['limit']}`",
            f"- 直接有限能量：`{payload['direct_finite_energy']}`",
            f"- Euler--φ 有限能量：`{payload['euler_phi_finite_energy']}`",
            f"- 能量恒等式残差：`{payload['energy_identity_residual']}`",
            (
                "- 互素尾和恒等式残差："
                f"`{payload['coprime_tail_identity_residual']}`"
            ),
            "",
            "## 状态边界",
            "",
            "```text",
            f"finite_model_status={payload['finite_model_status']}",
            f"w1_to_w2_status={payload['w1_to_w2_status']}",
            (
                "coprime_restricted_tail_bound_status="
                f"{payload['coprime_restricted_tail_bound_status']}"
            ),
            (
                "euler_phi_l2_aggregation_status="
                f"{payload['euler_phi_l2_aggregation_status']}"
            ),
            (
                "chebyshev_energy_transfer_status="
                f"{payload['chebyshev_energy_transfer_status']}"
            ),
            f"rh_proved={str(payload['rh_proved']).lower()}",
            "```",
            "",
            "本证书只验证有限 Möbius 尾和重排及其精确残差；不证明互素限制尾和",
            "L² 上界、Euler--φ 聚合的统一估计、Chebyshev 能量桥、Mellin 收缩、",
            "零自由区域或 RH。",
            "",
            "## 使用示例",
            "",
            "```bash",
            "python3 experiments/prime_matrix_mfac_w1_w2_noncircular_mobius_tail_l2_audit.py \\",
            "  --limit 512",
            "```",
            "",
        )
    )


def write_certificate(
    payload: Mapping[str, object], json_out: Path, markdown_out: Path
) -> None:
    """写出机器证书和明确不升级结论的人读证书。"""
    json_out.parent.mkdir(parents=True, exist_ok=True)
    markdown_out.parent.mkdir(parents=True, exist_ok=True)
    json_out.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    markdown_out.write_text(render_markdown(payload), encoding="utf-8")


def main() -> None:
    """运行默认有限模型并生成未证明边界明确的审计证书。"""
    parser = argparse.ArgumentParser(
        description="生成 MFAC W1→W2 非循环 Möbius 尾和有限审计证书"
    )
    parser.add_argument("--limit", type=int, default=512)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--markdown-out", type=Path, default=DEFAULT_MARKDOWN)
    args = parser.parse_args()
    payload = audit_noncircular_mobius_tail_l2(default_contract(), args.limit)
    write_certificate(payload, args.json_out, args.markdown_out)
    print(f"wrote {args.json_out}")
    print(f"wrote {args.markdown_out}")


if __name__ == "__main__":
    main()
