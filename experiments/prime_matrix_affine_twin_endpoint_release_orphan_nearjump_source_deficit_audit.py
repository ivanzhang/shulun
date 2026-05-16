#!/usr/bin/env python3
"""生成 AffineTwin endpoint-release orphan near-jump source-deficit 审计证书。

用法示例：
  python3 experiments/prime_matrix_affine_twin_endpoint_release_orphan_nearjump_source_deficit_audit.py
  python3 -m json.tool data/prime-matrix-affine-twin-endpoint-release-orphan-nearjump-source-deficit-ledger.json

输出：
  data/prime-matrix-affine-twin-endpoint-release-orphan-nearjump-source-deficit-ledger.json
  docs/monograph/prime-matrix-affine-twin-endpoint-release-orphan-nearjump-source-deficit-audit.json
  docs/monograph/prime-matrix-affine-twin-endpoint-release-orphan-nearjump-source-deficit-audit.md
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
SUPPORT_NEARSCALE_LEDGER = DATA / (
    "prime-matrix-affine-twin-endpoint-release-support-width-nearscale-fracture-ledger.json"
)

OUT_LEDGER = DATA / (
    "prime-matrix-affine-twin-endpoint-release-orphan-nearjump-source-deficit-ledger.json"
)
OUT_JSON = DOCS / (
    "prime-matrix-affine-twin-endpoint-release-orphan-nearjump-source-deficit-audit.json"
)
OUT_MD = DOCS / (
    "prime-matrix-affine-twin-endpoint-release-orphan-nearjump-source-deficit-audit.md"
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


def moving_index(rows: list[dict[str, Any]]) -> dict[int, dict[str, Any]]:
    """按 q 建立 moving-key 行索引。"""
    return {int(row["q"]): row for row in rows}


def nearest_source_gap(q: int, gap_values: list[int]) -> dict[str, Any]:
    """返回 q 或 q-2 到已有 gap source 的最近距离。"""
    candidates: list[dict[str, Any]] = []
    for scale_kind, scale_value in (("q", q), ("q_minus_2", q - 2)):
        for gap in gap_values:
            delta = int(gap) - scale_value
            candidates.append(
                {
                    "scale_kind": scale_kind,
                    "scale_value": scale_value,
                    "source_gap": int(gap),
                    "signed_delta": delta,
                    "abs_delta": abs(delta),
                }
            )
    return min(
        candidates,
        key=lambda row: (
            int(row["abs_delta"]),
            0 if row["scale_kind"] == "q_minus_2" else 1,
            int(row["source_gap"]),
        ),
    )


def nearest_jump_event(events: list[dict[str, Any]]) -> dict[str, Any]:
    """返回 orphan near-jump 的最近 unused jump 事件。"""
    return min(
        events,
        key=lambda row: (
            int(row["abs_delta"]),
            int(row["new_side_residue_count"]),
            str(row["target_unused_pair_key"]),
        ),
    )


def build_result(
    actual_anchor_path: Path,
    moving_key_path: Path,
    unused_target_path: Path,
    pair_path: Path,
    support_nearscale_path: Path,
) -> dict[str, Any]:
    """构造 orphan near-jump source-deficit 审计结果。"""
    actual_anchor = load_json(actual_anchor_path)
    moving_key = load_json(moving_key_path)
    unused_target = load_json(unused_target_path)
    pair = load_json(pair_path)
    support_nearscale = load_json(support_nearscale_path)

    support_width = int(actual_anchor["aggregate"]["support_width"])
    gap_values = sorted({int(row["gap_ell"]) for row in pair["gap_fill_pair_rows"]})
    moving_by_q = moving_index(moving_key["candidate_q_source_rematerialization_rows"])

    orphan_rows: list[dict[str, Any]] = []
    for row in support_nearscale["q_nearscale_rows"]:
        if str(row["route"]) != "NearJumpOnly":
            continue
        q = int(row["q"])
        moving_row = moving_by_q[q]
        nearest_source = nearest_source_gap(q, gap_values)
        nearest_jump = nearest_jump_event(row["unused_jump_nearscale_events"])
        all_jump_events_need_new_side = all(
            int(event["new_side_residue_count"]) > 0
            for event in row["unused_jump_nearscale_events"]
        )
        source_deficit = int(nearest_source["abs_delta"]) - support_width
        orphan_rows.append(
            {
                "q": q,
                "moving_route": str(row["moving_route"]),
                "source_pair_keys": row["source_pair_keys"],
                "failed_invariants": row["failed_invariants"],
                "prime_gate": moving_row["prime_gate"],
                "moving_key_source_rematerialized_current": bool(
                    moving_row["moving_key_source_rematerialized_current"]
                ),
                "nearest_unused_jump_event": nearest_jump,
                "nearest_source_gap_event": nearest_source,
                "source_gap_abs_delta_minus_support_width": source_deficit,
                "source_gap_abs_delta_to_support_width_ratio": (
                    int(nearest_source["abs_delta"]) / support_width
                ),
                "unused_jump_nearscale_event_count": int(
                    row["unused_jump_nearscale_event_count"]
                ),
                "all_unused_jump_events_need_new_side_residue": (
                    all_jump_events_need_new_side
                ),
                "orphan_nearjump_source_deficit_closed_current": (
                    int(nearest_source["abs_delta"]) > support_width
                    and all_jump_events_need_new_side
                    and not bool(
                        moving_row["moving_key_source_rematerialized_current"]
                    )
                    and not bool(
                        moving_row["prime_gate"]["affine_twin_prime_gate_passed"]
                    )
                ),
            }
        )

    if not orphan_rows:
        raise RuntimeError("expected NearJumpOnly orphan rows")

    min_source_deficit_row = min(
        orphan_rows,
        key=lambda row: (
            int(row["source_gap_abs_delta_minus_support_width"]),
            int(row["q"]),
        ),
    )
    route_histogram = Counter(str(row["moving_route"]) for row in orphan_rows)

    all_orphan_rows_closed = all(
        bool(row["orphan_nearjump_source_deficit_closed_current"])
        for row in orphan_rows
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
        "support_width_nearscale_fracture_ledger": str(
            support_nearscale_path.relative_to(ROOT)
        ),
        "support_width": support_width,
        "available_gap_source_values": gap_values,
        "orphan_nearjump_q_values": [int(row["q"]) for row in orphan_rows],
        "orphan_nearjump_count": len(orphan_rows),
        "orphan_nearjump_moving_route_histogram": dict(
            sorted(route_histogram.items())
        ),
        "min_source_gap_abs_delta": int(
            min_source_deficit_row["nearest_source_gap_event"]["abs_delta"]
        ),
        "min_source_gap_abs_delta_minus_support_width": int(
            min_source_deficit_row["source_gap_abs_delta_minus_support_width"]
        ),
        "min_source_gap_deficit_q": int(min_source_deficit_row["q"]),
        "min_source_gap_deficit_to_support_width_ratio": (
            min_source_deficit_row[
                "source_gap_abs_delta_to_support_width_ratio"
            ]
        ),
        "all_orphan_nearjump_source_gaps_exceed_support_width": all(
            int(row["nearest_source_gap_event"]["abs_delta"]) > support_width
            for row in orphan_rows
        ),
        "all_orphan_nearjump_events_need_new_side_residue": all(
            bool(row["all_unused_jump_events_need_new_side_residue"])
            for row in orphan_rows
        ),
        "all_orphan_nearjump_moving_sources_unmaterialized": all(
            not bool(row["moving_key_source_rematerialized_current"])
            for row in orphan_rows
        ),
        "all_orphan_nearjump_prime_or_source_gates_fail": all(
            not bool(row["prime_gate"]["affine_twin_prime_gate_passed"])
            for row in orphan_rows
        ),
        "orphan_nearjump_source_deficit_closed_current_sweep": (
            all_orphan_rows_closed
        ),
        "global_orphan_nearjump_source_deficit_excluded": False,
        "row_column_unconditional_closed": False,
    }

    return {
        "certificate_type": (
            "prime_matrix_affine_twin_endpoint_release_"
            "orphan_nearjump_source_deficit_audit"
        ),
        "status": "current_sweep_orphan_nearjump_source_deficit_closed_global_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "aggregate": aggregate,
        "orphan_nearjump_rows": orphan_rows,
        "contract": {
            "orphan_nearjump_gate": [
                "near unused-target jump is not enough without a near source",
                "the nearest source scale must be inside the support-width tolerance",
                "the moving q must pass the AffineTwin prime/source gate",
                "the unused-target side must not require a new side residue",
                "otherwise the candidate is an orphan near-jump and returns to source-arrival or unused-target PDEC",
            ],
            "closed_current_sweep": all_orphan_rows_closed,
            "global_remaining": [
                "OrphanNearJumpSourceDeficitGlobalNoGo",
                "SupportWidthNearScaleGlobalNoGo",
                "SourceRematerialization-PDEC/SAE",
                "UnusedTargetResidueArrival-PDEC",
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
                support_nearscale_path,
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
        "# Prime Matrix AffineTwin endpoint-release orphan near-jump source-deficit audit",
        "",
        "**状态：** `current_sweep_orphan_nearjump_source_deficit_closed_global_open`",
        "",
        "本审计继续下钻 support-width near-scale fracture 后的剩余：只靠近 unused-target jump、却不靠近 source 的 orphan near-jump 是否能补成真实相位桥。",
        "",
        "```text",
        f"support_width={agg['support_width']}",
        f"available_gap_source_values={agg['available_gap_source_values']}",
        f"orphan_nearjump_q_values={agg['orphan_nearjump_q_values']}",
        f"orphan_nearjump_moving_route_histogram={agg['orphan_nearjump_moving_route_histogram']}",
        f"min_source_gap_abs_delta={agg['min_source_gap_abs_delta']}",
        f"min_source_gap_abs_delta_minus_support_width={agg['min_source_gap_abs_delta_minus_support_width']}",
        f"min_source_gap_deficit_q={agg['min_source_gap_deficit_q']}",
        f"all_orphan_nearjump_source_gaps_exceed_support_width={fmt_bool(agg['all_orphan_nearjump_source_gaps_exceed_support_width'])}",
        f"all_orphan_nearjump_events_need_new_side_residue={fmt_bool(agg['all_orphan_nearjump_events_need_new_side_residue'])}",
        f"orphan_nearjump_source_deficit_closed_current_sweep={fmt_bool(agg['orphan_nearjump_source_deficit_closed_current_sweep'])}",
        "```",
        "",
        "## 1. orphan rows",
        "",
        "| q | moving route | nearest jump | jump delta | nearest source scale | source gap | source deficit | failed invariants |",
        "| ---: | --- | ---: | ---: | --- | ---: | ---: | --- |",
    ]
    for row in result["orphan_nearjump_rows"]:
        jump = row["nearest_unused_jump_event"]
        source = row["nearest_source_gap_event"]
        lines.append(
            "| {q} | `{route}` | {jump} | {jdelta} | `{scale}` | {sgap} | {deficit} | `{failed}` |".format(
                q=row["q"],
                route=table_cell(row["moving_route"]),
                jump=jump["unused_jump"],
                jdelta=jump["signed_delta"],
                scale=source["scale_kind"],
                sgap=source["source_gap"],
                deficit=row["source_gap_abs_delta_minus_support_width"],
                failed=table_cell(",".join(row["failed_invariants"])),
            )
        )

    lines.extend(
        [
            "",
            "## 2. 显式矛盾点",
            "",
            f"这些 orphan 候选虽然在 unused-target jump 侧落入 support width `{agg['support_width']}`，但到最近 source scale 的距离最小也是 `{agg['min_source_gap_abs_delta']}`，比 support width 还多 `{agg['min_source_gap_abs_delta_minus_support_width']}`。最窄例是 `q={agg['min_source_gap_deficit_q']}`。",
            "",
            "同时所有 orphan near-jump 的 unused-target 事件都需要新增侧残基，且 moving source 均未物化；候选本身也全部失败于合数或 AffineTwin prime/source gate。因此“近 target”不能替代“近 source”，也不能承载 actual load。",
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
        "--support-nearscale-ledger",
        type=Path,
        default=SUPPORT_NEARSCALE_LEDGER,
        help="support-width near-scale fracture ledger path",
    )
    args = parser.parse_args()
    result = build_result(
        args.actual_anchor_ledger,
        args.moving_key_ledger,
        args.unused_target_ledger,
        args.pair_ledger,
        args.support_nearscale_ledger,
    )
    write_outputs(result)
    print(json.dumps(result["aggregate"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
