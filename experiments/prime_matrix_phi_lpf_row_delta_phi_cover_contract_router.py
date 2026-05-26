#!/usr/bin/env python3
"""生成 Phi-LPF 行级 Delta-Phi 覆盖不等式合同证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_row_delta_phi_cover_contract_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-row-delta-phi-cover-contract-router.json

输出：
  data/prime-matrix-phi-lpf-row-delta-phi-cover-contract-ledger.json
  docs/monograph/prime-matrix-phi-lpf-row-delta-phi-cover-contract-router.json
  docs/monograph/prime-matrix-phi-lpf-row-delta-phi-cover-contract-router.md
"""

from __future__ import annotations

import hashlib
import json
from math import isqrt
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-row-delta-phi-cover-contract"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

LPF_BUCKET = DOCS / "prime-matrix-phi-lpf-lpf-bucket-count-formula-audit.json"
PRIME_CONTRACT = DOCS / "prime-matrix-phi-lpf-parity-barrier-prime-distribution-contract-router.json"
TRANSPORT_EDGE = DOCS / "prime-matrix-phi-lpf-parity-barrier-transport-edge-sync-router.json"
PUNCTURED_WHEEL30 = DOCS / "prime-matrix-phi-lpf-punctured-endpoint-wheel30-capacity-router.json"
CLAIM_STATUS = DOCS / "claim-status-table.md"
SYNTHESIS = DOCS / "three-claims-breakthrough-route-synthesis-20260525.md"
ACTUAL_LOAD = DOCS / "three-claims-actual-load-closure-contracts.md"
FORMAL_FRONTIER = DOCS / "three-claims-formal-to-actual-critical-load-frontier.md"
EXTERNAL_INDEX = DOCS / "external-theorem-index.md"
FRONTIER_HONEST = DOCS / "frontier-honest-status-and-true-side-theorems-20260522.md"
PAPER = ROOT / "paper" / "contradiction-field-monograph" / "contradiction-field-monograph.tex"

SOURCE_FILES = [
    Path(__file__).resolve(),
    LPF_BUCKET,
    PRIME_CONTRACT,
    TRANSPORT_EDGE,
    PUNCTURED_WHEEL30,
    CLAIM_STATUS,
    SYNTHESIS,
    ACTUAL_LOAD,
    FORMAL_FRONTIER,
    EXTERNAL_INDEX,
    FRONTIER_HONEST,
    PAPER,
]


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    return {str(path.relative_to(ROOT)): sha256(path) for path in SOURCE_FILES if path.exists()}


def primes_upto(n: int) -> list[int]:
    """朴素生成素数，样本规模很小。"""
    primes: list[int] = []
    for value in range(2, n + 1):
        if all(value % p for p in primes if p * p <= value):
            primes.append(value)
    return primes


def is_prime(n: int) -> bool:
    """判断素数。"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def phi_rough_count(y: int, p: int) -> int:
    """Phi(y; primes<p)：统计不被任何小于 p 的素数整除的 1<=m<=y。"""
    small = primes_upto(p - 1)
    return sum(1 for m in range(1, y + 1) if all(m % q for q in small))


def lpf_bucket_prefix(n: int, p: int) -> int:
    """C_p(n)=#{m<=n: m 合数且 LPF(m)=p} 的精确前缀公式。"""
    if n < p * p:
        return 0
    return phi_rough_count(n // p, p) - 1


def row_audit(a: int, b: int) -> dict[str, Any]:
    """审计整数区间 (a,b] 的 Delta-Phi 覆盖恒等式。"""
    if not (1 <= a < b):
        raise ValueError("row interval must satisfy 1 <= a < b")
    rows: list[dict[str, int]] = []
    composite_cover = 0
    for p in primes_upto(isqrt(b)):
        delta = lpf_bucket_prefix(b, p) - lpf_bucket_prefix(a, p)
        if delta:
            rows.append(
                {
                    "p": p,
                    "C_p_b": lpf_bucket_prefix(b, p),
                    "C_p_a": lpf_bucket_prefix(a, p),
                    "delta_phi_bucket": delta,
                }
            )
            composite_cover += delta

    length = b - a
    prime_count = sum(1 for n in range(a + 1, b + 1) if is_prime(n))
    direct_composites = sum(1 for n in range(a + 1, b + 1) if n > 1 and not is_prime(n))
    residual = length - composite_cover
    return {
        "interval": f"({a},{b}]",
        "a": a,
        "b": b,
        "length": length,
        "prime_count": prime_count,
        "direct_composite_count": direct_composites,
        "delta_phi_composite_cover": composite_cover,
        "residual_length_minus_cover": residual,
        "identity_holds": prime_count == residual and direct_composites == composite_cover,
        "strict_cover_inequality_holds": composite_cover <= length - 1,
        "prime_free": prime_count == 0,
        "nonzero_by_prefix_difference": prime_count > 0,
        "nonzero_bucket_rows": rows,
    }


def prime_matrix_row_samples() -> list[dict[str, Any]]:
    """给出小素数 P 的 punctured strict rows 样本。"""
    samples: list[dict[str, Any]] = []
    for p in [5, 7, 11, 13, 17, 19, 31]:
        counts: list[int] = []
        zero_rows: list[int] = []
        for k in range(1, p):
            row = row_audit(k * p, (k + 1) * p - 1)
            counts.append(row["prime_count"])
            if row["prime_count"] == 0:
                zero_rows.append(k)
        samples.append(
            {
                "P": p,
                "row_model": "(kP,(k+1)P) as integers kP<n<(k+1)P",
                "k_range": f"1..{p - 1}",
                "min_prime_count": min(counts),
                "max_prime_count": max(counts),
                "zero_row_count": len(zero_rows),
                "zero_rows": zero_rows,
                "counts": counts,
            }
        )
    return samples


def external_formula_rows() -> list[dict[str, str]]:
    """列出真正能闭合行级正性的输入格式。"""
    return [
        {
            "route": "Direct Delta-Phi strict cover inequality",
            "needed_formula": "sum_{p<=sqrt(B)}(C_p(B)-C_p(A)) <= B-A-1 for every target row (A,B]",
            "current_blocker": "this is exactly equivalent to pi(B)-pi(A)>0; no independent saving has been proved",
        },
        {
            "route": "Pointwise theta at sqrt row scale",
            "needed_formula": "theta(B)-theta(A)>0 for every target row",
            "current_blocker": "known short-interval inputs still do not give a zero-exception x^(1/2) theorem at this row scale",
        },
        {
            "route": "Psi beyond prime-power tail",
            "needed_formula": "psi(B)-psi(A)>prime_power_tail(A,B)",
            "current_blocker": "prime-power tail is bounded, but the required pointwise psi lower bound is still open",
        },
        {
            "route": "Signed Mobius/Von Mangoldt Type-I/II",
            "needed_formula": "source-key-consistent signed divisor decomposition with error < one row survivor",
            "current_blocker": "LPF/Phi support ledgers have not produced admissible signed coefficients",
        },
        {
            "route": "Trace/Kloosterman/spectral",
            "needed_formula": "completed source-keyed trace family with conductor and coefficient control",
            "current_blocker": "current q-spine/hinge ledgers are finite actual-load ledgers, not uniform trace families",
        },
        {
            "route": "Cover-equality PDEC/SAE return",
            "needed_formula": "if Delta-Phi cover equals row length, the induced LPF owner residues create a named contradiction",
            "current_blocker": "the covering equality has not yet been converted into a forbidden structured packet",
        },
    ]


def build_certificate() -> dict[str, Any]:
    """组装行级 Delta-Phi 覆盖合同证书。"""
    lpf_bucket = load_json(LPF_BUCKET)
    prime_contract = load_json(PRIME_CONTRACT)
    transport_edge = load_json(TRANSPORT_EDGE)

    sample_rows = [
        row_audit(90, 96),
        row_audit(100, 110),
        row_audit(110, 120),
        row_audit(900, 930),
        row_audit(990, 1020),
    ]

    identity_closed = all(row["identity_holds"] for row in sample_rows)
    zero_example = next(row for row in sample_rows if row["prime_free"])

    return {
        "certificate_type": "prime_matrix_phi_lpf_row_delta_phi_cover_contract_router",
        "status": "row_delta_phi_exact_identity_closed_but_positive_cover_gap_open",
        "verified_date": "2026-05-26",
        "same_theorem_target_preserved": True,
        "finite_evidence_not_used_as_global_proof": True,
        "lpf_prefix_formula_imported": lpf_bucket.get("exact_lpf_bucket_identity_closed") is True,
        "parity_contract_imported": prime_contract.get("unsigned_lpf_bucket_count_sufficient_for_prime_extraction") is False,
        "transport_edge_frontier_imported": transport_edge.get("transport_edge_sync_closed") is True,
        "row_delta_phi_identity_closed": identity_closed,
        "row_delta_phi_prefix_difference_is_exact": True,
        "row_delta_phi_positive_lower_bound_proved": False,
        "strict_cover_inequality_proved_uniformly": False,
        "row_column_unconditional_closed": False,
        "exact_prefix_formula": "C_p(N)=0 if N<p^2, else Phi(floor(N/p); primes<p)-1",
        "exact_row_formula": "pi(A,B]=B-A-sum_{p<=sqrt(B)}(C_p(B)-C_p(A))",
        "target_cover_inequality": "sum_{p<=sqrt(B)}(C_p(B)-C_p(A)) <= B-A-1",
        "equivalence_warning": "target_cover_inequality is equivalent to pi(A,B]>0, so it cannot be used as an independent proof without a new saving/PDEC/trace input",
        "prime_free_exact_delta_phi_sample": zero_example,
        "sample_rows": sample_rows,
        "prime_matrix_punctured_row_samples": prime_matrix_row_samples(),
        "external_formula_rows": external_formula_rows(),
        "next_primary_attack_target": "UniformDeltaPhiCoverDefectOrNamedLPFOwnerResiduePDEC",
        "paired_signed_attack_target": "PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward OR SourceKeyedMobiusVonMangoldtTraceTypeIIFamily",
        "paired_distribution_attack_target": "PointwiseThetaPsiCOneInputAtSqrtRowScale",
        "plain_conclusion": (
            "行内短区间计数确实等于两个前缀 LPF/Phi 计数之差；这给出完全精确的 "
            "Delta-Phi 覆盖恒等式。该恒等式把正性目标化为严格覆盖缺口：LPF 合数桶在"
            "目标行内的总覆盖必须小于行长。然而严格缺口本身等价于该行有素数，不能由"
            "恒等式自动推出。下一步必须证明统一 Delta-Phi cover defect，或把覆盖等号"
            "转化为命名 LPF-owner residue PDEC，或引入点态 theta/psi、signed divisor、"
            "trace/Type-II 输入。"
        ),
        "source_hashes": source_hashes(),
    }


def fmt_bool(value: Any) -> str:
    """小写布尔值。"""
    return "true" if bool(value) else "false"


def cell(value: Any) -> str:
    """Markdown 表格转义。"""
    return str(value).replace("|", r"\|")


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown。"""
    lines = [
        "# Prime Matrix Phi-LPF row Delta-Phi cover contract 路由",
        "",
        f"**状态：** `{cert['status']}`",
        f"**核验日期：** `{cert['verified_date']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"row_delta_phi_identity_closed={fmt_bool(cert['row_delta_phi_identity_closed'])}",
        f"row_delta_phi_prefix_difference_is_exact={fmt_bool(cert['row_delta_phi_prefix_difference_is_exact'])}",
        f"row_delta_phi_positive_lower_bound_proved={fmt_bool(cert['row_delta_phi_positive_lower_bound_proved'])}",
        f"strict_cover_inequality_proved_uniformly={fmt_bool(cert['strict_cover_inequality_proved_uniformly'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 精确恒等式",
        "",
        "```text",
        cert["exact_prefix_formula"],
        cert["exact_row_formula"],
        cert["target_cover_inequality"],
        "```",
        "",
        cert["equivalence_warning"],
        "",
        "## 2. 样本行核验",
        "",
        "| interval | length | Delta-Phi cover | primes | residual | identity | prime-free |",
        "| --- | ---: | ---: | ---: | ---: | --- | --- |",
    ]
    for row in cert["sample_rows"]:
        lines.append(
            f"| `{row['interval']}` | {row['length']} | {row['delta_phi_composite_cover']} | "
            f"{row['prime_count']} | {row['residual_length_minus_cover']} | "
            f"`{fmt_bool(row['identity_holds'])}` | `{fmt_bool(row['prime_free'])}` |"
        )

    zero = cert["prime_free_exact_delta_phi_sample"]
    lines.extend(
        [
            "",
            "prime-free 样本说明：前缀差公式会精确给出零素数行，而不是自动排除零行。",
            "",
            "```text",
            f"interval={zero['interval']}",
            f"length={zero['length']}",
            f"delta_phi_composite_cover={zero['delta_phi_composite_cover']}",
            f"prime_count={zero['prime_count']}",
            "```",
            "",
            "## 3. Prime Matrix 小 P punctured row 样本",
            "",
            "| P | k range | min primes | max primes | zero rows |",
            "| ---: | --- | ---: | ---: | ---: |",
        ]
    )
    for row in cert["prime_matrix_punctured_row_samples"]:
        lines.append(
            f"| {row['P']} | `{row['k_range']}` | {row['min_prime_count']} | "
            f"{row['max_prime_count']} | {row['zero_row_count']} |"
        )

    lines.extend(
        [
            "",
            "## 4. 真正需要攻克的公式",
            "",
            "| route | needed formula | current blocker |",
            "| --- | --- | --- |",
        ]
    )
    for row in cert["external_formula_rows"]:
        lines.append(
            f"| {cell(row['route'])} | `{cell(row['needed_formula'])}` | {cell(row['current_blocker'])} |"
        )

    lines.extend(
        [
            "",
            "## 5. 下一手",
            "",
            "```text",
            f"next_primary_attack_target={cert['next_primary_attack_target']}",
            f"paired_signed_attack_target={cert['paired_signed_attack_target']}",
            f"paired_distribution_attack_target={cert['paired_distribution_attack_target']}",
            "```",
            "",
            "## 6. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in sorted(cert["source_hashes"].items()):
        lines.append(f"| `{path}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """写出证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    cert = build_certificate()
    text = json.dumps(cert, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    OUT_LEDGER.write_text(text, encoding="utf-8")
    OUT_JSON.write_text(text, encoding="utf-8")
    OUT_MD.write_text(render_markdown(cert), encoding="utf-8")
    print(f"row_delta_phi_identity_closed={fmt_bool(cert['row_delta_phi_identity_closed'])}")
    print(f"strict_cover_inequality_proved_uniformly={fmt_bool(cert['strict_cover_inequality_proved_uniformly'])}")
    print(f"next_primary_attack_target={cert['next_primary_attack_target']}")
    print(f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
