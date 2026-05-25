#!/usr/bin/env python3
"""审计 m773 final negative run 是否只是两步 endpoint-collar wrap debt。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_right_tail_final_negative_run_endpoint_collar_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-right-tail-final-negative-run-endpoint-collar-router.json

本层承接 right-tail overhang excess decomposition。上一层把唯一未支付尾差压到
right:1887:selected_terminal:m773 的最终负 run。本层继续原子化该 run：

  q=461 -> 463 -> 467,
  A=417 -> 87 -> 34,
  D=44 -> 376 -> 433.

两条边均为 negative_Awrap1_Dwrap0_L1to1，且中间相位 87/463 完全消去。因此
最终尾差不是匿名变差，而是端点 collar 公式

  179065/215287 = 417/461 - 34/467 = 1 - 44/461 - 34/467.

剩余问题被压成 terminal double-Awrap endpoint-collar payment/PDEC，而不是新的
无条件闭合证明。
"""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-right-tail-final-negative-run-endpoint-collar"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

RIGHT_TAIL_JSON = DOCS / "prime-matrix-phi-lpf-right-tail-overhang-excess-decomposition-router.json"
TURN_JSON = DOCS / (
    "prime-matrix-phi-lpf-dominant-sign-word-repeated-step-packet-enclosure-"
    "terminal-phase-turn-word-audit.json"
)
NORMAL_FORM_JSON = DOCS / (
    "prime-matrix-phi-lpf-dominant-sign-word-repeated-step-packet-enclosure-"
    "terminal-phase-normal-form-audit.json"
)
VARIATION_JSON = DOCS / (
    "prime-matrix-phi-lpf-dominant-sign-word-repeated-step-packet-enclosure-"
    "terminal-phase-variation-budget-audit.json"
)

PIVOT_LAW = "BridgeRootQSpinePivotEnclosureLawOrPDEC"
DOUBLE_WRAP_COLLAR_LAW = "TerminalDoubleAwrapEndpointCollarPaymentOrPDEC"
MASS_RATIO_LAW = "BoundaryAdjacentRunMassRatioLawOrPDEC"
ORIENTATION_LAW = "PrimitiveOrientationLocalFactorProductLawBeforePushforward"
MOVING_BEATTY_SAVING = "SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving"
TRACE_FAMILY = "AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily"
GROUP_ORBIT_INPUT = "AdmissibleFiniteGroupOrbitExpansionOrThinGroupSieveFamily"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    paths = [Path(__file__).resolve(), RIGHT_TAIL_JSON, TURN_JSON, NORMAL_FORM_JSON, VARIATION_JSON]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def frac_record(value: Fraction) -> dict[str, Any]:
    """稳定输出分数。"""
    return {
        "fraction": f"{value.numerator}/{value.denominator}",
        "decimal": f"{float(value):.12f}",
        "numerator": value.numerator,
        "denominator": value.denominator,
    }


def frac_from_record(record: dict[str, Any]) -> Fraction:
    """从 JSON 分数记录恢复 Fraction。"""
    return Fraction(int(record["numerator"]), int(record["denominator"]))


def fmt_bool(value: Any) -> str:
    """布尔值小写渲染。"""
    return "true" if bool(value) else "false"


def cell(value: Any) -> str:
    """Markdown 表格单元转义。"""
    return str(value).replace("|", r"\|")


def render_fraction(record: dict[str, Any]) -> str:
    """表格用分数摘要。"""
    return f"{record['decimal']} ({record['fraction']})"


def find_m773_turn_profile(payload: dict[str, Any]) -> dict[str, Any]:
    """定位 m773 的 phase-turn profile。"""
    for row in payload["finite_audit"]["atom_phase_turn_profiles"]:
        if row.get("P") == 607 and row.get("m") == 773 and row.get("role") == "selected_terminal":
            return row
    raise ValueError("m773 selected-terminal turn profile not found")


def find_m773_normal_profile(payload: dict[str, Any]) -> dict[str, Any]:
    """定位 m773 的 phase normal-form profile。"""
    for row in payload["finite_audit"]["phase_profiles"]:
        if row.get("P") == 607 and row.get("m") == 773 and row.get("role") == "selected_terminal":
            return row
    raise ValueError("m773 selected-terminal normal-form profile not found")


def find_m773_variation_profile(payload: dict[str, Any]) -> dict[str, Any]:
    """定位 m773 的 variation profile。"""
    for row in payload["finite_audit"]["atom_variation_profiles"]:
        if row.get("P") == 607 and row.get("m") == 773 and row.get("role") == "selected_terminal":
            return row
    raise ValueError("m773 selected-terminal variation profile not found")


def transition_fraction(row: dict[str, Any]) -> Fraction:
    """恢复单步相位差。"""
    return Fraction(int(row["phase_delta_num"]), int(row["phase_delta_den"]))


def build_certificate() -> dict[str, Any]:
    """组装 final negative run endpoint-collar 证书。"""
    right_tail = load_json(RIGHT_TAIL_JSON)
    turn_profile = find_m773_turn_profile(load_json(TURN_JSON))
    normal_profile = find_m773_normal_profile(load_json(NORMAL_FORM_JSON))
    variation_profile = find_m773_variation_profile(load_json(VARIATION_JSON))

    final_run = right_tail["final_run"]
    start_i = 4
    end_i = 5
    transitions = [
        row
        for row in turn_profile["phase_turn_transitions"]
        if start_i <= int(row["transition_index"]) <= end_i
    ]
    if len(transitions) != 2:
        raise ValueError("expected exactly two final-run transitions")

    q_path = [int(transitions[0]["q"]), int(transitions[1]["q"]), int(transitions[1]["q_next"])]
    a_path = [int(transitions[0]["A"]), int(transitions[1]["A"]), int(transitions[1]["A_next"])]
    d_path = [int(transitions[0]["D"]), int(transitions[1]["D"]), int(transitions[1]["D_next"])]
    gap_path = [int(row["q_gap"]) for row in transitions]
    carry_path = [int(row["carry_formula"]) for row in transitions]
    words = [row["phase_turn_word"] for row in transitions]

    signed_delta_sum = sum((transition_fraction(row) for row in transitions), Fraction(0, 1))
    final_tail_mass = frac_from_record(right_tail["tail_overhang_mass"])
    variation_final_signed = frac_from_record(variation_profile["run_variation_rows"][-1]["signed_delta"])
    endpoint_drop_signed = Fraction(a_path[-1], q_path[-1]) - Fraction(a_path[0], q_path[0])
    endpoint_tail_mass = -endpoint_drop_signed
    collar_tail_mass = Fraction(1, 1) - Fraction(d_path[0], q_path[0]) - Fraction(a_path[-1], q_path[-1])

    two_edge_sum_matches = signed_delta_sum == variation_final_signed == -final_tail_mass
    endpoint_telescoping_closed = endpoint_drop_signed == signed_delta_sum
    collar_formula_closed = collar_tail_mass == final_tail_mass
    middle_phase_cancels = (
        Fraction(a_path[1], q_path[1]) - Fraction(a_path[0], q_path[0])
        + Fraction(a_path[-1], q_path[-1]) - Fraction(a_path[1], q_path[1])
        == endpoint_drop_signed
    )
    double_awrap_word_closed = all(
        row["phase_direction"] == "negative"
        and row["A_wrap"] is True
        and row["D_wrap"] is False
        and int(row["lift"]) == 1
        and int(row["lift_next"]) == 1
        for row in transitions
    )
    endpoint_normal_form_closed = (
        normal_profile.get("phase_normal_form") == "e(h*k*P/q)=e(-h*D/q)=e(h*A(q)/q)"
        and normal_profile.get("fixed_numerator_kloosterman_ready") is False
        and normal_profile.get("numerator_motion_class") == "full_distinct_moving_beatty_numerator"
    )
    reduction_closed = (
        right_tail.get("right_tail_overhang_excess_decomposition_closed") is True
        and two_edge_sum_matches
        and endpoint_telescoping_closed
        and collar_formula_closed
        and middle_phase_cancels
        and double_awrap_word_closed
        and endpoint_normal_form_closed
    )
    latest_gate = (
        f"{PIVOT_LAW} AND {DOUBLE_WRAP_COLLAR_LAW} AND {MASS_RATIO_LAW} AND {ORIENTATION_LAW} "
        f"AND {MOVING_BEATTY_SAVING} AND {TRACE_FAMILY} AND {GROUP_ORBIT_INPUT}"
    )
    gate_rows = [
        {
            "gate": "FinalRunTwoEdgeTurnWordIdentified",
            "closed": len(transitions) == 2 and q_path == [461, 463, 467],
            "proved": len(transitions) == 2 and q_path == [461, 463, 467],
            "meaning": "the remaining tail is exactly the q=461->463->467 two-edge terminal run.",
            "remaining": "finite turn-word ledger",
        },
        {
            "gate": "DoubleAwrapSameLiftEndpointCollar",
            "closed": double_awrap_word_closed,
            "proved": double_awrap_word_closed,
            "meaning": "both final edges are negative Awrap=1, Dwrap=0, L1->L1 transitions.",
            "remaining": "finite phase-turn ledger",
        },
        {
            "gate": "EndpointTelescopingIdentity",
            "closed": endpoint_telescoping_closed and middle_phase_cancels,
            "proved": endpoint_telescoping_closed and middle_phase_cancels,
            "meaning": "the middle phase A=87/q=463 cancels, leaving only endpoint collar data.",
            "remaining": "finite rational identity",
        },
        {
            "gate": "EndpointCollarDebtFormula",
            "closed": collar_formula_closed,
            "proved": collar_formula_closed,
            "meaning": "tail mass equals 1 - D_start/q_start - A_end/q_end.",
            "remaining": "finite endpoint-collar identity",
        },
        {
            "gate": "TerminalDoubleAwrapEndpointCollarPaymentLaw",
            "closed": False,
            "proved": False,
            "meaning": "a uniform law must pay or exclude this terminal double-Awrap collar debt.",
            "remaining": DOUBLE_WRAP_COLLAR_LAW,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "this is a finite collar reduction, not a global parity-breaking theorem.",
            "remaining": f"{PIVOT_LAW} AND {MASS_RATIO_LAW} AND {ORIENTATION_LAW} AND {MOVING_BEATTY_SAVING}",
        },
    ]
    return {
        "certificate_type": "prime_matrix_phi_lpf_right_tail_final_negative_run_endpoint_collar_router",
        "status": "final_negative_run_endpoint_collar_reduction_closed_payment_law_open",
        "verified_date": "2026-05-25",
        "previous_right_tail_overhang_excess_decomposition_closed": right_tail.get(
            "right_tail_overhang_excess_decomposition_closed"
        )
        is True,
        "atom_key": right_tail["atom_key"],
        "P": right_tail["P"],
        "m": right_tail["m"],
        "role": right_tail["role"],
        "q_path": q_path,
        "A_path": a_path,
        "D_path": d_path,
        "q_gap_path": gap_path,
        "carry_path": carry_path,
        "phase_turn_words": words,
        "transition_signed_deltas": [frac_record(transition_fraction(row)) for row in transitions],
        "transition_signed_delta_sum": frac_record(signed_delta_sum),
        "variation_final_signed_delta": frac_record(variation_final_signed),
        "final_tail_mass": frac_record(final_tail_mass),
        "endpoint_drop_signed": frac_record(endpoint_drop_signed),
        "endpoint_tail_mass": frac_record(endpoint_tail_mass),
        "left_collar_start_D_over_q": frac_record(Fraction(d_path[0], q_path[0])),
        "right_collar_end_A_over_q": frac_record(Fraction(a_path[-1], q_path[-1])),
        "endpoint_collar_formula_tail": frac_record(collar_tail_mass),
        "two_edge_sum_matches_variation_and_tail": two_edge_sum_matches,
        "endpoint_telescoping_closed": endpoint_telescoping_closed,
        "middle_phase_cancels": middle_phase_cancels,
        "endpoint_collar_debt_formula_closed": collar_formula_closed,
        "double_awrap_same_lift_word_closed": double_awrap_word_closed,
        "moving_beatty_numerator_obstruction_confirmed": endpoint_normal_form_closed,
        "right_tail_final_negative_run_endpoint_collar_reduction_closed": reduction_closed,
        "terminal_double_awrap_endpoint_collar_payment_law_proved": False,
        "admissible_trace_or_typeii_family_constructed": False,
        "finite_group_orbit_expansion_family_constructed": False,
        "phi_lpf_parity_barrier_globally_broken": False,
        "row_column_unconditional_closed": False,
        "latest_open_gate": latest_gate,
        "next_primary_attack_target": DOUBLE_WRAP_COLLAR_LAW,
        "gate_rows": gate_rows,
        "external_frontier_implication": {
            "trace_kloosterman_typeii": (
                "The two-edge final collar is too local for direct averaged trace/Kloosterman or "
                "Type-II input; one must first aggregate terminal double-Awrap collars into an "
                "admissible moving-denominator family."
            ),
            "finite_group_orbit": (
                "The path q=461->463->467 gives a deterministic collar orbit segment, not yet "
                "a finite-group expansion family with spectral gap."
            ),
        },
        "plain_conclusion": (
            "The final right-tail excess is exactly a two-edge terminal endpoint-collar wrap debt: "
            "179065/215287 = 417/461 - 34/467 = 1 - 44/461 - 34/467.  The remaining open task is "
            "a uniform payment or exclusion law for terminal double-Awrap endpoint collars."
        ),
        "source_hashes": source_hashes(),
    }


def render_markdown(payload: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF right-tail final negative-run endpoint-collar 证书",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['verified_date']}`",
        "",
        "本证书把上一层唯一 final negative tail 继续压成两步 endpoint-collar wrap debt。",
        "",
        "```text",
        f"atom_key={payload['atom_key']}",
        f"q_path={payload['q_path']}",
        f"A_path={payload['A_path']}",
        f"D_path={payload['D_path']}",
        f"q_gap_path={payload['q_gap_path']}",
        f"carry_path={payload['carry_path']}",
        f"two_edge_sum_matches_variation_and_tail={fmt_bool(payload['two_edge_sum_matches_variation_and_tail'])}",
        f"endpoint_telescoping_closed={fmt_bool(payload['endpoint_telescoping_closed'])}",
        f"middle_phase_cancels={fmt_bool(payload['middle_phase_cancels'])}",
        f"endpoint_collar_debt_formula_closed={fmt_bool(payload['endpoint_collar_debt_formula_closed'])}",
        f"double_awrap_same_lift_word_closed={fmt_bool(payload['double_awrap_same_lift_word_closed'])}",
        f"right_tail_final_negative_run_endpoint_collar_reduction_closed={fmt_bool(payload['right_tail_final_negative_run_endpoint_collar_reduction_closed'])}",
        f"terminal_double_awrap_endpoint_collar_payment_law_proved={fmt_bool(payload['terminal_double_awrap_endpoint_collar_payment_law_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(payload['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. exact endpoint identities",
        "",
        "| quantity | value |",
        "| --- | --- |",
        f"| `final_tail_mass` | {render_fraction(payload['final_tail_mass'])} |",
        f"| `transition_signed_delta_sum` | {render_fraction(payload['transition_signed_delta_sum'])} |",
        f"| `endpoint_drop_signed` | {render_fraction(payload['endpoint_drop_signed'])} |",
        f"| `left_collar_start_D_over_q` | {render_fraction(payload['left_collar_start_D_over_q'])} |",
        f"| `right_collar_end_A_over_q` | {render_fraction(payload['right_collar_end_A_over_q'])} |",
        f"| `endpoint_collar_formula_tail` | {render_fraction(payload['endpoint_collar_formula_tail'])} |",
        "",
        "核心恒等式：",
        "",
        "```text",
        "179065/215287 = 417/461 - 34/467 = 1 - 44/461 - 34/467",
        "```",
        "",
        "## 2. two-edge turn word",
        "",
        "| edge | signed delta | word |",
        "| ---: | --- | --- |",
    ]
    for index, (delta, word) in enumerate(zip(payload["transition_signed_deltas"], payload["phase_turn_words"])):
        lines.append(f"| {index} | {render_fraction(delta)} | `{cell(word)}` |")
    lines.extend(
        [
            "",
            "## 3. 门控表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for row in payload["gate_rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=cell(row["gate"]),
                closed=fmt_bool(row["closed"]),
                proved=fmt_bool(row["proved"]),
                meaning=cell(row["meaning"]),
                remaining=cell(row["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 最新开放口",
            "",
            "```text",
            payload["latest_open_gate"],
            "```",
            "",
            "## 5. 外部前沿含义",
            "",
            "- trace/Kloosterman/Type-II：两步 collar 太局部，必须先聚合成 admissible moving-denominator family。",
            "- finite-group orbit：当前只是确定性 collar orbit segment，还没有 spectral-gap orbit family。",
            "",
            "## 6. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in sorted(payload["source_hashes"].items()):
        lines.append(f"| `{path}` | `{digest}` |")
    lines.extend(["", "行/列命题仍未无条件闭合。", ""])
    return "\n".join(lines)


def write_outputs(payload: dict[str, Any]) -> None:
    """写出 JSON、ledger 与 Markdown。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    text = json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True)
    OUT_LEDGER.write_text(text + "\n", encoding="utf-8")
    OUT_JSON.write_text(text + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(payload), encoding="utf-8")


def main() -> None:
    """命令入口。"""
    payload = build_certificate()
    write_outputs(payload)
    print(
        "right_tail_final_negative_run_endpoint_collar_reduction_closed="
        f"{fmt_bool(payload['right_tail_final_negative_run_endpoint_collar_reduction_closed'])}"
    )
    print(f"endpoint_collar_debt_formula_closed={fmt_bool(payload['endpoint_collar_debt_formula_closed'])}")
    print(f"row_column_unconditional_closed={fmt_bool(payload['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
