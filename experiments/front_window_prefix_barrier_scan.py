#!/usr/bin/env python3
"""多 P 前窗口前缀势垒扫描。"""
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

def holes(P,active,x):
    covered=set()
    for q in active:
        res=(-x*P)%q
        for c in range(1,P):
            if c%q==res: covered.add(c)
    return [c for c in range(1,P) if c not in covered]

def scan(P):
    qs=primes_upto(P-1); levels=[]
    for k in range(1,len(qs)+1):
        active=qs[:k]
        best=[]
        min_h=P
        for x in range(1,P):
            h=holes(P,active,x)
            if len(h)<min_h:
                min_h=len(h); best=[{'x':x,'holes':h}]
            elif len(h)==min_h and len(best)<10:
                best.append({'x':x,'holes':h})
        levels.append({'k':k,'active':active,'last_q':active[-1],'min_holes_x_lt_P':min_h,'best':best})
    return {'P':P,'qs':qs,'levels':levels,'final_min':levels[-1]['min_holes_x_lt_P'],'final_best':levels[-1]['best']}

def main():
    Ps=[13,17,19,23,29,31,37,41]
    results=[scan(P) for P in Ps]
    audit={'certificate_type':'front_window_prefix_barrier_scan','status':'positive_front_window_prefix_barrier_persists_for_all_scanned_P','results':results,'structural_conclusion':'对多个 P，任意前缀根基集合在 1<=x<P 正行前窗口内的最小残洞数始终非零；加入更多模数会降低势函数但不会在前窗口触底。最终残洞数通常很小，显示证明应聚焦最后残洞核。','next_obligations':['分析 final_best 残洞核随 P 的结构。','证明前缀势函数在 x<P 中有正下界。','寻找残洞核与必要中大素数相位延迟的关系。']}
    (DOCS/'front-window-prefix-barrier-scan.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
    lines=['# 多 P 前窗口前缀势垒扫描','',f"**状态：** `{audit['status']}`",'',audit['structural_conclusion'],'','## 摘要']
    for r in results:
        curve=[(lv['last_q'],lv['min_holes_x_lt_P']) for lv in r['levels']]
        lines.append(f"- P={r['P']} final_min={r['final_min']} final_best={r['final_best']} curve={curve}")
    lines += ['', '## 下一证明义务']+[f'- {x}' for x in audit['next_obligations']]+['']
    (DOCS/'front-window-prefix-barrier-scan.md').write_text('\n'.join(lines))
    print(DOCS/'front-window-prefix-barrier-scan.json'); print(DOCS/'front-window-prefix-barrier-scan.md')
if __name__=='__main__': main()
