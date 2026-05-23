"""
K3-trivial-three-term-Li internal self-contained bound check.

Verifies the K3-trivial-three-term-Li inequality (Appendix M):

    |E(P)| <= P - P/(2 log P) - P/(4 log^2 P) - P/(4 log^3 P) + O(P/log^4 P)

This uses only PNT internal information (Li(x) asymptotic expansion +
de la Vallee-Poussin 1899 remainder), no sieve.

Run:
    python3 k3_trivial_three_term_li_check.py --pmax 500
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

    print("# P\t|E|\t|E*|\tK3-trivial-enhanced\tK3-trivial-3term-Li\tdiff\trow_ok\tcol_ok")

    all_ok_row = True
    all_ok_col = True
    for P in primes:
        if P < 100:
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

        lp = log(P)
        bound_enh = P - P / (2 * lp) - P / (4 * lp * lp)
        bound_3term = bound_enh - P / (4 * lp ** 3)

        # Allow small O(P/log^4 P) slack for big-O term
        slack = P / (lp ** 4) + 1

        ok_row = row_exc <= bound_3term + slack
        ok_col = col_exc <= bound_3term + slack
        if not ok_row:
            all_ok_row = False
        if not ok_col:
            all_ok_col = False

        print(
            f"{P}\t{row_exc}\t{col_exc}\t{bound_enh:.4f}\t{bound_3term:.4f}\t"
            f"{bound_enh - bound_3term:.4f}\t{ok_row}\t{ok_col}"
        )

    print(f"# all_pass_K3-trivial-3term-Li_row = {all_ok_row}")
    print(f"# all_pass_K3-trivial-3term-Li_col = {all_ok_col}")


if __name__ == "__main__":
    main()
