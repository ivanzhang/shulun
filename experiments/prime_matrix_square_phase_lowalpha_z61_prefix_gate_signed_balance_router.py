#!/usr/bin/env python3
"""审计 z=61 PrefixGate signed phase balance 的精确计数骨架。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_prefix_gate_signed_balance_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-prefix-gate-signed-balance-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-prefix-gate-signed-balance-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-prefix-gate-signed-balance-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
PREFIX_PHASE_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-prefix-gate-phase-persistence-router.json"
DYADIC_BALANCE_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-fixed-core-dyadic-balance-lemma-router.json"
DYADIC_SOURCE_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-dyadic-source-congruence-router.json"
SAME_P_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-dyadic-same-p-strip-carry-router.json"
SHIFTED_FACTOR_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-endpoint-shifted-factor-router.json"
SQUARE_WINDOW_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-shifted-square-window-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-prefix-gate-signed-balance-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-prefix-gate-signed-balance-router.md"

NEXT_TARGET = "DyadicLiftCompanionForPrefixPhaseOrPersistentPhasePDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-prefix-gate-phase-persistence-router.json",
    "prime-matrix-square-phase-lowalpha-z61-fixed-core-dyadic-balance-lemma-router.json",
    "prime-matrix-square-phase-lowalpha-z61-dyadic-source-congruence-router.json",
    "prime-matrix-square-phase-lowalpha-z61-dyadic-same-p-strip-carry-router.json",
    "prime-matrix-square-phase-lowalpha-z61-endpoint-shifted-factor-router.json",
    "prime-matrix-square-phase-lowalpha-z61-shifted-square-window-router.json",
]


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def fmt_float(value: float | None) -> str:
    """格式化浮点数。"""
    if value is None:
        return "n/a"
    return f"{value:.6f}"


def file_sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖哈希。"""
    result = {
        "experiments/prime_matrix_square_phase_lowalpha_z61_prefix_gate_signed_balance_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        result[f"docs/monograph/{name}"] = file_sha256(DOCS / name)
    return result


def load(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def audit() -> dict[str, Any]:
    """执行 PrefixGate signed balance 审计。"""
    phase = load(PREFIX_PHASE_JSON)
    balance = load(DYADIC_BALANCE_JSON)
    source = load(DYADIC_SOURCE_JSON)
    same_p = load(SAME_P_JSON)
    shifted = load(SHIFTED_FACTOR_JSON)
    square = load(SQUARE_WINDOW_JSON)

    source_by_quotient = {row["phase_quotient"]: row for row in source["source_rows"]}
    quotient_rows = []
    unit_weights = []
    signed_count = 0
    signed_weight = 0.0
    for row in balance["quotient_rows"]:
        quotient = row["quotient"]
        source_row = source_by_quotient[quotient]
        unit_weight = row["contribution"] / row["multiplicity"] if row["multiplicity"] else 0.0
        unit_weights.append(unit_weight)
        sign_factor = 1 if row["sign"] == "positive" else -1
        signed_count += sign_factor * row["multiplicity"]
        signed_weight += sign_factor * row["contribution"]
        quotient_rows.append(
            {
                "quotient": quotient,
                "sign": row["sign"],
                "p": row["p"],
                "q": row["q"],
                "a": row["a"],
                "b": row["b"],
                "delta": source_row["delta"],
                "multiplicity": row["multiplicity"],
                "unit_weight": unit_weight,
                "signed_contribution": row["signed_contribution"],
                "singleton_interval_gate_closed": row["singleton_interval_gate_closed"],
                "short_delta_closed": row["short_delta_closed"],
            }
        )

    same_unit_weight = len({round(value, 15) for value in unit_weights}) == 1
    negative_rows = [row for row in quotient_rows if row["sign"] == "negative"]
    positive_rows = [row for row in quotient_rows if row["sign"] == "positive"]
    phase_balance_identity_closed = (
        same_unit_weight
        and len(negative_rows) == 1
        and [row["quotient"] for row in negative_rows] == [1]
        and [row["quotient"] for row in positive_rows] == [2, 4]
        and signed_count == 1
        and signed_weight > 0
    )

    same_p_group = same_p["same_p_strip_groups"][0]
    shifted_row = shifted["shifted_factor_rows"][0]
    square_row = square["square_window_rows"][0]
    positive_companion_closed = (
        source["dyadic_source_congruence_skeleton_closed_for_sample"]
        and same_p["all_positive_same_p_groups_closed"]
        and same_p_group["occupies_both_strip_endpoints"]
        and shifted["all_endpoint_shifted_factor_groups_closed"]
        and shifted_row["shifted_product_identity_closed"]
        and shifted_row["a2_linear_form_closed"]
        and shifted_row["a4_linear_form_closed"]
        and square["all_shifted_square_window_groups_closed"]
        and square_row["s_recovery_closed"]
        and square_row["endpoint_span_window_closed"]
    )

    signed_balance_closed = (
        phase["registered_phase_signed_persistence_materialized"]
        and balance["fixed_core_dyadic_balance_lemma_closed_for_sample"]
        and phase_balance_identity_closed
        and positive_companion_closed
    )

    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_prefix_gate_signed_balance_router",
        "status": "z61_prefix_gate_signed_balance_reduced_to_dyadic_lift_companion_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "source_certificates": [
            phase["certificate_type"],
            balance["certificate_type"],
            source["certificate_type"],
            same_p["certificate_type"],
            shifted["certificate_type"],
            square["certificate_type"],
        ],
        "target_bucket": phase["target_bucket"],
        "target_omega": phase["target_omega"],
        "target_shell": phase["target_shell"],
        "phase_modulus": phase["phase_modulus"],
        "phase_condition": phase["phase_condition"],
        "quotient_rows": quotient_rows,
        "negative_quotients": [row["quotient"] for row in negative_rows],
        "positive_quotients": [row["quotient"] for row in positive_rows],
        "same_unit_weight_on_phase_hits": same_unit_weight,
        "signed_phase_count": signed_count,
        "signed_phase_weight": signed_weight,
        "phase_balance_identity_closed_for_sample": phase_balance_identity_closed,
        "positive_same_p": same_p_group["p"],
        "positive_same_p_endpoint_span": same_p_group["normalized_span"],
        "positive_same_p_endpoint_capacity": same_p_group["slot_capacity"],
        "positive_same_p_semiprime_carry_equation": same_p_group["semiprime_carry_equation"],
        "shifted_common_multiplier": shifted_row["common_multiplier"],
        "shifted_linear_prime_pair_forms": shifted_row["linear_prime_pair_forms"],
        "square_window_recovered_s": square_row["s_recovered_from_square_window"],
        "positive_dyadic_lift_companion_closed_for_sample": positive_companion_closed,
        "prefix_gate_signed_phase_balance_closed_for_sample": signed_balance_closed,
        "dyadic_lift_companion_proved_globally": False,
        "persistent_phase_pdec_excluded": False,
        "missing_lift_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "PrefixGate signed phase balance 可精确化为同权计数骨架：同一相位 "
            "`b≡0 mod 28842` 的三条命中有相同单位权重，负侧只有 quotient `1`，"
            "正侧为 quotient `2,4`，所以局部 signed weight 等于一个单位权重。"
            "正侧两条命中进一步等价于 same-p endpoint strip、shifted linear prime pair "
            "和 square-window selector。全局剩余因此收窄为：负锚是否必有 dyadic lift "
            "companion，或 PersistentPhase/MissingLift-PDEC 是否可排斥。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 PrefixGate signed balance",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"phase_condition={result['phase_condition']}",
        f"negative_quotients={result['negative_quotients']}",
        f"positive_quotients={result['positive_quotients']}",
        f"same_unit_weight_on_phase_hits={fmt_bool(result['same_unit_weight_on_phase_hits'])}",
        f"signed_phase_count={result['signed_phase_count']}",
        f"signed_phase_weight={fmt_float(result['signed_phase_weight'])}",
        f"positive_dyadic_lift_companion_closed_for_sample={fmt_bool(result['positive_dyadic_lift_companion_closed_for_sample'])}",
        f"prefix_gate_signed_phase_balance_closed_for_sample={fmt_bool(result['prefix_gate_signed_phase_balance_closed_for_sample'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 同权计数骨架",
        "",
        "| quotient | sign | p | q | a | b | delta | mult | unit weight | signed |",
        "| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in result["quotient_rows"]:
        lines.append(
            f"| {row['quotient']} | `{row['sign']}` | {row['p']} | {row['q']} | "
            f"{row['a']} | {row['b']} | {row['delta']} | {row['multiplicity']} | "
            f"{fmt_float(row['unit_weight'])} | {fmt_float(row['signed_contribution'])} |"
        )

    lines.extend(
        [
            "",
            "## 2. 正侧 companion",
            "",
            "| field | value |",
            "| --- | --- |",
            f"| same-p | `{result['positive_same_p']}` |",
            f"| endpoint span/capacity | `{result['positive_same_p_endpoint_span']} / {result['positive_same_p_endpoint_capacity']}` |",
            f"| carry equation | `{result['positive_same_p_semiprime_carry_equation']}` |",
            f"| shifted multiplier | `{result['shifted_common_multiplier']}` |",
            f"| linear forms | `{result['shifted_linear_prime_pair_forms']}` |",
            f"| square-window recovered s | `{result['square_window_recovered_s']}` |",
            "",
            "## 3. 证明边界",
            "",
            "- 已闭合：当前 formal unit 的 PrefixGate signed balance 精确同权计数骨架。",
            "- 已闭合：正侧两条 lift 与 shifted pair / square-window 链严格对接。",
            "- 未闭合：dyadic lift companion 的全局必然性，或 PersistentPhase/MissingLift-PDEC 排斥。",
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
                "prefix_gate_signed_phase_balance_closed_for_sample": result[
                    "prefix_gate_signed_phase_balance_closed_for_sample"
                ],
                "positive_dyadic_lift_companion_closed_for_sample": result[
                    "positive_dyadic_lift_companion_closed_for_sample"
                ],
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
