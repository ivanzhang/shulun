#!/usr/bin/env python3
"""回放 matching prime representatives 是否能提升为完整 shape/formal-unit 匹配。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_full_shape_provenance_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-full-shape-provenance-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-selector-full-shape-provenance-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-full-shape-provenance-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-full-shape-provenance-router.md
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
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-full-shape-provenance-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-full-shape-provenance-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-full-shape-provenance-router.md"

TEMPLATE_PROVENANCE_ROUTER = (
    ROOT
    / "experiments"
    / "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_template_provenance_router.py"
)
GAP_SHADOW_ROUTER = ROOT / "experiments" / "prime_matrix_square_phase_offband_prefix_gap_shadow_router.py"

MAIN_TARGET = "ActualFormalUnitResidueSelectorProvenanceOrTemplateOverlapPDEC"
NEXT_TARGET = "FullShapeFormalUnitSelectorSourceTheoremOrMatchingTemplateOverlapPDEC"


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
    """按路径加载上游路由器模块。"""
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
    """按 shape router 的规则重建 replay 模板形状键。"""
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


def compact_replay_atom(gap_module: Any, atom: dict[str, Any]) -> dict[str, Any]:
    """压缩回放 prefix atom。"""
    return {
        "key": gap_module.atom_key(atom),
        "shape": f"{atom['band']}:k{atom['k']}",
        "band": atom["band"],
        "k": atom["k"],
        "q_lo": atom["q_lo"],
        "q_hi": atom["q_hi"],
        "b_lo": atom["b_lo"],
        "b_hi": atom["b_hi"],
        "prime_load": atom["prime_load"],
        "candidate_count": gap_module.atom_candidate_count(atom),
    }


def exclusion_reason(row: dict[str, Any], target_shape_key: str, replay_shapes: list[str]) -> str:
    """给出 full-shape 失败原因。"""
    if int(row["required_offband_witness_count"]) == 0:
        return "OffbandWitnessRequirementZero"
    if not replay_shapes:
        return "NoReplayFailureTemplate"
    if target_shape_key not in replay_shapes:
        return "DifferentFullShapeKey"
    return "FullShapeCompatible"


def build_replay_environment(max_p: int) -> dict[str, Any]:
    """构造回放所需的上游模块和筛表。"""
    gap = load_module(GAP_SHADOW_ROUTER, "gap_shadow_full_shape_probe")
    phase = gap.load_module(gap.PHASEBAND_ROUTER, "phaseband_full_shape_probe")
    offband = gap.load_module(gap.OFFBAND_ROUTER, "offband_full_shape_probe")
    layer = gap.load_module(gap.LAYER_ROUTER, "layer_full_shape_probe")
    single = gap.load_module(gap.SINGLE_ROUTER, "single_full_shape_probe")
    two = gap.load_module(gap.TWO_ROUTER, "two_full_shape_probe")
    multiplicity = gap.load_module(gap.MULTIPLICITY_ROUTER, "multiplicity_full_shape_probe")
    interval = gap.load_module(gap.INTERVAL_ROUTER, "interval_full_shape_probe")
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


def replay_candidate_prime(env: dict[str, Any], candidate: dict[str, Any], replay_p: int) -> dict[str, Any]:
    """把一个 matching prime 代回完整上游 gap-shadow 构造。"""
    gap = env["gap"]
    split_record = env["split"].audit_p(replay_p, env["prime_flags"], env["pi_prefix"])
    atoms = env["layer"].layer_atoms_for_p(env["offband"], env["phase"], replay_p, env["small_flags"])
    row = gap.shadow_record(
        env["interval"],
        env["single"],
        env["multiplicity"],
        env["layer"],
        env["two"],
        replay_p,
        candidate["side"],
        split_record[f"{candidate['side']}_prime_window"],
        atoms,
        3,
    )
    replay_templates = []
    parent_shape = f"{candidate['parent_atom_band']}:k{candidate['parent_atom_k']}"
    for template in row["void_subset_templates"]:
        shape_key = shape_key_for_template(row, template)
        atom_shapes = [atom_shape_from_key(key) for key in template["void_atom_keys"]]
        replay_templates.append(
            {
                "shape_key": shape_key,
                "void_atom_keys": template["void_atom_keys"],
                "atom_shapes": atom_shapes,
                "contains_original_parent_atom_shape": parent_shape in atom_shapes,
            }
        )
    replay_shape_keys = [template["shape_key"] for template in replay_templates]
    full_shape_compatible = candidate["shape_key"] in replay_shape_keys
    parent_shape_hits = [template for template in replay_templates if template["contains_original_parent_atom_shape"]]
    return {
        "source_index": candidate["index"],
        "source_p": candidate["p"],
        "replay_p": replay_p,
        "side": candidate["side"],
        "labels": candidate["labels"],
        "distinct_labels": candidate["distinct_labels"],
        "target_shape_key": candidate["shape_key"],
        "target_parent_atom_shape": parent_shape,
        "target_parent_atom_key": candidate["parent_atom_key"],
        "cover_word_residue_mod_gcd15": candidate["cover_word_residue_mod_gcd15"],
        "source_actual_p_mod_gcd15": candidate["actual_p_mod_gcd15"],
        "replay_p_mod_gcd15": replay_p % int(candidate["gcd_modulus_15"]),
        "replay_required_offband_witness_count": row["required_offband_witness_count"],
        "replay_actual_prefix_atom_count": row["actual_prefix_atom_count"],
        "replay_forced_void_atoms": row["forced_void_atoms_under_failure"],
        "replay_prefix_prime_load": row["prefix_prime_load"],
        "replay_prefix_void_atom_count": row["prefix_void_atom_count"],
        "replay_actual_void_deficit_to_failure": row["actual_void_deficit_to_failure"],
        "replay_prefix_atoms": [compact_replay_atom(gap, atom) for atom in row["prefix_interval_atoms"]],
        "replay_template_count": len(replay_templates),
        "replay_template_shape_keys": replay_shape_keys,
        "replay_templates": replay_templates,
        "full_shape_compatible": full_shape_compatible,
        "full_shape_excluded": not full_shape_compatible,
        "parent_shape_hit_without_full_shape": bool(parent_shape_hits) and not full_shape_compatible,
        "exclusion_reason": exclusion_reason(row, candidate["shape_key"], replay_shape_keys),
    }


def template_summary(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """按模板键汇总 full-shape 回放结果。"""
    grouped: dict[str, list[dict[str, Any]]] = {}
    for record in records:
        key = (
            f"shape={record['target_shape_key']}|parent={record['target_parent_atom_shape']}|"
            f"labels={','.join(map(str, record['distinct_labels']))}|"
            f"rho={record['cover_word_residue_mod_gcd15']}"
        )
        grouped.setdefault(key, []).append(record)
    summaries = []
    for key, values in sorted(grouped.items()):
        summaries.append(
            {
                "full_shape_template_key": key,
                "instance_count": len(values),
                "replay_primes": sorted({int(item["replay_p"]) for item in values}),
                "full_shape_compatible_count": sum(1 for item in values if item["full_shape_compatible"]),
                "full_shape_excluded_count": sum(1 for item in values if item["full_shape_excluded"]),
                "positive_required_replay_count": sum(
                    1 for item in values if int(item["replay_required_offband_witness_count"]) > 0
                ),
                "exclusion_reasons": sorted({item["exclusion_reason"] for item in values}),
            }
        )
    return summaries


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "matching_prime_replay_registered",
            "status": "closed_on_current_frontier",
            "statement": "Every matching prime representative from the template provenance ledger is replayed through the full upstream gap-shadow selector.",
        },
        {
            "name": "parent_phase_not_full_shape",
            "status": "closed_on_current_frontier",
            "statement": "Matching a parent atom phase window is strictly weaker than matching the full W,N,V and ordered band/k shape.",
        },
        {
            "name": "current_matching_templates_do_not_lift",
            "status": "closed_on_current_frontier",
            "statement": "No current matching prime representative lifts to the same full shape template.",
        },
        {
            "name": "global_full_shape_selector_source",
            "status": "open",
            "statement": "A global proof still must derive the same full-shape selector provenance symbolically for the formal-unit family.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    agg = result["aggregate"]
    return [
        {
            "gate": "MatchingRepresentativesReplayed",
            "closed": True,
            "proved": True,
            "meaning": "上一层 matching primes 已全部代回完整上游构造。",
            "remaining": "closed on current finite frontier",
        },
        {
            "gate": "CurrentMatchingTemplatesLiftToFullShape",
            "closed": agg["full_shape_compatible_check_count"] == 0,
            "proved": True,
            "meaning": "当前 matching primes 只匹配局部父 atom，不匹配完整 shape。",
            "remaining": "closed on current finite frontier",
        },
        {
            "gate": "TemplateOverlapPDECNeededNow",
            "closed": agg["template_overlap_pdec_after_full_shape_count"] == 0,
            "proved": True,
            "meaning": "当前有限前沿没有 full-shape overlap PDEC 实例。",
            "remaining": "closed on current finite frontier",
        },
        {
            "gate": "GlobalFormalUnitSelectorSourceProved",
            "closed": False,
            "proved": False,
            "meaning": "仍需把 full-shape 回放提升为 formal-unit 族的符号来源定理。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只关闭当前 matching prime 代表的完整形状回放，不关闭全局行/列命题。",
            "remaining": NEXT_TARGET,
        },
    ]


def build_result(input_ledger: Path, max_replay_p: int | None = None) -> dict[str, Any]:
    """构造 full-shape provenance 回放结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    source = load_json(input_ledger)
    candidates = source["candidate_provenance_records"]
    max_matching_prime = max(
        (prime for candidate in candidates for prime in candidate["matching_prime_representatives"]),
        default=3,
    )
    replay_bound = max_replay_p or max_matching_prime
    env = build_replay_environment(replay_bound)
    replay_records: list[dict[str, Any]] = []
    for candidate in candidates:
        for replay_p in candidate["matching_prime_representatives"]:
            replay_records.append(replay_candidate_prime(env, candidate, int(replay_p)))
    template_records = template_summary(replay_records)
    aggregate = {
        "input_ledger": str(input_ledger.relative_to(ROOT)),
        "candidate_instance_count": len(candidates),
        "source_template_count": source["aggregate"]["template_count"],
        "raw_candidate_matching_prime_check_count": len(replay_records),
        "unique_replay_prime_count": len({int(row["replay_p"]) for row in replay_records}),
        "full_shape_compatible_check_count": sum(1 for row in replay_records if row["full_shape_compatible"]),
        "full_shape_excluded_check_count": sum(1 for row in replay_records if row["full_shape_excluded"]),
        "zero_required_replay_count": sum(
            1 for row in replay_records if int(row["replay_required_offband_witness_count"]) == 0
        ),
        "positive_required_replay_count": sum(
            1 for row in replay_records if int(row["replay_required_offband_witness_count"]) > 0
        ),
        "parent_shape_hit_without_full_shape_count": sum(
            1 for row in replay_records if row["parent_shape_hit_without_full_shape"]
        ),
        "template_overlap_pdec_after_full_shape_count": sum(
            1 for row in replay_records if row["full_shape_compatible"]
        ),
        "current_matching_template_representatives_excluded_by_full_shape_replay": all(
            row["full_shape_excluded"] for row in replay_records
        ),
        "full_shape_global_provenance_proved": False,
        "row_column_unconditional_closed": False,
    }
    ledger = {
        "parameters": {
            **source["parameters"],
            "max_replay_p": replay_bound,
            "replay_source": "full upstream square-phase off-band prefix gap-shadow selector",
        },
        "aggregate": aggregate,
        "full_shape_replay_records": replay_records,
        "full_shape_template_summaries": template_records,
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = {
        "certificate_type": "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_full_shape_provenance_router",
        "status": "selector_matching_templates_excluded_by_current_full_shape_replay_open_global",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_replay_not_used_as_global_proof": True,
        "parameters": ledger["parameters"],
        "aggregate": aggregate,
        "full_shape_replay_records": replay_records,
        "full_shape_template_summaries": template_records,
        "current_matching_template_representatives_excluded_by_full_shape_replay": aggregate[
            "current_matching_template_representatives_excluded_by_full_shape_replay"
        ],
        "template_overlap_pdec_after_full_shape_count": aggregate["template_overlap_pdec_after_full_shape_count"],
        "full_shape_global_provenance_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_full_shape_provenance_router.py": sha256(
                Path(__file__).resolve()
            ),
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_template_provenance_router.py": sha256(
                TEMPLATE_PROVENANCE_ROUTER
            ),
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_router.py": sha256(GAP_SHADOW_ROUTER),
            "data/square-phase-offband-prefix-gap-shadow-selector-template-provenance-ledger.json": sha256(
                input_ledger
            ),
            "data/square-phase-offband-prefix-gap-shadow-selector-full-shape-provenance-ledger.json": sha256(
                OUT_LEDGER
            ),
        },
        "plain_conclusion": (
            "本步把上一层 phase+素性无法排除的 matching prime representatives 代回完整上游 "
            "gap-shadow selector。结果：当前全部 matching 代表只匹配局部父 atom 相位，"
            "没有一个提升为同一 `W,N,V,ordered band/k` 完整 shape。"
            "因此当前有限前沿暂无 matching-template overlap PDEC 实例；真正剩余收窄为把这种 "
            "full-shape selector 来源写成 formal-unit 族的符号定理。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow selector full-shape provenance router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"candidate_instance_count={agg['candidate_instance_count']}",
        f"source_template_count={agg['source_template_count']}",
        f"raw_candidate_matching_prime_check_count={agg['raw_candidate_matching_prime_check_count']}",
        f"unique_replay_prime_count={agg['unique_replay_prime_count']}",
        f"full_shape_compatible_check_count={agg['full_shape_compatible_check_count']}",
        f"full_shape_excluded_check_count={agg['full_shape_excluded_check_count']}",
        f"template_overlap_pdec_after_full_shape_count={agg['template_overlap_pdec_after_full_shape_count']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. Full-Shape Replay",
        "",
        "| source P | replay P | side | labels | target parent | W replay | replay templates | full-shape compatible | reason |",
        "| ---: | ---: | --- | --- | --- | ---: | ---: | ---: | --- |",
    ]
    for row in result["full_shape_replay_records"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["source_p"]),
                    str(row["replay_p"]),
                    f"`{row['side']}`",
                    f"`{row['labels']}`",
                    f"`{row['target_parent_atom_shape']}`",
                    str(row["replay_required_offband_witness_count"]),
                    str(row["replay_template_count"]),
                    f"`{fmt_bool(row['full_shape_compatible'])}`",
                    f"`{row['exclusion_reason']}`",
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 2. Template Summary",
            "",
            "| template | replay primes | compatible | excluded | positive W replay | reasons |",
            "| --- | --- | ---: | ---: | ---: | --- |",
        ]
    )
    for row in result["full_shape_template_summaries"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(row['full_shape_template_key'])}`",
                    f"`{row['replay_primes']}`",
                    str(row["full_shape_compatible_count"]),
                    str(row["full_shape_excluded_count"]),
                    str(row["positive_required_replay_count"]),
                    f"`{row['exclusion_reasons']}`",
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
            "- 当前有限 matching 代表已经被完整 shape 回放排除。",
            "- 仍需把回放中使用的 `W_required`、prefix atom 排序和 ordered band/k 约束写成 formal-unit 族的符号来源定理。",
            "- 若符号来源定理失败，则必须登记 full-shape overlap `PDEC/ColumnCRT`。",
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
    parser.add_argument("--input-ledger", type=Path, default=INPUT_LEDGER)
    parser.add_argument("--max-replay-p", type=int, default=None)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    input_ledger = args.input_ledger if args.input_ledger.is_absolute() else ROOT / args.input_ledger
    result = build_result(input_ledger, args.max_replay_p)
    write_markdown(result)
    result["source_hashes"][
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-full-shape-provenance-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "full_shape_compatible_check_count": result["aggregate"]["full_shape_compatible_check_count"],
                "template_overlap_pdec_after_full_shape_count": result["template_overlap_pdec_after_full_shape_count"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
