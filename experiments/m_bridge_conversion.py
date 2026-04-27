#!/usr/bin/env python3
"""比较中因子 q 的全部 U 命中点与桥接命中点。

用法示例：
  python3 experiments/m_bridge_conversion.py --P 3000017 --c 458685 --r 8 --C 8 --delta 30
  python3 experiments/m_bridge_conversion.py --scan --primes 1000003,3000017 --cols 80 --C 8 --delta 30

目标：证明桥邻接稀疏。对每个 q∈(Y,L]，统计：
  hit_q = U 中由 q 作为最小因子的 M 点数；
  bridge_q = 其中在最长合数块内邻接 R 的桥点数。
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


def collect_items(P, c, r, delta, C, primes):
    """收集 U 项。"""
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


def longest_block_indices(items):
    """返回最长合数块的 U 索引集合。"""
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
    """生成转化率记录。"""
    L, Y, items = collect_items(P, c, r, delta, C, primes)
    longest = longest_block_indices(items)
    hit_by_q = defaultdict(list)
    bridge_by_q = defaultdict(list)
    all_bridge = []
    for idx, item in enumerate(items):
        if item["label"] != "M":
            continue
        hit_by_q[item["q"]].append(item)
        in_longest = item["u_idx"] in longest
        left_r = idx > 0 and items[idx - 1]["u_idx"] in longest and items[idx - 1]["label"] == "R"
        right_r = idx + 1 < len(items) and items[idx + 1]["u_idx"] in longest and items[idx + 1]["label"] == "R"
        if in_longest and (left_r or right_r):
            bridge_by_q[item["q"]].append(item)
            all_bridge.append(item)
    q_rows = []
    for q, hits in hit_by_q.items():
        bridges = bridge_by_q.get(q, [])
        q_rows.append({
            "q": q,
            "hits": len(hits),
            "bridges": len(bridges),
            "conversion": len(bridges) / len(hits),
            "hit_n": [item["n"] for item in hits],
            "bridge_n": [item["n"] for item in bridges],
        })
    q_rows.sort(key=lambda row: (-row["bridges"], -row["hits"], row["q"]))
    total_hits = sum(len(v) for v in hit_by_q.values())
    total_bridge = len(all_bridge)
    return {
        "P": P,
        "c": c,
        "r": r,
        "L": L,
        "Y": Y,
        "U": len(items),
        "Prime": sum(1 for item in items if item["label"] == "P"),
        "M_hits": total_hits,
        "bridge": total_bridge,
        "distinct_hit_q": len(hit_by_q),
        "distinct_bridge_q": len(bridge_by_q),
        "conversion": total_bridge / total_hits if total_hits else 0.0,
        "q_rows": q_rows[:14],
    }


def print_record(rec, detail=False):
    """打印记录。"""
    keys = ["P", "c", "r", "L", "Y", "U", "Prime", "M_hits", "bridge", "distinct_hit_q", "distinct_bridge_q", "conversion"]
    print(",".join(f"{k}={rec[k]}" for k in keys))
    if detail:
        print("q_rows=q,hits,bridges,conversion,hit_n,bridge_n")
        for row in rec["q_rows"]:
            print((row["q"], row["hits"], row["bridges"], round(row["conversion"], 3), row["hit_n"], row["bridge_n"]))


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
        rows.sort(key=lambda rec: (-rec["bridge"], -rec["conversion"], -rec["M_hits"]))
        print("worst M bridge conversion records")
        for rec in rows[:30]:
            print_record(rec)
        conversions = sorted(rec["conversion"] for rec in rows)
        print(
            "summary "
            f"total={len(rows)} max_bridge={max(rec['bridge'] for rec in rows)} "
            f"conv_q50={conversions[len(conversions)//2]:.3f} conv_q90={conversions[int(.9*len(conversions))]:.3f} conv_max={conversions[-1]:.3f}"
        )
    else:
        print_record(rows[0], detail=True)


if __name__ == "__main__":
    main()
