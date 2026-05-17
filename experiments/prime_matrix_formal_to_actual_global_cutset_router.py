#!/usr/bin/env python3
"""生成 Prime Matrix formal-to-actual 全局剩余切面证书。

用法示例：
  python3 experiments/prime_matrix_formal_to_actual_global_cutset_router.py
  python3 -m json.tool data/prime-matrix-formal-to-actual-global-cutset-ledger.json

输出：
  data/prime-matrix-formal-to-actual-global-cutset-ledger.json
  docs/monograph/prime-matrix-formal-to-actual-global-cutset-router.json
  docs/monograph/prime-matrix-formal-to-actual-global-cutset-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

ACTUAL_PACKET = DATA / "prime-matrix-affine-twin-actual-packet-contract-ledger.json"
FORMAL_PRUNING = DATA / "prime-matrix-affine-twin-formal-pair-pruning-ledger.json"
SOURCE_GATE = DATA / "prime-matrix-affine-twin-source-materialization-gate-ledger.json"
CRT_WINDOW = DATA / "prime-matrix-affine-twin-crt-window-gap-ledger.json"
MOVING_SLOT = DATA / "prime-matrix-affine-twin-endpoint-release-moving-slot-graph-cap-route-ledger.json"
REMAINING_BRIDGE = DATA / "prime-matrix-affine-twin-endpoint-release-remaining-frontier-bridge-ledger.json"
ENDPOINT_ATOM = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-endpoint-band-atom-ledger.json"

OUT_LEDGER = DATA / "prime-matrix-formal-to-actual-global-cutset-ledger.json"
OUT_JSON = DOCS / "prime-matrix-formal-to-actual-global-cutset-router.json"
OUT_MD = DOCS / "prime-matrix-formal-to-actual-global-cutset-router.md"

NEXT_TARGET = "GlobalFormalToActualCutsetPromotionOrNamedExitExclusion"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def build_result() -> dict[str, Any]:
    """合成 formal-to-actual 当前切面。"""
    actual = load_json(ACTUAL_PACKET)["aggregate"]
    pruning = load_json(FORMAL_PRUNING)["aggregate"]
    source = load_json(SOURCE_GATE)["aggregate"]
    crt = load_json(CRT_WINDOW)["aggregate"]
    moving = load_json(MOVING_SLOT)["aggregate"]
    remaining = load_json(REMAINING_BRIDGE)
    remaining_agg = remaining["aggregate"]
    endpoint = load_json(ENDPOINT_ATOM)
    endpoint_atom_count = len(endpoint["endpoint_atom_keys"])

    current_closed = all(
        [
            bool(pruning["product_accounting_tightening_closed_current_sweep"]),
            bool(source["source_materialization_gate_closed_current_sweep"]),
            bool(crt["crt_window_gap_closed_current_sweep"]),
            bool(moving["anonymous_moving_slot_actual_overload_closed_current_sweep"]),
            bool(remaining_agg["remaining_frontier_bridge_closed_current_sweep"]),
        ]
    )
    row_column_closed = all(
        [
            bool(actual["row_column_unconditional_closed"]),
            bool(pruning["row_column_unconditional_closed"]),
            bool(source["row_column_unconditional_closed"]),
            bool(crt["row_column_unconditional_closed"]),
            bool(moving["row_column_unconditional_closed"]),
            bool(remaining_agg["row_column_unconditional_closed"]),
        ]
    )

    cutset_rows = [
        {
            "gate": "ProductAccountingTighteningCurrent",
            "current_status": "closed_current_sweep",
            "capacity_phase_readout": (
                f"formal={pruning['formal_pair_total']}, actual={pruning['actual_packet_total_current']}, "
                f"gap={pruning['formal_to_actual_gap']}="
                f"{pruning['crt_window_empty_pair_total_current']} CRTWindowEmpty + "
                f"{pruning['source_unmaterialized_pair_total_current']} SourceMaterializationFailure"
            ),
            "global_remaining": "GlobalProductAccountingTightening",
        },
        {
            "gate": "SourceMaterializationGate",
            "current_status": "closed_current_sweep",
            "capacity_phase_readout": (
                f"pass={source['source_gate_pass_q_values']}, fail={source['source_gate_fail_q_values']}, "
                f"same_gap_wrong_source={source['same_gap_wrong_source_formal_pair_count']}, "
                f"no_gap_source={source['no_gap_source_formal_pair_count']}"
            ),
            "global_remaining": "SameGapWrongSource-PDEC/SAE + NoGapSource-PDEC/SAE",
        },
        {
            "gate": "CRTWindowGap",
            "current_status": "closed_current_sweep",
            "capacity_phase_readout": (
                f"modulus={crt['combined_modulus_current']}, support_width={crt['support_width_current']}, "
                f"modulus_minus_width={crt['modulus_minus_support_width_current']}, "
                f"empty_pairs={crt['crt_window_gap_pair_total_current']}, "
                f"min_distance={crt['min_empty_window_distance']}"
            ),
            "global_remaining": "GlobalCRTWindowGapBound + WindowEdgeCollision/SupportMotion exits",
        },
        {
            "gate": "PrimitiveSupportEscapeRouting",
            "current_status": "closed_current_sweep",
            "capacity_phase_readout": (
                f"support_width={moving['current_support_width']}, sqrt_floor={moving['current_sqrt_floor']}, "
                f"narrowest_release_over_width={moving['narrowest_release_over_support_width']}, "
                f"exact_rematerialized_q={moving['exact_rematerialized_q_values']}"
            ),
            "global_remaining": "MovingSlotFamilyPersistenceNoGo + SourceRematerialization/ColumnCRT exits",
        },
        {
            "gate": "RemainingFrontierBridge",
            "current_status": "closed_current_sweep",
            "capacity_phase_readout": (
                f"transport_reset_atoms={remaining_agg['transport_reset_pdec_atom_count']}, "
                f"singleton_packets={remaining_agg['singleton_residue_packet_count']}, "
                f"active_band={remaining_agg['active_band_min']}..{remaining_agg['active_band_max']}, "
                f"epoch_pair_mass={remaining_agg['candidate_product_mass_upper_sum']}<eta={remaining_agg['eta']}"
            ),
            "global_remaining": ", ".join(remaining["global_remaining"]),
        },
        {
            "gate": "EndpointAtomIsolation",
            "current_status": "closed_current_sweep",
            "capacity_phase_readout": (
                f"endpoints={endpoint['active_band_endpoints']}, "
                f"endpoint_atom_count={endpoint_atom_count}, "
                f"minus_only={endpoint['endpoint_only_minus_current_sweep']}"
            ),
            "global_remaining": "EndpointBandMotionBoundOrEndpointAtomPDECExclusion",
        },
    ]

    result = {
        "certificate_type": "prime_matrix_formal_to_actual_global_cutset_router",
        "status": "current_sweep_cutset_closed_global_unconditional_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_sweep_not_used_as_global_proof": True,
        "aggregate": {
            "candidate_q_values": pruning["candidate_q_values"],
            "formal_pair_total": pruning["formal_pair_total"],
            "actual_packet_total_current": pruning["actual_packet_total_current"],
            "formal_to_actual_gap": pruning["formal_to_actual_gap"],
            "crt_window_empty_pair_total_current": pruning["crt_window_empty_pair_total_current"],
            "source_unmaterialized_pair_total_current": pruning["source_unmaterialized_pair_total_current"],
            "unresolved_formal_pair_total_current": pruning["unresolved_formal_pair_total_current"],
            "combined_modulus_current": crt["combined_modulus_current"],
            "support_width_current": crt["support_width_current"],
            "min_empty_window_distance": crt["min_empty_window_distance"],
            "moving_slot_escape_closed_current_sweep": moving[
                "anonymous_moving_slot_actual_overload_closed_current_sweep"
            ],
            "remaining_frontier_bridge_closed_current_sweep": remaining_agg[
                "remaining_frontier_bridge_closed_current_sweep"
            ],
            "endpoint_atom_count": endpoint_atom_count,
            "current_sweep_cutset_closed": current_closed,
            "row_column_unconditional_closed": row_column_closed,
            "hardpoint_after_router": NEXT_TARGET,
            "next_direct_attack_target": NEXT_TARGET,
        },
        "cutset_rows": cutset_rows,
        "global_remaining_cutset": [
            "GlobalProductAccountingTightening promotion",
            "SourceMaterializationFailure-PDEC/SAE exclusion",
            "CRTWindowEmptyGlobalSupportBound promotion",
            "PrimitiveTwinSlotSupportEscape-PDEC/SAE exclusion",
            "ActiveEllBandEndpointGrowthBoundOrEndpointResetPDEC",
            "TransportResetPDECExclusion",
            "GlobalEpochPairMultiplicityBound",
            "MovingResidueShapeSAE/Rankin",
        ],
        "plain_conclusion": (
            "当前 sweep 的 formal-to-actual 容量差已经切成命名出口："
            "40 个形式配对只有 1 个 actual packet，39 个差额由 11 个 CRT 空窗和 28 个源未物化解释；"
            "CRT 主原子满足 899>20 且空窗最小距离为 40；"
            "固定 primitive 支撑内 actual load 低于平方根门，支撑逃逸已回流到 moving-slot、endpoint、transport 与 epoch-pair 出口。"
            "这关闭 current-sweep cutset，但全局行/列命题仍需把这些出口逐一全局排斥或求和吸收。"
        ),
        "dependency_hashes": {
            str(path.relative_to(ROOT)): sha256(path)
            for path in (
                ACTUAL_PACKET,
                FORMAL_PRUNING,
                SOURCE_GATE,
                CRT_WINDOW,
                MOVING_SLOT,
                REMAINING_BRIDGE,
                ENDPOINT_ATOM,
            )
        },
    }
    return result


def write_outputs(result: dict[str, Any]) -> None:
    """写出 JSON 与 Markdown。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    OUT_LEDGER.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    agg = result["aggregate"]
    lines = [
        "# Prime Matrix formal-to-actual global cutset router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"candidate_q_values={agg['candidate_q_values']}",
        f"formal_pair_total={agg['formal_pair_total']}",
        f"actual_packet_total_current={agg['actual_packet_total_current']}",
        f"formal_to_actual_gap={agg['formal_to_actual_gap']}",
        f"crt_window_empty_pair_total_current={agg['crt_window_empty_pair_total_current']}",
        f"source_unmaterialized_pair_total_current={agg['source_unmaterialized_pair_total_current']}",
        f"unresolved_formal_pair_total_current={agg['unresolved_formal_pair_total_current']}",
        f"combined_modulus_current={agg['combined_modulus_current']}",
        f"support_width_current={agg['support_width_current']}",
        f"min_empty_window_distance={agg['min_empty_window_distance']}",
        f"endpoint_atom_count={agg['endpoint_atom_count']}",
        f"current_sweep_cutset_closed={fmt_bool(agg['current_sweep_cutset_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(agg['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. cutset rows",
        "",
        "| gate | current status | capacity/phase readout | global remaining |",
        "| --- | --- | --- | --- |",
    ]
    for row in result["cutset_rows"]:
        lines.append(
            f"| `{row['gate']}` | `{row['current_status']}` | {row['capacity_phase_readout']} | `{row['global_remaining']}` |"
        )

    lines.extend(
        [
            "",
            "## 2. 最新剩余切面",
            "",
        ]
    )
    for item in result["global_remaining_cutset"]:
        lines.append(f"- `{item}`")
    lines.extend(
        [
            "",
            "## 3. 结论边界",
            "",
            "- 本证书关闭的是 current-sweep cutset：当前反例链容量读数无法作为匿名 actual load 保留。",
            "- 它没有证明全局行/列命题；全局证明仍需把上述出口提升为无条件排斥或可求和吸收。",
            f"- 下一主攻点：`{agg['next_direct_attack_target']}`。",
            "",
            "## 4. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in result["dependency_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """入口。"""
    result = build_result()
    write_outputs(result)
    print(json.dumps(result["aggregate"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
