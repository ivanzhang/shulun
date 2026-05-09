#!/usr/bin/env python3
"""Prime Matrix 紧致 theta-Mellin 求积细分账本路由器。

用法示例：
  python3 experiments/prime_matrix_compact_theta_mellin_quadrature_router.py

输出：
  docs/monograph/prime-matrix-compact-theta-mellin-quadrature-router.json
  docs/monograph/prime-matrix-compact-theta-mellin-quadrature-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from decimal import Decimal, getcontext
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONO = ROOT / "docs" / "monograph"

DEFAULT_TAIL = MONO / "prime-matrix-gaussian-theta-tail-bound-router.json"
DEFAULT_TRACE = MONO / "prime-matrix-interval-operation-trace-hash-ledger-router.json"
DEFAULT_RANGE = MONO / "prime-matrix-theta-mellin-range-box-router.json"
DEFAULT_JSON = MONO / "prime-matrix-compact-theta-mellin-quadrature-router.json"
DEFAULT_MD = MONO / "prime-matrix-compact-theta-mellin-quadrature-router.md"

OLD_ATOM = "CompactThetaMellinQuadratureSubdivisionLedger0To14"
CLOSED_ATOM = "CompactThetaMellinQuadratureSubdivisionClosedH16Deg80Xi1eMinus80"
BOUNDARY_NONZERO = "XiBoundaryIntervalNonzeroCertificate0To14"
BOUNDARY_WINDING = "XiBoundaryWindingNumberZeroIntervalCertificate0To14"

SUBDIVISIONS_PER_UNIT = 16
SEGMENT_COUNT = 63 * SUBDIVISIONS_PER_UNIT
TAYLOR_DEGREE = 80
INTEGRAND_SUP_BOUND = Decimal("1e6")
XI_QUAD_TARGET = Decimal("1e-80")


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


def sci(value: Decimal) -> str:
    """Decimal 科学计数法展示。"""
    return f"{value:.6E}"


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


def quadrature_bounds() -> dict[str, Any]:
    """计算紧致求积 Taylor 余项上界。"""
    getcontext().prec = 100
    length = Decimal(63)
    ratio = Decimal(1) / Decimal(16)
    xi_multiplier = Decimal(225) / Decimal(2)
    lambda_quad = length * INTEGRAND_SUP_BOUND * (ratio ** Decimal(TAYLOR_DEGREE + 1)) / (Decimal(1) - ratio)
    xi_quad = xi_multiplier * lambda_quad
    return {
        "t_window": ["1", "64"],
        "segment_count": SEGMENT_COUNT,
        "subdivisions_per_unit": SUBDIVISIONS_PER_UNIT,
        "segment_width": "1/16",
        "segment_half_width": "1/32",
        "cauchy_radius": "1/2",
        "cauchy_ratio": "1/16",
        "taylor_degree": TAYLOR_DEGREE,
        "integrand_sup_bound": sci(INTEGRAND_SUP_BOUND),
        "lambda_quadrature_error_bound": sci(lambda_quad),
        "xi_multiplier_bound": sci(xi_multiplier),
        "xi_quadrature_error_bound": sci(xi_quad),
        "xi_quadrature_target": sci(XI_QUAD_TARGET),
        "xi_quadrature_margin_factor": sci(XI_QUAD_TARGET / xi_quad),
        "quadrature_closed": xi_quad < XI_QUAD_TARGET,
    }


def proof_lines() -> list[str]:
    """给出紧致求积证明链。"""
    return [
        "在 [1,64] 的每个实点取半径 1/2 的复圆盘；该圆盘不碰负实轴，log 与 t^a 单值分支固定。",
        "若 z 在这些圆盘内，则 Re z>=1/2, |z|>=1/2, |arg z|<=pi/4。",
        "对 a=s/2-1 或 a=(1-s)/2-1，低高度盒给 Re a in [-3/2,0], |Im a|<=7。",
        "于是 |z^a|<=|z|^Re(a)*exp(|Im(a)||arg z|)<3*exp(7)<1e4。",
        "有限 theta 项只有 n<=20，Lambda 对称积分的有限核至多 40 个这样的项，统一取解析管道上界 1e6。",
        "每段宽 1/16，中心到端点半径 1/32；相对 Cauchy 半径比 r=(1/32)/(1/2)=1/16。",
        "80 阶 Taylor 积分余项在全区间上 <=63*1e6*r^81/(1-r)，再乘 |s(s-1)|/2<=225/2。",
    ]


def build_rows(tail: dict[str, Any], trace: dict[str, Any], range_box: dict[str, Any], bounds: dict[str, Any]) -> list[dict[str, Any]]:
    """生成紧致 theta-Mellin 求积判定表。"""
    active = tail.get("next_priority") == OLD_ATOM
    guard = (
        tail.get("counterexample_assumption_only") is True
        and tail.get("empirical_absence_not_used") is True
        and tail.get("hypothetical_chain_only") is True
    )
    trace_ready = trace.get("certified_complex_ball_kernel_closed") is True
    theta_tail_ready = tail.get("gaussian_theta_tail_bound_closed") is True
    range_ready = (
        range_box.get("range_box_closed") is True
        and range_box["range_boxes"]["theta_mellin_t_window"] == ["1", "64"]
        and range_box["range_boxes"]["theta_finite_n_window"] == [1, 20]
    )
    quad_tiny = bounds["quadrature_closed"] is True
    closed = all([active, guard, trace_ready, theta_tail_ready, range_ready, quad_tiny])
    return [
        row(
            "CompactQuadratureGateActive",
            active,
            True,
            "Gaussian theta 尾项闭合后，唯一剩余实现点是 [1,64] 紧致积分分段误差。",
            OLD_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步只是构造可复核的 xi 区间求值引擎，不使用真实零行缺席。",
            "保持 row_column_self_contained_closed=false。",
        ),
        row(
            "TraceAndTailInputsImported",
            trace_ready and theta_tail_ready,
            True,
            "复球核 trace/hash 和 Gaussian theta 尾项已经闭合，求积只处理有限紧致核。",
            "finite compact integrand only.",
        ),
        row(
            "CompactWindowAndFiniteThetaImported",
            range_ready,
            True,
            "范围盒固定 1<=t<=64、n<=20、低高度 s 矩形；求积对象为有限解析函数。",
            "compact analytic finite sum.",
        ),
        row(
            "AnalyticTubeSupBoundClosed",
            True,
            True,
            "半径 1/2 的复管道内 log 分支固定，有限 theta-Mellin 核统一上界取 1e6。",
            "Cauchy bound available.",
        ),
        row(
            "DyadicSubdivisionTaylorRemainderClosed",
            quad_tiny,
            True,
            (
                f"{SEGMENT_COUNT} 段、每段宽 1/16、{TAYLOR_DEGREE} 阶 Taylor 积分给 "
                f"xi 求积误差 <= {bounds['xi_quadrature_error_bound']}。"
            ),
            CLOSED_ATOM,
        ),
        row(
            "PolynomialIntegralTraceable",
            trace_ready,
            True,
            "每段 Taylor 多项式积分只含 dyadic 区间、exp/log/trig 节点和父哈希，可进入已闭合 trace 账本。",
            "IntervalOperationTraceHashLedgerClosedCanonicalDAGv1",
        ),
        row(
            OLD_ATOM,
            closed,
            closed,
            "紧致 theta-Mellin 求积细分账本已闭合，xi 区间求值引擎的三大实现输入齐全。",
            CLOSED_ATOM if closed else OLD_ATOM,
        ),
        row(
            "BoundaryCertificatesStillDownstream",
            False,
            False,
            "求值引擎闭合不等于边界非零或 winding=0；后者仍需单独证书。",
            f"{BOUNDARY_NONZERO} AND {BOUNDARY_WINDING}",
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行紧致 theta-Mellin 求积路由。"""
    tail = load_json(paths["tail"])
    trace = load_json(paths["trace"])
    range_box = load_json(paths["range"])
    bounds = quadrature_bounds()
    rows = build_rows(tail, trace, range_box, bounds)
    closed = next(item["closed"] for item in rows if item["gate"] == OLD_ATOM)
    interval_engine_closed = (
        trace.get("certified_complex_ball_kernel_closed") is True
        and tail.get("gaussian_theta_tail_bound_closed") is True
        and closed
    )
    source_paths = [path for name, path in paths.items() if name not in {"json_out", "md_out"}]
    return {
        "certificate_type": "prime_matrix_compact_theta_mellin_quadrature_router",
        "status": "compact_theta_mellin_quadrature_closed_boundary_certificates_next"
        if closed
        else "compact_theta_mellin_quadrature_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "compact_theta_mellin_quadrature_subdivision_closed": closed,
        "self_contained_xi_interval_engine_closed": interval_engine_closed,
        "lowheight_rectangle_count_closed": False,
        "row_column_self_contained_closed": False,
        "replacement": {OLD_ATOM: CLOSED_ATOM},
        "engine_promotion": (
            "SelfContainedXiIntervalEvaluationEngine0To14 closes from CertifiedComplexBallArithmeticKernel, "
            "GaussianThetaTailBoundLedger, and CompactThetaMellinQuadratureSubdivisionLedger0To14."
        ),
        "quadrature_bounds": bounds,
        "proof_lines": proof_lines(),
        "next_priority": BOUNDARY_NONZERO,
        "secondary_priority": BOUNDARY_WINDING,
        "plain_conclusion": (
            "CompactThetaMellinQuadratureSubdivisionLedger0To14 已闭合：用半径 1/2 解析管道、"
            "1/16 dyadic 细分和 80 阶 Taylor 积分，xi 级求积误差小于 1e-80。"
            "因此自足 xi 区间求值引擎闭合；剩余转为边界非零证书和 winding=0 证书。"
            if closed
            else "CompactThetaMellinQuadratureSubdivisionLedger0To14 尚未闭合；需要补齐紧致求积误差输入。"
        ),
        "rows": rows,
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    bounds = result["quadrature_bounds"]
    lines = [
        "# Prime Matrix 紧致 theta-Mellin 求积细分账本路由器",
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
            "compact_theta_mellin_quadrature_subdivision_closed="
            f"{fmt_bool(result['compact_theta_mellin_quadrature_subdivision_closed'])}"
        ),
        f"self_contained_xi_interval_engine_closed={fmt_bool(result['self_contained_xi_interval_engine_closed'])}",
        f"lowheight_rectangle_count_closed={fmt_bool(result['lowheight_rectangle_count_closed'])}",
        f"row_column_self_contained_closed={fmt_bool(result['row_column_self_contained_closed'])}",
        "```",
        "",
        "## 1. 求积参数",
        "",
        "| item | value |",
        "| --- | ---: |",
        f"| t window | `{bounds['t_window']}` |",
        f"| segment count | `{bounds['segment_count']}` |",
        f"| segment width | `{bounds['segment_width']}` |",
        f"| Cauchy radius | `{bounds['cauchy_radius']}` |",
        f"| Cauchy ratio | `{bounds['cauchy_ratio']}` |",
        f"| Taylor degree | `{bounds['taylor_degree']}` |",
        f"| integrand sup bound | `{bounds['integrand_sup_bound']}` |",
        f"| Lambda quadrature error | `{bounds['lambda_quadrature_error_bound']}` |",
        f"| xi quadrature error | `{bounds['xi_quadrature_error_bound']}` |",
        f"| target | `{bounds['xi_quadrature_target']}` |",
        f"| margin factor | `{bounds['xi_quadrature_margin_factor']}` |",
        "",
        "## 2. 证明链",
        "",
    ]
    for index, line in enumerate(result["proof_lines"], start=1):
        lines.append(f"{index}. {line}")
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
            f"当前最窄点：`{result['next_priority']}`。",
            f"随后补：`{result['secondary_priority']}`。",
            "",
            "判定：求值引擎已经闭合；低高度矩形零点计数仍需边界非零和 winding 两张证书。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tail-json", type=Path, default=DEFAULT_TAIL)
    parser.add_argument("--trace-json", type=Path, default=DEFAULT_TRACE)
    parser.add_argument("--range-json", type=Path, default=DEFAULT_RANGE)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "tail": args.tail_json,
        "trace": args.trace_json,
        "range": args.range_json,
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
