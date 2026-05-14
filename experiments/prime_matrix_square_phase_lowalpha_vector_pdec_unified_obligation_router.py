#!/usr/bin/env python3
"""统一登记 core channel 与 low-overflow edge 的 VectorSquarefree-PDEC 义务。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_vector_pdec_unified_obligation_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-vector-pdec-unified-obligation-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-vector-pdec-unified-obligation-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-vector-pdec-unified-obligation-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
CORE_JSON = DOCS / "prime-matrix-square-phase-lowalpha-core-channel-decomposition-router.json"
EDGE_JSON = DOCS / "prime-matrix-square-phase-lowalpha-low-overflow-edge-profile-router.json"
SPLIT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-coefficient-formula-split-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-vector-pdec-unified-obligation-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-vector-pdec-unified-obligation-router.md"

NEXT_TARGET = "MöbiusDivisorSumChannelBoundsAndBoundaryLCMEdgeBoundsOrUnifiedVectorPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-core-channel-decomposition-router.json",
    "prime-matrix-square-phase-lowalpha-low-overflow-edge-profile-router.json",
    "prime-matrix-square-phase-lowalpha-coefficient-formula-split-router.json",
]


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
        "experiments/prime_matrix_square_phase_lowalpha_vector_pdec_unified_obligation_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def core_obligations(core: dict[str, Any]) -> list[dict[str, Any]]:
    """从 core channel 账本抽取统一义务。"""
    obligations = []
    for row in core["rows"]:
        z = int(row["z"])
        obligations.append(
            {
                "family": "CoreS0MobiusDivisorSum",
                "z": z,
                "label": f"S0(z={z})",
                "sample_signed_value": row["S0"],
                "sample_abs_scale": abs(row["S0"]),
                "sample_ratio": row["core_net_over_channel_abs"],
                "required_proof": "Bound truncated Möbius divisor-sum discrepancy or route failure to PDEC",
            }
        )
        for channel in row["top_prime_channels"][:8]:
            obligations.append(
                {
                    "family": "PrimeLogSquareChannel",
                    "z": z,
                    "label": f"S_q(z={z},q={channel['prime']})",
                    "prime": channel["prime"],
                    "sample_signed_value": channel["S_q"],
                    "sample_abs_scale": abs(channel["weighted_term"]),
                    "sample_ratio": abs(channel["weighted_term"])
                    / row["channel_abs_sum"]
                    if row["channel_abs_sum"] > 0
                    else None,
                    "required_proof": "Bound prime-conditioned Möbius divisor-sum discrepancy or route failure to PDEC",
                }
            )
    return obligations


def edge_obligations(edge: dict[str, Any]) -> list[dict[str, Any]]:
    """从 low-overflow edge 账本抽取统一义务。"""
    obligations = []
    for row in edge["rows"]:
        z = int(row["z"])
        if row["total_low_overflow_edge"]["edge_count"] <= 0:
            continue
        obligations.append(
            {
                "family": "CoprimeBoundaryLCMEdge",
                "z": z,
                "label": f"coprime-boundary-edge(z={z})",
                "sample_signed_value": row["coprime_edge"]["signed_edge_contribution"],
                "sample_abs_scale": row["coprime_edge"]["abs_edge_contribution"],
                "sample_ratio": row["coprime_abs_share"],
                "required_proof": "Bound coprime boundary lcm edge angle or route failure to BoundaryLCM-PDEC",
            }
        )
        obligations.append(
            {
                "family": "SmallGCDOverflowEdge",
                "z": z,
                "label": f"small-gcd-overflow-edge(z={z})",
                "sample_signed_value": row["noncoprime_edge"]["signed_edge_contribution"],
                "sample_abs_scale": row["noncoprime_edge"]["abs_edge_contribution"],
                "sample_ratio": 1.0 - row["coprime_abs_share"]
                if row["coprime_abs_share"] is not None
                else None,
                "required_proof": "Absorb small-gcd overflow by gcd-sum budget or route failure to PDEC",
            }
        )
    return obligations


def audit() -> dict[str, Any]:
    """统一义务登记。"""
    core = json.loads(CORE_JSON.read_text(encoding="utf-8"))
    edge = json.loads(EDGE_JSON.read_text(encoding="utf-8"))
    split = json.loads(SPLIT_JSON.read_text(encoding="utf-8"))
    obligations = core_obligations(core) + edge_obligations(edge)
    by_family: dict[str, dict[str, Any]] = {}
    for obligation in obligations:
        family = obligation["family"]
        row = by_family.setdefault(
            family,
            {
                "family": family,
                "obligation_count": 0,
                "total_sample_abs_scale": 0.0,
                "max_sample_abs_scale": 0.0,
                "sample_labels": [],
            },
        )
        row["obligation_count"] += 1
        row["total_sample_abs_scale"] += float(obligation["sample_abs_scale"] or 0.0)
        row["max_sample_abs_scale"] = max(row["max_sample_abs_scale"], float(obligation["sample_abs_scale"] or 0.0))
        if len(row["sample_labels"]) < 8:
            row["sample_labels"].append(obligation["label"])
    families = sorted(by_family.values(), key=lambda row: -row["total_sample_abs_scale"])
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_vector_pdec_unified_obligation_router",
        "status": "unified_vector_pdec_obligations_materialized_bounds_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "unified_vector_pdec_obligation_schema_closed": True,
        "core_channel_obligations_imported": True,
        "low_overflow_edge_obligations_imported": True,
        "mobius_divisor_sum_channel_bounds_proved": False,
        "boundary_lcm_edge_bounds_proved": False,
        "unified_vector_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "equal_split_angle_target": split["tightest_equal_split_angle_row"]["required_equal_split_angle"],
        "obligation_count": len(obligations),
        "family_summaries": families,
        "top_obligations": sorted(obligations, key=lambda row: -float(row["sample_abs_scale"] or 0.0))[:32],
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "core 的 `S0/S_q` 通道与 tail 的 low-overflow `(d,e)` 边界通道现在共用同一个 "
            "VectorSquarefree-PDEC 义务格式：每个义务都有 family、z、label、样本尺度与待证明界。"
            "这一步不证明排斥，但切断了继续分叉：剩余只需证明 Möbius divisor-sum 通道界、"
            "boundary lcm edge 界，或排斥统一的 VectorSquarefree-PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha VectorSquarefree-PDEC 统一义务",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"unified_vector_pdec_obligation_schema_closed={fmt_bool(result['unified_vector_pdec_obligation_schema_closed'])}",
        f"core_channel_obligations_imported={fmt_bool(result['core_channel_obligations_imported'])}",
        f"low_overflow_edge_obligations_imported={fmt_bool(result['low_overflow_edge_obligations_imported'])}",
        f"mobius_divisor_sum_channel_bounds_proved={fmt_bool(result['mobius_divisor_sum_channel_bounds_proved'])}",
        f"boundary_lcm_edge_bounds_proved={fmt_bool(result['boundary_lcm_edge_bounds_proved'])}",
        f"unified_vector_pdec_excluded={fmt_bool(result['unified_vector_pdec_excluded'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 家族汇总",
        "",
        "| family | obligations | total sample scale | max sample scale | sample labels |",
        "| --- | ---: | ---: | ---: | --- |",
    ]
    for family in result["family_summaries"]:
        lines.append(
            f"| `{family['family']}` | {family['obligation_count']} | "
            f"{fmt_float(family['total_sample_abs_scale'])} | {fmt_float(family['max_sample_abs_scale'])} | "
            f"`{family['sample_labels']}` |"
        )
    lines.extend(
        [
            "",
            "## 2. 最大义务",
            "",
            "| family | z | label | sample signed | sample scale | sample ratio |",
            "| --- | ---: | --- | ---: | ---: | ---: |",
        ]
    )
    for obligation in result["top_obligations"]:
        lines.append(
            f"| `{obligation['family']}` | {obligation['z']} | `{obligation['label']}` | "
            f"{fmt_float(obligation['sample_signed_value'])} | "
            f"{fmt_float(obligation['sample_abs_scale'])} | {fmt_float(obligation['sample_ratio'])} |"
        )
    lines.extend(
        [
            "",
            "## 3. 证明边界",
            "",
            "- 已闭合：统一 VectorSquarefree-PDEC 义务格式。",
            "- 已导入：core channel 与 low-overflow edge 两类剩余。",
            "- 未闭合：Möbius divisor-sum 通道界。",
            "- 未闭合：boundary lcm edge 角度界。",
            "- 未闭合：统一 VectorSquarefree-PDEC 排斥。",
            f"- 下一目标：`{result['next_direct_attack_target']}`。",
            "",
            "## 4. 依赖哈希",
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
    result = audit()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result)
    print(
        json.dumps(
            {
                "status": result["status"],
                "obligation_count": result["obligation_count"],
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
