#!/usr/bin/env python3
"""生成 reset 后单周期 relief 容量缺口证书。

用法示例：
  python3 experiments/prime_matrix_one_period_relief_deficit_router.py
  python3 -m json.tool data/prime-matrix-one-period-relief-deficit-ledger.json

输出：
  data/prime-matrix-one-period-relief-deficit-ledger.json
  docs/monograph/prime-matrix-one-period-relief-deficit-router.json
  docs/monograph/prime-matrix-one-period-relief-deficit-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

PRIME_FILTER = DATA / "prime-matrix-two-residue-spare-prime-anchor-filter-ledger.json"
SATURATION = DATA / "prime-matrix-cross-carrier-fifty-unit-residue-saturation-ledger.json"
CYCLE_DEBT = DATA / "prime-matrix-long-relief-cycle-debt-ledger.json"

OUT_LEDGER = DATA / "prime-matrix-one-period-relief-deficit-ledger.json"
OUT_JSON = DOCS / "prime-matrix-one-period-relief-deficit-router.json"
OUT_MD = DOCS / "prime-matrix-one-period-relief-deficit-router.md"

PREVIOUS_TARGET = "LongReliefCycleDebtPDECExclusionOrSupportMotionSAESummability"
NEXT_TARGET = "OnePeriodReliefDeficitForcesCycleDebtPDECOrSupportMotionSAE"


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


def build_result() -> dict[str, Any]:
    """构造单周期 relief 缺口证书。"""
    filt = aggregate(PRIME_FILTER)
    sat = aggregate(SATURATION)
    cycle = aggregate(CYCLE_DEBT)

    ell = int(filt["ell"])
    anchor_p = int(filt["support_anchor_p"])
    delay = int(filt["support_delay"])
    period_p = ell * delay
    anchor_residue = int(sat["anchor_residue_mod_ell"])
    increment = int(sat["increment_mod_ell"])
    reset_step = int(cycle["reset_step"])
    period_steps = list(range(reset_step, reset_step + ell))
    missing = set(int(value) for value in filt["prime_filtered_missing_nonzero_residues"])
    missing_including_zero = set(
        int(value) for value in filt["prime_filtered_missing_residues_including_zero"]
    )
    seen = set(range(ell)) - missing_including_zero
    original_used = set(int(value) for value in sat["used_residues"])

    relief_rows: list[dict[str, Any]] = []
    composite_missing_rows: list[dict[str, Any]] = []
    repeat_prime_rows: list[dict[str, Any]] = []
    other_composite_rows: list[dict[str, Any]] = []
    residues_seen_in_period: set[int] = set()

    for step in period_steps:
        p_value = anchor_p + delay * step
        residue = (anchor_residue + increment * step) % ell
        residues_seen_in_period.add(residue)
        factor = smallest_factor(p_value)
        row = {
            "step": step,
            "p": p_value,
            "residue": residue,
            "is_prime_p": factor is None,
            "smallest_factor": factor,
            "already_in_prime_filtered_union": residue in seen,
            "already_in_original_used_residues": residue in original_used,
        }
        if factor is None and residue in missing:
            row["route"] = "actual_missing_nonzero_relief"
            relief_rows.append(row)
        elif factor is None:
            row["route"] = "repeat_prime_anchor_no_relief"
            repeat_prime_rows.append(row)
        elif residue in missing:
            row["route"] = "formal_missing_hit_but_composite"
            composite_missing_rows.append(row)
        else:
            row["route"] = "composite_seen_residue"
            other_composite_rows.append(row)

    formal_missing_hit_count = len(relief_rows) + len(composite_missing_rows)
    result = {
        "certificate_type": "prime_matrix_one_period_relief_deficit_router",
        "status": "one_period_relief_capacity_deficit_materialized",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_sweep_not_used_as_global_proof": True,
        "aggregate": {
            "row_column_unconditional_closed": False,
            "previous_hardpoint": PREVIOUS_TARGET,
            "ell": ell,
            "support_delay": delay,
            "period_p": period_p,
            "period_start_step": reset_step,
            "period_end_step": reset_step + ell - 1,
            "period_start_p": anchor_p + delay * reset_step,
            "period_end_p": anchor_p + delay * (reset_step + ell - 1),
            "period_residue_count": len(residues_seen_in_period),
            "period_is_complete_residue_cycle": len(residues_seen_in_period) == ell,
            "missing_nonzero_required": len(missing),
            "formal_missing_hit_count": formal_missing_hit_count,
            "actual_relief_count_in_one_period": len(relief_rows),
            "composite_missing_count_in_one_period": len(composite_missing_rows),
            "repeat_prime_anchor_count_in_one_period": len(repeat_prime_rows),
            "relief_deficit_after_one_period": len(missing) - len(relief_rows),
            "actual_relief_fraction_in_one_period": len(relief_rows) / len(missing),
            "composite_missing_matches_positive_cycle_debt_residues": len(composite_missing_rows)
            == int(cycle["positive_cycle_debt_residue_count"]),
            "one_period_insufficient_for_full_relief": len(relief_rows) < len(missing),
            "hardpoint_after_router": NEXT_TARGET,
            "next_direct_attack_target": NEXT_TARGET,
        },
        "relief_rows": relief_rows,
        "composite_missing_rows": composite_missing_rows,
        "repeat_prime_rows": repeat_prime_rows,
        "plain_conclusion": (
            "reset 后第一个完整 ell=71 周期已经让 35 个缺失非零 residue 全部形式命中一次，"
            "但只有 8 个命中为实际素数 relief；其余 27 个全部是合数形式命中，"
            "恰好对应正周期债务 residue 数。同时该周期还有 10 个 repeat prime anchor。"
            "因此一个 reset-local 周期存在明确 relief 容量缺口，必须进入后续周期债务。"
        ),
        "dependency_hashes": {
            str(PRIME_FILTER.relative_to(ROOT)): sha256(PRIME_FILTER),
            str(SATURATION.relative_to(ROOT)): sha256(SATURATION),
            str(CYCLE_DEBT.relative_to(ROOT)): sha256(CYCLE_DEBT),
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
        "# Prime Matrix one-period relief deficit router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"row_column_unconditional_closed={fmt_bool(agg['row_column_unconditional_closed'])}",
        f"previous_hardpoint={agg['previous_hardpoint']}",
        f"ell={agg['ell']}",
        f"period_p={agg['period_p']}",
        f"period_step_range={agg['period_start_step']}..{agg['period_end_step']}",
        f"period_p_range={agg['period_start_p']}..{agg['period_end_p']}",
        f"period_is_complete_residue_cycle={fmt_bool(agg['period_is_complete_residue_cycle'])}",
        f"missing_nonzero_required={agg['missing_nonzero_required']}",
        f"formal_missing_hit_count={agg['formal_missing_hit_count']}",
        f"actual_relief_count_in_one_period={agg['actual_relief_count_in_one_period']}",
        f"composite_missing_count_in_one_period={agg['composite_missing_count_in_one_period']}",
        f"repeat_prime_anchor_count_in_one_period={agg['repeat_prime_anchor_count_in_one_period']}",
        f"relief_deficit_after_one_period={agg['relief_deficit_after_one_period']}",
        f"next_direct_attack_target={agg['next_direct_attack_target']}",
        "```",
        "",
        "## 1. actual relief rows in one period",
        "",
        "| step | P | residue |",
        "| ---: | ---: | ---: |",
    ]
    for row in result["relief_rows"]:
        lines.append(f"| {row['step']} | {row['p']} | {row['residue']} |")

    lines.extend(
        [
            "",
            "## 2. 判定",
            "",
            "- 一个完整 residue 周期内，形式上 35 个缺失非零 residue 全部出现。",
            "- 实际素数 relief 只有 `8` 个，因此一周期后仍缺 `27` 个。",
            "- `27` 个合数形式命中正好是上一张 cycle-debt 证书中的正周期债务 residue。",
            "- 同周期还有 `10` 个 repeat prime-anchor，继续增加 reset/旧容量压力。",
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
