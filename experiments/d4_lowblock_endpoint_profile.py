#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, math
from pathlib import Path
G=0.5772156649015328606

def build(n):
    tau=[0]*(n+1)
    for d in range(1,n+1):
        for m in range(d,n+1,d): tau[m]+=1
    A=[0]*(n+1); s=0
    for i in range(1,n+1): s+=tau[i]; A[i]=s
    return tau,A

def delta(A,y):
    return A[int(math.floor(y))]-y*(math.log(y)+2*G-1)

def block_value(x, lo, hi, tau, A, q):
    active_hi=min(hi, math.isqrt(x))
    c=old=0.0
    parts=[]
    for a in range(lo,active_hi+1):
        c_a=2*tau[a]*delta(A,x/a)/(x**0.75)
        old_a=2*tau[a]*delta(A,2*x/a)/((2*x)**0.75)
        f=old_a-q*c_a
        c+=c_a; old+=old_a
        parts.append((f,a,c_a,old_a,int(math.floor(x/a)),int(math.floor(2*x/a))))
    return old-q*c, c, old, parts

def near_jumps(x, lo, hi, radius):
    hits=[]
    for a in range(lo,hi+1):
        for factor,name in [(1,'X/a'),(2,'2X/a')]:
            # jumps when factor*x/a is integer; record distance to nearest jump grid a*m/factor
            m=round(factor*x/a)
            val=a*m/factor
            dist=abs(x-val)
            if dist<=radius:
                hits.append({'a':a,'source':name,'m':m,'jump_x':val,'dist':dist})
    return sorted(hits,key=lambda r:(r['dist'],r['a'],r['source']))

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--x',type=int,default=1028143)
    ap.add_argument('--lo',type=int,default=1)
    ap.add_argument('--hi',type=int,default=400)
    ap.add_argument('--q',type=float,default=0.958)
    ap.add_argument('--top',type=int,default=30)
    ap.add_argument('--jump-radius',type=float,default=1.0)
    ap.add_argument('--json',type=Path)
    args=ap.parse_args()
    tau,A=build(2*args.x+10)
    total,c,old,parts=block_value(args.x,args.lo,args.hi,tau,A,args.q)
    top_pos=sorted(parts,reverse=True)[:args.top]
    top_neg=sorted(parts)[:args.top]
    payload={
        'x':args.x,'lo':args.lo,'hi':args.hi,'q':args.q,
        'total_contract':total,'c_norm':c,'old_norm':old,
        'top_positive_terms':[{'a':a,'contract':f,'c_norm':ca,'old_norm':oa,'floor_x_over_a':k1,'floor_2x_over_a':k2,'frac_x_over_a':args.x/a-k1,'frac_2x_over_a':2*args.x/a-k2,'tau':tau[a]} for f,a,ca,oa,k1,k2 in top_pos],
        'top_negative_terms':[{'a':a,'contract':f,'c_norm':ca,'old_norm':oa,'floor_x_over_a':k1,'floor_2x_over_a':k2,'frac_x_over_a':args.x/a-k1,'frac_2x_over_a':2*args.x/a-k2,'tau':tau[a]} for f,a,ca,oa,k1,k2 in top_neg],
        'near_jumps':near_jumps(args.x,args.lo,args.hi,args.jump_radius),
    }
    print(json.dumps({k:v for k,v in payload.items() if k not in ['top_positive_terms','top_negative_terms','near_jumps']},indent=2))
    print('top positive')
    for r in payload['top_positive_terms'][:10]: print(r)
    print('near jumps', payload['near_jumps'][:20])
    if args.json:
        args.json.parent.mkdir(parents=True,exist_ok=True)
        args.json.write_text(json.dumps(payload,ensure_ascii=False,indent=2))
if __name__=='__main__': main()
