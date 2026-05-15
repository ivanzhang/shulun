#!/usr/bin/env python3
"""把前三 off-band atom 供给门压成显式 q 区间公式与短素数缺口。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_interval_formula_router.py --max-p 5000 --prefix-atoms 3
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-interval-formula-router.json

输出：
  data/square-phase-offband-prefix-interval-formula-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-interval-formula-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-interval-formula-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
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
PREFIX_ROUTER = ROOT / "experiments" / "prime_matrix_square_phase_offband_prefix_atom_supply_router.py"

OUT_LEDGER = DATA / "square-phase-offband-prefix-interval-formula-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-interval-formula-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-interval-formula-router.md"

MAIN_TARGET = "FirstThreeOffBandAtomLoadedMultiplicityOrPrefixVoidPDEC"
NEXT_TARGET = "FirstThreeOffBandPrefixPrimeLoadOrExplicitQIntervalShortagePDEC"


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


def base_value(p: int, b_value: int, k_value: int) -> int:
    """返回 base=2b^2-k(P-2b)。"""
    return 2 * b_value * b_value - k_value * (p - 2 * b_value)


def lower_cut(p: int, b_value: int) -> int:
    """返回 lower=q-h=(P-4b+1)/2。"""
    return (p - 4 * b_value + 1) // 2


def atom_band_slack(p: int, atom: dict[str, Any]) -> dict[str, Any]:
    """计算 atom 内三分不等式的最小松弛。"""
    half = (p - 1) // 2
    k_value = int(atom["k"])
    slacks: list[int] = []
    bases: list[int] = []
    lowers: list[int] = []
    for b_value in range(int(atom["b_lo"]), int(atom["b_hi"]) + 1):
        base = base_value(p, b_value, k_value)
        lower = lower_cut(p, b_value)
        bases.append(base)
        lowers.append(lower)
        if atom["band"] == "plus_only_noslot":
            slacks.append(lower - base)
        elif atom["band"] == "minus_only_noslot":
            slacks.append(base - half)
        else:
            slacks.append(min(base - lower, half - base))
    return {
        "base_min": min(bases, default=None),
        "base_max": max(bases, default=None),
        "lower_min": min(lowers, default=None),
        "lower_max": max(lowers, default=None),
        "band_min_slack": min(slacks, default=None),
    }


def atom_formula_statement(atom: dict[str, Any]) -> str:
    """给出该 atom 的符号化公式口径。"""
    band = atom["band"]
    if band == "plus_only_noslot":
        band_formula = "2b^2-k(P-2b)<(P-4b+1)/2"
    elif band == "minus_only_noslot":
        band_formula = "2b^2-k(P-2b)>(P-1)/2"
    else:
        band_formula = "(P-4b+1)/2<=2b^2-k(P-2b)<=(P-1)/2"
    return (
        f"q=P-2b, {atom['b_lo']}<=b<={atom['b_hi']}, "
        f"k={atom['k']}, k(P-2b)<=2b^2<(k+1)(P-2b), {band_formula}"
    )


def compact_interval_atom(p: int, atom: dict[str, Any]) -> dict[str, Any]:
    """压缩前缀 atom，并附上显式公式信息。"""
    slack = atom_band_slack(p, atom)
    return {
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
        "formula": atom_formula_statement(atom),
        "base_min": slack["base_min"],
        "base_max": slack["base_max"],
        "lower_min": slack["lower_min"],
        "lower_max": slack["lower_max"],
        "band_min_slack": slack["band_min_slack"],
    }


def verify_atom_formula(offband: Any, layer: Any, p: int, atom: dict[str, Any]) -> list[dict[str, Any]]:
    """逐 b 验证 layer 与 band 公式。"""
    failures: list[dict[str, Any]] = []
    for b_value in range(int(atom["b_lo"]), int(atom["b_hi"]) + 1):
        q_value = p - 2 * b_value
        got_k = layer.layer_k(p, b_value)
        got_band = offband.trichotomy_record(p, q_value)["band"]
        if got_k != atom["k"] or got_band != atom["band"]:
            failures.append(
                {
                    "p": p,
                    "b": b_value,
                    "q": q_value,
                    "atom_k": atom["k"],
                    "got_k": got_k,
                    "atom_band": atom["band"],
                    "got_band": got_band,
                }
            )
    return failures


def top_two_prime_load(atoms: list[dict[str, Any]]) -> int:
    """返回前缀内两个最大 atom 的 prime-load 和。"""
    loads = sorted((int(atom["prime_load"]) for atom in atoms), reverse=True)
    return sum(loads[:2])


def prefix_support_summary(p: int, atoms: list[dict[str, Any]]) -> dict[str, Any]:
    """汇总前三 atom 的 q 支撑范围。"""
    if not atoms:
        return {
            "q_lo": None,
            "q_hi": None,
            "support_depth_from_p": None,
            "support_span": 0,
            "candidate_count": 0,
            "depth_over_sqrt_p": None,
        }
    q_lo = min(int(atom["q_lo"]) for atom in atoms)
    q_hi = max(int(atom["q_hi"]) for atom in atoms)
    candidate_count = sum(int(atom["b_length"]) for atom in atoms)
    depth = p - q_lo
    return {
        "q_lo": q_lo,
        "q_hi": q_hi,
        "support_depth_from_p": depth,
        "support_span": q_hi - q_lo + 1,
        "candidate_count": candidate_count,
        "depth_over_sqrt_p": depth / math.sqrt(p),
    }


def interval_record(
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
    """生成单侧显式前缀区间记录。"""
    mult_row = multiplicity.multiplicity_record(single, layer, two, p, side, h_value, atoms)
    offband_atoms = single.offband_atoms_for_side(atoms, side)
    prefix = offband_atoms[:prefix_atoms]
    required = int(mult_row["required_offband_witness_count"])
    prefix_prime_load = sum(int(atom["prime_load"]) for atom in prefix)
    prefix_top_two_load = top_two_prime_load(prefix)
    loaded_count = sum(1 for atom in prefix if atom["prime_load"] > 0)
    support = prefix_support_summary(p, prefix)
    capacity_gate_closes = required <= 2 and prefix_top_two_load >= required
    return {
        "p": p,
        "side": side,
        "halfgrid_survivors": mult_row["halfgrid_survivors"],
        "tail_prime_count": mult_row["tail_prime_count"],
        "tail_deficit": 2 * mult_row["tail_prime_count"] - mult_row["halfgrid_survivors"],
        "required_offband_witness_count": required,
        "prefix_atoms": prefix_atoms,
        "prefix_prime_load": prefix_prime_load,
        "prefix_top_two_prime_load": prefix_top_two_load,
        "prefix_loaded_atom_count": loaded_count,
        "prefix_capacity_gate_closes": capacity_gate_closes,
        "required_gt_two_pdec": required > 2,
        "prefix_prime_load_shortage_pdec": required > 0 and prefix_prime_load < required,
        "prefix_top_two_load_shortage_pdec": required > 0 and prefix_top_two_load < required,
        "tail_envelope_margin": mult_row["tail_envelope_margin"],
        "exact_pressure_margin": mult_row["exact_pressure_margin"],
        "support": support,
        "prefix_interval_atoms": [compact_interval_atom(p, atom) for atom in prefix],
    }


def compact_side(row: dict[str, Any]) -> dict[str, Any]:
    """压缩单侧记录。"""
    return {
        "p": row["p"],
        "side": row["side"],
        "halfgrid_survivors": row["halfgrid_survivors"],
        "tail_prime_count": row["tail_prime_count"],
        "tail_deficit": row["tail_deficit"],
        "required_offband_witness_count": row["required_offband_witness_count"],
        "prefix_atoms": row["prefix_atoms"],
        "prefix_prime_load": row["prefix_prime_load"],
        "prefix_top_two_prime_load": row["prefix_top_two_prime_load"],
        "prefix_loaded_atom_count": row["prefix_loaded_atom_count"],
        "tail_envelope_margin": row["tail_envelope_margin"],
        "exact_pressure_margin": row["exact_pressure_margin"],
        "support": row["support"],
        "prefix_interval_atoms": row["prefix_interval_atoms"],
    }


def theorem_rows(prefix_atoms: int) -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "prefix_capacity_refinement_gate",
            "status": "closed",
            "statement": (
                f"If W_required<=2 and the first {prefix_atoms} off-band atoms have total prime-load "
                "at least W_required, then their top-two atom load reaches W_required."
            ),
        },
        {
            "name": "explicit_prefix_interval_formula",
            "status": "closed",
            "statement": (
                "Each prefix atom is an explicit interval q=P-2b with fixed k=floor(2b^2/(P-2b)) "
                "and one quadratic band inequality."
            ),
        },
        {
            "name": "prefix_interval_shortage_pdec_registration",
            "status": "closed",
            "statement": (
                "A prefix prime-load failure is exactly a shortage of primes in at most "
                f"{prefix_atoms} explicit early q-intervals."
            ),
        },
        {
            "name": "finite_no_prefix_interval_prime_shortage",
            "status": "finite_evidence",
            "statement": "The finite audit finds no such explicit interval shortage up to the tested bound.",
        },
        {
            "name": "global_first_prefix_interval_prime_supply",
            "status": "open",
            "statement": (
                "A global proof still needs enough primes in these first prefix q-intervals, "
                "or exclusion of the corresponding short-q interval shortage PDEC."
            ),
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "PrefixCapacityRefinementGateClosed",
            "closed": True,
            "proved": True,
            "meaning": "前三 atom 不必先证明 loaded atom 个数；总 prime-load 达标且 W_required<=2 就推出双 atom 容量达标。",
            "remaining": "closed",
        },
        {
            "gate": "ExplicitPrefixIntervalFormulaClosed",
            "closed": result["formula_identity_failure_count"] == 0,
            "proved": True,
            "meaning": "前三 off-band atom 已写成固定 k 与固定 band 的显式 q=P-2b 区间。",
            "remaining": "closed",
        },
        {
            "gate": "FiniteNoPrefixIntervalPrimeShortagePDEC",
            "closed": result["prefix_prime_load_shortage_pdec_count"] == 0,
            "proved": False,
            "meaning": "有限扫描中显式前三 q 区间总素数负载均达到阈值。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "GlobalPrefixIntervalPrimeSupplyClosed",
            "closed": False,
            "proved": False,
            "meaning": "仍需全局证明前三 q 区间素数供给，或排斥显式短区间缺口 PDEC。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只完成容量口径精炼和区间公式化，不关闭全局行/列命题。",
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
    split = phase.load_split_router()
    prime_flags = split.sieve(max_p * max_p + max_p)
    pi_prefix = split.prime_prefix(prime_flags)
    small_flags = phase.sieve(max_p)
    primes = phase.primes_from_flags(small_flags, max_p)
    p_values = [p_value for p_value in primes if p_value >= 3]
    side_records: list[dict[str, Any]] = []
    formula_failures: list[dict[str, Any]] = []
    for p_value in p_values:
        split_record = split.audit_p(p_value, prime_flags, pi_prefix)
        atoms = layer.layer_atoms_for_p(offband, phase, p_value, small_flags)
        for atom in atoms[: max(prefix_atoms + 8, 12)]:
            formula_failures.extend(verify_atom_formula(offband, layer, p_value, atom))
        for side in ("plus", "minus"):
            side_records.append(
                interval_record(
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
    required_gt_two = [row for row in side_records if row["required_gt_two_pdec"]]
    prime_load_shortages = [row for row in side_records if row["prefix_prime_load_shortage_pdec"]]
    top_two_shortages = [row for row in side_records if row["prefix_top_two_load_shortage_pdec"]]
    capacity_failures = [row for row in side_records if row["required_offband_witness_count"] > 0 and not row["prefix_capacity_gate_closes"]]
    sample_set = set(sample_ps)
    tight_frontier = sorted(
        positive_required,
        key=lambda row: (
            row["prefix_prime_load"] - row["required_offband_witness_count"],
            row["support"]["support_depth_from_p"] or 0,
            row["p"],
            row["side"],
        ),
    )
    depth_frontier = sorted(
        positive_required,
        key=lambda row: (
            row["support"]["support_depth_from_p"] or 0,
            row["prefix_prime_load"] - row["required_offband_witness_count"],
            row["p"],
            row["side"],
        ),
        reverse=True,
    )
    aggregate = {
        "side_record_count": len(side_records),
        "positive_required_count": len(positive_required),
        "prefix_atoms": prefix_atoms,
        "required_gt_two_pdec_count": len(required_gt_two),
        "prefix_prime_load_shortage_pdec_count": len(prime_load_shortages),
        "prefix_top_two_load_shortage_pdec_count": len(top_two_shortages),
        "prefix_capacity_failure_count": len(capacity_failures),
        "formula_identity_failure_count": len(formula_failures),
        "tail_envelope_defect_count": sum(1 for row in side_records if row["tail_envelope_margin"] <= 0),
        "max_required_offband_witness_count": max((row["required_offband_witness_count"] for row in side_records), default=0),
        "min_prefix_prime_load_surplus_positive_required": min(
            (row["prefix_prime_load"] - row["required_offband_witness_count"] for row in positive_required),
            default=None,
        ),
        "min_prefix_top_two_load_surplus_positive_required": min(
            (row["prefix_top_two_prime_load"] - row["required_offband_witness_count"] for row in positive_required),
            default=None,
        ),
        "max_prefix_support_depth_positive_required": max(
            (row["support"]["support_depth_from_p"] or 0 for row in positive_required),
            default=0,
        ),
        "max_prefix_support_depth_over_sqrt_p": max(
            (row["support"]["depth_over_sqrt_p"] or 0 for row in positive_required),
            default=0,
        ),
        "min_exact_pressure_margin": min((row["exact_pressure_margin"] for row in side_records), default=None),
    }
    ledger = {
        "parameters": {"max_p": max_p, "sample_ps": sample_ps, "prefix_atoms": prefix_atoms},
        "prime_count": len(p_values),
        "aggregate": aggregate,
        "positive_required_tight_frontier": [compact_side(row) for row in tight_frontier[:80]],
        "positive_required_depth_frontier": [compact_side(row) for row in depth_frontier[:80]],
        "formula_identity_failures": formula_failures[:40],
        "prefix_prime_load_shortage_records": [compact_side(row) for row in prime_load_shortages[:40]],
        "prefix_top_two_load_shortage_records": [compact_side(row) for row in top_two_shortages[:40]],
        "capacity_failure_records": [compact_side(row) for row in capacity_failures[:40]],
        "sample_side_records": [compact_side(row) for row in side_records if row["p"] in sample_set],
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = {
        "certificate_type": "prime_matrix_square_phase_offband_prefix_interval_formula_router",
        "status": "first_prefix_supply_reduced_to_explicit_q_interval_prime_shortage_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "empirical_absence_not_used_as_proof": True,
        "parameters": ledger["parameters"],
        "finite_prime_count": len(p_values),
        "aggregate": aggregate,
        "required_gt_two_pdec_count": len(required_gt_two),
        "prefix_prime_load_shortage_pdec_count": len(prime_load_shortages),
        "prefix_top_two_load_shortage_pdec_count": len(top_two_shortages),
        "prefix_capacity_failure_count": len(capacity_failures),
        "formula_identity_failure_count": len(formula_failures),
        "positive_required_tight_frontier": ledger["positive_required_tight_frontier"][:24],
        "positive_required_depth_frontier": ledger["positive_required_depth_frontier"][:24],
        "sample_side_records": ledger["sample_side_records"],
        "prefix_capacity_refinement_gate_closed": True,
        "explicit_prefix_interval_formula_closed": len(formula_failures) == 0,
        "finite_no_prefix_interval_prime_shortage_pdec": len(prime_load_shortages) == 0,
        "global_prefix_interval_prime_supply_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(prefix_atoms),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_offband_prefix_interval_formula_router.py": sha256(
                Path(__file__).resolve()
            ),
            "experiments/prime_matrix_square_phase_offband_prefix_atom_supply_router.py": sha256(PREFIX_ROUTER),
            "experiments/prime_matrix_square_phase_offband_atom_multiplicity_gate_router.py": sha256(
                MULTIPLICITY_ROUTER
            ),
            "experiments/prime_matrix_square_phase_offband_layer_witness_router.py": sha256(LAYER_ROUTER),
            "data/square-phase-offband-prefix-interval-formula-ledger.json": sha256(OUT_LEDGER),
        },
        "plain_conclusion": (
            "本步把前三 off-band atom 的 loaded 重数口径精炼为真正需要的容量口径："
            f"当 `W_required<=2` 时，前 {prefix_atoms} 个 atoms 的总 prime-load 达到 `W_required` "
            "就足以推出 top-two atom 负载达标。每个前缀 atom 又被写成显式 `q=P-2b` 区间、固定 "
            "`k=floor(2b^2/(P-2b))` 和一个二次 band 不等式。因此若前缀失败，反例必须表现为"
            f"最多 {prefix_atoms} 个早期 q 区间的素数供给短缺。有限扫描未发现该短缺；全局仍需证明"
            "这些短 q 区间必有足够素数，或排斥对应 PDEC。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    prefix_atoms = result["parameters"]["prefix_atoms"]
    lines = [
        "# Prime Matrix square-phase off-band prefix interval formula router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"max_p={result['parameters']['max_p']}",
        f"prefix_atoms={prefix_atoms}",
        f"finite_prime_count={result['finite_prime_count']}",
        f"formula_identity_failure_count={result['formula_identity_failure_count']}",
        f"required_gt_two_pdec_count={result['required_gt_two_pdec_count']}",
        f"prefix_prime_load_shortage_pdec_count={result['prefix_prime_load_shortage_pdec_count']}",
        f"prefix_top_two_load_shortage_pdec_count={result['prefix_top_two_load_shortage_pdec_count']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 容量口径精炼",
        "",
        "上一层的 loaded atom 个数是足够条件，但真正接入双 atom 门的是前缀 prime-load 容量。若",
        "",
        "```text",
        "W_required <= 2",
        "sum prime_load(first prefix atoms) >= W_required,",
        "```",
        "",
        "则两个最大前缀 atom 的 prime-load 之和也至少为 `W_required`，因此双 atom 容量门闭合。",
        "",
        "## 2. 显式区间公式",
        "",
        "尾素写成 `q=P-2b`。每个前缀 atom 由固定 `k` 与固定 band 给出：",
        "",
        "```text",
        "k(P-2b) <= 2b^2 < (k+1)(P-2b)",
        "base = 2b^2-k(P-2b)",
        "plus_only_noslot:  base < (P-4b+1)/2",
        "minus_only_noslot: base > (P-1)/2",
        "both_offband:      (P-4b+1)/2 <= base <= (P-1)/2",
        "```",
        "",
        "所以前缀失败不再是抽象 atom 失败，而是显式短 q 区间中的素数个数不足。",
        "",
        "## 3. 有限审计摘要",
        "",
        "| metric | value |",
        "| --- | ---: |",
        f"| side records | {agg['side_record_count']} |",
        f"| positive required count | {agg['positive_required_count']} |",
        f"| prefix atoms | {agg['prefix_atoms']} |",
        f"| formula identity failures | {agg['formula_identity_failure_count']} |",
        f"| required > 2 PDEC count | {agg['required_gt_two_pdec_count']} |",
        f"| prefix prime-load shortage count | {agg['prefix_prime_load_shortage_pdec_count']} |",
        f"| prefix top-two shortage count | {agg['prefix_top_two_load_shortage_pdec_count']} |",
        f"| prefix capacity failure count | {agg['prefix_capacity_failure_count']} |",
        f"| tail envelope defect count | {agg['tail_envelope_defect_count']} |",
        f"| max required witnesses | {agg['max_required_offband_witness_count']} |",
        f"| min prefix prime-load surplus | {agg['min_prefix_prime_load_surplus_positive_required']} |",
        f"| min prefix top-two surplus | {agg['min_prefix_top_two_load_surplus_positive_required']} |",
        f"| max prefix support depth | {agg['max_prefix_support_depth_positive_required']} |",
        f"| max depth/sqrt(P) | {agg['max_prefix_support_depth_over_sqrt_p']:.6f} |",
        f"| min exact pressure margin | {agg['min_exact_pressure_margin']} |",
        "",
        "## 4. 最紧区间供给边界",
        "",
        "| P | side | W_req | prefix load | top-two load | support q | depth | atoms |",
        "| ---: | --- | ---: | ---: | ---: | --- | ---: | --- |",
    ]
    for record in result["positive_required_tight_frontier"][:24]:
        atoms = ",".join(
            f"{atom['band']}:k{atom['k']}:{atom['q_lo']}-{atom['q_hi']}#{atom['prime_load']}"
            for atom in record["prefix_interval_atoms"]
        )
        support = record["support"]
        lines.append(
            "| "
            + " | ".join(
                [
                    str(record["p"]),
                    f"`{record['side']}`",
                    str(record["required_offband_witness_count"]),
                    str(record["prefix_prime_load"]),
                    str(record["prefix_top_two_prime_load"]),
                    f"`{support['q_lo']}-{support['q_hi']}`",
                    str(support["support_depth_from_p"]),
                    f"`{atoms}`",
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 5. 深度边界",
            "",
            "| P | side | W_req | prefix load | q support | depth | depth/sqrt(P) |",
            "| ---: | --- | ---: | ---: | --- | ---: | ---: |",
        ]
    )
    for record in result["positive_required_depth_frontier"][:16]:
        support = record["support"]
        lines.append(
            "| "
            + " | ".join(
                [
                    str(record["p"]),
                    f"`{record['side']}`",
                    str(record["required_offband_witness_count"]),
                    str(record["prefix_prime_load"]),
                    f"`{support['q_lo']}-{support['q_hi']}`",
                    str(support["support_depth_from_p"]),
                    f"{support['depth_over_sqrt_p']:.6f}",
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
            "- 主攻：`FirstThreeOffBandPrefixPrimeLoadOrExplicitQIntervalShortagePDEC`。",
            "- 需证明正阈值处前三个显式 q 区间的 prime-load 达到 `W_required`。",
            "- 若失败，反例必须给出最多三个靠近 P 的短 q 区间素数短缺证书。",
            "- 该输入本质上仍是短区间素数供给问题；当前未推出全局行/列无条件闭合。",
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
    result["source_hashes"][
        "docs/monograph/prime-matrix-square-phase-offband-prefix-interval-formula-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "max_p": args.max_p,
                "prefix_atoms": args.prefix_atoms,
                "formula_identity_failure_count": result["formula_identity_failure_count"],
                "required_gt_two_pdec_count": result["required_gt_two_pdec_count"],
                "prefix_prime_load_shortage_pdec_count": result["prefix_prime_load_shortage_pdec_count"],
                "prefix_top_two_load_shortage_pdec_count": result["prefix_top_two_load_shortage_pdec_count"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
