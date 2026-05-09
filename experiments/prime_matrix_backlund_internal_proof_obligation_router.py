#!/usr/bin/env python3
"""Prime Matrix Backlund 内部证明义务终局路由器。

用法示例：
  python3 experiments/prime_matrix_backlund_internal_proof_obligation_router.py

输出：
  docs/monograph/prime-matrix-backlund-internal-proof-obligation-router.json
  docs/monograph/prime-matrix-backlund-internal-proof-obligation-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONO = ROOT / "docs" / "monograph"

DEFAULT_FINAL = MONO / "prime-matrix-backlund-final-branch-status-router.json"
DEFAULT_ABSORB = MONO / "prime-matrix-backlund-indent-weight-absorption-router.json"
DEFAULT_POINTWISE = MONO / "prime-matrix-backlund-pointwise-core-transfer-obstruction-router.json"
DEFAULT_STIELTJES = MONO / "prime-matrix-backlund-boundary-stieltjes-jump-transfer-router.json"
DEFAULT_ODD = MONO / "prime-matrix-backlund-odd-correction-terminal-router.json"
DEFAULT_JSON = MONO / "prime-matrix-backlund-internal-proof-obligation-router.json"
DEFAULT_MD = MONO / "prime-matrix-backlund-internal-proof-obligation-router.md"

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


def proof_obligations() -> list[dict[str, str]]:
    """内部证明经典 Backlund 缩进成本的不可压缩义务。"""
    return [
        {
            "obligation": "LocalContourDeformationWithZeros",
            "must_prove": "对每个短窗口和每个近零 cluster，给出避零轮廓、缩进弧、极限方向和解析重数登记。",
            "why_needed": "端点 convention 只定义极限；它不证明移动窗口中的近零核心预算。",
        },
        {
            "obligation": "BudgetPreservingJumpAccounting",
            "must_prove": "未配对 jump 的 log(T) 系数为 0，或等价地证明所有正比例跳变已在同一恒等式中抵消。",
            "why_needed": "任何 Jensen C16 规模的未配对 jump 都产生约 50.265 的系数，远超 5/64 余量。",
        },
        {
            "obligation": "NoRVMCircularity",
            "must_prove": "证明不得使用由待证 Backlund C_S 推出的 RVM/C_N=16 局部计数。",
            "why_needed": "RVM->CN16 已明确依赖原始 arg zeta 常数 C_S=8；反向调用会循环。",
        },
        {
            "obligation": "NoDoubleCountingAcrossJensenAndIndent",
            "must_prove": "近零点不能同时在 Jensen 计数、RVM 端点计数和凹口成本中重复扣费。",
            "why_needed": "C_S=8 是紧等号，窗口稳定余量只有 5/64，没有多余正预算。",
        },
        {
            "obligation": "C8ReaggregationPreserved",
            "must_prove": "缩进内部证明完成后，仍能保持 bridge factor=1/2 与 C_boundary=16 合成 C_S=8。",
            "why_needed": "若缩进证明引入任何额外常数，Backlund 外层常数立即失配。",
        },
    ]


def blocked_routes() -> list[dict[str, str]]:
    """已审查阻断或归并的路线。"""
    return [
        {
            "route": "LittlewoodWeightAbsorption",
            "status": "blocked",
            "reason": "横向权重 beta-a 不能统一支付贴边界点态跳变。",
        },
        {
            "route": "PointwiseCoreTransfer",
            "status": "blocked",
            "reason": "矩形平均层无法无乘子转成短窗口点态核心。",
        },
        {
            "route": "BoundaryStieltjesFreeTransfer",
            "status": "terminal_equivalent",
            "reason": "形式跳变公式可闭合，但预算保持正是凹口成本本身。",
        },
        {
            "route": "HalfMirrorAverageCancellation",
            "status": "blocked",
            "reason": "半平均不能证明原始 trace 奇部为 0。",
        },
        {
            "route": "OddCorrectionRoute",
            "status": "terminal_equivalent",
            "reason": "奇部修正成本已经归并为 Backlund 近零凹口成本。",
        },
    ]


def build_rows(
    final: dict[str, Any],
    absorb: dict[str, Any],
    pointwise: dict[str, Any],
    stieltjes: dict[str, Any],
    odd: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成内部证明义务判定表。"""
    old_remaining_active = final.get("self_contained_remaining") == INDENT_COST
    absorption_reduced = absorb.get("replacement_self_contained", {}).get(INDENT_COST) is not None
    pointwise_blocked = pointwise.get("support_mismatch_obstruction_closed") is True
    stieltjes_terminal = stieltjes.get("next_priority") == INTERNAL_PROOF
    odd_terminal = odd.get("odd_correction_terminal_equivalence_closed") is True
    guard = (
        final.get("counterexample_assumption_only") is True
        and final.get("empirical_absence_not_used") is True
        and final.get("hypothetical_chain_only") is True
    )
    return [
        row(
            "OldIndentCostRemainingActive",
            old_remaining_active,
            True,
            "旧最终状态中的严格自足剩余仍是 Backlund 近零凹口成本。",
            INDENT_COST,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只做假设链条内解析证明义务审查，不使用真实零行缺席。",
            "保持 row_column_self_contained_closed=false。",
        ),
        row(
            "WeightAbsorptionReducedNotClosed",
            absorption_reduced,
            True,
            "零点权重吸收已压成经典缩进引理内部化，而非直接闭合。",
            INTERNAL_PROOF,
        ),
        row(
            "PointwiseSupportMismatchClosed",
            pointwise_blocked,
            True,
            "点态核心转移的直接乘子路线已被横向支撑/纵向跳变不匹配阻断。",
            INTERNAL_PROOF,
        ),
        row(
            "StieltjesRouteTerminal",
            stieltjes_terminal,
            True,
            "边界 Stieltjes 形式层闭合，预算层终端等价于经典缩进成本。",
            INTERNAL_PROOF,
        ),
        row(
            "OddCorrectionTerminalImported",
            odd_terminal,
            True,
            "原始奇部修正没有新自由度，已归并回凹口成本。",
            INTERNAL_PROOF,
        ),
        row(
            INTERNAL_PROOF,
            False,
            False,
            "当前仓库没有完成经典 Backlund 零点缩进成本的作者侧内部证明。",
            f"{INTERNAL_PROOF} OR {EXTERNAL_ATOM}",
        ),
        row(
            "RowColumnSelfContainedClosed",
            False,
            False,
            "严格自足行/列命题仍未闭合；不能作者侧声明完整无条件证明。",
            INTERNAL_PROOF,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行内部证明义务终局审查。"""
    final = load_json(paths["final"])
    absorb = load_json(paths["absorb"])
    pointwise = load_json(paths["pointwise"])
    stieltjes = load_json(paths["stieltjes"])
    odd = load_json(paths["odd"])
    rows = build_rows(final, absorb, pointwise, stieltjes, odd)
    source_paths = [path for name, path in paths.items() if name not in {"json_out", "md_out"}]
    return {
        "certificate_type": "prime_matrix_backlund_internal_proof_obligation_router",
        "status": "backlund_internal_proof_obligation_unique_remaining_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "strict_self_contained_unique_remaining": INTERNAL_PROOF,
        "equivalent_old_remaining": INDENT_COST,
        "external_escape": EXTERNAL_ATOM,
        "parallel_priority": DSTRUCTURE,
        "row_column_self_contained_closed": False,
        "row_column_external_backlund_closed": False,
        "proof_obligations": proof_obligations(),
        "blocked_routes": blocked_routes(),
        "plain_conclusion": (
            "严格自足路线的唯一剩余已经不能再压成权重吸收、点态转移、Stieltjes 免费转移或镜像抵消。"
            "这些路线均已被阻断或终端归并。"
            "最新精确定名的剩余是 `ClassicalBacklundZeroIndentationCostInternalProofLedger`，"
            "它等价于旧的 `BacklundZeroProximityIndentationCostLedger`，但明确要求作者侧完整重证经典 Backlund 零点缩进成本。"
            "在该内部证明或外部引理接受之前，行/列命题不能声明无条件自足闭合。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix Backlund 内部证明义务终局路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"strict_self_contained_unique_remaining={result['strict_self_contained_unique_remaining']}",
        f"equivalent_old_remaining={result['equivalent_old_remaining']}",
        f"row_column_self_contained_closed={fmt_bool(result['row_column_self_contained_closed'])}",
        f"row_column_external_backlund_closed={fmt_bool(result['row_column_external_backlund_closed'])}",
        "```",
        "",
        "## 1. 已阻断或归并路线",
        "",
        "| route | status | reason |",
        "| --- | --- | --- |",
    ]
    for item in result["blocked_routes"]:
        lines.append(
            f"| `{table_cell(item['route'])}` | `{table_cell(item['status'])}` | {table_cell(item['reason'])} |"
        )
    lines.extend(
        [
            "",
            "## 2. 内部证明不可压缩义务",
            "",
            "| obligation | must prove | why needed |",
            "| --- | --- | --- |",
        ]
    )
    for item in result["proof_obligations"]:
        lines.append(
            f"| `{table_cell(item['obligation'])}` | {table_cell(item['must_prove'])} | "
            f"{table_cell(item['why_needed'])} |"
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
            f"严格自足唯一剩余：`{result['strict_self_contained_unique_remaining']}`。",
            f"外部可接受逃逸门：`{result['external_escape']}`。",
            f"外部路线仍需独立验收门：`{result['parallel_priority']}`。",
            "",
            "判定：这是当前作者侧证明链条的真正终端硬点；尚未闭合。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--final-json", type=Path, default=DEFAULT_FINAL)
    parser.add_argument("--absorb-json", type=Path, default=DEFAULT_ABSORB)
    parser.add_argument("--pointwise-json", type=Path, default=DEFAULT_POINTWISE)
    parser.add_argument("--stieltjes-json", type=Path, default=DEFAULT_STIELTJES)
    parser.add_argument("--odd-json", type=Path, default=DEFAULT_ODD)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "final": args.final_json,
        "absorb": args.absorb_json,
        "pointwise": args.pointwise_json,
        "stieltjes": args.stieltjes_json,
        "odd": args.odd_json,
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
