#!/usr/bin/env python3
"""生成 strict 1<k<P 的 Phi-LPF 顶行 square-collar 硬核证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_strict_k_top_row_square_collar_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-strict-k-top-row-square-collar-router.json

输出：
  data/prime-matrix-phi-lpf-strict-k-top-row-square-collar-ledger.json
  docs/monograph/prime-matrix-phi-lpf-strict-k-top-row-square-collar-router.json
  docs/monograph/prime-matrix-phi-lpf-strict-k-top-row-square-collar-router.md
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

SLUG = "prime-matrix-phi-lpf-strict-k-top-row-square-collar"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

DEPENDENCIES = [
    DOCS / "prime-matrix-phi-lpf-k-less-p-row-interval-difference-router.json",
    DOCS / "prime-matrix-phi-lpf-strict-k-raw-rejection-balance-router.json",
    DOCS / "prime-matrix-phi-lpf-strict-k-short-interval-exponent-barrier-router.json",
    DOCS / "prime-matrix-phi-lpf-strict-k-sqrt-gap-equivalence-router.json",
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


def top_row_count(flags: bytearray, p_len: int) -> int:
    """计算顶行 (P^2-P, P^2) 中的素数数。"""
    start = p_len * p_len - p_len + 1
    stop = p_len * p_len - 1
    return sum(flags[start : stop + 1])


def sample_audit(flags: bytearray, p_len: int) -> dict[str, Any]:
    """生成一个顶行样本。"""
    x = p_len * (p_len - 1)
    start = x + 1
    stop = p_len * p_len - 1
    count = top_row_count(flags, p_len)
    slack = p_len - sqrt(x)
    return {
        "P": p_len,
        "k": p_len - 1,
        "x": x,
        "internal_interval": [start, stop],
        "row_length": p_len - 1,
        "top_row_prime_count": count,
        "positive": count >= 1,
        "sqrt_x": sqrt(x),
        "p_minus_sqrt_x": slack,
        "critical_margin_between_half_and_one": 0.5 < slack < 1.0,
        "phi_lpf_top_formula": (
            "N_top(P)=P-1-sum_{q<P}[Phi(floor((P^2-1)/q),q)-"
            "Phi(floor((P^2-P)/q),q)]"
        ),
    }


def finite_sweep(max_prime: int = 5003) -> dict[str, Any]:
    """有限审计顶行 square-collar；不作全局证明。"""
    flags = prime_sieve(max_prime * max_prime)
    primes = [p for p in primes_from_flags(flags[: max_prime + 1]) if p >= 3]
    zero_top_rows: list[dict[str, int]] = []
    min_count: int | None = None
    min_cases: list[dict[str, int]] = []
    tail_rows: list[dict[str, Any]] = []
    for p_len in primes:
        count = top_row_count(flags, p_len)
        if count == 0:
            zero_top_rows.append({"P": p_len})
        if min_count is None or count < min_count:
            min_count = count
            min_cases = [{"P": p_len, "top_row_prime_count": count}]
        elif count == min_count and len(min_cases) < 16:
            min_cases.append({"P": p_len, "top_row_prime_count": count})
        if p_len >= max_prime - 200:
            tail_rows.append(
                {
                    "P": p_len,
                    "top_row_prime_count": count,
                    "p_minus_sqrt_p_pminus1": p_len - sqrt(p_len * (p_len - 1)),
                }
            )
    sample_ps = [5, 11, 17, 101, 499, 5003]
    return {
        "max_prime": max_prime,
        "case_count": len(primes),
        "zero_top_rows_found": zero_top_rows,
        "all_top_rows_positive_in_finite_sweep": not zero_top_rows,
        "minimum_top_row_prime_count": min_count,
        "minimum_cases": min_cases,
        "sample_audits": [sample_audit(flags, p) for p in sample_ps],
        "tail_rows_sample": tail_rows[-10:],
        "finite_evidence_not_used_as_global_proof": True,
    }


def build_rows() -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        row(
            "TopRowSpecializationClosed",
            True,
            True,
            "strict k=P-1 行专化为 prime-square 上边界 collar (P^2-P,P^2)。",
            "exact specialization",
        ),
        row(
            "PhiLPFTopRowExactFormulaClosed",
            True,
            True,
            "顶行 Phi-LPF 公式为 pi(P^2-1)-pi(P^2-P) 的精确端点差分。",
            "exact count only",
        ),
        row(
            "TopRowNecessaryHardCoreIdentified",
            True,
            True,
            "全 strict 行正性必须先证明顶行 square-collar 正性。",
            "PrimeSquareUpperCollarPrimeInput",
        ),
        row(
            "TopRowMinimalSqrtSlackClosed",
            True,
            True,
            "在 1<k<P 中，k=P-1 使 P-sqrt(kP) 最小，且该余量位于 (1/2,1)。",
            "critical sqrt margin",
        ),
        row(
            "TopRowPositiveProvedInCurrentCorpus",
            False,
            False,
            "当前语料没有无条件证明每个素数 P 的 (P^2-P,P^2) 内都有素数。",
            "prime-square upper-collar theorem or rejection-excess proof",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本层只提取必要硬核，不证明全部 strict 行正性。",
            "all rows still need sqrt-gap or PositiveRejectionExcess",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造证书。"""
    sweep = finite_sweep()
    dependency_hashes = {
        str(path.relative_to(ROOT)): sha256(path) for path in DEPENDENCIES if path.exists()
    }
    return {
        "certificate_type": "prime_matrix_phi_lpf_strict_k_top_row_square_collar_router",
        "status": "strict_k_top_row_square_collar_hard_core_identified_positive_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "strict_k_range": "1<k<P",
        "top_row_k": "k=P-1",
        "top_row_interval": "(P^2-P,P^2)",
        "top_row_exact_count": "N_top(P)=pi(P^2-1)-pi(P^2-P)",
        "phi_lpf_top_formula": (
            "N_top(P)=P-1-sum_{q<P}[Phi(floor((P^2-1)/q),q)-"
            "Phi(floor((P^2-P)/q),q)]"
        ),
        "top_row_necessary_hard_core_identified": True,
        "top_row_minimal_sqrt_slack_proved": True,
        "top_row_positive_proved_in_current_corpus": False,
        "row_column_unconditional_closed": False,
        "finite_sweep": sweep,
        "gates": build_rows(),
        "source_hashes": {
            str(Path(__file__).resolve().relative_to(ROOT)): sha256(Path(__file__).resolve()),
            **dependency_hashes,
        },
        "plain_conclusion": (
            "在 strict 1<k<P 的全部行中，k=P-1 顶行把 Phi-LPF 正性压到"
            " prime-square 上边界 collar：pi(P^2-1)-pi(P^2-P)>=1。"
            "这是全行正性的必要硬核，且它是 sqrt(kP)<P 余量最小的临界行。"
            "当前语料没有无条件证明每个素数 P 的该 collar 内必有素数；"
            "因此递推正性仍必须来自 prime-square collar 输入、sqrt-gap 输入，"
            "或 raw/rejection 严格失衡证明。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF strict k top row square collar 证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "## 1. 顶行专化",
        "",
        "```text",
        "k=P-1",
        result["top_row_exact_count"],
        result["phi_lpf_top_formula"],
        "```",
        "",
        "这说明任何证明 `1<k<P` 全部行正性的路线，必须先证明每个素数 `P` 的",
        "`(P^2-P,P^2)` 内存在素数。",
        "",
        "## 2. 临界 sqrt 余量",
        "",
        "对 `x=kP`，行长为 `P`。函数 `P-sqrt(kP)` 随 `k` 增大而减小，",
        "所以顶行 `k=P-1` 是平方根尺度余量最小的 strict 行：",
        "",
        "```text",
        "P-sqrt(P(P-1)) = P/(P+sqrt(P(P-1))) in (1/2,1).",
        "```",
        "",
        "## 3. 样本审计",
        "",
        "| P | interval | top row prime count | P-sqrt(P(P-1)) | positive |",
        "| ---: | --- | ---: | ---: | --- |",
    ]
    sweep = result["finite_sweep"]
    for item in sweep["sample_audits"]:
        lines.append(
            f"| {item['P']} | {item['internal_interval']} | {item['top_row_prime_count']} | "
            f"{item['p_minus_sqrt_x']:.6f} | `{fmt_bool(item['positive'])}` |"
        )
    lines.extend(
        [
            "",
            "## 4. 有限审计边界",
            "",
            "```text",
            f"max_prime={sweep['max_prime']}",
            f"case_count={sweep['case_count']}",
            f"all_top_rows_positive_in_finite_sweep={fmt_bool(sweep['all_top_rows_positive_in_finite_sweep'])}",
            f"zero_top_rows_found={sweep['zero_top_rows_found']}",
            f"minimum_top_row_prime_count={sweep['minimum_top_row_prime_count']}",
            "finite_evidence_not_used_as_global_proof=true",
            "```",
            "",
            "最小顶行素数数样本：",
            "",
            "| P | top row prime count |",
            "| ---: | ---: |",
        ]
    )
    for item in sweep["minimum_cases"]:
        lines.append(f"| {item['P']} | {item['top_row_prime_count']} |")
    lines.extend(
        [
            "",
            "尾部样本：",
            "",
            "| P | top row prime count | P-sqrt(P(P-1)) |",
            "| ---: | ---: | ---: |",
        ]
    )
    for item in sweep["tail_rows_sample"]:
        lines.append(
            f"| {item['P']} | {item['top_row_prime_count']} | "
            f"{item['p_minus_sqrt_p_pminus1']:.6f} |"
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
            f"| `{cell(item['gate'])}` | `{fmt_bool(item['closed'])}` | `{fmt_bool(item['proved'])}` | "
            f"{cell(item['meaning'])} | {cell(item['remaining'])} |"
        )
    lines.extend(
        [
            "",
            "## 6. 结论",
            "",
            "顶行 square-collar 是 strict 行正性的必要硬核，不是完整充分条件。",
            "它把最窄正性口压成 `PrimeSquareUpperCollarPrimeInput`：",
            "`pi(P^2-1)-pi(P^2-P)>=1` 对所有素数 `P` 成立。",
            "当前尚未无条件闭合，因此不能声称 Phi-LPF 递推已经推出正性。",
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
