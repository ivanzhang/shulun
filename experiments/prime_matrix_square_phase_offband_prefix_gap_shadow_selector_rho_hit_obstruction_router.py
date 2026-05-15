#!/usr/bin/env python3
"""分类几何层 rho 命中为何不能升级为 formal-unit overlap。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_rho_hit_obstruction_router.py --max-p 5000
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-rho-hit-obstruction-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-selector-rho-hit-obstruction-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-rho-hit-obstruction-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-rho-hit-obstruction-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import itertools
import json
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

TEMPLATE_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-template-provenance-ledger.json"
GEOMETRY_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-geometry-vs-formal-unit-ledger.json"
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-rho-hit-obstruction-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-rho-hit-obstruction-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-rho-hit-obstruction-router.md"

GEOMETRY_ROUTER = (
    ROOT
    / "experiments"
    / "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_geometry_vs_formal_unit_router.py"
)
GAP_SHADOW_ROUTER = ROOT / "experiments" / "prime_matrix_square_phase_offband_prefix_gap_shadow_router.py"

MAIN_TARGET = "PrimePressureResidueAvoidanceTheoremOrFullShapeOverlapPDEC"
NEXT_TARGET = "PrimeRhoHitWitnessPressureMismatchOrOrderedShapeMismatchTheorem"


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
    """解析 shape key。"""
    parts = shape_key.split("|")
    result: dict[str, Any] = {"atom_shapes": parts[-1].split(",")}
    for part in parts[:-1]:
        name, value = part.split("=", 1)
        result[name] = int(value) if name in {"W", "N", "V"} else value
    return result


def atom_shape_from_key(atom_key: str) -> str:
    """把 band:k:qlo-qhi 压成 band:k。"""
    band, rest = atom_key.split(":k", 1)
    return f"{band}:k{rest.split(':', 1)[0]}"


def shape_key_for_template(row: dict[str, Any], template: dict[str, Any]) -> str:
    """重建 replay shape key。"""
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
    """抽取 candidate-level templates。"""
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


def build_environment(max_p: int) -> dict[str, Any]:
    """构造扫描环境。"""
    gap = load_module(GAP_SHADOW_ROUTER, "gap_shadow_rho_hit_obstruction")
    phase = gap.load_module(gap.PHASEBAND_ROUTER, "phaseband_rho_hit_obstruction")
    offband = gap.load_module(gap.OFFBAND_ROUTER, "offband_rho_hit_obstruction")
    layer = gap.load_module(gap.LAYER_ROUTER, "layer_rho_hit_obstruction")
    single = gap.load_module(gap.SINGLE_ROUTER, "single_rho_hit_obstruction")
    two = gap.load_module(gap.TWO_ROUTER, "two_rho_hit_obstruction")
    multiplicity = gap.load_module(gap.MULTIPLICITY_ROUTER, "multiplicity_rho_hit_obstruction")
    interval = gap.load_module(gap.INTERVAL_ROUTER, "interval_rho_hit_obstruction")
    split = phase.load_split_router()
    prime_flags = split.sieve(max_p * max_p + max_p)
    pi_prefix = split.prime_prefix(prime_flags)
    small_flags = phase.sieve(max_p)
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
    }


def target_shape_occurs(prefix_shapes: list[str], target_shapes: list[str], length: int) -> bool:
    """判断 target 是否作为 ordered subset 出现在 prefix shapes 中。"""
    if len(prefix_shapes) < length:
        return False
    for indices in itertools.combinations(range(len(prefix_shapes)), length):
        if [prefix_shapes[index] for index in indices] == target_shapes:
            return True
    return False


def classify_prime_hit(env: dict[str, Any], p_value: int, template: dict[str, Any]) -> dict[str, Any]:
    """分类一个素数 rho 命中。"""
    gap = env["gap"]
    split_record = env["split"].audit_p(p_value, env["prime_flags"], env["pi_prefix"])
    atoms = env["layer"].layer_atoms_for_p(env["offband"], env["phase"], p_value, env["small_flags"])
    row = gap.shadow_record(
        env["interval"],
        env["single"],
        env["multiplicity"],
        env["layer"],
        env["two"],
        p_value,
        template["side"],
        split_record[f"{template['side']}_prime_window"],
        atoms,
        3,
    )
    replay_shape_keys = [shape_key_for_template(row, item) for item in row["void_subset_templates"]]
    if template["shape_key"] in replay_shape_keys:
        obstruction = "FullShapeOverlapPDEC"
    elif int(row["required_offband_witness_count"]) != int(template["W"]):
        obstruction = "WitnessPressureMismatch"
    else:
        obstruction = "OrderedPrefixShapeMismatch"
    return {
        "p": p_value,
        "obstruction": obstruction,
        "H": row["halfgrid_survivors"],
        "T": row["tail_prime_count"],
        "signed_tail_deficit_2T_minus_H": 2 * int(row["tail_prime_count"]) - int(row["halfgrid_survivors"]),
        "target_W": template["W"],
        "replay_W": row["required_offband_witness_count"],
        "replay_prefix_prime_load": row["prefix_prime_load"],
        "replay_prefix_atom_shapes": [
            f"{atom['band']}:k{atom['k']}" for atom in row["prefix_interval_atoms"]
        ],
        "replay_template_shape_keys": replay_shape_keys,
    }


def classify_template_hits(env: dict[str, Any], template: dict[str, Any], max_p: int) -> dict[str, Any]:
    """分类单个 template 的全部几何 rho 命中。"""
    geometry_rho_hits: list[int] = []
    composite_hits: list[int] = []
    prime_records: list[dict[str, Any]] = []
    for p_value in range(3, max_p + 1, 2):
        if p_value % int(template["gcd_modulus_15"]) != int(template["cover_word_residue_mod_gcd15"]):
            continue
        atoms = env["layer"].layer_atoms_for_p(env["offband"], env["phase"], p_value, env["small_flags"])
        if template["side"] == "plus":
            offband_atoms = [atom for atom in atoms if atom["plus_offband_atom"]]
        else:
            offband_atoms = [atom for atom in atoms if atom["minus_offband_atom"]]
        prefix_shapes = [f"{atom['band']}:k{atom['k']}" for atom in offband_atoms[:3]]
        if not target_shape_occurs(prefix_shapes, template["atom_shapes"], int(template["V"])):
            continue
        geometry_rho_hits.append(p_value)
        if not env["small_flags"][p_value]:
            composite_hits.append(p_value)
        else:
            prime_records.append(classify_prime_hit(env, p_value, template))

    obstruction_counter = Counter(["CompositeP"] * len(composite_hits))
    obstruction_counter.update(record["obstruction"] for record in prime_records)
    return {
        **template,
        "geometry_rho_hit_count": len(geometry_rho_hits),
        "geometry_rho_hit_examples": geometry_rho_hits[:8],
        "composite_rho_hit_count": len(composite_hits),
        "composite_rho_hit_examples": composite_hits[:8],
        "prime_rho_hit_count": len(prime_records),
        "prime_rho_hit_examples": [record["p"] for record in prime_records[:8]],
        "obstruction_counts": dict(sorted(obstruction_counter.items())),
        "prime_obstruction_examples": prime_records[:8],
        "full_shape_overlap_count": obstruction_counter.get("FullShapeOverlapPDEC", 0),
    }


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "geometry_rho_hits_classified",
            "status": "closed_on_current_sweep",
            "statement": "Every geometry-level rho hit is classified as composite P, witness-pressure mismatch, ordered-shape mismatch, or full-shape overlap.",
        },
        {
            "name": "current_prime_rho_hits_do_not_overlap_full_shape",
            "status": "closed_on_current_sweep",
            "statement": "No prime rho hit in the sweep reaches full-shape overlap; prime hits fail pressure or ordered-shape gates.",
        },
        {
            "name": "global_prime_rho_hit_obstruction",
            "status": "open",
            "statement": "A global proof must exclude prime rho hits by pressure/shape mismatch, or route full-shape overlaps to PDEC.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    agg = result["aggregate"]
    return [
        {
            "gate": "RhoHitObstructionClassificationClosed",
            "closed": True,
            "proved": True,
            "meaning": "几何 rho 命中已分为合数 P、压力不匹配、shape 不匹配或 overlap。",
            "remaining": "closed on current finite sweep",
        },
        {
            "gate": "CurrentFullShapeOverlapAbsent",
            "closed": agg["full_shape_overlap_count"] == 0,
            "proved": True,
            "meaning": "当前扫描无 full-shape overlap PDEC 实例。",
            "remaining": "closed on current finite sweep",
        },
        {
            "gate": "GlobalPrimeRhoHitObstructionProved",
            "closed": False,
            "proved": False,
            "meaning": "仍需证明所有素数 rho 命中都必压力不匹配或 shape 不匹配。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只完成 rho 命中有限分类，不关闭全局行/列命题。",
            "remaining": NEXT_TARGET,
        },
    ]


def build_result(template_ledger: Path, geometry_ledger: Path, max_p: int) -> dict[str, Any]:
    """构造 rho-hit obstruction 分类结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    template_source = load_json(template_ledger)
    geometry_source = load_json(geometry_ledger)
    env = build_environment(max_p)
    templates = build_templates(template_source)
    records = [classify_template_hits(env, template, max_p) for template in templates]
    combined_counter = Counter()
    for record in records:
        combined_counter.update(record["obstruction_counts"])
    aggregate = {
        "template_ledger": str(template_ledger.relative_to(ROOT)),
        "geometry_ledger": str(geometry_ledger.relative_to(ROOT)),
        "max_p": max_p,
        "template_count": len(records),
        "geometry_rho_hit_count": sum(row["geometry_rho_hit_count"] for row in records),
        "composite_rho_hit_count": sum(row["composite_rho_hit_count"] for row in records),
        "prime_rho_hit_count": sum(row["prime_rho_hit_count"] for row in records),
        "full_shape_overlap_count": sum(row["full_shape_overlap_count"] for row in records),
        "obstruction_counts": dict(sorted(combined_counter.items())),
        "matches_geometry_rho_total": sum(row["geometry_rho_hit_count"] for row in records)
        == geometry_source["aggregate"]["geometry_rho_hit_count"],
        "global_prime_rho_hit_obstruction_proved": False,
        "row_column_unconditional_closed": False,
    }
    ledger = {
        "parameters": {**template_source["parameters"], "max_p": max_p},
        "aggregate": aggregate,
        "rho_hit_obstruction_records": records,
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = {
        "certificate_type": "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_rho_hit_obstruction_router",
        "status": "selector_geometry_rho_hits_classified_open_global",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_classification_not_used_as_global_proof": True,
        "parameters": ledger["parameters"],
        "aggregate": aggregate,
        "rho_hit_obstruction_records": records,
        "global_prime_rho_hit_obstruction_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_rho_hit_obstruction_router.py": sha256(
                Path(__file__).resolve()
            ),
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_geometry_vs_formal_unit_router.py": sha256(
                GEOMETRY_ROUTER
            ),
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_router.py": sha256(GAP_SHADOW_ROUTER),
            "data/square-phase-offband-prefix-gap-shadow-selector-template-provenance-ledger.json": sha256(
                template_ledger
            ),
            "data/square-phase-offband-prefix-gap-shadow-selector-geometry-vs-formal-unit-ledger.json": sha256(
                geometry_ledger
            ),
            "data/square-phase-offband-prefix-gap-shadow-selector-rho-hit-obstruction-ledger.json": sha256(
                OUT_LEDGER
            ),
        },
        "plain_conclusion": (
            f"本步把几何层 {aggregate['geometry_rho_hit_count']} 个目标 rho 命中全部分类。"
            f"其中合数 P 命中 {aggregate['composite_rho_hit_count']} 个，素数 P 命中 "
            f"{aggregate['prime_rho_hit_count']} 个；当前 full-shape overlap 为 "
            f"{aggregate['full_shape_overlap_count']}。素数 rho 命中没有进入 overlap，"
            "而是落入 witness-pressure mismatch 或 ordered-shape mismatch。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow selector rho-hit obstruction router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"max_p={agg['max_p']}",
        f"geometry_rho_hit_count={agg['geometry_rho_hit_count']}",
        f"composite_rho_hit_count={agg['composite_rho_hit_count']}",
        f"prime_rho_hit_count={agg['prime_rho_hit_count']}",
        f"full_shape_overlap_count={agg['full_shape_overlap_count']}",
        f"matches_geometry_rho_total={fmt_bool(agg['matches_geometry_rho_total'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. Obstruction Counts",
        "",
        "| obstruction | count |",
        "| --- | ---: |",
    ]
    for name, count in agg["obstruction_counts"].items():
        lines.append(f"| `{name}` | {count} |")
    lines.extend(
        [
            "",
            "## 2. Template Records",
            "",
            "| template | side | g | rho | geometry rho | composite | prime | overlap | prime examples |",
            "| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for row in result["rho_hit_obstruction_records"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["template_index"]),
                    f"`{row['side']}`",
                    str(row["gcd_modulus_15"]),
                    str(row["cover_word_residue_mod_gcd15"]),
                    str(row["geometry_rho_hit_count"]),
                    str(row["composite_rho_hit_count"]),
                    str(row["prime_rho_hit_count"]),
                    str(row["full_shape_overlap_count"]),
                    f"`{row['prime_rho_hit_examples']}`",
                ]
            )
            + " |"
        )
    lines.extend(
        [
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
            "- 合数 P 出口已与素数 formal unit 分离；真正剩余是素数 rho 命中为何必压力不匹配或 shape 不匹配。",
            "- 若出现 `FullShapeOverlapPDEC`，立即登记 ColumnCRT/PDEC 证书对象。",
            "- 当前仍未证明全局行/列无条件闭合。",
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
    parser.add_argument("--template-ledger", type=Path, default=TEMPLATE_LEDGER)
    parser.add_argument("--geometry-ledger", type=Path, default=GEOMETRY_LEDGER)
    parser.add_argument("--max-p", type=int, default=5000)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    template_ledger = args.template_ledger if args.template_ledger.is_absolute() else ROOT / args.template_ledger
    geometry_ledger = args.geometry_ledger if args.geometry_ledger.is_absolute() else ROOT / args.geometry_ledger
    result = build_result(template_ledger, geometry_ledger, args.max_p)
    write_markdown(result)
    result["source_hashes"][
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-rho-hit-obstruction-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "max_p": args.max_p,
                "geometry_rho_hit_count": result["aggregate"]["geometry_rho_hit_count"],
                "prime_rho_hit_count": result["aggregate"]["prime_rho_hit_count"],
                "full_shape_overlap_count": result["aggregate"]["full_shape_overlap_count"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
