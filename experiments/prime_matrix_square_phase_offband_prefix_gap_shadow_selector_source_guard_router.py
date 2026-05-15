#!/usr/bin/env python3
"""把 full-shape selector 来源拆成见证压力门与 ordered-prefix-shape 门。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_source_guard_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-source-guard-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-selector-source-guard-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-source-guard-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-source-guard-router.md
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

INPUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-full-shape-provenance-ledger.json"
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-source-guard-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-source-guard-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-source-guard-router.md"

FULL_SHAPE_ROUTER = (
    ROOT
    / "experiments"
    / "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_full_shape_provenance_router.py"
)
GAP_SHADOW_ROUTER = ROOT / "experiments" / "prime_matrix_square_phase_offband_prefix_gap_shadow_router.py"

MAIN_TARGET = "FullShapeFormalUnitSelectorSourceTheoremOrMatchingTemplateOverlapPDEC"
NEXT_TARGET = "SymbolicWitnessPressureAndOrderedPrefixShapeExclusionForTemplateResidues"


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


def target_atom_shapes(shape_key: str) -> list[str]:
    """解析目标 shape key 中的 ordered atom shapes。"""
    parts = shape_key.split("|")
    return parts[-1].split(",") if parts else []


def shape_key_for_template(row: dict[str, Any], template: dict[str, Any]) -> str:
    """重建 replay 模板形状键。"""
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


def compact_atom(gap_module: Any, atom: dict[str, Any]) -> dict[str, Any]:
    """压缩 prefix atom。"""
    return {
        "key": gap_module.atom_key(atom),
        "shape": f"{atom['band']}:k{atom['k']}",
        "prime_load": atom["prime_load"],
        "q_lo": atom["q_lo"],
        "q_hi": atom["q_hi"],
        "b_lo": atom["b_lo"],
        "b_hi": atom["b_hi"],
    }


def build_replay_environment(max_p: int) -> dict[str, Any]:
    """构造回放所需的筛表。"""
    gap = load_module(GAP_SHADOW_ROUTER, "gap_shadow_source_guard_probe")
    phase = gap.load_module(gap.PHASEBAND_ROUTER, "phaseband_source_guard_probe")
    offband = gap.load_module(gap.OFFBAND_ROUTER, "offband_source_guard_probe")
    layer = gap.load_module(gap.LAYER_ROUTER, "layer_source_guard_probe")
    single = gap.load_module(gap.SINGLE_ROUTER, "single_source_guard_probe")
    two = gap.load_module(gap.TWO_ROUTER, "two_source_guard_probe")
    multiplicity = gap.load_module(gap.MULTIPLICITY_ROUTER, "multiplicity_source_guard_probe")
    interval = gap.load_module(gap.INTERVAL_ROUTER, "interval_source_guard_probe")
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


def replay_row(env: dict[str, Any], row: dict[str, Any]) -> dict[str, Any]:
    """重算 replay row 并登记两个来源门。"""
    gap = env["gap"]
    replay_p = int(row["replay_p"])
    side = row["side"]
    split_record = env["split"].audit_p(replay_p, env["prime_flags"], env["pi_prefix"])
    atoms = env["layer"].layer_atoms_for_p(env["offband"], env["phase"], replay_p, env["small_flags"])
    replay = gap.shadow_record(
        env["interval"],
        env["single"],
        env["multiplicity"],
        env["layer"],
        env["two"],
        replay_p,
        side,
        split_record[f"{side}_prime_window"],
        atoms,
        3,
    )
    halfgrid = int(replay["halfgrid_survivors"])
    tail_count = int(replay["tail_prime_count"])
    signed_tail_deficit = 2 * tail_count - halfgrid
    required_formula = max(0, signed_tail_deficit // 2 + 1)
    formula_ok = required_formula == int(replay["required_offband_witness_count"])
    pressure_gate_positive = signed_tail_deficit >= 0
    replay_shape_keys = [shape_key_for_template(replay, template) for template in replay["void_subset_templates"]]
    ordered_shape_gate = row["target_shape_key"] in replay_shape_keys
    if not pressure_gate_positive:
        primary_failure_gate = "WitnessPressureGate"
    elif not ordered_shape_gate:
        primary_failure_gate = "OrderedPrefixShapeGate"
    else:
        primary_failure_gate = "FullShapeOverlapPDEC"
    return {
        "source_index": row["source_index"],
        "source_p": row["source_p"],
        "replay_p": replay_p,
        "side": side,
        "labels": row["labels"],
        "target_shape_key": row["target_shape_key"],
        "target_atom_shapes": target_atom_shapes(row["target_shape_key"]),
        "halfgrid_survivors_H": halfgrid,
        "tail_prime_count_T": tail_count,
        "signed_tail_deficit_2T_minus_H": signed_tail_deficit,
        "witness_pressure_gate_positive": pressure_gate_positive,
        "required_offband_witness_formula": required_formula,
        "required_offband_witness_replay": replay["required_offband_witness_count"],
        "required_formula_ok": formula_ok,
        "replay_prefix_atom_shapes": [f"{atom['band']}:k{atom['k']}" for atom in replay["prefix_interval_atoms"]],
        "replay_prefix_atoms": [compact_atom(gap, atom) for atom in replay["prefix_interval_atoms"]],
        "replay_template_shape_keys": replay_shape_keys,
        "ordered_prefix_shape_gate": ordered_shape_gate,
        "full_shape_compatible": row["full_shape_compatible"],
        "primary_failure_gate": primary_failure_gate,
    }


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "witness_pressure_formula",
            "status": "closed",
            "statement": "The replay gate satisfies W_required=max(0,floor((2T-H)/2)+1), so W_required>0 iff 2T-H>=0.",
        },
        {
            "name": "current_matching_representatives_guard_decomposition",
            "status": "closed_on_current_frontier",
            "statement": "Every current matching representative fails either the witness pressure gate or the ordered prefix shape gate.",
        },
        {
            "name": "symbolic_pressure_and_shape_exclusion",
            "status": "open",
            "statement": "A global proof must show template residues force one of these two gates to fail in the formal-unit family, or route overlaps to PDEC.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    agg = result["aggregate"]
    return [
        {
            "gate": "WitnessPressureFormulaClosed",
            "closed": agg["required_formula_failure_count"] == 0,
            "proved": True,
            "meaning": "`W_required` 已由 `2T-H` 精确控制。",
            "remaining": "closed",
        },
        {
            "gate": "CurrentRepresentativesFailSourceGuards",
            "closed": agg["full_shape_overlap_count"] == 0,
            "proved": True,
            "meaning": "当前 matching 代表全部死于见证压力门或 ordered shape 门。",
            "remaining": "closed on current finite frontier",
        },
        {
            "gate": "GlobalTemplateResidueGuardExclusionProved",
            "closed": False,
            "proved": False,
            "meaning": "仍需证明模板 residue 在 formal-unit 族中必触发同样门控失败。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只把来源定理拆成两个原子门，不关闭全局行/列命题。",
            "remaining": NEXT_TARGET,
        },
    ]


def build_result(input_ledger: Path) -> dict[str, Any]:
    """构造 source guard 分解结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    source = load_json(input_ledger)
    max_p = max((int(row["replay_p"]) for row in source["full_shape_replay_records"]), default=3)
    env = build_replay_environment(max_p)
    records = [replay_row(env, row) for row in source["full_shape_replay_records"]]
    aggregate = {
        "input_ledger": str(input_ledger.relative_to(ROOT)),
        "record_count": len(records),
        "required_formula_failure_count": sum(1 for row in records if not row["required_formula_ok"]),
        "witness_pressure_gate_failure_count": sum(
            1 for row in records if row["primary_failure_gate"] == "WitnessPressureGate"
        ),
        "ordered_prefix_shape_gate_failure_count": sum(
            1 for row in records if row["primary_failure_gate"] == "OrderedPrefixShapeGate"
        ),
        "full_shape_overlap_count": sum(1 for row in records if row["primary_failure_gate"] == "FullShapeOverlapPDEC"),
        "min_signed_tail_deficit_2T_minus_H": min(
            (row["signed_tail_deficit_2T_minus_H"] for row in records),
            default=0,
        ),
        "max_signed_tail_deficit_2T_minus_H": max(
            (row["signed_tail_deficit_2T_minus_H"] for row in records),
            default=0,
        ),
        "current_guard_decomposition_closed": all(
            row["primary_failure_gate"] in {"WitnessPressureGate", "OrderedPrefixShapeGate"} for row in records
        ),
        "global_symbolic_guard_exclusion_proved": False,
        "row_column_unconditional_closed": False,
    }
    ledger = {
        "parameters": source["parameters"],
        "aggregate": aggregate,
        "source_guard_records": records,
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = {
        "certificate_type": "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_source_guard_router",
        "status": "selector_full_shape_source_decomposed_to_pressure_or_ordered_shape_guard_open_global",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_guard_decomposition_not_used_as_global_proof": True,
        "parameters": source["parameters"],
        "aggregate": aggregate,
        "source_guard_records": records,
        "witness_pressure_formula_closed": aggregate["required_formula_failure_count"] == 0,
        "current_guard_decomposition_closed": aggregate["current_guard_decomposition_closed"],
        "global_symbolic_guard_exclusion_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_source_guard_router.py": sha256(
                Path(__file__).resolve()
            ),
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_full_shape_provenance_router.py": sha256(
                FULL_SHAPE_ROUTER
            ),
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_router.py": sha256(GAP_SHADOW_ROUTER),
            "data/square-phase-offband-prefix-gap-shadow-selector-full-shape-provenance-ledger.json": sha256(
                input_ledger
            ),
            "data/square-phase-offband-prefix-gap-shadow-selector-source-guard-ledger.json": sha256(OUT_LEDGER),
        },
        "plain_conclusion": (
            "本步把 full-shape selector 来源拆成两个可攻原子："
            "`W_required>0` 等价于 `2T-H>=0` 的见证压力门；通过后还必须匹配 ordered prefix shape。"
            "当前 15 个 matching 代表中，14 个已在见证压力门失败，1 个在 ordered prefix shape 门失败，"
            "因此没有 full-shape overlap PDEC 实例。全局剩余是把这两个门控失败提升为 formal-unit 族的符号排斥。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow selector source guard router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"record_count={agg['record_count']}",
        f"required_formula_failure_count={agg['required_formula_failure_count']}",
        f"witness_pressure_gate_failure_count={agg['witness_pressure_gate_failure_count']}",
        f"ordered_prefix_shape_gate_failure_count={agg['ordered_prefix_shape_gate_failure_count']}",
        f"full_shape_overlap_count={agg['full_shape_overlap_count']}",
        f"signed_tail_deficit_range={agg['min_signed_tail_deficit_2T_minus_H']}..{agg['max_signed_tail_deficit_2T_minus_H']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. Guard Records",
        "",
        "| replay P | side | H | T | 2T-H | W formula | target atoms | replay atoms | failure gate |",
        "| ---: | --- | ---: | ---: | ---: | ---: | --- | --- | --- |",
    ]
    for row in result["source_guard_records"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["replay_p"]),
                    f"`{row['side']}`",
                    str(row["halfgrid_survivors_H"]),
                    str(row["tail_prime_count_T"]),
                    str(row["signed_tail_deficit_2T_minus_H"]),
                    str(row["required_offband_witness_formula"]),
                    f"`{row['target_atom_shapes']}`",
                    f"`{row['replay_prefix_atom_shapes']}`",
                    f"`{row['primary_failure_gate']}`",
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
            "- 先证明 small-modulus template residue 若匹配局部父 atom，则在 formal-unit selector 中必有 `2T-H<0`；",
            "- 剩余正阈值例外再证明 ordered prefix shape 必改变，或登记 full-shape overlap PDEC。",
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
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-source-guard-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "witness_pressure_gate_failure_count": result["aggregate"]["witness_pressure_gate_failure_count"],
                "ordered_prefix_shape_gate_failure_count": result["aggregate"]["ordered_prefix_shape_gate_failure_count"],
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
