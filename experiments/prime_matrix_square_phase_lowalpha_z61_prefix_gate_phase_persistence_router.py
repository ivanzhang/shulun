#!/usr/bin/env python3
"""审计 z=61 PrefixGate-PDEC 相位的跨 profile 持久性与符号路由。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_prefix_gate_phase_persistence_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-prefix-gate-phase-persistence-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-prefix-gate-phase-persistence-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-prefix-gate-phase-persistence-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

import prime_matrix_square_phase_lowalpha_selberg_remainder_attribution_router as attribution
import prime_matrix_square_phase_lowalpha_z61_depth_cell_weight_function_router as weight_router
import prime_matrix_square_phase_lowalpha_z61_mobius_kernel_normal_form_router as kernel_form
import prime_matrix_square_phase_lowalpha_z61_weight_profile_cancellation_router as profile_router


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
PDEC_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-prefix-gate-pdec-registration-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-prefix-gate-phase-persistence-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-prefix-gate-phase-persistence-router.md"

DEFAULT_P_LIST = attribution.DEFAULT_P_LIST
TARGET_BUCKET = "unbalanced<=8"
TARGET_OMEGA = 4
TARGET_SHELL = "(8D,16D]"
DEFAULT_Z = 61
DEFAULT_D_LEVEL = attribution.DEFAULT_D_LEVEL
DEFAULT_OVERFLOW_MULTIPLIER = 16

NEXT_TARGET = "PrefixGateSignedPhaseBalanceOrPersistentPhasePDECExclusion"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-prefix-gate-pdec-registration-router.json",
]


def safe_ratio(numerator: float, denominator: float) -> float | None:
    """计算安全比值。"""
    if denominator == 0:
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
        "experiments/prime_matrix_square_phase_lowalpha_z61_prefix_gate_phase_persistence_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def signed_label(value: float) -> str:
    """给 profile 线性余项打符号标签。"""
    if value > 0:
        return "positive"
    if value < 0:
        return "negative"
    return "zero"


def audit() -> dict[str, Any]:
    """执行相位持久性审计。"""
    pdec = json.loads(PDEC_JSON.read_text(encoding="utf-8"))
    record = pdec["prefix_gate_pdec_record"]
    phase_modulus = record["phase_modulus"]
    profiles, primes = profile_router.collect_value_profiles(DEFAULT_P_LIST)
    weights = attribution.selberg.selberg_weights(DEFAULT_Z, DEFAULT_D_LEVEL, primes)
    kernels = kernel_form.edge_kernel_weights(weights, DEFAULT_D_LEVEL, DEFAULT_OVERFLOW_MULTIPLIER)
    groups = weight_router.group_cell_moduli(kernels, primes, DEFAULT_D_LEVEL)
    target_moduli = groups[(TARGET_BUCKET, TARGET_OMEGA, TARGET_SHELL)]

    profile_rows = []
    phase_hit_rows = []
    for p_value in DEFAULT_P_LIST:
        linear, model_mean, nonzero_values, max_weight, max_weight_value = profile_router.profile_linear(
            profiles[p_value], target_moduli
        )
        value_count = sum(profiles[p_value].values())
        expected = value_count * model_mean
        actual = expected + linear
        phase_hits = []
        phase_actual = 0.0
        phase_multiplicity = 0
        for b_value, multiplicity in sorted(profiles[p_value].items()):
            if b_value % phase_modulus != 0:
                continue
            hit_moduli = [
                {"m": modulus, "K": k_value}
                for modulus, k_value in sorted(target_moduli.items())
                if b_value % modulus == 0
            ]
            hit_weight = sum(item["K"] for item in hit_moduli)
            contribution = multiplicity * hit_weight
            phase_actual += contribution
            phase_multiplicity += multiplicity
            phase_hits.append(
                {
                    "p": p_value,
                    "b_value": b_value,
                    "phase_quotient": b_value // phase_modulus,
                    "multiplicity": multiplicity,
                    "target_hit_moduli": hit_moduli,
                    "target_hit_modulus_count": len(hit_moduli),
                    "target_hit_weight": hit_weight,
                    "target_contribution": contribution,
                }
            )
        sign = signed_label(linear)
        row = {
            "p": p_value,
            "value_count": value_count,
            "target_cell_linear_remainder": linear,
            "target_cell_sign": sign,
            "target_cell_actual": actual,
            "target_cell_expected": expected,
            "target_cell_actual_over_expected": safe_ratio(actual, expected),
            "target_cell_nonzero_value_count": nonzero_values,
            "target_cell_max_weight": max_weight,
            "target_cell_max_weight_value": max_weight_value,
            "registered_phase_hit_value_count": len(phase_hits),
            "registered_phase_hit_multiplicity": phase_multiplicity,
            "registered_phase_target_actual": phase_actual,
            "registered_phase_share_of_target_actual": safe_ratio(phase_actual, actual),
            "registered_phase_hits": phase_hits,
        }
        profile_rows.append(row)
        phase_hit_rows.extend(phase_hits)

    negative_phase_actual = sum(
        row["registered_phase_target_actual"] for row in profile_rows if row["target_cell_sign"] == "negative"
    )
    positive_phase_actual = sum(
        row["registered_phase_target_actual"] for row in profile_rows if row["target_cell_sign"] == "positive"
    )
    phase_hits_by_sign = {
        "negative": sum(row["registered_phase_hit_multiplicity"] for row in profile_rows if row["target_cell_sign"] == "negative"),
        "positive": sum(row["registered_phase_hit_multiplicity"] for row in profile_rows if row["target_cell_sign"] == "positive"),
        "zero": sum(row["registered_phase_hit_multiplicity"] for row in profile_rows if row["target_cell_sign"] == "zero"),
    }
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_prefix_gate_phase_persistence_router",
        "status": "z61_prefix_gate_phase_persistence_is_signed_not_absent_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "source_certificate": pdec["certificate_type"],
        "target_bucket": TARGET_BUCKET,
        "target_omega": TARGET_OMEGA,
        "target_shell": TARGET_SHELL,
        "phase_modulus": phase_modulus,
        "phase_condition": record["phase_condition"],
        "p_list": DEFAULT_P_LIST,
        "profile_rows": profile_rows,
        "phase_hit_rows": phase_hit_rows,
        "phase_hit_profile_count": sum(1 for row in profile_rows if row["registered_phase_hit_multiplicity"] > 0),
        "phase_hit_total_multiplicity": sum(row["registered_phase_hit_multiplicity"] for row in profile_rows),
        "phase_hits_by_sign": phase_hits_by_sign,
        "negative_phase_actual": negative_phase_actual,
        "positive_phase_actual": positive_phase_actual,
        "positive_over_negative_phase_actual": safe_ratio(positive_phase_actual, negative_phase_actual),
        "registered_phase_absence_exclusion_failed": len(phase_hit_rows) > 1,
        "registered_phase_signed_persistence_materialized": True,
        "sample_positive_phase_actual_covers_negative_phase_actual": positive_phase_actual >= negative_phase_actual,
        "prefix_gate_signed_phase_balance_proved": False,
        "persistent_phase_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "已登记相位 `b≡0 mod 28842` 不能通过“样本中不存在”排斥："
            "它在 `p=36739` 的负 profile 中出现一次，在 `p=200003` 的正 profile 中出现两次。"
            "因此 PrefixGate-PDEC 的下一最窄形态不是相位缺席，而是 signed phase balance："
            "证明正 profile 中同相位贡献足以吸收负缺陷，或证明持久同相位偏斜形成可排斥的 PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 PrefixGate 相位持久性",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"phase_condition={result['phase_condition']}",
        f"phase_hit_profile_count={result['phase_hit_profile_count']}",
        f"phase_hit_total_multiplicity={result['phase_hit_total_multiplicity']}",
        f"phase_hits_by_sign={result['phase_hits_by_sign']}",
        f"negative_phase_actual={fmt_float(result['negative_phase_actual'])}",
        f"positive_phase_actual={fmt_float(result['positive_phase_actual'])}",
        f"positive_over_negative_phase_actual={fmt_float(result['positive_over_negative_phase_actual'])}",
        f"prefix_gate_signed_phase_balance_proved={fmt_bool(result['prefix_gate_signed_phase_balance_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. Profile 相位命中",
        "",
        "| p | sign | linear | phase hits | phase mult | phase actual | phase share actual |",
        "| ---: | --- | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in result["profile_rows"]:
        lines.append(
            f"| {row['p']} | `{row['target_cell_sign']}` | "
            f"{fmt_float(row['target_cell_linear_remainder'])} | "
            f"{row['registered_phase_hit_value_count']} | "
            f"{row['registered_phase_hit_multiplicity']} | "
            f"{fmt_float(row['registered_phase_target_actual'])} | "
            f"{fmt_float(row['registered_phase_share_of_target_actual'])} |"
        )
    lines.extend(
        [
            "",
            "## 2. 命中明细",
            "",
            "| p | b | quotient | mult | target moduli | contribution |",
            "| ---: | ---: | ---: | ---: | --- | ---: |",
        ]
    )
    for hit in result["phase_hit_rows"]:
        moduli = [item["m"] for item in hit["target_hit_moduli"]]
        lines.append(
            f"| {hit['p']} | {hit['b_value']} | {hit['phase_quotient']} | "
            f"{hit['multiplicity']} | `{moduli}` | {fmt_float(hit['target_contribution'])} |"
        )
    lines.extend(
        [
            "",
            "## 3. 证明边界",
            "",
            "- 已闭合：PrefixGate-PDEC 相位的样本持久性与符号路由账本。",
            "- 未闭合：signed phase balance 全局证明，或 PersistentPhase-PDEC 排斥。",
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
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    result = audit()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result)
    print(
        json.dumps(
            {
                "status": result["status"],
                "phase_hit_total_multiplicity": result["phase_hit_total_multiplicity"],
                "positive_over_negative_phase_actual": result["positive_over_negative_phase_actual"],
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
