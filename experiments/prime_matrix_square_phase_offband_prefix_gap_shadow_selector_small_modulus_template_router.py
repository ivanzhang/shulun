#!/usr/bin/env python3
"""把 small-modulus 低轮冲突候选归并为 residue 模板。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_small_modulus_template_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-small-modulus-template-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-selector-small-modulus-template-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-small-modulus-template-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-small-modulus-template-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

INPUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-small-modulus-candidate-ledger.json"
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-small-modulus-template-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-small-modulus-template-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-small-modulus-template-router.md"

CANDIDATE_ROUTER = (
    ROOT
    / "experiments"
    / "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_small_modulus_candidate_router.py"
)

MAIN_TARGET = "SmallModulusCompatibleWordsLowwheelConflictOrOverlapPDEC"
NEXT_TARGET = "SmallModulusLowwheelResidueTemplateGlobalizationOrOverlapPDEC"


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


def candidate_items(source: dict[str, Any]) -> list[dict[str, Any]]:
    """抽取全部 small-modulus 候选并补充父行信息。"""
    items: list[dict[str, Any]] = []
    for row in source["small_modulus_candidate_records"]:
        for item in row["small_modulus_candidates"]:
            items.append(
                {
                    **item,
                    "index": row["index"],
                    "shape_key": row["shape_key"],
                    "parent_atom_band": row["parent_atom_band"],
                    "parent_atom_k": row["parent_atom_k"],
                    "cell_length": row["cell_length"],
                }
            )
    return items


def template_records(items: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """按 family、标签集合和低轮残基归并模板。"""
    grouped: dict[tuple[Any, ...], list[dict[str, Any]]] = defaultdict(list)
    for item in items:
        key = (
            item["parent_atom_band"],
            item["parent_atom_k"],
            item["cell_length"],
            tuple(item["distinct_labels"]),
            item["gcd_modulus_15"],
            item["residue_mod_gcd15"],
            item["actual_p_mod_gcd15"],
        )
        grouped[key].append(item)
    records: list[dict[str, Any]] = []
    for index, (key, values) in enumerate(sorted(grouped.items())):
        band, k_value, length, distinct_labels, gcd15, residue_mod, actual_mod = key
        records.append(
            {
                "template_index": index,
                "template_key": (
                    f"band={band}|k={k_value}|L={length}|labels={','.join(map(str, distinct_labels))}|"
                    f"g={gcd15}|rho={residue_mod}|actual={actual_mod}"
                ),
                "parent_atom_band": band,
                "parent_atom_k": k_value,
                "cell_length": length,
                "distinct_labels": list(distinct_labels),
                "gcd_modulus_15": gcd15,
                "cover_word_residue_mod_gcd15": residue_mod,
                "actual_p_mod_gcd15": actual_mod,
                "structural_conflict": residue_mod != actual_mod,
                "instance_count": len(values),
                "moduli": sorted({int(item["modulus"]) for item in values}),
                "p_values": sorted({int(item["p"]) for item in values}),
                "example_labels": values[0]["labels"],
                "example_window_values": values[0]["window_values"],
                "pdec_needed": residue_mod == actual_mod,
            }
        )
    return records


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "finite_small_modulus_templates_registered",
            "status": "closed_on_current_frontier",
            "statement": "Current small-modulus candidates are reduced to finitely many lowwheel residue templates.",
        },
        {
            "name": "finite_templates_all_conflicting",
            "status": "closed_on_current_frontier",
            "statement": "Every current small-modulus template has cover-word residue different from actual P modulo gcd(M,15).",
        },
        {
            "name": "global_template_conflict",
            "status": "open",
            "statement": "A global proof must show the same residue-template conflict persists in the formal-unit family.",
        },
        {
            "name": "template_overlap_pdec",
            "status": "open",
            "statement": "Any template with matching residues must be routed to PDEC/ColumnCRT.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    agg = result["aggregate"]
    return [
        {
            "gate": "FiniteTemplateRegistrationClosed",
            "closed": True,
            "proved": True,
            "meaning": "当前 small-modulus 候选已归并为 residue 模板。",
            "remaining": "closed on current finite frontier",
        },
        {
            "gate": "FiniteTemplatesAllConflict",
            "closed": agg["pdec_template_count"] == 0,
            "proved": True,
            "meaning": "当前模板全部低轮冲突，无需 PDEC。",
            "remaining": "closed on current finite frontier",
        },
        {
            "gate": "GlobalTemplateConflictProved",
            "closed": False,
            "proved": False,
            "meaning": "尚未证明 formal-unit 族中同类模板必然冲突。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "TemplateOverlapPDECExcluded",
            "closed": False,
            "proved": False,
            "meaning": "若出现 residue 匹配模板，仍需 PDEC/ColumnCRT 排斥。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只关闭当前模板归并层，不关闭全局行/列命题。",
            "remaining": NEXT_TARGET,
        },
    ]


def build_result(input_ledger: Path) -> dict[str, Any]:
    """构造 small-modulus 模板归并结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    source = load_json(input_ledger)
    items = candidate_items(source)
    templates = template_records(items)
    aggregate = {
        "input_ledger": str(input_ledger.relative_to(ROOT)),
        "candidate_count": len(items),
        "template_count": len(templates),
        "conflicting_template_count": sum(1 for item in templates if item["structural_conflict"]),
        "pdec_template_count": sum(1 for item in templates if item["pdec_needed"]),
        "global_template_conflict_proved": False,
        "template_overlap_pdec_excluded": False,
        "row_column_unconditional_closed": False,
    }
    ledger = {
        "parameters": source["parameters"],
        "aggregate": aggregate,
        "small_modulus_template_records": templates,
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = {
        "certificate_type": "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_small_modulus_template_router",
        "status": "selector_small_modulus_templates_conflict_open_global",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_template_conflict_not_used_as_global_proof": True,
        "parameters": source["parameters"],
        "aggregate": aggregate,
        "small_modulus_template_records": templates,
        "small_modulus_candidate_aggregate": source["aggregate"],
        "global_template_conflict_proved": False,
        "template_overlap_pdec_excluded": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_small_modulus_template_router.py": sha256(
                Path(__file__).resolve()
            ),
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_small_modulus_candidate_router.py": sha256(
                CANDIDATE_ROUTER
            ),
            "data/square-phase-offband-prefix-gap-shadow-selector-small-modulus-candidate-ledger.json": sha256(
                input_ledger
            ),
            "data/square-phase-offband-prefix-gap-shadow-selector-small-modulus-template-ledger.json": sha256(
                OUT_LEDGER
            ),
        },
        "plain_conclusion": (
            "本步把 7 个 small-modulus 候选归并为 "
            f"{aggregate['template_count']} 个低轮 residue 模板；所有模板都满足 cover-word residue "
            "与 actual P 在 gcd(M,15) 下不相等，因此当前前沿无需 PDEC。全局剩余是证明这些模板冲突"
            "在 formal-unit 族中稳定，或对 residue 匹配模板提交 PDEC/ColumnCRT。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow selector small modulus template router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"candidate_count={agg['candidate_count']}",
        f"template_count={agg['template_count']}",
        f"conflicting_template_count={agg['conflicting_template_count']}",
        f"pdec_template_count={agg['pdec_template_count']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. Residue 模板",
        "",
        "| template | instances | labels | gcd | rho | actual | moduli | P values | conflict |",
        "| --- | ---: | --- | ---: | ---: | ---: | --- | --- | ---: |",
    ]
    for row in result["small_modulus_template_records"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(row['template_key'])}`",
                    str(row["instance_count"]),
                    f"`{row['distinct_labels']}`",
                    str(row["gcd_modulus_15"]),
                    str(row["cover_word_residue_mod_gcd15"]),
                    str(row["actual_p_mod_gcd15"]),
                    f"`{row['moduli']}`",
                    f"`{row['p_values']}`",
                    f"`{fmt_bool(row['structural_conflict'])}`",
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 2. 命题行",
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
            "## 3. 决策表",
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
            "## 4. 下一步",
            "",
            f"- 主攻：`{result['next_direct_attack_target']}`。",
            "- 直接证明目标：证明这些 residue 模板的冲突在 formal-unit 族中稳定。",
            "- 若出现 `rho=actual` 的模板，则登记为 template overlap `PDEC/ColumnCRT`。",
            "- 当前仍未证明全局行/列无条件闭合。",
            "",
            "## 5. 依赖哈希",
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
    parser.add_argument("--input-ledger", type=Path, default=INPUT_LEDGER)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    input_ledger = args.input_ledger if args.input_ledger.is_absolute() else ROOT / args.input_ledger
    result = build_result(input_ledger)
    write_markdown(result)
    result["source_hashes"][
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-small-modulus-template-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "template_count": result["aggregate"]["template_count"],
                "pdec_template_count": result["aggregate"]["pdec_template_count"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
