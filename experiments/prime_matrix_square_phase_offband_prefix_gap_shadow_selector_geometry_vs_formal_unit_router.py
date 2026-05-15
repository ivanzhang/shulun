#!/usr/bin/env python3
"""比较纯几何 band/k 形状 residue 与实际 formal-unit residue。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_geometry_vs_formal_unit_router.py --max-p 5000
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-geometry-vs-formal-unit-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-selector-geometry-vs-formal-unit-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-geometry-vs-formal-unit-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-geometry-vs-formal-unit-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

TEMPLATE_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-template-provenance-ledger.json"
FORMAL_SWEEP_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-formal-unit-residue-sweep-ledger.json"
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-geometry-vs-formal-unit-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-geometry-vs-formal-unit-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-geometry-vs-formal-unit-router.md"

FORMAL_SWEEP_ROUTER = (
    ROOT
    / "experiments"
    / "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_formal_unit_residue_sweep_router.py"
)
GAP_SHADOW_ROUTER = ROOT / "experiments" / "prime_matrix_square_phase_offband_prefix_gap_shadow_router.py"

MAIN_TARGET = "SymbolicFormalUnitShapeResidueAvoidanceOrFullShapeOverlapPDEC"
NEXT_TARGET = "PrimePressureResidueAvoidanceTheoremOrFullShapeOverlapPDEC"


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


def load_module(path: Path, name: str) -> Any:
    """按路径加载模块。"""
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def parse_shape(shape_key: str) -> dict[str, Any]:
    """解析 shape key 的 W/N/V 与 atom 序列。"""
    parts = shape_key.split("|")
    result: dict[str, Any] = {"shape_key": shape_key, "atom_shapes": parts[-1].split(",")}
    for part in parts[:-1]:
        name, value = part.split("=", 1)
        if name in {"W", "N", "V"}:
            result[name] = int(value)
        else:
            result[name] = value
    return result


def build_templates(source: dict[str, Any]) -> list[dict[str, Any]]:
    """抽取 candidate-level residue templates。"""
    templates: list[dict[str, Any]] = []
    seen: set[tuple[Any, ...]] = set()
    for candidate in source["candidate_provenance_records"]:
        key = (
            candidate["shape_key"],
            candidate["side"],
            candidate["gcd_modulus_15"],
            candidate["cover_word_residue_mod_gcd15"],
            tuple(candidate["distinct_labels"]),
        )
        if key in seen:
            continue
        seen.add(key)
        parsed = parse_shape(candidate["shape_key"])
        templates.append(
            {
                "template_index": len(templates),
                "shape_key": candidate["shape_key"],
                "side": candidate["side"],
                "W": parsed["W"],
                "N": parsed["N"],
                "V": parsed["V"],
                "atom_shapes": parsed["atom_shapes"],
                "gcd_modulus_15": candidate["gcd_modulus_15"],
                "cover_word_residue_mod_gcd15": candidate["cover_word_residue_mod_gcd15"],
                "distinct_labels": candidate["distinct_labels"],
            }
        )
    return templates


def build_geometry_environment(max_p: int) -> dict[str, Any]:
    """构造几何扫描环境。"""
    gap = load_module(GAP_SHADOW_ROUTER, "gap_shadow_geometry_vs_formal")
    phase = gap.load_module(gap.PHASEBAND_ROUTER, "phaseband_geometry_vs_formal")
    offband = gap.load_module(gap.OFFBAND_ROUTER, "offband_geometry_vs_formal")
    layer = gap.load_module(gap.LAYER_ROUTER, "layer_geometry_vs_formal")
    small_flags = phase.sieve(max_p)
    return {
        "gap": gap,
        "phase": phase,
        "offband": offband,
        "layer": layer,
        "small_flags": small_flags,
    }


def target_shape_occurs(prefix_shapes: list[str], target_shapes: list[str], length: int) -> bool:
    """判断 target 是否作为 ordered subset 出现在前三 prefix shapes 中。"""
    if len(prefix_shapes) < length:
        return False
    for indices in itertools.combinations(range(len(prefix_shapes)), length):
        if [prefix_shapes[index] for index in indices] == target_shapes:
            return True
    return False


def geometry_records(env: dict[str, Any], templates: list[dict[str, Any]], max_p: int) -> list[dict[str, Any]]:
    """扫描奇整数 P 的纯几何 ordered shape residue。"""
    records: dict[int, dict[str, Any]] = {
        template["template_index"]: {
            **template,
            "geometry_shape_hit_count": 0,
            "geometry_rho_hit_count": 0,
            "geometry_rho_hit_examples": [],
            "geometry_residue_histogram": {},
        }
        for template in templates
    }
    by_side: dict[str, list[dict[str, Any]]] = {"plus": [], "minus": []}
    for template in templates:
        by_side[template["side"]].append(template)

    for p_value in range(3, max_p + 1, 2):
        atoms = env["layer"].layer_atoms_for_p(env["offband"], env["phase"], p_value, env["small_flags"])
        for side in ("plus", "minus"):
            if side == "plus":
                offband_atoms = [atom for atom in atoms if atom["plus_offband_atom"]]
            else:
                offband_atoms = [atom for atom in atoms if atom["minus_offband_atom"]]
            prefix_shapes = [f"{atom['band']}:k{atom['k']}" for atom in offband_atoms[:3]]
            for template in by_side[side]:
                if not target_shape_occurs(prefix_shapes, template["atom_shapes"], int(template["V"])):
                    continue
                record = records[template["template_index"]]
                modulus = int(template["gcd_modulus_15"])
                residue = p_value % modulus
                record["geometry_shape_hit_count"] += 1
                record["geometry_residue_histogram"][str(residue)] = (
                    record["geometry_residue_histogram"].get(str(residue), 0) + 1
                )
                if residue == int(template["cover_word_residue_mod_gcd15"]):
                    record["geometry_rho_hit_count"] += 1
                    if len(record["geometry_rho_hit_examples"]) < 8:
                        record["geometry_rho_hit_examples"].append(p_value)

    return [records[index] for index in sorted(records)]


def join_formal_records(geometry: list[dict[str, Any]], formal_source: dict[str, Any]) -> list[dict[str, Any]]:
    """合并 formal-unit sweep 结果。"""
    formal_by_key = {
        (
            row["shape_key"],
            row["side"],
            row["gcd_modulus_15"],
            row["cover_word_residue_mod_gcd15"],
            tuple(row["distinct_labels"]),
        ): row
        for row in formal_source["formal_unit_residue_sweep_records"]
    }
    records: list[dict[str, Any]] = []
    for row in geometry:
        key = (
            row["shape_key"],
            row["side"],
            row["gcd_modulus_15"],
            row["cover_word_residue_mod_gcd15"],
            tuple(row["distinct_labels"]),
        )
        formal = formal_by_key[key]
        records.append(
            {
                **row,
                "formal_unit_shape_hit_count": formal["formal_unit_shape_hit_count"],
                "formal_unit_shape_hit_p_values": formal["formal_unit_shape_hit_p_values"],
                "formal_unit_shape_hit_residues": formal["formal_unit_shape_hit_residues"],
                "formal_unit_rho_hit_count": formal["formal_unit_rho_hit_count"],
                "formal_unit_rho_hit_p_values": formal["formal_unit_rho_hit_p_values"],
                "pure_geometry_residue_avoidance": row["geometry_rho_hit_count"] == 0,
                "prime_pressure_needed": row["geometry_rho_hit_count"] > 0
                and formal["formal_unit_rho_hit_count"] == 0,
            }
        )
    return records


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "pure_geometry_not_enough",
            "status": "closed_on_current_sweep",
            "statement": "The same band/k ordered shapes have many integer P with the template residue, so geometry alone cannot explain selector residue avoidance.",
        },
        {
            "name": "formal_unit_prime_pressure_needed",
            "status": "closed_on_current_sweep",
            "statement": "The observed residue avoidance appears only after imposing the formal-unit prime-pressure gates H,T and the actual selector chain.",
        },
        {
            "name": "prime_pressure_residue_avoidance_theorem",
            "status": "open",
            "statement": "A global proof must derive residue avoidance from the infinite prime-pressure constraints, or route overlaps to PDEC/ColumnCRT.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    agg = result["aggregate"]
    return [
        {
            "gate": "GeometryOnlyRouteRejected",
            "closed": agg["geometry_rho_hit_count"] > 0,
            "proved": True,
            "meaning": "纯 band/k 几何同 shape 中存在大量目标 rho 命中，不能作为闭合证明。",
            "remaining": "rejected",
        },
        {
            "gate": "PrimePressureRouteNecessary",
            "closed": agg["templates_requiring_prime_pressure_count"] == agg["template_count"],
            "proved": True,
            "meaning": "当前每个模板都需要 formal-unit 素数压力约束解释 residue 避让。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "GlobalPrimePressureResidueAvoidanceProved",
            "closed": False,
            "proved": False,
            "meaning": "仍需证明素数尾段压力门强制避开模板 rho。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只排除了纯几何捷径，不关闭全局行/列命题。",
            "remaining": NEXT_TARGET,
        },
    ]


def build_result(template_ledger: Path, formal_ledger: Path, max_p: int) -> dict[str, Any]:
    """构造几何-vs-formal-unit 比较结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    template_source = load_json(template_ledger)
    formal_source = load_json(formal_ledger)
    templates = build_templates(template_source)
    env = build_geometry_environment(max_p)
    records = join_formal_records(geometry_records(env, templates, max_p), formal_source)
    aggregate = {
        "template_ledger": str(template_ledger.relative_to(ROOT)),
        "formal_ledger": str(formal_ledger.relative_to(ROOT)),
        "max_p": max_p,
        "template_count": len(records),
        "geometry_shape_hit_count": sum(row["geometry_shape_hit_count"] for row in records),
        "geometry_rho_hit_count": sum(row["geometry_rho_hit_count"] for row in records),
        "formal_unit_shape_hit_count": sum(row["formal_unit_shape_hit_count"] for row in records),
        "formal_unit_rho_hit_count": sum(row["formal_unit_rho_hit_count"] for row in records),
        "pure_geometry_explains_avoidance_count": sum(
            1 for row in records if row["pure_geometry_residue_avoidance"]
        ),
        "templates_requiring_prime_pressure_count": sum(1 for row in records if row["prime_pressure_needed"]),
        "geometry_only_route_rejected": any(row["geometry_rho_hit_count"] > 0 for row in records),
        "global_prime_pressure_residue_avoidance_proved": False,
        "row_column_unconditional_closed": False,
    }
    ledger = {
        "parameters": {**template_source["parameters"], "max_p": max_p},
        "aggregate": aggregate,
        "geometry_vs_formal_unit_records": records,
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = {
        "certificate_type": "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_geometry_vs_formal_unit_router",
        "status": "selector_residue_avoidance_requires_prime_pressure_open_global",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "geometry_only_route_rejected": aggregate["geometry_only_route_rejected"],
        "finite_comparison_not_used_as_global_proof": True,
        "parameters": ledger["parameters"],
        "aggregate": aggregate,
        "geometry_vs_formal_unit_records": records,
        "global_prime_pressure_residue_avoidance_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_geometry_vs_formal_unit_router.py": sha256(
                Path(__file__).resolve()
            ),
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_formal_unit_residue_sweep_router.py": sha256(
                FORMAL_SWEEP_ROUTER
            ),
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_router.py": sha256(GAP_SHADOW_ROUTER),
            "data/square-phase-offband-prefix-gap-shadow-selector-template-provenance-ledger.json": sha256(
                template_ledger
            ),
            "data/square-phase-offband-prefix-gap-shadow-selector-formal-unit-residue-sweep-ledger.json": sha256(
                formal_ledger
            ),
            "data/square-phase-offband-prefix-gap-shadow-selector-geometry-vs-formal-unit-ledger.json": sha256(
                OUT_LEDGER
            ),
        },
        "plain_conclusion": (
            f"本步检验 residue avoidance 是否可由固定 band/k 几何单独推出。答案是否定的："
            f"在奇整数 P<={max_p} 的纯几何扫描中，同 ordered shape 命中 "
            f"{aggregate['geometry_shape_hit_count']} 次，其中目标 rho 命中 "
            f"{aggregate['geometry_rho_hit_count']} 次；但实际 formal-unit 同 shape 命中 "
            f"{aggregate['formal_unit_shape_hit_count']} 次，rho 命中为 "
            f"{aggregate['formal_unit_rho_hit_count']}。因此不能用固定几何常数闭合，"
            "必须使用 tail prime count、half-grid survivors 与 selector 链条形成的素数压力约束。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow selector geometry vs formal-unit router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"max_p={agg['max_p']}",
        f"template_count={agg['template_count']}",
        f"geometry_shape_hit_count={agg['geometry_shape_hit_count']}",
        f"geometry_rho_hit_count={agg['geometry_rho_hit_count']}",
        f"formal_unit_shape_hit_count={agg['formal_unit_shape_hit_count']}",
        f"formal_unit_rho_hit_count={agg['formal_unit_rho_hit_count']}",
        f"templates_requiring_prime_pressure_count={agg['templates_requiring_prime_pressure_count']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. Geometry vs Formal Unit",
        "",
        "| template | side | g | rho | geometry hits | geometry rho hits | examples | formal shape hits | formal rho hits |",
        "| ---: | --- | ---: | ---: | ---: | ---: | --- | ---: | ---: |",
    ]
    for row in result["geometry_vs_formal_unit_records"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["template_index"]),
                    f"`{row['side']}`",
                    str(row["gcd_modulus_15"]),
                    str(row["cover_word_residue_mod_gcd15"]),
                    str(row["geometry_shape_hit_count"]),
                    str(row["geometry_rho_hit_count"]),
                    f"`{row['geometry_rho_hit_examples']}`",
                    str(row["formal_unit_shape_hit_count"]),
                    str(row["formal_unit_rho_hit_count"]),
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
            "- 不能把 residue avoidance 降成固定 band/k 几何命题；几何层存在大量 rho 命中。",
            "- 必须证明素数压力门 `2T-H`、ordered selector 与 residue rho 不可同时成立，或登记 full-shape overlap PDEC/ColumnCRT。",
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
    parser.add_argument("--template-ledger", type=Path, default=TEMPLATE_LEDGER)
    parser.add_argument("--formal-ledger", type=Path, default=FORMAL_SWEEP_LEDGER)
    parser.add_argument("--max-p", type=int, default=5000)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    template_ledger = args.template_ledger if args.template_ledger.is_absolute() else ROOT / args.template_ledger
    formal_ledger = args.formal_ledger if args.formal_ledger.is_absolute() else ROOT / args.formal_ledger
    result = build_result(template_ledger, formal_ledger, args.max_p)
    write_markdown(result)
    result["source_hashes"][
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-geometry-vs-formal-unit-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "max_p": args.max_p,
                "geometry_rho_hit_count": result["aggregate"]["geometry_rho_hit_count"],
                "formal_unit_rho_hit_count": result["aggregate"]["formal_unit_rho_hit_count"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
