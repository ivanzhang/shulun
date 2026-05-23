#!/usr/bin/env python3
"""闭合 Phi-LPF sawtooth 门中的 LPF 权重有界系数抽取账本。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_weight_extraction_norm_closure_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-weight-extraction-norm-closure-audit.json

本层接在 finite-H truncation closure 之后。它不证明 weighted reciprocal
phase saving，而是把 LPF-shell 权重从“可能需要巨型 Mobius 展开”的表述
压成无损 bounded coefficient package：

  * 三元图系数 beta(q,r,a) 为 0/1；
  * 固定 (q,r) 至多一个 a；
  * 投影到固定 prime q 的总权重至多 #I_q(P,k)<=2；
  * 总质量仍满足 R_30(P,k)<=W_int(P,k)<=2*pi(P)<2P。

结论：`LPFShellWeightBoundedCoefficientExtraction` 闭合；剩余硬点缩成
接受这些 bounded LPF 系数的 prime-q reciprocal phase saving / completion
theorem，而不是 LPF 权重本身的范数爆炸。
"""

from __future__ import annotations

import hashlib
import json
import math
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-weight-extraction-norm-closure"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-23"

FINITE_H_JSON = DOCS / "prime-matrix-phi-lpf-finite-h-truncation-closure-audit.json"
TYPEII_JSON = DOCS / "prime-matrix-phi-lpf-lpf-tail-typeii-obligation-audit.json"
SHELL_JSON = DOCS / "prime-matrix-phi-lpf-lpf-shell-decrement-audit.json"
SAWTOOTH_JSON = DOCS / "prime-matrix-phi-lpf-sawtooth-reciprocal-tail-gateway-audit.json"
THREE_CLAIMS_JSON = DOCS / "three-claims-frontier-rankone-explicit-formula-router.json"

DEPENDENCIES = [
    FINITE_H_JSON,
    TYPEII_JSON,
    SHELL_JSON,
    SAWTOOTH_JSON,
    THREE_CLAIMS_JSON,
    DOCS / "external-theorem-index.md",
    DOCS / "claim-status-table.md",
    DOCS / "frontier-honest-status-and-true-side-theorems-20260522.md",
    ROOT / "paper" / "contradiction-field-monograph" / "contradiction-field-monograph.tex",
]


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def bool_text(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    paths = [Path(__file__).resolve(), *DEPENDENCIES]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空记录。"""
    if not path.exists():
        return {"available": False}
    payload = json.loads(path.read_text(encoding="utf-8"))
    payload["available"] = True
    return payload


def prime_sieve(n: int) -> list[int]:
    """生成不超过 n 的素数。"""
    if n < 2:
        return []
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, int(n**0.5) + 1):
        if sieve[p]:
            start = p * p
            sieve[start : n + 1 : p] = b"\x00" * (((n - start) // p) + 1)
    return [i for i in range(2, n + 1) if sieve[i]]


def lpf(n: int, primes: list[int]) -> int:
    """返回 n 的最小素因子；n 为素数时返回 n。"""
    for p in primes:
        if p * p > n:
            break
        if n % p == 0:
            return p
    return n


def is_prime(n: int, primes: list[int]) -> bool:
    """判断素数。"""
    if n < 2:
        return False
    return lpf(n, primes) == n


def reciprocal_window(P: int, k: int, q: int) -> tuple[int, int]:
    """返回 q 对应的 cofactor 窗口 I_q(P,k)。"""
    low = max(q, (k * P) // q + 1)
    high = min(2 * P - 1, (((k + 1) * P) - 1) // q)
    return low, high


def row_weight_package(P: int, k: int, primes: list[int]) -> dict[str, Any]:
    """计算一行的 LPF bounded coefficient package 诊断。"""
    q_primes = [q for q in primes if P // 2 < q < P]
    q_weights: Counter[int] = Counter()
    qr_weights: Counter[tuple[int, int]] = Counter()
    shell_counts: Counter[int] = Counter()
    triples: list[tuple[int, int, int]] = []
    wint = 0

    for q in q_primes:
        low, high = reciprocal_window(P, k, q)
        if low > high:
            continue
        for m in range(low, high + 1):
            wint += 1
            r = lpf(m, primes)
            if r < 7 or r == m:
                continue
            a = m // r
            # 中文注释：最小素因子定义自动保证 a 为 r-rough；这里仍显式防守。
            if a < r or any(a % p == 0 for p in primes if p < r):
                raise AssertionError((P, k, q, m, r, a))
            q_weights[q] += 1
            qr_weights[(q, r)] += 1
            shell_counts[r] += 1
            triples.append((q, r, a))

    max_q_weight = max(q_weights.values(), default=0)
    max_qr_weight = max(qr_weights.values(), default=0)
    shell_text = ", ".join(f"{r}:{shell_counts[r]}" for r in sorted(shell_counts)) or "empty"
    return {
        "P": P,
        "k": k,
        "q_count": len(q_primes),
        "W_int": wint,
        "R30": len(triples),
        "max_projected_q_weight": max_q_weight,
        "max_qr_fiber_weight": max_qr_weight,
        "projected_q_weight_le_2": max_q_weight <= 2,
        "qr_fiber_weight_le_1": max_qr_weight <= 1,
        "total_mass_le_Wint": len(triples) <= wint,
        "Wint_le_2piP": wint <= 2 * len([p for p in primes if p <= P]),
        "coefficient_linf": 1 if triples else 0,
        "shells": shell_text,
    }


def audit_rows(max_prime: int = 1009) -> dict[str, Any]:
    """对 P<=max_prime 的全部 strict rows 做有限一致性审计。"""
    primes = prime_sieve(2 * max_prime + 10)
    P_values = [p for p in primes if 11 <= p <= max_prime]
    row_count = 0
    active_rows = 0
    total_r30 = 0
    max_q_weight_seen = 0
    max_qr_weight_seen = 0
    violations: list[dict[str, Any]] = []
    samples: list[dict[str, Any]] = []
    interesting = {(101, 100), (257, 256), (971, 936), (1009, 1008)}

    for P in P_values:
        for k in range(1, P):
            row_count += 1
            row = row_weight_package(P, k, primes)
            total_r30 += row["R30"]
            active_rows += int(row["R30"] > 0)
            max_q_weight_seen = max(max_q_weight_seen, row["max_projected_q_weight"])
            max_qr_weight_seen = max(max_qr_weight_seen, row["max_qr_fiber_weight"])
            if (P, k) in interesting:
                samples.append(row)
            if not (
                row["projected_q_weight_le_2"]
                and row["qr_fiber_weight_le_1"]
                and row["total_mass_le_Wint"]
                and row["Wint_le_2piP"]
            ):
                violations.append(row)

    return {
        "max_prime": max_prime,
        "k_range": "1<=k<P in this implementation audit",
        "row_count": row_count,
        "active_residual_row_count": active_rows,
        "total_R30": total_r30,
        "max_projected_q_weight_seen": max_q_weight_seen,
        "max_qr_fiber_weight_seen": max_qr_weight_seen,
        "all_projected_q_weights_le_2": max_q_weight_seen <= 2 and not violations,
        "all_qr_fibers_le_1": max_qr_weight_seen <= 1 and not violations,
        "all_total_masses_le_Wint_le_2piP": not violations,
        "violation_count": len(violations),
        "finite_evidence_not_used_as_global_proof": True,
        "sample_rows": samples,
    }


def table(rows: list[dict[str, Any]], fields: list[str]) -> str:
    """生成 Markdown 表格。"""
    header = "| " + " | ".join(fields) + " |"
    sep = "| " + " | ".join("---" for _ in fields) + " |"
    body = []
    for row in rows:
        cells = []
        for field in fields:
            value = row.get(field, "")
            if isinstance(value, bool):
                value = bool_text(value)
            elif isinstance(value, list):
                value = " / ".join(str(item) for item in value)
            cells.append(str(value).replace("|", r"\|"))
        body.append("| " + " | ".join(cells) + " |")
    return "\n".join([header, sep, *body])


def gate(name: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造门控记录。"""
    return {
        "gate": name,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_payload() -> dict[str, Any]:
    """构造审计 payload。"""
    finite_h = load_json(FINITE_H_JSON)
    typeii = load_json(TYPEII_JSON)
    three_claims = load_json(THREE_CLAIMS_JSON)
    finite_audit = audit_rows()
    return {
        "certificate_type": "prime_matrix_phi_lpf_weight_extraction_norm_closure_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "lpf_shell_weight_extracted_to_bounded_coefficients_phase_saving_open",
        "three_claim_triage": [
            {
                "claim": "Prime Matrix row/column Phi-LPF",
                "frontier_before": finite_h.get("latest_narrowest_mouth"),
                "fastest_subgate": "LPFShellWeightBoundedCoefficientExtraction",
                "chosen": True,
                "reason": "pure support and coefficient-norm ledger after finite-H truncation; no new prime theorem required",
            },
            {
                "claim": "two-point sieve / prime-pair line",
                "frontier": "BMD=>TLI without hidden denominator/parity gap",
                "chosen": False,
                "reason": "still needs Buchstab transfer and denominator audit",
            },
            {
                "claim": "RH contradiction-field line",
                "frontier": "IndependentRefereeAcceptanceOfAllRHControlledExits",
                "chosen": False,
                "reason": "verification package, not a closable algebraic coefficient gate",
            },
        ],
        "three_claim_source_status": three_claims.get("plain_conclusion"),
        "upstream_typeii_status": {
            "available": typeii.get("available", False),
            "status": typeii.get("status"),
            "current_mouth": typeii.get("current_narrowest_mouth"),
        },
        "extraction_theorem": {
            "triple_package": "R_30(P,k)=sum_{P/2<q<P prime} sum_{r>=7 prime} sum_{a>=r, P^-(a)>=r} beta(q,r,a) 1_{kP<qra<(k+1)P}, beta in {0,1}.",
            "one_point_qr_fiber": "Since q*r>P for r>=7 and q>P/2, each fixed (q,r) has at most one quotient a in a row.",
            "q_projection": "The q-projected LPF weight b(q)=# {m in I_q(P,k): m composite and LPF(m)>=7} satisfies 0<=b(q)<=#I_q(P,k)<=2.",
            "total_mass": "sum_q b(q)=R_30(P,k)<=W_int(P,k)<=2*pi(P)<2P.",
            "norm_conclusion": "LPF extraction causes no coefficient blow-up: linf(beta)<=1, linf(b)<=2, l1 total O(P).",
            "rejected_route": "Do not expand the rough condition by full Mobius inclusion-exclusion over all primes <r; that exact identity is true but has exponential l1 risk and is unnecessary for the coefficient package.",
        },
        "finite_audit": finite_audit,
        "external_frontier_match_table": [
            {
                "source": "Vaughan/Heath-Brown Type-I/II identity framework",
                "useful_part": "accepts bounded coefficient sequences after an appropriate bilinear decomposition",
                "accepted_for_this_gate": True,
                "closes_phase_saving": False,
                "reason_not_direct": "the same-row reciprocal graph and prime-q phase still need their own Type-II/dispersion estimate",
            },
            {
                "source": "Duke-Friedlander-Iwaniec 1997 and Bettin--Chandee Kloosterman-fraction technology",
                "useful_part": "bounded coefficients are compatible after inverse-fraction completion",
                "accepted_for_this_gate": True,
                "closes_phase_saving": False,
                "reason_not_direct": "the completion identity from real reciprocal/product window to inverse Kloosterman form is still missing",
            },
            {
                "source": "Milićević--Qin--Wu 2025, Pascadi 2025, Shao--Shparlinski--Wijaya 2024/2025",
                "useful_part": "frontier Kloosterman estimates for later bounded-coefficient phase work",
                "accepted_for_this_gate": False,
                "closes_phase_saving": False,
                "reason_not_direct": "they do not directly estimate fixed-row prime-q real reciprocal phases with LPF-shell coefficients",
            },
        ],
        "closed_gates": [
            gate(
                "LPFShellWeightBoundedCoefficientExtraction",
                True,
                True,
                "The LPF-shell condition is absorbed into beta(q,r,a) in {0,1} and q-projected weights b(q)<=2.",
                "none",
            ),
            gate(
                "NoMobiusL1ExplosionNeeded",
                True,
                True,
                "The proof avoids full roughness inclusion-exclusion; all norms are controlled by thin reciprocal fibres.",
                "none",
            ),
            gate(
                "PrimeQBoundedLPFCoefficientReciprocalPhaseSaving",
                False,
                False,
                "For |h|<=polylog(P), prove cancellation for sum_{q prime} b_{P,k}(q)e(hkP/q) with 0<=b(q)<=2 coming from the LPF graph.",
                "weighted bounded-coefficient prime-q reciprocal phase theorem",
            ),
            gate(
                "CompletionToExternalKloostermanOrVaughanTypeII",
                False,
                False,
                "Convert the same-row reciprocal/product-window form to a DI/DFI/BC/FM-compatible estimate without losing pointwise P,k.",
                "completion/dispersion identity",
            ),
        ],
        "latest_narrowest_mouth": [
            "PrimeQBoundedLPFCoefficientReciprocalPhaseSaving",
            "AND CompletionToExternalKloostermanOrVaughanTypeII",
        ],
        "lpf_weight_bounded_coefficient_extraction_closed": True,
        "weighted_reciprocal_phase_saving_closed": False,
        "phi_lpf_parity_barrier_globally_broken": False,
        "row_column_unconditional_closed": False,
        "external_lemma_version_unconditional_closed": False,
        "internal_self_contained_closed": False,
        "source_hashes": source_hashes(),
    }


def build_markdown(payload: dict[str, Any]) -> str:
    """生成 Markdown 证书。"""
    theorem = payload["extraction_theorem"]
    audit = payload["finite_audit"]
    lines = [
        "# Prime Matrix Phi-LPF weight extraction norm closure 审计",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['frontier_verified_date']}`",
        "",
        "## 1. 三命题选择",
        "",
        table(payload["three_claim_triage"], ["claim", "frontier", "frontier_before", "fastest_subgate", "chosen", "reason"]),
        "",
        "finite-H 截断闭合后，本轮选择行/列 Phi-LPF 的 LPF 权重抽取子门。该子门是纯支撑与范数账本；二点筛与 RH 线没有同样可直接闭合的代数子门。",
        "",
        "## 2. 有界系数抽取定理",
        "",
        "```text",
        f"triple_package={theorem['triple_package']}",
        f"one_point_qr_fiber={theorem['one_point_qr_fiber']}",
        f"q_projection={theorem['q_projection']}",
        f"total_mass={theorem['total_mass']}",
        f"norm_conclusion={theorem['norm_conclusion']}",
        f"rejected_route={theorem['rejected_route']}",
        "```",
        "",
        "关键点是：LPF-shell 不需要展开成所有小素数的 Möbius 排斥和。保留 `r=LPF(m)` 与 `a` 为 `r`-rough 的三元图系数即可，系数为 `0/1`；再投影到每个 prime `q` 时，由 `#I_q(P,k)<=2` 直接得到 `b(q)<=2`。",
        "",
        "## 3. 全量有限审计",
        "",
        "```text",
        f"max_prime={audit['max_prime']}",
        f"k_range={audit['k_range']}",
        f"row_count={audit['row_count']}",
        f"active_residual_row_count={audit['active_residual_row_count']}",
        f"total_R30={audit['total_R30']}",
        f"max_projected_q_weight_seen={audit['max_projected_q_weight_seen']}",
        f"max_qr_fiber_weight_seen={audit['max_qr_fiber_weight_seen']}",
        f"all_projected_q_weights_le_2={bool_text(audit['all_projected_q_weights_le_2'])}",
        f"all_qr_fibers_le_1={bool_text(audit['all_qr_fibers_le_1'])}",
        f"all_total_masses_le_Wint_le_2piP={bool_text(audit['all_total_masses_le_Wint_le_2piP'])}",
        f"violation_count={audit['violation_count']}",
        "```",
        "",
        "有限审计只验证实现和账本一致性；全局闭合来自上面的符号 thin-fibre 论证。",
        "",
        "代表行：",
        "",
        table(
            audit["sample_rows"],
            [
                "P",
                "k",
                "q_count",
                "W_int",
                "R30",
                "max_projected_q_weight",
                "max_qr_fiber_weight",
                "coefficient_linf",
                "shells",
            ],
        ),
        "",
        "## 4. 外部前沿匹配",
        "",
        table(
            payload["external_frontier_match_table"],
            ["source", "useful_part", "accepted_for_this_gate", "closes_phase_saving", "reason_not_direct"],
        ),
        "",
        "Vaughan/Heath-Brown、DFI、Bettin--Chandee 与最新 Kloosterman 前沿都可在后续相位估计中利用 bounded coefficients；本层只关闭系数抽取与范数控制，不关闭 prime-q reciprocal phase saving。",
        "",
        "## 5. 门控表",
        "",
        table(payload["closed_gates"], ["gate", "closed", "proved", "meaning", "remaining"]),
        "",
        "## 6. 最新最窄口",
        "",
        "```text",
        *payload["latest_narrowest_mouth"],
        "```",
        "",
        "状态边界：",
        "",
        "```text",
        f"lpf_weight_bounded_coefficient_extraction_closed={bool_text(payload['lpf_weight_bounded_coefficient_extraction_closed'])}",
        f"weighted_reciprocal_phase_saving_closed={bool_text(payload['weighted_reciprocal_phase_saving_closed'])}",
        f"phi_lpf_parity_barrier_globally_broken={bool_text(payload['phi_lpf_parity_barrier_globally_broken'])}",
        f"row_column_unconditional_closed={bool_text(payload['row_column_unconditional_closed'])}",
        f"external_lemma_version_unconditional_closed={bool_text(payload['external_lemma_version_unconditional_closed'])}",
        f"internal_self_contained_closed={bool_text(payload['internal_self_contained_closed'])}",
        "```",
    ]
    return "\n".join(lines) + "\n"


def main() -> None:
    """写出 JSON、ledger 与 Markdown。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    payload = build_payload()
    text = json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True)
    OUT_LEDGER.write_text(text + "\n", encoding="utf-8")
    OUT_JSON.write_text(text + "\n", encoding="utf-8")
    OUT_MD.write_text(build_markdown(payload), encoding="utf-8")
    print(f"wrote {OUT_LEDGER.relative_to(ROOT)}")
    print(f"wrote {OUT_JSON.relative_to(ROOT)}")
    print(f"wrote {OUT_MD.relative_to(ROOT)}")
    print("lpf_weight_bounded_coefficient_extraction_closed=true")
    print("weighted_reciprocal_phase_saving_closed=false")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
