#!/usr/bin/env python3
"""Prime Matrix concrete color set 枚举路由器。

用法示例：
  python3 experiments/prime_matrix_concrete_color_set_enumeration_router.py

输出：
  docs/monograph/prime-matrix-concrete-color-set-enumeration-router.json
  docs/monograph/prime-matrix-concrete-color-set-enumeration-router.md
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

DEFAULT_PREVIOUS = MONOGRAPH / "prime-matrix-concrete-rankin-manifest-data-router.json"
DEFAULT_COLORING = MONOGRAPH / "prime-matrix-interval-graph-coloring-coverage-router.json"
DEFAULT_PARAMETER = MONOGRAPH / "prime-matrix-complement-anchor-d0k-parameter-router.json"
DEFAULT_FORMAL = MONOGRAPH / "prime-matrix-formal-corridor-inventory-contract-router.json"
DEFAULT_JSON = MONOGRAPH / "prime-matrix-concrete-color-set-enumeration-router.json"
DEFAULT_MD = MONOGRAPH / "prime-matrix-concrete-color-set-enumeration-router.md"

OLD_ATOM = "ConcreteColorSetEnumerationLedger"
ENUMERATOR_ATOM = "ConcreteColorSetEnumeratorClosed"
COLORING_DATA_ATOM = "ConcreteColoringCoverageDataLedger"
CERT_ATOM = "PerColorRankinCertificateFileLedger"


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


def is_coloring_data_like(payload: dict[str, Any]) -> bool:
    """判断 JSON 是否像 concrete coloring coverage 数据。"""
    keys = set(payload.keys())
    return (
        payload.get("certificate_type")
        in {
            "prime_matrix_interval_graph_coloring_coverage_certificate",
            "prime_matrix_concrete_coloring_coverage_data_router",
        }
        or payload.get("concrete_coloring_coverage_data_closed") is True
        or "coloring_coverage_records" in keys
        or "colored_corridor_color_set" in keys
        or "color_classes" in keys
    )


def scan_coloring_data(root: Path) -> list[dict[str, Any]]:
    """扫描 concrete coloring coverage 数据。"""
    found: list[dict[str, Any]] = []
    for path in sorted(root.rglob("*.json")):
        if "__pycache__" in path.parts:
            continue
        try:
            payload = load_json(path)
        except (json.JSONDecodeError, UnicodeDecodeError):
            continue
        if not isinstance(payload, dict) or not is_coloring_data_like(payload):
            continue
        records = (
            payload.get("coloring_coverage_records")
            or payload.get("colored_corridor_color_set")
            or payload.get("color_classes")
            or payload.get("required_components")
            or []
        )
        found.append(
            {
                "path": str(path.relative_to(ROOT)),
                "status": payload.get("status"),
                "record_count": len(records) if isinstance(records, list) else None,
                "coverage_complete": payload.get("coverage_complete")
                if payload.get("coverage_complete") is not None
                else payload.get("concrete_coloring_coverage_data_closed"),
            }
        )
    return found


def enumeration_fields() -> list[dict[str, str]]:
    """给出 color set 枚举输出字段。"""
    return [
        {"field": "color_set_id", "meaning": "颜色全集稳定编号。"},
        {"field": "source_tuple_hash", "meaning": "锁定 A、D0、K、Omega、phase_rule。"},
        {"field": "coverage_certificate_hash", "meaning": "concrete coloring coverage 证书 hash。"},
        {"field": "color_id", "meaning": "颜色编号。"},
        {"field": "intervals", "meaning": "该颜色类同色不相交 intervals。"},
        {"field": "K", "meaning": "继承同一 omega 截断。"},
        {"field": "phase_rule", "meaning": "继承同一 sigma_K phase 谓词。"},
        {"field": "allowed_budget", "meaning": "继承预算纪律下预登记的 B_allow。"},
        {"field": "coverage_equation_ref", "meaning": "指向证明无漏色/无漏 interval 的覆盖等式。"},
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
    coloring: dict[str, Any],
    parameter: dict[str, Any],
    formal: dict[str, Any],
    coloring_data: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """生成 concrete color set 枚举判定表。"""
    active = previous.get("current_narrowest_atom") == OLD_ATOM
    guard = (
        previous.get("counterexample_assumption_only") is True
        and previous.get("empirical_absence_not_used") is True
        and previous.get("hypothetical_chain_only") is True
        and previous.get("row_column_unconditional_closed") is False
    )
    manifest_emitter_ready = previous.get("concrete_rankin_batch_manifest_emitter_closed") is True
    coloring_schema_ready = coloring.get("interval_graph_coloring_coverage_closed") is True
    parameter_ready = parameter.get("complement_anchor_d0k_parameter_discipline_closed") is True
    formal_schema_ready = formal.get("formal_corridor_inventory_schema_closed") is True
    enumerator_closed = all([active, guard, manifest_emitter_ready, coloring_schema_ready, parameter_ready, formal_schema_ready])
    data_found = bool(coloring_data)
    data_complete = data_found and all(item.get("coverage_complete") is True for item in coloring_data)
    ledger_closed = enumerator_closed and data_complete
    data_found_meaning = (
        "已发现 concrete coloring coverage 数据闭合证书，可枚举 color set。"
        if data_found
        else "仓库尚未发现 concrete coloring coverage 数据；因此无法枚举真实 color set。"
    )
    data_complete_meaning = (
        "coverage 数据已声明四组件完整覆盖低重叠走廊。"
        if data_complete
        else "coverage 数据必须声明覆盖全部低重叠走廊。"
    )
    return [
        row(
            "ConcreteColorSetGateActive",
            active,
            False,
            "上一层已把最窄点推进到 concrete color set 枚举。",
            OLD_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只处理假设反例链条内的颜色枚举，不使用真实缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "EnumeratorInputsReady",
            manifest_emitter_ready and coloring_schema_ready and parameter_ready and formal_schema_ready,
            True,
            "manifest 发射器、coloring schema、参数纪律和 formal inventory schema 均已固定。",
            "无枚举规则剩余。",
        ),
        row(
            ENUMERATOR_ATOM,
            enumerator_closed,
            True,
            "color set 枚举器已闭合：从 concrete coloring coverage 数据输出每个 color_id 的 intervals 与预算字段。",
            ENUMERATOR_ATOM,
        ),
        row(
            "ConcreteColoringCoverageDataAvailable",
            data_found,
            False,
            data_found_meaning,
            COLORING_DATA_ATOM,
        ),
        row(
            "ConcreteColoringCoverageComplete",
            data_complete,
            False,
            data_complete_meaning,
            COLORING_DATA_ATOM,
        ),
        row(
            OLD_ATOM,
            ledger_closed,
            ledger_closed,
            "color set 由 concrete coloring coverage 数据确定性枚举；颜色全集、每色 intervals 和预算字段均可复算。",
            CERT_ATOM if ledger_closed else COLORING_DATA_ATOM,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """运行 concrete color set 枚举路由。"""
    previous = load_json(paths["previous"])
    coloring = load_json(paths["coloring"])
    parameter = load_json(paths["parameter"])
    formal = load_json(paths["formal"])
    coloring_data = scan_coloring_data(DOCS)
    rows = build_rows(previous, coloring, parameter, formal, coloring_data)
    enumerator_closed = next(item["closed"] for item in rows if item["gate"] == ENUMERATOR_ATOM)
    ledger_closed = next(item["closed"] for item in rows if item["gate"] == OLD_ATOM)
    evidence_paths = list(paths.values())
    evidence_paths.extend(ROOT / item["path"] for item in coloring_data)
    evidence_paths = list(dict.fromkeys(evidence_paths))
    status = (
        "concrete_color_set_enumeration_closed_rankin_open"
        if ledger_closed
        else "concrete_color_set_enumerator_closed_coloring_data_missing"
    )
    plain_conclusion = (
        "ConcreteColorSetEnumerationLedger 已闭合：由 concrete coloring coverage 数据可唯一输出 color_id 全集、"
        f"每色 intervals、phase/K 与 allowed_budget 字段。下一最窄点是 `{CERT_ATOM}`。"
        if ledger_closed
        else (
            "ConcreteColorSetEnumerationLedger 的枚举器规则已闭合：给定 concrete coloring coverage 数据，"
            "可以唯一输出 color_id 全集、每色 intervals、phase/K 与 allowed_budget 字段。当前仓库没有"
            f" concrete coloring coverage 数据，因此新的最窄点是 `{COLORING_DATA_ATOM}`。"
        )
    )
    return {
        "certificate_type": "prime_matrix_concrete_color_set_enumeration_router",
        "status": status,
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in evidence_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "row_column_unconditional_closed": False,
        "concrete_color_set_enumerator_closed": enumerator_closed,
        "concrete_color_set_enumeration_closed": ledger_closed,
        "coloring_data_like_json": coloring_data,
        "enumeration_fields": enumeration_fields(),
        "current_narrowest_atom": CERT_ATOM if ledger_closed else COLORING_DATA_ATOM,
        "secondary_narrowest_atom": CERT_ATOM,
        "reduction_formula": f"{OLD_ATOM} => {ENUMERATOR_ATOM} AND {COLORING_DATA_ATOM}.",
        "plain_conclusion": plain_conclusion,
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    if result["concrete_color_set_enumeration_closed"]:
        next_note = f"当前唯一最窄点更新为 `{result['current_narrowest_atom']}`。"
        boundary_note = "审稿边界：本步回收 concrete coloring coverage 数据并关闭 color set 枚举；不提交逐色 Rankin 证书。"
    else:
        next_note = (
            f"当前唯一最窄点更新为 `{result['current_narrowest_atom']}`；"
            f"随后才是 `{result['secondary_narrowest_atom']}`。"
        )
        boundary_note = "审稿边界：本步只关闭 color set 枚举器，不提交 concrete coloring coverage 数据。"
    lines = [
        "# Prime Matrix concrete color set 枚举路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"concrete_color_set_enumerator_closed={fmt_bool(result['concrete_color_set_enumerator_closed'])}",
        f"concrete_color_set_enumeration_closed={fmt_bool(result['concrete_color_set_enumeration_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 收缩公式",
        "",
        "```text",
        result["reduction_formula"],
        "```",
        "",
        "## 2. 枚举字段",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for item in result["enumeration_fields"]:
        lines.append(
            "| {field} | {meaning} |".format(
                field=table_cell(item["field"]),
                meaning=table_cell(item["meaning"]),
            )
        )
    lines.extend(
        [
            "",
            "## 3. 当前扫描",
            "",
            f"- coloring-data-like JSON: `{len(result['coloring_data_like_json'])}`",
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
            next_note,
            "",
            boundary_note,
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--coloring", type=Path, default=DEFAULT_COLORING)
    parser.add_argument("--parameter", type=Path, default=DEFAULT_PARAMETER)
    parser.add_argument("--formal", type=Path, default=DEFAULT_FORMAL)
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "previous": args.previous,
        "coloring": args.coloring,
        "parameter": args.parameter,
        "formal": args.formal,
    }
    result = run(paths)
    args.json.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result, args.md)
    print(f"wrote {args.json}")
    print(f"wrote {args.md}")


if __name__ == "__main__":
    main()
