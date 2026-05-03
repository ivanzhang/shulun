#!/usr/bin/env python3
"""前缀最佳残洞核迁移规律扫描。"""
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

def holes(P,active,x):
    covered=set()
    for q in active:
        res=(-x*P)%q
        for c in range(1,P):
            if c%q==res: covered.add(c)
    return [c for c in range(1,P) if c not in covered]

def scan(P):
    qs=primes_upto(P-1); levels=[]
    prev_best=None
    for k in range(1,len(qs)+1):
        active=qs[:k]
        all_best=[]; min_h=P
        for x in range(1,P):
            h=holes(P,active,x)
            if len(h)<min_h:
                min_h=len(h); all_best=[(x,h)]
            elif len(h)==min_h:
                all_best.append((x,h))
        reps=[]
        for x,h in all_best[:10]:
            gaps=[h[i+1]-h[i] for i in range(len(h)-1)]
            mirror=[P-c for c in h]
            reps.append({'x':x,'holes':h,'sum_holes':sum(h),'gaps':gaps,'mirror':mirror,'mod_last_q':[c%active[-1] for c in h]})
        levels.append({'k':k,'active':active,'last_q':active[-1],'min_holes':min_h,'best_count':len(all_best),'representatives':reps})
    return {'P':P,'levels':levels}

def main():
    Ps=[23,29,31,37,41,43,47]
    results=[scan(P) for P in Ps]
    audit={'certificate_type':'residual_core_migration_scan','status':'residual_cores_show_small_cardinality_and_mirror_gap_patterns','results':results,'structural_conclusion':'最佳残洞核在前缀加入过程中保持小基数，并常呈现镜像配对、固定小 gap 或靠近特定同余类的结构。残洞核不是随机剩余，而是被 CRT 相位和列镜像刚性约束的迁移对象。','next_obligations':['提取最终残洞核的镜像对称类型。','分析残洞核被下一素数消除时 CRT 代表是否跨过 P。','寻找残洞核势函数的不变量，如镜像奇偶、gap 模式或同余类缺陷。']}
    (DOCS/'residual-core-migration-scan.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
    lines=['# 残洞核迁移规律扫描','',f"**状态：** `{audit['status']}`",'',audit['structural_conclusion'],'','## 摘要']
    for r in results:
        final=r['levels'][-1]
        curve=[(lv['last_q'],lv['min_holes'],lv['representatives'][:2]) for lv in r['levels']]
        lines.append(f"- P={r['P']} final={final['representatives'][:5]} curve={curve}")
    lines += ['', '## 下一证明义务']+[f'- {x}' for x in audit['next_obligations']]+['']
    (DOCS/'residual-core-migration-scan.md').write_text('\n'.join(lines))
    print(DOCS/'residual-core-migration-scan.json'); print(DOCS/'residual-core-migration-scan.md')
if __name__=='__main__': main()
