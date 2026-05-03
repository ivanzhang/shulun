#!/usr/bin/env python3
"""D4/R5 有限窗口相位/成员单元枚举器。

枚举给定整数窗口内每一行的层泛函值、成员签名和 R5global 查询候选。
这是有限窗口无遗漏枚举器，不是全局 X 的解析模板枚举器。
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import d4_r5_layer_functional_certificate as layer_cert  # noqa: E402
import d4_r5_membership_cell_decomposition as member_dec  # noqa: E402


def row_record(x: int, args, tau, prefix) -> dict:
    """单行记录：层泛函与成员 digest。"""
    summary = layer_cert.layer_summary_for_x(x, args.hi, args.q, args.threshold_tau, args.H, tau, prefix)
    sig = member_dec.row_signature(x, args.hi, args.q, args.threshold_tau, args.H, tau, prefix)
    return {
        "x": x,
        "digest": sig["digest"],
        "U": summary["U"],
        "V": summary["V"],
        "light_L": summary["light_L"],
        "L": summary["L"],
        "E2": summary["E2"],
        "potential": summary["potential"],
        "short_L": summary["short_L"],
        "transition_L": summary["transition_L"],
        "W_pref": summary["W_pref"],
        "N_pref": summary["N_pref"],
        "M_pref": summary["M_pref"],
        "light_count": summary["light_count"],
        "transition_count": summary["transition_count"],
        "short_chain_count": summary["short_chain_count"],
        "signature_counts": sig["counts"],
        "signature_a_counts": sig["a_counts"],
    }


def argmax(rows: list[dict], key: str, pred=lambda r: True) -> dict | None:
    vals = [r for r in rows if pred(r)]
    return max(vals, key=lambda r: r[key]) if vals else None


def argmin(rows: list[dict], key: str, pred=lambda r: True) -> dict | None:
    vals = [r for r in rows if pred(r)]
    return min(vals, key=lambda r: r[key]) if vals else None


def compact(row: dict | None) -> dict | None:
    if row is None:
        return None
    keys = ["x", "digest", "U", "V", "light_L", "L", "E2", "potential", "short_L", "transition_L", "W_pref", "N_pref", "M_pref"]
    return {k: row[k] for k in keys}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", type=int, default=1_088_200)
    parser.add_argument("--end", type=int, default=1_088_600, help="exclusive")
    parser.add_argument("--H", type=int, default=80)
    parser.add_argument("--hi", type=int, default=400)
    parser.add_argument("--q", type=float, default=0.958)
    parser.add_argument("--threshold-tau", type=int, default=60)
    parser.add_argument("--U-split", type=float, default=0.16)
    parser.add_argument("--json", type=Path, default=Path("docs/d4-r5-window-phasecell-enumeration-1088200-1088600.json"))
    args = parser.parse_args()

    tau, prefix = layer_cert.build(2 * args.end + 10)
    rows = [row_record(x, args, tau, prefix) for x in range(args.start, args.end)]
    unique_digests = sorted({r["digest"] for r in rows})
    query_witnesses = {
        "R5global1_max_light_L_under_U_lt_split": compact(argmax(rows, "light_L", lambda r: r["U"] < args.U_split)),
        "R5global2_max_U_under_U_ge_split": compact(argmax(rows, "U", lambda r: r["U"] >= args.U_split)),
        "R5global2_max_V_under_U_ge_split": compact(argmax(rows, "V", lambda r: r["U"] >= args.U_split)),
        "R5light_max_light_L": compact(argmax(rows, "light_L")),
        "R5global3_min_potential_under_L_ge_035": compact(argmin(rows, "potential", lambda r: r["L"] >= 0.35)),
        "tailabsent_min_potential_proxy": compact(argmin(rows, "potential", lambda r: r["L"] >= 0.35 and r["transition_L"] == 0)),
    }
    candidate_xs = sorted({w["x"] for w in query_witnesses.values() if w is not None})
    payload = {
        "certificate_type": "D4-R5-finite-window-phasecell-enumeration",
        "status": "finite-window exhaustive integer-row/member-signature enumeration; not global analytic phase template enumeration",
        "start": args.start,
        "end": args.end,
        "row_count": len(rows),
        "H": args.H,
        "hi": args.hi,
        "q": args.q,
        "threshold_tau": args.threshold_tau,
        "U_split": args.U_split,
        "unique_member_signature_count": len(unique_digests),
        "query_witnesses": query_witnesses,
        "candidate_xs": candidate_xs,
        "candidate_count": len(candidate_xs),
        "checks": {
            "R5global1_window_ok": query_witnesses["R5global1_max_light_L_under_U_lt_split"]["light_L"] <= 0.245,
            "R5global2_U_window_ok": query_witnesses["R5global2_max_U_under_U_ge_split"]["U"] <= 0.182,
            "R5global2_V_window_ok": query_witnesses["R5global2_max_V_under_U_ge_split"]["V"] <= 0.074,
            "R5light_window_ok": query_witnesses["R5light_max_light_L"]["light_L"] <= 0.26,
            "R5global3_window_ok": query_witnesses["R5global3_min_potential_under_L_ge_035"]["potential"] >= 0,
        },
        "rows_compact": rows,
    }
    payload["all_window_checks_ok"] = all(payload["checks"].values())
    print(json.dumps({k: v for k, v in payload.items() if k != "rows_compact"}, ensure_ascii=False, indent=2))
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
