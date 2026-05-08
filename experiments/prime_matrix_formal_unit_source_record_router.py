#!/usr/bin/env python3
"""Prime Matrix formal unit 源记录路由器。

用法示例：
  python3 experiments/prime_matrix_formal_unit_source_record_router.py

输出：
  docs/monograph/prime-matrix-formal-unit-source-record-router.json
  docs/monograph/prime-matrix-formal-unit-source-record-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONOGRAPH = DOCS / "monograph"

DEFAULT_PREVIOUS = MONOGRAPH / "prime-matrix-concrete-source-tuple-anchor-parameter-router.json"
DEFAULT_TAXONOMY = MONOGRAPH / "prime-matrix-bad-window-source-family-extraction-router.json"
DEFAULT_EMITTER = MONOGRAPH / "prime-matrix-bad-window-source-data-emitter-router.json"
DEFAULT_JSON = MONOGRAPH / "prime-matrix-formal-unit-source-record-router.json"
DEFAULT_MD = MONOGRAPH / "prime-matrix-formal-unit-source-record-router.md"

OLD_ATOM = "ConcreteFormalUnitSourceRecordLedger"
SCHEMA_ATOM = "FormalUnitSourceRecordSchemaClosed"
EXTRACTOR_ATOM = "UniversalEarlyZeroRowFormalUnitExtractorTheoremLedger"
PARTITION_ATOM = "FormalUnitPartitionCoverageLemma"
ANCHOR_RECON_ATOM = "AnchorSetReconstructionCertificateLedger"


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


def is_formal_unit_record_like(payload: dict[str, Any]) -> bool:
    """判断 JSON 是否像 formal unit 源记录数据。"""
    cert_type = payload.get("certificate_type")
    keys = set(payload.keys())
    if cert_type in {
        "prime_matrix_concrete_formal_unit_source_records",
        "prime_matrix_universal_formal_unit_extractor_certificate",
    }:
        return True
    return bool(
        {
            "formal_unit_source_records",
            "concrete_formal_unit_records",
            "bad_window_source_records",
            "universal_formal_unit_extractor_records",
        }
        & keys
    )


def count_records(payload: dict[str, Any]) -> int | None:
    """读取记录数量。"""
    for key in [
        "formal_unit_source_records",
        "concrete_formal_unit_records",
        "bad_window_source_records",
        "universal_formal_unit_extractor_records",
    ]:
        value = payload.get(key)
        if isinstance(value, list):
            return len(value)
        if isinstance(value, dict):
            return len(value)
    return None


def scan_formal_unit_records(root: Path) -> list[dict[str, Any]]:
    """扫描 formal unit 源记录数据。"""
    found: list[dict[str, Any]] = []
    for path in sorted(root.rglob("*.json")):
        if "__pycache__" in path.parts:
            continue
        try:
            payload = load_json(path)
        except (json.JSONDecodeError, UnicodeDecodeError):
            continue
        if not isinstance(payload, dict) or not is_formal_unit_record_like(payload):
            continue
        found.append(
            {
                "path": str(path.relative_to(ROOT)),
                "status": payload.get("status"),
                "record_count": count_records(payload),
                "coverage_complete": payload.get("coverage_complete"),
                "universal_extractor_proved": payload.get("universal_extractor_proved"),
            }
        )
    return found


def required_theorem_clauses() -> list[dict[str, str]]:
    """给出普遍抽取定理的必要子句。"""
    return [
        {
            "clause": "witness_input",
            "meaning": "输入任意假设早期零行 witness，例如 (P,n,row_signature)，而不是使用真实零行缺席。",
        },
        {
            "clause": "finite_partition",
            "meaning": "把 witness 诱导的窗口、端点、尾锚、核心与走廊分成有限 formal units。",
        },
        {
            "clause": "source_family_assignment",
            "meaning": "每个 formal unit 必须落入已闭合 taxonomy 的有限 source_family_id。",
        },
        {
            "clause": "coverage_no_loss",
            "meaning": "所有坏窗/走廊义务要么被某个 formal unit 覆盖，要么显式回流 PDEC/SAE/Rankin。",
        },
        {
            "clause": "same_unit_hash",
            "meaning": "每条记录输出 canonical formal_unit_id 和 source_hash，供下游 A、D0、phase 重构。",
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
    taxonomy: dict[str, Any],
    emitter: dict[str, Any],
    records: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """生成 formal unit 源记录判定表。"""
    active = previous.get("current_narrowest_atom") == OLD_ATOM
    guard = (
        previous.get("counterexample_assumption_only") is True
        and previous.get("empirical_absence_not_used") is True
        and previous.get("hypothetical_chain_only") is True
        and previous.get("row_column_unconditional_closed") is False
    )
    source_tuple_schema_ready = previous.get("source_tuple_anchor_parameter_schema_closed") is True
    taxonomy_ready = taxonomy.get("bad_window_source_family_taxonomy_closed") is True
    emitter_ready = emitter.get("bad_window_source_family_record_emitter_closed") is True
    schema_closed = all([active, guard, source_tuple_schema_ready, taxonomy_ready, emitter_ready])
    data_available = bool(records)
    data_complete = data_available and all(item.get("coverage_complete") is True for item in records)
    universal_extractor_proved = data_available and all(
        item.get("universal_extractor_proved") is True for item in records
    )
    return [
        row(
            "ConcreteFormalUnitSourceRecordGateActive",
            active,
            False,
            "上一层已把最窄点推进到 concrete formal unit 源记录。",
            OLD_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只在假设早期零行分支内工作，不使用真实缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "UpstreamSourceSchemasImported",
            source_tuple_schema_ready and taxonomy_ready and emitter_ready,
            True,
            "source tuple schema、来源族 taxonomy 和记录发射器均已闭合。",
            "无来源类型剩余。",
        ),
        row(
            SCHEMA_ATOM,
            schema_closed,
            True,
            "formal unit source record 的输入、输出字段和 coverage/no-loss 义务已固定。",
            SCHEMA_ATOM,
        ),
        row(
            "ConcreteFormalUnitSourceRecordDataAvailable",
            data_available,
            False,
            "仓库尚未发现逐 formal unit 的 concrete source record 数据。",
            OLD_ATOM,
        ),
        row(
            "ConcreteFormalUnitSourceRecordDataComplete",
            data_complete,
            False,
            "固定数据若存在，必须覆盖全部假设反例链诱导的 formal units。",
            OLD_ATOM,
        ),
        row(
            "UniversalExtractorTheoremAvailable",
            universal_extractor_proved,
            False,
            "反证路线真正需要的是任意早期零行 witness 到 formal unit records 的普遍抽取定理。",
            EXTRACTOR_ATOM,
        ),
        row(
            OLD_ATOM,
            False,
            False,
            "没有实际反例数据时，ledger 只能由 universal extractor theorem 关闭；该定理尚未提交。",
            EXTRACTOR_ATOM,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """运行 formal unit 源记录路由。"""
    previous = load_json(paths["previous"])
    taxonomy = load_json(paths["taxonomy"])
    emitter = load_json(paths["emitter"])
    records = scan_formal_unit_records(DOCS)
    rows = build_rows(previous, taxonomy, emitter, records)
    schema_closed = next(item["closed"] for item in rows if item["gate"] == SCHEMA_ATOM)
    evidence_paths = list(paths.values())
    return {
        "certificate_type": "prime_matrix_formal_unit_source_record_router",
        "status": "formal_unit_source_record_schema_closed_universal_extractor_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in evidence_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "row_column_unconditional_closed": False,
        "formal_unit_source_record_schema_closed": schema_closed,
        "concrete_formal_unit_source_record_closed": False,
        "formal_unit_record_like_json": records,
        "required_theorem_clauses": required_theorem_clauses(),
        "current_narrowest_atom": EXTRACTOR_ATOM,
        "secondary_narrowest_atom": PARTITION_ATOM,
        "downstream_atoms": [ANCHOR_RECON_ATOM],
        "reduction_formula": f"{OLD_ATOM} => {SCHEMA_ATOM} AND {EXTRACTOR_ATOM}.",
        "plain_conclusion": (
            "ConcreteFormalUnitSourceRecordLedger 的 schema 层已闭合，但反证路线不能依赖真实反例数据。"
            "因此剩余被改写成普遍抽取输入：必须证明任意早期零行 witness 都能产生有限、无漏、同 formal unit "
            f"的 source records。新的最窄点是 `{EXTRACTOR_ATOM}`。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix formal unit 源记录路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"formal_unit_source_record_schema_closed={fmt_bool(result['formal_unit_source_record_schema_closed'])}",
        f"concrete_formal_unit_source_record_closed={fmt_bool(result['concrete_formal_unit_source_record_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 收缩公式",
        "",
        "```text",
        result["reduction_formula"],
        "```",
        "",
        "## 2. 普遍抽取定理子句",
        "",
        "| clause | meaning |",
        "| --- | --- |",
    ]
    for item in result["required_theorem_clauses"]:
        lines.append(
            "| {clause} | {meaning} |".format(
                clause=table_cell(item["clause"]),
                meaning=table_cell(item["meaning"]),
            )
        )
    lines.extend(
        [
            "",
            "## 3. 当前扫描",
            "",
            f"- formal-unit-record-like JSON: `{len(result['formal_unit_record_like_json'])}`",
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
            f"当前唯一最窄点更新为 `{result['current_narrowest_atom']}`；其内部第一子门是 "
            f"`{result['secondary_narrowest_atom']}`。",
            "",
            "审稿边界：本步没有证明普遍抽取定理，也没有关闭 PDEC/SAE、Rankin 或行列无条件定理。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
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
        "taxonomy": args.taxonomy,
        "emitter": args.emitter,
    }
    result = run(paths)
    args.json_out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result, args.md_out)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
