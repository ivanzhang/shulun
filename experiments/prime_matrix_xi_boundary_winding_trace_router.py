#!/usr/bin/env python3
"""Prime Matrix xi 边界 winding trace 路由器。

用法示例：
  python3 experiments/prime_matrix_xi_boundary_winding_trace_router.py

输出：
  docs/monograph/prime-matrix-xi-boundary-winding-trace-router.json
  docs/monograph/prime-matrix-xi-boundary-winding-trace-router.md
"""

from __future__ import annotations

import argparse
import cmath
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONO = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = MONO / "prime-matrix-top-critical-endpoint-chain-aggregation-router.json"
DEFAULT_JSON = MONO / "prime-matrix-xi-boundary-winding-trace-router.json"
DEFAULT_MD = MONO / "prime-matrix-xi-boundary-winding-trace-router.md"

OLD_ATOM = "XiBoundaryWindingNumberZeroIntervalCertificate0To14"
TRACE_ATOM = "XiBoundaryArgumentVariationDyadicTraceLedger0To14Mesh8192"
TRACE_DISCIPLINE_ATOM = "XiBoundaryArgumentVariationTraceDisciplineClosed"
EXTERNAL_ATOM = "ClassicalFirstZetaZeroHeightGT14ExternalAccepted"
EXTERNAL_CLOSED = "XiBoundaryWindingNumberZeroExternalClosedByFirstZeroGT14"

EM_N = 48
EM_P = 8
HEIGHT = 14.0
SIGMA_LEFT = -1.0
SIGMA_RIGHT = 2.0
DEFAULT_SAMPLES_PER_SIDE = 2048

BERNOULLI = {
    2: Fraction(1, 6),
    4: Fraction(-1, 30),
    6: Fraction(1, 42),
    8: Fraction(-1, 30),
    10: Fraction(5, 66),
    12: Fraction(-691, 2730),
    14: Fraction(7, 6),
    16: Fraction(-3617, 510),
}

LANCZOS_COEFFS = [
    0.99999999999980993,
    676.5203681218851,
    -1259.1392167224028,
    771.32342877765313,
    -176.61502916214059,
    12.507343278686905,
    -0.13857109526572012,
    9.9843695780195716e-6,
    1.5056327351493116e-7,
]


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


def loggamma_lanczos(z: complex) -> complex:
    """Lanczos 公式近似复 log Gamma，仅作 winding 侦察。"""
    if z.real < 0.5:
        return math.log(math.pi) - cmath.log(cmath.sin(math.pi * z)) - loggamma_lanczos(1 - z)
    shifted = z - 1
    accum = LANCZOS_COEFFS[0]
    for index in range(1, len(LANCZOS_COEFFS)):
        accum += LANCZOS_COEFFS[index] / (shifted + index)
    t = shifted + 7.5
    return 0.5 * math.log(2 * math.pi) + (shifted + 0.5) * cmath.log(t) - t + cmath.log(accum)


def zeta_euler_maclaurin(s: complex) -> complex:
    """Euler-Maclaurin 近似 zeta(s)，仅作 winding 侦察。"""
    log_n = math.log(EM_N)
    total = sum(cmath.exp(-s * math.log(n)) for n in range(1, EM_N))
    total += cmath.exp((1 - s) * log_n) / (s - 1)
    total += 0.5 * cmath.exp(-s * log_n)
    rising = 1 + 0j
    for k in range(1, EM_P + 1):
        if k == 1:
            rising = s
        else:
            rising *= (s + 2 * k - 3) * (s + 2 * k - 2)
        coeff = float(BERNOULLI[2 * k]) / math.factorial(2 * k)
        total += coeff * rising * cmath.exp(-(s + 2 * k - 1) * log_n)
    return total


def xi_value(s: complex) -> complex:
    """计算 xi(s) 的侦察值，s=0,1 使用可去点值。"""
    if abs(s) < 1e-12 or abs(s - 1) < 1e-12:
        return 0.5 + 0j
    return (
        0.5
        * s
        * (s - 1)
        * cmath.exp(-0.5 * s * math.log(math.pi) + loggamma_lanczos(s / 2))
        * zeta_euler_maclaurin(s)
    )


def boundary_points(samples_per_side: int) -> list[complex]:
    """生成逆时针矩形边界采样点。"""
    points: list[complex] = []
    for i in range(samples_per_side + 1):
        points.append(SIGMA_LEFT + (SIGMA_RIGHT - SIGMA_LEFT) * i / samples_per_side + 0j)
    for i in range(1, samples_per_side + 1):
        points.append(SIGMA_RIGHT + 1j * HEIGHT * i / samples_per_side)
    for i in range(1, samples_per_side + 1):
        points.append(SIGMA_RIGHT - (SIGMA_RIGHT - SIGMA_LEFT) * i / samples_per_side + 1j * HEIGHT)
    for i in range(1, samples_per_side + 1):
        points.append(SIGMA_LEFT + 1j * HEIGHT * (1 - i / samples_per_side))
    return points


def winding_float_audit(samples_per_side: int) -> dict[str, Any]:
    """计算边界 winding 的浮点侦察摘要。"""
    points = boundary_points(samples_per_side)
    values = [xi_value(point) for point in points]
    total_angle = 0.0
    max_step_angle = 0.0
    min_abs = float("inf")
    min_abs_index = 0
    finite = True
    for index, (left, right) in enumerate(zip(values, values[1:] + values[:1])):
        if not (
            math.isfinite(left.real)
            and math.isfinite(left.imag)
            and math.isfinite(right.real)
            and math.isfinite(right.imag)
        ):
            finite = False
            break
        abs_left = abs(left)
        if abs_left < min_abs:
            min_abs = abs_left
            min_abs_index = index
        step = cmath.phase(right / left)
        total_angle += step
        max_step_angle = max(max_step_angle, abs(step))
    winding = total_angle / (2 * math.pi)
    return {
        "samples_per_side": samples_per_side,
        "point_count": len(points),
        "finite": finite,
        "total_angle": total_angle,
        "winding_float": winding,
        "winding_rounded": round(winding),
        "rounding_error": abs(winding - round(winding)),
        "max_step_angle": max_step_angle,
        "min_abs_value": min_abs,
        "min_abs_index": min_abs_index,
        "min_abs_point_re": points[min_abs_index].real,
        "min_abs_point_im": points[min_abs_index].imag,
        "audit_supports_winding_zero": finite and round(winding) == 0 and abs(winding) < 1e-8,
    }


def trace_contract() -> list[str]:
    """写出自足 winding trace 合同。"""
    return [
        "用 dyadic 网格沿矩形边界 [-1,2] x [0,14] 逆时针取样，角点 s=0,1 使用 xi 的可去点值。",
        "每个节点用已闭合 SelfContainedXiIntervalEvaluationEngine0To14 输出 xi(s_j) 的复矩形区间和 trace hash。",
        "每条边段还需一个 xi' 的区间包络或直接的整段 xi 管道盒，证明该边段像不穿过 0。",
        "对相邻节点构造有理复数交叉积/点积区间，给出每步辐角增量所在的长度 < pi/2 区间。",
        "把所有辐角增量区间相加，证明总辐角变化属于 (-pi,pi)，且按端点方向连续为 0。",
        "这样 winding=0 由有限整数/有理区间 trace 复放给出，不借用真实零点缺席。",
    ]


def build_rows(previous: dict[str, Any], audit: dict[str, Any]) -> list[dict[str, Any]]:
    """生成 winding trace 判定表。"""
    active = previous.get("next_priority") == OLD_ATOM
    guard = (
        previous.get("counterexample_assumption_only") is True
        and previous.get("empirical_absence_not_used") is True
        and previous.get("hypothetical_chain_only") is True
    )
    boundary_nonzero = previous.get("boundary_nonzero_self_contained_closed") is True
    return [
        row(
            "WindingGateActive",
            active,
            True,
            "边界非零闭合后，唯一剩余是边界绕数为 0。",
            OLD_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只处理假设链条的解析证书，不使用真实零行缺席。",
            "保持 row_column_self_contained_closed=false。",
        ),
        row(
            "BoundaryNonzeroImported",
            boundary_nonzero,
            True,
            "边界非零已闭合，winding 可以由连续辐角 trace 定义。",
            "no boundary zero obstruction.",
        ),
        row(
            "FloatAuditWindingZero",
            audit["audit_supports_winding_zero"],
            False,
            (
                f"侦察 winding≈{audit['winding_float']:.3e}，最大单步角≈"
                f"{audit['max_step_angle']:.6f}，支持 trace 路线。"
            ),
            "不能作为自足证明，只用于确定网格和证书形状。",
        ),
        row(
            "TraceDisciplineSpecified",
            True,
            True,
            "winding trace 的节点、边段、角增量和总和复放规则已明确。",
            TRACE_DISCIPLINE_ATOM,
        ),
        row(
            "SelfContainedTraceStillMissing",
            False,
            False,
            "还需实际生成 dyadic 区间 trace/hash，逐段证明像不穿过 0 且总角变化为 0。",
            TRACE_ATOM,
        ),
        row(
            "ExternalFirstZeroRoute",
            True,
            False,
            "若接受外部首零点高度 >14 或 Turing 完备性证书，则内部无零点，winding=0 条件闭合。",
            f"{EXTERNAL_ATOM} => {EXTERNAL_CLOSED}",
        ),
        row(
            OLD_ATOM,
            False,
            False,
            "严格自足 winding 尚未闭合；已压缩成一个有限 dyadic argument-variation trace。",
            TRACE_ATOM,
        ),
    ]


def run(paths: dict[str, Path], samples_per_side: int) -> dict[str, Any]:
    """执行 winding trace 路由。"""
    previous = load_json(paths["previous"])
    audit = winding_float_audit(samples_per_side)
    rows = build_rows(previous, audit)
    source_paths = [path for name, path in paths.items() if name not in {"json_out", "md_out"}]
    return {
        "certificate_type": "prime_matrix_xi_boundary_winding_trace_router",
        "status": "winding_reduced_to_finite_argument_variation_trace_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "boundary_nonzero_self_contained_closed": previous.get("boundary_nonzero_self_contained_closed") is True,
        "winding_float_audit_zero": audit["audit_supports_winding_zero"],
        "winding_self_contained_closed": False,
        "winding_external_closed": True,
        "lowheight_rectangle_count_self_contained_closed": False,
        "row_column_self_contained_closed": False,
        "replacement_self_contained": {OLD_ATOM: TRACE_ATOM},
        "replacement_external": {OLD_ATOM: EXTERNAL_CLOSED},
        "audit": audit,
        "trace_contract": trace_contract(),
        "rows": rows,
        "next_priority": TRACE_ATOM,
        "external_priority": EXTERNAL_ATOM,
        "plain_conclusion": (
            "winding 的严格自足剩余已压缩成有限 dyadic 边界辐角 trace。浮点侦察在 "
            f"{audit['point_count']} 个边界点上得到 winding≈{audit['winding_float']:.3e}，"
            "支持绕数为 0；但自足闭合仍需实际 interval trace/hash。外部首零点 >14 路线可条件闭合。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    audit = result["audit"]
    lines = [
        "# Prime Matrix xi 边界 winding trace 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"boundary_nonzero_self_contained_closed={fmt_bool(result['boundary_nonzero_self_contained_closed'])}",
        f"winding_float_audit_zero={fmt_bool(result['winding_float_audit_zero'])}",
        f"winding_self_contained_closed={fmt_bool(result['winding_self_contained_closed'])}",
        f"winding_external_closed={fmt_bool(result['winding_external_closed'])}",
        (
            "lowheight_rectangle_count_self_contained_closed="
            f"{fmt_bool(result['lowheight_rectangle_count_self_contained_closed'])}"
        ),
        f"row_column_self_contained_closed={fmt_bool(result['row_column_self_contained_closed'])}",
        "```",
        "",
        "## 1. 浮点侦察",
        "",
        "| item | value |",
        "| --- | ---: |",
        f"| samples per side | `{audit['samples_per_side']}` |",
        f"| point count | `{audit['point_count']}` |",
        f"| winding float | `{audit['winding_float']:.12e}` |",
        f"| winding rounded | `{audit['winding_rounded']}` |",
        f"| rounding error | `{audit['rounding_error']:.12e}` |",
        f"| max step angle | `{audit['max_step_angle']:.12f}` |",
        f"| min abs value | `{audit['min_abs_value']:.12e}` |",
        f"| min abs point | `({audit['min_abs_point_re']:.6f}, {audit['min_abs_point_im']:.6f})` |",
        "",
        "## 2. 自足 trace 合同",
        "",
    ]
    for index, item in enumerate(result["trace_contract"], start=1):
        lines.append(f"{index}. {item}")
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
            f"严格自足唯一剩余：`{result['next_priority']}`。",
            f"外部条件闭合输入：`{result['external_priority']}`。",
            "",
            "判定：winding 已变成有限 trace 物化问题；尚未无条件自足闭合。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous-json", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--samples-per-side", type=int, default=DEFAULT_SAMPLES_PER_SIDE)
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
    result = run(paths, args.samples_per_side)
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(result["status"])
    print(result["next_priority"])


if __name__ == "__main__":
    main()
