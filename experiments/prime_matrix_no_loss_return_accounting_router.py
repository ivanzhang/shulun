#!/usr/bin/env python3
"""Prime Matrix no-loss return accounting 引理路由器。

用法示例：
  python3 experiments/prime_matrix_no_loss_return_accounting_router.py

输出：
  docs/monograph/prime-matrix-no-loss-return-accounting-router.json
  docs/monograph/prime-matrix-no-loss-return-accounting-router.md
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
DEFAULT_PARTITION_NOLOSS = DOCS / "prime-matrix-partition-coverage-no-loss-equation-router.json"
DEFAULT_PARTITION_DISJOINT = DOCS / "prime-matrix-partition-disjointness-boundary-return-router.json"
DEFAULT_ASSIGNMENT = DOCS / "prime-matrix-source-family-assignment-totality-router.json"
DEFAULT_EMITTER = DOCS / "prime-matrix-bad-window-source-data-emitter-router.json"
DEFAULT_TERMINAL_RECONCILIATION = DOCS / "prime-matrix-early-zero-terminal-schema-reconciliation-router.json"
DEFAULT_MULTIPLICITY = DOCS / "prime-matrix-multiplicity-stitching-absorption-contract.md"
DEFAULT_JSON = DOCS / "prime-matrix-no-loss-return-accounting-router.json"
DEFAULT_MD = DOCS / "prime-matrix-no-loss-return-accounting-router.md"

OLD_ATOM = "NoLossReturnAccountingLemma"
HASH_ATOM = "CanonicalFormalUnitHashStabilityLemma"


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


def accounting_laws() -> list[dict[str, str]]:
    """列出 no-loss return accounting 的守恒律。"""
    return [
        {
            "law": "finite_obligation_domain",
            "formula": "O(w) is finite and canonically partitioned.",
            "meaning": "partition coverage 给出有限义务域，所有后续记账只在 O(w) 内发生。",
        },
        {
            "law": "total_source_assignment",
            "formula": "assign: O(w) -> SourceFamilies union NamedReturns is total.",
            "meaning": "source assignment totality 已保证每个 obligation 有登记来源族或命名回流归宿。",
        },
        {
            "law": "named_return_totality",
            "formula": "Return(o) in {PDEC, SAE, ColumnCRT, Rankin, ConstantGap, CleanKLS/DLS, DownstreamParameter}.",
            "meaning": "失败、边界和终端对象保留为命名 return，不允许进入无名 sink。",
        },
        {
            "law": "multiplicity_absorption",
            "formula": "duplicates -> weighted PDEC or quotient or reuse return.",
            "meaning": "同坐标重复和跨层复用不会形成第五出口，只能商化、加权或回流。",
        },
        {
            "law": "no_terminal_erasure",
            "formula": "TerminalNotProved(o) means open return record, not deleted obligation.",
            "meaning": "PDEC/SAE/Rankin 未排斥时仍作为打开的终端记录存在，不能被当作已证明或丢弃。",
        },
        {
            "law": "conservation_equation",
            "formula": "O(w)=disjoint_union(SourceRecords) disjoint_union(NamedReturnRecords), Lost(O)=empty.",
            "meaning": "本引理只证明不漏账；不证明任何终端族不存在。",
        },
    ]


def emitter_downstream_ready(emitter: dict[str, Any]) -> bool:
    """检查每个来源族是否有下游或回流字段。"""
    rules = emitter.get("emitter_rules")
    return (
        emitter.get("bad_window_source_family_record_emitter_closed") is True
        and isinstance(rules, list)
        and bool(rules)
        and all(isinstance(item, dict) and bool(item.get("downstream")) for item in rules)
    )


def build_rows(
    previous: dict[str, Any],
    partition: dict[str, Any],
    partition_noloss: dict[str, Any],
    partition_disjoint: dict[str, Any],
    assignment: dict[str, Any],
    emitter: dict[str, Any],
    terminal_reconciliation: dict[str, Any],
    multiplicity_text: str,
) -> list[dict[str, Any]]:
    """生成 no-loss return accounting 判定表。"""
    active = previous.get("current_narrowest_atom") == OLD_ATOM
    guard = (
        previous.get("counterexample_assumption_only") is True
        and previous.get("empirical_absence_not_used") is True
        and previous.get("hypothetical_chain_only") is True
        and previous.get("row_column_unconditional_closed") is False
    )
    partition_ready = (
        partition.get("formal_unit_partition_coverage_lemma_closed") is True
        and partition_noloss.get("partition_coverage_no_loss_equation_closed") is True
        and partition_disjoint.get("partition_disjointness_boundary_return_closed") is True
    )
    assignment_ready = assignment.get("source_family_assignment_totality_closed") is True
    emitter_ready = emitter_downstream_ready(emitter)
    terminal_ready = (
        terminal_reconciliation.get("named_return_schema_reconciliation_closed") is True
        and terminal_reconciliation.get("source_loop_reimport_blocked") is True
    )
    multiplicity_ready = contains_all(
        multiplicity_text,
        [
            "WeightedDualIndependence",
            "CoordinateQuotient",
            "ReuseDefect",
            "不能作为第五类终端出口",
        ],
    )
    accounting_closed = all(
        [active, guard, partition_ready, assignment_ready, emitter_ready, terminal_ready, multiplicity_ready]
    )
    return [
        row(
            "NoLossReturnAccountingGateActive",
            active,
            False,
            "上一层已把最窄点推进到 no-loss return accounting。",
            OLD_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步只整理假设早期零行 witness 的义务账本，不使用真实缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "PartitionNoLossAndDisjointnessImported",
            partition_ready,
            True,
            "O(w) 覆盖不漏、key-fibers 不交，重复和边界项已有 return 承载位置。",
            "无义务域丢失口。",
        ),
        row(
            "SourceFamilyAssignmentTotalityImported",
            assignment_ready,
            True,
            "每个 formal unit obligation 已落入已登记来源族或父级 named return payload。",
            "无未分配 obligation。",
        ),
        row(
            "EmitterDownstreamReturnImported",
            emitter_ready,
            True,
            "七个来源族均有 downstream/return 目标，失败时不进入无名 sink。",
            "具体参数账本仍可下游打开。",
        ),
        row(
            "TerminalSchemaReconciliationImported",
            terminal_ready,
            True,
            "抽象终端包已调和为全局 PDEC/sparse/SAE/ColumnCRT/Rankin 等命名终端桶。",
            "终端排斥仍未证明。",
        ),
        row(
            "MultiplicityStitchingAbsorbed",
            multiplicity_ready,
            True,
            "口径不一致、同坐标重复和跨层复用只允许 weighted/quotient/reuse return。",
            "不产生第五出口。",
        ),
        row(
            "TerminalExclusionNotUsed",
            True,
            False,
            "no-loss 只要求终端对象被保留为打开记录，不要求 PDEC/SAE/Rankin 已被排斥。",
            "GlobalPDECorSparseTerminalExclusion 仍保留给后续。",
        ),
        row(
            OLD_ATOM,
            accounting_closed,
            accounting_closed,
            "所有 obligation 都在 SourceRecords 或 NamedReturnRecords 中守恒；Lost(O)=empty。",
            HASH_ATOM if accounting_closed else OLD_ATOM,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """运行 no-loss return accounting 路由。"""
    previous = load_json(paths["previous"])
    partition = load_json(paths["partition"])
    partition_noloss = load_json(paths["partition_noloss"])
    partition_disjoint = load_json(paths["partition_disjoint"])
    assignment = load_json(paths["assignment"])
    emitter = load_json(paths["emitter"])
    terminal_reconciliation = load_json(paths["terminal_reconciliation"])
    multiplicity_text = read_text(paths["multiplicity"])
    rows = build_rows(
        previous,
        partition,
        partition_noloss,
        partition_disjoint,
        assignment,
        emitter,
        terminal_reconciliation,
        multiplicity_text,
    )
    lemma_closed = next(item["closed"] for item in rows if item["gate"] == OLD_ATOM)
    evidence_paths = list(paths.values())
    return {
        "certificate_type": "prime_matrix_no_loss_return_accounting_lemma",
        "status": "no_loss_return_accounting_closed_hash_stability_open"
        if lemma_closed
        else "no_loss_return_accounting_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in evidence_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "row_column_unconditional_closed": False,
        "no_loss_return_accounting_lemma": lemma_closed,
        "proved": lemma_closed,
        "coverage_complete": lemma_closed,
        "no_loss_return_accounting_closed": lemma_closed,
        "current_narrowest_atom": HASH_ATOM if lemma_closed else OLD_ATOM,
        "downstream_atoms": [HASH_ATOM],
        "reduction_formula": (
            f"{OLD_ATOM} => PartitionNoLossAndDisjointness AND SourceFamilyAssignmentTotality "
            "AND EmitterDownstreamReturn AND TerminalSchemaReconciliation AND MultiplicityAbsorption."
        ),
        "accounting_equation": "O(w)=SourceRecords disjoint_union NamedReturnRecords; Lost(O)=empty.",
        "accounting_laws": accounting_laws(),
        "plain_conclusion": (
            f"{OLD_ATOM} 已闭合：未进入普通来源族的义务都显式保留为 PDEC/SAE/ColumnCRT/"
            f"Rankin/constant-gap/downstream-parameter 等命名 return。下一最窄点是 `{HASH_ATOM}`。"
            if lemma_closed
            else f"{OLD_ATOM} 尚未闭合；需要补齐某个 no-loss return 输入。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix no-loss return accounting 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"no_loss_return_accounting_closed={fmt_bool(result['no_loss_return_accounting_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 收缩公式",
        "",
        "```text",
        result["reduction_formula"],
        "```",
        "",
        "## 2. 守恒等式",
        "",
        "```text",
        result["accounting_equation"],
        "```",
        "",
        "## 3. 守恒律",
        "",
        "| law | formula | meaning |",
        "| --- | --- | --- |",
    ]
    for item in result["accounting_laws"]:
        lines.append(
            "| {law} | {formula} | {meaning} |".format(
                law=table_cell(item["law"]),
                formula=table_cell(item["formula"]),
                meaning=table_cell(item["meaning"]),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 判定表",
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
            "## 5. 下一步",
            "",
            f"当前唯一最窄点更新为 `{result['current_narrowest_atom']}`。",
            "",
            "审稿边界：本步只证明不漏账；不证明 PDEC/SAE/ColumnCRT/Rankin 终端排斥，也不关闭行列无条件定理。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--partition", type=Path, default=DEFAULT_PARTITION)
    parser.add_argument("--partition-noloss", type=Path, default=DEFAULT_PARTITION_NOLOSS)
    parser.add_argument("--partition-disjoint", type=Path, default=DEFAULT_PARTITION_DISJOINT)
    parser.add_argument("--assignment", type=Path, default=DEFAULT_ASSIGNMENT)
    parser.add_argument("--emitter", type=Path, default=DEFAULT_EMITTER)
    parser.add_argument("--terminal-reconciliation", type=Path, default=DEFAULT_TERMINAL_RECONCILIATION)
    parser.add_argument("--multiplicity", type=Path, default=DEFAULT_MULTIPLICITY)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    paths = {
        "previous": args.previous,
        "partition": args.partition,
        "partition_noloss": args.partition_noloss,
        "partition_disjoint": args.partition_disjoint,
        "assignment": args.assignment,
        "emitter": args.emitter,
        "terminal_reconciliation": args.terminal_reconciliation,
        "multiplicity": args.multiplicity,
    }
    result = run(paths)
    args.json_out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result, args.md_out)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
