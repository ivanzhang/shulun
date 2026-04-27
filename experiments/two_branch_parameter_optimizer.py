#!/usr/bin/env python3
"""二分闭合参数优化。

对 W,S 扫描：
A分支：窗口并集 (Nwin*U_block)<1；
B分支：theta=(W-S)/W，无低cover块推出 S_global>=theta*N-pi(P)，
再检查 saving_logL F(P,S_global)>2logP。

用法示例：
    python3 experiments/two_branch_parameter_optimizer.py --P 10000000 --c 1213 --Wmin 80 --Wmax 300
"""
import argparse, math, sys
sys.path.append('experiments')
from block_union_parameter_scan import block_bound
from saving_logL_tradeoff import run_case
from fixed_anchor_sieve_remainder import primes_upto

RHO=480/2310

def pi_count(n): return len(primes_upto(n))

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--P',type=int,default=10_000_000); ap.add_argument('--c',type=int,default=1213); ap.add_argument('--Wmin',type=int,default=80); ap.add_argument('--Wmax',type=int,default=300); ap.add_argument('--step',type=int,default=10); ap.add_argument('--top',type=int,default=30)
    args=ap.parse_args()
    N=math.floor(RHO*args.P); piP=pi_count(args.P)-5; threshold=2*math.log10(args.P)
    rows=[]
    for W in range(args.Wmin,args.Wmax+1,args.step):
        # S from 40%W to 85%W
        for S in range(max(1,int(0.35*W)), min(W-1,int(0.9*W))+1):
            try:
                ub,total,weight,qopts,D=block_bound(args.c,W,S,args.P)
            except Exception:
                continue
            A_ok=total<1
            theta=(W-S)/W
            Sglob=math.floor(theta*max(1,N-W+1)-piP)
            if Sglob<=0:
                B_ok=False; F=0; margin=-threshold
            else:
                rec,_=run_case(args.P,Sglob)
                F=rec['log10L'] if rec else 0
                margin=F-threshold
                B_ok=margin>0
            if A_ok or B_ok:
                rows.append((A_ok and B_ok,A_ok,B_ok,W,S,theta,total,Sglob,F,margin,ub))
    rows.sort(key=lambda r:(not r[0], not r[1], not r[2], r[6], -r[9]))
    print('P',args.P,'c',args.c,'N',N,'pi_gt11',piP,'2logP',threshold,'found',len(rows))
    print('both A B W S theta windowsU Sglob F margin Ublock')
    for r in rows[:args.top]:
        print(r[0],r[1],r[2],r[3],r[4],f'{r[5]:.4f}',f'{r[6]:.6g}',r[7],f'{r[8]:.3f}',f'{r[9]:.3f}',f'{r[10]:.6g}',flush=True)
if __name__=='__main__': main()
