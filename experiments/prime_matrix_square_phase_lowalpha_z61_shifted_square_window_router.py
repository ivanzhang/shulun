#!/usr/bin/env python3
"""审计 z=61 同步移位线性素数对的平方窗口刚性。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_shifted_square_window_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-shifted-square-window-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-shifted-square-window-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-shifted-square-window-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
SOURCE_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-endpoint-shifted-factor-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-shifted-square-window-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-shifted-square-window-router.md"

NEXT_TARGET = "ShiftedSquareWindowGlobalBoundOrSquareWindowPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-endpoint-shifted-factor-router.json",
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
        "experiments/prime_matrix_square_phase_lowalpha_z61_shifted_square_window_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def square_window_rows(source: dict[str, Any]) -> list[dict[str, Any]]:
    """把移位线性素数对和端点窗口联立。"""
    rows = []
    for row in source["shifted_factor_rows"]:
        p_value = row["p"]
        q2 = row["q2"]
        q4 = row["q4"]
        s_value = row["common_multiplier"]
        base_modulus = row["base_modulus"]
        n_low = 2 * q4 * (q2 * s_value - 1)
        n_high = q2 * (2 * q4 * s_value - 1)
        span = n_high - n_low
        delta_low = base_modulus * n_low - p_value * p_value
        delta_high = base_modulus * n_high - p_value * p_value
        endpoint_lower = delta_low + base_modulus * span
        endpoint_upper = delta_low + base_modulus * (span + 1)
        numerator = p_value * p_value + delta_low + 2 * base_modulus * q4
        denominator = 2 * base_modulus * q2 * q4
        recovered_s = numerator // denominator if numerator % denominator == 0 else None
        rows.append(
            {
                "p": p_value,
                "base_modulus": base_modulus,
                "q2": q2,
                "q4": q4,
                "s": s_value,
                "n_low": n_low,
                "n_high": n_high,
                "span": span,
                "carry": row["carry"],
                "span_equals_carry": span == row["carry"],
                "delta_low": delta_low,
                "delta_high": delta_high,
                "square_identity_low_closed": p_value * p_value == base_modulus * n_low - delta_low,
                "square_identity_high_closed": (
                    p_value * p_value == base_modulus * n_high - delta_high
                ),
                "low_endpoint_floor_closed": 0 < delta_low <= base_modulus,
                "high_endpoint_floor_closed": delta_high <= p_value - 1 < delta_high + base_modulus,
                "endpoint_span_window_closed": endpoint_lower <= p_value - 1 < endpoint_upper,
                "p_square_residue_mod_base": (p_value * p_value) % base_modulus,
                "negative_delta_residue_mod_base": (-delta_low) % base_modulus,
                "delta_congruence_closed": (
                    (p_value * p_value) % base_modulus == (-delta_low) % base_modulus
                ),
                "s_recovery_numerator": numerator,
                "s_recovery_denominator": denominator,
                "s_recovered_from_square_window": recovered_s,
                "s_recovery_closed": recovered_s == s_value,
                "shifted_square_window_closed_for_group": (
                    span == row["carry"]
                    and 0 < delta_low <= base_modulus
                    and delta_high <= p_value - 1 < delta_high + base_modulus
                    and endpoint_lower <= p_value - 1 < endpoint_upper
                    and (p_value * p_value) % base_modulus == (-delta_low) % base_modulus
                    and recovered_s == s_value
                ),
            }
        )
    return rows


def audit() -> dict[str, Any]:
    """执行平方窗口刚性审计。"""
    source = json.loads(SOURCE_JSON.read_text(encoding="utf-8"))
    rows = square_window_rows(source)
    all_rows_closed = bool(rows) and all(
        row["shifted_square_window_closed_for_group"] for row in rows
    )
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_shifted_square_window_router",
        "status": "z61_shifted_linear_prime_pair_reduced_to_square_window_congruence_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "source_certificate": source["certificate_type"],
        "target_bucket": source["target_bucket"],
        "target_omega": source["target_omega"],
        "target_shell": source["target_shell"],
        "shifted_square_window_group_count": len(rows),
        "all_shifted_square_window_groups_closed": all_rows_closed,
        "square_window_rows": rows,
        "shifted_square_window_global_bound_proved": False,
        "square_window_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "同步移位线性素数对继续和短条带端点联立："
            "`N_low=2q_4(q_2s-1)`、`N_high=q_2(2q_4s-1)`，"
            "且 `p^2=M*N_low-delta`。样本中 `M=57684`、`delta=527`，"
            "`p^2≡-527 (mod 57684)`，并且 "
            "`delta+M*span <= p-1 < delta+M*(span+1)`，"
            "所以 `s` 被平方窗口公式唯一恢复为 `132`。"
            "下一步硬点变为这种平方同余端点窗口的全局容量界，"
            "或登记 SquareWindow-PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 shifted square window",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"shifted_square_window_group_count={result['shifted_square_window_group_count']}",
        f"all_shifted_square_window_groups_closed={fmt_bool(result['all_shifted_square_window_groups_closed'])}",
        f"shifted_square_window_global_bound_proved={fmt_bool(result['shifted_square_window_global_bound_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 平方窗口",
        "",
        "| p | M | q2 | q4 | s | N low | N high | span | delta | residue | s recovered | closed |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in result["square_window_rows"]:
        lines.append(
            f"| {row['p']} | {row['base_modulus']} | {row['q2']} | {row['q4']} | "
            f"{row['s']} | {row['n_low']} | {row['n_high']} | {row['span']} | "
            f"{row['delta_low']} | {row['p_square_residue_mod_base']} | "
            f"{row['s_recovered_from_square_window']} | "
            f"{fmt_bool(row['shifted_square_window_closed_for_group'])} |"
        )
    lines.extend(
        [
            "",
            "## 2. 端点窗口不等式",
            "",
            "| delta_high | p-1 | next threshold | low floor | high floor | endpoint span |",
            "| ---: | ---: | ---: | --- | --- | --- |",
        ]
    )
    for row in result["square_window_rows"]:
        lines.append(
            f"| {row['delta_high']} | {row['p'] - 1} | "
            f"{row['delta_high'] + row['base_modulus']} | "
            f"{fmt_bool(row['low_endpoint_floor_closed'])} | "
            f"{fmt_bool(row['high_endpoint_floor_closed'])} | "
            f"{fmt_bool(row['endpoint_span_window_closed'])} |"
        )
    lines.extend(
        [
            "",
            "## 3. 自足小引理",
            "",
            "设 `M=2B`，端点移位对给出 `a_4=q_2s-1`、`a_2=2q_4s-1`。"
            "则归一条带端点为",
            "",
            "```text",
            "N_low=2q_4(q_2s-1),",
            "N_high=q_2(2q_4s-1),",
            "N_high-N_low=2q_4-q_2.",
            "```",
            "",
            "若 `p^2=M*N_low-delta` 且 "
            "`delta+M*(N_high-N_low) <= p-1 < delta+M*(N_high-N_low+1)`，"
            "则这两个归一半素数正好跨越 `p^2` 后长度 `p` 的端点窗口。"
            "同时 `s=(p^2+delta+2Mq_4)/(2Mq_2q_4)`，"
            "所以平方窗口会唯一锁定共同乘子。",
            "",
            "## 4. 证明边界",
            "",
            "- 已闭合：样本移位线性素数对等价于一个平方同余端点窗口。",
            "- 未闭合：全局平方窗口容量界，或 SquareWindow-PDEC 排斥。",
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
                "all_shifted_square_window_groups_closed": result[
                    "all_shifted_square_window_groups_closed"
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
