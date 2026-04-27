#!/usr/bin/env python3
"""扫描短链中的连续 L-粗合数簇。

用法示例：
  python3 experiments/rough_run_blocks.py --P 3000017 --c 458685 --r 8 --C 8
  python3 experiments/rough_run_blocks.py --scan --primes 1000003,3000017 --cols 80 --C 8

连续粗点簇是反例最危险的局部形态：多个相邻 n 都是 L-粗合数且两两互质。
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
    """构建素数表。"""
    max_P = max(Ps)
    max_L = int(C * math.log(max_P) ** 2 / delta) + 10
    max_N = max_P + delta * max_P * max_L + delta * max_P
    return vb.primes_upto_from_sieve(vb.sieve(math.isqrt(max_N) + 5000))


def lpf(n, primes):
    """返回最小素因子。"""
    for p in primes:
        if p * p > n:
            return n
        if n % p == 0:
            return p
    return n


def classify_points(P, c, r, delta, L, primes):
    """分类每个 n：R=L粗合数, P=素数, M=有 <=L 因子的合数。"""
    A = c + r * P
    step = delta * P
    labels = []
    details = []
    for n in range(L + 1):
        N = A + step * n
        if vb.is_prime_mr(N):
            labels.append("P")
            details.append((n, "P", None))
            continue
        least = lpf(N, primes)
        if least > L:
            labels.append("R")
            details.append((n, "R", least))
        else:
            labels.append("M")
            details.append((n, "M", least))
    return labels, details


def run_lengths(labels, target):
    """返回指定标签的连续块。"""
    runs = []
    start = None
    for idx, label in enumerate(labels + [None]):
        if label == target and start is None:
            start = idx
        elif label != target and start is not None:
            runs.append((start, idx - 1, idx - start))
            start = None
    return runs


def record_for(P, c, r, delta, L, primes):
    """计算连续粗点簇记录。"""
    labels, details = classify_points(P, c, r, delta, L, primes)
    rough_runs = run_lengths(labels, "R")
    prime_runs = run_lengths(labels, "P")
    mid_runs = run_lengths(labels, "M")
    rough_count = labels.count("R")
    prime_count = labels.count("P")
    mid_count = labels.count("M")
    max_rough_run = max((run[2] for run in rough_runs), default=0)
    first_prime = next((idx for idx, label in enumerate(labels) if label == "P"), None)
    return {
        "P": P,
        "c": c,
        "r": r,
        "L": L,
        "rough": rough_count,
        "prime": prime_count,
        "mid": mid_count,
        "max_rough_run": max_rough_run,
        "first_prime": first_prime,
        "rough_runs": rough_runs[:12],
        "label_prefix": "".join(labels[:80]),
        "least_prefix": details[:30],
        "rough_run_hist": dict(Counter(run[2] for run in rough_runs)),
        "prime_run_hist": dict(Counter(run[2] for run in prime_runs)),
        "mid_run_hist": dict(Counter(run[2] for run in mid_runs)),
    }


def print_record(record, detail=False):
    """打印记录。"""
    keys = ["P", "c", "r", "L", "rough", "prime", "mid", "max_rough_run", "first_prime"]
    print(",".join(f"{key}={record[key]}" for key in keys))
    if detail:
        print(f"label_prefix={record['label_prefix']}")
        print(f"rough_runs={record['rough_runs']}")
        print(f"rough_run_hist={record['rough_run_hist']}")
        print(f"least_prefix={record['least_prefix']}")


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
    args = parser.parse_args()

    Ps = [int(x) for x in args.primes.split(",") if x.strip()] if args.scan else [args.P]
    if not args.scan and (not args.P or not args.c):
        raise SystemExit("非扫描模式需要 --P 与 --c")
    primes = build_primes(Ps, args.C, args.delta)
    rows = []
    for P in Ps:
        L = int(args.C * math.log(P) ** 2 / args.delta)
        if args.scan:
            random.seed(P)
            cols = list(dict.fromkeys([1, 2, 6, 30, P // 2, P - 1] + random.sample(range(1, P), min(args.cols, P - 1))))
            for c in cols:
                for r in gap.allowed_residues(P, c, args.delta):
                    rows.append(record_for(P, c, r, args.delta, L, primes))
        else:
            rows.append(record_for(args.P, args.c, args.r, args.delta, L, primes))

    if args.scan:
        rows.sort(key=lambda rec: (-rec["max_rough_run"], -rec["rough"], rec["prime"]))
        print("worst rough run records")
        for record in rows[:30]:
            print_record(record)
        hist = Counter()
        for rec in rows:
            hist[rec["max_rough_run"]] += 1
        print(f"summary total={len(rows)} max_run_hist={dict(sorted(hist.items()))}")
    else:
        print_record(rows[0], detail=True)


if __name__ == "__main__":
    main()
