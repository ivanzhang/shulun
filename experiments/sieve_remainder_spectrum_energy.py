#!/usr/bin/env python3
"""H_c 乘法角色谱累计能量与最小列重构。"""
import argparse, math, cmath
from statistics import mean
from high_threshold_margin_fast import sieve, primes, H_count
from danger_column_character_spectrum import primitive_root_prime, dft


def analyze(P,c,ks):
    flags=sieve(P); root=primes(flags,P); y=int(c*P); small=[q for q in root if q<=y]
    counts=[0]*P
    for a in range(1,P): counts[a]=H_count(P,a,y,small)
    mu=mean(counts[1:]); mina=min(range(1,P), key=lambda a: counts[a]); dev=counts[mina]-mu
    g=primitive_root_prime(P); powers=[]; x=1
    for _ in range(P-1): powers.append(x); x=x*g%P
    n=P-1; t={a:i for i,a in enumerate(powers)}[mina]
    coeff=dft([counts[a]-mu for a in powers]); ranked=sorted(range(1,n), key=lambda m: abs(coeff[m]), reverse=True)
    total=sum(abs(coeff[m])**2 for m in range(1,n)); recon=0j; energy=0; idx=0
    print(f'P={P} minA={mina} min={counts[mina]} mean={mu:.3f} dev={dev:.3f}')
    for k in sorted(ks):
        while idx<k and idx<len(ranked):
            m=ranked[idx]
            recon += coeff[m]*cmath.exp(2j*math.pi*m*t/n)/n
            energy += abs(coeff[m])**2
            idx+=1
        print(f'  k={k} energy={energy/total:.3f} recon={recon.real:.3f} frac={recon.real/dev if dev else 0:.3f}')

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--Ps',default='251,503,1009'); ap.add_argument('--c',type=float,default=0.8); ap.add_argument('--ks',default='8,16,32,64,128,256,512'); args=ap.parse_args()
    ks=[int(x) for x in args.ks.split(',') if x.strip()]
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]: analyze(P,args.c,ks)
if __name__=='__main__': main()
