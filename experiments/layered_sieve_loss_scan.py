#!/usr/bin/env python3
"""分层筛损失扫描：先筛到 z，再看 z..cP 的额外删除。"""
import argparse, math
from high_threshold_margin_fast import sieve, primes, H_count


def H_for_primes(P,a,plist):
    alive=bytearray(b'\x01')*P
    for q in plist:
        residue=(-a*pow(P,-1,q))%q
        alive[residue:P:q]=b'\x00'*(((P-1-residue)//q)+1)
    return sum(alive), alive

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--Ps',default='1009,2003,4001'); ap.add_argument('--c',type=float,default=0.8); ap.add_argument('--thetas',default='0.5,0.6,0.7'); args=ap.parse_args()
    print('P theta z minH_z minH_c loss lossFrac HcConst HzConst')
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]:
        flags=sieve(P); root=primes(flags,P); scale=P/math.log(P); yc=int(args.c*P)
        for th in [float(x) for x in args.thetas.split(',') if x.strip()]:
            z=int(P**th); plist_z=[q for q in root if q<=z]; plist_c=[q for q in root if q<=yc]
            minHz=10**9; minHc=10**9; maxloss=-1; arg=None
            for a in range(1,P):
                Hz,_=H_for_primes(P,a,plist_z); Hc=H_count(P,a,yc,plist_c); loss=Hz-Hc
                if Hz<minHz: minHz=Hz
                if Hc<minHc: minHc=Hc
                if loss>maxloss: maxloss=loss; arg=a
            print(f'{P} {th:.2f} {z} {minHz} {minHc} {maxloss} {maxloss/minHz:.3f} {minHc/scale:.3f} {minHz/scale:.3f}')
if __name__=='__main__': main()
