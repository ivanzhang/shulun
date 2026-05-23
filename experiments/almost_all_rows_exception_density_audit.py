"""
Almost-all rows exception-density audit
========================================

For each prime P, count the rows i in [1, P-1] of the P x P matrix
A_{i,j} = (i-1)P + j whose row interval I_i = ((i-1)P, iP] is
*prime-free*.  Empirically tracks |E(P)| / P and |E(P)| * log P / P
versus P.

Status note (2026-05-22):
This audit is NOT a proof of H_P.  It is the rigorous empirical side
of side-theorem K (almost-all rows contain a prime), proven
unconditionally via Heath-Brown 1979 second-moment of theta(x+h)-theta(x)
combined with BHP 2001 short-interval prime existence on h = x^{0.525}.

Run:
    python3 almost_all_rows_exception_density_audit.py --pmax 4999
"""
from __future__ import annotations
import argparse
from math import isqrt, log


def sieve_upto(n: int) -> list[int]:
    sv = bytearray(b"\x01") * (n + 1)
    sv[0] = sv[1] = 0
    for i in range(2, isqrt(n) + 1):
        if sv[i]:
            step = i
            start = i * i
            sv[start : n + 1 : step] = b"\x00" * (((n - start) // step) + 1)
    return [i for i, b in enumerate(sv) if b]


def count_primes_in_range(primes_sorted: list[int], lo: int, hi: int) -> int:
    """Count primes p with lo < p <= hi via binary search."""
    from bisect import bisect_left, bisect_right

    return bisect_right(primes_sorted, hi) - bisect_right(primes_sorted, lo)


def exception_count_for_P(P: int, primes_upto_P2: list[int]) -> tuple[int, int, int]:
    """Return (|E(P)|, total_row_primes, max_row_primes)."""
    exc = 0
    total = 0
    mx = 0
    for k in range(1, P):
        lo = k * P
        hi = (k + 1) * P
        c = count_primes_in_range(primes_upto_P2, lo, hi)
        total += c
        if c == 0:
            exc += 1
        if c > mx:
            mx = c
    return exc, total, mx


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pmax", type=int, default=4999)
    parser.add_argument("--sample-stride", type=int, default=1,
                        help="audit only every k-th prime to limit runtime")
    args = parser.parse_args()

    cap = args.pmax * args.pmax + args.pmax
    print(f"# sieving primes up to {cap}")
    primes = sieve_upto(cap)
    primes_set = set(primes)

    print(f"# loaded {len(primes)} primes up to {cap}")
    print("# P\t|E(P)|\tP-1\t|E|/P\t|E|*logP/P\tmax_row\trow_mean")
    cnt = 0
    for P in primes:
        if P < 7:
            continue
        if P > args.pmax:
            break
        cnt += 1
        if (cnt - 1) % args.sample_stride != 0:
            continue
        exc, total, mx = exception_count_for_P(P, primes)
        ratio = exc / (P - 1)
        scaled = ratio * log(P) if P > 1 else 0
        mean = total / (P - 1) if P > 1 else 0
        print(f"{P}\t{exc}\t{P-1}\t{ratio:.4f}\t{scaled:.4f}\t{mx}\t{mean:.4f}")


if __name__ == "__main__":
    main()
