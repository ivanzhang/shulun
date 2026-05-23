"""K3-trivial-K-term-Li 一般族审计：验证 K=3 (四项 Li 展开) 的额外节省。

K3-trivial-K-term-Li 上界：
    |E(P)| <= P - sum_{k=0..K} c_k * P / log^{k+1}(P) + O(P/log^{K+2}(P)),
where c_k = k! / 2^{k+1}.

K=2: 已在 k3_trivial_three_term_li_check.py 中验证。
K=3: 新增 c_3 = 6/16 = 3/8 系数项 P / log^4(P)。

本脚本对比 K=0,1,2,3 四阶截断的上界与实际 |E(P)|=0。
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


def li_k_term_bound(P: float, K: int) -> float:
    """K3-trivial-K-term-Li upper bound on |E(P)|."""
    lp = log(P)
    result = P
    fact = 1
    for k in range(K + 1):
        if k > 0:
            fact *= k
        coef = fact / (2 ** (k + 1))
        result -= coef * P / (lp ** (k + 1))
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pmax", type=int, default=500)
    args = parser.parse_args()

    cap = args.pmax * args.pmax + args.pmax
    print(f"# sieving up to {cap}")
    primes = sieve_upto(cap)

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

    print("# P\t|E|\tK=0_bound\tK=1_bound\tK=2_bound\tK=3_bound\tactual_saving_K=3 vs K=2")

    all_ok = True
    for P in primes:
        if P < 100:
            continue
        if P > args.pmax:
            break

        row_exc = 0
        for k in range(1, P):
            c = pi_of((k + 1) * P) - pi_of(k * P)
            if c == 0:
                row_exc += 1

        b0 = li_k_term_bound(P, 0)
        b1 = li_k_term_bound(P, 1)
        b2 = li_k_term_bound(P, 2)
        b3 = li_k_term_bound(P, 3)

        # K=3 should be tighter (smaller) than K=2 for large P
        # since 3rd term coefficient 3/8 > 0
        diff_2_3 = b2 - b3

        # Check K=3 bound holds (with slack)
        lp = log(P)
        slack = P / lp ** 5 + 2
        ok = row_exc <= b3 + slack
        if not ok:
            all_ok = False

        print(
            f"{P}\t{row_exc}\t{b0:.4f}\t{b1:.4f}\t{b2:.4f}\t{b3:.4f}\t{diff_2_3:.4f}"
        )

    print(f"# all_pass_K_term_Li_K=3 = {all_ok}")


if __name__ == "__main__":
    main()
