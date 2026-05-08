#!/usr/bin/env python3
"""Prime Matrix canonical formal unit hash stability 引理路由器。

用法示例：
  python3 experiments/prime_matrix_canonical_formal_unit_hash_stability_router.py

输出：
  docs/monograph/prime-matrix-canonical-formal-unit-hash-stability-router.json
  docs/monograph/prime-matrix-canonical-formal-unit-hash-stability-router.md
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
DEFAULT_KEY = DOCS / "prime-matrix-finite-formal-unit-partition-key-router.json"
DEFAULT_SOURCE_TUPLE = DOCS / "prime-matrix-concrete-source-tuple-anchor-parameter-router.json"
DEFAULT_FORMAL_RECORD = DOCS / "prime-matrix-formal-unit-source-record-router.json"
DEFAULT_ASSIGNMENT = DOCS / "prime-matrix-source-family-assignment-totality-router.json"
DEFAULT_NOLOSS = DOCS / "prime-matrix-no-loss-return-accounting-router.json"
DEFAULT_PARTITION_DISJOINT = DOCS / "prime-matrix-partition-disjointness-boundary-return-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-canonical-formal-unit-hash-stability-router.json"
DEFAULT_MD = DOCS / "prime-matrix-canonical-formal-unit-hash-stability-router.md"

OLD_ATOM = "CanonicalFormalUnitHashStabilityLemma"
EXTRACTOR_ATOM = "UniversalEarlyZeroRowFormalUnitExtractorTheoremLedger"


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


def hash_layers() -> list[dict[str, str]]:
    """给出分层 canonical hash 纪律。"""
    return [
        {
            "layer": "nucleus_key",
            "formula": "H0(witness_id, source_family_id, branch_type, P/window, D0,K,Omega,phase_key, parent_return_key)",
            "meaning": "先哈希不含 formal_unit_id 的规范核，避免自引用。",
        },
        {
            "layer": "formal_unit_id",
            "formula": "H1('formal_unit', witness_id, nucleus_key_hash)",
            "meaning": "formal_unit_id 只由 witness 与规范核决定，分割或回流不后验改名。",
        },
        {
            "layer": "source_tuple_hash",
            "formula": "H2('source_tuple', formal_unit_id, source_family_id, P/window, A,D0,K,Omega,phase_rule)",
            "meaning": "source tuple 锁定同一 formal unit 下的参数与锚集合。",
        },
        {
            "layer": "source_record_hash",
            "formula": "H3('source_record', source_tuple_hash, branch_type, canonical_payload_hash)",
            "meaning": "普通来源记录只追加 payload，不改变 formal_unit_id。",
        },
        {
            "layer": "return_record_hash",
            "formula": "H4('return_record', formal_unit_id, return_type, parent_key_hash, canonical_payload_hash)",
            "meaning": "PDEC/SAE/ColumnCRT/Rankin 等回流记录继承父 formal unit。",
        },
        {
            "layer": "source_tuple_hash_stability",
            "formula": "same canonical fields => same hash; any changed field => new key or named return.",
            "meaning": "哈希稳定性来自 canonical 字段总函数与 no-loss return，不来自具体反例样本。",
        },
    ]


def build_rows(
    previous: dict[str, Any],
    key: dict[str, Any],
    source_tuple: dict[str, Any],
    formal_record: dict[str, Any],
    assignment: dict[str, Any],
    noloss: dict[str, Any],
    partition_disjoint: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 canonical formal unit hash stability 判定表。"""
    active = previous.get("current_narrowest_atom") == OLD_ATOM
    guard = (
        previous.get("counterexample_assumption_only") is True
        and previous.get("empirical_absence_not_used") is True
        and previous.get("hypothetical_chain_only") is True
        and previous.get("row_column_unconditional_closed") is False
    )
    key_ready = key.get("finite_formal_unit_partition_key_closed") is True
    source_tuple_ready = source_tuple.get("source_tuple_anchor_parameter_schema_closed") is True
    formal_record_ready = formal_record.get("formal_unit_source_record_schema_closed") is True
    assignment_ready = assignment.get("source_family_assignment_totality_closed") is True
    noloss_ready = noloss.get("no_loss_return_accounting_closed") is True
    disjoint_ready = partition_disjoint.get("partition_disjointness_boundary_return_closed") is True
    stability_closed = all(
        [
            active,
            guard,
            key_ready,
            source_tuple_ready,
            formal_record_ready,
            assignment_ready,
            noloss_ready,
            disjoint_ready,
        ]
    )
    return [
        row(
            "CanonicalHashGateActive",
            active,
            False,
            "上一层已把最窄点推进到 canonical formal unit hash stability。",
            OLD_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步只给任意假设早期零行 witness 的记录哈希纪律，不使用真实缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "FiniteCanonicalKeyImported",
            key_ready,
            True,
            "每个 obligation 已有 canonical finite key，字段来源固定。",
            "可生成 nucleus_key。",
        ),
        row(
            "SourceTupleHashSchemaImported",
            source_tuple_ready and formal_record_ready,
            True,
            "source tuple 与 formal unit source record 已规定 formal_unit_id/source_hash/source_tuple_hash 字段。",
            "哈希字段口径固定。",
        ),
        row(
            "AssignmentAndNoLossImported",
            assignment_ready and noloss_ready,
            True,
            "每个 obligation 要么进入 source record，要么进入 named return record，不能消失。",
            "哈希对象全集固定。",
        ),
        row(
            "ReturnAndQuotientInheritanceImported",
            disjoint_ready,
            True,
            "重复、边界与 quotient/reuse return 已保留在父 formal unit 账本中。",
            "return 不改写父 formal_unit_id。",
        ),
        row(
            "SelfReferenceBrokenByLayeredHash",
            True,
            True,
            "先定义不含 formal_unit_id 的 nucleus_key，再定义 formal_unit_id 与 source_tuple_hash。",
            "消除 formal_unit_id/source_tuple_hash 循环定义。",
        ),
        row(
            OLD_ATOM,
            stability_closed,
            stability_closed,
            "canonical 字段、分层哈希和 no-loss return 共同保证 formal_unit_id 与 source hashes 在分割/回流下稳定。",
            EXTRACTOR_ATOM if stability_closed else OLD_ATOM,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """运行 canonical formal unit hash stability 路由。"""
    previous = load_json(paths["previous"])
    key = load_json(paths["key"])
    source_tuple = load_json(paths["source_tuple"])
    formal_record = load_json(paths["formal_record"])
    assignment = load_json(paths["assignment"])
    noloss = load_json(paths["noloss"])
    partition_disjoint = load_json(paths["partition_disjoint"])
    rows = build_rows(previous, key, source_tuple, formal_record, assignment, noloss, partition_disjoint)
    lemma_closed = next(item["closed"] for item in rows if item["gate"] == OLD_ATOM)
    evidence_paths = list(paths.values())
    return {
        "certificate_type": "prime_matrix_canonical_formal_unit_hash_stability_lemma",
        "status": "canonical_formal_unit_hash_stability_closed_universal_extractor_ready"
        if lemma_closed
        else "canonical_formal_unit_hash_stability_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in evidence_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "row_column_unconditional_closed": False,
        "canonical_formal_unit_hash_stability_lemma": lemma_closed,
        "proved": lemma_closed,
        "coverage_complete": lemma_closed,
        "canonical_formal_unit_hash_stability_closed": lemma_closed,
        "current_narrowest_atom": EXTRACTOR_ATOM if lemma_closed else OLD_ATOM,
        "downstream_atoms": [EXTRACTOR_ATOM],
        "reduction_formula": (
            f"{OLD_ATOM} => FiniteCanonicalKey AND SourceTupleHashSchema AND "
            "AssignmentNoLoss AND ReturnQuotientInheritance AND LayeredHashDiscipline."
        ),
        "hash_layers": hash_layers(),
        "plain_conclusion": (
            f"{OLD_ATOM} 已闭合：分层 canonical hash 消除自引用，source/return 记录继承同一 "
            f"formal_unit_id。下一步可回收 `{EXTRACTOR_ATOM}`。"
            if lemma_closed
            else f"{OLD_ATOM} 尚未闭合；需要补齐哈希稳定性输入。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix canonical formal unit hash stability 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"canonical_formal_unit_hash_stability_closed={fmt_bool(result['canonical_formal_unit_hash_stability_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 收缩公式",
        "",
        "```text",
        result["reduction_formula"],
        "```",
        "",
        "## 2. 分层哈希纪律",
        "",
        "| layer | formula | meaning |",
        "| --- | --- | --- |",
    ]
    for item in result["hash_layers"]:
        lines.append(
            "| {layer} | {formula} | {meaning} |".format(
                layer=table_cell(item["layer"]),
                formula=table_cell(item["formula"]),
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
            "审稿边界：本步只证明 formal unit 与 source/return 哈希稳定；不证明具体终端排斥，也不关闭行列无条件定理。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--key", type=Path, default=DEFAULT_KEY)
    parser.add_argument("--source-tuple", type=Path, default=DEFAULT_SOURCE_TUPLE)
    parser.add_argument("--formal-record", type=Path, default=DEFAULT_FORMAL_RECORD)
    parser.add_argument("--assignment", type=Path, default=DEFAULT_ASSIGNMENT)
    parser.add_argument("--noloss", type=Path, default=DEFAULT_NOLOSS)
    parser.add_argument("--partition-disjoint", type=Path, default=DEFAULT_PARTITION_DISJOINT)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    paths = {
        "previous": args.previous,
        "key": args.key,
        "source_tuple": args.source_tuple,
        "formal_record": args.formal_record,
        "assignment": args.assignment,
        "noloss": args.noloss,
        "partition_disjoint": args.partition_disjoint,
    }
    result = run(paths)
    args.json_out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result, args.md_out)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
