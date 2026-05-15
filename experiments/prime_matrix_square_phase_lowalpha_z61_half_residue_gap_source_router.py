#!/usr/bin/env python3
"""审计 z=61 gap-3 CRT 结构中的半模残差源。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_half_residue_gap_source_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-half-residue-gap-source-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-half-residue-gap-source-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-half-residue-gap-source-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
SOURCE_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-gap3-crt-structure-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-half-residue-gap-source-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-half-residue-gap-source-router.md"

NEXT_TARGET = "HalfResidueGapSourceGlobalBoundOrGapSourcePDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-gap3-crt-structure-router.json",
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
        "experiments/prime_matrix_square_phase_lowalpha_z61_half_residue_gap_source_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def factorize(n: int) -> list[int]:
    """朴素分解；当前只用于小证书整数。"""
    factors: list[int] = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        factors.append(n)
    return factors


def signed_residue(value: int, modulus: int) -> int:
    """返回对称最小代表。"""
    residue = value % modulus
    if residue > modulus // 2:
        return residue - modulus
    return residue


def audit() -> dict[str, Any]:
    """执行半模残差源审计。"""
    source = json.loads(SOURCE_JSON.read_text(encoding="utf-8"))
    modulus = source["modulus"]
    q4 = source["q4"]
    q2 = source["q2"]
    core = modulus // 12
    core_factors = factorize(core)
    modulus_factors = factorize(modulus)

    m_mod_q4 = modulus % q4
    m_mod_q2 = modulus % q2
    half_q4 = (m_mod_q4 * pow(2, -1, q4)) % q4
    half_q2 = (m_mod_q2 * pow(2, -1, q2)) % q2
    source_half_q4 = (q4 + 1) // 2
    source_half_q2 = (q4 - 5) // 2
    source_gap = source_half_q4 - source_half_q2
    source_signed_crt = source_half_q4 - 2 * q4

    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_half_residue_gap_source_router",
        "status": "z61_gap3_crt_structure_reduced_to_half_residue_gap_source_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "source_certificate": source["certificate_type"],
        "target_bucket": source["target_bucket"],
        "target_omega": source["target_omega"],
        "target_shell": source["target_shell"],
        "modulus": modulus,
        "modulus_factorization": modulus_factors,
        "core": core,
        "core_factorization": core_factors,
        "modulus_equals_12_core": modulus == 12 * core,
        "q4": q4,
        "q2": q2,
        "q2_equals_2q4_minus_3": q2 == 2 * q4 - 3,
        "m_mod_q4": m_mod_q4,
        "m_mod_q2": m_mod_q2,
        "m_mod_q4_source_value": 1,
        "m_mod_q2_source_value": q4 - 5,
        "m_mod_q4_source_closed": m_mod_q4 == 1,
        "m_mod_q2_source_closed": m_mod_q2 == q4 - 5,
        "core_mod_q4": core % q4,
        "core_mod_q2": core % q2,
        "core_mod_q4_signed": signed_residue(core, q4),
        "core_mod_q2_signed": signed_residue(core, q2),
        "half_q4": half_q4,
        "half_q2": half_q2,
        "half_q4_from_source_formula": source_half_q4,
        "half_q2_from_source_formula": source_half_q2,
        "half_residue_source_formulas_closed": half_q4 == source_half_q4 and half_q2 == source_half_q2,
        "half_residue_gap_from_source": source_gap,
        "half_residue_gap_matches_gap3": source_gap == source["half_residue_gap_a_minus_b"],
        "structural_signed_crt_from_source": source_signed_crt,
        "structural_signed_crt_matches_source": source_signed_crt == source["structural_signed_crt"],
        "gap_source_closed_for_formal_unit": (
            modulus == 12 * core
            and core_factors == [11, 19, 23]
            and q2 == 2 * q4 - 3
            and m_mod_q4 == 1
            and m_mod_q2 == q4 - 5
            and half_q4 == source_half_q4
            and half_q2 == source_half_q2
            and source_gap == 3
            and source_signed_crt == source["structural_signed_crt"]
        ),
        "half_residue_gap_source_global_bound_proved": False,
        "gap_source_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "gap-3 CRT 的差值 `a-b=3` 可继续上提为半模残差源模板："
            "`M≡1 (mod 37)` 强制 `M/2≡(37+1)/2=19`，"
            "`M≡37-5=32 (mod 71)` 强制 `M/2≡(37-5)/2=16`。"
            "因此 `19-16=3`，并继续给出 `19-2*37=-55`。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 half-residue gap source",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"modulus_equals_12_core={fmt_bool(result['modulus_equals_12_core'])}",
        f"q2_equals_2q4_minus_3={fmt_bool(result['q2_equals_2q4_minus_3'])}",
        f"m_mod_q4_source_closed={fmt_bool(result['m_mod_q4_source_closed'])}",
        f"m_mod_q2_source_closed={fmt_bool(result['m_mod_q2_source_closed'])}",
        f"half_residue_gap_from_source={result['half_residue_gap_from_source']}",
        f"structural_signed_crt_from_source={result['structural_signed_crt_from_source']}",
        f"gap_source_closed_for_formal_unit={fmt_bool(result['gap_source_closed_for_formal_unit'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 上游因子源",
        "",
        "| M | factorization | core | core factorization |",
        "| ---: | --- | ---: | --- |",
        f"| {result['modulus']} | `{result['modulus_factorization']}` | "
        f"{result['core']} | `{result['core_factorization']}` |",
        "",
        "这里 `M=12C`，`C=11*19*23`，与前序 common-core 证书中的核心一致。",
        "",
        "## 2. 残差源模板",
        "",
        "| modulus | M residue | source value | half residue | formula |",
        "| ---: | ---: | ---: | ---: | ---: |",
        f"| {result['q4']} | {result['m_mod_q4']} | {result['m_mod_q4_source_value']} | "
        f"{result['half_q4']} | {result['half_q4_from_source_formula']} |",
        f"| {result['q2']} | {result['m_mod_q2']} | {result['m_mod_q2_source_value']} | "
        f"{result['half_q2']} | {result['half_q2_from_source_formula']} |",
        "",
        "若同时有 `q2=2q4-3`、`M≡1 (mod q4)`、`M≡q4-5 (mod q2)`，则",
        "",
        "```text",
        "a = M/2 mod q4 = (q4+1)/2,",
        "b = M/2 mod q2 = (q4-5)/2,",
        "a-b = 3,",
        "x = a-2q4.",
        "```",
        "",
        "在当前 formal unit 中，`x=19-74=-55`。",
        "",
        "## 3. 证明边界",
        "",
        "- 已闭合：`-55` 的来源从 gap-3 CRT 进一步上提到 `M` 的两个残差源。",
        "- 未闭合：全局证明这种残差源模板不能形成持续贴边，或登记并排斥 GapSource-PDEC。",
        f"- 下一目标：`{result['next_direct_attack_target']}`。",
        "",
        "## 4. 依赖哈希",
        "",
        "| file | sha256 |",
        "| --- | --- |",
    ]
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
                "gap_source_closed_for_formal_unit": result["gap_source_closed_for_formal_unit"],
                "half_residue_gap_from_source": result["half_residue_gap_from_source"],
                "structural_signed_crt_from_source": result["structural_signed_crt_from_source"],
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
