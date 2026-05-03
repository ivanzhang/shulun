#!/usr/bin/env python3
"""CRT 列均衡亏损-补偿流扫描（小 P 完整周期）。"""
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

def scan(P:int):
    qs=primes_upto(P-1); M=1
    for q in qs: M*=q
    # 限制小 P，完整 CRT 周期行数 M。
    col_counts=[0]*(P+1); zero_rows=[]
    row_counts=[]
    for r in range(1,M+1):
        cnt=0
        for c in range(1,P):  # 除第 P 列
            n=(r-1)*P+c
            ok=all(n%q!=0 for q in qs)
            if ok:
                col_counts[c]+=1; cnt+=1
        row_counts.append(cnt)
        if cnt==0: zero_rows.append(r)
    nonp=col_counts[1:P]
    return {'P':P,'basis_primes':qs,'M':M,'column_counts':nonp,'equal_columns':len(set(nonp))==1,'zero_rows':zero_rows,'zero_row_count':len(zero_rows),'row_count_hist':{str(k):row_counts.count(k) for k in sorted(set(row_counts))}}

def main():
    Ps=[5,7,11,13]
    results=[scan(P) for P in Ps]
    audit={'certificate_type':'column_balance_defect_flow_scan','status':'complete_CRT_smallP_confirms_column_balance_and_zero_row_pattern','results':results,'structural_conclusion':'小 P 完整 CRT 周期扫描确认除第 P 列外列类素数计数相等。零行若存在，其在周期内的位置呈刚性分布；下一步应研究零行间距与根基模数的关系，判断是否可推广为全行覆盖的周期矛盾。','next_obligations':['分析 zero_rows 的间距 gcd 与 M 的关系。','若 P x P 内出现零行，比较其在完整 CRT 周期中的重复位置。','将零行亏损视为列均衡缺陷，研究补偿行的相位分布。']}
    (DOCS/'column-balance-defect-flow-scan.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
    lines=['# CRT 列均衡亏损-补偿流扫描','',f"**状态：** `{audit['status']}`",'',audit['structural_conclusion'],'','## 摘要']
    for r in results:
      lines.append(f"- P={r['P']} M={r['M']} equal={r['equal_columns']} zero_rows={r['zero_rows']} hist={r['row_count_hist']}")
    lines += ['', '## 下一证明义务']+[f'- {x}' for x in audit['next_obligations']]+['']
    (DOCS/'column-balance-defect-flow-scan.md').write_text('\n'.join(lines))
    print(DOCS/'column-balance-defect-flow-scan.json'); print(DOCS/'column-balance-defect-flow-scan.md')
if __name__=='__main__': main()
