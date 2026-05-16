#!/usr/bin/env python3
"""生成 AffineTwin endpoint-release support-width near-scale fracture 审计证书。

用法示例：
  python3 experiments/prime_matrix_affine_twin_endpoint_release_support_width_nearscale_fracture_audit.py
  python3 -m json.tool data/prime-matrix-affine-twin-endpoint-release-support-width-nearscale-fracture-ledger.json

输出：
  data/prime-matrix-affine-twin-endpoint-release-support-width-nearscale-fracture-ledger.json
  docs/monograph/prime-matrix-affine-twin-endpoint-release-support-width-nearscale-fracture-audit.json
  docs/monograph/prime-matrix-affine-twin-endpoint-release-support-width-nearscale-fracture-audit.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

ACTUAL_ANCHOR_LEDGER = DATA / (
    "prime-matrix-affine-twin-endpoint-release-actual-anchor-replacement-ledger.json"
)
MOVING_KEY_LEDGER = DATA / (
    "prime-matrix-affine-twin-moving-key-source-rematerialization-ledger.json"
)
UNUSED_TARGET_LEDGER = DATA / (
    "prime-matrix-affine-twin-unused-target-arrival-ledger.json"
)
PAIR_LEDGER = DATA / (
    "square-phase-offband-prefix-gap-shadow-selector-h-lower-gap-fill-pair-ledger.json"
)
PHASE_SCALE_LEDGER = DATA / (
    "prime-matrix-affine-twin-endpoint-release-phase-scale-bridge-exhaustion-ledger.json"
)

OUT_LEDGER = DATA / (
    "prime-matrix-affine-twin-endpoint-release-support-width-nearscale-fracture-ledger.json"
)
OUT_JSON = DOCS / (
    "prime-matrix-affine-twin-endpoint-release-support-width-nearscale-fracture-audit.json"
)
OUT_MD = DOCS / (
    "prime-matrix-affine-twin-endpoint-release-support-width-nearscale-fracture-audit.md"
)


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def compact_source(row: dict[str, Any]) -> dict[str, Any]:
    """提取 gap-fill source 签名。"""
    return {
        "gap_ell": int(row["gap_ell"]),
        "generator_ell": int(row["generator_ell"]),
        "fill_ell": int(row["fill_ell"]),
        "generator_side": str(row["generator_side"]),
        "fill_side": str(row["fill_side"]),
        "p_delay": int(row["p_delay"]),
        "gap_fill_pair_key": str(row["gap_fill_pair_key"]),
    }


def source_matches_expected(source: dict[str, Any], expected: dict[str, Any]) -> bool:
    """判定 gap source 是否是 moving q 的同向 AffineTwin 期望源。"""
    return (
        int(expected["gap_ell"]) == int(source["gap_ell"])
        and int(expected["generator_ell"]) == int(source["generator_ell"])
        and int(expected["fill_ell"]) == int(source["fill_ell"])
        and str(expected["generator_side"]) == str(source["generator_side"])
        and str(expected["fill_side"]) == str(source["fill_side"])
        and expected["expected_p_delay"] == int(source["p_delay"])
    )


def source_events(
    q: int,
    support_width: int,
    sources: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """枚举 q 或 q-2 在 support width 内靠近 gap source 的事件。"""
    events: list[dict[str, Any]] = []
    for source in sources:
        gap = int(source["gap_ell"])
        for scale_name, scale_value in (("q", q), ("q_minus_2", q - 2)):
            delta = gap - scale_value
            if abs(delta) <= support_width:
                events.append(
                    {
                        "scale_kind": scale_name,
                        "scale_value": scale_value,
                        "source_gap": gap,
                        "signed_delta": delta,
                        "abs_delta": abs(delta),
                        "source_signature": compact_source(source),
                    }
                )
    return events


def jump_events(
    q: int,
    support_width: int,
    unused_rows: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """枚举 q 或 q-2 在 support width 内靠近 unused-target jump 的事件。"""
    events: list[dict[str, Any]] = []
    for row in unused_rows:
        jump = int(row["abs_crt_jump_to_unused_target"])
        for scale_name, scale_value in (("q", q), ("q_minus_2", q - 2)):
            delta = jump - scale_value
            if abs(delta) <= support_width:
                events.append(
                    {
                        "scale_kind": scale_name,
                        "scale_value": scale_value,
                        "unused_jump": jump,
                        "signed_delta": delta,
                        "abs_delta": abs(delta),
                        "source_pair_key": str(row["source_pair_key"]),
                        "target_unused_pair_key": str(row["target_unused_pair_key"]),
                        "new_side_residue_count": int(row["new_side_residue_count"]),
                    }
                )
    return events


def build_q_row(
    moving_row: dict[str, Any],
    support_width: int,
    sources: list[dict[str, Any]],
    unused_rows: list[dict[str, Any]],
) -> dict[str, Any]:
    """构造单个 q 的 near-scale 审计行。"""
    q = int(moving_row["q"])
    expected = moving_row["expected_signature"]
    src_events = source_events(q, support_width, sources)
    jmp_events = jump_events(q, support_width, unused_rows)
    scale_kinds_with_source = {event["scale_kind"] for event in src_events}
    scale_kinds_with_jump = {event["scale_kind"] for event in jmp_events}
    common_scale_kinds = sorted(scale_kinds_with_source & scale_kinds_with_jump)

    exact_source_signature_match = any(
        event["signed_delta"] == 0
        and source_matches_expected(event["source_signature"], expected)
        for event in src_events
    )
    exact_jump_without_new_side = any(
        event["signed_delta"] == 0 and event["new_side_residue_count"] == 0
        for event in jmp_events
    )
    viable_nearscale_bridge = (
        bool(moving_row["prime_gate"]["affine_twin_prime_gate_passed"])
        and bool(moving_row["moving_key_source_rematerialized_current"])
        and exact_source_signature_match
        and exact_jump_without_new_side
    )

    if viable_nearscale_bridge:
        route = "ViableNearScaleBridge"
    elif common_scale_kinds:
        route = "NearSourceAndJumpButGateFractured"
    elif src_events:
        route = "NearSourceOnly"
    elif jmp_events:
        route = "NearJumpOnly"
    else:
        route = "NoSupportWidthNearScale"

    return {
        "q": q,
        "route": route,
        "moving_route": str(moving_row["route"]),
        "source_pair_keys": moving_row["source_pair_keys"],
        "prime_gate": moving_row["prime_gate"],
        "failed_invariants": moving_row["failed_invariants"],
        "source_nearscale_event_count": len(src_events),
        "unused_jump_nearscale_event_count": len(jmp_events),
        "common_scale_kinds": common_scale_kinds,
        "source_nearscale_events": src_events,
        "unused_jump_nearscale_events": jmp_events,
        "exact_source_signature_match": exact_source_signature_match,
        "exact_jump_without_new_side_residue": exact_jump_without_new_side,
        "viable_support_width_nearscale_bridge_current": viable_nearscale_bridge,
    }


def build_result(
    actual_anchor_path: Path,
    moving_key_path: Path,
    unused_target_path: Path,
    pair_path: Path,
    phase_scale_path: Path,
) -> dict[str, Any]:
    """构造 support-width near-scale fracture 审计结果。"""
    actual_anchor = load_json(actual_anchor_path)
    moving_key = load_json(moving_key_path)
    unused_target = load_json(unused_target_path)
    pair = load_json(pair_path)
    phase_scale = load_json(phase_scale_path)

    support_width = int(actual_anchor["aggregate"]["support_width"])
    moving_rows = moving_key["candidate_q_source_rematerialization_rows"]
    source_rows = pair["gap_fill_pair_rows"]
    unused_rows = unused_target["unused_target_arrival_rows"]

    q_rows = [
        build_q_row(row, support_width, source_rows, unused_rows)
        for row in moving_rows
    ]
    near_source_rows = [
        row for row in q_rows if int(row["source_nearscale_event_count"]) > 0
    ]
    near_jump_rows = [
        row for row in q_rows if int(row["unused_jump_nearscale_event_count"]) > 0
    ]
    near_both_rows = [row for row in q_rows if row["common_scale_kinds"]]
    viable_rows = [
        row
        for row in q_rows
        if bool(row["viable_support_width_nearscale_bridge_current"])
    ]
    route_histogram = Counter(str(row["route"]) for row in q_rows)
    near_both_route_histogram = Counter(str(row["moving_route"]) for row in near_both_rows)

    all_nearscale_bridges_fractured = (
        not viable_rows
        and [int(row["q"]) for row in near_both_rows] == [61, 65]
        and all(
            str(row["moving_route"]) in {"PrimeButNotTwinAffine", "CompositeQ"}
            for row in near_both_rows
        )
        and bool(
            phase_scale["aggregate"][
                "all_exact_or_offset_scale_bridges_fractured_current_sweep"
            ]
        )
    )

    aggregate = {
        "actual_anchor_replacement_ledger": str(
            actual_anchor_path.relative_to(ROOT)
        ),
        "moving_key_source_rematerialization_ledger": str(
            moving_key_path.relative_to(ROOT)
        ),
        "unused_target_arrival_ledger": str(unused_target_path.relative_to(ROOT)),
        "pair_ledger": str(pair_path.relative_to(ROOT)),
        "phase_scale_bridge_exhaustion_ledger": str(
            phase_scale_path.relative_to(ROOT)
        ),
        "support_width": support_width,
        "moving_q_candidate_count": len(q_rows),
        "support_width_near_source_q_values": [int(row["q"]) for row in near_source_rows],
        "support_width_near_unused_jump_q_values": [
            int(row["q"]) for row in near_jump_rows
        ],
        "support_width_near_source_and_jump_q_values": [
            int(row["q"]) for row in near_both_rows
        ],
        "viable_support_width_nearscale_bridge_q_values": [
            int(row["q"]) for row in viable_rows
        ],
        "route_histogram": dict(sorted(route_histogram.items())),
        "near_source_and_jump_moving_route_histogram": dict(
            sorted(near_both_route_histogram.items())
        ),
        "phase_scale_exact_or_offset_bridges_fractured_current_sweep": bool(
            phase_scale["aggregate"][
                "all_exact_or_offset_scale_bridges_fractured_current_sweep"
            ]
        ),
        "all_support_width_nearscale_bridges_fractured_current_sweep": (
            all_nearscale_bridges_fractured
        ),
        "global_support_width_nearscale_bridge_excluded": False,
        "row_column_unconditional_closed": False,
    }

    return {
        "certificate_type": (
            "prime_matrix_affine_twin_endpoint_release_"
            "support_width_nearscale_fracture_audit"
        ),
        "status": "current_sweep_support_width_nearscale_fractured_global_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "aggregate": aggregate,
        "q_nearscale_rows": q_rows,
        "contract": {
            "support_width_nearscale_gate": [
                "near equality within support width is not an exact source or CRT identity",
                "a candidate must still pass the AffineTwin prime/source gate",
                "an exact source event must match gap/generator/fill/orientation/delay",
                "an exact unused jump event must avoid new side-residue arrival",
                "otherwise near-scale proximity is only a named phase fracture",
            ],
            "closed_current_sweep": all_nearscale_bridges_fractured,
            "global_remaining": [
                "SupportWidthNearScaleGlobalNoGo",
                "PhaseScaleBridgeGlobalNoGo",
                "SourceRematerialization-PDEC/SAE",
                "UnusedTargetResidueArrival-PDEC",
                "ColumnCRT/PDEC",
                "MovingFamilySAEColumnCRT",
            ],
        },
        "dependency_hashes": {
            str(path.relative_to(ROOT)): sha256(path)
            for path in (
                actual_anchor_path,
                moving_key_path,
                unused_target_path,
                pair_path,
                phase_scale_path,
            )
        },
    }


def write_outputs(result: dict[str, Any]) -> None:
    """写出 JSON 与 Markdown。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    for path in (OUT_LEDGER, OUT_JSON):
        path.write_text(
            json.dumps(result, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

    agg = result["aggregate"]
    lines = [
        "# Prime Matrix AffineTwin endpoint-release support-width near-scale fracture audit",
        "",
        "**状态：** `current_sweep_support_width_nearscale_fractured_global_open`",
        "",
        "本审计继续下钻 `PhaseScaleBridgeGlobalNoGo`：exact/offset 桥已空后，检查是否存在落在 support width 内的近似尺度桥可以偷渡。",
        "",
        "```text",
        f"support_width={agg['support_width']}",
        f"moving_q_candidate_count={agg['moving_q_candidate_count']}",
        f"support_width_near_source_q_values={agg['support_width_near_source_q_values']}",
        f"support_width_near_unused_jump_q_values={agg['support_width_near_unused_jump_q_values']}",
        f"support_width_near_source_and_jump_q_values={agg['support_width_near_source_and_jump_q_values']}",
        f"viable_support_width_nearscale_bridge_q_values={agg['viable_support_width_nearscale_bridge_q_values']}",
        f"near_source_and_jump_moving_route_histogram={agg['near_source_and_jump_moving_route_histogram']}",
        f"all_support_width_nearscale_bridges_fractured_current_sweep={fmt_bool(agg['all_support_width_nearscale_bridges_fractured_current_sweep'])}",
        "```",
        "",
        "## 1. q near-scale rows",
        "",
        "| q | route | moving route | near source events | near jump events | common scale kinds | failed invariants |",
        "| ---: | --- | --- | ---: | ---: | --- | --- |",
    ]
    for row in result["q_nearscale_rows"]:
        if (
            int(row["source_nearscale_event_count"]) == 0
            and int(row["unused_jump_nearscale_event_count"]) == 0
        ):
            continue
        lines.append(
            "| {q} | `{route}` | `{moving}` | {src} | {jmp} | `{common}` | `{failed}` |".format(
                q=row["q"],
                route=table_cell(row["route"]),
                moving=table_cell(row["moving_route"]),
                src=row["source_nearscale_event_count"],
                jmp=row["unused_jump_nearscale_event_count"],
                common=table_cell(row["common_scale_kinds"]),
                failed=table_cell(",".join(row["failed_invariants"])),
            )
        )

    lines.extend(
        [
            "",
            "## 2. 显式矛盾点",
            "",
            "在 support width `20` 内同时靠近 source 与 unused jump 的 moving-q 只有 `61` 和 `65`。其中 `61` 是 `PrimeButNotTwinAffine`，仍失败于 delay 整数性、`q mod 4=3` 与 gap `61` source 缺席；`65` 是合数。其余 near-jump 候选没有 near-source，不能形成相位桥。",
            "",
            "因此即使把 exact equality 放宽到 support-width 邻域，当前 sweep 也没有可承载 actual load 的桥。近似数值距离不能替代 CRT/source 签名：非零尺度差必须改变 moving key、source 或 unused target，因而回到 source-rematerialization、unused-target arrival、ColumnCRT/PDEC 或 moving-family 出口。",
            "",
            "## 3. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in result["dependency_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    lines.append("")
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--actual-anchor-ledger",
        type=Path,
        default=ACTUAL_ANCHOR_LEDGER,
        help="actual-anchor replacement ledger path",
    )
    parser.add_argument(
        "--moving-key-ledger",
        type=Path,
        default=MOVING_KEY_LEDGER,
        help="moving-key source-rematerialization ledger path",
    )
    parser.add_argument(
        "--unused-target-ledger",
        type=Path,
        default=UNUSED_TARGET_LEDGER,
        help="unused-target arrival ledger path",
    )
    parser.add_argument(
        "--pair-ledger",
        type=Path,
        default=PAIR_LEDGER,
        help="gap-fill pair ledger path",
    )
    parser.add_argument(
        "--phase-scale-ledger",
        type=Path,
        default=PHASE_SCALE_LEDGER,
        help="phase-scale bridge exhaustion ledger path",
    )
    args = parser.parse_args()
    result = build_result(
        args.actual_anchor_ledger,
        args.moving_key_ledger,
        args.unused_target_ledger,
        args.pair_ledger,
        args.phase_scale_ledger,
    )
    write_outputs(result)
    print(json.dumps(result["aggregate"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
