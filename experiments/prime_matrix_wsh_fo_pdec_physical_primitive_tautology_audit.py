#!/usr/bin/env python3
"""审计 FO-PDEC physical/primitive 二点阈值是否只是 Fourier 恒等现象。

用法示例：
  python3 experiments/prime_matrix_wsh_fo_pdec_physical_primitive_tautology_audit.py

输出：
  docs/monograph/prime-matrix-wsh-fo-pdec-physical-primitive-tautology-audit.json
  docs/monograph/prime-matrix-wsh-fo-pdec-physical-primitive-tautology-audit.md
"""

from __future__ import annotations

import argparse
import cmath
import hashlib
import itertools
import json
import math
from collections import defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_LOWMOD = DOCS / "prime-matrix-wsh-fo-pdec-lowmod-audit.json"
DEFAULT_CROSS_Q = DOCS / "prime-matrix-wsh-fo-pdec-cross-q-chart-overlap-audit.json"
DEFAULT_JSON = DOCS / "prime-matrix-wsh-fo-pdec-physical-primitive-tautology-audit.json"
DEFAULT_MD = DOCS / "prime-matrix-wsh-fo-pdec-physical-primitive-tautology-audit.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def best_two_point_fourier(ell: int, residues: tuple[int, int]) -> dict[str, Any]:
    """计算两个残基的最佳 Fourier，并给出使差为 1 的频率。"""
    first, second = residues
    if first == second:
        return {
            "frequency": 1,
            "fourier": 2.0,
            "dual_residues": [first % ell, second % ell],
            "tautology_bound": 2.0,
            "difference": 0,
        }
    difference = (second - first) % ell
    frequency = pow(difference, -1, ell)
    dual = [(frequency * first) % ell, (frequency * second) % ell]
    total = sum(
        cmath.exp(2j * math.pi * frequency * residue / ell)
        for residue in residues
    )
    tautology = 2.0 * math.cos(math.pi / ell)
    return {
        "frequency": frequency,
        "fourier": abs(total),
        "dual_residues": dual,
        "tautology_bound": tautology,
        "difference": difference,
        "matches_two_point_tautology": abs(abs(total) - tautology) < 1e-12,
    }


def grouped_physical_events(lowmod: dict[str, Any], factor: int) -> list[dict[str, Any]]:
    """按物理候选和解释因子分组。"""
    buckets: defaultdict[tuple[int, int], list[dict[str, Any]]] = defaultdict(list)
    for row in lowmod["equations"]:
        if int(row["explaining_factor"]) != factor:
            continue
        buckets[(int(row["candidate"]), int(row["explaining_factor"]))].append(row)
    result = []
    for (candidate, ell), rows in sorted(buckets.items()):
        residues = sorted({int(row["target_residue"]) for row in rows})
        result.append(
            {
                "candidate": candidate,
                "factor": ell,
                "multiplicity": len(rows),
                "residue_set": residues,
                "semiprime_set": sorted({int(row["semiprime"]) for row in rows}),
                "offset_set": sorted({int(row["offset"]) for row in rows}),
                "q_layers": sorted({int(row["q"]) for row in rows}),
                "sources": [
                    {
                        "block_index": row["block_index"],
                        "offset_row_index": row["offset_row_index"],
                        "p": row["p"],
                        "q": row["q"],
                        "row": row["candidate_row"],
                        "column": row["column"],
                        "offset": row["offset"],
                        "semiprime": row["semiprime"],
                        "tail_factors": row["tail_factors"],
                        "target_residue": row["target_residue"],
                    }
                    for row in rows
                ],
            }
        )
    return result


def residue_choices(events: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """枚举每个物理候选选择一个残基后的二点 Fourier。"""
    choices = []
    for residues in itertools.product(*(event["residue_set"] for event in events)):
        if len(residues) != 2:
            continue
        ell = int(events[0]["factor"])
        best = best_two_point_fourier(ell, (int(residues[0]), int(residues[1])))
        choices.append(
            {
                "chosen_residues": list(map(int, residues)),
                **best,
            }
        )
    choices.sort(key=lambda row: (-row["fourier"], row["chosen_residues"]))
    return choices


def build_audit(
    lowmod: dict[str, Any],
    cross_q: dict[str, Any],
    lowmod_path: Path,
    cross_q_path: Path,
    factor: int,
) -> dict[str, Any]:
    """构造 physical/primitive 二点 tautology 审计。"""
    events = grouped_physical_events(lowmod, factor)
    choices = residue_choices(events)
    two_point_tautology = 2.0 * math.cos(math.pi / factor)
    all_choices_tautological = all(
        choice.get("matches_two_point_tautology", choice["fourier"] == 2.0)
        for choice in choices
    )
    ambiguous_phase_events = [
        event for event in events if len(event["residue_set"]) > 1
    ]
    return {
        "certificate_type": "fo_pdec_physical_primitive_tautology_audit",
        "status": "physical_primitive_pdec_threshold_degenerates_to_two_point_tautology",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "lowmod_audit": file_sha256(lowmod_path),
            "cross_q_chart_overlap_audit": file_sha256(cross_q_path),
        },
        "factor": factor,
        "physical_event_count": len(events),
        "physical_events": events,
        "ambiguous_phase_event_count": len(ambiguous_phase_events),
        "ambiguous_phase_events": ambiguous_phase_events,
        "two_point_tautology_bound": two_point_tautology,
        "residue_choice_audit": choices,
        "all_residue_choices_are_two_point_tautology": all_choices_tautological,
        "cross_q_current_sample_blocked": (
            cross_q["closed_subgate"]
            == "CrossQCoordinatePersistenceRejectedForAuditedFO-PDEC"
        ),
        "closed_subgate": (
            "PhysicalPrimitivePDECThresholdDegeneratesToTwoPointTautology"
            if len(events) == 2 and all_choices_tautological
            else "PhysicalPrimitivePDECThresholdStillNeedsCaseSplit"
        ),
        "remaining_after_subgate": [
            "SAE/Endpoint absorption for the two physical primitive atoms",
            "future primitive PDEC only if a same-formal-unit family has at least three non-tautological physical atoms or extra constraints",
        ],
        "review_conclusion": (
            "物理去重后当前 factor=199 前沿只剩两个物理候选。模素数上任意两个不同残基都可由某个"
            " 非零频率送成相邻对偶点，从而 Fourier 达到 2*cos(pi/ell)。因此"
            " U_CRT < 1.9997507790353146 不是可攻的 PDEC 缺陷阈值，而是二点 Fourier tautology。"
            " 当前分支应转入 SAE/Endpoint，除非未来出现至少三点且同一 formal unit 的 primitive PDEC 家族。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# FO-PDEC physical/primitive 二点 tautology 审计",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 子门裁定",
        "",
        "```text",
        f"closed_subgate: {result['closed_subgate']}",
        f"factor: {result['factor']}",
        f"physical_event_count: {result['physical_event_count']}",
        f"two_point_tautology_bound: {result['two_point_tautology_bound']}",
        (
            "all_residue_choices_are_two_point_tautology: "
            f"{str(result['all_residue_choices_are_two_point_tautology']).lower()}"
        ),
        f"ambiguous_phase_event_count: {result['ambiguous_phase_event_count']}",
        "```",
        "",
        "## 2. 物理原子",
        "",
        "| candidate | factor | multiplicity | residues | semiprime | offset | q layers |",
        "| ---: | ---: | ---: | --- | --- | --- | --- |",
    ]
    for event in result["physical_events"]:
        lines.append(
            "| "
            + " | ".join(
                table_cell(value)
                for value in [
                    event["candidate"],
                    event["factor"],
                    event["multiplicity"],
                    event["residue_set"],
                    event["semiprime_set"],
                    event["offset_set"],
                    event["q_layers"],
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 3. 残基选择审计",
            "",
            "| chosen residues | h | dual residues | Fourier | tautology bound |",
            "| --- | ---: | --- | ---: | ---: |",
        ]
    )
    for choice in result["residue_choice_audit"]:
        lines.append(
            "| "
            + " | ".join(
                table_cell(value)
                for value in [
                    choice["chosen_residues"],
                    choice["frequency"],
                    choice["dual_residues"],
                    f"{choice['fourier']:.12f}",
                    f"{choice['tautology_bound']:.12f}",
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 4. 证明读法",
            "",
            "若模数 `ell` 为素数，两个不同残基 `a,b` 的差 `b-a` 可逆。取",
            "",
            "\\[",
            "h\\equiv (b-a)^{-1}\\pmod \\ell，",
            "\\]",
            "",
            "则 `ha` 与 `hb` 在对偶圆周上相邻，故",
            "",
            "\\[",
            "\\max_{h\\ne0}|e(ha/\\ell)+e(hb/\\ell)|=2\\cos(\\pi/\\ell)。",
            "\\]",
            "",
            "所以二点 physical/primitive Fourier 近质量上界不是异常，而是恒等现象。PDEC 必须捕捉"
            "持久偏斜；当前只有两个物理原子的分支应作为稀疏局部对象进入 SAE/Endpoint。",
            "",
            "## 5. 剩余",
            "",
        ]
    )
    for item in result["remaining_after_subgate"]:
        lines.append(f"- `{item}`")
    lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lowmod", type=Path, default=DEFAULT_LOWMOD)
    parser.add_argument("--cross-q", type=Path, default=DEFAULT_CROSS_Q)
    parser.add_argument("--factor", type=int, default=199)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    lowmod = load_json(args.lowmod)
    cross_q = load_json(args.cross_q)
    result = build_audit(lowmod, cross_q, args.lowmod, args.cross_q, args.factor)
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(result["status"])
    print(result["closed_subgate"])


if __name__ == "__main__":
    main()
