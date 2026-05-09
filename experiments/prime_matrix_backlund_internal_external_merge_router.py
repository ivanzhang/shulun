#!/usr/bin/env python3
"""Prime Matrix Backlund 内部主攻与外部合并路由器。

用法示例：
  python3 experiments/prime_matrix_backlund_internal_external_merge_router.py

输出：
  docs/monograph/prime-matrix-backlund-internal-external-merge-router.json
  docs/monograph/prime-matrix-backlund-internal-external-merge-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONO = ROOT / "docs" / "monograph"

DEFAULT_FINAL = MONO / "prime-matrix-backlund-final-branch-status-router.json"
DEFAULT_INDENT = MONO / "prime-matrix-b3-zero-proximity-indentation-cost-router.json"
DEFAULT_CS8 = MONO / "prime-matrix-b3-cs8-slack-router.json"
DEFAULT_ENDPOINT = MONO / "prime-matrix-b3-endpoint-multiplicity-convention-router.json"
DEFAULT_RVM = MONO / "prime-matrix-b3-rvm-to-cn16-local-inequality-router.json"
DEFAULT_DSTRUCTURE = MONO / "prime-matrix-dstructure-rankin-promotion-acceptance-router.json"
DEFAULT_INTERNAL = MONO / "prime-matrix-backlund-internal-proof-obligation-router.json"
DEFAULT_EXTERNAL_INDEX = MONO / "external-theorem-index.md"
DEFAULT_JSON = MONO / "prime-matrix-backlund-internal-external-merge-router.json"
DEFAULT_MD = MONO / "prime-matrix-backlund-internal-external-merge-router.md"

INTERNAL_PROOF = "ClassicalBacklundZeroIndentationCostInternalProofLedger"
EXTERNAL_ACCEPTED = "ClassicalBacklundZeroIndentationCostExternalAccepted"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证据。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算证据文件哈希。"""
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


def external_sources() -> list[dict[str, str]]:
    """外部 Backlund 引理的引用来源。"""
    return [
        {
            "source": "Trudgian 2012",
            "url": "https://doi.org/10.1090/S0025-5718-2011-02537-8",
            "role": "Backlund/Rosser--McCurley 轮廓方法给出 arg zeta/S(t) 的显式上界。",
        },
        {
            "source": "Trudgian 2014 arXiv:1208.5846",
            "url": "https://arxiv.org/abs/1208.5846",
            "role": "现代显式 Backlund 方法与 S(T) 零点处理 convention 的引用入口。",
        },
    ]


def internal_target_obligations() -> list[dict[str, str]]:
    """内部重证经典缩进引理的集中目标。"""
    return [
        {
            "obligation": "ClassicalContourIndentationProof",
            "content": "从局部避零轮廓直接证明近零缩进项被同一 Backlund 轮廓恒等式吸收。",
        },
        {
            "obligation": "EndpointAndMultiplicityLimit",
            "content": "端点落零先避开再取极限，零点按解析重数登记，且不新增 C_S 常数。",
        },
        {
            "obligation": "BudgetPreservingJumpLedger",
            "content": "证明局部 jump 不作为额外正比例成本进入 C_S=8；这是内部证明的核心。",
        },
        {
            "obligation": "NoDetourDiscipline",
            "content": "不再走权重吸收、镜像抵消、胶囊密度、小半径 anchor 或 RVM 反调用。",
        },
    ]


def build_rows(
    final: dict[str, Any],
    indent: dict[str, Any],
    cs8: dict[str, Any],
    endpoint: dict[str, Any],
    rvm: dict[str, Any],
    dstructure: dict[str, Any],
    internal: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成内部外部合并判定表。"""
    guard = (
        final.get("counterexample_assumption_only") is True
        and final.get("empirical_absence_not_used") is True
        and final.get("hypothetical_chain_only") is True
    )
    internal_open = internal.get("strict_self_contained_unique_remaining") == INTERNAL_PROOF
    external_indent_available = indent.get("zero_proximity_indentation_cost_external_closed") is True
    cs8_closed = cs8.get("backlund_cs8_slack_external_closed") is True
    endpoint_closed = endpoint.get("endpoint_multiplicity_convention_closed") is True
    rvm_closed = rvm.get("rvm_to_cn16_external_closed") is True
    dstructure_boundary = "DStructureRankinBoundaryClosed" in final.get("closed_gates", []) or (
        dstructure.get("promotion_package_boundary_closed") is True
    )
    dstructure_accepted = dstructure.get("promotion_package_independently_accepted") is True
    return [
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "合并仍只处理假设链条中的解析输入，不使用真实零行缺席。",
            "保持自足与外部两条链分离。",
        ),
        row(
            "InternalBacklundTargetLocked",
            internal_open,
            True,
            "内部路线集中攻经典 Backlund 零点缩进成本内部证明，不再转移目标。",
            INTERNAL_PROOF,
        ),
        row(
            "ExternalBacklundIndentAcceptedForRoute",
            external_indent_available,
            False,
            "外部路线把经典 Backlund 缩进处理作为引用输入接入。",
            EXTERNAL_ACCEPTED,
        ),
        row(
            "ExternalBacklundDownstreamCS8Closed",
            cs8_closed,
            True,
            "接受外部缩进输入后，C_S=8 紧等号验收已闭合。",
            "BacklundCS8SlackAfterBridgeClosedTightHalf",
        ),
        row(
            "ExternalEndpointConventionClosed",
            endpoint_closed,
            True,
            "端点避零与重数极限 convention 已闭合。",
            "EndpointZeroAvoidanceMultiplicityConventionClosedByLimit",
        ),
        row(
            "ExternalRVMToCN16Closed",
            rvm_closed,
            True,
            "原始 arg zeta 归一化下，RVM 到 C_N=16 合并已闭合。",
            "RVMToCN16LocalInequalityClosedWithRawArgCS8",
        ),
        row(
            "ExternalAnalyticBacklundPackageMerged",
            external_indent_available and cs8_closed and endpoint_closed and rvm_closed,
            False,
            "外部 Backlund 解析包已合并到最终晋级门前。",
            DSTRUCTURE,
        ),
        row(
            "DStructureRankinBoundaryClosed",
            dstructure_boundary,
            True,
            "DStructure/Tail-log4/finite Rankin 的验收边界已列清。",
            "independent acceptance",
        ),
        row(
            "DStructureRankinIndependentlyAccepted",
            dstructure_accepted,
            False,
            "该门仍需独立审稿/复现接受，作者侧不能自审关闭。",
            DSTRUCTURE,
        ),
        row(
            "RowColumnExternalRouteClosed",
            False,
            False,
            "外部 Backlund 包合并后仍缺 DStructure/Rankin 独立接受。",
            DSTRUCTURE,
        ),
        row(
            "RowColumnSelfContainedClosed",
            False,
            False,
            "内部经典 Backlund 缩进成本尚未作者侧重证。",
            INTERNAL_PROOF,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行内部外部合并路由。"""
    final = load_json(paths["final"])
    indent = load_json(paths["indent"])
    cs8 = load_json(paths["cs8"])
    endpoint = load_json(paths["endpoint"])
    rvm = load_json(paths["rvm"])
    dstructure = load_json(paths["dstructure"])
    internal = load_json(paths["internal"])
    rows = build_rows(final, indent, cs8, endpoint, rvm, dstructure, internal)
    source_paths = [path for name, path in paths.items() if name not in {"json_out", "md_out"}]
    external_merged = next(item["closed"] for item in rows if item["gate"] == "ExternalAnalyticBacklundPackageMerged")
    return {
        "certificate_type": "prime_matrix_backlund_internal_external_merge_router",
        "status": "backlund_external_analytic_package_merged_dstructure_open_internal_backlund_target_locked",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "internal_primary_target": INTERNAL_PROOF,
        "external_backlund_input": EXTERNAL_ACCEPTED,
        "external_theorem_index": str(paths["external_index"].relative_to(ROOT)),
        "external_analytic_backlund_package_merged": external_merged,
        "dstructure_rankin_independent_acceptance_completed": False,
        "row_column_self_contained_closed": False,
        "row_column_external_route_closed": False,
        "external_sources": external_sources(),
        "internal_target_obligations": internal_target_obligations(),
        "plain_conclusion": (
            "内部路线现在集中攻 `ClassicalBacklundZeroIndentationCostInternalProofLedger`。"
            "外部路线把经典 Backlund/Rosser-McCurley/Trudgian 缩进处理作为引用输入接入后，"
            "CS8、端点 convention、RVM->CN16 已合并到最终晋级门前。"
            "但完整无条件闭合仍被 `DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance` 阻断，"
            "作者侧不能把该独立验收门自审关闭。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix Backlund 内部主攻与外部合并路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"internal_primary_target={result['internal_primary_target']}",
        f"external_backlund_input={result['external_backlund_input']}",
        f"external_theorem_index={result['external_theorem_index']}",
        f"external_analytic_backlund_package_merged={fmt_bool(result['external_analytic_backlund_package_merged'])}",
        (
            "dstructure_rankin_independent_acceptance_completed="
            f"{fmt_bool(result['dstructure_rankin_independent_acceptance_completed'])}"
        ),
        f"row_column_self_contained_closed={fmt_bool(result['row_column_self_contained_closed'])}",
        f"row_column_external_route_closed={fmt_bool(result['row_column_external_route_closed'])}",
        "```",
        "",
        "## 1. 外部 Backlund 输入",
        "",
        "| source | url | role |",
        "| --- | --- | --- |",
    ]
    for item in result["external_sources"]:
        lines.append(f"| {table_cell(item['source'])} | {table_cell(item['url'])} | {table_cell(item['role'])} |")
    lines.extend(
        [
            "",
            "## 2. 内部主攻义务",
            "",
            "| obligation | content |",
            "| --- | --- |",
        ]
    )
    for item in result["internal_target_obligations"]:
        lines.append(f"| `{table_cell(item['obligation'])}` | {table_cell(item['content'])} |")
    lines.extend(
        [
            "",
            "## 3. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
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
            "## 4. 下一步",
            "",
            f"内部主攻：`{result['internal_primary_target']}`。",
            "外部路线下一门：`DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`。",
            "",
            "判定：外部 Backlund 解析包已合并到晋级门前；完整闭合仍需 DStructure/Rankin 独立验收或内部 Backlund 重证完成。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--final-json", type=Path, default=DEFAULT_FINAL)
    parser.add_argument("--indent-json", type=Path, default=DEFAULT_INDENT)
    parser.add_argument("--cs8-json", type=Path, default=DEFAULT_CS8)
    parser.add_argument("--endpoint-json", type=Path, default=DEFAULT_ENDPOINT)
    parser.add_argument("--rvm-json", type=Path, default=DEFAULT_RVM)
    parser.add_argument("--dstructure-json", type=Path, default=DEFAULT_DSTRUCTURE)
    parser.add_argument("--internal-json", type=Path, default=DEFAULT_INTERNAL)
    parser.add_argument("--external-index", type=Path, default=DEFAULT_EXTERNAL_INDEX)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "final": args.final_json,
        "indent": args.indent_json,
        "cs8": args.cs8_json,
        "endpoint": args.endpoint_json,
        "rvm": args.rvm_json,
        "dstructure": args.dstructure_json,
        "internal": args.internal_json,
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
    print(result["internal_primary_target"])


if __name__ == "__main__":
    main()
