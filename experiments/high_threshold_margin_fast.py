#!/usr/bin/env python3
"""快速扫描 min_a |H_c(P,a)| - 2(π(P)-π(cP))。
只用同余筛计算 H，不做因子分解。"""
import argparse, math


def sieve(n):
    flags=bytearray(b'\x01')*(n+1)
    if n>=0: flags[0]=0
    if n>=1: flags[1]=0
    for p in range(2, int(n**0.5)+1):
        if flags[p]: flags[p*p:n+1:p]=b'\x00'*(((n-p*p)//p)+1)
    return flags

def primes(flags,n): return [i for i in range(2,n+1) if flags[i]]

def H_count(P,a,y,small):
    alive=bytearray(b'\x01')*P
    for q in small:
        if q==P: continue
        residue=(-a*pow(P,-1,q))%q
        alive[residue:P:q]=b'\x00'*(((P-1-residue)//q)+1)
    return sum(alive)

def scan(P,c,root):
    y=int(c*P); small=[q for q in root if q<=y]; pi_tail=sum(1 for q in root if y<q<P); B=2*pi_tail
    minH=10**9; mina=None
    for a in range(1,P):
        H=H_count(P,a,y,small)
        if H<minH: minH=H; mina=a
    return y,pi_tail,B,minH,minH-B,mina,minH/B if B else float('inf')

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--Ps',default='2003,4001,8009'); ap.add_argument('--cs',default='0.75,0.78,0.8,0.82,0.85'); args=ap.parse_args()
    print('P c y piTail 2piTail minH margin ratio mina')
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]:
        flags=sieve(P); root=primes(flags,P)
        for c in [float(x) for x in args.cs.split(',') if x.strip()]:
            y,pt,B,H,m,a,ratio=scan(P,c,root)
            print(f'{P} {c:.3f} {y} {pt} {B} {H} {m} {ratio:.3f} {a}')
if __name__=='__main__': main()
