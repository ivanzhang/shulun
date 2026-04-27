#!/usr/bin/env python3
"""K=6 前洞形状共享能力分类。

对 y=7, M=210 的 182 个前 6 洞形状，按洞距中 >7 的素因子分类：
- no_share: 没有共享补丁可能；
- share11: 只可能共享 11；
- share13: 只可能共享 13；
- share11_13: 两者都可能。
并估计若六洞全合数，需要的最少不同补丁素因子数。
"""
import math
from collections import Counter, defaultdict
from front_hole_shapes_mod210 import front_holes, prime_factors

K=6; M=210
classes=defaultdict(list)
for c in range(M):
    shape=front_holes(c,K,M)
    share=set()
    pair_edges=[]
    for i,a in enumerate(shape):
        for j,b in enumerate(shape[i+1:],i+1):
            d=b-a
            for p in prime_factors(d):
                if p>7:
                    share.add(p); pair_edges.append((p,i,j,d))
    key=tuple(sorted(share))
    classes[key].append((shape,c,pair_edges))
print('class_count=',{k:len(v) for k,v in sorted(classes.items(), key=lambda kv:(kv[0],len(kv[1])) )})
# 估计最小不同因子数：共享边同素数 p 可把若干点连通；不同 p 不能同一个 q。
for key,items in sorted(classes.items(), key=lambda kv:(len(kv[0]),kv[0])):
    needs=[]
    for shape,c,edges in items:
        # 对每个可能共享素数，形成连通分量，最多可把一个分量用同一个 q=p 覆盖；但 q=p 必须实际整除对应数，这里只是容量下界。
        # 粗略最大节省：选择某个 p 的边覆盖形成分量节省 sum(size-1)。多个 p 可叠加但点不能重复节省，这里暴力枚举点分区很小，取图最大匹配式节省近似。
        # 安全下界：distinct >= K - max_single_p_saving
        max_save=0
        for p in key:
            parent=list(range(K))
            def find(x):
                while parent[x]!=x:
                    parent[x]=parent[parent[x]]; x=parent[x]
                return x
            def union(a,b):
                ra,rb=find(a),find(b)
                if ra!=rb: parent[rb]=ra
            for pp,i,j,d in edges:
                if pp==p: union(i,j)
            comp=Counter(find(i) for i in range(K))
            save=sum(v-1 for v in comp.values() if v>1)
            max_save=max(max_save,save)
        needs.append(K-max_save)
    print('class',key or ('none',),'count',len(items),'min_distinct_lower_bound_range',(min(needs),max(needs)),'examples',[it[0] for it in items[:8]])
