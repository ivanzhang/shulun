#!/usr/bin/env python3
"""汇总 Prime Matrix 行列无条件自足版的当前证明前沿。

用法示例：
  python3 experiments/prime_matrix_row_column_unconditional_frontier_router.py

输出：
  docs/monograph/prime-matrix-row-column-unconditional-frontier-router.json
  docs/monograph/prime-matrix-row-column-unconditional-frontier-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
PAPER = ROOT / "paper" / "contradiction-field-monograph"

DEFAULT_BOUNDARY = DOCS / "prime-matrix-row-theorem-boundary-merge-audit.json"
DEFAULT_CONFLUENCE = DOCS / "prime-matrix-triad-a1-terminal-confluence-router.json"
DEFAULT_TERMINAL_TRIAD = DOCS / "prime-matrix-terminal-certificate-triad.md"
DEFAULT_FORMAL_UNIT = DOCS / "prime-matrix-wsh-fo-pdec-formal-unit-audit.json"
DEFAULT_STITCHING = DOCS / "prime-matrix-wsh-fo-pdec-stitching-feasibility-audit.json"
DEFAULT_NESTED = DOCS / "prime-matrix-wsh-fo-pdec-nested-duplicate-dominance-audit.json"
DEFAULT_WEIGHTED = DOCS / "prime-matrix-wsh-fo-pdec-weighted-hall-dual-audit.json"
DEFAULT_LINE_REF = DOCS / "line-by-line-internal-referee-matrix.md"
DEFAULT_CLAIM_STATUS = DOCS / "claim-status-table.md"
DEFAULT_MAIN_TEX = PAPER / "contradiction-field-monograph.tex"
DEFAULT_JSON = DOCS / "prime-matrix-row-column-unconditional-frontier-router.json"
DEFAULT_MD = DOCS / "prime-matrix-row-column-unconditional-frontier-router.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def read_text(path: Path) -> str:
    """读取文本文件。"""
    return path.read_text(encoding="utf-8")


def file_sha256(path: Path) -> str:
    """计算文件 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def has_all(text: str, needles: list[str]) -> bool:
    """检查文本是否包含全部片段。"""
    return all(needle in text for needle in needles)


def frontier_row(
    gate: str,
    status: str,
    evidence: str,
    remaining: str,
    next_action: str,
    blocks_global: bool,
) -> dict[str, Any]:
    """构造前沿门控行。"""
    return {
        "gate": gate,
        "status": status,
        "evidence": evidence,
        "remaining": remaining,
        "next_action": next_action,
        "blocks_global": blocks_global,
    }


def build_frontier_rows(
    boundary: dict[str, Any],
    confluence: dict[str, Any],
    terminal_triad_text: str,
    formal_unit: dict[str, Any],
    stitching: dict[str, Any],
    nested: dict[str, Any],
    weighted: dict[str, Any],
    line_ref_text: str,
    claim_status_text: str,
    main_tex: str,
) -> list[dict[str, Any]]:
    """生成行列无条件前沿表。"""
    boundary_closed = (
        boundary["status"] == "row_theorem_boundary_merge_audit_passed"
        and boundary["merged_boundary_verdict"]
        == "CANONICAL_SOURCE_BOUNDARY_MERGED_NO_GLOBAL_OVERCLAIM"
        and not boundary["open_gates"]
    )
    generic_rejected = "Unrestricted generic" in boundary["not_claimed_theorem"]
    triad_routed = (
        confluence["all_current_pxP_exits_closed"]
        and confluence["all_materialized_branches_routed_to_terminal_triad"]
        and confluence["no_fourth_exit_current_a1_chain"]
        and has_all(
            terminal_triad_text,
            [
                "A. PDEC family certificates",
                "B. LocalSurvivorCert family",
                "C. CleanKLS/DLS certificates",
                "无第四出口定理",
            ],
        )
    )
    formal_unit_open = (
        formal_unit["status"] == "finite_fo_pdec_formal_unit_audit_not_global_proof"
        and stitching["summary"]["formal_unit_conclusion"]
    )
    nested_subgate_closed = (
        nested["closed_subgate"]
        == "NestedBlockFullMultiplicityRejectedForAuditedFO-PDEC"
        and nested["all_exact_nested_duplicates_unit_weight_blocked"]
    )
    weighted_subgate_closed = (
        weighted["closed_subgate"]
        == "FractionalWeightedHallCannotRecoverFullNestedDuplicateMass"
        and weighted["all_nested_full_extra_unit_weight_blocked"]
    )
    referee_guarded = has_all(
        line_ref_text,
        ["PM-16", "BLOCK-REFEREE", "Tail-log4", "finite"],
    ) and has_all(
        main_tex,
        [
            "D-structure exclusion",
            "remaining global PDEC/SAE/Rankin",
            "not as a final unconditional prime-matrix theorem",
        ],
    )
    status_table_guarded = has_all(
        claim_status_text,
        [
            "行命题最终边界合并审查",
            "PDEC family certificates",
            "LocalSurvivorCert family",
        ],
    )
    raw_best = stitching["summary"]["raw_best"]
    weighted_modes = {row["mode"]: row for row in weighted["mode_comparison"]}
    coordinate_cap_best = weighted_modes["nested_coordinate_cap"]["best"]
    physical_cap_best = weighted_modes["physical_candidate_cap"]["best"]
    q_row_best = stitching["summary"]["q_row_coordinate_dedup_best"]["best"]
    block_best = stitching["summary"]["block_local_best"]["best"]

    return [
        frontier_row(
            gate="CanonicalSourceSelfContainedBoundary",
            status="closed" if boundary_closed else "open",
            evidence=boundary["merged_boundary_verdict"],
            remaining="无 theorem-boundary 剩余；只限 canonical RIW/Buchstab source branch。",
            next_action="保持边界，不把它升级成完整行列无条件定理。",
            blocks_global=False,
        ),
        frontier_row(
            gate="UnrestrictedGenericWFD",
            status="refuted_not_claimed" if generic_rejected else "ambiguous",
            evidence=boundary["not_claimed_theorem"],
            remaining="不得作为自足闭合路线继续使用。",
            next_action="禁止回到 generic full-S WFD 自足版。",
            blocks_global=False,
        ),
        frontier_row(
            gate="TerminalTriadNoFourthExit",
            status="routed_not_closed" if triad_routed else "open",
            evidence=confluence["review_conclusion"],
            remaining="三终端证书全集仍未提交。",
            next_action="只在 PDEC / LocalSurvivor / CleanKLS 三终端内继续推进。",
            blocks_global=True,
        ),
        frontier_row(
            gate="A:PDECFamily",
            status="open_terminal",
            evidence="; ".join(confluence["terminal_open_obligations"][:1]),
            remaining="explicit/profinite/weighted/primitive/cofactor/displacement/gcd-stratum 全部需要 U_CRT<L_PDEC 或回流。",
            next_action="优先攻同一 formal unit 的 PDEC 合法性和容量上界。",
            blocks_global=True,
        ),
        frontier_row(
            gate="A1-FO-PDEC-SameFormalUnit",
            status="current_narrowest_open",
            evidence=(
                f"raw ell={raw_best['factor']}, h={raw_best['frequency']}, "
                f"Fourier={raw_best['fourier']}; "
                f"coordinate-cap Fourier={coordinate_cap_best['fourier']}; "
                f"physical-cap Fourier={physical_cap_best['fourier']}; "
                f"q-row dedup best={q_row_best['fourier']}; "
                f"block-local best={block_best['fourier']}; "
                f"nested_unit_blocked={nested_subgate_closed}; "
                f"weighted_full_duplicate_blocked={weighted_subgate_closed}"
            ),
            remaining=(
                "global_library_raw 强阈值尚未是单分支 PDEC 下界；"
                "嵌套单位重复和 fractional weighted full duplicate 均已被支配，"
                "剩余是 cross-q persistence、coordinate-cap 阈值、primitive 阈值或 SAE/Endpoint。"
            ),
            next_action=(
                "优先攻 cross-q persistence；若成立则攻 coordinate-cap U_CRT<2.9698366905785227，"
                "若失败则转 primitive PDEC 或 SAE/Endpoint 吸收。"
            ),
            blocks_global=True,
        ),
        frontier_row(
            gate="B:LocalSurvivorFamily",
            status="open_terminal",
            evidence="; ".join(confluence["terminal_open_obligations"][1:2]),
            remaining="所有 sparse/孤窗候选集仍需 witness 或 blocker 覆盖不足证书。",
            next_action="接收 PDEC 失败后的稀疏重复、Endpoint 和短弧对象，逐窗给 witness/deficit。",
            blocks_global=True,
        ),
        frontier_row(
            gate="C:CleanKLS-DLS",
            status="open_terminal_or_external",
            evidence="; ".join(confluence["terminal_open_obligations"][2:3]),
            remaining="所有 clean residual 仍需内部大筛证书或明确 ExternalKLS 输入。",
            next_action="只有在 PDEC/SAE/column/tail/fiber 峰全部剥离后才调用。",
            blocks_global=True,
        ),
        frontier_row(
            gate="D-structure/Tail-log4/RankinReferee",
            status="referee_block_guarded" if referee_guarded else "unguarded",
            evidence="PM-16 保持 BLOCK-REFEREE；主稿保留 D-structure/Tail-log4/Rankin 边界。",
            remaining="独立接受 D-structure/Tail-log4/finite Rankin 接口前不能升级全局定理。",
            next_action="与三终端并行保持为最终晋级输入，不得由 A1 边界替代。",
            blocks_global=True,
        ),
        frontier_row(
            gate="ClaimStatusDiscipline",
            status="guarded" if status_table_guarded else "needs_update",
            evidence="claim-status table records boundary merge and remaining global obligations.",
            remaining="状态表必须继续区分已闭合边界、已反证分支和未闭合全局命题。",
            next_action="本路由器归档后补入状态表和合著总览。",
            blocks_global=not status_table_guarded,
        ),
    ]


def run(
    boundary_path: Path,
    confluence_path: Path,
    terminal_triad_path: Path,
    formal_unit_path: Path,
    stitching_path: Path,
    nested_path: Path,
    weighted_path: Path,
    line_ref_path: Path,
    claim_status_path: Path,
    main_tex_path: Path,
) -> dict[str, Any]:
    """运行前沿路由审查。"""
    boundary = load_json(boundary_path)
    confluence = load_json(confluence_path)
    terminal_triad_text = read_text(terminal_triad_path)
    formal_unit = load_json(formal_unit_path)
    stitching = load_json(stitching_path)
    nested = load_json(nested_path)
    weighted = load_json(weighted_path)
    line_ref_text = read_text(line_ref_path)
    claim_status_text = read_text(claim_status_path)
    main_tex = read_text(main_tex_path)

    rows = build_frontier_rows(
        boundary,
        confluence,
        terminal_triad_text,
        formal_unit,
        stitching,
        nested,
        weighted,
        line_ref_text,
        claim_status_text,
        main_tex,
    )
    open_global_gates = [
        row["gate"]
        for row in rows
        if row["blocks_global"] and row["status"] not in {"guarded"}
    ]
    raw_best = stitching["summary"]["raw_best"]
    weighted_modes = {row["mode"]: row for row in weighted["mode_comparison"]}
    coordinate_cap_best = weighted_modes["nested_coordinate_cap"]["best"]
    physical_cap_best = weighted_modes["physical_candidate_cap"]["best"]
    nested_closed = (
        nested["closed_subgate"]
        == "NestedBlockFullMultiplicityRejectedForAuditedFO-PDEC"
    )
    return {
        "certificate_type": "prime_matrix_row_column_unconditional_frontier_router",
        "status": "row_column_unconditional_frontier_routed_not_closed",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "boundary_merge": file_sha256(boundary_path),
            "terminal_confluence": file_sha256(confluence_path),
            "terminal_triad": file_sha256(terminal_triad_path),
            "formal_unit_audit": file_sha256(formal_unit_path),
            "stitching_audit": file_sha256(stitching_path),
            "nested_duplicate_dominance": file_sha256(nested_path),
            "weighted_hall_dual_audit": file_sha256(weighted_path),
            "line_referee_matrix": file_sha256(line_ref_path),
            "claim_status_table": file_sha256(claim_status_path),
            "main_tex": file_sha256(main_tex_path),
        },
        "row_column_unconditional_closed": False,
        "canonical_source_boundary_closed": (
            boundary["merged_boundary_verdict"]
            == "CANONICAL_SOURCE_BOUNDARY_MERGED_NO_GLOBAL_OVERCLAIM"
        ),
        "generic_unrestricted_self_contained_refuted": True,
        "terminal_triad_routed_no_fourth_exit": (
            confluence["all_materialized_branches_routed_to_terminal_triad"]
            and confluence["no_fourth_exit_current_a1_chain"]
        ),
        "frontier_rows": rows,
        "open_global_gates": open_global_gates,
        "narrowest_next_hardpoint": {
            "name": "A1-FO-PDEC-SameFormalUnit",
            "subgate_closed_this_round": (
                "FractionalWeightedHallCannotRecoverFullNestedDuplicateMass"
                if weighted["closed_subgate"]
                == "FractionalWeightedHallCannotRecoverFullNestedDuplicateMass"
                else (
                    "NestedBlockFullMultiplicityRejectedForAuditedFO-PDEC"
                    if nested_closed
                    else "NestedBlockMultiplicityStillOpen"
                )
            ),
            "raw_best": raw_best,
            "coordinate_cap_best": coordinate_cap_best,
            "physical_cap_best": physical_cap_best,
            "reason": (
                "PDEC 是三终端中最直接连接 A1 已闭合边界的端口；"
                "但 U_CRT 常数比较必须先在同一 formal unit 上合法；"
                "本轮已排除嵌套重复通过 fractional weighted dual 恢复完整第二单位质量。"
            ),
            "next_routes": [
                "cross-q persistence theorem",
                "coordinate-cap PDEC threshold U_CRT < 2.9698366905785227",
                "physical/primitive PDEC threshold U_CRT < 1.9997507790353146",
                "SAE/Endpoint absorption for rejected cross-level reuses",
            ],
        },
        "review_conclusion": (
            "行列无条件自足版尚未闭合。已闭合的是 canonical-source Triad-A1 边界；"
            "已排除的是 unrestricted generic WFD 自足版；当前最窄硬点是 A:PDEC 端口内"
            "同一 formal unit 的 FO-PDEC 合法性。嵌套块单位重复及其 fractional weighted full duplicate "
            "恢复路线均已被阻断；下一步应攻 cross-q persistence，或转入 coordinate-cap/primitive PDEC "
            "与 SAE/Endpoint 吸收。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 前沿报告。"""
    lines = [
        "# Prime Matrix 行列无条件自足前沿路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 总裁定",
        "",
        "```text",
        f"row_column_unconditional_closed: {str(result['row_column_unconditional_closed']).lower()}",
        f"canonical_source_boundary_closed: {str(result['canonical_source_boundary_closed']).lower()}",
        (
            "generic_unrestricted_self_contained_refuted: "
            f"{str(result['generic_unrestricted_self_contained_refuted']).lower()}"
        ),
        (
            "terminal_triad_routed_no_fourth_exit: "
            f"{str(result['terminal_triad_routed_no_fourth_exit']).lower()}"
        ),
        "```",
        "",
        "## 2. 前沿门控表",
        "",
        "| gate | status | evidence | remaining | next action |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in result["frontier_rows"]:
        lines.append(
            "| "
            + " | ".join(
                table_cell(row[key])
                for key in ["gate", "status", "evidence", "remaining", "next_action"]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 3. 当前最窄硬点",
            "",
            "```text",
            f"name: {result['narrowest_next_hardpoint']['name']}",
            (
                "subgate_closed_this_round: "
                f"{result['narrowest_next_hardpoint']['subgate_closed_this_round']}"
            ),
            f"raw_best: {result['narrowest_next_hardpoint']['raw_best']}",
            f"coordinate_cap_best: {result['narrowest_next_hardpoint']['coordinate_cap_best']}",
            f"physical_cap_best: {result['narrowest_next_hardpoint']['physical_cap_best']}",
            "```",
            "",
            result["narrowest_next_hardpoint"]["reason"],
            "",
            "下一步只应在以下路线中择一推进：",
            "",
        ]
    )
    for item in result["narrowest_next_hardpoint"]["next_routes"]:
        lines.append(f"- `{item}`")
    lines.extend(
        [
            "",
            "## 4. 开放全局门",
            "",
        ]
    )
    for gate in result["open_global_gates"]:
        lines.append(f"- `{gate}`")
    lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--boundary", type=Path, default=DEFAULT_BOUNDARY)
    parser.add_argument("--confluence", type=Path, default=DEFAULT_CONFLUENCE)
    parser.add_argument("--terminal-triad", type=Path, default=DEFAULT_TERMINAL_TRIAD)
    parser.add_argument("--formal-unit", type=Path, default=DEFAULT_FORMAL_UNIT)
    parser.add_argument("--stitching", type=Path, default=DEFAULT_STITCHING)
    parser.add_argument("--nested", type=Path, default=DEFAULT_NESTED)
    parser.add_argument("--weighted", type=Path, default=DEFAULT_WEIGHTED)
    parser.add_argument("--line-ref", type=Path, default=DEFAULT_LINE_REF)
    parser.add_argument("--claim-status", type=Path, default=DEFAULT_CLAIM_STATUS)
    parser.add_argument("--main-tex", type=Path, default=DEFAULT_MAIN_TEX)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        args.boundary,
        args.confluence,
        args.terminal_triad,
        args.formal_unit,
        args.stitching,
        args.nested,
        args.weighted,
        args.line_ref,
        args.claim_status,
        args.main_tex,
    )
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(result["status"])
    print(result["narrowest_next_hardpoint"]["name"])


if __name__ == "__main__":
    main()
