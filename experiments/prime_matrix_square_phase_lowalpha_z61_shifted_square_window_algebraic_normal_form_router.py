#!/usr/bin/env python3
"""审计 z=61 shifted-square-window companion 的代数正规形。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_shifted_square_window_algebraic_normal_form_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-shifted-square-window-algebraic-normal-form-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-shifted-square-window-algebraic-normal-form-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-shifted-square-window-algebraic-normal-form-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
MISMATCH_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-shifted-square-window-input-mismatch-router.json"
SHIFTED_FACTOR_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-endpoint-shifted-factor-router.json"
SQUARE_WINDOW_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-shifted-square-window-router.json"
OUT_JSON = (
    DOCS
    / "prime-matrix-square-phase-lowalpha-z61-shifted-square-window-algebraic-normal-form-router.json"
)
OUT_MD = (
    DOCS
    / "prime-matrix-square-phase-lowalpha-z61-shifted-square-window-algebraic-normal-form-router.md"
)

NEXT_TARGET = "QuadraticResidueClassPrimeTripleInputOrPersistentPhasePDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-shifted-square-window-input-mismatch-router.json",
    "prime-matrix-square-phase-lowalpha-z61-endpoint-shifted-factor-router.json",
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
        "experiments/prime_matrix_square_phase_lowalpha_z61_shifted_square_window_algebraic_normal_form_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        result[f"docs/monograph/{name}"] = file_sha256(DOCS / name)
    return result


def load(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def factor_integer(value: int) -> list[dict[str, int]]:
    """朴素分解小整数。"""
    n = value
    factors: list[dict[str, int]] = []
    candidate = 2
    while candidate * candidate <= n:
        exponent = 0
        while n % candidate == 0:
            n //= candidate
            exponent += 1
        if exponent:
            factors.append({"prime": candidate, "exponent": exponent, "prime_power": candidate**exponent})
        candidate += 1 if candidate == 2 else 2
    if n > 1:
        factors.append({"prime": n, "exponent": 1, "prime_power": n})
    return factors


def square_roots_mod(residue: int, modulus: int) -> list[int]:
    """枚举小模平方根。"""
    target = residue % modulus
    return [x for x in range(modulus) if (x * x - target) % modulus == 0]


def audit() -> dict[str, Any]:
    """执行代数正规形审计。"""
    mismatch = load(MISMATCH_JSON)
    shifted = load(SHIFTED_FACTOR_JSON)
    square = load(SQUARE_WINDOW_JSON)
    shifted_row = shifted["shifted_factor_rows"][0]
    square_row = square["square_window_rows"][0]

    m_value = square_row["base_modulus"]
    q2 = square_row["q2"]
    q4 = square_row["q4"]
    delta = square_row["delta_low"]
    s_value = square_row["s"]
    p_value = square_row["p"]
    a4 = shifted_row["a4"]
    a2 = shifted_row["a2"]

    # 从 a4=q2*s-1 与 N_low=2*q4*a4 得到 p^2=A*s-C。
    coefficient_a = 2 * m_value * q2 * q4
    constant_c = delta + 2 * m_value * q4
    recovered_square = coefficient_a * s_value - constant_c
    algebraic_square_identity_closed = recovered_square == p_value * p_value
    s_from_square = (p_value * p_value + constant_c) // coefficient_a
    s_integrality_closed = (p_value * p_value + constant_c) % coefficient_a == 0

    factors = factor_integer(coefficient_a)
    local_root_rows = []
    root_count = 1
    for item in factors:
        modulus = item["prime_power"]
        roots = square_roots_mod(-constant_c, modulus)
        root_count *= len(roots)
        local_root_rows.append(
            {
                **item,
                "target_residue": (-constant_c) % modulus,
                "root_count": len(roots),
                "roots": roots,
                "selected_p_residue": p_value % modulus,
                "selected_residue_is_root": p_value % modulus in roots,
            }
        )

    prime_triple_conditions = {
        "p_prime": p_value,
        "a4_prime": a4,
        "a2_prime": a2,
        "a4_formula": f"{q2}*s-1",
        "a2_formula": f"{2 * q4}*s-1",
        "s": s_value,
        "all_sample_prime_flags_imported": True,
    }
    normal_form_closed = (
        mismatch["registered_standard_route_matches_required_shape"] is False
        and algebraic_square_identity_closed
        and s_integrality_closed
        and all(row["selected_residue_is_root"] for row in local_root_rows)
        and a4 == q2 * s_value - 1
        and a2 == 2 * q4 * s_value - 1
    )

    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_shifted_square_window_algebraic_normal_form_router",
        "status": "z61_shifted_square_window_companion_reduced_to_quadratic_prime_triple_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "source_certificates": [
            mismatch["certificate_type"],
            shifted["certificate_type"],
            square["certificate_type"],
        ],
        "target_bucket": mismatch["target_bucket"],
        "target_omega": mismatch["target_omega"],
        "target_shell": mismatch["target_shell"],
        "m": m_value,
        "q2": q2,
        "q4": q4,
        "delta": delta,
        "coefficient_A": coefficient_a,
        "constant_C": constant_c,
        "normal_form_equation": "p^2 = A*s - C",
        "selected_s": s_value,
        "selected_p": p_value,
        "selected_a4": a4,
        "selected_a2": a2,
        "recovered_square": recovered_square,
        "s_from_square": s_from_square,
        "algebraic_square_identity_closed": algebraic_square_identity_closed,
        "s_integrality_closed": s_integrality_closed,
        "A_factorization": factors,
        "local_square_root_rows": local_root_rows,
        "crt_root_class_count_mod_A": root_count,
        "selected_p_mod_A": p_value % coefficient_a,
        "prime_triple_conditions": prime_triple_conditions,
        "shifted_square_window_algebraic_normal_form_closed_for_sample": normal_form_closed,
        "quadratic_residue_class_prime_triple_input_proved": False,
        "persistent_phase_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "shifted-square-window companion 可化为单一平方进位正规形："
            "`p^2=A*s-C`，其中 `A=2*M*q2*q4=303071736`、"
            "`C=delta+2*M*q4=4269143`。当前样本为 `s=132`、"
            "`p=200003`，并附加三个素性条件 `p`、`71s-1`、`74s-1` 为素数。"
            "因此剩余不是普通短区间素数命题，而是二次剩余类上的三重素性输入，"
            "或命名 PersistentPhase-PDEC 排斥。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 shifted-square-window algebraic normal form",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"A={result['coefficient_A']}",
        f"C={result['constant_C']}",
        f"selected_s={result['selected_s']}",
        f"selected_p={result['selected_p']}",
        f"p^2=A*s-C -> {result['algebraic_square_identity_closed']}",
        f"crt_root_class_count_mod_A={result['crt_root_class_count_mod_A']}",
        f"quadratic_residue_class_prime_triple_input_proved={fmt_bool(result['quadratic_residue_class_prime_triple_input_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 正规形",
        "",
        "| field | value |",
        "| --- | --- |",
        f"| equation | `{result['normal_form_equation']}` |",
        f"| A | `{result['coefficient_A']}` |",
        f"| C | `{result['constant_C']}` |",
        f"| selected square | `{result['selected_p']}^2 = {result['recovered_square']}` |",
        f"| recovered s | `{result['s_from_square']}` |",
        f"| a4, a2 | `{result['selected_a4']}, {result['selected_a2']}` |",
        "",
        "## 2. 模 A 平方根",
        "",
        "| modulus | target | root count | selected residue | selected is root |",
        "| ---: | ---: | ---: | ---: | --- |",
    ]
    for row in result["local_square_root_rows"]:
        lines.append(
            f"| {row['prime_power']} | {row['target_residue']} | {row['root_count']} | "
            f"{row['selected_p_residue']} | {fmt_bool(row['selected_residue_is_root'])} |"
        )
    lines.extend(
        [
            "",
            "## 3. 素性条件",
            "",
            "| condition | value |",
            "| --- | --- |",
            f"| p | `{result['prime_triple_conditions']['p_prime']}` |",
            f"| a4=71s-1 | `{result['prime_triple_conditions']['a4_prime']}` |",
            f"| a2=74s-1 | `{result['prime_triple_conditions']['a2_prime']}` |",
            f"| s | `{result['prime_triple_conditions']['s']}` |",
            "",
            "## 4. 证明边界",
            "",
            "- 已闭合：当前 companion 的代数正规形与 CRT 平方根分解。",
            "- 未闭合：二次剩余类上的三重素性输入，或 PersistentPhase-PDEC 排斥。",
            "- 结论：该输入强于普通短区间素数、单线性型 Dirichlet 或普通有界素数间隔。",
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
                "normal_form_closed": result[
                    "shifted_square_window_algebraic_normal_form_closed_for_sample"
                ],
                "crt_root_class_count_mod_A": result["crt_root_class_count_mod_A"],
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
