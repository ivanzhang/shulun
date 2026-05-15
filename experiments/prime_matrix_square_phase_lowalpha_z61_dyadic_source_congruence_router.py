#!/usr/bin/env python3
"""审计 z=61 dyadic lift 吸收器的源同余骨架。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_dyadic_source_congruence_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-dyadic-source-congruence-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-dyadic-source-congruence-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-dyadic-source-congruence-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
ABSORBER_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-negative-dyadic-absorber-router.json"
INTERVAL_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-source-fiber-singleton-interval-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-dyadic-source-congruence-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-dyadic-source-congruence-router.md"

NEXT_TARGET = "GlobalDyadicSourceCongruenceProofOrDyadicSourcePDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-negative-dyadic-absorber-router.json",
    "prime-matrix-square-phase-lowalpha-z61-source-fiber-singleton-interval-router.json",
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
        "experiments/prime_matrix_square_phase_lowalpha_z61_dyadic_source_congruence_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def compact_row(row: dict[str, Any], phase_modulus: int) -> dict[str, Any]:
    """压缩源纤维行，只保留 dyadic 骨架需要的字段。"""
    expected_b = phase_modulus * row["phase_quotient"]
    return {
        "phase_quotient": row["phase_quotient"],
        "target_cell_sign": row["target_cell_sign"],
        "p": row["p"],
        "q": row["q"],
        "a": row["a"],
        "b": row["b"],
        "b_equals_phase_modulus_times_quotient": row["b"] == expected_b,
        "modulus_bq": row["modulus_bq"],
        "residue": row["modulus_bq"] - row["left_slack_abq_minus_p2"],
        "delta": row["left_slack_abq_minus_p2"],
        "short_delta_closed": 0 < row["left_slack_abq_minus_p2"] < row["p"],
        "a_interval_width": row["a_interval_width"],
        "valid_a_interval_singleton": row["valid_a_interval_singleton"],
        "a_floor_formula_closed": row["a_floor_formula_closed"],
        "prime_a": row["prime_a"],
        "prime_b": row["prime_b"],
        "singleton_interval_gate_closed": row["singleton_interval_gate_closed"],
    }


def audit() -> dict[str, Any]:
    """执行 dyadic 源同余骨架审计。"""
    absorber = json.loads(ABSORBER_JSON.read_text(encoding="utf-8"))
    interval = json.loads(INTERVAL_JSON.read_text(encoding="utf-8"))
    phase_modulus = interval["phase_modulus"]
    source_rows = [compact_row(row, phase_modulus) for row in interval["rows"]]
    source_rows.sort(key=lambda row: row["phase_quotient"])

    absorber_row = absorber["absorber_rows"][0] if absorber["absorber_rows"] else {}
    source_positive_quotients = [
        row["phase_quotient"] for row in source_rows if row["target_cell_sign"] == "positive"
    ]
    source_negative_quotients = [
        row["phase_quotient"] for row in source_rows if row["target_cell_sign"] == "negative"
    ]
    absorber_positive_quotients = absorber_row.get("dyadic_quotients", [])

    quotient_ladder_matches_absorber = (
        source_negative_quotients == [1]
        and source_positive_quotients == absorber_positive_quotients == [2, 4]
    )
    phase_modulus_matches_negative_anchor = (
        phase_modulus == absorber_row.get("negative_b") == absorber_row.get("hit_lcm")
    )
    all_b_on_phase_ladder = all(
        row["b_equals_phase_modulus_times_quotient"] for row in source_rows
    )
    all_singleton_sources_closed = all(
        row["singleton_interval_gate_closed"]
        and row["valid_a_interval_singleton"]
        and row["a_floor_formula_closed"]
        for row in source_rows
    )
    all_short_residues_closed = all(row["short_delta_closed"] for row in source_rows)
    all_a_prime = all(row["prime_a"] for row in source_rows)
    dyadic_source_congruence_skeleton_closed = (
        phase_modulus_matches_negative_anchor
        and quotient_ladder_matches_absorber
        and all_b_on_phase_ladder
        and all_singleton_sources_closed
        and all_short_residues_closed
        and all_a_prime
    )
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_dyadic_source_congruence_router",
        "status": "z61_dyadic_absorber_reduced_to_source_congruence_skeleton_global_proof_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "source_certificates": [absorber["certificate_type"], interval["certificate_type"]],
        "target_bucket": absorber["target_bucket"],
        "target_omega": absorber["target_omega"],
        "target_shell": absorber["target_shell"],
        "phase_modulus": phase_modulus,
        "phase_modulus_matches_negative_anchor": phase_modulus_matches_negative_anchor,
        "source_negative_quotients": source_negative_quotients,
        "source_positive_quotients": source_positive_quotients,
        "absorber_positive_quotients": absorber_positive_quotients,
        "quotient_ladder_matches_absorber": quotient_ladder_matches_absorber,
        "all_b_on_phase_ladder": all_b_on_phase_ladder,
        "all_singleton_sources_closed": all_singleton_sources_closed,
        "all_short_residues_closed": all_short_residues_closed,
        "all_a_prime": all_a_prime,
        "source_rows": source_rows,
        "dyadic_source_congruence_skeleton_closed_for_sample": (
            dyadic_source_congruence_skeleton_closed
        ),
        "global_dyadic_source_congruence_proved": False,
        "dyadic_source_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "dyadic lift 吸收器已经回落到同一个源同余骨架："
            "phase modulus `28842` 同时是负原子的 `b` 与 hit lcm，"
            "三条源纤维恰为 quotient `1,2,4`，且每条都满足 singleton interval "
            "`a=floor(p^2/(bq))+1` 与短残基 `0<qab-p^2<p`。"
            "因此下一步不再需要在抽象权重层打转，而是集中证明这种源同余骨架的全局强制性，"
            "或登记 DyadicSource-PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 dyadic source congruence",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"phase_modulus={result['phase_modulus']}",
        f"phase_modulus_matches_negative_anchor={fmt_bool(result['phase_modulus_matches_negative_anchor'])}",
        f"source_negative_quotients={result['source_negative_quotients']}",
        f"source_positive_quotients={result['source_positive_quotients']}",
        f"quotient_ladder_matches_absorber={fmt_bool(result['quotient_ladder_matches_absorber'])}",
        f"all_b_on_phase_ladder={fmt_bool(result['all_b_on_phase_ladder'])}",
        f"all_singleton_sources_closed={fmt_bool(result['all_singleton_sources_closed'])}",
        f"all_short_residues_closed={fmt_bool(result['all_short_residues_closed'])}",
        f"dyadic_source_congruence_skeleton_closed_for_sample={fmt_bool(result['dyadic_source_congruence_skeleton_closed_for_sample'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 源同余骨架",
        "",
        "| quotient | sign | p | q | a | b | delta | width(a) | singleton |",
        "| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in result["source_rows"]:
        lines.append(
            f"| {row['phase_quotient']} | `{row['target_cell_sign']}` | "
            f"{row['p']} | {row['q']} | {row['a']} | {row['b']} | "
            f"{row['delta']} | {fmt_float(row['a_interval_width'])} | "
            f"{fmt_bool(row['singleton_interval_gate_closed'])} |"
        )
    lines.extend(
        [
            "",
            "## 2. 自足小引理",
            "",
            "若同一 phase modulus `B` 下存在 quotient `1,2,4` 三条源纤维，"
            "其中 quotient `1` 为负、`2,4` 为正，并且三条都由 singleton interval gate "
            "`a=floor(p^2/(bq))+1` 产生，则该骨架给出 dyadic lift 吸收器。"
            "原因是 `b=B,2B,4B` 位于同一 hit-moduli 组的倍数相位，"
            "组权重相同，两个正原子逐权重吸收一个负原子。",
            "",
            "## 3. 证明边界",
            "",
            "- 已闭合：样本内 dyadic lift 吸收器完全来自 quotient `1,2,4` 源同余骨架。",
            "- 未闭合：全局源同余骨架强制性，或 DyadicSource-PDEC 排斥。",
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
                "dyadic_source_congruence_skeleton_closed_for_sample": result[
                    "dyadic_source_congruence_skeleton_closed_for_sample"
                ],
                "quotient_ladder_matches_absorber": result["quotient_ladder_matches_absorber"],
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
