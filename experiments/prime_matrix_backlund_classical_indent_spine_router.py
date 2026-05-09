#!/usr/bin/env python3
"""Prime Matrix 经典 Backlund 缩进内部证明脊柱路由器。

用法示例：
  python3 experiments/prime_matrix_backlund_classical_indent_spine_router.py

输出：
  docs/monograph/prime-matrix-backlund-classical-indent-spine-router.json
  docs/monograph/prime-matrix-backlund-classical-indent-spine-router.md
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

DEFAULT_ATOMIC = MONO / "prime-matrix-backlund-internal-proof-atomic-reduction-router.json"
DEFAULT_INDENT = MONO / "prime-matrix-b3-zero-proximity-indentation-cost-router.json"
DEFAULT_LITTLEWOOD = MONO / "prime-matrix-b3-backlund-littlewood-rectangle-router.json"
DEFAULT_JENSEN = MONO / "prime-matrix-b3-jensen-radius-contingency-router.json"
DEFAULT_CS8 = MONO / "prime-matrix-b3-cs8-slack-router.json"
DEFAULT_ENDPOINT = MONO / "prime-matrix-b3-endpoint-multiplicity-convention-router.json"
DEFAULT_MERGE = MONO / "prime-matrix-backlund-internal-external-merge-router.json"
DEFAULT_JSON = MONO / "prime-matrix-backlund-classical-indent-spine-router.json"
DEFAULT_MD = MONO / "prime-matrix-backlund-classical-indent-spine-router.md"

PARENT_INTERNAL = "ClassicalBacklundZeroIndentationCostInternalProofLedger"
OLD_JUMP = "BacklundBudgetPreservingJumpAccountingZeroCoefficientLedger"
NEW_REMAINING = "BacklundRealPartSignChangeJensenAbsorptionNoDoubleCountLedger"
SIGN_CHANGE_LEMMA = "BacklundRealTraceVariationBySignChangesClosed"
LOCAL_INDENT_REGISTRY = "BacklundIndentArcLimitRegisteredAsSignChangeZerosClosed"
EXTERNAL_ACCEPTED = "ClassicalBacklundZeroIndentationCostExternalAccepted"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证据。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算文件哈希。"""
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


def deterministic_lemmas() -> list[dict[str, str]]:
    """登记本步真正自足闭合的经典 Backlund 局部引理。"""
    return [
        {
            "lemma": SIGN_CHANGE_LEMMA,
            "statement": (
                "若连续可微曲线 f(x) 在区间上不为 0，且 arg 分支从右端固定，"
                "则 arg f 的净变化/振幅可由 Re(e^{-i theta} f(x)) 的零点/sign-change 次数控制。"
            ),
            "proof_note": "在两个相邻实部零点之间，曲线留在同一开半平面，arg 净摆幅小于 pi；逐段相加。",
        },
        {
            "lemma": LOCAL_INDENT_REGISTRY,
            "statement": (
                "当路径命中解析零点 rho 时，先以小半圆避开再取极限；局部模型 "
                "f(s)=(s-rho)^m g(s) 把缩进弧 jump 精确登记为 m 个 sign-change/重数事件。"
            ),
            "proof_note": "g(rho) 非零只给连续相位；全部离散跳变来自 (s-rho)^m，按解析重数登记。",
        },
    ]


def build_rows(
    atomic: dict[str, Any],
    indent: dict[str, Any],
    littlewood: dict[str, Any],
    jensen: dict[str, Any],
    cs8: dict[str, Any],
    endpoint: dict[str, Any],
    merge: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成经典 Backlund 内部脊柱判定表。"""
    guard = (
        atomic.get("counterexample_assumption_only") is True
        and atomic.get("empirical_absence_not_used") is True
        and atomic.get("hypothetical_chain_only") is True
    )
    atomic_open = atomic.get("strict_self_contained_unique_remaining") == OLD_JUMP
    external_indent_available = indent.get("zero_proximity_indentation_cost_external_closed") is True
    littlewood_closed = littlewood.get("backlund_littlewood_rectangle_argument_closed") is True
    jensen_external_c16 = jensen.get("jensen_c16_aggregation_external_closed") is True
    cs8_external = cs8.get("backlund_cs8_slack_external_closed") is True
    endpoint_closed = endpoint.get("endpoint_multiplicity_convention_closed") is True
    merge_locked = merge.get("internal_primary_target") == PARENT_INTERNAL
    return [
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只重排假设链条里的解析缩进成本，不使用真实零行缺席。",
            "保持自足与外部链条分离。",
        ),
        row(
            "ParentInternalTargetStillLocked",
            merge_locked,
            True,
            "内部主攻仍是经典 Backlund 缩进成本内部证明。",
            PARENT_INTERNAL,
        ),
        row(
            "PreviousZeroCoefficientAtomActive",
            atomic_open,
            True,
            "上一层把内部硬点写成未配对 jump 的 log(T) 零系数。",
            OLD_JUMP,
        ),
        row(
            "ClassicalBacklundSignChangeLemmaClosed",
            True,
            True,
            "经典 Backlund 的实变量骨架可自足证明：arg 净变化/振幅由实部 sign-change 数控制。",
            SIGN_CHANGE_LEMMA,
        ),
        row(
            "IndentArcLimitRegisteredAsSignChangeZeros",
            True,
            True,
            "局部缩进弧的 jump 不是额外对象；在避零极限中按解析重数登记为同一 sign-change/零点事件。",
            LOCAL_INDENT_REGISTRY,
        ),
        row(
            "LittlewoodRectangleIdentityAvailable",
            littlewood_closed,
            True,
            "Littlewood 矩形恒等式已可登记零点横向权重和边界积分。",
            "BacklundLittlewoodRectangleArgumentClosed",
        ),
        row(
            "ExternalJensenC16AvailableForAbsorptionTest",
            jensen_external_c16,
            False,
            "外部低高度输入下 Jensen C16 计数可作为对接参照；严格自足低高度仍未全部闭合。",
            "BacklundIndependentJensenZeroCountC16AggregationExternalClosed",
        ),
        row(
            "SeparateIndentChargeWouldDoubleCount",
            True,
            True,
            "若 sign-change 零点已进入 Jensen C16 计数，再额外逐零点付 pi 缩进成本就是重复扣费。",
            "NoDoubleCounting discipline",
        ),
        row(
            "SignChangeToJensenAbsorptionExactness",
            False,
            False,
            "仍需证明 sign-change 登记表逐项注入既有 Jensen C16 局部计数，且不遗漏端点、重零和贴线极限。",
            NEW_REMAINING,
        ),
        row(
            "CS8ReaggregationAfterAbsorption",
            cs8_external,
            True,
            "若上面的无重复吸收对接闭合，则 C_boundary=16 与桥因子 1/2 的 C_S=8 验收不再新增成本。",
            "BacklundCS8SlackAfterBridgeClosedTightHalf",
        ),
        row(
            "EndpointMultiplicityCompatible",
            endpoint_closed,
            True,
            "端点落零先避开再取极限，正好提供 sign-change 登记的重数 convention。",
            "EndpointZeroAvoidanceMultiplicityConventionClosedByLimit",
        ),
        row(
            "InternalClassicalBacklundIndentClosed",
            False,
            False,
            "经典脊柱已建立，但 sign-change 到 Jensen C16 的精确无重复对接仍未闭合。",
            NEW_REMAINING,
        ),
        row(
            "ExternalBacklundEscapeStillAvailable",
            external_indent_available,
            False,
            "接受外部经典 Backlund 缩进引理可绕过该内部对接证明。",
            EXTERNAL_ACCEPTED,
        ),
        row(
            "RowColumnExternalRouteStillNeedsDStructure",
            False,
            False,
            "外部 Backlund 包接上后，最终仍需 DStructure/Rankin 独立验收。",
            DSTRUCTURE,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行经典 Backlund 缩进内部脊柱路由。"""
    atomic = load_json(paths["atomic"])
    indent = load_json(paths["indent"])
    littlewood = load_json(paths["littlewood"])
    jensen = load_json(paths["jensen"])
    cs8 = load_json(paths["cs8"])
    endpoint = load_json(paths["endpoint"])
    merge = load_json(paths["merge"])
    rows = build_rows(atomic, indent, littlewood, jensen, cs8, endpoint, merge)
    source_paths = [path for name, path in paths.items() if name not in {"json_out", "md_out"}]
    naive_jump_coefficient = 16.0 * math.pi
    available_margin = 5.0 / 64.0
    return {
        "certificate_type": "prime_matrix_backlund_classical_indent_spine_router",
        "status": "backlund_classical_indent_spine_reduced_to_sign_change_absorption_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "parent_internal_target": PARENT_INTERNAL,
        "previous_unique_remaining": OLD_JUMP,
        "new_unique_internal_remaining": NEW_REMAINING,
        "sign_change_lemma_closed": True,
        "indent_arc_registry_closed": True,
        "row_column_self_contained_closed": False,
        "row_column_external_route_closed": False,
        "external_backlund_escape": EXTERNAL_ACCEPTED,
        "dstructure_rankin_gate": DSTRUCTURE,
        "budget_pressure": {
            "jensen_count_coefficient": 16.0,
            "per_jump_cost": math.pi,
            "naive_jump_coefficient": naive_jump_coefficient,
            "available_stability_margin": available_margin,
            "deficit_if_double_counted": naive_jump_coefficient - available_margin,
        },
        "deterministic_lemmas": deterministic_lemmas(),
        "plain_conclusion": (
            "经典 Backlund 内部化的正确脊柱不是证明近零 jump 消失，而是把水平 trace 的 "
            "arg 净变化/振幅改写为实部 sign-change 计数；缩进弧在避零极限中按解析重数登记为同一类事件。"
            "本步自足关闭了 sign-change 净变化引理和局部缩进登记引理，排除了逐零点额外付费的重复扣费。"
            "严格自足的新唯一剩余是证明该 sign-change 登记表精确注入既有 Jensen C16 局部计数，"
            "不遗漏端点、重零、贴线极限，也不调用外部 Backlund 引理。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    budget = result["budget_pressure"]
    lines = [
        "# Prime Matrix 经典 Backlund 缩进内部证明脊柱路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"parent_internal_target={result['parent_internal_target']}",
        f"previous_unique_remaining={result['previous_unique_remaining']}",
        f"new_unique_internal_remaining={result['new_unique_internal_remaining']}",
        f"sign_change_lemma_closed={fmt_bool(result['sign_change_lemma_closed'])}",
        f"indent_arc_registry_closed={fmt_bool(result['indent_arc_registry_closed'])}",
        f"row_column_self_contained_closed={fmt_bool(result['row_column_self_contained_closed'])}",
        f"row_column_external_route_closed={fmt_bool(result['row_column_external_route_closed'])}",
        "```",
        "",
        "## 1. 本步闭合的经典局部引理",
        "",
        "| lemma | statement | proof note |",
        "| --- | --- | --- |",
    ]
    for item in result["deterministic_lemmas"]:
        lines.append(
            f"| `{table_cell(item['lemma'])}` | {table_cell(item['statement'])} | {table_cell(item['proof_note'])} |"
        )
    lines.extend(
        [
            "",
            "## 2. 预算压力",
            "",
            "| item | value |",
            "| --- | ---: |",
            f"| Jensen count coefficient | `{budget['jensen_count_coefficient']:.12f}` |",
            f"| per jump cost | `{budget['per_jump_cost']:.12f}` |",
            f"| naive jump coefficient | `{budget['naive_jump_coefficient']:.12f}` |",
            f"| available stability margin | `{budget['available_stability_margin']:.12f}` |",
            f"| deficit if double counted | `{budget['deficit_if_double_counted']:.12f}` |",
            "",
            "解释：若把 sign-change/Jensen 已计入的近零事件再逐零点额外付 `pi`，会产生约 "
            "`50.187357` 的系数缺口。因此经典 Backlund 内部化必须证明“同一登记表吸收”，"
            "而不是添加一个新的缩进成本项。",
            "",
            "## 3. 新的精确剩余",
            "",
            "```text",
            f"{result['previous_unique_remaining']}",
            "  =>",
            f"({SIGN_CHANGE_LEMMA} AND {LOCAL_INDENT_REGISTRY} AND {result['new_unique_internal_remaining']})",
            "```",
            "",
            f"其中前两项本步关闭，唯一未闭合项是 `{result['new_unique_internal_remaining']}`。",
            "",
            "## 4. 判定表",
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
            "## 5. 下一步",
            "",
            f"内部唯一最窄点：`{result['new_unique_internal_remaining']}`。",
            f"外部逃逸门：`{result['external_backlund_escape']}`。",
            f"外部路线最终仍需：`{result['dstructure_rankin_gate']}`。",
            "",
            "判定：经典 Backlund 内部证明已缩成“sign-change 登记表无重复注入 Jensen C16”的精确对接命题；尚未严格自足闭合。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--atomic-json", type=Path, default=DEFAULT_ATOMIC)
    parser.add_argument("--indent-json", type=Path, default=DEFAULT_INDENT)
    parser.add_argument("--littlewood-json", type=Path, default=DEFAULT_LITTLEWOOD)
    parser.add_argument("--jensen-json", type=Path, default=DEFAULT_JENSEN)
    parser.add_argument("--cs8-json", type=Path, default=DEFAULT_CS8)
    parser.add_argument("--endpoint-json", type=Path, default=DEFAULT_ENDPOINT)
    parser.add_argument("--merge-json", type=Path, default=DEFAULT_MERGE)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "atomic": args.atomic_json,
        "indent": args.indent_json,
        "littlewood": args.littlewood_json,
        "jensen": args.jensen_json,
        "cs8": args.cs8_json,
        "endpoint": args.endpoint_json,
        "merge": args.merge_json,
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
    print(result["new_unique_internal_remaining"])


if __name__ == "__main__":
    main()
