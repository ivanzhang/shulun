#!/usr/bin/env python3
"""闭合 Phi-LPF boolean q-projection 后的 reciprocal matching graph 门。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_matching_graph_closure_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-matching-graph-closure-audit.json

上一层已证明每个 prime q 的 LPF residual 投影权重 b(q) 属于 {0,1}。
本层继续用同一个 thin-window + parity 机制证明反向纤维也为布尔：

  * 固定 residual cofactor m>P/2 时，可行 q 落在长度 P/m<2 的整数窗口；
  * 若有两个整数，它们连续；
  * prime q>P/2>2 必为奇数；
  * 两个连续整数至多一个奇数。

因此每个 m 也至多连接一个 prime q。结合上一层 q 侧布尔投影，
R_30(P,k) 的 (q,m) reciprocal graph 是一个部分匹配。该结论仍不证明
prime-q reciprocal phase saving，但删除了双向多重图/重合纤维噪声。
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

SLUG = "prime-matrix-phi-lpf-matching-graph-closure"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-23"

BOOLEAN_Q_JSON = DOCS / "prime-matrix-phi-lpf-boolean-q-projection-closure-audit.json"
WEIGHT_EXTRACTION_JSON = DOCS / "prime-matrix-phi-lpf-weight-extraction-norm-closure-audit.json"
TYPEII_JSON = DOCS / "prime-matrix-phi-lpf-lpf-tail-typeii-obligation-audit.json"
THREE_CLAIMS_JSON = DOCS / "three-claims-frontier-rankone-explicit-formula-router.json"

DEPENDENCIES = [
    BOOLEAN_Q_JSON,
    WEIGHT_EXTRACTION_JSON,
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


def q_candidate_window_for_m(P: int, k: int, m: int) -> tuple[int, int]:
    """返回固定 m 时可能的 q 整数窗口。"""
    low = max(P // 2 + 1, (k * P) // m + 1)
    high = min(P - 1, (((k + 1) * P) - 1) // m, m)
    return low, high


def residual_pairs(P: int, k: int, primes: list[int]) -> list[tuple[int, int]]:
    """列出一行中的 (q,m) residual 边。"""
    pairs: list[tuple[int, int]] = []
    for q in (p for p in primes if P // 2 < p < P):
        low, high = reciprocal_window(P, k, q)
        if low > high:
            continue
        for m in range(low, high + 1):
            r = lpf(m, primes)
            if r >= 7 and r != m:
                pairs.append((q, m))
    return pairs


def row_matching_payload(P: int, k: int, primes: list[int]) -> dict[str, Any]:
    """计算一行 reciprocal matching graph 诊断。"""
    pairs = residual_pairs(P, k, primes)
    q_degree = Counter(q for q, _ in pairs)
    m_degree = Counter(m for _, m in pairs)
    max_q_degree = max(q_degree.values(), default=0)
    max_m_degree = max(m_degree.values(), default=0)

    max_reverse_window = 0
    two_point_reverse_windows = 0
    two_point_reverse_with_residual = 0
    for _, m in pairs:
        low, high = q_candidate_window_for_m(P, k, m)
        size = max(0, high - low + 1)
        max_reverse_window = max(max_reverse_window, size)
        if size == 2:
            two_point_reverse_windows += 1
            two_point_reverse_with_residual += 1

    sample_edges = "; ".join(f"q={q},m={m}" for q, m in pairs[:5]) if pairs else "empty"
    return {
        "P": P,
        "k": k,
        "edge_count_R30": len(pairs),
        "distinct_q_vertices": len(q_degree),
        "distinct_m_vertices": len(m_degree),
        "max_q_degree": max_q_degree,
        "max_m_degree": max_m_degree,
        "matching_graph": max_q_degree <= 1 and max_m_degree <= 1 and len(q_degree) == len(pairs) == len(m_degree),
        "max_reverse_q_window_size": max_reverse_window,
        "two_point_reverse_windows_on_edges": two_point_reverse_windows,
        "two_point_reverse_windows_with_residual": two_point_reverse_with_residual,
        "sample_edges": sample_edges,
    }


def audit_rows(max_prime: int = 1009) -> dict[str, Any]:
    """对 P<=max_prime 的全部 1<=k<P 行做有限一致性审计。"""
    primes = prime_sieve(2 * max_prime + 10)
    P_values = [p for p in primes if 11 <= p <= max_prime]
    row_count = 0
    active_rows = 0
    total_edges = 0
    max_q_degree_seen = 0
    max_m_degree_seen = 0
    max_reverse_window_seen = 0
    total_two_point_reverse_windows_on_edges = 0
    violations: list[dict[str, Any]] = []
    samples: list[dict[str, Any]] = []
    interesting = {(101, 100), (257, 256), (971, 936), (1009, 1008)}

    for P in P_values:
        for k in range(1, P):
            row_count += 1
            row = row_matching_payload(P, k, primes)
            active_rows += int(row["edge_count_R30"] > 0)
            total_edges += row["edge_count_R30"]
            max_q_degree_seen = max(max_q_degree_seen, row["max_q_degree"])
            max_m_degree_seen = max(max_m_degree_seen, row["max_m_degree"])
            max_reverse_window_seen = max(max_reverse_window_seen, row["max_reverse_q_window_size"])
            total_two_point_reverse_windows_on_edges += row["two_point_reverse_windows_on_edges"]
            if (P, k) in interesting:
                samples.append(row)
            if not row["matching_graph"]:
                violations.append(row)

    return {
        "max_prime": max_prime,
        "k_range": "1<=k<P in this implementation audit",
        "row_count": row_count,
        "active_residual_row_count": active_rows,
        "total_edges_R30": total_edges,
        "max_q_degree_seen": max_q_degree_seen,
        "max_m_degree_seen": max_m_degree_seen,
        "max_reverse_q_window_size_seen": max_reverse_window_seen,
        "total_two_point_reverse_windows_on_edges": total_two_point_reverse_windows_on_edges,
        "all_rows_matching_graph": max_q_degree_seen <= 1 and max_m_degree_seen <= 1 and not violations,
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
    boolean_q = load_json(BOOLEAN_Q_JSON)
    three_claims = load_json(THREE_CLAIMS_JSON)
    finite_audit = audit_rows()
    return {
        "certificate_type": "prime_matrix_phi_lpf_matching_graph_closure_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "reciprocal_graph_is_matching_phase_saving_open",
        "three_claim_triage": [
            {
                "claim": "Prime Matrix row/column Phi-LPF",
                "frontier_before": boolean_q.get("latest_narrowest_mouth"),
                "fastest_subgate": "ReciprocalResidualGraphIsPartialMatching",
                "chosen": True,
                "reason": "reverse-fibre parity sharpening after boolean q-projection; no new prime theorem required",
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
                "reason": "verification package, not a closable reciprocal graph fibre gate",
            },
        ],
        "three_claim_source_status": three_claims.get("plain_conclusion"),
        "matching_theorem": {
            "q_side": "Previous gate gives each q at most one residual cofactor m.",
            "m_reverse_window": "For fixed residual m>P/2, possible q lie in an integer interval of length P/m<2.",
            "prime_parity": "If two integer q candidates are present, they are consecutive; since q>P/2>2 and q is prime, at most one can be prime.",
            "matching_conclusion": "The residual (q,m) graph has maximum degree 1 on both sides; it is a partial matching.",
            "phase_reduction": "The finite sawtooth object is a sum over matched edges q<->m, equivalently over a prime subset Q_{P,k} with a unique residual cofactor map m(q).",
            "not_enough": "A matching graph still does not imply cancellation for sum_{q in Q_{P,k}} e(hkP/q); completion/dispersion remains open.",
        },
        "finite_audit": finite_audit,
        "external_frontier_match_table": [
            {
                "source": "Classical parity and twin-prime exception observation",
                "useful_part": "two consecutive integers above 2 cannot both be prime",
                "accepted_for_this_gate": True,
                "closes_phase_saving": False,
                "reason_not_direct": "turns the graph into a matching only; no exponential-sum cancellation follows",
            },
            {
                "source": "Milićević--Qin--Wu 2025 arXiv:2511.07550",
                "useful_part": "arbitrary-modulus bilinear Kloosterman power savings for later completed matching sums",
                "accepted_for_this_gate": False,
                "closes_phase_saving": False,
                "reason_not_direct": "requires inverse/Kloosterman completion of the matching graph",
            },
            {
                "source": "Pascadi 2025 arXiv:2511.08445",
                "useful_part": "composite-modulus Type-II Kloosterman amplification",
                "accepted_for_this_gate": False,
                "closes_phase_saving": False,
                "reason_not_direct": "not a pointwise fixed-row real reciprocal matching theorem",
            },
            {
                "source": "Shao--Shparlinski--Wijaya 2024/2025 arXiv:2411.12113",
                "useful_part": "Kloosterman sums over square-free and smooth parameters",
                "accepted_for_this_gate": False,
                "closes_phase_saving": False,
                "reason_not_direct": "useful after finite-field completion, not direct for the real reciprocal matching graph",
            },
        ],
        "closed_gates": [
            gate(
                "ReversePrimeQFiberBooleanForResidualM",
                True,
                True,
                "For each residual cofactor m, at most one prime q in (P/2,P) can satisfy kP<qm<(k+1)P.",
                "none",
            ),
            gate(
                "ReciprocalResidualGraphIsPartialMatching",
                True,
                True,
                "Combining q-side and m-side booleanity, the residual graph has degree at most 1 on both sides.",
                "none",
            ),
            gate(
                "PrimeQMatchingSubsetReciprocalPhaseSaving",
                False,
                False,
                "For |h|<=polylog(P), prove cancellation for the matched prime subset sum over Q_{P,k}.",
                "matching subset reciprocal phase theorem",
            ),
            gate(
                "CompletionToExternalKloostermanOrVaughanTypeII",
                False,
                False,
                "Convert the same-row matching graph to a DI/DFI/BC/FM-compatible estimate without losing pointwise P,k.",
                "completion/dispersion identity",
            ),
        ],
        "latest_narrowest_mouth": [
            "PrimeQMatchingSubsetReciprocalPhaseSaving",
            "AND CompletionToExternalKloostermanOrVaughanTypeII",
        ],
        "reciprocal_residual_graph_matching_closed": True,
        "weighted_reciprocal_phase_saving_closed": False,
        "phi_lpf_parity_barrier_globally_broken": False,
        "row_column_unconditional_closed": False,
        "external_lemma_version_unconditional_closed": False,
        "internal_self_contained_closed": False,
        "source_hashes": source_hashes(),
    }


def build_markdown(payload: dict[str, Any]) -> str:
    """生成 Markdown 证书。"""
    theorem = payload["matching_theorem"]
    audit = payload["finite_audit"]
    lines = [
        "# Prime Matrix Phi-LPF matching graph closure 审计",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['frontier_verified_date']}`",
        "",
        "## 1. 三命题选择",
        "",
        table(payload["three_claim_triage"], ["claim", "frontier", "frontier_before", "fastest_subgate", "chosen", "reason"]),
        "",
        "boolean q-projection 后，本轮继续选择行/列 Phi-LPF 的反向纤维子门。该门只用 fixed-m thin window 与 prime parity，可完全闭合；它不证明后续相位和抵消。",
        "",
        "## 2. 部分匹配定理",
        "",
        "```text",
        f"q_side={theorem['q_side']}",
        f"m_reverse_window={theorem['m_reverse_window']}",
        f"prime_parity={theorem['prime_parity']}",
        f"matching_conclusion={theorem['matching_conclusion']}",
        f"phase_reduction={theorem['phase_reduction']}",
        f"not_enough={theorem['not_enough']}",
        "```",
        "",
        "关键点是：固定 `m` 后，满足 `kP<q*m<(k+1)P` 的整数 `q` 落在长度 `<2` 的窗口内；若有两个候选，它们连续。由于 `q>P/2>2` 且 `q` 为素数，候选 prime `q` 至多一个。结合上一层每个 `q` 至多一个 residual `m`，整个 `(q,m)` 图是部分匹配。",
        "",
        "## 3. 全量有限审计",
        "",
        "```text",
        f"max_prime={audit['max_prime']}",
        f"k_range={audit['k_range']}",
        f"row_count={audit['row_count']}",
        f"active_residual_row_count={audit['active_residual_row_count']}",
        f"total_edges_R30={audit['total_edges_R30']}",
        f"max_q_degree_seen={audit['max_q_degree_seen']}",
        f"max_m_degree_seen={audit['max_m_degree_seen']}",
        f"max_reverse_q_window_size_seen={audit['max_reverse_q_window_size_seen']}",
        f"total_two_point_reverse_windows_on_edges={audit['total_two_point_reverse_windows_on_edges']}",
        f"all_rows_matching_graph={bool_text(audit['all_rows_matching_graph'])}",
        f"violation_count={audit['violation_count']}",
        "```",
        "",
        "有限审计只验证实现和账本一致性；全局闭合来自上面的反向窗口长度与 prime parity 论证。",
        "",
        "代表行：",
        "",
        table(
            audit["sample_rows"],
            [
                "P",
                "k",
                "edge_count_R30",
                "distinct_q_vertices",
                "distinct_m_vertices",
                "max_q_degree",
                "max_m_degree",
                "max_reverse_q_window_size",
                "matching_graph",
                "sample_edges",
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
        "外部 Kloosterman/Type-II 前沿仍是后续相位门候选；本层只把 reciprocal graph 从双向 thin graph 缩成部分匹配。",
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
        f"reciprocal_residual_graph_matching_closed={bool_text(payload['reciprocal_residual_graph_matching_closed'])}",
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
    print("reciprocal_residual_graph_matching_closed=true")
    print("weighted_reciprocal_phase_saving_closed=false")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
