#!/usr/bin/env python3
"""对中因子命中点筛选“可桥接 R 邻点”的候选容量。

用法示例：
  python3 experiments/bridge_candidate_sieve.py --P 3000017 --c 458685 --r 8 --C 8 --delta 30
  python3 experiments/bridge_candidate_sieve.py --scan --primes 1000003,3000017 --cols 80 --C 8 --delta 30

桥点 n 必须是 M 点，且 U 序列邻点至少一侧为 R。
本脚本计算更宽的候选：M 点的高度邻域中，最近 U 左/右邻是否为 L-粗候选。
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


def collect(P, c, r, delta, C, primes):
    """收集 U 序列与标签。"""
    L = int(C * math.log(P) ** 2 / delta)
    Y = gap.next_prime_ge(math.sqrt(max(2, L)), primes)
    A = c + r * P
    step = delta * P
    small = [p for p in primes if p <= Y and math.gcd(p, step) == 1]
    items = []
    for n in range(L + 1):
        N = A + step * n
        if any(N % p == 0 for p in small):
            continue
        if vb.is_prime_mr(N):
            label = "P"
            q = N
        else:
            q = lpf(N, primes)
            label = "R" if q > L else "M"
        items.append({"u_idx": len(items), "n": n, "label": label, "q": q})
    return L, Y, items


def longest_block_set(items):
    """最长合数块索引集合。"""
    best = []
    cur = []
    for item in items + [{"label": "P"}]:
        if item["label"] in {"M", "R"}:
            cur.append(item["u_idx"])
        elif cur:
            if len(cur) > len(best):
                best = cur
            cur = []
    return set(best)


def record_for(P, c, r, delta, C, primes):
    """计算桥候选容量。"""
    L, Y, items = collect(P, c, r, delta, C, primes)
    longest = longest_block_set(items)
    M_items = [item for item in items if item["label"] == "M"]
    true_bridges = []
    candidate_bridges = []
    two_sided_candidates = []
    q_to_candidate = defaultdict(list)
    q_to_true = defaultdict(list)
    for idx, item in enumerate(items):
        if item["label"] != "M":
            continue
        left = items[idx - 1] if idx > 0 else None
        right = items[idx + 1] if idx + 1 < len(items) else None
        left_R = left is not None and left["label"] == "R"
        right_R = right is not None and right["label"] == "R"
        in_longest = item["u_idx"] in longest
        true_bridge = in_longest and (left_R or right_R)
        candidate = left_R or right_R
        if true_bridge:
            true_bridges.append(item)
            q_to_true[item["q"]].append(item)
        if candidate:
            candidate_bridges.append(item)
            q_to_candidate[item["q"]].append(item)
        if left_R and right_R:
            two_sided_candidates.append(item)
    candidate_by_q = {q: len(v) for q, v in q_to_candidate.items()}
    true_by_q = {q: len(v) for q, v in q_to_true.items()}
    return {
        "P": P,
        "c": c,
        "r": r,
        "L": L,
        "Y": Y,
        "U": len(items),
        "Prime": sum(1 for item in items if item["label"] == "P"),
        "M": len(M_items),
        "candidate": len(candidate_bridges),
        "true_bridge": len(true_bridges),
        "two_sided": len(two_sided_candidates),
        "distinct_candidate_q": len(q_to_candidate),
        "max_candidate_q_reuse": max(candidate_by_q.values()) if candidate_by_q else 0,
        "top_candidate_q": sorted(candidate_by_q.items(), key=lambda x: (-x[1], x[0]))[:8],
        "top_true_q": sorted(true_by_q.items(), key=lambda x: (-x[1], x[0]))[:8],
    }


def print_record(rec, detail=False):
    """打印记录。"""
    keys = ["P", "c", "r", "L", "Y", "U", "Prime", "M", "candidate", "true_bridge", "two_sided", "distinct_candidate_q", "max_candidate_q_reuse"]
    print(",".join(f"{k}={rec[k]}" for k in keys))
    if detail:
        print(f"top_candidate_q={rec['top_candidate_q']}")
        print(f"top_true_q={rec['top_true_q']}")


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
        rows.sort(key=lambda rec: (-rec["candidate"], rec["Prime"], -rec["two_sided"]))
        print("worst bridge candidate records")
        for rec in rows[:30]:
            print_record(rec)
        hist = Counter(rec["max_candidate_q_reuse"] for rec in rows)
        print(f"summary total={len(rows)} max_candidate_q_reuse_hist={dict(sorted(hist.items()))}")
    else:
        print_record(rows[0], detail=True)


if __name__ == "__main__":
    main()
