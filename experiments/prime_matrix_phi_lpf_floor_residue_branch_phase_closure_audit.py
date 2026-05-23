#!/usr/bin/env python3
"""闭合 Phi-LPF matched displacement 后的 floor-residue branch 正规形门。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_floor_residue_branch_phase_closure_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-floor-residue-branch-phase-closure-audit.json

上一层已把 residual graph 压成 matched displacement phase：

  e(h*kP/q)=e(-h*d/q),  d=q*m-kP,  1<=d<P.

本层继续证明 q 侧没有边界 cap 噪声。对每条 residual edge，q-window 的端点
都来自 floor 函数，而不是来自 m>=q 或 m<=2P-1 的剪裁边界。因此 d 必落在
两个显式余数分支之一：

  lower branch: d=q-(kP mod q);
  upper branch: d=P-1-(((k+1)P-1) mod q).

这仍不是相位抵消定理；它只把后续相位节省问题压成 floor-residue branch sum。
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

SLUG = "prime-matrix-phi-lpf-floor-residue-branch-phase-closure"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-23"

MATCHED_JSON = DOCS / "prime-matrix-phi-lpf-matched-displacement-phase-closure-audit.json"
MATCHING_JSON = DOCS / "prime-matrix-phi-lpf-matching-graph-closure-audit.json"
BOOLEAN_Q_JSON = DOCS / "prime-matrix-phi-lpf-boolean-q-projection-closure-audit.json"
THREE_CLAIMS_JSON = DOCS / "three-claims-frontier-rankone-explicit-formula-router.json"

DEPENDENCIES = [
    MATCHED_JSON,
    MATCHING_JSON,
    BOOLEAN_Q_JSON,
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


def q_branch(P: int, k: int, q: int, m: int) -> dict[str, Any]:
    """返回 q-window 的 floor/cap 分支诊断。"""
    lower_floor = (k * P) // q + 1
    upper_floor = (((k + 1) * P) - 1) // q
    low = max(q, lower_floor)
    high = min(2 * P - 1, upper_floor)
    d = q * m - k * P
    k_residue = (k * P) % q
    upper_residue = (((k + 1) * P) - 1) % q

    on_lower = m == low
    on_upper = m == high
    lower_floor_active = on_lower and low == lower_floor and lower_floor > q
    upper_floor_active = on_upper and high == upper_floor and upper_floor < 2 * P - 1
    lower_cap_active = on_lower and low == q
    upper_cap_active = on_upper and high == 2 * P - 1

    lower_formula = q - k_residue
    upper_formula = P - 1 - upper_residue
    lower_formula_ok = (not on_lower) or (d == lower_formula and 1 <= d <= q)
    upper_formula_ok = (not on_upper) or (d == upper_formula and P - q <= d <= P - 1)
    branch = "both" if on_lower and on_upper else "lower" if on_lower else "upper" if on_upper else "interior"

    # 中文注释：residual edge 应只有 floor branch，不能靠 q 或 2P-1 cap 支撑。
    cap_free = not lower_cap_active and not upper_cap_active
    floor_covered = (on_lower and lower_floor_active) or (on_upper and upper_floor_active)
    formula_ok = lower_formula_ok and upper_formula_ok
    return {
        "branch": branch,
        "d": d,
        "k_residue": k_residue,
        "upper_residue": upper_residue,
        "lower_formula": lower_formula,
        "upper_formula": upper_formula,
        "lower_floor_active": lower_floor_active,
        "upper_floor_active": upper_floor_active,
        "lower_cap_active": lower_cap_active,
        "upper_cap_active": upper_cap_active,
        "cap_free": cap_free,
        "floor_covered": floor_covered,
        "formula_ok": formula_ok,
    }


def row_payload(P: int, k: int, primes: list[int]) -> dict[str, Any]:
    """计算一行 floor-residue branch 诊断。"""
    edges = residual_edges(P, k, primes)
    branch_counter: Counter[str] = Counter()
    bad_cap = 0
    bad_floor = 0
    bad_formula = 0
    low_d_values: list[int] = []
    high_d_values: list[int] = []
    samples = []

    for q, m in edges:
        diag = q_branch(P, k, q, m)
        branch_counter[diag["branch"]] += 1
        bad_cap += int(not diag["cap_free"])
        bad_floor += int(not diag["floor_covered"])
        bad_formula += int(not diag["formula_ok"])
        if diag["branch"] in {"lower", "both"}:
            low_d_values.append(diag["d"])
        if diag["branch"] in {"upper", "both"}:
            high_d_values.append(diag["d"])
        if len(samples) < 5:
            samples.append(
                "q={q},m={m},d={d},branch={branch},rho={rho},sigma={sigma}".format(
                    q=q,
                    m=m,
                    d=diag["d"],
                    branch=diag["branch"],
                    rho=diag["k_residue"],
                    sigma=diag["upper_residue"],
                )
            )

    return {
        "P": P,
        "k": k,
        "edge_count_R30": len(edges),
        "branch_lower": branch_counter["lower"],
        "branch_upper": branch_counter["upper"],
        "branch_both": branch_counter["both"],
        "branch_interior": branch_counter["interior"],
        "min_lower_or_both_displacement": min(low_d_values) if low_d_values else 0,
        "max_lower_or_both_displacement": max(low_d_values) if low_d_values else 0,
        "min_upper_or_both_displacement": min(high_d_values) if high_d_values else 0,
        "max_upper_or_both_displacement": max(high_d_values) if high_d_values else 0,
        "bad_cap_count": bad_cap,
        "bad_floor_coverage_count": bad_floor,
        "bad_residue_formula_count": bad_formula,
        "sample_edges": "; ".join(samples) if samples else "empty",
    }


def audit_rows(max_prime: int = 1009) -> dict[str, Any]:
    """对 P<=max_prime 的全部 1<=k<P 行做有限一致性审计。"""
    primes = prime_sieve(2 * max_prime + 10)
    P_values = [p for p in primes if 11 <= p <= max_prime]
    row_count = 0
    active_rows = 0
    total_edges = 0
    branch_totals: Counter[str] = Counter()
    bad_cap_total = 0
    bad_floor_total = 0
    bad_formula_total = 0
    samples: list[dict[str, Any]] = []
    interesting = {(101, 100), (257, 256), (971, 936), (1009, 1008)}

    for P in P_values:
        for k in range(1, P):
            row_count += 1
            row = row_payload(P, k, primes)
            active_rows += int(row["edge_count_R30"] > 0)
            total_edges += row["edge_count_R30"]
            branch_totals["lower"] += row["branch_lower"]
            branch_totals["upper"] += row["branch_upper"]
            branch_totals["both"] += row["branch_both"]
            branch_totals["interior"] += row["branch_interior"]
            bad_cap_total += row["bad_cap_count"]
            bad_floor_total += row["bad_floor_coverage_count"]
            bad_formula_total += row["bad_residue_formula_count"]
            if (P, k) in interesting:
                samples.append(row)

    return {
        "max_prime": max_prime,
        "k_range": "1<=k<P in this implementation audit",
        "row_count": row_count,
        "active_residual_row_count": active_rows,
        "total_edges_R30": total_edges,
        "branch_totals": dict(branch_totals),
        "all_q_side_boundary_caps_absent": bad_cap_total == 0,
        "all_edges_floor_branch_covered": bad_floor_total == 0,
        "all_floor_residue_formulas_verified": bad_formula_total == 0,
        "bad_cap_total": bad_cap_total,
        "bad_floor_coverage_total": bad_floor_total,
        "bad_residue_formula_total": bad_formula_total,
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
    matched = load_json(MATCHED_JSON)
    three_claims = load_json(THREE_CLAIMS_JSON)
    finite_audit = audit_rows()
    return {
        "certificate_type": "prime_matrix_phi_lpf_floor_residue_branch_phase_closure_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "floor_residue_branch_normal_form_closed_phase_saving_open",
        "three_claim_triage": [
            {
                "claim": "Prime Matrix row/column Phi-LPF",
                "frontier_before": matched.get("latest_narrowest_mouth"),
                "fastest_subgate": "PrimeQFloorResidueBranchNormalForm",
                "chosen": True,
                "reason": "exact floor-residue algebra after matched displacement closure; no new prime theorem required",
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
                "reason": "verification package, not a closable floor-residue phase gate",
            },
        ],
        "three_claim_source_status": three_claims.get("plain_conclusion"),
        "floor_residue_branch_theorem": {
            "lower_cap_absence": "A residual edge cannot be supported by the q-side lower cap m>=q: m=q is prime and the only other possible point q+1 is even.",
            "upper_cap_absence": "A residual edge cannot be supported by the q-side upper cap m<=2P-1: q(2P-1)>P^2 for every integer q>P/2.",
            "lower_branch": "If m=floor(kP/q)+1, then d=q-(kP mod q), with 1<=d<=q.",
            "upper_branch": "If m=floor(((k+1)P-1)/q), then d=P-1-(((k+1)P-1) mod q), with P-q<=d<=P-1.",
            "normal_form": "The matched phase is a sum over lower/upper floor-residue branches, not over unclipped endpoint labels.",
            "not_enough": "The lower/upper branch residues still move with the LPF-selected matching graph; no cancellation follows from this identity alone.",
        },
        "finite_audit": finite_audit,
        "external_frontier_match_table": [
            {
                "source": "Elementary floor-residue algebra",
                "useful_part": "closes the q-side cap-free lower/upper residue branch formulas",
                "accepted_for_this_gate": True,
                "closes_phase_saving": False,
                "reason_not_direct": "normalises branches only; gives no cancellation over LPF-selected primes",
            },
            {
                "source": "Milićević--Qin--Wu 2025 arXiv:2511.07550",
                "useful_part": "power-saving bilinear Kloosterman estimates for arbitrary moduli",
                "accepted_for_this_gate": False,
                "closes_phase_saving": False,
                "reason_not_direct": "floor-residue branches are not yet completed bilinear Kloosterman sums",
            },
            {
                "source": "Pascadi 2025 arXiv:2511.08445",
                "useful_part": "Type-II Kloosterman sums with composite moduli via non-abelian amplification",
                "accepted_for_this_gate": False,
                "closes_phase_saving": False,
                "reason_not_direct": "the current modulus is prime q and the graph is a fixed-row matched subset",
            },
            {
                "source": "Shao--Shparlinski--Wijaya 2024/2025 arXiv:2411.12113",
                "useful_part": "Kloosterman sums parametrised by square-free and smooth integers",
                "accepted_for_this_gate": False,
                "closes_phase_saving": False,
                "reason_not_direct": "requires finite-field/Kloosterman completion before it can see these floor residues",
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
                "PrimeQBoundaryCapFreeForResidualEdges",
                True,
                True,
                "Residual edges cannot arise from q-side lower cap m=q or upper cap m=2P-1.",
                "none",
            ),
            gate(
                "PrimeQFloorResidueBranchNormalForm",
                True,
                True,
                "Every residual edge belongs to a lower and/or upper floor-residue branch with the exact d formulas.",
                "none",
            ),
            gate(
                "PrimeQFloorResidueBranchPhaseSaving",
                False,
                False,
                "For |h|<=polylog(P), prove cancellation over the lower/upper floor-residue branch sums.",
                "floor-residue branch phase theorem",
            ),
            gate(
                "CompletionToExternalKloostermanOrVaughanTypeII",
                False,
                False,
                "Convert the floor-residue branch graph to a DI/DFI/BC/FM-compatible estimate without losing pointwise P,k.",
                "completion/dispersion identity",
            ),
        ],
        "latest_narrowest_mouth": [
            "PrimeQFloorResidueBranchPhaseSaving",
            "AND CompletionToExternalKloostermanOrVaughanTypeII",
        ],
        "floor_residue_branch_normal_form_closed": True,
        "floor_residue_branch_phase_saving_closed": False,
        "phi_lpf_parity_barrier_globally_broken": False,
        "row_column_unconditional_closed": False,
        "external_lemma_version_unconditional_closed": False,
        "internal_self_contained_closed": False,
        "source_hashes": source_hashes(),
    }


def build_markdown(payload: dict[str, Any]) -> str:
    """生成 Markdown 证书。"""
    theorem = payload["floor_residue_branch_theorem"]
    audit = payload["finite_audit"]
    lines = [
        "# Prime Matrix Phi-LPF floor residue branch phase closure 审计",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['frontier_verified_date']}`",
        "",
        "## 1. 三命题选择",
        "",
        table(payload["three_claim_triage"], ["claim", "frontier", "frontier_before", "fastest_subgate", "chosen", "reason"]),
        "",
        "matched displacement 闭合后，本轮继续选择行/列 Phi-LPF 的 q-side floor-residue branch 子门。该门只用整数端点与余数恒等式闭合；它不证明后续相位和抵消。",
        "",
        "## 2. floor-residue branch 正规形",
        "",
        "```text",
        f"lower_cap_absence={theorem['lower_cap_absence']}",
        f"upper_cap_absence={theorem['upper_cap_absence']}",
        f"lower_branch={theorem['lower_branch']}",
        f"upper_branch={theorem['upper_branch']}",
        f"normal_form={theorem['normal_form']}",
        f"not_enough={theorem['not_enough']}",
        "```",
        "",
        "设 `rho=(kP mod q)`、`sigma=(((k+1)P-1) mod q)`。lower floor branch 给 `d=q-rho`；upper floor branch 给 `d=P-1-sigma`。若一个点同时是 lower 与 upper，则两个公式给出同一个 `d`。",
        "",
        "## 3. 全量有限审计",
        "",
        "```text",
        f"max_prime={audit['max_prime']}",
        f"k_range={audit['k_range']}",
        f"row_count={audit['row_count']}",
        f"active_residual_row_count={audit['active_residual_row_count']}",
        f"total_edges_R30={audit['total_edges_R30']}",
        f"branch_totals={audit['branch_totals']}",
        f"all_q_side_boundary_caps_absent={bool_text(audit['all_q_side_boundary_caps_absent'])}",
        f"all_edges_floor_branch_covered={bool_text(audit['all_edges_floor_branch_covered'])}",
        f"all_floor_residue_formulas_verified={bool_text(audit['all_floor_residue_formulas_verified'])}",
        f"bad_cap_total={audit['bad_cap_total']}",
        f"bad_floor_coverage_total={audit['bad_floor_coverage_total']}",
        f"bad_residue_formula_total={audit['bad_residue_formula_total']}",
        "```",
        "",
        "有限审计只验证实现和账本一致性；全局闭合来自 q-side cap 排除和 floor-residue 恒等式。",
        "",
        "代表行：",
        "",
        table(
            audit["sample_rows"],
            [
                "P",
                "k",
                "edge_count_R30",
                "branch_lower",
                "branch_upper",
                "branch_both",
                "min_lower_or_both_displacement",
                "max_lower_or_both_displacement",
                "min_upper_or_both_displacement",
                "max_upper_or_both_displacement",
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
        "外部 Kloosterman/Type-II 前沿仍是后续相位门候选；本层只把 matched displacement phase 精确拆成 lower/upper floor-residue branch phase。",
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
        f"floor_residue_branch_normal_form_closed={bool_text(payload['floor_residue_branch_normal_form_closed'])}",
        f"floor_residue_branch_phase_saving_closed={bool_text(payload['floor_residue_branch_phase_saving_closed'])}",
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
    print("floor_residue_branch_normal_form_closed=true")
    print("floor_residue_branch_phase_saving_closed=false")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
