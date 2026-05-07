#!/usr/bin/env python3
"""审计 SN3-C 同行多真分散带的同步结构。

用法示例：
  python3 experiments/prime_matrix_sn3c_multiband_sync_audit.py \
    --input docs/sn3_distributed_band_projection_audit_20260506.json \
    --out-prefix docs/sn3c_multiband_sync_audit_20260506

目标：
  SN3-B 的最紧行来自同一行多个 TrueDistributedDLS 带叠加。
  本脚本重算这些带的中心化签名，判断多带叠加是否来自：
    1. q 壳重叠；
    2. 低模 qmod/dmod 同步；
    3. 真正多壳高频同步，需要 KLS/dispersion 输入。
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path


def load_module(name: str, filename: str):
    """从 experiments 目录加载模块。"""
    path = Path(__file__).with_name(filename)
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load module: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


sn2 = load_module("sn2_band_audit", "prime_matrix_sn2_band_structure_audit.py")
sn3 = load_module("sn3_projection_audit", "prime_matrix_sn3_distributed_band_projection_audit.py")


def residue_diffs(actual: Counter, model: Counter) -> dict[int, float]:
    """返回中心化 residue 向量。"""
    keys = set(actual) | set(model)
    return {key: float(actual[key]) - float(model[key]) for key in keys}


def cosine(left: dict[int, float], right: dict[int, float]) -> float:
    """计算两个稀疏向量余弦。"""
    keys = set(left) | set(right)
    dot = sum(left.get(key, 0.0) * right.get(key, 0.0) for key in keys)
    left_norm = math.sqrt(sum(value * value for value in left.values()))
    right_norm = math.sqrt(sum(value * value for value in right.values()))
    if left_norm == 0 or right_norm == 0:
        return 0.0
    return dot / (left_norm * right_norm)


def signature_for_band(
    p: int,
    y: int,
    band: str,
    cutoff: int,
    tail_factor: float,
    rough: bytearray,
    prefix: list[int],
    primes: list[int],
    q_window_width: int,
    w_list: list[int],
) -> dict:
    """重算单带中心化签名。"""
    anchor = p * y
    tail_q_min = max(cutoff + 1, int(math.floor(tail_factor * cutoff)) + 1)
    m_max = (anchor - 1) // tail_q_min
    left_m, right_m = sn3.band_bounds(band, y, m_max)
    qwin_actual = Counter()
    qwin_model = Counter()
    qmod_actual = {w: Counter() for w in w_list}
    qmod_model = {w: Counter() for w in w_list}
    dmod_actual = {w: Counter() for w in w_list}
    dmod_model = {w: Counter() for w in w_list}
    unit_residues = {
        w: [residue for residue in range(w) if math.gcd(residue, w) == 1]
        for w in w_list
    }
    unit_multiplier = {w: w / sn3.euler_phi(w) for w in w_list}

    actual = 0
    model = 0.0
    q_min_seen = None
    q_max_seen = None
    active_m = 0

    for m in range(left_m, right_m + 1):
        if m >= len(rough) or not rough[m]:
            continue
        q_min = max(tail_q_min, sn2.ceil_div(anchor - (p - 1), m))
        q_max = min(p - 1, (anchor - 1) // m)
        if q_min > q_max:
            continue
        local_len = q_max - q_min + 1
        local_log = math.log(max(q_min, 3))
        model += local_len / local_log
        q_min_seen = q_min if q_min_seen is None else min(q_min_seen, q_min)
        q_max_seen = q_max if q_max_seen is None else max(q_max_seen, q_max)

        first_window = q_min // q_window_width
        last_window = q_max // q_window_width
        for idx in range(first_window, last_window + 1):
            left = max(q_min, idx * q_window_width)
            right = min(q_max, (idx + 1) * q_window_width - 1)
            if left <= right:
                qwin_model[idx] += (right - left + 1) / local_log

        lo = sn2.bisect.bisect_left(primes, q_min)
        hi = sn2.bisect.bisect_right(primes, q_max)
        if hi > lo:
            active_m += 1
        for q in primes[lo:hi]:
            actual += 1
            qwin_actual[q // q_window_width] += 1
            for w in w_list:
                qmod_actual[w][q % w] += 1
                dmod_actual[w][(anchor - q * m) % w] += 1

        for w in w_list:
            for residue in unit_residues[w]:
                residue_count = sn3.count_residue_interval(q_min, q_max, w, residue)
                if residue_count == 0:
                    continue
                weight = unit_multiplier[w] * residue_count / local_log
                qmod_model[w][residue] += weight
                dmod_model[w][(anchor - residue * m) % w] += weight

    return {
        "band": band,
        "actual": actual,
        "model": model,
        "excess": actual - model,
        "q_min": q_min_seen,
        "q_max": q_max_seen,
        "active_m": active_m,
        "q_window_diff": residue_diffs(qwin_actual, qwin_model),
        "q_mod_diff": {
            str(w): residue_diffs(qmod_actual[w], qmod_model[w]) for w in w_list
        },
        "d_mod_diff": {
            str(w): residue_diffs(dmod_actual[w], dmod_model[w]) for w in w_list
        },
    }


def interval_overlap(left: tuple[int, int], right: tuple[int, int]) -> int:
    """闭区间交长度。"""
    lo = max(left[0], right[0])
    hi = min(left[1], right[1])
    return max(0, hi - lo + 1)


def pair_report(left: dict, right: dict, w_list: list[int], cosine_threshold: float) -> dict:
    """生成两个带之间的同步报告。"""
    q_overlap = interval_overlap((left["q_min"], left["q_max"]), (right["q_min"], right["q_max"]))
    q_gap = max(0, max(left["q_min"], right["q_min"]) - min(left["q_max"], right["q_max"]) - 1)
    qwin_cos = cosine(left["q_window_diff"], right["q_window_diff"])
    qmod_cos = {}
    dmod_cos = {}
    max_lowmod_cos = -1.0
    max_kind = None
    max_w = None
    for w in w_list:
        q_value = cosine(left["q_mod_diff"][str(w)], right["q_mod_diff"][str(w)])
        d_value = cosine(left["d_mod_diff"][str(w)], right["d_mod_diff"][str(w)])
        qmod_cos[str(w)] = q_value
        dmod_cos[str(w)] = d_value
        if q_value > max_lowmod_cos:
            max_lowmod_cos = q_value
            max_kind = "q_mod"
            max_w = w
        if d_value > max_lowmod_cos:
            max_lowmod_cos = d_value
            max_kind = "d_mod"
            max_w = w
    if q_overlap > 0:
        route = "q_shell_overlap_sae_candidate"
    elif max_lowmod_cos >= cosine_threshold:
        route = "lowmod_multiband_sync_candidate"
    else:
        route = "kls_multishell_candidate"
    return {
        "left_band": left["band"],
        "right_band": right["band"],
        "left_q_shell": [left["q_min"], left["q_max"]],
        "right_q_shell": [right["q_min"], right["q_max"]],
        "q_shell_overlap": q_overlap,
        "q_shell_gap": q_gap,
        "q_window_cosine": qwin_cos,
        "qmod_cosine": qmod_cos,
        "dmod_cosine": dmod_cos,
        "max_lowmod_cosine": max_lowmod_cos,
        "max_lowmod_kind": max_kind,
        "max_lowmod_w": max_w,
        "route": route,
    }


def build_report(data: dict, cosine_threshold: float) -> dict:
    """构造 SN3-C 多带同步报告。"""
    params = data["parameters"]
    p_list = params["p_list"]
    alpha = float(params["alpha"])
    tail_factor = float(params["tail_factor"])
    y_factor = float(params["y_factor"])
    top_n = int(params["top_n"])
    del y_factor, top_n
    w_list = [int(w) for w in params["w_list"]]
    q_window_scale = float(params["q_window_scale"])

    flags = sn2.sieve_bool(max(p_list))
    prefix = sn2.prime_prefix(flags)
    primes = sn2.primes_from_flags(flags)

    grouped = defaultdict(list)
    for record in data["records"]:
        p = record["p"]
        cutoff = record["cutoff"]
        low_primes = [q for q in primes if q <= cutoff]
        # 只需要能覆盖本记录 top 行的 rough 范围。
        y_limit = record["y_limit"]
        tail_q_min = max(cutoff + 1, int(math.floor(tail_factor * cutoff)) + 1)
        m_limit = (p * y_limit - 1) // tail_q_min
        rough = sn2.rough_flags(m_limit, low_primes)
        q_window_width = int(record["q_window_width"])
        if q_window_width <= 0:
            q_window_width = max(1, int(round(q_window_scale * math.sqrt(p))))
        for item in record["candidates"]:
            if item["sn3_centered_route"]["route"] != "true_distributed_dls_candidate":
                continue
            key = (p, item["y"])
            signature = signature_for_band(
                p,
                item["y"],
                item["band"],
                cutoff,
                tail_factor,
                rough,
                prefix,
                primes,
                q_window_width,
                w_list,
            )
            signature["required_tail_excess"] = item["required_tail_excess"]
            signature["excess_over_required"] = item["excess_over_required"]
            grouped[key].append(signature)

    rows = []
    pair_rows = []
    route_counts = Counter()
    for (p, y), signatures in grouped.items():
        if len(signatures) < 2:
            continue
        total_excess = sum(item["excess"] for item in signatures)
        required = signatures[0]["required_tail_excess"]
        pairs = [
            pair_report(left, right, w_list, cosine_threshold)
            for left, right in combinations(signatures, 2)
        ]
        for pair in pairs:
            route_counts[pair["route"]] += 1
            pair_rows.append({"p": p, "y": y, **pair})
        rows.append(
            {
                "p": p,
                "y": y,
                "true_band_count": len(signatures),
                "total_true_excess": total_excess,
                "required_tail_excess": required,
                "total_true_excess_over_required": (
                    total_excess / required if required > 0 else 0.0
                ),
                "bands": [
                    {
                        "band": item["band"],
                        "excess": item["excess"],
                        "q_shell": [item["q_min"], item["q_max"]],
                        "excess_over_required": item["excess_over_required"],
                    }
                    for item in signatures
                ],
                "pairs": pairs,
            }
        )

    return {
        "source_parameters": params,
        "parameters": {"cosine_threshold": cosine_threshold},
        "summary": {
            "multi_true_row_count": len(rows),
            "pair_count": len(pair_rows),
            "pair_route_counts": dict(route_counts),
            "max_multirow_true_excess_over_required": max(
                (row["total_true_excess_over_required"] for row in rows),
                default=0.0,
            ),
            "max_pair_lowmod_cosine": max(
                (row["max_lowmod_cosine"] for row in pair_rows),
                default=0.0,
            ),
            "min_pair_q_shell_gap": min(
                (row["q_shell_gap"] for row in pair_rows),
                default=0,
            ),
        },
        "rows": sorted(rows, key=lambda row: -row["total_true_excess_over_required"]),
        "pairs": sorted(pair_rows, key=lambda row: -row["max_lowmod_cosine"]),
    }


def write_markdown(report: dict, path: Path) -> None:
    """写 Markdown 报告。"""
    summary = report["summary"]
    params = report["source_parameters"]
    lines = [
        "# SN3-C 多真分散带同步审计",
        "",
        "**状态：** `sn3c_multiband_sync_audit_not_a_proof`",
        "",
        "## 参数",
        "",
        f"- `p_list`: `{params['p_list']}`",
        f"- `w_list`: `{params['w_list']}`",
        f"- `cosine_threshold`: `{report['parameters']['cosine_threshold']}`",
        "",
        "## 摘要",
        "",
        f"- `multi_true_row_count`: `{summary['multi_true_row_count']}`",
        f"- `pair_count`: `{summary['pair_count']}`",
        f"- `pair_route_counts`: `{summary['pair_route_counts']}`",
        f"- `max_multirow_true_excess_over_required`: `{summary['max_multirow_true_excess_over_required']:.6f}`",
        f"- `max_pair_lowmod_cosine`: `{summary['max_pair_lowmod_cosine']:.6f}`",
        f"- `min_pair_q_shell_gap`: `{summary['min_pair_q_shell_gap']}`",
        "",
        "## 多带行",
        "",
        "| P | y | true bands | true E/R | pair routes |",
        "|---:|---:|---:|---:|---|",
    ]
    for row in report["rows"]:
        route_counts = Counter(pair["route"] for pair in row["pairs"])
        lines.append(
            f"| {row['p']} | {row['y']} | {row['true_band_count']} | "
            f"{row['total_true_excess_over_required']:.6f} | `{dict(route_counts)}` |"
        )
        for band in row["bands"]:
            lines.append(
                f"|  |  | `{band['band']} q={band['q_shell']}` | "
                f"{band['excess_over_required']:.6f} | E={band['excess']:.6f} |"
            )

    lines.extend(["", "## 最强低模同步对", ""])
    for pair in report["pairs"][:12]:
        lines.append(
            f"- `P={pair['p']}, y={pair['y']}, {pair['left_band']} vs {pair['right_band']}, "
            f"route={pair['route']}, q_gap={pair['q_shell_gap']}, "
            f"qwin_cos={pair['q_window_cosine']:.6f}, "
            f"max_lowmod_cos={pair['max_lowmod_cosine']:.6f} "
            f"({pair['max_lowmod_kind']} W={pair['max_lowmod_w']})`"
        )

    lines.extend(
        [
            "",
            "## 解释",
            "",
            "若两个真分散带的 q 壳相交，则多带同步可回到短窗/SAE；若 q 壳不相交但低模签名余弦很高，则回到 PDEC/ColumnCRT；两者都不发生时，剩余只能登记为多壳 KLS/dispersion 候选。",
            "",
            "该审计不是证明；它把 SN3-B 的多带叠加硬点进一步路由为 `lowmod_multiband_sync` 或 `kls_multishell`。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input",
        default="docs/sn3_distributed_band_projection_audit_20260506.json",
    )
    parser.add_argument("--cosine-threshold", type=float, default=0.75)
    parser.add_argument(
        "--out-prefix",
        default="docs/sn3c_multiband_sync_audit_20260506",
    )
    args = parser.parse_args()
    data = json.loads(Path(args.input).read_text(encoding="utf-8"))
    report = build_report(data, args.cosine_threshold)
    prefix = Path(args.out_prefix)
    prefix.with_suffix(".json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(report, prefix.with_suffix(".md"))
    print(json.dumps(report["summary"], ensure_ascii=False), flush=True)


if __name__ == "__main__":
    main()
