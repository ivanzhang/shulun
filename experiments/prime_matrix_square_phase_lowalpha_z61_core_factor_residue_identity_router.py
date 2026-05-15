#!/usr/bin/env python3
"""审计 z=61 半模残差源中的核心因子同余身份。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_core_factor_residue_identity_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-core-factor-residue-identity-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-core-factor-residue-identity-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-core-factor-residue-identity-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
SOURCE_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-half-residue-gap-source-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-core-factor-residue-identity-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-core-factor-residue-identity-router.md"

NEXT_TARGET = "CoreFactorResidueIdentityGlobalBoundOrCoreFactorPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-half-residue-gap-source-router.json",
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
        "experiments/prime_matrix_square_phase_lowalpha_z61_core_factor_residue_identity_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def signed_residue(value: int, modulus: int) -> int:
    """返回对称最小代表。"""
    residue = value % modulus
    if residue > modulus // 2:
        return residue - modulus
    return residue


def audit() -> dict[str, Any]:
    """执行核心因子同余身份审计。"""
    source = json.loads(SOURCE_JSON.read_text(encoding="utf-8"))
    core = source["core"]
    factors = source["core_factorization"]
    q4 = source["q4"]
    q2 = source["q2"]
    f11, f19, f23 = factors

    q4_anchor_gap = 2 * f19 - q4
    q2_anchor_gap = q2 - 3 * f23
    q4_pair = f11 * f23
    q2_pair = f11 * f19

    two_core_mod_q4 = (2 * core) % q4
    three_core_mod_q2 = (3 * core) % q2
    twelve_core_mod_q4 = (12 * core) % q4
    twelve_core_mod_q2 = (12 * core) % q2

    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_core_factor_residue_identity_router",
        "status": "z61_half_residue_gap_source_reduced_to_core_factor_identities_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "source_certificate": source["certificate_type"],
        "target_bucket": source["target_bucket"],
        "target_omega": source["target_omega"],
        "target_shell": source["target_shell"],
        "core": core,
        "core_factorization": factors,
        "q4": q4,
        "q2": q2,
        "q4_anchor_factor": f19,
        "q4_anchor_identity": "q4=2*19-1",
        "q4_anchor_gap_2f19_minus_q4": q4_anchor_gap,
        "q4_pair_11_23_mod": q4_pair % q4,
        "q4_pair_11_23_signed": signed_residue(q4_pair, q4),
        "two_core_mod_q4": two_core_mod_q4,
        "two_core_mod_q4_signed": signed_residue(two_core_mod_q4, q4),
        "core_mod_q4": core % q4,
        "core_mod_q4_signed": signed_residue(core, q4),
        "twelve_core_mod_q4": twelve_core_mod_q4,
        "twelve_core_mod_q4_matches_m_source": twelve_core_mod_q4 == source["m_mod_q4_source_value"],
        "q2_anchor_factor": f23,
        "q2_anchor_identity": "q2=3*23+2",
        "q2_anchor_gap_q2_minus_3f23": q2_anchor_gap,
        "q2_pair_11_19_mod": q2_pair % q2,
        "q2_pair_11_19_signed": signed_residue(q2_pair, q2),
        "three_core_mod_q2": three_core_mod_q2,
        "three_core_mod_q2_signed": signed_residue(three_core_mod_q2, q2),
        "core_mod_q2": core % q2,
        "core_mod_q2_signed": signed_residue(core, q2),
        "twelve_core_mod_q2": twelve_core_mod_q2,
        "twelve_core_mod_q2_matches_m_source": twelve_core_mod_q2 == source["m_mod_q2_source_value"],
        "core_factor_residue_identity_closed_for_formal_unit": (
            factors == [11, 19, 23]
            and q4_anchor_gap == 1
            and signed_residue(q4_pair, q4) == -6
            and signed_residue(two_core_mod_q4, q4) == -6
            and signed_residue(core, q4) == -3
            and twelve_core_mod_q4 == 1
            and q2_anchor_gap == 2
            and signed_residue(q2_pair, q2) == -4
            and three_core_mod_q2 == 8
            and signed_residue(core, q2) == -21
            and twelve_core_mod_q2 == source["m_mod_q2_source_value"]
        ),
        "core_factor_residue_identity_global_bound_proved": False,
        "core_factor_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "`M` 的两个残差源来自核心 `C=11*19*23` 的两个小同余身份："
            "`37=2*19-1` 使 `2C≡11*23≡-6 (mod37)`，故 `C≡-3`、"
            "`12C≡1`；`71=3*23+2` 且 `11*19≡-4 (mod71)`，故 "
            "`3C≡8`、`12C≡32=37-5`。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 core factor residue identity",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"q4_anchor_gap_2f19_minus_q4={result['q4_anchor_gap_2f19_minus_q4']}",
        f"q4_pair_11_23_signed={result['q4_pair_11_23_signed']}",
        f"core_mod_q4_signed={result['core_mod_q4_signed']}",
        f"twelve_core_mod_q4={result['twelve_core_mod_q4']}",
        f"q2_anchor_gap_q2_minus_3f23={result['q2_anchor_gap_q2_minus_3f23']}",
        f"q2_pair_11_19_signed={result['q2_pair_11_19_signed']}",
        f"core_mod_q2_signed={result['core_mod_q2_signed']}",
        f"twelve_core_mod_q2={result['twelve_core_mod_q2']}",
        f"core_factor_residue_identity_closed_for_formal_unit={fmt_bool(result['core_factor_residue_identity_closed_for_formal_unit'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. q4 侧身份",
        "",
        "| identity | value | consequence |",
        "| --- | ---: | --- |",
        f"| `{result['q4_anchor_identity']}` | {result['q4_anchor_gap_2f19_minus_q4']} | `2*19≡1 (mod37)` |",
        f"| `11*23 mod37` | {result['q4_pair_11_23_mod']} | signed `{result['q4_pair_11_23_signed']}` |",
        f"| `2C mod37` | {result['two_core_mod_q4']} | signed `{result['two_core_mod_q4_signed']}` |",
        f"| `C mod37` | {result['core_mod_q4']} | signed `{result['core_mod_q4_signed']}` |",
        f"| `12C mod37` | {result['twelve_core_mod_q4']} | gives `M≡1` |",
        "",
        "## 2. q2 侧身份",
        "",
        "| identity | value | consequence |",
        "| --- | ---: | --- |",
        f"| `{result['q2_anchor_identity']}` | {result['q2_anchor_gap_q2_minus_3f23']} | `3*23≡-2 (mod71)` |",
        f"| `11*19 mod71` | {result['q2_pair_11_19_mod']} | signed `{result['q2_pair_11_19_signed']}` |",
        f"| `3C mod71` | {result['three_core_mod_q2']} | signed `{result['three_core_mod_q2_signed']}` |",
        f"| `C mod71` | {result['core_mod_q2']} | signed `{result['core_mod_q2_signed']}` |",
        f"| `12C mod71` | {result['twelve_core_mod_q2']} | gives `M≡37-5` |",
        "",
        "## 3. 证明边界",
        "",
        "- 已闭合：`M` 的两个残差源已经拆为 `C` 的核心因子同余身份。",
        "- 未闭合：全局排斥这种核心因子身份模板持续导致贴边，或登记 CoreFactor-PDEC。",
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
                "core_factor_residue_identity_closed_for_formal_unit": result[
                    "core_factor_residue_identity_closed_for_formal_unit"
                ],
                "twelve_core_mod_q4": result["twelve_core_mod_q4"],
                "twelve_core_mod_q2": result["twelve_core_mod_q2"],
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
