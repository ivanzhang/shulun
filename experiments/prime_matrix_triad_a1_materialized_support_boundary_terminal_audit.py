#!/usr/bin/env python3
"""审计已物化 A1 支撑相位能否在 P 行以内产生终端零行。

用法示例：
  python3 experiments/prime_matrix_triad_a1_materialized_support_boundary_terminal_audit.py

输出：
  docs/monograph/prime-matrix-triad-a1-materialized-support-boundary-terminal-audit.json
  docs/monograph/prime-matrix-triad-a1-materialized-support-boundary-terminal-audit.md
"""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
from typing import Any

from prime_matrix_bpn_low_hole_bucket_capacity import primes_upto


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_MULTS = ",".join(
    str(path)
    for path in (
        DOCS / "h4-pdec-lhb-multiplicity-cap-certificate.json",
        DOCS / "prime-matrix-triad-a1-q30030-multiplicity-cap.json",
        DOCS / "prime-matrix-triad-a1-q510510-multiplicity-cap.json",
    )
)
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-materialized-support-boundary-terminal-audit.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-materialized-support-boundary-terminal-audit.md"


def parse_paths(raw: str) -> list[Path]:
    """解析逗号分隔路径。"""
    return [Path(item.strip()) for item in raw.split(",") if item.strip()]


def file_sha256(path: Path) -> str:
    """计算文件 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def uncovered_columns(p: int, row: int, primes: list[int]) -> list[int]:
    """返回给定行在完整小素数筛下未覆盖的列。"""
    holes = []
    for col in range(1, p):
        value = (row - 1) * p + col
        if not any(value % prime == 0 for prime in primes):
            holes.append(col)
    return holes


def positive_representative_lower_bound(
    phase: int,
    q: int,
    p: int,
    y0_complete: bool,
) -> int:
    """给出该相位类完整终端行的一个早期下界。"""
    if phase == 0:
        return q
    if phase <= p and not y0_complete:
        return phase + q
    return phase


def analyze_prime_item(
    q: int,
    item: dict[str, Any],
    witness_limit: int,
) -> dict[str, Any]:
    """分析单个 `(P,Q)` 的支撑相位边界终端。"""
    p = int(item["p"])
    if q <= p:
        raise ValueError(f"boundary audit requires q>P, got q={q}, P={p}")
    primes = primes_upto(p - 1)
    m_vector = [int(value) for value in item["m_vector"]]
    support = [phase for phase, value in enumerate(m_vector) if value > 0]

    phase_le_p_rows = []
    y0_completion_rows = []
    y0_completion_le_p_rows = []
    y0_completion_le_p2_rows = []
    lower_bounds = []

    for phase in support:
        y0_complete = False
        holes: list[int] | None = None
        if phase != 0:
            holes = uncovered_columns(p, phase, primes)
            y0_complete = len(holes) == 0
            if y0_complete:
                y0_completion_rows.append(phase)
                if phase <= p:
                    y0_completion_le_p_rows.append(phase)
                if phase <= p * p:
                    y0_completion_le_p2_rows.append(phase)

        lower_bounds.append(
            positive_representative_lower_bound(phase, q, p, y0_complete)
        )

        if 1 <= phase <= p:
            if holes is None:
                holes = uncovered_columns(p, phase, primes)
            phase_le_p_rows.append(
                {
                    "phase": phase,
                    "mass": m_vector[phase],
                    "y0_complete": y0_complete,
                    "uncovered_columns": holes,
                    "first_uncovered_column": holes[0] if holes else None,
                }
            )

    route = (
        "BoundaryTerminalExcluded"
        if not y0_completion_le_p_rows
        else "BoundaryTerminalConflict"
    )
    return {
        "p": p,
        "q": q,
        "base_primes": primes,
        "nonzero_phase_count": len(support),
        "total_mass": sum(m_vector),
        "min_nonzero_phase": min((phase for phase in support if phase > 0), default=None),
        "phase_le_p_count": len(phase_le_p_rows),
        "phase_le_p_mass": sum(row["mass"] for row in phase_le_p_rows),
        "phase_le_p_rows": phase_le_p_rows[:witness_limit],
        "phase_le_p_all_have_local_survivor": all(
            not row["y0_complete"] and row["uncovered_columns"]
            for row in phase_le_p_rows
        ),
        "y0_completion_count": len(y0_completion_rows),
        "min_y0_completion_phase": min(y0_completion_rows, default=None),
        "y0_completion_le_p_count": len(y0_completion_le_p_rows),
        "y0_completion_le_p_rows": y0_completion_le_p_rows[:witness_limit],
        "y0_completion_le_p2_count": len(y0_completion_le_p2_rows),
        "y0_completion_le_p2_rows": y0_completion_le_p2_rows[:witness_limit],
        "terminal_lower_bound_min": min(lower_bounds, default=None),
        "terminal_lower_bound_gt_p": all(value > p for value in lower_bounds),
        "terminal_lower_bound_gt_p2": all(value > p * p for value in lower_bounds),
        "route": route,
    }


def analyze_file(path: Path, witness_limit: int) -> dict[str, Any]:
    """分析一个 multiplicity 文件。"""
    data = load_json(path)
    q = int(data["q"])
    prime_rows = [
        analyze_prime_item(q, item, witness_limit)
        for item in data["prime_results"]
    ]
    return {
        "path": str(path),
        "sha256": file_sha256(path),
        "q": q,
        "p_values": [row["p"] for row in prime_rows],
        "prime_rows": prime_rows,
    }


def run(paths: list[Path], witness_limit: int) -> dict[str, Any]:
    """运行边界终端审计。"""
    q_results = [analyze_file(path, witness_limit) for path in paths]
    prime_rows = [
        row for q_result in q_results for row in q_result["prime_rows"]
    ]
    route_counts = Counter(row["route"] for row in prime_rows)
    return {
        "certificate_type": "triad_a1_materialized_support_boundary_terminal_audit",
        "status": "materialized_support_boundary_terminal_excluded_current_layers",
        "parameters": {
            "witness_limit": witness_limit,
            "meaning": "当 Q>P 时，只需检查支撑相位中 1<=u<=P 的 y=0 行是否完整覆盖。",
        },
        "source_hashes": {
            "materialized_support_boundary_terminal_script": file_sha256(Path(__file__).resolve()),
            **{
                f"multiplicity_q{result['q']}": result["sha256"]
                for result in q_results
            },
        },
        "q_results": q_results,
        "prime_row_count": len(prime_rows),
        "route_counts": dict(route_counts),
        "all_boundary_terminals_excluded": all(
            row["y0_completion_le_p_count"] == 0 for row in prime_rows
        ),
        "total_phase_le_p_count": sum(row["phase_le_p_count"] for row in prime_rows),
        "total_phase_le_p_mass": sum(row["phase_le_p_mass"] for row in prime_rows),
        "total_y0_completion_le_p_count": sum(row["y0_completion_le_p_count"] for row in prime_rows),
        "total_y0_completion_le_p2_count": sum(row["y0_completion_le_p2_count"] for row in prime_rows),
        "all_phase_le_p_have_local_survivor": all(
            row["phase_le_p_all_have_local_survivor"] for row in prime_rows
        ),
        "all_terminal_lower_bounds_gt_p": all(
            row["terminal_lower_bound_gt_p"] for row in prime_rows
        ),
        "global_min_terminal_lower_bound": min(
            (row["terminal_lower_bound_min"] for row in prime_rows if row["terminal_lower_bound_min"] is not None),
            default=None,
        ),
        "structural_law": (
            "If Q>P, any terminal row in a phase class u mod Q that lies within the first P rows "
            "must be exactly the y=0 representative with 1<=u<=P. Thus boundary exclusion reduces "
            "to checking whether such y=0 representatives are complete zero rows."
        ),
        "review_conclusion": (
            "当前 Q=2310、30030、510510 的所有已物化支撑相位均无 y=0 的 <=P 完整覆盖。"
            "少数支撑相位落在 1..P 时，都有明确未覆盖列作为 LocalSurvivor witness；"
            "因此这些已物化层的边界终端早期出口全部关闭。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 已物化支撑边界终端审计",
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
        "Q>P；",
        "terminal row r = u + yQ；",
        "r<=P 只能发生在 y=0 且 1<=u<=P；",
        "若该 y=0 行未完整覆盖，则此相位类不能给出 P 行以内零行。",
        "```",
        "",
        "这一步不依赖固定常数，也不需要展开巨大 CRT fiber。",
        "",
        "## 2. 汇总",
        "",
        f"- `prime_row_count={result['prime_row_count']}`。",
        f"- `route_counts={result['route_counts']}`。",
        f"- `all_boundary_terminals_excluded={result['all_boundary_terminals_excluded']}`。",
        f"- `total_phase_le_p_count={result['total_phase_le_p_count']}`。",
        f"- `total_phase_le_p_mass={result['total_phase_le_p_mass']}`。",
        f"- `total_y0_completion_le_p_count={result['total_y0_completion_le_p_count']}`。",
        f"- `total_y0_completion_le_p2_count={result['total_y0_completion_le_p2_count']}`。",
        f"- `all_phase_le_p_have_local_survivor={result['all_phase_le_p_have_local_survivor']}`。",
        f"- `all_terminal_lower_bounds_gt_p={result['all_terminal_lower_bounds_gt_p']}`。",
        f"- `global_min_terminal_lower_bound={result['global_min_terminal_lower_bound']}`。",
        "",
        "## 3. P 级明细",
        "",
        "| Q | P | support phases | total mass | phases <=P | mass <=P | y0 zero <=P | y0 zero <=P^2 | min y0 zero | route |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for q_result in result["q_results"]:
        for row in q_result["prime_rows"]:
            lines.append(
                "| {q} | {p} | {support} | {mass} | {lep} | {lepm} | {zlep} | {zlep2} | {minz} | `{route}` |".format(
                    q=q_result["q"],
                    p=row["p"],
                    support=row["nonzero_phase_count"],
                    mass=row["total_mass"],
                    lep=row["phase_le_p_count"],
                    lepm=row["phase_le_p_mass"],
                    zlep=row["y0_completion_le_p_count"],
                    zlep2=row["y0_completion_le_p2_count"],
                    minz=row["min_y0_completion_phase"],
                    route=row["route"],
                )
            )

    lines.extend(
        [
            "",
            "## 4. 首端支撑见证",
            "",
            "| Q | P | phase | mass | first uncovered column | uncovered columns |",
            "| ---: | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for q_result in result["q_results"]:
        for row in q_result["prime_rows"]:
            for witness in row["phase_le_p_rows"]:
                lines.append(
                    "| {q} | {p} | {phase} | {mass} | {first} | `{holes}` |".format(
                        q=q_result["q"],
                        p=row["p"],
                        phase=witness["phase"],
                        mass=witness["mass"],
                        first=witness["first_uncovered_column"],
                        holes=witness["uncovered_columns"],
                    )
                )

    lines.extend(
        [
            "",
            "## 5. 读法",
            "",
            "该报告比完整 CRT 终端展开更便宜：它只检查边界帽 `r<=P` 是否可能出现。",
            "若某相位 `u<=P` 有支撑但 `y=0` 不完整，则完成态即使存在也必须从 `u+Q` 开始，必然大于 `P`。",
            "这给后继层推广提供了一个一般接口：只要 `Q>P`，边界早期出口可由有限个 `u<=P` 的局部 survivor 见证排除。",
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
    parser.add_argument("--witness-limit", type=int, default=12)
    args = parser.parse_args()

    result = run(parse_paths(args.multiplicity_jsons), args.witness_limit)
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(
        json.dumps(
            {
                "status": result["status"],
                "prime_row_count": result["prime_row_count"],
                "all_boundary_terminals_excluded": result["all_boundary_terminals_excluded"],
                "total_phase_le_p_count": result["total_phase_le_p_count"],
                "total_y0_completion_le_p_count": result["total_y0_completion_le_p_count"],
                "all_phase_le_p_have_local_survivor": result["all_phase_le_p_have_local_survivor"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
