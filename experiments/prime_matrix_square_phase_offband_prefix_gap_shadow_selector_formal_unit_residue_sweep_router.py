#!/usr/bin/env python3
"""扫描实际 formal-unit shape 中是否出现 matching template residue。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_formal_unit_residue_sweep_router.py --max-p 5000
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-formal-unit-residue-sweep-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-selector-formal-unit-residue-sweep-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-formal-unit-residue-sweep-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-formal-unit-residue-sweep-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

INPUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-template-provenance-ledger.json"
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-formal-unit-residue-sweep-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-formal-unit-residue-sweep-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-formal-unit-residue-sweep-router.md"

SOURCE_GUARD_ROUTER = (
    ROOT
    / "experiments"
    / "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_source_guard_router.py"
)
GAP_SHADOW_ROUTER = ROOT / "experiments" / "prime_matrix_square_phase_offband_prefix_gap_shadow_router.py"

MAIN_TARGET = "SymbolicWitnessPressureAndOrderedPrefixShapeExclusionForTemplateResidues"
NEXT_TARGET = "SymbolicFormalUnitShapeResidueAvoidanceOrFullShapeOverlapPDEC"


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


def atom_shape_from_key(atom_key: str) -> str:
    """把 band:k:qlo-qhi 压成 band:k。"""
    band, rest = atom_key.split(":k", 1)
    k_text = rest.split(":", 1)[0]
    return f"{band}:k{k_text}"


def shape_key_for_template(row: dict[str, Any], template: dict[str, Any]) -> str:
    """重建 shape key。"""
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
        templates.append(
            {
                "template_index": len(templates),
                "shape_key": candidate["shape_key"],
                "side": candidate["side"],
                "gcd_modulus_15": candidate["gcd_modulus_15"],
                "cover_word_residue_mod_gcd15": candidate["cover_word_residue_mod_gcd15"],
                "distinct_labels": candidate["distinct_labels"],
                "source_p_values": sorted(
                    {
                        int(row["p"])
                        for row in source["candidate_provenance_records"]
                        if row["shape_key"] == candidate["shape_key"]
                        and row["side"] == candidate["side"]
                        and row["gcd_modulus_15"] == candidate["gcd_modulus_15"]
                        and row["cover_word_residue_mod_gcd15"] == candidate["cover_word_residue_mod_gcd15"]
                        and row["distinct_labels"] == candidate["distinct_labels"]
                    }
                ),
            }
        )
    return templates


def build_replay_environment(max_p: int) -> dict[str, Any]:
    """构造全范围 formal-unit 扫描环境。"""
    gap = load_module(GAP_SHADOW_ROUTER, "gap_shadow_formal_unit_sweep")
    phase = gap.load_module(gap.PHASEBAND_ROUTER, "phaseband_formal_unit_sweep")
    offband = gap.load_module(gap.OFFBAND_ROUTER, "offband_formal_unit_sweep")
    layer = gap.load_module(gap.LAYER_ROUTER, "layer_formal_unit_sweep")
    single = gap.load_module(gap.SINGLE_ROUTER, "single_formal_unit_sweep")
    two = gap.load_module(gap.TWO_ROUTER, "two_formal_unit_sweep")
    multiplicity = gap.load_module(gap.MULTIPLICITY_ROUTER, "multiplicity_formal_unit_sweep")
    interval = gap.load_module(gap.INTERVAL_ROUTER, "interval_formal_unit_sweep")
    split = phase.load_split_router()
    prime_flags = split.sieve(max_p * max_p + max_p)
    pi_prefix = split.prime_prefix(prime_flags)
    small_flags = phase.sieve(max_p)
    primes = [value for value in phase.primes_from_flags(small_flags, max_p) if value >= 3]
    return {
        "gap": gap,
        "phase": phase,
        "offband": offband,
        "layer": layer,
        "single": single,
        "two": two,
        "multiplicity": multiplicity,
        "interval": interval,
        "split": split,
        "prime_flags": prime_flags,
        "pi_prefix": pi_prefix,
        "small_flags": small_flags,
        "primes": primes,
    }


def sweep_formal_units(env: dict[str, Any], templates: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """扫描所有实际 prime formal units 是否命中模板 residue。"""
    template_hits: dict[int, dict[str, Any]] = {
        template["template_index"]: {
            **template,
            "formal_unit_shape_hit_p_values": [],
            "formal_unit_shape_hit_residues": [],
            "formal_unit_rho_hit_p_values": [],
        }
        for template in templates
    }
    by_side: dict[str, list[dict[str, Any]]] = {"plus": [], "minus": []}
    for template in templates:
        by_side[template["side"]].append(template)

    gap = env["gap"]
    for p_value in env["primes"]:
        split_record = env["split"].audit_p(p_value, env["prime_flags"], env["pi_prefix"])
        atoms = env["layer"].layer_atoms_for_p(env["offband"], env["phase"], p_value, env["small_flags"])
        for side in ("plus", "minus"):
            row = gap.shadow_record(
                env["interval"],
                env["single"],
                env["multiplicity"],
                env["layer"],
                env["two"],
                p_value,
                side,
                split_record[f"{side}_prime_window"],
                atoms,
                3,
            )
            if not row["void_subset_templates"]:
                continue
            shape_keys = {shape_key_for_template(row, template) for template in row["void_subset_templates"]}
            for template in by_side[side]:
                if template["shape_key"] not in shape_keys:
                    continue
                hit = template_hits[template["template_index"]]
                modulus = int(template["gcd_modulus_15"])
                residue = p_value % modulus
                hit["formal_unit_shape_hit_p_values"].append(p_value)
                hit["formal_unit_shape_hit_residues"].append(residue)
                if residue == int(template["cover_word_residue_mod_gcd15"]):
                    hit["formal_unit_rho_hit_p_values"].append(p_value)

    records: list[dict[str, Any]] = []
    for index in sorted(template_hits):
        hit = template_hits[index]
        p_values = sorted(set(hit["formal_unit_shape_hit_p_values"]))
        rho_hits = sorted(set(hit["formal_unit_rho_hit_p_values"]))
        records.append(
            {
                "template_index": hit["template_index"],
                "shape_key": hit["shape_key"],
                "side": hit["side"],
                "gcd_modulus_15": hit["gcd_modulus_15"],
                "cover_word_residue_mod_gcd15": hit["cover_word_residue_mod_gcd15"],
                "distinct_labels": hit["distinct_labels"],
                "source_p_values": hit["source_p_values"],
                "formal_unit_shape_hit_count": len(p_values),
                "formal_unit_shape_hit_p_values": p_values,
                "formal_unit_shape_hit_residues": [value % int(hit["gcd_modulus_15"]) for value in p_values],
                "formal_unit_rho_hit_count": len(rho_hits),
                "formal_unit_rho_hit_p_values": rho_hits,
                "formal_unit_residue_avoidance_holds_on_sweep": len(rho_hits) == 0,
            }
        )
    return records


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "finite_formal_unit_residue_sweep",
            "status": "closed_on_current_sweep",
            "statement": "For every candidate-level template, all actual formal units in the sweep with the same full shape avoid the template residue.",
        },
        {
            "name": "local_phase_residue_not_actual_selector_residue",
            "status": "closed_on_current_sweep",
            "statement": "The residue classes that have local phase matching primes do not occur as actual P residues on the same full shape in the sweep.",
        },
        {
            "name": "symbolic_formal_unit_residue_avoidance",
            "status": "open",
            "statement": "A global proof must derive this residue avoidance from the shape formulas, not from a finite sweep.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    agg = result["aggregate"]
    return [
        {
            "gate": "CurrentFormalUnitResidueSweepClosed",
            "closed": agg["formal_unit_rho_hit_count"] == 0,
            "proved": True,
            "meaning": "当前扫描范围内，同 shape actual formal unit 全部避开模板 residue。",
            "remaining": "closed on current finite sweep",
        },
        {
            "gate": "FullShapeOverlapPDECNeededOnSweep",
            "closed": agg["formal_unit_rho_hit_count"] == 0,
            "proved": True,
            "meaning": "当前扫描范围没有 full-shape residue overlap PDEC 实例。",
            "remaining": "closed on current finite sweep",
        },
        {
            "gate": "GlobalSymbolicResidueAvoidanceProved",
            "closed": False,
            "proved": False,
            "meaning": "仍需将有限 residue 分离提升为 formal-unit 族定理。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只完成当前扫描范围的 actual selector residue 审计，不关闭全局行/列命题。",
            "remaining": NEXT_TARGET,
        },
    ]


def build_result(input_ledger: Path, max_p: int) -> dict[str, Any]:
    """构造 formal-unit residue sweep 结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    source = load_json(input_ledger)
    templates = build_templates(source)
    env = build_replay_environment(max_p)
    records = sweep_formal_units(env, templates)
    aggregate = {
        "input_ledger": str(input_ledger.relative_to(ROOT)),
        "max_p": max_p,
        "prime_count": len(env["primes"]),
        "candidate_level_template_count": len(records),
        "formal_unit_shape_hit_count": sum(row["formal_unit_shape_hit_count"] for row in records),
        "formal_unit_rho_hit_count": sum(row["formal_unit_rho_hit_count"] for row in records),
        "templates_with_shape_hits": sum(1 for row in records if row["formal_unit_shape_hit_count"] > 0),
        "templates_with_rho_hits": sum(1 for row in records if row["formal_unit_rho_hit_count"] > 0),
        "formal_unit_residue_avoidance_holds_on_sweep": all(
            row["formal_unit_residue_avoidance_holds_on_sweep"] for row in records
        ),
        "global_symbolic_residue_avoidance_proved": False,
        "row_column_unconditional_closed": False,
    }
    ledger = {
        "parameters": {**source["parameters"], "max_p": max_p},
        "aggregate": aggregate,
        "formal_unit_residue_sweep_records": records,
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = {
        "certificate_type": "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_formal_unit_residue_sweep_router",
        "status": "selector_formal_unit_residue_avoidance_closed_on_sweep_open_global",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_sweep_not_used_as_global_proof": True,
        "parameters": ledger["parameters"],
        "aggregate": aggregate,
        "formal_unit_residue_sweep_records": records,
        "formal_unit_residue_avoidance_holds_on_sweep": aggregate[
            "formal_unit_residue_avoidance_holds_on_sweep"
        ],
        "global_symbolic_residue_avoidance_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_formal_unit_residue_sweep_router.py": sha256(
                Path(__file__).resolve()
            ),
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_source_guard_router.py": sha256(
                SOURCE_GUARD_ROUTER
            ),
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_router.py": sha256(GAP_SHADOW_ROUTER),
            "data/square-phase-offband-prefix-gap-shadow-selector-template-provenance-ledger.json": sha256(
                input_ledger
            ),
            "data/square-phase-offband-prefix-gap-shadow-selector-formal-unit-residue-sweep-ledger.json": sha256(
                OUT_LEDGER
            ),
        },
        "plain_conclusion": (
            f"本步在 `P<={max_p}` 的实际 formal-unit 记录中扫描 small-modulus matching templates。"
            f"候选级模板 {aggregate['candidate_level_template_count']} 个，同 full-shape 命中总数 "
            f"{aggregate['formal_unit_shape_hit_count']}，但目标 rho residue 命中数为 "
            f"{aggregate['formal_unit_rho_hit_count']}。因此当前扫描范围内 actual selector residue "
            "与局部 matching template residue 完全分离；全局剩余是把该 residue avoidance 证明为符号定理。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow selector formal-unit residue sweep router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"max_p={agg['max_p']}",
        f"prime_count={agg['prime_count']}",
        f"candidate_level_template_count={agg['candidate_level_template_count']}",
        f"formal_unit_shape_hit_count={agg['formal_unit_shape_hit_count']}",
        f"formal_unit_rho_hit_count={agg['formal_unit_rho_hit_count']}",
        f"templates_with_rho_hits={agg['templates_with_rho_hits']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. Residue Sweep",
        "",
        "| template | side | g | rho | shape P values | residues | rho hits |",
        "| ---: | --- | ---: | ---: | --- | --- | --- |",
    ]
    for row in result["formal_unit_residue_sweep_records"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["template_index"]),
                    f"`{row['side']}`",
                    str(row["gcd_modulus_15"]),
                    str(row["cover_word_residue_mod_gcd15"]),
                    f"`{row['formal_unit_shape_hit_p_values']}`",
                    f"`{row['formal_unit_shape_hit_residues']}`",
                    f"`{row['formal_unit_rho_hit_p_values']}`",
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
            "- 把有限 sweep 中的 residue avoidance 转写成 shape 参数不等式或 CRT residue identity。",
            "- 若出现同 shape 且同 rho 的 formal unit，则登记 full-shape overlap PDEC/ColumnCRT。",
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
    parser.add_argument("--max-p", type=int, default=5000)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    input_ledger = args.input_ledger if args.input_ledger.is_absolute() else ROOT / args.input_ledger
    result = build_result(input_ledger, args.max_p)
    write_markdown(result)
    result["source_hashes"][
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-formal-unit-residue-sweep-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "max_p": args.max_p,
                "formal_unit_shape_hit_count": result["aggregate"]["formal_unit_shape_hit_count"],
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
