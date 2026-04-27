#!/usr/bin/env python3
"""扫描 residue energy 危险样本。

用法示例：
  python3 experiments/scan_residue_danger.py --primes 999983,1999993 --cols 80
"""
import argparse, math, random, importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location(
    "verify_buchstab", Path(__file__).with_name("verify_buchstab.py")
)
vb = importlib.util.module_from_spec(spec)
spec.loader.exec_module(vb)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--primes", default="999983,1999993,2999933")
    ap.add_argument("--cols", type=int, default=50)
    ap.add_argument("--C", type=float, default=8.0)
    ap.add_argument("--fractions", default="1,0.75,0.5,0.3,0.2,0.1,0.05,0.02")
    args = ap.parse_args()

    Ps = [int(x) for x in args.primes.split(",") if x.strip()]
    max_p = max(Ps)
    max_k = int(args.C * math.log(max_p) ** 2)
    max_needed = math.isqrt(max_p + max_k * max_p) + 2000
    primes = vb.primes_upto_from_sieve(vb.sieve(max_needed))
    fractions = [float(x) for x in args.fractions.split(",")]

    rows = []
    for P in Ps:
        random.seed(P)
        base_cols = [1, 2, 6, 30, P // 2, P - 1]
        sample_n = min(args.cols, P - 1)
        cols = list(dict.fromkeys(base_cols + random.sample(range(1, P), sample_n)))
        for c in cols:
            for frac in fractions:
                row = vb.analyze(P, c, args.C, primes, frac)
                # 危险度：相关高且素数缺口比例低
                gap_ratio = row["gap"] / row["R"] if row["R"] else 0
                danger = row["RB_corr"] - gap_ratio
                rows.append((danger, row["RB_corr"], gap_ratio, row))

    rows.sort(reverse=True, key=lambda x: x[0])
    print("top danger: danger,corr,gap/R,P,c,K,delta,R,B,gap,R_E,B_E,R_occ,B_occ,first_prime")
    for danger, corr, gap_ratio, row in rows[:25]:
        print(
            f"{danger:.3f},{corr:.3f},{gap_ratio:.3f},{row['P']},{row['c']},{row['K']},"
            f"{row['delta']},{row['R']},{row['B']},{row['gap']},{row['R_energy']},"
            f"{row['B_energy']},{row['R_occupied']},{row['B_occupied']},{row['first_prime_t']}"
        )

    print("\nmax corr samples")
    rows_corr = sorted(rows, reverse=True, key=lambda x: x[1])
    for danger, corr, gap_ratio, row in rows_corr[:15]:
        print(
            f"corr={corr:.3f} gap/R={gap_ratio:.3f} P={row['P']} c={row['c']} "
            f"delta={row['delta']} R={row['R']} B={row['B']} gap={row['gap']}"
        )


if __name__ == "__main__":
    main()
