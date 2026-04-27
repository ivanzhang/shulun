#!/usr/bin/env python3
"""H>=4 残基类的素数洞阻断快速测试。

只检验 lift 候选窗口是否存在素数洞；不做完整分解覆盖。
"""
import argparse, math, sys
from collections import defaultdict, Counter
sys.path.append('experiments')
from fixed_anchor_sieve_remainder import primes_upto, sieve
from consistent_anchor_H_scan import holes_for_c, candidate_hits
M=2310

def residue_classes(threshold,W,limit):
    units=[x for x in range(M) if math.gcd(x,M)==1]; rec=[]
    for Pmod in units:
        invP=pow(Pmod,-1,M)
        for amod in units:
            c=(-amod*invP)%M; holes=holes_for_c(c,11,W); hits,_=candidate_hits(Pmod,amod,holes,11,[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83])
            if len(hits)>=threshold: rec.append((len(hits),Pmod,amod,c,holes,hits))
    rec.sort(reverse=True,key=lambda x:x[0]); return rec[:limit]

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--maxP',type=int,default=100000); ap.add_argument('--threshold',type=int,default=4); ap.add_argument('--W',type=int,default=15); ap.add_argument('--limit-classes',type=int,default=20); ap.add_argument('--max-a-per-class',type=int,default=100)
    args=ap.parse_args(); maxN=args.maxP*(max(200,args.W*8+100))+args.maxP
    flags=sieve(maxN); primes=primes_upto(args.maxP); by=defaultdict(list)
    for p in primes:
        if p>M: by[p%M].append(p)
    classes=residue_classes(args.threshold,args.W,args.limit_classes)
    print('classes',len(classes),'maxP',args.maxP,'maxN',maxN)
    print('H Pmod amod c Ps tested full_composite first_prime_fail holes hits')
    for H,Pmod,amod,c,holes,hits in classes:
        tested=full=0; fail=Counter(); examples=[]
        for P in by.get(Pmod,[]):
            acount=0
            for a in by.get(amod,[]):
                if a>=P: break
                acount+=1
                if acount>args.max_a_per_class: break
                tested+=1
                first=None
                for idx,r in enumerate(holes,1):
                    if flags[a+r*P]: first=idx; break
                if first is None:
                    full+=1; examples.append((P,a))
                    if len(examples)>=3: break
                else: fail[first]+=1
            if len(examples)>=3: break
        print(H,Pmod,amod,c,len(by.get(Pmod,[])),tested,full,fail.most_common(5),examples,holes,hits)
if __name__=='__main__': main()
