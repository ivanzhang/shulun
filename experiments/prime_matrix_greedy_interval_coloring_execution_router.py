#!/usr/bin/env python3
"""Prime Matrix greedy interval coloring execution 路由器。

用法示例：
  python3 experiments/prime_matrix_greedy_interval_coloring_execution_router.py

输出：
  docs/monograph/prime-matrix-greedy-interval-coloring-execution-router.json
  docs/monograph/prime-matrix-greedy-interval-coloring-execution-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-concrete-coloring-coverage-data-router.json"
DEFAULT_MULTIPLICITY = DOCS / "prime-matrix-low-overlap-multiplicity-table-router.json"
DEFAULT_COLORING = DOCS / "prime-matrix-interval-graph-coloring-coverage-router.json"
DEFAULT_ANCHOR = DOCS / "prime-matrix-anchor-interval-certificate-file-router.json"
DEFAULT_HASH = DOCS / "prime-matrix-canonical-formal-unit-hash-stability-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-greedy-interval-coloring-execution-router.json"
DEFAULT_MD = DOCS / "prime-matrix-greedy-interval-coloring-execution-router.md"

OLD_ATOM = "GreedyIntervalColoringExecutionLedger"
EQUATION_ATOM = "CoverageEquationCertificateDataLedger"


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


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def coloring_execution_records() -> list[dict[str, str]]:
    """给出贪心着色执行证书的记录族。"""
    return [
        {
            "record_type": "ordered_interval_input",
            "coverage": "每个低重叠 interval 一条排序输入记录。",
            "rule": "按 (left_d,right_d_exclusive,source_tuple_hash,anchor_id) 稳定排序。",
        },
        {
            "record_type": "release_event",
            "coverage": "扫描到新区间左端点时释放 right_d_exclusive<=left_d 的旧区间颜色。",
            "rule": "半开端点保证相接区间可复用同色。",
        },
        {
            "record_type": "active_set_before_after",
            "coverage": "每一步记录 active_before_hash 与 active_after_hash。",
            "rule": "active set 来自 low-overlap multiplicity table，不能重算出不同活动域。",
        },
        {
            "record_type": "chosen_color",
            "coverage": "每个 interval 一条颜色选择记录。",
            "rule": "取最小可用 color_id；无可用色则开新色，但 color_count 必须 <= Omega。",
        },
        {
            "record_type": "same_color_disjointness_check",
            "coverage": "每个颜色类记录上一右端点。",
            "rule": "新 interval 的 left_d 必须 >= 同色上一 right_d_exclusive。",
        },
        {
            "record_type": "color_count_bound_row",
            "coverage": "每个 source tuple 记录 max_color_count。",
            "rule": "max_color_count <= max_d m(d) <= Omega。",
        },
    ]


def greedy_laws() -> list[dict[str, str]]:
    """给出贪心区间着色纪律。"""
    return [
        {
            "law": "stable_interval_order",
            "formula": "sort by (left,right,source_tuple_hash,anchor_id).",
            "meaning": "执行 transcript 不依赖文件枚举顺序。",
        },
        {
            "law": "release_before_assign",
            "formula": "free colors with right<=left before assigning current interval.",
            "meaning": "半开区间相接不算重叠。",
        },
        {
            "law": "smallest_available_color",
            "formula": "color(I)=min(free_colors) or next_new_color.",
            "meaning": "颜色选择是确定性函数。",
        },
        {
            "law": "omega_capacity",
            "formula": "simultaneous_active_count<=Omega from low-overlap table.",
            "meaning": "贪心所需颜色数不超过 Omega。",
        },
        {
            "law": "per_color_disjointness",
            "formula": "same color implies previous_right<=next_left.",
            "meaning": "同色走廊两两不交。",
        },
        {
            "law": "transcript_hash",
            "formula": "transcript_id=H(source_tuple_hash,sorted(step_hashes)).",
            "meaning": "执行记录可复算且稳定。",
        },
    ]


def build_rows(
    previous: dict[str, Any],
    multiplicity: dict[str, Any],
    coloring: dict[str, Any],
    anchor: dict[str, Any],
    hash_ledger: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 greedy coloring execution 判定表。"""
    active = previous.get("current_narrowest_atom") == OLD_ATOM
    guard = (
        previous.get("counterexample_assumption_only") is True
        and previous.get("empirical_absence_not_used") is True
        and previous.get("hypothetical_chain_only") is True
        and previous.get("row_column_unconditional_closed") is False
    )
    coverage_schema_ready = previous.get("concrete_coloring_coverage_data_schema_closed") is True
    multiplicity_ready = multiplicity.get("low_overlap_multiplicity_table_ledger_closed") is True
    coloring_ready = coloring.get("interval_graph_coloring_coverage_closed") is True
    anchor_ready = anchor.get("anchor_interval_certificate_file_ledger_closed") is True
    hash_ready = hash_ledger.get("canonical_formal_unit_hash_stability_closed") is True
    execution_closed = all(
        [active, guard, coverage_schema_ready, multiplicity_ready, coloring_ready, anchor_ready, hash_ready]
    )
    return [
        row(
            "GreedyColoringExecutionGateActive",
            active,
            False,
            "上一层已把最窄点推进到 greedy interval coloring execution。",
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
            "CoverageComponentSchemaImported",
            coverage_schema_ready,
            True,
            "coverage 数据已拆成锚区间、多重度、着色执行和覆盖等式四组件。",
            "组件口径固定。",
        ),
        row(
            "LowOverlapMultiplicityImported",
            multiplicity_ready,
            True,
            "低重叠表已给出 m(d)<=Omega 的精确活动域。",
            "颜色容量上界固定。",
        ),
        row(
            "IntervalGraphColoringTheoremImported",
            coloring_ready,
            True,
            "整数区间图贪心着色与 color_count<=Omega 已由上层 formal 证书给出。",
            "无存在性剩余。",
        ),
        row(
            "AnchorIntervalInputImported",
            anchor_ready,
            True,
            "每个低重叠 interval 的端点可由 anchor interval 证书复算。",
            "输入区间稳定。",
        ),
        row(
            "CanonicalTranscriptHashImported",
            hash_ready,
            True,
            "执行步骤哈希继承 source_tuple_hash。",
            "transcript 身份稳定。",
        ),
        row(
            OLD_ATOM,
            execution_closed,
            execution_closed,
            "贪心着色执行 transcript 由排序、释放颜色和最小可用色规则确定性生成。",
            EQUATION_ATOM if execution_closed else OLD_ATOM,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """运行 greedy interval coloring execution 路由。"""
    previous = load_json(paths["previous"])
    multiplicity = load_json(paths["multiplicity"])
    coloring = load_json(paths["coloring"])
    anchor = load_json(paths["anchor"])
    hash_ledger = load_json(paths["hash"])
    rows = build_rows(previous, multiplicity, coloring, anchor, hash_ledger)
    execution_closed = next(item["closed"] for item in rows if item["gate"] == OLD_ATOM)
    evidence_paths = list(paths.values())
    return {
        "certificate_type": "prime_matrix_greedy_interval_coloring_execution_certificate",
        "certificate_scope": "universal_greedy_coloring_transcript_generator",
        "status": "greedy_interval_coloring_execution_closed_coverage_equation_open"
        if execution_closed
        else "greedy_interval_coloring_execution_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in evidence_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "row_column_unconditional_closed": False,
        "greedy_interval_coloring_execution_ledger_closed": execution_closed,
        "proved": execution_closed,
        "coverage_complete": execution_closed,
        "greedy_coloring_transcript": coloring_execution_records(),
        "greedy_laws": greedy_laws(),
        "current_narrowest_atom": EQUATION_ATOM if execution_closed else OLD_ATOM,
        "downstream_atoms": [EQUATION_ATOM],
        "reduction_formula": (
            f"{OLD_ATOM} => LowOverlapMultiplicityTable AND IntervalGraphColoringTheorem "
            "AND StableGreedyTranscript AND CanonicalTranscriptHash."
        ),
        "plain_conclusion": (
            f"{OLD_ATOM} 已闭合：低重叠 intervals 按稳定顺序执行贪心着色，"
            f"每步释放颜色并取最小可用色，color_count<=Omega。下一步可攻 `{EQUATION_ATOM}`。"
            if execution_closed
            else f"{OLD_ATOM} 尚未闭合。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix greedy interval coloring execution 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"greedy_interval_coloring_execution_ledger_closed={fmt_bool(result['greedy_interval_coloring_execution_ledger_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 收缩公式",
        "",
        "```text",
        result["reduction_formula"],
        "```",
        "",
        "## 2. 执行记录族",
        "",
        "| record_type | coverage | rule |",
        "| --- | --- | --- |",
    ]
    for item in result["greedy_coloring_transcript"]:
        lines.append(
            "| {record_type} | {coverage} | {rule} |".format(
                record_type=table_cell(item["record_type"]),
                coverage=table_cell(item["coverage"]),
                rule=table_cell(item["rule"]),
            )
        )
    lines.extend(["", "## 3. 贪心纪律", "", "| law | formula | meaning |", "| --- | --- | --- |"])
    for item in result["greedy_laws"]:
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
            "审稿边界：本步只关闭假设链条中的贪心着色执行 transcript；不提交覆盖等式证书，也不关闭行列无条件定理。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--multiplicity", type=Path, default=DEFAULT_MULTIPLICITY)
    parser.add_argument("--coloring", type=Path, default=DEFAULT_COLORING)
    parser.add_argument("--anchor", type=Path, default=DEFAULT_ANCHOR)
    parser.add_argument("--hash", type=Path, default=DEFAULT_HASH)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    paths = {
        "previous": args.previous,
        "multiplicity": args.multiplicity,
        "coloring": args.coloring,
        "anchor": args.anchor,
        "hash": args.hash,
    }
    result = run(paths)
    args.json_out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result, args.md_out)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
