#!/usr/bin/env python3
"""分析最瘦桥 R^1-M^1-R^1 的连续簇。

目标：把剩余硬核 T<=A+Q 继续压缩。若最瘦桥按桥序号连续出现，则它们在段链中形成
R-M-R-M-R-... 的严格交替簇。长度为 t 的最瘦桥簇正好对应 2t+1 个段，且可提供 t 个
R-M-R 三点窗口；这给出纯组合支付。

用法示例：
  python3 experiments/thin_bridge_cluster_analysis.py --P 1000003 --c 57634 --r 25 --C 8 --delta 30 --detail
  python3 experiments/thin_bridge_cluster_analysis.py --scan --primes 1000003,3000017,10000019 --cols 120 --C 8 --delta 30
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


def thin_bridge_clusters(bridges):
    """按内部桥顺序提取连续最瘦桥簇。"""
    clusters = []
    current = []
    for index, bridge in enumerate(bridges):
        thin = bridge["left_R_len"] == bridge["M_len"] == bridge["right_R_len"] == 1
        if thin:
            current.append((index, bridge))
        else:
            if current:
                clusters.append(current)
            current = []
    if current:
        clusters.append(current)
    return clusters


def record_for(P, c, r, delta, C, primes):
    """生成最瘦桥簇记录。"""
    rec = segpat.record_for(P, c, r, delta, C, primes)
    clusters = thin_bridge_clusters(rec["bridges"])
    cluster_rows = []
    for cluster in clusters:
        indices = [index for index, _ in cluster]
        bridges = [bridge for _, bridge in cluster]
        m_q_seq = [bridge["m_q_seq"][0] for bridge in bridges]
        m_n_seq = [bridge["m_n_seq"][0] for bridge in bridges]
        # 中文注释：长度 t 的最瘦桥簇提供 t 个 R-M-R 三点窗口，完全支付自身 T。
        cluster_rows.append({
            "bridge_indices": indices,
            "len": len(cluster),
            "m_n_seq": m_n_seq,
            "m_q_seq": m_q_seq,
            "distinct_m_q": len(set(m_q_seq)),
            "m_q_reuse": len(m_q_seq) - len(set(m_q_seq)),
            "window_capacity": len(cluster),
            "capacity_minus_need": len(cluster) - len(cluster),
        })
    thin_total = sum(row["len"] for row in cluster_rows)
    total_capacity = sum(row["window_capacity"] for row in cluster_rows)
    return {
        "P": P,
        "c": c,
        "r": r,
        "L": rec["L"],
        "Y": rec["Y"],
        "U": rec["U"],
        "Prime": rec["Prime"],
        "block_len": rec["block_len"],
        "R_segments": rec["R_segments"],
        "bridge_need": rec["internal_bridges"],
        "thin_total": thin_total,
        "cluster_count": len(cluster_rows),
        "max_cluster_len": max((row["len"] for row in cluster_rows), default=0),
        "total_window_capacity": total_capacity,
        "cluster_balance": total_capacity - thin_total,
        "total_m_q_reuse": sum(row["m_q_reuse"] for row in cluster_rows),
        "pattern": rec["pattern"],
        "clusters": cluster_rows,
    }


def print_record(rec, detail=False):
    """打印最瘦桥簇记录。"""
    keys = [
        "P", "c", "r", "L", "Y", "U", "Prime", "block_len", "R_segments", "bridge_need",
        "thin_total", "cluster_count", "max_cluster_len", "total_window_capacity", "cluster_balance",
        "total_m_q_reuse",
    ]
    print(",".join(f"{key}={rec[key]}" for key in keys))
    if detail:
        print(f"pattern={rec['pattern']}")
        print("clusters=indices,len,m_n_seq,m_q_seq,distinct_m_q,m_q_reuse")
        for row in rec["clusters"]:
            print(f"{row['bridge_indices']},{row['len']},{row['m_n_seq']},{row['m_q_seq']},{row['distinct_m_q']},{row['m_q_reuse']}")


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
                    rows.append(record_for(P, c, rr, args.delta, args.C, primes))
        else:
            rows.append(record_for(P, args.c, args.r, args.delta, args.C, primes))

    if args.scan:
        rows.sort(key=lambda row: (row["cluster_balance"], -row["thin_total"], -row["max_cluster_len"], row["P"], row["c"], row["r"]))
        for rec in rows[:30]:
            print_record(rec)
        print(
            "checked", len(rows),
            "min_cluster_balance", min((row["cluster_balance"] for row in rows), default=None),
            "negative", sum(row["cluster_balance"] < 0 for row in rows),
            "max_thin_total", max((row["thin_total"] for row in rows), default=None),
            "max_cluster_len", max((row["max_cluster_len"] for row in rows), default=None),
            "total_m_q_reuse", sum(row["total_m_q_reuse"] for row in rows),
        )
    else:
        print_record(rows[0], args.detail)


if __name__ == "__main__":
    main()
