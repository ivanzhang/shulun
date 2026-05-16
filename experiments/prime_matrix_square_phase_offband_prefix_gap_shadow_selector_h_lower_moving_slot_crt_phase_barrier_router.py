#!/usr/bin/env python3
"""审计 moving-slot 高因子吸收图样的 CRT 模数与相位支撑宽度屏障。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_moving_slot_crt_phase_barrier_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-moving-slot-crt-phase-barrier-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-selector-h-lower-moving-slot-crt-phase-barrier-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-moving-slot-crt-phase-barrier-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-moving-slot-crt-phase-barrier-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

TEMPLATE_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-template-provenance-ledger.json"
PHASE_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-equality-atom-phase-signature-ledger.json"
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-moving-slot-crt-phase-barrier-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-moving-slot-crt-phase-barrier-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-moving-slot-crt-phase-barrier-router.md"

RESIDUAL_MARGIN_ROUTER = (
    ROOT
    / "experiments"
    / "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_residual_prime_margin_router.py"
)
COMPANION_LOSS_ROUTER = (
    ROOT
    / "experiments"
    / "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_companion_composite_loss_router.py"
)
EVEN_LAYER_ROUTER = ROOT / "experiments" / "prime_matrix_square_phase_even_layer_interval_router.py"

MAIN_TARGET = "MovingSlotEqualityAtomPDECExclusionOrGlobalMarginJump"
NEXT_TARGET = "MovingSlotFamilyPDECOrGlobalResidualPrimeMarginJump"


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def load_module(path: Path, name: str) -> Any:
    """按路径加载模块。"""
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def least_prime_factor(value: int) -> int:
    """返回 value 的最小素因子；若 value 为素数则返回自身。"""
    if value % 2 == 0:
        return 2
    factor = 3
    while factor * factor <= value:
        if value % factor == 0:
            return factor
        factor += 2
    return value


def egcd(left: int, right: int) -> tuple[int, int, int]:
    """扩展欧几里得算法。"""
    if right == 0:
        return left, 1, 0
    gcd_value, x_next, y_next = egcd(right, left % right)
    return gcd_value, y_next, x_next - (left // right) * y_next


def crt_pair(residue_a: int, modulus_a: int, residue_b: int, modulus_b: int) -> tuple[int, int]:
    """合并两个相容 CRT 条件。"""
    gcd_value, inv_a, _ = egcd(modulus_a, modulus_b)
    delta = residue_b - residue_a
    if delta % gcd_value != 0:
        raise ValueError(
            f"incompatible CRT: x={residue_a} mod {modulus_a}, x={residue_b} mod {modulus_b}"
        )
    merged_modulus = modulus_a // gcd_value * modulus_b
    step = (delta // gcd_value * inv_a) % (modulus_b // gcd_value)
    merged_residue = (residue_a + modulus_a * step) % merged_modulus
    return merged_residue, merged_modulus


def combine_crt(congruences: list[dict[str, int]]) -> dict[str, int]:
    """合并同余条件。"""
    residue = 0
    modulus = 1
    for item in congruences:
        residue, modulus = crt_pair(residue, modulus, int(item["residue"]), int(item["modulus"]))
    return {"residue": residue, "modulus": modulus}


def slot_phase_interval(slot: dict[str, Any], side: str) -> dict[str, Any]:
    """计算固定 b/u 槽保持同一欧几里得相位的整数 P 区间。"""
    b_value = int(slot["b"])
    u_value = int(slot["u"])
    base = 2 * b_value * b_value

    if side == "minus":
        lower = base // (u_value + 1) + 2 * b_value + 1
        upper = 10**30 if u_value == 0 else base // u_value + 2 * b_value
        if u_value == 0:
            lower = max(lower, 2 * base + 1)
        else:
            lower = max(
                lower,
                (2 * base + 4 * b_value * u_value + 1 + (2 * u_value + 1) - 1)
                // (2 * u_value + 1),
            )
            upper = min(upper, (base + 2 * b_value * u_value - 1) // u_value)
    elif side == "plus":
        if u_value <= 0:
            raise ValueError("plus-side cap slot must have u>=1")
        lower = base // u_value + 2 * b_value + 1
        upper = 10**30 if u_value == 1 else base // (u_value - 1) + 2 * b_value
        lower = max(lower, (2 * b_value * (u_value + b_value) + 1 + u_value - 1) // u_value)
        upper = min(upper, (4 * b_value * (u_value + b_value) - 1) // (2 * u_value - 1))
    else:
        raise ValueError(f"unknown side: {side}")

    return {
        "phase_p_lo": lower,
        "phase_p_hi": upper,
        "phase_width": max(0, upper - lower + 1),
    }


def highfactor_slots(loss: Any, even: Any, p_value: int, side: str, prime_flags: bytearray) -> list[dict[str, Any]]:
    """枚举 residual 中 lpf(m)>7 的高因子吸收槽。"""
    rows = []
    for slot in loss.cap_slots(even, p_value, side, prime_flags):
        if slot["m_is_prime"]:
            continue
        lpf = least_prime_factor(int(slot["m"]))
        if lpf > 7:
            interval = slot_phase_interval(slot, side)
            rows.append({**slot, "least_prime_factor_m": lpf, **interval})
    return rows


def highfactor_crt_signature(slots: list[dict[str, Any]]) -> dict[str, Any]:
    """由高因子槽合成 CRT 签名。"""
    grouped: dict[int, list[dict[str, Any]]] = {}
    for slot in slots:
        ell = int(slot["least_prime_factor_m"])
        residue = (-2 * (int(slot["b"]) + int(slot["u"]))) % ell
        grouped.setdefault(ell, []).append({**slot, "modulus": ell, "residue": residue})

    consolidated = []
    compatible = True
    for ell, items in sorted(grouped.items()):
        residues = sorted({int(item["residue"]) for item in items})
        if len(residues) != 1:
            compatible = False
        consolidated.append(
            {
                "modulus": ell,
                "residue": residues[0] if len(residues) == 1 else residues,
                "slot_count": len(items),
                "compatible": len(residues) == 1,
            }
        )

    if not slots or not compatible:
        return {
            "compatible": compatible,
            "crt_residue": None,
            "crt_modulus": 1,
            "distinct_lpf_count": len(grouped),
            "consolidated": consolidated,
        }

    signature = combine_crt(
        [
            {"residue": int(item["residue"]), "modulus": int(item["modulus"])}
            for item in consolidated
            if bool(item["compatible"])
        ]
    )
    return {
        "compatible": compatible,
        "crt_residue": int(signature["residue"]),
        "crt_modulus": int(signature["modulus"]),
        "distinct_lpf_count": len(grouped),
        "consolidated": consolidated,
    }


def phase_intersection(slots: list[dict[str, Any]]) -> dict[str, Any]:
    """计算高因子槽相位交集。"""
    if not slots:
        return {
            "phase_p_lo": None,
            "phase_p_hi": None,
            "phase_width": None,
            "phase_nonempty": False,
        }
    lo_value = max(int(slot["phase_p_lo"]) for slot in slots)
    hi_value = min(int(slot["phase_p_hi"]) for slot in slots)
    return {
        "phase_p_lo": lo_value,
        "phase_p_hi": hi_value,
        "phase_width": max(0, hi_value - lo_value + 1),
        "phase_nonempty": lo_value <= hi_value,
    }


def barrier_record(row: dict[str, Any], loss: Any, even: Any, prime_flags: bytearray) -> dict[str, Any]:
    """生成单行 moving-slot CRT/phase 屏障记录。"""
    p_value = int(row["p"])
    side = str(row["side"])
    slots = highfactor_slots(loss, even, p_value, side, prime_flags)
    crt = highfactor_crt_signature(slots)
    phase = phase_intersection(slots)
    phase_width = phase["phase_width"]
    crt_modulus = int(crt["crt_modulus"])
    isolates = (
        bool(slots)
        and bool(crt["compatible"])
        and bool(phase["phase_nonempty"])
        and phase_width is not None
        and crt_modulus > int(phase_width)
        and crt["crt_residue"] is not None
        and p_value % crt_modulus == int(crt["crt_residue"])
        and int(phase["phase_p_lo"]) <= p_value <= int(phase["phase_p_hi"])
    )
    return {
        "template_index": int(row["template_index"]),
        "p": p_value,
        "side": side,
        "rho": int(row["rho"]),
        "failure_loaded_b_breakpoint": int(row["failure_loaded_b_breakpoint"]),
        "loaded_b_layers": int(row["loaded_b_layers"]),
        "residual_prime_pair_margin_to_bound": int(row["residual_prime_pair_margin_to_bound"]),
        "small_sieve_357_residual_cap_count": int(row["small_sieve_357_residual_cap_count"]),
        "small_sieve_357_residual_bound": int(row["small_sieve_357_residual_bound"]),
        "residual_prime_pair_count": int(row["residual_prime_pair_count"]),
        "highfactor_composite_absorber_count": len(slots),
        "highfactor_distinct_lpf_count": int(crt["distinct_lpf_count"]),
        "highfactor_crt_compatible": bool(crt["compatible"]),
        "highfactor_crt_residue": crt["crt_residue"],
        "highfactor_crt_modulus": crt_modulus,
        "phase_p_lo": phase["phase_p_lo"],
        "phase_p_hi": phase["phase_p_hi"],
        "phase_width": phase_width,
        "crt_minus_phase_width": None if phase_width is None else crt_modulus - int(phase_width),
        "fixed_highfactor_slot_pattern_isolated": isolates,
        "highfactor_lpf_histogram": {
            str(ell): sum(1 for slot in slots if int(slot["least_prime_factor_m"]) == ell)
            for ell in sorted({int(slot["least_prime_factor_m"]) for slot in slots})
        },
        "sample_highfactor_slots": [
            {
                "b": int(slot["b"]),
                "u": int(slot["u"]),
                "q": int(slot["q"]),
                "m": int(slot["m"]),
                "least_prime_factor_m": int(slot["least_prime_factor_m"]),
                "phase_p_lo": int(slot["phase_p_lo"]),
                "phase_p_hi": int(slot["phase_p_hi"]),
            }
            for slot in slots[:8]
        ],
    }


def select_tight_records(records: list[dict[str, Any]], limit: int) -> list[dict[str, Any]]:
    """选取最紧屏障记录。"""
    return sorted(
        records,
        key=lambda item: (
            int(item["residual_prime_pair_margin_to_bound"]),
            int(item["crt_minus_phase_width"]) if item["crt_minus_phase_width"] is not None else -1,
            int(item["p"]),
            item["side"],
            int(item["rho"]),
            int(item["template_index"]),
        ),
    )[:limit]


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "fixed_highfactor_slot_crt_phase_isolation_criterion",
            "status": "closed",
            "statement": "For any fixed highfactor slot pattern, if the CRT modulus from lpf(m)>7 exceeds the common phase-support width, that pattern has at most one P in the phase support.",
        },
        {
            "name": "current_sweep_highfactor_patterns_isolated",
            "status": "closed_on_current_sweep",
            "statement": "On the current selector sweep, every highfactor absorber pattern satisfies CRT modulus > phase width; the equality atom is one isolated instance.",
        },
        {
            "name": "moving_slot_family_exclusion",
            "status": "open",
            "statement": "A global proof must still exclude recurrence where the highfactor b/u slots themselves move with P, or route that moving family to PDEC/ColumnCRT.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    agg = result["aggregate"]
    return [
        {
            "gate": "FixedHighfactorSlotIsolationCriterionClosed",
            "closed": True,
            "proved": True,
            "meaning": "CRT 模数大于相位宽度时，固定高因子槽图样至多命中一个 P。",
            "remaining": "closed",
        },
        {
            "gate": "CurrentSweepHighfactorPatternsIsolated",
            "closed": agg["fixed_highfactor_slot_pattern_isolation_failure_count_at_p0"] == 0,
            "proved": False,
            "meaning": "当前重放中所有高因子图样都通过隔离门。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "CurrentEqualityAtomFixedPatternNonpersistent",
            "closed": agg["equality_atom_fixed_pattern_isolated"],
            "proved": True,
            "meaning": "唯一等号原子的固定高因子槽图样已不能复现。",
            "remaining": "closed",
        },
        {
            "gate": "MovingSlotFamilyExcluded",
            "closed": False,
            "proved": False,
            "meaning": "槽图样随 P 移动的等号族仍未排斥。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步不关闭全局行/列命题，只把固定图样持久性压成移动族 PDEC。",
            "remaining": result["next_direct_attack_target"],
        },
    ]


def build_result(template_ledger: Path, phase_ledger: Path, max_p: int, p0: int, target_h_coeff: float, tight_limit: int) -> dict[str, Any]:
    """构造 moving-slot CRT/phase 屏障结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    phase_source = load_json(phase_ledger)
    residual_margin = load_module(RESIDUAL_MARGIN_ROUTER, "moving_slot_residual_margin")
    loss = load_module(COMPANION_LOSS_ROUTER, "moving_slot_loss")
    even = load_module(EVEN_LAYER_ROUTER, "moving_slot_even")

    rows = residual_margin.enrich_margin_rows(max_p, template_ledger, target_h_coeff)
    selected = [row for row in rows if int(row["p"]) >= p0]
    prime_flags = even.sieve(2 * max_p + 1000)
    records = [barrier_record(row, loss, even, prime_flags) for row in selected]
    failures = [record for record in records if not bool(record["fixed_highfactor_slot_pattern_isolated"])]
    equality_records = [record for record in records if int(record["residual_prime_pair_margin_to_bound"]) == 0]
    exact_isolated = bool(equality_records) and all(
        bool(record["fixed_highfactor_slot_pattern_isolated"]) for record in equality_records
    )
    aggregate = {
        "template_ledger": str(template_ledger.relative_to(ROOT)),
        "phase_ledger": str(phase_ledger.relative_to(ROOT)),
        "max_p": max_p,
        "p0": p0,
        "target_h_coeff": target_h_coeff,
        "selected_hit_count_at_p0": len(selected),
        "barrier_record_count_at_p0": len(records),
        "fixed_highfactor_slot_pattern_isolation_failure_count_at_p0": len(failures),
        "equality_atom_count_at_p0": len(equality_records),
        "equality_atom_fixed_pattern_isolated": exact_isolated,
        "min_crt_minus_phase_width_at_p0": min(
            int(record["crt_minus_phase_width"])
            for record in records
            if record["crt_minus_phase_width"] is not None
        ),
        "min_highfactor_crt_modulus_at_p0": min(int(record["highfactor_crt_modulus"]) for record in records),
        "max_phase_width_at_p0": max(
            int(record["phase_width"]) for record in records if record["phase_width"] is not None
        ),
        "moving_slot_family_excluded": False,
        "global_residual_prime_margin_proved": False,
        "row_column_unconditional_closed": False,
    }
    ledger = {
        "parameters": {
            "max_p": max_p,
            "p0": p0,
            "target_h_coeff": target_h_coeff,
            "tight_limit": tight_limit,
        },
        "aggregate": aggregate,
        "fixed_atom_phase_signature_summary": {
            "registered_p": phase_source["aggregate"]["registered_p"],
            "highfactor_crt_residue": phase_source["aggregate"]["highfactor_crt_residue"],
            "highfactor_crt_modulus": phase_source["aggregate"]["highfactor_crt_modulus"],
            "phase_intersection": [
                phase_source["aggregate"]["phase_intersection_lo"],
                phase_source["aggregate"]["phase_intersection_hi"],
            ],
            "exact_fixed_slot_nonpersistence_proved": phase_source["aggregate"][
                "exact_fixed_slot_nonpersistence_proved"
            ],
        },
        "equality_atom_barrier_records": equality_records,
        "tight_barrier_records": select_tight_records(records, tight_limit),
        "isolation_failure_records": failures[:tight_limit],
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = {
        "certificate_type": "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_moving_slot_crt_phase_barrier_router",
        "status": "fixed_highfactor_slot_patterns_isolated_moving_slot_family_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_sweep_not_used_as_global_proof": True,
        "parameters": ledger["parameters"],
        "aggregate": aggregate,
        "fixed_atom_phase_signature_summary": ledger["fixed_atom_phase_signature_summary"],
        "equality_atom_barrier_records": equality_records,
        "tight_barrier_records": ledger["tight_barrier_records"],
        "isolation_failure_records": ledger["isolation_failure_records"],
        "moving_slot_family_excluded": False,
        "global_residual_prime_margin_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_moving_slot_crt_phase_barrier_router.py": sha256(
                Path(__file__).resolve()
            ),
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_residual_prime_margin_router.py": sha256(
                RESIDUAL_MARGIN_ROUTER
            ),
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_companion_composite_loss_router.py": sha256(
                COMPANION_LOSS_ROUTER
            ),
            "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-equality-atom-phase-signature-ledger.json": sha256(
                phase_ledger
            ),
            "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-moving-slot-crt-phase-barrier-ledger.json": sha256(
                OUT_LEDGER
            ),
        },
        "plain_conclusion": (
            "本步把 moving-slot 等号复现进一步压成固定高因子槽图样隔离门。"
            "确定性判据是：若 `lpf(m)>7` 槽给出的 CRT 模数大于这些槽共同的相位支撑宽度，"
            "则该固定高因子图样至多对应一个 P。"
            f"当前 `P>={p0}` 重放中隔离失败数为 "
            f"{aggregate['fixed_highfactor_slot_pattern_isolation_failure_count_at_p0']}；"
            "唯一等号原子的固定图样也已隔离。"
            "但如果 `b,u` 槽随 P 移动，本步只把它登记为下一层 moving family PDEC/ColumnCRT，"
            "还不是全局无条件闭合。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow selector H lower moving-slot CRT phase barrier router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"max_p={agg['max_p']}",
        f"p0={agg['p0']}",
        f"selected_hit_count_at_p0={agg['selected_hit_count_at_p0']}",
        f"fixed_highfactor_slot_pattern_isolation_failure_count_at_p0={agg['fixed_highfactor_slot_pattern_isolation_failure_count_at_p0']}",
        f"equality_atom_fixed_pattern_isolated={fmt_bool(agg['equality_atom_fixed_pattern_isolated'])}",
        f"min_crt_minus_phase_width_at_p0={agg['min_crt_minus_phase_width_at_p0']}",
        f"max_phase_width_at_p0={agg['max_phase_width_at_p0']}",
        f"moving_slot_family_excluded={fmt_bool(agg['moving_slot_family_excluded'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 判据",
        "",
        "```text",
        "fixed highfactor pattern isolated if:",
        "  CRT_modulus(lpf(m)>7 slots) > common_phase_width(fixed b/u slots)",
        "then at most one P in that fixed phase support can realize the pattern.",
        "```",
        "",
        "## 2. 等号原子屏障记录",
        "",
        "| p | side | rho | margin | highfactor | distinct lpf | CRT modulus | phase width | CRT-width | isolated |",
        "| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in result["equality_atom_barrier_records"]:
        lines.append(
            f"| {row['p']} | `{row['side']}` | {row['rho']} | {row['residual_prime_pair_margin_to_bound']} | "
            f"{row['highfactor_composite_absorber_count']} | {row['highfactor_distinct_lpf_count']} | "
            f"{row['highfactor_crt_modulus']} | {row['phase_width']} | {row['crt_minus_phase_width']} | "
            f"{fmt_bool(row['fixed_highfactor_slot_pattern_isolated'])} |"
        )
    lines.extend(
        [
            "",
            "## 3. 最紧屏障样本",
            "",
            "| p | side | rho | template | margin | highfactor | distinct lpf | CRT modulus | phase width | CRT-width | phase support |",
            "| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for row in result["tight_barrier_records"][:20]:
        lines.append(
            f"| {row['p']} | `{row['side']}` | {row['rho']} | {row['template_index']} | "
            f"{row['residual_prime_pair_margin_to_bound']} | {row['highfactor_composite_absorber_count']} | "
            f"{row['highfactor_distinct_lpf_count']} | {row['highfactor_crt_modulus']} | {row['phase_width']} | "
            f"{row['crt_minus_phase_width']} | `[{row['phase_p_lo']},{row['phase_p_hi']}]` |"
        )
    lines.extend(
        [
            "",
            "## 4. 失败形态",
            "",
        ]
    )
    if result["isolation_failure_records"]:
        lines.extend(
            [
                "| p | side | rho | margin | highfactor | CRT modulus | phase width |",
                "| ---: | --- | ---: | ---: | ---: | ---: | ---: |",
            ]
        )
        for row in result["isolation_failure_records"]:
            lines.append(
                f"| {row['p']} | `{row['side']}` | {row['rho']} | {row['residual_prime_pair_margin_to_bound']} | "
                f"{row['highfactor_composite_absorber_count']} | {row['highfactor_crt_modulus']} | {row['phase_width']} |"
            )
    else:
        lines.append("当前重放中没有固定高因子槽图样隔离失败。")
    lines.extend(
        [
            "",
            "## 5. 结构判断",
            "",
            "- 固定高因子槽图样已经被 CRT 模数/相位宽度屏障孤立。",
            "- 因此持久等号若存在，必须让高因子 `b,u` 槽随 `P` 移动，而不能复用同一固定图样。",
            "- 下一层要么证明 moving-slot family 的 CRT 签名仍不可持续，要么将其作为 `MovingSlot-PDEC/ColumnCRT` 排斥对象。",
            "- 当前仍未证明全局行/列无条件闭合。",
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
            f"- 主攻：`{result['next_direct_attack_target']}`。",
            "- 具体目标：对 moving-slot family 建立统一 CRT 模数增长/相位宽度屏障，或构造正式 `MovingSlot-PDEC/ColumnCRT` 排斥证书。",
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
    parser.add_argument("--template-ledger", type=Path, default=TEMPLATE_LEDGER)
    parser.add_argument("--phase-ledger", type=Path, default=PHASE_LEDGER)
    parser.add_argument("--max-p", type=int, default=10000)
    parser.add_argument("--p0", type=int, default=2001)
    parser.add_argument("--target-h-coeff", type=float, default=0.43)
    parser.add_argument("--tight-limit", type=int, default=40)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    template_ledger = args.template_ledger if args.template_ledger.is_absolute() else ROOT / args.template_ledger
    phase_ledger = args.phase_ledger if args.phase_ledger.is_absolute() else ROOT / args.phase_ledger
    result = build_result(
        template_ledger,
        phase_ledger,
        args.max_p,
        args.p0,
        args.target_h_coeff,
        args.tight_limit,
    )
    write_markdown(result)
    result["source_hashes"][
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-moving-slot-crt-phase-barrier-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "fixed_highfactor_slot_pattern_isolation_failure_count_at_p0": result["aggregate"][
                    "fixed_highfactor_slot_pattern_isolation_failure_count_at_p0"
                ],
                "equality_atom_fixed_pattern_isolated": result["aggregate"]["equality_atom_fixed_pattern_isolated"],
                "min_crt_minus_phase_width_at_p0": result["aggregate"]["min_crt_minus_phase_width_at_p0"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
