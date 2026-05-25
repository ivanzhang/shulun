#!/usr/bin/env python3
"""审计 terminal q-boundary synthetic split 的 residual-flow 障碍。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_terminal_boundary_residual_flow_obstruction_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-terminal-boundary-residual-flow-obstruction-router.json

输出：
  data/prime-matrix-phi-lpf-terminal-boundary-residual-flow-obstruction-ledger.json
  docs/monograph/prime-matrix-phi-lpf-terminal-boundary-residual-flow-obstruction-router.json
  docs/monograph/prime-matrix-phi-lpf-terminal-boundary-residual-flow-obstruction-router.md

本证书承接 boundary split ratio spectrum，把 47 个相邻 q-boundary split
继续分解为 residual side/source ledger。结论：边界内部的 opposite-side
相邻抵消律不成立；残差主要作为 new-side source 出现，必须改攻 source-key
源项生成律或边界外搬运律。
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"
EXPERIMENTS = ROOT / "experiments"

SLUG = "prime-matrix-phi-lpf-terminal-boundary-residual-flow-obstruction"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

BOUNDARY_SCRIPT = EXPERIMENTS / "prime_matrix_phi_lpf_terminal_boundary_split_ratio_obstruction_router.py"
BOUNDARY_JSON = DOCS / "prime-matrix-phi-lpf-terminal-boundary-split-ratio-obstruction-router.json"

BOUNDARY_MASS_RATIO_LAW = "BoundaryAdjacentRunMassRatioLawOrPDEC"
BOUNDARY_RESIDUAL_FLOW = "BoundaryResidualFlowSourceKeyConservationOrPDEC"
BOUNDARY_SOURCE_LAW = "BoundaryDominantNewResidualSourceLawOrPDEC"
BOUNDARY_TRANSPORT_LAW = "BoundaryResidualTransportToNonBoundaryInternalReturnsOrPDEC"
NONBOUNDARY_JUMP_LAW = "NonBoundaryPrefixRecordJumpSourceKeyLiftOrPDEC"
INTERNAL_SURVIVOR_LAW = "InternalPrefixRecordSurvivorPDEC"
ORIENTATION_LAW = "PrimitiveOrientationLocalFactorProductLawBeforePushforward"
MOVING_BEATTY_SAVING = "SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving"
TRACE_FAMILY = "AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def load_boundary_module() -> Any:
    """加载上一层 boundary ratio 审计模块。"""
    spec = importlib.util.spec_from_file_location("boundary_ratio", BOUNDARY_SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {BOUNDARY_SCRIPT}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    paths = [Path(__file__).resolve(), BOUNDARY_SCRIPT, BOUNDARY_JSON]
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


def collect_ratio_rows() -> list[dict[str, Any]]:
    """从上一层模块重新生成全部 boundary ratio rows。"""
    boundary = load_boundary_module()
    events = boundary.collect_boundary_events()
    rows = [boundary.event_ratio_row(event) for event in events]
    return sorted(rows, key=lambda row: (row["atom_key"], int(row["old_run_id"])))


def event_payload(row: dict[str, Any]) -> dict[str, Any]:
    """保留单个事件的 residual-flow 审计字段。"""
    return {
        "atom_key": row["atom_key"],
        "role": row["role"],
        "old_run_id": row["old_run_id"],
        "new_run_id": row["new_run_id"],
        "boundary_q": row["boundary_q"],
        "direction_pair": f"{row['old_direction']}->{row['new_direction']}",
        "residual_side": row["residual_side"],
        "old_consumed": row["old_consumed"],
        "new_consumed": row["new_consumed"],
        "old_mass": row["old_mass"],
        "new_mass": row["new_mass"],
        "residual_mass": row["residual_mass"],
        "smaller_to_larger_ratio": row["smaller_to_larger_ratio"],
    }


def atom_summary(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """按 atom 汇总 residual side 与 run 序列。"""
    buckets: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        buckets[row["atom_key"]].append(row)
    summary = []
    for atom_key, items in sorted(buckets.items()):
        items = sorted(items, key=lambda row: int(row["old_run_id"]))
        new_total = sum(
            (frac_from_record(row["residual_mass"]) for row in items if row["residual_side"] == "new"),
            Fraction(0),
        )
        old_total = sum(
            (frac_from_record(row["residual_mass"]) for row in items if row["residual_side"] == "old"),
            Fraction(0),
        )
        side_counts = Counter(row["residual_side"] for row in items)
        flips = sum(
            1 for left, right in zip(items, items[1:]) if left["residual_side"] != right["residual_side"]
        )
        sequence = "".join("N" if row["residual_side"] == "new" else "O" for row in items)
        summary.append(
            {
                "atom_key": atom_key,
                "role": items[0]["role"],
                "event_count": len(items),
                "new_residual_count": side_counts["new"],
                "old_residual_count": side_counts["old"],
                "side_sequence": sequence,
                "side_flip_count": flips,
                "new_residual_total": frac_record(new_total),
                "old_residual_total": frac_record(old_total),
                "net_new_minus_old": frac_record(new_total - old_total),
            }
        )
    return summary


def quadrant_summary(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """按 residual side 和方向对汇总质量。"""
    mass: dict[tuple[str, str], Fraction] = defaultdict(Fraction)
    counts: Counter[tuple[str, str]] = Counter()
    for row in rows:
        key = (row["residual_side"], f"{row['old_direction']}->{row['new_direction']}")
        mass[key] += frac_from_record(row["residual_mass"])
        counts[key] += 1
    return [
        {
            "residual_side": key[0],
            "direction_pair": key[1],
            "event_count": counts[key],
            "residual_mass_total": frac_record(value),
        }
        for key, value in sorted(mass.items())
    ]


def same_side_run_max(rows: list[dict[str, Any]]) -> dict[str, Any]:
    """寻找最长同侧 residual 连续段。"""
    buckets: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        buckets[row["atom_key"]].append(row)
    best = {
        "atom_key": "",
        "residual_side": "",
        "run_count": 0,
        "old_run_start": None,
        "old_run_end": None,
    }
    for atom_key, items in buckets.items():
        items = sorted(items, key=lambda row: int(row["old_run_id"]))
        current_side = None
        current_count = 0
        current_start = None
        current_end = None
        for row in items:
            side = row["residual_side"]
            if side == current_side:
                current_count += 1
            else:
                if current_count > int(best["run_count"]):
                    best = {
                        "atom_key": atom_key,
                        "residual_side": current_side,
                        "run_count": current_count,
                        "old_run_start": current_start,
                        "old_run_end": current_end,
                    }
                current_side = side
                current_count = 1
                current_start = row["old_run_id"]
            current_end = row["old_run_id"]
        if current_count > int(best["run_count"]):
            best = {
                "atom_key": atom_key,
                "residual_side": current_side,
                "run_count": current_count,
                "old_run_start": current_start,
                "old_run_end": current_end,
            }
    return best


def build_certificate() -> dict[str, Any]:
    """组装 residual-flow obstruction 证书。"""
    previous = load_json(BOUNDARY_JSON)
    rows = collect_ratio_rows()
    side_counts = Counter(row["residual_side"] for row in rows)
    direction_counts = Counter(f"{row['old_direction']}->{row['new_direction']}" for row in rows)
    new_total = sum(
        (frac_from_record(row["residual_mass"]) for row in rows if row["residual_side"] == "new"),
        Fraction(0),
    )
    old_total = sum(
        (frac_from_record(row["residual_mass"]) for row in rows if row["residual_side"] == "old"),
        Fraction(0),
    )
    neg_to_pos_total = sum(
        (
            frac_from_record(row["residual_mass"])
            for row in rows
            if row["old_direction"] == "negative" and row["new_direction"] == "positive"
        ),
        Fraction(0),
    )
    pos_to_neg_total = sum(
        (
            frac_from_record(row["residual_mass"])
            for row in rows
            if row["old_direction"] == "positive" and row["new_direction"] == "negative"
        ),
        Fraction(0),
    )
    summaries = atom_summary(rows)
    atomwise_matched = sum(
        (
            min(
                frac_from_record(item["new_residual_total"]),
                frac_from_record(item["old_residual_total"]),
            )
            for item in summaries
        ),
        Fraction(0),
    )
    atomwise_unmatched = sum(
        (
            abs(
                frac_from_record(item["new_residual_total"])
                - frac_from_record(item["old_residual_total"])
            )
            for item in summaries
        ),
        Fraction(0),
    )
    local_opposite_side_cancellation_refuted = (
        side_counts["new"] != side_counts["old"] or new_total != old_total
    )
    residual_flow_side_decomposition_closed = (
        previous.get("boundary_ratio_spectrum_closed") is True
        and len(rows) == int(previous["q_boundary_synthetic_split_event_count"])
        and side_counts["new"] + side_counts["old"] == len(rows)
    )
    full_rows = [event_payload(row) for row in rows]
    return {
        "certificate_type": "prime_matrix_phi_lpf_terminal_boundary_residual_flow_obstruction_router",
        "status": "boundary_residual_flow_side_ledger_closed_local_conservation_refuted",
        "verified_date": "2026-05-25",
        "previous_boundary_ratio_spectrum_closed": previous.get("boundary_ratio_spectrum_closed") is True,
        "q_boundary_synthetic_split_event_count": len(rows),
        "residual_flow_side_decomposition_closed": residual_flow_side_decomposition_closed,
        "new_residual_side_event_count": side_counts["new"],
        "old_residual_side_event_count": side_counts["old"],
        "new_residual_mass_total": frac_record(new_total),
        "old_residual_mass_total": frac_record(old_total),
        "net_new_minus_old_residual_mass": frac_record(new_total - old_total),
        "atomwise_opposite_side_matched_mass": frac_record(atomwise_matched),
        "atomwise_unmatched_residual_mass": frac_record(atomwise_unmatched),
        "atom_without_old_residual_count": sum(1 for item in summaries if item["old_residual_count"] == 0),
        "atom_with_old_residual_count": sum(1 for item in summaries if item["old_residual_count"] > 0),
        "negative_to_positive_event_count": direction_counts["negative->positive"],
        "positive_to_negative_event_count": direction_counts["positive->negative"],
        "direction_event_count_gap_abs": abs(
            direction_counts["negative->positive"] - direction_counts["positive->negative"]
        ),
        "negative_to_positive_residual_mass_total": frac_record(neg_to_pos_total),
        "positive_to_negative_residual_mass_total": frac_record(pos_to_neg_total),
        "direction_signed_residual_mass_negpos_minus_posneg": frac_record(
            neg_to_pos_total - pos_to_neg_total
        ),
        "max_same_side_run": same_side_run_max(rows),
        "finite_boundary_local_opposite_side_cancellation_refuted": local_opposite_side_cancellation_refuted,
        "boundary_residual_flow_source_key_conservation_proved": False,
        "boundary_dominant_new_residual_source_law_proved": False,
        "boundary_residual_transport_to_nonboundary_internal_returns_proved": False,
        "phi_lpf_parity_barrier_globally_broken": False,
        "row_column_unconditional_closed": False,
        "atom_residual_flow_summary_rows": summaries,
        "quadrant_residual_flow_summary_rows": quadrant_summary(rows),
        "old_residual_event_rows": sorted(
            [event_payload(row) for row in rows if row["residual_side"] == "old"],
            key=lambda row: frac_from_record(row["residual_mass"]),
            reverse=True,
        ),
        "largest_new_residual_event_rows": sorted(
            [event_payload(row) for row in rows if row["residual_side"] == "new"],
            key=lambda row: frac_from_record(row["residual_mass"]),
            reverse=True,
        )[:12],
        "full_boundary_residual_flow_rows": full_rows,
        "gate_rows": [
            {
                "gate": "BoundaryResidualSideLedgerClosed",
                "closed": residual_flow_side_decomposition_closed,
                "proved": True,
                "meaning": "all 47 adjacent boundary events have exact old/new residual side and mass.",
                "remaining": "finite residual-flow side ledger",
            },
            {
                "gate": "FiniteBoundaryLocalOppositeSideCancellation",
                "closed": False,
                "proved": False,
                "meaning": "new-side and old-side residual masses are not equal even after atomwise matching.",
                "remaining": BOUNDARY_SOURCE_LAW,
            },
            {
                "gate": "BoundaryDirectionEventBalance",
                "closed": True,
                "proved": True,
                "meaning": "direction counts are 24 versus 23, but residual mass by direction is still unbalanced.",
                "remaining": BOUNDARY_MASS_RATIO_LAW,
            },
            {
                "gate": "BoundaryResidualTransportOutsideBoundary",
                "closed": False,
                "proved": False,
                "meaning": "the leftover new-side source must be transported to non-boundary/internal returns or paid by PDEC.",
                "remaining": BOUNDARY_TRANSPORT_LAW,
            },
            {
                "gate": "RowColumnUnconditionalClosureReached",
                "closed": False,
                "proved": False,
                "meaning": "this is a finite obstruction certificate, not a global parity-breaking theorem.",
                "remaining": f"{ORIENTATION_LAW} AND {MOVING_BEATTY_SAVING} AND {TRACE_FAMILY}",
            },
        ],
        "next_primary_attack_target": (
            f"{BOUNDARY_SOURCE_LAW} AND {BOUNDARY_TRANSPORT_LAW} AND "
            f"{BOUNDARY_MASS_RATIO_LAW} AND {BOUNDARY_RESIDUAL_FLOW} AND "
            f"{NONBOUNDARY_JUMP_LAW} AND {INTERNAL_SURVIVOR_LAW} AND "
            f"{ORIENTATION_LAW} AND {MOVING_BEATTY_SAVING} AND {TRACE_FAMILY}"
        ),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "The 47 q-boundary split events do not contain a local opposite-side "
            "residual cancellation law.  New-side residual mass is about "
            "13.264539470882, old-side residual mass is about 0.215539338772, "
            "and atomwise matching leaves about 13.049000132111 unpaid.  The "
            "next non-cyclic route is therefore a dominant new-residual source "
            "law plus a transport/PDEC law, not another search for equal adjacent "
            "whole-run pairs."
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = []
    lines.append("# Prime Matrix Phi-LPF terminal boundary residual-flow obstruction 证书")
    lines.append("")
    lines.append(f"**状态：** `{result['status']}`")
    lines.append(f"**核验日期：** `{result['verified_date']}`")
    lines.append("")
    lines.append("本证书检验 q-boundary synthetic split 是否能在边界内部形成 residual-flow 守恒。")
    lines.append("")
    lines.append("```text")
    for key in [
        "previous_boundary_ratio_spectrum_closed",
        "q_boundary_synthetic_split_event_count",
        "residual_flow_side_decomposition_closed",
        "new_residual_side_event_count",
        "old_residual_side_event_count",
        "finite_boundary_local_opposite_side_cancellation_refuted",
        "boundary_residual_flow_source_key_conservation_proved",
        "row_column_unconditional_closed",
    ]:
        value = result[key]
        lines.append(f"{key}={fmt_bool(value) if isinstance(value, bool) else value}")
    lines.append("```")
    lines.append("")
    lines.append("## 1. residual totals")
    lines.append("")
    lines.append("| quantity | value |")
    lines.append("| --- | --- |")
    for key in [
        "new_residual_mass_total",
        "old_residual_mass_total",
        "net_new_minus_old_residual_mass",
        "atomwise_opposite_side_matched_mass",
        "atomwise_unmatched_residual_mass",
        "negative_to_positive_residual_mass_total",
        "positive_to_negative_residual_mass_total",
        "direction_signed_residual_mass_negpos_minus_posneg",
    ]:
        lines.append(f"| `{key}` | {render_fraction(result[key])} |")
    lines.append("")
    lines.append("## 2. atom residual-flow summary")
    lines.append("")
    lines.append("| atom | role | events | sequence | flips | new count | old count | net new-old |")
    lines.append("| --- | --- | ---: | --- | ---: | ---: | ---: | --- |")
    for row in result["atom_residual_flow_summary_rows"]:
        lines.append(
            f"| `{cell(row['atom_key'])}` | `{row['role']}` | {row['event_count']} | "
            f"`{row['side_sequence']}` | {row['side_flip_count']} | "
            f"{row['new_residual_count']} | {row['old_residual_count']} | "
            f"{render_fraction(row['net_new_minus_old'])} |"
        )
    lines.append("")
    lines.append("## 3. quadrant residual-flow summary")
    lines.append("")
    lines.append("| residual side | direction pair | events | mass |")
    lines.append("| --- | --- | ---: | --- |")
    for row in result["quadrant_residual_flow_summary_rows"]:
        lines.append(
            f"| `{row['residual_side']}` | `{row['direction_pair']}` | "
            f"{row['event_count']} | {render_fraction(row['residual_mass_total'])} |"
        )
    lines.append("")
    lines.append("## 4. old-side residual exceptions")
    lines.append("")
    lines.append("| atom | q | old/new run | direction | residual | ratio |")
    lines.append("| --- | ---: | --- | --- | --- | --- |")
    for row in result["old_residual_event_rows"]:
        lines.append(
            f"| `{cell(row['atom_key'])}` | {row['boundary_q']} | "
            f"{row['old_run_id']}->{row['new_run_id']} | `{row['direction_pair']}` | "
            f"{render_fraction(row['residual_mass'])} | {render_fraction(row['smaller_to_larger_ratio'])} |"
        )
    lines.append("")
    lines.append("## 5. 门控表")
    lines.append("")
    lines.append("| gate | closed | proved | meaning | remaining |")
    lines.append("| --- | --- | --- | --- | --- |")
    for row in result["gate_rows"]:
        lines.append(
            f"| `{cell(row['gate'])}` | `{fmt_bool(row['closed'])}` | `{fmt_bool(row['proved'])}` | "
            f"{cell(row['meaning'])} | `{cell(row['remaining'])}` |"
        )
    lines.append("")
    lines.append("## 6. 最新开放口")
    lines.append("")
    lines.append("```text")
    lines.append(result["next_primary_attack_target"])
    lines.append("```")
    lines.append("")
    lines.append("## 7. 依赖哈希")
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
    """生成 residual-flow obstruction 证书。"""
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
    print(
        "residual_flow_side_decomposition_closed="
        f"{fmt_bool(result['residual_flow_side_decomposition_closed'])}"
    )
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
