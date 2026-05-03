#!/usr/bin/env python3
"""比较实际大素数对数供给 S 与独立模型 |H| sum log(q)/q。"""
import argparse, math
from product_pressure_bound_scan import pressure
from rigid_patch_lemma_scan import sieve, primes_from_flags


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--Ps',default='251,503,1009'); ap.add_argument('--y-ratios',default='0.1,0.2,0.3,0.5'); args=ap.parse_args()
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]:
        flags=sieve(P*P); root=primes_from_flags(flags,P)
        for ratio in [float(x) for x in args.y_ratios.split(',') if x.strip()]:
            y=max(2,int(P*ratio)); big=[q for q in root if y<q<P]
            L=sum(math.log(q)/q for q in big)
            worst=(0,None); ratios=[]; margins=[]
            for a in range(1,P):
                S,D,rec=pressure(P,a,y,flags,root)
                pred=rec['holes']*L
                rho=S/pred if pred else 0
                ratios.append(rho); margins.append(D-S)
                if rho>worst[0]: worst=(rho,(a,S,pred,D,rec))
            a,S,pred,D,rec=worst[1]
            ratios.sort(); margins.sort()
            print(f"P={P} y={y} L=sumlog/q={L:.3f} logy={math.log(y):.3f} L/logy={L/math.log(y):.3f} rho_med={ratios[len(ratios)//2]:.3f} rho_max={worst[0]:.3f} margin_min={margins[0]:.2f} worst a={a} H={rec['holes']} prime={rec['prime_holes']} S/pred={S/pred if pred else 0:.3f} S/D={S/D if D else 0:.3f}")
if __name__=='__main__': main()
