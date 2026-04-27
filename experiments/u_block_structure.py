#!/usr/bin/env python3
"""剖析 U 序列中最长 M/R 合数块的内部结构。

用法示例：
  python3 experiments/u_block_structure.py --P 3000017 --c 458685 --r 8 --C 8 --delta 30
  python3 experiments/u_block_structure.py --scan --primes 1000003,3000017 --cols 80 --C 8 --delta 30

关注：M 点如何桥接 R 粗簇，以及 M 的中因子 q 是否形成少数周期骨架。
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
        items.append({"u_idx": len(items), "n": n, "N": N, "label": label, "q": q})
    return L, Y, items


def composite_blocks(items):
    """返回 U 序列中的连续合数块。"""
    blocks = []
    cur = []
    for item in items + [{"label": "P"}]:
        if item["label"] in {"M", "R"}:
            cur.append(item)
        elif cur:
            blocks.append(cur)
            cur = []
    return blocks


def block_signature(block, L, Y):
    """生成合数块签名。"""
    labels = "".join(item["label"] for item in block)
    m_items = [item for item in block if item["label"] == "M"]
    r_items = [item for item in block if item["label"] == "R"]
    m_qs = [item["q"] for item in m_items]
    r_qs = [item["q"] for item in r_items]
    m_counter = Counter(m_qs)
    # M 桥：夹在 R 段之间的 M，或把两个 R 邻近簇连起来的 M。
    bridge_m = 0
    for idx, item in enumerate(block):
        if item["label"] != "M":
            continue
        left_r = idx > 0 and block[idx - 1]["label"] == "R"
        right_r = idx + 1 < len(block) and block[idx + 1]["label"] == "R"
        if left_r or right_r:
            bridge_m += 1
    return {
        "start_u": block[0]["u_idx"],
        "end_u": block[-1]["u_idx"],
        "start_n": block[0]["n"],
        "end_n": block[-1]["n"],
        "length": len(block),
        "labels": labels,
        "M": len(m_items),
        "R": len(r_items),
        "bridge_M": bridge_m,
        "distinct_M_q": len(set(m_qs)),
        "top_M_q": m_counter.most_common(8),
        "R_q_min": min(r_qs) if r_qs else None,
        "R_q_max": max(r_qs) if r_qs else None,
        "M_q_min": min(m_qs) if m_qs else None,
        "M_q_max": max(m_qs) if m_qs else None,
        "detail": [(item["u_idx"], item["n"], item["label"], item["q"]) for item in block[:80]],
    }


def record_for(P, c, r, delta, C, primes):
    """单链最长 U 合数块记录。"""
    L, Y, items = collect_u_items(P, c, r, delta, C, primes)
    blocks = composite_blocks(items)
    sigs = [block_signature(block, L, Y) for block in blocks]
    sigs.sort(key=lambda sig: (-sig["length"], sig["start_u"]))
    top = sigs[0] if sigs else None
    return {
        "P": P,
        "c": c,
        "r": r,
        "L": L,
        "Y": Y,
        "U": len(items),
        "Prime": sum(1 for item in items if item["label"] == "P"),
        "block_count": len(sigs),
        "max_block": top["length"] if top else 0,
        "top": top,
    }


def print_record(rec, detail=False):
    """打印记录。"""
    top = rec["top"] or {}
    keys = ["P", "c", "r", "L", "Y", "U", "Prime", "block_count", "max_block"]
    print(",".join(f"{key}={rec[key]}" for key in keys) + 
          f",block_M={top.get('M')},block_R={top.get('R')},bridge_M={top.get('bridge_M')},distinct_M_q={top.get('distinct_M_q')}")
    if detail and top:
        print(f"labels={top['labels']}")
        print(f"u_range={top['start_u']}..{top['end_u']} n_range={top['start_n']}..{top['end_n']}")
        print(f"top_M_q={top['top_M_q']}")
        print(f"M_q_range={top['M_q_min']}..{top['M_q_max']} R_q_range={top['R_q_min']}..{top['R_q_max']}")
        print("detail=u_idx,n,label,q")
        for row in top["detail"]:
            print(row)


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
        rows.sort(key=lambda rec: (-rec["max_block"], rec["Prime"], -rec["U"]))
        print("worst U block structure records")
        for rec in rows[:30]:
            print_record(rec)
    else:
        print_record(rows[0], detail=True)


if __name__ == "__main__":
    main()
