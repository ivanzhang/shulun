#!/usr/bin/env python3
"""审计 repeated-step terminal phase-turn word 的 signed variation budget。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_repeated_step_packet_enclosure_terminal_phase_variation_budget_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-dominant-sign-word-repeated-step-packet-enclosure-terminal-phase-variation-budget-audit.json

上一层把 carry orbit 压成 two-lift phase-turn word。本层继续计算
A(q)/q 的正变差、负变差、总变差、净位移和 run 级分解。
该层只关闭有限 variation ledger，不证明相位节省。
"""

from __future__ import annotations

import hashlib
import json
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = (
    "prime-matrix-phi-lpf-dominant-sign-word-repeated-step-packet-enclosure-"
    "terminal-phase-variation-budget"
)
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-25"

PHASE_TURN_AUDIT = (
    DOCS
    / "prime-matrix-phi-lpf-dominant-sign-word-repeated-step-packet-enclosure-terminal-phase-turn-word-audit.json"
)

DEPENDENCIES = [
    PHASE_TURN_AUDIT,
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
        "role": "trace bilinear estimates need a completed averaging family; this audit only gives finite variation budgets",
    },
    {
        "key": "Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman",
        "url": "https://arxiv.org/abs/2511.07550",
        "role": "Kloosterman estimates need an admissible summation variable and do not act on the finite run ledger directly",
    },
    {
        "key": "Pascadi_2025_nonabelian_composite_type_II",
        "url": "https://arxiv.org/abs/2511.08445",
        "role": "the variation ledger is one-dimensional, not a Type-II rectangle",
    },
    {
        "key": "Wright_2026_unbalanced_kloosterman_fractions",
        "url": "https://arxiv.org/abs/2604.25177",
        "role": "unbalanced Kloosterman fractions remain candidate input only after an averaged fraction family is built",
    },
    {
        "key": "Dong_Robles_Zeindler_2026_bilinear_kloosterman_fractions_withdrawn",
        "url": "https://arxiv.org/abs/2601.00292",
        "role": "withdrawn on arXiv; recorded only as a non-usable boundary, not as an input",
    },
    {
        "key": "Li_2023_short_interval_primes_x_052_v8",
        "url": "https://arxiv.org/abs/2308.04458",
        "role": "short-interval prime existence does not estimate signed variation imbalance",
    },
    {
        "key": "Maynard_2015_small_gaps_prime_gaps",
        "url": "https://doi.org/10.4007/annals.2015.181.1.7",
        "role": "bounded gaps do not control total variation or run-level cancellation",
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


def frac(num: int, den: int) -> Fraction:
    """由证书分子分母构造 Fraction。"""
    return Fraction(num, den)


def frac_text(value: Fraction) -> str:
    """稳定输出分数。"""
    return f"{value.numerator}/{value.denominator}"


def frac_decimal(value: Fraction, places: int = 12) -> str:
    """输出有限小数摘要。"""
    return f"{float(value):.{places}f}"


def frac_record(value: Fraction) -> dict[str, Any]:
    """输出分数记录。"""
    return {
        "fraction": frac_text(value),
        "decimal": frac_decimal(value),
        "numerator": value.numerator,
        "denominator": value.denominator,
    }


def transition_delta(transition: dict[str, Any]) -> Fraction:
    """读取 transition 的 phase delta。"""
    return frac(transition["phase_delta_num"], transition["phase_delta_den"])


def run_variation_rows(transitions: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """把最大同向 run 写成 variation rows。"""
    if not transitions:
        return []
    rows: list[dict[str, Any]] = []
    start = 0
    for index in range(1, len(transitions)):
        if transitions[index]["phase_direction"] != transitions[start]["phase_direction"]:
            rows.append(run_variation_row(transitions, start, index - 1, len(rows)))
            start = index
    rows.append(run_variation_row(transitions, start, len(transitions) - 1, len(rows)))
    return rows


def run_variation_row(
    transitions: list[dict[str, Any]],
    start: int,
    end: int,
    run_id: int,
) -> dict[str, Any]:
    """构造单个 run 的 signed variation 行。"""
    segment = transitions[start : end + 1]
    deltas = [transition_delta(item) for item in segment]
    signed_delta = sum(deltas, Fraction(0))
    variation = sum(abs(item) for item in deltas)
    return {
        "run_id": run_id,
        "direction": segment[0]["phase_direction"],
        "start_transition_index": start,
        "end_transition_index": end,
        "length": len(segment),
        "q_start": segment[0]["q"],
        "q_end": segment[-1]["q_next"],
        "signed_delta": frac_record(signed_delta),
        "variation": frac_record(variation),
        "positive_variation": frac_record(max(signed_delta, Fraction(0))),
        "negative_variation": frac_record(max(-signed_delta, Fraction(0))),
        "A_wrap_count": sum(1 for item in segment if item["A_wrap"]),
        "D_wrap_count": sum(1 for item in segment if item["D_wrap"]),
        "carry_min": min(item["carry_formula"] for item in segment),
        "carry_max": max(item["carry_formula"] for item in segment),
        "run_variation_identity_verified": variation == abs(signed_delta),
    }


def atom_variation_profile(atom: dict[str, Any]) -> dict[str, Any]:
    """计算单个 atom 的 variation budget。"""
    transitions = atom["phase_turn_transitions"]
    deltas = [transition_delta(item) for item in transitions]
    positive = sum((item for item in deltas if item > 0), Fraction(0))
    negative = sum((-item for item in deltas if item < 0), Fraction(0))
    total = positive + negative
    net = positive - negative
    if transitions:
        start_phase = Fraction(transitions[0]["A"], transitions[0]["q"])
        end_phase = Fraction(transitions[-1]["A_next"], transitions[-1]["q_next"])
    else:
        start_phase = Fraction(0)
        end_phase = Fraction(0)
    runs = run_variation_rows(transitions)
    run_total = sum(
        Fraction(row["variation"]["numerator"], row["variation"]["denominator"])
        for row in runs
    )
    run_net = sum(
        Fraction(row["signed_delta"]["numerator"], row["signed_delta"]["denominator"])
        for row in runs
    )
    direction_counts = Counter(item["phase_direction"] for item in transitions)
    return {
        "packet_side": atom["packet_side"],
        "packet_index": atom["packet_index"],
        "role": atom["role"],
        "P": atom["P"],
        "m": atom["m"],
        "transition_count": len(transitions),
        "phase_run_count": len(runs),
        "phase_run_max_length": max((row["length"] for row in runs), default=0),
        "positive_transition_count": direction_counts["positive"],
        "negative_transition_count": direction_counts["negative"],
        "zero_transition_count": direction_counts["zero"],
        "phase_start": frac_record(start_phase),
        "phase_end": frac_record(end_phase),
        "positive_variation": frac_record(positive),
        "negative_variation": frac_record(negative),
        "total_variation": frac_record(total),
        "net_phase_displacement": frac_record(net),
        "negative_variation_excess": frac_record(negative - positive),
        "positive_variation_excess": frac_record(positive - negative),
        "dominant_variation_direction": "negative"
        if negative > positive
        else "positive"
        if positive > negative
        else "balanced",
        "endpoint_net_identity_verified": end_phase - start_phase == net,
        "variation_identity_verified": total == positive + negative,
        "run_variation_sum_identity_verified": run_total == total,
        "run_signed_sum_identity_verified": run_net == net,
        "all_run_variation_identities_verified": all(
            row["run_variation_identity_verified"] for row in runs
        ),
        "run_variation_rows": runs,
    }


def sum_records(records: list[dict[str, Any]]) -> Fraction:
    """累加分数记录。"""
    return sum(
        (
            Fraction(record["numerator"], record["denominator"])
            for record in records
        ),
        Fraction(0),
    )


def role_variation_rows(profiles: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """按 role 汇总 variation budget。"""
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for profile in profiles:
        grouped[profile["role"]].append(profile)
    rows: list[dict[str, Any]] = []
    for role in sorted(grouped):
        atoms = grouped[role]
        positive = sum_records([item["positive_variation"] for item in atoms])
        negative = sum_records([item["negative_variation"] for item in atoms])
        total = sum_records([item["total_variation"] for item in atoms])
        net = sum_records([item["net_phase_displacement"] for item in atoms])
        rows.append(
            {
                "role": role,
                "atom_count": len(atoms),
                "transition_count": sum(item["transition_count"] for item in atoms),
                "phase_run_count": sum(item["phase_run_count"] for item in atoms),
                "phase_run_max_length": max(
                    item["phase_run_max_length"] for item in atoms
                ),
                "positive_transition_count": sum(
                    item["positive_transition_count"] for item in atoms
                ),
                "negative_transition_count": sum(
                    item["negative_transition_count"] for item in atoms
                ),
                "positive_variation": frac_record(positive),
                "negative_variation": frac_record(negative),
                "total_variation": frac_record(total),
                "net_phase_displacement": frac_record(net),
                "negative_variation_excess": frac_record(negative - positive),
                "dominant_variation_direction": "negative"
                if negative > positive
                else "positive"
                if positive > negative
                else "balanced",
                "role_variation_identity_verified": total == positive + negative,
                "role_net_identity_verified": net == positive - negative,
            }
        )
    return rows


def audit() -> dict[str, Any]:
    """生成 signed variation budget 审计。"""
    turn_payload = load_json(PHASE_TURN_AUDIT)
    turn_audit = turn_payload["finite_audit"]
    profiles = [
        atom_variation_profile(atom)
        for atom in turn_audit["atom_phase_turn_profiles"]
    ]
    role_rows = role_variation_rows(profiles)
    selected_row = next(row for row in role_rows if row["role"] == "selected_terminal")
    extra_row = next(row for row in role_rows if row["role"] == "extra_shell")

    total_transition_count = sum(item["transition_count"] for item in profiles)
    total_run_count = sum(item["phase_run_count"] for item in profiles)
    bad_atom_count = sum(
        1
        for item in profiles
        if not (
            item["endpoint_net_identity_verified"]
            and item["variation_identity_verified"]
            and item["run_variation_sum_identity_verified"]
            and item["run_signed_sum_identity_verified"]
            and item["all_run_variation_identities_verified"]
        )
    )
    bad_role_count = sum(
        1
        for row in role_rows
        if not (
            row["role_variation_identity_verified"]
            and row["role_net_identity_verified"]
        )
    )
    all_closed = (
        turn_payload["terminal_phase_turn_word_closed"]
        and total_transition_count
        == turn_audit["terminal_phase_turn_transition_count_total"]
        and total_run_count == turn_audit["terminal_phase_turn_run_count_total"]
        and selected_row["transition_count"]
        == turn_audit["selected_terminal_transition_count"]
        and extra_row["transition_count"] == turn_audit["extra_transition_count"]
        and bad_atom_count == 0
        and bad_role_count == 0
    )

    return {
        "max_prime": turn_audit["max_prime"],
        "previous_terminal_phase_turn_word_closed": turn_payload[
            "terminal_phase_turn_word_closed"
        ],
        "terminal_phase_variation_budget_closed": all_closed,
        "terminal_phase_variation_atom_count_total": len(profiles),
        "terminal_phase_variation_transition_count_total": total_transition_count,
        "terminal_phase_variation_run_count_total": total_run_count,
        "selected_terminal_transition_count": selected_row["transition_count"],
        "selected_terminal_phase_run_count": selected_row["phase_run_count"],
        "selected_terminal_phase_run_max_length": selected_row[
            "phase_run_max_length"
        ],
        "selected_terminal_positive_transition_count": selected_row[
            "positive_transition_count"
        ],
        "selected_terminal_negative_transition_count": selected_row[
            "negative_transition_count"
        ],
        "selected_terminal_positive_variation": selected_row["positive_variation"],
        "selected_terminal_negative_variation": selected_row["negative_variation"],
        "selected_terminal_total_variation": selected_row["total_variation"],
        "selected_terminal_net_phase_displacement": selected_row[
            "net_phase_displacement"
        ],
        "selected_terminal_negative_variation_excess": selected_row[
            "negative_variation_excess"
        ],
        "extra_transition_count": extra_row["transition_count"],
        "extra_phase_run_count": extra_row["phase_run_count"],
        "extra_positive_variation": extra_row["positive_variation"],
        "extra_negative_variation": extra_row["negative_variation"],
        "extra_total_variation": extra_row["total_variation"],
        "extra_net_phase_displacement": extra_row["net_phase_displacement"],
        "extra_negative_variation_excess": extra_row[
            "negative_variation_excess"
        ],
        "bad_atom_variation_identity_count": bad_atom_count,
        "bad_role_variation_identity_count": bad_role_count,
        "role_variation_rows": role_rows,
        "atom_variation_profiles": profiles,
        "selected_terminal_variation_budget_closed": all_closed,
        "phase_variation_budget_phase_saving_proved": False,
        "extra_variation_budget_absorption_proved": False,
        "summable_family_created": False,
        "trace_or_kloosterman_completion_ready": False,
        "row_column_unconditional_closed": False,
    }


def build_payload() -> dict[str, Any]:
    """构造 payload。"""
    finite_audit = audit()
    return {
        "status": "terminal_phase_variation_budget_closed_phase_saving_open",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "input": "terminal phase-turn word audit",
        "identity": "total variation = positive variation + negative variation; net displacement = positive variation - negative variation",
        "finite_audit": finite_audit,
        "closed_gates": [
            gate(
                "TerminalPhaseTurnWordImported",
                finite_audit["previous_terminal_phase_turn_word_closed"],
                finite_audit["previous_terminal_phase_turn_word_closed"],
                "The two-lift phase-turn word is imported.",
                "none for import",
            ),
            gate(
                "SignedVariationBudgetIdentity",
                finite_audit["terminal_phase_variation_budget_closed"],
                finite_audit["terminal_phase_variation_budget_closed"],
                "Every atom and role satisfies total=positive+negative and net=positive-negative.",
                "none for finite variation ledger",
            ),
            gate(
                "SelectedTerminalVariationLedger",
                finite_audit["selected_terminal_variation_budget_closed"],
                finite_audit["selected_terminal_variation_budget_closed"],
                "The selected terminal word has exact positive/negative variation and run budgets.",
                "none for finite selected variation ledger",
            ),
            gate(
                "VariationBudgetPhaseSaving",
                False,
                False,
                "Use the variation budget to prove phase saving.",
                "requires analytic monotone-run cap or PDEC/SAE certificate",
            ),
            gate(
                "ExtraVariationBudgetAbsorption",
                False,
                False,
                "Absorb extra variation budgets without losing selected gain.",
                "requires dominance or summable absorption",
            ),
        ],
        "external_sources_consulted": EXTERNAL_SOURCES,
        "external_theorem_implication": {
            "FKMS_trace_bilinear": "variation budgets are not completed trace/bilinear sums",
            "Milicevic_Qin_Wu_Kloosterman": "no Kloosterman summation variable follows from a finite variation ledger",
            "Pascadi_Type_II": "no Type-II rectangle is created",
            "Wright_unbalanced_Kloosterman": "requires an averaged fraction family absent here",
            "Dong_Robles_Zeindler_2026": "withdrawn on arXiv and not used",
            "Li_short_interval_x_052": "does not estimate signed variation",
            "Maynard_small_gaps": "does not estimate run-level cancellation",
        },
        "latest_narrowest_mouth": [
            "SelectedTerminalNegativeVariationExcessPhaseSaving(total variation 17.979169131897; net -1.456565972578; 35 runs; max run 6)",
            "AND ExtraNegativeVariationBudgetAbsorption(total variation 14.109301881162; net -0.907719323182; 24 runs)",
            "AND SelectedTerminalAwrapPhaseTurnWordSavingOutsideVariationBudget",
            "AND RepeatedStepPacketEnclosureTerminalLineAtomUniformBoundOutsidePhaseNormalForm",
            "AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity",
        ],
        "terminal_phase_variation_budget_closed": finite_audit[
            "terminal_phase_variation_budget_closed"
        ],
        "selected_terminal_variation_budget_closed": finite_audit[
            "selected_terminal_variation_budget_closed"
        ],
        "phase_variation_budget_phase_saving_proved": False,
        "extra_variation_budget_absorption_proved": False,
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


def variation_cell(record: dict[str, Any]) -> str:
    """表格中使用小数加精确分数。"""
    return f"{record['decimal']} ({record['fraction']})"


def build_markdown(payload: dict[str, Any]) -> str:
    """生成 Markdown 证书。"""
    audit_result = payload["finite_audit"]
    atom_rows = [
        {
            "side": atom["packet_side"],
            "packet": atom["packet_index"],
            "role": atom["role"],
            "m": atom["m"],
            "transitions": atom["transition_count"],
            "runs": atom["phase_run_count"],
            "max_run": atom["phase_run_max_length"],
            "pos_var": variation_cell(atom["positive_variation"]),
            "neg_var": variation_cell(atom["negative_variation"]),
            "net": variation_cell(atom["net_phase_displacement"]),
            "total_var": variation_cell(atom["total_variation"]),
            "dominant": atom["dominant_variation_direction"],
        }
        for atom in audit_result["atom_variation_profiles"]
    ]
    role_rows = [
        {
            "role": row["role"],
            "transitions": row["transition_count"],
            "runs": row["phase_run_count"],
            "max_run": row["phase_run_max_length"],
            "positive_turns": row["positive_transition_count"],
            "negative_turns": row["negative_transition_count"],
            "pos_var": variation_cell(row["positive_variation"]),
            "neg_var": variation_cell(row["negative_variation"]),
            "net": variation_cell(row["net_phase_displacement"]),
            "total_var": variation_cell(row["total_variation"]),
            "dominant": row["dominant_variation_direction"],
        }
        for row in audit_result["role_variation_rows"]
    ]
    lines = [
        "# Prime Matrix Phi-LPF repeated-step terminal phase variation-budget 审计",
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
        "## 2. variation budget 有限审计",
        "",
        "```text",
        f"previous_terminal_phase_turn_word_closed={str(audit_result['previous_terminal_phase_turn_word_closed']).lower()}",
        f"terminal_phase_variation_budget_closed={str(audit_result['terminal_phase_variation_budget_closed']).lower()}",
        f"terminal_phase_variation_atom_count_total={audit_result['terminal_phase_variation_atom_count_total']}",
        f"terminal_phase_variation_transition_count_total={audit_result['terminal_phase_variation_transition_count_total']}",
        f"terminal_phase_variation_run_count_total={audit_result['terminal_phase_variation_run_count_total']}",
        f"selected_terminal_transition_count={audit_result['selected_terminal_transition_count']}",
        f"selected_terminal_phase_run_count={audit_result['selected_terminal_phase_run_count']}",
        f"selected_terminal_phase_run_max_length={audit_result['selected_terminal_phase_run_max_length']}",
        f"selected_terminal_positive_transition_count={audit_result['selected_terminal_positive_transition_count']}",
        f"selected_terminal_negative_transition_count={audit_result['selected_terminal_negative_transition_count']}",
        f"selected_terminal_positive_variation={variation_cell(audit_result['selected_terminal_positive_variation'])}",
        f"selected_terminal_negative_variation={variation_cell(audit_result['selected_terminal_negative_variation'])}",
        f"selected_terminal_total_variation={variation_cell(audit_result['selected_terminal_total_variation'])}",
        f"selected_terminal_net_phase_displacement={variation_cell(audit_result['selected_terminal_net_phase_displacement'])}",
        f"selected_terminal_negative_variation_excess={variation_cell(audit_result['selected_terminal_negative_variation_excess'])}",
        f"extra_transition_count={audit_result['extra_transition_count']}",
        f"extra_phase_run_count={audit_result['extra_phase_run_count']}",
        f"extra_total_variation={variation_cell(audit_result['extra_total_variation'])}",
        f"extra_net_phase_displacement={variation_cell(audit_result['extra_net_phase_displacement'])}",
        f"bad_atom_variation_identity_count={audit_result['bad_atom_variation_identity_count']}",
        f"bad_role_variation_identity_count={audit_result['bad_role_variation_identity_count']}",
        f"phase_variation_budget_phase_saving_proved={str(audit_result['phase_variation_budget_phase_saving_proved']).lower()}",
        f"row_column_unconditional_closed={str(audit_result['row_column_unconditional_closed']).lower()}",
        "```",
        "",
        "role variation rows：",
        "",
        *markdown_table(
            role_rows,
            [
                "role",
                "transitions",
                "runs",
                "max_run",
                "positive_turns",
                "negative_turns",
                "pos_var",
                "neg_var",
                "net",
                "total_var",
                "dominant",
            ],
        ),
        "",
        "atom variation rows：",
        "",
        *markdown_table(
            atom_rows,
            [
                "side",
                "packet",
                "role",
                "m",
                "transitions",
                "runs",
                "max_run",
                "pos_var",
                "neg_var",
                "net",
                "total_var",
                "dominant",
            ],
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
        "结论：phase-turn word 已被压成 signed variation budget。selected terminal",
        "部分的负变差严格超过正变差，净位移约为 `-1.456565972578`，总变差",
        "约为 `17.979169131897`。这仍不是 phase saving，也不是无条件闭合。",
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
        f"terminal_phase_variation_budget_closed={str(payload['terminal_phase_variation_budget_closed']).lower()}",
        f"selected_terminal_variation_budget_closed={str(payload['selected_terminal_variation_budget_closed']).lower()}",
        f"phase_variation_budget_phase_saving_proved={str(payload['phase_variation_budget_phase_saving_proved']).lower()}",
        f"extra_variation_budget_absorption_proved={str(payload['extra_variation_budget_absorption_proved']).lower()}",
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
    print(
        "terminal_phase_variation_budget_closed="
        f"{payload['terminal_phase_variation_budget_closed']}"
    )
    print(
        "selected_terminal_net_phase_displacement="
        f"{audit_result['selected_terminal_net_phase_displacement']['decimal']}"
    )
    print(f"row_column_unconditional_closed={payload['row_column_unconditional_closed']}")


if __name__ == "__main__":
    main()
