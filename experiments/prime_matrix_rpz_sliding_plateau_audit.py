#!/usr/bin/env python3
"""审计 RPZ 滑动零窗平台中的复活源多重度。

用法示例：
  python3 experiments/prime_matrix_rpz_sliding_plateau_audit.py

输入为 `prime-matrix-scaled-peeling-halfwidth-audit.json`。脚本围绕每个已知顶层零行
寻找包含原行的最大连续滑动零窗平台，并统计半宽层复活源在这些窗口中的重复出现次数。
该审计用于区分两种情况：

1. 单个窗口内吸收标签分散；
2. 滑动平台中同一复活源反复解释多个零窗，形成持久尾锚负载。
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path

from prime_matrix_rpz_absorption_defect_audit import select_absorber
from prime_matrix_scaled_peeling_halfwidth_audit import factor_with_allowed
from prime_matrix_zero_row_crt_audit import mark_old_sieve_interval, primes_upto


def is_zero_window(left: int, right: int, primes: list[int]) -> bool:
    """判断 `[left,right]` 是否在给定素数筛下无幸存者。"""
    if left < 1:
        return False
    return mark_old_sieve_interval(left, right, primes).count(1) == 0


def zero_shift_plateau(left: int, right: int, primes: list[int]) -> list[int]:
    """返回包含 `0` 的最大连续滑动零窗位移平台。"""
    if not is_zero_window(left, right, primes):
        return []

    shift_min = 0
    while is_zero_window(left + shift_min - 1, right + shift_min - 1, primes):
        shift_min -= 1

    shift_max = 0
    while is_zero_window(left + shift_max + 1, right + shift_max + 1, primes):
        shift_max += 1

    return list(range(shift_min, shift_max + 1))


def h_survivors(left: int, right: int, primes: list[int]) -> list[int]:
    """返回 `[left,right]` 中半宽筛幸存者。"""
    alive = mark_old_sieve_interval(left, right, primes)
    return [left + idx for idx, flag in enumerate(alive) if flag]


def audit_record(item: dict, all_primes: list[int], tail_threshold: int) -> dict:
    """审计单个顶层零行记录。"""
    top = item["top_prime"]
    half = item["half_prime"]
    left, right = item["top_interval"]
    top_primes = [prime for prime in all_primes if prime <= top]
    half_primes = [prime for prime in all_primes if prime <= half]
    peeled_primes = [prime for prime in all_primes if half < prime <= top]

    shifts = zero_shift_plateau(left, right, top_primes)
    source_to_shifts: dict[int, list[int]] = defaultdict(list)
    source_data: dict[int, dict] = {}
    event_label_load: Counter[int] = Counter()
    event_column_load: Counter[int] = Counter()

    for shift in shifts:
        window_left = left + shift
        window_right = right + shift
        for n in h_survivors(window_left, window_right, half_primes):
            factors = factor_with_allowed(n, peeled_primes)
            absorber = select_absorber(factors, half, top)
            source_to_shifts[n].append(shift)
            if n not in source_data:
                source_data[n] = {
                    "n": n,
                    "factors": factors,
                    "absorber": absorber,
                    "cofactor": None if absorber is None else n // absorber,
                }
            if absorber is not None:
                event_label_load[absorber] += 1
            event_column_load[n - window_left + 1] += 1

    source_label_load: Counter[int] = Counter()
    sources = []
    for n in sorted(source_to_shifts):
        data = source_data[n]
        absorber = data["absorber"]
        shifts_for_source = sorted(source_to_shifts[n])
        if absorber is not None:
            source_label_load[absorber] += 1
        sources.append(
            {
                **data,
                "shifts": shifts_for_source,
                "multiplicity": len(shifts_for_source),
                "tail_threshold_exceeded": len(shifts_for_source) > tail_threshold,
            }
        )

    max_source_multiplicity = max(
        (source["multiplicity"] for source in sources),
        default=0,
    )
    return {
        "top_prime": top,
        "top_zero_row": item["top_zero_row"],
        "top_interval": item["top_interval"],
        "half_prime": half,
        "tail_threshold": tail_threshold,
        "zero_shift_plateau": shifts,
        "zero_shift_plateau_length": len(shifts),
        "unique_resurrected_sources": len(sources),
        "absorption_events": sum(source["multiplicity"] for source in sources),
        "source_deletion_ratio": None
        if not sources
        else sum(source["multiplicity"] for source in sources) / len(sources),
        "event_label_load": dict(sorted(event_label_load.items())),
        "source_label_load": dict(sorted(source_label_load.items())),
        "max_event_label_load": max(event_label_load.values(), default=0),
        "max_source_label_load": max(source_label_load.values(), default=0),
        "max_source_multiplicity": max_source_multiplicity,
        "tailanchor_trigger_at_threshold": max_source_multiplicity > tail_threshold,
        "event_column_load": dict(sorted(event_column_load.items())),
        "max_event_column_load": max(event_column_load.values(), default=0),
        "sources": sources,
    }


def audit(source_path: Path, tail_threshold: int) -> dict:
    """执行滑动平台审计。"""
    source = json.loads(source_path.read_text(encoding="utf-8"))
    max_prime = max(record["top_prime"] for record in source["records"])
    all_primes = primes_upto(max_prime + 100)
    records = [
        audit_record(item, all_primes, tail_threshold)
        for item in source["records"]
    ]
    total_sources = sum(record["unique_resurrected_sources"] for record in records)
    total_events = sum(record["absorption_events"] for record in records)
    return {
        "status": "rpz_sliding_plateau_converts_single_window_dispersion_to_persistent_source_load",
        "source": str(source_path),
        "parameters": {
            "tail_threshold": tail_threshold,
        },
        "summary": {
            "records": len(records),
            "total_unique_resurrected_sources": total_sources,
            "total_absorption_events": total_events,
            "max_zero_shift_plateau_length": max(
                (record["zero_shift_plateau_length"] for record in records),
                default=0,
            ),
            "global_max_source_multiplicity": max(
                (record["max_source_multiplicity"] for record in records),
                default=0,
            ),
            "records_triggering_tailanchor": sum(
                1 for record in records if record["tailanchor_trigger_at_threshold"]
            ),
            "max_source_deletion_ratio": max(
                (
                    record["source_deletion_ratio"]
                    for record in records
                    if record["source_deletion_ratio"] is not None
                ),
                default=None,
            ),
        },
        "records": records,
    }


def write_markdown(result: dict, path: Path) -> None:
    """写 Markdown 审计报告。"""
    summary = result["summary"]
    tail_threshold = result["parameters"]["tail_threshold"]
    lines = [
        "# RPZ 滑动零窗平台审计",
        "",
        "**状态：** `rpz_sliding_plateau_converts_single_window_dispersion_to_persistent_source_load`",
        "",
        "## 总结",
        "",
        f"- 样本记录数：`{summary['records']}`。",
        f"- 唯一复活源总数：`{summary['total_unique_resurrected_sources']}`。",
        f"- 吸收事件总数：`{summary['total_absorption_events']}`。",
        f"- 最大滑动零窗平台长度：`{summary['max_zero_shift_plateau_length']}`。",
        f"- 最大复活源多重度：`{summary['global_max_source_multiplicity']}`。",
        f"- 阈值 `T0={tail_threshold}` 下触发 TailAnchor 的记录数：`{summary['records_triggering_tailanchor']}`。",
        f"- 最大源删除前/后事件比：`{summary['max_source_deletion_ratio']:.6f}`。",
        "",
        "## 逐例表",
        "",
        "| top P | row | half | plateau shifts | sources | events | max source mult | event label load | TailAnchor@T0 |",
        "|---:|---:|---:|---|---:|---:|---:|---|---|",
    ]
    for record in result["records"]:
        lines.append(
            "| {top} | {row} | {half} | `{shifts}` | {sources} | {events} | {mult} | `{loads}` | {tail} |".format(
                top=record["top_prime"],
                row=record["top_zero_row"],
                half=record["half_prime"],
                shifts=record["zero_shift_plateau"],
                sources=record["unique_resurrected_sources"],
                events=record["absorption_events"],
                mult=record["max_source_multiplicity"],
                loads=record["event_label_load"],
                tail="yes" if record["tailanchor_trigger_at_threshold"] else "no",
            )
        )

    lines.extend(
        [
            "",
            "## 审稿解释",
            "",
            "单个顶层零窗内的半宽复活标签可以完全分散；但若把包含该零窗的最大连续滑动零窗平台一起计数，同一个复活源会在多个窗口中重复出现。这个重复不是新的整数点，而是同一解释源对多个坏窗的持久解释。",
            "",
            "因此 `Distributed-RPZ` 必须区分两种账本约定：若按窗口事件计数，则复活源多重度立刻形成 TailAnchor 负载；若按源删除计数，则必须显式证明源删除后的剩余窗口仍满足同口径反例抽取，否则该分支只能作为 `Sparse/SAE` 型孤立逃逸。",
            "",
            "本审计不排除全局 `Distributed-RPZ`。它把下一步硬点压缩为：证明低负载分散吸收若避免持久源重复，则所有复活源必须压到滑动平台边界层；再排除这种边界压缩，或把它送入 `SAE/PDEC`。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source",
        type=Path,
        default=Path("docs/monograph/prime-matrix-scaled-peeling-halfwidth-audit.json"),
    )
    parser.add_argument(
        "--out-prefix",
        type=Path,
        default=Path("docs/monograph/prime-matrix-rpz-sliding-plateau-audit"),
    )
    parser.add_argument("--tail-threshold", type=int, default=4)
    args = parser.parse_args()
    result = audit(args.source, args.tail_threshold)
    args.out_prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.out_prefix.with_suffix(".md"))
    print(json.dumps(result["summary"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
