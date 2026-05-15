#!/usr/bin/env python3
"""审计 z=61 平方窗口的 CRT 相位锁定结构。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_square_residue_phase_lock_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-square-residue-phase-lock-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-square-residue-phase-lock-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-square-residue-phase-lock-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from itertools import product
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
SOURCE_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-shifted-square-window-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-square-residue-phase-lock-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-square-residue-phase-lock-router.md"

NEXT_TARGET = "SquareResiduePhaseLockGlobalBoundOrCRTPhasePDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-shifted-square-window-router.json",
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
        "experiments/prime_matrix_square_phase_lowalpha_z61_square_residue_phase_lock_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def factorint(value: int) -> dict[int, int]:
    """试除分解整数。"""
    result: dict[int, int] = {}
    n_value = value
    divisor = 2
    while divisor * divisor <= n_value:
        while n_value % divisor == 0:
            result[divisor] = result.get(divisor, 0) + 1
            n_value //= divisor
        divisor += 1 if divisor == 2 else 2
    if n_value > 1:
        result[n_value] = result.get(n_value, 0) + 1
    return result


def square_roots_mod(delta: int, modulus: int) -> list[int]:
    """求 r^2 == -delta (mod modulus) 的全部根。"""
    return [residue for residue in range(modulus) if (residue * residue + delta) % modulus == 0]


def crt_pair(a1: int, m1: int, a2: int, m2: int) -> tuple[int, int]:
    """合并互素模数下的两个 CRT 条件。"""
    inv = pow(m1, -1, m2)
    t_value = ((a2 - a1) * inv) % m2
    modulus = m1 * m2
    return (a1 + m1 * t_value) % modulus, modulus


def crt_many(pairs: list[tuple[int, int]]) -> int:
    """合并互素 CRT 条件并返回最小非负解。"""
    residue, modulus = pairs[0]
    for next_residue, next_modulus in pairs[1:]:
        residue, modulus = crt_pair(residue, modulus, next_residue, next_modulus)
    return residue


def phase_lock_rows(source: dict[str, Any]) -> list[dict[str, Any]]:
    """把平方窗口压成 CRT 根相位与商锁定。"""
    rows = []
    for row in source["square_window_rows"]:
        p_value = row["p"]
        modulus = row["base_modulus"]
        delta = row["delta_low"]
        span = row["span"]
        factors = factorint(modulus)
        prime_power_roots = []
        root_options = []
        selected_vector = []
        for prime, exponent in sorted(factors.items()):
            prime_power = prime**exponent
            roots = square_roots_mod(delta, prime_power)
            selected = p_value % prime_power
            prime_power_roots.append(
                {
                    "prime_power": prime_power,
                    "roots": roots,
                    "selected_root": selected,
                    "selected_root_valid": selected in roots,
                }
            )
            root_options.append([(root, prime_power) for root in roots])
            selected_vector.append({"modulus": prime_power, "residue": selected})
        all_roots = sorted(crt_many(list(option)) for option in product(*root_options))
        selected_residue = p_value % modulus
        quotient = p_value // modulus
        residue_margin_left = selected_residue - 1 - delta
        residue_margin_right = modulus - residue_margin_left
        rows.append(
            {
                "p": p_value,
                "modulus": modulus,
                "delta": delta,
                "span": span,
                "quotient_floor_p_over_modulus": quotient,
                "selected_residue": selected_residue,
                "p_reconstruction_closed": p_value == quotient * modulus + selected_residue,
                "quotient_equals_span": quotient == span,
                "p_square_residue_mod_modulus": (p_value * p_value) % modulus,
                "negative_delta_residue_mod_modulus": (-delta) % modulus,
                "delta_congruence_closed": (p_value * p_value + delta) % modulus == 0,
                "modulus_factorization": factors,
                "delta_factorization": factorint(delta),
                "prime_power_roots": prime_power_roots,
                "selected_crt_vector": selected_vector,
                "crt_root_count": len(all_roots),
                "crt_roots": all_roots,
                "selected_residue_is_crt_root": selected_residue in all_roots,
                "root_density_numerator": len(all_roots),
                "root_density_denominator": modulus,
                "endpoint_residue_margin_left": residue_margin_left,
                "endpoint_residue_margin_right": residue_margin_right,
                "endpoint_residue_window_closed": 0 <= residue_margin_left < modulus,
                "phase_lock_closed_for_group": (
                    quotient == span
                    and selected_residue in all_roots
                    and (p_value * p_value + delta) % modulus == 0
                    and p_value == quotient * modulus + selected_residue
                    and 0 <= residue_margin_left < modulus
                ),
            }
        )
    return rows


def audit() -> dict[str, Any]:
    """执行 CRT 相位锁定审计。"""
    source = json.loads(SOURCE_JSON.read_text(encoding="utf-8"))
    rows = phase_lock_rows(source)
    all_rows_closed = bool(rows) and all(row["phase_lock_closed_for_group"] for row in rows)
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_square_residue_phase_lock_router",
        "status": "z61_square_window_reduced_to_crt_phase_lock_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "source_certificate": source["certificate_type"],
        "target_bucket": source["target_bucket"],
        "target_omega": source["target_omega"],
        "target_shell": source["target_shell"],
        "square_residue_phase_lock_group_count": len(rows),
        "all_square_residue_phase_locks_closed": all_rows_closed,
        "phase_lock_rows": rows,
        "square_residue_phase_lock_global_bound_proved": False,
        "crt_phase_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "平方窗口进一步压成有限 CRT 相位锁："
            "`M=57684=2^2*3*11*19*23`，`delta=527=17*31`，"
            "`p^2≡-527 (mod M)` 在每个素幂因子上只有两个根，"
            "总共 `32` 个 CRT 根相位。样本选中 `p mod M=26951`，"
            "并且 `floor(p/M)=span=3`，所以 `p=3M+26951`。"
            "下一步硬点变为全局 CRT 相位锁容量界，或登记 CRTPhase-PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 square residue phase lock",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"square_residue_phase_lock_group_count={result['square_residue_phase_lock_group_count']}",
        f"all_square_residue_phase_locks_closed={fmt_bool(result['all_square_residue_phase_locks_closed'])}",
        f"square_residue_phase_lock_global_bound_proved={fmt_bool(result['square_residue_phase_lock_global_bound_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. CRT 相位锁",
        "",
        "| p | M | delta | quotient | span | residue | root count | density | closed |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in result["phase_lock_rows"]:
        density = row["root_density_numerator"] / row["root_density_denominator"]
        lines.append(
            f"| {row['p']} | {row['modulus']} | {row['delta']} | "
            f"{row['quotient_floor_p_over_modulus']} | {row['span']} | "
            f"{row['selected_residue']} | {row['crt_root_count']} | "
            f"{density:.6f} | {fmt_bool(row['phase_lock_closed_for_group'])} |"
        )
    lines.extend(
        [
            "",
            "## 2. 素幂根",
            "",
            "| prime power | roots | selected | valid |",
            "| ---: | --- | ---: | --- |",
        ]
    )
    for row in result["phase_lock_rows"]:
        for item in row["prime_power_roots"]:
            lines.append(
                f"| {item['prime_power']} | `{item['roots']}` | "
                f"{item['selected_root']} | {fmt_bool(item['selected_root_valid'])} |"
            )
    lines.extend(
        [
            "",
            "## 3. 自足小引理",
            "",
            "平方窗口给出 `p^2≡-delta (mod M)`。若 `M` 的素幂分解固定，"
            "则合法 `p mod M` 必须落入各素幂根集的 CRT 组合。"
            "同时端点窗口要求 `floor(p/M)=span`，于是 `p=span*M+r`。"
            "因此该层失败对象不再是自由素数 `p`，而是少数 CRT 根相位中的素数。",
            "",
            "## 4. 证明边界",
            "",
            "- 已闭合：样本平方窗口等价于一个具体 CRT 根相位与商锁定。",
            "- 未闭合：全局 CRT 相位锁容量界，或 CRTPhase-PDEC 排斥。",
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
                "all_square_residue_phase_locks_closed": result[
                    "all_square_residue_phase_locks_closed"
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
