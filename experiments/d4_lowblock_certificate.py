#!/usr/bin/env python3
"""D4 R5 低块 a<=A 的块化正峰证书。

用法示例：
  python3 experiments/d4_lowblock_certificate.py \
    --start 1000000 --end 20000000 --width 10000 --q 0.958 --amax 400 \
    --json docs/d4-r5-lowblock-certificate-q958.json
"""
from __future__ import annotations

import argparse
import json
import math
import subprocess
import sys
from pathlib import Path


def run_block(start: int, end: int, block: int, q: float) -> dict:
    """运行已有块证书脚本并返回 JSON。"""
    path = Path(f"/tmp/d4_lowblock_{start}_{end}_b{block}_q{q}.json")
    if not path.exists():
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
                str(path),
            ],
            check=True,
            stdout=subprocess.DEVNULL,
        )
    return json.loads(path.read_text())


def positive(value: float) -> float:
    """只取正峰贡献。"""
    return max(0.0, value)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", type=int, default=1_000_000)
    parser.add_argument("--end", type=int, default=20_000_000)
    parser.add_argument("--width", type=int, default=10_000)
    parser.add_argument("--block", type=int, default=200)
    parser.add_argument("--q", type=float, default=0.958)
    parser.add_argument("--amax", type=int, default=400)
    parser.add_argument("--envelope-k", type=float, default=0.71)
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()

    rows = []
    global_positive_blocks = []
    cursor = args.start
    while cursor < args.end:
        interval_end = min(args.end, cursor + args.width)
        data = run_block(cursor, interval_end, args.block, args.q)
        low_rows = [row for row in data["rows"] if row["hi"] <= args.amax]
        positive_rows = [
            {
                "lo": row["lo"],
                "hi": row["hi"],
                "x": row["x"],
                "positive_contract": positive(row["max_contract"]),
                "max_contract": row["max_contract"],
                "c_norm": row["c_norm"],
                "old_norm": row["old_norm"],
                "critical_roots": row["critical_roots"],
                "total_candidates": row["total_candidates"],
            }
            for row in low_rows
            if positive(row["max_contract"]) > 0.0
        ]
        low = sum(row["positive_contract"] for row in positive_rows)
        for row in positive_rows:
            global_positive_blocks.append({"start": cursor, "end": interval_end, **row})
        envelope = args.envelope_k * (cursor ** -0.25) * math.log(cursor)
        rows.append(
            {
                "start": cursor,
                "end": interval_end,
                "lowblock": low,
                "envelope": envelope,
                "margin": envelope - low,
                "ratio": low / envelope if envelope else 0.0,
                "positive_block_count": len(positive_rows),
                "top_positive_blocks": sorted(
                    positive_rows,
                    key=lambda row: row["positive_contract"],
                    reverse=True,
                )[:5],
                "lowblock_critical_roots": sum(row["critical_roots"] for row in low_rows),
                "lowblock_candidates": sum(row["total_candidates"] for row in low_rows),
                "total_critical_roots": data["total_critical_roots"],
                "total_candidates": data["total_candidates"],
            }
        )
        print(
            f"[{cursor},{interval_end}] low={low:.12f} "
            f"env={envelope:.12f} margin={envelope-low:.12f}"
        )
        cursor = interval_end

    worst_margin_row = min(rows, key=lambda row: row["margin"])
    worst_ratio_row = max(rows, key=lambda row: row["ratio"])
    top_global_blocks = sorted(
        global_positive_blocks,
        key=lambda row: row["positive_contract"],
        reverse=True,
    )[:20]

    payload = {
        "certificate_type": "D4-R5-lowblock-fixed-a-envelope",
        "description": "低块 a<=amax 的正峰贡献与 K X^{-1/4} log X 包络比较；top 字段用于定位有限分段证明的责任块。",
        "start": args.start,
        "end": args.end,
        "width": args.width,
        "block": args.block,
        "q": args.q,
        "amax": args.amax,
        "envelope_k": args.envelope_k,
        "min_margin": worst_margin_row["margin"],
        "max_ratio": worst_ratio_row["ratio"],
        "worst_margin_row": worst_margin_row,
        "worst_ratio_row": worst_ratio_row,
        "top_global_positive_blocks": top_global_blocks,
        "lowblock_critical_roots": sum(row["lowblock_critical_roots"] for row in rows),
        "lowblock_candidates": sum(row["lowblock_candidates"] for row in rows),
        "total_critical_roots": sum(row["total_critical_roots"] for row in rows),
        "rows": rows,
    }
    print(
        f"SUMMARY rows={len(rows)} min_margin={payload['min_margin']:.12f} "
        f"max_ratio={payload['max_ratio']:.12f}"
    )
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
