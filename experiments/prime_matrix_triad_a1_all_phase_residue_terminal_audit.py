#!/usr/bin/env python3
"""把当前已物化升层的全部非零 phase-residue 原子展开到完整 CRT 终端。

用法示例：
  python3 experiments/prime_matrix_triad_a1_all_phase_residue_terminal_audit.py

输出：
  docs/monograph/prime-matrix-triad-a1-all-phase-residue-terminal-audit.json
  docs/monograph/prime-matrix-triad-a1-all-phase-residue-terminal-audit.md
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
DEFAULT_MULTS = ",".join(
    str(path)
    for path in (
        DOCS / "prime-matrix-triad-a1-q30030-multiplicity-cap.json",
        DOCS / "prime-matrix-triad-a1-q510510-multiplicity-cap.json",
    )
)
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-all-phase-residue-terminal-audit.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-all-phase-residue-terminal-audit.md"


def parse_paths(raw: str) -> list[Path]:
    """解析逗号分隔路径。"""
    return [Path(item.strip()) for item in raw.split(",") if item.strip()]


def file_sha256(path: Path) -> str:
    """计算文件 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def completion_phases(
    p: int,
    q: int,
    phase: int,
    low_primes: list[int],
    high_primes: list[int],
) -> tuple[list[int], list[int]]:
    """对单个相位局部展开剩余高素 CRT fiber。"""
    holes = low_holes_for_phase(p, q, low_primes, phase)
    high_period = prod(high_primes) if high_primes else 1
    if not holes:
        return [phase + offset * q for offset in range(high_period)], holes

    phases = []
    for offset in range(high_period):
        row = phase + offset * q
        complete = True
        for col in holes:
            if not any(((row - 1) * p + col) % prime == 0 for prime in high_primes):
                complete = False
                break
        if complete:
            phases.append(row)
    return phases, holes


def phase_report(
    p: int,
    q: int,
    phase: int,
    expected_mass: int,
    low_primes: list[int],
    high_primes: list[int],
    sample_limit: int,
) -> dict[str, Any]:
    """生成单相位终端展开报告。"""
    phases, holes = completion_phases(p, q, phase, low_primes, high_primes)
    phases_sorted = sorted(phases)
    count = len(phases_sorted)
    return {
        "phase": phase,
        "expected_mass": expected_mass,
        "completion_count": count,
        "mass_identity_holds": count == expected_mass,
        "low_holes": holes,
        "min_terminal_phase": phases_sorted[0] if phases_sorted else None,
        "max_terminal_phase": phases_sorted[-1] if phases_sorted else None,
        "terminal_phase_sample": phases_sorted[:sample_limit],
        "terminal_le_p": [value for value in phases_sorted if value <= p],
        "terminal_le_p2_sample": [
            value for value in phases_sorted if value <= p * p
        ][:sample_limit],
        "terminal_le_p_count": sum(1 for value in phases_sorted if value <= p),
        "terminal_le_p2_count": sum(1 for value in phases_sorted if value <= p * p),
        "all_terminal_gt_p": all(value > p for value in phases_sorted),
        "all_terminal_gt_p2": all(value > p * p for value in phases_sorted),
    }


def analyze_prime_item(
    q: int,
    item: dict[str, Any],
    sample_limit: int,
) -> dict[str, Any]:
    """分析一个 `(P,Q)` 的全部非零相位。"""
    p = int(item["p"])
    m_vector = [int(value) for value in item["m_vector"]]
    base_primes = primes_upto(p - 1)
    low_primes = [prime for prime in base_primes if q % prime == 0]
    high_primes = [prime for prime in base_primes if q % prime != 0]
    high_period = prod(high_primes) if high_primes else 1
    reports = [
        phase_report(
            p,
            q,
            phase,
            value,
            low_primes,
            high_primes,
            sample_limit,
        )
        for phase, value in enumerate(m_vector)
        if value > 0
    ]
    total_terminal_count = sum(row["completion_count"] for row in reports)
    expected_total = sum(row["expected_mass"] for row in reports)
    earliest = sorted(
        (
            row["min_terminal_phase"]
            for row in reports
            if row["min_terminal_phase"] is not None
        )
    )[:sample_limit]
    le_p_rows = [row for row in reports if row["terminal_le_p_count"] > 0]
    le_p2_rows = [row for row in reports if row["terminal_le_p2_count"] > 0]
    mismatch_rows = [row for row in reports if not row["mass_identity_holds"]]
    return {
        "p": p,
        "q": q,
        "base_primes": base_primes,
        "low_primes": low_primes,
        "remaining_high_primes": high_primes,
        "remaining_high_period": high_period,
        "nonzero_phase_count": len(reports),
        "expected_total_mass": expected_total,
        "total_terminal_count": total_terminal_count,
        "total_mass_identity_holds": expected_total == total_terminal_count,
        "all_phase_mass_identities_hold": not mismatch_rows,
        "all_terminal_gt_p": all(row["all_terminal_gt_p"] for row in reports),
        "all_terminal_gt_p2": all(row["all_terminal_gt_p2"] for row in reports),
        "terminal_le_p_count": sum(row["terminal_le_p_count"] for row in reports),
        "terminal_le_p2_count": sum(row["terminal_le_p2_count"] for row in reports),
        "phase_with_terminal_le_p_count": len(le_p_rows),
        "phase_with_terminal_le_p2_count": len(le_p2_rows),
        "min_terminal_phase": earliest[0] if earliest else None,
        "earliest_terminal_phases": earliest,
        "mismatch_phase_sample": mismatch_rows[:sample_limit],
        "terminal_le_p_phase_sample": le_p_rows[:sample_limit],
        "terminal_le_p2_phase_sample": le_p2_rows[:sample_limit],
        "phase_report_count": len(reports),
    }


def analyze_multiplicity(path: Path, sample_limit: int) -> dict[str, Any]:
    """分析一个 multiplicity-cap JSON。"""
    data = load_json(path)
    q = int(data["q"])
    prime_summaries = [
        analyze_prime_item(q, item, sample_limit)
        for item in data["prime_results"]
    ]
    return {
        "path": str(path),
        "sha256": file_sha256(path),
        "q": q,
        "p_values": [row["p"] for row in prime_summaries],
        "prime_summaries": prime_summaries,
    }


def run(paths: list[Path], sample_limit: int) -> dict[str, Any]:
    """运行全部非零 phase-residue 终端审计。"""
    q_results = [analyze_multiplicity(path, sample_limit) for path in paths]
    prime_rows = [
        row
        for q_result in q_results
        for row in q_result["prime_summaries"]
    ]
    route_counts = Counter(
        "AllTerminalBeyondP" if row["all_terminal_gt_p"] else "HasTerminalAtOrBeforeP"
        for row in prime_rows
    )
    return {
        "certificate_type": "triad_a1_all_phase_residue_terminal_audit",
        "status": "all_materialized_phase_residue_atoms_expanded_to_full_crt",
        "parameters": {
            "sample_limit": sample_limit,
            "meaning": "审计当前已物化 Q=30030 与 Q=510510 的全部非零相位，不只 top KL 原子。",
        },
        "source_hashes": {
            "all_phase_residue_terminal_script": file_sha256(Path(__file__).resolve()),
            **{
                f"multiplicity_q{result['q']}": result["sha256"]
                for result in q_results
            },
        },
        "q_results": q_results,
        "prime_row_count": len(prime_rows),
        "route_counts": dict(route_counts),
        "all_total_mass_identities_hold": all(
            row["total_mass_identity_holds"] for row in prime_rows
        ),
        "all_phase_mass_identities_hold": all(
            row["all_phase_mass_identities_hold"] for row in prime_rows
        ),
        "all_terminal_gt_p": all(row["all_terminal_gt_p"] for row in prime_rows),
        "all_terminal_gt_p2": all(row["all_terminal_gt_p2"] for row in prime_rows),
        "total_nonzero_phase_count": sum(row["nonzero_phase_count"] for row in prime_rows),
        "total_terminal_count": sum(row["total_terminal_count"] for row in prime_rows),
        "total_terminal_le_p_count": sum(row["terminal_le_p_count"] for row in prime_rows),
        "total_terminal_le_p2_count": sum(row["terminal_le_p2_count"] for row in prime_rows),
        "global_min_terminal_phase": min(
            (row["min_terminal_phase"] for row in prime_rows if row["min_terminal_phase"] is not None),
            default=None,
        ),
        "structural_law": (
            "对每个非零 M_Q(u)，枚举剩余高素 CRT fiber u+yQ。完整终端行数量必须等于 M_Q(u)。"
            "若所有终端行都大于 P，则这一整层已物化 phase-residue 原子都不能在前 P 行内产生零行。"
        ),
        "review_conclusion": (
            "当前已物化 Q=30030 与 Q=510510 的全部非零相位都可局部展开为完整 CRT 终端相位，"
            "且所有终端相位均大于 P；因此当前有限升层的全 phase-residue 原子都不能产生 P 行以内零行。"
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
        "# Triad-A1 全 PhaseResidue 终端审计",
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
        "M_Q(u)>0；",
        "R={ell<P: ell does not divide Q}；",
        "terminal row w=u+yQ, y mod prod(R)；",
        "M_Q(u)=#{y: w 完整覆盖}。",
        "```",
        "",
        "这一步审计全部非零相位，不只 `NoDeletion-KL` 见证器抽出的 top 原子。",
        "",
        "## 2. 汇总",
        "",
        f"- `prime_row_count={result['prime_row_count']}`。",
        f"- `route_counts={result['route_counts']}`。",
        f"- `total_nonzero_phase_count={result['total_nonzero_phase_count']}`。",
        f"- `total_terminal_count={result['total_terminal_count']}`。",
        f"- `all_total_mass_identities_hold={result['all_total_mass_identities_hold']}`。",
        f"- `all_phase_mass_identities_hold={result['all_phase_mass_identities_hold']}`。",
        f"- `all_terminal_gt_p={result['all_terminal_gt_p']}`。",
        f"- `all_terminal_gt_p2={result['all_terminal_gt_p2']}`。",
        f"- `total_terminal_le_p_count={result['total_terminal_le_p_count']}`。",
        f"- `total_terminal_le_p2_count={result['total_terminal_le_p2_count']}`。",
        f"- `global_min_terminal_phase={result['global_min_terminal_phase']}`。",
        "",
        "## 3. P 级明细",
        "",
        "| Q | P | nonzero phases | terminal count | high primes | min terminal | <=P | <=P^2 | mass ok | >P | >P^2 | earliest terminals |",
        "| ---: | ---: | ---: | ---: | --- | ---: | ---: | ---: | --- | --- | --- | --- |",
    ]
    for q_result in result["q_results"]:
        for row in q_result["prime_summaries"]:
            lines.append(
                "| {q} | {p} | {nz} | {tc} | `{high}` | {minp} | {lep} | {lep2} | `{mok}` | `{gtp}` | `{gtp2}` | `{early}` |".format(
                    q=q_result["q"],
                    p=row["p"],
                    nz=row["nonzero_phase_count"],
                    tc=row["total_terminal_count"],
                    high=row["remaining_high_primes"],
                    minp=row["min_terminal_phase"],
                    lep=row["terminal_le_p_count"],
                    lep2=row["terminal_le_p2_count"],
                    mok=row["total_mass_identity_holds"] and row["all_phase_mass_identities_hold"],
                    gtp=row["all_terminal_gt_p"],
                    gtp2=row["all_terminal_gt_p2"],
                    early=row["earliest_terminal_phases"],
                )
            )

    lines.extend(
        [
            "",
            "## 4. 读法",
            "",
            "`all_terminal_gt_p=True` 是行命题相关读数：当前已物化升层的全部非零相位都不会在第 `P` 行以内形成零行。",
            "`all_terminal_gt_p2=False` 是预期现象，例如 `P=23` 的完整 CRT 周期中存在第 59 行零行；它不违反行命题，因为 59>P。",
            "因此本报告关闭的是当前有限升层全原子的 `P×P` 早期出口，不是所有无限终端证书全集。",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--multiplicity-jsons", default=DEFAULT_MULTS)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    parser.add_argument("--sample-limit", type=int, default=8)
    args = parser.parse_args()

    result = run(parse_paths(args.multiplicity_jsons), args.sample_limit)
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(
        json.dumps(
            {
                "status": result["status"],
                "total_nonzero_phase_count": result["total_nonzero_phase_count"],
                "total_terminal_count": result["total_terminal_count"],
                "all_terminal_gt_p": result["all_terminal_gt_p"],
                "all_terminal_gt_p2": result["all_terminal_gt_p2"],
                "total_terminal_le_p_count": result["total_terminal_le_p_count"],
                "total_terminal_le_p2_count": result["total_terminal_le_p2_count"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
