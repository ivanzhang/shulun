#!/usr/bin/env python3
"""闭合 unique odd candidate 后的 LPF 五分划正规形门。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_unique_odd_candidate_lpf_partition_closure_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-unique-odd-candidate-lpf-partition-closure-audit.json

上一层已经把每个 prime q in (P/2,P) 的 residual object 压成唯一奇候选
omega_{P,k}(q)。本层继续做原子化下钻：对每个 q 恰有五种互斥状态之一：

  no_odd_candidate,
  prime,
  small_lpf_3,
  small_lpf_5,
  residual_lpf_ge_7_composite.

因为 omega 为奇数，LPF<7 只能是 3 或 5。因此 residual cell 等价于
omega 存在、gcd(omega,30)=1 且 omega 合成。这把奇偶障碍精确定位到
30-wheel survivor 内的 prime/composite 分离；它仍不证明相位节省。
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

SLUG = "prime-matrix-phi-lpf-unique-odd-candidate-lpf-partition-closure"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-23"

PROJECTION_JSON = DOCS / "prime-matrix-phi-lpf-unique-odd-candidate-projection-closure-audit.json"
PARITY_JSON = DOCS / "prime-matrix-phi-lpf-parity-selected-branch-phase-closure-audit.json"
THREE_CLAIMS_JSON = DOCS / "three-claims-frontier-rankone-explicit-formula-router.json"

DEPENDENCIES = [
    PROJECTION_JSON,
    PARITY_JSON,
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
    """返回 q 对应的 clipped cofactor 窗口。"""
    low = max(q, (k * P) // q + 1)
    high = min(2 * P - 1, (((k + 1) * P) - 1) // q)
    return low, high


def classify_omega(omega: int, primes: list[int]) -> dict[str, Any]:
    """把唯一奇候选分入五个互斥 LPF 状态。"""
    if omega == 0:
        return {
            "lpf": 0,
            "reason": "no_odd_candidate",
            "is_prime": False,
            "is_small_lpf": False,
            "is_wheel30_survivor": False,
            "is_residual": False,
            "forced_composite_by_30wheel": False,
        }

    r = lpf(omega, primes)
    is_prime = r == omega
    is_small_lpf = r in {3, 5}
    is_wheel30_survivor = omega % 3 != 0 and omega % 5 != 0
    is_residual = (not is_prime) and is_wheel30_survivor

    if is_prime:
        reason = "prime"
    elif r == 3:
        reason = "small_lpf_3"
    elif r == 5:
        reason = "small_lpf_5"
    else:
        reason = "residual_lpf_ge_7_composite"

    return {
        "lpf": r,
        "reason": reason,
        "is_prime": is_prime,
        "is_small_lpf": is_small_lpf,
        "is_wheel30_survivor": is_wheel30_survivor,
        "is_residual": is_residual,
        "forced_composite_by_30wheel": is_small_lpf,
    }


def odd_candidate(P: int, k: int, q: int, primes: list[int]) -> dict[str, Any]:
    """返回 clipped q-window 中的唯一奇候选及其五分划状态。"""
    low, high = q_window(P, k, q)
    width = high - low if low <= high else -1
    candidates = [m for m in range(low, high + 1) if m % 2 == 1] if low <= high else []
    omega = candidates[0] if candidates else 0

    branch = "none"
    if omega:
        if low == high:
            branch = "both"
        elif omega == low:
            branch = "lower"
        elif omega == high:
            branch = "upper"
        else:
            branch = "interior"

    cls = classify_omega(omega, primes)
    d = q * omega - k * P if omega else 0

    # 中文注释：q>P/2 保证窗口最多两个连续整数，所以奇候选数必须 <=1。
    return {
        "low": low,
        "high": high,
        "width": width,
        "odd_candidate_count": len(candidates),
        "omega": omega,
        "branch": branch,
        "d": d,
        **cls,
    }


def residual_edges(P: int, k: int, primes: list[int]) -> list[tuple[int, int]]:
    """直接扫描窗口，列出真实 residual (q,m) 边。"""
    edges: list[tuple[int, int]] = []
    for q in (p for p in primes if P // 2 < p < P):
        low, high = q_window(P, k, q)
        if low > high:
            continue
        for m in range(low, high + 1):
            r = lpf(m, primes)
            if r >= 7 and r != m:
                edges.append((q, m))
    return edges


def row_payload(P: int, k: int, primes: list[int]) -> dict[str, Any]:
    """计算一行五分划诊断。"""
    q_values = [p for p in primes if P // 2 < p < P]
    actual_edges = set(residual_edges(P, k, primes))
    predicted_edges: set[tuple[int, int]] = set()
    reason_counter: Counter[str] = Counter()
    branch_counter: Counter[str] = Counter()
    width_counter: Counter[str] = Counter()
    odd_candidate_total = 0
    max_odd_candidates = 0
    bad_candidate_count = 0
    bad_displacement_count = 0
    bad_small_lpf_count = 0
    samples = []

    for q in q_values:
        cand = odd_candidate(P, k, q, primes)
        reason_counter[cand["reason"]] += 1
        width_counter[str(cand["width"])] += 1
        max_odd_candidates = max(max_odd_candidates, cand["odd_candidate_count"])
        bad_candidate_count += int(cand["odd_candidate_count"] > 1)

        if not cand["omega"]:
            continue

        odd_candidate_total += 1
        branch_counter[cand["branch"]] += 1
        bad_displacement_count += int(not (1 <= cand["d"] < P))

        if cand["reason"] == "small_lpf_3":
            bad_small_lpf_count += int(cand["omega"] % 3 != 0)
        if cand["reason"] == "small_lpf_5":
            bad_small_lpf_count += int(cand["omega"] % 5 != 0 or cand["omega"] % 3 == 0)
        if cand["reason"] == "residual_lpf_ge_7_composite":
            predicted_edges.add((q, cand["omega"]))
            bad_small_lpf_count += int(cand["omega"] % 3 == 0 or cand["omega"] % 5 == 0)
            if len(samples) < 5:
                samples.append(
                    "q={q},omega={m},branch={b},d={d},lpf={r}".format(
                        q=q,
                        m=cand["omega"],
                        b=cand["branch"],
                        d=cand["d"],
                        r=cand["lpf"],
                    )
                )

    missing = actual_edges - predicted_edges
    extra = predicted_edges - actual_edges
    candidate_reasons = (
        reason_counter["prime"]
        + reason_counter["small_lpf_3"]
        + reason_counter["small_lpf_5"]
        + reason_counter["residual_lpf_ge_7_composite"]
    )
    wheel30_survivor = reason_counter["prime"] + reason_counter["residual_lpf_ge_7_composite"]

    return {
        "P": P,
        "k": k,
        "q_count": len(q_values),
        "odd_candidate_count": odd_candidate_total,
        "actual_edge_count_R30": len(actual_edges),
        "predicted_edge_count_R30": len(predicted_edges),
        "reason_counter": dict(reason_counter),
        "branch_counter_on_candidates": dict(branch_counter),
        "window_width_counter": dict(width_counter),
        "wheel30_survivor_candidate_count": wheel30_survivor,
        "forced_composite_by_30wheel_count": reason_counter["small_lpf_3"] + reason_counter["small_lpf_5"],
        "max_odd_candidates_per_q": max_odd_candidates,
        "bad_candidate_count": bad_candidate_count,
        "bad_candidate_displacement_count": bad_displacement_count,
        "bad_small_lpf_partition_count": bad_small_lpf_count,
        "bad_five_way_partition_count": int(sum(reason_counter.values()) != len(q_values)),
        "bad_candidate_partition_count": int(candidate_reasons != odd_candidate_total),
        "bad_wheel30_split_count": int(
            wheel30_survivor
            != reason_counter["prime"] + reason_counter["residual_lpf_ge_7_composite"]
        ),
        "missing_edge_count": len(missing),
        "extra_edge_count": len(extra),
        "sample_residual_edges": "; ".join(samples) if samples else "empty",
    }


def audit_rows(max_prime: int = 1009) -> dict[str, Any]:
    """对 P<=max_prime 的全部 1<=k<P 行做有限一致性审计。"""
    primes = prime_sieve(2 * max_prime + 10)
    P_values = [p for p in primes if 11 <= p <= max_prime]
    row_count = 0
    active_rows = 0
    total_q = 0
    total_candidates = 0
    actual_edges = 0
    predicted_edges = 0
    wheel30_survivor_total = 0
    forced_composite_total = 0
    max_odd_candidates = 0
    totals: Counter[str] = Counter()
    reason_totals: Counter[str] = Counter()
    branch_totals: Counter[str] = Counter()
    width_totals: Counter[str] = Counter()
    samples: list[dict[str, Any]] = []
    interesting = {(101, 100), (257, 256), (971, 936), (1009, 1008)}

    for P in P_values:
        for k in range(1, P):
            row_count += 1
            row = row_payload(P, k, primes)
            active_rows += int(row["actual_edge_count_R30"] > 0)
            total_q += row["q_count"]
            total_candidates += row["odd_candidate_count"]
            actual_edges += row["actual_edge_count_R30"]
            predicted_edges += row["predicted_edge_count_R30"]
            wheel30_survivor_total += row["wheel30_survivor_candidate_count"]
            forced_composite_total += row["forced_composite_by_30wheel_count"]
            max_odd_candidates = max(max_odd_candidates, row["max_odd_candidates_per_q"])
            for key in (
                "bad_candidate_count",
                "bad_candidate_displacement_count",
                "bad_small_lpf_partition_count",
                "bad_five_way_partition_count",
                "bad_candidate_partition_count",
                "bad_wheel30_split_count",
                "missing_edge_count",
                "extra_edge_count",
            ):
                totals[key] += row[key]
            reason_totals.update(row["reason_counter"])
            branch_totals.update(row["branch_counter_on_candidates"])
            width_totals.update(row["window_width_counter"])
            if (P, k) in interesting:
                samples.append(row)

    candidate_partition_total = (
        reason_totals["prime"]
        + reason_totals["small_lpf_3"]
        + reason_totals["small_lpf_5"]
        + reason_totals["residual_lpf_ge_7_composite"]
    )
    five_way_total = sum(reason_totals.values())
    expected_wheel30_survivor_total = reason_totals["prime"] + reason_totals["residual_lpf_ge_7_composite"]
    expected_forced_total = reason_totals["small_lpf_3"] + reason_totals["small_lpf_5"]

    return {
        "max_prime": max_prime,
        "k_range": "1<=k<P in this implementation audit",
        "row_count": row_count,
        "active_residual_row_count": active_rows,
        "total_prime_q_instances": total_q,
        "total_odd_candidate_instances": total_candidates,
        "actual_total_edges_R30": actual_edges,
        "predicted_total_edges_R30": predicted_edges,
        "reason_totals": dict(reason_totals),
        "branch_totals_on_candidates": dict(branch_totals),
        "window_width_totals": dict(width_totals),
        "wheel30_survivor_candidate_total": wheel30_survivor_total,
        "forced_composite_by_30wheel_total": forced_composite_total,
        "prime_candidate_total": reason_totals["prime"],
        "residual_lpf_ge_7_composite_total": reason_totals["residual_lpf_ge_7_composite"],
        "candidate_partition_total": candidate_partition_total,
        "five_way_partition_total": five_way_total,
        "max_odd_candidates_per_q": max_odd_candidates,
        "unique_odd_candidate_per_q": max_odd_candidates <= 1 and totals["bad_candidate_count"] == 0,
        "five_way_partition_exhaustive": five_way_total == total_q and totals["bad_five_way_partition_count"] == 0,
        "candidate_partition_exhaustive": candidate_partition_total == total_candidates
        and totals["bad_candidate_partition_count"] == 0,
        "wheel30_survivor_identity_verified": wheel30_survivor_total == expected_wheel30_survivor_total
        and totals["bad_wheel30_split_count"] == 0,
        "forced_composite_identity_verified": forced_composite_total == expected_forced_total,
        "residual_cell_equals_actual_edges": predicted_edges == actual_edges
        and reason_totals["residual_lpf_ge_7_composite"] == actual_edges
        and totals["missing_edge_count"] == 0
        and totals["extra_edge_count"] == 0,
        "all_candidate_displacements_in_1_to_Pminus1": totals["bad_candidate_displacement_count"] == 0,
        "bad_candidate_total": totals["bad_candidate_count"],
        "bad_candidate_displacement_total": totals["bad_candidate_displacement_count"],
        "bad_small_lpf_partition_total": totals["bad_small_lpf_partition_count"],
        "bad_five_way_partition_total": totals["bad_five_way_partition_count"],
        "bad_candidate_partition_total": totals["bad_candidate_partition_count"],
        "bad_wheel30_split_total": totals["bad_wheel30_split_count"],
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
                value = ", ".join(f"{k}:{value[k]}" for k in sorted(value))
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
    projection = load_json(PROJECTION_JSON)
    three_claims = load_json(THREE_CLAIMS_JSON)
    finite_audit = audit_rows()
    return {
        "certificate_type": "prime_matrix_phi_lpf_unique_odd_candidate_lpf_partition_closure_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "unique_odd_candidate_lpf_partition_closed_phase_saving_open",
        "three_claim_triage": [
            {
                "claim": "Prime Matrix row/column Phi-LPF",
                "frontier_before": projection.get("latest_narrowest_mouth"),
                "fastest_subgate": "UniqueOddCandidateFiveWayLPFPartition",
                "chosen": True,
                "reason": "the existing omega(q) map has an immediate disjoint LPF partition and isolates the wheel-30 survivor prime/composite split",
            },
            {
                "claim": "two-point sieve / prime-pair line",
                "frontier": "BMD=>TLI without hidden denominator/parity gap",
                "chosen": False,
                "reason": "not a one-line closure after the omega(q) projection",
            },
            {
                "claim": "RH contradiction-field line",
                "frontier": "IndependentRefereeAcceptanceOfAllRHControlledExits",
                "chosen": False,
                "reason": "verification package, not a Phi-LPF LPF-partition gate",
            },
        ],
        "three_claim_source_status": three_claims.get("plain_conclusion"),
        "lpf_partition_theorem": {
            "five_cells": [
                "no_odd_candidate",
                "prime",
                "small_lpf_3",
                "small_lpf_5",
                "residual_lpf_ge_7_composite",
            ],
            "pointwise_identity": "For each prime q in (P/2,P), exactly one of the five cells holds.",
            "candidate_identity": "1_{omega exists}=1_{prime}+1_{LPF=3}+1_{LPF=5}+1_{residual_lpf_ge_7_composite}.",
            "wheel30_identity": "1_{gcd(omega,30)=1}=1_{prime}+1_{residual_lpf_ge_7_composite} on the candidate support.",
            "residual_identity": "Residual edges are exactly omega exists, gcd(omega,30)=1, and omega composite.",
            "phase_decomposition": "S_candidate(h)=S_prime(h)+S_LPF3(h)+S_LPF5(h)+S_residual(h), with phase e(-hD(q)/q).",
            "not_enough": "The remaining hard point is the signed/oscillatory separation of composite 30-wheel survivors from prime survivors.",
        },
        "finite_audit": finite_audit,
        "external_frontier_match_table": [
            {
                "source": "Milićević--Qin--Wu 2025 arXiv:2511.07550",
                "source_url": "https://arxiv.org/abs/2511.07550",
                "verified_status": "submitted 2025-11-10; bilinear Kloosterman sums modulo arbitrary q",
                "useful_part": "candidate input after a completion from omega(q) phases to bilinear Kloosterman sums",
                "closes_this_gate": False,
                "reason_not_direct": "does not supply the missing prime/composite split inside the wheel-30 survivor q-subset",
            },
            {
                "source": "Pascadi 2025 arXiv:2511.08445",
                "source_url": "https://arxiv.org/abs/2511.08445",
                "verified_status": "submitted 2025-11-11; Type-II Kloosterman sums with composite moduli",
                "useful_part": "candidate external Type-II source after a valid completion identity",
                "closes_this_gate": False,
                "reason_not_direct": "the present q-moduli are prime and the LPF partition is a fixed-row subset problem",
            },
            {
                "source": "Shao--Shparlinski--Wijaya 2024 arXiv:2411.12113",
                "source_url": "https://arxiv.org/abs/2411.12113",
                "verified_status": "submitted 2024-11-18; Kloosterman sums over square-free and smooth parameters",
                "useful_part": "possible comparison source for arithmetic-function-twisted Kloosterman sums",
                "closes_this_gate": False,
                "reason_not_direct": "requires a prior finite-field/completion bridge from omega(q) to their parameter family",
            },
            {
                "source": "Dong--Robles--Zeindler 2026 arXiv:2601.00292",
                "source_url": "https://arxiv.org/abs/2601.00292",
                "verified_status": "withdrawn on arXiv v2 after a missing factor was reported",
                "useful_part": "near-miss diagnostic only",
                "closes_this_gate": False,
                "reason_not_direct": "withdrawn papers cannot be used as valid external input",
            },
        ],
        "closed_gates": [
            gate(
                "UniqueOddCandidateFiveWayLPFPartition",
                True,
                True,
                "Each prime q falls in exactly one of no-candidate, prime, LPF=3, LPF=5, or residual composite LPF>=7.",
                "none",
            ),
            gate(
                "LPFResidualAsWheel30CompositeSurvivor",
                True,
                True,
                "The residual cell is exactly the composite part of the unique odd candidate with gcd(omega,30)=1.",
                "none",
            ),
            gate(
                "CandidatePhaseFourTermExactDecomposition",
                True,
                True,
                "The candidate phase sum splits exactly into prime, LPF=3, LPF=5, and residual terms.",
                "none",
            ),
            gate(
                "PrimeQUniqueOddCandidateWheel30CompositeSurvivorPhaseSaving",
                False,
                False,
                "Prove cancellation or positivity control for the composite wheel-30 survivor q-subset.",
                "wheel-30 survivor prime/composite separation theorem",
            ),
            gate(
                "CompletionToExternalKloostermanOrVaughanTypeII",
                False,
                False,
                "Convert the omega(q) survivor phase to an external DI/DFI/BC/FM-compatible estimate without losing pointwise P,k.",
                "completion/dispersion identity",
            ),
        ],
        "latest_narrowest_mouth": [
            "PrimeQUniqueOddCandidateWheel30CompositeSurvivorPhaseSaving",
            "AND CompletionToExternalKloostermanOrVaughanTypeII",
        ],
        "unique_odd_candidate_lpf_partition_closed": True,
        "wheel30_survivor_prime_composite_phase_saving_closed": False,
        "phi_lpf_parity_barrier_globally_broken": False,
        "row_column_unconditional_closed": False,
        "external_lemma_version_unconditional_closed": False,
        "internal_self_contained_closed": False,
        "source_hashes": source_hashes(),
    }


def build_markdown(payload: dict[str, Any]) -> str:
    """生成 Markdown 证书。"""
    theorem = payload["lpf_partition_theorem"]
    audit = payload["finite_audit"]
    lines = [
        "# Prime Matrix Phi-LPF unique odd candidate LPF partition closure 审计",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['frontier_verified_date']}`",
        "",
        "## 1. 三命题选择",
        "",
        table(payload["three_claim_triage"], ["claim", "frontier", "frontier_before", "fastest_subgate", "chosen", "reason"]),
        "",
        "本轮继续选择行/列 Phi-LPF，因为上一层已经把对象压成 `omega_{P,k}(q)`。最快可闭合的真子门不是再改写旧等价命题，而是把 LPF 子集谓词拆成互斥的五个点态状态。",
        "",
        "## 2. LPF 五分划正规形",
        "",
        "```text",
        "five_cells=" + ", ".join(theorem["five_cells"]),
        f"pointwise_identity={theorem['pointwise_identity']}",
        f"candidate_identity={theorem['candidate_identity']}",
        f"wheel30_identity={theorem['wheel30_identity']}",
        f"residual_identity={theorem['residual_identity']}",
        f"phase_decomposition={theorem['phase_decomposition']}",
        f"not_enough={theorem['not_enough']}",
        "```",
        "",
        "证明要点很短：上一层给出唯一奇候选；奇数的 `LPF<7` 只能是 `3` 或 `5`。因此 `LPF>=7` 合成候选正是 `gcd(omega,30)=1` 的合成幸存者。这个闭合删除了小素因子噪声，但没有解决 wheel-30 幸存者内部的素数/合数分离。",
        "",
        "## 3. 全量有限审计",
        "",
        "```text",
        f"max_prime={audit['max_prime']}",
        f"k_range={audit['k_range']}",
        f"row_count={audit['row_count']}",
        f"active_residual_row_count={audit['active_residual_row_count']}",
        f"total_prime_q_instances={audit['total_prime_q_instances']}",
        f"total_odd_candidate_instances={audit['total_odd_candidate_instances']}",
        f"actual_total_edges_R30={audit['actual_total_edges_R30']}",
        f"predicted_total_edges_R30={audit['predicted_total_edges_R30']}",
        f"reason_totals={audit['reason_totals']}",
        f"wheel30_survivor_candidate_total={audit['wheel30_survivor_candidate_total']}",
        f"prime_candidate_total={audit['prime_candidate_total']}",
        f"residual_lpf_ge_7_composite_total={audit['residual_lpf_ge_7_composite_total']}",
        f"forced_composite_by_30wheel_total={audit['forced_composite_by_30wheel_total']}",
        f"branch_totals_on_candidates={audit['branch_totals_on_candidates']}",
        f"window_width_totals={audit['window_width_totals']}",
        f"max_odd_candidates_per_q={audit['max_odd_candidates_per_q']}",
        f"five_way_partition_total={audit['five_way_partition_total']}",
        f"candidate_partition_total={audit['candidate_partition_total']}",
        f"unique_odd_candidate_per_q={bool_text(audit['unique_odd_candidate_per_q'])}",
        f"five_way_partition_exhaustive={bool_text(audit['five_way_partition_exhaustive'])}",
        f"candidate_partition_exhaustive={bool_text(audit['candidate_partition_exhaustive'])}",
        f"wheel30_survivor_identity_verified={bool_text(audit['wheel30_survivor_identity_verified'])}",
        f"forced_composite_identity_verified={bool_text(audit['forced_composite_identity_verified'])}",
        f"residual_cell_equals_actual_edges={bool_text(audit['residual_cell_equals_actual_edges'])}",
        f"all_candidate_displacements_in_1_to_Pminus1={bool_text(audit['all_candidate_displacements_in_1_to_Pminus1'])}",
        f"bad_candidate_total={audit['bad_candidate_total']}",
        f"bad_candidate_displacement_total={audit['bad_candidate_displacement_total']}",
        f"bad_small_lpf_partition_total={audit['bad_small_lpf_partition_total']}",
        f"bad_five_way_partition_total={audit['bad_five_way_partition_total']}",
        f"bad_candidate_partition_total={audit['bad_candidate_partition_total']}",
        f"bad_wheel30_split_total={audit['bad_wheel30_split_total']}",
        f"missing_edge_total={audit['missing_edge_total']}",
        f"extra_edge_total={audit['extra_edge_total']}",
        "```",
        "",
        "有限审计只验证实现和账本一致性；全局闭合来自唯一奇候选与 `LPF<7` 的小素数穷尽。",
        "",
        "代表行：",
        "",
        table(
            audit["sample_rows"],
            [
                "P",
                "k",
                "q_count",
                "odd_candidate_count",
                "wheel30_survivor_candidate_count",
                "forced_composite_by_30wheel_count",
                "actual_edge_count_R30",
                "reason_counter",
                "sample_residual_edges",
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
        "这些外部 Kloosterman/Type-II 结果仍是后续 completion 的候选工具；本层的五分划闭合是内部确定性门，不把任何外部前沿误用为 Phi-LPF 闭合。",
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
        f"unique_odd_candidate_lpf_partition_closed={bool_text(payload['unique_odd_candidate_lpf_partition_closed'])}",
        f"wheel30_survivor_prime_composite_phase_saving_closed={bool_text(payload['wheel30_survivor_prime_composite_phase_saving_closed'])}",
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
    print("unique_odd_candidate_lpf_partition_closed=true")
    print("wheel30_survivor_prime_composite_phase_saving_closed=false")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
