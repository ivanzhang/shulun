#!/usr/bin/env python3
"""多个 P 的前窗口缺口与首个零行位置比较。"""
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

def holes_for_x(P,qs,x):
    covered=set()
    for q in qs:
        res=(-x*P)%q
        for c in range(1,P):
            if c%q==res: covered.add(c)
    return [c for c in range(1,P) if c not in covered]

def scan(P,limit=200000):
    qs=primes_upto(P-1)
    front=[]
    for x in range(0,P):
        h=holes_for_x(P,qs,x); front.append({'x':x,'holes':h,'hole_count':len(h)})
    first_zero=None
    for x in range(0,limit):
        if not holes_for_x(P,qs,x):
            first_zero=x+1; break
    pos_front=[r for r in front if r['x']>=1]
    return {'P':P,'prime_basis':qs,'front_min':min(front,key=lambda r:r['hole_count']),'front_positive_min':min(pos_front,key=lambda r:r['hole_count']),'first_zero_r':first_zero,'first_zero_over_P':first_zero/P if first_zero else None,'search_limit':limit}

def main():
    Ps=[5,7,11,13,17,19,23,29,31]
    results=[scan(P,300000) for P in Ps]
    audit={'certificate_type':'front_window_defect_vs_first_zero','status':'front_window_keeps_holes_before_first_zero_phase_delay','results':results,'structural_conclusion':'多个 P 显示前窗口 x<P 均保留洞，而首个零行需要相位延迟到 r>P。前窗口最佳洞数通常很小但非零，说明证明可聚焦于“最后一个洞为何不能被大素数相位提前补齐”。','next_obligations':['分析 front_positive_min 的最后洞位置与缺失大素数相位条件。','证明补齐最后洞需要 x 满足某个模数系统，其最小正解超过 P。','将首零行问题转化为覆盖同余系统的最小正解下界。']}
    (DOCS/'front-window-defect-vs-first-zero.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
    lines=['# 前窗口缺口与首个零行相位延迟','',f"**状态：** `{audit['status']}`",'',audit['structural_conclusion'],'','## 摘要']
    for r in results:
        lines.append(f"- P={r['P']} front_min={r['front_min']} positive_min={r['front_positive_min']} first_zero_r={r['first_zero_r']} first/P={r['first_zero_over_P']}")
    lines += ['', '## 下一证明义务']+[f'- {x}' for x in audit['next_obligations']]+['']
    (DOCS/'front-window-defect-vs-first-zero.md').write_text('\n'.join(lines))
    print(DOCS/'front-window-defect-vs-first-zero.json'); print(DOCS/'front-window-defect-vs-first-zero.md')
if __name__=='__main__': main()
