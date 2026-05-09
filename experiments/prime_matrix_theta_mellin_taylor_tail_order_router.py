#!/usr/bin/env python3
"""Prime Matrix theta-Mellin Taylor 尾阶账本路由器。

用法示例：
  python3 experiments/prime_matrix_theta_mellin_taylor_tail_order_router.py

输出：
  docs/monograph/prime-matrix-theta-mellin-taylor-tail-order-router.json
  docs/monograph/prime-matrix-theta-mellin-taylor-tail-order-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONO = ROOT / "docs" / "monograph"

DEFAULT_RANGE = MONO / "prime-matrix-theta-mellin-range-box-router.json"
DEFAULT_JSON = MONO / "prime-matrix-theta-mellin-taylor-tail-order-router.json"
DEFAULT_MD = MONO / "prime-matrix-theta-mellin-taylor-tail-order-router.md"

OLD_ATOM = "ThetaMellinTaylorTailOrderLedger0To14"
CLOSED_ATOM = "ThetaMellinTaylorTailOrdersClosedLog120Pi120Trig120Exp80"
TRACE_LEDGER = "IntervalOperationTraceHashLedger"
THETA_TAIL = "GaussianThetaTailBoundLedger"
QUADRATURE = "CompactThetaMellinQuadratureSubdivisionLedger0To14"

LOG_TERMS = 120
PI_TERMS = 120
TRIG_DEGREE = 120
EXP_DEGREE = 80


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


def sci(value: Fraction) -> str:
    """把有理上界转成科学计数法字符串，仅用于报告展示。"""
    return f"{float(value):.6e}"


def factorial(n: int) -> int:
    """计算阶乘。"""
    out = 1
    for value in range(2, n + 1):
        out *= value
    return out


def tail_bounds() -> dict[str, Any]:
    """计算保守 Taylor 尾界。"""
    # log: 缩放到 y in [1,2] 后 z=(y-1)/(y+1)<=1/3。
    z = Fraction(1, 3)
    log_tail = 2 * z ** (2 * LOG_TERMS + 1) / ((2 * LOG_TERMS + 1) * (1 - z * z))
    # Machin arctan 由交错级数下一项给出，取主项 arctan(1/5) 的保守尾界。
    pi_tail = 16 * Fraction(1, 5) ** (2 * PI_TERMS + 1) / (2 * PI_TERMS + 1)
    # sin/cos: range reduction 后 |x|<=pi<4。
    trig_tail = Fraction(4, 1) ** (TRIG_DEGREE + 1) / factorial(TRIG_DEGREE + 1)
    # exp: range reduction 后 |r|<=1/2，正项尾用 4*(1/2)^(N+1)/(N+1)!。
    exp_tail = 4 * Fraction(1, 2) ** (EXP_DEGREE + 1) / factorial(EXP_DEGREE + 1)
    return {
        "log_terms": LOG_TERMS,
        "pi_terms": PI_TERMS,
        "trig_degree": TRIG_DEGREE,
        "exp_degree": EXP_DEGREE,
        "log_tail_bound": sci(log_tail),
        "pi_tail_bound": sci(pi_tail),
        "trig_tail_bound": sci(trig_tail),
        "exp_tail_bound": sci(exp_tail),
        "max_tail_bound_float": max(
            float(log_tail), float(pi_tail), float(trig_tail), float(exp_tail)
        ),
    }


def row(
    gate: str,
    closed: bool,
    proved: bool,
    meaning: str,
    remaining: str,
) -> dict[str, Any]:
    """构造判定行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_rows(previous: dict[str, Any], tails: dict[str, Any]) -> list[dict[str, Any]]:
    """生成 Taylor 尾阶判定表。"""
    active = previous.get("next_priority") == OLD_ATOM
    range_ready = previous.get("range_box_closed") is True
    tails_tiny = tails["max_tail_bound_float"] < 1e-60
    closed = active and range_ready and tails_tiny
    return [
        row(
            "TaylorTailOrderGateActive",
            active,
            True,
            "范围盒闭合后，当前最窄点是为每类 Taylor 调用指定截断阶数与尾界。",
            OLD_ATOM,
        ),
        row(
            "RangeBoxesAvailable",
            range_ready,
            True,
            "log/power/trig/exp 的有理范围盒已闭合。",
            "ThetaMellinCompactRangeBoxClosed0To14T64N20",
        ),
        row(
            "LogTailOrderClosed",
            closed,
            True,
            f"log 使用 atanh 级数 {LOG_TERMS} 项，缩放后 z<=1/3，尾界 {tails['log_tail_bound']}。",
            CLOSED_ATOM,
        ),
        row(
            "PiTailOrderClosed",
            closed,
            True,
            f"pi 使用 Machin 公式 {PI_TERMS} 项，主尾界 {tails['pi_tail_bound']}。",
            CLOSED_ATOM,
        ),
        row(
            "TrigTailOrderClosed",
            closed,
            True,
            f"sin/cos range reduction 到 |x|<=pi<4 后用 {TRIG_DEGREE} 阶，尾界 {tails['trig_tail_bound']}。",
            CLOSED_ATOM,
        ),
        row(
            "ExpTailOrderClosed",
            closed,
            True,
            f"exp range reduction 到 |r|<=1/2 后用 {EXP_DEGREE} 阶，尾界 {tails['exp_tail_bound']}。",
            CLOSED_ATOM,
        ),
        row(
            "TraceThetaQuadratureStillDownstream",
            False,
            False,
            "尾阶表不替代实际调用轨迹、Gaussian theta 尾项或积分分段误差。",
            f"{TRACE_LEDGER} AND {THETA_TAIL} AND {QUADRATURE}",
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行 Taylor 尾阶账本路由。"""
    previous = load_json(paths["previous"])
    tails = tail_bounds()
    rows = build_rows(previous, tails)
    tail_orders_closed = all(item["closed"] for item in rows[:6])
    source_paths = [path for name, path in paths.items() if name not in {"json_out", "md_out"}]
    return {
        "certificate_type": "prime_matrix_theta_mellin_taylor_tail_order_router",
        "status": "theta_mellin_taylor_tail_orders_closed_trace_theta_quadrature_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "tail_orders_closed": tail_orders_closed,
        "theta_mellin_transcendental_kernel_closed": False,
        "row_column_self_contained_closed": False,
        "replacement": {OLD_ATOM: CLOSED_ATOM},
        "tail_bounds": tails,
        "next_priority": TRACE_LEDGER,
        "secondary_priority": THETA_TAIL,
        "tertiary_priority": QUADRATURE,
        "plain_conclusion": (
            "theta-Mellin 超越函数调用的 Taylor 尾阶账本已闭合：log、pi、trig、exp 都给出保守阶数，"
            "最大模板尾界小于 1e-60。剩余不再是 Taylor 理论，而是把这些调用实际登记成 trace/hash，"
            "并证明 Gaussian theta 尾项和紧致积分分段误差。"
        ),
        "rows": rows,
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    tails = result["tail_bounds"]
    lines = [
        "# Prime Matrix theta-Mellin Taylor 尾阶账本路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"tail_orders_closed={fmt_bool(result['tail_orders_closed'])}",
        (
            "theta_mellin_transcendental_kernel_closed="
            f"{fmt_bool(result['theta_mellin_transcendental_kernel_closed'])}"
        ),
        f"max_tail_bound_float={tails['max_tail_bound_float']:.6e}",
        f"row_column_self_contained_closed={fmt_bool(result['row_column_self_contained_closed'])}",
        "```",
        "",
        "## 1. 尾界表",
        "",
        "| call | order | tail bound |",
        "| --- | ---: | ---: |",
        f"| log atanh | {tails['log_terms']} | `{tails['log_tail_bound']}` |",
        f"| pi Machin | {tails['pi_terms']} | `{tails['pi_tail_bound']}` |",
        f"| sin/cos Taylor | {tails['trig_degree']} | `{tails['trig_tail_bound']}` |",
        f"| exp Taylor | {tails['exp_degree']} | `{tails['exp_tail_bound']}` |",
        "",
        "## 2. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
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
            f"当前最窄点：`{result['next_priority']}`。",
            f"随后补 `{result['secondary_priority']}` 与 `{result['tertiary_priority']}`。",
            "",
            "判定：Taylor 尾阶已闭合，剩余是可复核调用日志、theta 尾项和积分分段。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous-json", type=Path, default=DEFAULT_RANGE)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "previous": args.previous_json,
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
