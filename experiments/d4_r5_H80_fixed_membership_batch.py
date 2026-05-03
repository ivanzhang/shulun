#!/usr/bin/env python3
"""批量生成 H80 关键行的固定成员层泛函根证书。"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path


def parse_xs(raw: str) -> list[int]:
    """解析逗号分隔的整数行。"""
    return [int(item.strip()) for item in raw.split(",") if item.strip()]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--xs", default="1088475,1088496,1088506,1088551")
    parser.add_argument("--H", type=int, default=80)
    parser.add_argument("--hi", type=int, default=400)
    parser.add_argument("--q", type=float, default=0.958)
    parser.add_argument("--threshold-tau", type=int, default=60)
    parser.add_argument("--samples", type=int, default=64)
    parser.add_argument("--out-dir", type=Path, default=Path("docs/d4-r5-fixed-membership-H80"))
    parser.add_argument("--json", type=Path, default=Path("docs/d4-r5-H80-fixed-membership-batch.json"))
    args = parser.parse_args()

    args.out_dir.mkdir(parents=True, exist_ok=True)
    rows = []
    for x in parse_xs(args.xs):
        out = args.out_dir / f"x{x}.json"
        cmd = [
            sys.executable,
            "experiments/d4_r5_fixed_membership_functional_roots.py",
            "--x",
            str(x),
            "--cell-left",
            str(x),
            "--cell-right",
            str(x + 1),
            "--H",
            str(args.H),
            "--hi",
            str(args.hi),
            "--q",
            str(args.q),
            "--threshold-tau",
            str(args.threshold_tau),
            "--samples",
            str(args.samples),
            "--json",
            str(out),
        ]
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL)
        data = json.loads(out.read_text())
        rows.append(
            {
                "x": x,
                "certificate": str(out),
                "ok": data["all_functional_root_ledgers_ok"],
                "total_root_boxes": data["total_root_boxes"],
                "total_unresolved": data["total_unresolved"],
                "membership_group_counts": data["membership_group_counts"],
                "functional_summary": [
                    {
                        "functional": cert["functional"],
                        "group_count": cert["group_count"],
                        "no_root_count": cert["no_root_count"],
                        "root_box_count": cert["root_box_count"],
                        "unresolved_count": cert["unresolved_count"],
                        "endpoint_values": cert["candidate_values"][:2],
                    }
                    for cert in data["certificates"]
                ],
            }
        )
    payload = {
        "certificate_type": "D4-R5-H80-fixed-membership-layer-functional-root-batch",
        "status": "prototype: key H80 witnesses only; exact membership cell generation remains",
        "H": args.H,
        "hi": args.hi,
        "q": args.q,
        "threshold_tau": args.threshold_tau,
        "samples": args.samples,
        "rows": rows,
        "all_ok": all(row["ok"] for row in rows),
        "total_root_boxes": sum(row["total_root_boxes"] for row in rows),
        "total_unresolved": sum(row["total_unresolved"] for row in rows),
    }
    print(json.dumps({k: v for k, v in payload.items() if k != "rows"}, ensure_ascii=False, indent=2))
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
