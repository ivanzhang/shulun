#!/usr/bin/env python3
"""审计 D4/R5 的 G1 容量界证据。

本脚本只抽取已有有限窗口/局部证书中的容量数据，
并明确区分“已验证的局部上界”和“全局化所需证明义务”。
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"


def load_json(name: str) -> Any:
    with (DOCS / name).open(encoding="utf-8") as fh:
        return json.load(fh)


def round_float(value: Any) -> Any:
    if isinstance(value, float):
        return float(f"{value:.17g}")
    return value


def main() -> None:
    resource = load_json("d4-r5-layer-resource-curves.json")
    layered = load_json("d4-r5-offset-layered-scan-1088200-1088600-step1-T60-full.json")
    window = load_json("d4-r5-window-phasecell-enumeration-1088200-1088600.json")
    gates = load_json("d4-r5-global-rpl-gates.json")

    curves = resource.get("curves", {})
    curve_summary = {}
    for name, curve in curves.items():
        point = curve.get("max_point", {})
        curve_summary[name] = {
            "max_L": round_float(point.get("L")),
            "max_E": round_float(point.get("E")),
            "max_N": point.get("N"),
            "max_M": point.get("M"),
            "max_x": point.get("x"),
            "max_R": round_float(point.get("R")),
            "L_floor_support": curve.get("by_L_floor", []),
        }

    regimes = resource.get("regimes", [])
    regime_summary = []
    local_total_max_L = 0.0
    local_total_max_record = None
    for regime in regimes:
        total = regime.get("max_total", {})
        L = float(total.get("L", 0.0) or 0.0)
        if L > local_total_max_L:
            local_total_max_L = L
            local_total_max_record = {"regime": regime.get("name"), **total}
        regime_summary.append(
            {
                "name": regime.get("name"),
                "count": regime.get("count"),
                "max_total": total,
            }
        )

    # 行级扫描中的 positive_contract_sum 是容量支付账本更直接使用的口径；
    # resource curves 的 regime max_total.L 是分层资源曲线口径。
    row_capacity_records = []
    for row in layered.get("rows", []):
        row_L = float(row.get("positive_contract_sum", 0.0) or 0.0)
        row_E_l2 = sum(
            float(row.get(key, 0.0) or 0.0)
            for key in [
                "transition_high_tail_l2",
                "transition_low_start_l2",
                "short_chain_l2",
                "light_l2",
            ]
        )
        row_E_sqrt_sum = sum(
            float(row.get(key, 0.0) or 0.0)
            for key in [
                "transition_high_tail_l2_sqrt",
                "transition_low_start_l2_sqrt",
                "short_chain_l2_sqrt",
                "light_l2_sqrt",
            ]
        )
        row_capacity_records.append(
            {
                "x": row.get("x"),
                "L_positive_contract_sum": row_L,
                "E_layer_l2_sum": row_E_l2,
                "D_l2_minus_L2_over_20": row_E_l2 - row_L * row_L / 20.0,
                "E_sqrt_layer_sum": row_E_sqrt_sum,
                "D_sqrt_sum_minus_L2_over_20": row_E_sqrt_sum - row_L * row_L / 20.0,
            }
        )

    row_max_record = max(row_capacity_records, key=lambda item: item["L_positive_contract_sum"])
    row_max_L = row_max_record["L_positive_contract_sum"]
    candidate_Lmax = max(0.48, local_total_max_L, row_max_L)
    payment_bound = candidate_Lmax * candidate_Lmax / 20.0

    row_floor_summary = []
    for floor in [0.35, 0.38, 0.4, 0.42, 0.45]:
        subset = [item for item in row_capacity_records if item["L_positive_contract_sum"] >= floor]
        if subset:
            row_floor_summary.append(
                {
                    "L_floor": floor,
                    "count": len(subset),
                    "min_D_l2_minus_L2_over_20": min(item["D_l2_minus_L2_over_20"] for item in subset),
                    "min_D_sqrt_sum_minus_L2_over_20": min(item["D_sqrt_sum_minus_L2_over_20"] for item in subset),
                    "max_L_positive_contract_sum": max(item["L_positive_contract_sum"] for item in subset),
                }
            )
        else:
            row_floor_summary.append({"L_floor": floor, "count": 0})

    gate_status = {g.get("id", g.get("name", f"gate_{i}")): g for i, g in enumerate(gates.get("gates", []), 1)}

    audit = {
        "certificate_type": "D4/R5 G1 capacity audit",
        "status": "local_window_capacity_extracted_global_G1_not_yet_proved",
        "input_files": {
            "resource_curves": str(DOCS / "d4-r5-layer-resource-curves.json"),
            "layered_scan": str(DOCS / "d4-r5-offset-layered-scan-1088200-1088600-step1-T60-full.json"),
            "window_enumeration": str(DOCS / "d4-r5-window-phasecell-enumeration-1088200-1088600.json"),
            "global_gates": str(DOCS / "d4-r5-global-rpl-gates.json"),
        },
        "finite_window": {
            "start": window.get("start"),
            "end": window.get("end"),
            "row_count": window.get("row_count"),
            "all_window_checks_ok": window.get("all_window_checks_ok"),
            "hi": window.get("hi"),
            "q": window.get("q"),
        },
        "layered_scan_global_fields": {
            key: layered.get(key)
            for key in [
                "max_total_contract",
                "max_positive_contract_sum",
                "max_light_l2_sqrt",
                "max_transition_l2_sqrt",
                "max_short_chain_l2_sqrt",
                "max_exceptional_l2_sqrt",
                "worst_total_row",
                "worst_light_l2_row",
                "worst_short_chain_l2_row",
            ]
            if key in layered
        },
        "curve_summary": curve_summary,
        "regime_summary": regime_summary,
        "local_total_capacity_bound": {
            "resource_curve_observed_max_L": round_float(local_total_max_L),
            "resource_curve_observed_max_record": local_total_max_record,
            "row_positive_contract_observed_max_L": round_float(row_max_L),
            "row_positive_contract_observed_max_record": row_max_record,
            "row_positive_contract_floor_summary": row_floor_summary,
            "safe_candidate_Lmax_for_local_certificates": round_float(candidate_Lmax),
            "corresponding_stable_payment_telescope_bound_Lmax_squared_over_20": round_float(payment_bound),
            "interpretation": "Two local capacity conventions are reported. The row positive-contract convention is larger and should be used for payment safety; this is still finite-window evidence, not a global proof.",
        },
        "G1_candidate_statement": {
            "name": "scale_stable_capacity_bound",
            "claim_needed": "For every recursive peeling chain reaching a dangerous R5 state, the active capacity L_j stays below a universal L_max before it enters the finite certified terminal window, or else the excess capacity forces positive defect and exits the dangerous class.",
            "minimal_sufficient_form": "0 <= L_j <= Lmax on all stable positive-mass steps; jumps are charged separately and backflow losses are summable.",
            "local_suggested_Lmax": round_float(candidate_Lmax),
            "warning": "Use at least L_cap=0.48 after the multi-window Lyapunov audit; the 0.47 value only covered this single row-level payment window.",
        },
        "proof_obligations_remaining": [
            "G1a: define active capacity L_j intrinsically for arbitrary scale X, not by the finite window extractor.",
            "G1b: prove shell monotonicity/nonnegative mass for stable steps after canonical relabelling.",
            "G1c: prove either L_j <= Lmax or a capacity-energy defect D_j >= delta(L_j) that excludes the bad configuration.",
            "G1d: prove the terminal finite-window certificate is reached by the recursion without changing the functional semantics.",
        ],
        "current_gate_snapshot": gate_status,
    }

    out = DOCS / "d4-r5-G1-capacity-audit.json"
    with out.open("w", encoding="utf-8") as fh:
        json.dump(audit, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    print(out)
    print(json.dumps(audit["local_total_capacity_bound"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
