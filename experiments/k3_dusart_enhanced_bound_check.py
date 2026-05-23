"""
K3''' Dusart-enhanced bound check.

Verifies the K3''' explicit inequality:

    |E(P)| < 3P/4 - P/(8 log P)   for every prime P >= 79.

The proof in frontier-honest-status-and-true-side-theorems-20260522.md
appendix C combines:
  - Dusart 2010: pi(x) >= x/(log x - 1) for x >= 5393.
  - Rosser-Schoenfeld 1962: pi(x) < 1.25506 x / log x for x > 1.
  - Montgomery-Vaughan 1973: pi(x+y)-pi(x) <= 2y/log y for y >= 2.

Run:
    python3 k3_dusart_enhanced_bound_check.py --pmax 1500
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


def pi_in_range(primes_sorted: list[int], lo: int, hi: int) -> int:
    from bisect import bisect_right
    return bisect_right(primes_sorted, hi) - bisect_right(primes_sorted, lo)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pmax", type=int, default=1500)
    args = parser.parse_args()

    cap = args.pmax * args.pmax + args.pmax
    print(f"# sieving up to {cap}")
    primes = sieve_upto(cap)

    print(
        "# P\t|E(P)|\tK3'_bound=3P/4-0.37\tK3'''_bound=3P/4-P/(8logP)\t"
        "C.1_LHS\tC.1_RHS\tC.1_OK\tK3'''_holds?"
    )

    all_pass_C1 = True
    all_pass_K3_triple = True
    all_pass_dusart_lower = True

    for P in primes:
        if P < 79:
            continue
        if P > args.pmax:
            break

        exc = 0
        for k in range(1, P):
            c = pi_in_range(primes, k * P, (k + 1) * P)
            if c == 0:
                exc += 1

        pi_P2 = pi_in_range(primes, 0, P * P)
        pi_P = pi_in_range(primes, 0, P)

        # Verify Dusart 2010 lower bound: pi(P^2) >= P^2 / (2 log P - 1)
        dusart_pred = P * P / (2 * log(P) - 1)
        dusart_ok = pi_P2 >= dusart_pred
        if not dusart_ok:
            all_pass_dusart_lower = False

        # C.1 LHS = (P-1-|E|) * 2P / log P
        # C.1 RHS = P^2 / (2 log P - 1) - 1.25506 P / log P  (used in proof)
        lhs_C1 = (P - 1 - exc) * (2 * P / log(P))
        rhs_C1 = P * P / (2 * log(P) - 1) - 1.25506 * P / log(P)
        ok_C1 = lhs_C1 >= rhs_C1
        if not ok_C1:
            all_pass_C1 = False

        bound_K3prime = 3 * P / 4.0 - 0.37247
        bound_K3triple = 3 * P / 4.0 - P / (8 * log(P))

        ok_K3triple = exc < bound_K3triple
        if not ok_K3triple:
            all_pass_K3_triple = False

        print(
            f"{P}\t{exc}\t{bound_K3prime:.2f}\t{bound_K3triple:.2f}\t"
            f"{lhs_C1:.2f}\t{rhs_C1:.2f}\t{ok_C1}\t{ok_K3triple}"
        )

    print(f"# all_pass_Dusart_lower = {all_pass_dusart_lower}")
    print(f"# all_pass_C1 = {all_pass_C1}")
    print(f"# all_pass_K3''' = {all_pass_K3_triple}")


if __name__ == "__main__":
    main()
