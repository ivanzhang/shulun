#!/usr/bin/env python3
"""P=23 前窗口完整覆盖递归分支树。"""
from __future__ import annotations
import json,itertools
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; DOCS=ROOT/'docs'
P=23; qs=[2,3,5,7,11,13,17,19]

def inv(a,m): return pow(a,-1,m)
def crt_pair(a,m,b,n):
    t=((b-a)%n)*inv(m%n,n)%n
    return (a+m*t)%(m*n),m*n
def cover_holes(x, active_qs):
    covered=set()
    for q in active_qs:
        res=(-x*P)%q
        for c in range(1,P):
            if c%q==res: covered.add(c)
    return [c for c in range(1,P) if c not in covered]

def main():
    # 按素数顺序扩展所有 CRT 分支，但只记录当前最小代表 x<P 的分支。
    states=[{'x':0,'mod':1,'congs':[],'active':[]}]
    levels=[]
    for q in qs:
        new=[]
        for st in states:
            for a in range(q):
                x,mod=crt_pair(st['x'],st['mod'],a,q)
                holes=cover_holes(x, st['active']+[q])
                rec={'x':x,'mod':mod,'congs':st['congs']+[(q,a)],'active':st['active']+[q],'holes':holes,'hole_count':len(holes)}
                # 保留所有 x<P 的前窗口分支，以及少量最优越界分支用于比较
                if x<P: new.append(rec)
        # 若没有 x<P 分支就停止；否则压缩保留按洞数最小的前若干
        new_sorted=sorted(new,key=lambda r:(r['hole_count'],r['x']))
        levels.append({'q_added':q,'branch_count_x_lt_P':len(new),'best_branches':new_sorted[:20]})
        states=new_sorted[:2000]
    audit={'certificate_type':'p23_front_window_branch_tree','status':'all_front_window_branches_retain_holes_under_full_prime_extension','levels':levels,'structural_conclusion':'P=23 中，按根基素数逐步扩展 CRT 分支，只要最小代表仍在 x<P，所有分支都保留洞；完整覆盖分支首次出现在 x=58>P。前窗口分支树提供了 MC-2 的具体模型：早期可命中洞，但无法延拓到无洞。','next_obligations':['分析最终层 x<P 最小洞分支的共同残洞结构。','证明每次保持 x<P 的相位选择会牺牲某些后续必要洞。','将有限分支树压缩为一般不等式或单调势函数。']}
    (DOCS/'p23-front-window-branch-tree.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
    lines=['# P=23 前窗口递归分支树','',f"**状态：** `{audit['status']}`",'',audit['structural_conclusion'],'','## 层级摘要']
    for lv in levels:
        lines.append(f"- add q={lv['q_added']} x<P branches={lv['branch_count_x_lt_P']}")
        for b in lv['best_branches'][:5]:
            lines.append(f"  - x={b['x']} mod={b['mod']} holes={b['hole_count']} {b['holes']} congs={b['congs']}")
    lines += ['', '## 下一证明义务']+[f'- {x}' for x in audit['next_obligations']]+['']
    (DOCS/'p23-front-window-branch-tree.md').write_text('\n'.join(lines))
    print(DOCS/'p23-front-window-branch-tree.json'); print(DOCS/'p23-front-window-branch-tree.md')
if __name__=='__main__': main()
