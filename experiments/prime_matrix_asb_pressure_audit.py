#!/usr/bin/env python3
"""ASB(p,q) 采样端点屏障压力审计。

用法示例：
  python3 experiments/prime_matrix_asb_pressure_audit.py
  python3 experiments/prime_matrix_asb_pressure_audit.py --max-p 10000
"""
from __future__ import annotations

import argparse
from bisect import bisect_left, bisect_right
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"
DEFAULT_JSON = MONOGRAPH / "prime-matrix-asb-pressure-audit.json"
DEFAULT_MD = MONOGRAPH / "prime-matrix-asb-pressure-audit.md"


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


def row_interval(width: int, row: int) -> tuple[int, int]:
    """返回方阵第 row 行对应的闭区间。"""
    return (row - 1) * width + 1, row * width


def interval_primes(primes: list[int], left: int, right: int) -> list[int]:
    """返回闭区间内的素数列表。"""
    return primes[bisect_left(primes, max(left, 2)) : bisect_right(primes, right)]


def p_row_endpoint_profile(primes: list[int], p: int, row: int) -> dict[str, int | None]:
    """返回旧 p 行的首末素数端点剖面。"""
    left, right = row_interval(p, row)
    ps = interval_primes(primes, left, right)
    if not ps:
        return {"first_pos": None, "last_pos": None, "prefix_gap": None, "suffix_gap": None}
    first_pos = ps[0] - left + 1
    last_pos = ps[-1] - left + 1
    return {
        "first_pos": first_pos,
        "last_pos": last_pos,
        "prefix_gap": first_pos - 1,
        "suffix_gap": p - last_pos,
    }


def build_profiles(primes: list[int], p: int) -> list[dict[str, int | None]]:
    """生成所有旧 p 行端点剖面。"""
    return [p_row_endpoint_profile(primes, p, row) for row in range(1, p + 1)]


def contains_full_p_row(p: int, left: int, right: int) -> bool:
    """判断区间是否含完整旧 p 行。"""
    first_t = (left - 1 + p - 1) // p
    block_left = first_t * p + 1
    block_right = (first_t + 1) * p
    return block_left >= left and block_right <= right


def analyze_pair(p: int, q: int, primes: list[int]) -> dict[str, Any]:
    """分析一对相邻素数的 ASB 采样压力。"""
    g = q - p
    profiles = build_profiles(primes, p)
    old_square = p * p
    last_full_q_row = old_square // q
    sampled = []
    failures = 0
    min_margin: int | None = None
    worst_sample: dict[str, Any] | None = None
    max_sampled_endpoint_sum: int | None = None
    worst_endpoint_sample: dict[str, Any] | None = None
    min_prime_count: int | None = None
    min_prime_count_sample: dict[str, Any] | None = None

    for s in range(1, last_full_q_row + 1):
        left, right = row_interval(q, s)
        if contains_full_p_row(p, left, right):
            continue
        start = left - 1
        r = start % p
        if r <= g:
            continue
        t = start // p + 1
        if t >= p:
            continue
        suffix_len = p - r
        prefix_len = r + g
        current = profiles[t - 1]
        nxt = profiles[t]
        suffix_gap = current["suffix_gap"]
        prefix_gap = nxt["prefix_gap"]
        suffix_margin = None if suffix_gap is None else suffix_len - int(suffix_gap)
        prefix_margin = None if prefix_gap is None else prefix_len - int(prefix_gap)
        margins = [m for m in (suffix_margin, prefix_margin) if m is not None]
        asb_margin = max(margins) if margins else None
        endpoint_sum = None if suffix_gap is None or prefix_gap is None else int(suffix_gap) + int(prefix_gap)
        ps = interval_primes(primes, left, right)
        prime_count = len(ps)
        if prime_count == 0:
            failures += 1
        witness_pos = None if not ps else ps[0] - left + 1
        witness_side = None
        if witness_pos is not None:
            witness_side = "suffix" if witness_pos <= suffix_len else "prefix"
        sample = {
            "q_row": s,
            "left": left,
            "right": right,
            "r": r,
            "t": t,
            "suffix_len": suffix_len,
            "prefix_len": prefix_len,
            "suffix_gap": suffix_gap,
            "prefix_gap": prefix_gap,
            "suffix_margin": suffix_margin,
            "prefix_margin": prefix_margin,
            "asb_margin": asb_margin,
            "endpoint_sum": endpoint_sum,
            "endpoint_sum_ratio_to_q": None if endpoint_sum is None else endpoint_sum / q,
            "prime_count": prime_count,
            "first_prime_offset": witness_pos,
            "first_prime_side": witness_side,
        }
        sampled.append(sample)
        if asb_margin is not None and (min_margin is None or asb_margin < min_margin):
            min_margin = asb_margin
            worst_sample = sample
        if endpoint_sum is not None and (
            max_sampled_endpoint_sum is None or endpoint_sum > max_sampled_endpoint_sum
        ):
            max_sampled_endpoint_sum = endpoint_sum
            worst_endpoint_sample = sample
        if min_prime_count is None or prime_count < min_prime_count:
            min_prime_count = prime_count
            min_prime_count_sample = sample

    return {
        "p": p,
        "q": q,
        "gap": g,
        "sampled_asb_windows": len(sampled),
        "actual_asb_failures": failures,
        "min_asb_margin": min_margin,
        "worst_margin_sample": worst_sample,
        "max_sampled_endpoint_sum": max_sampled_endpoint_sum,
        "max_sampled_endpoint_sum_ratio_to_q": (
            None if max_sampled_endpoint_sum is None else max_sampled_endpoint_sum / q
        ),
        "worst_endpoint_sample": worst_endpoint_sample,
        "min_prime_count": min_prime_count,
        "min_prime_count_sample": min_prime_count_sample,
        "hard_samples": sorted(
            sampled,
            key=lambda sample: (
                10**9 if sample["asb_margin"] is None else int(sample["asb_margin"]),
                sample["prime_count"],
            ),
        )[:6],
    }


def build_audit(max_p: int) -> dict[str, Any]:
    """生成 ASB 压力审计。"""
    base_primes = [p for p in primes_upto(max_p + 200) if p >= 3]
    max_q = base_primes[-1]
    all_primes = primes_upto(max_q * max_q)
    cases = []
    for p, q in zip(base_primes, base_primes[1:]):
        if p > max_p:
            break
        cases.append(analyze_pair(p, q, all_primes))

    worst_margin = min(
        (case for case in cases if case["min_asb_margin"] is not None),
        key=lambda case: case["min_asb_margin"],
        default=None,
    )
    worst_endpoint = max(
        (case for case in cases if case["max_sampled_endpoint_sum_ratio_to_q"] is not None),
        key=lambda case: case["max_sampled_endpoint_sum_ratio_to_q"],
        default=None,
    )
    min_prime_count_case = min(
        (case for case in cases if case["min_prime_count"] is not None),
        key=lambda case: case["min_prime_count"],
        default=None,
    )
    return {
        "certificate_type": "prime_matrix_asb_pressure_audit",
        "status": "asb_sampled_pressure_evidence_not_a_proof",
        "parameters": {"max_p": max_p},
        "case_count": len(cases),
        "total_sampled_asb_windows": sum(case["sampled_asb_windows"] for case in cases),
        "total_actual_asb_failures": sum(case["actual_asb_failures"] for case in cases),
        "worst_margin_case": worst_margin,
        "worst_endpoint_case": worst_endpoint,
        "min_prime_count_case": min_prime_count_case,
        "cases": cases,
        "review_conclusion": (
            "ASB 是比 SEB 更精确的采样端点屏障；样本中没有 ASB-Fail。"
            "但最小素数计数和端点余量仍只是证据，真正证明需要把 ASB-Fail 的 q 行空窗"
            "转化为小素斜线覆盖容量与 CRT 漂移相关的定量矛盾。"
        ),
    }


def render_markdown(audit: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# ASB 采样端点屏障压力审计",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        "本文档专门比较实际采样的 `ASB(p,q)` 与过强的全局 `SEB(p,q)`。`ASB` 只检查新 `q` 行边界给出的残基 `r_s=(s-1)(q-p) mod p`，因此保留了递推剥离路线的算术结构。",
        "",
        "## 1. 审计范围",
        "",
        f"- 参数：`max_p={audit['parameters']['max_p']}`。",
        f"- 相邻素数对数量：`{audit['case_count']}`。",
        f"- 实际采样 ASB 窗口总数：`{audit['total_sampled_asb_windows']}`。",
        f"- 实测 ASB-Fail 数量：`{audit['total_actual_asb_failures']}`。",
        "",
        "## 2. 最紧样本",
        "",
    ]
    worst_margin = audit["worst_margin_case"]
    if worst_margin:
        sample = worst_margin["worst_margin_sample"]
        lines += [
            f"- 最小 `ASB` 余量出现在 `p={worst_margin['p']}, q={worst_margin['q']}`。",
            f"- `asb_margin={worst_margin['min_asb_margin']}`，对应 `q` 行 `{sample['q_row']}`。",
            f"- 残基 `r={sample['r']}`，尾段长度 `{sample['suffix_len']}`，头段长度 `{sample['prefix_len']}`。",
            f"- `suffix_gap={sample['suffix_gap']}`，`prefix_gap={sample['prefix_gap']}`。",
            f"- 该窗口内实际素数数：`{sample['prime_count']}`，首个素数位于 `{sample['first_prime_side']}` 段。",
            "",
        ]
    worst_endpoint = audit["worst_endpoint_case"]
    if worst_endpoint:
        sample = worst_endpoint["worst_endpoint_sample"]
        lines += [
            f"- 最大采样端点空段和出现在 `p={worst_endpoint['p']}, q={worst_endpoint['q']}`。",
            f"- 端点空段和 `{worst_endpoint['max_sampled_endpoint_sum']}`，比值 `{worst_endpoint['max_sampled_endpoint_sum_ratio_to_q']:.6f}`。",
            f"- 对应 `q` 行 `{sample['q_row']}`，实际 `ASB` 余量 `{sample['asb_margin']}`。",
            "",
        ]
    min_prime_case = audit["min_prime_count_case"]
    if min_prime_case:
        sample = min_prime_case["min_prime_count_sample"]
        lines += [
            f"- 最小窗口素数数出现在 `p={min_prime_case['p']}, q={min_prime_case['q']}`。",
            f"- `prime_count={min_prime_case['min_prime_count']}`，对应区间 `[{sample['left']},{sample['right']}]`。",
            "",
        ]
    lines += [
        "## 3. 审稿解释",
        "",
        "实验证据显示 `ASB` 比全局 `SEB` 更贴合真实递推硬点：它只检查实际被 `q` 行边界采样到的端点组合。但该审计仍不是证明。要无条件化，需要证明不存在 `ASB-Fail`：",
        "",
        "\\[",
        "\\sigma_{t_s}\\ge p-r_s,\\qquad \\pi_{t_s+1}\\ge r_s+q-p.",
        "\\]",
        "",
        "这等价于一个长度 `q` 的新行窗口完全由合数填满。下一步硬攻必须给出覆盖容量不等式：小素斜线、相邻互质、CRT 漂移残基和旧/新双分块结构共同导致可覆盖位置数严格小于 `q`。",
        "",
        "## 4. 当前结论",
        "",
        audit["review_conclusion"],
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-p", type=int, default=10000)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    audit = build_audit(args.max_p)
    args.json_out.write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")
    args.md_out.write_text(render_markdown(audit) + "\n")
    print(args.json_out)
    print(args.md_out)


if __name__ == "__main__":
    main()
