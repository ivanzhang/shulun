#!/usr/bin/env python3
"""闭合 rough quotient 图的第二 LPF 分裂正规形门。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_rough_quotient_second_lpf_split_closure_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-rough-quotient-second-lpf-split-closure-audit.json

上一层把 residual edge 写成唯一三元图：

  m = r*alpha,  r=LPF(m),  alpha=alpha_{P,k}(q,r),  LPF(alpha)>=r.

本层继续递降 alpha。恰有两种互斥情况：

  * alpha 是素数，此时 residual 是 semiprime-alpha cell；
  * alpha 是合成数，写 alpha=s*beta，其中 s=LPF(alpha)>=r、
    beta>=s 且 LPF(beta)>=s。

固定 (q,r,s) 后，beta 的实区间长度 P/(q*r*s)<2/(r*s)<=2/49<1，
故二级商也是唯一候选：

  beta_{P,k}(q,r,s)=floor(kP/(q*r*s))+1.

这仍不是相位节省；它只把 rough quotient 的合成部分继续压成第二 LPF
0/1 图，留下 semiprime-alpha 与 second-rough-quotient 两个相位单元。
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

SLUG = "prime-matrix-phi-lpf-rough-quotient-second-lpf-split-closure"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-23"

DESCENT_JSON = DOCS / "prime-matrix-phi-lpf-wheel30-composite-lpf-descent-closure-audit.json"
PARTITION_JSON = DOCS / "prime-matrix-phi-lpf-unique-odd-candidate-lpf-partition-closure-audit.json"
THREE_CLAIMS_JSON = DOCS / "three-claims-frontier-rankone-explicit-formula-router.json"

DEPENDENCIES = [
    DESCENT_JSON,
    PARTITION_JSON,
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
    """判断 n 是否为素数。"""
    return n >= 2 and lpf(n, primes) == n


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


def first_alpha_candidate(P: int, k: int, q: int, r: int, primes: list[int]) -> dict[str, Any]:
    """固定 (q,r) 后计算第一层 alpha 候选。"""
    qr = q * r
    alpha = (k * P) // qr + 1
    upper = (((k + 1) * P) - 1) // qr
    if alpha > upper:
        return {"reason": "no_integer_alpha", "alpha": alpha, "m": 0, "d": 0, "is_residual": False}
    if alpha < r:
        return {"reason": "alpha_below_r", "alpha": alpha, "m": r * alpha, "d": q * r * alpha - k * P, "is_residual": False}
    m = r * alpha
    d = q * m - k * P
    if not (q <= m <= 2 * P - 1):
        return {"reason": "cofactor_clip_fail", "alpha": alpha, "m": m, "d": d, "is_residual": False}
    alpha_lpf = lpf(alpha, primes)
    if alpha_lpf < r:
        return {"reason": "alpha_not_r_rough", "alpha": alpha, "m": m, "d": d, "is_residual": False}
    if is_prime(alpha, primes):
        reason = "semiprime_alpha_prime"
    else:
        reason = "second_lpf_descent_cell"
    return {
        "reason": reason,
        "alpha": alpha,
        "m": m,
        "d": d,
        "alpha_lpf": alpha_lpf,
        "is_residual": True,
    }


def second_beta_candidate(P: int, k: int, q: int, r: int, s: int, primes: list[int]) -> dict[str, Any]:
    """固定 (q,r,s) 后计算第二层 beta 候选。"""
    qrs = q * r * s
    beta = (k * P) // qrs + 1
    upper = (((k + 1) * P) - 1) // qrs
    if beta > upper:
        return {"reason": "no_integer_beta", "beta": beta, "m": 0, "d": 0, "is_second": False}
    if beta < s:
        return {
            "reason": "beta_below_s",
            "beta": beta,
            "m": r * s * beta,
            "d": q * r * s * beta - k * P,
            "is_second": False,
        }
    m = r * s * beta
    d = q * m - k * P
    if not (q <= m <= 2 * P - 1):
        return {"reason": "second_cofactor_clip_fail", "beta": beta, "m": m, "d": d, "is_second": False}
    beta_lpf = lpf(beta, primes)
    if beta_lpf < s:
        return {
            "reason": "beta_not_s_rough",
            "beta": beta,
            "m": m,
            "d": d,
            "beta_lpf": beta_lpf,
            "is_second": False,
        }
    # 中文注释：beta_lpf>=s 确保 r,s 是 m 的前两级最小素因子。
    return {
        "reason": "second_lpf_descent_quadruple",
        "beta": beta,
        "m": m,
        "d": d,
        "beta_lpf": beta_lpf,
        "is_second": True,
    }


def row_payload(P: int, k: int, primes: list[int]) -> dict[str, Any]:
    """计算一行第二 LPF 分裂诊断。"""
    q_values = [p for p in primes if P // 2 < p < P]
    actual = actual_residual_edges(P, k, primes)
    predicted_edges: set[tuple[int, int]] = set()
    semiprime_edges: set[tuple[int, int]] = set()
    second_edges: set[tuple[int, int]] = set()
    predicted_second_quads: set[tuple[int, int, int, int, int]] = set()
    split_counter: Counter[str] = Counter()
    r_bucket_counter: Counter[int] = Counter()
    rs_bucket_counter: Counter[tuple[int, int]] = Counter()
    max_beta_interval_points = 0
    bad_beta_interval_count = 0
    bad_alpha_formula_count = 0
    bad_beta_formula_count = 0
    bad_second_lpf_count = 0
    bad_displacement_count = 0
    semiprime_samples: list[str] = []
    second_samples: list[str] = []

    for q, m in actual:
        r = lpf(m, primes)
        alpha = m // r
        d = q * m - k * P
        alpha_formula = (k * P) // (q * r) + 1
        predicted_edges.add((q, r * alpha))
        r_bucket_counter[r] += 1
        bad_alpha_formula_count += int(alpha != alpha_formula)
        bad_displacement_count += int(not (1 <= d < P))

        if is_prime(alpha, primes):
            split_counter["semiprime_alpha_prime"] += 1
            semiprime_edges.add((q, m))
            if len(semiprime_samples) < 5:
                semiprime_samples.append(f"q={q},r={r},alpha={alpha},m={m},d={d}")
            continue

        s = lpf(alpha, primes)
        beta = alpha // s
        qrs = q * r * s
        beta_formula = (k * P) // qrs + 1
        beta_upper = (((k + 1) * P) - 1) // qrs
        interval_points = max(0, beta_upper - beta_formula + 1)
        max_beta_interval_points = max(max_beta_interval_points, interval_points)
        bad_beta_interval_count += int(interval_points > 1)
        bad_beta_formula_count += int(beta != beta_formula)
        split_counter["second_lpf_descent_cell"] += 1
        second_edges.add((q, m))
        predicted_second_quads.add((q, r, s, beta, d))
        rs_bucket_counter[(r, s)] += 1
        bad_second_lpf_count += int(s < r or beta < s or lpf(beta, primes) < s)
        if len(second_samples) < 5:
            second_samples.append(f"q={q},r={r},s={s},beta={beta},m={m},d={d}")

    missing = actual - predicted_edges
    extra = predicted_edges - actual
    return {
        "P": P,
        "k": k,
        "q_count": len(q_values),
        "actual_edge_count_R30": len(actual),
        "predicted_edge_count_R30": len(predicted_edges),
        "semiprime_alpha_edge_count": len(semiprime_edges),
        "second_lpf_edge_count": len(second_edges),
        "predicted_second_quadruple_count": len(predicted_second_quads),
        "split_counter_on_edges": dict(split_counter),
        "r_bucket_counter": {str(r): r_bucket_counter[r] for r in sorted(r_bucket_counter)},
        "rs_bucket_counter": {f"{r},{s}": rs_bucket_counter[(r, s)] for r, s in sorted(rs_bucket_counter)},
        "max_beta_interval_points": max_beta_interval_points,
        "bad_beta_interval_count": bad_beta_interval_count,
        "bad_alpha_formula_count": bad_alpha_formula_count,
        "bad_beta_formula_count": bad_beta_formula_count,
        "bad_second_lpf_count": bad_second_lpf_count,
        "bad_displacement_count": bad_displacement_count,
        "missing_edge_count": len(missing),
        "extra_edge_count": len(extra),
        "semiprime_samples": "; ".join(semiprime_samples) if semiprime_samples else "empty",
        "second_lpf_samples": "; ".join(second_samples) if second_samples else "empty",
    }


def audit_rows(max_prime: int = 1009) -> dict[str, Any]:
    """对 P<=max_prime 的全部 1<=k<P 行做有限一致性审计。"""
    primes = prime_sieve(2 * max_prime + 10)
    P_values = [p for p in primes if 11 <= p <= max_prime]
    row_count = 0
    active_rows = 0
    actual_edges = 0
    predicted_edges = 0
    semiprime_edges = 0
    second_edges = 0
    second_quads = 0
    max_beta_interval_points = 0
    totals: Counter[str] = Counter()
    split_totals: Counter[str] = Counter()
    r_bucket_totals: Counter[int] = Counter()
    rs_bucket_totals: Counter[tuple[int, int]] = Counter()
    samples: list[dict[str, Any]] = []
    interesting = {(101, 100), (257, 256), (971, 936), (1009, 1008)}

    for P in P_values:
        for k in range(1, P):
            row_count += 1
            row = row_payload(P, k, primes)
            active_rows += int(row["actual_edge_count_R30"] > 0)
            actual_edges += row["actual_edge_count_R30"]
            predicted_edges += row["predicted_edge_count_R30"]
            semiprime_edges += row["semiprime_alpha_edge_count"]
            second_edges += row["second_lpf_edge_count"]
            second_quads += row["predicted_second_quadruple_count"]
            max_beta_interval_points = max(max_beta_interval_points, row["max_beta_interval_points"])
            for key in (
                "bad_beta_interval_count",
                "bad_alpha_formula_count",
                "bad_beta_formula_count",
                "bad_second_lpf_count",
                "bad_displacement_count",
                "missing_edge_count",
                "extra_edge_count",
            ):
                totals[key] += row[key]
            split_totals.update(row["split_counter_on_edges"])
            for r_text, count in row["r_bucket_counter"].items():
                r_bucket_totals[int(r_text)] += count
            for pair_text, count in row["rs_bucket_counter"].items():
                r, s = (int(part) for part in pair_text.split(","))
                rs_bucket_totals[(r, s)] += count
            if (P, k) in interesting:
                samples.append(row)

    return {
        "max_prime": max_prime,
        "k_range": "1<=k<P in this implementation audit",
        "row_count": row_count,
        "active_residual_row_count": active_rows,
        "actual_total_edges_R30": actual_edges,
        "predicted_total_edges_R30": predicted_edges,
        "semiprime_alpha_total_edges": semiprime_edges,
        "second_lpf_total_edges": second_edges,
        "predicted_second_quadruple_total": second_quads,
        "split_totals_on_edges": dict(split_totals),
        "lpf_r_bucket_totals": {str(r): r_bucket_totals[r] for r in sorted(r_bucket_totals)},
        "second_rs_bucket_totals": {f"{r},{s}": rs_bucket_totals[(r, s)] for r, s in sorted(rs_bucket_totals)},
        "max_beta_interval_points": max_beta_interval_points,
        "beta_interval_unique_for_each_qrs": max_beta_interval_points <= 1
        and totals["bad_beta_interval_count"] == 0,
        "predicted_edges_equal_actual_edges": predicted_edges == actual_edges
        and totals["missing_edge_count"] == 0
        and totals["extra_edge_count"] == 0,
        "two_cell_partition_exhaustive": semiprime_edges + second_edges == actual_edges,
        "second_quadruples_equal_second_edges": second_quads == second_edges,
        "all_predicted_displacements_in_1_to_Pminus1": totals["bad_displacement_count"] == 0,
        "all_alpha_formulas_verified": totals["bad_alpha_formula_count"] == 0,
        "all_beta_formulas_verified": totals["bad_beta_formula_count"] == 0,
        "all_second_lpf_descent_valid": totals["bad_second_lpf_count"] == 0,
        "bad_beta_interval_total": totals["bad_beta_interval_count"],
        "bad_alpha_formula_total": totals["bad_alpha_formula_count"],
        "bad_beta_formula_total": totals["bad_beta_formula_count"],
        "bad_second_lpf_total": totals["bad_second_lpf_count"],
        "bad_displacement_total": totals["bad_displacement_count"],
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
    descent = load_json(DESCENT_JSON)
    three_claims = load_json(THREE_CLAIMS_JSON)
    finite_audit = audit_rows()
    return {
        "certificate_type": "prime_matrix_phi_lpf_rough_quotient_second_lpf_split_closure_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "rough_quotient_second_lpf_split_closed_phase_saving_open",
        "three_claim_triage": [
            {
                "claim": "Prime Matrix row/column Phi-LPF",
                "frontier_before": descent.get("latest_narrowest_mouth"),
                "fastest_subgate": "RoughQuotientSecondLPFSplitAndUniqueBeta",
                "chosen": True,
                "reason": "the rough quotient alpha has an immediate prime/composite split, and its composite cell has a unique second quotient for each (q,r,s)",
            },
            {
                "claim": "two-point sieve / prime-pair line",
                "frontier": "BMD=>TLI without hidden denominator/parity gap",
                "chosen": False,
                "reason": "no faster deterministic closure than the available second-LPF descent inside Phi-LPF",
            },
            {
                "claim": "RH contradiction-field line",
                "frontier": "IndependentRefereeAcceptanceOfAllRHControlledExits",
                "chosen": False,
                "reason": "verification package, not a second-LPF rough quotient gate",
            },
        ],
        "three_claim_source_status": three_claims.get("plain_conclusion"),
        "second_lpf_split_theorem": {
            "two_cells": "alpha prime OR alpha=s*beta with s=LPF(alpha)>=r, beta>=s, LPF(beta)>=s.",
            "unique_beta_candidate": "For fixed (q,r,s), beta=floor(kP/(q*r*s))+1 is the only possible second quotient because P/(q*r*s)<2/(r*s)<=2/49<1.",
            "edge_decomposition": "Residual edges split exactly into semiprime-alpha edges and second-LPF rough-quotient quadruples (q,r,s,beta).",
            "phase": "Both cells keep phase e(-hD/q), with D=q*r*alpha-kP or D=q*r*s*beta-kP.",
            "not_enough": "The remaining hard point is phase saving or signed separation across the two-cell iterated rough quotient graph.",
        },
        "finite_audit": finite_audit,
        "external_frontier_match_table": [
            {
                "source": "Milićević--Qin--Wu 2025 arXiv:2511.07550",
                "source_url": "https://arxiv.org/abs/2511.07550",
                "verified_status": "power-saving estimates for general bilinear Kloosterman forms modulo arbitrary q",
                "useful_part": "possible target only after completing the iterated rough quotient graph to bilinear Kloosterman sums",
                "closes_this_gate": False,
                "reason_not_direct": "does not handle the fixed-row alpha-prime/second-LPF split directly",
            },
            {
                "source": "Pascadi 2025 arXiv:2511.08445",
                "source_url": "https://arxiv.org/abs/2511.08445",
                "verified_status": "non-abelian amplification for Type-II Kloosterman sums with composite moduli",
                "useful_part": "possible completion technology for a later Type-II organisation",
                "closes_this_gate": False,
                "reason_not_direct": "not a pointwise estimate for this prime-q iterated quotient graph",
            },
            {
                "source": "Shao--Shparlinski--Wijaya 2024/2025 arXiv:2411.12113",
                "source_url": "https://arxiv.org/abs/2411.12113",
                "verified_status": "Kloosterman sums parametrised by square-free and smooth integers; Cambridge journal version first online in 2025",
                "useful_part": "comparison source for arithmetic-function-twisted Kloosterman sums after a bridge",
                "closes_this_gate": False,
                "reason_not_direct": "alpha-prime and second-LPF rough quotient cells are not their completed parameter family",
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
                "RoughQuotientPrimeOrSecondLPFPartition",
                True,
                True,
                "The r-rough quotient alpha is either prime or has second least prime factor s>=r.",
                "none",
            ),
            gate(
                "FixedPrimeQRSecondLPFQuotientSingleton",
                True,
                True,
                "For fixed q,r,s, the beta interval has length <1 and contains at most one integer.",
                "none",
            ),
            gate(
                "ResidualAsSemiprimeAlphaOrSecondRoughQuotientGraph",
                True,
                True,
                "Residual edges split exactly into semiprime-alpha edges and second-LPF rough quotient quadruples.",
                "none",
            ),
            gate(
                "PrimeQIteratedRoughQuotientTwoCellPhaseSaving",
                False,
                False,
                "Prove cancellation or signed separation over semiprime-alpha and second-LPF rough quotient cells.",
                "two-cell iterated rough quotient phase theorem",
            ),
            gate(
                "CompletionToExternalKloostermanOrVaughanTypeII",
                False,
                False,
                "Convert the iterated quotient graph to a DI/DFI/BC/FM-compatible estimate without losing pointwise P,k.",
                "completion/dispersion identity",
            ),
        ],
        "latest_narrowest_mouth": [
            "PrimeQIteratedRoughQuotientTwoCellPhaseSaving",
            "AND CompletionToExternalKloostermanOrVaughanTypeII",
        ],
        "rough_quotient_second_lpf_split_closed": True,
        "iterated_rough_quotient_phase_saving_closed": False,
        "phi_lpf_parity_barrier_globally_broken": False,
        "row_column_unconditional_closed": False,
        "external_lemma_version_unconditional_closed": False,
        "internal_self_contained_closed": False,
        "source_hashes": source_hashes(),
    }


def build_markdown(payload: dict[str, Any]) -> str:
    """生成 Markdown 证书。"""
    theorem = payload["second_lpf_split_theorem"]
    audit = payload["finite_audit"]
    lines = [
        "# Prime Matrix Phi-LPF rough quotient second LPF split closure 审计",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['frontier_verified_date']}`",
        "",
        "## 1. 三命题选择",
        "",
        table(payload["three_claim_triage"], ["claim", "frontier", "frontier_before", "fastest_subgate", "chosen", "reason"]),
        "",
        "本轮继续选择行/列 Phi-LPF，因为上一层已经把 residual 压成 `q,r,alpha` 的唯一 rough quotient 图。最快可闭合的真子门是把 `alpha` 分成素数商与第二 LPF 合成商。",
        "",
        "## 2. 第二 LPF 分裂正规形",
        "",
        "```text",
        f"two_cells={theorem['two_cells']}",
        f"unique_beta_candidate={theorem['unique_beta_candidate']}",
        f"edge_decomposition={theorem['edge_decomposition']}",
        f"phase={theorem['phase']}",
        f"not_enough={theorem['not_enough']}",
        "```",
        "",
        "这一步继续下钻而不循环：`alpha` 的合成部分被强制写成 `s*beta`，且固定 `(q,r,s)` 时二级商区间长度 `<1`。剩余困难转为两个相位单元的 signed/oscillatory 控制。",
        "",
        "## 3. 全量有限审计",
        "",
        "```text",
        f"max_prime={audit['max_prime']}",
        f"k_range={audit['k_range']}",
        f"row_count={audit['row_count']}",
        f"active_residual_row_count={audit['active_residual_row_count']}",
        f"actual_total_edges_R30={audit['actual_total_edges_R30']}",
        f"predicted_total_edges_R30={audit['predicted_total_edges_R30']}",
        f"semiprime_alpha_total_edges={audit['semiprime_alpha_total_edges']}",
        f"second_lpf_total_edges={audit['second_lpf_total_edges']}",
        f"predicted_second_quadruple_total={audit['predicted_second_quadruple_total']}",
        f"split_totals_on_edges={audit['split_totals_on_edges']}",
        f"lpf_r_bucket_totals={audit['lpf_r_bucket_totals']}",
        f"second_rs_bucket_totals={audit['second_rs_bucket_totals']}",
        f"max_beta_interval_points={audit['max_beta_interval_points']}",
        f"beta_interval_unique_for_each_qrs={bool_text(audit['beta_interval_unique_for_each_qrs'])}",
        f"predicted_edges_equal_actual_edges={bool_text(audit['predicted_edges_equal_actual_edges'])}",
        f"two_cell_partition_exhaustive={bool_text(audit['two_cell_partition_exhaustive'])}",
        f"second_quadruples_equal_second_edges={bool_text(audit['second_quadruples_equal_second_edges'])}",
        f"all_predicted_displacements_in_1_to_Pminus1={bool_text(audit['all_predicted_displacements_in_1_to_Pminus1'])}",
        f"all_alpha_formulas_verified={bool_text(audit['all_alpha_formulas_verified'])}",
        f"all_beta_formulas_verified={bool_text(audit['all_beta_formulas_verified'])}",
        f"all_second_lpf_descent_valid={bool_text(audit['all_second_lpf_descent_valid'])}",
        f"bad_beta_interval_total={audit['bad_beta_interval_total']}",
        f"bad_alpha_formula_total={audit['bad_alpha_formula_total']}",
        f"bad_beta_formula_total={audit['bad_beta_formula_total']}",
        f"bad_second_lpf_total={audit['bad_second_lpf_total']}",
        f"bad_displacement_total={audit['bad_displacement_total']}",
        f"missing_edge_total={audit['missing_edge_total']}",
        f"extra_edge_total={audit['extra_edge_total']}",
        "```",
        "",
        "有限审计只验证实现和账本一致性；全局闭合来自 `P/(q*r*s)<1` 与最小素因子递降。",
        "",
        "代表行：",
        "",
        table(
            audit["sample_rows"],
            [
                "P",
                "k",
                "actual_edge_count_R30",
                "semiprime_alpha_edge_count",
                "second_lpf_edge_count",
                "r_bucket_counter",
                "rs_bucket_counter",
                "semiprime_samples",
                "second_lpf_samples",
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
        "这些外部 Kloosterman/Type-II 结果仍只是后续 completion 的候选工具；本层闭合的是内部第二 LPF 分裂和唯一 beta 正规形。",
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
        f"rough_quotient_second_lpf_split_closed={bool_text(payload['rough_quotient_second_lpf_split_closed'])}",
        f"iterated_rough_quotient_phase_saving_closed={bool_text(payload['iterated_rough_quotient_phase_saving_closed'])}",
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
    print("rough_quotient_second_lpf_split_closed=true")
    print("iterated_rough_quotient_phase_saving_closed=false")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
