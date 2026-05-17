#!/usr/bin/env python3
"""生成 long-relief 的 71 周期相位债务证书。

用法示例：
  python3 experiments/prime_matrix_long_relief_cycle_debt_router.py
  python3 -m json.tool data/prime-matrix-long-relief-cycle-debt-ledger.json

输出：
  data/prime-matrix-long-relief-cycle-debt-ledger.json
  docs/monograph/prime-matrix-long-relief-cycle-debt-router.json
  docs/monograph/prime-matrix-long-relief-cycle-debt-router.md
"""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

PRIME_FILTER = DATA / "prime-matrix-two-residue-spare-prime-anchor-filter-ledger.json"
SATURATION = DATA / "prime-matrix-cross-carrier-fifty-unit-residue-saturation-ledger.json"
FULL_HORIZON = DATA / "prime-matrix-accepted-reset-full-relief-horizon-ledger.json"

OUT_LEDGER = DATA / "prime-matrix-long-relief-cycle-debt-ledger.json"
OUT_JSON = DOCS / "prime-matrix-long-relief-cycle-debt-router.json"
OUT_MD = DOCS / "prime-matrix-long-relief-cycle-debt-router.md"

PREVIOUS_TARGET = "AcceptedResetPDECExclusionOrLongReliefHorizonSupportMotionSAE"
NEXT_TARGET = "LongReliefCycleDebtPDECExclusionOrSupportMotionSAESummability"


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


def first_step_for_residue(
    residue: int,
    *,
    reset_step: int,
    ell: int,
    anchor_residue: int,
    increment: int,
) -> int:
    """求 reset 后第一个落到指定 residue 的同步步号。"""
    for step in range(reset_step, reset_step + ell):
        if (anchor_residue + increment * step) % ell == residue:
            return step
    raise RuntimeError(f"residue {residue} not found in one period")


def build_result() -> dict[str, Any]:
    """构造周期债务证书。"""
    filt = aggregate(PRIME_FILTER)
    sat = aggregate(SATURATION)
    horizon = aggregate(FULL_HORIZON)

    ell = int(filt["ell"])
    anchor_p = int(filt["support_anchor_p"])
    delay = int(filt["support_delay"])
    period_p = ell * delay
    anchor_residue = int(sat["anchor_residue_mod_ell"])
    increment = int(sat["increment_mod_ell"])
    reset_step = int(horizon["reset_step"])
    reset_p = int(horizon["reset_p"])
    full_step = int(horizon["full_relief_step"])
    full_p = int(horizon["full_relief_p"])

    missing = [int(value) for value in filt["prime_filtered_missing_nonzero_residues"]]
    debt_rows: list[dict[str, Any]] = []
    for residue in missing:
        formal_step = first_step_for_residue(
            residue,
            reset_step=reset_step,
            ell=ell,
            anchor_residue=anchor_residue,
            increment=increment,
        )
        formal_p = anchor_p + delay * formal_step
        composite_wait_rows: list[dict[str, Any]] = []
        first_prime_step = None
        first_prime_p = None
        cycle_delay = None
        for cycle in range(0, 1000):
            step = formal_step + cycle * ell
            p_value = anchor_p + delay * step
            factor = smallest_factor(p_value)
            if factor is None:
                first_prime_step = step
                first_prime_p = p_value
                cycle_delay = cycle
                break
            composite_wait_rows.append(
                {
                    "cycle": cycle,
                    "step": step,
                    "p": p_value,
                    "smallest_factor": factor,
                }
            )
        if first_prime_step is None or first_prime_p is None or cycle_delay is None:
            raise RuntimeError(f"no prime relief found for residue {residue}")
        debt_rows.append(
            {
                "residue": residue,
                "first_formal_step_after_reset": formal_step,
                "first_formal_p_after_reset": formal_p,
                "first_prime_step": first_prime_step,
                "first_prime_p": first_prime_p,
                "cycle_delay": cycle_delay,
                "p_delay_from_formal": first_prime_p - formal_p,
                "composite_wait_count": len(composite_wait_rows),
                "composite_wait_rows_sample": composite_wait_rows[:5],
            }
        )

    debt_rows.sort(key=lambda row: (-int(row["cycle_delay"]), int(row["residue"])))
    cycle_hist = Counter(int(row["cycle_delay"]) for row in debt_rows)
    positive_rows = [row for row in debt_rows if int(row["cycle_delay"]) > 0]
    max_row = debt_rows[0]
    total_cycle_debt = sum(int(row["cycle_delay"]) for row in debt_rows)
    result = {
        "certificate_type": "prime_matrix_long_relief_cycle_debt_router",
        "status": "long_relief_requires_explicit_ell_cycle_phase_debt",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_sweep_not_used_as_global_proof": True,
        "aggregate": {
            "row_column_unconditional_closed": False,
            "previous_hardpoint": PREVIOUS_TARGET,
            "ell": ell,
            "support_delay": delay,
            "period_p": period_p,
            "reset_step": reset_step,
            "reset_p": reset_p,
            "full_relief_step": full_step,
            "full_relief_p": full_p,
            "missing_nonzero_count": len(missing),
            "zero_cycle_relief_count": len(debt_rows) - len(positive_rows),
            "positive_cycle_debt_residue_count": len(positive_rows),
            "total_cycle_debt": total_cycle_debt,
            "total_composite_wait_count": sum(int(row["composite_wait_count"]) for row in debt_rows),
            "matches_full_horizon_composite_missing_count": total_cycle_debt
            == int(horizon["composite_missing_candidate_count_until_full_relief"]),
            "max_cycle_debt": int(max_row["cycle_delay"]),
            "max_cycle_debt_residue": int(max_row["residue"]),
            "max_cycle_debt_first_formal_p": int(max_row["first_formal_p_after_reset"]),
            "max_cycle_debt_first_prime_p": int(max_row["first_prime_p"]),
            "max_cycle_debt_p_delay": int(max_row["p_delay_from_formal"]),
            "cycle_debt_histogram": [
                {"cycle_delay": cycle, "count": count}
                for cycle, count in sorted(cycle_hist.items())
            ],
            "periods_touched_until_full_relief": (full_step - reset_step) // ell + 1,
            "hardpoint_after_router": NEXT_TARGET,
            "next_direct_attack_target": NEXT_TARGET,
        },
        "cycle_debt_rows": debt_rows,
        "plain_conclusion": (
            "long-relief 并非简单远端等待，而是固定 ell=71 周期上的显式相位债务："
            "35 个缺失 residue 中只有 8 个在 reset 后第一次相位命中即为素数，"
            "其余 27 个必须跨后续周期；总周期债务为 101，恰好等于 full-horizon "
            "中的 101 个合数形式命中。最大债务来自 residue=67，需要等待 15 个完整 "
            "71 周期才到 P=98047。"
        ),
        "dependency_hashes": {
            str(PRIME_FILTER.relative_to(ROOT)): sha256(PRIME_FILTER),
            str(SATURATION.relative_to(ROOT)): sha256(SATURATION),
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
    lines = [
        "# Prime Matrix long relief cycle debt router",
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
        f"missing_nonzero_count={agg['missing_nonzero_count']}",
        f"zero_cycle_relief_count={agg['zero_cycle_relief_count']}",
        f"positive_cycle_debt_residue_count={agg['positive_cycle_debt_residue_count']}",
        f"total_cycle_debt={agg['total_cycle_debt']}",
        f"total_composite_wait_count={agg['total_composite_wait_count']}",
        f"matches_full_horizon_composite_missing_count={fmt_bool(agg['matches_full_horizon_composite_missing_count'])}",
        f"max_cycle_debt={agg['max_cycle_debt']}",
        f"max_cycle_debt_residue={agg['max_cycle_debt_residue']}",
        f"max_cycle_debt_p_delay={agg['max_cycle_debt_p_delay']}",
        f"periods_touched_until_full_relief={agg['periods_touched_until_full_relief']}",
        f"next_direct_attack_target={agg['next_direct_attack_target']}",
        "```",
        "",
        "## 1. cycle-debt rows",
        "",
        "| residue | first formal P | first prime P | cycle debt | composite waits |",
        "| ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in result["cycle_debt_rows"]:
        lines.append(
            f"| {row['residue']} | {row['first_formal_p_after_reset']} | "
            f"{row['first_prime_p']} | {row['cycle_delay']} | {row['composite_wait_count']} |"
        )

    lines.extend(
        [
            "",
            "## 2. 判定",
            "",
            "- 每个 cycle debt 都是一整段 `71` 同 residue 周期的素数锚等待。",
            "- `total_cycle_debt=101` 与 full-horizon 账本中的合数形式命中数完全相等。",
            "- 最大单点债务是 `residue=67`，从首次形式命中到真实素数锚相差 `85200`。",
            "- 因此 long-relief 分支必须解释长期相位等待，而不是只解释 endpoint 外延。",
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
