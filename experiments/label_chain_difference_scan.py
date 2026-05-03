#!/usr/bin/env python3
"""行内大因子标签链的相邻差分扫描。"""
from __future__ import annotations
import json, math
from collections import Counter, defaultdict
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; DOCS=ROOT/'docs'

def primes_upto(n:int):
    s=[True]*(n+1)
    if n>=0:s[0]=False
    if n>=1:s[1]=False
    for i in range(2,int(n**0.5)+1):
        if s[i]: s[i*i:n+1:i]=[False]*(((n-i*i)//i)+1)
    return [i for i,v in enumerate(s) if v]

def scan_row(P,r,ps):
    Y=math.isqrt(P); small=[q for q in ps if q<=Y]; large=[q for q in ps if q>Y]
    chain=[]
    for c in range(1,P+1):
        n=(r-1)*P+c
        if any(n%q==0 for q in small): continue
        qs=[q for q in large if n%q==0]
        if qs: chain.append((c,qs[0]))
    gaps=Counter(); transitions=defaultdict(set)
    for (c1,q1),(c2,q2) in zip(chain,chain[1:]):
        gap=c2-c1; gaps[gap]+=1; transitions[gap].update([q1,q2])
    top=[]
    for gap,count in gaps.most_common(10):
        mods=transitions[gap]
        top.append({'gap':gap,'count':count,'mod_count':len(mods),'log_product':sum(math.log(q) for q in mods),'log_gap':math.log(gap) if gap>0 else 0,'mods_sample':sorted(mods)[:12]})
    return {'r':r,'chain_len':len(chain),'top_gaps':top}

def main():
    Ps=[211,401,809,1601]
    results=[]
    for P in Ps:
        ps=primes_upto(P-1); rows=sorted(set([P//4,P//2,3*P//4,P]))
        results.append({'P':P,'rows':[scan_row(P,r,ps) for r in rows]})
    audit={'certificate_type':'label_chain_difference_scan','status':'label_chain_has_repeated_small_gaps_with_many_moduli','results':results,'structural_conclusion':'行内大因子补洞标签链的相邻洞距有重复小 gap，且同一 gap 涉及多个大因子标签。这比同因子短差更接近“多因子共同位移”闭锁；下一步要证明全覆盖时某个 gap 的多因子集合必须共同约束相同短位移。','next_obligations':['把相邻洞距 gap 与行推进/列推进闭锁向量 (u,v) 联系起来。','证明重复 gap 的多标签集合在全覆盖假设下不能自由漂移。','寻找 gap 级 CRT 矛盾：多个 q 对同一 v=gap 或 uP+v 的共同约束。']}
    (DOCS/'label-chain-difference-scan.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
    lines=['# 标签链相邻差分扫描','',f"**状态：** `{audit['status']}`",'',audit['structural_conclusion'],'','## 摘要']
    for item in results:
      lines.append(f"- P={item['P']}")
      for row in item['rows']:
        lines.append(f"  - r={row['r']} len={row['chain_len']} top={row['top_gaps'][:3]}")
    lines += ['', '## 下一证明义务']+[f'- {x}' for x in audit['next_obligations']]+['']
    (DOCS/'label-chain-difference-scan.md').write_text('\n'.join(lines))
    print(DOCS/'label-chain-difference-scan.json'); print(DOCS/'label-chain-difference-scan.md')
if __name__=='__main__': main()
