#!/usr/bin/env python3
"""FSC 层谱剖面扫描：检查有效 m 倒数和、覆盖率、层大小之间的关系。"""
from __future__ import annotations
import argparse, json, math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / 'docs'


def primes_upto(n:int):
    sieve=[True]*(n+1)
    if n>=0: sieve[0]=False
    if n>=1: sieve[1]=False
    for i in range(2,int(n**0.5)+1):
        if sieve[i]:
            step=i; start=i*i
            sieve[start:n+1:step]=[False]*(((n-start)//step)+1)
    return [i for i,v in enumerate(sieve) if v]


def spf_sieve(n:int):
    spf=list(range(n+1))
    if n>=0: spf[0]=0
    if n>=1: spf[1]=1
    for i in range(2,int(n**0.5)+1):
        if spf[i]==i:
            for j in range(i*i,n+1,i):
                if spf[j]==j: spf[j]=i
    return spf


def fac(n:int, spf:list[int]):
    out=[]
    while n>1:
        p=spf[n]
        out.append(p)
        while n%p==0:
            n//=p
    return out


def rough(n:int, small:list[int]):
    return all(n%p for p in small)


def row_profile(P:int, k:int, spf:list[int], small:list[int]):
    D=math.isqrt(P)
    locks=set(fac(P-1,spf)+fac(P+1,spf))
    U=[]; col_to_ms={}; layers={}
    for c in range(1,P+1):
        n=k*P+c
        if not rough(n,small):
            continue
        if any(n%p==0 for p in locks):
            continue
        U.append(c)
        if spf[n]==n:
            continue
        for q in fac(n,spf):
            if D<q<P:
                m=n//q
                if rough(m,small):
                    col_to_ms.setdefault(c,set()).add(m)
                    layers.setdefault(m,set()).add(c)
    covered=set(col_to_ms)
    mvals=sorted(layers)
    sizes=[len(layers[m]) for m in mvals]
    inv=sum(1/m for m in mvals)
    single=sum(1 for s in sizes if s==1)
    return {
        'row':k,'U':len(U),'covered':len(covered),'holes':len(U)-len(covered),
        'share':len(covered)/len(U) if U else 0,'cap':sum(sizes),'cap_over_U':sum(sizes)/len(U) if U else 0,
        'm_count':len(mvals),'sum_inv_m':inv,'single_layer_share':single/len(mvals) if mvals else 0,
        'max_layer_size':max(sizes) if sizes else 0,
        'top_layers':sorted(([m,len(layers[m]),round(1/m,6)] for m in mvals), key=lambda x:(-x[1],x[0]))[:12],
        'm_min':min(mvals) if mvals else None,'m_max':max(mvals) if mvals else None,
    }


def analyze(P:int):
    D=math.isqrt(P); small=primes_upto(D); spf=spf_sieve(P*P+P)
    recs=[row_profile(P,k,spf,small) for k in range(1,P+1)]
    top_cover=sorted(recs,key=lambda r:(-r['share'],-r['cap_over_U']))[:5]
    top_inv=sorted(recs,key=lambda r:-r['sum_inv_m'])[:5]
    # 高覆盖与高倒数和的相关性，用于判断是否存在反相关刚性。
    n=len(recs)
    avg_s=sum(r['share'] for r in recs)/n
    avg_i=sum(r['sum_inv_m'] for r in recs)/n
    cov=sum((r['share']-avg_s)*(r['sum_inv_m']-avg_i) for r in recs)/n
    var_s=sum((r['share']-avg_s)**2 for r in recs)/n
    var_i=sum((r['sum_inv_m']-avg_i)**2 for r in recs)/n
    corr=cov/(var_s*var_i)**0.5 if var_s and var_i else 0
    return {'P':P,'D':D,'top_cover':top_cover,'top_inv':top_inv,'corr_share_inv':corr}


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--ps',default='83,107,167,197,251')
    args=ap.parse_args()
    ps=[int(x) for x in args.ps.split(',') if x.strip()]
    results=[analyze(P) for P in ps]
    audit={'certificate_type':'fsc_layer_profile_scan','status':'layer_activation_coverage_tension_observed','results':results}
    (DOCS/'fsc-layer-profile-scan.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
    lines=['# FSC 层谱剖面扫描','','**状态：** `layer_activation_coverage_tension_observed`','','## 摘要']
    for it in results:
        tc=it['top_cover'][0]; ti=it['top_inv'][0]
        lines.append(f"- P={it['P']} corr(coverage,sum1/m)={it['corr_share_inv']:.3f}; topCover row={tc['row']} share={tc['share']:.3f} U={tc['U']} sum1/m={tc['sum_inv_m']:.3f} cap/U={tc['cap_over_U']:.3f} singleLayer={tc['single_layer_share']:.2f}; topInv row={ti['row']} sum1/m={ti['sum_inv_m']:.3f} share={ti['share']:.3f} cap/U={ti['cap_over_U']:.3f}")
    lines += ['', '## 最高覆盖行细节']
    for it in results:
        r=it['top_cover'][0]
        lines.append(f"- P={it['P']} row={r['row']}: m_count={r['m_count']} m_range=[{r['m_min']},{r['m_max']}] max_layer={r['max_layer_size']} top_layers={r['top_layers']}")
    (DOCS/'fsc-layer-profile-scan.md').write_text('\n'.join(lines)+'\n')
    print(DOCS/'fsc-layer-profile-scan.md')

if __name__=='__main__':
    main()
