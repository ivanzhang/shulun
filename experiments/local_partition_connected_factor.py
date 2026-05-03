#!/usr/bin/env python3
"""计算单个素数 p 上 r 点 connected cumulant 局部因子。"""
import argparse, itertools, math


def partitions(seq):
    if not seq:
        yield []
        return
    first=seq[0]
    for rest in partitions(seq[1:]):
        yield [[first]]+[b[:] for b in rest]
        for i in range(len(rest)):
            new=[b[:] for b in rest]
            new[i]=[first]+new[i]
            yield new

def coeff(k): return (-1)**(k-1)*math.factorial(k-1)

def local_EY(block, residues, p):
    # Y=I/(1-1/p)-1, local expectation over x mod p avoiding residues shifted by h.
    # For product over block, average over x of prod_i (1_{x != -h_i}/p0 - 1)
    p0=1-1/p
    total=0.0
    for x in range(p):
        prod=1.0
        for i in block:
            ind=1 if (x+residues[i])%p != 0 else 0
            prod *= ind/p0 - 1
        total += prod/p
    return total

def local_cumulant(residues,p):
    r=len(residues); idx=list(range(r)); total=0.0
    for part in partitions(idx):
        prod=1.0
        for block in part:
            prod*=local_EY(block,residues,p)
        total += coeff(len(part))*prod
    return total

def pattern(residues,p):
    # 返回分块形状，例如 111,21,3
    counts=[]
    seen={}
    for x in residues:
        seen[x]=seen.get(x,0)+1
    return ''.join(map(str,sorted(seen.values(),reverse=True)))

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--r',type=int,default=4); ap.add_argument('--p',type=int,default=5); args=ap.parse_args()
    stats={}
    for residues in itertools.product(range(args.p), repeat=args.r):
        # 平移归一：固定第一个为 0，避免重复也可；这里全枚举看均值。
        pat=pattern(residues,args.p); val=local_cumulant(residues,args.p)
        if pat not in stats: stats[pat]=[0,0.0,0.0,0.0]
        st=stats[pat]; st[0]+=1; st[1]+=val; st[2]+=abs(val); st[3]=max(st[3],abs(val))
    print('r p pattern count mean localSum meanAbs maxAbs')
    for pat,st in sorted(stats.items()):
        print(args.r,args.p,pat,st[0],f'{st[1]/st[0]:.8f}',f'{st[1]:.8f}',f'{st[2]/st[0]:.8f}',f'{st[3]:.8f}')
if __name__=='__main__': main()
