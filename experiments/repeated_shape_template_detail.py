#!/usr/bin/env python3
"""细析固定段形状 R^a-M^b-R^c 重复出现时的 q 序列与间距。"""
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
 details=[]
 for shape, bs in groups.items():
  if len(bs)<2: continue
  all_m_q=[q for b in bs for q in b['m_q_seq']]
  all_left=[b['left_end_n'] for b in bs]
  starts=[b['m_n_seq'][0] for b in bs]
  gaps=[starts[i+1]-starts[i] for i in range(len(starts)-1)]
  details.append({
   'shape':shape,'count':len(bs),'m_points':sum(len(b['m_q_seq']) for b in bs),
   'distinct_m_q':len(set(all_m_q)),'m_q_repeat':len(all_m_q)-len(set(all_m_q)),
   'm_q_counter':Counter(all_m_q),'start_gaps':gaps,'bridges':bs
  })
 details.sort(key=lambda x:(-x['count'],-x['m_points'],x['shape']))
 return {**{k:rec[k] for k in ['P','c','r','L','Y','U','Prime','block_len','R_segments','internal_bridges','pattern']},
         'repeat_shape_count':len(details),'max_shape_repeat':details[0]['count'] if details else 0,'details':details}

def print_record(rec,detail=False):
 keys=['P','c','r','L','Y','U','Prime','block_len','R_segments','internal_bridges','repeat_shape_count','max_shape_repeat']
 print(','.join(f'{k}={rec[k]}' for k in keys))
 if detail:
  print(f"pattern={rec['pattern']}")
  for d in rec['details']:
   print(f"shape={d['shape']} count={d['count']} m_points={d['m_points']} distinct_m_q={d['distinct_m_q']} repeat={d['m_q_repeat']} gaps={d['start_gaps']} q_counter={d['m_q_counter'].most_common()}")
   for b in d['bridges']:
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
  rows.sort(key=lambda x:(-x['max_shape_repeat'],-x['repeat_shape_count'],-x['R_segments'],x['P'],x['c'],x['r']))
  for rec in rows[:12]: print_record(rec)
  print('checked',len(rows),'max_shape_repeat',rows[0]['max_shape_repeat'] if rows else None)
 else: print_record(rows[0],args.detail)
if __name__=='__main__': main()
