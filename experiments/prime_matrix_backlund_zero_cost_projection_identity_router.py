#!/usr/bin/env python3
"""Prime Matrix Backlund 零成本镜像投影身份路由器。

用法示例：
  python3 experiments/prime_matrix_backlund_zero_cost_projection_identity_router.py

输出：
  docs/monograph/prime-matrix-backlund-zero-cost-projection-identity-router.json
  docs/monograph/prime-matrix-backlund-zero-cost-projection-identity-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONO = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = MONO / "prime-matrix-backlund-symmetric-doubling-capacity-router.json"
DEFAULT_TRANSPORT = MONO / "prime-matrix-backlund-zeta-xi-branch-jump-transport-router.json"
DEFAULT_LEFT = MONO / "prime-matrix-b3-functional-equation-left-edge-router.json"
DEFAULT_JSON = MONO / "prime-matrix-backlund-zero-cost-projection-identity-router.json"
DEFAULT_MD = MONO / "prime-matrix-backlund-zero-cost-projection-identity-router.md"

ZERO_COST_ATOM = "BacklundZeroCostMirrorProjectionIdentityLedger"
HALF_AVERAGE_ATOM = "BacklundOriginalTraceHalfMirrorAverageIdentityLedger"
ODD_JUMP_ATOM = "BacklundMirrorOddJumpCancellationIdentityLedger"
EVEN_GAMMA_ATOM = "BacklundEvenGammaElementaryRemainderBudgetLedger"
HALF_WEIGHT_ATOM = "BacklundHalfWeightSymmetricTraceNormalizationLedger"
NO_DOUBLE_ATOM = "BacklundNoDoubleCountingMirrorBoundaryLedger"
ORIENTATION_ATOM = "BacklundMirrorIndentArcOrientationLedger"
PROJECTION_ATOM = "BacklundOriginalTraceProjectionNoLossLedger"
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


def projection_modes() -> list[dict[str, str]]:
    """区分两种投影，防止伪闭合。"""
    return [
        {
            "mode": "coordinate_projection",
            "effect": "保留原始 Backlund trace，但镜像不会自动抵消原 trace 的 crossing 成本。",
        },
        {
            "mode": "symmetric_half_average",
            "effect": "可让镜像奇部抵消，但必须先证明半平均严格等于原始目标加已预算的偶部余项。",
        },
    ]


def lower_atoms() -> list[dict[str, str]]:
    """零成本镜像投影身份的下层原子。"""
    return [
        {
            "atom": HALF_AVERAGE_ATOM,
            "role": "证明原始 Backlund trace 等于 xi 镜像半平均加显式 Gamma/初等偶部余项。",
        },
        {
            "atom": ODD_JUMP_ATOM,
            "role": "证明 crossing branch_jump 属于镜像奇部，因此在半平均中逐项抵消。",
        },
        {
            "atom": EVEN_GAMMA_ATOM,
            "role": "证明镜像偶部只剩 Gamma/初等连续相位，并已由既有预算吸收。",
        },
    ]


def build_rows(previous: dict[str, Any], transport: dict[str, Any], left: dict[str, Any]) -> list[dict[str, Any]]:
    """生成零成本镜像投影身份判定表。"""
    active = previous.get("next_priority") == ZERO_COST_ATOM
    guard = (
        previous.get("counterexample_assumption_only") is True
        and previous.get("empirical_absence_not_used") is True
        and previous.get("hypothetical_chain_only") is True
    )
    transport_ready = transport.get("zeta_xi_branch_jump_transport_closed") is True
    left_ready = left.get("functional_equation_left_edge_closed") is True
    false_projection_blocked = True
    reduction_closed = active and guard and transport_ready and left_ready and false_projection_blocked
    return [
        row(
            "ZeroCostProjectionGateActive",
            active,
            True,
            "doubling 容量纪律后，当前最窄点是零成本镜像投影身份。",
            ZERO_COST_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只处理假设链条的解析恒等式，不使用真实零行缺席。",
            "保持 row_column_self_contained_closed=false。",
        ),
        row(
            "ZetaXiJumpTransportAvailable",
            transport_ready,
            True,
            "zeta branch_jump 已搬运到 xi；因此镜像奇偶分解可以在 xi 语言中表达。",
            ODD_JUMP_ATOM,
        ),
        row(
            "LeftRightFunctionalEquationBridgeAvailable",
            left_ready,
            True,
            "左/右边界函数方程桥已闭合，提供半镜像平均的边界身份基础。",
            HALF_AVERAGE_ATOM,
        ),
        row(
            "CoordinateProjectionFalseClosureBlocked",
            false_projection_blocked,
            True,
            "只投影回原 trace 虽然零成本，但不能带来抵消；必须证明半平均身份。",
            HALF_AVERAGE_ATOM,
        ),
        row(
            "ZeroCostProjectionReducedToHalfAverageIdentity",
            reduction_closed,
            False,
            "零成本投影已压成半镜像平均身份、奇部跳变抵消、偶部 Gamma 余项预算三包。",
            f"{HALF_AVERAGE_ATOM} AND {ODD_JUMP_ATOM} AND {EVEN_GAMMA_ATOM}",
        ),
        row(
            HALF_AVERAGE_ATOM,
            False,
            False,
            "尚未证明原始 Backlund 目标等于半镜像平均加已预算偶部。",
            HALF_AVERAGE_ATOM,
        ),
        row(
            ODD_JUMP_ATOM,
            False,
            False,
            "尚未证明所有 crossing branch_jump 都进入镜像奇部并逐项抵消。",
            ODD_JUMP_ATOM,
        ),
        row(
            EVEN_GAMMA_ATOM,
            False,
            False,
            "尚未证明半平均留下的 Gamma/初等偶部不新增预算。",
            EVEN_GAMMA_ATOM,
        ),
        row(
            ZERO_COST_ATOM,
            False,
            False,
            "三包闭合后才可继续半权归一化和无重复扣费验收。",
            f"{HALF_WEIGHT_ATOM} AND {NO_DOUBLE_ATOM}",
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行零成本镜像投影身份路由。"""
    previous = load_json(paths["previous"])
    transport = load_json(paths["transport"])
    left = load_json(paths["left"])
    rows = build_rows(previous, transport, left)
    reduction_closed = next(
        item["closed"] for item in rows if item["gate"] == "ZeroCostProjectionReducedToHalfAverageIdentity"
    )
    source_paths = [path for name, path in paths.items() if name not in {"json_out", "md_out"}]
    return {
        "certificate_type": "prime_matrix_backlund_zero_cost_projection_identity_router",
        "status": "backlund_zero_cost_projection_reduced_to_half_average_identity_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "zero_cost_projection_reduction_closed": reduction_closed,
        "zero_cost_projection_identity_closed": False,
        "budget_preserving_doubling_closed": False,
        "backlund_local_crossing_trace_closed": False,
        "row_column_self_contained_closed": False,
        "projection_modes": projection_modes(),
        "lower_atoms": lower_atoms(),
        "replacement_self_contained": {
            ZERO_COST_ATOM: f"({HALF_AVERAGE_ATOM} AND {ODD_JUMP_ATOM} AND {EVEN_GAMMA_ATOM})"
        },
        "next_priority": HALF_AVERAGE_ATOM,
        "odd_jump_priority": ODD_JUMP_ATOM,
        "even_gamma_priority": EVEN_GAMMA_ATOM,
        "post_projection_priority": HALF_WEIGHT_ATOM,
        "post_normalization_priority": NO_DOUBLE_ATOM,
        "orientation_priority": ORIENTATION_ATOM,
        "projection_priority": PROJECTION_ATOM,
        "external_escape": EXTERNAL_ATOM,
        "parallel_priority": DSTRUCTURE,
        "plain_conclusion": (
            "零成本镜像投影不能用“坐标投影回原 trace”伪闭合；那样没有任何 crossing 抵消。"
            "真正需要证明的是半镜像平均身份：原始 Backlund trace 等于 xi 对称半平均加已预算的 Gamma/初等偶部，"
            "同时 crossing branch_jump 全部落入镜像奇部并逐项抵消。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement_self_contained"].items()))
    lines = [
        "# Prime Matrix Backlund 零成本镜像投影身份路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"zero_cost_projection_reduction_closed={fmt_bool(result['zero_cost_projection_reduction_closed'])}",
        f"zero_cost_projection_identity_closed={fmt_bool(result['zero_cost_projection_identity_closed'])}",
        f"budget_preserving_doubling_closed={fmt_bool(result['budget_preserving_doubling_closed'])}",
        f"backlund_local_crossing_trace_closed={fmt_bool(result['backlund_local_crossing_trace_closed'])}",
        f"row_column_self_contained_closed={fmt_bool(result['row_column_self_contained_closed'])}",
        "```",
        "",
        "## 1. 投影模式",
        "",
        "| mode | effect |",
        "| --- | --- |",
    ]
    for item in result["projection_modes"]:
        lines.append(f"| `{table_cell(item['mode'])}` | {table_cell(item['effect'])} |")
    lines.extend(
        [
            "",
            "## 2. 自足替换",
            "",
            "```text",
            replacement[0],
            "  =>",
            replacement[1],
            "```",
            "",
            "| atom | role |",
            "| --- | --- |",
        ]
    )
    for item in result["lower_atoms"]:
        lines.append(f"| `{table_cell(item['atom'])}` | {table_cell(item['role'])} |")
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
            f"当前真正最窄点：`{result['next_priority']}`。",
            f"奇部跳变验收：`{result['odd_jump_priority']}`。",
            f"偶部 Gamma 预算验收：`{result['even_gamma_priority']}`。",
            f"随后归一化验收：`{result['post_projection_priority']}`。",
            f"随后无重复扣费验收：`{result['post_normalization_priority']}`。",
            f"外部可接受逃逸门：`{result['external_escape']}`。",
            "",
            "判定：零成本镜像投影已压到半镜像平均身份；命题尚未自足闭合。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous-json", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--transport-json", type=Path, default=DEFAULT_TRANSPORT)
    parser.add_argument("--left-json", type=Path, default=DEFAULT_LEFT)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "previous": args.previous_json,
        "transport": args.transport_json,
        "left": args.left_json,
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
