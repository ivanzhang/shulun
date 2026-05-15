#!/usr/bin/env python3
"""把前三 q 区间 prime-load 短缺压成多 atom prime-void gap shadow。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_router.py --max-p 5000 --prefix-atoms 3
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-router.md
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

PHASEBAND_ROUTER = ROOT / "experiments" / "prime_matrix_square_phase_halfgrid_noslot_phaseband_pdec_router.py"
OFFBAND_ROUTER = ROOT / "experiments" / "prime_matrix_square_phase_offband_witness_trichotomy_router.py"
LAYER_ROUTER = ROOT / "experiments" / "prime_matrix_square_phase_offband_layer_witness_router.py"
SINGLE_ROUTER = ROOT / "experiments" / "prime_matrix_square_phase_offband_single_atom_cover_router.py"
TWO_ROUTER = ROOT / "experiments" / "prime_matrix_square_phase_offband_two_atom_cover_router.py"
MULTIPLICITY_ROUTER = ROOT / "experiments" / "prime_matrix_square_phase_offband_atom_multiplicity_gate_router.py"
INTERVAL_ROUTER = ROOT / "experiments" / "prime_matrix_square_phase_offband_prefix_interval_formula_router.py"

OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-router.md"

MAIN_TARGET = "FirstThreeOffBandPrefixPrimeLoadOrExplicitQIntervalShortagePDEC"
NEXT_TARGET = "FirstPrefixMultiAtomPrimeVoidGapShadowPDECExclusion"


def load_module(path: Path, name: str) -> Any:
    """按路径加载前置路由器。"""
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def atom_key(atom: dict[str, Any]) -> str:
    """生成 atom 简短键。"""
    return f"{atom['band']}:k{atom['k']}:{atom['q_lo']}-{atom['q_hi']}"


def atom_candidate_count(atom: dict[str, Any]) -> int:
    """返回 q=P-2b 候选数，也就是 b 长度。"""
    return int(atom["b_length"])


def compact_atom(atom: dict[str, Any]) -> dict[str, Any]:
    """压缩 atom 为 gap shadow 使用的记录。"""
    return {
        "key": atom_key(atom),
        "band": atom["band"],
        "k": atom["k"],
        "b_lo": atom["b_lo"],
        "b_hi": atom["b_hi"],
        "b_length": atom["b_length"],
        "q_lo": atom["q_lo"],
        "q_hi": atom["q_hi"],
        "q_span": atom["q_span"],
        "prime_load": atom["prime_load"],
        "q_values": atom["q_values"][:12],
        "candidate_count": atom_candidate_count(atom),
    }


def void_subset_templates(atoms: list[dict[str, Any]], forced_void_atoms: int) -> list[dict[str, Any]]:
    """枚举 failure 必须包含的 prime-void atom 子集模板。"""
    if forced_void_atoms <= 0:
        return []
    templates: list[dict[str, Any]] = []
    for subset in itertools.combinations(atoms, forced_void_atoms):
        q_lo = min(int(atom["q_lo"]) for atom in subset)
        q_hi = max(int(atom["q_hi"]) for atom in subset)
        templates.append(
            {
                "void_atom_keys": [atom_key(atom) for atom in subset],
                "void_atom_count": forced_void_atoms,
                "combined_candidate_count": sum(atom_candidate_count(atom) for atom in subset),
                "max_single_atom_candidate_count": max(atom_candidate_count(atom) for atom in subset),
                "q_hull_lo": q_lo,
                "q_hull_hi": q_hi,
                "q_hull_span": q_hi - q_lo + 1,
            }
        )
    return templates


def shadow_record(
    interval: Any,
    single: Any,
    multiplicity: Any,
    layer: Any,
    two: Any,
    p: int,
    side: str,
    h_value: int,
    atoms: list[dict[str, Any]],
    prefix_atoms: int,
) -> dict[str, Any]:
    """生成单侧 gap shadow 记录。"""
    row = interval.interval_record(single, multiplicity, layer, two, p, side, h_value, atoms, prefix_atoms)
    prefix = row["prefix_interval_atoms"]
    actual_prefix_atom_count = len(prefix)
    required = int(row["required_offband_witness_count"])
    loaded_count = sum(1 for atom in prefix if atom["prime_load"] > 0)
    void_count = sum(1 for atom in prefix if atom["prime_load"] == 0)
    failure_max_loaded_atoms = max(0, required - 1)
    forced_void_atoms = max(0, actual_prefix_atom_count - failure_max_loaded_atoms) if required > 0 else 0
    actual_void_deficit_to_failure = forced_void_atoms - void_count if required > 0 else None
    failure_templates = void_subset_templates(prefix, forced_void_atoms)
    largest_forced_template_candidates = max(
        (template["combined_candidate_count"] for template in failure_templates),
        default=0,
    )
    smallest_forced_template_candidates = min(
        (template["combined_candidate_count"] for template in failure_templates),
        default=0,
    )
    return {
        "p": p,
        "side": side,
        "halfgrid_survivors": row["halfgrid_survivors"],
        "tail_prime_count": row["tail_prime_count"],
        "tail_deficit": row["tail_deficit"],
        "required_offband_witness_count": required,
        "prefix_atoms": prefix_atoms,
        "actual_prefix_atom_count": actual_prefix_atom_count,
        "prefix_prime_load": row["prefix_prime_load"],
        "prefix_top_two_prime_load": row["prefix_top_two_prime_load"],
        "prefix_loaded_atom_count": loaded_count,
        "prefix_void_atom_count": void_count,
        "failure_max_loaded_atoms": failure_max_loaded_atoms,
        "forced_void_atoms_under_failure": forced_void_atoms,
        "actual_void_deficit_to_failure": actual_void_deficit_to_failure,
        "prefix_prime_load_shortage_pdec": row["prefix_prime_load_shortage_pdec"],
        "multi_void_gap_shadow_active": required > 0 and void_count >= forced_void_atoms and row["prefix_prime_load"] < required,
        "tail_envelope_margin": row["tail_envelope_margin"],
        "exact_pressure_margin": row["exact_pressure_margin"],
        "support": row["support"],
        "prefix_interval_atoms": prefix,
        "void_subset_template_count": len(failure_templates),
        "smallest_forced_template_candidate_count": smallest_forced_template_candidates,
        "largest_forced_template_candidate_count": largest_forced_template_candidates,
        "void_subset_templates": failure_templates[:12],
    }


def compact_side(row: dict[str, Any]) -> dict[str, Any]:
    """压缩单侧记录。"""
    return {
        "p": row["p"],
        "side": row["side"],
        "required_offband_witness_count": row["required_offband_witness_count"],
        "actual_prefix_atom_count": row["actual_prefix_atom_count"],
        "prefix_prime_load": row["prefix_prime_load"],
        "prefix_loaded_atom_count": row["prefix_loaded_atom_count"],
        "prefix_void_atom_count": row["prefix_void_atom_count"],
        "forced_void_atoms_under_failure": row["forced_void_atoms_under_failure"],
        "actual_void_deficit_to_failure": row["actual_void_deficit_to_failure"],
        "support": row["support"],
        "smallest_forced_template_candidate_count": row["smallest_forced_template_candidate_count"],
        "largest_forced_template_candidate_count": row["largest_forced_template_candidate_count"],
        "prefix_interval_atoms": [compact_atom(atom) for atom in row["prefix_interval_atoms"]],
        "void_subset_templates": row["void_subset_templates"],
    }


def theorem_rows(prefix_atoms: int) -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "prefix_load_shortage_to_multivoid_shadow",
            "status": "closed",
            "statement": (
                f"For N<={prefix_atoms} available prefix atoms and W_required<=2, prefix prime-load < W_required "
                "forces at least N-W_required+1 available prefix atoms to be prime-void."
            ),
        },
        {
            "name": "explicit_void_subset_pdec_registration",
            "status": "closed",
            "statement": "Each failure registers a finite set of explicit q=P-2b atom intervals that must be prime-free.",
        },
        {
            "name": "finite_no_multivoid_gap_shadow",
            "status": "finite_evidence",
            "statement": "The finite audit finds no active multi-atom prime-void shadow up to the tested bound.",
        },
        {
            "name": "global_multivoid_gap_shadow_exclusion",
            "status": "open",
            "statement": "A global proof still needs to exclude simultaneous prime-void in the required explicit prefix atom subsets.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "PrimeLoadShortageToMultiVoidShadowClosed",
            "closed": True,
            "proved": True,
            "meaning": "前三 atom 若 prime-load 不足，必有多个前缀 atom 完全无素数。",
            "remaining": "closed",
        },
        {
            "gate": "ExplicitVoidSubsetRegistrationClosed",
            "closed": True,
            "proved": True,
            "meaning": "失败已登记为若干显式 q 区间同时 prime-void 的证书族。",
            "remaining": "closed",
        },
        {
            "gate": "FiniteNoMultiVoidGapShadowPDEC",
            "closed": result["multi_void_gap_shadow_active_count"] == 0,
            "proved": False,
            "meaning": "有限扫描中未出现真实前缀 prime-load 失败。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "GlobalMultiVoidGapShadowExcluded",
            "closed": False,
            "proved": False,
            "meaning": "仍需全局排斥多个固定二次相位 q 区间同时无素数。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只把短缺 PDEC 改写成多 prime-void gap shadow，不关闭全局行/列命题。",
            "remaining": NEXT_TARGET,
        },
    ]


def build_result(max_p: int, sample_ps: list[int], prefix_atoms: int) -> dict[str, Any]:
    """构造路由器结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    phase = load_module(PHASEBAND_ROUTER, "phaseband_router")
    offband = load_module(OFFBAND_ROUTER, "offband_router")
    layer = load_module(LAYER_ROUTER, "layer_router")
    single = load_module(SINGLE_ROUTER, "single_router")
    two = load_module(TWO_ROUTER, "two_router")
    multiplicity = load_module(MULTIPLICITY_ROUTER, "multiplicity_router")
    interval = load_module(INTERVAL_ROUTER, "interval_router")
    split = phase.load_split_router()
    prime_flags = split.sieve(max_p * max_p + max_p)
    pi_prefix = split.prime_prefix(prime_flags)
    small_flags = phase.sieve(max_p)
    primes = phase.primes_from_flags(small_flags, max_p)
    p_values = [p_value for p_value in primes if p_value >= 3]
    side_records: list[dict[str, Any]] = []
    for p_value in p_values:
        split_record = split.audit_p(p_value, prime_flags, pi_prefix)
        atoms = layer.layer_atoms_for_p(offband, phase, p_value, small_flags)
        for side in ("plus", "minus"):
            side_records.append(
                shadow_record(
                    interval,
                    single,
                    multiplicity,
                    layer,
                    two,
                    p_value,
                    side,
                    split_record[f"{side}_prime_window"],
                    atoms,
                    prefix_atoms,
                )
            )
    positive_required = [row for row in side_records if row["required_offband_witness_count"] > 0]
    active_shadows = [row for row in side_records if row["multi_void_gap_shadow_active"]]
    prime_load_shortages = [row for row in side_records if row["prefix_prime_load_shortage_pdec"]]
    sample_set = set(sample_ps)
    tight_frontier = sorted(
        positive_required,
        key=lambda row: (
            row["actual_void_deficit_to_failure"],
            row["prefix_prime_load"] - row["required_offband_witness_count"],
            row["p"],
            row["side"],
        ),
    )
    template_frontier = sorted(
        positive_required,
        key=lambda row: (
            row["smallest_forced_template_candidate_count"],
            row["support"]["support_depth_from_p"] or 0,
            row["p"],
            row["side"],
        ),
    )
    aggregate = {
        "side_record_count": len(side_records),
        "positive_required_count": len(positive_required),
        "prefix_atoms": prefix_atoms,
        "prefix_prime_load_shortage_pdec_count": len(prime_load_shortages),
        "multi_void_gap_shadow_active_count": len(active_shadows),
        "max_required_offband_witness_count": max((row["required_offband_witness_count"] for row in side_records), default=0),
        "min_actual_void_deficit_to_failure_positive_required": min(
            (row["actual_void_deficit_to_failure"] for row in positive_required),
            default=None,
        ),
        "max_actual_void_atom_count_positive_required": max(
            (row["prefix_void_atom_count"] for row in positive_required),
            default=0,
        ),
        "min_forced_void_atoms_positive_required": min(
            (row["forced_void_atoms_under_failure"] for row in positive_required),
            default=0,
        ),
        "max_forced_void_atoms_positive_required": max(
            (row["forced_void_atoms_under_failure"] for row in positive_required),
            default=0,
        ),
        "min_forced_template_candidate_count": min(
            (row["smallest_forced_template_candidate_count"] for row in positive_required),
            default=0,
        ),
        "max_forced_template_candidate_count": max(
            (row["largest_forced_template_candidate_count"] for row in positive_required),
            default=0,
        ),
    }
    ledger = {
        "parameters": {"max_p": max_p, "sample_ps": sample_ps, "prefix_atoms": prefix_atoms},
        "prime_count": len(p_values),
        "aggregate": aggregate,
        "positive_required_void_tight_frontier": [compact_side(row) for row in tight_frontier[:80]],
        "positive_required_template_frontier": [compact_side(row) for row in template_frontier[:80]],
        "multi_void_gap_shadow_active_records": [compact_side(row) for row in active_shadows[:40]],
        "prefix_prime_load_shortage_records": [compact_side(row) for row in prime_load_shortages[:40]],
        "sample_side_records": [compact_side(row) for row in side_records if row["p"] in sample_set],
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = {
        "certificate_type": "prime_matrix_square_phase_offband_prefix_gap_shadow_router",
        "status": "prefix_interval_shortage_reduced_to_multi_atom_prime_void_gap_shadow_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "empirical_absence_not_used_as_proof": True,
        "parameters": ledger["parameters"],
        "finite_prime_count": len(p_values),
        "aggregate": aggregate,
        "prefix_prime_load_shortage_pdec_count": len(prime_load_shortages),
        "multi_void_gap_shadow_active_count": len(active_shadows),
        "positive_required_void_tight_frontier": ledger["positive_required_void_tight_frontier"][:24],
        "positive_required_template_frontier": ledger["positive_required_template_frontier"][:24],
        "sample_side_records": ledger["sample_side_records"],
        "prefix_load_shortage_to_multivoid_shadow_closed": True,
        "explicit_void_subset_pdec_registration_closed": True,
        "finite_no_multivoid_gap_shadow_pdec": len(active_shadows) == 0,
        "global_multivoid_gap_shadow_excluded": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(prefix_atoms),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_router.py": sha256(
                Path(__file__).resolve()
            ),
            "experiments/prime_matrix_square_phase_offband_prefix_interval_formula_router.py": sha256(
                INTERVAL_ROUTER
            ),
            "experiments/prime_matrix_square_phase_offband_layer_witness_router.py": sha256(LAYER_ROUTER),
            "data/square-phase-offband-prefix-gap-shadow-ledger.json": sha256(OUT_LEDGER),
        },
        "plain_conclusion": (
            f"本步把 `{MAIN_TARGET}` 的 prime-load 短缺继续压缩："
            f"前三 prefix atoms 中若 `W_required<=2` 且 prime-load 小于 `W_required`，"
            "则 loaded atom 个数至多为 `W_required-1`，所以在实际可用的 `N<=3` 个前缀 atom 中，"
            "至少 `N-W_required+1` 个前缀 atom "
            "必须完全 prime-void。这样反例不再只是总量短缺，而是多个固定二次相位 q 区间同时无素数的 "
            "gap shadow。有限扫描中没有 active shadow；全局仍需排斥这个多区间 prime-void PDEC。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    prefix_atoms = result["parameters"]["prefix_atoms"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"max_p={result['parameters']['max_p']}",
        f"prefix_atoms={prefix_atoms}",
        f"finite_prime_count={result['finite_prime_count']}",
        f"prefix_prime_load_shortage_pdec_count={result['prefix_prime_load_shortage_pdec_count']}",
        f"multi_void_gap_shadow_active_count={result['multi_void_gap_shadow_active_count']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 多空 atom 影子",
        "",
        f"令实际可用的前三 prefix atoms 数量为 `N<={prefix_atoms}`。若 `W_required<=2` 且 prime-load 失败，则",
        "",
        "```text",
        "loaded_atom_count <= prime_load <= W_required-1",
        "void_atom_count >= N-(W_required-1).",
        "```",
        "",
        "因此当 `N=3` 时，`W_required=1` 要求三个前缀 atom 全空；`W_required=2` 要求至少两个前缀 atom 全空。",
        "",
        "## 2. 显式 PDEC 形态",
        "",
        "每个空 atom 都是上一层已经公式化的短区间：",
        "",
        "```text",
        "q=P-2b,  b_lo<=b<=b_hi",
        "k=floor(2b^2/(P-2b))",
        "band inequality fixed",
        "prime_count({q in this atom})=0",
        "```",
        "",
        "所以反例必须给出多个这样的短 q 区间同时 prime-void，而不是单个总量不等式失败。",
        "",
        "## 3. 有限审计摘要",
        "",
        "| metric | value |",
        "| --- | ---: |",
        f"| side records | {agg['side_record_count']} |",
        f"| positive required count | {agg['positive_required_count']} |",
        f"| prefix atoms | {agg['prefix_atoms']} |",
        f"| prefix prime-load shortage count | {agg['prefix_prime_load_shortage_pdec_count']} |",
        f"| active multi-void shadow count | {agg['multi_void_gap_shadow_active_count']} |",
        f"| max required witnesses | {agg['max_required_offband_witness_count']} |",
        f"| min actual void deficit to failure | {agg['min_actual_void_deficit_to_failure_positive_required']} |",
        f"| max actual void atom count | {agg['max_actual_void_atom_count_positive_required']} |",
        f"| forced void atoms range | {agg['min_forced_void_atoms_positive_required']}..{agg['max_forced_void_atoms_positive_required']} |",
        f"| forced template candidate count range | {agg['min_forced_template_candidate_count']}..{agg['max_forced_template_candidate_count']} |",
        "",
        "## 4. 最紧 void 边界",
        "",
        "| P | side | W_req | N | load | void actual | void forced if fail | deficit | atoms |",
        "| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for record in result["positive_required_void_tight_frontier"][:24]:
        atoms = ",".join(
            f"{atom['key']}#{atom['prime_load']}"
            for atom in record["prefix_interval_atoms"]
        )
        lines.append(
            "| "
            + " | ".join(
                [
                    str(record["p"]),
                    f"`{record['side']}`",
                    str(record["required_offband_witness_count"]),
                    str(record["actual_prefix_atom_count"]),
                    str(record["prefix_prime_load"]),
                    str(record["prefix_void_atom_count"]),
                    str(record["forced_void_atoms_under_failure"]),
                    str(record["actual_void_deficit_to_failure"]),
                    f"`{atoms}`",
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 5. 最小 failure 模板",
            "",
            "| P | side | W_req | N | forced void atoms | smallest candidates | templates |",
            "| ---: | --- | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for record in result["positive_required_template_frontier"][:16]:
        templates = "; ".join(
            "+".join(template["void_atom_keys"]) + f"({template['combined_candidate_count']})"
            for template in record["void_subset_templates"][:4]
        )
        lines.append(
            "| "
            + " | ".join(
                [
                    str(record["p"]),
                    f"`{record['side']}`",
                    str(record["required_offband_witness_count"]),
                    str(record["actual_prefix_atom_count"]),
                    str(record["forced_void_atoms_under_failure"]),
                    str(record["smallest_forced_template_candidate_count"]),
                    f"`{templates}`",
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 6. 命题行",
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
            "## 7. 决策表",
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
            "## 8. 下一步",
            "",
            "- 主攻：`FirstPrefixMultiAtomPrimeVoidGapShadowPDECExclusion`。",
            "- 需排斥多个固定二次相位前缀 atom 同时 prime-void。",
            "- 若不能自足排斥，则必须承认这里需要 sqrt 级短区间素数供给或同强度的新输入。",
            "- 当前仍未证明全局行/列无条件闭合。",
            "",
            "## 9. 依赖哈希",
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
    parser.add_argument("--max-p", type=int, default=5000)
    parser.add_argument("--prefix-atoms", type=int, default=3)
    parser.add_argument(
        "--sample-ps",
        type=str,
        default="23,37,43,47,73,113,313,523,673,683,691,733,1129,4999",
    )
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    sample_ps = [int(item) for item in args.sample_ps.split(",") if item.strip()]
    result = build_result(args.max_p, sample_ps, args.prefix_atoms)
    write_markdown(result)
    result["source_hashes"]["docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-router.md"] = sha256(
        OUT_MD
    )
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "max_p": args.max_p,
                "prefix_atoms": args.prefix_atoms,
                "prefix_prime_load_shortage_pdec_count": result["prefix_prime_load_shortage_pdec_count"],
                "multi_void_gap_shadow_active_count": result["multi_void_gap_shadow_active_count"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
