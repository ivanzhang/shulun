#!/usr/bin/env python3
"""快速搜索 q=13 三点簇窗口的最小 cover。"""
import argparse, math, sys
from collections import defaultdict, Counter
sys.path.append('experiments')
from fixed_anchor_sieve_remainder import primes_upto, sieve
from local_cover_min_scan import exact_cover_size
Y=11; M=2310
small_primes=None

def holes_for_c(c,W):
    holes=[]; r=1
    while len(holes)<W:
        if math.gcd((r-c)%M,M)==1: holes.append(r)
        r+=1
    return holes

def triple_templates(W):
    out=[]
    for c in range(M):
        holes=holes_for_c(c,W); by=defaultdict(list)
        for r in holes: by[r%13].append(r)
        for res,rs in by.items():
            if len(rs)>=3: out.append((c,holes,res,tuple(rs)))
    return out

def factor_small(n,limit):
    qs=[]; x=n
    for p in small_primes:
        if p>limit or p*p>x: break
        if x%p==0:
            if p>Y: qs.append(p)
            while x%p==0: x//=p
    if x>1 and x<=limit and x>Y: qs.append(x)
    return tuple(qs)

def patch_sets(P,a,holes):
    sets=[]
    for r in holes:
        n=a+r*P; root=math.isqrt(n); qs=factor_small(n,root)
        if not qs: return None
        sets.append(qs)
    return sets

def main():
    global small_primes
    ap=argparse.ArgumentParser(); ap.add_argument('--maxP',type=int,default=200000); ap.add_argument('--max-a-per-class',type=int,default=500); ap.add_argument('--W',type=int,default=15); ap.add_argument('--show',type=int,default=20)
    args=ap.parse_args(); small_primes=primes_upto(math.isqrt(args.maxP*(100+args.maxP))+1000)
    primes=[p for p in primes_upto(args.maxP) if p>M]; by=defaultdict(list)
    for p in primes: by[p%M].append(p)
    templates=triple_templates(args.W); results=[]; tested=full=0; cover_hist=Counter()
    for c,holes,res,trs in templates:
        for Pmod,Ps in by.items():
            amod=(-c*Pmod)%M
            if math.gcd(amod,M)!=1: continue
            acands=by.get(amod,[])
            for P in Ps:
                acount=0
                for a in acands:
                    if a>=P: break
                    acount+=1
                    if acount>args.max_a_per_class: break
                    if any((a+r*P)%13 for r in trs): continue
                    tested+=1
                    sets=patch_sets(P,a,holes)
                    if sets is None: continue
                    full+=1; cover=exact_cover_size(sets); cover_hist[cover]+=1
                    inc=sum(len(s) for s in sets); dist=len({q for s in sets for q in s}); R=inc-dist
                    q_to=defaultdict(list)
                    for r,qs in zip(holes,sets):
                        for q in qs: q_to[q].append(r)
                    shared={q:rs for q,rs in q_to.items() if len(rs)>=2}
                    results.append((cover,R,P,a,c,res,trs,shared,[len(s) for s in sets],holes,sets))
    results.sort(key=lambda x:(x[0],-x[1]))
    print('templates',len(templates),'tested',tested,'full',full,'cover_hist',sorted(cover_hist.items()))
    for i,row in enumerate(results[:args.show],1): print(i,row)
if __name__=='__main__': main()
