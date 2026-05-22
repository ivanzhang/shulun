#!/usr/bin/env python3
"""生成 strict 行 low-carrier payment 下半源切断证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_strict_k_low_carrier_lower_half_source_cut_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-strict-k-low-carrier-lower-half-source-cut-router.json

输出：
  data/prime-matrix-phi-lpf-strict-k-low-carrier-lower-half-source-cut-ledger.json
  docs/monograph/prime-matrix-phi-lpf-strict-k-low-carrier-lower-half-source-cut-router.json
  docs/monograph/prime-matrix-phi-lpf-strict-k-low-carrier-lower-half-source-cut-router.md
"""

from __future__ import annotations

from array import array
import hashlib
import json
from math import isqrt
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-strict-k-low-carrier-lower-half-source-cut"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

DEPENDENCIES = [
    DOCS / "prime-matrix-phi-lpf-strict-k-row-high-prime-payment-support-router.json",
    DOCS / "prime-matrix-phi-lpf-strict-k-row-load-phase-tradeoff-router.json",
    DOCS / "prime-matrix-phi-lpf-strict-k-dusart-interval-bridge-router.json",
    DOCS / "prime-matrix-phi-lpf-strict-k-raw-rejection-balance-router.json",
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


def h_m(prefix: array, p_len: int, k: int, m: int) -> int:
    """计算第 m 个 low-carrier payment lane 的素数源数。"""
    lower = k * p_len
    upper = (k + 1) * p_len - 1
    return pi_between(prefix, lower // m, upper // m)


def row_payment_summary(prefix: array, p_len: int, k: int) -> dict[str, Any]:
    """汇总一行的 lower-half source cut 读数。"""
    payment = 0
    positive_lanes = 0
    max_source_row_bound = 0
    max_source_ratio = 0.0
    tight_lanes: list[dict[str, Any]] = []
    for m in range(2, k + 1):
        count = h_m(prefix, p_len, k, m)
        if count == 0:
            continue
        positive_lanes += 1
        payment += count
        max_r = ((k + 1) * p_len - 1) // m
        source_row_bound = max_r // p_len
        ratio = source_row_bound / k
        if source_row_bound > max_source_row_bound:
            max_source_row_bound = source_row_bound
            max_source_ratio = ratio
            tight_lanes = [
                {
                    "m": m,
                    "H_m": count,
                    "source_row_bound": source_row_bound,
                    "floor_k_over_2": k // 2,
                    "source_ratio": ratio,
                }
            ]
        elif source_row_bound == max_source_row_bound and len(tight_lanes) < 8:
            tight_lanes.append(
                {
                    "m": m,
                    "H_m": count,
                    "source_row_bound": source_row_bound,
                    "floor_k_over_2": k // 2,
                    "source_ratio": ratio,
                }
            )
    return {
        "P": p_len,
        "k": k,
        "low_carrier_payment": payment,
        "positive_payment_lanes": positive_lanes,
        "max_source_row_bound": max_source_row_bound,
        "floor_k_over_2": k // 2,
        "max_source_ratio": max_source_ratio,
        "bound_holds": max_source_row_bound <= k // 2,
        "tight_lanes": tight_lanes,
    }


def finite_sweep(max_prime: int = 1009) -> dict[str, Any]:
    """有限审计下半源切断；不把有限样本当全局证明。"""
    flags = prime_sieve(max_prime * max_prime)
    prefix = prime_prefix(flags)
    strict_primes = [p for p in primes_from_flags(flags[: max_prime + 1]) if p >= 5]
    row_count = 0
    rows_with_payment = 0
    violation_rows: list[dict[str, int]] = []
    max_payment = {"value": -1, "cases": []}
    max_source_ratio = {"value": -1.0, "cases": []}
    tight_half_cases: list[dict[str, Any]] = []
    sample_pairs = [(11, 10), (101, 50), (101, 100), (571, 438), (1009, 1008)]
    sample_rows: list[dict[str, Any]] = []

    for p_len in strict_primes:
        for k in range(2, p_len):
            row_count += 1
            summary = row_payment_summary(prefix, p_len, k)
            if summary["low_carrier_payment"] > 0:
                rows_with_payment += 1
            if not summary["bound_holds"] and len(violation_rows) < 32:
                violation_rows.append({"P": p_len, "k": k})
            payment = summary["low_carrier_payment"]
            if payment > max_payment["value"]:
                max_payment = {"value": payment, "cases": [summary]}
            elif payment == max_payment["value"] and len(max_payment["cases"]) < 8:
                max_payment["cases"].append(summary)
            ratio = summary["max_source_ratio"]
            if ratio > max_source_ratio["value"]:
                max_source_ratio = {"value": ratio, "cases": [summary]}
            elif ratio == max_source_ratio["value"] and len(max_source_ratio["cases"]) < 8:
                max_source_ratio["cases"].append(summary)
            if summary["max_source_row_bound"] == summary["floor_k_over_2"] and len(tight_half_cases) < 16:
                tight_half_cases.append(summary)

    for p_len, k in sample_pairs:
        sample_rows.append(row_payment_summary(prefix, p_len, k))

    return {
        "max_prime": max_prime,
        "prime_count": len(strict_primes),
        "strict_row_count": row_count,
        "rows_with_low_carrier_payment": rows_with_payment,
        "all_payment_sources_in_lower_half": not violation_rows,
        "violation_rows": violation_rows,
        "max_low_carrier_payment": max_payment,
        "max_source_ratio": max_source_ratio,
        "tight_half_cases": tight_half_cases,
        "sample_rows": sample_rows,
        "finite_evidence_not_used_as_global_proof": True,
    }


def build_rows() -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        row(
            "LowCarrierPaymentSourceIntervalClosed",
            True,
            True,
            "若 n=mr 落在 strict 行且 r>P 为素数、m>=2，则 r 位于 (kP/m,((k+1)P-1)/m]。",
            "exact source interval",
        ),
        row(
            "PaymentSourceLowerHalfCutClosed",
            True,
            True,
            "因 m>=2，所有 payment prime r 都满足 r<((k+1)P)/2<kP。",
            "source row <= floor(k/2)",
        ),
        row(
            "SameRowAndFuturePaymentLoopExcluded",
            True,
            True,
            "low-carrier payment 不能来自当前行、近顶端行或未来行。",
            "acyclic lower-half source only",
        ),
        row(
            "PaymentInjectionPerSourcePrimeClosed",
            True,
            True,
            "固定目标行内，一个源素数 r>P 至多对应一个 carrier m，因为相邻 m 的乘积差为 r>P。",
            "injective source-to-slot map",
        ),
        row(
            "ZeroRowReducedToLowerHalfPaymentPlusSmoothTiling",
            True,
            True,
            "若 strict 行为零素数行，则所有槽必须由下半源 payment 注入像与 P-smooth 槽铺满。",
            "lower-half payment image + smooth = all slots",
        ),
        row(
            "LowerHalfPaymentSmoothAntiTilingProved",
            False,
            False,
            "当前语料尚未证明下半源 payment 像与 P-smooth 槽不能完美铺满全部行槽。",
            "global lower-half payment/smooth anti-tiling inequality",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本层排除 payment 来源环并压窄剩余，但不证明 strict 行正性。",
            "anti-tiling, rejection excess, or sqrt-scale input",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造证书。"""
    sweep = finite_sweep()
    dependency_hashes = {
        str(path.relative_to(ROOT)): sha256(path) for path in DEPENDENCIES if path.exists()
    }
    return {
        "certificate_type": "prime_matrix_phi_lpf_strict_k_low_carrier_lower_half_source_cut_router",
        "status": "strict_k_low_carrier_payment_reduced_to_acyclic_lower_half_source_injection",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "strict_k_range": "1<k<P",
        "source_cut_statement": (
            "For every payment slot n=mr with 2<=m<=k and prime r>P, "
            "one has r<((k+1)P)/2<kP and floor(r/P)<=floor(k/2)."
        ),
        "source_injection_statement": (
            "For fixed target row (P,k), each source prime r>P contributes to at most one "
            "low-carrier payment slot, since two carriers differ by at least r>P."
        ),
        "zero_row_consequence": (
            "A zero row must be a perfect tiling by the image of an acyclic lower-half "
            "payment injection plus the P-smooth slots."
        ),
        "lower_half_payment_smooth_anti_tiling_proved": False,
        "row_column_unconditional_closed": False,
        "finite_sweep": sweep,
        "gates": build_rows(),
        "source_hashes": {
            str(Path(__file__).resolve().relative_to(ROOT)): sha256(Path(__file__).resolve()),
            **dependency_hashes,
        },
        "plain_conclusion": (
            "low-carrier high-prime payment 不是当前行的自反馈来源：每个支付素数 r>P "
            "都落在当前行左侧并且最多位于 floor(k/2) 行。于是零行反例必须表现为"
            "早期下半源 prime injection 与 P-smooth 槽的完美铺满。当前层关闭来源环，"
            "但尚未证明该下半源 payment/smooth 反铺满不等式。"
        ),
    }


def render_case(case: dict[str, Any]) -> str:
    """渲染一条行样本。"""
    lanes = ",".join(
        f"m={lane['m']}:H={lane['H_m']}:j<={lane['source_row_bound']}"
        for lane in case.get("tight_lanes", [])
    )
    return (
        f"P={case['P']}, k={case['k']}, pay={case['low_carrier_payment']}, "
        f"j_max={case['max_source_row_bound']}, floor(k/2)={case['floor_k_over_2']}, "
        f"lanes={lanes}"
    )


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    sweep = result["finite_sweep"]
    lines = [
        "# Prime Matrix Phi-LPF strict k low-carrier lower-half source-cut 证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "## 1. 下半源切断",
        "",
        "```text",
        "n=mr, 2<=m<=k, r>P prime, kP<n<(k+1)P",
        "kP/m < r <= ((k+1)P-1)/m",
        "m>=2 => r < ((k+1)P)/2 < kP",
        "therefore floor(r/P) <= floor(k/2)",
        "```",
        "",
        "这说明 low-carrier payment 不能由当前行或未来行反向生成；它只能从严格更早的下半行源进入。",
        "",
        "## 2. 源素数注入",
        "",
        "固定目标行 `(P,k)` 与源素数 `r>P`。若两个不同 carrier `m1<m2` 同时命中该行，",
        "则 `(m2-m1)r>=r>P`，超过行宽 `P-1`。因此每个源素数至多支付一个槽。",
        "",
        "零行反设因此变成：",
        "",
        "```text",
        "all slots = image(lower-half prime source injection) union P-smooth slots",
        "```",
        "",
        "## 3. 有限审计",
        "",
        "```text",
        f"max_prime={sweep['max_prime']}",
        f"strict_row_count={sweep['strict_row_count']}",
        f"rows_with_low_carrier_payment={sweep['rows_with_low_carrier_payment']}",
        f"all_payment_sources_in_lower_half={fmt_bool(sweep['all_payment_sources_in_lower_half'])}",
        f"finite_evidence_not_used_as_global_proof={fmt_bool(sweep['finite_evidence_not_used_as_global_proof'])}",
        "```",
        "",
        "最大 payment 样本：",
        "",
        "| value | cases |",
        "| ---: | --- |",
        f"| {sweep['max_low_carrier_payment']['value']} | "
        f"{'; '.join(render_case(c) for c in sweep['max_low_carrier_payment']['cases'])} |",
        "",
        "最大源行比例样本：",
        "",
        "| value | cases |",
        "| ---: | --- |",
        f"| {sweep['max_source_ratio']['value']:.6f} | "
        f"{'; '.join(render_case(c) for c in sweep['max_source_ratio']['cases'])} |",
        "",
        "样本行：",
        "",
        "| P | k | payment | max source row | floor(k/2) | bound |",
        "| ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for item in sweep["sample_rows"]:
        lines.append(
            f"| {item['P']} | {item['k']} | {item['low_carrier_payment']} | "
            f"{item['max_source_row_bound']} | {item['floor_k_over_2']} | "
            f"`{fmt_bool(item['bound_holds'])}` |"
        )
    lines.extend(
        [
            "",
            "## 4. 判定表",
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
            "## 5. 结论",
            "",
            "本层把 `lambda` payment 负载改写为一个无环下半源注入像。",
            "若 strict 零行存在，它不能再解释为当前行自反馈支付；它必须是下半源 prime injection",
            "与 `P`-smooth 槽的完美铺满。剩余硬点相应压成",
            "`LowerHalfPaymentSmoothAntiTilingInequality`，或回到 raw/rejection strict excess，",
            "或提交真正的 sqrt-scale 短区间输入。",
            "",
            "## 6. 依赖哈希",
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
    print(
        json.dumps(
            {"status": result["status"], "outputs": [str(OUT_LEDGER), str(OUT_JSON), str(OUT_MD)]},
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
