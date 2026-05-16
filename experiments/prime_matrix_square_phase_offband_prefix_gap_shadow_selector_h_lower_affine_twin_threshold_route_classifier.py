#!/usr/bin/env python3
"""分类 AffineTwin 整数阈值穿越的最小补齐路线。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_affine_twin_threshold_route_classifier.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-threshold-route-classifier.json

输出：
  data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-threshold-route-classifier-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-threshold-route-classifier.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-threshold-route-classifier.md
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

THRESHOLD_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-integer-threshold-deficit-ledger.json"
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-threshold-route-classifier-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-threshold-route-classifier.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-threshold-route-classifier.md"

NEXT_TARGET = "AffineTwinFillCatchUpOrMixedCoaccumulationPDECExclusion"


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def classify_witnesses(witnesses: list[dict[str, int]]) -> str:
    """按最小补齐见证分类。"""
    has_fill_only = any(w["extra_generator_residues"] == 0 and w["extra_fill_residues"] > 0 for w in witnesses)
    has_mixed = any(w["extra_generator_residues"] > 0 and w["extra_fill_residues"] > 0 for w in witnesses)
    has_generator_only = any(w["extra_generator_residues"] > 0 and w["extra_fill_residues"] == 0 for w in witnesses)
    if has_fill_only and not has_mixed and not has_generator_only:
        return "FillCatchUpOnly"
    if has_fill_only and has_mixed:
        return "FillCatchUpOrMixed"
    if has_mixed and not has_fill_only and not has_generator_only:
        return "MixedCoaccumulationOnly"
    if has_generator_only and not has_fill_only and not has_mixed:
        return "GeneratorOnly"
    return "Composite"


def route_row(row: dict[str, Any]) -> dict[str, Any]:
    """构造一个 q 的阈值穿越路线分类行。"""
    witnesses = list(row["min_crossing_witnesses"])
    route = classify_witnesses(witnesses)
    min_extra_fill = min(w["extra_fill_residues"] for w in witnesses)
    min_extra_generator = min(w["extra_generator_residues"] for w in witnesses)
    max_new_fill = max(w["new_fill_used"] for w in witnesses)
    max_new_generator = max(w["new_generator_used"] for w in witnesses)
    fill_used = int(row["fill_used_residue_count"])
    generator_used = int(row["generator_used_residue_count"])
    return {
        "q": int(row["q"]),
        "generator_ell": int(row["generator_ell"]),
        "fill_ell": int(row["fill_ell"]),
        "current_generator_used": generator_used,
        "current_fill_used": fill_used,
        "current_residue_product": int(row["current_residue_product"]),
        "integer_safe_product_threshold": int(row["integer_safe_product_threshold"]),
        "integer_product_slack": int(row["integer_product_slack"]),
        "min_total_extra_residues_to_cross": int(row["min_total_extra_residues_to_cross"]),
        "route_class": route,
        "minimal_route_requires_fill_increment": min_extra_fill > 0,
        "minimal_route_can_be_fill_only": any(
            w["extra_generator_residues"] == 0 and w["extra_fill_residues"] > 0 for w in witnesses
        ),
        "minimal_route_can_be_mixed": any(
            w["extra_generator_residues"] > 0 and w["extra_fill_residues"] > 0 for w in witnesses
        ),
        "minimal_route_can_be_generator_only": any(
            w["extra_generator_residues"] > 0 and w["extra_fill_residues"] == 0 for w in witnesses
        ),
        "min_extra_fill_in_minimal_routes": min_extra_fill,
        "min_extra_generator_in_minimal_routes": min_extra_generator,
        "max_new_fill_in_minimal_routes": max_new_fill,
        "max_new_generator_in_minimal_routes": max_new_generator,
        "fill_catchup_multiplier_upper": max_new_fill / fill_used if fill_used else None,
        "generator_catchup_multiplier_upper": max_new_generator / generator_used if generator_used else None,
        "fill_activation_delay_over_generator": int(row["fill_activation_delay_over_generator"]),
        "fill_delay_per_required_fill_increment": (
            int(row["fill_activation_delay_over_generator"]) / min_extra_fill if min_extra_fill else None
        ),
        "min_crossing_witnesses": witnesses,
        "threshold_crossing_pdec_name": f"AffineTwin-{route}-ThresholdCrossing-PDEC",
        "realized_current_sweep": bool(row["realized_current_sweep"]),
    }


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "minimal_threshold_crossing_routes_classified",
            "status": "closed_current_sweep",
            "statement": "Every current q has an explicit minimal crossing route; all minimal routes require fill-side residue growth.",
        },
        {
            "name": "fill_catchup_and_mixed_routes_split",
            "status": "closed_routing",
            "statement": "Threshold crossing splits into FillCatchUp-only, MixedCoaccumulation-only, or composite route classes with named PDEC labels.",
        },
        {
            "name": "global_fill_catchup_or_mixed_exclusion",
            "status": "open",
            "statement": "A self-contained proof must exclude persistent fill-side catch-up or mixed coaccumulation, or close the named PDEC/ColumnCRT families.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    agg = result["aggregate"]
    return [
        {
            "gate": "MinimalRoutesClassified",
            "closed": True,
            "proved": True,
            "meaning": "阈值穿越的最小补齐路线已逐 q 分类。",
            "remaining": "closed",
        },
        {
            "gate": "AllMinimalRoutesRequireFillIncrement",
            "closed": agg["all_minimal_routes_require_fill_increment"],
            "proved": False,
            "meaning": "当前所有最小穿越路线都必须增加 fill 侧 residue。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "RoutePDECsNamed",
            "closed": True,
            "proved": True,
            "meaning": "fill-only 与 mixed 补齐失败形态已命名为具体 PDEC。",
            "remaining": "exclusion still separate",
        },
        {
            "gate": "GlobalFillCatchupExcluded",
            "closed": False,
            "proved": False,
            "meaning": "仍需全局证明 fill 侧不能持久追赶到阈值，或排斥对应 PDEC。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只完成阈值穿越路线分类，不关闭全局行/列命题。",
            "remaining": NEXT_TARGET,
        },
    ]


def build_result(threshold_ledger: Path) -> dict[str, Any]:
    """构造阈值路线分类结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    threshold = load_json(threshold_ledger)
    rows = [route_row(row) for row in threshold["integer_threshold_deficit_rows"]]
    route_histogram: dict[str, int] = {}
    for row in rows:
        route_histogram[row["route_class"]] = route_histogram.get(row["route_class"], 0) + 1
    aggregate = {
        "threshold_ledger": str(threshold_ledger.relative_to(ROOT)),
        "candidate_q_values": [row["q"] for row in rows],
        "realized_q_values": [row["q"] for row in rows if row["realized_current_sweep"]],
        "route_class_histogram": route_histogram,
        "all_minimal_routes_require_fill_increment": all(
            row["minimal_route_requires_fill_increment"] for row in rows
        ),
        "fill_only_route_q_values": [
            row["q"] for row in rows if row["route_class"] == "FillCatchUpOnly"
        ],
        "mixed_only_route_q_values": [
            row["q"] for row in rows if row["route_class"] == "MixedCoaccumulationOnly"
        ],
        "composite_route_q_values": [
            row["q"] for row in rows if row["route_class"] not in {"FillCatchUpOnly", "MixedCoaccumulationOnly"}
        ],
        "max_fill_catchup_multiplier_upper": max(
            row["fill_catchup_multiplier_upper"] for row in rows if row["fill_catchup_multiplier_upper"] is not None
        ),
        "min_fill_delay_per_required_fill_increment": min(
            row["fill_delay_per_required_fill_increment"]
            for row in rows
            if row["fill_delay_per_required_fill_increment"] is not None
        ),
        "route_classifier_closed_current_sweep": True,
        "fill_catchup_or_mixed_pdec_excluded_globally": False,
        "row_column_unconditional_closed": False,
    }
    ledger = {
        "aggregate": aggregate,
        "threshold_route_rows": rows,
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    result = {
        "certificate_type": (
            "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_"
            "affine_twin_threshold_route_classifier"
        ),
        "status": "affine_twin_threshold_crossing_routes_classified_global_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_sweep_not_used_as_global_proof": True,
        "aggregate": aggregate,
        "threshold_route_rows": rows,
        "fill_catchup_or_mixed_pdec_excluded_globally": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": "AffineTwinThresholdDeficitBoundOrThresholdCrossingPDECExclusion",
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "plain_conclusion": (
            "本步把整数阈值穿越缺口继续拆成最小补齐路线。当前所有最小穿越路线都需要 "
            "fill 侧新增 residue；`q=31` 是 mixed coaccumulation-only，`q=43,103` "
            "允许 fill-catchup 或 mixed 两种最小补齐，且没有 generator-only 最小路线。最大 fill catch-up 倍率上界为 "
            f"{aggregate['max_fill_catchup_multiplier_upper']:.6f}，最小 fill 延迟/所需新增 fill "
            f"为 {aggregate['min_fill_delay_per_required_fill_increment']:.6f}。"
            "因此最新硬点从总阈值穿越压成：排斥 fill 侧持久追赶或 mixed 双侧同步补齐。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    result["source_hashes"] = {
        "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_affine_twin_threshold_route_classifier.py": sha256(
            Path(__file__).resolve()
        ),
        "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-integer-threshold-deficit-ledger.json": sha256(
            threshold_ledger
        ),
        "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-threshold-route-classifier-ledger.json": sha256(
            OUT_LEDGER
        ),
    }
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow selector H lower affine twin threshold route classifier",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"candidate_q_values={agg['candidate_q_values']}",
        f"route_class_histogram={agg['route_class_histogram']}",
        f"all_minimal_routes_require_fill_increment={fmt_bool(agg['all_minimal_routes_require_fill_increment'])}",
        f"fill_only_route_q_values={agg['fill_only_route_q_values']}",
        f"mixed_only_route_q_values={agg['mixed_only_route_q_values']}",
        f"max_fill_catchup_multiplier_upper={agg['max_fill_catchup_multiplier_upper']:.12f}",
        f"min_fill_delay_per_required_fill_increment={agg['min_fill_delay_per_required_fill_increment']:.12f}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 路线分类",
        "",
        "| q | route | min extra | fill extra min | gen extra min | fill multiplier | delay/fill | PDEC |",
        "| ---: | --- | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in result["threshold_route_rows"]:
        lines.append(
            f"| {row['q']} | `{row['route_class']}` | {row['min_total_extra_residues_to_cross']} | "
            f"{row['min_extra_fill_in_minimal_routes']} | {row['min_extra_generator_in_minimal_routes']} | "
            f"{row['fill_catchup_multiplier_upper']:.6f} | "
            f"{row['fill_delay_per_required_fill_increment']:.6f} | "
            f"`{row['threshold_crossing_pdec_name']}` |"
        )
    lines.extend(
        [
            "",
            "## 2. 结论",
            "",
            "- 最小穿越路线没有 generator-only 情形。",
            "- `q=31` 必须双侧共同补齐；`q=43,103` 存在 fill-only 追赶路线，也允许少量 mixed 路线，但都必须新增 fill 侧 residue。",
            "- 因此下一步只需攻 fill-catchup 与 mixed-coaccumulation 两类持久 PDEC。",
            "",
            "## 3. 命题行",
            "",
            "| name | status | statement |",
            "| --- | --- | --- |",
        ]
    )
    for row in result["theorem_rows"]:
        lines.append(f"| `{row['name']}` | `{row['status']}` | {table_cell(row['statement'])} |")
    lines.extend(
        [
            "",
            "## 4. 决策表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | ---: | ---: | --- | --- |",
        ]
    )
    for row in result["decision_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{row['gate']}`",
                    f"`{fmt_bool(row['closed'])}`",
                    f"`{fmt_bool(row['proved'])}`",
                    table_cell(row["meaning"]),
                    table_cell(row["remaining"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 5. 下一步",
            "",
            f"- 主攻：`{result['next_direct_attack_target']}`。",
            "- fill-catchup 线：证明 fill 侧晚激活后无法补足最小新增 residue。",
            "- mixed 线：证明双侧同时新增到最小见证会触发固定双模 ColumnCRT/PDEC。",
            "",
            "## 6. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in result["source_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--threshold-ledger", type=Path, default=THRESHOLD_LEDGER)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    threshold_ledger = args.threshold_ledger if args.threshold_ledger.is_absolute() else ROOT / args.threshold_ledger
    result = build_result(threshold_ledger)
    write_markdown(result)
    result["source_hashes"][
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-threshold-route-classifier.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "route_class_histogram": result["aggregate"]["route_class_histogram"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
