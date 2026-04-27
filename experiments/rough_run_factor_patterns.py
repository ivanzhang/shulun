#!/usr/bin/env python3
"""分析连续 L-粗合数簇中的最小因子模式。

用法示例：
  python3 experiments/rough_run_factor_patterns.py --P 3000017 --c 458685 --r 8 --C 8
  python3 experiments/rough_run_factor_patterns.py --scan --primes 1000003,3000017 --cols 80 --C 8

对每个连续 R 簇，记录最小因子 q_k、协因子 h_k、q 的大小层、q 之间的互异性，
并验证簇内任意 q_i 不整除相邻差分结构。
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


def min_factor_pair(n, primes):
    """返回最小素因子和协因子。"""
    for p in primes:
        if p * p > n:
            return n, 1
        if n % p == 0:
            return p, n // p
    return n, 1


def classify(P, c, r, delta, L, primes):
    """返回每个点的标签和分解信息。"""
    A = c + r * P
    step = delta * P
    items = []
    for n in range(L + 1):
        N = A + step * n
        q, h = min_factor_pair(N, primes)
        if h == 1:
            label = "P"
        elif q > L:
            label = "R"
        else:
            label = "M"
        items.append({"n": n, "N": N, "label": label, "q": q, "h": h})
    return A, step, items


def rough_runs(items):
    """提取连续 R 簇。"""
    runs = []
    current = []
    for item in items + [{"label": None}]:
        if item["label"] == "R":
            current.append(item)
        elif current:
            runs.append(current)
            current = []
    return runs


def run_signature(run, L):
    """生成粗簇签名。"""
    q_values = [item["q"] for item in run]
    h_values = [item["h"] for item in run]
    n_values = [item["n"] for item in run]
    q_log_blocks = [int(math.log2(q)) for q in q_values]
    hq_logs = [int(math.log2(max(1.0, h / q))) for q, h in zip(q_values, h_values)]
    q_min = min(q_values)
    q_max = max(q_values)
    q_spread = q_max / q_min if q_min else 0
    adjacent_q_direction = "".join("+" if b > a else "-" for a, b in zip(q_values, q_values[1:]))
    return {
        "start": n_values[0],
        "end": n_values[-1],
        "length": len(run),
        "q_min": q_min,
        "q_max": q_max,
        "q_spread": q_spread,
        "q_values": q_values,
        "h_values": h_values,
        "q_log_blocks": q_log_blocks,
        "hq_logs": hq_logs,
        "q_direction": adjacent_q_direction,
        "all_q_distinct": len(set(q_values)) == len(q_values),
        "product_log_q_over_L": sum(math.log(q / L) for q in q_values),
    }


def record_for(P, c, r, delta, L, primes):
    """单链粗簇因子模式记录。"""
    A, step, items = classify(P, c, r, delta, L, primes)
    runs = rough_runs(items)
    signatures = [run_signature(run, L) for run in runs]
    signatures.sort(key=lambda sig: (-sig["length"], sig["start"]))
    max_sig = signatures[0] if signatures else None
    return {
        "P": P,
        "c": c,
        "r": r,
        "L": L,
        "run_count": len(runs),
        "max_run": max_sig["length"] if max_sig else 0,
        "max_run_start": max_sig["start"] if max_sig else None,
        "max_run_qmin": max_sig["q_min"] if max_sig else None,
        "max_run_qmax": max_sig["q_max"] if max_sig else None,
        "max_run_qspread": max_sig["q_spread"] if max_sig else None,
        "max_run_prodlog": max_sig["product_log_q_over_L"] if max_sig else None,
        "top_runs": signatures[:6],
    }


def print_record(record, detail=False):
    """打印记录。"""
    keys = ["P", "c", "r", "L", "run_count", "max_run", "max_run_start", "max_run_qmin", "max_run_qmax", "max_run_qspread", "max_run_prodlog"]
    print(",".join(f"{key}={record[key]}" for key in keys))
    if detail:
        for sig in record["top_runs"]:
            print(
                "run "
                f"start={sig['start']} end={sig['end']} length={sig['length']} "
                f"q={sig['q_values']} h={sig['h_values']} "
                f"qlog={sig['q_log_blocks']} hqlog={sig['hq_logs']} "
                f"dir={sig['q_direction']} prodlog={sig['product_log_q_over_L']:.3f}"
            )


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
        rows.sort(key=lambda rec: (-rec["max_run"], -(rec["max_run_prodlog"] or 0), rec["P"]))
        print("worst rough run factor pattern records")
        for record in rows[:30]:
            print_record(record)
        hist = Counter(rec["max_run"] for rec in rows)
        print(f"summary total={len(rows)} max_run_hist={dict(sorted(hist.items()))}")
    else:
        print_record(rows[0], detail=True)


if __name__ == "__main__":
    main()
