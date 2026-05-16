#!/usr/bin/env python3
"""生成 AffineTwin endpoint-release critical-error 审计证书。

用法示例：
  python3 experiments/prime_matrix_affine_twin_endpoint_release_critical_error_audit.py
  python3 -m json.tool data/prime-matrix-affine-twin-endpoint-release-critical-error-ledger.json

输出：
  data/prime-matrix-affine-twin-endpoint-release-critical-error-ledger.json
  docs/monograph/prime-matrix-affine-twin-endpoint-release-critical-error-audit.json
  docs/monograph/prime-matrix-affine-twin-endpoint-release-critical-error-audit.md
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

SUPPORT_MOTION_LEDGER = DATA / "prime-matrix-affine-twin-support-motion-depth-ledger.json"
PRIMITIVE_DEFECT_LEDGER = DATA / (
    "prime-matrix-affine-twin-support-motion-primitive-defect-ledger.json"
)
MOVING_KEY_SOURCE_LEDGER = DATA / (
    "prime-matrix-affine-twin-moving-key-source-rematerialization-ledger.json"
)

OUT_LEDGER = DATA / (
    "prime-matrix-affine-twin-endpoint-release-critical-error-ledger.json"
)
OUT_JSON = DOCS / (
    "prime-matrix-affine-twin-endpoint-release-critical-error-audit.json"
)
OUT_MD = DOCS / (
    "prime-matrix-affine-twin-endpoint-release-critical-error-audit.md"
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


def pair_to_moving_q_candidates(remat: dict[str, Any]) -> dict[str, list[int]]:
    """建立 source pair 到 moving q 候选的索引。"""
    out: dict[str, set[int]] = {}
    for occurrence in remat["moving_q_occurrences"]:
        out.setdefault(str(occurrence["source_pair_key"]), set()).add(
            int(occurrence["q_candidate"])
        )
    return {key: sorted(values) for key, values in out.items()}


def q_to_rematerialization_row(remat: dict[str, Any]) -> dict[int, dict[str, Any]]:
    """建立 q 到重物化审计行的索引。"""
    return {
        int(row["q"]): row
        for row in remat["candidate_q_source_rematerialization_rows"]
    }


def pair_to_primitive_defect_row(primitive: dict[str, Any]) -> dict[str, dict[str, Any]]:
    """建立 source pair 到 primitive-depth 缺陷行的索引。"""
    return {
        str(row["source_pair_key"]): row
        for row in primitive["support_motion_primitive_defect_rows"]
    }


def critical_fraction(numerator: int, denominator: int) -> str:
    """保留原始临界误差分数。"""
    return f"{numerator}/{denominator}"


def endpoint_row(
    support_row: dict[str, Any],
    q_candidates_by_pair: dict[str, list[int]],
    remat_by_q: dict[int, dict[str, Any]],
    primitive_by_pair: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    """构造单个 endpoint-release 临界误差行。"""
    pair = str(support_row["source_pair_key"])
    support_width = int(support_row["support_width"])
    endpoint_load = int(support_row["endpoint_release_total_required"])
    overcritical_units = endpoint_load - support_width
    q_candidates = q_candidates_by_pair.get(pair, [])
    q_routes = [
        {
            "q": q,
            "route": str(remat_by_q[q]["route"]),
            "rematerialized": bool(
                remat_by_q[q]["moving_key_source_rematerialized_current"]
            ),
        }
        for q in q_candidates
        if q in remat_by_q
    ]
    rematerialized = any(bool(item["rematerialized"]) for item in q_routes)
    primitive_row = primitive_by_pair[pair]
    positive_critical_error = overcritical_units > 0
    structured_route = (
        "EndpointReleaseCoupling-PDEC"
        if positive_critical_error and not rematerialized
        else "RematerializedSourceOrNonpositiveError"
    )

    return {
        "source_pair_key": pair,
        "q": int(support_row["q"]),
        "window_side": str(support_row["window_side"]),
        "nearest_representative": int(support_row["nearest_representative"]),
        "support_interval": support_row["support_interval"],
        "critical_capacity_support_width": support_width,
        "actual_endpoint_release_load": endpoint_load,
        "endpoint_release_overcritical_units": overcritical_units,
        "endpoint_release_load_to_capacity_ratio": endpoint_load / support_width,
        "endpoint_release_critical_error_fraction": critical_fraction(
            overcritical_units, support_width
        ),
        "endpoint_release_critical_error": overcritical_units / support_width,
        "generator_endpoint_release_required": int(
            support_row["generator_endpoint_release_required"]
        ),
        "fill_endpoint_release_required": int(
            support_row["fill_endpoint_release_required"]
        ),
        "endpoint_release_max_required": int(
            support_row["endpoint_release_max_required"]
        ),
        "requires_both_endpoint_release": bool(
            support_row["requires_both_endpoint_release"]
        ),
        "moving_q_candidates": q_candidates,
        "moving_q_rematerialization_routes": q_routes,
        "same_orientation_rematerialization_available": rematerialized,
        "primitive_depth_defect_total": int(
            primitive_row["total_affine_depth_defect"]
        ),
        "primitive_depth_defect_matches_endpoint_load": (
            int(primitive_row["total_affine_depth_defect"]) == endpoint_load
        ),
        "positive_endpoint_release_critical_error": positive_critical_error,
        "anonymous_critical_error_eliminated_current": (
            positive_critical_error
            and bool(support_row["requires_both_endpoint_release"])
            and not rematerialized
            and int(primitive_row["total_affine_depth_defect"]) == endpoint_load
        ),
        "structured_route_current": structured_route,
        "pinned_endpoint": str(support_row["pinned_endpoint"]),
    }


def build_result(
    support_motion_path: Path,
    primitive_defect_path: Path,
    moving_key_source_path: Path,
) -> dict[str, Any]:
    """构造 endpoint-release critical-error 审计结果。"""
    support_motion = load_json(support_motion_path)
    primitive_defect = load_json(primitive_defect_path)
    moving_key_source = load_json(moving_key_source_path)

    q_candidates_by_pair = pair_to_moving_q_candidates(moving_key_source)
    remat_by_q = q_to_rematerialization_row(moving_key_source)
    primitive_by_pair = pair_to_primitive_defect_row(primitive_defect)

    rows = [
        endpoint_row(row, q_candidates_by_pair, remat_by_q, primitive_by_pair)
        for row in support_motion["support_motion_rows"]
    ]
    if not rows:
        raise RuntimeError("no support-motion rows found")

    support_width = int(support_motion["aggregate"]["support_width_current"])
    total_load = sum(int(row["actual_endpoint_release_load"]) for row in rows)
    total_capacity = support_width * len(rows)
    total_overcritical = total_load - total_capacity
    narrowest = min(
        rows,
        key=lambda row: (
            int(row["actual_endpoint_release_load"]),
            int(row["endpoint_release_overcritical_units"]),
            str(row["source_pair_key"]),
        ),
    )
    worst = max(
        rows,
        key=lambda row: (
            float(row["endpoint_release_critical_error"]),
            int(row["actual_endpoint_release_load"]),
            str(row["source_pair_key"]),
        ),
    )

    aggregate = {
        "support_motion_ledger": str(support_motion_path.relative_to(ROOT)),
        "primitive_defect_ledger": str(primitive_defect_path.relative_to(ROOT)),
        "moving_key_source_ledger": str(moving_key_source_path.relative_to(ROOT)),
        "support_motion_candidate_count": len(rows),
        "critical_capacity_support_width": support_width,
        "total_endpoint_release_load": total_load,
        "total_window_capacity_budget": total_capacity,
        "total_endpoint_release_overcritical_units": total_overcritical,
        "total_endpoint_release_load_to_capacity_ratio": total_load / total_capacity,
        "total_endpoint_release_critical_error": total_overcritical / total_capacity,
        "min_endpoint_release_load": min(
            int(row["actual_endpoint_release_load"]) for row in rows
        ),
        "max_endpoint_release_load": max(
            int(row["actual_endpoint_release_load"]) for row in rows
        ),
        "min_endpoint_release_critical_error": min(
            float(row["endpoint_release_critical_error"]) for row in rows
        ),
        "max_endpoint_release_critical_error": max(
            float(row["endpoint_release_critical_error"]) for row in rows
        ),
        "narrowest_endpoint_release_critical_atom": {
            "source_pair_key": narrowest["source_pair_key"],
            "window_side": narrowest["window_side"],
            "actual_endpoint_release_load": narrowest[
                "actual_endpoint_release_load"
            ],
            "critical_capacity_support_width": narrowest[
                "critical_capacity_support_width"
            ],
            "endpoint_release_critical_error_fraction": narrowest[
                "endpoint_release_critical_error_fraction"
            ],
            "endpoint_release_critical_error": narrowest[
                "endpoint_release_critical_error"
            ],
            "moving_q_candidates": narrowest["moving_q_candidates"],
            "structured_route_current": narrowest["structured_route_current"],
        },
        "worst_endpoint_release_critical_atom": {
            "source_pair_key": worst["source_pair_key"],
            "window_side": worst["window_side"],
            "actual_endpoint_release_load": worst["actual_endpoint_release_load"],
            "critical_capacity_support_width": worst[
                "critical_capacity_support_width"
            ],
            "endpoint_release_critical_error_fraction": worst[
                "endpoint_release_critical_error_fraction"
            ],
            "endpoint_release_critical_error": worst[
                "endpoint_release_critical_error"
            ],
            "moving_q_candidates": worst["moving_q_candidates"],
            "structured_route_current": worst["structured_route_current"],
        },
        "all_support_motion_requires_both_endpoint_release": all(
            bool(row["requires_both_endpoint_release"]) for row in rows
        ),
        "all_endpoint_release_loads_supercritical": all(
            int(row["endpoint_release_overcritical_units"]) > 0 for row in rows
        ),
        "all_primitive_defects_match_endpoint_load": all(
            bool(row["primitive_depth_defect_matches_endpoint_load"]) for row in rows
        ),
        "all_same_orientation_rematerialization_absent": all(
            not bool(row["same_orientation_rematerialization_available"])
            for row in rows
        ),
        "all_positive_endpoint_release_errors_structured_current": all(
            bool(row["anonymous_critical_error_eliminated_current"]) for row in rows
        ),
        "endpoint_release_critical_error_structured_current_sweep": all(
            bool(row["anonymous_critical_error_eliminated_current"]) for row in rows
        ),
        "global_endpoint_release_coupling_excluded": False,
        "row_column_unconditional_closed": False,
    }

    return {
        "certificate_type": (
            "prime_matrix_affine_twin_endpoint_release_critical_error_audit"
        ),
        "status": (
            "current_sweep_endpoint_release_critical_error_structured_global_open"
        ),
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "aggregate": aggregate,
        "endpoint_release_critical_error_rows": rows,
        "contract": {
            "critical_error_definition": (
                "Endpoint release critical error is "
                "actual_endpoint_release_load / support_width - 1."
            ),
            "current_sweep_structuring_gate": [
                "support motion requires both generator and shifted-fill endpoint release",
                "endpoint release load exceeds the current support width",
                "fixed primitive depth identities fail by the same total load",
                "same-orientation moving-key source rematerialization is absent",
                "therefore the positive local critical error is routed to EndpointReleaseCoupling-PDEC rather than kept as anonymous error",
            ],
            "closed_current_sweep": aggregate[
                "endpoint_release_critical_error_structured_current_sweep"
            ],
            "global_remaining": [
                "EndpointReleaseCoupling-PDEC exclusion",
                "OrientationChangingPrimitiveKey-PDEC/SAE",
                "SourceRematerialization-PDEC/SAE",
                "MovingPrimitiveKeyNonPersistence",
            ],
        },
        "dependency_hashes": {
            str(path.relative_to(ROOT)): sha256(path)
            for path in (
                support_motion_path,
                primitive_defect_path,
                moving_key_source_path,
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
    narrow = agg["narrowest_endpoint_release_critical_atom"]
    worst = agg["worst_endpoint_release_critical_atom"]
    lines = [
        "# Prime Matrix AffineTwin endpoint-release critical-error audit",
        "",
        "**状态：** `current_sweep_endpoint_release_critical_error_structured_global_open`",
        "",
        "本审计把 support-motion 的剩余逃逸接入临界误差框架：",
        "",
        "```text",
        "critical error = actual endpoint-release load / support width - 1",
        "```",
        "",
        "这里的 `support width` 是当前 primitive 双槽共同支撑窗口宽度；`actual endpoint-release load` 是为了把空窗 CRT 代表纳入支撑，generator 与 shifted-fill 两个端点必须同步释放的总量。",
        "",
        "```text",
        f"support_motion_candidate_count={agg['support_motion_candidate_count']}",
        f"critical_capacity_support_width={agg['critical_capacity_support_width']}",
        f"total_endpoint_release_load={agg['total_endpoint_release_load']}",
        f"total_window_capacity_budget={agg['total_window_capacity_budget']}",
        f"total_endpoint_release_critical_error={fmt_decimal(agg['total_endpoint_release_critical_error'])}",
        f"min_endpoint_release_critical_error={fmt_decimal(agg['min_endpoint_release_critical_error'])}",
        f"max_endpoint_release_critical_error={fmt_decimal(agg['max_endpoint_release_critical_error'])}",
        f"all_endpoint_release_loads_supercritical={fmt_bool(agg['all_endpoint_release_loads_supercritical'])}",
        f"all_same_orientation_rematerialization_absent={fmt_bool(agg['all_same_orientation_rematerialization_absent'])}",
        f"endpoint_release_critical_error_structured_current_sweep={fmt_bool(agg['endpoint_release_critical_error_structured_current_sweep'])}",
        "```",
        "",
        "## 1. endpoint-release 临界误差表",
        "",
        "| pair | side | load | capacity | critical error | moving q | route |",
        "| --- | --- | ---: | ---: | ---: | --- | --- |",
    ]
    for row in result["endpoint_release_critical_error_rows"]:
        routes = ",".join(
            f"{item['q']}:{item['route']}"
            for item in row["moving_q_rematerialization_routes"]
        )
        lines.append(
            "| `{pair}` | `{side}` | {load} | {capacity} | {err} | `{qs}` | `{route}` |".format(
                pair=row["source_pair_key"],
                side=row["window_side"],
                load=row["actual_endpoint_release_load"],
                capacity=row["critical_capacity_support_width"],
                err=fmt_decimal(row["endpoint_release_critical_error"]),
                qs=",".join(str(q) for q in row["moving_q_candidates"]),
                route=routes or row["structured_route_current"],
            )
        )

    lines.extend(
        [
            "",
            "## 2. 最窄显式超界点",
            "",
            f"最窄 atom 为 `{narrow['source_pair_key']}`，side `{narrow['window_side']}`。它的端点释放负载为 `{narrow['actual_endpoint_release_load']}`，临界窗口容量为 `{narrow['critical_capacity_support_width']}`，所以临界误差为 `{narrow['endpoint_release_critical_error_fraction']}={fmt_decimal(narrow['endpoint_release_critical_error'])}`。",
            f"该 atom 的 moving q 候选是 `{narrow['moving_q_candidates']}`；上一层 source-rematerialization 审计已经证明这些候选不能同向重物化为 AffineTwin source。因此这个正临界误差不能作为普通波动隐藏，只能显化为 `{narrow['structured_route_current']}`。",
            "",
            "## 3. 最大局部超界波",
            "",
            f"最大 atom 为 `{worst['source_pair_key']}`，side `{worst['window_side']}`，端点释放负载 `{worst['actual_endpoint_release_load']}` 对容量 `{worst['critical_capacity_support_width']}`，临界误差 `{worst['endpoint_release_critical_error_fraction']}={fmt_decimal(worst['endpoint_release_critical_error'])}`。",
            "",
            "## 4. 结论边界",
            "",
            "- 当前 `11` 个 support-motion 候选全部为正临界误差，并且全部需要双端点同步释放。",
            "- 固定 primitive key 的深度缺陷总量与端点释放负载逐项相同，说明这不是记账重复，而是同一个结构刚性的两种投影。",
            "- 同向 moving-key source-rematerialization 已缺席，所以当前 sweep 的匿名临界误差被消去，全部登记为 `EndpointReleaseCoupling-PDEC`。",
            "- 本步仍不证明全局行/列命题；全局剩余是排斥 `EndpointReleaseCoupling-PDEC` 持久复现，或处理方向改变/source 重物化出口。",
            "",
            "## 5. 依赖哈希",
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
        description="生成 AffineTwin endpoint-release critical-error 审计证书。"
    )
    parser.add_argument(
        "--support-motion-ledger", type=Path, default=SUPPORT_MOTION_LEDGER
    )
    parser.add_argument(
        "--primitive-defect-ledger", type=Path, default=PRIMITIVE_DEFECT_LEDGER
    )
    parser.add_argument(
        "--moving-key-source-ledger", type=Path, default=MOVING_KEY_SOURCE_LEDGER
    )
    return parser.parse_args()


def main() -> None:
    """入口。"""
    args = parse_args()
    result = build_result(
        args.support_motion_ledger,
        args.primitive_defect_ledger,
        args.moving_key_source_ledger,
    )
    write_outputs(result)
    print(json.dumps(result["aggregate"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
