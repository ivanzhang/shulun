#!/usr/bin/env python3
"""前洞形状危险度统计。

对边界素数样本，按前 K 洞形状统计：
- 出现次数；
- 前 K 洞被补数量最大值；
- 是否曾全补；
- 失败洞位置分布。

用法示例：
    python3 experiments/shape_danger_score.py --P 461 --y 7 --Rmax 150 --K 5
"""
import argparse
from collections import defaultdict, Counter
from zero_repair_boundary_scan import boundary_events
from small_height_failure_rule import status

ap=argparse.ArgumentParser(); ap.add_argument('--P',type=int,default=461); ap.add_argument('--y',type=int,default=7); ap.add_argument('--Rmax',type=int,default=150); ap.add_argument('--K',type=int,default=5); ap.add_argument('--A',type=int,default=83)
args=ap.parse_args(); rows=[x for x in boundary_events(args.P,args.y,args.Rmax) if x['a']>args.A]
stats=defaultdict(lambda:{'count':0,'max_patched':0,'full':0,'fail_index':Counter(),'examples':[]})
for x in rows:
    holes=[]; patched=0; fail_idx=None; detail=[]; r=1
    while len(holes)<args.K and r<=300:
        st,qs=status(args.P,x['a'],args.y,r)
        if st!='blocked':
            holes.append(r); detail.append((r,st,qs))
            if st=='patched': patched+=1
            elif fail_idx is None: fail_idx=len(holes)
        r+=1
    shape=tuple(holes); s=stats[shape]; s['count']+=1; s['max_patched']=max(s['max_patched'],patched)
    if patched==args.K: s['full']+=1
    s['fail_index'][fail_idx]+=1
    if len(s['examples'])<5: s['examples'].append((x['a'],x['R'],patched,fail_idx,detail))
print(f"P={args.P},rows={len(rows)},shape_seen={len(stats)}")
rank=sorted(stats.items(), key=lambda kv:(-kv[1]['max_patched'],-kv[1]['count'],kv[0]))
for shape,s in rank[:50]:
    print('shape',shape,'count',s['count'],'max_patched',s['max_patched'],'full',s['full'],'fail_index',dict(s['fail_index']),'examples',s['examples'])
