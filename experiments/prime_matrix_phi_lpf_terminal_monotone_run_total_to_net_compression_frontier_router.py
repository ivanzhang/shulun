#!/usr/bin/env python3
"""审计 terminal monotone-run total-to-net compression 前沿。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_terminal_monotone_run_total_to_net_compression_frontier_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-terminal-monotone-run-total-to-net-compression-frontier-router.json

输出：
  data/prime-matrix-phi-lpf-terminal-monotone-run-total-to-net-compression-frontier-ledger.json
  docs/monograph/prime-matrix-phi-lpf-terminal-monotone-run-total-to-net-compression-frontier-router.json
  docs/monograph/prime-matrix-phi-lpf-terminal-monotone-run-total-to-net-compression-frontier-router.md

本证书承接 terminal signed payload absorption frontier。核心检查是：
每个 monotone run 内部没有 total-to-net 压缩，压缩只来自相邻反向 run 的有符号抵消。
有限数据可以精确分解为 cancelled chunks + atom-local survivor；但把这种分解提升为全局
相位节省仍需要 uniform run-cancellation law、PDEC/SAE/LocalSurvivor 回流，或外部 trace/
Kloosterman/Type-II 可求和族。
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

SLUG = "prime-matrix-phi-lpf-terminal-monotone-run-total-to-net-compression-frontier"
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
SIGNED_PAYLOAD = DOCS / "prime-matrix-phi-lpf-terminal-signed-payload-measure-absorption-frontier-router.json"

TOTAL_TO_NET = "MonotoneRunTotalToNetCompressionOrPDEC"
EXTRA_ABSORB = "ExtraTotalVariationAbsorptionOrLocalSurvivor"
MOVING_BEATTY_SAVING = "SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving"
TRACE_FAMILY = "AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily"
RUN_CANCELLATION = "UniformAdjacentRunCancellationFamilyOrPDEC"
LOCAL_SURVIVOR = "AtomLocalSurvivorPaymentOrPDEC"


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


def render_fraction(record: dict[str, Any]) -> str:
    """表格用分数摘要。"""
    return f"{record['decimal']} ({record['fraction']})"


def source_hashes() -> dict[str, str]:
    """登记本层依赖哈希。"""
    paths = [Path(__file__).resolve(), VARIATION, TURN_WORD, SIGNED_PAYLOAD]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def atom_key(item: dict[str, Any]) -> tuple[str, int, str, int]:
    """统一 atom key。"""
    return (item["packet_side"], int(item["packet_index"]), item["role"], int(item["m"]))


def run_key(atom: dict[str, Any], run: dict[str, Any]) -> tuple[str, int, str, int, int]:
    """统一 run key。"""
    return (*atom_key(atom), int(run["run_id"]))


def build_turn_run_map(turn_payload: dict[str, Any]) -> dict[tuple[str, int, str, int, int], dict[str, Any]]:
    """索引 phase-turn run rows，用于补齐 q-gap 信息。"""
    mapping: dict[tuple[str, int, str, int, int], dict[str, Any]] = {}
    for atom in turn_payload["finite_audit"]["atom_phase_turn_profiles"]:
        for run in atom["phase_run_rows"]:
            mapping[run_key(atom, run)] = run
    return mapping


def collect_run_rows(
    variation_payload: dict[str, Any],
    turn_payload: dict[str, Any],
) -> list[dict[str, Any]]:
    """抽取所有 monotone run，并补齐相位/间隔字段。"""
    turn_runs = build_turn_run_map(turn_payload)
    rows: list[dict[str, Any]] = []
    for atom in variation_payload["finite_audit"]["atom_variation_profiles"]:
        key = atom_key(atom)
        for run in atom["run_variation_rows"]:
            signed = frac_from_record(run["signed_delta"])
            variation = frac_from_record(run["variation"])
            turn = turn_runs.get(run_key(atom, run), {})
            local_ratio = abs(signed) / variation if variation else Fraction(0)
            rows.append(
                {
                    "packet_side": key[0],
                    "packet_index": key[1],
                    "role": key[2],
                    "P": atom["P"],
                    "m": key[3],
                    "run_id": run["run_id"],
                    "direction": run["direction"],
                    "length": run["length"],
                    "transition_start": run["start_transition_index"],
                    "transition_end": run["end_transition_index"],
                    "q_start": run["q_start"],
                    "q_end": run["q_end"],
                    "q_gap_min": turn.get("q_gap_min"),
                    "q_gap_max": turn.get("q_gap_max"),
                    "A_wrap_count": run["A_wrap_count"],
                    "D_wrap_count": run["D_wrap_count"],
                    "carry_min": run["carry_min"],
                    "carry_max": run["carry_max"],
                    "signed_delta": frac_record(signed),
                    "variation": frac_record(variation),
                    "run_local_compression_ratio": frac_record(local_ratio),
                    "run_identity_verified": run.get("run_variation_identity_verified") is True
                    and variation == abs(signed),
                    "atom_key": f"{key[0]}:{key[1]}:{key[2]}:m{key[3]}",
                }
            )
    return rows


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造门控记录。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def role_summaries(run_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """按 selected/extra 汇总 run 级总变差和净位移。"""
    groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for item in run_rows:
        groups[item["role"]].append(item)
    rows: list[dict[str, Any]] = []
    for role in sorted(groups):
        items = groups[role]
        total = sum((frac_from_record(item["variation"]) for item in items), Fraction(0))
        signed = sum((frac_from_record(item["signed_delta"]) for item in items), Fraction(0))
        positive = sum(
            (frac_from_record(item["signed_delta"]) for item in items if frac_from_record(item["signed_delta"]) > 0),
            Fraction(0),
        )
        negative = -sum(
            (frac_from_record(item["signed_delta"]) for item in items if frac_from_record(item["signed_delta"]) < 0),
            Fraction(0),
        )
        local_ratios = [frac_from_record(item["run_local_compression_ratio"]) for item in items]
        rows.append(
            {
                "role": role,
                "run_count": len(items),
                "transition_count": sum(int(item["length"]) for item in items),
                "positive_run_count": sum(1 for item in items if item["direction"] == "positive"),
                "negative_run_count": sum(1 for item in items if item["direction"] == "negative"),
                "total_variation": frac_record(total),
                "signed_net": frac_record(signed),
                "abs_net": frac_record(abs(signed)),
                "positive_variation": frac_record(positive),
                "negative_variation": frac_record(negative),
                "aggregate_total_to_net_ratio": frac_record(abs(signed) / total),
                "run_local_ratio_min": frac_record(min(local_ratios)),
                "run_local_ratio_max": frac_record(max(local_ratios)),
                "strict_run_local_compression_count": sum(1 for value in local_ratios if value < 1),
            }
        )
    return rows


def cancel_atom_runs(items: list[dict[str, Any]]) -> dict[str, Any]:
    """对单个 atom 的相邻反向 run 做有限贪心抵消分解。"""
    stack: list[dict[str, Any]] = []
    cancelled = Fraction(0)
    event_count = 0
    for item in sorted(items, key=lambda row_item: int(row_item["run_id"])):
        delta = frac_from_record(item["signed_delta"])
        sign = 1 if delta > 0 else -1 if delta < 0 else 0
        mass = abs(delta)
        if sign == 0:
            continue
        source = {
            "sign": sign,
            "mass": mass,
            "run_id": item["run_id"],
            "direction": item["direction"],
            "q_start": item["q_start"],
            "q_end": item["q_end"],
        }
        while mass and stack and stack[-1]["sign"] != sign:
            chunk = min(stack[-1]["mass"], mass)
            stack[-1]["mass"] -= chunk
            mass -= chunk
            cancelled += chunk
            event_count += 1
            if stack[-1]["mass"] == 0:
                stack.pop()
        if mass:
            source["mass"] = mass
            stack.append(source)
    survivor_signed = sum((item["sign"] * item["mass"] for item in stack), Fraction(0))
    survivor_mass = sum((item["mass"] for item in stack), Fraction(0))
    return {
        "cancelled_mass": cancelled,
        "cancel_event_count": event_count,
        "survivor_signed": survivor_signed,
        "survivor_mass": survivor_mass,
        "survivor_fragments": stack,
    }


def atom_cancellation_rows(run_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """按 atom 输出 cancelled chunks + local survivor 分解。"""
    groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for item in run_rows:
        groups[item["atom_key"]].append(item)
    rows: list[dict[str, Any]] = []
    for key in sorted(groups):
        items = groups[key]
        first = items[0]
        total = sum((frac_from_record(item["variation"]) for item in items), Fraction(0))
        signed = sum((frac_from_record(item["signed_delta"]) for item in items), Fraction(0))
        cancel = cancel_atom_runs(items)
        survivor_direction = (
            "positive" if cancel["survivor_signed"] > 0 else "negative" if cancel["survivor_signed"] < 0 else "zero"
        )
        rows.append(
            {
                "atom_key": key,
                "packet": f"{first['packet_side']}:{first['packet_index']}",
                "role": first["role"],
                "P": first["P"],
                "m": first["m"],
                "run_count": len(items),
                "transition_count": sum(int(item["length"]) for item in items),
                "total_variation": frac_record(total),
                "signed_net": frac_record(signed),
                "cancelled_mass": frac_record(cancel["cancelled_mass"]),
                "cancelled_variation_removed": frac_record(2 * cancel["cancelled_mass"]),
                "cancel_event_count": cancel["cancel_event_count"],
                "survivor_mass": frac_record(cancel["survivor_mass"]),
                "survivor_signed": frac_record(cancel["survivor_signed"]),
                "survivor_direction": survivor_direction,
                "survivor_fragment_count": len(cancel["survivor_fragments"]),
                "survivor_fragments_sample": [
                    {
                        "run_id": frag["run_id"],
                        "direction": frag["direction"],
                        "q_start": frag["q_start"],
                        "q_end": frag["q_end"],
                        "mass": frac_record(frag["mass"]),
                    }
                    for frag in cancel["survivor_fragments"][:4]
                ],
                "atom_local_total_to_survivor_ratio": frac_record(cancel["survivor_mass"] / total),
                "decomposition_identity_verified": total - 2 * cancel["cancelled_mass"] == cancel["survivor_mass"]
                and signed == cancel["survivor_signed"],
            }
        )
    return rows


def bucket_rows(run_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """按 role/direction/wrap signature 分桶。"""
    groups: dict[tuple[str, str, bool, bool], list[dict[str, Any]]] = defaultdict(list)
    for item in run_rows:
        key = (
            item["role"],
            item["direction"],
            int(item["A_wrap_count"]) > 0,
            int(item["D_wrap_count"]) > 0,
        )
        groups[key].append(item)
    rows: list[dict[str, Any]] = []
    for (role, direction, a_wrap, d_wrap), items in sorted(groups.items()):
        total = sum((frac_from_record(item["variation"]) for item in items), Fraction(0))
        signed = sum((frac_from_record(item["signed_delta"]) for item in items), Fraction(0))
        rows.append(
            {
                "role": role,
                "direction": direction,
                "A_wrap_positive": a_wrap,
                "D_wrap_positive": d_wrap,
                "run_count": len(items),
                "transition_count": sum(int(item["length"]) for item in items),
                "variation": frac_record(total),
                "signed_delta": frac_record(signed),
                "max_run_variation": frac_record(max(frac_from_record(item["variation"]) for item in items)),
            }
        )
    return rows


def top_run_rows(run_rows: list[dict[str, Any]], limit: int = 12) -> list[dict[str, Any]]:
    """列出最大变差 run，定位 LocalSurvivor/PDEC 热点。"""
    ordered = sorted(run_rows, key=lambda item: frac_from_record(item["variation"]), reverse=True)
    return [
        {
            "atom_key": item["atom_key"],
            "role": item["role"],
            "P": item["P"],
            "m": item["m"],
            "run_id": item["run_id"],
            "direction": item["direction"],
            "length": item["length"],
            "q_interval": f"[{item['q_start']},{item['q_end']}]",
            "q_gap_min": item["q_gap_min"],
            "q_gap_max": item["q_gap_max"],
            "A_wrap_count": item["A_wrap_count"],
            "D_wrap_count": item["D_wrap_count"],
            "carry_range": f"[{item['carry_min']},{item['carry_max']}]",
            "variation": item["variation"],
            "signed_delta": item["signed_delta"],
        }
        for item in ordered[:limit]
    ]


def absorption_metrics(
    role_rows: list[dict[str, Any]],
    atom_rows: list[dict[str, Any]],
) -> dict[str, Any]:
    """计算有限 run 分解后的吸收读数。"""
    roles = {item["role"]: item for item in role_rows}
    selected = roles["selected_terminal"]
    extra = roles["extra_shell"]
    selected_negative_excess = max(-frac_from_record(selected["signed_net"]), Fraction(0))
    extra_negative_excess = max(-frac_from_record(extra["signed_net"]), Fraction(0))
    extra_total = frac_from_record(extra["total_variation"])
    extra_atom_survivor = sum(
        (frac_from_record(item["survivor_mass"]) for item in atom_rows if item["role"] == "extra_shell"),
        Fraction(0),
    )
    selected_atom_survivor = sum(
        (frac_from_record(item["survivor_mass"]) for item in atom_rows if item["role"] == "selected_terminal"),
        Fraction(0),
    )
    selected_vs_extra_survivor_margin = selected_negative_excess - extra_atom_survivor
    return {
        "selected_negative_excess": frac_record(selected_negative_excess),
        "extra_negative_excess": frac_record(extra_negative_excess),
        "extra_total_variation": frac_record(extra_total),
        "selected_atom_local_survivor_total": frac_record(selected_atom_survivor),
        "extra_atom_local_survivor_total": frac_record(extra_atom_survivor),
        "extra_total_to_atom_survivor_compression_ratio": frac_record(extra_atom_survivor / extra_total),
        "extra_total_to_atom_survivor_variation_removed": frac_record(extra_total - extra_atom_survivor),
        "selected_negative_excess_minus_extra_atom_survivor": frac_record(selected_vs_extra_survivor_margin),
        "selected_negative_excess_beats_extra_atom_survivor": selected_vs_extra_survivor_margin > 0,
        "finite_absorption_would_close_after_uniform_cancellation_law": selected_vs_extra_survivor_margin > 0,
    }


def gate_rows(metrics: dict[str, Any]) -> list[dict[str, Any]]:
    """生成本层门控表。"""
    return [
        row(
            "TerminalSignedPayloadImported",
            True,
            True,
            "上一层 mu(q,m,packet) signed payload measure 已导入。",
            "finite signed payload imported",
        ),
        row(
            "MonotoneRunRowsClosed",
            True,
            True,
            "59 个 monotone run 的 signed_delta、variation、wrap、carry、q-window 字段已全部抽取。",
            "finite run ledger closed",
        ),
        row(
            "RunLocalTotalToNetCompression",
            False,
            False,
            "每个 monotone run 内 variation=abs(signed_delta)，局部压缩比恒为 1；run 内没有相消。",
            RUN_CANCELLATION,
        ),
        row(
            "AtomAdjacentCancellationDecompositionClosed",
            True,
            True,
            "每个 atom 可有限分解为 adjacent opposite-run cancelled chunks 加 atom-local survivor。",
            "finite decomposition only",
        ),
        row(
            "ExtraTotalToAtomSurvivorIfCancellationLaw",
            metrics["finite_absorption_would_close_after_uniform_cancellation_law"],
            False,
            "若能全局证明 adjacent-run cancellation law，则 extra total variation 将压到 atom survivor。",
            f"{RUN_CANCELLATION} OR {LOCAL_SURVIVOR}",
        ),
        row(
            "SelectedBeatsExtraAtomSurvivorFiniteCheck",
            metrics["selected_negative_excess_beats_extra_atom_survivor"],
            True,
            "有限账本中 selected negative excess 已大于 extra atom-local survivor。",
            "finite numerical check; not a global theorem",
        ),
        row(
            "UniformRunCancellationLawProved",
            False,
            False,
            "尚无可审稿的 uniform family/trace/Type-II 定理把 run cancellation 推广到所有反例链。",
            f"{RUN_CANCELLATION} AND {TRACE_FAMILY}",
        ),
        row(
            "NamedLocalSurvivorReturnRegistered",
            True,
            False,
            "若 cancellation law 失败，剩余必须登记为 PDEC/SAE/LocalSurvivor，不能保留匿名。",
            f"{EXTRA_ABSORB} OR {LOCAL_SURVIVOR}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步闭合有限 run 分解和真正缺口位置，没有证明三命题无条件闭合。",
            f"{TOTAL_TO_NET} AND {EXTRA_ABSORB} AND {MOVING_BEATTY_SAVING} AND {TRACE_FAMILY}",
        ),
    ]


def external_frontier_note() -> list[dict[str, str]]:
    """外部前沿输入与当前缺口的适配边界。"""
    return [
        {
            "input": "Fouvry-Kowalski-Michel-Sawin, arXiv:2511.09459v3",
            "date": "2026-03-11",
            "usable_after": "terminal runs are promoted to a bilinear trace-function family with monodromy data",
            "current_gap": "the present object is a finite run ledger, not an ell-adic trace family",
            "url": "https://arxiv.org/abs/2511.09459",
        },
        {
            "input": "Milicevic-Qin-Wu, arXiv:2511.07550v1",
            "date": "2025-11-10",
            "usable_after": "moving Beatty numerator is completed into a genuine bilinear Kloosterman sum modulo q",
            "current_gap": "no admissible two-variable Kloosterman family has been constructed from the prime-q prefix",
            "url": "https://arxiv.org/abs/2511.07550",
        },
        {
            "input": "Pascadi, arXiv:2505.00653v2",
            "date": "2025-06-29",
            "usable_after": "Prime Matrix weights become triply-well-factorable AP averages",
            "current_gap": "row/column positivity is pointwise at P^2 scale, not an averaged distribution statement",
            "url": "https://arxiv.org/abs/2505.00653",
        },
        {
            "input": "Wright, arXiv:2604.25177v1",
            "date": "2026-04-28",
            "usable_after": "terminal payload is upgraded to a trilinear Kloosterman-fraction convolution",
            "current_gap": "current signed payload is one-dimensional and finite, with no equidistributed beta sequence",
            "url": "https://arxiv.org/abs/2604.25177",
        },
    ]


def build_certificate() -> dict[str, Any]:
    """组装证书。"""
    variation_payload = load_json(VARIATION)
    turn_payload = load_json(TURN_WORD)
    signed_payload = load_json(SIGNED_PAYLOAD)
    run_rows = collect_run_rows(variation_payload, turn_payload)
    roles = role_summaries(run_rows)
    atoms = atom_cancellation_rows(run_rows)
    metrics = absorption_metrics(roles, atoms)
    all_identities = all(item["run_identity_verified"] for item in run_rows) and all(
        item["decomposition_identity_verified"] for item in atoms
    )
    local_ratios = [frac_from_record(item["run_local_compression_ratio"]) for item in run_rows]
    return {
        "certificate_type": "prime_matrix_phi_lpf_terminal_monotone_run_total_to_net_compression_frontier_router",
        "status": "finite_run_decomposition_closed_uniform_compression_open",
        "verified_date": "2026-05-25",
        "previous_terminal_signed_payload_schema_closed": signed_payload.get(
            "terminal_signed_payload_measure_schema_closed"
        )
        is True,
        "terminal_monotone_run_ledger_closed": len(run_rows) == 59 and all_identities,
        "terminal_run_count_total": len(run_rows),
        "selected_terminal_run_count": sum(1 for item in run_rows if item["role"] == "selected_terminal"),
        "extra_shell_run_count": sum(1 for item in run_rows if item["role"] == "extra_shell"),
        "run_local_compression_ratio_min": frac_record(min(local_ratios)),
        "run_local_compression_ratio_max": frac_record(max(local_ratios)),
        "strict_run_local_compression_count": sum(1 for value in local_ratios if value < 1),
        "atom_adjacent_cancellation_decomposition_closed": all_identities,
        "finite_extra_total_to_atom_survivor_compression_closed": True,
        "finite_absorption_would_close_after_uniform_cancellation_law": metrics[
            "finite_absorption_would_close_after_uniform_cancellation_law"
        ],
        "monotone_run_total_to_net_compression_proved": False,
        "uniform_run_cancellation_family_created": False,
        "extra_total_variation_absorption_proved": False,
        "named_local_survivor_return_registered": True,
        "admissible_averaged_trace_family_created": False,
        "trace_or_kloosterman_completion_ready": False,
        "phi_lpf_parity_barrier_globally_broken": False,
        "row_column_unconditional_closed": False,
        "absorption_metrics": metrics,
        "role_summary_rows": roles,
        "atom_cancellation_rows": atoms,
        "wrap_bucket_rows": bucket_rows(run_rows),
        "largest_run_rows": top_run_rows(run_rows),
        "gate_rows": gate_rows(metrics),
        "external_frontier_note": external_frontier_note(),
        "source_hashes": source_hashes(),
        "next_primary_attack_target": (
            f"{RUN_CANCELLATION} AND {LOCAL_SURVIVOR} AND "
            f"{MOVING_BEATTY_SAVING} AND {TRACE_FAMILY}"
        ),
        "plain_conclusion": (
            "The finite terminal run ledger decomposes exactly into adjacent opposite-run "
            "cancellations plus atom-local survivors.  This explains how the extra total "
            "variation 14.109301881162 would compress to the extra atom survivor "
            "0.907719323182 if a uniform run-cancellation law were available.  However each "
            "monotone run itself has local compression ratio one, so the required saving is "
            "not local inside a run.  The remaining proof obligation is a uniform adjacent-run "
            "cancellation family, an admissible trace/Kloosterman/Type-II family, or a named "
            "PDEC/SAE/LocalSurvivor return."
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = []
    lines.append("# Prime Matrix Phi-LPF terminal monotone-run total-to-net compression frontier 证书")
    lines.append("")
    lines.append(f"**状态：** `{result['status']}`")
    lines.append(f"**核验日期：** `{result['verified_date']}`")
    lines.append("")
    lines.append("本证书继续上一层 signed payload absorption，逐 run 检查 total variation 能否压成 net。")
    lines.append("结论是：有限相消分解可闭合，但全局 run-cancellation 定理仍未证明。")
    lines.append("")
    lines.append("```text")
    for key in [
        "previous_terminal_signed_payload_schema_closed",
        "terminal_monotone_run_ledger_closed",
        "terminal_run_count_total",
        "selected_terminal_run_count",
        "extra_shell_run_count",
        "strict_run_local_compression_count",
        "atom_adjacent_cancellation_decomposition_closed",
        "finite_absorption_would_close_after_uniform_cancellation_law",
        "monotone_run_total_to_net_compression_proved",
        "uniform_run_cancellation_family_created",
        "extra_total_variation_absorption_proved",
        "trace_or_kloosterman_completion_ready",
        "row_column_unconditional_closed",
        "phi_lpf_parity_barrier_globally_broken",
    ]:
        value = result[key]
        lines.append(f"{key}={fmt_bool(value) if isinstance(value, bool) else value}")
    lines.append("```")
    lines.append("")
    lines.append("## 1. 压缩读数")
    lines.append("")
    metrics = result["absorption_metrics"]
    lines.append("```text")
    lines.append(f"selected_negative_excess={render_fraction(metrics['selected_negative_excess'])}")
    lines.append(f"extra_total_variation={render_fraction(metrics['extra_total_variation'])}")
    lines.append(f"extra_atom_local_survivor_total={render_fraction(metrics['extra_atom_local_survivor_total'])}")
    lines.append(
        "extra_total_to_atom_survivor_compression_ratio="
        f"{render_fraction(metrics['extra_total_to_atom_survivor_compression_ratio'])}"
    )
    lines.append(
        "extra_total_to_atom_survivor_variation_removed="
        f"{render_fraction(metrics['extra_total_to_atom_survivor_variation_removed'])}"
    )
    lines.append(
        "selected_negative_excess_minus_extra_atom_survivor="
        f"{render_fraction(metrics['selected_negative_excess_minus_extra_atom_survivor'])}"
    )
    lines.append("```")
    lines.append("")
    lines.append("解释：若存在 uniform adjacent-run cancellation law，extra 的强总变差会被压到")
    lines.append("atom-local survivor，有限账本中 selected negative excess 足以支付它。")
    lines.append("但每个 monotone run 内部压缩比恒为 1，所需相消来自 run 间配对，不是局部事实。")
    lines.append("")
    lines.append("## 2. role 汇总")
    lines.append("")
    lines.append("| role | runs | transitions | +runs | -runs | total variation | signed net | abs net | total-to-net ratio | local ratio range |")
    lines.append("| --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |")
    for item in result["role_summary_rows"]:
        ratio_range = (
            f"{item['run_local_ratio_min']['decimal']}..{item['run_local_ratio_max']['decimal']}"
        )
        lines.append(
            f"| `{item['role']}` | {item['run_count']} | {item['transition_count']} | "
            f"{item['positive_run_count']} | {item['negative_run_count']} | "
            f"{render_fraction(item['total_variation'])} | {render_fraction(item['signed_net'])} | "
            f"{render_fraction(item['abs_net'])} | {render_fraction(item['aggregate_total_to_net_ratio'])} | "
            f"`{ratio_range}` |"
        )
    lines.append("")
    lines.append("## 3. atom cancellation 分解")
    lines.append("")
    lines.append("| atom | role | P | m | runs | total variation | cancelled removed | survivor | survivor direction | ratio | identity |")
    lines.append("| --- | --- | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- |")
    for item in result["atom_cancellation_rows"]:
        lines.append(
            f"| `{cell(item['atom_key'])}` | `{item['role']}` | {item['P']} | {item['m']} | "
            f"{item['run_count']} | {render_fraction(item['total_variation'])} | "
            f"{render_fraction(item['cancelled_variation_removed'])} | "
            f"{render_fraction(item['survivor_mass'])} | `{item['survivor_direction']}` | "
            f"{render_fraction(item['atom_local_total_to_survivor_ratio'])} | "
            f"`{fmt_bool(item['decomposition_identity_verified'])}` |"
        )
    lines.append("")
    lines.append("## 4. 最大 run 热点")
    lines.append("")
    lines.append("| atom | role | run | dir | len | q | gap | wraps | carry | variation |")
    lines.append("| --- | --- | ---: | --- | ---: | --- | --- | --- | --- | --- |")
    for item in result["largest_run_rows"]:
        gap = f"[{item['q_gap_min']},{item['q_gap_max']}]"
        wraps = f"A{item['A_wrap_count']}/D{item['D_wrap_count']}"
        lines.append(
            f"| `{cell(item['atom_key'])}` | `{item['role']}` | {item['run_id']} | "
            f"`{item['direction']}` | {item['length']} | `{item['q_interval']}` | `{gap}` | "
            f"`{wraps}` | `{item['carry_range']}` | {render_fraction(item['variation'])} |"
        )
    lines.append("")
    lines.append("## 5. 门控表")
    lines.append("")
    lines.append("| gate | closed | proved | meaning | remaining |")
    lines.append("| --- | --- | --- | --- | --- |")
    for item in result["gate_rows"]:
        lines.append(
            f"| `{cell(item['gate'])}` | `{fmt_bool(item['closed'])}` | `{fmt_bool(item['proved'])}` | "
            f"{cell(item['meaning'])} | `{cell(item['remaining'])}` |"
        )
    lines.append("")
    lines.append("## 6. 外部前沿适配")
    lines.append("")
    lines.append("| input | date | usable after | current gap | url |")
    lines.append("| --- | --- | --- | --- | --- |")
    for item in result["external_frontier_note"]:
        lines.append(
            f"| {cell(item['input'])} | `{item['date']}` | {cell(item['usable_after'])} | "
            f"{cell(item['current_gap'])} | {item['url']} |"
        )
    lines.append("")
    lines.append("## 7. 最新开放口")
    lines.append("")
    lines.append("```text")
    lines.append(result["next_primary_attack_target"])
    lines.append("```")
    lines.append("")
    lines.append("## 8. 依赖哈希")
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
    print(f"terminal_run_count_total={result['terminal_run_count_total']}")
    print(
        "finite_absorption_would_close_after_uniform_cancellation_law="
        f"{fmt_bool(result['finite_absorption_would_close_after_uniform_cancellation_law'])}"
    )
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
