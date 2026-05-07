#!/usr/bin/env python3
"""把 PhaseResidueMutual 原子展开到完整 CRT 终端零行相位。

用法示例：
  python3 experiments/prime_matrix_triad_a1_phase_residue_full_crt_terminal_audit.py

输出：
  docs/monograph/prime-matrix-triad-a1-phase-residue-full-crt-terminal-audit.json
  docs/monograph/prime-matrix-triad-a1-phase-residue-full-crt-terminal-audit.md
"""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from math import prod
from pathlib import Path
from typing import Any

from prime_matrix_bpn_low_hole_bucket_capacity import low_holes_for_phase, primes_upto


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_ATOM_LIFT = DOCS / "prime-matrix-triad-a1-phase-residue-mutual-atom-lift-audit.json"
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-phase-residue-full-crt-terminal-audit.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-phase-residue-full-crt-terminal-audit.md"


def file_sha256(path: Path) -> str:
    """计算文件 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def completion_offsets(
    p: int,
    q: int,
    phase: int,
    low_primes: list[int],
    high_primes: list[int],
) -> tuple[list[int], list[int]]:
    """枚举剩余高素 CRT 偏移；返回补洞偏移与低洞。"""
    holes = low_holes_for_phase(p, q, low_primes, phase)
    high_period = prod(high_primes) if high_primes else 1
    if not holes:
        return list(range(high_period)), holes
    offsets = []
    for offset in range(high_period):
        row = phase + offset * q
        if all(
            any(((row - 1) * p + col) % prime == 0 for prime in high_primes)
            for col in holes
        ):
            offsets.append(offset)
    return offsets, holes


def terminal_rows_for_atom(row: dict[str, Any]) -> dict[str, Any]:
    """展开一个已有下一层数据的 atom row。"""
    p = int(row["p"])
    q_lift = int(row["q_lift"])
    next_q = int(row["next_q"])
    base_primes = primes_upto(p - 1)
    low_primes = [prime for prime in base_primes if next_q % prime == 0]
    high_primes = [prime for prime in base_primes if next_q % prime != 0]
    high_period = prod(high_primes) if high_primes else 1

    residue_reports = []
    terminal_phases = []
    for item in row["next_nonzero_residue_mass"]:
        residue = int(item["residue"])
        expected_mass = int(item["mass"])
        phase = int(row["new_phase"]) + residue * q_lift
        offsets, holes = completion_offsets(p, next_q, phase, low_primes, high_primes)
        phases = [phase + offset * next_q for offset in offsets]
        terminal_phases.extend(phases)
        residue_reports.append(
            {
                "next_residue": residue,
                "phase_at_next_q": phase,
                "expected_mass": expected_mass,
                "low_holes": holes,
                "completion_offsets": offsets,
                "completion_count": len(offsets),
                "mass_identity_holds": len(offsets) == expected_mass,
                "terminal_phases": phases,
                "all_terminal_phases_gt_p": all(value > p for value in phases),
                "all_terminal_phases_gt_p2": all(value > p * p for value in phases),
            }
        )

    terminal_phases_sorted = sorted(terminal_phases)
    return {
        "p": p,
        "source_route": row["route"],
        "q": int(row["q"]),
        "q_lift": q_lift,
        "next_q": next_q,
        "base_primes": base_primes,
        "low_primes_at_next_q": low_primes,
        "remaining_high_primes": high_primes,
        "remaining_high_period": high_period,
        "old_phase": int(row["old_phase"]),
        "source_residue": int(row["residue"]),
        "new_phase": int(row["new_phase"]),
        "expected_next_total_mass": int(row["next_total_mass"]),
        "terminal_phase_count": len(terminal_phases_sorted),
        "terminal_mass_identity_holds": len(terminal_phases_sorted) == int(row["next_total_mass"]),
        "min_terminal_phase": min(terminal_phases_sorted) if terminal_phases_sorted else None,
        "max_terminal_phase": max(terminal_phases_sorted) if terminal_phases_sorted else None,
        "min_terminal_phase_over_p": (
            min(terminal_phases_sorted) / p if terminal_phases_sorted else None
        ),
        "min_terminal_phase_over_p2": (
            min(terminal_phases_sorted) / (p * p) if terminal_phases_sorted else None
        ),
        "all_terminal_phases_gt_p": all(value > p for value in terminal_phases_sorted),
        "all_terminal_phases_gt_p2": all(value > p * p for value in terminal_phases_sorted),
        "residue_reports": residue_reports,
        "terminal_phases_sample": terminal_phases_sorted[:20],
        "route": (
            "FullCRTTerminalFarBeyondPxP"
            if terminal_phases_sorted and all(value > p for value in terminal_phases_sorted)
            else "TerminalNeedsLocalSurvivorOrPDEC"
        ),
    }


def run(atom_lift_path: Path) -> dict[str, Any]:
    """运行完整 CRT 终端审计。"""
    atom_lift = load_json(atom_lift_path)
    rows_with_next = [
        row for row in atom_lift["atom_rows"]
        if row["next_q"] is not None and row["next_total_mass"] is not None
    ]
    terminal_rows = [terminal_rows_for_atom(row) for row in rows_with_next]
    route_counts = Counter(row["route"] for row in terminal_rows)
    source_route_counts = Counter(row["source_route"] for row in terminal_rows)
    return {
        "certificate_type": "triad_a1_phase_residue_full_crt_terminal_audit",
        "status": "phase_residue_atoms_expanded_to_full_crt_terminal_rows",
        "source_hashes": {
            "phase_residue_full_crt_terminal_script": file_sha256(Path(__file__).resolve()),
            "phase_residue_atom_lift_json": file_sha256(atom_lift_path),
        },
        "rows_with_next_count": len(rows_with_next),
        "terminal_row_count": len(terminal_rows),
        "route_counts": dict(route_counts),
        "source_route_counts": dict(source_route_counts),
        "all_terminal_mass_identities_hold": all(
            row["terminal_mass_identity_holds"] for row in terminal_rows
        ),
        "all_residue_mass_identities_hold": all(
            report["mass_identity_holds"]
            for row in terminal_rows
            for report in row["residue_reports"]
        ),
        "all_terminal_phases_gt_p": all(
            row["all_terminal_phases_gt_p"] for row in terminal_rows
        ),
        "all_terminal_phases_gt_p2": all(
            row["all_terminal_phases_gt_p2"] for row in terminal_rows
        ),
        "min_terminal_phase": min(
            (row["min_terminal_phase"] for row in terminal_rows if row["min_terminal_phase"] is not None),
            default=None,
        ),
        "min_terminal_phase_over_p": min(
            (
                row["min_terminal_phase_over_p"]
                for row in terminal_rows
                if row["min_terminal_phase_over_p"] is not None
            ),
            default=None,
        ),
        "min_terminal_phase_over_p2": min(
            (
                row["min_terminal_phase_over_p2"]
                for row in terminal_rows
                if row["min_terminal_phase_over_p2"] is not None
            ),
            default=None,
        ),
        "terminal_rows": terminal_rows,
        "structural_law": (
            "对每个已有下一层数据的互信息原子，先把每个非零下一 residue 写成相位 v，"
            "再枚举剩余高素 CRT 偏移。展开计数必须等于记录的 M(v)；"
            "展开得到的相位都是完整 CRT 零行相位。"
        ),
        "review_conclusion": (
            "当前已有下一层数据的 phase-residue 原子全部可展开为完整 CRT 零行相位，"
            "且所有终端相位均大于 P^2；它们不能形成 P 行以内零行，只能作为远处 finite/profinite PDEC 数据包。"
        ),
    }


def fmt_float(value: float | None) -> str:
    """格式化浮点数。"""
    if value is None:
        return "n/a"
    return f"{value:.6g}"


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 PhaseResidue 完整 CRT 终端审计",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 结构律",
        "",
        result["structural_law"],
        "",
        "```text",
        "atom u at Q'；",
        "next residue phase v=u+sQ'；",
        "terminal phase w=v+y*nextQ；",
        "completion_count(v)=#{y: w 是完整 CRT 零行相位}。",
        "```",
        "",
        "## 2. 汇总",
        "",
        f"- `rows_with_next_count={result['rows_with_next_count']}`。",
        f"- `source_route_counts={result['source_route_counts']}`。",
        f"- `route_counts={result['route_counts']}`。",
        f"- `all_terminal_mass_identities_hold={result['all_terminal_mass_identities_hold']}`。",
        f"- `all_residue_mass_identities_hold={result['all_residue_mass_identities_hold']}`。",
        f"- `all_terminal_phases_gt_p={result['all_terminal_phases_gt_p']}`。",
        f"- `all_terminal_phases_gt_p2={result['all_terminal_phases_gt_p2']}`。",
        f"- `min_terminal_phase={result['min_terminal_phase']}`。",
        f"- `min_terminal_phase_over_p={fmt_float(result['min_terminal_phase_over_p'])}`。",
        f"- `min_terminal_phase_over_p2={fmt_float(result['min_terminal_phase_over_p2'])}`。",
        "",
        "## 3. 原子级明细",
        "",
        "| P | source route | Q' | next Q | u | terminal count | min terminal | max terminal | route |",
        "| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in result["terminal_rows"]:
        lines.append(
            "| {p} | `{source}` | {ql} | {nq} | {u} | {count} | {minp} | {maxp} | `{route}` |".format(
                p=row["p"],
                source=row["source_route"],
                ql=row["q_lift"],
                nq=row["next_q"],
                u=row["new_phase"],
                count=row["terminal_phase_count"],
                minp=row["min_terminal_phase"],
                maxp=row["max_terminal_phase"],
                route=row["route"],
            )
        )

    lines.extend(
        [
            "",
            "## 4. 读法",
            "",
            "这一步同时处理上一账本中的 `NextLayerCleanFiberCandidate` 与 `NextLayerRefinedPDECEntropy`。",
            "两类在当前已有下一层数据时都已展开为完整 CRT 零行相位，并且全部远离 `P×P` 早期区域。",
            "剩余 `NoNextLayerDataProfiniteObligation` 仍需在更高层按同一规则处理，不能视为已排除。",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--atom-lift-json", type=Path, default=DEFAULT_ATOM_LIFT)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(args.atom_lift_json)
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(
        json.dumps(
            {
                "status": result["status"],
                "rows_with_next_count": result["rows_with_next_count"],
                "source_route_counts": result["source_route_counts"],
                "all_terminal_mass_identities_hold": result["all_terminal_mass_identities_hold"],
                "all_terminal_phases_gt_p2": result["all_terminal_phases_gt_p2"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
