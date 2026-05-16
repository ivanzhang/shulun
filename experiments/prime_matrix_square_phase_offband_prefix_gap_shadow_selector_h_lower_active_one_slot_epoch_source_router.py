#!/usr/bin/env python3
"""审计活跃一槽 epoch 的 ell 来源范围。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_active_one_slot_epoch_source_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-active-one-slot-epoch-source-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-selector-h-lower-active-one-slot-epoch-source-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-active-one-slot-epoch-source-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-active-one-slot-epoch-source-router.md
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

CAPACITY_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-one-slot-residue-epoch-capacity-ledger.json"
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-active-one-slot-epoch-source-ledger.json"
OUT_JSON = DOCS / (
    "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-"
    "active-one-slot-epoch-source-router.json"
)
OUT_MD = DOCS / (
    "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-"
    "active-one-slot-epoch-source-router.md"
)

MAIN_TARGET = "ActiveOneSlotEpochCountBoundOrTransportResetPDECExclusion"
NEXT_TARGET = "ActiveEllGrowthBoundOrTransportResetPDECExclusion"


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


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "active_epoch_source_materialized",
            "status": "closed",
            "statement": "The active one-slot epochs are exactly represented by their side and least-prime-factor ell source.",
        },
        {
            "name": "current_active_ell_band_finite",
            "status": "closed_on_current_sweep",
            "statement": "In the current sweep, all active one-slot epochs have ell in a finite low-mod band.",
        },
        {
            "name": "active_ell_growth_bound_open",
            "status": "open",
            "statement": "A global proof must bound the number of active ell sources per scale, or show growth forces transport reset-PDEC/SAE.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "ActiveEpochSourceMaterialized",
            "closed": True,
            "proved": True,
            "meaning": "活跃 epoch 已完全化为 `(side,ell)` 来源集合。",
            "remaining": "closed",
        },
        {
            "gate": "CurrentActiveEllBandFinite",
            "closed": True,
            "proved": False,
            "meaning": "当前活跃 ell 落在 `23..109`，但这只是有限扫描事实。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "ActiveEllGrowthBoundProved",
            "closed": False,
            "proved": False,
            "meaning": "尚未证明活跃 ell 数量随尺度有全局可求和控制。",
            "remaining": "ActiveEllGrowthBound",
        },
        {
            "gate": "TransportResetPDECExcluded",
            "closed": False,
            "proved": False,
            "meaning": "若活跃 ell 增长导致 residue 重复，仍需 reset-PDEC 排斥。",
            "remaining": "TransportResetPDECExclusion",
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只定位活跃 epoch 来源，不关闭全局命题。",
            "remaining": result["next_direct_attack_target"],
        },
    ]


def build_result(capacity_ledger: Path) -> dict[str, Any]:
    """构造活跃 ell 来源结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    source = load_json(capacity_ledger)
    rows = source["epoch_capacity_rows"]
    ell_values = sorted({int(row["ell"]) for row in rows})
    minus_ells = sorted({int(row["ell"]) for row in rows if row["side"] == "minus"})
    plus_ells = sorted({int(row["ell"]) for row in rows if row["side"] == "plus"})
    both = sorted(set(minus_ells).intersection(plus_ells))
    minus_only = sorted(set(minus_ells).difference(plus_ells))
    plus_only = sorted(set(plus_ells).difference(minus_ells))
    source_rows = []
    for ell in ell_values:
        items = [row for row in rows if int(row["ell"]) == ell]
        source_rows.append(
            {
                "ell": ell,
                "active_sides": sorted(row["side"] for row in items),
                "side_count": len(items),
                "used_residue_count": sum(int(row["used_residue_count"]) for row in items),
                "capacity": sum(int(row["epoch_residue_capacity"]) for row in items),
                "rankin_mass": sum(float(row["rankin_mass"]) for row in items),
                "p_min": min(int(row["p_min"]) for row in items),
                "p_max": max(int(row["p_max"]) for row in items),
            }
        )

    aggregate = {
        "capacity_ledger": str(capacity_ledger.relative_to(ROOT)),
        "active_epoch_count": len(rows),
        "distinct_active_ell_count": len(ell_values),
        "active_ell_min": min(ell_values),
        "active_ell_max": max(ell_values),
        "minus_epoch_count": len(minus_ells),
        "plus_epoch_count": len(plus_ells),
        "both_side_ell_count": len(both),
        "minus_only_ell_count": len(minus_only),
        "plus_only_ell_count": len(plus_only),
        "active_ell_values": ell_values,
        "both_side_ell_values": both,
        "minus_only_ell_values": minus_only,
        "plus_only_ell_values": plus_only,
        "active_epoch_source_materialized": True,
        "active_ell_growth_bound_proved": False,
        "transport_reset_pdec_excluded_globally": False,
        "row_column_unconditional_closed": False,
    }
    ledger = {
        "aggregate": aggregate,
        "active_ell_source_rows": source_rows,
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    result = {
        "certificate_type": (
            "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_"
            "active_one_slot_epoch_source_router"
        ),
        "status": "active_one_slot_epoch_sources_materialized_growth_bound_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_sweep_not_used_as_global_proof": True,
        "aggregate": aggregate,
        "active_ell_source_rows": source_rows,
        "active_ell_growth_bound_proved": False,
        "transport_reset_pdec_excluded_globally": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "plain_conclusion": (
            "本步把活跃一槽 epoch 数量界压成活跃 `ell` 来源界：当前有 "
            f"{len(rows)} 个 `(side,ell)` epoch，来自 {len(ell_values)} 个不同 `ell`，"
            f"范围为 `{min(ell_values)}..{max(ell_values)}`；其中 {len(both)} 个 `ell` 同时出现在正负侧。"
            "全局仍需证明活跃 `ell` 来源随尺度可控，或证明来源增长会触发 transport reset-PDEC/SAE。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    result["source_hashes"] = {
        "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_active_one_slot_epoch_source_router.py": sha256(
            Path(__file__).resolve()
        ),
        "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-one-slot-residue-epoch-capacity-ledger.json": sha256(
            capacity_ledger
        ),
        "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-active-one-slot-epoch-source-ledger.json": sha256(
            OUT_LEDGER
        ),
    }
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow selector H lower active one-slot epoch source router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"active_epoch_count={agg['active_epoch_count']}",
        f"distinct_active_ell_count={agg['distinct_active_ell_count']}",
        f"active_ell_min={agg['active_ell_min']}",
        f"active_ell_max={agg['active_ell_max']}",
        f"both_side_ell_count={agg['both_side_ell_count']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 活跃 ell 来源",
        "",
        "| ell | sides | used | capacity | Rankin mass | p range |",
        "| ---: | --- | ---: | ---: | ---: | --- |",
    ]
    for row in result["active_ell_source_rows"]:
        lines.append(
            f"| {row['ell']} | `{row['active_sides']}` | {row['used_residue_count']} | "
            f"{row['capacity']} | {row['rankin_mass']:.6f} | `{row['p_min']}..{row['p_max']}` |"
        )
    lines.extend(
        [
            "",
            "## 2. 结构判断",
            "",
            "- 单个 epoch 容量已经闭合后，Rankin 可求和只可能来自活跃 ell 来源数的全局控制。",
            "- 当前活跃 ell 是有限低模带，但不能把有限带直接外推为全局定理。",
            "- 若活跃 ell 来源持续增长，必须证明它触发 residue 重复、transport reset-PDEC 或 SAE/Rankin 稀疏化。",
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
            "- 证明活跃 ell 来源增长受限，或证明增长必然产生 reset-PDEC/SAE。",
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
    parser.add_argument("--capacity-ledger", type=Path, default=CAPACITY_LEDGER)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    capacity_ledger = args.capacity_ledger if args.capacity_ledger.is_absolute() else ROOT / args.capacity_ledger
    result = build_result(capacity_ledger)
    write_markdown(result)
    result["source_hashes"][
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-active-one-slot-epoch-source-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "active_epoch_count": result["aggregate"]["active_epoch_count"],
                "distinct_active_ell_count": result["aggregate"]["distinct_active_ell_count"],
                "active_ell_min": result["aggregate"]["active_ell_min"],
                "active_ell_max": result["aggregate"]["active_ell_max"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
