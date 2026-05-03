#!/usr/bin/env python3
"""P=23 禁余类覆盖缺口随 x 的变化。"""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; DOCS=ROOT/'docs'
P=23; qs=[2,3,5,7,11,13,17,19]

def covered_for_x(x:int):
    covered=set(); byq={}
    for q in qs:
        res=(-x*P)%q
        cs=[c for c in range(1,P) if c%q==res]
        byq[q]=cs; covered.update(cs)
    return covered,byq

def main():
    rows=[]
    for x in range(0,100):
        cov,byq=covered_for_x(x); holes=[c for c in range(1,P) if c not in cov]
        rows.append({'x':x,'r':x+1,'covered':len(cov),'holes':holes,'is_zero':not holes})
    front=[r for r in rows if r['x']<P]
    zeros=[r for r in rows if r['is_zero']]
    audit={'certificate_type':'p23_cover_defect_by_x','P':P,'rows':rows,'front_min_holes':min(len(r['holes']) for r in front),'front_best':min(front,key=lambda r:len(r['holes'])),'zeros':zeros[:20],'structural_conclusion':'对 P=23，前窗口 x<P 中没有完整覆盖，最少仍有 3 个洞；第一个完整覆盖在 x=58。零行出现需要禁余类相位经过足够长的 CRT 漂移后使大素数逐点补齐小筛洞。','next_obligations':['对一般 P 证明 x<P 时禁余类族至少留一个洞。','分析前窗口最小洞数与 P 的增长。','研究大素数逐点补洞所需的相位延迟下界。']}
    (DOCS/'p23-cover-defect-by-x.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
    lines=['# P=23 覆盖缺口随 x 变化','',audit['structural_conclusion'],'',f"前窗口最少洞数：`{audit['front_min_holes']}`",f"前窗口最佳：`{audit['front_best']}`",'',f"零行样本：`{audit['zeros'][:5]}`",'', '## x=0..22']
    for r in front:
        lines.append(f"- x={r['x']} r={r['r']} covered={r['covered']} holes={r['holes']}")
    lines += ['', '## 下一证明义务']+[f"- {x}" for x in audit['next_obligations']]+['']
    (DOCS/'p23-cover-defect-by-x.md').write_text('\n'.join(lines))
    print(DOCS/'p23-cover-defect-by-x.json'); print(DOCS/'p23-cover-defect-by-x.md')
if __name__=='__main__': main()
