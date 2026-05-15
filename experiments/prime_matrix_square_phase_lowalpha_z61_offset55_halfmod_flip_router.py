#!/usr/bin/env python3
"""审计 z=61 最近 offset-55 碰撞的 half-modulus flip 来源。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_offset55_halfmod_flip_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-offset55-halfmod-flip-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-offset55-halfmod-flip-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-offset55-halfmod-flip-router.md
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
NEAREST_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-nearest-margin-collision-router.json"
BRANCH_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-branch-decision-ledger-router.json"
SIGNED_SUM_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-signed-sum-residue-gate-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-offset55-halfmod-flip-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-offset55-halfmod-flip-router.md"

NEXT_TARGET = "HalfModulusFlipSeparationGlobalBoundOrHalfFlipPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-nearest-margin-collision-router.json",
    "prime-matrix-square-phase-lowalpha-z61-branch-decision-ledger-router.json",
    "prime-matrix-square-phase-lowalpha-z61-signed-sum-residue-gate-router.json",
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
        "experiments/prime_matrix_square_phase_lowalpha_z61_offset55_halfmod_flip_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def sign_value(sign_word: str, coefficients: list[int]) -> int:
    """计算符号和。"""
    return sum((1 if sign == "+" else -1) * coeff for sign, coeff in zip(sign_word, coefficients))


def circular_distance(value: int, modulus: int) -> int:
    """计算 residue 到 0 的模圆距离。"""
    residue = value % modulus
    return min(residue, (-residue) % modulus)


def audit() -> dict[str, Any]:
    """执行 half-modulus flip 审计。"""
    nearest = json.loads(NEAREST_JSON.read_text(encoding="utf-8"))
    branch = json.loads(BRANCH_JSON.read_text(encoding="utf-8"))
    signed_sum = json.loads(SIGNED_SUM_JSON.read_text(encoding="utf-8"))

    signed_group = signed_sum["signed_sum_rows"][0]
    modulus = signed_group["modulus"]
    target_modulus = signed_group["q2"] * signed_group["q4"]
    coefficients = branch["peel_coefficients"]
    selected_word = branch["selected_peel_sign_word"]
    selected_sum = sign_value(selected_word, coefficients)
    selected_sum_mod = selected_sum % target_modulus

    closest_members = nearest["closest_collision_groups"][0]["members"]
    reconstructed = []
    for atom in closest_members:
        step = atom["step"]
        prefix_before_step = selected_word[: step - 1]
        full_word = prefix_before_step + atom["branch_sign"] + atom["candidate_sign_word"]
        full_sum = sign_value(full_word, coefficients)
        reconstructed.append(
            {
                "step": step,
                "prefix_before_step": prefix_before_step,
                "branch_sign": atom["branch_sign"],
                "candidate_sign_word": atom["candidate_sign_word"],
                "full_peel_sign_word": full_word,
                "full_sum": full_sum,
                "full_sum_mod": full_sum % target_modulus,
                "atom_candidate_sum_mod": atom["candidate_sum_mod"],
                "atom_target": atom["nearest_target"],
                "atom_offset": atom["signed_offset_to_target"],
            }
        )
    full_alt_words = sorted({row["full_peel_sign_word"] for row in reconstructed})
    alternative_word = full_alt_words[0] if len(full_alt_words) == 1 else None
    alternative_sum = sign_value(alternative_word, coefficients) if alternative_word else None
    alternative_sum_mod = alternative_sum % target_modulus if alternative_sum is not None else None

    differing_positions = [
        index
        for index, (left, right) in enumerate(zip(selected_word, alternative_word or ""), start=1)
        if left != right
    ]
    flip_position = differing_positions[0] if len(differing_positions) == 1 else None
    flip_coefficient = coefficients[flip_position - 1] if flip_position else None
    flip_delta = alternative_sum - selected_sum if alternative_sum is not None else None
    expected_half_modulus = modulus // 2
    separation_mod = flip_delta % target_modulus if flip_delta is not None else None
    signed_separation = (
        separation_mod - target_modulus if separation_mod and separation_mod > target_modulus // 2 else separation_mod
    )

    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_offset55_halfmod_flip_router",
        "status": "z61_offset55_collision_reduced_to_half_modulus_flip_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "source_certificate": nearest["certificate_type"],
        "target_bucket": nearest["target_bucket"],
        "target_omega": nearest["target_omega"],
        "target_shell": nearest["target_shell"],
        "modulus": modulus,
        "target_modulus": target_modulus,
        "selected_peel_sign_word": selected_word,
        "selected_original_sign_word": branch["selected_original_sign_word"],
        "alternative_peel_sign_word": alternative_word,
        "peel_coefficients": coefficients,
        "selected_sum": selected_sum,
        "selected_sum_mod": selected_sum_mod,
        "alternative_sum": alternative_sum,
        "alternative_sum_mod": alternative_sum_mod,
        "reconstructed_nearest_atoms": reconstructed,
        "all_nearest_atoms_same_alternative_word": len(full_alt_words) == 1,
        "differing_positions": differing_positions,
        "single_flip_position": flip_position,
        "single_flip_coefficient": flip_coefficient,
        "flip_delta": flip_delta,
        "expected_half_modulus": expected_half_modulus,
        "flip_delta_equals_half_modulus": flip_delta == expected_half_modulus,
        "target_modulus_coprime_to_half_modulus": math.gcd(target_modulus, expected_half_modulus) == 1,
        "separation_mod_target": separation_mod,
        "signed_separation_mod_target": signed_separation,
        "separation_circular_margin": circular_distance(flip_delta, target_modulus)
        if flip_delta is not None
        else None,
        "offset55_halfmod_flip_closed_for_formal_unit": (
            len(full_alt_words) == 1
            and alternative_word == "+++--"
            and differing_positions == [3]
            and flip_delta == expected_half_modulus
            and signed_separation == -55
        ),
        "half_modulus_flip_separation_global_bound_proved": False,
        "half_flip_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "最近 offset-55 碰撞族可继续压缩：三条最近原子其实是同一完整替代路径 "
            "`+++--` 在不同剥离深度的投影。它与选中路径 `++---` 只差第三个符号，"
            "即翻转系数 `14421=M/4`；两条完整 signed-sum 的差为 `2*14421=M/2=28842`。"
            "模 `2627=37*71` 下 `M/2≡-55`，所以 offset-55 的来源是 2-adic half-modulus flip，"
            "不是独立随机碰撞。全局剩余变成 half-modulus flip 分离下界，或 HalfFlip-PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 offset-55 half-modulus flip",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"selected_peel_sign_word={result['selected_peel_sign_word']}",
        f"alternative_peel_sign_word={result['alternative_peel_sign_word']}",
        f"single_flip_position={result['single_flip_position']}",
        f"single_flip_coefficient={result['single_flip_coefficient']}",
        f"flip_delta={result['flip_delta']}",
        f"signed_separation_mod_target={result['signed_separation_mod_target']}",
        f"separation_circular_margin={result['separation_circular_margin']}",
        f"offset55_halfmod_flip_closed_for_formal_unit={fmt_bool(result['offset55_halfmod_flip_closed_for_formal_unit'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 两条完整路径",
        "",
        "| path | sign word | signed sum | mod 2627 |",
        "| --- | --- | ---: | ---: |",
        f"| selected | `{result['selected_peel_sign_word']}` | {result['selected_sum']} | {result['selected_sum_mod']} |",
        f"| nearest alternative | `{result['alternative_peel_sign_word']}` | {result['alternative_sum']} | {result['alternative_sum_mod']} |",
        "",
        "## 2. 最近原子重构",
        "",
        "| step | prefix | branch | suffix | full word | full sum mod 2627 | atom offset |",
        "| ---: | --- | --- | --- | --- | ---: | ---: |",
    ]
    for row in result["reconstructed_nearest_atoms"]:
        lines.append(
            f"| {row['step']} | `{row['prefix_before_step']}` | `{row['branch_sign']}` | "
            f"`{row['candidate_sign_word']}` | `{row['full_peel_sign_word']}` | "
            f"{row['full_sum_mod']} | {row['atom_offset']} |"
        )
    lines.extend(
        [
            "",
            "## 3. 结构恒等式",
            "",
            "最近替代路径与选中路径只差第三个符号，因此",
            "",
            "```text",
            "S(++ + --) - S(++ - --) = 2*14421 = 28842 = M/2.",
            "M/2 mod (37*71) = -55.",
            "```",
            "",
            "由于 `gcd(M/2,37*71)=1`，精确重合不发生；但最小环距离为 `55`，"
            "这就是当前 formal unit 的最近 Margin-PDEC 来源。",
            "",
            "## 4. 证明边界",
            "",
            "- 已闭合：当前 z=61 formal unit 的 offset-55 最近碰撞全部来自同一个 half-modulus flip。",
            "- 未闭合：全局 half-modulus flip 分离下界，或 HalfFlip-PDEC 排斥。",
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
                "offset55_halfmod_flip_closed_for_formal_unit": result[
                    "offset55_halfmod_flip_closed_for_formal_unit"
                ],
                "signed_separation_mod_target": result["signed_separation_mod_target"],
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
