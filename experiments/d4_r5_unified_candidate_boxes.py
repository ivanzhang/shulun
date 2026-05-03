#!/usr/bin/env python3
"""D4/R5 统一候选盒表原型。

用法示例：
  python3 experiments/d4_r5_unified_candidate_boxes.py \
    --units "1088472:1088477,1088496:1088499,1088506:1088507,1088551:1088555" \
    --H 80 --hi 400 --q 0.958 --threshold-tau 60 \
    --root-blocks "1:200,201:400" \
    --json docs/d4-r5-H80-unified-candidate-boxes.json

说明：
  合并 layer functional certificate 与 phasecell derivative/root certificate。
  当前输出的是统一证书表的最小可运行版本：整数边界候选负责层泛函查询，
  root/no-root 开区间账本负责说明尚需接入层泛函导数的地方。
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import d4_r5_layer_functional_certificate as layer_cert  # noqa: E402
import d4_r5_phasecell_root_certificate as root_cert  # noqa: E402


def parse_blocks(raw: str) -> list[tuple[int, int]]:
    """解析 lo:hi,lo:hi 块列表。"""
    blocks = []
    for item in raw.split(","):
        item = item.strip()
        if not item:
            continue
        left, right = item.split(":", 1)
        blocks.append((int(left), int(right)))
    return blocks


def root_table_for_unit(start: int, end: int, blocks: list[tuple[int, int]], q: float, tau: list[int], prefix: list[int]) -> list[dict]:
    """为一个 x 单元生成各 a 块的根盒/无根账本。"""
    tables = []
    for lo, hi in blocks:
        boundaries = root_cert.phase_boundaries(start, end, lo, hi, include_integer_grid=True)
        no_root, root_boxes = root_cert.isolate_roots(boundaries, lo, hi, tau, prefix, q)
        unresolved_no_root = [item for item in no_root if "only" in item.get("method", "")]
        tables.append(
            {
                "block": [lo, hi],
                "boundary_count": len(boundaries),
                "no_root_interval_count": len(no_root),
                "monotone_no_root_count": sum(
                    1 for item in no_root if item.get("method") == "same-sign endpoints plus monotone F'"
                ),
                "unresolved_no_root_count": len(unresolved_no_root),
                "root_box_count": len(root_boxes),
                "boundaries": boundaries,
                "no_root_subintervals": no_root[:100],
                "root_boxes": root_boxes[:100],
            }
        )
    return tables


def unit_candidate_table(unit_id: int, start: int, end: int, args, tau: list[int], prefix: list[int]) -> dict:
    """合并一个 H80 单元的层查询与相位根盒账本。"""
    layer = layer_cert.unit_certificate(unit_id, start, end, args, tau, prefix)
    roots = root_table_for_unit(start, end, parse_blocks(args.root_blocks), args.q, tau, prefix)
    layer_checks_ok = all(check["ok"] for check in layer["checks"])
    root_ledger_ok = all(table["unresolved_no_root_count"] == 0 for table in roots)
    return {
        "unit_id": unit_id,
        "x_range": [start, end],
        "integer_candidate_checks_ok": layer_checks_ok,
        "root_ledger_ok_for_contract_blocks": root_ledger_ok,
        "status": "merged ledger; full closure still requires layer-functional derivatives, not only block contract derivatives",
        "layer_summary": {
            "max_U": layer["max_U"],
            "max_V": layer["max_V"],
            "max_light_L": layer["max_light_L"],
            "min_potential_L_ge_035": layer["min_potential_L_ge_035"],
            "checks": layer["checks"],
        },
        "root_tables": roots,
        "candidate_box_count": sum(table["boundary_count"] + table["root_box_count"] for table in roots),
        "open_interval_no_root_count": sum(table["no_root_interval_count"] for table in roots),
        "open_interval_root_box_count": sum(table["root_box_count"] for table in roots),
        "unresolved_open_interval_count": sum(table["unresolved_no_root_count"] for table in roots),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--units", default="1088472:1088477,1088496:1088499,1088506:1088507,1088551:1088555")
    parser.add_argument("--H", type=int, default=80)
    parser.add_argument("--hi", type=int, default=400)
    parser.add_argument("--q", type=float, default=0.958)
    parser.add_argument("--threshold-tau", type=int, default=60)
    parser.add_argument("--U-split", type=float, default=0.16)
    parser.add_argument("--root-blocks", default="1:200,201:400")
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()

    units = layer_cert.parse_units(args.units)
    max_end = max(end for _, end in units)
    tau, prefix = layer_cert.build(2 * max_end + 10)
    unit_tables = [unit_candidate_table(i + 1, start, end, args, tau, prefix) for i, (start, end) in enumerate(units)]
    payload = {
        "certificate_type": "D4-R5-unified-candidate-box-table",
        "status": "prototype merged table; proves integer H80 checks and records contract-root ledgers, but not yet full layer-functional root closure",
        "H": args.H,
        "hi": args.hi,
        "q": args.q,
        "threshold_tau": args.threshold_tau,
        "U_split": args.U_split,
        "root_blocks": parse_blocks(args.root_blocks),
        "units": unit_tables,
        "integer_candidate_checks_ok": all(unit["integer_candidate_checks_ok"] for unit in unit_tables),
        "contract_root_ledgers_ok": all(unit["root_ledger_ok_for_contract_blocks"] for unit in unit_tables),
        "total_candidate_box_count": sum(unit["candidate_box_count"] for unit in unit_tables),
        "total_open_interval_no_root_count": sum(unit["open_interval_no_root_count"] for unit in unit_tables),
        "total_open_interval_root_box_count": sum(unit["open_interval_root_box_count"] for unit in unit_tables),
        "total_unresolved_open_interval_count": sum(unit["unresolved_open_interval_count"] for unit in unit_tables),
        "remaining_hard_point": "replace block-contract root ledgers by derivatives of layer functionals U,V,L,E2,light_L,potential on fixed membership cells",
    }
    print(
        json.dumps(
            {
                "certificate_type": payload["certificate_type"],
                "integer_candidate_checks_ok": payload["integer_candidate_checks_ok"],
                "contract_root_ledgers_ok": payload["contract_root_ledgers_ok"],
                "unit_count": len(unit_tables),
                "total_candidate_box_count": payload["total_candidate_box_count"],
                "total_open_interval_no_root_count": payload["total_open_interval_no_root_count"],
                "total_open_interval_root_box_count": payload["total_open_interval_root_box_count"],
                "total_unresolved_open_interval_count": payload["total_unresolved_open_interval_count"],
                "remaining_hard_point": payload["remaining_hard_point"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
