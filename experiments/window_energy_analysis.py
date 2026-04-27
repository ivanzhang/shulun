#!/usr/bin/env python3
"""局部窗口同余能量分析。

把桥层闭合后的每个内部桥转成一个或多个局部窗口，并量化：
- R 端点粗因子是否复用；
- M 中因子是否周期复用；
- 三点窗口的模数乘积是否超过短带尺度 L。

用法示例：
  python3 experiments/window_energy_analysis.py --P 1000003 --c 57634 --r 25 --C 8 --delta 30 --detail
  python3 experiments/window_energy_analysis.py --scan --primes 1000003,3000017,10000019 --cols 120 --C 8 --delta 30
"""
import argparse
import importlib.util
import math
import random
from collections import Counter, defaultdict
from pathlib import Path

base = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("m_long_segment_analysis", base / "m_long_segment_analysis.py")
mlong = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mlong)
gap = mlong.gap


def build_windows(P, c, r, delta, C, primes):
    """从最长合数块生成局部窗口。"""
    L, Y, items = mlong.collect_with_N(P, c, r, delta, C, primes)
    block = mlong.longest_block(items)
    segs = mlong.segmod.segments(block)
    windows = []
    for idx, (label, seg) in enumerate(segs):
        if label != "M" or not (idx > 0 and idx + 1 < len(segs)):
            continue
        if segs[idx - 1][0] != "R" or segs[idx + 1][0] != "R":
            continue
        left_r = segs[idx - 1][1]
        right_r = segs[idx + 1][1]
        shape = (len(left_r), len(seg), len(right_r))
        # 中文注释：每个内部 M 点配最近左右 R 端点，形成基本 R-M-R 窗口。
        for offset, m_item in enumerate(seg):
            left_item = left_r[-1] if offset == 0 else left_r[-1]
            right_item = right_r[0] if offset == len(seg) - 1 else right_r[0]
            r_gap = right_item["n"] - left_item["n"]
            lm_gap = m_item["n"] - left_item["n"]
            mr_gap = right_item["n"] - m_item["n"]
            modulus_product = left_item["q"] * m_item["q"] * right_item["q"]
            windows.append({
                "seg_idx": idx,
                "shape": shape,
                "kind": "thin" if shape == (1, 1, 1) else "direct",
                "left_n": left_item["n"],
                "m_n": m_item["n"],
                "right_n": right_item["n"],
                "left_q": left_item["q"],
                "m_q": m_item["q"],
                "right_q": right_item["q"],
                "r_gap": r_gap,
                "lm_gap": lm_gap,
                "mr_gap": mr_gap,
                "modulus_product": modulus_product,
                "log_product_over_L": math.log(modulus_product) / math.log(max(2, L)),
            })
    return L, Y, items, block, segs, windows


def periodic_reuse_defects(windows):
    """检查同一 M 因子的周期复用是否违反 q|差。"""
    by_q = defaultdict(list)
    for window in windows:
        by_q[window["m_q"]].append(window["m_n"])
    defects = []
    reuse = 0
    for q, ns in by_q.items():
        ns = sorted(set(ns))
        reuse += max(0, len(ns) - 1)
        for a, b in zip(ns, ns[1:]):
            if (b - a) % q != 0:
                defects.append((q, a, b, b - a))
    return reuse, defects


def r_factor_reuse(block):
    """统计 R 点粗因子复用。严格理论预期为 0。"""
    r_qs = [item["q"] for item in block if item["label"] == "R"]
    counter = Counter(r_qs)
    return sum(count - 1 for count in counter.values()), counter


def record_for(P, c, r, delta, C, primes):
    """生成窗口能量记录。"""
    L, Y, items, block, segs, windows = build_windows(P, c, r, delta, C, primes)
    m_reuse, m_defects = periodic_reuse_defects(windows)
    r_reuse, r_counter = r_factor_reuse(block)
    products = [window["modulus_product"] for window in windows]
    thin_windows = [window for window in windows if window["kind"] == "thin"]
    direct_windows = [window for window in windows if window["kind"] == "direct"]
    labels = "".join(label + str(len(seg)) for label, seg in segs)
    return {
        "P": P,
        "c": c,
        "r": r,
        "L": L,
        "Y": Y,
        "U": len(items),
        "Prime": sum(1 for item in items if item["label"] == "P"),
        "block_len": len(block),
        "R_total": sum(1 for item in block if item["label"] == "R"),
        "M_total": sum(1 for item in block if item["label"] == "M"),
        "window_count": len(windows),
        "thin_windows": len(thin_windows),
        "direct_windows": len(direct_windows),
        "min_product_over_L": min((p / L for p in products), default=0),
        "min_log_product_over_L": min((window["log_product_over_L"] for window in windows), default=0),
        "m_q_reuse": m_reuse,
        "m_period_defects": len(m_defects),
        "r_q_reuse": r_reuse,
        "distinct_r_q": len(r_counter),
        "pattern": labels,
        "windows": windows,
        "m_defects": m_defects,
        "r_counter": r_counter,
    }


def print_record(rec, detail=False):
    """打印窗口能量记录。"""
    keys = [
        "P", "c", "r", "L", "Y", "U", "Prime", "block_len", "R_total", "M_total",
        "window_count", "thin_windows", "direct_windows", "min_product_over_L",
        "min_log_product_over_L", "m_q_reuse", "m_period_defects", "r_q_reuse", "distinct_r_q",
    ]
    print(",".join(f"{key}={rec[key]}" for key in keys))
    if detail:
        print(f"pattern={rec['pattern']}")
        print(f"m_defects={rec['m_defects']}")
        print("windows=kind,shape,n_triplet,q_triplet,gaps,product,log_product_over_L")
        for window in rec["windows"]:
            print(
                f"{window['kind']},{window['shape']},"
                f"({window['left_n']},{window['m_n']},{window['right_n']}),"
                f"({window['left_q']},{window['m_q']},{window['right_q']}),"
                f"({window['lm_gap']},{window['mr_gap']},{window['r_gap']}),"
                f"{window['modulus_product']},{window['log_product_over_L']:.3f}"
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
                    rows.append(record_for(P, c, rr, args.delta, args.C, primes))
        else:
            rows.append(record_for(P, args.c, args.r, args.delta, args.C, primes))

    if args.scan:
        rows.sort(key=lambda row: (row["min_log_product_over_L"], -row["window_count"], -row["block_len"], row["P"], row["c"], row["r"]))
        for rec in rows[:30]:
            print_record(rec)
        print(
            "checked", len(rows),
            "min_log_product_over_L", min((row["min_log_product_over_L"] for row in rows), default=None),
            "period_defect_total", sum(row["m_period_defects"] for row in rows),
            "r_reuse_total", sum(row["r_q_reuse"] for row in rows),
            "max_window_count", max((row["window_count"] for row in rows), default=None),
            "max_thin_windows", max((row["thin_windows"] for row in rows), default=None),
        )
    else:
        print_record(rows[0], args.detail)


if __name__ == "__main__":
    main()
