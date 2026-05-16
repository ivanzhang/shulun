#!/usr/bin/env python3
"""把 AffineTwin 门继续压成双槽 CRT 相位锁。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_affine_twin_slot_phase_lock_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-slot-phase-lock-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-slot-phase-lock-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-slot-phase-lock-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-slot-phase-lock-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

AFFINE_TWIN_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-prime-gate-ledger.json"
PRIMITIVE_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-margin-slot-primitive-identity-ledger.json"
PAIR_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-gap-fill-pair-ledger.json"
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-slot-phase-lock-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-slot-phase-lock-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-slot-phase-lock-router.md"

NEXT_TARGET = "AffineTwinMovingFamilySAEOrColumnCRTExclusion"


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


def slot_residue(b_value: int, u_value: int, ell: int) -> int:
    """高因子槽给出的 P 同余残基。"""
    return (-2 * (b_value + u_value)) % ell


def slot_phase_interval(b_value: int, u_value: int, side: str) -> tuple[int, int]:
    """计算固定 b/u 槽保持同一欧几里得相位的整数 P 区间。"""
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
    return lower, upper


def representatives(lo_value: int, hi_value: int, residue: int, modulus: int) -> list[int]:
    """列出短区间中满足 CRT 残基的整数代表。"""
    if lo_value > hi_value:
        return []
    first = lo_value + ((residue - lo_value) % modulus)
    if first > hi_value:
        return []
    return list(range(first, hi_value + 1, modulus))


def indexed_rows(rows: list[dict[str, Any]]) -> dict[tuple[int, int, int], dict[str, Any]]:
    """按 gap/generator/fill 建立索引。"""
    return {
        (int(row["gap_ell"]), int(row["generator_ell"]), int(row["fill_ell"])): row
        for row in rows
    }


def pair_row(
    twin_row: dict[str, Any],
    primitive_by_key: dict[tuple[int, int, int], dict[str, Any]],
    pair_by_key: dict[tuple[int, int, int], dict[str, Any]],
) -> dict[str, Any]:
    """构造单个 AffineTwin 双槽相位锁记录。"""
    q = int(twin_row["gap_ell"])
    generator_ell = int(twin_row["generator_ell"])
    fill_ell = int(twin_row["fill_ell"])
    key = (q, generator_ell, fill_ell)
    primitive = primitive_by_key[key]
    pair = pair_by_key[key]

    generator_b = int(pair["generator_b"])
    generator_u = int(pair["generator_u"])
    fill_b = int(pair["fill_b"])
    fill_u = int(pair["fill_u"])
    generator_side = str(pair["generator_side"])
    fill_side = str(pair["fill_side"])
    generator_modulus = int(pair["generator_slot_ell"])
    fill_modulus = int(pair["fill_slot_ell"])

    generator_residue = slot_residue(generator_b, generator_u, generator_modulus)
    fill_residue = slot_residue(fill_b, fill_u, fill_modulus)
    generator_phase = slot_phase_interval(generator_b, generator_u, generator_side)
    fill_phase = slot_phase_interval(fill_b, fill_u, fill_side)

    generator_p = int(pair["generator_p"])
    fill_p = int(pair["fill_p"])
    p_delay = fill_p - generator_p
    shifted_fill_residue = (fill_residue - p_delay) % fill_modulus
    combined_residue, combined_modulus = crt_pair(
        generator_residue,
        generator_modulus,
        shifted_fill_residue,
        fill_modulus,
    )
    shifted_fill_phase = (fill_phase[0] - p_delay, fill_phase[1] - p_delay)
    pair_lo = max(generator_phase[0], shifted_fill_phase[0])
    pair_hi = min(generator_phase[1], shifted_fill_phase[1])
    pair_width = max(0, pair_hi - pair_lo + 1)
    pair_representatives = representatives(pair_lo, pair_hi, combined_residue, combined_modulus)

    gen_left, gen_right = map(int, pair["generator_depth"])
    fill_left, fill_right = map(int, pair["fill_depth"])
    symbolic_width = (q + 9) // 2
    symbolic_delay = (11 * q - 21) // 4
    symbolic_pair_modulus = q * (q - 2)
    return {
        "gap_ell": q,
        "generator_ell": generator_ell,
        "fill_ell": fill_ell,
        "generator_p": generator_p,
        "fill_p": fill_p,
        "p_delay": p_delay,
        "p_delay_affine_rhs": symbolic_delay,
        "p_delay_affine_identity": p_delay == symbolic_delay,
        "generator_slot": f"{generator_b}:{generator_u}:{generator_modulus}",
        "fill_slot": f"{fill_b}:{fill_u}:{fill_modulus}",
        "generator_side": generator_side,
        "fill_side": fill_side,
        "generator_modulus": generator_modulus,
        "fill_modulus": fill_modulus,
        "generator_modulus_is_q_minus_2": generator_modulus == q - 2,
        "fill_modulus_is_q": fill_modulus == q,
        "slot_moduli_are_coprime": egcd(generator_modulus, fill_modulus)[0] == 1,
        "generator_residue": generator_residue,
        "fill_residue": fill_residue,
        "shifted_fill_residue_for_generator_p": shifted_fill_residue,
        "slot_residues_match_pair_ledger": generator_residue == int(pair["generator_residue"])
        and fill_residue == int(pair["fill_residue"]),
        "generator_phase": list(generator_phase),
        "fill_phase": list(fill_phase),
        "shifted_fill_phase_for_generator_p": list(shifted_fill_phase),
        "pair_phase_support": [pair_lo, pair_hi],
        "pair_phase_support_width": pair_width,
        "pair_phase_support_width_affine_rhs": symbolic_width,
        "pair_phase_width_affine_identity": pair_width == symbolic_width,
        "generator_left_depth": gen_left,
        "generator_right_depth": gen_right,
        "fill_left_depth": fill_left,
        "fill_right_depth": fill_right,
        "generator_left_depth_affine_rhs": (q + 5) // 2,
        "generator_right_depth_affine_rhs": (q - 7) // 4,
        "fill_left_depth_affine_rhs": q - 3,
        "fill_right_depth_affine_rhs": 1,
        "depth_affine_identities_closed": gen_left == (q + 5) // 2
        and gen_right == (q - 7) // 4
        and fill_left == q - 3
        and fill_right == 1,
        "combined_crt_residue_for_generator_p": combined_residue,
        "combined_crt_modulus": combined_modulus,
        "combined_crt_modulus_affine_rhs": symbolic_pair_modulus,
        "combined_crt_modulus_affine_identity": combined_modulus == symbolic_pair_modulus,
        "combined_modulus_minus_pair_support_width": combined_modulus - pair_width,
        "combined_modulus_exceeds_pair_support_width": combined_modulus > pair_width,
        "pair_unique_representatives": pair_representatives,
        "actual_generator_p_is_unique_pair_representative": pair_representatives == [generator_p],
        "actual_fill_p_recovered_from_pair_representative": pair_representatives == [generator_p]
        and generator_p + p_delay == fill_p,
        "fixed_affine_twin_slot_pair_isolated": combined_modulus > pair_width
        and pair_representatives == [generator_p],
        "source_affine_twin_gate_key": str(twin_row["affine_twin_gate_key"]),
        "source_primitive_key": str(primitive["primitive_key"]),
        "source_gap_fill_pair_key": str(pair["gap_fill_pair_key"]),
    }


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "affine_twin_slot_pair_phase_lock",
            "status": "closed_current_atom",
            "statement": "In the current AffineTwin atom, generator and fill slots give coprime CRT conditions modulo q-2 and q; after shifting by the affine p-delay, their product modulus exceeds the common phase support.",
        },
        {
            "name": "fixed_affine_twin_slot_pair_isolation",
            "status": "closed",
            "statement": "For a fixed affine-twin slot pair satisfying the recorded primitive depth identities, q(q-2)>(q+9)/2 isolates at most one generator P in the pair support.",
        },
        {
            "name": "moving_affine_twin_family_exclusion",
            "status": "open",
            "statement": "A global proof must still exclude recurrence where q and the slot pair move with P, or route that family to SAE/ColumnCRT/PDEC.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    agg = result["aggregate"]
    return [
        {
            "gate": "AffineTwinSlotPhaseLockClosedCurrentAtom",
            "closed": agg["all_current_affine_twin_slot_pairs_isolated"],
            "proved": True,
            "meaning": "当前 AffineTwin 原子已由双槽 CRT/相位支撑判据孤立。",
            "remaining": "closed for fixed atom",
        },
        {
            "gate": "FixedAffineTwinSlotPairIsolationCriterionClosed",
            "closed": True,
            "proved": True,
            "meaning": "`q(q-2)>(q+9)/2` 给出固定仿射双槽图样唯一代表判据。",
            "remaining": "closed",
        },
        {
            "gate": "MovingAffineTwinFamilyExcluded",
            "closed": False,
            "proved": False,
            "meaning": "q 与槽图样随 P 移动的族尚未全局排斥。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步关闭固定双槽原子，不关闭全局行/列命题。",
            "remaining": NEXT_TARGET,
        },
    ]


def build_result(affine_twin_ledger: Path, primitive_ledger: Path, pair_ledger: Path) -> dict[str, Any]:
    """构造 AffineTwin 双槽相位锁结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    affine_twin = load_json(affine_twin_ledger)
    primitive = load_json(primitive_ledger)
    pair = load_json(pair_ledger)
    primitive_by_key = indexed_rows(primitive["primitive_rows"])
    pair_by_key = indexed_rows(pair["gap_fill_pair_rows"])
    rows = [
        pair_row(row, primitive_by_key, pair_by_key)
        for row in affine_twin["affine_twin_gate_rows"]
    ]
    aggregate = {
        "affine_twin_ledger": str(affine_twin_ledger.relative_to(ROOT)),
        "primitive_ledger": str(primitive_ledger.relative_to(ROOT)),
        "pair_ledger": str(pair_ledger.relative_to(ROOT)),
        "affine_twin_slot_phase_lock_row_count": len(rows),
        "all_generator_fill_slots_are_twin_moduli": all(
            row["generator_modulus_is_q_minus_2"] and row["fill_modulus_is_q"]
            for row in rows
        ),
        "all_slot_moduli_are_coprime": all(row["slot_moduli_are_coprime"] for row in rows),
        "all_slot_residues_match_pair_ledger": all(row["slot_residues_match_pair_ledger"] for row in rows),
        "all_pair_delay_affine_identities_closed": all(row["p_delay_affine_identity"] for row in rows),
        "all_depth_affine_identities_closed": all(row["depth_affine_identities_closed"] for row in rows),
        "all_pair_phase_width_affine_identities_closed": all(
            row["pair_phase_width_affine_identity"] for row in rows
        ),
        "all_combined_crt_modulus_affine_identities_closed": all(
            row["combined_crt_modulus_affine_identity"] for row in rows
        ),
        "all_combined_moduli_exceed_pair_support_width": all(
            row["combined_modulus_exceeds_pair_support_width"] for row in rows
        ),
        "all_current_affine_twin_slot_pairs_isolated": all(
            row["fixed_affine_twin_slot_pair_isolated"] for row in rows
        ),
        "min_combined_modulus_minus_pair_support_width": min(
            row["combined_modulus_minus_pair_support_width"] for row in rows
        )
        if rows
        else None,
        "fixed_affine_twin_slot_pair_isolation_criterion_proved": True,
        "moving_affine_twin_family_excluded": False,
        "row_column_unconditional_closed": False,
    }
    ledger = {
        "aggregate": aggregate,
        "affine_twin_slot_phase_lock_rows": rows,
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = {
        "certificate_type": (
            "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_"
            "affine_twin_slot_phase_lock_router"
        ),
        "status": "affine_twin_fixed_slot_pair_isolated_moving_family_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_sweep_not_used_as_global_proof": True,
        "aggregate": aggregate,
        "affine_twin_slot_phase_lock_rows": rows,
        "fixed_affine_twin_slot_pair_isolation_criterion_proved": True,
        "moving_affine_twin_family_excluded": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": "AffineTwinPrimeGateBoundOrAffineTwinPDECExclusion",
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "plain_conclusion": (
            "本步把 AffineTwin 门继续接入 slot-depth/CRT 相位锁：生成槽给出 "
            "`P≡a_g (mod q-2)`，修补槽在平移 `p_delay` 后给出 "
            "`P≡a_f-p_delay (mod q)`。两模互素，合成模数为 `q(q-2)`；"
            "primitive 深度身份把共同相位支撑压成 `(q+9)/2`。当前 `q=31` 时 "
            "`29*31=899 > 20`，唯一代表为 `P=2687`，并恢复 `P+80=2767`。"
            "因此固定 AffineTwin 双槽原子已孤立；全局剩余是排斥 q/槽随 P 移动的族，"
            "或将其作为 SAE/ColumnCRT/PDEC 终端证书处理。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    result["source_hashes"] = {
        "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_affine_twin_slot_phase_lock_router.py": sha256(
            Path(__file__).resolve()
        ),
        "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-prime-gate-ledger.json": sha256(
            affine_twin_ledger
        ),
        "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-margin-slot-primitive-identity-ledger.json": sha256(
            primitive_ledger
        ),
        "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-gap-fill-pair-ledger.json": sha256(
            pair_ledger
        ),
        "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-slot-phase-lock-ledger.json": sha256(
            OUT_LEDGER
        ),
    }
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow selector H lower affine twin slot phase lock router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"affine_twin_slot_phase_lock_row_count={agg['affine_twin_slot_phase_lock_row_count']}",
        f"all_generator_fill_slots_are_twin_moduli={fmt_bool(agg['all_generator_fill_slots_are_twin_moduli'])}",
        f"all_pair_delay_affine_identities_closed={fmt_bool(agg['all_pair_delay_affine_identities_closed'])}",
        f"all_pair_phase_width_affine_identities_closed={fmt_bool(agg['all_pair_phase_width_affine_identities_closed'])}",
        f"all_combined_moduli_exceed_pair_support_width={fmt_bool(agg['all_combined_moduli_exceed_pair_support_width'])}",
        f"all_current_affine_twin_slot_pairs_isolated={fmt_bool(agg['all_current_affine_twin_slot_pairs_isolated'])}",
        f"min_combined_modulus_minus_pair_support_width={agg['min_combined_modulus_minus_pair_support_width']}",
        f"moving_affine_twin_family_excluded={fmt_bool(agg['moving_affine_twin_family_excluded'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 双槽相位锁",
        "",
        "| q | slots | p delay | pair support | CRT conditions | CRT modulus | margin | representative | isolated |",
        "| ---: | --- | ---: | --- | --- | ---: | ---: | --- | ---: |",
    ]
    for row in result["affine_twin_slot_phase_lock_rows"]:
        conditions = (
            f"P={row['generator_residue']} mod {row['generator_modulus']}; "
            f"P={row['shifted_fill_residue_for_generator_p']} mod {row['fill_modulus']}"
        )
        lines.append(
            f"| {row['gap_ell']} | `{row['generator_slot']} -> {row['fill_slot']}` | "
            f"{row['p_delay']} | `{row['pair_phase_support']}` | `{conditions}` | "
            f"{row['combined_crt_modulus']} | {row['combined_modulus_minus_pair_support_width']} | "
            f"`{row['pair_unique_representatives']}` | "
            f"`{fmt_bool(row['fixed_affine_twin_slot_pair_isolated'])}` |"
        )
    lines.extend(
        [
            "",
            "## 2. 闭合身份",
            "",
            "- `generator_modulus=q-2` 且 `fill_modulus=q`。",
            "- `p_delay=(11q-21)/4`。",
            "- `generator_left=(q+5)/2`、`generator_right=(q-7)/4`、`fill_left=q-3`、`fill_right=1`。",
            "- 双槽共同支撑宽度为 `(q+9)/2`。",
            "- 合成 CRT 模数为 `q(q-2)`，因此固定双槽图样满足 `q(q-2)>(q+9)/2`。",
            "",
            "## 3. 结构判断",
            "",
            "- 这一步不是证明或调用全局孪生素数命题；`q,q-2` 只是当前失败原子的必要门。",
            "- 当前固定 AffineTwin 双槽原子已由 CRT 模数超过相位支撑宽度而孤立。",
            "- 若反例链要持久复现，必须让 `q` 和槽图样一起移动；这已经是更窄的 `AffineTwinMovingFamily` 终端。",
            "- 当前仍未证明全局行/列无条件闭合。",
            "",
            "## 4. 命题行",
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
            "## 5. 决策表",
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
            "## 6. 下一步",
            "",
            f"- 主攻：`{result['next_direct_attack_target']}`。",
            "- 具体目标：把移动 `q`/移动槽族分流为可求和 SAE 或固定/移动模 ColumnCRT-PDEC，并证明其不能承载反例链。",
            "",
            "## 7. 依赖哈希",
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
    parser.add_argument("--affine-twin-ledger", type=Path, default=AFFINE_TWIN_LEDGER)
    parser.add_argument("--primitive-ledger", type=Path, default=PRIMITIVE_LEDGER)
    parser.add_argument("--pair-ledger", type=Path, default=PAIR_LEDGER)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    affine_twin_ledger = args.affine_twin_ledger if args.affine_twin_ledger.is_absolute() else ROOT / args.affine_twin_ledger
    primitive_ledger = args.primitive_ledger if args.primitive_ledger.is_absolute() else ROOT / args.primitive_ledger
    pair_ledger = args.pair_ledger if args.pair_ledger.is_absolute() else ROOT / args.pair_ledger
    result = build_result(affine_twin_ledger, primitive_ledger, pair_ledger)
    write_markdown(result)
    result["source_hashes"][
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-slot-phase-lock-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "affine_twin_slot_phase_lock_row_count": result["aggregate"][
                    "affine_twin_slot_phase_lock_row_count"
                ],
                "all_current_affine_twin_slot_pairs_isolated": result["aggregate"][
                    "all_current_affine_twin_slot_pairs_isolated"
                ],
                "min_combined_modulus_minus_pair_support_width": result["aggregate"][
                    "min_combined_modulus_minus_pair_support_width"
                ],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
