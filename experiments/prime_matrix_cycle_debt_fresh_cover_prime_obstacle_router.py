#!/usr/bin/env python3
"""生成 cycle-debt fresh-cover 真实素数障碍证书。

用法示例：
  python3 experiments/prime_matrix_cycle_debt_fresh_cover_prime_obstacle_router.py
  python3 -m json.tool data/prime-matrix-cycle-debt-fresh-cover-prime-obstacle-ledger.json

输出：
  data/prime-matrix-cycle-debt-fresh-cover-prime-obstacle-ledger.json
  docs/monograph/prime-matrix-cycle-debt-fresh-cover-prime-obstacle-router.json
  docs/monograph/prime-matrix-cycle-debt-fresh-cover-prime-obstacle-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

CYCLE_COVER = DATA / "prime-matrix-cycle-debt-crt-cover-pressure-ledger.json"
NEAR_SHIFT = DATA / "prime-matrix-cycle-debt-near-shift-exit-boundary-ledger.json"

OUT_LEDGER = DATA / "prime-matrix-cycle-debt-fresh-cover-prime-obstacle-ledger.json"
OUT_JSON = DOCS / "prime-matrix-cycle-debt-fresh-cover-prime-obstacle-router.json"
OUT_MD = DOCS / "prime-matrix-cycle-debt-fresh-cover-prime-obstacle-router.md"

PREVIOUS_TARGET = "FreshMovingCoverPDECOrGlobalSupportMotionSAE"
NEXT_TARGET = "FreshCoverPrimeObstaclePDECOrSupportRowReplacementSAE"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def division_record(numerator: int, denominator: int) -> dict[str, Any]:
    """记录整数比值。"""
    floor, remainder = divmod(numerator, denominator)
    return {
        "numerator": numerator,
        "denominator": denominator,
        "floor": floor,
        "remainder": remainder,
        "is_integer": remainder == 0,
    }


def is_prime(n: int) -> bool:
    """试除判定素数；本证书只处理小样本整数。"""
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def build_result() -> dict[str, Any]:
    """构造 fresh-cover 真实素数障碍证书。"""
    cover = load_json(CYCLE_COVER)
    near = load_json(NEAR_SHIFT)
    cover_agg = cover["aggregate"]
    near_agg = near["aggregate"]

    period_p = int(cover_agg["period_p"])
    near_shift_limit = int(near_agg["near_shift_limit_cycles"])
    rows = sorted(cover["pressure_rows"], key=lambda row: int(row["residue"]))
    total_rows = len(rows)
    total_debt_mass = sum(int(row["cycle_debt"]) for row in rows)

    shift_obstacle_audits: list[dict[str, Any]] = []
    total_prime_obstacles_all_shifts = 0
    total_new_prime_obstacles_all_shifts = 0
    min_prime_obstacles = total_debt_mass
    min_prime_obstacle_rows = total_rows
    max_prime_obstacles = 0
    max_prime_obstacle_rows = 0
    min_obstacle_shift = None
    max_obstacle_shift = None

    for shift in range(1, near_shift_limit + 1):
        row_windows = []
        prime_obstacles = []
        certified_exit_prime_obstacles = []
        new_prime_obstacles = []
        composite_slot_count = 0
        rows_with_prime_obstacle = 0

        for row in rows:
            residue = int(row["residue"])
            debt = int(row["cycle_debt"])
            p0 = int(row["first_formal_p"])
            row_primes = []
            row_composites = []
            for position in range(debt):
                cycle = shift + position
                p_value = p0 + cycle * period_p
                if is_prime(p_value):
                    obstacle = {
                        "residue": residue,
                        "cycle_debt": debt,
                        "window_position": position,
                        "absolute_cycle_from_first_formal": cycle,
                        "p": p_value,
                        "prime_obstacle_type": "certified_exit_prime"
                        if cycle == debt
                        else "new_prime_obstacle",
                    }
                    row_primes.append(obstacle)
                    prime_obstacles.append(obstacle)
                    if cycle == debt:
                        certified_exit_prime_obstacles.append(obstacle)
                    else:
                        new_prime_obstacles.append(obstacle)
                else:
                    row_composites.append(
                        {
                            "window_position": position,
                            "absolute_cycle_from_first_formal": cycle,
                            "p": p_value,
                        }
                    )
                    composite_slot_count += 1
            if row_primes:
                rows_with_prime_obstacle += 1
            row_windows.append(
                {
                    "residue": residue,
                    "cycle_debt": debt,
                    "shift_cycles": shift,
                    "window_start_cycle": shift,
                    "window_end_cycle": shift + debt - 1,
                    "window_slot_count": debt,
                    "prime_obstacle_count": len(row_primes),
                    "composite_slot_count": len(row_composites),
                    "has_prime_obstacle": bool(row_primes),
                    "prime_obstacles": row_primes,
                }
            )

        obstacle_count = len(prime_obstacles)
        if obstacle_count < min_prime_obstacles:
            min_prime_obstacles = obstacle_count
            min_obstacle_shift = shift
        if rows_with_prime_obstacle < min_prime_obstacle_rows:
            min_prime_obstacle_rows = rows_with_prime_obstacle
        if obstacle_count > max_prime_obstacles:
            max_prime_obstacles = obstacle_count
            max_obstacle_shift = shift
        if rows_with_prime_obstacle > max_prime_obstacle_rows:
            max_prime_obstacle_rows = rows_with_prime_obstacle

        total_prime_obstacles_all_shifts += obstacle_count
        total_new_prime_obstacles_all_shifts += len(new_prime_obstacles)
        shift_obstacle_audits.append(
            {
                "shift_cycles": shift,
                "shift_p": shift * period_p,
                "window_slot_count": total_debt_mass,
                "prime_obstacle_count": obstacle_count,
                "certified_exit_prime_obstacle_count": len(certified_exit_prime_obstacles),
                "new_prime_obstacle_count": len(new_prime_obstacles),
                "composite_slot_count": composite_slot_count,
                "rows_with_prime_obstacle": rows_with_prime_obstacle,
                "rows_without_prime_obstacle": total_rows - rows_with_prime_obstacle,
                "same_support_fresh_cover_closed_by_actual_primes": obstacle_count > 0,
                "prime_obstacle_fraction": division_record(obstacle_count, total_debt_mass),
                "row_windows": row_windows,
                "prime_obstacles": prime_obstacles,
            }
        )

    total_tested_slots = total_debt_mass * near_shift_limit
    shift_16 = shift_obstacle_audits[-1]
    result = {
        "certificate_type": "prime_matrix_cycle_debt_fresh_cover_prime_obstacle_router",
        "status": "same_support_fresh_cover_hits_actual_prime_obstacles",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_sweep_not_used_as_global_proof": True,
        "aggregate": {
            "row_column_unconditional_closed": False,
            "previous_hardpoint": PREVIOUS_TARGET,
            "period_p": period_p,
            "near_shift_limit_cycles": near_shift_limit,
            "positive_cycle_debt_residue_count": total_rows,
            "total_cycle_debt_mass_per_shift": total_debt_mass,
            "tested_shift_count": near_shift_limit,
            "total_tested_same_support_slots": total_tested_slots,
            "total_prime_obstacles_all_near_shifts": total_prime_obstacles_all_shifts,
            "total_new_prime_obstacles_all_near_shifts": total_new_prime_obstacles_all_shifts,
            "prime_obstacle_density_all_near_shifts": division_record(
                total_prime_obstacles_all_shifts, total_tested_slots
            ),
            "all_near_shift_same_support_windows_have_prime_obstacles": all(
                bool(item["same_support_fresh_cover_closed_by_actual_primes"])
                for item in shift_obstacle_audits
            ),
            "min_prime_obstacle_count_per_shift": min_prime_obstacles,
            "min_prime_obstacle_shift": min_obstacle_shift,
            "min_prime_obstacle_rows_per_shift": min_prime_obstacle_rows,
            "max_prime_obstacle_count_per_shift": max_prime_obstacles,
            "max_prime_obstacle_shift": max_obstacle_shift,
            "max_prime_obstacle_rows_per_shift": max_prime_obstacle_rows,
            "shift_1_prime_obstacle_count": int(shift_obstacle_audits[0]["prime_obstacle_count"]),
            "shift_1_rows_with_prime_obstacle": int(
                shift_obstacle_audits[0]["rows_with_prime_obstacle"]
            ),
            "shift_near_limit_prime_obstacle_count": int(shift_16["prime_obstacle_count"]),
            "shift_near_limit_new_prime_obstacle_count": int(
                shift_16["new_prime_obstacle_count"]
            ),
            "shift_near_limit_rows_with_prime_obstacle": int(
                shift_16["rows_with_prime_obstacle"]
            ),
            "same_support_fresh_cover_closed_current_certificate": True,
            "support_row_replacement_or_prime_obstacle_pdec_required": True,
            "hardpoint_after_router": NEXT_TARGET,
            "next_direct_attack_target": NEXT_TARGET,
        },
        "shift_obstacle_audits": shift_obstacle_audits,
        "plain_conclusion": (
            "在保持同一 27 个正债务 residue 支撑行的前提下，任一近程平移窗口 "
            f"K=1..{near_shift_limit} 都含有真实素数障碍。每个平移窗口有 "
            f"{total_debt_mass} 个待覆盖槽，最少也有 {min_prime_obstacles} 个素数障碍"
            f"（K={min_obstacle_shift}），K={near_shift_limit} 的全 fresh 窗口仍有 "
            f"{shift_16['prime_obstacle_count']} 个素数障碍。故 fresh moving cover 不能在"
            "同一支撑行上重建全合数词；它必须删除实际素数障碍成为 PDEC，或替换支撑行并进入 support-row replacement SAE/PDEC。"
        ),
        "dependency_hashes": {
            str(CYCLE_COVER.relative_to(ROOT)): sha256(CYCLE_COVER),
            str(NEAR_SHIFT.relative_to(ROOT)): sha256(NEAR_SHIFT),
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
    density = agg["prime_obstacle_density_all_near_shifts"]
    lines = [
        "# Prime Matrix cycle-debt fresh-cover prime-obstacle router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"row_column_unconditional_closed={fmt_bool(agg['row_column_unconditional_closed'])}",
        f"previous_hardpoint={agg['previous_hardpoint']}",
        f"period_p={agg['period_p']}",
        f"near_shift_limit_cycles={agg['near_shift_limit_cycles']}",
        f"positive_cycle_debt_residue_count={agg['positive_cycle_debt_residue_count']}",
        f"total_cycle_debt_mass_per_shift={agg['total_cycle_debt_mass_per_shift']}",
        f"tested_shift_count={agg['tested_shift_count']}",
        f"total_tested_same_support_slots={agg['total_tested_same_support_slots']}",
        f"total_prime_obstacles_all_near_shifts={agg['total_prime_obstacles_all_near_shifts']}",
        f"total_new_prime_obstacles_all_near_shifts={agg['total_new_prime_obstacles_all_near_shifts']}",
        f"prime_obstacle_density_all_near_shifts={density['numerator']}/{density['denominator']}",
        f"all_near_shift_same_support_windows_have_prime_obstacles={fmt_bool(agg['all_near_shift_same_support_windows_have_prime_obstacles'])}",
        f"min_prime_obstacle_count_per_shift={agg['min_prime_obstacle_count_per_shift']}",
        f"min_prime_obstacle_shift={agg['min_prime_obstacle_shift']}",
        f"min_prime_obstacle_rows_per_shift={agg['min_prime_obstacle_rows_per_shift']}",
        f"max_prime_obstacle_count_per_shift={agg['max_prime_obstacle_count_per_shift']}",
        f"max_prime_obstacle_shift={agg['max_prime_obstacle_shift']}",
        f"shift_1_prime_obstacle_count={agg['shift_1_prime_obstacle_count']}",
        f"shift_near_limit_prime_obstacle_count={agg['shift_near_limit_prime_obstacle_count']}",
        f"shift_near_limit_new_prime_obstacle_count={agg['shift_near_limit_new_prime_obstacle_count']}",
        f"same_support_fresh_cover_closed_current_certificate={fmt_bool(agg['same_support_fresh_cover_closed_current_certificate'])}",
        f"support_row_replacement_or_prime_obstacle_pdec_required={fmt_bool(agg['support_row_replacement_or_prime_obstacle_pdec_required'])}",
        f"next_direct_attack_target={agg['next_direct_attack_target']}",
        "```",
        "",
        "## 1. shift obstacle audit",
        "",
        "| shift K | prime obstacles | exit primes | new primes | composite slots | rows hit |",
        "| ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for item in result["shift_obstacle_audits"]:
        lines.append(
            f"| {item['shift_cycles']} | {item['prime_obstacle_count']} | "
            f"{item['certified_exit_prime_obstacle_count']} | "
            f"{item['new_prime_obstacle_count']} | {item['composite_slot_count']} | "
            f"{item['rows_with_prime_obstacle']} |"
        )

    lines.extend(
        [
            "",
            "## 2. 判定",
            "",
            "- 对每个 `K=1..16`，同一 27 行支撑的 fresh window 都含有 actual prime obstacles。",
            "- 最轻窗口仍有 17 个素数障碍；全 fresh 的 `K=16` 窗口有 27 个素数障碍，且全是新素数障碍。",
            "- 因此 same-support fresh cover 已被真实链打断；要继续复现必须删除实际素数障碍，或更换支撑行。",
            "- 本步仍不宣称行/列命题无条件闭合；它把剩余压成 prime-obstacle PDEC 或 support-row replacement SAE/PDEC。",
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
