#!/usr/bin/env python3
"""审计 terminal signed payload measure 与 extra variation absorption 前沿。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_terminal_signed_payload_measure_absorption_frontier_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-terminal-signed-payload-measure-absorption-frontier-router.json

输出：
  data/prime-matrix-phi-lpf-terminal-signed-payload-measure-absorption-frontier-ledger.json
  docs/monograph/prime-matrix-phi-lpf-terminal-signed-payload-measure-absorption-frontier-router.json
  docs/monograph/prime-matrix-phi-lpf-terminal-signed-payload-measure-absorption-frontier-router.md

本证书承接 terminal phase variation budget，把七个 terminal/extra fixed-m line atoms
写成一个统一的 signed payload measure mu(q,m,packet)。关键新结论是：
selected terminal 的负净超额可以覆盖 extra 的负净超额，但不能覆盖 extra 的总变差。
因此若要继续突破，必须证明 monotone-run total-to-net 压缩、强吸收，或给出
PDEC/SAE/LocalSurvivor 命名回流；不能把净超额余额误当作相位节省定理。
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

SLUG = "prime-matrix-phi-lpf-terminal-signed-payload-measure-absorption-frontier"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

VARIATION = DOCS / (
    "prime-matrix-phi-lpf-dominant-sign-word-repeated-step-packet-enclosure-"
    "terminal-phase-variation-budget-audit.json"
)
TURN_WORD = DOCS / (
    "prime-matrix-phi-lpf-dominant-sign-word-repeated-step-packet-enclosure-"
    "terminal-phase-turn-word-audit.json"
)
NORMAL_FORM = DOCS / (
    "prime-matrix-phi-lpf-dominant-sign-word-repeated-step-packet-enclosure-"
    "terminal-phase-normal-form-audit.json"
)
PARITY_SHADOW_NOGO = DOCS / "prime-matrix-phi-lpf-factor-word-parity-shadow-orientation-nogo-router.json"

PRIME_Q_PHASE = "PrimeQSupportSetReciprocalPhaseSavingBeyondParity"
MOVING_BEATTY_SAVING = "SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving"
TOTAL_TO_NET = "MonotoneRunTotalToNetCompressionOrPDEC"
EXTRA_ABSORB = "ExtraTotalVariationAbsorptionOrLocalSurvivor"
TRACE_FAMILY = "AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily"
ORIENTATION_LAW = "PrimitiveOrientationLocalFactorProductLawBeforePushforward"
BUILTIN_PAIRING = "BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """布尔值写成小写文本。"""
    return "true" if bool(value) else "false"


def cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def frac_from_record(record: dict[str, Any]) -> Fraction:
    """从证书分数记录读取 Fraction。"""
    return Fraction(int(record["numerator"]), int(record["denominator"]))


def frac_record(value: Fraction) -> dict[str, Any]:
    """稳定输出分数和小数。"""
    return {
        "fraction": f"{value.numerator}/{value.denominator}",
        "decimal": f"{float(value):.12f}",
        "numerator": value.numerator,
        "denominator": value.denominator,
    }


def transition_delta(item: dict[str, Any]) -> Fraction:
    """读取 transition 的 signed phase delta。"""
    return Fraction(int(item["phase_delta_num"]), int(item["phase_delta_den"]))


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造门控记录。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def source_hashes() -> dict[str, str]:
    """登记本层依赖哈希。"""
    paths = [
        Path(__file__).resolve(),
        VARIATION,
        TURN_WORD,
        NORMAL_FORM,
        PARITY_SHADOW_NOGO,
    ]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def profile_key(item: dict[str, Any]) -> tuple[str, int, str, int]:
    """统一 atom key。"""
    return (item["packet_side"], int(item["packet_index"]), item["role"], int(item["m"]))


def build_measure_entries(turn_payload: dict[str, Any]) -> list[dict[str, Any]]:
    """把 phase-turn transitions 写成 mu(q,m,packet) signed payload measure。"""
    entries: list[dict[str, Any]] = []
    for atom in turn_payload["finite_audit"]["atom_phase_turn_profiles"]:
        for trans in atom["phase_turn_transitions"]:
            delta = transition_delta(trans)
            entries.append(
                {
                    "packet_side": atom["packet_side"],
                    "packet_index": atom["packet_index"],
                    "role": atom["role"],
                    "P": atom["P"],
                    "m": atom["m"],
                    "q": trans["q"],
                    "q_next": trans["q_next"],
                    "q_gap": trans["q_gap"],
                    "A": trans["A"],
                    "A_next": trans["A_next"],
                    "D": trans["D"],
                    "D_next": trans["D_next"],
                    "lift": trans["lift"],
                    "lift_next": trans["lift_next"],
                    "carry": trans["carry_formula"],
                    "phase_direction": trans["phase_direction"],
                    "A_wrap": trans["A_wrap"],
                    "D_wrap": trans["D_wrap"],
                    "signed_delta": frac_record(delta),
                    "weight_sign": 1 if delta > 0 else -1 if delta < 0 else 0,
                    "transition_index": trans["transition_index"],
                }
            )
    return entries


def role_row_map(variation_payload: dict[str, Any]) -> dict[str, dict[str, Any]]:
    """按 role 取出 variation row。"""
    rows = variation_payload["finite_audit"]["role_variation_rows"]
    return {row["role"]: row for row in rows}


def atom_readiness_rows(
    variation_payload: dict[str, Any],
    normal_payload: dict[str, Any],
) -> list[dict[str, Any]]:
    """汇总每个 atom 的 readiness。"""
    variation_profiles = {
        profile_key(item): item
        for item in variation_payload["finite_audit"]["atom_variation_profiles"]
    }
    normal_profiles = {
        profile_key(item): item for item in normal_payload["finite_audit"]["phase_profiles"]
    }
    rows: list[dict[str, Any]] = []
    for key in sorted(variation_profiles):
        var = variation_profiles[key]
        norm = normal_profiles.get(key, {})
        rows.append(
            {
                "packet": f"{var['packet_side']}:{var['packet_index']}",
                "role": var["role"],
                "P": var["P"],
                "m": var["m"],
                "q_count": norm.get("q_prefix_count", var["transition_count"] + 1),
                "transitions": var["transition_count"],
                "runs": var["phase_run_count"],
                "max_run": var["phase_run_max_length"],
                "A_full_distinct": bool(norm.get("A_full_distinct", False)),
                "fixed_numerator_kloosterman_ready": bool(
                    norm.get("fixed_numerator_kloosterman_ready", False)
                ),
                "numerator_motion_class": norm.get("numerator_motion_class", "unknown"),
                "net": var["net_phase_displacement"],
                "total_variation": var["total_variation"],
                "negative_excess": var["negative_variation_excess"],
            }
        )
    return rows


def compute_absorption_metrics(variation_payload: dict[str, Any]) -> dict[str, Any]:
    """计算 selected 与 extra 的净超额/总变差吸收指标。"""
    roles = role_row_map(variation_payload)
    selected = roles["selected_terminal"]
    extra = roles["extra_shell"]
    selected_neg_excess = frac_from_record(selected["negative_variation_excess"])
    extra_neg_excess = frac_from_record(extra["negative_variation_excess"])
    extra_total = frac_from_record(extra["total_variation"])
    selected_total = frac_from_record(selected["total_variation"])
    selected_net_absorption_margin = selected_neg_excess - extra_neg_excess
    selected_strong_absorption_margin = selected_neg_excess - extra_total
    return {
        "selected_negative_excess": frac_record(selected_neg_excess),
        "extra_negative_excess": frac_record(extra_neg_excess),
        "extra_total_variation": frac_record(extra_total),
        "selected_total_variation": frac_record(selected_total),
        "net_excess_absorption_margin": frac_record(selected_net_absorption_margin),
        "strong_total_variation_absorption_margin": frac_record(
            selected_strong_absorption_margin
        ),
        "net_excess_absorption_margin_positive": selected_net_absorption_margin > 0,
        "strong_total_variation_absorption_margin_positive": selected_strong_absorption_margin > 0,
        "selected_excess_to_extra_total_ratio": frac_record(selected_neg_excess / extra_total),
        "selected_excess_to_extra_negative_excess_ratio": frac_record(
            selected_neg_excess / extra_neg_excess
        ),
    }


def schema_contract(entries: list[dict[str, Any]]) -> dict[str, Any]:
    """检查 mu(q,m,packet) schema 的字段完整性。"""
    required = [
        "packet_side",
        "packet_index",
        "role",
        "P",
        "m",
        "q",
        "q_next",
        "A",
        "A_next",
        "D",
        "D_next",
        "lift",
        "lift_next",
        "carry",
        "phase_direction",
        "signed_delta",
    ]
    missing_count = sum(1 for entry in entries for key in required if key not in entry)
    return {
        "measure_entry_count": len(entries),
        "required_field_count": len(required),
        "missing_required_field_count": missing_count,
        "schema_closed": missing_count == 0 and len(entries) == 126,
        "roles": sorted({entry["role"] for entry in entries}),
        "packets": sorted({f"{entry['packet_side']}:{entry['packet_index']}" for entry in entries}),
        "P_values": sorted({entry["P"] for entry in entries}),
        "m_values": sorted({entry["m"] for entry in entries}),
    }


def build_rows(
    variation_payload: dict[str, Any],
    normal_payload: dict[str, Any],
    parity_payload: dict[str, Any],
    schema: dict[str, Any],
    metrics: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成本层门控表。"""
    return [
        row(
            "TerminalVariationBudgetImported",
            variation_payload.get("terminal_phase_variation_budget_closed") is True,
            True,
            "terminal phase variation budget 已给出 selected 与 extra 的精确正/负变差。",
            "finite variation ledger imported",
        ),
        row(
            "MuPayloadMeasureSchemaClosed",
            schema["schema_closed"],
            True,
            "七个 terminal/extra fixed-m line atoms 已统一写成 mu(q,m,packet) transition measure。",
            "closed finite signed payload measure schema",
        ),
        row(
            "SelectedNetExcessBeatsExtraNetExcess",
            metrics["net_excess_absorption_margin_positive"],
            True,
            "selected terminal 负净超额大于 extra 负净超额；这是净账本层面的真实余量。",
            "net-level margin only",
        ),
        row(
            "SelectedNetExcessBeatsExtraTotalVariation",
            metrics["strong_total_variation_absorption_margin_positive"],
            False,
            "selected 负净超额远小于 extra 总变差，不能直接支付强吸收。",
            EXTRA_ABSORB,
        ),
        row(
            "SelectedFixedNumeratorKloostermanReady",
            normal_payload["finite_audit"].get("selected_terminal_fixed_numerator_kloosterman_ready") is True,
            False,
            "selected terminal atoms 全是 moving Beatty numerator；直接 fixed-numerator Kloosterman 输入不可用。",
            MOVING_BEATTY_SAVING,
        ),
        row(
            "ParityShadowShortcutRejected",
            parity_payload.get("factor_word_shadow_proves_orientation_local_factor_law") is False,
            True,
            "factor-word parity shadow 不能替代本层所需 signed payload 或 orientation law。",
            f"{ORIENTATION_LAW} OR {BUILTIN_PAIRING}",
        ),
        row(
            "TraceKloostermanFamilyReady",
            False,
            False,
            "mu 目前是有限 transition measure，还没有外部 trace/Kloosterman/Type-II 可求和族。",
            TRACE_FAMILY,
        ),
        row(
            "MonotoneRunTotalToNetCompressionProved",
            False,
            False,
            "要把 strong absorption 失败变成可用相消，必须证明 run 级 total-to-net 压缩或命名回流。",
            TOTAL_TO_NET,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步只关闭 payload measure schema 与吸收余量账本，没有闭合三命题。",
            f"{TOTAL_TO_NET} AND {EXTRA_ABSORB} AND {TRACE_FAMILY}",
        ),
    ]


def external_frontier_note() -> list[dict[str, str]]:
    """外部前沿输入的适配边界。"""
    return [
        {
            "input": "FKMS trace/bilinear and DI/BFI/Kuznetsov dispersion",
            "usable_after": "mu is promoted from a finite transition measure to an averaged trace family",
            "current_gap": "only two P packets and seven fixed-m atoms are present",
        },
        {
            "input": "Milicevic-Qin-Wu arbitrary-modulus Kloosterman and Wright unbalanced fractions",
            "usable_after": "moving Beatty numerator A(q)/q is completed into a summable reciprocal family",
            "current_gap": "selected atoms are moving-numerator, not fixed-numerator Kloosterman sums",
        },
        {
            "input": "Pascadi composite Type-II",
            "usable_after": "terminal line atoms are enlarged to a genuine two-dimensional Type-II rectangle",
            "current_gap": "current object is a one-dimensional prime-q prefix transition measure",
        },
    ]


def build_certificate() -> dict[str, Any]:
    """组装证书。"""
    variation_payload = load_json(VARIATION)
    turn_payload = load_json(TURN_WORD)
    normal_payload = load_json(NORMAL_FORM)
    parity_payload = load_json(PARITY_SHADOW_NOGO)
    entries = build_measure_entries(turn_payload)
    schema = schema_contract(entries)
    metrics = compute_absorption_metrics(variation_payload)
    atom_rows = atom_readiness_rows(variation_payload, normal_payload)
    rows = build_rows(variation_payload, normal_payload, parity_payload, schema, metrics)
    return {
        "certificate_type": "prime_matrix_phi_lpf_terminal_signed_payload_measure_absorption_frontier_router",
        "status": "terminal_signed_payload_measure_schema_closed_strong_absorption_open",
        "verified_date": "2026-05-25",
        "terminal_signed_payload_measure_schema_closed": schema["schema_closed"],
        "mu_transition_count": schema["measure_entry_count"],
        "selected_net_excess_beats_extra_net_excess": metrics[
            "net_excess_absorption_margin_positive"
        ],
        "selected_net_excess_beats_extra_total_variation": metrics[
            "strong_total_variation_absorption_margin_positive"
        ],
        "monotone_run_total_to_net_compression_proved": False,
        "extra_total_variation_absorption_proved": False,
        "admissible_averaged_trace_family_created": False,
        "trace_or_kloosterman_completion_ready": False,
        "selected_terminal_fixed_numerator_kloosterman_ready": normal_payload[
            "finite_audit"
        ].get("selected_terminal_fixed_numerator_kloosterman_ready")
        is True,
        "selected_terminal_moving_beatty_numerator_phase_saving_proved": False,
        "phi_lpf_parity_barrier_globally_broken": False,
        "row_column_unconditional_closed": False,
        "schema_contract": schema,
        "absorption_metrics": metrics,
        "atom_readiness_rows": atom_rows,
        "mu_entry_sample": entries[:8],
        "gate_rows": rows,
        "external_frontier_note": external_frontier_note(),
        "source_hashes": source_hashes(),
        "next_primary_attack_target": (
            f"{TOTAL_TO_NET} AND {EXTRA_ABSORB} AND "
            f"{MOVING_BEATTY_SAVING} AND {TRACE_FAMILY}"
        ),
        "retained_basis": (
            f"{PRIME_Q_PHASE} AND ({ORIENTATION_LAW} OR {BUILTIN_PAIRING}) AND "
            f"{TRACE_FAMILY}"
        ),
        "plain_conclusion": (
            "The terminal/extra phase-turn data can be packaged as a finite signed "
            "payload measure mu(q,m,packet).  The selected terminal negative net "
            "excess beats the extra negative net excess, but it does not beat the "
            "extra total variation.  Therefore the next non-cyclic step must prove "
            "a monotone-run total-to-net compression, a strong extra-variation "
            "absorption, or a named PDEC/SAE/LocalSurvivor return before any external "
            "trace/Kloosterman or Type-II theorem can be applied."
        ),
    }


def render_fraction(record: dict[str, Any]) -> str:
    """表格用分数摘要。"""
    return f"{record['decimal']} ({record['fraction']})"


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = []
    lines.append("# Prime Matrix Phi-LPF terminal signed payload measure absorption frontier 证书")
    lines.append("")
    lines.append(f"**状态：** `{result['status']}`")
    lines.append(f"**核验日期：** `{result['verified_date']}`")
    lines.append("")
    lines.append("本证书把 terminal/extra phase-turn 数据统一写成有限 signed payload measure")
    lines.append("`mu(q,m,packet)`，并检查 selected terminal 余量能否吸收 extra 变差。")
    lines.append("")
    lines.append("```text")
    for key in [
        "terminal_signed_payload_measure_schema_closed",
        "mu_transition_count",
        "selected_net_excess_beats_extra_net_excess",
        "selected_net_excess_beats_extra_total_variation",
        "monotone_run_total_to_net_compression_proved",
        "extra_total_variation_absorption_proved",
        "admissible_averaged_trace_family_created",
        "trace_or_kloosterman_completion_ready",
        "selected_terminal_fixed_numerator_kloosterman_ready",
        "row_column_unconditional_closed",
        "phi_lpf_parity_barrier_globally_broken",
    ]:
        value = result[key]
        lines.append(f"{key}={fmt_bool(value) if isinstance(value, bool) else value}")
    lines.append("```")
    lines.append("")
    lines.append("## 1. 吸收余量")
    lines.append("")
    metrics = result["absorption_metrics"]
    lines.append("```text")
    lines.append(f"selected_negative_excess={render_fraction(metrics['selected_negative_excess'])}")
    lines.append(f"extra_negative_excess={render_fraction(metrics['extra_negative_excess'])}")
    lines.append(f"extra_total_variation={render_fraction(metrics['extra_total_variation'])}")
    lines.append(f"net_excess_absorption_margin={render_fraction(metrics['net_excess_absorption_margin'])}")
    lines.append(
        "strong_total_variation_absorption_margin="
        f"{render_fraction(metrics['strong_total_variation_absorption_margin'])}"
    )
    lines.append(
        "selected_excess_to_extra_total_ratio="
        f"{render_fraction(metrics['selected_excess_to_extra_total_ratio'])}"
    )
    lines.append(
        "selected_excess_to_extra_negative_excess_ratio="
        f"{render_fraction(metrics['selected_excess_to_extra_negative_excess_ratio'])}"
    )
    lines.append("```")
    lines.append("")
    lines.append("结论：净超额吸收有正余量，但强总变差吸收仍为负余量。")
    lines.append("")
    lines.append("## 2. atom readiness")
    lines.append("")
    lines.append("| packet | role | P | m | q_count | transitions | runs | max_run | A_full_distinct | fixed_Kloosterman | numerator | net | total variation |")
    lines.append("| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |")
    for item in result["atom_readiness_rows"]:
        lines.append(
            "| {packet} | {role} | {P} | {m} | {q_count} | {transitions} | {runs} | {max_run} | "
            "`{A}` | `{fixed}` | `{num}` | {net} | {total} |".format(
                packet=cell(item["packet"]),
                role=cell(item["role"]),
                P=item["P"],
                m=item["m"],
                q_count=item["q_count"],
                transitions=item["transitions"],
                runs=item["runs"],
                max_run=item["max_run"],
                A=fmt_bool(item["A_full_distinct"]),
                fixed=fmt_bool(item["fixed_numerator_kloosterman_ready"]),
                num=cell(item["numerator_motion_class"]),
                net=render_fraction(item["net"]),
                total=render_fraction(item["total_variation"]),
            )
        )
    lines.append("")
    lines.append("## 3. 门控表")
    lines.append("")
    lines.append("| gate | closed | proved | meaning | remaining |")
    lines.append("| --- | --- | --- | --- | --- |")
    for item in result["gate_rows"]:
        lines.append(
            f"| `{cell(item['gate'])}` | `{fmt_bool(item['closed'])}` | `{fmt_bool(item['proved'])}` | "
            f"{cell(item['meaning'])} | `{cell(item['remaining'])}` |"
        )
    lines.append("")
    lines.append("## 4. 外部前沿适配")
    lines.append("")
    lines.append("| input | usable after | current gap |")
    lines.append("| --- | --- | --- |")
    for item in result["external_frontier_note"]:
        lines.append(
            f"| {cell(item['input'])} | {cell(item['usable_after'])} | {cell(item['current_gap'])} |"
        )
    lines.append("")
    lines.append("## 5. 最新开放口")
    lines.append("")
    lines.append("```text")
    lines.append(result["next_primary_attack_target"])
    lines.append("```")
    lines.append("")
    lines.append("保留基底：")
    lines.append("")
    lines.append("```text")
    lines.append(result["retained_basis"])
    lines.append("```")
    lines.append("")
    lines.append("## 6. 依赖哈希")
    lines.append("")
    lines.append("| file | sha256 |")
    lines.append("| --- | --- |")
    for path, digest in result["source_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    lines.append("")
    lines.append("行/列命题仍未无条件闭合。")
    lines.append("")
    return "\n".join(lines)


def write_outputs(result: dict[str, Any]) -> None:
    """写出 JSON 与 Markdown。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(result, ensure_ascii=False, indent=2)
    OUT_LEDGER.write_text(payload + "\n", encoding="utf-8")
    OUT_JSON.write_text(payload + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")


def main() -> None:
    """入口。"""
    result = build_certificate()
    write_outputs(result)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
