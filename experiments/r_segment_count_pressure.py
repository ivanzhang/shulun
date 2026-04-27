#!/usr/bin/env python3
"""分析 R_segments 的压力来源：短 R 段、插桥、素数断点。

用法示例：
  python3 experiments/r_segment_count_pressure.py --P 3000017 --c 458685 --r 8 --C 8 --delta 30 --detail
  python3 experiments/r_segment_count_pressure.py --scan --primes 1000003,3000017,10000019 --cols 80 --C 8 --delta 30
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


def all_composite_blocks(items):
    """返回所有 U 合数块。"""
    blocks = []
    cur = []
    for item in items + [{"label": "P"}]:
        if item["label"] in {"M", "R"}:
            cur.append(item)
        elif cur:
            blocks.append(cur)
            cur = []
    return blocks


def summarize_block(block):
    """总结一个合数块的段数压力。"""
    segs = mlong.segmod.segments(block)
    r_lens = [len(seg) for label, seg in segs if label == "R"]
    m_lens = [len(seg) for label, seg in segs if label == "M"]
    internal_m = 0
    long_internal_m = 0
    singleton_internal_m = 0
    for idx, (label, seg) in enumerate(segs):
        if label != "M":
            continue
        left_r = idx > 0 and segs[idx - 1][0] == "R"
        right_r = idx + 1 < len(segs) and segs[idx + 1][0] == "R"
        if left_r and right_r:
            internal_m += 1
            if len(seg) == 1:
                singleton_internal_m += 1
            else:
                long_internal_m += 1
    return {
        "block_len": len(block),
        "u_start": block[0]["u_idx"],
        "u_end": block[-1]["u_idx"],
        "n_start": block[0]["n"],
        "n_end": block[-1]["n"],
        "R_segments": len(r_lens),
        "R_total": sum(r_lens),
        "M_segments": len(m_lens),
        "M_total": sum(m_lens),
        "R_len_counter": Counter(r_lens),
        "M_len_counter": Counter(m_lens),
        "short_R_segments": sum(1 for x in r_lens if x == 1),
        "long_R_segments": sum(1 for x in r_lens if x >= 2),
        "internal_m": internal_m,
        "singleton_internal_m": singleton_internal_m,
        "long_internal_m": long_internal_m,
        "pattern": "".join(label + str(len(seg)) for label, seg in segs),
    }


def record_for(P, c, r, delta, C, primes):
    """生成 R 段数压力记录。"""
    L, Y, items = mlong.collect_with_N(P, c, r, delta, C, primes)
    blocks = all_composite_blocks(items)
    summaries = [summarize_block(block) for block in blocks]
    summaries.sort(key=lambda x: (-x["R_segments"], -x["block_len"], x["u_start"]))
    top = summaries[0] if summaries else None
    prime_count = sum(1 for item in items if item["label"] == "P")
    total_R_segments = sum(s["R_segments"] for s in summaries)
    return {
        "P": P,
        "c": c,
        "r": r,
        "L": L,
        "Y": Y,
        "U": len(items),
        "Prime": prime_count,
        "block_count": len(blocks),
        "total_R_segments": total_R_segments,
        "max_R_segments": top["R_segments"] if top else 0,
        "top_block_len": top["block_len"] if top else 0,
        "top_R_total": top["R_total"] if top else 0,
        "top_M_total": top["M_total"] if top else 0,
        "top_short_R_segments": top["short_R_segments"] if top else 0,
        "top_long_R_segments": top["long_R_segments"] if top else 0,
        "top_internal_m": top["internal_m"] if top else 0,
        "top_long_internal_m": top["long_internal_m"] if top else 0,
        "top_singleton_internal_m": top["singleton_internal_m"] if top else 0,
        "top": top,
        "summaries": summaries,
    }


def print_record(rec, detail=False):
    """打印 R 段数压力记录。"""
    keys = [
        "P", "c", "r", "L", "Y", "U", "Prime", "block_count", "total_R_segments", "max_R_segments",
        "top_block_len", "top_R_total", "top_M_total", "top_short_R_segments", "top_long_R_segments",
        "top_internal_m", "top_singleton_internal_m", "top_long_internal_m",
    ]
    print(",".join(f"{key}={rec[key]}" for key in keys))
    if detail and rec["top"]:
        top = rec["top"]
        print(f"pattern={top['pattern']}")
        print(f"R_len_counter={dict(top['R_len_counter'])}")
        print(f"M_len_counter={dict(top['M_len_counter'])}")
        print("all_blocks=R_segments,block_len,R_total,M_total,pattern")
        for block in rec["summaries"]:
            print(f"{block['R_segments']},{block['block_len']},{block['R_total']},{block['M_total']},{block['pattern']}")


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
        rows.sort(key=lambda rec: (-rec["max_R_segments"], -rec["top_block_len"], rec["P"], rec["c"], rec["r"]))
        print("highest R-segment-count records")
        for rec in rows[:20]:
            print_record(rec, detail=False)
        print(f"checked={len(rows)} max_R_segments={rows[0]['max_R_segments'] if rows else None} max_total_R_segments={max((rec['total_R_segments'] for rec in rows), default=None)}")
    else:
        print_record(rows[0], detail=args.detail)


if __name__ == "__main__":
    main()
