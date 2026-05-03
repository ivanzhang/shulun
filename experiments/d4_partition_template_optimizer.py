#!/usr/bin/env python3
"""D4 R5 异常层 W/N/K 模板优化证书原型。

用法示例：
  python3 experiments/d4_partition_template_optimizer.py \
    --input docs/d4-r5-offset-layered-scan-1088200-1088600-step1-T60-full.json \
    --json docs/d4-r5-partition-template-optimizer.json
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

CLASSES = ["transition_high_tail", "transition_low_start", "short", "light"]


def classify(item: dict, threshold_tau: int) -> str:
    """按当前 R5 分层规则分类偏移块。"""
    weight = item["tau_sum"]
    count = item["count"]
    values = item.get("a_values", [])
    if weight >= threshold_tau and count > 25:
        return "ordinary"
    if weight >= threshold_tau and 20 < count <= 25:
        high_tail_share = (
            sum(1 for value in values if value >= 120) / len(values) if values else 0.0
        )
        return "transition_high_tail" if high_tail_share >= 0.80 else "transition_low_start"
    if weight >= threshold_tau and count <= 20:
        return "short"
    return "light"


def load_rows(path: Path, threshold_tau: int) -> list[dict]:
    """读取全偏移扫描并提取异常块。"""
    payload = json.loads(path.read_text())
    rows = []
    for row in payload["rows"]:
        items = []
        for item in row["all_offsets"]:
            item_class = classify(item, threshold_tau)
            if item_class == "ordinary":
                continue
            block = {
                "class": item_class,
                "offset": item["offset"],
                "B": item["positive_contract_sum"],
                "W": item["tau_sum"],
                "N": item["count"],
                "K": item["average_kernel"],
            }
            items.append(block)
        rows.append({"x": row["x"], "items": items})
    return rows


def row_metrics(items: list[dict]) -> dict:
    """计算单行异常层指标。"""
    l1 = sum(item["B"] for item in items)
    e2 = sum(item["B"] ** 2 for item in items)
    return {
        "L": l1,
        "E": math.sqrt(e2),
        "R": l1 * l1 / e2 if e2 else 0.0,
        "M": len(items),
        "W": sum(item["W"] for item in items),
        "N": sum(item["N"] for item in items),
    }


def template_key(item: dict, w_bin: int, k_bin: float) -> tuple:
    """生成支配模板键：W 向下取箱，K 向上取箱，N 保留。"""
    w_floor = (item["W"] // w_bin) * w_bin
    k_ceil = math.ceil(item["K"] / k_bin) * k_bin
    return (item["class"], w_floor, item["N"], round(k_ceil, 12))


def build_templates(rows: list[dict], w_bin: int, k_bin: float) -> list[dict]:
    """从观测块云抽取支配模板。"""
    by_key: dict[tuple, dict] = {}
    for row in rows:
        for item in row["items"]:
            key = template_key(item, w_bin, k_bin)
            block_class, w_floor, support, k_ceil = key
            # 用箱右端支配 W，用 K 上取整支配核温。
            w_cap = w_floor + w_bin - 1
            b_cap = k_ceil * w_cap
            old = by_key.get(key)
            if old is None or b_cap > old["B_cap"]:
                by_key[key] = {
                    "class": block_class,
                    "W_min": max(1, w_floor),
                    "W_cap": w_cap,
                    "N": support,
                    "K_cap": k_ceil,
                    "B_cap": b_cap,
                    "witness": item,
                }
    return sorted(by_key.values(), key=lambda item: item["B_cap"], reverse=True)


def empirical_envelope(rows: list[dict], r_values: list[float], l_values: list[float]) -> dict:
    """直接从扫描行中提取经验反共峰曲线。"""
    metrics = [{"x": row["x"], **row_metrics(row["items"])} for row in rows]
    r_floor = []
    for r0 in r_values:
        selected = [row for row in metrics if row["R"] >= r0]
        witness = max(selected, key=lambda row: row["L"], default=None)
        r_floor.append(
            {
                "R0": r0,
                "count": len(selected),
                "max_L": witness["L"] if witness else 0.0,
                "witness_x": witness["x"] if witness else None,
            }
        )
    l_floor = []
    for l0 in l_values:
        selected = [row for row in metrics if row["L"] >= l0]
        witness = max(selected, key=lambda row: row["R"], default=None)
        l_floor.append(
            {
                "L0": l0,
                "count": len(selected),
                "max_R": witness["R"] if witness else 0.0,
                "witness_x": witness["x"] if witness else None,
            }
        )
    return {"r_floor": r_floor, "l_floor": l_floor}


def bounded_knapsack_upper(
    templates: list[dict],
    r0: float,
    w_cap: int,
    n_cap: int,
    m_cap: int,
    scale: int,
) -> dict:
    """用离散 DP 粗求 R>=r0 下 L 的上界。

    状态保留 (W,N,M,E2_scaled) 的最大 L_scaled。这里仍是上界原型，
    因为模板可重复使用；后续需要加入行内同余可实现性约束。
    """
    # 只保留非支配模板，避免状态爆炸。
    candidates = []
    for tpl in templates:
        b_scaled = max(1, math.ceil(tpl["B_cap"] * scale))
        e_scaled = b_scaled * b_scaled
        candidates.append(
            {
                "class": tpl["class"],
                "W": max(1, tpl["W_min"]),
                "N": max(1, tpl["N"]),
                "B": b_scaled,
                "E2": e_scaled,
                "real_B": tpl["B_cap"],
            }
        )
    # 每类每个 N 只保留 B/W 效率较高的前若干模板。
    candidates.sort(key=lambda item: item["real_B"], reverse=True)
    candidates = candidates[:80]

    states = {(0, 0, 0, 0): 0}
    for _ in range(m_cap):
        new_states = dict(states)
        for state, l_scaled in states.items():
            used_w, used_n, used_m, used_e = state
            if used_m >= m_cap:
                continue
            for item in candidates:
                next_w = used_w + item["W"]
                next_n = used_n + item["N"]
                next_m = used_m + 1
                next_e = used_e + item["E2"]
                if next_w > w_cap or next_n > n_cap or next_m > m_cap:
                    continue
                next_l = l_scaled + item["B"]
                key = (next_w, next_n, next_m, next_e)
                if next_l > new_states.get(key, -1):
                    new_states[key] = next_l
        # Pareto 压缩：按 (W,N,M) 保留每个 E2 下最高 L，再截断近似。
        if len(new_states) > 200000:
            scored = []
            for key, value in new_states.items():
                w, n, m, e2 = key
                if e2 == 0:
                    score = value
                else:
                    score = value - int(math.sqrt(e2))
                scored.append((score, key, value))
            scored.sort(reverse=True)
            new_states = {key: value for _, key, value in scored[:120000]}
        states = new_states

    best = 0
    best_state = None
    for (used_w, used_n, used_m, used_e), l_scaled in states.items():
        if used_e == 0:
            continue
        if l_scaled * l_scaled >= r0 * used_e and l_scaled > best:
            best = l_scaled
            best_state = (used_w, used_n, used_m, used_e)
    return {
        "R0": r0,
        "upper_L_scaled": best,
        "upper_L": best / scale,
        "state": best_state,
        "candidate_count": len(candidates),
        "state_count": len(states),
        "note": "prototype upper bound with repeatable templates and approximate pruning",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--json", type=Path, required=True)
    parser.add_argument("--threshold-tau", type=int, default=60)
    parser.add_argument("--w-bin", type=int, default=10)
    parser.add_argument("--k-bin", type=float, default=5e-5)
    parser.add_argument("--scale", type=int, default=1000)
    parser.add_argument("--run-dp", action="store_true")
    args = parser.parse_args()

    rows = load_rows(args.input, args.threshold_tau)
    templates = build_templates(rows, args.w_bin, args.k_bin)
    empirical = empirical_envelope(rows, [10, 18, 24, 30, 36], [0.25, 0.30, 0.35, 0.40])
    row_caps = [row_metrics(row["items"]) for row in rows]
    caps = {
        "max_W": max(row["W"] for row in row_caps),
        "max_N": max(row["N"] for row in row_caps),
        "max_M": max(row["M"] for row in row_caps),
        "max_L": max(row["L"] for row in row_caps),
        "max_R": max(row["R"] for row in row_caps),
    }

    dp = []
    if args.run_dp:
        for r0 in [18, 24, 30, 36]:
            dp.append(
                bounded_knapsack_upper(
                    templates,
                    r0,
                    caps["max_W"],
                    min(400, caps["max_N"]),
                    min(40, caps["max_M"]),
                    args.scale,
                )
            )

    payload = {
        "input": str(args.input),
        "threshold_tau": args.threshold_tau,
        "w_bin": args.w_bin,
        "k_bin": args.k_bin,
        "scale": args.scale,
        "row_caps": caps,
        "template_count": len(templates),
        "top_templates": templates[:30],
        "empirical_envelope": empirical,
        "dp_upper_prototype": dp,
        "status": "certificate prototype; DP is not yet a proof because template repetition ignores congruence-realizability",
    }
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(payload, ensure_ascii=False, indent=2))
    print(
        json.dumps(
            {
                "json": str(args.json),
                "template_count": len(templates),
                "row_caps": caps,
                "empirical": empirical,
                "dp": dp,
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
