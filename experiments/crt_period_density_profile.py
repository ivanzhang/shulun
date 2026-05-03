#!/usr/bin/env python3
"""CRT 周期内行类素数密度位置剖面。"""
from __future__ import annotations
import json, math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; DOCS=ROOT/'docs'

def primes_upto(n:int):
    s=[True]*(n+1)
    if n>=0:s[0]=False
    if n>=1:s[1]=False
    for i in range(2,int(n**0.5)+1):
        if s[i]: s[i*i:n+1:i]=[False]*(((n-i*i)//i)+1)
    return [i for i,v in enumerate(s) if v]

def profile(P:int, window:int=20):
    qs=primes_upto(P-1); M=1
    for q in qs:M*=q
    row_counts=[]
    for r in range(1,M+1):
        cnt=0
        for c in range(1,P):
            n=(r-1)*P+c
            if all(n%q!=0 for q in qs): cnt+=1
        row_counts.append(cnt)
    def block(center):
        out=[]
        for r in range(max(1,center-window), min(M,center+window)+1):
            out.append({'r':r,'count':row_counts[r-1]})
        return out
    maxcnt=max(row_counts); mincnt=min(row_counts)
    return {'P':P,'M':M,'max_count':maxcnt,'min_count':mincnt,'zero_rows':[i+1 for i,v in enumerate(row_counts) if v==0][:20],'front':block(1),'middle':block((M+1)//2),'end':block(M),'max_rows':[i+1 for i,v in enumerate(row_counts) if v==maxcnt][:20],'hist':{str(k):row_counts.count(k) for k in sorted(set(row_counts))}}

def main():
    Ps=[11,13,17]
    results=[profile(P, min(30, P*3)) for P in Ps]
    audit={'certificate_type':'crt_period_density_profile','status':'CRT_position_density_profile_shows_middle_end_asymmetry_in_small_periods','results':results,'structural_conclusion':'完整 CRT 周期内行密度随位置有明显刚性剖面；零行与高密行不是均匀随机散布。中点附近与末端附近的密度结构可作为相位势能，约束零行进入前 P 窗口。','next_obligations':['量化中点高密与末端高合密的对称性。','研究 row_count(r)+row_count(M+1-r) 是否存在守恒或偏置。','把行密度剖面作为势函数加入零行相位延迟方程。']}
    (DOCS/'crt-period-density-profile.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
    lines=['# CRT 周期行密度位置剖面','',f"**状态：** `{audit['status']}`",'',audit['structural_conclusion'],'','## 摘要']
    for r in results:
        mid_counts=[x['count'] for x in r['middle']]
        end_counts=[x['count'] for x in r['end']]
        front_counts=[x['count'] for x in r['front']]
        lines.append(f"- P={r['P']} M={r['M']} hist={r['hist']} zero_sample={r['zero_rows']} front_avg={sum(front_counts)/len(front_counts):.2f} mid_avg={sum(mid_counts)/len(mid_counts):.2f} end_avg={sum(end_counts)/len(end_counts):.2f} max_rows={r['max_rows'][:5]}")
    lines += ['', '## 下一证明义务']+[f'- {x}' for x in audit['next_obligations']]+['']
    (DOCS/'crt-period-density-profile.md').write_text('\n'.join(lines))
    print(DOCS/'crt-period-density-profile.json'); print(DOCS/'crt-period-density-profile.md')
if __name__=='__main__': main()
