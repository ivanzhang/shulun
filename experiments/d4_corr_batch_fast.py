#!/usr/bin/env python3
"""复用 tau/A 数组的 D4 相关和短区间端点证书批处理。"""
from __future__ import annotations

import argparse
import csv
import json
import math
from pathlib import Path

GAMMA = 0.5772156649015328606


def build_tau_prefix(n: int):
    tau = [0] * (n + 1)
    for d in range(1, n + 1):
        for m in range(d, n + 1, d):
            tau[m] += 1
    pref = [0] * (n + 1)
    run = 0
    for i in range(1, n + 1):
        run += tau[i]
        pref[i] = run
    return tau, pref


def delta_real(A: list[int], y: float) -> float:
    return A[int(math.floor(y))] - y * (math.log(y) + 2.0 * GAMMA - 1.0)


def block_bound(start: int, end: int, block: int, tau: list[int], A: list[int]) -> dict[str, float | int]:
    sqrt_r = math.isqrt(end)
    total_bound = 0.0
    best_exact = (-1e100, start)
    for lo in range(1, sqrt_r + 1, block):
        hi = min(sqrt_r, lo + block - 1)
        best_sum = -1e100
        candidates = {start, end}
        for a in range(lo, hi + 1):
            aa = a * a
            if start <= aa <= end:
                candidates.add(aa)
                if aa + 1 <= end:
                    candidates.add(aa + 1)
            m_min = max(1, start // a - 2)
            m_max = end // a + 2
            for m in range(m_min, m_max + 1):
                left = a * m
                right = a * (m + 1)
                for x0 in (left, right):
                    for z in (x0 - 1, x0, x0 + 1):
                        if start <= z <= end:
                            candidates.add(z)
        for x in candidates:
            local_hi = min(hi, math.isqrt(x))
            if local_hi < lo:
                continue
            val = sum(tau[a] * delta_real(A, x / a) for a in range(lo, local_hi + 1))
            if val > best_sum:
                best_sum = val
        total_bound += 2.0 * best_sum
    # sample exact at endpoints and multiples of 1000 for diagnostic only
    step = max(1, (end - start) // 10)
    for x in range(start, end + 1, step):
        val = 2.0 * sum(tau[a] * delta_real(A, x / a) for a in range(1, math.isqrt(x) + 1)) / (x ** 0.75)
        if val > best_exact[0]:
            best_exact = (val, x)
    return {
        "start": start,
        "end": end,
        "block": block,
        "bound_norm": total_bound / (start ** 0.75),
        "sample_norm": best_exact[0],
        "sample_x": best_exact[1],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--start", type=int, default=1_000_000)
    parser.add_argument("--end", type=int, default=1_100_000)
    parser.add_argument("--width", type=int, default=10_000)
    parser.add_argument("--block", type=int, default=200)
    parser.add_argument("--csv", type=Path, required=True)
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    tau, A = build_tau_prefix(args.end)
    rows = []
    current = args.start
    while current < args.end:
        next_end = min(args.end, current + args.width)
        row = block_bound(current, next_end, args.block, tau, A)
        rows.append(row)
        print(f"[{current},{next_end}] bound={row['bound_norm']:.9f} sample={row['sample_norm']:.9f}")
        current = next_end
    args.csv.parent.mkdir(parents=True, exist_ok=True)
    with args.csv.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["start", "end", "block", "bound_norm", "sample_norm", "sample_x"])
        writer.writeheader()
        writer.writerows(rows)
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps({"rows": rows}, ensure_ascii=False, indent=2))
    print(f"SUMMARY rows={len(rows)} max_bound={max(r['bound_norm'] for r in rows):.9f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
