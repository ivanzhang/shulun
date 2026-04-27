#!/usr/bin/env python3
"""共享 R 顶点的局部容量分析。

相邻两个内部桥共享一个中间 R 段：
R^{a}-M^{b}-R^{c}-M^{d}-R^{e}
其中共享 R 段长度为 c。若 c>1，由 R 段厚度支付；若 c=1，则形成薄共享，需由左右 M 桥或最瘦交替链支付。

用法示例：
  python3 experiments/shared_r_vertex_capacity.py --P 1000003 --c 57634 --r 25 --C 8 --delta 30 --detail
  python3 experiments/shared_r_vertex_capacity.py --scan --primes 1000003,3000017,10000019 --cols 120 --C 8 --delta 30
"""
import argparse
import importlib.util
import random
from pathlib import Path

base = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("m_long_segment_analysis", base / "m_long_segment_analysis.py")
mlong = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mlong)
gap = mlong.gap


def shared_vertices_from_segments(segs):
    """从段链找相邻内部 M 桥共享的 R 段。"""
    rows = []
    for idx in range(2, len(segs) - 2):
        label, r_seg = segs[idx]
        if label != "R":
            continue
        if not (segs[idx - 1][0] == "M" and segs[idx + 1][0] == "M"):
            continue
        if not (idx - 2 >= 0 and segs[idx - 2][0] == "R" and idx + 2 < len(segs) and segs[idx + 2][0] == "R"):
            continue
        left_m = segs[idx - 1][1]
        right_m = segs[idx + 1][1]
        left_r = segs[idx - 2][1]
        right_r = segs[idx + 2][1]
        r_len = len(r_seg)
        left_m_len = len(left_m)
        right_m_len = len(right_m)
        thin_shared = r_len == 1 and left_m_len == 1 and right_m_len == 1
        # 中文注释：厚 R 段或长 M 桥都提供局部补偿；完全薄共享进入交替链硬核。
        thickness_credit = max(0, r_len - 1)
        m_credit = max(0, left_m_len - 1) + max(0, right_m_len - 1)
        local_credit = thickness_credit + m_credit
        rows.append({
            "seg_idx": idx,
            "r_len": r_len,
            "left_m_len": left_m_len,
            "right_m_len": right_m_len,
            "left_r_len": len(left_r),
            "right_r_len": len(right_r),
            "thin_shared": thin_shared,
            "thickness_credit": thickness_credit,
            "m_credit": m_credit,
            "local_credit": local_credit,
            "r_n_seq": [item["n"] for item in r_seg],
            "r_q_seq": [item["q"] for item in r_seg],
            "left_m_q_seq": [item["q"] for item in left_m],
            "right_m_q_seq": [item["q"] for item in right_m],
        })
    return rows


def thin_shared_clusters(rows):
    """按段索引提取连续完全薄共享簇。"""
    clusters = []
    current = []
    last_idx = None
    for row in rows:
        if not row["thin_shared"]:
            if current:
                clusters.append(current)
            current = []
            last_idx = None
            continue
        if last_idx is None or row["seg_idx"] == last_idx + 2:
            current.append(row)
        else:
            if current:
                clusters.append(current)
            current = [row]
        last_idx = row["seg_idx"]
    if current:
        clusters.append(current)
    return clusters


def record_for(P, c, r, delta, C, primes):
    """生成共享 R 顶点容量记录。"""
    L, Y, items = mlong.collect_with_N(P, c, r, delta, C, primes)
    block = mlong.longest_block(items)
    segs = mlong.segmod.segments(block)
    rows = shared_vertices_from_segments(segs)
    clusters = thin_shared_clusters(rows)
    shared_count = len(rows)
    directly_paid = sum(1 for row in rows if row["local_credit"] > 0)
    thin_count = sum(1 for row in rows if row["thin_shared"])
    local_credit_sum = sum(row["local_credit"] for row in rows)
    thin_cluster_capacity = sum(len(cluster) for cluster in clusters)
    pattern = "".join(label + str(len(seg)) for label, seg in segs)
    return {
        "P": P,
        "c": c,
        "r": r,
        "L": L,
        "Y": Y,
        "Prime": sum(1 for item in items if item["label"] == "P"),
        "block_len": len(block),
        "shared_count": shared_count,
        "directly_paid": directly_paid,
        "thin_count": thin_count,
        "local_credit_sum": local_credit_sum,
        "thin_cluster_count": len(clusters),
        "thin_cluster_capacity": thin_cluster_capacity,
        "balance_saturated": directly_paid + thin_cluster_capacity - shared_count,
        "max_thin_cluster": max((len(cluster) for cluster in clusters), default=0),
        "pattern": pattern,
        "rows": rows,
        "thin_clusters": clusters,
    }


def print_record(rec, detail=False):
    """打印共享 R 顶点记录。"""
    keys = [
        "P", "c", "r", "L", "Y", "Prime", "block_len", "shared_count", "directly_paid",
        "thin_count", "thin_cluster_count", "thin_cluster_capacity", "balance_saturated",
        "max_thin_cluster", "local_credit_sum",
    ]
    print(",".join(f"{key}={rec[key]}" for key in keys))
    if detail:
        print(f"pattern={rec['pattern']}")
        print("shared=seg_idx,r_len,leftM,rightM,thin,credit,r_n,r_q,left_m_q,right_m_q")
        for row in rec["rows"]:
            print(f"{row['seg_idx']},{row['r_len']},{row['left_m_len']},{row['right_m_len']},{row['thin_shared']},{row['local_credit']},{row['r_n_seq']},{row['r_q_seq']},{row['left_m_q_seq']},{row['right_m_q_seq']}")


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
    primes = mlong.segmod.build_primes(Ps, args.C, args.delta)
    rows = []
    for P in Ps:
        if args.scan:
            random.seed(P)
            cols = list(dict.fromkeys([1, 2, 6, 30, P // 2, P - 1] + random.sample(range(1, P), min(args.cols, P - 1))))
            for c in cols:
                for rr in gap.allowed_residues(P, c, args.delta):
                    rec = record_for(P, c, rr, args.delta, args.C, primes)
                    if rec["shared_count"]:
                        rows.append(rec)
        else:
            rows.append(record_for(P, args.c, args.r, args.delta, args.C, primes))

    if args.scan:
        rows.sort(key=lambda row: (row["balance_saturated"], -row["shared_count"], -row["max_thin_cluster"], row["P"], row["c"], row["r"]))
        for rec in rows[:30]:
            print_record(rec)
        print(
            "checked", len(rows),
            "min_balance", min((row["balance_saturated"] for row in rows), default=None),
            "max_shared", max((row["shared_count"] for row in rows), default=None),
            "max_thin_cluster", max((row["max_thin_cluster"] for row in rows), default=None),
        )
    else:
        print_record(rows[0], args.detail)


if __name__ == "__main__":
    main()
