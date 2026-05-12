#!/usr/bin/env python3
"""分段补齐 strict table_012 theta 极值完整归档。

用法示例：
  g++ -O3 -std=c++17 -Wall -Wextra -o /tmp/table012_theta_extremal \
    experiments/prime_matrix_table012_theta_extremal_runner.cpp

  python3 experiments/prime_matrix_table012_segmented_completion_driver.py \
    --archive data/theta-table012-extremal-archive.jsonl \
    --runner /tmp/table012_theta_extremal \
    --segment-width 1000000000 \
    --chunk-width 256000000
"""

from __future__ import annotations

import argparse
import json
import math
import subprocess
import sys
from decimal import Decimal, getcontext
from pathlib import Path
from typing import Any


getcontext().prec = 80

TABLE012 = [
    ("1E+08", 100_000_000, 200_000_000, Decimal("-0.00044")),
    ("2E+08", 200_000_000, 300_000_000, Decimal("-0.00065")),
    ("3E+08", 300_000_000, 400_000_000, Decimal("-0.00057")),
    ("4E+08", 400_000_000, 500_000_000, Decimal("-0.00049")),
    ("5E+08", 500_000_000, 600_000_000, Decimal("-0.00052")),
    ("6E+08", 600_000_000, 700_000_000, Decimal("-0.00038")),
    ("7E+08", 700_000_000, 800_000_000, Decimal("-0.00051")),
    ("8E+08", 800_000_000, 900_000_000, Decimal("-0.00044")),
    ("9E+08", 900_000_000, 1_000_000_000, Decimal("-0.00050")),
    ("1E+09", 1_000_000_000, 2_000_000_000, Decimal("-0.00021")),
    ("2E+09", 2_000_000_000, 3_000_000_000, Decimal("-0.00018")),
    ("3E+09", 3_000_000_000, 4_000_000_000, Decimal("-0.00015")),
    ("4E+09", 4_000_000_000, 5_000_000_000, Decimal("-0.00017")),
    ("5E+09", 5_000_000_000, 6_000_000_000, Decimal("-0.00018")),
    ("6E+09", 6_000_000_000, 7_000_000_000, Decimal("-0.00013")),
    ("7E+09", 7_000_000_000, 8_000_000_000, Decimal("-0.00018")),
    ("8E+09", 8_000_000_000, 9_000_000_000, Decimal("-0.00016")),
    ("9E+09", 9_000_000_000, 10_000_000_000, Decimal("-0.00010")),
    ("1E+10", 10_000_000_000, 20_000_000_000, Decimal("-0.00008")),
    ("2E+10", 20_000_000_000, 30_000_000_000, Decimal("-0.00006")),
    ("3E+10", 30_000_000_000, 40_000_000_000, Decimal("-0.00005")),
    ("4E+10", 40_000_000_000, 50_000_000_000, Decimal("-0.00007")),
    ("5E+10", 50_000_000_000, 60_000_000_000, Decimal("-0.00004")),
    ("6E+10", 60_000_000_000, 70_000_000_000, Decimal("-0.00006")),
    ("7E+10", 70_000_000_000, 80_000_000_000, Decimal("-0.00004")),
    ("8E+10", 80_000_000_000, 90_000_000_000, Decimal("-0.00006")),
    ("9E+10", 90_000_000_000, 100_000_000_000, Decimal("-0.00004")),
    ("1E+11", 100_000_000_000, 200_000_000_000, Decimal("-0.00002")),
    ("2E+11", 200_000_000_000, 300_000_000_000, Decimal("-0.00002")),
    ("3E+11", 300_000_000_000, 400_000_000_000, Decimal("-0.00001")),
    ("4E+11", 400_000_000_000, 500_000_000_000, Decimal("-0.00002")),
    ("5E+11", 500_000_000_000, 600_000_000_000, Decimal("-0.00001")),
    ("6E+11", 600_000_000_000, 700_000_000_000, Decimal("-0.00002")),
    ("7E+11", 700_000_000_000, 800_000_000_000, Decimal("-0.00001")),
]


def load_rows(path: Path) -> list[dict[str, Any]]:
    """读取已有完整行归档。"""
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def load_segment_ledger(path: Path) -> dict[tuple[int, int, int], dict[str, Any]]:
    """读取已完成的子区间证书，供中断后复用。"""
    if not path.exists():
        return {}
    segments: dict[tuple[int, int, int], dict[str, Any]] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        item = json.loads(line)
        key = (int(item["row_index"]), int(item["segment_left"]), int(item["segment_right"]))
        segments[key] = item
    return segments


def dec(value: Any) -> Decimal:
    """统一转 Decimal。"""
    return Decimal(str(value))


def sci(value: Decimal) -> str:
    """输出稳定科学计数法字符串。"""
    return f"{value:.21E}".replace("E", "e")


def derivative_lower_bound(left: int, right: int, b1: Decimal) -> str:
    """登记右侧函数导数的粗下界。"""
    best = min(
        1.0 + float(b1) * (math.log(float(x)) - 1.0) / (math.log(float(x)) ** 2)
        for x in (left, right)
    )
    return f"{best:.21e}"


def validate_prefix(rows: list[dict[str, Any]]) -> None:
    """确认已有前缀与 table_012 顺序一致。"""
    for idx, row in enumerate(rows):
        label, left, right, b1 = TABLE012[idx]
        if row.get("label") != label or row.get("left") != left or row.get("right") != right:
            raise SystemExit(f"archive prefix mismatch at row {idx}: {row.get('label')}")
        if dec(row.get("b1")) != b1:
            raise SystemExit(f"archive b1 mismatch at row {idx}: {row.get('b1')}")
        if row.get("passed_with_guard") is not True:
            raise SystemExit(f"archive prefix row {idx} is not passed")


def run_segment(
    runner: Path,
    row_index: int,
    seg_left: int,
    seg_right: int,
    theta: str,
    prime_count: int,
    chunk_width: int,
) -> dict[str, Any]:
    """调用 C++ runner 扫描一个子区间。"""
    command = [
        str(runner),
        "--start-index",
        str(row_index),
        "--initial-theta",
        theta,
        "--initial-prime-count",
        str(prime_count),
        "--max-rows",
        str(len(TABLE012)),
        "--segment-left",
        str(seg_left),
        "--segment-right",
        str(seg_right),
        "--chunk-width",
        str(chunk_width),
    ]
    completed = subprocess.run(command, check=True, text=True, capture_output=True)
    if completed.stderr.strip():
        print(completed.stderr.strip(), file=sys.stderr, flush=True)
    lines = [line for line in completed.stdout.splitlines() if line.strip()]
    if len(lines) != 1:
        raise SystemExit(f"segment runner returned {len(lines)} JSON lines")
    return json.loads(lines[0])


def combine_row(row_index: int, segments: list[dict[str, Any]]) -> dict[str, Any]:
    """把多个子区间证书合并成原始完整行证书。"""
    label, left, right, b1 = TABLE012[row_index]
    best = max(segments, key=lambda item: dec(item["max_defect"]))
    last = segments[-1]
    global_prime_count = int(last["global_prime_count"])
    row_prime_count = sum(int(item["segment_prime_count"]) for item in segments)
    max_defect = dec(best["max_defect"])
    error_bound = Decimal("1") + Decimal("1e-12") * Decimal(global_prime_count)
    margin_after_guard = -(max_defect + error_bound)
    raw_margin = -max_defect
    b1_margin = b1 - dec(best["max_required_b1"])

    return {
        "label": label,
        "left": left,
        "right": right,
        "b1": str(b1),
        "row_prime_count": row_prime_count,
        "global_prime_count": global_prime_count,
        "theta_at_right": last["theta_at_right"],
        "max_defect": sci(max_defect),
        "numeric_error_bound": sci(error_bound),
        "margin_after_guard": sci(margin_after_guard),
        "raw_margin": sci(raw_margin),
        "max_x": int(best["max_x"]),
        "max_kind": best["max_kind"],
        "max_required_b1": best["max_required_b1"],
        "b1_minus_max_required_b1": sci(b1_margin),
        "rhs_derivative_lower_bound": derivative_lower_bound(left, right, b1),
        "passed_raw": max_defect < 0,
        "passed_with_guard": margin_after_guard > 0,
    }


def append_row(path: Path, row: dict[str, Any]) -> None:
    """追加一行完整归档。"""
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n")
        handle.flush()


def append_segment(path: Path, segment: dict[str, Any]) -> None:
    """追加一个子区间证书，保证中断后可复用。"""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(segment, ensure_ascii=False, separators=(",", ":")) + "\n")
        handle.flush()


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--archive", type=Path, required=True)
    parser.add_argument("--segment-ledger", type=Path, default=Path("data/theta-table012-extremal-segments.jsonl"))
    parser.add_argument("--runner", type=Path, default=Path("/tmp/table012_theta_extremal"))
    parser.add_argument("--segment-width", type=int, default=1_000_000_000)
    parser.add_argument("--chunk-width", type=int, default=256_000_000)
    parser.add_argument("--suppress-reused", action="store_true", help="不打印已复用子段，只打印新完成子段")
    args = parser.parse_args()

    rows = load_rows(args.archive)
    validate_prefix(rows)
    completed_segments = load_segment_ledger(args.segment_ledger)
    if len(rows) >= len(TABLE012):
        print("archive already complete", flush=True)
        return
    if not rows:
        raise SystemExit("driver requires an existing prefix ending at theta(1e8) or later")

    theta = str(rows[-1]["theta_at_right"])
    prime_count = int(rows[-1]["global_prime_count"])
    start_index = len(rows)
    print(f"resume_from_rows={start_index} theta={theta} prime_count={prime_count}", flush=True)

    for row_index in range(start_index, len(TABLE012)):
        label, left, right, _b1 = TABLE012[row_index]
        segments: list[dict[str, Any]] = []
        seg_left = left
        print(f"row_start index={row_index} label={label} range=[{left},{right}]", flush=True)
        while seg_left < right:
            seg_right = min(right, seg_left + args.segment_width)
            segment_key = (row_index, seg_left, seg_right)
            if segment_key in completed_segments:
                segment = completed_segments[segment_key]
                if not args.suppress_reused:
                    print(
                        "segment_reused "
                        f"row={label} segment=[{seg_left},{seg_right}] "
                        f"passed={segment['passed_with_guard']} "
                        f"max_defect={segment['max_defect']}",
                        flush=True,
                    )
            else:
                segment = run_segment(
                    args.runner,
                    row_index,
                    seg_left,
                    seg_right,
                    theta,
                    prime_count,
                    args.chunk_width,
                )
                append_segment(args.segment_ledger, segment)
                completed_segments[segment_key] = segment
                print(
                    "segment_done "
                    f"row={label} segment=[{seg_left},{seg_right}] "
                    f"passed={segment['passed_with_guard']} "
                    f"max_defect={segment['max_defect']}",
                    flush=True,
                )
            segments.append(segment)
            theta = str(segment["theta_at_right"])
            prime_count = int(segment["global_prime_count"])
            seg_left = seg_right

        row = combine_row(row_index, segments)
        append_row(args.archive, row)
        print(
            "row_done "
            f"index={row_index} label={label} passed={row['passed_with_guard']} "
            f"raw_margin={row['raw_margin']} guard_margin={row['margin_after_guard']}",
            flush=True,
        )


if __name__ == "__main__":
    main()
