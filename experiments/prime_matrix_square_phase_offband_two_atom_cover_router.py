#!/usr/bin/env python3
"""把分散覆盖 PDEC 压成双 atom 覆盖门或更高阶分散 PDEC。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_two_atom_cover_router.py --max-p 5000
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-two-atom-cover-router.json

输出：
  data/square-phase-offband-two-atom-cover-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-two-atom-cover-router.json
  docs/monograph/prime-matrix-square-phase-offband-two-atom-cover-router.md
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

OUT_LEDGER = DATA / "square-phase-offband-two-atom-cover-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-two-atom-cover-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-two-atom-cover-router.md"

MAIN_TARGET = "SingleOffBandLayerAtomPrimeLoadLowerBoundOrDistributedCoverPDECExclusion"
NEXT_TARGET = "TwoOffBandLayerAtomPrimeLoadLowerBoundOrHigherDistributedCoverPDECExclusion"


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


def two_atom_record(single: Any, layer: Any, p: int, side: str, h_value: int, atoms: list[dict[str, Any]]) -> dict[str, Any]:
    """生成单侧双 atom 覆盖记录。"""
    row = single.side_cover_record(layer, p, side, h_value, atoms)
    offband_atoms = single.offband_atoms_for_side(atoms, side)
    sorted_atoms = sorted(offband_atoms, key=lambda atom: (atom["prime_load"], atom["b_length"], atom["q_hi"]), reverse=True)
    top_two = [atom for atom in sorted_atoms if atom["prime_load"] > 0][:2]
    top_two_load = sum(atom["prime_load"] for atom in top_two)
    required = int(row["required_offband_witness_count"])
    two_atom_covers = required <= 0 or top_two_load >= required
    higher_distributed_pdec = required > 0 and not two_atom_covers
    return {
        "p": p,
        "side": side,
        "halfgrid_survivors": row["halfgrid_survivors"],
        "tail_prime_count": row["tail_prime_count"],
        "offband_witness_count": row["offband_witness_count"],
        "required_offband_witness_count": required,
        "witness_surplus": row["witness_surplus"],
        "tail_envelope_margin": row["tail_envelope_margin"],
        "exact_pressure_margin": row["exact_pressure_margin"],
        "max_single_atom_load": row["max_single_atom_load"],
        "minimal_cover_size": row["minimal_cover_size"],
        "minimal_cover_load": row["minimal_cover_load"],
        "top_two_atom_load": top_two_load,
        "two_atom_covers_required": two_atom_covers,
        "higher_distributed_cover_pdec": higher_distributed_pdec,
        "top_two_atoms": [compact_atom(atom) for atom in top_two],
        "single_selected_cover_atoms": row["selected_cover_atoms"],
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
        "witness_surplus": row["witness_surplus"],
        "tail_envelope_margin": row["tail_envelope_margin"],
        "exact_pressure_margin": row["exact_pressure_margin"],
        "max_single_atom_load": row["max_single_atom_load"],
        "minimal_cover_size": row["minimal_cover_size"],
        "minimal_cover_load": row["minimal_cover_load"],
        "top_two_atom_load": row["top_two_atom_load"],
        "two_atom_covers_required": row["two_atom_covers_required"],
        "higher_distributed_cover_pdec": row["higher_distributed_cover_pdec"],
        "top_two_atoms": row["top_two_atoms"],
    }


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "two_atom_cover_sufficient_gate",
            "status": "closed",
            "statement": "If the two largest loaded off-band atoms have total prime load at least the required witness count, then the side closes.",
        },
        {
            "name": "distributed_cover_profile_absorbed_by_two_atoms",
            "status": "finite_evidence",
            "statement": "The finite distributed-cover profile is absorbed by two loaded off-band atoms.",
        },
        {
            "name": "higher_distributed_cover_pdec_registration",
            "status": "closed",
            "statement": "Failure of two-atom cover is registered as a higher-distributed-cover PDEC.",
        },
        {
            "name": "finite_no_higher_distributed_cover_pdec",
            "status": "finite_evidence",
            "statement": "The finite audit finds no positive-required side requiring more than two loaded off-band atoms.",
        },
        {
            "name": "global_two_atom_load_bound",
            "status": "open",
            "statement": "A global proof still needs two off-band layer atoms with enough prime load, or exclusion of higher distributed-cover PDEC.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "TwoAtomCoverGateClosed",
            "closed": True,
            "proved": True,
            "meaning": "两个最大 loaded off-band atoms 的负载和达到阈值即可闭合单侧。",
            "remaining": "closed",
        },
        {
            "gate": "FiniteNoHigherDistributedCoverPDEC",
            "closed": result["higher_distributed_cover_pdec_count"] == 0,
            "proved": False,
            "meaning": "有限扫描中没有需要超过两个 atoms 的正阈值点。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "GlobalTwoAtomLoadBoundClosed",
            "closed": False,
            "proved": False,
            "meaning": "仍需全局证明两个 off-band atoms 足够，或排斥更高阶分散覆盖 PDEC。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只把分散覆盖压成双 atom 门，不关闭全局行/列命题。",
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
            side_records.append(two_atom_record(single, layer, p_value, side, split_record[f"{side}_prime_window"], atoms))
    positive_required = [row for row in side_records if row["required_offband_witness_count"] > 0]
    higher_pdecs = [row for row in positive_required if row["higher_distributed_cover_pdec"]]
    distributed_single_failures = [
        row for row in positive_required if row["max_single_atom_load"] < row["required_offband_witness_count"]
    ]
    sample_set = set(sample_ps)
    positive_frontier = sorted(
        positive_required,
        key=lambda row: (
            row["top_two_atom_load"] - row["required_offband_witness_count"],
            row["max_single_atom_load"] - row["required_offband_witness_count"],
            row["p"],
            row["side"],
        ),
    )
    distributed_frontier = sorted(
        distributed_single_failures,
        key=lambda row: (row["top_two_atom_load"] - row["required_offband_witness_count"], row["p"], row["side"]),
    )
    aggregate = {
        "side_record_count": len(side_records),
        "positive_required_count": len(positive_required),
        "single_atom_failure_count": len(distributed_single_failures),
        "two_atom_cover_count": sum(1 for row in positive_required if row["two_atom_covers_required"]),
        "higher_distributed_cover_pdec_count": len(higher_pdecs),
        "tail_envelope_defect_count": sum(1 for row in side_records if row["tail_envelope_margin"] <= 0),
        "max_required_offband_witness_count": max((row["required_offband_witness_count"] for row in side_records), default=0),
        "max_top_two_atom_load": max((row["top_two_atom_load"] for row in side_records), default=0),
        "max_minimal_cover_size": max((row["minimal_cover_size"] or 0 for row in positive_required), default=0),
        "min_two_atom_margin_positive_required": min(
            (row["top_two_atom_load"] - row["required_offband_witness_count"] for row in positive_required),
            default=None,
        ),
        "min_exact_pressure_margin": min((row["exact_pressure_margin"] for row in side_records), default=None),
    }
    ledger = {
        "parameters": {"max_p": max_p, "sample_ps": sample_ps},
        "prime_count": len(p_values),
        "aggregate": aggregate,
        "positive_required_frontier": [compact_side(row) for row in positive_frontier[:80]],
        "distributed_single_failure_records": [compact_side(row) for row in distributed_frontier[:40]],
        "higher_distributed_cover_pdec_records": [compact_side(row) for row in higher_pdecs[:40]],
        "sample_side_records": [compact_side(row) for row in side_records if row["p"] in sample_set],
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = {
        "certificate_type": "prime_matrix_square_phase_offband_two_atom_cover_router",
        "status": "distributed_cover_reduced_to_two_atom_load_or_higher_distributed_pdec_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "empirical_absence_not_used_as_proof": True,
        "parameters": ledger["parameters"],
        "finite_prime_count": len(p_values),
        "aggregate": aggregate,
        "higher_distributed_cover_pdec_count": len(higher_pdecs),
        "single_atom_failure_count": len(distributed_single_failures),
        "positive_required_frontier": ledger["positive_required_frontier"][:20],
        "distributed_single_failure_records": ledger["distributed_single_failure_records"],
        "sample_side_records": ledger["sample_side_records"],
        "two_atom_cover_gate_closed": True,
        "finite_no_higher_distributed_cover_pdec": len(higher_pdecs) == 0,
        "global_two_atom_load_bound_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_offband_two_atom_cover_router.py": sha256(Path(__file__).resolve()),
            "experiments/prime_matrix_square_phase_offband_single_atom_cover_router.py": sha256(SINGLE_ROUTER),
            "experiments/prime_matrix_square_phase_offband_layer_witness_router.py": sha256(LAYER_ROUTER),
            "data/square-phase-offband-two-atom-cover-ledger.json": sha256(OUT_LEDGER),
        },
        "plain_conclusion": (
            "本步把上一层暴露的分散覆盖形态压成双 atom 覆盖门。"
            "若两个最大 loaded off-band atoms 的 prime load 之和达到所需见证数，单侧闭合；"
            "否则才登记为更高阶分散覆盖 PDEC。有限扫描中唯一单 atom 不足点 `P=733` plus "
            "由两个 load=1 的 off-band atoms 覆盖，因此没有更高阶分散覆盖 PDEC；"
            "全局仍需证明双 atom 负载下界，或排斥高阶分散异常。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase off-band two atom cover router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"max_p={result['parameters']['max_p']}",
        f"finite_prime_count={result['finite_prime_count']}",
        f"positive_required_count={agg['positive_required_count']}",
        f"single_atom_failure_count={result['single_atom_failure_count']}",
        f"higher_distributed_cover_pdec_count={result['higher_distributed_cover_pdec_count']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 双 Atom 覆盖门",
        "",
        "记两个最大 loaded off-band atoms 的负载和为 `L2`。若",
        "",
        "```text",
        "L2 >= W_required,",
        "```",
        "",
        "则单侧见证门闭合。只有 `L2<W_required` 时才进入更高阶分散覆盖 PDEC。",
        "",
        "## 2. 有限审计摘要",
        "",
        "| metric | value |",
        "| --- | ---: |",
        f"| side records | {agg['side_record_count']} |",
        f"| positive required count | {agg['positive_required_count']} |",
        f"| single atom failure count | {agg['single_atom_failure_count']} |",
        f"| two atom cover count | {agg['two_atom_cover_count']} |",
        f"| higher distributed cover PDEC count | {agg['higher_distributed_cover_pdec_count']} |",
        f"| tail envelope defect count | {agg['tail_envelope_defect_count']} |",
        f"| max required witnesses | {agg['max_required_offband_witness_count']} |",
        f"| max top-two atom load | {agg['max_top_two_atom_load']} |",
        f"| max minimal cover size | {agg['max_minimal_cover_size']} |",
        f"| min two atom margin on positive required | {agg['min_two_atom_margin_positive_required']} |",
        f"| min exact pressure margin | {agg['min_exact_pressure_margin']} |",
        "",
        "## 3. 正阈值最紧边界",
        "",
        "| P | side | W | W_req | max atom | top-two load | two margin | min cover | top atoms |",
        "| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for record in result["positive_required_frontier"][:24]:
        atoms = ",".join(
            f"{atom['band']}:k{atom['k']}:{atom['q_lo']}-{atom['q_hi']}#{atom['prime_load']}"
            for atom in record["top_two_atoms"]
        )
        lines.append(
            "| "
            + " | ".join(
                [
                    str(record["p"]),
                    f"`{record['side']}`",
                    str(record["offband_witness_count"]),
                    str(record["required_offband_witness_count"]),
                    str(record["max_single_atom_load"]),
                    str(record["top_two_atom_load"]),
                    str(record["top_two_atom_load"] - record["required_offband_witness_count"]),
                    str(record["minimal_cover_size"]),
                    f"`{atoms}`",
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 4. 单 Atom 不足点",
            "",
            "| P | side | W_req | top-two load | atoms |",
            "| ---: | --- | ---: | ---: | --- |",
        ]
    )
    for record in result["distributed_single_failure_records"]:
        atoms = ",".join(
            f"{atom['band']}:k{atom['k']}:{atom['q_lo']}-{atom['q_hi']}#{atom['prime_load']}"
            for atom in record["top_two_atoms"]
        )
        lines.append(
            "| "
            + " | ".join(
                [
                    str(record["p"]),
                    f"`{record['side']}`",
                    str(record["required_offband_witness_count"]),
                    str(record["top_two_atom_load"]),
                    f"`{atoms}`",
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 5. 命题行",
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
            "## 6. 决策表",
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
            "## 7. 下一步",
            "",
            "- 主攻：`TwoOffBandLayerAtomPrimeLoadLowerBoundOrHigherDistributedCoverPDECExclusion`。",
            "- 需证明两个 off-band layer atoms 的 q 区间素数负载和达到所需阈值。",
            "- 若失败，则进入更高阶分散覆盖 PDEC。",
            "- 当前仍未证明全局行/列无条件闭合。",
            "",
            "## 8. 依赖哈希",
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
    result["source_hashes"]["docs/monograph/prime-matrix-square-phase-offband-two-atom-cover-router.md"] = sha256(
        OUT_MD
    )
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "max_p": args.max_p,
                "positive_required_count": result["aggregate"]["positive_required_count"],
                "single_atom_failure_count": result["single_atom_failure_count"],
                "higher_distributed_cover_pdec_count": result["higher_distributed_cover_pdec_count"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
