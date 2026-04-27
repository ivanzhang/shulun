#!/usr/bin/env python3
"""检验 R/M 段链中“内部桥需求”的结构余额。

核心思想不是解释整个合数块长度，而是解释把 s 个 R 段连接成一条长块所需的
s-1 个内部 M 桥。每个桥尝试由三类刚性支付：

1. 长桥支付：M_len>1 时，多出来的 M 点带来同余锁相。
2. 厚端支付：相邻 R 段长度>1 时，R 粗因子互质带来端点刚性。
3. 模板支付：重复的 (left_R_len, M_len, right_R_len) 形状需要新 M 因子或周期复用。

用法示例：
  python3 experiments/bridge_need_balance.py --P 3000017 --c 458685 --r 8 --C 8 --delta 30 --detail
  python3 experiments/bridge_need_balance.py --scan --primes 1000003,3000017,10000019 --cols 80 --C 8 --delta 30
"""
import argparse
import importlib.util
import random
from collections import Counter
from pathlib import Path

base = Path(__file__).resolve().parent
mods = {}
for name in [
    "segment_level_endpoint_pattern",
    "alternating_chain_analysis",
    "template_capacity_general",
    "revised_dichotomy_analysis",
]:
    spec = importlib.util.spec_from_file_location(name, base / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    mods[name] = mod

gap = mods["segment_level_endpoint_pattern"].gap


def bridge_direct_credits(bridges):
    """给每个内部桥计算直接刚性信用。"""
    rows = []
    for bridge in bridges:
        left = bridge["left_R_len"]
        middle = bridge["M_len"]
        right = bridge["right_R_len"]
        # 中文注释：长 M 桥的额外点都产生连续锁相约束。
        long_credit = max(0, middle - 1)
        # 中文注释：左右 R 段超过单点的厚度，提供粗因子互质端点约束。
        endpoint_credit = max(0, left - 1) + max(0, right - 1)
        # 中文注释：最瘦的 R-M-R 桥没有局部厚度，只能交给交替链或模板复用处理。
        thin = left == 1 and middle == 1 and right == 1
        rows.append({
            "shape": (left, middle, right),
            "long_credit": long_credit,
            "endpoint_credit": endpoint_credit,
            "direct_credit": long_credit + endpoint_credit,
            "thin": thin,
            "m_q_seq": bridge["m_q_seq"],
            "m_n_seq": bridge["m_n_seq"],
            "left_end_n": bridge["left_end_n"],
            "right_start_n": bridge["right_start_n"],
        })
    return rows


def template_repeat_credit(bridges):
    """重复形状信用：同形桥重复越多，越需要模板容量解释。"""
    counter = Counter(tuple(bridge["shape"]) for bridge in bridges)
    repeat_excess = sum(count - 1 for count in counter.values())
    repeated_shapes = sum(1 for count in counter.values() if count >= 2)
    distinct_shapes = len(counter)
    max_repeat = max(counter.values(), default=0)
    return {
        "distinct_shapes": distinct_shapes,
        "repeat_excess": repeat_excess,
        "repeated_shapes": repeated_shapes,
        "max_shape_repeat": max_repeat,
        "shape_counter": counter,
    }


def alternating_bridge_credit(seg_record, alt_record):
    """交替链信用：最长交替链可解释一串连续瘦桥。"""
    # 中文注释：长度为 k 的严格 R/M 交替链最多含 k-2 个内部三点桥窗口。
    max_alt_len = alt_record["max_alt_len"]
    alt_bridge_windows = max(0, max_alt_len - 2)
    thin_bridges = sum(
        1 for bridge in seg_record["bridges"]
        if bridge["left_R_len"] == bridge["M_len"] == bridge["right_R_len"] == 1
    )
    return {
        "max_alt_len": max_alt_len,
        "alt_bridge_windows": alt_bridge_windows,
        "thin_bridges": thin_bridges,
        "alt_pays_thin": min(thin_bridges, alt_bridge_windows),
    }


def record_for(P, c, r, delta, C, primes):
    seg = mods["segment_level_endpoint_pattern"].record_for(P, c, r, delta, C, primes)
    alt = mods["alternating_chain_analysis"].record_for(P, c, r, delta, C, primes)
    tmpl = mods["template_capacity_general"].record_for(P, c, r, delta, C, primes)
    rev = mods["revised_dichotomy_analysis"].record_for(P, c, r, delta, C, primes)

    bridge_rows = bridge_direct_credits(seg["bridges"])
    direct_positive = sum(1 for row in bridge_rows if row["direct_credit"] > 0)
    direct_sum = sum(row["direct_credit"] for row in bridge_rows)
    saturated_direct = sum(min(1, row["direct_credit"]) for row in bridge_rows)
    template = template_repeat_credit(seg["bridges"])
    alt_credit = alternating_bridge_credit(seg, alt)

    bridge_need = seg["internal_bridges"]
    # 中文注释：候选余额逐步从保守到宽松，寻找真正能闭合的组合不等式。
    balance_direct_alt_template = saturated_direct + alt_credit["alt_pays_thin"] + template["repeat_excess"] - bridge_need
    balance_energy_half = rev["revised_energy"] / 2 + alt_credit["alt_bridge_windows"] + tmpl["max_template_m_points"] - bridge_need
    balance_energy_third = rev["revised_energy"] / 3 + alt_credit["alt_bridge_windows"] + tmpl["max_template_m_points"] - bridge_need
    balance_shape_alt_template = template["distinct_shapes"] + alt_credit["alt_bridge_windows"] + tmpl["max_template_m_points"] - bridge_need

    return {
        "P": P,
        "c": c,
        "r": r,
        "L": seg["L"],
        "Y": seg["Y"],
        "U": seg["U"],
        "Prime": seg["Prime"],
        "block_len": seg["block_len"],
        "R_segments": seg["R_segments"],
        "bridge_need": bridge_need,
        "direct_positive": direct_positive,
        "direct_sum": direct_sum,
        "saturated_direct": saturated_direct,
        "thin_bridges": alt_credit["thin_bridges"],
        "max_alt_len": alt_credit["max_alt_len"],
        "alt_bridge_windows": alt_credit["alt_bridge_windows"],
        "alt_pays_thin": alt_credit["alt_pays_thin"],
        "distinct_shapes": template["distinct_shapes"],
        "repeat_excess": template["repeat_excess"],
        "max_shape_repeat": template["max_shape_repeat"],
        "revised_energy": rev["revised_energy"],
        "max_template_m_points": tmpl["max_template_m_points"],
        "balance_direct_alt_template": balance_direct_alt_template,
        "balance_energy_half": balance_energy_half,
        "balance_energy_third": balance_energy_third,
        "balance_shape_alt_template": balance_shape_alt_template,
        "pattern": seg["pattern"],
        "bridge_rows": bridge_rows,
        "shape_counter": template["shape_counter"],
        "template_rows": tmpl["rows"],
    }


def print_record(rec, detail=False):
    """打印桥需求余额记录。"""
    keys = [
        "P", "c", "r", "L", "Y", "U", "Prime", "block_len", "R_segments", "bridge_need",
        "saturated_direct", "thin_bridges", "alt_bridge_windows", "distinct_shapes", "repeat_excess",
        "revised_energy", "max_template_m_points", "balance_direct_alt_template",
        "balance_energy_half", "balance_energy_third", "balance_shape_alt_template",
    ]
    print(",".join(f"{key}={rec[key]}" for key in keys))
    if detail:
        print(f"pattern={rec['pattern']}")
        print(f"shape_counter={rec['shape_counter'].most_common()}")
        print("bridges=shape,direct,thin,left_end,right_start,m_n_seq,m_q_seq")
        for row in rec["bridge_rows"]:
            print(f"{row['shape']},{row['direct_credit']},{row['thin']},{row['left_end_n']},{row['right_start_n']},{row['m_n_seq']},{row['m_q_seq']}")
        print("template_rows=shape,repeat,m_points,distinct_q,periodic_reuse,triple_terms")
        for row in rec["template_rows"][:12]:
            print(f"{row['shape']},{row['repeat']},{row['m_points']},{row['distinct_q']},{row['periodic_reuse']},{row['triple_terms']}")


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
    primes = mods["segment_level_endpoint_pattern"].mlong.segmod.build_primes(Ps, args.C, args.delta)
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
        rows.sort(key=lambda rec: (rec["balance_energy_third"], rec["balance_direct_alt_template"], -rec["bridge_need"], rec["P"], rec["c"], rec["r"]))
        for rec in rows[:30]:
            print_record(rec)
        print(
            "checked", len(rows),
            "min_direct_alt_template", min((x["balance_direct_alt_template"] for x in rows), default=None),
            "min_energy_half", min((x["balance_energy_half"] for x in rows), default=None),
            "min_energy_third", min((x["balance_energy_third"] for x in rows), default=None),
            "min_shape_alt_template", min((x["balance_shape_alt_template"] for x in rows), default=None),
        )
        print(
            "negative_counts",
            "direct_alt_template", sum(x["balance_direct_alt_template"] < 0 for x in rows),
            "energy_half", sum(x["balance_energy_half"] < 0 for x in rows),
            "energy_third", sum(x["balance_energy_third"] < 0 for x in rows),
            "shape_alt_template", sum(x["balance_shape_alt_template"] < 0 for x in rows),
        )
    else:
        print_record(rows[0], args.detail)


if __name__ == "__main__":
    main()
