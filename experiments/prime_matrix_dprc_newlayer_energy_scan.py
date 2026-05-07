#!/usr/bin/env python3
"""扫描 DPRC 层叠轮新增素因子层 Fourier 能量。

用法示例：
  python3 experiments/prime_matrix_dprc_newlayer_energy_scan.py \
    --max-p 100000 --alpha 0.43 --wheels 30,210,2310 \
    --out-prefix docs/dprc_newlayer_energy_scan_p100000_20260506

目标：
  对 W_prev -> W 的轮层提升，把中心化单位类偏差的 Fourier 能量精确拆为：
  继承频率 h 被新增素因子整除；新增层频率 h 不被新增素因子整除。
  该拆分不需要扫描全部频率，由 Parseval 和按 W_prev 折叠即可得到。
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


BETA_BUCKETS = [
    (0.43, 0.50, "[0.43,0.50)"),
    (0.50, 0.60, "[0.50,0.60)"),
    (0.60, 0.70, "[0.60,0.70)"),
    (0.70, 0.80, "[0.70,0.80)"),
    (0.80, 0.90, "[0.80,0.90)"),
    (0.90, 1.01, "[0.90,1.00)"),
]
L1_DANGER = 12.0 / 5.0
L2_ENERGY = 6.0 / 5.0
L2_CAUCHY = 3.0 / math.sqrt(6.0)


def sieve_bool(limit: int) -> bytearray:
    """返回素数布尔表。"""
    flags = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        flags[0] = 0
    if limit >= 1:
        flags[1] = 0
    for value in range(2, int(limit**0.5) + 1):
        if not flags[value]:
            continue
        start = value * value
        flags[start : limit + 1 : value] = b"\x00" * (
            ((limit - start) // value) + 1
        )
    return flags


def primes_from_flags(flags: bytearray) -> list[int]:
    """提取素数列表。"""
    return [idx for idx, flag in enumerate(flags) if flag]


def units_mod(wheel: int) -> list[int]:
    """返回 wheel 的单位类。"""
    return [residue for residue in range(wheel) if math.gcd(residue, wheel) == 1]


def row_residue(p: int, q: int, side: str) -> int:
    """返回 q 覆盖平方前/后行时的 k 同余类。"""
    p2 = (p * p) % q
    if side == "plus":
        return (-p2) % q
    if side == "minus":
        return p2
    raise ValueError(f"unknown side: {side}")


def n_residue_mod(p: int, k: int, side: str, wheel: int) -> int:
    """返回真实数值 P^2±k 的 mod wheel 残基。"""
    p2 = (p * p) % wheel
    if side == "plus":
        return (p2 + k) % wheel
    return (p2 - k) % wheel


def mark_low_skeleton(p: int, low_primes: list[int], side: str) -> bytearray:
    """标记动态粗骨架。"""
    alive = bytearray(b"\x01") * p
    alive[0] = 0
    for q in low_primes:
        residue = row_residue(p, q, side)
        start = residue if residue > 0 else q
        if start >= p:
            continue
        alive[start:p:q] = b"\x00" * (((p - 1 - start) // q) + 1)
    return alive


def beta_bucket(beta: float) -> str:
    """返回 beta 桶标签。"""
    for left, right, label in BETA_BUCKETS:
        if left <= beta < right:
            return label
    return "outside"


def newlayer_energy(
    centered: dict[int, float], wheel: int, previous_wheel: int | None
) -> dict:
    """用 Parseval 精确拆分继承频率和新增层频率能量。"""
    centered_l2_sq = sum(value * value for value in centered.values())
    total_fourier_energy = wheel * centered_l2_sq
    if previous_wheel is None or not total_fourier_energy:
        return {
            "previous_wheel": previous_wheel,
            "new_factor": None,
            "total_fourier_energy": total_fourier_energy,
            "inherited_fourier_energy": 0.0,
            "newlayer_fourier_energy": total_fourier_energy,
            "newlayer_energy_share": 1.0 if total_fourier_energy else 0.0,
        }

    if wheel % previous_wheel != 0:
        raise ValueError(f"wheel {wheel} is not a multiple of {previous_wheel}")
    new_factor = wheel // previous_wheel
    folded = [0.0] * previous_wheel
    for residue, value in centered.items():
        folded[residue % previous_wheel] += value
    inherited_fourier_energy = previous_wheel * sum(value * value for value in folded)
    newlayer = max(0.0, total_fourier_energy - inherited_fourier_energy)
    return {
        "previous_wheel": previous_wheel,
        "new_factor": new_factor,
        "total_fourier_energy": total_fourier_energy,
        "inherited_fourier_energy": inherited_fourier_energy,
        "newlayer_fourier_energy": newlayer,
        "newlayer_energy_share": newlayer / total_fourier_energy,
    }


def audit_record(
    p: int,
    side: str,
    alpha: float,
    primes: list[int],
    wheels: list[int],
    unit_tables: dict[int, list[int]],
) -> dict:
    """计算单条 P/side 的 BES 与新增层能量指标。"""
    cutoff = int(p**alpha)
    low_primes = [q for q in primes if q <= cutoff]
    high_primes = [q for q in primes if cutoff < q < p]
    alive = mark_low_skeleton(p, low_primes, side)
    skeleton = sum(alive)
    sqrt_s = math.sqrt(skeleton)
    bucket_disc = {label: 0.0 for _left, _right, label in BETA_BUCKETS}
    actual = {wheel: [0] * wheel for wheel in wheels}
    expected_counts = {wheel: [0] * wheel for wheel in wheels}
    harmonic_high = 0.0

    for k, flag in enumerate(alive):
        if not flag:
            continue
        for wheel in wheels:
            expected_counts[wheel][n_residue_mod(p, k, side, wheel)] += 1

    for q in high_primes:
        residue = row_residue(p, q, side)
        start = residue if residue > 0 else q
        hits = 0
        for k in range(start, p, q):
            if not alive[k]:
                continue
            hits += 1
            for wheel in wheels:
                actual[wheel][n_residue_mod(p, k, side, wheel)] += 1
        harmonic_high += 1.0 / q
        label = beta_bucket(math.log(q) / math.log(p))
        if label != "outside":
            bucket_disc[label] += hits - skeleton / q

    bucket_vector = [
        bucket_disc[label] / sqrt_s if sqrt_s else 0.0
        for _left, _right, label in BETA_BUCKETS
    ]
    positive_vector = [max(0.0, value) for value in bucket_vector]
    l1_value = sum(positive_vector)
    l2_value = math.sqrt(sum(value * value for value in positive_vector))
    effective_dimension = (
        (l1_value * l1_value) / (l2_value * l2_value) if l2_value else 0.0
    )

    wheel_rows = []
    previous_wheel: int | None = None
    for wheel in wheels:
        discrepancies = []
        for residue in unit_tables[wheel]:
            expected = expected_counts[wheel][residue] * harmonic_high
            discrepancies.append((residue, actual[wheel][residue] - expected))
        mean = sum(value for _residue, value in discrepancies) / len(discrepancies)
        centered = {residue: value - mean for residue, value in discrepancies}
        centered_top = max(centered.items(), key=lambda item: item[1])
        centered_l2 = math.sqrt(sum(value * value for value in centered.values()))
        energy = newlayer_energy(centered, wheel, previous_wheel)
        wheel_rows.append(
            {
                "wheel": wheel,
                "phi": len(discrepancies),
                "centered_top_residue": centered_top[0],
                "centered_top_over_sqrt": centered_top[1] / sqrt_s
                if sqrt_s
                else 0.0,
                "centered_l2_over_sqrt": centered_l2 / sqrt_s if sqrt_s else 0.0,
                **energy,
            }
        )
        previous_wheel = wheel

    return {
        "p": p,
        "side": side,
        "skeleton_count": skeleton,
        "positive_bucket_l1_over_sqrt": l1_value,
        "positive_bucket_l2_over_sqrt": l2_value,
        "positive_bucket_effective_dimension": effective_dimension,
        "danger_l1_l2_6_5": l1_value >= L1_DANGER and l2_value > L2_ENERGY,
        "danger_l1_l2_cauchy": l1_value >= L1_DANGER and l2_value > L2_CAUCHY,
        "wheels": wheel_rows,
    }


def compact_record(record: dict, wheel: int) -> dict:
    """压缩单条记录。"""
    wheel_row = next(row for row in record["wheels"] if row["wheel"] == wheel)
    return {
        "p": record["p"],
        "side": record["side"],
        "positive_bucket_l1_over_sqrt": record["positive_bucket_l1_over_sqrt"],
        "positive_bucket_l2_over_sqrt": record["positive_bucket_l2_over_sqrt"],
        "positive_bucket_effective_dimension": record[
            "positive_bucket_effective_dimension"
        ],
        **wheel_row,
    }


def summarize_wheel(records: list[dict], wheel: int) -> dict:
    """汇总单层新增能量。"""
    rows = [compact_record(record, wheel) for record in records]
    transition_rows = [row for row in rows if row["previous_wheel"] is not None]
    high_l1 = [
        row for row in rows if row["positive_bucket_l1_over_sqrt"] >= L1_DANGER
    ]
    high_l2 = [
        row for row in rows if row["positive_bucket_l2_over_sqrt"] > L2_CAUCHY
    ]
    share_key = lambda row: row["newlayer_energy_share"]
    peak_key = lambda row: row["centered_top_over_sqrt"]
    return {
        "wheel": wheel,
        "transition": bool(transition_rows),
        "max_centered_top_over_sqrt": peak_key(max(rows, key=peak_key)),
        "max_centered_top_record": max(rows, key=peak_key),
        "high_l1_count": len(high_l1),
        "high_l1_max_centered_top": max([peak_key(row) for row in high_l1] or [0.0]),
        "high_l2_count": len(high_l2),
        "high_l2_max_centered_top": max([peak_key(row) for row in high_l2] or [0.0]),
        "top_by_centered_peak": sorted(rows, key=peak_key, reverse=True)[:8],
        "top_by_l1": sorted(
            rows, key=lambda row: -row["positive_bucket_l1_over_sqrt"]
        )[:8],
        "top_by_l2": sorted(
            rows, key=lambda row: -row["positive_bucket_l2_over_sqrt"]
        )[:8],
        "newlayer_summary": None
        if not transition_rows
        else {
            "min_share": min(share_key(row) for row in transition_rows),
            "max_share": max(share_key(row) for row in transition_rows),
            "avg_share": sum(share_key(row) for row in transition_rows)
            / len(transition_rows),
            "share_ge_0_50_count": sum(
                1 for row in transition_rows if share_key(row) >= 0.50
            ),
            "share_ge_0_75_count": sum(
                1 for row in transition_rows if share_key(row) >= 0.75
            ),
            "high_l1_max_share": max(
                [
                    share_key(row)
                    for row in transition_rows
                    if row["positive_bucket_l1_over_sqrt"] >= L1_DANGER
                ]
                or [0.0]
            ),
            "high_l2_max_share": max(
                [
                    share_key(row)
                    for row in transition_rows
                    if row["positive_bucket_l2_over_sqrt"] > L2_CAUCHY
                ]
                or [0.0]
            ),
            "top_by_newlayer_share": sorted(
                transition_rows, key=share_key, reverse=True
            )[:8],
        },
    }


def summarize(records: list[dict], threshold: int, wheels: list[int]) -> dict:
    """汇总某个 P 下界以上的记录。"""
    rows = [record for record in records if record["p"] >= threshold]
    return {
        "threshold": threshold,
        "record_count": len(rows),
        "danger_l1_l2_6_5_count": sum(row["danger_l1_l2_6_5"] for row in rows),
        "danger_l1_l2_cauchy_count": sum(row["danger_l1_l2_cauchy"] for row in rows),
        "wheels": [summarize_wheel(rows, wheel) for wheel in wheels],
    }


def audit(max_p: int, alpha: float, thresholds: list[int], wheels: list[int]) -> dict:
    """执行新增层能量扫描。"""
    primes = primes_from_flags(sieve_bool(max_p))
    p_values = [p for p in primes if p >= 13]
    unit_tables = {wheel: units_mod(wheel) for wheel in wheels}
    records = []
    for p in p_values:
        for side in ("minus", "plus"):
            records.append(audit_record(p, side, alpha, primes, wheels, unit_tables))
    return {
        "parameters": {
            "max_p": max_p,
            "alpha": alpha,
            "thresholds": thresholds,
            "wheels": wheels,
            "prime_count": len(p_values),
        },
        "summaries": [summarize(records, threshold, wheels) for threshold in thresholds],
    }


def record_id(row: dict) -> str:
    """格式化记录标识。"""
    return f"P={row['p']} {row['side']}"


def fmt(value: float | int | None) -> str:
    """格式化报告字段。"""
    if value is None:
        return "-"
    if isinstance(value, int):
        return str(value)
    return f"{value:.6f}"


def write_record_table(lines: list[str], rows: list[dict], include_share: bool) -> None:
    """写记录表。"""
    if include_share:
        lines.extend(
            [
                "| record | L1 | L2 | centered peak | centered L2 | new share | new factor |",
                "|---|---:|---:|---:|---:|---:|---:|",
            ]
        )
    else:
        lines.extend(
            [
                "| record | L1 | L2 | centered peak | centered L2 |",
                "|---|---:|---:|---:|---:|",
            ]
        )
    for row in rows:
        if include_share:
            lines.append(
                f"| {record_id(row)} | "
                f"{fmt(row['positive_bucket_l1_over_sqrt'])} | "
                f"{fmt(row['positive_bucket_l2_over_sqrt'])} | "
                f"{fmt(row['centered_top_over_sqrt'])} | "
                f"{fmt(row['centered_l2_over_sqrt'])} | "
                f"{fmt(row['newlayer_energy_share'])} | "
                f"{fmt(row['new_factor'])} |"
            )
        else:
            lines.append(
                f"| {record_id(row)} | "
                f"{fmt(row['positive_bucket_l1_over_sqrt'])} | "
                f"{fmt(row['positive_bucket_l2_over_sqrt'])} | "
                f"{fmt(row['centered_top_over_sqrt'])} | "
                f"{fmt(row['centered_l2_over_sqrt'])} |"
            )


def write_markdown(result: dict, path: Path) -> None:
    """写 Markdown 报告。"""
    params = result["parameters"]
    lines = [
        "# DPRC 新增轮层 Fourier 能量扫描",
        "",
        "**状态：** `newlayer_energy_scan_not_a_proof`",
        "",
        "## 参数",
        "",
        f"- `max_p`: `{params['max_p']}`",
        f"- `alpha`: `{params['alpha']}`",
        f"- `thresholds`: `{params['thresholds']}`",
        f"- `wheels`: `{params['wheels']}`",
        f"- `prime_count`: `{params['prime_count']}`",
        "",
    ]
    for summary in result["summaries"]:
        lines.extend(
            [
                f"## P>={summary['threshold']}",
                "",
                f"- `record_count`: `{summary['record_count']}`",
                f"- `danger_l1_l2_6_5_count`: `{summary['danger_l1_l2_6_5_count']}`",
                f"- `danger_l1_l2_cauchy_count`: `{summary['danger_l1_l2_cauchy_count']}`",
                "",
            ]
        )
        for wheel_summary in summary["wheels"]:
            include_share = wheel_summary["transition"]
            lines.extend(
                [
                    f"### W={wheel_summary['wheel']}",
                    "",
                    f"- `max_centered_top_over_sqrt`: `{wheel_summary['max_centered_top_over_sqrt']:.6f}`",
                    f"- `high_l1_count`: `{wheel_summary['high_l1_count']}`",
                    f"- `high_l1_max_centered_top`: `{wheel_summary['high_l1_max_centered_top']:.6f}`",
                    f"- `high_l2_count`: `{wheel_summary['high_l2_count']}`",
                    f"- `high_l2_max_centered_top`: `{wheel_summary['high_l2_max_centered_top']:.6f}`",
                ]
            )
            if wheel_summary["newlayer_summary"]:
                nl = wheel_summary["newlayer_summary"]
                lines.extend(
                    [
                        f"- `newlayer share min/avg/max`: `{nl['min_share']:.6f}/{nl['avg_share']:.6f}/{nl['max_share']:.6f}`",
                        f"- `newlayer share >=0.50`: `{nl['share_ge_0_50_count']}`",
                        f"- `newlayer share >=0.75`: `{nl['share_ge_0_75_count']}`",
                        f"- `high_l1_max_share`: `{nl['high_l1_max_share']:.6f}`",
                        f"- `high_l2_max_share`: `{nl['high_l2_max_share']:.6f}`",
                    ]
                )
            lines.extend(["", "Top by centered peak:", ""])
            write_record_table(lines, wheel_summary["top_by_centered_peak"], include_share)
            lines.extend(["", "Top by L1:", ""])
            write_record_table(lines, wheel_summary["top_by_l1"], include_share)
            lines.extend(["", "Top by L2:", ""])
            write_record_table(lines, wheel_summary["top_by_l2"], include_share)
            if wheel_summary["newlayer_summary"]:
                lines.extend(["", "Top by new-layer share:", ""])
                write_record_table(
                    lines,
                    wheel_summary["newlayer_summary"]["top_by_newlayer_share"],
                    True,
                )
            lines.append("")
    lines.extend(
        [
            "## 结构解释",
            "",
            "对 `W_prev -> W`，新增素因子为 `r=W/W_prev`。Fourier 频率中 `r|h` 的部分是旧轮继承；`r∤h` 的部分是新增层。若新增层能量很高但 centered peak 不与 BES 高 L1/L2 同步，则它只是层级相位振荡，不足以支付零行覆盖压力。若同步发生，则进入 `new-layer W-unit PDEC`。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_ints(raw: str) -> list[int]:
    """解析逗号分隔整数。"""
    return [int(item) for item in raw.split(",") if item.strip()]


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-p", type=int, default=100000)
    parser.add_argument("--alpha", type=float, default=0.43)
    parser.add_argument("--thresholds", default="2003,10007")
    parser.add_argument("--wheels", default="30,210,2310")
    parser.add_argument(
        "--out-prefix",
        default="docs/dprc_newlayer_energy_scan_p100000_20260506",
    )
    args = parser.parse_args()
    result = audit(
        args.max_p,
        args.alpha,
        parse_ints(args.thresholds),
        parse_ints(args.wheels),
    )
    prefix = Path(args.out_prefix)
    prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, prefix.with_suffix(".md"))
    print(json.dumps(result["parameters"], ensure_ascii=False, indent=2), flush=True)


if __name__ == "__main__":
    main()
