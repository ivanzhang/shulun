#!/usr/bin/env python3
"""扫描每个列的 sqrt(P) 窗口中粗候选/粗素数/粗合数分布。"""
from __future__ import annotations
from math import isqrt


def sieve(n: int) -> list[bool]:
    is_prime = [True] * (n + 1)
    if n >= 0: is_prime[0] = False
    if n >= 1: is_prime[1] = False
    for p in range(2, isqrt(n) + 1):
        if is_prime[p]:
            for j in range(p*p, n+1, p):
                is_prime[j] = False
    return is_prime


def primes_upto(n: int) -> list[int]:
    s = sieve(n)
    return [i for i,v in enumerate(s) if v]


def scan(P: int) -> dict:
    D = isqrt(P)
    prime_table = sieve(P*P)
    small = primes_upto(D)
    worst = None
    zero_rough_prime_windows = 0
    total_windows = 0
    for c in range(1, P):
        rough = []
        rough_prime = []
        rough_comp = []
        for k in range(P):
            n = k*P+c
            if n >= 2 and all(n % q for q in small):
                rough.append(k)
                if prime_table[n]: rough_prime.append(k)
                else: rough_comp.append(k)
        rp = set(rough_prime)
        rr = set(rough)
        rc = set(rough_comp)
        for a in range(0, P-D+1):
            total_windows += 1
            r_count = sum(1 for k in range(a, a+D) if k in rr)
            p_count = sum(1 for k in range(a, a+D) if k in rp)
            c_count = sum(1 for k in range(a, a+D) if k in rc)
            if r_count and p_count == 0:
                zero_rough_prime_windows += 1
                item = {"P":P,"c":c,"start":a,"D":D,"rough":r_count,"rough_prime":p_count,"rough_comp":c_count}
                if worst is None or item["rough"] > worst["rough"]:
                    worst = item
    return {"P":P,"D":D,"zero_rough_prime_windows":zero_rough_prime_windows,"total_windows":total_windows,"worst":worst}


def main():
    for P in [101,251,503,1009]:
        print(scan(P))

if __name__ == "__main__":
    main()
