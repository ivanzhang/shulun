#!/usr/bin/env python3
"""扫描小筛幸存序列 U 中的连续合数块。

用法示例：
  python3 experiments/u_sequence_composite_blocks.py --primes 1000003,3000017 --cols 80 --C 8 --delta 30

区别：普通 n 坐标中的 S 点会打断块，但 S 不属于 U。证明素数存在要在 U 序列里证明不能全是 M/R。
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


def block_lengths(labels, composite_labels):
    """在 U 标签序列中计算连续合数块。"""
    blocks = []
    start = None
    for idx, label in enumerate(labels + ["P"]):
        if label in composite_labels and start is None:
            start = idx
        elif label not in composite_labels and start is not None:
            blocks.append((start, idx - 1, idx - start))
            start = None
    return blocks


def record_for(P, c, r, delta, C, primes):
    """计算 U 序列合数块记录。"""
    L = int(C * math.log(P) ** 2 / delta)
    Y = gap.next_prime_ge(math.sqrt(max(2, L)), primes)
    A = c + r * P
    step = delta * P
    small = [p for p in primes if p <= Y and math.gcd(p, step) == 1]
    u_positions = []
    u_labels = []
    for n in range(L + 1):
        N = A + step * n
        if any(N % p == 0 for p in small):
            continue
        u_positions.append(n)
        if vb.is_prime_mr(N):
            u_labels.append("P")
        else:
            least = lpf(N, primes)
            u_labels.append("R" if least > L else "M")
    comp_blocks = block_lengths(u_labels, {"M", "R"})
    rough_blocks = block_lengths(u_labels, {"R"})
    max_comp = max((b[2] for b in comp_blocks), default=0)
    max_rough = max((b[2] for b in rough_blocks), default=0)
    first_prime_idx = next((idx for idx, label in enumerate(u_labels) if label == "P"), None)
    first_prime_n = u_positions[first_prime_idx] if first_prime_idx is not None else None
    return {
        "P": P,
        "c": c,
        "r": r,
        "L": L,
        "Y": Y,
        "U": len(u_labels),
        "Prime": u_labels.count("P"),
        "M": u_labels.count("M"),
        "R": u_labels.count("R"),
        "max_U_comp_block": max_comp,
        "max_U_rough_block": max_rough,
        "first_prime_idx": first_prime_idx,
        "first_prime_n": first_prime_n,
        "u_label_prefix": "".join(u_labels[:100]),
        "u_pos_prefix": u_positions[:40],
        "comp_blocks": comp_blocks[:10],
    }


def print_record(rec, detail=False):
    """打印记录。"""
    keys = ["P", "c", "r", "L", "Y", "U", "Prime", "M", "R", "max_U_comp_block", "max_U_rough_block", "first_prime_idx", "first_prime_n"]
    print(",".join(f"{k}={rec[k]}" for k in keys))
    if detail:
        print(f"u_labels={rec['u_label_prefix']}")
        print(f"u_positions={rec['u_pos_prefix']}")
        print(f"comp_blocks={rec['comp_blocks']}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--P", type=int, default=0)
    parser.add_argument("--c", type=int, default=0)
    parser.add_argument("--r", type=int, default=0)
    parser.add_argument("--scan", action="store_true")
    parser.add_argument("--primes", default="1000003,3000017,10000019")
    parser.add_argument("--cols", type=int, default=80)
    parser.add_argument("--C", type=float, default=8.0)
    parser.add_argument("--delta", type=int, default=30)
    args = parser.parse_args()

    Ps = [int(x) for x in args.primes.split(",") if x.strip()] if args.scan else [args.P]
    if not args.scan and (not args.P or not args.c):
        raise SystemExit("非扫描模式需要 --P 与 --c，或使用 --scan")
    primes = build_primes(Ps, args.C, args.delta)
    rows = []
    for P in Ps:
        if args.scan:
            random.seed(P)
            cols = list(dict.fromkeys([1, 2, 6, 30, P // 2, P - 1] + random.sample(range(1, P), min(args.cols, P - 1))))
            for c in cols:
                for r in gap.allowed_residues(P, c, args.delta):
                    rows.append(record_for(P, c, r, args.delta, args.C, primes))
        else:
            rows.append(record_for(P, args.c, args.r, args.delta, args.C, primes))
    if args.scan:
        rows.sort(key=lambda rec: (-rec["max_U_comp_block"], rec["Prime"], -(rec["U"])))
        print("worst U-sequence composite block records")
        for rec in rows[:30]:
            print_record(rec)
        hist = Counter(rec["max_U_comp_block"] for rec in rows)
        print(f"summary total={len(rows)} hist={dict(sorted(hist.items()))}")
    else:
        print_record(rows[0], detail=True)


if __name__ == "__main__":
    main()
