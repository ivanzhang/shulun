#!/usr/bin/env python3
"""扫描 D4 旧区块证书的比例核心/顶层尾带分解。

用法示例：
  python3 experiments/d4_core_tail_theta_scan.py \
    --starts 1000000:1300000:10000 --thetas 0.8,0.9,0.95
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path


def parse_range(spec: str) -> list[int]:
    """解析 start:end:step 形式的整数区间。"""
    start, end, step = (int(part) for part in spec.split(":"))
    return list(range(start, end, step))


def ensure_old_certificate(start: int, width: int, block: int, q: float) -> Path:
    """确保旧区块证书存在，优先复用 /tmp 缓存。"""
    end = start + width
    cache = Path(f"/tmp/d4_recursion_batch/old_{start}_{end}.json")
    if cache.exists():
        return cache
    cache.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [
            sys.executable,
            "experiments/d4_block_contract_certificate.py",
            "--start",
            str(start),
            "--end",
            str(end),
            "--block",
            str(block),
            "--q",
            str(q),
            "--json",
            str(cache),
        ],
        check=True,
        stdout=subprocess.DEVNULL,
    )
    return cache


def positive_contract(row: dict) -> float:
    """只统计块正峰包络贡献。"""
    return max(0.0, float(row["max_contract"]))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--starts", default="1000000:1300000:10000")
    parser.add_argument("--width", type=int, default=10_000)
    parser.add_argument("--block", type=int, default=200)
    parser.add_argument("--q", type=float, default=0.91)
    parser.add_argument("--thetas", default="0.7,0.75,0.8,0.85,0.9,0.95")
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()

    starts = parse_range(args.starts)
    thetas = [float(item) for item in args.thetas.split(",")]
    summaries = []
    for theta in thetas:
        worst = {"tail": -1.0}
        tails = []
        intervals = []
        for start in starts:
            path = ensure_old_certificate(start, args.width, args.block, args.q)
            data = json.loads(path.read_text())
            rows = data["rows"]
            sqrt_hi = rows[-1]["hi"]
            cutoff = theta * sqrt_hi
            core = sum(positive_contract(row) for row in rows if row["lo"] <= cutoff)
            tail = sum(positive_contract(row) for row in rows if row["lo"] > cutoff)
            total = core + tail
            tails.append(tail)
            intervals.append(
                {
                    "start": start,
                    "end": start + args.width,
                    "sqrt_hi": sqrt_hi,
                    "cutoff": cutoff,
                    "core": core,
                    "tail": tail,
                    "total": total,
                    "tail_ratio": tail / total if total else 0.0,
                }
            )
            if tail > worst["tail"]:
                worst = {
                    "start": start,
                    "end": start + args.width,
                    "sqrt_hi": sqrt_hi,
                    "cutoff": cutoff,
                    "core": core,
                    "tail": tail,
                    "total": total,
                    "tail_ratio": tail / total if total else 0.0,
                }
        summary = {
            "theta": theta,
            "worst": worst,
            "mean_tail": sum(tails) / len(tails),
            "max_tail": max(tails),
            "max_core_jump": max(
                (
                    intervals[index + 1]["core"] - intervals[index]["core"]
                    for index in range(len(intervals) - 1)
                ),
                default=0.0,
            ),
            "min_core_jump": min(
                (
                    intervals[index + 1]["core"] - intervals[index]["core"]
                    for index in range(len(intervals) - 1)
                ),
                default=0.0,
            ),
            "intervals": intervals,
        }
        summaries.append(summary)
        print(
            f"theta={theta:.2f} max_tail={summary['max_tail']:.12f} "
            f"mean_tail={summary['mean_tail']:.12f} worst={worst}"
        )

    payload = {
        "starts": args.starts,
        "width": args.width,
        "block": args.block,
        "q": args.q,
        "summaries": summaries,
    }
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
