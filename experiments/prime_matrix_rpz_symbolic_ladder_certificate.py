#!/usr/bin/env python3
"""生成 RPZ accepted-set 符号阶梯证书。

用法示例：
  python3 experiments/prime_matrix_rpz_symbolic_ladder_certificate.py
  python3 experiments/prime_matrix_rpz_symbolic_ladder_certificate.py --max-prime 97

本脚本攻击 formal-family avoidance 的下一硬点：不再把 `A_p` 看成
巨大相位集合，而是把它压成相邻素数下降中的一串局部数字约束

  delta_q(a_q)=-(a_q-1)(q-r) mod r <= q-r。

输出是一个可复核的阶梯账本：每一层列出允许数字数、失败余类和
候选接受相位计数公式；并在可枚举范围内逐相位核验该计数公式。

注意：这仍不是全局 formal-family avoidance 定理。它把剩余证明义务改写为：
正式反例族的起始相位必须逐层满足这些局部数字约束；若某层失败，
则已经进入 first-grid-fail seam/PDEC/ColumnCRT 出口。
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

from prime_matrix_rpz_formal_phase_automaton import (
    acceptance_checker,
    phase_delta,
    previous_prime,
    primes_upto,
    primorial,
)


def accepted_count_formula(primes: list[int], p: int) -> int:
    """返回符号阶梯给出的候选 `|A_p|`。"""
    if p == 2:
        return 2
    count = p
    current = p
    while current != 2:
        r = previous_prime(primes, current)
        if r is None:
            raise ValueError(f"no previous prime for {current}")
        count *= current - r + 1
        current = r
    return count


def transition_row(primes: list[int], p: int) -> dict[str, Any]:
    """构造一层局部数字约束。"""
    r = previous_prime(primes, p)
    if r is None:
        return {"p": p, "status": "base"}
    gap = p - r
    allowed_residues = [
        residue for residue in range(r) if phase_delta(p, r, residue) <= gap
    ]
    fail_residues = [
        residue for residue in range(r) if phase_delta(p, r, residue) > gap
    ]
    return {
        "p": p,
        "r": r,
        "gap": gap,
        "allowed_delta_count": gap + 1,
        "allowed_residues_mod_r": allowed_residues,
        "fail_residues_mod_r": fail_residues,
        "local_allowed_density": f"{gap + 1}/{r}",
    }


def enumerate_count(primes: list[int], p: int, max_modulus: int) -> dict[str, Any]:
    """在可承受范围内枚举核验 `|A_p|`。"""
    modulus = primorial(primes, p)
    formula_count = accepted_count_formula(primes, p)
    if modulus > max_modulus:
        return {
            "p": p,
            "modulus": modulus,
            "formula_count": formula_count,
            "enumerated": False,
            "match": None,
        }
    accepts = acceptance_checker(primes, p)
    enumerated_count = sum(1 for phase in range(modulus) if accepts(p, phase))
    return {
        "p": p,
        "modulus": modulus,
        "formula_count": formula_count,
        "enumerated": True,
        "enumerated_count": enumerated_count,
        "match": enumerated_count == formula_count,
    }


def build(max_prime: int, max_enum_modulus: int) -> dict[str, Any]:
    """构造符号阶梯证书。"""
    primes = primes_upto(max_prime)
    rows = []
    verification_rows = []
    for p in primes:
        modulus = primorial(primes, p)
        formula_count = accepted_count_formula(primes, p)
        density = Fraction(formula_count, modulus)
        rows.append(
            {
                "p": p,
                "modulus": modulus,
                "symbolic_accepted_count": formula_count,
                "symbolic_rejected_count": modulus - formula_count,
                "symbolic_density": f"{density.numerator}/{density.denominator}",
                "transition": transition_row(primes, p),
            }
        )
        verification_rows.append(enumerate_count(primes, p, max_enum_modulus))

    checked = [row for row in verification_rows if row["enumerated"]]
    return {
        "status": "rpz_symbolic_ladder_certificate_verified_not_global_avoidance",
        "parameters": {
            "max_prime": max_prime,
            "max_enum_modulus": max_enum_modulus,
        },
        "summary": {
            "prime_rows": len(rows),
            "enumerated_rows": len(checked),
            "enumerated_formula_mismatches": sum(
                1 for row in checked if not row["match"]
            ),
            "largest_enumerated_modulus": max(
                (row["modulus"] for row in checked), default=0
            ),
            "largest_symbolic_prime": rows[-1]["p"] if rows else None,
            "largest_symbolic_density": rows[-1]["symbolic_density"] if rows else None,
        },
        "rows": rows,
        "verification_rows": verification_rows,
        "theorem_boundary": [
            "若 formal start 的每层下降数字均满足 delta<=gap，则进入 A_p 并下降到 p=2。",
            "若某层首次违反 delta<=gap，则进入已物化 first-grid-fail seam。",
            "本证书尚未证明 formal-family start 必满足这些数字约束。",
            "下一硬点是把 BCB/TailAnchor/zero-row 结构转写为这些局部数字约束。",
        ],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 证书。"""
    summary = result["summary"]
    lines = [
        "# RPZ Accepted-Set 符号阶梯证书",
        "",
        "**状态：** `rpz_symbolic_ladder_certificate_verified_not_global_avoidance`",
        "",
        "## 总结",
        "",
        f"- 符号素数层数：`{summary['prime_rows']}`。",
        f"- 已逐相位枚举核验层数：`{summary['enumerated_rows']}`。",
        f"- 枚举计数公式不一致数：`{summary['enumerated_formula_mismatches']}`。",
        f"- 最大枚举模数：`{summary['largest_enumerated_modulus']}`。",
        f"- 最大符号素数：`{summary['largest_symbolic_prime']}`。",
        f"- 最大符号层接受密度：`{summary['largest_symbolic_density']}`。",
        "",
        "## 局部阶梯约束",
        "",
        "对相邻素数 `p>r`、`g=p-r`，定义",
        "",
        "```text",
        "delta_p(a)=-(a-1)g mod r。",
        "success iff delta_p(a)<=g；",
        "first fail iff delta_p(a)>g。",
        "```",
        "",
        "因此 formal-family 避开定理的真正目标不是枚举 `A_p`，而是证明正式起始相位沿下降链每层都满足该局部数字约束。",
        "",
        "## 符号计数表",
        "",
        "| p | modulus P(p) | symbolic accepted | symbolic rejected | density | fail residues at p->r |",
        "|---:|---:|---:|---:|---:|---|",
    ]
    for row in result["rows"]:
        transition = row["transition"]
        fail = transition.get("fail_residues_mod_r", [])
        lines.append(
            "| {p} | {modulus} | {accepted} | {rejected} | `{density}` | `{fail}` |".format(
                p=row["p"],
                modulus=row["modulus"],
                accepted=row["symbolic_accepted_count"],
                rejected=row["symbolic_rejected_count"],
                density=row["symbolic_density"],
                fail=fail,
            )
        )

    lines.extend(
        [
            "",
            "## 枚举核验",
            "",
            "| p | modulus | formula count | enumerated | enumerated count | match |",
            "|---:|---:|---:|---|---:|---|",
        ]
    )
    for row in result["verification_rows"]:
        lines.append(
            "| {p} | {modulus} | {formula} | `{enum}` | {count} | `{match}` |".format(
                p=row["p"],
                modulus=row["modulus"],
                formula=row["formula_count"],
                enum=row["enumerated"],
                count=row.get("enumerated_count", ""),
                match=row["match"],
            )
        )

    lines.extend(
        [
            "",
            "## 审稿边界",
            "",
            "本证书把 `A_p` 的可检查结构从大集合压成局部阶梯约束，并在可枚举范围内核验计数公式。",
            "它仍不证明全局 formal-family avoidance：尚需从 BCB 核心、TailAnchor 排除和条件零行结构中推出这些 `delta<=gap` 约束。",
            "",
            "下一步最小硬点：把正式反例起始行的构造公式写成 `a mod r` 的约束，并逐层证明它避开表中的 fail residues；否则按已物化 seam 出口处理。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-prime", type=int, default=97)
    parser.add_argument("--max-enum-modulus", type=int, default=10_000_000)
    parser.add_argument(
        "--out-prefix",
        type=Path,
        default=Path("docs/monograph/prime-matrix-rpz-symbolic-ladder-certificate"),
    )
    args = parser.parse_args()

    result = build(args.max_prime, args.max_enum_modulus)
    args.out_prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.out_prefix.with_suffix(".md"))
    print(json.dumps(result["summary"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
