#!/usr/bin/env python3
"""生成 1<k<P Phi-LPF 行计数 >=1 与平方根尺度间隙输入的等价证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_strict_k_sqrt_gap_equivalence_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-strict-k-sqrt-gap-equivalence-router.json

输出：
  data/prime-matrix-phi-lpf-strict-k-sqrt-gap-equivalence-ledger.json
  docs/monograph/prime-matrix-phi-lpf-strict-k-sqrt-gap-equivalence-router.json
  docs/monograph/prime-matrix-phi-lpf-strict-k-sqrt-gap-equivalence-router.md
"""

from __future__ import annotations

import hashlib
import json
from math import isqrt, sqrt
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-strict-k-sqrt-gap-equivalence"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

DEPENDENCIES = [
    DOCS / "prime-matrix-phi-lpf-k-less-p-row-interval-difference-router.json",
    DOCS / "prime-matrix-phi-lpf-strict-k-endpoint-bucket-cancellation-router.json",
    DOCS / "prime-matrix-phi-lpf-strict-k-internal-owner-saturation-router.json",
    DOCS / "prime-matrix-phi-lpf-strict-k-raw-rejection-balance-router.json",
    DOCS / "prime-matrix-phi-lpf-strict-k-short-interval-exponent-barrier-router.json",
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


def prime_prefix(n: int) -> list[int]:
    """生成 pi 前缀表，prefix[x]=pi(x)。"""
    sieve = bytearray(b"\x01") * (n + 1)
    if n >= 0:
        sieve[0] = 0
    if n >= 1:
        sieve[1] = 0
    for p in range(2, isqrt(n) + 1):
        if sieve[p]:
            start = p * p
            sieve[start : n + 1 : p] = b"\x00" * (((n - start) // p) + 1)
    prefix = [0] * (n + 1)
    total = 0
    for i in range(n + 1):
        if sieve[i]:
            total += 1
        prefix[i] = total
    return prefix


def row_prime_count(prefix: list[int], p_len: int, k: int) -> int:
    """计算 strict 内部行 (kP, (k+1)P) 的素数数。"""
    left = k * p_len
    right = k * p_len + p_len - 1
    return prefix[right] - prefix[left]


def sample_row(prefix: list[int], p_len: int, k: int) -> dict[str, Any]:
    """生成一条 strict 行的等价审计。"""
    left = k * p_len
    right = k * p_len + p_len - 1
    count = row_prime_count(prefix, p_len, k)
    sqrt_bound = sqrt(left)
    return {
        "P": p_len,
        "k": k,
        "x": left,
        "internal_interval": [left + 1, right],
        "row_prime_count": count,
        "ge_one": count >= 1,
        "sqrt_x_lt_p": sqrt_bound < p_len,
        "sqrt_x": sqrt_bound,
        "p_minus_sqrt_x": p_len - sqrt_bound,
        "conditional_sqrt_gap_would_fit": sqrt_bound < p_len,
    }


def finite_sweep(max_prime: int = 499) -> dict[str, Any]:
    """有限审计 strict 行最小素数数；不作全局证明。"""
    limit = max_prime * max_prime
    prefix = prime_prefix(limit)
    cases = 0
    zero_rows: list[dict[str, int]] = []
    min_count: int | None = None
    min_cases: list[dict[str, int]] = []
    per_prime_min: list[dict[str, int]] = []
    for p_len in [p for p in primes_upto(max_prime) if p >= 3]:
        local_min: int | None = None
        local_min_k: list[int] = []
        for k in range(2, p_len):
            cases += 1
            count = row_prime_count(prefix, p_len, k)
            if count == 0:
                zero_rows.append({"P": p_len, "k": k})
            if min_count is None or count < min_count:
                min_count = count
                min_cases = [{"P": p_len, "k": k, "row_prime_count": count}]
            elif count == min_count and len(min_cases) < 16:
                min_cases.append({"P": p_len, "k": k, "row_prime_count": count})
            if local_min is None or count < local_min:
                local_min = count
                local_min_k = [k]
            elif count == local_min and len(local_min_k) < 6:
                local_min_k.append(k)
        per_prime_min.append(
            {"P": p_len, "min_row_prime_count": local_min or 0, "sample_k": local_min_k}
        )
    return {
        "max_prime": max_prime,
        "case_count": cases,
        "zero_rows_found": zero_rows,
        "minimum_row_prime_count": min_count,
        "minimum_cases": min_cases,
        "all_finite_rows_have_prime": not zero_rows,
        "finite_evidence_not_used_as_global_proof": True,
        "per_prime_min_tail_sample": per_prime_min[-10:],
    }


def build_rows() -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        row(
            "PhiLPFExactIntegerValueAvailable",
            True,
            True,
            "Phi-LPF 端点差分给出 strict 行素数数目的精确整数值。",
            "exact count only",
        ),
        row(
            "GEOneEquivalentToPositiveRejectionExcess",
            True,
            True,
            "该整数 >=1 等价于 raw/rejection 严格失衡。",
            "PositiveRejectionExcessForStrictKRawLPFIncidence",
        ),
        row(
            "GEOneEquivalentToAlignedSqrtGapExclusion",
            True,
            True,
            "行值 >=1 等价于没有完整 P 网格行被连续素数间隙覆盖。",
            "aligned sqrt-scale prime-gap exclusion",
        ),
        row(
            "SqrtGapInputWouldCloseLargeRows",
            True,
            True,
            "若 x 后 sqrt(x) 内总有素数，则因 sqrt(kP)<P，所有充分大 strict 行闭合。",
            "finite verification below threshold",
        ),
        row(
            "FiniteVerificationTemplateIdentified",
            True,
            True,
            "若 sqrt-gap 输入从 X0 起成立，则仅需有限验证 kP<X0 的行。",
            "depends on unproved sqrt-gap input",
        ),
        row(
            "SqrtGapInputProvedInCurrentCorpus",
            False,
            False,
            "当前语料没有无条件证明 x 后 sqrt(x) 内总有素数。",
            "external/internal square-root prime-gap theorem",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本层给出 >=1 的等价和条件闭合模板，不给出无条件正性。",
            "sqrt-gap input or structural rejection-excess proof",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造证书。"""
    prefix = prime_prefix(101 * 101)
    sample_audits = [
        sample_row(prefix, 5, 4),
        sample_row(prefix, 11, 10),
        sample_row(prefix, 17, 16),
        sample_row(prefix, 101, 50),
        sample_row(prefix, 101, 100),
    ]
    dependency_hashes = {
        str(path.relative_to(ROOT)): sha256(path) for path in DEPENDENCIES if path.exists()
    }
    return {
        "certificate_type": "prime_matrix_phi_lpf_strict_k_sqrt_gap_equivalence_router",
        "status": "strict_k_phi_lpf_ge_one_reduced_to_sqrt_gap_or_rejection_excess",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "strict_k_range": "1<k<P",
        "endpoint_difference_exact_integer_value_proved": True,
        "ge_one_equivalent_to_positive_rejection_excess_proved": True,
        "ge_one_equivalent_to_aligned_sqrt_gap_exclusion_proved": True,
        "sqrt_gap_input_would_close_all_large_strict_rows": True,
        "finite_verification_template_after_sqrt_gap_input_proved": True,
        "sqrt_gap_input_proved_in_current_corpus": False,
        "row_column_unconditional_closed": False,
        "phi_lpf_count_formula": "N_P(k)=pi((k+1)P-1)-pi(kP)",
        "ge_one_condition": "N_P(k)>=1 iff next_prime(kP)<(k+1)P",
        "sqrt_gap_conditional": (
            "If every x>=X0 has a prime in (x,x+sqrt(x)], then all strict rows "
            "with kP>=X0 have N_P(k)>=1 because sqrt(kP)<P."
        ),
        "finite_verification_residual": (
            "The remaining rows under that hypothesis satisfy kP<X0; since k>=2, "
            "only P<X0/2 must be checked."
        ),
        "sample_audits": sample_audits,
        "finite_sweep": finite_sweep(),
        "gates": build_rows(),
        "source_hashes": {
            str(Path(__file__).resolve().relative_to(ROOT)): sha256(Path(__file__).resolve()),
            **dependency_hashes,
        },
        "plain_conclusion": (
            "Phi-LPF 端点差分确实给出 strict 1<k<P 行的精确素数个数。"
            "要把该值证明为 >=1，等价于排除一个 P 网格对齐的平方根尺度素数荒漠，"
            "也等价于证明 raw/rejection 的严格正失衡。若未来给出 x 后 sqrt(x) 内必有素数"
            "的输入，则充分大部分立即闭合，剩余可有限验证；当前该 sqrt-gap 输入仍未证明。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF strict k sqrt gap equivalence 证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "## 1. >=1 的精确等价",
        "",
        "```text",
        result["phi_lpf_count_formula"],
        result["ge_one_condition"],
        "```",
        "",
        "由于 `1<k<P`，闭区间两个端点 `kP` 与 `(k+1)P` 都是合数，",
        "所以 `>=1` 完全等价于开行 `(kP,(k+1)P)` 中存在素数。",
        "",
        "## 2. sqrt-gap 条件闭合模板",
        "",
        "```text",
        result["sqrt_gap_conditional"],
        result["finite_verification_residual"],
        "```",
        "",
        "注意这里需要的是 `x` 后的平方根尺度间隙输入，而不是普通 `theta>1/2` 的短区间输入。",
        "",
        "## 3. 样本审计",
        "",
        "| P | k | x=kP | interval | row prime count | sqrt(x)<P | P-sqrt(x) |",
        "| ---: | ---: | ---: | --- | ---: | --- | ---: |",
    ]
    for item in result["sample_audits"]:
        lines.append(
            f"| {item['P']} | {item['k']} | {item['x']} | {item['internal_interval']} | "
            f"{item['row_prime_count']} | `{fmt_bool(item['sqrt_x_lt_p'])}` | "
            f"{item['p_minus_sqrt_x']:.6f} |"
        )
    sweep = result["finite_sweep"]
    lines.extend(
        [
            "",
            "## 4. 有限审计边界",
            "",
            "```text",
            f"max_prime={sweep['max_prime']}",
            f"case_count={sweep['case_count']}",
            f"all_finite_rows_have_prime={fmt_bool(sweep['all_finite_rows_have_prime'])}",
            f"zero_rows_found={sweep['zero_rows_found']}",
            f"minimum_row_prime_count={sweep['minimum_row_prime_count']}",
            "finite_evidence_not_used_as_global_proof=true",
            "```",
            "",
            "最小行素数数样本：",
            "",
            "| P | k | row prime count |",
            "| ---: | ---: | ---: |",
        ]
    )
    for item in sweep["minimum_cases"]:
        lines.append(f"| {item['P']} | {item['k']} | {item['row_prime_count']} |")
    lines.extend(
        [
            "",
            "尾部 P 的最小值样本：",
            "",
            "| P | min row prime count | sample k |",
            "| ---: | ---: | --- |",
        ]
    )
    for item in sweep["per_prime_min_tail_sample"]:
        lines.append(f"| {item['P']} | {item['min_row_prime_count']} | `{item['sample_k']}` |")
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
            f"| `{cell(item['gate'])}` | `{fmt_bool(item['closed'])}` | `{fmt_bool(item['proved'])}` | "
            f"{cell(item['meaning'])} | {cell(item['remaining'])} |"
        )
    lines.extend(
        [
            "",
            "## 6. 结论",
            "",
            "Phi-LPF 可以计算出行素数个数这个整数，但 `>=1` 的证明不能从恒等式自身推出。",
            "当前最清楚的闭合模板是：先证明平方根尺度 prime-gap 输入，再做有限验证。",
            "在没有该输入时，非循环主攻仍应回到 `PositiveRejectionExcessForStrictKRawLPFIncidence`。",
            "",
            "## 7. 依赖哈希",
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
