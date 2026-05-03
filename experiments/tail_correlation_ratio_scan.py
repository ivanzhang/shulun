#!/usr/bin/env python3
"""扫描尾部相关量 T_c(P,a)/|H_{cP}(a)|。

H_y(a): 避开所有 q<=y 的小筛洞。
T_y(a): sum_{y<q<P} |H_y(a) ∩ {r ≡ -aP^{-1} mod q}|，排除 n=q 自身。
若 T_y(a)<|H_y(a)|，则尾部大素数无法覆盖全部 H_y(a)，列中存在素数。

用法：
  python3 experiments/tail_correlation_ratio_scan.py --Ps 251,503,1009,2003 --cs 0.3,0.5,0.7,0.9
"""
import argparse, math
from statistics import median
from rigid_patch_lemma_scan import sieve, primes_from_flags, record_for


def tail_T(P, a, y, rec, root):
    holes = set(rec['holes_list'])
    T = 0
    q_nonzero = 0
    max_hit = 0
    for q in root:
        if not (y < q < P):
            continue
        residue = (-a * pow(P, -1, q)) % q
        hit = 0
        for r in range(residue, P, q):
            if r in holes and a + r * P != q:
                hit += 1
        if hit:
            q_nonzero += 1
            max_hit = max(max_hit, hit)
            T += hit
    return T, q_nonzero, max_hit


def scan(P, c):
    y = int(c * P)
    flags = sieve(P * P)
    root = primes_from_flags(flags, P)
    rows = []
    for a in range(1, P):
        rec = record_for(P, a, y, flags, root)
        T, qnz, maxhit = tail_T(P, a, y, rec, root)
        H = rec['holes']
        ratio = T / H if H else 0
        model = sum(1 / q for q in root if y < q < P)
        rows.append((ratio, T, H, rec['prime_holes'], rec['composite_holes'], qnz, maxhit, a, model))
    rows.sort(reverse=True)
    ratios = [r[0] for r in rows]
    top = rows[0]
    return y, top, median(ratios), sum(ratios) / len(ratios), rows


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--Ps', default='251,503,1009,2003')
    parser.add_argument('--cs', default='0.3,0.5,0.7,0.9')
    parser.add_argument('--show', type=int, default=3)
    args = parser.parse_args()
    print('P c y maxRatio medRatio avgRatio modelSum1q top[a,T,H,prime,comp,qnz,maxhit]')
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]:
        for c in [float(x) for x in args.cs.split(',') if x.strip()]:
            y, top, medr, avgr, rows = scan(P, c)
            ratio,T,H,prime,comp,qnz,maxhit,a,model = top
            print(f"{P} {c:.2f} {y} {ratio:.4f} {medr:.4f} {avgr:.4f} {model:.4f} top=[{a},{T},{H},{prime},{comp},{qnz},{maxhit}]")
            for extra in rows[1:args.show]:
                er, eT, eH, ep, ec, eq, em, ea, _ = extra
                print(f"  next a={ea} ratio={er:.4f} T={eT} H={eH} prime={ep} comp={ec} qnz={eq} maxhit={em}")

if __name__ == '__main__':
    main()
