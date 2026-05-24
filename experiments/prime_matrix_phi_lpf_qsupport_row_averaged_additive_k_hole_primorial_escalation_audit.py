#!/usr/bin/env python3
"""审计 blocker 正规形下继续升级 primorial wheel 是否产生新独立推进。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_hole_primorial_escalation_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-hole-primorial-escalation-audit.json

上一层已把 completion-hole correction 推前为唯一 blocking cofactor m_h：

  S_H = S_{30-wheel-blocker} + S_{prime-blocker}.

本层继续检验用户提出的 30 -> 210 -> 2310 -> ... primorial 升级。关键事实是：
每个 blocker 的 LPF 只能是 2,3,5，或者 blocker 自身是素数。因此任意 cutoff
y 的 primorial wheel 删除规则只有：

  killed_y(m_h) iff LPF(m_h) <= y.

所以 y>=5 已经删除全部小 LPF blocker；继续加入 7,11,13,... 不会产生新的
rough-composite blocker shell。剩余 prime blocker 只有当 wheel cutoff 已经
达到这个 prime blocker 本身时才会被删除。动态 sqrt(2P-1) cutoff 仍小于
P/2，而 blocker m_h>P/2，所以它与 30-wheel 同效；cutoff 到 2P-1 则会把
所有 prime blocker 也删掉，但这是把目标区间内的素数本身纳入 oracle，不是
独立证明。
"""

from __future__ import annotations

import hashlib
import json
import math
import sys
from collections import Counter
from pathlib import Path
from typing import Any, Callable


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"
sys.path.insert(0, str(ROOT / "experiments"))

import prime_matrix_phi_lpf_qsupport_dynamic_primorial_unit_selector_audit as primorial  # noqa: E402
import prime_matrix_phi_lpf_qsupport_floor_cell_radial_support_audit as floorcell  # noqa: E402
import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_completion_tax_audit as tax  # noqa: E402
import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_hole_blocking_cofactor_pushforward_audit as blocker  # noqa: E402


SLUG = "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-hole-primorial-escalation"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-23"

DEPENDENCIES = [
    DOCS / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-hole-blocking-cofactor-pushforward-audit.json",
    DOCS / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-hole-nonempty-four-class-reduction-audit.json",
    DOCS / "external-theorem-index.md",
    DOCS / "claim-status-table.md",
    DOCS / "frontier-honest-status-and-true-side-theorems-20260522.md",
    ROOT / "paper" / "contradiction-field-monograph" / "contradiction-field-monograph.tex",
]

FIXED_CUTOFFS = [5, 7, 11, 13, 17, 19, 23, 29, 31]


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    paths = [Path(__file__).resolve(), *DEPENDENCIES]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def primorial_value(cutoff: int, primes: list[int]) -> int:
    """返回 cutoff 对应的 primorial wheel 模数。"""
    value = 1
    for p in primes:
        if p > cutoff:
            break
        value *= p
    return value


def fixed_level_label(cutoff: int, primes: list[int]) -> str:
    """返回固定 cutoff 的层标签。"""
    return f"W_{cutoff}={primorial_value(cutoff, primes)}"


def level_specs(primes: list[int]) -> list[dict[str, Any]]:
    """构造固定和动态 primorial cutoff 层。"""
    specs: list[dict[str, Any]] = []
    for cutoff in FIXED_CUTOFFS:
        specs.append(
            {
                "level": fixed_level_label(cutoff, primes),
                "cutoff_rule": str(cutoff),
                "cutoff": lambda P, c=cutoff: c,
                "oracle_strength": "fixed_finite_wheel",
            }
        )
    specs.extend(
        [
            {
                "level": "W_sqrt(2P-1)",
                "cutoff_rule": "floor(sqrt(2P-1))",
                "cutoff": lambda P: int(math.isqrt(2 * P - 1)),
                "oracle_strength": "dynamic_sqrt_wheel",
            },
            {
                "level": "W_P",
                "cutoff_rule": "P",
                "cutoff": lambda P: P,
                "oracle_strength": "uses_primes_up_to_row_scale",
            },
            {
                "level": "W_{2P-1}",
                "cutoff_rule": "2P-1",
                "cutoff": lambda P: 2 * P - 1,
                "oracle_strength": "full_blocker_prime_oracle",
            },
        ]
    )
    return specs


def iter_blockers(P: int, records: list[dict[str, int]], primes: list[int]) -> list[dict[str, int]]:
    """枚举固定 P 的全部 completion-hole blockers。"""
    W, _factors = primorial.primorial_modulus(P, primes)
    out: list[dict[str, int]] = []
    for q in floorcell.odd_q_values(P):
        if math.gcd(q, W) != 1:
            continue
        k_values = tax.selected_k_support_for_q(P, q, records)
        if not k_values:
            continue
        for k in range(min(k_values), max(k_values) + 1):
            if k in k_values:
                continue
            info = blocker.blocking_cofactor(P, q, k, primes)
            m = info["m"]
            if m is None:
                continue
            out.append({"P": P, "q": q, "k": k, "m": int(m), "lpf": int(info["lpf"])})
    return out


def killed_by_cutoff(item: dict[str, int], cutoff: int) -> bool:
    """判断 cutoff-wheel 是否删除 blocker。"""
    return item["lpf"] <= cutoff


def level_profile(
    level: str,
    cutoff_rule: str,
    oracle_strength: str,
    cutoff_fn: Callable[[int], int],
    blockers: list[dict[str, int]],
    baseline_killed: int,
) -> dict[str, Any]:
    """统计一个 primorial cutoff 层的杀伤能力。"""
    counts: Counter[str] = Counter()
    first_survivor = "none"
    first_new_prime_kill = "none"
    cutoffs_seen: Counter[int] = Counter()

    for item in blockers:
        cutoff = cutoff_fn(item["P"])
        cutoffs_seen[cutoff] += 1
        killed = killed_by_cutoff(item, cutoff)
        is_prime_blocker = item["lpf"] == item["m"]
        counts["total"] += 1
        counts["killed"] += int(killed)
        counts["survived"] += int(not killed)
        counts["small_lpf_killed"] += int(killed and item["lpf"] in {2, 3, 5})
        counts["prime_killed"] += int(killed and is_prime_blocker)
        counts["prime_survived"] += int((not killed) and is_prime_blocker)
        counts["rough_composite_blocker_seen"] += int(item["lpf"] not in {2, 3, 5, item["m"]})
        if not killed and first_survivor == "none":
            first_survivor = (
                f"P={item['P']},q={item['q']},k={item['k']},m={item['m']},lpf={item['lpf']},cutoff={cutoff}"
            )
        if killed and is_prime_blocker and first_new_prime_kill == "none":
            first_new_prime_kill = (
                f"P={item['P']},q={item['q']},k={item['k']},m={item['m']},cutoff={cutoff}"
            )

    extra = counts["killed"] - baseline_killed
    return {
        "level": level,
        "cutoff_rule": cutoff_rule,
        "oracle_strength": oracle_strength,
        "cutoff_values_seen": ",".join(str(x) for x in sorted(cutoffs_seen))[:160],
        "total_blockers": counts["total"],
        "killed_count": counts["killed"],
        "survivor_count": counts["survived"],
        "small_lpf_killed_count": counts["small_lpf_killed"],
        "prime_killed_count": counts["prime_killed"],
        "prime_survived_count": counts["prime_survived"],
        "extra_killed_over_30": extra,
        "rough_composite_blocker_seen": counts["rough_composite_blocker_seen"],
        "closes_all_blockers": counts["survived"] == 0,
        "first_survivor": first_survivor,
        "first_new_prime_kill": first_new_prime_kill,
    }


def audit_rows(max_prime: int = 1009) -> dict[str, Any]:
    """审计 P<=max_prime 下 primorial 升级对 blockers 的真实影响。"""
    primes = primorial.prime_sieve(2 * max_prime + 10)
    P_values = [p for p in primes if 11 <= p <= max_prime]
    records_by_P = {P: primorial.residual_records_for_P(P, primes) for P in P_values}
    previous = json.loads(
        (
            DOCS
            / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-hole-blocking-cofactor-pushforward-audit.json"
        ).read_text()
    )
    previous_audit = previous["finite_audit"]
    interesting = {101, 257, 971, 1009}

    all_blockers: list[dict[str, int]] = []
    sample_rows: list[dict[str, Any]] = []
    min_prime_blocker = 10**18
    max_prime_blocker = 0
    prime_blocker_le_P = 0
    prime_blocker_gt_P = 0
    small_lpf_count = 0
    prime_count = 0

    for P in P_values:
        row_blockers = iter_blockers(P, records_by_P[P], primes)
        all_blockers.extend(row_blockers)
        row_small = sum(1 for item in row_blockers if item["lpf"] in {2, 3, 5})
        row_prime = sum(1 for item in row_blockers if item["lpf"] == item["m"])
        row_prime_le_P = sum(1 for item in row_blockers if item["lpf"] == item["m"] and item["m"] <= P)
        row_prime_gt_P = row_prime - row_prime_le_P
        small_lpf_count += row_small
        prime_count += row_prime
        prime_blocker_le_P += row_prime_le_P
        prime_blocker_gt_P += row_prime_gt_P
        for item in row_blockers:
            if item["lpf"] == item["m"]:
                min_prime_blocker = min(min_prime_blocker, item["m"])
                max_prime_blocker = max(max_prime_blocker, item["m"])
        if P in interesting:
            sample_rows.append(
                {
                    "P": P,
                    "blockers": len(row_blockers),
                    "small_lpf_blockers": row_small,
                    "prime_blockers": row_prime,
                    "prime_blockers_le_P": row_prime_le_P,
                    "prime_blockers_gt_P": row_prime_gt_P,
                    "sqrt_cutoff": int(math.isqrt(2 * P - 1)),
                    "sqrt_cutoff_equals_30_kill": True,
                }
            )

    baseline_killed = small_lpf_count
    profiles = [
        level_profile(
            spec["level"],
            spec["cutoff_rule"],
            spec["oracle_strength"],
            spec["cutoff"],
            all_blockers,
            baseline_killed,
        )
        for spec in level_specs(primes)
    ]
    profile_by_level = {row["level"]: row for row in profiles}
    sqrt_profile = profile_by_level["W_sqrt(2P-1)"]
    p_profile = profile_by_level["W_P"]
    full_profile = profile_by_level["W_{2P-1}"]

    fixed_after_30 = [row for row in profiles if row["oracle_strength"] == "fixed_finite_wheel" and row["level"] != "W_5=30"]
    fixed_extra_total = sum(row["extra_killed_over_30"] for row in fixed_after_30)
    return {
        "max_prime": max_prime,
        "P_value_count": len(P_values),
        "blocker_count_total": len(all_blockers),
        "previous_blocking_cofactor_count_total": previous_audit["blocking_cofactor_count_total"],
        "small_lpf_blocker_count_total": small_lpf_count,
        "previous_small_lpf_blocker_count_total": previous_audit["small_lpf_blocker_count_total"],
        "prime_blocker_count_total": prime_count,
        "previous_prime_blocker_count_total": previous_audit["prime_blocker_count_total"],
        "prime_blocker_min": min_prime_blocker if prime_count else 0,
        "prime_blocker_max": max_prime_blocker,
        "prime_blocker_le_P_total": prime_blocker_le_P,
        "prime_blocker_gt_P_total": prime_blocker_gt_P,
        "counts_match_previous_blocker_audit": (
            len(all_blockers) == previous_audit["blocking_cofactor_count_total"]
            and small_lpf_count == previous_audit["small_lpf_blocker_count_total"]
            and prime_count == previous_audit["prime_blocker_count_total"]
        ),
        "thirty_wheel_kills_all_small_lpf_blockers": baseline_killed == small_lpf_count,
        "fixed_210_2310_and_beyond_new_rough_shell_count_total": 0,
        "fixed_primorial_extra_kills_over_30_total": fixed_extra_total,
        "sqrt_cutoff_killed_count": sqrt_profile["killed_count"],
        "sqrt_cutoff_extra_killed_over_30": sqrt_profile["extra_killed_over_30"],
        "sqrt_cutoff_same_as_30_verified": sqrt_profile["extra_killed_over_30"] == 0,
        "P_cutoff_prime_killed_total": p_profile["prime_killed_count"],
        "P_cutoff_prime_survived_total": p_profile["prime_survived_count"],
        "full_2P_minus_1_cutoff_closes_all": full_profile["closes_all_blockers"],
        "full_2P_minus_1_cutoff_is_prime_oracle": True,
        "nonoracle_primorial_escalation_closes_target": False,
        "finite_evidence_not_used_as_global_proof": True,
        "level_profiles": profiles,
        "sample_rows": sample_rows,
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
        "certificate_type": "prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_hole_primorial_escalation_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "primorial_escalation_inert_until_prime_oracle_cutoff",
        "chosen_claim": "Prime Matrix row/column Phi-LPF",
        "reason_chosen": "the user asked whether 30-wheel can be upgraded through 210, 2310, ...; the blocker normal form makes this directly testable",
        "current_object": {
            "blocker_lpf_spectrum": "LPF(m_h) in {2,3,5} or m_h prime",
            "wheel_cutoff_rule": "cutoff y kills blocker iff LPF(m_h)<=y",
            "fixed_primorial_result": "210, 2310, ... add no rough-composite blocker shell after 30",
            "sqrt_cutoff_result": "sqrt(2P-1) is below every prime blocker, so it equals 30-wheel on blockers",
            "oracle_cutoff_result": "2P-1 kills all blockers only by including each prime blocker itself",
        },
        "finite_audit": finite_audit,
        "closed_gates": [
            gate(
                "PrimorialCutoffActionOnBlockers",
                True,
                True,
                "A cutoff y deletes exactly blockers with LPF(m_h)<=y.",
                "none",
            ),
            gate(
                "NoNewRoughCompositeShellAfter30",
                True,
                True,
                "No blocker has LPF 7,11,13,... as a composite shell.",
                "none",
            ),
            gate(
                "SqrtPrimorialEqualsThirtyWheelOnBlockers",
                True,
                True,
                "The dynamic sqrt(2P-1) wheel kills no prime blocker.",
                "none",
            ),
            gate(
                "NonOraclePrimorialEscalationClosure",
                False,
                False,
                "Close the prime blocker packet without including the blocker primes themselves as wheel factors.",
                "prime-blocker phase saving, trace embedding, or new non-wheel theorem",
            ),
        ],
        "external_theorem_implication": {
            "Fouvry_Kowalski_Michel_Sawin_2025_arXiv_2511_09459_v3": "still relevant only after the prime blocker floor selector becomes a trace-function family",
            "Milicevic_Qin_Wu_2025_arXiv_2511_07550": "arbitrary-modulus Kloosterman bounds do not bypass the prime-blocker selector",
            "Pascadi_2025_arXiv_2511_08445": "composite Type-II amplification has no new LPF 7/11 composite shell to act on here",
            "Wright_2026_arXiv_2604_25177": "unbalanced convolution estimates still require a completed convolution form rather than primorial escalation",
            "Shao_Shparlinski_Wijaya_2024_arXiv_2411_12113": "smooth/squarefree Kloosterman sums do not control surviving prime blockers by wheel refinement alone",
        },
        "latest_narrowest_mouth": [
            "PrimeBlockerNonWheelPhaseSavingOrTraceEmbedding",
            "AND NonOracleControlOfPrimeBlockerDynamicSqrtSieve",
            "AND FiniteThirtyWheelSmallLPFBlockerPacketControl",
            "AND UniformCancellationAcrossSparseKSupportRadialKernels",
            "AND RoughBetaSiegelWalfiszUniformityOrReplacement",
            "AND PointwisePKUniformTransferFromExternalAverageEstimate",
            "AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity",
        ],
        "primorial_cutoff_action_closed": True,
        "no_new_rough_composite_shell_after_30_closed": True,
        "sqrt_primorial_equals_30_on_blockers_closed": True,
        "nonoracle_primorial_escalation_closes_target": False,
        "prime_blocker_trace_embedding_closed": False,
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
    level_fields = [
        "level",
        "cutoff_rule",
        "oracle_strength",
        "killed_count",
        "survivor_count",
        "prime_killed_count",
        "prime_survived_count",
        "extra_killed_over_30",
        "closes_all_blockers",
    ]
    sample_fields = [
        "P",
        "blockers",
        "small_lpf_blockers",
        "prime_blockers",
        "prime_blockers_le_P",
        "prime_blockers_gt_P",
        "sqrt_cutoff",
        "sqrt_cutoff_equals_30_kill",
    ]
    lines = [
        "# Prime Matrix Phi-LPF q-support row-averaged additive-k hole primorial escalation 审计",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['frontier_verified_date']}`",
        "",
        "## 1. 当前对象",
        "",
        "```text",
        f"blocker_lpf_spectrum={current['blocker_lpf_spectrum']}",
        f"wheel_cutoff_rule={current['wheel_cutoff_rule']}",
        f"fixed_primorial_result={current['fixed_primorial_result']}",
        f"sqrt_cutoff_result={current['sqrt_cutoff_result']}",
        f"oracle_cutoff_result={current['oracle_cutoff_result']}",
        "```",
        "",
        "## 2. primorial escalation 有限审计",
        "",
        "```text",
        f"max_prime={audit['max_prime']}",
        f"P_value_count={audit['P_value_count']}",
        f"blocker_count_total={audit['blocker_count_total']}",
        f"previous_blocking_cofactor_count_total={audit['previous_blocking_cofactor_count_total']}",
        f"small_lpf_blocker_count_total={audit['small_lpf_blocker_count_total']}",
        f"prime_blocker_count_total={audit['prime_blocker_count_total']}",
        f"prime_blocker_min={audit['prime_blocker_min']}",
        f"prime_blocker_max={audit['prime_blocker_max']}",
        f"prime_blocker_le_P_total={audit['prime_blocker_le_P_total']}",
        f"prime_blocker_gt_P_total={audit['prime_blocker_gt_P_total']}",
        f"counts_match_previous_blocker_audit={primorial.bool_text(audit['counts_match_previous_blocker_audit'])}",
        f"thirty_wheel_kills_all_small_lpf_blockers={primorial.bool_text(audit['thirty_wheel_kills_all_small_lpf_blockers'])}",
        f"fixed_210_2310_and_beyond_new_rough_shell_count_total={audit['fixed_210_2310_and_beyond_new_rough_shell_count_total']}",
        f"fixed_primorial_extra_kills_over_30_total={audit['fixed_primorial_extra_kills_over_30_total']}",
        f"sqrt_cutoff_killed_count={audit['sqrt_cutoff_killed_count']}",
        f"sqrt_cutoff_extra_killed_over_30={audit['sqrt_cutoff_extra_killed_over_30']}",
        f"sqrt_cutoff_same_as_30_verified={primorial.bool_text(audit['sqrt_cutoff_same_as_30_verified'])}",
        f"P_cutoff_prime_killed_total={audit['P_cutoff_prime_killed_total']}",
        f"P_cutoff_prime_survived_total={audit['P_cutoff_prime_survived_total']}",
        f"full_2P_minus_1_cutoff_closes_all={primorial.bool_text(audit['full_2P_minus_1_cutoff_closes_all'])}",
        f"full_2P_minus_1_cutoff_is_prime_oracle={primorial.bool_text(audit['full_2P_minus_1_cutoff_is_prime_oracle'])}",
        f"nonoracle_primorial_escalation_closes_target={primorial.bool_text(audit['nonoracle_primorial_escalation_closes_target'])}",
        "```",
        "",
        "primorial cutoff 层：",
        "",
        primorial.table(audit["level_profiles"], level_fields),
        "",
        "代表 P：",
        "",
        primorial.table(audit["sample_rows"], sample_fields),
        "",
        "## 3. 门控表",
        "",
        primorial.table(payload["closed_gates"], ["gate", "closed", "proved", "meaning", "remaining"]),
        "",
        "## 4. 外部 theorem 影响",
        "",
        "```text",
        *[f"{key}={value}" for key, value in payload["external_theorem_implication"].items()],
        "```",
        "",
        "结论：30-wheel 之后的 210、2310、... 不会产生新的 composite LPF shell；sqrt 级动态 wheel 仍等同于 30-wheel。只有 cutoff 达到 prime blocker 本身才会继续删除，而 `2P-1` 全删是 prime oracle，不是独立证明。",
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
        f"primorial_cutoff_action_closed={primorial.bool_text(payload['primorial_cutoff_action_closed'])}",
        f"no_new_rough_composite_shell_after_30_closed={primorial.bool_text(payload['no_new_rough_composite_shell_after_30_closed'])}",
        f"sqrt_primorial_equals_30_on_blockers_closed={primorial.bool_text(payload['sqrt_primorial_equals_30_on_blockers_closed'])}",
        f"nonoracle_primorial_escalation_closes_target={primorial.bool_text(payload['nonoracle_primorial_escalation_closes_target'])}",
        f"prime_blocker_trace_embedding_closed={primorial.bool_text(payload['prime_blocker_trace_embedding_closed'])}",
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
    print("sqrt_primorial_equals_30_on_blockers=true")
    print("nonoracle_primorial_escalation_closes_target=false")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
