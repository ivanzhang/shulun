#!/usr/bin/env python3
"""审计 SN-3 分散正带的有限投影残余。

用法示例：
  python3 experiments/prime_matrix_sn3_distributed_band_projection_audit.py \
    --p-list 5003,10007,20011,50021,100003,200003 \
    --alpha 0.43 \
    --y-factor 4 \
    --tail-factor 10 \
    --top-n 8 \
    --w-list 30,210 \
    --centered-return-share 0.75 \
    --out-prefix docs/sn3_distributed_band_projection_audit_20260506

目标：
  接续 SN-2 正二进带审计，只重新分析其中被标为
  DistributedBandLargeSieve 的正带。对每个候选带重新生成
  (m,q) 事件，并计算 q 短窗、q mod W、d=Py-qm mod W 的
  中心化正桶峰与能量压力。

说明：
  本脚本是结构定位工具，不是证明。阈值只用于发现最紧的
  SN3-DLS/KLS 输入位置。
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
from collections import Counter, defaultdict
from pathlib import Path


def load_sn2_module():
    """加载 SN-2 审计脚本中的基础函数。"""
    path = Path(__file__).with_name("prime_matrix_sn2_band_structure_audit.py")
    spec = importlib.util.spec_from_file_location("sn2_band_audit", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load SN-2 audit module: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


sn2 = load_sn2_module()


def parse_ints(raw: str) -> list[int]:
    """解析逗号分隔整数。"""
    return [int(item) for item in raw.split(",") if item.strip()]


def count_residue_interval(left: int, right: int, modulus: int, residue: int) -> int:
    """统计闭区间内等于指定模类的整数个数。"""
    if left > right:
        return 0
    residue %= modulus
    first = left + ((residue - left) % modulus)
    if first > right:
        return 0
    return (right - first) // modulus + 1


def euler_phi(value: int) -> int:
    """计算欧拉 phi。"""
    result = value
    n = value
    factor = 2
    while factor * factor <= n:
        if n % factor == 0:
            result -= result // factor
            while n % factor == 0:
                n //= factor
        factor += 1
    if n > 1:
        result -= result // n
    return result


def band_bounds(band: str, y: int, m_max: int) -> tuple[int, int]:
    """把 `[2y,4y)` 这类标签转为 m 的整数范围。"""
    if band == "<1y":
        return 1, min(y - 1, m_max)
    body = band.strip()[1:-1]
    left_raw, right_raw = body.split(",")
    left_mul = int(left_raw.replace("y", ""))
    right_mul = int(right_raw.replace("y", ""))
    return max(1, left_mul * y), min(right_mul * y - 1, m_max)


def counter_from_qwindows(q_windows: dict[int, dict[str, float]]) -> tuple[Counter, Counter]:
    """把 q window 字典转为 actual/model 计数器。"""
    actual = Counter()
    model = Counter()
    for idx, item in q_windows.items():
        actual[idx] = int(item.get("actual", 0))
        model[idx] = float(item.get("model", 0.0))
    return actual, model


def partition_metrics(actual: Counter, model: Counter, total_excess: float) -> dict:
    """计算一个分割下的中心化正桶峰与 L2 能量。"""
    keys = set(actual) | set(model)
    diffs = {key: float(actual[key]) - float(model[key]) for key in keys}
    positive = {key: max(0.0, value) for key, value in diffs.items()}
    max_key = None
    max_positive = 0.0
    for key, value in positive.items():
        if value > max_positive:
            max_key = key
            max_positive = value
    positive_sum = sum(positive.values())
    signed_l2 = math.sqrt(sum(value * value for value in diffs.values()))
    chi2 = sum(
        (diffs[key] * diffs[key]) / max(float(model[key]), 1e-9)
        for key in keys
        if model[key] > 0 or actual[key] > 0
    )
    return {
        "block_count": len(keys),
        "max_key": max_key,
        "max_positive": max_positive,
        "max_positive_share_of_E": (
            max_positive / total_excess if total_excess > 0 else 0.0
        ),
        "positive_sum": positive_sum,
        "positive_sum_share_of_E": (
            positive_sum / total_excess if total_excess > 0 else 0.0
        ),
        "signed_l2": signed_l2,
        "chi2": chi2,
        "chi2_sqrt": math.sqrt(chi2),
    }


def projection_for_band(
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
    """重新生成单个分散带的 q 短窗与低模投影账本。"""
    anchor = p * y
    tail_q_min = max(cutoff + 1, int(math.floor(tail_factor * cutoff)) + 1)
    m_max = (anchor - 1) // tail_q_min
    left_m, right_m = band_bounds(band, y, m_max)

    q_windows = defaultdict(lambda: {"actual": 0, "model": 0.0})
    qmod_actual = {w: Counter() for w in w_list}
    qmod_model = {w: Counter() for w in w_list}
    dmod_actual = {w: Counter() for w in w_list}
    dmod_model = {w: Counter() for w in w_list}
    unit_residues = {
        w: [residue for residue in range(w) if math.gcd(residue, w) == 1]
        for w in w_list
    }
    unit_multiplier = {w: w / euler_phi(w) for w in w_list}

    total_actual = 0
    total_model = 0.0
    interval_len = 0
    active_m = 0
    q_min_seen = None
    q_max_seen = None

    for m in range(left_m, right_m + 1):
        if m >= len(rough) or not rough[m]:
            continue
        q_min = max(tail_q_min, sn2.ceil_div(anchor - (p - 1), m))
        q_max = min(p - 1, (anchor - 1) // m)
        if q_min > q_max:
            continue

        local_len = q_max - q_min + 1
        local_log = math.log(max(q_min, 3))
        local_model = local_len / local_log
        count = prefix[q_max] - (prefix[q_min - 1] if q_min > 0 else 0)

        total_actual += count
        total_model += local_model
        interval_len += local_len
        q_min_seen = q_min if q_min_seen is None else min(q_min_seen, q_min)
        q_max_seen = q_max if q_max_seen is None else max(q_max_seen, q_max)

        sn2.add_window_model(q_windows, q_min, q_max, local_log, q_window_width)
        lo = sn2.bisect.bisect_left(primes, q_min)
        hi = sn2.bisect.bisect_right(primes, q_max)
        if hi > lo:
            active_m += 1
        for q in primes[lo:hi]:
            q_windows[q // q_window_width]["actual"] += 1
            for w in w_list:
                qmod_actual[w][q % w] += 1
                dmod_actual[w][(anchor - q * m) % w] += 1

        # q 是大素数，低模主项只能分配到 W 的单位类。
        # 因此每个单位类用 W/phi(W) 修正；非单位类模型为 0。
        for w in w_list:
            for residue in unit_residues[w]:
                residue_count = count_residue_interval(q_min, q_max, w, residue)
                if residue_count == 0:
                    continue
                weight = unit_multiplier[w] * residue_count / local_log
                qmod_model[w][residue] += weight
                dmod_model[w][(anchor - residue * m) % w] += weight

    total_excess = total_actual - total_model
    qwin_actual, qwin_model = counter_from_qwindows(q_windows)
    q_window_metrics = partition_metrics(qwin_actual, qwin_model, total_excess)

    qmod_metrics = {}
    dmod_metrics = {}
    for w in w_list:
        qmod_metrics[str(w)] = partition_metrics(qmod_actual[w], qmod_model[w], total_excess)
        dmod_metrics[str(w)] = partition_metrics(dmod_actual[w], dmod_model[w], total_excess)

    all_peak_shares = [q_window_metrics["max_positive_share_of_E"]]
    all_peak_shares.extend(
        item["max_positive_share_of_E"] for item in qmod_metrics.values()
    )
    all_peak_shares.extend(
        item["max_positive_share_of_E"] for item in dmod_metrics.values()
    )

    return {
        "actual": total_actual,
        "model": total_model,
        "excess": total_excess,
        "actual_over_model": total_actual / total_model if total_model else 0.0,
        "interval_len": interval_len,
        "active_m": active_m,
        "q_min": q_min_seen,
        "q_max": q_max_seen,
        "q_window": q_window_metrics,
        "q_mod_w": qmod_metrics,
        "d_mod_w": dmod_metrics,
        "max_centered_projection_peak_share": max(all_peak_shares) if all_peak_shares else 0.0,
    }


def centered_route(projection: dict, w_list: list[int], threshold: float) -> dict:
    """按中心化投影峰给出 SN-3 诊断路由。"""
    candidates = [
        (
            "centered_sae_return",
            "q_window",
            None,
            projection["q_window"]["max_key"],
            projection["q_window"]["max_positive_share_of_E"],
        )
    ]
    for w in w_list:
        qmod = projection["q_mod_w"][str(w)]
        dmod = projection["d_mod_w"][str(w)]
        candidates.append(
            (
                "centered_pdec_return",
                "q_mod_w",
                w,
                qmod["max_key"],
                qmod["max_positive_share_of_E"],
            )
        )
        candidates.append(
            (
                "centered_columncrt_return",
                "d_mod_w",
                w,
                dmod["max_key"],
                dmod["max_positive_share_of_E"],
            )
        )
    route, kind, w_value, key, share = max(candidates, key=lambda item: item[4])
    if share < threshold:
        route = "true_distributed_dls_candidate"
    return {
        "route": route,
        "peak_kind": kind,
        "peak_w": w_value,
        "peak_key": key,
        "peak_share": share,
        "threshold": threshold,
    }


def audit_p(
    p: int,
    alpha: float,
    y_factor: float,
    tail_factor: float,
    top_n: int,
    q_window_scale: float,
    qwindow_excess_share: float,
    phase_share: float,
    centered_return_share: float,
    w_list: list[int],
    primes: list[int],
    prefix: list[int],
) -> dict:
    """审计单个 P 的 SN-3 分散候选。"""
    cutoff = int(p**alpha)
    low_primes = [q for q in primes if q <= cutoff]
    high_primes = [q for q in primes if cutoff < q < p]
    y_limit = min(p + 1, max(2, int(math.ceil(y_factor * cutoff))))
    tail_q_min = max(cutoff + 1, int(math.floor(tail_factor * cutoff)) + 1)
    m_limit = (p * y_limit - 1) // tail_q_min
    rough = sn2.rough_flags(m_limit, low_primes)
    q_window_width = max(1, int(round(q_window_scale * math.sqrt(p))))

    rows = [
        sn2.row_capacity(p, y, low_primes, high_primes)
        for y in range(2, y_limit + 1)
    ]
    top_rows = sorted(rows, key=lambda row: -row["hit_ratio"])[:top_n]

    candidates = []
    route_counts = Counter()
    for row in top_rows:
        bands = sn2.band_structure_for_row(
            p,
            row["y"],
            cutoff,
            tail_factor,
            low_primes,
            rough,
            prefix,
            primes,
            q_window_width,
        )
        non_tail = row["total_high_hits"] - bands["actual_tail_hits"]
        allowable = row["skeleton_count"] - non_tail
        c_allow = allowable / bands["model_tail"] if bands["model_tail"] else 0.0
        required = (c_allow - 1.0) * bands["model_tail"]

        for band_row in bands["positive_bands"]:
            labels = sn2.classify_band(
                band_row,
                qwindow_excess_share,
                phase_share,
            )
            if "distributed_band_large_sieve_candidate" not in labels:
                continue
            projection = projection_for_band(
                p,
                row["y"],
                band_row["band"],
                cutoff,
                tail_factor,
                rough,
                prefix,
                primes,
                q_window_width,
                w_list,
            )
            route = centered_route(projection, w_list, centered_return_share)
            route_counts[route["route"]] += 1
            excess = projection["excess"]
            model = projection["model"]
            candidates.append(
                {
                    "p": p,
                    "y": row["y"],
                    "x": row["x"],
                    "capacity_margin": row["capacity_margin"],
                    "hit_ratio": row["hit_ratio"],
                    "required_tail_excess": required,
                    "band": band_row["band"],
                    "sn2_labels": labels,
                    "excess_over_required": excess / required if required > 0 else 0.0,
                    "excess_over_sqrt_model": excess / math.sqrt(model) if model > 0 else 0.0,
                    "sn3_centered_route": route,
                    "projection": projection,
                }
            )

    total_excess = sum(item["projection"]["excess"] for item in candidates)
    total_model = sum(item["projection"]["model"] for item in candidates)
    return {
        "p": p,
        "cutoff": cutoff,
        "y_limit": y_limit,
        "q_window_width": q_window_width,
        "distributed_candidate_count": len(candidates),
        "sn3_centered_route_counts": dict(route_counts),
        "total_distributed_excess": total_excess,
        "total_distributed_model": total_model,
        "energy_lower_bound_if_same_sign": (
            (total_excess * total_excess) / total_model if total_model > 0 else 0.0
        ),
        "max_excess_over_required": max(
            (item["excess_over_required"] for item in candidates),
            default=0.0,
        ),
        "max_excess_over_sqrt_model": max(
            (item["excess_over_sqrt_model"] for item in candidates),
            default=0.0,
        ),
        "max_projection_peak_share": max(
            (
                item["projection"]["max_centered_projection_peak_share"]
                for item in candidates
            ),
            default=0.0,
        ),
        "candidates": sorted(
            candidates,
            key=lambda item: -item["excess_over_required"],
        ),
    }


def audit(
    p_list: list[int],
    alpha: float,
    y_factor: float,
    tail_factor: float,
    top_n: int,
    q_window_scale: float,
    qwindow_excess_share: float,
    phase_share: float,
    centered_return_share: float,
    w_list: list[int],
) -> dict:
    """执行全局审计。"""
    flags = sn2.sieve_bool(max(p_list))
    prefix = sn2.prime_prefix(flags)
    primes = sn2.primes_from_flags(flags)
    records = [
        audit_p(
            p,
            alpha,
            y_factor,
            tail_factor,
            top_n,
            q_window_scale,
            qwindow_excess_share,
            phase_share,
            centered_return_share,
            w_list,
            primes,
            prefix,
        )
        for p in p_list
    ]
    all_candidates = [
        item for record in records for item in record["candidates"]
    ]
    route_counts = Counter()
    for record in records:
        route_counts.update(record["sn3_centered_route_counts"])
    return {
        "parameters": {
            "p_list": p_list,
            "alpha": alpha,
            "y_factor": y_factor,
            "tail_factor": tail_factor,
            "top_n": top_n,
            "q_window_scale": q_window_scale,
            "qwindow_excess_share": qwindow_excess_share,
            "phase_share": phase_share,
            "centered_return_share": centered_return_share,
            "w_list": w_list,
        },
        "global_summary": {
            "distributed_candidate_count": len(all_candidates),
            "sn3_centered_route_counts": dict(route_counts),
            "max_excess_over_required": max(
                (item["excess_over_required"] for item in all_candidates),
                default=0.0,
            ),
            "max_excess_over_sqrt_model": max(
                (item["excess_over_sqrt_model"] for item in all_candidates),
                default=0.0,
            ),
            "max_projection_peak_share": max(
                (
                    item["projection"]["max_centered_projection_peak_share"]
                    for item in all_candidates
                ),
                default=0.0,
            ),
            "total_distributed_excess": sum(
                item["projection"]["excess"] for item in all_candidates
            ),
            "total_distributed_model": sum(
                item["projection"]["model"] for item in all_candidates
            ),
        },
        "records": records,
        "top_candidates": sorted(
            all_candidates,
            key=lambda item: -item["excess_over_required"],
        )[:16],
    }


def projection_summary(candidate: dict, w_list: list[int]) -> str:
    """压缩展示候选带投影指标。"""
    projection = candidate["projection"]
    qwin = projection["q_window"]
    parts = [
        f"qwin_peak={qwin['max_positive_share_of_E']:.6f}",
    ]
    for w in w_list:
        qmod = projection["q_mod_w"][str(w)]
        dmod = projection["d_mod_w"][str(w)]
        parts.append(f"qmod{w}_peak={qmod['max_positive_share_of_E']:.6f}")
        parts.append(f"dmod{w}_peak={dmod['max_positive_share_of_E']:.6f}")
    route = candidate["sn3_centered_route"]
    parts.append(
        "route="
        f"{route['route']}:{route['peak_kind']}"
        f"/W={route['peak_w']}/key={route['peak_key']}"
        f"/share={route['peak_share']:.6f}"
    )
    return ", ".join(parts)


def write_markdown(result: dict, path: Path) -> None:
    """写 Markdown 报告。"""
    params = result["parameters"]
    summary = result["global_summary"]
    lines = [
        "# SN-3 分散正带投影残余审计",
        "",
        "**状态：** `sn3_projection_audit_not_a_proof`",
        "",
        "## 参数",
        "",
        f"- `p_list`: `{params['p_list']}`",
        f"- `alpha`: `{params['alpha']}`",
        f"- `y_factor`: `{params['y_factor']}`",
        f"- `tail_factor`: `{params['tail_factor']}`",
        f"- `top_n`: `{params['top_n']}`",
        f"- `q_window_scale`: `{params['q_window_scale']}`",
        f"- `qwindow_excess_share`: `{params['qwindow_excess_share']}`",
        f"- `phase_share`: `{params['phase_share']}`",
        f"- `centered_return_share`: `{params['centered_return_share']}`",
        f"- `w_list`: `{params['w_list']}`",
        "",
        "## 全局摘要",
        "",
        f"- `distributed_candidate_count`: `{summary['distributed_candidate_count']}`",
        f"- `sn3_centered_route_counts`: `{summary['sn3_centered_route_counts']}`",
        f"- `max_excess_over_required`: `{summary['max_excess_over_required']:.6f}`",
        f"- `max_excess_over_sqrt_model`: `{summary['max_excess_over_sqrt_model']:.6f}`",
        f"- `max_projection_peak_share`: `{summary['max_projection_peak_share']:.6f}`",
        f"- `total_distributed_excess`: `{summary['total_distributed_excess']:.6f}`",
        f"- `total_distributed_model`: `{summary['total_distributed_model']:.6f}`",
        "",
        "## 按 P 汇总",
        "",
        "| P | cutoff | y_limit | count | routes | total E | total M | E^2/M | max E/R | max E/sqrt(M) | max proj peak |",
        "|---:|---:|---:|---:|---|---:|---:|---:|---:|---:|---:|",
    ]
    for record in result["records"]:
        lines.append(
            f"| {record['p']} | {record['cutoff']} | {record['y_limit']} | "
            f"{record['distributed_candidate_count']} | "
            f"`{record['sn3_centered_route_counts']}` | "
            f"{record['total_distributed_excess']:.6f} | "
            f"{record['total_distributed_model']:.6f} | "
            f"{record['energy_lower_bound_if_same_sign']:.6f} | "
            f"{record['max_excess_over_required']:.6f} | "
            f"{record['max_excess_over_sqrt_model']:.6f} | "
            f"{record['max_projection_peak_share']:.6f} |"
        )

    lines.extend(["", "## 最紧候选", ""])
    for item in result["top_candidates"][:12]:
        lines.append(
            f"- `P={item['p']}, y={item['y']}, band={item['band']}, "
            f"E={item['projection']['excess']:.3f}, "
            f"M={item['projection']['model']:.3f}, "
            f"E/R={item['excess_over_required']:.6f}, "
            f"E/sqrt(M)={item['excess_over_sqrt_model']:.6f}, "
            f"{projection_summary(item, params['w_list'])}`"
        )

    lines.extend(
        [
            "",
            "## 解释",
            "",
            "该审计只处理 SN-2 中未触发短窗、`q mod 30`、`d mod 30` 峰的分散正带。这里进一步把模型量也投影到 `q mod W` 与 `d mod W`，因此峰值是中心化正桶峰，而不是单纯实际计数峰。",
            "",
            "路由阈值 `centered_return_share` 只是诊断仪表：超过阈值的中心化低维峰回流到 `SAE/PDEC/ColumnCRT` 候选；低于阈值的才登记为 `true_distributed_dls_candidate`。",
            "",
            "`max_projection_peak_share` 越小，说明低维结构越难解释该正带；剩余责任必须由 `SN3-DLS/KLS` 型分散估计吸收。若某个低维中心化峰持续升高，则它不是随机波动，而应路由到 `SAE/PDEC/ColumnCRT`。",
            "",
            "这些数值不能替代证明；它们只给下一步可审稿输入的最紧参数和失败出口位置。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--p-list", default="5003,10007,20011,50021,100003,200003")
    parser.add_argument("--alpha", type=float, default=0.43)
    parser.add_argument("--y-factor", type=float, default=4.0)
    parser.add_argument("--tail-factor", type=float, default=10.0)
    parser.add_argument("--top-n", type=int, default=8)
    parser.add_argument("--q-window-scale", type=float, default=1.0)
    parser.add_argument("--qwindow-excess-share", type=float, default=0.5)
    parser.add_argument("--phase-share", type=float, default=0.35)
    parser.add_argument("--centered-return-share", type=float, default=0.75)
    parser.add_argument("--w-list", default="30,210")
    parser.add_argument(
        "--out-prefix",
        default="docs/sn3_distributed_band_projection_audit_20260506",
    )
    args = parser.parse_args()
    result = audit(
        parse_ints(args.p_list),
        args.alpha,
        args.y_factor,
        args.tail_factor,
        args.top_n,
        args.q_window_scale,
        args.qwindow_excess_share,
        args.phase_share,
        args.centered_return_share,
        parse_ints(args.w_list),
    )
    prefix = Path(args.out_prefix)
    prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, prefix.with_suffix(".md"))
    print(json.dumps(result["global_summary"], ensure_ascii=False), flush=True)


if __name__ == "__main__":
    main()
