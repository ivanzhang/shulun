#!/usr/bin/env python3
"""检验固定 b=1 模板 R^a-M-R^c 的重复容量上界。"""
import argparse
import importlib.util
import random
from collections import defaultdict, Counter
from pathlib import Path

base=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('segment_level_endpoint_pattern', base/'segment_level_endpoint_pattern.py')
segpat=importlib.util.module_from_spec(spec); spec.loader.exec_module(segpat)
spec_gap=importlib.util.spec_from_file_location('scan_ub_gap', base/'scan_ub_gap.py')
gap=importlib.util.module_from_spec(spec_gap); spec_gap.loader.exec_module(gap)

def record_for(P,c,r,delta,C,primes):
 rec=segpat.record_for(P,c,r,delta,C,primes)
 mid_primes=[p for p in primes if rec['Y'] < p <= rec['L']]
 groups=defaultdict(list)
 for b in rec['bridges']:
  shape=tuple(b['shape'])
  if shape[1]==1:
   groups[shape].append(b)
 rows=[]
 for shape, bs in groups.items():
  qs=[b['m_q_seq'][0] for b in bs]
  ns=[b['m_n_seq'][0] for b in bs]
  q_counter=Counter(qs)
  repeat=len(bs)
  distinct_q=len(q_counter)
  periodic_reuse=sum(v-1 for v in q_counter.values())
  # 检查同 q 复用是否均满足 q 周期。
  bad=[]
  byq=defaultdict(list)
  for n,q in zip(ns,qs): byq[q].append(n)
  for q,nlist in byq.items():
   nlist=sorted(nlist)
   for a,b in zip(nlist,nlist[1:]):
    if (b-a)%q!=0: bad.append((q,a,b,b-a))
  rows.append({'shape':shape,'repeat':repeat,'distinct_q':distinct_q,'periodic_reuse':periodic_reuse,'bad':bad,'qs':qs,'ns':ns})
 rows.sort(key=lambda x:(-x['repeat'],x['shape']))
 return {**{k:rec[k] for k in ['P','c','r','L','Y','U','Prime','block_len','R_segments','internal_bridges','pattern']},
         'mid_prime_count':len(mid_primes),'max_b1_repeat':rows[0]['repeat'] if rows else 0,
         'capacity_failures':sum(1 for row in rows if row['repeat']>row['distinct_q']+row['periodic_reuse']),
         'period_bad':sum(len(row['bad']) for row in rows),'rows':rows}

def print_record(rec,detail=False):
 keys=['P','c','r','L','Y','U','Prime','block_len','R_segments','internal_bridges','mid_prime_count','max_b1_repeat','capacity_failures','period_bad']
 print(','.join(f'{k}={rec[k]}' for k in keys))
 if detail:
  print(f"pattern={rec['pattern']}")
  for row in rec['rows'][:20]:
   print(f"shape={row['shape']} repeat={row['repeat']} distinct_q={row['distinct_q']} periodic_reuse={row['periodic_reuse']} qs={row['qs']} ns={row['ns']} bad={row['bad']}")

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--scan',action='store_true')
 ap.add_argument('--P',type=int,default=0); ap.add_argument('--c',type=int,default=0); ap.add_argument('--r',type=int,default=0)
 ap.add_argument('--primes',default='1000003,3000017,10000019'); ap.add_argument('--cols',type=int,default=80)
 ap.add_argument('--C',type=float,default=8.0); ap.add_argument('--delta',type=int,default=30); ap.add_argument('--detail',action='store_true')
 args=ap.parse_args(); Ps=[int(x) for x in args.primes.split(',') if x.strip()] if args.scan else [args.P]
 if not args.scan and (not args.P or not args.c): raise SystemExit('需要 --P --c 或 --scan')
 primes=segpat.mlong.segmod.build_primes(Ps,args.C,args.delta); rows=[]
 for P in Ps:
  if args.scan:
   random.seed(P); cols=list(dict.fromkeys([1,2,6,30,P//2,P-1]+random.sample(range(1,P),min(args.cols,P-1))))
   for c in cols:
    for rr in gap.allowed_residues(P,c,args.delta): rows.append(record_for(P,c,rr,args.delta,args.C,primes))
  else: rows.append(record_for(P,args.c,args.r,args.delta,args.C,primes))
 if args.scan:
  rows.sort(key=lambda x:(-x['max_b1_repeat'],-x['R_segments'],x['P'],x['c'],x['r']))
  for rec in rows[:20]: print_record(rec)
  print('checked',len(rows),'max_b1_repeat',rows[0]['max_b1_repeat'] if rows else None,'period_bad_total',sum(x['period_bad'] for x in rows))
 else: print_record(rows[0],args.detail)
if __name__=='__main__': main()
