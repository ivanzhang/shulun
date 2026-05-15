#!/usr/bin/env python3
"""审计 small-modulus residue 模板是否可由 phase+primality 自动排除。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_template_provenance_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-template-provenance-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-selector-template-provenance-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-template-provenance-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-template-provenance-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

CANDIDATE_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-small-modulus-candidate-ledger.json"
TEMPLATE_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-small-modulus-template-ledger.json"
PHASE_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-phase-compatibility-ledger.json"
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-template-provenance-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-template-provenance-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-template-provenance-router.md"

TEMPLATE_ROUTER = (
    ROOT
    / "experiments"
    / "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_small_modulus_template_router.py"
)

MAIN_TARGET = "SmallModulusLowwheelResidueTemplateGlobalizationOrOverlapPDEC"
NEXT_TARGET = "ActualFormalUnitResidueSelectorProvenanceOrTemplateOverlapPDEC"


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


def is_prime(value: int) -> bool:
    """朴素素性检查。"""
    if value < 2:
        return False
    if value == 2:
        return True
    if value % 2 == 0:
        return False
    for divisor in range(3, math.isqrt(value) + 1, 2):
        if value % divisor == 0:
            return False
    return True


def matching_primes(lo_value: int, hi_value: int, modulus: int, residue: int) -> list[int]:
    """列出窗口中与模板 residue 匹配的素数代表。"""
    return [
        value
        for value in range(lo_value, hi_value + 1)
        if value % modulus == residue and is_prime(value)
    ]


def candidate_items(candidate_source: dict[str, Any], phase_source: dict[str, Any]) -> list[dict[str, Any]]:
    """抽取候选并补充 phase 窗口信息。"""
    phase_by_index = {int(row["index"]): row for row in phase_source["phase_compatibility_records"]}
    items: list[dict[str, Any]] = []
    for row in candidate_source["small_modulus_candidate_records"]:
        phase = phase_by_index[int(row["index"])]
        for item in row["small_modulus_candidates"]:
            primes = matching_primes(
                int(phase["phase_p_lo"]),
                int(phase["phase_p_hi"]),
                int(item["gcd_modulus_15"]),
                int(item["residue_mod_gcd15"]),
            )
            items.append(
                {
                    "index": row["index"],
                    "p": row["p"],
                    "side": row["side"],
                    "shape_key": row["shape_key"],
                    "parent_atom_key": row["parent_atom_key"],
                    "parent_atom_band": row["parent_atom_band"],
                    "parent_atom_k": row["parent_atom_k"],
                    "cell_length": row["cell_length"],
                    "phase_p_lo": phase["phase_p_lo"],
                    "phase_p_hi": phase["phase_p_hi"],
                    "phase_p_width": phase["phase_p_width"],
                    "labels": item["labels"],
                    "distinct_labels": item["distinct_labels"],
                    "modulus": item["modulus"],
                    "gcd_modulus_15": item["gcd_modulus_15"],
                    "cover_word_residue_mod_gcd15": item["residue_mod_gcd15"],
                    "actual_p_mod_gcd15": item["actual_p_mod_gcd15"],
                    "structural_conflict_for_actual_p": item["structural_lowwheel_conflict"],
                    "matching_prime_representatives": primes,
                    "matching_prime_count": len(primes),
                    "phase_primality_alone_excludes_template": len(primes) == 0,
                    "selector_provenance_required": len(primes) > 0,
                }
            )
    return items


def template_records(items: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """按 residue 模板汇总 selector provenance 边界。"""
    grouped: dict[str, list[dict[str, Any]]] = {}
    for item in items:
        key = (
            f"band={item['parent_atom_band']}|k={item['parent_atom_k']}|L={item['cell_length']}|"
            f"labels={','.join(map(str, item['distinct_labels']))}|g={item['gcd_modulus_15']}|"
            f"rho={item['cover_word_residue_mod_gcd15']}|actual={item['actual_p_mod_gcd15']}"
        )
        grouped.setdefault(key, []).append(item)
    records: list[dict[str, Any]] = []
    for key, values in sorted(grouped.items()):
        all_primes = sorted({prime for item in values for prime in item["matching_prime_representatives"]})
        records.append(
            {
                "template_key": key,
                "instance_count": len(values),
                "p_values": sorted({int(item["p"]) for item in values}),
                "gcd_modulus_15": values[0]["gcd_modulus_15"],
                "cover_word_residue_mod_gcd15": values[0]["cover_word_residue_mod_gcd15"],
                "actual_p_mod_gcd15": values[0]["actual_p_mod_gcd15"],
                "matching_prime_representatives": all_primes,
                "matching_prime_count": len(all_primes),
                "phase_primality_alone_excludes_template": len(all_primes) == 0,
                "selector_provenance_required": len(all_primes) > 0,
                "pdec_needed_for_residue_matching_template": False,
            }
        )
    return records


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "phase_primality_globalization_rejected",
            "status": "closed",
            "statement": "The small-modulus template conflict cannot be globalized using only the phase window and primality, because matching prime representatives exist.",
        },
        {
            "name": "actual_selector_provenance_required",
            "status": "open",
            "statement": "A global proof must use the actual formal-unit selector to force actual P into the nonmatching residue class.",
        },
        {
            "name": "template_overlap_pdec",
            "status": "open",
            "statement": "If the selector can land in the template residue, the matching template must be routed to PDEC/ColumnCRT.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    agg = result["aggregate"]
    return [
        {
            "gate": "PhasePrimalityAloneExcludesTemplates",
            "closed": agg["template_with_matching_prime_count"] == 0,
            "proved": False,
            "meaning": "模板 residue 在当前 phase 窗口中有素数代表，不能靠 phase+素性排除。",
            "remaining": "rejected",
        },
        {
            "gate": "ActualSelectorProvenanceNeeded",
            "closed": agg["template_with_matching_prime_count"] > 0,
            "proved": True,
            "meaning": "必须证明 actual formal-unit selector 为什么避开这些 residue。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "GlobalActualSelectorResidueProved",
            "closed": False,
            "proved": False,
            "meaning": "尚未证明 formal-unit selector 的 residue 来源定理。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "TemplateOverlapPDECExcluded",
            "closed": False,
            "proved": False,
            "meaning": "若 selector 可命中模板 residue，仍需 PDEC/ColumnCRT 排斥。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只关闭错误的 phase-primality 全球化路线，不关闭全局行/列命题。",
            "remaining": NEXT_TARGET,
        },
    ]


def build_result(candidate_ledger: Path, template_ledger: Path, phase_ledger: Path) -> dict[str, Any]:
    """构造 selector provenance 边界结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    candidate_source = load_json(candidate_ledger)
    template_source = load_json(template_ledger)
    phase_source = load_json(phase_ledger)
    items = candidate_items(candidate_source, phase_source)
    templates = template_records(items)
    aggregate = {
        "candidate_ledger": str(candidate_ledger.relative_to(ROOT)),
        "template_ledger": str(template_ledger.relative_to(ROOT)),
        "phase_ledger": str(phase_ledger.relative_to(ROOT)),
        "candidate_count": len(items),
        "template_count": len(templates),
        "template_with_matching_prime_count": sum(
            1 for item in templates if item["matching_prime_count"] > 0
        ),
        "total_matching_prime_representative_count": sum(item["matching_prime_count"] for item in templates),
        "phase_primality_alone_excludes_all_templates": all(
            item["phase_primality_alone_excludes_template"] for item in templates
        ),
        "actual_selector_provenance_proved": False,
        "template_overlap_pdec_excluded": False,
        "row_column_unconditional_closed": False,
    }
    ledger = {
        "parameters": candidate_source["parameters"],
        "aggregate": aggregate,
        "candidate_provenance_records": items,
        "template_provenance_records": templates,
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = {
        "certificate_type": "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_template_provenance_router",
        "status": "selector_template_provenance_required_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "phase_primality_route_rejected": True,
        "parameters": candidate_source["parameters"],
        "aggregate": aggregate,
        "candidate_provenance_records": items,
        "template_provenance_records": templates,
        "small_modulus_template_aggregate": template_source["aggregate"],
        "actual_selector_provenance_proved": False,
        "template_overlap_pdec_excluded": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_template_provenance_router.py": sha256(
                Path(__file__).resolve()
            ),
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_small_modulus_template_router.py": sha256(
                TEMPLATE_ROUTER
            ),
            "data/square-phase-offband-prefix-gap-shadow-selector-small-modulus-candidate-ledger.json": sha256(
                candidate_ledger
            ),
            "data/square-phase-offband-prefix-gap-shadow-selector-small-modulus-template-ledger.json": sha256(
                template_ledger
            ),
            "data/square-phase-offband-prefix-gap-shadow-phase-compatibility-ledger.json": sha256(
                phase_ledger
            ),
            "data/square-phase-offband-prefix-gap-shadow-selector-template-provenance-ledger.json": sha256(
                OUT_LEDGER
            ),
        },
        "plain_conclusion": (
            "本步审计 small-modulus 模板冲突能否由 phase+素性自动全球化。结果是否定的："
            f"{aggregate['template_with_matching_prime_count']} 个模板的 residue 在当前 phase 窗口中都有素数代表，"
            f"匹配素数代表总数为 {aggregate['total_matching_prime_representative_count']}。"
            "因此当前 actual P 避开模板 residue 是 formal-unit selector 来源问题，而不是局部 phase/primality 问题；"
            "下一步必须证明 actual selector 的 residue 来源，或对 matching template 提交 PDEC/ColumnCRT。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow selector template provenance router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"candidate_count={agg['candidate_count']}",
        f"template_count={agg['template_count']}",
        f"template_with_matching_prime_count={agg['template_with_matching_prime_count']}",
        f"total_matching_prime_representative_count={agg['total_matching_prime_representative_count']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. Template Provenance",
        "",
        "| template | rho | actual | matching primes | selector provenance required |",
        "| --- | ---: | ---: | --- | ---: |",
    ]
    for row in result["template_provenance_records"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(row['template_key'])}`",
                    str(row["cover_word_residue_mod_gcd15"]),
                    str(row["actual_p_mod_gcd15"]),
                    f"`{row['matching_prime_representatives']}`",
                    f"`{fmt_bool(row['selector_provenance_required'])}`",
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
            "- 直接证明目标：解释 actual formal-unit selector 的 residue 来源，证明它不能落入模板 rho。",
            "- 若 selector 可落入 rho，则登记 matching template overlap `PDEC/ColumnCRT`。",
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
    parser.add_argument("--candidate-ledger", type=Path, default=CANDIDATE_LEDGER)
    parser.add_argument("--template-ledger", type=Path, default=TEMPLATE_LEDGER)
    parser.add_argument("--phase-ledger", type=Path, default=PHASE_LEDGER)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    candidate_ledger = args.candidate_ledger if args.candidate_ledger.is_absolute() else ROOT / args.candidate_ledger
    template_ledger = args.template_ledger if args.template_ledger.is_absolute() else ROOT / args.template_ledger
    phase_ledger = args.phase_ledger if args.phase_ledger.is_absolute() else ROOT / args.phase_ledger
    result = build_result(candidate_ledger, template_ledger, phase_ledger)
    write_markdown(result)
    result["source_hashes"][
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-template-provenance-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "template_with_matching_prime_count": result["aggregate"][
                    "template_with_matching_prime_count"
                ],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
