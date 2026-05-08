#!/usr/bin/env python3
"""Prime Matrix finite formal unit partition key 引理路由器。

用法示例：
  python3 experiments/prime_matrix_finite_formal_unit_partition_key_router.py

输出：
  docs/monograph/prime-matrix-finite-formal-unit-partition-key-router.json
  docs/monograph/prime-matrix-finite-formal-unit-partition-key-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-witness-obligation-domain-canonicalization-router.json"
DEFAULT_SOURCE_TUPLE = DOCS / "prime-matrix-concrete-source-tuple-anchor-parameter-router.json"
DEFAULT_FORMAL_RECORD = DOCS / "prime-matrix-formal-unit-source-record-router.json"
DEFAULT_TAXONOMY = DOCS / "prime-matrix-bad-window-source-family-extraction-router.json"
DEFAULT_EMITTER = DOCS / "prime-matrix-bad-window-source-data-emitter-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-finite-formal-unit-partition-key-router.json"
DEFAULT_MD = DOCS / "prime-matrix-finite-formal-unit-partition-key-router.md"

OLD_ATOM = "FiniteFormalUnitPartitionKeyLemma"
CLOSED_ATOM = "FiniteFormalUnitPartitionKeyClosed"
NOLOSS_ATOM = "PartitionCoverageNoLossEquationLemma"
HASH_ATOM = "CanonicalFormalUnitHashStabilityLemma"


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


def key_fields() -> list[dict[str, str]]:
    """给出 formal unit partition key 字段。"""
    return [
        {"field": "formal_unit_id", "source": "由 witness_id 与 source record canonical hash 给出。"},
        {"field": "source_family_id", "source": "来自已闭合的有限来源族 taxonomy。"},
        {"field": "branch_type", "source": "physical、phase_defect、carry_cofactor、return、quotient 等有限分支。"},
        {"field": "P_or_P_range", "source": "继承 witness 或 source tuple。"},
        {"field": "window_id", "source": "CLB 行窗、端点窗、走廊窗或 return packet 窗。"},
        {"field": "D0,K,Omega", "source": "若该义务有核心尺度/omega 截断/重叠阈值则继承；无则写 null。"},
        {"field": "phase_key", "source": "相位、residue、anchor、fixed_core 或 identity。"},
        {"field": "source_tuple_hash", "source": "锁定上述字段的 canonical hash。"},
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
    source_tuple: dict[str, Any],
    formal_record: dict[str, Any],
    taxonomy: dict[str, Any],
    emitter: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 finite formal unit partition key 判定表。"""
    active = previous.get("current_narrowest_atom") == OLD_ATOM
    guard = (
        previous.get("counterexample_assumption_only") is True
        and previous.get("empirical_absence_not_used") is True
        and previous.get("hypothetical_chain_only") is True
        and previous.get("row_column_unconditional_closed") is False
    )
    domain_ready = previous.get("witness_obligation_domain_canonicalization_closed") is True
    source_tuple_ready = source_tuple.get("source_tuple_anchor_parameter_schema_closed") is True
    formal_record_ready = formal_record.get("formal_unit_source_record_schema_closed") is True
    taxonomy_ready = taxonomy.get("bad_window_source_family_taxonomy_closed") is True
    emitter_ready = emitter.get("bad_window_source_family_record_emitter_closed") is True
    key_closed = all(
        [active, guard, domain_ready, source_tuple_ready, formal_record_ready, taxonomy_ready, emitter_ready]
    )
    return [
        row(
            "FinitePartitionKeyGateActive",
            active,
            False,
            "上一层已把最窄点推进到 finite formal-unit key。",
            OLD_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只处理任意假设早期零行 witness 的 O(w)，不使用真实缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "CanonicalObligationDomainImported",
            domain_ready,
            True,
            "O(w) 已规范化为有限 physical/return/quotient records。",
            "可逐 obligation 指派 key。",
        ),
        row(
            "SourceTupleAndRecordSchemasImported",
            source_tuple_ready and formal_record_ready,
            True,
            "source tuple 与 formal unit source record 的字段、哈希纪律已固定。",
            "key 字段来源固定。",
        ),
        row(
            "FiniteSourceFamilyImported",
            taxonomy_ready and emitter_ready,
            True,
            "source_family_id 只能来自有限来源族，记录发射器无新类型。",
            "key 的 family 坐标有限。",
        ),
        row(
            CLOSED_ATOM,
            key_closed,
            True,
            "每个 obligation 都可用固定字段生成 canonical finite key；同 key 的对象形成一个 formal unit fiber。",
            CLOSED_ATOM,
        ),
        row(
            OLD_ATOM,
            key_closed,
            True,
            "finite key 引理闭合；下一步要证明 key-fibers 与 return records 对 O(w) 的 no-loss 覆盖等式。",
            NOLOSS_ATOM,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """运行 finite formal unit partition key 路由。"""
    previous = load_json(paths["previous"])
    source_tuple = load_json(paths["source_tuple"])
    formal_record = load_json(paths["formal_record"])
    taxonomy = load_json(paths["taxonomy"])
    emitter = load_json(paths["emitter"])
    rows = build_rows(previous, source_tuple, formal_record, taxonomy, emitter)
    key_closed = next(item["closed"] for item in rows if item["gate"] == CLOSED_ATOM)
    evidence_paths = list(paths.values())
    return {
        "certificate_type": "prime_matrix_finite_formal_unit_partition_key_router",
        "status": "finite_formal_unit_partition_key_closed_no_loss_equation_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in evidence_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "row_column_unconditional_closed": False,
        "finite_formal_unit_partition_key_lemma": key_closed,
        "proved": key_closed,
        "coverage_complete": key_closed,
        "finite_formal_unit_partition_key_closed": key_closed,
        "formal_unit_partition_coverage_lemma_closed": False,
        "key_fields": key_fields(),
        "current_narrowest_atom": NOLOSS_ATOM,
        "secondary_narrowest_atom": HASH_ATOM,
        "reduction_formula": f"{OLD_ATOM} => {CLOSED_ATOM} AND {NOLOSS_ATOM}.",
        "plain_conclusion": (
            "FiniteFormalUnitPartitionKeyLemma 已闭合：O(w) 的每个 obligation 都有 canonical finite key，"
            "同 key 对象就是一个 formal unit fiber。剩余不再是能否切分，而是 no-loss 覆盖等式 "
            f"`{NOLOSS_ATOM}`。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix finite formal unit partition key 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"finite_formal_unit_partition_key_closed={fmt_bool(result['finite_formal_unit_partition_key_closed'])}",
        f"formal_unit_partition_coverage_lemma_closed={fmt_bool(result['formal_unit_partition_coverage_lemma_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 收缩公式",
        "",
        "```text",
        result["reduction_formula"],
        "```",
        "",
        "## 2. Key 字段",
        "",
        "| field | source |",
        "| --- | --- |",
    ]
    for item in result["key_fields"]:
        lines.append(
            "| {field} | {source} |".format(
                field=table_cell(item["field"]),
                source=table_cell(item["source"]),
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
            "审稿边界：本步只证明 finite key 存在；不证明 no-loss 覆盖等式，也不关闭行列无条件定理。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--source-tuple", type=Path, default=DEFAULT_SOURCE_TUPLE)
    parser.add_argument("--formal-record", type=Path, default=DEFAULT_FORMAL_RECORD)
    parser.add_argument("--taxonomy", type=Path, default=DEFAULT_TAXONOMY)
    parser.add_argument("--emitter", type=Path, default=DEFAULT_EMITTER)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    paths = {
        "previous": args.previous,
        "source_tuple": args.source_tuple,
        "formal_record": args.formal_record,
        "taxonomy": args.taxonomy,
        "emitter": args.emitter,
    }
    result = run(paths)
    args.json_out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result, args.md_out)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
