#!/usr/bin/env python3
"""Prime Matrix Backlund 边界 Stieltjes 跳变转移终端路由器。

用法示例：
  python3 experiments/prime_matrix_backlund_boundary_stieltjes_jump_transfer_router.py

输出：
  docs/monograph/prime-matrix-backlund-boundary-stieltjes-jump-transfer-router.json
  docs/monograph/prime-matrix-backlund-boundary-stieltjes-jump-transfer-router.md
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

DEFAULT_POINTWISE = MONO / "prime-matrix-backlund-pointwise-core-transfer-obstruction-router.json"
DEFAULT_ENDPOINT = MONO / "prime-matrix-b3-endpoint-multiplicity-convention-router.json"
DEFAULT_TRANSPORT = MONO / "prime-matrix-backlund-zeta-xi-branch-jump-transport-router.json"
DEFAULT_HALF = MONO / "prime-matrix-backlund-half-mirror-average-obstruction-router.json"
DEFAULT_ODD = MONO / "prime-matrix-backlund-odd-correction-terminal-router.json"
DEFAULT_CS8 = MONO / "prime-matrix-b3-cs8-slack-router.json"
DEFAULT_JSON = MONO / "prime-matrix-backlund-boundary-stieltjes-jump-transfer-router.json"
DEFAULT_MD = MONO / "prime-matrix-backlund-boundary-stieltjes-jump-transfer-router.md"

STIELTJES_JUMP = "BacklundBoundaryStieltjesJumpTransferLedger"
FORMAL_STIELTJES = "BacklundBoundaryStieltjesJumpFormulaClosed"
BUDGET_TRANSFER = "BacklundBudgetPreservingStieltjesJumpTransferLedger"
SIGNED_CANCEL = "BacklundSignedCrossingPairingInvolutionLedger"
ODD_CORRECTION = "BacklundOddMirrorCorrectionCostLedger"
INDENT_COST = "BacklundZeroProximityIndentationCostLedger"
INTERNAL_PROOF = "ClassicalBacklundZeroIndentationCostInternalProofLedger"
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


def stieltjes_atoms() -> list[dict[str, str]]:
    """Stieltjes 跳变账本的最小拆解。"""
    return [
        {
            "atom": FORMAL_STIELTJES,
            "status": "closed",
            "role": "避零后取极限，把边界 arg 变化写成连续 log-derivative 变差加按重数计的跳变测度。",
        },
        {
            "atom": BUDGET_TRANSFER,
            "status": "open",
            "role": "证明该跳变测度不新增 C_S 或窗口余量成本；这要求精确抵消或外部缩进引理。",
        },
        {
            "atom": SIGNED_CANCEL,
            "status": "blocked_by_prior_reviews",
            "role": "此前半镜像/奇部为零路线已证明不能免费消掉原始 trace 的奇部。",
        },
        {
            "atom": INTERNAL_PROOF,
            "status": "only_strict_internal_remaining",
            "role": "若坚持完全自足，必须直接内部证明经典 Backlund 缩进成本，而不是再做权重或镜像转移。",
        },
    ]


def jump_budget_table() -> list[dict[str, float]]:
    """登记跳变预算压力。"""
    zero_count_coeff = 16.0
    per_jump = math.pi
    naive = zero_count_coeff * per_jump
    stability = 5.0 / 64.0
    return [
        {
            "zero_count_coefficient": zero_count_coeff,
            "per_unpaired_jump_cost": per_jump,
            "naive_jump_coefficient": naive,
            "available_stability_margin": stability,
            "deficit": naive - stability,
            "allowed_unpaired_coefficient": stability / per_jump,
        }
    ]


def build_rows(
    pointwise: dict[str, Any],
    endpoint: dict[str, Any],
    transport: dict[str, Any],
    half: dict[str, Any],
    odd: dict[str, Any],
    cs8: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 Stieltjes 跳变转移判定表。"""
    active = pointwise.get("next_priority") == STIELTJES_JUMP
    guard = (
        pointwise.get("counterexample_assumption_only") is True
        and pointwise.get("empirical_absence_not_used") is True
        and pointwise.get("hypothetical_chain_only") is True
    )
    endpoint_closed = endpoint.get("endpoint_multiplicity_convention_closed") is True
    transport_closed = transport.get("zeta_xi_branch_jump_transport_closed") is True
    half_obstruction = half.get("half_average_obstruction_closed") is True
    odd_terminal = odd.get("odd_correction_terminal_equivalence_closed") is True
    cs8_tight = cs8.get("backlund_cs8_slack_external_closed") is True and float(cs8.get("slack", 1.0)) == 0.0
    return [
        row(
            "BoundaryStieltjesJumpGateActive",
            active,
            True,
            "点态支撑不匹配后，唯一剩余被压成边界 Stieltjes 跳变/缩进账本。",
            STIELTJES_JUMP,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只处理假设链条中的解析 trace，不使用真实零行缺席。",
            "保持 row_column_self_contained_closed=false。",
        ),
        row(
            FORMAL_STIELTJES,
            endpoint_closed,
            True,
            "端点避零和重数极限 convention 足以给出跳变测度的形式登记。",
            BUDGET_TRANSFER,
        ),
        row(
            "ZetaXiJumpTransportAlreadyClosed",
            transport_closed,
            True,
            "跳变可从 arg zeta 搬运到 xi 零点重数；Gamma/初等因子不产生 crossing jump。",
            SIGNED_CANCEL,
        ),
        row(
            "HalfMirrorFreeCancellationBlocked",
            half_obstruction,
            True,
            "半镜像平均只能消掉平均 trace 的奇偶组合，不能证明原始 trace 奇部为零。",
            ODD_CORRECTION,
        ),
        row(
            "OddCorrectionEqualsIndentCost",
            odd_terminal,
            True,
            "原始 trace 的未配对跳变成本已终端归并为 Backlund 近零凹口成本。",
            INDENT_COST,
        ),
        row(
            "CS8HasNoResidualBudget",
            cs8_tight,
            True,
            "外部 C_S=8 已是 16*1/2 的紧等号；自足路线不能新增任何正比例 Stieltjes 跳变成本。",
            BUDGET_TRANSFER,
        ),
        row(
            BUDGET_TRANSFER,
            False,
            False,
            "形式跳变公式不等于预算保持；预算保持正是经典 Backlund 缩进成本本身。",
            INTERNAL_PROOF,
        ),
        row(
            STIELTJES_JUMP,
            False,
            False,
            "Stieltjes 路线没有产生新闭合自由度，终端回到内部证明经典缩进引理或接受外部引理。",
            f"{INTERNAL_PROOF} OR {EXTERNAL_ATOM}",
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行 Stieltjes 跳变转移终端审查。"""
    pointwise = load_json(paths["pointwise"])
    endpoint = load_json(paths["endpoint"])
    transport = load_json(paths["transport"])
    half = load_json(paths["half"])
    odd = load_json(paths["odd"])
    cs8 = load_json(paths["cs8"])
    rows = build_rows(pointwise, endpoint, transport, half, odd, cs8)
    source_paths = [path for name, path in paths.items() if name not in {"json_out", "md_out"}]
    budget = jump_budget_table()[0]
    return {
        "certificate_type": "prime_matrix_backlund_boundary_stieltjes_jump_transfer_router",
        "status": "backlund_boundary_stieltjes_jump_transfer_terminal_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "formal_stieltjes_jump_formula_closed": True,
        "budget_preserving_stieltjes_jump_transfer_closed": False,
        "indent_cost_self_contained_closed": False,
        "row_column_self_contained_closed": False,
        "jump_budget_pressure": budget,
        "stieltjes_atoms": stieltjes_atoms(),
        "terminal_equivalence": {
            STIELTJES_JUMP: f"{FORMAL_STIELTJES} AND {BUDGET_TRANSFER}",
            BUDGET_TRANSFER: f"{INTERNAL_PROOF} OR {EXTERNAL_ATOM}",
            INTERNAL_PROOF: INDENT_COST,
        },
        "next_priority": INTERNAL_PROOF,
        "external_escape": EXTERNAL_ATOM,
        "parallel_priority": DSTRUCTURE,
        "plain_conclusion": (
            "边界 Stieltjes 跳变公式本身可以自足登记：避零、应用 argument principle、再按重数取极限。"
            "但这只说明跳变在哪里，并不支付跳变预算。"
            "由于半镜像免费抵消和原始奇部为零都已被阻断，预算保持的 Stieltjes 转移与 Backlund 近零凹口成本等价。"
            "因此严格自足路线没有新的更小逃逸口；唯一剩余就是内部证明经典 Backlund 零点缩进成本，"
            "或明确接受外部经典 Backlund 缩进引理。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    budget = result["jump_budget_pressure"]
    lines = [
        "# Prime Matrix Backlund 边界 Stieltjes 跳变转移终端路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"formal_stieltjes_jump_formula_closed={fmt_bool(result['formal_stieltjes_jump_formula_closed'])}",
        (
            "budget_preserving_stieltjes_jump_transfer_closed="
            f"{fmt_bool(result['budget_preserving_stieltjes_jump_transfer_closed'])}"
        ),
        f"indent_cost_self_contained_closed={fmt_bool(result['indent_cost_self_contained_closed'])}",
        f"row_column_self_contained_closed={fmt_bool(result['row_column_self_contained_closed'])}",
        "```",
        "",
        "## 1. 形式恒等式与预算差别",
        "",
        "```text",
        "d arg F(a+it) = continuous log-derivative variation + pi * dN_boundary(t)",
        "boundary zeros are first avoided, then counted by analytic multiplicity in the limit",
        "```",
        "",
        "这条公式只登记跳变测度；若要闭合 `C_S=8`，还必须证明跳变测度不产生新的正比例成本。",
        "",
        "## 2. 跳变预算压力",
        "",
        "| item | value |",
        "| --- | ---: |",
        f"| Jensen zero-count coefficient | `{budget['zero_count_coefficient']:.12f}` |",
        f"| per unpaired jump cost | `{budget['per_unpaired_jump_cost']:.12f}` |",
        f"| naive jump coefficient | `{budget['naive_jump_coefficient']:.12f}` |",
        f"| available stability margin | `{budget['available_stability_margin']:.12f}` |",
        f"| allowed unpaired coefficient | `{budget['allowed_unpaired_coefficient']:.12f}` |",
        f"| deficit | `{budget['deficit']:.12f}` |",
        "",
        "结论：任何 Jensen 规模的未配对 Stieltjes 跳变都会立即超过稳定余量；预算保持必须是零系数级。",
        "",
        "## 3. Stieltjes 拆解",
        "",
        "| atom | status | role |",
        "| --- | --- | --- |",
    ]
    for item in result["stieltjes_atoms"]:
        lines.append(
            f"| `{table_cell(item['atom'])}` | `{table_cell(item['status'])}` | {table_cell(item['role'])} |"
        )
    lines.extend(
        [
            "",
            "## 4. 终端等价",
            "",
            "```text",
        ]
    )
    for key, value in result["terminal_equivalence"].items():
        lines.append(f"{key} => {value}")
    lines.extend(
        [
            "```",
            "",
            "## 5. 判定表",
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
            "## 6. 下一步",
            "",
            f"严格自足唯一剩余：`{result['next_priority']}`。",
            f"外部可接受逃逸门：`{result['external_escape']}`。",
            f"并行保留晋级门：`{result['parallel_priority']}`。",
            "",
            "判定：Stieltjes 形式层已闭合，预算层未闭合；它终端等价于 Backlund 近零凹口成本。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pointwise-json", type=Path, default=DEFAULT_POINTWISE)
    parser.add_argument("--endpoint-json", type=Path, default=DEFAULT_ENDPOINT)
    parser.add_argument("--transport-json", type=Path, default=DEFAULT_TRANSPORT)
    parser.add_argument("--half-json", type=Path, default=DEFAULT_HALF)
    parser.add_argument("--odd-json", type=Path, default=DEFAULT_ODD)
    parser.add_argument("--cs8-json", type=Path, default=DEFAULT_CS8)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "pointwise": args.pointwise_json,
        "endpoint": args.endpoint_json,
        "transport": args.transport_json,
        "half": args.half_json,
        "odd": args.odd_json,
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
    print(result["next_priority"])


if __name__ == "__main__":
    main()
