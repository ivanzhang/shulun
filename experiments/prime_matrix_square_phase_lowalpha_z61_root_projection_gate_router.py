#!/usr/bin/env python3
"""审计 z=61 仿射根选择器的小模投影门。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_root_projection_gate_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-root-projection-gate-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-root-projection-gate-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-root-projection-gate-router.md
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
SOURCE_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-affine-lift-selector-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-root-projection-gate-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-root-projection-gate-router.md"

NEXT_TARGET = "RootProjectionGateGlobalBoundOrProjectionPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-affine-lift-selector-router.json",
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
        "experiments/prime_matrix_square_phase_lowalpha_z61_root_projection_gate_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def crt_pair(a: int, mod_a: int, b: int, mod_b: int) -> int:
    """求两个互素模的 CRT 最小非负代表。"""
    return (a + mod_a * (((b - a) * pow(mod_a, -1, mod_b)) % mod_b)) % (mod_a * mod_b)


def projection_solutions(modulus: int, delta: int, span_h: int, ell: int, offset: int) -> list[int]:
    """求根投影方程 `(r+hM)^2+delta+offset*M=0 mod ell` 的解。"""
    return [
        residue
        for residue in range(ell)
        if ((residue + span_h * modulus) ** 2 + delta + offset * modulus) % ell == 0
    ]


def p_projection_solutions(modulus: int, delta: int, ell: int, offset: int) -> list[int]:
    """求同一条件写成 `p^2+delta+offset*M=0 mod ell` 时的 p 相位解。"""
    return [
        residue
        for residue in range(ell)
        if (residue * residue + delta + offset * modulus) % ell == 0
    ]


def projection_gate_rows(source: dict[str, Any]) -> list[dict[str, Any]]:
    """把仿射门压成根 r 的小模投影门。"""
    rows = []
    for group in source["affine_selector_rows"]:
        modulus = group["modulus"]
        delta = group["delta"]
        q2 = group["q2"]
        q4 = group["q4"]
        selected = group["selected_residue"]
        span_values = group["span_values"]
        single_span_locked = len(span_values) == 1
        span_h = span_values[0] if single_span_locked else None

        gate_specs = [
            {
                "name": "q4_plain_root_projection",
                "ell": q4,
                "offset_multiple_of_M": 0,
                "affine_residue_key": "q4_affine_residue",
                "affine_closed_key": "q4_affine_gate_closed",
                "meaning": "K≡0 mod q4, equivalently (r+hM)^2+delta≡0 mod q4",
            },
            {
                "name": "q2_shifted_root_projection",
                "ell": q2,
                "offset_multiple_of_M": 2 * q4,
                "affine_residue_key": "q2_shifted_affine_residue",
                "affine_closed_key": "q2_shifted_affine_gate_closed",
                "meaning": "K+2q4≡0 mod q2, equivalently (r+hM)^2+delta+2Mq4≡0 mod q2",
            },
        ]

        candidate_rows = []
        for candidate in group["candidate_rows"]:
            root = candidate["root_residue"]
            p_value = candidate["p_candidate"]
            enriched = {
                "root_residue": root,
                "p_candidate": p_value,
                "span_h": candidate["span_h"],
                "local_k0": candidate["local_k0"],
                "affine_k": candidate["affine_k"],
                "p_is_prime": candidate["p_is_prime"],
                "full_source_candidate": candidate["full_source_candidate"],
            }
            for spec in gate_specs:
                ell = spec["ell"]
                offset = spec["offset_multiple_of_M"]
                affine_residue = candidate[spec["affine_residue_key"]]
                projection_residue = (
                    (root + candidate["span_h"] * modulus) ** 2 + delta + offset * modulus
                ) % ell
                projection_closed = projection_residue == 0
                # 因为 p^2+delta+offset*M = M*(K+offset)，M 在 ell 下可逆。
                scaled_affine_residue = (modulus * affine_residue) % ell
                enriched[f"{spec['name']}_root_mod"] = root % ell
                enriched[f"{spec['name']}_p_mod"] = p_value % ell
                enriched[f"{spec['name']}_projection_residue"] = projection_residue
                enriched[f"{spec['name']}_scaled_affine_residue"] = scaled_affine_residue
                enriched[f"{spec['name']}_closed"] = projection_closed
                enriched[f"{spec['name']}_matches_affine"] = (
                    projection_closed == candidate[spec["affine_closed_key"]]
                    and projection_residue == scaled_affine_residue
                )
            candidate_rows.append(enriched)

        projection_gate_specs = []
        for spec in gate_specs:
            ell = spec["ell"]
            offset = spec["offset_multiple_of_M"]
            root_solutions = projection_solutions(modulus, delta, span_h, ell, offset)
            p_solutions = p_projection_solutions(modulus, delta, ell, offset)
            pass_roots = [
                row["root_residue"]
                for row in candidate_rows
                if row[f"{spec['name']}_root_mod"] in root_solutions
            ]
            realized_solution_fibers = {
                str(solution): [
                    row["root_residue"]
                    for row in candidate_rows
                    if row[f"{spec['name']}_root_mod"] == solution
                ]
                for solution in root_solutions
            }
            projection_gate_specs.append(
                {
                    **spec,
                    "root_projection_solutions": root_solutions,
                    "p_projection_solutions": p_solutions,
                    "pass_count": len(pass_roots),
                    "pass_residues": pass_roots,
                    "selected_passes_uniquely": len(pass_roots) == 1 and pass_roots[0] == selected,
                    "realized_solution_fibers": realized_solution_fibers,
                    "unrealized_projection_solutions": [
                        solution
                        for solution in root_solutions
                        if not realized_solution_fibers[str(solution)]
                    ],
                }
            )

        q4_solutions = projection_gate_specs[0]["root_projection_solutions"]
        q2_solutions = projection_gate_specs[1]["root_projection_solutions"]
        combined_classes = [
            crt_pair(q4_solution, q4, q2_solution, q2)
            for q4_solution, q2_solution in product(q4_solutions, q2_solutions)
        ]
        combined_fibers = {
            str(cls): [
                row["root_residue"]
                for row in candidate_rows
                if row["root_residue"] % (q2 * q4) == cls
            ]
            for cls in combined_classes
        }
        combined_pass = [
            root
            for fiber in combined_fibers.values()
            for root in fiber
        ]
        rows.append(
            {
                "modulus": modulus,
                "delta": delta,
                "q2": q2,
                "q4": q4,
                "selected_residue": selected,
                "candidate_count": len(candidate_rows),
                "span_values": span_values,
                "single_span_locked": single_span_locked,
                "span_h": span_h,
                "projection_gate_specs": projection_gate_specs,
                "combined_modulus_q2q4": q2 * q4,
                "combined_projection_classes": combined_classes,
                "combined_projection_fibers": combined_fibers,
                "combined_pass_count": len(combined_pass),
                "combined_pass_residues": combined_pass,
                "combined_projection_gate_unique": len(combined_pass) == 1 and combined_pass[0] == selected,
                "all_projection_formulae_match_affine": all(
                    all(row[f"{spec['name']}_matches_affine"] for spec in gate_specs)
                    for row in candidate_rows
                ),
                "q4_projection_gate_unique": projection_gate_specs[0]["selected_passes_uniquely"],
                "q2_projection_gate_unique": projection_gate_specs[1]["selected_passes_uniquely"],
                "candidate_rows": candidate_rows,
                "root_projection_gate_closed_for_group": (
                    single_span_locked
                    and all(
                        all(row[f"{spec['name']}_matches_affine"] for spec in gate_specs)
                        for row in candidate_rows
                    )
                    and projection_gate_specs[0]["selected_passes_uniquely"]
                    and projection_gate_specs[1]["selected_passes_uniquely"]
                    and len(combined_pass) == 1
                    and combined_pass[0] == selected
                ),
            }
        )
    return rows


def audit() -> dict[str, Any]:
    """执行根投影门审计。"""
    source = json.loads(SOURCE_JSON.read_text(encoding="utf-8"))
    rows = projection_gate_rows(source)
    all_rows_closed = bool(rows) and all(row["root_projection_gate_closed_for_group"] for row in rows)
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_root_projection_gate_router",
        "status": "z61_affine_root_selector_reduced_to_root_projection_gate_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "source_certificate": source["certificate_type"],
        "target_bucket": source["target_bucket"],
        "target_omega": source["target_omega"],
        "target_shell": source["target_shell"],
        "root_projection_gate_group_count": len(rows),
        "all_root_projection_gates_closed": all_rows_closed,
        "projection_gate_rows": rows,
        "root_projection_gate_global_bound_proved": False,
        "projection_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "仿射选择器可继续消去 `K`：因 `p=hM+r` 且 `p^2+delta=M*K`，"
            "`K+offset≡0 (mod ell)` 等价于 "
            "`(r+hM)^2+delta+offset*M≡0 (mod ell)`。"
            "在当前 z=61 样本中，`q4=37` 投影根为 `r≡15,16`，"
            "`q2=71` 移位投影根为 `r≡42,50`；但 32 个一级 CRT 根支撑上，"
            "两门各自以及合并门都只命中 `r=26951`。"
            "因此最新硬点进一步收窄为根支撑投影容量界，或登记 Projection-PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 root projection gate",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"root_projection_gate_group_count={result['root_projection_gate_group_count']}",
        f"all_root_projection_gates_closed={fmt_bool(result['all_root_projection_gates_closed'])}",
        f"root_projection_gate_global_bound_proved={fmt_bool(result['root_projection_gate_global_bound_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 投影门摘要",
        "",
        "| M | h | roots | q4 unique | q2 unique | combined classes | combined pass | selected | closed |",
        "| ---: | ---: | ---: | --- | --- | --- | --- | ---: | --- |",
    ]
    for row in result["projection_gate_rows"]:
        lines.append(
            f"| {row['modulus']} | {row['span_h']} | {row['candidate_count']} | "
            f"{fmt_bool(row['q4_projection_gate_unique'])} | "
            f"{fmt_bool(row['q2_projection_gate_unique'])} | "
            f"`{row['combined_projection_classes']}` | "
            f"`{row['combined_pass_residues']}` | {row['selected_residue']} | "
            f"{fmt_bool(row['root_projection_gate_closed_for_group'])} |"
        )
    lines.extend(
        [
            "",
            "## 2. 单投影门",
            "",
            "| gate | ell | offset/M | root solutions | p solutions | pass roots | unrealized solutions | unique |",
            "| --- | ---: | ---: | --- | --- | --- | --- | --- |",
        ]
    )
    for row in result["projection_gate_rows"]:
        for gate in row["projection_gate_specs"]:
            lines.append(
                f"| `{gate['name']}` | {gate['ell']} | {gate['offset_multiple_of_M']} | "
                f"`{gate['root_projection_solutions']}` | `{gate['p_projection_solutions']}` | "
                f"`{gate['pass_residues']}` | `{gate['unrealized_projection_solutions']}` | "
                f"{fmt_bool(gate['selected_passes_uniquely'])} |"
            )
    lines.extend(
        [
            "",
            "## 3. 合并投影纤维",
            "",
            "| class mod q2q4 | roots in CRT support |",
            "| ---: | --- |",
        ]
    )
    for row in result["projection_gate_rows"]:
        for cls, fiber in row["combined_projection_fibers"].items():
            lines.append(f"| {cls} | `{fiber}` |")
    lines.extend(
        [
            "",
            "## 4. 候选根投影残差",
            "",
            "| root | p | r mod 37 | r mod 71 | q4 proj | q2 proj | prime p | full source |",
            "| ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |",
        ]
    )
    for row in result["projection_gate_rows"]:
        for candidate in row["candidate_rows"]:
            if candidate["p_is_prime"] or candidate["full_source_candidate"]:
                lines.append(
                    f"| {candidate['root_residue']} | {candidate['p_candidate']} | "
                    f"{candidate['q4_plain_root_projection_root_mod']} | "
                    f"{candidate['q2_shifted_root_projection_root_mod']} | "
                    f"{candidate['q4_plain_root_projection_projection_residue']} | "
                    f"{candidate['q2_shifted_root_projection_projection_residue']} | "
                    f"{fmt_bool(candidate['p_is_prime'])} | "
                    f"{fmt_bool(candidate['full_source_candidate'])} |"
                )
    lines.extend(
        [
            "",
            "## 5. 自足小引理",
            "",
            "若 `p=hM+r` 且 `p^2+delta=M*K`，并且 `gcd(M,ell)=1`，则",
            "",
            "```text",
            "K+offset ≡ 0 (mod ell)",
            "⇔ M*(K+offset) ≡ 0 (mod ell)",
            "⇔ (r+hM)^2+delta+offset*M ≡ 0 (mod ell).",
            "```",
            "",
            "因此仿射选择器不是新的大变量条件，而是一级 CRT 根集合在小模 `37`、`71` 上的投影筛选。",
            "",
            "## 6. 证明边界",
            "",
            "- 已闭合：样本仿射门等价于根相位投影门，且两个单投影门与合并投影门均唯一选中同一根。",
            "- 新发现：理论投影根共有四个合并类，但一级 CRT 根支撑只实现其中一个类；其余三个类是支撑空纤维。",
            "- 未闭合：全局根支撑投影容量界，或 Projection-PDEC 排斥。",
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
                "all_root_projection_gates_closed": result["all_root_projection_gates_closed"],
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
