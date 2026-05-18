#!/usr/bin/env python3
"""同步 terminal-row square-phase 接口到仓库中已有的更深前沿。

用法示例：
  python3 experiments/prime_matrix_terminal_square_phase_downstream_frontier_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-terminal-square-phase-downstream-frontier-sync-router.json

输出：
  data/prime-matrix-terminal-square-phase-downstream-frontier-sync-ledger.json
  docs/monograph/prime-matrix-terminal-square-phase-downstream-frontier-sync-router.json
  docs/monograph/prime-matrix-terminal-square-phase-downstream-frontier-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-terminal-square-phase-downstream-frontier-sync-ledger.json"
OUT_JSON = DOCS / "prime-matrix-terminal-square-phase-downstream-frontier-sync-router.json"
OUT_MD = DOCS / "prime-matrix-terminal-square-phase-downstream-frontier-sync-router.md"

NEXT_TARGET = (
    "TerminalSquarePhaseDownstreamFrontierBasis: "
    "PageExceptionalSingletonCarrierOrNonrealZeroPacketResidualBudget OR "
    "AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn OR "
    "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
)


FRONTIER_FILES = [
    {
        "id": "terminal_crt_atom",
        "label": "Terminal-row CRT atom",
        "json": "prime-matrix-terminal-row-crt-atom-router.json",
        "role": "closes specified terminal atoms small-factor absorption",
    },
    {
        "id": "terminal_square_bridge",
        "label": "Terminal-row square-phase bridge",
        "json": "prime-matrix-terminal-row-square-phase-bridge-router.json",
        "role": "maps terminal missing rows to P^2 +/- r square-phase survivors",
    },
    {
        "id": "halfgrid_boundary",
        "label": "Square-phase half-grid boundary word",
        "json": "prime-matrix-square-phase-halfgrid-boundary-word-router.json",
        "role": "reduces special long block to signed even half-grid survivor pressure",
    },
    {
        "id": "phaseband_pdec",
        "label": "No-slot phase-band PDEC",
        "json": "prime-matrix-square-phase-halfgrid-noslot-phaseband-pdec-router.json",
        "role": "rewrites no-slot load as tail-prime quadratic phase-band count",
    },
    {
        "id": "global_crt_signed_payload",
        "label": "Global CRT signed payload sync",
        "json": "prime-matrix-global-crt-signed-payload-sync-router.json",
        "role": "routes internal CRT skeleton to signed payload / same-set PDEC frontiers",
    },
    {
        "id": "localized_pcrt_linnik2",
        "label": "Localized P-CRT / Linnik=2 barrier",
        "json": "prime-matrix-localized-pcrt-transfer-linnik2-barrier-router.json",
        "role": "identifies pointwise AP least-prime below P^2 as a barrier",
    },
    {
        "id": "rankone_phase_capacity",
        "label": "Linnik=2 rank-one phase capacity",
        "json": "prime-matrix-linnik2-rankone-phase-capacity-router.json",
        "role": "separates total energy capacity from rank-one negative evaluation projection",
    },
    {
        "id": "rankone_explicit_formula",
        "label": "Three-claims rank-one explicit formula",
        "json": "three-claims-frontier-rankone-explicit-formula-router.json",
        "role": "routes rank-one AP obstruction to explicit AP zero-packet bounds",
    },
    {
        "id": "siegel_split",
        "label": "Explicit AP zero-packet Siegel split",
        "json": "prime-matrix-explicit-ap-zero-packet-siegel-split-router.json",
        "role": "splits AP zero packet into Siegel bias and nonreal phase concentration",
    },
    {
        "id": "beta_page_sparsity",
        "label": "Beta-gap Page sparsity",
        "json": "prime-matrix-beta-gap-page-sparsity-router.json",
        "role": "routes ultra-close real-zero multi-carrier risk to Page singleton or nonreal residual",
    },
]


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时给出明确错误。"""
    if not path.exists():
        raise FileNotFoundError(path)
    return json.loads(path.read_text(encoding="utf-8"))


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def compact_status(item: dict[str, str]) -> dict[str, Any]:
    """抽取一个前沿证书的同步状态。"""
    path = DOCS / item["json"]
    data = load_json(path)
    remaining = (
        data.get("hardpoint_after_router")
        or data.get("next_direct_attack_target")
        or data.get("plain_conclusion")
        or data.get("status")
    )
    return {
        "id": item["id"],
        "label": item["label"],
        "json": str(path.relative_to(ROOT)),
        "role": item["role"],
        "status": data.get("status"),
        "hardpoint_before_router": data.get("hardpoint_before_router"),
        "hardpoint_after_router": data.get("hardpoint_after_router"),
        "next_direct_attack_target": data.get("next_direct_attack_target"),
        "remaining_or_status": remaining,
        "same_theorem_target_preserved": data.get("same_theorem_target_preserved"),
        "row_column_unconditional_closed": bool(data.get("row_column_unconditional_closed", False)),
        "sha256": sha256(path),
    }


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "terminal_square_phase_downstream_sync",
            "status": "closed_routing",
            "statement": (
                "The terminal-row square-phase bridge is synchronized with the already "
                "materialized half-grid, phase-band, AP-zero-packet, and signed-payload frontiers."
            ),
        },
        {
            "name": "square_phase_longblock_not_latest_terminal_basis",
            "status": "closed_routing",
            "statement": (
                "SquarePhaseSpecialPhaseLongBlockPDECExclusion is retained as an upstream alias, "
                "not as the deepest active terminal-row frontier in the repository."
            ),
        },
        {
            "name": "downstream_frontier_unconditional_closure",
            "status": "open",
            "statement": (
                "A full row/column proof still needs the remaining AP zero-packet, signed payload, "
                "same-set PDEC, and accepted global input frontiers to close."
            ),
        },
    ]


def build_result() -> dict[str, Any]:
    """生成同步证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    rows = [compact_status(item) for item in FRONTIER_FILES]
    missing_unconditional = [row["label"] for row in rows if row["row_column_unconditional_closed"]]

    aggregate = {
        "frontier_file_count": len(rows),
        "terminal_bridge_upstream_hardpoint": "SquarePhaseSpecialPhaseLongBlockPDECExclusion",
        "square_phase_longblock_synced_downstream": True,
        "row_column_unconditional_closed": False,
        "direct_unconditional_contradiction_found": False,
        "unexpected_closed_rows": missing_unconditional,
        "current_consolidated_remaining_basis": [
            "PageExceptionalSingletonCarrierOrNonrealZeroPacketResidualBudget",
            "AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn",
            "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate",
            "ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem",
            "ExplicitModelGapAndFiniteDPRCLedger",
            "RatePreservationLedger_FOR_moving_atom_packet",
            "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance",
        ],
    }

    ledger = {
        "aggregate": aggregate,
        "frontier_sync_rows": rows,
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    result = {
        "certificate_type": "prime_matrix_terminal_square_phase_downstream_frontier_sync_router",
        "status": "terminal_square_phase_synced_to_downstream_frontier_global_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_evidence_not_used_as_global_proof": True,
        "aggregate": aggregate,
        "frontier_sync_rows": rows,
        "theorem_rows": theorem_rows(),
        "decision_rows": [
            {
                "gate": "TerminalSquarePhaseDownstreamSyncClosed",
                "closed": True,
                "proved": True,
                "meaning": "终端行平方相位桥接已和仓库下游前沿同步。",
                "remaining": "closed routing",
            },
            {
                "gate": "SquarePhaseLongBlockStillDeepestFrontier",
                "closed": True,
                "proved": False,
                "meaning": "`SquarePhaseSpecialPhaseLongBlockPDECExclusion` 只是上游别名，不应再作为最深硬点。",
                "remaining": "downstream basis",
            },
            {
                "gate": "RowColumnUnconditionalClosureReached",
                "closed": False,
                "proved": False,
                "meaning": "本步只同步前沿，不关闭全局行/列命题。",
                "remaining": NEXT_TARGET,
            },
        ],
        "plain_conclusion": (
            "本步把 terminal-row square-phase bridge 从旧的 "
            "`SquarePhaseSpecialPhaseLongBlockPDECExclusion` 同步到仓库已有下游前沿："
            "half-grid/phase-band 路由、localized P-CRT/AP 零点包路线、以及 global CRT signed-payload 路线。"
            "因此该旧硬点应视为上游接口别名；当前 consolidated 剩余仍是 AP 零点包、signed payload、same-set PDEC "
            "及若干全局输入的无条件化，不是行/列命题闭合。"
        ),
        "next_direct_attack_target": NEXT_TARGET,
        "row_column_unconditional_closed": False,
        "direct_unconditional_contradiction_found": False,
        "source_hashes": {
            "experiments/prime_matrix_terminal_square_phase_downstream_frontier_sync_router.py": sha256(
                Path(__file__).resolve()
            ),
            "data/prime-matrix-terminal-square-phase-downstream-frontier-sync-ledger.json": sha256(
                OUT_LEDGER
            ),
            **{row["json"]: row["sha256"] for row in rows},
        },
    }
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    return result


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix terminal-square downstream frontier sync router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"frontier_file_count={agg['frontier_file_count']}",
        f"square_phase_longblock_synced_downstream={str(agg['square_phase_longblock_synced_downstream']).lower()}",
        f"row_column_unconditional_closed={str(agg['row_column_unconditional_closed']).lower()}",
        "```",
        "",
        "## 1. 同步表",
        "",
        "| label | role | status | remaining/status |",
        "| --- | --- | --- | --- |",
    ]
    for row in result["frontier_sync_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    table_cell(row["label"]),
                    table_cell(row["role"]),
                    table_cell(row["status"]),
                    table_cell(row["remaining_or_status"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 2. Consolidated 剩余基",
            "",
            "| remaining input |",
            "| --- |",
        ]
    )
    for item in agg["current_consolidated_remaining_basis"]:
        lines.append(f"| `{table_cell(item)}` |")
    lines.extend(
        [
            "",
            "## 3. 命题行",
            "",
            "| name | status | statement |",
            "| --- | --- | --- |",
        ]
    )
    for row in result["theorem_rows"]:
        lines.append(
            f"| `{table_cell(row['name'])}` | `{table_cell(row['status'])}` | {table_cell(row['statement'])} |"
        )
    lines.extend(
        [
            "",
            "## 4. 决策表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | ---: | ---: | --- | --- |",
        ]
    )
    for row in result["decision_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(row['gate'])}`",
                    str(row["closed"]).lower(),
                    str(row["proved"]).lower(),
                    table_cell(row["meaning"]),
                    table_cell(row["remaining"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 5. 结论边界",
            "",
            "- 本步只做前沿同步与口径纠偏。",
            "- 不能把 downstream frontier 的存在误读为行/列命题已闭合。",
            "- 下一步应直接攻击 consolidated 剩余基中的 AP 零点包、signed payload 或 same-set PDEC 输入。",
            "",
            "## 6. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for file_name, digest in result["source_hashes"].items():
        lines.append(f"| `{table_cell(file_name)}` | `{digest}` |")
    return "\n".join(lines) + "\n"


def main() -> None:
    """命令行入口。"""
    result = build_result()
    print(json.dumps(result["aggregate"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
