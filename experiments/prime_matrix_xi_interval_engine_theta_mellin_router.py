#!/usr/bin/env python3
"""Prime Matrix xi 区间求值引擎 theta-Mellin 路由器。

用法示例：
  python3 experiments/prime_matrix_xi_interval_engine_theta_mellin_router.py

输出：
  docs/monograph/prime-matrix-xi-interval-engine-theta-mellin-router.json
  docs/monograph/prime-matrix-xi-interval-engine-theta-mellin-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONO = ROOT / "docs" / "monograph"

DEFAULT_RECTANGLE = MONO / "prime-matrix-lowheight-rectangle-count-compression-router.json"
DEFAULT_THETA = MONO / "prime-matrix-b3-theta-mellin-functional-equation-router.json"
DEFAULT_XI = MONO / "prime-matrix-b3-xi-entire-order-router.json"
DEFAULT_JSON = MONO / "prime-matrix-xi-interval-engine-theta-mellin-router.json"
DEFAULT_MD = MONO / "prime-matrix-xi-interval-engine-theta-mellin-router.md"

OLD_ENGINE = "SelfContainedXiIntervalEvaluationEngine0To14"
THETA_ENGINE = "ThetaMellinXiCompactIntervalEngine0To14"
BALL_KERNEL = "CertifiedComplexBallArithmeticKernel"
THETA_TAIL = "GaussianThetaTailBoundLedger"
QUADRATURE = "CompactThetaMellinQuadratureSubdivisionLedger0To14"
BOUNDARY_NONZERO = "XiBoundaryIntervalNonzeroCertificate0To14"
WINDING_ZERO = "XiBoundaryWindingNumberZeroIntervalCertificate0To14"


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
    """构造判定行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def engine_replacement() -> str:
    """写出区间引擎替换包。"""
    return f"{OLD_ENGINE} => ({THETA_ENGINE} AND {BALL_KERNEL} AND {THETA_TAIL} AND {QUADRATURE})"


def build_rows(
    rectangle: dict[str, Any],
    theta: dict[str, Any],
    xi: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 theta-Mellin xi 区间引擎判定表。"""
    rectangle_needs_engine = rectangle.get("next_engine_priority") == OLD_ENGINE
    theta_closed = theta.get("theta_mellin_zeta_functional_equation_closed") is True
    xi_closed = xi.get("xi_entire_order_one_growth_closed") is True
    route_available = rectangle_needs_engine and theta_closed and xi_closed

    return [
        row(
            "RectangleCountNeedsXiEngine",
            rectangle_needs_engine,
            True,
            "矩形计数单原子当前首要缺口是 xi 区间求值引擎。",
            OLD_ENGINE,
        ),
        row(
            "ThetaMellinAndXiInputsAvailable",
            theta_closed and xi_closed,
            True,
            "theta-Mellin 延拓、函数方程、xi 整函数性和增长层均已在仓库内闭合。",
            "可用 theta-Mellin 紧致积分构造 xi 区间引擎。",
        ),
        row(
            "RiemannSiegelEngineNotPrimary",
            route_available,
            True,
            "低高度 0<=t<=14 是紧致小盒；用 theta-Mellin 对称积分比从零实现 Riemann-Siegel 更贴合已有自足材料。",
            THETA_ENGINE,
        ),
        row(
            "CertifiedBallArithmeticKernelMissing",
            False,
            False,
            "仍需复球区间加减乘除、exp/log/Gamma 或 theta 项指数的向外舍入实现与审计。",
            BALL_KERNEL,
        ),
        row(
            "GaussianThetaTailBoundMissing",
            False,
            False,
            "theta 尾项需要显式高斯尾界，保证截断到有限 n 与有限积分段后仍有严格外包。",
            THETA_TAIL,
        ),
        row(
            "CompactQuadratureSubdivisionMissing",
            False,
            False,
            "边界曲线上的 xi 值需要有限分段积分/求和证书，并给每段误差半径。",
            QUADRATURE,
        ),
        row(
            "BoundaryAndWindingStillDownstream",
            False,
            False,
            "引擎完成后才可证明边界非零和 winding=0。",
            f"{BOUNDARY_NONZERO} AND {WINDING_ZERO}",
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行 xi 区间引擎 theta-Mellin 路由。"""
    rectangle = load_json(paths["rectangle"])
    theta = load_json(paths["theta"])
    xi = load_json(paths["xi"])
    rows = build_rows(rectangle, theta, xi)
    route_selected = rows[2]["closed"]
    source_paths = [path for name, path in paths.items() if name not in {"json_out", "md_out"}]
    return {
        "certificate_type": "prime_matrix_xi_interval_engine_theta_mellin_router",
        "status": "xi_interval_engine_routed_to_theta_mellin_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "theta_mellin_interval_engine_route_selected": route_selected,
        "self_contained_xi_interval_engine_closed": False,
        "row_column_self_contained_closed": False,
        "replacement": engine_replacement(),
        "next_priority": BALL_KERNEL,
        "secondary_priority": THETA_TAIL,
        "tertiary_priority": QUADRATURE,
        "downstream_priority": f"{BOUNDARY_NONZERO} AND {WINDING_ZERO}",
        "plain_conclusion": (
            "xi 区间求值引擎不用再固定为 Riemann-Siegel 路线。"
            "由于 theta-Poisson、theta-Mellin 和 xi 整函数层已闭合，低高度紧致矩形可改用 "
            "theta-Mellin 对称积分的复球区间引擎。真正剩余变成可实现的球算术核、"
            "高斯 theta 尾界和紧致积分分段证书。"
        ),
        "rows": rows,
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix xi 区间求值引擎 theta-Mellin 路由器",
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
            "theta_mellin_interval_engine_route_selected="
            f"{fmt_bool(result['theta_mellin_interval_engine_route_selected'])}"
        ),
        f"self_contained_xi_interval_engine_closed={fmt_bool(result['self_contained_xi_interval_engine_closed'])}",
        f"row_column_self_contained_closed={fmt_bool(result['row_column_self_contained_closed'])}",
        "```",
        "",
        "## 1. 引擎替换",
        "",
        "```text",
        result["replacement"],
        "```",
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
            f"先攻 `{result['next_priority']}`，再攻 `{result['secondary_priority']}` 与 `{result['tertiary_priority']}`。",
            f"完成引擎后进入 `{result['downstream_priority']}`。",
            "",
            "判定：本步把求值引擎路线换成可复用已有 theta-Mellin 材料的自足路线，但尚未给出区间实现。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rectangle-json", type=Path, default=DEFAULT_RECTANGLE)
    parser.add_argument("--theta-json", type=Path, default=DEFAULT_THETA)
    parser.add_argument("--xi-json", type=Path, default=DEFAULT_XI)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "rectangle": args.rectangle_json,
        "theta": args.theta_json,
        "xi": args.xi_json,
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
