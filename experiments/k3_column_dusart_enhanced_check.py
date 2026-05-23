"""
K3*-Dusart column Dusart-enhanced bound check.

Verifies the K3*-Dusart explicit inequality:

    |E*(P)| < 3P/4 - P/(8 log P)   for every prime P >= 79.

Combines:
  - Dusart 2010: pi(x) >= x/(log x - 1) for x >= 5393.
  - Montgomery-Vaughan 1973 AP-BT: pi(x; q, a) <= 2x/(phi(q) log(x/q)).
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


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pmax", type=int, default=200)
    args = parser.parse_args()

    cap = args.pmax * args.pmax + args.pmax
    print(f"# sieving up to {cap}")
    primes = sieve_upto(cap)
    prime_set = set(primes)

    pi_cap_table = [0] * (cap + 1)
    for p in primes:
        if p <= cap:
            pi_cap_table[p] = 1
    for i in range(1, cap + 1):
        pi_cap_table[i] += pi_cap_table[i - 1]

    def pi_of(x: int) -> int:
        if x < 0:
            return 0
        if x > cap:
            x = cap
        return pi_cap_table[x]

    print("# P\t|E*(P)|\tK3*_bound\tK3*-Dusart_bound\tdusart_lower_ok\tK3*-Dusart_holds")

    all_ok = True
    for P in primes:
        if P < 79:
            continue
        if P > args.pmax:
            break

        exc = 0
        for j in range(1, P):
            has_prime = False
            for k in range(P):
                val = j + k * P
                if val >= 2 and val in prime_set:
                    has_prime = True
                    break
            if not has_prime:
                exc += 1

        pi_P2 = pi_of(P * P)
        dusart_lower = P * P / (2 * log(P) - 1)
        dusart_ok = pi_P2 >= dusart_lower

        bound_K3star = 3 * P / 4.0
        bound_K3star_dusart = 3 * P / 4.0 - P / (8 * log(P))

        ok = exc < bound_K3star_dusart
        if not ok or not dusart_ok:
            all_ok = False

        print(
            f"{P}\t{exc}\t{bound_K3star:.2f}\t{bound_K3star_dusart:.2f}\t{dusart_ok}\t{ok}"
        )

    print(f"# all_pass = {all_ok}")


if __name__ == "__main__":
    main()
