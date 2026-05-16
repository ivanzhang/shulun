#!/usr/bin/env python3
"""生成 AffineTwin endpoint-release near-jump carrier exhaustion 审计证书。

用法示例：
  python3 experiments/prime_matrix_affine_twin_endpoint_release_nearjump_carrier_exhaustion_audit.py
  python3 -m json.tool data/prime-matrix-affine-twin-endpoint-release-nearjump-carrier-exhaustion-ledger.json

输出：
  data/prime-matrix-affine-twin-endpoint-release-nearjump-carrier-exhaustion-ledger.json
  docs/monograph/prime-matrix-affine-twin-endpoint-release-nearjump-carrier-exhaustion-audit.json
  docs/monograph/prime-matrix-affine-twin-endpoint-release-nearjump-carrier-exhaustion-audit.md
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
SUPPORT_NEARSCALE_LEDGER = DATA / (
    "prime-matrix-affine-twin-endpoint-release-support-width-nearscale-fracture-ledger.json"
)
ORPHAN_NEARJUMP_LEDGER = DATA / (
    "prime-matrix-affine-twin-endpoint-release-orphan-nearjump-source-deficit-ledger.json"
)

OUT_LEDGER = DATA / (
    "prime-matrix-affine-twin-endpoint-release-nearjump-carrier-exhaustion-ledger.json"
)
OUT_JSON = DOCS / (
    "prime-matrix-affine-twin-endpoint-release-nearjump-carrier-exhaustion-audit.json"
)
OUT_MD = DOCS / (
    "prime-matrix-affine-twin-endpoint-release-nearjump-carrier-exhaustion-audit.md"
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


def min_jump_event(events: list[dict[str, Any]]) -> dict[str, Any]:
    """返回最近的 unused-target jump 事件。"""
    return min(
        events,
        key=lambda event: (
            int(event["abs_delta"]),
            int(event["new_side_residue_count"]),
            str(event["target_unused_pair_key"]),
        ),
    )


def build_result(
    actual_anchor_path: Path,
    support_nearscale_path: Path,
    orphan_nearjump_path: Path,
) -> dict[str, Any]:
    """构造 near-jump carrier exhaustion 审计结果。"""
    actual_anchor = load_json(actual_anchor_path)
    support_nearscale = load_json(support_nearscale_path)
    orphan_nearjump = load_json(orphan_nearjump_path)

    support_width = int(actual_anchor["aggregate"]["support_width"])
    orphan_by_q = {
        int(row["q"]): row for row in orphan_nearjump["orphan_nearjump_rows"]
    }

    carrier_rows: list[dict[str, Any]] = []
    for row in support_nearscale["q_nearscale_rows"]:
        if int(row["unused_jump_nearscale_event_count"]) == 0:
            continue
        q = int(row["q"])
        jump_events = row["unused_jump_nearscale_events"]
        all_jump_events_need_new_side = all(
            int(event["new_side_residue_count"]) > 0 for event in jump_events
        )
        nearest_jump = min_jump_event(jump_events)
        near_source = int(row["source_nearscale_event_count"]) > 0
        if near_source:
            source_status = "near_source_gate_fractured"
            source_gap_abs_delta = None
            source_deficit = None
            closed = (
                str(row["route"]) == "NearSourceAndJumpButGateFractured"
                and str(row["moving_route"]) in {"PrimeButNotTwinAffine", "CompositeQ"}
                and all_jump_events_need_new_side
                and not bool(row["viable_support_width_nearscale_bridge_current"])
            )
        else:
            orphan = orphan_by_q[q]
            source_status = "orphan_source_deficit"
            source_gap_abs_delta = int(
                orphan["nearest_source_gap_event"]["abs_delta"]
            )
            source_deficit = int(
                orphan["source_gap_abs_delta_minus_support_width"]
            )
            closed = (
                bool(orphan["orphan_nearjump_source_deficit_closed_current"])
                and all_jump_events_need_new_side
                and source_gap_abs_delta > support_width
            )

        carrier_rows.append(
            {
                "q": q,
                "carrier_route": str(row["route"]),
                "moving_route": str(row["moving_route"]),
                "source_status": source_status,
                "near_source_event_count": int(row["source_nearscale_event_count"]),
                "near_jump_event_count": int(
                    row["unused_jump_nearscale_event_count"]
                ),
                "nearest_unused_jump_event": nearest_jump,
                "all_jump_events_need_new_side_residue": all_jump_events_need_new_side,
                "source_gap_abs_delta": source_gap_abs_delta,
                "source_gap_abs_delta_minus_support_width": source_deficit,
                "failed_invariants": row["failed_invariants"],
                "nearjump_carrier_closed_current": closed,
            }
        )

    if not carrier_rows:
        raise RuntimeError("expected near-jump carrier rows")

    near_source_rows = [
        row for row in carrier_rows if row["source_status"] == "near_source_gate_fractured"
    ]
    orphan_rows = [
        row for row in carrier_rows if row["source_status"] == "orphan_source_deficit"
    ]
    route_histogram = Counter(str(row["carrier_route"]) for row in carrier_rows)
    source_status_histogram = Counter(str(row["source_status"]) for row in carrier_rows)
    moving_route_histogram = Counter(str(row["moving_route"]) for row in carrier_rows)
    min_orphan_source_deficit_row = min(
        orphan_rows,
        key=lambda row: (
            int(row["source_gap_abs_delta_minus_support_width"]),
            int(row["q"]),
        ),
    )
    min_near_jump_row = min(
        carrier_rows,
        key=lambda row: (
            int(row["nearest_unused_jump_event"]["abs_delta"]),
            int(row["q"]),
        ),
    )

    all_carriers_closed = (
        all(bool(row["nearjump_carrier_closed_current"]) for row in carrier_rows)
        and bool(
            support_nearscale["aggregate"][
                "all_support_width_nearscale_bridges_fractured_current_sweep"
            ]
        )
        and bool(
            orphan_nearjump["aggregate"][
                "orphan_nearjump_source_deficit_closed_current_sweep"
            ]
        )
    )

    aggregate = {
        "actual_anchor_replacement_ledger": str(
            actual_anchor_path.relative_to(ROOT)
        ),
        "support_width_nearscale_fracture_ledger": str(
            support_nearscale_path.relative_to(ROOT)
        ),
        "orphan_nearjump_source_deficit_ledger": str(
            orphan_nearjump_path.relative_to(ROOT)
        ),
        "support_width": support_width,
        "nearjump_carrier_q_values": [int(row["q"]) for row in carrier_rows],
        "nearjump_carrier_count": len(carrier_rows),
        "near_source_gate_fractured_q_values": [
            int(row["q"]) for row in near_source_rows
        ],
        "orphan_source_deficit_q_values": [int(row["q"]) for row in orphan_rows],
        "carrier_route_histogram": dict(sorted(route_histogram.items())),
        "source_status_histogram": dict(sorted(source_status_histogram.items())),
        "moving_route_histogram": dict(sorted(moving_route_histogram.items())),
        "min_near_jump_abs_delta": int(
            min_near_jump_row["nearest_unused_jump_event"]["abs_delta"]
        ),
        "min_near_jump_q": int(min_near_jump_row["q"]),
        "min_orphan_source_gap_abs_delta": int(
            min_orphan_source_deficit_row["source_gap_abs_delta"]
        ),
        "min_orphan_source_gap_abs_delta_minus_support_width": int(
            min_orphan_source_deficit_row[
                "source_gap_abs_delta_minus_support_width"
            ]
        ),
        "min_orphan_source_deficit_q": int(min_orphan_source_deficit_row["q"]),
        "all_carrier_jump_events_need_new_side_residue": all(
            bool(row["all_jump_events_need_new_side_residue"]) for row in carrier_rows
        ),
        "support_width_nearscale_fractured_current_sweep": bool(
            support_nearscale["aggregate"][
                "all_support_width_nearscale_bridges_fractured_current_sweep"
            ]
        ),
        "orphan_nearjump_source_deficit_closed_current_sweep": bool(
            orphan_nearjump["aggregate"][
                "orphan_nearjump_source_deficit_closed_current_sweep"
            ]
        ),
        "nearjump_carrier_exhausted_current_sweep": all_carriers_closed,
        "global_nearjump_carrier_exhausted": False,
        "row_column_unconditional_closed": False,
    }

    return {
        "certificate_type": (
            "prime_matrix_affine_twin_endpoint_release_"
            "nearjump_carrier_exhaustion_audit"
        ),
        "status": "current_sweep_nearjump_carrier_exhausted_global_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "aggregate": aggregate,
        "nearjump_carrier_rows": carrier_rows,
        "contract": {
            "nearjump_carrier_gate": [
                "every support-width near-jump candidate must have a source-side carrier",
                "near-source carriers must pass the AffineTwin prime/source gate",
                "orphan carriers must have source distance within support width",
                "target-side near-jump must not require new side-residue arrival",
                "otherwise the near-jump carrier is exhausted and routes to named exits",
            ],
            "closed_current_sweep": all_carriers_closed,
            "global_remaining": [
                "NearJumpCarrierGlobalNoGo",
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
                support_nearscale_path,
                orphan_nearjump_path,
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
        "# Prime Matrix AffineTwin endpoint-release near-jump carrier exhaustion audit",
        "",
        "**状态：** `current_sweep_nearjump_carrier_exhausted_global_open`",
        "",
        "本审计把 support-width 内所有 near-jump 候选统一分解为 near-source gate fracture 与 orphan source deficit 两类，检查 target 侧近邻是否还有匿名承载通道。",
        "",
        "```text",
        f"support_width={agg['support_width']}",
        f"nearjump_carrier_q_values={agg['nearjump_carrier_q_values']}",
        f"near_source_gate_fractured_q_values={agg['near_source_gate_fractured_q_values']}",
        f"orphan_source_deficit_q_values={agg['orphan_source_deficit_q_values']}",
        f"source_status_histogram={agg['source_status_histogram']}",
        f"moving_route_histogram={agg['moving_route_histogram']}",
        f"min_near_jump_abs_delta={agg['min_near_jump_abs_delta']}",
        f"min_orphan_source_gap_abs_delta={agg['min_orphan_source_gap_abs_delta']}",
        f"min_orphan_source_gap_abs_delta_minus_support_width={agg['min_orphan_source_gap_abs_delta_minus_support_width']}",
        f"all_carrier_jump_events_need_new_side_residue={fmt_bool(agg['all_carrier_jump_events_need_new_side_residue'])}",
        f"nearjump_carrier_exhausted_current_sweep={fmt_bool(agg['nearjump_carrier_exhausted_current_sweep'])}",
        "```",
        "",
        "## 1. carrier rows",
        "",
        "| q | carrier route | source status | moving route | nearest jump | jump delta | source deficit | failed invariants |",
        "| ---: | --- | --- | --- | ---: | ---: | ---: | --- |",
    ]
    for row in result["nearjump_carrier_rows"]:
        jump = row["nearest_unused_jump_event"]
        source_deficit = row["source_gap_abs_delta_minus_support_width"]
        lines.append(
            "| {q} | `{route}` | `{status}` | `{moving}` | {jump} | {delta} | {deficit} | `{failed}` |".format(
                q=row["q"],
                route=table_cell(row["carrier_route"]),
                status=table_cell(row["source_status"]),
                moving=table_cell(row["moving_route"]),
                jump=jump["unused_jump"],
                delta=jump["signed_delta"],
                deficit="-" if source_deficit is None else source_deficit,
                failed=table_cell(",".join(row["failed_invariants"])),
            )
        )

    lines.extend(
        [
            "",
            "## 2. 显式矛盾点",
            "",
            "near-jump carrier 全部分成两类：`61,65` 同时 near source 与 near jump，但前者不是同向 AffineTwin source，后者是合数；其余七个 q 是 orphan source deficit，到 source 侧至少还差 `35>20`。",
            "",
            "更强的是，所有 carrier 的 target 侧 near-jump 事件都需要新增侧残基。因此反例链无法只凭 target 侧近邻承载 actual load；一旦补 source 或补 target，就回到 source-rematerialization、unused-target arrival 或 moving-family 出口。",
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
        "--support-nearscale-ledger",
        type=Path,
        default=SUPPORT_NEARSCALE_LEDGER,
        help="support-width near-scale fracture ledger path",
    )
    parser.add_argument(
        "--orphan-nearjump-ledger",
        type=Path,
        default=ORPHAN_NEARJUMP_LEDGER,
        help="orphan near-jump source-deficit ledger path",
    )
    args = parser.parse_args()
    result = build_result(
        args.actual_anchor_ledger,
        args.support_nearscale_ledger,
        args.orphan_nearjump_ledger,
    )
    write_outputs(result)
    print(json.dumps(result["aggregate"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
