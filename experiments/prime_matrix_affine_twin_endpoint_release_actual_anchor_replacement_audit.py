#!/usr/bin/env python3
"""生成 AffineTwin actual-anchor replacement 审计证书。

用法示例：
  python3 experiments/prime_matrix_affine_twin_endpoint_release_actual_anchor_replacement_audit.py
  python3 -m json.tool data/prime-matrix-affine-twin-endpoint-release-actual-anchor-replacement-ledger.json

输出：
  data/prime-matrix-affine-twin-endpoint-release-actual-anchor-replacement-ledger.json
  docs/monograph/prime-matrix-affine-twin-endpoint-release-actual-anchor-replacement-audit.json
  docs/monograph/prime-matrix-affine-twin-endpoint-release-actual-anchor-replacement-audit.md
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

BIDIRECTIONAL_HULL_LEDGER = DATA / (
    "prime-matrix-affine-twin-endpoint-release-bidirectional-skew-hull-ledger.json"
)
CUT_ANCHOR_COLUMNCRT_LEDGER = DATA / (
    "prime-matrix-affine-twin-endpoint-release-cut-anchor-"
    "columncrt-compression-ledger.json"
)
SUPPORT_MOTION_LEDGER = DATA / (
    "prime-matrix-affine-twin-support-motion-depth-ledger.json"
)
UNUSED_TARGET_LEDGER = DATA / (
    "prime-matrix-affine-twin-unused-target-arrival-ledger.json"
)

OUT_LEDGER = DATA / (
    "prime-matrix-affine-twin-endpoint-release-actual-anchor-replacement-ledger.json"
)
OUT_JSON = DOCS / (
    "prime-matrix-affine-twin-endpoint-release-actual-anchor-replacement-audit.json"
)
OUT_MD = DOCS / (
    "prime-matrix-affine-twin-endpoint-release-actual-anchor-replacement-audit.md"
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


def fmt_decimal(value: float) -> str:
    """稳定输出小数。"""
    return f"{value:.12g}"


def signed_minimal_delta(target: int, source: int, modulus: int) -> int:
    """计算 source 到 target 的最小有符号模差。"""
    residue = (target - source) % modulus
    if residue > modulus // 2:
        return residue - modulus
    return residue


def support_motion_index(rows: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    """按 pair key 索引 support-motion 行。"""
    return {str(row["source_pair_key"]): row for row in rows}


def build_result(
    bidirectional_hull_path: Path,
    cut_anchor_columncrt_path: Path,
    support_motion_path: Path,
    unused_target_path: Path,
) -> dict[str, Any]:
    """构造 actual-anchor replacement 审计结果。"""
    hull = load_json(bidirectional_hull_path)
    columncrt = load_json(cut_anchor_columncrt_path)
    support_motion = load_json(support_motion_path)
    unused_target = load_json(unused_target_path)

    hull_rows = hull["formal_alignment_rows"]
    hull_agg = hull["aggregate"]
    column_agg = columncrt["aggregate"]
    support_agg = support_motion["aggregate"]
    unused_agg = unused_target["aggregate"]

    modulus = int(hull_agg["combined_crt_modulus"])
    support_width = int(hull_agg["support_width"])
    actual_rows = [
        row for row in hull_rows if bool(row["supported_actual_packet_current"])
    ]
    if len(actual_rows) != 1:
        raise RuntimeError(f"expected one actual row, got {len(actual_rows)}")
    actual_row = actual_rows[0]
    actual_pair = str(actual_row["source_pair_key"])
    actual_residue = int(column_agg["actual_crt_residue"])
    actual_nearest = int(actual_row["nearest_representative"])
    support_by_pair = support_motion_index(support_motion["support_motion_rows"])

    formal_replacement_rows: list[dict[str, Any]] = []
    for row in hull_rows:
        if bool(row["supported_actual_packet_current"]):
            continue
        key = str(row["source_pair_key"])
        motion = support_by_pair[key]
        target_residue = int(row["combined_crt_residue"])
        signed_jump = signed_minimal_delta(target_residue, actual_residue, modulus)
        nearest_delta = int(row["nearest_representative"]) - actual_nearest
        formal_replacement_rows.append(
            {
                "target_pair_key": key,
                "target_residue": target_residue,
                "window_side": str(row["window_side"]),
                "nearest_representative": int(row["nearest_representative"]),
                "signed_crt_jump_from_actual": signed_jump,
                "abs_crt_jump_from_actual": abs(signed_jump),
                "nearest_representative_delta_from_actual": nearest_delta,
                "jump_minus_support_width": abs(signed_jump) - support_width,
                "required_common_side_depth": int(
                    motion["required_common_side_depth"]
                ),
                "endpoint_release_total_required": int(
                    motion["endpoint_release_total_required"]
                ),
                "requires_both_endpoint_release": bool(
                    motion["requires_both_endpoint_release"]
                ),
                "replacement_route": "existing_formal_pair_support_motion",
            }
        )

    unused_replacement_rows: list[dict[str, Any]] = []
    for row in unused_target["unused_target_arrival_rows"]:
        unused_replacement_rows.append(
            {
                "source_pair_key": str(row["source_pair_key"]),
                "target_unused_pair_key": str(row["target_unused_pair_key"]),
                "source_window_side": str(row["source_window_side"]),
                "abs_crt_jump_to_unused_target": int(
                    row["abs_crt_jump_to_unused_target"]
                ),
                "jump_minus_support_width": int(row["jump_minus_support_width"]),
                "new_side_residue_count": int(row["new_side_residue_count"]),
                "needs_new_generator_residue": bool(
                    row["needs_new_generator_residue"]
                ),
                "needs_new_fill_residue": bool(row["needs_new_fill_residue"]),
                "replacement_route": "unused_target_residue_arrival",
            }
        )

    if not formal_replacement_rows:
        raise RuntimeError("no formal replacement rows found")
    if not unused_replacement_rows:
        raise RuntimeError("no unused replacement rows found")

    min_formal_jump_row = min(
        formal_replacement_rows,
        key=lambda row: (
            int(row["abs_crt_jump_from_actual"]),
            int(row["endpoint_release_total_required"]),
            str(row["target_pair_key"]),
        ),
    )
    min_formal_release_row = min(
        formal_replacement_rows,
        key=lambda row: (
            int(row["endpoint_release_total_required"]),
            int(row["abs_crt_jump_from_actual"]),
            str(row["target_pair_key"]),
        ),
    )
    min_unused_jump_row = min(
        unused_replacement_rows,
        key=lambda row: (
            int(row["abs_crt_jump_to_unused_target"]),
            int(row["new_side_residue_count"]),
            str(row["target_unused_pair_key"]),
        ),
    )

    all_formal_jumps_exceed_support = all(
        int(row["abs_crt_jump_from_actual"]) > support_width
        for row in formal_replacement_rows
    )
    all_formal_release_exceeds_support = all(
        int(row["endpoint_release_total_required"]) > support_width
        for row in formal_replacement_rows
    )
    all_unused_jumps_exceed_support = all(
        int(row["abs_crt_jump_to_unused_target"]) > support_width
        for row in unused_replacement_rows
    )

    aggregate = {
        "bidirectional_hull_ledger": str(
            bidirectional_hull_path.relative_to(ROOT)
        ),
        "cut_anchor_columncrt_ledger": str(
            cut_anchor_columncrt_path.relative_to(ROOT)
        ),
        "support_motion_depth_ledger": str(
            support_motion_path.relative_to(ROOT)
        ),
        "unused_target_arrival_ledger": str(
            unused_target_path.relative_to(ROOT)
        ),
        "combined_crt_modulus": modulus,
        "support_interval": hull_agg["support_interval"],
        "support_width": support_width,
        "actual_anchor_pair": actual_pair,
        "actual_crt_residue": actual_residue,
        "actual_nearest_representative": actual_nearest,
        "formal_replacement_candidate_count": len(formal_replacement_rows),
        "unused_target_replacement_candidate_count": len(unused_replacement_rows),
        "unique_unused_target_pair_count": int(
            unused_agg["unique_unused_target_pair_count"]
        ),
        "min_formal_replacement_abs_crt_jump": int(
            min_formal_jump_row["abs_crt_jump_from_actual"]
        ),
        "min_formal_replacement_jump_minus_support_width": int(
            min_formal_jump_row["jump_minus_support_width"]
        ),
        "min_formal_replacement_pair": str(min_formal_jump_row["target_pair_key"]),
        "min_formal_replacement_endpoint_release": int(
            min_formal_release_row["endpoint_release_total_required"]
        ),
        "min_formal_replacement_release_pair": str(
            min_formal_release_row["target_pair_key"]
        ),
        "min_formal_release_to_support_width_ratio": int(
            min_formal_release_row["endpoint_release_total_required"]
        )
        / support_width,
        "min_unused_target_abs_crt_jump": int(
            min_unused_jump_row["abs_crt_jump_to_unused_target"]
        ),
        "min_unused_target_jump_minus_support_width": int(
            min_unused_jump_row["jump_minus_support_width"]
        ),
        "min_unused_target_pair": str(
            min_unused_jump_row["target_unused_pair_key"]
        ),
        "min_unused_target_new_side_residue_count": int(
            min_unused_jump_row["new_side_residue_count"]
        ),
        "all_formal_replacement_jumps_exceed_support_width": (
            all_formal_jumps_exceed_support
        ),
        "all_formal_replacement_releases_exceed_support_width": (
            all_formal_release_exceeds_support
        ),
        "all_formal_replacements_require_both_endpoint_release": all(
            bool(row["requires_both_endpoint_release"])
            for row in formal_replacement_rows
        ),
        "all_unused_target_jumps_exceed_support_width": (
            all_unused_jumps_exceed_support
        ),
        "all_unused_targets_need_new_side_residue": bool(
            unused_agg["all_unused_targets_need_new_side_residue"]
        ),
        "support_motion_depth_closed_current_sweep": bool(
            support_agg["support_motion_depth_closed_current_sweep"]
        ),
        "unused_target_arrival_closed_current_sweep": bool(
            unused_agg["unused_target_arrival_closed_current_sweep"]
        ),
        "cut_anchor_columncrt_compression_closed_current_sweep": bool(
            column_agg["cut_anchor_columncrt_compression_closed_current_sweep"]
        ),
        "actual_anchor_replacement_closed_current_sweep": (
            all_formal_jumps_exceed_support
            and all_formal_release_exceeds_support
            and all_unused_jumps_exceed_support
            and bool(unused_agg["all_unused_targets_need_new_side_residue"])
            and bool(support_agg["support_motion_depth_closed_current_sweep"])
            and bool(unused_agg["unused_target_arrival_closed_current_sweep"])
        ),
        "global_actual_anchor_replacement_excluded": False,
        "row_column_unconditional_closed": False,
    }

    return {
        "certificate_type": (
            "prime_matrix_affine_twin_endpoint_release_"
            "actual_anchor_replacement_audit"
        ),
        "status": "current_sweep_actual_anchor_replacement_closed_global_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "aggregate": aggregate,
        "formal_replacement_rows": sorted(
            formal_replacement_rows,
            key=lambda row: int(row["abs_crt_jump_from_actual"]),
        ),
        "unused_target_replacement_rows": sorted(
            unused_replacement_rows,
            key=lambda row: int(row["abs_crt_jump_to_unused_target"]),
        ),
        "contract": {
            "actual_anchor_replacement_gate": [
                "if the current actual anchor is retained, use cut-anchor ColumnCRT compression",
                "if an existing formal pair replaces the anchor, pay the CRT jump and support-motion endpoint release",
                "if an unused target replaces the anchor, introduce new side residues and pay the unused-target CRT jump",
                "no current replacement route stays inside the primitive support width",
            ],
            "closed_current_sweep": aggregate[
                "actual_anchor_replacement_closed_current_sweep"
            ],
            "global_remaining": [
                "ActualAnchorReplacementGlobalNoGo",
                "SupportMotionDepthNonPersistence",
                "UnusedTargetResidueArrivalBoundOrPDEC",
                "CutAnchorColumnCRTPDECExclusion",
                "MovingFamilySAEColumnCRT",
            ],
        },
        "dependency_hashes": {
            str(path.relative_to(ROOT)): sha256(path)
            for path in (
                bidirectional_hull_path,
                cut_anchor_columncrt_path,
                support_motion_path,
                unused_target_path,
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
        "# Prime Matrix AffineTwin endpoint-release actual-anchor replacement audit",
        "",
        "**状态：** `current_sweep_actual_anchor_replacement_closed_global_open`",
        "",
        "本审计继续下钻 cut-anchor ColumnCRT compression 后的逃逸：若反例链不保留当前 actual anchor `19:8`，则必须让另一个 formal pair 或未使用 target residue 成为 actual。两条路线都需要超过当前 support width 的 CRT 相位跳跃。",
        "",
        "```text",
        f"combined_crt_modulus={agg['combined_crt_modulus']}",
        f"support_width={agg['support_width']}",
        f"actual_anchor_pair={agg['actual_anchor_pair']}",
        f"actual_crt_residue={agg['actual_crt_residue']}",
        f"formal_replacement_candidate_count={agg['formal_replacement_candidate_count']}",
        f"min_formal_replacement_pair={agg['min_formal_replacement_pair']}",
        f"min_formal_replacement_abs_crt_jump={agg['min_formal_replacement_abs_crt_jump']}",
        f"min_formal_replacement_endpoint_release={agg['min_formal_replacement_endpoint_release']}",
        f"min_formal_release_to_support_width_ratio={fmt_decimal(agg['min_formal_release_to_support_width_ratio'])}",
        f"unused_target_replacement_candidate_count={agg['unused_target_replacement_candidate_count']}",
        f"unique_unused_target_pair_count={agg['unique_unused_target_pair_count']}",
        f"min_unused_target_pair={agg['min_unused_target_pair']}",
        f"min_unused_target_abs_crt_jump={agg['min_unused_target_abs_crt_jump']}",
        f"min_unused_target_new_side_residue_count={agg['min_unused_target_new_side_residue_count']}",
        f"all_formal_replacement_jumps_exceed_support_width={fmt_bool(agg['all_formal_replacement_jumps_exceed_support_width'])}",
        f"all_formal_replacement_releases_exceed_support_width={fmt_bool(agg['all_formal_replacement_releases_exceed_support_width'])}",
        f"all_unused_target_jumps_exceed_support_width={fmt_bool(agg['all_unused_target_jumps_exceed_support_width'])}",
        f"all_unused_targets_need_new_side_residue={fmt_bool(agg['all_unused_targets_need_new_side_residue'])}",
        f"actual_anchor_replacement_closed_current_sweep={fmt_bool(agg['actual_anchor_replacement_closed_current_sweep'])}",
        "```",
        "",
        "## 1. existing formal pair replacement",
        "",
        "| target pair | side | target residue | signed jump | abs jump | release | both endpoints |",
        "| --- | --- | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in result["formal_replacement_rows"]:
        lines.append(
            "| `{}` | `{}` | {} | {} | {} | {} | `{}` |".format(
                row["target_pair_key"],
                row["window_side"],
                row["target_residue"],
                row["signed_crt_jump_from_actual"],
                row["abs_crt_jump_from_actual"],
                row["endpoint_release_total_required"],
                fmt_bool(row["requires_both_endpoint_release"]),
            )
        )

    lines.extend(
        [
            "",
            "## 2. unused target replacement",
            "",
            "| source pair | target pair | side | abs CRT jump | jump-support | new side residues |",
            "| --- | --- | --- | ---: | ---: | ---: |",
        ]
    )
    for row in result["unused_target_replacement_rows"]:
        lines.append(
            "| `{}` | `{}` | `{}` | {} | {} | {} |".format(
                row["source_pair_key"],
                row["target_unused_pair_key"],
                row["source_window_side"],
                row["abs_crt_jump_to_unused_target"],
                row["jump_minus_support_width"],
                row["new_side_residue_count"],
            )
        )

    lines.extend(
        [
            "",
            "## 3. 显式矛盾点",
            "",
            f"保留 actual anchor 时，上一层已经压缩为固定 `P == {agg['actual_crt_residue']} mod {agg['combined_crt_modulus']}` 的单个 ColumnCRT 原子。若改由现有 formal pair 替换 actual anchor，最小 CRT 跳跃是 `{agg['min_formal_replacement_abs_crt_jump']}`，来自 `{agg['min_formal_replacement_pair']}`，已经超过 support width `{agg['support_width']}`；同时最小双端点释放为 `{agg['min_formal_replacement_endpoint_release']}`，是 support width 的 `{fmt_decimal(agg['min_formal_release_to_support_width_ratio'])}` 倍。",
            "",
            f"若改由未使用 target residue 替换 actual anchor，最小 CRT 跳跃为 `{agg['min_unused_target_abs_crt_jump']}`，来自 target `{agg['min_unused_target_pair']}`，仍超过 support width，并且至少要新增 `{agg['min_unused_target_new_side_residue_count']}` 个侧残基。两条 actual-anchor replacement 路线都不能在当前 primitive support 内完成。",
            "",
            "## 4. 结论边界",
            "",
            "- 本步关闭当前 sweep 的 actual-anchor replacement 吸收解释。",
            "- 本步仍不证明全局行/列命题；剩余是把 replacement no-go 升格为全局族定理，或排斥 support-motion、unused-target arrival、ColumnCRT/PDEC 与 moving-family 出口。",
            "",
            "## 5. 依赖哈希",
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
        "--bidirectional-hull-ledger",
        type=Path,
        default=BIDIRECTIONAL_HULL_LEDGER,
        help="bidirectional skew-hull ledger path",
    )
    parser.add_argument(
        "--cut-anchor-columncrt-ledger",
        type=Path,
        default=CUT_ANCHOR_COLUMNCRT_LEDGER,
        help="cut-anchor ColumnCRT compression ledger path",
    )
    parser.add_argument(
        "--support-motion-ledger",
        type=Path,
        default=SUPPORT_MOTION_LEDGER,
        help="support-motion depth ledger path",
    )
    parser.add_argument(
        "--unused-target-ledger",
        type=Path,
        default=UNUSED_TARGET_LEDGER,
        help="unused-target arrival ledger path",
    )
    args = parser.parse_args()
    result = build_result(
        args.bidirectional_hull_ledger,
        args.cut_anchor_columncrt_ledger,
        args.support_motion_ledger,
        args.unused_target_ledger,
    )
    write_outputs(result)
    print(json.dumps(result["aggregate"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
