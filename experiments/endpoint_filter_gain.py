#!/usr/bin/env python3
"""量化所有短偏移 RMR 到相邻端点 RMR 的过滤压缩比例。

用法示例：
  python3 experiments/endpoint_filter_gain.py --P 3000017 --c 458685 --r 8 --C 8 --delta 30 --max-offset 8 --detail
  python3 experiments/endpoint_filter_gain.py --scan --primes 1000003,3000017,10000019 --cols 80 --C 8 --delta 30 --max-offset 8
"""
import argparse
import importlib.util
import random
from collections import Counter
from pathlib import Path

base = Path(__file__).resolve().parent
spec_three = importlib.util.spec_from_file_location("rmr_three_point_sieve", base / "rmr_three_point_sieve.py")
three = importlib.util.module_from_spec(spec_three)
spec_three.loader.exec_module(three)

spec_rmr = importlib.util.spec_from_file_location("rmr_local_configuration", base / "rmr_local_configuration.py")
rmr = importlib.util.module_from_spec(spec_rmr)
spec_rmr.loader.exec_module(rmr)

spec_gap = importlib.util.spec_from_file_location("scan_ub_gap", base / "scan_ub_gap.py")
gap = importlib.util.module_from_spec(spec_gap)
spec_gap.loader.exec_module(gap)


def record_for(P, c, r, delta, C, primes, max_offset):
    """生成端点过滤增益记录。"""
    all_rec = three.record_for(P, c, r, delta, C, primes, max_offset)
    endpoint_rec = rmr.record_for(P, c, r, delta, C, primes)
    endpoint_by_shape = Counter((row["d_left"], row["d_right"]) for row in endpoint_rec["records"])
    all_by_shape = Counter()
    for row in all_rec["rows"]:
        all_by_shape[(row["u"], row["v"])] = row["rmr"]
    gains = []
    for shape, total in all_by_shape.items():
        end = endpoint_by_shape.get(shape, 0)
        if total or end:
            gains.append({
                "shape": shape,
                "all_rmr": total,
                "endpoint_rmr": end,
                "filtered_out": total - end,
                "endpoint_ratio": end / total if total else 0.0,
            })
    gains.sort(key=lambda x: (-x["all_rmr"], x["shape"]))
    total_all = all_rec["total_rmr"]
    total_endpoint = endpoint_rec["rmr_count"]
    return {
        "P": P,
        "c": c,
        "r": r,
        "L": all_rec["L"],
        "Y": all_rec["Y"],
        "U": all_rec["U_full_survivors"],
        "Prime": all_rec["Prime"],
        "max_offset": max_offset,
        "total_all_rmr": total_all,
        "endpoint_rmr": total_endpoint,
        "filtered_out": total_all - total_endpoint,
        "endpoint_ratio": total_endpoint / total_all if total_all else 0.0,
        "max_uv_rmr": all_rec["max_rmr_for_uv"],
        "R_segments": endpoint_rec["R_segments"],
        "gains": gains,
    }


def print_record(rec, detail=False):
    """打印端点过滤增益。"""
    keys = [
        "P", "c", "r", "L", "Y", "U", "Prime", "max_offset", "total_all_rmr", "endpoint_rmr",
        "filtered_out", "endpoint_ratio", "max_uv_rmr", "R_segments",
    ]
    print(",".join(f"{key}={rec[key]}" for key in keys))
    if detail:
        print("shape_gain=u,v,all_rmr,endpoint_rmr,filtered_out,endpoint_ratio")
        for row in rec["gains"][:50]:
            print(f"{row['shape'][0]},{row['shape'][1]},{row['all_rmr']},{row['endpoint_rmr']},{row['filtered_out']},{row['endpoint_ratio']:.3f}")


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
    parser.add_argument("--max-offset", type=int, default=8)
    parser.add_argument("--detail", action="store_true")
    args = parser.parse_args()

    Ps = [int(x) for x in args.primes.split(",") if x.strip()] if args.scan else [args.P]
    if not args.scan and (not args.P or not args.c):
        raise SystemExit("非扫描模式需要 --P 与 --c，或使用 --scan")
    primes = three.mlong.segmod.build_primes(Ps, args.C, args.delta)
    rows = []
    for P in Ps:
        if args.scan:
            random.seed(P)
            cols = list(dict.fromkeys([1, 2, 6, 30, P // 2, P - 1] + random.sample(range(1, P), min(args.cols, P - 1))))
            for c in cols:
                for rr in gap.allowed_residues(P, c, args.delta):
                    rows.append(record_for(P, c, rr, args.delta, args.C, primes, args.max_offset))
        else:
            rows.append(record_for(P, args.c, args.r, args.delta, args.C, primes, args.max_offset))
    if args.scan:
        rows.sort(key=lambda rec: (-rec["endpoint_rmr"], rec["endpoint_ratio"], -rec["total_all_rmr"], rec["P"], rec["c"], rec["r"]))
        print("highest endpoint-filter records")
        for rec in rows[:20]:
            print_record(rec, detail=False)
        ratios = [rec["endpoint_ratio"] for rec in rows if rec["total_all_rmr"]]
        print(f"checked={len(rows)} max_endpoint_rmr={rows[0]['endpoint_rmr'] if rows else None} max_ratio={max(ratios) if ratios else None:.6f} min_ratio={min(ratios) if ratios else None:.6f}")
    else:
        print_record(rows[0], detail=args.detail)


if __name__ == "__main__":
    main()
