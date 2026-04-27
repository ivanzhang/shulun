#!/usr/bin/env python3
"""构造 M桥 + R粗簇 的联合压力指标。

用法示例：
  python3 experiments/joint_pressure_metric.py --P 3000017 --c 458685 --r 8 --C 8 --delta 30
  python3 experiments/joint_pressure_metric.py --scan --primes 1000003,3000017 --cols 80 --C 8 --delta 30

指标：
  block_len: 最长 U 合数块长度
  bridge_conversion: M命中转化为桥的比例
  rough_pressure: 最长块中 R 点最小因子乘积压力 sum(log(q/L))
  run_pressure: R段长度平方和，衡量粗簇集中程度
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


def segment_lengths(block, label):
    """指定标签连续段长度。"""
    out = []
    cur = 0
    for item in block + [{"label": None}]:
        if item["label"] == label:
            cur += 1
        elif cur:
            out.append(cur)
            cur = 0
    return out


def bridge_items(block):
    """最长块中的桥接 M 点。"""
    out = []
    for idx, item in enumerate(block):
        if item["label"] != "M":
            continue
        left_r = idx > 0 and block[idx - 1]["label"] == "R"
        right_r = idx + 1 < len(block) and block[idx + 1]["label"] == "R"
        if left_r or right_r:
            out.append(item)
    return out


def record_for(P, c, r, delta, C, primes):
    """计算联合压力记录。"""
    L, Y, items = collect_items(P, c, r, delta, C, primes)
    block = longest_block(items)
    block_set = {item["u_idx"] for item in block}
    all_m_hits = [item for item in items if item["label"] == "M"]
    bridges = bridge_items(block)
    r_items = [item for item in block if item["label"] == "R"]
    m_items = [item for item in block if item["label"] == "M"]
    r_runs = segment_lengths(block, "R")
    m_runs = segment_lengths(block, "M")
    rough_pressure = sum(math.log(item["q"] / L) for item in r_items) if L else 0.0
    run_pressure = sum(length * length for length in r_runs)
    bridge_conversion = len(bridges) / len(all_m_hits) if all_m_hits else 0.0
    # deficit 是还差多少覆盖整个 U；等于素数数，但用结构名表达。
    deficit = len(items) - len([item for item in items if item["label"] in {"M", "R"}])
    return {
        "P": P,
        "c": c,
        "r": r,
        "L": L,
        "Y": Y,
        "U": len(items),
        "Prime": deficit,
        "block_len": len(block),
        "block_R": len(r_items),
        "block_M": len(m_items),
        "bridge": len(bridges),
        "M_hits": len(all_m_hits),
        "bridge_conversion": bridge_conversion,
        "rough_pressure": rough_pressure,
        "run_pressure": run_pressure,
        "r_run_max": max(r_runs) if r_runs else 0,
        "r_run_count": len(r_runs),
        "m_run_max": max(m_runs) if m_runs else 0,
        "m_run_count": len(m_runs),
        "pressure_score": rough_pressure * max(0.0, bridge_conversion) + run_pressure,
        "labels": "".join(item["label"] for item in block[:100]),
    }


def print_record(rec, detail=False):
    """打印记录。"""
    keys = [
        "P", "c", "r", "L", "Y", "U", "Prime", "block_len", "block_R", "block_M",
        "bridge", "M_hits", "bridge_conversion", "rough_pressure", "run_pressure",
        "r_run_max", "r_run_count", "m_run_max", "m_run_count", "pressure_score",
    ]
    print(",".join(f"{k}={rec[k]}" if not isinstance(rec[k], float) else f"{k}={rec[k]:.3f}" for k in keys))
    if detail:
        print(f"labels={rec['labels']}")


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
        rows.sort(key=lambda rec: (rec["Prime"], -rec["block_len"], -rec["pressure_score"]))
        print("worst joint pressure records")
        for rec in rows[:30]:
            print_record(rec)
        scores = sorted(rec["pressure_score"] for rec in rows)
        print(f"summary total={len(rows)} score_q50={scores[len(scores)//2]:.3f} score_q90={scores[int(.9*len(scores))]:.3f} score_max={scores[-1]:.3f}")
    else:
        print_record(rows[0], detail=True)


if __name__ == "__main__":
    main()
