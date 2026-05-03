#!/usr/bin/env python3
"""Full tail worst scan: across rows, tail beta share and total constant for q>=tau P."""
from __future__ import annotations
import argparse, json, math
from pathlib import Path
from math import gcd

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

def mu_squarefree_products(primes,limit):
    out={1:1}
    for p in primes:
        for x,mu in list(out.items()):
            y=x*p
            if y<=limit: out[y]=-mu
    return out

def build(P,rho):
    D=math.isqrt(P); R=int(P**rho); small=primes_upto(D); V=1.0
    for p in small: V*=1-1/p
    mu=mu_squarefree_products(small,R)
    lamb={d:mud*math.log(R/d)/math.log(R) for d,mud in mu.items()}
    return D,R,small,V,lamb

def beta(m,lamb):
    s=0.0
    for d,ld in lamb.items():
        if m%d==0: s+=ld
    return s*s

def analyze(P,rho,taus):
    D,R,small,V,lamb=build(P,rho); primes=primes_upto(P-1)
    rows=[]
    for k in range(1,P+1):
        fullW=0; fullBeta=0.0; tail={tau:[0,0.0] for tau in taus}
        for q in primes:
            if not (D<q<P): continue
            a=k*P//q+1; b=(k*P+P)//q
            if a>b: continue
            for m in range(a,b+1):
                val=beta(m,lamb); fullW+=1; fullBeta+=val
                for tau in taus:
                    if q>=tau*P:
                        tail[tau][0]+=1; tail[tau][1]+=val
        rec={'row':k,'fullW':fullW,'fullBeta':fullBeta,'fullConst':fullBeta/(V*fullW) if fullW else 0}
        for tau in taus:
            W,B=tail[tau]
            rec[f'tailW_{tau}']=W; rec[f'tailShare_{tau}']=W/fullW if fullW else 0; rec[f'tailBetaShare_{tau}']=B/fullBeta if fullBeta else 0; rec[f'tailConst_{tau}']=B/(V*W) if W else 0
        rows.append(rec)
    out={'P':P,'rho':rho,'D':D,'R':R,'V':V,'taus':taus}
    for tau in taus:
        out[f'top_tail_beta_share_{tau}']=max(rows,key=lambda r:r[f'tailBetaShare_{tau}'])
        out[f'top_tail_const_{tau}']=max(rows,key=lambda r:r[f'tailConst_{tau}'])
    out['top_full_const']=max(rows,key=lambda r:r['fullConst'])
    return out

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--ps',default='251,503,997'); ap.add_argument('--rho',type=float,default=0.75); ap.add_argument('--taus',default='0.5,0.6,0.7')
    args=ap.parse_args(); taus=[float(x) for x in args.taus.split(',')]
    res=[analyze(int(P),args.rho,taus) for P in args.ps.split(',')]
    audit={'certificate_type':'full_tail_worst_scan','status':'tail_worst_across_rows','results':res}
    (DOCS/'full-tail-worst-scan.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
    lines=['# Full tail worst scan','','**状态：** `tail_worst_across_rows`',f"rho={args.rho}",'','## 摘要']
    for it in res:
        fc=it['top_full_const']
        lines.append(f"- P={it['P']} topFull row={fc['row']} fullConst={fc['fullConst']:.3f}")
        for tau in taus:
            s=it[f'top_tail_beta_share_{tau}']; c=it[f'top_tail_const_{tau}']
            lines.append(f"  - tau={tau}: maxBetaShare row={s['row']} share={s[f'tailBetaShare_{tau}']:.3f} Wshare={s[f'tailShare_{tau}']:.3f}; maxTailConst row={c['row']} const={c[f'tailConst_{tau}']:.3f} W={c[f'tailW_{tau}']}")
    (DOCS/'full-tail-worst-scan.md').write_text('\n'.join(lines)+'\n')
    print(DOCS/'full-tail-worst-scan.md')
if __name__=='__main__': main()
