#!/usr/bin/env python3
"""检查乘积压力判据 S_y(a) < |H_y(a)| log y 的强度。

S_y(a)=sum_{q in (y,P)} v_q(prod_{r in H_y}(a+rP))*log q。
若 S_y(a)<|H_y|log y，则 H_y 不可能全合，因此列有素数。

用法：
  python3 experiments/product_pressure_bound_scan.py --Ps 251,503,1009,2003 --y-ratios 0.1,0.2,0.3,0.5
"""
import argparse, math
from product_valuation_pressure import valuation
from rigid_patch_lemma_scan import sieve, primes_from_flags, record_for


def pressure(P,a,y,flags,root):
    rec=record_for(P,a,y,flags,root); S=0.0
    for r in rec['holes_list']:
        n=a+r*P
        for q in root:
            if y<q<P and n!=q and n%q==0:
                S += valuation(n,q)*math.log(q)
    demand=len(rec['holes_list'])*math.log(y)
    return S,demand,rec

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--Ps',default='251,503,1009,2003'); ap.add_argument('--y-ratios',default='0.1,0.2,0.3,0.5'); args=ap.parse_args()
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]:
        flags=sieve(P*P); root=primes_from_flags(flags,P)
        for ratio in [float(x) for x in args.y_ratios.split(',') if x.strip()]:
            y=max(2,int(P*ratio))
            # choose largest prime <= y? record small primes <=y accepts any int.
            proved=0; worst=(-1,None,None,None)
            min_margin=10**9; dangerous=None
            for a in range(1,P):
                S,D,rec=pressure(P,a,y,flags,root)
                margin=D-S
                if margin>0: proved+=1
                if margin<min_margin: min_margin=margin; dangerous=(a,S,D,rec)
                ratioSD=S/D if D else 0
                if ratioSD>worst[0]: worst=(ratioSD,a,S,D)
            a,S,D,rec=dangerous
            print(f"P={P} y={y} ratio={ratio:.2f} proved={proved}/{P-1} worstS/D={worst[0]:.3f} minMargin={min_margin:.2f} danger a={a} H={rec['holes']} prime={rec['prime_holes']} comp={rec['composite_holes']} S/D={S/D if D else 0:.3f}")
if __name__=='__main__': main()
