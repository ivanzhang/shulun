#!/usr/bin/env python3
"""审计固定 m 的 q-prefix line atom 是否具备逐 atom 相位节省。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_qprefix_line_atom_phase_coherence_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-qprefix-line-atom-phase-coherence-audit.json

本脚本承接 q-prefix atom 分解。对每个固定 m、连续 prime-q prefix atom，
直接计算

  S_A(h)=sum_{q in A} exp(2*pi*i*h*P*floor(q*m/P)/q)
        =sum_{q in A} exp(-2*pi*i*h*(q*m mod P)/q).

审计目的不是证明相位节省，而是判断“每个 line atom 自己给出相消”
是否可作为下一门。若大量 atom 很短或近相干，则下一门必须改写为：
短 atom 聚合吸收 + 长 atom 的 completed trace/Kloosterman family。
"""

from __future__ import annotations

import cmath
import hashlib
import json
import math
import statistics
import sys
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"
sys.path.insert(0, str(ROOT / "experiments"))

import prime_matrix_phi_lpf_qsupport_dynamic_primorial_unit_selector_audit as primorial  # noqa: E402
import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_atom_audit as qatom  # noqa: E402
import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_right_tail_endpoint_collar_audit as collar  # noqa: E402
import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_shell_step_packet_audit as shell_step  # noqa: E402


SLUG = "prime-matrix-phi-lpf-qprefix-line-atom-phase-coherence"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-06-03"
H_VALUES = [1, 2, 3, 5]

DEPENDENCIES = [
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-atom-audit.json",
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-unification-audit.json",
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-shell-step-packet-audit.json",
    DOCS / "external-theorem-index.md",
    DOCS / "claim-status-table.md",
    DOCS / "frontier-honest-status-and-true-side-theorems-20260522.md",
    ROOT / "paper" / "contradiction-field-monograph" / "contradiction-field-monograph.tex",
]


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    paths = [Path(__file__).resolve(), *DEPENDENCIES]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def gate(name: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造门控记录。"""
    return {
        "gate": name,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def phase_sum(P: int, m: int, q_values: list[int], h: int) -> complex:
    """计算固定 m、prime-q prefix 上的实际相位和。"""
    total = 0j
    for q in q_values:
        k = (q * m) // P
        total += cmath.exp(2j * math.pi * h * P * k / q)
    return total


def phase_range(P: int, m: int, q_values: list[int], h: int) -> float:
    """粗略记录相位角跨度；只用于有限诊断。"""
    if not q_values:
        return 0.0
    angles = []
    for q in q_values:
        k = (q * m) // P
        angles.append((h * P * k / q) % 1.0)
    return max(angles) - min(angles)


def iter_atoms(max_prime: int = 1009) -> list[dict[str, Any]]:
    """复用上一层分解，列出所有固定 m 的 q-prefix line atoms。"""
    primes = primorial.prime_sieve(2 * max_prime + 10)
    packets = shell_step.packetize_rectangles(max_prime)
    fibres_by_row = collar.right_tail_fibres_by_row(max_prime, primes)
    atoms: list[dict[str, Any]] = []

    for packet_index, packet in enumerate(packets):
        profile = qatom.endpoint_profile_for_packet(packet, fibres_by_row, primes)
        m_values = sorted(qatom.endpoint_flux.packet_shell_values(packet, primes))
        q_values = [q for q in primes if packet["q_start"] <= q <= packet["q_end"]]
        for m_value in m_values:
            atoms.append(
                {
                    "packet_index": packet_index,
                    "P": packet["P"],
                    "strip": packet["strip"],
                    "endpoint_flux_class": profile["endpoint_flux_class"],
                    "m": m_value,
                    "q_start": packet["q_start"],
                    "q_end": packet["q_end"],
                    "q_values": q_values,
                    "q_prefix_count": len(q_values),
                }
            )
    return atoms


def h_summary(atoms: list[dict[str, Any]], h: int) -> dict[str, Any]:
    """汇总单个 h 的相干统计。"""
    ratios: list[float] = []
    sqrt_ratios: list[float] = []
    abs_values: list[float] = []
    top: list[dict[str, Any]] = []
    coherent_counts = Counter()

    for atom in atoms:
        q_values = atom["q_values"]
        length = len(q_values)
        value = phase_sum(atom["P"], atom["m"], q_values, h)
        abs_value = abs(value)
        ratio = abs_value / length if length else 0.0
        sqrt_ratio = abs_value / math.sqrt(length) if length else 0.0
        ratios.append(ratio)
        sqrt_ratios.append(sqrt_ratio)
        abs_values.append(abs_value)
        coherent_counts["ratio_ge_0_90"] += int(ratio >= 0.90)
        coherent_counts["ratio_ge_0_75"] += int(ratio >= 0.75)
        coherent_counts["ratio_ge_0_50"] += int(ratio >= 0.50)
        coherent_counts["sqrt_ratio_ge_2"] += int(sqrt_ratio >= 2.0)
        coherent_counts["sqrt_ratio_ge_3"] += int(sqrt_ratio >= 3.0)
        top.append(
            {
                "P": atom["P"],
                "m": atom["m"],
                "strip": atom["strip"],
                "endpoint_flux_class": atom["endpoint_flux_class"],
                "q_start": atom["q_start"],
                "q_end": atom["q_end"],
                "q_prefix_count": length,
                "abs_sum": round(abs_value, 6),
                "abs_over_length": round(ratio, 6),
                "abs_over_sqrt_length": round(sqrt_ratio, 6),
                "phase_range_mod_1": round(phase_range(atom["P"], atom["m"], q_values, h), 6),
                "q_sample": q_values[:8],
            }
        )

    top.sort(key=lambda row: (row["abs_over_length"], row["q_prefix_count"]), reverse=True)
    return {
        "h": h,
        "sum_abs": round(sum(abs_values), 6),
        "mean_abs_over_length": round(statistics.mean(ratios), 6),
        "median_abs_over_length": round(statistics.median(ratios), 6),
        "max_abs_over_length": round(max(ratios), 6),
        "mean_abs_over_sqrt_length": round(statistics.mean(sqrt_ratios), 6),
        "median_abs_over_sqrt_length": round(statistics.median(sqrt_ratios), 6),
        "max_abs_over_sqrt_length": round(max(sqrt_ratios), 6),
        **dict(coherent_counts),
        "top_coherent_atoms": top[:10],
    }


def audit(max_prime: int = 1009) -> dict[str, Any]:
    """执行 q-prefix line atom 相干审计。"""
    atoms = iter_atoms(max_prime)
    q_counts = [atom["q_prefix_count"] for atom in atoms]
    short_count = sum(1 for value in q_counts if value <= 4)
    long_count = sum(1 for value in q_counts if value >= 17)
    by_q_bin = Counter(qatom.q_bin(value) for value in q_counts)
    by_strip = Counter(atom["strip"] for atom in atoms)
    h_summaries = [h_summary(atoms, h) for h in H_VALUES]
    h1 = h_summaries[0]

    return {
        "max_prime": max_prime,
        "h_values": H_VALUES,
        "atom_count_total": len(atoms),
        "edge_count_total": sum(q_counts),
        "q_prefix_count_min": min(q_counts),
        "q_prefix_count_median": statistics.median(q_counts),
        "q_prefix_count_max": max(q_counts),
        "short_atom_count_q_le_4": short_count,
        "short_atom_ratio_q_le_4": round(short_count / len(atoms), 6),
        "long_atom_count_q_ge_17": long_count,
        "long_atom_ratio_q_ge_17": round(long_count / len(atoms), 6),
        "q_prefix_bin_counts": dict(sorted(by_q_bin.items())),
        "strip_counts": dict(sorted(by_strip.items())),
        "h_summaries": h_summaries,
        "h1_ratio_ge_0_90": h1["ratio_ge_0_90"],
        "h1_ratio_ge_0_75": h1["ratio_ge_0_75"],
        "h1_ratio_ge_0_50": h1["ratio_ge_0_50"],
        "h1_sqrt_ratio_ge_2": h1["sqrt_ratio_ge_2"],
        "h1_sqrt_ratio_ge_3": h1["sqrt_ratio_ge_3"],
        "atomwise_phase_saving_route_closed": False,
        "short_atom_aggregation_needed": short_count > 0,
        "long_atom_trace_completion_needed": long_count > 0,
    }


def markdown_table(rows: list[dict[str, Any]], fields: list[str]) -> list[str]:
    """生成简单 Markdown 表格。"""
    lines = [
        "| " + " | ".join(fields) + " |",
        "| " + " | ".join(["---"] * len(fields)) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(str(row.get(field, "")) for field in fields) + " |")
    return lines


def dict_table(mapping: dict[str, Any], key_name: str, value_name: str) -> list[dict[str, Any]]:
    """把字典转换成 Markdown 表格行。"""
    return [{key_name: key, value_name: value} for key, value in sorted(mapping.items())]


def build_payload() -> dict[str, Any]:
    """构造完整证书 payload。"""
    finite_audit = audit()
    return {
        "certificate_type": "prime_matrix_phi_lpf_qprefix_line_atom_phase_coherence_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "qprefix_line_atom_phase_coherence_blocks_atomwise_saving_route",
        "chosen_claim": "Prime Matrix row/column Phi-LPF",
        "current_object": {
            "phase": "S_A(h)=sum_{q in A} e(h*P*floor(q*m/P)/q)=sum_{q in A} e(-h*(q*m mod P)/q)",
            "atom": "fixed m and contiguous prime-q prefix from endpoint-flux atomization",
            "tested_h_values": H_VALUES,
        },
        "finite_audit": finite_audit,
        "closed_gates": [
            gate(
                "QPrefixLineAtomPhaseIdentity",
                True,
                True,
                "The fixed-m atom phase is exactly e(h*P*floor(q*m/P)/q).",
                "none",
            ),
            gate(
                "AtomwiseQPrefixPhaseSavingRoute",
                False,
                False,
                "Per-atom cancellation is not a valid standalone route for the current atom family.",
                "short atoms and coherent atoms require aggregation or a stronger trace family",
            ),
            gate(
                "ShortAtomAggregationGate",
                False,
                False,
                "Atoms with very short q-prefix cannot create internal cancellation.",
                "aggregate short atoms with signed weights or absorb them by a separate budget",
            ),
            gate(
                "LongAtomMovingDenominatorTraceGate",
                False,
                False,
                "Longer atoms still have moving prime denominator q and are not yet a completed trace/Kloosterman family.",
                "construct completed moving-q denominator trace family",
            ),
        ],
        "latest_narrowest_mouth": [
            "ShortQPrefixAtomSignedAggregationOrBudgetAbsorption",
            "AND LongQPrefixMovingPrimeDenominatorTraceCompletion",
            "AND NoLossAggregationAcrossQPrefixAtoms",
            "AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity",
        ],
        "atomwise_qprefix_phase_saving_closed": False,
        "short_atom_aggregation_closed": False,
        "long_atom_trace_completion_closed": False,
        "no_loss_qprefix_atom_aggregation_closed": False,
        "phi_lpf_parity_barrier_globally_broken": False,
        "row_column_unconditional_closed": False,
        "source_hashes": source_hashes(),
    }


def build_markdown(payload: dict[str, Any]) -> str:
    """生成 Markdown 证书。"""
    audit_payload = payload["finite_audit"]
    h_rows = [
        {
            key: item[key]
            for key in [
                "h",
                "sum_abs",
                "median_abs_over_length",
                "max_abs_over_length",
                "median_abs_over_sqrt_length",
                "max_abs_over_sqrt_length",
                "ratio_ge_0_90",
                "sqrt_ratio_ge_3",
            ]
        }
        for item in audit_payload["h_summaries"]
    ]
    top_h1 = audit_payload["h_summaries"][0]["top_coherent_atoms"]
    current = payload["current_object"]
    lines = [
        "# Prime Matrix Phi-LPF q-prefix line atom phase coherence 审计",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['frontier_verified_date']}`",
        "",
        "## 1. 当前对象",
        "",
        "```text",
        f"phase={current['phase']}",
        f"atom={current['atom']}",
        f"tested_h_values={current['tested_h_values']}",
        "```",
        "",
        "## 2. 有限相干审计",
        "",
        "```text",
        f"max_prime={audit_payload['max_prime']}",
        f"atom_count_total={audit_payload['atom_count_total']}",
        f"edge_count_total={audit_payload['edge_count_total']}",
        f"q_prefix_count_min={audit_payload['q_prefix_count_min']}",
        f"q_prefix_count_median={audit_payload['q_prefix_count_median']}",
        f"q_prefix_count_max={audit_payload['q_prefix_count_max']}",
        f"short_atom_count_q_le_4={audit_payload['short_atom_count_q_le_4']}",
        f"short_atom_ratio_q_le_4={audit_payload['short_atom_ratio_q_le_4']}",
        f"long_atom_count_q_ge_17={audit_payload['long_atom_count_q_ge_17']}",
        f"long_atom_ratio_q_ge_17={audit_payload['long_atom_ratio_q_ge_17']}",
        f"h1_ratio_ge_0_90={audit_payload['h1_ratio_ge_0_90']}",
        f"h1_ratio_ge_0_75={audit_payload['h1_ratio_ge_0_75']}",
        f"h1_ratio_ge_0_50={audit_payload['h1_ratio_ge_0_50']}",
        f"h1_sqrt_ratio_ge_2={audit_payload['h1_sqrt_ratio_ge_2']}",
        f"h1_sqrt_ratio_ge_3={audit_payload['h1_sqrt_ratio_ge_3']}",
        "```",
        "",
        "q-prefix 长度分桶：",
        "",
        *markdown_table(dict_table(audit_payload["q_prefix_bin_counts"], "q_prefix_bin", "atom_count"), ["q_prefix_bin", "atom_count"]),
        "",
        "h 汇总：",
        "",
        *markdown_table(
            h_rows,
            [
                "h",
                "sum_abs",
                "median_abs_over_length",
                "max_abs_over_length",
                "median_abs_over_sqrt_length",
                "max_abs_over_sqrt_length",
                "ratio_ge_0_90",
                "sqrt_ratio_ge_3",
            ],
        ),
        "",
        "h=1 近相干样例：",
        "",
        *markdown_table(
            top_h1,
            [
                "P",
                "m",
                "strip",
                "q_start",
                "q_end",
                "q_prefix_count",
                "abs_sum",
                "abs_over_length",
                "abs_over_sqrt_length",
                "phase_range_mod_1",
            ],
        ),
        "",
        "## 3. 判定",
        "",
        "逐 atom 相消不能作为独立闭合门：当前 atom family 含大量极短 prime-q prefix，",
        "这些 atom 内部没有足够长度产生 cancellation；同时有限审计中存在多个 h=1",
        "近相干 atom。故下一门应二分为短 atom 的带符号聚合/预算吸收，和长 atom",
        "的 moving-prime-denominator completed trace/Kloosterman family。",
        "",
        "## 4. 门控表",
        "",
        *markdown_table(payload["closed_gates"], ["gate", "closed", "proved", "meaning", "remaining"]),
        "",
        "## 5. 最新最窄口",
        "",
        "```text",
        *payload["latest_narrowest_mouth"],
        "```",
        "",
        "状态边界：",
        "",
        "```text",
        f"atomwise_qprefix_phase_saving_closed={str(payload['atomwise_qprefix_phase_saving_closed']).lower()}",
        f"short_atom_aggregation_closed={str(payload['short_atom_aggregation_closed']).lower()}",
        f"long_atom_trace_completion_closed={str(payload['long_atom_trace_completion_closed']).lower()}",
        f"no_loss_qprefix_atom_aggregation_closed={str(payload['no_loss_qprefix_atom_aggregation_closed']).lower()}",
        f"phi_lpf_parity_barrier_globally_broken={str(payload['phi_lpf_parity_barrier_globally_broken']).lower()}",
        f"row_column_unconditional_closed={str(payload['row_column_unconditional_closed']).lower()}",
        "```",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    """写出 ledger、JSON 与 Markdown 证书。"""
    payload = build_payload()
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    text = json.dumps(payload, indent=2, sort_keys=True)
    OUT_LEDGER.write_text(text + "\n", encoding="utf-8")
    OUT_JSON.write_text(text + "\n", encoding="utf-8")
    OUT_MD.write_text(build_markdown(payload), encoding="utf-8")
    print(f"wrote {OUT_LEDGER.relative_to(ROOT)}")
    print(f"wrote {OUT_JSON.relative_to(ROOT)}")
    print(f"wrote {OUT_MD.relative_to(ROOT)}")
    print(f"atom_count_total={payload['finite_audit']['atom_count_total']}")
    print(f"h1_ratio_ge_0_90={payload['finite_audit']['h1_ratio_ge_0_90']}")
    print(f"atomwise_qprefix_phase_saving_closed={payload['atomwise_qprefix_phase_saving_closed']}")
    print(f"row_column_unconditional_closed={payload['row_column_unconditional_closed']}")


if __name__ == "__main__":
    main()
