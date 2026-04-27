#!/usr/bin/env python3
"""分析 U 合数块中 M 如何桥接 R 粗簇之间的缝隙。

用法示例：
  python3 experiments/m_bridge_gap_analysis.py --P 3000017 --c 458685 --r 8 --C 8 --delta 30
  python3 experiments/m_bridge_gap_analysis.py --scan --primes 1000003,3000017 --cols 80 --C 8 --delta 30

定义：在 U 序列的最长合数块中，把连续 R 段看作粗簇，夹在 R 段之间的 M 串看作桥。
记录每座桥的长度、使用的中因子 q、是否由单个 q 支配、以及 q 的复用情况。
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


def collect_u_items(P, c, r, delta, C, primes):
    """收集 U 序列项目。"""
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


def longest_composite_block(items):
    """返回最长 U 合数块。"""
    blocks = []
    cur = []
    for item in items + [{"label": "P"}]:
        if item["label"] in {"M", "R"}:
            cur.append(item)
        elif cur:
            blocks.append(cur)
            cur = []
    return max(blocks, key=len) if blocks else []


def decompose_bridges(block):
    """把最长块分解为 R 段与 M 桥。"""
    segments = []
    cur = []
    cur_label = None
    for item in block:
        label = item["label"]
        if label != cur_label and cur:
            segments.append((cur_label, cur))
            cur = []
        cur_label = label
        cur.append(item)
    if cur:
        segments.append((cur_label, cur))

    bridges = []
    for idx, (label, seg) in enumerate(segments):
        if label != "M":
            continue
        left_r = idx > 0 and segments[idx - 1][0] == "R"
        right_r = idx + 1 < len(segments) and segments[idx + 1][0] == "R"
        if left_r or right_r:
            qs = [item["q"] for item in seg]
            bridges.append({
                "start_u": seg[0]["u_idx"],
                "end_u": seg[-1]["u_idx"],
                "start_n": seg[0]["n"],
                "end_n": seg[-1]["n"],
                "length": len(seg),
                "qs": qs,
                "distinct_q": len(set(qs)),
                "dominant_q_count": Counter(qs).most_common(1)[0][1],
                "left_r_len": len(segments[idx - 1][1]) if left_r else 0,
                "right_r_len": len(segments[idx + 1][1]) if right_r else 0,
            })
    return segments, bridges


def record_for(P, c, r, delta, C, primes):
    """生成桥接记录。"""
    L, Y, items = collect_u_items(P, c, r, delta, C, primes)
    block = longest_composite_block(items)
    segments, bridges = decompose_bridges(block)
    m_items = [item for item in block if item["label"] == "M"]
    r_items = [item for item in block if item["label"] == "R"]
    q_counter = Counter(item["q"] for item in m_items)
    return {
        "P": P,
        "c": c,
        "r": r,
        "L": L,
        "Y": Y,
        "U": len(items),
        "Prime": sum(1 for item in items if item["label"] == "P"),
        "block_len": len(block),
        "block_M": len(m_items),
        "block_R": len(r_items),
        "segment_count": len(segments),
        "bridge_count": len(bridges),
        "bridge_total": sum(b["length"] for b in bridges),
        "max_bridge": max((b["length"] for b in bridges), default=0),
        "distinct_M_q": len(q_counter),
        "top_M_q": q_counter.most_common(8),
        "bridges": bridges[:20],
        "segment_pattern": "".join(label + str(len(seg)) for label, seg in segments),
    }


def print_record(rec, detail=False):
    """打印记录。"""
    keys = ["P", "c", "r", "L", "Y", "U", "Prime", "block_len", "block_M", "block_R", "segment_count", "bridge_count", "bridge_total", "max_bridge", "distinct_M_q"]
    print(",".join(f"{k}={rec[k]}" for k in keys))
    if detail:
        print(f"segment_pattern={rec['segment_pattern']}")
        print(f"top_M_q={rec['top_M_q']}")
        print("bridges=start_u,end_u,start_n,end_n,length,qs,distinct,dominant,leftR,rightR")
        for b in rec["bridges"]:
            print((b["start_u"], b["end_u"], b["start_n"], b["end_n"], b["length"], b["qs"], b["distinct_q"], b["dominant_q_count"], b["left_r_len"], b["right_r_len"]))


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
        rows.sort(key=lambda rec: (-rec["block_len"], -rec["bridge_total"], rec["Prime"]))
        print("worst M-bridge gap records")
        for rec in rows[:30]:
            print_record(rec)
    else:
        print_record(rows[0], detail=True)


if __name__ == "__main__":
    main()
