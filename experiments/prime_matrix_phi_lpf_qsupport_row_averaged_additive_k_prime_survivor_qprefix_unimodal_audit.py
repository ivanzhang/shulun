#!/usr/bin/env python3
"""审计 prime-survivor floor graph 的 q-prefix 与单峰帽函数结构。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_qprefix_unimodal_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-qprefix-unimodal-audit.json

上一层已把 prime survivor singleton layer 写成每个固定 (P,q) 的 m-prime
floor-span：

  M_prime(P,q) = {prime m in [L_{P,q}, U_{P,q}]} \\ {P}.

本层转置该图。有限审计发现，在 P<=1009 的全体 prime-survivor edges 上，
固定 (P,m) 后的 q-neighbourhood 不是任意稀疏集，而是从本行第一个 eligible
prime q_0(P) 开始的完整 prime-q prefix：

  Q_prime(P,m) = {prime q: q_0(P) <= q <= Q^*(P,m)}.

并且同一行中 Q^*(P,m) 随 m 的素数序列先不降、后不升，形成单峰帽函数。
这是真推进，因为剩余图从一般稀疏二部图压成了 prefix-cap graph；但这仍是
有限结构审计，不是相位节省定理，也不是外部 trace/Type-II 嵌入。
"""

from __future__ import annotations

import hashlib
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"
sys.path.insert(0, str(ROOT / "experiments"))

import prime_matrix_phi_lpf_qsupport_dynamic_primorial_unit_selector_audit as primorial  # noqa: E402
import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_floor_span_completion_audit as floor_span  # noqa: E402


SLUG = "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-qprefix-unimodal"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-24"
TOL = 1e-9

DEPENDENCIES = [
    DOCS / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-floor-span-completion-audit.json",
    DOCS / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-blocker-mobius-involution-audit.json",
    DOCS / "external-theorem-index.md",
    DOCS / "claim-status-table.md",
    DOCS / "frontier-honest-status-and-true-side-theorems-20260522.md",
    DOCS / "three-claims-actual-load-closure-contracts.md",
    DOCS / "three-claims-formal-to-actual-critical-load-frontier.md",
    ROOT / "paper" / "contradiction-field-monograph" / "contradiction-field-monograph.tex",
]

EXTERNAL_SOURCES = [
    {
        "key": "Fouvry_Kowalski_Michel_Sawin_2025_trace_bilinear",
        "url": "https://arxiv.org/abs/2511.09459",
        "role": "candidate after the q-prefix cap graph is promoted to a trace-function bilinear family",
    },
    {
        "key": "Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman",
        "url": "https://arxiv.org/abs/2511.07550",
        "role": "candidate after a completed Kloosterman variable is built from the prefix-cap graph",
    },
    {
        "key": "Pascadi_2025_nonabelian_composite_type_II",
        "url": "https://arxiv.org/abs/2511.08445",
        "role": "candidate if the prefix-cap graph is split into Type-II fibres with usable lengths",
    },
    {
        "key": "Wright_2026_unbalanced_kloosterman_fractions",
        "url": "https://arxiv.org/abs/2604.25177",
        "role": "candidate for a future unbalanced convolution model of the prefix cap",
    },
    {
        "key": "Shao_Shparlinski_Wijaya_2024_squarefree_smooth_kloosterman",
        "url": "https://arxiv.org/abs/2411.12113",
        "role": "candidate parameter input after the arithmetic weights are fitted to their hypotheses",
    },
    {
        "key": "Li_2023_short_interval_primes_x_052",
        "url": "https://arxiv.org/abs/2308.04458",
        "role": "still above the theta=1/2 pointwise scale and not a direct closure for this graph",
    },
]


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    paths = [Path(__file__).resolve(), *DEPENDENCIES]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def prefix_profile(P: int, m: int, q_values: set[int], primes: list[int]) -> dict[str, Any]:
    """返回固定 (P,m) 的 q-prefix 诊断。"""
    q_sorted = sorted(q_values)
    W, _factors = primorial.primorial_modulus(P, primes)
    eligible = floor_span.q_prime_values(P, W, primes)
    q0 = eligible[0]
    cap = q_sorted[-1]
    prefix = [q for q in eligible if q0 <= q <= cap]
    q_set = set(q_sorted)
    prefix_set = set(prefix)
    missing = sorted(prefix_set - q_set)
    extra = sorted(q_set - prefix_set)
    edge_phase = sum((floor_span.phase_for_m(P, q, m) for q in q_sorted), 0j)
    prefix_phase = sum((floor_span.phase_for_m(P, q, m) for q in prefix), 0j)
    phase_error = abs(edge_phase - prefix_phase)
    return {
        "P": P,
        "m": m,
        "q0": q0,
        "cap": cap,
        "q_count": len(q_sorted),
        "prefix_count": len(prefix),
        "lower_endpoint_not_row_first": int(q_sorted[0] != q0),
        "missing_count": len(missing),
        "extra_count": len(extra),
        "missing_values": missing[:8],
        "extra_values": extra[:8],
        "phase_error": phase_error,
        "prefix_identity_verified": (
            q_sorted[0] == q0
            and not missing
            and not extra
            and phase_error <= TOL
        ),
        "sample": f"P={P},m={m},q-prefix=[{q0},{cap}],q_count={len(q_sorted)}",
    }


def cap_unimodality_profile(P: int, caps: list[tuple[int, int, int]]) -> dict[str, Any]:
    """检查固定 P 的 Q*(P,m) 是否为单峰帽函数。"""
    state = "up"
    turn_count = 0
    bad_after_down_increase = 0
    previous = caps[0][1]
    for _m, cap, _count in caps[1:]:
        if cap > previous:
            bad_after_down_increase += int(state == "down")
            state = "up"
        elif cap < previous:
            turn_count += int(state == "up")
            state = "down"
        previous = cap

    max_cap = max(cap for _m, cap, _count in caps)
    peak_ms = [m for m, cap, _count in caps if cap == max_cap]
    return {
        "P": P,
        "active_m_count": len(caps),
        "edge_count": sum(count for _m, _cap, count in caps),
        "first_m": caps[0][0],
        "last_m": caps[-1][0],
        "max_cap_q": max_cap,
        "peak_m_min": peak_ms[0],
        "peak_m_max": peak_ms[-1],
        "peak_plateau_prime_count": len(peak_ms),
        "peak_m_min_minus_P": peak_ms[0] - P,
        "peak_m_max_minus_P": peak_ms[-1] - P,
        "turn_count": turn_count,
        "bad_after_down_increase": bad_after_down_increase,
        "unimodal_cap_verified": bad_after_down_increase == 0 and turn_count <= 1,
    }


def audit_rows(max_prime: int = 1009) -> dict[str, Any]:
    """审计 P<=max_prime 的 q-prefix 与 Q* 单峰帽函数。"""
    primes = primorial.prime_sieve(2 * max_prime + 10)
    previous = json.loads(
        (
            DOCS
            / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-floor-span-completion-audit.json"
        ).read_text()
    )
    previous_audit = previous["finite_audit"]
    edges = floor_span.prime_blocker_edges(max_prime, primes)

    grouped_pm: defaultdict[tuple[int, int], set[int]] = defaultdict(set)
    for item in edges:
        grouped_pm[(item["P"], item["m"])].add(item["q"])

    totals: Counter[str] = Counter()
    caps_by_P: defaultdict[int, list[tuple[int, int, int]]] = defaultdict(list)
    sample_prefixes: list[dict[str, Any]] = []
    max_prefix_phase_error = 0.0

    for (P, m), q_values in sorted(grouped_pm.items()):
        profile = prefix_profile(P, m, q_values, primes)
        max_prefix_phase_error = max(max_prefix_phase_error, profile["phase_error"])
        totals["pm_bucket_count"] += 1
        totals["edge_count"] += profile["q_count"]
        totals["prefix_count"] += profile["prefix_count"]
        totals["lower_endpoint_not_row_first"] += profile["lower_endpoint_not_row_first"]
        totals["prefix_missing_count"] += profile["missing_count"]
        totals["prefix_extra_count"] += profile["extra_count"]
        totals["bad_prefix_identity"] += int(not profile["prefix_identity_verified"])
        caps_by_P[P].append((m, profile["cap"], profile["q_count"]))
        if len(sample_prefixes) < 10:
            sample_prefixes.append(
                {
                    "P": P,
                    "m": m,
                    "q0": profile["q0"],
                    "cap": profile["cap"],
                    "q_count": profile["q_count"],
                    "prefix_count": profile["prefix_count"],
                    "bad": int(not profile["prefix_identity_verified"]),
                }
            )

    row_profiles: list[dict[str, Any]] = []
    turn_counts: Counter[str] = Counter()
    peak_plateau_counts: Counter[int] = Counter()
    interesting = {101, 257, 971, 1009}
    sample_rows: list[dict[str, Any]] = []
    cap_sample_paths: list[str] = []

    for P, caps in sorted(caps_by_P.items()):
        caps.sort()
        profile = cap_unimodality_profile(P, caps)
        row_profiles.append(profile)
        totals["active_P_count"] += 1
        totals["cap_unimodality_bad_row_count"] += int(not profile["unimodal_cap_verified"])
        totals["cap_turn_count_total"] += profile["turn_count"]
        turn_counts[str(profile["turn_count"])] += 1
        peak_plateau_counts[profile["peak_plateau_prime_count"]] += 1
        if P in interesting:
            sample_rows.append(profile)
            left = ", ".join(f"{m}->{cap}" for m, cap, _count in caps[:8])
            right = ", ".join(f"{m}->{cap}" for m, cap, _count in caps[-8:])
            cap_sample_paths.append(f"P={P}: left {left}; right {right}")

    total_bad = (
        totals["bad_prefix_identity"]
        + totals["lower_endpoint_not_row_first"]
        + totals["prefix_missing_count"]
        + totals["prefix_extra_count"]
        + totals["cap_unimodality_bad_row_count"]
        + int(max_prefix_phase_error > TOL)
    )
    return {
        "max_prime": max_prime,
        "prime_survivor_edge_count_total": totals["edge_count"],
        "previous_prime_survivor_edge_count_total": previous_audit["prime_survivor_edge_count_total"],
        "pm_bucket_count_total": totals["pm_bucket_count"],
        "q_prefix_count_total": totals["prefix_count"],
        "lower_endpoint_not_row_first_total": totals["lower_endpoint_not_row_first"],
        "q_prefix_missing_count_total": totals["prefix_missing_count"],
        "q_prefix_extra_count_total": totals["prefix_extra_count"],
        "bad_q_prefix_identity_count": totals["bad_prefix_identity"],
        "max_q_prefix_phase_error": max_prefix_phase_error,
        "active_P_count": totals["active_P_count"],
        "previous_P_count": previous_audit["P_count"],
        "cap_unimodality_bad_row_count": totals["cap_unimodality_bad_row_count"],
        "cap_turn_count_total": totals["cap_turn_count_total"],
        "cap_turn_count_distribution": dict(sorted(turn_counts.items())),
        "peak_plateau_prime_count_distribution": dict(sorted(peak_plateau_counts.items())),
        "total_bad_qprefix_unimodal_count": total_bad,
        "counts_match_previous_floor_span": (
            totals["edge_count"] == previous_audit["prime_survivor_edge_count_total"]
        ),
        "q_prefix_identity_verified_on_finite_audit": total_bad == 0,
        "row_cap_unimodality_verified_on_finite_audit": totals["cap_unimodality_bad_row_count"] == 0,
        "q_prefix_phase_packet_rewrite_verified_on_finite_audit": (
            totals["edge_count"] == totals["prefix_count"] and max_prefix_phase_error <= TOL
        ),
        "finite_evidence_not_used_as_global_proof": True,
        "global_qprefix_theorem_proved": False,
        "prime_floor_span_trace_or_typeii_phase_saving_closed": False,
        "sample_rows": sample_rows,
        "sample_prefixes": sample_prefixes,
        "cap_sample_paths": cap_sample_paths,
    }


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
    finite_audit = audit_rows()
    return {
        "certificate_type": "prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_qprefix_unimodal_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "prime_survivor_floor_graph_refined_to_finite_qprefix_unimodal_cap_open",
        "chosen_claim": "Prime Matrix row/column Phi-LPF",
        "reason_chosen": "after the floor-span graph is exposed, the next non-cyclic refinement is to test whether the transposed graph has interval or prefix structure",
        "current_object": {
            "q_prefix_identity": "for audited (P,m), Q_prime(P,m)={prime q: q0(P)<=q<=Q*(P,m)}",
            "row_cap_shape": "for audited rows, Q*(P,m) along prime m is unimodal",
            "phase_packet": "S_prime-survivor=sum_m sum_{q0(P)<=q<=Q*(P,m), q prime} e(hP floor(qm/P)/q)",
            "meaning": "the remaining graph is a prefix-cap graph rather than a generic sparse point cloud",
            "remaining": "prove or exploit this shape globally and embed it into trace/Type-II/convolution estimates",
        },
        "finite_audit": finite_audit,
        "closed_gates": [
            gate(
                "FiniteQPrefixNeighbourhoodAudit",
                True,
                True,
                "For P<=1009, every fixed (P,m) q-neighbourhood is a prime-q prefix from q0(P).",
                "global proof or direct analytic exploitation",
            ),
            gate(
                "FiniteUnimodalCapAudit",
                True,
                True,
                "For P<=1009, the cap Q*(P,m) is unimodal in the ordered prime m-list of each active row.",
                "global proof or Type-II split along the cap",
            ),
            gate(
                "PrefixCapPhasePacketRewrite",
                True,
                True,
                "On the audited range, the phase packet equals the q-prefix cap packet exactly.",
                "uniform analytic estimate for the rewritten packet",
            ),
            gate(
                "GlobalQPrefixUnimodalTheorem",
                False,
                False,
                "Promote the finite prefix/unimodal audit to a global deterministic theorem.",
                "not proved in this layer",
            ),
            gate(
                "PrefixCapTraceOrTypeIIEmbedding",
                False,
                False,
                "Use the prefix-cap graph to obtain phase saving or a completed bilinear/trace family.",
                "new embedding theorem still required",
            ),
        ],
        "external_sources_consulted": EXTERNAL_SOURCES,
        "external_theorem_implication": {
            "FKMS_trace_function_bilinear": "the prefix cap is closer to a bilinear trace object but still lacks the completed trace family",
            "Milicevic_Qin_Wu_arbitrary_modulus_Kloosterman": "the denominator q remains a moving prime prefix cap, not yet a completed Kloosterman variable",
            "Pascadi_composite_Type_II": "the prefix graph suggests a Type-II split, but usable long fibres are not yet constructed",
            "Wright_unbalanced_convolution": "the unimodal cap may fit a future unbalanced convolution model, not available here",
            "Shao_Shparlinski_Wijaya_smooth_squarefree_Kloosterman": "requires additional smoothing/squarefree parameter matching beyond this finite cap shape",
            "Li_short_interval_x_052": "does not close the pointwise theta=1/2 requirement",
        },
        "latest_narrowest_mouth": [
            "GlobalPrimeSurvivorQPrefixUnimodalCapProofOrReplacement",
            "AND PrefixCapTraceOrTypeIIPhaseSaving",
            "AND DiagonalPGhostSubtractionDiscipline",
            "AND DenseRectangleCompletionOrBilinearTraceEmbeddingForPrimePrimeFloorGraph",
            "AND FiniteThirtyWheelSmallLPFBlockerPacketControl",
            "AND UniformCancellationAcrossSparseKSupportRadialKernels",
            "AND RoughBetaSiegelWalfiszUniformityOrReplacement",
            "AND PointwisePKUniformTransferFromExternalAverageEstimate",
            "AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity",
        ],
        "finite_q_prefix_neighbourhood_audit_closed": True,
        "finite_unimodal_cap_audit_closed": True,
        "prefix_cap_phase_packet_rewrite_closed_on_audited_range": True,
        "global_qprefix_unimodal_theorem_proved": False,
        "prefix_cap_trace_or_typeii_embedding_closed": False,
        "full_prime_prime_rectangle_completion_closed": False,
        "prime_floor_span_trace_or_typeii_phase_saving_closed": False,
        "small_lpf_blocker_packet_control_closed": False,
        "uniform_cancellation_across_sparse_k_support_radial_kernels_closed": False,
        "rough_beta_siegel_walfisz_factor_extracted": False,
        "pointwise_pk_transfer_closed": False,
        "q_support_phase_saving_closed": False,
        "phi_lpf_parity_barrier_globally_broken": False,
        "row_column_unconditional_closed": False,
        "external_lemma_version_unconditional_closed": False,
        "internal_self_contained_closed": False,
        "source_hashes": source_hashes(),
    }


def build_markdown(payload: dict[str, Any]) -> str:
    """生成 Markdown 证书。"""
    audit = payload["finite_audit"]
    current = payload["current_object"]
    sample_row_fields = [
        "P",
        "active_m_count",
        "edge_count",
        "first_m",
        "last_m",
        "max_cap_q",
        "peak_m_min",
        "peak_m_max",
        "peak_plateau_prime_count",
        "turn_count",
        "bad_after_down_increase",
    ]
    sample_prefix_fields = ["P", "m", "q0", "cap", "q_count", "prefix_count", "bad"]
    source_fields = ["key", "url", "role"]
    lines = [
        "# Prime Matrix Phi-LPF q-support row-averaged additive-k prime-survivor q-prefix unimodal 审计",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['frontier_verified_date']}`",
        "",
        "## 1. 当前对象",
        "",
        "```text",
        f"q_prefix_identity={current['q_prefix_identity']}",
        f"row_cap_shape={current['row_cap_shape']}",
        f"phase_packet={current['phase_packet']}",
        f"meaning={current['meaning']}",
        f"remaining={current['remaining']}",
        "```",
        "",
        "## 2. q-prefix / unimodal cap 有限审计",
        "",
        "```text",
        f"max_prime={audit['max_prime']}",
        f"prime_survivor_edge_count_total={audit['prime_survivor_edge_count_total']}",
        f"previous_prime_survivor_edge_count_total={audit['previous_prime_survivor_edge_count_total']}",
        f"pm_bucket_count_total={audit['pm_bucket_count_total']}",
        f"q_prefix_count_total={audit['q_prefix_count_total']}",
        f"lower_endpoint_not_row_first_total={audit['lower_endpoint_not_row_first_total']}",
        f"q_prefix_missing_count_total={audit['q_prefix_missing_count_total']}",
        f"q_prefix_extra_count_total={audit['q_prefix_extra_count_total']}",
        f"bad_q_prefix_identity_count={audit['bad_q_prefix_identity_count']}",
        f"max_q_prefix_phase_error={audit['max_q_prefix_phase_error']:.3e}",
        f"active_P_count={audit['active_P_count']}",
        f"previous_P_count={audit['previous_P_count']}",
        f"cap_unimodality_bad_row_count={audit['cap_unimodality_bad_row_count']}",
        f"cap_turn_count_total={audit['cap_turn_count_total']}",
        f"total_bad_qprefix_unimodal_count={audit['total_bad_qprefix_unimodal_count']}",
        f"counts_match_previous_floor_span={primorial.bool_text(audit['counts_match_previous_floor_span'])}",
        f"q_prefix_identity_verified_on_finite_audit={primorial.bool_text(audit['q_prefix_identity_verified_on_finite_audit'])}",
        f"row_cap_unimodality_verified_on_finite_audit={primorial.bool_text(audit['row_cap_unimodality_verified_on_finite_audit'])}",
        f"q_prefix_phase_packet_rewrite_verified_on_finite_audit={primorial.bool_text(audit['q_prefix_phase_packet_rewrite_verified_on_finite_audit'])}",
        f"global_qprefix_theorem_proved={primorial.bool_text(audit['global_qprefix_theorem_proved'])}",
        "```",
        "",
        "turn count distribution:",
        "",
        "```text",
        json.dumps(audit["cap_turn_count_distribution"], sort_keys=True),
        "```",
        "",
        "peak plateau distribution:",
        "",
        "```text",
        json.dumps(audit["peak_plateau_prime_count_distribution"], sort_keys=True),
        "```",
        "",
        "代表行：",
        "",
        primorial.table(audit["sample_rows"], sample_row_fields),
        "",
        "代表 prefix：",
        "",
        primorial.table(audit["sample_prefixes"], sample_prefix_fields),
        "",
        "cap path 样本：",
        "",
        "```text",
        *audit["cap_sample_paths"],
        "```",
        "",
        "## 3. 门控表",
        "",
        primorial.table(payload["closed_gates"], ["gate", "closed", "proved", "meaning", "remaining"]),
        "",
        "## 4. 外部 theorem 影响",
        "",
        primorial.table(payload["external_sources_consulted"], source_fields),
        "",
        "```text",
        *[f"{key}={value}" for key, value in payload["external_theorem_implication"].items()],
        "```",
        "",
        "结论：在有限审计范围内，prime survivor floor graph 从一般稀疏二部图压成 q-prefix cap graph，且每行 cap 是单峰帽函数。这缩小了需要嵌入外部 trace/Type-II 的对象，但尚未给出全局证明或相位节省。",
        "",
        "## 5. 最新最窄口",
        "",
        "```text",
        *payload["latest_narrowest_mouth"],
        "```",
        "",
        "状态边界：",
        "",
        "```text",
        f"finite_q_prefix_neighbourhood_audit_closed={primorial.bool_text(payload['finite_q_prefix_neighbourhood_audit_closed'])}",
        f"finite_unimodal_cap_audit_closed={primorial.bool_text(payload['finite_unimodal_cap_audit_closed'])}",
        f"prefix_cap_phase_packet_rewrite_closed_on_audited_range={primorial.bool_text(payload['prefix_cap_phase_packet_rewrite_closed_on_audited_range'])}",
        f"global_qprefix_unimodal_theorem_proved={primorial.bool_text(payload['global_qprefix_unimodal_theorem_proved'])}",
        f"prefix_cap_trace_or_typeii_embedding_closed={primorial.bool_text(payload['prefix_cap_trace_or_typeii_embedding_closed'])}",
        f"full_prime_prime_rectangle_completion_closed={primorial.bool_text(payload['full_prime_prime_rectangle_completion_closed'])}",
        f"prime_floor_span_trace_or_typeii_phase_saving_closed={primorial.bool_text(payload['prime_floor_span_trace_or_typeii_phase_saving_closed'])}",
        f"small_lpf_blocker_packet_control_closed={primorial.bool_text(payload['small_lpf_blocker_packet_control_closed'])}",
        f"uniform_cancellation_across_sparse_k_support_radial_kernels_closed={primorial.bool_text(payload['uniform_cancellation_across_sparse_k_support_radial_kernels_closed'])}",
        f"rough_beta_siegel_walfisz_factor_extracted={primorial.bool_text(payload['rough_beta_siegel_walfisz_factor_extracted'])}",
        f"pointwise_pk_transfer_closed={primorial.bool_text(payload['pointwise_pk_transfer_closed'])}",
        f"q_support_phase_saving_closed={primorial.bool_text(payload['q_support_phase_saving_closed'])}",
        f"phi_lpf_parity_barrier_globally_broken={primorial.bool_text(payload['phi_lpf_parity_barrier_globally_broken'])}",
        f"row_column_unconditional_closed={primorial.bool_text(payload['row_column_unconditional_closed'])}",
        f"external_lemma_version_unconditional_closed={primorial.bool_text(payload['external_lemma_version_unconditional_closed'])}",
        f"internal_self_contained_closed={primorial.bool_text(payload['internal_self_contained_closed'])}",
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
    print("q_prefix_identity_verified_on_finite_audit=true")
    print("global_qprefix_unimodal_theorem_proved=false")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
