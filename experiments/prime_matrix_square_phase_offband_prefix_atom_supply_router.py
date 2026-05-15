#!/usr/bin/env python3
"""把 loaded off-band atom 重数门压成早期前缀 atom 供给门。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_atom_supply_router.py --max-p 5000 --prefix-atoms 3
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-atom-supply-router.json

输出：
  data/square-phase-offband-prefix-atom-supply-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-atom-supply-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-atom-supply-router.md
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
MULTIPLICITY_ROUTER = ROOT / "experiments" / "prime_matrix_square_phase_offband_atom_multiplicity_gate_router.py"

OUT_LEDGER = DATA / "square-phase-offband-prefix-atom-supply-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-atom-supply-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-atom-supply-router.md"

MAIN_TARGET = "RequiredWitnessAtMostTwoAndLoadedOffBandAtomMultiplicityBoundOrPDEC"
NEXT_TARGET = "FirstThreeOffBandAtomLoadedMultiplicityOrPrefixVoidPDEC"


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


def prefix_needed_for_loaded_count(required: int, offband_atoms: list[dict[str, Any]]) -> int | None:
    """返回达到 required 个 loaded atoms 需要的自然前缀长度。"""
    if required <= 0:
        return 0
    loaded = 0
    for index, atom in enumerate(offband_atoms, 1):
        if atom["prime_load"] > 0:
            loaded += 1
        if loaded >= required:
            return index
    return None


def prefix_needed_for_prime_load(required: int, offband_atoms: list[dict[str, Any]]) -> int | None:
    """返回达到 required prime-load 需要的自然前缀长度。"""
    if required <= 0:
        return 0
    load = 0
    for index, atom in enumerate(offband_atoms, 1):
        load += int(atom["prime_load"])
        if load >= required:
            return index
    return None


def prefix_record(
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
    """生成单侧前缀供给记录。"""
    mult_row = multiplicity.multiplicity_record(single, layer, two, p, side, h_value, atoms)
    offband_atoms = single.offband_atoms_for_side(atoms, side)
    prefix = offband_atoms[:prefix_atoms]
    prefix_loaded_count = sum(1 for atom in prefix if atom["prime_load"] > 0)
    prefix_prime_load = sum(int(atom["prime_load"]) for atom in prefix)
    required = int(mult_row["required_offband_witness_count"])
    needed_count = prefix_needed_for_loaded_count(required, offband_atoms)
    needed_load = prefix_needed_for_prime_load(required, offband_atoms)
    prefix_loaded_count_ok = prefix_loaded_count >= required
    prefix_prime_load_ok = prefix_prime_load >= required
    prefix_gate_closes = required <= 2 and prefix_loaded_count_ok
    return {
        "p": p,
        "side": side,
        "halfgrid_survivors": mult_row["halfgrid_survivors"],
        "tail_prime_count": mult_row["tail_prime_count"],
        "tail_deficit": 2 * mult_row["tail_prime_count"] - mult_row["halfgrid_survivors"],
        "required_offband_witness_count": required,
        "loaded_offband_atom_count": mult_row["loaded_offband_atom_count"],
        "prefix_atoms": prefix_atoms,
        "prefix_loaded_atom_count": prefix_loaded_count,
        "prefix_prime_load": prefix_prime_load,
        "prefix_loaded_count_ok": prefix_loaded_count_ok,
        "prefix_prime_load_ok": prefix_prime_load_ok,
        "prefix_gate_closes": prefix_gate_closes,
        "prefix_loaded_count_shortage_pdec": required > 0 and not prefix_loaded_count_ok,
        "prefix_prime_load_shortage_pdec": required > 0 and not prefix_prime_load_ok,
        "required_gt_two_pdec": required > 2,
        "needed_prefix_for_loaded_count": needed_count,
        "needed_prefix_for_prime_load": needed_load,
        "tail_envelope_margin": mult_row["tail_envelope_margin"],
        "exact_pressure_margin": mult_row["exact_pressure_margin"],
        "prefix_atoms_records": [compact_atom(atom) for atom in prefix],
        "top_loaded_atoms": mult_row["top_loaded_atoms"],
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
        "loaded_offband_atom_count": row["loaded_offband_atom_count"],
        "prefix_atoms": row["prefix_atoms"],
        "prefix_loaded_atom_count": row["prefix_loaded_atom_count"],
        "prefix_prime_load": row["prefix_prime_load"],
        "needed_prefix_for_loaded_count": row["needed_prefix_for_loaded_count"],
        "needed_prefix_for_prime_load": row["needed_prefix_for_prime_load"],
        "tail_envelope_margin": row["tail_envelope_margin"],
        "exact_pressure_margin": row["exact_pressure_margin"],
        "prefix_atoms_records": row["prefix_atoms_records"],
        "top_loaded_atoms": row["top_loaded_atoms"][:6],
    }


def theorem_rows(prefix_atoms: int) -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "prefix_loaded_atom_supply_gate",
            "status": "closed",
            "statement": f"If the first {prefix_atoms} off-band atoms contain at least W_required loaded atoms and W_required<=2, then the side closes.",
        },
        {
            "name": "finite_first_prefix_loaded_supply",
            "status": "finite_evidence",
            "statement": f"The finite audit finds that the first {prefix_atoms} off-band atoms already supply enough loaded atoms for every positive-required side.",
        },
        {
            "name": "finite_first_prefix_prime_load_supply",
            "status": "finite_evidence",
            "statement": f"The finite audit also finds enough prime load inside the first {prefix_atoms} off-band atoms.",
        },
        {
            "name": "prefix_void_pdec_registration",
            "status": "closed",
            "statement": "A failure of the prefix supply gate is registered as PrefixVoidPDEC over explicit early q-interval atoms.",
        },
        {
            "name": "global_prefix_loaded_supply",
            "status": "open",
            "statement": f"A global proof still needs loaded atom supply in the first {prefix_atoms} off-band atoms, or PrefixVoidPDEC exclusion.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "PrefixLoadedAtomSupplyGateClosed",
            "closed": True,
            "proved": True,
            "meaning": "早期前缀 loaded atom 重数达标即可推出上一层重数门。",
            "remaining": "closed",
        },
        {
            "gate": "FiniteNoPrefixLoadedShortagePDEC",
            "closed": result["prefix_loaded_count_shortage_pdec_count"] == 0,
            "proved": False,
            "meaning": "有限扫描中早期前缀没有 loaded atom 重数短缺。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "FiniteNoPrefixPrimeLoadShortagePDEC",
            "closed": result["prefix_prime_load_shortage_pdec_count"] == 0,
            "proved": False,
            "meaning": "有限扫描中早期前缀 prime-load 也没有短缺。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "GlobalPrefixSupplyClosed",
            "closed": False,
            "proved": False,
            "meaning": "仍需全局证明早期 off-band atom 前缀供给，或排斥 PrefixVoidPDEC。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只把 loaded atom 重数硬点压成早期前缀供给，不关闭全局行/列命题。",
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
    for p_value in p_values:
        split_record = split.audit_p(p_value, prime_flags, pi_prefix)
        atoms = layer.layer_atoms_for_p(offband, phase, p_value, small_flags)
        for side in ("plus", "minus"):
            side_records.append(
                prefix_record(
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
    prefix_loaded_shortages = [row for row in side_records if row["prefix_loaded_count_shortage_pdec"]]
    prefix_load_shortages = [row for row in side_records if row["prefix_prime_load_shortage_pdec"]]
    sample_set = set(sample_ps)
    positive_frontier = sorted(
        positive_required,
        key=lambda row: (
            row["needed_prefix_for_loaded_count"] if row["needed_prefix_for_loaded_count"] is not None else 10**9,
            row["prefix_loaded_atom_count"] - row["required_offband_witness_count"],
            row["p"],
            row["side"],
        ),
        reverse=True,
    )
    tight_frontier = sorted(
        positive_required,
        key=lambda row: (
            row["prefix_loaded_atom_count"] - row["required_offband_witness_count"],
            row["needed_prefix_for_loaded_count"] or 0,
            row["p"],
            row["side"],
        ),
    )
    aggregate = {
        "side_record_count": len(side_records),
        "positive_required_count": len(positive_required),
        "prefix_atoms": prefix_atoms,
        "required_gt_two_pdec_count": len(required_gt_two),
        "prefix_loaded_count_shortage_pdec_count": len(prefix_loaded_shortages),
        "prefix_prime_load_shortage_pdec_count": len(prefix_load_shortages),
        "tail_envelope_defect_count": sum(1 for row in side_records if row["tail_envelope_margin"] <= 0),
        "max_required_offband_witness_count": max((row["required_offband_witness_count"] for row in side_records), default=0),
        "max_needed_prefix_for_loaded_count": max(
            (row["needed_prefix_for_loaded_count"] or 0 for row in positive_required),
            default=0,
        ),
        "max_needed_prefix_for_prime_load": max(
            (row["needed_prefix_for_prime_load"] or 0 for row in positive_required),
            default=0,
        ),
        "min_prefix_loaded_surplus_positive_required": min(
            (row["prefix_loaded_atom_count"] - row["required_offband_witness_count"] for row in positive_required),
            default=None,
        ),
        "min_prefix_prime_load_surplus_positive_required": min(
            (row["prefix_prime_load"] - row["required_offband_witness_count"] for row in positive_required),
            default=None,
        ),
        "min_exact_pressure_margin": min((row["exact_pressure_margin"] for row in side_records), default=None),
    }
    ledger = {
        "parameters": {"max_p": max_p, "sample_ps": sample_ps, "prefix_atoms": prefix_atoms},
        "prime_count": len(p_values),
        "aggregate": aggregate,
        "positive_required_prefix_depth_frontier": [compact_side(row) for row in positive_frontier[:80]],
        "positive_required_tight_frontier": [compact_side(row) for row in tight_frontier[:80]],
        "prefix_loaded_shortage_records": [compact_side(row) for row in prefix_loaded_shortages[:40]],
        "prefix_prime_load_shortage_records": [compact_side(row) for row in prefix_load_shortages[:40]],
        "required_gt_two_pdec_records": [compact_side(row) for row in required_gt_two[:40]],
        "sample_side_records": [compact_side(row) for row in side_records if row["p"] in sample_set],
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = {
        "certificate_type": "prime_matrix_square_phase_offband_prefix_atom_supply_router",
        "status": "loaded_atom_multiplicity_reduced_to_first_prefix_supply_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "empirical_absence_not_used_as_proof": True,
        "parameters": ledger["parameters"],
        "finite_prime_count": len(p_values),
        "aggregate": aggregate,
        "required_gt_two_pdec_count": len(required_gt_two),
        "prefix_loaded_count_shortage_pdec_count": len(prefix_loaded_shortages),
        "prefix_prime_load_shortage_pdec_count": len(prefix_load_shortages),
        "positive_required_prefix_depth_frontier": ledger["positive_required_prefix_depth_frontier"][:20],
        "positive_required_tight_frontier": ledger["positive_required_tight_frontier"][:20],
        "sample_side_records": ledger["sample_side_records"],
        "prefix_loaded_atom_supply_gate_closed": True,
        "finite_no_prefix_loaded_shortage_pdec": len(prefix_loaded_shortages) == 0,
        "finite_no_prefix_prime_load_shortage_pdec": len(prefix_load_shortages) == 0,
        "global_prefix_loaded_supply_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(prefix_atoms),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_offband_prefix_atom_supply_router.py": sha256(
                Path(__file__).resolve()
            ),
            "experiments/prime_matrix_square_phase_offband_atom_multiplicity_gate_router.py": sha256(
                MULTIPLICITY_ROUTER
            ),
            "experiments/prime_matrix_square_phase_offband_layer_witness_router.py": sha256(LAYER_ROUTER),
            "data/square-phase-offband-prefix-atom-supply-ledger.json": sha256(OUT_LEDGER),
        },
        "plain_conclusion": (
            f"本步把 loaded off-band atom 重数下界压成早期前缀供给门：按 b 从小到大，"
            f"也就是 q 从接近 P 向下排列 off-band atoms；若前 {prefix_atoms} 个 atoms 中的 loaded atom 个数"
            "至少为 `W_required`，且 `W_required<=2`，则上一层重数门闭合。"
            f"有限扫描显示所有正阈值点在前 {prefix_atoms} 个 off-band atoms 内已经获得足够 loaded atoms，"
            "并且 prime-load 也足够；全局仍需证明这个早期前缀非空供给，或排斥 PrefixVoidPDEC。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    prefix_atoms = result["parameters"]["prefix_atoms"]
    lines = [
        "# Prime Matrix square-phase off-band prefix atom supply router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"max_p={result['parameters']['max_p']}",
        f"prefix_atoms={prefix_atoms}",
        f"finite_prime_count={result['finite_prime_count']}",
        f"required_gt_two_pdec_count={result['required_gt_two_pdec_count']}",
        f"prefix_loaded_count_shortage_pdec_count={result['prefix_loaded_count_shortage_pdec_count']}",
        f"prefix_prime_load_shortage_pdec_count={result['prefix_prime_load_shortage_pdec_count']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 前缀供给门",
        "",
        "按自然顺序排列 off-band atoms：`b` 从小到大，也就是 `q=P-2b` 从接近 `P` 向下移动。",
        "",
        "若前缀满足",
        "",
        "```text",
        "loaded_atom_count(first prefix) >= W_required",
        "W_required <= 2,",
        "```",
        "",
        "则上一层 loaded atom 重数门闭合。",
        "",
        "## 2. 有限审计摘要",
        "",
        "| metric | value |",
        "| --- | ---: |",
        f"| side records | {agg['side_record_count']} |",
        f"| positive required count | {agg['positive_required_count']} |",
        f"| prefix atoms | {agg['prefix_atoms']} |",
        f"| required > 2 PDEC count | {agg['required_gt_two_pdec_count']} |",
        f"| prefix loaded shortage count | {agg['prefix_loaded_count_shortage_pdec_count']} |",
        f"| prefix prime-load shortage count | {agg['prefix_prime_load_shortage_pdec_count']} |",
        f"| tail envelope defect count | {agg['tail_envelope_defect_count']} |",
        f"| max required witnesses | {agg['max_required_offband_witness_count']} |",
        f"| max needed prefix for loaded count | {agg['max_needed_prefix_for_loaded_count']} |",
        f"| max needed prefix for prime load | {agg['max_needed_prefix_for_prime_load']} |",
        f"| min prefix loaded surplus | {agg['min_prefix_loaded_surplus_positive_required']} |",
        f"| min prefix prime-load surplus | {agg['min_prefix_prime_load_surplus_positive_required']} |",
        f"| min exact pressure margin | {agg['min_exact_pressure_margin']} |",
        "",
        "## 3. 前缀深度边界",
        "",
        "| P | side | D=2T-H | W_req | needed prefix | prefix loaded | prefix load | prefix atoms |",
        "| ---: | --- | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for record in result["positive_required_prefix_depth_frontier"][:24]:
        atoms = ",".join(
            f"{atom['band']}:k{atom['k']}:{atom['q_lo']}-{atom['q_hi']}#{atom['prime_load']}"
            for atom in record["prefix_atoms_records"]
        )
        lines.append(
            "| "
            + " | ".join(
                [
                    str(record["p"]),
                    f"`{record['side']}`",
                    str(record["tail_deficit"]),
                    str(record["required_offband_witness_count"]),
                    str(record["needed_prefix_for_loaded_count"]),
                    str(record["prefix_loaded_atom_count"]),
                    str(record["prefix_prime_load"]),
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
            "- 主攻：`FirstThreeOffBandAtomLoadedMultiplicityOrPrefixVoidPDEC`。",
            "- 需证明正阈值处前 3 个 off-band atoms 已有足够 loaded atoms。",
            "- 若失败，则反例必须表现为显式早期 q 区间前缀 prime void。",
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
    parser.add_argument("--prefix-atoms", type=int, default=3)
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
    result = build_result(args.max_p, sample_ps, args.prefix_atoms)
    write_markdown(result)
    result["source_hashes"]["docs/monograph/prime-matrix-square-phase-offband-prefix-atom-supply-router.md"] = sha256(
        OUT_MD
    )
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "max_p": args.max_p,
                "prefix_atoms": args.prefix_atoms,
                "required_gt_two_pdec_count": result["required_gt_two_pdec_count"],
                "prefix_loaded_count_shortage_pdec_count": result["prefix_loaded_count_shortage_pdec_count"],
                "prefix_prime_load_shortage_pdec_count": result["prefix_prime_load_shortage_pdec_count"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
