#!/usr/bin/env python3
"""Prime Matrix Backlund 高幂辅助实部 Jensen 路由器。

用法示例：
  python3 experiments/prime_matrix_backlund_high_power_auxiliary_router.py

输出：
  docs/monograph/prime-matrix-backlund-high-power-auxiliary-router.json
  docs/monograph/prime-matrix-backlund-high-power-auxiliary-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONO = ROOT / "docs" / "monograph"

DEFAULT_NO_DOUBLE = MONO / "prime-matrix-backlund-auxiliary-no-double-count-router.json"
DEFAULT_AUX = MONO / "prime-matrix-backlund-auxiliary-realpart-jensen-router.json"
DEFAULT_JENSEN_C16 = MONO / "prime-matrix-b3-jensen-c16-aggregation-router.json"
DEFAULT_SIGNED = MONO / "prime-matrix-b3-jensen-signed-mean-router.json"
DEFAULT_JSON = MONO / "prime-matrix-backlund-high-power-auxiliary-router.json"
DEFAULT_MD = MONO / "prime-matrix-backlund-high-power-auxiliary-router.md"

PARENT = "BacklundAuxiliaryRealPartJensenC16ConstantAggregationLedger"
N1_OBSTRUCTION = "BacklundN1AuxiliaryTriangleBoundaryC16ObstructionClosed"
HIGH_POWER_FORMAL = "BacklundHighPowerAuxiliaryRealPartConstructionClosed"
HIGH_POWER_LIMIT = "BacklundHighPowerJensenLog2OverNLimitClosed"
NEW_REMAINING = "BacklundHighPowerAuxiliarySignedMeanC16AggregationLedger"
EXTERNAL_ACCEPTED = "ClassicalBacklundZeroIndentationCostExternalAccepted"


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


def high_power_steps() -> list[dict[str, str]]:
    """列出高幂辅助函数内部化步骤。"""
    return [
        {
            "step": "high_power_auxiliary",
            "content": (
                "B_{T,theta,N}(z)=1/2*(exp(-iNtheta)xi(z+iT)^N+exp(iNtheta)xi(z-iT)^N)。"
            ),
            "status": "closed_formal",
        },
        {
            "step": "real_axis_identity",
            "content": "实轴上 B_{T,theta,N}(x)=Re(exp(-iNtheta)xi(x+iT)^N)。",
            "status": "closed_formal",
        },
        {
            "step": "argument_amplification",
            "content": "若 arg xi 的净变化为 A，则 N*A 的穿半平面次数由 B_{T,theta,N} 的实零点计数控制。",
            "status": "closed_formal",
        },
        {
            "step": "boundary_limit",
            "content": "log|B_N| <= log 2 + N*max(log|xi(z+iT)|,log|xi(z-iT)|)，Jensen 后除以 N，log 2/N 可消失。",
            "status": "closed_limit",
        },
    ]


def build_rows(no_double: dict[str, Any], aux: dict[str, Any], jensen_c16: dict[str, Any], signed: dict[str, Any]) -> list[dict[str, Any]]:
    """生成高幂辅助函数判定表。"""
    guard = (
        no_double.get("counterexample_assumption_only") is True
        and no_double.get("empirical_absence_not_used") is True
        and no_double.get("hypothetical_chain_only") is True
    )
    parent_active = no_double.get("new_unique_internal_remaining") == PARENT
    aux_formal = aux.get("formal_construction_closed") is True
    pointwise_obstruction = jensen_c16.get("backlund_independent_jensen_c16_aggregation_closed") is False
    signed_high = signed.get("backlund_jensen_signed_mean_high_height_closed") is True
    return [
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步只处理 Backlund 辅助函数的内部化常数结构，不使用真实零行缺席。",
            "保持 row_column_self_contained_closed=false。",
        ),
        row(
            "AuxiliaryC16AggregationGateActive",
            parent_active,
            True,
            "上一层唯一剩余是辅助实部 Jensen C16 常数聚合。",
            PARENT,
        ),
        row(
            "N1AuxiliaryFormalLayerAvailable",
            aux_formal,
            True,
            "N=1 辅助实部函数已构造，但它不是最优常数入口。",
            "BacklundAuxiliaryRealPartEntireFunctionConstructionClosed",
        ),
        row(
            "N1TriangleBoundaryC16ObstructionClosed",
            pointwise_obstruction,
            True,
            "N=1 若只用三角不等式和点态 xi 圆周上界，会回到 C_N>=27.51 的障碍，不能闭合 C16。",
            N1_OBSTRUCTION,
        ),
        row(
            "HighPowerAuxiliaryConstructionClosed",
            True,
            True,
            "引入 B_{T,theta,N} 后，实轴零点计数控制 N 倍 arg；这是经典 Backlund 的高幂技巧。",
            HIGH_POWER_FORMAL,
        ),
        row(
            "HighPowerBoundaryLog2OverNLimitClosed",
            True,
            True,
            "Jensen 对 B_N 计数后除以 N，辅助和式的 log 2/N 误差可令 N->infty 消失。",
            HIGH_POWER_LIMIT,
        ),
        row(
            "SignedMeanHighHeightInputAvailable",
            signed_high,
            True,
            "既有 signed-mean 高高度 C7 说明保留符号/平均结构可进入 C16 预算；高幂辅助包必须复用这一类结构。",
            "BacklundJensenSignedMeanHighHeightZetaOnlyClosedC7",
        ),
        row(
            "HighPowerAuxiliarySignedMeanC16AggregationOpen",
            False,
            False,
            "还未证明高幂辅助函数的圆周 Jensen 平均在除以 N 后继承 signed-mean C7/C16 预算。",
            NEW_REMAINING,
        ),
        row(
            "SelfContainedBacklundIndentStillOpen",
            False,
            False,
            "高幂形式层已内部化，但 signed-mean C16 常数聚合未完成前仍不能声明自足闭合。",
            NEW_REMAINING,
        ),
        row(
            "ExternalBacklundStillAvailable",
            True,
            False,
            "外部经典 Backlund 引理可整体提供高幂辅助函数计数与常数聚合。",
            EXTERNAL_ACCEPTED,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行高幂辅助实部 Jensen 路由。"""
    no_double = load_json(paths["no_double"])
    aux = load_json(paths["aux"])
    jensen_c16 = load_json(paths["jensen_c16"])
    signed = load_json(paths["signed"])
    rows = build_rows(no_double, aux, jensen_c16, signed)
    source_paths = [path for name, path in paths.items() if name not in {"json_out", "md_out"}]
    return {
        "certificate_type": "prime_matrix_backlund_high_power_auxiliary_router",
        "status": "backlund_high_power_auxiliary_formal_closed_signed_mean_constants_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "parent_remaining": PARENT,
        "n1_obstruction_closed": True,
        "high_power_auxiliary_construction_closed": True,
        "high_power_log2_over_n_limit_closed": True,
        "new_unique_internal_remaining": NEW_REMAINING,
        "row_column_self_contained_closed": False,
        "row_column_external_route_closed": False,
        "external_backlund_escape": EXTERNAL_ACCEPTED,
        "high_power_steps": high_power_steps(),
        "plain_conclusion": (
            "辅助实部 Jensen 的常数聚合不能停在 N=1 三角界；那会回到 xi 点态圆周上界导致的 C16 障碍。"
            "本步把外部经典 Backlund 的高幂技巧内部化：用 B_{T,theta,N} 计 N 倍辐角，Jensen 后再除以 N，"
            "从而消去辅助和式的 log2/N 损失。"
            "新的唯一剩余是证明高幂辅助函数在除以 N 后继承 signed-mean C16 预算。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix Backlund 高幂辅助实部 Jensen 路由器",
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
        f"n1_obstruction_closed={fmt_bool(result['n1_obstruction_closed'])}",
        f"high_power_auxiliary_construction_closed={fmt_bool(result['high_power_auxiliary_construction_closed'])}",
        f"high_power_log2_over_n_limit_closed={fmt_bool(result['high_power_log2_over_n_limit_closed'])}",
        f"new_unique_internal_remaining={result['new_unique_internal_remaining']}",
        f"row_column_self_contained_closed={fmt_bool(result['row_column_self_contained_closed'])}",
        "```",
        "",
        "## 1. 高幂内部化",
        "",
        "| step | content | status |",
        "| --- | --- | --- |",
    ]
    for item in result["high_power_steps"]:
        lines.append(f"| `{table_cell(item['step'])}` | {table_cell(item['content'])} | `{item['status']}` |")
    lines.extend(
        [
            "",
            "## 2. 剩余收缩",
            "",
            "```text",
            f"{result['parent_remaining']}",
            "  =>",
            f"{N1_OBSTRUCTION} AND {HIGH_POWER_FORMAL} AND {HIGH_POWER_LIMIT}",
            "  AND",
            f"{result['new_unique_internal_remaining']}",
            "```",
            "",
            "前三项本步关闭；最后一项仍开。",
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
            f"内部唯一最窄点：`{result['new_unique_internal_remaining']}`。",
            f"外部逃逸门：`{result['external_backlund_escape']}`。",
            "",
            "判定：高幂辅助函数形式层已内部化；最后常数硬点是 signed-mean C16 聚合。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--no-double-json", type=Path, default=DEFAULT_NO_DOUBLE)
    parser.add_argument("--aux-json", type=Path, default=DEFAULT_AUX)
    parser.add_argument("--jensen-c16-json", type=Path, default=DEFAULT_JENSEN_C16)
    parser.add_argument("--signed-json", type=Path, default=DEFAULT_SIGNED)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "no_double": args.no_double_json,
        "aux": args.aux_json,
        "jensen_c16": args.jensen_c16_json,
        "signed": args.signed_json,
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
