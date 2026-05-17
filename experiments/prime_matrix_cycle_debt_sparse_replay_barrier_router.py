#!/usr/bin/env python3
"""生成 cycle-debt 稀疏复现屏障证书。

用法示例：
  python3 experiments/prime_matrix_cycle_debt_sparse_replay_barrier_router.py
  python3 -m json.tool data/prime-matrix-cycle-debt-sparse-replay-barrier-ledger.json

输出：
  data/prime-matrix-cycle-debt-sparse-replay-barrier-ledger.json
  docs/monograph/prime-matrix-cycle-debt-sparse-replay-barrier-router.json
  docs/monograph/prime-matrix-cycle-debt-sparse-replay-barrier-router.md
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

TRANSVERSE = DATA / "prime-matrix-cycle-debt-transverse-crt-independence-ledger.json"
CYCLE_COVER = DATA / "prime-matrix-cycle-debt-crt-cover-pressure-ledger.json"
FULL_HORIZON = DATA / "prime-matrix-accepted-reset-full-relief-horizon-ledger.json"

OUT_LEDGER = DATA / "prime-matrix-cycle-debt-sparse-replay-barrier-ledger.json"
OUT_JSON = DOCS / "prime-matrix-cycle-debt-sparse-replay-barrier-router.json"
OUT_MD = DOCS / "prime-matrix-cycle-debt-sparse-replay-barrier-router.md"

PREVIOUS_TARGET = "TransverseCRTCoverPDECExclusionOrGlobalSupportMotionSAE"
NEXT_TARGET = "SparseReplaySAEOrMovingTransverseCoverPDEC"


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
        "log10_ratio": math.log10(numerator) - math.log10(denominator),
    }


def build_result() -> dict[str, Any]:
    """构造稀疏复现屏障证书。"""
    transverse = load_json(TRANSVERSE)
    cover = load_json(CYCLE_COVER)
    horizon = load_json(FULL_HORIZON)

    trans_agg = transverse["aggregate"]
    cover_agg = cover["aggregate"]
    horizon_agg = horizon["aggregate"]

    period_p = int(trans_agg["period_p"])
    ell = int(cover_agg["ell"])
    global_lcm = int(trans_agg["global_blocker_lcm"])
    combined_period = int(trans_agg["combined_period_lcm_period_p_and_blocker_lcm"])
    total_waits = int(trans_agg["total_composite_waits"])
    max_debt = int(trans_agg["max_row_cycle_debt"])
    full_step_gap = int(horizon_agg["full_relief_step_gap_after_reset"])
    full_p_gap = int(horizon_agg["full_relief_p_gap_after_reset"])
    full_cycle_span_floor, full_cycle_span_remainder = divmod(full_step_gap, ell)
    full_cycle_span_ceiling = full_cycle_span_floor + int(full_cycle_span_remainder > 0)
    full_cycle_span_exact_num = full_step_gap
    full_cycle_span_exact_den = ell

    row_replay_audits: list[dict[str, Any]] = []
    rows_with_single_copy_in_full_horizon = 0
    rows_with_replay_modulus_exceeding_total_waits = 0
    rows_with_replay_modulus_exceeding_own_debt = 0

    for row in transverse["row_audits"]:
        row_lcm = int(row["row_blocker_lcm"])
        debt = int(row["cycle_debt"])
        dead_gap = max(row_lcm - debt, 0)
        if row_lcm > full_cycle_span_ceiling:
            rows_with_single_copy_in_full_horizon += 1
        if row_lcm > total_waits:
            rows_with_replay_modulus_exceeding_total_waits += 1
        if row_lcm > debt:
            rows_with_replay_modulus_exceeding_own_debt += 1
        row_replay_audits.append(
            {
                "residue": int(row["residue"]),
                "cycle_debt": debt,
                "row_exact_replay_cycle_modulus": row_lcm,
                "row_dead_gap_cycles_after_support": dead_gap,
                "row_exact_replay_p_gap": row_lcm * period_p,
                "row_dead_gap_p_after_support": dead_gap * period_p,
                "single_copy_in_full_relief_horizon": row_lcm > full_cycle_span_ceiling,
                "row_modulus_over_own_debt": division_record(row_lcm, debt),
                "row_modulus_over_full_cycle_span_ceiling": division_record(row_lcm, full_cycle_span_ceiling),
            }
        )

    row_replay_audits.sort(
        key=lambda item: (-int(item["row_exact_replay_cycle_modulus"]), int(item["residue"]))
    )

    global_dead_gap_cycles = global_lcm - max_debt
    result = {
        "certificate_type": "prime_matrix_cycle_debt_sparse_replay_barrier_router",
        "status": "exact_transverse_crt_replay_is_sparse_or_moving_pdec",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_sweep_not_used_as_global_proof": True,
        "aggregate": {
            "row_column_unconditional_closed": False,
            "previous_hardpoint": PREVIOUS_TARGET,
            "period_p": period_p,
            "ell": ell,
            "global_exact_replay_cycle_modulus": global_lcm,
            "global_exact_replay_p_gap": combined_period,
            "global_exact_replay_density_log10": -math.log10(global_lcm),
            "max_cycle_debt_support_width": max_debt,
            "total_composite_wait_width": total_waits,
            "full_relief_step_gap_after_reset": full_step_gap,
            "full_relief_cycle_span_exact": {
                "numerator": full_cycle_span_exact_num,
                "denominator": full_cycle_span_exact_den,
                "floor": full_cycle_span_floor,
                "remainder": full_cycle_span_remainder,
                "ceiling": full_cycle_span_ceiling,
            },
            "full_relief_p_gap_after_reset": full_p_gap,
            "global_dead_gap_cycles_after_debt_word": global_dead_gap_cycles,
            "global_dead_gap_p_after_debt_word": global_dead_gap_cycles * period_p,
            "global_modulus_over_max_debt_width": division_record(global_lcm, max_debt),
            "global_modulus_over_total_wait_width": division_record(global_lcm, total_waits),
            "global_modulus_over_full_cycle_span_ceiling": division_record(
                global_lcm, full_cycle_span_ceiling
            ),
            "global_p_gap_over_full_relief_p_gap": division_record(combined_period, full_p_gap),
            "single_full_debt_copy_per_full_relief_horizon": global_lcm > full_cycle_span_ceiling,
            "single_full_debt_copy_per_any_window_shorter_than_global_modulus": True,
            "rows_with_replay_modulus_exceeding_own_debt": rows_with_replay_modulus_exceeding_own_debt,
            "rows_with_replay_modulus_exceeding_total_waits": rows_with_replay_modulus_exceeding_total_waits,
            "rows_with_single_copy_in_full_horizon": rows_with_single_copy_in_full_horizon,
            "positive_cycle_debt_residue_count": int(trans_agg["positive_cycle_debt_residue_count"]),
            "exact_replay_branch_is_sae_sparse_current_certificate": True,
            "non_sparse_persistence_forces_moving_blocker_map": True,
            "hardpoint_after_router": NEXT_TARGET,
            "next_direct_attack_target": NEXT_TARGET,
        },
        "row_replay_audits": row_replay_audits,
        "plain_conclusion": (
            "横向 CRT cover 若保持同一阻断图 exact replay，则完整 debt word 的下一次复现"
            f"必须相隔 {global_lcm} 个 residue 周期，即 P 距离 {combined_period}。"
            f"而当前 full-relief 可见跨度只有 {full_step_gap}/{ell} 个周期，向上取整为 "
            f"{full_cycle_span_ceiling}。因此任意短于 global_lcm 的局部/中程 support-motion "
            "窗口至多包含一份完整复本；exact 分支是稀疏 SAE 型。若反例链需要高频复现，"
            "就不能保持同一 CRT cover，而必须移动阻断素因子或相位类，进入 moving transverse cover PDEC。"
        ),
        "dependency_hashes": {
            str(TRANSVERSE.relative_to(ROOT)): sha256(TRANSVERSE),
            str(CYCLE_COVER.relative_to(ROOT)): sha256(CYCLE_COVER),
            str(FULL_HORIZON.relative_to(ROOT)): sha256(FULL_HORIZON),
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
    full_span = agg["full_relief_cycle_span_exact"]
    ratio_max = agg["global_modulus_over_max_debt_width"]
    ratio_total = agg["global_modulus_over_total_wait_width"]
    ratio_full = agg["global_modulus_over_full_cycle_span_ceiling"]
    ratio_p = agg["global_p_gap_over_full_relief_p_gap"]

    lines = [
        "# Prime Matrix cycle-debt sparse replay barrier router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"row_column_unconditional_closed={fmt_bool(agg['row_column_unconditional_closed'])}",
        f"previous_hardpoint={agg['previous_hardpoint']}",
        f"period_p={agg['period_p']}",
        f"ell={agg['ell']}",
        f"global_exact_replay_cycle_modulus={agg['global_exact_replay_cycle_modulus']}",
        f"global_exact_replay_p_gap={agg['global_exact_replay_p_gap']}",
        f"global_exact_replay_density_log10={agg['global_exact_replay_density_log10']:.12f}",
        f"max_cycle_debt_support_width={agg['max_cycle_debt_support_width']}",
        f"total_composite_wait_width={agg['total_composite_wait_width']}",
        f"full_relief_step_gap_after_reset={agg['full_relief_step_gap_after_reset']}",
        f"full_relief_cycle_span={full_span['numerator']}/{full_span['denominator']}",
        f"full_relief_cycle_span_ceiling={full_span['ceiling']}",
        f"global_dead_gap_cycles_after_debt_word={agg['global_dead_gap_cycles_after_debt_word']}",
        f"global_modulus_over_max_debt_width_floor={ratio_max['floor']}",
        f"global_modulus_over_total_wait_width_floor={ratio_total['floor']}",
        f"global_modulus_over_full_cycle_span_ceiling_floor={ratio_full['floor']}",
        f"global_p_gap_over_full_relief_p_gap_floor={ratio_p['floor']}",
        f"single_full_debt_copy_per_full_relief_horizon={fmt_bool(agg['single_full_debt_copy_per_full_relief_horizon'])}",
        f"rows_with_replay_modulus_exceeding_own_debt={agg['rows_with_replay_modulus_exceeding_own_debt']}",
        f"rows_with_replay_modulus_exceeding_total_waits={agg['rows_with_replay_modulus_exceeding_total_waits']}",
        f"rows_with_single_copy_in_full_horizon={agg['rows_with_single_copy_in_full_horizon']}",
        f"exact_replay_branch_is_sae_sparse_current_certificate={fmt_bool(agg['exact_replay_branch_is_sae_sparse_current_certificate'])}",
        f"non_sparse_persistence_forces_moving_blocker_map={fmt_bool(agg['non_sparse_persistence_forces_moving_blocker_map'])}",
        f"next_direct_attack_target={agg['next_direct_attack_target']}",
        "```",
        "",
        "## 1. row replay audit",
        "",
        "| residue | debt | replay modulus | dead gap cycles | replay P gap | single in full horizon |",
        "| ---: | ---: | ---: | ---: | ---: | :---: |",
    ]
    for row in result["row_replay_audits"]:
        lines.append(
            f"| {row['residue']} | {row['cycle_debt']} | "
            f"{row['row_exact_replay_cycle_modulus']} | "
            f"{row['row_dead_gap_cycles_after_support']} | "
            f"{row['row_exact_replay_p_gap']} | "
            f"{fmt_bool(row['single_copy_in_full_relief_horizon'])} |"
        )

    lines.extend(
        [
            "",
            "## 2. 判定",
            "",
            "- exact replay 保持同一阻断图时，完整 debt word 的平移量必须是全局横向 lcm 的倍数。",
            "- 当前 full-relief horizon 只有 `ceil(1102/71)=16` 个 residue 周期；完整复现间距远超该窗口。",
            "- 因此 exact 分支只能作为孤立稀疏复本计入 SAE；它不能提供高频容量补偿。",
            "- 若反例链要求在短窗口或正密度中持续复现，就必须改变阻断素因子、阻断相位或行组合，形成 moving transverse cover PDEC。",
            "- 本步仍不宣称行/列命题无条件闭合；它把剩余压成 sparse SAE 与 moving-cover PDEC 的二分。",
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
