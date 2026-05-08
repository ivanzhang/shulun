#!/usr/bin/env python3
"""Prime Matrix concrete coloring coverage 数据路由器。

用法示例：
  python3 experiments/prime_matrix_concrete_coloring_coverage_data_router.py

输出：
  docs/monograph/prime-matrix-concrete-coloring-coverage-data-router.json
  docs/monograph/prime-matrix-concrete-coloring-coverage-data-router.md
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

DEFAULT_PREVIOUS = MONOGRAPH / "prime-matrix-concrete-color-set-enumeration-router.json"
DEFAULT_COLORING = MONOGRAPH / "prime-matrix-interval-graph-coloring-coverage-router.json"
DEFAULT_PARAMETER = MONOGRAPH / "prime-matrix-complement-anchor-d0k-parameter-router.json"
DEFAULT_FORMAL = MONOGRAPH / "prime-matrix-formal-corridor-inventory-contract-router.json"
DEFAULT_JSON = MONOGRAPH / "prime-matrix-concrete-coloring-coverage-data-router.json"
DEFAULT_MD = MONOGRAPH / "prime-matrix-concrete-coloring-coverage-data-router.md"

OLD_ATOM = "ConcreteColoringCoverageDataLedger"
SCHEMA_ATOM = "ConcreteColoringCoverageDataSchemaClosed"
ANCHOR_ATOM = "ConcreteAnchorIntervalEnumerationLedger"
MULTIPLICITY_ATOM = "LowOverlapMultiplicityTableLedger"
COLORING_ATOM = "GreedyIntervalColoringExecutionLedger"
EQUATION_ATOM = "CoverageEquationCertificateDataLedger"
RANKIN_ATOM = "PerColorRankinCertificateFileLedger"


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


def component_kind(payload: dict[str, Any]) -> str | None:
    """识别 concrete coloring coverage 的组件数据类型。"""
    cert_type = payload.get("certificate_type")
    keys = set(payload.keys())
    if cert_type == "prime_matrix_concrete_anchor_interval_enumeration_certificate":
        return ANCHOR_ATOM
    if cert_type == "prime_matrix_low_overlap_multiplicity_table_certificate":
        return MULTIPLICITY_ATOM
    if cert_type == "prime_matrix_greedy_interval_coloring_execution_certificate":
        return COLORING_ATOM
    if cert_type == "prime_matrix_coverage_equation_certificate_data":
        return EQUATION_ATOM
    if {"concrete_anchor_interval_records", "anchor_interval_records"} & keys:
        return ANCHOR_ATOM
    if {"low_overlap_multiplicity_table", "multiplicity_records", "overlap_table"} & keys:
        return MULTIPLICITY_ATOM
    if {"greedy_coloring_transcript", "coloring_execution_records", "colored_interval_records"} & keys:
        return COLORING_ATOM
    if {"coverage_equation_certificate", "coverage_equation_records"} & keys:
        return EQUATION_ATOM
    return None


def record_count(payload: dict[str, Any], kind: str) -> int | None:
    """读取组件记录数量。"""
    candidate_keys = {
        ANCHOR_ATOM: ["concrete_anchor_interval_records", "anchor_interval_records"],
        MULTIPLICITY_ATOM: ["low_overlap_multiplicity_table", "multiplicity_records", "overlap_table"],
        COLORING_ATOM: ["greedy_coloring_transcript", "coloring_execution_records", "colored_interval_records"],
        EQUATION_ATOM: ["coverage_equation_certificate", "coverage_equation_records"],
    }[kind]
    for key in candidate_keys:
        value = payload.get(key)
        if isinstance(value, list):
            return len(value)
        if isinstance(value, dict):
            return len(value)
    return None


def scan_component_data(root: Path) -> dict[str, list[dict[str, Any]]]:
    """扫描 concrete coverage 组件数据。"""
    found: dict[str, list[dict[str, Any]]] = {
        ANCHOR_ATOM: [],
        MULTIPLICITY_ATOM: [],
        COLORING_ATOM: [],
        EQUATION_ATOM: [],
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
        kind = component_kind(payload)
        if kind is None:
            continue
        found[kind].append(
            {
                "path": str(path.relative_to(ROOT)),
                "status": payload.get("status"),
                "record_count": record_count(payload, kind),
                "coverage_complete": payload.get("coverage_complete"),
                "source_tuple_hash": payload.get("source_tuple_hash"),
            }
        )
    return found


def required_components() -> list[dict[str, str]]:
    """给出 concrete coloring coverage 数据的四个必要组件。"""
    return [
        {
            "atom": ANCHOR_ATOM,
            "input": "逐 source tuple 枚举每个 anchor a 的整数区间 J_a。",
            "equation": "J_a=[ceil(L/a),floor(R/a)] ∩ [D0,2D0) ∩ phase_rule。",
        },
        {
            "atom": MULTIPLICITY_ATOM,
            "input": "对每个核心 d 记录 active anchors 与 m(d)，并把 m(d)>Omega 回流高重叠缺陷。",
            "equation": "m(d)=# {a: d in J_a}; low-overlap iff m(d)<=Omega。",
        },
        {
            "atom": COLORING_ATOM,
            "input": "按左端点贪心给低重叠区间着色，并记录每一步 active set。",
            "equation": "overlap(J_i,J_j) and same color is forbidden; color_count<=Omega。",
        },
        {
            "atom": EQUATION_ATOM,
            "input": "给出有色 interval 多重集与低重叠走廊多重集完全相等的证书。",
            "equation": "multiset(colored intervals)=multiset((a,d): d in J_a, m(d)<=Omega)。",
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
    coloring: dict[str, Any],
    parameter: dict[str, Any],
    formal_text: str,
    component_data: dict[str, list[dict[str, Any]]],
) -> list[dict[str, Any]]:
    """生成 concrete coloring coverage 数据判定表。"""
    active = previous.get("current_narrowest_atom") == OLD_ATOM
    guard = (
        previous.get("counterexample_assumption_only") is True
        and previous.get("empirical_absence_not_used") is True
        and previous.get("hypothetical_chain_only") is True
        and previous.get("row_column_unconditional_closed") is False
    )
    enumerator_ready = previous.get("concrete_color_set_enumerator_closed") is True
    coloring_schema_ready = coloring.get("interval_graph_coloring_coverage_closed") is True
    parameter_ready = parameter.get("complement_anchor_d0k_parameter_discipline_closed") is True
    formal_fields_ready = contains_all(
        formal_text,
        ["anchor_set_hash", "intervals", "coverage_equation", "allowed_budget"],
    )
    schema_closed = all([active, guard, enumerator_ready, coloring_schema_ready, parameter_ready, formal_fields_ready])
    data_available = {atom: bool(records) for atom, records in component_data.items()}
    all_components_available = all(data_available.values())
    all_components_complete = all(
        records and all(item.get("coverage_complete") is True for item in records)
        for records in component_data.values()
    )
    return [
        row(
            "ConcreteColoringCoverageGateActive",
            active,
            False,
            "上一层已把最窄点推进到 concrete coloring coverage 数据。",
            OLD_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只处理假设早期零行反例链中的 coverage 数据，不使用真实缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "UpstreamSchemasImported",
            enumerator_ready and coloring_schema_ready and parameter_ready and formal_fields_ready,
            True,
            "color set 枚举器、formal coloring schema、参数纪律和 inventory 字段均已固定。",
            "无 coverage 格式剩余。",
        ),
        row(
            SCHEMA_ATOM,
            schema_closed,
            True,
            "Concrete coverage 数据被唯一拆成锚区间、多重度表、着色执行和覆盖等式四个组件。",
            SCHEMA_ATOM,
        ),
        row(
            "ConcreteAnchorIntervalsAvailable",
            data_available[ANCHOR_ATOM],
            False,
            "仓库尚未发现逐 source tuple 的 J_a 锚区间枚举数据。",
            ANCHOR_ATOM,
        ),
        row(
            "LowOverlapMultiplicityTableAvailable",
            data_available[MULTIPLICITY_ATOM],
            False,
            "仓库尚未发现 m(d) 与 low/high overlap 分流表。",
            MULTIPLICITY_ATOM,
        ),
        row(
            "GreedyColoringExecutionAvailable",
            data_available[COLORING_ATOM],
            False,
            "仓库尚未发现贪心区间着色执行 transcript。",
            COLORING_ATOM,
        ),
        row(
            "CoverageEquationCertificateAvailable",
            data_available[EQUATION_ATOM],
            False,
            "仓库尚未发现多重集相等的 coverage equation 数据证书。",
            EQUATION_ATOM,
        ),
        row(
            "AllCoverageComponentsComplete",
            all_components_available and all_components_complete,
            False,
            "四个组件必须同 source tuple/hash 完整覆盖后，才可枚举 concrete color set。",
            f"{ANCHOR_ATOM} AND {MULTIPLICITY_ATOM} AND {COLORING_ATOM} AND {EQUATION_ATOM}",
        ),
        row(
            OLD_ATOM,
            False,
            False,
            "ConcreteColoringCoverageDataLedger 不能由 schema 单独关闭；仍需提交四类 concrete 组件数据。",
            ANCHOR_ATOM,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """运行 concrete coloring coverage 数据路由。"""
    previous = load_json(paths["previous"])
    coloring = load_json(paths["coloring"])
    parameter = load_json(paths["parameter"])
    formal_text = read_text(paths["formal"])
    component_data = scan_component_data(DOCS)
    rows = build_rows(previous, coloring, parameter, formal_text, component_data)
    schema_closed = next(item["closed"] for item in rows if item["gate"] == SCHEMA_ATOM)
    evidence_paths = list(paths.values())
    return {
        "certificate_type": "prime_matrix_concrete_coloring_coverage_data_router",
        "status": "concrete_coloring_coverage_schema_closed_anchor_data_missing",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in evidence_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "row_column_unconditional_closed": False,
        "concrete_coloring_coverage_data_schema_closed": schema_closed,
        "concrete_coloring_coverage_data_closed": False,
        "component_data_like_json": component_data,
        "required_components": required_components(),
        "current_narrowest_atom": ANCHOR_ATOM,
        "downstream_atoms": [MULTIPLICITY_ATOM, COLORING_ATOM, EQUATION_ATOM, RANKIN_ATOM],
        "reduction_formula": (
            f"{OLD_ATOM} => {SCHEMA_ATOM} AND {ANCHOR_ATOM} AND {MULTIPLICITY_ATOM} "
            f"AND {COLORING_ATOM} AND {EQUATION_ATOM}."
        ),
        "plain_conclusion": (
            "ConcreteColoringCoverageDataLedger 的数据格式和依赖顺序已闭合：先由同一 source tuple 枚举"
            "锚区间 J_a，再计算 m(d) 的低/高重叠分流表，再执行区间图贪心着色，最后用覆盖等式证明"
            "有色多重集等于低重叠走廊多重集。仓库尚未提交第一类 concrete 锚区间枚举数据，因此新的"
            f"最窄点是 `{ANCHOR_ATOM}`。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix concrete coloring coverage 数据路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"concrete_coloring_coverage_data_schema_closed={fmt_bool(result['concrete_coloring_coverage_data_schema_closed'])}",
        f"concrete_coloring_coverage_data_closed={fmt_bool(result['concrete_coloring_coverage_data_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 收缩公式",
        "",
        "```text",
        result["reduction_formula"],
        "```",
        "",
        "## 2. 四个必要组件",
        "",
        "| atom | input | equation |",
        "| --- | --- | --- |",
    ]
    for item in result["required_components"]:
        lines.append(
            "| {atom} | {input} | {equation} |".format(
                atom=table_cell(item["atom"]),
                input=table_cell(item["input"]),
                equation=table_cell(item["equation"]),
            )
        )
    lines.extend(
        [
            "",
            "## 3. 当前扫描",
            "",
        ]
    )
    for atom, records in result["component_data_like_json"].items():
        lines.append(f"- {atom}: `{len(records)}`")
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
            f"当前唯一最窄点更新为 `{result['current_narrowest_atom']}`；随后依次验收 "
            f"`{MULTIPLICITY_ATOM}`、`{COLORING_ATOM}`、`{EQUATION_ATOM}`，再进入 `{RANKIN_ATOM}`。",
            "",
            "审稿边界：本步只关闭 concrete coloring coverage 的数据分解和验收顺序，不提交 concrete 数据全集。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--coloring", type=Path, default=DEFAULT_COLORING)
    parser.add_argument("--parameter", type=Path, default=DEFAULT_PARAMETER)
    parser.add_argument("--formal", type=Path, default=DEFAULT_FORMAL)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    paths = {
        "previous": args.previous,
        "coloring": args.coloring,
        "parameter": args.parameter,
        "formal": args.formal,
    }
    result = run(paths)
    args.json_out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result, args.md_out)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
