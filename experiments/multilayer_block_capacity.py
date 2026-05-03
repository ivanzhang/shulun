#!/usr/bin/env python3
"""多层短块容量扫描：比较每层实际消洞数与局部容量上限。"""
import argparse, math
from high_threshold_margin_fast import sieve, primes


def survivors_in_block(P,row,start,end,qs):
    out=[]
    for c in range(start,end+1):
        n=(row-1)*P+c
        if all(n%q for q in qs): out.append(c)
    return set(out)


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--P',type=int,default=1009); ap.add_argument('--top',type=int,default=4); ap.add_argument('--levels',default='sqrt,0.2,0.4,0.6,0.8'); args=ap.parse_args()
    P=args.P; B=math.isqrt(P); flags=sieve(P*P+P); root=primes(sieve(P),P)
    lows=[]
    for r in range(1,P+1): lows.append((sum(1 for c in range(1,P+1) if flags[(r-1)*P+c]),r))
    rows=[r for _,r in sorted(lows)[:args.top]]
    z=[]
    for x in args.levels.split(','):
        if x=='sqrt': z.append(B)
        else: z.append(int(float(x)*P))
    z=sorted(set(v for v in z if 2<=v<P))
    print(f'P={P} B={B} levels={z} rows={sorted(lows)[:args.top]}')
    for r in rows:
        worst=[]
        for start in range(1,P+1,B):
            end=min(P,start+B-1)
            qs_prev=[q for q in root if q<=z[0]]
            prev=survivors_in_block(P,r,start,end,qs_prev)
            layer_records=[]
            for i in range(len(z)-1):
                qs_cur=[q for q in root if q<=z[i+1]]
                cur=survivors_in_block(P,r,start,end,qs_cur)
                killed=len(prev-cur)
                layer_primes=[q for q in root if z[i]<q<=z[i+1]]
                # 每个 q 在长度 B 块中最多 floor((B-1)/q)+1；q>B 时为1
                cap=sum(((B-1)//q)+1 for q in layer_primes)
                layer_records.append((z[i],z[i+1],len(prev),len(cur),killed,cap,killed/cap if cap else 0))
                prev=cur
            final=len(prev)
            maxratio=max((x[6] for x in layer_records), default=0)
            totalKilled=sum(x[4] for x in layer_records); totalCap=sum(x[5] for x in layer_records)
            worst.append((maxratio,totalKilled/(totalCap or 1),final,start,end,layer_records))
        worst=sorted(worst, reverse=True)[:5]
        print('row',r)
        for maxratio,totalratio,final,start,end,recs in worst:
            print(f' block {start}-{end} finalSurv={final} maxLayerRatio={maxratio:.3f} totalRatio={totalratio:.3f}')
            print('  layers z0-z1 prev cur killed cap ratio:', [(a,b,pr,cu,k,cap,round(rat,3)) for a,b,pr,cu,k,cap,rat in recs])

if __name__=='__main__': main()
