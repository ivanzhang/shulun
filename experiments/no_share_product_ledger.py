#!/usr/bin/env python3
"""无共享 A 类的乘积/因子账本。

对边界素数 a 的前 K=6 洞，筛选无共享形状，记录：
- 素数洞数量；
- 若全合数需要的最小因子乘积；
- 实际合数项最小因子乘积与 n_i 乘积；
- 最坏接近全合数样本。
"""
import argparse, math, sys
sys.path.append('experiments')
from fixed_anchor_sieve_remainder import primes_upto
from zero_repair_boundary_scan import boundary_events
from small_height_failure_rule import status
from front_hole_shapes_mod210 import prime_factors


def factor(n):
    out=[]; x=n
    for p in primes_upto(math.isqrt(n)+1):
        if p*p>x: break
        if x%p==0:
            e=0
            while x%p==0: x//=p; e+=1
            out.append((p,e))
    if x>1: out.append((x,1))
    return out

def isprimefac(f,n): return len(f)==1 and f[0][0]==n and f[0][1]==1

def share_primes(shape):
    s=set()
    for i,a in enumerate(shape):
        for b in shape[i+1:]:
            for p in prime_factors(b-a):
                if p>7: s.add(p)
    return s

ap=argparse.ArgumentParser(); ap.add_argument('--P',type=int,default=461); ap.add_argument('--y',type=int,default=7); ap.add_argument('--Rmax',type=int,default=500); ap.add_argument('--A',type=int,default=83); ap.add_argument('--K',type=int,default=6)
args=ap.parse_args(); rows=[x for x in boundary_events(args.P,args.y,args.Rmax) if args.A<x['a']<args.P]
records=[]
for x in rows:
    front=[]; r=1
    while len(front)<args.K and r<=600:
        st,qs=status(args.P,x['a'],args.y,r)
        if st!='blocked': front.append(r)
        r+=1
    if share_primes(tuple(front)): continue
    nums=[]; prime_rs=[]; comp=[]; logN=0; logMin=0
    for r in front:
        n=x['a']+r*args.P; f=factor(n); logN+=math.log(n)
        if isprimefac(f,n): prime_rs.append(r)
        else:
            comp.append((r,n,f,f[0][0])); logMin+=math.log(f[0][0])
        nums.append((r,n,f))
    records.append({'a':x['a'],'R':x['R'],'front':front,'prime_rs':prime_rs,'comp':comp,'logN':logN,'logMin':logMin})
records.sort(key=lambda z:(len(z['prime_rs']),-len(z['comp']),z['a']))
print('Aclass_records',len(records))
for rec in records[:30]:
    print(f"a={rec['a']},R={rec['R']},front={rec['front']},prime_rs={rec['prime_rs']},comp_minf={[c[3] for c in rec['comp']]},logN/logMin={rec['logN']:.1f}/{rec['logMin']:.1f}")
    print(' comp=',[(r,n,f) for r,n,f,m in rec['comp']])
