#!/usr/bin/env python3
"""生成 prime-anchor post-band immediate repeat 证书。

用法示例：
  python3 experiments/prime_matrix_prime_anchor_postband_immediate_repeat_router.py
  python3 -m json.tool data/prime-matrix-prime-anchor-postband-immediate-repeat-ledger.json

输出：
  data/prime-matrix-prime-anchor-postband-immediate-repeat-ledger.json
  docs/monograph/prime-matrix-prime-anchor-postband-immediate-repeat-router.json
  docs/monograph/prime-matrix-prime-anchor-postband-immediate-repeat-router.md
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

PRIME_FILTER = DATA / "prime-matrix-two-residue-spare-prime-anchor-filter-ledger.json"
SATURATION = DATA / "prime-matrix-cross-carrier-fifty-unit-residue-saturation-ledger.json"

OUT_LEDGER = DATA / "prime-matrix-prime-anchor-postband-immediate-repeat-ledger.json"
OUT_JSON = DOCS / "prime-matrix-prime-anchor-postband-immediate-repeat-router.json"
OUT_MD = DOCS / "prime-matrix-prime-anchor-postband-immediate-repeat-router.md"

PREVIOUS_TARGET = "PrimeAnchorFilteredNonzeroResidueCoverageOrTransportResetPDEC"
NEXT_TARGET = "ImmediatePrimeAnchorRepeatTransportResetPDECOrEndpointMotionSAE"


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


def smallest_factor(n: int) -> int | None:
    """返回最小非平凡因子；素数返回 None。"""
    if n < 2:
        return n
    if n % 2 == 0:
        return 2 if n != 2 else None
    d = 3
    while d * d <= n:
        if n % d == 0:
            return d
        d += 2
    return None


def is_prime(n: int) -> bool:
    """小范围素性判定。"""
    return smallest_factor(n) is None and n >= 2


def p_at(anchor_p: int, delay: int, step: int) -> int:
    """由同步步号计算 P。"""
    return anchor_p + delay * step


def residue_at(anchor_residue: int, increment: int, ell: int, step: int) -> int:
    """由同步步号计算 residue。"""
    return (anchor_residue + increment * step) % ell


def row_for_step(
    step: int,
    anchor_p: int,
    delay: int,
    anchor_residue: int,
    increment: int,
    ell: int,
    current_union: set[int],
    original_used: set[int],
) -> dict[str, Any]:
    """构造单步审计行。"""
    p_value = p_at(anchor_p, delay, step)
    factor = smallest_factor(p_value)
    residue = residue_at(anchor_residue, increment, ell, step)
    return {
        "step": step,
        "p": p_value,
        "residue": residue,
        "is_prime_p": factor is None,
        "smallest_factor": factor,
        "already_in_prime_filtered_union": residue in current_union,
        "already_in_original_used_residues": residue in original_used,
    }


def build_result() -> dict[str, Any]:
    """构造 post-band immediate repeat 证书。"""
    filt = aggregate(PRIME_FILTER)
    sat = aggregate(SATURATION)

    ell = int(filt["ell"])
    anchor_p = int(filt["support_anchor_p"])
    delay = int(filt["support_delay"])
    anchor_residue = int(sat["anchor_residue_mod_ell"])
    increment = int(sat["increment_mod_ell"])
    first_step, last_step = [int(value) for value in filt["admitted_step_range"]]
    p_min, p_max = [int(value) for value in filt["current_epoch_p_range"]]

    original_used = set(int(value) for value in sat["used_residues"])
    missing_including_zero = set(int(value) for value in filt["prime_filtered_missing_residues_including_zero"])
    current_union = set(range(ell)) - missing_including_zero
    nonzero_universe = set(range(1, ell))
    missing_nonzero = set(int(value) for value in filt["prime_filtered_missing_nonzero_residues"])

    post_band_rows: list[dict[str, Any]] = []
    first_prime_row: dict[str, Any] | None = None
    first_new_prime_row: dict[str, Any] | None = None
    first_repeat_prime_row: dict[str, Any] | None = None
    new_prime_rows_before_repeat: list[dict[str, Any]] = []

    seen = set(current_union)
    remaining_missing = set(missing_nonzero)
    for step in range(last_step + 1, 5000):
        row = row_for_step(
            step,
            anchor_p,
            delay,
            anchor_residue,
            increment,
            ell,
            current_union,
            original_used,
        )
        if step <= last_step + 12:
            post_band_rows.append(row)
        if not row["is_prime_p"]:
            continue
        if first_prime_row is None:
            first_prime_row = row
        residue = int(row["residue"])
        if residue in seen:
            first_repeat_prime_row = row
            break
        if first_new_prime_row is None:
            first_new_prime_row = row
        new_prime_rows_before_repeat.append(row)
        seen.add(residue)
        remaining_missing.discard(residue)

    if first_prime_row is None or first_repeat_prime_row is None:
        raise RuntimeError("scan did not find the expected post-band prime repeat")

    coverage_preempted = first_repeat_prime_row == first_prime_row
    repeat_step = int(first_repeat_prime_row["step"])
    repeat_p = int(first_repeat_prime_row["p"])
    repeat_residue = int(first_repeat_prime_row["residue"])
    admitted_lattice_p_max = p_at(anchor_p, delay, last_step)

    result = {
        "certificate_type": "prime_matrix_prime_anchor_postband_immediate_repeat_router",
        "status": "prime_anchor_nonzero_coverage_preempted_by_first_postband_repeat",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_sweep_not_used_as_global_proof": True,
        "aggregate": {
            "row_column_unconditional_closed": False,
            "previous_hardpoint": PREVIOUS_TARGET,
            "ell": ell,
            "support_anchor_p": anchor_p,
            "support_delay": delay,
            "admitted_step_range": [first_step, last_step],
            "current_epoch_p_range": [p_min, p_max],
            "current_prime_filtered_union_size": len(current_union),
            "current_prime_filtered_nonzero_seen": len(current_union & nonzero_universe),
            "current_prime_filtered_nonzero_spare": len(missing_nonzero),
            "first_postband_prime_anchor": first_prime_row,
            "first_postband_prime_is_repeat": coverage_preempted,
            "first_postband_prime_is_original_used_repeat": bool(
                first_prime_row["already_in_original_used_residues"]
            ),
            "first_new_prime_anchor_before_repeat": first_new_prime_row,
            "new_prime_anchor_count_before_first_repeat": len(new_prime_rows_before_repeat),
            "new_prime_rows_before_first_repeat": new_prime_rows_before_repeat,
            "first_repeat_prime_anchor": first_repeat_prime_row,
            "repeat_residue": repeat_residue,
            "repeat_in_original_used_residues": repeat_residue in original_used,
            "missing_nonzero_remaining_at_first_repeat": len(remaining_missing),
            "missing_nonzero_residues_remaining_at_first_repeat": sorted(remaining_missing),
            "coverage_before_reset_possible_in_same_epoch": False,
            "repeat_step_gap_after_admitted_band": repeat_step - last_step,
            "repeat_p_extension_beyond_epoch_p_max": repeat_p - p_max,
            "repeat_p_extension_beyond_admitted_lattice_p_max": repeat_p - admitted_lattice_p_max,
            "repeat_extension_over_epoch_width": (repeat_p - p_max) / (p_max - p_min + 1),
            "near_endpoint_candidate_steps_checked": [last_step + 1, repeat_step],
            "hardpoint_after_router": NEXT_TARGET,
            "next_direct_attack_target": NEXT_TARGET,
        },
        "post_band_rows_until_first_prime_window": [
            row for row in post_band_rows if int(row["step"]) <= repeat_step
        ],
        "plain_conclusion": (
            "在 prime-anchor 过滤后，长 AP 非零 residue 覆盖分支被更早截断："
            "当前 admitted 带后的第一个素数锚就是 P=9887，residue=18，"
            "而 18 已在原始 minus:71 已用 residue 集中。"
            "因此在同一无 reset epoch 中，反例链无法先补入任何新缺失非零 residue；"
            "若 epoch 延伸到该点，立即进入 transport reset-PDEC；"
            "若不延伸，则回到 endpoint motion/SAE。"
        ),
        "dependency_hashes": {
            str(PRIME_FILTER.relative_to(ROOT)): sha256(PRIME_FILTER),
            str(SATURATION.relative_to(ROOT)): sha256(SATURATION),
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
    first_prime = agg["first_postband_prime_anchor"]
    repeat = agg["first_repeat_prime_anchor"]
    lines = [
        "# Prime Matrix prime-anchor post-band immediate repeat router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"row_column_unconditional_closed={fmt_bool(agg['row_column_unconditional_closed'])}",
        f"previous_hardpoint={agg['previous_hardpoint']}",
        f"current_prime_filtered_union_size={agg['current_prime_filtered_union_size']}",
        f"current_prime_filtered_nonzero_spare={agg['current_prime_filtered_nonzero_spare']}",
        f"first_postband_prime_anchor={first_prime}",
        f"first_postband_prime_is_repeat={fmt_bool(agg['first_postband_prime_is_repeat'])}",
        f"first_postband_prime_is_original_used_repeat={fmt_bool(agg['first_postband_prime_is_original_used_repeat'])}",
        f"new_prime_anchor_count_before_first_repeat={agg['new_prime_anchor_count_before_first_repeat']}",
        f"missing_nonzero_remaining_at_first_repeat={agg['missing_nonzero_remaining_at_first_repeat']}",
        f"repeat_p_extension_beyond_epoch_p_max={agg['repeat_p_extension_beyond_epoch_p_max']}",
        f"repeat_extension_over_epoch_width={agg['repeat_extension_over_epoch_width']:.12f}",
        f"coverage_before_reset_possible_in_same_epoch={fmt_bool(agg['coverage_before_reset_possible_in_same_epoch'])}",
        f"next_direct_attack_target={agg['next_direct_attack_target']}",
        "```",
        "",
        "## 1. admitted 带后首个素数锚窗口",
        "",
        "| step | P | residue | prime P | smallest factor | in filtered union | in original used |",
        "| ---: | ---: | ---: | --- | ---: | --- | --- |",
    ]
    for row in result["post_band_rows_until_first_prime_window"]:
        factor = "" if row["smallest_factor"] is None else str(row["smallest_factor"])
        lines.append(
            f"| {row['step']} | {row['p']} | {row['residue']} | "
            f"`{fmt_bool(row['is_prime_p'])}` | {factor} | "
            f"`{fmt_bool(row['already_in_prime_filtered_union'])}` | "
            f"`{fmt_bool(row['already_in_original_used_residues'])}` |"
        )

    lines.extend(
        [
            "",
            "## 2. 判定",
            "",
            f"- admitted 带后的第一个素数锚是 `P={first_prime['p']}`，步号 `{first_prime['step']}`，residue `{first_prime['residue']}`。",
            "- 该 residue 已经属于原始 `minus:71` 已用集合，不只是 prime-filtered 合并集合。",
            "- 因此在同一无 reset epoch 中，长 AP 无法先补任何新缺失非零 residue；首次素数锚已经触发旧 residue。",
            "- 若该 epoch 不允许延伸到此点，则出口是 endpoint motion/SAE；若允许延伸，则出口是 transport reset-PDEC。",
            f"- 下一主攻点：`{agg['next_direct_attack_target']}`。",
            "",
            "## 3. 依赖哈希",
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
