#!/usr/bin/env python3
"""审计 terminal adjacent-run Jordan cancellation 与源保持障碍。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_terminal_adjacent_run_jordan_cancellation_source_obstruction_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-terminal-adjacent-run-jordan-cancellation-source-obstruction-router.json

输出：
  data/prime-matrix-phi-lpf-terminal-adjacent-run-jordan-cancellation-source-obstruction-ledger.json
  docs/monograph/prime-matrix-phi-lpf-terminal-adjacent-run-jordan-cancellation-source-obstruction-router.json
  docs/monograph/prime-matrix-phi-lpf-terminal-adjacent-run-jordan-cancellation-source-obstruction-router.md

本证书把“统一相邻抵消律”拆成两个层级：
1. 形式层：对每条一维相位路径 A(q)/q，run 间抵消就是 Jordan/telescoping 恒等式；
2. actual-load 层：要把该恒等式用于素数/LPF 证明，必须构造源保持 signed pairing、
   orientation local-factor law，或可求和 trace/Kloosterman/Type-II family。
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

SLUG = "prime-matrix-phi-lpf-terminal-adjacent-run-jordan-cancellation-source-obstruction"
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
RUN_COMPRESSION = DOCS / "prime-matrix-phi-lpf-terminal-monotone-run-total-to-net-compression-frontier-router.json"

SOURCE_PAIRING = "SourcePreservingAdjacentRunPairingOrInternalSurvivorPDEC"
ORIENTATION_LAW = "PrimitiveOrientationLocalFactorProductLawBeforePushforward"
MOVING_BEATTY_SAVING = "SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving"
TRACE_FAMILY = "AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily"


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


def frac(num: int, den: int) -> Fraction:
    """构造 Fraction。"""
    return Fraction(int(num), int(den))


def frac_from_record(record: dict[str, Any]) -> Fraction:
    """从证书分数记录读取 Fraction。"""
    return frac(record["numerator"], record["denominator"])


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


def source_hashes() -> dict[str, str]:
    """登记本层依赖哈希。"""
    paths = [Path(__file__).resolve(), VARIATION, TURN_WORD, RUN_COMPRESSION]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def atom_key(atom: dict[str, Any]) -> str:
    """统一 atom key。"""
    return f"{atom['packet_side']}:{atom['packet_index']}:{atom['role']}:m{atom['m']}"


def delta(trans: dict[str, Any]) -> Fraction:
    """读取 transition signed phase delta。"""
    return frac(trans["phase_delta_num"], trans["phase_delta_den"])


def sign_of(value: Fraction) -> int:
    """返回分数符号。"""
    return 1 if value > 0 else -1 if value < 0 else 0


def group_runs(transitions: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """按 phase_direction 分组，重建 maximal monotone runs。"""
    if not transitions:
        return []
    groups: list[dict[str, Any]] = []
    start = 0
    current = transitions[0]["phase_direction"]
    for index, item in enumerate(transitions[1:], start=1):
        if item["phase_direction"] != current:
            groups.append({"direction": current, "start": start, "end": index - 1})
            start = index
            current = item["phase_direction"]
    groups.append({"direction": current, "start": start, "end": len(transitions) - 1})
    return groups


def variation_atom_map(variation_payload: dict[str, Any]) -> dict[str, dict[str, Any]]:
    """索引 variation atom profile。"""
    return {atom_key(atom): atom for atom in variation_payload["finite_audit"]["atom_variation_profiles"]}


def run_compression_atom_map(run_payload: dict[str, Any]) -> dict[str, dict[str, Any]]:
    """索引上一层 atom cancellation row。"""
    return {item["atom_key"]: item for item in run_payload["atom_cancellation_rows"]}


def audit_atom_rows(
    variation_payload: dict[str, Any],
    turn_payload: dict[str, Any],
    run_payload: dict[str, Any],
) -> list[dict[str, Any]]:
    """逐 atom 审计 Jordan/telescoping 与 maximal-run 一致性。"""
    variation_atoms = variation_atom_map(variation_payload)
    run_atoms = run_compression_atom_map(run_payload)
    rows: list[dict[str, Any]] = []
    for atom in turn_payload["finite_audit"]["atom_phase_turn_profiles"]:
        key = atom_key(atom)
        transitions = atom["phase_turn_transitions"]
        rebuilt = group_runs(transitions)
        variation_runs = variation_atoms[key]["run_variation_rows"]
        signed_sum = sum((delta(item) for item in transitions), Fraction(0))
        endpoint_delta = frac(transitions[-1]["A_next"], transitions[-1]["q_next"]) - frac(
            transitions[0]["A"], transitions[0]["q"]
        )
        total_variation = sum((abs(delta(item)) for item in transitions), Fraction(0))
        positive = sum((delta(item) for item in transitions if delta(item) > 0), Fraction(0))
        negative = -sum((delta(item) for item in transitions if delta(item) < 0), Fraction(0))
        survivor = frac_from_record(run_atoms[key]["survivor_mass"])
        cancelled_removed = frac_from_record(run_atoms[key]["cancelled_variation_removed"])
        sign_matches = all(
            (item["phase_direction"] == "negative" and item["A_wrap"])
            or (item["phase_direction"] == "positive" and not item["A_wrap"])
            for item in transitions
        )
        run_match = len(rebuilt) == len(variation_runs) and all(
            group["direction"] == run["direction"]
            and group["start"] == run["start_transition_index"]
            and group["end"] == run["end_transition_index"]
            for group, run in zip(rebuilt, variation_runs)
        )
        boundary_match = all(
            left["q_end"] == right["q_start"]
            for left, right in zip(variation_runs, variation_runs[1:])
        )
        rows.append(
            {
                "atom_key": key,
                "role": atom["role"],
                "P": atom["P"],
                "m": atom["m"],
                "transition_count": len(transitions),
                "run_count": len(variation_runs),
                "sign_matches_Awrap": sign_matches,
                "maximal_runs_rebuilt": run_match,
                "adjacent_run_boundaries_match": boundary_match,
                "signed_telescoping_identity_verified": signed_sum == endpoint_delta,
                "jordan_identity_verified": total_variation - cancelled_removed == survivor,
                "positive_variation": frac_record(positive),
                "negative_variation": frac_record(negative),
                "signed_net": frac_record(signed_sum),
                "total_variation": frac_record(total_variation),
                "cancelled_variation_removed": run_atoms[key]["cancelled_variation_removed"],
                "survivor_mass": run_atoms[key]["survivor_mass"],
                "survivor_direction": run_atoms[key]["survivor_direction"],
                "survivor_fragment_count": run_atoms[key]["survivor_fragment_count"],
            }
        )
    return rows


def run_rows_by_atom(variation_payload: dict[str, Any]) -> dict[str, list[dict[str, Any]]]:
    """取每个 atom 的 run rows。"""
    return {
        atom_key(atom): atom["run_variation_rows"]
        for atom in variation_payload["finite_audit"]["atom_variation_profiles"]
    }


def cancellation_events_for_atom(key: str, runs: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """生成栈式相邻抵消事件和最终 survivor fragments。"""
    stack: list[dict[str, Any]] = []
    events: list[dict[str, Any]] = []
    for run in sorted(runs, key=lambda item: int(item["run_id"])):
        signed = frac_from_record(run["signed_delta"])
        sign = sign_of(signed)
        mass = abs(signed)
        if sign == 0:
            continue
        source = {
            "atom_key": key,
            "sign": sign,
            "mass": mass,
            "original_mass": mass,
            "run_id": run["run_id"],
            "direction": run["direction"],
            "q_start": run["q_start"],
            "q_end": run["q_end"],
        }
        while mass and stack and stack[-1]["sign"] != sign:
            top = stack[-1]
            old_before = top["mass"]
            new_before = mass
            chunk = min(old_before, new_before)
            top["mass"] -= chunk
            mass -= chunk
            events.append(
                {
                    "atom_key": key,
                    "left_run_id": top["run_id"],
                    "right_run_id": run["run_id"],
                    "left_direction": top["direction"],
                    "right_direction": run["direction"],
                    "left_q_interval": f"[{top['q_start']},{top['q_end']}]",
                    "right_q_interval": f"[{run['q_start']},{run['q_end']}]",
                    "chunk": frac_record(chunk),
                    "old_before": frac_record(old_before),
                    "new_before": frac_record(new_before),
                    "old_consumed": old_before == chunk,
                    "new_consumed": new_before == chunk,
                    "complete_whole_run_pair": old_before == chunk and new_before == chunk,
                    "synthetic_split_required": not (old_before == chunk and new_before == chunk),
                }
            )
            if top["mass"] == 0:
                stack.pop()
        if mass:
            source["mass"] = mass
            stack.append(source)
    fragments = [
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
    return events, fragments


def cancellation_event_rows(variation_payload: dict[str, Any]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """汇总全部抵消事件与 survivor fragments。"""
    events: list[dict[str, Any]] = []
    fragments: list[dict[str, Any]] = []
    for key, runs in run_rows_by_atom(variation_payload).items():
        atom_events, atom_fragments = cancellation_events_for_atom(key, runs)
        events.extend(atom_events)
        fragments.extend(atom_fragments)
    return events, fragments


def internal_survivor_rows(
    variation_payload: dict[str, Any],
    fragments: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """找出不在最后 run 上的 survivor fragment。"""
    last_run = {
        key: max(int(run["run_id"]) for run in runs)
        for key, runs in run_rows_by_atom(variation_payload).items()
    }
    return [
        item
        for item in fragments
        if int(item["run_id"]) != last_run[item["atom_key"]]
    ]


def gate_row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造门控记录。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def external_frontier_note() -> list[dict[str, str]]:
    """外部前沿输入与当前源保持缺口。"""
    return [
        {
            "input": "Fouvry-Kowalski-Michel-Sawin, Bilinear forms with trace functions",
            "source": "https://arxiv.org/abs/2511.09459",
            "current_use": "only after adjacent-run chunks become a trace-function bilinear family",
        },
        {
            "input": "Milićević-Qin-Wu, Bilinear forms with Kloosterman sums",
            "source": "https://arxiv.org/abs/2511.07550",
            "current_use": "only after moving Beatty phases are completed to a bilinear Kloosterman family",
        },
        {
            "input": "Pascadi, On the exponents of distribution of primes and smooth numbers",
            "source": "https://arxiv.org/abs/2505.00653",
            "current_use": "only after the pointwise row/column load is turned into well-factorable AP averages",
        },
        {
            "input": "Wright, Trilinear Kloosterman fractions I",
            "source": "https://arxiv.org/abs/2604.25177",
            "current_use": "only after terminal payload becomes a trilinear convolution with equidistributed beta sequence",
        },
    ]


def build_certificate() -> dict[str, Any]:
    """组装证书。"""
    variation_payload = load_json(VARIATION)
    turn_payload = load_json(TURN_WORD)
    run_payload = load_json(RUN_COMPRESSION)
    atom_rows = audit_atom_rows(variation_payload, turn_payload, run_payload)
    events, fragments = cancellation_event_rows(variation_payload)
    internal_fragments = internal_survivor_rows(variation_payload, fragments)
    synthetic_events = [item for item in events if item["synthetic_split_required"]]
    complete_pairs = [item for item in events if item["complete_whole_run_pair"]]
    all_formal_closed = all(
        item["sign_matches_Awrap"]
        and item["maximal_runs_rebuilt"]
        and item["adjacent_run_boundaries_match"]
        and item["signed_telescoping_identity_verified"]
        and item["jordan_identity_verified"]
        for item in atom_rows
    )
    return {
        "certificate_type": "prime_matrix_phi_lpf_terminal_adjacent_run_jordan_cancellation_source_obstruction_router",
        "status": "formal_jordan_cancellation_closed_source_preserving_pairing_open",
        "verified_date": "2026-05-25",
        "terminal_phase_path_count": len(atom_rows),
        "terminal_transition_count_total": sum(item["transition_count"] for item in atom_rows),
        "terminal_run_count_total": sum(item["run_count"] for item in atom_rows),
        "sign_matches_Awrap_all_transitions": all(item["sign_matches_Awrap"] for item in atom_rows),
        "maximal_run_reconstruction_closed": all(item["maximal_runs_rebuilt"] for item in atom_rows),
        "signed_telescoping_identity_closed": all(item["signed_telescoping_identity_verified"] for item in atom_rows),
        "formal_jordan_cancellation_law_closed": all_formal_closed,
        "cancellation_event_count": len(events),
        "complete_whole_run_pair_event_count": len(complete_pairs),
        "synthetic_split_cancellation_event_count": len(synthetic_events),
        "survivor_fragment_count_total": len(fragments),
        "internal_survivor_fragment_count": len(internal_fragments),
        "tail_only_survivor_law_proved": len(internal_fragments) == 0,
        "source_preserving_adjacent_run_pairing_constructed": False,
        "primitive_orientation_local_factor_law_proved": False,
        "admissible_averaged_trace_family_created": False,
        "phi_lpf_parity_barrier_globally_broken": False,
        "row_column_unconditional_closed": False,
        "atom_law_rows": atom_rows,
        "synthetic_split_event_sample": synthetic_events[:12],
        "internal_survivor_rows": internal_fragments,
        "gate_rows": [
            gate_row(
                "AwrapSignLawClosed",
                True,
                True,
                "所有 transition 的符号由 A(q)/q 是否 wrap 精确决定。",
                "formal phase-path sign law",
            ),
            gate_row(
                "SignedTelescopingClosed",
                True,
                True,
                "每个 atom 的 signed_delta 总和等于末端相位减初端相位。",
                "one-dimensional phase telescoping",
            ),
            gate_row(
                "FormalJordanCancellationClosed",
                all_formal_closed,
                True,
                "total variation 被分解为 cancelled chunks 与 survivor，这是形式 Jordan 恒等式。",
                "formal cancellation law only",
            ),
            gate_row(
                "WholeRunInvolutionClosesCancellation",
                len(synthetic_events) == 0,
                False,
                "抵消事件需要切分 run 质量，不是完整 run 对完整 run 的自然 involution。",
                SOURCE_PAIRING,
            ),
            gate_row(
                "TailOnlySurvivorLaw",
                len(internal_fragments) == 0,
                False,
                "存在内部 survivor fragment，不能只用右端尾段 survivor 律闭合。",
                "InternalSurvivorPDECOrSourcePreservingPairing",
            ),
            gate_row(
                "SourcePreservingPairingConstructed",
                False,
                False,
                "尚未把形式抵消块绑定到 pre-Cauchy source/orientation/local-factor 键。",
                f"{SOURCE_PAIRING} AND {ORIENTATION_LAW}",
            ),
            gate_row(
                "RowColumnUnconditionalClosureReached",
                False,
                False,
                "本步找到统一形式抵消律，但未生成 actual signed payload 定理。",
                f"{SOURCE_PAIRING} AND {MOVING_BEATTY_SAVING} AND {TRACE_FAMILY}",
            ),
        ],
        "external_frontier_note": external_frontier_note(),
        "source_hashes": source_hashes(),
        "next_primary_attack_target": (
            f"{SOURCE_PAIRING} AND {ORIENTATION_LAW} AND "
            f"{MOVING_BEATTY_SAVING} AND {TRACE_FAMILY}"
        ),
        "plain_conclusion": (
            "A uniform formal adjacent-run cancellation law is now isolated: it is exactly the "
            "Jordan/telescoping identity for the one-dimensional phase path A(q)/q, with signs "
            "determined by A-wrap.  This does not yet close the Phi-LPF parity barrier.  The "
            "finite cancellation uses synthetic split chunks and even has an internal survivor "
            "fragment, so the actual proof still needs a source-preserving adjacent-run pairing, "
            "an orientation local-factor law, an admissible averaged trace/Kloosterman/Type-II "
            "family, or a named internal-survivor PDEC return."
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = []
    lines.append("# Prime Matrix Phi-LPF terminal adjacent-run Jordan cancellation source obstruction 证书")
    lines.append("")
    lines.append(f"**状态：** `{result['status']}`")
    lines.append(f"**核验日期：** `{result['verified_date']}`")
    lines.append("")
    lines.append("本证书寻找统一相邻抵消律。结论是：形式律已找到，它就是相位路径")
    lines.append("`A(q)/q` 的 signed telescoping/Jordan 分解；actual 证明仍缺源保持 pairing。")
    lines.append("")
    lines.append("```text")
    for key in [
        "terminal_phase_path_count",
        "terminal_transition_count_total",
        "terminal_run_count_total",
        "sign_matches_Awrap_all_transitions",
        "maximal_run_reconstruction_closed",
        "signed_telescoping_identity_closed",
        "formal_jordan_cancellation_law_closed",
        "cancellation_event_count",
        "complete_whole_run_pair_event_count",
        "synthetic_split_cancellation_event_count",
        "survivor_fragment_count_total",
        "internal_survivor_fragment_count",
        "tail_only_survivor_law_proved",
        "source_preserving_adjacent_run_pairing_constructed",
        "row_column_unconditional_closed",
    ]:
        value = result[key]
        lines.append(f"{key}={fmt_bool(value) if isinstance(value, bool) else value}")
    lines.append("```")
    lines.append("")
    lines.append("## 1. atom 形式律")
    lines.append("")
    lines.append("| atom | role | P | m | transitions | runs | sign=Awrap | telescope | Jordan | survivor |")
    lines.append("| --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- |")
    for item in result["atom_law_rows"]:
        lines.append(
            f"| `{cell(item['atom_key'])}` | `{item['role']}` | {item['P']} | {item['m']} | "
            f"{item['transition_count']} | {item['run_count']} | `{fmt_bool(item['sign_matches_Awrap'])}` | "
            f"`{fmt_bool(item['signed_telescoping_identity_verified'])}` | "
            f"`{fmt_bool(item['jordan_identity_verified'])}` | "
            f"{render_fraction(item['survivor_mass'])} `{item['survivor_direction']}` |"
        )
    lines.append("")
    lines.append("## 2. 源保持障碍")
    lines.append("")
    lines.append("抵消不是完整 run 对完整 run 的自然 involution，而需要切分质量块。样本：")
    lines.append("")
    lines.append("| atom | old run | new run | old dir | new dir | chunk | old consumed | new consumed |")
    lines.append("| --- | ---: | ---: | --- | --- | --- | --- | --- |")
    for item in result["synthetic_split_event_sample"]:
        lines.append(
            f"| `{cell(item['atom_key'])}` | {item['left_run_id']} | {item['right_run_id']} | "
            f"`{item['left_direction']}` | `{item['right_direction']}` | "
            f"{render_fraction(item['chunk'])} | `{fmt_bool(item['old_consumed'])}` | "
            f"`{fmt_bool(item['new_consumed'])}` |"
        )
    lines.append("")
    lines.append("内部 survivor fragment：")
    lines.append("")
    lines.append("| atom | run | dir | q interval | mass |")
    lines.append("| --- | ---: | --- | --- | --- |")
    if result["internal_survivor_rows"]:
        for item in result["internal_survivor_rows"]:
            lines.append(
                f"| `{cell(item['atom_key'])}` | {item['run_id']} | `{item['direction']}` | "
                f"`[{item['q_start']},{item['q_end']}]` | {render_fraction(item['mass'])} |"
            )
    else:
        lines.append("| none |  |  |  |  |")
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
    lines.append("| input | source | current use |")
    lines.append("| --- | --- | --- |")
    for item in result["external_frontier_note"]:
        lines.append(f"| {cell(item['input'])} | {item['source']} | {cell(item['current_use'])} |")
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
    print(f"formal_jordan_cancellation_law_closed={fmt_bool(result['formal_jordan_cancellation_law_closed'])}")
    print(
        "source_preserving_adjacent_run_pairing_constructed="
        f"{fmt_bool(result['source_preserving_adjacent_run_pairing_constructed'])}"
    )
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
