#!/usr/bin/env python3
"""局部窗口中 H_sqrt, S2粗半素数, T3, Z素数 的联合矩与缺口。"""
import argparse, math
from statistics import mean
from high_threshold_margin_fast import sieve, primes
from large_factor_exclusion import factor_distinct


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--Ps',default='503,1009,2003'); ap.add_argument('--Cs',default='3,4,5,6'); args=ap.parse_args()
    print('P C L windows meanH meanZ meanS2 meanT3 minGap gapMean gapVar corrHS2 zeroZ')
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]:
        B=math.isqrt(P); flags=sieve(P*P+P); plist=primes(flags,P*P+P); small=primes(sieve(B),B)
        # per position classification arrays per row computed on fly
        for C in [float(x) for x in args.Cs.split(',') if x.strip()]:
            L=max(1,int(C*math.sqrt(P))); step=max(1,L//8)
            Hs=[]; Zs=[]; S2s=[]; T3s=[]; Gaps=[]
            for row in range(1,P+1):
                prefH=[0]*(P+1); prefZ=[0]*(P+1); prefS2=[0]*(P+1); prefT3=[0]*(P+1)
                for c in range(1,P+1):
                    n=(row-1)*P+c
                    H=Z=S2=T3=0
                    if all(n%q for q in small):
                        H=1
                        if flags[n]: Z=1
                        else:
                            fac=factor_distinct(n,plist)
                            if all(q>B for q in fac):
                                if len(fac)==2: S2=1
                                elif len(fac)==3: T3=1
                    prefH[c]=prefH[c-1]+H; prefZ[c]=prefZ[c-1]+Z; prefS2[c]=prefS2[c-1]+S2; prefT3[c]=prefT3[c-1]+T3
                for start in range(1,P-L+2,step):
                    end=start+L-1
                    H=prefH[end]-prefH[start-1]; Z=prefZ[end]-prefZ[start-1]; S2=prefS2[end]-prefS2[start-1]; T3=prefT3[end]-prefT3[start-1]
                    Hs.append(H); Zs.append(Z); S2s.append(S2); T3s.append(T3); Gaps.append(H-S2-T3)
            mh=mean(Hs); ms=mean(S2s); mz=mean(Zs); mt=mean(T3s); mg=mean(Gaps); vg=mean((g-mg)**2 for g in Gaps)
            cov=mean((h-mh)*(s-ms) for h,s in zip(Hs,S2s)); vh=mean((h-mh)**2 for h in Hs); vs=mean((s-ms)**2 for s in S2s); corr=cov/(vh*vs)**0.5 if vh and vs else 0
            print(P,C,L,len(Hs),f'{mh:.3f}',f'{mz:.3f}',f'{ms:.3f}',f'{mt:.3f}',min(Gaps),f'{mg:.3f}',f'{vg:.3f}',f'{corr:.3f}',f'{sum(1 for z in Zs if z==0)/len(Zs):.5f}')

if __name__=='__main__': main()
