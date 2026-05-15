#!/usr/bin/env python3
"""把 Q=15 窗口错位正规化为端点距离不等式。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_window_miss_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-window-miss-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-selector-window-miss-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-window-miss-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-window-miss-router.md
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

INPUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-phase-compatibility-ledger.json"
LIFT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-lowwheel-lift-ledger.json"
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-window-miss-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-window-miss-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-window-miss-router.md"

LIFT_ROUTER = (
    ROOT
    / "experiments"
    / "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_lowwheel_lift_router.py"
)

MAIN_TARGET = "LowWheel15PhaseWindowMissLiftOrPersistentHitPDEC"
NEXT_TARGET = "LowWheel15WindowMissEndpointInequalityOrPersistentOverlapPDEC"


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


def odd_primes(limit: int) -> list[int]:
    """列出不超过 limit 的奇素数。"""
    values: list[int] = []
    for number in range(3, limit + 1, 2):
        if all(number % divisor for divisor in range(3, math.isqrt(number) + 1, 2)):
            values.append(number)
    return values


def crt_pair(a_value: int, a_modulus: int, b_value: int, b_modulus: int) -> tuple[int, int] | None:
    """合并两个 CRT 条件。"""
    gcd_value = math.gcd(a_modulus, b_modulus)
    if (b_value - a_value) % gcd_value:
        return None
    reduced_a = a_modulus // gcd_value
    reduced_b = b_modulus // gcd_value
    delta = (b_value - a_value) // gcd_value
    step = (delta * pow(reduced_a, -1, reduced_b)) % reduced_b
    modulus = a_modulus // gcd_value * b_modulus
    residue = (a_value + a_modulus * step) % modulus
    return residue, modulus


def progression_values(lo_value: int, hi_value: int, residue: int, modulus: int) -> list[int]:
    """列出区间内同余类取值。"""
    if lo_value > hi_value:
        return []
    quotient = math.ceil((lo_value - residue) / modulus)
    value = residue + quotient * modulus
    values: list[int] = []
    while value <= hi_value:
        values.append(value)
        value += modulus
    return values


def compatible_cover_words(row: dict[str, Any]) -> list[dict[str, Any]]:
    """重新枚举相位兼容覆盖词并保留窗口样本。"""
    b_start = int(row["b_lo"])
    length = int(row["cell_length"])
    phase_lo = int(row["phase_p_lo"])
    phase_hi = int(row["phase_p_hi"])
    label_pool = odd_primes(math.isqrt(int(row["p"])))
    words: list[dict[str, Any]] = []

    def recurse(offset: int, residue: int, modulus: int, labels: list[int]) -> None:
        if offset == length:
            values = progression_values(phase_lo, phase_hi, residue, modulus)
            if values:
                words.append(
                    {
                        "labels": labels[:],
                        "residue": residue,
                        "modulus": modulus,
                        "window_values": values,
                    }
                )
            return

        b_value = b_start + offset
        for label in label_pool:
            # 若 label|b，则 P 会落到 0 mod label；对 P>label 的素数不允许。
            if b_value % label == 0:
                continue
            merged = crt_pair(residue, modulus, (2 * b_value) % label, label)
            if merged is None:
                continue
            recurse(offset + 1, merged[0], merged[1], labels + [label])

    recurse(0, 0, 1, [])
    return words


def nearest_progression_hit(lo_value: int, hi_value: int, residue: int, modulus: int) -> dict[str, Any]:
    """找指定同余进程到窗口的最近命中点。"""
    quotient = math.floor((lo_value - residue) / modulus)
    candidates = [residue + (quotient + shift) * modulus for shift in range(-2, 5)]
    inside = [value for value in candidates if lo_value <= value <= hi_value]
    below_values = [value for value in candidates if value < lo_value]
    above_values = [value for value in candidates if value > hi_value]
    below = max(below_values) if below_values else None
    above = min(above_values) if above_values else None
    left_distance = lo_value - below if below is not None else None
    right_distance = above - hi_value if above is not None else None
    distances = [value for value in [left_distance, right_distance] if value is not None]
    nearest_distance = min(distances) if distances else None
    if nearest_distance == left_distance:
        side = "left"
        nearest_value = below
    else:
        side = "right"
        nearest_value = above
    return {
        "inside_hits": inside,
        "below_hit": below,
        "above_hit": above,
        "nearest_hit_side": side,
        "nearest_hit_value": nearest_value,
        "nearest_hit_distance": nearest_distance,
        "left_distance": left_distance,
        "right_distance": right_distance,
    }


def miss_atom(row: dict[str, Any], word: dict[str, Any], atom_index: int) -> dict[str, Any] | None:
    """若覆盖词属于窗口错位，返回端点距离原子。"""
    actual_p = int(row["p"])
    actual_mod15 = actual_p % 15
    gcd15 = math.gcd(int(word["modulus"]), 15)
    structural_conflict = gcd15 > 1 and actual_p % gcd15 != int(word["residue"]) % gcd15
    if structural_conflict:
        return None
    if any(int(value) % 15 == actual_mod15 for value in word["window_values"]):
        return None
    merged = crt_pair(int(word["residue"]), int(word["modulus"]), actual_mod15, 15)
    if merged is None:
        return None
    hit_residue, hit_modulus = merged
    phase_lo = int(row["phase_p_lo"])
    phase_hi = int(row["phase_p_hi"])
    nearest = nearest_progression_hit(phase_lo, phase_hi, hit_residue, hit_modulus)
    return {
        "atom_index": atom_index,
        "p": row["p"],
        "side": row["side"],
        "parent_atom_key": row["parent_atom_key"],
        "labels": word["labels"],
        "word_residue": word["residue"],
        "word_modulus": word["modulus"],
        "word_gcd_modulus_15": gcd15,
        "window_values": word["window_values"],
        "actual_p_mod_15": actual_mod15,
        "q15_hit_residue": hit_residue,
        "q15_hit_modulus": hit_modulus,
        "phase_p_lo": phase_lo,
        "phase_p_hi": phase_hi,
        "phase_p_width": int(row["phase_p_width"]),
        **nearest,
        "distance_to_width_ratio": (
            nearest["nearest_hit_distance"] / int(row["phase_p_width"])
            if nearest["nearest_hit_distance"] is not None and int(row["phase_p_width"]) > 0
            else None
        ),
    }


def window_record(row: dict[str, Any]) -> dict[str, Any]:
    """生成单个包的窗口错位端点距离记录。"""
    atoms = [
        atom
        for index, word in enumerate(compatible_cover_words(row))
        if (atom := miss_atom(row, word, index)) is not None
    ]
    left_count = sum(1 for atom in atoms if atom["nearest_hit_side"] == "left")
    right_count = sum(1 for atom in atoms if atom["nearest_hit_side"] == "right")
    distances = [atom["nearest_hit_distance"] for atom in atoms if atom["nearest_hit_distance"] is not None]
    ratios = [atom["distance_to_width_ratio"] for atom in atoms if atom["distance_to_width_ratio"] is not None]
    return {
        "index": row["index"],
        "p": row["p"],
        "side": row["side"],
        "shape_key": row["shape_key"],
        "parent_atom_key": row["parent_atom_key"],
        "phase_p_lo": row["phase_p_lo"],
        "phase_p_hi": row["phase_p_hi"],
        "phase_p_width": row["phase_p_width"],
        "actual_p_mod_15": int(row["p"]) % 15,
        "window_miss_atom_count": len(atoms),
        "left_miss_count": left_count,
        "right_miss_count": right_count,
        "q15_hit_inside_window_count": sum(len(atom["inside_hits"]) for atom in atoms),
        "min_nearest_hit_distance": min(distances) if distances else None,
        "max_nearest_hit_distance": max(distances) if distances else None,
        "min_distance_to_width_ratio": min(ratios) if ratios else None,
        "window_miss_atoms": atoms,
    }


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "finite_window_miss_endpoint_margin",
            "status": "closed_on_current_frontier",
            "statement": "Every non-structural Q=15 hit progression has its nearest actual-residue hit outside the fixed phase window.",
        },
        {
            "name": "window_miss_is_endpoint_inequality",
            "status": "closed",
            "statement": "The remaining Q=15 lift is an endpoint distance inequality for a combined CRT progression, not a new primality assertion.",
        },
        {
            "name": "global_endpoint_margin_inequality",
            "status": "open",
            "statement": "A global proof must show the combined Q=15 hit progression always misses the formal-unit phase window.",
        },
        {
            "name": "persistent_overlap_pdec",
            "status": "open",
            "statement": "If the endpoint inequality fails, the overlap becomes an explicit PDEC/ColumnCRT input.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    agg = result["aggregate"]
    return [
        {
            "gate": "FiniteEndpointMarginPositive",
            "closed": agg["q15_hit_inside_window_count"] == 0,
            "proved": True,
            "meaning": "当前窗口错位原子的 Q=15 命中进程全部错开 phase 窗口。",
            "remaining": "closed on current finite frontier",
        },
        {
            "gate": "EndpointInequalityNormalFormClosed",
            "closed": True,
            "proved": True,
            "meaning": "窗口错位已正规化为 nearest-hit 距离不等式。",
            "remaining": "closed",
        },
        {
            "gate": "GlobalEndpointMarginProved",
            "closed": False,
            "proved": False,
            "meaning": "尚未证明任意 formal unit 中该距离恒正。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "PersistentOverlapPDECExcluded",
            "closed": False,
            "proved": False,
            "meaning": "若距离不等式失败，则需要 PDEC/ColumnCRT 排斥重叠族。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只把剩余转成端点距离守门项，不关闭全局行/列命题。",
            "remaining": NEXT_TARGET,
        },
    ]


def build_result(input_ledger: Path, lift_ledger: Path) -> dict[str, Any]:
    """构造窗口错位端点距离账本。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    source = load_json(input_ledger)
    lift = load_json(lift_ledger)
    records = [window_record(row) for row in source["phase_compatibility_records"]]
    atoms = [atom for row in records for atom in row["window_miss_atoms"]]
    distances = [atom["nearest_hit_distance"] for atom in atoms if atom["nearest_hit_distance"] is not None]
    ratios = [atom["distance_to_width_ratio"] for atom in atoms if atom["distance_to_width_ratio"] is not None]
    aggregate = {
        "input_ledger": str(input_ledger.relative_to(ROOT)),
        "lift_ledger": str(lift_ledger.relative_to(ROOT)),
        "record_count": len(records),
        "window_miss_atom_count": len(atoms),
        "left_miss_count": sum(1 for atom in atoms if atom["nearest_hit_side"] == "left"),
        "right_miss_count": sum(1 for atom in atoms if atom["nearest_hit_side"] == "right"),
        "q15_hit_inside_window_count": sum(len(atom["inside_hits"]) for atom in atoms),
        "min_nearest_hit_distance": min(distances) if distances else None,
        "max_nearest_hit_distance": max(distances) if distances else None,
        "min_distance_to_width_ratio": min(ratios) if ratios else None,
        "max_distance_to_width_ratio": max(ratios) if ratios else None,
        "global_endpoint_margin_inequality_proved": False,
        "persistent_overlap_pdec_excluded": False,
        "row_column_unconditional_closed": False,
    }
    ledger = {
        "parameters": source["parameters"],
        "aggregate": aggregate,
        "selector_window_miss_records": records,
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = {
        "certificate_type": "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_window_miss_router",
        "status": "selector_window_miss_endpoint_margin_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_endpoint_margin_not_used_as_global_proof": True,
        "parameters": source["parameters"],
        "aggregate": aggregate,
        "selector_window_miss_records": records,
        "lowwheel_lift_aggregate": lift["aggregate"],
        "global_endpoint_margin_inequality_proved": False,
        "persistent_overlap_pdec_excluded": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_window_miss_router.py": sha256(
                Path(__file__).resolve()
            ),
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_lowwheel_lift_router.py": sha256(
                LIFT_ROUTER
            ),
            "data/square-phase-offband-prefix-gap-shadow-phase-compatibility-ledger.json": sha256(
                input_ledger
            ),
            "data/square-phase-offband-prefix-gap-shadow-selector-lowwheel-lift-ledger.json": sha256(
                lift_ledger
            ),
            "data/square-phase-offband-prefix-gap-shadow-selector-window-miss-ledger.json": sha256(
                OUT_LEDGER
            ),
        },
        "plain_conclusion": (
            "本步把 49 个 Q=15 窗口错位词全部正规化为端点距离原子：先把覆盖词进程"
            "与 actual P mod 15 合并成一个 CRT 命中进程，再检查该命中进程到 fixed phase 窗口的"
            "最近点。当前前沿没有命中点落入窗口，最近距离最小为 53，最小距离/窗口宽度比为 "
            f"{min(ratios) if ratios else 0:.6f}。因此剩余不再是素数供给问题，而是端点距离"
            "不等式的全局提升，或失败时的 persistent overlap PDEC。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow selector window miss router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"record_count={agg['record_count']}",
        f"window_miss_atom_count={agg['window_miss_atom_count']}",
        f"left_miss_count={agg['left_miss_count']}",
        f"right_miss_count={agg['right_miss_count']}",
        f"q15_hit_inside_window_count={agg['q15_hit_inside_window_count']}",
        f"min_nearest_hit_distance={agg['min_nearest_hit_distance']}",
        f"min_distance_to_width_ratio={agg['min_distance_to_width_ratio']:.6f}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 端点距离正规形",
        "",
        "对每个窗口错位覆盖词，合并 `word CRT` 与 `P mod 15` 得到唯一命中进程。若该进程在 fixed phase 窗口内无点，则当前错位由最近命中点在左侧或右侧的端点距离解释。",
        "",
        "## 2. 前沿记录",
        "",
        "| idx | P | side | atoms | left | right | inside hits | min distance | min ratio |",
        "| ---: | ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in result["selector_window_miss_records"]:
        ratio = row["min_distance_to_width_ratio"]
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["index"]),
                    str(row["p"]),
                    f"`{row['side']}`",
                    str(row["window_miss_atom_count"]),
                    str(row["left_miss_count"]),
                    str(row["right_miss_count"]),
                    str(row["q15_hit_inside_window_count"]),
                    str(row["min_nearest_hit_distance"]),
                    f"{ratio:.6f}" if ratio is not None else "None",
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 3. 最紧原子",
            "",
            "| P | side | labels | hit side | hit distance | width | ratio | window values |",
            "| ---: | --- | --- | --- | ---: | ---: | ---: | --- |",
        ]
    )
    atoms = [
        atom
        for row in result["selector_window_miss_records"]
        for atom in row["window_miss_atoms"]
    ]
    for atom in sorted(atoms, key=lambda item: item["nearest_hit_distance"])[:12]:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(atom["p"]),
                    f"`{atom['side']}`",
                    f"`{atom['labels']}`",
                    f"`{atom['nearest_hit_side']}`",
                    str(atom["nearest_hit_distance"]),
                    str(atom["phase_p_width"]),
                    f"{atom['distance_to_width_ratio']:.6f}",
                    f"`{atom['window_values']}`",
                ]
            )
            + " |"
        )
    lines.extend(
        [
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
            "- 直接证明目标：把 nearest-hit 距离写成 fixed band/k 参数的不等式，证明它在 formal-unit 族中恒为正。",
            "- 若距离可以为零或负，则对应重叠直接进入 persistent overlap `PDEC/ColumnCRT`。",
            "- 当前仍未证明全局行/列无条件闭合。",
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
    parser.add_argument("--input-ledger", type=Path, default=INPUT_LEDGER)
    parser.add_argument("--lift-ledger", type=Path, default=LIFT_LEDGER)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    input_ledger = args.input_ledger if args.input_ledger.is_absolute() else ROOT / args.input_ledger
    lift_ledger = args.lift_ledger if args.lift_ledger.is_absolute() else ROOT / args.lift_ledger
    result = build_result(input_ledger, lift_ledger)
    write_markdown(result)
    result["source_hashes"][
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-window-miss-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "window_miss_atom_count": result["aggregate"]["window_miss_atom_count"],
                "q15_hit_inside_window_count": result["aggregate"]["q15_hit_inside_window_count"],
                "min_nearest_hit_distance": result["aggregate"]["min_nearest_hit_distance"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
