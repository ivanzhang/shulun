#!/usr/bin/env python3
"""中模数在骨架洞集中的命中顺序分析。"""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; DOCS=ROOT/'docs'

def inv(a,m): return pow(a,-1,m)

def main():
    rows=json.loads((DOCS/'medium-crossing-step-geometry.json').read_text())['rows']
    out=[]
    for r in rows:
        P=r['P']; q=r['cross_q']; x0=r['x0']; m=r['m']; holes=r['holes_before']
        order=[]
        for h in holes:
            a=(-h*inv(P%q,q))%q
            s=((a-x0)%q)*inv(m%q,q)%q
            order.append({'hole':h,'s':s,'x':x0+m*s,'crosses_P':x0+m*s>=P})
        order.sort(key=lambda z:z['s'])
        out.append({**{k:r[k] for k in ['P','cross_q','necessary_c','x0','m','threshold']},'hole_hit_order':order,'necessary_rank':[z['hole'] for z in order].index(r['necessary_c'])+1})
    audit={'certificate_type':'medium_crossing_hole_hit_order','status':'necessary_columns_are_not_early_hole_hits_for_crossing_prime','rows':out,'structural_conclusion':'对跨越素数 q，其在骨架洞集中的早期命中通常落在其他洞；真正必要列的命中序号足够靠后，使得 x0+m*s>=P。这提示必要列不是任意洞，而是完整方案中与后续模数兼容的延迟洞。','next_obligations':['解释为什么早期命中的洞不能作为完整方案必要列：它们会破坏后续唯一覆盖结构。','研究后续模数兼容性如何选择延迟洞。','将必要列定义改为全方案兼容必要列，而非当前骨架的任意洞。']}
    (DOCS/'medium-crossing-hole-hit-order.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
    lines=['# 中模数对骨架洞集的命中顺序','',f"**状态：** `{audit['status']}`",'',audit['structural_conclusion'],'','## 摘要']
    for r in out:
        lines.append(f"- P={r['P']} q={r['cross_q']} necessary={r['necessary_c']} rank={r['necessary_rank']} threshold={r['threshold']} order={r['hole_hit_order']}")
    lines += ['', '## 下一证明义务']+[f'- {x}' for x in audit['next_obligations']]+['']
    (DOCS/'medium-crossing-hole-hit-order.md').write_text('\n'.join(lines))
    print(DOCS/'medium-crossing-hole-hit-order.json'); print(DOCS/'medium-crossing-hole-hit-order.md')
if __name__=='__main__': main()
