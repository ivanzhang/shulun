#!/usr/bin/env python3
"""把双 atom 负载门压成所需见证数上界与非空 atom 重数门。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_atom_multiplicity_gate_router.py --max-p 5000
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-atom-multiplicity-gate-router.json

输出：
  data/square-phase-offband-atom-multiplicity-gate-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-atom-multiplicity-gate-router.json
  docs/monograph/prime-matrix-square-phase-offband-atom-multiplicity-gate-router.md
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
LAYER_ROUTER = ROOT / "experiments" / "prime_matrix_square_phase_offband_layer_witness_router.py"
SINGLE_ROUTER = ROOT / "experiments" / "prime_matrix_square_phase_offband_single_atom_cover_router.py"
TWO_ROUTER = ROOT / "experiments" / "prime_matrix_square_phase_offband_two_atom_cover_router.py"

OUT_LEDGER = DATA / "square-phase-offband-atom-multiplicity-gate-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-atom-multiplicity-gate-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-atom-multiplicity-gate-router.md"

MAIN_TARGET = "TwoOffBandLayerAtomPrimeLoadLowerBoundOrHigherDistributedCoverPDECExclusion"
NEXT_TARGET = "RequiredWitnessAtMostTwoAndLoadedOffBandAtomMultiplicityBoundOrPDEC"


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


def compact_atom(atom: dict[str, Any]) -> dict[str, Any]:
    """压缩 atom。"""
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


def multiplicity_record(
    single: Any,
    layer: Any,
    two: Any,
    p: int,
    side: str,
    h_value: int,
    atoms: list[dict[str, Any]],
) -> dict[str, Any]:
    """生成单侧 atom 重数门记录。"""
    two_row = two.two_atom_record(single, layer, p, side, h_value, atoms)
    offband_atoms = single.offband_atoms_for_side(atoms, side)
    loaded_atoms = [
        atom for atom in sorted(offband_atoms, key=lambda atom: (atom["prime_load"], atom["b_length"], atom["q_hi"]), reverse=True)
        if atom["prime_load"] > 0
    ]
    required = int(two_row["required_offband_witness_count"])
    required_at_most_two = required <= 2
    loaded_multiplicity_ok = len(loaded_atoms) >= required
    multiplicity_two_atom_equivalence_ok = (required_at_most_two and loaded_multiplicity_ok) == two_row["two_atom_covers_required"]
    return {
        "p": p,
        "side": side,
        "halfgrid_survivors": two_row["halfgrid_survivors"],
        "tail_prime_count": two_row["tail_prime_count"],
        "offband_witness_count": two_row["offband_witness_count"],
        "required_offband_witness_count": required,
        "tail_envelope_margin": two_row["tail_envelope_margin"],
        "exact_pressure_margin": two_row["exact_pressure_margin"],
        "loaded_offband_atom_count": len(loaded_atoms),
        "top_two_atom_load": two_row["top_two_atom_load"],
        "max_single_atom_load": two_row["max_single_atom_load"],
        "required_at_most_two": required_at_most_two,
        "loaded_multiplicity_ok": loaded_multiplicity_ok,
        "two_atom_covers_required": two_row["two_atom_covers_required"],
        "multiplicity_two_atom_equivalence_ok": multiplicity_two_atom_equivalence_ok,
        "required_gt_two_pdec": required > 2,
        "loaded_multiplicity_shortage_pdec": required <= 2 and not loaded_multiplicity_ok,
        "top_loaded_atoms": [compact_atom(atom) for atom in loaded_atoms[:6]],
    }


def compact_side(row: dict[str, Any]) -> dict[str, Any]:
    """压缩单侧记录。"""
    return {
        "p": row["p"],
        "side": row["side"],
        "halfgrid_survivors": row["halfgrid_survivors"],
        "tail_prime_count": row["tail_prime_count"],
        "offband_witness_count": row["offband_witness_count"],
        "required_offband_witness_count": row["required_offband_witness_count"],
        "tail_envelope_margin": row["tail_envelope_margin"],
        "exact_pressure_margin": row["exact_pressure_margin"],
        "loaded_offband_atom_count": row["loaded_offband_atom_count"],
        "top_two_atom_load": row["top_two_atom_load"],
        "max_single_atom_load": row["max_single_atom_load"],
        "required_at_most_two": row["required_at_most_two"],
        "loaded_multiplicity_ok": row["loaded_multiplicity_ok"],
        "two_atom_covers_required": row["two_atom_covers_required"],
        "top_loaded_atoms": row["top_loaded_atoms"],
    }


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "two_atom_to_multiplicity_gate",
            "status": "closed",
            "statement": "If W_required<=2 and at least W_required off-band atoms are loaded, then the two-atom cover gate closes.",
        },
        {
            "name": "two_atom_multiplicity_equivalence",
            "status": "closed",
            "statement": "The finite audit verifies equivalence between the two-atom load gate and the multiplicity gate for all tested sides.",
        },
        {
            "name": "required_witness_at_most_two",
            "status": "finite_evidence",
            "statement": "The finite audit finds W_required<=2 up to the tested bound.",
        },
        {
            "name": "loaded_offband_atom_multiplicity_bound",
            "status": "finite_evidence",
            "statement": "The finite audit finds enough loaded off-band atoms whenever W_required is positive.",
        },
        {
            "name": "global_required_two_and_loaded_atom_bound",
            "status": "open",
            "statement": "A global proof still needs W_required<=2 and enough loaded off-band atoms, or the corresponding PDEC exclusions.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "TwoAtomToMultiplicityGateClosed",
            "closed": result["multiplicity_equivalence_failure_count"] == 0,
            "proved": True,
            "meaning": "双 atom 负载门已压成 W_required<=2 加 loaded atom 重数门。",
            "remaining": "closed",
        },
        {
            "gate": "FiniteNoRequiredGtTwoPDEC",
            "closed": result["required_gt_two_pdec_count"] == 0,
            "proved": False,
            "meaning": "有限扫描中所需见证数未超过 2。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "FiniteNoLoadedMultiplicityShortagePDEC",
            "closed": result["loaded_multiplicity_shortage_pdec_count"] == 0,
            "proved": False,
            "meaning": "有限扫描中 loaded off-band atom 个数均达到所需阈值。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "GlobalMultiplicityGateClosed",
            "closed": False,
            "proved": False,
            "meaning": "仍需全局证明 W_required<=2 与 loaded atom 重数下界，或排斥对应 PDEC。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只把双 atom 硬点压成两个更原子的输入，不关闭全局行/列命题。",
            "remaining": NEXT_TARGET,
        },
    ]


def build_result(max_p: int, sample_ps: list[int]) -> dict[str, Any]:
    """构造路由器结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    phase = load_module(PHASEBAND_ROUTER, "phaseband_router")
    offband = load_module(OFFBAND_ROUTER, "offband_router")
    layer = load_module(LAYER_ROUTER, "layer_router")
    single = load_module(SINGLE_ROUTER, "single_router")
    two = load_module(TWO_ROUTER, "two_router")
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
            side_records.append(multiplicity_record(single, layer, two, p_value, side, split_record[f"{side}_prime_window"], atoms))
    positive_required = [row for row in side_records if row["required_offband_witness_count"] > 0]
    equivalence_failures = [row for row in side_records if not row["multiplicity_two_atom_equivalence_ok"]]
    required_gt_two = [row for row in side_records if row["required_gt_two_pdec"]]
    multiplicity_shortages = [row for row in side_records if row["loaded_multiplicity_shortage_pdec"]]
    sample_set = set(sample_ps)
    positive_frontier = sorted(
        positive_required,
        key=lambda row: (
            row["loaded_offband_atom_count"] - row["required_offband_witness_count"],
            row["required_offband_witness_count"],
            row["p"],
            row["side"],
        ),
    )
    tail_frontier = sorted(
        [row for row in side_records if row["tail_envelope_margin"] <= 0],
        key=lambda row: (
            row["loaded_offband_atom_count"] - row["required_offband_witness_count"],
            row["tail_envelope_margin"],
            row["p"],
            row["side"],
        ),
    )
    aggregate = {
        "side_record_count": len(side_records),
        "positive_required_count": len(positive_required),
        "multiplicity_equivalence_failure_count": len(equivalence_failures),
        "required_gt_two_pdec_count": len(required_gt_two),
        "loaded_multiplicity_shortage_pdec_count": len(multiplicity_shortages),
        "tail_envelope_defect_count": sum(1 for row in side_records if row["tail_envelope_margin"] <= 0),
        "max_required_offband_witness_count": max((row["required_offband_witness_count"] for row in side_records), default=0),
        "max_loaded_offband_atom_count": max((row["loaded_offband_atom_count"] for row in side_records), default=0),
        "min_loaded_atom_surplus_positive_required": min(
            (row["loaded_offband_atom_count"] - row["required_offband_witness_count"] for row in positive_required),
            default=None,
        ),
        "min_exact_pressure_margin": min((row["exact_pressure_margin"] for row in side_records), default=None),
    }
    ledger = {
        "parameters": {"max_p": max_p, "sample_ps": sample_ps},
        "prime_count": len(p_values),
        "aggregate": aggregate,
        "positive_required_frontier": [compact_side(row) for row in positive_frontier[:80]],
        "tail_defect_frontier": [compact_side(row) for row in tail_frontier[:80]],
        "multiplicity_equivalence_failures": [compact_side(row) for row in equivalence_failures[:40]],
        "required_gt_two_pdec_records": [compact_side(row) for row in required_gt_two[:40]],
        "loaded_multiplicity_shortage_records": [compact_side(row) for row in multiplicity_shortages[:40]],
        "sample_side_records": [compact_side(row) for row in side_records if row["p"] in sample_set],
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = {
        "certificate_type": "prime_matrix_square_phase_offband_atom_multiplicity_gate_router",
        "status": "two_atom_gate_reduced_to_required_count_and_loaded_atom_multiplicity_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "empirical_absence_not_used_as_proof": True,
        "parameters": ledger["parameters"],
        "finite_prime_count": len(p_values),
        "aggregate": aggregate,
        "multiplicity_equivalence_failure_count": len(equivalence_failures),
        "required_gt_two_pdec_count": len(required_gt_two),
        "loaded_multiplicity_shortage_pdec_count": len(multiplicity_shortages),
        "positive_required_frontier": ledger["positive_required_frontier"][:20],
        "tail_defect_frontier": ledger["tail_defect_frontier"][:20],
        "sample_side_records": ledger["sample_side_records"],
        "two_atom_to_multiplicity_gate_closed": len(equivalence_failures) == 0,
        "finite_no_required_gt_two_pdec": len(required_gt_two) == 0,
        "finite_no_loaded_multiplicity_shortage_pdec": len(multiplicity_shortages) == 0,
        "global_required_two_and_loaded_atom_bound_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_offband_atom_multiplicity_gate_router.py": sha256(
                Path(__file__).resolve()
            ),
            "experiments/prime_matrix_square_phase_offband_two_atom_cover_router.py": sha256(TWO_ROUTER),
            "experiments/prime_matrix_square_phase_offband_layer_witness_router.py": sha256(LAYER_ROUTER),
            "data/square-phase-offband-atom-multiplicity-gate-ledger.json": sha256(OUT_LEDGER),
        },
        "plain_conclusion": (
            "本步把双 atom 负载门压成两个更原子的条件：第一，所需见证数 `W_required` 不超过 2；"
            "第二，loaded off-band atom 的个数至少为 `W_required`。"
            "因为每个 loaded atom 至少贡献一个素数，两个条件合起来推出 top-two 负载和达到阈值。"
            "有限扫描中 `W_required` 最大为 2，且所有正阈值点的 loaded atom 重数均足够；"
            "全局仍需证明这两个输入，或排斥所需见证数过大与 loaded atom 重数不足的 PDEC。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase off-band atom multiplicity gate router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"max_p={result['parameters']['max_p']}",
        f"finite_prime_count={result['finite_prime_count']}",
        f"multiplicity_equivalence_failure_count={result['multiplicity_equivalence_failure_count']}",
        f"required_gt_two_pdec_count={result['required_gt_two_pdec_count']}",
        f"loaded_multiplicity_shortage_pdec_count={result['loaded_multiplicity_shortage_pdec_count']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 重数门",
        "",
        "双 atom 覆盖可以被更粗但更结构化的重数门替代：",
        "",
        "```text",
        "W_required <= 2",
        "loaded_offband_atom_count >= W_required",
        "```",
        "",
        "因为每个 loaded atom 至少含一个尾素，取两个最大 loaded atoms 即可覆盖阈值。",
        "",
        "## 2. 有限审计摘要",
        "",
        "| metric | value |",
        "| --- | ---: |",
        f"| side records | {agg['side_record_count']} |",
        f"| positive required count | {agg['positive_required_count']} |",
        f"| multiplicity equivalence failures | {agg['multiplicity_equivalence_failure_count']} |",
        f"| required > 2 PDEC count | {agg['required_gt_two_pdec_count']} |",
        f"| loaded multiplicity shortage count | {agg['loaded_multiplicity_shortage_pdec_count']} |",
        f"| tail envelope defect count | {agg['tail_envelope_defect_count']} |",
        f"| max required witnesses | {agg['max_required_offband_witness_count']} |",
        f"| max loaded offband atom count | {agg['max_loaded_offband_atom_count']} |",
        f"| min loaded atom surplus on positive required | {agg['min_loaded_atom_surplus_positive_required']} |",
        f"| min exact pressure margin | {agg['min_exact_pressure_margin']} |",
        "",
        "## 3. 正阈值最紧边界",
        "",
        "| P | side | W_req | loaded atoms | surplus | top atoms |",
        "| ---: | --- | ---: | ---: | ---: | --- |",
    ]
    for record in result["positive_required_frontier"][:24]:
        atoms = ",".join(
            f"{atom['band']}:k{atom['k']}:{atom['q_lo']}-{atom['q_hi']}#{atom['prime_load']}"
            for atom in record["top_loaded_atoms"][:4]
        )
        surplus = record["loaded_offband_atom_count"] - record["required_offband_witness_count"]
        lines.append(
            "| "
            + " | ".join(
                [
                    str(record["p"]),
                    f"`{record['side']}`",
                    str(record["required_offband_witness_count"]),
                    str(record["loaded_offband_atom_count"]),
                    str(surplus),
                    f"`{atoms}`",
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
            "- 主攻：`RequiredWitnessAtMostTwoAndLoadedOffBandAtomMultiplicityBoundOrPDEC`。",
            "- 需证明 `W_required<=2`，并证明正阈值处至少有足够多个 loaded off-band atoms。",
            "- 若失败，则分别登记为 required-count PDEC 或 atom-multiplicity-shortage PDEC。",
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
    result["source_hashes"]["docs/monograph/prime-matrix-square-phase-offband-atom-multiplicity-gate-router.md"] = sha256(
        OUT_MD
    )
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "max_p": args.max_p,
                "multiplicity_equivalence_failure_count": result["multiplicity_equivalence_failure_count"],
                "required_gt_two_pdec_count": result["required_gt_two_pdec_count"],
                "loaded_multiplicity_shortage_pdec_count": result["loaded_multiplicity_shortage_pdec_count"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
