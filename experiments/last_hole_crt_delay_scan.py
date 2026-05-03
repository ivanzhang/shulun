#!/usr/bin/env python3
"""前窗口最佳洞集的补洞 CRT 最小解扫描。"""
from __future__ import annotations
import itertools, json, math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; DOCS=ROOT/'docs'

def primes_upto(n:int):
    s=[True]*(n+1)
    if n>=0:s[0]=False
    if n>=1:s[1]=False
    for i in range(2,int(n**0.5)+1):
        if s[i]: s[i*i:n+1:i]=[False]*(((n-i*i)//i)+1)
    return [i for i,v in enumerate(s) if v]

def inv(a,m):
    return pow(a,-1,m)

def crt_pair(a,m,b,n):
    # coprime
    t=((b-a)%n)*inv(m%n,n)%n
    x=a+m*t
    return x%(m*n),m*n

def crt_system(congruences):
    x=0; mod=1
    for a,m in congruences:
        x,mod=crt_pair(x,mod,a%m,m)
    return x,mod

def holes(P,qs,x):
    covered=set()
    for q in qs:
        res=(-x*P)%q
        for c in range(1,P):
            if c%q==res: covered.add(c)
    return [c for c in range(1,P) if c not in covered]

def first_zero(P,qs,limit=500000):
    for x in range(limit):
        if not holes(P,qs,x): return x+1
    return None

def scan(P):
    qs=primes_upto(P-1)
    front=[{'x':x,'holes':holes(P,qs,x)} for x in range(1,P)]
    best=min(front,key=lambda r:len(r['holes']))
    H=best['holes']
    # 对每个洞 c，所有可补 q 满足 x ≡ -c P^{-1} mod q；枚举组合，仅限洞数小。
    options=[]
    for c in H:
        opts=[]
        for q in qs:
            a=(-c*inv(P%q,q))%q
            opts.append({'c':c,'q':q,'a':a})
        options.append(opts)
    best_solutions=[]
    if len(H)<=4:
        for combo in itertools.product(*options):
            # 同一个 q 给多个洞不可能要求不同余；若冲突跳过
            byq={}
            ok=True
            for item in combo:
                q=item['q']; a=item['a']
                if q in byq and byq[q]!=a: ok=False; break
                byq[q]=a
            if not ok: continue
            congr=[(a,q) for q,a in byq.items()]
            x0,mod=crt_system(congr)
            best_solutions.append({'x':x0,'mod':mod,'combo':[{'c':it['c'],'q':it['q'],'a':it['a']} for it in combo]})
        best_solutions.sort(key=lambda s:s['x'])
    fz=first_zero(P,qs)
    return {'P':P,'qs':qs,'front_best':best,'first_zero_r':fz,'first_zero_x':None if fz is None else fz-1,'best_completion_solutions':best_solutions[:20]}

def main():
    Ps=[13,17,19,23,29,31]
    results=[scan(P) for P in Ps]
    audit={'certificate_type':'last_hole_crt_delay_scan','status':'last_hole_completion_CRT_solutions_can_be_enumerated_for_small_hole_sets','results':results,'structural_conclusion':'对前窗口最佳近零行的最后洞，可以枚举补洞模数并求 CRT 最小解。该最小解若仍小于 P，说明仅补最佳洞还不足以保证全行零行；必须同时保持已覆盖列不丢失。因此真正对象是“补洞且保持全覆盖”的覆盖方案 CRT 解。','next_obligations':['加入保持已覆盖列的条件，枚举完整覆盖方案而非只补洞。','对 P=23 检查补洞组合 (17,19) 的 CRT 解与首零行 x=58 的关系。','构造覆盖方案的最小正解下界。']}
    (DOCS/'last-hole-crt-delay-scan.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
    lines=['# 最后洞补洞 CRT 延迟扫描','',f"**状态：** `{audit['status']}`",'',audit['structural_conclusion'],'','## 摘要']
    for r in results:
        sols=r['best_completion_solutions'][:5]
        lines.append(f"- P={r['P']} best={r['front_best']} first_zero_x={r['first_zero_x']} first_solutions={sols}")
    lines += ['', '## 下一证明义务']+[f'- {x}' for x in audit['next_obligations']]+['']
    (DOCS/'last-hole-crt-delay-scan.md').write_text('\n'.join(lines))
    print(DOCS/'last-hole-crt-delay-scan.json'); print(DOCS/'last-hole-crt-delay-scan.md')
if __name__=='__main__': main()
