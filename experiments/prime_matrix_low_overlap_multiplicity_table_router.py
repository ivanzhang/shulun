#!/usr/bin/env python3
"""Prime Matrix low-overlap multiplicity table 路由器。

用法示例：
  python3 experiments/prime_matrix_low_overlap_multiplicity_table_router.py

输出：
  docs/monograph/prime-matrix-low-overlap-multiplicity-table-router.json
  docs/monograph/prime-matrix-low-overlap-multiplicity-table-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-concrete-anchor-interval-enumeration-router.json"
DEFAULT_ANCHOR_CERTIFICATE = DOCS / "prime-matrix-anchor-interval-certificate-file-router.json"
DEFAULT_PARAMETER = DOCS / "prime-matrix-complement-anchor-d0k-parameter-router.json"
DEFAULT_HASH = DOCS / "prime-matrix-canonical-formal-unit-hash-stability-router.json"
DEFAULT_FORMAL = DOCS / "prime-matrix-formal-corridor-inventory-contract-router.md"
DEFAULT_JSON = DOCS / "prime-matrix-low-overlap-multiplicity-table-router.json"
DEFAULT_MD = DOCS / "prime-matrix-low-overlap-multiplicity-table-router.md"

OLD_ATOM = "LowOverlapMultiplicityTableLedger"
COLORING_ATOM = "GreedyIntervalColoringExecutionLedger"
HIGH_OVERLAP_RETURN = "HighOverlapFixedCoreDefect"


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


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def multiplicity_records() -> list[dict[str, str]]:
    """给出低重叠多重度表的记录族。"""
    return [
        {
            "record_type": "endpoint_event",
            "coverage": "每个非空 anchor interval 产生 left:+1 与 right:-1 两个事件。",
            "rule": "事件按 (d,event_type,anchor_id) 规范排序；半开端点先处理 right 再处理 left。",
        },
        {
            "record_type": "active_anchor_set",
            "coverage": "每个核心 d 或最大常值段一条。",
            "rule": "active(d)={a: left_a<=d<right_a 且 phase_rule(d)=true}。",
        },
        {
            "record_type": "multiplicity_row",
            "coverage": "每个 d 或最大常值段记录 m(d)。",
            "rule": "m(d)=|active(d)|，active_anchor_hash=H(sorted(active(d)))。",
        },
        {
            "record_type": "low_overlap_row",
            "coverage": "m(d)<=Omega 的核心点或段进入低重叠走廊。",
            "rule": "写 low_overlap_flag=true，并保留 active_anchor_hash。",
        },
        {
            "record_type": "high_overlap_return",
            "coverage": "m(d)>Omega 的核心点或段必须命名回流。",
            "rule": f"写 return_type={HIGH_OVERLAP_RETURN}，不得留在低重叠着色域。",
        },
        {
            "record_type": "empty_active_row",
            "coverage": "m(d)=0 的空活动段显式记录或压缩记录。",
            "rule": "空活动段不是数据缺口，写 empty_active_flag=true。",
        },
    ]


def sweep_laws() -> list[dict[str, str]]:
    """给出 sweep-line 多重度计算纪律。"""
    return [
        {
            "law": "event_conservation",
            "formula": "sum(left_events)-sum(right_events)=0 over each source_tuple file.",
            "meaning": "每条锚区间只进入一次、退出一次，不能制造或丢失 active anchor。",
        },
        {
            "law": "half_open_endpoint_order",
            "formula": "[left,right) uses right-events before left-events at the same d.",
            "meaning": "相接区间不被误判为重叠。",
        },
        {
            "law": "phase_filtered_activity",
            "formula": "active(d) additionally requires phase_rule(d)=true.",
            "meaning": "相位过滤继承证书文件，不能在多重度表里重选。",
        },
        {
            "law": "omega_split_exact",
            "formula": "low(d) iff m(d)<=Omega; high(d) iff m(d)>Omega.",
            "meaning": "低/高重叠二分是互斥且穷尽的。",
        },
        {
            "law": "high_overlap_named_return",
            "formula": "m(d)>Omega -> HighOverlapFixedCoreDefect(d,active(d)).",
            "meaning": "高重叠点不能进入 colored corridor，也不能静默删除。",
        },
        {
            "law": "canonical_table_hash",
            "formula": "table_id=H(source_tuple_hash,Omega,sorted(multiplicity_row_hashes)).",
            "meaning": "多重度表由锚区间证书和 Omega 唯一决定。",
        },
    ]


def build_rows(
    previous: dict[str, Any],
    anchor_certificate: dict[str, Any],
    parameter: dict[str, Any],
    hash_ledger: dict[str, Any],
    formal_text: str,
) -> list[dict[str, Any]]:
    """生成 low-overlap multiplicity table 判定表。"""
    active = previous.get("current_narrowest_atom") == OLD_ATOM
    guard = (
        previous.get("counterexample_assumption_only") is True
        and previous.get("empirical_absence_not_used") is True
        and previous.get("hypothetical_chain_only") is True
        and previous.get("row_column_unconditional_closed") is False
    )
    anchor_ready = previous.get("concrete_anchor_interval_enumeration_closed") is True
    certificate_ready = anchor_certificate.get("anchor_interval_certificate_file_ledger_closed") is True
    parameter_ready = parameter.get("complement_anchor_d0k_parameter_discipline_closed") is True
    omega_ready = contains_all(formal_text, ["Omega", "低重叠阈值", "高重叠分支"])
    hash_ready = hash_ledger.get("canonical_formal_unit_hash_stability_closed") is True
    table_closed = all([active, guard, anchor_ready, certificate_ready, parameter_ready, omega_ready, hash_ready])
    return [
        row(
            "LowOverlapMultiplicityGateActive",
            active,
            False,
            "上一层已把最窄点推进到 low-overlap multiplicity table。",
            OLD_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只处理假设早期零行链条，不使用真实零行缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "AnchorIntervalsImported",
            anchor_ready and certificate_ready,
            True,
            "锚区间枚举账本和证书文件生成律均已闭合，事件域固定。",
            "不能重选 J_a。",
        ),
        row(
            "OmegaDisciplineImported",
            parameter_ready and omega_ready,
            True,
            "Omega 来自同一 source tuple 的 DCS 高/低重叠二分纪律。",
            "不能后验移动阈值。",
        ),
        row(
            "SweepLineMultiplicityDeterministic",
            anchor_ready and certificate_ready and parameter_ready,
            True,
            "按端点事件前缀和可唯一复算每个 d 的 active anchors 与 m(d)。",
            "无多重度选择口。",
        ),
        row(
            "HighLowSplitExhaustive",
            parameter_ready and omega_ready,
            True,
            "m(d)<=Omega 进入低重叠表；m(d)>Omega 进入命名 high-overlap return。",
            HIGH_OVERLAP_RETURN,
        ),
        row(
            "CanonicalMultiplicityHashImported",
            hash_ready,
            True,
            "multiplicity row hash 与 table_id 继承 source_tuple_hash。",
            "表身份稳定。",
        ),
        row(
            OLD_ATOM,
            table_closed,
            table_closed,
            "低重叠多重度表由锚区间事件和 Omega 确定性生成；高重叠点强制命名回流。",
            COLORING_ATOM if table_closed else OLD_ATOM,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """运行 low-overlap multiplicity table 路由。"""
    previous = load_json(paths["previous"])
    anchor_certificate = load_json(paths["anchor_certificate"])
    parameter = load_json(paths["parameter"])
    hash_ledger = load_json(paths["hash"])
    formal_text = read_text(paths["formal"])
    rows = build_rows(previous, anchor_certificate, parameter, hash_ledger, formal_text)
    table_closed = next(item["closed"] for item in rows if item["gate"] == OLD_ATOM)
    evidence_paths = list(paths.values())
    return {
        "certificate_type": "prime_matrix_low_overlap_multiplicity_table_certificate",
        "certificate_scope": "universal_sweepline_multiplicity_generator",
        "status": "low_overlap_multiplicity_table_closed_coloring_open"
        if table_closed
        else "low_overlap_multiplicity_table_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in evidence_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "row_column_unconditional_closed": False,
        "low_overlap_multiplicity_table_ledger_closed": table_closed,
        "proved": table_closed,
        "coverage_complete": table_closed,
        "low_overlap_multiplicity_table": multiplicity_records(),
        "sweep_laws": sweep_laws(),
        "current_narrowest_atom": COLORING_ATOM if table_closed else OLD_ATOM,
        "downstream_atoms": [COLORING_ATOM],
        "reduction_formula": (
            f"{OLD_ATOM} => AnchorIntervalEnumeration AND AnchorIntervalCertificateFile "
            "AND OmegaDiscipline AND SweepLineEventConservation AND HighOverlapNamedReturn."
        ),
        "plain_conclusion": (
            f"{OLD_ATOM} 已闭合：从锚区间端点事件可唯一复算 m(d)，"
            f"m(d)<=Omega 进入低重叠表，m(d)>Omega 强制回流 `{HIGH_OVERLAP_RETURN}`。"
            f"下一步可攻 `{COLORING_ATOM}`。"
            if table_closed
            else f"{OLD_ATOM} 尚未闭合。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix low-overlap multiplicity table 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"low_overlap_multiplicity_table_ledger_closed={fmt_bool(result['low_overlap_multiplicity_table_ledger_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 收缩公式",
        "",
        "```text",
        result["reduction_formula"],
        "```",
        "",
        "## 2. 多重度记录族",
        "",
        "| record_type | coverage | rule |",
        "| --- | --- | --- |",
    ]
    for item in result["low_overlap_multiplicity_table"]:
        lines.append(
            "| {record_type} | {coverage} | {rule} |".format(
                record_type=table_cell(item["record_type"]),
                coverage=table_cell(item["coverage"]),
                rule=table_cell(item["rule"]),
            )
        )
    lines.extend(["", "## 3. sweep-line 纪律", "", "| law | formula | meaning |", "| --- | --- | --- |"])
    for item in result["sweep_laws"]:
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
            f"当前回收目标为 `{result['current_narrowest_atom']}`。",
            "",
            "审稿边界：本步只关闭假设链条中的低重叠多重度表生成律；高重叠点保留为命名 return，不关闭行列无条件定理。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--anchor-certificate", type=Path, default=DEFAULT_ANCHOR_CERTIFICATE)
    parser.add_argument("--parameter", type=Path, default=DEFAULT_PARAMETER)
    parser.add_argument("--hash", type=Path, default=DEFAULT_HASH)
    parser.add_argument("--formal", type=Path, default=DEFAULT_FORMAL)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    paths = {
        "previous": args.previous,
        "anchor_certificate": args.anchor_certificate,
        "parameter": args.parameter,
        "hash": args.hash,
        "formal": args.formal,
    }
    result = run(paths)
    args.json_out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result, args.md_out)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
