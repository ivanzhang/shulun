#!/usr/bin/env python3
"""D4/R5 Decimal 高精区间审计。

目标：对固定成员层泛函证书中的最坏子区间，用 Decimal 高精度和
人为外扩误差重算 F'' 包络，检查双精度余量是否稳定。

注意：Decimal ln/power 仍不是形式化证明器；本脚本是迈向外向舍入区间
算术的审计层，用高精+外扩替代双精裸计算。
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from decimal import Decimal, getcontext
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import d4_r5_fixed_membership_functional_roots as fm  # noqa: E402
import d4_r5_layer_functional_certificate as layer_cert  # noqa: E402

GAMMA = Decimal("0.57721566490153286060651209008240243104215933593992")
LN2 = Decimal(2).ln()


def dlog(x: Decimal) -> Decimal:
    """Decimal 自然对数。"""
    return x.ln()


def dpow_neg(x: Decimal, exponent: Decimal) -> Decimal:
    """计算 x^{-exponent}。"""
    return (-(exponent) * x.ln()).exp()


def decimal_coeffs_for_a(x_probe: Decimal, a: int, tau: list[int], prefix: list[int]) -> tuple[Decimal, ...]:
    """固定 floor 单元下单个 a 的 Decimal 系数。"""
    k1 = int(x_probe // Decimal(a))
    k2 = int((Decimal(2) * x_probe) // Decimal(a))
    weight = Decimal(tau[a])
    inv = weight / Decimal(a)
    c_const = Decimal(2) * weight * Decimal(prefix[k1])
    c_s_log = Decimal(2) * inv
    c_s0 = Decimal(2) * inv * (Decimal(2) * GAMMA - Decimal(1) - Decimal(a).ln())
    o_const = Decimal(2) * weight * Decimal(prefix[k2])
    o_s_log = Decimal(4) * inv
    o_s0 = Decimal(4) * inv * (Decimal(2) * GAMMA - Decimal(1) + LN2 - Decimal(a).ln())
    return c_const, c_s_log, c_s0, o_const, o_s_log, o_s0


def decimal_contract_second(x: Decimal, a: int, q: Decimal, tau: list[int], prefix: list[int]) -> Decimal:
    """单 a contract 的二阶导数 Decimal 值。"""
    c_const, c_s_log, c_s0, o_const, o_s_log, o_s0 = decimal_coeffs_for_a(x, a, tau, prefix)
    p = Decimal("0.75")
    old_factor = Decimal(2) ** (-p)
    c0 = old_factor * p * (p + Decimal(1)) * o_const - q * p * (p + Decimal(1)) * c_const
    c1 = old_factor * p * (Decimal(1) - p) * o_s_log - q * p * (Decimal(1) - p) * c_s_log
    c2_old = p * (Decimal(1) - p) * o_s0 + (Decimal(2) * p - Decimal(1)) * o_s_log
    c2_new = p * (Decimal(1) - p) * c_s0 + (Decimal(2) * p - Decimal(1)) * c_s_log
    c2 = old_factor * c2_old - q * c2_new
    core = c0 + x * (c1 * x.ln() + c2)
    return (x ** Decimal("-2.75")) * core


def decimal_term_value_first_second(x: Decimal, a: int, q: Decimal, tau: list[int], prefix: list[int]) -> tuple[Decimal, Decimal, Decimal]:
    """返回单 a 的 value, first, second。"""
    coeffs = decimal_coeffs_for_a(x, a, tau, prefix)
    c_const, c_s_log, c_s0, o_const, o_s_log, o_s0 = coeffs
    logx = x.ln()
    c_val = c_const - x * (c_s_log * logx + c_s0)
    o_val = o_const - x * (o_s_log * logx + o_s0)
    c_der = -(c_s_log * (logx + Decimal(1)) + c_s0)
    o_der = -(o_s_log * (logx + Decimal(1)) + o_s0)
    value = o_val / ((Decimal(2) * x) ** Decimal("0.75")) - q * c_val / (x ** Decimal("0.75"))
    first = (Decimal(2) ** Decimal("-0.75")) * (o_der * (x ** Decimal("-0.75")) - Decimal("0.75") * o_val * (x ** Decimal("-1.75"))) - q * (
        c_der * (x ** Decimal("-0.75")) - Decimal("0.75") * c_val * (x ** Decimal("-1.75"))
    )
    second = decimal_contract_second(x, a, q, tau, prefix)
    return value, first, second


def decimal_group_values(x: Decimal, group: dict, q: Decimal, tau: list[int], prefix: list[int]) -> tuple[Decimal, Decimal, Decimal]:
    """偏移团 B_h 及导数。"""
    vals = [decimal_term_value_first_second(x, a, q, tau, prefix) for a in group["a_values"]]
    return sum(v[0] for v in vals), sum(v[1] for v in vals), sum(v[2] for v in vals)


def decimal_functional_second(kind: str, x: Decimal, memberships: dict, q: Decimal, tau: list[int], prefix: list[int]) -> Decimal:
    """层泛函二阶导数。"""
    groups = memberships["L"] if kind in {"E2", "potential"} else memberships[kind]
    terms = [decimal_group_values(x, group, q, tau, prefix) for group in groups]
    values = [t[0] for t in terms]
    firsts = [t[1] for t in terms]
    seconds = [t[2] for t in terms]
    L = sum(values)
    L1 = sum(firsts)
    L2 = sum(seconds)
    if kind in {"U", "V", "light_L", "L"}:
        return L2
    E2_2 = Decimal(2) * sum(first * first + value * second for value, first, second in zip(values, firsts, seconds))
    if kind == "E2":
        return E2_2
    return E2_2 - (L1 * L1 + L * L2) / Decimal(10)


def audit_interval(x_anchor: int, kind: str, left: float, right: float, precision: int, outward: Decimal) -> dict:
    """审计一个子区间的 F'' 包络。"""
    getcontext().prec = precision
    tau, prefix = layer_cert.build(2 * (math.ceil(right) + 2))
    memberships = fm.row_membership_sets(x_anchor, 400, 0.958, 60, 80, tau, prefix)
    q = Decimal("0.958")
    l = Decimal(str(left))
    r = Decimal(str(right))
    points = [l + (r - l) * Decimal(i) / Decimal(4) for i in range(5)]
    values = [decimal_functional_second(kind, point, memberships, q, tau, prefix) for point in points]
    local_variation = max(abs(values[i + 1] - values[i]) for i in range(4))
    lower = min(values) - local_variation - outward
    upper = max(values) + local_variation + outward
    return {
        "x_anchor": x_anchor,
        "functional": kind,
        "interval": [str(l), str(r)],
        "precision": precision,
        "outward_margin": str(outward),
        "values": [str(v) for v in values],
        "local_variation_margin": str(local_variation),
        "enclosure": [str(lower), str(upper)],
        "sign_certified": lower > 0 or upper < 0,
        "signed_margin": str(lower if lower > 0 else (-upper if upper < 0 else Decimal(0))),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--x", type=int, default=1088499)
    parser.add_argument("--functional", default="V")
    parser.add_argument("--left", type=float, default=1088499.4687500312)
    parser.add_argument("--right", type=float, default=1088499.4999999688)
    parser.add_argument("--precision", type=int, default=80)
    parser.add_argument("--outward", default="1e-30")
    parser.add_argument("--json", type=Path, default=Path("docs/d4-r5-decimal-interval-audit-worst.json"))
    args = parser.parse_args()
    payload = audit_interval(args.x, args.functional, args.left, args.right, args.precision, Decimal(args.outward))
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
