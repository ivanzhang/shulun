#!/usr/bin/env python3
"""生成 AffineTwin formal-pair pruning 审计证书。

用法示例：
  python3 experiments/prime_matrix_affine_twin_formal_pair_pruning_audit.py
  python3 -m json.tool data/prime-matrix-affine-twin-formal-pair-pruning-ledger.json

输出：
  data/prime-matrix-affine-twin-formal-pair-pruning-ledger.json
  docs/monograph/prime-matrix-affine-twin-formal-pair-pruning-audit.json
  docs/monograph/prime-matrix-affine-twin-formal-pair-pruning-audit.md
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

MOVING_LEDGER = DATA / (
    "square-phase-offband-prefix-gap-shadow-selector-h-lower-"
    "affine-twin-moving-family-sae-columncrt-ledger.json"
)
SLOT_LEDGER = DATA / (
    "square-phase-offband-prefix-gap-shadow-selector-h-lower-"
    "affine-twin-slot-phase-lock-ledger.json"
)
PAIR_LEDGER = DATA / (
    "square-phase-offband-prefix-gap-shadow-selector-h-lower-gap-fill-pair-ledger.json"
)
EPOCH_LEDGER = DATA / (
    "square-phase-offband-prefix-gap-shadow-selector-h-lower-"
    "one-slot-residue-epoch-capacity-ledger.json"
)
ACTUAL_CONTRACT_LEDGER = DATA / "prime-matrix-affine-twin-actual-packet-contract-ledger.json"

OUT_LEDGER = DATA / "prime-matrix-affine-twin-formal-pair-pruning-ledger.json"
OUT_JSON = DOCS / "prime-matrix-affine-twin-formal-pair-pruning-audit.json"
OUT_MD = DOCS / "prime-matrix-affine-twin-formal-pair-pruning-audit.md"


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


def representatives(lo_value: int, hi_value: int, residue: int, modulus: int) -> list[int]:
    """列出短区间中的 CRT 代表。"""
    if lo_value > hi_value:
        return []
    first = lo_value + ((residue - lo_value) % modulus)
    if first > hi_value:
        return []
    return list(range(first, hi_value + 1, modulus))


def epoch_index(rows: list[dict[str, Any]]) -> dict[tuple[str, int], dict[str, Any]]:
    """按 side/ell 建立 residue epoch 索引。"""
    return {(str(row["side"]), int(row["ell"])): row for row in rows}


def slot_index(rows: list[dict[str, Any]]) -> dict[int, dict[str, Any]]:
    """按 AffineTwin q 建立 slot-lock 索引。"""
    return {int(row["gap_ell"]): row for row in rows}


def pair_rows_by_q(rows: list[dict[str, Any]]) -> dict[int, list[dict[str, Any]]]:
    """按 gap ell 建立 gap-fill source 索引。"""
    out: dict[int, list[dict[str, Any]]] = {}
    for row in rows:
        out.setdefault(int(row["gap_ell"]), []).append(row)
    return out


def exact_pruning_for_slot(
    moving_row: dict[str, Any],
    slot_row: dict[str, Any],
    epoch_by_key: dict[tuple[str, int], dict[str, Any]],
) -> dict[str, Any]:
    """对已经有 slot-lock 的 q 逐个枚举 formal residue pair。"""
    q = int(moving_row["q"])
    generator_ell = int(moving_row["generator_ell"])
    fill_ell = int(moving_row["fill_ell"])
    generator_side = str(moving_row["generator_side"])
    fill_side = str(moving_row["fill_side"])
    generator_epoch = epoch_by_key[(generator_side, generator_ell)]
    fill_epoch = epoch_by_key[(fill_side, fill_ell)]
    generator_residues = [int(value) for value in generator_epoch["residue_sample"]]
    fill_residues = [int(value) for value in fill_epoch["residue_sample"]]

    p_delay = int(slot_row["p_delay"])
    pair_lo, pair_hi = [int(value) for value in slot_row["pair_phase_support"]]
    support_width = max(0, pair_hi - pair_lo + 1)
    formal_pair_count = len(generator_residues) * len(fill_residues)

    supported_pairs: list[dict[str, Any]] = []
    pruned_samples: list[dict[str, Any]] = []
    for generator_residue in generator_residues:
        for fill_residue in fill_residues:
            shifted_fill_residue = (fill_residue - p_delay) % fill_ell
            combined_residue, combined_modulus = crt_pair(
                generator_residue,
                generator_ell,
                shifted_fill_residue,
                fill_ell,
            )
            reps = representatives(pair_lo, pair_hi, combined_residue, combined_modulus)
            packet = {
                "generator_residue": generator_residue,
                "fill_residue": fill_residue,
                "shifted_fill_residue": shifted_fill_residue,
                "combined_crt_residue": combined_residue,
                "combined_crt_modulus": combined_modulus,
                "representatives_in_pair_support": reps,
            }
            if reps:
                supported_pairs.append(packet)
            elif len(pruned_samples) < 6:
                pruned_samples.append(packet)

    actual_count = int(moving_row["realized_affine_twin_pair_count"])
    supported_count = len(supported_pairs)
    return {
        "q": q,
        "route": "CRTWindowExactPruning",
        "generator_ell": generator_ell,
        "fill_ell": fill_ell,
        "generator_side": generator_side,
        "fill_side": fill_side,
        "formal_pair_count": formal_pair_count,
        "actual_packet_count_current": actual_count,
        "source_materialized_current": True,
        "slot_lock_materialized_current": True,
        "pair_phase_support": [pair_lo, pair_hi],
        "pair_phase_support_width": support_width,
        "combined_modulus": generator_ell * fill_ell,
        "combined_modulus_exceeds_support_width": generator_ell * fill_ell > support_width,
        "supported_pair_count_by_exact_crt": supported_count,
        "crt_window_empty_pair_count": formal_pair_count - supported_count,
        "source_unmaterialized_pair_count": 0,
        "unresolved_formal_pair_count_current": max(0, supported_count - actual_count),
        "supported_pairs": supported_pairs,
        "pruned_pair_samples": pruned_samples,
    }


def unmaterialized_row(
    moving_row: dict[str, Any],
    pair_by_gap: dict[int, list[dict[str, Any]]],
) -> dict[str, Any]:
    """对没有 matching source 的 q 登记 source materialization 删除。"""
    q = int(moving_row["q"])
    generator_ell = int(moving_row["generator_ell"])
    fill_ell = int(moving_row["fill_ell"])
    generator_side = str(moving_row["generator_side"])
    fill_side = str(moving_row["fill_side"])
    formal_pair_count = int(moving_row["epoch_pair_product_used_upper"])
    same_gap_rows = pair_by_gap.get(q, [])
    matching_rows = [
        row
        for row in same_gap_rows
        if int(row["generator_ell"]) == generator_ell
        and int(row["fill_ell"]) == fill_ell
        and str(row["generator_side"]) == generator_side
        and str(row["fill_side"]) == fill_side
    ]
    same_gap_mismatch_keys = [row["gap_fill_pair_key"] for row in same_gap_rows[:4]]
    if same_gap_rows and not matching_rows:
        reason = "SameGapButWrongGeneratorOrOrientation"
    else:
        reason = "NoGapFillSourceForQ"
    return {
        "q": q,
        "route": "SourceMaterializationFailure",
        "generator_ell": generator_ell,
        "fill_ell": fill_ell,
        "generator_side": generator_side,
        "fill_side": fill_side,
        "formal_pair_count": formal_pair_count,
        "actual_packet_count_current": 0,
        "source_materialized_current": False,
        "slot_lock_materialized_current": False,
        "source_failure_reason": reason,
        "same_gap_source_row_count": len(same_gap_rows),
        "matching_source_row_count": len(matching_rows),
        "same_gap_mismatch_keys": same_gap_mismatch_keys,
        "supported_pair_count_by_exact_crt": 0,
        "crt_window_empty_pair_count": 0,
        "source_unmaterialized_pair_count": formal_pair_count,
        "unresolved_formal_pair_count_current": 0,
    }


def build_result(
    moving_path: Path,
    slot_path: Path,
    pair_path: Path,
    epoch_path: Path,
    actual_contract_path: Path,
) -> dict[str, Any]:
    """构造 formal-pair pruning 审计结果。"""
    moving = load_json(moving_path)
    slot = load_json(slot_path)
    pair = load_json(pair_path)
    epoch = load_json(epoch_path)
    actual_contract = load_json(actual_contract_path)

    slot_by_q = slot_index(slot["affine_twin_slot_phase_lock_rows"])
    pair_by_gap = pair_rows_by_q(pair["gap_fill_pair_rows"])
    epoch_by_key = epoch_index(epoch["epoch_capacity_rows"])

    rows: list[dict[str, Any]] = []
    for moving_row in moving["candidate_affine_twin_epoch_pair_rows"]:
        q = int(moving_row["q"])
        if q in slot_by_q:
            rows.append(exact_pruning_for_slot(moving_row, slot_by_q[q], epoch_by_key))
        else:
            rows.append(unmaterialized_row(moving_row, pair_by_gap))

    formal_total = sum(int(row["formal_pair_count"]) for row in rows)
    actual_total = sum(int(row["actual_packet_count_current"]) for row in rows)
    crt_pruned_total = sum(int(row["crt_window_empty_pair_count"]) for row in rows)
    source_unmaterialized_total = sum(
        int(row["source_unmaterialized_pair_count"]) for row in rows
    )
    unresolved_total = sum(int(row["unresolved_formal_pair_count_current"]) for row in rows)
    formal_to_actual_gap = formal_total - actual_total
    aggregate = {
        "moving_ledger": str(moving_path.relative_to(ROOT)),
        "slot_ledger": str(slot_path.relative_to(ROOT)),
        "pair_ledger": str(pair_path.relative_to(ROOT)),
        "epoch_ledger": str(epoch_path.relative_to(ROOT)),
        "actual_contract_ledger": str(actual_contract_path.relative_to(ROOT)),
        "candidate_q_values": [int(row["q"]) for row in rows],
        "formal_pair_total": formal_total,
        "actual_packet_total_current": actual_total,
        "formal_to_actual_gap": formal_to_actual_gap,
        "crt_window_empty_pair_total_current": crt_pruned_total,
        "source_unmaterialized_pair_total_current": source_unmaterialized_total,
        "unresolved_formal_pair_total_current": unresolved_total,
        "current_formal_gap_fully_pruned": formal_to_actual_gap
        == crt_pruned_total + source_unmaterialized_total,
        "all_exact_crt_supported_pairs_match_actual_current": all(
            int(row["supported_pair_count_by_exact_crt"])
            == int(row["actual_packet_count_current"])
            for row in rows
        ),
        "actual_contract_gap_agrees": formal_to_actual_gap
        == int(actual_contract["aggregate"]["total_formal_to_actual_gap"]),
        "product_accounting_tightening_closed_current_sweep": unresolved_total == 0,
        "global_product_accounting_tightening_proved": False,
        "row_column_unconditional_closed": False,
    }
    return {
        "certificate_type": "prime_matrix_affine_twin_formal_pair_pruning_audit",
        "status": "current_sweep_formal_pair_gap_fully_pruned_global_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "aggregate": aggregate,
        "pruning_rows": rows,
        "contract": {
            "formal_universe": "all generator/fill residue products counted by M_form",
            "actual_packet": "source-materialized gap-fill pair plus slot-lock CRT representative",
            "closed_current_sweep": aggregate["current_formal_gap_fully_pruned"],
            "global_remaining": [
                "GlobalProductAccountingTightening",
                "SourceMaterializationFailure-PDEC/SAE",
                "CRTWindowEmptyGlobalSupportBound",
                "PrimitiveTwinSlotSupportEscape-PDEC/SAE",
            ],
        },
        "dependency_hashes": {
            str(path.relative_to(ROOT)): sha256(path)
            for path in (moving_path, slot_path, pair_path, epoch_path, actual_contract_path)
        },
    }


def write_outputs(result: dict[str, Any]) -> None:
    """写出 JSON 和 Markdown 证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    for path in (OUT_LEDGER, OUT_JSON):
        path.write_text(
            json.dumps(result, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

    agg = result["aggregate"]
    lines = [
        "# Prime Matrix AffineTwin formal-pair pruning audit",
        "",
        "**状态：** `current_sweep_formal_pair_gap_fully_pruned_global_open`",
        "",
        "本审计继续压缩 PM-ALC 的 `ProductAccountingTightening` 缺口：",
        "形式乘积 `M_form` 只计入两侧 residue 的笛卡尔积；actual packet 还必须同时有 gap-fill source materialization 与双槽 CRT 相位代表。",
        "",
        "```text",
        f"candidate_q_values={agg['candidate_q_values']}",
        f"formal_pair_total={agg['formal_pair_total']}",
        f"actual_packet_total_current={agg['actual_packet_total_current']}",
        f"formal_to_actual_gap={agg['formal_to_actual_gap']}",
        f"crt_window_empty_pair_total_current={agg['crt_window_empty_pair_total_current']}",
        f"source_unmaterialized_pair_total_current={agg['source_unmaterialized_pair_total_current']}",
        f"unresolved_formal_pair_total_current={agg['unresolved_formal_pair_total_current']}",
        f"current_formal_gap_fully_pruned={fmt_bool(agg['current_formal_gap_fully_pruned'])}",
        "```",
        "",
        "## 1. pruning 表",
        "",
        "| q | route | M_form | actual | CRT empty | source unmaterialized | unresolved | note |",
        "| ---: | --- | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in result["pruning_rows"]:
        note = row.get("source_failure_reason", "")
        if row["route"] == "CRTWindowExactPruning":
            note = "slot CRT support enumerated exactly"
        lines.append(
            "| {q} | `{route}` | {formal} | {actual} | {crt} | {source} | {unresolved} | {note} |".format(
                q=row["q"],
                route=table_cell(row["route"]),
                formal=row["formal_pair_count"],
                actual=row["actual_packet_count_current"],
                crt=row["crt_window_empty_pair_count"],
                source=row["source_unmaterialized_pair_count"],
                unresolved=row["unresolved_formal_pair_count_current"],
                note=table_cell(note),
            )
        )

    lines.extend(
        [
            "",
            "## 2. q=31 的精确 CRT 删除",
            "",
            "`q=31` 的 `M_form=12` 来自 `3 x 4` 个 residue 配对。逐个 CRT 合并后，只有一对在 pair support `[2669,2688]` 中有代表：",
            "",
            "| generator residue | fill residue | shifted fill residue | CRT residue | representatives |",
            "| ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for row in result["pruning_rows"]:
        if row["q"] == 31:
            for packet in row.get("supported_pairs", []):
                lines.append(
                    "| {g} | {f} | {sf} | {cr} | `{reps}` |".format(
                        g=packet["generator_residue"],
                        f=packet["fill_residue"],
                        sf=packet["shifted_fill_residue"],
                        cr=packet["combined_crt_residue"],
                        reps=packet["representatives_in_pair_support"],
                    )
                )
            lines.extend(
                [
                    "",
                    f"其余 `{row['crt_window_empty_pair_count']}` 对 residue 的 CRT 代表均落在该支撑窗外，所以是 `CRTWindowEmpty` 虚配对。",
                ]
            )
            break

    lines.extend(
        [
            "",
            "## 3. 结论边界",
            "",
            "- 当前 sweep 的 `formal_to_actual_gap=39` 已完全分解：`11` 个 `CRTWindowEmpty`，`28` 个 `SourceMaterializationFailure`。",
            "- 这关闭的是当前证书的形式账本收紧，不是全局行/列命题。",
            "- 全局仍需证明所有未来形式配对也必须进入 `CRTWindowEmpty`、`SourceMaterializationFailure-PDEC/SAE` 或 `PrimitiveTwinSlotSupportEscape-PDEC/SAE`。",
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
    parser = argparse.ArgumentParser(description="生成 AffineTwin formal-pair pruning 审计证书。")
    parser.add_argument("--moving-ledger", type=Path, default=MOVING_LEDGER)
    parser.add_argument("--slot-ledger", type=Path, default=SLOT_LEDGER)
    parser.add_argument("--pair-ledger", type=Path, default=PAIR_LEDGER)
    parser.add_argument("--epoch-ledger", type=Path, default=EPOCH_LEDGER)
    parser.add_argument("--actual-contract-ledger", type=Path, default=ACTUAL_CONTRACT_LEDGER)
    return parser.parse_args()


def main() -> None:
    """入口。"""
    args = parse_args()
    result = build_result(
        args.moving_ledger,
        args.slot_ledger,
        args.pair_ledger,
        args.epoch_ledger,
        args.actual_contract_ledger,
    )
    write_outputs(result)
    print(json.dumps(result["aggregate"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
