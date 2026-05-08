#!/usr/bin/env python3
"""Prime Matrix concrete 锚区间枚举路由器。

用法示例：
  python3 experiments/prime_matrix_concrete_anchor_interval_enumeration_router.py

输出：
  docs/monograph/prime-matrix-concrete-anchor-interval-enumeration-router.json
  docs/monograph/prime-matrix-concrete-anchor-interval-enumeration-router.md
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

DEFAULT_PREVIOUS = MONOGRAPH / "prime-matrix-concrete-coloring-coverage-data-router.json"
DEFAULT_PARAMETER = MONOGRAPH / "prime-matrix-complement-anchor-d0k-parameter-router.json"
DEFAULT_FORMAL = MONOGRAPH / "prime-matrix-formal-corridor-inventory-contract-router.json"
DEFAULT_SOURCE_TUPLE = MONOGRAPH / "prime-matrix-concrete-source-tuple-anchor-parameter-router.json"
DEFAULT_JSON = MONOGRAPH / "prime-matrix-concrete-anchor-interval-enumeration-router.json"
DEFAULT_MD = MONOGRAPH / "prime-matrix-concrete-anchor-interval-enumeration-router.md"

OLD_ATOM = "ConcreteAnchorIntervalEnumerationLedger"
FORMULA_ATOM = "AnchorIntervalEndpointFormulaClosed"
SOURCE_ATOM = "ConcreteSourceTupleAnchorParameterDataLedger"
CERT_ATOM = "AnchorIntervalCertificateFileLedger"
MULTIPLICITY_ATOM = "LowOverlapMultiplicityTableLedger"


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


def is_source_tuple_anchor_parameter_like(payload: dict[str, Any]) -> bool:
    """判断 JSON 是否像 concrete source tuple/anchor 参数数据。"""
    cert_type = payload.get("certificate_type")
    keys = set(payload.keys())
    if cert_type in {
        "prime_matrix_concrete_source_tuple_anchor_parameter_data",
        "prime_matrix_concrete_formal_unit_anchor_parameter_data",
    }:
        return True
    return bool(
        {
            "concrete_source_tuple_records",
            "source_tuple_anchor_parameter_records",
            "formal_unit_anchor_parameter_records",
            "anchor_parameter_records",
        }
        & keys
    )


def is_anchor_interval_certificate_like(payload: dict[str, Any]) -> bool:
    """判断 JSON 是否像锚区间枚举证书。"""
    cert_type = payload.get("certificate_type")
    keys = set(payload.keys())
    if cert_type == "prime_matrix_concrete_anchor_interval_enumeration_certificate":
        return True
    return bool({"concrete_anchor_interval_records", "anchor_interval_records"} & keys)


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
    """扫描锚区间枚举相关数据。"""
    found: dict[str, list[dict[str, Any]]] = {
        SOURCE_ATOM: [],
        CERT_ATOM: [],
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
        if is_source_tuple_anchor_parameter_like(payload):
            found[SOURCE_ATOM].append(
                {
                    "path": str(path.relative_to(ROOT)),
                    "status": payload.get("status"),
                    "record_count": count_records(
                        payload,
                        [
                            "concrete_source_tuple_records",
                            "source_tuple_anchor_parameter_records",
                            "formal_unit_anchor_parameter_records",
                            "anchor_parameter_records",
                        ],
                    ),
                    "coverage_complete": payload.get("coverage_complete"),
                }
            )
        if is_anchor_interval_certificate_like(payload):
            found[CERT_ATOM].append(
                {
                    "path": str(path.relative_to(ROOT)),
                    "status": payload.get("status"),
                    "record_count": count_records(
                        payload,
                        ["concrete_anchor_interval_records", "anchor_interval_records"],
                    ),
                    "coverage_complete": payload.get("coverage_complete"),
                }
            )
    return found


def certificate_fields() -> list[dict[str, str]]:
    """给出锚区间枚举证书字段。"""
    return [
        {"field": "formal_unit_id", "meaning": "假设反例链中同一 formal unit 的稳定编号。"},
        {"field": "source_tuple_hash", "meaning": "锁定 P/range、window_id、I=[L,R]、A、D0、phase_rule。"},
        {"field": "anchor_id", "meaning": "互补锚 a 的稳定编号。"},
        {"field": "a", "meaning": "实际 anchor 值，必须来自 anchor_set_hash 对应的 A。"},
        {"field": "left_d", "meaning": "max(D0, ceil(L/a))。"},
        {"field": "right_d_exclusive", "meaning": "min(2D0, floor(R/a)+1)，使用半开整数区间。"},
        {"field": "phase_filtered_segments", "meaning": "若 phase_rule 非 identity，记录过滤后的子区间或 residue 条件。"},
        {"field": "empty_interval_flag", "meaning": "若 left_d>=right_d_exclusive，则显式登记空区间。"},
        {"field": "endpoint_proof_hash", "meaning": "端点公式和 source tuple 的可复算证明哈希。"},
    ]


def endpoint_laws() -> list[dict[str, str]]:
    """给出端点公式纪律。"""
    return [
        {
            "law": "window_membership",
            "formula": "ad in [L,R] iff ceil(L/a)<=d<=floor(R/a)。",
        },
        {
            "law": "dyadic_core_clip",
            "formula": "d in [D0,2D0) gives left=max(D0,ceil(L/a)), right_excl=min(2D0,floor(R/a)+1)。",
        },
        {
            "law": "phase_filter",
            "formula": "phase_rule(d)=true 的点保留；identity phase 必须显式写出。",
        },
        {
            "law": "same_tuple_guard",
            "formula": "A、D0、phase_rule、window_id 必须共享同一 source_tuple_hash。",
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
    parameter: dict[str, Any],
    source_tuple: dict[str, Any],
    formal_text: str,
    data: dict[str, list[dict[str, Any]]],
) -> list[dict[str, Any]]:
    """生成锚区间枚举判定表。"""
    active = previous.get("current_narrowest_atom") == OLD_ATOM
    guard = (
        previous.get("counterexample_assumption_only") is True
        and previous.get("empirical_absence_not_used") is True
        and previous.get("hypothetical_chain_only") is True
        and previous.get("row_column_unconditional_closed") is False
    )
    coverage_schema_ready = previous.get("concrete_coloring_coverage_data_schema_closed") is True
    parameter_ready = parameter.get("complement_anchor_d0k_parameter_discipline_closed") is True
    formal_fields_ready = contains_all(formal_text, ["anchor_set_hash", "D0", "phase_rule", "intervals"])
    formula_closed = all([active, guard, coverage_schema_ready, parameter_ready, formal_fields_ready])
    source_data_available = bool(data[SOURCE_ATOM])
    source_data_complete = source_data_available and all(
        item.get("coverage_complete") is True for item in data[SOURCE_ATOM]
    )
    source_tuple_closed = source_tuple.get("concrete_source_tuple_anchor_parameter_data_closed") is True
    source_gate_closed = source_data_available or source_tuple_closed
    source_complete_gate_closed = source_data_complete or source_tuple_closed
    cert_available = bool(data[CERT_ATOM])
    cert_complete = cert_available and all(item.get("coverage_complete") is True for item in data[CERT_ATOM])
    cert_available_meaning = (
        "已发现 anchor interval 证书文件生成律，可按端点公式生成逐锚记录。"
        if cert_available
        else "仓库尚未发现按端点公式生成的 anchor interval 证书文件。"
    )
    cert_complete_meaning = (
        "anchor interval 证书已登记逐锚记录、空锚集、空区间和相位过滤情况。"
        if cert_complete
        else "anchor interval 证书必须逐 anchor 覆盖并携带空区间记录。"
    )
    ledger_closed = formula_closed and source_complete_gate_closed and cert_complete
    ledger_remaining = CERT_ATOM if source_complete_gate_closed else SOURCE_ATOM
    ledger_meaning = (
        "端点公式、source tuple 参数与 anchor interval 证书均已闭合；锚区间枚举账本闭合。"
        if ledger_closed
        else (
            "端点公式与 source tuple 参数已闭合；剩余是按公式生成 anchor interval 证书文件。"
            if source_complete_gate_closed
            else "锚区间枚举公式已闭合，但没有 concrete source tuple 数据就不能生成真实 J_a 清单。"
        )
    )
    return [
        row(
            "ConcreteAnchorIntervalGateActive",
            active,
            False,
            "上一层已把最窄点推进到 concrete anchor interval 枚举。",
            OLD_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只处理假设早期零行反例链，不使用真实零行缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "UpstreamCoverageSchemaImported",
            coverage_schema_ready,
            True,
            "coverage 数据已经被拆为锚区间、多重度、着色执行和覆盖等式。",
            "本步只处理第一组件。",
        ),
        row(
            "ParameterDisciplineImported",
            parameter_ready and formal_fields_ready,
            True,
            "A、D0、phase_rule 与 anchor_set_hash 的来源纪律已固定。",
            "不能后验移动参数。",
        ),
        row(
            FORMULA_ATOM,
            formula_closed,
            True,
            "给定同一 source tuple，J_a 端点由 ceil/floor 与 [D0,2D0) 裁剪唯一确定。",
            FORMULA_ATOM,
        ),
        row(
            "ConcreteSourceTupleAnchorParameterDataAvailable",
            source_gate_closed,
            source_data_available,
            "仓库尚未发现逐 formal unit 的真实 source tuple 参数数据；source tuple 参数账本闭合后该缺席不再阻塞。",
            SOURCE_ATOM,
        ),
        row(
            "ConcreteSourceTupleAnchorParameterDataComplete",
            source_complete_gate_closed,
            source_data_complete,
            "source tuple 数据必须完整覆盖 P/range、window_id、A、D0、phase_rule；当前由上层闭合账本给出覆盖。",
            SOURCE_ATOM,
        ),
        row(
            "AnchorIntervalCertificateFilesAvailable",
            cert_available,
            False,
            cert_available_meaning,
            CERT_ATOM,
        ),
        row(
            "AnchorIntervalCertificateFilesComplete",
            cert_complete,
            False,
            cert_complete_meaning,
            CERT_ATOM,
        ),
        row(
            OLD_ATOM,
            ledger_closed,
            ledger_closed,
            ledger_meaning,
            MULTIPLICITY_ATOM if ledger_closed else ledger_remaining,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """运行 concrete 锚区间枚举路由。"""
    previous = load_json(paths["previous"])
    parameter = load_json(paths["parameter"])
    source_tuple = load_json(paths["source_tuple"])
    formal_text = read_text(paths["formal"])
    data = scan_data(DOCS)
    rows = build_rows(previous, parameter, source_tuple, formal_text, data)
    formula_closed = next(item["closed"] for item in rows if item["gate"] == FORMULA_ATOM)
    ledger_closed = next(item["closed"] for item in rows if item["gate"] == OLD_ATOM)
    source_tuple_closed = source_tuple.get("concrete_source_tuple_anchor_parameter_data_closed") is True
    evidence_paths = list(paths.values())
    for records in data.values():
        evidence_paths.extend(ROOT / item["path"] for item in records)
    evidence_paths = list(dict.fromkeys(evidence_paths))
    current_narrowest = MULTIPLICITY_ATOM if ledger_closed else (CERT_ATOM if source_tuple_closed else SOURCE_ATOM)
    status = (
        "anchor_interval_enumeration_closed_multiplicity_open"
        if ledger_closed
        else (
            "anchor_interval_formula_closed_certificate_file_open"
            if source_tuple_closed
            else "anchor_interval_formula_closed_source_tuple_data_missing"
        )
    )
    plain_conclusion = (
        "ConcreteAnchorIntervalEnumerationLedger 已闭合：端点公式、source tuple 参数账本和 anchor interval 证书文件生成律均已齐备。"
        f"下一最窄点是 `{MULTIPLICITY_ATOM}`。"
        if ledger_closed
        else (
            "ConcreteAnchorIntervalEnumerationLedger 的端点公式与 source tuple 参数已闭合；"
            f"当前最窄点是 `{CERT_ATOM}`。"
            if source_tuple_closed
            else (
            "ConcreteAnchorIntervalEnumerationLedger 的端点公式已经闭合：在同一 source tuple 下，"
            "每个 anchor a 的 J_a 由 [L,R]、[D0,2D0) 与 phase_rule 唯一确定。当前缺的不是公式，"
            f"而是逐 formal unit 的 concrete source tuple/anchor 参数数据；新的最窄点是 `{SOURCE_ATOM}`。"
            )
        )
    )
    return {
        "certificate_type": "prime_matrix_concrete_anchor_interval_enumeration_router",
        "status": status,
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in evidence_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "row_column_unconditional_closed": False,
        "anchor_interval_endpoint_formula_closed": formula_closed,
        "concrete_anchor_interval_enumeration_closed": ledger_closed,
        "data_like_json": data,
        "certificate_fields": certificate_fields(),
        "endpoint_laws": endpoint_laws(),
        "current_narrowest_atom": current_narrowest,
        "secondary_narrowest_atom": CERT_ATOM,
        "downstream_atoms": [MULTIPLICITY_ATOM],
        "reduction_formula": f"{OLD_ATOM} => {FORMULA_ATOM} AND {SOURCE_ATOM} AND {CERT_ATOM}.",
        "plain_conclusion": plain_conclusion,
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    if result["concrete_anchor_interval_enumeration_closed"]:
        next_note = f"当前唯一最窄点更新为 `{result['current_narrowest_atom']}`。"
        boundary_note = (
            "审稿边界：本步回收 anchor interval 证书文件并关闭锚区间枚举账本；"
            "仍不关闭行列无条件定理。"
        )
    elif result["current_narrowest_atom"] == CERT_ATOM:
        next_note = f"当前唯一最窄点更新为 `{result['current_narrowest_atom']}`；随后才是 `{MULTIPLICITY_ATOM}`。"
        boundary_note = (
            "审稿边界：本步吸收已闭合 source tuple 参数账本；仍不提交 anchor interval 证书文件，"
            "也不关闭行列无条件定理。"
        )
    else:
        next_note = (
            f"当前唯一最窄点更新为 `{result['current_narrowest_atom']}`；随后才是 "
            f"`{result['secondary_narrowest_atom']}` 和 `{MULTIPLICITY_ATOM}`。"
        )
        boundary_note = (
            "审稿边界：本步只关闭锚区间端点公式，不提交 concrete source tuple 数据，"
            "也不关闭行列无条件定理。"
        )
    lines = [
        "# Prime Matrix concrete 锚区间枚举路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"anchor_interval_endpoint_formula_closed={fmt_bool(result['anchor_interval_endpoint_formula_closed'])}",
        f"concrete_anchor_interval_enumeration_closed={fmt_bool(result['concrete_anchor_interval_enumeration_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 收缩公式",
        "",
        "```text",
        result["reduction_formula"],
        "```",
        "",
        "## 2. 端点公式纪律",
        "",
        "| law | formula |",
        "| --- | --- |",
    ]
    for item in result["endpoint_laws"]:
        lines.append(
            "| {law} | {formula} |".format(
                law=table_cell(item["law"]),
                formula=table_cell(item["formula"]),
            )
        )
    lines.extend(
        [
            "",
            "## 3. 证书字段",
            "",
            "| field | meaning |",
            "| --- | --- |",
        ]
    )
    for item in result["certificate_fields"]:
        lines.append(
            "| {field} | {meaning} |".format(
                field=table_cell(item["field"]),
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
    parser.add_argument("--parameter", type=Path, default=DEFAULT_PARAMETER)
    parser.add_argument("--formal", type=Path, default=DEFAULT_FORMAL)
    parser.add_argument("--source-tuple", type=Path, default=DEFAULT_SOURCE_TUPLE)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    paths = {
        "previous": args.previous,
        "parameter": args.parameter,
        "formal": args.formal,
        "source_tuple": args.source_tuple,
    }
    result = run(paths)
    args.json_out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result, args.md_out)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
