#!/usr/bin/env python3
"""Hall 型匹配缺口搜索。

左侧：最长合数块中的位置 n。
右侧：根基素数 q 的命中槽。默认每个命中 (q,n) 是一个槽；也可按 q 合并容量。
边：q | N_n。

目标：检查是否存在匹配失败；若失败，输出由 Hopcroft-Karp 可达集给出的 Hall 缺口。

用法示例：
  python3 experiments/hall_matching_search.py --P 3000017 --c 458685 --r 8 --C 8 --delta 30 --detail
  python3 experiments/hall_matching_search.py --scan --primes 1000003,3000017,10000019 --cols 60 --C 8 --delta 30
"""
import argparse
import importlib.util
import math
import random
from collections import deque, defaultdict, Counter
from pathlib import Path

base = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("root_supply_capacity", base / "root_supply_capacity.py")
rsc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rsc)
gap = rsc.gap


def build_graph(rec, mode):
    """构造二分图。"""
    left = [item["n"] for item in rec["block"]]
    left_set = set(left)
    adj = {n: [] for n in left}
    right_labels = []
    right_index = {}

    def add_right(label):
        if label not in right_index:
            right_index[label] = len(right_labels)
            right_labels.append(label)
        return right_index[label]

    if mode == "hit":
        # 中文注释：每个实际命中是一个独立槽；这会非常容易匹配成功。
        for q, ns in rec["hits_by_q"].items():
            for n in ns:
                if n in left_set:
                    idx = add_right((q, n))
                    adj[n].append(idx)
    elif mode == "q_capacity":
        # 中文注释：每个 q 有 capacity=len(hits) 个槽，仍等同原始供给。
        for q, ns in rec["hits_by_q"].items():
            for k, n in enumerate(ns):
                idx = add_right((q, k))
                for target in ns:
                    if target in left_set:
                        adj[target].append(idx)
    elif mode == "q_once":
        # 中文注释：每个 q 只能用一次，测试最强独占压缩。
        for q, ns in rec["hits_by_q"].items():
            idx = add_right((q, 0))
            for n in ns:
                if n in left_set:
                    adj[n].append(idx)
    elif mode == "hybrid":
        # 中文注释：中因子 q<=L 按命中容量给槽；粗因子 q>L 在短带内只给一个槽。
        L = rec["L"]
        for q, ns in rec["hits_by_q"].items():
            if q <= L:
                for k, _ in enumerate(ns):
                    idx = add_right((q, k))
                    for target in ns:
                        if target in left_set:
                            adj[target].append(idx)
            else:
                idx = add_right((q, 0))
                for n in ns:
                    if n in left_set:
                        adj[n].append(idx)
    else:
        raise ValueError(mode)
    return left, right_labels, adj


def hopcroft_karp(left, right_count, adj):
    """Hopcroft-Karp 最大匹配。"""
    pair_u = {u: -1 for u in left}
    pair_v = [-1] * right_count
    dist = {}

    def bfs():
        queue = deque()
        found = False
        for u in left:
            if pair_u[u] == -1:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = None
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                mate = pair_v[v]
                if mate == -1:
                    found = True
                elif dist[mate] is None:
                    dist[mate] = dist[u] + 1
                    queue.append(mate)
        return found

    def dfs(u):
        for v in adj[u]:
            mate = pair_v[v]
            if mate == -1 or (dist[mate] == dist[u] + 1 and dfs(mate)):
                pair_u[u] = v
                pair_v[v] = u
                return True
        dist[u] = None
        return False

    matching = 0
    while bfs():
        for u in left:
            if pair_u[u] == -1 and dfs(u):
                matching += 1
    return matching, pair_u, pair_v


def hall_defect(left, right_count, adj, pair_u, pair_v):
    """从未匹配左点出发找交替可达集，给出一个 Hall 缺口候选。"""
    reachable_u = set()
    reachable_v = set()
    queue = deque([u for u in left if pair_u[u] == -1])
    reachable_u.update(queue)
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if pair_u[u] == v:
                continue
            if v not in reachable_v:
                reachable_v.add(v)
                mate = pair_v[v]
                if mate != -1 and mate not in reachable_u:
                    reachable_u.add(mate)
                    queue.append(mate)
    return reachable_u, reachable_v


def record_for(P, c, r, delta, C, primes, mode):
    """生成匹配记录。"""
    rec = rsc.capacity_for_block(P, c, r, delta, C, primes)
    left, right_labels, adj = build_graph(rec, mode)
    matching, pair_u, pair_v = hopcroft_karp(left, len(right_labels), adj)
    reach_u, reach_v = hall_defect(left, len(right_labels), adj, pair_u, pair_v)
    degrees = [len(adj[u]) for u in left]
    return {
        "P": P,
        "c": c,
        "r": r,
        "L": rec["L"],
        "Y": rec["Y"],
        "Prime": rec["Prime"],
        "block_len": rec["block_len"],
        "mode": mode,
        "left_count": len(left),
        "right_count": len(right_labels),
        "matching": matching,
        "defect": len(left) - matching,
        "min_degree": min(degrees) if degrees else 0,
        "max_degree": max(degrees) if degrees else 0,
        "avg_degree": sum(degrees) / len(degrees) if degrees else 0,
        "hall_left": len(reach_u),
        "hall_right": len(reach_v),
        "hall_gap": len(reach_u) - len(reach_v),
        "pattern": rec["pattern"],
        "left": left,
        "right_labels": right_labels,
        "adj": adj,
        "pair_u": pair_u,
        "lpf_counter": rec["lpf_counter"],
    }


def print_record(rec, detail=False):
    """打印匹配记录。"""
    keys = [
        "P", "c", "r", "L", "Y", "Prime", "block_len", "mode", "left_count", "right_count",
        "matching", "defect", "min_degree", "max_degree", "avg_degree", "hall_left", "hall_right", "hall_gap",
    ]
    print(",".join(f"{key}={rec[key]}" for key in keys))
    if detail:
        print(f"pattern={rec['pattern']}")
        print(f"lpf_counter={rec['lpf_counter'].most_common(20)}")
        print("assignments=n -> slot")
        for n in rec["left"]:
            v = rec["pair_u"][n]
            print(f"{n}->{rec['right_labels'][v] if v != -1 else None}, degree={len(rec['adj'][n])}")


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
    parser.add_argument("--mode", choices=["hit", "q_capacity", "q_once", "hybrid"], default="q_once")
    parser.add_argument("--detail", action="store_true")
    args = parser.parse_args()

    Ps = [int(x) for x in args.primes.split(",") if x.strip()] if args.scan else [args.P]
    if not args.scan and (not args.P or not args.c):
        raise SystemExit("需要 --P --c 或 --scan")
    primes = rsc.mlong.segmod.build_primes(Ps, args.C, args.delta)
    rows = []
    for P in Ps:
        if args.scan:
            random.seed(P)
            cols = list(dict.fromkeys([1, 2, 6, 30, P // 2, P - 1] + random.sample(range(1, P), min(args.cols, P - 1))))
            for c in cols:
                for rr in gap.allowed_residues(P, c, args.delta):
                    rows.append(record_for(P, c, rr, args.delta, args.C, primes, args.mode))
        else:
            rows.append(record_for(P, args.c, args.r, args.delta, args.C, primes, args.mode))

    if args.scan:
        rows.sort(key=lambda row: (-row["defect"], row["right_count" - 0] if False else row["right_count"], -row["block_len"], row["P"], row["c"], row["r"]))
        for rec in rows[:30]:
            print_record(rec)
        print(
            "checked", len(rows),
            "max_defect", max((row["defect"] for row in rows), default=None),
            "perfect", sum(row["defect"] == 0 for row in rows),
            "min_degree", min((row["min_degree"] for row in rows), default=None),
        )
    else:
        print_record(rows[0], args.detail)


if __name__ == "__main__":
    main()
