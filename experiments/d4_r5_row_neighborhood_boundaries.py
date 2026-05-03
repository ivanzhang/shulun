#!/usr/bin/env python3
"""D4/R5 行邻域固定成员边界候选。

给定整数行 x，输出围绕 x 的最近连续相位边界。
这些边界由 a*m、a*m/2、整数点构成，是固定 floor/相位模板的候选邻域。
"""
from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from pathlib import Path


def rational_boundaries_around(x: int, hi: int, radius: float) -> list[Fraction]:
    """收集 [x-radius,x+radius] 内的有理相位边界。"""
    left = Fraction(math.floor((x - radius) * 2), 2)
    right = Fraction(math.ceil((x + radius) * 2), 2)
    bounds: set[Fraction] = {Fraction(n, 1) for n in range(math.floor(float(left)), math.ceil(float(right)) + 1)}
    for a in range(1, hi + 1):
        aa = Fraction(a * a, 1)
        if left <= aa <= right:
            bounds.add(aa)
        for factor in (1, 2):
            lo_m = math.floor(float(left) * factor / a) - 2
            hi_m = math.ceil(float(right) * factor / a) + 2
            for m in range(max(1, lo_m), hi_m + 1):
                value = Fraction(a * m, factor)
                if left <= value <= right:
                    bounds.add(value)
    return sorted(bounds)


def cell_containing_x(x: int, boundaries: list[Fraction]) -> dict:
    """返回包含 x 的左右开单元；若 x 是边界，给出左右邻域。"""
    fx = Fraction(x, 1)
    idx = boundaries.index(fx) if fx in boundaries else None
    if idx is None:
        for i, (a, b) in enumerate(zip(boundaries, boundaries[1:])):
            if a < fx < b:
                return {"mode": "interior", "cell": [str(a), str(b)], "width": float(b - a)}
        raise ValueError("x not covered")
    left_cell = None if idx == 0 else [str(boundaries[idx - 1]), str(boundaries[idx])]
    right_cell = None if idx + 1 >= len(boundaries) else [str(boundaries[idx]), str(boundaries[idx + 1])]
    return {
        "mode": "boundary",
        "left_cell": left_cell,
        "right_cell": right_cell,
        "left_width": None if left_cell is None else float(boundaries[idx] - boundaries[idx - 1]),
        "right_width": None if right_cell is None else float(boundaries[idx + 1] - boundaries[idx]),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--xs", default="1088475,1088496,1088506,1088551")
    parser.add_argument("--hi", type=int, default=400)
    parser.add_argument("--radius", type=float, default=1.0)
    parser.add_argument("--json", type=Path, default=Path("docs/d4-r5-H80-row-neighborhood-boundaries.json"))
    args = parser.parse_args()

    rows = []
    for x in [int(item) for item in args.xs.split(",") if item.strip()]:
        boundaries = rational_boundaries_around(x, args.hi, args.radius)
        around = [b for b in boundaries if Fraction(x - 1, 1) <= b <= Fraction(x + 1, 1)]
        rows.append(
            {
                "x": x,
                "boundary_count_radius": len(boundaries),
                "local_boundaries": [str(b) for b in around],
                "cell_containing_x": cell_containing_x(x, boundaries),
            }
        )
    payload = {
        "certificate_type": "D4-R5-row-neighborhood-rational-boundaries",
        "status": "rational phase-boundary prototype for exact fixed-membership cells",
        "hi": args.hi,
        "radius": args.radius,
        "rows": rows,
        "interpretation": "Integer witnesses sit on rational phase boundaries; final proof should certify both one-sided cells adjacent to each witness.",
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
