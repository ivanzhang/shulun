#!/usr/bin/env python3
"""闭合 Phi-LPF bounded coefficient 后的 prime-q 布尔投影门。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_boolean_q_projection_closure_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-boolean-q-projection-closure-audit.json

上一层已证明 LPF-shell 权重可抽成 b_{P,k}(q)<=2 的有界 prime-q
系数。本层再用一个完全初等但关键的奇偶事实把它 sharpen 到布尔权重：

  * #I_q(P,k)<=2，且若有两个点它们必为连续整数；
  * residual 条件 LPF(m)>=7 且 m composite 强迫 m 为奇数；
  * 两个连续整数中至多一个奇数。

因此 b_{P,k}(q) in {0,1}。这仍不证明 prime-q reciprocal phase saving，
但删除了“同一个 q 可能双重带权”的 multiplicity 噪声。
"""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-boolean-q-projection-closure"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-23"

WEIGHT_EXTRACTION_JSON = DOCS / "prime-matrix-phi-lpf-weight-extraction-norm-closure-audit.json"
FINITE_H_JSON = DOCS / "prime-matrix-phi-lpf-finite-h-truncation-closure-audit.json"
TYPEII_JSON = DOCS / "prime-matrix-phi-lpf-lpf-tail-typeii-obligation-audit.json"
THREE_CLAIMS_JSON = DOCS / "three-claims-frontier-rankone-explicit-formula-router.json"

DEPENDENCIES = [
    WEIGHT_EXTRACTION_JSON,
    FINITE_H_JSON,
    TYPEII_JSON,
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


def reciprocal_window(P: int, k: int, q: int) -> tuple[int, int]:
    """返回 q 对应的 cofactor 窗口 I_q(P,k)。"""
    low = max(q, (k * P) // q + 1)
    high = min(2 * P - 1, (((k + 1) * P) - 1) // q)
    return low, high


def residual_ms(P: int, k: int, q: int, primes: list[int]) -> list[int]:
    """列出固定 q 上的 LPF residual cofactor。"""
    low, high = reciprocal_window(P, k, q)
    if low > high:
        return []
    out: list[int] = []
    for m in range(low, high + 1):
        r = lpf(m, primes)
        if r >= 7 and r != m:
            out.append(m)
    return out


def row_boolean_projection(P: int, k: int, primes: list[int]) -> dict[str, Any]:
    """计算一行的 prime-q 布尔投影诊断。"""
    q_primes = [q for q in primes if P // 2 < q < P]
    q_weights: Counter[int] = Counter()
    two_point_windows = 0
    two_point_with_residual = 0
    max_window_size = 0
    parity_blocked_double_residual = True
    sample_qs: list[str] = []

    for q in q_primes:
        low, high = reciprocal_window(P, k, q)
        window_size = max(0, high - low + 1)
        max_window_size = max(max_window_size, window_size)
        if window_size == 2:
            two_point_windows += 1
        ms = residual_ms(P, k, q, primes)
        q_weights[q] = len(ms)
        if len(ms) > 0 and len(sample_qs) < 5:
            sample_qs.append(f"q={q}:m={','.join(map(str, ms))}")
        if window_size == 2 and ms:
            two_point_with_residual += 1
        if len(ms) > 1:
            parity_blocked_double_residual = False

    max_q_weight = max(q_weights.values(), default=0)
    return {
        "P": P,
        "k": k,
        "q_count": len(q_primes),
        "max_window_size": max_window_size,
        "two_point_windows": two_point_windows,
        "two_point_windows_with_residual": two_point_with_residual,
        "R30": sum(q_weights.values()),
        "max_projected_q_weight": max_q_weight,
        "projected_q_weight_boolean": max_q_weight <= 1,
        "parity_blocked_double_residual": parity_blocked_double_residual,
        "sample_q_residuals": "; ".join(sample_qs) if sample_qs else "empty",
    }


def audit_rows(max_prime: int = 1009) -> dict[str, Any]:
    """对 P<=max_prime 的全部 1<=k<P 行做有限一致性审计。"""
    primes = prime_sieve(2 * max_prime + 10)
    P_values = [p for p in primes if 11 <= p <= max_prime]
    row_count = 0
    active_rows = 0
    total_r30 = 0
    max_q_weight_seen = 0
    max_window_seen = 0
    total_two_point_windows = 0
    total_two_point_with_residual = 0
    violations: list[dict[str, Any]] = []
    samples: list[dict[str, Any]] = []
    interesting = {(101, 100), (257, 256), (971, 936), (1009, 1008)}

    for P in P_values:
        for k in range(1, P):
            row_count += 1
            row = row_boolean_projection(P, k, primes)
            total_r30 += row["R30"]
            active_rows += int(row["R30"] > 0)
            max_q_weight_seen = max(max_q_weight_seen, row["max_projected_q_weight"])
            max_window_seen = max(max_window_seen, row["max_window_size"])
            total_two_point_windows += row["two_point_windows"]
            total_two_point_with_residual += row["two_point_windows_with_residual"]
            if (P, k) in interesting:
                samples.append(row)
            if not row["projected_q_weight_boolean"]:
                violations.append(row)

    return {
        "max_prime": max_prime,
        "k_range": "1<=k<P in this implementation audit",
        "row_count": row_count,
        "active_residual_row_count": active_rows,
        "total_R30": total_r30,
        "max_window_size_seen": max_window_seen,
        "total_two_point_windows": total_two_point_windows,
        "total_two_point_windows_with_residual": total_two_point_with_residual,
        "max_projected_q_weight_seen": max_q_weight_seen,
        "all_projected_q_weights_boolean": max_q_weight_seen <= 1 and not violations,
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
    weight = load_json(WEIGHT_EXTRACTION_JSON)
    three_claims = load_json(THREE_CLAIMS_JSON)
    finite_audit = audit_rows()
    return {
        "certificate_type": "prime_matrix_phi_lpf_boolean_q_projection_closure_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "prime_q_lpf_projection_boolean_phase_saving_open",
        "three_claim_triage": [
            {
                "claim": "Prime Matrix row/column Phi-LPF",
                "frontier_before": weight.get("latest_narrowest_mouth"),
                "fastest_subgate": "PrimeQBooleanProjectionForLPFShellResidual",
                "chosen": True,
                "reason": "pure parity plus thin-window sharpening after bounded coefficient extraction; no new prime theorem required",
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
                "reason": "verification package, not a closable prime-q projection gate",
            },
        ],
        "three_claim_source_status": three_claims.get("plain_conclusion"),
        "boolean_projection_theorem": {
            "window_bound": "For q>P/2, I_q(P,k) has at most two integers; if two occur they are consecutive.",
            "residual_parity": "If m is composite and LPF(m)>=7, then m is odd and coprime to 2,3,5.",
            "boolean_projection": "Therefore b_{P,k}(q)=# {m in I_q(P,k): m composite, LPF(m)>=7} belongs to {0,1}.",
            "phase_reduction": "Finite sawtooth modes reduce to sums over a subset Q_{P,k} of primes q in (P/2,P), not to a multi-weighted prime sequence.",
            "not_enough": "Boolean coefficients alone do not prove cancellation; a prime-q subset reciprocal phase theorem or a completion theorem is still needed.",
        },
        "finite_audit": finite_audit,
        "external_frontier_match_table": [
            {
                "source": "Classical parity/2-wheel observation",
                "useful_part": "closes the q-projected multiplicity gate because residual m are odd",
                "accepted_for_this_gate": True,
                "closes_phase_saving": False,
                "reason_not_direct": "removes double weights only; does not estimate exponential sums over the resulting prime subset",
            },
            {
                "source": "Milićević--Qin--Wu 2025 arXiv:2511.07550",
                "useful_part": "arbitrary-modulus bilinear Kloosterman power savings for a later completed form",
                "accepted_for_this_gate": False,
                "closes_phase_saving": False,
                "reason_not_direct": "requires inverse/Kloosterman completion, not merely boolean q-coefficients",
            },
            {
                "source": "Pascadi 2025 arXiv:2511.08445",
                "useful_part": "composite-modulus Type-II Kloosterman amplification",
                "accepted_for_this_gate": False,
                "closes_phase_saving": False,
                "reason_not_direct": "not a fixed-row real reciprocal phase theorem",
            },
            {
                "source": "Shao--Shparlinski--Wijaya 2024/2025 arXiv:2411.12113",
                "useful_part": "Kloosterman sums over square-free and smooth parameters",
                "accepted_for_this_gate": False,
                "closes_phase_saving": False,
                "reason_not_direct": "useful after finite-field completion, not direct for Q_{P,k} prime subsets",
            },
        ],
        "closed_gates": [
            gate(
                "PrimeQBooleanProjectionForLPFShellResidual",
                True,
                True,
                "The projected LPF residual coefficient b_{P,k}(q) is 0 or 1, not merely bounded by 2.",
                "none",
            ),
            gate(
                "NoDoubleMultiplicityPrimeQNoise",
                True,
                True,
                "Two-point reciprocal windows cannot contribute two LPF residual cofactors because one of two consecutive integers is even.",
                "none",
            ),
            gate(
                "PrimeQBooleanSubsetReciprocalPhaseSaving",
                False,
                False,
                "For |h|<=polylog(P), prove cancellation for sum_{q in Q_{P,k}} e(hkP/q).",
                "boolean prime-q subset reciprocal phase theorem",
            ),
            gate(
                "CompletionToExternalKloostermanOrVaughanTypeII",
                False,
                False,
                "Convert the same-row boolean subset phase to a DI/DFI/BC/FM-compatible estimate without losing pointwise P,k.",
                "completion/dispersion identity",
            ),
        ],
        "latest_narrowest_mouth": [
            "PrimeQBooleanSubsetReciprocalPhaseSaving",
            "AND CompletionToExternalKloostermanOrVaughanTypeII",
        ],
        "prime_q_boolean_projection_closed": True,
        "weighted_reciprocal_phase_saving_closed": False,
        "phi_lpf_parity_barrier_globally_broken": False,
        "row_column_unconditional_closed": False,
        "external_lemma_version_unconditional_closed": False,
        "internal_self_contained_closed": False,
        "source_hashes": source_hashes(),
    }


def build_markdown(payload: dict[str, Any]) -> str:
    """生成 Markdown 证书。"""
    theorem = payload["boolean_projection_theorem"]
    audit = payload["finite_audit"]
    lines = [
        "# Prime Matrix Phi-LPF boolean q-projection closure 审计",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['frontier_verified_date']}`",
        "",
        "## 1. 三命题选择",
        "",
        table(payload["three_claim_triage"], ["claim", "frontier", "frontier_before", "fastest_subgate", "chosen", "reason"]),
        "",
        "bounded coefficient 抽取后，本轮继续选择行/列 Phi-LPF 的 prime-q 投影子门。该门只用 thin window 与奇偶性，可完全闭合；它不证明后续相位和抵消。",
        "",
        "## 2. 布尔投影定理",
        "",
        "```text",
        f"window_bound={theorem['window_bound']}",
        f"residual_parity={theorem['residual_parity']}",
        f"boolean_projection={theorem['boolean_projection']}",
        f"phase_reduction={theorem['phase_reduction']}",
        f"not_enough={theorem['not_enough']}",
        "```",
        "",
        "关键点是：`I_q(P,k)` 最多两个点；若有两个点，它们是连续整数。LPF residual 要求 `LPF(m)>=7` 且 `m` 合成，所以 `m` 不可被 `2` 整除。两个连续整数至多一个奇数，因此每个 prime `q` 对 residual 的贡献最多为一个。",
        "",
        "## 3. 全量有限审计",
        "",
        "```text",
        f"max_prime={audit['max_prime']}",
        f"k_range={audit['k_range']}",
        f"row_count={audit['row_count']}",
        f"active_residual_row_count={audit['active_residual_row_count']}",
        f"total_R30={audit['total_R30']}",
        f"max_window_size_seen={audit['max_window_size_seen']}",
        f"total_two_point_windows={audit['total_two_point_windows']}",
        f"total_two_point_windows_with_residual={audit['total_two_point_windows_with_residual']}",
        f"max_projected_q_weight_seen={audit['max_projected_q_weight_seen']}",
        f"all_projected_q_weights_boolean={bool_text(audit['all_projected_q_weights_boolean'])}",
        f"violation_count={audit['violation_count']}",
        "```",
        "",
        "有限审计只验证实现和账本一致性；全局闭合来自上面的两点窗口加奇偶论证。",
        "",
        "代表行：",
        "",
        table(
            audit["sample_rows"],
            [
                "P",
                "k",
                "q_count",
                "R30",
                "max_window_size",
                "two_point_windows",
                "two_point_windows_with_residual",
                "max_projected_q_weight",
                "sample_q_residuals",
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
        "外部 Kloosterman/Type-II 前沿仍是后续相位门候选；本层只把系数从 bounded multiplicity 缩成 prime-q 布尔子集。",
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
        f"prime_q_boolean_projection_closed={bool_text(payload['prime_q_boolean_projection_closed'])}",
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
    print("prime_q_boolean_projection_closed=true")
    print("weighted_reciprocal_phase_saving_closed=false")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
