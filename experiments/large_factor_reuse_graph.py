#!/usr/bin/env python3
"""统计一行内大因子复用的间距与块跨度。"""
import argparse, math
from collections import defaultdict, Counter
from high_threshold_margin_fast import sieve, primes
from large_factor_exclusion import factor_distinct


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--P',type=int,default=2003); ap.add_argument('--rows',default=''); ap.add_argument('--top',type=int,default=4); args=ap.parse_args()
    P=args.P; B=math.isqrt(P); N=P*P+P; flags=sieve(N); plist=primes(flags,N)
    if args.rows: rows=[int(x) for x in args.rows.split(',') if x.strip()]
    else:
        rec=[]
        for r in range(1,P+1): rec.append((sum(1 for c in range(1,P+1) if flags[(r-1)*P+c]),r))
        rows=[r for _,r in sorted(rec)[:args.top]]
        print('lowRows', sorted(rec)[:args.top])
    print(f'P={P} B={B}')
    for r in rows:
        pos=defaultdict(list); rough_count=0
        for c in range(1,P+1):
            n=(r-1)*P+c
            if flags[n]: continue
            fac=factor_distinct(n,plist)
            if all(q>B for q in fac):
                rough_count+=1
                for q in fac:
                    if q>B: pos[q].append(c)
        reused={q:cs for q,cs in pos.items() if len(cs)>=2}
        gaps=[]; block_gaps=[]
        for q,cs in reused.items():
            cs=sorted(cs)
            for a,b in zip(cs,cs[1:]):
                gaps.append(b-a); block_gaps.append((b-1)//B-(a-1)//B)
        print('row',r,'rough',rough_count,'distinctLarge',len(pos),'reusedFactors',len(reused),'reuseEdges',len(gaps))
        if gaps:
            print(' gap min/avg/max',min(gaps),round(sum(gaps)/len(gaps),1),max(gaps),'blockGapCounts',Counter(block_gaps).most_common(6))
            top=sorted(((len(cs),q,cs[:6]) for q,cs in reused.items()), reverse=True)[:5]
            print(' topReuse',top)

if __name__=='__main__': main()
