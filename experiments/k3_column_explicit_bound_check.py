"""
K3* column explicit bound check.

Verifies the K3* explicit inequality:

    |E*(P)| < 3P/4   for every prime P >= 5,

where E*(P) is the set of columns j in [1, P-1] of the P x P matrix
A(P)_{i,j} = (i-1)*P + j whose column contains no prime.

The proof in frontier-honest-status-and-true-side-theorems-20260522.md
appendix B reduces this to:

    (P - 1 - |E*(P)|) * (2 P^2 / ((P-1) log P))  >=  pi(P^2) - 2     (B.4)

Run:
    python3 k3_column_explicit_bound_check.py --pmax 200
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

    print("# P\t|E*(P)|\t3P/4\tlhs=B.4_LHS\trhs=pi(P^2)-2\tlhs>=rhs?\t|E*|<3P/4?")

    all_pass_B4 = True
    all_pass_K3star = True
    for P in primes:
        if P < 5:
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
        rhs = pi_P2 - 2

        lhs_B4 = (P - 1 - exc) * (2 * P * P / ((P - 1) * log(P)))
        bound_3P4 = 3 * P / 4.0

        ok_B4 = lhs_B4 >= rhs
        ok_K3star = exc < bound_3P4

        if not ok_B4:
            all_pass_B4 = False
        if not ok_K3star:
            all_pass_K3star = False

        print(f"{P}\t{exc}\t{bound_3P4:.2f}\t{lhs_B4:.2f}\t{rhs}\t{ok_B4}\t{ok_K3star}")

    print(f"# all_pass_B4 = {all_pass_B4}")
    print(f"# all_pass_K3* = {all_pass_K3star}")


if __name__ == "__main__":
    main()
