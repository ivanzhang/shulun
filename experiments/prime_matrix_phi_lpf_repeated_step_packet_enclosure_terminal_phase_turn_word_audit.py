#!/usr/bin/env python3
"""审计 repeated-step terminal carry orbit 的 phase-turn word。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_repeated_step_packet_enclosure_terminal_phase_turn_word_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-dominant-sign-word-repeated-step-packet-enclosure-terminal-phase-turn-word-audit.json

上一层已经证明相邻 prime-q 转移满足 carry recurrence。本层继续检查
A(q)/q 的真实相位方向，并把每个 atom 分解成单调 phase runs。
该层只关闭有限 phase-turn ledger，不证明相位节省。
"""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from fractions import Fraction
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = (
    "prime-matrix-phi-lpf-dominant-sign-word-repeated-step-packet-enclosure-"
    "terminal-phase-turn-word"
)
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-25"

CARRY_ORBIT_AUDIT = (
    DOCS
    / "prime-matrix-phi-lpf-dominant-sign-word-repeated-step-packet-enclosure-terminal-phase-carry-orbit-audit.json"
)

DEPENDENCIES = [
    CARRY_ORBIT_AUDIT,
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
        "role": "trace bilinear estimates require a completed averaging family, not a finite phase-turn word",
    },
    {
        "key": "Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman",
        "url": "https://arxiv.org/abs/2511.07550",
        "role": "arbitrary-modulus Kloosterman bounds need an admissible summation variable",
    },
    {
        "key": "Pascadi_2025_nonabelian_composite_type_II",
        "url": "https://arxiv.org/abs/2511.08445",
        "role": "the phase-turn word is not a composite Type-II rectangle",
    },
    {
        "key": "Wright_2026_unbalanced_kloosterman_fractions",
        "url": "https://arxiv.org/abs/2604.25177",
        "role": "unbalanced fraction bounds may help only after a trilinear or averaged fraction family is built",
    },
    {
        "key": "Li_2023_short_interval_primes_x_052_v8",
        "url": "https://arxiv.org/abs/2308.04458",
        "role": "short-interval prime existence does not estimate signed A-wrap phase turns",
    },
    {
        "key": "Maynard_2015_small_gaps_prime_gaps",
        "url": "https://doi.org/10.4007/annals.2015.181.1.7",
        "role": "bounded prime gaps do not control the signed phase-turn run imbalance",
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


def counter_rows(counts: Counter[Any], key_name: str, count_name: str = "count") -> list[dict[str, Any]]:
    """把计数器转为稳定表格。"""

    def sort_key(item: Any) -> Any:
        if isinstance(item, tuple):
            return tuple(str(part) for part in item)
        if isinstance(item, int):
            return (0, item)
        return (1, str(item))

    return [
        {key_name: str(key), count_name: counts[key]}
        for key in sorted(counts, key=sort_key)
    ]


def lifted_edge(edge: dict[str, int]) -> dict[str, Any]:
    """给 phase edge 增加两层 lift 表示。"""
    q = edge["q"]
    D = edge["D"]
    lift = (D + q - 1) // q
    return {
        **edge,
        "lift": lift,
        "lift_identity_verified": lift in {1, 2} and lift * q - D == edge["A"],
        "phase_fraction": f"{edge['A']}/{q}",
    }


def phase_direction(delta: Fraction) -> str:
    """返回相位差分方向。"""
    if delta > 0:
        return "positive"
    if delta < 0:
        return "negative"
    return "zero"


def phase_run_rows(transitions: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """按相位方向分解为最大连续 runs。"""
    if not transitions:
        return []
    rows: list[dict[str, Any]] = []
    start = 0
    for index in range(1, len(transitions)):
        if transitions[index]["phase_direction"] != transitions[start]["phase_direction"]:
            rows.append(phase_run_row(transitions, start, index - 1, len(rows)))
            start = index
    rows.append(phase_run_row(transitions, start, len(transitions) - 1, len(rows)))
    return rows


def phase_run_row(
    transitions: list[dict[str, Any]],
    start: int,
    end: int,
    run_id: int,
) -> dict[str, Any]:
    """构造一个 phase run 行。"""
    segment = transitions[start : end + 1]
    carries = [item["carry_formula"] for item in segment]
    q_gaps = [item["q_gap"] for item in segment]
    return {
        "run_id": run_id,
        "direction": segment[0]["phase_direction"],
        "start_transition_index": start,
        "end_transition_index": end,
        "length": len(segment),
        "q_start": segment[0]["q"],
        "q_end": segment[-1]["q_next"],
        "carry_min": min(carries),
        "carry_max": max(carries),
        "q_gap_min": min(q_gaps),
        "q_gap_max": max(q_gaps),
        "A_wrap_count": sum(1 for item in segment if item["A_wrap"]),
        "D_wrap_count": sum(1 for item in segment if item["D_wrap"]),
    }


def atom_phase_turn_profile(atom: dict[str, Any]) -> dict[str, Any]:
    """构造单个 atom 的 phase-turn profile。"""
    transitions = atom["transitions"]
    if not transitions:
        return {
            "packet_side": atom["packet_side"],
            "packet_index": atom["packet_index"],
            "role": atom["role"],
            "P": atom["P"],
            "m": atom["m"],
            "phase_turn_transition_count": 0,
            "phase_run_count": 0,
            "phase_runs": [],
            "phase_turn_transitions": [],
        }

    edges = [
        lifted_edge(
            {
                "q": transitions[0]["q"],
                "A": transitions[0]["A"],
                "D": transitions[0]["D"],
                "k": transitions[0]["k"],
            }
        )
    ]
    for item in transitions:
        edges.append(
            lifted_edge(
                {
                    "q": item["q_next"],
                    "A": item["A_next"],
                    "D": item["D_next"],
                    "k": item["k_next"],
                }
            )
        )

    phase_turns: list[dict[str, Any]] = []
    for index, (left, right, carry) in enumerate(zip(edges, edges[1:], transitions)):
        delta = Fraction(right["A"], right["q"]) - Fraction(left["A"], left["q"])
        direction = phase_direction(delta)
        phase_turns.append(
            {
                "transition_index": index,
                "q": left["q"],
                "q_next": right["q"],
                "q_gap": carry["q_gap"],
                "carry_formula": carry["carry_formula"],
                "A": left["A"],
                "A_next": right["A"],
                "A_wrap": carry["A_wrap"],
                "D": left["D"],
                "D_next": right["D"],
                "D_wrap": carry["D_wrap"],
                "lift": left["lift"],
                "lift_next": right["lift"],
                "lift_step": right["lift"] - left["lift"],
                "phase_delta_num": delta.numerator,
                "phase_delta_den": delta.denominator,
                "phase_direction": direction,
                "phase_direction_matches_A_wrap": (
                    (direction == "negative" and carry["A_wrap"])
                    or (direction == "positive" and not carry["A_wrap"])
                ),
                "zero_phase_delta": direction == "zero",
                "lift_identities_verified": left["lift_identity_verified"]
                and right["lift_identity_verified"],
                "phase_turn_word": (
                    f"{direction}_Awrap{int(carry['A_wrap'])}_"
                    f"Dwrap{int(carry['D_wrap'])}_L{left['lift']}to{right['lift']}_"
                    f"gap{carry['q_gap']}_carry{carry['carry_formula']}"
                ),
            }
        )

    runs = phase_run_rows(phase_turns)
    direction_counts = Counter(item["phase_direction"] for item in phase_turns)
    lift_counts = Counter(edge["lift"] for edge in edges)
    lift_transition_counts = Counter(
        f"L{item['lift']}to{item['lift_next']}_{item['phase_direction']}"
        for item in phase_turns
    )
    return {
        "packet_side": atom["packet_side"],
        "packet_index": atom["packet_index"],
        "role": atom["role"],
        "P": atom["P"],
        "m": atom["m"],
        "q_prefix_count": atom["q_prefix_count"],
        "phase_turn_transition_count": len(phase_turns),
        "phase_positive_transition_count": direction_counts["positive"],
        "phase_negative_transition_count": direction_counts["negative"],
        "phase_zero_transition_count": direction_counts["zero"],
        "phase_run_count": len(runs),
        "phase_run_max_length": max((row["length"] for row in runs), default=0),
        "phase_run_rows": runs,
        "lift_1_edge_count": lift_counts[1],
        "lift_2_edge_count": lift_counts[2],
        "lift_other_edge_count": sum(
            count for lift, count in lift_counts.items() if lift not in {1, 2}
        ),
        "lift_transition_rows": counter_rows(
            lift_transition_counts, "lift_transition", "transition_count"
        ),
        "phase_direction_Awrap_mismatch_count": sum(
            1 for item in phase_turns if not item["phase_direction_matches_A_wrap"]
        ),
        "lift_identity_mismatch_count": sum(
            1 for item in phase_turns if not item["lift_identities_verified"]
        ),
        "phase_turn_word_count": len(set(item["phase_turn_word"] for item in phase_turns)),
        "phase_turn_words_sample": sorted(
            {item["phase_turn_word"] for item in phase_turns}
        )[:10],
        "phase_turn_transitions": phase_turns,
    }


def audit() -> dict[str, Any]:
    """生成 phase-turn word 审计。"""
    carry_payload = load_json(CARRY_ORBIT_AUDIT)
    carry_audit = carry_payload["finite_audit"]
    profiles = [
        atom_phase_turn_profile(atom) for atom in carry_audit["atom_carry_profiles"]
    ]

    role_direction_counts: Counter[tuple[str, str]] = Counter()
    role_run_counts: Counter[str] = Counter()
    role_max_run: Counter[str] = Counter()
    role_lift_counts: Counter[tuple[str, str]] = Counter()
    role_lift_transition_counts: Counter[tuple[str, str]] = Counter()
    turn_word_counts: Counter[str] = Counter()

    direction_mismatch_count = 0
    lift_mismatch_count = 0
    zero_phase_delta_count = 0
    total_transition_count = 0
    total_run_count = 0

    for profile in profiles:
        role = profile["role"]
        total_transition_count += profile["phase_turn_transition_count"]
        total_run_count += profile["phase_run_count"]
        role_run_counts[role] += profile["phase_run_count"]
        role_max_run[role] = max(role_max_run[role], profile["phase_run_max_length"])
        direction_mismatch_count += profile["phase_direction_Awrap_mismatch_count"]
        lift_mismatch_count += profile["lift_identity_mismatch_count"]
        zero_phase_delta_count += profile["phase_zero_transition_count"]
        role_lift_counts[(role, "lift1")] += profile["lift_1_edge_count"]
        role_lift_counts[(role, "lift2")] += profile["lift_2_edge_count"]
        role_lift_counts[(role, "other")] += profile["lift_other_edge_count"]
        role_direction_counts[(role, "positive")] += profile["phase_positive_transition_count"]
        role_direction_counts[(role, "negative")] += profile["phase_negative_transition_count"]
        role_direction_counts[(role, "zero")] += profile["phase_zero_transition_count"]
        for row in profile["lift_transition_rows"]:
            role_lift_transition_counts[(role, row["lift_transition"])] += row[
                "transition_count"
            ]
        for item in profile["phase_turn_transitions"]:
            turn_word_counts[item["phase_turn_word"]] += 1

    selected_transition_count = sum(
        count
        for (role, direction), count in role_direction_counts.items()
        if role == "selected_terminal" and direction in {"positive", "negative", "zero"}
    )
    extra_transition_count = sum(
        count
        for (role, direction), count in role_direction_counts.items()
        if role == "extra_shell" and direction in {"positive", "negative", "zero"}
    )
    all_closed = (
        carry_payload["terminal_phase_carry_orbit_closed"]
        and total_transition_count == carry_audit["terminal_carry_transition_count_total"]
        and selected_transition_count == carry_audit["selected_terminal_transition_count"]
        and extra_transition_count == carry_audit["extra_transition_count"]
        and direction_mismatch_count == 0
        and lift_mismatch_count == 0
        and zero_phase_delta_count == 0
    )

    return {
        "max_prime": carry_audit["max_prime"],
        "previous_terminal_phase_carry_orbit_closed": carry_payload[
            "terminal_phase_carry_orbit_closed"
        ],
        "terminal_phase_turn_word_closed": all_closed,
        "terminal_phase_turn_atom_count_total": len(profiles),
        "terminal_phase_turn_transition_count_total": total_transition_count,
        "terminal_phase_turn_run_count_total": total_run_count,
        "selected_terminal_transition_count": selected_transition_count,
        "extra_transition_count": extra_transition_count,
        "selected_terminal_positive_transition_count": role_direction_counts[
            ("selected_terminal", "positive")
        ],
        "selected_terminal_negative_transition_count": role_direction_counts[
            ("selected_terminal", "negative")
        ],
        "extra_positive_transition_count": role_direction_counts[("extra_shell", "positive")],
        "extra_negative_transition_count": role_direction_counts[("extra_shell", "negative")],
        "selected_terminal_phase_run_count": role_run_counts["selected_terminal"],
        "extra_phase_run_count": role_run_counts["extra_shell"],
        "selected_terminal_phase_run_max_length": role_max_run["selected_terminal"],
        "extra_phase_run_max_length": role_max_run["extra_shell"],
        "phase_direction_Awrap_mismatch_count": direction_mismatch_count,
        "lift_identity_mismatch_count": lift_mismatch_count,
        "zero_phase_delta_count": zero_phase_delta_count,
        "role_direction_rows": [
            {
                "role": role,
                "direction": direction,
                "transition_count": role_direction_counts[(role, direction)],
            }
            for role in sorted({role for role, _ in role_direction_counts})
            for direction in ["positive", "negative", "zero"]
        ],
        "role_lift_edge_rows": [
            {
                "role": role,
                "lift_class": lift_class,
                "edge_count": role_lift_counts[(role, lift_class)],
            }
            for role in sorted({role for role, _ in role_lift_counts})
            for lift_class in ["lift1", "lift2", "other"]
        ],
        "role_lift_transition_rows": [
            {
                "role": role,
                "lift_transition": lift_transition,
                "transition_count": role_lift_transition_counts[
                    (role, lift_transition)
                ],
            }
            for role, lift_transition in sorted(role_lift_transition_counts)
        ],
        "turn_word_rows": counter_rows(
            turn_word_counts, "phase_turn_word", "transition_count"
        ),
        "atom_phase_turn_profiles": profiles,
        "selected_terminal_phase_turn_word_closed": all_closed,
        "phase_turn_word_phase_saving_proved": False,
        "extra_phase_turn_run_absorption_proved": False,
        "summable_family_created": False,
        "trace_or_kloosterman_completion_ready": False,
        "row_column_unconditional_closed": False,
    }


def build_payload() -> dict[str, Any]:
    """构造审计 payload。"""
    finite_audit = audit()
    return {
        "status": "terminal_phase_turn_word_closed_phase_saving_open",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "input": "terminal phase carry-orbit audit",
        "identity": "A(q)=lambda(q)*q-D(q), lambda(q) in {1,2}; phase direction is audited by sign(A(q')/q'-A(q)/q)",
        "finite_audit": finite_audit,
        "closed_gates": [
            gate(
                "TerminalPhaseCarryOrbitImported",
                finite_audit["previous_terminal_phase_carry_orbit_closed"],
                finite_audit["previous_terminal_phase_carry_orbit_closed"],
                "The deterministic carry orbit is imported.",
                "none for import",
            ),
            gate(
                "TwoLiftNumeratorRepresentation",
                finite_audit["lift_identity_mismatch_count"] == 0,
                finite_audit["lift_identity_mismatch_count"] == 0,
                "Every edge satisfies A=lambda*q-D with lambda in {1,2}.",
                "none for finite lift ledger",
            ),
            gate(
                "PhaseDirectionAwrapEquivalence",
                finite_audit["phase_direction_Awrap_mismatch_count"] == 0,
                finite_audit["phase_direction_Awrap_mismatch_count"] == 0,
                "Every phase decrease is exactly an A-wrap and every no-wrap is a phase increase.",
                "none for finite phase-turn ledger",
            ),
            gate(
                "SelectedTerminalPhaseRunLedger",
                finite_audit["selected_terminal_phase_turn_word_closed"],
                finite_audit["selected_terminal_phase_turn_word_closed"],
                "The selected terminal word has 66 transitions, 35 monotone runs, and max run length 6.",
                "none for finite selected run ledger",
            ),
            gate(
                "PhaseTurnWordPhaseSaving",
                False,
                False,
                "Prove cancellation for the selected A-wrap phase-turn word.",
                "requires analytic phase saving or a PDEC/SAE cap",
            ),
            gate(
                "ExtraPhaseTurnRunAbsorption",
                False,
                False,
                "Absorb the extra phase-turn runs without losing selected gain.",
                "requires summable absorption or explicit dominance certificate",
            ),
        ],
        "external_sources_consulted": EXTERNAL_SOURCES,
        "external_theorem_implication": {
            "FKMS_trace_bilinear": "the phase-turn word is finite and not a completed trace/bilinear family",
            "Milicevic_Qin_Wu_Kloosterman": "no admissible Kloosterman summation variable is created by the run ledger",
            "Pascadi_Type_II": "the selected object is a one-dimensional word, not a Type-II box",
            "Wright_unbalanced_Kloosterman": "could matter only after promoting runs to an averaged trilinear fraction family",
            "Li_short_interval_x_052": "prime existence does not estimate signed A-wrap imbalance",
            "Maynard_small_gaps": "bounded gaps do not control the phase-turn run signs",
        },
        "latest_narrowest_mouth": [
            "SelectedTerminalAwrapPhaseTurnWordSaving(66 transitions: 49 negative/A-wrap, 17 positive/no-wrap; 35 runs; max run 6)",
            "AND ExtraPhaseTurnRunAbsorption(60 transitions: 33 negative, 27 positive; 24 runs)",
            "AND SelectedTerminalPrimeGapCarryWordPhaseSavingOutsidePhaseTurnLedger",
            "AND RepeatedStepPacketEnclosureTerminalLineAtomUniformBoundOutsidePhaseNormalForm",
            "AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity",
        ],
        "terminal_phase_turn_word_closed": finite_audit["terminal_phase_turn_word_closed"],
        "selected_terminal_phase_turn_word_closed": finite_audit[
            "selected_terminal_phase_turn_word_closed"
        ],
        "phase_turn_word_phase_saving_proved": False,
        "extra_phase_turn_run_absorption_proved": False,
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
    """生成 Markdown 审计报告。"""
    audit_result = payload["finite_audit"]
    atom_rows = [
        {
            "side": atom["packet_side"],
            "packet": atom["packet_index"],
            "role": atom["role"],
            "m": atom["m"],
            "transitions": atom["phase_turn_transition_count"],
            "positive": atom["phase_positive_transition_count"],
            "negative": atom["phase_negative_transition_count"],
            "runs": atom["phase_run_count"],
            "max_run": atom["phase_run_max_length"],
            "lift1_edges": atom["lift_1_edge_count"],
            "lift2_edges": atom["lift_2_edge_count"],
            "turn_words": atom["phase_turn_word_count"],
        }
        for atom in audit_result["atom_phase_turn_profiles"]
    ]
    lines = [
        "# Prime Matrix Phi-LPF repeated-step terminal phase-turn word 审计",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['frontier_verified_date']}`",
        "",
        "## 1. 当前对象",
        "",
        "```text",
        f"input={payload['input']}",
        f"identity={payload['identity']}",
        "```",
        "",
        "## 2. phase-turn 有限审计",
        "",
        "```text",
        f"previous_terminal_phase_carry_orbit_closed={str(audit_result['previous_terminal_phase_carry_orbit_closed']).lower()}",
        f"terminal_phase_turn_word_closed={str(audit_result['terminal_phase_turn_word_closed']).lower()}",
        f"terminal_phase_turn_atom_count_total={audit_result['terminal_phase_turn_atom_count_total']}",
        f"terminal_phase_turn_transition_count_total={audit_result['terminal_phase_turn_transition_count_total']}",
        f"terminal_phase_turn_run_count_total={audit_result['terminal_phase_turn_run_count_total']}",
        f"selected_terminal_transition_count={audit_result['selected_terminal_transition_count']}",
        f"selected_terminal_positive_transition_count={audit_result['selected_terminal_positive_transition_count']}",
        f"selected_terminal_negative_transition_count={audit_result['selected_terminal_negative_transition_count']}",
        f"selected_terminal_phase_run_count={audit_result['selected_terminal_phase_run_count']}",
        f"selected_terminal_phase_run_max_length={audit_result['selected_terminal_phase_run_max_length']}",
        f"extra_transition_count={audit_result['extra_transition_count']}",
        f"extra_positive_transition_count={audit_result['extra_positive_transition_count']}",
        f"extra_negative_transition_count={audit_result['extra_negative_transition_count']}",
        f"extra_phase_run_count={audit_result['extra_phase_run_count']}",
        f"extra_phase_run_max_length={audit_result['extra_phase_run_max_length']}",
        f"phase_direction_Awrap_mismatch_count={audit_result['phase_direction_Awrap_mismatch_count']}",
        f"lift_identity_mismatch_count={audit_result['lift_identity_mismatch_count']}",
        f"zero_phase_delta_count={audit_result['zero_phase_delta_count']}",
        f"phase_turn_word_phase_saving_proved={str(audit_result['phase_turn_word_phase_saving_proved']).lower()}",
        f"row_column_unconditional_closed={str(audit_result['row_column_unconditional_closed']).lower()}",
        "```",
        "",
        "atom phase-turn rows：",
        "",
        *markdown_table(
            atom_rows,
            [
                "side",
                "packet",
                "role",
                "m",
                "transitions",
                "positive",
                "negative",
                "runs",
                "max_run",
                "lift1_edges",
                "lift2_edges",
                "turn_words",
            ],
        ),
        "",
        "role direction rows：",
        "",
        *markdown_table(
            audit_result["role_direction_rows"],
            ["role", "direction", "transition_count"],
        ),
        "",
        "role lift edge rows：",
        "",
        *markdown_table(
            audit_result["role_lift_edge_rows"],
            ["role", "lift_class", "edge_count"],
        ),
        "",
        "role lift transition rows：",
        "",
        *markdown_table(
            audit_result["role_lift_transition_rows"],
            ["role", "lift_transition", "transition_count"],
        ),
        "",
        "## 3. 门控表",
        "",
        *markdown_table(
            payload["closed_gates"], ["gate", "closed", "proved", "meaning", "remaining"]
        ),
        "",
        "## 4. 外部 theorem 影响",
        "",
        *markdown_table(payload["external_sources_consulted"], ["key", "url", "role"]),
        "",
        "```text",
        *[f"{key}={value}" for key, value in payload["external_theorem_implication"].items()],
        "```",
        "",
        "结论：carry orbit 已被进一步压成 two-lift phase-turn word。有限账本中",
        "`A(q)/q` 的相位下降恰好等于 `A_wrap`，相位上升恰好等于 no-wrap。",
        "这仍不是相位节省定理，也不是 row/column Phi-LPF 无条件闭合。",
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
        f"terminal_phase_turn_word_closed={str(payload['terminal_phase_turn_word_closed']).lower()}",
        f"selected_terminal_phase_turn_word_closed={str(payload['selected_terminal_phase_turn_word_closed']).lower()}",
        f"phase_turn_word_phase_saving_proved={str(payload['phase_turn_word_phase_saving_proved']).lower()}",
        f"extra_phase_turn_run_absorption_proved={str(payload['extra_phase_turn_run_absorption_proved']).lower()}",
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
    print(f"terminal_phase_turn_word_closed={payload['terminal_phase_turn_word_closed']}")
    print(
        "selected_terminal_negative_transition_count="
        f"{audit_result['selected_terminal_negative_transition_count']}"
    )
    print(f"row_column_unconditional_closed={payload['row_column_unconditional_closed']}")


if __name__ == "__main__":
    main()
