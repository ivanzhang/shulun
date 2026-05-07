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
DEFAULT_CROSS_Q = DOCS / "prime-matrix-wsh-fo-pdec-cross-q-chart-overlap-audit.json"
DEFAULT_PHYSICAL_TAUTOLOGY = (
    DOCS / "prime-matrix-wsh-fo-pdec-physical-primitive-tautology-audit.json"
)
DEFAULT_SAE_ENDPOINT = (
    DOCS / "prime-matrix-wsh-fo-pdec-sae-endpoint-absorption-audit.json"
)
DEFAULT_LOCAL_SURVIVOR_LEDGER = (
    DOCS / "prime-matrix-local-survivor-materialized-packet-ledger.json"
)
DEFAULT_PACKET_EXTRACTOR_COVERAGE = (
    DOCS / "prime-matrix-local-survivor-packet-extractor-coverage.json"
)
DEFAULT_NEW_SPARSE_ADMISSION = (
    DOCS / "prime-matrix-new-sparse-entry-admission-audit.json"
)
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
    cross_q: dict[str, Any],
    physical_tautology: dict[str, Any],
    sae_endpoint: dict[str, Any],
    local_survivor_ledger: dict[str, Any],
    packet_extractor_coverage: dict[str, Any],
    new_sparse_admission: dict[str, Any],
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
    cross_q_subgate_closed = (
        cross_q["closed_subgate"]
        == "CrossQCoordinatePersistenceRejectedForAuditedFO-PDEC"
        and cross_q["all_cross_level_reuses_chart_overlap_blocked"]
    )
    physical_tautology_subgate_closed = (
        physical_tautology["closed_subgate"]
        == "PhysicalPrimitivePDECThresholdDegeneratesToTwoPointTautology"
        and physical_tautology["all_residue_choices_are_two_point_tautology"]
    )
    sae_endpoint_subgate_closed = (
        sae_endpoint["closed_subgate"]
        == "TwoPhysicalPrimitiveAtomsAbsorbedByLocalSurvivorWitnesses"
        and sae_endpoint["all_sources_have_local_survivor_witness"]
        and sae_endpoint["all_factor_199_fibers_are_sparse_load_one"]
    )
    materialized_local_survivor_closed = (
        local_survivor_ledger["closed_subgate"]
        == "MaterializedLocalSurvivorPacketsExhausted"
        and local_survivor_ledger[
            "current_materialized_local_survivor_packets_closed"
        ]
        and local_survivor_ledger["open_materialized_obligation_count"] == 0
    )
    known_packet_extractors_covered = (
        packet_extractor_coverage["closed_subgate"]
        == "KnownLocalSurvivorEntryExtractorsCovered"
        and packet_extractor_coverage["known_entry_extractor_coverage_closed"]
        and packet_extractor_coverage["missing_or_open_count"] == 0
    )
    no_new_sparse_entry = (
        new_sparse_admission["closed_subgate"]
        == "NoAdditionalUnnamedLocalSurvivorEntryRoute"
        and new_sparse_admission["no_additional_unnamed_local_survivor_entry_route"]
        and new_sparse_admission["missing_admission_count"] == 0
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
            "TwoPhysicalPrimitiveAtomsAbsorbedByLocalSurvivorWitnesses",
            "MaterializedLocalSurvivorPacketsExhausted",
            "KnownLocalSurvivorEntryExtractorsCovered",
            "NoAdditionalUnnamedLocalSurvivorEntryRoute",
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
            status=(
                "audited_current_sample_subgates_closed_global_family_open"
                if sae_endpoint_subgate_closed
                else "current_narrowest_open"
            ),
            evidence=(
                f"raw ell={raw_best['factor']}, h={raw_best['frequency']}, "
                f"Fourier={raw_best['fourier']}; "
                f"coordinate-cap Fourier={coordinate_cap_best['fourier']}; "
                f"physical-cap Fourier={physical_cap_best['fourier']}; "
                f"q-row dedup best={q_row_best['fourier']}; "
                f"block-local best={block_best['fourier']}; "
                f"nested_unit_blocked={nested_subgate_closed}; "
                f"weighted_full_duplicate_blocked={weighted_subgate_closed}; "
                f"cross_q_chart_overlap_blocked={cross_q_subgate_closed}; "
                f"physical_two_point_tautology={physical_tautology_subgate_closed}; "
                f"two_atom_sae_endpoint_absorbed={sae_endpoint_subgate_closed}"
            ),
            remaining=(
                "当前已审计 FO-PDEC 样本链中，raw、coordinate-cap、physical 二点阈值和二点 "
                "SAE/Endpoint 均已被降口径或本地 witness 吸收；但完整 PDEC family 对未来非二点、"
                "非同图重叠 formal unit 仍未闭合。"
            ),
            next_action=(
                "停止优化当前 U_CRT 常数；转向 packet-generation，或寻找至少三点非退化 "
                "primitive PDEC formal unit。"
            ),
            blocks_global=True,
        ),
        frontier_row(
            gate="B:LocalSurvivorFamily",
            status=(
                "materialized_packets_closed_global_generation_open"
                if materialized_local_survivor_closed
                else "open_terminal"
            ),
            evidence=(
                f"materialized_packets={local_survivor_ledger['materialized_packet_count']}; "
                f"witnesses={local_survivor_ledger['local_survivor_witness_count']}; "
                f"open_materialized={local_survivor_ledger['open_materialized_obligation_count']}; "
                f"known_extractors_covered={known_packet_extractors_covered}; "
                f"no_new_sparse_entry={no_new_sparse_entry}"
            ),
            remaining=(
                "当前已物化 LocalSurvivor/SAE 包全部闭合；全局剩余是 packet-generation："
                "已知入口 extractor 均覆盖；当前也不存在未命名新 sparse 入口。未来若新增显式"
                " sparse 路线，必须提交同类 extractor。"
            ),
            next_action="LocalSurvivor 当前分支转为条件闭合；主攻非二点 PDEC 或 CleanKLS/DLS。",
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
    cross_q_path: Path,
    physical_tautology_path: Path,
    sae_endpoint_path: Path,
    local_survivor_ledger_path: Path,
    packet_extractor_coverage_path: Path,
    new_sparse_admission_path: Path,
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
    cross_q = load_json(cross_q_path)
    physical_tautology = load_json(physical_tautology_path)
    sae_endpoint = load_json(sae_endpoint_path)
    local_survivor_ledger = load_json(local_survivor_ledger_path)
    packet_extractor_coverage = load_json(packet_extractor_coverage_path)
    new_sparse_admission = load_json(new_sparse_admission_path)
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
        cross_q,
        physical_tautology,
        sae_endpoint,
        local_survivor_ledger,
        packet_extractor_coverage,
        new_sparse_admission,
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
            "cross_q_chart_overlap_audit": file_sha256(cross_q_path),
            "physical_primitive_tautology_audit": file_sha256(physical_tautology_path),
            "sae_endpoint_absorption_audit": file_sha256(sae_endpoint_path),
            "local_survivor_materialized_packet_ledger": file_sha256(
                local_survivor_ledger_path
            ),
            "local_survivor_packet_extractor_coverage": file_sha256(
                packet_extractor_coverage_path
            ),
            "new_sparse_entry_admission_audit": file_sha256(new_sparse_admission_path),
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
            "name": (
                "NonTautologicalPDECOrCleanKLS"
                if new_sparse_admission["closed_subgate"]
                == "NoAdditionalUnnamedLocalSurvivorEntryRoute"
                else (
                    "NewSparseEntryAdmissionOrNonTautologicalPDEC"
                    if packet_extractor_coverage["closed_subgate"]
                    == "KnownLocalSurvivorEntryExtractorsCovered"
                    else (
                        "LocalSurvivorPacketGenerationOrNonTautologicalPDEC"
                        if local_survivor_ledger["closed_subgate"]
                        == "MaterializedLocalSurvivorPacketsExhausted"
                        else "GlobalLocalSurvivorOrNonTautologicalPDEC"
                    )
                )
            ),
            "subgate_closed_this_round": (
                "NoAdditionalUnnamedLocalSurvivorEntryRoute"
                if new_sparse_admission["closed_subgate"]
                == "NoAdditionalUnnamedLocalSurvivorEntryRoute"
                else (
                    "KnownLocalSurvivorEntryExtractorsCovered"
                    if packet_extractor_coverage["closed_subgate"]
                    == "KnownLocalSurvivorEntryExtractorsCovered"
                    else (
                        "MaterializedLocalSurvivorPacketsExhausted"
                        if local_survivor_ledger["closed_subgate"]
                        == "MaterializedLocalSurvivorPacketsExhausted"
                        else (
                            "TwoPhysicalPrimitiveAtomsAbsorbedByLocalSurvivorWitnesses"
                            if sae_endpoint["closed_subgate"]
                            == "TwoPhysicalPrimitiveAtomsAbsorbedByLocalSurvivorWitnesses"
                            else (
                                "PhysicalPrimitivePDECThresholdDegeneratesToTwoPointTautology"
                                if physical_tautology["closed_subgate"]
                                == "PhysicalPrimitivePDECThresholdDegeneratesToTwoPointTautology"
                                else (
                                    "CrossQCoordinatePersistenceRejectedForAuditedFO-PDEC"
                                    if cross_q["closed_subgate"]
                                    == "CrossQCoordinatePersistenceRejectedForAuditedFO-PDEC"
                                    else (
                                        "FractionalWeightedHallCannotRecoverFullNestedDuplicateMass"
                                        if weighted["closed_subgate"]
                                        == "FractionalWeightedHallCannotRecoverFullNestedDuplicateMass"
                                        else (
                                            "NestedBlockFullMultiplicityRejectedForAuditedFO-PDEC"
                                            if nested_closed
                                            else "NestedBlockMultiplicityStillOpen"
                                        )
                                    )
                                )
                            )
                        )
                    )
                )
            ),
            "raw_best": raw_best,
            "coordinate_cap_best": coordinate_cap_best,
            "physical_cap_best": physical_cap_best,
            "reason": (
                "PDEC 是三终端中最直接连接 A1 已闭合边界的端口；"
                "当前已审计 FO-PDEC 强信号链已被逐层降口径，最后两个物理原子由"
                "同固定偏移纤维的本地素数见证吸收；已物化 LocalSurvivor/SAE 包总账"
                "也无开放窗口；已知 packet extractor 入口全覆盖，且无未命名新 sparse 入口。"
                "LocalSurvivor 当前分支只剩未来显式新增入口的条件义务；当前主硬点转向非二点 "
                "primitive PDEC 或 CleanKLS/DLS。"
            ),
            "next_routes": [
                "PacketExtractorCompleteness for any newly admitted sparse route",
                "future primitive PDEC only if a same-formal-unit family has at least three non-tautological physical atoms or extra constraints",
                "CleanKLS/DLS and D-structure/Rankin referee inputs for final theorem promotion",
            ],
        },
        "review_conclusion": (
            "行列无条件自足版尚未闭合。已闭合的是 canonical-source Triad-A1 边界；"
            "已排除的是 unrestricted generic WFD 自足版；当前已审计 FO-PDEC ell=199 强信号链"
            "已经依次通过嵌套重复、weighted Hall、cross-q 坐标图、physical 二点 tautology 和"
            "二点 SAE/Endpoint 本地 witness 吸收；已物化 LocalSurvivor/SAE 包总账也全部闭合。"
            "已知 LocalSurvivor packet extractor 入口也全部覆盖，且无未命名新 sparse 入口。"
            "下一步应攻非二点 primitive PDEC formal unit 或 CleanKLS/DLS。"
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
    parser.add_argument("--cross-q", type=Path, default=DEFAULT_CROSS_Q)
    parser.add_argument("--physical-tautology", type=Path, default=DEFAULT_PHYSICAL_TAUTOLOGY)
    parser.add_argument("--sae-endpoint", type=Path, default=DEFAULT_SAE_ENDPOINT)
    parser.add_argument("--local-survivor-ledger", type=Path, default=DEFAULT_LOCAL_SURVIVOR_LEDGER)
    parser.add_argument("--packet-extractor-coverage", type=Path, default=DEFAULT_PACKET_EXTRACTOR_COVERAGE)
    parser.add_argument("--new-sparse-admission", type=Path, default=DEFAULT_NEW_SPARSE_ADMISSION)
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
        args.cross_q,
        args.physical_tautology,
        args.sae_endpoint,
        args.local_survivor_ledger,
        args.packet_extractor_coverage,
        args.new_sparse_admission,
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
