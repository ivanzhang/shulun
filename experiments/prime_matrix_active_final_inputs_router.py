#!/usr/bin/env python3
"""Prime Matrix 当前活跃最终输入归约路由器。

用法示例：
  python3 experiments/prime_matrix_active_final_inputs_router.py

输出：
  docs/monograph/prime-matrix-active-final-inputs-router.json
  docs/monograph/prime-matrix-active-final-inputs-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_FIREWALL = DOCS / "prime-matrix-final-input-firewall-boundary-router.json"
DEFAULT_THREE_ATOMS = DOCS / "prime-matrix-three-final-atoms-hard-attack-router.json"
DEFAULT_PDEC = DOCS / "prime-matrix-pdec-family-explicit-input-boundary-router.json"
DEFAULT_SPARSE = DOCS / "prime-matrix-future-sparse-packet-extractor-schema-boundary-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-active-final-inputs-router.json"
DEFAULT_MD = DOCS / "prime-matrix-active-final-inputs-router.md"

NONCANONICAL_ATOM = "NoncanonicalTwoLaneMathInput"
DSTRUCTURE_ATOM = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
PDEC_FUTURE = "FutureExplicitPrimitivePDECSchema"
SPARSE_FUTURE = "FutureExplicitSparsePacketExtractorSchema"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算文件 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(
    gate: str,
    active_now: bool,
    boundary_closed: bool,
    proved_or_accepted: bool,
    meaning: str,
    remaining: str,
) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "active_now": active_now,
        "boundary_closed": boundary_closed,
        "proved_or_accepted": proved_or_accepted,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_rows(
    firewall: dict[str, Any],
    three_atoms: dict[str, Any],
    pdec: dict[str, Any],
    sparse: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成当前活跃最终输入判定表。"""
    current_frontier_zero = firewall.get("current_materialized_terminal_frontier_closed") is True
    pdec_inactive = (
        pdec.get("pdec_family_explicit_input_boundary_closed") is True
        and pdec.get("current_materialized_pdec_frontier_closed") is True
        and pdec.get("global_pdec_family_unconditional_closed") is False
    )
    sparse_inactive = (
        sparse.get("future_sparse_packet_schema_boundary_closed") is True
        and sparse.get("current_materialized_sparse_frontier_closed") is True
        and sparse.get("global_sparse_family_unconditional_closed") is False
    )
    choices = three_atoms.get("mathematical_final_choice", [])
    noncanonical_active = (
        three_atoms.get("three_atom_attack_boundary_closed") is True
        and len(choices) == 2
        and three_atoms.get("all_three_atoms_proved_or_accepted") is False
    )
    dstructure_active = (
        three_atoms.get("promotion_final_atom") == DSTRUCTURE_ATOM
        and three_atoms.get("row_column_unconditional_closed") is False
    )
    return [
        row(
            "CurrentMaterializedPDECSparseFrontierZero",
            False,
            current_frontier_zero,
            True,
            "当前已物化 PDEC/sparse 终端前沿清零；它们不是当前活跃硬点。",
            "若未来新增实例，才触发显式 schema。",
        ),
        row(
            PDEC_FUTURE,
            False,
            pdec_inactive,
            False,
            "PDEC future schema 是防火墙义务，不是当前已有待排斥对象。",
            "new materialized PDEC family only if proposed",
        ),
        row(
            SPARSE_FUTURE,
            False,
            sparse_inactive,
            False,
            "Sparse future schema 是防火墙义务，不是当前已有待排斥对象。",
            "new materialized sparse route only if proposed",
        ),
        row(
            NONCANONICAL_ATOM,
            noncanonical_active,
            noncanonical_active,
            False,
            "当前数学硬点是 noncanonical 二选一：实际源反原子，或 c-dependent 完成型谱抵消。",
            "ActualFullSNonAPSourceCapacityAntiAtomForActualSource OR CDependentResidueWeightSpectralCancellationInput",
        ),
        row(
            DSTRUCTURE_ATOM,
            dstructure_active,
            dstructure_active,
            False,
            "最终晋级硬点是 DStructure/Tail-log4/finite verification/Rankin 子账本的独立接受。",
            "independent promotion acceptance",
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行当前活跃最终输入归约。"""
    firewall = load_json(paths["firewall"])
    three_atoms = load_json(paths["three_atoms"])
    pdec = load_json(paths["pdec"])
    sparse = load_json(paths["sparse"])
    rows = build_rows(firewall, three_atoms, pdec, sparse)
    active_rows = [item for item in rows if item["active_now"]]
    active_inputs = [item["gate"] for item in active_rows]
    inactive_future_inputs = [
        item["gate"] for item in rows if not item["active_now"] and item["gate"].startswith("Future")
    ]
    return {
        "certificate_type": "prime_matrix_active_final_inputs_router",
        "status": "active_final_inputs_reduced_to_noncanonical_math_plus_dstructure_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "row_column_unconditional_closed": False,
        "active_final_inputs_boundary_closed": all(item["boundary_closed"] for item in rows),
        "all_active_final_inputs_proved_or_accepted": all(
            item["proved_or_accepted"] for item in active_rows
        ),
        "currently_active_final_inputs": active_inputs,
        "inactive_unless_new_materialization": inactive_future_inputs,
        "mathematical_narrowest_atom": NONCANONICAL_ATOM,
        "promotion_narrowest_atom": DSTRUCTURE_ATOM,
        "minimum_unconditional_basis": three_atoms.get("minimum_unconditional_basis"),
        "next_priority": NONCANONICAL_ATOM,
        "parallel_acceptance_priority": DSTRUCTURE_ATOM,
        "reduction_formula": (
            "FinalOpenInputs = inactive_future_schema(PDEC,sparse) + "
            "(ActualFullSNonAPSourceCapacityAntiAtomForActualSource OR "
            "CDependentResidueWeightSpectralCancellationInput) + "
            "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance."
        ),
        "plain_conclusion": (
            "最终开放输入已收窄：PDEC 与 sparse 只是未来新增实例时的显式 schema 防火墙，"
            "当前没有已物化对象可攻。现在真正活跃的最终输入只剩 noncanonical 二选一数学输入，"
            "另加 DStructure/Rankin 晋级独立验收；完整无条件闭合仍未成立。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["boundary_closed"]],
        "open_active_gates": [
            item["gate"] for item in active_rows if not item["proved_or_accepted"]
        ],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix 当前活跃最终输入归约路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"active_final_inputs_boundary_closed={fmt_bool(result['active_final_inputs_boundary_closed'])}",
        f"all_active_final_inputs_proved_or_accepted={fmt_bool(result['all_active_final_inputs_proved_or_accepted'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 收缩公式",
        "",
        "```text",
        result["reduction_formula"],
        "```",
        "",
        "## 2. 判定表",
        "",
        "| gate | active_now | boundary_closed | proved_or_accepted | meaning | remaining |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for item in result["rows"]:
        lines.append(
            "| {gate} | `{active}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=table_cell(item["gate"]),
                active=fmt_bool(item["active_now"]),
                closed=fmt_bool(item["boundary_closed"]),
                proved=fmt_bool(item["proved_or_accepted"]),
                meaning=table_cell(item["meaning"]),
                remaining=table_cell(item["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 3. 下一步",
            "",
            f"数学最窄点：`{result['mathematical_narrowest_atom']}`。",
            f"并行晋级验收点：`{result['promotion_narrowest_atom']}`。",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--firewall", type=Path, default=DEFAULT_FIREWALL)
    parser.add_argument("--three-atoms", type=Path, default=DEFAULT_THREE_ATOMS)
    parser.add_argument("--pdec", type=Path, default=DEFAULT_PDEC)
    parser.add_argument("--sparse", type=Path, default=DEFAULT_SPARSE)
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "firewall": args.firewall,
        "three_atoms": args.three_atoms,
        "pdec": args.pdec,
        "sparse": args.sparse,
    }
    result = run(paths)
    args.json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_markdown(result, args.md)
    print(f"wrote {args.json}")
    print(f"wrote {args.md}")


if __name__ == "__main__":
    main()
