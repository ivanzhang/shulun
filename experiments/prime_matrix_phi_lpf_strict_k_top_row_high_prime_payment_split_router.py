#!/usr/bin/env python3
"""生成 strict 顶行 high-prime payment 分裂证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_strict_k_top_row_high_prime_payment_split_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-strict-k-top-row-high-prime-payment-split-router.json

输出：
  data/prime-matrix-phi-lpf-strict-k-top-row-high-prime-payment-split-ledger.json
  docs/monograph/prime-matrix-phi-lpf-strict-k-top-row-high-prime-payment-split-router.json
  docs/monograph/prime-matrix-phi-lpf-strict-k-top-row-high-prime-payment-split-router.md
"""

from __future__ import annotations

import hashlib
import json
from array import array
from math import isqrt
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-strict-k-top-row-high-prime-payment-split"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

DEPENDENCIES = [
    DOCS / "prime-matrix-phi-lpf-strict-k-top-row-square-collar-router.json",
    DOCS / "prime-matrix-phi-lpf-strict-k-top-row-perfect-tiling-router.json",
]


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """把布尔值格式化成小写文本。"""
    return "true" if bool(value) else "false"


def cell(value: Any) -> str:
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


def prime_sieve(n: int) -> bytearray:
    """返回素数标记表。"""
    if n < 2:
        return bytearray(n + 1)
    flags = bytearray(b"\x01") * (n + 1)
    flags[0:2] = b"\x00\x00"
    for p in range(2, isqrt(n) + 1):
        if flags[p]:
            start = p * p
            flags[start : n + 1 : p] = b"\x00" * (((n - start) // p) + 1)
    return flags


def primes_from_flags(flags: bytearray) -> list[int]:
    """从标记表抽取素数。"""
    return [i for i, is_prime in enumerate(flags) if is_prime]


def prime_prefix(flags: bytearray) -> array:
    """构造 pi(x) 前缀表。"""
    prefix = array("I", [0]) * len(flags)
    count = 0
    for i, is_prime in enumerate(flags):
        if is_prime:
            count += 1
        prefix[i] = count
    return prefix


def pi_between(prefix: array, lower_exclusive: int, upper_inclusive: int) -> int:
    """计算 lower < prime <= upper 的素数个数。"""
    if upper_inclusive <= lower_exclusive:
        return 0
    return int(prefix[upper_inclusive]) - int(prefix[lower_exclusive])


def high_prime_payment_counts(prefix: array, p_len: int) -> dict[str, Any]:
    """计算顶行 high-prime payment 的精确分裂。"""
    lower = p_len * p_len - p_len
    upper = p_len * p_len - 1
    prime_slots = pi_between(prefix, lower, upper)
    low_carrier_payment = 0
    carrier_rows: list[dict[str, int]] = []
    for m in range(2, p_len):
        count = pi_between(prefix, lower // m, upper // m)
        if count:
            low_carrier_payment += count
            if len(carrier_rows) < 16:
                carrier_rows.append({"carrier_m": m, "high_prime_payment_slots": count})
    slot_count = p_len - 1
    smooth_slots = slot_count - prime_slots - low_carrier_payment
    return {
        "P": p_len,
        "slot_count": slot_count,
        "prime_slots_m_equals_1": prime_slots,
        "low_carrier_high_prime_payment_slots_m_ge_2": low_carrier_payment,
        "p_smooth_composite_slots": smooth_slots,
        "split_identity_holds": slot_count == prime_slots + low_carrier_payment + smooth_slots,
        "sample_nonzero_carriers": carrier_rows,
    }


def finite_sweep(max_prime: int = 5003) -> dict[str, Any]:
    """有限审计 high-prime payment 分裂；不作全局证明。"""
    flags = prime_sieve(max_prime * max_prime)
    prefix = prime_prefix(flags)
    strict_primes = [p for p in primes_from_flags(flags[: max_prime + 1]) if p >= 3]
    min_prime_slots: int | None = None
    min_prime_cases: list[dict[str, int]] = []
    max_low_payment_ratio = 0.0
    max_low_payment_cases: list[dict[str, Any]] = []
    max_smooth_ratio = 0.0
    max_smooth_cases: list[dict[str, Any]] = []
    identity_failures: list[dict[str, int]] = []
    for p_len in strict_primes:
        counts = high_prime_payment_counts(prefix, p_len)
        if not counts["split_identity_holds"]:
            identity_failures.append({"P": p_len})
        prime_slots = counts["prime_slots_m_equals_1"]
        if min_prime_slots is None or prime_slots < min_prime_slots:
            min_prime_slots = prime_slots
            min_prime_cases = [{"P": p_len, "prime_slots": prime_slots}]
        elif prime_slots == min_prime_slots and len(min_prime_cases) < 16:
            min_prime_cases.append({"P": p_len, "prime_slots": prime_slots})
        low_ratio = counts["low_carrier_high_prime_payment_slots_m_ge_2"] / counts["slot_count"]
        if low_ratio > max_low_payment_ratio:
            max_low_payment_ratio = low_ratio
            max_low_payment_cases = [
                {
                    "P": p_len,
                    "low_carrier_high_prime_payment_slots": counts[
                        "low_carrier_high_prime_payment_slots_m_ge_2"
                    ],
                    "slot_count": counts["slot_count"],
                    "ratio": low_ratio,
                    "prime_slots": prime_slots,
                }
            ]
        elif low_ratio == max_low_payment_ratio and len(max_low_payment_cases) < 16:
            max_low_payment_cases.append(
                {
                    "P": p_len,
                    "low_carrier_high_prime_payment_slots": counts[
                        "low_carrier_high_prime_payment_slots_m_ge_2"
                    ],
                    "slot_count": counts["slot_count"],
                    "ratio": low_ratio,
                    "prime_slots": prime_slots,
                }
            )
        smooth_ratio = counts["p_smooth_composite_slots"] / counts["slot_count"]
        if smooth_ratio > max_smooth_ratio:
            max_smooth_ratio = smooth_ratio
            max_smooth_cases = [
                {
                    "P": p_len,
                    "p_smooth_composite_slots": counts["p_smooth_composite_slots"],
                    "slot_count": counts["slot_count"],
                    "ratio": smooth_ratio,
                    "prime_slots": prime_slots,
                }
            ]
        elif smooth_ratio == max_smooth_ratio and len(max_smooth_cases) < 16:
            max_smooth_cases.append(
                {
                    "P": p_len,
                    "p_smooth_composite_slots": counts["p_smooth_composite_slots"],
                    "slot_count": counts["slot_count"],
                    "ratio": smooth_ratio,
                    "prime_slots": prime_slots,
                }
            )
    sample_ps = [5, 11, 17, 101, 499, 5003]
    return {
        "max_prime": max_prime,
        "case_count": len(strict_primes),
        "identity_failures": identity_failures,
        "all_split_identities_hold": not identity_failures,
        "minimum_prime_slots_m_equals_1": min_prime_slots,
        "minimum_prime_slot_cases": min_prime_cases,
        "maximum_low_carrier_payment_ratio": max_low_payment_ratio,
        "maximum_low_carrier_payment_cases": max_low_payment_cases,
        "maximum_p_smooth_composite_ratio": max_smooth_ratio,
        "maximum_p_smooth_composite_cases": max_smooth_cases,
        "sample_splits": [high_prime_payment_counts(prefix, p) for p in sample_ps],
        "finite_evidence_not_used_as_global_proof": True,
    }


def build_rows() -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        row(
            "HighPrimePaymentSplitIdentityClosed",
            True,
            True,
            "顶行槽位精确分裂为 m=1 素数槽、2<=m<P 低载体高素数 payment、以及 P-smooth 合数槽。",
            "exact split only",
        ),
        row(
            "PrimeSlotEqualsMOneClosed",
            True,
            True,
            "目标正性正是 m=1 high-prime slot 非空。",
            "prove H_1(P)>=1",
        ),
        row(
            "SylvesterSchurLeakLocated",
            True,
            True,
            "若 m=1 为空，连续乘积输入只强制 2<=m<P 的低载体 payment 非空。",
            "single leak is not positivity",
        ),
        row(
            "LowCarrierPaymentCapacityExceeded",
            False,
            False,
            "当前语料没有证明低载体 payment 与 P-smooth 槽的合计容量小于 P-1。",
            "capacity deficit or positive rejection excess",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本层只定位 high-prime leak 的真实落点。",
            "strict row positivity still open",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造证书。"""
    sweep = finite_sweep()
    dependency_hashes = {
        str(path.relative_to(ROOT)): sha256(path) for path in DEPENDENCIES if path.exists()
    }
    return {
        "certificate_type": "prime_matrix_phi_lpf_strict_k_top_row_high_prime_payment_split_router",
        "status": "strict_k_top_row_high_prime_leak_split_into_prime_slot_or_low_carrier_payment",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "top_row_slots": "T_P={n:P^2-P<n<P^2}",
        "high_prime_factor_split": (
            "P-1 = H_1(P)+sum_{2<=m<P}H_m(P)+S_P(P)"
        ),
        "prime_slot_term": "H_1(P)=pi(P^2-1)-pi(P^2-P)",
        "low_carrier_payment_term": (
            "H_m(P)=pi(floor((P^2-1)/m))-pi(floor((P^2-P)/m)), 2<=m<P"
        ),
        "smooth_term": "S_P(P)=# top-row composite slots with all prime factors <=P",
        "target_positivity": "H_1(P)>=1",
        "sylvester_schur_conditional_output": (
            "若 H_1(P)=0，Sylvester-Schur 只给出 sum_{2<=m<P}H_m(P)>=1，"
            "而不是 H_1(P)>=1。"
        ),
        "low_carrier_payment_capacity_exceeded": False,
        "row_column_unconditional_closed": False,
        "finite_sweep": sweep,
        "gates": build_rows(),
        "source_hashes": {
            str(Path(__file__).resolve().relative_to(ROOT)): sha256(Path(__file__).resolve()),
            **dependency_hashes,
        },
        "plain_conclusion": (
            "顶行的 high-prime 泄出分成三块：m=1 是真正的素数槽，2<=m<P 是低载体"
            "高素数 payment，剩余是所有素因子 <=P 的 smooth 合数槽。目标正性就是"
            "证明 m=1 非空。Sylvester-Schur 在 m=1 为空的反设下只推出低载体 payment"
            " 非空，不能直接推出矛盾；要闭合还必须证明低载体 payment 加 smooth 槽"
            "不能铺满全部 P-1 个槽位。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    sweep = result["finite_sweep"]
    lines = [
        "# Prime Matrix Phi-LPF strict k top row high-prime payment split 证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "## 1. high-prime 分裂恒等式",
        "",
        "```text",
        result["top_row_slots"],
        result["high_prime_factor_split"],
        result["prime_slot_term"],
        result["low_carrier_payment_term"],
        result["smooth_term"],
        result["target_positivity"],
        "```",
        "",
        "这里 `m=1` 正是顶行素数本身；`2<=m<P` 是一个大素数因子被小载体支付，",
        "不是未铺满槽位。",
        "",
        "## 2. Sylvester-Schur 的实际强度",
        "",
        "```text",
        result["sylvester_schur_conditional_output"],
        "```",
        "",
        "因此经典连续乘积输入只定位一笔低载体 payment；它缺少把该 payment 放大成",
        "`H_1(P)>=1` 的机制。",
        "",
        "## 3. 有限审计边界",
        "",
        "```text",
        f"max_prime={sweep['max_prime']}",
        f"case_count={sweep['case_count']}",
        f"all_split_identities_hold={fmt_bool(sweep['all_split_identities_hold'])}",
        f"minimum_prime_slots_m_equals_1={sweep['minimum_prime_slots_m_equals_1']}",
        f"maximum_low_carrier_payment_ratio={sweep['maximum_low_carrier_payment_ratio']:.6f}",
        f"maximum_p_smooth_composite_ratio={sweep['maximum_p_smooth_composite_ratio']:.6f}",
        "finite_evidence_not_used_as_global_proof=true",
        "```",
        "",
        "最小 `m=1` 素数槽样本：",
        "",
        "| P | H_1(P) |",
        "| ---: | ---: |",
    ]
    for item in sweep["minimum_prime_slot_cases"]:
        lines.append(f"| {item['P']} | {item['prime_slots']} |")
    lines.extend(
        [
            "",
            "低载体 payment 比例最大样本：",
            "",
            "| P | low-carrier payment | slot count | ratio | H_1(P) |",
            "| ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for item in sweep["maximum_low_carrier_payment_cases"]:
        lines.append(
            "| {P} | {low} | {slot} | {ratio:.6f} | {prime} |".format(
                P=item["P"],
                low=item["low_carrier_high_prime_payment_slots"],
                slot=item["slot_count"],
                ratio=item["ratio"],
                prime=item["prime_slots"],
            )
        )
    lines.extend(
        [
            "",
            "P-smooth 合数比例最大样本：",
            "",
            "| P | P-smooth composite | slot count | ratio | H_1(P) |",
            "| ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for item in sweep["maximum_p_smooth_composite_cases"]:
        lines.append(
            "| {P} | {smooth} | {slot} | {ratio:.6f} | {prime} |".format(
                P=item["P"],
                smooth=item["p_smooth_composite_slots"],
                slot=item["slot_count"],
                ratio=item["ratio"],
                prime=item["prime_slots"],
            )
        )
    lines.extend(["", "## 4. 样本分裂", ""])
    lines.extend(
        [
            "| P | H_1 prime slots | low-carrier payment | P-smooth composite | slot count |",
            "| ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for item in sweep["sample_splits"]:
        lines.append(
            "| {P} | {prime} | {low} | {smooth} | {slot} |".format(
                P=item["P"],
                prime=item["prime_slots_m_equals_1"],
                low=item["low_carrier_high_prime_payment_slots_m_ge_2"],
                smooth=item["p_smooth_composite_slots"],
                slot=item["slot_count"],
            )
        )
    lines.extend(
        [
            "",
            "## 5. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in result["gates"]:
        lines.append(
            f"| `{cell(item['gate'])}` | `{fmt_bool(item['closed'])}` | "
            f"`{fmt_bool(item['proved'])}` | {cell(item['meaning'])} | {cell(item['remaining'])} |"
        )
    lines.extend(
        [
            "",
            "## 6. 结论",
            "",
            "这一层排除了一个常见误读：大素因子泄出不等于顶行有素数。",
            "只有 `m=1` 泄出才是目标正性；`2<=m<P` 泄出是低载体 payment。",
            "剩余硬点是证明低载体 payment 与 P-smooth 合数槽不能合计铺满全部顶行。",
            "",
            "## 7. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in result["source_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def write_outputs(result: dict[str, Any]) -> None:
    """写出 JSON 与 Markdown。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    text = json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True)
    OUT_LEDGER.write_text(text + "\n", encoding="utf-8")
    OUT_JSON.write_text(text + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")


def main() -> None:
    """入口。"""
    result = build_result()
    write_outputs(result)
    print(json.dumps({"status": result["status"], "outputs": [str(OUT_LEDGER), str(OUT_JSON), str(OUT_MD)]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
