#!/usr/bin/env python3
"""P=23 完整覆盖方案的 CRT 解枚举。"""
from __future__ import annotations
import itertools,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; DOCS=ROOT/'docs'
P=23; qs=[2,3,5,7,11,13,17,19]

def inv(a,m): return pow(a,-1,m)
def crt_pair(a,m,b,n):
    t=((b-a)%n)*inv(m%n,n)%n
    return (a+m*t)%(m*n),m*n
def crt_system(congs):
    x=0; mod=1
    for a,m in congs:
        x,mod=crt_pair(x,mod,a%m,m)
    return x,mod

def residues_for_c(c):
    return [{'q':q,'a':(-c*inv(P%q,q))%q} for q in qs]

def main():
    # 使用 P=23,r=59 的贪心最小覆盖方案：q=2,3,5,7,13,17,19 覆盖全部列。
    scheme={2:[2,4,6,8,10,12,14,16,18,20,22],3:[1,7,13,19],5:[11,21],7:[3,17],13:[5],17:[9],19:[15]}
    congs=[]; conflict=False
    for q,cs in scheme.items():
        vals=set((-c*inv(P%q,q))%q for c in cs)
        if len(vals)!=1: conflict=True
        congs.append((next(iter(vals)),q))
    x,mod=crt_system(congs)
    # 枚举较小方案：每列选一个可覆盖 q，但限制必须一致；搜索前若干最小 CRT 解
    options=[[(c,q,(-c*inv(P%q,q))%q) for q in qs] for c in range(1,P)]
    # 回溯按 q->a 一致性，剪枝；P=23 可能很大，限制找 x<200 的完整覆盖相位验证
    solutions=[]
    for cand_x in range(0,200):
        ok=True; cover=[]
        for c in range(1,P):
            found=[q for q in qs if cand_x%q==(-c*inv(P%q,q))%q]
            if not found: ok=False; break
            cover.append((c,found))
        if ok: solutions.append({'x':cand_x,'r':cand_x+1,'cover_choices':cover})
    audit={'certificate_type':'p23_full_cover_scheme_crt','scheme':scheme,'scheme_congruences':congs,'scheme_x':x,'scheme_mod':mod,'conflict':conflict,'solutions_x_lt_200':solutions,'structural_conclusion':'P=23 首零行 x=58 对应一个完整覆盖方案，其各 q 的列集合给出一致 CRT 条件。直接扫描 x<200 只发现 x=58 为完整覆盖，说明必须保持全部列覆盖时，补洞相位的最小解确实被推迟到 P 之后。','next_obligations':['对一般 P 枚举/抽象完整覆盖方案，而非最后洞局部补齐。','证明任意完整覆盖方案的 CRT 最小解 x>=P。','将小素数骨架方案与中大素数补洞方案分离估计。']}
    (DOCS/'p23-full-cover-scheme-crt.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
    lines=['# P=23 完整覆盖方案 CRT 解','',audit['structural_conclusion'],'',f"方案 CRT 解：x={x}, r={x+1}, mod={mod}",f"x<200 完整覆盖解：`{[(s['x'],s['r']) for s in solutions]}`",'', '## 方案同余']
    for a,q in congs: lines.append(f"- x ≡ {a} mod {q}")
    lines += ['', '## 下一证明义务']+[f'- {z}' for z in audit['next_obligations']]+['']
    (DOCS/'p23-full-cover-scheme-crt.md').write_text('\n'.join(lines))
    print(DOCS/'p23-full-cover-scheme-crt.json'); print(DOCS/'p23-full-cover-scheme-crt.md')
if __name__=='__main__': main()
