#!/usr/bin/env python3
"""分析单点粗补洞的 q/h 分层与粗协因子约束。

用法示例：
  python3 experiments/singleton_cofactor_layers.py --P 3000017 --c 458685 --r 8 --C 8
  python3 experiments/singleton_cofactor_layers.py --scan --primes 1000003,3000017 --cols 80 --C 8

目标：
  把单点补洞分成 Y<q<=L 与 q>L 两类，并统计 h 的大小层、h/q 比值、
  以及 h 在小素数筛下的粗性约束强度，为单点稀疏估计寻找可证上界。
"""
import argparse
import importlib.util
import math
import random
from collections import Counter, defaultdict
from pathlib import Path

base = Path(__file__).resolve().parent
spec_vb = importlib.util.spec_from_file_location("verify_buchstab", base / "verify_buchstab.py")
vb = importlib.util.module_from_spec(spec_vb)
spec_vb.loader.exec_module(vb)

spec_gap = importlib.util.spec_from_file_location("scan_ub_gap", base / "scan_ub_gap.py")
gap = importlib.util.module_from_spec(spec_gap)
spec_gap.loader.exec_module(gap)


def build_prime_table(Ps, C, delta):
    """构建足够分解到 sqrt(N) 的素数表。"""
    max_P = max(Ps)
    max_L = int(C * math.log(max_P) ** 2 / delta) + 10
    max_N = max_P + delta * max_P * max_L + delta * max_P
    return vb.primes_upto_from_sieve(vb.sieve(math.isqrt(max_N) + 5000))


def least_factor_below(n, bound, primes):
    """返回 n 中小于 bound 的最小素因子；若没有则返回 None。"""
    for p in primes:
        if p >= bound or p * p > n:
            return None
        if n % p == 0:
            return p
    return None


def collect(P, c, r, delta, L, Y, primes):
    """收集链中所有补洞及其 q/h 信息。"""
    A = c + r * P
    step = delta * P
    max_N = A + step * L
    small = [p for p in primes if p <= Y and math.gcd(p, step) == 1]
    U = set()
    for n in range(L + 1):
        N = A + step * n
        if N >= 2 and all(N % p for p in small):
            U.add(n)

    q_to_items = defaultdict(list)
    n_to_items = defaultdict(list)
    for q in primes:
        if q <= Y:
            continue
        if q > math.isqrt(max_N) + 1:
            break
        if math.gcd(q, step) != 1:
            continue
        residue = (-A * pow(step, -1, q)) % q
        for n in range(residue, L + 1, q):
            if n not in U:
                continue
            N = A + step * n
            h = N // q
            if N % q == 0 and h >= q and vb.rough_ge(h, q, primes):
                item = (n, q, h, N)
                q_to_items[q].append(item)
                n_to_items[n].append(item)

    singleton_items = []
    skeleton_items = []
    for q, items in q_to_items.items():
        unique_ns = {item[0] for item in items}
        if len(unique_ns) == 1:
            singleton_items.extend(items)
        else:
            skeleton_items.extend(items)
    B = set(n_to_items) & U
    escapes = sorted(n for n in U - B if vb.is_prime_mr(A + step * n))
    return U, B, escapes, singleton_items, skeleton_items


def layer_record(P, c, r, delta, L, Y, primes):
    """生成单点补洞分层记录。"""
    U, B, escapes, singleton_items, skeleton_items = collect(P, c, r, delta, L, Y, primes)
    large_q = [item for item in singleton_items if item[1] > L]
    mid_q = [item for item in singleton_items if item[1] <= L]
    h_blocks = Counter(1 << (item[2].bit_length() - 1) for item in singleton_items)
    ratio_blocks = Counter(int(math.log2(max(1.0, item[2] / item[1]))) for item in singleton_items)
    q_blocks = Counter("q>L" if item[1] > L else "Y<q<=L" for item in singleton_items)
    h_mod_small_hits = Counter()
    for _, q, h, _ in singleton_items:
        # 记录若降低粗性阈值时，h 最先会被哪个小素数破坏。
        witness = least_factor_below(h, q, primes)
        h_mod_small_hits[witness or "rough"] += 1
    return {
        "P": P,
        "c": c,
        "r": r,
        "L": L,
        "Y": Y,
        "U": len(U),
        "B": len(B),
        "escapes": len(escapes),
        "first_escape": escapes[0] if escapes else None,
        "singleton": len(singleton_items),
        "single_large_q": len(large_q),
        "single_mid_q": len(mid_q),
        "skeleton_items": len(skeleton_items),
        "q_blocks": dict(q_blocks),
        "ratio_blocks": dict(sorted(ratio_blocks.items())),
        "h_blocks": dict(sorted(h_blocks.items())),
        "h_rough_witness": dict(h_mod_small_hits.most_common(12)),
        "sample_large": [(n, q, h) for n, q, h, _ in large_q[:12]],
        "sample_mid": [(n, q, h) for n, q, h, _ in mid_q[:12]],
    }


def print_record(record, detail=False):
    """打印记录。"""
    keys = [
        "P", "c", "r", "L", "Y", "U", "B", "escapes", "first_escape",
        "singleton", "single_large_q", "single_mid_q", "skeleton_items",
    ]
    print(",".join(f"{key}={record[key]}" for key in keys))
    if detail:
        print(f"q_blocks={record['q_blocks']}")
        print(f"ratio_log2_h_over_q={record['ratio_blocks']}")
        print(f"h_power2_blocks={record['h_blocks']}")
        print(f"h_rough_witness={record['h_rough_witness']}")
        print(f"sample_large={record['sample_large']}")
        print(f"sample_mid={record['sample_mid']}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--scan", action="store_true")
    parser.add_argument("--P", type=int, default=0)
    parser.add_argument("--c", type=int, default=0)
    parser.add_argument("--r", type=int, default=0)
    parser.add_argument("--primes", default="1000003,3000017,10000019")
    parser.add_argument("--cols", type=int, default=80)
    parser.add_argument("--C", type=float, default=8.0)
    parser.add_argument("--delta", type=int, default=30)
    parser.add_argument("--Y-mode", choices=["sqrtL", "logP", "fixed"], default="sqrtL")
    parser.add_argument("--Y", type=int, default=0)
    args = parser.parse_args()

    Ps = [int(x) for x in args.primes.split(",") if x.strip()] if args.scan else [args.P]
    if not args.scan and (not args.P or not args.c):
        raise SystemExit("非扫描模式需要 --P 与 --c")
    primes = build_prime_table(Ps, args.C, args.delta)
    records = []
    for P in Ps:
        L = int(args.C * math.log(P) ** 2 / args.delta)
        if args.Y_mode == "sqrtL":
            Y = gap.next_prime_ge(math.sqrt(max(2, L)), primes)
        elif args.Y_mode == "logP":
            Y = gap.next_prime_ge(math.log(P), primes)
        else:
            Y = args.Y
        if args.scan:
            random.seed(P)
            cols = list(dict.fromkeys([1, 2, 6, 30, P // 2, P - 1] + random.sample(range(1, P), min(args.cols, P - 1))))
            for c in cols:
                for r in gap.allowed_residues(P, c, args.delta):
                    records.append(layer_record(P, c, r, args.delta, L, Y, primes))
        else:
            records.append(layer_record(P, args.c, args.r, args.delta, L, Y, primes))

    if args.scan:
        records.sort(key=lambda rec: (rec["escapes"], -rec["single_large_q"], rec["first_escape"] if rec["first_escape"] is not None else -1))
        print("worst singleton layer records")
        for record in records[:30]:
            print_record(record)
        if records:
            large_ratios = sorted(rec["single_large_q"] / max(1, rec["singleton"]) for rec in records)
            print(
                "summary "
                f"total={len(records)} min_escape={min(r['escapes'] for r in records)} "
                f"large_ratio_q50={large_ratios[len(large_ratios)//2]:.3f} "
                f"large_ratio_min={large_ratios[0]:.3f} large_ratio_max={large_ratios[-1]:.3f}"
            )
    else:
        print_record(records[0], detail=True)


if __name__ == "__main__":
    main()
