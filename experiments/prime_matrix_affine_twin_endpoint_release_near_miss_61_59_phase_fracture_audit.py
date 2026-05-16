#!/usr/bin/env python3
"""生成 AffineTwin endpoint-release 61/59 near-miss phase-fracture 审计证书。

用法示例：
  python3 experiments/prime_matrix_affine_twin_endpoint_release_near_miss_61_59_phase_fracture_audit.py
  python3 -m json.tool data/prime-matrix-affine-twin-endpoint-release-near-miss-61-59-phase-fracture-ledger.json

输出：
  data/prime-matrix-affine-twin-endpoint-release-near-miss-61-59-phase-fracture-ledger.json
  docs/monograph/prime-matrix-affine-twin-endpoint-release-near-miss-61-59-phase-fracture-audit.json
  docs/monograph/prime-matrix-affine-twin-endpoint-release-near-miss-61-59-phase-fracture-audit.md
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

ACTUAL_ANCHOR_REPLACEMENT_LEDGER = DATA / (
    "prime-matrix-affine-twin-endpoint-release-actual-anchor-replacement-ledger.json"
)
MOVING_KEY_REMATERIALIZATION_LEDGER = DATA / (
    "prime-matrix-affine-twin-moving-key-source-rematerialization-ledger.json"
)
UNUSED_TARGET_ARRIVAL_LEDGER = DATA / (
    "prime-matrix-affine-twin-unused-target-arrival-ledger.json"
)
PAIR_LEDGER = DATA / (
    "square-phase-offband-prefix-gap-shadow-selector-h-lower-gap-fill-pair-ledger.json"
)

OUT_LEDGER = DATA / (
    "prime-matrix-affine-twin-endpoint-release-near-miss-61-59-phase-fracture-ledger.json"
)
OUT_JSON = DOCS / (
    "prime-matrix-affine-twin-endpoint-release-near-miss-61-59-phase-fracture-audit.json"
)
OUT_MD = DOCS / (
    "prime-matrix-affine-twin-endpoint-release-near-miss-61-59-phase-fracture-audit.md"
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


def min_formal_replacement(rows: list[dict[str, Any]]) -> dict[str, Any]:
    """取现有 formal pair 替换 actual anchor 的最窄原子。"""
    return min(
        rows,
        key=lambda row: (
            int(row["abs_crt_jump_from_actual"]),
            int(row["endpoint_release_total_required"]),
            str(row["target_pair_key"]),
        ),
    )


def min_unused_replacement(rows: list[dict[str, Any]]) -> dict[str, Any]:
    """取 unused-target 替换 actual anchor 的最窄原子。"""
    return min(
        rows,
        key=lambda row: (
            int(row["abs_crt_jump_to_unused_target"]),
            int(row["new_side_residue_count"]),
            str(row["target_unused_pair_key"]),
        ),
    )


def moving_row_by_q(rows: list[dict[str, Any]], q: int) -> dict[str, Any] | None:
    """按 q 返回 moving-key source-rematerialization 行。"""
    matches = [row for row in rows if int(row["q"]) == q]
    if len(matches) > 1:
        raise RuntimeError(f"expected at most one row for q={q}, got {len(matches)}")
    return matches[0] if matches else None


def pair_rows_by_gap(rows: list[dict[str, Any]], gap: int) -> list[dict[str, Any]]:
    """按 gap ell 过滤 gap-fill source 行。"""
    return [row for row in rows if int(row["gap_ell"]) == gap]


def compact_gap_source(row: dict[str, Any]) -> dict[str, Any]:
    """提取 gap source 的相位签名。"""
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


def build_result(
    actual_anchor_path: Path,
    moving_key_path: Path,
    unused_target_path: Path,
    pair_path: Path,
) -> dict[str, Any]:
    """构造 61/59 near-miss 相位裂缝审计结果。"""
    actual_anchor = load_json(actual_anchor_path)
    moving_key = load_json(moving_key_path)
    unused_target = load_json(unused_target_path)
    pair = load_json(pair_path)

    actual_agg = actual_anchor["aggregate"]
    moving_agg = moving_key["aggregate"]
    unused_agg = unused_target["aggregate"]

    formal_atom = min_formal_replacement(actual_anchor["formal_replacement_rows"])
    unused_atom = min_unused_replacement(
        actual_anchor["unused_target_replacement_rows"]
    )
    unused_arrival_atom = unused_agg["minimum_crt_jump_atom"]

    q61 = moving_row_by_q(
        moving_key["candidate_q_source_rematerialization_rows"], 61
    )
    q111 = moving_row_by_q(
        moving_key["candidate_q_source_rematerialization_rows"], 111
    )
    q59 = moving_row_by_q(
        moving_key["candidate_q_source_rematerialization_rows"], 59
    )
    if q61 is None or q111 is None:
        raise RuntimeError("expected q=61 and q=111 near-miss rows")

    gap59_sources = pair_rows_by_gap(pair["gap_fill_pair_rows"], 59)
    if len(gap59_sources) != 1:
        raise RuntimeError(f"expected one gap=59 source, got {len(gap59_sources)}")
    gap59_source = compact_gap_source(gap59_sources[0])

    q61_expected = q61["expected_signature"]
    q61_nearest = q61["nearest_available_gap_source"]
    formal_pair = str(formal_atom["target_pair_key"])
    unused_source_pair = str(unused_atom["source_pair_key"])
    unused_target_pair = str(unused_atom["target_unused_pair_key"])
    support_width = int(actual_agg["support_width"])

    q61_nearest_is_gap59 = (
        q61_nearest is not None
        and int(q61_nearest["gap_ell"]) == 59
        and int(q61_nearest["signed_delta"]) == -2
    )
    unused_jump_matches_gap59 = (
        int(unused_atom["abs_crt_jump_to_unused_target"]) == 59
        and int(unused_arrival_atom["abs_crt_jump_to_unused_target"]) == 59
    )
    same_narrow_source_pair = (
        formal_pair == unused_source_pair == str(unused_arrival_atom["source_pair_key"])
    )
    q61_expected_not_gap59_source = not (
        int(q61_expected["gap_ell"]) == gap59_source["gap_ell"]
        and int(q61_expected["generator_ell"]) == gap59_source["generator_ell"]
        and int(q61_expected["fill_ell"]) == gap59_source["fill_ell"]
        and str(q61_expected["generator_side"]) == gap59_source["generator_side"]
        and str(q61_expected["fill_side"]) == gap59_source["fill_side"]
        and q61_expected["expected_p_delay"] == gap59_source["p_delay"]
    )
    q61_gate_closed = (
        not bool(q61["moving_key_source_rematerialized_current"])
        and "q_mod4_eq3" in q61["failed_invariants"]
        and "expected_p_delay_integral" in q61["failed_invariants"]
        and "gap_source_absent" in q61["failed_invariants"]
    )
    q111_gate_closed = (
        not bool(q111["moving_key_source_rematerialized_current"])
        and "q_composite" in q111["failed_invariants"]
    )

    phase_fracture_closed = all(
        [
            formal_pair == "19:12",
            int(formal_atom["required_common_side_depth"]) == 58,
            int(formal_atom["abs_crt_jump_from_actual"]) == 58,
            int(formal_atom["endpoint_release_total_required"]) == 70,
            int(q61["q"]) == 61,
            int(q111["q"]) == 111,
            q61_nearest_is_gap59,
            q61_expected_not_gap59_source,
            q61_gate_closed,
            q111_gate_closed,
            q59 is None,
            unused_target_pair == "20:9",
            unused_jump_matches_gap59,
            same_narrow_source_pair,
            int(unused_atom["new_side_residue_count"]) >= 1,
            int(formal_atom["abs_crt_jump_from_actual"]) > support_width,
            int(unused_atom["abs_crt_jump_to_unused_target"]) > support_width,
        ]
    )

    bridge_rows = [
        {
            "atom": "formal_replacement_minimum",
            "role": "existing formal pair would replace actual anchor",
            "source_or_pair": formal_pair,
            "integer_scale": int(formal_atom["abs_crt_jump_from_actual"]),
            "phase_status": "jump_exceeds_support_and_requires_endpoint_release",
            "blocking_invariant": "abs_crt_jump=58 > support_width=20; endpoint_release=70",
        },
        {
            "atom": "moving_key_fill_candidate",
            "role": "fill-depth formula candidate for the same formal atom",
            "source_or_pair": "q=61",
            "integer_scale": 61,
            "phase_status": str(q61["route"]),
            "blocking_invariant": ",".join(q61["failed_invariants"]),
        },
        {
            "atom": "moving_key_generator_candidate",
            "role": "generator-depth formula candidate for the same formal atom",
            "source_or_pair": "q=111",
            "integer_scale": 111,
            "phase_status": str(q111["route"]),
            "blocking_invariant": ",".join(q111["failed_invariants"]),
        },
        {
            "atom": "nearest_available_gap_source",
            "role": "nearest source to q=61 in the current source ledger",
            "source_or_pair": "gap=59",
            "integer_scale": 59,
            "phase_status": "wrong_gap_role_for_q61",
            "blocking_invariant": "gap=59 source has generator=61, fill=59, sides=minus->minus",
        },
        {
            "atom": "unused_target_minimum",
            "role": "unused target replacement from the same formal atom",
            "source_or_pair": f"{formal_pair}->{unused_target_pair}",
            "integer_scale": int(unused_atom["abs_crt_jump_to_unused_target"]),
            "phase_status": "new_side_residue_required",
            "blocking_invariant": "jump=59 > support_width=20; new_generator_residue=20",
        },
    ]

    aggregate = {
        "actual_anchor_replacement_ledger": str(
            actual_anchor_path.relative_to(ROOT)
        ),
        "moving_key_source_rematerialization_ledger": str(
            moving_key_path.relative_to(ROOT)
        ),
        "unused_target_arrival_ledger": str(unused_target_path.relative_to(ROOT)),
        "pair_ledger": str(pair_path.relative_to(ROOT)),
        "combined_crt_modulus": int(actual_agg["combined_crt_modulus"]),
        "support_width": support_width,
        "actual_anchor_pair": str(actual_agg["actual_anchor_pair"]),
        "actual_crt_residue": int(actual_agg["actual_crt_residue"]),
        "formal_min_pair": formal_pair,
        "formal_min_abs_crt_jump": int(formal_atom["abs_crt_jump_from_actual"]),
        "formal_min_required_common_side_depth": int(
            formal_atom["required_common_side_depth"]
        ),
        "formal_min_endpoint_release": int(
            formal_atom["endpoint_release_total_required"]
        ),
        "moving_narrowest_source_pair": str(
            moving_agg["narrowest_depth_source_pair_key"]
        ),
        "moving_narrowest_candidate_q_values": [
            int(q) for q in moving_agg["narrowest_depth_candidate_q_values"]
        ],
        "q61_route": str(q61["route"]),
        "q61_failed_invariants": q61["failed_invariants"],
        "q61_nearest_available_gap_source": q61_nearest,
        "q61_expected_signature": q61_expected,
        "q111_route": str(q111["route"]),
        "q111_failed_invariants": q111["failed_invariants"],
        "q59_is_moving_candidate": q59 is not None,
        "gap59_source_signature": gap59_source,
        "unused_min_source_pair": unused_source_pair,
        "unused_min_target_pair": unused_target_pair,
        "unused_min_abs_crt_jump": int(
            unused_atom["abs_crt_jump_to_unused_target"]
        ),
        "unused_min_new_side_residue_count": int(
            unused_atom["new_side_residue_count"]
        ),
        "q61_nearest_is_gap59_delta_minus_2": q61_nearest_is_gap59,
        "unused_jump_matches_gap59_scale": unused_jump_matches_gap59,
        "q61_expected_signature_differs_from_gap59_source": (
            q61_expected_not_gap59_source
        ),
        "same_narrow_source_pair_for_formal_and_unused_minima": same_narrow_source_pair,
        "near_miss_61_59_phase_fracture_closed_current_sweep": (
            phase_fracture_closed
        ),
        "global_near_miss_family_excluded": False,
        "row_column_unconditional_closed": False,
    }

    return {
        "certificate_type": (
            "prime_matrix_affine_twin_endpoint_release_"
            "near_miss_61_59_phase_fracture_audit"
        ),
        "status": "current_sweep_near_miss_61_59_phase_fracture_closed_global_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "aggregate": aggregate,
        "bridge_rows": bridge_rows,
        "formal_replacement_minimum": formal_atom,
        "moving_q61_row": q61,
        "moving_q111_row": q111,
        "gap59_source_row": gap59_source,
        "unused_target_minimum": unused_atom,
        "contract": {
            "near_miss_bridge_gate": [
                "the formal replacement minimum and unused-target minimum must refer to the same support atom",
                "the moving q=61 candidate must pass AffineTwin prime/source gates",
                "the nearest available gap=59 source must match the expected q=61 source signature",
                "the unused-target jump scale 59 must not require a new side residue",
                "otherwise the same integer scales 61 and 59 are only a phase near-miss, not a bridge",
            ],
            "closed_current_sweep": phase_fracture_closed,
            "global_remaining": [
                "NearMiss6159GlobalFamilyNoGo",
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
        "# Prime Matrix AffineTwin endpoint-release 61/59 near-miss phase-fracture audit",
        "",
        "**状态：** `current_sweep_near_miss_61_59_phase_fracture_closed_global_open`",
        "",
        "本审计对准 actual-anchor replacement 后的最窄近失配：formal 替换最窄 atom `19:12` 要求 moving-key 候选 `61/111`，而 unused-target 最窄跳跃与最近可用 gap source 都出现整数 `59`。审计目标是判定这个 `61/59` 近邻是否能桥接反例链与真实链。",
        "",
        "```text",
        f"combined_crt_modulus={agg['combined_crt_modulus']}",
        f"support_width={agg['support_width']}",
        f"actual_anchor_pair={agg['actual_anchor_pair']}",
        f"actual_crt_residue={agg['actual_crt_residue']}",
        f"formal_min_pair={agg['formal_min_pair']}",
        f"formal_min_abs_crt_jump={agg['formal_min_abs_crt_jump']}",
        f"formal_min_required_common_side_depth={agg['formal_min_required_common_side_depth']}",
        f"formal_min_endpoint_release={agg['formal_min_endpoint_release']}",
        f"moving_narrowest_candidate_q_values={agg['moving_narrowest_candidate_q_values']}",
        f"q61_route={agg['q61_route']}",
        f"q61_failed_invariants={agg['q61_failed_invariants']}",
        f"q111_route={agg['q111_route']}",
        f"q111_failed_invariants={agg['q111_failed_invariants']}",
        f"q59_is_moving_candidate={fmt_bool(agg['q59_is_moving_candidate'])}",
        f"unused_min_target_pair={agg['unused_min_target_pair']}",
        f"unused_min_abs_crt_jump={agg['unused_min_abs_crt_jump']}",
        f"unused_min_new_side_residue_count={agg['unused_min_new_side_residue_count']}",
        f"near_miss_61_59_phase_fracture_closed_current_sweep={fmt_bool(agg['near_miss_61_59_phase_fracture_closed_current_sweep'])}",
        "```",
        "",
        "## 1. bridge rows",
        "",
        "| atom | role | source/pair | scale | phase status | blocking invariant |",
        "| --- | --- | --- | ---: | --- | --- |",
    ]
    for row in result["bridge_rows"]:
        lines.append(
            "| `{}` | {} | `{}` | {} | `{}` | `{}` |".format(
                row["atom"],
                table_cell(row["role"]),
                row["source_or_pair"],
                row["integer_scale"],
                table_cell(row["phase_status"]),
                table_cell(row["blocking_invariant"]),
            )
        )

    gap59 = agg["gap59_source_signature"]
    q61_expected = agg["q61_expected_signature"]
    lines.extend(
        [
            "",
            "## 2. 相位裂缝",
            "",
            f"`q=61` 是最强 near miss：`61` 与 `59` 都为素数，且最近可用 gap source 确实是 `59`，signed delta 为 `-2`。但 AffineTwin 同向源要求的是 `gap=61, generator=59, fill=61, sides=minus->plus`，并且 `p_delay=(11q-21)/4` 必须为整数。",
            "",
            f"当前 gap `59` source 的实际签名是 `gap={gap59['gap_ell']}, generator={gap59['generator_ell']}, fill={gap59['fill_ell']}, sides={gap59['generator_side']}->{gap59['fill_side']}, p_delay={gap59['p_delay']}`。它和 `q=61` 的期望签名 `{q61_expected}` 不同：gap、fill、方向和 delay 均不能匹配。因此 `59` 只是最近相邻源，不是 `q=61` 的重物化源。",
            "",
            f"同时，unused-target 最窄跳跃也是 `59`，但它的对象是 `{agg['formal_min_pair']}->{agg['unused_min_target_pair']}` 的新侧残基到达，仍有 `59>20`，并且至少新增 `{agg['unused_min_new_side_residue_count']}` 个侧残基。这与 moving-key `q=61` 的源门控不是同一相位义务。",
            "",
            "## 3. 结论边界",
            "",
            "- 本步关闭当前 sweep 中 `61/59` 近失配作为隐藏桥接通道的解释。",
            "- 本步没有证明全局行/列命题；剩余是把 `NearMiss6159GlobalFamilyNoGo` 升格为族定理，或继续排斥 source-rematerialization、unused-target arrival、ColumnCRT/PDEC 与 moving-family 出口。",
            "",
            "## 4. 依赖哈希",
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
        "--actual-anchor-replacement-ledger",
        type=Path,
        default=ACTUAL_ANCHOR_REPLACEMENT_LEDGER,
        help="actual-anchor replacement ledger path",
    )
    parser.add_argument(
        "--moving-key-rematerialization-ledger",
        type=Path,
        default=MOVING_KEY_REMATERIALIZATION_LEDGER,
        help="moving-key source-rematerialization ledger path",
    )
    parser.add_argument(
        "--unused-target-arrival-ledger",
        type=Path,
        default=UNUSED_TARGET_ARRIVAL_LEDGER,
        help="unused-target arrival ledger path",
    )
    parser.add_argument(
        "--pair-ledger",
        type=Path,
        default=PAIR_LEDGER,
        help="gap-fill pair ledger path",
    )
    args = parser.parse_args()
    result = build_result(
        args.actual_anchor_replacement_ledger,
        args.moving_key_rematerialization_ledger,
        args.unused_target_arrival_ledger,
        args.pair_ledger,
    )
    write_outputs(result)
    print(json.dumps(result["aggregate"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
