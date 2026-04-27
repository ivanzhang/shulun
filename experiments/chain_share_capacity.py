#!/usr/bin/env python3
"""链式端点共享容量分析。

同端点压缩已由局部宽度引理闭合。本脚本分析剩余的端点共享：相邻窗口共享中间 R 点，形成
R-M-R-M-R 或更一般的内部桥链。

用法示例：
  python3 experiments/chain_share_capacity.py --P 1000003 --c 57634 --r 25 --C 8 --delta 30 --detail
  python3 experiments/chain_share_capacity.py --scan --primes 1000003,3000017,10000019 --cols 120 --C 8 --delta 30
"""
import argparse
import importlib.util
import random
from pathlib import Path

base = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("segment_level_endpoint_pattern", base / "segment_level_endpoint_pattern.py")
segpat = importlib.util.module_from_spec(spec)
spec.loader.exec_module(segpat)
gap = segpat.gap


def bridge_chain_runs(bridges):
    """把内部桥按连续桥序列分成链。当前最长合数块内 bridges 本身就是按序内部桥。"""
    runs = []
    current = []
    last_idx = None
    for index, bridge in enumerate(bridges):
        if last_idx is None or index == last_idx + 1:
            current.append((index, bridge))
        else:
            if current:
                runs.append(current)
            current = [(index, bridge)]
        last_idx = index
    if current:
        runs.append(current)
    return runs


def chain_metrics(bridges):
    """计算链式共享指标。"""
    runs = bridge_chain_runs(bridges)
    rows = []
    total_chain_share = 0
    total_r_positions = 0
    total_m_segments = 0
    for run in runs:
        if not run:
            continue
        shapes = [tuple(bridge["shape"]) for _, bridge in run]
        # 中文注释：桥链有 t 个内部 M 桥，至少 t+1 个 R 段位置参与链式连接。
        t = len(run)
        r_segment_positions = t + 1
        chain_share = max(0, t - 1)
        total_chain_share += chain_share
        total_r_positions += r_segment_positions
        total_m_segments += t
        thin_count = sum(1 for shape in shapes if shape == (1, 1, 1))
        nonthin_count = t - thin_count
        m_qs = [q for _, bridge in run for q in bridge["m_q_seq"]]
        rows.append({
            "bridge_indices": [index for index, _ in run],
            "len": t,
            "chain_share": chain_share,
            "r_segment_positions": r_segment_positions,
            "thin_count": thin_count,
            "nonthin_count": nonthin_count,
            "shapes": shapes,
            "m_qs": m_qs,
            "distinct_m_q": len(set(m_qs)),
            "m_q_reuse": len(m_qs) - len(set(m_qs)),
        })
    return {
        "chain_runs": rows,
        "total_chain_share": total_chain_share,
        "total_r_positions_in_chains": total_r_positions,
        "total_m_segments_in_chains": total_m_segments,
        "max_chain_len": max((row["len"] for row in rows), default=0),
        "max_thin_in_chain": max((row["thin_count"] for row in rows), default=0),
    }


def record_for(P, c, r, delta, C, primes):
    """生成链式共享容量记录。"""
    rec = segpat.record_for(P, c, r, delta, C, primes)
    metrics = chain_metrics(rec["bridges"])
    bridge_count = rec["internal_bridges"]
    # 中文注释：一条含 B 个桥的链，链式共享为 B-1；需要 B+1 个 R 段位置支撑。
    chain_balance = metrics["total_r_positions_in_chains"] - (metrics["total_chain_share"] + 2 * len(metrics["chain_runs"]))
    return {
        "P": P,
        "c": c,
        "r": r,
        "L": rec["L"],
        "Y": rec["Y"],
        "Prime": rec["Prime"],
        "block_len": rec["block_len"],
        "R_segments": rec["R_segments"],
        "bridge_count": bridge_count,
        "chain_count": len(metrics["chain_runs"]),
        "total_chain_share": metrics["total_chain_share"],
        "total_r_positions_in_chains": metrics["total_r_positions_in_chains"],
        "max_chain_len": metrics["max_chain_len"],
        "max_thin_in_chain": metrics["max_thin_in_chain"],
        "chain_balance": chain_balance,
        "pattern": rec["pattern"],
        "chain_runs": metrics["chain_runs"],
    }


def print_record(rec, detail=False):
    """打印链式共享记录。"""
    keys = [
        "P", "c", "r", "L", "Y", "Prime", "block_len", "R_segments", "bridge_count",
        "chain_count", "total_chain_share", "total_r_positions_in_chains", "max_chain_len",
        "max_thin_in_chain", "chain_balance",
    ]
    print(",".join(f"{key}={rec[key]}" for key in keys))
    if detail:
        print(f"pattern={rec['pattern']}")
        print("chains=indices,len,share,Rpos,thin,nonthin,distinct_m_q,m_q_reuse,shapes,m_qs")
        for row in rec["chain_runs"]:
            print(f"{row['bridge_indices']},{row['len']},{row['chain_share']},{row['r_segment_positions']},{row['thin_count']},{row['nonthin_count']},{row['distinct_m_q']},{row['m_q_reuse']},{row['shapes']},{row['m_qs']}")


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
        raise SystemExit("需要 --P --c 或 --scan")
    primes = segpat.mlong.segmod.build_primes(Ps, args.C, args.delta)
    rows = []
    for P in Ps:
        if args.scan:
            random.seed(P)
            cols = list(dict.fromkeys([1, 2, 6, 30, P // 2, P - 1] + random.sample(range(1, P), min(args.cols, P - 1))))
            for c in cols:
                for rr in gap.allowed_residues(P, c, args.delta):
                    rec = record_for(P, c, rr, args.delta, args.C, primes)
                    if rec["bridge_count"]:
                        rows.append(rec)
        else:
            rows.append(record_for(P, args.c, args.r, args.delta, args.C, primes))

    if args.scan:
        rows.sort(key=lambda row: (-row["total_chain_share"], -row["max_chain_len"], row["P"], row["c"], row["r"]))
        for rec in rows[:30]:
            print_record(rec)
        print(
            "checked", len(rows),
            "max_chain_share", max((row["total_chain_share"] for row in rows), default=None),
            "max_chain_len", max((row["max_chain_len"] for row in rows), default=None),
            "min_chain_balance", min((row["chain_balance"] for row in rows), default=None),
        )
    else:
        print_record(rows[0], args.detail)


if __name__ == "__main__":
    main()
