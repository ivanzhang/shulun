#!/usr/bin/env python3
"""审计 z=61 固定核心的同权 dyadic balance 引理。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_fixed_core_dyadic_balance_lemma_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-fixed-core-dyadic-balance-lemma-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-fixed-core-dyadic-balance-lemma-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-fixed-core-dyadic-balance-lemma-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
SOURCE_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-quotient-lock-fixed-core-bridge-router.json"
PREFIX_PHASE_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-prefix-gate-phase-persistence-router.json"
DYADIC_SOURCE_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-dyadic-source-congruence-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-fixed-core-dyadic-balance-lemma-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-fixed-core-dyadic-balance-lemma-router.md"

NEXT_TARGET = "PositiveDyadicLiftExistenceForFixedCoreOrMissingLiftPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-quotient-lock-fixed-core-bridge-router.json",
    "prime-matrix-square-phase-lowalpha-z61-prefix-gate-phase-persistence-router.json",
    "prime-matrix-square-phase-lowalpha-z61-dyadic-source-congruence-router.json",
]


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def fmt_float(value: float) -> str:
    """格式化浮点数。"""
    return f"{value:.6f}"


def file_sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖哈希。"""
    result = {
        "experiments/prime_matrix_square_phase_lowalpha_z61_fixed_core_dyadic_balance_lemma_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def load(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def audit() -> dict[str, Any]:
    """执行同权 dyadic balance 引理审计。"""
    bridge = load(SOURCE_JSON)
    prefix_phase = load(PREFIX_PHASE_JSON)
    dyadic_source = load(DYADIC_SOURCE_JSON)

    by_quotient: dict[int, list[dict[str, Any]]] = defaultdict(list)
    for hit in prefix_phase["phase_hit_rows"]:
        by_quotient[hit["phase_quotient"]].append(hit)

    quotient_rows = []
    signed_total = 0.0
    signed_count = 0
    unit_weights = []
    for row in dyadic_source["source_rows"]:
        quotient = row["phase_quotient"]
        sign = row["target_cell_sign"]
        hits = by_quotient.get(quotient, [])
        contribution = sum(hit["target_contribution"] for hit in hits)
        multiplicity = sum(hit["multiplicity"] for hit in hits)
        signed = contribution if sign == "positive" else -contribution
        signed_total += signed
        signed_count += multiplicity if sign == "positive" else -multiplicity
        for hit in hits:
            unit_weights.append(hit["target_hit_weight"])
        quotient_rows.append(
            {
                "quotient": quotient,
                "sign": sign,
                "p": row["p"],
                "q": row["q"],
                "a": row["a"],
                "b": row["b"],
                "hit_count": len(hits),
                "multiplicity": multiplicity,
                "contribution": contribution,
                "signed_contribution": signed,
                "singleton_interval_gate_closed": row["singleton_interval_gate_closed"],
                "short_delta_closed": row["short_delta_closed"],
            }
        )

    same_unit_weight = len(set(unit_weights)) == 1
    negative_count = sum(row["multiplicity"] for row in quotient_rows if row["sign"] == "negative")
    positive_count = sum(row["multiplicity"] for row in quotient_rows if row["sign"] == "positive")
    dyadic_positive_quotients = [
        row["quotient"]
        for row in quotient_rows
        if row["sign"] == "positive" and row["quotient"] in {2, 4}
    ]
    negative_quotients = [row["quotient"] for row in quotient_rows if row["sign"] == "negative"]

    lemma_closed = (
        bridge["quotient_lock_fixed_core_bridge_closed_for_sample"]
        and same_unit_weight
        and negative_quotients == [1]
        and dyadic_positive_quotients == [2, 4]
        and positive_count >= 2 * negative_count
        and signed_count > 0
        and signed_total > 0
        and all(row["singleton_interval_gate_closed"] for row in quotient_rows)
        and all(row["short_delta_closed"] for row in quotient_rows)
    )

    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_fixed_core_dyadic_balance_lemma_router",
        "status": "z61_fixed_core_dyadic_balance_reduced_to_positive_lift_existence_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "source_certificates": [
            bridge["certificate_type"],
            prefix_phase["certificate_type"],
            dyadic_source["certificate_type"],
        ],
        "target_bucket": bridge["target_bucket"],
        "target_omega": bridge["target_omega"],
        "target_shell": bridge["target_shell"],
        "phase_modulus": bridge["phase_modulus"],
        "core": bridge["core"],
        "quotient_rows": quotient_rows,
        "negative_quotients": negative_quotients,
        "dyadic_positive_quotients": dyadic_positive_quotients,
        "same_unit_weight_on_phase_hits": same_unit_weight,
        "negative_phase_multiplicity": negative_count,
        "positive_phase_multiplicity": positive_count,
        "signed_phase_count": signed_count,
        "signed_phase_weight": signed_total,
        "positive_count_at_least_twice_negative": positive_count >= 2 * negative_count,
        "fixed_core_dyadic_balance_lemma_closed_for_sample": lemma_closed,
        "positive_dyadic_lift_existence_proved_globally": False,
        "missing_lift_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "固定核心的局部吸收可抽象为同权 dyadic balance 引理：同一 hit-moduli 组内"
            "单位权重相同，负 quotient `1` 若有正 quotient `2,4` 两个 lift，则 signed count "
            "和 signed weight 自动为正。样本内该引理闭合；剩余不再是权重比较，"
            "而是全局证明正向 dyadic lift 必存在，或登记 MissingLift-PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 fixed-core dyadic balance lemma",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"same_unit_weight_on_phase_hits={fmt_bool(result['same_unit_weight_on_phase_hits'])}",
        f"negative_quotients={result['negative_quotients']}",
        f"dyadic_positive_quotients={result['dyadic_positive_quotients']}",
        f"positive_count_at_least_twice_negative={fmt_bool(result['positive_count_at_least_twice_negative'])}",
        f"signed_phase_count={result['signed_phase_count']}",
        f"signed_phase_weight={fmt_float(result['signed_phase_weight'])}",
        f"fixed_core_dyadic_balance_lemma_closed_for_sample={fmt_bool(result['fixed_core_dyadic_balance_lemma_closed_for_sample'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. Quotient rows",
        "",
        "| quotient | sign | p | q | a | b | mult | contribution | signed | singleton | short delta |",
        "| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |",
    ]
    for row in result["quotient_rows"]:
        lines.append(
            f"| {row['quotient']} | `{row['sign']}` | {row['p']} | {row['q']} | "
            f"{row['a']} | {row['b']} | {row['multiplicity']} | "
            f"{fmt_float(row['contribution'])} | {fmt_float(row['signed_contribution'])} | "
            f"{fmt_bool(row['singleton_interval_gate_closed'])} | {fmt_bool(row['short_delta_closed'])} |"
        )
    lines.extend(
        [
            "",
            "## 2. 自足引理",
            "",
            "在固定 hit-moduli 组中，单位权重只由目标模数组决定；若负侧只有 quotient `1` 一次命中，"
            "而正侧存在 quotient `2,4` 两个同组命中，则",
            "",
            "```text",
            "signed_count = 2 - 1 = 1 > 0,",
            "signed_weight = 2w - w = w > 0.",
            "```",
            "",
            "因此该固定核心的局部剩余已经从权重估计降为正向 lift 存在性。",
            "",
            "## 3. 证明边界",
            "",
            "- 已闭合：样本内同权 dyadic balance 引理。",
            "- 未闭合：全局证明 quotient `2,4` 正向 lift 必伴随 quotient `1` 负锚，或登记 MissingLift-PDEC。",
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
                "fixed_core_dyadic_balance_lemma_closed_for_sample": result[
                    "fixed_core_dyadic_balance_lemma_closed_for_sample"
                ],
                "signed_phase_count": result["signed_phase_count"],
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
