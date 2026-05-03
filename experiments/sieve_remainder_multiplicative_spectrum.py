#!/usr/bin/env python3
"""H_c(P,a) 在乘法群 (Z/PZ)^* 上的角色谱分析。"""
import argparse, math, cmath
from statistics import mean, pstdev
from high_threshold_margin_fast import sieve, primes, H_count
from danger_column_character_spectrum import primitive_root_prime, dft


def analyze(P,c,top):
    flags=sieve(P); root=primes(flags,P); y=int(c*P); small=[q for q in root if q<=y]
    counts=[0]*P
    for a in range(1,P): counts[a]=H_count(P,a,y,small)
    mu=mean(counts[1:]); sd=pstdev(counts[1:]); mn=min(counts[1:]); mx=max(counts[1:])
    g=primitive_root_prime(P); powers=[]; x=1
    for _ in range(P-1): powers.append(x); x=x*g%P
    seq=[counts[a]-mu for a in powers]
    coeff=dft(seq); n=P-1
    ranked=sorted(range(1,n), key=lambda m: abs(coeff[m]), reverse=True)[:top]
    energy=sum(abs(coeff[m])**2 for m in range(1,n))/(n*n)
    l1=sum(abs(coeff[m]) for m in range(1,n))/n
    l2=math.sqrt((n-1)*sum(abs(coeff[m])**2 for m in range(1,n)))/n
    print(f'P={P} c={c} mean={mu:.3f} sd={sd:.3f} min={mn} max={mx} energy={energy:.3f} L1bound={l1:.2f} L2bound={l2:.2f}')
    print(' top', [(m, round(abs(coeff[m])/n,3)) for m in ranked])


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--Ps',default='251,503,1009'); ap.add_argument('--c',type=float,default=0.8); ap.add_argument('--top',type=int,default=12); args=ap.parse_args()
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]: analyze(P,args.c,args.top)
if __name__=='__main__': main()
