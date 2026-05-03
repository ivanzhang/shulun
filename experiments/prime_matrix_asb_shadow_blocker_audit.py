#!/usr/bin/env python3
"""ASB 后排窗口的“素数遮挡/光照”审计。

用法示例：
  python3 experiments/prime_matrix_asb_shadow_blocker_audit.py
  python3 experiments/prime_matrix_asb_shadow_blocker_audit.py --max-p 1000 --alpha 0.4 --tail-fraction 0.25
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"
DEFAULT_JSON = MONOGRAPH / "prime-matrix-asb-shadow-blocker-audit.json"
DEFAULT_MD = MONOGRAPH / "prime-matrix-asb-shadow-blocker-audit.md"


def sieve(n: int) -> bytearray:
    """返回不超过 n 的素数标记表。"""
    flags = bytearray(b"\x01") * (n + 1)
    if n >= 0:
        flags[0] = 0
    if n >= 1:
        flags[1] = 0
    p = 2
    while p * p <= n:
        if flags[p]:
            start = p * p
            flags[start : n + 1 : p] = b"\x00" * (((n - start) // p) + 1)
        p += 1
    return flags


def primes_upto(n: int) -> list[int]:
    """列出不超过 n 的素数。"""
    flags = sieve(n)
    return [i for i in range(2, n + 1) if flags[i]]


def smallest_prime_factor(n: int) -> list[int]:
    """构造最小素因子表。"""
    spf = list(range(n + 1))
    if n >= 0:
        spf[0] = 0
    if n >= 1:
        spf[1] = 1
    p = 2
    while p * p <= n:
        if spf[p] == p:
            for m in range(p * p, n + 1, p):
                if spf[m] == m:
                    spf[m] = p
        p += 1
    return spf


def row_interval(width: int, row: int) -> tuple[int, int]:
    """返回方阵第 row 行对应的闭区间。"""
    return (row - 1) * width + 1, row * width


def contains_full_p_row(p: int, left: int, right: int) -> bool:
    """判断区间是否含完整旧 p 行。"""
    first_t = (left - 1 + p - 1) // p
    block_left = first_t * p + 1
    block_right = (first_t + 1) * p
    return block_left >= left and block_right <= right


def distinct_prime_factors(n: int, spf: list[int]) -> list[int]:
    """返回 n 的不同素因子。"""
    factors: list[int] = []
    while n > 1:
        p = spf[n]
        factors.append(p)
        while n % p == 0:
            n //= p
    return factors


def high_factor_count(n: int, z: int, p: int, spf: list[int]) -> int:
    """统计 n 的不同高素因子数量。"""
    return sum(1 for factor in distinct_prime_factors(n, spf) if z < factor <= p)


def analyze_window(left: int, right: int, z: int, p: int, prime_flags: bytearray, spf: list[int]) -> dict[str, Any]:
    """分析单个 ASB 后排窗口的粗剩余和高素点覆盖。"""
    rough_count = 0
    rough_prime_count = 0
    high_incidence = 0
    high_covered_points = 0
    max_high_multiplicity = 0
    first_rough_prime = None
    for n in range(left, right + 1):
        if spf[n] <= z:
            continue
        rough_count += 1
        if prime_flags[n]:
            rough_prime_count += 1
            if first_rough_prime is None:
                first_rough_prime = n
            continue
        multiplicity = high_factor_count(n, z, p, spf)
        high_incidence += multiplicity
        if multiplicity:
            high_covered_points += 1
            max_high_multiplicity = max(max_high_multiplicity, multiplicity)
    return {
        "rough_count": rough_count,
        "rough_prime_count": rough_prime_count,
        "high_incidence": high_incidence,
        "high_covered_points": high_covered_points,
        "incidence_ratio": None if rough_count == 0 else high_incidence / rough_count,
        "covered_point_ratio": None if rough_count == 0 else high_covered_points / rough_count,
        "rough_prime_ratio": None if rough_count == 0 else rough_prime_count / rough_count,
        "max_high_multiplicity": max_high_multiplicity,
        "first_rough_prime": first_rough_prime,
    }


def analyze_pair(
    p: int,
    q: int,
    alpha: float,
    tail_fraction: float,
    prime_flags: bytearray,
    spf: list[int],
) -> dict[str, Any]:
    """分析一对相邻素数的后排 ASB 窗口。"""
    g = q - p
    z = max(2, int(p**alpha))
    old_square = p * p
    last_full_q_row = old_square // q
    tail_start = max(1, int((1.0 - tail_fraction) * last_full_q_row))
    samples = []
    for s in range(tail_start, last_full_q_row + 1):
        left, right = row_interval(q, s)
        if contains_full_p_row(p, left, right):
            continue
        r = (left - 1) % p
        if r <= g:
            continue
        window = analyze_window(left, right, z, p, prime_flags, spf)
        window.update({"q_row": s, "left": left, "right": right, "r": r})
        samples.append(window)

    if not samples:
        return {
            "p": p,
            "q": q,
            "gap": g,
            "z": z,
            "tail_samples": 0,
            "max_incidence_ratio": None,
            "worst_incidence_window": None,
            "min_rough_prime_ratio": None,
            "worst_prime_window": None,
        }

    incidence_samples = [sample for sample in samples if sample["incidence_ratio"] is not None]
    prime_samples = [sample for sample in samples if sample["rough_prime_ratio"] is not None]
    worst_incidence = max(incidence_samples, key=lambda sample: sample["incidence_ratio"], default=None)
    worst_prime = min(prime_samples, key=lambda sample: sample["rough_prime_ratio"], default=None)
    return {
        "p": p,
        "q": q,
        "gap": g,
        "z": z,
        "tail_samples": len(samples),
        "max_incidence_ratio": None if worst_incidence is None else worst_incidence["incidence_ratio"],
        "worst_incidence_window": worst_incidence,
        "min_rough_prime_ratio": None if worst_prime is None else worst_prime["rough_prime_ratio"],
        "worst_prime_window": worst_prime,
    }


def build_audit(max_p: int, alpha: float, tail_fraction: float) -> dict[str, Any]:
    """生成遮挡/覆盖审计。"""
    base_primes = [p for p in primes_upto(max_p + 200) if p >= 3]
    max_q = base_primes[-1]
    max_n = max_q * max_q
    prime_flags = sieve(max_n)
    spf = smallest_prime_factor(max_n)
    cases = []
    for p, q in zip(base_primes, base_primes[1:]):
        if p > max_p:
            break
        cases.append(analyze_pair(p, q, alpha, tail_fraction, prime_flags, spf))

    worst_incidence_case = max(
        (case for case in cases if case["max_incidence_ratio"] is not None),
        key=lambda case: case["max_incidence_ratio"],
        default=None,
    )
    worst_prime_case = min(
        (case for case in cases if case["min_rough_prime_ratio"] is not None),
        key=lambda case: case["min_rough_prime_ratio"],
        default=None,
    )
    return {
        "certificate_type": "prime_matrix_asb_shadow_blocker_audit",
        "status": "shadow_is_capacity_not_direct_blocker",
        "parameters": {"max_p": max_p, "alpha": alpha, "tail_fraction": tail_fraction},
        "case_count": len(cases),
        "total_tail_samples": sum(case["tail_samples"] for case in cases),
        "worst_incidence_case": worst_incidence_case,
        "worst_prime_case": worst_prime_case,
        "cases": cases,
        "review_conclusion": (
            "同余斜线不会被上方非同余素数直接阻断；直接遮挡图像不是严格证明。"
            "可保留的严格内容是容量遮挡：低筛粗剩余中的实际素数是高素线无法覆盖的点，"
            "ASB-Fail 要求这些点全部消失，因此等价地要求高素有效点覆盖率达到 1。"
        ),
    }


def render_markdown(audit: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    params = audit["parameters"]
    lines = [
        "# ASB 后排窗口的素数遮挡审计",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        "本报告审查“后排行若被斜线完全覆盖，斜线是否必须穿过上方已确定素数而矛盾”的想法。结论分两层：直接几何遮挡不是严格同余证明；但它有一个严格版本，即低筛粗剩余中的素数会造成高素点覆盖容量缺口。",
        "",
        "## 1. 直接遮挡为何不能直接使用",
        "",
        "若某条斜线表示素数 `ell` 的整除类，则该线上的整数都满足 `n≡0 mod ell`。除源点 `ell` 本身外，线上不可能出现另一个素数。因此一条同余斜线覆盖后方合数时，并不会在同一同余线上穿过一个非同余素数；上方素数不是硬障碍物。",
        "",
        "所以“光线穿过上方素数”只有在几何画线意义下直观成立；若要成为证明，必须改写成同余/容量语言。",
        "",
        "## 2. 可保留的严格遮挡版本",
        "",
        "取 `z=p^alpha`，低筛粗剩余为",
        "",
        "\\[",
        "R_z(J)=\\{n\\in J:(n,\\prod_{\\ell\\le z}\\ell)=1\\}.",
        "\\]",
        "",
        "`R_z(J)` 中若存在素数，则该点不能被任何 `z<ell<=p` 的高素线覆盖。于是这些素数就是严格意义上的“容量遮挡点”。`ASB-Fail` 要求 `J` 无素数，因此要求 `R_z(J)` 中每个点都被高素因子覆盖，即高素有效点覆盖率至少为 `1`。",
        "",
        "## 3. 后排窗口样本",
        "",
        f"- 参数：`max_p={params['max_p']}`，`alpha={params['alpha']}`，`tail_fraction={params['tail_fraction']}`。",
        f"- 后排 ASB 样本数：`{audit['total_tail_samples']}`。",
        "",
    ]
    worst_incidence = audit["worst_incidence_case"]
    if worst_incidence:
        win = worst_incidence["worst_incidence_window"]
        lines += [
            "最大高素相对命中样本：",
            "",
            f"- `p={worst_incidence['p']}, q={worst_incidence['q']}, z={worst_incidence['z']}`。",
            f"- 区间 `[{win['left']},{win['right']}]`，`q_row={win['q_row']}`，残基 `r={win['r']}`。",
            f"- `rough_count={win['rough_count']}`，`rough_prime_count={win['rough_prime_count']}`。",
            f"- `high_incidence={win['high_incidence']}`，命中率 `{win['incidence_ratio']:.6f}`。",
            "",
        ]
    worst_prime = audit["worst_prime_case"]
    if worst_prime:
        win = worst_prime["worst_prime_window"]
        lines += [
            "最弱粗剩余素数遮挡样本：",
            "",
            f"- `p={worst_prime['p']}, q={worst_prime['q']}, z={worst_prime['z']}`。",
            f"- 区间 `[{win['left']},{win['right']}]`。",
            f"- 粗剩余素数比例 `{win['rough_prime_ratio']:.6f}`，首个粗剩余素数 `{win['first_rough_prime']}`。",
            "",
        ]
    lines += [
        "## 4. 对 ASB-RHC 的影响",
        "",
        "遮挡思想不能替代 `ASB-RHC`，但它解释了 `ASB-RHC` 的正确方向：不要证明斜线在几何上不能穿过素数，而要证明低筛粗剩余中保留下来的素数/准素数容量，使高素线的有效点覆盖率达不到 `1`。",
        "",
        "本次实验还暴露一个必要修正：裸总 incidence 不是正确目标。若 `high_incidence/rough_count` 超过 `1`，则总 incidence 上界已经失败。必须改成并集点覆盖：",
        "",
        "\\[",
        "|D_z(J)|",
        "\\le (1-\\eta)|R_z(J)|.",
        "\\]",
        "",
        "## 5. 审稿结论",
        "",
        audit["review_conclusion"],
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-p", type=int, default=1000)
    parser.add_argument("--alpha", type=float, default=0.4)
    parser.add_argument("--tail-fraction", type=float, default=0.25)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    audit = build_audit(args.max_p, args.alpha, args.tail_fraction)
    args.json_out.write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")
    args.md_out.write_text(render_markdown(audit) + "\n")
    print(args.json_out)
    print(args.md_out)


if __name__ == "__main__":
    main()
