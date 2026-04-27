#!/usr/bin/env python3
"""剖析 30P 链中的逆元粗补洞结构。

用法示例：
  python3 experiments/analyze_inverse_holes.py --P 3000017 --c 458685 --r 8 --L 80 --Y 7
  python3 experiments/analyze_inverse_holes.py --P 3000017 --c 2148110 --r 27 --C 8 --Y-mode sqrtL

输出重点：
  U：小筛幸存点；B：完整粗合数补洞点；Prime=U-B。
  collision_energy：补洞在短区间的聚集能量，越大表示越可能试图填满空隙。
  q_reuse：同一 q 多次补洞的次数分布。
"""
import argparse
import importlib.util
import math
from collections import Counter, defaultdict
from pathlib import Path

spec = importlib.util.spec_from_file_location("verify_buchstab", Path(__file__).with_name("verify_buchstab.py"))
vb = importlib.util.module_from_spec(spec)
spec.loader.exec_module(vb)


def next_prime_ge(value, primes):
    """返回不小于 value 的第一个素数。"""
    for prime in primes:
        if prime >= value:
            return prime
    return primes[-1]


def collect_structure(P, c, r, delta, L, Y, primes):
    """收集小筛幸存点与完整粗补洞点。"""
    A = c + r * P
    step = delta * P
    max_N = A + step * L
    small_primes = [prime for prime in primes if prime <= Y and math.gcd(prime, step) == 1]

    U = []
    for n in range(L + 1):
        N = A + step * n
        if N >= 2 and all(N % prime for prime in small_primes):
            U.append(n)

    holes_by_n = defaultdict(list)
    max_q = math.isqrt(max_N) + 1
    for q in primes:
        if q <= Y:
            continue
        if q > max_q:
            break
        if math.gcd(q, step) != 1:
            continue
        residue = (-A * pow(step, -1, q)) % q
        for n in range(residue, L + 1, q):
            N = A + step * n
            h = N // q
            if N % q == 0 and h >= q and vb.rough_ge(h, q, primes):
                holes_by_n[n].append((q, h))

    B = sorted(n for n in U if n in holes_by_n)
    primes_in_U = [n for n in U if n not in holes_by_n and vb.is_prime_mr(A + step * n)]
    mismatch = [n for n in U if n not in holes_by_n and not vb.is_prime_mr(A + step * n)]
    return A, step, U, B, primes_in_U, mismatch, holes_by_n


def gap_profile(points):
    """计算点集间距轮廓。"""
    if len(points) < 2:
        return []
    return [right - left for left, right in zip(points, points[1:])]


def window_energy(points, L, windows):
    """计算多个窗口尺度下的最大局部占用。"""
    point_set = set(points)
    result = {}
    for width in windows:
        if width <= 0:
            continue
        best = 0
        best_start = 0
        current = sum(1 for n in range(0, min(L, width) + 1) if n in point_set)
        best = current
        for start in range(1, L + 1):
            left = start - 1
            right = start + width
            if left in point_set:
                current -= 1
            if right <= L and right in point_set:
                current += 1
            if current > best:
                best = current
                best_start = start
        result[width] = (best, best_start)
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--P", type=int, required=True)
    parser.add_argument("--c", type=int, required=True)
    parser.add_argument("--r", type=int, required=True)
    parser.add_argument("--delta", type=int, default=30)
    parser.add_argument("--C", type=float, default=8.0)
    parser.add_argument("--L", type=int, default=0)
    parser.add_argument("--Y-mode", choices=["sqrtL", "logP", "fixed"], default="sqrtL")
    parser.add_argument("--Y", type=int, default=0)
    parser.add_argument("--top", type=int, default=30)
    args = parser.parse_args()

    L = args.L or int(args.C * math.log(args.P) ** 2 / args.delta)
    max_N = args.c + args.r * args.P + args.delta * args.P * L
    primes = vb.primes_upto_from_sieve(vb.sieve(math.isqrt(max_N) + 5000))
    if args.Y_mode == "sqrtL":
        Y = next_prime_ge(math.sqrt(max(2, L)), primes)
    elif args.Y_mode == "logP":
        Y = next_prime_ge(math.log(args.P), primes)
    else:
        Y = args.Y

    A, step, U, B, prime_points, mismatch, holes_by_n = collect_structure(
        args.P, args.c, args.r, args.delta, L, Y, primes
    )
    q_counter = Counter(q for n in B for q, _ in holes_by_n[n])
    h_rough_blocks = Counter(1 << (h.bit_length() - 1) for n in B for _, h in holes_by_n[n])
    b_gaps = gap_profile(B)
    u_gaps = gap_profile(U)
    windows = sorted(set([1, 2, 3, 5, 8, 13, int(math.sqrt(max(2, L))), max(1, L // 4), max(1, L // 2)]))
    b_energy = window_energy(B, L, windows)
    u_energy = window_energy(U, L, windows)

    print(f"P={args.P} c={args.c} r={args.r} delta={args.delta} L={L} Y={Y}")
    print(f"A={A} step={step}")
    print(f"U={len(U)} B={len(B)} primes={len(prime_points)} U-B={len(U)-len(B)} mismatch={len(mismatch)}")
    print(f"prime_points={prime_points[:args.top]}")
    print(f"U_points={U[:args.top]}")
    print(f"B_points={B[:args.top]}")
    print(f"U_gaps_first={u_gaps[:args.top]}")
    print(f"B_gaps_first={b_gaps[:args.top]}")
    print("window,width:B_best@start/U_best@start")
    for width in windows:
        print(f"{width}:{b_energy[width][0]}@{b_energy[width][1]}/{u_energy[width][0]}@{u_energy[width][1]}")
    print("q_reuse_top=q,count")
    for q, count in q_counter.most_common(args.top):
        print(f"{q},{count}")
    print("h_power2_blocks=block,count")
    for block, count in sorted(h_rough_blocks.items())[:args.top]:
        print(f"{block},{count}")
    print("hole_details=n,N,q,h")
    for n in B[:args.top]:
        N = A + step * n
        for q, h in holes_by_n[n]:
            print(f"{n},{N},{q},{h}")


if __name__ == "__main__":
    main()
