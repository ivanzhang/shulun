#!/usr/bin/env python3
"""生成 AffineTwin support-motion depth 审计证书。

用法示例：
  python3 experiments/prime_matrix_affine_twin_support_motion_depth_audit.py
  python3 -m json.tool data/prime-matrix-affine-twin-support-motion-depth-ledger.json

输出：
  data/prime-matrix-affine-twin-support-motion-depth-ledger.json
  docs/monograph/prime-matrix-affine-twin-support-motion-depth-audit.json
  docs/monograph/prime-matrix-affine-twin-support-motion-depth-audit.md
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

CRT_LEDGER = DATA / "prime-matrix-affine-twin-crt-window-gap-ledger.json"
SLOT_LEDGER = DATA / (
    "square-phase-offband-prefix-gap-shadow-selector-h-lower-"
    "affine-twin-slot-phase-lock-ledger.json"
)
UNUSED_TARGET_LEDGER = DATA / (
    "prime-matrix-affine-twin-unused-target-arrival-ledger.json"
)
EXISTING_ACTUAL_LEDGER = DATA / (
    "prime-matrix-affine-twin-existing-actual-collision-jump-ledger.json"
)

OUT_LEDGER = DATA / "prime-matrix-affine-twin-support-motion-depth-ledger.json"
OUT_JSON = DOCS / "prime-matrix-affine-twin-support-motion-depth-audit.json"
OUT_MD = DOCS / "prime-matrix-affine-twin-support-motion-depth-audit.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def pair_key(row: dict[str, Any]) -> str:
    """生成 residue pair 的稳定键。"""
    return f"{int(row['generator_residue'])}:{int(row['fill_residue'])}"


def slot_index(rows: list[dict[str, Any]]) -> dict[int, dict[str, Any]]:
    """按 q 建立 slot-lock 索引。"""
    return {int(row["gap_ell"]): row for row in rows}


def support_motion_row(
    crt_row: dict[str, Any],
    slot_row: dict[str, Any],
) -> dict[str, Any]:
    """把一个 CRT 空窗行转成支撑运动深度义务。"""
    q = int(crt_row["q"])
    representative = int(crt_row["nearest_representative"])
    generator_p = int(slot_row["generator_p"])
    shifted_anchor_p = int(slot_row["fill_p"]) - int(slot_row["p_delay"])
    if shifted_anchor_p != generator_p:
        raise RuntimeError("shifted fill anchor does not match generator p")

    generator_lo, generator_hi = [int(value) for value in slot_row["generator_phase"]]
    shifted_fill_lo, shifted_fill_hi = [
        int(value) for value in slot_row["shifted_fill_phase_for_generator_p"]
    ]
    support_lo, support_hi = [int(value) for value in crt_row["pair_phase_support"]]
    current_side = str(crt_row["window_side"])

    if current_side == "below":
        required_common_depth = generator_p - representative
        current_generator_depth = int(slot_row["generator_left_depth"])
        current_fill_depth = int(slot_row["fill_left_depth"])
        generator_endpoint_release = max(0, generator_lo - representative)
        fill_endpoint_release = max(0, shifted_fill_lo - representative)
        pinned_endpoint = "support_left=max(generator_left,shifted_fill_left)"
    elif current_side == "above":
        required_common_depth = representative - generator_p
        current_generator_depth = int(slot_row["generator_right_depth"])
        current_fill_depth = int(slot_row["fill_right_depth"])
        generator_endpoint_release = max(0, representative - generator_hi)
        fill_endpoint_release = max(0, representative - shifted_fill_hi)
        pinned_endpoint = "support_right=min(generator_right,shifted_fill_right)"
    else:
        raise RuntimeError(f"unsupported non-empty side: {current_side}")

    if required_common_depth <= 0:
        raise RuntimeError("required support depth must be positive")

    generator_depth_increment = required_common_depth - current_generator_depth
    fill_depth_increment = required_common_depth - current_fill_depth
    endpoint_release_total = generator_endpoint_release + fill_endpoint_release
    window_distance = int(crt_row["window_distance"])

    return {
        "q": q,
        "source_pair_key": pair_key(crt_row),
        "generator_residue": int(crt_row["generator_residue"]),
        "fill_residue": int(crt_row["fill_residue"]),
        "nearest_representative": representative,
        "window_side": current_side,
        "window_distance": window_distance,
        "support_interval": [support_lo, support_hi],
        "support_width": int(crt_row["pair_phase_support_width"]),
        "generator_phase": [generator_lo, generator_hi],
        "shifted_fill_phase": [shifted_fill_lo, shifted_fill_hi],
        "generator_p": generator_p,
        "p_delay": int(slot_row["p_delay"]),
        "required_common_side_depth": required_common_depth,
        "current_generator_side_depth": current_generator_depth,
        "current_fill_side_depth": current_fill_depth,
        "generator_depth_increment_required": generator_depth_increment,
        "fill_depth_increment_required": fill_depth_increment,
        "generator_endpoint_release_required": generator_endpoint_release,
        "fill_endpoint_release_required": fill_endpoint_release,
        "endpoint_release_total_required": endpoint_release_total,
        "endpoint_release_max_required": max(
            generator_endpoint_release, fill_endpoint_release
        ),
        "extra_release_beyond_window_distance": endpoint_release_total
        - window_distance,
        "requires_both_endpoint_release": generator_endpoint_release > 0
        and fill_endpoint_release > 0,
        "required_depth_exceeds_current_generator_depth": generator_depth_increment
        > 0,
        "required_depth_exceeds_current_fill_depth": fill_depth_increment > 0,
        "support_motion_depth_identity_closed": required_common_depth
        == abs(representative - generator_p),
        "pinned_endpoint": pinned_endpoint,
    }


def build_result(
    crt_path: Path,
    slot_path: Path,
    unused_target_path: Path,
    existing_actual_path: Path,
) -> dict[str, Any]:
    """构造 support-motion depth 审计结果。"""
    crt = load_json(crt_path)
    slot = load_json(slot_path)
    slot_by_q = slot_index(slot["affine_twin_slot_phase_lock_rows"])

    rows = [
        support_motion_row(row, slot_by_q[int(row["q"])])
        for row in crt["crt_window_rows"]
        if not bool(row["supported_actual_packet_current"])
    ]
    if not rows:
        raise RuntimeError("no CRT-window empty rows found")

    side_histogram = Counter(str(row["window_side"]) for row in rows)
    depth_values = [int(row["required_common_side_depth"]) for row in rows]
    generator_increments = [
        int(row["generator_depth_increment_required"]) for row in rows
    ]
    fill_increments = [int(row["fill_depth_increment_required"]) for row in rows]
    total_releases = [int(row["endpoint_release_total_required"]) for row in rows]
    extra_releases = [
        int(row["extra_release_beyond_window_distance"]) for row in rows
    ]
    narrowest_depth_row = min(
        rows,
        key=lambda row: (
            int(row["required_common_side_depth"]),
            int(row["endpoint_release_total_required"]),
            str(row["source_pair_key"]),
        ),
    )
    narrowest_total_release_row = min(
        rows,
        key=lambda row: (
            int(row["endpoint_release_total_required"]),
            int(row["required_common_side_depth"]),
            str(row["source_pair_key"]),
        ),
    )

    aggregate = {
        "crt_window_gap_ledger": str(crt_path.relative_to(ROOT)),
        "slot_ledger": str(slot_path.relative_to(ROOT)),
        "unused_target_arrival_ledger": str(unused_target_path.relative_to(ROOT)),
        "existing_actual_collision_jump_ledger": str(
            existing_actual_path.relative_to(ROOT)
        ),
        "support_motion_candidate_count": len(rows),
        "support_motion_side_histogram": dict(sorted(side_histogram.items())),
        "support_interval_current": rows[0]["support_interval"],
        "support_width_current": int(rows[0]["support_width"]),
        "generator_phase_current": rows[0]["generator_phase"],
        "shifted_fill_phase_current": rows[0]["shifted_fill_phase"],
        "generator_p_current": int(rows[0]["generator_p"]),
        "min_required_common_side_depth": min(depth_values),
        "max_required_common_side_depth": max(depth_values),
        "min_generator_depth_increment_required": min(generator_increments),
        "max_generator_depth_increment_required": max(generator_increments),
        "min_fill_depth_increment_required": min(fill_increments),
        "max_fill_depth_increment_required": max(fill_increments),
        "min_endpoint_release_total_required": min(total_releases),
        "max_endpoint_release_total_required": max(total_releases),
        "min_extra_release_beyond_window_distance": min(extra_releases),
        "max_extra_release_beyond_window_distance": max(extra_releases),
        "narrowest_required_depth_atom": {
            "source_pair_key": narrowest_depth_row["source_pair_key"],
            "window_side": narrowest_depth_row["window_side"],
            "nearest_representative": narrowest_depth_row[
                "nearest_representative"
            ],
            "required_common_side_depth": narrowest_depth_row[
                "required_common_side_depth"
            ],
            "generator_depth_increment_required": narrowest_depth_row[
                "generator_depth_increment_required"
            ],
            "fill_depth_increment_required": narrowest_depth_row[
                "fill_depth_increment_required"
            ],
            "endpoint_release_total_required": narrowest_depth_row[
                "endpoint_release_total_required"
            ],
        },
        "narrowest_endpoint_release_atom": {
            "source_pair_key": narrowest_total_release_row["source_pair_key"],
            "window_side": narrowest_total_release_row["window_side"],
            "nearest_representative": narrowest_total_release_row[
                "nearest_representative"
            ],
            "required_common_side_depth": narrowest_total_release_row[
                "required_common_side_depth"
            ],
            "generator_depth_increment_required": narrowest_total_release_row[
                "generator_depth_increment_required"
            ],
            "fill_depth_increment_required": narrowest_total_release_row[
                "fill_depth_increment_required"
            ],
            "endpoint_release_total_required": narrowest_total_release_row[
                "endpoint_release_total_required"
            ],
        },
        "all_support_motion_requires_both_endpoint_release": all(
            bool(row["requires_both_endpoint_release"]) for row in rows
        ),
        "all_required_depths_exceed_current_generator_depth": all(
            bool(row["required_depth_exceeds_current_generator_depth"])
            for row in rows
        ),
        "all_required_depths_exceed_current_fill_depth": all(
            bool(row["required_depth_exceeds_current_fill_depth"]) for row in rows
        ),
        "all_support_motion_depth_identities_closed": all(
            bool(row["support_motion_depth_identity_closed"]) for row in rows
        ),
        "support_motion_depth_closed_current_sweep": all(
            bool(row["requires_both_endpoint_release"])
            and bool(row["required_depth_exceeds_current_generator_depth"])
            and bool(row["required_depth_exceeds_current_fill_depth"])
            and bool(row["support_motion_depth_identity_closed"])
            for row in rows
        ),
        "global_support_motion_nonpersistence_proved": False,
        "row_column_unconditional_closed": False,
    }

    return {
        "certificate_type": "prime_matrix_affine_twin_support_motion_depth_audit",
        "status": "current_sweep_support_motion_depths_closed_global_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "aggregate": aggregate,
        "support_motion_rows": rows,
        "contract": {
            "support_motion_gate": (
                "A CRT-window empty pair can become actual by moving support "
                "only if both relevant side endpoints are released and both "
                "generator/fill side depths inflate to the common representative "
                "distance."
            ),
            "closed_current_sweep": aggregate[
                "support_motion_depth_closed_current_sweep"
            ],
            "global_remaining": [
                "GlobalSupportMotionNonPersistence",
                "MovingSupportDepthInflation-PDEC/SAE",
                "EndpointReleaseCoupling-PDEC",
                "PrimitiveTwinSlotSupportEscape-PDEC/SAE",
            ],
        },
        "dependency_hashes": {
            str(path.relative_to(ROOT)): sha256(path)
            for path in (crt_path, slot_path, unused_target_path, existing_actual_path)
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
        "# Prime Matrix AffineTwin support-motion depth audit",
        "",
        "**状态：** `current_sweep_support_motion_depths_closed_global_open`",
        "",
        "本审计继续下钻 `SupportMotionEscape`：如果不移动 residue pair，而是移动共同支撑窗口来吞掉空窗 CRT 代表，则相关同侧的 generator 与 shifted-fill 端点都必须释放，且两侧深度必须同时膨胀到同一个代表距离。",
        "",
        "```text",
        f"support_motion_candidate_count={agg['support_motion_candidate_count']}",
        f"support_motion_side_histogram={agg['support_motion_side_histogram']}",
        f"support_width_current={agg['support_width_current']}",
        f"min_required_common_side_depth={agg['min_required_common_side_depth']}",
        f"max_required_common_side_depth={agg['max_required_common_side_depth']}",
        f"min_endpoint_release_total_required={agg['min_endpoint_release_total_required']}",
        f"max_endpoint_release_total_required={agg['max_endpoint_release_total_required']}",
        f"min_extra_release_beyond_window_distance={agg['min_extra_release_beyond_window_distance']}",
        f"support_motion_depth_closed_current_sweep={fmt_bool(agg['support_motion_depth_closed_current_sweep'])}",
        "```",
        "",
        "## 1. support-motion depth 表",
        "",
        "| pair | side | nearest rep | window gap | common depth | g depth + | f depth + | endpoint release total | extra over gap |",
        "| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in result["support_motion_rows"]:
        lines.append(
            "| `{pair}` | `{side}` | {rep} | {gap} | {depth} | {g_inc} | {f_inc} | {release} | {extra} |".format(
                pair=row["source_pair_key"],
                side=row["window_side"],
                rep=row["nearest_representative"],
                gap=row["window_distance"],
                depth=row["required_common_side_depth"],
                g_inc=row["generator_depth_increment_required"],
                f_inc=row["fill_depth_increment_required"],
                release=row["endpoint_release_total_required"],
                extra=row["extra_release_beyond_window_distance"],
            )
        )

    narrow = agg["narrowest_required_depth_atom"]
    lines.extend(
        [
            "",
            "## 2. 当前读数",
            "",
            f"- 当前 generator phase 为 `{agg['generator_phase_current']}`，shifted-fill phase 为 `{agg['shifted_fill_phase_current']}`，共同支撑为 `{agg['support_interval_current']}`。",
            "- 因此左侧支撑由 generator lower 与 shifted-fill lower 共同限制，右侧支撑由 generator upper 与 shifted-fill upper 共同限制；吞掉空窗代表需要同侧两个端点同时释放。",
            f"- 最小深度膨胀 atom 是 `{narrow['source_pair_key']}`，nearest representative `{narrow['nearest_representative']}`，需要共同侧深度 `{narrow['required_common_side_depth']}`，generator 深度额外 `{narrow['generator_depth_increment_required']}`，fill 深度额外 `{narrow['fill_depth_increment_required']}`。",
            f"- 当前最小总端点释放为 `{agg['min_endpoint_release_total_required']}`，仍比原 window gap 多 `{agg['min_extra_release_beyond_window_distance']}`。",
            "",
            "## 3. 结论边界",
            "",
            "- 本步关闭当前 sweep 的 support-motion depth 账本：每个空窗若靠移动支撑变 actual，都必须同时释放两个相关端点，并同步增加 generator/fill 侧深度。",
            "- 本步不证明全局 support motion 不复现；全局剩余是排斥这种同步深度膨胀的持久复现，或路由到 `MovingSupportDepthInflation-PDEC/SAE`、`EndpointReleaseCoupling-PDEC`、`PrimitiveTwinSlotSupportEscape-PDEC/SAE`。",
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


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(
        description="生成 AffineTwin support-motion depth 审计证书。"
    )
    parser.add_argument("--crt-window-gap-ledger", type=Path, default=CRT_LEDGER)
    parser.add_argument("--slot-ledger", type=Path, default=SLOT_LEDGER)
    parser.add_argument("--unused-target-ledger", type=Path, default=UNUSED_TARGET_LEDGER)
    parser.add_argument(
        "--existing-actual-ledger", type=Path, default=EXISTING_ACTUAL_LEDGER
    )
    return parser.parse_args()


def main() -> None:
    """入口。"""
    args = parse_args()
    result = build_result(
        args.crt_window_gap_ledger,
        args.slot_ledger,
        args.unused_target_ledger,
        args.existing_actual_ledger,
    )
    write_outputs(result)
    print(json.dumps(result["aggregate"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
