#!/usr/bin/env python3
"""D4/R5 精确符号模板提取原型。

模板 T=(floor residue data, offset groups, layer labels, constraint branch)。
此脚本仍针对有限窗口提取精确离散模板；下一步需把模板变量化为参数族。
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import d4_r5_layer_functional_certificate as layer_cert  # noqa: E402
from d4_lowblock_phase_capacity import offset_stats, term_rows  # noqa: E402


def symbolic_row_template(x: int, args, tau, prefix) -> dict:
    """提取一行的精确符号模板。"""
    rows = term_rows(x, args.hi, args.q, tau, prefix)
    offsets = offset_stats(x, rows)
    light, transition, short_chain = layer_cert.classify_offsets(offsets, args.threshold_tau)
    summary = layer_cert.layer_summary_for_x(x, args.hi, args.q, args.threshold_tau, args.H, tau, prefix)

    layer_by_offset = {}
    for layer_name, items in [("light", light), ("transition", transition), ("short", short_chain)]:
        for item in items:
            layer_by_offset[item["offset"]] = layer_name

    groups = []
    for item in sorted(light + transition + short_chain, key=lambda it: (it["offset"], it["count"], it["tau_sum"])):
        avals = sorted(item.get("a_values", []))
        # 精确 floor/residue 数据；a_values 本身已经由 a|x+h 确定。
        a_data = []
        for a in avals:
            a_data.append(
                {
                    "a": a,
                    "tau": tau[a],
                    "h_mod_a": (-x) % a or a,
                    "floor_x_over_a": x // a,
                    "floor_2x_over_a": (2 * x) // a,
                }
            )
        groups.append(
            {
                "offset": item["offset"],
                "layer": layer_by_offset[item["offset"]],
                "prefix_tail": "prefix" if item["offset"] <= args.H else "tail",
                "count": item["count"],
                "tau_sum": item["tau_sum"],
                "a_data": a_data,
            }
        )

    branch = {
        "U_branch": "high" if summary["U"] >= args.U_split else "low",
        "L_branch": "highmass" if summary["L"] >= 0.35 else "lowmass",
        "transition_present": summary["transition_L"] > 0,
        "short_present": summary["short_L"] > 0,
    }
    template = {"groups": groups, "branch": branch}
    canonical = json.dumps(template, sort_keys=True, separators=(",", ":"))
    digest = hashlib.sha256(canonical.encode()).hexdigest()[:20]
    return {
        "x": x,
        "template_digest": digest,
        "branch": branch,
        "group_count": len(groups),
        "a_total": sum(len(group["a_data"]) for group in groups),
        "query_values": {
            "U": summary["U"],
            "V": summary["V"],
            "light_L": summary["light_L"],
            "L": summary["L"],
            "E2": summary["E2"],
            "potential": summary["potential"],
        },
        "template": template,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", type=int, default=1_088_200)
    parser.add_argument("--end", type=int, default=1_088_600)
    parser.add_argument("--H", type=int, default=80)
    parser.add_argument("--hi", type=int, default=400)
    parser.add_argument("--q", type=float, default=0.958)
    parser.add_argument("--threshold-tau", type=int, default=60)
    parser.add_argument("--U-split", type=float, default=0.16)
    parser.add_argument("--json", type=Path, default=Path("docs/d4-r5-symbolic-templates-1088200-1088600.json"))
    args = parser.parse_args()

    tau, prefix = layer_cert.build(2 * args.end + 10)
    rows = [symbolic_row_template(x, args, tau, prefix) for x in range(args.start, args.end)]
    digest_map = {}
    for row in rows:
        digest_map.setdefault(row["template_digest"], []).append(row["x"])
    collisions = {k: v for k, v in digest_map.items() if len(v) > 1}
    branch_counts = {}
    for row in rows:
        key = json.dumps(row["branch"], sort_keys=True)
        branch_counts[key] = branch_counts.get(key, 0) + 1
    # 取 R5 查询见证模板。
    def argmax(key, pred=lambda r: True):
        vals = [r for r in rows if pred(r)]
        return max(vals, key=lambda r: r["query_values"][key]) if vals else None
    def argmin(key, pred=lambda r: True):
        vals = [r for r in rows if pred(r)]
        return min(vals, key=lambda r: r["query_values"][key]) if vals else None
    witnesses = {
        "R5global1": argmax("light_L", lambda r: r["query_values"]["U"] < args.U_split),
        "R5global2_U": argmax("U", lambda r: r["query_values"]["U"] >= args.U_split),
        "R5global2_V": argmax("V", lambda r: r["query_values"]["U"] >= args.U_split),
        "R5global3": argmin("potential", lambda r: r["query_values"]["L"] >= 0.35),
    }
    compact_witnesses = {
        name: None if row is None else {
            "x": row["x"],
            "template_digest": row["template_digest"],
            "branch": row["branch"],
            "group_count": row["group_count"],
            "a_total": row["a_total"],
            "query_values": row["query_values"],
            "template": row["template"],
        }
        for name, row in witnesses.items()
    }
    payload = {
        "certificate_type": "D4-R5-symbolic-template-extraction",
        "status": "finite-window exact symbolic templates; not yet parameterized global coverage",
        "start": args.start,
        "end": args.end,
        "row_count": len(rows),
        "unique_template_count": len(digest_map),
        "collision_count": len(collisions),
        "collisions": collisions,
        "branch_counts": branch_counts,
        "witnesses": compact_witnesses,
        "rows_compact": [
            {k: row[k] for k in ["x", "template_digest", "branch", "group_count", "a_total", "query_values"]}
            for row in rows
        ],
    }
    print(json.dumps({k: v for k, v in payload.items() if k not in {"rows_compact", "witnesses"}}, ensure_ascii=False, indent=2))
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
