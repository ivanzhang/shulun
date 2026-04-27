#!/usr/bin/env python3
"""预计算版纯同余 H(a) 扫描。"""
import argparse, math
from collections import Counter, defaultdict
from fixed_anchor_sieve_remainder import primes_upto

def holes_for_c(c,y,W):
    M=math.prod(primes_upto(y)); holes=[]; r=1
    while len(holes)<W:
        if math.gcd((r-c)%M,M)==1: holes.append(r)
        r+=1
    return holes

def gt_y_prime_factors(n,y,prime_cache):
    out=[]; x=n
    for p in prime_cache:
        if p*p>x: break
        if x%p==0:
            if p>y: out.append(p)
            while x%p==0: x//=p
    if x>1 and x>y: out.append(x)
    return out

def edges_for_holes(holes,y,prime_cache):
    edges=[]
    for i,r in enumerate(holes):
        for j in range(i+1,len(holes)):
            d=holes[j]-r
            for q in gt_y_prime_factors(d,y,prime_cache):
                edges.append((i,j,q,r,d))
    return edges

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--y',type=int,default=11); ap.add_argument('--W',type=int,default=15); ap.add_argument('--show',type=int,default=8); ap.add_argument('--patterns',type=int,default=2310); ap.add_argument('--pmods',type=int,default=0); ap.add_argument('--nonzero-a', action='store_true', help='排除 a≡0 mod q 的命中，模拟 a 为大于 q 的根基素数')
    args=ap.parse_args(); M=math.prod(primes_upto(args.y)); prime_cache=primes_upto(200)
    pmods=[p for p in range(M) if math.gcd(p,M)==1]
    if args.pmods: pmods=pmods[:args.pmods]
    templates=[]
    for c in range(min(args.patterns,M)):
        holes=holes_for_c(c,args.y,args.W); edges=edges_for_holes(holes,args.y,prime_cache)
        templates.append((c,holes,edges))
    hist=Counter(); records=[]
    for pmod in pmods:
        residues_by_q={}
        for q in {e[2] for _,_,edges in templates for e in edges}:
            residues_by_q[q]=pmod%q
        for c,holes,edges in templates:
            groups=defaultdict(Counter); edge_by=(defaultdict(list))
            for e in edges:
                i,j,q,r,d=e; b=(-r*residues_by_q[q])%q
                
                if args.nonzero_a and b == 0:
                    continue
                groups[q][b]+=1; edge_by[(q,b)].append(e)
            best=sum(max(cnt.values()) for cnt in groups.values()) if groups else 0
            hist[best]+=1
            if len(records)<args.show or best>records[-1][0]:
                witness=[]
                for q,cnt in groups.items():
                    b=max(cnt, key=cnt.get)
                    witness += [(q,b,e) for e in edge_by[(q,b)]]
                records.append((best,pmod,c,holes,len(edges),witness)); records.sort(reverse=True,key=lambda x:x[0]); records=records[:args.show]
    print('y',args.y,'W',args.W,'pmods',len(pmods),'patterns',len(templates),'hist',sorted(hist.items()),'max',records[0][0])
    for best,pmod,c,holes,edge_count,wit in records:
        print('record',best,'pmod',pmod,'c',c,'edge_count',edge_count,'holes',holes)
        print(' witness',[(e[0]+1,e[1]+1,e[4],q,b) for q,b,e in wit])
if __name__=='__main__': main()
