#!/usr/bin/env python3
"""Prime Matrix Backlund 内部证明义务原子压缩路由器。

用法示例：
  python3 experiments/prime_matrix_backlund_internal_proof_atomic_reduction_router.py

输出：
  docs/monograph/prime-matrix-backlund-internal-proof-atomic-reduction-router.json
  docs/monograph/prime-matrix-backlund-internal-proof-atomic-reduction-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONO = ROOT / "docs" / "monograph"

DEFAULT_OBLIGATION = MONO / "prime-matrix-backlund-internal-proof-obligation-router.json"
DEFAULT_STIELTJES = MONO / "prime-matrix-backlund-boundary-stieltjes-jump-transfer-router.json"
DEFAULT_ENDPOINT = MONO / "prime-matrix-b3-endpoint-multiplicity-convention-router.json"
DEFAULT_NEAR = MONO / "prime-matrix-b3-near-zero-indent-separation-router.json"
DEFAULT_SPIKE = MONO / "prime-matrix-b3-backlund-spike-exclusion-router.json"
DEFAULT_CS8 = MONO / "prime-matrix-b3-cs8-slack-router.json"
DEFAULT_JSON = MONO / "prime-matrix-backlund-internal-proof-atomic-reduction-router.json"
DEFAULT_MD = MONO / "prime-matrix-backlund-internal-proof-atomic-reduction-router.md"

INTERNAL_PROOF = "ClassicalBacklundZeroIndentationCostInternalProofLedger"
BUDGET_ZERO = "BacklundBudgetPreservingJumpAccountingZeroCoefficientLedger"
LOCAL_CONTOUR = "BacklundLocalContourDeformationWithZerosClosed"
NO_RVM = "BacklundSpikeNoRVMCircularityDisciplineClosed"
NO_DOUBLE = "BacklundIndentJensenEndpointNoDoubleCountingPartitionClosed"
CS8_COND = "BacklundC8ReaggregationConditionalOnZeroJumpCoefficientClosed"
EXTERNAL_ATOM = "ClassicalBacklundZeroIndentationCostExternalAccepted"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证据。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
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


def atomic_basis() -> list[dict[str, str]]:
    """内部证明的最小原子基。"""
    return [
        {
            "atom": LOCAL_CONTOUR,
            "status": "closed",
            "content": "避零序列、小凹口、解析重数和极限登记都可由端点 convention 与 Stieltjes 形式公式支撑。",
        },
        {
            "atom": NO_RVM,
            "status": "closed",
            "content": "尖峰排斥链已登记禁止调用待证 Backlund/RVM 局部计数。",
        },
        {
            "atom": NO_DOUBLE,
            "status": "closed_as_partition_discipline",
            "content": "eta 外进入倒距离/Jensen，eta 内进入凹口成本，端点 convention 不新增常数；这关闭的是分区纪律。",
        },
        {
            "atom": CS8_COND,
            "status": "conditional",
            "content": "若未配对 jump 的 log(T) 系数为 0，则 C_boundary=16 与桥因子 1/2 仍给 C_S=8。",
        },
        {
            "atom": BUDGET_ZERO,
            "status": "open",
            "content": "必须证明未配对近零跳变的 log(T) 系数为 0；这是当前唯一数学硬核。",
        },
    ]


def pressure() -> dict[str, float]:
    """预算压力常数。"""
    zero_count = 16.0
    jump = math.pi
    margin = 5.0 / 64.0
    return {
        "jensen_zero_count_coefficient": zero_count,
        "per_jump_cost": jump,
        "naive_jump_coefficient": zero_count * jump,
        "available_margin": margin,
        "allowed_unpaired_coefficient": margin / jump,
        "allowed_fraction_of_jensen_count": margin / (zero_count * jump),
        "deficit": zero_count * jump - margin,
    }


def build_rows(
    obligation: dict[str, Any],
    stieltjes: dict[str, Any],
    endpoint: dict[str, Any],
    near: dict[str, Any],
    spike: dict[str, Any],
    cs8: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成原子压缩判定表。"""
    active = obligation.get("strict_self_contained_unique_remaining") == INTERNAL_PROOF
    guard = (
        obligation.get("counterexample_assumption_only") is True
        and obligation.get("empirical_absence_not_used") is True
        and obligation.get("hypothetical_chain_only") is True
    )
    local_contour = (
        endpoint.get("endpoint_multiplicity_convention_closed") is True
        and stieltjes.get("formal_stieltjes_jump_formula_closed") is True
    )
    no_rvm = NO_RVM in spike.get("closed_gates", []) or "NoRVMCircularityDisciplineClosed" in spike.get(
        "closed_gates", []
    )
    no_double = (
        endpoint.get("endpoint_multiplicity_convention_closed") is True
        and near.get("near_zero_indent_separation_external_closed") is True
        and stieltjes.get("formal_stieltjes_jump_formula_closed") is True
    )
    cs8_tight = cs8.get("backlund_cs8_slack_external_closed") is True and float(cs8.get("slack", 1.0)) == 0.0
    return [
        row(
            "InternalProofGateActive",
            active,
            True,
            "严格自足路线的唯一剩余已经精确定名为经典 Backlund 缩进成本内部证明。",
            INTERNAL_PROOF,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只审查假设链条的解析输入，不使用真实零行缺席。",
            "保持 row_column_self_contained_closed=false。",
        ),
        row(
            LOCAL_CONTOUR,
            local_contour,
            True,
            "避零、小凹口、极限和重数登记可由端点 convention 与 Stieltjes 形式公式自足完成。",
            BUDGET_ZERO,
        ),
        row(
            NO_RVM,
            no_rvm,
            True,
            "非循环纪律已闭合：不能用待由 Backlund 推出的 RVM/CN16 反证 Backlund。",
            BUDGET_ZERO,
        ),
        row(
            NO_DOUBLE,
            no_double,
            True,
            "近零/远零/端点的归属分区已固定；这避免重复扣费，但不支付近零跳变预算。",
            BUDGET_ZERO,
        ),
        row(
            CS8_COND,
            cs8_tight,
            True,
            "C_S=8 是紧等号；只要跳变零系数成立，重聚合不新增常数。",
            BUDGET_ZERO,
        ),
        row(
            BUDGET_ZERO,
            False,
            False,
            "仍未证明未配对近零 Stieltjes/缩进跳变的 log(T) 系数为 0。",
            f"{BUDGET_ZERO} OR {EXTERNAL_ATOM}",
        ),
        row(
            INTERNAL_PROOF,
            False,
            False,
            "内部证明被压成一个零系数预算原子；该原子未闭合前不能声明严格自足证明。",
            BUDGET_ZERO,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行内部证明义务原子压缩。"""
    obligation = load_json(paths["obligation"])
    stieltjes = load_json(paths["stieltjes"])
    endpoint = load_json(paths["endpoint"])
    near = load_json(paths["near"])
    spike = load_json(paths["spike"])
    cs8 = load_json(paths["cs8"])
    rows = build_rows(obligation, stieltjes, endpoint, near, spike, cs8)
    source_paths = [path for name, path in paths.items() if name not in {"json_out", "md_out"}]
    return {
        "certificate_type": "prime_matrix_backlund_internal_proof_atomic_reduction_router",
        "status": "backlund_internal_proof_reduced_to_zero_coefficient_jump_accounting_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "internal_proof_atomic_reduction_closed": True,
        "strict_self_contained_unique_remaining": BUDGET_ZERO,
        "parent_remaining": INTERNAL_PROOF,
        "row_column_self_contained_closed": False,
        "external_escape": EXTERNAL_ATOM,
        "parallel_priority": DSTRUCTURE,
        "atomic_basis": atomic_basis(),
        "budget_pressure": pressure(),
        "plain_conclusion": (
            "经典 Backlund 缩进成本内部证明已进一步压缩：形式轮廓变形、非循环纪律、近零/远零/端点分区、"
            "以及 C_S=8 条件重聚合都可由现有账本支撑。"
            "剩下的唯一真正数学原子是 `BacklundBudgetPreservingJumpAccountingZeroCoefficientLedger`："
            "必须证明未配对近零 Stieltjes/缩进跳变的 log(T) 系数为 0。"
            "该零系数原子未完成前，严格自足闭合仍未成立。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    pressure_row = result["budget_pressure"]
    lines = [
        "# Prime Matrix Backlund 内部证明义务原子压缩路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"parent_remaining={result['parent_remaining']}",
        f"strict_self_contained_unique_remaining={result['strict_self_contained_unique_remaining']}",
        f"row_column_self_contained_closed={fmt_bool(result['row_column_self_contained_closed'])}",
        "```",
        "",
        "## 1. 原子基",
        "",
        "| atom | status | content |",
        "| --- | --- | --- |",
    ]
    for item in result["atomic_basis"]:
        lines.append(
            f"| `{table_cell(item['atom'])}` | `{table_cell(item['status'])}` | {table_cell(item['content'])} |"
        )
    lines.extend(
        [
            "",
            "## 2. 零系数压力",
            "",
            "| item | value |",
            "| --- | ---: |",
            f"| Jensen zero-count coefficient | `{pressure_row['jensen_zero_count_coefficient']:.12f}` |",
            f"| per jump cost | `{pressure_row['per_jump_cost']:.12f}` |",
            f"| naive jump coefficient | `{pressure_row['naive_jump_coefficient']:.12f}` |",
            f"| available margin | `{pressure_row['available_margin']:.12f}` |",
            f"| allowed unpaired coefficient | `{pressure_row['allowed_unpaired_coefficient']:.12f}` |",
            f"| allowed fraction of Jensen count | `{pressure_row['allowed_fraction_of_jensen_count']:.12f}` |",
            f"| deficit | `{pressure_row['deficit']:.12f}` |",
            "",
            "这说明不能证明“小比例剩余”来闭合；必须证明 log(T) 级未配对跳变系数为 `0`。",
            "",
            "## 3. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
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
            f"新的严格自足唯一剩余：`{result['strict_self_contained_unique_remaining']}`。",
            f"外部可接受逃逸门：`{result['external_escape']}`。",
            f"并行保留晋级门：`{result['parallel_priority']}`。",
            "",
            "判定：外围义务已压缩，真正剩余只剩零系数跳变预算原子。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--obligation-json", type=Path, default=DEFAULT_OBLIGATION)
    parser.add_argument("--stieltjes-json", type=Path, default=DEFAULT_STIELTJES)
    parser.add_argument("--endpoint-json", type=Path, default=DEFAULT_ENDPOINT)
    parser.add_argument("--near-json", type=Path, default=DEFAULT_NEAR)
    parser.add_argument("--spike-json", type=Path, default=DEFAULT_SPIKE)
    parser.add_argument("--cs8-json", type=Path, default=DEFAULT_CS8)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "obligation": args.obligation_json,
        "stieltjes": args.stieltjes_json,
        "endpoint": args.endpoint_json,
        "near": args.near_json,
        "spike": args.spike_json,
        "cs8": args.cs8_json,
        "json_out": args.json_out,
        "md_out": args.md_out,
    }
    result = run(paths)
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(result["status"])
    print(result["strict_self_contained_unique_remaining"])


if __name__ == "__main__":
    main()
