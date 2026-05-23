"""K3'''' 修正系数的行/列数值审计。

用法示例：
  python3 experiments/k3_quadruple_prime_corrected_check.py --pmax 500

早期草稿把 Dusart 三项中的 0.225 P^2/log^3 P 除以 2P/logP 后写成
0.05625 P/log^2 P。逐行重算给出正确系数 0.1125：

  0.225 * P^2/log^3 P * logP/(2P) = 0.1125 P/log^2 P.

本脚本同时核对行例外 E(P) 与列例外 E*(P) 是否满足修正后的更紧上界。
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

    prime_set = set(primes)

    print("# P\t|E(P)|\t|E*(P)|\tK3''''_OLD\tK3''''_CORR\tK3''''_DiffOld-Corr\trow_hold?\tcol_hold?")

    all_ok_row = True
    all_ok_col = True
    for P in primes:
        if P < 180:
            continue
        if P > args.pmax:
            break

        # 行例外：第 k 行区间 (kP, (k+1)P] 中没有素数。
        exc = 0
        for k in range(1, P):
            c = pi_in_range(primes, k * P, (k + 1) * P)
            if c == 0:
                exc += 1

        # 列例外：固定 residue j mod P 的 P 方阵列中没有素数。
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

        old_bound = 3 * P / 4.0 - P / (8 * log(P)) - 0.05625 * P / (log(P) ** 2) - 0.37247
        corr_bound = 3 * P / 4.0 - P / (8 * log(P)) - 0.1125 * P / (log(P) ** 2) - 0.37247

        ok_row = exc < corr_bound
        ok_col = col_exc < corr_bound
        if not ok_row:
            all_ok_row = False
        if not ok_col:
            all_ok_col = False

        print(
            f"{P}\t{exc}\t{col_exc}\t{old_bound:.4f}\t{corr_bound:.4f}\t"
            f"{old_bound - corr_bound:.4f}\t{ok_row}\t{ok_col}"
        )

    print(f"# all_pass_K3''''_corrected_row = {all_ok_row}")
    print(f"# all_pass_K3''''_corrected_col = {all_ok_col}")


if __name__ == "__main__":
    main()
