#!/usr/bin/env python3
"""局部窗口中 sqrt(P)-候选素数计数 Z_J 的矩统计。"""
import argparse, math
from statistics import mean, pstdev
from high_threshold_margin_fast import sieve, primes


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--Ps',default='503,1009,2003,4001'); ap.add_argument('--Cs',default='2,3,4,5,6'); args=ap.parse_args()
    print('P C L windows meanZ varZ m4/var2 zeroRate minZ meanA minA')
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]:
        B=math.isqrt(P); flags=sieve(P*P+P); small=primes(sieve(B),B)
        # 预计算每行每列：A候选、候选且素数
        for C in [float(x) for x in args.Cs.split(',') if x.strip()]:
            L=max(1,int(C*math.sqrt(P)))
            Zs=[]; As=[]
            # 为节省时间，步长 max(1,L//8)，而不是所有窗口；仍覆盖大量局部窗口
            step=max(1,L//8)
            for row in range(1,P+1):
                A=[0]*(P+1); Z=[0]*(P+1)
                for c in range(1,P+1):
                    n=(row-1)*P+c
                    cand=all(n%q for q in small)
                    A[c]=A[c-1]+(1 if cand else 0)
                    Z[c]=Z[c-1]+(1 if cand and flags[n] else 0)
                for start in range(1,P-L+2,step):
                    end=start+L-1
                    As.append(A[end]-A[start-1]); Zs.append(Z[end]-Z[start-1])
            mz=mean(Zs); var=mean((z-mz)**2 for z in Zs); m4=mean((z-mz)**4 for z in Zs) if var else 0
            print(P,C,L,len(Zs),f'{mz:.3f}',f'{var:.3f}',f'{m4/(var*var) if var else 0:.3f}',f'{sum(1 for z in Zs if z==0)/len(Zs):.4f}',min(Zs),f'{mean(As):.3f}',min(As))

if __name__=='__main__': main()
