#!/usr/bin/env python3
"""批量检查旧区递推 + 新增壳合并余量。"""
from __future__ import annotations
import argparse, csv, json, subprocess, sys
from pathlib import Path

def run_json(cmd: list[str], path: Path) -> dict:
    subprocess.run(cmd + ["--json", str(path)], check=True, stdout=subprocess.DEVNULL)
    return json.loads(path.read_text())

def main() -> int:
    ap=argparse.ArgumentParser()
    ap.add_argument('--start',type=int,default=1_000_000)
    ap.add_argument('--end',type=int,default=1_050_000)
    ap.add_argument('--width',type=int,default=10_000)
    ap.add_argument('--block',type=int,default=200)
    ap.add_argument('--q',type=float,default=0.85)
    ap.add_argument('--shell-cap',type=float,default=0.2)
    ap.add_argument('--csv',type=Path,required=True)
    ap.add_argument('--json',type=Path)
    args=ap.parse_args()
    rows=[]; cur=args.start
    tmpdir=Path('/tmp/d4_recursion_batch'); tmpdir.mkdir(exist_ok=True)
    while cur<args.end:
        nxt=min(args.end,cur+args.width)
        old=run_json([sys.executable,'experiments/d4_block_contract_certificate.py','--start',str(cur),'--end',str(nxt),'--block',str(args.block),'--q',str(args.q)], tmpdir/f'old_{cur}_{nxt}.json')
        shell=run_json([sys.executable,'experiments/d4_new_shell_certificate.py','--start',str(cur),'--end',str(nxt)], tmpdir/f'shell_{cur}_{nxt}.json')
        old_margin=args.q*old['sum_c_bounds']-old['sum_old_bounds']
        shell_margin=args.shell_cap-shell['best_shell_norm']
        combined=old_margin+shell_margin
        # 审稿证书需要保留候选覆盖统计，避免只留下余量数值。
        row={
            'start':cur,'end':nxt,'q':args.q,
            'old_bound':old['sum_old_bounds'],'c_bound':old['sum_c_bounds'],
            'old_margin':old_margin,'shell':shell['best_shell_norm'],
            'shell_margin':shell_margin,'combined_margin':combined,
            'total_base_candidates':old.get('total_base_candidates',0),
            'total_critical_roots':old.get('total_critical_roots',0),
            'total_candidates':old.get('total_candidates',0),
            'shell_base_candidates':shell.get('base_candidates',0),
            'shell_midpoint_candidates':shell.get('midpoint_candidates',0),
            'shell_total_candidates':shell.get('total_candidates',0),
            'shell_monotonicity_certificate':shell.get('monotonicity_certificate',''),
        }
        rows.append(row)
        print(f"[{cur},{nxt}] old_margin={old_margin:.6f} shell={shell['best_shell_norm']:.6f} combined={combined:.6f}")
        cur=nxt
    args.csv.parent.mkdir(parents=True,exist_ok=True)
    with args.csv.open('w',newline='') as h:
        w=csv.DictWriter(h,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    if args.json:
        # 汇总字段用于论文审查：最坏余量与候选覆盖总量必须可直接读取。
        summary={
            'start':args.start,'end':args.end,'width':args.width,
            'block':args.block,'q':args.q,'shell_cap':args.shell_cap,
            'rows':rows,
            'min_old_margin':min(r['old_margin'] for r in rows),
            'min_shell_margin':min(r['shell_margin'] for r in rows),
            'min_combined_margin':min(r['combined_margin'] for r in rows),
            'total_base_candidates':sum(r['total_base_candidates'] for r in rows),
            'total_critical_roots':sum(r['total_critical_roots'] for r in rows),
            'total_candidates':sum(r['total_candidates'] for r in rows),
            'shell_base_candidates':sum(r['shell_base_candidates'] for r in rows),
            'shell_midpoint_candidates':sum(r['shell_midpoint_candidates'] for r in rows),
            'shell_total_candidates':sum(r['shell_total_candidates'] for r in rows),
            'shell_monotonicity_certificate':'piecewise decreasing between activation/floor endpoints',
        }
        args.json.parent.mkdir(parents=True,exist_ok=True)
        args.json.write_text(json.dumps(summary,ensure_ascii=False,indent=2))
    print(f"SUMMARY rows={len(rows)} min_combined={min(r['combined_margin'] for r in rows):.6f}")
    return 0
if __name__=='__main__': raise SystemExit(main())
