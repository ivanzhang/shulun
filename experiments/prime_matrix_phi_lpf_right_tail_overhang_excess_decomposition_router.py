#!/usr/bin/env python3
"""审计唯一 right-tail overhang 是否等于 m773 负变差超额的剩余部分。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_right_tail_overhang_excess_decomposition_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-right-tail-overhang-excess-decomposition-router.json

输出：
  data/prime-matrix-phi-lpf-right-tail-overhang-excess-decomposition-ledger.json
  docs/monograph/prime-matrix-phi-lpf-right-tail-overhang-excess-decomposition-router.json
  docs/monograph/prime-matrix-phi-lpf-right-tail-overhang-excess-decomposition-router.md

本层承接 bulk carry-chain 与 old-residual return alignment。它把唯一的
RightSelectedTerminalTailOverhangPDEC 从匿名尾段压成：

    m773 selected-terminal negative excess
      = internal survivor return + final negative tail overhang.

internal survivor 已在 old-side return 中支付，因此剩余 tail 是 final negative
run excess payment/PDEC，而不是一个独立的未知残差池。
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

SLUG = "prime-matrix-phi-lpf-right-tail-overhang-excess-decomposition"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

VARIATION_JSON = DOCS / (
    "prime-matrix-phi-lpf-dominant-sign-word-repeated-step-packet-enclosure-"
    "terminal-phase-variation-budget-audit.json"
)
PARTITION_JSON = DOCS / "prime-matrix-phi-lpf-terminal-source-key-obstruction-partition-router.json"
OLD_RETURN_JSON = DOCS / "prime-matrix-phi-lpf-terminal-boundary-old-residual-return-alignment-router.json"
BULK_JSON = DOCS / "prime-matrix-phi-lpf-terminal-boundary-bulk-carry-chain-normal-form-router.json"
PIVOT_JSON = DOCS / "prime-matrix-phi-lpf-terminal-boundary-bridge-root-qspine-pivot-enclosure-router.json"

PIVOT_LAW = "BridgeRootQSpinePivotEnclosureLawOrPDEC"
TAIL_FINAL_LAW = "RightSelectedTerminalFinalNegativeRunExcessPaymentOrPDEC"
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
    paths = [Path(__file__).resolve(), VARIATION_JSON, PARTITION_JSON, OLD_RETURN_JSON, BULK_JSON, PIVOT_JSON]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def frac_from_record(record: dict[str, Any]) -> Fraction:
    """从 JSON 分数记录恢复 Fraction。"""
    return Fraction(int(record["numerator"]), int(record["denominator"]))


def frac_record(value: Fraction) -> dict[str, Any]:
    """稳定输出分数。"""
    return {
        "fraction": f"{value.numerator}/{value.denominator}",
        "decimal": f"{float(value):.12f}",
        "numerator": value.numerator,
        "denominator": value.denominator,
    }


def fmt_bool(value: Any) -> str:
    """布尔值小写渲染。"""
    return "true" if bool(value) else "false"


def cell(value: Any) -> str:
    """Markdown 表格单元转义。"""
    return str(value).replace("|", r"\|")


def render_fraction(record: dict[str, Any]) -> str:
    """表格用分数摘要。"""
    return f"{record['decimal']} ({record['fraction']})"


def find_m773_profile(variation_payload: dict[str, Any]) -> dict[str, Any]:
    """定位 right:1887 selected-terminal m773 的变差 profile。"""
    for row in variation_payload["finite_audit"]["atom_variation_profiles"]:
        if row.get("P") == 607 and row.get("m") == 773 and row.get("role") == "selected_terminal":
            return row
    raise ValueError("m773 selected-terminal variation profile not found")


def find_survivors(partition_payload: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any]]:
    """定位 m773 的 internal survivor 与 tail survivor。"""
    internal = None
    tail = None
    for row in partition_payload["survivor_partition_rows"]:
        if row["atom_key"] != "right:1887:selected_terminal:m773":
            continue
        if row["survivor_type"] == "internal_survivor":
            internal = row
        if row["survivor_type"] == "tail_survivor":
            tail = row
    if internal is None or tail is None:
        raise ValueError("m773 internal/tail survivor rows not found")
    return internal, tail


def find_final_run(profile: dict[str, Any]) -> dict[str, Any]:
    """定位 m773 的最终 run。"""
    return max(profile["run_variation_rows"], key=lambda row: int(row["run_id"]))


def build_certificate() -> dict[str, Any]:
    """组装 right-tail overhang excess decomposition 证书。"""
    variation_payload = load_json(VARIATION_JSON)
    partition_payload = load_json(PARTITION_JSON)
    old_return_payload = load_json(OLD_RETURN_JSON)
    bulk_payload = load_json(BULK_JSON)
    pivot_payload = load_json(PIVOT_JSON)

    profile = find_m773_profile(variation_payload)
    internal_row, tail_row = find_survivors(partition_payload)
    final_run = find_final_run(profile)

    negative_excess = frac_from_record(profile["negative_variation_excess"])
    internal_mass = frac_from_record(internal_row["mass"])
    tail_mass = frac_from_record(tail_row["mass"])
    final_run_negative_variation = frac_from_record(final_run["negative_variation"])
    final_run_signed_delta = frac_from_record(final_run["signed_delta"])
    final_run_tail_matches = (
        int(final_run["run_id"]) == int(tail_row["run_id"])
        and int(final_run["q_start"]) == int(tail_row["q_start"])
        and int(final_run["q_end"]) == int(tail_row["q_end"])
        and final_run_negative_variation == tail_mass
        and final_run["direction"] == "negative"
    )
    internal_paid = (
        old_return_payload.get("old_residual_return_alignment_closed") is True
        and old_return_payload.get("internal_survivor_return_count") == 1
        and frac_from_record(old_return_payload["internal_survivor_mass_total"]) == internal_mass
    )
    excess_decomposition_closed = negative_excess == internal_mass + tail_mass
    residual_after_internal = negative_excess - internal_mass
    tail_is_residual_after_internal = residual_after_internal == tail_mass
    reduction_closed = (
        partition_payload.get("source_key_obstruction_partition_closed") is True
        and bulk_payload.get("bulk_carry_chain_normal_form_closed") is True
        and pivot_payload.get("bridge_root_qspine_pivot_enclosure_reduction_closed") is True
        and final_run_tail_matches
        and internal_paid
        and excess_decomposition_closed
        and tail_is_residual_after_internal
    )
    latest_gate = (
        f"{PIVOT_LAW} AND {TAIL_FINAL_LAW} AND {MASS_RATIO_LAW} AND {ORIENTATION_LAW} "
        f"AND {MOVING_BEATTY_SAVING} AND {TRACE_FAMILY} AND {GROUP_ORBIT_INPUT}"
    )
    return {
        "certificate_type": "prime_matrix_phi_lpf_right_tail_overhang_excess_decomposition_router",
        "status": "right_tail_overhang_excess_decomposition_closed_final_payment_law_open",
        "verified_date": "2026-05-25",
        "previous_source_key_obstruction_partition_closed": partition_payload.get(
            "source_key_obstruction_partition_closed"
        )
        is True,
        "previous_old_residual_return_alignment_closed": old_return_payload.get(
            "old_residual_return_alignment_closed"
        )
        is True,
        "previous_bulk_carry_chain_normal_form_closed": bulk_payload.get(
            "bulk_carry_chain_normal_form_closed"
        )
        is True,
        "previous_pivot_enclosure_reduction_closed": pivot_payload.get(
            "bridge_root_qspine_pivot_enclosure_reduction_closed"
        )
        is True,
        "atom_key": "right:1887:selected_terminal:m773",
        "P": profile["P"],
        "m": profile["m"],
        "role": profile["role"],
        "negative_variation_excess": profile["negative_variation_excess"],
        "internal_survivor_mass": internal_row["mass"],
        "tail_overhang_mass": tail_row["mass"],
        "residual_after_internal_return": frac_record(residual_after_internal),
        "negative_excess_equals_internal_plus_tail": excess_decomposition_closed,
        "tail_overhang_equals_excess_after_internal_return": tail_is_residual_after_internal,
        "internal_survivor_old_return_paid": internal_paid,
        "final_run_tail_matches": final_run_tail_matches,
        "final_run": {
            "run_id": final_run["run_id"],
            "direction": final_run["direction"],
            "q_start": final_run["q_start"],
            "q_end": final_run["q_end"],
            "length": final_run["length"],
            "A_wrap_count": final_run["A_wrap_count"],
            "D_wrap_count": final_run["D_wrap_count"],
            "carry_min": final_run["carry_min"],
            "carry_max": final_run["carry_max"],
            "signed_delta": final_run["signed_delta"],
            "negative_variation": final_run["negative_variation"],
        },
        "internal_survivor_row": {
            "run_id": internal_row["run_id"],
            "q_start": internal_row["q_start"],
            "q_end": internal_row["q_end"],
            "direction": internal_row["direction"],
            "mass": internal_row["mass"],
            "survivor_type": internal_row["survivor_type"],
        },
        "tail_survivor_row": {
            "run_id": tail_row["run_id"],
            "q_start": tail_row["q_start"],
            "q_end": tail_row["q_end"],
            "direction": tail_row["direction"],
            "mass": tail_row["mass"],
            "survivor_type": tail_row["survivor_type"],
        },
        "right_tail_overhang_excess_decomposition_closed": reduction_closed,
        "right_tail_final_negative_run_payment_law_proved": False,
        "right_tail_overhang_pdec_constructed": False,
        "admissible_trace_or_typeii_family_constructed": False,
        "finite_group_orbit_expansion_family_constructed": False,
        "phi_lpf_parity_barrier_globally_broken": False,
        "row_column_unconditional_closed": False,
        "latest_open_gate": latest_gate,
        "next_primary_attack_target": TAIL_FINAL_LAW,
        "gate_rows": [
            {
                "gate": "M773NegativeExcessDecomposition",
                "closed": reduction_closed,
                "proved": reduction_closed,
                "meaning": "m773 selected-terminal negative excess equals internal survivor return plus final tail overhang.",
                "remaining": "finite excess decomposition ledger",
            },
            {
                "gate": "InternalSurvivorAlreadyPaid",
                "closed": internal_paid,
                "proved": internal_paid,
                "meaning": "the internal survivor part is already matched by old-residual return alignment.",
                "remaining": "none for internal survivor payment",
            },
            {
                "gate": "FinalNegativeRunTailIdentification",
                "closed": final_run_tail_matches,
                "proved": final_run_tail_matches,
                "meaning": "the unmatched tail is exactly the final negative run q=461->467 of m773.",
                "remaining": "finite final-run identification",
            },
            {
                "gate": "RightTailFinalNegativeRunPaymentLaw",
                "closed": False,
                "proved": False,
                "meaning": "a uniform law must pay or exclude such final negative tail excess.",
                "remaining": TAIL_FINAL_LAW,
            },
            {
                "gate": "RowColumnUnconditionalClosureReached",
                "closed": False,
                "proved": False,
                "meaning": "this is a finite decomposition, not a global parity-breaking theorem.",
                "remaining": f"{PIVOT_LAW} AND {MASS_RATIO_LAW} AND {ORIENTATION_LAW} AND {MOVING_BEATTY_SAVING}",
            },
        ],
        "plain_conclusion": (
            "The only right selected-terminal tail overhang is not an independent residual pool: "
            "for m773, selected-terminal negative excess equals the already-paid internal survivor "
            "plus the final negative run q=461->467.  The remaining open task is a uniform final "
            "negative-tail payment law or a named PDEC/LocalSurvivor return."
        ),
        "source_hashes": source_hashes(),
    }


def render_markdown(payload: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF right-tail overhang excess decomposition 证书",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['verified_date']}`",
        "",
        "本证书把唯一 right-tail overhang 压成 m773 selected-terminal 负变差超额的剩余部分。",
        "",
        "```text",
        f"atom_key={payload['atom_key']}",
        f"negative_excess_equals_internal_plus_tail={fmt_bool(payload['negative_excess_equals_internal_plus_tail'])}",
        f"tail_overhang_equals_excess_after_internal_return={fmt_bool(payload['tail_overhang_equals_excess_after_internal_return'])}",
        f"internal_survivor_old_return_paid={fmt_bool(payload['internal_survivor_old_return_paid'])}",
        f"final_run_tail_matches={fmt_bool(payload['final_run_tail_matches'])}",
        f"right_tail_overhang_excess_decomposition_closed={fmt_bool(payload['right_tail_overhang_excess_decomposition_closed'])}",
        f"right_tail_final_negative_run_payment_law_proved={fmt_bool(payload['right_tail_final_negative_run_payment_law_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(payload['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. exact decomposition",
        "",
        "| quantity | value |",
        "| --- | --- |",
        f"| `negative_variation_excess` | {render_fraction(payload['negative_variation_excess'])} |",
        f"| `internal_survivor_mass` | {render_fraction(payload['internal_survivor_mass'])} |",
        f"| `tail_overhang_mass` | {render_fraction(payload['tail_overhang_mass'])} |",
        f"| `residual_after_internal_return` | {render_fraction(payload['residual_after_internal_return'])} |",
        "",
        "## 2. final run",
        "",
        "| run | direction | q-range | length | A-wrap | D-wrap | carry | signed delta |",
        "| ---: | --- | --- | ---: | ---: | ---: | --- | --- |",
        "| {run_id} | `{direction}` | {q_start}->{q_end} | {length} | {awrap} | {dwrap} | {cmin}->{cmax} | {delta} |".format(
            run_id=payload["final_run"]["run_id"],
            direction=payload["final_run"]["direction"],
            q_start=payload["final_run"]["q_start"],
            q_end=payload["final_run"]["q_end"],
            length=payload["final_run"]["length"],
            awrap=payload["final_run"]["A_wrap_count"],
            dwrap=payload["final_run"]["D_wrap_count"],
            cmin=payload["final_run"]["carry_min"],
            cmax=payload["final_run"]["carry_max"],
            delta=render_fraction(payload["final_run"]["signed_delta"]),
        ),
        "",
        "## 3. 门控表",
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
            "## 4. 最新开放口",
            "",
            "```text",
            payload["latest_open_gate"],
            "```",
            "",
            "## 5. 依赖哈希",
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
        "right_tail_overhang_excess_decomposition_closed="
        f"{fmt_bool(payload['right_tail_overhang_excess_decomposition_closed'])}"
    )
    print(
        "tail_overhang_equals_excess_after_internal_return="
        f"{fmt_bool(payload['tail_overhang_equals_excess_after_internal_return'])}"
    )
    print(f"row_column_unconditional_closed={fmt_bool(payload['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
