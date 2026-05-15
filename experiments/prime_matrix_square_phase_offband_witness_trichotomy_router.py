#!/usr/bin/env python3
"""把二次相位节省压成 off-band 尾素见证与 plus/minus 三分结构。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_witness_trichotomy_router.py --max-p 5000
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-witness-trichotomy-router.json

输出：
  data/square-phase-offband-witness-trichotomy-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-witness-trichotomy-router.json
  docs/monograph/prime-matrix-square-phase-offband-witness-trichotomy-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

PHASEBAND_ROUTER = ROOT / "experiments" / "prime_matrix_square_phase_halfgrid_noslot_phaseband_pdec_router.py"
SAVING_ROUTER = ROOT / "experiments" / "prime_matrix_square_phase_phaseband_saving_dichotomy_router.py"

OUT_LEDGER = DATA / "square-phase-offband-witness-trichotomy-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-witness-trichotomy-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-witness-trichotomy-router.md"

MAIN_TARGET = "TailEnvelopeOrQuadraticPhaseSavingGlobalLowerBound"
NEXT_TARGET = "RequiredOffBandTailPrimeWitnessOrExtremeOrientationPDECExclusion"


def load_module(path: Path, name: str) -> Any:
    """按路径加载前置路由器。"""
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def tail_primes_for_p(phase: Any, p: int, primes: list[int]) -> list[int]:
    """返回 alpha=4/5 尾窗内的素数 q。"""
    cutoff = phase.cutoff_alpha45(p)
    return [q_value for q_value in primes if cutoff < q_value < p]


def trichotomy_record(p: int, q_value: int) -> dict[str, Any]:
    """返回单个尾素的二次相位三分记录。"""
    b_value = (p - q_value) // 2
    half = (p - 1) // 2
    base_mod = (2 * b_value * b_value) % q_value
    lower_cut = q_value - half
    plus_gap = q_value - base_mod
    minus_gap = base_mod
    plus_no_slot = plus_gap > half
    minus_no_slot = minus_gap > half
    plus_offband = not plus_no_slot
    minus_offband = not minus_no_slot
    if base_mod < lower_cut:
        band = "plus_only_noslot"
    elif base_mod > half:
        band = "minus_only_noslot"
    else:
        band = "both_offband_middle"
    return {
        "q": q_value,
        "b": b_value,
        "half": half,
        "base_mod": base_mod,
        "lower_cut": lower_cut,
        "middle_width": max(0, half - lower_cut + 1),
        "plus_gap": plus_gap,
        "minus_gap": minus_gap,
        "plus_no_slot": plus_no_slot,
        "minus_no_slot": minus_no_slot,
        "plus_offband": plus_offband,
        "minus_offband": minus_offband,
        "band": band,
        "trichotomy_ok": (
            (band == "plus_only_noslot" and plus_no_slot and minus_offband)
            or (band == "minus_only_noslot" and minus_no_slot and plus_offband)
            or (band == "both_offband_middle" and plus_offband and minus_offband)
        ),
        "no_double_noslot": not (plus_no_slot and minus_no_slot),
    }


def side_record(p: int, side: str, h_value: int, tail_records: list[dict[str, Any]]) -> dict[str, Any]:
    """生成单侧 off-band 见证记录。"""
    tail_count = len(tail_records)
    if side == "plus":
        phaseband_count = sum(1 for row in tail_records if row["plus_no_slot"])
        offband_records = [row for row in tail_records if row["plus_offband"]]
        extreme_count = sum(1 for row in tail_records if row["band"] == "plus_only_noslot")
    elif side == "minus":
        phaseband_count = sum(1 for row in tail_records if row["minus_no_slot"])
        offband_records = [row for row in tail_records if row["minus_offband"]]
        extreme_count = sum(1 for row in tail_records if row["band"] == "minus_only_noslot")
    else:
        raise ValueError(f"unknown side: {side}")
    offband_count = len(offband_records)
    signed_tail_deficit = 2 * tail_count - h_value
    tail_deficit = max(0, signed_tail_deficit)
    required_witness_count = max(0, signed_tail_deficit // 2 + 1)
    pressure_threshold = (h_value + 1) // 2
    witness_shortage = max(0, required_witness_count - offband_count)
    exact_pressure_margin = h_value - 2 * phaseband_count
    selected = sorted(
        offband_records,
        key=lambda row: (
            row[f"{side}_gap"],
            -row["q"],
        ),
    )[: max(required_witness_count, 4)]
    return {
        "p": p,
        "side": side,
        "halfgrid_survivors": h_value,
        "tail_prime_count": tail_count,
        "phaseband_count": phaseband_count,
        "offband_witness_count": offband_count,
        "extreme_orientation_count": extreme_count,
        "pressure_threshold": pressure_threshold,
        "tail_envelope_margin": h_value - 2 * tail_count,
        "tail_deficit": tail_deficit,
        "required_offband_witness_count": required_witness_count,
        "witness_surplus": offband_count - required_witness_count,
        "witness_shortage": witness_shortage,
        "exact_pressure_margin": exact_pressure_margin,
        "phaseband_pressure_defect": phaseband_count >= pressure_threshold,
        "witness_gate_ok": offband_count >= required_witness_count,
        "pressure_witness_equivalence_ok": (exact_pressure_margin > 0) == (offband_count >= required_witness_count),
        "selected_offband_witnesses": [
            {
                "q": row["q"],
                "b": row["b"],
                "base_mod": row["base_mod"],
                "lower_cut": row["lower_cut"],
                "gap": row[f"{side}_gap"],
                "band": row["band"],
            }
            for row in selected
        ],
    }


def compact_side(row: dict[str, Any]) -> dict[str, Any]:
    """压缩单侧记录。"""
    return {
        "p": row["p"],
        "side": row["side"],
        "halfgrid_survivors": row["halfgrid_survivors"],
        "tail_prime_count": row["tail_prime_count"],
        "phaseband_count": row["phaseband_count"],
        "offband_witness_count": row["offband_witness_count"],
        "extreme_orientation_count": row["extreme_orientation_count"],
        "pressure_threshold": row["pressure_threshold"],
        "tail_envelope_margin": row["tail_envelope_margin"],
        "tail_deficit": row["tail_deficit"],
        "required_offband_witness_count": row["required_offband_witness_count"],
        "witness_surplus": row["witness_surplus"],
        "witness_shortage": row["witness_shortage"],
        "exact_pressure_margin": row["exact_pressure_margin"],
        "selected_offband_witnesses": row["selected_offband_witnesses"][:6],
    }


def compact_trichotomy(row: dict[str, Any]) -> dict[str, Any]:
    """压缩尾素三分记录。"""
    return {
        "q": row["q"],
        "b": row["b"],
        "base_mod": row["base_mod"],
        "lower_cut": row["lower_cut"],
        "middle_width": row["middle_width"],
        "plus_gap": row["plus_gap"],
        "minus_gap": row["minus_gap"],
        "band": row["band"],
    }


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "tailprime_signed_phase_trichotomy",
            "status": "closed",
            "statement": "For each tail prime q=P-2b, base=2b^2 mod q lies in exactly one of plus-only no-slot, minus-only no-slot, or both-offband middle.",
        },
        {
            "name": "no_double_noslot_for_tailprime",
            "status": "closed",
            "statement": "A tail prime cannot be no-slot on both plus and minus sides.",
        },
        {
            "name": "offband_witness_pressure_gate",
            "status": "closed",
            "statement": "For each side, H>2C is equivalent to having at least max(0, floor((2T-H)/2)+1) off-band tail-prime witnesses when H<=2T.",
        },
        {
            "name": "finite_required_witnesses_present",
            "status": "finite_evidence",
            "statement": "The finite audit finds no required off-band witness shortage up to the tested bound.",
        },
        {
            "name": "global_witness_or_orientation_pdec",
            "status": "open",
            "statement": "A global proof still needs required off-band witnesses, or exclusion of an extreme-orientation PDEC where too many tail primes fall on one no-slot side.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "SignedPhaseTrichotomyClosed",
            "closed": result["trichotomy_failure_count"] == 0,
            "proved": True,
            "meaning": "尾素二次相位三分逐点闭合。",
            "remaining": "closed",
        },
        {
            "gate": "NoDoubleNoSlotClosed",
            "closed": result["double_noslot_failure_count"] == 0,
            "proved": True,
            "meaning": "同一尾素不会同时成为 plus 与 minus 的 no-slot 负载。",
            "remaining": "closed",
        },
        {
            "gate": "OffBandWitnessGateClosed",
            "closed": result["pressure_witness_equivalence_failure_count"] == 0,
            "proved": True,
            "meaning": "压力不等式已经等价为 off-band 尾素见证数下界。",
            "remaining": "closed",
        },
        {
            "gate": "FiniteNoWitnessShortage",
            "closed": result["witness_shortage_count"] == 0,
            "proved": False,
            "meaning": "有限扫描没有见证不足。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "GlobalWitnessOrOrientationPDECExcluded",
            "closed": False,
            "proved": False,
            "meaning": "仍需全局排斥一侧极端取向过密，或证明所需 off-band 见证必存在。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只把相位节省硬点压成见证/取向 PDEC，不关闭全局行/列命题。",
            "remaining": NEXT_TARGET,
        },
    ]


def build_result(max_p: int, sample_ps: list[int]) -> dict[str, Any]:
    """构造路由器结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    phase = load_module(PHASEBAND_ROUTER, "phaseband_router")
    split = phase.load_split_router()
    prime_flags = split.sieve(max_p * max_p + max_p)
    pi_prefix = split.prime_prefix(prime_flags)
    small_flags = phase.sieve(max_p)
    primes = phase.primes_from_flags(small_flags, max_p)
    p_values = [p_value for p_value in primes if p_value >= 3]
    side_records: list[dict[str, Any]] = []
    pair_records: list[dict[str, Any]] = []
    trichotomy_failures: list[dict[str, Any]] = []
    double_failures: list[dict[str, Any]] = []
    for p_value in p_values:
        split_record = split.audit_p(p_value, prime_flags, pi_prefix)
        tail_records = [trichotomy_record(p_value, q_value) for q_value in tail_primes_for_p(phase, p_value, primes)]
        trichotomy_failures.extend(row for row in tail_records if not row["trichotomy_ok"])
        double_failures.extend(row for row in tail_records if not row["no_double_noslot"])
        plus_side = side_record(p_value, "plus", split_record["plus_prime_window"], tail_records)
        minus_side = side_record(p_value, "minus", split_record["minus_prime_window"], tail_records)
        side_records.extend([plus_side, minus_side])
        plus_count = sum(1 for row in tail_records if row["band"] == "plus_only_noslot")
        minus_count = sum(1 for row in tail_records if row["band"] == "minus_only_noslot")
        middle_count = sum(1 for row in tail_records if row["band"] == "both_offband_middle")
        pair_records.append(
            {
                "p": p_value,
                "tail_prime_count": len(tail_records),
                "plus_only_noslot_count": plus_count,
                "minus_only_noslot_count": minus_count,
                "both_offband_middle_count": middle_count,
                "phase_orientation_identity_ok": plus_count + minus_count + middle_count == len(tail_records),
                "combined_phaseband_count": plus_side["phaseband_count"] + minus_side["phaseband_count"],
                "combined_offband_witness_count": plus_side["offband_witness_count"] + minus_side["offband_witness_count"],
                "combined_identity_ok": (
                    plus_side["phaseband_count"] + minus_side["phaseband_count"] + middle_count == len(tail_records)
                    and plus_side["offband_witness_count"] + minus_side["offband_witness_count"]
                    == len(tail_records) + middle_count
                ),
                "sample_tail_records": [compact_trichotomy(row) for row in tail_records[:12]],
            }
        )
    pressure_equivalence_failures = [row for row in side_records if not row["pressure_witness_equivalence_ok"]]
    witness_shortages = [row for row in side_records if row["witness_shortage"] > 0]
    tail_defect_records = [row for row in side_records if row["tail_envelope_margin"] <= 0]
    pair_identity_failures = [row for row in pair_records if not row["phase_orientation_identity_ok"] or not row["combined_identity_ok"]]
    sample_set = set(sample_ps)
    witness_frontier = sorted(side_records, key=lambda row: (row["witness_surplus"], row["exact_pressure_margin"], row["p"], row["side"]))
    tail_frontier = sorted(tail_defect_records, key=lambda row: (row["tail_envelope_margin"], row["witness_surplus"], row["p"], row["side"]))
    orientation_frontier = sorted(
        side_records,
        key=lambda row: (
            row["extreme_orientation_count"] - row["pressure_threshold"],
            row["exact_pressure_margin"],
            row["p"],
            row["side"],
        ),
        reverse=True,
    )
    aggregate = {
        "record_count": len(side_records),
        "pair_record_count": len(pair_records),
        "tail_prime_total": sum(row["tail_prime_count"] for row in pair_records),
        "plus_only_noslot_total": sum(row["plus_only_noslot_count"] for row in pair_records),
        "minus_only_noslot_total": sum(row["minus_only_noslot_count"] for row in pair_records),
        "both_offband_middle_total": sum(row["both_offband_middle_count"] for row in pair_records),
        "trichotomy_failure_count": len(trichotomy_failures),
        "double_noslot_failure_count": len(double_failures),
        "pair_identity_failure_count": len(pair_identity_failures),
        "pressure_witness_equivalence_failure_count": len(pressure_equivalence_failures),
        "witness_shortage_count": len(witness_shortages),
        "tail_envelope_defect_count": len(tail_defect_records),
        "max_required_offband_witness_count": max((row["required_offband_witness_count"] for row in side_records), default=0),
        "min_witness_surplus": witness_frontier[0]["witness_surplus"] if witness_frontier else None,
        "min_exact_pressure_margin": min((row["exact_pressure_margin"] for row in side_records), default=None),
    }
    ledger = {
        "parameters": {"max_p": max_p, "sample_ps": sample_ps},
        "prime_count": len(p_values),
        "aggregate": aggregate,
        "witness_frontier": [compact_side(row) for row in witness_frontier[:80]],
        "tail_defect_frontier": [compact_side(row) for row in tail_frontier[:80]],
        "orientation_frontier": [compact_side(row) for row in orientation_frontier[:80]],
        "tail_defect_records": [compact_side(row) for row in tail_defect_records[:120]],
        "witness_shortage_records": [compact_side(row) for row in witness_shortages[:40]],
        "pressure_witness_equivalence_failures": [compact_side(row) for row in pressure_equivalence_failures[:40]],
        "pair_identity_failures": pair_identity_failures[:20],
        "sample_side_records": [compact_side(row) for row in side_records if row["p"] in sample_set],
        "sample_pair_records": [row for row in pair_records if row["p"] in sample_set],
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = {
        "certificate_type": "prime_matrix_square_phase_offband_witness_trichotomy_router",
        "status": "phase_saving_reduced_to_required_offband_tailprime_witnesses_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "empirical_absence_not_used_as_proof": True,
        "parameters": ledger["parameters"],
        "finite_prime_count": len(p_values),
        "aggregate": aggregate,
        "trichotomy_failure_count": len(trichotomy_failures),
        "double_noslot_failure_count": len(double_failures),
        "pair_identity_failure_count": len(pair_identity_failures),
        "pressure_witness_equivalence_failure_count": len(pressure_equivalence_failures),
        "witness_shortage_count": len(witness_shortages),
        "tail_envelope_defect_count": len(tail_defect_records),
        "witness_frontier": ledger["witness_frontier"][:20],
        "tail_defect_frontier": ledger["tail_defect_frontier"][:20],
        "orientation_frontier": ledger["orientation_frontier"][:20],
        "sample_side_records": ledger["sample_side_records"],
        "sample_pair_records": ledger["sample_pair_records"],
        "tailprime_signed_phase_trichotomy_closed": len(trichotomy_failures) == 0,
        "no_double_noslot_closed": len(double_failures) == 0,
        "offband_witness_pressure_gate_closed": len(pressure_equivalence_failures) == 0,
        "finite_required_witnesses_present": len(witness_shortages) == 0,
        "global_witness_or_orientation_pdec_excluded": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_offband_witness_trichotomy_router.py": sha256(
                Path(__file__).resolve()
            ),
            "experiments/prime_matrix_square_phase_halfgrid_noslot_phaseband_pdec_router.py": sha256(
                PHASEBAND_ROUTER
            ),
            "experiments/prime_matrix_square_phase_phaseband_saving_dichotomy_router.py": sha256(SAVING_ROUTER),
            "data/square-phase-offband-witness-trichotomy-ledger.json": sha256(OUT_LEDGER),
        },
        "plain_conclusion": (
            "本步把二次相位节省 `T-C` 具体化为 off-band 尾素见证数。"
            "对每个尾素 `q=P-2b`，令 `base=2b^2 mod q`、`h=(P-1)/2`、`lower=q-h`。"
            "若 `base<lower`，它只给 plus 侧 no-slot 负载；若 `base>h`，它只给 minus 侧 no-slot 负载；"
            "若 `lower<=base<=h`，它同时给两侧 off-band 节省。因此同一尾素不可能同时伤害两侧。"
            "单侧压力目标 `H>2C` 等价于：当尾包络缺陷 `2T-H>=0` 时，至少存在 "
            "`floor((2T-H)/2)+1` 个 off-band 尾素见证。有限扫描没有见证不足；"
            "全局仍需证明这些见证必存在，或排斥尾素过度集中到单侧极端取向的 PDEC。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase off-band witness trichotomy router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"max_p={result['parameters']['max_p']}",
        f"finite_prime_count={result['finite_prime_count']}",
        f"trichotomy_failure_count={result['trichotomy_failure_count']}",
        f"double_noslot_failure_count={result['double_noslot_failure_count']}",
        f"pressure_witness_equivalence_failure_count={result['pressure_witness_equivalence_failure_count']}",
        f"witness_shortage_count={result['witness_shortage_count']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 尾素三分",
        "",
        "尾素写为 `q=P-2b`，并记",
        "",
        "```text",
        "h = (P-1)/2",
        "base = 2b^2 mod q",
        "lower = q-h = h-2b+1.",
        "```",
        "",
        "则三种情况互斥且穷尽：",
        "",
        "| condition | meaning |",
        "| --- | --- |",
        "| `base<lower` | 只给 plus 侧 no-slot 负载，minus 侧是 off-band 见证 |",
        "| `base>h` | 只给 minus 侧 no-slot 负载，plus 侧是 off-band 见证 |",
        "| `lower<=base<=h` | 同时给 plus/minus 两侧 off-band 见证 |",
        "",
        "因此同一尾素不会同时成为两侧 no-slot 负载。",
        "",
        "## 2. 见证阈值",
        "",
        "记 `H=HalfGridSurvivors_side(P)`、`T=TailPrimeCount(P)`、`C=NoSlotPhaseBandCount_side(P)`。单侧目标为 `H>2C`。当 `H<=2T` 时，所需 off-band 见证数为",
        "",
        "```text",
        "W_required = floor((2T-H)/2)+1.",
        "```",
        "",
        "且 `H>2C` 等价于 `W>=W_required`，其中 `W=T-C`。",
        "",
        "## 3. 有限审计摘要",
        "",
        "| metric | value |",
        "| --- | ---: |",
        f"| side records | {agg['record_count']} |",
        f"| pair records | {agg['pair_record_count']} |",
        f"| tail prime total | {agg['tail_prime_total']} |",
        f"| plus-only no-slot total | {agg['plus_only_noslot_total']} |",
        f"| minus-only no-slot total | {agg['minus_only_noslot_total']} |",
        f"| both-offband middle total | {agg['both_offband_middle_total']} |",
        f"| trichotomy failures | {agg['trichotomy_failure_count']} |",
        f"| double no-slot failures | {agg['double_noslot_failure_count']} |",
        f"| pair identity failures | {agg['pair_identity_failure_count']} |",
        f"| pressure-witness equivalence failures | {agg['pressure_witness_equivalence_failure_count']} |",
        f"| witness shortage count | {agg['witness_shortage_count']} |",
        f"| tail envelope defect count | {agg['tail_envelope_defect_count']} |",
        f"| max required off-band witnesses | {agg['max_required_offband_witness_count']} |",
        f"| min witness surplus | {agg['min_witness_surplus']} |",
        f"| min exact pressure margin | {agg['min_exact_pressure_margin']} |",
        "",
        "## 4. 最紧见证边界",
        "",
        "| P | side | H | T | C | W | W_req | surplus | tail margin | exact margin | witnesses |",
        "| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for record in result["witness_frontier"][:16]:
        witnesses = ",".join(f"{item['q']}:{item['band']}" for item in record["selected_offband_witnesses"][:4])
        lines.append(
            "| "
            + " | ".join(
                [
                    str(record["p"]),
                    f"`{record['side']}`",
                    str(record["halfgrid_survivors"]),
                    str(record["tail_prime_count"]),
                    str(record["phaseband_count"]),
                    str(record["offband_witness_count"]),
                    str(record["required_offband_witness_count"]),
                    str(record["witness_surplus"]),
                    str(record["tail_envelope_margin"]),
                    str(record["exact_pressure_margin"]),
                    f"`{witnesses}`",
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 5. 尾包络失败点",
            "",
            "| P | side | H | T | C | W | W_req | surplus | tail deficit | exact margin | witnesses |",
            "| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for record in result["tail_defect_frontier"][:24]:
        witnesses = ",".join(f"{item['q']}:{item['band']}" for item in record["selected_offband_witnesses"][:4])
        lines.append(
            "| "
            + " | ".join(
                [
                    str(record["p"]),
                    f"`{record['side']}`",
                    str(record["halfgrid_survivors"]),
                    str(record["tail_prime_count"]),
                    str(record["phaseband_count"]),
                    str(record["offband_witness_count"]),
                    str(record["required_offband_witness_count"]),
                    str(record["witness_surplus"]),
                    str(record["tail_deficit"]),
                    str(record["exact_pressure_margin"]),
                    f"`{witnesses}`",
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 6. 命题行",
            "",
            "| name | status | statement |",
            "| --- | --- | --- |",
        ]
    )
    for row in result["theorem_rows"]:
        lines.append(f"| `{row['name']}` | `{row['status']}` | {table_cell(row['statement'])} |")
    lines.extend(
        [
            "",
            "## 7. 决策表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | ---: | ---: | --- | --- |",
        ]
    )
    for row in result["decision_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{row['gate']}`",
                    f"`{fmt_bool(row['closed'])}`",
                    f"`{fmt_bool(row['proved'])}`",
                    table_cell(row["meaning"]),
                    table_cell(row["remaining"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 8. 下一步",
            "",
            "- 主攻：`RequiredOffBandTailPrimeWitnessOrExtremeOrientationPDECExclusion`。",
            "- 需要证明尾包络失败处必有足够 off-band 尾素见证。",
            "- 等价地，排斥尾素 `base=2b^2 mod q` 过度集中在单侧极端取向区间。",
            "- 当前仍未证明全局行/列无条件闭合。",
            "",
            "## 9. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in result["source_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-p", type=int, default=5000)
    parser.add_argument(
        "--sample-ps",
        type=str,
        default="23,37,43,47,73,113,313,673,691,733,1129,4999",
    )
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    sample_ps = [int(item) for item in args.sample_ps.split(",") if item.strip()]
    result = build_result(args.max_p, sample_ps)
    write_markdown(result)
    result["source_hashes"]["docs/monograph/prime-matrix-square-phase-offband-witness-trichotomy-router.md"] = sha256(
        OUT_MD
    )
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "max_p": args.max_p,
                "trichotomy_failure_count": result["trichotomy_failure_count"],
                "double_noslot_failure_count": result["double_noslot_failure_count"],
                "pressure_witness_equivalence_failure_count": result["pressure_witness_equivalence_failure_count"],
                "witness_shortage_count": result["witness_shortage_count"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
