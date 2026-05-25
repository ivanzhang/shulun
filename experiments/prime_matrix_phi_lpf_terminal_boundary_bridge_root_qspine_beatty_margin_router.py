#!/usr/bin/env python3
"""审计 bridge-root q-spine 的 Beatty 整数分子 margin。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_terminal_boundary_bridge_root_qspine_beatty_margin_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-terminal-boundary-bridge-root-qspine-beatty-margin-router.json

输出：
  data/prime-matrix-phi-lpf-terminal-boundary-bridge-root-qspine-beatty-margin-ledger.json
  docs/monograph/prime-matrix-phi-lpf-terminal-boundary-bridge-root-qspine-beatty-margin-router.json
  docs/monograph/prime-matrix-phi-lpf-terminal-boundary-bridge-root-qspine-beatty-margin-router.md

本证书承接 bridge-root q-spine microtemplate。它证明四个 AD-singleton
微转移的相位分子满足同一个 Beatty 整数恒等式：

    phase_delta_num = lift_step*q*q' + P*(s*q-a*g),

其中 m=P+r, a=floor(qr/P), D=qr-aP, q'=q+g,
s=floor((D+gr)/P)。该层仍不证明 uniform source law；它只把
BridgeRootADSingletonQSpineSourceLawOrPDEC 压成 Beatty margin 源律或 PDEC。
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

SLUG = "prime-matrix-phi-lpf-terminal-boundary-bridge-root-qspine-beatty-margin"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

QSPINE_JSON = DOCS / (
    "prime-matrix-phi-lpf-terminal-boundary-bridge-root-qspine-microtemplate-router.json"
)
PHASE_TURN_JSON = DOCS / (
    "prime-matrix-phi-lpf-dominant-sign-word-repeated-step-packet-enclosure-"
    "terminal-phase-turn-word-audit.json"
)

BEATTY_MARGIN_LAW = "BridgeRootADSingletonBeattyMarginSourceLawOrPDEC"
TAIL_OVERHANG_LAW = "RightSelectedTerminalTailOverhangPDEC"
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
    paths = [Path(__file__).resolve(), QSPINE_JSON, PHASE_TURN_JSON]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def fmt_bool(value: Any) -> str:
    """布尔值小写渲染。"""
    return "true" if bool(value) else "false"


def cell(value: Any) -> str:
    """Markdown 表格单元转义。"""
    return str(value).replace("|", r"\|")


def frac_record(value: Fraction) -> dict[str, Any]:
    """稳定输出分数。"""
    return {
        "fraction": f"{value.numerator}/{value.denominator}",
        "decimal": f"{float(value):.12f}",
        "numerator": value.numerator,
        "denominator": value.denominator,
    }


def atom_key(atom: dict[str, Any]) -> str:
    """统一 atom key。"""
    return f"{atom['packet_side']}:{atom['packet_index']}:{atom['role']}:m{atom['m']}"


def transition_key(row: dict[str, Any]) -> str:
    """微转移 key。"""
    return f"m{row['m']}:q{row['q']}->{row['q_next']}"


def phase_atom_map(payload: dict[str, Any]) -> dict[str, dict[str, Any]]:
    """按 atom key 索引 phase-turn profiles。"""
    return {
        atom_key(atom): atom
        for atom in payload["finite_audit"]["atom_phase_turn_profiles"]
    }


def find_transition(atom: dict[str, Any], q: int, q_next: int) -> dict[str, Any]:
    """按 q 端点找相邻 prime 转移。"""
    for transition in atom["phase_turn_transitions"]:
        if int(transition["q"]) == q and int(transition["q_next"]) == q_next:
            return transition
    raise KeyError(f"transition q{q}->{q_next} not found for {atom_key(atom)}")


def micro_transition_rows(
    qspine_payload: dict[str, Any],
    phase_payload: dict[str, Any],
) -> list[dict[str, Any]]:
    """提取四个 AD-singleton 微转移并验证 Beatty 分子恒等式。"""
    atoms = phase_atom_map(phase_payload)
    rows: list[dict[str, Any]] = []
    for packet in qspine_payload["microtemplate_rows"]:
        atom = atoms[packet["atom_key"]]
        for role, run_name in [
            ("A_singleton_pre_bridge", "pre_bridge_run"),
            ("D_singleton_bridge_old", "bridge_old_run"),
        ]:
            run = packet[run_name]
            q = int(run["q_start"])
            q_next = int(run["q_end"])
            transition = find_transition(atom, q, q_next)
            P = int(packet["P"])
            m = int(packet["m"])
            r = m - P
            g = int(transition["q_gap"])
            beatty_a = (q * r) // P
            residual_D = q * r - beatty_a * P
            beatty_s = (residual_D + g * r) // P
            beatty_B = beatty_s * q - beatty_a * g
            lift_step = int(transition["lift_step"])
            numerator_formula = lift_step * q * q_next + P * beatty_B
            actual_num = int(transition["phase_delta_num"])
            actual_den = int(transition["phase_delta_den"])
            phase_delta = Fraction(actual_num, actual_den)
            expected_carry = g + beatty_s
            expected_k = q + beatty_a
            k_identity_verified = q * m == expected_k * P + residual_D
            row = {
                "packet_id": packet["packet_id"],
                "atom_key": packet["atom_key"],
                "micro_role": role,
                "P": P,
                "m": m,
                "r": r,
                "q": q,
                "q_next": q_next,
                "g": g,
                "D": int(transition["D"]),
                "D_from_r": residual_D,
                "k_from_m": expected_k,
                "k_from_r": expected_k,
                "carry": int(transition["carry_formula"]),
                "carry_from_gap_plus_s": expected_carry,
                "beatty_a_floor_qr_over_P": beatty_a,
                "beatty_s_floor_D_plus_gr_over_P": beatty_s,
                "beatty_B_s_q_minus_a_g": beatty_B,
                "lift": int(transition["lift"]),
                "lift_next": int(transition["lift_next"]),
                "lift_step": lift_step,
                "phase_delta_num": actual_num,
                "phase_delta_den": actual_den,
                "phase_delta": frac_record(phase_delta),
                "numerator_formula": numerator_formula,
                "numerator_identity_verified": numerator_formula == actual_num,
                "D_identity_verified": residual_D == int(transition["D"]),
                "k_identity_verified": k_identity_verified,
                "carry_decomposition_verified": expected_carry == int(transition["carry_formula"]),
                "direction": transition["phase_direction"],
                "A_wrap": bool(transition["A_wrap"]),
                "D_wrap": bool(transition["D_wrap"]),
                "phase_turn_word": transition["phase_turn_word"],
            }
            row["A_singleton_negative_pure_P_multiple_closed"] = (
                role == "A_singleton_pre_bridge"
                and lift_step == 0
                and beatty_s == 0
                and beatty_B < 0
                and numerator_formula == P * beatty_B
                and actual_num < 0
            )
            row["D_singleton_positive_margin_closed"] = (
                role == "D_singleton_bridge_old"
                and lift_step == -1
                and beatty_s == 1
                and numerator_formula == P * beatty_B - q * q_next
                and actual_num > 0
            )
            rows.append(row)
    return rows


def packet_rows(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """把 A/D 微转移合并成每个 bridge packet 的 margin 行。"""
    grouped: dict[int, list[dict[str, Any]]] = {}
    for row in rows:
        grouped.setdefault(int(row["packet_id"]), []).append(row)
    output: list[dict[str, Any]] = []
    for packet_id, items in sorted(grouped.items()):
        a_row = next(row for row in items if row["micro_role"] == "A_singleton_pre_bridge")
        d_row = next(row for row in items if row["micro_role"] == "D_singleton_bridge_old")
        output.append(
            {
                "packet_id": packet_id,
                "atom_key": a_row["atom_key"],
                "P": a_row["P"],
                "m": a_row["m"],
                "r": a_row["r"],
                "A_transition": transition_key(a_row),
                "D_transition": transition_key(d_row),
                "A_beatty_a": a_row["beatty_a_floor_qr_over_P"],
                "D_beatty_a": d_row["beatty_a_floor_qr_over_P"],
                "A_beatty_B": a_row["beatty_B_s_q_minus_a_g"],
                "D_beatty_B": d_row["beatty_B_s_q_minus_a_g"],
                "A_phase_delta_num": a_row["phase_delta_num"],
                "D_phase_delta_num": d_row["phase_delta_num"],
                "D_positive_margin": d_row["phase_delta_num"],
                "A_negative_pure_P_multiple_closed": a_row[
                    "A_singleton_negative_pure_P_multiple_closed"
                ],
                "D_positive_margin_closed": d_row["D_singleton_positive_margin_closed"],
                "packet_margin_identity_closed": a_row[
                    "A_singleton_negative_pure_P_multiple_closed"
                ]
                and d_row["D_singleton_positive_margin_closed"],
            }
        )
    return output


def delta_summary(rows: list[dict[str, Any]]) -> dict[str, Any]:
    """汇总两个 packet 的离散漂移。"""
    packets = packet_rows(rows)
    if len(packets) != 2:
        return {"packet_count": len(packets), "two_packet_delta_closed": False}
    first, second = packets
    return {
        "packet_count": len(packets),
        "two_packet_delta_closed": True,
        "r_gap": second["r"] - first["r"],
        "m_gap": second["m"] - first["m"],
        "A_beatty_a_gap": second["A_beatty_a"] - first["A_beatty_a"],
        "D_beatty_a_gap": second["D_beatty_a"] - first["D_beatty_a"],
        "A_B_gap": second["A_beatty_B"] - first["A_beatty_B"],
        "D_B_gap": second["D_beatty_B"] - first["D_beatty_B"],
        "D_positive_margin_drop": first["D_positive_margin"] - second["D_positive_margin"],
        "first_D_positive_margin": first["D_positive_margin"],
        "second_D_positive_margin": second["D_positive_margin"],
    }


def build_certificate() -> dict[str, Any]:
    """组装 Beatty margin 证书。"""
    qspine_payload = load_json(QSPINE_JSON)
    phase_payload = load_json(PHASE_TURN_JSON)
    rows = micro_transition_rows(qspine_payload, phase_payload)
    packets = packet_rows(rows)
    summary = delta_summary(rows)
    numerator_identity_closed = all(row["numerator_identity_verified"] for row in rows)
    low_level_closed = all(
        row["D_identity_verified"]
        and row["k_identity_verified"]
        and row["carry_decomposition_verified"]
        for row in rows
    )
    a_side_closed = all(
        row["A_singleton_negative_pure_P_multiple_closed"]
        for row in rows
        if row["micro_role"] == "A_singleton_pre_bridge"
    )
    d_side_closed = all(
        row["D_singleton_positive_margin_closed"]
        for row in rows
        if row["micro_role"] == "D_singleton_bridge_old"
    )
    beatty_margin_closed = (
        qspine_payload.get("bridge_root_qspine_microtemplate_closed") is True
        and len(rows) == 4
        and numerator_identity_closed
        and low_level_closed
        and a_side_closed
        and d_side_closed
        and summary.get("two_packet_delta_closed") is True
    )
    latest_gate = (
        f"{BEATTY_MARGIN_LAW} AND {TAIL_OVERHANG_LAW} AND {MASS_RATIO_LAW} "
        f"AND {ORIENTATION_LAW} AND {MOVING_BEATTY_SAVING} AND {TRACE_FAMILY} "
        f"AND {GROUP_ORBIT_INPUT}"
    )
    return {
        "certificate_type": "prime_matrix_phi_lpf_terminal_boundary_bridge_root_qspine_beatty_margin_router",
        "status": "bridge_root_qspine_beatty_margin_closed_uniform_source_law_open",
        "verified_date": "2026-05-25",
        "previous_qspine_microtemplate_closed": qspine_payload.get(
            "bridge_root_qspine_microtemplate_closed"
        )
        is True,
        "micro_transition_count": len(rows),
        "packet_count": len(packets),
        "beatty_numerator_identity_closed": numerator_identity_closed,
        "low_level_beatty_decomposition_closed": low_level_closed,
        "A_singleton_negative_pure_P_multiple_closed": a_side_closed,
        "D_singleton_positive_margin_closed": d_side_closed,
        "bridge_root_qspine_beatty_margin_closed": beatty_margin_closed,
        "bridge_root_uniform_beatty_margin_source_law_proved": False,
        "right_tail_overhang_pdec_constructed": False,
        "admissible_trace_or_typeii_family_constructed": False,
        "finite_group_orbit_expansion_family_constructed": False,
        "phi_lpf_parity_barrier_globally_broken": False,
        "row_column_unconditional_closed": False,
        "identity": "phase_delta_num = lift_step*q*q_next + P*(s*q-a*g), m=P+r, a=floor(qr/P), s=floor((D+gr)/P)",
        "micro_transition_rows": rows,
        "packet_margin_rows": packets,
        "two_packet_delta_summary": summary,
        "next_primary_attack_target": BEATTY_MARGIN_LAW,
        "latest_open_gate": latest_gate,
        "plain_conclusion": (
            "The q-spine source is no longer an opaque local phase event: all four "
            "AD-singleton micro-transitions satisfy the same Beatty numerator "
            "factorization.  The remaining uniform problem is to prove the Beatty "
            "margin source law, especially the positive D-singleton margin, beyond "
            "this finite ledger."
        ),
        "gate_rows": [
            {
                "gate": "BridgeRootQSpineMicrotemplateImported",
                "closed": qspine_payload.get("bridge_root_qspine_microtemplate_closed") is True,
                "proved": qspine_payload.get("bridge_root_qspine_microtemplate_closed") is True,
                "meaning": "the two bridge roots already form one selected-terminal q-spine.",
                "remaining": "none for import",
            },
            {
                "gate": "BeattyNumeratorIdentity",
                "closed": numerator_identity_closed,
                "proved": numerator_identity_closed,
                "meaning": "each micro transition satisfies phase_delta_num = lift_step*q*q' + P*(s*q-a*g).",
                "remaining": "finite numerator factorization",
            },
            {
                "gate": "ASingletonPurePMultiple",
                "closed": a_side_closed,
                "proved": a_side_closed,
                "meaning": "the A-singleton pre-bridge steps have lift_step=0, s=0, and negative P-multiple numerator.",
                "remaining": "finite A-side margin ledger",
            },
            {
                "gate": "DSingletonPositiveBeattyMargin",
                "closed": d_side_closed,
                "proved": d_side_closed,
                "meaning": "the D-singleton bridge-old steps have lift_step=-1, s=1, and positive numerator margin.",
                "remaining": "finite D-side margin ledger",
            },
            {
                "gate": "BridgeRootUniformBeattyMarginSourceLaw",
                "closed": False,
                "proved": False,
                "meaning": "a uniform law must force the same margin pattern outside the finite q=607 spine.",
                "remaining": BEATTY_MARGIN_LAW,
            },
            {
                "gate": "RowColumnUnconditionalClosureReached",
                "closed": False,
                "proved": False,
                "meaning": "this is a finite Beatty margin factorization, not a global parity-breaking theorem.",
                "remaining": (
                    f"{BEATTY_MARGIN_LAW} AND {TAIL_OVERHANG_LAW} AND {MASS_RATIO_LAW} "
                    f"AND {ORIENTATION_LAW} AND {MOVING_BEATTY_SAVING}"
                ),
            },
        ],
        "source_hashes": source_hashes(),
    }


def run_label(row: dict[str, Any]) -> str:
    """Markdown 表格中的微转移标签。"""
    return f"m{row['m']} q{row['q']}->{row['q_next']} g{row['g']}"


def render_markdown(payload: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF terminal boundary bridge-root q-spine Beatty margin 证书",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['verified_date']}`",
        "",
        "本证书把 bridge-root q-spine 源律继续压成 Beatty 整数分子 margin。",
        "",
        "```text",
        f"previous_qspine_microtemplate_closed={fmt_bool(payload['previous_qspine_microtemplate_closed'])}",
        f"micro_transition_count={payload['micro_transition_count']}",
        f"packet_count={payload['packet_count']}",
        f"beatty_numerator_identity_closed={fmt_bool(payload['beatty_numerator_identity_closed'])}",
        f"A_singleton_negative_pure_P_multiple_closed={fmt_bool(payload['A_singleton_negative_pure_P_multiple_closed'])}",
        f"D_singleton_positive_margin_closed={fmt_bool(payload['D_singleton_positive_margin_closed'])}",
        f"bridge_root_qspine_beatty_margin_closed={fmt_bool(payload['bridge_root_qspine_beatty_margin_closed'])}",
        f"bridge_root_uniform_beatty_margin_source_law_proved={fmt_bool(payload['bridge_root_uniform_beatty_margin_source_law_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(payload['row_column_unconditional_closed'])}",
        "```",
        "",
        "核心恒等式：",
        "",
        "```text",
        payload["identity"],
        "```",
        "",
        "## 1. micro transition rows",
        "",
        "| role | transition | r | a | s | B=sq-ag | lift step | numerator | formula ok |",
        "| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in payload["micro_transition_rows"]:
        lines.append(
            "| `{role}` | {label} | {r} | {a} | {s} | {B} | {eps} | {num} | `{ok}` |".format(
                role=row["micro_role"],
                label=run_label(row),
                r=row["r"],
                a=row["beatty_a_floor_qr_over_P"],
                s=row["beatty_s_floor_D_plus_gr_over_P"],
                B=row["beatty_B_s_q_minus_a_g"],
                eps=row["lift_step"],
                num=row["phase_delta_num"],
                ok=fmt_bool(row["numerator_identity_verified"]),
            )
        )
    lines.extend(
        [
            "",
            "## 2. packet margin rows",
            "",
            "| packet | atom | r | A transition | A numerator | D transition | D positive margin | packet closed |",
            "| ---: | --- | ---: | --- | ---: | --- | ---: | --- |",
        ]
    )
    for row in payload["packet_margin_rows"]:
        lines.append(
            "| {packet} | `{atom}` | {r} | {atr} | {anum} | {dtr} | {dnum} | `{closed}` |".format(
                packet=row["packet_id"],
                atom=cell(row["atom_key"]),
                r=row["r"],
                atr=row["A_transition"],
                anum=row["A_phase_delta_num"],
                dtr=row["D_transition"],
                dnum=row["D_positive_margin"],
                closed=fmt_bool(row["packet_margin_identity_closed"]),
            )
        )
    lines.extend(
        [
            "",
            "## 3. two-packet delta summary",
            "",
            "| field | value |",
            "| --- | --- |",
        ]
    )
    for key, value in payload["two_packet_delta_summary"].items():
        lines.append(f"| `{key}` | `{cell(value)}` |")
    lines.extend(
        [
            "",
            "## 4. 门控表",
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
    print(f"micro_transition_count={payload['micro_transition_count']}")
    print(
        "beatty_numerator_identity_closed="
        f"{fmt_bool(payload['beatty_numerator_identity_closed'])}"
    )
    print(
        "A_singleton_negative_pure_P_multiple_closed="
        f"{fmt_bool(payload['A_singleton_negative_pure_P_multiple_closed'])}"
    )
    print(
        "D_singleton_positive_margin_closed="
        f"{fmt_bool(payload['D_singleton_positive_margin_closed'])}"
    )
    print(
        "bridge_root_qspine_beatty_margin_closed="
        f"{fmt_bool(payload['bridge_root_qspine_beatty_margin_closed'])}"
    )
    print(f"row_column_unconditional_closed={fmt_bool(payload['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
