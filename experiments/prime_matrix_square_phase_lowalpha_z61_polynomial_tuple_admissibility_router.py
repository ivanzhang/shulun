#!/usr/bin/env python3
"""审计 z=61 多项式素性三元组的精确可容许性边界。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_polynomial_tuple_admissibility_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-polynomial-tuple-admissibility-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-polynomial-tuple-admissibility-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-polynomial-tuple-admissibility-router.md
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
SOURCE_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-quadratic-prime-triple-param-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-polynomial-tuple-admissibility-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-polynomial-tuple-admissibility-router.md"

NEXT_TARGET = "SchinzelHypothesisHLevelInputOrPersistentPhasePDECExclusion"


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def file_sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖哈希。"""
    return {
        "docs/monograph/prime-matrix-square-phase-lowalpha-z61-quadratic-prime-triple-param-router.json": file_sha256(
            SOURCE_JSON
        ),
        "experiments/prime_matrix_square_phase_lowalpha_z61_polynomial_tuple_admissibility_router.py": file_sha256(
            Path(__file__).resolve()
        ),
    }


def load(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def coeff_gcd(coefficients: list[int]) -> int:
    """计算多项式系数最大公因数。"""
    result = 0
    for value in coefficients:
        result = math.gcd(result, abs(value))
    return result


def trim_leading(coefficients: list[int]) -> list[int]:
    """去掉高位零系数，保留从高到低的表示。"""
    result = coefficients[:]
    while len(result) > 1 and result[0] == 0:
        result.pop(0)
    return result


def multiply_poly(left: list[int], right: list[int]) -> list[int]:
    """相乘两个从高到低排列的多项式。"""
    left = trim_leading(left)
    right = trim_leading(right)
    result = [0] * (len(left) + len(right) - 1)
    for i, a_value in enumerate(left):
        for j, b_value in enumerate(right):
            result[i + j] += a_value * b_value
    return trim_leading(result)


def eval_poly(coefficients: list[int], t_value: int) -> int:
    """Horner 法计算从高到低排列的多项式。"""
    value = 0
    for coefficient in coefficients:
        value = value * t_value + coefficient
    return value


def primes_upto(n: int) -> list[int]:
    """生成小素数。"""
    primes: list[int] = []
    for value in range(2, n + 1):
        if all(value % prime for prime in primes if prime * prime <= value):
            primes.append(value)
    return primes


def discriminant_quadratic(coefficients: list[int]) -> int | None:
    """返回二次多项式判别式。"""
    coefficients = trim_leading(coefficients)
    if len(coefficients) != 3:
        return None
    a_value, b_value, c_value = coefficients
    return b_value * b_value - 4 * a_value * c_value


def is_square_integer(value: int) -> bool:
    """判断整数是否为平方数。"""
    if value < 0:
        return False
    root = math.isqrt(value)
    return root * root == value


def audit() -> dict[str, Any]:
    """执行精确可容许性审计。"""
    source = load(SOURCE_JSON)
    p_poly = source["p_polynomial"]["coefficients_c2_c1_c0"]
    a4_poly = source["a4_polynomial"]["coefficients_c2_c1_c0"]
    a2_poly = source["a2_polynomial"]["coefficients_c2_c1_c0"]
    prime_polys = [
        {"name": "p(t)", "coefficients": p_poly},
        {"name": "a4(t)", "coefficients": a4_poly},
        {"name": "a2(t)", "coefficients": a2_poly},
    ]

    poly_rows = []
    product_poly = [1]
    for item in prime_polys:
        coefficients = trim_leading(item["coefficients"])
        degree = len(coefficients) - 1
        content = coeff_gcd(coefficients)
        discriminant = discriminant_quadratic(coefficients)
        irreducible = degree == 1 or (
            degree == 2 and discriminant is not None and not is_square_integer(discriminant)
        )
        poly_rows.append(
            {
                "name": item["name"],
                "degree": degree,
                "coefficients": coefficients,
                "content": content,
                "primitive": content == 1,
                "discriminant": discriminant,
                "irreducible_over_Z": irreducible,
            }
        )
        product_poly = multiply_poly(product_poly, coefficients)

    product_degree = len(product_poly) - 1
    product_content = coeff_gcd(product_poly)
    candidate_fixed_primes = primes_upto(product_degree)
    fixed_prime_rows = []
    no_fixed_prime_divisor = product_content == 1
    for prime in candidate_fixed_primes:
        survivors = [
            residue for residue in range(prime) if eval_poly(product_poly, residue) % prime != 0
        ]
        fixed = len(survivors) == 0
        if fixed:
            no_fixed_prime_divisor = False
        fixed_prime_rows.append(
            {
                "prime": prime,
                "surviving_residue_count": len(survivors),
                "surviving_residues": survivors,
                "fixed_prime_divisor": fixed,
            }
        )

    exact_admissibility_closed = (
        all(row["primitive"] and row["irreducible_over_Z"] for row in poly_rows)
        and product_content == 1
        and no_fixed_prime_divisor
    )

    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_polynomial_tuple_admissibility_router",
        "status": "z61_polynomial_prime_tuple_admissible_but_requires_schinzel_level_input_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "source_certificate": source["certificate_type"],
        "target_bucket": source["target_bucket"],
        "target_omega": source["target_omega"],
        "target_shell": source["target_shell"],
        "polynomial_rows": poly_rows,
        "product_polynomial_coefficients": product_poly,
        "product_degree": product_degree,
        "product_content": product_content,
        "fixed_prime_divisor_candidates_by_degree_bound": candidate_fixed_primes,
        "fixed_prime_rows": fixed_prime_rows,
        "no_fixed_prime_divisor_proved": no_fixed_prime_divisor,
        "exact_admissibility_closed": exact_admissibility_closed,
        "schinzel_hypothesis_h_level_input_proved": False,
        "bateman_horn_level_input_proved": False,
        "persistent_phase_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "当前三元组 `p(t),a4(t),a2(t)` 已经精确可容许：三个多项式均为 primitive，"
            "`p(t)` 线性不可约，两个二次多项式判别式非平方，因此在 Z 上不可约；"
            "乘积多项式 degree=5 且 content=1。若存在固定素因子，除非素数不超过 degree，"
            "否则非零多项式模该素数不可能在所有剩余类上为零；检查 2,3,5 均有幸存类。"
            "所以局部障碍路线关闭。剩余正是 Schinzel Hypothesis H / Bateman-Horn 等级的"
            "多项式素性输入，或 PersistentPhase-PDEC 排斥。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 polynomial tuple admissibility",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"product_degree={result['product_degree']}",
        f"product_content={result['product_content']}",
        f"no_fixed_prime_divisor_proved={fmt_bool(result['no_fixed_prime_divisor_proved'])}",
        f"exact_admissibility_closed={fmt_bool(result['exact_admissibility_closed'])}",
        f"schinzel_hypothesis_h_level_input_proved={fmt_bool(result['schinzel_hypothesis_h_level_input_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 多项式验收",
        "",
        "| polynomial | degree | content | discriminant | irreducible |",
        "| --- | ---: | ---: | ---: | --- |",
    ]
    for row in result["polynomial_rows"]:
        lines.append(
            f"| `{row['name']}` | {row['degree']} | {row['content']} | "
            f"{row['discriminant']} | {fmt_bool(row['irreducible_over_Z'])} |"
        )
    lines.extend(
        [
            "",
            "## 2. 固定素因子",
            "",
            "| prime | surviving residues | fixed divisor |",
            "| ---: | --- | --- |",
        ]
    )
    for row in result["fixed_prime_rows"]:
        lines.append(
            f"| {row['prime']} | `{row['surviving_residues']}` | "
            f"{fmt_bool(row['fixed_prime_divisor'])} |"
        )
    lines.extend(
        [
            "",
            "## 3. 精确引理",
            "",
            "令 `F(t)=p(t)a4(t)a2(t)`，`deg F=5` 且 `content(F)=1`。"
            "若某素数 `ell>5` 对所有整数 `t` 都整除 `F(t)`，则 `F mod ell` "
            "作为非零次数至多 5 的多项式会在 `ell>5` 个剩余类上全为零，矛盾。"
            "因此只需检查 `ell<=5`；`2,3,5` 均有幸存剩余类，所以没有固定素因子。",
            "",
            "## 4. 证明边界",
            "",
            "- 已闭合：primitive、不可约、无固定素因子，即精确可容许性。",
            "- 未闭合：可容许多项式三元组是否取同步素值；这是 Schinzel/Bateman-Horn 等级输入。",
            "- 结论：不能从可容许性推出无条件全局 companion。",
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
                "exact_admissibility_closed": result["exact_admissibility_closed"],
                "no_fixed_prime_divisor_proved": result["no_fixed_prime_divisor_proved"],
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
