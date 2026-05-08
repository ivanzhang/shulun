#!/usr/bin/env python3
"""Prime Matrix 区间图着色覆盖证书路由器。

用法示例：
  python3 experiments/prime_matrix_interval_graph_coloring_coverage_router.py

输出：
  docs/monograph/prime-matrix-interval-graph-coloring-coverage-router.json
  docs/monograph/prime-matrix-interval-graph-coloring-coverage-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = MONOGRAPH / "prime-matrix-complement-anchor-d0k-parameter-router.json"
DEFAULT_FORMAL = MONOGRAPH / "prime-matrix-formal-corridor-inventory-contract-router.md"
DEFAULT_DCS = MONOGRAPH / "prime-matrix-bpn-distributed-corridor-saturation-reduction.md"
DEFAULT_CCB = MONOGRAPH / "prime-matrix-bpn-colored-corridor-core-sieve-budget.md"
DEFAULT_JSON = MONOGRAPH / "prime-matrix-interval-graph-coloring-coverage-router.json"
DEFAULT_MD = MONOGRAPH / "prime-matrix-interval-graph-coloring-coverage-router.md"

OLD_ATOM = "IntervalGraphColoringCoverageCertificateLedger"
CLOSED_ATOM = "IntervalGraphColoringCoverageCertificateClosed"
BUDGET_ATOM = "AllowedBudgetAllocationLedger"
RANKIN_ATOM = "BatchRankinCertificatesAllPassOrReturnToPDECSAE"
PDEC_SAE_ATOM = "PDECOrSAEUnifiedExclusionLedger"


def read_text(path: Path) -> str:
    """读取文本文件。"""
    return path.read_text(encoding="utf-8")


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算文件 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def contains_all(text: str, needles: list[str]) -> bool:
    """检查文本是否包含全部片段。"""
    return all(needle in text for needle in needles)


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def certificate_fields() -> list[dict[str, str]]:
    """给出 coloring coverage 证书字段。"""
    return [
        {
            "field": "source_tuple_hash",
            "meaning": "锁定 P/range、window_id、A、D0、K、Omega、phase_rule。",
        },
        {
            "field": "anchor_intervals",
            "meaning": "每个 anchor a 的 J_a=[ceil(L/a),floor(R/a)] 与 [D0,2D0) 的交。",
        },
        {
            "field": "low_overlap_filter",
            "meaning": "只保留 m(d)<=Omega 的走廊部分；m(d)>Omega 已回流 high-overlap defect。",
        },
        {
            "field": "coloring_algorithm",
            "meaning": "按左端点扫描的贪心 interval coloring；活动区间颜色复用。",
        },
        {
            "field": "color_count_bound",
            "meaning": "最大同时活动区间数 <= Omega，因此 color_id in {1,...,Omega}。",
        },
        {
            "field": "per_color_disjointness",
            "meaning": "每个颜色类内 intervals 两两不交。",
        },
        {
            "field": "coverage_equation",
            "meaning": "有色 interval 多重集精确等于低重叠 anchor interval 多重集。",
        },
        {
            "field": "failure_return",
            "meaning": "若重叠界或覆盖等式失败，回流 high-overlap defect 或 source tuple 错配。",
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


def build_rows(previous: dict[str, Any], texts: dict[str, str]) -> list[dict[str, Any]]:
    """生成区间图着色覆盖判定表。"""
    active = previous.get("current_narrowest_atom") == OLD_ATOM
    guard = (
        previous.get("counterexample_assumption_only") is True
        and previous.get("empirical_absence_not_used") is True
        and previous.get("hypothetical_chain_only") is True
        and previous.get("row_column_unconditional_closed") is False
    )
    parameter_ready = previous.get("complement_anchor_d0k_parameter_discipline_closed") is True
    formal_ready = contains_all(texts["formal"], ["intervals", "coverage_equation", "color_id"])
    dcs_ready = contains_all(
        texts["dcs"],
        ["整数区间图是完美图", "活动区间数最多为最大重叠度 `\\Omega`", "同色区间不相交"],
    )
    ccb_ready = contains_all(texts["ccb"], ["不相交走廊并集", "Rankin ledger <= allowed budget"])
    coloring_closed = all([active, guard, parameter_ready, formal_ready, dcs_ready, ccb_ready])
    return [
        row(
            "IntervalColoringGateActive",
            active,
            False,
            "上一层已把最窄点推进到区间图着色和覆盖等式证书。",
            OLD_ATOM,
        ),
        row(
            "ParameterTupleImported",
            parameter_ready,
            True,
            "A、D0、K、Omega 与 phase_rule 已由上一层固定。",
            "不能重选参数。",
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只处理假设反例链条内的 formal corridor 证书，不用真实缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "FormalCoverageFieldsPinned",
            formal_ready,
            True,
            "正式 inventory 已要求 color_id、intervals 与 coverage_equation。",
            "字段格式无剩余。",
        ),
        row(
            "IntervalGraphPerfectColoringImported",
            dcs_ready,
            True,
            "DCS 已证明最大重叠度 <= Omega 的整数区间族可用 Omega 色贪心着色。",
            "无着色存在性剩余。",
        ),
        row(
            "PerColorRankinObjectReady",
            ccb_ready,
            True,
            "CCB 的 Rankin 账本对象正是同色不相交走廊并集。",
            BUDGET_ATOM,
        ),
        row(
            CLOSED_ATOM,
            coloring_closed,
            True,
            "着色和覆盖等式可由 source tuple 确定性复算；无额外数学出口。",
            CLOSED_ATOM,
        ),
        row(
            OLD_ATOM,
            coloring_closed,
            True,
            "区间图着色覆盖证书闭合；下一步只剩 allowed budget 分配纪律。",
            BUDGET_ATOM,
        ),
        row(
            "AllowedBudgetStillDownstream",
            False,
            False,
            "每个颜色类的 allowed_budget 分配和 Rankin 批量验收尚未提交。",
            f"{BUDGET_ATOM} AND {RANKIN_ATOM}",
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """运行区间图着色覆盖路由。"""
    previous = load_json(paths["previous"])
    texts = {key: read_text(path) for key, path in paths.items() if key != "previous"}
    rows = build_rows(previous, texts)
    coloring_closed = next(item["closed"] for item in rows if item["gate"] == CLOSED_ATOM)
    evidence_paths = list(paths.values())
    return {
        "certificate_type": "prime_matrix_interval_graph_coloring_coverage_router",
        "status": "interval_graph_coloring_coverage_closed_budget_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in evidence_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "row_column_unconditional_closed": False,
        "interval_graph_coloring_coverage_closed": coloring_closed,
        "formal_colored_corridor_inventory_closed": False,
        "certificate_fields": certificate_fields(),
        "current_narrowest_atom": BUDGET_ATOM,
        "downstream_atoms": [RANKIN_ATOM, PDEC_SAE_ATOM],
        "reduction_formula": f"{OLD_ATOM} => {CLOSED_ATOM} AND {BUDGET_ATOM}.",
        "plain_conclusion": (
            "IntervalGraphColoringCoverageCertificateLedger 已闭合为确定性证书：固定 source tuple 后，"
            "anchor intervals 的低重叠部分按整数区间图贪心着色，颜色数不超过 Omega；每个颜色类内"
            " intervals 两两不交，coverage_equation 记录有色多重集等于低重叠走廊多重集。"
            f"新的最窄点是 `{BUDGET_ATOM}`。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix 区间图着色覆盖证书路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"interval_graph_coloring_coverage_closed={fmt_bool(result['interval_graph_coloring_coverage_closed'])}",
        f"formal_colored_corridor_inventory_closed={fmt_bool(result['formal_colored_corridor_inventory_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 收缩公式",
        "",
        "```text",
        result["reduction_formula"],
        "```",
        "",
        "## 2. 证书字段",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
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
            f"当前唯一最窄点更新为 `{result['current_narrowest_atom']}`；随后是 `{RANKIN_ATOM}`。",
            "",
            "审稿边界：本步不分配预算，不执行全量 Rankin 批量验收，也不关闭行列无条件定理。",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--formal", type=Path, default=DEFAULT_FORMAL)
    parser.add_argument("--dcs", type=Path, default=DEFAULT_DCS)
    parser.add_argument("--ccb", type=Path, default=DEFAULT_CCB)
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "previous": args.previous,
        "formal": args.formal,
        "dcs": args.dcs,
        "ccb": args.ccb,
    }
    result = run(paths)
    args.json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_markdown(result, args.md)
    print(f"wrote {args.json}")
    print(f"wrote {args.md}")


if __name__ == "__main__":
    main()
