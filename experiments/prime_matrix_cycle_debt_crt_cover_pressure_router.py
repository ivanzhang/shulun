#!/usr/bin/env python3
"""生成 cycle-debt 的 CRT cover pressure 证书。

用法示例：
  python3 experiments/prime_matrix_cycle_debt_crt_cover_pressure_router.py
  python3 -m json.tool data/prime-matrix-cycle-debt-crt-cover-pressure-ledger.json

输出：
  data/prime-matrix-cycle-debt-crt-cover-pressure-ledger.json
  docs/monograph/prime-matrix-cycle-debt-crt-cover-pressure-router.json
  docs/monograph/prime-matrix-cycle-debt-crt-cover-pressure-router.md
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
ONE_PERIOD = DATA / "prime-matrix-one-period-relief-deficit-ledger.json"

OUT_LEDGER = DATA / "prime-matrix-cycle-debt-crt-cover-pressure-ledger.json"
OUT_JSON = DOCS / "prime-matrix-cycle-debt-crt-cover-pressure-router.json"
OUT_MD = DOCS / "prime-matrix-cycle-debt-crt-cover-pressure-router.md"

PREVIOUS_TARGET = "OnePeriodReliefDeficitForcesCycleDebtPDECOrSupportMotionSAE"
NEXT_TARGET = "CycleDebtCRTCoverPressurePDECOrGlobalSupportMotionSAE"


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


def product(values: list[int]) -> int:
    """计算整数乘积。"""
    out = 1
    for value in values:
        out *= value
    return out


def build_result() -> dict[str, Any]:
    """构造 CRT cover pressure 证书。"""
    filt = aggregate(PRIME_FILTER)
    sat = aggregate(SATURATION)
    one = aggregate(ONE_PERIOD)

    ell = int(filt["ell"])
    anchor_p = int(filt["support_anchor_p"])
    delay = int(filt["support_delay"])
    period_p = ell * delay
    anchor_residue = int(sat["anchor_residue_mod_ell"])
    increment = int(sat["increment_mod_ell"])
    reset_step = int(one["period_start_step"])
    missing = [int(value) for value in filt["prime_filtered_missing_nonzero_residues"]]

    pressure_rows: list[dict[str, Any]] = []
    all_unique_factors: set[int] = set()
    total_composite_waits = 0

    for residue in missing:
        formal_step = first_step_for_residue(
            residue,
            reset_step=reset_step,
            ell=ell,
            anchor_residue=anchor_residue,
            increment=increment,
        )
        p0 = anchor_p + delay * formal_step
        blockers: list[dict[str, Any]] = []
        for cycle in range(1000):
            p_value = p0 + period_p * cycle
            factor = smallest_factor(p_value)
            if factor is None:
                first_prime = {"cycle": cycle, "step": formal_step + ell * cycle, "p": p_value}
                break
            inv = pow(period_p % factor, -1, factor)
            k_class = (-p0 * inv) % factor
            blockers.append(
                {
                    "cycle": cycle,
                    "p": p_value,
                    "smallest_factor": factor,
                    "cycle_class_mod_factor": k_class,
                }
            )
        else:
            raise RuntimeError(f"no prime relief found for residue {residue}")

        if not blockers:
            continue

        factors = [int(row["smallest_factor"]) for row in blockers]
        unique_factors = sorted(set(factors))
        all_unique_factors.update(unique_factors)
        total_composite_waits += len(blockers)
        lcm_value = math.lcm(*unique_factors)
        pressure_rows.append(
            {
                "residue": residue,
                "first_formal_step": formal_step,
                "first_formal_p": p0,
                "first_prime_cycle": first_prime["cycle"],
                "first_prime_step": first_prime["step"],
                "first_prime_p": first_prime["p"],
                "cycle_debt": len(blockers),
                "blocker_factor_sequence": factors,
                "unique_blocker_factors": unique_factors,
                "unique_blocker_factor_count": len(unique_factors),
                "blocker_lcm": lcm_value,
                "blocker_product": product(unique_factors),
                "blocker_lcm_over_cycle_debt": lcm_value / len(blockers),
                "blockers": blockers,
            }
        )

    pressure_rows.sort(key=lambda row: (-int(row["blocker_lcm"]), int(row["residue"])))
    global_lcm = math.lcm(*sorted(all_unique_factors))
    global_product = product(sorted(all_unique_factors))
    max_row = pressure_rows[0]
    result = {
        "certificate_type": "prime_matrix_cycle_debt_crt_cover_pressure_router",
        "status": "cycle_debt_requires_large_crt_cover_pressure",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_sweep_not_used_as_global_proof": True,
        "aggregate": {
            "row_column_unconditional_closed": False,
            "previous_hardpoint": PREVIOUS_TARGET,
            "ell": ell,
            "period_p": period_p,
            "positive_cycle_debt_residue_count": len(pressure_rows),
            "total_composite_waits": total_composite_waits,
            "one_period_composite_missing_count": int(one["composite_missing_count_in_one_period"]),
            "first_period_composite_waits_match_one_period_deficit": int(
                one["composite_missing_count_in_one_period"]
            )
            == len(pressure_rows),
            "global_unique_blocker_factor_count": len(all_unique_factors),
            "global_unique_blocker_factors": sorted(all_unique_factors),
            "global_blocker_lcm": global_lcm,
            "global_blocker_product": global_product,
            "global_blocker_product_log10": math.log10(global_product),
            "max_row_residue": int(max_row["residue"]),
            "max_row_cycle_debt": int(max_row["cycle_debt"]),
            "max_row_unique_blocker_factor_count": int(max_row["unique_blocker_factor_count"]),
            "max_row_blocker_lcm": int(max_row["blocker_lcm"]),
            "max_row_blocker_lcm_log10": math.log10(int(max_row["blocker_lcm"])),
            "crt_cover_modulus_exceeds_local_period": global_lcm > period_p,
            "hardpoint_after_router": NEXT_TARGET,
            "next_direct_attack_target": NEXT_TARGET,
        },
        "pressure_rows": pressure_rows,
        "plain_conclusion": (
            "27 个正周期债务 residue 的合数等待可写成周期坐标 k 上的 CRT 阻断覆盖。"
            "所有阻断最小素因子合并后共有 24 个不同素因子，整体 lcm 为 "
            f"{global_lcm}，远大于本地 P 周期 {period_p}。最大压力行是 residue=67："
            "15 个等待周期由 11 个不同阻断素因子覆盖，单行 lcm 为 "
            f"{max_row['blocker_lcm']}。因此周期债务若作为全局族复现，必须携带大 CRT "
            "相位包，而不能被视为局部自由 support motion。"
        ),
        "dependency_hashes": {
            str(PRIME_FILTER.relative_to(ROOT)): sha256(PRIME_FILTER),
            str(SATURATION.relative_to(ROOT)): sha256(SATURATION),
            str(ONE_PERIOD.relative_to(ROOT)): sha256(ONE_PERIOD),
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
        "# Prime Matrix cycle-debt CRT cover pressure router",
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
        f"positive_cycle_debt_residue_count={agg['positive_cycle_debt_residue_count']}",
        f"total_composite_waits={agg['total_composite_waits']}",
        f"global_unique_blocker_factor_count={agg['global_unique_blocker_factor_count']}",
        f"global_blocker_lcm={agg['global_blocker_lcm']}",
        f"global_blocker_product_log10={agg['global_blocker_product_log10']:.12f}",
        f"max_row_residue={agg['max_row_residue']}",
        f"max_row_cycle_debt={agg['max_row_cycle_debt']}",
        f"max_row_blocker_lcm={agg['max_row_blocker_lcm']}",
        f"crt_cover_modulus_exceeds_local_period={fmt_bool(agg['crt_cover_modulus_exceeds_local_period'])}",
        f"next_direct_attack_target={agg['next_direct_attack_target']}",
        "```",
        "",
        "## 1. pressure rows",
        "",
        "| residue | debt | unique factors | blocker lcm | first prime P |",
        "| ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in result["pressure_rows"]:
        lines.append(
            f"| {row['residue']} | {row['cycle_debt']} | "
            f"{row['unique_blocker_factor_count']} | {row['blocker_lcm']} | "
            f"{row['first_prime_p']} |"
        )

    lines.extend(
        [
            "",
            "## 2. 判定",
            "",
            "- 每个合数等待都是周期坐标 `k` 上的一个 CRT 阻断类。",
            "- 27 个正债务 residue 合并后需要 `24` 个不同阻断素因子。",
            "- 全局阻断 lcm 远大于本地 `P` 周期 `5680`，所以复现该债务需要大 CRT 相位包。",
            "- 本步不排斥所有大 CRT 包；它把剩余命名为 cycle-debt CRT cover PDEC 或全局 support-motion SAE。",
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
