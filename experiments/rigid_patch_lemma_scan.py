#!/usr/bin/env python3
"""刚性补洞引理实验扫描。

研究列 a mod P 的小筛幸存洞 H_y(a)，以及大素数 y<q<P 对这些洞的补洞能力。

用法示例：
  python3 experiments/rigid_patch_lemma_scan.py --P 1009 --y 31 --top 12 --detail
  python3 experiments/rigid_patch_lemma_scan.py --scan --maxP 2000 --y 31 --top 20
  python3 experiments/rigid_patch_lemma_scan.py --Ps 251,503,1009,2003 --ys 11,17,31,47
"""
import argparse
import math
from collections import Counter, defaultdict


def sieve(n: int) -> bytearray:
    """返回 n 以内素数标记。"""
    flags = bytearray(b"\x01") * (n + 1)
    if n >= 0:
        flags[0] = 0
    if n >= 1:
        flags[1] = 0
    for p in range(2, math.isqrt(n) + 1):
        if flags[p]:
            start = p * p
            flags[start:n + 1:p] = b"\x00" * (((n - start) // p) + 1)
    return flags


def primes_from_flags(flags: bytearray, n: int) -> list[int]:
    """从筛标记中提取素数。"""
    return [i for i in range(2, n + 1) if flags[i]]


def factor_by_primes(n: int, primes: list[int]) -> list[int]:
    """用给定素数表返回 n 的不同素因子。"""
    out = []
    x = n
    for p in primes:
        if p * p > x:
            break
        if x % p == 0:
            out.append(p)
            while x % p == 0:
                x //= p
    if x > 1:
        out.append(x)
    return out


def record_for(P: int, a: int, y: int, flags: bytearray, root_primes: list[int]) -> dict:
    """计算一个列剩余类的刚性补洞指标。"""
    small = [q for q in root_primes if q <= y]
    big = [q for q in root_primes if y < q < P]
    holes = []
    prime_holes = []
    composite_holes = []
    patch_factors_by_r = {}
    hit_rows_by_q = defaultdict(list)

    for r in range(P):
        n = a + r * P
        if all(n % q for q in small):
            holes.append(r)
            if flags[n]:
                prime_holes.append(r)
                patch_factors_by_r[r] = []
            else:
                factors = [q for q in factor_by_primes(n, root_primes) if y < q < P]
                composite_holes.append(r)
                patch_factors_by_r[r] = factors
                for q in factors:
                    hit_rows_by_q[q].append(r)

    q_hit_sizes = [len(v) for v in hit_rows_by_q.values()]
    shared_qs = {q: rows for q, rows in hit_rows_by_q.items() if len(rows) >= 2}
    singleton_holes = [r for r in composite_holes if len(patch_factors_by_r[r]) == 1]
    multi_factor_holes = [r for r in composite_holes if len(patch_factors_by_r[r]) >= 2]

    # 差分证书：同一个 q 命中多个洞时，所有差分都应被 q 整除。
    diff_violations = 0
    shared_edges = 0
    max_span_share = 0
    for q, rows in shared_qs.items():
        rows = sorted(rows)
        max_span_share = max(max_span_share, rows[-1] - rows[0])
        for i, r1 in enumerate(rows):
            for r2 in rows[i + 1:]:
                shared_edges += 1
                if (r2 - r1) % q != 0:
                    diff_violations += 1

    # 使用实际合数因子的最小补丁覆盖数：每个 composite hole 至少选一个因子。
    # 小规模精确，大规模用贪心近似，衡量“共享补丁”节省能力。
    uncovered = set(composite_holes)
    greedy_cover = 0
    q_to_set = {q: set(rows) for q, rows in hit_rows_by_q.items()}
    while uncovered and q_to_set:
        q, rows = max(q_to_set.items(), key=lambda item: len(item[1] & uncovered))
        gain = rows & uncovered
        if not gain:
            break
        greedy_cover += 1
        uncovered -= gain

    return {
        "P": P,
        "a": a,
        "y": y,
        "holes": len(holes),
        "prime_holes": len(prime_holes),
        "composite_holes": len(composite_holes),
        "singleton_holes": len(singleton_holes),
        "multi_factor_holes": len(multi_factor_holes),
        "distinct_patch_q": len(hit_rows_by_q),
        "shared_q": len(shared_qs),
        "shared_edges": shared_edges,
        "max_q_hit": max(q_hit_sizes) if q_hit_sizes else 0,
        "greedy_cover": greedy_cover,
        "diff_violations": diff_violations,
        "max_span_share": max_span_share,
        "holes_list": holes,
        "prime_rows": prime_holes,
        "singleton_rows": singleton_holes,
        "shared_qs": shared_qs,
        "patch_factors_by_r": patch_factors_by_r,
    }


def format_record(rec: dict, detail: bool = False) -> str:
    """格式化单条记录。"""
    parts = [
        f"P={rec['P']}", f"a={rec['a']}", f"y={rec['y']}",
        f"H={rec['holes']}", f"prime={rec['prime_holes']}", f"comp={rec['composite_holes']}",
        f"single={rec['singleton_holes']}", f"multi={rec['multi_factor_holes']}",
        f"q*={rec['distinct_patch_q']}", f"shared_q={rec['shared_q']}",
        f"edges={rec['shared_edges']}", f"maxhit={rec['max_q_hit']}",
        f"cover≈{rec['greedy_cover']}", f"diff_bad={rec['diff_violations']}",
    ]
    text = " ".join(parts)
    if detail:
        top_shared = sorted(rec["shared_qs"].items(), key=lambda item: (-len(item[1]), item[0]))[:12]
        text += "\n  prime_rows=" + str(rec["prime_rows"][:80])
        text += "\n  singleton_rows=" + str(rec["singleton_rows"][:80])
        text += "\n  top_shared=" + str([(q, rows[:20], len(rows)) for q, rows in top_shared])
    return text


def scan_one_P(P: int, y: int, top: int) -> list[dict]:
    """扫描一个 P 下所有非零列。"""
    flags = sieve(P * P)
    root_primes = primes_from_flags(flags, P)
    records = [record_for(P, a, y, flags, root_primes) for a in range(1, P)]
    # 最危险：素数洞少、小筛洞少、补洞共享强。
    records.sort(key=lambda rec: (rec["prime_holes"], rec["holes"], -rec["shared_edges"], -rec["max_q_hit"]))
    return records[:top]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--P", type=int, default=1009)
    parser.add_argument("--a", type=int, default=1)
    parser.add_argument("--y", type=int, default=31)
    parser.add_argument("--scan", action="store_true")
    parser.add_argument("--maxP", type=int, default=1000)
    parser.add_argument("--Ps", default="")
    parser.add_argument("--ys", default="")
    parser.add_argument("--top", type=int, default=10)
    parser.add_argument("--detail", action="store_true")
    args = parser.parse_args()

    if args.Ps or args.ys:
        Ps = [int(x) for x in args.Ps.split(",") if x.strip()] or [args.P]
        ys = [int(x) for x in args.ys.split(",") if x.strip()] or [args.y]
        for P in Ps:
            for y in ys:
                rows = scan_one_P(P, y, min(args.top, P - 1))
                best = rows[0]
                print(format_record(best, args.detail))
        return

    if args.scan:
        flags = sieve(args.maxP)
        Ps = [p for p in primes_from_flags(flags, args.maxP) if p >= 3]
        global_rows = []
        for P in Ps:
            global_rows.extend(scan_one_P(P, args.y, min(args.top, P - 1)))
        global_rows.sort(key=lambda rec: (rec["prime_holes"], rec["holes"], -rec["shared_edges"], -rec["P"]))
        for rec in global_rows[:args.top]:
            print(format_record(rec, args.detail))
        print("checked_P", len(Ps), "records", len(global_rows), "missing_prime_records", sum(1 for r in global_rows if r["prime_holes"] == 0))
        return

    flags = sieve(args.P * args.P)
    root_primes = primes_from_flags(flags, args.P)
    print(format_record(record_for(args.P, args.a, args.y, flags, root_primes), args.detail))


if __name__ == "__main__":
    main()
