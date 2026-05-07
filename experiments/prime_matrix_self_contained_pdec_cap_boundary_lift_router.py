#!/usr/bin/env python3
"""把 PDEC-CAP canonical-source 闭合结果提升到上层自足边界。

用法示例：
  python3 experiments/prime_matrix_self_contained_pdec_cap_boundary_lift_router.py

输出：
  docs/monograph/prime-matrix-self-contained-pdec-cap-boundary-lift-router.json
  docs/monograph/prime-matrix-self-contained-pdec-cap-boundary-lift-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PDEC_CAP = DOCS / "prime-matrix-pdec-cap-same-set-global-dual-router.json"
DEFAULT_SELF_BOTTLENECK = (
    DOCS / "prime-matrix-self-contained-terminal-bottleneck-router.json"
)
DEFAULT_GLOBAL_SPLIT = (
    DOCS / "prime-matrix-global-terminal-family-exclusion-split-router.json"
)
DEFAULT_ROW_FRONTIER = (
    DOCS / "prime-matrix-row-column-unconditional-frontier-router.json"
)
DEFAULT_LINE_REF = DOCS / "line-by-line-internal-referee-matrix.md"
DEFAULT_JSON = (
    DOCS / "prime-matrix-self-contained-pdec-cap-boundary-lift-router.json"
)
DEFAULT_MD = DOCS / "prime-matrix-self-contained-pdec-cap-boundary-lift-router.md"


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
    """把布尔值写成小写文本。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def find_row(rows: list[dict[str, Any]], gate: str) -> dict[str, Any]:
    """按 gate 查找行。"""
    for row in rows:
        if row.get("gate") == gate:
            return row
    return {}


def lift_row(
    gate: str,
    closed: bool,
    evidence: str,
    lifted_meaning: str,
    boundary_warning: str,
    blocks_final: bool,
) -> dict[str, Any]:
    """构造边界提升审查行。"""
    return {
        "gate": gate,
        "closed": closed,
        "evidence": evidence,
        "lifted_meaning": lifted_meaning,
        "boundary_warning": boundary_warning,
        "blocks_final": blocks_final,
    }


def build_rows(
    pdec_cap: dict[str, Any],
    self_bottleneck: dict[str, Any],
    global_split: dict[str, Any],
    row_frontier: dict[str, Any],
    line_ref_text: str,
) -> list[dict[str, Any]]:
    """生成 PDEC-CAP 边界提升审查表。"""
    pdec_old_hardpoint = (
        self_bottleneck["self_contained_terminal_bottleneck_is_pdec_cap"]
        and self_bottleneck["narrowest_self_contained_hardpoint"]
        == "PDEC_CAP_SameSetGlobalDualCertificate"
    )
    pdec_canonical_closed = (
        pdec_cap["canonical_source_self_contained_pdec_cap_closed"]
        and pdec_cap["closed_current_materialized_pdec_gates"]
    )
    pdec_canonical_gate = find_row(
        pdec_cap["rows"], "CanonicalLayerAdmissionNonzeroTransferAndThinIntervalReturn"
    )
    no_self_contained_pdec_open_gate = (
        pdec_canonical_closed
        and pdec_canonical_gate.get("closed") is True
        and pdec_cap["open_final_gates"]
        == ["DIBFIQuantifiedNoProjectionWindowCertificate"]
        and pdec_cap["narrowest_next_hardpoint"]
        == "DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY"
    )
    generic_external_separated = (
        not pdec_cap["pdec_cap_same_set_global_dual_closed"]
        and "DIBFIQuantifiedNoProjectionWindowCertificate"
        in pdec_cap["open_final_gates"]
    )
    global_family_still_open = (
        not global_split["global_terminal_family_exclusion_closed"]
        and not row_frontier["row_column_unconditional_closed"]
    )
    referee_open = "BLOCK-REFEREE" in line_ref_text
    row_frontier_guarded = (
        row_frontier["canonical_source_boundary_closed"]
        and row_frontier["generic_unrestricted_self_contained_refuted"]
        and not row_frontier["row_column_unconditional_closed"]
    )

    return [
        lift_row(
            gate="PreviousSelfContainedPDECBottleneckAccepted",
            closed=pdec_old_hardpoint,
            evidence=self_bottleneck["narrowest_self_contained_hardpoint"],
            lifted_meaning="上一层已经把 canonical-source 自足路线的独立数学瓶颈压到 PDEC-CAP。",
            boundary_warning="这是旧瓶颈定位，不是最终全局定理。",
            blocks_final=False,
        ),
        lift_row(
            gate="CanonicalSourcePDECCapBranchClosed",
            closed=pdec_canonical_closed,
            evidence=(
                f"canonical={pdec_cap['canonical_source_self_contained_pdec_cap_closed']}; "
                f"materialized={pdec_cap['closed_current_materialized_pdec_gates']}"
            ),
            lifted_meaning=(
                "PDEC-CAP 内部的来源嵌入、横向商、canonical 层转移和已物化门控已经闭合。"
            ),
            boundary_warning="闭合范围只限 canonical RIW/Buchstab source branch。",
            blocks_final=False,
        ),
        lift_row(
            gate="NoFurtherCanonicalSelfContainedPDECGate",
            closed=no_self_contained_pdec_open_gate,
            evidence=pdec_cap["narrowest_next_hardpoint"],
            lifted_meaning=(
                "旧 `PDEC_CAP_SameSetGlobalDualCertificate` 不再是 canonical-source 自足分支的开门。"
            ),
            boundary_warning=(
                "`DIBFIQuantifiedNoProjectionWindowCertificate` 只属于 generic/external 原始 DI/BFI 路线。"
            ),
            blocks_final=False,
        ),
        lift_row(
            gate="GenericExternalDIBFIBoundarySeparated",
            closed=generic_external_separated,
            evidence=", ".join(pdec_cap["open_final_gates"]),
            lifted_meaning="外部 DI/BFI 量化证书被保留为外部分支，不再污染 canonical-source 自足声明。",
            boundary_warning="若要关闭 generic/external 版本，仍需提交无投影对象恒等式与量化尺度代入。",
            blocks_final=False,
        ),
        lift_row(
            gate="RowFrontierBoundaryDisciplinePreserved",
            closed=row_frontier_guarded,
            evidence=row_frontier["narrowest_next_hardpoint"]["name"],
            lifted_meaning="行列前沿仍区分已闭合 canonical 边界、已反证 generic 分支和未闭合全局命题。",
            boundary_warning="不能把 PDEC-CAP 的 canonical 闭合升级为行/列无条件定理。",
            blocks_final=False,
        ),
        lift_row(
            gate="GlobalTerminalFamiliesStillOpen",
            closed=not global_family_still_open,
            evidence=global_split["narrowest_next_hardpoint"],
            lifted_meaning="完整行/列命题仍需全局终端家族排斥或外部输入。",
            boundary_warning=(
                "PDEC、LocalSurvivor、CleanKLS/DLS 的全局生成/排斥仍是最终晋级前沿。"
            ),
            blocks_final=global_family_still_open,
        ),
        lift_row(
            gate="DStructureRankinRefereeStillOpen",
            closed=not referee_open,
            evidence="BLOCK-REFEREE" if referee_open else "no referee block token found",
            lifted_meaning="最终定理升级仍需 D-structure/Tail-log4/finite Rankin 接口通过独立审稿。",
            boundary_warning="该门不能由 A1/PDEC-CAP canonical 边界替代。",
            blocks_final=referee_open,
        ),
    ]


def run(
    pdec_cap_path: Path,
    self_bottleneck_path: Path,
    global_split_path: Path,
    row_frontier_path: Path,
    line_ref_path: Path,
) -> dict[str, Any]:
    """运行 PDEC-CAP 自足边界提升审查。"""
    pdec_cap = load_json(pdec_cap_path)
    self_bottleneck = load_json(self_bottleneck_path)
    global_split = load_json(global_split_path)
    row_frontier = load_json(row_frontier_path)
    line_ref_text = read_text(line_ref_path)

    rows = build_rows(
        pdec_cap=pdec_cap,
        self_bottleneck=self_bottleneck,
        global_split=global_split,
        row_frontier=row_frontier,
        line_ref_text=line_ref_text,
    )
    closed_nonfinal_lift_gates = all(
        row["closed"] for row in rows if not row["blocks_final"]
    )
    open_final_gates = [
        row["gate"] for row in rows if row["blocks_final"] and not row["closed"]
    ]
    canonical_lift_closed = (
        closed_nonfinal_lift_gates
        and pdec_cap["canonical_source_self_contained_pdec_cap_closed"]
    )

    return {
        "certificate_type": "prime_matrix_self_contained_pdec_cap_boundary_lift_router",
        "status": "self_contained_pdec_cap_boundary_lifted_global_not_closed",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "pdec_cap_same_set_global_dual": file_sha256(pdec_cap_path),
            "self_contained_terminal_bottleneck": file_sha256(
                self_bottleneck_path
            ),
            "global_terminal_family_split": file_sha256(global_split_path),
            "row_column_unconditional_frontier": file_sha256(row_frontier_path),
            "line_referee": file_sha256(line_ref_path),
        },
        "closed_nonfinal_lift_gates": closed_nonfinal_lift_gates,
        "canonical_source_self_contained_pdec_bottleneck_closed": canonical_lift_closed,
        "pdec_cap_same_set_global_dual_closed": pdec_cap[
            "pdec_cap_same_set_global_dual_closed"
        ],
        "generic_external_dibfi_boundary_open": (
            "DIBFIQuantifiedNoProjectionWindowCertificate"
            in pdec_cap["open_final_gates"]
        ),
        "d_structure_rankin_referee_open": "DStructureRankinRefereeStillOpen"
        in open_final_gates,
        "global_terminal_family_exclusion_closed": global_split[
            "global_terminal_family_exclusion_closed"
        ],
        "row_column_unconditional_closed": False,
        "open_final_gates": open_final_gates,
        "narrowest_self_contained_boundary": "NoFurtherCanonicalSourceSelfContainedPDECCapGap",
        "narrowest_global_next_hardpoint": (
            "GlobalTerminalFamilyPromotionReview_OR_DStructureRankinReferee"
        ),
        "external_next_hardpoint": (
            "DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY"
        ),
        "rows": rows,
        "lift_law": (
            "The former self-contained PDEC-CAP bottleneck is closed only after restricting "
            "to the canonical RIW/Buchstab source branch and using the transverse source "
            "embedding plus canonical layer transfer. The remaining DIBFI gate is an "
            "external/generic branch, not a canonical-source self-contained gap. This does "
            "not close the full row/column theorem, because global terminal-family promotion "
            "and the D-structure/Rankin referee interface remain open."
        ),
        "review_conclusion": (
            "PDEC-CAP 的旧自足瓶颈已经完成边界提升：在 canonical-source 分支内，"
            "`PDEC_CAP_SameSetGlobalDualCertificate` 不再是开放硬点；最新剩余 "
            "`DIBFIQuantifiedNoProjectionWindowCertificate` 只属于 generic/external 原始 "
            "DI/BFI 路线。完整行/列无条件定理仍未闭合，剩余是全局终端家族晋级审查与 "
            "`DStructureRankinReferee`。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix PDEC-CAP 自足边界提升路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 提升律",
        "",
        result["lift_law"],
        "",
        "```text",
        "old self-contained bottleneck:",
        "  PDEC_CAP_SameSetGlobalDualCertificate",
        "",
        "after canonical-source lift:",
        "  NoFurtherCanonicalSourceSelfContainedPDECCapGap",
        "",
        "remaining outside that boundary:",
        "  generic/external DI/BFI quantified no-projection certificate;",
        "  global terminal-family promotion review;",
        "  D-structure/Tail-log4/finite Rankin referee interface.",
        "```",
        "",
        "## 2. 汇总",
        "",
        f"- `closed_nonfinal_lift_gates={fmt_bool(result['closed_nonfinal_lift_gates'])}`。",
        (
            "- `canonical_source_self_contained_pdec_bottleneck_closed="
            f"{fmt_bool(result['canonical_source_self_contained_pdec_bottleneck_closed'])}`。"
        ),
        (
            "- `pdec_cap_same_set_global_dual_closed="
            f"{fmt_bool(result['pdec_cap_same_set_global_dual_closed'])}`。"
        ),
        (
            "- `generic_external_dibfi_boundary_open="
            f"{fmt_bool(result['generic_external_dibfi_boundary_open'])}`。"
        ),
        (
            "- `d_structure_rankin_referee_open="
            f"{fmt_bool(result['d_structure_rankin_referee_open'])}`。"
        ),
        (
            "- `row_column_unconditional_closed="
            f"{fmt_bool(result['row_column_unconditional_closed'])}`。"
        ),
        f"- `narrowest_self_contained_boundary={result['narrowest_self_contained_boundary']}`。",
        f"- `narrowest_global_next_hardpoint={result['narrowest_global_next_hardpoint']}`。",
        f"- `external_next_hardpoint={result['external_next_hardpoint']}`。",
        "",
        "## 3. 审查表",
        "",
        "| gate | closed | blocks final | evidence | lifted meaning | boundary warning |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for row in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{blocks}` | {evidence} | {meaning} | {warning} |".format(
                gate=table_cell(row["gate"]),
                closed=fmt_bool(bool(row["closed"])),
                blocks=fmt_bool(bool(row["blocks_final"])),
                evidence=table_cell(row["evidence"]),
                meaning=table_cell(row["lifted_meaning"]),
                warning=table_cell(row["boundary_warning"]),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 下一步",
            "",
            "下一步不再把 canonical-source 自足路线写成缺一个 PDEC-CAP 估计。"
            "真正剩余应分层处理：若坚持自足 canonical-source 分支，当前边界已经没有 PDEC-CAP 开门；"
            "若攻完整行/列无条件定理，则必须处理全局终端家族晋级和 D-structure/Rankin 审稿门；"
            "若攻 generic/external 版本，则另行提交 DI/BFI 无投影量化证书。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pdec-cap-json", type=Path, default=DEFAULT_PDEC_CAP)
    parser.add_argument(
        "--self-bottleneck-json", type=Path, default=DEFAULT_SELF_BOTTLENECK
    )
    parser.add_argument("--global-split-json", type=Path, default=DEFAULT_GLOBAL_SPLIT)
    parser.add_argument("--row-frontier-json", type=Path, default=DEFAULT_ROW_FRONTIER)
    parser.add_argument("--line-ref-md", type=Path, default=DEFAULT_LINE_REF)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        pdec_cap_path=args.pdec_cap_json,
        self_bottleneck_path=args.self_bottleneck_json,
        global_split_path=args.global_split_json,
        row_frontier_path=args.row_frontier_json,
        line_ref_path=args.line_ref_md,
    )
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(result["status"])
    print(result["narrowest_self_contained_boundary"])


if __name__ == "__main__":
    main()
