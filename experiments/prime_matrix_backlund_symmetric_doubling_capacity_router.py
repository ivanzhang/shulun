#!/usr/bin/env python3
"""Prime Matrix Backlund 对称 doubling 容量纪律路由器。

用法示例：
  python3 experiments/prime_matrix_backlund_symmetric_doubling_capacity_router.py

输出：
  docs/monograph/prime-matrix-backlund-symmetric-doubling-capacity-router.json
  docs/monograph/prime-matrix-backlund-symmetric-doubling-capacity-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONO = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = MONO / "prime-matrix-backlund-xi-formal-unit-contour-router.json"
DEFAULT_CS8 = MONO / "prime-matrix-b3-cs8-slack-router.json"
DEFAULT_CAPACITY = MONO / "prime-matrix-backlund-crossing-trace-capacity-router.json"
DEFAULT_JSON = MONO / "prime-matrix-backlund-symmetric-doubling-capacity-router.json"
DEFAULT_MD = MONO / "prime-matrix-backlund-symmetric-doubling-capacity-router.md"

DOUBLING_ATOM = "BacklundBudgetPreservingXiSymmetricContourDoublingLedger"
ZERO_COST_ATOM = "BacklundZeroCostMirrorProjectionIdentityLedger"
HALF_WEIGHT_ATOM = "BacklundHalfWeightSymmetricTraceNormalizationLedger"
NO_DOUBLE_ATOM = "BacklundNoDoubleCountingMirrorBoundaryLedger"
ORIENTATION_ATOM = "BacklundMirrorIndentArcOrientationLedger"
PROJECTION_ATOM = "BacklundOriginalTraceProjectionNoLossLedger"
FORMAL_UNIT_ATOM = "BacklundXiSymmetricFormalUnitContourLedger"
PAIRING_ATOM = "BacklundSignedCrossingPairingInvolutionLedger"
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


def fmt_float(value: float) -> str:
    """输出固定精度浮点数。"""
    return f"{value:.12f}"


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


def lower_atoms() -> list[dict[str, str]]:
    """对称 doubling 容量纪律下的真正下层原子。"""
    return [
        {
            "atom": ZERO_COST_ATOM,
            "role": "证明 xi 对称 doubling 是恒等式级投影，不产生任何新增 log(T) 预算项。",
        },
        {
            "atom": HALF_WEIGHT_ATOM,
            "role": "若使用 doubled trace，必须同步使用 1/2 归一化，使边界常数不从 16 变 32。",
        },
        {
            "atom": NO_DOUBLE_ATOM,
            "role": "证明镜像边界、镜像凹口和原边界没有被重复扣费。",
        },
    ]


def build_rows(previous: dict[str, Any], cs8: dict[str, Any], capacity: dict[str, Any]) -> list[dict[str, Any]]:
    """生成对称 doubling 容量纪律判定表。"""
    active = previous.get("next_priority") == DOUBLING_ATOM
    guard = (
        previous.get("counterexample_assumption_only") is True
        and previous.get("empirical_absence_not_used") is True
        and previous.get("hypothetical_chain_only") is True
    )
    cs8_tight = float(cs8.get("slack", 1.0)) == 0.0 and float(cs8.get("C_S_result", 0.0)) == float(
        cs8.get("C_S_target", -1.0)
    )
    residual_tiny = capacity.get("trace_capacity_reduction_closed") is True
    paid_doubling_forbidden = cs8_tight and residual_tiny
    reduction_closed = active and guard and paid_doubling_forbidden
    return [
        row(
            "SymmetricDoublingCapacityGateActive",
            active,
            True,
            "formal unit 路由后，当前最窄点是预算保持的 xi 对称 doubling。",
            DOUBLING_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只处理假设链条中的容量纪律，不使用真实零行缺席。",
            "保持 row_column_self_contained_closed=false。",
        ),
        row(
            "CS8SlackIsTight",
            cs8_tight,
            True,
            "Backlund C_S=8 余量是紧等号，slack=0；不能支付任何正的 doubling 乘子。",
            ZERO_COST_ATOM,
        ),
        row(
            "TraceResidualMarginAlreadyTiny",
            residual_tiny,
            True,
            "crossing trace 容量已证明凹口残余必须是零系数；不能让 doubled unit 新增正比例残留。",
            ZERO_COST_ATOM,
        ),
        row(
            "PaidDoublingForbidden",
            paid_doubling_forbidden,
            True,
            "如果 doubling 把边界或凹口预算乘以 2，则 C_S 由 8 变 16，立即破坏闭合目标。",
            ZERO_COST_ATOM,
        ),
        row(
            "DoublingReducedToZeroCostProjection",
            reduction_closed,
            False,
            "预算保持 doubling 已压成零成本镜像投影、半权归一化、无重复扣费三包。",
            f"{ZERO_COST_ATOM} AND {HALF_WEIGHT_ATOM} AND {NO_DOUBLE_ATOM}",
        ),
        row(
            ZERO_COST_ATOM,
            False,
            False,
            "尚未证明 doubled formal unit 是恒等式级投影而非新预算项。",
            ZERO_COST_ATOM,
        ),
        row(
            HALF_WEIGHT_ATOM,
            False,
            False,
            "尚未证明 doubled trace 的 1/2 归一化与原始 Backlund 目标严格等价。",
            HALF_WEIGHT_ATOM,
        ),
        row(
            NO_DOUBLE_ATOM,
            False,
            False,
            "尚未证明镜像边界和镜像凹口不会重复扣费。",
            NO_DOUBLE_ATOM,
        ),
        row(
            DOUBLING_ATOM,
            False,
            False,
            "三包闭合后才可继续验收镜像弧方向和原 trace 投影。",
            f"{ORIENTATION_ATOM} AND {PROJECTION_ATOM}",
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行对称 doubling 容量纪律路由。"""
    previous = load_json(paths["previous"])
    cs8 = load_json(paths["cs8"])
    capacity = load_json(paths["capacity"])
    rows = build_rows(previous, cs8, capacity)
    reduction_closed = next(item["closed"] for item in rows if item["gate"] == "DoublingReducedToZeroCostProjection")
    source_paths = [path for name, path in paths.items() if name not in {"json_out", "md_out"}]
    return {
        "certificate_type": "prime_matrix_backlund_symmetric_doubling_capacity_router",
        "status": "backlund_symmetric_doubling_reduced_to_zero_cost_projection_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "doubling_capacity_reduction_closed": reduction_closed,
        "budget_preserving_doubling_closed": False,
        "xi_symmetric_formal_unit_closed": False,
        "backlund_local_crossing_trace_closed": False,
        "row_column_self_contained_closed": False,
        "C_S_target": float(cs8["C_S_target"]),
        "C_S_result": float(cs8["C_S_result"]),
        "C_S_slack": float(cs8["slack"]),
        "paid_doubling_multiplier": 2.0,
        "paid_doubling_C_S_result": 2.0 * float(cs8["C_S_result"]),
        "lower_atoms": lower_atoms(),
        "replacement_self_contained": {
            DOUBLING_ATOM: f"({ZERO_COST_ATOM} AND {HALF_WEIGHT_ATOM} AND {NO_DOUBLE_ATOM})"
        },
        "next_priority": ZERO_COST_ATOM,
        "normalization_priority": HALF_WEIGHT_ATOM,
        "no_double_count_priority": NO_DOUBLE_ATOM,
        "post_doubling_priority": ORIENTATION_ATOM,
        "projection_priority": PROJECTION_ATOM,
        "parent_priority": FORMAL_UNIT_ATOM,
        "grandparent_priority": PAIRING_ATOM,
        "external_escape": EXTERNAL_ATOM,
        "parallel_priority": DSTRUCTURE,
        "plain_conclusion": (
            "预算保持 xi 对称 doubling 不能按普通双份轮廓付费。"
            "因为 Backlund C_S=8 已是紧等号，任何正的 doubling 乘子都会把 C_S 从 8 推到 16。"
            "所以当前最窄点被压成 `BacklundZeroCostMirrorProjectionIdentityLedger`："
            "必须证明对称化是在恒等式层完成的零成本投影，并配套半权归一化与无重复扣费纪律。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement_self_contained"].items()))
    lines = [
        "# Prime Matrix Backlund 对称 doubling 容量纪律路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"doubling_capacity_reduction_closed={fmt_bool(result['doubling_capacity_reduction_closed'])}",
        f"budget_preserving_doubling_closed={fmt_bool(result['budget_preserving_doubling_closed'])}",
        f"xi_symmetric_formal_unit_closed={fmt_bool(result['xi_symmetric_formal_unit_closed'])}",
        f"backlund_local_crossing_trace_closed={fmt_bool(result['backlund_local_crossing_trace_closed'])}",
        f"row_column_self_contained_closed={fmt_bool(result['row_column_self_contained_closed'])}",
        "```",
        "",
        "## 1. 容量纪律",
        "",
        "| item | value |",
        "| --- | ---: |",
        f"| `C_S_target` | `{fmt_float(result['C_S_target'])}` |",
        f"| `C_S_result` | `{fmt_float(result['C_S_result'])}` |",
        f"| `C_S_slack` | `{fmt_float(result['C_S_slack'])}` |",
        f"| `paid_doubling_multiplier` | `{fmt_float(result['paid_doubling_multiplier'])}` |",
        f"| `paid_doubling_C_S_result` | `{fmt_float(result['paid_doubling_C_S_result'])}` |",
        "",
        "结论：doubling 只能是恒等式级零成本投影，不能是付费复制轮廓。",
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
            f"归一化验收：`{result['normalization_priority']}`。",
            f"无重复扣费验收：`{result['no_double_count_priority']}`。",
            f"doubling 后方向验收：`{result['post_doubling_priority']}`。",
            f"原 trace 投影验收：`{result['projection_priority']}`。",
            f"外部可接受逃逸门：`{result['external_escape']}`。",
            "",
            "判定：对称 doubling 已压到零成本镜像投影；命题尚未自足闭合。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous-json", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--cs8-json", type=Path, default=DEFAULT_CS8)
    parser.add_argument("--capacity-json", type=Path, default=DEFAULT_CAPACITY)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "previous": args.previous_json,
        "cs8": args.cs8_json,
        "capacity": args.capacity_json,
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
