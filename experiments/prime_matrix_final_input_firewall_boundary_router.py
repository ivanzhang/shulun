#!/usr/bin/env python3
"""汇总行列命题最终输入防火墙边界。

用法示例：
  python3 experiments/prime_matrix_final_input_firewall_boundary_router.py

输出：
  docs/monograph/prime-matrix-final-input-firewall-boundary-router.json
  docs/monograph/prime-matrix-final-input-firewall-boundary-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PDEC = DOCS / "prime-matrix-pdec-family-explicit-input-boundary-router.json"
DEFAULT_SPARSE = DOCS / "prime-matrix-future-sparse-packet-extractor-schema-boundary-router.json"
DEFAULT_NONCANONICAL = DOCS / "prime-matrix-noncanonical-complement-trilemma-router.json"
DEFAULT_DSTRUCTURE = DOCS / "prime-matrix-dstructure-rankin-promotion-acceptance-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-final-input-firewall-boundary-router.json"
DEFAULT_MD = DOCS / "prime-matrix-final-input-firewall-boundary-router.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算文件 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: bool) -> str:
    """把布尔值输出成小写文本。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(
    gate: str,
    boundary_closed: bool,
    independently_accepted: bool,
    evidence: str,
    consequence: str,
    remaining: str,
) -> dict[str, Any]:
    """构造最终输入防火墙表格行。"""
    return {
        "gate": gate,
        "boundary_closed": boundary_closed,
        "independently_accepted": independently_accepted,
        "evidence": evidence,
        "consequence": consequence,
        "remaining": remaining,
    }


def build_rows(
    pdec: dict[str, Any],
    sparse: dict[str, Any],
    noncanonical: dict[str, Any],
    dstructure: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成最终输入防火墙审查表。"""
    pdec_boundary = (
        pdec.get("pdec_family_explicit_input_boundary_closed") is True
        and pdec.get("current_materialized_pdec_frontier_closed") is True
        and pdec.get("global_pdec_family_unconditional_closed") is False
    )
    sparse_boundary = (
        sparse.get("future_sparse_packet_schema_boundary_closed") is True
        and sparse.get("current_materialized_sparse_frontier_closed") is True
        and sparse.get("global_sparse_family_unconditional_closed") is False
    )
    noncanonical_boundary = (
        noncanonical.get("trilemma_boundary_closed") is True
        and noncanonical.get("self_contained_noncanonical_package_closed") is False
        and noncanonical.get("external_contract_package_closed_if_fulls_kls_ext_accepted")
        is True
    )
    dstructure_boundary = (
        dstructure.get("promotion_package_boundary_closed") is True
        and dstructure.get("promotion_package_independently_accepted") is False
    )
    no_hidden_terminal = pdec_boundary and sparse_boundary and noncanonical_boundary and dstructure_boundary

    return [
        row(
            gate="FirstPackagePDECExplicitSchemaFirewall",
            boundary_closed=pdec_boundary,
            independently_accepted=False,
            evidence="PDEC family explicit input boundary router",
            consequence="当前已物化 PDEC 前沿清零；未来 PDEC 不能作为泛称终端进入。",
            remaining="FutureExplicitPrimitivePDECSchema if a new PDEC family is proposed",
        ),
        row(
            gate="FirstPackageSparseExtractorSchemaFirewall",
            boundary_closed=sparse_boundary,
            independently_accepted=False,
            evidence="future sparse packet extractor schema boundary router",
            consequence="当前已物化 sparse/LocalSurvivor 前沿清零；未来 sparse 必须给有限 extractor schema。",
            remaining="FutureExplicitSparsePacketExtractorSchema if a new sparse route is proposed",
        ),
        row(
            gate="SecondPackageNoncanonicalTrilemmaFirewall",
            boundary_closed=noncanonical_boundary,
            independently_accepted=False,
            evidence="noncanonical complement trilemma router",
            consequence="generic 自足反原子被排除；noncanonical 分支只能走实际源恒等、强化实际源反原子或 FullS-KLS-ext。",
            remaining="choose and prove/accept one legal noncanonical closure mode",
        ),
        row(
            gate="ThirdPackageDStructureRankinPromotionFirewall",
            boundary_closed=dstructure_boundary,
            independently_accepted=False,
            evidence="DStructure/Rankin promotion acceptance router",
            consequence="最终晋级门已命名为 D-structure/Tail-log4/finite Rankin 独立验收包。",
            remaining="independent acceptance of the promotion package",
        ),
        row(
            gate="NoHiddenTerminalAfterFirewall",
            boundary_closed=no_hidden_terminal,
            independently_accepted=False,
            evidence="four firewall inputs",
            consequence="当前材料中没有未命名终端可继续偷渡；每个剩余必须以显式 schema 或外部验收进入。",
            remaining="named inputs still open; not a final unconditional theorem",
        ),
    ]


def run(
    pdec_path: Path,
    sparse_path: Path,
    noncanonical_path: Path,
    dstructure_path: Path,
    json_out: Path,
    md_out: Path,
) -> dict[str, Any]:
    """执行最终输入防火墙边界路由。"""
    pdec = load_json(pdec_path)
    sparse = load_json(sparse_path)
    noncanonical = load_json(noncanonical_path)
    dstructure = load_json(dstructure_path)

    rows = build_rows(pdec, sparse, noncanonical, dstructure)
    firewall_boundary_closed = all(item["boundary_closed"] for item in rows)
    all_inputs_accepted = all(item["independently_accepted"] for item in rows)
    current_materialized_frontier_closed = (
        pdec.get("current_materialized_pdec_frontier_closed") is True
        and sparse.get("current_materialized_sparse_frontier_closed") is True
    )

    final_open_inputs = [
        "FutureExplicitPrimitivePDECSchema：若未来新增 PDEC family，必须提交同 formal unit、三物理原子以上、二秩以上、cap-stable schema",
        "FutureExplicitSparsePacketExtractorSchema：若未来新增 sparse route，必须提交有限 packet extractor schema",
        "NoncanonicalFullSComplementTrilemma：证明实际源恒等、强化实际源反原子，或接受/证明 FullS-KLS-ext",
        "DStructureRankinPromotion：D-structure/Tail-log4/finite Rankin 晋级包必须独立接受",
    ]

    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_final_input_firewall_boundary_router",
        "status": "final_input_firewall_boundary_closed_current_frontier_zero_final_inputs_open",
        "firewall_law": (
            "当前已物化 PDEC 与 sparse/LocalSurvivor 前沿均已清零，且 noncanonical 与最终晋级门已压成命名输入。"
            "因此剩余不能再作为无名终端或口头硬点进入；必须以四类显式输入之一提交。"
            "但这些输入并未全部独立证明或接受，所以完整行/列无条件定理仍未闭合。"
        ),
        "final_input_firewall_boundary_closed": firewall_boundary_closed,
        "current_materialized_terminal_frontier_closed": current_materialized_frontier_closed,
        "all_final_inputs_independently_accepted": all_inputs_accepted,
        "row_column_unconditional_closed": False,
        "no_hidden_terminal_remaining": firewall_boundary_closed,
        "final_open_inputs": final_open_inputs,
        "review_conclusion": (
            "最终输入防火墙边界已闭合：当前材料没有剩余已物化 PDEC 或 sparse 终端，"
            "noncanonical 分支和 DStructure/Rankin 晋级门也已命名。"
            "最终定理尚未闭合，因为四类输入中至少 noncanonical 合法闭合模式与 DStructure/Rankin 独立接受仍未完成；"
            "未来 PDEC/sparse 新路线也必须先提交显式 schema。"
        ),
        "rows": rows,
        "source_hashes": {
            str(path.relative_to(ROOT)): file_sha256(path)
            for path in [pdec_path, sparse_path, noncanonical_path, dstructure_path]
        },
    }

    json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, md_out)
    return result


def write_markdown(result: dict[str, Any], md_out: Path) -> None:
    """写出 Markdown 审查报告。"""
    lines: list[str] = [
        "# Prime Matrix 最终输入防火墙边界路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 防火墙律",
        "",
        result["firewall_law"],
        "",
        "```text",
        f"final_input_firewall_boundary_closed={fmt_bool(result['final_input_firewall_boundary_closed'])}",
        f"current_materialized_terminal_frontier_closed={fmt_bool(result['current_materialized_terminal_frontier_closed'])}",
        f"all_final_inputs_independently_accepted={fmt_bool(result['all_final_inputs_independently_accepted'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"no_hidden_terminal_remaining={fmt_bool(result['no_hidden_terminal_remaining'])}",
        "```",
        "",
        "## 2. 审查表",
        "",
        "| gate | boundary_closed | independently_accepted | evidence | consequence | remaining |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for item in result["rows"]:
        lines.append(
            "| `{gate}` | `{boundary_closed}` | `{accepted}` | {evidence} | {consequence} | {remaining} |".format(
                gate=table_cell(item["gate"]),
                boundary_closed=fmt_bool(item["boundary_closed"]),
                accepted=fmt_bool(item["independently_accepted"]),
                evidence=table_cell(item["evidence"]),
                consequence=table_cell(item["consequence"]),
                remaining=table_cell(item["remaining"]),
            )
        )

    lines.extend(
        [
            "",
            "## 3. 最终开放输入",
            "",
        ]
    )
    lines.extend(f"- `{item}`" for item in result["final_open_inputs"])
    lines.extend(
        [
            "",
            "## 4. 判定",
            "",
            (
                "这一步闭合的是边界和命名性：没有隐藏终端剩余。"
                "它不闭合最终无条件定理，因为显式输入仍未全部证明或独立接受。"
            ),
            "",
        ]
    )
    md_out.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pdec", type=Path, default=DEFAULT_PDEC)
    parser.add_argument("--sparse", type=Path, default=DEFAULT_SPARSE)
    parser.add_argument("--noncanonical", type=Path, default=DEFAULT_NONCANONICAL)
    parser.add_argument("--dstructure", type=Path, default=DEFAULT_DSTRUCTURE)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    result = run(
        pdec_path=args.pdec,
        sparse_path=args.sparse,
        noncanonical_path=args.noncanonical,
        dstructure_path=args.dstructure,
        json_out=args.json_out,
        md_out=args.md_out,
    )
    print(result["status"])
    print(result["final_open_inputs"])


if __name__ == "__main__":
    main()
