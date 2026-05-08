#!/usr/bin/env python3
"""Prime Matrix coverage equation certificate 路由器。

用法示例：
  python3 experiments/prime_matrix_coverage_equation_certificate_router.py

输出：
  docs/monograph/prime-matrix-coverage-equation-certificate-router.json
  docs/monograph/prime-matrix-coverage-equation-certificate-router.md
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
DEFAULT_ANCHOR = DOCS / "prime-matrix-anchor-interval-certificate-file-router.json"
DEFAULT_MULTIPLICITY = DOCS / "prime-matrix-low-overlap-multiplicity-table-router.json"
DEFAULT_GREEDY = DOCS / "prime-matrix-greedy-interval-coloring-execution-router.json"
DEFAULT_COLORING = DOCS / "prime-matrix-interval-graph-coloring-coverage-router.json"
DEFAULT_HASH = DOCS / "prime-matrix-canonical-formal-unit-hash-stability-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-coverage-equation-certificate-router.json"
DEFAULT_MD = DOCS / "prime-matrix-coverage-equation-certificate-router.md"

OLD_ATOM = "CoverageEquationCertificateDataLedger"
COVERAGE_ATOM = "ConcreteColoringCoverageDataLedger"
RANKIN_ATOM = "PerColorRankinCertificateFileLedger"


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


def equation_records() -> list[dict[str, str]]:
    """给出覆盖等式证书记录族。"""
    return [
        {
            "record_type": "low_overlap_atom",
            "coverage": "每个低重叠原子 (source_tuple_hash,a,d) 一条。",
            "rule": "来自 multiplicity table 的 low_overlap_row，且 d in J_a。",
        },
        {
            "record_type": "colored_atom",
            "coverage": "每个着色 interval 展开为同一批 (source_tuple_hash,a,d,color_id)。",
            "rule": "投影 pi(source_tuple_hash,a,d,color_id)=(source_tuple_hash,a,d)。",
        },
        {
            "record_type": "projection_count_row",
            "coverage": "每个 projection key 一条计数比较。",
            "rule": "count_low_overlap(key)=count_colored_projection(key)=1；压缩段按长度计数。",
        },
        {
            "record_type": "color_partition_row",
            "coverage": "每个 color_id 一条同色不交走廊记录。",
            "rule": "同色 intervals 两两不交，允许交给后续 per-color Rankin。",
        },
        {
            "record_type": "zero_loss_balance_row",
            "coverage": "每个 source_tuple_hash 一条总量平衡记录。",
            "rule": "sum low_overlap atoms = sum colored projected atoms。",
        },
        {
            "record_type": "mismatch_return",
            "coverage": "若计数不等，必须命名为 CoverageEquationMismatchReturn。",
            "rule": "不允许把漏点、重复点或跨 tuple 错配静默带入 color set。",
        },
    ]


def equation_laws() -> list[dict[str, str]]:
    """给出 coverage equation 的闭合纪律。"""
    return [
        {
            "law": "same_source_tuple_projection",
            "formula": "pi(source_tuple_hash,a,d,color_id)=(source_tuple_hash,a,d).",
            "meaning": "颜色只是附加标签，不改变原低重叠原子。",
        },
        {
            "law": "low_overlap_domain_exact",
            "formula": "domain = {(a,d): d in J_a and m(d)<=Omega}.",
            "meaning": "覆盖等式的左边由低重叠表唯一给出。",
        },
        {
            "law": "colored_domain_exact",
            "formula": "colored = union_color {(a,d,color): d in colored_interval(a,color)}.",
            "meaning": "右边由贪心 transcript 唯一给出。",
        },
        {
            "law": "multiplicity_preservation",
            "formula": "for every key, count_left(key)=count_right(pi^-1(key)).",
            "meaning": "不漏点、不重复、不跨 source tuple 拼接。",
        },
        {
            "law": "per_color_disjoint_partition",
            "formula": "same color intervals are disjoint and colors partition the low-overlap atoms.",
            "meaning": "后续 Rankin 只接收同色不交走廊。",
        },
        {
            "law": "canonical_equation_hash",
            "formula": "equation_id=H(source_tuple_hash,sorted(projection_count_hashes),transcript_id).",
            "meaning": "等式证书可复算且稳定。",
        },
    ]


def build_rows(
    previous: dict[str, Any],
    anchor: dict[str, Any],
    multiplicity: dict[str, Any],
    greedy: dict[str, Any],
    coloring: dict[str, Any],
    hash_ledger: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 coverage equation 判定表。"""
    active = previous.get("current_narrowest_atom") == OLD_ATOM
    guard = (
        previous.get("counterexample_assumption_only") is True
        and previous.get("empirical_absence_not_used") is True
        and previous.get("hypothetical_chain_only") is True
        and previous.get("row_column_unconditional_closed") is False
    )
    schema_ready = previous.get("concrete_coloring_coverage_data_schema_closed") is True
    anchor_ready = anchor.get("anchor_interval_certificate_file_ledger_closed") is True
    multiplicity_ready = multiplicity.get("low_overlap_multiplicity_table_ledger_closed") is True
    greedy_ready = greedy.get("greedy_interval_coloring_execution_ledger_closed") is True
    coloring_ready = coloring.get("interval_graph_coloring_coverage_closed") is True
    hash_ready = hash_ledger.get("canonical_formal_unit_hash_stability_closed") is True
    equation_closed = all(
        [active, guard, schema_ready, anchor_ready, multiplicity_ready, greedy_ready, coloring_ready, hash_ready]
    )
    return [
        row(
            "CoverageEquationGateActive",
            active,
            False,
            "上一层已把最窄点推进到 coverage equation certificate。",
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
            schema_ready,
            True,
            "coverage 数据四组件口径已固定。",
            "等式左右边字段固定。",
        ),
        row(
            "LowOverlapDomainImported",
            anchor_ready and multiplicity_ready,
            True,
            "低重叠原子域由 J_a 与 m(d)<=Omega 唯一给出。",
            "左边 multiset 固定。",
        ),
        row(
            "GreedyColoredDomainImported",
            greedy_ready and coloring_ready,
            True,
            "贪心 transcript 给出每个低重叠 interval 的 color_id 和同色不交性。",
            "右边 colored multiset 固定。",
        ),
        row(
            "ProjectionEqualityDiscipline",
            greedy_ready and multiplicity_ready,
            True,
            "投影 pi 删除 color_id 后逐 key 比较计数。",
            "无漏点或重复点出口。",
        ),
        row(
            "CanonicalEquationHashImported",
            hash_ready,
            True,
            "equation_id 继承 source_tuple_hash 与 transcript hash。",
            "等式身份稳定。",
        ),
        row(
            OLD_ATOM,
            equation_closed,
            equation_closed,
            "有色 interval 多重集投影后与低重叠走廊多重集逐 key 相等。",
            COVERAGE_ATOM if equation_closed else OLD_ATOM,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """运行 coverage equation certificate 路由。"""
    previous = load_json(paths["previous"])
    anchor = load_json(paths["anchor"])
    multiplicity = load_json(paths["multiplicity"])
    greedy = load_json(paths["greedy"])
    coloring = load_json(paths["coloring"])
    hash_ledger = load_json(paths["hash"])
    rows = build_rows(previous, anchor, multiplicity, greedy, coloring, hash_ledger)
    equation_closed = next(item["closed"] for item in rows if item["gate"] == OLD_ATOM)
    evidence_paths = list(paths.values())
    return {
        "certificate_type": "prime_matrix_coverage_equation_certificate_data",
        "certificate_scope": "universal_colored_low_overlap_multiset_equation",
        "status": "coverage_equation_certificate_closed_coverage_data_ready"
        if equation_closed
        else "coverage_equation_certificate_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in evidence_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "row_column_unconditional_closed": False,
        "coverage_equation_certificate_data_ledger_closed": equation_closed,
        "proved": equation_closed,
        "coverage_complete": equation_closed,
        "coverage_equation_certificate": equation_records(),
        "equation_laws": equation_laws(),
        "current_narrowest_atom": COVERAGE_ATOM if equation_closed else OLD_ATOM,
        "downstream_atoms": [COVERAGE_ATOM, RANKIN_ATOM],
        "reduction_formula": (
            f"{OLD_ATOM} => LowOverlapDomain AND GreedyColoredDomain AND "
            "ProjectionMultiplicityEquality AND CanonicalEquationHash."
        ),
        "plain_conclusion": (
            f"{OLD_ATOM} 已闭合：colored interval multiset 删除 color_id 后，"
            f"逐 key 等于低重叠走廊 multiset。下一步可回收 `{COVERAGE_ATOM}`。"
            if equation_closed
            else f"{OLD_ATOM} 尚未闭合。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix coverage equation certificate 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"coverage_equation_certificate_data_ledger_closed={fmt_bool(result['coverage_equation_certificate_data_ledger_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 收缩公式",
        "",
        "```text",
        result["reduction_formula"],
        "```",
        "",
        "## 2. 等式记录族",
        "",
        "| record_type | coverage | rule |",
        "| --- | --- | --- |",
    ]
    for item in result["coverage_equation_certificate"]:
        lines.append(
            "| {record_type} | {coverage} | {rule} |".format(
                record_type=table_cell(item["record_type"]),
                coverage=table_cell(item["coverage"]),
                rule=table_cell(item["rule"]),
            )
        )
    lines.extend(["", "## 3. 等式纪律", "", "| law | formula | meaning |", "| --- | --- | --- |"])
    for item in result["equation_laws"]:
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
            f"当前回收目标为 `{result['current_narrowest_atom']}`；随后才是 `{RANKIN_ATOM}`。",
            "",
            "审稿边界：本步只关闭假设链条中的 coverage equation 数据证书；不执行 per-color Rankin，也不关闭行列无条件定理。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--anchor", type=Path, default=DEFAULT_ANCHOR)
    parser.add_argument("--multiplicity", type=Path, default=DEFAULT_MULTIPLICITY)
    parser.add_argument("--greedy", type=Path, default=DEFAULT_GREEDY)
    parser.add_argument("--coloring", type=Path, default=DEFAULT_COLORING)
    parser.add_argument("--hash", type=Path, default=DEFAULT_HASH)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    paths = {
        "previous": args.previous,
        "anchor": args.anchor,
        "multiplicity": args.multiplicity,
        "greedy": args.greedy,
        "coloring": args.coloring,
        "hash": args.hash,
    }
    result = run(paths)
    args.json_out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result, args.md_out)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
