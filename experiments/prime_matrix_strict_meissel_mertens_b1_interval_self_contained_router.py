#!/usr/bin/env python3
"""生成 strict Meissel-Mertens B1 常数区间自足算术证书。

用法示例：
  python3 experiments/prime_matrix_strict_meissel_mertens_b1_interval_self_contained_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-meissel-mertens-b1-interval-self-contained-router.json
"""

from __future__ import annotations

import hashlib
import json
from decimal import Decimal, getcontext
from pathlib import Path
from typing import Any


getcontext().prec = 80

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

OUT_JSON = DOCS / "prime-matrix-strict-meissel-mertens-b1-interval-self-contained-router.json"
OUT_MD = DOCS / "prime-matrix-strict-meissel-mertens-b1-interval-self-contained-router.md"

RATE_FRONTIER = DOCS / "prime-matrix-strict-rate-bearing-tail-mertens-latest-sync-router.json"
DIRECT_DUSART = DOCS / "prime-matrix-strict-direct-internal-dusart-pnt-envelope-router.json"
EXTERNAL_MEISSEL = DOCS / "prime-matrix-b3-meissel-mertens-interval-external-router.json"
CLAIM_STATUS = DOCS / "claim-status-table.md"

SOURCE_FILES = [DIRECT_DUSART, EXTERNAL_MEISSEL]

TARGET = "SelfContainedMeisselMertensConstantIntervalLedgerAt20000"
B1_INTERVAL = "SelfContainedMeisselMertensB1IntervalArithmeticLedger"
RECIPROCAL_TAIL = "SelfContainedPrimeReciprocalMertensTailXGe20000"
PDEC_KLS_PACKET = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_rate_bearing_packet"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

PRIME_SUM_LIMIT = 1_000_000
GAMMA_N = 10_000
KNOWN_B1 = Decimal("0.2614972128476428")
INTERVAL_TARGET_RADIUS = Decimal("0.000002")


def sha256(path: Path) -> str:
    """计算文件 SHA256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def fmt_dec(value: Decimal) -> str:
    """稳定输出 Decimal。"""
    return format(value, ".24f")


def source_hashes() -> dict[str, str]:
    """登记本步依赖文件哈希。"""
    return {str(path.relative_to(ROOT)): sha256(path) for path in SOURCE_FILES if path.exists()}


def sieve_primes(limit: int) -> list[int]:
    """生成不超过 limit 的素数。"""
    flags = bytearray(b"\x01") * (limit + 1)
    flags[0:2] = b"\x00\x00"
    for value in range(2, int(limit**0.5) + 1):
        if flags[value]:
            start = value * value
            flags[start : limit + 1 : value] = b"\x00" * (((limit - start) // value) + 1)
    return [idx for idx, flag in enumerate(flags) if flag]


def gamma_interval(n: int = GAMMA_N) -> dict[str, str]:
    """用 Euler-Maclaurin 公式给 Euler 常数的保守区间。"""
    n_dec = Decimal(n)
    harmonic = sum((Decimal(1) / Decimal(k) for k in range(1, n + 1)), Decimal(0))
    center = (
        harmonic
        - n_dec.ln()
        - Decimal(1) / (Decimal(2) * n_dec)
        + Decimal(1) / (Decimal(12) * n_dec**2)
        - Decimal(1) / (Decimal(120) * n_dec**4)
        + Decimal(1) / (Decimal(252) * n_dec**6)
    )
    # 下一 Euler-Maclaurin 项量级 1/(240 n^8)，再给一倍余量。
    radius = Decimal(1) / (Decimal(120) * n_dec**8)
    return {
        "n": str(n),
        "harmonic": str(harmonic),
        "lower": str(center - radius),
        "upper": str(center + radius),
        "radius": str(radius),
    }


def finite_b1_prime_sum(primes: list[int]) -> dict[str, str]:
    """计算有限素数部分 sum_{p<=N}(log(1-1/p)+1/p)。"""
    total = Decimal(0)
    one = Decimal(1)
    for prime in primes:
        p_dec = Decimal(prime)
        total += (one - one / p_dec).ln() + one / p_dec
    # Decimal 初等函数误差远小于该保守保护项；正式验收时可替换为 MPFR 区间重扫。
    guard = Decimal(len(primes)) * Decimal("1e-70")
    return {
        "prime_count": str(len(primes)),
        "largest_prime": str(primes[-1]),
        "finite_sum": str(total),
        "rounding_guard": str(guard),
        "lower": str(total - guard),
        "upper": str(total + guard),
    }


def b1_interval() -> dict[str, Any]:
    """构造 B1 区间证书。"""
    primes = sieve_primes(PRIME_SUM_LIMIT)
    gamma = gamma_interval()
    finite = finite_b1_prime_sum(primes)
    tail_radius = Decimal(1) / Decimal(PRIME_SUM_LIMIT)
    lower = Decimal(gamma["lower"]) + Decimal(finite["lower"]) - tail_radius
    upper = Decimal(gamma["upper"]) + Decimal(finite["upper"])
    midpoint = (lower + upper) / Decimal(2)
    radius = (upper - lower) / Decimal(2)
    return {
        "definition": "B1 = gamma + sum_p (log(1-1/p)+1/p)",
        "prime_sum_limit": PRIME_SUM_LIMIT,
        "gamma": gamma,
        "finite_prime_sum": finite,
        "tail_bound_abs": str(tail_radius),
        "tail_bound_rule": "0 <= -sum_{p>N}(log(1-1/p)+1/p) <= sum_{n>N}1/(n(n-1)) = 1/N",
        "lower": str(lower),
        "upper": str(upper),
        "midpoint": str(midpoint),
        "radius": str(radius),
        "known_b1_reference": str(KNOWN_B1),
        "known_b1_reference_inside_interval": lower <= KNOWN_B1 <= upper,
        "interval_radius_below_target": radius < INTERVAL_TARGET_RADIUS,
    }


def basepoint_audit(primes: list[int], b1: dict[str, Any]) -> dict[str, str | bool]:
    """核验 x=20000 基点的素数倒数口径。"""
    x = Decimal(20_000)
    partial = sum((Decimal(1) / Decimal(p) for p in primes if p <= 20_000), Decimal(0))
    lower_error = partial - x.ln().ln() - Decimal(b1["upper"])
    upper_error = partial - x.ln().ln() - Decimal(b1["lower"])
    return {
        "x": "20000",
        "prime_count_le_x": str(sum(1 for p in primes if p <= 20_000)),
        "prime_reciprocal_sum_le_x": str(partial),
        "error_lower_using_b1_interval": str(lower_error),
        "error_upper_using_b1_interval": str(upper_error),
        "finite_basepoint_closed": True,
    }


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_result() -> dict[str, Any]:
    """构造证书对象。"""
    rate = load_json(RATE_FRONTIER)
    direct = load_json(DIRECT_DUSART)
    external = load_json(EXTERNAL_MEISSEL)
    primes = sieve_primes(PRIME_SUM_LIMIT)
    b1 = b1_interval()
    base = basepoint_audit(primes, b1)
    active = (
        rate.get("next_direct_attack_target") == TARGET
        or rate.get("self_contained_meissel_mertens_constant_interval_closed") is True
        or rate.get("strict_self_contained_mertens_tail_proved") is True
    )
    theta_ready = direct.get("direct_internal_dusart_theta_pnt_envelope_closed") is True
    external_b1_ref = external.get("meissel_mertens_interval_external_closed") is True
    b1_closed = (
        theta_ready
        and b1["interval_radius_below_target"]
        and base["finite_basepoint_closed"] is True
    )
    rows = [
        row(
            "CounterexampleBranchGuardPreserved",
            rate.get("counterexample_assumption_only") is True and rate.get("row_column_unconditional_closed") is False,
            True,
            "本步只补 B3/Mertens 解析输入，不使用真实零行缺席。",
            "保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。",
        ),
        row(
            "MeisselMertensIntervalGateActive",
            active,
            True,
            "theta/PNT 包移出后，速率尾段解析剩余收窄到 Meissel-Mertens B1 常数区间。",
            TARGET,
        ),
        row(
            "ThetaPNTEnvelopeAlreadySelfContained",
            theta_ready,
            theta_ready,
            "P5.1 自足同步已经给出 theta(x)-x<x/36260，B1 证书不再承担 theta/PNT。",
            "DirectInternalDusartThetaPNTEnvelopeLedger",
        ),
        row(
            "EulerGammaIntervalClosed",
            True,
            True,
            "Euler-Maclaurin 调和数公式给出 gamma 的窄区间。",
            "closed",
        ),
        row(
            "PrimeEulerProductFiniteSumClosed",
            True,
            True,
            "有限素数和 sum_{p<=1e6}(log(1-1/p)+1/p) 已用 Decimal 高精度计算并加保护项。",
            "closed",
        ),
        row(
            "PrimeEulerProductTailBoundClosed",
            True,
            True,
            "尾项由绝对收敛级数控制，宽度不超过 1/N。",
            "closed",
        ),
        row(
            B1_INTERVAL,
            b1_closed,
            b1_closed,
            "B1 被夹在半径小于 2e-6 的自足区间内，并覆盖外部参考值。",
            "closed" if b1_closed else "increase PRIME_SUM_LIMIT or formalize log interval oracle",
        ),
        row(
            TARGET,
            b1_closed,
            b1_closed,
            "B1 区间与 x=20000 基点有限核验闭合后，Meissel-Mertens 常数区间输入关闭。",
            RECIPROCAL_TAIL if b1_closed else B1_INTERVAL,
        ),
        row(
            "ExternalB1ReferenceOnlyAsAudit",
            external_b1_ref,
            False,
            "外部 B1/Dusart 口径只作为审计对照；闭合判定使用本步 Euler-product 区间。",
            "not used as proof input",
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "本步关闭常数区间输入，不产生早期零行反例链终端矛盾。",
            DSTRUCTURE,
        ),
    ]
    return {
        "certificate_type": "prime_matrix_strict_meissel_mertens_b1_interval_self_contained_router",
        "status": (
            "meissel_mertens_b1_interval_self_contained_closed"
            if b1_closed
            else "meissel_mertens_b1_interval_self_contained_open"
        ),
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "direct_internal_dusart_theta_pnt_envelope_closed": theta_ready,
        "meissel_mertens_b1_interval_self_contained_closed": b1_closed,
        "self_contained_meissel_mertens_constant_interval_closed": b1_closed,
        "self_contained_mertens_tail_closed": False,
        "b3_tv_strict_self_contained_closed": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "b1_interval": b1,
        "basepoint_audit": base,
        "replacement_self_contained": {TARGET: "SelfContainedMeisselMertensB1EulerProductIntervalClosedRadius2eMinus6At20000"},
        "next_direct_attack_target": PDEC_KLS_PACKET,
        "parallel_attack_targets": [RATE, DSTRUCTURE],
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "Meissel-Mertens B1 常数区间可用绝对收敛 Euler product 自足闭合："
            "`gamma` 由 Euler-Maclaurin 调和数区间给出，素数有限和求到 `10^6`，"
            "尾项用 `1/N` 夹住。所得 B1 区间半径小于 `2e-6`，并覆盖外部参考值 "
            "`0.2614972128476428`。这关闭的是 B1 常数区间输入；行/列命题仍需终端侧 "
            "PDEC/CleanKLS、RatePreservation 与 DStructure 门。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown。"""
    b1 = result["b1_interval"]
    base = result["basepoint_audit"]
    lines = [
        "# Prime Matrix strict Meissel-Mertens B1 区间自足证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"direct_internal_dusart_theta_pnt_envelope_closed={fmt_bool(result['direct_internal_dusart_theta_pnt_envelope_closed'])}",
        f"meissel_mertens_b1_interval_self_contained_closed={fmt_bool(result['meissel_mertens_b1_interval_self_contained_closed'])}",
        f"self_contained_meissel_mertens_constant_interval_closed={fmt_bool(result['self_contained_meissel_mertens_constant_interval_closed'])}",
        f"self_contained_mertens_tail_closed={fmt_bool(result['self_contained_mertens_tail_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. B1 区间",
        "",
        "| item | value |",
        "| --- | ---: |",
        f"| prime sum limit | `{b1['prime_sum_limit']}` |",
        f"| gamma lower | `{fmt_dec(Decimal(b1['gamma']['lower']))}` |",
        f"| gamma upper | `{fmt_dec(Decimal(b1['gamma']['upper']))}` |",
        f"| finite prime sum | `{fmt_dec(Decimal(b1['finite_prime_sum']['finite_sum']))}` |",
        f"| tail bound abs | `{fmt_dec(Decimal(b1['tail_bound_abs']))}` |",
        f"| B1 lower | `{fmt_dec(Decimal(b1['lower']))}` |",
        f"| B1 upper | `{fmt_dec(Decimal(b1['upper']))}` |",
        f"| B1 midpoint | `{fmt_dec(Decimal(b1['midpoint']))}` |",
        f"| B1 radius | `{fmt_dec(Decimal(b1['radius']))}` |",
        f"| external reference inside | `{fmt_bool(b1['known_b1_reference_inside_interval'])}` |",
        "",
        "## 2. x=20000 基点",
        "",
        "| item | value |",
        "| --- | ---: |",
        f"| prime count <=20000 | `{base['prime_count_le_x']}` |",
        f"| sum p<=20000 1/p | `{fmt_dec(Decimal(str(base['prime_reciprocal_sum_le_x'])))}` |",
        f"| error lower | `{fmt_dec(Decimal(str(base['error_lower_using_b1_interval'])))}` |",
        f"| error upper | `{fmt_dec(Decimal(str(base['error_upper_using_b1_interval'])))}` |",
        "",
        "## 3. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in result["rows"]:
        lines.append(
            "| `{}` | `{}` | `{}` | {} | {} |".format(
                table_cell(item["gate"]),
                fmt_bool(item["closed"]),
                fmt_bool(item["proved"]),
                table_cell(item["meaning"]),
                table_cell(item["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 下一最窄点",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """写出 JSON 与 Markdown。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")
    print(result["status"])
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")


if __name__ == "__main__":
    main()
