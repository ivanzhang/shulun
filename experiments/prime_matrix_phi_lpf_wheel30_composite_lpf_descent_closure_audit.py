#!/usr/bin/env python3
"""闭合 30-wheel composite survivor 的 LPF 递降正规形门。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_wheel30_composite_lpf_descent_closure_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-wheel30-composite-lpf-descent-closure-audit.json

上一层把唯一奇候选的 residual cell 精确定位为 30-wheel survivor 中的
composite 部分。本层继续递降：若 omega 是 residual composite，则

  omega = r*a,  r=LPF(omega),  7<=r<=sqrt(2P-1),  LPF(a)>=r.

反过来，固定 prime q in (P/2,P) 与 prime r>=7 后，商 a 必须落在

  kP < q*r*a < (k+1)P

的整数区间内。该实区间长度 P/(q*r)<2/r<1，所以最多一个整数商；唯一候选是

  alpha_{P,k}(q,r)=floor(kP/(q*r))+1.

因此 residual edge 等价于这个 alpha 同时满足 a>=r、q<=r*a<=2P-1、
LPF(a)>=r。本层不证明相位节省；它把剩余对象压成 prime q 与小 LPF r 的
唯一 rough-quotient 候选相位。
"""

from __future__ import annotations

import hashlib
import json
import math
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-wheel30-composite-lpf-descent-closure"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-23"

PARTITION_JSON = DOCS / "prime-matrix-phi-lpf-unique-odd-candidate-lpf-partition-closure-audit.json"
PROJECTION_JSON = DOCS / "prime-matrix-phi-lpf-unique-odd-candidate-projection-closure-audit.json"
THREE_CLAIMS_JSON = DOCS / "three-claims-frontier-rankone-explicit-formula-router.json"

DEPENDENCIES = [
    PARTITION_JSON,
    PROJECTION_JSON,
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


def q_window(P: int, k: int, q: int) -> tuple[int, int]:
    """返回 q 侧 clipped cofactor 窗口。"""
    low = max(q, (k * P) // q + 1)
    high = min(2 * P - 1, (((k + 1) * P) - 1) // q)
    return low, high


def actual_residual_edges(P: int, k: int, primes: list[int]) -> set[tuple[int, int]]:
    """直接扫描 q-window，得到真实 residual (q,m) 边。"""
    edges: set[tuple[int, int]] = set()
    for q in (p for p in primes if P // 2 < p < P):
        low, high = q_window(P, k, q)
        if low > high:
            continue
        for m in range(low, high + 1):
            r = lpf(m, primes)
            if r >= 7 and r != m:
                edges.add((q, m))
    return edges


def rough_quotient_candidate(P: int, k: int, q: int, r: int, primes: list[int]) -> dict[str, Any]:
    """固定 (q,r) 后计算唯一 rough quotient 候选。"""
    qr = q * r
    alpha = (k * P) // qr + 1
    upper = (((k + 1) * P) - 1) // qr
    if alpha > upper:
        return {
            "reason": "no_integer_quotient",
            "alpha": alpha,
            "m": 0,
            "d": 0,
            "lpf_alpha": 0,
            "is_residual": False,
        }

    if alpha < r:
        return {
            "reason": "quotient_below_lpf",
            "alpha": alpha,
            "m": r * alpha,
            "d": q * r * alpha - k * P,
            "lpf_alpha": lpf(alpha, primes) if alpha > 1 else 0,
            "is_residual": False,
        }

    m = r * alpha
    d = q * m - k * P
    if not (q <= m <= 2 * P - 1):
        return {
            "reason": "cofactor_clip_fail",
            "alpha": alpha,
            "m": m,
            "d": d,
            "lpf_alpha": lpf(alpha, primes),
            "is_residual": False,
        }

    alpha_lpf = lpf(alpha, primes)
    if alpha_lpf < r:
        return {
            "reason": "quotient_not_r_rough",
            "alpha": alpha,
            "m": m,
            "d": d,
            "lpf_alpha": alpha_lpf,
            "is_residual": False,
        }

    # 中文注释：alpha_lpf>=r 时，r 是 r*alpha 的最小素因子，且自动避开 2,3,5。
    return {
        "reason": "residual_lpf_descent_triple",
        "alpha": alpha,
        "m": m,
        "d": d,
        "lpf_alpha": alpha_lpf,
        "is_residual": True,
    }


def row_payload(P: int, k: int, primes: list[int]) -> dict[str, Any]:
    """计算一行 LPF 递降正规形诊断。"""
    q_values = [p for p in primes if P // 2 < p < P]
    r_values = [p for p in primes if 7 <= p and p * p <= 2 * P - 1]
    actual = actual_residual_edges(P, k, primes)
    predicted_edges: set[tuple[int, int]] = set()
    predicted_triples: set[tuple[int, int, int, int]] = set()
    reverse_m_seen: Counter[int] = Counter()
    q_reason_counter: Counter[str] = Counter()
    r_bucket_counter: Counter[int] = Counter()
    max_quotient_interval_points = 0
    bad_interval_count = 0
    bad_displacement_count = 0
    bad_lpf_descent_count = 0
    samples: list[str] = []

    for q in q_values:
        for r in r_values:
            qr = q * r
            alpha = (k * P) // qr + 1
            upper = (((k + 1) * P) - 1) // qr
            interval_points = max(0, upper - alpha + 1)
            max_quotient_interval_points = max(max_quotient_interval_points, interval_points)
            bad_interval_count += int(interval_points > 1)

            cand = rough_quotient_candidate(P, k, q, r, primes)
            q_reason_counter[cand["reason"]] += 1
            if not cand["is_residual"]:
                continue

            m = cand["m"]
            a = cand["alpha"]
            d = cand["d"]
            predicted_edges.add((q, m))
            predicted_triples.add((q, r, a, d))
            reverse_m_seen[m] += 1
            r_bucket_counter[r] += 1
            bad_displacement_count += int(not (1 <= d < P))
            bad_lpf_descent_count += int(lpf(m, primes) != r or lpf(a, primes) < r)
            if len(samples) < 5:
                samples.append(f"q={q},r={r},a={a},m={m},d={d}")

    missing = actual - predicted_edges
    extra = predicted_edges - actual
    return {
        "P": P,
        "k": k,
        "q_count": len(q_values),
        "r_count": len(r_values),
        "qr_pair_count": len(q_values) * len(r_values),
        "actual_edge_count_R30": len(actual),
        "predicted_edge_count_R30": len(predicted_edges),
        "predicted_triple_count": len(predicted_triples),
        "reason_counter_on_qr": dict(q_reason_counter),
        "r_bucket_counter": {str(r): r_bucket_counter[r] for r in sorted(r_bucket_counter)},
        "max_quotient_interval_points": max_quotient_interval_points,
        "max_reverse_m_multiplicity": max(reverse_m_seen.values(), default=0),
        "bad_quotient_interval_count": bad_interval_count,
        "bad_displacement_count": bad_displacement_count,
        "bad_lpf_descent_count": bad_lpf_descent_count,
        "missing_edge_count": len(missing),
        "extra_edge_count": len(extra),
        "sample_descent_triples": "; ".join(samples) if samples else "empty",
    }


def audit_rows(max_prime: int = 1009) -> dict[str, Any]:
    """对 P<=max_prime 的全部 1<=k<P 行做有限一致性审计。"""
    primes = prime_sieve(2 * max_prime + 10)
    P_values = [p for p in primes if 11 <= p <= max_prime]
    row_count = 0
    active_rows = 0
    total_q = 0
    total_r = 0
    total_qr = 0
    actual_edges = 0
    predicted_edges = 0
    predicted_triples = 0
    max_interval_points = 0
    max_reverse_m_multiplicity = 0
    max_r_seen = 0
    max_alpha_seen = 0
    totals: Counter[str] = Counter()
    reason_totals: Counter[str] = Counter()
    r_bucket_totals: Counter[int] = Counter()
    samples: list[dict[str, Any]] = []
    interesting = {(101, 100), (257, 256), (971, 936), (1009, 1008)}

    for P in P_values:
        for k in range(1, P):
            row_count += 1
            row = row_payload(P, k, primes)
            active_rows += int(row["actual_edge_count_R30"] > 0)
            total_q += row["q_count"]
            total_r += row["r_count"]
            total_qr += row["qr_pair_count"]
            actual_edges += row["actual_edge_count_R30"]
            predicted_edges += row["predicted_edge_count_R30"]
            predicted_triples += row["predicted_triple_count"]
            max_interval_points = max(max_interval_points, row["max_quotient_interval_points"])
            max_reverse_m_multiplicity = max(
                max_reverse_m_multiplicity, row["max_reverse_m_multiplicity"]
            )
            for key in (
                "bad_quotient_interval_count",
                "bad_displacement_count",
                "bad_lpf_descent_count",
                "missing_edge_count",
                "extra_edge_count",
            ):
                totals[key] += row[key]
            reason_totals.update(row["reason_counter_on_qr"])
            for r_text, count in row["r_bucket_counter"].items():
                r = int(r_text)
                r_bucket_totals[r] += count
                max_r_seen = max(max_r_seen, r)
            if row["sample_descent_triples"] != "empty":
                for item in row["sample_descent_triples"].split("; "):
                    for part in item.split(","):
                        if part.startswith("a="):
                            max_alpha_seen = max(max_alpha_seen, int(part.split("=")[1]))
            if (P, k) in interesting:
                samples.append(row)

    return {
        "max_prime": max_prime,
        "k_range": "1<=k<P in this implementation audit",
        "row_count": row_count,
        "active_residual_row_count": active_rows,
        "total_prime_q_instances": total_q,
        "total_lpf_r_row_instances": total_r,
        "total_qr_pair_instances": total_qr,
        "actual_total_edges_R30": actual_edges,
        "predicted_total_edges_R30": predicted_edges,
        "predicted_total_triples": predicted_triples,
        "reason_totals_on_qr": dict(reason_totals),
        "lpf_r_bucket_totals": {str(r): r_bucket_totals[r] for r in sorted(r_bucket_totals)},
        "distinct_lpf_r_count": len(r_bucket_totals),
        "max_lpf_r_seen": max_r_seen,
        "max_sample_alpha_seen": max_alpha_seen,
        "max_quotient_interval_points": max_interval_points,
        "max_reverse_m_multiplicity": max_reverse_m_multiplicity,
        "quotient_interval_unique_for_each_qr": max_interval_points <= 1
        and totals["bad_quotient_interval_count"] == 0,
        "predicted_edges_equal_actual_edges": predicted_edges == actual_edges
        and totals["missing_edge_count"] == 0
        and totals["extra_edge_count"] == 0,
        "predicted_triples_equal_edges": predicted_triples == predicted_edges,
        "all_predicted_displacements_in_1_to_Pminus1": totals["bad_displacement_count"] == 0,
        "all_predicted_triples_have_lpf_descent": totals["bad_lpf_descent_count"] == 0,
        "reverse_m_multiplicity_le_1": max_reverse_m_multiplicity <= 1,
        "bad_quotient_interval_total": totals["bad_quotient_interval_count"],
        "bad_displacement_total": totals["bad_displacement_count"],
        "bad_lpf_descent_total": totals["bad_lpf_descent_count"],
        "missing_edge_total": totals["missing_edge_count"],
        "extra_edge_total": totals["extra_edge_count"],
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
            elif isinstance(value, dict):
                value = ", ".join(f"{k}:{value[k]}" for k in sorted(value, key=str))
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
    partition = load_json(PARTITION_JSON)
    three_claims = load_json(THREE_CLAIMS_JSON)
    finite_audit = audit_rows()
    return {
        "certificate_type": "prime_matrix_phi_lpf_wheel30_composite_lpf_descent_closure_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "wheel30_composite_lpf_descent_closed_phase_saving_open",
        "three_claim_triage": [
            {
                "claim": "Prime Matrix row/column Phi-LPF",
                "frontier_before": partition.get("latest_narrowest_mouth"),
                "fastest_subgate": "Wheel30CompositeLPFDescentUniqueRoughQuotient",
                "chosen": True,
                "reason": "the composite survivor has an immediate least-prime-factor descent with a unique quotient candidate for each (q,r)",
            },
            {
                "claim": "two-point sieve / prime-pair line",
                "frontier": "BMD=>TLI without hidden denominator/parity gap",
                "chosen": False,
                "reason": "slower than the deterministic LPF descent now available inside the Phi-LPF branch",
            },
            {
                "claim": "RH contradiction-field line",
                "frontier": "IndependentRefereeAcceptanceOfAllRHControlledExits",
                "chosen": False,
                "reason": "verification package, not a closable wheel-30 composite descent gate",
            },
        ],
        "three_claim_source_status": three_claims.get("plain_conclusion"),
        "lpf_descent_theorem": {
            "factorization": "residual omega=r*a with r=LPF(omega), 7<=r<=sqrt(2P-1), a>=r, LPF(a)>=r.",
            "unique_quotient_candidate": "For fixed (q,r), alpha=floor(kP/(q*r))+1 is the only possible quotient because P/(q*r)<2/r<1.",
            "edge_equivalence": "A residual edge is exactly a prime pair (q,r) with alpha<=floor(((k+1)P-1)/(q*r)), alpha>=r, q<=r*alpha<=2P-1, and LPF(alpha)>=r.",
            "phase": "The residual phase is e(-hD(q,r)/q), D(q,r)=q*r*alpha_{P,k}(q,r)-kP.",
            "normal_form": "The residual q-subset becomes a sparse prime-q/small-prime-r rough-quotient candidate graph with 0/1 coefficients.",
            "not_enough": "The remaining hard point is cancellation or signed separation on this rough-quotient graph.",
        },
        "finite_audit": finite_audit,
        "external_frontier_match_table": [
            {
                "source": "Milićević--Qin--Wu 2025 arXiv:2511.07550",
                "source_url": "https://arxiv.org/abs/2511.07550",
                "verified_status": "power-saving bilinear Kloosterman estimates modulo arbitrary q",
                "useful_part": "a target theorem after turning the (q,r,alpha) graph into a genuine bilinear Kloosterman form",
                "closes_this_gate": False,
                "reason_not_direct": "the present phase still has a floor-defined rough quotient and a fixed-row LPF predicate",
            },
            {
                "source": "Pascadi 2025 arXiv:2511.08445",
                "source_url": "https://arxiv.org/abs/2511.08445",
                "verified_status": "non-abelian amplification for Type-II Kloosterman sums with composite moduli",
                "useful_part": "candidate completion technology if the rough quotient graph is reorganised into composite-modulus Type-II sums",
                "closes_this_gate": False,
                "reason_not_direct": "does not estimate the pointwise prime-q/small-r graph directly",
            },
            {
                "source": "Shao--Shparlinski--Wijaya 2024/2025 arXiv:2411.12113",
                "source_url": "https://arxiv.org/abs/2411.12113",
                "verified_status": "Kloosterman sums parametrised by square-free and smooth integers; journal version appeared online in 2025",
                "useful_part": "relevant to arithmetic-function-twisted Kloosterman sums after a completion bridge",
                "closes_this_gate": False,
                "reason_not_direct": "rough quotient candidates are neither their square-free/smooth parameter family nor already completed Kloosterman sums",
            },
            {
                "source": "Dong--Robles--Zeindler 2026 arXiv:2601.00292",
                "source_url": "https://arxiv.org/abs/2601.00292",
                "verified_status": "withdrawn on arXiv v2 after a missing factor was reported",
                "useful_part": "near-miss diagnostic only",
                "closes_this_gate": False,
                "reason_not_direct": "withdrawn papers cannot be used as an admissible external theorem",
            },
        ],
        "closed_gates": [
            gate(
                "Wheel30CompositeLPFDescentUniqueRoughQuotient",
                True,
                True,
                "Every residual wheel-30 composite survivor is uniquely r*a with r=LPF and a r-rough.",
                "none",
            ),
            gate(
                "FixedPrimeQSmallRQuotientIntervalSingleton",
                True,
                True,
                "For fixed q and r, the quotient interval has length <1 and has at most one integer alpha.",
                "none",
            ),
            gate(
                "ResidualAsPrimeQSmallRoughQuotientCandidateGraph",
                True,
                True,
                "Residual edges are exactly the 0/1 graph of prime q, small prime r, and the unique rough quotient alpha.",
                "none",
            ),
            gate(
                "PrimeQSmallRoughQuotientCandidatePhaseSaving",
                False,
                False,
                "Prove cancellation or signed separation over the resulting prime-q/small-r rough-quotient graph.",
                "rough quotient graph phase theorem",
            ),
            gate(
                "CompletionToExternalKloostermanOrVaughanTypeII",
                False,
                False,
                "Convert the rough-quotient graph phase to a DI/DFI/BC/FM-compatible estimate without losing pointwise P,k.",
                "completion/dispersion identity",
            ),
        ],
        "latest_narrowest_mouth": [
            "PrimeQSmallRoughQuotientCandidatePhaseSaving",
            "AND CompletionToExternalKloostermanOrVaughanTypeII",
        ],
        "wheel30_composite_lpf_descent_closed": True,
        "rough_quotient_graph_phase_saving_closed": False,
        "phi_lpf_parity_barrier_globally_broken": False,
        "row_column_unconditional_closed": False,
        "external_lemma_version_unconditional_closed": False,
        "internal_self_contained_closed": False,
        "source_hashes": source_hashes(),
    }


def build_markdown(payload: dict[str, Any]) -> str:
    """生成 Markdown 证书。"""
    theorem = payload["lpf_descent_theorem"]
    audit = payload["finite_audit"]
    lines = [
        "# Prime Matrix Phi-LPF wheel30 composite LPF descent closure 审计",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['frontier_verified_date']}`",
        "",
        "## 1. 三命题选择",
        "",
        table(payload["three_claim_triage"], ["claim", "frontier", "frontier_before", "fastest_subgate", "chosen", "reason"]),
        "",
        "本轮继续选择行/列 Phi-LPF，因为上一层留下的对象已经是 `30`-wheel survivor 的 composite 部分。最快可闭合的真子门是把该 composite survivor 按最小素因子 `r` 递降为唯一 rough quotient 候选。",
        "",
        "## 2. LPF 递降正规形",
        "",
        "```text",
        f"factorization={theorem['factorization']}",
        f"unique_quotient_candidate={theorem['unique_quotient_candidate']}",
        f"edge_equivalence={theorem['edge_equivalence']}",
        f"phase={theorem['phase']}",
        f"normal_form={theorem['normal_form']}",
        f"not_enough={theorem['not_enough']}",
        "```",
        "",
        "这一步是真推进：`omega(q)` 的 composite 判断不再是黑箱，而被替换为小素数 `r<=sqrt(2P-1)` 与唯一商 `alpha=floor(kP/(q*r))+1` 的 0/1 图。相位节省仍未得到。",
        "",
        "## 3. 全量有限审计",
        "",
        "```text",
        f"max_prime={audit['max_prime']}",
        f"k_range={audit['k_range']}",
        f"row_count={audit['row_count']}",
        f"active_residual_row_count={audit['active_residual_row_count']}",
        f"total_prime_q_instances={audit['total_prime_q_instances']}",
        f"total_lpf_r_row_instances={audit['total_lpf_r_row_instances']}",
        f"total_qr_pair_instances={audit['total_qr_pair_instances']}",
        f"actual_total_edges_R30={audit['actual_total_edges_R30']}",
        f"predicted_total_edges_R30={audit['predicted_total_edges_R30']}",
        f"predicted_total_triples={audit['predicted_total_triples']}",
        f"reason_totals_on_qr={audit['reason_totals_on_qr']}",
        f"lpf_r_bucket_totals={audit['lpf_r_bucket_totals']}",
        f"distinct_lpf_r_count={audit['distinct_lpf_r_count']}",
        f"max_lpf_r_seen={audit['max_lpf_r_seen']}",
        f"max_quotient_interval_points={audit['max_quotient_interval_points']}",
        f"max_reverse_m_multiplicity={audit['max_reverse_m_multiplicity']}",
        f"quotient_interval_unique_for_each_qr={bool_text(audit['quotient_interval_unique_for_each_qr'])}",
        f"predicted_edges_equal_actual_edges={bool_text(audit['predicted_edges_equal_actual_edges'])}",
        f"predicted_triples_equal_edges={bool_text(audit['predicted_triples_equal_edges'])}",
        f"all_predicted_displacements_in_1_to_Pminus1={bool_text(audit['all_predicted_displacements_in_1_to_Pminus1'])}",
        f"all_predicted_triples_have_lpf_descent={bool_text(audit['all_predicted_triples_have_lpf_descent'])}",
        f"reverse_m_multiplicity_le_1={bool_text(audit['reverse_m_multiplicity_le_1'])}",
        f"bad_quotient_interval_total={audit['bad_quotient_interval_total']}",
        f"bad_displacement_total={audit['bad_displacement_total']}",
        f"bad_lpf_descent_total={audit['bad_lpf_descent_total']}",
        f"missing_edge_total={audit['missing_edge_total']}",
        f"extra_edge_total={audit['extra_edge_total']}",
        "```",
        "",
        "有限审计只验证实现和账本一致性；全局闭合来自 `P/(q*r)<2/r<1` 与最小素因子分解。",
        "",
        "代表行：",
        "",
        table(
            audit["sample_rows"],
            [
                "P",
                "k",
                "q_count",
                "r_count",
                "actual_edge_count_R30",
                "predicted_edge_count_R30",
                "reason_counter_on_qr",
                "r_bucket_counter",
                "sample_descent_triples",
            ],
        ),
        "",
        "## 4. 外部前沿匹配",
        "",
        table(
            payload["external_frontier_match_table"],
            ["source", "source_url", "verified_status", "useful_part", "closes_this_gate", "reason_not_direct"],
        ),
        "",
        "这些外部 Kloosterman/Type-II 结果仍只是 completion 后的候选工具；本层闭合的是内部 LPF 递降与唯一商正规形。",
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
        f"wheel30_composite_lpf_descent_closed={bool_text(payload['wheel30_composite_lpf_descent_closed'])}",
        f"rough_quotient_graph_phase_saving_closed={bool_text(payload['rough_quotient_graph_phase_saving_closed'])}",
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
    print("wheel30_composite_lpf_descent_closed=true")
    print("rough_quotient_graph_phase_saving_closed=false")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
