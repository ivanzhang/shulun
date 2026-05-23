#!/usr/bin/env python3
"""闭合 Phi-LPF matching graph 后的 matched displacement phase 正规形门。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_matched_displacement_phase_closure_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-matched-displacement-phase-closure-audit.json

上一层已证明 LPF residual 的 (q,m) 图是部分匹配。本层继续把每条匹配边
正规化为端点-位移相位：

  * d=q*m-kP 满足 1<=d<P；
  * 对任意整数 h，e(h*kP/q)=e(-h*d/q)，因为 h*kP/q=h*m-h*d/q；
  * m 是 q 窗口的 lower/upper floor 端点之一；
  * q 是 m 反向窗口的 lower/upper floor 端点之一。

结论：large numerator hkP 被精确替换为 matched displacement d<P。剩余硬点
变成 matched displacement phase saving，而不是一个未正规化的大分子倒数相位。
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

SLUG = "prime-matrix-phi-lpf-matched-displacement-phase-closure"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-23"

MATCHING_JSON = DOCS / "prime-matrix-phi-lpf-matching-graph-closure-audit.json"
BOOLEAN_Q_JSON = DOCS / "prime-matrix-phi-lpf-boolean-q-projection-closure-audit.json"
WEIGHT_EXTRACTION_JSON = DOCS / "prime-matrix-phi-lpf-weight-extraction-norm-closure-audit.json"
THREE_CLAIMS_JSON = DOCS / "three-claims-frontier-rankone-explicit-formula-router.json"

DEPENDENCIES = [
    MATCHING_JSON,
    BOOLEAN_Q_JSON,
    WEIGHT_EXTRACTION_JSON,
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
    """返回 q 对应的 cofactor 窗口 I_q(P,k)。"""
    low = max(q, (k * P) // q + 1)
    high = min(2 * P - 1, (((k + 1) * P) - 1) // q)
    return low, high


def m_window(P: int, k: int, m: int) -> tuple[int, int]:
    """返回固定 m 时可能的 q 整数窗口。"""
    low = max(P // 2 + 1, (k * P) // m + 1)
    high = min(P - 1, (((k + 1) * P) - 1) // m, m)
    return low, high


def residual_edges(P: int, k: int, primes: list[int]) -> list[tuple[int, int]]:
    """列出一行中的 (q,m) residual 边。"""
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


def endpoint_side(value: int, low: int, high: int) -> str:
    """返回 value 在窗口端点中的位置。"""
    if low == high == value:
        return "both"
    if value == low:
        return "lower"
    if value == high:
        return "upper"
    return "interior_or_missing"


def row_phase_payload(P: int, k: int, primes: list[int]) -> dict[str, Any]:
    """计算一行 matched displacement phase 正规形诊断。"""
    edges = residual_edges(P, k, primes)
    q_endpoint_counter: Counter[str] = Counter()
    m_endpoint_counter: Counter[str] = Counter()
    d_values: list[int] = []
    bad_edges: list[tuple[int, int, int, str, str]] = []
    bad_displacement_count = 0
    bad_phase_count = 0
    bad_endpoint_count = 0

    for q, m in edges:
        d = q * m - k * P
        q_low, q_high = q_window(P, k, q)
        m_low, m_high = m_window(P, k, m)
        q_side = endpoint_side(m, q_low, q_high)
        m_side = endpoint_side(q, m_low, m_high)
        q_endpoint_counter[q_side] += 1
        m_endpoint_counter[m_side] += 1
        d_values.append(d)

        # 中文注释：相位恒等式等价于 q | (kP+d)，这里对几个 h 做同余防守。
        phase_ok = all((h * k * P + h * d) % q == 0 for h in (1, 2, 7, 31))
        displacement_ok = 1 <= d < P
        endpoint_ok = q_side != "interior_or_missing" and m_side != "interior_or_missing"
        bad_displacement_count += int(not displacement_ok)
        bad_phase_count += int(not phase_ok)
        bad_endpoint_count += int(not endpoint_ok)
        ok = displacement_ok and phase_ok and endpoint_ok
        if not ok:
            bad_edges.append((q, m, d, q_side, m_side))

    sample_edges = "; ".join(
        f"q={q},m={m},d={q*m-k*P}" for q, m in edges[:5]
    ) if edges else "empty"
    return {
        "P": P,
        "k": k,
        "edge_count_R30": len(edges),
        "min_displacement": min(d_values) if d_values else 0,
        "max_displacement": max(d_values) if d_values else 0,
        "all_displacements_in_1_to_Pminus1": bad_displacement_count == 0,
        "all_phase_congruences_verified": bad_phase_count == 0,
        "all_endpoint_selectors_verified": bad_endpoint_count == 0,
        "q_endpoint_lower": q_endpoint_counter["lower"],
        "q_endpoint_upper": q_endpoint_counter["upper"],
        "q_endpoint_both": q_endpoint_counter["both"],
        "m_endpoint_lower": m_endpoint_counter["lower"],
        "m_endpoint_upper": m_endpoint_counter["upper"],
        "m_endpoint_both": m_endpoint_counter["both"],
        "bad_displacement_count": bad_displacement_count,
        "bad_phase_count": bad_phase_count,
        "bad_endpoint_count": bad_endpoint_count,
        "bad_edge_count": len(bad_edges),
        "sample_edges": sample_edges,
    }


def audit_rows(max_prime: int = 1009) -> dict[str, Any]:
    """对 P<=max_prime 的全部 1<=k<P 行做有限一致性审计。"""
    primes = prime_sieve(2 * max_prime + 10)
    P_values = [p for p in primes if 11 <= p <= max_prime]
    row_count = 0
    active_rows = 0
    total_edges = 0
    global_min_d = 0
    global_max_d = 0
    bad_edge_total = 0
    bad_displacement_total = 0
    bad_phase_total = 0
    bad_endpoint_total = 0
    q_endpoint_totals: Counter[str] = Counter()
    m_endpoint_totals: Counter[str] = Counter()
    samples: list[dict[str, Any]] = []
    interesting = {(101, 100), (257, 256), (971, 936), (1009, 1008)}

    for P in P_values:
        for k in range(1, P):
            row_count += 1
            row = row_phase_payload(P, k, primes)
            active_rows += int(row["edge_count_R30"] > 0)
            total_edges += row["edge_count_R30"]
            bad_edge_total += row["bad_edge_count"]
            bad_displacement_total += row["bad_displacement_count"]
            bad_phase_total += row["bad_phase_count"]
            bad_endpoint_total += row["bad_endpoint_count"]
            if row["edge_count_R30"]:
                if global_min_d == 0:
                    global_min_d = row["min_displacement"]
                else:
                    global_min_d = min(global_min_d, row["min_displacement"])
                global_max_d = max(global_max_d, row["max_displacement"])
            for key in ("lower", "upper", "both"):
                q_endpoint_totals[key] += row[f"q_endpoint_{key}"]
                m_endpoint_totals[key] += row[f"m_endpoint_{key}"]
            if (P, k) in interesting:
                samples.append(row)

    return {
        "max_prime": max_prime,
        "k_range": "1<=k<P in this implementation audit",
        "row_count": row_count,
        "active_residual_row_count": active_rows,
        "total_edges_R30": total_edges,
        "global_min_displacement": global_min_d,
        "global_max_displacement": global_max_d,
        "all_displacements_in_1_to_Pminus1": bad_displacement_total == 0,
        "all_phase_congruences_verified": bad_phase_total == 0,
        "all_endpoint_selectors_verified": bad_endpoint_total == 0,
        "q_endpoint_totals": dict(q_endpoint_totals),
        "m_endpoint_totals": dict(m_endpoint_totals),
        "bad_displacement_total": bad_displacement_total,
        "bad_phase_total": bad_phase_total,
        "bad_endpoint_total": bad_endpoint_total,
        "bad_edge_total": bad_edge_total,
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
    matching = load_json(MATCHING_JSON)
    three_claims = load_json(THREE_CLAIMS_JSON)
    finite_audit = audit_rows()
    return {
        "certificate_type": "prime_matrix_phi_lpf_matched_displacement_phase_closure_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "matched_displacement_phase_normal_form_closed_phase_saving_open",
        "three_claim_triage": [
            {
                "claim": "Prime Matrix row/column Phi-LPF",
                "frontier_before": matching.get("latest_narrowest_mouth"),
                "fastest_subgate": "MatchedDisplacementPhaseNormalForm",
                "chosen": True,
                "reason": "exact integer displacement identity after matching graph closure; no new prime theorem required",
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
                "reason": "verification package, not a closable phase-normal-form gate",
            },
        ],
        "three_claim_source_status": three_claims.get("plain_conclusion"),
        "phase_normal_form_theorem": {
            "displacement": "For every matched edge (q,m), define d=q*m-kP; then 1<=d<P.",
            "phase_identity": "For every integer h, e(h*kP/q)=e(-h*d/q), since h*kP/q=h*m-h*d/q.",
            "q_endpoint_selector": "m is one of the two clipped endpoints max(q,floor(kP/q)+1) or min(2P-1,floor(((k+1)P-1)/q)).",
            "m_endpoint_selector": "q is one of the two clipped reverse endpoints max(P/2+1,floor(kP/m)+1) or min(P-1,m,floor(((k+1)P-1)/m)).",
            "normal_form": "The finite phase is a matched displacement sum over edges (q,m,d), not an unnormalised large-numerator reciprocal phase.",
            "not_enough": "The displacement d is still a moving, LPF-selected residue; cancellation for the matched displacement sum remains open.",
        },
        "finite_audit": finite_audit,
        "external_frontier_match_table": [
            {
                "source": "Elementary integer phase reduction",
                "useful_part": "closes e(hkP/q)=e(-hd/q) on every matched edge",
                "accepted_for_this_gate": True,
                "closes_phase_saving": False,
                "reason_not_direct": "normalises the phase only; gives no cancellation over moving displacements",
            },
            {
                "source": "Milićević--Qin--Wu 2025 arXiv:2511.07550",
                "useful_part": "arbitrary-modulus bilinear Kloosterman power savings after completion",
                "accepted_for_this_gate": False,
                "closes_phase_saving": False,
                "reason_not_direct": "matched displacement phase is not yet a completed Kloosterman bilinear form",
            },
            {
                "source": "Pascadi 2025 arXiv:2511.08445",
                "useful_part": "non-abelian amplification for composite-modulus Kloosterman sums",
                "accepted_for_this_gate": False,
                "closes_phase_saving": False,
                "reason_not_direct": "does not estimate this fixed-row matched real phase directly",
            },
            {
                "source": "Shao--Shparlinski--Wijaya 2024/2025 arXiv:2411.12113",
                "useful_part": "Kloosterman sums over square-free and smooth parameters",
                "accepted_for_this_gate": False,
                "closes_phase_saving": False,
                "reason_not_direct": "requires finite-field Kloosterman completion first",
            },
        ],
        "closed_gates": [
            gate(
                "MatchedDisplacementPhaseNormalForm",
                True,
                True,
                "Every matched edge has d=qm-kP in [1,P-1] and e(hkP/q)=e(-hd/q).",
                "none",
            ),
            gate(
                "TwoSidedEndpointSelectorNormalForm",
                True,
                True,
                "Each matched edge lies on a q-side endpoint and an m-side reverse endpoint.",
                "none",
            ),
            gate(
                "PrimeQMatchedDisplacementPhaseSaving",
                False,
                False,
                "For |h|<=polylog(P), prove cancellation for sum over matched edges e(-h*d(q)/q).",
                "matched displacement phase theorem",
            ),
            gate(
                "CompletionToExternalKloostermanOrVaughanTypeII",
                False,
                False,
                "Convert the matched displacement graph to a DI/DFI/BC/FM-compatible estimate without losing pointwise P,k.",
                "completion/dispersion identity",
            ),
        ],
        "latest_narrowest_mouth": [
            "PrimeQMatchedDisplacementPhaseSaving",
            "AND CompletionToExternalKloostermanOrVaughanTypeII",
        ],
        "matched_displacement_phase_normal_form_closed": True,
        "weighted_reciprocal_phase_saving_closed": False,
        "phi_lpf_parity_barrier_globally_broken": False,
        "row_column_unconditional_closed": False,
        "external_lemma_version_unconditional_closed": False,
        "internal_self_contained_closed": False,
        "source_hashes": source_hashes(),
    }


def build_markdown(payload: dict[str, Any]) -> str:
    """生成 Markdown 证书。"""
    theorem = payload["phase_normal_form_theorem"]
    audit = payload["finite_audit"]
    lines = [
        "# Prime Matrix Phi-LPF matched displacement phase closure 审计",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['frontier_verified_date']}`",
        "",
        "## 1. 三命题选择",
        "",
        table(payload["three_claim_triage"], ["claim", "frontier", "frontier_before", "fastest_subgate", "chosen", "reason"]),
        "",
        "matching graph 闭合后，本轮继续选择行/列 Phi-LPF 的 phase normal-form 子门。该门只用整数恒等式与端点窗口，可完全闭合；它不证明后续相位和抵消。",
        "",
        "## 2. matched displacement phase 正规形",
        "",
        "```text",
        f"displacement={theorem['displacement']}",
        f"phase_identity={theorem['phase_identity']}",
        f"q_endpoint_selector={theorem['q_endpoint_selector']}",
        f"m_endpoint_selector={theorem['m_endpoint_selector']}",
        f"normal_form={theorem['normal_form']}",
        f"not_enough={theorem['not_enough']}",
        "```",
        "",
        "关键点是：每条匹配边满足 `kP<qm<(k+1)P`，所以 `d=qm-kP` 自动落在 `[1,P-1]`。又因为 `kP=qm-d`，对任意整数 `h` 有 `h*kP/q=h*m-h*d/q`，指数相位中的整数项消失，得到 `e(hkP/q)=e(-hd/q)`。",
        "",
        "## 3. 全量有限审计",
        "",
        "```text",
        f"max_prime={audit['max_prime']}",
        f"k_range={audit['k_range']}",
        f"row_count={audit['row_count']}",
        f"active_residual_row_count={audit['active_residual_row_count']}",
        f"total_edges_R30={audit['total_edges_R30']}",
        f"global_min_displacement={audit['global_min_displacement']}",
        f"global_max_displacement={audit['global_max_displacement']}",
        f"all_displacements_in_1_to_Pminus1={bool_text(audit['all_displacements_in_1_to_Pminus1'])}",
        f"all_phase_congruences_verified={bool_text(audit['all_phase_congruences_verified'])}",
        f"all_endpoint_selectors_verified={bool_text(audit['all_endpoint_selectors_verified'])}",
        f"q_endpoint_totals={audit['q_endpoint_totals']}",
        f"m_endpoint_totals={audit['m_endpoint_totals']}",
        f"bad_displacement_total={audit['bad_displacement_total']}",
        f"bad_phase_total={audit['bad_phase_total']}",
        f"bad_endpoint_total={audit['bad_endpoint_total']}",
        f"bad_edge_total={audit['bad_edge_total']}",
        "```",
        "",
        "有限审计只验证实现和账本一致性；全局闭合来自上面的整数位移恒等式。",
        "",
        "代表行：",
        "",
        table(
            audit["sample_rows"],
            [
                "P",
                "k",
                "edge_count_R30",
                "min_displacement",
                "max_displacement",
                "q_endpoint_lower",
                "q_endpoint_upper",
                "q_endpoint_both",
                "m_endpoint_lower",
                "m_endpoint_upper",
                "m_endpoint_both",
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
        "外部 Kloosterman/Type-II 前沿仍是后续相位门候选；本层只把大分子 reciprocal phase 精确改写为 matched displacement phase。",
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
        f"matched_displacement_phase_normal_form_closed={bool_text(payload['matched_displacement_phase_normal_form_closed'])}",
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
    print("matched_displacement_phase_normal_form_closed=true")
    print("weighted_reciprocal_phase_saving_closed=false")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
