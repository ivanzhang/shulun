#!/usr/bin/env python3
"""审计 z=61 根投影门的 CRT 符号支撑。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_signed_projection_support_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-signed-projection-support-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-signed-projection-support-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-signed-projection-support-router.md
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
SOURCE_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-root-projection-gate-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-signed-projection-support-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-signed-projection-support-router.md"

NEXT_TARGET = "SignedRootProjectionSupportGlobalBoundOrSignedProjectionPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-root-projection-gate-router.json",
]


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def fmt_fiber(fiber: list[dict[str, Any]]) -> str:
    """把符号纤维压成短字符串。"""
    if not fiber:
        return "[]"
    return "[" + ", ".join(f"{item['sign_word']}:{item['root_residue']}" for item in fiber) + "]"


def file_sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖哈希。"""
    result = {
        "experiments/prime_matrix_square_phase_lowalpha_z61_signed_projection_support_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def prime_power_factors(n: int) -> list[int]:
    """返回 n 的素数幂因子列表。"""
    factors = []
    d = 2
    value = n
    while d * d <= value:
        if value % d == 0:
            power = 1
            while value % d == 0:
                power *= d
                value //= d
            factors.append(power)
        d += 1 if d == 2 else 2
    if value > 1:
        factors.append(value)
    return factors


def roots_mod(modulus: int, delta: int) -> list[int]:
    """枚举局部平方根 `x^2+delta=0 mod modulus`。"""
    return [x for x in range(modulus) if (x * x + delta) % modulus == 0]


def crt_from_local(local_residues: list[int], local_moduli: list[int], global_modulus: int) -> int:
    """由互素局部余数重建 CRT 根。"""
    total = 0
    for residue, modulus in zip(local_residues, local_moduli):
        block = global_modulus // modulus
        total += residue * block * pow(block, -1, modulus)
    return total % global_modulus


def sign_word(signs: tuple[int, ...]) -> str:
    """把 ±1 符号向量写成短字。"""
    return "".join("+" if sign > 0 else "-" for sign in signs)


def signed_projection_rows(source: dict[str, Any]) -> list[dict[str, Any]]:
    """把一级 CRT 根支撑改写为五维符号投影支撑。"""
    rows = []
    for group in source["projection_gate_rows"]:
        modulus = group["modulus"]
        delta = group["delta"]
        q2 = group["q2"]
        q4 = group["q4"]
        selected = group["selected_residue"]
        local_moduli = prime_power_factors(modulus)
        local_root_pairs = [roots_mod(local_modulus, delta) for local_modulus in local_moduli]
        pairwise_two_roots = all(len(pair) == 2 for pair in local_root_pairs)

        local_rows = []
        positive_roots = []
        for local_modulus, pair in zip(local_moduli, local_root_pairs):
            positive_root = pair[0]
            negative_root = (-positive_root) % local_modulus
            positive_roots.append(positive_root)
            basis = (modulus // local_modulus) * pow(modulus // local_modulus, -1, local_modulus)
            local_rows.append(
                {
                    "local_modulus": local_modulus,
                    "local_roots": pair,
                    "positive_root": positive_root,
                    "negative_root": negative_root,
                    "basis_mod_M": basis % modulus,
                    "coefficient_mod_37": (positive_root * basis) % q4,
                    "coefficient_mod_71": (positive_root * basis) % q2,
                    "coefficient_mod_2627": (positive_root * basis) % (q2 * q4),
                    "roots_are_pm_pair": sorted(pair) == sorted([positive_root, negative_root]),
                }
            )

        sign_rows = []
        for signs in product([1, -1], repeat=len(local_moduli)):
            local_residues = [
                positive_root if sign > 0 else (-positive_root) % local_modulus
                for sign, positive_root, local_modulus in zip(signs, positive_roots, local_moduli)
            ]
            root = crt_from_local(local_residues, local_moduli, modulus)
            sign_rows.append(
                {
                    "sign_word": sign_word(signs),
                    "signs": list(signs),
                    "local_residues": local_residues,
                    "root_residue": root,
                    "root_mod_37": root % q4,
                    "root_mod_71": root % q2,
                    "root_mod_2627": root % (q2 * q4),
                    "selected": root == selected,
                }
            )
        sign_rows.sort(key=lambda item: item["root_residue"])

        source_roots = sorted(row["root_residue"] for row in group["candidate_rows"])
        signed_roots = sorted(row["root_residue"] for row in sign_rows)

        gate_fibers = []
        for gate in group["projection_gate_specs"]:
            ell = gate["ell"]
            key = f"root_mod_{ell}"
            target_fibers = []
            for target in gate["root_projection_solutions"]:
                fiber = [
                    {
                        "sign_word": row["sign_word"],
                        "root_residue": row["root_residue"],
                    }
                    for row in sign_rows
                    if row[key] == target
                ]
                target_fibers.append(
                    {
                        "target_residue": target,
                        "fiber_size": len(fiber),
                        "fiber": fiber,
                    }
                )
            gate_fibers.append(
                {
                    "gate_name": gate["name"],
                    "ell": ell,
                    "target_residues": gate["root_projection_solutions"],
                    "target_fibers": target_fibers,
                    "total_target_fiber_size": sum(item["fiber_size"] for item in target_fibers),
                    "selected_singleton": (
                        sum(item["fiber_size"] for item in target_fibers) == 1
                        and any(
                            item["fiber"] and item["fiber"][0]["root_residue"] == selected
                            for item in target_fibers
                        )
                    ),
                }
            )

        combined_fibers = []
        for target_class in group["combined_projection_classes"]:
            fiber = [
                {
                    "sign_word": row["sign_word"],
                    "root_residue": row["root_residue"],
                }
                for row in sign_rows
                if row["root_mod_2627"] == target_class
            ]
            combined_fibers.append(
                {
                    "target_class": target_class,
                    "fiber_size": len(fiber),
                    "fiber": fiber,
                }
            )
        selected_sign_rows = [row for row in sign_rows if row["selected"]]
        rows.append(
            {
                "modulus": modulus,
                "delta": delta,
                "q2": q2,
                "q4": q4,
                "selected_residue": selected,
                "local_moduli": local_moduli,
                "local_rows": local_rows,
                "pairwise_two_roots": pairwise_two_roots,
                "all_local_roots_pm_pairs": all(row["roots_are_pm_pair"] for row in local_rows),
                "sign_vector_count": len(sign_rows),
                "source_root_count": len(source_roots),
                "signed_support_matches_source_roots": signed_roots == source_roots,
                "selected_sign_word": selected_sign_rows[0]["sign_word"] if selected_sign_rows else None,
                "selected_sign_rows": selected_sign_rows,
                "gate_fibers": gate_fibers,
                "combined_fibers": combined_fibers,
                "combined_total_target_fiber_size": sum(item["fiber_size"] for item in combined_fibers),
                "combined_selected_singleton": (
                    sum(item["fiber_size"] for item in combined_fibers) == 1
                    and any(
                        item["fiber"] and item["fiber"][0]["root_residue"] == selected
                        for item in combined_fibers
                    )
                ),
                "signed_projection_support_closed_for_group": (
                    pairwise_two_roots
                    and all(row["roots_are_pm_pair"] for row in local_rows)
                    and signed_roots == source_roots
                    and all(gate["selected_singleton"] for gate in gate_fibers)
                    and sum(item["fiber_size"] for item in combined_fibers) == 1
                    and any(
                        item["fiber"] and item["fiber"][0]["root_residue"] == selected
                        for item in combined_fibers
                    )
                ),
            }
        )
    return rows


def audit() -> dict[str, Any]:
    """执行符号投影支撑审计。"""
    source = json.loads(SOURCE_JSON.read_text(encoding="utf-8"))
    rows = signed_projection_rows(source)
    all_rows_closed = bool(rows) and all(
        row["signed_projection_support_closed_for_group"] for row in rows
    )
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_signed_projection_support_router",
        "status": "z61_root_projection_gate_reduced_to_signed_crt_support_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "source_certificate": source["certificate_type"],
        "target_bucket": source["target_bucket"],
        "target_omega": source["target_omega"],
        "target_shell": source["target_shell"],
        "signed_projection_support_group_count": len(rows),
        "all_signed_projection_supports_closed": all_rows_closed,
        "signed_projection_rows": rows,
        "signed_projection_support_global_bound_proved": False,
        "signed_projection_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "根投影门可继续展开为 CRT 局部根的符号支撑问题："
            "`M=57684=4*3*11*19*23`，每个局部模都有两个相反平方根，"
            "所以 32 个一级根正好是五维符号向量的 CRT 像。"
            "在该符号支撑上，`q4=37`、`q2=71` 以及合并模 `2627` 的目标投影纤维"
            "都只有同一个符号字 `--++-`，对应 `r=26951`；其余目标类为空。"
            "因此最新硬点变成全局符号投影支撑容量界，或登记 SignedProjection-PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 signed projection support",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"signed_projection_support_group_count={result['signed_projection_support_group_count']}",
        f"all_signed_projection_supports_closed={fmt_bool(result['all_signed_projection_supports_closed'])}",
        f"signed_projection_support_global_bound_proved={fmt_bool(result['signed_projection_support_global_bound_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 符号支撑摘要",
        "",
        "| M | local moduli | sign vectors | source roots | selected sign | selected root | closed |",
        "| ---: | --- | ---: | ---: | --- | ---: | --- |",
    ]
    for row in result["signed_projection_rows"]:
        lines.append(
            f"| {row['modulus']} | `{row['local_moduli']}` | {row['sign_vector_count']} | "
            f"{row['source_root_count']} | `{row['selected_sign_word']}` | "
            f"{row['selected_residue']} | {fmt_bool(row['signed_projection_support_closed_for_group'])} |"
        )
    lines.extend(
        [
            "",
            "## 2. 局部 CRT 系数",
            "",
            "| local modulus | roots | + root | basis mod M | coeff mod 37 | coeff mod 71 | coeff mod 2627 |",
            "| ---: | --- | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in result["signed_projection_rows"]:
        for local in row["local_rows"]:
            lines.append(
                f"| {local['local_modulus']} | `{local['local_roots']}` | "
                f"{local['positive_root']} | {local['basis_mod_M']} | "
                f"{local['coefficient_mod_37']} | {local['coefficient_mod_71']} | "
                f"{local['coefficient_mod_2627']} |"
            )
    lines.extend(
        [
            "",
            "## 3. 单投影目标纤维",
            "",
            "| gate | target | fiber size | fiber |",
            "| --- | ---: | ---: | --- |",
        ]
    )
    for row in result["signed_projection_rows"]:
        for gate in row["gate_fibers"]:
            for fiber in gate["target_fibers"]:
                lines.append(
                    f"| `{gate['gate_name']}` | {fiber['target_residue']} | "
                    f"{fiber['fiber_size']} | `{fmt_fiber(fiber['fiber'])}` |"
                )
    lines.extend(
        [
            "",
            "## 4. 合并投影目标纤维",
            "",
            "| class mod 2627 | fiber size | fiber |",
            "| ---: | ---: | --- |",
        ]
    )
    for row in result["signed_projection_rows"]:
        for fiber in row["combined_fibers"]:
            lines.append(
                f"| {fiber['target_class']} | {fiber['fiber_size']} | `{fmt_fiber(fiber['fiber'])}` |"
            )
    lines.extend(
        [
            "",
            "## 5. 自足小引理",
            "",
            "若 `M=prod m_i` 且 `x^2+delta=0 mod m_i` 的两个局部根为 `±a_i`，则所有一级根可写成",
            "",
            "```text",
            "r(sigma)=sum_i sigma_i*a_i*B_i (mod M),  sigma_i in {+1,-1},",
            "B_i=(M/m_i)*(M/m_i)^{-1} mod m_i.",
            "```",
            "",
            "因此任意小模投影 `r mod ell` 都是同一符号向量的线性投影。"
            "本证书精确枚举该五维符号支撑，证明目标投影纤维为单点或空纤维。",
            "",
            "## 6. 证明边界",
            "",
            "- 已闭合：当前 z=61 formal unit 的一级根支撑等于五维 CRT 符号像，且目标投影纤维唯一命中 `--++- / r=26951`。",
            "- 未闭合：把这种符号投影支撑单点性提升为全局容量界，或排斥 SignedProjection-PDEC。",
            f"- 下一目标：`{result['next_direct_attack_target']}`。",
            "",
            "## 7. 依赖哈希",
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
                "all_signed_projection_supports_closed": result[
                    "all_signed_projection_supports_closed"
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
