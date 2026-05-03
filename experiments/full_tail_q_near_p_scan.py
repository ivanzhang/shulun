#!/usr/bin/env python3
"""Full-DSIU 尾部 q≈P 扫描：不同 q 阈值下的长度、B、beta 贡献。"""
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

def rough(n,small): return all(n%p for p in small)

def build(P,rho):
    D=math.isqrt(P); R=int(P**rho); small=primes_upto(D); V=1.0
    for p in small: V*=1-1/p
    mu=mu_squarefree_products(small,R)
    lamb={d:mud*math.log(R/d)/math.log(R) for d,mud in mu.items()}
    ds=list(lamb); M=0.0
    for d in ds:
        for e in ds: M+=lamb[d]*lamb[e]/(d//gcd(d,e)*e)
    return D,R,small,V,lamb,M

def beta(m,lamb):
    s=0.0
    for d,ld in lamb.items():
        if m%d==0: s+=ld
    return s*s

def analyze(P,k,rho,thresholds):
    D,R,small,V,lamb,M=build(P,rho); primes=primes_upto(P-1)
    # full totals
    fullW=fullB=0; fullBeta=0.0
    recs=[]
    for tau in thresholds:
        Q0=int(tau*P); W=B=0; beta_sum=0.0; mvals=[]
        for q in primes:
            if not (D<q<P): continue
            a=k*P//q+1; b=(k*P+P)//q
            if a>b: continue
            for m in range(a,b+1):
                if tau==thresholds[0]:
                    fullW+=1; fullB+=1 if rough(m,small) else 0; fullBeta+=beta(m,lamb)
                if q>=Q0:
                    W+=1; mvals.append(m)
                    if rough(m,small): B+=1
                    beta_sum+=beta(m,lamb)
        recs.append({'tau':tau,'Q0':Q0,'W':W,'B':B,'beta':beta_sum,'W_share':None,'B_over_VW':B/(V*W) if W else 0,'beta_over_VW':beta_sum/(V*W) if W else 0,'m_min':min(mvals) if mvals else None,'m_max':max(mvals) if mvals else None,'m_count':len(set(mvals))})
    for r in recs:
        r['W_share']=r['W']/fullW if fullW else 0
        r['beta_share']=r['beta']/fullBeta if fullBeta else 0
    return {'P':P,'row':k,'rho':rho,'D':D,'R':R,'V':V,'M_over_V':M/V,'fullW':fullW,'fullB_over_VW':fullB/(V*fullW) if fullW else 0,'fullBeta_over_VW':fullBeta/(V*fullW) if fullW else 0,'records':recs}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--pairs',default='997:35,2003:34,5003:37,10007:88'); ap.add_argument('--rho',type=float,default=0.75); ap.add_argument('--taus',default='0.5,0.6,0.7,0.8,0.9')
    args=ap.parse_args(); thresholds=[float(x) for x in args.taus.split(',')]
    res=[]
    for pair in args.pairs.split(','):
        P,k=map(int,pair.split(':')); res.append(analyze(P,k,args.rho,thresholds))
    audit={'certificate_type':'full_tail_q_near_p_scan','status':'tail_q_near_p_profile','results':res}
    (DOCS/'full-tail-q-near-p-scan.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
    lines=['# Full-DSIU 尾部 q≈P 扫描','','**状态：** `tail_q_near_p_profile`',f"rho={args.rho}",'','## 摘要']
    for it in res:
        lines.append(f"- P={it['P']} row={it['row']} fullBeta/(VW)={it['fullBeta_over_VW']:.3f} fullB/(VW)={it['fullB_over_VW']:.3f} M/V={it['M_over_V']:.3f}")
        for r in it['records']:
            lines.append(f"  - q>={r['tau']:.1f}P: Wshare={r['W_share']:.3f} betaShare={r['beta_share']:.3f} beta/(VW)={r['beta_over_VW']:.3f} B/(VW)={r['B_over_VW']:.3f} m=[{r['m_min']},{r['m_max']}] distinctM={r['m_count']}")
    (DOCS/'full-tail-q-near-p-scan.md').write_text('\n'.join(lines)+'\n')
    print(DOCS/'full-tail-q-near-p-scan.md')
if __name__=='__main__': main()
