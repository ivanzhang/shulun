#!/usr/bin/env python3
"""闭合 Phi-LPF floor-residue phase 后的 parity-selected branch 正规形门。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_parity_selected_branch_phase_closure_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-parity-selected-branch-phase-closure-audit.json

上一层已证明 residual edge 只能来自 q 侧 lower/upper floor endpoint：

  L=floor(kP/q)+1, U=floor(((k+1)P-1)/q), U-L in {0,1}.

本层继续关闭端点选择门：

  * 若 U=L，则 residual edge 是 singleton/both branch；
  * 若 U=L+1，则两个端点连续，而 residual cofactor 满足 LPF(m)>=7，必为奇数；
    因而 lower/upper 分支由 L 的奇偶性唯一决定；
  * lower phase 使用 d=q-(kP mod q)，upper phase 使用
    d=P-1-(((k+1)P-1) mod q)。

这仍不是相位抵消定理；它只说明 LPF 条件不再引入额外的端点侧选择自由度。
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

SLUG = "prime-matrix-phi-lpf-parity-selected-branch-phase-closure"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-23"

FLOOR_JSON = DOCS / "prime-matrix-phi-lpf-floor-residue-branch-phase-closure-audit.json"
MATCHED_JSON = DOCS / "prime-matrix-phi-lpf-matched-displacement-phase-closure-audit.json"
THREE_CLAIMS_JSON = DOCS / "three-claims-frontier-rankone-explicit-formula-router.json"

DEPENDENCIES = [
    FLOOR_JSON,
    MATCHED_JSON,
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
    """返回 q 对应的 cofactor 窗口。"""
    low = max(q, (k * P) // q + 1)
    high = min(2 * P - 1, (((k + 1) * P) - 1) // q)
    return low, high


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


def branch_payload(P: int, k: int, q: int, m: int) -> dict[str, Any]:
    """计算一条边的 parity-selected branch 诊断。"""
    L = (k * P) // q + 1
    U = (((k + 1) * P) - 1) // q
    width = U - L
    d = q * m - k * P
    rho = (k * P) % q
    sigma = (((k + 1) * P) - 1) % q

    if m == L == U:
        actual_branch = "both"
    elif m == L:
        actual_branch = "lower"
    elif m == U:
        actual_branch = "upper"
    else:
        actual_branch = "interior"

    if width == 0:
        predicted_branch = "both"
    elif width == 1 and L % 2 == 1:
        predicted_branch = "lower"
    elif width == 1 and U % 2 == 1:
        predicted_branch = "upper"
    else:
        predicted_branch = "invalid"

    lower_formula = q - rho
    upper_formula = P - 1 - sigma
    if actual_branch == "lower":
        phase_numerator = lower_formula
    elif actual_branch == "upper":
        phase_numerator = upper_formula
    else:
        phase_numerator = lower_formula

    singleton_formula_consistent = actual_branch != "both" or lower_formula == upper_formula == d
    two_point_parity_ok = width != 1 or (L % 2) != (U % 2)
    residual_odd = m % 2 == 1
    predicted_ok = actual_branch == predicted_branch
    phase_formula_ok = phase_numerator == d

    # 中文注释：width>1 或 interior 说明前一层 floor branch 正规形被破坏。
    return {
        "L": L,
        "U": U,
        "width": width,
        "d": d,
        "rho": rho,
        "sigma": sigma,
        "actual_branch": actual_branch,
        "predicted_branch": predicted_branch,
        "residual_odd": residual_odd,
        "two_point_parity_ok": two_point_parity_ok,
        "singleton_formula_consistent": singleton_formula_consistent,
        "phase_formula_ok": phase_formula_ok,
        "predicted_ok": predicted_ok,
        "phase_numerator": phase_numerator,
    }


def row_payload(P: int, k: int, primes: list[int]) -> dict[str, Any]:
    """计算一行 parity-selected branch 诊断。"""
    edges = residual_edges(P, k, primes)
    width_counter: Counter[str] = Counter()
    branch_counter: Counter[str] = Counter()
    predicted_counter: Counter[str] = Counter()
    bad_width = 0
    bad_parity = 0
    bad_prediction = 0
    bad_phase_formula = 0
    bad_singleton_formula = 0
    sample_items = []

    for q, m in edges:
        diag = branch_payload(P, k, q, m)
        width_counter[str(diag["width"])] += 1
        branch_counter[diag["actual_branch"]] += 1
        predicted_counter[diag["predicted_branch"]] += 1
        bad_width += int(diag["width"] not in {0, 1} or diag["actual_branch"] == "interior")
        bad_parity += int(not diag["residual_odd"] or not diag["two_point_parity_ok"])
        bad_prediction += int(not diag["predicted_ok"])
        bad_phase_formula += int(not diag["phase_formula_ok"])
        bad_singleton_formula += int(not diag["singleton_formula_consistent"])
        if len(sample_items) < 5:
            sample_items.append(
                "q={q},m={m},L={L},U={U},branch={b},pred={p},d={d}".format(
                    q=q,
                    m=m,
                    L=diag["L"],
                    U=diag["U"],
                    b=diag["actual_branch"],
                    p=diag["predicted_branch"],
                    d=diag["d"],
                )
            )

    return {
        "P": P,
        "k": k,
        "edge_count_R30": len(edges),
        "width_0_singleton_edges": width_counter["0"],
        "width_1_two_point_edges": width_counter["1"],
        "branch_lower": branch_counter["lower"],
        "branch_upper": branch_counter["upper"],
        "branch_both": branch_counter["both"],
        "predicted_lower": predicted_counter["lower"],
        "predicted_upper": predicted_counter["upper"],
        "predicted_both": predicted_counter["both"],
        "bad_width_count": bad_width,
        "bad_parity_count": bad_parity,
        "bad_prediction_count": bad_prediction,
        "bad_phase_formula_count": bad_phase_formula,
        "bad_singleton_formula_count": bad_singleton_formula,
        "sample_edges": "; ".join(sample_items) if sample_items else "empty",
    }


def audit_rows(max_prime: int = 1009) -> dict[str, Any]:
    """对 P<=max_prime 的全部 1<=k<P 行做有限一致性审计。"""
    primes = prime_sieve(2 * max_prime + 10)
    P_values = [p for p in primes if 11 <= p <= max_prime]
    row_count = 0
    active_rows = 0
    total_edges = 0
    totals: Counter[str] = Counter()
    samples: list[dict[str, Any]] = []
    interesting = {(101, 100), (257, 256), (971, 936), (1009, 1008)}

    for P in P_values:
        for k in range(1, P):
            row_count += 1
            row = row_payload(P, k, primes)
            active_rows += int(row["edge_count_R30"] > 0)
            total_edges += row["edge_count_R30"]
            for key in (
                "width_0_singleton_edges",
                "width_1_two_point_edges",
                "branch_lower",
                "branch_upper",
                "branch_both",
                "predicted_lower",
                "predicted_upper",
                "predicted_both",
                "bad_width_count",
                "bad_parity_count",
                "bad_prediction_count",
                "bad_phase_formula_count",
                "bad_singleton_formula_count",
            ):
                totals[key] += row[key]
            if (P, k) in interesting:
                samples.append(row)

    return {
        "max_prime": max_prime,
        "k_range": "1<=k<P in this implementation audit",
        "row_count": row_count,
        "active_residual_row_count": active_rows,
        "total_edges_R30": total_edges,
        "width_totals": {
            "singleton_width_0": totals["width_0_singleton_edges"],
            "two_point_width_1": totals["width_1_two_point_edges"],
        },
        "actual_branch_totals": {
            "lower": totals["branch_lower"],
            "upper": totals["branch_upper"],
            "both": totals["branch_both"],
        },
        "predicted_branch_totals": {
            "lower": totals["predicted_lower"],
            "upper": totals["predicted_upper"],
            "both": totals["predicted_both"],
        },
        "all_edges_width_zero_or_one": totals["bad_width_count"] == 0,
        "all_two_point_branches_parity_selected": totals["bad_prediction_count"] == 0,
        "all_residual_cofactors_odd": totals["bad_parity_count"] == 0,
        "all_branch_phase_formulas_verified": totals["bad_phase_formula_count"] == 0,
        "all_singleton_branch_formulas_consistent": totals["bad_singleton_formula_count"] == 0,
        "bad_width_total": totals["bad_width_count"],
        "bad_parity_total": totals["bad_parity_count"],
        "bad_prediction_total": totals["bad_prediction_count"],
        "bad_phase_formula_total": totals["bad_phase_formula_count"],
        "bad_singleton_formula_total": totals["bad_singleton_formula_count"],
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
    floor = load_json(FLOOR_JSON)
    three_claims = load_json(THREE_CLAIMS_JSON)
    finite_audit = audit_rows()
    return {
        "certificate_type": "prime_matrix_phi_lpf_parity_selected_branch_phase_closure_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "parity_selected_branch_normal_form_closed_phase_saving_open",
        "three_claim_triage": [
            {
                "claim": "Prime Matrix row/column Phi-LPF",
                "frontier_before": floor.get("latest_narrowest_mouth"),
                "fastest_subgate": "PrimeQParitySelectedFloorResidueBranchNormalForm",
                "chosen": True,
                "reason": "two-point floor windows plus LPF>=7 oddness determine the branch; no new prime theorem required",
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
                "reason": "verification package, not a closable parity-selected branch gate",
            },
        ],
        "three_claim_source_status": three_claims.get("plain_conclusion"),
        "parity_selected_branch_theorem": {
            "floor_window": "After cap removal, L=floor(kP/q)+1 and U=floor(((k+1)P-1)/q), with U-L in {0,1} on every edge.",
            "singleton": "If U=L, the edge is simultaneously lower and upper and both residue formulae give the same d.",
            "two_point_selector": "If U=L+1, the residual cofactor is odd, so the edge is lower exactly when L is odd and upper exactly when U is odd.",
            "phase_formula": "The selected branch phase uses d=q-(kP mod q) on lower and d=P-1-(((k+1)P-1) mod q) on upper.",
            "not_enough": "Parity selects the endpoint side but gives no cancellation over the remaining LPF-selected prime q set.",
        },
        "finite_audit": finite_audit,
        "external_frontier_match_table": [
            {
                "source": "Euler 2-wheel parity plus floor-window algebra",
                "useful_part": "closes endpoint-side selection in every two-point q-window",
                "accepted_for_this_gate": True,
                "closes_phase_saving": False,
                "reason_not_direct": "endpoint selection is deterministic, but cancellation over selected q remains open",
            },
            {
                "source": "Milićević--Qin--Wu 2025 arXiv:2511.07550",
                "useful_part": "power-saving bilinear Kloosterman estimates for arbitrary moduli",
                "accepted_for_this_gate": False,
                "closes_phase_saving": False,
                "reason_not_direct": "the parity-selected branch is not yet a completed bilinear Kloosterman sum",
            },
            {
                "source": "Pascadi 2025 arXiv:2511.08445",
                "useful_part": "Type-II Kloosterman sums with composite moduli via non-abelian amplification",
                "accepted_for_this_gate": False,
                "closes_phase_saving": False,
                "reason_not_direct": "does not estimate this fixed-row prime-q branch phase directly",
            },
            {
                "source": "Shao--Shparlinski--Wijaya 2024/2025 arXiv:2411.12113",
                "useful_part": "Kloosterman sums parametrised by square-free and smooth integers",
                "accepted_for_this_gate": False,
                "closes_phase_saving": False,
                "reason_not_direct": "still requires a completion identity from floor residues to Kloosterman sums",
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
                "TwoPointFloorWindowParitySelector",
                True,
                True,
                "When U=L+1, the residual endpoint is the unique odd endpoint.",
                "none",
            ),
            gate(
                "SingletonBothBranchConsistency",
                True,
                True,
                "When U=L, lower and upper residue formulae agree on the same displacement d.",
                "none",
            ),
            gate(
                "PrimeQParitySelectedFloorResidueBranchPhaseSaving",
                False,
                False,
                "For |h|<=polylog(P), prove cancellation after replacing branch choice by the parity selector.",
                "parity-selected branch phase theorem",
            ),
            gate(
                "CompletionToExternalKloostermanOrVaughanTypeII",
                False,
                False,
                "Convert the parity-selected branch graph to a DI/DFI/BC/FM-compatible estimate without losing pointwise P,k.",
                "completion/dispersion identity",
            ),
        ],
        "latest_narrowest_mouth": [
            "PrimeQParitySelectedFloorResidueBranchPhaseSaving",
            "AND CompletionToExternalKloostermanOrVaughanTypeII",
        ],
        "parity_selected_branch_normal_form_closed": True,
        "parity_selected_branch_phase_saving_closed": False,
        "phi_lpf_parity_barrier_globally_broken": False,
        "row_column_unconditional_closed": False,
        "external_lemma_version_unconditional_closed": False,
        "internal_self_contained_closed": False,
        "source_hashes": source_hashes(),
    }


def build_markdown(payload: dict[str, Any]) -> str:
    """生成 Markdown 证书。"""
    theorem = payload["parity_selected_branch_theorem"]
    audit = payload["finite_audit"]
    lines = [
        "# Prime Matrix Phi-LPF parity selected branch phase closure 审计",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['frontier_verified_date']}`",
        "",
        "## 1. 三命题选择",
        "",
        table(payload["three_claim_triage"], ["claim", "frontier", "frontier_before", "fastest_subgate", "chosen", "reason"]),
        "",
        "floor-residue branch 闭合后，本轮继续选择行/列 Phi-LPF 的 parity-selected branch 子门。该门只用二点窗口和 `LPF(m)>=7` 的奇性闭合；它不证明后续相位和抵消。",
        "",
        "## 2. parity-selected branch 正规形",
        "",
        "```text",
        f"floor_window={theorem['floor_window']}",
        f"singleton={theorem['singleton']}",
        f"two_point_selector={theorem['two_point_selector']}",
        f"phase_formula={theorem['phase_formula']}",
        f"not_enough={theorem['not_enough']}",
        "```",
        "",
        "写 `L=floor(kP/q)+1`、`U=floor(((k+1)P-1)/q)`。若 `U=L+1`，则两个候选端点连续；residual cofactor 必为奇数，因此分支由 `L` 的奇偶性决定。若 `U=L`，该边同时是 lower 与 upper。",
        "",
        "## 3. 全量有限审计",
        "",
        "```text",
        f"max_prime={audit['max_prime']}",
        f"k_range={audit['k_range']}",
        f"row_count={audit['row_count']}",
        f"active_residual_row_count={audit['active_residual_row_count']}",
        f"total_edges_R30={audit['total_edges_R30']}",
        f"width_totals={audit['width_totals']}",
        f"actual_branch_totals={audit['actual_branch_totals']}",
        f"predicted_branch_totals={audit['predicted_branch_totals']}",
        f"all_edges_width_zero_or_one={bool_text(audit['all_edges_width_zero_or_one'])}",
        f"all_two_point_branches_parity_selected={bool_text(audit['all_two_point_branches_parity_selected'])}",
        f"all_residual_cofactors_odd={bool_text(audit['all_residual_cofactors_odd'])}",
        f"all_branch_phase_formulas_verified={bool_text(audit['all_branch_phase_formulas_verified'])}",
        f"all_singleton_branch_formulas_consistent={bool_text(audit['all_singleton_branch_formulas_consistent'])}",
        f"bad_width_total={audit['bad_width_total']}",
        f"bad_parity_total={audit['bad_parity_total']}",
        f"bad_prediction_total={audit['bad_prediction_total']}",
        f"bad_phase_formula_total={audit['bad_phase_formula_total']}",
        f"bad_singleton_formula_total={audit['bad_singleton_formula_total']}",
        "```",
        "",
        "有限审计只验证实现和账本一致性；全局闭合来自二点窗口与奇偶端点选择。",
        "",
        "代表行：",
        "",
        table(
            audit["sample_rows"],
            [
                "P",
                "k",
                "edge_count_R30",
                "width_0_singleton_edges",
                "width_1_two_point_edges",
                "branch_lower",
                "branch_upper",
                "branch_both",
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
        "外部 Kloosterman/Type-II 前沿仍是后续相位门候选；本层只把 floor-residue branch 精确拆成由 parity selector 决定的 branch phase。",
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
        f"parity_selected_branch_normal_form_closed={bool_text(payload['parity_selected_branch_normal_form_closed'])}",
        f"parity_selected_branch_phase_saving_closed={bool_text(payload['parity_selected_branch_phase_saving_closed'])}",
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
    print("parity_selected_branch_normal_form_closed=true")
    print("parity_selected_branch_phase_saving_closed=false")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
