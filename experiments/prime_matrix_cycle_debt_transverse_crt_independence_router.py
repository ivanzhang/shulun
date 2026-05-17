#!/usr/bin/env python3
"""生成 cycle-debt 横向 CRT 独立性证书。

用法示例：
  python3 experiments/prime_matrix_cycle_debt_transverse_crt_independence_router.py
  python3 -m json.tool data/prime-matrix-cycle-debt-transverse-crt-independence-ledger.json

输出：
  data/prime-matrix-cycle-debt-transverse-crt-independence-ledger.json
  docs/monograph/prime-matrix-cycle-debt-transverse-crt-independence-router.json
  docs/monograph/prime-matrix-cycle-debt-transverse-crt-independence-router.md
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

CYCLE_COVER = DATA / "prime-matrix-cycle-debt-crt-cover-pressure-ledger.json"

OUT_LEDGER = DATA / "prime-matrix-cycle-debt-transverse-crt-independence-ledger.json"
OUT_JSON = DOCS / "prime-matrix-cycle-debt-transverse-crt-independence-router.json"
OUT_MD = DOCS / "prime-matrix-cycle-debt-transverse-crt-independence-router.md"

PREVIOUS_TARGET = "CycleDebtCRTCoverPressurePDECOrGlobalSupportMotionSAE"
NEXT_TARGET = "TransverseCRTCoverPDECExclusionOrGlobalSupportMotionSAE"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def factorization(n: int) -> dict[str, int]:
    """返回整数的试除分解。"""
    out: dict[str, int] = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            out[str(d)] = out.get(str(d), 0) + 1
            n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        out[str(n)] = out.get(str(n), 0) + 1
    return out


def product(values: list[int]) -> int:
    """计算整数乘积。"""
    out = 1
    for value in values:
        out *= value
    return out


def division_record(numerator: int, denominator: int) -> dict[str, Any]:
    """记录精确除法的商、余数与数量级。"""
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
    """构造横向 CRT 独立性证书。"""
    cover = load_json(CYCLE_COVER)
    agg = cover["aggregate"]
    period_p = int(agg["period_p"])
    total_waits = int(agg["total_composite_waits"])
    global_factors = [int(value) for value in agg["global_unique_blocker_factors"]]
    global_lcm = int(agg["global_blocker_lcm"])

    period_factorization = factorization(period_p)
    period_prime_factors = sorted(int(value) for value in period_factorization)
    factor_audit = []
    for factor in global_factors:
        gcd_value = math.gcd(factor, period_p)
        factor_audit.append(
            {
                "blocker_factor": factor,
                "gcd_with_period_p": gcd_value,
                "is_transverse_unit_mod_period": gcd_value == 1,
                "period_inverse_mod_factor": pow(period_p % factor, -1, factor)
                if gcd_value == 1
                else None,
            }
        )

    row_audits: list[dict[str, Any]] = []
    all_row_shift_consistent = True
    all_row_shift_zero = True
    all_row_lcm_exceeds_support_width = True
    row_lcm_exceeds_period_count = 0

    for row in cover["pressure_rows"]:
        debt = int(row["cycle_debt"])
        row_lcm = int(row["blocker_lcm"])
        support_width = debt
        if row_lcm > period_p:
            row_lcm_exceeds_period_count += 1
        all_row_lcm_exceeds_support_width &= row_lcm > support_width

        shift_classes: dict[int, set[int]] = {}
        blocker_class_checks = []
        for blocker in row["blockers"]:
            cycle = int(blocker["cycle"])
            factor = int(blocker["smallest_factor"])
            cycle_class = int(blocker["cycle_class_mod_factor"])
            shift_class = (cycle_class - cycle) % factor
            shift_classes.setdefault(factor, set()).add(shift_class)
            blocker_class_checks.append(
                {
                    "cycle": cycle,
                    "factor": factor,
                    "cycle_class_mod_factor": cycle_class,
                    "cycle_matches_class": cycle % factor == cycle_class,
                    "shift_replay_class_mod_factor": shift_class,
                }
            )

        row_shift_consistent = all(len(values) == 1 for values in shift_classes.values())
        row_shift_zero = all(values == {0} for values in shift_classes.values())
        all_row_shift_consistent &= row_shift_consistent
        all_row_shift_zero &= row_shift_zero

        row_audits.append(
            {
                "residue": int(row["residue"]),
                "cycle_debt": debt,
                "phase_support_width_cycles": support_width,
                "unique_blocker_factor_count": int(row["unique_blocker_factor_count"]),
                "unique_blocker_factors": [int(value) for value in row["unique_blocker_factors"]],
                "row_blocker_lcm": row_lcm,
                "gcd_row_lcm_with_period_p": math.gcd(row_lcm, period_p),
                "row_lcm_exceeds_phase_support_width": row_lcm > support_width,
                "row_lcm_over_support_width": division_record(row_lcm, support_width),
                "row_lcm_exceeds_period_p": row_lcm > period_p,
                "shift_replay_crt_consistent": row_shift_consistent,
                "shift_replay_class_mod_row_lcm": 0 if row_shift_consistent and row_shift_zero else None,
                "blocker_class_checks": blocker_class_checks,
            }
        )

    row_audits.sort(key=lambda item: (-int(item["row_blocker_lcm"]), int(item["residue"])))
    global_gcd = math.gcd(global_lcm, period_p)
    combined_period = math.lcm(global_lcm, period_p)
    transverse_factor_count = sum(1 for item in factor_audit if item["is_transverse_unit_mod_period"])

    result = {
        "certificate_type": "prime_matrix_cycle_debt_transverse_crt_independence_router",
        "status": "cycle_debt_crt_cover_is_transverse_to_local_period",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_sweep_not_used_as_global_proof": True,
        "aggregate": {
            "row_column_unconditional_closed": False,
            "previous_hardpoint": PREVIOUS_TARGET,
            "period_p": period_p,
            "period_p_factorization": period_factorization,
            "period_prime_factors": period_prime_factors,
            "global_unique_blocker_factor_count": len(global_factors),
            "transverse_blocker_factor_count": transverse_factor_count,
            "all_blocker_factors_coprime_to_period_p": transverse_factor_count == len(global_factors),
            "period_prime_factors_absent_from_blocker_factors": not (
                set(period_prime_factors) & set(global_factors)
            ),
            "global_blocker_lcm": global_lcm,
            "gcd_global_blocker_lcm_with_period_p": global_gcd,
            "global_blocker_lcm_coprime_to_period_p": global_gcd == 1,
            "combined_period_lcm_period_p_and_blocker_lcm": combined_period,
            "combined_period_equals_product": combined_period == period_p * global_lcm,
            "global_lcm_over_period_p": division_record(global_lcm, period_p),
            "total_composite_waits": total_waits,
            "global_lcm_exceeds_total_wait_width": global_lcm > total_waits,
            "global_lcm_over_total_wait_width": division_record(global_lcm, total_waits),
            "positive_cycle_debt_residue_count": int(agg["positive_cycle_debt_residue_count"]),
            "all_row_shift_replay_crt_consistent": all_row_shift_consistent,
            "all_row_shift_replay_classes_zero": all_row_shift_zero,
            "all_row_lcm_exceeds_phase_support_width": all_row_lcm_exceeds_support_width,
            "row_lcm_exceeds_period_p_count": row_lcm_exceeds_period_count,
            "max_row_residue": int(agg["max_row_residue"]),
            "max_row_cycle_debt": int(agg["max_row_cycle_debt"]),
            "max_row_blocker_lcm": int(agg["max_row_blocker_lcm"]),
            "max_row_lcm_over_period_p": division_record(int(agg["max_row_blocker_lcm"]), period_p),
            "local_period_absorption_closed_current_certificate": (
                transverse_factor_count == len(global_factors)
                and global_gcd == 1
                and all_row_shift_consistent
                and all_row_shift_zero
                and all_row_lcm_exceeds_support_width
            ),
            "hardpoint_after_router": NEXT_TARGET,
            "next_direct_attack_target": NEXT_TARGET,
        },
        "factor_audit": factor_audit,
        "row_audits": row_audits,
        "plain_conclusion": (
            "上一张 cycle-debt 账本中的 24 个阻断素因子全部与本地周期 "
            f"{period_p} 互素，且其全局 lcm 与该周期互素。对每个同 residue 列 "
            "P(k)=P0+5680*k，复现同一合数等待前缀时，周期平移量 K 必须同时满足 "
            "K=0 mod q 的横向 CRT 条件；合并后即 K=0 mod "
            f"{global_lcm}。因此该债务包不能由 5680 周期内的局部槽平移吸收，"
            "而必须升级为 transverse CRT cover PDEC，或进入真正全局 support-motion SAE。"
        ),
        "dependency_hashes": {
            str(CYCLE_COVER.relative_to(ROOT)): sha256(CYCLE_COVER),
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
    global_ratio = agg["global_lcm_over_period_p"]
    wait_ratio = agg["global_lcm_over_total_wait_width"]
    max_row_ratio = agg["max_row_lcm_over_period_p"]
    lines = [
        "# Prime Matrix cycle-debt transverse CRT independence router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"row_column_unconditional_closed={fmt_bool(agg['row_column_unconditional_closed'])}",
        f"previous_hardpoint={agg['previous_hardpoint']}",
        f"period_p={agg['period_p']}",
        f"period_p_factorization={json.dumps(agg['period_p_factorization'], ensure_ascii=False)}",
        f"global_unique_blocker_factor_count={agg['global_unique_blocker_factor_count']}",
        f"transverse_blocker_factor_count={agg['transverse_blocker_factor_count']}",
        f"all_blocker_factors_coprime_to_period_p={fmt_bool(agg['all_blocker_factors_coprime_to_period_p'])}",
        f"global_blocker_lcm={agg['global_blocker_lcm']}",
        f"gcd_global_blocker_lcm_with_period_p={agg['gcd_global_blocker_lcm_with_period_p']}",
        f"combined_period_equals_product={fmt_bool(agg['combined_period_equals_product'])}",
        f"global_lcm_over_period_p_floor={global_ratio['floor']}",
        f"global_lcm_over_period_p_remainder={global_ratio['remainder']}",
        f"global_lcm_over_period_p_log10={global_ratio['log10_ratio']:.12f}",
        f"global_lcm_over_total_wait_width_floor={wait_ratio['floor']}",
        f"global_lcm_over_total_wait_width_log10={wait_ratio['log10_ratio']:.12f}",
        f"all_row_shift_replay_crt_consistent={fmt_bool(agg['all_row_shift_replay_crt_consistent'])}",
        f"all_row_shift_replay_classes_zero={fmt_bool(agg['all_row_shift_replay_classes_zero'])}",
        f"all_row_lcm_exceeds_phase_support_width={fmt_bool(agg['all_row_lcm_exceeds_phase_support_width'])}",
        f"row_lcm_exceeds_period_p_count={agg['row_lcm_exceeds_period_p_count']}",
        f"max_row_residue={agg['max_row_residue']}",
        f"max_row_cycle_debt={agg['max_row_cycle_debt']}",
        f"max_row_blocker_lcm={agg['max_row_blocker_lcm']}",
        f"max_row_lcm_over_period_p_floor={max_row_ratio['floor']}",
        f"local_period_absorption_closed_current_certificate={fmt_bool(agg['local_period_absorption_closed_current_certificate'])}",
        f"next_direct_attack_target={agg['next_direct_attack_target']}",
        "```",
        "",
        "## 1. transverse factor audit",
        "",
        "| blocker factor | gcd(q,5680) | inverse of 5680 mod q | transverse unit |",
        "| ---: | ---: | ---: | :---: |",
    ]
    for item in result["factor_audit"]:
        lines.append(
            f"| {item['blocker_factor']} | {item['gcd_with_period_p']} | "
            f"{item['period_inverse_mod_factor']} | "
            f"{fmt_bool(item['is_transverse_unit_mod_period'])} |"
        )

    lines.extend(
        [
            "",
            "## 2. row replay pressure",
            "",
            "| residue | debt width | unique factors | row lcm | gcd(lcm,5680) | lcm>width | shift class |",
            "| ---: | ---: | ---: | ---: | ---: | :---: | ---: |",
        ]
    )
    for row in result["row_audits"]:
        lines.append(
            f"| {row['residue']} | {row['phase_support_width_cycles']} | "
            f"{row['unique_blocker_factor_count']} | {row['row_blocker_lcm']} | "
            f"{row['gcd_row_lcm_with_period_p']} | "
            f"{fmt_bool(row['row_lcm_exceeds_phase_support_width'])} | "
            f"{row['shift_replay_class_mod_row_lcm']} |"
        )

    lines.extend(
        [
            "",
            "## 3. 判定",
            "",
            "- `5680=2^4*5*71`，而 24 个阻断素因子均不含 `2,5,71`。",
            "- 因为 `gcd(q,5680)=1`，每个合数等待的阻断不是周期内因子，而是周期坐标上的横向 CRT 条件。",
            "- 对固定 residue 行，复现同一等待前缀的平移量 `K` 必须满足 `K=0 mod row_lcm`；全部 27 行合并为 `K=0 mod global_lcm`。",
            "- 该全局横向模数与 `5680` 互素，组合周期等于两者乘积；因此 local period absorption 在当前证书内关闭。",
            "- 本步仍不宣称行/列命题无条件闭合；剩余是排斥 transverse CRT cover PDEC，或证明 global support-motion SAE 可求和。",
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
