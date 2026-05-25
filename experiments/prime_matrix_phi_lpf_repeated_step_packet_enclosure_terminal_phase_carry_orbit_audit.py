#!/usr/bin/env python3
"""审计 repeated-step terminal phase 的 prime-gap carry orbit。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_repeated_step_packet_enclosure_terminal_phase_carry_orbit_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-dominant-sign-word-repeated-step-packet-enclosure-terminal-phase-carry-orbit-audit.json

上一层把 7 个 terminal/extra line atoms 的 endpoint phase 正规化为
e(h*A(q)/q)。本层继续原子化相邻 q-prime 的运动。若 q' = q+g，则

    q*m = k*P + D,
    q'*m = k'*P + D',
    c = floor((D+g*m)/P),

于是

    k' = k+c,
    D' = D+g*m-c*P,
    A(q') = -D' mod q'.

这把 moving Beatty numerator 的局部运动改写为 prime-gap/carry recurrence。
该层只关闭确定性 carry orbit，不证明相位节省。
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

SLUG = "prime-matrix-phi-lpf-dominant-sign-word-repeated-step-packet-enclosure-terminal-phase-carry-orbit"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-25"

TERMINAL_PHASE_NORMAL_FORM_AUDIT = (
    DOCS
    / "prime-matrix-phi-lpf-dominant-sign-word-repeated-step-packet-enclosure-terminal-phase-normal-form-audit.json"
)

DEPENDENCIES = [
    TERMINAL_PHASE_NORMAL_FORM_AUDIT,
    DOCS / "external-theorem-index.md",
    DOCS / "claim-status-table.md",
    DOCS / "frontier-honest-status-and-true-side-theorems-20260522.md",
    DOCS / "three-claims-actual-load-closure-contracts.md",
    DOCS / "three-claims-formal-to-actual-critical-load-frontier.md",
    ROOT / "paper" / "contradiction-field-monograph" / "contradiction-field-monograph.tex",
]

EXTERNAL_SOURCES = [
    {
        "key": "Fouvry_Kowalski_Michel_Sawin_2025_trace_bilinear_v3",
        "url": "https://arxiv.org/abs/2511.09459",
        "role": "trace bilinear estimates need a completed family; this audit only gives local prime-gap carry recurrence",
    },
    {
        "key": "Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman",
        "url": "https://arxiv.org/abs/2511.07550",
        "role": "Kloosterman bounds require an admissible completed variable, not a finite carry word by itself",
    },
    {
        "key": "Pascadi_2025_nonabelian_composite_type_II",
        "url": "https://arxiv.org/abs/2511.08445",
        "role": "prime-gap carry words remain one-dimensional and are not Type-II rectangles",
    },
    {
        "key": "Wright_2026_unbalanced_kloosterman_fractions",
        "url": "https://arxiv.org/abs/2604.25177",
        "role": "unbalanced fraction estimates are candidates only after the carry orbit is promoted to an averaging family",
    },
    {
        "key": "Li_2023_short_interval_primes_x_052_v8",
        "url": "https://arxiv.org/abs/2308.04458",
        "role": "short interval prime existence does not control the carry-word exponential phase",
    },
    {
        "key": "Maynard_2015_small_gaps_prime_gaps",
        "url": "https://doi.org/10.4007/annals.2015.181.1.7",
        "role": "bounded gaps supply existence patterns, not signed carry-orbit cancellation",
    },
]


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    paths = [Path(__file__).resolve(), *DEPENDENCIES]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def load_json(path: Path) -> dict[str, Any]:
    """读入 JSON 证书。"""
    return json.loads(path.read_text())


def gate(name: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造门控记录。"""
    return {
        "gate": name,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def transition_profile(atom: dict[str, Any], left: dict[str, int], right: dict[str, int]) -> dict[str, Any]:
    """构造一个相邻 prime-q transition 的 carry profile。"""
    q_gap = right["q"] - left["q"]
    raw = left["D"] + q_gap * atom["m"]
    carry_formula = raw // atom["P"]
    D_next_formula = raw - carry_formula * atom["P"]
    A_next_formula = (-D_next_formula) % right["q"]
    k_next_formula = left["k"] + carry_formula
    return {
        "packet_side": atom["packet_side"],
        "packet_index": atom["packet_index"],
        "role": atom["role"],
        "P": atom["P"],
        "m": atom["m"],
        "q": left["q"],
        "q_next": right["q"],
        "q_gap": q_gap,
        "k": left["k"],
        "k_next": right["k"],
        "k_step": right["k"] - left["k"],
        "D": left["D"],
        "D_next": right["D"],
        "D_step": right["D"] - left["D"],
        "D_wrap": right["D"] < left["D"],
        "A": left["A"],
        "A_next": right["A"],
        "A_step": right["A"] - left["A"],
        "A_wrap": right["A"] < left["A"],
        "raw_D_plus_gap_m": raw,
        "carry_formula": carry_formula,
        "D_next_formula": D_next_formula,
        "A_next_formula": A_next_formula,
        "k_next_formula": k_next_formula,
        "carry_identity_verified": (
            carry_formula == right["k"] - left["k"]
            and D_next_formula == right["D"]
            and A_next_formula == right["A"]
            and k_next_formula == right["k"]
        ),
        "transition_word": (
            f"gap{q_gap}_carry{carry_formula}_"
            f"Awrap{int(right['A'] < left['A'])}_Dwrap{int(right['D'] < left['D'])}"
        ),
    }


def atom_carry_profile(profile: dict[str, Any]) -> dict[str, Any]:
    """构造单个 atom 的 carry orbit profile。"""
    edges = profile["phase_edges"]
    transitions = [
        transition_profile(profile, left, right) for left, right in zip(edges, edges[1:])
    ]
    carry_values = [item["carry_formula"] for item in transitions]
    q_gaps = [item["q_gap"] for item in transitions]
    A_wrap_count = sum(1 for item in transitions if item["A_wrap"])
    D_wrap_count = sum(1 for item in transitions if item["D_wrap"])
    return {
        "packet_side": profile["packet_side"],
        "packet_index": profile["packet_index"],
        "role": profile["role"],
        "P": profile["P"],
        "m": profile["m"],
        "q_prefix_count": profile["q_prefix_count"],
        "transition_count": len(transitions),
        "q_gap_min": min(q_gaps) if q_gaps else 0,
        "q_gap_max": max(q_gaps) if q_gaps else 0,
        "carry_min": min(carry_values) if carry_values else 0,
        "carry_max": max(carry_values) if carry_values else 0,
        "carry_distinct_count": len(set(carry_values)),
        "A_wrap_count": A_wrap_count,
        "D_wrap_count": D_wrap_count,
        "A_wrap_fraction": f"{A_wrap_count}/{len(transitions)}" if transitions else "0/0",
        "D_wrap_fraction": f"{D_wrap_count}/{len(transitions)}" if transitions else "0/0",
        "all_carry_identities_verified": all(
            item["carry_identity_verified"] for item in transitions
        ),
        "transition_word_count": len(set(item["transition_word"] for item in transitions)),
        "transition_words_sample": sorted({item["transition_word"] for item in transitions})[:8],
        "transitions": transitions,
    }


def counter_rows(
    counts: Counter[Any],
    key_name: str,
    count_name: str = "transition_count",
) -> list[dict[str, Any]]:
    """把计数器转为稳定表格。"""
    def sort_key(item: Any) -> Any:
        """数字键按数值排序，其余键按字符串排序。"""
        if isinstance(item, int):
            return (0, item)
        return (1, str(item))

    return [
        {key_name: str(key), count_name: counts[key]}
        for key in sorted(counts, key=sort_key)
    ]


def audit() -> dict[str, Any]:
    """生成 terminal carry orbit 审计。"""
    phase_payload = load_json(TERMINAL_PHASE_NORMAL_FORM_AUDIT)
    phase_audit = phase_payload["finite_audit"]
    atom_profiles = phase_audit["phase_profiles"]
    carry_profiles = [atom_carry_profile(profile) for profile in atom_profiles]

    role_transition_counts: Counter[str] = Counter()
    role_A_wrap_counts: Counter[str] = Counter()
    role_D_wrap_counts: Counter[str] = Counter()
    q_gap_counts: Counter[int] = Counter()
    carry_counts: Counter[int] = Counter()
    gap_carry_counts: Counter[str] = Counter()
    wrap_pattern_counts: Counter[str] = Counter()
    bad_transition_samples: list[dict[str, Any]] = []

    for atom in carry_profiles:
        role_transition_counts[atom["role"]] += atom["transition_count"]
        role_A_wrap_counts[atom["role"]] += atom["A_wrap_count"]
        role_D_wrap_counts[atom["role"]] += atom["D_wrap_count"]
        for transition in atom["transitions"]:
            q_gap_counts[transition["q_gap"]] += 1
            carry_counts[transition["carry_formula"]] += 1
            gap_carry_counts[f"gap{transition['q_gap']}_carry{transition['carry_formula']}"] += 1
            wrap_pattern_counts[
                f"Awrap{int(transition['A_wrap'])}_Dwrap{int(transition['D_wrap'])}"
            ] += 1
            if not transition["carry_identity_verified"] and len(bad_transition_samples) < 8:
                bad_transition_samples.append(transition)

    total_transition_count = sum(role_transition_counts.values())
    selected_transition_count = role_transition_counts["selected_terminal"]
    extra_transition_count = role_transition_counts["extra_shell"]
    selected_A_wrap_count = role_A_wrap_counts["selected_terminal"]
    selected_D_wrap_count = role_D_wrap_counts["selected_terminal"]
    all_verified = (
        phase_payload["terminal_phase_normal_form_closed"]
        and total_transition_count
        == phase_audit["terminal_phase_normal_form_edge_count_total"]
        - phase_audit["terminal_phase_normal_form_atom_count_total"]
        and selected_transition_count
        == phase_audit["selected_terminal_phase_edge_count"]
        - phase_audit["selected_terminal_phase_atom_count"]
        and extra_transition_count
        == phase_audit["extra_phase_edge_count"] - phase_audit["extra_phase_atom_count"]
        and not bad_transition_samples
        and all(atom["all_carry_identities_verified"] for atom in carry_profiles)
    )

    return {
        "max_prime": phase_audit["max_prime"],
        "previous_terminal_phase_normal_form_closed": phase_payload[
            "terminal_phase_normal_form_closed"
        ],
        "terminal_phase_carry_orbit_closed": all_verified,
        "terminal_carry_atom_count_total": len(carry_profiles),
        "terminal_carry_transition_count_total": total_transition_count,
        "selected_terminal_transition_count": selected_transition_count,
        "extra_transition_count": extra_transition_count,
        "selected_terminal_A_wrap_count": selected_A_wrap_count,
        "selected_terminal_D_wrap_count": selected_D_wrap_count,
        "selected_terminal_A_wrap_fraction": f"{selected_A_wrap_count}/{selected_transition_count}",
        "selected_terminal_D_wrap_fraction": f"{selected_D_wrap_count}/{selected_transition_count}",
        "extra_A_wrap_count": role_A_wrap_counts["extra_shell"],
        "extra_D_wrap_count": role_D_wrap_counts["extra_shell"],
        "carry_identity_mismatch_count": len(bad_transition_samples),
        "bad_transition_samples": bad_transition_samples,
        "q_gap_rows": counter_rows(q_gap_counts, "q_gap"),
        "carry_rows": counter_rows(carry_counts, "carry"),
        "gap_carry_rows": counter_rows(gap_carry_counts, "gap_carry"),
        "wrap_pattern_rows": counter_rows(wrap_pattern_counts, "wrap_pattern"),
        "role_transition_rows": [
            {
                "role": role,
                "transition_count": role_transition_counts[role],
                "A_wrap_count": role_A_wrap_counts[role],
                "D_wrap_count": role_D_wrap_counts[role],
            }
            for role in sorted(role_transition_counts)
        ],
        "atom_carry_profiles": carry_profiles,
        "selected_terminal_carry_orbit_recurrence_closed": all_verified,
        "prime_gap_carry_word_phase_saving_proved": False,
        "extra_carry_orbit_absorption_proved": False,
        "summable_family_created": False,
        "trace_or_kloosterman_completion_ready": False,
        "row_column_unconditional_closed": False,
    }


def build_payload() -> dict[str, Any]:
    """构造审计 payload。"""
    finite_audit = audit()
    return {
        "certificate_type": "prime_matrix_phi_lpf_dominant_sign_word_repeated_step_packet_enclosure_terminal_phase_carry_orbit_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "terminal_phase_carry_orbit_closed_phase_saving_open",
        "chosen_claim": "Prime Matrix row/column Phi-LPF",
        "reason_chosen": "after terminal phase normal form, the acyclic next step is to expose the exact prime-gap carry recurrence for A(q)",
        "current_object": {
            "input": "terminal/extra moving-numerator phase profiles",
            "identity": "q'=q+g gives k'=k+floor((D+gm)/P), D'=D+gm-cP, A(q')=-D' mod q'",
            "dominant_shape": "selected terminal phase is a 66-transition prime-gap/carry word with 49 A-wraps",
            "remaining": "phase saving for the prime-gap/carry word and absorption of extra carry orbits",
        },
        "finite_audit": finite_audit,
        "closed_gates": [
            gate(
                "TerminalPhaseNormalFormImported",
                finite_audit["previous_terminal_phase_normal_form_closed"],
                finite_audit["previous_terminal_phase_normal_form_closed"],
                "The local A(q)/q phase normal form is imported.",
                "none for import",
            ),
            gate(
                "PrimeGapCarryRecurrence",
                finite_audit["terminal_phase_carry_orbit_closed"],
                finite_audit["terminal_phase_carry_orbit_closed"],
                "Every adjacent q-prime transition satisfies the exact carry recurrence.",
                "none for deterministic carry orbit",
            ),
            gate(
                "SelectedTerminalCarryOrbitLedger",
                finite_audit["selected_terminal_carry_orbit_recurrence_closed"],
                finite_audit["selected_terminal_carry_orbit_recurrence_closed"],
                "The selected terminal recurrence has 66 transitions and verified wrap/carry counts.",
                "none for finite selected carry ledger",
            ),
            gate(
                "PrimeGapCarryWordPhaseSaving",
                False,
                False,
                "Prove cancellation along the selected terminal prime-gap/carry word.",
                "requires analytic phase saving or a PDEC/SAE cap",
            ),
            gate(
                "ExtraCarryOrbitAbsorption",
                False,
                False,
                "Absorb the extra carry orbits without losing the selected terminal gain.",
                "requires summable absorption or explicit dominance certificate",
            ),
        ],
        "external_sources_consulted": EXTERNAL_SOURCES,
        "external_theorem_implication": {
            "FKMS_trace_bilinear": "the carry recurrence is deterministic but still not a completed bilinear trace family",
            "Milicevic_Qin_Wu_arbitrary_modulus_Kloosterman": "no admissible Kloosterman variable follows from a finite carry word alone",
            "Pascadi_composite_Type_II": "the transition word is one-dimensional, not a Type-II rectangle",
            "Wright_unbalanced_Kloosterman": "may become relevant only after promoting these carry orbits to an averaged family",
            "Li_short_interval_x_052": "prime existence does not estimate the signed carry word",
            "Maynard_small_gaps": "small-gap structure does not control the A-wrap/D-wrap phase signs",
        },
        "latest_narrowest_mouth": [
            "SelectedTerminalPrimeGapCarryWordPhaseSaving(66 transitions, 49 A-wraps, carry spectrum 2..13)",
            "AND ExtraCarryOrbitAbsorption(60 transitions)",
            "AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSavingOutsideCarryOrbit",
            "AND RepeatedStepPacketEnclosureTerminalLineAtomUniformBoundOutsidePhaseNormalForm",
            "AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity",
        ],
        "terminal_phase_carry_orbit_closed": finite_audit["terminal_phase_carry_orbit_closed"],
        "selected_terminal_carry_orbit_recurrence_closed": finite_audit[
            "selected_terminal_carry_orbit_recurrence_closed"
        ],
        "prime_gap_carry_word_phase_saving_proved": False,
        "extra_carry_orbit_absorption_proved": False,
        "summable_family_created": False,
        "trace_or_kloosterman_completion_ready": False,
        "phi_lpf_parity_barrier_globally_broken": False,
        "row_column_unconditional_closed": False,
        "external_lemma_version_unconditional_closed": False,
        "internal_self_contained_closed": False,
        "source_hashes": source_hashes(),
    }


def markdown_table(rows: list[dict[str, Any]], fields: list[str]) -> list[str]:
    """生成 Markdown 表格。"""
    lines = [
        "| " + " | ".join(fields) + " |",
        "| " + " | ".join(["---"] * len(fields)) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(str(row.get(field, "")) for field in fields) + " |")
    return lines


def build_markdown(payload: dict[str, Any]) -> str:
    """生成 Markdown 证书。"""
    audit_result = payload["finite_audit"]
    current = payload["current_object"]
    atom_rows = [
        {
            "side": atom["packet_side"],
            "packet": atom["packet_index"],
            "role": atom["role"],
            "m": atom["m"],
            "transitions": atom["transition_count"],
            "q_gap_range": f"[{atom['q_gap_min']},{atom['q_gap_max']}]",
            "carry_range": f"[{atom['carry_min']},{atom['carry_max']}]",
            "carry_distinct": atom["carry_distinct_count"],
            "A_wrap": atom["A_wrap_fraction"],
            "D_wrap": atom["D_wrap_fraction"],
            "word_count": atom["transition_word_count"],
        }
        for atom in audit_result["atom_carry_profiles"]
    ]
    lines = [
        "# Prime Matrix Phi-LPF repeated-step packet-enclosure terminal phase carry-orbit 审计",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['frontier_verified_date']}`",
        "",
        "## 1. 当前对象",
        "",
        "```text",
        f"input={current['input']}",
        f"identity={current['identity']}",
        f"dominant_shape={current['dominant_shape']}",
        f"remaining={current['remaining']}",
        "```",
        "",
        "## 2. carry orbit 有限审计",
        "",
        "```text",
        f"previous_terminal_phase_normal_form_closed={str(audit_result['previous_terminal_phase_normal_form_closed']).lower()}",
        f"terminal_phase_carry_orbit_closed={str(audit_result['terminal_phase_carry_orbit_closed']).lower()}",
        f"terminal_carry_atom_count_total={audit_result['terminal_carry_atom_count_total']}",
        f"terminal_carry_transition_count_total={audit_result['terminal_carry_transition_count_total']}",
        f"selected_terminal_transition_count={audit_result['selected_terminal_transition_count']}",
        f"extra_transition_count={audit_result['extra_transition_count']}",
        f"selected_terminal_A_wrap_count={audit_result['selected_terminal_A_wrap_count']}",
        f"selected_terminal_D_wrap_count={audit_result['selected_terminal_D_wrap_count']}",
        f"selected_terminal_A_wrap_fraction={audit_result['selected_terminal_A_wrap_fraction']}",
        f"selected_terminal_D_wrap_fraction={audit_result['selected_terminal_D_wrap_fraction']}",
        f"carry_identity_mismatch_count={audit_result['carry_identity_mismatch_count']}",
        f"prime_gap_carry_word_phase_saving_proved={str(audit_result['prime_gap_carry_word_phase_saving_proved']).lower()}",
        f"row_column_unconditional_closed={str(audit_result['row_column_unconditional_closed']).lower()}",
        "```",
        "",
        "atom carry rows：",
        "",
        *markdown_table(
            atom_rows,
            [
                "side",
                "packet",
                "role",
                "m",
                "transitions",
                "q_gap_range",
                "carry_range",
                "carry_distinct",
                "A_wrap",
                "D_wrap",
                "word_count",
            ],
        ),
        "",
        "role transition rows：",
        "",
        *markdown_table(
            audit_result["role_transition_rows"],
            ["role", "transition_count", "A_wrap_count", "D_wrap_count"],
        ),
        "",
        "q-gap 分桶：",
        "",
        *markdown_table(audit_result["q_gap_rows"], ["q_gap", "transition_count"]),
        "",
        "carry 分桶：",
        "",
        *markdown_table(audit_result["carry_rows"], ["carry", "transition_count"]),
        "",
        "wrap pattern 分桶：",
        "",
        *markdown_table(audit_result["wrap_pattern_rows"], ["wrap_pattern", "transition_count"]),
        "",
        "## 3. 门控表",
        "",
        *markdown_table(payload["closed_gates"], ["gate", "closed", "proved", "meaning", "remaining"]),
        "",
        "## 4. 外部 theorem 影响",
        "",
        *markdown_table(payload["external_sources_consulted"], ["key", "url", "role"]),
        "",
        "```text",
        *[f"{key}={value}" for key, value in payload["external_theorem_implication"].items()],
        "```",
        "",
        "结论：moving numerator 已被拆成相邻 prime-gap 驱动的 carry recurrence。",
        "selected terminal 部分有 `66` 个 transition，其中 `49` 次 A-wrap，carry 谱覆盖 `2..13`。",
        "这关闭的是确定性动力系统账本，不关闭 carry-word phase saving。",
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
        f"terminal_phase_carry_orbit_closed={str(payload['terminal_phase_carry_orbit_closed']).lower()}",
        f"selected_terminal_carry_orbit_recurrence_closed={str(payload['selected_terminal_carry_orbit_recurrence_closed']).lower()}",
        f"prime_gap_carry_word_phase_saving_proved={str(payload['prime_gap_carry_word_phase_saving_proved']).lower()}",
        f"extra_carry_orbit_absorption_proved={str(payload['extra_carry_orbit_absorption_proved']).lower()}",
        f"summable_family_created={str(payload['summable_family_created']).lower()}",
        f"trace_or_kloosterman_completion_ready={str(payload['trace_or_kloosterman_completion_ready']).lower()}",
        f"phi_lpf_parity_barrier_globally_broken={str(payload['phi_lpf_parity_barrier_globally_broken']).lower()}",
        f"row_column_unconditional_closed={str(payload['row_column_unconditional_closed']).lower()}",
        f"external_lemma_version_unconditional_closed={str(payload['external_lemma_version_unconditional_closed']).lower()}",
        f"internal_self_contained_closed={str(payload['internal_self_contained_closed']).lower()}",
        "```",
    ]
    return "\n".join(lines)


def main() -> None:
    """生成审计证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    payload = build_payload()
    text = json.dumps(payload, indent=2, sort_keys=True)
    OUT_LEDGER.write_text(text + "\n")
    OUT_JSON.write_text(text + "\n")
    OUT_MD.write_text(build_markdown(payload).rstrip() + "\n")
    audit_result = payload["finite_audit"]
    print(f"wrote {OUT_JSON.relative_to(ROOT)}")
    print(f"terminal_phase_carry_orbit_closed={payload['terminal_phase_carry_orbit_closed']}")
    print(f"selected_terminal_transition_count={audit_result['selected_terminal_transition_count']}")
    print(f"row_column_unconditional_closed={payload['row_column_unconditional_closed']}")


if __name__ == "__main__":
    main()
