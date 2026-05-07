#!/usr/bin/env python3
"""硬攻 CanonicalSelectorRetentionOrCleanReturn 的有限签名保留机制。

用法示例：
  python3 experiments/prime_matrix_triad_a1_selector_retention_router.py
  python3 experiments/prime_matrix_triad_a1_selector_retention_router.py --signature-count-power 0.75

输出：
  docs/monograph/prime-matrix-triad-a1-selector-retention-router.json
  docs/monograph/prime-matrix-triad-a1-selector-retention-router.md
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
DEFAULT_LAYER_TRANSFER = DOCS / "prime-matrix-triad-a1-layer-transfer-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-selector-retention-router.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-selector-retention-router.md"


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


def signature_row(
    k: int,
    support_power: float,
    buchstab_loss: float,
    signature_count_power: float,
    required_loss: float,
) -> dict[str, Any]:
    """生成有限签名 pigeonhole 保留率阈值行。"""
    y = 10**k
    log_y = math.log(y)
    interval_size = log_y**support_power
    raw_support = interval_size / (log_y**buchstab_loss)
    signature_count = log_y**signature_count_power
    max_signature_support_lower = raw_support / signature_count
    required_support = interval_size / (log_y**required_loss)
    signature_retention_suffices = max_signature_support_lower >= required_support
    max_allowed_signature_power = required_loss - buchstab_loss
    return {
        "k": k,
        "y": y,
        "log_y": log_y,
        "support_power_B": support_power,
        "buchstab_loss_power_E": buchstab_loss,
        "signature_count_power_J": signature_count_power,
        "required_loss_power_C": required_loss,
        "max_allowed_signature_power_C_minus_E": max_allowed_signature_power,
        "model_interval_size": interval_size,
        "raw_support": raw_support,
        "signature_count": signature_count,
        "max_signature_support_lower": max_signature_support_lower,
        "required_support": required_support,
        "signature_retention_suffices": signature_retention_suffices,
    }


def build_gate_rows() -> list[dict[str, Any]]:
    """列出 finite-signature selector 保留的门控。"""
    return [
        {
            "gate": "FiniteSignaturePartition",
            "available": "K6/tail-label bookkeeping gives polylog-many dyadic labels",
            "needed": "raw thick Buchstab support is partitioned into <= log^J exact selector signatures",
            "gap": "polylog labels are known abstractly, but not yet tied to exact RIW coefficient paths",
            "route": "define RIW path signature including parity, dyadic bin and truncation state",
            "closed": False,
        },
        {
            "gate": "MaxSignatureRetention",
            "available": "finite partition once the previous gate is fixed",
            "needed": "one canonical signature retains at least raw_support/log^J",
            "gap": "none after finite partition; this is pigeonhole",
            "route": "choose canonical maximal signature with deterministic tie-break",
            "closed": True,
        },
        {
            "gate": "UniquePathNoCancellation",
            "available": "Buchstab recursion suggests a decision-tree decomposition",
            "needed": "one product belongs to one selected path or same-path coefficient is nonzero",
            "gap": "without unique path, different signed paths could cancel the same product",
            "route": "prove path signatures are disjoint, or refine signature until disjoint",
            "closed": False,
        },
        {
            "gate": "SelectorRetentionCleanReturn",
            "available": "edge/PDEC/SAE exits exist",
            "needed": "if finite signature retention or unique-path noncancellation fails, block exits clean A1",
            "gap": "this contrapositive clean contract is not yet recorded",
            "route": "low-retention or multi-path cancellation must be named as tail-label/PDEC failure",
            "closed": False,
        },
        {
            "gate": "FiniteSignatureImpliesSelectorRetention",
            "available": "max-signature pigeonhole plus no-cancellation",
            "needed": "retained nonzero support >= interval/log^C",
            "gap": "conditional implication is direct; finite partition/no-cancellation/return remain",
            "route": "combine finite signatures with E+J<=C",
            "closed": True,
        },
    ]


def run(
    layer_transfer_path: Path,
    min_k: int,
    max_k: int,
    support_power: float,
    buchstab_loss: float,
    signature_count_power: float,
    required_loss: float,
) -> dict[str, Any]:
    """运行 selector 保留率路由。"""
    layer_transfer = load_json(layer_transfer_path)
    rows = [
        signature_row(
            k,
            support_power,
            buchstab_loss,
            signature_count_power,
            required_loss,
        )
        for k in range(min_k, max_k + 1)
    ]
    all_signature_rows_suffice = all(row["signature_retention_suffices"] for row in rows)
    return {
        "certificate_type": "triad_a1_selector_retention_router",
        "status": "selector_retention_reduced_to_finite_signature_no_cancellation_or_clean_return",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "layer_transfer_json": file_sha256(layer_transfer_path),
        },
        "parameters": {
            "min_k": min_k,
            "max_k": max_k,
            "support_power_B": support_power,
            "buchstab_loss_power_E": buchstab_loss,
            "signature_count_power_J": signature_count_power,
            "required_loss_power_C": required_loss,
            "scale": "y=10^k",
        },
        "layer_transfer_input_status": layer_transfer["status"],
        "layer_transfer_input_next_target": layer_transfer["next_internal_target"],
        "gate_rows": build_gate_rows(),
        "rows": rows,
        "all_signature_rows_suffice": all_signature_rows_suffice,
        "finite_signature_partition_closed": False,
        "unique_path_no_cancellation_closed": False,
        "selector_retention_clean_return_closed": False,
        "selector_retention_closed": False,
        "conditional_finite_signature_implies_selector_retention": True,
        "reduction_law": (
            "Selector retention can be proved by a finite-signature pigeonhole principle, not by "
            "new density estimates. If the raw thick Buchstab support is partitioned into at most "
            "log^J exact RIW path signatures, then the maximal signature retains at least a "
            "log^-J fraction. This is enough whenever the Buchstab loss E plus signature loss J "
            "does not exceed the support budget C. The remaining exact obstruction is no-cancellation "
            "of selected paths and the clean-return contract for failures."
        ),
        "next_internal_target": "FiniteSignatureNoCancellationOrCleanReturn",
        "terminal_gap_after_router": (
            "FiniteSignatureNoCancellationOrCleanReturnOrExternalDIBFIOriginalDispersion"
        ),
        "review_conclusion": (
            "CanonicalSelectorRetention 已被压成有限签名 pigeonhole：若 exact RIW/Buchstab "
            "路径签名数只有 log^J 个，则最大签名自动保留 log-power 支撑。真正剩余是把 K6 "
            "有限标签严格提升为 exact coefficient path partition，并证明所选路径无抵消；"
            "失败时必须回到 clean 退出口。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 Canonical Selector Retention 路由审计",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 有限签名保留律",
        "",
        result["reduction_law"],
        "",
        "```text",
        "raw support S is partitioned into at most log^J exact signatures;",
        "max signature support >= S/log^J;",
        "if raw S >= interval/log^E and E+J<=C:",
        "  retained support >= interval/log^C;",
        "remaining issue: unique path/no cancellation, or clean return.",
        "```",
        "",
        "## 2. 汇总",
        "",
        f"- `layer_transfer_input_status={result['layer_transfer_input_status']}`。",
        f"- `layer_transfer_input_next_target={result['layer_transfer_input_next_target']}`。",
        f"- `all_signature_rows_suffice={result['all_signature_rows_suffice']}`。",
        f"- `conditional_finite_signature_implies_selector_retention={result['conditional_finite_signature_implies_selector_retention']}`。",
        f"- `selector_retention_closed={result['selector_retention_closed']}`。",
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
            "## 4. 签名保留模型",
            "",
            "| k | log y | raw support | signature count | max signature support | required support | suffices |",
            "| ---: | ---: | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for row in result["rows"]:
        lines.append(
            "| {k} | {logy} | {raw} | {count} | {maxsig} | {required} | `{suffices}` |".format(
                k=row["k"],
                logy=fmt_float(row["log_y"]),
                raw=fmt_float(row["raw_support"]),
                count=fmt_float(row["signature_count"]),
                maxsig=fmt_float(row["max_signature_support_lower"]),
                required=fmt_float(row["required_support"]),
                suffices=row["signature_retention_suffices"],
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
            "FiniteSignatureNoCancellationOrCleanReturn:",
            "  promote K6/polylog labels to an exact RIW path-signature partition;",
            "  prove selected path signatures are disjoint or non-cancelling;",
            "  otherwise return the failed block to edge/PDEC/SAE.",
            "```",
            "",
            "这一步把 selector retention 的数量问题化为有限签名 pigeonhole；剩余是 exact "
            "路径分割与无抵消的结构合同。",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--layer-transfer-json", type=Path, default=DEFAULT_LAYER_TRANSFER)
    parser.add_argument("--min-k", type=int, default=3)
    parser.add_argument("--max-k", type=int, default=9)
    parser.add_argument("--support-power", type=float, default=7.0)
    parser.add_argument("--buchstab-loss", type=float, default=2.0)
    parser.add_argument("--signature-count-power", type=float, default=1.0)
    parser.add_argument("--required-loss", type=float, default=3.0)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        args.layer_transfer_json,
        args.min_k,
        args.max_k,
        args.support_power,
        args.buchstab_loss,
        args.signature_count_power,
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
