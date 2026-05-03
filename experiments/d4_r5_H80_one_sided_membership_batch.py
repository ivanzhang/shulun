#!/usr/bin/env python3
"""H80 关键行左右半单元固定成员层泛函根证书。"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path


def parse_xs(raw: str) -> list[int]:
    """解析逗号分隔整数。"""
    return [int(item.strip()) for item in raw.split(",") if item.strip()]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--xs", default="1088475,1088496,1088506,1088551")
    parser.add_argument("--samples", type=int, default=32)
    parser.add_argument("--out-dir", type=Path, default=Path("docs/d4-r5-fixed-membership-H80-one-sided"))
    parser.add_argument("--json", type=Path, default=Path("docs/d4-r5-H80-one-sided-fixed-membership-batch.json"))
    args = parser.parse_args()

    args.out_dir.mkdir(parents=True, exist_ok=True)
    rows = []
    for x in parse_xs(args.xs):
        side_specs = [
            ("left", x - 0.5, x),
            ("right", x, x + 0.5),
        ]
        side_rows = []
        for side, left, right in side_specs:
            out = args.out_dir / f"x{x}-{side}.json"
            cmd = [
                sys.executable,
                "experiments/d4_r5_fixed_membership_functional_roots.py",
                "--x", str(x),
                "--cell-left", str(left),
                "--cell-right", str(right),
                "--samples", str(args.samples),
                "--json", str(out),
            ]
            subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL)
            data = json.loads(out.read_text())
            side_rows.append(
                {
                    "side": side,
                    "cell": [left, right],
                    "certificate": str(out),
                    "ok": data["all_functional_root_ledgers_ok"],
                    "total_root_boxes": data["total_root_boxes"],
                    "total_unresolved": data["total_unresolved"],
                    "membership_group_counts": data["membership_group_counts"],
                }
            )
        rows.append({"x": x, "sides": side_rows, "ok": all(side["ok"] for side in side_rows)})
    payload = {
        "certificate_type": "D4-R5-H80-one-sided-fixed-membership-root-batch",
        "status": "one-sided half-cell prototype around integer phase-boundary witnesses",
        "samples": args.samples,
        "rows": rows,
        "all_ok": all(row["ok"] for row in rows),
        "total_root_boxes": sum(side["total_root_boxes"] for row in rows for side in row["sides"]),
        "total_unresolved": sum(side["total_unresolved"] for row in rows for side in row["sides"]),
    }
    print(json.dumps({k: v for k, v in payload.items() if k != "rows"}, ensure_ascii=False, indent=2))
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
