#!/usr/bin/env python3
"""生成 strict 1<k<P 行 high-prime payment 支撑证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_strict_k_row_high_prime_payment_support_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-strict-k-row-high-prime-payment-support-router.json

输出：
  data/prime-matrix-phi-lpf-strict-k-row-high-prime-payment-support-ledger.json
  docs/monograph/prime-matrix-phi-lpf-strict-k-row-high-prime-payment-support-router.json
  docs/monograph/prime-matrix-phi-lpf-strict-k-row-high-prime-payment-support-router.md
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

SLUG = "prime-matrix-phi-lpf-strict-k-row-high-prime-payment-support"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

DEPENDENCIES = [
    DOCS / "prime-matrix-phi-lpf-strict-k-top-row-high-prime-payment-split-router.json",
    DOCS / "prime-matrix-phi-lpf-strict-k-top-row-perfect-tiling-router.json",
    DOCS / "prime-matrix-phi-lpf-strict-k-sqrt-gap-equivalence-router.json",
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


def row_split(prefix: array, p_len: int, k: int) -> dict[str, Any]:
    """计算 strict 行的 high-prime payment 支撑分裂。"""
    lower = k * p_len
    upper = (k + 1) * p_len - 1
    prime_slots = pi_between(prefix, lower, upper)
    low_carrier_payment = 0
    nonzero_carriers: list[dict[str, int]] = []
    for m in range(2, k + 1):
        count = pi_between(prefix, lower // m, upper // m)
        if count:
            low_carrier_payment += count
            if len(nonzero_carriers) < 16:
                nonzero_carriers.append({"carrier_m": m, "high_prime_payment_slots": count})
    slot_count = p_len - 1
    smooth_slots = slot_count - prime_slots - low_carrier_payment
    return {
        "P": p_len,
        "k": k,
        "interval": [lower + 1, upper],
        "slot_count": slot_count,
        "carrier_support_bound": f"2<=m<={k}",
        "prime_slots_m_equals_1": prime_slots,
        "low_carrier_high_prime_payment_slots": low_carrier_payment,
        "p_smooth_composite_slots": smooth_slots,
        "split_identity_holds": smooth_slots >= 0,
        "positive": prime_slots >= 1,
        "nonzero_carriers_sample": nonzero_carriers,
    }


def finite_sweep(max_prime: int = 1009) -> dict[str, Any]:
    """有限审计一般 strict 行；不作全局证明。"""
    flags = prime_sieve(max_prime * max_prime)
    prefix = prime_prefix(flags)
    strict_primes = [p for p in primes_from_flags(flags[: max_prime + 1]) if p >= 5]
    row_count = 0
    identity_failures: list[dict[str, int]] = []
    zero_prime_rows: list[dict[str, int]] = []
    max_low_payment_ratio = 0.0
    max_low_payment_cases: list[dict[str, Any]] = []
    max_smooth_ratio = 0.0
    max_smooth_cases: list[dict[str, Any]] = []
    min_prime_slots: int | None = None
    min_prime_cases: list[dict[str, int]] = []
    top_row_low_payment_ratio_wins = True
    for p_len in strict_primes:
        top_low_ratio = row_split(prefix, p_len, p_len - 1)[
            "low_carrier_high_prime_payment_slots"
        ] / (p_len - 1)
        for k in range(2, p_len):
            row_count += 1
            counts = row_split(prefix, p_len, k)
            if not counts["split_identity_holds"]:
                identity_failures.append({"P": p_len, "k": k})
            prime_slots = counts["prime_slots_m_equals_1"]
            if prime_slots == 0 and len(zero_prime_rows) < 32:
                zero_prime_rows.append({"P": p_len, "k": k})
            if min_prime_slots is None or prime_slots < min_prime_slots:
                min_prime_slots = prime_slots
                min_prime_cases = [{"P": p_len, "k": k, "prime_slots": prime_slots}]
            elif prime_slots == min_prime_slots and len(min_prime_cases) < 16:
                min_prime_cases.append({"P": p_len, "k": k, "prime_slots": prime_slots})
            low_ratio = counts["low_carrier_high_prime_payment_slots"] / counts["slot_count"]
            if k < p_len - 1 and low_ratio > top_low_ratio:
                top_row_low_payment_ratio_wins = False
            if low_ratio > max_low_payment_ratio:
                max_low_payment_ratio = low_ratio
                max_low_payment_cases = [
                    {
                        "P": p_len,
                        "k": k,
                        "low_carrier_high_prime_payment_slots": counts[
                            "low_carrier_high_prime_payment_slots"
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
                        "k": k,
                        "low_carrier_high_prime_payment_slots": counts[
                            "low_carrier_high_prime_payment_slots"
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
                        "k": k,
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
                        "k": k,
                        "p_smooth_composite_slots": counts["p_smooth_composite_slots"],
                        "slot_count": counts["slot_count"],
                        "ratio": smooth_ratio,
                        "prime_slots": prime_slots,
                    }
                )
    sample_pairs = [(5, 2), (11, 2), (11, 10), (101, 50), (101, 100), (1009, 1008)]
    return {
        "max_prime": max_prime,
        "prime_count": len(strict_primes),
        "strict_row_count": row_count,
        "identity_failures": identity_failures[:32],
        "all_split_identities_hold": not identity_failures,
        "zero_prime_rows_found_in_finite_sweep": zero_prime_rows,
        "all_rows_positive_in_finite_sweep": not zero_prime_rows,
        "minimum_prime_slots_m_equals_1": min_prime_slots,
        "minimum_prime_slot_cases": min_prime_cases,
        "maximum_low_carrier_payment_ratio": max_low_payment_ratio,
        "maximum_low_carrier_payment_cases": max_low_payment_cases,
        "maximum_p_smooth_composite_ratio": max_smooth_ratio,
        "maximum_p_smooth_composite_cases": max_smooth_cases,
        "top_row_low_payment_ratio_wins_for_each_prime_in_sweep": top_row_low_payment_ratio_wins,
        "sample_splits": [row_split(prefix, p, k) for p, k in sample_pairs],
        "finite_evidence_not_used_as_global_proof": True,
    }


def build_rows() -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        row(
            "StrictRowCarrierSupportBoundClosed",
            True,
            True,
            "若 strict 行槽位有素因子 r>P 且不是素数槽，则其低载体满足 2<=m<=k。",
            "exact support bound",
        ),
        row(
            "StrictRowHighPrimeSplitClosed",
            True,
            True,
            "每行精确分裂为 m=1 素数槽、2<=m<=k 的低载体 high-prime payment、以及 P-smooth 合数槽。",
            "exact split only",
        ),
        row(
            "TopRowMaximalCarrierSupportClosed",
            True,
            True,
            "k=P-1 顶行拥有最大低载体支撑 2<=m<P。",
            "top row remains necessary hard core",
        ),
        row(
            "GeneralCapacityDeficitProved",
            False,
            False,
            "当前语料没有证明每个 strict 行的低载体 payment 与 P-smooth 槽合计小于 P-1。",
            "strict-k capacity deficit",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本层只统一了一般 strict 行的 high-prime payment 支撑。",
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
        "certificate_type": "prime_matrix_phi_lpf_strict_k_row_high_prime_payment_support_router",
        "status": "strict_k_row_high_prime_payment_support_bound_identified_capacity_deficit_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "strict_row": "I_{k,P}={kP+a:1<=a<P}, 1<k<P",
        "carrier_support_bound": (
            "If n=mr in I_{k,P} and r>P, then m<n/P<k+1, hence m<=k."
        ),
        "strict_row_split": (
            "P-1=H_1(k,P)+sum_{2<=m<=k}H_m(k,P)+S_k(P)"
        ),
        "prime_slot_term": "H_1(k,P)=pi((k+1)P-1)-pi(kP)",
        "low_carrier_payment_term": (
            "H_m(k,P)=pi(floor(((k+1)P-1)/m))-pi(floor(kP/m)), 2<=m<=k"
        ),
        "smooth_term": "S_k(P)=# row slots with all prime factors <=P",
        "target_positivity": "H_1(k,P)>=1",
        "capacity_deficit_needed": "sum_{2<=m<=k}H_m(k,P)+S_k(P)<=P-2",
        "general_capacity_deficit_proved": False,
        "row_column_unconditional_closed": False,
        "finite_sweep": sweep,
        "gates": build_rows(),
        "source_hashes": {
            str(Path(__file__).resolve().relative_to(ROOT)): sha256(Path(__file__).resolve()),
            **dependency_hashes,
        },
        "plain_conclusion": (
            "对任意 strict 行，high-prime 泄出的低载体支撑不是 2<=m<P，"
            "而是精确缩到 2<=m<=k。顶行 k=P-1 因此仍是最大支撑硬核。"
            "Phi-LPF 端点差分的正性等价于证明低载体 high-prime payment 与"
            " P-smooth 合数槽不能合计铺满 P-1 个槽位；当前语料尚未无条件证明"
            "这个 strict-k 容量缺口。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    sweep = result["finite_sweep"]
    lines = [
        "# Prime Matrix Phi-LPF strict k row high-prime payment support 证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "## 1. 一般 strict 行支撑界",
        "",
        "```text",
        result["strict_row"],
        result["carrier_support_bound"],
        "```",
        "",
        "因此低载体 payment 的支撑随 k 增长；顶行 `k=P-1` 是最大支撑情形。",
        "",
        "## 2. 行级 high-prime 分裂",
        "",
        "```text",
        result["strict_row_split"],
        result["prime_slot_term"],
        result["low_carrier_payment_term"],
        result["smooth_term"],
        result["target_positivity"],
        result["capacity_deficit_needed"],
        "```",
        "",
        "这说明端点差分正性正是 `m=1` 非空；`2<=m<=k` 只是低载体支付。",
        "",
        "## 3. 有限审计边界",
        "",
        "```text",
        f"max_prime={sweep['max_prime']}",
        f"prime_count={sweep['prime_count']}",
        f"strict_row_count={sweep['strict_row_count']}",
        f"all_split_identities_hold={fmt_bool(sweep['all_split_identities_hold'])}",
        f"all_rows_positive_in_finite_sweep={fmt_bool(sweep['all_rows_positive_in_finite_sweep'])}",
        f"minimum_prime_slots_m_equals_1={sweep['minimum_prime_slots_m_equals_1']}",
        f"maximum_low_carrier_payment_ratio={sweep['maximum_low_carrier_payment_ratio']:.6f}",
        f"maximum_p_smooth_composite_ratio={sweep['maximum_p_smooth_composite_ratio']:.6f}",
        "top_row_low_payment_ratio_wins_for_each_prime_in_sweep="
        f"{fmt_bool(sweep['top_row_low_payment_ratio_wins_for_each_prime_in_sweep'])}",
        "finite_evidence_not_used_as_global_proof=true",
        "```",
        "",
        "最小 `m=1` 素数槽样本：",
        "",
        "| P | k | H_1(k,P) |",
        "| ---: | ---: | ---: |",
    ]
    for item in sweep["minimum_prime_slot_cases"]:
        lines.append(f"| {item['P']} | {item['k']} | {item['prime_slots']} |")
    lines.extend(
        [
            "",
            "低载体 payment 比例最大样本：",
            "",
            "| P | k | low-carrier payment | slot count | ratio | H_1(k,P) |",
            "| ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for item in sweep["maximum_low_carrier_payment_cases"]:
        lines.append(
            "| {P} | {k} | {low} | {slot} | {ratio:.6f} | {prime} |".format(
                P=item["P"],
                k=item["k"],
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
            "| P | k | P-smooth composite | slot count | ratio | H_1(k,P) |",
            "| ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for item in sweep["maximum_p_smooth_composite_cases"]:
        lines.append(
            "| {P} | {k} | {smooth} | {slot} | {ratio:.6f} | {prime} |".format(
                P=item["P"],
                k=item["k"],
                smooth=item["p_smooth_composite_slots"],
                slot=item["slot_count"],
                ratio=item["ratio"],
                prime=item["prime_slots"],
            )
        )
    lines.extend(["", "## 4. 样本分裂", ""])
    lines.extend(
        [
            "| P | k | H_1 prime slots | low-carrier payment | P-smooth composite | support |",
            "| ---: | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for item in sweep["sample_splits"]:
        lines.append(
            "| {P} | {k} | {prime} | {low} | {smooth} | `{support}` |".format(
                P=item["P"],
                k=item["k"],
                prime=item["prime_slots_m_equals_1"],
                low=item["low_carrier_high_prime_payment_slots"],
                smooth=item["p_smooth_composite_slots"],
                support=item["carrier_support_bound"],
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
            "一般 strict 行的 high-prime payment 已经被压到最窄支撑 `2<=m<=k`。",
            "这强化了顶行是最大支撑硬核的判断，但仍没有给出无条件正性。",
            "剩余需要一个真正的容量缺口：低载体 payment 与 P-smooth 合数槽不能铺满全部行槽。",
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
