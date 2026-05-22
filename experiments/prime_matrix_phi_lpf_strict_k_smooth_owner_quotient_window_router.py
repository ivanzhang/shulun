#!/usr/bin/env python3
"""生成 strict 行 P-smooth 槽的 LPF-owner quotient-window 证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_strict_k_smooth_owner_quotient_window_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-strict-k-smooth-owner-quotient-window-router.json

输出：
  data/prime-matrix-phi-lpf-strict-k-smooth-owner-quotient-window-ledger.json
  docs/monograph/prime-matrix-phi-lpf-strict-k-smooth-owner-quotient-window-router.json
  docs/monograph/prime-matrix-phi-lpf-strict-k-smooth-owner-quotient-window-router.md
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

SLUG = "prime-matrix-phi-lpf-strict-k-smooth-owner-quotient-window"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

DEPENDENCIES = [
    DOCS / "prime-matrix-phi-lpf-strict-k-endpoint-beatty-smooth-value-router.json",
    DOCS / "prime-matrix-phi-lpf-strict-k-beatty-euclidean-source-window-router.json",
    DOCS / "prime-matrix-phi-lpf-strict-k-internal-owner-saturation-router.json",
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


def spf_and_lpf(n: int) -> tuple[array, array, bytearray, list[int]]:
    """返回最小素因子、最大素因子、素数标记和素数表。"""
    spf = array("I", range(n + 1))
    lpf = array("I", [0]) * (n + 1)
    flags = bytearray(b"\x01") * (n + 1)
    if n >= 0:
        flags[0] = 0
        spf[0] = 0
    if n >= 1:
        flags[1] = 0
        spf[1] = 1
        lpf[1] = 1
    for p in range(2, isqrt(n) + 1):
        if spf[p] == p:
            for m in range(p * p, n + 1, p):
                if spf[m] == m:
                    spf[m] = p
                    flags[m] = 0
    primes = [i for i in range(2, n + 1) if flags[i]]
    for x in range(2, n + 1):
        y = x
        last = 1
        while y > 1:
            p = int(spf[y])
            last = p
            while y % p == 0:
                y //= p
        lpf[x] = last
    return spf, lpf, flags, primes


def beatty_payment_count(primes: list[int], p_len: int, k: int) -> int:
    """按 Beatty 近倍数源表计算 high-prime payment 槽数。"""
    lower = k * p_len
    upper = (k + 1) * p_len - 1
    source_upper = upper // 2
    total = 0
    for r in primes:
        if r <= p_len:
            continue
        if r > source_upper:
            break
        slot = r - (lower % r)
        if 1 <= slot <= p_len - 1:
            total += 1
    return total


def direct_slot_split(flags: bytearray, lpf: array, p_len: int, k: int) -> dict[str, Any]:
    """直接按最大素因子拆分目标行槽。"""
    lower = k * p_len
    prime_slots: list[int] = []
    smooth_slots: list[int] = []
    payment_slots: list[int] = []
    for slot in range(1, p_len):
        n = lower + slot
        if flags[n]:
            prime_slots.append(slot)
        elif lpf[n] <= p_len:
            smooth_slots.append(slot)
        else:
            payment_slots.append(slot)
    return {
        "prime_slots": prime_slots,
        "smooth_slots": smooth_slots,
        "payment_slots": payment_slots,
    }


def smooth_owner_window_count(
    spf: array,
    lpf: array,
    primes: list[int],
    p_len: int,
    k: int,
) -> dict[str, Any]:
    """按 LPF-owner 粗余因子窗口计算 P-smooth 槽。"""
    lower = k * p_len
    upper = (k + 1) * p_len - 1
    total = 0
    owner_rows: list[dict[str, Any]] = []
    for p in primes:
        if p > isqrt(upper):
            break
        left = lower // p
        right = upper // p
        count = 0
        sample_q: list[int] = []
        for q in range(left + 1, right + 1):
            if q >= p and spf[q] >= p and lpf[q] <= p_len:
                count += 1
                if len(sample_q) < 8:
                    sample_q.append(q)
        if count:
            owner_rows.append(
                {
                    "owner_p": p,
                    "q_left_exclusive": left,
                    "q_right_inclusive": right,
                    "smooth_q_count": count,
                    "sample_q": sample_q,
                }
            )
            total += count
    return {
        "smooth_owner_window_count": total,
        "owner_rows": owner_rows,
    }


def row_summary(
    spf: array,
    lpf: array,
    flags: bytearray,
    primes: list[int],
    p_len: int,
    k: int,
) -> dict[str, Any]:
    """汇总一条 strict 行的 high-prime/smooth 双 quotient-window 分解。"""
    split = direct_slot_split(flags, lpf, p_len, k)
    smooth_window = smooth_owner_window_count(spf, lpf, primes, p_len, k)
    beatty_count = beatty_payment_count(primes, p_len, k)
    length = p_len - 1
    prime_count = len(split["prime_slots"])
    smooth_count = len(split["smooth_slots"])
    payment_count = len(split["payment_slots"])
    return {
        "P": p_len,
        "k": k,
        "length": length,
        "prime_count": prime_count,
        "beatty_payment_count": beatty_count,
        "direct_high_prime_payment_count": payment_count,
        "smooth_count": smooth_count,
        "smooth_owner_window_count": smooth_window["smooth_owner_window_count"],
        "dual_window_formula_count": length - beatty_count - smooth_window["smooth_owner_window_count"],
        "beatty_matches_high_prime_slots": beatty_count == payment_count,
        "smooth_matches_owner_windows": smooth_count == smooth_window["smooth_owner_window_count"],
        "dual_formula_matches_prime_count": (
            prime_count == length - beatty_count - smooth_window["smooth_owner_window_count"]
        ),
        "positive_iff_dual_windows_not_full": (
            (prime_count > 0)
            == (beatty_count + smooth_window["smooth_owner_window_count"] <= p_len - 2)
        ),
        "prime_slots_sample": split["prime_slots"][:16],
        "payment_slots_sample": split["payment_slots"][:16],
        "smooth_slots_sample": split["smooth_slots"][:16],
        "owner_rows_sample": smooth_window["owner_rows"][:12],
    }


def finite_sweep(max_prime: int = 257) -> dict[str, Any]:
    """有限审计双 quotient-window 分解；不作为全局证明。"""
    sample_pairs = [(11, 10), (101, 50), (101, 100), (257, 244), (571, 438), (1009, 1008)]
    sieve_prime = max(max_prime, max(p for p, _k in sample_pairs))
    spf, lpf, flags, primes = spf_and_lpf(sieve_prime * sieve_prime)
    strict_primes = [p for p in primes if 5 <= p <= max_prime]
    row_count = 0
    failures: list[dict[str, Any]] = []
    min_prime_count: int | None = None
    min_prime_cases: list[dict[str, int]] = []
    max_smooth = {"value": -1, "cases": []}
    max_fill = {"value": -1.0, "cases": []}
    for p_len in strict_primes:
        for k in range(2, p_len):
            row_count += 1
            summary = row_summary(spf, lpf, flags, primes, p_len, k)
            ok = (
                summary["beatty_matches_high_prime_slots"]
                and summary["smooth_matches_owner_windows"]
                and summary["dual_formula_matches_prime_count"]
                and summary["positive_iff_dual_windows_not_full"]
            )
            if not ok and len(failures) < 8:
                failures.append(summary)
            prime_count = summary["prime_count"]
            if min_prime_count is None or prime_count < min_prime_count:
                min_prime_count = prime_count
                min_prime_cases = [{"P": p_len, "k": k, "prime_count": prime_count}]
            elif prime_count == min_prime_count and len(min_prime_cases) < 16:
                min_prime_cases.append({"P": p_len, "k": k, "prime_count": prime_count})
            case = {
                "P": p_len,
                "k": k,
                "prime_count": prime_count,
                "B": summary["beatty_payment_count"],
                "S": summary["smooth_count"],
                "fill": (summary["beatty_payment_count"] + summary["smooth_count"]) / summary["length"],
            }
            if summary["smooth_count"] > max_smooth["value"]:
                max_smooth = {"value": summary["smooth_count"], "cases": [case]}
            elif summary["smooth_count"] == max_smooth["value"] and len(max_smooth["cases"]) < 8:
                max_smooth["cases"].append(case)
            if case["fill"] > max_fill["value"]:
                max_fill = {"value": case["fill"], "cases": [case]}
            elif case["fill"] == max_fill["value"] and len(max_fill["cases"]) < 8:
                max_fill["cases"].append(case)
    sample_rows = [row_summary(spf, lpf, flags, primes, p, k) for p, k in sample_pairs]
    return {
        "max_prime": max_prime,
        "sieve_prime_for_large_samples": sieve_prime,
        "strict_row_count": row_count,
        "all_dual_quotient_window_identities_hold": not failures,
        "failures": failures,
        "minimum_prime_count": min_prime_count,
        "minimum_prime_cases": min_prime_cases,
        "max_smooth": max_smooth,
        "max_dual_fill": max_fill,
        "sample_rows": sample_rows,
        "finite_evidence_not_used_as_global_proof": True,
    }


def build_rows() -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        row(
            "SmoothOwnerQuotientWindowClosed",
            True,
            True,
            "P-smooth 槽等于 LPF-owner p 的 p-rough 且 P-smooth cofactor q 窗口计数之和。",
            "smooth owner windows",
        ),
        row(
            "HighPrimeBeattyWindowClosed",
            True,
            True,
            "high-prime payment 槽等于 Beatty/Euclidean source-window prime 计数。",
            "high-prime source windows",
        ),
        row(
            "DualWindowExactValueClosed",
            True,
            True,
            "N_P(k)=(P-1)-B_P(k)-S_P(k)，其中 B 与 S 均为 quotient-window 计数。",
            "dual quotient-window value",
        ),
        row(
            "DualWindowAntiTilingEquivalentClosed",
            True,
            True,
            "正性等价于 high-prime source windows 与 smooth owner windows 未铺满 P-1 个槽。",
            "same positivity target",
        ),
        row(
            "DualWindowAntiTilingProved",
            False,
            False,
            "本层没有证明双窗口不能铺满。",
            "global dual-window anti-tiling inequality",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本层只统一了两个 quotient-window 源域。",
            "anti-tiling, rejection excess, or sqrt-scale input",
        ),
    ]


def rows_markdown(rows: list[dict[str, Any]]) -> str:
    """输出判定表 Markdown。"""
    lines = ["| gate | closed | proved | meaning | remaining |", "| --- | --- | --- | --- | --- |"]
    for item in rows:
        lines.append(
            "| {gate} | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=cell(item["gate"]),
                closed=fmt_bool(item["closed"]),
                proved=fmt_bool(item["proved"]),
                meaning=cell(item["meaning"]),
                remaining=cell(item["remaining"]),
            )
        )
    return "\n".join(lines)


def sample_rows_markdown(sample_rows: list[dict[str, Any]]) -> str:
    """输出样本行 Markdown。"""
    lines = [
        "| P | k | N_P(k) | B high-prime | S smooth | dual formula | first owner rows |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for item in sample_rows:
        owners = ", ".join(
            f"{row['owner_p']}:{row['smooth_q_count']}" for row in item["owner_rows_sample"][:8]
        )
        lines.append(
            f"| {item['P']} | {item['k']} | {item['prime_count']} | "
            f"{item['beatty_payment_count']} | {item['smooth_count']} | "
            f"{item['dual_window_formula_count']} | {owners} |"
        )
    return "\n".join(lines)


def cases_markdown(cases: list[dict[str, Any]]) -> str:
    """压缩输出极值样本。"""
    if not cases:
        return "无"
    return "; ".join(
        f"P={case['P']}, k={case['k']}, N={case['prime_count']}, "
        f"B={case['B']}, S={case['S']}, fill={case['fill']:.6f}"
        for case in cases
    )


def build_payload() -> dict[str, Any]:
    """生成证书 payload。"""
    sweep = finite_sweep()
    rows = build_rows()
    dependency_hashes = {
        str(path.relative_to(ROOT)): sha256(path)
        for path in DEPENDENCIES
        if path.exists()
    }
    return {
        "status": "strict_k_smooth_slots_refined_to_lpf_owner_quotient_windows",
        "formula": {
            "smooth_owner_window": "S_P(k)=sum_p #{q: kP/p<q<((k+1)P)/p, LPF(q)>=p, LPMax(q)<=P}",
            "high_prime_window": "B_P(k)=sum_m #{prime r>P in Euclidean source window for m}",
            "dual_value": "N_P(k)=(P-1)-B_P(k)-S_P(k)",
            "positivity": "N_P(k)>=1 iff B_P(k)+S_P(k)<=P-2",
        },
        "finite_sweep": sweep,
        "gates": rows,
        "dependency_hashes": dependency_hashes,
        "plain_conclusion": (
            "strict 行的两个合数源域现在都已写成 quotient-window："
            "最大素因子大于 P 的槽来自 Beatty/Euclidean high-prime source windows；"
            "最大素因子不超过 P 的槽来自 LPF-owner 的 rough cofactor windows。"
            "剩余硬点正是这两个窗口源域不能共同铺满目标行。"
        ),
    }


def build_markdown(payload: dict[str, Any]) -> str:
    """生成 Markdown 证书。"""
    sweep = payload["finite_sweep"]
    lines = [
        "# Prime Matrix Phi-LPF strict k smooth owner quotient-window 证书",
        "",
        f"**状态：** `{payload['status']}`",
        "",
        "本层把 `P`-smooth 槽也写成 quotient-window。对 owner prime `p`，令 `n=pq` 落在 strict 行内。",
        "`p` 是 LPF-owner 当且仅当 `q` 为 `p`-rough；该槽是 `P`-smooth 当且仅当 `q` 的最大素因子不超过 `P`。",
        "",
        "```text",
        "S_P(k)=sum_{p<=sqrt((k+1)P-1)} #{ q :",
        "  floor(kP/p)<q<=floor(((k+1)P-1)/p),",
        "  LPF(q)>=p, LPMax(q)<=P }.",
        "```",
        "",
        "结合前一层 high-prime Beatty/Euclidean source windows：",
        "",
        "```text",
        "N_P(k)=(P-1)-B_P(k)-S_P(k),",
        "N_P(k)>=1 iff B_P(k)+S_P(k)<=P-2.",
        "```",
        "",
        "## 1. 有限审计",
        "",
        "```text",
        f"max_prime={sweep['max_prime']}",
        f"strict_row_count={sweep['strict_row_count']}",
        f"all_dual_quotient_window_identities_hold={fmt_bool(sweep['all_dual_quotient_window_identities_hold'])}",
        f"minimum_prime_count={sweep['minimum_prime_count']}",
        f"finite_evidence_not_used_as_global_proof={fmt_bool(sweep['finite_evidence_not_used_as_global_proof'])}",
        "```",
        "",
        "最大 smooth 样本：",
        "",
        "```text",
        cases_markdown(sweep["max_smooth"]["cases"]),
        "```",
        "",
        "最接近双窗口铺满样本：",
        "",
        "```text",
        cases_markdown(sweep["max_dual_fill"]["cases"]),
        "```",
        "",
        "## 2. 样本行",
        "",
        sample_rows_markdown(sweep["sample_rows"]),
        "",
        "## 3. 判定表",
        "",
        rows_markdown(payload["gates"]),
        "",
        "## 4. 结论",
        "",
        payload["plain_conclusion"],
        "",
        "本层关闭的是 smooth 槽源域的 quotient-window 口径，不是双窗口反铺满不等式。",
        "最新剩余仍为 `DualWindowAntiTilingProved`、",
        "`PositiveRejectionExcessForStrictKRawLPFIncidence` 或真正的 `SqrtGapInputAfterX`。",
        "",
        "## 5. 依赖哈希",
        "",
        "| file | sha256 |",
        "| --- | --- |",
    ]
    for path, digest in payload["dependency_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """写出证书文件。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    payload = build_payload()
    text = json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True)
    OUT_LEDGER.write_text(text + "\n", encoding="utf-8")
    OUT_JSON.write_text(text + "\n", encoding="utf-8")
    OUT_MD.write_text(build_markdown(payload), encoding="utf-8")
    print(f"wrote {OUT_LEDGER}")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")


if __name__ == "__main__":
    main()
