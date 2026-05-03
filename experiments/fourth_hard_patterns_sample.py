#!/usr/bin/env python3
"""采样估计四阶展开中 (2,1,1) 与 distinct 模式贡献。"""
import argparse
import random
from statistics import mean
from sieve_remainder_pair_correlation import alive_matrix


def ordered_count(P, typ):
    if typ == '211':
        return P * (P-1) * (P-2) // 2 * 12
    if typ == '1111':
        return P * (P-1) * (P-2) * (P-3)
    raise ValueError(typ)


def sample_211(P):
    vals=random.sample(range(P),3)
    arr=[vals[0],vals[0],vals[1],vals[2]]
    random.shuffle(arr)
    return arr


def sample_1111(P):
    return random.sample(range(P),4)


def term_mean(Y, tup):
    n=len(Y); total=0.0
    for row in Y:
        prod=1.0
        for r in tup: prod*=row[r]
        total+=prod
    return total/n


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--P',type=int,default=503); ap.add_argument('--c',type=float,default=0.8); ap.add_argument('--samples',type=int,default=5000); ap.add_argument('--seed',type=int,default=1); args=ap.parse_args()
    random.seed(args.seed); P=args.P; A=alive_matrix(P,args.c); H=[sum(row) for row in A]; mu=mean(H); fourth=mean((h-mu)**4 for h in H)
    pr=[mean(row[r] for row in A) for r in range(P)]
    Y=[[row[r]-pr[r] for r in range(P)] for row in A]
    for typ, sampler in [('211', sample_211), ('1111', sample_1111)]:
        vals=[term_mean(Y, sampler(P)) for _ in range(args.samples)]
        mt=mean(vals); absmt=mean(abs(v) for v in vals); est=ordered_count(P,typ)*mt; absest=ordered_count(P,typ)*absmt
        print(f'P={P} typ={typ} samples={args.samples} meanTerm={mt:.8g} absMeanTerm={absmt:.8g} est={est:.3f} absEst={absest:.3f} est/fourth={est/fourth:.3f} absEst/mu2={absest/(mu*mu):.3f}')

if __name__=='__main__': main()
