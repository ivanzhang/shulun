#!/usr/bin/env python3
"""生成 1<k<P 行区间的 Phi-LPF 端点差分证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_k_less_p_row_interval_difference_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-k-less-p-row-interval-difference-router.json

输出：
  data/prime-matrix-phi-lpf-k-less-p-row-interval-difference-ledger.json
  docs/monograph/prime-matrix-phi-lpf-k-less-p-row-interval-difference-router.json
  docs/monograph/prime-matrix-phi-lpf-k-less-p-row-interval-difference-router.md
"""

from __future__ import annotations

from functools import cache
import hashlib
import json
from math import isqrt
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-k-less-p-row-interval-difference"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

DEPENDENCIES = [
    DOCS / "prime-matrix-phi-lpf-endpoint-interval-difference-router.json",
    DOCS / "prime-matrix-row-gap-supply-phase-cycle-cut-router.json",
    DOCS / "prime-matrix-lowroot-sifted-deficit-frontier-router.json",
    DOCS / "prime-matrix-short-interval-rough-residue-barrier-router.json",
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


def primes_upto(n: int) -> list[int]:
    """返回不超过 n 的素数。"""
    if n < 2:
        return []
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, isqrt(n) + 1):
        if sieve[p]:
            start = p * p
            sieve[start : n + 1 : p] = b"\x00" * (((n - start) // p) + 1)
    return [i for i in range(2, n + 1) if sieve[i]]


def spf_upto(n: int) -> list[int]:
    """返回最小素因子表；spf[1]=1。"""
    spf = list(range(n + 1))
    if n >= 0:
        spf[0] = 0
    if n >= 1:
        spf[1] = 1
    for p in range(2, isqrt(n) + 1):
        if spf[p] == p:
            for m in range(p * p, n + 1, p):
                if spf[m] == m:
                    spf[m] = p
    return spf


def phi_count_by_spf(x: int, p: int, spf: list[int]) -> int:
    """用 LPF 表计算 Phi(x,p)。"""
    if x <= 0:
        return 0
    return sum(1 for n in range(1, x + 1) if n == 1 or spf[n] >= p)


def phi_count_by_recurrence(x: int, p: int) -> int:
    """用 Phi(x,p_j)=Phi(x,p_{j+1})+Phi(floor(x/p_j),p_j) 递推计算。"""
    if x <= 0:
        return 0
    primes = primes_upto(x)
    if p > x:
        return 1
    try:
        start_index = primes.index(p)
    except ValueError as exc:
        raise ValueError("p 必须是素数") from exc

    @cache
    def rec(y: int, index: int) -> int:
        if y <= 0:
            return 0
        if y == 1 or index >= len(primes) or primes[index] > y:
            return 1
        q = primes[index]
        return rec(y, index + 1) + rec(y // q, index)

    return rec(x, start_index)


def prime_count_direct(a: int, b: int, spf: list[int]) -> int:
    """直接数闭区间 [a,b] 内的素数。"""
    return sum(1 for n in range(max(2, a), b + 1) if spf[n] == n)


def lpf_endpoint_interval_count(a: int, b: int) -> dict[str, Any]:
    """用 Phi-LPF 端点差分精确计算闭区间 [a,b] 内素数个数。"""
    if a < 2 or b < a:
        raise ValueError("本证书只审计 2<=a<=b 的闭区间")
    spf = spf_upto(b)
    bucket_rows: list[dict[str, int]] = []
    composite_delta = 0
    for p in primes_upto(isqrt(b)):
        right = phi_count_by_spf(b // p, p, spf)
        left = phi_count_by_spf((a - 1) // p, p, spf)
        delta = right - left
        if delta:
            bucket_rows.append(
                {
                    "p": p,
                    "right_phi": right,
                    "left_phi": left,
                    "delta": delta,
                }
            )
        composite_delta += delta
    length = b - a + 1
    formula_count = length - composite_delta
    direct_count = prime_count_direct(a, b, spf)
    return {
        "a": a,
        "b": b,
        "length": length,
        "root_bound": isqrt(b),
        "composite_count_by_lpf_endpoint_difference": composite_delta,
        "prime_count_by_endpoint_difference": formula_count,
        "prime_count_direct": direct_count,
        "formula_matches_direct": formula_count == direct_count,
        "positive_from_identity_condition": f"{composite_delta} < {length}",
        "nonzero_bucket_deltas": bucket_rows,
    }


def row_internal_audit(p_len: int, k: int) -> dict[str, Any]:
    """审计 1<k<P 时内部行 I_k={kP+a:1<=a<P}。"""
    if not (1 < k < p_len):
        raise ValueError("本证书要求 1<k<P")
    a = k * p_len + 1
    b = k * p_len + p_len - 1
    audit = lpf_endpoint_interval_count(a, b)
    spf = spf_upto(b)
    root_primes = primes_upto(isqrt(b))
    uncovered: list[int] = []
    primes: list[int] = []
    for slot in range(1, p_len):
        n = k * p_len + slot
        if all(n % q != 0 for q in root_primes):
            uncovered.append(slot)
        if spf[n] == n:
            primes.append(slot)
    audit.update(
        {
            "P": p_len,
            "k": k,
            "row_internal_interval": [a, b],
            "inside_p_square": b < p_len * p_len,
            "uncovered_slots_by_full_root": uncovered,
            "prime_slots": primes,
            "full_root_uncovered_equals_prime_slots": uncovered == primes,
            "row_prime_positive": bool(primes),
        }
    )
    return audit


def closed_kp_interval_audit(p_len: int, k: int) -> dict[str, Any]:
    """审计闭区间 [kP,kP+P]，保留端点倍数信息。"""
    if not (1 < k < p_len):
        raise ValueError("本证书要求 1<k<P")
    a = k * p_len
    b = k * p_len + p_len
    audit = lpf_endpoint_interval_count(a, b)
    internal = lpf_endpoint_interval_count(a + 1, b - 1)
    audit.update(
        {
            "P": p_len,
            "k": k,
            "closed_interval": [a, b],
            "internal_interval": [a + 1, b - 1],
            "left_endpoint_is_composite_multiple_of_P": True,
            "right_endpoint_is_composite_multiple_of_P": True,
            "closed_count_equals_internal_row_count": (
                audit["prime_count_by_endpoint_difference"]
                == internal["prime_count_by_endpoint_difference"]
                == internal["prime_count_direct"]
            ),
            "internal_prime_count": internal["prime_count_by_endpoint_difference"],
        }
    )
    return audit


def recurrence_sample(p_len: int, k: int) -> dict[str, Any]:
    """给出 Phi 递推与 LPF 计数一致的桶级样本。"""
    a = k * p_len + 1
    b = k * p_len + p_len - 1
    spf = spf_upto(b)
    rows = []
    for p in primes_upto(isqrt(b)):
        right_x = b // p
        left_x = (a - 1) // p
        right_spf = phi_count_by_spf(right_x, p, spf)
        left_spf = phi_count_by_spf(left_x, p, spf)
        right_rec = phi_count_by_recurrence(right_x, p)
        left_rec = phi_count_by_recurrence(left_x, p)
        rows.append(
            {
                "p": p,
                "right_x": right_x,
                "left_x": left_x,
                "right_phi_spf": right_spf,
                "right_phi_recurrence": right_rec,
                "left_phi_spf": left_spf,
                "left_phi_recurrence": left_rec,
                "delta": right_rec - left_rec,
                "recurrence_matches_lpf_count": right_rec == right_spf and left_rec == left_spf,
            }
        )
    return {
        "P": p_len,
        "k": k,
        "interval": [a, b],
        "all_bucket_recurrence_matches_lpf_count": all(
            item["recurrence_matches_lpf_count"] for item in rows
        ),
        "bucket_rows": rows,
    }


def finite_k_less_p_sweep(max_prime: int = 97) -> dict[str, Any]:
    """做小范围有限审计；该数据只作验证，不作全局证明。"""
    cases = []
    all_positive = True
    all_equivalent = True
    min_prime_count: int | None = None
    min_cases: list[dict[str, int]] = []
    for p_len in [p for p in primes_upto(max_prime) if p >= 3]:
        spf = spf_upto(p_len * p_len)
        root_primes_all = primes_upto(p_len)
        for k in range(2, p_len):
            a = k * p_len + 1
            b = k * p_len + p_len - 1
            root = isqrt(b)
            roots = [q for q in root_primes_all if q <= root]
            prime_slots = [slot for slot in range(1, p_len) if spf[k * p_len + slot] == k * p_len + slot]
            uncovered = [
                slot
                for slot in range(1, p_len)
                if all((k * p_len + slot) % q != 0 for q in roots)
            ]
            count = len(prime_slots)
            all_positive = all_positive and count > 0
            all_equivalent = all_equivalent and uncovered == prime_slots
            if min_prime_count is None or count < min_prime_count:
                min_prime_count = count
                min_cases = [{"P": p_len, "k": k, "prime_count": count, "a": a, "b": b}]
            elif count == min_prime_count and len(min_cases) < 12:
                min_cases.append({"P": p_len, "k": k, "prime_count": count, "a": a, "b": b})
            cases.append((p_len, k))
    return {
        "max_prime": max_prime,
        "case_count": len(cases),
        "all_internal_rows_positive_in_finite_sweep": all_positive,
        "all_full_root_uncovered_equals_prime_slots": all_equivalent,
        "minimum_prime_count": min_prime_count,
        "minimum_cases_sample": min_cases,
        "finite_evidence_not_used_as_global_proof": True,
    }


def build_rows() -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        row(
            "KLessPEndpointDifferenceIdentityClosed",
            True,
            True,
            "端点差分恒等式对任意 2<=A<=B 成立，因此也适用于 1<k<P 的 [kP,kP+P]。",
            "exact identity",
        ),
        row(
            "StrictKClosedEqualsInternalRow",
            True,
            True,
            "当 1<k<P 时，kP 与 kP+P=(k+1)P 都是合数端点，闭区间素数数目等于内部行素数数目。",
            "endpoints contribute zero primes",
        ),
        row(
            "InternalRowFormulaClosed",
            True,
            True,
            "对 I_k={kP+a:1<=a<P}，素数数目等于 P-1 减去 full-root LPF 桶端点增量和。",
            "pi(kP+P-1)-pi(kP)",
        ),
        row(
            "PhiRecurrenceComputesBucketDeltas",
            True,
            True,
            "Phi 递推可机械计算每个桶端点值，样本与 LPF 直接计数一致。",
            "recurrence, not asymptotic",
        ),
        row(
            "InsidePSquarePrimeUncoveredEquivalence",
            True,
            True,
            "因为 1<k<P 且 1<=a<P，所以 kP+a<P^2；full-root 未覆盖槽等价于素数槽。",
            "uncovered iff prime",
        ),
        row(
            "PreviousCRTPrimeFreeBlockApplicableToKLessP",
            False,
            False,
            "上一层 P=5,k=8166 的全合数闭区间样本满足 k>P，不能否定 k<P 行区间目标。",
            "need k<P-specific argument",
        ),
        row(
            "IntervalPositivityFromIdentityAlone",
            False,
            False,
            "要推出行内有素数，仍需证明 LPF 合数桶增量和小于 P-1。",
            "composite bucket delta < row length",
        ),
        row(
            "FullRootUncoveredSlotPositiveProved",
            False,
            False,
            "正性就是 full-root 未覆盖槽存在；这与 row-prime 目标等价，不能作为内部黑箱。",
            "noncircular short-interval input still missing",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本层只把 1<k<P 的 Phi-LPF 行差分完全规范化；未证明行/列命题无条件闭合。",
            "Q1/Q2 transport, seed/PDEC scope, signed table, Rate, DStructure",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造证书。"""
    sample_rows = [row_internal_audit(5, 4), row_internal_audit(11, 10), row_internal_audit(101, 100)]
    closed_samples = [closed_kp_interval_audit(5, 4), closed_kp_interval_audit(11, 10)]
    recurrence = recurrence_sample(17, 16)
    sweep = finite_k_less_p_sweep()
    dependency_hashes = {
        str(path.relative_to(ROOT)): sha256(path) for path in DEPENDENCIES if path.exists()
    }
    return {
        "certificate_type": "prime_matrix_phi_lpf_k_less_p_row_interval_difference_router",
        "status": "k_less_p_phi_lpf_row_interval_difference_closed_but_row_positivity_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "strict_k_range": "1<k<P",
        "k_less_p_endpoint_difference_identity_proved": True,
        "strict_k_closed_interval_equals_internal_row_proved": True,
        "internal_row_formula_proved": True,
        "phi_recurrence_computes_bucket_deltas": True,
        "inside_p_square_prime_uncovered_equivalence_proved": True,
        "previous_crt_prime_free_block_not_applicable": True,
        "interval_positivity_from_identity_alone_proved": False,
        "full_root_uncovered_slot_positive_proved": False,
        "row_column_unconditional_closed": False,
        "closed_kp_interval_formula_for_1_less_k_less_p": (
            "pi(kP+P)-pi(kP-1)=P+1-sum_{p<=sqrt(kP+P)}"
            "[Phi(floor((kP+P)/p),p)-Phi(floor((kP-1)/p),p)]"
        ),
        "internal_row_interval_formula": (
            "pi(kP+P-1)-pi(kP)=(P-1)-sum_{p<=sqrt(kP+P-1)}"
            "[Phi(floor((kP+P-1)/p),p)-Phi(floor(kP/p),p)]"
        ),
        "positive_row_condition": (
            "sum_{p<=sqrt(kP+P-1)}[Phi(floor((kP+P-1)/p),p)-Phi(floor(kP/p),p)] < P-1"
        ),
        "phi_recurrence": "Phi(x,p_j)=Phi(x,p_{j+1})+Phi(floor(x/p_j),p_j)",
        "closed_equals_internal_row_for_1_less_k_less_p": True,
        "sample_internal_rows": sample_rows,
        "sample_closed_kp_intervals": closed_samples,
        "recurrence_sample": recurrence,
        "finite_sweep": sweep,
        "gates": build_rows(),
        "source_hashes": {
            str(Path(__file__).resolve().relative_to(ROOT)): sha256(Path(__file__).resolve()),
            **dependency_hashes,
        },
        "plain_conclusion": (
            "对 1<k<P，Phi-LPF 端点差分能直接用于闭区间 [kP,kP+P]。"
            "由于两个端点 kP 与 (k+1)P 都是合数倍，闭区间素数数目恰等于内部行 "
            "I_k={kP+a:1<=a<P} 的素数数目。它给出逐行素数个数的精确值。"
            "但要证明该值为正，必须证明 LPF 合数桶端点增量和小于 P-1；"
            "在 1<k<P 时这等价于 full-root 未覆盖槽存在，也就是行内已有素数。"
            "因此本层是精确计数闭合和循环边界定位，不是行/列命题的无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF 1<k<P row interval difference 证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "## 1. 两个端点公式",
        "",
        "闭区间 `[kP,kP+P]`，其中 `1<k<P`：",
        "",
        "```text",
        result["closed_kp_interval_formula_for_1_less_k_less_p"],
        "```",
        "",
        "内部行 `I_k={kP+a:1<=a<P}`：",
        "",
        "```text",
        result["internal_row_interval_formula"],
        "```",
        "",
        "正性需要证明：",
        "",
        "```text",
        result["positive_row_condition"],
        "```",
        "",
        "Phi 递推读法：",
        "",
        "```text",
        result["phi_recurrence"],
        "```",
        "",
        "因为 `kP` 与 `(k+1)P` 在 `1<k<P` 时都是合数，闭区间计数与内部行计数相同：",
        "",
        "```text",
        "pi(kP+P)-pi(kP-1)=pi(kP+P-1)-pi(kP)",
        "```",
        "",
        "## 2. k<P 的额外等价",
        "",
        "当 `1<k<P` 且 `1<=a<P` 时，`kP+a<P^2`。因此若 `kP+a` 没有任何",
        "`q<=sqrt(kP+P-1)` 的素因子覆盖，它不可能是合数，只能是素数。反过来素数槽当然未被这些",
        "根内素数覆盖。所以 full-root uncovered slots 与 row prime slots 完全相同。",
        "",
        "上一层 CRT 样本 `P=5,k=8166` 的确说明一般 `[kP,kP+P]` 全称命题为假；但该样本",
        "满足 `k>P`，不能用于否定本层 `k<P` 行区间目标。",
        "",
        "## 3. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in result["gates"]:
        lines.append(
            f"| `{cell(item['gate'])}` | `{fmt_bool(item['closed'])}` | `{fmt_bool(item['proved'])}` | "
            f"{cell(item['meaning'])} | {cell(item['remaining'])} |"
        )
    lines.extend(
        [
            "",
            "## 4. 内部行样本",
            "",
            "| P | k | interval | length | LPF composite delta | endpoint prime count | direct prime count | uncovered=prime |",
            "| ---: | ---: | --- | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for audit in result["sample_internal_rows"]:
        lines.append(
            f"| {audit['P']} | {audit['k']} | [{audit['a']},{audit['b']}] | "
            f"{audit['length']} | {audit['composite_count_by_lpf_endpoint_difference']} | "
            f"{audit['prime_count_by_endpoint_difference']} | {audit['prime_count_direct']} | "
            f"`{fmt_bool(audit['full_root_uncovered_equals_prime_slots'])}` |"
        )
    lines.extend(
        [
            "",
            "## 5. 闭区间端点样本",
            "",
            "| P | k | interval | length | endpoint prime count | internal prime count | closed=internal |",
            "| ---: | ---: | --- | ---: | ---: | ---: | --- |",
        ]
    )
    for audit in result["sample_closed_kp_intervals"]:
        lines.append(
            f"| {audit['P']} | {audit['k']} | [{audit['a']},{audit['b']}] | "
            f"{audit['length']} | {audit['prime_count_by_endpoint_difference']} | "
            f"{audit['internal_prime_count']} | `{fmt_bool(audit['closed_count_equals_internal_row_count'])}` |"
        )
    rec = result["recurrence_sample"]
    lines.extend(
        [
            "",
            "## 6. Phi 递推样本",
            "",
            f"`P={rec['P']}, k={rec['k']}, interval={rec['interval']}`",
            "",
            f"`all_bucket_recurrence_matches_lpf_count={fmt_bool(rec['all_bucket_recurrence_matches_lpf_count'])}`",
            "",
            "| p | left x | right x | delta | recurrence ok |",
            "| ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for item in rec["bucket_rows"]:
        lines.append(
            f"| {item['p']} | {item['left_x']} | {item['right_x']} | {item['delta']} | "
            f"`{fmt_bool(item['recurrence_matches_lpf_count'])}` |"
        )
    sweep = result["finite_sweep"]
    lines.extend(
        [
            "",
            "## 7. 有限审计边界",
            "",
            "```text",
            f"max_prime={sweep['max_prime']}",
            f"case_count={sweep['case_count']}",
            f"all_internal_rows_positive_in_finite_sweep={fmt_bool(sweep['all_internal_rows_positive_in_finite_sweep'])}",
            f"all_full_root_uncovered_equals_prime_slots={fmt_bool(sweep['all_full_root_uncovered_equals_prime_slots'])}",
            f"minimum_prime_count={sweep['minimum_prime_count']}",
            "finite_evidence_not_used_as_global_proof=true",
            "```",
            "",
            "最小样本行：",
            "",
            "| P | k | interval | prime count |",
            "| ---: | ---: | --- | ---: |",
        ]
    )
    for item in sweep["minimum_cases_sample"]:
        lines.append(
            f"| {item['P']} | {item['k']} | [{item['a']},{item['b']}] | {item['prime_count']} |"
        )
    lines.extend(
        [
            "",
            "## 8. 结论",
            "",
            "Phi-LPF 端点差分在 `1<k<P` 行内已经完全可用：它给出精确素数个数值，并可由 Phi 递推机械计算。",
            "剩余硬点被压成一个清晰不等式：LPF 合数桶端点增量和必须小于 `P-1`。",
            "但这个不等式在 `1<k<P` 行内等价于 full-root 未覆盖槽存在，也等价于行内有素数。",
            "因此它不能作为非循环内部黑箱；下一步仍需从 Q1/Q2 传输、seed/PDEC 作用域、signed table 或外部短区间输入中突破。",
            "",
            "## 9. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in result["source_hashes"].items():
        lines.append(f"| `{cell(path)}` | `{digest}` |")
    return "\n".join(lines) + "\n"


def main() -> None:
    """写出 ledger、JSON 与 Markdown 证书。"""
    result = build_result()
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    text = json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    OUT_LEDGER.write_text(text, encoding="utf-8")
    OUT_JSON.write_text(text, encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(OUT_LEDGER.relative_to(ROOT))
    print(OUT_JSON.relative_to(ROOT))
    print(OUT_MD.relative_to(ROOT))


if __name__ == "__main__":
    main()
