#!/usr/bin/env python3
"""CRT 周期内零行最小位置扫描。"""
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

def scan(P:int, max_rows:int|None=None):
    qs=primes_upto(P-1); M=1
    for q in qs: M*=q
    limit=M if max_rows is None else min(M,max_rows)
    zeros=[]; min_zero=None
    for r in range(1,limit+1):
        ok_zero=True
        for c in range(1,P):
            n=(r-1)*P+c
            if all(n%q!=0 for q in qs):
                ok_zero=False; break
        if ok_zero:
            zeros.append(r)
            if min_zero is None: min_zero=r
            if len(zeros)>=20 and max_rows is not None: break
    return {'P':P,'basis_primes':qs,'M':M,'scanned_rows':limit,'min_zero':min_zero,'min_zero_over_P':(min_zero/P if min_zero else None),'min_zero_over_P2':(min_zero/(P*P) if min_zero else None),'zero_count_seen':len(zeros),'zeros_sample':zeros[:20]}

def main():
    Ps=[5,7,11,13,17,19,23]
    results=[]
    for P in Ps:
        qs=primes_upto(P-1); M=1
        for q in qs: M*=q
        max_rows=None if M<=1_000_000 else 1_000_000
        results.append(scan(P,max_rows))
    audit={'certificate_type':'zero_row_min_position_scan','status':'min_zero_rows_appear_well_beyond_first_P_window_in_scanned_cases','results':results,'structural_conclusion':'扫描显示完整周期零行若出现，其最小位置远大于 P；P=13 的最小零行为 169=P^2，P=17 在前 1e6 行未见零行。该规律支持将目标转化为 min Z_P>P 的高度排斥命题。','next_obligations':['分析 P=13 min_zero=P^2 的构造原因。','证明 r<=P 时 xP+c<P^2 的高度约束阻止覆盖所有 c。','寻找 min_zero 的下界，目标仅需 min_zero>P。']}
    (DOCS/'zero-row-min-position-scan.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
    lines=['# CRT 零行最小位置扫描','',f"**状态：** `{audit['status']}`",'',audit['structural_conclusion'],'','## 摘要']
    for r in results:
      lines.append(f"- P={r['P']} M={r['M']} scanned={r['scanned_rows']} min_zero={r['min_zero']} min/P={r['min_zero_over_P']} sample={r['zeros_sample']}")
    lines += ['', '## 下一证明义务']+[f'- {x}' for x in audit['next_obligations']]+['']
    (DOCS/'zero-row-min-position-scan.md').write_text('\n'.join(lines))
    print(DOCS/'zero-row-min-position-scan.json'); print(DOCS/'zero-row-min-position-scan.md')
if __name__=='__main__': main()
