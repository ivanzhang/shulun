#!/usr/bin/env python3
"""验证同余约束图的秩计数：连通图带来 r-1 个自由度损失。"""
import argparse, itertools, math


def find(parent,x):
    while parent[x]!=x:
        parent[x]=parent[parent[x]]; x=parent[x]
    return x

def rank_for_edges(r, edges):
    # edges: (i,j,mod). 对不同 mod 先合并成模 lcm 的约束；这里只对素数模且独立时估计秩。
    # 返回图论连通秩 r-components，作为最低独立约束数。
    parent=list(range(r))
    for i,j,p in edges:
        ri,rj=find(parent,i),find(parent,j)
        if ri!=rj: parent[rj]=ri
    comps=len({find(parent,i) for i in range(r)})
    return r-comps

def count_solutions(r, L, edges):
    cnt=0
    for hs in itertools.product(range(L), repeat=r-1):
        arr=(0,)+hs
        ok=True
        for i,j,p in edges:
            if (arr[i]-arr[j])%p: ok=False; break
        if ok: cnt+=1
    return cnt

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--r',type=int,default=4); ap.add_argument('--L',type=int,default=60); args=ap.parse_args()
    examples=[
        [(0,1,5),(1,2,5),(2,3,5)],
        [(0,1,5),(2,3,5)],
        [(0,1,5),(1,2,7),(2,3,11)],
        [(0,1,5),(0,2,7),(0,3,11)],
        [(0,1,5),(1,2,5),(0,2,5),(2,3,7)],
    ]
    print('r L edges graphRank count naiveL^(r-1)/prodp ratio')
    for edges in examples:
        cnt=count_solutions(args.r,args.L,edges)
        prod=1
        for *_,p in edges: prod*=p
        naive=(args.L**(args.r-1))/prod
        print(args.r,args.L,edges,rank_for_edges(args.r,edges),cnt,f'{naive:.2f}',f'{cnt/naive if naive else 0:.3f}')
if __name__=='__main__': main()
