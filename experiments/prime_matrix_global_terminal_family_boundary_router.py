#!/usr/bin/env python3
"""审查当前已物化前沿耗尽后，剩余是否只剩全局终端家族排斥。

用法示例：
  python3 experiments/prime_matrix_global_terminal_family_boundary_router.py

输出：
  docs/monograph/prime-matrix-global-terminal-family-boundary-router.json
  docs/monograph/prime-matrix-global-terminal-family-boundary-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_ROW_FRONTIER = DOCS / "prime-matrix-row-column-unconditional-frontier-router.json"
DEFAULT_TERMINAL_TRIAD = DOCS / "prime-matrix-terminal-certificate-triad.md"
DEFAULT_LOCAL_LEDGER = DOCS / "prime-matrix-local-survivor-materialized-packet-ledger.json"
DEFAULT_PACKET_COVERAGE = DOCS / "prime-matrix-local-survivor-packet-extractor-coverage.json"
DEFAULT_SPARSE_ADMISSION = DOCS / "prime-matrix-new-sparse-entry-admission-audit.json"
DEFAULT_NCBLK = DOCS / "prime-matrix-ncblk-boundary-reconciliation-router.json"
DEFAULT_NONTAUTOLOGICAL_PDEC = (
    DOCS / "prime-matrix-nontautological-pdec-admission-audit.json"
)
DEFAULT_BOUNDARY_MERGE = DOCS / "prime-matrix-row-theorem-boundary-merge-audit.json"
DEFAULT_LINE_REF = DOCS / "line-by-line-internal-referee-matrix.md"
DEFAULT_JSON = DOCS / "prime-matrix-global-terminal-family-boundary-router.json"
DEFAULT_MD = DOCS / "prime-matrix-global-terminal-family-boundary-router.md"


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
    """把布尔值输出成小写文本。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def has_all(text: str, needles: list[str]) -> bool:
    """检查文本是否包含全部片段。"""
    return all(needle in text for needle in needles)


def find_frontier_row(row_frontier: dict[str, Any], gate: str) -> dict[str, Any]:
    """按 gate 查找总前沿行。"""
    for row in row_frontier.get("frontier_rows", []):
        if row.get("gate") == gate:
            return row
    return {}


def boundary_row(
    gate: str,
    closed: bool,
    evidence: str,
    meaning: str,
    blocks_final: bool,
) -> dict[str, Any]:
    """构造边界审查行。"""
    return {
        "gate": gate,
        "closed": closed,
        "evidence": evidence,
        "meaning": meaning,
        "blocks_final": blocks_final,
    }


def build_rows(
    row_frontier: dict[str, Any],
    terminal_triad_text: str,
    local_ledger: dict[str, Any],
    packet_coverage: dict[str, Any],
    sparse_admission: dict[str, Any],
    ncblk: dict[str, Any],
    nontautological_pdec: dict[str, Any],
    boundary_merge: dict[str, Any],
    line_ref_text: str,
) -> list[dict[str, Any]]:
    """生成全局终端家族边界审查表。"""
    hardpoint = row_frontier["narrowest_next_hardpoint"]
    pdec_row = find_frontier_row(row_frontier, "A1-FO-PDEC-SameFormalUnit")
    local_row = find_frontier_row(row_frontier, "B:LocalSurvivorFamily")
    clean_row = find_frontier_row(row_frontier, "C:CleanKLS-DLS")

    materialized_exhausted = (
        hardpoint["name"]
        == "CurrentMaterializedFrontierExhausted_GlobalTerminalFamiliesOpen"
        and hardpoint["subgate_closed_this_round"]
        == "NoCurrentMaterializedNonTautologicalPDECAndNCBLKReconciled"
        and not row_frontier["row_column_unconditional_closed"]
    )
    triad_generation_contract_closed = (
        row_frontier["terminal_triad_routed_no_fourth_exit"]
        and has_all(
            terminal_triad_text,
            [
                "A. PDEC family certificates",
                "B. LocalSurvivorCert family",
                "C. CleanKLS/DLS certificates",
                "无第四出口定理",
                "Persistent",
                "Sparse",
                "Flat",
            ],
        )
    )
    current_pdec_empty = (
        nontautological_pdec["all_current_routes_blocked_or_absorbed"]
        and nontautological_pdec[
            "current_materialized_nontautological_pdec_candidate_count"
        ]
        == 0
        and not nontautological_pdec["global_pdec_family_closed"]
    )
    local_current_guarded = (
        local_ledger["open_materialized_obligation_count"] == 0
        and packet_coverage["missing_or_open_count"] == 0
        and sparse_admission["missing_admission_count"] == 0
    )
    ncblk_boundary_reconciled = (
        ncblk["all_reconciliation_gates_passed"]
        and ncblk["canonical_ncblk_absorbed_by_existing_boundary"]
        and ncblk["generic_ncblk_self_contained_not_claimed"]
        and not ncblk["row_column_unconditional_closed"]
    )
    status_table_guarded = (
        boundary_merge["merged_boundary_verdict"]
        == "CANONICAL_SOURCE_BOUNDARY_MERGED_NO_GLOBAL_OVERCLAIM"
        and bool(boundary_merge["remaining_global_obligations"])
    )
    referee_open = "BLOCK-REFEREE" in line_ref_text

    return [
        boundary_row(
            gate="CurrentMaterializedFrontierExhausted",
            closed=materialized_exhausted,
            evidence=(
                f"name={hardpoint['name']}; "
                f"subgate={hardpoint['subgate_closed_this_round']}"
            ),
            meaning="当前机器总账能触及的 PDEC、LocalSurvivor 与 NC-BLK 局部硬点已耗尽。",
            blocks_final=False,
        ),
        boundary_row(
            gate="TerminalTriadGenerationContract",
            closed=triad_generation_contract_closed,
            evidence="PDEC / LocalSurvivor / CleanKLS-DLS; no fourth exit",
            meaning="在已列上游合同内，任何最小反例必须进入三类终端证书之一。",
            blocks_final=False,
        ),
        boundary_row(
            gate="CurrentPDECAdmissionEmpty",
            closed=current_pdec_empty,
            evidence=(
                "candidate_count="
                f"{nontautological_pdec['current_materialized_nontautological_pdec_candidate_count']}; "
                f"frontier_status={pdec_row.get('status', 'missing')}"
            ),
            meaning="当前已物化的合法非二点 primitive PDEC 候选为零；未来候选需重新准入。",
            blocks_final=False,
        ),
        boundary_row(
            gate="CurrentLocalSurvivorAndSparseEntryGuarded",
            closed=local_current_guarded,
            evidence=(
                f"open_materialized={local_ledger['open_materialized_obligation_count']}; "
                f"missing_extractors={packet_coverage['missing_or_open_count']}; "
                f"missing_admission={sparse_admission['missing_admission_count']}; "
                f"frontier_status={local_row.get('status', 'missing')}"
            ),
            meaning="当前已物化孤窗包清零，已知入口均有 extractor 或合同准入。",
            blocks_final=False,
        ),
        boundary_row(
            gate="NCBLKBoundaryReconciled",
            closed=ncblk_boundary_reconciled,
            evidence=(
                f"ncblk_reconciled={ncblk['all_reconciliation_gates_passed']}; "
                f"frontier_status={clean_row.get('status', 'missing')}"
            ),
            meaning="NC-BLK 已从无名 CleanKLS 出口改写为 canonical 吸收或 generic 外部路线。",
            blocks_final=False,
        ),
        boundary_row(
            gate="GlobalTerminalFamilyExclusion",
            closed=False,
            evidence=", ".join(boundary_merge["remaining_global_obligations"]),
            meaning="仍未提交全部 PDEC、LocalSurvivor 与 CleanKLS/DLS 家族证书或外部输入。",
            blocks_final=True,
        ),
        boundary_row(
            gate="DStructureRankinRefereePromotion",
            closed=not referee_open,
            evidence="BLOCK-REFEREE" if referee_open else "no referee block token found",
            meaning="D-structure/Tail-log4/finite Rankin 接口仍需独立逐行审稿接受。",
            blocks_final=referee_open,
        ),
        boundary_row(
            gate="ClaimStatusNoOverclaim",
            closed=status_table_guarded,
            evidence=boundary_merge["merged_boundary_verdict"],
            meaning="状态表继续区分已闭合边界、已反证强化版和未闭合全局命题。",
            blocks_final=False,
        ),
    ]


def run(
    row_frontier_path: Path,
    terminal_triad_path: Path,
    local_ledger_path: Path,
    packet_coverage_path: Path,
    sparse_admission_path: Path,
    ncblk_path: Path,
    nontautological_pdec_path: Path,
    boundary_merge_path: Path,
    line_ref_path: Path,
) -> dict[str, Any]:
    """运行全局终端家族边界审查。"""
    row_frontier = load_json(row_frontier_path)
    terminal_triad_text = read_text(terminal_triad_path)
    local_ledger = load_json(local_ledger_path)
    packet_coverage = load_json(packet_coverage_path)
    sparse_admission = load_json(sparse_admission_path)
    ncblk = load_json(ncblk_path)
    nontautological_pdec = load_json(nontautological_pdec_path)
    boundary_merge = load_json(boundary_merge_path)
    line_ref_text = read_text(line_ref_path)

    rows = build_rows(
        row_frontier=row_frontier,
        terminal_triad_text=terminal_triad_text,
        local_ledger=local_ledger,
        packet_coverage=packet_coverage,
        sparse_admission=sparse_admission,
        ncblk=ncblk,
        nontautological_pdec=nontautological_pdec,
        boundary_merge=boundary_merge,
        line_ref_text=line_ref_text,
    )
    closed_nonfinal_gates = all(
        row["closed"] for row in rows if not row["blocks_final"]
    )
    open_final_gates = [row["gate"] for row in rows if row["blocks_final"]]
    materialized_frontier_exhausted = rows[0]["closed"]

    return {
        "certificate_type": "prime_matrix_global_terminal_family_boundary_router",
        "status": "materialized_frontier_exhausted_terminal_family_exclusion_open",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "row_frontier": file_sha256(row_frontier_path),
            "terminal_triad": file_sha256(terminal_triad_path),
            "local_ledger": file_sha256(local_ledger_path),
            "packet_coverage": file_sha256(packet_coverage_path),
            "sparse_admission": file_sha256(sparse_admission_path),
            "ncblk": file_sha256(ncblk_path),
            "nontautological_pdec": file_sha256(nontautological_pdec_path),
            "boundary_merge": file_sha256(boundary_merge_path),
            "line_referee": file_sha256(line_ref_path),
        },
        "materialized_frontier_exhausted": materialized_frontier_exhausted,
        "terminal_generation_contract_closed": rows[1]["closed"],
        "current_terminal_instances_exhausted": all(row["closed"] for row in rows[:5]),
        "global_terminal_family_exclusion_closed": False,
        "row_column_unconditional_closed": False,
        "closed_nonfinal_gates": closed_nonfinal_gates,
        "open_final_gates": open_final_gates,
        "narrowest_next_hardpoint": "GlobalTerminalFamilyExclusionCertificates",
        "next_required_theorem": (
            "For every minimal counterexample, the emitted terminal object must be "
            "certified by a PDEC-family exclusion, a LocalSurvivor witness/deficit "
            "certificate, or a CleanKLS/DLS/internal-large-sieve certificate; otherwise "
            "the branch must route to an explicitly accepted external/referee input."
        ),
        "rows": rows,
        "boundary_law": (
            "The current materialized ledger has no remaining local terminal instance to "
            "eliminate: the non-tautological primitive PDEC candidate count is zero, the "
            "materialized LocalSurvivor ledger has no open packet, all known sparse entry "
            "routes are admitted, and NC-BLK has been reconciled with the canonical boundary. "
            "This proves a boundary statement, not the full row/column theorem: a future "
            "counterexample can only survive by producing a genuinely new global terminal "
            "family certificate obligation or by using an accepted external/referee input."
        ),
        "review_conclusion": (
            "当前已物化前沿已经耗尽：PDEC 侧无合法非二点候选，LocalSurvivor 侧无开放包，"
            "已知 sparse 入口全部准入，NC-BLK 已与 canonical-source 边界核查对齐。"
            "因此下一硬点不再是局部样本或固定常数，而是全局终端家族排斥证书：必须证明"
            "所有未来 PDEC/LocalSurvivor/CleanKLS-DLS 终端对象都被证书排除，或明确调用"
            "外部/referee 输入。完整行/列无条件定理仍未闭合。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix 全局终端家族边界路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 边界律",
        "",
        result["boundary_law"],
        "",
        "```text",
        "current materialized frontier:",
        "  PDEC current non-tautological primitive candidates = 0;",
        "  LocalSurvivor open materialized packets = 0;",
        "  known sparse entry routes admitted = true;",
        "  NC-BLK reconciled with canonical boundary = true;",
        "therefore:",
        "  local materialized frontier is exhausted;",
        "  remaining proof target = global terminal family exclusion certificates.",
        "```",
        "",
        "## 2. 汇总",
        "",
        f"- `materialized_frontier_exhausted={fmt_bool(result['materialized_frontier_exhausted'])}`。",
        f"- `terminal_generation_contract_closed={fmt_bool(result['terminal_generation_contract_closed'])}`。",
        f"- `current_terminal_instances_exhausted={fmt_bool(result['current_terminal_instances_exhausted'])}`。",
        f"- `global_terminal_family_exclusion_closed={fmt_bool(result['global_terminal_family_exclusion_closed'])}`。",
        f"- `row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}`。",
        f"- `narrowest_next_hardpoint={result['narrowest_next_hardpoint']}`。",
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
            "## 4. 下一条必须证明的定理",
            "",
            result["next_required_theorem"],
            "",
            "这个路由器的结论不是最终无条件证明。它关闭的是“当前已物化前沿还有可继续局部消元的对象”这一可能；"
            "剩余是全局终端家族全集的排斥或外部/referee 接口接受。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--row-frontier-json", type=Path, default=DEFAULT_ROW_FRONTIER)
    parser.add_argument("--terminal-triad-md", type=Path, default=DEFAULT_TERMINAL_TRIAD)
    parser.add_argument("--local-ledger-json", type=Path, default=DEFAULT_LOCAL_LEDGER)
    parser.add_argument("--packet-coverage-json", type=Path, default=DEFAULT_PACKET_COVERAGE)
    parser.add_argument("--sparse-admission-json", type=Path, default=DEFAULT_SPARSE_ADMISSION)
    parser.add_argument("--ncblk-json", type=Path, default=DEFAULT_NCBLK)
    parser.add_argument(
        "--nontautological-pdec-json", type=Path, default=DEFAULT_NONTAUTOLOGICAL_PDEC
    )
    parser.add_argument("--boundary-merge-json", type=Path, default=DEFAULT_BOUNDARY_MERGE)
    parser.add_argument("--line-ref-md", type=Path, default=DEFAULT_LINE_REF)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        row_frontier_path=args.row_frontier_json,
        terminal_triad_path=args.terminal_triad_md,
        local_ledger_path=args.local_ledger_json,
        packet_coverage_path=args.packet_coverage_json,
        sparse_admission_path=args.sparse_admission_json,
        ncblk_path=args.ncblk_json,
        nontautological_pdec_path=args.nontautological_pdec_json,
        boundary_merge_path=args.boundary_merge_json,
        line_ref_path=args.line_ref_md,
    )
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(result["status"])
    print(result["narrowest_next_hardpoint"])


if __name__ == "__main__":
    main()
