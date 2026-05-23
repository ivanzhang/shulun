"""
K3' explicit bound check.

Verifies the K3' explicit inequality:

    |E(P)| < 3P/4   for every prime P >= 5.

Concretely, the proof in frontier-honest-status-and-true-side-theorems-20260522.md
appendix A reduces this to:

    (P - 1 - |E(P)|) * (2P / log P)  >=  pi(P^2) - pi(P)        (A.4)

and uses Rosser-Schoenfeld + Montgomery-Vaughan to produce the explicit
constant 0.37247.  This script computes the actual |E(P)| numerically and
checks BOTH sides of (A.4) hold.

Run:
    python3 k3_prime_explicit_bound_check.py --pmax 1500
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

    print("# P\t|E(P)|\t3P/4\tlhs=A.4_LHS\trhs=pi(P^2)-pi(P)\tlhs>=rhs?\t|E|<3P/4?")

    all_pass_K3 = True
    all_pass_A4 = True
    for P in primes:
        if P < 5:
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
        rhs = pi_P2 - pi_P

        lhs_A4 = (P - 1 - exc) * (2 * P / log(P))
        bound_3P4 = 3 * P / 4.0

        ok_A4 = lhs_A4 >= rhs
        ok_K3 = exc < bound_3P4

        if not ok_A4:
            all_pass_A4 = False
        if not ok_K3:
            all_pass_K3 = False

        print(f"{P}\t{exc}\t{bound_3P4:.2f}\t{lhs_A4:.2f}\t{rhs}\t{ok_A4}\t{ok_K3}")

    print(f"# all_pass_A4 = {all_pass_A4}")
    print(f"# all_pass_K3' = {all_pass_K3}")


if __name__ == "__main__":
    main()
