#!/usr/bin/env python3
"""扫描不同 C 下长度 >= C sqrt(P) 的无素数坏段中 S2/A 最大比例。"""
import argparse, math
from high_threshold_margin_fast import sieve, primes
from large_factor_exclusion import factor_distinct
from bad_segment_factor_shell import find_bad_segments


def classify(P,row,start,end,flags,plist,small,B):
    cand=semi=rough=multi=0
    for c in range(start,end+1):
        n=(row-1)*P+c
        if all(n%q for q in small):
            cand+=1
            if not flags[n]:
                fac=factor_distinct(n,plist)
                if all(q>B for q in fac):
                    rough+=1
                    if len(fac)==2: semi+=1
                    else: multi+=1
    return cand,semi,rough,multi


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--Ps',default='503,1009,2003,4001'); ap.add_argument('--Cs',default='2.0,2.5,3.0,3.5,4.0,4.5,5.0'); args=ap.parse_args()
    Cs=[float(x) for x in args.Cs.split(',')]
    print('P C eligible maxSemiRatio maxRoughRatio maxLenRatio row start end cand semi rough multi')
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]:
        B=math.isqrt(P); flags=sieve(P*P+P); plist=primes(flags,P*P+P); small=primes(sieve(B),B)
        seg_records=[]
        for row in range(1,P+1):
            for L,start,end,cands in find_bad_segments(P,row,flags,small):
                cand,semi,rough,multi=classify(P,row,start,end,flags,plist,small,B)
                if cand:
                    seg_records.append((L/math.sqrt(P), semi/cand, rough/cand, L,row,start,end,cand,semi,rough,multi))
        for C in Cs:
            elig=[x for x in seg_records if x[0]>=C]
            if not elig:
                print(P,C,0,'NA','NA','NA','','','','','','','')
            else:
                # 先按半素数比例，再按长度排序
                rec=max(elig, key=lambda x:(x[1],x[0]))
                lr,sr,rr,L,row,start,end,cand,semi,rough,multi=rec
                print(P,C,len(elig),f'{sr:.3f}',f'{rr:.3f}',f'{lr:.3f}',row,start,end,cand,semi,rough,multi)

if __name__=='__main__': main()
