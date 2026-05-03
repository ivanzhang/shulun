#!/usr/bin/env python3
"""物化 H4-PDEC 的 Q=2310 LHB column-cap 相位块。

用法示例：
  python3 experiments/prime_matrix_bpn_lhb_column_phase_blocks.py
  python3 experiments/prime_matrix_bpn_lhb_column_phase_blocks.py --p-values 43,47,53,59,61

输出：
  docs/monograph/h4-pdec-lhb-column-phase-blocks.json
  docs/monograph/h4-pdec-lhb-column-phase-blocks.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from math import prod
from pathlib import Path
from typing import Any

from prime_matrix_bpn_lhb_column_residue_rigidity_audit import (
    affine_rigidity_failures,
    bridge_candidates,
    completion_exists_from_residue_masks,
    residue_capacity,
)
from prime_matrix_bpn_low_hole_bucket_capacity import low_holes_for_phase, primes_upto


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"


def parse_p_values(raw: str) -> list[int]:
    """解析逗号分隔的 P 列表。"""
    return [int(item.strip()) for item in raw.split(",") if item.strip()]


def file_sha256(path: Path) -> str:
    """计算文件 sha256，作为证书来源指纹。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记本证书依赖的脚本指纹。"""
    return {
        "phase_block_script": file_sha256(Path(__file__).resolve()),
        "rigidity_audit_script": file_sha256(
            ROOT / "experiments" / "prime_matrix_bpn_lhb_column_residue_rigidity_audit.py"
        ),
        "capacity_script": file_sha256(
            ROOT / "experiments" / "prime_matrix_bpn_low_hole_bucket_capacity.py"
        ),
    }


def row(
    row_id: str,
    p: int,
    q: int,
    block_name: str,
    phase_block: list[int],
    bound: int,
    source_type: str,
    a_ready: str,
    note: str,
) -> dict[str, Any]:
    """构造一条机器可读 column-cap 行。"""
    return {
        "row_id": row_id,
        "p": p,
        "q": q,
        "phase_block_name": block_name,
        "phase_block": phase_block,
        "phase_block_size": len(phase_block),
        "bound": bound,
        "inequality": "sum_{t in phase_block} g(t) <= bound",
        "source_type": source_type,
        "source_hash_ref": "source_hashes",
        "admissibility": a_ready,
        "pass": len(phase_block) <= bound,
        "note": note,
    }


def scan_prime_phase_blocks(p: int, q: int) -> dict[str, Any]:
    """扫描单个 P，输出 Q=2310 的 column-cap 相位块。"""
    base_primes = primes_upto(p - 1)
    if prod(base_primes) % q != 0:
        raise ValueError(f"q={q} 不整除 P={p} 的根基 CRT 周期")

    low_primes = [prime for prime in base_primes if q % prime == 0]
    high_primes = [prime for prime in base_primes if q % prime != 0]

    affine_failure_phases: list[int] = []
    zero_phases: list[int] = []
    whole_deficit_phases: list[int] = []
    critical_phases: list[int] = []
    bridged_critical_phases: list[int] = []
    unbridged_critical_phases: list[int] = []
    negative_delta_zero_phases: list[int] = []
    bridge_support_histogram: Counter[tuple[int, ...]] = Counter()
    delta_histogram: Counter[int] = Counter()

    for phase in range(q):
        holes = low_holes_for_phase(p, q, low_primes, phase)
        phase_affine_failures = affine_rigidity_failures(p, q, phase, holes, high_primes)
        if phase_affine_failures:
            affine_failure_phases.append(phase)

        capacity, _details = residue_capacity(holes, high_primes)
        delta = len(holes) - capacity
        candidates: list[dict[str, Any]] = []
        if delta > 0:
            completion_exists = False
        elif delta == 0:
            candidates = bridge_candidates(holes, high_primes)
            completion_exists = (
                False if candidates
                else completion_exists_from_residue_masks(holes, high_primes)
            )
        else:
            completion_exists = completion_exists_from_residue_masks(holes, high_primes)

        if completion_exists:
            continue

        zero_phases.append(phase)
        delta_histogram[delta] += 1
        if delta > 0:
            whole_deficit_phases.append(phase)
        elif delta < 0:
            negative_delta_zero_phases.append(phase)
        else:
            critical_phases.append(phase)
            if candidates:
                bridged_critical_phases.append(phase)
                bridge_support_histogram[tuple(candidates[0]["support_primes"])] += 1
            else:
                unbridged_critical_phases.append(phase)

    rows = [
        row(
            f"CC-LHB-AFFINE-Q{q}-P{p}",
            p,
            q,
            "affine_rigidity_failure_phases",
            affine_failure_phases,
            0,
            "FiniteCert",
            "A-ready-empty-anomaly-block",
            "列残基仿射刚性失败相位块；当前证书要求为空。",
        ),
        row(
            f"CC-LHB-NEGDELTA-Q{q}-P{p}",
            p,
            q,
            "negative_delta_zero_phases",
            negative_delta_zero_phases,
            0,
            "FiniteCert",
            "A-ready-empty-anomaly-block",
            "Delta(H)<0 但仍 zero 的异常相位块；当前证书要求为空。",
        ),
        row(
            f"CC-LHB-UNBRIDGED-Q{q}-P{p}",
            p,
            q,
            "unbridged_critical_phases",
            unbridged_critical_phases,
            0,
            "FiniteCert",
            "A-ready-empty-anomaly-block",
            "Delta(H)=0 且无桥洞证书的临界相位块；当前证书要求为空。",
        ),
        row(
            f"CC-LHB-WHOLEDEF-Q{q}-P{p}",
            p,
            q,
            "whole_deficit_phases",
            whole_deficit_phases,
            len(whole_deficit_phases),
            "FiniteCert",
            "diagnostic-phase-support",
            "整洞集 Hall 亏损相位支撑；需结合 S subset Z 后才可转成 A 行。",
        ),
        row(
            f"CC-LHB-BRIDGED-Q{q}-P{p}",
            p,
            q,
            "bridged_critical_phases",
            bridged_critical_phases,
            len(bridged_critical_phases),
            "FiniteCert",
            "diagnostic-phase-support",
            "桥洞临界相位支撑；需按 P 拆行并证明 S 的投影关系。",
        ),
    ]

    return {
        "p": p,
        "q": q,
        "low_primes": low_primes,
        "high_primes": high_primes,
        "summary": {
            "zero_count": len(zero_phases),
            "whole_deficit_count": len(whole_deficit_phases),
            "critical_count": len(critical_phases),
            "bridged_critical_count": len(bridged_critical_phases),
            "unbridged_critical_count": len(unbridged_critical_phases),
            "negative_delta_zero_count": len(negative_delta_zero_phases),
            "affine_failure_count": len(affine_failure_phases),
            "delta_histogram": dict(sorted(delta_histogram.items())),
            "bridge_support_histogram": {
                str(key): value
                for key, value in sorted(bridge_support_histogram.items(), key=lambda item: str(item[0]))
            },
        },
        "rows": rows,
        "zero_phases": zero_phases,
    }


def run(p_values: list[int], q: int) -> dict[str, Any]:
    """运行相位块物化。"""
    prime_results = [scan_prime_phase_blocks(p, q) for p in p_values]
    rows = [item for result in prime_results for item in result["rows"]]
    return {
        "certificate_type": "h4_pdec_lhb_column_phase_blocks",
        "status": "q2310_lhb_column_phase_blocks_materialized_finite_certificate",
        "q": q,
        "p_values": p_values,
        "source_hashes": source_hashes(),
        "rows": rows,
        "prime_results": prime_results,
        "all_empty_anomaly_rows_pass": all(
            item["pass"]
            for item in rows
            if item["admissibility"] == "A-ready-empty-anomaly-block"
        ),
        "review_conclusion": (
            "Q=2310 的 LHB column rows 已输出机器可读 phase_block 与 bound。"
            "空异常块可作为有限 A 行；整洞集亏损与桥洞临界块仍是诊断支撑，"
            "需进一步证明正式坏窗集合 S 的投影关系后才能进入全局 PDEC-Dual-Cert。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写审稿摘要 Markdown；完整相位块保存在 JSON。"""
    lines = [
        "# H4-PDEC Q=2310 LHB Column Phase Blocks",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 来源指纹",
        "",
        "| source | sha256 |",
        "| --- | --- |",
    ]
    for name, digest in result["source_hashes"].items():
        lines.append(f"| `{name}` | `{digest}` |")

    lines.extend(
        [
            "",
            "## 2. P 汇总",
            "",
            "| P | zero | whole deficit | critical | bridged | unbridged | negative delta | affine failures |",
            "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for item in result["prime_results"]:
        summary = item["summary"]
        lines.append(
            "| {p} | {zero} | {whole} | {critical} | {bridged} | {unbridged} | {negative} | {affine} |".format(
                p=item["p"],
                zero=summary["zero_count"],
                whole=summary["whole_deficit_count"],
                critical=summary["critical_count"],
                bridged=summary["bridged_critical_count"],
                unbridged=summary["unbridged_critical_count"],
                negative=summary["negative_delta_zero_count"],
                affine=summary["affine_failure_count"],
            )
        )

    lines.extend(
        [
            "",
            "## 3. 机器行摘要",
            "",
            "| row_id | block | size | bound | admissibility | pass |",
            "| --- | --- | ---: | ---: | --- | --- |",
        ]
    )
    for item in result["rows"]:
        lines.append(
            "| `{row_id}` | `{block}` | {size} | {bound} | `{admissibility}` | `{passed}` |".format(
                row_id=item["row_id"],
                block=item["phase_block_name"],
                size=item["phase_block_size"],
                bound=item["bound"],
                admissibility=item["admissibility"],
                passed=item["pass"],
            )
        )

    lines.extend(
        [
            "",
            "## 4. 审稿边界",
            "",
            "- `A-ready-empty-anomaly-block` 行已经有 `phase_block` 与 `bound=0`；在有限 `Q=2310` 范围内可作为空异常块约束。",
            "- `diagnostic-phase-support` 行只登记支撑相位；若要进入 `A,b,E,e`，还需证明正式坏窗集合 `S` 投影到这些相位块并给出对应容量界。",
            "- 本文件不证明全局 `PDEC exclusion`，也不把有限相位块推广到无限 `P`。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--p-values", default="13,17,19,23,29,31,37,43,47")
    parser.add_argument("--q", type=int, default=2310)
    parser.add_argument(
        "--json-output",
        type=Path,
        default=DOCS / "h4-pdec-lhb-column-phase-blocks.json",
    )
    parser.add_argument(
        "--md-output",
        type=Path,
        default=DOCS / "h4-pdec-lhb-column-phase-blocks.md",
    )
    args = parser.parse_args()
    result = run(parse_p_values(args.p_values), args.q)
    args.json_output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result, args.md_output)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
