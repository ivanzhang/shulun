#!/usr/bin/env python3
"""登记 z=61 唯一精确商锁的 QuotientLock-PDEC 对象。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_quotient_lock_pdec_registration_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-quotient-lock-pdec-registration-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-quotient-lock-pdec-registration-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-quotient-lock-pdec-registration-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
SOURCE_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-core-quotient-lock-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-quotient-lock-pdec-registration-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-quotient-lock-pdec-registration-router.md"

NEXT_TARGET = "QuotientLockPDECExclusionByFixedCoreCheckOrGlobalTemplateBound"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-core-quotient-lock-router.json",
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
        "experiments/prime_matrix_square_phase_lowalpha_z61_quotient_lock_pdec_registration_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def audit() -> dict[str, Any]:
    """登记 QuotientLock-PDEC 对象。"""
    source = json.loads(SOURCE_JSON.read_text(encoding="utf-8"))
    sol = source["selected_solution"]
    a = sol["a"]
    b = sol["b"]
    c = sol["c"]
    q4 = sol["q4"]
    q2 = sol["q2"]
    core = a * b * c
    modulus = 12 * core
    pdec_record = {
        "formal_unit_key": (
            "z61|bucket=unbalanced<=8|omega=4|shell=(8D,16D]|"
            f"core={core}|factors={a},{b},{c}|q4={q4}|q2={q2}"
        ),
        "core": core,
        "modulus": modulus,
        "core_factorization": [a, b, c],
        "q4": q4,
        "q2": q2,
        "q4_lock": {
            "equation": source["q4_lock_equation"],
            "left_value": a * c + 6,
            "right_value": 7 * q4,
            "quotient": source["q4_exact_quotient"],
        },
        "q2_lock": {
            "equation": source["q2_lock_equation"],
            "left_value": a * b + 4,
            "right_value": 3 * q2,
            "quotient": source["q2_exact_quotient"],
        },
        "elimination_formula": source["eliminated_b_formula"],
        "m_residue_sources": {
            "mod_q4": modulus % q4,
            "mod_q2": modulus % q2,
            "expected_mod_q4": 1,
            "expected_mod_q2": b + c - 10,
        },
        "fixed_core_uniqueness_witness": source["positive_integer_solution_rows"],
    }
    registration_closed = (
        source["q4_exact_quotient_lock_closed"]
        and source["q2_exact_quotient_lock_closed"]
        and source["quotient_lock_unique_positive_integer_solution_proved"]
        and pdec_record["m_residue_sources"]["mod_q4"] == 1
        and pdec_record["m_residue_sources"]["mod_q2"] == q4 - 5
    )
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_quotient_lock_pdec_registration_router",
        "status": "z61_unique_quotient_lock_pdec_registered_not_excluded",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "source_certificate": source["certificate_type"],
        "target_bucket": source["target_bucket"],
        "target_omega": source["target_omega"],
        "target_shell": source["target_shell"],
        "quotient_lock_pdec_registration_closed": registration_closed,
        "quotient_lock_pdec_record": pdec_record,
        "fixed_core_candidate_count": len(source["positive_integer_solution_rows"]),
        "fixed_core_candidate_unique": len(source["positive_integer_solution_rows"]) == 1,
        "fixed_core_m_residue_sources_closed": (
            pdec_record["m_residue_sources"]["mod_q4"] == 1
            and pdec_record["m_residue_sources"]["mod_q2"] == q4 - 5
        ),
        "quotient_lock_pdec_excluded": False,
        "fixed_core_check_completed": False,
        "global_template_bound_proved": False,
        "row_column_unconditional_closed": False,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "唯一精确商锁已登记为固定核心 QuotientLock-PDEC：同模板失败不再有参数自由度，"
            "只能是 `core=4807=11*19*23`、`q4=37`、`q2=71`、`M=57684` 这一对象。"
            "这完成失败对象登记，但尚未排斥该固定核心。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    record = result["quotient_lock_pdec_record"]
    q4_lock = record["q4_lock"]
    q2_lock = record["q2_lock"]
    residues = record["m_residue_sources"]
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 QuotientLock-PDEC registration",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"quotient_lock_pdec_registration_closed={fmt_bool(result['quotient_lock_pdec_registration_closed'])}",
        f"fixed_core_candidate_unique={fmt_bool(result['fixed_core_candidate_unique'])}",
        f"fixed_core_m_residue_sources_closed={fmt_bool(result['fixed_core_m_residue_sources_closed'])}",
        f"quotient_lock_pdec_excluded={fmt_bool(result['quotient_lock_pdec_excluded'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. PDEC 对象",
        "",
        "| field | value |",
        "| --- | --- |",
        f"| formal unit | `{record['formal_unit_key']}` |",
        f"| core | `{record['core']}={record['core_factorization']}` |",
        f"| modulus | `{record['modulus']}` |",
        f"| q4/q2 | `{record['q4']}, {record['q2']}` |",
        f"| elimination | `{record['elimination_formula']}` |",
        "",
        "## 2. 商锁",
        "",
        "| side | equation | left | right | quotient |",
        "| --- | --- | ---: | ---: | ---: |",
        f"| q4 | `{q4_lock['equation']}` | {q4_lock['left_value']} | {q4_lock['right_value']} | {q4_lock['quotient']} |",
        f"| q2 | `{q2_lock['equation']}` | {q2_lock['left_value']} | {q2_lock['right_value']} | {q2_lock['quotient']} |",
        "",
        "## 3. 残差源复核",
        "",
        "| modulus | residue | expected |",
        "| ---: | ---: | ---: |",
        f"| {record['q4']} | {residues['mod_q4']} | {residues['expected_mod_q4']} |",
        f"| {record['q2']} | {residues['mod_q2']} | {residues['expected_mod_q2']} |",
        "",
        "## 4. 证明边界",
        "",
        "- 已闭合：QuotientLock-PDEC 的失败对象登记，并证明同模板只有一个固定核心候选。",
        "- 未闭合：对该固定核心做独立排斥检查，或证明全局模板界。",
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
                "quotient_lock_pdec_registration_closed": result[
                    "quotient_lock_pdec_registration_closed"
                ],
                "fixed_core_candidate_unique": result["fixed_core_candidate_unique"],
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
