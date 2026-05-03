#!/usr/bin/env python3
"""P=23 的 P+36k 族零行命中分析。"""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; DOCS=ROOT/'docs'
P=23; qs=[2,3,5,7,11,13,17,19]

def holes_r(r:int):
    x=r-1; covered=set()
    for q in qs:
        res=(-x*P)%q
        for c in range(1,P):
            if c%q==res: covered.add(c)
    return [c for c in range(1,P) if c not in covered]

def main():
    rows=[]
    for k in range(1,101):
        r=P+36*k
        h=holes_r(r)
        rows.append({'k':k,'r':r,'holes':h,'hole_count':len(h),'is_zero':not h})
    zeros=[r for r in rows if r['is_zero']]
    best=sorted(rows,key=lambda x:x['hole_count'])[:20]
    audit={'certificate_type':'p23_offset36_family','status':'offset_36_first_hit_not_periodic_family','zero_count_in_first100':len(zeros),'zeros':zeros,'best':best,'structural_conclusion':'P=23 的 r=P+36 是零行，但 P+36k 不是零行周期族；前 100 个 k 中只有部分命中/近命中。36=2^2*3^2 提供了与小素数骨架对齐的首个机会，但完整零行还依赖 5,7,11,13,17,19 的剩余相位同时补洞。','next_obligations':['分解 r=P+36 首次命中中各素数的贡献。','证明小素数骨架只给候选相位，不给周期性零行。','将零行解集视为多个覆盖方案的并集，而非单一等差数列。']}
    (DOCS/'p23-offset36-family.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
    lines=['# P=23 的 P+36k 族分析','',f"**状态：** `{audit['status']}`",'',audit['structural_conclusion'],'',f"前100个 k 中零行数：`{len(zeros)}`",f"零行：`{zeros[:20]}`",'', '## 最佳近命中']
    for b in best:
        lines.append(f"- k={b['k']} r={b['r']} holes={b['hole_count']} {b['holes']}")
    lines += ['', '## 下一证明义务']+[f'- {x}' for x in audit['next_obligations']]+['']
    (DOCS/'p23-offset36-family.md').write_text('\n'.join(lines))
    print(DOCS/'p23-offset36-family.json'); print(DOCS/'p23-offset36-family.md')
if __name__=='__main__': main()
