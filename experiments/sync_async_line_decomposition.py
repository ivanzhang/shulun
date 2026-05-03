#!/usr/bin/env python3
"""同步/非同步斜线分解。

第 k 行行参数 t=k-1。q|t 的斜线与第一行同相位(j≡0 mod q)，称同步；q∤t 为非同步。
分析危险行的同步覆盖容量、非同步筛余等。
"""
import argparse, math
from statistics import mean, pstdev
from high_threshold_margin_fast import sieve, primes
from multiple_row_orbit_scan import H_row


def count_after_primes(P,k,plist):
    t=k-1
    alive=bytearray(b'\x01')*P
    for q in plist:
        residue=(-t*P)%q
        first=residue if residue!=0 else q
        if first<=P:
            idx=first-1
            alive[idx:P:q]=b'\x00'*(((P-1-idx)//q)+1)
    return sum(alive), alive

def analyze(P,c,top):
    flags=sieve(P); root=primes(flags,P); y=int(c*P); small=[q for q in root if q<=y]
    vals=[H_row(P,k,y,small) for k in range(1,P+1)]
    mu=mean(vals); sd=pstdev(vals)
    ranked=sorted((v,k) for k,v in enumerate(vals, start=1))[:top]
    print(f'P={P} c={c} y={y} mean={mu:.2f} sd={sd:.2f}')
    print('H k t omegaSync sum1qSync H_syncOnly H_asyncOnly H_all syncCovered asyncCovered')
    for H,k in ranked:
        t=k-1
        sync=[q for q in small if t%q==0] if t else small[:]  # first row all sync by phase 0
        asyncp=[q for q in small if q not in set(sync)]
        Hs,_=count_after_primes(P,k,sync)
        Ha,_=count_after_primes(P,k,asyncp)
        print(f'{H} {k} {t} {len(sync)} {sum(1/q for q in sync):.3f} {Hs} {Ha} {H} {P-Hs} {P-Ha}')

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--Ps',default='503,1009,2003'); ap.add_argument('--c',type=float,default=0.8); ap.add_argument('--top',type=int,default=8); args=ap.parse_args()
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]: analyze(P,args.c,args.top)
if __name__=='__main__': main()
