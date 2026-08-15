"""审计 Euler、Gauss 与 Riemann 三层精确因子化。"""

import argparse
import json
from math import isfinite, log
from pathlib import Path
import sys
from typing import Mapping

if __package__ in (None, ""):
    # 直接按脚本路径运行时确保仓库根目录可导入。
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from experiments.prime_matrix_mfac_actual_lcm_gram_energy_audit import (
    lcm_gram_quadratic_form,
    mobius,
    von_mangoldt,
)


DEFAULT_JSON = Path("docs/monograph/prime-matrix-mfac-euler-gauss-riemann-factorization-audit.json")
DEFAULT_MARKDOWN = Path("docs/monograph/prime-matrix-mfac-euler-gauss-riemann-factorization-audit.md")
FORBIDDEN_INPUTS = frozenset(
    {
        "RH",
        "zeta_zero",
        "zero_free_region",
        "explicit_formula",
        "Mellin_contraction",
        "w3_spectral_contraction",
        "finite_profile",
        "numerical_experiment",
        "free_multiplicative_model",
    }
)
FORBIDDEN_CONCLUSION_FIELDS = frozenset(
    {"rh_proved", "w3_closed", "mellin_continuation_proved", "spectral_gap_proved"}
)


def _require_limit(value: object) -> int:
    """验证有限审计上界。"""
    if type(value) is not int or value < 2:
        raise ValueError("limit 必须是至少为 2 的内建整数")
    return value


def _checked_string_tuple(value: object, field_name: str) -> tuple[str, ...]:
    """验证非空字符串序列，拒绝裸字符串和空来源。"""
    if type(value) not in (tuple, list):
        raise ValueError(f"{field_name} 必须是字符串 tuple 或 list")
    if not value or any(type(item) is not str or not item for item in value):
        raise ValueError(f"{field_name} 必须含非空字符串")
    return tuple(value)


def euler_coefficients(limit: object) -> dict[int, float]:
    """返回 Euler 反演系数 a(d)=-mu(d)log(d)。"""
    checked_limit = _require_limit(limit)
    return {
        divisor: -mobius(divisor) * log(divisor)
        for divisor in range(1, checked_limit + 1)
    }


def divisor_transform(coefficients: Mapping[int, float], value: object) -> float:
    """计算有限 divisor transform D a(n)=sum_{d|n}a(d)。"""
    if type(value) is not int or value < 1:
        raise ValueError("value 必须是正内建整数")
    return sum(weight for divisor, weight in coefficients.items() if value % divisor == 0)


def _psi_at(integer_part: int) -> float:
    """计算有限 Chebyshev 和 psi(floor(x))。"""
    return sum(von_mangoldt(value) for value in range(1, integer_part + 1))


def _mellin_identity_contract(contract: Mapping[str, object]) -> dict[str, object]:
    """登记 Mellin 公式的正确初始定义域，拒绝左移或收缩循环。"""
    if not isinstance(contract, Mapping):
        raise ValueError("contract 必须是 Mapping")
    forbidden_fields = tuple(
        field for field in FORBIDDEN_CONCLUSION_FIELDS if field in contract
    )
    if forbidden_fields:
        raise ValueError(f"contract 含目标结论循环字段：{', '.join(forbidden_fields)}")
    real_part = contract.get("real_part")
    if type(real_part) not in (int, float) or not isfinite(float(real_part)):
        raise ValueError("real_part 必须是有限内建实数")
    if float(real_part) <= 1.0:
        raise ValueError("real_part 必须严格大于 1")
    uses = _checked_string_tuple(contract.get("uses"), "uses")
    claimed = _checked_string_tuple(contract.get("claimed_identity_uses"), "claimed_identity_uses")
    forbidden = tuple(item for item in uses + claimed if item in FORBIDDEN_INPUTS)
    if forbidden:
        raise ValueError(f"uses 含禁止循环依赖：{', '.join(forbidden)}")
    undeclared = tuple(item for item in claimed if item not in uses)
    if undeclared:
        raise ValueError(f"claimed_identity_uses 含未声明依赖：{', '.join(undeclared)}")
    return {
        "mellin_real_part": float(real_part),
        "mellin_identity_domain": "real_part_greater_than_one",
        "mellin_uses": uses,
        "claimed_identity_uses": claimed,
    }


def default_mellin_contract(real_part: float = 1.25) -> dict[str, object]:
    """返回仅登记 Re(s)>1 初始 Mellin 恒等式的默认合同。"""
    uses = (
        "euler_mobius_inversion",
        "discrete_continuous_floor_correction",
        "mellin_stieltjes_identity",
    )
    return {
        "real_part": real_part,
        "uses": uses,
        "claimed_identity_uses": uses,
    }


def audit_euler_gauss_riemann_factorization(
    limit: object, mellin_contract: Mapping[str, object] | None = None
) -> dict[str, object]:
    """有限核验三层因子化，绝不升级为 Mellin 收缩或 RH。"""
    checked_limit = _require_limit(limit)
    coefficients = euler_coefficients(checked_limit)
    mismatches = tuple(
        value
        for value in range(1, checked_limit + 1)
        if abs(divisor_transform(coefficients, value) - von_mangoldt(value)) > 1e-12
    )
    direct_energy = sum(
        divisor_transform(coefficients, value) ** 2
        for value in range(1, checked_limit + 1)
    )
    gram_energy = lcm_gram_quadratic_form(checked_limit, coefficients)
    correction_residual = 0.0
    for integer_part in range(1, checked_limit + 1):
        prefix = sum(
            divisor_transform(coefficients, value) - 1.0
            for value in range(1, integer_part + 1)
        )
        for point in (float(integer_part), integer_part + 0.5):
            left = _psi_at(integer_part) - point
            right = prefix + integer_part - point
            correction_residual = max(correction_residual, abs(left - right))
    mellin = _mellin_identity_contract(
        default_mellin_contract() if mellin_contract is None else mellin_contract
    )
    return {
        "limit": checked_limit,
        "euler_coefficient_formula": "a(d)=-mu(d)*log(d)",
        "euler_inversion_mismatch_count": len(mismatches),
        "euler_inversion_mismatches": mismatches,
        "gauss_direct_energy": direct_energy,
        "gauss_lcm_gram_energy": gram_energy,
        "gauss_gram_residual": direct_energy - gram_energy,
        "discrete_continuous_correction_residual": correction_residual,
        "factorization_formula": (
            "psi(x)-x=S(D(-mu*log)-1)(x)+floor(x)-x"
        ),
        **mellin,
        "forbidden_dependency_check": "passed",
        "euler_gauss_riemann_factorization_status": "finite_exact_identity_registered",
        "cross_scale_prefix_coercivity_status": "unproved",
        "actual_mellin_half_plane_contraction_status": "unproved",
        "rh_proved": False,
    }


def _render_markdown(payload: Mapping[str, object]) -> str:
    """渲染三层公式、定义域与唯一开放门。"""
    return f"""# MFAC Euler–Gauss–Riemann 三层因子化审计

## 有限核验

- `limit`：`{payload['limit']}`
- Euler 反演失配数：`{payload['euler_inversion_mismatch_count']}`
- Gauss LCM Gram 残差：`{payload['gauss_gram_residual']}`
- 离散—连续校正残差：`{payload['discrete_continuous_correction_residual']}`

```text
Lambda=D(-mu*log)
psi(x)-x=S(D(-mu*log)-1)(x)+floor(x)-x
Mellin domain: Re(s)>1
```

## 状态边界

```text
euler_gauss_riemann_factorization_status=finite_exact_identity_registered
cross_scale_prefix_coercivity_status=unproved
actual_mellin_half_plane_contraction_status=unproved
rh_proved=false
```

有限 LCM Gram 正定性控制的是 divisor transform 的局部二次能量；Mellin 公式在
`Re(s)>1` 只给出精确表示。把它推进到 `Re(s)>1/2` 所需的跨 dyadic 尺度前缀和
强制性仍未证明，本证书不证明零自由区域或 RH。

## 使用示例

```bash
python3 experiments/prime_matrix_mfac_euler_gauss_riemann_factorization_audit.py \\
  --limit 96
```
"""


def write_certificate(payload: Mapping[str, object], json_out: Path, markdown_out: Path) -> None:
    """写出机器证书和人读证书。"""
    json_out.parent.mkdir(parents=True, exist_ok=True)
    markdown_out.parent.mkdir(parents=True, exist_ok=True)
    json_out.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    markdown_out.write_text(_render_markdown(payload), encoding="utf-8")


def main() -> None:
    """运行默认有限审计并写出证书。"""
    parser = argparse.ArgumentParser(description="生成 MFAC Euler–Gauss–Riemann 因子化证书")
    parser.add_argument("--limit", type=int, default=96)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--markdown-out", type=Path, default=DEFAULT_MARKDOWN)
    args = parser.parse_args()
    write_certificate(
        audit_euler_gauss_riemann_factorization(args.limit),
        args.json_out,
        args.markdown_out,
    )
    print(f"wrote {args.json_out}")
    print(f"wrote {args.markdown_out}")


if __name__ == "__main__":
    main()
