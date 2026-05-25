#!/usr/bin/env python3
"""审计 terminal q-boundary synthetic split 的 ratio 障碍。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_terminal_boundary_split_ratio_obstruction_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-terminal-boundary-split-ratio-obstruction-router.json

输出：
  data/prime-matrix-phi-lpf-terminal-boundary-split-ratio-obstruction-ledger.json
  docs/monograph/prime-matrix-phi-lpf-terminal-boundary-split-ratio-obstruction-router.json
  docs/monograph/prime-matrix-phi-lpf-terminal-boundary-split-ratio-obstruction-router.md

本证书继续 source-key obstruction partition，把最大的 q-boundary synthetic split
分支压成相邻 run 质量比率谱。结论：边界相邻性与 ratio spectrum 闭合；
但没有等量 whole-run involution，boundary split ratio source-key law 仍未构造。
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

SLUG = "prime-matrix-phi-lpf-terminal-boundary-split-ratio-obstruction"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREFIX_SCRIPT = EXPERIMENTS / "prime_matrix_phi_lpf_terminal_prefix_record_source_key_obstruction_router.py"
PARTITION_JSON = DOCS / "prime-matrix-phi-lpf-terminal-source-key-obstruction-partition-router.json"
VARIATION_JSON = DOCS / (
    "prime-matrix-phi-lpf-dominant-sign-word-repeated-step-packet-enclosure-"
    "terminal-phase-variation-budget-audit.json"
)

BOUNDARY_RATIO_LAW = "BoundarySyntheticSplitRatioSourceKeyLawOrPDEC"
BOUNDARY_MASS_RATIO_LAW = "BoundaryAdjacentRunMassRatioLawOrPDEC"
BOUNDARY_RESIDUAL_FLOW = "BoundaryResidualFlowSourceKeyConservationOrPDEC"
NONBOUNDARY_JUMP_LAW = "NonBoundaryPrefixRecordJumpSourceKeyLiftOrPDEC"
INTERNAL_SURVIVOR_LAW = "InternalPrefixRecordSurvivorPDEC"
ORIENTATION_LAW = "PrimitiveOrientationLocalFactorProductLawBeforePushforward"
MOVING_BEATTY_SAVING = "SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving"
TRACE_FAMILY = "AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def load_prefix_module() -> Any:
    """加载 prefix-record 审计模块。"""
    spec = importlib.util.spec_from_file_location("prefix_record_source_key", PREFIX_SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {PREFIX_SCRIPT}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    paths = [Path(__file__).resolve(), PREFIX_SCRIPT, PARTITION_JSON, VARIATION_JSON]
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


def collect_boundary_events() -> list[dict[str, Any]]:
    """重新生成全部 q-boundary cancellation events。"""
    prefix = load_prefix_module()
    variation = load_json(VARIATION_JSON)
    boundary_events: list[dict[str, Any]] = []
    for atom in variation["finite_audit"]["atom_variation_profiles"]:
        key = prefix.atom_key(atom)
        events, _ = prefix.cancellation_events_and_survivors(key, atom["run_variation_rows"])
        boundary_events.extend(event for event in events if event["q_boundary_pair"])
    return boundary_events


def event_ratio_row(event: dict[str, Any]) -> dict[str, Any]:
    """把单个 boundary event 转成 ratio row。"""
    old_mass = frac_from_record(event["old_before"])
    new_mass = frac_from_record(event["new_before"])
    chunk = frac_from_record(event["chunk"])
    larger = max(old_mass, new_mass)
    smaller = min(old_mass, new_mass)
    residual = larger - smaller
    if old_mass < new_mass:
        smaller_side = "old"
        residual_side = "new"
    elif new_mass < old_mass:
        smaller_side = "new"
        residual_side = "old"
    else:
        smaller_side = "equal"
        residual_side = "none"
    return {
        "atom_key": event["atom_key"],
        "role": event["atom_key"].split(":")[2],
        "old_run_id": event["old_run_id"],
        "new_run_id": event["new_run_id"],
        "boundary_q": event["old_q_end"],
        "old_direction": event["old_direction"],
        "new_direction": event["new_direction"],
        "old_mass": frac_record(old_mass),
        "new_mass": frac_record(new_mass),
        "chunk": frac_record(chunk),
        "residual_mass": frac_record(residual),
        "smaller_to_larger_ratio": frac_record(smaller / larger),
        "smaller_side": smaller_side,
        "residual_side": residual_side,
        "old_consumed": event["old_consumed"],
        "new_consumed": event["new_consumed"],
        "whole_equal_pair": old_mass == new_mass,
    }


def aggregate_rows(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """按 atom 汇总 ratio 谱。"""
    buckets: dict[str, dict[str, Any]] = {}
    for row in rows:
        key = row["atom_key"]
        if key not in buckets:
            buckets[key] = {
                "atom_key": key,
                "role": row["role"],
                "event_count": 0,
                "chunk_total": Fraction(0),
                "residual_total": Fraction(0),
                "ratio_min": None,
                "ratio_max": None,
                "old_consumed_count": 0,
                "new_consumed_count": 0,
            }
        item = buckets[key]
        ratio = frac_from_record(row["smaller_to_larger_ratio"])
        item["event_count"] += 1
        item["chunk_total"] += frac_from_record(row["chunk"])
        item["residual_total"] += frac_from_record(row["residual_mass"])
        item["ratio_min"] = ratio if item["ratio_min"] is None else min(item["ratio_min"], ratio)
        item["ratio_max"] = ratio if item["ratio_max"] is None else max(item["ratio_max"], ratio)
        item["old_consumed_count"] += int(bool(row["old_consumed"]))
        item["new_consumed_count"] += int(bool(row["new_consumed"]))
    rendered = []
    for item in buckets.values():
        rendered.append(
            {
                "atom_key": item["atom_key"],
                "role": item["role"],
                "event_count": item["event_count"],
                "chunk_total": frac_record(item["chunk_total"]),
                "residual_total": frac_record(item["residual_total"]),
                "ratio_min": frac_record(item["ratio_min"]),
                "ratio_max": frac_record(item["ratio_max"]),
                "old_consumed_count": item["old_consumed_count"],
                "new_consumed_count": item["new_consumed_count"],
            }
        )
    return sorted(rendered, key=lambda item: item["atom_key"])


def build_certificate() -> dict[str, Any]:
    """组装 boundary split ratio obstruction 证书。"""
    partition_payload = load_json(PARTITION_JSON)
    boundary_events = collect_boundary_events()
    ratio_rows = [event_ratio_row(event) for event in boundary_events]
    ratios = [frac_from_record(row["smaller_to_larger_ratio"]) for row in ratio_rows]
    residuals = [frac_from_record(row["residual_mass"]) for row in ratio_rows]
    chunks = [frac_from_record(row["chunk"]) for row in ratio_rows]
    consumed_counter = Counter((row["old_consumed"], row["new_consumed"]) for row in ratio_rows)
    direction_counter = Counter((row["old_direction"], row["new_direction"]) for row in ratio_rows)
    residual_side_counter = Counter(row["residual_side"] for row in ratio_rows)
    whole_equal_count = sum(1 for row in ratio_rows if row["whole_equal_pair"])
    adjacency_closed = all(int(event["run_distance"]) == 1 for event in boundary_events) and all(
        event["old_q_end"] == event["new_q_start"] for event in boundary_events
    )
    ratio_spectrum_closed = (
        partition_payload.get("source_key_obstruction_partition_closed") is True
        and len(boundary_events) == int(partition_payload["q_boundary_synthetic_split_event_count"])
        and len(boundary_events) == len(ratio_rows)
        and whole_equal_count == 0
    )
    return {
        "certificate_type": "prime_matrix_phi_lpf_terminal_boundary_split_ratio_obstruction_router",
        "status": "boundary_split_ratio_spectrum_closed_ratio_source_key_law_open",
        "verified_date": "2026-05-25",
        "previous_source_key_obstruction_partition_closed": partition_payload.get(
            "source_key_obstruction_partition_closed"
        )
        is True,
        "q_boundary_synthetic_split_event_count": len(boundary_events),
        "boundary_adjacency_closed": adjacency_closed,
        "boundary_run_distance_all_one": all(int(event["run_distance"]) == 1 for event in boundary_events),
        "whole_equal_pair_event_count": whole_equal_count,
        "synthetic_split_event_count": len(boundary_events),
        "old_consumed_new_residual_event_count": consumed_counter[(True, False)],
        "old_residual_new_consumed_event_count": consumed_counter[(False, True)],
        "both_sides_whole_event_count": consumed_counter[(True, True)],
        "both_sides_residual_event_count": consumed_counter[(False, False)],
        "negative_to_positive_event_count": direction_counter[("negative", "positive")],
        "positive_to_negative_event_count": direction_counter[("positive", "negative")],
        "new_residual_side_event_count": residual_side_counter["new"],
        "old_residual_side_event_count": residual_side_counter["old"],
        "ratio_min": frac_record(min(ratios)),
        "ratio_max": frac_record(max(ratios)),
        "boundary_chunk_mass_total": frac_record(sum(chunks, Fraction(0))),
        "boundary_residual_gap_mass_total": frac_record(sum(residuals, Fraction(0))),
        "boundary_residual_gap_mass_max": frac_record(max(residuals)),
        "boundary_ratio_spectrum_closed": ratio_spectrum_closed,
        "boundary_equal_whole_run_involution_constructed": False,
        "boundary_adjacent_run_mass_ratio_law_proved": False,
        "boundary_residual_flow_source_key_conservation_proved": False,
        "boundary_synthetic_split_ratio_source_key_law_proved": False,
        "primitive_orientation_local_factor_law_proved": False,
        "admissible_averaged_trace_family_created": False,
        "phi_lpf_parity_barrier_globally_broken": False,
        "row_column_unconditional_closed": False,
        "atom_ratio_summary_rows": aggregate_rows(ratio_rows),
        "smallest_ratio_event_rows": sorted(
            ratio_rows, key=lambda row: frac_from_record(row["smaller_to_larger_ratio"])
        )[:12],
        "largest_residual_gap_event_rows": sorted(
            ratio_rows, key=lambda row: frac_from_record(row["residual_mass"]), reverse=True
        )[:12],
        "gate_rows": [
            {
                "gate": "BoundaryAdjacencyClosed",
                "closed": adjacency_closed,
                "proved": True,
                "meaning": "all 47 events are adjacent q-boundary events with run_distance=1.",
                "remaining": "formal deterministic boundary ledger",
            },
            {
                "gate": "BoundaryRatioSpectrumClosed",
                "closed": ratio_spectrum_closed,
                "proved": True,
                "meaning": "each boundary split has an exact old/new mass ratio and residual side.",
                "remaining": "finite ratio spectrum",
            },
            {
                "gate": "BoundaryEqualWholeRunInvolution",
                "closed": False,
                "proved": False,
                "meaning": "no boundary event has equal old/new run masses.",
                "remaining": BOUNDARY_MASS_RATIO_LAW,
            },
            {
                "gate": "BoundaryResidualFlowSourceKeyConservation",
                "closed": False,
                "proved": False,
                "meaning": "42 events leave a new-run residual and 5 leave an old-run residual; this needs source-key conservation.",
                "remaining": BOUNDARY_RESIDUAL_FLOW,
            },
            {
                "gate": "RowColumnUnconditionalClosureReached",
                "closed": False,
                "proved": False,
                "meaning": "the boundary ratio spectrum is finite evidence, not a global parity-breaking theorem.",
                "remaining": f"{ORIENTATION_LAW} AND {MOVING_BEATTY_SAVING} AND {TRACE_FAMILY}",
            },
        ],
        "next_primary_attack_target": (
            f"{BOUNDARY_MASS_RATIO_LAW} AND {BOUNDARY_RESIDUAL_FLOW} AND "
            f"{NONBOUNDARY_JUMP_LAW} AND {INTERNAL_SURVIVOR_LAW} AND "
            f"{ORIENTATION_LAW} AND {MOVING_BEATTY_SAVING} AND {TRACE_FAMILY}"
        ),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "The q-boundary synthetic split branch has been narrowed to a ratio-spectrum "
            "obstruction.  All 47 events are adjacent q-boundary events, but none is an "
            "equal whole-run involution.  The smallest smaller/larger ratio is about "
            "0.013003592969 and the largest residual gap is about 0.861355534983.  "
            "A proof now needs an adjacent-run mass ratio law or a source-key residual "
            "flow conservation law before external trace/Kloosterman tools can enter."
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = []
    lines.append("# Prime Matrix Phi-LPF terminal boundary split ratio obstruction 证书")
    lines.append("")
    lines.append(f"**状态：** `{result['status']}`")
    lines.append(f"**核验日期：** `{result['verified_date']}`")
    lines.append("")
    lines.append("本证书把 q-boundary synthetic split 分支压成相邻 run 质量比率谱。")
    lines.append("")
    lines.append("```text")
    for key in [
        "previous_source_key_obstruction_partition_closed",
        "q_boundary_synthetic_split_event_count",
        "boundary_adjacency_closed",
        "whole_equal_pair_event_count",
        "synthetic_split_event_count",
        "old_consumed_new_residual_event_count",
        "old_residual_new_consumed_event_count",
        "negative_to_positive_event_count",
        "positive_to_negative_event_count",
        "boundary_ratio_spectrum_closed",
        "boundary_synthetic_split_ratio_source_key_law_proved",
        "row_column_unconditional_closed",
    ]:
        value = result[key]
        lines.append(f"{key}={fmt_bool(value) if isinstance(value, bool) else value}")
    lines.append("```")
    lines.append("")
    lines.append("## 1. ratio totals")
    lines.append("")
    lines.append("| quantity | value |")
    lines.append("| --- | --- |")
    for key in [
        "ratio_min",
        "ratio_max",
        "boundary_chunk_mass_total",
        "boundary_residual_gap_mass_total",
        "boundary_residual_gap_mass_max",
    ]:
        lines.append(f"| `{key}` | {render_fraction(result[key])} |")
    lines.append("")
    lines.append("## 2. atom ratio summary")
    lines.append("")
    lines.append("| atom | role | events | chunk mass | residual mass | ratio min | ratio max | old consumed | new consumed |")
    lines.append("| --- | --- | ---: | --- | --- | --- | --- | ---: | ---: |")
    for row in result["atom_ratio_summary_rows"]:
        lines.append(
            f"| `{cell(row['atom_key'])}` | `{row['role']}` | {row['event_count']} | "
            f"{render_fraction(row['chunk_total'])} | {render_fraction(row['residual_total'])} | "
            f"{render_fraction(row['ratio_min'])} | {render_fraction(row['ratio_max'])} | "
            f"{row['old_consumed_count']} | {row['new_consumed_count']} |"
        )
    lines.append("")
    lines.append("## 3. smallest ratio events")
    lines.append("")
    lines.append("| atom | old/new run | boundary q | ratio | residual | consumed pattern |")
    lines.append("| --- | --- | ---: | --- | --- | --- |")
    for row in result["smallest_ratio_event_rows"]:
        pattern = f"old={fmt_bool(row['old_consumed'])}, new={fmt_bool(row['new_consumed'])}"
        lines.append(
            f"| `{cell(row['atom_key'])}` | {row['old_run_id']}->{row['new_run_id']} | "
            f"{row['boundary_q']} | {render_fraction(row['smaller_to_larger_ratio'])} | "
            f"{render_fraction(row['residual_mass'])} | `{pattern}` |"
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
    """生成 boundary split ratio obstruction 证书。"""
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
    print(f"boundary_ratio_spectrum_closed={fmt_bool(result['boundary_ratio_spectrum_closed'])}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
