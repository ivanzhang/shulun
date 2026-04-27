#!/usr/bin/env python3
"""比较不同轮筛 δ 下的一般化框架指标。

用法示例：
  python3 experiments/compare_delta_framework.py --primes 1000003,3000017 --cols 60 --deltas 6,30,210 --C 8

输出每个 δ 的：U、M、R、Prime、C_mid、最大粗簇长度等平均/极值，
用于选择最适合证明框架的轮筛参数。
"""
import argparse
import importlib.util
import math
import random
from collections import defaultdict
from pathlib import Path

base = Path(__file__).resolve().parent
spec_vb = importlib.util.spec_from_file_location("verify_buchstab", base / "verify_buchstab.py")
vb = importlib.util.module_from_spec(spec_vb)
spec_vb.loader.exec_module(vb)


def build_primes(max_P, max_C, min_delta):
    """生成素数表。"""
    max_L = int(max_C * math.log(max_P) ** 2 / min_delta) + 20
    max_N = max_P + min_delta * max_P * max_L + 1000 * max_P
    return vb.primes_upto_from_sieve(vb.sieve(math.isqrt(max_N) + 10000))


def allowed_residues(P, c, delta):
    """返回允许残基。"""
    return [r for r in range(delta) if math.gcd(c + r * P, delta) == 1]


def lpf(n, primes):
    """返回最小素因子。"""
    for p in primes:
        if p * p > n:
            return n
        if n % p == 0:
            return p
    return n


def max_run(labels, target):
    """计算最大连续块。"""
    best = 0
    current = 0
    for label in labels:
        if label == target:
            current += 1
            best = max(best, current)
        else:
            current = 0
    return best


def chain_metrics(P, c, r, delta, C, primes):
    """计算单链一般化指标。"""
    L = int(C * math.log(P) ** 2 / delta)
    Y = next((p for p in primes if p >= math.sqrt(max(2, L))), 2)
    A = c + r * P
    step = delta * P
    small = [p for p in primes if p <= Y and math.gcd(p, step) == 1]
    U = M = R = Prime = 0
    labels = []
    for n in range(L + 1):
        N = A + step * n
        if any(N % p == 0 for p in small):
            labels.append("S")
            continue
        U += 1
        if vb.is_prime_mr(N):
            Prime += 1
            labels.append("P")
            continue
        least = lpf(N, primes)
        if least > L:
            R += 1
            labels.append("R")
        else:
            M += 1
            labels.append("M")
    C_mid = sum(L // q + 1 for q in primes if Y < q <= L and math.gcd(q, step) == 1)
    return {
        "L": L,
        "Y": Y,
        "U": U,
        "M": M,
        "R": R,
        "Prime": Prime,
        "C_mid": C_mid,
        "max_R_run": max_run(labels, "R"),
        "gap": U - M - R,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--primes", default="1000003,3000017,10000019")
    parser.add_argument("--cols", type=int, default=60)
    parser.add_argument("--deltas", default="6,30,210")
    parser.add_argument("--C", type=float, default=8.0)
    args = parser.parse_args()

    Ps = [int(x) for x in args.primes.split(",") if x.strip()]
    deltas = [int(x) for x in args.deltas.split(",") if x.strip()]
    primes = build_primes(max(Ps), args.C, min(deltas))
    buckets = defaultdict(list)
    for P in Ps:
        random.seed(P)
        cols = list(dict.fromkeys([1, 2, 6, 30, P // 2, P - 1] + random.sample(range(1, P), min(args.cols, P - 1))))
        for delta in deltas:
            if math.gcd(P, delta) != 1:
                continue
            for c in cols:
                for r in allowed_residues(P, c, delta):
                    buckets[delta].append(chain_metrics(P, c, r, delta, args.C, primes))

    print("delta,count,avg_L,avg_U,avg_M,avg_R,avg_Prime,avg_Cmid,min_Prime,max_R_run,max_Cmid_minus_M")
    for delta in deltas:
        rows = buckets[delta]
        if not rows:
            continue
        def avg(key):
            return sum(row[key] for row in rows) / len(rows)
        print(
            f"{delta},{len(rows)},{avg('L'):.2f},{avg('U'):.2f},{avg('M'):.2f},{avg('R'):.2f},"
            f"{avg('Prime'):.2f},{avg('C_mid'):.2f},{min(row['Prime'] for row in rows)},"
            f"{max(row['max_R_run'] for row in rows)},{max(row['C_mid'] - row['M'] for row in rows)}"
        )


if __name__ == "__main__":
    main()
