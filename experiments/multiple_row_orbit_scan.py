#!/usr/bin/env python3
"""倍数行轨道筛余扫描。

检验：若第 k 行危险，2k,3k,... 行的 H_c 是否也偏低。
这里第 k 行对应行参数 t=k-1，行内数为 tP+j, j=1..P。
"""
import argparse, math
from statistics import mean, pstdev
from high_threshold_margin_fast import sieve, primes


def H_row(P, k, y, small):
    # k is 1-based row index; n=(k-1)P+j, j=1..P
    t=k-1
    alive=bytearray(b'\x01')*P  # index 0 -> j=1
    for q in small:
        # j ≡ -tP mod q, j in 1..P. convert to index j-1.
        residue=(-t*P) % q
        first = residue if residue != 0 else q
        # j = first + m q <= P
        if first <= P:
            idx=first-1
            alive[idx:P:q]=b'\x00'*(((P-1-idx)//q)+1)
    return sum(alive)

def scan(P,c,top,show_orbit):
    flags=sieve(P); root=primes(flags,P); y=int(c*P); small=[q for q in root if q<=y]
    vals=[H_row(P,k,y,small) for k in range(1,P+1)]
    mu=mean(vals); sd=pstdev(vals)
    ranked=sorted((v,k) for k,v in enumerate(vals, start=1))[:top]
    tail=2*sum(1 for q in root if y<q<P)
    print(f'P={P} c={c} y={y} mean={mu:.3f} sd={sd:.3f} min={ranked[0]} tailBound={tail}')
    for v,k in ranked:
        orbit=[]
        for m in range(1, P//k + 1):
            kk=m*k
            hv=vals[kk-1]
            orbit.append((kk,hv,round((hv-mu)/sd,2) if sd else 0))
            if len(orbit)>=show_orbit: break
        print(f'  danger k={k} H={v} z={(v-mu)/sd if sd else 0:.2f} orbit={orbit}')

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--Ps',default='503,1009,2003'); ap.add_argument('--c',type=float,default=0.8); ap.add_argument('--top',type=int,default=8); ap.add_argument('--show-orbit',type=int,default=12); args=ap.parse_args()
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]: scan(P,args.c,args.top,args.show_orbit)
if __name__=='__main__': main()
