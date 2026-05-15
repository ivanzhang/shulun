#!/usr/bin/env python3
"""审计 z=61 端点半素数 carry 对的移位因子刚性。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_endpoint_shifted_factor_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-endpoint-shifted-factor-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-endpoint-shifted-factor-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-endpoint-shifted-factor-router.md
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
SOURCE_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-dyadic-same-p-strip-carry-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-endpoint-shifted-factor-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-endpoint-shifted-factor-router.md"

NEXT_TARGET = "ShiftedLinearPrimePairGlobalBoundOrShiftedFactorPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-dyadic-same-p-strip-carry-router.json",
]


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def file_sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖哈希。"""
    result = {
        "experiments/prime_matrix_square_phase_lowalpha_z61_endpoint_shifted_factor_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def row_by_quotient(rows: list[dict[str, Any]], quotient: int) -> dict[str, Any] | None:
    """按 quotient 查找源纤维。"""
    for row in rows:
        if row["phase_quotient"] == quotient:
            return row
    return None


def shifted_rows(source: dict[str, Any]) -> list[dict[str, Any]]:
    """从同 p 条带组中抽取 endpoint shifted factor 恒等式。"""
    result = []
    for group in source["same_p_strip_groups"]:
        q2_row = row_by_quotient(group["source_rows"], 2)
        q4_row = row_by_quotient(group["source_rows"], 4)
        if q2_row is None or q4_row is None:
            continue
        q2 = q2_row["q"]
        a2 = q2_row["a"]
        q4 = q4_row["q"]
        a4 = q4_row["a"]
        carry = group["semiprime_carry_equation_value"]
        q_gap = 2 * q4 - q2
        shifted_left = q2 * (a2 + 1)
        shifted_right = 2 * q4 * (a4 + 1)
        gcd_value = math.gcd(q2, 2 * q4)
        multiplier_from_a2 = None
        multiplier_from_a4 = None
        if (a2 + 1) % (2 * q4) == 0:
            multiplier_from_a2 = (a2 + 1) // (2 * q4)
        if (a4 + 1) % q2 == 0:
            multiplier_from_a4 = (a4 + 1) // q2
        common_multiplier = (
            multiplier_from_a2
            if multiplier_from_a2 is not None and multiplier_from_a2 == multiplier_from_a4
            else None
        )
        result.append(
            {
                "p": group["p"],
                "phase_modulus": group["phase_modulus"],
                "base_modulus": group["base_modulus"],
                "slot_min": group["slot_min"],
                "slot_max": group["slot_max"],
                "slot_capacity": group["slot_capacity"],
                "carry": carry,
                "q2": q2,
                "a2": a2,
                "q4": q4,
                "a4": a4,
                "q_gap_2q4_minus_q2": q_gap,
                "carry_equals_q_gap": carry == q_gap,
                "shifted_left_q2_a2_plus_1": shifted_left,
                "shifted_right_2q4_a4_plus_1": shifted_right,
                "shifted_product_identity_closed": shifted_left == shifted_right,
                "gcd_q2_2q4": gcd_value,
                "coprime_q2_2q4": gcd_value == 1,
                "common_multiplier": common_multiplier,
                "a2_linear_form_closed": (
                    common_multiplier is not None and a2 == 2 * q4 * common_multiplier - 1
                ),
                "a4_linear_form_closed": (
                    common_multiplier is not None and a4 == q2 * common_multiplier - 1
                ),
                "linear_prime_pair_forms": (
                    None
                    if common_multiplier is None
                    else {
                        "a4": f"{q2}*{common_multiplier}-1",
                        "a2": f"{2 * q4}*{common_multiplier}-1",
                    }
                ),
                "endpoint_shifted_factor_closed_for_group": (
                    carry == q_gap
                    and shifted_left == shifted_right
                    and gcd_value == 1
                    and common_multiplier is not None
                    and a2 == 2 * q4 * common_multiplier - 1
                    and a4 == q2 * common_multiplier - 1
                ),
            }
        )
    return result


def audit() -> dict[str, Any]:
    """执行 endpoint shifted factor 审计。"""
    source = json.loads(SOURCE_JSON.read_text(encoding="utf-8"))
    rows = shifted_rows(source)
    all_rows_closed = bool(rows) and all(
        row["endpoint_shifted_factor_closed_for_group"] for row in rows
    )
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_endpoint_shifted_factor_router",
        "status": "z61_endpoint_spanning_pair_reduced_to_shifted_linear_prime_pair_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "source_certificate": source["certificate_type"],
        "target_bucket": source["target_bucket"],
        "target_omega": source["target_omega"],
        "target_shell": source["target_shell"],
        "endpoint_shifted_factor_group_count": len(rows),
        "all_endpoint_shifted_factor_groups_closed": all_rows_closed,
        "shifted_factor_rows": rows,
        "shifted_linear_prime_pair_global_bound_proved": False,
        "shifted_factor_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "端点半素数 carry 对继续压缩：样本中 carry `3` 等于 `2q_4-q_2`，"
            "因此 `q_2a_2-2q_4a_4=3` 等价变形为 "
            "`q_2(a_2+1)=2q_4(a_4+1)`。由于 `gcd(q_2,2q_4)=1`，"
            "得到共同乘子 `s=132`，即 `a_4=71s-1`、`a_2=74s-1`。"
            "下一步的全局硬点进一步收窄为移位线性素数对容量界，"
            "或登记 ShiftedFactor-PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 endpoint shifted factor",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"endpoint_shifted_factor_group_count={result['endpoint_shifted_factor_group_count']}",
        f"all_endpoint_shifted_factor_groups_closed={fmt_bool(result['all_endpoint_shifted_factor_groups_closed'])}",
        f"shifted_linear_prime_pair_global_bound_proved={fmt_bool(result['shifted_linear_prime_pair_global_bound_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 移位因子恒等式",
        "",
        "| p | q2 | a2 | q4 | a4 | carry | 2q4-q2 | shifted identity | s | closed |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | --- |",
    ]
    for row in result["shifted_factor_rows"]:
        lines.append(
            f"| {row['p']} | {row['q2']} | {row['a2']} | {row['q4']} | "
            f"{row['a4']} | {row['carry']} | {row['q_gap_2q4_minus_q2']} | "
            f"`{row['shifted_left_q2_a2_plus_1']}={row['shifted_right_2q4_a4_plus_1']}` | "
            f"{row['common_multiplier']} | "
            f"{fmt_bool(row['endpoint_shifted_factor_closed_for_group'])} |"
        )
    lines.extend(
        [
            "",
            "## 2. 线性素数型",
            "",
            "| s | a4 form | a2 form | coprime(q2,2q4) |",
            "| ---: | --- | --- | --- |",
        ]
    )
    for row in result["shifted_factor_rows"]:
        forms = row["linear_prime_pair_forms"] or {"a4": "n/a", "a2": "n/a"}
        lines.append(
            f"| {row['common_multiplier']} | `{forms['a4']}` | `{forms['a2']}` | "
            f"{fmt_bool(row['coprime_q2_2q4'])} |"
        )
    lines.extend(
        [
            "",
            "## 3. 自足小引理",
            "",
            "若 endpoint carry 方程 `q_2a_2-2q_4a_4=c` 同时满足 `c=2q_4-q_2`，"
            "则有 `q_2(a_2+1)=2q_4(a_4+1)`。若再有 `gcd(q_2,2q_4)=1`，"
            "则存在整数 `s` 使得 `a_4=q_2s-1` 且 `a_2=2q_4s-1`。"
            "因此端点跨越半素数对被压成两个同步移位线性素数型。",
            "",
            "## 4. 证明边界",
            "",
            "- 已闭合：样本 endpoint pair 等价于 `s=132` 的同步移位线性素数对。",
            "- 未闭合：全局移位线性素数对容量界，或 ShiftedFactor-PDEC 排斥。",
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
                "all_endpoint_shifted_factor_groups_closed": result[
                    "all_endpoint_shifted_factor_groups_closed"
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
