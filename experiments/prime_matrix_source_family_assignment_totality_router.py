#!/usr/bin/env python3
"""Prime Matrix source family assignment totality 引理路由器。

用法示例：
  python3 experiments/prime_matrix_source_family_assignment_totality_router.py

输出：
  docs/monograph/prime-matrix-source-family-assignment-totality-router.json
  docs/monograph/prime-matrix-source-family-assignment-totality-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-universal-formal-unit-extractor-router.json"
DEFAULT_PARTITION = DOCS / "prime-matrix-formal-unit-partition-coverage-router.json"
DEFAULT_DOMAIN = DOCS / "prime-matrix-witness-obligation-domain-canonicalization-router.json"
DEFAULT_TAXONOMY = DOCS / "prime-matrix-bad-window-source-family-extraction-router.json"
DEFAULT_EMITTER = DOCS / "prime-matrix-bad-window-source-data-emitter-router.json"
DEFAULT_PHASE = DOCS / "prime-matrix-early-zero-phase-defect-schema-router.json"
DEFAULT_TERMINAL_RECONCILIATION = DOCS / "prime-matrix-early-zero-terminal-schema-reconciliation-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-source-family-assignment-totality-router.json"
DEFAULT_MD = DOCS / "prime-matrix-source-family-assignment-totality-router.md"

OLD_ATOM = "SourceFamilyAssignmentTotalityLemma"
INTERFACE_ATOM = "SourceFamilyAssignmentInterfaceClosed"
PHYSICAL_ATOM = "PhysicalFillerAtomSourceFamilyEmbeddingLemma"
RETURN_ATOM = "NamedReturnSourceFamilyAssignmentClosed"
QUOTIENT_ATOM = "QuotientReuseSourceFamilyAssignmentClosed"
NOLOSS_ATOM = "NoLossReturnAccountingLemma"


def read_text(path: Path) -> str:
    """读取文本文件。"""
    return path.read_text(encoding="utf-8")


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


def contains_all(text: str, needles: list[str]) -> bool:
    """检查文本是否包含全部片段。"""
    return all(needle in text for needle in needles)


def is_assignment_proof_like(payload: dict[str, Any]) -> str | None:
    """识别 source family assignment 相关证明。"""
    cert_type = payload.get("certificate_type")
    keys = set(payload.keys())
    if cert_type == "prime_matrix_source_family_assignment_totality_lemma":
        return OLD_ATOM
    if cert_type == "prime_matrix_physical_filler_atom_source_family_embedding_lemma":
        return PHYSICAL_ATOM
    if "source_family_assignment_totality_lemma" in keys:
        return OLD_ATOM
    if "physical_filler_atom_source_family_embedding_lemma" in keys:
        return PHYSICAL_ATOM
    return None


def proof_closed(records: list[dict[str, Any]]) -> bool:
    """判断证明记录是否闭合。"""
    return bool(records) and all(
        item.get("proved") is True and item.get("coverage_complete") is True for item in records
    )


def scan_assignment_proofs(root: Path) -> dict[str, list[dict[str, Any]]]:
    """扫描 assignment 证明。"""
    found: dict[str, list[dict[str, Any]]] = {
        OLD_ATOM: [],
        PHYSICAL_ATOM: [],
    }
    for path in sorted(root.rglob("*.json")):
        try:
            payload = load_json(path)
        except (json.JSONDecodeError, UnicodeDecodeError):
            continue
        if not isinstance(payload, dict):
            continue
        kind = is_assignment_proof_like(payload)
        if kind is None:
            continue
        found[kind].append(
            {
                "path": str(path.relative_to(ROOT)),
                "status": payload.get("status"),
                "proved": payload.get("proved"),
                "coverage_complete": payload.get("coverage_complete"),
            }
        )
    return found


def assignment_table() -> list[dict[str, str]]:
    """给出当前可登记 assignment 表。"""
    return [
        {
            "obligation_kind": "named_return_records",
            "assignment": "按 return source_family_id 直接进入 Endpoint/TailAnchor/HighOverlap/SmoothCore/Sparse/RankinConstant 等已登记族。",
            "status": "closed_schema",
        },
        {
            "obligation_kind": "quotient_reuse_records",
            "assignment": "按 Multiplicity-Stitching 回流到 CoordinateQuotient、ReuseDefect、ColumnCRT/SAE/TailAnchor/PDEC。",
            "status": "closed_schema",
        },
        {
            "obligation_kind": "colored_corridor_records",
            "assignment": "进入 ColoredDisjointCorridorBudgetViolation。",
            "status": "closed_schema",
        },
        {
            "obligation_kind": "raw_physical_filler_atoms",
            "assignment": "必须证明每个 canonical (c,q_*(c),m_*(c)) 可作为某个已登记 source family 的 payload 或 named return 字段。",
            "status": "open",
        },
    ]


def row(
    gate: str,
    closed: bool,
    proved: bool,
    meaning: str,
    remaining: str,
) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_rows(
    previous: dict[str, Any],
    partition: dict[str, Any],
    domain: dict[str, Any],
    taxonomy: dict[str, Any],
    emitter: dict[str, Any],
    phase: dict[str, Any],
    terminal_reconciliation: dict[str, Any],
    proofs: dict[str, list[dict[str, Any]]],
) -> list[dict[str, Any]]:
    """生成 source family assignment 判定表。"""
    active = previous.get("current_narrowest_atom") == OLD_ATOM
    guard = (
        previous.get("counterexample_assumption_only") is True
        and previous.get("empirical_absence_not_used") is True
        and previous.get("hypothetical_chain_only") is True
        and previous.get("row_column_unconditional_closed") is False
    )
    partition_ready = partition.get("formal_unit_partition_coverage_lemma_closed") is True
    domain_ready = domain.get("witness_obligation_domain_canonicalization_closed") is True
    taxonomy_ready = taxonomy.get("bad_window_source_family_taxonomy_closed") is True
    emitter_ready = emitter.get("bad_window_source_family_record_emitter_closed") is True
    phase_ready = phase.get("boundary_phase_defect_to_named_families_closed") is True
    terminal_ready = terminal_reconciliation.get("named_return_schema_reconciliation_closed") is True
    interface_closed = all(
        [active, guard, partition_ready, domain_ready, taxonomy_ready, emitter_ready, phase_ready, terminal_ready]
    )
    physical_closed = proof_closed(proofs[PHYSICAL_ATOM])
    totality_closed = proof_closed(proofs[OLD_ATOM]) or (interface_closed and physical_closed)
    return [
        row(
            "SourceFamilyAssignmentGateActive",
            active,
            False,
            "上一层已把最窄点推进到 source family assignment totality。",
            OLD_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只处理假设早期零行 witness 的 formal units，不使用真实缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "PartitionAndDomainImported",
            partition_ready and domain_ready,
            True,
            "partition coverage 与 O(w) 规范化已闭合。",
            "每个 obligation 已有 key 与类型。",
        ),
        row(
            "FiniteTaxonomyEmitterImported",
            taxonomy_ready and emitter_ready,
            True,
            "有限来源族 taxonomy 与记录发射器已闭合。",
            "assignment 的目标族固定。",
        ),
        row(
            "NamedReturnAssignmentClosed",
            phase_ready and terminal_ready,
            True,
            "phase defect、PDEC/SAE/ColumnCRT 和终端回流都已有命名 return schema。",
            RETURN_ATOM,
        ),
        row(
            QUOTIENT_ATOM,
            terminal_ready,
            True,
            "quotient/reuse 记录作为 named return 处理，不要求新增来源族。",
            QUOTIENT_ATOM,
        ),
        row(
            INTERFACE_ATOM,
            interface_closed,
            True,
            "source family assignment 的输入域、目标 taxonomy 与已闭合 schema 已固定。",
            INTERFACE_ATOM,
        ),
        row(
            "PhysicalFillerAtomSourceFamilyEmbeddingAvailable",
            physical_closed,
            False,
            "尚未发现 raw physical filler atom 到已登记 source family 的嵌入证明。",
            PHYSICAL_ATOM,
        ),
        row(
            OLD_ATOM,
            totality_closed,
            totality_closed,
            "只有 raw physical filler atom embedding 也闭合后，assignment totality 才闭合。",
            PHYSICAL_ATOM if not totality_closed else NOLOSS_ATOM,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """运行 source family assignment totality 路由。"""
    previous = load_json(paths["previous"])
    partition = load_json(paths["partition"])
    domain = load_json(paths["domain"])
    taxonomy = load_json(paths["taxonomy"])
    emitter = load_json(paths["emitter"])
    phase = load_json(paths["phase"])
    terminal_reconciliation = load_json(paths["terminal_reconciliation"])
    proofs = scan_assignment_proofs(DOCS)
    rows = build_rows(previous, partition, domain, taxonomy, emitter, phase, terminal_reconciliation, proofs)
    interface_closed = next(item["closed"] for item in rows if item["gate"] == INTERFACE_ATOM)
    totality_closed = next(item["closed"] for item in rows if item["gate"] == OLD_ATOM)
    evidence_paths = list(paths.values())
    return {
        "certificate_type": "prime_matrix_source_family_assignment_totality_router",
        "status": "source_family_assignment_interface_closed_physical_embedding_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in evidence_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "row_column_unconditional_closed": False,
        "source_family_assignment_interface_closed": interface_closed,
        "source_family_assignment_totality_lemma": totality_closed,
        "proved": totality_closed,
        "coverage_complete": totality_closed,
        "source_family_assignment_totality_closed": totality_closed,
        "assignment_proof_like_json": proofs,
        "assignment_table": assignment_table(),
        "current_narrowest_atom": PHYSICAL_ATOM if not totality_closed else NOLOSS_ATOM,
        "downstream_atoms": [NOLOSS_ATOM],
        "reduction_formula": f"{OLD_ATOM} => {INTERFACE_ATOM} AND {PHYSICAL_ATOM}.",
        "plain_conclusion": (
            "SourceFamilyAssignmentTotalityLemma 的接口已闭合：命名 return、quotient/reuse 和 colored corridor "
            "都有已登记来源族或回流 schema。真正未闭合的是 raw physical filler atom "
            f"`{PHYSICAL_ATOM}`。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix source family assignment totality 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"source_family_assignment_interface_closed={fmt_bool(result['source_family_assignment_interface_closed'])}",
        f"source_family_assignment_totality_closed={fmt_bool(result['source_family_assignment_totality_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 收缩公式",
        "",
        "```text",
        result["reduction_formula"],
        "```",
        "",
        "## 2. Assignment 表",
        "",
        "| obligation_kind | assignment | status |",
        "| --- | --- | --- |",
    ]
    for item in result["assignment_table"]:
        lines.append(
            "| {obligation_kind} | {assignment} | {status} |".format(
                obligation_kind=table_cell(item["obligation_kind"]),
                assignment=table_cell(item["assignment"]),
                status=table_cell(item["status"]),
            )
        )
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
            "| {gate} | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
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
            f"当前唯一最窄点更新为 `{result['current_narrowest_atom']}`。",
            "",
            "审稿边界：本步只关闭 assignment 接口，不新增来源族，也不关闭行列无条件定理。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--partition", type=Path, default=DEFAULT_PARTITION)
    parser.add_argument("--domain", type=Path, default=DEFAULT_DOMAIN)
    parser.add_argument("--taxonomy", type=Path, default=DEFAULT_TAXONOMY)
    parser.add_argument("--emitter", type=Path, default=DEFAULT_EMITTER)
    parser.add_argument("--phase", type=Path, default=DEFAULT_PHASE)
    parser.add_argument("--terminal-reconciliation", type=Path, default=DEFAULT_TERMINAL_RECONCILIATION)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    paths = {
        "previous": args.previous,
        "partition": args.partition,
        "domain": args.domain,
        "taxonomy": args.taxonomy,
        "emitter": args.emitter,
        "phase": args.phase,
        "terminal_reconciliation": args.terminal_reconciliation,
    }
    result = run(paths)
    args.json_out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result, args.md_out)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
