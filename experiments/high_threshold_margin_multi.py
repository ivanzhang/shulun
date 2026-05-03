#!/usr/bin/env python3
"""多阈值列筛余扫描：逐步加入小素数，避免每个 c 重复全筛。"""
import argparse
from high_threshold_margin_fast import sieve, primes


def scan(P, cs):
    flags=sieve(P); ps=primes(flags,P)
    targets=sorted((int(c*P), c) for c in cs)
    alive=[bytearray(b'\x01')*P for _ in range(P)]
    # a=0 不用于列命题，但保留便于同余计算；最后只扫 1..P-1。
    ti=0; results=[]
    for q in ps:
        if q==P: continue
        while ti<len(targets) and q>targets[ti][0]:
            y,c=targets[ti]
            pi_tail=sum(1 for p in ps if y<p<P); cap=2*pi_tail
            vals=[sum(alive[a]) for a in range(1,P)]
            minH=min(vals); mina=vals.index(minH)+1
            results.append((P,c,y,pi_tail,cap,minH,minH-cap,minH/cap if cap else float('inf'),mina))
            ti+=1
        # 加入 q 的禁余类：a+kP=0 mod q => k=-a P^-1 mod q
        inv=pow(P,-1,q)
        for a in range(1,P):
            residue=(-a*inv)%q
            alive[a][residue:P:q]=b'\x00'*(((P-1-residue)//q)+1)
    while ti<len(targets):
        y,c=targets[ti]
        pi_tail=sum(1 for p in ps if y<p<P); cap=2*pi_tail
        vals=[sum(alive[a]) for a in range(1,P)]
        minH=min(vals); mina=vals.index(minH)+1
        results.append((P,c,y,pi_tail,cap,minH,minH-cap,minH/cap if cap else float('inf'),mina))
        ti+=1
    return sorted(results, key=lambda x:x[1])


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--Ps',default='8009'); ap.add_argument('--cs',default='0.8,0.85,0.9'); args=ap.parse_args()
    cs=[float(x) for x in args.cs.split(',') if x.strip()]
    print('P c y piTail 2piTail minH margin ratio mina')
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]:
        for row in scan(P, cs):
            P,c,y,pt,cap,H,m,ratio,mina=row
            print(f'{P} {c:.3f} {y} {pt} {cap} {H} {m} {ratio:.3f} {mina}')
if __name__=='__main__': main()
