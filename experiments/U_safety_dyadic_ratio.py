#!/usr/bin/env python3
"""U 安全间隙 dyadic 层贡献扫描。

U: 小筛候选中的粗半素数 n=uv，min(u,v)>L=4sqrt(P)。
按较小因子 u 的 dyadic 层统计 U/H 贡献。

用法示例：
  python3 experiments/U_safety_dyadic_ratio.py --Ps 503,1009,2003 --C 4
"""
import argparse
import math
from collections import defaultdict
from statistics import mean

from high_threshold_margin_fast import sieve, primes
from large_factor_exclusion import factor_distinct


def layer_idx(u, L):
    idx = 0
    bound = L
    while u > 2 * bound:
        bound *= 2
        idx += 1
    return idx, bound, 2 * bound


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--Ps', default='503,1009,2003')
    ap.add_argument('--C', type=float, default=4.0)
    args = ap.parse_args()
    print('P C L meanH totalU alphaU layer idx lo hi meanU alphaU_layer fracOfU')
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]:
        B = math.isqrt(P); L = max(1, int(args.C * math.sqrt(P)))
        flags = sieve(P * P + P); plist = primes(flags, P * P + P); small = primes(sieve(B), B)
        step = max(1, L // 8)
        Hs=[]; totalUs=[]; layer_vals=defaultdict(list)
        for row in range(1, P + 1):
            prefH=[0]*(P+1); prefU=defaultdict(lambda: [0]*(P+1))
            # 先确保常见层存在，方便前缀补零。
            for idx in range(12): prefU[idx]
            max_idx=0
            for c in range(1, P + 1):
                n=(row-1)*P+c; H=0; hit_idx=None
                if all(n%q for q in small):
                    H=1
                    if not flags[n]:
                        fac=factor_distinct(n, plist)
                        if len(fac)==2 and all(q>B for q in fac):
                            u=min(fac)
                            if u>L:
                                hit_idx,_,_=layer_idx(u,L)
                                max_idx=max(max_idx,hit_idx)
                prefH[c]=prefH[c-1]+H
                for idx in range(max_idx+2):
                    prefU[idx][c]=prefU[idx][c-1]+(1 if hit_idx==idx else 0)
            for start in range(1, P-L+2, step):
                end=start+L-1
                H=prefH[end]-prefH[start-1]
                U=0
                for idx, arr in prefU.items():
                    val=arr[end]-arr[start-1]
                    U+=val
                    layer_vals[idx].append(val)
                Hs.append(H); totalUs.append(U)
        meanH=mean(Hs); meanU=mean(totalUs)
        for idx in sorted(layer_vals):
            vals=layer_vals[idx]
            if mean(vals)==0 and idx>8:
                continue
            lo=L*(2**idx); hi=2*lo
            print(P,args.C,L,f'{meanH:.3f}',f'{meanU:.3f}',f'{meanU/meanH:.3f}','layer',idx,lo,hi,f'{mean(vals):.3f}',f'{mean(vals)/meanH:.4f}',f'{mean(vals)/meanU if meanU else 0:.3f}')


if __name__=='__main__': main()
