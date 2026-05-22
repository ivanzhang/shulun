#!/usr/bin/env python3
"""生成 strict 行 Beatty payment 的欧几里得商源行窗口证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_strict_k_beatty_euclidean_source_window_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-strict-k-beatty-euclidean-source-window-router.json

输出：
  data/prime-matrix-phi-lpf-strict-k-beatty-euclidean-source-window-ledger.json
  docs/monograph/prime-matrix-phi-lpf-strict-k-beatty-euclidean-source-window-router.json
  docs/monograph/prime-matrix-phi-lpf-strict-k-beatty-euclidean-source-window-router.md
"""

from __future__ import annotations

from array import array
from collections import Counter
import hashlib
import json
from math import isqrt
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-strict-k-beatty-euclidean-source-window"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

DEPENDENCIES = [
    DOCS / "prime-matrix-phi-lpf-strict-k-payment-beatty-source-map-router.json",
    DOCS / "prime-matrix-phi-lpf-strict-k-endpoint-beatty-smooth-value-router.json",
    DOCS / "prime-matrix-phi-lpf-strict-k-low-carrier-lower-half-source-cut-router.json",
]


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """把布尔值格式化为小写文本。"""
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


def h_m_sum(prefix: array, p_len: int, k: int) -> int:
    """按 H_m 定义计算 low-carrier payment 总量。"""
    lower = k * p_len
    upper = (k + 1) * p_len - 1
    total = 0
    for m in range(2, k + 1):
        total += pi_between(prefix, lower // m, upper // m)
    return total


def source_window_for_carrier(p_len: int, k: int, m: int) -> dict[str, int]:
    """把 carrier m 转成欧几里得商源行窗口。"""
    j = k // m
    t = k - m * j
    lower_b = (t * p_len) // m + 1
    upper_b = (((t + 1) * p_len) - 1) // m
    return {
        "m": m,
        "source_row": j,
        "residue_t": t,
        "lower_b": lower_b,
        "upper_b": upper_b,
        "source_left_exclusive": j * p_len + lower_b - 1,
        "source_right_inclusive": j * p_len + upper_b,
        "window_width": max(0, upper_b - lower_b + 1),
    }


def quotient_window_payment(prefix: array, p_len: int, k: int) -> dict[str, Any]:
    """按欧几里得商源行窗口计算 payment，并记录源行分布。"""
    total = 0
    source_hist: Counter[int] = Counter()
    carrier_rows: list[dict[str, int]] = []
    nonempty_windows = 0
    max_window_width = 0
    for m in range(2, k + 1):
        window = source_window_for_carrier(p_len, k, m)
        count = pi_between(
            prefix,
            window["source_left_exclusive"],
            window["source_right_inclusive"],
        )
        window["prime_count"] = count
        total += count
        if count:
            nonempty_windows += 1
            source_hist[window["source_row"]] += count
        max_window_width = max(max_window_width, window["window_width"])
        if len(carrier_rows) < 16 or count:
            carrier_rows.append(window)
    return {
        "quotient_window_payment_count": total,
        "source_histogram": {str(key): source_hist[key] for key in sorted(source_hist)},
        "nonempty_windows": nonempty_windows,
        "max_window_width": max_window_width,
        "carrier_window_sample": carrier_rows[:24],
    }


def direct_beatty_slot_count(flags: bytearray, p_len: int, k: int) -> int:
    """直接按目标行高素因子槽计数，用于交叉校验。"""
    lower = k * p_len
    total = 0
    for slot in range(1, p_len):
        n = lower + slot
        # n<P^2，若存在高素因子 r>P，则 cofactor m<=k 且唯一。
        found = False
        for m in range(2, k + 1):
            if n % m == 0:
                r = n // m
                if r > p_len and flags[r]:
                    found = True
                    break
        if found:
            total += 1
    return total


def row_summary(prefix: array, flags: bytearray, p_len: int, k: int) -> dict[str, Any]:
    """汇总一条 strict 行的三种 payment 读法。"""
    hm = h_m_sum(prefix, p_len, k)
    quotient = quotient_window_payment(prefix, p_len, k)
    direct = direct_beatty_slot_count(flags, p_len, k) if p_len <= 101 else None
    source_rows = [int(key) for key in quotient["source_histogram"]]
    max_source_row = max(source_rows) if source_rows else 0
    return {
        "P": p_len,
        "k": k,
        "hm_payment_count": hm,
        "quotient_window_payment_count": quotient["quotient_window_payment_count"],
        "direct_beatty_slot_count": direct,
        "hm_matches_quotient_windows": hm == quotient["quotient_window_payment_count"],
        "direct_matches_when_checked": direct is None or direct == hm,
        "source_rows_all_in_lower_half": max_source_row <= k // 2,
        "max_source_row": max_source_row,
        "source_histogram": quotient["source_histogram"],
        "nonempty_windows": quotient["nonempty_windows"],
        "max_window_width": quotient["max_window_width"],
        "carrier_window_sample": quotient["carrier_window_sample"],
    }


def finite_sweep(max_prime: int = 1009) -> dict[str, Any]:
    """有限审计欧几里得商源行窗口；不作为全局证明。"""
    flags = prime_sieve(max_prime * max_prime)
    prefix = prime_prefix(flags)
    strict_primes = [p for p in primes_from_flags(flags[: max_prime + 1]) if p >= 5]
    row_count = 0
    failures: list[dict[str, Any]] = []
    lower_half_failures: list[dict[str, Any]] = []
    max_payment = {"value": -1, "cases": []}
    max_nonempty_windows = {"value": -1, "cases": []}
    sample_pairs = [(11, 10), (101, 50), (101, 100), (571, 438), (1009, 1008)]

    for p_len in strict_primes:
        for k in range(2, p_len):
            row_count += 1
            summary = row_summary(prefix, flags, p_len, k)
            if not (
                summary["hm_matches_quotient_windows"]
                and summary["direct_matches_when_checked"]
            ) and len(failures) < 8:
                failures.append(summary)
            if not summary["source_rows_all_in_lower_half"] and len(lower_half_failures) < 8:
                lower_half_failures.append(summary)
            case = {
                "P": p_len,
                "k": k,
                "payment": summary["hm_payment_count"],
                "nonempty_windows": summary["nonempty_windows"],
                "max_source_row": summary["max_source_row"],
            }
            if summary["hm_payment_count"] > max_payment["value"]:
                max_payment = {"value": summary["hm_payment_count"], "cases": [case]}
            elif summary["hm_payment_count"] == max_payment["value"] and len(max_payment["cases"]) < 8:
                max_payment["cases"].append(case)
            if summary["nonempty_windows"] > max_nonempty_windows["value"]:
                max_nonempty_windows = {"value": summary["nonempty_windows"], "cases": [case]}
            elif (
                summary["nonempty_windows"] == max_nonempty_windows["value"]
                and len(max_nonempty_windows["cases"]) < 8
            ):
                max_nonempty_windows["cases"].append(case)

    sample_rows = [row_summary(prefix, flags, p, k) for p, k in sample_pairs]
    return {
        "max_prime": max_prime,
        "strict_row_count": row_count,
        "all_hm_counts_match_quotient_source_windows": not failures,
        "all_source_rows_in_lower_half": not lower_half_failures,
        "failures": failures,
        "lower_half_failures": lower_half_failures,
        "max_payment": max_payment,
        "max_nonempty_windows": max_nonempty_windows,
        "sample_rows": sample_rows,
        "finite_evidence_not_used_as_global_proof": True,
    }


def build_rows() -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        row(
            "EuclideanSourceRowLawClosed",
            True,
            True,
            "若 carrier 为 m，则源素数 r 必在源行 j=floor(k/m)。",
            "exact quotient source row",
        ),
        row(
            "ResidueWindowLawClosed",
            True,
            True,
            "写 k=mj+t 后，源行余数 b 必满足 tP < mb < (t+1)P。",
            "rational residue window",
        ),
        row(
            "BeattyPaymentEqualsQuotientWindowPrimeCountClosed",
            True,
            True,
            "B_P(k) 等于所有欧几里得商源行窗口中的素数计数之和。",
            "source-window payment table",
        ),
        row(
            "LowerHalfSourceCutRefined",
            True,
            True,
            "j=floor(k/m)<=floor(k/2)，所以下半源切口是该商行定律的直接推论。",
            "lower-half source is quotient law",
        ),
        row(
            "BeattySmoothAntiTilingProved",
            False,
            False,
            "本层没有证明这些源行窗口与 P-smooth 槽不能共同铺满目标行。",
            "source-window/smooth anti-tiling inequality",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本层细化 payment 来源，不证明 strict 行正性。",
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
        "| P | k | H_m payment | quotient windows | nonempty windows | max source row | source histogram |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for item in sample_rows:
        hist = ", ".join(f"{key}:{value}" for key, value in list(item["source_histogram"].items())[:8])
        lines.append(
            f"| {item['P']} | {item['k']} | {item['hm_payment_count']} | "
            f"{item['quotient_window_payment_count']} | {item['nonempty_windows']} | "
            f"{item['max_source_row']} | {hist} |"
        )
    return "\n".join(lines)


def cases_markdown(cases: list[dict[str, Any]]) -> str:
    """压缩输出极值样本。"""
    if not cases:
        return "无"
    return "; ".join(
        f"P={case['P']}, k={case['k']}, payment={case['payment']}, "
        f"nonempty_windows={case['nonempty_windows']}, max_source_row={case['max_source_row']}"
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
        "status": "strict_k_beatty_payment_refined_to_euclidean_quotient_source_windows",
        "formula": {
            "carrier_source_row": "j=floor(k/m)",
            "residue_decomposition": "k=mj+t, 0<=t<m, r=jP+b",
            "source_window": "tP < m b < (t+1)P",
            "integer_window": "floor(tP/m)+1 <= b <= floor(((t+1)P-1)/m)",
            "payment_count": "B_P(k)=sum_{m=2}^k #{prime r=jP+b in the source window}",
        },
        "finite_sweep": sweep,
        "gates": rows,
        "dependency_hashes": dependency_hashes,
        "plain_conclusion": (
            "Beatty payment 源表进一步等价于欧几里得商源行窗口表："
            "每个 carrier m 只读取早期源行 floor(k/m) 的一个短有理窗口。"
            "这把反铺满硬点从抽象的 Beatty 源像改写为早期源行窗口供给与 P-smooth 槽的耦合不等式。"
        ),
    }


def build_markdown(payload: dict[str, Any]) -> str:
    """生成 Markdown 证书。"""
    sweep = payload["finite_sweep"]
    lines = [
        "# Prime Matrix Phi-LPF strict k Beatty Euclidean source-window 证书",
        "",
        f"**状态：** `{payload['status']}`",
        "",
        "本层把 Beatty payment 源表继续展开为欧几里得商源行窗口。若目标行为 `k`，carrier 为 `m`，",
        "写：",
        "",
        "```text",
        "j=floor(k/m),  k=mj+t, 0<=t<m,  r=jP+b.",
        "```",
        "",
        "则 payment 条件等价于：",
        "",
        "```text",
        "tP < m b < (t+1)P",
        "floor(tP/m)+1 <= b <= floor(((t+1)P-1)/m).",
        "```",
        "",
        "所以",
        "",
        "```text",
        "B_P(k)=sum_{2<=m<=k} #{ prime r=jP+b in the corresponding source window }.",
        "```",
        "",
        "这比“下半源”更精确：下半源界只是 `j=floor(k/m)<=floor(k/2)` 的推论。",
        "",
        "## 1. 有限审计",
        "",
        "```text",
        f"max_prime={sweep['max_prime']}",
        f"strict_row_count={sweep['strict_row_count']}",
        f"all_hm_counts_match_quotient_source_windows={fmt_bool(sweep['all_hm_counts_match_quotient_source_windows'])}",
        f"all_source_rows_in_lower_half={fmt_bool(sweep['all_source_rows_in_lower_half'])}",
        f"finite_evidence_not_used_as_global_proof={fmt_bool(sweep['finite_evidence_not_used_as_global_proof'])}",
        "```",
        "",
        "最大 payment 样本：",
        "",
        "```text",
        cases_markdown(sweep["max_payment"]["cases"]),
        "```",
        "",
        "最大非空源窗口数样本：",
        "",
        "```text",
        cases_markdown(sweep["max_nonempty_windows"]["cases"]),
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
        "本层关闭的是 payment 源行与源窗口的选择自由；它没有证明这些源窗口供给与 `P`-smooth 槽不能铺满。",
        "最新剩余仍是 `BeattySmoothAntiTilingInequality`、",
        "`PositiveRejectionExcessForStrictKRawLPFIncidence` 或 `SqrtGapInputAfterX`。",
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
