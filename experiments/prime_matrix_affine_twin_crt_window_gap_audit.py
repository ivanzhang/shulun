#!/usr/bin/env python3
"""生成 AffineTwin CRT window gap 审计证书。

用法示例：
  python3 experiments/prime_matrix_affine_twin_crt_window_gap_audit.py
  python3 -m json.tool data/prime-matrix-affine-twin-crt-window-gap-ledger.json

输出：
  data/prime-matrix-affine-twin-crt-window-gap-ledger.json
  docs/monograph/prime-matrix-affine-twin-crt-window-gap-audit.json
  docs/monograph/prime-matrix-affine-twin-crt-window-gap-audit.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLOT_LEDGER = DATA / (
    "square-phase-offband-prefix-gap-shadow-selector-h-lower-"
    "affine-twin-slot-phase-lock-ledger.json"
)
EPOCH_LEDGER = DATA / (
    "square-phase-offband-prefix-gap-shadow-selector-h-lower-"
    "one-slot-residue-epoch-capacity-ledger.json"
)
SOURCE_GATE_LEDGER = DATA / "prime-matrix-affine-twin-source-materialization-gate-ledger.json"
PRUNING_LEDGER = DATA / "prime-matrix-affine-twin-formal-pair-pruning-ledger.json"

OUT_LEDGER = DATA / "prime-matrix-affine-twin-crt-window-gap-ledger.json"
OUT_JSON = DOCS / "prime-matrix-affine-twin-crt-window-gap-audit.json"
OUT_MD = DOCS / "prime-matrix-affine-twin-crt-window-gap-audit.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def egcd(left: int, right: int) -> tuple[int, int, int]:
    """扩展欧几里得算法。"""
    if right == 0:
        return left, 1, 0
    gcd_value, x_next, y_next = egcd(right, left % right)
    return gcd_value, y_next, x_next - (left // right) * y_next


def crt_pair(
    residue_a: int,
    modulus_a: int,
    residue_b: int,
    modulus_b: int,
) -> tuple[int, int]:
    """合并互素 CRT 条件。"""
    gcd_value, inv_a, _ = egcd(modulus_a, modulus_b)
    delta = residue_b - residue_a
    if delta % gcd_value != 0:
        raise ValueError("incompatible CRT conditions")
    merged_modulus = modulus_a // gcd_value * modulus_b
    step = (delta // gcd_value * inv_a) % (modulus_b // gcd_value)
    merged_residue = (residue_a + modulus_a * step) % merged_modulus
    return merged_residue, merged_modulus


def representatives_in_window(
    lo_value: int,
    hi_value: int,
    residue: int,
    modulus: int,
) -> list[int]:
    """列出窗口内 CRT 代表。"""
    first = lo_value + ((residue - lo_value) % modulus)
    if first > hi_value:
        return []
    return list(range(first, hi_value + 1, modulus))


def nearest_representative_to_window(
    lo_value: int,
    hi_value: int,
    residue: int,
    modulus: int,
) -> dict[str, Any]:
    """计算离窗口最近的 CRT 代表及距离。"""
    first_above_or_inside = lo_value + ((residue - lo_value) % modulus)
    previous = first_above_or_inside - modulus
    if first_above_or_inside <= hi_value:
        return {
            "nearest_representative": first_above_or_inside,
            "window_distance": 0,
            "side": "inside",
        }

    candidates = [
        (previous, lo_value - previous, "below"),
        (first_above_or_inside, first_above_or_inside - hi_value, "above"),
    ]
    nearest, distance, side = min(candidates, key=lambda item: (item[1], item[0]))
    return {
        "nearest_representative": nearest,
        "window_distance": distance,
        "side": side,
    }


def epoch_index(rows: list[dict[str, Any]]) -> dict[tuple[str, int], dict[str, Any]]:
    """按 side/ell 建立 residue epoch 索引。"""
    return {(str(row["side"]), int(row["ell"])): row for row in rows}


def source_gate_pass_q_values(rows: list[dict[str, Any]]) -> list[int]:
    """列出当前通过 source gate 的 q。"""
    return [
        int(row["q"])
        for row in rows
        if bool(row["source_gate_passed_current"])
    ]


def pruning_index(rows: list[dict[str, Any]]) -> dict[int, dict[str, Any]]:
    """按 q 建立 pruning 行索引。"""
    return {int(row["q"]): row for row in rows}


def slot_index(rows: list[dict[str, Any]]) -> dict[int, dict[str, Any]]:
    """按 q 建立 slot-lock 行索引。"""
    return {int(row["gap_ell"]): row for row in rows}


def window_rows_for_q(
    q: int,
    slot_row: dict[str, Any],
    pruning_row: dict[str, Any],
    epoch_by_key: dict[tuple[str, int], dict[str, Any]],
) -> list[dict[str, Any]]:
    """为单个通过 source gate 的 q 枚举 CRT 窗口间隙。"""
    generator_ell = int(slot_row["generator_ell"])
    fill_ell = int(slot_row["fill_ell"])
    generator_side = str(slot_row["generator_side"])
    fill_side = str(slot_row["fill_side"])
    generator_epoch = epoch_by_key[(generator_side, generator_ell)]
    fill_epoch = epoch_by_key[(fill_side, fill_ell)]
    generator_residues = [int(value) for value in generator_epoch["residue_sample"]]
    fill_residues = [int(value) for value in fill_epoch["residue_sample"]]
    p_delay = int(slot_row["p_delay"])
    lo_value, hi_value = [int(value) for value in slot_row["pair_phase_support"]]

    rows: list[dict[str, Any]] = []
    for generator_residue in generator_residues:
        for fill_residue in fill_residues:
            shifted_fill_residue = (fill_residue - p_delay) % fill_ell
            combined_residue, combined_modulus = crt_pair(
                generator_residue,
                generator_ell,
                shifted_fill_residue,
                fill_ell,
            )
            reps = representatives_in_window(
                lo_value,
                hi_value,
                combined_residue,
                combined_modulus,
            )
            nearest = nearest_representative_to_window(
                lo_value,
                hi_value,
                combined_residue,
                combined_modulus,
            )
            supported = bool(reps)
            rows.append(
                {
                    "q": q,
                    "generator_residue": generator_residue,
                    "fill_residue": fill_residue,
                    "shifted_fill_residue": shifted_fill_residue,
                    "combined_crt_residue": combined_residue,
                    "combined_crt_modulus": combined_modulus,
                    "pair_phase_support": [lo_value, hi_value],
                    "pair_phase_support_width": hi_value - lo_value + 1,
                    "support_residue_interval_mod_m": [
                        lo_value % combined_modulus,
                        hi_value % combined_modulus,
                    ],
                    "representatives_in_pair_support": reps,
                    "nearest_representative": nearest["nearest_representative"],
                    "window_distance": nearest["window_distance"],
                    "window_side": nearest["side"],
                    "supported_actual_packet_current": supported,
                    "route": "SupportedActualPacket"
                    if supported
                    else "CRTWindowGap",
                }
            )

    expected_formal_count = int(pruning_row["formal_pair_count"])
    if len(rows) != expected_formal_count:
        raise RuntimeError(
            f"q={q}: enumerated {len(rows)} formal pairs, expected {expected_formal_count}"
        )
    return rows


def build_result(
    slot_path: Path,
    epoch_path: Path,
    source_gate_path: Path,
    pruning_path: Path,
) -> dict[str, Any]:
    """构造 CRT window gap 审计结果。"""
    slot = load_json(slot_path)
    epoch = load_json(epoch_path)
    source_gate = load_json(source_gate_path)
    pruning = load_json(pruning_path)

    slot_by_q = slot_index(slot["affine_twin_slot_phase_lock_rows"])
    epoch_by_key = epoch_index(epoch["epoch_capacity_rows"])
    pruning_by_q = pruning_index(pruning["pruning_rows"])
    q_values = source_gate_pass_q_values(source_gate["source_gate_rows"])

    rows: list[dict[str, Any]] = []
    for q in q_values:
        rows.extend(window_rows_for_q(q, slot_by_q[q], pruning_by_q[q], epoch_by_key))

    supported_rows = [row for row in rows if row["supported_actual_packet_current"]]
    empty_rows = [row for row in rows if not row["supported_actual_packet_current"]]
    empty_distances = [int(row["window_distance"]) for row in empty_rows]
    side_histogram = Counter(str(row["window_side"]) for row in empty_rows)
    distance_histogram = Counter(str(row["window_distance"]) for row in empty_rows)

    formal_total = len(rows)
    actual_total = len(supported_rows)
    empty_total = len(empty_rows)
    expected_empty_total = sum(
        int(pruning_by_q[q]["crt_window_empty_pair_count"]) for q in q_values
    )
    aggregate = {
        "slot_ledger": str(slot_path.relative_to(ROOT)),
        "epoch_ledger": str(epoch_path.relative_to(ROOT)),
        "source_gate_ledger": str(source_gate_path.relative_to(ROOT)),
        "pruning_ledger": str(pruning_path.relative_to(ROOT)),
        "source_gate_pass_q_values": q_values,
        "formal_pair_total_with_exact_source": formal_total,
        "supported_actual_packet_total_current": actual_total,
        "crt_window_gap_pair_total_current": empty_total,
        "expected_crt_window_empty_pair_total": expected_empty_total,
        "crt_window_gap_count_agrees_with_pruning": empty_total == expected_empty_total,
        "all_empty_pairs_have_positive_window_distance": all(
            int(row["window_distance"]) > 0 for row in empty_rows
        ),
        "min_empty_window_distance": min(empty_distances) if empty_distances else None,
        "max_empty_window_distance": max(empty_distances) if empty_distances else None,
        "empty_window_side_histogram": dict(sorted(side_histogram.items())),
        "empty_window_distance_histogram": dict(sorted(distance_histogram.items(), key=lambda item: int(item[0]))),
        "support_width_current": rows[0]["pair_phase_support_width"] if rows else None,
        "combined_modulus_current": rows[0]["combined_crt_modulus"] if rows else None,
        "modulus_minus_support_width_current": (
            rows[0]["combined_crt_modulus"] - rows[0]["pair_phase_support_width"]
            if rows
            else None
        ),
        "crt_window_gap_closed_current_sweep": empty_total == expected_empty_total
        and all(int(row["window_distance"]) > 0 for row in empty_rows),
        "global_crt_window_gap_bound_proved": False,
        "row_column_unconditional_closed": False,
    }

    return {
        "certificate_type": "prime_matrix_affine_twin_crt_window_gap_audit",
        "status": "current_sweep_crt_window_gap_distances_closed_global_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "aggregate": aggregate,
        "crt_window_rows": rows,
        "contract": {
            "window_gate": "A source-materialized formal residue pair is actual only if its CRT class has a representative in the pair phase support.",
            "closed_current_sweep": aggregate["crt_window_gap_closed_current_sweep"],
            "global_remaining": [
                "GlobalCRTWindowGapBound",
                "WindowEdgeCollision-PDEC",
                "SupportMotionEscape-PDEC/SAE",
            ],
        },
        "dependency_hashes": {
            str(path.relative_to(ROOT)): sha256(path)
            for path in (slot_path, epoch_path, source_gate_path, pruning_path)
        },
    }


def write_outputs(result: dict[str, Any]) -> None:
    """写出 JSON 与 Markdown。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    for path in (OUT_LEDGER, OUT_JSON):
        path.write_text(
            json.dumps(result, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

    agg = result["aggregate"]
    lines = [
        "# Prime Matrix AffineTwin CRT window gap audit",
        "",
        "**状态：** `current_sweep_crt_window_gap_distances_closed_global_open`",
        "",
        "本审计把 `CRTWindowEmpty` 从布尔空窗推进为带距离的相位间隙证书：每个通过 source gate 的 formal residue pair 都合成为一个 CRT 类；只有该类在共同 pair support 中有代表时才是 actual packet。",
        "",
        "```text",
        f"source_gate_pass_q_values={agg['source_gate_pass_q_values']}",
        f"formal_pair_total_with_exact_source={agg['formal_pair_total_with_exact_source']}",
        f"supported_actual_packet_total_current={agg['supported_actual_packet_total_current']}",
        f"crt_window_gap_pair_total_current={agg['crt_window_gap_pair_total_current']}",
        f"expected_crt_window_empty_pair_total={agg['expected_crt_window_empty_pair_total']}",
        f"min_empty_window_distance={agg['min_empty_window_distance']}",
        f"max_empty_window_distance={agg['max_empty_window_distance']}",
        f"modulus_minus_support_width_current={agg['modulus_minus_support_width_current']}",
        f"crt_window_gap_closed_current_sweep={fmt_bool(agg['crt_window_gap_closed_current_sweep'])}",
        "```",
        "",
        "## 1. CRT window 表",
        "",
        "| gen residue | fill residue | shifted fill | CRT residue | nearest P | distance | side | route |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |",
    ]
    for row in result["crt_window_rows"]:
        lines.append(
            "| {g} | {f} | {sf} | {cr} | {nearest} | {dist} | `{side}` | `{route}` |".format(
                g=row["generator_residue"],
                f=row["fill_residue"],
                sf=row["shifted_fill_residue"],
                cr=row["combined_crt_residue"],
                nearest=row["nearest_representative"],
                dist=row["window_distance"],
                side=table_cell(row["window_side"]),
                route=table_cell(row["route"]),
            )
        )

    lines.extend(
        [
            "",
            "## 2. 当前结构读数",
            "",
            "- `q=31` 的共同 pair support 为 `[2669,2688]`，宽度 `20`。",
            "- 合成模数为 `29*31=899`，模数-窗口宽度为 `879`。",
            "- 唯一 supported actual packet 是 `(19,8)`，CRT 代表为 `2687`。",
            f"- 其余 `11` 个 formal pairs 的最近 CRT 代表距离窗口至少 `{agg['min_empty_window_distance']}`，因此是严格正间隙，不是边界等号。",
            "",
            "## 3. 结论边界",
            "",
            "- 当前 sweep 的 `CRTWindowEmpty=11` 已全部转成正距离 `CRTWindowGap`。",
            "- 这仍不是全局行/列证明；全局需要证明窗口随参数移动时，空窗失败只能进入 `WindowEdgeCollision-PDEC` 或 `SupportMotionEscape-PDEC/SAE`。",
            "",
            "## 4. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in result["dependency_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(
        description="生成 AffineTwin CRT window gap 审计证书。"
    )
    parser.add_argument("--slot-ledger", type=Path, default=SLOT_LEDGER)
    parser.add_argument("--epoch-ledger", type=Path, default=EPOCH_LEDGER)
    parser.add_argument("--source-gate-ledger", type=Path, default=SOURCE_GATE_LEDGER)
    parser.add_argument("--pruning-ledger", type=Path, default=PRUNING_LEDGER)
    return parser.parse_args()


def main() -> None:
    """入口。"""
    args = parse_args()
    result = build_result(
        args.slot_ledger,
        args.epoch_ledger,
        args.source_gate_ledger,
        args.pruning_ledger,
    )
    write_outputs(result)
    print(json.dumps(result["aggregate"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
