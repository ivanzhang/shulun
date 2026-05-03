#!/usr/bin/env python3
"""块级旧区收缩端点证书原型。

验证 C_J,old(2X) - q C_J(X) 在短区间上的最大值。
"""
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

def delta(A,y): return A[int(math.floor(y))]-y*(math.log(y)+2*G-1)

def block_values(x, lo, hi, tau, A):
    active_hi=min(hi, math.isqrt(x))
    if active_hi<lo: return 0.0,0.0
    c=2*sum(tau[a]*delta(A,x/a) for a in range(lo,active_hi+1))
    old=2*sum(tau[a]*delta(A,2*x/a) for a in range(lo,active_hi+1))
    return c, old

def block_constants_on_interval(x, lo, hi, tau, A):
    """返回 floor 固定时 c/old 的常数和系数。

    delta(k)(X/a)=A[k]-(X/a)(log(X/a)+2G-1)
    块和是 const - X*(S1*log X + S0)。这里只用于导数临界点。
    """
    active_hi=min(hi, math.isqrt(x))
    if active_hi<lo:
        return None
    c_const=c_s_log=c_s0=0.0
    o_const=o_s_log=o_s0=0.0
    for a in range(lo,active_hi+1):
        w=tau[a]
        k1=int(math.floor(x/a))
        k2=int(math.floor(2*x/a))
        inv=w/a
        c_const += w*A[k1]
        c_s_log += inv
        c_s0 += inv*(2*G-1-math.log(a))
        o_const += w*A[k2]
        # old uses y=2X/a, so coefficient has 2/a and log(2X/a)
        o_s_log += 2*inv
        o_s0 += 2*inv*(2*G-1+math.log(2)-math.log(a))
    return (2*c_const,2*c_s_log,2*c_s0,2*o_const,2*o_s_log,2*o_s0)

def fprime_value(x, coeffs, q):
    c_const,c_s_log,c_s0,o_const,o_s_log,o_s0=coeffs
    # c(X)=c_const - X(c_s_log logX + c_s0)
    # old(X)=o_const - X(o_s_log logX + o_s0)
    logx=math.log(x)
    c_val=c_const - x*(c_s_log*logx+c_s0)
    o_val=o_const - x*(o_s_log*logx+o_s0)
    c_der=-(c_s_log*(logx+1)+c_s0)
    o_der=-(o_s_log*(logx+1)+o_s0)
    # F= old/(2X)^.75 - q*c/X^.75
    return (2**(-0.75))*(o_der*x**(-0.75)-0.75*o_val*x**(-1.75))-q*(c_der*x**(-0.75)-0.75*c_val*x**(-1.75))

def candidates_for(start,end,lo,hi):
    cand={start,end}
    # Need jump points for X/a and 2X/a, plus activation a^2.
    for a in range(lo,hi+1):
        aa=a*a
        for z in (aa-1,aa,aa+1):
            if start<=z<=end: cand.add(z)
        for factor in (1,2):
            # floor(factor*X/a)=m jumps at X=a*m/factor.
            m_min=max(1, (factor*start)//a - 2)
            m_max=(factor*end)//a + 2
            for m in range(m_min,m_max+1):
                val=a*m/factor
                for z in (math.floor(val)-1, math.floor(val), math.ceil(val), math.ceil(val)+1):
                    if start<=z<=end: cand.add(int(z))
    return sorted(cand)

def add_critical_candidates(cand, start, end, lo, hi, tau, A, q):
    ordered=sorted(cand)
    extra=set()
    roots=[]
    for left,right in zip(ordered, ordered[1:]):
        if right-left<=2:
            continue
        probe=(left+right)//2
        coeffs=block_constants_on_interval(probe,lo,hi,tau,A)
        if coeffs is None:
            continue
        # 检查端点内侧导数变号；二分一个零点。
        a=left+1; b=right-1
        fa=fprime_value(a,coeffs,q); fb=fprime_value(b,coeffs,q)
        if fa==0:
            root=a
        elif fb==0:
            root=b
        elif fa*fb>0:
            continue
        else:
            lo_x=float(a); hi_x=float(b)
            for _ in range(50):
                mid=(lo_x+hi_x)/2
                fm=fprime_value(mid,coeffs,q)
                if fa*fm<=0:
                    hi_x=mid; fb=fm
                else:
                    lo_x=mid; fa=fm
            root=(lo_x+hi_x)/2
        for z in (math.floor(root)-1,math.floor(root),math.ceil(root),math.ceil(root)+1):
            if start<=z<=end:
                extra.add(int(z))
        roots.append(root)
    return sorted(set(ordered)|extra), roots

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--start',type=int,default=1_000_000)
    ap.add_argument('--end',type=int,default=1_010_000)
    ap.add_argument('--block',type=int,default=200)
    ap.add_argument('--q',type=float,default=0.82)
    ap.add_argument('--json',type=Path)
    args=ap.parse_args()
    tau,A=build(2*args.end)
    rows=[]; total_max=0.0; total_c_bound=0.0; total_old_bound=0.0
    for lo in range(1,math.isqrt(args.end)+1,args.block):
        hi=min(math.isqrt(args.end), lo+args.block-1)
        best=(-1e100,None,0,0)
        best_c=(-1e100,None)
        best_old=(-1e100,None)
        base_cand=candidates_for(args.start,args.end,lo,hi)
        cand, roots=add_critical_candidates(base_cand,args.start,args.end,lo,hi,tau,A,args.q)
        for x in cand:
            c,old=block_values(x,lo,hi,tau,A)
            val=old/(2*x)**0.75 - args.q*c/(x**0.75)
            if val>best[0]: best=(val,x,c/(x**0.75),old/(2*x)**0.75)
            if c/(x**0.75)>best_c[0]: best_c=(c/(x**0.75),x)
            if old/(2*x)**0.75>best_old[0]: best_old=(old/(2*x)**0.75,x)
        rows.append({'lo':lo,'hi':hi,'max_contract':best[0],'x':best[1],'c_norm':best[2],'old_norm':best[3],'best_c':best_c[0],'best_old':best_old[0],'base_candidates':len(base_cand),'critical_roots':len(roots),'total_candidates':len(cand)})
        total_max += max(0.0,best[0])
        total_c_bound += best_c[0]
        total_old_bound += best_old[0]
    payload={'start':args.start,'end':args.end,'block':args.block,'q':args.q,'sum_positive_contract':total_max,'sum_c_bounds':total_c_bound,'sum_old_bounds':total_old_bound,'total_base_candidates':sum(r['base_candidates'] for r in rows),'total_critical_roots':sum(r['critical_roots'] for r in rows),'total_candidates':sum(r['total_candidates'] for r in rows),'rows':rows}
    print(json.dumps({k:v for k,v in payload.items() if k!='rows'}, indent=2))
    print('top rows')
    for r in sorted(rows,key=lambda r:r['max_contract'],reverse=True)[:10]: print(r)
    if args.json:
        args.json.parent.mkdir(parents=True,exist_ok=True); args.json.write_text(json.dumps(payload,ensure_ascii=False,indent=2))
if __name__=='__main__': main()
