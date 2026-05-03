#!/usr/bin/env python3
"""必要列同余子系统的 CRT 最小解分析。"""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; DOCS=ROOT/'docs'

def primes_upto(n:int):
    s=[True]*(n+1)
    if n>=0:s[0]=False
    if n>=1:s[1]=False
    for i in range(2,int(n**0.5)+1):
        if s[i]: s[i*i:n+1:i]=[False]*(((n-i*i)//i)+1)
    return [i for i,v in enumerate(s) if v]

def inv(a,m): return pow(a,-1,m)
def crt_pair(a,m,b,n):
    t=((b-a)%n)*inv(m%n,n)%n
    return (a+m*t)%(m*n),m*n
def crt_system(congs):
    x=0; mod=1
    for a,m in congs:
        x,mod=crt_pair(x,mod,a%m,m)
    return x,mod

def main():
    data=json.loads((DOCS/'full-scheme-essential-primes.json').read_text())['rows']
    out=[]
    for row in data:
        P=row['P']
        congs=[]
        for e in row['essential']:
            q=e['q']; c=e['unique_columns'][0]
            a=(-c*inv(P%q,q))%q
            congs.append((a,q,c))
        x,mod=crt_system([(a,q) for a,q,c in congs])
        out.append({'P':P,'full_x':row['x'],'essential_x':x,'essential_mod':mod,'essential_x_over_P':x/P,'matches_full_x_mod':(row['x']-x)%mod==0,'congruences':[{'q':q,'c':c,'a':a} for a,q,c in congs]})
    audit={'certificate_type':'essential_crt_min_solution','status':'essential_subsystem_often_already_delays_beyond_P_but_not_identical_to_full_scheme','rows':out,'structural_conclusion':'必要列同余子系统通常已经给出大于 P 的最小解，说明 FSC-2 很有希望。但必要列只取一个唯一列时，子系统未必等同完整方案；完整方案还包含小素数骨架约束。','next_obligations':['检查所有必要唯一列而非每个 q 只取一个。','若 essential_x>=P 普遍成立，尝试证明必要列子系统最小解下界。','若某些 essential_x<P，则加入小素数骨架约束补强。']}
    (DOCS/'essential-crt-min-solution.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
    lines=['# 必要列同余子系统 CRT 最小解','',f"**状态：** `{audit['status']}`",'',audit['structural_conclusion'],'','## 摘要']
    for r in out:
        lines.append(f"- P={r['P']} full_x={r['full_x']} essential_x={r['essential_x']} x/P={r['essential_x_over_P']:.2f} mod={r['essential_mod']} matches={r['matches_full_x_mod']} congs={r['congruences']}")
    lines += ['', '## 下一证明义务']+[f'- {x}' for x in audit['next_obligations']]+['']
    (DOCS/'essential-crt-min-solution.md').write_text('\n'.join(lines))
    print(DOCS/'essential-crt-min-solution.json'); print(DOCS/'essential-crt-min-solution.md')
if __name__=='__main__': main()
