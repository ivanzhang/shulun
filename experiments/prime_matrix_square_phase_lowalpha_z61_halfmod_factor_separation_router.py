#!/usr/bin/env python3
"""审计 z=61 half-modulus flip 在 37/71 因子上的分离。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_halfmod_factor_separation_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-halfmod-factor-separation-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-halfmod-factor-separation-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-halfmod-factor-separation-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
SOURCE_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-offset55-halfmod-flip-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-halfmod-factor-separation-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-halfmod-factor-separation-router.md"

NEXT_TARGET = "HalfModulusFlipFactorSeparationGlobalBoundOrFactorPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-offset55-halfmod-flip-router.json",
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
        "experiments/prime_matrix_square_phase_lowalpha_z61_halfmod_factor_separation_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def signed_residue(value: int, modulus: int) -> int:
    """返回最小绝对值代表。"""
    residue = value % modulus
    if residue > modulus // 2:
        residue -= modulus
    return residue


def crt_pair(a: int, mod_a: int, b: int, mod_b: int) -> int:
    """合成两个互素模的最小非负 CRT 代表。"""
    return (a + mod_a * (((b - a) * pow(mod_a, -1, mod_b)) % mod_b)) % (mod_a * mod_b)


def audit() -> dict[str, Any]:
    """执行因子分离审计。"""
    source = json.loads(SOURCE_JSON.read_text(encoding="utf-8"))
    modulus = source["modulus"]
    target_modulus = source["target_modulus"]
    half = source["expected_half_modulus"]
    q4 = 37
    q2 = 71
    q4_residue = half % q4
    q2_residue = half % q2
    q4_signed = signed_residue(half, q4)
    q2_signed = signed_residue(half, q2)
    combined = crt_pair(q4_residue, q4, q2_residue, q2)
    combined_signed = signed_residue(combined, target_modulus)
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_halfmod_factor_separation_router",
        "status": "z61_half_modulus_flip_reduced_to_factor_separation_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "source_certificate": source["certificate_type"],
        "target_bucket": source["target_bucket"],
        "target_omega": source["target_omega"],
        "target_shell": source["target_shell"],
        "modulus": modulus,
        "half_modulus": half,
        "target_modulus": target_modulus,
        "q4": q4,
        "q2": q2,
        "q4_half_residue": q4_residue,
        "q2_half_residue": q2_residue,
        "q4_half_signed_residue": q4_signed,
        "q2_half_signed_residue": q2_signed,
        "combined_crt_residue": combined,
        "combined_signed_residue": combined_signed,
        "combined_circular_margin": abs(combined_signed),
        "factor_residues_nonzero": q4_residue != 0 and q2_residue != 0,
        "combined_matches_source_separation": combined_signed == source["signed_separation_mod_target"],
        "halfmod_factor_separation_closed_for_formal_unit": (
            q4_residue != 0
            and q2_residue != 0
            and combined_signed == -55
            and abs(combined_signed) == source["separation_circular_margin"]
        ),
        "half_modulus_flip_factor_separation_global_bound_proved": False,
        "factor_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "half-modulus flip 的最近分离可在素因子上解释：`M/2=28842` 在 `37` 下为 "
            "`19`（最小代表 `-18`），在 `71` 下为 `16`。这两个非零因子残差经 CRT "
            "合成后得到 `2572≡-55 mod 2627`，正是上一层最近 offset。"
            "因此 exact collision 已由两个因子非零排除；全局剩余是证明这种 CRT 合成"
            "不会持久贴近 0，或登记 Factor-PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 half-mod factor separation",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"half_modulus={result['half_modulus']}",
        f"q4_half_residue={result['q4_half_residue']}",
        f"q2_half_residue={result['q2_half_residue']}",
        f"combined_signed_residue={result['combined_signed_residue']}",
        f"combined_circular_margin={result['combined_circular_margin']}",
        f"halfmod_factor_separation_closed_for_formal_unit={fmt_bool(result['halfmod_factor_separation_closed_for_formal_unit'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 因子分离",
        "",
        "| factor | residue of M/2 | signed residue | nonzero |",
        "| ---: | ---: | ---: | --- |",
        f"| {result['q4']} | {result['q4_half_residue']} | {result['q4_half_signed_residue']} | {fmt_bool(result['q4_half_residue'] != 0)} |",
        f"| {result['q2']} | {result['q2_half_residue']} | {result['q2_half_signed_residue']} | {fmt_bool(result['q2_half_residue'] != 0)} |",
        "",
        "## 2. CRT 合成",
        "",
        "| modulus | CRT residue | signed residue | circular margin |",
        "| ---: | ---: | ---: | ---: |",
        f"| {result['target_modulus']} | {result['combined_crt_residue']} | {result['combined_signed_residue']} | {result['combined_circular_margin']} |",
        "",
        "## 3. 自足小引理",
        "",
        "若 half-modulus flip 造成 exact collision，则必须有",
        "",
        "```text",
        "M/2 ≡ 0 (mod 37) and M/2 ≡ 0 (mod 71).",
        "```",
        "",
        "当前两个因子残差分别为 `19` 与 `16`，所以 exact collision 被排除。"
        "最近余量 `55` 是这两个非零残差的 CRT 合成结果。",
        "",
        "## 4. 证明边界",
        "",
        "- 已闭合：当前 z=61 formal unit 的 half flip exact collision 被因子非零排除，且 CRT 合成恢复 offset `-55`。",
        "- 未闭合：全局 CRT 合成分离下界，或 Factor-PDEC 排斥。",
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
                "halfmod_factor_separation_closed_for_formal_unit": result[
                    "halfmod_factor_separation_closed_for_formal_unit"
                ],
                "combined_signed_residue": result["combined_signed_residue"],
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
