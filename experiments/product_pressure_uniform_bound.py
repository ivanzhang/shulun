#!/usr/bin/env python3
"""乘积压力的统一容量上界检查。

比较 U(y,P)=sum_{y<q<P} ceil(P/q) log q 与 min_a |H_y(a)| log y。
若 U < minH log y，则不用分解即可证明所有列有洞。
"""
import argparse, math
from rigid_patch_lemma_scan import sieve, primes_from_flags, record_for


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--Ps',default='251,503,1009,2003,4001'); ap.add_argument('--y-ratios',default='0.1,0.2,0.3,0.5,0.7'); args=ap.parse_args()
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]:
        flags=sieve(P*P); root=primes_from_flags(flags,P)
        for ratio in [float(x) for x in args.y_ratios.split(',') if x.strip()]:
            y=max(2,int(P*ratio))
            big=[q for q in root if y<q<P]
            U=sum(math.ceil(P/q)*math.log(q) for q in big)
            minH=10**9; maxH=0; mina=None
            for a in range(1,P):
                rec=record_for(P,a,y,flags,root)
                if rec['holes']<minH: minH=rec['holes']; mina=a
                maxH=max(maxH,rec['holes'])
            D=minH*math.log(y)
            print(f"P={P} y={y} ratio={ratio:.2f} bigQ={len(big)} U={U:.2f} minH={minH} maxH={maxH} Dmin={D:.2f} U/D={U/D if D else 0:.3f} mina={mina} proves={U<D}")
if __name__=='__main__': main()
