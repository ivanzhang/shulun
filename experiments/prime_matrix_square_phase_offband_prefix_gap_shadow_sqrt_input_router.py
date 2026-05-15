#!/usr/bin/env python3
"""把固定形状 gap shadow 压成 sqrt 级短区间/穿孔区间素数供给输入。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_sqrt_input_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-sqrt-input-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-sqrt-input-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-sqrt-input-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-sqrt-input-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

INPUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-ledger.json"
SHAPE_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-shape-ledger.json"
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-sqrt-input-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-sqrt-input-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-sqrt-input-router.md"

GAP_SHADOW_ROUTER = ROOT / "experiments" / "prime_matrix_square_phase_offband_prefix_gap_shadow_router.py"
SHAPE_ROUTER = ROOT / "experiments" / "prime_matrix_square_phase_offband_prefix_gap_shadow_shape_router.py"

MAIN_TARGET = "FixedPrefixGapShadowShapePDECOrMovingDepthSAEExclusion"
NEXT_TARGET = "FixedShapeUnionPrimeSupplyOrSqrtScaleGapInput"


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
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def atom_shape_from_key(key: str) -> str:
    """从 atom 键提取 band/k 形状。"""
    band, rest = key.split(":k", 1)
    k_text = rest.split(":", 1)[0]
    return f"{band}:k{k_text}"


def shape_key_for_template(row: dict[str, Any], template: dict[str, Any]) -> str:
    """复用形状键定义。"""
    atom_shapes = [atom_shape_from_key(key) for key in template["void_atom_keys"]]
    return "|".join(
        [
            f"side={row['side']}",
            f"W={row['required_offband_witness_count']}",
            f"N={row['actual_prefix_atom_count']}",
            f"V={row['forced_void_atoms_under_failure']}",
            ",".join(atom_shapes),
        ]
    )


def odd_candidate_count(q_lo: int, q_hi: int) -> int:
    """计算同奇偶 q 候选数。"""
    if q_hi < q_lo:
        return 0
    return (q_hi - q_lo) // 2 + 1


def template_record(row: dict[str, Any], template: dict[str, Any]) -> dict[str, Any]:
    """把一个 void 模板改写成素数供给输入记录。"""
    atom_by_key = {atom["key"]: atom for atom in row["prefix_interval_atoms"]}
    atoms = [atom_by_key[key] for key in template["void_atom_keys"]]
    q_lo = min(int(atom["q_lo"]) for atom in atoms)
    q_hi = max(int(atom["q_hi"]) for atom in atoms)
    p_value = int(row["p"])
    hull_candidates = odd_candidate_count(q_lo, q_hi)
    union_candidates = sum(int(atom["candidate_count"]) for atom in atoms)
    coverage_defect = hull_candidates - union_candidates
    actual_prime_load = sum(int(atom["prime_load"]) for atom in atoms)
    input_type = "BackwardSqrtPrimeGap" if coverage_defect == 0 else "PuncturedShapeUnionPrimeSupply"
    depth = p_value - q_lo
    return {
        "p": p_value,
        "side": row["side"],
        "shape_key": shape_key_for_template(row, template),
        "required_offband_witness_count": row["required_offband_witness_count"],
        "actual_prefix_atom_count": row["actual_prefix_atom_count"],
        "forced_void_atoms": row["forced_void_atoms_under_failure"],
        "void_atom_keys": template["void_atom_keys"],
        "q_hull_lo": q_lo,
        "q_hull_hi": q_hi,
        "q_hull_span": q_hi - q_lo + 1,
        "depth_from_p": depth,
        "depth_over_sqrt_p": depth / math.sqrt(p_value),
        "hull_candidate_count": hull_candidates,
        "union_candidate_count": union_candidates,
        "coverage_defect_candidate_count": coverage_defect,
        "actual_template_prime_load": actual_prime_load,
        "actual_template_void": actual_prime_load == 0,
        "input_type": input_type,
        "prime_supply_input_statement": (
            f"The union of fixed prefix atom intervals {template['void_atom_keys']} contains a prime q."
        ),
    }


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "template_void_exclusion_by_union_prime_supply",
            "status": "closed",
            "statement": "A forced void template is excluded once its union of fixed q=P-2b atom intervals contains at least one prime q.",
        },
        {
            "name": "contiguous_template_to_backward_sqrt_gap",
            "status": "closed",
            "statement": "If the template covers every odd q in its hull, its exclusion is a backward prime-gap bound below P with length equal to the hull depth.",
        },
        {
            "name": "punctured_template_to_shape_union_supply",
            "status": "closed",
            "statement": "If the template does not cover the whole hull, its exclusion is a punctured fixed-shape union prime-supply input.",
        },
        {
            "name": "finite_no_template_void",
            "status": "finite_evidence",
            "statement": "The finite audit finds that every listed template union actually contains at least one prime.",
        },
        {
            "name": "global_fixed_shape_union_supply",
            "status": "open",
            "statement": "A global proof still needs the fixed-shape union prime-supply theorem, or an external sqrt-scale prime-gap input strong enough to imply it.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "TemplateVoidExclusionByUnionPrimeSupplyClosed",
            "closed": True,
            "proved": True,
            "meaning": "每个强制空模板只要自身并集含素数即可排除。",
            "remaining": "closed",
        },
        {
            "gate": "SqrtGapInputBoundaryClosed",
            "closed": True,
            "proved": True,
            "meaning": "连续 hull 模板已等价为 P 下方 sqrt 级后向素数间隙输入。",
            "remaining": "closed",
        },
        {
            "gate": "FiniteNoTemplateVoid",
            "closed": result["actual_template_void_count"] == 0,
            "proved": False,
            "meaning": "有限样本中所有模板并集都含素数。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "GlobalFixedShapeUnionSupplyClosed",
            "closed": False,
            "proved": False,
            "meaning": "仍需全局证明固定形状并集素数供给，或引用同等强度短区间素数输入。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只标定最终输入边界，不关闭全局行/列命题。",
            "remaining": NEXT_TARGET,
        },
    ]


def build_result(input_ledger: Path, shape_ledger: Path) -> dict[str, Any]:
    """构造路由器结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    source = load_json(input_ledger)
    shape_source = load_json(shape_ledger)
    template_records: list[dict[str, Any]] = []
    for row in source["positive_required_template_frontier"]:
        for template in row["void_subset_templates"]:
            template_records.append(template_record(row, template))
    type_counter = Counter(row["input_type"] for row in template_records)
    shape_counter = Counter(row["shape_key"] for row in template_records)
    by_shape: dict[str, dict[str, Any]] = {}
    examples: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in template_records:
        key = row["shape_key"]
        if len(examples[key]) < 5:
            examples[key].append(row)
        item = by_shape.setdefault(
            key,
            {
                "shape_key": key,
                "count": 0,
                "input_types": Counter(),
                "min_p": row["p"],
                "max_p": row["p"],
                "max_depth_over_sqrt_p": row["depth_over_sqrt_p"],
                "max_depth_from_p": row["depth_from_p"],
                "max_coverage_defect": row["coverage_defect_candidate_count"],
                "min_actual_template_prime_load": row["actual_template_prime_load"],
                "examples": examples[key],
            },
        )
        item["count"] += 1
        item["input_types"][row["input_type"]] += 1
        item["min_p"] = min(item["min_p"], row["p"])
        item["max_p"] = max(item["max_p"], row["p"])
        item["max_depth_over_sqrt_p"] = max(item["max_depth_over_sqrt_p"], row["depth_over_sqrt_p"])
        item["max_depth_from_p"] = max(item["max_depth_from_p"], row["depth_from_p"])
        item["max_coverage_defect"] = max(item["max_coverage_defect"], row["coverage_defect_candidate_count"])
        item["min_actual_template_prime_load"] = min(item["min_actual_template_prime_load"], row["actual_template_prime_load"])
    shape_summaries = []
    for item in by_shape.values():
        item["input_types"] = dict(item["input_types"])
        shape_summaries.append(item)
    shape_summaries.sort(key=lambda item: (-item["count"], -item["max_depth_over_sqrt_p"], item["shape_key"]))
    aggregate = {
        "input_ledger": str(input_ledger.relative_to(ROOT)),
        "shape_ledger": str(shape_ledger.relative_to(ROOT)),
        "template_count": len(template_records),
        "shape_count": len(shape_counter),
        "input_type_counts": dict(type_counter),
        "actual_template_void_count": sum(1 for row in template_records if row["actual_template_void"]),
        "max_depth_from_p": max((row["depth_from_p"] for row in template_records), default=0),
        "max_depth_over_sqrt_p": max((row["depth_over_sqrt_p"] for row in template_records), default=0),
        "max_coverage_defect_candidate_count": max(
            (row["coverage_defect_candidate_count"] for row in template_records),
            default=0,
        ),
        "source_shape_count": shape_source["aggregate"]["shape_count"],
    }
    ledger = {
        "parameters": source["parameters"],
        "aggregate": aggregate,
        "template_records": template_records,
        "shape_summaries": shape_summaries,
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = {
        "certificate_type": "prime_matrix_square_phase_offband_prefix_gap_shadow_sqrt_input_router",
        "status": "fixed_shape_gap_shadow_reduced_to_union_prime_supply_or_sqrt_gap_input_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "empirical_absence_not_used_as_proof": True,
        "parameters": source["parameters"],
        "aggregate": aggregate,
        "actual_template_void_count": aggregate["actual_template_void_count"],
        "template_frontier": sorted(
            template_records,
            key=lambda row: (-row["depth_over_sqrt_p"], row["actual_template_prime_load"], row["p"]),
        )[:40],
        "shape_summaries": shape_summaries[:40],
        "union_prime_supply_gate_closed": True,
        "sqrt_gap_boundary_identified": True,
        "global_fixed_shape_union_supply_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_sqrt_input_router.py": sha256(
                Path(__file__).resolve()
            ),
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_router.py": sha256(GAP_SHADOW_ROUTER),
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_shape_router.py": sha256(SHAPE_ROUTER),
            "data/square-phase-offband-prefix-gap-shadow-ledger.json": sha256(input_ledger),
            "data/square-phase-offband-prefix-gap-shadow-shape-ledger.json": sha256(shape_ledger),
            "data/square-phase-offband-prefix-gap-shadow-sqrt-input-ledger.json": sha256(OUT_LEDGER),
        },
        "plain_conclusion": (
            "本步把固定小 k 形状 PDEC 的最后数学输入边界写清："
            "每个强制 prime-void 模板，只要其固定 q 区间并集含一个素数就被排除。"
            "若模板覆盖整个奇 q hull，则这正是 P 下方长度 depth 的后向素数间隙输入；"
            "若存在覆盖缺口，则是更精细的穿孔固定形状并集素数供给输入。"
            "有限账本中所有模板并集实际都含素数，但全局仍未证明。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow sqrt-input router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"template_count={agg['template_count']}",
        f"shape_count={agg['shape_count']}",
        f"actual_template_void_count={agg['actual_template_void_count']}",
        f"max_depth_from_p={agg['max_depth_from_p']}",
        f"max_depth_over_sqrt_p={agg['max_depth_over_sqrt_p']:.6f}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 输入边界",
        "",
        "每个 failure 模板是一组固定前缀 atom 区间。若这些区间并集中存在一个素数 `q`，则该模板不可能全空，gap shadow 被排除。",
        "",
        "若这些 atom 覆盖其 hull 内全部奇 `q`，则所需输入就是",
        "",
        "```text",
        "there is a prime in [P-depth, P) with the correct odd parity",
        "```",
        "",
        "也就是 `P` 下方 sqrt 尺度的后向素数间隙界。否则，它是穿孔形状并集的素数供给问题。",
        "",
        "## 2. 有限审计摘要",
        "",
        "| metric | value |",
        "| --- | ---: |",
        f"| template records | {agg['template_count']} |",
        f"| shape count | {agg['shape_count']} |",
        f"| input types | `{agg['input_type_counts']}` |",
        f"| actual template void count | {agg['actual_template_void_count']} |",
        f"| max depth from P | {agg['max_depth_from_p']} |",
        f"| max depth/sqrt(P) | {agg['max_depth_over_sqrt_p']:.6f} |",
        f"| max coverage defect candidates | {agg['max_coverage_defect_candidate_count']} |",
        "",
        "## 3. 最深模板边界",
        "",
        "| P | side | type | load | q hull | depth | depth/sqrt(P) | coverage defect | atoms |",
        "| ---: | --- | --- | ---: | --- | ---: | ---: | ---: | --- |",
    ]
    for row in result["template_frontier"][:24]:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["p"]),
                    f"`{row['side']}`",
                    f"`{row['input_type']}`",
                    str(row["actual_template_prime_load"]),
                    f"`{row['q_hull_lo']}-{row['q_hull_hi']}`",
                    str(row["depth_from_p"]),
                    f"{row['depth_over_sqrt_p']:.6f}",
                    str(row["coverage_defect_candidate_count"]),
                    f"`{','.join(row['void_atom_keys'])}`",
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 4. 形状输入摘要",
            "",
            "| count | shape | input types | P range | max depth/sqrt(P) | min load | max defect |",
            "| ---: | --- | --- | --- | ---: | ---: | ---: |",
        ]
    )
    for item in result["shape_summaries"][:24]:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(item["count"]),
                    f"`{item['shape_key']}`",
                    f"`{item['input_types']}`",
                    f"{item['min_p']}..{item['max_p']}",
                    f"{item['max_depth_over_sqrt_p']:.6f}",
                    str(item["min_actual_template_prime_load"]),
                    str(item["max_coverage_defect"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 5. 命题行",
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
            "## 6. 决策表",
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
            "## 7. 下一步",
            "",
            "- 主攻：`FixedShapeUnionPrimeSupplyOrSqrtScaleGapInput`。",
            "- 自足路线必须证明这些固定/穿孔 q 区间并集含素数。",
            "- 外部路线需要 sqrt 尺度后向短区间素数输入；现有有限审计不能替代该全局输入。",
            "- 当前仍未证明全局行/列无条件闭合。",
            "",
            "## 8. 依赖哈希",
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
    parser.add_argument("--shape-ledger", type=Path, default=SHAPE_LEDGER)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    input_ledger = args.input_ledger if args.input_ledger.is_absolute() else ROOT / args.input_ledger
    shape_ledger = args.shape_ledger if args.shape_ledger.is_absolute() else ROOT / args.shape_ledger
    result = build_result(input_ledger, shape_ledger)
    write_markdown(result)
    result["source_hashes"][
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-sqrt-input-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "template_count": result["aggregate"]["template_count"],
                "actual_template_void_count": result["actual_template_void_count"],
                "max_depth_over_sqrt_p": result["aggregate"]["max_depth_over_sqrt_p"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
