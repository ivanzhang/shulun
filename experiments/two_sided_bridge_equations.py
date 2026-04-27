#!/usr/bin/env python3
"""分析双侧 R-M-R 桥的局部方程与因子消耗。

用法示例：
  python3 experiments/two_sided_bridge_equations.py --P 3000017 --c 458685 --r 8 --C 8 --delta 30
  python3 experiments/two_sided_bridge_equations.py --scan --primes 1000003,3000017 --cols 80 --C 8 --delta 30

对 R-M-R：N_M=q*h，N_L=Q_L*H_L，N_R=Q_R*H_R，且
N_M-N_L=δP*d_L, N_R-N_M=δP*d_R。
记录 d_L,d_R、q,Q_L,Q_R、以及 Q_L/Q_R 是否跨三元组复用。
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
        items.append({"u_idx": len(items), "n": n, "N": N, "label": label, "q": q})
    return L, Y, step, items


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


def two_sided_records(block, step):
    """提取双侧桥方程记录。"""
    records = []
    for idx in range(1, len(block) - 1):
        mid = block[idx]
        left = block[idx - 1]
        right = block[idx + 1]
        if not (mid["label"] == "M" and left["label"] == "R" and right["label"] == "R"):
            continue
        d_left = mid["n"] - left["n"]
        d_right = right["n"] - mid["n"]
        records.append({
            "u": mid["u_idx"],
            "n": mid["n"],
            "qM": mid["q"],
            "qL": left["q"],
            "qR": right["q"],
            "dL": d_left,
            "dR": d_right,
            "span": right["n"] - left["n"],
            "qL_log": math.log(left["q"]),
            "qR_log": math.log(right["q"]),
            "qM_log": math.log(mid["q"]),
            "left_eq_ok": mid["N"] - left["N"] == step * d_left,
            "right_eq_ok": right["N"] - mid["N"] == step * d_right,
        })
    return records


def record_for(P, c, r, delta, C, primes):
    """生成双侧桥记录。"""
    L, Y, step, items = collect(P, c, r, delta, C, primes)
    block = longest_block(items)
    recs = two_sided_records(block, step)
    qR_all = []
    qM_all = []
    for rec in recs:
        qM_all.append(rec["qM"])
        qR_all.extend([rec["qL"], rec["qR"]])
    d_pairs = Counter((rec["dL"], rec["dR"]) for rec in recs)
    return {
        "P": P,
        "c": c,
        "r": r,
        "L": L,
        "Y": Y,
        "U": len(items),
        "Prime": sum(1 for item in items if item["label"] == "P"),
        "block_len": len(block),
        "two_sided": len(recs),
        "distinct_qM": len(set(qM_all)),
        "distinct_qR": len(set(qR_all)),
        "max_qM_reuse": max(Counter(qM_all).values()) if qM_all else 0,
        "max_qR_reuse": max(Counter(qR_all).values()) if qR_all else 0,
        "span_sum": sum(rec["span"] for rec in recs),
        "qR_log_sum": sum(rec["qL_log"] + rec["qR_log"] for rec in recs),
        "d_pairs": d_pairs.most_common(8),
        "records": recs[:20],
    }


def print_record(rec, detail=False):
    """打印记录。"""
    keys = ["P", "c", "r", "L", "Y", "U", "Prime", "block_len", "two_sided", "distinct_qM", "distinct_qR", "max_qM_reuse", "max_qR_reuse", "span_sum", "qR_log_sum"]
    print(",".join(f"{k}={rec[k]}" if not isinstance(rec[k], float) else f"{k}={rec[k]:.3f}" for k in keys))
    if detail:
        print(f"d_pairs={rec['d_pairs']}")
        print("records=u,n,qM,qL,qR,dL,dR,span")
        for row in rec["records"]:
            print((row["u"], row["n"], row["qM"], row["qL"], row["qR"], row["dL"], row["dR"], row["span"]))


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
        rows.sort(key=lambda rec: (-rec["two_sided"], -rec["qR_log_sum"], rec["Prime"]))
        print("worst two-sided bridge equation records")
        for rec in rows[:30]:
            print_record(rec)
        hist = Counter(rec["two_sided"] for rec in rows)
        print(f"summary total={len(rows)} two_sided_hist={dict(sorted(hist.items()))}")
    else:
        print_record(rows[0], detail=True)


if __name__ == "__main__":
    main()
