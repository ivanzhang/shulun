"""
K3'''' corrected bound (factor-of-2 self-audit fix) verification.

The original Appendix H gave coefficient 0.05625 on P/log^2 P.
Atomic re-derivation: 0.225 * P^2/log^3 P times log P / (2P) = 0.225 P/(2 log^2 P) = 0.1125 P/log^2 P.

So the correct coefficient is 0.1125, not 0.05625. The earlier bound was looser by factor 2.
Both forms are still upper bounds on |E(P)|; the corrected version is strictly tighter.

This script verifies BOTH bounds for primes in [180, 500].
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
    parser.add_argument("--pmax", type=int, default=500)
    args = parser.parse_args()

    cap = args.pmax * args.pmax + args.pmax
    print(f"# sieving up to {cap}")
    primes = sieve_upto(cap)

    print("# P\t|E(P)|\tK3''''_OLD\tK3''''_CORR\tK3''''_DiffOld-Corr\tboth_hold?")

    all_ok = True
    for P in primes:
        if P < 180:
            continue
        if P > args.pmax:
            break

        exc = 0
        for k in range(1, P):
            c = pi_in_range(primes, k * P, (k + 1) * P)
            if c == 0:
                exc += 1

        old_bound = 3 * P / 4.0 - P / (8 * log(P)) - 0.05625 * P / (log(P) ** 2) - 0.37247
        corr_bound = 3 * P / 4.0 - P / (8 * log(P)) - 0.1125 * P / (log(P) ** 2) - 0.37247

        ok = exc < corr_bound  # tighter bound, automatically implies old
        if not ok:
            all_ok = False

        print(f"{P}\t{exc}\t{old_bound:.4f}\t{corr_bound:.4f}\t{old_bound - corr_bound:.4f}\t{ok}")

    print(f"# all_pass_K3''''_corrected = {all_ok}")


if __name__ == "__main__":
    main()
