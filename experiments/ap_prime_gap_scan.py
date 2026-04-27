#!/usr/bin/env python3
"""扫描模 P 剩余类在 P^2 内的首个素数位置。

列 c 对应数列 c+1 + rP。若 c=P-1，则第一项 P 是素数，其余都是 P 的倍数。
其他列对应 gcd(a,P)=1 的等差数列 a mod P。

用法示例：
  python3 experiments/ap_prime_gap_scan.py --P 101 --detail
  python3 experiments/ap_prime_gap_scan.py --scan --maxP 2000
"""
import argparse
import math


def sieve(n):
    arr = bytearray(b"\x01") * (n + 1)
    if n >= 0:
        arr[0] = 0
    if n >= 1:
        arr[1] = 0
    for p in range(2, math.isqrt(n) + 1):
        if arr[p]:
            arr[p*p:n+1:p] = b"\x00" * (((n - p*p)//p) + 1)
    return arr


def primes_upto(n):
    flags=sieve(n)
    return [i for i in range(2,n+1) if flags[i]]


def record_for(P):
    flags = sieve(P * P)
    first = []
    for a in range(1, P + 1):
        pos = None
        val = None
        for r in range(P):
            N = a + r * P
            if flags[N]:
                pos = r
                val = N
                break
        first.append((pos, a, val))
    worst = max(first, key=lambda x: x[0] if x[0] is not None else P + 1)
    missing = [x for x in first if x[0] is None]
    return {
        "P": P,
        "worst_r": worst[0],
        "worst_a": worst[1],
        "worst_prime": worst[2],
        "missing": missing,
        "first": first,
    }


def print_record(rec, detail=False):
    print(f"P={rec['P']},worst_r={rec['worst_r']},worst_a={rec['worst_a']},worst_prime={rec['worst_prime']},missing={len(rec['missing'])}")
    if detail:
        print("first_r,a,prime")
        for row in sorted(rec["first"], reverse=True)[:50]:
            print(row)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--scan',action='store_true')
    parser.add_argument('--P',type=int,default=101)
    parser.add_argument('--maxP',type=int,default=2000)
    parser.add_argument('--detail',action='store_true')
    args=parser.parse_args()
    if args.scan:
        rows=[record_for(P) for P in primes_upto(args.maxP)]
        rows.sort(key=lambda x:(-(x['worst_r'] if x['worst_r'] is not None else 10**9), -x['P']))
        for rec in rows[:30]: print_record(rec)
        print('checked',len(rows),'missing_total',sum(len(r['missing']) for r in rows),'max_worst_r',rows[0]['worst_r'])
    else:
        print_record(record_for(args.P), args.detail)

if __name__=='__main__': main()
