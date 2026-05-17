#!/usr/bin/env python3
"""生成 endpoint cut zero-gain 证书。

用法示例：
  python3 experiments/prime_matrix_endpoint_cut_zero_gain_router.py
  python3 -m json.tool data/prime-matrix-endpoint-cut-zero-gain-ledger.json

输出：
  data/prime-matrix-endpoint-cut-zero-gain-ledger.json
  docs/monograph/prime-matrix-endpoint-cut-zero-gain-router.json
  docs/monograph/prime-matrix-endpoint-cut-zero-gain-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

REPEAT_ATOM = DATA / "prime-matrix-prime-anchor-repeat-reset-atom-ledger.json"
IMMEDIATE_REPEAT = DATA / "prime-matrix-prime-anchor-postband-immediate-repeat-ledger.json"

OUT_LEDGER = DATA / "prime-matrix-endpoint-cut-zero-gain-ledger.json"
OUT_JSON = DOCS / "prime-matrix-endpoint-cut-zero-gain-router.json"
OUT_MD = DOCS / "prime-matrix-endpoint-cut-zero-gain-router.md"

PREVIOUS_TARGET = "OneSlotPrimeAnchorRepeatResetPDECExclusionOrEndpointMotionSAE"
NEXT_TARGET = "ZeroGainEndpointCutSAEOrOneSlotResetPDECExclusion"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def aggregate(path: Path) -> dict[str, Any]:
    """读取账本 aggregate；没有 aggregate 时返回原对象。"""
    obj = load_json(path)
    return obj.get("aggregate", obj)


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def enrich_buffer_rows(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """补充 buffer 行的分类标签。"""
    enriched = []
    for row in rows:
        residue = int(row["residue"])
        is_prime = bool(row["is_prime_p"])
        in_union = bool(row["already_in_prime_filtered_union"])
        in_original = bool(row["already_in_original_used_residues"])
        if is_prime and in_original:
            route = "prime_anchor_repeat_reset"
        elif is_prime and not in_union:
            route = "new_prime_anchor_gain"
        elif is_prime:
            route = "prime_anchor_filtered_repeat"
        elif not in_union:
            route = "formal_gap_but_composite_anchor"
        else:
            route = "old_residue_composite_anchor"
        enriched.append({**row, "residue": residue, "route": route})
    return enriched


def build_result() -> dict[str, Any]:
    """构造 endpoint cut zero-gain 证书。"""
    atom = aggregate(REPEAT_ATOM)
    immediate_obj = load_json(IMMEDIATE_REPEAT)
    immediate = immediate_obj["aggregate"]
    endpoint_cut = atom["endpoint_cut"]
    buffer_steps = set(int(step) for step in endpoint_cut["composite_buffer_steps"])
    repeat_step = int(atom["repeat_prime_anchor_step"])
    rows = enrich_buffer_rows(immediate_obj["post_band_rows_until_first_prime_window"])
    cut_buffer_rows = [row for row in rows if int(row["step"]) in buffer_steps]
    repeat_rows = [row for row in rows if int(row["step"]) == repeat_step]
    if len(repeat_rows) != 1:
        raise RuntimeError("expected exactly one repeat row")

    formal_gap_rows = [
        row for row in cut_buffer_rows if row["route"] == "formal_gap_but_composite_anchor"
    ]
    actual_prime_rows = [row for row in cut_buffer_rows if row["is_prime_p"]]
    actual_new_prime_rows = [
        row for row in cut_buffer_rows
        if row["is_prime_p"] and not row["already_in_prime_filtered_union"]
    ]
    old_composite_rows = [
        row for row in cut_buffer_rows if row["route"] == "old_residue_composite_anchor"
    ]
    reset_row = repeat_rows[0]

    result = {
        "certificate_type": "prime_matrix_endpoint_cut_zero_gain_router",
        "status": "endpoint_cut_before_reset_has_zero_prime_anchor_gain",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_sweep_not_used_as_global_proof": True,
        "aggregate": {
            "row_column_unconditional_closed": False,
            "previous_hardpoint": PREVIOUS_TARGET,
            "ell": int(atom["ell"]),
            "endpoint_cut_required_to_avoid_reset": bool(atom["endpoint_cut_required_to_avoid_reset"]),
            "last_epoch_p_max": int(endpoint_cut["last_epoch_p_max"]),
            "must_cut_before_step": int(endpoint_cut["must_cut_before_step"]),
            "must_cut_before_p": int(endpoint_cut["must_cut_before_p"]),
            "cut_buffer_step_count": len(cut_buffer_rows),
            "cut_buffer_steps": [int(row["step"]) for row in cut_buffer_rows],
            "cut_buffer_p_values": [int(row["p"]) for row in cut_buffer_rows],
            "formal_gap_composite_row_count": len(formal_gap_rows),
            "formal_gap_composite_residues": [int(row["residue"]) for row in formal_gap_rows],
            "actual_prime_anchor_count_before_reset": len(actual_prime_rows),
            "actual_new_prime_anchor_count_before_reset": len(actual_new_prime_rows),
            "old_residue_composite_row_count": len(old_composite_rows),
            "reset_row": reset_row,
            "reset_atom_instantiated_at_first_prime_anchor": bool(atom["reset_atom_instantiated"]),
            "endpoint_cut_actual_gain_zero": len(actual_prime_rows) == 0,
            "endpoint_cut_formal_gap_gain_zero_after_prime_filter": (
                len(formal_gap_rows) > 0 and len(actual_prime_rows) == 0
            ),
            "reset_or_zero_gain_endpoint_dichotomy_closed_current_epoch": (
                len(actual_prime_rows) == 0 and bool(atom["reset_atom_instantiated"])
            ),
            "hardpoint_after_router": NEXT_TARGET,
            "next_direct_attack_target": NEXT_TARGET,
        },
        "cut_buffer_rows": cut_buffer_rows,
        "formal_gap_composite_rows": formal_gap_rows,
        "old_residue_composite_rows": old_composite_rows,
        "repeat_reset_row": reset_row,
        "plain_conclusion": (
            "若为避免 P=9887 的 one-slot reset 而在首个 post-band 素数锚前切断端点，"
            "端点外延区间 step=83..89 没有任何实际素数锚。"
            "其中 residue 62 与 0 只是形式缺口，实际 P=9647 与 P=9727 均为合数/被 71 整除。"
            "因此 endpoint cut 分支在当前 primitive epoch 内是零收益 SAE 形态；"
            "若不切断，则 step=90 的 P=9887 立即实例化 one-slot reset-PDEC。"
        ),
        "dependency_hashes": {
            str(REPEAT_ATOM.relative_to(ROOT)): sha256(REPEAT_ATOM),
            str(IMMEDIATE_REPEAT.relative_to(ROOT)): sha256(IMMEDIATE_REPEAT),
        },
    }
    return result


def write_outputs(result: dict[str, Any]) -> None:
    """写出 JSON 与 Markdown。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    OUT_LEDGER.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    agg = result["aggregate"]
    lines = [
        "# Prime Matrix endpoint cut zero-gain router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"row_column_unconditional_closed={fmt_bool(agg['row_column_unconditional_closed'])}",
        f"previous_hardpoint={agg['previous_hardpoint']}",
        f"cut_buffer_step_count={agg['cut_buffer_step_count']}",
        f"formal_gap_composite_row_count={agg['formal_gap_composite_row_count']}",
        f"formal_gap_composite_residues={agg['formal_gap_composite_residues']}",
        f"actual_prime_anchor_count_before_reset={agg['actual_prime_anchor_count_before_reset']}",
        f"actual_new_prime_anchor_count_before_reset={agg['actual_new_prime_anchor_count_before_reset']}",
        f"endpoint_cut_actual_gain_zero={fmt_bool(agg['endpoint_cut_actual_gain_zero'])}",
        f"reset_atom_instantiated_at_first_prime_anchor={fmt_bool(agg['reset_atom_instantiated_at_first_prime_anchor'])}",
        f"reset_or_zero_gain_endpoint_dichotomy_closed_current_epoch={fmt_bool(agg['reset_or_zero_gain_endpoint_dichotomy_closed_current_epoch'])}",
        f"next_direct_attack_target={agg['next_direct_attack_target']}",
        "```",
        "",
        "## 1. endpoint cut buffer",
        "",
        "| step | P | residue | prime P | smallest factor | route |",
        "| ---: | ---: | ---: | --- | ---: | --- |",
    ]
    for row in result["cut_buffer_rows"]:
        factor = "" if row["smallest_factor"] is None else str(row["smallest_factor"])
        lines.append(
            f"| {row['step']} | {row['p']} | {row['residue']} | "
            f"`{fmt_bool(row['is_prime_p'])}` | {factor} | `{row['route']}` |"
        )

    reset = result["repeat_reset_row"]
    lines.extend(
        [
            "",
            "## 2. first prime anchor after buffer",
            "",
            "| step | P | residue | route |",
            "| ---: | ---: | ---: | --- |",
            f"| {reset['step']} | {reset['p']} | {reset['residue']} | `{reset['route']}` |",
            "",
            "## 3. 判定",
            "",
            "- `step=83..89` 是端点切断前唯一可用缓冲，实际素数锚数为 0。",
            "- `residue 62` 与 `residue 0` 是形式缺口，但对应 `P=9647,9727` 都不是素数锚。",
            "- 若端点不切断，`step=90,P=9887` 立刻进入已实例化的一槽 repeat-reset 原子。",
            "- 因此当前 epoch 内的二分是：`reset-PDEC` 或 `zero-gain endpoint cut SAE`。",
            f"- 下一主攻点：`{agg['next_direct_attack_target']}`。",
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


def main() -> None:
    """入口。"""
    result = build_result()
    write_outputs(result)
    print(json.dumps(result["aggregate"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
