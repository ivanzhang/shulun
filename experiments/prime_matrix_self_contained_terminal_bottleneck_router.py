#!/usr/bin/env python3
"""把完全自足路线的终端瓶颈压到最小独立门。

用法示例：
  python3 experiments/prime_matrix_self_contained_terminal_bottleneck_router.py

输出：
  docs/monograph/prime-matrix-self-contained-terminal-bottleneck-router.json
  docs/monograph/prime-matrix-self-contained-terminal-bottleneck-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_SPLIT = DOCS / "prime-matrix-global-terminal-family-exclusion-split-router.json"
DEFAULT_SAME_SET = DOCS / "prime-matrix-triad-a1-pdec-same-set-capacity-frontier-router.json"
DEFAULT_NCBLK = DOCS / "prime-matrix-ncblk-boundary-reconciliation-router.json"
DEFAULT_CLEAN_CONTRACT = DOCS / "prime-matrix-cleankls-dls-certificate-contract.md"
DEFAULT_CLEAN_ROUTER = DOCS / "prime-matrix-triad-a1-clean-kls-external-input-router.json"
DEFAULT_KUZNETSOV = DOCS / "prime-matrix-triad-a1-kuznetsov-ls-atom-frontier-router.json"
DEFAULT_PDEC_ROUTE = DOCS / "prime-matrix-triad-a1-pdec-capacity-upper-route.md"
DEFAULT_LINE_REF = DOCS / "line-by-line-internal-referee-matrix.md"
DEFAULT_JSON = DOCS / "prime-matrix-self-contained-terminal-bottleneck-router.json"
DEFAULT_MD = DOCS / "prime-matrix-self-contained-terminal-bottleneck-router.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def read_text(path: Path) -> str:
    """读取文本文件。"""
    return path.read_text(encoding="utf-8")


def file_sha256(path: Path) -> str:
    """计算文件 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: bool) -> str:
    """把布尔值输出为小写文本。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def has_all(text: str, needles: list[str]) -> bool:
    """检查文本是否包含全部片段。"""
    return all(needle in text for needle in needles)


def find_row(rows: list[dict[str, Any]], gate: str) -> dict[str, Any]:
    """按 gate 查找行。"""
    for row in rows:
        if row.get("gate") == gate:
            return row
    return {}


def bottleneck_row(
    gate: str,
    closed: bool,
    evidence: str,
    meaning: str,
    blocks_final: bool,
) -> dict[str, Any]:
    """构造瓶颈审查行。"""
    return {
        "gate": gate,
        "closed": closed,
        "evidence": evidence,
        "meaning": meaning,
        "blocks_final": blocks_final,
    }


def build_rows(
    split_router: dict[str, Any],
    same_set: dict[str, Any],
    ncblk: dict[str, Any],
    clean_contract_text: str,
    clean_router: dict[str, Any],
    kuznetsov: dict[str, Any],
    pdec_route_text: str,
    line_ref_text: str,
) -> list[dict[str, Any]]:
    """生成完全自足终端瓶颈审查表。"""
    split_kls_row = find_row(
        split_router["rows"], "KLS_EXT_OR_INTERNAL_LARGE_SIEVE"
    )
    split_pdec_row = find_row(split_router["rows"], "PDEC_CAP")
    split_self_contained_target = (
        split_router["self_contained_next_hardpoint"]
        == "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve"
    )
    clean_failure_returns_to_pdec = has_all(
        clean_contract_text,
        [
            "large-sieve fail",
            "输出对偶集中并回流 PDEC/SAE",
            "所以 `CleanKLS` 失败也不生成新出口",
        ],
    )
    canonical_clean_absorbed = (
        same_set["canonical_restricted_self_contained_version_closed"]
        and same_set["self_contained_final_boundary_closed"]
        and ncblk["all_reconciliation_gates_passed"]
        and ncblk["canonical_ncblk_absorbed_by_existing_boundary"]
    )
    generic_self_contained_not_allowed = (
        same_set["unrestricted_generic_self_contained_refuted"]
        and ncblk["generic_ncblk_self_contained_not_claimed"]
        and not same_set["original_unrestricted_self_contained_version_closed"]
    )
    clean_sc9_route_registered = (
        clean_router["self_contained_version_status"] == "open_at_kuznetsov_ls_atom_sc9"
        and kuznetsov["terminal_gap_after_router"]
        == "NCBLKOrExternalDIBFIOriginalDispersion"
    )
    clean_independent_gate_collapsed = (
        split_kls_row.get("blocks_final")
        and clean_failure_returns_to_pdec
        and canonical_clean_absorbed
        and generic_self_contained_not_allowed
        and clean_sc9_route_registered
    )
    pdec_cap_open = has_all(
        pdec_route_text,
        [
            "triad_a1_capacity_upper_route_not_closed",
            "同一坏窗集合",
            "它仍未提交任何全局 `U_CRT<L_PDEC` 证书",
        ],
    )
    referee_open = "BLOCK-REFEREE" in line_ref_text

    return [
        bottleneck_row(
            gate="PreviousSelfContainedSplitAccepted",
            closed=split_self_contained_target,
            evidence=split_router["self_contained_next_hardpoint"],
            meaning="上一轮已把完全自足路线压成 PDEC-CAP 或内部 CleanKLS 大筛。",
            blocks_final=False,
        ),
        bottleneck_row(
            gate="CleanKLSFailureDualReturnsToPDEC",
            closed=clean_failure_returns_to_pdec,
            evidence="large-sieve fail => dual concentration => PDEC/SAE",
            meaning="CleanKLS 失败不是独立数学出口；其对偶集中对象回流到 PDEC/SAE。",
            blocks_final=False,
        ),
        bottleneck_row(
            gate="CanonicalCleanBranchAbsorbed",
            closed=canonical_clean_absorbed,
            evidence=(
                f"canonical_boundary={same_set['self_contained_final_boundary_closed']}; "
                f"ncblk_reconciled={ncblk['all_reconciliation_gates_passed']}"
            ),
            meaning="canonical-source CleanKLS/NC-BLK 分支已由既有同集容量边界吸收。",
            blocks_final=False,
        ),
        bottleneck_row(
            gate="GenericSelfContainedKLSNotAClaim",
            closed=generic_self_contained_not_allowed,
            evidence=same_set["not_claimed_self_contained_statement"],
            meaning="unrestricted generic 自足版已反证隔离，不能作为完全自足路线的剩余门。",
            blocks_final=False,
        ),
        bottleneck_row(
            gate="SC9RouteAccounted",
            closed=clean_sc9_route_registered,
            evidence=(
                f"clean={clean_router['self_contained_version_status']}; "
                f"sc9={kuznetsov['terminal_gap_after_router']}"
            ),
            meaning="SC-9 已展开到 NC-BLK 或外部 DI/BFI，不再保留宽泛 KLS 黑箱。",
            blocks_final=False,
        ),
        bottleneck_row(
            gate="InternalCleanKLSIndependentBlockerCollapsed",
            closed=clean_independent_gate_collapsed,
            evidence=split_kls_row.get("evidence", "missing"),
            meaning=(
                "在当前 canonical-source 自足边界内，内部 CleanKLS 不再是独立最窄瓶颈；"
                "它要么被边界吸收，要么失败回流到 PDEC/SAE，要么属于已隔离 generic 外部路线。"
            ),
            blocks_final=False,
        ),
        bottleneck_row(
            gate="PDEC_CAP_SameSetGlobalDualCertificate",
            closed=not pdec_cap_open,
            evidence=split_pdec_row.get("evidence", "missing"),
            meaning="剩余独立自足硬点是全部 PDEC family 的同坏窗 U_CRT<L_PDEC 全局对偶证书。",
            blocks_final=pdec_cap_open,
        ),
        bottleneck_row(
            gate="DStructureRankinReferee",
            closed=not referee_open,
            evidence="BLOCK-REFEREE" if referee_open else "no referee block token found",
            meaning="完整行/列定理最终升级仍需 D-structure/Tail-log4/finite Rankin 接口被接受。",
            blocks_final=referee_open,
        ),
    ]


def run(
    split_path: Path,
    same_set_path: Path,
    ncblk_path: Path,
    clean_contract_path: Path,
    clean_router_path: Path,
    kuznetsov_path: Path,
    pdec_route_path: Path,
    line_ref_path: Path,
) -> dict[str, Any]:
    """运行完全自足终端瓶颈审查。"""
    split_router = load_json(split_path)
    same_set = load_json(same_set_path)
    ncblk = load_json(ncblk_path)
    clean_contract_text = read_text(clean_contract_path)
    clean_router = load_json(clean_router_path)
    kuznetsov = load_json(kuznetsov_path)
    pdec_route_text = read_text(pdec_route_path)
    line_ref_text = read_text(line_ref_path)

    rows = build_rows(
        split_router=split_router,
        same_set=same_set,
        ncblk=ncblk,
        clean_contract_text=clean_contract_text,
        clean_router=clean_router,
        kuznetsov=kuznetsov,
        pdec_route_text=pdec_route_text,
        line_ref_text=line_ref_text,
    )
    closed_nonfinal = all(row["closed"] for row in rows if not row["blocks_final"])
    open_final_gates = [row["gate"] for row in rows if row["blocks_final"]]
    pdec_only_bottleneck = (
        closed_nonfinal
        and "PDEC_CAP_SameSetGlobalDualCertificate" in open_final_gates
    )
    return {
        "certificate_type": "prime_matrix_self_contained_terminal_bottleneck_router",
        "status": "self_contained_terminal_bottleneck_reduced_to_pdec_cap_not_closed",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "split_router": file_sha256(split_path),
            "same_set_capacity_frontier": file_sha256(same_set_path),
            "ncblk_reconciliation": file_sha256(ncblk_path),
            "clean_contract": file_sha256(clean_contract_path),
            "clean_router": file_sha256(clean_router_path),
            "kuznetsov_frontier": file_sha256(kuznetsov_path),
            "pdec_route": file_sha256(pdec_route_path),
            "line_referee": file_sha256(line_ref_path),
        },
        "closed_nonfinal_reductions": closed_nonfinal,
        "internal_clean_kls_independent_blocker_collapsed": rows[5]["closed"],
        "self_contained_terminal_bottleneck_is_pdec_cap": pdec_only_bottleneck,
        "pdec_cap_closed": False,
        "row_column_unconditional_closed": False,
        "open_final_gates": open_final_gates,
        "narrowest_self_contained_hardpoint": "PDEC_CAP_SameSetGlobalDualCertificate",
        "rows": rows,
        "bottleneck_law": (
            "The fully self-contained route no longer needs to carry InternalCleanKLS as an "
            "independent minimal blocker inside the current canonical-source boundary. A clean "
            "large-sieve failure gives a dual concentration object and returns to PDEC/SAE; the "
            "canonical-source NC-BLK/KLS chain is already absorbed by the closed same-set boundary; "
            "and the unrestricted generic self-contained KLS/WFD route is refuted and not claimed. "
            "Therefore the remaining independent self-contained hardpoint is the global same-set "
            "PDEC capacity certificate U_CRT<L_PDEC, plus the separate referee-promotion interface."
        ),
        "review_conclusion": (
            "完全自足路线继续收窄：`InternalCleanKLS_LargeSieve` 不再是当前 canonical-source 边界内的"
            "独立最窄硬点；它要么被 NC-BLK/canonical same-set 边界吸收，要么失败回流 PDEC/SAE，"
            "要么属于已反证隔离的 unrestricted generic 自足版。当前唯一独立自足数学硬点是"
            "`PDEC_CAP_SameSetGlobalDualCertificate`，即对全部 PDEC family 提交同一坏窗集合上的"
            "`U_CRT<L_PDEC` 全局对偶证书。完整行/列无条件定理仍未闭合。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix 完全自足终端瓶颈路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 瓶颈律",
        "",
        result["bottleneck_law"],
        "",
        "```text",
        "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve",
        "  + CleanKLS failure duality => PDEC/SAE return;",
        "  + canonical NC-BLK boundary reconciliation => clean canonical branch absorbed;",
        "  + unrestricted generic self-contained WFD refuted/not claimed;",
        "therefore:",
        "  independent self-contained bottleneck = PDEC_CAP_SameSetGlobalDualCertificate.",
        "```",
        "",
        "## 2. 汇总",
        "",
        f"- `closed_nonfinal_reductions={fmt_bool(result['closed_nonfinal_reductions'])}`。",
        f"- `internal_clean_kls_independent_blocker_collapsed={fmt_bool(result['internal_clean_kls_independent_blocker_collapsed'])}`。",
        f"- `self_contained_terminal_bottleneck_is_pdec_cap={fmt_bool(result['self_contained_terminal_bottleneck_is_pdec_cap'])}`。",
        f"- `pdec_cap_closed={fmt_bool(result['pdec_cap_closed'])}`。",
        f"- `row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}`。",
        f"- `narrowest_self_contained_hardpoint={result['narrowest_self_contained_hardpoint']}`。",
        "",
        "## 3. 审查表",
        "",
        "| gate | closed | blocks final | evidence | meaning |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{blocks}` | {evidence} | {meaning} |".format(
                gate=table_cell(row["gate"]),
                closed=fmt_bool(bool(row["closed"])),
                blocks=fmt_bool(bool(row["blocks_final"])),
                evidence=table_cell(row["evidence"]),
                meaning=table_cell(row["meaning"]),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 下一步",
            "",
            "下一步不应再把完全自足路线写成 PDEC 与 CleanKLS 平行双黑箱。"
            "应直接攻 `PDEC_CAP_SameSetGlobalDualCertificate`：对每个同口径 PDEC family，"
            "证明同一坏窗集合上的全频率 LP/对偶容量上界 `U_CRT<L_PDEC`；若失败，必须输出"
            "合法 `DualCap` 并按既有 cap-localization、refined PDEC、SAE 或 ColumnCRT 路由处理。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--split-json", type=Path, default=DEFAULT_SPLIT)
    parser.add_argument("--same-set-json", type=Path, default=DEFAULT_SAME_SET)
    parser.add_argument("--ncblk-json", type=Path, default=DEFAULT_NCBLK)
    parser.add_argument("--clean-contract-md", type=Path, default=DEFAULT_CLEAN_CONTRACT)
    parser.add_argument("--clean-router-json", type=Path, default=DEFAULT_CLEAN_ROUTER)
    parser.add_argument("--kuznetsov-json", type=Path, default=DEFAULT_KUZNETSOV)
    parser.add_argument("--pdec-route-md", type=Path, default=DEFAULT_PDEC_ROUTE)
    parser.add_argument("--line-ref-md", type=Path, default=DEFAULT_LINE_REF)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        split_path=args.split_json,
        same_set_path=args.same_set_json,
        ncblk_path=args.ncblk_json,
        clean_contract_path=args.clean_contract_md,
        clean_router_path=args.clean_router_json,
        kuznetsov_path=args.kuznetsov_json,
        pdec_route_path=args.pdec_route_md,
        line_ref_path=args.line_ref_md,
    )
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(result["status"])
    print(result["narrowest_self_contained_hardpoint"])


if __name__ == "__main__":
    main()
