#!/usr/bin/env python3
"""分析 G=粗点容量单独上界为何不足，并扫描联合容量缺口。

用法示例：
  python3 experiments/joint_capacity_defect.py --primes 1000003,3000017 --cols 80 --C 8 --delta 30

核心：
  原条件 |U| > C_mid + G 若取 G≈|R|，通常 C_mid 很松。
  真正需要利用 M 与 R 的互斥/位置结构，证明 |M|+|R|<|U|。
"""
import argparse
import importlib.util
import math
import random
from collections import Counter
from pathlib import Path

base = Path(__file__).resolve().parent
spec_vb = importlib.util.spec_from_file_location("verify_buchstab", base / "verify_buchstab.py")
vb = importlib.util.module_from_spec(spec_vb)
spec_vb.loader.exec_module(vb)

spec_gap = importlib.util.spec_from_file_location("scan_ub_gap", base / "scan_ub_gap.py")
gap = importlib.util.module_from_spec(spec_gap)
spec_gap.loader.exec_module(gap)


def build_primes(Ps, C, delta):
    """生成素数表。"""
    max_P = max(Ps)
    max_L = int(C * math.log(max_P) ** 2 / delta) + 20
    max_N = max_P + delta * max_P * max_L + delta * max_P
    return vb.primes_upto_from_sieve(vb.sieve(math.isqrt(max_N) + 10000))


def lpf(n, primes):
    """返回最小素因子。"""
    for p in primes:
        if p * p > n:
            return n
        if n % p == 0:
            return p
    return n


def max_run(labels, targets):
    """计算目标标签集合的最大连续块。"""
    best = 0
    cur = 0
    for label in labels:
        if label in targets:
            cur += 1
            best = max(best, cur)
        else:
            cur = 0
    return best


def record_for(P, c, r, delta, C, primes):
    """计算单链联合容量指标。"""
    L = int(C * math.log(P) ** 2 / delta)
    Y = gap.next_prime_ge(math.sqrt(max(2, L)), primes)
    A = c + r * P
    step = delta * P
    small = [p for p in primes if p <= Y and math.gcd(p, step) == 1]
    labels = []
    U = M = R = Prime = 0
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
    actual_composite = M + R
    loose_slack = C_mid + R - U
    true_gap = U - actual_composite
    return {
        "P": P,
        "c": c,
        "r": r,
        "L": L,
        "Y": Y,
        "U": U,
        "M": M,
        "R": R,
        "Prime": Prime,
        "C_mid": C_mid,
        "actual_composite": actual_composite,
        "true_gap": true_gap,
        "loose_slack": loose_slack,
        "max_composite_run": max_run(labels, {"M", "R"}),
        "max_rough_run": max_run(labels, {"R"}),
        "label_prefix": "".join(labels[:100]),
    }


def print_record(rec, detail=False):
    """打印记录。"""
    keys = ["P", "c", "r", "L", "Y", "U", "M", "R", "Prime", "C_mid", "true_gap", "loose_slack", "max_composite_run", "max_rough_run"]
    print(",".join(f"{k}={rec[k]}" for k in keys))
    if detail:
        print(f"labels={rec['label_prefix']}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--primes", default="1000003,3000017,10000019")
    parser.add_argument("--cols", type=int, default=80)
    parser.add_argument("--C", type=float, default=8.0)
    parser.add_argument("--delta", type=int, default=30)
    args = parser.parse_args()

    Ps = [int(x) for x in args.primes.split(",") if x.strip()]
    primes = build_primes(Ps, args.C, args.delta)
    rows = []
    for P in Ps:
        random.seed(P)
        cols = list(dict.fromkeys([1, 2, 6, 30, P // 2, P - 1] + random.sample(range(1, P), min(args.cols, P - 1))))
        for c in cols:
            for r in gap.allowed_residues(P, c, args.delta):
                rows.append(record_for(P, c, r, args.delta, args.C, primes))

    rows.sort(key=lambda rec: (rec["true_gap"], -rec["loose_slack"], -rec["max_composite_run"]))
    print("worst joint capacity records")
    for rec in rows[:30]:
        print_record(rec)
    gaps = sorted(rec["true_gap"] for rec in rows)
    slacks = sorted(rec["loose_slack"] for rec in rows)
    comp_runs = Counter(rec["max_composite_run"] for rec in rows)
    print(
        "summary "
        f"total={len(rows)} min_true_gap={gaps[0]} q50_true_gap={gaps[len(gaps)//2]} "
        f"max_loose_slack={slacks[-1]} q50_loose_slack={slacks[len(slacks)//2]} "
        f"composite_run_hist={dict(sorted(comp_runs.items()))}"
    )


if __name__ == "__main__":
    main()
