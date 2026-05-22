#!/usr/bin/env python3
"""生成 strict 行 Phi-LPF load-phase tradeoff 证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_strict_k_row_load_phase_tradeoff_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-strict-k-row-load-phase-tradeoff-router.json

输出：
  data/prime-matrix-phi-lpf-strict-k-row-load-phase-tradeoff-ledger.json
  docs/monograph/prime-matrix-phi-lpf-strict-k-row-load-phase-tradeoff-router.json
  docs/monograph/prime-matrix-phi-lpf-strict-k-row-load-phase-tradeoff-router.md
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

SLUG = "prime-matrix-phi-lpf-strict-k-row-load-phase-tradeoff"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

DEPENDENCIES = [
    DOCS / "prime-matrix-phi-lpf-strict-k-row-high-prime-payment-support-router.json",
    DOCS / "prime-matrix-phi-lpf-strict-k-raw-rejection-balance-router.json",
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
    """计算 strict 行的三股负载。"""
    lower = k * p_len
    upper = (k + 1) * p_len - 1
    prime_slots = pi_between(prefix, lower, upper)
    low_payment = 0
    for m in range(2, k + 1):
        low_payment += pi_between(prefix, lower // m, upper // m)
    slot_count = p_len - 1
    smooth_slots = slot_count - prime_slots - low_payment
    return {
        "P": p_len,
        "k": k,
        "slot_count": slot_count,
        "prime_slots": prime_slots,
        "low_carrier_payment": low_payment,
        "p_smooth_slots": smooth_slots,
        "payment_ratio": low_payment / slot_count,
        "smooth_ratio": smooth_slots / slot_count,
        "prime_ratio": prime_slots / slot_count,
        "composite_ratio": (low_payment + smooth_slots) / slot_count,
        "identity_holds": smooth_slots >= 0 and slot_count == prime_slots + low_payment + smooth_slots,
    }


def phase_label(index: int, bins: int) -> str:
    """生成 k/P 相位分箱标签。"""
    left = index / bins
    right = (index + 1) / bins
    return f"[{left:.1f},{right:.1f})" if index < bins - 1 else f"[{left:.1f},1.0)"


def update_max(bucket: dict[str, Any], key: str, value: float, case: dict[str, Any]) -> None:
    """更新某个最大值记录。"""
    if value > bucket[key]["value"]:
        bucket[key] = {"value": value, "cases": [case]}
    elif value == bucket[key]["value"] and len(bucket[key]["cases"]) < 8:
        bucket[key]["cases"].append(case)


def finite_sweep(max_prime: int = 1009, bins: int = 10) -> dict[str, Any]:
    """有限审计 normalized load tradeoff；不作全局证明。"""
    flags = prime_sieve(max_prime * max_prime)
    prefix = prime_prefix(flags)
    strict_primes = [p for p in primes_from_flags(flags[: max_prime + 1]) if p >= 5]
    global_max = {
        "payment": {"value": -1.0, "cases": []},
        "smooth": {"value": -1.0, "cases": []},
        "composite": {"value": -1.0, "cases": []},
        "prime": {"value": -1.0, "cases": []},
    }
    phase_bins = [
        {
            "label": phase_label(i, bins),
            "row_count": 0,
            "max_payment": {"value": -1.0, "cases": []},
            "max_smooth": {"value": -1.0, "cases": []},
            "max_composite": {"value": -1.0, "cases": []},
            "min_prime_slots": None,
            "min_prime_cases": [],
        }
        for i in range(bins)
    ]
    row_count = 0
    identity_failures: list[dict[str, int]] = []
    zero_prime_rows: list[dict[str, int]] = []
    high_high_threshold_hits: list[dict[str, Any]] = []
    min_prime_slots: int | None = None
    min_prime_cases: list[dict[str, int]] = []
    for p_len in strict_primes:
        for k in range(2, p_len):
            row_count += 1
            split = row_split(prefix, p_len, k)
            if not split["identity_holds"]:
                identity_failures.append({"P": p_len, "k": k})
            if split["prime_slots"] == 0 and len(zero_prime_rows) < 32:
                zero_prime_rows.append({"P": p_len, "k": k})
            if min_prime_slots is None or split["prime_slots"] < min_prime_slots:
                min_prime_slots = split["prime_slots"]
                min_prime_cases = [{"P": p_len, "k": k, "prime_slots": split["prime_slots"]}]
            elif split["prime_slots"] == min_prime_slots and len(min_prime_cases) < 16:
                min_prime_cases.append({"P": p_len, "k": k, "prime_slots": split["prime_slots"]})
            case = {
                "P": p_len,
                "k": k,
                "k_over_p": k / p_len,
                "prime_slots": split["prime_slots"],
                "payment_ratio": split["payment_ratio"],
                "smooth_ratio": split["smooth_ratio"],
                "composite_ratio": split["composite_ratio"],
            }
            update_max(global_max, "payment", split["payment_ratio"], case)
            update_max(global_max, "smooth", split["smooth_ratio"], case)
            update_max(global_max, "composite", split["composite_ratio"], case)
            update_max(global_max, "prime", split["prime_ratio"], case)
            if split["payment_ratio"] >= 0.70 and split["smooth_ratio"] >= 0.70:
                high_high_threshold_hits.append(case)
            idx = min(bins - 1, int((k * bins) / p_len))
            bucket = phase_bins[idx]
            bucket["row_count"] += 1
            update_max(bucket, "max_payment", split["payment_ratio"], case)
            update_max(bucket, "max_smooth", split["smooth_ratio"], case)
            update_max(bucket, "max_composite", split["composite_ratio"], case)
            if bucket["min_prime_slots"] is None or split["prime_slots"] < bucket["min_prime_slots"]:
                bucket["min_prime_slots"] = split["prime_slots"]
                bucket["min_prime_cases"] = [{"P": p_len, "k": k, "prime_slots": split["prime_slots"]}]
            elif split["prime_slots"] == bucket["min_prime_slots"] and len(bucket["min_prime_cases"]) < 8:
                bucket["min_prime_cases"].append(
                    {"P": p_len, "k": k, "prime_slots": split["prime_slots"]}
                )
    sample_pairs = [(11, 2), (101, 2), (101, 50), (101, 100), (863, 2), (1009, 1008)]
    return {
        "max_prime": max_prime,
        "prime_count": len(strict_primes),
        "strict_row_count": row_count,
        "identity_failures": identity_failures[:32],
        "all_split_identities_hold": not identity_failures,
        "zero_prime_rows_found_in_finite_sweep": zero_prime_rows,
        "all_rows_positive_in_finite_sweep": not zero_prime_rows,
        "minimum_prime_slots": min_prime_slots,
        "minimum_prime_cases": min_prime_cases,
        "global_maxima": global_max,
        "phase_bins": phase_bins,
        "no_payment_smooth_both_ge_070_in_sweep": not high_high_threshold_hits,
        "payment_smooth_both_ge_070_hits": high_high_threshold_hits[:32],
        "sample_splits": [row_split(prefix, p, k) for p, k in sample_pairs],
        "finite_evidence_not_used_as_global_proof": True,
    }


def build_rows() -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        row(
            "NormalizedLoadIdentityClosed",
            True,
            True,
            "每行满足 lambda_payment+sigma_smooth+eta_prime=1。",
            "exact normalized ledger",
        ),
        row(
            "PositivityEquivalentToAntiSaturationClosed",
            True,
            True,
            "H_1(k,P)>=1 等价于 lambda_payment+sigma_smooth <= 1-1/(P-1)。",
            "same target in load variables",
        ),
        row(
            "PhaseTradeoffIdentified",
            True,
            False,
            "有限审计显示 payment 峰值与 smooth 峰值分处不同 k/P 相位。",
            "finite evidence only",
        ),
        row(
            "AntiCoSaturationInequalityProved",
            False,
            False,
            "当前语料没有证明 payment 与 smooth 不能同相饱和。",
            "global anti-co-saturation inequality",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本层只把容量缺口重写成两股负载反同相问题。",
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
        "certificate_type": "prime_matrix_phi_lpf_strict_k_row_load_phase_tradeoff_router",
        "status": "strict_k_capacity_deficit_reduced_to_payment_smooth_anti_cosaturation",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "normalized_loads": (
            "lambda(k,P)=sum_{2<=m<=k}H_m(k,P)/(P-1), "
            "sigma(k,P)=S_k(P)/(P-1), eta(k,P)=H_1(k,P)/(P-1)"
        ),
        "load_identity": "lambda(k,P)+sigma(k,P)+eta(k,P)=1",
        "positivity_equivalence": (
            "H_1(k,P)>=1 iff lambda(k,P)+sigma(k,P)<=1-1/(P-1)"
        ),
        "anti_cosaturation_needed": (
            "payment and P-smooth load cannot co-saturate at total mass 1"
        ),
        "anti_cosaturation_inequality_proved": False,
        "row_column_unconditional_closed": False,
        "finite_sweep": sweep,
        "gates": build_rows(),
        "source_hashes": {
            str(Path(__file__).resolve().relative_to(ROOT)): sha256(Path(__file__).resolve()),
            **dependency_hashes,
        },
        "plain_conclusion": (
            "strict 行正性现在被压成两股负载的反同相问题：低载体 high-prime payment"
            " 负载 lambda 与 P-smooth 合数负载 sigma 满足 lambda+sigma+eta=1，"
            "其中 eta 是目标素数槽比例。要证明正性，必须证明 lambda 与 sigma 不能"
            "同相饱和到 1。有限审计显示两股峰值出现在不同 k/P 相位，但当前语料尚无"
            "全局反同相不等式。"
        ),
    }


def render_case(case: dict[str, Any]) -> str:
    """渲染最大值样本。"""
    return (
        f"P={case['P']}, k={case['k']}, k/P={case['k_over_p']:.4f}, "
        f"pay={case['payment_ratio']:.6f}, smooth={case['smooth_ratio']:.6f}, "
        f"prime={case['prime_slots']}"
    )


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    sweep = result["finite_sweep"]
    lines = [
        "# Prime Matrix Phi-LPF strict k row load phase tradeoff 证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "## 1. 归一化负载恒等式",
        "",
        "```text",
        result["normalized_loads"],
        result["load_identity"],
        result["positivity_equivalence"],
        "```",
        "",
        "因此正性不再是计数公式问题，而是 `lambda` 与 `sigma` 不能同时把总质量推到 1 的问题。",
        "",
        "## 2. 有限审计边界",
        "",
        "```text",
        f"max_prime={sweep['max_prime']}",
        f"prime_count={sweep['prime_count']}",
        f"strict_row_count={sweep['strict_row_count']}",
        f"all_split_identities_hold={fmt_bool(sweep['all_split_identities_hold'])}",
        f"all_rows_positive_in_finite_sweep={fmt_bool(sweep['all_rows_positive_in_finite_sweep'])}",
        f"minimum_prime_slots={sweep['minimum_prime_slots']}",
        "no_payment_smooth_both_ge_070_in_sweep="
        f"{fmt_bool(sweep['no_payment_smooth_both_ge_070_in_sweep'])}",
        "finite_evidence_not_used_as_global_proof=true",
        "```",
        "",
        "全局峰值样本：",
        "",
        "| load | value | cases |",
        "| --- | ---: | --- |",
    ]
    for key, label in [
        ("payment", "lambda payment"),
        ("smooth", "sigma smooth"),
        ("composite", "lambda+sigma"),
        ("prime", "eta prime"),
    ]:
        item = sweep["global_maxima"][key]
        cases = "; ".join(render_case(case) for case in item["cases"][:3])
        lines.append(f"| {label} | {item['value']:.6f} | {cell(cases)} |")
    lines.extend(
        [
            "",
            "最小素数槽样本：",
            "",
            "| P | k | H_1(k,P) |",
            "| ---: | ---: | ---: |",
        ]
    )
    for item in sweep["minimum_prime_cases"]:
        lines.append(f"| {item['P']} | {item['k']} | {item['prime_slots']} |")
    lines.extend(
        [
            "",
            "## 3. k/P 相位分箱",
            "",
            "| phase k/P | rows | max payment | max smooth | max composite | min H_1 |",
            "| --- | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for bucket in sweep["phase_bins"]:
        min_prime = bucket["min_prime_slots"]
        lines.append(
            f"| `{bucket['label']}` | {bucket['row_count']} | "
            f"{bucket['max_payment']['value']:.6f} | {bucket['max_smooth']['value']:.6f} | "
            f"{bucket['max_composite']['value']:.6f} | {min_prime} |"
        )
    lines.extend(["", "## 4. 样本行", ""])
    lines.extend(
        [
            "| P | k | payment ratio | smooth ratio | prime ratio | H_1 |",
            "| ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for item in sweep["sample_splits"]:
        lines.append(
            "| {P} | {k} | {pay:.6f} | {smooth:.6f} | {prime_ratio:.6f} | {prime} |".format(
                P=item["P"],
                k=item["k"],
                pay=item["payment_ratio"],
                smooth=item["smooth_ratio"],
                prime_ratio=item["prime_ratio"],
                prime=item["prime_slots"],
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
            "这一层把剩余硬点改写成全局反同相不等式：",
            "`lambda(k,P)+sigma(k,P)<=1-1/(P-1)`。有限审计支持 payment 与 smooth 峰值错相，",
            "但没有证明全局错相。因此不能声称 strict 行正性已经无条件闭合。",
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
