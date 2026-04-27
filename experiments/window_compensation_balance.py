#!/usr/bin/env python3
"""窗口族压缩补偿余额。

目标：检验端点压缩节省的粗端点槽位，是否被同端点组内互异 M 中因子和周期跨度补偿。

定义：
- W：窗口数；
- S：端点共享亏损 = 2W - distinct_R_endpoints；
- G：同端点组的内部额外窗口 = Σ(max(0, group_size-1))；
- Q：同端点组内互异 M 因子额外量 = Σ(max(0, distinct_m_q(group)-1))；
- R：中因子周期复用次数 = Σ_q(max(0,t_q-1))；
- Span：周期复用强制跨度 Σ_q(t_q-1)q。

用法示例：
  python3 experiments/window_compensation_balance.py --P 10000019 --c 8701435 --r 24 --C 8 --delta 30 --detail
  python3 experiments/window_compensation_balance.py --scan --primes 1000003,3000017,10000019 --cols 120 --C 8 --delta 30
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


def compensation_metrics(rec):
    """计算若干候选补偿余额。"""
    W = rec["window_count"]
    endpoint_share = rec["endpoint_share_defect"]
    pair_extra = sum(max(0, row["size"] - 1) for row in rec["endpoint_pair_groups"])
    pair_m_diversity = sum(max(0, row["distinct_m_q"] - 1) for row in rec["endpoint_pair_groups"])
    pair_q_reuse = sum(row["q_reuse"] for row in rec["endpoint_pair_groups"])
    period_reuse = sum(max(0, row["count"] - 1) for row in rec["period_groups"])
    period_span = sum(row["forced_span"] for row in rec["period_groups"])
    period_span_units = period_span / rec["L"] if rec["L"] else 0
    # 中文注释：端点共享来自同一端点对内多窗口和链式相邻窗口共享，pair_extra只解释同端点压缩。
    bridge_chain_share = endpoint_share - pair_extra
    return {
        "pair_extra": pair_extra,
        "pair_m_diversity": pair_m_diversity,
        "pair_q_reuse": pair_q_reuse,
        "period_reuse": period_reuse,
        "period_span": period_span,
        "period_span_units": period_span_units,
        "bridge_chain_share": bridge_chain_share,
        "balance_pair_diversity": pair_m_diversity - pair_extra,
        "balance_pair_with_period": pair_m_diversity + period_reuse - pair_extra,
        "balance_endpoint_all": pair_m_diversity + period_reuse - endpoint_share,
        "balance_endpoint_span": pair_m_diversity + period_span_units - endpoint_share,
        "density_pressure": W - rec["distinct_r_endpoints"] - pair_m_diversity,
    }


def record_for(P, c, r, delta, C, primes):
    """生成补偿余额记录。"""
    rec = wfc.record_for(P, c, r, delta, C, primes)
    return {**rec, **compensation_metrics(rec)}


def print_record(rec, detail=False):
    """打印补偿余额。"""
    keys = [
        "P", "c", "r", "L", "Prime", "block_len", "window_count", "distinct_r_endpoints",
        "endpoint_share_defect", "pair_extra", "pair_m_diversity", "period_reuse", "period_span",
        "bridge_chain_share", "balance_pair_diversity", "balance_pair_with_period",
        "balance_endpoint_all", "density_pressure",
    ]
    print(",".join(f"{key}={rec[key]}" for key in keys))
    if detail:
        print(f"pattern={rec['pattern']}")
        print("pair_groups=size,width,distinct_m_q,q_reuse,m_qs")
        for row in sorted(rec["endpoint_pair_groups"], key=lambda x: (-x["size"], x["pair"])):
            print(f"{row['size']},{row['interior_width']},{row['distinct_m_q']},{row['q_reuse']},{row['m_qs']}")
        print("period_groups=q,count,capacity,slack,forced_span,ns")
        for row in sorted(rec["period_groups"], key=lambda x: (-x["count"], x["q"])):
            print(f"{row['q']},{row['count']},{row['capacity']},{row['slack']},{row['forced_span']},{row['ns']}")


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
                    if rec["window_count"]:
                        rows.append(rec)
        else:
            rows.append(record_for(P, args.c, args.r, args.delta, args.C, primes))

    if args.scan:
        rows.sort(key=lambda row: (row["balance_pair_diversity"], row["balance_endpoint_all"], -row["window_count"], row["P"], row["c"], row["r"]))
        for rec in rows[:30]:
            print_record(rec)
        print(
            "checked", len(rows),
            "min_pair_diversity", min((row["balance_pair_diversity"] for row in rows), default=None),
            "min_pair_with_period", min((row["balance_pair_with_period"] for row in rows), default=None),
            "min_endpoint_all", min((row["balance_endpoint_all"] for row in rows), default=None),
            "max_density_pressure", max((row["density_pressure"] for row in rows), default=None),
        )
    else:
        print_record(rows[0], args.detail)


if __name__ == "__main__":
    main()
