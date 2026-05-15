#!/usr/bin/env python3
"""审计 z=61 负多命中支撑的 dyadic lift 吸收器。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_negative_dyadic_absorber_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-negative-dyadic-absorber-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-negative-dyadic-absorber-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-negative-dyadic-absorber-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
SOURCE_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-negative-support-isolation-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-negative-dyadic-absorber-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-negative-dyadic-absorber-router.md"

NEXT_TARGET = "GlobalDyadicLiftAbsorberProofOrDyadicLiftPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-negative-support-isolation-router.json",
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
        "experiments/prime_matrix_square_phase_lowalpha_z61_negative_dyadic_absorber_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def is_power_of_two(value: int | None) -> bool:
    """判断正整数是否为 2 的幂。"""
    if value is None or value <= 0:
        return False
    return value & (value - 1) == 0


def lcm_many(values: list[int]) -> int:
    """计算多个整数的最小公倍数。"""
    result = 1
    for value in values:
        result = math.lcm(result, value)
    return result


def quotient_if_integer(numerator: int, denominator: int) -> int | None:
    """若 numerator 是 denominator 的整数倍，则返回商。"""
    if denominator == 0 or numerator % denominator != 0:
        return None
    return numerator // denominator


def negative_groups(data: dict[str, Any]) -> list[dict[str, Any]]:
    """取出所有含负支撑的多命中组。"""
    rows: list[dict[str, Any]] = []
    for class_name in ["negative_only", "mixed_absorbed", "mixed_unabsorbed"]:
        rows.extend(data["class_rows"].get(class_name, []))
    return [row for row in rows if row["negative_count"] > 0]


def absorber_rows(data: dict[str, Any]) -> list[dict[str, Any]]:
    """为每个负原子构造同组正向 dyadic lift 吸收器。"""
    rows = []
    for group in negative_groups(data):
        hit_moduli = group["hit_moduli"]
        hit_lcm = lcm_many(hit_moduli)
        negative_atoms = [atom for atom in group["atoms"] if atom["profile_sign"] == "negative"]
        positive_atoms = [atom for atom in group["atoms"] if atom["profile_sign"] == "positive"]
        for negative_atom in negative_atoms:
            witnesses = []
            for positive_atom in positive_atoms:
                quotient = quotient_if_integer(positive_atom["b_value"], negative_atom["b_value"])
                witnesses.append(
                    {
                        "p": positive_atom["p"],
                        "b_value": positive_atom["b_value"],
                        "quotient_over_negative_b": quotient,
                        "quotient_is_power_of_two": is_power_of_two(quotient),
                        "same_unit_weight": (
                            abs(positive_atom["signed_weight_contribution"])
                            == abs(negative_atom["signed_weight_contribution"])
                        ),
                    }
                )
            dyadic_witnesses = [item for item in witnesses if item["quotient_is_power_of_two"]]
            rows.append(
                {
                    "hit_moduli": hit_moduli,
                    "hit_lcm": hit_lcm,
                    "negative_p": negative_atom["p"],
                    "negative_b": negative_atom["b_value"],
                    "negative_b_equals_hit_lcm": negative_atom["b_value"] == hit_lcm,
                    "negative_unit_weight": abs(negative_atom["signed_weight_contribution"]),
                    "group_positive_count": group["positive_count"],
                    "group_negative_count": group["negative_count"],
                    "group_signed_count": group["signed_count"],
                    "group_signed_weight": group["signed_weight"],
                    "group_locally_absorbed": group["locally_absorbed"],
                    "positive_witnesses": witnesses,
                    "positive_witness_count": len(witnesses),
                    "dyadic_witness_count": len(dyadic_witnesses),
                    "dyadic_quotients": [
                        item["quotient_over_negative_b"] for item in dyadic_witnesses
                    ],
                    "positive_surplus_count": group["positive_count"] - group["negative_count"],
                    "dyadic_absorber_closed_for_atom": (
                        negative_atom["b_value"] == hit_lcm
                        and group["locally_absorbed"]
                        and group["positive_count"] > group["negative_count"]
                        and len(dyadic_witnesses) >= group["negative_count"] + 1
                        and all(item["same_unit_weight"] for item in witnesses)
                    ),
                }
            )
    return rows


def audit() -> dict[str, Any]:
    """执行 dyadic lift 吸收器审计。"""
    data = json.loads(SOURCE_JSON.read_text(encoding="utf-8"))
    rows = absorber_rows(data)
    all_rows_closed = bool(rows) and all(row["dyadic_absorber_closed_for_atom"] for row in rows)
    all_lcm_anchored = bool(rows) and all(row["negative_b_equals_hit_lcm"] for row in rows)
    all_have_two_dyadic_lifts = bool(rows) and all(row["dyadic_witness_count"] >= 2 for row in rows)
    all_locally_absorbed = bool(rows) and all(row["group_locally_absorbed"] for row in rows)
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_negative_dyadic_absorber_router",
        "status": "z61_negative_support_absorbed_by_lcm_anchored_dyadic_lifts_global_proof_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "source_certificate": data["certificate_type"],
        "target_bucket": data["target_bucket"],
        "target_omega": data["target_omega"],
        "target_shell": data["target_shell"],
        "negative_group_count": len(negative_groups(data)),
        "absorber_atom_count": len(rows),
        "all_negative_atoms_lcm_anchored": all_lcm_anchored,
        "all_negative_atoms_have_two_dyadic_lifts": all_have_two_dyadic_lifts,
        "all_negative_groups_locally_absorbed": all_locally_absorbed,
        "dyadic_absorber_criterion_closed_for_sample": all_rows_closed,
        "absorber_rows": rows,
        "global_dyadic_lift_absorber_proved": False,
        "dyadic_lift_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "唯一负多命中支撑不只是被正计数覆盖，而是呈现更刚性的 dyadic lift 吸收："
            "负原子 `b=28842` 等于 hit-moduli `[9614,14421]` 的 lcm，"
            "同组两条正记录正好位于 `2b` 与 `4b`，且单位权重完全相同。"
            "因此样本内负-only 失败对象被压成一个更窄的全局输入："
            "证明所有负多命中 lcm 锚都有足够 dyadic 正升格，"
            "或登记 DyadicLift-PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 negative dyadic absorber",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"negative_group_count={result['negative_group_count']}",
        f"absorber_atom_count={result['absorber_atom_count']}",
        f"all_negative_atoms_lcm_anchored={fmt_bool(result['all_negative_atoms_lcm_anchored'])}",
        f"all_negative_atoms_have_two_dyadic_lifts={fmt_bool(result['all_negative_atoms_have_two_dyadic_lifts'])}",
        f"all_negative_groups_locally_absorbed={fmt_bool(result['all_negative_groups_locally_absorbed'])}",
        f"dyadic_absorber_criterion_closed_for_sample={fmt_bool(result['dyadic_absorber_criterion_closed_for_sample'])}",
        f"global_dyadic_lift_absorber_proved={fmt_bool(result['global_dyadic_lift_absorber_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 吸收器表",
        "",
        "| hit moduli | lcm | negative p | negative b | dyadic quotients | positive surplus | signed weight | closed |",
        "| --- | ---: | ---: | ---: | --- | ---: | ---: | --- |",
    ]
    for row in result["absorber_rows"]:
        lines.append(
            f"| `{row['hit_moduli']}` | {row['hit_lcm']} | {row['negative_p']} | "
            f"{row['negative_b']} | `{row['dyadic_quotients']}` | "
            f"{row['positive_surplus_count']} | {fmt_float(row['group_signed_weight'])} | "
            f"{fmt_bool(row['dyadic_absorber_closed_for_atom'])} |"
        )
    lines.extend(
        [
            "",
            "## 2. 正向 lift 见证",
            "",
            "| negative b | positive p | positive b | quotient | power of two | same weight |",
            "| ---: | ---: | ---: | ---: | --- | --- |",
        ]
    )
    for row in result["absorber_rows"]:
        for witness in row["positive_witnesses"]:
            lines.append(
                f"| {row['negative_b']} | {witness['p']} | {witness['b_value']} | "
                f"{witness['quotient_over_negative_b']} | "
                f"{fmt_bool(witness['quotient_is_power_of_two'])} | "
                f"{fmt_bool(witness['same_unit_weight'])} |"
            )
    lines.extend(
        [
            "",
            "## 3. 自足小引理",
            "",
            "在固定 hit-moduli 组中，所有原子的单位权重只由该组决定。"
            "若负原子数为 `N_-`，同组正原子数为 `N_+`，且 `N_+>=N_-`，"
            "则该组 signed count 与 signed weight 均非负。"
            "本证书进一步确认样本中的唯一负组满足更强条件："
            "负 `b` 等于 hit lcm，正见证为同组 `2b,4b` 两个 dyadic lift。",
            "",
            "## 4. 证明边界",
            "",
            "- 已闭合：样本目标格中唯一负多命中原子由 `2b,4b` 两个同权正 lift 吸收。",
            "- 未闭合：全局 dyadic lift 吸收器存在性，或 DyadicLift-PDEC 排斥。",
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
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    result = audit()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result)
    print(
        json.dumps(
            {
                "status": result["status"],
                "dyadic_absorber_criterion_closed_for_sample": result[
                    "dyadic_absorber_criterion_closed_for_sample"
                ],
                "all_negative_atoms_have_two_dyadic_lifts": result[
                    "all_negative_atoms_have_two_dyadic_lifts"
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
