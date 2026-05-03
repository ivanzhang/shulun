#!/usr/bin/env python3
"""局部窗口 Z_J 的方差与二点差分模型。"""
import argparse, math
from statistics import mean
from high_threshold_margin_fast import sieve, primes
from pair_corr_singular_model import model_ratio


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--P',type=int,default=1009); ap.add_argument('--C',type=float,default=4.0); args=ap.parse_args()
    P=args.P; B=math.isqrt(P); L=max(1,int(args.C*math.sqrt(P))); flags=sieve(P*P+P); small=primes(sieve(B),B)
    # 实际 Z 窗口（步长1，P=1009/2003可接受）
    Zs=[]; As=[]
    for row in range(1,P+1):
        A=[0]*(P+1); Z=[0]*(P+1)
        for c in range(1,P+1):
            n=(row-1)*P+c
            cand=all(n%q for q in small)
            A[c]=A[c-1]+cand
            Z[c]=Z[c-1]+(cand and flags[n])
        for start in range(1,P-L+2):
            end=start+L-1
            As.append(A[end]-A[start-1]); Zs.append(Z[end]-Z[start-1])
    mu=mean(Zs); var=mean((z-mu)**2 for z in Zs)
    # 筛候选二点奇异级数窗口权重模型：sum_{d<L}(L-d)(S2(d)-1)
    root=primes(sieve(P),P); smallB=[q for q in root if q<=B]
    p=1.0
    for q in smallB: p*=1-1/q
    excess=0.0; abs_excess=0.0
    for d in range(1,L):
        s=model_ratio(d,smallB)
        term=(L-d)*(s-1)
        excess+=term; abs_excess+=abs(term)
    print(f'P={P} C={args.C} B={B} L={L} windows={len(Zs)}')
    print(f'actual meanZ={mu:.6f} varZ={var:.6f} var/mean={var/mu:.4f} meanA={mean(As):.6f} minZ={min(Zs)} zero={sum(1 for z in Zs if z==0)}')
    print(f'sieve pB={p:.6f} Lp={L*p:.3f} pairExcess={excess:.3f} pairExcess/(LlogL)={excess/(L*math.log(L)):.4f} absExcess/(LlogL)={abs_excess/(L*math.log(L)):.3f}')

if __name__=='__main__': main()
