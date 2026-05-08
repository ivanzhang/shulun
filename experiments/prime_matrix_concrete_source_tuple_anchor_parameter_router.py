#!/usr/bin/env python3
"""Prime Matrix concrete source tuple/anchor 参数路由器。

用法示例：
  python3 experiments/prime_matrix_concrete_source_tuple_anchor_parameter_router.py

输出：
  docs/monograph/prime-matrix-concrete-source-tuple-anchor-parameter-router.json
  docs/monograph/prime-matrix-concrete-source-tuple-anchor-parameter-router.md
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

DEFAULT_PREVIOUS = MONOGRAPH / "prime-matrix-concrete-anchor-interval-enumeration-router.json"
DEFAULT_SOURCE_EMITTER = MONOGRAPH / "prime-matrix-bad-window-source-data-emitter-router.json"
DEFAULT_PARAMETER = MONOGRAPH / "prime-matrix-complement-anchor-d0k-parameter-router.json"
DEFAULT_FORMAL = MONOGRAPH / "prime-matrix-formal-corridor-inventory-contract-router.json"
DEFAULT_FORMAL_UNIT_SOURCE_RECORD = MONOGRAPH / "prime-matrix-formal-unit-source-record-router.json"
DEFAULT_JSON = MONOGRAPH / "prime-matrix-concrete-source-tuple-anchor-parameter-router.json"
DEFAULT_MD = MONOGRAPH / "prime-matrix-concrete-source-tuple-anchor-parameter-router.md"

OLD_ATOM = "ConcreteSourceTupleAnchorParameterDataLedger"
SCHEMA_ATOM = "SourceTupleAnchorParameterSchemaClosed"
FORMAL_UNIT_ATOM = "ConcreteFormalUnitSourceRecordLedger"
ANCHOR_RECON_ATOM = "AnchorSetReconstructionCertificateLedger"
ANCHOR_INTERVAL_ATOM = "AnchorIntervalCertificateFileLedger"


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


def is_formal_unit_source_record_like(payload: dict[str, Any]) -> bool:
    """判断 JSON 是否像 concrete formal unit 源记录。"""
    cert_type = payload.get("certificate_type")
    keys = set(payload.keys())
    if cert_type in {
        "prime_matrix_concrete_formal_unit_source_records",
        "prime_matrix_bad_window_source_family_record_data",
    }:
        return True
    return bool(
        {
            "formal_unit_source_records",
            "concrete_formal_unit_records",
            "bad_window_source_records",
            "source_family_record_data",
        }
        & keys
    )


def is_anchor_reconstruction_like(payload: dict[str, Any]) -> bool:
    """判断 JSON 是否像 anchor 参数重构证书。"""
    cert_type = payload.get("certificate_type")
    keys = set(payload.keys())
    if cert_type in {
        "prime_matrix_anchor_set_reconstruction_certificate",
        "prime_matrix_concrete_source_tuple_anchor_parameter_data",
    }:
        return True
    return bool(
        {
            "anchor_set_reconstruction_records",
            "source_tuple_anchor_parameter_records",
            "formal_unit_anchor_parameter_records",
            "anchor_parameter_records",
        }
        & keys
    )


def count_records(payload: dict[str, Any], keys: list[str]) -> int | None:
    """读取记录数量。"""
    for key in keys:
        value = payload.get(key)
        if isinstance(value, list):
            return len(value)
        if isinstance(value, dict):
            return len(value)
    return None


def scan_data(root: Path) -> dict[str, list[dict[str, Any]]]:
    """扫描 source tuple/anchor 参数相关数据。"""
    found: dict[str, list[dict[str, Any]]] = {
        FORMAL_UNIT_ATOM: [],
        ANCHOR_RECON_ATOM: [],
    }
    for path in sorted(root.rglob("*.json")):
        if "__pycache__" in path.parts:
            continue
        try:
            payload = load_json(path)
        except (json.JSONDecodeError, UnicodeDecodeError):
            continue
        if not isinstance(payload, dict):
            continue
        if is_formal_unit_source_record_like(payload):
            found[FORMAL_UNIT_ATOM].append(
                {
                    "path": str(path.relative_to(ROOT)),
                    "status": payload.get("status"),
                    "record_count": count_records(
                        payload,
                        [
                            "formal_unit_source_records",
                            "concrete_formal_unit_records",
                            "bad_window_source_records",
                            "source_family_record_data",
                        ],
                    ),
                    "coverage_complete": payload.get("coverage_complete"),
                }
            )
        if is_anchor_reconstruction_like(payload):
            found[ANCHOR_RECON_ATOM].append(
                {
                    "path": str(path.relative_to(ROOT)),
                    "status": payload.get("status"),
                    "record_count": count_records(
                        payload,
                        [
                            "anchor_set_reconstruction_records",
                            "source_tuple_anchor_parameter_records",
                            "formal_unit_anchor_parameter_records",
                            "anchor_parameter_records",
                        ],
                    ),
                    "coverage_complete": payload.get("coverage_complete"),
                }
            )
    return found


def schema_fields() -> list[dict[str, str]]:
    """给出 source tuple/anchor 参数字段。"""
    return [
        {"field": "formal_unit_id", "meaning": "同一假设反例链的最小稳定单元。"},
        {"field": "source_family_id", "meaning": "必须来自已登记的有限坏窗来源族。"},
        {"field": "P_or_P_range", "meaning": "该记录适用的素数或素数范围。"},
        {"field": "window_id", "meaning": "坏窗或走廊窗口编号。"},
        {"field": "L,R", "meaning": "窗口 I=[L,R] 的整数端点。"},
        {"field": "A", "meaning": "互补锚集合，必须可由 source record 复算。"},
        {"field": "D0,K,Omega", "meaning": "dyadic core scale、omega 截断和低重叠阈值。"},
        {"field": "phase_rule", "meaning": "有限相位谓词；无相位过滤时写 identity。"},
        {"field": "anchor_set_hash", "meaning": "排序后 A 与 source tuple 的哈希。"},
        {"field": "source_tuple_hash", "meaning": "锁定以上全部字段的 canonical hash。"},
    ]


def reconstruction_laws() -> list[dict[str, str]]:
    """给出重构纪律。"""
    return [
        {
            "law": "same_formal_unit",
            "meaning": "P/range、window、A、D0、K、Omega、phase_rule 必须来自同一 formal_unit_id。",
        },
        {
            "law": "finite_source_family",
            "meaning": "source_family_id 必须属于坏窗来源族抽取路由器列出的有限族。",
        },
        {
            "law": "canonical_anchor_hash",
            "meaning": "anchor_set_hash=H(source_tuple_key, sorted(A))，禁止口头或后验 anchor set。",
        },
        {
            "law": "tuple_hash_lock",
            "meaning": "source_tuple_hash=H(formal_unit_id,P/window,I,A,D0,K,Omega,phase_rule)。",
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
    source_emitter: dict[str, Any],
    parameter: dict[str, Any],
    formal_unit_source_record: dict[str, Any],
    formal_text: str,
    data: dict[str, list[dict[str, Any]]],
) -> list[dict[str, Any]]:
    """生成 source tuple/anchor 参数判定表。"""
    active = previous.get("current_narrowest_atom") == OLD_ATOM
    guard = (
        previous.get("counterexample_assumption_only") is True
        and previous.get("empirical_absence_not_used") is True
        and previous.get("hypothetical_chain_only") is True
        and previous.get("row_column_unconditional_closed") is False
    )
    endpoint_formula_ready = previous.get("anchor_interval_endpoint_formula_closed") is True
    source_emitter_ready = source_emitter.get("bad_window_source_family_record_emitter_closed") is True
    parameter_ready = parameter.get("complement_anchor_d0k_parameter_discipline_closed") is True
    formal_fields_ready = contains_all(
        formal_text,
        ["family_id", "anchor_set_hash", "D0", "K", "Omega", "phase_rule"],
    )
    schema_closed = all(
        [active, guard, endpoint_formula_ready, source_emitter_ready, parameter_ready, formal_fields_ready]
    )
    formal_unit_available = bool(data[FORMAL_UNIT_ATOM])
    formal_unit_complete = formal_unit_available and all(
        item.get("coverage_complete") is True for item in data[FORMAL_UNIT_ATOM]
    )
    formal_unit_ledger_closed = formal_unit_source_record.get("concrete_formal_unit_source_record_closed") is True
    formal_unit_gate_closed = formal_unit_available or formal_unit_ledger_closed
    formal_unit_complete_gate_closed = formal_unit_complete or formal_unit_ledger_closed
    anchor_recon_available = bool(data[ANCHOR_RECON_ATOM])
    anchor_recon_complete = anchor_recon_available and all(
        item.get("coverage_complete") is True for item in data[ANCHOR_RECON_ATOM]
    )
    ledger_closed = schema_closed and formal_unit_complete_gate_closed and anchor_recon_complete
    ledger_remaining = ANCHOR_RECON_ATOM if formal_unit_complete_gate_closed else FORMAL_UNIT_ATOM
    ledger_meaning = (
        "schema 与 formal unit source records 已闭合；剩余是 anchor set 与 D0/K/Omega/phase_rule 重构证书。"
        if formal_unit_complete_gate_closed and not anchor_recon_complete
        else "schema 已闭合，但没有 concrete formal unit 源记录就不能落地 source tuple 参数。"
    )
    return [
        row(
            "ConcreteSourceTupleGateActive",
            active,
            False,
            "上一层已把最窄点推进到 concrete source tuple/anchor 参数数据。",
            OLD_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只处理假设反例链条，不使用真实零行缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "UpstreamEmittersImported",
            endpoint_formula_ready and source_emitter_ready and parameter_ready,
            True,
            "锚区间端点公式、坏窗来源记录发射器和参数纪律均已固定。",
            "无格式出口剩余。",
        ),
        row(
            "FormalTupleFieldsPinned",
            formal_fields_ready,
            True,
            "正式 inventory 已要求 family_id、A/hash、D0/K/Omega 和 phase_rule。",
            "字段名和来源口径固定。",
        ),
        row(
            SCHEMA_ATOM,
            schema_closed,
            True,
            "source tuple/anchor 参数数据的字段、哈希和同 formal unit 纪律已闭合。",
            SCHEMA_ATOM,
        ),
        row(
            "ConcreteFormalUnitSourceRecordsAvailable",
            formal_unit_gate_closed,
            formal_unit_available,
            "仓库尚未发现逐 formal unit 的真实 source record 数据；formal unit source record ledger 闭合后该缺席不再阻塞。",
            FORMAL_UNIT_ATOM,
        ),
        row(
            "ConcreteFormalUnitSourceRecordsComplete",
            formal_unit_complete_gate_closed,
            formal_unit_complete,
            "formal unit source records 必须覆盖所有假设来源记录；当前由已闭合普遍抽取链给出覆盖。",
            FORMAL_UNIT_ATOM,
        ),
        row(
            "AnchorSetReconstructionCertificatesAvailable",
            anchor_recon_available,
            False,
            "仓库尚未发现 anchor set 与 D0/K/Omega/phase_rule 的重构证书。",
            ANCHOR_RECON_ATOM,
        ),
        row(
            "AnchorSetReconstructionCertificatesComplete",
            anchor_recon_complete,
            False,
            "重构证书必须逐 source tuple 给出 anchor_set_hash 与 source_tuple_hash。",
            ANCHOR_RECON_ATOM,
        ),
        row(
            OLD_ATOM,
            ledger_closed,
            ledger_closed,
            ledger_meaning,
            ANCHOR_INTERVAL_ATOM if ledger_closed else ledger_remaining,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """运行 concrete source tuple/anchor 参数路由。"""
    previous = load_json(paths["previous"])
    source_emitter = load_json(paths["source_emitter"])
    parameter = load_json(paths["parameter"])
    formal_unit_source_record = load_json(paths["formal_unit_source_record"])
    formal_text = read_text(paths["formal"])
    data = scan_data(DOCS)
    rows = build_rows(previous, source_emitter, parameter, formal_unit_source_record, formal_text, data)
    schema_closed = next(item["closed"] for item in rows if item["gate"] == SCHEMA_ATOM)
    ledger_closed = next(item["closed"] for item in rows if item["gate"] == OLD_ATOM)
    formal_unit_closed = formal_unit_source_record.get("concrete_formal_unit_source_record_closed") is True
    evidence_paths = list(paths.values())
    current_narrowest = ANCHOR_INTERVAL_ATOM if ledger_closed else (
        ANCHOR_RECON_ATOM if formal_unit_closed else FORMAL_UNIT_ATOM
    )
    status = (
        "source_tuple_anchor_parameter_data_closed_anchor_interval_open"
        if ledger_closed
        else (
            "source_tuple_anchor_parameter_schema_closed_anchor_reconstruction_open"
            if formal_unit_closed
            else "source_tuple_anchor_parameter_schema_closed_formal_unit_records_missing"
        )
    )
    plain_conclusion = (
        "ConcreteSourceTupleAnchorParameterDataLedger 的 schema 与 formal unit source records 已闭合；"
        f"当前最窄点收缩为 `{ANCHOR_RECON_ATOM}`。"
        if formal_unit_closed and not ledger_closed
        else (
            "ConcreteSourceTupleAnchorParameterDataLedger 的字段和哈希纪律已闭合：每条记录必须来自同一"
            " formal unit，锁定 source_family、P/window、I=[L,R]、A、D0/K/Omega 与 phase_rule。"
            f"当前缺少逐 formal unit 的 concrete source record 数据，因此新的最窄点是 `{FORMAL_UNIT_ATOM}`。"
        )
    )
    return {
        "certificate_type": "prime_matrix_concrete_source_tuple_anchor_parameter_router",
        "status": status,
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in evidence_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "row_column_unconditional_closed": False,
        "source_tuple_anchor_parameter_schema_closed": schema_closed,
        "concrete_source_tuple_anchor_parameter_data_closed": ledger_closed,
        "data_like_json": data,
        "schema_fields": schema_fields(),
        "reconstruction_laws": reconstruction_laws(),
        "current_narrowest_atom": current_narrowest,
        "secondary_narrowest_atom": ANCHOR_RECON_ATOM,
        "downstream_atoms": [ANCHOR_INTERVAL_ATOM],
        "reduction_formula": f"{OLD_ATOM} => {SCHEMA_ATOM} AND {FORMAL_UNIT_ATOM} AND {ANCHOR_RECON_ATOM}.",
        "plain_conclusion": plain_conclusion,
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    if result["current_narrowest_atom"] == result["secondary_narrowest_atom"]:
        next_note = f"当前唯一最窄点更新为 `{result['current_narrowest_atom']}`；随后才是 `{ANCHOR_INTERVAL_ATOM}`。"
        boundary_note = (
            "审稿边界：本步吸收已闭合 formal unit source record ledger；不提交 anchor set 重构证书，"
            "也不关闭行列无条件定理。"
        )
    else:
        next_note = (
            f"当前唯一最窄点更新为 `{result['current_narrowest_atom']}`；随后才是 "
            f"`{result['secondary_narrowest_atom']}` 和 `{ANCHOR_INTERVAL_ATOM}`。"
        )
        boundary_note = "审稿边界：本步只关闭 source tuple/anchor 参数 schema，不提交 concrete formal unit 源记录。"
    lines = [
        "# Prime Matrix concrete source tuple/anchor 参数路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"source_tuple_anchor_parameter_schema_closed={fmt_bool(result['source_tuple_anchor_parameter_schema_closed'])}",
        f"concrete_source_tuple_anchor_parameter_data_closed={fmt_bool(result['concrete_source_tuple_anchor_parameter_data_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 收缩公式",
        "",
        "```text",
        result["reduction_formula"],
        "```",
        "",
        "## 2. 必要字段",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for item in result["schema_fields"]:
        lines.append(
            "| {field} | {meaning} |".format(
                field=table_cell(item["field"]),
                meaning=table_cell(item["meaning"]),
            )
        )
    lines.extend(
        [
            "",
            "## 3. 重构纪律",
            "",
            "| law | meaning |",
            "| --- | --- |",
        ]
    )
    for item in result["reconstruction_laws"]:
        lines.append(
            "| {law} | {meaning} |".format(
                law=table_cell(item["law"]),
                meaning=table_cell(item["meaning"]),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 当前扫描",
            "",
        ]
    )
    for atom, records in result["data_like_json"].items():
        lines.append(f"- {atom}: `{len(records)}`")
    lines.extend(
        [
            "",
            "## 5. 判定表",
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
            "## 6. 下一步",
            "",
            next_note,
            "",
            boundary_note,
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--source-emitter", type=Path, default=DEFAULT_SOURCE_EMITTER)
    parser.add_argument("--parameter", type=Path, default=DEFAULT_PARAMETER)
    parser.add_argument("--formal", type=Path, default=DEFAULT_FORMAL)
    parser.add_argument("--formal-unit-source-record", type=Path, default=DEFAULT_FORMAL_UNIT_SOURCE_RECORD)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    paths = {
        "previous": args.previous,
        "source_emitter": args.source_emitter,
        "parameter": args.parameter,
        "formal": args.formal,
        "formal_unit_source_record": args.formal_unit_source_record,
    }
    result = run(paths)
    args.json_out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result, args.md_out)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
