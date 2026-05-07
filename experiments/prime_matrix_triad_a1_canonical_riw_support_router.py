#!/usr/bin/env python3
"""把 CanonicalRIWFactorSupportLowerBound 压缩为 squarefree Buchstab 支撑下界。

用法示例：
  python3 experiments/prime_matrix_triad_a1_canonical_riw_support_router.py
  python3 experiments/prime_matrix_triad_a1_canonical_riw_support_router.py --prime-density-loss 2

输出：
  docs/monograph/prime-matrix-triad-a1-canonical-riw-support-router.json
  docs/monograph/prime-matrix-triad-a1-canonical-riw-support-router.md
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
DEFAULT_INCIDENCE = DOCS / "prime-matrix-triad-a1-factor-residue-incidence-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-canonical-riw-support-router.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-canonical-riw-support-router.md"


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
    support_power: float,
    divisor_loss_power: float,
    prime_density_loss: float,
) -> dict[str, Any]:
    """生成 squarefree product 支撑阈值模型。"""
    y = 10**k
    log_y = math.log(y)
    interval_size = log_y**support_power
    expected_squarefree_products = interval_size / (log_y**prime_density_loss)
    required_absolute_mass = interval_size / (log_y**divisor_loss_power)
    support_lemma_suffices = expected_squarefree_products >= required_absolute_mass
    return {
        "k": k,
        "y": y,
        "log_y": log_y,
        "support_power_B": support_power,
        "divisor_loss_power_C": divisor_loss_power,
        "prime_density_loss_E": prime_density_loss,
        "model_interval_size": interval_size,
        "expected_squarefree_products": expected_squarefree_products,
        "required_absolute_mass": required_absolute_mass,
        "support_lemma_suffices": support_lemma_suffices,
    }


def build_gate_rows() -> list[dict[str, Any]]:
    """列出 canonical RIW 支撑的门控。"""
    return [
        {
            "gate": "CanonicalFactorizationFixed",
            "available": "WFD ledger uses existence of well-factorable splitting",
            "needed": "a specified canonical Rosser/Iwaniec-Buchstab splitting alpha*delta",
            "gap": "support statements are meaningless until the splitting is fixed",
            "route": "define the exact RIW/Buchstab factorization used in KZ-E",
            "closed": False,
        },
        {
            "gate": "SquarefreeBuchstabLayerSupport",
            "available": "not present as a local lower-bound lemma",
            "needed": "many squarefree products in each surviving balanced dyadic factor interval",
            "gap": "this is a short multiplicative interval support theorem, not a Kloosterman estimate",
            "route": "prove by Buchstab recursion/Mertens product or route thin intervals to edge/PDEC",
            "closed": False,
        },
        {
            "gate": "NonzeroCoefficientTransfer",
            "available": "RIW factors are divisor-bounded",
            "needed": "squarefree products counted by the support lemma carry nonzero canonical coefficients",
            "gap": "parity/layer truncation can zero out a combinatorial class unless layer admission is recorded",
            "route": "record layer support and parity nonvanishing for the exact construction",
            "closed": False,
        },
        {
            "gate": "SmallOrThinIntervalReturn",
            "available": "K1/K3/K6 and finite PDEC/SAE exits exist",
            "needed": "balanced intervals too short for support lemma do not remain in clean branch",
            "gap": "threshold return is not yet connected to canonical support",
            "route": "prove thin support => edge/endpoint/tail-label failure",
            "closed": False,
        },
        {
            "gate": "SupportLemmaImpliesRIWSupport",
            "available": "elementary once previous gates hold",
            "needed": "sum |alpha_u| >= U/log^C and sum |delta_v| >= V/log^C",
            "gap": "conditional implication is clear; hypotheses remain",
            "route": "SquarefreeBuchstabLayerSupport + NonzeroCoefficientTransfer",
            "closed": True,
        },
    ]


def run(
    incidence_path: Path,
    min_k: int,
    max_k: int,
    support_power: float,
    divisor_loss_power: float,
    prime_density_loss: float,
) -> dict[str, Any]:
    """运行 canonical RIW 支撑路由。"""
    incidence = load_json(incidence_path)
    rows = [
        model_row(k, support_power, divisor_loss_power, prime_density_loss)
        for k in range(min_k, max_k + 1)
    ]
    return {
        "certificate_type": "triad_a1_canonical_riw_support_router",
        "status": "canonical_riw_support_reduced_to_squarefree_buchstab_layer_support",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "factor_residue_incidence_json": file_sha256(incidence_path),
        },
        "parameters": {
            "min_k": min_k,
            "max_k": max_k,
            "support_power_B": support_power,
            "divisor_loss_power_C": divisor_loss_power,
            "prime_density_loss_E": prime_density_loss,
            "scale": "y=10^k",
        },
        "incidence_input_status": incidence["status"],
        "gate_rows": build_gate_rows(),
        "rows": rows,
        "all_model_rows_support_lemma_suffices": all(
            row["support_lemma_suffices"] for row in rows
        ),
        "canonical_riw_support_closed": False,
        "conditional_squarefree_support_implies_riw_support": True,
        "reduction_law": (
            "Canonical RIW support is not a spectral problem. Once the exact factorization is fixed, "
            "it follows from a local lower bound for squarefree Buchstab-layer products in every "
            "surviving balanced dyadic interval, plus nonzero transfer of those products into the "
            "canonical alpha and delta coefficients."
        ),
        "next_internal_target": "SquarefreeBuchstabLayerSupportLowerBound",
        "terminal_gap_after_router": (
            "SquarefreeBuchstabLayerSupportLowerBoundOrExternalDIBFIOriginalDispersion"
        ),
        "review_conclusion": (
            "CanonicalRIWFactorSupportLowerBound 已被压缩为一个更初等的组合筛支撑命题："
            "固定 exact Rosser/Iwaniec-Buchstab 分解后，只需证明 surviving balanced dyadic "
            "factor interval 中有足够多非零 squarefree Buchstab-layer products，并把薄区间返回"
            " edge/PDEC/SAE。当前 ledger 尚未提供这个局部支撑下界。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 CanonicalRIWFactorSupport 路由审计",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 归约律",
        "",
        result["reduction_law"],
        "",
        "```text",
        "fix canonical RIW/Buchstab factorization alpha*delta;",
        "prove many squarefree Buchstab-layer products in each surviving balanced interval;",
        "prove those products carry nonzero alpha/delta coefficients;",
        "then sum |alpha_u|, sum |delta_v| have log-power lower bounds.",
        "```",
        "",
        "## 2. 汇总",
        "",
        f"- `incidence_input_status={result['incidence_input_status']}`。",
        f"- `conditional_squarefree_support_implies_riw_support={result['conditional_squarefree_support_implies_riw_support']}`。",
        f"- `canonical_riw_support_closed={result['canonical_riw_support_closed']}`。",
        f"- `all_model_rows_support_lemma_suffices={result['all_model_rows_support_lemma_suffices']}`。",
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
            "## 4. 阈值模型表",
            "",
            "| k | log y | interval size | expected sqfree products | required mass | suffices |",
            "| ---: | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for row in result["rows"]:
        lines.append(
            "| {k} | {logy} | {size} | {expected} | {required} | `{suffices}` |".format(
                k=row["k"],
                logy=fmt_float(row["log_y"]),
                size=fmt_float(row["model_interval_size"]),
                expected=fmt_float(row["expected_squarefree_products"]),
                required=fmt_float(row["required_absolute_mass"]),
                suffices=row["support_lemma_suffices"],
            )
        )

    lines.extend(
        [
            "",
            "## 5. 结论",
            "",
            "当前新最窄目标为：",
            "",
            "```text",
            "SquarefreeBuchstabLayerSupportLowerBound:",
            "  every surviving balanced dyadic factor interval contains enough nonzero",
            "  squarefree products in the canonical RIW/Buchstab layer.",
            "```",
            "",
            "这仍不是行命题最终证明；它把 canonical RIW 支撑问题降到局部组合筛支撑下界。",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--incidence-json", type=Path, default=DEFAULT_INCIDENCE)
    parser.add_argument("--min-k", type=int, default=3)
    parser.add_argument("--max-k", type=int, default=9)
    parser.add_argument("--support-power", type=float, default=7.0)
    parser.add_argument("--divisor-loss-power", type=float, default=3.0)
    parser.add_argument("--prime-density-loss", type=float, default=2.0)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        args.incidence_json,
        args.min_k,
        args.max_k,
        args.support_power,
        args.divisor_loss_power,
        args.prime_density_loss,
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
