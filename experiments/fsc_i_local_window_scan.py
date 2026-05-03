#!/usr/bin/env python3
"""FSC-I-local 局部窗口扫描：统计单点层在长度约 C√P 窗口内的覆盖缺口。"""
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

def row_sets(P,k,spf,small):
    D=math.isqrt(P); locks=set(fac(P-1,spf)+fac(P+1,spf))
    U=[]; singleton=set(); allcov=set()
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
                    allcov.add(c)
                    if m>P:
                        singleton.add(c)
    return set(U), singleton, allcov

def analyze(P:int, C:int):
    D=math.isqrt(P); W=max(1,C*D); small=primes_upto(D); spf=spf_sieve(P*P+P)
    best_single=None; best_all=None
    for k in range(1,P+1):
        U,S,A=row_sets(P,k,spf,small)
        for a in range(1,P+1,W//2 or 1):
            b=min(P,a+W-1)
            Uj={c for c in U if a<=c<=b}
            if not Uj: continue
            Sj=Uj & S; Aj=Uj & A
            rec={'row':k,'start':a,'end':b,'U':len(Uj),'single':len(Sj),'all':len(Aj),'single_share':len(Sj)/len(Uj),'all_share':len(Aj)/len(Uj)}
            if best_single is None or (rec['single_share'],rec['U'])>(best_single['single_share'],best_single['U']): best_single=rec
            if best_all is None or (rec['all_share'],rec['U'])>(best_all['all_share'],best_all['U']): best_all=rec
    return {'P':P,'D':D,'C':C,'W':W,'best_single':best_single,'best_all':best_all}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--ps',default='251,503,997'); ap.add_argument('--C',type=int,default=4); ap.add_argument('--min-u',type=int,default=20)
    args=ap.parse_args(); ps=[int(x) for x in args.ps.split(',') if x.strip()]
    res=[]
    for P in ps:
        item=analyze(P,args.C)
        # 另算只保留 U 足够大的窗口，避免稀疏小样本伪满覆盖。
        D=math.isqrt(P); W=max(1,args.C*D); small=primes_upto(D); spf=spf_sieve(P*P+P)
        best_single=None; best_all=None
        for k in range(1,P+1):
            U,S,A=row_sets(P,k,spf,small)
            for a in range(1,P+1,W//2 or 1):
                b=min(P,a+W-1)
                Uj={c for c in U if a<=c<=b}
                if len(Uj)<args.min_u: continue
                Sj=Uj&S; Aj=Uj&A
                rec={'row':k,'start':a,'end':b,'U':len(Uj),'single':len(Sj),'all':len(Aj),'single_share':len(Sj)/len(Uj),'all_share':len(Aj)/len(Uj)}
                if best_single is None or (rec['single_share'],rec['U'])>(best_single['single_share'],best_single['U']): best_single=rec
                if best_all is None or (rec['all_share'],rec['U'])>(best_all['all_share'],best_all['U']): best_all=rec
        item['dense_min_u']=args.min_u; item['dense_best_single']=best_single; item['dense_best_all']=best_all
        res.append(item)
    audit={'certificate_type':'fsc_i_local_window_scan','status':'local_singleton_gap_observed_in_samples','results':res}
    (DOCS/'fsc-i-local-window-scan.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
    lines=['# FSC-I-local 局部窗口扫描','',f"**状态：** `{audit['status']}`",'',f"窗口长度 `W=C√P`, C={args.C}；稠密窗口阈值 `U>= {args.min_u}`。",'','## 摘要']
    for it in res:
        s=it['best_single']; a=it['best_all']

        ds=it.get('dense_best_single'); da=it.get('dense_best_all')
        dense = 'dense: none' if ds is None else f"denseSingleton row={ds['row']} U={ds['U']} share={ds['single_share']:.3f}; denseAll row={da['row']} U={da['U']} share={da['all_share']:.3f}"
        lines.append(f"- P={it['P']} W={it['W']} bestSingleton row={s['row']} J=[{s['start']},{s['end']}] U={s['U']} share={s['single_share']:.3f}; bestAll row={a['row']} J=[{a['start']},{a['end']}] U={a['U']} share={a['all_share']:.3f}; {dense}")
    (DOCS/'fsc-i-local-window-scan.md').write_text('\n'.join(lines)+'\n')
    print(DOCS/'fsc-i-local-window-scan.md')
if __name__=='__main__': main()
