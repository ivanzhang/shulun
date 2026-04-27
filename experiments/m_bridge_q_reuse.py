#!/usr/bin/env python3
"""分析每个中因子 q 在 M 桥中的复用容量。

用法示例：
  python3 experiments/m_bridge_q_reuse.py --P 3000017 --c 458685 --r 8 --C 8 --delta 30
  python3 experiments/m_bridge_q_reuse.py --scan --primes 1000003,3000017 --cols 80 --C 8 --delta 30

核心：同一个 q 的桥点在高度 n 上间距为 q；若它多次承担桥接，桥位之间必须相隔 q，
同时每个桥位还要邻接 R 粗簇。
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


def collect_u(P, c, r, delta, C, primes):
    """收集 U 序列。"""
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


def longest_block(items):
    """最长 U 合数块。"""
    blocks = []
    cur = []
    for item in items + [{"label": "P"}]:
        if item["label"] in {"M", "R"}:
            cur.append(item)
        elif cur:
            blocks.append(cur)
            cur = []
    return max(blocks, key=len) if blocks else []


def bridge_m_items(block):
    """返回桥接 M 点。"""
    out = []
    for idx, item in enumerate(block):
        if item["label"] != "M":
            continue
        left_r = idx > 0 and block[idx - 1]["label"] == "R"
        right_r = idx + 1 < len(block) and block[idx + 1]["label"] == "R"
        if left_r or right_r:
            out.append({**item, "left_r": left_r, "right_r": right_r})
    return out


def record_for(P, c, r, delta, C, primes):
    """生成 q 复用记录。"""
    L, Y, items = collect_u(P, c, r, delta, C, primes)
    block = longest_block(items)
    bridges = bridge_m_items(block)
    by_q = defaultdict(list)
    for item in bridges:
        by_q[item["q"]].append(item)
    q_records = []
    for q, q_items in by_q.items():
        q_items.sort(key=lambda item: item["n"])
        n_values = [item["n"] for item in q_items]
        gaps = [b - a for a, b in zip(n_values, n_values[1:])]
        q_records.append({
            "q": q,
            "count": len(q_items),
            "n_values": n_values,
            "u_values": [item["u_idx"] for item in q_items],
            "gaps": gaps,
            "all_gaps_multiple_q": all(g % q == 0 for g in gaps),
            "two_sided": sum(1 for item in q_items if item["left_r"] and item["right_r"]),
        })
    q_records.sort(key=lambda rec: (-rec["count"], rec["q"]))
    return {
        "P": P,
        "c": c,
        "r": r,
        "L": L,
        "Y": Y,
        "U": len(items),
        "Prime": sum(1 for item in items if item["label"] == "P"),
        "block_len": len(block),
        "bridge_total": len(bridges),
        "distinct_bridge_q": len(by_q),
        "max_q_reuse": q_records[0]["count"] if q_records else 0,
        "q_records": q_records[:12],
    }


def print_record(rec, detail=False):
    """打印记录。"""
    keys = ["P", "c", "r", "L", "Y", "U", "Prime", "block_len", "bridge_total", "distinct_bridge_q", "max_q_reuse"]
    print(",".join(f"{key}={rec[key]}" for key in keys))
    if detail:
        print("q_records=q,count,n_values,u_values,gaps,multiple_q,two_sided")
        for qr in rec["q_records"]:
            print((qr["q"], qr["count"], qr["n_values"], qr["u_values"], qr["gaps"], qr["all_gaps_multiple_q"], qr["two_sided"]))


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
        rows.sort(key=lambda rec: (-rec["max_q_reuse"], -rec["bridge_total"], -rec["block_len"]))
        print("worst bridge q reuse records")
        for rec in rows[:30]:
            print_record(rec)
        hist = Counter(rec["max_q_reuse"] for rec in rows)
        print(f"summary total={len(rows)} max_q_reuse_hist={dict(sorted(hist.items()))}")
    else:
        print_record(rows[0], detail=True)


if __name__ == "__main__":
    main()
