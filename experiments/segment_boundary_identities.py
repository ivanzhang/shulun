#!/usr/bin/env python3
"""验证 U 合数块中 R/M 分段的纯组合边界恒等式。

用法示例：
  python3 experiments/segment_boundary_identities.py --P 3000017 --c 458685 --r 8 --C 8 --delta 30
  python3 experiments/segment_boundary_identities.py --scan --primes 1000003,3000017 --cols 80 --C 8 --delta 30

组合事实：双侧桥 R-M-R 只可能发生在长度为 1 的 M 段，且左右段都是 R。
因此 T <= #M段，且 T <= #内部M段 <= #R段-1（在以R开头结尾时）。
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


def collect(P, c, r, delta, C, primes):
    """收集 U 标签。"""
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
    """最长合数块。"""
    blocks = []
    cur = []
    for item in items + [{"label": "P"}]:
        if item["label"] in {"M", "R"}:
            cur.append(item)
        elif cur:
            blocks.append(cur)
            cur = []
    return max(blocks, key=len) if blocks else []


def segments(block):
    """分段。"""
    out = []
    cur = []
    cur_label = None
    for item in block:
        if item["label"] != cur_label and cur:
            out.append((cur_label, cur))
            cur = []
        cur_label = item["label"]
        cur.append(item)
    if cur:
        out.append((cur_label, cur))
    return out


def record_for(P, c, r, delta, C, primes):
    """生成边界恒等式记录。"""
    L, Y, items = collect(P, c, r, delta, C, primes)
    block = longest_block(items)
    segs = segments(block)
    r_segments = [(i, seg) for i, (label, seg) in enumerate(segs) if label == "R"]
    m_segments = [(i, seg) for i, (label, seg) in enumerate(segs) if label == "M"]
    internal_m_segments = []
    singleton_internal_m = []
    two_sided = 0
    for i, seg in m_segments:
        left_r = i > 0 and segs[i - 1][0] == "R"
        right_r = i + 1 < len(segs) and segs[i + 1][0] == "R"
        if left_r and right_r:
            internal_m_segments.append((i, seg))
            if len(seg) == 1:
                singleton_internal_m.append((i, seg))
                two_sided += 1
    pattern = "".join(label + str(len(seg)) for label, seg in segs)
    identity_ok = two_sided == len(singleton_internal_m)
    bound_ok = two_sided <= len(internal_m_segments) <= max(0, len(r_segments) - 1)
    return {
        "P": P,
        "c": c,
        "r": r,
        "L": L,
        "Y": Y,
        "U": len(items),
        "Prime": sum(1 for item in items if item["label"] == "P"),
        "block_len": len(block),
        "R_total": sum(len(seg) for _, seg in r_segments),
        "M_total": sum(len(seg) for _, seg in m_segments),
        "R_segments": len(r_segments),
        "M_segments": len(m_segments),
        "internal_M_segments": len(internal_m_segments),
        "singleton_internal_M": len(singleton_internal_m),
        "two_sided": two_sided,
        "identity_ok": identity_ok,
        "bound_ok": bound_ok,
        "pattern": pattern,
    }


def print_record(rec, detail=False):
    """打印记录。"""
    keys = ["P", "c", "r", "L", "Y", "U", "Prime", "block_len", "R_total", "M_total", "R_segments", "M_segments", "internal_M_segments", "singleton_internal_M", "two_sided", "identity_ok", "bound_ok"]
    print(",".join(f"{k}={rec[k]}" for k in keys))
    if detail:
        print(f"pattern={rec['pattern']}")


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
        bad = [rec for rec in rows if not rec["identity_ok"] or not rec["bound_ok"]]
        rows.sort(key=lambda rec: (-rec["two_sided"], -rec["block_len"], rec["Prime"]))
        print("worst segment boundary records")
        for rec in rows[:30]:
            print_record(rec)
        print(f"summary total={len(rows)} bad={len(bad)}")
    else:
        print_record(rows[0], detail=True)


if __name__ == "__main__":
    main()
