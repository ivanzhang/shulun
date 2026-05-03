#!/usr/bin/env python3
"""D4/R5 多窗口模板稳定性探针。

将逐行成员签名压缩为尺度归一模板键，用多个窗口检查候选极值模板是否稳定。
这是解析相位模板枚举器的前置实验，不是证明器。
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import d4_r5_layer_functional_certificate as layer_cert  # noqa: E402
from d4_lowblock_phase_capacity import offset_stats, term_rows  # noqa: E402


def compressed_template(x: int, args, tau, prefix) -> dict:
    """生成压缩模板键：只记录层计数/权重桶/主导偏移形状。"""
    rows = term_rows(x, args.hi, args.q, tau, prefix)
    offsets = offset_stats(x, rows)
    light, transition, short_chain = layer_cert.classify_offsets(offsets, args.threshold_tau)
    pref = [item for item in light if item["offset"] <= args.H]
    tail = [item for item in light if item["offset"] > args.H]

    def top_shape(items: list[dict], n: int = 5) -> tuple:
        top = sorted(items, key=lambda item: item["positive_contract_sum"], reverse=True)[:n]
        shape = []
        for item in top:
            avals = item.get("a_values", [])
            shape.append(
                (
                    min(item["offset"], 999),
                    item["count"],
                    item["tau_sum"],
                    min(avals) if avals else 0,
                    max(avals) if avals else 0,
                    len([a for a in avals if a <= 80]),
                    len([a for a in avals if a >= 200]),
                )
            )
        return tuple(shape)

    def stats(items: list[dict]) -> tuple:
        return (
            len(items),
            sum(item["count"] for item in items),
            sum(item["tau_sum"] for item in items),
            round(sum(item["positive_contract_sum"] for item in items), 6),
            round(sum(item["positive_contract_sum"] ** 2 for item in items), 8),
        )

    summary = layer_cert.layer_summary_for_x(x, args.hi, args.q, args.threshold_tau, args.H, tau, prefix)
    key = {
        "layer_stats": {
            "pref": stats(pref),
            "tail": stats(tail),
            "light": stats(light),
            "short": stats(short_chain),
            "transition": stats(transition),
        },
        "top_shapes": {
            "pref": top_shape(pref),
            "tail": top_shape(tail),
            "short": top_shape(short_chain),
        },
        "query_values": {
            "U": summary["U"],
            "V": summary["V"],
            "light_L": summary["light_L"],
            "L": summary["L"],
            "E2": summary["E2"],
            "potential": summary["potential"],
            "short_L": summary["short_L"],
            "transition_L": summary["transition_L"],
        },
    }
    template_key = json.dumps({"layer_stats": key["layer_stats"], "top_shapes": key["top_shapes"]}, sort_keys=True)
    return {"x": x, "template_key": template_key, **key}


def window_probe(start: int, width: int, args) -> dict:
    """扫描一个窗口。"""
    end = start + width
    tau, prefix = layer_cert.build(2 * end + 10)
    rows = [compressed_template(x, args, tau, prefix) for x in range(start, end)]
    witnesses = {
        "R5global1": max([r for r in rows if r["query_values"]["U"] < args.U_split], key=lambda r: r["query_values"]["light_L"], default=None),
        "R5global2_U": max([r for r in rows if r["query_values"]["U"] >= args.U_split], key=lambda r: r["query_values"]["U"], default=None),
        "R5global2_V": max([r for r in rows if r["query_values"]["U"] >= args.U_split], key=lambda r: r["query_values"]["V"], default=None),
        "R5global3": min([r for r in rows if r["query_values"]["L"] >= 0.35], key=lambda r: r["query_values"]["potential"], default=None),
    }
    compact_witnesses = {}
    for name, row in witnesses.items():
        if row is None:
            compact_witnesses[name] = None
        else:
            compact_witnesses[name] = {
                "x": row["x"],
                "template_key": row["template_key"],
                "query_values": row["query_values"],
                "layer_stats": row["layer_stats"],
                "top_shapes": row["top_shapes"],
            }
    return {
        "start": start,
        "end": end,
        "row_count": len(rows),
        "unique_template_count": len({r["template_key"] for r in rows}),
        "witnesses": compact_witnesses,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--starts", default="1028000,1049500,1088200,1470000,2000000")
    parser.add_argument("--width", type=int, default=400)
    parser.add_argument("--H", type=int, default=80)
    parser.add_argument("--hi", type=int, default=400)
    parser.add_argument("--q", type=float, default=0.958)
    parser.add_argument("--threshold-tau", type=int, default=60)
    parser.add_argument("--U-split", type=float, default=0.16)
    parser.add_argument("--json", type=Path, default=Path("docs/d4-r5-multwindow-template-probe.json"))
    args = parser.parse_args()
    starts = [int(item) for item in args.starts.split(",") if item.strip()]
    windows = [window_probe(start, args.width, args) for start in starts]
    witness_templates = {}
    for window in windows:
        for name, row in window["witnesses"].items():
            if row is not None:
                witness_templates.setdefault(name, set()).add(row["template_key"])
    payload = {
        "certificate_type": "D4-R5-multiwindow-compressed-template-probe",
        "status": "exploratory template stability probe; not a proof of global coverage",
        "width": args.width,
        "windows": windows,
        "witness_template_counts": {name: len(values) for name, values in witness_templates.items()},
        "total_witness_template_count": sum(len(values) for values in witness_templates.values()),
        "interpretation": "If witness template counts remain small, next step is to define exact symbolic template keys and prove coverage.",
    }
    print(json.dumps({k: v for k, v in payload.items() if k != "windows"}, ensure_ascii=False, indent=2))
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
