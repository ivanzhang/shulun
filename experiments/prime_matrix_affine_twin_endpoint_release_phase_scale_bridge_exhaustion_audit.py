#!/usr/bin/env python3
"""生成 AffineTwin endpoint-release phase-scale bridge exhaustion 审计证书。

用法示例：
  python3 experiments/prime_matrix_affine_twin_endpoint_release_phase_scale_bridge_exhaustion_audit.py
  python3 -m json.tool data/prime-matrix-affine-twin-endpoint-release-phase-scale-bridge-exhaustion-ledger.json

输出：
  data/prime-matrix-affine-twin-endpoint-release-phase-scale-bridge-exhaustion-ledger.json
  docs/monograph/prime-matrix-affine-twin-endpoint-release-phase-scale-bridge-exhaustion-audit.json
  docs/monograph/prime-matrix-affine-twin-endpoint-release-phase-scale-bridge-exhaustion-audit.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
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
NEAR_MISS_LEDGER = DATA / (
    "prime-matrix-affine-twin-endpoint-release-near-miss-61-59-phase-fracture-ledger.json"
)

OUT_LEDGER = DATA / (
    "prime-matrix-affine-twin-endpoint-release-phase-scale-bridge-exhaustion-ledger.json"
)
OUT_JSON = DOCS / (
    "prime-matrix-affine-twin-endpoint-release-phase-scale-bridge-exhaustion-audit.json"
)
OUT_MD = DOCS / (
    "prime-matrix-affine-twin-endpoint-release-phase-scale-bridge-exhaustion-audit.md"
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


def nearest(value: int, values: list[int]) -> dict[str, int] | None:
    """返回最近整数及其差值。"""
    if not values:
        return None
    item = min(values, key=lambda candidate: (abs(candidate - value), candidate))
    return {
        "value": item,
        "signed_delta": item - value,
        "abs_delta": abs(item - value),
    }


def compact_source(row: dict[str, Any]) -> dict[str, Any]:
    """提取 gap-fill source 的相位签名。"""
    return {
        "gap_ell": int(row["gap_ell"]),
        "generator_ell": int(row["generator_ell"]),
        "fill_ell": int(row["fill_ell"]),
        "generator_side": str(row["generator_side"]),
        "fill_side": str(row["fill_side"]),
        "p_delay": int(row["p_delay"]),
        "generator_residue": int(row["generator_residue"]),
        "fill_residue": int(row["fill_residue"]),
        "gap_fill_pair_key": str(row["gap_fill_pair_key"]),
    }


def source_matches_expected(
    source: dict[str, Any],
    expected: dict[str, Any],
) -> bool:
    """判定 source 是否匹配 moving q 的 AffineTwin 期望签名。"""
    return (
        int(expected["gap_ell"]) == int(source["gap_ell"])
        and int(expected["generator_ell"]) == int(source["generator_ell"])
        and int(expected["fill_ell"]) == int(source["fill_ell"])
        and str(expected["generator_side"]) == str(source["generator_side"])
        and str(expected["fill_side"]) == str(source["fill_side"])
        and expected["expected_p_delay"] == int(source["p_delay"])
    )


def unused_jump_index(rows: list[dict[str, Any]]) -> dict[int, list[dict[str, Any]]]:
    """按 absolute CRT jump 建立 unused-target 索引。"""
    out: dict[int, list[dict[str, Any]]] = {}
    for row in rows:
        out.setdefault(int(row["abs_crt_jump_to_unused_target"]), []).append(row)
    return out


def source_index(rows: list[dict[str, Any]]) -> dict[int, list[dict[str, Any]]]:
    """按 gap ell 建立 source 索引。"""
    out: dict[int, list[dict[str, Any]]] = {}
    for row in rows:
        out.setdefault(int(row["gap_ell"]), []).append(compact_source(row))
    return out


def jump_summary(rows: list[dict[str, Any]]) -> dict[str, Any] | None:
    """压缩同一 jump 的 unused-target 行。"""
    if not rows:
        return None
    return {
        "row_count": len(rows),
        "min_new_side_residue_count": min(
            int(row["new_side_residue_count"]) for row in rows
        ),
        "all_need_new_side_residue": all(
            int(row["new_side_residue_count"]) > 0 for row in rows
        ),
        "target_pairs": sorted({str(row["target_unused_pair_key"]) for row in rows}),
        "source_pairs": sorted({str(row["source_pair_key"]) for row in rows}),
    }


def build_q_row(
    moving_row: dict[str, Any],
    sources_by_gap: dict[int, list[dict[str, Any]]],
    jumps_by_value: dict[int, list[dict[str, Any]]],
    gap_values: list[int],
    jump_values: list[int],
) -> dict[str, Any]:
    """构造单个 moving q 的桥接审计行。"""
    q = int(moving_row["q"])
    q_minus_2 = q - 2
    expected = moving_row["expected_signature"]
    exact_gap_q_sources = sources_by_gap.get(q, [])
    exact_gap_q_minus_2_sources = sources_by_gap.get(q_minus_2, [])
    exact_jump_q_rows = jumps_by_value.get(q, [])
    exact_jump_q_minus_2_rows = jumps_by_value.get(q_minus_2, [])

    exact_gap_sources = exact_gap_q_sources + exact_gap_q_minus_2_sources
    exact_source_signature_match = any(
        source_matches_expected(source, expected) for source in exact_gap_sources
    )
    q_minus_2_gap_signature_mismatch = bool(exact_gap_q_minus_2_sources) and not any(
        source_matches_expected(source, expected)
        for source in exact_gap_q_minus_2_sources
    )
    exact_or_offset_unused_rows = exact_jump_q_rows + exact_jump_q_minus_2_rows
    unused_without_new_side = any(
        int(row["new_side_residue_count"]) == 0 for row in exact_or_offset_unused_rows
    )
    prime_gate = moving_row["prime_gate"]

    viable_bridge = (
        bool(moving_row["moving_key_source_rematerialized_current"])
        and exact_source_signature_match
        and bool(exact_or_offset_unused_rows)
        and unused_without_new_side
        and bool(prime_gate["affine_twin_prime_gate_passed"])
    )

    if viable_bridge:
        route = "ViableExactScaleBridge"
    elif exact_gap_q_sources or exact_jump_q_rows:
        route = "ExactQScaleFractured"
    elif exact_gap_q_minus_2_sources or exact_jump_q_minus_2_rows:
        route = "ExactQMinus2ScaleFractured"
    else:
        route = "NoExactScaleBridge"

    return {
        "q": q,
        "route": route,
        "moving_route": str(moving_row["route"]),
        "source_pair_keys": moving_row["source_pair_keys"],
        "min_required_common_side_depth": int(
            moving_row["min_required_common_side_depth"]
        ),
        "prime_gate": prime_gate,
        "failed_invariants": moving_row["failed_invariants"],
        "exact_gap_q_count": len(exact_gap_q_sources),
        "exact_gap_q_minus_2_count": len(exact_gap_q_minus_2_sources),
        "exact_unused_jump_q_count": len(exact_jump_q_rows),
        "exact_unused_jump_q_minus_2_count": len(exact_jump_q_minus_2_rows),
        "nearest_gap_to_q": nearest(q, gap_values),
        "nearest_gap_to_q_minus_2": nearest(q_minus_2, gap_values),
        "nearest_unused_jump_to_q": nearest(q, jump_values),
        "nearest_unused_jump_to_q_minus_2": nearest(q_minus_2, jump_values),
        "exact_gap_q_sources": exact_gap_q_sources,
        "exact_gap_q_minus_2_sources": exact_gap_q_minus_2_sources,
        "exact_unused_jump_q_summary": jump_summary(exact_jump_q_rows),
        "exact_unused_jump_q_minus_2_summary": jump_summary(
            exact_jump_q_minus_2_rows
        ),
        "expected_signature": expected,
        "exact_source_signature_match": exact_source_signature_match,
        "q_minus_2_gap_signature_mismatch": q_minus_2_gap_signature_mismatch,
        "unused_without_new_side_residue": unused_without_new_side,
        "viable_exact_scale_bridge_current": viable_bridge,
    }


def build_result(
    actual_anchor_path: Path,
    moving_key_path: Path,
    unused_target_path: Path,
    pair_path: Path,
    near_miss_path: Path,
) -> dict[str, Any]:
    """构造 phase-scale bridge exhaustion 审计结果。"""
    actual_anchor = load_json(actual_anchor_path)
    moving_key = load_json(moving_key_path)
    unused_target = load_json(unused_target_path)
    pair = load_json(pair_path)
    near_miss = load_json(near_miss_path)

    moving_rows = moving_key["candidate_q_source_rematerialization_rows"]
    unused_rows = unused_target["unused_target_arrival_rows"]
    pair_rows = pair["gap_fill_pair_rows"]
    sources_by_gap = source_index(pair_rows)
    jumps_by_value = unused_jump_index(unused_rows)
    gap_values = sorted(sources_by_gap)
    jump_values = sorted(jumps_by_value)

    q_rows = [
        build_q_row(row, sources_by_gap, jumps_by_value, gap_values, jump_values)
        for row in moving_rows
    ]
    exact_q_gap_rows = [row for row in q_rows if row["exact_gap_q_count"]]
    exact_q_jump_rows = [row for row in q_rows if row["exact_unused_jump_q_count"]]
    exact_qminus2_gap_rows = [
        row for row in q_rows if row["exact_gap_q_minus_2_count"]
    ]
    exact_qminus2_jump_rows = [
        row for row in q_rows if row["exact_unused_jump_q_minus_2_count"]
    ]
    exact_qminus2_both_rows = [
        row
        for row in q_rows
        if row["exact_gap_q_minus_2_count"]
        and row["exact_unused_jump_q_minus_2_count"]
    ]
    viable_rows = [row for row in q_rows if row["viable_exact_scale_bridge_current"]]

    nearest_q_to_gap = min(
        q_rows,
        key=lambda row: (
            int(row["nearest_gap_to_q"]["abs_delta"]),
            int(row["q"]),
        ),
    )
    nearest_q_to_jump = min(
        q_rows,
        key=lambda row: (
            int(row["nearest_unused_jump_to_q"]["abs_delta"]),
            int(row["q"]),
        ),
    )
    strongest_exact_offset = min(
        exact_qminus2_both_rows or q_rows,
        key=lambda row: (
            0 if row in exact_qminus2_both_rows else 1,
            int(row["nearest_gap_to_q_minus_2"]["abs_delta"]),
            int(row["nearest_unused_jump_to_q_minus_2"]["abs_delta"]),
            int(row["q"]),
        ),
    )

    all_exact_or_offset_bridges_fractured = (
        not viable_rows
        and not exact_q_gap_rows
        and not exact_q_jump_rows
        and [int(row["q"]) for row in exact_qminus2_both_rows] == [61]
        and bool(
            near_miss["aggregate"][
                "near_miss_61_59_phase_fracture_closed_current_sweep"
            ]
        )
        and all(
            row["q_minus_2_gap_signature_mismatch"]
            and row["exact_unused_jump_q_minus_2_summary"] is not None
            and row["exact_unused_jump_q_minus_2_summary"][
                "all_need_new_side_residue"
            ]
            for row in exact_qminus2_both_rows
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
        "near_miss_61_59_ledger": str(near_miss_path.relative_to(ROOT)),
        "combined_crt_modulus": int(
            actual_anchor["aggregate"]["combined_crt_modulus"]
        ),
        "support_width": int(actual_anchor["aggregate"]["support_width"]),
        "moving_q_candidate_count": len(q_rows),
        "moving_q_values": [int(row["q"]) for row in q_rows],
        "available_gap_source_values": gap_values,
        "unused_target_jump_values": jump_values,
        "exact_q_gap_bridge_q_values": [int(row["q"]) for row in exact_q_gap_rows],
        "exact_q_unused_jump_bridge_q_values": [
            int(row["q"]) for row in exact_q_jump_rows
        ],
        "exact_qminus2_gap_bridge_q_values": [
            int(row["q"]) for row in exact_qminus2_gap_rows
        ],
        "exact_qminus2_unused_jump_bridge_q_values": [
            int(row["q"]) for row in exact_qminus2_jump_rows
        ],
        "exact_qminus2_gap_and_unused_bridge_q_values": [
            int(row["q"]) for row in exact_qminus2_both_rows
        ],
        "viable_exact_scale_bridge_q_values": [int(row["q"]) for row in viable_rows],
        "nearest_q_to_gap_atom": {
            "q": int(nearest_q_to_gap["q"]),
            "nearest_gap_to_q": nearest_q_to_gap["nearest_gap_to_q"],
            "route": str(nearest_q_to_gap["route"]),
        },
        "nearest_q_to_unused_jump_atom": {
            "q": int(nearest_q_to_jump["q"]),
            "nearest_unused_jump_to_q": nearest_q_to_jump[
                "nearest_unused_jump_to_q"
            ],
            "route": str(nearest_q_to_jump["route"]),
        },
        "strongest_exact_offset_bridge_atom": {
            "q": int(strongest_exact_offset["q"]),
            "route": str(strongest_exact_offset["route"]),
            "q_minus_2": int(strongest_exact_offset["q"]) - 2,
            "exact_gap_q_minus_2_count": int(
                strongest_exact_offset["exact_gap_q_minus_2_count"]
            ),
            "exact_unused_jump_q_minus_2_count": int(
                strongest_exact_offset["exact_unused_jump_q_minus_2_count"]
            ),
            "moving_route": str(strongest_exact_offset["moving_route"]),
            "failed_invariants": strongest_exact_offset["failed_invariants"],
        },
        "near_miss_61_59_phase_fracture_closed_current_sweep": bool(
            near_miss["aggregate"][
                "near_miss_61_59_phase_fracture_closed_current_sweep"
            ]
        ),
        "all_exact_or_offset_scale_bridges_fractured_current_sweep": (
            all_exact_or_offset_bridges_fractured
        ),
        "global_phase_scale_bridge_excluded": False,
        "row_column_unconditional_closed": False,
    }

    return {
        "certificate_type": (
            "prime_matrix_affine_twin_endpoint_release_"
            "phase_scale_bridge_exhaustion_audit"
        ),
        "status": "current_sweep_phase_scale_bridge_exhausted_global_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "aggregate": aggregate,
        "q_bridge_rows": q_rows,
        "contract": {
            "phase_scale_bridge_gate": [
                "a moving q must exactly match an available source scale or its q-2 complement",
                "the matched source must have the expected AffineTwin gap/generator/fill/orientation/delay signature",
                "the same scale must also match an unused-target arrival without introducing a new side residue",
                "the moving q must pass the AffineTwin prime/source gate",
                "otherwise the apparent integer-scale bridge is only a phase-scale fracture",
            ],
            "closed_current_sweep": all_exact_or_offset_bridges_fractured,
            "global_remaining": [
                "PhaseScaleBridgeGlobalNoGo",
                "NearMiss6159GlobalFamilyNoGo",
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
                near_miss_path,
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
        "# Prime Matrix AffineTwin endpoint-release phase-scale bridge exhaustion audit",
        "",
        "**状态：** `current_sweep_phase_scale_bridge_exhausted_global_open`",
        "",
        "本审计把全部 moving-q 候选、当前可用 gap source、unused-target CRT 跳跃放入同一个相位尺度账本，检查是否存在比 `61/59` 更强的桥接通道。",
        "",
        "```text",
        f"support_width={agg['support_width']}",
        f"moving_q_candidate_count={agg['moving_q_candidate_count']}",
        f"moving_q_values={agg['moving_q_values']}",
        f"available_gap_source_values={agg['available_gap_source_values']}",
        f"unused_target_jump_values={agg['unused_target_jump_values']}",
        f"exact_q_gap_bridge_q_values={agg['exact_q_gap_bridge_q_values']}",
        f"exact_q_unused_jump_bridge_q_values={agg['exact_q_unused_jump_bridge_q_values']}",
        f"exact_qminus2_gap_and_unused_bridge_q_values={agg['exact_qminus2_gap_and_unused_bridge_q_values']}",
        f"viable_exact_scale_bridge_q_values={agg['viable_exact_scale_bridge_q_values']}",
        f"strongest_exact_offset_bridge_atom={agg['strongest_exact_offset_bridge_atom']}",
        f"all_exact_or_offset_scale_bridges_fractured_current_sweep={fmt_bool(agg['all_exact_or_offset_scale_bridges_fractured_current_sweep'])}",
        "```",
        "",
        "## 1. q bridge rows",
        "",
        "| q | route | moving route | exact gap q | exact gap q-2 | exact jump q | exact jump q-2 | nearest gap to q | nearest jump to q | failed invariants |",
        "| ---: | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |",
    ]
    for row in result["q_bridge_rows"]:
        lines.append(
            "| {q} | `{route}` | `{moving}` | {gq} | {gm2} | {jq} | {jm2} | `{ng}` | `{nj}` | `{failed}` |".format(
                q=row["q"],
                route=table_cell(row["route"]),
                moving=table_cell(row["moving_route"]),
                gq=row["exact_gap_q_count"],
                gm2=row["exact_gap_q_minus_2_count"],
                jq=row["exact_unused_jump_q_count"],
                jm2=row["exact_unused_jump_q_minus_2_count"],
                ng=row["nearest_gap_to_q"],
                nj=row["nearest_unused_jump_to_q"],
                failed=table_cell(",".join(row["failed_invariants"])),
            )
        )

    lines.extend(
        [
            "",
            "## 2. 显式矛盾点",
            "",
            "没有任何 moving-q 与可用 gap source 精确相等，也没有任何 moving-q 与 unused-target CRT 跳跃精确相等。唯一同时命中 gap source 与 unused jump 的精确 offset 是 `q=61` 的 `q-2=59`。",
            "",
            "这个唯一 offset 桥已经被上一层 `61/59` phase-fracture 关闭：`q=61` 不通过 AffineTwin 同向 prime/source gate；gap `59` source 的角色是 `generator=61, fill=59, sides=minus->minus`，不是 `q=61` 期望的 `generator=59, fill=61, sides=minus->plus`；unused-target 的 `59` 跳跃仍需要新增侧残基。",
            "",
            "因此当前 sweep 中反例链不能把 moving-key、已有 source、unused-target arrival 三者接成同一条 actual 相位桥。若全局族中这类桥持续复现，必须升级为 `PhaseScaleBridgeGlobalNoGo` 的族证明；否则失败形态应登记为 source-rematerialization、unused-target、ColumnCRT/PDEC 或 moving-family 出口。",
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
        "--near-miss-ledger",
        type=Path,
        default=NEAR_MISS_LEDGER,
        help="near-miss 61/59 phase-fracture ledger path",
    )
    args = parser.parse_args()
    result = build_result(
        args.actual_anchor_ledger,
        args.moving_key_ledger,
        args.unused_target_ledger,
        args.pair_ledger,
        args.near_miss_ledger,
    )
    write_outputs(result)
    print(json.dumps(result["aggregate"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
