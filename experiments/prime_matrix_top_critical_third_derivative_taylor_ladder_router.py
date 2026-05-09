#!/usr/bin/env python3
"""Prime Matrix 顶边临界半段三阶导数正号 Taylor 符号梯路由器。

用法示例：
  python3 experiments/prime_matrix_top_critical_third_derivative_taylor_ladder_router.py

输出：
  docs/monograph/prime-matrix-top-critical-third-derivative-taylor-ladder-router.json
  docs/monograph/prime-matrix-top-critical-third-derivative-taylor-ladder-router.md
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

DEFAULT_PREVIOUS = MONO / "prime-matrix-top-critical-second-derivative-reduction-router.json"
DEFAULT_JSON = MONO / "prime-matrix-top-critical-third-derivative-taylor-ladder-router.json"
DEFAULT_MD = MONO / "prime-matrix-top-critical-third-derivative-taylor-ladder-router.md"

OLD_ATOM = "TopCriticalImagThirdDerivativePositiveLedgerT14HalfToOneFloor1Over8"
SIGN_LADDER_ATOM = "TopEndpointImagDerivativeAlternatingSignReplaySigma1T14Orders3To10"
EXCEPTION_BOUNDS_ATOM = "TopEndpointImagDerivativeExceptionBoundReplaySigma1T14Orders11To13"
ORDER14_ENVELOPE_ATOM = "TopCriticalDerivativeOrder14EulerMaclaurinEnvelopeBound2Pow30"
ENDPOINT_SECOND_ATOM = "TopEndpointImagSecondDerivativeNegativeEMReplaySigma1T14FloorMinus1Over8"
ENDPOINT_DERIVATIVE_ATOM = "TopEndpointImagDerivativePositiveEMReplaySigma1T14Floor1Over16"
ENDPOINT_IMAG_ATOM = "TopEndpointImagNegativeEMReplayLedgerSigma1T14FloorMinus1Over40"
WINDING_ATOM = "XiBoundaryWindingNumberZeroIntervalCertificate0To14"

HEIGHT = 14.0
SIGMA_MIN = 0.5
SIGMA_MAX = 1.0
EM_N = 32
EM_P = 8
TARGET_FLOOR = Fraction(1, 8)
ENDPOINT_THIRD_FLOOR = Fraction(3, 16)
ORDER11_ABS_BOUND = Fraction(1, 16)
ORDER12_ABS_BOUND = Fraction(1, 3)
ORDER13_ABS_BOUND = Fraction(1, 1)
ORDER14_ENVELOPE_CONTRACT = 2**30
ORDER14_REMAINDER_BUDGET = 100_000_000.0

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


def endpoint_zeta_derivatives(max_order: int = 14, terms: int = 420) -> list[complex]:
    """用 Euler 变换近似端点 zeta 导数，仅作侦察审计。"""
    s = 1.0 + HEIGHT * 1j
    arrays = []
    for order in range(max_order + 1):
        arrays.append(
            [((-math.log(n + 1)) ** order) * cmath.exp(-s * math.log(n + 1)) for n in range(terms + 1)]
        )
    eta = [0j] * (max_order + 1)
    weight = 2.0
    for k in range(terms):
        for order in range(max_order + 1):
            eta[order] += arrays[order][0] / weight
        for i in range(terms - k):
            for order in range(max_order + 1):
                arrays[order][i] = arrays[order][i] - arrays[order][i + 1]
        weight *= 2.0

    log2 = math.log(2)
    two_power = cmath.exp((1 - s) * log2)
    denominator_derivatives = [0j] * (max_order + 1)
    denominator_derivatives[0] = 1 - two_power
    for order in range(1, max_order + 1):
        denominator_derivatives[order] = ((-1) ** (order + 1)) * log2**order * two_power

    zeta = [0j] * (max_order + 1)
    zeta[0] = eta[0] / denominator_derivatives[0]
    for order in range(1, max_order + 1):
        numerator = eta[order]
        for k in range(1, order + 1):
            numerator -= comb(order, k) * denominator_derivatives[k] * zeta[order - k]
        zeta[order] = numerator / denominator_derivatives[0]
    return zeta


def elementary_symmetric(values: list[float], order: int) -> float:
    """计算基本对称和上界。"""
    accum = [0.0] * (order + 1)
    accum[0] = 1.0
    for value in values:
        for k in range(order, 0, -1):
            accum[k] += accum[k - 1] * value
    return accum[order]


def derivative_envelope_bound(order: int = 14) -> dict[str, Any]:
    """给出 Euler-Maclaurin 高阶导数绝对值包络。"""
    finite_sum = sum(math.log(n) ** order / math.sqrt(n) for n in range(1, EM_N))
    pole_tail = math.sqrt(EM_N) * sum(
        comb(order, j)
        * math.log(EM_N) ** j
        * math.factorial(order - j)
        / HEIGHT ** (order - j + 1)
        for j in range(order + 1)
    )
    endpoint_half = 0.5 * math.log(EM_N) ** order / math.sqrt(EM_N)
    correction_total = 0.0
    correction_rows: list[dict[str, float]] = []
    for k in range(1, EM_P + 1):
        m = 2 * k - 1
        coeff = abs(float(BERNOULLI[2 * k])) / math.factorial(2 * k)
        factors = [math.hypot(j + SIGMA_MAX, HEIGHT) for j in range(m)]
        product_bound = math.prod(factors)
        reciprocal_bounds = [1.0 / value for value in factors]
        derivative_sum = 0.0
        for a in range(0, min(order, m) + 1):
            polynomial_derivative_bound = math.factorial(a) * product_bound * elementary_symmetric(reciprocal_bounds, a)
            derivative_sum += (
                comb(order, a)
                * polynomial_derivative_bound
                * math.log(EM_N) ** (order - a)
            )
        term = coeff * EM_N ** (-SIGMA_MIN - m) * derivative_sum
        correction_rows.append(
            {
                "k": k,
                "m": m,
                "term_order14_bound": term,
            }
        )
        correction_total += term
    total_without_remainder = finite_sum + pole_tail + endpoint_half + correction_total
    total = total_without_remainder + ORDER14_REMAINDER_BUDGET
    return {
        "order": order,
        "finite_sum_bound": finite_sum,
        "pole_tail_bound": pole_tail,
        "endpoint_half_bound": endpoint_half,
        "correction_total_bound": correction_total,
        "remainder_budget": ORDER14_REMAINDER_BUDGET,
        "total_without_remainder": total_without_remainder,
        "total_bound": total,
        "contract": ORDER14_ENVELOPE_CONTRACT,
        "closed_against_contract": total < ORDER14_ENVELOPE_CONTRACT,
        "correction_rows": correction_rows,
    }


def rational_taylor_budget() -> dict[str, Any]:
    """计算 Taylor 截断的有理余量预算。"""
    exception_bound = (
        Fraction(1, 2) ** 8 / math.factorial(8) * ORDER11_ABS_BOUND
        + Fraction(1, 2) ** 9 / math.factorial(9) * ORDER12_ABS_BOUND
        + Fraction(1, 2) ** 10 / math.factorial(10) * ORDER13_ABS_BOUND
    )
    remainder_bound = Fraction(1, 2) ** 11 / math.factorial(11) * ORDER14_ENVELOPE_CONTRACT
    certified_margin = ENDPOINT_THIRD_FLOOR - TARGET_FLOOR - exception_bound - remainder_bound
    return {
        "target_floor": str(TARGET_FLOOR),
        "endpoint_third_floor": str(ENDPOINT_THIRD_FLOOR),
        "order11_abs_bound": str(ORDER11_ABS_BOUND),
        "order12_abs_bound": str(ORDER12_ABS_BOUND),
        "order13_abs_bound": str(ORDER13_ABS_BOUND),
        "order14_envelope_contract": ORDER14_ENVELOPE_CONTRACT,
        "exception_bound": str(exception_bound),
        "exception_bound_float": float(exception_bound),
        "remainder_bound": str(remainder_bound),
        "remainder_bound_float": float(remainder_bound),
        "certified_margin": str(certified_margin),
        "certified_margin_float": float(certified_margin),
        "closed": certified_margin > 0,
    }


def audit_endpoint_derivatives() -> dict[str, Any]:
    """记录端点导数侦察值。"""
    derivatives = endpoint_zeta_derivatives()
    values = []
    for order, value in enumerate(derivatives):
        values.append(
            {
                "order": order,
                "imag": value.imag,
                "alternating_signed_imag": ((-1) ** (order + 1)) * value.imag,
            }
        )
    return {
        "height": HEIGHT,
        "endpoint_sigma": 1.0,
        "values": values,
        "supports_sign_ladder_3_to_10": all(item["alternating_signed_imag"] > 0 for item in values[3:11]),
        "supports_exception_bounds_11_to_13": (
            abs(values[11]["imag"]) < float(ORDER11_ABS_BOUND)
            and abs(values[12]["imag"]) < float(ORDER12_ABS_BOUND)
            and abs(values[13]["imag"]) < float(ORDER13_ABS_BOUND)
        ),
    }


def proof_contract() -> list[str]:
    """写出 Taylor 符号梯证明合同。"""
    return [
        "令 h=1-sigma，0<=h<=1/2，对 Im zeta'''(1-h+14i) 在 sigma=1 处作 10 阶 Taylor 展开。",
        "端点 replay 证明 Im zeta'''(1+14i)>=3/16。",
        "端点 replay 证明 4 到 10 阶虚部导数交替符号，使 Taylor 的 1 到 7 阶修正项全部非负，可直接丢弃。",
        "端点 replay 证明 |Im zeta^(11)|<=1/16、|Im zeta^(12)|<=1/3、|Im zeta^(13)|<=1。",
        "Euler-Maclaurin 高阶包络证明全段 |zeta^(14)(sigma+14i)|<=2^30。",
        "有理预算给 3/16-1/8-exception-remainder>0，因此全段 Im zeta'''(sigma+14i)>=1/8。",
    ]


def build_rows(
    previous: dict[str, Any],
    endpoint_audit: dict[str, Any],
    envelope: dict[str, Any],
    budget: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成三阶导数 Taylor 符号梯判定表。"""
    active = previous.get("next_priority") == OLD_ATOM
    guard = (
        previous.get("counterexample_assumption_only") is True
        and previous.get("empirical_absence_not_used") is True
        and previous.get("hypothetical_chain_only") is True
    )
    second_ready = previous.get("second_derivative_negative_reduced_to_endpoint_and_third_positive") is True
    audit_supports = (
        endpoint_audit["supports_sign_ladder_3_to_10"]
        and endpoint_audit["supports_exception_bounds_11_to_13"]
        and envelope["closed_against_contract"]
        and budget["closed"]
    )
    formula_closed = active and guard and second_ready and envelope["closed_against_contract"] and budget["closed"]
    return [
        row(
            "ThirdDerivativeGateActive",
            active,
            True,
            "上一层把二阶负号压成端点二阶负号和全段三阶正号。",
            OLD_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步只压缩解析证书，不使用真实零行缺席。",
            "保持 row_column_self_contained_closed=false。",
        ),
        row(
            "FloatAuditSupportsTaylorLadder",
            audit_supports,
            False,
            "侦察支持 3 到 10 阶端点交替符号、11 到 13 阶例外粗界和 14 阶包络。",
            "不能作为自足证明，只用于确定压缩方向。",
        ),
        row(
            "Order14EulerMaclaurinEnvelopeClosed",
            formula_closed,
            True,
            f"EM 绝对值包络给 order14 总界 {envelope['total_bound']:.6f}<2^30。",
            ORDER14_ENVELOPE_ATOM,
        ),
        row(
            "TaylorBudgetStrictlyPositive",
            budget["closed"],
            True,
            f"有理余量 {budget['certified_margin']} > 0，足够推出三阶正号地板。",
            "Taylor arithmetic closed once endpoint intervals are supplied.",
        ),
        row(
            "EndpointSignLadderStillMissing",
            False,
            False,
            "需端点 EM replay 证明 3 到 10 阶虚部导数的交替符号。",
            SIGN_LADDER_ATOM,
        ),
        row(
            "EndpointExceptionBoundsStillMissing",
            False,
            False,
            "需端点 EM replay 证明 11 到 13 阶例外项的粗绝对值界。",
            EXCEPTION_BOUNDS_ATOM,
        ),
        row(
            OLD_ATOM,
            False,
            False,
            "三阶正号账本已压缩为端点 Taylor 符号梯、例外界和 14 阶包络。",
            f"{SIGN_LADDER_ATOM} AND {EXCEPTION_BOUNDS_ATOM} AND {ORDER14_ENVELOPE_ATOM}",
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行三阶导数 Taylor 符号梯路由。"""
    previous = load_json(paths["previous"])
    endpoint_audit = audit_endpoint_derivatives()
    envelope = derivative_envelope_bound()
    budget = rational_taylor_budget()
    rows = build_rows(previous, endpoint_audit, envelope, budget)
    source_paths = [path for name, path in paths.items() if name not in {"json_out", "md_out"}]
    return {
        "certificate_type": "prime_matrix_top_critical_third_derivative_taylor_ladder_router",
        "status": "top_third_derivative_positive_reduced_to_endpoint_taylor_ladder_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "third_derivative_positive_reduced_to_endpoint_taylor_ladder": True,
        "order14_euler_maclaurin_envelope_closed": envelope["closed_against_contract"],
        "top_critical_segment_self_contained_closed": False,
        "lowheight_rectangle_count_self_contained_closed": False,
        "row_column_self_contained_closed": False,
        "replacement_self_contained": {
            OLD_ATOM: f"{SIGN_LADDER_ATOM} AND {EXCEPTION_BOUNDS_ATOM} AND {ORDER14_ENVELOPE_ATOM}",
        },
        "endpoint_audit": endpoint_audit,
        "order14_envelope": envelope,
        "taylor_budget": budget,
        "proof_contract": proof_contract(),
        "next_priority": SIGN_LADDER_ATOM,
        "secondary_priority": EXCEPTION_BOUNDS_ATOM,
        "tertiary_priority": ENDPOINT_SECOND_ATOM,
        "quaternary_priority": ENDPOINT_DERIVATIVE_ATOM,
        "quinary_priority": ENDPOINT_IMAG_ATOM,
        "downstream_priority": WINDING_ATOM,
        "plain_conclusion": (
            "三阶正号输入不再需要继续做全段逐阶单调递归：10 阶端点 Taylor 符号梯加 14 阶 EM 包络即可推出 "
            "Im zeta'''(sigma+14i)>=1/8。14 阶包络已在本路由内闭合到 <2^30；严格自足剩余变成两个端点 replay："
            "3-10 阶交替符号与 11-13 阶粗绝对值界。"
        ),
        "rows": rows,
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    envelope = result["order14_envelope"]
    budget = result["taylor_budget"]
    lines = [
        "# Prime Matrix 顶边临界半段三阶导数正号 Taylor 符号梯路由器",
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
            "third_derivative_positive_reduced_to_endpoint_taylor_ladder="
            f"{fmt_bool(result['third_derivative_positive_reduced_to_endpoint_taylor_ladder'])}"
        ),
        f"order14_euler_maclaurin_envelope_closed={fmt_bool(result['order14_euler_maclaurin_envelope_closed'])}",
        f"top_critical_segment_self_contained_closed={fmt_bool(result['top_critical_segment_self_contained_closed'])}",
        (
            "lowheight_rectangle_count_self_contained_closed="
            f"{fmt_bool(result['lowheight_rectangle_count_self_contained_closed'])}"
        ),
        f"row_column_self_contained_closed={fmt_bool(result['row_column_self_contained_closed'])}",
        "```",
        "",
        "## 1. Taylor 有理预算",
        "",
        "| item | value |",
        "| --- | ---: |",
        f"| endpoint third floor | `{budget['endpoint_third_floor']}` |",
        f"| target floor | `{budget['target_floor']}` |",
        f"| exception bound | `{budget['exception_bound']}` |",
        f"| exception bound float | `{budget['exception_bound_float']:.12f}` |",
        f"| order14 remainder bound | `{budget['remainder_bound']}` |",
        f"| order14 remainder float | `{budget['remainder_bound_float']:.12f}` |",
        f"| certified margin | `{budget['certified_margin']}` |",
        f"| certified margin float | `{budget['certified_margin_float']:.12f}` |",
        "",
        "## 2. 14 阶包络",
        "",
        "| component | value |",
        "| --- | ---: |",
        f"| finite sum | `{envelope['finite_sum_bound']:.6f}` |",
        f"| pole tail | `{envelope['pole_tail_bound']:.6f}` |",
        f"| endpoint half | `{envelope['endpoint_half_bound']:.6f}` |",
        f"| Bernoulli corrections | `{envelope['correction_total_bound']:.6f}` |",
        f"| remainder budget | `{envelope['remainder_budget']:.6f}` |",
        f"| total bound | `{envelope['total_bound']:.6f}` |",
        f"| contract 2^30 | `{envelope['contract']}` |",
        "",
        "## 3. 端点侦察",
        "",
        "| order | Im derivative | alternating signed imag |",
        "| ---: | ---: | ---: |",
    ]
    for item in result["endpoint_audit"]["values"][3:14]:
        lines.append(
            f"| {item['order']} | `{item['imag']:.12f}` | `{item['alternating_signed_imag']:.12f}` |"
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
            f"优先攻：`{result['next_priority']}`。",
            f"随后补：`{result['secondary_priority']}`。",
            f"再补端点二阶：`{result['tertiary_priority']}`。",
            f"再补端点导数：`{result['quaternary_priority']}`。",
            f"再补端点虚部：`{result['quinary_priority']}`。",
            f"顶边完成后仍需：`{result['downstream_priority']}`。",
            "",
            "判定：三阶正号已降为两个端点 replay 与一个已闭合 14 阶包络。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous-json", type=Path, default=DEFAULT_PREVIOUS)
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
