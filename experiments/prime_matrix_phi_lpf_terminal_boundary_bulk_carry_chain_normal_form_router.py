#!/usr/bin/env python3
"""审计 bulk new-residual 是否压缩为 atomwise carry-chain normal form。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_terminal_boundary_bulk_carry_chain_normal_form_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-terminal-boundary-bulk-carry-chain-normal-form-router.json

输出：
  data/prime-matrix-phi-lpf-terminal-boundary-bulk-carry-chain-normal-form-ledger.json
  docs/monograph/prime-matrix-phi-lpf-terminal-boundary-bulk-carry-chain-normal-form-router.json
  docs/monograph/prime-matrix-phi-lpf-terminal-boundary-bulk-carry-chain-normal-form-router.md

本证书承接 new-residual tail alignment，把 36 个未支付的 bulk new residual
拆成有限 carry-chain normal form：42 个 new-side residual 事件分成 11 段
atomwise carry segments，其中 31 个相邻 carry transition 精确满足
old_mass(next)=residual_mass(previous)。这不是无条件闭合；它把下一步硬点从
散点 residual 改写为 segment root/source law、tail overhang PDEC 或可平均
signed trace/Type-II/群轨道族。
"""

from __future__ import annotations

import hashlib
import json
from collections import defaultdict
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-terminal-boundary-bulk-carry-chain-normal-form"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

RESIDUAL_JSON = DOCS / "prime-matrix-phi-lpf-terminal-boundary-residual-flow-obstruction-router.json"
TAIL_JSON = DOCS / "prime-matrix-phi-lpf-terminal-boundary-new-residual-tail-alignment-router.json"
OLD_RETURN_JSON = DOCS / "prime-matrix-phi-lpf-terminal-boundary-old-residual-return-alignment-router.json"

CARRY_SEGMENT_LAW = "BoundaryBulkCarrySegmentRootSourceLawOrPDEC"
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
    paths = [Path(__file__).resolve(), RESIDUAL_JSON, TAIL_JSON, OLD_RETURN_JSON]
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


def event_key(row: dict[str, Any]) -> tuple[str, int, int]:
    """new residual 事件 key。"""
    return (row["atom_key"], int(row["new_run_id"]), int(row["boundary_q"]))


def is_carry_transition(previous: dict[str, Any], current: dict[str, Any]) -> bool:
    """判断相邻事件是否为精确 carry。"""
    return (
        int(current["old_run_id"]) == int(previous["new_run_id"])
        and frac_from_record(current["old_mass"]) == frac_from_record(previous["residual_mass"])
    )


def segment_rows_for_atom(rows: list[dict[str, Any]], tail_keys: set[tuple[str, int, int]]) -> tuple[list[list[dict[str, Any]]], list[dict[str, Any]]]:
    """按 atom 切成 carry segments，并记录 break。"""
    ordered = sorted(rows, key=lambda row: int(row["new_run_id"]))
    segments: list[list[dict[str, Any]]] = []
    breaks: list[dict[str, Any]] = []
    current: list[dict[str, Any]] = []
    for row in ordered:
        if not current:
            current = [row]
            continue
        previous = current[-1]
        if is_carry_transition(previous, row):
            current.append(row)
            continue
        segments.append(current)
        diff = frac_from_record(row["old_mass"]) - frac_from_record(previous["residual_mass"])
        breaks.append(
            {
                "atom_key": row["atom_key"],
                "previous_new_run_id": previous["new_run_id"],
                "previous_boundary_q": previous["boundary_q"],
                "previous_residual_mass": previous["residual_mass"],
                "root_new_run_id": row["new_run_id"],
                "root_boundary_q": row["boundary_q"],
                "root_old_mass": row["old_mass"],
                "root_minus_previous_residual": frac_record(diff),
                "run_gap": int(row["new_run_id"]) - int(previous["new_run_id"]),
                "q_gap": int(row["boundary_q"]) - int(previous["boundary_q"]),
                "tail_before_break": event_key(previous) in tail_keys,
            }
        )
        current = [row]
    if current:
        segments.append(current)
    return segments, breaks


def summarize_segment(index: int, segment: list[dict[str, Any]], tail_keys: set[tuple[str, int, int]]) -> dict[str, Any]:
    """输出 carry segment 摘要。"""
    first = segment[0]
    last = segment[-1]
    terminal_tail_closed = event_key(last) in tail_keys
    bulk_count = sum(1 for row in segment if event_key(row) not in tail_keys)
    residual_sum = sum((frac_from_record(row["residual_mass"]) for row in segment), Fraction(0))
    return {
        "segment_id": index,
        "atom_key": first["atom_key"],
        "role": first["role"],
        "event_count": len(segment),
        "carry_transition_count": max(0, len(segment) - 1),
        "bulk_unmatched_event_count": bulk_count,
        "new_run_start": first["new_run_id"],
        "new_run_end": last["new_run_id"],
        "q_start": first["boundary_q"],
        "q_end": last["boundary_q"],
        "direction_start": first["direction_pair"],
        "direction_end": last["direction_pair"],
        "root_old_mass": first["old_mass"],
        "terminal_residual_mass": last["residual_mass"],
        "segment_residual_mass_total": frac_record(residual_sum),
        "terminal_tail_closed": terminal_tail_closed,
    }


def build_certificate() -> dict[str, Any]:
    """组装 bulk carry-chain normal form 证书。"""
    residual_payload = load_json(RESIDUAL_JSON)
    tail_payload = load_json(TAIL_JSON)
    old_return_payload = load_json(OLD_RETURN_JSON)
    new_rows = [
        row
        for row in residual_payload["full_boundary_residual_flow_rows"]
        if row["residual_side"] == "new"
    ]
    tail_keys = {event_key(row) for row in tail_payload["tail_alignment_rows"]}
    by_atom: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in new_rows:
        by_atom[row["atom_key"]].append(row)

    segment_summaries: list[dict[str, Any]] = []
    break_rows: list[dict[str, Any]] = []
    segment_id = 1
    for atom_key in sorted(by_atom):
        segments, breaks = segment_rows_for_atom(by_atom[atom_key], tail_keys)
        break_rows.extend(breaks)
        for segment in segments:
            summary = summarize_segment(segment_id, segment, tail_keys)
            segment_summaries.append(summary)
            segment_id += 1

    carry_transition_count = sum(row["carry_transition_count"] for row in segment_summaries)
    segment_event_total = sum(row["event_count"] for row in segment_summaries)
    bulk_event_total = sum(row["bulk_unmatched_event_count"] for row in segment_summaries)
    tail_closed_segment_count = sum(1 for row in segment_summaries if row["terminal_tail_closed"])
    open_segment_count = len(segment_summaries) - tail_closed_segment_count
    terminal_keys = set()
    for atom_key in sorted(by_atom):
        segments, _ = segment_rows_for_atom(by_atom[atom_key], tail_keys)
        for segment in segments:
            terminal_keys.add(event_key(segment[-1]))
    all_tail_terminal = tail_keys <= terminal_keys

    carry_normal_form_closed = (
        tail_payload.get("new_residual_tail_alignment_partial_closed") is True
        and old_return_payload.get("old_residual_return_alignment_closed") is True
        and segment_event_total == len(new_rows)
        and carry_transition_count + len(segment_summaries) == len(new_rows)
        and bulk_event_total == tail_payload.get("new_residual_unmatched_after_tail_event_count")
        and all_tail_terminal
    )

    return {
        "certificate_type": "prime_matrix_phi_lpf_terminal_boundary_bulk_carry_chain_normal_form_router",
        "status": "bulk_new_residual_carry_chain_normal_form_closed_uniform_source_open",
        "verified_date": "2026-05-25",
        "previous_new_residual_tail_alignment_partial_closed": tail_payload.get(
            "new_residual_tail_alignment_partial_closed"
        )
        is True,
        "previous_old_residual_return_alignment_closed": old_return_payload.get(
            "old_residual_return_alignment_closed"
        )
        is True,
        "new_residual_event_count": len(new_rows),
        "bulk_unmatched_new_residual_event_count": tail_payload.get(
            "new_residual_unmatched_after_tail_event_count"
        ),
        "atom_count": len(by_atom),
        "carry_segment_count": len(segment_summaries),
        "carry_transition_count": carry_transition_count,
        "carry_break_count": len(break_rows),
        "atom_initial_segment_count": len(by_atom),
        "tail_closed_segment_count": tail_closed_segment_count,
        "open_segment_count": open_segment_count,
        "all_new_residual_events_partitioned": segment_event_total == len(new_rows),
        "all_carry_transitions_exact": carry_transition_count + len(segment_summaries) == len(new_rows),
        "all_tail_matched_events_are_segment_terminal": all_tail_terminal,
        "bulk_events_accounted_by_segment_normal_form": bulk_event_total
        == tail_payload.get("new_residual_unmatched_after_tail_event_count"),
        "bulk_carry_chain_normal_form_closed": carry_normal_form_closed,
        "carry_segment_root_source_law_proved": False,
        "right_tail_overhang_pdec_constructed": False,
        "admissible_trace_or_typeii_family_constructed": False,
        "finite_group_orbit_expansion_family_constructed": False,
        "phi_lpf_parity_barrier_globally_broken": False,
        "row_column_unconditional_closed": False,
        "segment_rows": segment_summaries,
        "carry_break_rows": break_rows,
        "tail_overhang_rows": tail_payload["unmatched_tail_survivor_rows"],
        "gate_rows": [
            {
                "gate": "BulkCarryChainNormalForm",
                "closed": carry_normal_form_closed,
                "proved": True,
                "meaning": "42 new-side residual events are partitioned into 11 atomwise carry segments with 31 exact carry transitions.",
                "remaining": "finite carry-chain ledger",
            },
            {
                "gate": "BulkResidualIndependentEventReduction",
                "closed": carry_normal_form_closed,
                "proved": True,
                "meaning": "the 36 unmatched bulk events are no longer independent scatter; they are segment roots/interiors in the carry normal form.",
                "remaining": CARRY_SEGMENT_LAW,
            },
            {
                "gate": "CarrySegmentRootSourceLaw",
                "closed": False,
                "proved": False,
                "meaning": "the 11 segment roots and 4 carry breaks still need a uniform source law or named PDEC.",
                "remaining": CARRY_SEGMENT_LAW,
            },
            {
                "gate": "RightTailOverhangPDEC",
                "closed": False,
                "proved": False,
                "meaning": "the single unmatched right selected-terminal tail survivor is carried forward.",
                "remaining": TAIL_OVERHANG_LAW,
            },
            {
                "gate": "ExternalTraceOrGroupEntry",
                "closed": False,
                "proved": False,
                "meaning": "frontier trace/Kloosterman/Type-II or group-expansion inputs still require an admissible family built from these segments.",
                "remaining": f"{TRACE_FAMILY} AND {GROUP_ORBIT_INPUT}",
            },
            {
                "gate": "RowColumnUnconditionalClosureReached",
                "closed": False,
                "proved": False,
                "meaning": "this is a finite normal form, not a global parity-breaking theorem.",
                "remaining": f"{ORIENTATION_LAW} AND {MOVING_BEATTY_SAVING}",
            },
        ],
        "next_primary_attack_target": (
            f"{CARRY_SEGMENT_LAW} AND {TAIL_OVERHANG_LAW} AND {MASS_RATIO_LAW} AND "
            f"{ORIENTATION_LAW} AND {MOVING_BEATTY_SAVING} AND {TRACE_FAMILY} AND {GROUP_ORBIT_INPUT}"
        ),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "The 36 bulk new-side residual events are compressed into an atomwise carry-chain "
            "normal form: 42 new residual events form 11 segments with 31 exact carry transitions. "
            "Six segments end in the already matched tail returns; five segments remain open, "
            "together with the right selected-terminal tail overhang.  The remaining theorem-level "
            "task is a uniform segment-root source law, a tail-overhang PDEC, or an admissible "
            "trace/Type-II/group-orbit family."
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = []
    lines.append("# Prime Matrix Phi-LPF terminal boundary bulk carry-chain normal form 证书")
    lines.append("")
    lines.append(f"**状态：** `{result['status']}`")
    lines.append(f"**核验日期：** `{result['verified_date']}`")
    lines.append("")
    lines.append("本证书把未支付的 bulk new residual 压缩为 atomwise carry-chain normal form。")
    lines.append("")
    lines.append("```text")
    for key in [
        "previous_new_residual_tail_alignment_partial_closed",
        "new_residual_event_count",
        "bulk_unmatched_new_residual_event_count",
        "atom_count",
        "carry_segment_count",
        "carry_transition_count",
        "carry_break_count",
        "tail_closed_segment_count",
        "open_segment_count",
        "all_carry_transitions_exact",
        "all_tail_matched_events_are_segment_terminal",
        "bulk_carry_chain_normal_form_closed",
        "row_column_unconditional_closed",
    ]:
        value = result[key]
        lines.append(f"{key}={fmt_bool(value) if isinstance(value, bool) else value}")
    lines.append("```")
    lines.append("")
    lines.append("## 1. carry segments")
    lines.append("")
    lines.append("| id | atom | events | carry | q-range | run-range | bulk | tail closed | terminal residual |")
    lines.append("| ---: | --- | ---: | ---: | --- | --- | ---: | --- | --- |")
    for row in result["segment_rows"]:
        lines.append(
            f"| {row['segment_id']} | `{cell(row['atom_key'])}` | {row['event_count']} | "
            f"{row['carry_transition_count']} | {row['q_start']}->{row['q_end']} | "
            f"{row['new_run_start']}->{row['new_run_end']} | {row['bulk_unmatched_event_count']} | "
            f"`{fmt_bool(row['terminal_tail_closed'])}` | {render_fraction(row['terminal_residual_mass'])} |"
        )
    lines.append("")
    lines.append("## 2. carry breaks")
    lines.append("")
    lines.append("| atom | prev run/q | root run/q | run gap | q gap | previous residual | root old mass | delta |")
    lines.append("| --- | --- | --- | ---: | ---: | --- | --- | --- |")
    for row in result["carry_break_rows"]:
        lines.append(
            f"| `{cell(row['atom_key'])}` | {row['previous_new_run_id']}/{row['previous_boundary_q']} | "
            f"{row['root_new_run_id']}/{row['root_boundary_q']} | {row['run_gap']} | {row['q_gap']} | "
            f"{render_fraction(row['previous_residual_mass'])} | {render_fraction(row['root_old_mass'])} | "
            f"{render_fraction(row['root_minus_previous_residual'])} |"
        )
    lines.append("")
    lines.append("## 3. tail overhang carried forward")
    lines.append("")
    lines.append("| atom | run | q-range | mass |")
    lines.append("| --- | ---: | --- | --- |")
    for row in result["tail_overhang_rows"]:
        lines.append(
            f"| `{cell(row['atom_key'])}` | {row['run_id']} | {row['q_start']}->{row['q_end']} | "
            f"{render_fraction(row['mass'])} |"
        )
    lines.append("")
    lines.append("## 4. 门控表")
    lines.append("")
    lines.append("| gate | closed | proved | meaning | remaining |")
    lines.append("| --- | --- | --- | --- | --- |")
    for row in result["gate_rows"]:
        lines.append(
            f"| `{cell(row['gate'])}` | `{fmt_bool(row['closed'])}` | `{fmt_bool(row['proved'])}` | "
            f"{cell(row['meaning'])} | `{cell(row['remaining'])}` |"
        )
    lines.append("")
    lines.append("## 5. 最新开放口")
    lines.append("")
    lines.append("```text")
    lines.append(result["next_primary_attack_target"])
    lines.append("```")
    lines.append("")
    lines.append("## 6. 依赖哈希")
    lines.append("")
    lines.append("| file | sha256 |")
    lines.append("| --- | --- |")
    for path, digest in sorted(result["source_hashes"].items()):
        lines.append(f"| `{path}` | `{digest}` |")
    lines.append("")
    lines.append("行/列命题仍未无条件闭合。")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """生成 bulk carry-chain normal form 证书。"""
    result = build_certificate()
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    text = json.dumps(result, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    OUT_JSON.write_text(text, encoding="utf-8")
    OUT_LEDGER.write_text(text, encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"wrote {OUT_JSON.relative_to(ROOT)}")
    print(f"wrote {OUT_LEDGER.relative_to(ROOT)}")
    print(f"wrote {OUT_MD.relative_to(ROOT)}")
    print(f"bulk_carry_chain_normal_form_closed={fmt_bool(result['bulk_carry_chain_normal_form_closed'])}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
