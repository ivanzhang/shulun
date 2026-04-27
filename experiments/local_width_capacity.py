#!/usr/bin/env python3
"""同端点桥组的局部宽度容量检验。

若同一对 R 端点之间有 b 个 M 点，内部宽度 h=n_right-n_left-1。
若 h < min(M_q)，则同一桥组内任何 M 中因子都不能复用，因为复用要求 q | 差且 0<差<=h<q。
于是 b 个 M 点需要 b 个互异中因子，端点压缩的 b-1 个额外窗口被 b-1 个互异中因子精确补偿。

用法示例：
  python3 experiments/local_width_capacity.py --P 10000019 --c 8701435 --r 24 --C 8 --delta 30 --detail
  python3 experiments/local_width_capacity.py --scan --primes 1000003,3000017,10000019 --cols 120 --C 8 --delta 30
"""
import argparse
import importlib.util
import random
from pathlib import Path

base = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("window_family_capacity", base / "window_family_capacity.py")
wfc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(wfc)
gap = wfc.gap


def record_for(P, c, r, delta, C, primes):
    """生成局部宽度容量记录。"""
    rec = wfc.record_for(P, c, r, delta, C, primes)
    groups = []
    bad_width = []
    bad_reuse = []
    total_extra = 0
    total_diversity_extra = 0
    min_margin = None
    for group in rec["endpoint_pair_groups"]:
        if group["size"] < 2:
            continue
        min_q = min(group["m_qs"])
        margin = min_q - group["interior_width"]
        local_ok = margin > 0 and group["q_reuse"] == 0 and group["distinct_m_q"] == group["size"]
        row = {
            "pair": group["pair"],
            "size": group["size"],
            "width": group["interior_width"],
            "min_q": min_q,
            "margin": margin,
            "distinct_m_q": group["distinct_m_q"],
            "q_reuse": group["q_reuse"],
            "m_ns": group["m_ns"],
            "m_qs": group["m_qs"],
            "local_ok": local_ok,
        }
        groups.append(row)
        total_extra += group["size"] - 1
        total_diversity_extra += group["distinct_m_q"] - 1
        min_margin = margin if min_margin is None else min(min_margin, margin)
        if margin <= 0:
            bad_width.append(row)
        if group["q_reuse"] or group["distinct_m_q"] != group["size"]:
            bad_reuse.append(row)
    return {
        "P": P,
        "c": c,
        "r": r,
        "L": rec["L"],
        "Y": rec["Y"],
        "Prime": rec["Prime"],
        "block_len": rec["block_len"],
        "window_count": rec["window_count"],
        "group_count_ge2": len(groups),
        "max_group_size": max((row["size"] for row in groups), default=0),
        "min_margin": min_margin if min_margin is not None else 0,
        "total_extra": total_extra,
        "total_diversity_extra": total_diversity_extra,
        "balance": total_diversity_extra - total_extra,
        "bad_width": len(bad_width),
        "bad_reuse": len(bad_reuse),
        "pattern": rec["pattern"],
        "groups": groups,
        "bad_width_rows": bad_width,
        "bad_reuse_rows": bad_reuse,
    }


def print_record(rec, detail=False):
    """打印局部宽度容量记录。"""
    keys = [
        "P", "c", "r", "L", "Y", "Prime", "block_len", "window_count", "group_count_ge2",
        "max_group_size", "min_margin", "total_extra", "total_diversity_extra", "balance",
        "bad_width", "bad_reuse",
    ]
    print(",".join(f"{key}={rec[key]}" for key in keys))
    if detail:
        print(f"pattern={rec['pattern']}")
        print("groups=size,width,min_q,margin,distinct_m_q,q_reuse,m_ns,m_qs")
        for row in sorted(rec["groups"], key=lambda x: (x["margin"], -x["size"])):
            print(f"{row['size']},{row['width']},{row['min_q']},{row['margin']},{row['distinct_m_q']},{row['q_reuse']},{row['m_ns']},{row['m_qs']}")


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
    primes = wfc.we.mlong.segmod.build_primes(Ps, args.C, args.delta)
    rows = []
    for P in Ps:
        if args.scan:
            random.seed(P)
            cols = list(dict.fromkeys([1, 2, 6, 30, P // 2, P - 1] + random.sample(range(1, P), min(args.cols, P - 1))))
            for c in cols:
                for rr in gap.allowed_residues(P, c, args.delta):
                    rec = record_for(P, c, rr, args.delta, args.C, primes)
                    if rec["group_count_ge2"]:
                        rows.append(rec)
        else:
            rows.append(record_for(P, args.c, args.r, args.delta, args.C, primes))

    if args.scan:
        rows.sort(key=lambda row: (row["min_margin"], row["balance"], -row["max_group_size"], row["P"], row["c"], row["r"]))
        for rec in rows[:30]:
            print_record(rec)
        print(
            "checked", len(rows),
            "min_margin", min((row["min_margin"] for row in rows), default=None),
            "min_balance", min((row["balance"] for row in rows), default=None),
            "bad_width_total", sum(row["bad_width"] for row in rows),
            "bad_reuse_total", sum(row["bad_reuse"] for row in rows),
            "max_group_size", max((row["max_group_size"] for row in rows), default=None),
        )
    else:
        print_record(rows[0], args.detail)


if __name__ == "__main__":
    main()
