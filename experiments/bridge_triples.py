#!/usr/bin/env python3
"""分析长 U 合数块中的局部桥三元组 R-M-R / R-M / M-R。

用法示例：
  python3 experiments/bridge_triples.py --P 3000017 --c 458685 --r 8 --C 8 --delta 30
  python3 experiments/bridge_triples.py --scan --primes 1000003,3000017 --cols 80 --C 8 --delta 30

每个 M 桥点若左右邻接 R，就产生局部约束：中因子 q_M 与相邻粗点最小因子 Q_R 同时满足固定差分关系。
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


def triple_record(block, step):
    """提取桥三元组记录。"""
    triples = []
    for idx, item in enumerate(block):
        if item["label"] != "M":
            continue
        left = block[idx - 1] if idx > 0 and block[idx - 1]["label"] == "R" else None
        right = block[idx + 1] if idx + 1 < len(block) and block[idx + 1]["label"] == "R" else None
        if not left and not right:
            continue
        kind = "RMR" if left and right else ("RM" if left else "MR")
        constraints = []
        for side, rough in (("L", left), ("R", right)):
            if rough is None:
                continue
            dn = rough["n"] - item["n"]
            constraints.append({
                "side": side,
                "dn": dn,
                "qM": item["q"],
                "qR": rough["q"],
                "gcd_q": math.gcd(item["q"], rough["q"]),
                "deltaN_over_step": dn,
            })
        triples.append({
            "u": item["u_idx"],
            "n": item["n"],
            "kind": kind,
            "qM": item["q"],
            "left_qR": left["q"] if left else None,
            "right_qR": right["q"] if right else None,
            "constraints": constraints,
        })
    return triples


def record_for(P, c, r, delta, C, primes):
    """生成桥三元组记录。"""
    L, Y, items = collect(P, c, r, delta, C, primes)
    A = c + r * P
    step = delta * P
    block = longest_block(items)
    triples = triple_record(block, step)
    kind_counter = Counter(t["kind"] for t in triples)
    qM_counter = Counter(t["qM"] for t in triples)
    qR_values = []
    for t in triples:
        if t["left_qR"]:
            qR_values.append(t["left_qR"])
        if t["right_qR"]:
            qR_values.append(t["right_qR"])
    return {
        "P": P,
        "c": c,
        "r": r,
        "L": L,
        "Y": Y,
        "U": len(items),
        "Prime": sum(1 for item in items if item["label"] == "P"),
        "block_len": len(block),
        "triple_count": len(triples),
        "two_sided": kind_counter.get("RMR", 0),
        "one_sided": kind_counter.get("RM", 0) + kind_counter.get("MR", 0),
        "distinct_qM": len(qM_counter),
        "max_qM_reuse": max(qM_counter.values()) if qM_counter else 0,
        "distinct_adjacent_qR": len(set(qR_values)),
        "top_qM": qM_counter.most_common(8),
        "triples": triples[:24],
    }


def print_record(rec, detail=False):
    """打印记录。"""
    keys = ["P", "c", "r", "L", "Y", "U", "Prime", "block_len", "triple_count", "two_sided", "one_sided", "distinct_qM", "max_qM_reuse", "distinct_adjacent_qR"]
    print(",".join(f"{k}={rec[k]}" for k in keys))
    if detail:
        print(f"top_qM={rec['top_qM']}")
        print("triples=u,n,kind,qM,left_qR,right_qR")
        for t in rec["triples"]:
            print((t["u"], t["n"], t["kind"], t["qM"], t["left_qR"], t["right_qR"]))


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
        rows.sort(key=lambda rec: (-rec["two_sided"], -rec["triple_count"], rec["Prime"]))
        print("worst bridge triple records")
        for rec in rows[:30]:
            print_record(rec)
        hist = Counter(rec["two_sided"] for rec in rows)
        print(f"summary total={len(rows)} two_sided_hist={dict(sorted(hist.items()))}")
    else:
        print_record(rows[0], detail=True)


if __name__ == "__main__":
    main()
