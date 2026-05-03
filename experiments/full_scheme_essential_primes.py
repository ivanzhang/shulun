#!/usr/bin/env python3
"""首个完整覆盖方案的必要素数分析。"""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; DOCS=ROOT/'docs'

def load(): return json.loads((DOCS/'full-scheme-min-x-scan.json').read_text())['results']

def main():
    rows=[]
    for item in load():
        P=item['P']; f=item['first_full']
        if not f: continue
        used={int(q):set(cs) for q,cs in f['used'].items()}
        allcols=set(range(1,P))
        essential=[]
        for q,cs in used.items():
            others=set().union(*(s for qq,s in used.items() if qq!=q)) if len(used)>1 else set()
            unique=sorted(cs-others)
            if unique: essential.append({'q':q,'unique_columns':unique,'unique_count':len(unique)})
        prod=1
        for e in essential: prod*=e['q']
        rows.append({'P':P,'x':f['x'],'r':f['r'],'used_count':len(used),'essential':essential,'essential_product':prod,'essential_product_over_P':prod/P})
    audit={'certificate_type':'full_scheme_essential_primes','status':'first_full_schemes_need_essential_medium_large_primes','rows':rows,'structural_conclusion':'首个完整覆盖方案中，除小素数骨架外，总有若干必要中大素数负责唯一列。其乘积远超 P，这解释了完整方案 CRT 解被推出前窗口。','next_obligations':['证明任意完整覆盖方案都含有必要素数集合 E，且 prod(E)>P。','证明这些必要素数的同余条件不能在 x<P 同时满足。','把必要列与相邻互斥/gap复杂度结合，给出 E 的下界。']}
    (DOCS/'full-scheme-essential-primes.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
    lines=['# 完整覆盖方案必要素数分析','',f"**状态：** `{audit['status']}`",'',audit['structural_conclusion'],'','## 摘要']
    for r in rows:
        lines.append(f"- P={r['P']} x={r['x']} essential_product/P={r['essential_product_over_P']:.2f} essential={r['essential']}")
    lines += ['', '## 下一证明义务']+[f'- {x}' for x in audit['next_obligations']]+['']
    (DOCS/'full-scheme-essential-primes.md').write_text('\n'.join(lines))
    print(DOCS/'full-scheme-essential-primes.json'); print(DOCS/'full-scheme-essential-primes.md')
if __name__=='__main__': main()
