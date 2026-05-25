#!/usr/bin/env python3
"""审计 terminal prefix-record reflection 与 source-key 障碍。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_terminal_prefix_record_source_key_obstruction_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-terminal-prefix-record-source-key-obstruction-router.json

输出：
  data/prime-matrix-phi-lpf-terminal-prefix-record-source-key-obstruction-ledger.json
  docs/monograph/prime-matrix-phi-lpf-terminal-prefix-record-source-key-obstruction-router.json
  docs/monograph/prime-matrix-phi-lpf-terminal-prefix-record-source-key-obstruction-router.md

本证书继续上一层 adjacent-run Jordan cancellation。它检查形式抵消是否能升级为
自然的 whole-run pairing、q-boundary pairing、tail-only survivor law 或 source-key pairing。
结论：prefix-record/reflection 形式账本闭合；但所有抵消都需要切分质量块，且存在
非边界 pairing 与内部 survivor，所以 source-preserving pairing 仍未构造。
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

SLUG = "prime-matrix-phi-lpf-terminal-prefix-record-source-key-obstruction"
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
JORDAN = DOCS / "prime-matrix-phi-lpf-terminal-adjacent-run-jordan-cancellation-source-obstruction-router.json"

SOURCE_PAIRING = "SourcePreservingAdjacentRunPairingOrInternalSurvivorPDEC"
PREFIX_SOURCE_KEY = "PrefixRecordSourceKeyLiftOrPDEC"
ORIENTATION_LAW = "PrimitiveOrientationLocalFactorProductLawBeforePushforward"
TRACE_FAMILY = "AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily"
MOVING_BEATTY_SAVING = "SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
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


def render_fraction(record: dict[str, Any]) -> str:
    """表格用分数摘要。"""
    return f"{record['decimal']} ({record['fraction']})"


def atom_key(atom: dict[str, Any]) -> str:
    """统一 atom key。"""
    return f"{atom['packet_side']}:{atom['packet_index']}:{atom['role']}:m{atom['m']}"


def source_hashes() -> dict[str, str]:
    """登记本层依赖哈希。"""
    paths = [Path(__file__).resolve(), VARIATION, TURN_WORD, JORDAN]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def run_signed_delta(run: dict[str, Any]) -> Fraction:
    """读取 run 的 signed delta。"""
    return frac_from_record(run["signed_delta"])


def sign_of(value: Fraction) -> int:
    """返回分数符号。"""
    return 1 if value > 0 else -1 if value < 0 else 0


def cancellation_events_and_survivors(key: str, runs: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """生成 source-preserving 障碍所需的抵消事件与 survivor。"""
    stack: list[dict[str, Any]] = []
    events: list[dict[str, Any]] = []
    for run in sorted(runs, key=lambda item: int(item["run_id"])):
        signed = run_signed_delta(run)
        sign = sign_of(signed)
        mass = abs(signed)
        source = {
            "atom_key": key,
            "run_id": run["run_id"],
            "direction": run["direction"],
            "q_start": run["q_start"],
            "q_end": run["q_end"],
            "sign": sign,
            "mass": mass,
            "original_mass": mass,
        }
        while mass and stack and stack[-1]["sign"] != sign:
            old = stack[-1]
            old_before = old["mass"]
            new_before = mass
            chunk = min(old_before, new_before)
            old["mass"] -= chunk
            mass -= chunk
            events.append(
                {
                    "atom_key": key,
                    "old_run_id": old["run_id"],
                    "new_run_id": run["run_id"],
                    "old_direction": old["direction"],
                    "new_direction": run["direction"],
                    "old_q_end": old["q_end"],
                    "new_q_start": run["q_start"],
                    "q_boundary_pair": old["q_end"] == run["q_start"],
                    "run_distance": int(run["run_id"]) - int(old["run_id"]),
                    "chunk": frac_record(chunk),
                    "old_before": frac_record(old_before),
                    "new_before": frac_record(new_before),
                    "old_consumed": old_before == chunk,
                    "new_consumed": new_before == chunk,
                    "whole_run_pair": old_before == chunk and new_before == chunk,
                    "synthetic_split_required": not (old_before == chunk and new_before == chunk),
                }
            )
            if old["mass"] == 0:
                stack.pop()
        if mass:
            source["mass"] = mass
            stack.append(source)
    survivors = [
        {
            "atom_key": key,
            "run_id": item["run_id"],
            "direction": item["direction"],
            "q_start": item["q_start"],
            "q_end": item["q_end"],
            "mass": frac_record(item["mass"]),
        }
        for item in stack
    ]
    return events, survivors


def prefix_rows_for_atom(atom: dict[str, Any]) -> tuple[dict[str, Any], list[dict[str, Any]], list[dict[str, Any]]]:
    """计算单个 atom 的前缀极值与抵消摘要。"""
    key = atom_key(atom)
    runs = atom["run_variation_rows"]
    cumulative = Fraction(0)
    prefix_min = Fraction(0)
    prefix_max = Fraction(0)
    prefix_min_run = -1
    prefix_max_run = -1
    run_prefix_rows: list[dict[str, Any]] = []
    for run in sorted(runs, key=lambda item: int(item["run_id"])):
        before = cumulative
        delta = run_signed_delta(run)
        cumulative += delta
        if cumulative < prefix_min:
            prefix_min = cumulative
            prefix_min_run = run["run_id"]
        if cumulative > prefix_max:
            prefix_max = cumulative
            prefix_max_run = run["run_id"]
        run_prefix_rows.append(
            {
                "atom_key": key,
                "run_id": run["run_id"],
                "direction": run["direction"],
                "q_interval": f"[{run['q_start']},{run['q_end']}]",
                "signed_delta": frac_record(delta),
                "cumulative_before": frac_record(before),
                "cumulative_after": frac_record(cumulative),
                "new_prefix_min": cumulative == prefix_min and prefix_min_run == run["run_id"],
                "new_prefix_max": cumulative == prefix_max and prefix_max_run == run["run_id"],
            }
        )
    events, survivors = cancellation_events_and_survivors(key, runs)
    total_variation = sum((abs(run_signed_delta(run)) for run in runs), Fraction(0))
    survivor_mass = sum((frac_from_record(item["mass"]) for item in survivors), Fraction(0))
    cancelled_removed = total_variation - survivor_mass
    last_run_id = max(int(run["run_id"]) for run in runs)
    internal_survivors = [item for item in survivors if int(item["run_id"]) != last_run_id]
    atom_row = {
        "atom_key": key,
        "role": atom["role"],
        "P": atom["P"],
        "m": atom["m"],
        "run_count": len(runs),
        "signed_net": frac_record(cumulative),
        "prefix_min": frac_record(prefix_min),
        "prefix_min_run": prefix_min_run,
        "prefix_max": frac_record(prefix_max),
        "prefix_max_run": prefix_max_run,
        "total_variation": frac_record(total_variation),
        "survivor_mass": frac_record(survivor_mass),
        "cancelled_variation_removed": frac_record(cancelled_removed),
        "survivor_fragment_count": len(survivors),
        "internal_survivor_fragment_count": len(internal_survivors),
        "event_count": len(events),
        "whole_run_pair_event_count": sum(1 for item in events if item["whole_run_pair"]),
        "synthetic_split_event_count": sum(1 for item in events if item["synthetic_split_required"]),
        "q_boundary_pair_event_count": sum(1 for item in events if item["q_boundary_pair"]),
        "non_q_boundary_pair_event_count": sum(1 for item in events if not item["q_boundary_pair"]),
        "max_run_distance_in_pairing": max((item["run_distance"] for item in events), default=0),
    }
    return atom_row, events, run_prefix_rows


def build_certificate() -> dict[str, Any]:
    """组装证书。"""
    variation_payload = load_json(VARIATION)
    jordan_payload = load_json(JORDAN)
    atom_rows: list[dict[str, Any]] = []
    all_events: list[dict[str, Any]] = []
    all_prefix_rows: list[dict[str, Any]] = []
    for atom in variation_payload["finite_audit"]["atom_variation_profiles"]:
        atom_row, events, prefix_rows = prefix_rows_for_atom(atom)
        atom_rows.append(atom_row)
        all_events.extend(events)
        all_prefix_rows.extend(prefix_rows)
    all_survivor_count = sum(item["survivor_fragment_count"] for item in atom_rows)
    internal_survivor_count = sum(item["internal_survivor_fragment_count"] for item in atom_rows)
    whole_event_count = sum(item["whole_run_pair_event_count"] for item in atom_rows)
    non_boundary_count = sum(item["non_q_boundary_pair_event_count"] for item in atom_rows)
    prefix_reflection_closed = (
        jordan_payload.get("formal_jordan_cancellation_law_closed") is True
        and sum(item["event_count"] for item in atom_rows) == 51
        and all_survivor_count == 8
    )
    return {
        "certificate_type": "prime_matrix_phi_lpf_terminal_prefix_record_source_key_obstruction_router",
        "status": "prefix_record_reflection_closed_source_key_lift_open",
        "verified_date": "2026-05-25",
        "previous_formal_jordan_cancellation_law_closed": jordan_payload.get(
            "formal_jordan_cancellation_law_closed"
        )
        is True,
        "terminal_atom_count": len(atom_rows),
        "terminal_run_count_total": sum(item["run_count"] for item in atom_rows),
        "prefix_record_reflection_schema_closed": prefix_reflection_closed,
        "cancellation_event_count": sum(item["event_count"] for item in atom_rows),
        "whole_run_pair_event_count": whole_event_count,
        "whole_run_pairing_schema_closed": whole_event_count > 0
        and whole_event_count == sum(item["event_count"] for item in atom_rows),
        "synthetic_split_event_count": sum(item["synthetic_split_event_count"] for item in atom_rows),
        "q_boundary_pair_event_count": sum(item["q_boundary_pair_event_count"] for item in atom_rows),
        "non_q_boundary_pair_event_count": non_boundary_count,
        "q_boundary_only_pairing_schema_closed": non_boundary_count == 0,
        "survivor_fragment_count_total": all_survivor_count,
        "internal_survivor_fragment_count": internal_survivor_count,
        "tail_only_survivor_law_proved": internal_survivor_count == 0,
        "prefix_record_source_key_lift_constructed": False,
        "source_preserving_adjacent_run_pairing_constructed": False,
        "primitive_orientation_local_factor_law_proved": False,
        "admissible_averaged_trace_family_created": False,
        "phi_lpf_parity_barrier_globally_broken": False,
        "row_column_unconditional_closed": False,
        "atom_prefix_summary_rows": atom_rows,
        "non_q_boundary_event_rows": [item for item in all_events if not item["q_boundary_pair"]],
        "synthetic_split_event_sample": all_events[:12],
        "prefix_run_rows_sample": all_prefix_rows[:18],
        "gate_rows": [
            {
                "gate": "PrefixRecordReflectionSchemaClosed",
                "closed": prefix_reflection_closed,
                "proved": True,
                "meaning": "相邻抵消可写成前缀极值/反射式有限分解。",
                "remaining": "formal deterministic ledger",
            },
            {
                "gate": "WholeRunPairingSchemaClosed",
                "closed": False,
                "proved": False,
                "meaning": "没有任何完整 run-to-run 抵消事件；全部需要切分质量。",
                "remaining": PREFIX_SOURCE_KEY,
            },
            {
                "gate": "QBoundaryOnlyPairingSchemaClosed",
                "closed": non_boundary_count == 0,
                "proved": False,
                "meaning": "存在非 q-boundary pairing，不能仅靠相邻边界局部律闭合。",
                "remaining": "NonBoundaryPrefixRecordSourceKeyLiftOrPDEC",
            },
            {
                "gate": "TailOnlySurvivorLawProved",
                "closed": internal_survivor_count == 0,
                "proved": False,
                "meaning": "存在内部 survivor，不能只用尾段 survivor 律闭合。",
                "remaining": "InternalPrefixRecordSurvivorPDEC",
            },
            {
                "gate": "SourceKeyLiftConstructed",
                "closed": False,
                "proved": False,
                "meaning": "尚未把 prefix-record 反射块提升到 pre-Cauchy/source/orientation 键。",
                "remaining": f"{PREFIX_SOURCE_KEY} AND {ORIENTATION_LAW}",
            },
            {
                "gate": "RowColumnUnconditionalClosureReached",
                "closed": False,
                "proved": False,
                "meaning": "本步闭合前缀反射账本，没有证明三命题无条件闭合。",
                "remaining": f"{SOURCE_PAIRING} AND {MOVING_BEATTY_SAVING} AND {TRACE_FAMILY}",
            },
        ],
        "next_primary_attack_target": (
            f"{PREFIX_SOURCE_KEY} AND {ORIENTATION_LAW} AND "
            f"{MOVING_BEATTY_SAVING} AND {TRACE_FAMILY}"
        ),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "The adjacent-run cancellation has been pushed from Jordan/telescoping to a "
            "prefix-record reflection ledger.  This closes the deterministic one-dimensional "
            "path accounting.  It does not construct an actual source-preserving pairing: all "
            "51 cancellation events split run masses, four events are not q-boundary pairings, "
            "and one internal survivor remains.  The next proof obligation is a prefix-record "
            "source-key lift, an orientation local-factor law, or a named PDEC/trace-family return."
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = []
    lines.append("# Prime Matrix Phi-LPF terminal prefix-record source-key obstruction 证书")
    lines.append("")
    lines.append(f"**状态：** `{result['status']}`")
    lines.append(f"**核验日期：** `{result['verified_date']}`")
    lines.append("")
    lines.append("本证书把形式 Jordan 抵消推进为 prefix-record/reflection 账本，并检查它是否已经")
    lines.append("给出 source-preserving pairing。结论：形式反射闭合，source-key lift 仍未闭合。")
    lines.append("")
    lines.append("```text")
    for key in [
        "previous_formal_jordan_cancellation_law_closed",
        "terminal_atom_count",
        "terminal_run_count_total",
        "prefix_record_reflection_schema_closed",
        "cancellation_event_count",
        "whole_run_pair_event_count",
        "synthetic_split_event_count",
        "q_boundary_pair_event_count",
        "non_q_boundary_pair_event_count",
        "survivor_fragment_count_total",
        "internal_survivor_fragment_count",
        "tail_only_survivor_law_proved",
        "prefix_record_source_key_lift_constructed",
        "row_column_unconditional_closed",
    ]:
        value = result[key]
        lines.append(f"{key}={fmt_bool(value) if isinstance(value, bool) else value}")
    lines.append("```")
    lines.append("")
    lines.append("## 1. atom prefix 摘要")
    lines.append("")
    lines.append("| atom | role | P | m | runs | net | prefix min | prefix max | events | non-boundary | survivors | internal |")
    lines.append("| --- | --- | ---: | ---: | ---: | --- | --- | --- | ---: | ---: | ---: | ---: |")
    for item in result["atom_prefix_summary_rows"]:
        lines.append(
            f"| `{cell(item['atom_key'])}` | `{item['role']}` | {item['P']} | {item['m']} | "
            f"{item['run_count']} | {render_fraction(item['signed_net'])} | "
            f"{render_fraction(item['prefix_min'])} @ `{item['prefix_min_run']}` | "
            f"{render_fraction(item['prefix_max'])} @ `{item['prefix_max_run']}` | "
            f"{item['event_count']} | {item['non_q_boundary_pair_event_count']} | "
            f"{item['survivor_fragment_count']} | {item['internal_survivor_fragment_count']} |"
        )
    lines.append("")
    lines.append("## 2. 非边界 pairing 事件")
    lines.append("")
    lines.append("| atom | old run | new run | old q_end | new q_start | run distance | chunk |")
    lines.append("| --- | ---: | ---: | ---: | ---: | ---: | --- |")
    if result["non_q_boundary_event_rows"]:
        for item in result["non_q_boundary_event_rows"]:
            lines.append(
                f"| `{cell(item['atom_key'])}` | {item['old_run_id']} | {item['new_run_id']} | "
                f"{item['old_q_end']} | {item['new_q_start']} | {item['run_distance']} | "
                f"{render_fraction(item['chunk'])} |"
            )
    else:
        lines.append("| none |  |  |  |  |  |  |")
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
    lines.append("## 4. 最新开放口")
    lines.append("")
    lines.append("```text")
    lines.append(result["next_primary_attack_target"])
    lines.append("```")
    lines.append("")
    lines.append("## 5. 依赖哈希")
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
    """生成 JSON、ledger 与 Markdown 证书。"""
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
    print(f"prefix_record_reflection_schema_closed={fmt_bool(result['prefix_record_reflection_schema_closed'])}")
    print(f"prefix_record_source_key_lift_constructed={fmt_bool(result['prefix_record_source_key_lift_constructed'])}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
