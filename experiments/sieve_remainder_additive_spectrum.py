#!/usr/bin/env python3
"""H_c(P,a) 在加法群 mod P 上的傅里叶谱分析。"""
import argparse, math, cmath
from statistics import mean, pstdev
from high_threshold_margin_fast import sieve, primes, H_count


def dft(vals):
    n=len(vals)
    out=[]
    for k in range(n):
        s=0j
        for j,v in enumerate(vals):
            ang=-2*math.pi*k*j/n
            s += v*complex(math.cos(ang), math.sin(ang))
        out.append(s)
    return out


def analyze(P,c,top):
    flags=sieve(P); root=primes(flags,P); y=int(c*P); small=[q for q in root if q<=y]
    vals=[0]+[H_count(P,a,y,small) for a in range(1,P)]
    # a=0 不属于列命题，但加法谱用完整模 P；同时输出非零 a 统计。
    nonzero=vals[1:]
    mu=mean(nonzero); sd=pstdev(nonzero); mn=min(nonzero); mx=max(nonzero)
    centered=[v-mean(vals) for v in vals]
    coeff=dft(centered)
    n=P
    energy=sum(abs(z)**2 for z in coeff[1:])/(n*n)
    ranked=sorted(range(1,n), key=lambda k: abs(coeff[k]), reverse=True)[:top]
    linf_bound=sum(abs(coeff[k]) for k in range(1,n))/n
    l2_bound=math.sqrt((n-1)*sum(abs(coeff[k])**2 for k in range(1,n)))/n
    print(f'P={P} c={c} meanNZ={mu:.3f} sdNZ={sd:.3f} min={mn} max={mx} energy={energy:.3f} linfL1={linf_bound:.2f} linfL2={l2_bound:.2f}')
    print(' top', [(k, round(abs(coeff[k])/n,3)) for k in ranked])


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--Ps',default='251,503,1009'); ap.add_argument('--c',type=float,default=0.8); ap.add_argument('--top',type=int,default=10); args=ap.parse_args()
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]: analyze(P,args.c,args.top)
if __name__=='__main__': main()
