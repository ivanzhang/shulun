#!/usr/bin/env python3
"""把 off-band layer 见证下界压成单 atom 覆盖或分散覆盖 PDEC。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_single_atom_cover_router.py --max-p 5000
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-single-atom-cover-router.json

输出：
  data/square-phase-offband-single-atom-cover-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-single-atom-cover-router.json
  docs/monograph/prime-matrix-square-phase-offband-single-atom-cover-router.md
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

OUT_LEDGER = DATA / "square-phase-offband-single-atom-cover-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-single-atom-cover-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-single-atom-cover-router.md"

MAIN_TARGET = "OffBandLayerPrimeWitnessLowerBoundOrLayerVoidPDECExclusion"
NEXT_TARGET = "SingleOffBandLayerAtomPrimeLoadLowerBoundOrDistributedCoverPDECExclusion"


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


def offband_atoms_for_side(atoms: list[dict[str, Any]], side: str) -> list[dict[str, Any]]:
    """返回单侧 off-band atoms。"""
    if side == "plus":
        return [atom for atom in atoms if atom["plus_offband_atom"]]
    if side == "minus":
        return [atom for atom in atoms if atom["minus_offband_atom"]]
    raise ValueError(f"unknown side: {side}")


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


def minimal_cover(required: int, atoms: list[dict[str, Any]]) -> tuple[int | None, int, list[dict[str, Any]]]:
    """用最大 prime-load atoms 给出最小数量覆盖证书。"""
    if required <= 0:
        return 0, 0, []
    sorted_atoms = sorted(atoms, key=lambda atom: (atom["prime_load"], atom["b_length"], atom["q_hi"]), reverse=True)
    total = 0
    selected: list[dict[str, Any]] = []
    for atom in sorted_atoms:
        if atom["prime_load"] <= 0:
            break
        selected.append(atom)
        total += atom["prime_load"]
        if total >= required:
            return len(selected), total, selected
    return None, total, selected


def side_cover_record(layer: Any, p: int, side: str, h_value: int, atoms: list[dict[str, Any]]) -> dict[str, Any]:
    """生成单侧单 atom 覆盖记录。"""
    side_row = layer.side_from_atoms(p, side, h_value, atoms)
    offband_atoms = offband_atoms_for_side(atoms, side)
    max_atom = max(offband_atoms, key=lambda atom: (atom["prime_load"], atom["b_length"], atom["q_hi"]), default=None)
    max_load = int(max_atom["prime_load"]) if max_atom is not None else 0
    required = int(side_row["required_offband_witness_count"])
    cover_size, cover_load, selected = minimal_cover(required, offband_atoms)
    single_atom_covers = required <= 0 or max_load >= required
    distributed_cover_needed = required > 0 and not single_atom_covers and cover_size is not None
    single_atom_failure_pdec = required > 0 and not single_atom_covers
    return {
        "p": p,
        "side": side,
        "halfgrid_survivors": side_row["halfgrid_survivors"],
        "tail_prime_count": side_row["tail_prime_count"],
        "extreme_orientation_count": side_row["extreme_orientation_count"],
        "offband_witness_count": side_row["offband_witness_count"],
        "required_offband_witness_count": required,
        "witness_surplus": side_row["witness_surplus"],
        "tail_envelope_margin": side_row["tail_envelope_margin"],
        "exact_pressure_margin": side_row["exact_pressure_margin"],
        "offband_atom_count": side_row["offband_atom_count"],
        "loaded_offband_atom_count": side_row["loaded_offband_atom_count"],
        "max_single_atom_load": max_load,
        "single_atom_covers_required": single_atom_covers,
        "minimal_cover_size": cover_size,
        "minimal_cover_load": cover_load,
        "distributed_cover_needed": distributed_cover_needed,
        "single_atom_failure_pdec": single_atom_failure_pdec,
        "selected_cover_atoms": [compact_atom(atom) for atom in selected[:8]],
        "top_single_atom": compact_atom(max_atom) if max_atom is not None else None,
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
        "tail_envelope_margin": row["tail_envelope_margin"],
        "exact_pressure_margin": row["exact_pressure_margin"],
        "offband_atom_count": row["offband_atom_count"],
        "loaded_offband_atom_count": row["loaded_offband_atom_count"],
        "max_single_atom_load": row["max_single_atom_load"],
        "single_atom_covers_required": row["single_atom_covers_required"],
        "minimal_cover_size": row["minimal_cover_size"],
        "minimal_cover_load": row["minimal_cover_load"],
        "distributed_cover_needed": row["distributed_cover_needed"],
        "selected_cover_atoms": row["selected_cover_atoms"],
        "top_single_atom": row["top_single_atom"],
    }


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "single_atom_cover_sufficient_gate",
            "status": "closed",
            "statement": "If one off-band layer atom has prime load at least the required witness count, then the side closes immediately.",
        },
        {
            "name": "minimal_loaded_atom_cover_certificate",
            "status": "closed",
            "statement": "The required witness load can be certified by the smallest number of loaded off-band atoms sorted by prime load.",
        },
        {
            "name": "distributed_cover_pdec_registration",
            "status": "closed",
            "statement": "Failure of single-atom cover is registered as a distributed-cover PDEC requiring multiple off-band atoms.",
        },
        {
            "name": "finite_distributed_cover_profile",
            "status": "finite_counterexample_to_single_atom_only",
            "statement": "The finite audit finds the distributed-cover profile when a single off-band atom fails, but the minimal loaded-atom cover still exists.",
        },
        {
            "name": "global_single_atom_load_bound",
            "status": "open",
            "statement": "A global proof still needs one off-band layer atom with enough prime load, or exclusion of distributed-cover PDEC.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "SingleAtomCoverGateClosed",
            "closed": True,
            "proved": True,
            "meaning": "单个 off-band atom 的 prime load 达到阈值即可闭合单侧。",
            "remaining": "closed",
        },
        {
            "gate": "MinimalCoverCertificateClosed",
            "closed": result["minimal_cover_failure_count"] == 0,
            "proved": True,
            "meaning": "最小 loaded-atom 覆盖证书均可计算并与见证总量一致。",
            "remaining": "closed",
        },
        {
            "gate": "FiniteDistributedCoverProfileMaterialized",
            "closed": result["distributed_cover_pdec_count"] == 0,
            "proved": False,
            "meaning": "有限扫描出现单 atom 不足的分散覆盖形态；需继续压成双 atom 门。",
            "remaining": "finite distributed profile; next split",
        },
        {
            "gate": "GlobalSingleAtomLoadBoundClosed",
            "closed": False,
            "proved": False,
            "meaning": "仍需全局证明存在足够负载的单 off-band atom，或排斥分散覆盖 PDEC。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只把 layer-void 硬点压成单 atom 负载或分散覆盖 PDEC，不关闭全局行/列命题。",
            "remaining": NEXT_TARGET,
        },
    ]


def build_result(max_p: int, sample_ps: list[int]) -> dict[str, Any]:
    """构造路由器结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    phase = load_module(PHASEBAND_ROUTER, "phaseband_router")
    layer = load_module(LAYER_ROUTER, "layer_router")
    offband = load_module(OFFBAND_ROUTER, "offband_router")
    split = phase.load_split_router()
    prime_flags = split.sieve(max_p * max_p + max_p)
    pi_prefix = split.prime_prefix(prime_flags)
    small_flags = phase.sieve(max_p)
    primes = phase.primes_from_flags(small_flags, max_p)
    p_values = [p_value for p_value in primes if p_value >= 3]
    side_records: list[dict[str, Any]] = []
    cover_failures: list[dict[str, Any]] = []
    for p_value in p_values:
        split_record = split.audit_p(p_value, prime_flags, pi_prefix)
        atoms = layer.layer_atoms_for_p(offband, phase, p_value, small_flags)
        for side in ("plus", "minus"):
            row = side_cover_record(layer, p_value, side, split_record[f"{side}_prime_window"], atoms)
            if row["minimal_cover_size"] is None and row["offband_witness_count"] >= row["required_offband_witness_count"]:
                cover_failures.append(compact_side(row))
            side_records.append(row)
    positive_required = [row for row in side_records if row["required_offband_witness_count"] > 0]
    distributed_pdecs = [row for row in positive_required if row["distributed_cover_needed"]]
    single_failures = [row for row in positive_required if row["single_atom_failure_pdec"]]
    sample_set = set(sample_ps)
    witness_frontier = sorted(
        side_records,
        key=lambda row: (
            row["max_single_atom_load"] - row["required_offband_witness_count"],
            row["witness_surplus"],
            row["p"],
            row["side"],
        ),
    )
    positive_frontier = sorted(
        positive_required,
        key=lambda row: (
            row["max_single_atom_load"] - row["required_offband_witness_count"],
            row["witness_surplus"],
            row["p"],
            row["side"],
        ),
    )
    tail_frontier = sorted(
        [row for row in side_records if row["tail_envelope_margin"] <= 0],
        key=lambda row: (row["tail_envelope_margin"], row["max_single_atom_load"], row["p"], row["side"]),
    )
    aggregate = {
        "side_record_count": len(side_records),
        "positive_required_count": len(positive_required),
        "single_atom_cover_count": sum(1 for row in positive_required if row["single_atom_covers_required"]),
        "distributed_cover_pdec_count": len(distributed_pdecs),
        "single_atom_failure_count": len(single_failures),
        "minimal_cover_failure_count": len(cover_failures),
        "tail_envelope_defect_count": sum(1 for row in side_records if row["tail_envelope_margin"] <= 0),
        "max_required_offband_witness_count": max((row["required_offband_witness_count"] for row in side_records), default=0),
        "max_single_atom_load": max((row["max_single_atom_load"] for row in side_records), default=0),
        "max_minimal_cover_size": max((row["minimal_cover_size"] or 0 for row in positive_required), default=0),
        "min_single_atom_margin_positive_required": (
            min((row["max_single_atom_load"] - row["required_offband_witness_count"] for row in positive_required), default=None)
        ),
        "min_witness_surplus": min((row["witness_surplus"] for row in side_records), default=None),
        "min_exact_pressure_margin": min((row["exact_pressure_margin"] for row in side_records), default=None),
    }
    ledger = {
        "parameters": {"max_p": max_p, "sample_ps": sample_ps},
        "prime_count": len(p_values),
        "aggregate": aggregate,
        "witness_frontier": [compact_side(row) for row in witness_frontier[:80]],
        "positive_required_frontier": [compact_side(row) for row in positive_frontier[:80]],
        "tail_defect_frontier": [compact_side(row) for row in tail_frontier[:80]],
        "distributed_cover_pdec_records": [compact_side(row) for row in distributed_pdecs[:40]],
        "minimal_cover_failures": cover_failures[:40],
        "sample_side_records": [compact_side(row) for row in side_records if row["p"] in sample_set],
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = {
        "certificate_type": "prime_matrix_square_phase_offband_single_atom_cover_router",
        "status": "offband_layer_void_reduced_to_single_atom_prime_load_or_distributed_cover_pdec_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "empirical_absence_not_used_as_proof": True,
        "parameters": ledger["parameters"],
        "finite_prime_count": len(p_values),
        "aggregate": aggregate,
        "distributed_cover_pdec_count": len(distributed_pdecs),
        "single_atom_failure_count": len(single_failures),
        "minimal_cover_failure_count": len(cover_failures),
        "witness_frontier": ledger["witness_frontier"][:20],
        "positive_required_frontier": ledger["positive_required_frontier"][:20],
        "tail_defect_frontier": ledger["tail_defect_frontier"][:20],
        "sample_side_records": ledger["sample_side_records"],
        "single_atom_cover_gate_closed": True,
        "minimal_loaded_atom_cover_certificate_closed": len(cover_failures) == 0,
        "finite_no_distributed_cover_pdec": len(distributed_pdecs) == 0,
        "global_single_atom_load_bound_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_offband_single_atom_cover_router.py": sha256(
                Path(__file__).resolve()
            ),
            "experiments/prime_matrix_square_phase_offband_layer_witness_router.py": sha256(LAYER_ROUTER),
            "experiments/prime_matrix_square_phase_offband_witness_trichotomy_router.py": sha256(OFFBAND_ROUTER),
            "data/square-phase-offband-single-atom-cover-ledger.json": sha256(OUT_LEDGER),
        },
        "plain_conclusion": (
            "本步把 layer-void 见证硬点再压成单 atom 覆盖门。"
            "若某个 off-band layer atom 的 prime load 至少等于所需见证数，单侧立即闭合；"
            "否则即使总见证数足够，也必须由多个 loaded atoms 分散覆盖，登记为 DistributedCoverPDEC。"
            "有限扫描中存在一个单 atom 不足的分散覆盖点，但最小 loaded-atom 覆盖仍存在且大小为 2；"
            "全局仍需证明存在足够负载的单 atom，或把分散覆盖异常继续压成更小的多 atom 门。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase off-band single atom cover router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"max_p={result['parameters']['max_p']}",
        f"finite_prime_count={result['finite_prime_count']}",
        f"positive_required_count={agg['positive_required_count']}",
        f"distributed_cover_pdec_count={result['distributed_cover_pdec_count']}",
        f"single_atom_failure_count={result['single_atom_failure_count']}",
        f"minimal_cover_failure_count={result['minimal_cover_failure_count']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 单 Atom 覆盖门",
        "",
        "记单侧所需 off-band 见证数为 `W_required`。若存在一个 off-band layer atom 满足",
        "",
        "```text",
        "prime_load(atom) >= W_required,",
        "```",
        "",
        "则该侧的 off-band 见证门立即闭合。",
        "",
        "## 2. 分散覆盖 PDEC",
        "",
        "若总 off-band 见证数足够但没有任何单 atom 达到 `W_required`，则见证必须分散在多个 atoms 中。这被登记为 `DistributedCoverPDEC`；有限审计中该形态确实出现 1 次。",
        "",
        "## 3. 有限审计摘要",
        "",
        "| metric | value |",
        "| --- | ---: |",
        f"| side records | {agg['side_record_count']} |",
        f"| positive required count | {agg['positive_required_count']} |",
        f"| single atom cover count | {agg['single_atom_cover_count']} |",
        f"| distributed cover PDEC count | {agg['distributed_cover_pdec_count']} |",
        f"| single atom failure count | {agg['single_atom_failure_count']} |",
        f"| minimal cover failure count | {agg['minimal_cover_failure_count']} |",
        f"| tail envelope defect count | {agg['tail_envelope_defect_count']} |",
        f"| max required witnesses | {agg['max_required_offband_witness_count']} |",
        f"| max single atom load | {agg['max_single_atom_load']} |",
        f"| max minimal cover size | {agg['max_minimal_cover_size']} |",
        f"| min single atom margin on positive required | {agg['min_single_atom_margin_positive_required']} |",
        f"| min witness surplus | {agg['min_witness_surplus']} |",
        f"| min exact pressure margin | {agg['min_exact_pressure_margin']} |",
        "",
        "## 4. 正阈值最紧边界",
        "",
        "| P | side | H | T | W | W_req | max atom load | atom margin | cover size | cover load | top atom |",
        "| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for record in result["positive_required_frontier"][:24]:
        top = record["top_single_atom"]
        top_text = "" if top is None else f"{top['band']}:k{top['k']}:{top['q_lo']}-{top['q_hi']}#{top['prime_load']}"
        lines.append(
            "| "
            + " | ".join(
                [
                    str(record["p"]),
                    f"`{record['side']}`",
                    str(record["halfgrid_survivors"]),
                    str(record["tail_prime_count"]),
                    str(record["offband_witness_count"]),
                    str(record["required_offband_witness_count"]),
                    str(record["max_single_atom_load"]),
                    str(record["max_single_atom_load"] - record["required_offband_witness_count"]),
                    str(record["minimal_cover_size"]),
                    str(record["minimal_cover_load"]),
                    f"`{top_text}`",
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 5. 尾包络失败点",
            "",
            "| P | side | tail margin | W | W_req | max atom load | cover size | top atom |",
            "| ---: | --- | ---: | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for record in result["tail_defect_frontier"][:24]:
        top = record["top_single_atom"]
        top_text = "" if top is None else f"{top['band']}:k{top['k']}:{top['q_lo']}-{top['q_hi']}#{top['prime_load']}"
        lines.append(
            "| "
            + " | ".join(
                [
                    str(record["p"]),
                    f"`{record['side']}`",
                    str(record["tail_envelope_margin"]),
                    str(record["offband_witness_count"]),
                    str(record["required_offband_witness_count"]),
                    str(record["max_single_atom_load"]),
                    str(record["minimal_cover_size"]),
                    f"`{top_text}`",
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
            "- 主攻：`SingleOffBandLayerAtomPrimeLoadLowerBoundOrDistributedCoverPDECExclusion`。",
            "- 需证明至少一个 off-band layer atom 的 q 区间含有足够多素数。",
            "- 若单 atom 失败，则必须进入多 atom 分散覆盖 PDEC；有限唯一分散点由两个 atoms 覆盖。",
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
    result["source_hashes"]["docs/monograph/prime-matrix-square-phase-offband-single-atom-cover-router.md"] = sha256(
        OUT_MD
    )
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "max_p": args.max_p,
                "positive_required_count": result["aggregate"]["positive_required_count"],
                "distributed_cover_pdec_count": result["distributed_cover_pdec_count"],
                "single_atom_failure_count": result["single_atom_failure_count"],
                "minimal_cover_failure_count": result["minimal_cover_failure_count"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
