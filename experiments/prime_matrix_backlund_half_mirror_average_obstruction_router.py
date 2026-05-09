#!/usr/bin/env python3
"""Prime Matrix Backlund 半镜像平均身份障碍路由器。

用法示例：
  python3 experiments/prime_matrix_backlund_half_mirror_average_obstruction_router.py

输出：
  docs/monograph/prime-matrix-backlund-half-mirror-average-obstruction-router.json
  docs/monograph/prime-matrix-backlund-half-mirror-average-obstruction-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONO = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = MONO / "prime-matrix-backlund-zero-cost-projection-identity-router.json"
DEFAULT_TRANSPORT = MONO / "prime-matrix-backlund-zeta-xi-branch-jump-transport-router.json"
DEFAULT_CAPACITY = MONO / "prime-matrix-backlund-crossing-trace-capacity-router.json"
DEFAULT_JSON = MONO / "prime-matrix-backlund-half-mirror-average-obstruction-router.json"
DEFAULT_MD = MONO / "prime-matrix-backlund-half-mirror-average-obstruction-router.md"

HALF_AVERAGE_ATOM = "BacklundOriginalTraceHalfMirrorAverageIdentityLedger"
ODD_ZERO_ATOM = "BacklundOriginalTraceOddPartZeroLedger"
ODD_CORRECTION_ATOM = "BacklundOddMirrorCorrectionCostLedger"
EVEN_IDENTITY_ATOM = "BacklundMirrorEvenPartIdentityClosed"
ZERO_AVOIDING_ATOM = "BacklundZeroAvoidingShiftWithoutJumpLedger"
EXTERNAL_ATOM = "ClassicalBacklundZeroIndentationCostExternalAccepted"
ZERO_COST_ATOM = "BacklundZeroCostMirrorProjectionIdentityLedger"
ODD_JUMP_ATOM = "BacklundMirrorOddJumpCancellationIdentityLedger"
EVEN_GAMMA_ATOM = "BacklundEvenGammaElementaryRemainderBudgetLedger"
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


def algebra_rows() -> list[dict[str, str]]:
    """写出半镜像平均的纯代数分解。"""
    return [
        {
            "symbol": "A",
            "meaning": "原始 Backlund trace 的局部 branch-jump 贡献。",
        },
        {
            "symbol": "M",
            "meaning": "xi 镜像 trace 的对应 branch-jump 贡献。",
        },
        {
            "symbol": "E=(A+M)/2",
            "meaning": "镜像偶部，也就是半镜像平均能保留的部分。",
        },
        {
            "symbol": "O=(A-M)/2",
            "meaning": "镜像奇部；若 M=-A，则 O=A，正是原始 crossing 贡献。",
        },
    ]


def route_options() -> list[dict[str, str]]:
    """列出障碍之后的真实路线。"""
    return [
        {
            "route": ODD_ZERO_ATOM,
            "meaning": "证明原始 trace 的奇部为 0；这等价于无 crossing/零避让在本 formal unit 中成立。",
        },
        {
            "route": ODD_CORRECTION_ATOM,
            "meaning": "保留奇部修正并支付其成本；这回到凹口成本/外部 Backlund 引理路线。",
        },
        {
            "route": EXTERNAL_ATOM,
            "meaning": "接受经典 Backlund 零点缩进引理，绕开内部半平均配对路线。",
        },
    ]


def build_rows(previous: dict[str, Any], transport: dict[str, Any], capacity: dict[str, Any]) -> list[dict[str, Any]]:
    """生成半镜像平均障碍判定表。"""
    active = previous.get("next_priority") == HALF_AVERAGE_ATOM
    guard = (
        previous.get("counterexample_assumption_only") is True
        and previous.get("empirical_absence_not_used") is True
        and previous.get("hypothetical_chain_only") is True
    )
    transport_ready = transport.get("zeta_xi_branch_jump_transport_closed") is True
    capacity_ready = capacity.get("trace_capacity_reduction_closed") is True
    algebra_obstruction = True
    return [
        row(
            "HalfMirrorAverageGateActive",
            active,
            True,
            "上一层把零成本投影压到原始 trace 与半镜像平均的身份。",
            HALF_AVERAGE_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只分析假设链条中的解析 trace，不使用真实零行缺席。",
            "保持 row_column_self_contained_closed=false。",
        ),
        row(
            "ZetaXiJumpTransportAvailable",
            transport_ready,
            True,
            "branch-jump 已可在 xi 语言中讨论，镜像奇偶分解合法。",
            "无对象搬运剩余。",
        ),
        row(
            "TraceCapacityRequiresZeroOddCoefficient",
            capacity_ready,
            True,
            "容量收缩已证明任何 Jensen 规模正比例奇部残留都会超出 5/64 余量。",
            ODD_ZERO_ATOM,
        ),
        row(
            "HalfAverageAlgebraObstructionClosed",
            algebra_obstruction,
            True,
            "若镜像跳变反号，半平均消掉的是奇部；但原始 trace 等于偶部加奇部，除非奇部先为 0。",
            ODD_ZERO_ATOM,
        ),
        row(
            "EvenPartIdentityClosed",
            True,
            True,
            "A=(A+M)/2+(A-M)/2 是恒等式；只能闭合偶部定义，不能闭合原始 trace。",
            EVEN_IDENTITY_ATOM,
        ),
        row(
            HALF_AVERAGE_ATOM,
            False,
            False,
            "半镜像平均不能单独替代原始 trace；必须额外证明奇部为 0 或支付奇部修正成本。",
            f"{ODD_ZERO_ATOM} OR {ODD_CORRECTION_ATOM}",
        ),
        row(
            ODD_ZERO_ATOM,
            False,
            False,
            "尚未证明原始 trace 没有 crossing 奇部；这是新的唯一最窄内部目标。",
            ZERO_AVOIDING_ATOM,
        ),
        row(
            ODD_CORRECTION_ATOM,
            False,
            False,
            "若不能证明奇部为 0，就必须恢复成本账本；这不会给出零成本自足闭合。",
            EXTERNAL_ATOM,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行半镜像平均障碍路由。"""
    previous = load_json(paths["previous"])
    transport = load_json(paths["transport"])
    capacity = load_json(paths["capacity"])
    rows = build_rows(previous, transport, capacity)
    obstruction_closed = next(item["closed"] for item in rows if item["gate"] == "HalfAverageAlgebraObstructionClosed")
    source_paths = [path for name, path in paths.items() if name not in {"json_out", "md_out"}]
    return {
        "certificate_type": "prime_matrix_backlund_half_mirror_average_obstruction_router",
        "status": "backlund_half_mirror_average_obstruction_closed_odd_part_zero_next",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "half_average_obstruction_closed": obstruction_closed,
        "half_average_identity_closed": False,
        "zero_cost_projection_identity_closed": False,
        "backlund_local_crossing_trace_closed": False,
        "row_column_self_contained_closed": False,
        "algebra_rows": algebra_rows(),
        "route_options": route_options(),
        "replacement_self_contained": {
            HALF_AVERAGE_ATOM: f"({EVEN_IDENTITY_ATOM} AND ({ODD_ZERO_ATOM} OR {ODD_CORRECTION_ATOM}))"
        },
        "next_priority": ODD_ZERO_ATOM,
        "equivalent_old_priority": ZERO_AVOIDING_ATOM,
        "fallback_priority": ODD_CORRECTION_ATOM,
        "external_escape": EXTERNAL_ATOM,
        "parent_priority": ZERO_COST_ATOM,
        "odd_jump_priority": ODD_JUMP_ATOM,
        "even_gamma_priority": EVEN_GAMMA_ATOM,
        "parallel_priority": DSTRUCTURE,
        "plain_conclusion": (
            "半镜像平均路线存在纯代数障碍：设原始 branch-jump 为 A、镜像为 M。"
            "半平均只给 E=(A+M)/2；原始 trace 是 E+O，其中 O=(A-M)/2。"
            "若镜像抵消条件 M=-A 成立，则 E=0 但 O=A，原始 crossing 成本并没有消失。"
            "因此要想零成本闭合，必须另证 `BacklundOriginalTraceOddPartZeroLedger`；"
            "否则只能保留奇部修正并回到凹口成本/外部 Backlund 引理。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement_self_contained"].items()))
    lines = [
        "# Prime Matrix Backlund 半镜像平均身份障碍路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"half_average_obstruction_closed={fmt_bool(result['half_average_obstruction_closed'])}",
        f"half_average_identity_closed={fmt_bool(result['half_average_identity_closed'])}",
        f"zero_cost_projection_identity_closed={fmt_bool(result['zero_cost_projection_identity_closed'])}",
        f"backlund_local_crossing_trace_closed={fmt_bool(result['backlund_local_crossing_trace_closed'])}",
        f"row_column_self_contained_closed={fmt_bool(result['row_column_self_contained_closed'])}",
        "```",
        "",
        "## 1. 代数分解",
        "",
        "| symbol | meaning |",
        "| --- | --- |",
    ]
    for item in result["algebra_rows"]:
        lines.append(f"| `{table_cell(item['symbol'])}` | {table_cell(item['meaning'])} |")
    lines.extend(
        [
            "",
            "关键判断：若 `M=-A`，半平均 `E=0`，但原始 trace 的奇部 `O=A`，所以原始成本没有被消灭。",
            "",
            "## 2. 自足替换",
            "",
            "```text",
            replacement[0],
            "  =>",
            replacement[1],
            "```",
            "",
            "## 3. 后续路线",
            "",
            "| route | meaning |",
            "| --- | --- |",
        ]
    )
    for item in result["route_options"]:
        lines.append(f"| `{table_cell(item['route'])}` | {table_cell(item['meaning'])} |")
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
            f"当前真正最窄点：`{result['next_priority']}`。",
            f"等价旧目标：`{result['equivalent_old_priority']}`。",
            f"若失败则回到：`{result['fallback_priority']}`。",
            f"外部可接受逃逸门：`{result['external_escape']}`。",
            "",
            "判定：半镜像平均身份不能直接闭合；必须证明原始奇部为 0。",
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
    parser.add_argument("--capacity-json", type=Path, default=DEFAULT_CAPACITY)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "previous": args.previous_json,
        "transport": args.transport_json,
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
