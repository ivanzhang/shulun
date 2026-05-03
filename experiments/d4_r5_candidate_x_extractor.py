#!/usr/bin/env python3
"""从 D4/R5 证书中提取当前有限证书候选 x 集合。"""
from __future__ import annotations

import json
import re
from pathlib import Path

SOURCES = [
    "docs/d4-r5-light-layer-closure-master-certificate.json",
    "docs/d4-r5-highmass-energy-master-certificate.json",
    "docs/d4-r5-tailabsent-short-light-frontier-certificate.json",
    "docs/d4-r5-light-H80-layer-functional-certificate.json",
    "docs/d4-r5-H80-membership-cell-decomposition.json",
    "docs/d4-r5-valley-fourpoint-local-table.json",
    "docs/d4-r5-valley-fourpoint-resource-lock.json",
    "docs/d4-r5-fourpoint-fixed-target-template-proof.json",
]


def collect_x(obj, xs: set[int]) -> None:
    """递归收集字段名含 x 的整数值。"""
    if isinstance(obj, dict):
        for key, value in obj.items():
            if key == "x" or key.endswith("_x") or key == "witness_x" or "x" == key.lower():
                if isinstance(value, int):
                    xs.add(value)
            collect_x(value, xs)
    elif isinstance(obj, list):
        for item in obj:
            collect_x(item, xs)


def main() -> int:
    rows = []
    all_xs: set[int] = set()
    for source in SOURCES:
        path = Path(source)
        if not path.exists():
            rows.append({"source": source, "exists": False, "xs": []})
            continue
        data = json.loads(path.read_text())
        xs: set[int] = set()
        collect_x(data, xs)
        # 只保留 R5 窗口附近候选，避免误收非行号常数。
        xs = {x for x in xs if 1_000_000 <= x <= 1_200_000}
        all_xs |= xs
        rows.append({"source": source, "exists": True, "count": len(xs), "xs": sorted(xs)})
    payload = {
        "certificate_type": "D4-R5-current-finite-certificate-candidate-x-set",
        "sources": rows,
        "candidate_xs": sorted(all_xs),
        "candidate_count": len(all_xs),
        "scope": "current finite-window/template certificate witnesses only; not a global phasecell enumeration",
    }
    Path("docs/d4-r5-current-candidate-x-set.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2))
    print(json.dumps({k: v for k, v in payload.items() if k != "sources"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
