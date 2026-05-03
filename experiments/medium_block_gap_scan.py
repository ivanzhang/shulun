#!/usr/bin/env python3
"""C sqrt(P) 中块补洞缺口扫描。"""
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

def scan(P:int,C:int):
    ps=primes_upto(P-1); Y=math.isqrt(P); small=[q for q in ps if q<=Y]; large=[q for q in ps if q>Y]
    L=max(1,C*Y); rows=sorted(set([2,P//4,P//2,3*P//4,P])); blocks=[]
    for r in rows:
      for start in range(1,P+1,L):
        end=min(P,start+L-1); holes=patch=unpatched=0
        for c in range(start,end+1):
          n=(r-1)*P+c
          if any(n%q==0 for q in small): continue
          holes+=1
          if any(n%q==0 for q in large): patch+=1
          else: unpatched+=1
        if holes: blocks.append({'r':r,'start':start,'end':end,'holes':holes,'patch':patch,'unpatched':unpatched,'patch_ratio':patch/holes})
    return {'C':C,'L':L,'max_patch_ratio':max(b['patch_ratio'] for b in blocks),'min_unpatched':min(b['unpatched'] for b in blocks),'bad_full_blocks':sum(1 for b in blocks if b['unpatched']==0)}

def main():
    Ps=[809,1601,3203,6421,12809]
    results=[]
    for P in Ps:
      results.append({'P':P,'Y':math.isqrt(P),'C_blocks':[scan(P,C) for C in [1,2,3,4,5,8,10]]})
    audit={'certificate_type':'medium_block_gap_scan','status':'larger_blocks_reduce_full_patch_blocks_but_tail_blocks_need_care','results':results,'structural_conclusion':'增大到 C sqrt(P) 后满补块减少；但末端短块会干扰最小值。可证路线应使用滑动中块或整行累计缺口，而非固定分块逐块命题。','next_obligations':['改用滑动窗口而非固定尾块。','证明满补中块不能连续覆盖整行。','将连续满补块转化为 CRT 短周期或大因子乘积矛盾。']}
    (DOCS/'medium-block-gap-scan.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
    lines=['# C sqrt(P) 中块补洞缺口扫描','',f"**状态：** `{audit['status']}`",'',audit['structural_conclusion'],'','## 摘要']
    for item in results:
      parts=[f"C={b['C']} max_patch={b['max_patch_ratio']:.3f} full_blocks={b['bad_full_blocks']}" for b in item['C_blocks']]
      lines.append(f"- P={item['P']}："+'; '.join(parts))
    lines += ['', '## 下一证明义务'] + [f'- {x}' for x in audit['next_obligations']] + ['']
    (DOCS/'medium-block-gap-scan.md').write_text('\n'.join(lines))
    print(DOCS/'medium-block-gap-scan.json'); print(DOCS/'medium-block-gap-scan.md')
if __name__=='__main__': main()
