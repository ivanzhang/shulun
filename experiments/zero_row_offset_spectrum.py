#!/usr/bin/env python3
"""零行相对 P 的增量与间隔谱分析。"""
from __future__ import annotations
import json, math
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

def factor_small(n:int):
    out=[]; d=2
    while d*d<=n:
        while n%d==0:
            out.append(d); n//=d
        d+=1
    if n>1: out.append(n)
    return out

def zero_rows(P:int, limit:int|None=None):
    qs=primes_upto(P-1); M=1
    for q in qs:M*=q
    L=M if limit is None else min(M,limit)
    zeros=[]
    for r in range(1,L+1):
        if all(any(((r-1)*P+c)%q==0 for q in qs) for c in range(1,P)):
            zeros.append(r)
    return qs,M,zeros

def analyze(P:int, limit:int|None=None):
    qs,M,zs=zero_rows(P,limit)
    gaps=[zs[i+1]-zs[i] for i in range(len(zs)-1)]
    cyclic_gaps=gaps+([M+zs[0]-zs[-1]] if len(zs)>1 and (limit is None or limit>=M) else [])
    offsets=[z-P for z in zs]
    special=[]
    for k in [36,72,108,144,180,216,252,288,324]:
        r=P+k
        is_zero=r in zs if (limit is None or r<=limit) else None
        special.append({'offset':k,'r':r,'factors':factor_small(k),'is_zero':is_zero})
    return {
        'P':P,'basis_primes':qs,'M':M,'zero_count_seen':len(zs),'zeros_sample':zs[:50],
        'offsets_sample':offsets[:50],
        'offset_factor_samples':[{'offset':o,'factors':factor_small(o)} for o in offsets[:30] if o>0],
        'gap_hist':dict(Counter(gaps).most_common(20)),
        'cyclic_gap_hist':dict(Counter(cyclic_gaps).most_common(20)),
        'gcd_gaps': math.gcd(*gaps) if gaps else None,
        'special_offsets':special,
    }

def main():
    results=[analyze(23,None), analyze(29,300000), analyze(31,300000)]
    audit={'certificate_type':'zero_row_offset_spectrum','status':'zero_row_offsets_show_small_factor_bias_but_not_simple_multiples_rule','results':results,'structural_conclusion':'P=23 的首个零行 r=59=P+36，36=6^2 确有小因子重叠特征；但后续零行偏移并非简单的 36、72 等倍数规则。零行集合在 CRT 周期内有间隔谱，需分析为覆盖同余系统的解集，而不是单一小周期。','next_obligations':['对 P=23 检查 P+36k 的零行命中率。','分析零行间隔的 gcd 与小素数周期的关系。','建立零行解集是多覆盖同余条件交并组合，而非固定等差周期。']}
    (DOCS/'zero-row-offset-spectrum.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
    lines=['# 零行相对 P 的增量与间隔谱','',f"**状态：** `{audit['status']}`",'',audit['structural_conclusion'],'','## 摘要']
    for r in results:
        lines.append(f"- P={r['P']} M={r['M']} zero_count={r['zero_count_seen']} gcd_gaps={r['gcd_gaps']} zeros={r['zeros_sample'][:12]} offsets={r['offsets_sample'][:12]} gap_hist={r['gap_hist']} special={r['special_offsets'][:4]}")
    lines += ['', '## 下一证明义务']+[f'- {x}' for x in audit['next_obligations']]+['']
    (DOCS/'zero-row-offset-spectrum.md').write_text('\n'.join(lines))
    print(DOCS/'zero-row-offset-spectrum.json'); print(DOCS/'zero-row-offset-spectrum.md')
if __name__=='__main__': main()
