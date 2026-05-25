#!/usr/bin/env python3
"""审计 bridge-root debt 是否落入同一 q-spine 微模板。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_terminal_boundary_bridge_root_qspine_microtemplate_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-terminal-boundary-bridge-root-qspine-microtemplate-router.json

输出：
  data/prime-matrix-phi-lpf-terminal-boundary-bridge-root-qspine-microtemplate-ledger.json
  docs/monograph/prime-matrix-phi-lpf-terminal-boundary-bridge-root-qspine-microtemplate-router.json
  docs/monograph/prime-matrix-phi-lpf-terminal-boundary-bridge-root-qspine-microtemplate-router.md

本证书承接 carry-break source-packet reduction。它不证明 bridge-root debt
的统一源律；它只把两个 bridge roots 压成同一个 AD-singleton q-spine 微模板，
从而把下一步硬点改写为该微模板的源律或 PDEC。
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

SLUG = "prime-matrix-phi-lpf-terminal-boundary-bridge-root-qspine-microtemplate"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

CARRY_BREAK_JSON = DOCS / "prime-matrix-phi-lpf-terminal-boundary-carry-break-source-packet-router.json"
VARIATION_JSON = DOCS / (
    "prime-matrix-phi-lpf-dominant-sign-word-repeated-step-packet-enclosure-"
    "terminal-phase-variation-budget-audit.json"
)

QSPINE_LAW = "BridgeRootADSingletonQSpineSourceLawOrPDEC"
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
    paths = [Path(__file__).resolve(), CARRY_BREAK_JSON, VARIATION_JSON]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def fmt_bool(value: Any) -> str:
    """布尔值小写渲染。"""
    return "true" if bool(value) else "false"


def cell(value: Any) -> str:
    """Markdown 表格单元转义。"""
    return str(value).replace("|", r"\|")


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


def render_fraction(record: dict[str, Any]) -> str:
    """表格用分数摘要。"""
    return f"{record['decimal']} ({record['fraction']})"


def atom_key(atom: dict[str, Any]) -> str:
    """统一 atom key。"""
    return f"{atom['packet_side']}:{atom['packet_index']}:{atom['role']}:m{atom['m']}"


def run_by_id(atom: dict[str, Any]) -> dict[int, dict[str, Any]]:
    """按 run_id 索引 run variation rows。"""
    return {int(row["run_id"]): row for row in atom["run_variation_rows"]}


def run_digest(row: dict[str, Any]) -> dict[str, Any]:
    """抽取微模板需要的 run 字段。"""
    return {
        "run_id": row["run_id"],
        "direction": row["direction"],
        "q_start": row["q_start"],
        "q_end": row["q_end"],
        "length": row["length"],
        "A_wrap_count": row["A_wrap_count"],
        "D_wrap_count": row["D_wrap_count"],
        "carry_min": row["carry_min"],
        "carry_max": row["carry_max"],
        "variation": row["variation"],
        "signed_delta": row["signed_delta"],
    }


def is_negative_a_singleton(row: dict[str, Any]) -> bool:
    """判断是否为负向 A-singleton 微步。"""
    return (
        row["direction"] == "negative"
        and int(row["length"]) == 1
        and int(row["A_wrap_count"]) == 1
        and int(row["D_wrap_count"]) == 0
        and int(row["carry_min"]) == 2
        and int(row["carry_max"]) == 2
    )


def is_positive_d_singleton(row: dict[str, Any]) -> bool:
    """判断是否为正向 D-singleton 微步。"""
    return (
        row["direction"] == "positive"
        and int(row["length"]) == 1
        and int(row["A_wrap_count"]) == 0
        and int(row["D_wrap_count"]) == 1
        and int(row["carry_min"]) == 7
        and int(row["carry_max"]) == 7
    )


def build_microtemplate_rows(
    packet_rows: list[dict[str, Any]],
    atom_map: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    """为每个 bridge/unit packet 提取局部 run 微模板。"""
    rows = []
    for packet in packet_rows:
        atom = atom_map[packet["atom_key"]]
        runs = run_by_id(atom)
        bridge_root_run = int(packet["bridge_root_run"])
        unit_root_run = int(packet["unit_root_run"])
        pre_bridge_run = runs[bridge_root_run - 2]
        bridge_old_run = runs[bridge_root_run - 1]
        following_negative_run = runs[bridge_root_run]
        unit_positive_run = runs[unit_root_run]
        bridge_template_closed = is_negative_a_singleton(pre_bridge_run) and is_positive_d_singleton(
            bridge_old_run
        )
        following_starts_at_bridge_q = int(following_negative_run["q_start"]) == int(packet["bridge_root_q"])
        unit_event_starts_at_unit_q = int(unit_positive_run["q_start"]) == int(packet["unit_root_q"])
        rows.append(
            {
                "packet_id": packet["packet_id"],
                "atom_key": packet["atom_key"],
                "P": atom["P"],
                "m": atom["m"],
                "packet_side": atom["packet_side"],
                "packet_index": atom["packet_index"],
                "role": atom["role"],
                "bridge_root_q": packet["bridge_root_q"],
                "unit_root_q": packet["unit_root_q"],
                "old_return_boundary_q": packet["old_return_boundary_q"],
                "old_return_new_q_start": packet["old_return_new_q_start"],
                "bridge_root_debt": packet["bridge_root_debt"],
                "unit_old_return_echo_mass": packet["unit_old_return_echo_mass"],
                "pre_bridge_run": run_digest(pre_bridge_run),
                "bridge_old_run": run_digest(bridge_old_run),
                "following_negative_run": run_digest(following_negative_run),
                "unit_positive_run": run_digest(unit_positive_run),
                "bridge_ad_singleton_template_closed": bridge_template_closed,
                "following_negative_run_starts_at_bridge_q": following_starts_at_bridge_q,
                "unit_positive_run_starts_at_unit_q": unit_event_starts_at_unit_q,
                "bridge_micro_q_interval": f"{pre_bridge_run['q_start']}->{bridge_old_run['q_end']}",
                "bridge_micro_q_width": int(bridge_old_run["q_end"]) - int(pre_bridge_run["q_start"]),
                "following_negative_width": int(following_negative_run["q_end"]) - int(following_negative_run["q_start"]),
                "unit_positive_width": int(unit_positive_run["q_end"]) - int(unit_positive_run["q_start"]),
            }
        )
    return sorted(rows, key=lambda row: (int(row["bridge_root_q"]), int(row["m"])))


def q_spine_summary(rows: list[dict[str, Any]]) -> dict[str, Any]:
    """汇总两个 bridge/unit packet 的 q-spine。"""
    ordered = sorted(rows, key=lambda row: int(row["bridge_root_q"]))
    shared_pivot = None
    if len(ordered) == 2 and int(ordered[0]["unit_root_q"]) == int(ordered[1]["bridge_root_q"]):
        shared_pivot = int(ordered[0]["unit_root_q"])
    root_micro_q_shift = None
    if len(ordered) == 2:
        root_micro_q_shift = int(ordered[1]["pre_bridge_run"]["q_start"]) - int(
            ordered[0]["pre_bridge_run"]["q_start"]
        )
    m_gap = None
    if len(ordered) == 2:
        m_gap = int(ordered[1]["m"]) - int(ordered[0]["m"])
    return {
        "q_spine_node_count": 3 if shared_pivot is not None else len({row["bridge_root_q"] for row in ordered}),
        "q_spine_nodes": [ordered[0]["bridge_root_q"], shared_pivot, ordered[-1]["unit_root_q"]]
        if shared_pivot is not None
        else [row["bridge_root_q"] for row in ordered],
        "shared_pivot_q": shared_pivot,
        "unit_to_bridge_pivot_alignment_closed": shared_pivot is not None,
        "m_gap_between_bridge_packets": m_gap,
        "root_micro_q_shift": root_micro_q_shift,
        "same_P": len({row["P"] for row in ordered}) == 1,
        "same_packet_index": len({row["packet_index"] for row in ordered}) == 1,
        "same_packet_side": len({row["packet_side"] for row in ordered}) == 1,
        "same_role": len({row["role"] for row in ordered}) == 1,
        "bridge_to_unit_q_gaps": [
            int(row["unit_root_q"]) - int(row["bridge_root_q"]) for row in ordered
        ],
    }


def build_certificate() -> dict[str, Any]:
    """组装 q-spine microtemplate 证书。"""
    carry_payload = load_json(CARRY_BREAK_JSON)
    variation_payload = load_json(VARIATION_JSON)
    atom_map = {
        atom_key(atom): atom
        for atom in variation_payload["finite_audit"]["atom_variation_profiles"]
    }
    packet_rows = carry_payload["packet_rows"]
    micro_rows = build_microtemplate_rows(packet_rows, atom_map)
    spine = q_spine_summary(micro_rows)

    bridge_debt_mass = sum(
        (frac_from_record(row["bridge_root_debt"]) for row in micro_rows), Fraction(0)
    )
    unit_echo_mass = sum(
        (frac_from_record(row["unit_old_return_echo_mass"]) for row in micro_rows), Fraction(0)
    )
    all_bridge_templates_closed = all(row["bridge_ad_singleton_template_closed"] for row in micro_rows)
    all_endpoint_links_closed = all(
        row["following_negative_run_starts_at_bridge_q"]
        and row["unit_positive_run_starts_at_unit_q"]
        for row in micro_rows
    )
    qspine_microtemplate_closed = (
        carry_payload.get("carry_break_source_packet_reduction_closed") is True
        and len(micro_rows) == 2
        and all_bridge_templates_closed
        and all_endpoint_links_closed
        and spine["unit_to_bridge_pivot_alignment_closed"] is True
        and spine["same_P"]
        and spine["same_packet_index"]
        and spine["same_packet_side"]
        and spine["same_role"]
    )

    return {
        "certificate_type": "prime_matrix_phi_lpf_terminal_boundary_bridge_root_qspine_microtemplate_router",
        "status": "bridge_root_qspine_microtemplate_closed_source_law_open",
        "verified_date": "2026-05-25",
        "previous_carry_break_source_packet_reduction_closed": carry_payload.get(
            "carry_break_source_packet_reduction_closed"
        )
        is True,
        "bridge_root_packet_count": len(micro_rows),
        "bridge_root_qspine_microtemplate_closed": qspine_microtemplate_closed,
        "all_bridge_roots_share_ad_singleton_template": all_bridge_templates_closed,
        "all_bridge_endpoint_links_closed": all_endpoint_links_closed,
        "unit_to_bridge_pivot_alignment_closed": spine["unit_to_bridge_pivot_alignment_closed"],
        "shared_pivot_q": spine["shared_pivot_q"],
        "m_gap_between_bridge_packets": spine["m_gap_between_bridge_packets"],
        "root_micro_q_shift": spine["root_micro_q_shift"],
        "bridge_to_unit_q_gaps": spine["bridge_to_unit_q_gaps"],
        "bridge_root_debt_open_mass": frac_record(bridge_debt_mass),
        "unit_old_return_echo_mass": frac_record(unit_echo_mass),
        "bridge_root_qspine_source_law_proved": False,
        "right_tail_overhang_pdec_constructed": False,
        "admissible_trace_or_typeii_family_constructed": False,
        "finite_group_orbit_expansion_family_constructed": False,
        "phi_lpf_parity_barrier_globally_broken": False,
        "row_column_unconditional_closed": False,
        "q_spine_summary": spine,
        "microtemplate_rows": micro_rows,
        "next_primary_attack_target": QSPINE_LAW,
        "plain_conclusion": (
            "The two bridge-root debts form one selected-terminal q-spine: both roots "
            "are preceded by the same negative A-singleton and positive D-singleton "
            "microtemplate, and the first unit root q=607 is the second bridge root. "
            "The source law for this q-spine remains open."
        ),
        "gate_rows": [
            {
                "gate": "BridgeRootADSingletonMicrotemplateLedger",
                "closed": all_bridge_templates_closed,
                "proved": all_bridge_templates_closed,
                "meaning": "both bridge roots are preceded by the same negative A-singleton and positive D-singleton run pair.",
                "remaining": "finite bridge-root microtemplate ledger",
            },
            {
                "gate": "BridgeRootQSpinePivotLedger",
                "closed": spine["unit_to_bridge_pivot_alignment_closed"],
                "proved": spine["unit_to_bridge_pivot_alignment_closed"],
                "meaning": "the first packet unit root q equals the second packet bridge root q.",
                "remaining": "shared q=607 pivot ledger",
            },
            {
                "gate": "BridgeRootQSpineSourceLaw",
                "closed": False,
                "proved": False,
                "meaning": "the shared AD-singleton q-spine still needs a uniform source law or named PDEC.",
                "remaining": QSPINE_LAW,
            },
            {
                "gate": "RightTailOverhangPDEC",
                "closed": False,
                "proved": False,
                "meaning": "the single right selected-terminal tail overhang is unchanged.",
                "remaining": TAIL_OVERHANG_LAW,
            },
            {
                "gate": "ExternalTraceOrGroupEntry",
                "closed": False,
                "proved": False,
                "meaning": "trace/Kloosterman/Type-II or group-expansion inputs still need a signed averaged family built from the q-spine.",
                "remaining": f"{TRACE_FAMILY} AND {GROUP_ORBIT_INPUT}",
            },
            {
                "gate": "RowColumnUnconditionalClosureReached",
                "closed": False,
                "proved": False,
                "meaning": "this is a finite q-spine microtemplate reduction, not a global parity-breaking theorem.",
                "remaining": (
                    f"{QSPINE_LAW} AND {TAIL_OVERHANG_LAW} AND {MASS_RATIO_LAW} "
                    f"AND {ORIENTATION_LAW} AND {MOVING_BEATTY_SAVING}"
                ),
            },
        ],
        "source_hashes": source_hashes(),
    }


def write_outputs(payload: dict[str, Any]) -> None:
    """写出 JSON、ledger 与 Markdown。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    text = json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True)
    OUT_LEDGER.write_text(text + "\n", encoding="utf-8")
    OUT_JSON.write_text(text + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(payload), encoding="utf-8")


def render_markdown(payload: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF terminal boundary bridge-root q-spine microtemplate 证书",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['verified_date']}`",
        "",
        "本证书把两个 bridge-root debt 压成共享 q-spine 微模板。",
        "",
        "```text",
        f"previous_carry_break_source_packet_reduction_closed={fmt_bool(payload['previous_carry_break_source_packet_reduction_closed'])}",
        f"bridge_root_packet_count={payload['bridge_root_packet_count']}",
        f"all_bridge_roots_share_ad_singleton_template={fmt_bool(payload['all_bridge_roots_share_ad_singleton_template'])}",
        f"unit_to_bridge_pivot_alignment_closed={fmt_bool(payload['unit_to_bridge_pivot_alignment_closed'])}",
        f"shared_pivot_q={payload['shared_pivot_q']}",
        f"m_gap_between_bridge_packets={payload['m_gap_between_bridge_packets']}",
        f"root_micro_q_shift={payload['root_micro_q_shift']}",
        f"bridge_to_unit_q_gaps={payload['bridge_to_unit_q_gaps']}",
        f"bridge_root_qspine_microtemplate_closed={fmt_bool(payload['bridge_root_qspine_microtemplate_closed'])}",
        f"bridge_root_qspine_source_law_proved={fmt_bool(payload['bridge_root_qspine_source_law_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(payload['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. q-spine summary",
        "",
        "| field | value |",
        "| --- | --- |",
    ]
    for key, value in payload["q_spine_summary"].items():
        lines.append(f"| `{key}` | `{cell(value)}` |")

    lines.extend(
        [
            "",
            "## 2. bridge-root microtemplates",
            "",
            "| packet | atom | P | bridge q | unit q | pre bridge run | bridge old run | following run | unit run | bridge debt |",
            "| ---: | --- | ---: | ---: | ---: | --- | --- | --- | --- | --- |",
        ]
    )
    for row in payload["microtemplate_rows"]:
        lines.append(
            "| {pid} | `{atom}` | {P} | {bq} | {uq} | {pre} | {bridge} | {follow} | {unit} | {debt} |".format(
                pid=row["packet_id"],
                atom=cell(row["atom_key"]),
                P=row["P"],
                bq=row["bridge_root_q"],
                uq=row["unit_root_q"],
                pre=run_label(row["pre_bridge_run"]),
                bridge=run_label(row["bridge_old_run"]),
                follow=run_label(row["following_negative_run"]),
                unit=run_label(row["unit_positive_run"]),
                debt=render_fraction(row["bridge_root_debt"]),
            )
        )

    lines.extend(
        [
            "",
            "## 3. mass ledger",
            "",
            "| mass | value |",
            "| --- | --- |",
            f"| bridge-root debt still open | {render_fraction(payload['bridge_root_debt_open_mass'])} |",
            f"| unit old-return echo mass | {render_fraction(payload['unit_old_return_echo_mass'])} |",
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
            f"{QSPINE_LAW} AND {TAIL_OVERHANG_LAW} AND {MASS_RATIO_LAW} AND {ORIENTATION_LAW} AND {MOVING_BEATTY_SAVING} AND {TRACE_FAMILY} AND {GROUP_ORBIT_INPUT}",
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


def run_label(row: dict[str, Any]) -> str:
    """Markdown 表格中的 run 微标签。"""
    return (
        f"r{row['run_id']} {row['direction']} "
        f"q{row['q_start']}->{row['q_end']} "
        f"A{row['A_wrap_count']}/D{row['D_wrap_count']} "
        f"c{row['carry_min']}..{row['carry_max']}"
    )


def main() -> None:
    """命令入口。"""
    payload = build_certificate()
    write_outputs(payload)
    print(f"bridge_root_packet_count={payload['bridge_root_packet_count']}")
    print(
        "all_bridge_roots_share_ad_singleton_template="
        f"{fmt_bool(payload['all_bridge_roots_share_ad_singleton_template'])}"
    )
    print(f"shared_pivot_q={payload['shared_pivot_q']}")
    print(
        "bridge_root_qspine_microtemplate_closed="
        f"{fmt_bool(payload['bridge_root_qspine_microtemplate_closed'])}"
    )
    print(f"bridge_root_debt_open_mass={render_fraction(payload['bridge_root_debt_open_mass'])}")
    print(f"row_column_unconditional_closed={fmt_bool(payload['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
