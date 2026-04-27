#!/usr/bin/env python3
"""检验一般固定模板 R^a-M^b-R^c 的 M 点容量与周期/高阶锁相。"""
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
 groups=defaultdict(list)
 for b in rec['bridges']:
  groups[tuple(b['shape'])].append(b)
 rows=[]
 for shape, bs in groups.items():
  all_pairs=[]
  triples=0
  for b in bs:
   all_pairs.extend(zip(b['m_n_seq'], b['m_q_seq']))
   triples += max(0, len(b['m_q_seq'])-2)
  q_counter=Counter(q for _,q in all_pairs)
  bad=[]; byq=defaultdict(list)
  for n,q in all_pairs: byq[q].append(n)
  for q,ns in byq.items():
   ns=sorted(ns)
   for x,y in zip(ns,ns[1:]):
    if (y-x)%q!=0: bad.append((q,x,y,y-x))
  rows.append({
   'shape':shape,'repeat':len(bs),'b':shape[1],'m_points':len(all_pairs),
   'distinct_q':len(q_counter),'periodic_reuse':sum(v-1 for v in q_counter.values()),
   'triple_terms':triples,'bad':bad,'q_counter':q_counter,'bridges':bs
  })
 rows.sort(key=lambda x:(-x['m_points'],-x['repeat'],x['shape']))
 return {**{k:rec[k] for k in ['P','c','r','L','Y','U','Prime','block_len','R_segments','internal_bridges','pattern']},
         'max_template_m_points':rows[0]['m_points'] if rows else 0,
         'max_repeat':max((x['repeat'] for x in rows), default=0),
         'period_bad':sum(len(x['bad']) for x in rows),
         'rows':rows}

def print_record(rec,detail=False):
 keys=['P','c','r','L','Y','U','Prime','block_len','R_segments','internal_bridges','max_template_m_points','max_repeat','period_bad']
 print(','.join(f'{k}={rec[k]}' for k in keys))
 if detail:
  print(f"pattern={rec['pattern']}")
  for row in rec['rows'][:20]:
   print(f"shape={row['shape']} repeat={row['repeat']} m_points={row['m_points']} distinct_q={row['distinct_q']} periodic_reuse={row['periodic_reuse']} triple_terms={row['triple_terms']} bad={row['bad']} q_counter={row['q_counter'].most_common()}")
   for b in row['bridges']:
    print(' ',b['left_end_n'],b['right_start_n'],b['m_n_seq'],b['m_q_seq'])

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
  rows.sort(key=lambda x:(-x['max_template_m_points'],-x['max_repeat'],-x['R_segments'],x['P'],x['c'],x['r']))
  for rec in rows[:20]: print_record(rec)
  print('checked',len(rows),'max_template_m_points',rows[0]['max_template_m_points'] if rows else None,'period_bad_total',sum(x['period_bad'] for x in rows))
 else: print_record(rows[0],args.detail)
if __name__=='__main__': main()
