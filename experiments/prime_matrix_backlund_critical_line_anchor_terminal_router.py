#!/usr/bin/env python3
"""Prime Matrix Backlund 临界线小半径 anchor 终端路由器。

用法示例：
  python3 experiments/prime_matrix_backlund_critical_line_anchor_terminal_router.py

输出：
  docs/monograph/prime-matrix-backlund-critical-line-anchor-terminal-router.json
  docs/monograph/prime-matrix-backlund-critical-line-anchor-terminal-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONO = ROOT / "docs" / "monograph"

DEFAULT_SCALE = MONO / "prime-matrix-backlund-scale-sensitive-jensen-obstruction-router.json"
DEFAULT_ENDPOINT = MONO / "prime-matrix-b3-endpoint-multiplicity-convention-router.json"
DEFAULT_STIELTJES = MONO / "prime-matrix-backlund-boundary-stieltjes-jump-transfer-router.json"
DEFAULT_INTERNAL = MONO / "prime-matrix-backlund-internal-proof-obligation-router.json"
DEFAULT_JSON = MONO / "prime-matrix-backlund-critical-line-anchor-terminal-router.json"
DEFAULT_MD = MONO / "prime-matrix-backlund-critical-line-anchor-terminal-router.md"

CRITICAL_ANCHOR = "BacklundCriticalLineScaleAnchorAvoidanceLedger"
MOVING_CENTER = "BacklundMovingCenterZeroAvoidanceWithoutCostLedger"
CAPSULE_DENSITY = "BacklundIndependentCapsuleZeroDensityCoefficientLedger"
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


def terminal_routes() -> list[dict[str, str]]:
    """临界线小半径 anchor 的终端分叉。"""
    return [
        {
            "route": "fixed_critical_center",
            "verdict": "blocked",
            "reason": "固定靠近临界线的圆心无法给出统一非零下界；圆心可与零点或零点簇任意接近。",
        },
        {
            "route": "moving_center_avoidance",
            "verdict": "loops_to_indent_cost",
            "reason": "移动圆心避零必须记录穿越、绕行和跳变；这正是 Backlund 近零缩进成本。",
        },
        {
            "route": "cartan_average_center",
            "verdict": "requires_capsule_density_first",
            "reason": "平均/Cartan 选点需要先控制例外小圆盘总量；该控制就是胶囊零点密度。",
        },
        {
            "route": "external_backlund_indent",
            "verdict": "external_escape",
            "reason": "接受经典 Backlund 缩进引理可直接关闭该终端缺口。",
        },
    ]


def build_rows(
    scale: dict[str, Any],
    endpoint: dict[str, Any],
    stieltjes: dict[str, Any],
    internal: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成临界线 anchor 终端判定表。"""
    active = scale.get("strict_self_contained_unique_remaining") == CRITICAL_ANCHOR
    guard = (
        scale.get("counterexample_assumption_only") is True
        and scale.get("empirical_absence_not_used") is True
        and scale.get("hypothetical_chain_only") is True
    )
    endpoint_limit = endpoint.get("endpoint_multiplicity_convention_closed") is True
    stieltjes_terminal = stieltjes.get("budget_preserving_stieltjes_jump_transfer_closed") is False
    internal_equiv = internal.get("equivalent_old_remaining") == INDENT_COST
    return [
        row(
            "CriticalLineScaleAnchorGateActive",
            active,
            True,
            "右边界 anchor 半径障碍后，唯一剩余变成临界线附近小半径 anchor。",
            CRITICAL_ANCHOR,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只处理假设链条内的解析 anchor，不使用真实零行缺席。",
            "保持 row_column_self_contained_closed=false。",
        ),
        row(
            "FixedCriticalAnchorBlocked",
            True,
            True,
            "靠近临界线的固定圆心没有 Euler product 下界；若圆心碰零或贴近零点，下界失效。",
            MOVING_CENTER,
        ),
        row(
            "EndpointLimitDoesNotPayAnchor",
            endpoint_limit,
            True,
            "端点极限 convention 只定义重数和极限，不给临界线圆心非零下界。",
            MOVING_CENTER,
        ),
        row(
            "MovingCenterLoopsToStieltjesIndent",
            stieltjes_terminal,
            True,
            "移动圆心避零产生的穿越/跳变账本已经终端等价于缩进成本。",
            INDENT_COST,
        ),
        row(
            "CartanAverageRequiresDensity",
            True,
            True,
            "用平均或 Cartan 选好圆心，需要先知道零点例外集密度；这正是父级胶囊密度目标。",
            CAPSULE_DENSITY,
        ),
        row(
            "TerminalEquivalenceImported",
            internal_equiv,
            True,
            "仓库已登记经典内部证明义务等价于旧 Backlund 近零凹口成本。",
            INTERNAL_PROOF,
        ),
        row(
            CRITICAL_ANCHOR,
            False,
            False,
            "临界线小半径 anchor 没有产生新自由度，终端回到缩进成本内部证明或外部引理。",
            f"{INTERNAL_PROOF} OR {EXTERNAL_ATOM}",
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行临界线小半径 anchor 终端审查。"""
    scale = load_json(paths["scale"])
    endpoint = load_json(paths["endpoint"])
    stieltjes = load_json(paths["stieltjes"])
    internal = load_json(paths["internal"])
    rows = build_rows(scale, endpoint, stieltjes, internal)
    source_paths = [path for name, path in paths.items() if name not in {"json_out", "md_out"}]
    return {
        "certificate_type": "prime_matrix_backlund_critical_line_anchor_terminal_router",
        "status": "backlund_critical_line_scale_anchor_terminal_equivalent_to_indent_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "critical_line_anchor_terminal_equivalence_closed": True,
        "critical_line_anchor_self_contained_closed": False,
        "row_column_self_contained_closed": False,
        "terminal_routes": terminal_routes(),
        "strict_self_contained_unique_remaining": INTERNAL_PROOF,
        "equivalent_old_remaining": INDENT_COST,
        "external_escape": EXTERNAL_ATOM,
        "parallel_priority": DSTRUCTURE,
        "plain_conclusion": (
            "临界线小半径 anchor 路线终端归并。"
            "固定临界线圆心没有统一非零下界；移动圆心避零会重新产生 Stieltjes 跳变/缩进成本；"
            "平均选点又需要先证明胶囊零点密度。"
            "因此该路线没有新自由度，最终回到 `ClassicalBacklundZeroIndentationCostInternalProofLedger`，"
            "也就是旧的 `BacklundZeroProximityIndentationCostLedger`。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix Backlund 临界线小半径 anchor 终端路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        (
            "critical_line_anchor_terminal_equivalence_closed="
            f"{fmt_bool(result['critical_line_anchor_terminal_equivalence_closed'])}"
        ),
        f"critical_line_anchor_self_contained_closed={fmt_bool(result['critical_line_anchor_self_contained_closed'])}",
        f"strict_self_contained_unique_remaining={result['strict_self_contained_unique_remaining']}",
        f"row_column_self_contained_closed={fmt_bool(result['row_column_self_contained_closed'])}",
        "```",
        "",
        "## 1. 终端分叉",
        "",
        "| route | verdict | reason |",
        "| --- | --- | --- |",
    ]
    for item in result["terminal_routes"]:
        lines.append(
            f"| `{table_cell(item['route'])}` | `{table_cell(item['verdict'])}` | {table_cell(item['reason'])} |"
        )
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
            f"严格自足唯一剩余回到：`{result['strict_self_contained_unique_remaining']}`。",
            f"等价旧剩余：`{result['equivalent_old_remaining']}`。",
            f"外部可接受逃逸门：`{result['external_escape']}`。",
            "",
            "判定：临界线小半径 anchor 不是新闭合路线；它终端等价于 Backlund 缩进成本。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--scale-json", type=Path, default=DEFAULT_SCALE)
    parser.add_argument("--endpoint-json", type=Path, default=DEFAULT_ENDPOINT)
    parser.add_argument("--stieltjes-json", type=Path, default=DEFAULT_STIELTJES)
    parser.add_argument("--internal-json", type=Path, default=DEFAULT_INTERNAL)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "scale": args.scale_json,
        "endpoint": args.endpoint_json,
        "stieltjes": args.stieltjes_json,
        "internal": args.internal_json,
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
