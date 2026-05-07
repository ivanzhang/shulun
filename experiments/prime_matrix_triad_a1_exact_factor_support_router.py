#!/usr/bin/env python3
"""审计 ExactFactorSupportLowerBound 能否由 K4/K6 clean admission 自动推出。

用法示例：
  python3 experiments/prime_matrix_triad_a1_exact_factor_support_router.py
  python3 experiments/prime_matrix_triad_a1_exact_factor_support_router.py --support-power 7

输出：
  docs/monograph/prime-matrix-triad-a1-exact-factor-support-router.json
  docs/monograph/prime-matrix-triad-a1-exact-factor-support-router.md
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
DEFAULT_EXACT_WFD = DOCS / "prime-matrix-triad-a1-exact-wfd-source-entropy-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-exact-factor-support-router.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-exact-factor-support-router.md"


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


def model_row(
    k: int,
    saving_exponent: float,
    divisor_loss_power: float,
    support_power: float,
) -> dict[str, Any]:
    """生成 residue-flat 但 factor-concentrated 的阻断模型。

    模型含义：
    - K4 看到 residue atoms 上的平坦分布；
    - moving factor-pair 层只有一个块，故 ExactFactorSupport 失败；
    - 若没有 factor->residue incidence 上界，K4 不能排除这种模型。
    """
    y = 10**k
    log_y = math.log(y)
    required_factor_share = log_y ** (-2.0 * saving_exponent)
    residue_atoms = math.ceil(log_y**support_power)
    max_residue_share = 1.0 / residue_atoms
    concentrated_factor_share = 1.0
    support_threshold_power = saving_exponent + 2.0 * divisor_loss_power
    exact_support_needed = math.ceil(log_y**support_threshold_power)
    return {
        "k": k,
        "y": y,
        "log_y": log_y,
        "saving_exponent_A": saving_exponent,
        "divisor_loss_power_C": divisor_loss_power,
        "support_power_B": support_power,
        "residue_atoms_in_k4_model": residue_atoms,
        "max_residue_share": max_residue_share,
        "k4_flat_enough_for_A": max_residue_share <= required_factor_share,
        "moving_factor_pair_count": 1,
        "moving_factor_pair_share": concentrated_factor_share,
        "exact_factor_support_needed": exact_support_needed,
        "exact_factor_support_fails": concentrated_factor_share > required_factor_share,
        "incidence_multiplicity_needed_to_hide": residue_atoms,
    }


def build_gate_rows() -> list[dict[str, Any]]:
    """列出 ExactFactorSupport 的当前门控。"""
    return [
        {
            "gate": "K4ResidueFlatness",
            "available": "L2 flatness on fixed residue/phase atoms, support A_B >= R/C_flat",
            "needed": "many moving factor pairs (u,v) carry the exact WFD capacity",
            "gap": "a single moving factor pair may split into many residue atoms unless incidence is bounded",
            "route": "prove FactorResidueIncidenceBridge or use direct canonical factor support",
            "closed": False,
        },
        {
            "gate": "K6DyadicBookkeeping",
            "available": "dyadic/tail-label split count is polylog and over-splitting is routed",
            "needed": "each surviving dyadic block has broad internal u- and v-support",
            "gap": "polylog many blocks does not imply lower support inside a block",
            "route": "small internal support must be named as a failure route or proved impossible for exact weights",
            "closed": False,
        },
        {
            "gate": "CanonicalRIWFactorSupport",
            "available": "not recorded for the exact Rosser/Iwaniec-Buchstab factorization used by KZ-E",
            "needed": "sum |alpha_u| >= U/log^C and sum |delta_v| >= V/log^C",
            "gap": "well-factorable existence alone permits sparse formal factors",
            "route": "prove direct exact sieve-factor support lemma",
            "closed": False,
        },
        {
            "gate": "FactorResidueIncidenceBridge",
            "available": "not present in current ledger",
            "needed": "bounded multiplicity from one moving (u,v) block into K4 residue atoms",
            "gap": "without this bridge, residue flatness and factor support live on different sigma-algebras",
            "route": "prove concentration on few factor pairs triggers coefficient/tail-label PDEC/SAE failure",
            "closed": False,
        },
        {
            "gate": "SupportFailureReturn",
            "available": "clean branch routes coefficient concentration and tail-label concentration",
            "needed": "factor-support failure is shown to be one of those named failures",
            "gap": "the implication is not yet proved; it is exactly the incidence bridge",
            "route": "FactorResidueIncidenceBridge",
            "closed": False,
        },
    ]


def build_acceptable_inputs() -> list[dict[str, str]]:
    """列出能闭合 ExactFactorSupport 的合法输入。"""
    return [
        {
            "input": "CanonicalRIWFactorSupportLowerBound",
            "statement": (
                "the exact Rosser/Iwaniec-Buchstab well-factorable factors used in KZ-E "
                "have log-power lower absolute support in every surviving balanced block"
            ),
            "would_imply": "ExactFactorSupportLowerBound directly",
            "status": "not_present_in_current_ledger",
        },
        {
            "input": "FactorResidueIncidenceBridge",
            "statement": (
                "if moving factor support is too small, then K4 coefficient concentration or "
                "K6 tail-label concentration is triggered"
            ),
            "would_imply": "ExactFactorSupportLowerBound on the clean branch by contrapositive",
            "status": "not_present_in_current_ledger",
        },
        {
            "input": "ExternalDIBFIOriginalDispersion",
            "statement": "original DI/BFI dispersion supplies block variance saving without proving internal support",
            "would_imply": "A1 clean branch closed in external theorem version",
            "status": "acceptable_external_route",
        },
    ]


def run(
    exact_wfd_path: Path,
    min_k: int,
    max_k: int,
    saving_exponent: float,
    divisor_loss_power: float,
    support_power: float,
) -> dict[str, Any]:
    """运行 ExactFactorSupport 路由审计。"""
    exact_wfd = load_json(exact_wfd_path)
    rows = [
        model_row(k, saving_exponent, divisor_loss_power, support_power)
        for k in range(min_k, max_k + 1)
    ]
    return {
        "certificate_type": "triad_a1_exact_factor_support_router",
        "status": "exact_factor_support_not_implied_by_k4_k6_without_incidence_bridge",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "exact_wfd_source_entropy_json": file_sha256(exact_wfd_path),
        },
        "parameters": {
            "min_k": min_k,
            "max_k": max_k,
            "saving_exponent_A": saving_exponent,
            "divisor_loss_power_C": divisor_loss_power,
            "support_power_B": support_power,
            "scale": "y=10^k",
        },
        "exact_wfd_input_status": exact_wfd["status"],
        "gate_rows": build_gate_rows(),
        "acceptable_inputs": build_acceptable_inputs(),
        "rows": rows,
        "all_rows_k4_flat_but_factor_support_fails": all(
            row["k4_flat_enough_for_A"] and row["exact_factor_support_fails"]
            for row in rows
        ),
        "current_internal_exact_factor_support_closed": False,
        "k4_k6_imply_exact_factor_support": False,
        "projection_mismatch_law": (
            "K4 controls residue/phase atoms, while ExactFactorSupport controls moving factor-pair atoms. "
            "K6 controls how many dyadic blocks exist, not how much support each block contains. "
            "Without an incidence bridge bounding how many residue atoms one moving factor pair can hide behind, "
            "K4/K6 do not imply factor support lower bounds."
        ),
        "conditional_closure_law": (
            "ExactFactorSupport can still be closed internally in either of two ways: "
            "prove the canonical Rosser/Iwaniec-Buchstab factor support lower bound directly, "
            "or prove that any failure of factor support triggers existing clean-branch failures "
            "through a FactorResidueIncidenceBridge."
        ),
        "next_internal_target": "FactorResidueIncidenceBridgeOrCanonicalRIWFactorSupport",
        "terminal_gap_after_router": (
            "FactorResidueIncidenceBridgeOrCanonicalRIWFactorSupportOrExternalDIBFIOriginalDispersion"
        ),
        "review_conclusion": (
            "ExactFactorSupportLowerBound 不能从当前 K4/K6 clean admission 自动推出："
            "存在 residue-flat 但 factor-concentrated 的投影错配模型。"
            "下一步必须证明 factor-residue incidence 桥，说明少数 moving factor pairs "
            "会触发既有 K4/K6 失败；或者直接证明 canonical Rosser/Iwaniec-Buchstab 因子支撑下界。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 ExactFactorSupport 路由审计",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 投影错配律",
        "",
        result["projection_mismatch_law"],
        "",
        "```text",
        "K4 flatness lives on residue/phase atoms;",
        "ExactFactorSupport lives on moving factor-pair atoms b=(u,v);",
        "K6 limits the number of dyadic blocks, not the internal support of each block;",
        "therefore K4+K6 need an incidence bridge before they can imply factor support.",
        "```",
        "",
        "## 2. 条件闭合律",
        "",
        result["conditional_closure_law"],
        "",
        "## 3. 汇总",
        "",
        f"- `exact_wfd_input_status={result['exact_wfd_input_status']}`。",
        f"- `all_rows_k4_flat_but_factor_support_fails={result['all_rows_k4_flat_but_factor_support_fails']}`。",
        f"- `k4_k6_imply_exact_factor_support={result['k4_k6_imply_exact_factor_support']}`。",
        f"- `current_internal_exact_factor_support_closed={result['current_internal_exact_factor_support_closed']}`。",
        f"- `next_internal_target={result['next_internal_target']}`。",
        f"- `terminal_gap_after_router={result['terminal_gap_after_router']}`。",
        "",
        "## 4. 门控表",
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
            "## 5. 阻断模型表",
            "",
            "| k | log y | residue atoms | max residue share | K4 flat | factor pairs | factor share | support needed | factor support fails |",
            "| ---: | ---: | ---: | ---: | --- | ---: | ---: | ---: | --- |",
        ]
    )
    for row in result["rows"]:
        lines.append(
            "| {k} | {logy} | {residues} | {rshare} | `{k4}` | {pairs} | {fshare} | {needed} | `{fails}` |".format(
                k=row["k"],
                logy=fmt_float(row["log_y"]),
                residues=row["residue_atoms_in_k4_model"],
                rshare=fmt_float(row["max_residue_share"]),
                k4=row["k4_flat_enough_for_A"],
                pairs=row["moving_factor_pair_count"],
                fshare=fmt_float(row["moving_factor_pair_share"]),
                needed=row["exact_factor_support_needed"],
                fails=row["exact_factor_support_fails"],
            )
        )

    lines.extend(
        [
            "",
            "## 6. 可接受输入",
            "",
            "| input | statement | would imply | status |",
            "| --- | --- | --- | --- |",
        ]
    )
    for row in result["acceptable_inputs"]:
        lines.append(
            "| `{input}` | {statement} | {would_imply} | `{status}` |".format(
                input=table_cell(row["input"]),
                statement=table_cell(row["statement"]),
                would_imply=table_cell(row["would_imply"]),
                status=table_cell(row["status"]),
            )
        )

    lines.extend(
        [
            "",
            "## 7. 结论",
            "",
            "当前推进不是证明失败，而是排除一次偷换：",
            "",
            "```text",
            "residue-flat + dyadic-bookkeeping",
            "  does not imply moving factor-pair support lower bound.",
            "```",
            "",
            "下一步若继续无黑箱路线，应直接证明：",
            "",
            "```text",
            "FactorResidueIncidenceBridge:",
            "  small moving factor support forces an existing K4/K6 failure;",
            "or",
            "CanonicalRIWFactorSupport:",
            "  exact Rosser/Iwaniec-Buchstab factors have broad support in each surviving balanced block.",
            "```",
            "",
            "否则仍只能切到外部 `DI/BFI original dispersion`。",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--exact-wfd-json", type=Path, default=DEFAULT_EXACT_WFD)
    parser.add_argument("--min-k", type=int, default=3)
    parser.add_argument("--max-k", type=int, default=9)
    parser.add_argument("--saving-exponent", type=float, default=2.0)
    parser.add_argument("--divisor-loss-power", type=float, default=2.0)
    parser.add_argument("--support-power", type=float, default=7.0)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        args.exact_wfd_json,
        args.min_k,
        args.max_k,
        args.saving_exponent,
        args.divisor_loss_power,
        args.support_power,
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
