#!/usr/bin/env python3
"""DSIU 残基均匀性扫描：检查 dyadic 乘子区间并 E_Q(k) 在小素数模下的分布。"""
from __future__ import annotations
import argparse, json, math
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
DOCS=ROOT/'docs'

def primes_upto(n:int):
    s=[True]*(n+1)
    if n>=0:s[0]=False
    if n>=1:s[1]=False
    for i in range(2,int(n**0.5)+1):
        if s[i]:
            for j in range(i*i,n+1,i): s[j]=False
    return [i for i,v in enumerate(s) if v]

def merge(intervals):
    if not intervals: return []
    intervals=sorted(intervals); out=[list(intervals[0])]
    for a,b in intervals[1:]:
        if a<=out[-1][1]+1: out[-1][1]=max(out[-1][1],b)
        else: out.append([a,b])
    return [(a,b) for a,b in out]

def interval_residue_counts(intervals,p):
    counts=[0]*p; total=0
    for a,b in intervals:
        if a>b: continue
        n=b-a+1; total+=n
        full=n//p; rem=n%p
        for r in range(p): counts[r]+=full
        start=a%p
        for i in range(rem): counts[(start+i)%p]+=1
    return total,counts

def block_intervals(P,k,Q,primes):
    bqs=[q for q in primes if Q<q<=min(2*Q,k)]
    intervals=[]
    for q in bqs:
        a=k*P//q+1; b=(k*P+P)//q
        if a<=b: intervals.append((a,b))
    return merge(intervals), len(bqs)

def analyze_pair(P,k):
    D=math.isqrt(P); primes=primes_upto(k); small=primes_upto(D)
    blocks=[]; Q=1
    while Q<=k:
        if 2*Q>D:
            intervals,qcnt=block_intervals(P,k,Q,primes)
            total=sum(b-a+1 for a,b in intervals)
            if total:
                worst=[]
                for p in small:
                    t,cnt=interval_residue_counts(intervals,p)
                    exp=t/p
                    max_abs=max(abs(x-exp) for x in cnt)
                    zero_def=cnt[0]-exp
                    # 筛粗数关心避开 0 residue；记录零类偏差与最大相对偏差。
                    worst.append({'p':p,'total':t,'max_abs':max_abs,'max_rel':max_abs/exp if exp else 0,'zero_rel':zero_def/exp if exp else 0})
                top=max(worst,key=lambda x:x['max_rel'])
                zero_top=max(worst,key=lambda x:abs(x['zero_rel']))
                blocks.append({'Q':Q,'hi':min(2*Q,k),'q_count':qcnt,'components':len(intervals),'length':total,'worst_mod':top,'worst_zero':zero_top})
        Q*=2
    return {'P':P,'row':k,'D':D,'blocks':blocks}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--pairs',default='997:916,2003:1877')
    args=ap.parse_args()
    res=[]
    for pair in args.pairs.split(','):
        P,k=map(int,pair.split(':')); res.append(analyze_pair(P,k))
    audit={'certificate_type':'dsiu_residue_discrepancy_scan','status':'small_mod_residue_discrepancy_profile','results':res}
    (DOCS/'dsiu-residue-discrepancy-scan.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
    lines=['# DSIU 残基均匀性扫描','','**状态：** `small_mod_residue_discrepancy_profile`','','## 摘要']
    for it in res:
        lines.append(f"- P={it['P']} row={it['row']} D={it['D']}")
        for b in it['blocks']:
            wm=b['worst_mod']; wz=b['worst_zero']
            lines.append(f"  - Q=({b['Q']},{b['hi']}]: len={b['length']} comp={b['components']} q={b['q_count']} worst p={wm['p']} maxRel={wm['max_rel']:.2f}; zeroWorst p={wz['p']} zeroRel={wz['zero_rel']:.2f}")
    (DOCS/'dsiu-residue-discrepancy-scan.md').write_text('\n'.join(lines)+'\n')
    print(DOCS/'dsiu-residue-discrepancy-scan.md')
if __name__=='__main__': main()
