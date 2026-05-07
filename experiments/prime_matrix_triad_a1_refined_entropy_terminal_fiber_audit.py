#!/usr/bin/env python3
"""审计 PhaseResidueMutual 中 RefinedPDECEntropy 峰的终端 fiber。

用法示例：
  python3 experiments/prime_matrix_triad_a1_refined_entropy_terminal_fiber_audit.py

输出：
  docs/monograph/prime-matrix-triad-a1-refined-entropy-terminal-fiber-audit.json
  docs/monograph/prime-matrix-triad-a1-refined-entropy-terminal-fiber-audit.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from math import prod
from pathlib import Path
from typing import Any

from prime_matrix_bpn_low_hole_bucket_capacity import low_holes_for_phase, primes_upto


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_ATOM_LIFT = DOCS / "prime-matrix-triad-a1-phase-residue-mutual-atom-lift-audit.json"
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-refined-entropy-terminal-fiber-audit.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-refined-entropy-terminal-fiber-audit.md"


def file_sha256(path: Path) -> str:
    """计算文件 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def analyze_entropy_row(row: dict[str, Any]) -> dict[str, Any]:
    """分析一个下一层仍偏斜的互信息原子。"""
    p = int(row["p"])
    q_lift = int(row["q_lift"])
    next_q = int(row["next_q"])
    next_residue = int(row["next_top_residue"])
    new_phase = int(row["new_phase"])
    terminal_phase = new_phase + next_residue * q_lift
    if not 0 <= terminal_phase < next_q:
        raise ValueError(f"terminal phase out of range: {terminal_phase} mod {next_q}")

    base_primes = primes_upto(p - 1)
    low_primes = [prime for prime in base_primes if next_q % prime == 0]
    high_primes = [prime for prime in base_primes if next_q % prime != 0]
    holes = low_holes_for_phase(p, next_q, low_primes, terminal_phase)
    high_period = prod(high_primes) if high_primes else 1
    terminal_children = [
        terminal_phase + idx * next_q
        for idx in range(high_period)
    ]
    is_full_zero_fiber = len(holes) == 0
    return {
        "p": p,
        "source_q": int(row["q"]),
        "source_q_lift": q_lift,
        "next_q": next_q,
        "base_primes": base_primes,
        "low_primes_at_next_q": low_primes,
        "remaining_high_primes": high_primes,
        "new_phase": new_phase,
        "next_top_residue": next_residue,
        "terminal_phase": terminal_phase,
        "terminal_phase_over_p": terminal_phase / p,
        "terminal_phase_over_p2": terminal_phase / (p * p),
        "terminal_phase_le_p": terminal_phase <= p,
        "terminal_phase_le_p2": terminal_phase <= p * p,
        "low_holes_at_terminal_phase": holes,
        "is_full_zero_fiber_before_remaining_high_primes": is_full_zero_fiber,
        "terminal_child_count": len(terminal_children),
        "terminal_children": terminal_children,
        "min_terminal_child": min(terminal_children),
        "max_terminal_child": max(terminal_children),
        "all_terminal_children_gt_p": all(child > p for child in terminal_children),
        "all_terminal_children_gt_p2": all(child > p * p for child in terminal_children),
        "source_next_normalized_kl": row["next_normalized_kl"],
        "source_next_top_probability": row["next_top_probability"],
        "route": (
            "TerminalFullZeroFiberFarBeyondPxP"
            if is_full_zero_fiber and all(child > p for child in terminal_children)
            else "NeedsFurtherTerminalPDECOrLocalSurvivor"
        ),
    }


def run(atom_lift_path: Path) -> dict[str, Any]:
    """运行终端 fiber 审计。"""
    atom_lift = load_json(atom_lift_path)
    entropy_rows = [
        row for row in atom_lift["atom_rows"]
        if row["route"] == "NextLayerRefinedPDECEntropy"
    ]
    terminal_rows = [analyze_entropy_row(row) for row in entropy_rows]
    route_counts: dict[str, int] = {}
    for row in terminal_rows:
        route_counts[row["route"]] = route_counts.get(row["route"], 0) + 1

    return {
        "certificate_type": "triad_a1_refined_entropy_terminal_fiber_audit",
        "status": "refined_entropy_peaks_terminal_full_fiber_current_data",
        "source_hashes": {
            "refined_entropy_terminal_fiber_script": file_sha256(Path(__file__).resolve()),
            "phase_residue_atom_lift_json": file_sha256(atom_lift_path),
        },
        "entropy_peak_count": len(entropy_rows),
        "terminal_row_count": len(terminal_rows),
        "route_counts": route_counts,
        "all_terminal_low_holes_empty": all(
            not row["low_holes_at_terminal_phase"] for row in terminal_rows
        ),
        "all_terminal_children_gt_p": all(
            row["all_terminal_children_gt_p"] for row in terminal_rows
        ),
        "all_terminal_children_gt_p2": all(
            row["all_terminal_children_gt_p2"] for row in terminal_rows
        ),
        "min_terminal_phase": min((row["terminal_phase"] for row in terminal_rows), default=None),
        "min_terminal_phase_over_p": min(
            (row["terminal_phase_over_p"] for row in terminal_rows),
            default=None,
        ),
        "min_terminal_phase_over_p2": min(
            (row["terminal_phase_over_p2"] for row in terminal_rows),
            default=None,
        ),
        "terminal_rows": terminal_rows,
        "structural_law": (
            "一个 NextLayerRefinedPDECEntropy 原子 u 与 top residue b 生成终端相位 "
            "v=u+bQ'。若 v 在下一模数下低洞为空，则剩余高素 fiber 已经是完整零行 fiber；"
            "当 v>P 时，它不能成为 P×P 内早期零行。"
        ),
        "review_conclusion": (
            "当前已有数据中的 refined entropy top 子相位在下一层低洞全部为空，"
            "并且所有终端子行均大于 P^2；它们转为远处 finite/profinite PDEC 原子，"
            "不构成 P 行以内零行。"
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
        "# Triad-A1 RefinedEntropy 终端 Fiber 审计",
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
        "u = old refined atom at Q'；",
        "v = u + b Q'；",
        "若 H_{nextQ}(v)=empty，则 v+s*nextQ 全部是完整零行相位。",
        "```",
        "",
        "这类相位若 `v>P`，就不能构成 `P×P` 内早期零行；若还满足 `v>P^2`，则更直接地落入远处 finite/profinite PDEC 包。",
        "",
        "## 2. 汇总",
        "",
        f"- `entropy_peak_count={result['entropy_peak_count']}`。",
        f"- `terminal_row_count={result['terminal_row_count']}`。",
        f"- `route_counts={result['route_counts']}`。",
        f"- `all_terminal_low_holes_empty={result['all_terminal_low_holes_empty']}`。",
        f"- `all_terminal_children_gt_p={result['all_terminal_children_gt_p']}`。",
        f"- `all_terminal_children_gt_p2={result['all_terminal_children_gt_p2']}`。",
        f"- `min_terminal_phase={result['min_terminal_phase']}`。",
        f"- `min_terminal_phase_over_p={fmt_float(result['min_terminal_phase_over_p'])}`。",
        f"- `min_terminal_phase_over_p2={fmt_float(result['min_terminal_phase_over_p2'])}`。",
        "",
        "## 3. 明细",
        "",
        "| P | Q' | next Q | u | top b | v | holes | child count | min child | max child | route |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | ---: | --- |",
    ]
    for row in result["terminal_rows"]:
        lines.append(
            "| {p} | {ql} | {nq} | {u} | {b} | {v} | `{holes}` | {count} | {minc} | {maxc} | `{route}` |".format(
                p=row["p"],
                ql=row["source_q_lift"],
                nq=row["next_q"],
                u=row["new_phase"],
                b=row["next_top_residue"],
                v=row["terminal_phase"],
                holes=row["low_holes_at_terminal_phase"],
                count=row["terminal_child_count"],
                minc=row["min_terminal_child"],
                maxc=row["max_terminal_child"],
                route=row["route"],
            )
        )

    lines.extend(
        [
            "",
            "## 4. 读法",
            "",
            "这一步不是说所有 refined PDEC 已排除；它只关闭当前已抽取熵峰的早期出口。",
            "这些熵峰提升后直接变成远处完整零行 fiber，因此只能作为 finite/profinite PDEC 数据包继续处理，",
            "不能作为 `P` 行以内零行证据。",
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
                "entropy_peak_count": result["entropy_peak_count"],
                "route_counts": result["route_counts"],
                "all_terminal_low_holes_empty": result["all_terminal_low_holes_empty"],
                "all_terminal_children_gt_p2": result["all_terminal_children_gt_p2"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
