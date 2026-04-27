#!/usr/bin/env python3
"""统计 T_{u,v}: R-M-R 三点构型，并与三点小筛密度预测比较。

用法示例：
  python3 experiments/rmr_three_point_sieve.py --P 3000017 --c 458685 --r 8 --C 8 --delta 30 --max-offset 8 --detail
  python3 experiments/rmr_three_point_sieve.py --scan --primes 1000003,3000017,10000019 --cols 80 --C 8 --delta 30 --max-offset 8
"""
import argparse
import importlib.util
import math
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


def small_sieve_density(u, v, small_primes):
    """计算三点偏移 {0,u,u+v} 的小筛局部密度。"""
    density = 1.0
    omega_sum = 0
    for p in small_primes:
        residues = {0 % p, u % p, (u + v) % p}
        omega = len(residues)
        omega_sum += omega
        density *= max(0.0, 1.0 - omega / p)
    return density, omega_sum


def label_array(P, c, r, delta, C, primes):
    """返回每个 n 的标签和最小因子。"""
    L = int(C * math.log(P) ** 2 / delta)
    Y = gap.next_prime_ge(math.sqrt(max(2, L)), primes)
    A = c + r * P
    step = delta * P
    small = [p for p in primes if p <= Y and math.gcd(p, step) == 1]
    labels = []
    qs = []
    small_survive = []
    for n in range(L + 1):
        N = A + step * n
        survives = not any(N % p == 0 for p in small)
        small_survive.append(survives)
        if not survives:
            labels.append("S")
            qs.append(None)
            continue
        if mlong.segmod.vb.is_prime_mr(N):
            labels.append("P")
            qs.append(N)
        else:
            q = mlong.segmod.lpf(N, primes)
            labels.append("R" if q > L else "M")
            qs.append(q)
    return L, Y, labels, qs, small


def record_for(P, c, r, delta, C, primes, max_offset):
    """生成三点筛记录。"""
    L, Y, labels, qs, small = label_array(P, c, r, delta, C, primes)
    mid_primes = [p for p in primes if Y < p <= L]
    harmonic_mid = sum(1.0 / p for p in mid_primes)
    rows = []
    total_rmr = 0
    total_small_survive_triples = 0
    total_pred = 0.0
    for u in range(1, max_offset + 1):
        for v in range(1, max_offset + 1):
            limit = L - u - v
            if limit < 0:
                continue
            small_survive_count = 0
            rmr_count = 0
            rm_any_m_count = 0
            q_counter = Counter()
            for a in range(limit + 1):
                if labels[a] == "S" or labels[a + u] == "S" or labels[a + u + v] == "S":
                    continue
                small_survive_count += 1
                if labels[a] == "R" and labels[a + u] == "M" and labels[a + u + v] == "R":
                    rmr_count += 1
                    q_counter[qs[a + u]] += 1
                if labels[a] == "R" and labels[a + u] in {"M", "R", "P"} and labels[a + u + v] == "R":
                    rm_any_m_count += 1
            density, omega_sum = small_sieve_density(u, v, small)
            predicted_small = (limit + 1) * density
            predicted_rmr_scale = predicted_small * harmonic_mid
            total_rmr += rmr_count
            total_small_survive_triples += small_survive_count
            total_pred += predicted_rmr_scale
            if rmr_count or small_survive_count:
                rows.append({
                    "u": u,
                    "v": v,
                    "limit": limit,
                    "small_survive": small_survive_count,
                    "pred_small": predicted_small,
                    "rmr": rmr_count,
                    "pred_rmr_scale": predicted_rmr_scale,
                    "omega_sum": omega_sum,
                    "distinct_mid_q": len(q_counter),
                    "top_q": q_counter.most_common(5),
                })
    rows.sort(key=lambda x: (-x["rmr"], -x["small_survive"], x["u"], x["v"]))
    return {
        "P": P,
        "c": c,
        "r": r,
        "L": L,
        "Y": Y,
        "U_full_survivors": sum(1 for x in labels if x != "S"),
        "Prime": sum(1 for x in labels if x == "P"),
        "max_offset": max_offset,
        "mid_prime_count": len(mid_primes),
        "harmonic_mid": harmonic_mid,
        "total_rmr": total_rmr,
        "total_small_survive_triples": total_small_survive_triples,
        "total_pred_rmr_scale": total_pred,
        "max_rmr_for_uv": rows[0]["rmr"] if rows else 0,
        "rows": rows,
    }


def print_record(rec, detail=False):
    """打印三点筛记录。"""
    keys = [
        "P", "c", "r", "L", "Y", "U_full_survivors", "Prime", "max_offset", "mid_prime_count",
        "total_rmr", "total_small_survive_triples", "total_pred_rmr_scale", "max_rmr_for_uv",
    ]
    print(",".join(f"{key}={rec[key]}" for key in keys))
    if detail:
        print(f"harmonic_mid={rec['harmonic_mid']:.6f}")
        print("top_uv=u,v,small_survive,pred_small,rmr,pred_rmr_scale,distinct_mid_q,top_q")
        for row in rec["rows"][:40]:
            print(
                f"{row['u']},{row['v']},{row['small_survive']},{row['pred_small']:.3f},"
                f"{row['rmr']},{row['pred_rmr_scale']:.3f},{row['distinct_mid_q']},{row['top_q']}"
            )


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
    primes = mlong.segmod.build_primes(Ps, args.C, args.delta)
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
        rows.sort(key=lambda rec: (-rec["total_rmr"], -rec["max_rmr_for_uv"], rec["P"], rec["c"], rec["r"]))
        print("highest three-point-sieve RMR records")
        for rec in rows[:20]:
            print_record(rec, detail=False)
        print(f"checked={len(rows)} max_total_rmr={rows[0]['total_rmr'] if rows else None} max_uv_rmr={max((rec['max_rmr_for_uv'] for rec in rows), default=None)}")
    else:
        print_record(rows[0], detail=args.detail)


if __name__ == "__main__":
    main()
