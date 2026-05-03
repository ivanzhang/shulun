#!/usr/bin/env python3
"""D4/R5 带显式误差预算的区间审计。

该脚本不依赖第三方区间库。它用 Decimal 高精计算中心值，并为每次
ln/exp/pow 和四则运算累计保守绝对误差预算，最后输出 [value-error,value+error]。
这是从 Decimal 审计走向形式化外向舍入证书的中间层。
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from dataclasses import dataclass
from decimal import Decimal, getcontext
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import d4_r5_fixed_membership_functional_roots as fm  # noqa: E402
import d4_r5_layer_functional_certificate as layer_cert  # noqa: E402

GAMMA = Decimal("0.57721566490153286060651209008240243104215933593992")


@dataclass
class BVal:
    """中心值加绝对误差预算。"""

    value: Decimal
    error: Decimal

    def add(self, other: "BVal", unit: Decimal) -> "BVal":
        return BVal(self.value + other.value, self.error + other.error + unit)

    def sub(self, other: "BVal", unit: Decimal) -> "BVal":
        return BVal(self.value - other.value, self.error + other.error + unit)

    def mul(self, other: "BVal", unit: Decimal) -> "BVal":
        value = self.value * other.value
        error = abs(self.value) * other.error + abs(other.value) * self.error + self.error * other.error + unit
        return BVal(value, error)

    def div(self, other: "BVal", unit: Decimal) -> "BVal":
        value = self.value / other.value
        denom = abs(other.value) - other.error
        if denom <= 0:
            raise ValueError("division interval crosses zero")
        error = (abs(self.value) * other.error + abs(other.value) * self.error) / (denom * denom) + unit
        return BVal(value, error)

    def neg(self) -> "BVal":
        return BVal(-self.value, self.error)


def const(x: Decimal | int | str) -> BVal:
    """精确常数。"""
    return BVal(Decimal(x), Decimal(0))


def ln_b(x: BVal, unit: Decimal) -> BVal:
    """ln 的预算传播。"""
    lower = x.value - x.error
    if lower <= 0:
        raise ValueError("log interval crosses zero")
    value = x.value.ln()
    error = x.error / lower + unit
    return BVal(value, error)


def exp_b(x: BVal, unit: Decimal) -> BVal:
    """exp 的预算传播。"""
    value = x.value.exp()
    error = value * (x.error.exp() - Decimal(1)) + unit
    return BVal(value, error)


def pow_b(x: BVal, exponent: Decimal, unit: Decimal) -> BVal:
    """x^exponent 的预算传播。"""
    return exp_b(BVal(exponent, Decimal(0)).mul(ln_b(x, unit), unit), unit)


def coeffs_for_a(x: BVal, a: int, tau: list[int], prefix: list[int], unit: Decimal) -> tuple[BVal, ...]:
    """单 a 的预算系数。"""
    # floor 固定由中心点决定；调用方负责确保处在固定相位单元。
    k1 = int(x.value // Decimal(a))
    k2 = int((Decimal(2) * x.value) // Decimal(a))
    weight = const(tau[a])
    inv = weight.div(const(a), unit)
    loga = ln_b(const(a), unit)
    ln2 = ln_b(const(2), unit)
    c_const = const(2).mul(weight, unit).mul(const(prefix[k1]), unit)
    c_s_log = const(2).mul(inv, unit)
    c_s0 = const(2).mul(inv, unit).mul(const(2).mul(const(GAMMA), unit).sub(const(1), unit).sub(loga, unit), unit)
    o_const = const(2).mul(weight, unit).mul(const(prefix[k2]), unit)
    o_s_log = const(4).mul(inv, unit)
    o_s0 = const(4).mul(inv, unit).mul(const(2).mul(const(GAMMA), unit).sub(const(1), unit).add(ln2, unit).sub(loga, unit), unit)
    return c_const, c_s_log, c_s0, o_const, o_s_log, o_s0


def term_value_first_second(x: BVal, a: int, q: BVal, tau: list[int], prefix: list[int], unit: Decimal) -> tuple[BVal, BVal, BVal]:
    """单 a 的 value, first, second 预算值。"""
    c_const, c_s_log, c_s0, o_const, o_s_log, o_s0 = coeffs_for_a(x, a, tau, prefix, unit)
    logx = ln_b(x, unit)
    c_val = c_const.sub(x.mul(c_s_log.mul(logx, unit).add(c_s0, unit), unit), unit)
    o_val = o_const.sub(x.mul(o_s_log.mul(logx, unit).add(o_s0, unit), unit), unit)
    c_der = c_s_log.mul(logx.add(const(1), unit), unit).add(c_s0, unit).neg()
    o_der = o_s_log.mul(logx.add(const(1), unit), unit).add(o_s0, unit).neg()
    x_m075 = pow_b(x, Decimal("-0.75"), unit)
    x_m175 = pow_b(x, Decimal("-1.75"), unit)
    x_m275 = pow_b(x, Decimal("-2.75"), unit)
    two_x_m075 = pow_b(const(2).mul(x, unit), Decimal("-0.75"), unit)
    value = o_val.mul(two_x_m075, unit).sub(q.mul(c_val, unit).mul(x_m075, unit), unit)
    first_old = const(2).pow if False else None
    old_factor = pow_b(const(2), Decimal("-0.75"), unit)
    first = old_factor.mul(o_der.mul(x_m075, unit).sub(const("0.75").mul(o_val, unit).mul(x_m175, unit), unit), unit).sub(
        q.mul(c_der.mul(x_m075, unit).sub(const("0.75").mul(c_val, unit).mul(x_m175, unit), unit), unit),
        unit,
    )
    p = Decimal("0.75")
    old_factor_core = pow_b(const(2), -p, unit)
    c0 = old_factor_core.mul(const(p * (p + 1)).mul(o_const, unit), unit).sub(q.mul(const(p * (p + 1)).mul(c_const, unit), unit), unit)
    c1 = old_factor_core.mul(const(p * (1 - p)).mul(o_s_log, unit), unit).sub(q.mul(const(p * (1 - p)).mul(c_s_log, unit), unit), unit)
    c2_old = const(p * (1 - p)).mul(o_s0, unit).add(const(2 * p - 1).mul(o_s_log, unit), unit)
    c2_new = const(p * (1 - p)).mul(c_s0, unit).add(const(2 * p - 1).mul(c_s_log, unit), unit)
    c2 = old_factor_core.mul(c2_old, unit).sub(q.mul(c2_new, unit), unit)
    core = c0.add(x.mul(c1.mul(logx, unit).add(c2, unit), unit), unit)
    second = x_m275.mul(core, unit)
    return value, first, second


def group_values(x: BVal, group: dict, q: BVal, tau: list[int], prefix: list[int], unit: Decimal) -> tuple[BVal, BVal, BVal]:
    """团值预算。"""
    total = (const(0), const(0), const(0))
    for a in group["a_values"]:
        vals = term_value_first_second(x, a, q, tau, prefix, unit)
        total = tuple(total[i].add(vals[i], unit) for i in range(3))
    return total


def functional_second(kind: str, x: BVal, memberships: dict, q: BVal, tau: list[int], prefix: list[int], unit: Decimal) -> BVal:
    """层泛函二阶导预算。"""
    groups = memberships["L"] if kind in {"E2", "potential"} else memberships[kind]
    terms = [group_values(x, group, q, tau, prefix, unit) for group in groups]
    values = [t[0] for t in terms]
    firsts = [t[1] for t in terms]
    seconds = [t[2] for t in terms]
    L = const(0)
    L1 = const(0)
    L2 = const(0)
    for value, first, second in terms:
        L = L.add(value, unit)
        L1 = L1.add(first, unit)
        L2 = L2.add(second, unit)
    if kind in {"U", "V", "light_L", "L"}:
        return L2
    E2_2 = const(0)
    for value, first, second in zip(values, firsts, seconds):
        E2_2 = E2_2.add(const(2).mul(first.mul(first, unit).add(value.mul(second, unit), unit), unit), unit)
    if kind == "E2":
        return E2_2
    correction = L1.mul(L1, unit).add(L.mul(L2, unit), unit).div(const(10), unit)
    return E2_2.sub(correction, unit)


def audit(x_anchor: int, kind: str, left: float, right: float, precision: int, unit: Decimal) -> dict:
    """审计一个子区间。"""
    getcontext().prec = precision
    tau, prefix = layer_cert.build(2 * (math.ceil(right) + 2))
    memberships = fm.row_membership_sets(x_anchor, 400, 0.958, 60, 80, tau, prefix)
    q = const("0.958")
    l = Decimal(str(left)); r = Decimal(str(right))
    points = [l + (r - l) * Decimal(i) / Decimal(4) for i in range(5)]
    vals = [functional_second(kind, BVal(point, unit), memberships, q, tau, prefix, unit) for point in points]
    centers = [v.value for v in vals]
    errors = [v.error for v in vals]
    variation = max(abs(centers[i + 1] - centers[i]) + errors[i + 1] + errors[i] for i in range(4))
    lower = min(c - e for c, e in zip(centers, errors)) - variation
    upper = max(c + e for c, e in zip(centers, errors)) + variation
    return {
        "x_anchor": x_anchor,
        "functional": kind,
        "interval": [str(l), str(r)],
        "precision": precision,
        "unit_error_budget": str(unit),
        "centers": [str(c) for c in centers],
        "point_errors": [str(e) for e in errors],
        "variation_budget": str(variation),
        "enclosure": [str(lower), str(upper)],
        "sign_certified": lower > 0 or upper < 0,
        "signed_margin": str(lower if lower > 0 else (-upper if upper < 0 else Decimal(0))),
        "max_point_error": str(max(errors)),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--x", type=int, default=1088499)
    parser.add_argument("--functional", default="V")
    parser.add_argument("--left", type=float, default=1088499.4687500312)
    parser.add_argument("--right", type=float, default=1088499.4999999688)
    parser.add_argument("--precision", type=int, default=80)
    parser.add_argument("--unit", default="1e-50")
    parser.add_argument("--json", type=Path, default=Path("docs/d4-r5-budget-interval-audit-worst.json"))
    args = parser.parse_args()
    payload = audit(args.x, args.functional, args.left, args.right, args.precision, Decimal(args.unit))
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
