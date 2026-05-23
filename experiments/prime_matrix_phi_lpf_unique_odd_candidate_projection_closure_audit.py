#!/usr/bin/env python3
"""闭合 Phi-LPF parity-selected branch 后的 unique odd candidate 投影门。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_unique_odd_candidate_projection_closure_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-unique-odd-candidate-projection-closure-audit.json

上一层已证明 two-point floor window 的端点侧由奇偶性唯一选择。本层继续把
整个 residual graph 压成 q 上的单值候选函数：

  J_q(P,k)=[max(q,floor(kP/q)+1), min(2P-1,floor(((k+1)P-1)/q))].

因为 q>P/2，J_q 至多含两个连续整数，故至多含一个奇数。记这个奇数为
omega_{P,k}(q)；若不存在奇数则 q 无 residual 边。则

  (q,m) 是 residual edge
  iff m=omega_{P,k}(q), m composite, LPF(m)>=7.

因此 LPF 条件只是在 q 的单值候选上做 subset predicate；它不再携带分支或
多重图自由度。剩余硬点仍是对这个 LPF-selected q 子集的相位节省。
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

SLUG = "prime-matrix-phi-lpf-unique-odd-candidate-projection-closure"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-23"

PARITY_JSON = DOCS / "prime-matrix-phi-lpf-parity-selected-branch-phase-closure-audit.json"
FLOOR_JSON = DOCS / "prime-matrix-phi-lpf-floor-residue-branch-phase-closure-audit.json"
THREE_CLAIMS_JSON = DOCS / "three-claims-frontier-rankone-explicit-formula-router.json"

DEPENDENCIES = [
    PARITY_JSON,
    FLOOR_JSON,
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


def odd_candidate(P: int, k: int, q: int) -> dict[str, Any]:
    """返回 clipped q-window 中的唯一奇候选。"""
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

    if omega:
        r = lpf(omega, PRIME_CACHE)
        is_residual = r >= 7 and r != omega
        reason = "residual_lpf_ge_7_composite" if is_residual else "prime" if r == omega else f"small_lpf_{r}"
        d = q * omega - k * P
    else:
        r = 0
        is_residual = False
        reason = "no_odd_candidate"
        d = 0

    # 中文注释：q>P/2 时 clipped 窗口长度小于 2，因此奇候选数必须 <=1。
    return {
        "low": low,
        "high": high,
        "width": width,
        "odd_candidate_count": len(candidates),
        "omega": omega,
        "branch": branch,
        "lpf": r,
        "reason": reason,
        "is_residual": is_residual,
        "d": d,
    }


def residual_edges(P: int, k: int, primes: list[int]) -> list[tuple[int, int]]:
    """列出一行中的 residual (q,m) 边。"""
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
    """计算一行 unique odd candidate 投影诊断。"""
    q_values = [p for p in primes if P // 2 < p < P]
    actual_edges = set(residual_edges(P, k, primes))
    predicted_edges: set[tuple[int, int]] = set()
    reason_counter: Counter[str] = Counter()
    branch_counter: Counter[str] = Counter()
    width_counter: Counter[str] = Counter()
    odd_candidate_total = 0
    max_odd_candidates = 0
    bad_candidate_count = 0
    bad_phase_count = 0
    samples = []

    for q in q_values:
        cand = odd_candidate(P, k, q)
        width_counter[str(cand["width"])] += 1
        max_odd_candidates = max(max_odd_candidates, cand["odd_candidate_count"])
        bad_candidate_count += int(cand["odd_candidate_count"] > 1)
        if cand["omega"]:
            odd_candidate_total += 1
            branch_counter[cand["branch"]] += 1
            reason_counter[cand["reason"]] += 1
            if cand["is_residual"]:
                predicted_edges.add((q, cand["omega"]))
                bad_phase_count += int(not (1 <= cand["d"] < P))
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
        else:
            reason_counter[cand["reason"]] += 1

    missing = actual_edges - predicted_edges
    extra = predicted_edges - actual_edges
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
        "max_odd_candidates_per_q": max_odd_candidates,
        "bad_candidate_count": bad_candidate_count,
        "bad_phase_displacement_count": bad_phase_count,
        "missing_edge_count": len(missing),
        "extra_edge_count": len(extra),
        "sample_predicted_edges": "; ".join(samples) if samples else "empty",
    }


def audit_rows(max_prime: int = 1009) -> dict[str, Any]:
    """对 P<=max_prime 的全部 1<=k<P 行做有限一致性审计。"""
    global PRIME_CACHE
    PRIME_CACHE = prime_sieve(2 * max_prime + 10)
    primes = PRIME_CACHE
    P_values = [p for p in primes if 11 <= p <= max_prime]
    row_count = 0
    active_rows = 0
    total_q = 0
    total_candidates = 0
    actual_edges = 0
    predicted_edges = 0
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
            max_odd_candidates = max(max_odd_candidates, row["max_odd_candidates_per_q"])
            for key in (
                "bad_candidate_count",
                "bad_phase_displacement_count",
                "missing_edge_count",
                "extra_edge_count",
            ):
                totals[key] += row[key]
            reason_totals.update(row["reason_counter"])
            branch_totals.update(row["branch_counter_on_candidates"])
            width_totals.update(row["window_width_counter"])
            if (P, k) in interesting:
                samples.append(row)

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
        "max_odd_candidates_per_q": max_odd_candidates,
        "unique_odd_candidate_per_q": max_odd_candidates <= 1 and totals["bad_candidate_count"] == 0,
        "predicted_edges_equal_actual_edges": totals["missing_edge_count"] == 0 and totals["extra_edge_count"] == 0,
        "all_predicted_displacements_in_1_to_Pminus1": totals["bad_phase_displacement_count"] == 0,
        "bad_candidate_total": totals["bad_candidate_count"],
        "bad_phase_displacement_total": totals["bad_phase_displacement_count"],
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
    parity = load_json(PARITY_JSON)
    three_claims = load_json(THREE_CLAIMS_JSON)
    finite_audit = audit_rows()
    return {
        "certificate_type": "prime_matrix_phi_lpf_unique_odd_candidate_projection_closure_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "unique_odd_candidate_projection_closed_phase_saving_open",
        "three_claim_triage": [
            {
                "claim": "Prime Matrix row/column Phi-LPF",
                "frontier_before": parity.get("latest_narrowest_mouth"),
                "fastest_subgate": "PrimeQUniqueOddCandidateProjection",
                "chosen": True,
                "reason": "two-point clipped q-windows have a unique odd candidate; LPF becomes a q-subset predicate",
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
                "reason": "verification package, not a closable q-candidate projection gate",
            },
        ],
        "three_claim_source_status": three_claims.get("plain_conclusion"),
        "unique_odd_candidate_theorem": {
            "candidate": "For each prime q in (P/2,P), the clipped window J_q contains at most one odd integer omega_{P,k}(q).",
            "edge_equivalence": "(q,m) is a residual edge iff omega exists, m=omega, omega is composite, and LPF(omega)>=7.",
            "phase": "On a residual q, the phase is e(-hD(q)/q), where D(q)=q*omega_{P,k}(q)-kP.",
            "normal_form": "The residual graph is a q-subset of a single-valued odd-candidate map, not a branch graph.",
            "not_enough": "The subset predicate LPF(omega)>=7 is still parity-sensitive and no cancellation over q follows.",
        },
        "finite_audit": finite_audit,
        "external_frontier_match_table": [
            {
                "source": "Euler parity plus clipped reciprocal window algebra",
                "useful_part": "closes the unique odd candidate projection",
                "accepted_for_this_gate": True,
                "closes_phase_saving": False,
                "reason_not_direct": "turns residual edges into a q-subset, but gives no cancellation on that subset",
            },
            {
                "source": "Milićević--Qin--Wu 2025 arXiv:2511.07550",
                "useful_part": "power-saving bilinear Kloosterman estimates for arbitrary moduli",
                "accepted_for_this_gate": False,
                "closes_phase_saving": False,
                "reason_not_direct": "the q-subset odd-candidate phase is not yet a completed bilinear Kloosterman sum",
            },
            {
                "source": "Pascadi 2025 arXiv:2511.08445",
                "useful_part": "Type-II Kloosterman sums with composite moduli via non-abelian amplification",
                "accepted_for_this_gate": False,
                "closes_phase_saving": False,
                "reason_not_direct": "does not estimate this fixed-row prime-q LPF-subset phase directly",
            },
            {
                "source": "Shao--Shparlinski--Wijaya 2024/2025 arXiv:2411.12113",
                "useful_part": "Kloosterman sums parametrised by square-free and smooth integers",
                "accepted_for_this_gate": False,
                "closes_phase_saving": False,
                "reason_not_direct": "still requires a completion identity from odd candidates to Kloosterman sums",
            },
            {
                "source": "Dong--Robles--Zeindler 2026 arXiv:2601.00292",
                "useful_part": "Kloosterman-fraction bilinear-form near miss",
                "accepted_for_this_gate": False,
                "closes_phase_saving": False,
                "reason_not_direct": "withdrawn on arXiv; cannot be cited as a valid external input",
            },
        ],
        "closed_gates": [
            gate(
                "PrimeQUniqueOddCandidateProjection",
                True,
                True,
                "Every prime q has at most one odd candidate omega in its clipped reciprocal window.",
                "none",
            ),
            gate(
                "LPFResidualAsQSubsetPredicate",
                True,
                True,
                "Residual edges are exactly q with omega composite and LPF(omega)>=7.",
                "none",
            ),
            gate(
                "PrimeQUniqueOddCandidateLPFSubsetPhaseSaving",
                False,
                False,
                "For |h|<=polylog(P), prove cancellation over q with LPF(omega(q))>=7 composite.",
                "unique odd candidate LPF-subset phase theorem",
            ),
            gate(
                "CompletionToExternalKloostermanOrVaughanTypeII",
                False,
                False,
                "Convert the odd-candidate q-subset phase to a DI/DFI/BC/FM-compatible estimate without losing pointwise P,k.",
                "completion/dispersion identity",
            ),
        ],
        "latest_narrowest_mouth": [
            "PrimeQUniqueOddCandidateLPFSubsetPhaseSaving",
            "AND CompletionToExternalKloostermanOrVaughanTypeII",
        ],
        "unique_odd_candidate_projection_closed": True,
        "unique_odd_candidate_phase_saving_closed": False,
        "phi_lpf_parity_barrier_globally_broken": False,
        "row_column_unconditional_closed": False,
        "external_lemma_version_unconditional_closed": False,
        "internal_self_contained_closed": False,
        "source_hashes": source_hashes(),
    }


def build_markdown(payload: dict[str, Any]) -> str:
    """生成 Markdown 证书。"""
    theorem = payload["unique_odd_candidate_theorem"]
    audit = payload["finite_audit"]
    lines = [
        "# Prime Matrix Phi-LPF unique odd candidate projection closure 审计",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['frontier_verified_date']}`",
        "",
        "## 1. 三命题选择",
        "",
        table(payload["three_claim_triage"], ["claim", "frontier", "frontier_before", "fastest_subgate", "chosen", "reason"]),
        "",
        "parity-selected branch 闭合后，本轮继续选择行/列 Phi-LPF 的 q 单值候选投影门。该门只用 clipped reciprocal window 与奇偶性闭合；它不证明后续相位和抵消。",
        "",
        "## 2. unique odd candidate 正规形",
        "",
        "```text",
        f"candidate={theorem['candidate']}",
        f"edge_equivalence={theorem['edge_equivalence']}",
        f"phase={theorem['phase']}",
        f"normal_form={theorem['normal_form']}",
        f"not_enough={theorem['not_enough']}",
        "```",
        "",
        "换言之，LPF residual graph 已被压成 q 上的单值函数 `omega(q)` 及其 LPF 子集谓词。后续难点不再是端点/分支/多重性，而是这个 LPF 选择的 q 子集是否有相位抵消。",
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
        f"branch_totals_on_candidates={audit['branch_totals_on_candidates']}",
        f"window_width_totals={audit['window_width_totals']}",
        f"max_odd_candidates_per_q={audit['max_odd_candidates_per_q']}",
        f"unique_odd_candidate_per_q={bool_text(audit['unique_odd_candidate_per_q'])}",
        f"predicted_edges_equal_actual_edges={bool_text(audit['predicted_edges_equal_actual_edges'])}",
        f"all_predicted_displacements_in_1_to_Pminus1={bool_text(audit['all_predicted_displacements_in_1_to_Pminus1'])}",
        f"bad_candidate_total={audit['bad_candidate_total']}",
        f"bad_phase_displacement_total={audit['bad_phase_displacement_total']}",
        f"missing_edge_total={audit['missing_edge_total']}",
        f"extra_edge_total={audit['extra_edge_total']}",
        "```",
        "",
        "有限审计只验证实现和账本一致性；全局闭合来自 clipped window 长度 `<2` 与 residual cofactor 的奇性。",
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
                "actual_edge_count_R30",
                "predicted_edge_count_R30",
                "reason_counter",
                "sample_predicted_edges",
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
        "外部 Kloosterman/Type-II 前沿仍是后续相位门候选；本层只把 parity-selected branch phase 精确改写为 q 单值 odd-candidate LPF-subset phase。",
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
        f"unique_odd_candidate_projection_closed={bool_text(payload['unique_odd_candidate_projection_closed'])}",
        f"unique_odd_candidate_phase_saving_closed={bool_text(payload['unique_odd_candidate_phase_saving_closed'])}",
        f"phi_lpf_parity_barrier_globally_broken={bool_text(payload['phi_lpf_parity_barrier_globally_broken'])}",
        f"row_column_unconditional_closed={bool_text(payload['row_column_unconditional_closed'])}",
        f"external_lemma_version_unconditional_closed={bool_text(payload['external_lemma_version_unconditional_closed'])}",
        f"internal_self_contained_closed={bool_text(payload['internal_self_contained_closed'])}",
        "```",
    ]
    return "\n".join(lines) + "\n"


# 全局素数表由 audit_rows 初始化，odd_candidate 使用它避免重复筛。
PRIME_CACHE: list[int] = []


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
    print("unique_odd_candidate_projection_closed=true")
    print("unique_odd_candidate_phase_saving_closed=false")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
