#!/usr/bin/env python3
"""扫描坏段半素数证书中 u<=L、u<=2L 的占比。"""
import argparse, math
from high_threshold_margin_fast import sieve, primes
from large_factor_exclusion import factor_distinct
from bad_segment_factor_shell import find_bad_segments


def cert_stats(P,row,start,end,cands,flags,plist,small,B):
    L=end-start+1
    semi=leL=le2L=distinct_u=0; us=[]; triples=0
    for c in cands:
        n=(row-1)*P+c
        if flags[n]: continue
        fac=factor_distinct(n,plist)
        if all(q>B for q in fac):
            if len(fac)==2:
                semi+=1; u=min(fac); us.append(u)
                if u<=L: leL+=1
                if u<=2*L: le2L+=1
            elif len(fac)==3: triples+=1
    distinct_u=len(set(us))
    return semi,leL,le2L,distinct_u,triples


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--Ps',default='503,1009,2003,4001'); ap.add_argument('--Cs',default='2.0,2.5,3.0'); ap.add_argument('--top',type=int,default=8); args=ap.parse_args()
    Cs=[float(x) for x in args.Cs.split(',')]
    print('P C eligible maxLeLRatio avgLeLRatio maxLe2LRatio minDistinctURatio example')
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]:
        B=math.isqrt(P); flags=sieve(P*P+P); plist=primes(flags,P*P+P); small=primes(sieve(B),B)
        records=[]
        for row in range(1,P+1):
            for L,start,end,cands in find_bad_segments(P,row,flags,small):
                if not cands: continue
                semi,leL,le2L,du,tri=cert_stats(P,row,start,end,cands,flags,plist,small,B)
                if semi:
                    records.append((L/math.sqrt(P),leL/semi,le2L/semi,du/semi,row,start,end,L,len(cands),semi,leL,le2L,du,tri))
        for C in Cs:
            elig=[r for r in records if r[0]>=C]
            if not elig:
                print(P,C,0,'NA','NA','NA','NA','')
            else:
                maxLe=max(r[1] for r in elig); avgLe=sum(r[1] for r in elig)/len(elig); maxLe2=max(r[2] for r in elig); minDu=min(r[3] for r in elig)
                ex=max(elig, key=lambda r:r[1])
                print(P,C,len(elig),f'{maxLe:.3f}',f'{avgLe:.3f}',f'{maxLe2:.3f}',f'{minDu:.3f}',ex[4:])

if __name__=='__main__': main()
