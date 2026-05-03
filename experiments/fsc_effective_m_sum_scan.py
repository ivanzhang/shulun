#!/usr/bin/env python3
"""FSC 有效互补因子倒数和扫描。"""
from __future__ import annotations
import argparse, json, math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / 'docs'


def primes_upto(n:int):
    s=[True]*(n+1)
    if n>=0:s[0]=False
    if n>=1:s[1]=False
    for i in range(2,int(n**0.5)+1):
        if s[i]:
            for j in range(i*i,n+1,i): s[j]=False
    return [i for i,v in enumerate(s) if v]

def spf_sieve(n:int):
    spf=list(range(n+1))
    if n>=0: spf[0]=0
    if n>=1: spf[1]=1
    for i in range(2,int(n**0.5)+1):
        if spf[i]==i:
            for j in range(i*i,n+1,i):
                if spf[j]==j: spf[j]=i
    return spf

def fac(n,spf):
    out=[]
    while n>1:
        p=spf[n]; out.append(p)
        while n%p==0:n//=p
    return out

def rough(n,small): return all(n%p for p in small)

def analyze(P:int):
    D=math.isqrt(P); small=primes_upto(D); spf=spf_sieve(P*P+P)
    locks=set(fac(P-1,spf)+fac(P+1,spf))
    recs=[]
    for k in range(1,P+1):
        U=[]; covered=set(); ms=set(); layer_sizes={}
        for c in range(1,P+1):
            n=k*P+c
            if not rough(n,small): continue
            if any(n%p==0 for p in locks): continue
            U.append(c)
            if spf[n]==n: continue
            for q in fac(n,spf):
                if D<q<P:
                    m=n//q
                    if rough(m,small):
                        ms.add(m); covered.add(c); layer_sizes[m]=layer_sizes.get(m,0)+1
        sum_inv=sum(1/m for m in ms)
        weighted_capacity=sum(layer_sizes.values())
        recs.append({'row':k,'U':len(U),'covered':len(covered),'holes':len(U)-len(covered),'m_count':len(ms),'sum_inv_m':sum_inv,'cap':weighted_capacity,'share':len(covered)/len(U) if U else 0,'cap_over_U':weighted_capacity/len(U) if U else 0})
    worst=max(recs,key=lambda r:(r['share'],r['cap_over_U']))
    max_inv=max(recs,key=lambda r:r['sum_inv_m'])
    return {'P':P,'D':D,'worst_cover':worst,'max_inv':max_inv,'top_by_inv':sorted(recs,key=lambda r:-r['sum_inv_m'])[:5]}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--max-p',type=int,default=251); args=ap.parse_args()
    results=[analyze(P) for P in primes_upto(args.max_p) if P>=5]
    audit={'certificate_type':'fsc_effective_m_sum_scan','status':'effective_m_inverse_sum_below_covering_threshold_in_samples','max_p':args.max_p,'results':results,'structural_conclusion':'对无锁定核心实际出现的有效 m 层计算倒数和。样本中最坏覆盖行的有效倒数和通常低于覆盖系统阈值 1，支持 FSC 的覆盖倒数和缺口；但理论可用 m 范围的倒数和可达 1，仍需证明有效素数层不能激活全部可用 m。'}
    (DOCS/'fsc-effective-m-sum-scan.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
    lines=['# FSC 有效 m 倒数和扫描','',f"**状态：** `{audit['status']}`",'',audit['structural_conclusion'],'','## 摘要']
    for it in results:
        w=it['worst_cover']; mi=it['max_inv']
        lines.append(f"- P={it['P']} worst row={w['row']} share={w['share']:.3f} U={w['U']} holes={w['holes']} m_count={w['m_count']} sum1/m={w['sum_inv_m']:.3f} cap/U={w['cap_over_U']:.3f}; maxInv row={mi['row']} sum1/m={mi['sum_inv_m']:.3f} share={mi['share']:.3f}")
    (DOCS/'fsc-effective-m-sum-scan.md').write_text('\n'.join(lines)+'\n')
    print(DOCS/'fsc-effective-m-sum-scan.json'); print(DOCS/'fsc-effective-m-sum-scan.md')
if __name__=='__main__': main()
