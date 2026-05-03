#!/usr/bin/env python3
"""多点配置奇异级数采样。

对 tuple R=(r1..rk)，局部禁忌类数量 ν_q(R)=# distinct { -r_i P mod q }。
归一化奇异级数 ratio = prod_q (1-ν_q/q)/(1-1/q)^k。
采样检查平均是否 O(1)，高值是否稀少。
"""
import argparse, math, random
from statistics import mean, median
from high_threshold_margin_fast import sieve, primes


def singular_ratio(P, small, R):
    ratio=1.0
    for q in small:
        residues={r % q for r in R}  # P invertible, distinct count same
        nu=len(residues)
        if nu>=q: return 0.0
        ratio *= (1-nu/q)/((1-1/q)**len(R))
    return ratio

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--P',type=int,default=1009); ap.add_argument('--c',type=float,default=0.8); ap.add_argument('--k',type=int,default=4); ap.add_argument('--samples',type=int,default=20000); ap.add_argument('--seed',type=int,default=1); ap.add_argument('--distinct',action='store_true'); args=ap.parse_args()
    random.seed(args.seed); flags=sieve(args.P); root=primes(flags,args.P); y=int(args.c*args.P); small=[q for q in root if q<=y]
    vals=[]; zeros=0; maxv=0; maxR=None
    for _ in range(args.samples):
        R=tuple(random.sample(range(args.P), args.k)) if args.distinct else tuple(random.randrange(args.P) for _ in range(args.k))
        v=singular_ratio(args.P, small, R)
        if v==0: zeros+=1
        if v>maxv: maxv=v; maxR=R
        vals.append(v)
    vals_sorted=sorted(vals)
    def qtile(q): return vals_sorted[int(q*(len(vals_sorted)-1))]
    print(f"P={args.P} c={args.c} k={args.k} distinct={args.distinct} samples={args.samples} mean={mean(vals):.4f} median={median(vals):.4f} zero={zeros/args.samples:.4f} p90={qtile(0.9):.4f} p99={qtile(0.99):.4f} max={maxv:.4f} maxR={maxR}")
if __name__=='__main__': main()
