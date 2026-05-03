#!/usr/bin/env python3
"""D4/R5 外向舍入 Decimal 区间审计原型。

使用 decimal.localcontext 的 ROUND_FLOOR / ROUND_CEILING 对基础运算做外向舍入。
对 ln/exp/pow 同样使用定向 rounding 的 Decimal 函数；这是比中心值误差预算
更接近形式化区间库的证书层。
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from dataclasses import dataclass
from decimal import Decimal, ROUND_CEILING, ROUND_FLOOR, localcontext
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import d4_r5_fixed_membership_functional_roots as fm  # noqa: E402
import d4_r5_layer_functional_certificate as layer_cert  # noqa: E402

GAMMA_STR = "0.57721566490153286060651209008240243104215933593992"


def down(value: Decimal, precision: int) -> Decimal:
    """向下舍入一元值。"""
    with localcontext() as ctx:
        ctx.prec = precision
        ctx.rounding = ROUND_FLOOR
        return +value


def up(value: Decimal, precision: int) -> Decimal:
    """向上舍入一元值。"""
    with localcontext() as ctx:
        ctx.prec = precision
        ctx.rounding = ROUND_CEILING
        return +value


@dataclass(frozen=True)
class IVal:
    """闭区间 [lo, hi]。"""

    lo: Decimal
    hi: Decimal
    precision: int

    @staticmethod
    def point(value: Decimal | int | str, precision: int) -> "IVal":
        d = Decimal(value)
        return IVal(down(d, precision), up(d, precision), precision)

    def add(self, other: "IVal") -> "IVal":
        with localcontext() as ctx:
            ctx.prec = self.precision
            ctx.rounding = ROUND_FLOOR
            lo = self.lo + other.lo
            ctx.rounding = ROUND_CEILING
            hi = self.hi + other.hi
        return IVal(lo, hi, self.precision)

    def sub(self, other: "IVal") -> "IVal":
        with localcontext() as ctx:
            ctx.prec = self.precision
            ctx.rounding = ROUND_FLOOR
            lo = self.lo - other.hi
            ctx.rounding = ROUND_CEILING
            hi = self.hi - other.lo
        return IVal(lo, hi, self.precision)

    def neg(self) -> "IVal":
        return IVal(-self.hi, -self.lo, self.precision)

    def mul(self, other: "IVal") -> "IVal":
        vals = [self.lo * other.lo, self.lo * other.hi, self.hi * other.lo, self.hi * other.hi]
        with localcontext() as ctx:
            ctx.prec = self.precision
            ctx.rounding = ROUND_FLOOR
            lo = +min(vals)
            ctx.rounding = ROUND_CEILING
            hi = +max(vals)
        return IVal(lo, hi, self.precision)

    def div(self, other: "IVal") -> "IVal":
        if other.lo <= 0 <= other.hi:
            raise ValueError("division by interval containing zero")
        recip_vals = [Decimal(1) / other.lo, Decimal(1) / other.hi]
        recip = IVal(min(recip_vals), max(recip_vals), self.precision)
        return self.mul(recip)

    def ln(self) -> "IVal":
        if self.lo <= 0:
            raise ValueError("log of non-positive interval")
        with localcontext() as ctx:
            ctx.prec = self.precision
            ctx.rounding = ROUND_FLOOR
            lo = self.lo.ln()
            ctx.rounding = ROUND_CEILING
            hi = self.hi.ln()
        return IVal(lo, hi, self.precision)

    def exp(self) -> "IVal":
        with localcontext() as ctx:
            ctx.prec = self.precision
            ctx.rounding = ROUND_FLOOR
            lo = self.lo.exp()
            ctx.rounding = ROUND_CEILING
            hi = self.hi.exp()
        return IVal(lo, hi, self.precision)

    def pow_const(self, exponent: Decimal) -> "IVal":
        return IVal.point(exponent, self.precision).mul(self.ln()).exp()


def coeffs_for_a(x: IVal, a: int, tau: list[int], prefix: list[int]) -> tuple[IVal, ...]:
    """单 a 系数区间；floor 用整个 x 区间检查固定性。"""
    k1_lo = int(x.lo // Decimal(a)); k1_hi = int(x.hi // Decimal(a))
    k2_lo = int((Decimal(2) * x.lo) // Decimal(a)); k2_hi = int((Decimal(2) * x.hi) // Decimal(a))
    if k1_lo != k1_hi or k2_lo != k2_hi:
        raise ValueError(f"floor not fixed for a={a}: {k1_lo},{k1_hi},{k2_lo},{k2_hi}")
    p = x.precision
    weight = IVal.point(tau[a], p)
    inv = weight.div(IVal.point(a, p))
    loga = IVal.point(a, p).ln()
    ln2 = IVal.point(2, p).ln()
    gamma = IVal.point(GAMMA_STR, p)
    c_const = IVal.point(2, p).mul(weight).mul(IVal.point(prefix[k1_lo], p))
    c_s_log = IVal.point(2, p).mul(inv)
    c_s0 = IVal.point(2, p).mul(inv).mul(IVal.point(2, p).mul(gamma).sub(IVal.point(1, p)).sub(loga))
    o_const = IVal.point(2, p).mul(weight).mul(IVal.point(prefix[k2_lo], p))
    o_s_log = IVal.point(4, p).mul(inv)
    o_s0 = IVal.point(4, p).mul(inv).mul(IVal.point(2, p).mul(gamma).sub(IVal.point(1, p)).add(ln2).sub(loga))
    return c_const, c_s_log, c_s0, o_const, o_s_log, o_s0


def term_vfs(x: IVal, a: int, q: IVal, tau: list[int], prefix: list[int]) -> tuple[IVal, IVal, IVal]:
    """单 a 的 value/first/second 区间。"""
    p = x.precision
    c_const, c_s_log, c_s0, o_const, o_s_log, o_s0 = coeffs_for_a(x, a, tau, prefix)
    logx = x.ln()
    c_val = c_const.sub(x.mul(c_s_log.mul(logx).add(c_s0)))
    o_val = o_const.sub(x.mul(o_s_log.mul(logx).add(o_s0)))
    c_der = c_s_log.mul(logx.add(IVal.point(1, p))).add(c_s0).neg()
    o_der = o_s_log.mul(logx.add(IVal.point(1, p))).add(o_s0).neg()
    x_m075 = x.pow_const(Decimal("-0.75"))
    x_m175 = x.pow_const(Decimal("-1.75"))
    x_m275 = x.pow_const(Decimal("-2.75"))
    two_x_m075 = IVal.point(2, p).mul(x).pow_const(Decimal("-0.75"))
    value = o_val.mul(two_x_m075).sub(q.mul(c_val).mul(x_m075))
    old_factor = IVal.point(2, p).pow_const(Decimal("-0.75"))
    first = old_factor.mul(o_der.mul(x_m075).sub(IVal.point("0.75", p).mul(o_val).mul(x_m175))).sub(
        q.mul(c_der.mul(x_m075).sub(IVal.point("0.75", p).mul(c_val).mul(x_m175)))
    )
    pp = Decimal("0.75")
    old_factor_core = IVal.point(2, p).pow_const(-pp)
    c0 = old_factor_core.mul(IVal.point(pp * (pp + 1), p).mul(o_const)).sub(q.mul(IVal.point(pp * (pp + 1), p).mul(c_const)))
    c1 = old_factor_core.mul(IVal.point(pp * (1 - pp), p).mul(o_s_log)).sub(q.mul(IVal.point(pp * (1 - pp), p).mul(c_s_log)))
    c2_old = IVal.point(pp * (1 - pp), p).mul(o_s0).add(IVal.point(2 * pp - 1, p).mul(o_s_log))
    c2_new = IVal.point(pp * (1 - pp), p).mul(c_s0).add(IVal.point(2 * pp - 1, p).mul(c_s_log))
    c2 = old_factor_core.mul(c2_old).sub(q.mul(c2_new))
    core = c0.add(x.mul(c1.mul(logx).add(c2)))
    second = x_m275.mul(core)
    return value, first, second


def group_vfs(x: IVal, group: dict, q: IVal, tau: list[int], prefix: list[int]) -> tuple[IVal, IVal, IVal]:
    p = x.precision
    total = (IVal.point(0, p), IVal.point(0, p), IVal.point(0, p))
    for a in group["a_values"]:
        vals = term_vfs(x, a, q, tau, prefix)
        total = tuple(total[i].add(vals[i]) for i in range(3))
    return total


def functional_second(kind: str, x: IVal, memberships: dict, q: IVal, tau: list[int], prefix: list[int]) -> IVal:
    p = x.precision
    groups = memberships["L"] if kind in {"E2", "potential"} else memberships[kind]
    terms = [group_vfs(x, group, q, tau, prefix) for group in groups]
    L = IVal.point(0, p); L1 = IVal.point(0, p); L2 = IVal.point(0, p)
    for value, first, second in terms:
        L = L.add(value); L1 = L1.add(first); L2 = L2.add(second)
    if kind in {"U", "V", "light_L", "L"}:
        return L2
    E2_2 = IVal.point(0, p)
    for value, first, second in terms:
        E2_2 = E2_2.add(IVal.point(2, p).mul(first.mul(first).add(value.mul(second))))
    if kind == "E2":
        return E2_2
    return E2_2.sub(L1.mul(L1).add(L.mul(L2)).div(IVal.point(10, p)))


def audit(x_anchor: int, kind: str, left: float, right: float, precision: int) -> dict:
    tau, prefix = layer_cert.build(2 * (math.ceil(right) + 2))
    memberships = fm.row_membership_sets(x_anchor, 400, 0.958, 60, 80, tau, prefix)
    q = IVal.point("0.958", precision)
    l = Decimal(str(left)); r = Decimal(str(right))
    # 审计整个子区间，不再只审计采样点。
    x_interval = IVal(l, r, precision)
    sec = functional_second(kind, x_interval, memberships, q, tau, prefix)
    return {
        "x_anchor": x_anchor,
        "functional": kind,
        "interval": [str(l), str(r)],
        "precision": precision,
        "enclosure": [str(sec.lo), str(sec.hi)],
        "sign_certified": sec.lo > 0 or sec.hi < 0,
        "signed_margin": str(sec.lo if sec.lo > 0 else (-sec.hi if sec.hi < 0 else Decimal(0))),
        "width": str(sec.hi - sec.lo),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--x", type=int, default=1088499)
    parser.add_argument("--functional", default="V")
    parser.add_argument("--left", type=float, default=1088499.4687500312)
    parser.add_argument("--right", type=float, default=1088499.4999999688)
    parser.add_argument("--precision", type=int, default=80)
    parser.add_argument("--json", type=Path, default=Path("docs/d4-r5-outward-interval-audit-worst.json"))
    args = parser.parse_args()
    payload = audit(args.x, args.functional, args.left, args.right, args.precision)
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
