#!/usr/bin/env python3
"""物化 squarefree PDEC 阈值包的跨模数符号配对账本。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_squarefree_pdec_pairing_ledger_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-squarefree-pdec-pairing-ledger-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-squarefree-pdec-pairing-ledger-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-squarefree-pdec-pairing-ledger-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import defaultdict
from pathlib import Path
from typing import Any

import prime_matrix_square_phase_lowalpha_squarefree_pdec_cancellation_router as cancellation


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-squarefree-pdec-pairing-ledger-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-squarefree-pdec-pairing-ledger-router.md"

DEFAULT_P_LIST = cancellation.DEFAULT_P_LIST
DEFAULT_Z_LIST = cancellation.DEFAULT_Z_LIST
DEFAULT_D_LEVEL = cancellation.DEFAULT_D_LEVEL
DEFAULT_ABS_CONTRIBUTION = cancellation.DEFAULT_ABS_CONTRIBUTION
NEXT_TARGET = "StructuralCrossModulusPartnerInvariantOrResidualSignedPDECExclusion"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-squarefree-pdec-cancellation-router.json",
    "prime-matrix-square-phase-lowalpha-selberg-remainder-attribution-router.json",
]


def parse_int_list(text: str) -> list[int]:
    """解析整数列表。"""
    return [int(part) for part in text.split(",") if part.strip()]


def safe_ratio(numerator: float, denominator: float) -> float | None:
    """计算安全比值。"""
    if denominator <= 0:
        return None
    return numerator / denominator


def fmt_float(value: float | None) -> str:
    """格式化浮点数。"""
    if value is None:
        return "n/a"
    return f"{value:.6f}"


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def file_sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖哈希。"""
    result = {
        "experiments/prime_matrix_square_phase_lowalpha_squarefree_pdec_pairing_ledger_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def greedy_pair_z(z: int, packets: list[dict[str, Any]]) -> dict[str, Any]:
    """对单个 z 层做正负阈值包贪心配对。"""
    positives = [
        {"m": item["m"], "mass": float(item["abs_contribution"])}
        for item in packets
        if int(item["z"]) == z and item["contribution_sign"] > 0
    ]
    negatives = [
        {"m": item["m"], "mass": float(item["abs_contribution"])}
        for item in packets
        if int(item["z"]) == z and item["contribution_sign"] < 0
    ]
    positives.sort(key=lambda item: (-item["mass"], item["m"]))
    negatives.sort(key=lambda item: (-item["mass"], item["m"]))
    pos_total = sum(item["mass"] for item in positives)
    neg_total = sum(item["mass"] for item in negatives)
    i = 0
    j = 0
    edges = []
    pos_remaining = positives[0]["mass"] if positives else 0.0
    neg_remaining = negatives[0]["mass"] if negatives else 0.0
    while i < len(positives) and j < len(negatives):
        amount = min(pos_remaining, neg_remaining)
        edges.append(
            {
                "z": z,
                "positive_m": positives[i]["m"],
                "negative_m": negatives[j]["m"],
                "paired_amount": amount,
            }
        )
        pos_remaining -= amount
        neg_remaining -= amount
        if pos_remaining <= 1e-12:
            i += 1
            pos_remaining = positives[i]["mass"] if i < len(positives) else 0.0
        if neg_remaining <= 1e-12:
            j += 1
            neg_remaining = negatives[j]["mass"] if j < len(negatives) else 0.0
    residual_side = "positive" if pos_total > neg_total else "negative" if neg_total > pos_total else "balanced"
    residual_amount = abs(pos_total - neg_total)
    total_abs = pos_total + neg_total
    paired_mass = 2.0 * min(pos_total, neg_total)
    return {
        "z": z,
        "positive_packet_count": len(positives),
        "negative_packet_count": len(negatives),
        "positive_abs": pos_total,
        "negative_abs": neg_total,
        "paired_mass": paired_mass,
        "residual_side": residual_side,
        "residual_amount": residual_amount,
        "residual_over_abs": safe_ratio(residual_amount, total_abs),
        "edge_count": len(edges),
        "top_edges": sorted(edges, key=lambda item: -item["paired_amount"])[:16],
    }


def summarize_edges(z_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """汇总跨 z 重复出现的配对边。"""
    grouped: dict[tuple[int, int], list[dict[str, Any]]] = defaultdict(list)
    for row in z_rows:
        for edge in row["top_edges"]:
            grouped[(int(edge["positive_m"]), int(edge["negative_m"]))].append(edge)
    summaries = []
    for (positive_m, negative_m), edges in grouped.items():
        summaries.append(
            {
                "positive_m": positive_m,
                "negative_m": negative_m,
                "z_values": [int(edge["z"]) for edge in edges],
                "occurrence_count": len(edges),
                "total_paired_amount": sum(float(edge["paired_amount"]) for edge in edges),
                "max_paired_amount": max(float(edge["paired_amount"]) for edge in edges),
            }
        )
    return sorted(summaries, key=lambda item: (-item["occurrence_count"], -item["total_paired_amount"]))


def audit(p_list: list[int], z_list: list[int], d_level: int, abs_contribution: float) -> dict[str, Any]:
    """执行跨模数配对审计。"""
    packets, _metadata = cancellation.all_threshold_packets(p_list, z_list, d_level, abs_contribution)
    z_rows = [greedy_pair_z(z, packets) for z in z_list]
    edge_summaries = summarize_edges(z_rows)
    total_abs = sum(row["positive_abs"] + row["negative_abs"] for row in z_rows)
    total_residual = sum(row["residual_amount"] for row in z_rows)
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_squarefree_pdec_pairing_ledger_router",
        "status": "cross_modulus_pairing_ledger_materialized_structural_invariant_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "pairing_ledger_materialized": True,
        "all_threshold_packet_mass_pairable_except_signed_residual": True,
        "structural_cross_modulus_partner_invariant_proved": False,
        "residual_signed_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "abs_contribution_threshold": abs_contribution,
        "total_threshold_abs_mass": total_abs,
        "total_residual_mass_after_pairing": total_residual,
        "total_residual_over_abs": safe_ratio(total_residual, total_abs),
        "z_pairing_rows": z_rows,
        "recurrent_pair_edges": edge_summaries[:24],
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "同一 `m` 纵向自取消被排除后，阈值包的可见取消只能在同一 `z` 层跨不同模数发生。"
            "本账本把每层正负包配对成边，并把未配对量压成 signed residual。"
            "这一步闭合的是算术收费格式：除 signed residual 外，所有阈值质量都可被异号包账面配对；"
            "尚未闭合的是这些配对边为何由结构强制、以及 residual 是否必然形成 PDEC/SAE。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha squarefree PDEC 跨模数配对账本",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"pairing_ledger_materialized={fmt_bool(result['pairing_ledger_materialized'])}",
        (
            "all_threshold_packet_mass_pairable_except_signed_residual="
            f"{fmt_bool(result['all_threshold_packet_mass_pairable_except_signed_residual'])}"
        ),
        f"structural_cross_modulus_partner_invariant_proved={fmt_bool(result['structural_cross_modulus_partner_invariant_proved'])}",
        f"residual_signed_pdec_excluded={fmt_bool(result['residual_signed_pdec_excluded'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 配对总览",
        "",
        "| total abs | residual after pairing | residual/abs |",
        "| ---: | ---: | ---: |",
        (
            f"| {fmt_float(result['total_threshold_abs_mass'])} | "
            f"{fmt_float(result['total_residual_mass_after_pairing'])} | "
            f"{fmt_float(result['total_residual_over_abs'])} |"
        ),
        "",
        "## 2. 分层配对",
        "",
        "| z | + packets | - packets | + abs | - abs | paired mass | residual side | residual | residual/abs | edges |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | ---: |",
    ]
    for row in result["z_pairing_rows"]:
        lines.append(
            f"| {row['z']} | {row['positive_packet_count']} | {row['negative_packet_count']} | "
            f"{fmt_float(row['positive_abs'])} | {fmt_float(row['negative_abs'])} | "
            f"{fmt_float(row['paired_mass'])} | `{row['residual_side']}` | "
            f"{fmt_float(row['residual_amount'])} | {fmt_float(row['residual_over_abs'])} | "
            f"{row['edge_count']} |"
        )
    lines.extend(
        [
            "",
            "## 3. 重复配对边",
            "",
            "| +m | -m | z values | occurrences | total paired | max paired |",
            "| ---: | ---: | --- | ---: | ---: | ---: |",
        ]
    )
    for edge in result["recurrent_pair_edges"]:
        lines.append(
            f"| {edge['positive_m']} | {edge['negative_m']} | `{edge['z_values']}` | "
            f"{edge['occurrence_count']} | {fmt_float(edge['total_paired_amount'])} | "
            f"{fmt_float(edge['max_paired_amount'])} |"
        )
    lines.extend(
        [
            "",
            "## 4. 证明边界",
            "",
            "- 已物化：每个 `z` 层阈值包的正负配对边和 residual。",
            "- 已压缩：若能证明配对边有统一结构不变量，则 coefficient cancellation 可进入定理化预算。",
            "- 未闭合：当前配对是账本配对，不是结构证明。",
            "- 未闭合：若结构配对失败，需证明 residual 触发 `PDEC/SAE/ColumnCRT`，或排斥 residual signed PDEC。",
            f"- 下一目标：`{result['next_direct_attack_target']}`。",
            "",
            "## 5. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for name, digest in sorted(result["source_hashes"].items()):
        lines.append(f"| `{name}` | `{digest}` |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--p-list", default=",".join(str(item) for item in DEFAULT_P_LIST))
    parser.add_argument("--z-list", default=",".join(str(item) for item in DEFAULT_Z_LIST))
    parser.add_argument("--d-level", type=int, default=DEFAULT_D_LEVEL)
    parser.add_argument("--abs-contribution", type=float, default=DEFAULT_ABS_CONTRIBUTION)
    args = parser.parse_args()
    result = audit(
        parse_int_list(args.p_list),
        parse_int_list(args.z_list),
        args.d_level,
        args.abs_contribution,
    )
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result)
    print(
        json.dumps(
            {
                "status": result["status"],
                "total_residual_over_abs": result["total_residual_over_abs"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        ),
        flush=True,
    )


if __name__ == "__main__":
    main()
