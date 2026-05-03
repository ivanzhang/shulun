#!/usr/bin/env python3
"""CRT 行密度镜像与端点刚性扫描。"""
from __future__ import annotations
import json
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; DOCS=ROOT/'docs'

def primes_upto(n:int):
    s=[True]*(n+1)
    if n>=0:s[0]=False
    if n>=1:s[1]=False
    for i in range(2,int(n**0.5)+1):
        if s[i]: s[i*i:n+1:i]=[False]*(((n-i*i)//i)+1)
    return [i for i,v in enumerate(s) if v]

def counts(P):
    qs=primes_upto(P-1); M=1
    for q in qs:M*=q
    arr=[]
    for r in range(1,M+1):
        cnt=0
        for c in range(1,P):
            n=(r-1)*P+c
            if all(n%q for q in qs):cnt+=1
        arr.append(cnt)
    return M,arr

def scan(P):
    M,arr=counts(P)
    pair=Counter(arr[i]+arr[M-1-i] for i in range(M))
    diff=Counter(arr[i]-arr[M-1-i] for i in range(M))
    zero=[i+1 for i,v in enumerate(arr) if v==0]
    mirror_zero=[(z,M+1-z,arr[M-z]) for z in zero[:20]]
    return {'P':P,'M':M,'pair_sum_hist':dict(pair),'mirror_diff_hist':dict(diff),'zero_mirrors':mirror_zero,'front_counts':arr[:P],'end_counts':arr[-P:]}

def main():
    results=[scan(P) for P in [11,13,17]]
    audit={'certificate_type':'crt_density_symmetry_scan','status':'mirror_symmetry_is_exact_candidate_for_density_potential','results':results,'structural_conclusion':'镜像 r ↔ M+1-r 的行密度关系比粗平均更关键；若存在近似或精确互补律，可解释中点/末端密度刚性，并给零行位置提供势能约束。','next_obligations':['从同余变换 n -> -n mod q 推导镜像行密度关系。','分析第 P 列排除导致的镜像偏差项。','将镜像互补律用于证明前 P 窗口不能出现零行。']}
    (DOCS/'crt-density-symmetry-scan.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
    lines=['# CRT 行密度镜像刚性扫描','',f"**状态：** `{audit['status']}`",'',audit['structural_conclusion'],'','## 摘要']
    for r in results:
        lines.append(f"- P={r['P']} pair_sum_hist={r['pair_sum_hist']} diff_hist_sample={dict(list(r['mirror_diff_hist'].items())[:10])} zero_mirrors={r['zero_mirrors'][:5]} front={r['front_counts']} end={r['end_counts']}")
    lines += ['', '## 下一证明义务']+[f'- {x}' for x in audit['next_obligations']]+['']
    (DOCS/'crt-density-symmetry-scan.md').write_text('\n'.join(lines))
    print(DOCS/'crt-density-symmetry-scan.json'); print(DOCS/'crt-density-symmetry-scan.md')
if __name__=='__main__': main()
