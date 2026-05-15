#!/usr/bin/env python3
"""把 off-band 尾素见证压成显式 layer atoms 与 layer-void PDEC。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_layer_witness_router.py --max-p 5000
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-layer-witness-router.json

输出：
  data/square-phase-offband-layer-witness-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-layer-witness-router.json
  docs/monograph/prime-matrix-square-phase-offband-layer-witness-router.md
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

PHASEBAND_ROUTER = ROOT / "experiments" / "prime_matrix_square_phase_halfgrid_noslot_phaseband_pdec_router.py"
OFFBAND_ROUTER = ROOT / "experiments" / "prime_matrix_square_phase_offband_witness_trichotomy_router.py"

OUT_LEDGER = DATA / "square-phase-offband-layer-witness-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-layer-witness-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-layer-witness-router.md"

MAIN_TARGET = "RequiredOffBandTailPrimeWitnessOrExtremeOrientationPDECExclusion"
NEXT_TARGET = "OffBandLayerPrimeWitnessLowerBoundOrLayerVoidPDECExclusion"


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


def layer_k(p: int, b_value: int) -> int:
    """返回 floor(2b^2/(P-2b))。"""
    return (2 * b_value * b_value) // (p - 2 * b_value)


def b_max_for_tail(phase: Any, p: int) -> int:
    """返回 q=P-2b>floor(4P/5) 的最大 b。"""
    return (p - phase.cutoff_alpha45(p) - 1) // 2


def atom_prime_values(p: int, b_lo: int, b_hi: int, prime_flags: bytearray) -> list[int]:
    """列出 atom 中的尾素 q=P-2b。"""
    return [p - 2 * b for b in range(b_lo, b_hi + 1) if prime_flags[p - 2 * b]]


def finalize_atom(p: int, atom: dict[str, Any], prime_flags: bytearray) -> dict[str, Any]:
    """补全 layer atom 的 q 区间和 prime load。"""
    b_lo = int(atom["b_lo"])
    b_hi = int(atom["b_hi"])
    q_hi = p - 2 * b_lo
    q_lo = p - 2 * b_hi
    q_values = atom_prime_values(p, b_lo, b_hi, prime_flags)
    band = str(atom["band"])
    return {
        "p": p,
        "band": band,
        "k": int(atom["k"]),
        "b_lo": b_lo,
        "b_hi": b_hi,
        "b_length": b_hi - b_lo + 1,
        "q_lo": q_lo,
        "q_hi": q_hi,
        "q_span": q_hi - q_lo + 1,
        "prime_load": len(q_values),
        "q_values": q_values[:12],
        "plus_extreme_atom": band == "plus_only_noslot",
        "minus_extreme_atom": band == "minus_only_noslot",
        "plus_offband_atom": band != "plus_only_noslot",
        "minus_offband_atom": band != "minus_only_noslot",
    }


def layer_atoms_for_p(offband: Any, phase: Any, p: int, prime_flags: bytearray) -> list[dict[str, Any]]:
    """按 (k, band) 把尾部 b 轴切成连续 layer atoms。"""
    max_b = b_max_for_tail(phase, p)
    atoms: list[dict[str, Any]] = []
    current: dict[str, Any] | None = None
    for b_value in range(1, max_b + 1):
        q_value = p - 2 * b_value
        band = offband.trichotomy_record(p, q_value)["band"]
        k_value = layer_k(p, b_value)
        if (
            current is None
            or current["band"] != band
            or current["k"] != k_value
            or b_value != current["b_hi"] + 1
        ):
            if current is not None:
                atoms.append(finalize_atom(p, current, prime_flags))
            current = {"band": band, "k": k_value, "b_lo": b_value, "b_hi": b_value}
        else:
            current["b_hi"] = b_value
    if current is not None:
        atoms.append(finalize_atom(p, current, prime_flags))
    return atoms


def side_from_atoms(p: int, side: str, h_value: int, atoms: list[dict[str, Any]]) -> dict[str, Any]:
    """从 layer atoms 汇总单侧见证门。"""
    tail_count = sum(atom["prime_load"] for atom in atoms)
    if side == "plus":
        extreme_atoms = [atom for atom in atoms if atom["plus_extreme_atom"]]
        offband_atoms = [atom for atom in atoms if atom["plus_offband_atom"]]
    elif side == "minus":
        extreme_atoms = [atom for atom in atoms if atom["minus_extreme_atom"]]
        offband_atoms = [atom for atom in atoms if atom["minus_offband_atom"]]
    else:
        raise ValueError(f"unknown side: {side}")
    extreme_count = sum(atom["prime_load"] for atom in extreme_atoms)
    offband_count = sum(atom["prime_load"] for atom in offband_atoms)
    signed_tail_deficit = 2 * tail_count - h_value
    required_witness_count = max(0, signed_tail_deficit // 2 + 1)
    witness_shortage = max(0, required_witness_count - offband_count)
    threshold = (h_value + 1) // 2
    atom_count = len(offband_atoms)
    loaded_atom_count = sum(1 for atom in offband_atoms if atom["prime_load"] > 0)
    top_atoms = sorted(offband_atoms, key=lambda atom: (atom["prime_load"], atom["b_length"], atom["q_hi"]), reverse=True)
    return {
        "p": p,
        "side": side,
        "halfgrid_survivors": h_value,
        "tail_prime_count": tail_count,
        "extreme_orientation_count": extreme_count,
        "offband_witness_count": offband_count,
        "required_offband_witness_count": required_witness_count,
        "witness_surplus": offband_count - required_witness_count,
        "witness_shortage": witness_shortage,
        "tail_envelope_margin": h_value - 2 * tail_count,
        "exact_pressure_margin": h_value - 2 * extreme_count,
        "pressure_threshold": threshold,
        "offband_atom_count": atom_count,
        "loaded_offband_atom_count": loaded_atom_count,
        "layer_void_pdec": witness_shortage > 0,
        "extreme_orientation_pressure_pdec": extreme_count >= threshold,
        "offband_layer_atoms": [compact_atom(atom) for atom in top_atoms[:8]],
    }


def compact_atom(atom: dict[str, Any]) -> dict[str, Any]:
    """压缩 layer atom。"""
    return {
        "band": atom["band"],
        "k": atom["k"],
        "b_lo": atom["b_lo"],
        "b_hi": atom["b_hi"],
        "b_length": atom["b_length"],
        "q_lo": atom["q_lo"],
        "q_hi": atom["q_hi"],
        "prime_load": atom["prime_load"],
        "q_values": atom["q_values"][:8],
    }


def compact_side(row: dict[str, Any]) -> dict[str, Any]:
    """压缩单侧记录。"""
    return {
        "p": row["p"],
        "side": row["side"],
        "halfgrid_survivors": row["halfgrid_survivors"],
        "tail_prime_count": row["tail_prime_count"],
        "extreme_orientation_count": row["extreme_orientation_count"],
        "offband_witness_count": row["offband_witness_count"],
        "required_offband_witness_count": row["required_offband_witness_count"],
        "witness_surplus": row["witness_surplus"],
        "witness_shortage": row["witness_shortage"],
        "tail_envelope_margin": row["tail_envelope_margin"],
        "exact_pressure_margin": row["exact_pressure_margin"],
        "pressure_threshold": row["pressure_threshold"],
        "offband_atom_count": row["offband_atom_count"],
        "loaded_offband_atom_count": row["loaded_offband_atom_count"],
        "offband_layer_atoms": row["offband_layer_atoms"],
    }


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "offband_layer_atom_partition",
            "status": "closed",
            "statement": "The tail b-axis is partitioned into contiguous atoms with fixed layer k and fixed signed phase band.",
        },
        {
            "name": "side_witness_count_from_layer_atoms",
            "status": "closed",
            "statement": "For each side, the off-band witness count is exactly the total prime load of the opposite-only plus middle layer atoms.",
        },
        {
            "name": "layer_void_pdec_registration",
            "status": "closed",
            "statement": "A witness shortage is equivalent to a registered layer-void PDEC over explicit q-interval atoms.",
        },
        {
            "name": "finite_no_layer_void_pdec",
            "status": "finite_evidence",
            "statement": "The finite audit finds no off-band layer witness shortage up to the tested bound.",
        },
        {
            "name": "global_offband_layer_prime_witness_lower_bound",
            "status": "open",
            "statement": "A global proof still needs to show enough primes in off-band layer atoms, or exclude the layer-void PDEC family.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "LayerAtomPartitionClosed",
            "closed": result["atom_partition_identity_failure_count"] == 0,
            "proved": True,
            "meaning": "尾部 b 轴已按固定 k 与三分 band 切成连续原子。",
            "remaining": "closed",
        },
        {
            "gate": "LayerWitnessIdentityClosed",
            "closed": result["layer_witness_identity_failure_count"] == 0,
            "proved": True,
            "meaning": "off-band 见证数等于对应 layer atoms 的 prime load。",
            "remaining": "closed",
        },
        {
            "gate": "FiniteNoLayerVoidPDEC",
            "closed": result["layer_void_pdec_count"] == 0,
            "proved": False,
            "meaning": "有限扫描没有 layer-void 见证短缺。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "GlobalOffBandLayerPrimeWitnessBoundClosed",
            "closed": False,
            "proved": False,
            "meaning": "仍需证明 off-band layer atoms 中有足够素数，或排斥显式 layer-void PDEC。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只把见证硬点压成 layer atoms 和 layer-void PDEC，不关闭全局行/列命题。",
            "remaining": NEXT_TARGET,
        },
    ]


def build_result(max_p: int, sample_ps: list[int]) -> dict[str, Any]:
    """构造路由器结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    phase = load_module(PHASEBAND_ROUTER, "phaseband_router")
    offband = load_module(OFFBAND_ROUTER, "offband_router")
    split = phase.load_split_router()
    prime_flags = split.sieve(max_p * max_p + max_p)
    pi_prefix = split.prime_prefix(prime_flags)
    small_flags = phase.sieve(max_p)
    primes = phase.primes_from_flags(small_flags, max_p)
    p_values = [p_value for p_value in primes if p_value >= 3]
    side_records: list[dict[str, Any]] = []
    atom_records: list[dict[str, Any]] = []
    partition_failures: list[dict[str, Any]] = []
    witness_identity_failures: list[dict[str, Any]] = []
    for p_value in p_values:
        split_record = split.audit_p(p_value, prime_flags, pi_prefix)
        atoms = layer_atoms_for_p(offband, phase, p_value, small_flags)
        atom_records.extend(atoms)
        tail_prime_count = sum(atom["prime_load"] for atom in atoms)
        expected_tail = len(offband.tail_primes_for_p(phase, p_value, primes))
        if tail_prime_count != expected_tail:
            partition_failures.append({"p": p_value, "tail_prime_count": tail_prime_count, "expected_tail": expected_tail})
        for side in ("plus", "minus"):
            h_value = split_record[f"{side}_prime_window"]
            side_row = side_from_atoms(p_value, side, h_value, atoms)
            direct_tail_records = [
                offband.trichotomy_record(p_value, q_value)
                for q_value in offband.tail_primes_for_p(phase, p_value, primes)
            ]
            direct_row = offband.side_record(p_value, side, h_value, direct_tail_records)
            if (
                side_row["tail_prime_count"] != direct_row["tail_prime_count"]
                or side_row["extreme_orientation_count"] != direct_row["extreme_orientation_count"]
                or side_row["offband_witness_count"] != direct_row["offband_witness_count"]
                or side_row["required_offband_witness_count"] != direct_row["required_offband_witness_count"]
            ):
                witness_identity_failures.append(
                    {
                        "p": p_value,
                        "side": side,
                        "from_atoms": compact_side(side_row),
                        "direct": {
                            "tail_prime_count": direct_row["tail_prime_count"],
                            "extreme_orientation_count": direct_row["extreme_orientation_count"],
                            "offband_witness_count": direct_row["offband_witness_count"],
                            "required_offband_witness_count": direct_row["required_offband_witness_count"],
                        },
                    }
                )
            side_records.append(side_row)
    layer_voids = [row for row in side_records if row["layer_void_pdec"]]
    pressure_pdecs = [row for row in side_records if row["extreme_orientation_pressure_pdec"]]
    sample_set = set(sample_ps)
    witness_frontier = sorted(side_records, key=lambda row: (row["witness_surplus"], row["exact_pressure_margin"], row["p"], row["side"]))
    tail_frontier = sorted(
        [row for row in side_records if row["tail_envelope_margin"] <= 0],
        key=lambda row: (row["tail_envelope_margin"], row["witness_surplus"], row["p"], row["side"]),
    )
    atom_load_frontier = sorted(atom_records, key=lambda atom: (atom["prime_load"], atom["b_length"], atom["p"]), reverse=True)
    aggregate = {
        "side_record_count": len(side_records),
        "atom_record_count": len(atom_records),
        "loaded_atom_count": sum(1 for atom in atom_records if atom["prime_load"] > 0),
        "combined_tail_prime_load": sum(atom["prime_load"] for atom in atom_records),
        "plus_extreme_atom_load": sum(atom["prime_load"] for atom in atom_records if atom["plus_extreme_atom"]),
        "minus_extreme_atom_load": sum(atom["prime_load"] for atom in atom_records if atom["minus_extreme_atom"]),
        "middle_atom_load": sum(atom["prime_load"] for atom in atom_records if atom["band"] == "both_offband_middle"),
        "atom_partition_identity_failure_count": len(partition_failures),
        "layer_witness_identity_failure_count": len(witness_identity_failures),
        "layer_void_pdec_count": len(layer_voids),
        "extreme_orientation_pressure_pdec_count": len(pressure_pdecs),
        "tail_envelope_defect_count": sum(1 for row in side_records if row["tail_envelope_margin"] <= 0),
        "max_offband_atom_count": max((row["offband_atom_count"] for row in side_records), default=0),
        "max_required_offband_witness_count": max((row["required_offband_witness_count"] for row in side_records), default=0),
        "min_witness_surplus": witness_frontier[0]["witness_surplus"] if witness_frontier else None,
        "min_exact_pressure_margin": min((row["exact_pressure_margin"] for row in side_records), default=None),
        "max_atom_prime_load": atom_load_frontier[0]["prime_load"] if atom_load_frontier else 0,
    }
    ledger = {
        "parameters": {"max_p": max_p, "sample_ps": sample_ps},
        "prime_count": len(p_values),
        "aggregate": aggregate,
        "witness_frontier": [compact_side(row) for row in witness_frontier[:80]],
        "tail_defect_frontier": [compact_side(row) for row in tail_frontier[:80]],
        "atom_load_frontier": [compact_atom(row) | {"p": row["p"]} for row in atom_load_frontier[:80]],
        "layer_void_records": [compact_side(row) for row in layer_voids[:40]],
        "pressure_pdec_records": [compact_side(row) for row in pressure_pdecs[:40]],
        "partition_failures": partition_failures[:20],
        "witness_identity_failures": witness_identity_failures[:20],
        "sample_side_records": [compact_side(row) for row in side_records if row["p"] in sample_set],
        "sample_atoms": [compact_atom(row) | {"p": row["p"]} for row in atom_records if row["p"] in sample_set][:120],
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = {
        "certificate_type": "prime_matrix_square_phase_offband_layer_witness_router",
        "status": "offband_witness_reduced_to_explicit_layer_atoms_and_layer_void_pdec_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "empirical_absence_not_used_as_proof": True,
        "parameters": ledger["parameters"],
        "finite_prime_count": len(p_values),
        "aggregate": aggregate,
        "atom_partition_identity_failure_count": len(partition_failures),
        "layer_witness_identity_failure_count": len(witness_identity_failures),
        "layer_void_pdec_count": len(layer_voids),
        "extreme_orientation_pressure_pdec_count": len(pressure_pdecs),
        "witness_frontier": ledger["witness_frontier"][:20],
        "tail_defect_frontier": ledger["tail_defect_frontier"][:20],
        "atom_load_frontier": ledger["atom_load_frontier"][:20],
        "sample_side_records": ledger["sample_side_records"],
        "offband_layer_atom_partition_closed": len(partition_failures) == 0,
        "side_witness_count_from_layer_atoms_closed": len(witness_identity_failures) == 0,
        "finite_no_layer_void_pdec": len(layer_voids) == 0,
        "global_offband_layer_prime_witness_lower_bound_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_offband_layer_witness_router.py": sha256(Path(__file__).resolve()),
            "experiments/prime_matrix_square_phase_offband_witness_trichotomy_router.py": sha256(OFFBAND_ROUTER),
            "experiments/prime_matrix_square_phase_halfgrid_noslot_phaseband_pdec_router.py": sha256(
                PHASEBAND_ROUTER
            ),
            "data/square-phase-offband-layer-witness-ledger.json": sha256(OUT_LEDGER),
        },
        "plain_conclusion": (
            "本步把 off-band 尾素见证进一步落到显式 layer atoms。"
            "尾部 b 轴按 `k=floor(2b^2/(P-2b))` 与三分 band 切成连续原子；"
            "每个原子对应一个明确的 q 区间 `[P-2b_hi, P-2b_lo]`，其 prime load 就是可用见证数或极端取向负载。"
            "因此见证短缺等价于这些 off-band q-区间原子的联合 prime load 小于所需阈值，"
            "即一个显式 layer-void PDEC。有限扫描未出现 layer-void；全局仍需证明 off-band layer atoms 中有足够素数，或排斥该 PDEC family。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase off-band layer witness router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"max_p={result['parameters']['max_p']}",
        f"finite_prime_count={result['finite_prime_count']}",
        f"atom_partition_identity_failure_count={result['atom_partition_identity_failure_count']}",
        f"layer_witness_identity_failure_count={result['layer_witness_identity_failure_count']}",
        f"layer_void_pdec_count={result['layer_void_pdec_count']}",
        f"extreme_orientation_pressure_pdec_count={result['extreme_orientation_pressure_pdec_count']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. Layer Atom 正规形",
        "",
        "尾素仍写成 `q=P-2b`。在尾窗 `q>floor(4P/5)` 内，按",
        "",
        "```text",
        "k = floor(2b^2/(P-2b))",
        "band in {plus_only_noslot, minus_only_noslot, both_offband_middle}",
        "```",
        "",
        "把连续 b 段合并成 atom。每个 atom 给出一个明确的 q 区间和其中的素数负载。",
        "",
        "## 2. 见证短缺的 PDEC 形态",
        "",
        "单侧所需见证仍为",
        "",
        "```text",
        "W_required = max(0, floor((2T-H)/2)+1).",
        "```",
        "",
        "见证短缺等价于所有 off-band atoms 的 prime load 总和小于 `W_required`。这就是当前登记的 layer-void PDEC。",
        "",
        "## 3. 有限审计摘要",
        "",
        "| metric | value |",
        "| --- | ---: |",
        f"| side records | {agg['side_record_count']} |",
        f"| atom records | {agg['atom_record_count']} |",
        f"| loaded atoms | {agg['loaded_atom_count']} |",
        f"| combined tail prime load | {agg['combined_tail_prime_load']} |",
        f"| plus extreme atom load | {agg['plus_extreme_atom_load']} |",
        f"| minus extreme atom load | {agg['minus_extreme_atom_load']} |",
        f"| middle atom load | {agg['middle_atom_load']} |",
        f"| atom partition identity failures | {agg['atom_partition_identity_failure_count']} |",
        f"| layer witness identity failures | {agg['layer_witness_identity_failure_count']} |",
        f"| layer-void PDEC count | {agg['layer_void_pdec_count']} |",
        f"| extreme orientation pressure PDEC count | {agg['extreme_orientation_pressure_pdec_count']} |",
        f"| tail envelope defect count | {agg['tail_envelope_defect_count']} |",
        f"| max offband atom count | {agg['max_offband_atom_count']} |",
        f"| max required witnesses | {agg['max_required_offband_witness_count']} |",
        f"| min witness surplus | {agg['min_witness_surplus']} |",
        f"| min exact pressure margin | {agg['min_exact_pressure_margin']} |",
        f"| max atom prime load | {agg['max_atom_prime_load']} |",
        "",
        "## 4. 最紧见证边界",
        "",
        "| P | side | H | T | extreme | W | W_req | surplus | offband atoms | loaded atoms | top atoms |",
        "| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for record in result["witness_frontier"][:18]:
        top_atoms = ",".join(
            f"{atom['band']}:k{atom['k']}:{atom['q_lo']}-{atom['q_hi']}#{atom['prime_load']}"
            for atom in record["offband_layer_atoms"][:4]
        )
        lines.append(
            "| "
            + " | ".join(
                [
                    str(record["p"]),
                    f"`{record['side']}`",
                    str(record["halfgrid_survivors"]),
                    str(record["tail_prime_count"]),
                    str(record["extreme_orientation_count"]),
                    str(record["offband_witness_count"]),
                    str(record["required_offband_witness_count"]),
                    str(record["witness_surplus"]),
                    str(record["offband_atom_count"]),
                    str(record["loaded_offband_atom_count"]),
                    f"`{top_atoms}`",
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 5. 尾包络失败点",
            "",
            "| P | side | H | T | extreme | W | W_req | surplus | tail margin | exact margin | top atoms |",
            "| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for record in result["tail_defect_frontier"][:24]:
        top_atoms = ",".join(
            f"{atom['band']}:k{atom['k']}:{atom['q_lo']}-{atom['q_hi']}#{atom['prime_load']}"
            for atom in record["offband_layer_atoms"][:4]
        )
        lines.append(
            "| "
            + " | ".join(
                [
                    str(record["p"]),
                    f"`{record['side']}`",
                    str(record["halfgrid_survivors"]),
                    str(record["tail_prime_count"]),
                    str(record["extreme_orientation_count"]),
                    str(record["offband_witness_count"]),
                    str(record["required_offband_witness_count"]),
                    str(record["witness_surplus"]),
                    str(record["tail_envelope_margin"]),
                    str(record["exact_pressure_margin"]),
                    f"`{top_atoms}`",
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
            "- 主攻：`OffBandLayerPrimeWitnessLowerBoundOrLayerVoidPDECExclusion`。",
            "- 需证明 off-band layer atoms 的 q 区间素数负载达到所需见证阈值。",
            "- 若失败，则反例必须表现为这些显式 q 区间的联合 prime void。",
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
    parser.add_argument(
        "--sample-ps",
        type=str,
        default="23,37,43,47,73,113,313,673,691,733,1129,4999",
    )
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    sample_ps = [int(item) for item in args.sample_ps.split(",") if item.strip()]
    result = build_result(args.max_p, sample_ps)
    write_markdown(result)
    result["source_hashes"]["docs/monograph/prime-matrix-square-phase-offband-layer-witness-router.md"] = sha256(
        OUT_MD
    )
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "max_p": args.max_p,
                "atom_partition_identity_failure_count": result["atom_partition_identity_failure_count"],
                "layer_witness_identity_failure_count": result["layer_witness_identity_failure_count"],
                "layer_void_pdec_count": result["layer_void_pdec_count"],
                "extreme_orientation_pressure_pdec_count": result["extreme_orientation_pressure_pdec_count"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
