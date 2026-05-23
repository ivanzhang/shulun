"""
K3'''' three-term Dusart-enhanced bound check.

Verifies the K3'''' explicit inequality (Appendix H):

    |E(P)| < 3P/4 - P/(8 log P) - 0.1125 P / log^2 P
                                            for every prime P >= 180.

Uses Dusart 2010 three-term lower bound for pi(x):
    pi(x) >= x/log x * (1 + 1/log x + 1.8/log^2 x)   for x >= 32299.

Run:
    python3 k3_threeterm_dusart_bound_check.py --pmax 500
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
    parser.add_argument("--pmax", type=int, default=500)
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

    print(
        "# P\t|E|\t|E*|\tDusart_3term_pred\tactual_pi(P^2)\t"
        "Dusart_3term_ok\tK3''''_bound\tK3''''_holds\tK3*-3term_holds"
    )

    all_ok_dusart3 = True
    all_ok_row = True
    all_ok_col = True

    for P in primes:
        if P < 180:
            continue
        if P > args.pmax:
            break

        # row exceptions
        row_exc = 0
        for k in range(1, P):
            c = pi_of((k + 1) * P) - pi_of(k * P)
            if c == 0:
                row_exc += 1

        # column exceptions
        col_exc = 0
        for j in range(1, P):
            has_prime = False
            for kk in range(P):
                val = j + kk * P
                if val >= 2 and val in prime_set:
                    has_prime = True
                    break
            if not has_prime:
                col_exc += 1

        pi_P2 = pi_of(P * P)
        # Dusart 2010 三项：pi(x) >= x/log(x) * (1 + 1/log(x) + 1.8/log^2(x))
        log_P2 = 2 * log(P)
        dusart3 = (P * P / log_P2) * (1 + 1 / log_P2 + 1.8 / (log_P2 * log_P2))
        ok_d3 = pi_P2 >= dusart3
        if not ok_d3:
            all_ok_dusart3 = False

        bound_K3_4primes = (
            3 * P / 4.0 - P / (8 * log(P)) - 0.1125 * P / (log(P) ** 2)
        )

        ok_row = row_exc < bound_K3_4primes
        ok_col = col_exc < bound_K3_4primes

        if not ok_row:
            all_ok_row = False
        if not ok_col:
            all_ok_col = False

        print(
            f"{P}\t{row_exc}\t{col_exc}\t{dusart3:.2f}\t{pi_P2}\t{ok_d3}\t"
            f"{bound_K3_4primes:.4f}\t{ok_row}\t{ok_col}"
        )

    print(f"# all_pass_Dusart_3term_lower = {all_ok_dusart3}")
    print(f"# all_pass_K3'''' = {all_ok_row}")
    print(f"# all_pass_K3*-3term = {all_ok_col}")


if __name__ == "__main__":
    main()
