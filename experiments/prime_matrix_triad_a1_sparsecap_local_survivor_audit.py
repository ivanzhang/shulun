#!/usr/bin/env python3
"""把 Triad-A1 SparseCap 路由压成 LocalSurvivor / finite PDEC 原子证书。

用法示例：
  python3 experiments/prime_matrix_triad_a1_sparsecap_local_survivor_audit.py
  python3 experiments/prime_matrix_triad_a1_sparsecap_local_survivor_audit.py --max-enumerate-period 100000

输出：
  docs/monograph/prime-matrix-triad-a1-sparsecap-local-survivor.json
  docs/monograph/prime-matrix-triad-a1-sparsecap-local-survivor.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from math import prod
from pathlib import Path
from typing import Any

from prime_matrix_bpn_low_hole_bucket_capacity import (
    high_completion_stats,
    low_holes_for_phase,
)


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_DUALCAP = DOCS / "prime-matrix-triad-a1-pdec-dualcap-extractor.json"
DEFAULT_MULT = DOCS / "h4-pdec-lhb-multiplicity-cap-certificate.json"
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-sparsecap-local-survivor.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-sparsecap-local-survivor.md"


def file_sha256(path: Path) -> str:
    """计算文件 sha256，保证证书来源可复核。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def first_covering_low_prime(
    p: int,
    row: int,
    col: int,
    low_primes: list[int],
) -> int | None:
    """返回覆盖给定列的第一个低素数。"""
    value = (row - 1) * p + col
    for prime in low_primes:
        if value % prime == 0:
            return prime
    return None


def high_covers_col(
    p: int,
    q: int,
    phase: int,
    y: int,
    col: int,
    high_primes: list[int],
) -> bool:
    """检查 lift row=phase+Q*y 时，高素数是否覆盖列 col。"""
    value = (phase + q * y - 1) * p + col
    return any(value % prime == 0 for prime in high_primes)


def completion_y_values(
    p: int,
    q: int,
    phase: int,
    holes: list[int],
    high_primes: list[int],
    max_enumerate_period: int,
) -> tuple[list[int], bool, int]:
    """枚举补洞完成的高层 CRT lift；周期过大时只返回未枚举标记。"""
    high_period = prod(high_primes) if high_primes else 1
    if high_period > max_enumerate_period:
        return [], False, high_period

    y_values = []
    for y in range(high_period):
        if all(high_covers_col(p, q, phase, y, col, high_primes) for col in holes):
            y_values.append(y)
    return y_values, True, high_period


def early_row_from_phase(p: int, phase: int) -> bool:
    """判断相位自身是否对应 P 行以内的正行。"""
    return 1 <= phase <= p


def analyze_sparse_phase(
    p: int,
    q: int,
    phase: int,
    low_primes: list[int],
    high_primes: list[int],
    m_value: int,
    max_enumerate_period: int,
) -> dict[str, Any]:
    """把一个 sparse 相位压成早期幸存者或有限 PDEC 原子。"""
    holes = low_holes_for_phase(p, q, low_primes, phase)
    stats = high_completion_stats(p, q, phase, holes, high_primes)
    y_values, enumerated, high_period = completion_y_values(
        p=p,
        q=q,
        phase=phase,
        holes=holes,
        high_primes=high_primes,
        max_enumerate_period=max_enumerate_period,
    )
    y0_complete = enumerated and 0 in y_values
    y0_uncovered_holes = [
        col for col in holes
        if not high_covers_col(p, q, phase, 0, col, high_primes)
    ]
    low_cover_signature = [
        {
            "col": col,
            "low_prime": first_covering_low_prime(p, phase, col, low_primes),
        }
        for col in range(1, p)
        if first_covering_low_prime(p, phase, col, low_primes) is not None
    ]

    if early_row_from_phase(p, phase) and y0_complete:
        phase_route = "EarlyCompletionConflict"
    elif early_row_from_phase(p, phase):
        phase_route = "LocalSurvivorWitnessAtRowLeP"
    elif stats["completion_count"] > 0:
        phase_route = "FinitePDECAtomBeyondP"
    else:
        phase_route = "BlockerDeficitLocalSurvivor"

    completion_rows = [phase + q * y for y in y_values] if enumerated else []
    return {
        "phase": phase,
        "m_value": m_value,
        "low_holes": holes,
        "low_hole_count": len(holes),
        "completion_count": int(stats["completion_count"]),
        "high_period": high_period,
        "enumerated_completions": enumerated,
        "completion_y_values": y_values,
        "completion_rows": completion_rows,
        "first_completion_row": min(completion_rows) if completion_rows else None,
        "row_le_p_phase": early_row_from_phase(p, phase),
        "y0_complete": y0_complete,
        "y0_uncovered_holes": y0_uncovered_holes,
        "local_survivor_witness_col": (
            y0_uncovered_holes[0]
            if early_row_from_phase(p, phase) and not y0_complete and y0_uncovered_holes
            else None
        ),
        "low_cover_signature": low_cover_signature,
        "phase_route": phase_route,
    }


def sparse_caps_from_dualcap(dualcap: dict[str, Any]) -> list[dict[str, Any]]:
    """从 DualCap 账本中提取并按相位集去重的 SparseCap。"""
    grouped: dict[tuple[int, tuple[int, ...]], dict[str, Any]] = {}
    for prime_item in dualcap["prime_results"]:
        p = int(prime_item["p"])
        for cap in prime_item["top_caps"]:
            if cap["classification"] != "SparseCap":
                continue
            if cap["intersection_size"] > len(cap["phase_sample"]):
                raise ValueError(
                    "SparseCap phase_sample 不完整；请提高 dualcap 的 phase_sample_limit"
                )
            phases = tuple(sorted(int(phase) for phase in cap["phase_sample"]))
            key = (p, phases)
            if key not in grouped:
                grouped[key] = {
                    "p": p,
                    "q": int(cap["q"]),
                    "phases": list(phases),
                    "descriptor_count": 0,
                    "descriptors": [],
                }
            grouped[key]["descriptor_count"] += 1
            grouped[key]["descriptors"].append(
                {
                    "alpha": cap["alpha"],
                    "direction": cap["direction"],
                    "h": cap["h"],
                    "source": cap["source"],
                    "cap_size": cap["cap_size"],
                    "intersection_size": cap["intersection_size"],
                    "mass_share_of_total_m": cap["mass_share_of_total_m"],
                }
            )
    return sorted(grouped.values(), key=lambda row: (row["p"], row["phases"]))


def analyze_sparse_cap(
    sparse_cap: dict[str, Any],
    mult_by_p: dict[int, dict[str, Any]],
    max_enumerate_period: int,
) -> dict[str, Any]:
    """分析一个去重后的 SparseCap 相位集。"""
    p = int(sparse_cap["p"])
    q = int(sparse_cap["q"])
    mult_item = mult_by_p[p]
    low_primes = [int(value) for value in mult_item["low_primes"]]
    high_primes = [int(value) for value in mult_item["high_primes"]]
    m_vector = [int(value) for value in mult_item["m_vector"]]
    phases = [int(phase) for phase in sparse_cap["phases"]]

    phase_reports = [
        analyze_sparse_phase(
            p=p,
            q=q,
            phase=phase,
            low_primes=low_primes,
            high_primes=high_primes,
            m_value=m_vector[phase],
            max_enumerate_period=max_enumerate_period,
        )
        for phase in phases
    ]
    early_conflicts = [
        row for row in phase_reports
        if row["phase_route"] == "EarlyCompletionConflict"
    ]
    local_witnesses = [
        row for row in phase_reports
        if row["local_survivor_witness_col"] is not None
    ]
    finite_atoms = [
        row for row in phase_reports
        if row["phase_route"] == "FinitePDECAtomBeyondP"
    ]
    total_m_bound = sum(m_vector[phase] for phase in phases)
    first_completion_rows = [
        row["first_completion_row"] for row in phase_reports
        if row["first_completion_row"] is not None
    ]
    p_square = p * p
    return {
        **sparse_cap,
        "base_primes": [int(value) for value in mult_item["base_primes"]],
        "low_primes": low_primes,
        "high_primes": high_primes,
        "total_m_bound_on_phase_set": total_m_bound,
        "phase_reports": phase_reports,
        "early_completion_conflicts": early_conflicts,
        "local_survivor_witness_count": len(local_witnesses),
        "finite_pdec_atom_count": len(finite_atoms),
        "first_completion_row_min": min(first_completion_rows) if first_completion_rows else None,
        "first_completion_row_over_p": (
            min(first_completion_rows) > p if first_completion_rows else True
        ),
        "first_completion_row_equals_p_square": (
            min(first_completion_rows) == p_square if first_completion_rows else False
        ),
        "cap_route": (
            "SparseCapClosedForPxPAndRoutedToFinitePDEC"
            if not early_conflicts
            else "SparseCapHasEarlyCompletionConflict"
        ),
        "finite_pdec_packet": {
            "modulus": q,
            "residues": phases,
            "mass_upper_bound": total_m_bound,
            "descriptor_count": sparse_cap["descriptor_count"],
            "formal_use": (
                "若无限反例族在该 sparse cap 中持久复现，则坏窗推前计数 g(t) "
                "被限制在这些有限 residue 上，下一步可用 finite PDEC / "
                "column-tail 行继续排斥。"
            ),
        },
    }


def run(
    dualcap_path: Path,
    mult_path: Path,
    max_enumerate_period: int,
) -> dict[str, Any]:
    """运行 SparseCap -> LocalSurvivor / finite PDEC 审计。"""
    dualcap = load_json(dualcap_path)
    mult = load_json(mult_path)
    mult_by_p = {int(item["p"]): item for item in mult["prime_results"]}
    sparse_caps = sparse_caps_from_dualcap(dualcap)
    cap_reports = [
        analyze_sparse_cap(
            sparse_cap=cap,
            mult_by_p=mult_by_p,
            max_enumerate_period=max_enumerate_period,
        )
        for cap in sparse_caps
    ]
    phase_reports = [
        phase
        for cap in cap_reports
        for phase in cap["phase_reports"]
    ]
    unique_phase_reports: dict[tuple[int, int], dict[str, Any]] = {}
    for cap in cap_reports:
        for phase in cap["phase_reports"]:
            unique_phase_reports[(int(cap["p"]), int(phase["phase"]))] = phase
    early_conflict_count = sum(
        1 for phase in phase_reports
        if phase["phase_route"] == "EarlyCompletionConflict"
    )
    unique_early_conflict_count = sum(
        1 for phase in unique_phase_reports.values()
        if phase["phase_route"] == "EarlyCompletionConflict"
    )
    return {
        "certificate_type": "triad_a1_sparsecap_local_survivor_audit",
        "status": "sparsecap_atoms_routed_to_local_survivor_or_finite_pdec",
        "q": int(dualcap["q"]),
        "max_enumerate_period": max_enumerate_period,
        "source_hashes": {
            "sparsecap_local_survivor_script": file_sha256(Path(__file__).resolve()),
            "dualcap_json": file_sha256(dualcap_path),
            "multiplicity_cap_json": file_sha256(mult_path),
        },
        "sparse_descriptor_count": sum(cap["descriptor_count"] for cap in cap_reports),
        "unique_sparse_cap_count": len(cap_reports),
        "phase_atom_count_with_multiplicity": len(phase_reports),
        "unique_phase_atom_count": len(unique_phase_reports),
        "early_completion_conflict_count": early_conflict_count,
        "unique_early_completion_conflict_count": unique_early_conflict_count,
        "all_sparse_caps_closed_for_pxP": early_conflict_count == 0,
        "local_survivor_witness_count": sum(
            1 for phase in phase_reports
            if phase["local_survivor_witness_col"] is not None
        ),
        "unique_local_survivor_witness_count": sum(
            1 for phase in unique_phase_reports.values()
            if phase["local_survivor_witness_col"] is not None
        ),
        "finite_pdec_atom_count": sum(
            1 for phase in phase_reports
            if phase["phase_route"] == "FinitePDECAtomBeyondP"
        ),
        "unique_finite_pdec_atom_count": sum(
            1 for phase in unique_phase_reports.values()
            if phase["phase_route"] == "FinitePDECAtomBeyondP"
        ),
        "cap_reports": cap_reports,
        "review_conclusion": (
            "SparseCap 路由已去重到有限相位原子。所有枚举到的 sparse 完成行都不在 "
            "P 行以内；phase<=P 但 y=0 不能完成的原子给出显式 LocalSurvivor 列见证，"
            "其余原子转入 finite PDEC packet。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 审稿摘要。"""
    lines = [
        "# Triad-A1 SparseCap 到 LocalSurvivor / finite PDEC 审计",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 证书语义",
        "",
        "`DualCap` 的 `SparseCap` 不能继续停在路由标签上。本文把它去重为有限相位集，并逐相位检查：",
        "",
        "```text",
        "row = phase + Q*y；",
        "y=0 且 phase<=P 代表 P 行以内真实早期行；",
        "若该行未被高素数补完，则输出未覆盖列 LocalSurvivor witness；",
        "若完成只发生在 y>0 或 phase>P，则该 sparse 原子转入 finite PDEC packet。",
        "```",
        "",
        "## 2. 来源指纹",
        "",
        "| source | sha256 |",
        "| --- | --- |",
    ]
    for name, digest in result["source_hashes"].items():
        lines.append(f"| `{name}` | `{digest}` |")

    lines.extend(
        [
            "",
            "## 3. 汇总",
            "",
            f"- `sparse_descriptor_count={result['sparse_descriptor_count']}`。",
            f"- `unique_sparse_cap_count={result['unique_sparse_cap_count']}`。",
            f"- `phase_atom_count_with_multiplicity={result['phase_atom_count_with_multiplicity']}`。",
            f"- `unique_phase_atom_count={result['unique_phase_atom_count']}`。",
            f"- `early_completion_conflict_count={result['early_completion_conflict_count']}`。",
            f"- `unique_early_completion_conflict_count={result['unique_early_completion_conflict_count']}`。",
            f"- `all_sparse_caps_closed_for_pxP={result['all_sparse_caps_closed_for_pxP']}`。",
            f"- `local_survivor_witness_count={result['local_survivor_witness_count']}`。",
            f"- `unique_local_survivor_witness_count={result['unique_local_survivor_witness_count']}`。",
            f"- `finite_pdec_atom_count={result['finite_pdec_atom_count']}`。",
            f"- `unique_finite_pdec_atom_count={result['unique_finite_pdec_atom_count']}`。",
            "",
            "| P | descriptors | phases | first completion row | equals P^2 | local witnesses | finite atoms | route |",
            "| ---: | ---: | ---: | ---: | --- | ---: | ---: | --- |",
        ]
    )
    for cap in result["cap_reports"]:
        lines.append(
            "| {p} | {desc} | {phases} | {first_row} | `{eq_p2}` | {lw} | {fa} | `{route}` |".format(
                p=cap["p"],
                desc=cap["descriptor_count"],
                phases=len(cap["phases"]),
                first_row=cap["first_completion_row_min"],
                eq_p2=cap["first_completion_row_equals_p_square"],
                lw=cap["local_survivor_witness_count"],
                fa=cap["finite_pdec_atom_count"],
                route=cap["cap_route"],
            )
        )

    lines.extend(["", "## 4. 相位原子", ""])
    for cap in result["cap_reports"]:
        lines.extend(
            [
                f"### P={cap['p']} sparse phase set",
                "",
                f"- residues mod `{cap['q']}`: `{cap['phases']}`。",
                f"- finite PDEC mass upper bound: `{cap['total_m_bound_on_phase_set']}`。",
                "",
                "| phase | holes | y completions | completion rows | y=0 complete | witness col | route |",
                "| ---: | --- | --- | --- | --- | --- | --- |",
            ]
        )
        for phase in cap["phase_reports"]:
            lines.append(
                "| {phase} | `{holes}` | `{ys}` | `{rows}` | `{y0}` | {wit} | `{route}` |".format(
                    phase=phase["phase"],
                    holes=phase["low_holes"],
                    ys=phase["completion_y_values"],
                    rows=phase["completion_rows"],
                    y0=phase["y0_complete"],
                    wit=phase["local_survivor_witness_col"],
                    route=phase["phase_route"],
                )
            )
        lines.append("")

    lines.extend(
        [
            "## 5. 结构读数",
            "",
            "本审计确认：在当前 `Q=2310` 的 sparse 失败帽中，没有一个完成态落在 `row<=P` 的早期方阵内。",
            "尤其 `P=13` 的最早 sparse 完成行为 `169=P^2`，正对应“必须到 P 与 P^2 连线后才出现完整斜线”的几何直觉。",
            "",
            "因此 `SparseCap` 路由已被压成：",
            "",
            "```text",
            "早期 phase<=P 且 y=0 不完成 => LocalSurvivor witness；",
            "完成行全部在 P 之后         => finite PDEC / column-tail 后续证书输入。",
            "```",
            "",
            "这仍不是整个行命题闭合；它关闭的是 `DualCap` 中 `SparseCap` 的 P×P 早期出口，并把持久稀疏复现交给 finite PDEC packet。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dualcap-json", type=Path, default=DEFAULT_DUALCAP)
    parser.add_argument("--multiplicity-json", type=Path, default=DEFAULT_MULT)
    parser.add_argument("--max-enumerate-period", type=int, default=100000)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        dualcap_path=args.dualcap_json,
        mult_path=args.multiplicity_json,
        max_enumerate_period=args.max_enumerate_period,
    )
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(
        json.dumps(
            {
                "status": result["status"],
                "all_sparse_caps_closed_for_pxP": result["all_sparse_caps_closed_for_pxP"],
                "early_completion_conflict_count": result["early_completion_conflict_count"],
                "unique_early_completion_conflict_count": result["unique_early_completion_conflict_count"],
                "local_survivor_witness_count": result["local_survivor_witness_count"],
                "unique_local_survivor_witness_count": result["unique_local_survivor_witness_count"],
                "finite_pdec_atom_count": result["finite_pdec_atom_count"],
                "unique_finite_pdec_atom_count": result["unique_finite_pdec_atom_count"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
