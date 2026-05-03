#!/usr/bin/env python3
"""批量生成 D4 相关和短区间端点证书。"""
from __future__ import annotations

import argparse
import csv
import json
import subprocess
import sys
from pathlib import Path


def run_one(start: int, end: int, block: int) -> dict[str, float | int]:
    tmp = Path(f"/tmp/d4_corr_block_{start}_{end}_{block}.json")
    cmd = [
        sys.executable,
        "experiments/d4_corr_block_certificate.py",
        "--start",
        str(start),
        "--end",
        str(end),
        "--block",
        str(block),
        "--endpoint",
        "--json",
        str(tmp),
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL)
    data = json.loads(tmp.read_text())
    return {
        "start": start,
        "end": end,
        "block": block,
        "bound_norm": data["prototype_bound_norm"],
        "sample_norm": data["sample_exact_best_norm"],
        "sample_x": data["sample_exact_best_x"],
        "blocks": len(data["blocks"]),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--start", type=int, default=1_000_000)
    parser.add_argument("--end", type=int, default=1_100_000)
    parser.add_argument("--width", type=int, default=10_000)
    parser.add_argument("--block", type=int, default=200)
    parser.add_argument("--csv", type=Path, required=True)
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()

    rows = []
    current = args.start
    while current < args.end:
        next_end = min(args.end, current + args.width)
        row = run_one(current, next_end, args.block)
        rows.append(row)
        print(
            f"[{current},{next_end}] bound={row['bound_norm']:.9f} "
            f"sample={row['sample_norm']:.9f} sample_x={row['sample_x']}"
        )
        current = next_end

    args.csv.parent.mkdir(parents=True, exist_ok=True)
    with args.csv.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["start", "end", "block", "bound_norm", "sample_norm", "sample_x", "blocks"])
        writer.writeheader()
        writer.writerows(rows)
    if args.json is not None:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps({"rows": rows}, ensure_ascii=False, indent=2))
    print(f"SUMMARY rows={len(rows)} max_bound={max(r['bound_norm'] for r in rows):.9f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
