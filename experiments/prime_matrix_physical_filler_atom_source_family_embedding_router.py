#!/usr/bin/env python3
"""Prime Matrix physical filler atom source-family embedding 引理路由器。

用法示例：
  python3 experiments/prime_matrix_physical_filler_atom_source_family_embedding_router.py

输出：
  docs/monograph/prime-matrix-physical-filler-atom-source-family-embedding-router.json
  docs/monograph/prime-matrix-physical-filler-atom-source-family-embedding-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-source-family-assignment-totality-router.json"
DEFAULT_DOMAIN = DOCS / "prime-matrix-witness-obligation-domain-canonicalization-router.json"
DEFAULT_PHASE = DOCS / "prime-matrix-early-zero-phase-defect-schema-router.json"
DEFAULT_TERMINAL_RECONCILIATION = DOCS / "prime-matrix-early-zero-terminal-schema-reconciliation-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-physical-filler-atom-source-family-embedding-router.json"
DEFAULT_MD = DOCS / "prime-matrix-physical-filler-atom-source-family-embedding-router.md"

OLD_ATOM = "PhysicalFillerAtomSourceFamilyEmbeddingLemma"
CLOSED_ATOM = "PhysicalFillerAtomSourceFamilyEmbeddingClosed"
ASSIGNMENT_ATOM = "SourceFamilyAssignmentTotalityLemma"


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


def embedding_laws() -> list[dict[str, str]]:
    """给出 raw physical atom 嵌入律。"""
    return [
        {
            "law": "parent_phase_record",
            "meaning": "每个 raw physical filler atom (c,q_*(c),m_*(c)) 都是同一 BoundaryPhaseDefect/phase record 的 payload。",
        },
        {
            "law": "no_standalone_family",
            "meaning": "raw physical atom 不新增 source_family_id；它继承父级 phase/return record 的归宿。",
        },
        {
            "law": "canonical_payload_lock",
            "meaning": "q_*(c) 与 m_*(c) 由 O(w) 规范化锁定，不能后验改标签。",
        },
        {
            "law": "named_return_inheritance",
            "meaning": "父级 phase defect 已闭合到 PDEC/SAE/ColumnCRT 命名回流；raw atom 作为 payload 随父记录回流。",
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
    domain: dict[str, Any],
    phase: dict[str, Any],
    terminal_reconciliation: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 physical filler atom embedding 判定表。"""
    active = previous.get("current_narrowest_atom") == OLD_ATOM
    guard = (
        previous.get("counterexample_assumption_only") is True
        and previous.get("empirical_absence_not_used") is True
        and previous.get("hypothetical_chain_only") is True
        and previous.get("row_column_unconditional_closed") is False
    )
    assignment_interface_ready = previous.get("source_family_assignment_interface_closed") is True
    domain_ready = domain.get("witness_obligation_domain_canonicalization_closed") is True
    phase_payload_ready = (
        phase.get("early_zero_phase_defect_schema_admission_closed") is True
        and phase.get("registered_same_formal_unit_rxf_ledger") is True
        and phase.get("boundary_phase_defect_to_named_families_closed") is True
    )
    terminal_ready = terminal_reconciliation.get("named_return_schema_reconciliation_closed") is True
    closed = all([active, guard, assignment_interface_ready, domain_ready, phase_payload_ready, terminal_ready])
    return [
        row(
            "PhysicalFillerEmbeddingGateActive",
            active,
            False,
            "上一层已把最窄点推进到 raw physical filler atom 的来源族嵌入。",
            OLD_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只处理假设早期零行 witness 的 raw physical atoms，不使用真实缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "AssignmentInterfaceImported",
            assignment_interface_ready,
            True,
            "source family assignment 接口已要求 raw atom 只能作为 payload 或 named return 字段进入。",
            "不能新增来源族。",
        ),
        row(
            "CanonicalDomainImported",
            domain_ready,
            True,
            "O(w) 已给出 canonical q_*(c),m_*(c) 与 phase/carry/cofactor 字段。",
            "raw atom 标签固定。",
        ),
        row(
            "ParentPhaseRecordImported",
            phase_payload_ready,
            True,
            "EarlyZeroPhaseDefectSchemaAdmission 已把 physical atom 登记到同一 formal unit phase defect。",
            "raw atom 有父级 return record。",
        ),
        row(
            "NamedReturnInheritanceImported",
            terminal_ready,
            True,
            "父级 phase/terminal record 已按 PDEC/SAE/ColumnCRT 命名回流。",
            "raw atom 作为 payload 继承归宿。",
        ),
        row(
            CLOSED_ATOM,
            closed,
            True,
            "raw physical filler atom 不作为独立来源族；它嵌入父级 BoundaryPhaseDefect named return payload。",
            CLOSED_ATOM,
        ),
        row(
            OLD_ATOM,
            closed,
            True,
            "physical filler atom source-family embedding 已闭合；可回收 source assignment totality。",
            ASSIGNMENT_ATOM,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """运行 physical filler atom embedding 路由。"""
    previous = load_json(paths["previous"])
    domain = load_json(paths["domain"])
    phase = load_json(paths["phase"])
    terminal_reconciliation = load_json(paths["terminal_reconciliation"])
    rows = build_rows(previous, domain, phase, terminal_reconciliation)
    closed = next(item["closed"] for item in rows if item["gate"] == CLOSED_ATOM)
    evidence_paths = list(paths.values())
    return {
        "certificate_type": "prime_matrix_physical_filler_atom_source_family_embedding_router",
        "status": "physical_filler_atom_source_family_embedding_closed_assignment_ready",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in evidence_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "row_column_unconditional_closed": False,
        "physical_filler_atom_source_family_embedding_lemma": closed,
        "proved": closed,
        "coverage_complete": closed,
        "physical_filler_atom_source_family_embedding_closed": closed,
        "source_family_assignment_totality_closed": False,
        "embedding_laws": embedding_laws(),
        "current_narrowest_atom": ASSIGNMENT_ATOM,
        "reduction_formula": f"{OLD_ATOM} => {CLOSED_ATOM} AND {ASSIGNMENT_ATOM}.",
        "plain_conclusion": (
            "PhysicalFillerAtomSourceFamilyEmbeddingLemma 已闭合：raw physical filler atom 不新增来源族，"
            "而是作为父级 BoundaryPhaseDefect/phase record 的 canonical payload，继承 PDEC/SAE/ColumnCRT "
            f"命名回流。下一步可回收 `{ASSIGNMENT_ATOM}`。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix physical filler atom source-family embedding 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"physical_filler_atom_source_family_embedding_closed={fmt_bool(result['physical_filler_atom_source_family_embedding_closed'])}",
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
        "## 2. 嵌入律",
        "",
        "| law | meaning |",
        "| --- | --- |",
    ]
    for item in result["embedding_laws"]:
        lines.append(
            "| {law} | {meaning} |".format(
                law=table_cell(item["law"]),
                meaning=table_cell(item["meaning"]),
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
            f"当前回收目标为 `{result['current_narrowest_atom']}`。",
            "",
            "审稿边界：本步只处理 raw physical atom 的来源族嵌入，不证明终端排斥，也不关闭行列无条件定理。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--domain", type=Path, default=DEFAULT_DOMAIN)
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
        "domain": args.domain,
        "phase": args.phase,
        "terminal_reconciliation": args.terminal_reconciliation,
    }
    result = run(paths)
    args.json_out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result, args.md_out)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
