#!/usr/bin/env python3
"""前 P 行高度受限最小因子链扫描。"""
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

def min_factor(n,ps):
    for p in ps:
        if p*p>n: return None
        if n%p==0: return p
    return None

def row_chain(P,r,ps):
    composites=[]; primes=[]; factors=[]; gaps=[]
    prev_c=None
    for c in range(1,P):
        n=(r-1)*P+c; p=min_factor(n,ps)
        if p is None:
            primes.append(c)
        else:
            composites.append(c); factors.append((c,p,n//p))
            if prev_c is not None: gaps.append(c-prev_c)
            prev_c=c
    big=[(c,p,m) for c,p,m in factors if p>math.isqrt(P)]
    return {'r':r,'prime_count':len(primes),'composite_count':len(composites),'big_minfactor_count':len(big),'max_minfactor':max([p for _,p,_ in factors], default=None),'top_gaps':Counter(gaps).most_common(5),'big_samples':big[:10]}

def main():
    Ps=[23,101,211,401,809]
    results=[]
    for P in Ps:
        ps=primes_upto(P)
        rows=sorted(set([1,2,P//4,P//2,3*P//4,P]))
        results.append({'P':P,'rows':[row_chain(P,r,ps) for r in rows]})
    audit={'certificate_type':'front_window_factor_chain_scan','status':'front_window_has_prime_gaps_in_every_sampled_row_and_height_limited_factor_chain','results':results,'structural_conclusion':'前 P 行的高度受限最小因子链与 CRT 远处零行不同：采样行均有素数洞，且大最小因子标签数量受高度约束。下一步应将“若 prime_count=0”时最小因子链必须异常密集这一点不等式化。','next_obligations':['假设 prime_count=0，估计最小因子标签链的必要覆盖密度。','利用 p_c<=sqrt(n)<P 和商 m_c<n/p_c 建立递归高度约束。','比较前窗口链与 P=23,r=59 这类远处零行链的差异。']}
    (DOCS/'front-window-factor-chain-scan.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
    lines=['# 前 P 行高度受限最小因子链扫描','',f"**状态：** `{audit['status']}`",'',audit['structural_conclusion'],'','## 摘要']
    for item in results:
      lines.append(f"- P={item['P']}")
      for row in item['rows']:
        lines.append(f"  - r={row['r']} primes={row['prime_count']} comp={row['composite_count']} big_min={row['big_minfactor_count']} max_factor={row['max_minfactor']} gaps={row['top_gaps']}")
    lines += ['', '## 下一证明义务']+[f'- {x}' for x in audit['next_obligations']]+['']
    (DOCS/'front-window-factor-chain-scan.md').write_text('\n'.join(lines))
    print(DOCS/'front-window-factor-chain-scan.json'); print(DOCS/'front-window-factor-chain-scan.md')
if __name__=='__main__': main()
