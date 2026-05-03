#!/usr/bin/env python3
"""筛余指标 X_r(a) 的二点相关，按差分 d=r-s 分类。

X_r(a)=1_{a+rP 避开 q<=cP}，a 在 1..P-1 上平均。
对差分 d，统计 E_a X_r X_{r+d} 的平均与相对独立比。
"""
import argparse, math
from statistics import mean
from high_threshold_margin_fast import sieve, primes


def alive_matrix(P,c):
    flags=sieve(P); root=primes(flags,P); y=int(c*P); small=[q for q in root if q<=y]
    rows=[]
    for a in range(1,P):
        alive=bytearray(b'\x01')*P
        for q in small:
            residue=(-a*pow(P,-1,q))%q
            alive[residue:P:q]=b'\x00'*(((P-1-residue)//q)+1)
        rows.append(alive)
    return rows

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--P',type=int,default=1009); ap.add_argument('--c',type=float,default=0.8); ap.add_argument('--top',type=int,default=20); args=ap.parse_args()
    P=args.P; A=alive_matrix(P,args.c); nA=P-1
    H=[sum(row) for row in A]; p=mean(H)/P
    records=[]
    # 采样/全扫所有 d=1..P-1；每个 d 统计所有 r with r+d<P 和所有 a。
    for d in range(1,P):
        total=0; count=0
        for row in A:
            # 线性不环绕差分；也可考虑圆周差分，先用行内窗口。
            for r in range(0,P-d):
                total += row[r] & row[r+d]
            count += P-d
        e=total/count if count else 0
        ratio=e/(p*p) if p else 0
        records.append((ratio,e,d,total,count))
    records.sort(reverse=True)
    print(f'P={P} c={args.c} p={p:.6f} meanH={mean(H):.3f}')
    print('top positive corr ratio,e,d,total,count')
    for rec in records[:args.top]: print(tuple(round(x,6) if isinstance(x,float) else x for x in rec))
    print('bottom corr')
    for rec in sorted(records)[:args.top]: print(tuple(round(x,6) if isinstance(x,float) else x for x in rec))
if __name__=='__main__': main()
