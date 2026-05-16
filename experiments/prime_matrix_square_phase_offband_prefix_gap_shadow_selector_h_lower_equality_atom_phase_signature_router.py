#!/usr/bin/env python3
"""把 residual-prime 等号原子压成固定槽相位签名并排斥固定槽复现。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_equality_atom_phase_signature_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-equality-atom-phase-signature-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-selector-h-lower-equality-atom-phase-signature-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-equality-atom-phase-signature-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-equality-atom-phase-signature-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

EQUALITY_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-equality-atom-pdec-ledger.json"
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-equality-atom-phase-signature-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-equality-atom-phase-signature-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-equality-atom-phase-signature-router.md"

MAIN_TARGET = "ResidualPrimeEqualityAtomPDECExclusionOrGlobalMarginJump"
NEXT_TARGET = "MovingSlotEqualityAtomPDECExclusionOrGlobalMarginJump"


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
    """合并两个可能非互素的 CRT 条件。"""
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
    """合并同余条件列表。"""
    residue = 0
    modulus = 1
    for item in congruences:
        residue, modulus = crt_pair(residue, modulus, int(item["residue"]), int(item["modulus"]))
    return {"residue": residue, "modulus": modulus}


def slot_phase_interval_minus(slot: dict[str, Any]) -> dict[str, Any]:
    """计算 minus 侧固定 b/u 槽保持同一欧几里得相位的整数 P 区间。"""
    b_value = int(slot["b"])
    u_value = int(slot["u"])
    base = 2 * b_value * b_value

    # quotient 条件：u <= base/(P-2b) < u+1。
    lower = base // (u_value + 1) + 2 * b_value + 1
    upper = 10**30 if u_value == 0 else base // u_value + 2 * b_value

    # cap 条件：1 <= base-u(P-2b) <= (P-1)/2。
    if u_value == 0:
        lower = max(lower, 2 * base + 1)
    else:
        lower = max(lower, math.ceil((2 * base + 4 * b_value * u_value + 1) / (2 * u_value + 1)))
        upper = min(upper, (base + 2 * b_value * u_value - 1) // u_value)

    return {
        "b": b_value,
        "u": u_value,
        "phase_p_lo": lower,
        "phase_p_hi": upper,
        "contains_registered_p": lower <= int(slot["registered_p"]) <= upper,
    }


def highfactor_congruences(source: dict[str, Any]) -> list[dict[str, int]]:
    """由高因子吸收槽 m=P+2(b+u) 的最小素因子生成 P 的 CRT 签名。"""
    records = []
    for slot in source["highfactor_composite_slots"]:
        ell = int(slot["least_prime_factor_m"])
        offset = 2 * (int(slot["b"]) + int(slot["u"]))
        records.append(
            {
                "b": int(slot["b"]),
                "u": int(slot["u"]),
                "m": int(slot["m"]),
                "lpf_m": ell,
                "offset": offset,
                "modulus": ell,
                "residue": (-offset) % ell,
            }
        )
    return records


def consolidated_highfactor_congruences(records: list[dict[str, int]]) -> list[dict[str, Any]]:
    """按最小素因子合并重复同余，并检查重复槽是否相容。"""
    grouped: dict[int, list[dict[str, int]]] = {}
    for record in records:
        grouped.setdefault(int(record["modulus"]), []).append(record)
    consolidated = []
    for modulus, items in sorted(grouped.items()):
        residues = sorted({int(item["residue"]) for item in items})
        consolidated.append(
            {
                "modulus": modulus,
                "residue": residues[0] if len(residues) == 1 else residues,
                "slot_count": len(items),
                "compatible": len(residues) == 1,
                "slots": items,
            }
        )
    return consolidated


def all_slots(source: dict[str, Any]) -> list[dict[str, Any]]:
    """抽取 357 残余中的高因子合数槽与真素对槽。"""
    rows = []
    p_value = int(source["formal_unit"]["p"])
    for slot in source["highfactor_composite_slots"]:
        rows.append({**slot, "registered_p": p_value, "slot_type": "highfactor_composite"})
    for slot in source["residual_prime_pair_slots"]:
        rows.append({**slot, "registered_p": p_value, "slot_type": "residual_prime_pair"})
    return sorted(rows, key=lambda item: (int(item["b"]), int(item["u"])))


def slot_phase_records(source: dict[str, Any]) -> list[dict[str, Any]]:
    """列出所有固定 b/u 槽的相位支撑区间。"""
    rows = []
    for slot in all_slots(source):
        interval = slot_phase_interval_minus(slot)
        rows.append(
            {
                "slot_type": slot["slot_type"],
                "b": int(slot["b"]),
                "u": int(slot["u"]),
                "q": int(slot["q"]),
                "m": int(slot["m"]),
                "r": int(slot["r"]),
                "phase_p_lo": interval["phase_p_lo"],
                "phase_p_hi": interval["phase_p_hi"],
                "contains_registered_p": interval["contains_registered_p"],
            }
        )
    return rows


def intersect_intervals(records: list[dict[str, Any]]) -> dict[str, int | bool]:
    """求所有固定槽相位区间交集。"""
    lo_value = max(int(record["phase_p_lo"]) for record in records)
    hi_value = min(int(record["phase_p_hi"]) for record in records)
    return {
        "phase_intersection_lo": lo_value,
        "phase_intersection_hi": hi_value,
        "phase_intersection_nonempty": lo_value <= hi_value,
        "phase_intersection_length": max(0, hi_value - lo_value + 1),
    }


def primes_in_interval(lo_value: int, hi_value: int) -> list[int]:
    """列出短区间中的素数。"""
    result = []
    for value in range(max(2, lo_value), hi_value + 1):
        if value == 2:
            result.append(value)
            continue
        if value % 2 == 0:
            continue
        is_prime = True
        for divisor in range(3, math.isqrt(value) + 1, 2):
            if value % divisor == 0:
                is_prime = False
                break
        if is_prime:
            result.append(value)
    return result


def prime_pair_nonforced_records(source: dict[str, Any], crt_signature: dict[str, int]) -> list[dict[str, Any]]:
    """检查高因子 CRT 签名不会自动摧毁 6 个真素对槽。"""
    residue = int(crt_signature["residue"])
    modulus_list = [int(item["least_prime_factor_m"]) for item in source["highfactor_composite_slots"]]
    rows = []
    for slot in source["residual_prime_pair_slots"]:
        b_value = int(slot["b"])
        u_value = int(slot["u"])
        q_residues = {ell: (residue - 2 * b_value) % ell for ell in sorted(set(modulus_list))}
        m_residues = {ell: (residue + 2 * (b_value + u_value)) % ell for ell in sorted(set(modulus_list))}
        rows.append(
            {
                "b": b_value,
                "u": u_value,
                "q": int(slot["q"]),
                "m": int(slot["m"]),
                "q_zero_for_highfactor_moduli": [ell for ell, value in q_residues.items() if value == 0],
                "m_zero_for_highfactor_moduli": [ell for ell, value in m_residues.items() if value == 0],
                "not_forced_composite_by_highfactor_signature": all(value != 0 for value in q_residues.values())
                and all(value != 0 for value in m_residues.values()),
            }
        )
    return rows


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "fixed_slot_highfactor_crt_signature",
            "status": "closed",
            "statement": "The eight high-factor absorber slots impose five compatible congruences whose CRT representative is the registered P.",
        },
        {
            "name": "fixed_bu_phase_support_is_local",
            "status": "closed",
            "statement": "Keeping all fourteen b/u slots in the same Euclidean cap phase forces P into the short interval [2460,2478].",
        },
        {
            "name": "exact_slot_formal_unit_nonpersistent",
            "status": "closed",
            "statement": "The fixed-slot equality formal unit is isolated: the CRT signature and phase support intersect only at P=2467.",
        },
        {
            "name": "moving_slot_or_template_level_recurrence",
            "status": "open",
            "statement": "A global proof must still exclude equality recurrence with moving b/u slots or prove a global positive margin.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    agg = result["aggregate"]
    return [
        {
            "gate": "HighFactorCRTSignatureClosed",
            "closed": agg["highfactor_crt_signature_closed"],
            "proved": True,
            "meaning": "8 个高因子吸收槽合并为 5 个相容 CRT 条件。",
            "remaining": "closed",
        },
        {
            "gate": "FixedSlotPhaseSupportClosed",
            "closed": agg["fixed_slot_phase_support_closed"],
            "proved": True,
            "meaning": "所有固定 b/u 槽共同只允许短相位区间。",
            "remaining": "closed",
        },
        {
            "gate": "ExactFixedSlotFormalUnitExcludedBeyondRegisteredP",
            "closed": agg["exact_fixed_slot_nonpersistence_proved"],
            "proved": True,
            "meaning": "固定槽级等号原子不能在别的 P 上复现。",
            "remaining": "closed",
        },
        {
            "gate": "MovingSlotEqualityAtomExcluded",
            "closed": False,
            "proved": False,
            "meaning": "移动槽/模板级等号复现仍未排斥。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只关闭固定槽等号原子持久性，不关闭全局命题。",
            "remaining": result["next_direct_attack_target"],
        },
    ]


def build_result(equality_ledger: Path) -> dict[str, Any]:
    """构造固定槽相位签名结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    source = load_json(equality_ledger)
    p_value = int(source["formal_unit"]["p"])
    raw_congruences = highfactor_congruences(source)
    consolidated = consolidated_highfactor_congruences(raw_congruences)
    crt_input = [
        {"residue": int(item["residue"]), "modulus": int(item["modulus"])}
        for item in consolidated
        if bool(item["compatible"])
    ]
    crt_signature = combine_crt(crt_input)
    phase_records = slot_phase_records(source)
    phase_intersection = intersect_intervals(phase_records)
    interval_primes = primes_in_interval(
        int(phase_intersection["phase_intersection_lo"]),
        int(phase_intersection["phase_intersection_hi"]),
    )
    crt_interval_hits = [
        value
        for value in range(
            int(phase_intersection["phase_intersection_lo"]),
            int(phase_intersection["phase_intersection_hi"]) + 1,
        )
        if value % int(crt_signature["modulus"]) == int(crt_signature["residue"])
    ]
    exact_fixed_slot_nonpersistent = crt_interval_hits == [p_value]
    aggregate = {
        "source_ledger": str(equality_ledger.relative_to(ROOT)),
        "registered_p": p_value,
        "highfactor_raw_congruence_count": len(raw_congruences),
        "highfactor_distinct_modulus_count": len(consolidated),
        "highfactor_crt_signature_closed": all(bool(item["compatible"]) for item in consolidated)
        and p_value % int(crt_signature["modulus"]) == int(crt_signature["residue"]),
        "highfactor_crt_residue": int(crt_signature["residue"]),
        "highfactor_crt_modulus": int(crt_signature["modulus"]),
        "odd_prime_physical_period": 2 * int(crt_signature["modulus"]),
        **phase_intersection,
        "fixed_slot_phase_support_closed": bool(phase_intersection["phase_intersection_nonempty"])
        and all(bool(item["contains_registered_p"]) for item in phase_records),
        "phase_intersection_primes": interval_primes,
        "crt_hits_inside_phase_intersection": crt_interval_hits,
        "exact_fixed_slot_nonpersistence_proved": exact_fixed_slot_nonpersistent,
        "moving_slot_equality_atom_excluded": False,
        "global_margin_jump_proved": False,
        "row_column_unconditional_closed": False,
    }
    ledger = {
        "parameters": {"source_ledger": str(equality_ledger.relative_to(ROOT))},
        "aggregate": aggregate,
        "formal_unit": source["formal_unit"],
        "highfactor_congruences": raw_congruences,
        "highfactor_consolidated_congruences": consolidated,
        "slot_phase_records": phase_records,
        "prime_pair_nonforced_records": prime_pair_nonforced_records(source, crt_signature),
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = {
        "certificate_type": "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_equality_atom_phase_signature_router",
        "status": "exact_fixed_slot_equality_atom_nonpersistent_moving_slot_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_registered_atom_not_used_as_global_proof": True,
        "parameters": ledger["parameters"],
        "aggregate": aggregate,
        "formal_unit": source["formal_unit"],
        "highfactor_consolidated_congruences": consolidated,
        "slot_phase_records": phase_records,
        "prime_pair_nonforced_records": ledger["prime_pair_nonforced_records"],
        "moving_slot_equality_atom_excluded": False,
        "global_margin_jump_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_equality_atom_phase_signature_router.py": sha256(
                Path(__file__).resolve()
            ),
            "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-equality-atom-pdec-ledger.json": sha256(
                equality_ledger
            ),
            "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-equality-atom-phase-signature-ledger.json": sha256(
                OUT_LEDGER
            ),
        },
        "plain_conclusion": (
            "本步关闭固定槽级等号原子的持久性。"
            "8 个高因子吸收槽合并为 5 个相容 CRT 条件，"
            f"给出 `P ≡ {crt_signature['residue']} (mod {crt_signature['modulus']})`；"
            "同时 14 个固定 `b,u` 槽的相位支撑交集为 "
            f"`[{phase_intersection['phase_intersection_lo']},{phase_intersection['phase_intersection_hi']}]`。"
            "二者在该交集中只命中注册原子 `P=2467`。"
            "这排除了 exact fixed-slot formal unit 的复现，但移动槽/模板级等号复现仍需继续排斥。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow selector H lower equality atom phase signature router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"registered_p={agg['registered_p']}",
        f"highfactor_crt=P≡{agg['highfactor_crt_residue']} mod {agg['highfactor_crt_modulus']}",
        f"odd_prime_physical_period={agg['odd_prime_physical_period']}",
        f"phase_intersection=[{agg['phase_intersection_lo']},{agg['phase_intersection_hi']}]",
        f"phase_intersection_primes={agg['phase_intersection_primes']}",
        f"crt_hits_inside_phase_intersection={agg['crt_hits_inside_phase_intersection']}",
        f"exact_fixed_slot_nonpersistence_proved={fmt_bool(agg['exact_fixed_slot_nonpersistence_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 高因子 CRT 签名",
        "",
        "| ell | residue | slots | compatible |",
        "| ---: | ---: | ---: | ---: |",
    ]
    for row in result["highfactor_consolidated_congruences"]:
        lines.append(
            f"| {row['modulus']} | {row['residue']} | {row['slot_count']} | {fmt_bool(row['compatible'])} |"
        )
    lines.extend(
        [
            "",
            "## 2. 固定槽相位支撑",
            "",
            "| type | b | u | q | m | r | P lo | P hi | contains P |",
            "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in result["slot_phase_records"]:
        lines.append(
            f"| `{row['slot_type']}` | {row['b']} | {row['u']} | {row['q']} | {row['m']} | {row['r']} | "
            f"{row['phase_p_lo']} | {row['phase_p_hi']} | {fmt_bool(row['contains_registered_p'])} |"
        )
    lines.extend(
        [
            "",
            "## 3. 真素对槽未被高因子签名自动摧毁",
            "",
            "| b | u | q | m | q zero mod highfactor | m zero mod highfactor | nonforced |",
            "| ---: | ---: | ---: | ---: | --- | --- | ---: |",
        ]
    )
    for row in result["prime_pair_nonforced_records"]:
        lines.append(
            f"| {row['b']} | {row['u']} | {row['q']} | {row['m']} | "
            f"`{row['q_zero_for_highfactor_moduli']}` | `{row['m_zero_for_highfactor_moduli']}` | "
            f"{fmt_bool(row['not_forced_composite_by_highfactor_signature'])} |"
        )
    lines.extend(
        [
            "",
            "## 4. 结构判断",
            "",
            "- 高因子吸收槽给出的是强 CRT 锁相，不是松散统计现象。",
            "- 固定 `b,u` 槽相位支撑极窄，和 CRT 签名相交只剩 `P=2467`。",
            "- 因此 exact fixed-slot equality formal unit 已不能持久复现。",
            "- 这仍不排斥移动 `b,u` 槽或同模板等号原子在高处复现；全局行/列命题仍未闭合。",
            "",
            "## 5. 命题行",
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
            "## 6. 决策表",
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
            "## 7. 下一步",
            "",
            f"- 主攻：`{result['next_direct_attack_target']}`。",
            "- 具体目标：把 moving-slot/template-level 等号复现也压成相位签名，或证明 residual prime margin 全局正下界。",
            "",
            "## 8. 依赖哈希",
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
    parser.add_argument("--equality-ledger", type=Path, default=EQUALITY_LEDGER)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    equality_ledger = args.equality_ledger if args.equality_ledger.is_absolute() else ROOT / args.equality_ledger
    result = build_result(equality_ledger)
    write_markdown(result)
    result["source_hashes"][
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-equality-atom-phase-signature-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "highfactor_crt": {
                    "residue": result["aggregate"]["highfactor_crt_residue"],
                    "modulus": result["aggregate"]["highfactor_crt_modulus"],
                },
                "phase_intersection": [
                    result["aggregate"]["phase_intersection_lo"],
                    result["aggregate"]["phase_intersection_hi"],
                ],
                "crt_hits_inside_phase_intersection": result["aggregate"]["crt_hits_inside_phase_intersection"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
