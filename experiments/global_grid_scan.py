#!/usr/bin/env python3
"""素数 P×P 方阵的整行/整列全局扫描。

方阵按行优先排列自然数：第 r 行第 c 列为 N=rP+c+1（0<=r,c<P）。
根基模数库是第一行中的素数，即 2..P 中的素数。

用法示例：
  python3 experiments/global_grid_scan.py --P 101 --detail
  python3 experiments/global_grid_scan.py --scan --maxP 1000
"""
import argparse
import math


def sieve(n):
    """埃氏筛。"""
    arr = bytearray(b"\x01") * (n + 1)
    if n >= 0:
        arr[0] = 0
    if n >= 1:
        arr[1] = 0
    for p in range(2, math.isqrt(n) + 1):
        if arr[p]:
            start = p * p
            arr[start:n + 1:p] = b"\x00" * (((n - start) // p) + 1)
    return arr


def primes_upto(n):
    flags = sieve(n)
    return [i for i in range(2, n + 1) if flags[i]]


def record_for(P):
    """生成整行列记录。"""
    flags = sieve(P * P)
    root = primes_upto(P)
    row_prime_counts = []
    col_prime_counts = []
    row_root_cover_counts = []
    col_root_cover_counts = []
    for r in range(P):
        pcount = 0
        ccover = 0
        for c in range(P):
            N = r * P + c + 1
            if flags[N]:
                pcount += 1
            elif N > 1 and any(N % q == 0 for q in root):
                ccover += 1
        row_prime_counts.append(pcount)
        row_root_cover_counts.append(ccover)
    for c in range(P):
        pcount = 0
        ccover = 0
        for r in range(P):
            N = r * P + c + 1
            if flags[N]:
                pcount += 1
            elif N > 1 and any(N % q == 0 for q in root):
                ccover += 1
        col_prime_counts.append(pcount)
        col_root_cover_counts.append(ccover)
    zero_rows = [i for i, x in enumerate(row_prime_counts) if x == 0]
    zero_cols = [i for i, x in enumerate(col_prime_counts) if x == 0]
    return {
        "P": P,
        "root_count": len(root),
        "min_row_primes": min(row_prime_counts),
        "min_col_primes": min(col_prime_counts),
        "max_row_primes": max(row_prime_counts),
        "max_col_primes": max(col_prime_counts),
        "zero_rows": zero_rows,
        "zero_cols": zero_cols,
        "row_prime_counts": row_prime_counts,
        "col_prime_counts": col_prime_counts,
        "row_root_cover_counts": row_root_cover_counts,
        "col_root_cover_counts": col_root_cover_counts,
        "root": root,
    }


def print_record(rec, detail=False):
    """打印整行列记录。"""
    keys = ["P", "root_count", "min_row_primes", "min_col_primes", "max_row_primes", "max_col_primes"]
    print(",".join(f"{key}={rec[key]}" for key in keys) + f",zero_rows={len(rec['zero_rows'])},zero_cols={len(rec['zero_cols'])}")
    if detail:
        print(f"root={rec['root']}")
        print(f"row_prime_counts={rec['row_prime_counts']}")
        print(f"col_prime_counts={rec['col_prime_counts']}")
        print(f"zero_rows={rec['zero_rows']}")
        print(f"zero_cols={rec['zero_cols']}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--scan", action="store_true")
    parser.add_argument("--P", type=int, default=101)
    parser.add_argument("--maxP", type=int, default=1000)
    parser.add_argument("--detail", action="store_true")
    args = parser.parse_args()
    if args.scan:
        Ps = primes_upto(args.maxP)
        rows = [record_for(P) for P in Ps if P >= 2]
        rows.sort(key=lambda row: (row["min_row_primes"], row["min_col_primes"], -row["P"]))
        for rec in rows[:30]:
            print_record(rec)
        print(
            "checked", len(rows),
            "zero_row_total", sum(len(row["zero_rows"]) for row in rows),
            "zero_col_total", sum(len(row["zero_cols"]) for row in rows),
            "global_min_row", min(row["min_row_primes"] for row in rows),
            "global_min_col", min(row["min_col_primes"] for row in rows),
        )
    else:
        print_record(record_for(args.P), args.detail)


if __name__ == "__main__":
    main()
