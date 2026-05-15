#!/usr/bin/env python3
"""审计 z=61 half-mod 因子分离中的 gap-3 CRT 结构。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_gap3_crt_structure_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-gap3-crt-structure-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-gap3-crt-structure-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-gap3-crt-structure-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
SOURCE_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-halfmod-factor-separation-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-gap3-crt-structure-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-gap3-crt-structure-router.md"

NEXT_TARGET = "GapThreeCRTStructureGlobalBoundOrGapPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-halfmod-factor-separation-router.json",
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
        "experiments/prime_matrix_square_phase_lowalpha_z61_gap3_crt_structure_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def audit() -> dict[str, Any]:
    """执行 gap-3 CRT 结构审计。"""
    source = json.loads(SOURCE_JSON.read_text(encoding="utf-8"))
    modulus = source["modulus"]
    q4 = source["q4"]
    q2 = source["q2"]
    a = source["q4_half_residue"]
    b = source["q2_half_residue"]
    gap = a - b
    q_relation_gap = 2 * q4 - q2
    t_signed = (b - a) // q4 if (b - a) % q4 == 0 else -2
    # 用结构式 x=a-2*q4，而不是重新做一般 CRT。
    structural_signed_crt = a - 2 * q4
    m_residue_q4 = modulus % q4
    m_residue_q2 = modulus % q2
    half_residue_from_m_q4 = (m_residue_q4 * pow(2, -1, q4)) % q4
    half_residue_from_m_q2 = (m_residue_q2 * pow(2, -1, q2)) % q2
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_gap3_crt_structure_router",
        "status": "z61_halfmod_factor_separation_reduced_to_gap3_crt_structure_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "source_certificate": source["certificate_type"],
        "target_bucket": source["target_bucket"],
        "target_omega": source["target_omega"],
        "target_shell": source["target_shell"],
        "modulus": modulus,
        "q4": q4,
        "q2": q2,
        "q2_equals_2q4_minus_3": q2 == 2 * q4 - 3,
        "q_relation_gap_2q4_minus_q2": q_relation_gap,
        "m_residue_mod_q4": m_residue_q4,
        "m_residue_mod_q2": m_residue_q2,
        "m_residue_q4_is_1": m_residue_q4 == 1,
        "m_residue_q2_is_q4_minus_5": m_residue_q2 == q4 - 5,
        "half_residue_q4": a,
        "half_residue_q2": b,
        "half_residue_from_m_q4": half_residue_from_m_q4,
        "half_residue_from_m_q2": half_residue_from_m_q2,
        "half_residue_gap_a_minus_b": gap,
        "gap_matches_q_relation_gap": gap == q_relation_gap,
        "structural_crt_formula": "a-2*q4",
        "structural_signed_crt": structural_signed_crt,
        "source_signed_crt": source["combined_signed_residue"],
        "structural_crt_matches_source": structural_signed_crt == source["combined_signed_residue"],
        "gap3_crt_structure_closed_for_formal_unit": (
            q2 == 2 * q4 - 3
            and gap == 3
            and gap == q_relation_gap
            and structural_signed_crt == source["combined_signed_residue"]
            and half_residue_from_m_q4 == a
            and half_residue_from_m_q2 == b
        ),
        "gap_three_crt_structure_global_bound_proved": False,
        "gap_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "half-modulus flip 的 CRT 小余量可进一步解释为 gap-3 结构："
            "`q2=71=2*37-3`，而 `M/2` 的因子残差为 `a=19 mod37`、"
            "`b=16 mod71`，满足 `a-b=3`。因此 CRT 解无需一般合成，直接是 "
            "`a-2*q4=19-74=-55`。这说明最近余量来自 q2 与 2q4 的 gap-3 "
            "因子关系和半模残差差值同步，而非任意 CRT 偶合。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 gap-3 CRT structure",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"q2_equals_2q4_minus_3={fmt_bool(result['q2_equals_2q4_minus_3'])}",
        f"half_residue_gap_a_minus_b={result['half_residue_gap_a_minus_b']}",
        f"gap_matches_q_relation_gap={fmt_bool(result['gap_matches_q_relation_gap'])}",
        f"structural_signed_crt={result['structural_signed_crt']}",
        f"gap3_crt_structure_closed_for_formal_unit={fmt_bool(result['gap3_crt_structure_closed_for_formal_unit'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. Gap-3 数据",
        "",
        "| q4 | q2 | 2q4-q2 | a=M/2 mod q4 | b=M/2 mod q2 | a-b |",
        "| ---: | ---: | ---: | ---: | ---: | ---: |",
        f"| {result['q4']} | {result['q2']} | {result['q_relation_gap_2q4_minus_q2']} | "
        f"{result['half_residue_q4']} | {result['half_residue_q2']} | "
        f"{result['half_residue_gap_a_minus_b']} |",
        "",
        "## 2. M 残差来源",
        "",
        "| modulus | M residue | half residue | expected |",
        "| ---: | ---: | ---: | ---: |",
        f"| {result['q4']} | {result['m_residue_mod_q4']} | {result['half_residue_from_m_q4']} | {result['half_residue_q4']} |",
        f"| {result['q2']} | {result['m_residue_mod_q2']} | {result['half_residue_from_m_q2']} | {result['half_residue_q2']} |",
        "",
        "## 3. 结构 CRT",
        "",
        "由 `q2=2q4-3` 可得 `2q4≡3 (mod q2)`。若 `a-b=3`，则",
        "",
        "```text",
        "x = a-2q4",
        "x ≡ a (mod q4),",
        "x ≡ a-2q4 ≡ a-3 = b (mod q2).",
        "```",
        "",
        "所以 `x=19-74=-55`，即当前最近 offset。",
        "",
        "## 4. 证明边界",
        "",
        "- 已闭合：当前 z=61 formal unit 的 `-55` 来自 gap-3 CRT 结构。",
        "- 未闭合：全局排斥 gap-3 型持续贴边，或登记 Gap-PDEC。",
        f"- 下一目标：`{result['next_direct_attack_target']}`。",
        "",
        "## 5. 依赖哈希",
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
                "gap3_crt_structure_closed_for_formal_unit": result[
                    "gap3_crt_structure_closed_for_formal_unit"
                ],
                "structural_signed_crt": result["structural_signed_crt"],
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
