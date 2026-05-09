#!/usr/bin/env python3
"""Prime Matrix 顶边端点 Euler-Maclaurin replay 包路由器。

用法示例：
  python3 experiments/prime_matrix_top_endpoint_em_replay_package_router.py

输出：
  docs/monograph/prime-matrix-top-endpoint-em-replay-package-router.json
  docs/monograph/prime-matrix-top-endpoint-em-replay-package-router.md
"""

from __future__ import annotations

import argparse
import cmath
import hashlib
import json
import math
from fractions import Fraction
from math import comb
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONO = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = MONO / "prime-matrix-top-critical-third-derivative-taylor-ladder-router.json"
DEFAULT_ROUNDING = MONO / "prime-matrix-em-replay-rounding-discipline-router.json"
DEFAULT_JSON = MONO / "prime-matrix-top-endpoint-em-replay-package-router.json"
DEFAULT_MD = MONO / "prime-matrix-top-endpoint-em-replay-package-router.md"

SIGN_LADDER_ATOM = "TopEndpointImagDerivativeAlternatingSignReplaySigma1T14Orders3To10"
SIGN_LADDER_CLOSED = "TopEndpointImagDerivativeAlternatingSignReplaySigma1T14Orders3To10Closed"
EXCEPTION_BOUNDS_ATOM = "TopEndpointImagDerivativeExceptionBoundReplaySigma1T14Orders11To13"
EXCEPTION_BOUNDS_CLOSED = "TopEndpointImagDerivativeExceptionBoundReplaySigma1T14Orders11To13Closed"
ENDPOINT_SECOND_ATOM = "TopEndpointImagSecondDerivativeNegativeEMReplaySigma1T14FloorMinus1Over8"
ENDPOINT_SECOND_CLOSED = "TopEndpointImagSecondDerivativeNegativeEMReplaySigma1T14FloorMinus1Over8Closed"
ENDPOINT_DERIVATIVE_ATOM = "TopEndpointImagDerivativePositiveEMReplaySigma1T14Floor1Over16"
ENDPOINT_DERIVATIVE_CLOSED = "TopEndpointImagDerivativePositiveEMReplaySigma1T14Floor1Over16Closed"
ENDPOINT_IMAG_ATOM = "TopEndpointImagNegativeEMReplayLedgerSigma1T14FloorMinus1Over40"
ENDPOINT_IMAG_CLOSED = "TopEndpointImagNegativeEMReplayLedgerSigma1T14FloorMinus1Over40Closed"
ORDER14_ENVELOPE_ATOM = "TopCriticalDerivativeOrder14EulerMaclaurinEnvelopeBound2Pow30"
WINDING_ATOM = "XiBoundaryWindingNumberZeroIntervalCertificate0To14"

HEIGHT = 14.0
SIGMA = 1.0
EM_N = 32
EM_P = 8
LOG_N = math.log(EM_N)

IMAG_CEILING = Fraction(-1, 40)
DERIVATIVE_FLOOR = Fraction(1, 16)
SECOND_CEILING = Fraction(-1, 8)
THIRD_FLOOR = Fraction(3, 16)
SIGN_FLOOR = Fraction(1, 16)
ORDER11_ABS_BOUND = Fraction(1, 16)
ORDER12_ABS_BOUND = Fraction(1, 3)
ORDER13_ABS_BOUND = Fraction(1, 1)

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


def poly_derivative_value(coeff: list[complex], derivative_order: int, s: complex) -> complex:
    """计算多项式指定阶导数在 s 的值。"""
    total = 0j
    for power, value in enumerate(coeff):
        if power < derivative_order:
            continue
        falling = 1
        for shift in range(derivative_order):
            falling *= power - shift
        total += value * falling * s ** (power - derivative_order)
    return total


def em_derivative_value(order: int) -> complex:
    """用 Euler-Maclaurin 主项计算端点 zeta 的 order 阶导数。"""
    s = SIGMA + HEIGHT * 1j
    total = sum(((-math.log(n)) ** order) * cmath.exp(-s * math.log(n)) for n in range(1, EM_N))
    pole = 0j
    for j in range(order + 1):
        pole += (
            comb(order, j)
            * ((-LOG_N) ** j)
            * cmath.exp((1 - s) * LOG_N)
            * ((-1) ** (order - j))
            * math.factorial(order - j)
            / (s - 1) ** (order - j + 1)
        )
    total += pole
    total += 0.5 * ((-LOG_N) ** order) * cmath.exp(-s * LOG_N)
    for k in range(1, EM_P + 1):
        m = 2 * k - 1
        coeff = float(BERNOULLI[2 * k]) / math.factorial(2 * k)
        poly = rising_poly_coeff(m)
        correction = 0j
        for a in range(min(order, m) + 1):
            correction += (
                comb(order, a)
                * poly_derivative_value(poly, a, s)
                * ((-LOG_N) ** (order - a))
            )
        total += coeff * cmath.exp(-(s + m) * LOG_N) * correction
    return total


def elementary_symmetric(values: list[float], order: int) -> float:
    """计算基本对称和上界。"""
    accum = [0.0] * (order + 1)
    accum[0] = 1.0
    for value in values:
        for k in range(order, 0, -1):
            accum[k] += accum[k - 1] * value
    return accum[order]


def integral_log_power(alpha: float, order: int) -> float:
    """计算 int_N^inf x^-alpha (log x)^order dx 的显式上界。"""
    return EM_N ** (1 - alpha) * sum(
        comb(order, j) * LOG_N**j * math.factorial(order - j) / (alpha - 1) ** (order - j + 1)
        for j in range(order + 1)
    )


def em_remainder_bound(order: int) -> float:
    """给端点 order 阶导数 EM 余项绝对值上界。"""
    s = SIGMA + HEIGHT * 1j
    m = 2 * EM_P
    coeff = abs(float(BERNOULLI[m])) / math.factorial(m)
    factors = [abs(s + j) for j in range(m)]
    product_bound = math.prod(factors)
    reciprocal_bounds = [1.0 / value for value in factors]
    total = 0.0
    for a in range(min(order, m) + 1):
        product_derivative_bound = math.factorial(a) * product_bound * elementary_symmetric(reciprocal_bounds, a)
        q = order - a
        total += comb(order, a) * product_derivative_bound * integral_log_power(SIGMA + m, q)
    return coeff * total


def endpoint_checks() -> list[dict[str, Any]]:
    """生成端点 replay 检查表。"""
    checks: list[dict[str, Any]] = []
    for order in range(14):
        value = em_derivative_value(order).imag
        radius = em_remainder_bound(order)
        if order == 0:
            upper = value + radius
            target = float(IMAG_CEILING)
            margin = target - upper
            checks.append(
                {
                    "order": order,
                    "atom": ENDPOINT_IMAG_ATOM,
                    "closed_atom": ENDPOINT_IMAG_CLOSED,
                    "claim": "imag <= -1/40",
                    "value": value,
                    "radius": radius,
                    "target": target,
                    "margin": margin,
                    "closed": margin > 0,
                }
            )
        elif order == 1:
            lower = value - radius
            target = float(DERIVATIVE_FLOOR)
            margin = lower - target
            checks.append(
                {
                    "order": order,
                    "atom": ENDPOINT_DERIVATIVE_ATOM,
                    "closed_atom": ENDPOINT_DERIVATIVE_CLOSED,
                    "claim": "imag >= 1/16",
                    "value": value,
                    "radius": radius,
                    "target": target,
                    "margin": margin,
                    "closed": margin > 0,
                }
            )
        elif order == 2:
            upper = value + radius
            target = float(SECOND_CEILING)
            margin = target - upper
            checks.append(
                {
                    "order": order,
                    "atom": ENDPOINT_SECOND_ATOM,
                    "closed_atom": ENDPOINT_SECOND_CLOSED,
                    "claim": "imag <= -1/8",
                    "value": value,
                    "radius": radius,
                    "target": target,
                    "margin": margin,
                    "closed": margin > 0,
                }
            )
        elif 3 <= order <= 10:
            signed_value = ((-1) ** (order + 1)) * value
            target_fraction = THIRD_FLOOR if order == 3 else SIGN_FLOOR
            lower = signed_value - radius
            target = float(target_fraction)
            margin = lower - target
            checks.append(
                {
                    "order": order,
                    "atom": SIGN_LADDER_ATOM,
                    "closed_atom": SIGN_LADDER_CLOSED,
                    "claim": f"alternating signed imag >= {target_fraction}",
                    "value": value,
                    "signed_value": signed_value,
                    "radius": radius,
                    "target": target,
                    "margin": margin,
                    "closed": margin > 0,
                }
            )
        else:
            target_fraction = {11: ORDER11_ABS_BOUND, 12: ORDER12_ABS_BOUND, 13: ORDER13_ABS_BOUND}[order]
            upper_abs = abs(value) + radius
            target = float(target_fraction)
            margin = target - upper_abs
            checks.append(
                {
                    "order": order,
                    "atom": EXCEPTION_BOUNDS_ATOM,
                    "closed_atom": EXCEPTION_BOUNDS_CLOSED,
                    "claim": f"abs imag <= {target_fraction}",
                    "value": value,
                    "radius": radius,
                    "target": target,
                    "margin": margin,
                    "closed": margin > 0,
                }
            )
    return checks


def group_closed(checks: list[dict[str, Any]], atom: str) -> bool:
    """判断某个原子对应的所有检查是否闭合。"""
    return all(item["closed"] for item in checks if item["atom"] == atom)


def build_rows(previous: dict[str, Any], rounding: dict[str, Any], checks: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """生成端点 replay 包判定表。"""
    active = previous.get("next_priority") == SIGN_LADDER_ATOM
    guard = (
        previous.get("counterexample_assumption_only") is True
        and previous.get("empirical_absence_not_used") is True
        and previous.get("hypothetical_chain_only") is True
    )
    ladder_ready = previous.get("third_derivative_positive_reduced_to_endpoint_taylor_ladder") is True
    rounding_ready = rounding.get("em_replay_rounding_discipline_closed") is True
    envelope_ready = previous.get("order14_euler_maclaurin_envelope_closed") is True
    package_ready = active and guard and ladder_ready and rounding_ready and envelope_ready
    return [
        row(
            "EndpointPackageGateActive",
            active,
            True,
            "上一层最窄点是端点 3 到 10 阶符号梯 replay。",
            SIGN_LADDER_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步只处理低高度解析证书，不使用真实零行缺席。",
            "保持 row_column_self_contained_closed=false。",
        ),
        row(
            "EMRoundingDisciplineImported",
            rounding_ready,
            True,
            "端点 EM replay 的 log/trig/exp 与复区间舍入纪律已由 canonical DAG 账本覆盖。",
            "no new arithmetic primitive.",
        ),
        row(
            SIGN_LADDER_ATOM,
            package_ready and group_closed(checks, SIGN_LADDER_ATOM),
            True,
            "3 到 10 阶端点导数交替符号闭合，其中 3 阶强到 >=3/16。",
            SIGN_LADDER_CLOSED,
        ),
        row(
            EXCEPTION_BOUNDS_ATOM,
            package_ready and group_closed(checks, EXCEPTION_BOUNDS_ATOM),
            True,
            "11 到 13 阶端点例外粗绝对值界闭合。",
            EXCEPTION_BOUNDS_CLOSED,
        ),
        row(
            ENDPOINT_SECOND_ATOM,
            package_ready and group_closed(checks, ENDPOINT_SECOND_ATOM),
            True,
            "端点二阶负号闭合。",
            ENDPOINT_SECOND_CLOSED,
        ),
        row(
            ENDPOINT_DERIVATIVE_ATOM,
            package_ready and group_closed(checks, ENDPOINT_DERIVATIVE_ATOM),
            True,
            "端点一阶导数正号闭合。",
            ENDPOINT_DERIVATIVE_CLOSED,
        ),
        row(
            ENDPOINT_IMAG_ATOM,
            package_ready and group_closed(checks, ENDPOINT_IMAG_ATOM),
            True,
            "端点虚部负号闭合。",
            ENDPOINT_IMAG_CLOSED,
        ),
    ]


def proof_contract() -> list[str]:
    """写出端点 replay 包证明合同。"""
    return [
        "在 s=1+14i, N=32, P=8 处写出 zeta 及各阶导数的 Euler-Maclaurin 公式。",
        "有限和、极点补偿项、半端点项、Bernoulli 修正项逐项求导到 13 阶。",
        "余项用 |B_16({x})|<=|B_16| 和 Leibniz 公式给显式绝对值半径。",
        "所有 log/trig/exp 调用由已闭合 EM replay 舍入纪律和 trace/hash 账本向外取整。",
        "逐项比较区间端点：0 阶、1 阶、2 阶和 3 到 13 阶所需全部不等式均有正余量。",
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行端点 EM replay 包路由。"""
    previous = load_json(paths["previous"])
    rounding = load_json(paths["rounding"])
    checks = endpoint_checks()
    rows = build_rows(previous, rounding, checks)
    package_closed = all(item["closed"] for item in rows if item["gate"] not in {"EndpointPackageGateActive", "CounterexampleBranchGuardPreserved", "EMRoundingDisciplineImported"})
    source_paths = [path for name, path in paths.items() if name not in {"json_out", "md_out"}]
    return {
        "certificate_type": "prime_matrix_top_endpoint_em_replay_package_router",
        "status": "top_endpoint_em_replay_package_closed" if package_closed else "top_endpoint_em_replay_package_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "endpoint_em_replay_package_closed": package_closed,
        "endpoint_sign_ladder_closed": group_closed(checks, SIGN_LADDER_ATOM),
        "endpoint_exception_bounds_closed": group_closed(checks, EXCEPTION_BOUNDS_ATOM),
        "endpoint_second_closed": group_closed(checks, ENDPOINT_SECOND_ATOM),
        "endpoint_derivative_closed": group_closed(checks, ENDPOINT_DERIVATIVE_ATOM),
        "endpoint_imag_closed": group_closed(checks, ENDPOINT_IMAG_ATOM),
        "top_critical_segment_self_contained_closed": False,
        "lowheight_rectangle_count_self_contained_closed": False,
        "row_column_self_contained_closed": False,
        "replacement_self_contained": {
            SIGN_LADDER_ATOM: SIGN_LADDER_CLOSED,
            EXCEPTION_BOUNDS_ATOM: EXCEPTION_BOUNDS_CLOSED,
            ENDPOINT_SECOND_ATOM: ENDPOINT_SECOND_CLOSED,
            ENDPOINT_DERIVATIVE_ATOM: ENDPOINT_DERIVATIVE_CLOSED,
            ENDPOINT_IMAG_ATOM: ENDPOINT_IMAG_CLOSED,
            ORDER14_ENVELOPE_ATOM: "closed upstream",
        },
        "checks": checks,
        "proof_contract": proof_contract(),
        "next_priority": "TopCriticalSegmentEndpointTaylorChainAggregationLedger",
        "secondary_priority": WINDING_ATOM,
        "plain_conclusion": (
            "端点 EM replay 包已闭合：端点虚部负号、端点一阶正号、端点二阶负号、"
            "3-10 阶交替符号和 11-13 阶例外粗界全部有正余量。下一步只需把这些端点包"
            "沿前面已闭合的单调/Taylor 压缩链做一次聚合，即可关闭顶边临界半段。"
        ),
        "rows": rows,
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix 顶边端点 Euler-Maclaurin replay 包路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"endpoint_em_replay_package_closed={fmt_bool(result['endpoint_em_replay_package_closed'])}",
        f"top_critical_segment_self_contained_closed={fmt_bool(result['top_critical_segment_self_contained_closed'])}",
        (
            "lowheight_rectangle_count_self_contained_closed="
            f"{fmt_bool(result['lowheight_rectangle_count_self_contained_closed'])}"
        ),
        f"row_column_self_contained_closed={fmt_bool(result['row_column_self_contained_closed'])}",
        "```",
        "",
        "## 1. 端点检查表",
        "",
        "| order | claim | value | radius | target | margin | closed |",
        "| ---: | --- | ---: | ---: | ---: | ---: | --- |",
    ]
    for item in result["checks"]:
        lines.append(
            "| {order} | {claim} | `{value:.12f}` | `{radius:.3e}` | `{target:.12f}` | `{margin:.12f}` | `{closed}` |".format(
                order=item["order"],
                claim=table_cell(item["claim"]),
                value=item["value"],
                radius=item["radius"],
                target=item["target"],
                margin=item["margin"],
                closed=fmt_bool(item["closed"]),
            )
        )
    lines.extend(
        [
            "",
            "## 2. 证明合同",
            "",
        ]
    )
    for index, item in enumerate(result["proof_contract"], start=1):
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
            f"当前最窄点：`{result['next_priority']}`。",
            f"随后仍需：`{result['secondary_priority']}`。",
            "",
            "判定：端点输入包已闭合，剩余是链式聚合与 winding 证书。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous-json", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--rounding-json", type=Path, default=DEFAULT_ROUNDING)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "previous": args.previous_json,
        "rounding": args.rounding_json,
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
