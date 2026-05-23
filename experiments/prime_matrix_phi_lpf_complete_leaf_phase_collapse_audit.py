#!/usr/bin/env python3
"""审计 complete rough-factor leaves 的 q-only phase collapse。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_complete_leaf_phase_collapse_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-complete-leaf-phase-collapse-audit.json

上一层把 residual cofactor 写成完整粗因子叶子：

  m=p_1*...*p_t,  7<=p_1<=...<=p_t.

本层关闭一个相位层硬点：这些叶子的 matched displacement phase

  D=qm-kP,  e(-hD/q)

在模 q 意义下不依赖 m 或任何叶子因子，因为

  D == -kP (mod q),  e(-hD/q)=e(hkP/q).

所以 complete factor tree 内部没有新的振荡可榨取；叶子树只决定 prime-q
支撑集合。剩余真硬点是这个 q 支撑集合上的 reciprocal phase saving，或把
该支撑集合完成到外部 Kloosterman/Vaughan Type-II 输入。
"""

from __future__ import annotations

import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-complete-leaf-phase-collapse"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-23"

COMPLETE_TREE_JSON = DOCS / "prime-matrix-phi-lpf-complete-rough-factor-tree-closure-audit.json"
SECOND_SPLIT_JSON = DOCS / "prime-matrix-phi-lpf-rough-quotient-second-lpf-split-closure-audit.json"
THREE_CLAIMS_JSON = DOCS / "three-claims-frontier-rankone-explicit-formula-router.json"

DEPENDENCIES = [
    COMPLETE_TREE_JSON,
    SECOND_SPLIT_JSON,
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


def row_payload(P: int, k: int, primes: list[int]) -> dict[str, Any]:
    """计算一行的 phase-collapse 诊断。"""
    actual = actual_residual_edges(P, k, primes)
    q_to_edges: dict[int, list[int]] = defaultdict(list)
    phase_residue_by_q: dict[int, set[int]] = defaultdict(set)
    leaf_signature_counter: Counter[str] = Counter()
    depth_counter: Counter[int] = Counter()
    bad_phase_residue_count = 0
    bad_displacement_count = 0
    bad_factor_leaf_count = 0
    samples: list[str] = []

    for q, m in actual:
        q_to_edges[q].append(m)
        D = q * m - k * P
        expected = (-k * P) % q
        actual_residue = D % q
        phase_residue_by_q[q].add(actual_residue)
        bad_phase_residue_count += int(actual_residue != expected)
        bad_displacement_count += int(not (1 <= D < P))
        factors = factor_nondec(m, primes)
        rough_leaf = len(factors) >= 2 and all(p >= 7 for p in factors)
        nondecreasing = all(a <= b for a, b in zip(factors, factors[1:]))
        bad_factor_leaf_count += int((not rough_leaf) or (not nondecreasing))
        depth_counter[len(factors)] += 1
        leaf_signature_counter["*".join(str(p) for p in factors[:4]) + ("*" if len(factors) > 4 else "")] += 1
        if len(samples) < 6:
            samples.append(
                f"q={q},m={m},D={D},Dmodq={actual_residue},expected={expected},"
                f"phase=e(h*kP/q),factors={'*'.join(str(p) for p in factors)}"
            )

    max_q_leaf_multiplicity = max((len(ms) for ms in q_to_edges.values()), default=0)
    max_phase_residue_count_per_q = max((len(values) for values in phase_residue_by_q.values()), default=0)
    q_multiplicity_counter = Counter(len(ms) for ms in q_to_edges.values())
    return {
        "P": P,
        "k": k,
        "actual_edge_count_R30": len(actual),
        "support_q_count": len(q_to_edges),
        "max_q_leaf_multiplicity": max_q_leaf_multiplicity,
        "q_multiplicity_counter": {str(n): q_multiplicity_counter[n] for n in sorted(q_multiplicity_counter)},
        "max_phase_residue_count_per_q": max_phase_residue_count_per_q,
        "depth_counter": {str(d): depth_counter[d] for d in sorted(depth_counter)},
        "leaf_signature_counter": {
            signature: leaf_signature_counter[signature]
            for signature in sorted(leaf_signature_counter, key=lambda item: (item.count("*"), item))
        },
        "bad_phase_residue_count": bad_phase_residue_count,
        "bad_displacement_count": bad_displacement_count,
        "bad_factor_leaf_count": bad_factor_leaf_count,
        "samples": " | ".join(samples) if samples else "empty",
    }


def audit_rows(max_prime: int = 1009) -> dict[str, Any]:
    """对 P<=max_prime 的全部 1<=k<P 行做有限一致性审计。"""
    primes = prime_sieve(2 * max_prime + 10)
    P_values = [p for p in primes if 11 <= p <= max_prime]
    row_count = 0
    active_rows = 0
    actual_edges = 0
    support_q_total = 0
    max_q_leaf_multiplicity = 0
    max_phase_residue_count_per_q = 0
    totals: Counter[str] = Counter()
    depth_totals: Counter[int] = Counter()
    q_multiplicity_totals: Counter[int] = Counter()
    leaf_signature_totals: Counter[str] = Counter()
    samples: list[dict[str, Any]] = []
    interesting = {(101, 100), (257, 256), (971, 936), (1009, 1008)}

    for P in P_values:
        for k in range(1, P):
            row_count += 1
            row = row_payload(P, k, primes)
            active_rows += int(row["actual_edge_count_R30"] > 0)
            actual_edges += row["actual_edge_count_R30"]
            support_q_total += row["support_q_count"]
            max_q_leaf_multiplicity = max(max_q_leaf_multiplicity, row["max_q_leaf_multiplicity"])
            max_phase_residue_count_per_q = max(
                max_phase_residue_count_per_q, row["max_phase_residue_count_per_q"]
            )
            for key in ("bad_phase_residue_count", "bad_displacement_count", "bad_factor_leaf_count"):
                totals[key] += row[key]
            for depth_text, count in row["depth_counter"].items():
                depth_totals[int(depth_text)] += count
            for multiplicity_text, count in row["q_multiplicity_counter"].items():
                q_multiplicity_totals[int(multiplicity_text)] += count
            leaf_signature_totals.update(row["leaf_signature_counter"])
            if (P, k) in interesting:
                samples.append(row)

    return {
        "max_prime": max_prime,
        "k_range": "1<=k<P in this implementation audit",
        "row_count": row_count,
        "active_residual_row_count": active_rows,
        "actual_total_edges_R30": actual_edges,
        "support_q_total": support_q_total,
        "support_q_total_equals_edge_total": support_q_total == actual_edges,
        "max_q_leaf_multiplicity": max_q_leaf_multiplicity,
        "q_multiplicity_totals": {
            str(n): q_multiplicity_totals[n] for n in sorted(q_multiplicity_totals)
        },
        "max_phase_residue_count_per_q": max_phase_residue_count_per_q,
        "phase_residue_q_only_for_every_leaf": totals["bad_phase_residue_count"] == 0
        and max_phase_residue_count_per_q <= 1,
        "all_predicted_displacements_in_1_to_Pminus1": totals["bad_displacement_count"] == 0,
        "all_factor_leaves_valid": totals["bad_factor_leaf_count"] == 0,
        "depth_totals": {str(d): depth_totals[d] for d in sorted(depth_totals)},
        "leaf_signature_top20": {
            signature: count for signature, count in leaf_signature_totals.most_common(20)
        },
        "bad_phase_residue_total": totals["bad_phase_residue_count"],
        "bad_displacement_total": totals["bad_displacement_count"],
        "bad_factor_leaf_total": totals["bad_factor_leaf_count"],
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
    complete_tree = load_json(COMPLETE_TREE_JSON)
    three_claims = load_json(THREE_CLAIMS_JSON)
    finite_audit = audit_rows()
    return {
        "certificate_type": "prime_matrix_phi_lpf_complete_leaf_phase_collapse_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "complete_leaf_phase_collapsed_to_prime_q_support_phase_open",
        "three_claim_triage": [
            {
                "claim": "Prime Matrix row/column Phi-LPF",
                "frontier_before": complete_tree.get("latest_narrowest_mouth"),
                "fastest_subgate": "CompleteLeafPhaseCollapseToPrimeQSupport",
                "chosen": True,
                "reason": "the complete leaf phase has an immediate q-only congruence, so internal factor-tree oscillation is not a real source of saving",
            },
            {
                "claim": "two-point sieve / prime-pair line",
                "frontier": "BMD=>TLI without hidden denominator/parity gap",
                "chosen": False,
                "reason": "no faster deterministic phase-collapse gate than the current Phi-LPF leaf phase",
            },
            {
                "claim": "RH contradiction-field line",
                "frontier": "IndependentRefereeAcceptanceOfAllRHControlledExits",
                "chosen": False,
                "reason": "not a same-object leaf-phase gate",
            },
        ],
        "three_claim_source_status": three_claims.get("plain_conclusion"),
        "phase_collapse_theorem": {
            "congruence": "For every complete leaf edge, D=q*m-kP satisfies D == -kP (mod q).",
            "phase_identity": "For every integer h, e(-hD/q)=e(h*kP/q).",
            "support_form": "The complete factor tree only supplies a 0/1 prime-q support set in the audited row model.",
            "no_internal_leaf_oscillation": "Leaves with the same q have the same phase; in fact the audited residual graph has max q-leaf multiplicity 1.",
            "not_enough": "The remaining hard point is nontrivial control of the prime-q support set, or a completion to external Kloosterman/Vaughan Type-II estimates.",
        },
        "finite_audit": finite_audit,
        "external_frontier_match_table": [
            {
                "source": "Milićević--Qin--Wu 2025 arXiv:2511.07550",
                "source_url": "https://arxiv.org/abs/2511.07550",
                "verified_status": "power-saving estimates for general bilinear Kloosterman forms modulo arbitrary q",
                "useful_part": "possible target after converting the q-support reciprocal phase into a genuine bilinear Kloosterman family",
                "closes_this_gate": False,
                "reason_not_direct": "this layer shows the leaf phase is q-only; it does not yet provide the required completion identity",
            },
            {
                "source": "Pascadi 2025 arXiv:2511.08445",
                "source_url": "https://arxiv.org/abs/2511.08445",
                "verified_status": "Type-II Kloosterman sums with composite moduli via non-abelian amplification",
                "useful_part": "candidate only after the q-support phase is reorganised into Type-II sums",
                "closes_this_gate": False,
                "reason_not_direct": "the present object is a prime-denominator support phase, not the input Type-II family",
            },
            {
                "source": "Shao--Shparlinski--Wijaya 2024/2025 arXiv:2411.12113",
                "source_url": "https://arxiv.org/abs/2411.12113",
                "verified_status": "Kloosterman sums over square-free and smooth integer parameters; Cambridge version online in 2025",
                "useful_part": "possible comparison after a bridge from LPF support to completed square-free/smooth parameter sums",
                "closes_this_gate": False,
                "reason_not_direct": "q-only reciprocal phase is still not their completed parameter family",
            },
            {
                "source": "Ford--Maynard 2024 arXiv:2407.14368",
                "source_url": "https://arxiv.org/abs/2407.14368",
                "verified_status": "prime-producing sieve framework with required Type-I/II hypotheses",
                "useful_part": "guidance for the support-set theorem one would need",
                "closes_this_gate": False,
                "reason_not_direct": "does not automatically verify Type-I/II estimates for this q-support set",
            },
        ],
        "closed_gates": [
            gate(
                "CompleteLeafPhaseDependsOnlyOnPrimeQ",
                True,
                True,
                "The matched displacement phase of every complete leaf equals e(h*kP/q).",
                "none",
            ),
            gate(
                "NoInternalFactorTreeOscillation",
                True,
                True,
                "The LPF factor chain changes support membership, not the phase at fixed q.",
                "none",
            ),
            gate(
                "LeafTreePhaseSavingReducedToPrimeQSupportPhase",
                True,
                True,
                "Complete-leaf phase saving is reduced to cancellation/separation over the prime-q support set.",
                "none",
            ),
            gate(
                "PrimeQSupportSetReciprocalPhaseSavingBeyondParity",
                False,
                False,
                "Prove nontrivial signed control of the actual q-support set, not an arbitrary subset.",
                "object-sensitive q-support theorem",
            ),
            gate(
                "CompletionToExternalKloostermanOrVaughanTypeII",
                False,
                False,
                "Convert the q-support reciprocal phase to a DI/DFI/BC/FM-compatible estimate without losing pointwise P,k.",
                "completion/dispersion identity",
            ),
        ],
        "latest_narrowest_mouth": [
            "PrimeQSupportSetReciprocalPhaseSavingBeyondParity",
            "AND CompletionToExternalKloostermanOrVaughanTypeII",
        ],
        "complete_leaf_phase_collapsed": True,
        "internal_factor_tree_oscillation_available": False,
        "q_support_phase_saving_closed": False,
        "phi_lpf_parity_barrier_globally_broken": False,
        "row_column_unconditional_closed": False,
        "external_lemma_version_unconditional_closed": False,
        "internal_self_contained_closed": False,
        "source_hashes": source_hashes(),
    }


def build_markdown(payload: dict[str, Any]) -> str:
    """生成 Markdown 证书。"""
    theorem = payload["phase_collapse_theorem"]
    audit = payload["finite_audit"]
    lines = [
        "# Prime Matrix Phi-LPF complete leaf phase collapse 审计",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['frontier_verified_date']}`",
        "",
        "## 1. 三命题选择",
        "",
        table(payload["three_claim_triage"], ["claim", "frontier", "frontier_before", "fastest_subgate", "chosen", "reason"]),
        "",
        "本轮继续选择行/列 Phi-LPF，因为完整因子树层之后仍有一个可无条件关闭的相位门：叶子相位对因子链本身塌缩，只剩 prime-q 支撑集合。",
        "",
        "## 2. 叶子相位塌缩",
        "",
        "```text",
        f"congruence={theorem['congruence']}",
        f"phase_identity={theorem['phase_identity']}",
        f"support_form={theorem['support_form']}",
        f"no_internal_leaf_oscillation={theorem['no_internal_leaf_oscillation']}",
        f"not_enough={theorem['not_enough']}",
        "```",
        "",
        "这一步是非循环下钻后的剪枝：继续分解 LPF 叶子不会产生新的相位振荡。真正剩余转为 actual prime-q 支撑集合的 signed/oscillatory 控制。",
        "",
        "## 3. 全量有限审计",
        "",
        "```text",
        f"max_prime={audit['max_prime']}",
        f"k_range={audit['k_range']}",
        f"row_count={audit['row_count']}",
        f"active_residual_row_count={audit['active_residual_row_count']}",
        f"actual_total_edges_R30={audit['actual_total_edges_R30']}",
        f"support_q_total={audit['support_q_total']}",
        f"support_q_total_equals_edge_total={bool_text(audit['support_q_total_equals_edge_total'])}",
        f"max_q_leaf_multiplicity={audit['max_q_leaf_multiplicity']}",
        f"q_multiplicity_totals={audit['q_multiplicity_totals']}",
        f"max_phase_residue_count_per_q={audit['max_phase_residue_count_per_q']}",
        f"phase_residue_q_only_for_every_leaf={bool_text(audit['phase_residue_q_only_for_every_leaf'])}",
        f"all_predicted_displacements_in_1_to_Pminus1={bool_text(audit['all_predicted_displacements_in_1_to_Pminus1'])}",
        f"all_factor_leaves_valid={bool_text(audit['all_factor_leaves_valid'])}",
        f"depth_totals={audit['depth_totals']}",
        f"leaf_signature_top20={audit['leaf_signature_top20']}",
        f"bad_phase_residue_total={audit['bad_phase_residue_total']}",
        f"bad_displacement_total={audit['bad_displacement_total']}",
        f"bad_factor_leaf_total={audit['bad_factor_leaf_total']}",
        "```",
        "",
        "有限审计只验证实现与账本一致性；全局相位塌缩来自恒等式 `D=qm-kP`。",
        "",
        "代表行：",
        "",
        table(
            audit["sample_rows"],
            [
                "P",
                "k",
                "actual_edge_count_R30",
                "support_q_count",
                "max_q_leaf_multiplicity",
                "max_phase_residue_count_per_q",
                "depth_counter",
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
        "这些外部结果仍是后续 completion 的候选工具；本层闭合的是内部叶子相位塌缩，不是 q 支撑集合相位节省。",
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
        f"complete_leaf_phase_collapsed={bool_text(payload['complete_leaf_phase_collapsed'])}",
        f"internal_factor_tree_oscillation_available={bool_text(payload['internal_factor_tree_oscillation_available'])}",
        f"q_support_phase_saving_closed={bool_text(payload['q_support_phase_saving_closed'])}",
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
    print("complete_leaf_phase_collapsed=true")
    print("q_support_phase_saving_closed=false")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
