#!/usr/bin/env python3
"""审计 terminal source-key lift 障碍的三分 partition。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_terminal_source_key_obstruction_partition_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-terminal-source-key-obstruction-partition-router.json

输出：
  data/prime-matrix-phi-lpf-terminal-source-key-obstruction-partition-ledger.json
  docs/monograph/prime-matrix-phi-lpf-terminal-source-key-obstruction-partition-router.json
  docs/monograph/prime-matrix-phi-lpf-terminal-source-key-obstruction-partition-router.md

本证书继续 prefix-record/reflection 账本，把 source-key lift 的失败拆成三类：
q-boundary synthetic split、non-boundary record jump、internal survivor。
结论：三分 partition 闭合；但三类 actual source-key law 均未证明。
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

SLUG = "prime-matrix-phi-lpf-terminal-source-key-obstruction-partition"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREFIX_SCRIPT = EXPERIMENTS / "prime_matrix_phi_lpf_terminal_prefix_record_source_key_obstruction_router.py"
PREFIX_JSON = DOCS / "prime-matrix-phi-lpf-terminal-prefix-record-source-key-obstruction-router.json"
VARIATION_JSON = DOCS / (
    "prime-matrix-phi-lpf-dominant-sign-word-repeated-step-packet-enclosure-"
    "terminal-phase-variation-budget-audit.json"
)
MONOTONE_JSON = DOCS / "prime-matrix-phi-lpf-terminal-monotone-run-total-to-net-compression-frontier-router.json"

BOUNDARY_SPLIT_LAW = "BoundarySyntheticSplitRatioSourceKeyLawOrPDEC"
NONBOUNDARY_JUMP_LAW = "NonBoundaryPrefixRecordJumpSourceKeyLiftOrPDEC"
INTERNAL_SURVIVOR_LAW = "InternalPrefixRecordSurvivorPDEC"
ORIENTATION_LAW = "PrimitiveOrientationLocalFactorProductLawBeforePushforward"
MOVING_BEATTY_SAVING = "SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving"
TRACE_FAMILY = "AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def load_prefix_module() -> Any:
    """加载上一层 prefix-record 审计模块，复用其精确分数逻辑。"""
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
    paths = [Path(__file__).resolve(), PREFIX_SCRIPT, PREFIX_JSON, VARIATION_JSON, MONOTONE_JSON]
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


def event_mass(event: dict[str, Any]) -> Fraction:
    """读取 cancellation chunk mass。"""
    return frac_from_record(event["chunk"])


def collect_events_and_survivors() -> tuple[list[dict[str, Any]], list[dict[str, Any]], dict[str, Any]]:
    """复用上一层模块生成完整 event/survivor rows。"""
    prefix = load_prefix_module()
    variation = load_json(VARIATION_JSON)
    events: list[dict[str, Any]] = []
    survivors: list[dict[str, Any]] = []
    atom_last_run: dict[str, int] = {}
    for atom in variation["finite_audit"]["atom_variation_profiles"]:
        key = prefix.atom_key(atom)
        atom_last_run[key] = max(int(run["run_id"]) for run in atom["run_variation_rows"])
        atom_events, atom_survivors = prefix.cancellation_events_and_survivors(
            key, atom["run_variation_rows"]
        )
        events.extend(atom_events)
        survivors.extend(atom_survivors)
    return events, survivors, {"atom_last_run": atom_last_run}


def event_partition_rows(events: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """按 atom 和 event 类型汇总 cancellation events。"""
    buckets: dict[tuple[str, str], dict[str, Any]] = {}
    for event in events:
        kind = "q_boundary_synthetic_split" if event["q_boundary_pair"] else "nonboundary_record_jump"
        key = (event["atom_key"], kind)
        if key not in buckets:
            buckets[key] = {
                "atom_key": event["atom_key"],
                "partition": kind,
                "event_count": 0,
                "mass_total": Fraction(0),
                "max_run_distance": 0,
                "old_consumed_count": 0,
                "new_consumed_count": 0,
            }
        row = buckets[key]
        row["event_count"] += 1
        row["mass_total"] += event_mass(event)
        row["max_run_distance"] = max(row["max_run_distance"], int(event["run_distance"]))
        row["old_consumed_count"] += int(bool(event["old_consumed"]))
        row["new_consumed_count"] += int(bool(event["new_consumed"]))
    rendered = []
    for row in buckets.values():
        rendered.append(
            {
                "atom_key": row["atom_key"],
                "partition": row["partition"],
                "event_count": row["event_count"],
                "mass_total": frac_record(row["mass_total"]),
                "max_run_distance": row["max_run_distance"],
                "old_consumed_count": row["old_consumed_count"],
                "new_consumed_count": row["new_consumed_count"],
            }
        )
    return sorted(rendered, key=lambda item: (item["atom_key"], item["partition"]))


def survivor_partition_rows(
    survivors: list[dict[str, Any]], atom_last_run: dict[str, int]
) -> list[dict[str, Any]]:
    """给 survivor 标注 tail/internal 类型。"""
    rows = []
    for item in survivors:
        last_run = atom_last_run[item["atom_key"]]
        internal = int(item["run_id"]) != last_run
        rows.append(
            {
                "atom_key": item["atom_key"],
                "run_id": item["run_id"],
                "direction": item["direction"],
                "q_start": item["q_start"],
                "q_end": item["q_end"],
                "survivor_type": "internal_survivor" if internal else "tail_survivor",
                "mass": item["mass"],
            }
        )
    return sorted(rows, key=lambda item: (item["atom_key"], int(item["run_id"])))


def build_certificate() -> dict[str, Any]:
    """组装三分 partition 证书。"""
    prefix_payload = load_json(PREFIX_JSON)
    monotone_payload = load_json(MONOTONE_JSON)
    events, survivors, meta = collect_events_and_survivors()
    atom_last_run = meta["atom_last_run"]

    boundary_events = [event for event in events if event["q_boundary_pair"]]
    nonboundary_events = [event for event in events if not event["q_boundary_pair"]]
    synthetic_events = [event for event in events if event["synthetic_split_required"]]
    whole_events = [event for event in events if event["whole_run_pair"]]
    survivor_rows = survivor_partition_rows(survivors, atom_last_run)
    internal_survivors = [row for row in survivor_rows if row["survivor_type"] == "internal_survivor"]
    tail_survivors = [row for row in survivor_rows if row["survivor_type"] == "tail_survivor"]
    consumed_counter = Counter((event["old_consumed"], event["new_consumed"]) for event in events)

    boundary_mass = sum((event_mass(event) for event in boundary_events), Fraction(0))
    nonboundary_mass = sum((event_mass(event) for event in nonboundary_events), Fraction(0))
    internal_survivor_mass = sum((frac_from_record(row["mass"]) for row in internal_survivors), Fraction(0))
    nonboundary_plus_internal = nonboundary_mass + internal_survivor_mass
    finite_margin = frac_from_record(
        monotone_payload["absorption_metrics"]["selected_negative_excess_minus_extra_atom_survivor"]
    )
    finite_margin_after_obstruction = finite_margin - nonboundary_plus_internal

    nonboundary_atoms = sorted({event["atom_key"] for event in nonboundary_events})
    partition_closed = (
        prefix_payload.get("prefix_record_reflection_schema_closed") is True
        and len(events) == len(boundary_events) + len(nonboundary_events)
        and len(survivors) == len(tail_survivors) + len(internal_survivors)
        and len(events) == int(prefix_payload["cancellation_event_count"])
        and len(survivors) == int(prefix_payload["survivor_fragment_count_total"])
        and len(whole_events) == 0
        and len(synthetic_events) == len(events)
    )

    return {
        "certificate_type": "prime_matrix_phi_lpf_terminal_source_key_obstruction_partition_router",
        "status": "source_key_obstruction_partition_closed_three_actual_gates_open",
        "verified_date": "2026-05-25",
        "previous_prefix_record_reflection_schema_closed": prefix_payload.get(
            "prefix_record_reflection_schema_closed"
        )
        is True,
        "terminal_atom_count": prefix_payload["terminal_atom_count"],
        "terminal_run_count_total": prefix_payload["terminal_run_count_total"],
        "cancellation_event_count": len(events),
        "whole_run_pair_event_count": len(whole_events),
        "synthetic_split_event_count": len(synthetic_events),
        "q_boundary_synthetic_split_event_count": len(boundary_events),
        "nonboundary_record_jump_event_count": len(nonboundary_events),
        "nonboundary_record_jump_atom_count": len(nonboundary_atoms),
        "nonboundary_record_jump_atoms": nonboundary_atoms,
        "old_consumed_new_residual_event_count": consumed_counter[(True, False)],
        "old_residual_new_consumed_event_count": consumed_counter[(False, True)],
        "both_sides_whole_event_count": consumed_counter[(True, True)],
        "both_sides_residual_event_count": consumed_counter[(False, False)],
        "boundary_synthetic_split_mass_total": frac_record(boundary_mass),
        "nonboundary_record_jump_mass_total": frac_record(nonboundary_mass),
        "survivor_fragment_count_total": len(survivors),
        "tail_survivor_fragment_count": len(tail_survivors),
        "internal_survivor_fragment_count": len(internal_survivors),
        "internal_survivor_mass_total": frac_record(internal_survivor_mass),
        "nonboundary_plus_internal_obstruction_mass": frac_record(nonboundary_plus_internal),
        "finite_selected_margin_after_nonboundary_internal_payment": frac_record(
            finite_margin_after_obstruction
        ),
        "finite_margin_after_nonboundary_internal_payment_positive": finite_margin_after_obstruction > 0,
        "source_key_obstruction_partition_closed": partition_closed,
        "boundary_synthetic_split_ratio_source_key_law_proved": False,
        "nonboundary_record_jump_source_key_lift_constructed": False,
        "internal_survivor_pdec_constructed": False,
        "primitive_orientation_local_factor_law_proved": False,
        "admissible_averaged_trace_family_created": False,
        "phi_lpf_parity_barrier_globally_broken": False,
        "row_column_unconditional_closed": False,
        "event_partition_rows": event_partition_rows(events),
        "nonboundary_record_jump_rows": [
            {
                "atom_key": event["atom_key"],
                "old_run_id": event["old_run_id"],
                "new_run_id": event["new_run_id"],
                "old_q_end": event["old_q_end"],
                "new_q_start": event["new_q_start"],
                "run_distance": event["run_distance"],
                "chunk": event["chunk"],
                "old_consumed": event["old_consumed"],
                "new_consumed": event["new_consumed"],
            }
            for event in nonboundary_events
        ],
        "survivor_partition_rows": survivor_rows,
        "gate_rows": [
            {
                "gate": "SourceKeyObstructionPartitionClosed",
                "closed": partition_closed,
                "proved": True,
                "meaning": "prefix-record source-key failure is split into boundary splits, non-boundary jumps, and internal survivor.",
                "remaining": "formal deterministic partition",
            },
            {
                "gate": "BoundarySyntheticSplitRatioSourceKeyLaw",
                "closed": False,
                "proved": False,
                "meaning": "47 q-boundary cancellations still split masses and need a pre-pushforward source ratio law.",
                "remaining": BOUNDARY_SPLIT_LAW,
            },
            {
                "gate": "NonBoundaryPrefixRecordJumpSourceKeyLift",
                "closed": False,
                "proved": False,
                "meaning": "4 cancellations jump across q-boundaries and cannot be certified by adjacent q-locality.",
                "remaining": NONBOUNDARY_JUMP_LAW,
            },
            {
                "gate": "InternalPrefixRecordSurvivorPDEC",
                "closed": False,
                "proved": False,
                "meaning": "1 selected-terminal survivor is internal rather than tail-only.",
                "remaining": INTERNAL_SURVIVOR_LAW,
            },
            {
                "gate": "RowColumnUnconditionalClosureReached",
                "closed": False,
                "proved": False,
                "meaning": "the partition is finite evidence, not a global Phi-LPF parity-breaking theorem.",
                "remaining": f"{ORIENTATION_LAW} AND {MOVING_BEATTY_SAVING} AND {TRACE_FAMILY}",
            },
        ],
        "next_primary_attack_target": (
            f"{BOUNDARY_SPLIT_LAW} AND {NONBOUNDARY_JUMP_LAW} AND "
            f"{INTERNAL_SURVIVOR_LAW} AND {ORIENTATION_LAW} AND "
            f"{MOVING_BEATTY_SAVING} AND {TRACE_FAMILY}"
        ),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "The source-key obstruction has been partitioned into exactly 47 q-boundary "
            "synthetic splits, 4 non-boundary record jumps, and 1 internal survivor.  "
            "The finite scalar margin remains positive after the non-boundary plus internal "
            "mass is subtracted, but this is not a proof: the boundary split ratio law, "
            "non-boundary jump lift, internal survivor return, and orientation/local-factor "
            "law are still missing."
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = []
    lines.append("# Prime Matrix Phi-LPF terminal source-key obstruction partition 证书")
    lines.append("")
    lines.append(f"**状态：** `{result['status']}`")
    lines.append(f"**核验日期：** `{result['verified_date']}`")
    lines.append("")
    lines.append("本证书把 `PrefixRecordSourceKeyLiftOrPDEC` 拆成三类实际缺口：")
    lines.append("q-boundary synthetic split、non-boundary record jump、internal survivor。")
    lines.append("")
    lines.append("```text")
    for key in [
        "previous_prefix_record_reflection_schema_closed",
        "source_key_obstruction_partition_closed",
        "cancellation_event_count",
        "whole_run_pair_event_count",
        "synthetic_split_event_count",
        "q_boundary_synthetic_split_event_count",
        "nonboundary_record_jump_event_count",
        "nonboundary_record_jump_atom_count",
        "old_consumed_new_residual_event_count",
        "old_residual_new_consumed_event_count",
        "survivor_fragment_count_total",
        "tail_survivor_fragment_count",
        "internal_survivor_fragment_count",
        "finite_margin_after_nonboundary_internal_payment_positive",
        "row_column_unconditional_closed",
    ]:
        value = result[key]
        lines.append(f"{key}={fmt_bool(value) if isinstance(value, bool) else value}")
    lines.append("```")
    lines.append("")
    lines.append("## 1. event partition")
    lines.append("")
    lines.append("| atom | partition | events | mass | max distance | old consumed | new consumed |")
    lines.append("| --- | --- | ---: | --- | ---: | ---: | ---: |")
    for row in result["event_partition_rows"]:
        lines.append(
            f"| `{cell(row['atom_key'])}` | `{row['partition']}` | {row['event_count']} | "
            f"{render_fraction(row['mass_total'])} | {row['max_run_distance']} | "
            f"{row['old_consumed_count']} | {row['new_consumed_count']} |"
        )
    lines.append("")
    lines.append("## 2. non-boundary record jumps")
    lines.append("")
    lines.append("| atom | old run | new run | old q_end | new q_start | distance | chunk |")
    lines.append("| --- | ---: | ---: | ---: | ---: | ---: | --- |")
    for row in result["nonboundary_record_jump_rows"]:
        lines.append(
            f"| `{cell(row['atom_key'])}` | {row['old_run_id']} | {row['new_run_id']} | "
            f"{row['old_q_end']} | {row['new_q_start']} | {row['run_distance']} | "
            f"{render_fraction(row['chunk'])} |"
        )
    lines.append("")
    lines.append("## 3. survivor partition")
    lines.append("")
    lines.append("| atom | run | q interval | type | mass |")
    lines.append("| --- | ---: | --- | --- | --- |")
    for row in result["survivor_partition_rows"]:
        lines.append(
            f"| `{cell(row['atom_key'])}` | {row['run_id']} | [{row['q_start']},{row['q_end']}] | "
            f"`{row['survivor_type']}` | {render_fraction(row['mass'])} |"
        )
    lines.append("")
    lines.append("## 4. finite scalar check")
    lines.append("")
    lines.append("| quantity | value |")
    lines.append("| --- | --- |")
    lines.append(
        "| nonboundary plus internal obstruction mass | "
        f"{render_fraction(result['nonboundary_plus_internal_obstruction_mass'])} |"
    )
    lines.append(
        "| selected finite margin after that subtraction | "
        f"{render_fraction(result['finite_selected_margin_after_nonboundary_internal_payment'])} |"
    )
    lines.append("")
    lines.append("该标量余量不是证明；它只说明有限样本中非边界 jump 与内部 survivor 的质量本身")
    lines.append("不是最大的数值障碍。真正缺口仍是 source-key lift 与 orientation/local-factor law。")
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
    """生成三分 partition 证书。"""
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
    print(f"source_key_obstruction_partition_closed={fmt_bool(result['source_key_obstruction_partition_closed'])}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
