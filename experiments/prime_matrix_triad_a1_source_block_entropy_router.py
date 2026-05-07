#!/usr/bin/env python3
"""审计 SourceBlockEntropyNCBLK 是否由当前形式 WFD 输入强制推出。

用法示例：
  python3 experiments/prime_matrix_triad_a1_source_block_entropy_router.py
  python3 experiments/prime_matrix_triad_a1_source_block_entropy_router.py --max-k 10

输出：
  docs/monograph/prime-matrix-triad-a1-source-block-entropy-router.json
  docs/monograph/prime-matrix-triad-a1-source-block-entropy-router.md
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
DEFAULT_MOVING_BLOCK = (
    DOCS / "prime-matrix-triad-a1-moving-block-spread-obstruction.json"
)
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-source-block-entropy-router.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-source-block-entropy-router.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_float(value: float) -> str:
    """格式化浮点数。"""
    return f"{value:.6g}"


def model_row(k: int, saving_exponent: float) -> dict[str, Any]:
    """生成一个尺度上的源头块熵阻断模型。

    模型含义：
    - SourceBlockEntropy(A) 至少要求最大 moving block 容量份额为 log(y)^(-2A)；
    - spread model 把容量分到足够多 moving blocks，满足该条件；
    - moving-delta WFD model 用一点型 well-factorable 因子集中到一个新块，
      不违反形式 WFD/Type/Fourier 模板，但完全破坏源头块熵。
    """
    y = 10**k
    log_y = math.log(y)
    required_share = log_y ** (-2.0 * saving_exponent)
    required_entropy_nats = -math.log(required_share)
    spread_block_count = math.ceil(1.0 / required_share)
    spread_max_share = 1.0 / spread_block_count
    return {
        "k": k,
        "y": y,
        "log_y": log_y,
        "saving_exponent_A": saving_exponent,
        "required_max_block_capacity_share": required_share,
        "required_min_entropy_nats": required_entropy_nats,
        "spread_block_count_needed": spread_block_count,
        "spread_model_max_block_share": spread_max_share,
        "spread_model_satisfies_source_entropy": spread_max_share <= required_share,
        "moving_delta_model_max_block_share": 1.0,
        "moving_delta_model_min_entropy_nats": 0.0,
        "moving_delta_violates_source_entropy": 1.0 > required_share,
        "formal_wfd_delta_factors_admissible_at_template_level": True,
    }


def build_gate_rows() -> list[dict[str, Any]]:
    """列出当前输入到 SourceBlockEntropy 的缺口。"""
    return [
        {
            "gate": "WellFactorableConvolution",
            "available": "lambda_c admits bounded convolution factorizations after choosing dyadic ranges",
            "needed": "each moving same-(u,v) block has max capacity share <= log(y)^(-2A)",
            "gap": "bounded convolution factors may be point-supported on a moving u and v",
            "route": "prove exact sieve weights have anti-atom entropy, not merely well-factorability",
            "closed": False,
        },
        {
            "gate": "TypeITypeIIDecomposition",
            "available": "Vaughan/Heath-Brown blocks with divisor-bounded coefficients",
            "needed": "entropy across factor-pair blocks after every Type split",
            "gap": "Type decomposition is algebraic and does not forbid one dyadic factor-pair from carrying the mass",
            "route": "add a genuine source anti-concentration theorem for the produced coefficients",
            "closed": False,
        },
        {
            "gate": "FourierSmoothing",
            "available": "smooth h-window and finite nonzero Fourier frequencies",
            "needed": "non-concentration in the moving block coordinate b=(u,v)",
            "gap": "frequency smoothing acts in h, not in the factorization block coordinate",
            "route": "prove block entropy before or inside the dispersion identity",
            "closed": False,
        },
        {
            "gate": "FixedProjectionDiffuse",
            "available": "every fixed finite signature eventually has small mass",
            "needed": "uniform control of growing labels b_y=(u_y,v_y)",
            "gap": "a moving-delta block can evade every fixed projection while staying concentrated",
            "route": "replace fixed-projection diffuse by scale-uniform moving-block entropy",
            "closed": False,
        },
        {
            "gate": "ConditionalImplicationToNCBLK",
            "available": "Cauchy capacity identity sum_b M_b^2 <= max_b(M_b/M) M^2",
            "needed": "max_b M_b/M <= log(y)^(-2A) for actual source blocks",
            "gap": "the implication is valid, but the hypothesis is not yet proved upstream",
            "route": "ExactWFDSourceEntropy or external original dispersion",
            "closed": True,
        },
    ]


def build_acceptable_inputs() -> list[dict[str, str]]:
    """列出能继续闭合该口的合法输入。"""
    return [
        {
            "input": "ExactWFDSourceEntropy",
            "statement": (
                "for the exact Rosser/Iwaniec-Buchstab + Type-I/II + Fourier coefficients, "
                "max moving same-(u,v) block capacity share is <= log(y)^(-2A)"
            ),
            "would_imply": "SourceBlockEntropyNCBLK, hence NC-BLK via the Cauchy capacity inequality",
            "status": "not_present_in_current_ledger",
        },
        {
            "input": "StrengthenedCleanAdmissionWithMovingEntropy",
            "statement": "upgrade K1--K9 clean admission to include scale-uniform moving-block entropy",
            "would_imply": "internal A1 clean branch closure after proving the upgraded admission from prior routes",
            "status": "would_be_sufficient_but_unproved",
        },
        {
            "input": "ExternalDIBFIOriginalDispersion",
            "statement": "original DI/BFI dispersion theorem supplies the needed block variance saving directly",
            "would_imply": "A1 clean branch closed in external-deep-theorem version",
            "status": "acceptable_external_route",
        },
    ]


def run(
    moving_block_path: Path,
    min_k: int,
    max_k: int,
    saving_exponent: float,
) -> dict[str, Any]:
    """运行 SourceBlockEntropy 路由审计。"""
    moving_block = load_json(moving_block_path)
    rows = [model_row(k, saving_exponent) for k in range(min_k, max_k + 1)]
    return {
        "certificate_type": "triad_a1_source_block_entropy_router",
        "status": "source_block_entropy_not_forced_by_formal_wfd_inputs",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "moving_block_spread_obstruction_json": file_sha256(moving_block_path),
        },
        "parameters": {
            "min_k": min_k,
            "max_k": max_k,
            "saving_exponent_A": saving_exponent,
            "scale": "y=10^k",
        },
        "moving_block_input_status": moving_block["status"],
        "gate_rows": build_gate_rows(),
        "acceptable_inputs": build_acceptable_inputs(),
        "rows": rows,
        "source_entropy_gap_exists": True,
        "conditional_source_entropy_implies_ncblk": True,
        "current_internal_source_entropy_closed": False,
        "all_spread_models_satisfy_source_entropy": all(
            row["spread_model_satisfies_source_entropy"] for row in rows
        ),
        "all_moving_delta_models_violate_source_entropy": all(
            row["moving_delta_violates_source_entropy"] for row in rows
        ),
        "moving_delta_obstruction_law": (
            "形式 well-factorable/Type/Fourier 模板只限制因子可分解性、系数大小与频率平滑，"
            "不禁止每个尺度选择一个新的 moving block b_y=(u_y,v_y) 承载全部容量。"
            "因此 SourceBlockEntropy 不能由当前形式输入自动推出。"
        ),
        "conditional_implication_law": (
            "若实际源块满足 max_b M_b/M <= log(y)^(-2A)，则 "
            "sum_b |S_b|^2 <= sum_b M_b^2 <= max_b(M_b/M) M^2，"
            "从而得到 NC-BLK 所需的任意对数块能量节省。"
        ),
        "next_internal_target": "ExactWFDSourceEntropy",
        "terminal_gap_after_router": "ExactWFDSourceEntropyOrExternalDIBFIOriginalDispersion",
        "review_conclusion": (
            "SourceBlockEntropy 是足够强的正确入口：一旦证明，即可推出 NC-BLK。"
            "但它不由当前形式 WFD/Type-I-II/Fourier 准入条件强制；moving-delta "
            "well-factorable 模型在每个尺度集中到一个新 `(u,v)` 块，仍能通过形式模板。"
            "内部无黑箱路线必须继续证明 exact WFD source entropy，外部路线仍是 DI/BFI 原始 dispersion。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 SourceBlockEntropy 路由审计",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 条件闭合律",
        "",
        result["conditional_implication_law"],
        "",
        "写成结构公式：",
        "",
        "```text",
        "M_b = Cauchy capacity of moving block b=(u,v)",
        "M   = sum_b M_b",
        "if max_b M_b/M <= log(y)^(-2A), then",
        "  sum_b |S_b|^2 <= sum_b M_b^2 <= log(y)^(-2A) M^2.",
        "```",
        "",
        "因此 `SourceBlockEntropyNCBLK` 本身是正确的充分条件；问题只剩它是否能从上游结构推出。",
        "",
        "## 2. moving-delta 阻断律",
        "",
        result["moving_delta_obstruction_law"],
        "",
        "```text",
        "well-factorable convolution permits bounded point-supported factors at template level；",
        "Type-I/II decomposition is algebraic and does not create block entropy；",
        "Fourier smoothing controls h, not the moving block b=(u,v)；",
        "fixed-projection diffuse cannot see a block label moving with the scale。",
        "```",
        "",
        "## 3. 汇总",
        "",
        f"- `moving_block_input_status={result['moving_block_input_status']}`。",
        f"- `conditional_source_entropy_implies_ncblk={result['conditional_source_entropy_implies_ncblk']}`。",
        f"- `source_entropy_gap_exists={result['source_entropy_gap_exists']}`。",
        f"- `current_internal_source_entropy_closed={result['current_internal_source_entropy_closed']}`。",
        f"- `all_spread_models_satisfy_source_entropy={result['all_spread_models_satisfy_source_entropy']}`。",
        f"- `all_moving_delta_models_violate_source_entropy={result['all_moving_delta_models_violate_source_entropy']}`。",
        f"- `next_internal_target={result['next_internal_target']}`。",
        f"- `terminal_gap_after_router={result['terminal_gap_after_router']}`。",
        "",
        "## 4. 缺口表",
        "",
        "| gate | available | needed | gap | route | closed |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for row in result["gate_rows"]:
        lines.append(
            "| `{gate}` | {available} | {needed} | {gap} | {route} | `{closed}` |".format(
                gate=row["gate"],
                available=row["available"],
                needed=row["needed"],
                gap=row["gap"],
                route=row["route"],
                closed=row["closed"],
            )
        )

    lines.extend(
        [
            "",
            "## 5. 模型审计表",
            "",
            "| k | log y | required max share | entropy needed | spread blocks | spread share | delta share | delta violates |",
            "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for row in result["rows"]:
        lines.append(
            "| {k} | {logy} | {required} | {entropy} | {blocks} | {spread} | {delta} | `{violates}` |".format(
                k=row["k"],
                logy=fmt_float(row["log_y"]),
                required=fmt_float(row["required_max_block_capacity_share"]),
                entropy=fmt_float(row["required_min_entropy_nats"]),
                blocks=row["spread_block_count_needed"],
                spread=fmt_float(row["spread_model_max_block_share"]),
                delta=fmt_float(row["moving_delta_model_max_block_share"]),
                violates=row["moving_delta_violates_source_entropy"],
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
                input=row["input"],
                statement=row["statement"],
                would_imply=row["would_imply"],
                status=row["status"],
            )
        )

    lines.extend(
        [
            "",
            "## 7. 结论",
            "",
            "本步给出一个正向闭合和一个负向阻断：",
            "",
            "```text",
            "SourceBlockEntropyNCBLK => NC-BLK;",
            "formal WFD/Type-I-II/Fourier inputs do not imply SourceBlockEntropyNCBLK.",
            "```",
            "",
            "所以下一步若继续完全无黑箱路线，目标必须再收窄为：",
            "",
            "```text",
            "ExactWFDSourceEntropy:",
            "prove the exact sieve/Type/Fourier coefficients cannot concentrate on a moving same-(u,v) block.",
            "```",
            "",
            "否则只能切到外部 `DI/BFI original dispersion`。",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--moving-block-json", type=Path, default=DEFAULT_MOVING_BLOCK)
    parser.add_argument("--min-k", type=int, default=3)
    parser.add_argument("--max-k", type=int, default=9)
    parser.add_argument("--saving-exponent", type=float, default=2.0)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        args.moving_block_json,
        args.min_k,
        args.max_k,
        args.saving_exponent,
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
