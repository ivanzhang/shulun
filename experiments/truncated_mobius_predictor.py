#!/usr/bin/env python3
"""截断 Möbius 短除数权 H_D(a) 与真实 H_z(a) 对比。

H_D(a)=sum_{r<P} sum_{d|M_z, d<=D} mu(d) 1_{d | a+rP}。
这是粗数指标的截断包含-排除近似，不保证非负/下界，但可检验集中与相关性。
"""
import argparse, math
from statistics import mean, pstdev
from high_threshold_margin_fast import sieve, primes, H_count


def squarefree_divisors(prs, D):
    divs=[(1,1)]
    for p in prs:
        new=[]
        for d,mu in divs:
            nd=d*p
            if nd<=D: new.append((nd,-mu))
        divs += new
    return divs

def H_trunc(P,a,divs):
    total=0
    for d,mu in divs:
        # count r in [0,P-1] with a+rP ≡0 mod d. gcd(P,d)=1 for d from primes <P.
        if d==1:
            cnt=P
        else:
            residue=(-a*pow(P,-1,d))%d
            cnt=0 if residue>=P else ((P-1-residue)//d)+1
        total += mu*cnt
    return total

def corr(xs,ys):
    mx=mean(xs); my=mean(ys); sx=pstdev(xs); sy=pstdev(ys)
    if sx==0 or sy==0: return 0
    return mean((x-mx)*(y-my) for x,y in zip(xs,ys))/(sx*sy)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--P',type=int,default=1009); ap.add_argument('--c',type=float,default=0.8); ap.add_argument('--Ds',default='10,30,100,300,1000,3000'); args=ap.parse_args()
    P=args.P; flags=sieve(P); root=primes(flags,P); y=int(args.c*P); small=[q for q in root if q<=y]
    real=[H_count(P,a,y,small) for a in range(1,P)]
    print(f'P={P} c={args.c} realMean={mean(real):.3f} realStd={pstdev(real):.3f} realMin={min(real)}')
    for D in [int(x) for x in args.Ds.split(',') if x.strip()]:
        divs=squarefree_divisors(small,D)
        pred=[H_trunc(P,a,divs) for a in range(1,P)]
        err=[p-r for p,r in zip(pred,real)]
        print(f'D={D} divs={len(divs)} mean={mean(pred):.3f} std={pstdev(pred):.3f} min={min(pred)} corr={corr(pred,real):.3f} errMean={mean(err):.3f} errStd={pstdev(err):.3f} maxAbsErr={max(abs(e) for e in err)}')
if __name__=='__main__': main()
