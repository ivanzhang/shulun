#!/usr/bin/env python3
"""检查危险列与低阶乘法字符的关系。

在原根坐标 a=g^t 下，阶 d 的角色频率为 m=(P-1)/d 的倍数。
输出低阶角色对子空间重构危险列偏差的贡献。
"""
import argparse
import cmath
import math
from danger_column_character_spectrum import primitive_root_prime, dft, column_prime_counts


def divisors(n):
    out=[]
    for d in range(2,n+1):
        if n%d==0: out.append(d)
    return out


def analyze(P, max_order):
    counts=column_prime_counts(P); mean=sum(counts[1:])/(P-1); min_a=min(range(1,P), key=lambda a: counts[a])
    g=primitive_root_prime(P); powers=[]; x=1
    for _ in range(P-1): powers.append(x); x=x*g%P
    n=P-1; seq=[counts[a]-mean for a in powers]; coeffs=dft(seq); t={a:i for i,a in enumerate(powers)}[min_a]
    true_dev=counts[min_a]-mean; total=sum(abs(c)**2 for c in coeffs[1:])
    print(f'P={P} min_a={min_a} true_dev={true_dev:.4f}')
    for d in divisors(n):
        if d>max_order: continue
        # exact order dividing d: frequencies multiple n/d, excluding 0
        ms=[k*(n//d) for k in range(1,d)]
        recon=sum(coeffs[m]*cmath.exp(2j*math.pi*m*t/n)/n for m in ms)
        energy=sum(abs(coeffs[m])**2 for m in ms)
        print(f'  order_dividing={d} modes={len(ms)} energy_frac={energy/total:.4f} recon={recon.real:.4f} recon_frac={recon.real/true_dev if true_dev else 0:.4f}')


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--Ps',default='251,503,1009'); ap.add_argument('--max-order',type=int,default=32); args=ap.parse_args()
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]: analyze(P,args.max_order)
if __name__=='__main__': main()
