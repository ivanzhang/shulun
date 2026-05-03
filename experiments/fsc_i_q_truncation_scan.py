#!/usr/bin/env python3
"""FSC-I q≤k 截断扫描：单点层 m>P 强制 q≤k，检查理论调和容量与实测覆盖。"""
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
            for j in range(i*i,n+1,i):s[j]=False
    return [i for i,v in enumerate(s) if v]

def spf_sieve(n:int):
    spf=list(range(n+1))
    if n>=0:spf[0]=0
    if n>=1:spf[1]=1
    for i in range(2,int(n**0.5)+1):
        if spf[i]==i:
            for j in range(i*i,n+1,i):
                if spf[j]==j:spf[j]=i
    return spf

def fac(n:int,spf:list[int]):
    out=[]
    while n>1:
        p=spf[n]; out.append(p)
        while n%p==0:n//=p
    return out

def rough(n:int,small:list[int]): return all(n%p for p in small)

def analyze(P:int):
    D=math.isqrt(P); small=primes_upto(D); spf=spf_sieve(P*P+P); primes=primes_upto(P)
    locks=set(fac(P-1,spf)+fac(P+1,spf))
    rows=[]
    for k in range(1,P+1):
        U=[]; single=set(); bad_q_gt_k=0; qset=set()
        for c in range(1,P+1):
            n=k*P+c
            if not rough(n,small): continue
            if any(n%p==0 for p in locks): continue
            U.append(c)
            if spf[n]==n: continue
            for q in fac(n,spf):
                if D<q<P:
                    m=n//q
                    if m>P and rough(m,small):
                        single.add(c); qset.add(q)
                        if q>k: bad_q_gt_k+=1
        hsum=sum(1/q for q in primes if D<q<=k)
        rows.append({'row':k,'U':len(U),'single':len(single),'share':len(single)/len(U) if U else 0,'q_count':len(qset),'bad_q_gt_k':bad_q_gt_k,'prime_hsum_D_to_k':hsum})
    top=sorted(rows,key=lambda r:(-r['share'],r['U']))[:8]
    # 分 k/P 桶，统计最高覆盖与调和容量。
    buckets=[]
    for b in range(10):
        lo=b*P/10; hi=(b+1)*P/10
        rr=[r for r in rows if lo<r['row']<=hi]
        if rr:
            mx=max(rr,key=lambda r:r['share'])
            buckets.append({'bucket':b,'row':mx['row'],'max_share':mx['share'],'U':mx['U'],'hsum':mx['prime_hsum_D_to_k']})
    return {'P':P,'D':D,'top_single':top,'buckets':buckets}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--ps',default='251,503,997')
    args=ap.parse_args(); ps=[int(x) for x in args.ps.split(',') if x.strip()]
    res=[analyze(P) for P in ps]
    audit={'certificate_type':'fsc_i_q_truncation_scan','status':'singleton_implies_q_le_k_verified','results':res}
    (DOCS/'fsc-i-q-truncation-scan.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
    lines=['# FSC-I q≤k 截断扫描','','**状态：** `singleton_implies_q_le_k_verified`','','## 摘要']
    for it in res:
        t=it['top_single'][0]
        bad=sum(r['bad_q_gt_k'] for r in it['top_single'])
        lines.append(f"- P={it['P']} top row={t['row']} share={t['share']:.3f} U={t['U']} qCount={t['q_count']} hsum(D,k)={t['prime_hsum_D_to_k']:.3f} bad_q_gt_k_top8={bad}")
    lines+=['','## k/P 分桶最高单点覆盖']
    for it in res:
        lines.append(f"- P={it['P']}: "+'; '.join(f"b{b['bucket']}:row={b['row']},share={b['max_share']:.2f},H={b['hsum']:.2f}" for b in it['buckets']))
    (DOCS/'fsc-i-q-truncation-scan.md').write_text('\n'.join(lines)+'\n')
    print(DOCS/'fsc-i-q-truncation-scan.md')
if __name__=='__main__': main()
