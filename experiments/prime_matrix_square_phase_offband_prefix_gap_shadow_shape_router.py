#!/usr/bin/env python3
"""把多 atom prime-void gap shadow 压成形状键 PDEC/移动深度 SAE 分流。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_shape_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-shape-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-shape-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-shape-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-shape-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

INPUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-ledger.json"
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-shape-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-shape-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-shape-router.md"

GAP_SHADOW_ROUTER = ROOT / "experiments" / "prime_matrix_square_phase_offband_prefix_gap_shadow_router.py"

MAIN_TARGET = "FirstPrefixMultiAtomPrimeVoidGapShadowPDECExclusion"
NEXT_TARGET = "FixedPrefixGapShadowShapePDECOrMovingDepthSAEExclusion"


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


def parse_atom_key(key: str) -> dict[str, Any]:
    """解析 band:k:qlo-qhi 形式的 atom 键。"""
    band, rest = key.split(":k", 1)
    k_text, q_text = rest.split(":", 1)
    q_lo_text, q_hi_text = q_text.split("-", 1)
    return {
        "band": band,
        "k": int(k_text),
        "q_lo": int(q_lo_text),
        "q_hi": int(q_hi_text),
    }


def atom_shape(key: str) -> str:
    """返回只保留 band 与 k 的形状原子。"""
    parsed = parse_atom_key(key)
    return f"{parsed['band']}:k{parsed['k']}"


def template_shape(row: dict[str, Any], template: dict[str, Any]) -> dict[str, Any]:
    """生成单个 void 模板的形状键。"""
    atom_shapes = [atom_shape(key) for key in template["void_atom_keys"]]
    parsed_atoms = [parse_atom_key(key) for key in template["void_atom_keys"]]
    k_values = [atom["k"] for atom in parsed_atoms]
    q_lo = min(atom["q_lo"] for atom in parsed_atoms)
    q_hi = max(atom["q_hi"] for atom in parsed_atoms)
    shape_key = "|".join(
        [
            f"side={row['side']}",
            f"W={row['required_offband_witness_count']}",
            f"N={row['actual_prefix_atom_count']}",
            f"V={row['forced_void_atoms_under_failure']}",
            ",".join(atom_shapes),
        ]
    )
    return {
        "shape_key": shape_key,
        "side": row["side"],
        "p": row["p"],
        "required_offband_witness_count": row["required_offband_witness_count"],
        "actual_prefix_atom_count": row["actual_prefix_atom_count"],
        "forced_void_atoms": row["forced_void_atoms_under_failure"],
        "atom_shapes": atom_shapes,
        "void_atom_keys": template["void_atom_keys"],
        "combined_candidate_count": template["combined_candidate_count"],
        "max_single_atom_candidate_count": template["max_single_atom_candidate_count"],
        "q_hull_lo": q_lo,
        "q_hull_hi": q_hi,
        "q_hull_span": q_hi - q_lo + 1,
        "max_k": max(k_values, default=0),
        "shape_route": "FixedSmallK-PDEC/ColumnCRT" if max(k_values, default=0) <= 2 else "MovingDepth-SAE",
    }


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "gap_shadow_template_shape_key",
            "status": "closed",
            "statement": "Every multi-void prefix failure template has a canonical shape key built from side, W, N, V and ordered band/k atoms.",
        },
        {
            "name": "fixed_shape_or_moving_depth_route",
            "status": "closed",
            "statement": "A persistent shadow must enter either a fixed small-k PDEC/ColumnCRT family or a moving-depth SAE family.",
        },
        {
            "name": "finite_shape_ledger",
            "status": "finite_evidence",
            "statement": "The finite ledger lists the observed hypothetical shadow shapes and their examples.",
        },
        {
            "name": "global_shape_family_exclusion",
            "status": "open",
            "statement": "A global proof still needs to exclude every fixed shape family or supply a summable moving-depth SAE bound.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "ShapeKeyRegistrationClosed",
            "closed": True,
            "proved": True,
            "meaning": "多空 atom 失败模板已有规范形状键。",
            "remaining": "closed",
        },
        {
            "gate": "FixedShapeOrMovingDepthDichotomyClosed",
            "closed": True,
            "proved": True,
            "meaning": "持久失败分流为固定形状 PDEC/ColumnCRT 或移动深度 SAE。",
            "remaining": "closed",
        },
        {
            "gate": "FiniteNoActiveShapeFailure",
            "closed": result["active_shadow_count"] == 0,
            "proved": False,
            "meaning": "有限账本没有真实 active shadow；这里只是形状证据。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "GlobalShapeFamiliesExcluded",
            "closed": False,
            "proved": False,
            "meaning": "仍需排斥固定形状族或给出移动深度可求和。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只完成形状分流，不关闭全局行/列命题。",
            "remaining": NEXT_TARGET,
        },
    ]


def build_result(input_ledger: Path) -> dict[str, Any]:
    """构造路由器结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    source = load_json(input_ledger)
    rows = source["positive_required_template_frontier"]
    shape_records: list[dict[str, Any]] = []
    for row in rows:
        for template in row["void_subset_templates"]:
            shape_records.append(template_shape(row, template))
    shape_counter = Counter(record["shape_key"] for record in shape_records)
    route_counter = Counter(record["shape_route"] for record in shape_records)
    examples: dict[str, list[dict[str, Any]]] = defaultdict(list)
    stats: dict[str, dict[str, Any]] = {}
    for record in shape_records:
        key = record["shape_key"]
        if len(examples[key]) < 5:
            examples[key].append(record)
        stat = stats.setdefault(
            key,
            {
                "shape_key": key,
                "count": 0,
                "route": record["shape_route"],
                "min_p": record["p"],
                "max_p": record["p"],
                "min_candidate_count": record["combined_candidate_count"],
                "max_candidate_count": record["combined_candidate_count"],
                "max_k": record["max_k"],
                "examples": examples[key],
            },
        )
        stat["count"] += 1
        stat["min_p"] = min(stat["min_p"], record["p"])
        stat["max_p"] = max(stat["max_p"], record["p"])
        stat["min_candidate_count"] = min(stat["min_candidate_count"], record["combined_candidate_count"])
        stat["max_candidate_count"] = max(stat["max_candidate_count"], record["combined_candidate_count"])
        stat["max_k"] = max(stat["max_k"], record["max_k"])
    shape_summaries = sorted(
        stats.values(),
        key=lambda item: (-item["count"], item["route"], item["shape_key"]),
    )
    active_shadow_count = source["aggregate"]["multi_void_gap_shadow_active_count"]
    aggregate = {
        "input_ledger": str(input_ledger.relative_to(ROOT)),
        "template_count": len(shape_records),
        "shape_count": len(shape_counter),
        "active_shadow_count": active_shadow_count,
        "route_counts": dict(route_counter),
        "max_shape_occurrence_count": max(shape_counter.values(), default=0),
        "fixed_small_k_shape_count": sum(1 for item in shape_summaries if item["route"] == "FixedSmallK-PDEC/ColumnCRT"),
        "moving_depth_shape_count": sum(1 for item in shape_summaries if item["route"] == "MovingDepth-SAE"),
    }
    ledger = {
        "parameters": source["parameters"],
        "aggregate": aggregate,
        "shape_summaries": shape_summaries,
        "shape_records": shape_records,
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = {
        "certificate_type": "prime_matrix_square_phase_offband_prefix_gap_shadow_shape_router",
        "status": "multivoid_gap_shadow_reduced_to_shape_pdec_or_moving_depth_sae_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "empirical_absence_not_used_as_proof": True,
        "parameters": source["parameters"],
        "aggregate": aggregate,
        "active_shadow_count": active_shadow_count,
        "shape_summaries": shape_summaries[:40],
        "shape_key_registration_closed": True,
        "fixed_shape_or_moving_depth_route_closed": True,
        "global_shape_family_exclusion_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_shape_router.py": sha256(
                Path(__file__).resolve()
            ),
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_router.py": sha256(GAP_SHADOW_ROUTER),
            "data/square-phase-offband-prefix-gap-shadow-ledger.json": sha256(input_ledger),
            "data/square-phase-offband-prefix-gap-shadow-shape-ledger.json": sha256(OUT_LEDGER),
        },
        "plain_conclusion": (
            "本步把多 atom prime-void gap shadow 进一步登记成形状键："
            "每个失败模板由 side、W、实际前缀数 N、强制空 atom 数 V，以及有序 band/k 原子确定。"
            "持久失败若形状固定且 k 有界，则进入 FixedSmallK-PDEC/ColumnCRT；若 k 或深度漂移，"
            "则进入 MovingDepth-SAE。有限账本只给出形状样本，不构成全局排斥。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow shape router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"input_ledger={agg['input_ledger']}",
        f"template_count={agg['template_count']}",
        f"shape_count={agg['shape_count']}",
        f"active_shadow_count={agg['active_shadow_count']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 形状键",
        "",
        "每个 failure 模板登记为",
        "",
        "```text",
        "shape_key = side | W | N | V | ordered(band:k)",
        "```",
        "",
        "其中 `V` 是 failure 强制 prime-void 的 atom 数。这个键只记录结构形状，不把有限样本当成全局规律。",
        "",
        "## 2. 分流",
        "",
        "| route | count |",
        "| --- | ---: |",
    ]
    for route, count in sorted(agg["route_counts"].items()):
        lines.append(f"| `{route}` | {count} |")
    lines.extend(
        [
            "",
            "固定小 `k` 的持久形状进入 PDEC/ColumnCRT；随 `k` 或深度漂移的形状进入 MovingDepth-SAE。",
            "",
            "## 3. 形状摘要",
            "",
            "| count | route | shape | P range | candidates | examples |",
            "| ---: | --- | --- | --- | --- | --- |",
        ]
    )
    for item in result["shape_summaries"][:24]:
        examples = "; ".join(
            f"P={example['p']} {example['side']} {example['void_atom_keys']}"
            for example in item["examples"][:3]
        )
        lines.append(
            "| "
            + " | ".join(
                [
                    str(item["count"]),
                    f"`{item['route']}`",
                    f"`{item['shape_key']}`",
                    f"{item['min_p']}..{item['max_p']}",
                    f"{item['min_candidate_count']}..{item['max_candidate_count']}",
                    table_cell(examples),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 4. 命题行",
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
            "- 主攻：`FixedPrefixGapShadowShapePDECOrMovingDepthSAEExclusion`。",
            "- 对固定小 `k` 形状，需要构造 ColumnCRT/PDEC 排斥。",
            "- 对移动深度形状，需要给出可求和 SAE 或证明其不可能持久。",
            "- 当前仍未证明全局行/列无条件闭合。",
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
    parser.add_argument("--input-ledger", type=Path, default=INPUT_LEDGER)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    input_ledger = args.input_ledger
    if not input_ledger.is_absolute():
        input_ledger = ROOT / input_ledger
    result = build_result(input_ledger)
    write_markdown(result)
    result["source_hashes"][
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-shape-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "template_count": result["aggregate"]["template_count"],
                "shape_count": result["aggregate"]["shape_count"],
                "active_shadow_count": result["active_shadow_count"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
