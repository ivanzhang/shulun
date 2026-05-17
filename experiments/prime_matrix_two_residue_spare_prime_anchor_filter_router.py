#!/usr/bin/env python3
"""生成 two-residue spare 的素数锚过滤证书。

用法示例：
  python3 experiments/prime_matrix_two_residue_spare_prime_anchor_filter_router.py
  python3 -m json.tool data/prime-matrix-two-residue-spare-prime-anchor-filter-ledger.json

输出：
  data/prime-matrix-two-residue-spare-prime-anchor-filter-ledger.json
  docs/monograph/prime-matrix-two-residue-spare-prime-anchor-filter-router.json
  docs/monograph/prime-matrix-two-residue-spare-prime-anchor-filter-router.md
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

SATURATION = DATA / "prime-matrix-cross-carrier-fifty-unit-residue-saturation-ledger.json"

OUT_LEDGER = DATA / "prime-matrix-two-residue-spare-prime-anchor-filter-ledger.json"
OUT_JSON = DOCS / "prime-matrix-two-residue-spare-prime-anchor-filter-router.json"
OUT_MD = DOCS / "prime-matrix-two-residue-spare-prime-anchor-filter-router.md"

NEXT_TARGET = "PrimeAnchorFilteredNonzeroResidueCoverageOrTransportResetPDEC"


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


def is_prime(n: int) -> bool:
    """小范围素性判定。"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def inv_mod(a: int, modulus: int) -> int:
    """求模逆。"""
    return pow(a, -1, modulus)


def p_at(anchor_p: int, delay: int, step: int) -> int:
    """由同步步号计算 P。"""
    return anchor_p + delay * step


def residue_at(anchor_residue: int, increment: int, ell: int, step: int) -> int:
    """由同步步号计算 residue。"""
    return (anchor_residue + increment * step) % ell


def ap_class_for_residue(
    residue: int,
    anchor_p: int,
    delay: int,
    anchor_residue: int,
    increment: int,
    ell: int,
) -> dict[str, Any]:
    """计算指定 residue 对应的 P 算术级数类。"""
    step0 = ((residue - anchor_residue) * inv_mod(increment, ell)) % ell
    modulus = delay * ell
    p_class = p_at(anchor_p, delay, step0) % modulus
    return {
        "residue": residue,
        "step_class_mod_ell": step0,
        "p_class_mod_delay_ell": p_class,
        "modulus": modulus,
        "gcd_class_modulus": math.gcd(p_class, modulus),
        "prime_anchor_possible_by_coprime_class": math.gcd(p_class, modulus) == 1,
    }


def first_prime_hit_for_residue(
    residue: int,
    start_step: int,
    max_step: int,
    anchor_p: int,
    delay: int,
    anchor_residue: int,
    increment: int,
    ell: int,
) -> dict[str, Any] | None:
    """查找某个 residue 在给定步号后的首个素数锚。"""
    for step in range(start_step, max_step + 1):
        if residue_at(anchor_residue, increment, ell, step) != residue:
            continue
        p_value = p_at(anchor_p, delay, step)
        if is_prime(p_value):
            return {"step": step, "p": p_value, "residue": residue}
    return None


def build_result() -> dict[str, Any]:
    """构造素数锚过滤证书。"""
    sat = aggregate(SATURATION)
    ell = int(sat["ell"])
    used_set = set(int(value) for value in sat["used_residues"])
    anchor_p = int(sat["support_anchor_p"])
    delay = int(sat["support_delay"])
    anchor_residue = int(sat["anchor_residue_mod_ell"])
    increment = int(sat["increment_mod_ell"])
    first_step, last_step = [int(value) for value in sat["admitted_step_range"]]
    p_min, p_max = [int(value) for value in sat["current_epoch_p_range"]]
    current_rows = []
    current_prime_residues: set[int] = set()
    current_composite_rows = []
    for step in range(first_step, last_step + 1):
        p_value = p_at(anchor_p, delay, step)
        residue = residue_at(anchor_residue, increment, ell, step)
        row = {
            "step": step,
            "p": p_value,
            "residue": residue,
            "already_used": residue in used_set,
        }
        if is_prime(p_value):
            current_prime_residues.add(residue)
            current_rows.append(row)
        else:
            current_composite_rows.append(row)

    current_union = set(used_set) | current_prime_residues
    nonzero_universe = set(range(1, ell))
    missing_nonzero = sorted(nonzero_universe - current_union)
    missing_including_zero = sorted(set(range(ell)) - current_union)

    predicted_rows = []
    for row in sat["first_missing_future_steps"] + [sat["first_post_full_repeat_step"]]:
        p_value = int(row["p"])
        residue = int(row["residue"])
        predicted_rows.append(
            {
                "step": int(row["step"]),
                "p": p_value,
                "residue": residue,
                "is_prime_p": is_prime(p_value),
                "p_factor_note": "divisible_by_ell" if residue == 0 else "composite_or_unavailable",
                "structurally_possible_prime_anchor": residue != 0,
            }
        )

    residue_zero_class = ap_class_for_residue(
        0,
        anchor_p,
        delay,
        anchor_residue,
        increment,
        ell,
    )
    residue_62_first_hit = first_prime_hit_for_residue(
        62,
        last_step + 1,
        20000,
        anchor_p,
        delay,
        anchor_residue,
        increment,
        ell,
    )

    first_hit_rows = []
    remaining = set(missing_nonzero)
    for step in range(last_step + 1, 20000):
        if not remaining:
            break
        residue = residue_at(anchor_residue, increment, ell, step)
        if residue not in remaining:
            continue
        p_value = p_at(anchor_p, delay, step)
        if is_prime(p_value):
            first_hit_rows.append(
                {
                    "residue": residue,
                    "step": step,
                    "p": p_value,
                    "extension_beyond_epoch_p_max": p_value - p_max,
                }
            )
            remaining.remove(residue)

    full_nonzero_row = first_hit_rows[-1] if not remaining else None
    first_repeat_after_full = None
    if full_nonzero_row is not None:
        for step in range(int(full_nonzero_row["step"]) + 1, int(full_nonzero_row["step"]) + 5000):
            p_value = p_at(anchor_p, delay, step)
            if is_prime(p_value):
                first_repeat_after_full = {
                    "step": step,
                    "p": p_value,
                    "residue": residue_at(anchor_residue, increment, ell, step),
                    "extension_beyond_epoch_p_max": p_value - p_max,
                }
                break

    result = {
        "certificate_type": "prime_matrix_two_residue_spare_prime_anchor_filter_router",
        "status": "two_residue_spare_prime_anchor_filter_closes_near_fill_global_ap_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_sweep_not_used_as_global_proof": True,
        "aggregate": {
            "row_column_unconditional_closed": False,
            "previous_hardpoint": "TwoResidueSpareEndpointExtensionOrTransportResetPDEC",
            "ell": ell,
            "support_anchor_p": anchor_p,
            "support_delay": delay,
            "current_epoch_p_range": [p_min, p_max],
            "admitted_step_range": [first_step, last_step],
            "existing_used_residue_count": len(used_set),
            "admitted_lattice_step_count": last_step - first_step + 1,
            "admitted_prime_anchor_count": len(current_rows),
            "admitted_composite_anchor_count": len(current_composite_rows),
            "admitted_prime_anchor_residue_count": len(current_prime_residues),
            "admitted_prime_anchor_intersection_existing_count": len(current_prime_residues & used_set),
            "admitted_prime_anchor_new_residue_count": len(current_prime_residues - used_set),
            "prime_filtered_union_size": len(current_union),
            "prime_filtered_nonzero_spare": len(nonzero_universe - current_union),
            "prime_filtered_missing_nonzero_residues": missing_nonzero,
            "prime_filtered_missing_residues_including_zero": missing_including_zero,
            "residue_zero_prime_anchor_impossible": not bool(
                residue_zero_class["prime_anchor_possible_by_coprime_class"]
            ),
            "residue_zero_ap_class": residue_zero_class,
            "predicted_two_spare_rows_are_prime": all(row["is_prime_p"] for row in predicted_rows[:2]),
            "predicted_two_spare_rows": predicted_rows,
            "first_prime_hit_for_residue_62": residue_62_first_hit,
            "first_full_nonzero_capacity_row": full_nonzero_row,
            "first_repeat_after_full_nonzero_capacity": first_repeat_after_full,
            "all_missing_nonzero_residues_hit_within_scan": not bool(remaining),
            "remaining_missing_nonzero_residues_after_scan": sorted(remaining),
            "hardpoint_after_router": NEXT_TARGET,
            "next_direct_attack_target": NEXT_TARGET,
        },
        "current_prime_anchor_rows": current_rows,
        "first_hit_rows_for_current_missing_nonzero_residues": first_hit_rows,
        "plain_conclusion": (
            "加入 P 必须为素数的锚限制后，上一证书的两空位外延进一步收窄。"
            "当前 admitted lattice 的 64 个步号中只有 17 个素数锚，新增 residue 只有 13 个；"
            "与既有 22 个 residue 合并后仅为 35/70 个非零 residue。"
            "原先两个空位中的 residue 0 对 P>71 素数锚结构性不可能，因为它强制 71|P；"
            "residue 62 的近端候选 P=9647 也是合数，首个素数锚要到 P=26687。"
            "因此近端 two-residue fill 不能作为真实链；若要最终填满全部非零 residue，"
            "必须进入长 AP 素数锚到达问题，当前扫描中最后一个非零 residue 到 P=98047 才出现，"
            "之后首个素数锚重复在 P=98207，才会进入 transport reset-PDEC。"
        ),
        "dependency_hashes": {
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
    zero_class = agg["residue_zero_ap_class"]
    hit62 = agg["first_prime_hit_for_residue_62"]
    full = agg["first_full_nonzero_capacity_row"]
    repeat = agg["first_repeat_after_full_nonzero_capacity"]
    lines = [
        "# Prime Matrix two-residue spare prime-anchor filter router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"row_column_unconditional_closed={fmt_bool(agg['row_column_unconditional_closed'])}",
        f"admitted_lattice_step_count={agg['admitted_lattice_step_count']}",
        f"admitted_prime_anchor_count={agg['admitted_prime_anchor_count']}",
        f"admitted_prime_anchor_new_residue_count={agg['admitted_prime_anchor_new_residue_count']}",
        f"prime_filtered_union_size={agg['prime_filtered_union_size']}",
        f"prime_filtered_nonzero_spare={agg['prime_filtered_nonzero_spare']}",
        f"residue_zero_prime_anchor_impossible={fmt_bool(agg['residue_zero_prime_anchor_impossible'])}",
        f"residue_zero_p_class_mod_5680={zero_class['p_class_mod_delay_ell']}",
        f"residue_zero_gcd_class_modulus={zero_class['gcd_class_modulus']}",
        f"first_prime_hit_for_residue_62={hit62}",
        f"first_full_nonzero_capacity_row={full}",
        f"first_repeat_after_full_nonzero_capacity={repeat}",
        f"next_direct_attack_target={agg['next_direct_attack_target']}",
        "```",
        "",
        "## 1. 当前 admitted 带内的素数锚",
        "",
        "| step | P | residue | already used |",
        "| ---: | ---: | ---: | --- |",
    ]
    for row in result["current_prime_anchor_rows"]:
        lines.append(
            f"| {row['step']} | {row['p']} | {row['residue']} | `{fmt_bool(row['already_used'])}` |"
        )

    lines.extend(
        [
            "",
            "## 2. 两空位近端候选",
            "",
            "| step | P | residue | prime P | structural status |",
            "| ---: | ---: | ---: | --- | --- |",
        ]
    )
    for row in agg["predicted_two_spare_rows"]:
        lines.append(
            f"| {row['step']} | {row['p']} | {row['residue']} | "
            f"`{fmt_bool(row['is_prime_p'])}` | `{row['p_factor_note']}` |"
        )

    lines.extend(
        [
            "",
            "## 3. 当前缺失非零 residue 的首个素数锚",
            "",
            "| residue | step | P | extension beyond current p_max |",
            "| ---: | ---: | ---: | ---: |",
        ]
    )
    for row in result["first_hit_rows_for_current_missing_nonzero_residues"]:
        lines.append(
            f"| {row['residue']} | {row['step']} | {row['p']} | {row['extension_beyond_epoch_p_max']} |"
        )

    lines.extend(
        [
            "",
            "## 4. 证明边界",
            "",
            "- `residue 0` 不是可填空位；在 `P>71` 的素数锚线上它结构性不可能。",
            "- 近端 `P=9647,9727,9807` 都不是素数锚，因此不能作为真实链到达。",
            "- 若反例链仍要靠 `minus:71` 饱和触发 reset，必须证明长 AP 素数锚覆盖全部非零 residue；当前 finite scan 中这要到 `P=98047` 才发生。",
            f"- 下一主攻点：`{agg['next_direct_attack_target']}`。",
            "",
            "## 5. 依赖哈希",
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
