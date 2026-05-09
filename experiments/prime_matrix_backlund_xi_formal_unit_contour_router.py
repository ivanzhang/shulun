#!/usr/bin/env python3
"""Prime Matrix Backlund xi 对称 formal unit 轮廓路由器。

用法示例：
  python3 experiments/prime_matrix_backlund_xi_formal_unit_contour_router.py

输出：
  docs/monograph/prime-matrix-backlund-xi-formal-unit-contour-router.json
  docs/monograph/prime-matrix-backlund-xi-formal-unit-contour-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONO = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = MONO / "prime-matrix-backlund-zeta-xi-branch-jump-transport-router.json"
DEFAULT_LITTLEWOOD = MONO / "prime-matrix-b3-backlund-littlewood-rectangle-router.json"
DEFAULT_LEFT = MONO / "prime-matrix-b3-functional-equation-left-edge-router.json"
DEFAULT_WINDING = MONO / "prime-matrix-xi-boundary-polygon-winding-router.json"
DEFAULT_JSON = MONO / "prime-matrix-backlund-xi-formal-unit-contour-router.json"
DEFAULT_MD = MONO / "prime-matrix-backlund-xi-formal-unit-contour-router.md"

FORMAL_UNIT_ATOM = "BacklundXiSymmetricFormalUnitContourLedger"
DOUBLING_ATOM = "BacklundBudgetPreservingXiSymmetricContourDoublingLedger"
ORIENTATION_ATOM = "BacklundMirrorIndentArcOrientationLedger"
PROJECTION_ATOM = "BacklundOriginalTraceProjectionNoLossLedger"
MIRROR_HASH_ATOM = "BacklundMirrorOrbitMultiplicityHashLedger"
PAIRING_ATOM = "BacklundSignedCrossingPairingInvolutionLedger"
RESIDUAL_ATOM = "BacklundResidualIndentCoefficientZeroLedger"
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


def lower_atoms() -> list[dict[str, str]]:
    """formal unit 轮廓的下层原子。"""
    return [
        {
            "atom": DOUBLING_ATOM,
            "role": "把原始 Backlund 移动凹口 trace 与 xi 镜像 trace 合成同一 formal unit，且不改变目标预算。",
        },
        {
            "atom": ORIENTATION_ATOM,
            "role": "证明镜像凹口弧的方向与 branch_jump 符号正好相反。",
        },
        {
            "atom": PROJECTION_ATOM,
            "role": "从对称 doubled unit 投影回原始 Backlund trace 时不丢失、不重复计算成本。",
        },
    ]


def build_rows(
    previous: dict[str, Any],
    littlewood: dict[str, Any],
    left: dict[str, Any],
    winding: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 formal unit 轮廓判定表。"""
    active = previous.get("next_priority") == FORMAL_UNIT_ATOM
    guard = (
        previous.get("counterexample_assumption_only") is True
        and previous.get("empirical_absence_not_used") is True
        and previous.get("hypothetical_chain_only") is True
    )
    littlewood_ready = littlewood.get("backlund_littlewood_rectangle_argument_closed") is True
    left_ready = left.get("functional_equation_left_edge_closed") is True
    lowheight_model = winding.get("polygon_winding_zero_closed") is True
    existing_formal_inputs = littlewood_ready and left_ready and lowheight_model
    reduction_closed = active and guard and existing_formal_inputs
    return [
        row(
            "XiFormalUnitGateActive",
            active,
            True,
            "zeta-xi 跳变搬运闭合后，剩余是把移动凹口注册成 xi 对称 formal unit。",
            FORMAL_UNIT_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只处理假设链条中的 contour/homotopy 账本，不使用真实零行缺席。",
            "保持 row_column_self_contained_closed=false。",
        ),
        row(
            "BacklundRectangleIdentityAvailable",
            littlewood_ready,
            True,
            "Littlewood 矩形恒等式已闭合，说明原始 Backlund trace 可以按边界和零点权重精确记账。",
            "无矩形恒等式剩余。",
        ),
        row(
            "LeftRightFunctionalEquationBridgeAvailable",
            left_ready,
            True,
            "左边界可经函数方程回到右边界，这提供 formal unit 对称化的解析桥。",
            "无左边界函数方程剩余。",
        ),
        row(
            "LowHeightXiSymmetricUnitModelAvailable",
            lowheight_model,
            True,
            "低高度 xi 多边形给出成功的对称 formal unit 模型，但不自动覆盖移动凹口。",
            "只能作为模型输入。",
        ),
        row(
            "MovingIndentDirectSymmetryNotRegistered",
            True,
            True,
            "现有账本尚未证明原始移动凹口和其 xi 镜像属于同一预算单位。",
            DOUBLING_ATOM,
        ),
        row(
            "FormalUnitReducedToBudgetPreservingDoubling",
            reduction_closed,
            False,
            "formal unit 硬点已压成预算保持的 xi 对称 doubling、镜像弧方向、原 trace 投影三包。",
            f"{DOUBLING_ATOM} AND {ORIENTATION_ATOM} AND {PROJECTION_ATOM}",
        ),
        row(
            DOUBLING_ATOM,
            False,
            False,
            "尚未构造预算保持的 doubled contour/homotopy 账本。",
            DOUBLING_ATOM,
        ),
        row(
            ORIENTATION_ATOM,
            False,
            False,
            "尚未证明镜像凹口弧方向使 branch_jump 成反号配对。",
            ORIENTATION_ATOM,
        ),
        row(
            PROJECTION_ATOM,
            False,
            False,
            "尚未证明 doubled formal unit 回投到原始 trace 时不重复、不漏记。",
            PROJECTION_ATOM,
        ),
        row(
            FORMAL_UNIT_ATOM,
            False,
            False,
            "三包闭合后才可把 xi 对称 formal unit 交给 mirror orbit hash 与 signed pairing。",
            f"{MIRROR_HASH_ATOM} AND {PAIRING_ATOM}",
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行 xi formal unit 轮廓路由。"""
    previous = load_json(paths["previous"])
    littlewood = load_json(paths["littlewood"])
    left = load_json(paths["left"])
    winding = load_json(paths["winding"])
    rows = build_rows(previous, littlewood, left, winding)
    reduction_closed = next(
        item["closed"] for item in rows if item["gate"] == "FormalUnitReducedToBudgetPreservingDoubling"
    )
    source_paths = [path for name, path in paths.items() if name not in {"json_out", "md_out"}]
    return {
        "certificate_type": "prime_matrix_backlund_xi_formal_unit_contour_router",
        "status": "backlund_xi_formal_unit_reduced_to_budget_preserving_doubling_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "formal_unit_reduction_closed": reduction_closed,
        "xi_symmetric_formal_unit_closed": False,
        "signed_pairing_involution_closed": False,
        "backlund_local_crossing_trace_closed": False,
        "row_column_self_contained_closed": False,
        "lower_atoms": lower_atoms(),
        "replacement_self_contained": {
            FORMAL_UNIT_ATOM: f"({DOUBLING_ATOM} AND {ORIENTATION_ATOM} AND {PROJECTION_ATOM})"
        },
        "next_priority": DOUBLING_ATOM,
        "orientation_priority": ORIENTATION_ATOM,
        "projection_priority": PROJECTION_ATOM,
        "support_priority": MIRROR_HASH_ATOM,
        "parent_priority": PAIRING_ATOM,
        "post_pairing_priority": RESIDUAL_ATOM,
        "external_escape": EXTERNAL_ATOM,
        "parallel_priority": DSTRUCTURE,
        "plain_conclusion": (
            "`BacklundXiSymmetricFormalUnitContourLedger` 不能直接由低高度 xi winding 证书推出。"
            "本步把它收缩为一个更窄的预算保持 doubling 问题："
            "必须把原始 Backlund 移动凹口 trace 和 xi 镜像 trace 放入同一 formal unit，"
            "并证明镜像弧反向、回投无损且无重复计费。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement_self_contained"].items()))
    lines = [
        "# Prime Matrix Backlund xi 对称 formal unit 轮廓路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"formal_unit_reduction_closed={fmt_bool(result['formal_unit_reduction_closed'])}",
        f"xi_symmetric_formal_unit_closed={fmt_bool(result['xi_symmetric_formal_unit_closed'])}",
        f"signed_pairing_involution_closed={fmt_bool(result['signed_pairing_involution_closed'])}",
        f"backlund_local_crossing_trace_closed={fmt_bool(result['backlund_local_crossing_trace_closed'])}",
        f"row_column_self_contained_closed={fmt_bool(result['row_column_self_contained_closed'])}",
        "```",
        "",
        "## 1. 自足替换",
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
            "## 2. 判定表",
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
            "## 3. 下一步",
            "",
            f"当前真正最窄点：`{result['next_priority']}`。",
            f"方向验收：`{result['orientation_priority']}`。",
            f"投影验收：`{result['projection_priority']}`。",
            f"mirror hash 支撑：`{result['support_priority']}`。",
            f"父级配对账本：`{result['parent_priority']}`。",
            f"外部可接受逃逸门：`{result['external_escape']}`。",
            "",
            "判定：formal unit 已压到预算保持对称 doubling；命题尚未自足闭合。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous-json", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--littlewood-json", type=Path, default=DEFAULT_LITTLEWOOD)
    parser.add_argument("--left-json", type=Path, default=DEFAULT_LEFT)
    parser.add_argument("--winding-json", type=Path, default=DEFAULT_WINDING)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "previous": args.previous_json,
        "littlewood": args.littlewood_json,
        "left": args.left_json,
        "winding": args.winding_json,
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
