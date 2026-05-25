#!/usr/bin/env python3
"""审计 terminal boundary carry breaks 的 source-packet 对齐。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_terminal_boundary_carry_break_source_packet_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-terminal-boundary-carry-break-source-packet-router.json

输出：
  data/prime-matrix-phi-lpf-terminal-boundary-carry-break-source-packet-ledger.json
  docs/monograph/prime-matrix-phi-lpf-terminal-boundary-carry-break-source-packet-router.json
  docs/monograph/prime-matrix-phi-lpf-terminal-boundary-carry-break-source-packet-router.md

本证书承接 bulk carry-chain normal form。它不声称断点已全局闭合；
它只把 4 个 carry break 拆成 2 个 bridge-root debt 与 2 个 unit old-return echo，
从而把下一步硬点压到两个 bridge-root source law/PDEC。
"""

from __future__ import annotations

import hashlib
import json
import re
from collections import defaultdict
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-terminal-boundary-carry-break-source-packet"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

BULK_JSON = DOCS / "prime-matrix-phi-lpf-terminal-boundary-bulk-carry-chain-normal-form-router.json"
RESIDUAL_JSON = DOCS / "prime-matrix-phi-lpf-terminal-boundary-residual-flow-obstruction-router.json"
OLD_RETURN_JSON = DOCS / "prime-matrix-phi-lpf-terminal-boundary-old-residual-return-alignment-router.json"

BRIDGE_ROOT_LAW = "BoundaryBridgeRootDebtSourceLawOrPDEC"
UNIT_OLD_RETURN_ECHO = "UnitCarryBreakOldReturnEchoSourceAligned"
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
    paths = [Path(__file__).resolve(), BULK_JSON, RESIDUAL_JSON, OLD_RETURN_JSON]
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


def display(value: Any) -> str:
    """Markdown 表格中的空值显示。"""
    return "-" if value is None else str(value)


def parse_new_q_start(endpoint: str) -> int | None:
    """从 old-return endpoint 文本中提取 new_q_start。"""
    match = re.search(r"new_q_start=(\d+)", endpoint)
    if match:
        return int(match.group(1))
    return None


def break_debt(row: dict[str, Any]) -> Fraction:
    """carry break 的正 debt，等于 previous residual 减 root old mass。"""
    return -frac_from_record(row["root_minus_previous_residual"])


def old_return_key(row: dict[str, Any]) -> tuple[str, Fraction]:
    """用于匹配 unit break echo 的 key。"""
    return (row["atom_key"], frac_from_record(row["old_residual_mass"]))


def build_old_return_index(rows: list[dict[str, Any]]) -> dict[tuple[str, Fraction], list[dict[str, Any]]]:
    """按 atom 与 old residual mass 建索引。"""
    index: dict[tuple[str, Fraction], list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        index[old_return_key(row)].append(row)
    return index


def classify_break_rows(
    break_rows: list[dict[str, Any]],
    old_return_rows: list[dict[str, Any]],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """分类 carry break：unit old-return echo 或 bridge-root debt。"""
    old_index = build_old_return_index(old_return_rows)
    classified = []
    for index, row in enumerate(break_rows):
        debt = break_debt(row)
        matches = old_index.get((row["atom_key"], debt), [])
        matched = matches[0] if matches else None
        classification = "bridge_root_debt_open"
        if matched is not None and int(row["run_gap"]) == 1:
            classification = "unit_old_return_echo_source_aligned"
        elif matched is not None:
            classification = "nonunit_old_return_echo_source_aligned"
        classified.append(
            {
                "break_index": index,
                "atom_key": row["atom_key"],
                "classification": classification,
                "previous_new_run_id": row["previous_new_run_id"],
                "previous_boundary_q": row["previous_boundary_q"],
                "root_new_run_id": row["root_new_run_id"],
                "root_boundary_q": row["root_boundary_q"],
                "run_gap": row["run_gap"],
                "q_gap": row["q_gap"],
                "break_debt": frac_record(debt),
                "root_minus_previous_residual": row["root_minus_previous_residual"],
                "matched_old_return": matched is not None,
                "matched_old_return_boundary_q": matched["boundary_q"] if matched else None,
                "matched_old_return_new_q_start": parse_new_q_start(matched.get("return_endpoint", "")) if matched else None,
                "matched_old_return_type": matched["return_type"] if matched else None,
                "matched_old_return_mass": matched["old_residual_mass"] if matched else None,
            }
        )
    bridge_rows = [row for row in classified if row["classification"] == "bridge_root_debt_open"]
    return classified, bridge_rows


def packetize_by_atom(classified_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """把 bridge-root debt 与随后 unit old-return echo 成包。"""
    by_atom: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in classified_rows:
        by_atom[row["atom_key"]].append(row)

    packets = []
    packet_id = 1
    for atom_key, rows in sorted(by_atom.items()):
        ordered = sorted(rows, key=lambda row: int(row["root_new_run_id"]))
        for left, right in zip(ordered, ordered[1:]):
            if (
                left["classification"] == "bridge_root_debt_open"
                and right["classification"] == "unit_old_return_echo_source_aligned"
            ):
                endpoint_match = left["root_boundary_q"] == right["matched_old_return_new_q_start"]
                packets.append(
                    {
                        "packet_id": packet_id,
                        "atom_key": atom_key,
                        "bridge_break_index": left["break_index"],
                        "unit_break_index": right["break_index"],
                        "bridge_root_run": left["root_new_run_id"],
                        "bridge_root_q": left["root_boundary_q"],
                        "unit_root_run": right["root_new_run_id"],
                        "unit_root_q": right["root_boundary_q"],
                        "old_return_boundary_q": right["matched_old_return_boundary_q"],
                        "old_return_new_q_start": right["matched_old_return_new_q_start"],
                        "old_return_type": right["matched_old_return_type"],
                        "bridge_root_matches_old_return_new_q_start": endpoint_match,
                        "unit_debt_equals_old_return_mass": right["matched_old_return"],
                        "bridge_root_debt": left["break_debt"],
                        "unit_old_return_echo_mass": right["break_debt"],
                        "bridge_to_unit_q_gap": int(right["root_boundary_q"]) - int(left["root_boundary_q"]),
                        "bridge_to_unit_run_gap": int(right["root_new_run_id"]) - int(left["root_new_run_id"]),
                        "status": "unit_echo_source_aligned_bridge_root_debt_still_open",
                    }
                )
                packet_id += 1
    return packets


def build_certificate() -> dict[str, Any]:
    """组装 carry-break source-packet 证书。"""
    bulk_payload = load_json(BULK_JSON)
    old_return_payload = load_json(OLD_RETURN_JSON)
    residual_payload = load_json(RESIDUAL_JSON)

    break_rows = bulk_payload["carry_break_rows"]
    old_return_rows = old_return_payload["return_alignment_rows"]
    classified_rows, bridge_rows = classify_break_rows(break_rows, old_return_rows)
    packet_rows = packetize_by_atom(classified_rows)

    unit_rows = [
        row for row in classified_rows if row["classification"] == "unit_old_return_echo_source_aligned"
    ]
    nonunit_echo_rows = [
        row for row in classified_rows if row["classification"] == "nonunit_old_return_echo_source_aligned"
    ]
    unmatched_unit_rows = [
        row
        for row in classified_rows
        if int(row["run_gap"]) == 1 and row["classification"] != "unit_old_return_echo_source_aligned"
    ]

    total_break_debt = sum((break_debt(row) for row in break_rows), Fraction(0))
    unit_echo_debt = sum((frac_from_record(row["break_debt"]) for row in unit_rows), Fraction(0))
    bridge_debt = sum((frac_from_record(row["break_debt"]) for row in bridge_rows), Fraction(0))
    packet_bridge_debt = sum((frac_from_record(row["bridge_root_debt"]) for row in packet_rows), Fraction(0))

    all_unit_echo_source_aligned = len(unit_rows) == 2 and not unmatched_unit_rows
    all_bridge_roots_packetized = len(packet_rows) == len(bridge_rows) == 2 and all(
        row["bridge_root_matches_old_return_new_q_start"] and row["unit_debt_equals_old_return_mass"]
        for row in packet_rows
    )
    source_packet_reduction_closed = (
        bulk_payload.get("bulk_carry_chain_normal_form_closed") is True
        and len(classified_rows) == bulk_payload.get("carry_break_count")
        and len(bridge_rows) + len(unit_rows) + len(nonunit_echo_rows) == len(classified_rows)
        and all_unit_echo_source_aligned
        and all_bridge_roots_packetized
        and total_break_debt == unit_echo_debt + bridge_debt
        and bridge_debt == packet_bridge_debt
    )

    return {
        "certificate_type": "prime_matrix_phi_lpf_terminal_boundary_carry_break_source_packet_router",
        "status": "carry_break_source_packets_closed_bridge_root_debt_open",
        "verified_date": "2026-05-25",
        "previous_bulk_carry_chain_normal_form_closed": bulk_payload.get(
            "bulk_carry_chain_normal_form_closed"
        )
        is True,
        "previous_old_residual_return_alignment_closed": old_return_payload.get(
            "old_residual_return_alignment_closed"
        )
        is True,
        "residual_flow_side_decomposition_closed": residual_payload.get(
            "residual_flow_side_decomposition_closed"
        )
        is True,
        "carry_break_count": len(break_rows),
        "unit_old_return_echo_break_count": len(unit_rows),
        "bridge_root_debt_break_count": len(bridge_rows),
        "nonunit_old_return_echo_break_count": len(nonunit_echo_rows),
        "unmatched_unit_break_count": len(unmatched_unit_rows),
        "paired_bridge_unit_packet_count": len(packet_rows),
        "all_unit_echo_breaks_source_aligned_to_old_returns": all_unit_echo_source_aligned,
        "all_bridge_roots_packetized_with_following_unit_echo": all_bridge_roots_packetized,
        "carry_break_source_packet_reduction_closed": source_packet_reduction_closed,
        "bridge_root_source_law_proved": False,
        "right_tail_overhang_pdec_constructed": False,
        "admissible_trace_or_typeii_family_constructed": False,
        "finite_group_orbit_expansion_family_constructed": False,
        "phi_lpf_parity_barrier_globally_broken": False,
        "row_column_unconditional_closed": False,
        "total_carry_break_debt_mass": frac_record(total_break_debt),
        "unit_old_return_echo_debt_mass": frac_record(unit_echo_debt),
        "bridge_root_debt_open_mass": frac_record(bridge_debt),
        "classified_break_rows": classified_rows,
        "bridge_root_debt_rows": bridge_rows,
        "unit_old_return_echo_rows": unit_rows,
        "packet_rows": packet_rows,
        "next_primary_attack_target": BRIDGE_ROOT_LAW,
        "plain_conclusion": (
            "4 carry breaks reduce to 2 paired bridge/unit packets: the two unit breaks "
            "echo already aligned old-return masses exactly, while the two bridge-root debts "
            "remain open source-law/PDEC obligations.  This is not an unconditional row/column proof."
        ),
        "gate_rows": [
            {
                "gate": "CarryBreakSourcePacketPartition",
                "closed": source_packet_reduction_closed,
                "proved": source_packet_reduction_closed,
                "meaning": "the 4 carry breaks are classified into unit old-return echoes and bridge-root debts.",
                "remaining": "finite carry-break source packet ledger",
            },
            {
                "gate": UNIT_OLD_RETURN_ECHO,
                "closed": all_unit_echo_source_aligned,
                "proved": all_unit_echo_source_aligned,
                "meaning": "both run_gap=1 carry-break debts equal already aligned old-side return masses.",
                "remaining": "old-return source echo, not new global cancellation",
            },
            {
                "gate": "BridgeRootEndpointAlignment",
                "closed": all_bridge_roots_packetized,
                "proved": all_bridge_roots_packetized,
                "meaning": "each bridge root is the new_q_start endpoint of the old-return mass echoed by the following unit break.",
                "remaining": BRIDGE_ROOT_LAW,
            },
            {
                "gate": "BridgeRootDebtSourceLaw",
                "closed": False,
                "proved": False,
                "meaning": "the two bridge-root debts are not yet generated by a uniform source law or named PDEC.",
                "remaining": BRIDGE_ROOT_LAW,
            },
            {
                "gate": "RightTailOverhangPDEC",
                "closed": False,
                "proved": False,
                "meaning": "the right selected-terminal tail overhang is unchanged from the previous layer.",
                "remaining": TAIL_OVERHANG_LAW,
            },
            {
                "gate": "ExternalTraceOrGroupEntry",
                "closed": False,
                "proved": False,
                "meaning": "trace/Kloosterman/Type-II or group-expansion inputs still need a signed family built from bridge roots.",
                "remaining": f"{TRACE_FAMILY} AND {GROUP_ORBIT_INPUT}",
            },
            {
                "gate": "RowColumnUnconditionalClosureReached",
                "closed": False,
                "proved": False,
                "meaning": "this is a finite source-packet reduction, not a global parity-breaking theorem.",
                "remaining": (
                    f"{BRIDGE_ROOT_LAW} AND {TAIL_OVERHANG_LAW} AND {MASS_RATIO_LAW} "
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
        "# Prime Matrix Phi-LPF terminal boundary carry-break source-packet 证书",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['verified_date']}`",
        "",
        "本证书把 bulk carry-chain normal form 中的 4 个 carry break 继续原子化。",
        "",
        "```text",
        f"previous_bulk_carry_chain_normal_form_closed={fmt_bool(payload['previous_bulk_carry_chain_normal_form_closed'])}",
        f"carry_break_count={payload['carry_break_count']}",
        f"unit_old_return_echo_break_count={payload['unit_old_return_echo_break_count']}",
        f"bridge_root_debt_break_count={payload['bridge_root_debt_break_count']}",
        f"paired_bridge_unit_packet_count={payload['paired_bridge_unit_packet_count']}",
        f"unmatched_unit_break_count={payload['unmatched_unit_break_count']}",
        f"all_unit_echo_breaks_source_aligned_to_old_returns={fmt_bool(payload['all_unit_echo_breaks_source_aligned_to_old_returns'])}",
        f"all_bridge_roots_packetized_with_following_unit_echo={fmt_bool(payload['all_bridge_roots_packetized_with_following_unit_echo'])}",
        f"carry_break_source_packet_reduction_closed={fmt_bool(payload['carry_break_source_packet_reduction_closed'])}",
        f"bridge_root_source_law_proved={fmt_bool(payload['bridge_root_source_law_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(payload['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. classified carry breaks",
        "",
        "| index | atom | class | prev run/q | root run/q | run gap | q gap | debt | old-return q | old-return new_q_start | return type |",
        "| ---: | --- | --- | --- | --- | ---: | ---: | --- | ---: | ---: | --- |",
    ]
    for row in payload["classified_break_rows"]:
        lines.append(
            "| {idx} | `{atom}` | `{cls}` | {prev_run}/{prev_q} | {root_run}/{root_q} | {run_gap} | {q_gap} | {debt} | {old_q} | {new_q} | `{rtype}` |".format(
                idx=row["break_index"],
                atom=cell(row["atom_key"]),
                cls=row["classification"],
                prev_run=row["previous_new_run_id"],
                prev_q=row["previous_boundary_q"],
                root_run=row["root_new_run_id"],
                root_q=row["root_boundary_q"],
                run_gap=row["run_gap"],
                q_gap=row["q_gap"],
                debt=render_fraction(row["break_debt"]),
                old_q=display(row["matched_old_return_boundary_q"]),
                new_q=display(row["matched_old_return_new_q_start"]),
                rtype=display(row["matched_old_return_type"]),
            )
        )

    lines.extend(
        [
            "",
            "## 2. bridge/unit packets",
            "",
            "| packet | atom | bridge root | unit root | old-return q -> new_q_start | bridge endpoint match | unit echo match | bridge debt | unit echo mass |",
            "| ---: | --- | --- | --- | --- | --- | --- | --- | --- |",
        ]
    )
    for row in payload["packet_rows"]:
        lines.append(
            "| {pid} | `{atom}` | run {br_run}/q {br_q} | run {unit_run}/q {unit_q} | {old_q}->{new_q} | `{endpoint}` | `{echo}` | {bridge} | {unit} |".format(
                pid=row["packet_id"],
                atom=cell(row["atom_key"]),
                br_run=row["bridge_root_run"],
                br_q=row["bridge_root_q"],
                unit_run=row["unit_root_run"],
                unit_q=row["unit_root_q"],
                old_q=row["old_return_boundary_q"],
                new_q=row["old_return_new_q_start"],
                endpoint=fmt_bool(row["bridge_root_matches_old_return_new_q_start"]),
                echo=fmt_bool(row["unit_debt_equals_old_return_mass"]),
                bridge=render_fraction(row["bridge_root_debt"]),
                unit=render_fraction(row["unit_old_return_echo_mass"]),
            )
        )

    lines.extend(
        [
            "",
            "## 3. mass ledger",
            "",
            "| mass | value |",
            "| --- | --- |",
            f"| total carry-break debt | {render_fraction(payload['total_carry_break_debt_mass'])} |",
            f"| unit old-return echo debt | {render_fraction(payload['unit_old_return_echo_debt_mass'])} |",
            f"| bridge-root debt still open | {render_fraction(payload['bridge_root_debt_open_mass'])} |",
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
            f"{BRIDGE_ROOT_LAW} AND {TAIL_OVERHANG_LAW} AND {MASS_RATIO_LAW} AND {ORIENTATION_LAW} AND {MOVING_BEATTY_SAVING} AND {TRACE_FAMILY} AND {GROUP_ORBIT_INPUT}",
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


def main() -> None:
    """命令入口。"""
    payload = build_certificate()
    write_outputs(payload)
    print(f"carry_break_count={payload['carry_break_count']}")
    print(f"unit_old_return_echo_break_count={payload['unit_old_return_echo_break_count']}")
    print(f"bridge_root_debt_break_count={payload['bridge_root_debt_break_count']}")
    print(f"paired_bridge_unit_packet_count={payload['paired_bridge_unit_packet_count']}")
    print(
        "carry_break_source_packet_reduction_closed="
        f"{fmt_bool(payload['carry_break_source_packet_reduction_closed'])}"
    )
    print(f"bridge_root_debt_open_mass={render_fraction(payload['bridge_root_debt_open_mass'])}")
    print(f"row_column_unconditional_closed={fmt_bool(payload['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
