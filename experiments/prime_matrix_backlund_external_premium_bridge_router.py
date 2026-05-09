#!/usr/bin/env python3
"""Prime Matrix Backlund 外部对称 max 溢价桥路由器。

用法示例：
  python3 experiments/prime_matrix_backlund_external_premium_bridge_router.py

输出：
  docs/monograph/prime-matrix-backlund-external-premium-bridge-router.json
  docs/monograph/prime-matrix-backlund-external-premium-bridge-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONO = ROOT / "docs" / "monograph"

DEFAULT_PREMIUM = MONO / "prime-matrix-backlund-symmetric-max-premium-router.json"
DEFAULT_MERGE = MONO / "prime-matrix-backlund-internal-external-merge-router.json"
DEFAULT_DSTRUCTURE = MONO / "prime-matrix-dstructure-rankin-promotion-acceptance-router.json"
DEFAULT_EXTERNAL_INDEX = MONO / "external-theorem-index.md"
DEFAULT_JSON = MONO / "prime-matrix-backlund-external-premium-bridge-router.json"
DEFAULT_MD = MONO / "prime-matrix-backlund-external-premium-bridge-router.md"

PREMIUM = "BacklundSymmetricHeightMaxPremiumBelowC16MarginLedger"
EXTERNAL_ACCEPTED = "ClassicalBacklundZeroIndentationCostExternalAccepted"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证据。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_rows(premium: dict[str, Any], merge: dict[str, Any], dstructure: dict[str, Any], index_text: str) -> list[dict[str, Any]]:
    """生成外部溢价桥判定表。"""
    guard = (
        premium.get("counterexample_assumption_only") is True
        and premium.get("empirical_absence_not_used") is True
        and premium.get("hypothetical_chain_only") is True
    )
    premium_open = premium.get("new_unique_internal_remaining") == PREMIUM
    index_registered = PREMIUM in index_text and EXTERNAL_ACCEPTED in index_text
    external_package_merged = merge.get("external_analytic_backlund_package_merged") is True
    dstructure_accepted = dstructure.get("promotion_package_independently_accepted") is True
    return [
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "外部桥仍只处理假设链条的解析 Backlund 输入，不使用真实零行缺席。",
            "保持自足/外部链分离。",
        ),
        row(
            "SymmetricMaxPremiumIsExactInternalRemaining",
            premium_open,
            True,
            "严格自足内部化已压到对称高度 max 溢价微输入。",
            PREMIUM,
        ),
        row(
            "ExternalIndexRegistersPremiumMicroInput",
            index_registered,
            False,
            "外部索引已把经典 Backlund 引理精确对接到该微输入。",
            "external theorem acceptance",
        ),
        row(
            "ExternalBacklundClosesPremiumBridge",
            index_registered,
            False,
            "接受经典 Backlund 外部引理时，该对称 max/高幂 Jensen 常数包作为外部输入关闭。",
            EXTERNAL_ACCEPTED,
        ),
        row(
            "ExternalBacklundAnalyticPackageMerged",
            external_package_merged,
            False,
            "外部 Backlund 包已能接上 CS8、端点 convention 与 RVM->CN16。",
            DSTRUCTURE,
        ),
        row(
            "StrictSelfContainedBacklundClosed",
            False,
            False,
            "作者侧仍未在文内证明对称 max 溢价不等式，所以严格自足 Backlund 未闭合。",
            PREMIUM,
        ),
        row(
            "DStructureRankinIndependentlyAccepted",
            dstructure_accepted,
            False,
            "即使外部 Backlund 接受，最终行/列命题仍需 DStructure/Rankin 独立验收。",
            DSTRUCTURE,
        ),
        row(
            "RowColumnExternalRouteClosed",
            False,
            False,
            "外部 Backlund 只关闭解析 Backlund 包；DStructure/Rankin 未接受前全局外部路线仍未闭合。",
            DSTRUCTURE,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行外部溢价桥路由。"""
    premium = load_json(paths["premium"])
    merge = load_json(paths["merge"])
    dstructure = load_json(paths["dstructure"])
    index_text = paths["external_index"].read_text(encoding="utf-8")
    rows = build_rows(premium, merge, dstructure, index_text)
    source_paths = [path for name, path in paths.items() if name not in {"json_out", "md_out"}]
    return {
        "certificate_type": "prime_matrix_backlund_external_premium_bridge_router",
        "status": "external_backlund_closes_symmetric_max_premium_dstructure_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "strict_internal_remaining": PREMIUM,
        "external_backlund_input": EXTERNAL_ACCEPTED,
        "external_backlund_closes_premium": True,
        "strict_self_contained_backlund_closed": False,
        "external_backlund_package_merged": True,
        "dstructure_rankin_independent_acceptance_completed": False,
        "row_column_external_route_closed": False,
        "plain_conclusion": (
            "外部 Backlund 引理现在已精确对接到内部化后的最终微输入 "
            "`BacklundSymmetricHeightMaxPremiumBelowC16MarginLedger`。"
            "接受该外部输入可关闭解析 Backlund 包，并接上 CS8、端点 convention、RVM->CN16；"
            "但严格自足版仍未证明该溢价不等式，且全局外部路线仍需 DStructure/Rankin 独立验收。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix Backlund 外部对称 max 溢价桥路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"strict_internal_remaining={result['strict_internal_remaining']}",
        f"external_backlund_input={result['external_backlund_input']}",
        f"external_backlund_closes_premium={fmt_bool(result['external_backlund_closes_premium'])}",
        f"strict_self_contained_backlund_closed={fmt_bool(result['strict_self_contained_backlund_closed'])}",
        f"external_backlund_package_merged={fmt_bool(result['external_backlund_package_merged'])}",
        f"dstructure_rankin_independent_acceptance_completed={fmt_bool(result['dstructure_rankin_independent_acceptance_completed'])}",
        f"row_column_external_route_closed={fmt_bool(result['row_column_external_route_closed'])}",
        "```",
        "",
        "## 1. 精确对接链",
        "",
        "```text",
        "BacklundSymmetricHeightMaxPremiumBelowC16MarginLedger",
        "  => BacklundHighPowerAuxiliarySignedMeanC16AggregationLedger",
        "  => BacklundAuxiliaryRealPartJensenC16ConstantAggregationLedger",
        "  => ClassicalBacklundZeroIndentationCostInternalProofLedger",
        "",
        "ClassicalBacklundZeroIndentationCostExternalAccepted",
        "  closes the same premium package externally.",
        "```",
        "",
        "## 2. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=table_cell(item["gate"]),
                closed=fmt_bool(item["closed"]),
                proved=fmt_bool(item["proved"]),
                meaning=table_cell(item["meaning"]),
                remaining=table_cell(item["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 3. 下一步",
            "",
            "若坚持严格自足：继续证明 `BacklundSymmetricHeightMaxPremiumBelowC16MarginLedger`。",
            "若走外部路线：Backlund 解析包可接受，但仍需 `DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--premium-json", type=Path, default=DEFAULT_PREMIUM)
    parser.add_argument("--merge-json", type=Path, default=DEFAULT_MERGE)
    parser.add_argument("--dstructure-json", type=Path, default=DEFAULT_DSTRUCTURE)
    parser.add_argument("--external-index", type=Path, default=DEFAULT_EXTERNAL_INDEX)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "premium": args.premium_json,
        "merge": args.merge_json,
        "dstructure": args.dstructure_json,
        "external_index": args.external_index,
        "json_out": args.json_out,
        "md_out": args.md_out,
    }
    result = run(paths)
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(result["status"])
    print(result["strict_internal_remaining"])


if __name__ == "__main__":
    main()
