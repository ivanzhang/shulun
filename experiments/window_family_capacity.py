#!/usr/bin/env python3
"""窗口族容量亏损分析。

在第72节的单窗口能量基础上，分析窗口族之间的共享：
- 同一对 R 端点夹住多个 M 点的长桥组；
- 同一 M 中因子 q 的周期复用容量；
- 窗口签名是否可复用；
- 端点共享导致的自由度亏损。

用法示例：
  python3 experiments/window_family_capacity.py --P 3000017 --c 458685 --r 8 --C 8 --delta 30 --detail
  python3 experiments/window_family_capacity.py --scan --primes 1000003,3000017,10000019 --cols 120 --C 8 --delta 30
"""
import argparse
import importlib.util
import random
from collections import Counter, defaultdict
from pathlib import Path

base = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("window_energy_analysis", base / "window_energy_analysis.py")
we = importlib.util.module_from_spec(spec)
spec.loader.exec_module(we)
gap = we.gap


def family_metrics(windows, L):
    """计算窗口族容量指标。"""
    endpoint_pairs = defaultdict(list)
    by_m_q = defaultdict(list)
    signatures = Counter()
    r_positions = set()
    r_qs = []
    for window in windows:
        pair = (window["left_n"], window["right_n"], window["left_q"], window["right_q"])
        endpoint_pairs[pair].append(window)
        by_m_q[window["m_q"]].append(window)
        signature = (
            window["left_q"], window["m_q"], window["right_q"],
            window["lm_gap"], window["mr_gap"],
        )
        signatures[signature] += 1
        r_positions.add((window["left_n"], window["left_q"]))
        r_positions.add((window["right_n"], window["right_q"]))
        r_qs.append(window["left_q"])
        r_qs.append(window["right_q"])

    long_pair_groups = []
    for pair, group in endpoint_pairs.items():
        m_ns = sorted(window["m_n"] for window in group)
        m_qs = [window["m_q"] for window in sorted(group, key=lambda row: row["m_n"])]
        left_n, right_n, left_q, right_q = pair
        interior_width = right_n - left_n - 1
        q_reuse = len(m_qs) - len(set(m_qs))
        # 中文注释：若同一桥组内复用 q，则 q 必须整除 M 位置差；当内部宽度 < q 时复用不可能。
        local_period_violations = []
        by_q_local = defaultdict(list)
        for window in group:
            by_q_local[window["m_q"]].append(window["m_n"])
        for q, ns in by_q_local.items():
            ns = sorted(ns)
            for a, b in zip(ns, ns[1:]):
                if (b - a) % q != 0:
                    local_period_violations.append((q, a, b, b - a))
        long_pair_groups.append({
            "pair": pair,
            "size": len(group),
            "interior_width": interior_width,
            "m_ns": m_ns,
            "m_qs": m_qs,
            "distinct_m_q": len(set(m_qs)),
            "q_reuse": q_reuse,
            "local_period_violations": local_period_violations,
            "density_num": len(group),
            "density_den": max(1, interior_width),
        })

    period_groups = []
    period_defects = []
    for q, group in by_m_q.items():
        ns = sorted(set(window["m_n"] for window in group))
        capacity = L // q + 1
        for a, b in zip(ns, ns[1:]):
            if (b - a) % q != 0:
                period_defects.append((q, a, b, b - a))
        period_groups.append({
            "q": q,
            "count": len(ns),
            "capacity": capacity,
            "slack": capacity - len(ns),
            "span": ns[-1] - ns[0] if len(ns) >= 2 else 0,
            "forced_span": (len(ns) - 1) * q if len(ns) >= 2 else 0,
            "ns": ns,
        })

    endpoint_slot_count = 2 * len(windows)
    endpoint_share_defect = endpoint_slot_count - len(r_positions)
    repeated_signature_excess = sum(count - 1 for count in signatures.values())
    return {
        "endpoint_pair_groups": long_pair_groups,
        "period_groups": period_groups,
        "endpoint_slots": endpoint_slot_count,
        "distinct_r_endpoints": len(r_positions),
        "endpoint_share_defect": endpoint_share_defect,
        "distinct_r_q_in_windows": len(set(r_qs)),
        "signature_repeat_excess": repeated_signature_excess,
        "period_defects": period_defects,
        "max_pair_group_size": max((row["size"] for row in long_pair_groups), default=0),
        "max_m_q_count": max((row["count"] for row in period_groups), default=0),
        "min_period_slack": min((row["slack"] for row in period_groups), default=0),
        "total_period_forced_span": sum(row["forced_span"] for row in period_groups),
    }


def record_for(P, c, r, delta, C, primes):
    """生成窗口族容量记录。"""
    base = we.record_for(P, c, r, delta, C, primes)
    metrics = family_metrics(base["windows"], base["L"])
    W = base["window_count"]
    # 中文注释：压缩比越小，说明窗口共享端点越强；共享越强越依赖中因子的独立性。
    endpoint_compression = metrics["distinct_r_endpoints"] / (2 * W) if W else 0
    return {
        **{key: base[key] for key in [
            "P", "c", "r", "L", "Y", "U", "Prime", "block_len", "R_total", "M_total",
            "window_count", "thin_windows", "direct_windows", "pattern",
        ]},
        **metrics,
        "endpoint_compression": endpoint_compression,
        "windows": base["windows"],
    }


def print_record(rec, detail=False):
    """打印窗口族容量记录。"""
    keys = [
        "P", "c", "r", "L", "Y", "U", "Prime", "block_len", "R_total", "M_total",
        "window_count", "thin_windows", "direct_windows", "distinct_r_endpoints", "endpoint_share_defect",
        "endpoint_compression", "max_pair_group_size", "max_m_q_count", "min_period_slack",
        "signature_repeat_excess", "total_period_forced_span",
    ]
    print(",".join(f"{key}={rec[key]}" for key in keys))
    if detail:
        print(f"pattern={rec['pattern']}")
        print(f"period_defects={rec['period_defects']}")
        print("pair_groups=pair,size,width,m_ns,m_qs,distinct_m_q,q_reuse")
        for row in sorted(rec["endpoint_pair_groups"], key=lambda x: (-x["size"], x["pair"]))[:20]:
            print(f"{row['pair']},{row['size']},{row['interior_width']},{row['m_ns']},{row['m_qs']},{row['distinct_m_q']},{row['q_reuse']}")
        print("period_groups=q,count,capacity,slack,span,forced_span,ns")
        for row in sorted(rec["period_groups"], key=lambda x: (-x["count"], x["q"]))[:20]:
            print(f"{row['q']},{row['count']},{row['capacity']},{row['slack']},{row['span']},{row['forced_span']},{row['ns']}")


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
    primes = we.mlong.segmod.build_primes(Ps, args.C, args.delta)
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
        rows.sort(key=lambda row: (row["endpoint_compression"], -row["window_count"], -row["max_pair_group_size"], row["P"], row["c"], row["r"]))
        for rec in rows[:30]:
            print_record(rec)
        print(
            "checked", len(rows),
            "min_endpoint_compression", min((row["endpoint_compression"] for row in rows), default=None),
            "max_endpoint_share_defect", max((row["endpoint_share_defect"] for row in rows), default=None),
            "max_pair_group_size", max((row["max_pair_group_size"] for row in rows), default=None),
            "max_m_q_count", max((row["max_m_q_count"] for row in rows), default=None),
            "signature_repeat_total", sum(row["signature_repeat_excess"] for row in rows),
            "period_defect_total", sum(len(row["period_defects"]) for row in rows),
        )
    else:
        print_record(rows[0], args.detail)


if __name__ == "__main__":
    main()
