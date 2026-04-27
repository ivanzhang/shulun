#!/usr/bin/env python3
"""分析低能量危险模式：R-M-R-M-... 交替链。

用法示例：
  python3 experiments/alternating_chain_analysis.py --P 3000017 --c 458685 --r 8 --C 8 --delta 30 --detail
  python3 experiments/alternating_chain_analysis.py --scan --primes 1000003,3000017,10000019 --cols 80 --C 8 --delta 30
"""
import argparse
import importlib.util
import random
from collections import Counter
from pathlib import Path

base = Path(__file__).resolve().parent
spec_m = importlib.util.spec_from_file_location("m_long_segment_analysis", base / "m_long_segment_analysis.py")
mlong = importlib.util.module_from_spec(spec_m)
spec_m.loader.exec_module(mlong)

spec_gap = importlib.util.spec_from_file_location("scan_ub_gap", base / "scan_ub_gap.py")
gap = importlib.util.module_from_spec(spec_gap)
spec_gap.loader.exec_module(gap)


def alternating_runs(items):
    """在 U 序列中找 R/M 交替连续子链。"""
    runs = []
    cur = []
    for item in items:
        if item["label"] not in {"R", "M"}:
            if len(cur) >= 3:
                runs.append(cur)
            cur = []
            continue
        if not cur:
            cur = [item]
        elif item["label"] != cur[-1]["label"]:
            cur.append(item)
        else:
            if len(cur) >= 3:
                runs.append(cur)
            cur = [item]
    if len(cur) >= 3:
        runs.append(cur)
    return runs


def run_signature(run):
    """交替链签名。"""
    labels = "".join(x["label"] for x in run)
    qs = [x["q"] for x in run]
    ns = [x["n"] for x in run]
    r_qs = [x["q"] for x in run if x["label"] == "R"]
    m_qs = [x["q"] for x in run if x["label"] == "M"]
    return {
        "len": len(run),
        "labels": labels,
        "u_start": run[0]["u_idx"],
        "u_end": run[-1]["u_idx"],
        "n_start": ns[0],
        "n_end": ns[-1],
        "n_span": ns[-1] - ns[0],
        "R_count": len(r_qs),
        "M_count": len(m_qs),
        "distinct_R_q": len(set(r_qs)),
        "distinct_M_q": len(set(m_qs)),
        "M_q_repeat": len(m_qs) - len(set(m_qs)),
        "q_seq": qs,
        "n_seq": ns,
    }


def record_for(P, c, r, delta, C, primes):
    """生成交替链记录。"""
    L, Y, items = mlong.collect_with_N(P, c, r, delta, C, primes)
    runs = alternating_runs(items)
    sigs = [run_signature(run) for run in runs]
    sigs.sort(key=lambda x: (-x["len"], -x["R_count"], x["u_start"]))
    top = sigs[0] if sigs else None
    return {
        "P": P,
        "c": c,
        "r": r,
        "L": L,
        "Y": Y,
        "U": len(items),
        "Prime": sum(1 for item in items if item["label"] == "P"),
        "run_count": len(sigs),
        "max_alt_len": top["len"] if top else 0,
        "max_alt_R": top["R_count"] if top else 0,
        "max_alt_M": top["M_count"] if top else 0,
        "top_M_q_repeat": top["M_q_repeat"] if top else 0,
        "top_distinct_R_q": top["distinct_R_q"] if top else 0,
        "top_distinct_M_q": top["distinct_M_q"] if top else 0,
        "top": top,
        "sigs": sigs,
    }


def print_record(rec, detail=False):
    """打印交替链。"""
    keys = [
        "P", "c", "r", "L", "Y", "U", "Prime", "run_count", "max_alt_len", "max_alt_R",
        "max_alt_M", "top_distinct_R_q", "top_distinct_M_q", "top_M_q_repeat",
    ]
    print(",".join(f"{key}={rec[key]}" for key in keys))
    if detail and rec["top"]:
        top = rec["top"]
        print(f"labels={top['labels']}")
        print(f"u={top['u_start']}..{top['u_end']} n={top['n_start']}..{top['n_end']} span={top['n_span']}")
        print(f"n_seq={top['n_seq']}")
        print(f"q_seq={top['q_seq']}")
        print("top_runs=len,labels,n_span,R,M,M_q_repeat,n_seq,q_seq")
        for sig in rec["sigs"][:20]:
            print(f"{sig['len']},{sig['labels']},{sig['n_span']},{sig['R_count']},{sig['M_count']},{sig['M_q_repeat']},{sig['n_seq']},{sig['q_seq']}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--scan", action="store_true")
    parser.add_argument("--P", type=int, default=0)
    parser.add_argument("--c", type=int, default=0)
    parser.add_argument("--r", type=int, default=0)
    parser.add_argument("--primes", default="1000003,3000017,10000019")
    parser.add_argument("--cols", type=int, default=80)
    parser.add_argument("--C", type=float, default=8.0)
    parser.add_argument("--delta", type=int, default=30)
    parser.add_argument("--detail", action="store_true")
    args = parser.parse_args()

    Ps = [int(x) for x in args.primes.split(",") if x.strip()] if args.scan else [args.P]
    if not args.scan and (not args.P or not args.c):
        raise SystemExit("非扫描模式需要 --P 与 --c，或使用 --scan")
    primes = mlong.segmod.build_primes(Ps, args.C, args.delta)
    rows = []
    for P in Ps:
        if args.scan:
            random.seed(P)
            cols = list(dict.fromkeys([1, 2, 6, 30, P // 2, P - 1] + random.sample(range(1, P), min(args.cols, P - 1))))
            for c in cols:
                for rr in gap.allowed_residues(P, c, args.delta):
                    rows.append(record_for(P, c, rr, args.delta, args.C, primes))
        else:
            rows.append(record_for(P, args.c, args.r, args.delta, args.C, primes))
    if args.scan:
        rows.sort(key=lambda rec: (-rec["max_alt_len"], -rec["max_alt_R"], rec["P"], rec["c"], rec["r"]))
        print("longest alternating-chain records")
        for rec in rows[:20]:
            print_record(rec, detail=False)
        print(f"checked={len(rows)} max_alt_len={rows[0]['max_alt_len'] if rows else None}")
    else:
        print_record(rows[0], detail=args.detail)


if __name__ == "__main__":
    main()
