#!/usr/bin/env python3
"""小筛洞大因子标签的相位回归压力扫描。"""
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

def factor_label(n:int, large:list[int]):
    for q in large:
        if n%q==0: return q
    return None

def scan_row(P:int,r:int,ps:list[int]):
    Y=math.isqrt(P); small=[q for q in ps if q<=Y]; large=[q for q in ps if q>Y]
    labels=[]
    for c in range(1,P+1):
        n=(r-1)*P+c
        if any(n%q==0 for q in small): continue
        q=factor_label(n,large)
        if q is not None:
            labels.append((c,q))
    if not labels:
        return {'r':r,'label_count':0}
    best={'t':None,'covered':-1,'coverage_ratio':0}
    for t in range(1,P):
        positions=set()
        for c,q in labels:
            # 推进 t 行后同一 q 斜线命中的列；只统计落入 1..P 的代表余数
            pos=((c - t*P - 1) % q) + 1
            if pos<=P: positions.add(pos)
        if len(positions)>best['covered']:
            best={'t':t,'covered':len(positions),'coverage_ratio':len(positions)/P}
    distinct=sorted(set(q for _,q in labels))
    prod_log=sum(math.log(q) for q in distinct)
    return {'r':r,'label_count':len(labels),'distinct_labels':len(distinct),'distinct_log_product':prod_log,'logP':math.log(P),'product_exceeds_P':prod_log>math.log(P),'best_recurrence':best}

def main():
    Ps=[211,401,809,1601,3203]
    results=[]
    for P in Ps:
        ps=primes_upto(P-1); rows=sorted(set([2,P//4,P//2,3*P//4,P]))
        scans=[scan_row(P,r,ps) for r in rows]
        results.append({'P':P,'rows':scans,'max_best_recurrence_ratio':max(s.get('best_recurrence',{}).get('coverage_ratio',0) for s in scans),'min_label_product_exceeds':min(s.get('product_exceeds_P',False) for s in scans if s.get('label_count',0)>0)})
    audit={'certificate_type':'phase_recurrence_pressure_scan','status':'label_modulus_product_exceeds_P_but_short_recurrence_not_full_in_samples','results':results,'structural_conclusion':'大因子标签集合的模数乘积很快超过 P，说明若短复现要求稳定这些标签会立刻 CRT 矛盾；但实验未显示自然短步长会全覆盖复现，关键仍是从全覆盖假设推出短回归。','next_obligations':['证明全覆盖迫使某个大标签子集在短步长下相位稳定。','或改用行列双向闭锁推出短回路。','将标签模数乘积超过 P 作为 CRT 矛盾的后半段。']}
    (DOCS/'phase-recurrence-pressure-scan.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
    lines=['# 相位回归压力扫描','',f"**状态：** `{audit['status']}`",'',audit['structural_conclusion'],'','## 摘要']
    for item in results:
      parts=[f"r={s['r']} labels={s.get('label_count',0)} distinct={s.get('distinct_labels',0)} prod>P={s.get('product_exceeds_P')} best={s.get('best_recurrence',{}).get('coverage_ratio',0):.3f}" for s in item['rows']]
      lines.append(f"- P={item['P']}："+'; '.join(parts))
    lines += ['', '## 下一证明义务']+[f'- {x}' for x in audit['next_obligations']]+['']
    (DOCS/'phase-recurrence-pressure-scan.md').write_text('\n'.join(lines))
    print(DOCS/'phase-recurrence-pressure-scan.json'); print(DOCS/'phase-recurrence-pressure-scan.md')
if __name__=='__main__': main()
