#!/usr/bin/env python3
"""把高能量、交替链、模板容量三类工具合成闭合余额检验。"""
import argparse
import importlib.util
import random
from pathlib import Path

base=Path(__file__).resolve().parent
mods={}
for name in ['revised_dichotomy_analysis','alternating_chain_analysis','template_capacity_general','structural_budget_decomposition']:
 spec=importlib.util.spec_from_file_location(name, base/(name+'.py'))
 mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); mods[name]=mod
gap=mods['revised_dichotomy_analysis'].gap

def record_for(P,c,r,delta,C,primes):
 rev=mods['revised_dichotomy_analysis'].record_for(P,c,r,delta,C,primes)
 alt=mods['alternating_chain_analysis'].record_for(P,c,r,delta,C,primes)
 tmpl=mods['template_capacity_general'].record_for(P,c,r,delta,C,primes)
 bud=mods['structural_budget_decomposition'].record_for(P,c,r,delta,C,primes)
 # 三个工具的“解释量”：高能量 E'，最长交替链，最大模板M容量。
 tool_balance=rev['revised_energy'] + alt['max_alt_len'] + tmpl['max_template_m_points']
 # 需要解释的量：最长块长度或 R/M 复杂度。
 need=bud['block_len']
 need_segments=2*rev['R_segments'] if rev['R_segments'] else 0
 return {
  'P':P,'c':c,'r':r,'L':rev['L'],'Y':rev['Y'],'U':rev['U'],'Prime':rev['Prime'],
  'block_len':bud['block_len'],'R_segments':rev['R_segments'],'revised_energy':rev['revised_energy'],
  'max_alt_len':alt['max_alt_len'],'max_template_m_points':tmpl['max_template_m_points'],
  'tool_balance':tool_balance,'balance_minus_block':tool_balance-need,
  'balance_minus_2segments':tool_balance-need_segments,
  'pattern':rev['pattern']
 }

def print_record(rec,detail=False):
 keys=['P','c','r','L','Y','U','Prime','block_len','R_segments','revised_energy','max_alt_len','max_template_m_points','tool_balance','balance_minus_block','balance_minus_2segments']
 print(','.join(f'{k}={rec[k]}' for k in keys))
 if detail: print('pattern='+rec['pattern'])

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--scan',action='store_true')
 ap.add_argument('--P',type=int,default=0); ap.add_argument('--c',type=int,default=0); ap.add_argument('--r',type=int,default=0)
 ap.add_argument('--primes',default='1000003,3000017,10000019'); ap.add_argument('--cols',type=int,default=80)
 ap.add_argument('--C',type=float,default=8.0); ap.add_argument('--delta',type=int,default=30); ap.add_argument('--detail',action='store_true')
 args=ap.parse_args(); Ps=[int(x) for x in args.primes.split(',') if x.strip()] if args.scan else [args.P]
 if not args.scan and (not args.P or not args.c): raise SystemExit('需要 --P --c 或 --scan')
 primes=mods['revised_dichotomy_analysis'].segpat.mlong.segmod.build_primes(Ps,args.C,args.delta); rows=[]
 for P in Ps:
  if args.scan:
   random.seed(P); cols=list(dict.fromkeys([1,2,6,30,P//2,P-1]+random.sample(range(1,P),min(args.cols,P-1))))
   for c in cols:
    for rr in gap.allowed_residues(P,c,args.delta): rows.append(record_for(P,c,rr,args.delta,args.C,primes))
  else: rows.append(record_for(P,args.c,args.r,args.delta,args.C,primes))
 if args.scan:
  rows.sort(key=lambda x:(x['balance_minus_block'], -x['block_len'], x['P'],x['c'],x['r']))
  for rec in rows[:25]: print_record(rec)
  print('checked',len(rows),'min_balance_minus_block',rows[0]['balance_minus_block'] if rows else None,'negative',sum(x['balance_minus_block']<0 for x in rows))
 else: print_record(rows[0],args.detail)
if __name__=='__main__': main()
