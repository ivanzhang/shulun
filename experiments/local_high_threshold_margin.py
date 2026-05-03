#!/usr/bin/env python3
"""局部窗口高阈值筛余 H_{cP}(J) 与尾部容量比较。"""
import argparse, math
from high_threshold_margin_fast import sieve, primes


def mark_positions(P,row,qs):
    arr=[0]*(P+1)
    N0=(row-1)*P
    for q in qs:
        r=(-N0)%q
        first=q if r==0 else r
        for c in range(first,P+1,q):
            arr[c]=1
    return arr


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--Ps',default='503,1009,2003'); ap.add_argument('--Cs',default='4,5,6,8,10'); ap.add_argument('--c',type=float,default=0.8); args=ap.parse_args()
    print('P C L windows minH meanH minTailCap meanTailCap minMargin minRowStart')
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]:
        root=primes(sieve(P),P); y=int(args.c*P); small=[q for q in root if q<=y]; tail=[q for q in root if y<q<P]
        for C in [float(x) for x in args.Cs.split(',') if x.strip()]:
            L=max(1,int(C*math.sqrt(P))); step=max(1,L//8)
            Hs=[]; caps=[]; minrec=None
            for row in range(1,P+1):
                smallhit=mark_positions(P,row,small)
                tailhit=mark_positions(P,row,tail)
                prefH=[0]*(P+1); prefT=[0]*(P+1)
                for i in range(1,P+1):
                    prefH[i]=prefH[i-1]+(1-smallhit[i])
                    prefT[i]=prefT[i-1]+tailhit[i]
                for start in range(1,P-L+2,step):
                    end=start+L-1
                    H=prefH[end]-prefH[start-1]
                    cap=prefT[end]-prefT[start-1]
                    margin=H-cap
                    Hs.append(H); caps.append(cap)
                    if minrec is None or margin<minrec[0]: minrec=(margin,row,start,H,cap)
            print(P,C,L,len(Hs),min(Hs),f'{sum(Hs)/len(Hs):.3f}',min(caps),f'{sum(caps)/len(caps):.3f}',minrec[0],(minrec[1],minrec[2],minrec[3],minrec[4]))

if __name__=='__main__': main()
