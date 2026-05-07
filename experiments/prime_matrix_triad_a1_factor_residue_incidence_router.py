#!/usr/bin/env python3
"""审计 FactorResidueIncidenceBridge 是否能闭合 ExactFactorSupport。

用法示例：
  python3 experiments/prime_matrix_triad_a1_factor_residue_incidence_router.py
  python3 experiments/prime_matrix_triad_a1_factor_residue_incidence_router.py --internal-power 7

输出：
  docs/monograph/prime-matrix-triad-a1-factor-residue-incidence-router.json
  docs/monograph/prime-matrix-triad-a1-factor-residue-incidence-router.md
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
DEFAULT_FACTOR_SUPPORT = DOCS / "prime-matrix-triad-a1-exact-factor-support-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-factor-residue-incidence-router.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-factor-residue-incidence-router.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_float(value: float) -> str:
    """格式化浮点数。"""
    return f"{value:.6g}"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def model_row(k: int, saving_exponent: float, internal_power: float) -> dict[str, Any]:
    """生成单 factor pair、多内部 residue 的阻断模型。"""
    y = 10**k
    log_y = math.log(y)
    required_share = log_y ** (-2.0 * saving_exponent)
    internal_atoms = math.ceil(log_y**internal_power)
    max_internal_atom_share = 1.0 / internal_atoms
    return {
        "k": k,
        "y": y,
        "log_y": log_y,
        "saving_exponent_A": saving_exponent,
        "internal_power_B": internal_power,
        "moving_factor_pair_count": 1,
        "internal_residue_phase_atoms": internal_atoms,
        "max_internal_atom_share": max_internal_atom_share,
        "k4_flat_enough": max_internal_atom_share <= required_share,
        "factor_pair_share": 1.0,
        "factor_support_fails": True,
        "incidence_multiplicity": internal_atoms,
    }


def build_gate_rows() -> list[dict[str, Any]]:
    """列出 incidence bridge 的失败点。"""
    return [
        {
            "gate": "BoundedIncidenceMultiplicity",
            "available": "not present",
            "needed": "one moving (u,v) block hits only polylog-small residue/phase atoms",
            "gap": "actual Kloosterman expansion has many h,ell,x,z atoms inside one (u,v) block",
            "route": "cannot be assumed; must be proved as arithmetic incidence, and naive form is false",
            "closed": False,
        },
        {
            "gate": "K4ConcentrationReturn",
            "available": "K4 returns if a residue/phase atom is large",
            "needed": "small factor support creates a large residue/phase atom",
            "gap": "a single factor pair can distribute its mass over many internal atoms and stay K4-flat",
            "route": "requires block-level capacity, which is NC-BLK/DI-BFI again",
            "closed": False,
        },
        {
            "gate": "K6TailLabelReturn",
            "available": "K6 returns if dyadic/tail-label splitting is excessive",
            "needed": "small factor support creates excessive splitting",
            "gap": "one factor pair inside one dyadic block is not excessive splitting",
            "route": "K6 does not see missing internal support",
            "closed": False,
        },
        {
            "gate": "CanonicalSupportFallback",
            "available": "still logically possible",
            "needed": "direct support theorem for exact RIW/Buchstab factors",
            "gap": "not yet proved or cited",
            "route": "CanonicalRIWFactorSupportLowerBound",
            "closed": False,
        },
    ]


def run(
    factor_support_path: Path,
    min_k: int,
    max_k: int,
    saving_exponent: float,
    internal_power: float,
) -> dict[str, Any]:
    """运行 factor-residue incidence 审计。"""
    factor_support = load_json(factor_support_path)
    rows = [model_row(k, saving_exponent, internal_power) for k in range(min_k, max_k + 1)]
    return {
        "certificate_type": "triad_a1_factor_residue_incidence_router",
        "status": "factor_residue_incidence_bridge_blocked_by_internal_atom_fiber",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "exact_factor_support_json": file_sha256(factor_support_path),
        },
        "parameters": {
            "min_k": min_k,
            "max_k": max_k,
            "saving_exponent_A": saving_exponent,
            "internal_power_B": internal_power,
            "scale": "y=10^k",
        },
        "factor_support_input_status": factor_support["status"],
        "gate_rows": build_gate_rows(),
        "rows": rows,
        "all_rows_k4_flat_inside_one_factor_pair": all(row["k4_flat_enough"] for row in rows),
        "factor_residue_incidence_bridge_closed": False,
        "naive_incidence_bridge_valid": False,
        "internal_fiber_obstruction_law": (
            "A moving factor-pair b=(u,v) is not a single K4 atom. It contains a growing internal fiber "
            "of h, ell, completion and Kloosterman variables. Mass can be flat on that internal fiber "
            "while remaining completely concentrated on one moving factor pair. Therefore small factor "
            "support does not force K4 coefficient concentration or K6 tail-label concentration."
        ),
        "next_internal_target": "CanonicalRIWFactorSupportLowerBound",
        "terminal_gap_after_router": (
            "CanonicalRIWFactorSupportLowerBoundOrExternalDIBFIOriginalDispersion"
        ),
        "review_conclusion": (
            "FactorResidueIncidenceBridge 的朴素形式被内部 fiber 阻断："
            "一个 moving `(u,v)` 块内可含许多 residue/phase 原子，质量在内部原子上平坦，"
            "但在 factor-pair 层仍完全集中。因此 clean K4/K6 不能通过 incidence 桥推出"
            " ExactFactorSupport。内部路线只剩直接证明 CanonicalRIWFactorSupportLowerBound，"
            "否则走外部 DI/BFI。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 FactorResidueIncidence 路由审计",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 内部 fiber 阻断律",
        "",
        result["internal_fiber_obstruction_law"],
        "",
        "```text",
        "one moving factor pair b=(u,v)",
        "  contains many internal atoms (h, ell, x, z, completion labels);",
        "mass can be flat on those internal K4 atoms",
        "  while remaining concentrated on b;",
        "therefore K4/K6 do not imply ExactFactorSupport through naive incidence.",
        "```",
        "",
        "## 2. 汇总",
        "",
        f"- `factor_support_input_status={result['factor_support_input_status']}`。",
        f"- `all_rows_k4_flat_inside_one_factor_pair={result['all_rows_k4_flat_inside_one_factor_pair']}`。",
        f"- `naive_incidence_bridge_valid={result['naive_incidence_bridge_valid']}`。",
        f"- `factor_residue_incidence_bridge_closed={result['factor_residue_incidence_bridge_closed']}`。",
        f"- `next_internal_target={result['next_internal_target']}`。",
        f"- `terminal_gap_after_router={result['terminal_gap_after_router']}`。",
        "",
        "## 3. 门控表",
        "",
        "| gate | available | needed | gap | route | closed |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for row in result["gate_rows"]:
        lines.append(
            "| `{gate}` | {available} | {needed} | {gap} | {route} | `{closed}` |".format(
                gate=table_cell(row["gate"]),
                available=table_cell(row["available"]),
                needed=table_cell(row["needed"]),
                gap=table_cell(row["gap"]),
                route=table_cell(row["route"]),
                closed=row["closed"],
            )
        )

    lines.extend(
        [
            "",
            "## 4. 阻断模型表",
            "",
            "| k | log y | factor pairs | internal atoms | max internal share | K4 flat | factor share | factor support fails |",
            "| ---: | ---: | ---: | ---: | ---: | --- | ---: | --- |",
        ]
    )
    for row in result["rows"]:
        lines.append(
            "| {k} | {logy} | {pairs} | {atoms} | {share} | `{flat}` | {fshare} | `{fails}` |".format(
                k=row["k"],
                logy=fmt_float(row["log_y"]),
                pairs=row["moving_factor_pair_count"],
                atoms=row["internal_residue_phase_atoms"],
                share=fmt_float(row["max_internal_atom_share"]),
                flat=row["k4_flat_enough"],
                fshare=fmt_float(row["factor_pair_share"]),
                fails=row["factor_support_fails"],
            )
        )

    lines.extend(
        [
            "",
            "## 5. 结论",
            "",
            "当前可删去一个伪出口：",
            "",
            "```text",
            "FactorResidueIncidenceBridge, in the naive bounded-multiplicity form, is blocked.",
            "```",
            "",
            "继续无黑箱路线只剩：",
            "",
            "```text",
            "CanonicalRIWFactorSupportLowerBound:",
            "  prove exact Rosser/Iwaniec-Buchstab factors have broad balanced support.",
            "```",
            "",
            "外部路线仍是 `DI/BFI original dispersion`。",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--factor-support-json", type=Path, default=DEFAULT_FACTOR_SUPPORT)
    parser.add_argument("--min-k", type=int, default=3)
    parser.add_argument("--max-k", type=int, default=9)
    parser.add_argument("--saving-exponent", type=float, default=2.0)
    parser.add_argument("--internal-power", type=float, default=7.0)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        args.factor_support_json,
        args.min_k,
        args.max_k,
        args.saving_exponent,
        args.internal_power,
    )
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(
        json.dumps(
            {
                "status": result["status"],
                "next_internal_target": result["next_internal_target"],
                "terminal_gap_after_router": result["terminal_gap_after_router"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
