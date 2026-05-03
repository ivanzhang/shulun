#!/usr/bin/env python3
"""分析坏段中单命中证书 u>L 的分层贡献。"""
import argparse, math
from collections import Counter, defaultdict
from high_threshold_margin_fast import sieve, primes
from large_factor_exclusion import factor_distinct
from bad_segment_factor_shell import find_bad_segments


def layer_key(u,L):
    ratio=u/L
    k=0
    while ratio>2:
        ratio/=2; k+=1
    return k  # layer: (2^k L, 2^{k+1} L]


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--Ps',default='503,1009,2003,4001'); ap.add_argument('--Cmin',type=float,default=2.5); ap.add_argument('--top',type=int,default=6); args=ap.parse_args()
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]:
        B=math.isqrt(P); flags=sieve(P*P+P); plist=primes(flags,P*P+P); small=primes(sieve(B),B)
        rec=[]
        for row in range(1,P+1):
            for L,start,end,cands in find_bad_segments(P,row,flags,small):
                if L/math.sqrt(P)<args.Cmin: continue
                layers=Counter(); semis=0; single=0; us=[]
                for c in cands:
                    n=(row-1)*P+c
                    if flags[n]: continue
                    fac=factor_distinct(n,plist)
                    if all(q>B for q in fac) and len(fac)==2:
                        semis+=1; u=min(fac); us.append(u)
                        if u>L:
                            single+=1; layers[layer_key(u,L)] += 1
                if semis:
                    rec.append((single/semis,L/math.sqrt(P),P,row,start,end,L,len(cands),semis,single,layers,sorted(us)))
        print(f'P={P} B={B}')
        for _,ratio,P,row,start,end,L,A,semis,single,layers,us in sorted(rec, reverse=True)[:args.top]:
            layer_desc={f'({2**k}L,{2**(k+1)}L]':v for k,v in sorted(layers.items())}
            print(f' row={row} seg={start}-{end} L={L} ratio={ratio:.3f} A={A} semi={semis} single={single} single/semi={single/semis:.3f}')
            print('  layers',layer_desc)
            print('  u>L sorted', [u for u in us if u>L][:20])

if __name__=='__main__': main()
