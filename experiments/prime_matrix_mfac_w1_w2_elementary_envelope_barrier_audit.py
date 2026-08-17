"""审计 MFAC W1→W2 初等绝对值包络的有限障碍。"""

import argparse
from fractions import Fraction
import json
from math import gcd
from pathlib import Path
from typing import Mapping


DEFAULT_JSON = Path(
    "docs/monograph/prime-matrix-mfac-w1-w2-elementary-envelope-barrier-audit.json"
)
DEFAULT_MARKDOWN = Path(
    "docs/monograph/prime-matrix-mfac-w1-w2-elementary-envelope-barrier-audit.md"
)

ALLOWED_SOURCES = frozenset(
    {
        "finite_arithmetic",
        "mobius_definition",
        "coprimality_relation",
        "triangle_inequality",
        "finite_sum_identity",
    }
)
REQUIRED_CLAIMED_USES = frozenset(
    {
        "finite_tail_identity",
        "triangle_envelope",
        "euler_phi_aggregation",
        "dyadic_growth_witness",
    }
)
FORBIDDEN_INPUTS = frozenset(
    {
        "Mertens",
        "PNT",
        "RH",
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
        "uniform_l2_upper_proved",
        "w1_to_w2_proved",
        "w2_closed",
        "chebyshev_energy_bridge_proved",
        "rh_proved",
        "rh_consequence",
    }
)
FIXED_STATUSES = {
    "finite_inequality_status": "verified_finite",
    "finite_growth_status": "finite_growth_witnessed",
    "nonuniformity_obligation_status": "open",
    "w1_to_w2_status": "unproved",
}


def default_contract() -> dict[str, object]:
    """返回仅声明有限初等来源的默认合同。"""
    return {
        "uses": (
            "finite_arithmetic",
            "mobius_definition",
            "coprimality_relation",
            "triangle_inequality",
            "finite_sum_identity",
        ),
        "claimed_uses": {
            "finite_tail_identity": ("mobius_definition", "finite_sum_identity"),
            "triangle_envelope": ("triangle_inequality",),
            "euler_phi_aggregation": ("finite_arithmetic",),
            "dyadic_growth_witness": ("finite_arithmetic",),
        },
    }


def _checked_string_tuple(value: object, field_name: str) -> tuple[str, ...]:
    """验证非空字符串序列，拒绝裸字符串和非字符串元素。"""
    if type(value) not in (tuple, list):
        raise ValueError(f"{field_name} 必须是字符串 tuple 或 list")
    if not value or any(type(item) is not str for item in value):
        raise ValueError(f"{field_name} 必须是非空字符串序列")
    return tuple(value)


def _validate_contract(contract: object) -> dict[str, object]:
    """验证合同只使用有限来源且不包含结论提升。"""
    if not isinstance(contract, Mapping):
        raise ValueError("contract 必须是 Mapping")

    uses = _checked_string_tuple(contract.get("uses"), "uses")
    forbidden_sources = set(uses) & FORBIDDEN_INPUTS
    if forbidden_sources:
        raise ValueError(f"uses 包含禁止来源: {sorted(forbidden_sources)}")
    unknown_sources = set(uses) - ALLOWED_SOURCES
    if unknown_sources:
        raise ValueError(f"uses 包含未允许来源: {sorted(unknown_sources)}")

    claimed_uses = contract.get("claimed_uses")
    if not isinstance(claimed_uses, Mapping):
        raise ValueError("claimed_uses 必须是 Mapping")
    if set(claimed_uses) != REQUIRED_CLAIMED_USES:
        raise ValueError("claimed_uses 必须完整声明每项有限义务")
    checked_claimed_uses: dict[str, tuple[str, ...]] = {}
    for obligation in REQUIRED_CLAIMED_USES:
        declared = _checked_string_tuple(claimed_uses[obligation], obligation)
        forbidden_sources = set(declared) & FORBIDDEN_INPUTS
        if forbidden_sources:
            raise ValueError(f"{obligation} 包含禁止来源: {sorted(forbidden_sources)}")
        if not set(declared).issubset(uses):
            raise ValueError(f"{obligation} 包含未声明来源")
        checked_claimed_uses[obligation] = declared

    for field in FORBIDDEN_CONCLUSION_FIELDS:
        if field in contract and (type(contract[field]) is not bool or contract[field]):
            raise ValueError(f"{field} 不能提升为已证明")
    for field, expected in FIXED_STATUSES.items():
        if field in contract and contract[field] != expected:
            raise ValueError(f"{field} 必须保持 {expected}")

    return {"uses": uses, "claimed_uses": checked_claimed_uses}


def _require_limit(limit: object) -> int:
    """验证有限模型截断只使用合法的内建整数。"""
    if type(limit) is not int or limit < 3:
        raise ValueError("limit 必须是至少为 3 的内建整数")
    return limit


def mobius_value(index: int) -> int:
    """以定义计算整数的 Möbius 函数值。"""
    remaining = index
    prime_factors = 0
    factor = 2
    while factor * factor <= remaining:
        if remaining % factor == 0:
            remaining //= factor
            if remaining % factor == 0:
                return 0
            prime_factors += 1
            while remaining % factor == 0:
                remaining //= factor
        factor += 1
    if remaining > 1:
        prime_factors += 1
    return -1 if prime_factors % 2 else 1


def euler_phi(index: int) -> int:
    """以有限互素计数计算 Euler--φ 值。"""
    return sum(1 for candidate in range(1, index + 1) if gcd(candidate, index) == 1)


def _fraction_text(value: Fraction) -> str:
    """将精确分数渲染为稳定文本。"""
    return str(value)


def _require_dyadic_levels(dyadic_levels: object) -> int:
    """验证请求的 dyadic 截断层数。"""
    if type(dyadic_levels) is not int or dyadic_levels < 1:
        raise ValueError("dyadic_levels 必须是正内建整数")
    return dyadic_levels


def _r2_envelope(limit: int) -> Fraction:
    """计算截断为 limit 时 r=2 的精确绝对值包络。"""
    return Fraction(1, 2) * sum(
        (
            Fraction(1, cofactor)
            for cofactor in range(1, (limit - 1) // 2 + 1)
            if gcd(cofactor, 2) == 1
        ),
        Fraction(0),
    )


def dyadic_envelope_growth_witness(
    limit: object, dyadic_levels: object
) -> dict[str, object]:
    """为 r=2 生成仅陈述有限增长的精确 dyadic 见证。"""
    checked_limit = _require_limit(limit)
    checked_levels = _require_dyadic_levels(dyadic_levels)
    largest_exponent = checked_limit.bit_length() - 1
    available_levels = largest_exponent - 1
    if checked_levels > available_levels:
        raise ValueError("dyadic_levels 超过 limit 可提供的二幂尺度数")

    first_exponent = largest_exponent - checked_levels + 1
    dyadic_limits = tuple(1 << exponent for exponent in range(first_exponent, largest_exponent + 1))
    adjacent_witnesses: list[dict[str, object]] = []
    for base_limit, next_limit in zip(dyadic_limits, dyadic_limits[1:]):
        base_envelope = _r2_envelope(base_limit)
        next_envelope = _r2_envelope(next_limit)
        odd_block_sum = sum(
            (
                Fraction(1, cofactor)
                for cofactor in range(base_limit // 2, base_limit)
                if cofactor % 2 == 1
            ),
            Fraction(0),
        )
        block_increment = Fraction(1, 2) * odd_block_sum
        increment = next_envelope - base_envelope
        block_lower_bound = Fraction(1, 2 * (base_limit - 1))
        adjacent_witnesses.append(
            {
                "base_limit": base_limit,
                "next_limit": next_limit,
                "base_r2_envelope_squared": _fraction_text(base_envelope * base_envelope),
                "next_r2_envelope_squared": _fraction_text(next_envelope * next_envelope),
                "odd_block_sum": _fraction_text(odd_block_sum),
                "increment": _fraction_text(increment),
                "block_increment": _fraction_text(block_increment),
                "block_identity_residual": _fraction_text(increment - block_increment),
                "block_lower_bound": _fraction_text(block_lower_bound),
            }
        )

    return {
        "limit": checked_limit,
        "dyadic_levels": checked_levels,
        "dyadic_limits": dyadic_limits,
        "adjacent_witnesses": tuple(adjacent_witnesses),
        "finite_growth_status": "finite_growth_witnessed",
        "nonuniformity_obligation_status": "open",
    }


def finite_elementary_envelope_model(limit: object) -> dict[str, object]:
    """精确核验有限尾和、绝对值包络及 Euler--φ 聚合。"""
    checked_limit = _require_limit(limit)
    rows: list[dict[str, object]] = []
    finite_energy = Fraction(0)
    envelope_energy = Fraction(0)

    for modulus in range(2, checked_limit):
        direct_tail = sum(
            (
                Fraction(mobius_value(divisor), divisor)
                for divisor in range(2, checked_limit)
                if divisor % modulus == 0
            ),
            Fraction(0),
        )
        factored_tail = Fraction(mobius_value(modulus), modulus) * sum(
            (
                Fraction(mobius_value(cofactor), cofactor)
                for cofactor in range(1, (checked_limit - 1) // modulus + 1)
                if gcd(cofactor, modulus) == 1
            ),
            Fraction(0),
        )
        envelope = Fraction(abs(mobius_value(modulus)), modulus) * sum(
            (
                Fraction(1, cofactor)
                for cofactor in range(1, (checked_limit - 1) // modulus + 1)
                if gcd(cofactor, modulus) == 1
            ),
            Fraction(0),
        )
        weight = euler_phi(modulus)
        weighted_energy = weight * direct_tail * direct_tail
        weighted_envelope = weight * envelope * envelope
        finite_energy += weighted_energy
        envelope_energy += weighted_envelope
        rows.append(
            {
                "modulus": modulus,
                "direct_tail": _fraction_text(direct_tail),
                "factored_tail": _fraction_text(factored_tail),
                "tail_identity_residual": _fraction_text(direct_tail - factored_tail),
                "absolute_envelope": _fraction_text(envelope),
                "pointwise_envelope_slack": _fraction_text(
                    envelope - abs(direct_tail)
                ),
                "weight": weight,
                "weighted_energy_component": _fraction_text(weighted_energy),
                "weighted_envelope_component": _fraction_text(weighted_envelope),
            }
        )

    r2_row = next(row for row in rows if row["modulus"] == 2)
    return {
        "limit": checked_limit,
        "candidate_moduli": tuple(range(2, checked_limit)),
        "rows": tuple(rows),
        "finite_energy": _fraction_text(finite_energy),
        "absolute_envelope_energy": _fraction_text(envelope_energy),
        "aggregate_envelope_slack": _fraction_text(envelope_energy - finite_energy),
        "r2_envelope_component": r2_row["weighted_envelope_component"],
        "finite_inequality_status": "verified_finite",
    }


def audit_elementary_envelope_barrier(
    contract: Mapping[str, object], limit: object, dyadic_levels: object
) -> dict[str, object]:
    """登记有限审计状态，绝不把有限读数提升为解析结论。"""
    checked_contract = _validate_contract(contract)
    return {
        **checked_contract,
        **finite_elementary_envelope_model(limit),
        **dyadic_envelope_growth_witness(limit, dyadic_levels),
        "finite_inequality_status": "verified_finite",
        "finite_growth_status": "finite_growth_witnessed",
        "nonuniformity_obligation_status": "open",
        "w1_to_w2_status": "unproved",
        "rh_proved": False,
    }


def render_markdown(payload: Mapping[str, object]) -> str:
    """渲染明确区分有限读数与开放解析义务的证书。"""
    return "\n".join(
        (
            "# MFAC W1→W2 初等绝对值包络障碍审计证书",
            "",
            f"finite_inequality_status={payload['finite_inequality_status']}",
            f"finite_growth_status={payload['finite_growth_status']}",
            (
                "nonuniformity_obligation_status="
                f"{payload['nonuniformity_obligation_status']}"
            ),
            f"w1_to_w2_status={payload['w1_to_w2_status']}",
            f"rh_proved={str(payload['rh_proved']).lower()}",
            "",
            "## 边界",
            "",
            "本证书只核验有限 Möbius 尾和、三角不等式包络与有限 dyadic 读数。",
            "有限增长见证不证明 D→∞ 发散，也不证明不存在统一 L² 上界。",
            "本模块不证明 W1→W2、Chebyshev 能量桥或 RH。",
            "",
            "## 使用示例",
            "",
            "```bash",
            "python3 experiments/prime_matrix_mfac_w1_w2_elementary_envelope_barrier_audit.py \\",
            "  --limit 512 --dyadic-levels 5",
            "```",
            "",
        )
    )


def write_certificate(
    payload: Mapping[str, object], json_out: Path, markdown_out: Path
) -> None:
    """写出机器可读 JSON 与人读 Markdown 有限证书。"""
    json_out.parent.mkdir(parents=True, exist_ok=True)
    markdown_out.parent.mkdir(parents=True, exist_ok=True)
    json_out.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    markdown_out.write_text(render_markdown(payload), encoding="utf-8")


def main() -> None:
    """解析命令行参数并生成默认有限证书。"""
    parser = argparse.ArgumentParser(
        description="生成 MFAC W1→W2 初等绝对值包络障碍证书"
    )
    parser.add_argument("--limit", type=int, default=512)
    parser.add_argument("--dyadic-levels", type=int, default=5)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--markdown-out", type=Path, default=DEFAULT_MARKDOWN)
    args = parser.parse_args()
    payload = audit_elementary_envelope_barrier(
        default_contract(), args.limit, args.dyadic_levels
    )
    write_certificate(payload, args.json_out, args.markdown_out)


if __name__ == "__main__":
    main()
