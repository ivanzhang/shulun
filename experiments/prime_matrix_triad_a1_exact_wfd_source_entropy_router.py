#!/usr/bin/env python3
"""把 ExactWFDSourceEntropy 压缩为精确因子支撑下界。

用法示例：
  python3 experiments/prime_matrix_triad_a1_exact_wfd_source_entropy_router.py
  python3 experiments/prime_matrix_triad_a1_exact_wfd_source_entropy_router.py --support-power 8

输出：
  docs/monograph/prime-matrix-triad-a1-exact-wfd-source-entropy-router.json
  docs/monograph/prime-matrix-triad-a1-exact-wfd-source-entropy-router.md
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
DEFAULT_SOURCE_BLOCK = DOCS / "prime-matrix-triad-a1-source-block-entropy-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-exact-wfd-source-entropy-router.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-exact-wfd-source-entropy-router.md"


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
    """生成支撑下界推出源头熵的尺度模型。"""
    y = 10**k
    log_y = math.log(y)
    u_size = log_y**support_power
    v_size = log_y**support_power
    max_pair_share_bound = log_y ** (4.0 * divisor_loss_power) / (u_size * v_size)
    required_share = log_y ** (-2.0 * saving_exponent)
    support_threshold_power = saving_exponent + 2.0 * divisor_loss_power
    return {
        "k": k,
        "y": y,
        "log_y": log_y,
        "saving_exponent_A": saving_exponent,
        "divisor_loss_power_C": divisor_loss_power,
        "support_power_B": support_power,
        "support_threshold_power_A_plus_2C": support_threshold_power,
        "model_u_support_size": u_size,
        "model_v_support_size": v_size,
        "required_max_block_share": required_share,
        "max_pair_share_from_support_bound": max_pair_share_bound,
        "support_bound_suffices": max_pair_share_bound <= required_share,
    }


def build_gate_rows() -> list[dict[str, Any]]:
    """列出 ExactWFDSourceEntropy 的必要门。"""
    return [
        {
            "gate": "BalancedRangeSize",
            "available": "WFD reduction gives U,V=C^(1/2) log^(O(1)) on balanced blocks",
            "needed": "balanced ranges are at least log(y)^B in the clean non-edge case",
            "gap": "range size is plausible from K1/K6, but exact lower thresholds are not recorded in A1 ledger",
            "route": "record explicit lower-size threshold or route small ranges back to finite PDEC/SAE",
            "closed": False,
        },
        {
            "gate": "DivisorBoundedFactors",
            "available": "|alpha_u|, |delta_v| <= tau(uv)^C after well-factorable splitting",
            "needed": "polylog upper bound for each factor atom",
            "gap": "this is part of the WFD template and only costs a fixed log power",
            "route": "absorb into support threshold B >= A+2C",
            "closed": True,
        },
        {
            "gate": "ExactFactorSupportLowerBound",
            "available": "not currently present as a theorem for exact Rosser/Iwaniec-Buchstab factors",
            "needed": "sum |alpha_u| >= U/log^C and sum |delta_v| >= V/log^C on each surviving balanced block",
            "gap": "without this, bounded factors may still be supported on one moving u and one moving v",
            "route": "prove squarefree/Buchstab support lower bound for exact sieve factors or route to external DI/BFI",
            "closed": False,
        },
        {
            "gate": "TypeFourierCapacityCompatibility",
            "available": "Type-I/II and h-smoothing share the same dyadic formal unit",
            "needed": "their Cauchy capacity does not multiply a single factor pair by an unrecorded atom",
            "gap": "current K4 is fixed-residue L2-flat, not a moving factor-pair support theorem",
            "route": "state a capacity compatibility lemma or make it part of ExactFactorSupportLowerBound",
            "closed": False,
        },
        {
            "gate": "SupportLowerBoundImpliesEntropy",
            "available": "elementary inequality max pair share <= log^(4C)/(UV)",
            "needed": "UV >= log(y)^(2A+4C)",
            "gap": "the implication is proved; only the exact support hypotheses remain",
            "route": "ExactFactorSupportLowerBound",
            "closed": True,
        },
    ]


def run(
    source_block_path: Path,
    min_k: int,
    max_k: int,
    saving_exponent: float,
    divisor_loss_power: float,
    support_power: float,
) -> dict[str, Any]:
    """运行 exact WFD 源头熵路由。"""
    source_block = load_json(source_block_path)
    rows = [
        model_row(k, saving_exponent, divisor_loss_power, support_power)
        for k in range(min_k, max_k + 1)
    ]
    support_threshold_power = saving_exponent + 2.0 * divisor_loss_power
    return {
        "certificate_type": "triad_a1_exact_wfd_source_entropy_router",
        "status": "exact_wfd_source_entropy_reduced_to_factor_support_lower_bound",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "source_block_entropy_json": file_sha256(source_block_path),
        },
        "parameters": {
            "min_k": min_k,
            "max_k": max_k,
            "saving_exponent_A": saving_exponent,
            "divisor_loss_power_C": divisor_loss_power,
            "support_power_B": support_power,
            "scale": "y=10^k",
        },
        "source_block_input_status": source_block["status"],
        "gate_rows": build_gate_rows(),
        "rows": rows,
        "conditional_factor_support_implies_exact_source_entropy": True,
        "exact_factor_support_lower_bound_present": False,
        "current_internal_exact_wfd_source_entropy_closed": False,
        "all_model_rows_support_bound_suffices": all(
            row["support_bound_suffices"] for row in rows
        ),
        "support_threshold_law": (
            "若 |alpha_u|,|delta_v| <= log(y)^C，且 "
            "sum|alpha_u| >= U/log(y)^C、sum|delta_v| >= V/log(y)^C，"
            "则任一 moving pair 的容量份额至多 log(y)^(4C)/(UV)。"
            "因此只要 U,V >= log(y)^B 且 B>=A+2C，就推出 ExactWFDSourceEntropy(A)。"
        ),
        "missing_input_law": (
            "当前 A1/KLS ledger 有 balanced dyadic range、divisor bound、fixed-residue L2-flat，"
            "但没有逐 balanced block 的 exact factor support lower bound。"
            "所以 ExactWFDSourceEntropy 已化为一个初等筛权支撑命题，而非新的谱大筛命题。"
        ),
        "support_threshold_power_A_plus_2C": support_threshold_power,
        "next_internal_target": "ExactFactorSupportLowerBound",
        "terminal_gap_after_router": "ExactFactorSupportLowerBoundOrExternalDIBFIOriginalDispersion",
        "review_conclusion": (
            "ExactWFDSourceEntropy 不需要再依赖抽象 moving-block diffuse："
            "若精确 well-factorable 因子在每个 surviving balanced block 内有多对数以上支撑，"
            "divisor-bound 立即给出单块容量份额的任意对数小上界。"
            "当前缺口不是谱相消，而是尚未登记 exact Rosser/Iwaniec-Buchstab 因子支撑下界"
            "及 Type/Fourier 容量兼容。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 ExactWFDSourceEntropy 路由审计",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 支撑下界闭合律",
        "",
        result["support_threshold_law"],
        "",
        "结构推导如下：",
        "",
        "```text",
        "Assume |alpha_u|, |delta_v| <= L^C, L=log y.",
        "Assume sum_u |alpha_u| >= U/L^C and sum_v |delta_v| >= V/L^C.",
        "Then max_{u,v} |alpha_u delta_v| / (sum|alpha| sum|delta|)",
        "  <= L^(4C)/(UV).",
        "If U,V >= L^B and B >= A+2C, this is <= L^(-2A).",
        "Therefore exact factor support lower bound => ExactWFDSourceEntropy(A).",
        "```",
        "",
        "这一步把源头熵从谱大筛问题降为精确筛权支撑问题。",
        "",
        "## 2. 当前缺口",
        "",
        result["missing_input_law"],
        "",
        "## 3. 汇总",
        "",
        f"- `source_block_input_status={result['source_block_input_status']}`。",
        f"- `conditional_factor_support_implies_exact_source_entropy={result['conditional_factor_support_implies_exact_source_entropy']}`。",
        f"- `exact_factor_support_lower_bound_present={result['exact_factor_support_lower_bound_present']}`。",
        f"- `current_internal_exact_wfd_source_entropy_closed={result['current_internal_exact_wfd_source_entropy_closed']}`。",
        f"- `support_threshold_power_A_plus_2C={result['support_threshold_power_A_plus_2C']}`。",
        f"- `all_model_rows_support_bound_suffices={result['all_model_rows_support_bound_suffices']}`。",
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
            "## 5. 阈值模型表",
            "",
            "| k | log y | B | C | required share | support-share bound | suffices |",
            "| ---: | ---: | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for row in result["rows"]:
        lines.append(
            "| {k} | {logy} | {b} | {c} | {required} | {bound} | `{suffices}` |".format(
                k=row["k"],
                logy=fmt_float(row["log_y"]),
                b=fmt_float(row["support_power_B"]),
                c=fmt_float(row["divisor_loss_power_C"]),
                required=fmt_float(row["required_max_block_share"]),
                bound=fmt_float(row["max_pair_share_from_support_bound"]),
                suffices=row["support_bound_suffices"],
            )
        )

    lines.extend(
        [
            "",
            "## 6. 结论",
            "",
            "当前已证明的推进是：",
            "",
            "```text",
            "ExactFactorSupportLowerBound => ExactWFDSourceEntropy",
            "=> SourceBlockEntropyNCBLK => NC-BLK.",
            "```",
            "",
            "但 `ExactFactorSupportLowerBound` 尚未在当前 ledger 中出现。下一步要么证明精确筛权支撑下界，",
            "要么继续走外部 `DI/BFI original dispersion`。",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-block-json", type=Path, default=DEFAULT_SOURCE_BLOCK)
    parser.add_argument("--min-k", type=int, default=3)
    parser.add_argument("--max-k", type=int, default=9)
    parser.add_argument("--saving-exponent", type=float, default=2.0)
    parser.add_argument("--divisor-loss-power", type=float, default=2.0)
    parser.add_argument("--support-power", type=float, default=7.0)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        args.source_block_json,
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
