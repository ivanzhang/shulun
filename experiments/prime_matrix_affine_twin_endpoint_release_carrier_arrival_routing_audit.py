#!/usr/bin/env python3
"""生成 AffineTwin endpoint-release carrier-arrival routing 审计证书。

用法示例：
  python3 experiments/prime_matrix_affine_twin_endpoint_release_carrier_arrival_routing_audit.py
  python3 -m json.tool data/prime-matrix-affine-twin-endpoint-release-carrier-arrival-routing-ledger.json

输出：
  data/prime-matrix-affine-twin-endpoint-release-carrier-arrival-routing-ledger.json
  docs/monograph/prime-matrix-affine-twin-endpoint-release-carrier-arrival-routing-audit.json
  docs/monograph/prime-matrix-affine-twin-endpoint-release-carrier-arrival-routing-audit.md
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

SUPPORT_NEARSCALE_LEDGER = DATA / (
    "prime-matrix-affine-twin-endpoint-release-support-width-nearscale-fracture-ledger.json"
)
NEARJUMP_CARRIER_LEDGER = DATA / (
    "prime-matrix-affine-twin-endpoint-release-nearjump-carrier-exhaustion-ledger.json"
)
UNUSED_TARGET_ARRIVAL_LEDGER = DATA / (
    "prime-matrix-affine-twin-unused-target-arrival-ledger.json"
)

OUT_LEDGER = DATA / (
    "prime-matrix-affine-twin-endpoint-release-carrier-arrival-routing-ledger.json"
)
OUT_JSON = DOCS / (
    "prime-matrix-affine-twin-endpoint-release-carrier-arrival-routing-audit.json"
)
OUT_MD = DOCS / (
    "prime-matrix-affine-twin-endpoint-release-carrier-arrival-routing-audit.md"
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


def arrival_key_from_event(event: dict[str, Any]) -> tuple[str, str, int]:
    """把 near-jump event 规范成 unused-target arrival 键。"""
    return (
        str(event["source_pair_key"]),
        str(event["target_unused_pair_key"]),
        int(event["unused_jump"]),
    )


def arrival_key_from_row(row: dict[str, Any]) -> tuple[str, str, int]:
    """把 unused-target arrival row 规范成匹配键。"""
    return (
        str(row["source_pair_key"]),
        str(row["target_unused_pair_key"]),
        int(row["abs_crt_jump_to_unused_target"]),
    )


def build_result(
    support_nearscale_path: Path,
    nearjump_carrier_path: Path,
    unused_target_arrival_path: Path,
) -> dict[str, Any]:
    """构造 carrier-arrival routing 审计结果。"""
    support_nearscale = load_json(support_nearscale_path)
    nearjump_carrier = load_json(nearjump_carrier_path)
    unused_target_arrival = load_json(unused_target_arrival_path)

    carrier_q_values = {
        int(q) for q in nearjump_carrier["aggregate"]["nearjump_carrier_q_values"]
    }
    carrier_source_status = {
        int(row["q"]): str(row["source_status"])
        for row in nearjump_carrier["nearjump_carrier_rows"]
    }
    arrival_by_key = {
        arrival_key_from_row(row): row
        for row in unused_target_arrival["unused_target_arrival_rows"]
    }

    event_rows: list[dict[str, Any]] = []
    missing_keys: list[dict[str, Any]] = []
    used_arrival_keys: set[tuple[str, str, int]] = set()

    for row in support_nearscale["q_nearscale_rows"]:
        q = int(row["q"])
        if q not in carrier_q_values:
            continue
        for event in row["unused_jump_nearscale_events"]:
            key = arrival_key_from_event(event)
            arrival = arrival_by_key.get(key)
            if arrival is None:
                missing_keys.append(
                    {
                        "q": q,
                        "source_pair_key": key[0],
                        "target_unused_pair_key": key[1],
                        "unused_jump": key[2],
                    }
                )
                matched = False
                needs_new_generator = None
                needs_new_fill = None
                target_formal = None
                target_supported_actual = None
                target_residue_l1 = None
            else:
                used_arrival_keys.add(key)
                matched = True
                needs_new_generator = bool(arrival["needs_new_generator_residue"])
                needs_new_fill = bool(arrival["needs_new_fill_residue"])
                target_formal = bool(arrival["target_pair_currently_formal"])
                target_supported_actual = bool(
                    arrival["target_pair_currently_supported_actual"]
                )
                target_residue_l1 = int(arrival["residue_l1_displacement"])

            event_rows.append(
                {
                    "q": q,
                    "moving_route": str(row["moving_route"]),
                    "source_status": carrier_source_status[q],
                    "scale_kind": str(event["scale_kind"]),
                    "scale_value": int(event["scale_value"]),
                    "unused_jump": int(event["unused_jump"]),
                    "signed_delta": int(event["signed_delta"]),
                    "abs_delta": int(event["abs_delta"]),
                    "source_pair_key": str(event["source_pair_key"]),
                    "target_unused_pair_key": str(event["target_unused_pair_key"]),
                    "new_side_residue_count": int(event["new_side_residue_count"]),
                    "matched_unused_target_arrival": matched,
                    "target_needs_new_generator_residue": needs_new_generator,
                    "target_needs_new_fill_residue": needs_new_fill,
                    "target_pair_currently_formal": target_formal,
                    "target_pair_currently_supported_actual": target_supported_actual,
                    "target_residue_l1_displacement": target_residue_l1,
                }
            )

    if not event_rows:
        raise RuntimeError("expected carrier arrival event rows")

    matched_arrivals = [arrival_by_key[key] for key in sorted(used_arrival_keys)]
    exact_zero_phase_rows = [row for row in event_rows if int(row["abs_delta"]) == 0]
    new_side_histogram = Counter(
        int(row["new_side_residue_count"]) for row in event_rows
    )
    target_pair_histogram = Counter(
        str(row["target_unused_pair_key"]) for row in event_rows
    )
    event_count_by_q = Counter(int(row["q"]) for row in event_rows)

    required_generator_residues = sorted(
        {
            int(row["target_generator_residue"])
            for row in matched_arrivals
            if bool(row["needs_new_generator_residue"])
        }
    )
    required_fill_residues = sorted(
        {
            int(row["target_fill_residue"])
            for row in matched_arrivals
            if bool(row["needs_new_fill_residue"])
        }
    )

    all_events_match = len(missing_keys) == 0
    all_events_need_new_side = all(
        int(row["new_side_residue_count"]) > 0 for row in event_rows
    )
    all_targets_outside_formal = all(
        row["target_pair_currently_formal"] is False for row in event_rows
    )
    all_targets_not_supported_actual = all(
        row["target_pair_currently_supported_actual"] is False for row in event_rows
    )
    closed_current = (
        all_events_match
        and all_events_need_new_side
        and all_targets_outside_formal
        and all_targets_not_supported_actual
        and bool(
            nearjump_carrier["aggregate"][
                "nearjump_carrier_exhausted_current_sweep"
            ]
        )
        and bool(
            unused_target_arrival["aggregate"][
                "unused_target_arrival_closed_current_sweep"
            ]
        )
    )

    aggregate = {
        "support_width_nearscale_fracture_ledger": str(
            support_nearscale_path.relative_to(ROOT)
        ),
        "nearjump_carrier_exhaustion_ledger": str(
            nearjump_carrier_path.relative_to(ROOT)
        ),
        "unused_target_arrival_ledger": str(
            unused_target_arrival_path.relative_to(ROOT)
        ),
        "support_width": int(support_nearscale["aggregate"]["support_width"]),
        "carrier_q_values": sorted(carrier_q_values),
        "carrier_event_count": len(event_rows),
        "carrier_event_count_by_q": dict(sorted(event_count_by_q.items())),
        "unique_arrival_atom_count_used_by_carriers": len(used_arrival_keys),
        "unused_target_arrival_candidate_count": int(
            unused_target_arrival["aggregate"][
                "unused_target_arrival_candidate_count"
            ]
        ),
        "unique_target_pair_count_used_by_carriers": len(target_pair_histogram),
        "target_pair_histogram": dict(sorted(target_pair_histogram.items())),
        "carrier_event_new_side_residue_requirement_total": sum(
            int(row["new_side_residue_count"]) for row in event_rows
        ),
        "carrier_event_new_side_residue_histogram": dict(
            sorted(new_side_histogram.items())
        ),
        "required_new_generator_residues": required_generator_residues,
        "required_new_fill_residues": required_fill_residues,
        "required_unique_side_residue_arrival_count": len(
            set(required_generator_residues) | set(required_fill_residues)
        ),
        "min_carrier_abs_delta": min(int(row["abs_delta"]) for row in event_rows),
        "max_carrier_abs_delta": max(int(row["abs_delta"]) for row in event_rows),
        "exact_zero_phase_event_count": len(exact_zero_phase_rows),
        "exact_zero_phase_events_need_new_side_residue": all(
            int(row["new_side_residue_count"]) > 0 for row in exact_zero_phase_rows
        ),
        "missing_unused_target_arrival_match_count": len(missing_keys),
        "all_carrier_events_match_closed_unused_target_arrival": all_events_match,
        "all_carrier_events_need_new_side_residue": all_events_need_new_side,
        "all_carrier_targets_outside_current_formal_product": all_targets_outside_formal,
        "all_carrier_targets_not_supported_actual_current_sweep": (
            all_targets_not_supported_actual
        ),
        "nearjump_carrier_exhausted_current_sweep": bool(
            nearjump_carrier["aggregate"][
                "nearjump_carrier_exhausted_current_sweep"
            ]
        ),
        "unused_target_arrival_closed_current_sweep": bool(
            unused_target_arrival["aggregate"][
                "unused_target_arrival_closed_current_sweep"
            ]
        ),
        "carrier_arrival_routed_current_sweep": closed_current,
        "global_carrier_arrival_no_go_proved": False,
        "row_column_unconditional_closed": False,
    }

    return {
        "certificate_type": (
            "prime_matrix_affine_twin_endpoint_release_"
            "carrier_arrival_routing_audit"
        ),
        "status": "current_sweep_carrier_arrival_routed_global_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "aggregate": aggregate,
        "carrier_arrival_event_rows": sorted(
            event_rows,
            key=lambda row: (
                int(row["q"]),
                int(row["abs_delta"]),
                str(row["target_unused_pair_key"]),
                str(row["scale_kind"]),
            ),
        ),
        "missing_unused_target_arrival_matches": missing_keys,
        "contract": {
            "carrier_arrival_routing_gate": [
                "every near-jump carrier target event must match a registered unused-target arrival atom",
                "the matched target must be outside the current formal product and current actual support",
                "the matched event must require at least one new side residue",
                "otherwise the carrier target side would contain an anonymous absorption channel",
            ],
            "closed_current_sweep": closed_current,
            "global_remaining": [
                "GlobalUnusedTargetResidueArrivalBound",
                "NewGeneratorResidueArrival-PDEC/SAE",
                "NewFillResidueArrival-PDEC/SAE",
                "SourceRematerialization-PDEC/SAE",
                "ColumnCRT/PDEC",
                "MovingFamilySAEColumnCRT",
            ],
        },
        "dependency_hashes": {
            str(path.relative_to(ROOT)): sha256(path)
            for path in (
                support_nearscale_path,
                nearjump_carrier_path,
                unused_target_arrival_path,
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
        "# Prime Matrix AffineTwin endpoint-release carrier-arrival routing audit",
        "",
        "**状态：** `current_sweep_carrier_arrival_routed_global_open`",
        "",
        "本审计把 near-jump carrier 的 target 侧近邻事件逐个路由到 unused-target arrival 账本，检查是否存在未登记的匿名 target 侧承载通道。",
        "",
        "```text",
        f"carrier_q_values={agg['carrier_q_values']}",
        f"carrier_event_count={agg['carrier_event_count']}",
        f"unique_arrival_atom_count_used_by_carriers={agg['unique_arrival_atom_count_used_by_carriers']}",
        f"target_pair_histogram={agg['target_pair_histogram']}",
        f"carrier_event_new_side_residue_requirement_total={agg['carrier_event_new_side_residue_requirement_total']}",
        f"carrier_event_new_side_residue_histogram={agg['carrier_event_new_side_residue_histogram']}",
        f"required_new_generator_residues={agg['required_new_generator_residues']}",
        f"required_new_fill_residues={agg['required_new_fill_residues']}",
        f"exact_zero_phase_event_count={agg['exact_zero_phase_event_count']}",
        f"missing_unused_target_arrival_match_count={agg['missing_unused_target_arrival_match_count']}",
        f"all_carrier_events_match_closed_unused_target_arrival={fmt_bool(agg['all_carrier_events_match_closed_unused_target_arrival'])}",
        f"all_carrier_targets_not_supported_actual_current_sweep={fmt_bool(agg['all_carrier_targets_not_supported_actual_current_sweep'])}",
        f"carrier_arrival_routed_current_sweep={fmt_bool(agg['carrier_arrival_routed_current_sweep'])}",
        "```",
        "",
        "## 1. carrier-arrival rows",
        "",
        "| q | route | scale | jump | delta | source | target | new side | matched | target actual |",
        "| ---: | --- | --- | ---: | ---: | --- | --- | ---: | --- | --- |",
    ]
    for row in result["carrier_arrival_event_rows"]:
        lines.append(
            "| {q} | `{route}` | `{scale}` | {jump} | {delta} | `{source}` | `{target}` | {new_side} | {matched} | {actual} |".format(
                q=row["q"],
                route=table_cell(row["moving_route"]),
                scale=table_cell(f"{row['scale_kind']}={row['scale_value']}"),
                jump=row["unused_jump"],
                delta=row["signed_delta"],
                source=table_cell(row["source_pair_key"]),
                target=table_cell(row["target_unused_pair_key"]),
                new_side=row["new_side_residue_count"],
                matched=fmt_bool(row["matched_unused_target_arrival"]),
                actual=fmt_bool(row["target_pair_currently_supported_actual"]),
            )
        )

    lines.extend(
        [
            "",
            "## 2. 显式矛盾点",
            "",
            "27 个 carrier target 侧近邻事件全部匹配到已登记的 9 个 unused-target arrival 原子，缺失匹配数为 `0`。这些 target pair 全部不在当前形式积，也不被当前 actual support 支持。",
            "",
            "唯一 exact zero phase 事件是 `q=61, q-2=59, jump=59`，但它仍对应 `19:12 -> 20:9`，需要新增 generator residue `20`，且 source gate 已在 `61/59` phase-fracture 中失败。因此“相位正好贴住 target jump”仍不能生成真实链 actual load。",
            "",
            "carrier 侧总共出现 `50` 次事件级新侧残基需求，压缩为 generator residues `[10,16,17,18,20]` 与 fill residues `[5,6,7,30]`。所以 target 侧若要复现，只能进入全局新残基到达率控制或命名 `PDEC/SAE/ColumnCRT` 出口。",
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
        "--support-nearscale-ledger",
        type=Path,
        default=SUPPORT_NEARSCALE_LEDGER,
        help="support-width near-scale fracture ledger path",
    )
    parser.add_argument(
        "--nearjump-carrier-ledger",
        type=Path,
        default=NEARJUMP_CARRIER_LEDGER,
        help="near-jump carrier exhaustion ledger path",
    )
    parser.add_argument(
        "--unused-target-arrival-ledger",
        type=Path,
        default=UNUSED_TARGET_ARRIVAL_LEDGER,
        help="unused-target arrival ledger path",
    )
    args = parser.parse_args()
    result = build_result(
        args.support_nearscale_ledger,
        args.nearjump_carrier_ledger,
        args.unused_target_arrival_ledger,
    )
    write_outputs(result)
    print(json.dumps(result["aggregate"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
