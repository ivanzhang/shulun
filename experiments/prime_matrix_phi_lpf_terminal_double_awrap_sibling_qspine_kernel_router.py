#!/usr/bin/env python3
"""审计 terminal double-Awrap collar 是否降为 sibling q-spine P-scaled kernel。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_terminal_double_awrap_sibling_qspine_kernel_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-terminal-double-awrap-sibling-qspine-kernel-router.json

上一层把 m773 final tail 压成两步 endpoint collar。本层继续把它与同 packet 的
paid sibling m769 对齐。两个 selected-terminal sibling 共享
q_path=[461,463,467] 与同一 double-Awrap turn word，而 m769 的 tail return 已由
new residual 精确支付。剩余 m773 tail 可写成 P-scaled q-spine 三分母核：

  179065/215287
    = 123221/205013 + 36420/202379 + 10926/215287
    = P * (203/(439*467) + 60/(439*461) + 18/(461*467)).

这不是无条件闭合；它把 terminal collar payment 门降为统一 sibling q-spine
kernel payment/exclusion 或 PDEC。
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

SLUG = "prime-matrix-phi-lpf-terminal-double-awrap-sibling-qspine-kernel"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

ENDPOINT_JSON = DOCS / "prime-matrix-phi-lpf-right-tail-final-negative-run-endpoint-collar-router.json"
TAIL_ALIGNMENT_JSON = DOCS / "prime-matrix-phi-lpf-terminal-boundary-new-residual-tail-alignment-router.json"
SOURCE_PARTITION_JSON = DOCS / "prime-matrix-phi-lpf-terminal-source-key-obstruction-partition-router.json"
TURN_JSON = DOCS / (
    "prime-matrix-phi-lpf-dominant-sign-word-repeated-step-packet-enclosure-"
    "terminal-phase-turn-word-audit.json"
)
VARIATION_JSON = DOCS / (
    "prime-matrix-phi-lpf-dominant-sign-word-repeated-step-packet-enclosure-"
    "terminal-phase-variation-budget-audit.json"
)

PIVOT_LAW = "BridgeRootQSpinePivotEnclosureLawOrPDEC"
SIBLING_KERNEL_LAW = "TerminalDoubleAwrapSiblingQSpineKernelPaymentOrPDEC"
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
    paths = [Path(__file__).resolve(), ENDPOINT_JSON, TAIL_ALIGNMENT_JSON, SOURCE_PARTITION_JSON, TURN_JSON, VARIATION_JSON]
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


def atom_key(m: int) -> str:
    """right selected-terminal atom key。"""
    return f"right:1887:selected_terminal:m{m}"


def find_turn_profile(payload: dict[str, Any], m: int) -> dict[str, Any]:
    """定位 selected-terminal turn profile。"""
    for row in payload["finite_audit"]["atom_phase_turn_profiles"]:
        if row.get("P") == 607 and row.get("m") == m and row.get("role") == "selected_terminal":
            return row
    raise ValueError(f"turn profile not found for m={m}")


def find_variation_profile(payload: dict[str, Any], m: int) -> dict[str, Any]:
    """定位 selected-terminal variation profile。"""
    for row in payload["finite_audit"]["atom_variation_profiles"]:
        if row.get("P") == 607 and row.get("m") == m and row.get("role") == "selected_terminal":
            return row
    raise ValueError(f"variation profile not found for m={m}")


def final_two_edge_signature(turn_profile: dict[str, Any]) -> dict[str, Any]:
    """提取最后两步 terminal collar signature。"""
    transitions = turn_profile["phase_turn_transitions"][-2:]
    q_path = [int(transitions[0]["q"]), int(transitions[1]["q"]), int(transitions[1]["q_next"])]
    a_path = [int(transitions[0]["A"]), int(transitions[1]["A"]), int(transitions[1]["A_next"])]
    d_path = [int(transitions[0]["D"]), int(transitions[1]["D"]), int(transitions[1]["D_next"])]
    words = [row["phase_turn_word"] for row in transitions]
    return {
        "q_path": q_path,
        "A_path": a_path,
        "D_path": d_path,
        "q_gap_path": [int(row["q_gap"]) for row in transitions],
        "carry_path": [int(row["carry_formula"]) for row in transitions],
        "words": words,
    }


def final_negative_mass(variation_profile: dict[str, Any]) -> Fraction:
    """恢复 final run negative variation。"""
    return frac_from_record(variation_profile["run_variation_rows"][-1]["negative_variation"])


def find_paid_tail_alignment(payload: dict[str, Any], m: int) -> dict[str, Any]:
    """定位 paid sibling tail alignment row。"""
    for row in payload["tail_alignment_rows"]:
        if row.get("atom_key") == atom_key(m) and row.get("matched") is True:
            return row
    raise ValueError(f"paid tail alignment not found for m={m}")


def find_internal_survivor_unit(payload: dict[str, Any], m: int) -> dict[str, Any]:
    """定位 m 的 internal survivor unit。"""
    for row in payload["survivor_partition_rows"]:
        if row.get("atom_key") == atom_key(m) and row.get("survivor_type") == "internal_survivor":
            return row
    raise ValueError(f"internal survivor not found for m={m}")


def p_scaled_coefficient(value: Fraction, p: int) -> int | None:
    """若分子可写为 P 倍整数，返回该整数。"""
    if value.numerator % p != 0:
        return None
    return value.numerator // p


def build_certificate() -> dict[str, Any]:
    """组装 sibling q-spine kernel 证书。"""
    endpoint = load_json(ENDPOINT_JSON)
    tail_alignment = load_json(TAIL_ALIGNMENT_JSON)
    source_partition = load_json(SOURCE_PARTITION_JSON)
    turn = load_json(TURN_JSON)
    variation = load_json(VARIATION_JSON)

    p = 607
    sibling_m = 769
    target_m = 773
    sibling_turn = find_turn_profile(turn, sibling_m)
    target_turn = find_turn_profile(turn, target_m)
    sibling_sig = final_two_edge_signature(sibling_turn)
    target_sig = final_two_edge_signature(target_turn)
    sibling_variation = find_variation_profile(variation, sibling_m)
    target_variation = find_variation_profile(variation, target_m)
    sibling_final_mass = final_negative_mass(sibling_variation)
    target_final_mass = final_negative_mass(target_variation)
    paid_row = find_paid_tail_alignment(tail_alignment, sibling_m)
    paid_sibling_tail = frac_from_record(paid_row["tail_mass"])
    internal_row = find_internal_survivor_unit(source_partition, target_m)
    internal_unit = frac_from_record(internal_row["mass"])

    sibling_final_minus_paid = sibling_final_mass - paid_sibling_tail
    sibling_endpoint_offset = target_final_mass - sibling_final_mass
    target_after_paid = target_final_mass - paid_sibling_tail
    endpoint_unit = Fraction(internal_unit.numerator, target_final_mass.denominator)

    same_q_path = sibling_sig["q_path"] == target_sig["q_path"] == endpoint["q_path"]
    same_turn_words = sibling_sig["words"] == target_sig["words"] == endpoint["phase_turn_words"]
    same_gap_carry = (
        sibling_sig["q_gap_path"] == target_sig["q_gap_path"] == endpoint["q_gap_path"]
        and sibling_sig["carry_path"] == target_sig["carry_path"] == endpoint["carry_path"]
    )
    paid_sibling_tail_closed = (
        tail_alignment.get("new_residual_tail_alignment_partial_closed") is True
        and int(paid_row["tail_q_start"]) == 461
        and int(paid_row["tail_q_end"]) == 467
    )
    sibling_gap_is_ten_internal_units = sibling_final_minus_paid == 10 * internal_unit
    endpoint_offset_is_three_endpoint_units = sibling_endpoint_offset == 3 * endpoint_unit
    target_kernel_identity = (
        target_final_mass == paid_sibling_tail + sibling_final_minus_paid + sibling_endpoint_offset
    )
    p_scaled_kernel_identity = target_final_mass == (
        Fraction(p * 203, 439 * 467)
        + Fraction(p * 60, 439 * 461)
        + Fraction(p * 18, 461 * 467)
    )
    all_kernel_numerators_p_scaled = all(
        p_scaled_coefficient(value, p) is not None
        for value in [target_final_mass, sibling_final_mass, paid_sibling_tail, sibling_final_minus_paid, sibling_endpoint_offset]
    )
    reduction_closed = all(
        [
            endpoint.get("right_tail_final_negative_run_endpoint_collar_reduction_closed") is True,
            same_q_path,
            same_turn_words,
            same_gap_carry,
            paid_sibling_tail_closed,
            sibling_gap_is_ten_internal_units,
            endpoint_offset_is_three_endpoint_units,
            target_kernel_identity,
            p_scaled_kernel_identity,
            all_kernel_numerators_p_scaled,
        ]
    )

    latest_open_gate = (
        f"{PIVOT_LAW} AND {SIBLING_KERNEL_LAW} AND {MASS_RATIO_LAW} AND "
        f"{ORIENTATION_LAW} AND {MOVING_BEATTY_SAVING} AND {TRACE_FAMILY} AND {GROUP_ORBIT_INPUT}"
    )
    return {
        "certificate_type": "prime_matrix_phi_lpf_terminal_double_awrap_sibling_qspine_kernel_router",
        "status": "terminal_double_awrap_sibling_qspine_kernel_closed_payment_law_open",
        "verified_date": "2026-05-25",
        "previous_endpoint_collar_reduction_closed": endpoint.get(
            "right_tail_final_negative_run_endpoint_collar_reduction_closed"
        )
        is True,
        "P": p,
        "sibling_atom_key": atom_key(sibling_m),
        "target_atom_key": atom_key(target_m),
        "sibling_m": sibling_m,
        "target_m": target_m,
        "sibling_signature": sibling_sig,
        "target_signature": target_sig,
        "same_q_path": same_q_path,
        "same_turn_words": same_turn_words,
        "same_gap_carry": same_gap_carry,
        "paid_sibling_tail_closed": paid_sibling_tail_closed,
        "target_final_tail_mass": frac_record(target_final_mass),
        "sibling_final_collar_mass": frac_record(sibling_final_mass),
        "paid_sibling_tail_mass": frac_record(paid_sibling_tail),
        "target_internal_survivor_unit": frac_record(internal_unit),
        "endpoint_unit_same_numerator": frac_record(endpoint_unit),
        "sibling_final_minus_paid": frac_record(sibling_final_minus_paid),
        "sibling_endpoint_offset": frac_record(sibling_endpoint_offset),
        "target_after_paid_sibling_tail": frac_record(target_after_paid),
        "sibling_gap_is_ten_internal_units": sibling_gap_is_ten_internal_units,
        "endpoint_offset_is_three_endpoint_units": endpoint_offset_is_three_endpoint_units,
        "target_kernel_identity_closed": target_kernel_identity,
        "p_scaled_kernel_identity_closed": p_scaled_kernel_identity,
        "all_kernel_numerators_p_scaled": all_kernel_numerators_p_scaled,
        "p_scaled_coefficients": {
            "target_final_tail": p_scaled_coefficient(target_final_mass, p),
            "sibling_final_collar": p_scaled_coefficient(sibling_final_mass, p),
            "paid_sibling_tail": p_scaled_coefficient(paid_sibling_tail, p),
            "sibling_final_minus_paid": p_scaled_coefficient(sibling_final_minus_paid, p),
            "sibling_endpoint_offset": p_scaled_coefficient(sibling_endpoint_offset, p),
        },
        "qspine_kernel_formula": {
            "target": "179065/215287",
            "decomposition": "123221/205013 + 36420/202379 + 10926/215287",
            "p_scaled": "607*(203/(439*467) + 60/(439*461) + 18/(461*467))",
            "normalized": "295/(461*467) = 203/(439*467) + 60/(439*461) + 18/(461*467)",
        },
        "terminal_double_awrap_sibling_qspine_kernel_closed": reduction_closed,
        "terminal_double_awrap_sibling_qspine_kernel_payment_law_proved": False,
        "admissible_trace_or_typeii_family_constructed": False,
        "finite_group_orbit_expansion_family_constructed": False,
        "phi_lpf_parity_barrier_globally_broken": False,
        "row_column_unconditional_closed": False,
        "latest_open_gate": latest_open_gate,
        "next_primary_attack_target": SIBLING_KERNEL_LAW,
        "gate_rows": [
            {
                "gate": "SiblingDoubleAwrapSignatureMatched",
                "closed": same_q_path and same_turn_words and same_gap_carry,
                "proved": same_q_path and same_turn_words and same_gap_carry,
                "meaning": "m769 and m773 share q-path, gap/carry path, and terminal double-Awrap turn words.",
                "remaining": "finite turn-word ledger",
            },
            {
                "gate": "PaidSiblingTailImported",
                "closed": paid_sibling_tail_closed,
                "proved": paid_sibling_tail_closed,
                "meaning": "m769 terminal tail is already paid by new-residual tail alignment.",
                "remaining": "finite tail-alignment ledger",
            },
            {
                "gate": "InternalUnitScalingIdentity",
                "closed": sibling_gap_is_ten_internal_units,
                "proved": sibling_gap_is_ten_internal_units,
                "meaning": "m769 final collar minus paid tail equals ten copies of the m773 internal survivor unit.",
                "remaining": "finite rational identity",
            },
            {
                "gate": "EndpointOffsetUnitIdentity",
                "closed": endpoint_offset_is_three_endpoint_units,
                "proved": endpoint_offset_is_three_endpoint_units,
                "meaning": "m773 minus m769 final collar equals three copies of the same numerator over the final endpoint denominator.",
                "remaining": "finite rational identity",
            },
            {
                "gate": "PScaledQSpineKernelIdentity",
                "closed": reduction_closed,
                "proved": reduction_closed,
                "meaning": "the target final tail is a P-scaled three-denominator q-spine kernel.",
                "remaining": "finite q-spine kernel ledger",
            },
            {
                "gate": "SiblingQSpineKernelPaymentLaw",
                "closed": False,
                "proved": False,
                "meaning": "a uniform law must pay or exclude this P-scaled sibling q-spine kernel.",
                "remaining": SIBLING_KERNEL_LAW,
            },
            {
                "gate": "RowColumnUnconditionalClosureReached",
                "closed": False,
                "proved": False,
                "meaning": "this is a finite sibling-kernel reduction, not a global parity-breaking theorem.",
                "remaining": f"{PIVOT_LAW} AND {MASS_RATIO_LAW} AND {ORIENTATION_LAW} AND {MOVING_BEATTY_SAVING}",
            },
        ],
        "plain_conclusion": (
            "The m773 terminal double-Awrap debt is not an isolated endpoint collar: it equals the already-paid "
            "m769 sibling tail plus a P-scaled q-spine kernel, namely "
            "179065/215287 = 123221/205013 + 36420/202379 + 10926/215287.  The open task is a uniform "
            "payment/exclusion law for this sibling q-spine kernel or a named PDEC."
        ),
        "source_hashes": source_hashes(),
    }


def render_markdown(payload: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF terminal double-Awrap sibling q-spine kernel 证书",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['verified_date']}`",
        "",
        "本证书把 m773 terminal double-Awrap endpoint collar 与已支付 sibling m769 对齐。",
        "",
        "```text",
        f"sibling_atom_key={payload['sibling_atom_key']}",
        f"target_atom_key={payload['target_atom_key']}",
        f"q_path={payload['target_signature']['q_path']}",
        f"same_q_path={fmt_bool(payload['same_q_path'])}",
        f"same_turn_words={fmt_bool(payload['same_turn_words'])}",
        f"same_gap_carry={fmt_bool(payload['same_gap_carry'])}",
        f"paid_sibling_tail_closed={fmt_bool(payload['paid_sibling_tail_closed'])}",
        f"sibling_gap_is_ten_internal_units={fmt_bool(payload['sibling_gap_is_ten_internal_units'])}",
        f"endpoint_offset_is_three_endpoint_units={fmt_bool(payload['endpoint_offset_is_three_endpoint_units'])}",
        f"target_kernel_identity_closed={fmt_bool(payload['target_kernel_identity_closed'])}",
        f"p_scaled_kernel_identity_closed={fmt_bool(payload['p_scaled_kernel_identity_closed'])}",
        f"terminal_double_awrap_sibling_qspine_kernel_closed={fmt_bool(payload['terminal_double_awrap_sibling_qspine_kernel_closed'])}",
        f"terminal_double_awrap_sibling_qspine_kernel_payment_law_proved={fmt_bool(payload['terminal_double_awrap_sibling_qspine_kernel_payment_law_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(payload['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. q-spine kernel identity",
        "",
        "```text",
        payload["qspine_kernel_formula"]["target"],
        f"= {payload['qspine_kernel_formula']['decomposition']}",
        f"= {payload['qspine_kernel_formula']['p_scaled']}",
        payload["qspine_kernel_formula"]["normalized"],
        "```",
        "",
        "## 2. exact masses",
        "",
        "| quantity | value | P-scaled coefficient |",
        "| --- | --- | ---: |",
        f"| `target_final_tail_mass` | {render_fraction(payload['target_final_tail_mass'])} | {payload['p_scaled_coefficients']['target_final_tail']} |",
        f"| `sibling_final_collar_mass` | {render_fraction(payload['sibling_final_collar_mass'])} | {payload['p_scaled_coefficients']['sibling_final_collar']} |",
        f"| `paid_sibling_tail_mass` | {render_fraction(payload['paid_sibling_tail_mass'])} | {payload['p_scaled_coefficients']['paid_sibling_tail']} |",
        f"| `sibling_final_minus_paid` | {render_fraction(payload['sibling_final_minus_paid'])} | {payload['p_scaled_coefficients']['sibling_final_minus_paid']} |",
        f"| `sibling_endpoint_offset` | {render_fraction(payload['sibling_endpoint_offset'])} | {payload['p_scaled_coefficients']['sibling_endpoint_offset']} |",
        f"| `target_internal_survivor_unit` | {render_fraction(payload['target_internal_survivor_unit'])} | 6 |",
        f"| `endpoint_unit_same_numerator` | {render_fraction(payload['endpoint_unit_same_numerator'])} | 6 |",
        "",
        "## 3. shared terminal words",
        "",
        "| atom | A path | D path | words |",
        "| --- | --- | --- | --- |",
        f"| `{payload['sibling_atom_key']}` | `{payload['sibling_signature']['A_path']}` | `{payload['sibling_signature']['D_path']}` | `{cell(payload['sibling_signature']['words'])}` |",
        f"| `{payload['target_atom_key']}` | `{payload['target_signature']['A_path']}` | `{payload['target_signature']['D_path']}` | `{cell(payload['target_signature']['words'])}` |",
        "",
        "## 4. 门控表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
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
            "## 5. 最新开放口",
            "",
            "```text",
            payload["latest_open_gate"],
            "```",
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
        "terminal_double_awrap_sibling_qspine_kernel_closed="
        f"{fmt_bool(payload['terminal_double_awrap_sibling_qspine_kernel_closed'])}"
    )
    print(f"p_scaled_kernel_identity_closed={fmt_bool(payload['p_scaled_kernel_identity_closed'])}")
    print(f"row_column_unconditional_closed={fmt_bool(payload['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
