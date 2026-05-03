#!/usr/bin/env python3
"""列素数计数字符谱累计能量与危险列重构比例。"""
import argparse
import cmath
import math
from danger_column_character_spectrum import sieve, primitive_root_prime, dft, column_prime_counts


def analyze(P, ks):
    counts = column_prime_counts(P)
    mean = sum(counts[1:]) / (P - 1)
    min_a = min(range(1, P), key=lambda a: counts[a])
    g = primitive_root_prime(P)
    powers = []
    x = 1
    for _ in range(P - 1):
        powers.append(x)
        x = (x * g) % P
    n = P - 1
    seq = [counts[a] - mean for a in powers]
    coeffs = dft(seq)
    ranked = sorted(range(1, n), key=lambda m: abs(coeffs[m]), reverse=True)
    total_energy = sum(abs(c) ** 2 for c in coeffs[1:])
    t_min = {a: t for t, a in enumerate(powers)}[min_a]
    true_dev = counts[min_a] - mean
    print(f"P={P} min_a={min_a} min={counts[min_a]} mean={mean:.4f} true_dev={true_dev:.4f} total_energy={total_energy/n/n:.4f}")
    recon = 0j
    energy = 0.0
    next_i = 0
    for k in sorted(ks):
        while next_i < k and next_i < len(ranked):
            m = ranked[next_i]
            recon += coeffs[m] * cmath.exp(2j * math.pi * m * t_min / n) / n
            energy += abs(coeffs[m]) ** 2
            next_i += 1
        print(f"  k={k} energy_frac={energy/total_energy:.4f} recon={recon.real:.4f} recon_frac={recon.real/true_dev if true_dev else 0:.4f}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--Ps', default='251,503,1009')
    ap.add_argument('--ks', default='8,16,32,64,128,256')
    args = ap.parse_args()
    ks = [int(x) for x in args.ks.split(',') if x.strip()]
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]:
        analyze(P, ks)

if __name__ == '__main__':
    main()
