#!/usr/bin/env python3
"""D4/R5 相位单元导数根隔离证书原型。

用法示例：
  python3 experiments/d4_r5_phasecell_root_certificate.py \
    --start 1088370 --end 1088375 --lo 1 --hi 400 --q 0.958 \
    --json docs/d4-r5-phasecell-root-fourpoint-sample.json

说明：
  这是最小可执行样板，用已有 D4 block contract 核的精确 floor 单元来生成
  边界点、无根区间、导数变号根盒和候选点势能表。它先服务于 R5
  phasecell-extremum 的证书格式调试；完整 R5global 批量化仍需接入层分类。
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

GAMMA = 0.5772156649015328606


def build_tau_prefix(n: int) -> tuple[list[int], list[int]]:
    """构造 tau 与求和前缀 A(n)=sum_{m<=n}tau(m)。"""
    tau = [0] * (n + 1)
    for d in range(1, n + 1):
        for m in range(d, n + 1, d):
            tau[m] += 1
    prefix = [0] * (n + 1)
    total = 0
    for i in range(1, n + 1):
        total += tau[i]
        prefix[i] = total
    return tau, prefix


def delta(prefix: list[int], y: float) -> float:
    """D4 误差核 Delta(y)。"""
    return prefix[int(math.floor(y))] - y * (math.log(y) + 2 * GAMMA - 1)


def block_constants_on_interval(x: float, lo: int, hi: int, tau: list[int], prefix: list[int]):
    """返回 floor 固定单元上的 c/old 线性-log 系数。"""
    active_hi = min(hi, math.isqrt(int(x)))
    if active_hi < lo:
        return None
    c_const = c_s_log = c_s0 = 0.0
    o_const = o_s_log = o_s0 = 0.0
    for a in range(lo, active_hi + 1):
        weight = tau[a]
        k1 = int(math.floor(x / a))
        k2 = int(math.floor(2 * x / a))
        inv = weight / a
        c_const += weight * prefix[k1]
        c_s_log += inv
        c_s0 += inv * (2 * GAMMA - 1 - math.log(a))
        o_const += weight * prefix[k2]
        o_s_log += 2 * inv
        o_s0 += 2 * inv * (2 * GAMMA - 1 + math.log(2) - math.log(a))
    return (2 * c_const, 2 * c_s_log, 2 * c_s0, 2 * o_const, 2 * o_s_log, 2 * o_s0)


def c_old_values(x: float, coeffs: tuple[float, ...]) -> tuple[float, float]:
    """在固定单元上由系数重建 c(X), old(X)。"""
    c_const, c_s_log, c_s0, o_const, o_s_log, o_s0 = coeffs
    logx = math.log(x)
    c_val = c_const - x * (c_s_log * logx + c_s0)
    o_val = o_const - x * (o_s_log * logx + o_s0)
    return c_val, o_val


def contract_value(x: float, coeffs: tuple[float, ...], q: float) -> float:
    """归一化 contract 泛函。"""
    c_val, o_val = c_old_values(x, coeffs)
    return o_val / (2 * x) ** 0.75 - q * c_val / x**0.75


def fprime_value(x: float, coeffs: tuple[float, ...], q: float) -> float:
    """contract 泛函的一阶导数。"""
    c_const, c_s_log, c_s0, o_const, o_s_log, o_s0 = coeffs
    logx = math.log(x)
    c_val, o_val = c_old_values(x, coeffs)
    c_der = -(c_s_log * (logx + 1) + c_s0)
    o_der = -(o_s_log * (logx + 1) + o_s0)
    return (2 ** -0.75) * (o_der * x**-0.75 - 0.75 * o_val * x**-1.75) - q * (
        c_der * x**-0.75 - 0.75 * c_val * x**-1.75
    )


def fdouble_core_coeffs(coeffs: tuple[float, ...], q: float) -> tuple[float, float, float]:
    """返回 F'' 的核心 C0+x(C1 log x+C2) 系数。

    因为 F''=x^{-11/4} * core(x)，正因子不影响符号。
    这给无根区间提供一个可复核的单调性证书。
    """
    c_const, c_s_log, c_s0, o_const, o_s_log, o_s0 = coeffs
    p = 0.75
    old_factor = 2 ** -p
    c0 = old_factor * p * (p + 1) * o_const - q * p * (p + 1) * c_const
    c1 = old_factor * p * (1 - p) * o_s_log - q * p * (1 - p) * c_s_log
    c2_old = p * (1 - p) * o_s0 + (2 * p - 1) * o_s_log
    c2_new = p * (1 - p) * c_s0 + (2 * p - 1) * c_s_log
    c2 = old_factor * c2_old - q * c2_new
    return c0, c1, c2


def fdouble_core_value(x: float, coeffs: tuple[float, ...], q: float) -> float:
    """计算 F'' 的符号核心。"""
    c0, c1, c2 = fdouble_core_coeffs(coeffs, q)
    return c0 + x * (c1 * math.log(x) + c2)


def fdouble_core_range(left: float, right: float, coeffs: tuple[float, ...], q: float) -> tuple[float, float, list[float]]:
    """精确枚举 core(x)=C0+x(C1 log x+C2) 在区间上的候选极值。"""
    c0, c1, c2 = fdouble_core_coeffs(coeffs, q)
    points = [left, right]
    if c1 != 0.0:
        critical = math.exp(-1.0 - c2 / c1)
        if left <= critical <= right:
            points.append(critical)
    values = [c0 + x * (c1 * math.log(x) + c2) for x in points]
    return min(values), max(values), points


def monotone_fprime_certificate(left: float, right: float, coeffs: tuple[float, ...], q: float) -> dict | None:
    """若 F'' 在区间内不变号，则证明 F' 单调。"""
    core_min, core_max, points = fdouble_core_range(left, right, coeffs, q)
    if core_min > 0.0 or core_max < 0.0:
        return {
            "method": "analytic F'' core sign",
            "fdouble_core_range": [core_min, core_max],
            "checked_points": points,
            "monotone": "increasing" if core_min > 0.0 else "decreasing",
        }
    return None


def phase_boundaries(start: int, end: int, lo: int, hi: int, include_integer_grid: bool = True) -> list[float]:
    """生成连续相位边界。

    边界包括整数网格、a^2 激活点、floor(x/a) 跳点 x=a*m、
    以及 floor(2x/a) 跳点 x=a*m/2。返回浮点数只用于数值证书；
    严格版本应把这些点保存为有理数。
    """
    candidates: set[float] = set(float(z) for z in range(start, end + 1)) if include_integer_grid else {float(start), float(end)}
    for a in range(lo, hi + 1):
        aa = float(a * a)
        if start <= aa <= end:
            candidates.add(aa)
        for factor in (1, 2):
            m_min = max(1, int(factor * start // a) - 2)
            m_max = int(factor * end // a) + 2
            for m in range(m_min, m_max + 1):
                val = a * m / factor
                if start <= val <= end:
                    candidates.add(float(val))
    ordered = sorted(candidates)
    deduped: list[float] = []
    for value in ordered:
        if not deduped or abs(value - deduped[-1]) > 1e-10:
            deduped.append(value)
    return deduped


def isolate_roots(boundaries: list[float], lo: int, hi: int, tau: list[int], prefix: list[int], q: float) -> tuple[list[dict], list[dict]]:
    """在相邻边界之间隔离导数根或记录无根区间。"""
    no_root = []
    root_boxes = []
    for left, right in zip(boundaries, boundaries[1:]):
        if right - left <= 1e-9:
            continue
        eps = max(1e-9, (right - left) * 1e-7)
        a = left + eps
        b = right - eps
        if b <= a:
            continue
        probe = (a + b) / 2
        coeffs = block_constants_on_interval(probe, lo, hi, tau, prefix)
        if coeffs is None:
            continue
        fa = fprime_value(a, coeffs, q)
        fb = fprime_value(b, coeffs, q)
        if fa == 0.0:
            root_boxes.append({"interval": [a, a], "method": "endpoint-zero", "fprime": [fa, fa]})
            continue
        if fb == 0.0:
            root_boxes.append({"interval": [b, b], "method": "endpoint-zero", "fprime": [fb, fb]})
            continue
        if fa * fb > 0:
            monotone = monotone_fprime_certificate(a, b, coeffs, q)
            if monotone is not None:
                no_root.append(
                    {
                        "interval": [a, b],
                        "method": "same-sign endpoints plus monotone F'",
                        "fprime_endpoints": [fa, fb],
                        "monotone_certificate": monotone,
                    }
                )
            else:
                no_root.append(
                    {
                        "interval": [a, b],
                        "method": "same-sign endpoints only; requires interval subdivision",
                        "fprime_endpoints": [fa, fb],
                    }
                )
            continue
        low = a
        high = b
        flow = fa
        fhigh = fb
        for _ in range(70):
            mid = (low + high) / 2
            fmid = fprime_value(mid, coeffs, q)
            if flow * fmid <= 0:
                high = mid
                fhigh = fmid
            else:
                low = mid
                flow = fmid
        root_boxes.append(
            {
                "interval": [low, high],
                "method": "bisection sign-change",
                "fprime_endpoints": [flow, fhigh],
                "probe_cell": [left, right],
            }
        )
    return no_root, root_boxes


def candidate_values(points: list[float], lo: int, hi: int, tau: list[int], prefix: list[int], q: float) -> list[dict]:
    """评估整数候选点的 contract 值。"""
    rows = []
    for x in points:
        coeffs = block_constants_on_interval(float(x), lo, hi, tau, prefix)
        if coeffs is None:
            value = 0.0
        else:
            value = contract_value(float(x), coeffs, q)
        rows.append({"x": x, "contract": value, "positive_contract": max(0.0, value)})
    return rows


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", type=int, default=1_088_370)
    parser.add_argument("--end", type=int, default=1_088_375)
    parser.add_argument("--lo", type=int, default=1)
    parser.add_argument("--hi", type=int, default=400)
    parser.add_argument("--q", type=float, default=0.958)
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()

    tau, prefix = build_tau_prefix(2 * args.end + 10)
    boundaries = phase_boundaries(args.start, args.end, args.lo, args.hi)
    no_root, root_boxes = isolate_roots(boundaries, args.lo, args.hi, tau, prefix, args.q)
    rows = candidate_values(boundaries, args.lo, args.hi, tau, prefix, args.q)
    best = max(rows, key=lambda row: row["contract"])
    payload = {
        "certificate_type": "D4-R5-phasecell-root-certificate-sample",
        "status": "prototype: validates certificate shape, not full R5global closure",
        "cell_interval": [args.start, args.end],
        "block": [args.lo, args.hi],
        "q": args.q,
        "boundary_count": len(boundaries),
        "no_root_interval_count": len(no_root),
        "root_box_count": len(root_boxes),
        "coverage": "covered by integer phase boundaries plus open intervals between consecutive boundaries",
        "best_boundary_value": best,
        "boundary_boxes": [{"x": x, "type": "integer/floor boundary candidate"} for x in boundaries],
        "no_root_subintervals": no_root[:200],
        "root_boxes": root_boxes[:200],
        "candidate_values": rows,
        "audit_note": "已支持 F'' 核不变号的单调无根证书；下一步需接入外向舍入区间算术，并把层分类 L,E2,U,V,S,Q 接入同一候选框架。",
    }
    print(json.dumps({k: v for k, v in payload.items() if k not in {"boundary_boxes", "no_root_subintervals", "root_boxes", "candidate_values"}}, ensure_ascii=False, indent=2))
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
