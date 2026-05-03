#!/usr/bin/env python3
"""锚命中层数 m_q 与 Φ=1-τ*C(n_q,2) 分层扫描。

用途示例：
  python3 experiments/anchor_hit_layer_phi_scan.py --P 2003 --c 219 --tau 0.05
"""
from __future__ import annotations

import argparse
from collections import defaultdict
from math import isqrt


def sieve(n: int) -> list[bool]:
    """返回素数布尔表。"""
    a = [True] * (n + 1)
    if n >= 0:
        a[0] = False
    if n >= 1:
        a[1] = False
    for p in range(2, isqrt(n) + 1):
        if a[p]:
            for j in range(p * p, n + 1, p):
                a[j] = False
    return a


def primes_upto(n: int) -> list[int]:
    s = sieve(n)
    return [i for i, v in enumerate(s) if v]


def factor_distinct(n: int, primes: list[int]) -> list[int]:
    out = []
    x = n
    for p in primes:
        if p * p > x:
            break
        if x % p == 0:
            out.append(p)
            while x % p == 0:
                x //= p
    if x > 1:
        out.append(x)
    return out


def bucket(q: int, d: int) -> int:
    j = 0
    x = d
    while q >= 2 * x:
        x *= 2
        j += 1
    return j


def scan(P: int, c: int, tau: float) -> dict:
    d = isqrt(P)
    pt = sieve(P * P)
    small = primes_upto(d)
    facp = primes_upto(P * P)
    anchors = defaultdict(list)
    rough = []
    for k in range(P):
        n = k * P + c
        if n >= 2 and all(n % p for p in small):
            rough.append(k)
            if not pt[n]:
                for q in factor_distinct(n, facp):
                    if d < q < P:
                        anchors[q].append(k)

    layers = defaultdict(lambda: {"Q": 0, "A": 0, "E": 0, "Phi": 0.0, "buckets": defaultdict(int)})
    for q, rows in anchors.items():
        n = len(rows)
        e = n * (n - 1) // 2
        phi = 1 - tau * e
        key = n if n < 8 else ">=8"
        layers[key]["Q"] += 1
        layers[key]["A"] += n
        layers[key]["E"] += e
        layers[key]["Phi"] += phi
        layers[key]["buckets"][bucket(q, d)] += 1

    return {
        "P": P,
        "c": c,
        "N": len(rough),
        "tau": tau,
        "layers": {
            str(k): {kk: (dict(vv) if kk == "buckets" else round(vv, 4) if isinstance(vv, float) else vv) for kk, vv in data.items()}
            for k, data in layers.items()
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--P", type=int, default=2003)
    parser.add_argument("--c", type=int, default=219)
    parser.add_argument("--tau", type=float, default=0.05)
    args = parser.parse_args()
    print(scan(args.P, args.c, args.tau))


if __name__ == "__main__":
    main()
