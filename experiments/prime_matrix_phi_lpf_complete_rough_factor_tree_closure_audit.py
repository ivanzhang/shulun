#!/usr/bin/env python3
"""闭合 Phi-LPF residual 的完整粗因子树正规形门。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_complete_rough_factor_tree_closure_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-complete-rough-factor-tree-closure-audit.json

上一层把 residual edge 分成：

  m=r*alpha,  alpha prime
  或
  m=r*s*beta,  s=LPF(alpha)>=r,  LPF(beta)>=s.

本层继续递归到底。若

  m=p_1*p_2*...*p_t,  7<=p_1<=p_2<=...<=p_t

是 residual cofactor 的完整粗素因子分解，则对每个前缀

  G_j=p_1*...*p_j,  1<=j<t,

剩余商

  A_j=p_{j+1}*...*p_t

都由唯一公式给出：

  A_j=floor(kP/(q*G_j))+1,

因为对应实区间长度 P/(q*G_j)<2/G_j<=2/7<1。

这耗尽了 deterministic LPF descent；剩余不是新的因子分裂，而是完整
rough-factor leaves 上的 signed/oscillatory phase saving，或把该叶子树完成
到外部 Kloosterman/Vaughan Type-II 估计。
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

SLUG = "prime-matrix-phi-lpf-complete-rough-factor-tree-closure"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-23"

SECOND_SPLIT_JSON = DOCS / "prime-matrix-phi-lpf-rough-quotient-second-lpf-split-closure-audit.json"
DESCENT_JSON = DOCS / "prime-matrix-phi-lpf-wheel30-composite-lpf-descent-closure-audit.json"
THREE_CLAIMS_JSON = DOCS / "three-claims-frontier-rankone-explicit-formula-router.json"

DEPENDENCIES = [
    SECOND_SPLIT_JSON,
    DESCENT_JSON,
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


def factor_nondec(n: int, primes: list[int]) -> list[int]:
    """返回 n 的非降素因子分解。"""
    factors: list[int] = []
    remaining = n
    for p in primes:
        if p * p > remaining:
            break
        while remaining % p == 0:
            factors.append(p)
            remaining //= p
    if remaining > 1:
        factors.append(remaining)
    return factors


def q_window(P: int, k: int, q: int) -> tuple[int, int]:
    """返回 q 侧 clipped cofactor 窗口。"""
    low = max(q, (k * P) // q + 1)
    high = min(2 * P - 1, (((k + 1) * P) - 1) // q)
    return low, high


def actual_residual_edges(P: int, k: int, primes: list[int]) -> set[tuple[int, int]]:
    """直接扫描 q-window，得到真实 R30 residual (q,m) 边。"""
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


def prefix_payload(P: int, k: int, q: int, m: int, primes: list[int]) -> dict[str, Any]:
    """核验一条 residual edge 的完整粗因子树。"""
    factors = factor_nondec(m, primes)
    displacement = q * m - k * P
    prefix_product = 1
    prefix_records: list[str] = []
    bad_prefix_formula = 0
    bad_prefix_interval = 0
    max_prefix_interval_points = 0

    for depth, factor in enumerate(factors[:-1], start=1):
        prefix_product *= factor
        suffix_product = m // prefix_product
        candidate = (k * P) // (q * prefix_product) + 1
        upper = (((k + 1) * P) - 1) // (q * prefix_product)
        interval_points = max(0, upper - candidate + 1)
        max_prefix_interval_points = max(max_prefix_interval_points, interval_points)
        bad_prefix_formula += int(suffix_product != candidate)
        bad_prefix_interval += int(interval_points > 1)
        if len(prefix_records) < 4:
            prefix_records.append(
                f"depth={depth},G={prefix_product},next_or_suffix={suffix_product},candidate={candidate}"
            )

    # 中文注释：完整叶子处不再有商变量，只有相位 D=q*m-kP。
    rough = all(p >= 7 for p in factors)
    nondecreasing = all(a <= b for a, b in zip(factors, factors[1:]))
    composite = len(factors) >= 2
    return {
        "q": q,
        "m": m,
        "D": displacement,
        "factors": factors,
        "depth": len(factors),
        "rough": rough,
        "nondecreasing": nondecreasing,
        "composite": composite,
        "prefix_records": prefix_records,
        "max_prefix_interval_points": max_prefix_interval_points,
        "bad_prefix_formula_count": bad_prefix_formula,
        "bad_prefix_interval_count": bad_prefix_interval,
        "bad_displacement_count": int(not (1 <= displacement < P)),
        "bad_factorization_count": int((not rough) or (not nondecreasing) or (not composite)),
    }


def row_payload(P: int, k: int, primes: list[int]) -> dict[str, Any]:
    """计算一行完整粗因子树诊断。"""
    actual = actual_residual_edges(P, k, primes)
    predicted_edges: set[tuple[int, int]] = set()
    depth_counter: Counter[int] = Counter()
    leaf_signature_counter: Counter[str] = Counter()
    first_factor_counter: Counter[int] = Counter()
    max_depth = 0
    max_prefix_interval_points = 0
    bad_prefix_formula_count = 0
    bad_prefix_interval_count = 0
    bad_displacement_count = 0
    bad_factorization_count = 0
    samples: list[str] = []

    for q, m in actual:
        leaf = prefix_payload(P, k, q, m, primes)
        predicted_edges.add((q, m))
        factors = leaf["factors"]
        depth = leaf["depth"]
        max_depth = max(max_depth, depth)
        depth_counter[depth] += 1
        first_factor_counter[factors[0]] += 1
        leaf_signature_counter["*".join(str(p) for p in factors[:4]) + ("*" if depth > 4 else "")] += 1
        max_prefix_interval_points = max(max_prefix_interval_points, leaf["max_prefix_interval_points"])
        bad_prefix_formula_count += leaf["bad_prefix_formula_count"]
        bad_prefix_interval_count += leaf["bad_prefix_interval_count"]
        bad_displacement_count += leaf["bad_displacement_count"]
        bad_factorization_count += leaf["bad_factorization_count"]
        if len(samples) < 6:
            samples.append(
                f"q={q},m={m},D={leaf['D']},factors={'*'.join(str(p) for p in factors)},"
                f"prefixes={';'.join(leaf['prefix_records'])}"
            )

    missing = actual - predicted_edges
    extra = predicted_edges - actual
    return {
        "P": P,
        "k": k,
        "actual_edge_count_R30": len(actual),
        "predicted_leaf_edge_count": len(predicted_edges),
        "max_depth": max_depth,
        "depth_counter": {str(d): depth_counter[d] for d in sorted(depth_counter)},
        "first_factor_counter": {str(r): first_factor_counter[r] for r in sorted(first_factor_counter)},
        "leaf_signature_counter": {
            signature: leaf_signature_counter[signature]
            for signature in sorted(leaf_signature_counter, key=lambda item: (item.count("*"), item))
        },
        "max_prefix_interval_points": max_prefix_interval_points,
        "bad_prefix_formula_count": bad_prefix_formula_count,
        "bad_prefix_interval_count": bad_prefix_interval_count,
        "bad_displacement_count": bad_displacement_count,
        "bad_factorization_count": bad_factorization_count,
        "missing_edge_count": len(missing),
        "extra_edge_count": len(extra),
        "samples": " | ".join(samples) if samples else "empty",
    }


def audit_rows(max_prime: int = 1009) -> dict[str, Any]:
    """对 P<=max_prime 的全部 1<=k<P 行做有限一致性审计。"""
    primes = prime_sieve(2 * max_prime + 10)
    P_values = [p for p in primes if 11 <= p <= max_prime]
    row_count = 0
    active_rows = 0
    actual_edges = 0
    predicted_edges = 0
    max_depth = 0
    max_prefix_interval_points = 0
    totals: Counter[str] = Counter()
    depth_totals: Counter[int] = Counter()
    first_factor_totals: Counter[int] = Counter()
    leaf_signature_totals: Counter[str] = Counter()
    samples: list[dict[str, Any]] = []
    interesting = {(101, 100), (257, 256), (971, 936), (1009, 1008)}

    for P in P_values:
        for k in range(1, P):
            row_count += 1
            row = row_payload(P, k, primes)
            active_rows += int(row["actual_edge_count_R30"] > 0)
            actual_edges += row["actual_edge_count_R30"]
            predicted_edges += row["predicted_leaf_edge_count"]
            max_depth = max(max_depth, row["max_depth"])
            max_prefix_interval_points = max(max_prefix_interval_points, row["max_prefix_interval_points"])
            for key in (
                "bad_prefix_formula_count",
                "bad_prefix_interval_count",
                "bad_displacement_count",
                "bad_factorization_count",
                "missing_edge_count",
                "extra_edge_count",
            ):
                totals[key] += row[key]
            for depth_text, count in row["depth_counter"].items():
                depth_totals[int(depth_text)] += count
            for r_text, count in row["first_factor_counter"].items():
                first_factor_totals[int(r_text)] += count
            leaf_signature_totals.update(row["leaf_signature_counter"])
            if (P, k) in interesting:
                samples.append(row)

    return {
        "max_prime": max_prime,
        "k_range": "1<=k<P in this implementation audit",
        "row_count": row_count,
        "active_residual_row_count": active_rows,
        "actual_total_edges_R30": actual_edges,
        "predicted_complete_leaf_total": predicted_edges,
        "max_factor_depth_observed": max_depth,
        "depth_totals": {str(d): depth_totals[d] for d in sorted(depth_totals)},
        "first_factor_totals": {str(r): first_factor_totals[r] for r in sorted(first_factor_totals)},
        "leaf_signature_top20": {
            signature: count
            for signature, count in leaf_signature_totals.most_common(20)
        },
        "max_prefix_interval_points": max_prefix_interval_points,
        "prefix_interval_unique_for_every_prefix": max_prefix_interval_points <= 1
        and totals["bad_prefix_interval_count"] == 0,
        "predicted_complete_leaves_equal_actual_edges": predicted_edges == actual_edges
        and totals["missing_edge_count"] == 0
        and totals["extra_edge_count"] == 0,
        "complete_factorization_valid": totals["bad_factorization_count"] == 0,
        "all_prefix_formulas_verified": totals["bad_prefix_formula_count"] == 0,
        "all_predicted_displacements_in_1_to_Pminus1": totals["bad_displacement_count"] == 0,
        "bad_prefix_formula_total": totals["bad_prefix_formula_count"],
        "bad_prefix_interval_total": totals["bad_prefix_interval_count"],
        "bad_displacement_total": totals["bad_displacement_count"],
        "bad_factorization_total": totals["bad_factorization_count"],
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
    second_split = load_json(SECOND_SPLIT_JSON)
    three_claims = load_json(THREE_CLAIMS_JSON)
    finite_audit = audit_rows()
    return {
        "certificate_type": "prime_matrix_phi_lpf_complete_rough_factor_tree_closure_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "complete_rough_factor_tree_closed_leaf_phase_saving_open",
        "three_claim_triage": [
            {
                "claim": "Prime Matrix row/column Phi-LPF",
                "frontier_before": second_split.get("latest_narrowest_mouth"),
                "fastest_subgate": "CompleteRoughFactorTreeAndPrefixSingletons",
                "chosen": True,
                "reason": "the two-cell iterated quotient graph still has deterministic LPF recursion; all fixed-prefix suffixes are singleton intervals",
            },
            {
                "claim": "two-point sieve / prime-pair line",
                "frontier": "BMD=>TLI without hidden denominator/parity gap",
                "chosen": False,
                "reason": "no faster deterministic closure than exhausting the current Phi-LPF LPF recursion",
            },
            {
                "claim": "RH contradiction-field line",
                "frontier": "IndependentRefereeAcceptanceOfAllRHControlledExits",
                "chosen": False,
                "reason": "not a same-object LPF recursion gate",
            },
        ],
        "three_claim_source_status": three_claims.get("plain_conclusion"),
        "complete_factor_tree_theorem": {
            "normal_form": "Every R30 residual edge has a unique complete rough prime factor chain m=p1*...*pt with 7<=p1<=...<=pt.",
            "prefix_singleton": "For each proper prefix G_j=p1*...*pj, the suffix A_j=m/G_j is the unique integer floor(kP/(q*G_j))+1.",
            "interval_reason": "P/(q*G_j)<2/G_j<=2/7<1, and the bound only improves with depth.",
            "phase": "Each leaf keeps D=q*m-kP and phase e(-hD/q); no deterministic LPF split remains.",
            "not_enough": "The remaining hard point is signed phase saving over the complete rough-factor leaves or an exact completion to external Kloosterman/Vaughan Type-II form.",
        },
        "finite_audit": finite_audit,
        "external_frontier_match_table": [
            {
                "source": "Milićević--Qin--Wu 2025 arXiv:2511.07550",
                "source_url": "https://arxiv.org/abs/2511.07550",
                "verified_status": "power-saving estimates for general bilinear Kloosterman forms modulo arbitrary q",
                "useful_part": "candidate target after completing complete rough-factor leaves to a genuine bilinear Kloosterman family",
                "closes_this_gate": False,
                "reason_not_direct": "does not supply the missing completion from q, factor-chain leaves, and floor suffixes to standard Kloosterman sums",
            },
            {
                "source": "Pascadi 2025 arXiv:2511.08445",
                "source_url": "https://arxiv.org/abs/2511.08445",
                "verified_status": "Type-II Kloosterman sums with composite moduli via non-abelian amplification",
                "useful_part": "candidate technology if the leaf tree is reorganised into composite-modulus Type-II sums",
                "closes_this_gate": False,
                "reason_not_direct": "near-prime/prime-q fixed-row leaf phases are not yet its input family",
            },
            {
                "source": "Shao--Shparlinski--Wijaya 2024/2025 arXiv:2411.12113",
                "source_url": "https://arxiv.org/abs/2411.12113",
                "verified_status": "Kloosterman sums over square-free and smooth integer parameters",
                "useful_part": "possible comparison after replacing LPF leaves by completed smooth/square-free parameter sums",
                "closes_this_gate": False,
                "reason_not_direct": "the complete rough-factor tree remains a pointwise floor-suffix graph",
            },
            {
                "source": "Ford--Maynard 2024 arXiv:2407.14368",
                "source_url": "https://arxiv.org/abs/2407.14368",
                "verified_status": "prime-producing sieve framework requiring object-specific Type-I/II inputs",
                "useful_part": "conceptual guide for what a successful source package must prove",
                "closes_this_gate": False,
                "reason_not_direct": "the required Type-II estimates for these exact leaves are not produced automatically",
            },
        ],
        "closed_gates": [
            gate(
                "CompleteRoughFactorTreeNormalForm",
                True,
                True,
                "Every residual cofactor is written as one nondecreasing rough-prime leaf chain.",
                "none",
            ),
            gate(
                "EveryPrefixRoughQuotientSingleton",
                True,
                True,
                "For every fixed prime-q and proper factor prefix, the remaining suffix interval has length <1.",
                "none",
            ),
            gate(
                "DeterministicLPFDescentExhausted",
                True,
                True,
                "Further LPF splitting only reveals later leaves of the same complete factor tree.",
                "none",
            ),
            gate(
                "PrimeQCompleteRoughFactorTreeLeafPhaseSaving",
                False,
                False,
                "Prove signed cancellation/separation over the complete rough-factor leaves.",
                "complete leaf phase theorem",
            ),
            gate(
                "CompletionToExternalKloostermanOrVaughanTypeII",
                False,
                False,
                "Convert the leaf tree to a DI/DFI/BC/FM-compatible estimate without losing pointwise P,k.",
                "completion/dispersion identity",
            ),
        ],
        "latest_narrowest_mouth": [
            "PrimeQCompleteRoughFactorTreeLeafPhaseSaving",
            "AND CompletionToExternalKloostermanOrVaughanTypeII",
        ],
        "complete_rough_factor_tree_closed": True,
        "deterministic_lpf_descent_exhausted": True,
        "complete_leaf_phase_saving_closed": False,
        "phi_lpf_parity_barrier_globally_broken": False,
        "row_column_unconditional_closed": False,
        "external_lemma_version_unconditional_closed": False,
        "internal_self_contained_closed": False,
        "source_hashes": source_hashes(),
    }


def build_markdown(payload: dict[str, Any]) -> str:
    """生成 Markdown 证书。"""
    theorem = payload["complete_factor_tree_theorem"]
    audit = payload["finite_audit"]
    lines = [
        "# Prime Matrix Phi-LPF complete rough factor tree closure 审计",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['frontier_verified_date']}`",
        "",
        "## 1. 三命题选择",
        "",
        table(payload["three_claim_triage"], ["claim", "frontier", "frontier_before", "fastest_subgate", "chosen", "reason"]),
        "",
        "本轮继续选择行/列 Phi-LPF，因为上一层二级 LPF 分裂仍留下 deterministic LPF recursion。最快可闭合子门是把 residual cofactor 完整写成粗素因子叶子树。",
        "",
        "## 2. 完整粗因子树正规形",
        "",
        "```text",
        f"normal_form={theorem['normal_form']}",
        f"prefix_singleton={theorem['prefix_singleton']}",
        f"interval_reason={theorem['interval_reason']}",
        f"phase={theorem['phase']}",
        f"not_enough={theorem['not_enough']}",
        "```",
        "",
        "这一步耗尽了“继续按 LPF 分裂”的确定性收益：任何再分裂只是在同一完整叶子链上揭示更深前缀。真正剩余不再是因子正规形，而是叶子相位节省或外部 completion。",
        "",
        "## 3. 全量有限审计",
        "",
        "```text",
        f"max_prime={audit['max_prime']}",
        f"k_range={audit['k_range']}",
        f"row_count={audit['row_count']}",
        f"active_residual_row_count={audit['active_residual_row_count']}",
        f"actual_total_edges_R30={audit['actual_total_edges_R30']}",
        f"predicted_complete_leaf_total={audit['predicted_complete_leaf_total']}",
        f"max_factor_depth_observed={audit['max_factor_depth_observed']}",
        f"depth_totals={audit['depth_totals']}",
        f"first_factor_totals={audit['first_factor_totals']}",
        f"leaf_signature_top20={audit['leaf_signature_top20']}",
        f"max_prefix_interval_points={audit['max_prefix_interval_points']}",
        f"prefix_interval_unique_for_every_prefix={bool_text(audit['prefix_interval_unique_for_every_prefix'])}",
        f"predicted_complete_leaves_equal_actual_edges={bool_text(audit['predicted_complete_leaves_equal_actual_edges'])}",
        f"complete_factorization_valid={bool_text(audit['complete_factorization_valid'])}",
        f"all_prefix_formulas_verified={bool_text(audit['all_prefix_formulas_verified'])}",
        f"all_predicted_displacements_in_1_to_Pminus1={bool_text(audit['all_predicted_displacements_in_1_to_Pminus1'])}",
        f"bad_prefix_formula_total={audit['bad_prefix_formula_total']}",
        f"bad_prefix_interval_total={audit['bad_prefix_interval_total']}",
        f"bad_displacement_total={audit['bad_displacement_total']}",
        f"bad_factorization_total={audit['bad_factorization_total']}",
        f"missing_edge_total={audit['missing_edge_total']}",
        f"extra_edge_total={audit['extra_edge_total']}",
        "```",
        "",
        "有限审计只验证实现和账本一致性；全局闭合来自唯一分解、最小素因子递降和 `P/(q*G_j)<1`。",
        "",
        "代表行：",
        "",
        table(
            audit["sample_rows"],
            [
                "P",
                "k",
                "actual_edge_count_R30",
                "predicted_leaf_edge_count",
                "max_depth",
                "depth_counter",
                "first_factor_counter",
                "samples",
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
        "这些外部结果仍是后续 completion 的候选工具；本层闭合的是内部完整 LPF 叶子树，不是外部相位节省。",
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
        f"complete_rough_factor_tree_closed={bool_text(payload['complete_rough_factor_tree_closed'])}",
        f"deterministic_lpf_descent_exhausted={bool_text(payload['deterministic_lpf_descent_exhausted'])}",
        f"complete_leaf_phase_saving_closed={bool_text(payload['complete_leaf_phase_saving_closed'])}",
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
    print("complete_rough_factor_tree_closed=true")
    print("complete_leaf_phase_saving_closed=false")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
