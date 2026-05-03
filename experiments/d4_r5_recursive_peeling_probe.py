#!/usr/bin/env python3
"""D4/R5 递归剥离数值探针。

比较不同 hi 壳层截断下 R5 层泛函的变化，观察坏度是回传还是由新壳层耗散。
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import d4_r5_layer_functional_certificate as layer_cert  # noqa: E402


def row_at_hi(x: int, hi: int, args, tau, prefix) -> dict:
    """给定 hi 的层统计。"""
    s = layer_cert.layer_summary_for_x(x, hi, args.q, args.threshold_tau, args.H, tau, prefix)
    return {k: s[k] for k in ["x", "U", "V", "light_L", "L", "E2", "potential", "short_L", "transition_L"]}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--xs", default="1088373,1088475,1088588")
    parser.add_argument("--his", default="80,120,160,200,240,280,320,360,400")
    parser.add_argument("--H", type=int, default=80)
    parser.add_argument("--q", type=float, default=0.958)
    parser.add_argument("--threshold-tau", type=int, default=60)
    parser.add_argument("--json", type=Path, default=Path("docs/d4-r5-recursive-peeling-probe.json"))
    args = parser.parse_args()
    xs = [int(item) for item in args.xs.split(",") if item]
    his = [int(item) for item in args.his.split(",") if item]
    tau, prefix = layer_cert.build(2 * (max(xs) + 10))
    rows = []
    for x in xs:
        stats = [row_at_hi(x, hi, args, tau, prefix) | {"hi": hi} for hi in his]
        deltas = []
        for prev, cur in zip(stats, stats[1:]):
            deltas.append(
                {
                    "from_hi": prev["hi"],
                    "to_hi": cur["hi"],
                    "dL": cur["L"] - prev["L"],
                    "dE2": cur["E2"] - prev["E2"],
                    "dPotential": cur["potential"] - prev["potential"],
                    "new_shell_defect": (cur["E2"] - prev["E2"]) - ((cur["L"] - prev["L"]) ** 2) / 20 if cur["L"] != prev["L"] else cur["E2"] - prev["E2"],
                }
            )
        rows.append({"x": x, "stats": stats, "deltas": deltas})
    payload = {
        "certificate_type": "D4-R5-recursive-peeling-probe",
        "status": "numerical shell peeling probe; suggests variables for RPL, not a proof",
        "xs": xs,
        "his": his,
        "rows": rows,
    }
    print(json.dumps({"certificate_type": payload["certificate_type"], "xs": xs, "his": his}, ensure_ascii=False, indent=2))
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
