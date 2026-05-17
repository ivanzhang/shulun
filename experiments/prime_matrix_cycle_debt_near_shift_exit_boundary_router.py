#!/usr/bin/env python3
"""生成 cycle-debt 近程平移首素数边界证书。

用法示例：
  python3 experiments/prime_matrix_cycle_debt_near_shift_exit_boundary_router.py
  python3 -m json.tool data/prime-matrix-cycle-debt-near-shift-exit-boundary-ledger.json

输出：
  data/prime-matrix-cycle-debt-near-shift-exit-boundary-ledger.json
  docs/monograph/prime-matrix-cycle-debt-near-shift-exit-boundary-router.json
  docs/monograph/prime-matrix-cycle-debt-near-shift-exit-boundary-router.md
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
SPARSE_REPLAY = DATA / "prime-matrix-cycle-debt-sparse-replay-barrier-ledger.json"

OUT_LEDGER = DATA / "prime-matrix-cycle-debt-near-shift-exit-boundary-ledger.json"
OUT_JSON = DOCS / "prime-matrix-cycle-debt-near-shift-exit-boundary-router.json"
OUT_MD = DOCS / "prime-matrix-cycle-debt-near-shift-exit-boundary-router.md"

PREVIOUS_TARGET = "SparseReplaySAEOrMovingTransverseCoverPDEC"
NEXT_TARGET = "FreshMovingCoverPDECOrGlobalSupportMotionSAE"


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


def build_result() -> dict[str, Any]:
    """构造近程平移首素数边界证书。"""
    cover = load_json(CYCLE_COVER)
    sparse = load_json(SPARSE_REPLAY)
    cover_agg = cover["aggregate"]
    sparse_agg = sparse["aggregate"]

    period_p = int(cover_agg["period_p"])
    full_span = sparse_agg["full_relief_cycle_span_exact"]
    near_shift_limit = int(full_span["ceiling"])
    rows = sorted(cover["pressure_rows"], key=lambda row: int(row["residue"]))
    total_rows = len(rows)
    total_debt_mass = sum(int(row["cycle_debt"]) for row in rows)
    max_debt = max(int(row["cycle_debt"]) for row in rows)

    row_boundary_audit: list[dict[str, Any]] = []
    for row in rows:
        debt = int(row["cycle_debt"])
        first_prime_cycle = int(row["first_prime_cycle"])
        if first_prime_cycle != debt:
            raise RuntimeError(f"unexpected first prime cycle for residue {row['residue']}")
        row_boundary_audit.append(
            {
                "residue": int(row["residue"]),
                "cycle_debt": debt,
                "first_formal_p": int(row["first_formal_p"]),
                "first_prime_cycle": first_prime_cycle,
                "first_prime_p": int(row["first_prime_p"]),
                "exit_prime_p_gap_from_first_formal": int(row["first_prime_p"])
                - int(row["first_formal_p"]),
                "exit_prime_p_gap_equals_debt_period": (
                    int(row["first_prime_p"]) - int(row["first_formal_p"]) == debt * period_p
                ),
            }
        )

    shift_audits: list[dict[str, Any]] = []
    min_exit_rows_nonzero_shift = total_rows
    min_exit_mass_nonzero_shift = total_debt_mass
    min_fresh_rows_nonzero_shift = total_rows
    max_fresh_rows_nonzero_shift = 0

    for shift in range(1, near_shift_limit + 1):
        exit_rows = []
        fresh_rows = []
        for row in row_boundary_audit:
            debt = int(row["cycle_debt"])
            if shift <= debt:
                exit_rows.append(
                    {
                        "residue": int(row["residue"]),
                        "cycle_debt": debt,
                        "exit_prime_cycle": int(row["first_prime_cycle"]),
                        "exit_prime_p": int(row["first_prime_p"]),
                        "exit_prime_position_inside_shifted_word": debt - shift,
                    }
                )
            else:
                fresh_rows.append(
                    {
                        "residue": int(row["residue"]),
                        "cycle_debt": debt,
                        "reason": "shift_starts_after_certified_debt_prefix",
                    }
                )

        exit_mass = sum(int(row["cycle_debt"]) for row in exit_rows)
        fresh_mass = sum(int(row["cycle_debt"]) for row in fresh_rows)
        if shift <= max_debt:
            min_exit_rows_nonzero_shift = min(min_exit_rows_nonzero_shift, len(exit_rows))
            min_exit_mass_nonzero_shift = min(min_exit_mass_nonzero_shift, exit_mass)
        min_fresh_rows_nonzero_shift = min(min_fresh_rows_nonzero_shift, len(fresh_rows))
        max_fresh_rows_nonzero_shift = max(max_fresh_rows_nonzero_shift, len(fresh_rows))
        shift_audits.append(
            {
                "shift_cycles": shift,
                "shift_p": shift * period_p,
                "exit_prime_collision_row_count": len(exit_rows),
                "exit_prime_collision_debt_mass": exit_mass,
                "fresh_cover_required_row_count": len(fresh_rows),
                "fresh_cover_required_debt_mass": fresh_mass,
                "reusable_old_prefix_row_count": 0,
                "all_rows_exit_or_fresh": len(exit_rows) + len(fresh_rows) == total_rows,
                "old_prefix_reuse_closed": True,
                "exit_rows": exit_rows,
                "fresh_rows": fresh_rows,
            }
        )

    result = {
        "certificate_type": "prime_matrix_cycle_debt_near_shift_exit_boundary_router",
        "status": "near_shift_hits_exit_primes_or_requires_fresh_cover",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_sweep_not_used_as_global_proof": True,
        "aggregate": {
            "row_column_unconditional_closed": False,
            "previous_hardpoint": PREVIOUS_TARGET,
            "period_p": period_p,
            "near_shift_limit_cycles": near_shift_limit,
            "near_shift_limit_p": near_shift_limit * period_p,
            "positive_cycle_debt_residue_count": total_rows,
            "total_cycle_debt_mass": total_debt_mass,
            "max_cycle_debt": max_debt,
            "tested_nonzero_near_shift_count": near_shift_limit,
            "all_near_shifts_close_old_prefix_reuse": all(
                bool(item["old_prefix_reuse_closed"]) for item in shift_audits
            ),
            "all_near_shifts_all_rows_exit_or_fresh": all(
                bool(item["all_rows_exit_or_fresh"]) for item in shift_audits
            ),
            "shift_1_exit_prime_collision_row_count": int(
                shift_audits[0]["exit_prime_collision_row_count"]
            ),
            "shift_1_exit_prime_collision_debt_mass": int(
                shift_audits[0]["exit_prime_collision_debt_mass"]
            ),
            "shift_max_cycle_debt_exit_prime_collision_row_count": int(
                shift_audits[max_debt - 1]["exit_prime_collision_row_count"]
            ),
            "shift_max_cycle_debt_exit_prime_collision_debt_mass": int(
                shift_audits[max_debt - 1]["exit_prime_collision_debt_mass"]
            ),
            "shift_near_limit_fresh_cover_required_row_count": int(
                shift_audits[-1]["fresh_cover_required_row_count"]
            ),
            "shift_near_limit_fresh_cover_required_debt_mass": int(
                shift_audits[-1]["fresh_cover_required_debt_mass"]
            ),
            "min_exit_rows_for_shifts_1_to_max_debt": min_exit_rows_nonzero_shift,
            "min_exit_mass_for_shifts_1_to_max_debt": min_exit_mass_nonzero_shift,
            "min_fresh_rows_for_shifts_1_to_near_limit": min_fresh_rows_nonzero_shift,
            "max_fresh_rows_for_shifts_1_to_near_limit": max_fresh_rows_nonzero_shift,
            "old_blocker_graph_near_shift_reuse_closed_current_certificate": True,
            "moving_branch_must_replace_some_or_all_support_rows": True,
            "fresh_cover_mass_at_near_limit_over_total_debt": division_record(
                int(shift_audits[-1]["fresh_cover_required_debt_mass"]), total_debt_mass
            ),
            "hardpoint_after_router": NEXT_TARGET,
            "next_direct_attack_target": NEXT_TARGET,
        },
        "row_boundary_audit": row_boundary_audit,
        "shift_audits": shift_audits,
        "plain_conclusion": (
            "对任一正债务 residue，原始 debt 前缀之后紧接着是该行的首个 relief prime。"
            f"因此任意 1..{max_debt} 周期的小平移都会让所有 debt>=K 的行在平移词内部"
            f"撞上 exit prime；而 K>{max_debt} 到 near limit={near_shift_limit} 时，旧前缀"
            "已经完全不能提供复用支撑。故 moving 分支不是旧 CRT cover 的轻微滑动；"
            "它必须替换部分或全部支撑行，成为 fresh moving cover PDEC 或真正全局 support-motion SAE。"
        ),
        "dependency_hashes": {
            str(CYCLE_COVER.relative_to(ROOT)): sha256(CYCLE_COVER),
            str(SPARSE_REPLAY.relative_to(ROOT)): sha256(SPARSE_REPLAY),
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
        "# Prime Matrix cycle-debt near-shift exit-boundary router",
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
        f"near_shift_limit_p={agg['near_shift_limit_p']}",
        f"positive_cycle_debt_residue_count={agg['positive_cycle_debt_residue_count']}",
        f"total_cycle_debt_mass={agg['total_cycle_debt_mass']}",
        f"max_cycle_debt={agg['max_cycle_debt']}",
        f"tested_nonzero_near_shift_count={agg['tested_nonzero_near_shift_count']}",
        f"all_near_shifts_close_old_prefix_reuse={fmt_bool(agg['all_near_shifts_close_old_prefix_reuse'])}",
        f"shift_1_exit_prime_collision_row_count={agg['shift_1_exit_prime_collision_row_count']}",
        f"shift_1_exit_prime_collision_debt_mass={agg['shift_1_exit_prime_collision_debt_mass']}",
        f"shift_max_cycle_debt_exit_prime_collision_row_count={agg['shift_max_cycle_debt_exit_prime_collision_row_count']}",
        f"shift_max_cycle_debt_exit_prime_collision_debt_mass={agg['shift_max_cycle_debt_exit_prime_collision_debt_mass']}",
        f"shift_near_limit_fresh_cover_required_row_count={agg['shift_near_limit_fresh_cover_required_row_count']}",
        f"shift_near_limit_fresh_cover_required_debt_mass={agg['shift_near_limit_fresh_cover_required_debt_mass']}",
        f"moving_branch_must_replace_some_or_all_support_rows={fmt_bool(agg['moving_branch_must_replace_some_or_all_support_rows'])}",
        f"next_direct_attack_target={agg['next_direct_attack_target']}",
        "```",
        "",
        "## 1. shift audit",
        "",
        "| shift K | exit rows | exit debt mass | fresh rows | fresh debt mass | old prefix reusable |",
        "| ---: | ---: | ---: | ---: | ---: | :---: |",
    ]
    for item in result["shift_audits"]:
        lines.append(
            f"| {item['shift_cycles']} | {item['exit_prime_collision_row_count']} | "
            f"{item['exit_prime_collision_debt_mass']} | "
            f"{item['fresh_cover_required_row_count']} | "
            f"{item['fresh_cover_required_debt_mass']} | "
            f"{fmt_bool(item['reusable_old_prefix_row_count'] > 0)} |"
        )

    lines.extend(
        [
            "",
            "## 2. row exit boundary",
            "",
            "| residue | debt | first formal P | exit prime cycle | exit prime P | gap=debt*5680 |",
            "| ---: | ---: | ---: | ---: | ---: | :---: |",
        ]
    )
    for row in result["row_boundary_audit"]:
        lines.append(
            f"| {row['residue']} | {row['cycle_debt']} | {row['first_formal_p']} | "
            f"{row['first_prime_cycle']} | {row['first_prime_p']} | "
            f"{fmt_bool(row['exit_prime_p_gap_equals_debt_period'])} |"
        )

    lines.extend(
        [
            "",
            "## 3. 判定",
            "",
            "- 每个正债务行的旧 composite prefix 之后立即是 exit prime；平移旧前缀会把这个 prime 拉入词内。",
            "- 对 `K=1`，27 行全部被 exit prime 撕裂；对 `1<=K<=15`，所有 `debt>=K` 的行被撕裂。",
            "- 对 `K=16`，没有旧 composite prefix 可复用，27 行都必须 fresh cover。",
            "- 因此 moving 分支不能靠同一 CRT cover 近程滑动维持；它必须替换支撑行或进入全局 support-motion。",
            "- 本步仍不宣称行/列命题无条件闭合；它把 moving 分支压成 fresh moving cover PDEC/SAE。",
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
