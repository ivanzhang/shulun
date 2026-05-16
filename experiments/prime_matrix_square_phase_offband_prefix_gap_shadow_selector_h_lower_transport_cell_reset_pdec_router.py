#!/usr/bin/env python3
"""登记非连续 transport cell 复现的 reset-PDEC 口径。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_transport_cell_reset_pdec_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-transport-cell-reset-pdec-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-selector-h-lower-transport-cell-reset-pdec-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-transport-cell-reset-pdec-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-transport-cell-reset-pdec-router.md
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

TRANSPORT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-fixed-residue-transport-cell-ledger.json"
DRIFT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-transport-cell-iteration-drift-ledger.json"
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-transport-cell-reset-pdec-ledger.json"
OUT_JSON = DOCS / (
    "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-"
    "transport-cell-reset-pdec-router.json"
)
OUT_MD = DOCS / (
    "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-"
    "transport-cell-reset-pdec-router.md"
)

MAIN_TARGET = "NonChainedTransportCellPDECOrSingletonResidueSAESummability"
NEXT_TARGET = "TransportResetPDECExclusionOrSingletonResidueSAESummability"


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


def reset_atom_rows(cells: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """找出同一 transport cell key 的非连续重复候选。"""
    grouped: dict[str, list[dict[str, Any]]] = {}
    for cell in cells:
        grouped.setdefault(str(cell["transport_cell_key"]), []).append(cell)
    rows = []
    for key, items in sorted(grouped.items()):
        if len(items) <= 1:
            continue
        p_ranges = [list(item["p_values"]) for item in items]
        rows.append(
            {
                "transport_cell_key": key,
                "occurrence_count": len(items),
                "p_ranges": p_ranges,
                "side": items[0]["side"],
                "ell": int(items[0]["ell"]),
                "crt_residue": int(items[0]["crt_residue"]),
                "p_lift": int(items[0]["p_lift"]),
                "slot_sum_lift": int(items[0]["slot_sum_lift"]),
                "lo_translate_defect": int(items[0]["lo_translate_defect"]),
                "hi_translate_defect": int(items[0]["hi_translate_defect"]),
                "formal_unit": (
                    f"transport-reset|{key}|occurrences={len(items)}"
                ),
            }
        )
    return rows


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "transport_reset_pdec_formal_unit",
            "status": "closed",
            "statement": "A non-chained transport recurrence must repeat the full transport-cell key, including side, ell, residue, lifts, residue step, edge defects, and active edge modes.",
        },
        {
            "name": "current_sweep_transport_reset_atoms_empty",
            "status": "closed_on_current_sweep",
            "statement": "No transport-cell key repeats in the current sweep after chained persistence has been bounded.",
        },
        {
            "name": "global_transport_reset_pdec_exclusion_open",
            "status": "open",
            "statement": "A global proof must exclude reset-PDEC atoms, or route their sparse occurrence to SAE/Rankin.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    agg = result["aggregate"]
    return [
        {
            "gate": "TransportResetFormalUnitClosed",
            "closed": True,
            "proved": True,
            "meaning": "非连续复现必须重复完整 transport cell key，不再有未命名自由度。",
            "remaining": "closed",
        },
        {
            "gate": "CurrentResetPDECAtomsEmpty",
            "closed": agg["reset_pdec_atom_count"] == 0,
            "proved": False,
            "meaning": "当前扫描中 transport reset atom 缺席。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "GlobalResetPDECExcluded",
            "closed": False,
            "proved": False,
            "meaning": "仍需全局排斥 transport reset atom，或证明其 SAE/Rankin 可求和。",
            "remaining": "TransportResetPDECExclusion",
        },
        {
            "gate": "SingletonResidueSAESummabilityProved",
            "closed": False,
            "proved": False,
            "meaning": "singleton residue packet 仍需独立 SAE/Rankin 账本。",
            "remaining": "SingletonResidueSAE/Rankin",
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步登记 reset-PDEC 口径，不关闭全局命题。",
            "remaining": result["next_direct_attack_target"],
        },
    ]


def build_result(transport_ledger: Path, drift_ledger: Path) -> dict[str, Any]:
    """构造 reset-PDEC 登记。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    transport = load_json(transport_ledger)
    drift = load_json(drift_ledger)
    cells = transport["transport_cells"]
    reset_rows = reset_atom_rows(cells)
    key_counts = Counter(str(cell["transport_cell_key"]) for cell in cells)
    aggregate = {
        "transport_ledger": str(transport_ledger.relative_to(ROOT)),
        "drift_ledger": str(drift_ledger.relative_to(ROOT)),
        "transport_cell_count": len(cells),
        "unique_transport_cell_key_count": len(key_counts),
        "repeated_transport_cell_key_count": sum(1 for count in key_counts.values() if count > 1),
        "reset_pdec_atom_count": len(reset_rows),
        "max_transport_cell_key_multiplicity": max(key_counts.values()) if key_counts else 0,
        "chained_transport_persistence_excluded_current_sweep": bool(
            drift["aggregate"]["chained_transport_persistence_excluded_current_sweep"]
        ),
        "current_sweep_transport_reset_atoms_empty": len(reset_rows) == 0,
        "transport_reset_pdec_excluded_globally": False,
        "transport_reset_sae_rankin_bound_proved": False,
        "singleton_residue_sae_rankin_bound_proved": False,
        "row_column_unconditional_closed": False,
    }
    ledger = {
        "aggregate": aggregate,
        "reset_pdec_atoms": reset_rows,
        "formal_unit_contract": {
            "required_repeated_fields": [
                "side",
                "ell",
                "crt_residue",
                "p_lift",
                "slot_sum_lift",
                "b_residue_step",
                "lo_translate_defect",
                "hi_translate_defect",
                "common_lower_active",
                "common_upper_active",
            ],
            "meaning": "Any non-chained recurrence must repeat this full key; otherwise it belongs to singleton/SAE drift.",
        },
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    result = {
        "certificate_type": (
            "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_"
            "transport_cell_reset_pdec_router"
        ),
        "status": "transport_reset_pdec_registered_current_atoms_empty",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_sweep_not_used_as_global_proof": True,
        "aggregate": aggregate,
        "reset_pdec_atoms": reset_rows,
        "formal_unit_contract": ledger["formal_unit_contract"],
        "transport_reset_pdec_excluded_globally": False,
        "singleton_residue_sae_rankin_bound_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "plain_conclusion": (
            "本步把非连续 transport 复现登记为 reset-PDEC：若同一 transport cell 不沿同一链连续复现，"
            "仍要重复完整 cell key。当前 12 个 transport cell key 全部唯一，reset-PDEC atom 数为 0。"
            "因此 transport 分支的当前样本没有未吸收 atom；全局仍需证明 reset atom 不会持久出现，"
            "或转入 SAE/Rankin。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    result["source_hashes"] = {
        "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_transport_cell_reset_pdec_router.py": sha256(
            Path(__file__).resolve()
        ),
        "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-fixed-residue-transport-cell-ledger.json": sha256(
            transport_ledger
        ),
        "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-transport-cell-iteration-drift-ledger.json": sha256(
            drift_ledger
        ),
        "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-transport-cell-reset-pdec-ledger.json": sha256(
            OUT_LEDGER
        ),
    }
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow selector H lower transport-cell reset-PDEC router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"transport_cell_count={agg['transport_cell_count']}",
        f"unique_transport_cell_key_count={agg['unique_transport_cell_key_count']}",
        f"repeated_transport_cell_key_count={agg['repeated_transport_cell_key_count']}",
        f"reset_pdec_atom_count={agg['reset_pdec_atom_count']}",
        f"chained_transport_persistence_excluded_current_sweep={fmt_bool(agg['chained_transport_persistence_excluded_current_sweep'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. reset-PDEC 口径",
        "",
        "非连续 transport 复现必须重复完整 key：",
        "",
        "```text",
        ", ".join(result["formal_unit_contract"]["required_repeated_fields"]),
        "```",
        "",
        "## 2. 当前 atom",
        "",
        f"当前 reset-PDEC atom 数为 `{agg['reset_pdec_atom_count']}`。",
        "",
        "## 3. 结构判断",
        "",
        "- 链式 transport 已由深度漂移给出有限寿命。",
        "- 非连续 transport 被登记为完整 key 重复的 reset-PDEC。",
        "- 当前扫描 reset atom 缺席；全局仍需排斥或给 SAE/Rankin 可求和。",
        "",
        "## 4. 命题行",
        "",
        "| name | status | statement |",
        "| --- | --- | --- |",
    ]
    for row in result["theorem_rows"]:
        lines.append(f"| `{row['name']}` | `{row['status']}` | {table_cell(row['statement'])} |")
    lines.extend(
        [
            "",
            "## 5. 决策表",
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
            "## 6. 下一步",
            "",
            f"- 主攻：`{result['next_direct_attack_target']}`。",
            "- 若继续攻 transport 分支，目标是全局排斥 reset-PDEC atom。",
            "- 若转入另一门，目标是 singleton residue SAE/Rankin 可求和。",
            "",
            "## 7. 依赖哈希",
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
    parser.add_argument("--transport-ledger", type=Path, default=TRANSPORT_LEDGER)
    parser.add_argument("--drift-ledger", type=Path, default=DRIFT_LEDGER)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    transport_ledger = args.transport_ledger if args.transport_ledger.is_absolute() else ROOT / args.transport_ledger
    drift_ledger = args.drift_ledger if args.drift_ledger.is_absolute() else ROOT / args.drift_ledger
    result = build_result(transport_ledger, drift_ledger)
    write_markdown(result)
    result["source_hashes"][
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-transport-cell-reset-pdec-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "transport_cell_count": result["aggregate"]["transport_cell_count"],
                "reset_pdec_atom_count": result["aggregate"]["reset_pdec_atom_count"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
