#!/usr/bin/env python3
"""硬攻 exact canonical 层承认、非零转移与薄块回流。

用法示例：
  python3 experiments/prime_matrix_triad_a1_layer_transfer_router.py
  python3 experiments/prime_matrix_triad_a1_layer_transfer_router.py --selector-retention-loss 0.5

输出：
  docs/monograph/prime-matrix-triad-a1-layer-transfer-router.json
  docs/monograph/prime-matrix-triad-a1-layer-transfer-router.md
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
DEFAULT_SQUAREFREE = DOCS / "prime-matrix-triad-a1-squarefree-buchstab-support-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-layer-transfer-router.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-layer-transfer-router.md"


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


def retention_row(
    k: int,
    support_power: float,
    buchstab_loss: float,
    selector_retention_loss: float,
    required_loss: float,
) -> dict[str, Any]:
    """生成 canonical selector 保留率阈值行。"""
    y = 10**k
    log_y = math.log(y)
    interval_size = log_y**support_power
    raw_support = interval_size / (log_y**buchstab_loss)
    retained_support = raw_support / (log_y**selector_retention_loss)
    required_support = interval_size / (log_y**required_loss)
    retention_suffices = retained_support >= required_support
    max_allowed_selector_loss = required_loss - buchstab_loss
    return {
        "k": k,
        "y": y,
        "log_y": log_y,
        "support_power_B": support_power,
        "buchstab_loss_power_E": buchstab_loss,
        "selector_retention_loss_R": selector_retention_loss,
        "required_loss_power_C": required_loss,
        "max_allowed_selector_loss_C_minus_E": max_allowed_selector_loss,
        "model_interval_size": interval_size,
        "raw_support": raw_support,
        "retained_support": retained_support,
        "required_support": required_support,
        "retention_suffices": retention_suffices,
    }


def build_gate_rows() -> list[dict[str, Any]]:
    """列出 exact 层转移的门控。"""
    return [
        {
            "gate": "ExactCoefficientFormulaFixed",
            "available": "RIW/Buchstab factors are named but the exact selector is not ledgered here",
            "needed": "an explicit formula for alpha_u and delta_v on the canonical layer",
            "gap": "without the formula, layer admission is a label rather than a checkable predicate",
            "route": "record the canonical RIW path selector, parity rule and dyadic truncation rule",
            "closed": False,
        },
        {
            "gate": "SelectorRetentionLowerBound",
            "available": "raw thick Buchstab support has already been paid",
            "needed": "the exact selector keeps at least a log-power fraction of raw support",
            "gap": "a selector could be formally well-factorable but keep a sparse sublayer",
            "route": "prove retained_support >= raw_support/log^R in every clean thick block",
            "closed": False,
        },
        {
            "gate": "NonzeroTransferAfterSelection",
            "available": "once selected support is defined by alpha_u != 0 or delta_v != 0",
            "needed": "selected products carry nonzero coefficients in absolute support",
            "gap": "this is tautological only after the exact coefficient formula is fixed",
            "route": "define admission by nonzero coefficient, then no extra cancellation gate remains",
            "closed": True,
        },
        {
            "gate": "RejectedOrThinCleanReturn",
            "available": "edge/PDEC/SAE exits exist elsewhere",
            "needed": "blocks failing thickness or selector retention cannot stay in clean A1",
            "gap": "clean admission has not yet been stated as the contrapositive of this failure",
            "route": "add clean-branch contract: low retention => endpoint/edge/tail-label/PDEC exit",
            "closed": False,
        },
        {
            "gate": "LayerTransferImpliesSquarefreeSupport",
            "available": "previous squarefree router closed raw thick support",
            "needed": "selector retention plus return contract",
            "gap": "conditional implication is direct; the selector/return contract remains",
            "route": "combine retained support with nonzero transfer",
            "closed": True,
        },
    ]


def run(
    squarefree_path: Path,
    min_k: int,
    max_k: int,
    support_power: float,
    buchstab_loss: float,
    selector_retention_loss: float,
    required_loss: float,
) -> dict[str, Any]:
    """运行 exact 层转移路由。"""
    squarefree = load_json(squarefree_path)
    rows = [
        retention_row(
            k,
            support_power,
            buchstab_loss,
            selector_retention_loss,
            required_loss,
        )
        for k in range(min_k, max_k + 1)
    ]
    all_retention_model_rows_suffice = all(row["retention_suffices"] for row in rows)
    return {
        "certificate_type": "triad_a1_layer_transfer_router",
        "status": "layer_transfer_reduced_to_selector_retention_or_clean_return",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "squarefree_buchstab_support_json": file_sha256(squarefree_path),
        },
        "parameters": {
            "min_k": min_k,
            "max_k": max_k,
            "support_power_B": support_power,
            "buchstab_loss_power_E": buchstab_loss,
            "selector_retention_loss_R": selector_retention_loss,
            "required_loss_power_C": required_loss,
            "scale": "y=10^k",
        },
        "squarefree_input_status": squarefree["status"],
        "squarefree_input_next_target": squarefree["next_internal_target"],
        "gate_rows": build_gate_rows(),
        "rows": rows,
        "all_retention_model_rows_suffice": all_retention_model_rows_suffice,
        "exact_coefficient_formula_fixed": False,
        "selector_retention_lower_bound_closed": False,
        "rejected_or_thin_clean_return_closed": False,
        "layer_transfer_closed": False,
        "conditional_selector_retention_implies_layer_transfer": True,
        "reduction_law": (
            "Layer admission and nonzero transfer should not be treated as two mysterious "
            "analytic estimates. Once the exact canonical coefficient formula is fixed, "
            "admission can be defined by nonzero coefficient support. The only real quantitative "
            "obligation is selector retention: the canonical selector must retain a log-power "
            "fraction of the raw thick Buchstab support in every clean block; if it does not, "
            "that block must be rejected into an existing edge/PDEC/SAE exit."
        ),
        "next_internal_target": "CanonicalSelectorRetentionOrCleanReturn",
        "terminal_gap_after_router": (
            "CanonicalSelectorRetentionOrCleanReturnOrExternalDIBFIOriginalDispersion"
        ),
        "review_conclusion": (
            "exact 层承认、非零转移与薄块回流已被压成一个更尖锐的合同："
            "先固定 alpha/delta 的 canonical 系数公式；随后非零转移按定义闭合；"
            "真正需要证明的是 selector 在每个 clean 厚块中至少保留 log-power 比例的 "
            "Buchstab 支撑，否则该块必须从 clean 分支退出到 edge/PDEC/SAE。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 Canonical Layer Transfer 路由审计",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 选择器保留律",
        "",
        result["reduction_law"],
        "",
        "```text",
        "raw thick Buchstab support >= interval/log^E;",
        "canonical selector retains >= log^-R of that support;",
        "if E+R <= C, retained nonzero coefficients >= interval/log^C;",
        "if selector retention fails, the block must return to edge/PDEC/SAE.",
        "```",
        "",
        "## 2. 汇总",
        "",
        f"- `squarefree_input_status={result['squarefree_input_status']}`。",
        f"- `squarefree_input_next_target={result['squarefree_input_next_target']}`。",
        f"- `all_retention_model_rows_suffice={result['all_retention_model_rows_suffice']}`。",
        f"- `conditional_selector_retention_implies_layer_transfer={result['conditional_selector_retention_implies_layer_transfer']}`。",
        f"- `layer_transfer_closed={result['layer_transfer_closed']}`。",
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
            "## 4. 保留率阈值模型",
            "",
            "| k | log y | raw support | retained support | required support | max selector loss | suffices |",
            "| ---: | ---: | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for row in result["rows"]:
        lines.append(
            "| {k} | {logy} | {raw} | {retained} | {required} | {maxloss} | `{suffices}` |".format(
                k=row["k"],
                logy=fmt_float(row["log_y"]),
                raw=fmt_float(row["raw_support"]),
                retained=fmt_float(row["retained_support"]),
                required=fmt_float(row["required_support"]),
                maxloss=fmt_float(row["max_allowed_selector_loss_C_minus_E"]),
                suffices=row["retention_suffices"],
            )
        )

    lines.extend(
        [
            "",
            "## 5. 结论",
            "",
            "新最窄内部目标为：",
            "",
            "```text",
            "CanonicalSelectorRetentionOrCleanReturn:",
            "  fix the exact canonical RIW/Buchstab coefficient selector;",
            "  prove it retains a log-power fraction of thick Buchstab support in every clean block;",
            "  otherwise prove the block exits to edge/PDEC/SAE.",
            "```",
            "",
            "这仍不是行命题最终闭合；但它把 nonzero transfer 的语义问题压成了一个可审稿的"
            "选择器保留率/clean 反向退出合同。",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--squarefree-json", type=Path, default=DEFAULT_SQUAREFREE)
    parser.add_argument("--min-k", type=int, default=3)
    parser.add_argument("--max-k", type=int, default=9)
    parser.add_argument("--support-power", type=float, default=7.0)
    parser.add_argument("--buchstab-loss", type=float, default=2.0)
    parser.add_argument("--selector-retention-loss", type=float, default=1.0)
    parser.add_argument("--required-loss", type=float, default=3.0)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        args.squarefree_json,
        args.min_k,
        args.max_k,
        args.support_power,
        args.buchstab_loss,
        args.selector_retention_loss,
        args.required_loss,
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
