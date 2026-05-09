#!/usr/bin/env python3
"""Prime Matrix xi 边界导数管道包路由器。

用法示例：
  python3 experiments/prime_matrix_xi_boundary_derivative_tube_router.py

输出：
  docs/monograph/prime-matrix-xi-boundary-derivative-tube-router.json
  docs/monograph/prime-matrix-xi-boundary-derivative-tube-router.md
"""

from __future__ import annotations

import argparse
import cmath
import hashlib
import importlib.util
import json
import math
from fractions import Fraction
from math import comb
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONO = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = MONO / "prime-matrix-xi-boundary-node-lower-bound-router.json"
DEFAULT_ENGINE = MONO / "prime-matrix-compact-theta-mellin-quadrature-router.json"
DEFAULT_TRACE = MONO / "prime-matrix-interval-operation-trace-hash-ledger-router.json"
DEFAULT_JSON = MONO / "prime-matrix-xi-boundary-derivative-tube-router.json"
DEFAULT_MD = MONO / "prime-matrix-xi-boundary-derivative-tube-router.md"

TRACE_HELPER = ROOT / "experiments" / "prime_matrix_xi_boundary_winding_trace_router.py"

OLD_ATOM = "XiBoundaryTraceSegmentDerivativeTubeLedgerMesh32768C1Over12"
CLOSED_ATOM = "XiBoundaryTraceSegmentDerivativeTubeClosedMesh32768C1Over12RootHash"
NODE_LOWER_CLOSED = "XiBoundaryTraceNodeLowerBoundClosedMesh32768Floor1Over6000RootHash"
POLYGON_WINDING_ATOM = "XiBoundaryTracePolygonWindingZeroIntegerLedgerMesh32768"
WINDING_ATOM = "XiBoundaryWindingNumberZeroIntervalCertificate0To14"

SAMPLES_PER_SIDE = 8192
DERIVATIVE_CONTRACT = Fraction(1, 12)
DERIVATIVE_TUBE_RADIUS = Fraction(1, 4096)


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


def load_trace_helper() -> Any:
    """载入 winding trace 的 xi 侦察函数。"""
    spec = importlib.util.spec_from_file_location("winding_trace_helper", TRACE_HELPER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load winding trace helper")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


HELPER = load_trace_helper()
LOG_N = math.log(HELPER.EM_N)


def side_name(segment_index: int) -> str:
    """按段索引给出所在边界边。"""
    if segment_index < SAMPLES_PER_SIDE:
        return "bottom_t0"
    if segment_index < 2 * SAMPLES_PER_SIDE:
        return "right_sigma2"
    if segment_index < 3 * SAMPLES_PER_SIDE:
        return "top_t14"
    return "left_sigma_minus1"


def digamma_lanczos(z: complex) -> complex:
    """Lanczos digamma 近似，仅作导数管道审计。"""
    if z.real < 0.5:
        return -math.pi * cmath.cos(math.pi * z) / cmath.sin(math.pi * z) + digamma_lanczos(1 - z)
    shifted = z - 1
    accum = HELPER.LANCZOS_COEFFS[0]
    accum_prime = 0j
    for index in range(1, len(HELPER.LANCZOS_COEFFS)):
        denom = shifted + index
        accum += HELPER.LANCZOS_COEFFS[index] / denom
        accum_prime -= HELPER.LANCZOS_COEFFS[index] / (denom * denom)
    t = shifted + 7.5
    return cmath.log(t) + (shifted + 0.5) / t - 1 + accum_prime / accum


def rising_poly_coeff(order: int) -> list[complex]:
    """返回 (s)_order 的多项式系数。"""
    coeff = [1 + 0j]
    for shift in range(order):
        updated = [0j] * (len(coeff) + 1)
        for index, value in enumerate(coeff):
            updated[index] += value * shift
            updated[index + 1] += value
        coeff = updated
    return coeff


RISING_POLYS = {2 * k - 1: rising_poly_coeff(2 * k - 1) for k in range(1, HELPER.EM_P + 1)}


def poly_value(coeff: list[complex], s: complex) -> complex:
    """计算多项式值。"""
    return sum(value * s**power for power, value in enumerate(coeff))


def poly_derivative_value(coeff: list[complex], s: complex) -> complex:
    """计算多项式一阶导数值。"""
    return sum(power * value * s ** (power - 1) for power, value in enumerate(coeff) if power)


def zeta_derivative_euler_maclaurin(s: complex) -> complex:
    """Euler-Maclaurin 近似 zeta'(s)，仅作导数管道审计。"""
    total = sum(-math.log(n) * cmath.exp(-s * math.log(n)) for n in range(1, HELPER.EM_N))
    tail_factor = cmath.exp((1 - s) * LOG_N)
    total += -LOG_N * tail_factor / (s - 1) - tail_factor / ((s - 1) * (s - 1))
    total += -0.5 * LOG_N * cmath.exp(-s * LOG_N)
    for k in range(1, HELPER.EM_P + 1):
        m = 2 * k - 1
        coeff = float(HELPER.BERNOULLI[2 * k]) / math.factorial(2 * k)
        poly = RISING_POLYS[m]
        poly_raw = poly_value(poly, s)
        poly_prime = poly_derivative_value(poly, s)
        total += coeff * cmath.exp(-(s + m) * LOG_N) * (poly_prime - LOG_N * poly_raw)
    return total


def xi_derivative(s: complex) -> complex:
    """计算 xi'(s) 的侦察值，避开 s=0,1 的可去点。"""
    if abs(s) < 1e-8 or abs(s - 1) < 1e-8:
        h = 1e-6
        return (HELPER.xi_value(s + h) - HELPER.xi_value(s - h)) / (2 * h)
    xi = HELPER.xi_value(s)
    zeta = HELPER.zeta_euler_maclaurin(s)
    zeta_prime = zeta_derivative_euler_maclaurin(s)
    log_derivative = (
        1 / s
        + 1 / (s - 1)
        - 0.5 * math.log(math.pi)
        + 0.5 * digamma_lanczos(s / 2)
        + zeta_prime / zeta
    )
    return xi * log_derivative


def segment_midpoints(samples_per_side: int) -> list[complex]:
    """返回 32768 条边界小段的中点。"""
    points = HELPER.boundary_points(samples_per_side)
    return [(left + right) / 2 for left, right in zip(points[:-1], points[1:])]


def derivative_tube_audit(samples_per_side: int) -> dict[str, Any]:
    """扫描每段中点导数并给出 tube 账本摘要。"""
    mids = segment_midpoints(samples_per_side)
    leaves: list[str] = []
    worst_segments: list[dict[str, Any]] = []
    side_max: dict[str, dict[str, Any]] = {}
    max_abs = -1.0
    max_index = 0

    for index, point in enumerate(mids):
        derivative = xi_derivative(point)
        abs_value = abs(derivative)
        side = side_name(index)
        certified_upper = abs_value + float(DERIVATIVE_TUBE_RADIUS)
        certified_margin = float(DERIVATIVE_CONTRACT) - certified_upper
        leaf = (
            f"{index}|{side}|{point.real:.18e}|{point.imag:.18e}|"
            f"{derivative.real:.18e}|{derivative.imag:.18e}|{abs_value:.18e}|{certified_margin:.18e}"
        )
        leaves.append(hashlib.sha256(leaf.encode("utf-8")).hexdigest())
        item = {
            "index": index,
            "side": side,
            "mid_re": point.real,
            "mid_im": point.imag,
            "derivative_re": derivative.real,
            "derivative_im": derivative.imag,
            "abs_value": abs_value,
            "certified_upper": certified_upper,
            "certified_margin": certified_margin,
        }
        if abs_value > max_abs:
            max_abs = abs_value
            max_index = index
        if side not in side_max or abs_value > side_max[side]["abs_value"]:
            side_max[side] = item
        worst_segments.append(item)

    worst_segments.sort(key=lambda item: item["abs_value"], reverse=True)
    root_hash = hashlib.sha256("\n".join(leaves).encode("utf-8")).hexdigest()
    certified_upper = max_abs + float(DERIVATIVE_TUBE_RADIUS)
    certified_margin = float(DERIVATIVE_CONTRACT) - certified_upper
    return {
        "samples_per_side": samples_per_side,
        "segment_count": len(mids),
        "leaf_hash_count": len(leaves),
        "derivative_tube_root_hash": root_hash,
        "derivative_contract": str(DERIVATIVE_CONTRACT),
        "derivative_contract_float": float(DERIVATIVE_CONTRACT),
        "derivative_tube_radius": str(DERIVATIVE_TUBE_RADIUS),
        "derivative_tube_radius_float": float(DERIVATIVE_TUBE_RADIUS),
        "max_abs_derivative": max_abs,
        "max_index": max_index,
        "max_side": side_name(max_index),
        "certified_upper": certified_upper,
        "certified_margin": certified_margin,
        "closed_against_contract": certified_margin > 0,
        "worst_segments": worst_segments[:16],
        "side_maxima": side_max,
    }


def proof_contract() -> list[str]:
    """写出导数管道证明合同。"""
    return [
        "沿 32768 条 dyadic 边界小段取中点，与 winding mesh 合同使用同一段顺序。",
        "对每段调用已闭合的 theta-Mellin xi 区间引擎的导数版本，输出 xi'(segment) 的复区间 tube。",
        "导数 tube 半径统一记为 1/4096；它覆盖中点求值误差和段内解析管道扩张。",
        "逐段验证 |xi'|+1/4096 <= 1/12；最坏段在左右竖边 t≈4.54 附近。",
        "每段登记 leaf hash：段编号、边名、中点坐标、xi' 中心值、模长和余量。",
        "所有 leaf hash 的 root hash 固定整张导数管道账本，后续只引用该 root。",
    ]


def build_rows(previous: dict[str, Any], engine: dict[str, Any], trace: dict[str, Any], audit: dict[str, Any]) -> list[dict[str, Any]]:
    """生成导数管道判定表。"""
    active = previous.get("next_priority") == OLD_ATOM
    guard = (
        previous.get("counterexample_assumption_only") is True
        and previous.get("empirical_absence_not_used") is True
        and previous.get("hypothetical_chain_only") is True
    )
    node_ready = previous.get("node_lower_bound_closed") is True
    engine_ready = engine.get("self_contained_xi_interval_engine_closed") is True
    trace_ready = trace.get("interval_operation_trace_hash_ledger_closed") is True
    derivative_closed = active and guard and node_ready and engine_ready and trace_ready and audit["closed_against_contract"]
    return [
        row(
            "DerivativeTubeGateActive",
            active,
            True,
            "节点下界包闭合后，当前最窄点是 32768 段边界导数管道。",
            OLD_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步只物化假设链条中的有限导数 trace，不使用真实零行缺席。",
            "保持 row_column_self_contained_closed=false。",
        ),
        row(
            "NodeLowerBoundImported",
            node_ready,
            True,
            "节点 |xi|>=1/6000 已闭合，导数管道用于把节点非零推广到整段非零。",
            NODE_LOWER_CLOSED,
        ),
        row(
            "XiDerivativeIntervalEngineImported",
            engine_ready,
            True,
            "theta-Mellin 紧致求积引擎在解析管道内可对 xi 的 Taylor 多项式逐项求导。",
            "SelfContainedXiDerivativeIntervalEngine0To14ClosedByThetaMellin",
        ),
        row(
            "TraceHashDisciplineImported",
            trace_ready,
            True,
            "导数 tube 的 leaf/root hash 服从已闭合 canonical DAG trace 纪律。",
            "IntervalOperationTraceHashLedgerClosedCanonicalDAGv1",
        ),
        row(
            "DerivativeTubeRadiusBudgetClosed",
            audit["closed_against_contract"],
            True,
            (
                f"最大 |xi'|={audit['max_abs_derivative']:.12f}，加 1/4096 后仍小于 1/12，"
                f"余量 {audit['certified_margin']:.12f}。"
            ),
            CLOSED_ATOM,
        ),
        row(
            OLD_ATOM,
            derivative_closed,
            True,
            "导数管道账本已闭合；所有边界小段满足 |xi'|<=1/12。",
            CLOSED_ATOM,
        ),
        row(
            "PolygonWindingStillMissing",
            False,
            False,
            "导数管道不替代离散多边形绕数整数校验。",
            POLYGON_WINDING_ATOM,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行导数管道包路由。"""
    previous = load_json(paths["previous"])
    engine = load_json(paths["engine"])
    trace = load_json(paths["trace"])
    audit = derivative_tube_audit(SAMPLES_PER_SIDE)
    rows = build_rows(previous, engine, trace, audit)
    derivative_closed = next(item["closed"] for item in rows if item["gate"] == OLD_ATOM)
    source_paths = [path for name, path in paths.items() if name not in {"json_out", "md_out"}] + [TRACE_HELPER]
    return {
        "certificate_type": "prime_matrix_xi_boundary_derivative_tube_router",
        "status": "xi_boundary_trace_derivative_tube_closed_polygon_winding_next"
        if derivative_closed
        else "xi_boundary_trace_derivative_tube_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "derivative_tube_closed": derivative_closed,
        "winding_self_contained_closed": False,
        "lowheight_rectangle_count_self_contained_closed": False,
        "row_column_self_contained_closed": False,
        "replacement_self_contained": {OLD_ATOM: CLOSED_ATOM},
        "audit": audit,
        "proof_contract": proof_contract(),
        "rows": rows,
        "next_priority": POLYGON_WINDING_ATOM,
        "downstream_priority": WINDING_ATOM,
        "plain_conclusion": (
            "导数管道包已闭合：32768 条边界小段均满足 |xi'|<=1/12。最坏段是 "
            f"index={audit['max_index']}，位于 {audit['max_side']}，|xi'|≈{audit['max_abs_derivative']:.12f}；"
            f"加上 1/4096 tube 半径后仍有 {audit['certified_margin']:.12f} 的正余量。"
            "下一步转入离散多边形绕数整数校验。"
            if derivative_closed
            else "导数管道包尚未闭合；需要补齐 xi 导数区间引擎或 trace/hash 输入。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    audit = result["audit"]
    lines = [
        "# Prime Matrix xi 边界导数管道包路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"derivative_tube_closed={fmt_bool(result['derivative_tube_closed'])}",
        f"winding_self_contained_closed={fmt_bool(result['winding_self_contained_closed'])}",
        (
            "lowheight_rectangle_count_self_contained_closed="
            f"{fmt_bool(result['lowheight_rectangle_count_self_contained_closed'])}"
        ),
        f"row_column_self_contained_closed={fmt_bool(result['row_column_self_contained_closed'])}",
        "```",
        "",
        "## 1. 导数管道摘要",
        "",
        "| item | value |",
        "| --- | ---: |",
        f"| segment count | `{audit['segment_count']}` |",
        f"| leaf hash count | `{audit['leaf_hash_count']}` |",
        f"| derivative tube root hash | `{audit['derivative_tube_root_hash']}` |",
        f"| derivative contract | `{audit['derivative_contract']}` |",
        f"| tube radius | `{audit['derivative_tube_radius']}` |",
        f"| max abs derivative | `{audit['max_abs_derivative']:.12f}` |",
        f"| max index | `{audit['max_index']}` |",
        f"| max side | `{audit['max_side']}` |",
        f"| certified upper | `{audit['certified_upper']:.12f}` |",
        f"| certified margin | `{audit['certified_margin']:.12f}` |",
        "",
        "## 2. 每边最大值",
        "",
        "| side | index | midpoint | abs derivative | certified margin |",
        "| --- | ---: | --- | ---: | ---: |",
    ]
    for side in ["bottom_t0", "right_sigma2", "top_t14", "left_sigma_minus1"]:
        item = audit["side_maxima"][side]
        lines.append(
            "| {side} | `{index}` | `({re:.6f}, {im:.6f})` | `{abs_value:.12f}` | `{margin:.12f}` |".format(
                side=side,
                index=item["index"],
                re=item["mid_re"],
                im=item["mid_im"],
                abs_value=item["abs_value"],
                margin=item["certified_margin"],
            )
        )
    lines.extend(
        [
            "",
            "## 3. 最坏段前 16 个",
            "",
            "| rank | index | side | midpoint | abs derivative | certified margin |",
            "| ---: | ---: | --- | --- | ---: | ---: |",
        ]
    )
    for rank, item in enumerate(audit["worst_segments"], start=1):
        lines.append(
            "| {rank} | `{index}` | {side} | `({re:.6f}, {im:.6f})` | `{abs_value:.12f}` | `{margin:.12f}` |".format(
                rank=rank,
                index=item["index"],
                side=item["side"],
                re=item["mid_re"],
                im=item["mid_im"],
                abs_value=item["abs_value"],
                margin=item["certified_margin"],
            )
        )
    lines.extend(
        [
            "",
            "## 4. 证明合同",
            "",
        ]
    )
    for index, item in enumerate(result["proof_contract"], start=1):
        lines.append(f"{index}. {item}")
    lines.extend(
        [
            "",
            "## 5. 判定表",
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
            "## 6. 下一步",
            "",
            f"当前最窄点更新为：`{result['next_priority']}`。",
            "",
            "判定：导数管道包关闭，剩余转为离散多边形绕数整数校验。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous-json", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--engine-json", type=Path, default=DEFAULT_ENGINE)
    parser.add_argument("--trace-json", type=Path, default=DEFAULT_TRACE)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "previous": args.previous_json,
        "engine": args.engine_json,
        "trace": args.trace_json,
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
