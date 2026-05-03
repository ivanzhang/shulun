#!/usr/bin/env python3
"""审计 CRT 行反射与“短周期”猜想。

用法示例：
  python3 experiments/prime_matrix_row_reflection_period_audit.py
  python3 experiments/prime_matrix_row_reflection_period_audit.py --out-prefix docs/monograph/prime-matrix-row-reflection-period-audit

该脚本只检查已知的 p 对齐零行及其 CRT 镜像行，不枚举完整 CRT 周期。
核心目的是区分：
1. 反射配对是严格真命题；
2. 第二周期复现只给出二面体轨道；
3. k、2k、2k-1 都不是自动的“全覆盖现象周期”；
4. 由反射配对推出短平移周期或整除条件是错误的。
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


KNOWN_ZERO_ROWS = [
    {"p": 13, "first_zero_row": 169},
    {"p": 17, "first_zero_row": 1211},
    {"p": 19, "first_zero_row": 3659},
    {"p": 23, "first_zero_row": 59},
    {"p": 29, "first_zero_row": 5210},
]


def primes_upto(limit: int) -> list[int]:
    """返回不超过 limit 的素数。"""
    is_prime = [True] * (limit + 1)
    if limit >= 0:
        is_prime[0] = False
    if limit >= 1:
        is_prime[1] = False
    for value in range(2, int(limit**0.5) + 1):
        if is_prime[value]:
            for multiple in range(value * value, limit + 1, value):
                is_prime[multiple] = False
    return [value for value in range(2, limit + 1) if is_prime[value]]


def primorial(primes: list[int]) -> int:
    """计算素数连乘。"""
    result = 1
    for prime in primes:
        result *= prime
    return result


def covered_by_old_sieve(value: int, primes: list[int]) -> bool:
    """判断 value 是否被旧筛小素数覆盖。"""
    if value <= 1:
        return False
    return any(value % prime == 0 for prime in primes)


def row_is_zero(p: int, row: int, primes: list[int]) -> bool:
    """检查宽 p 行的非平凡列是否全被覆盖。

    第 p 列恒被 p 覆盖，不计入提供幸存者的非平凡列。
    """
    left = (row - 1) * p
    return all(covered_by_old_sieve(left + col, primes) for col in range(1, p))


def small_factors(value: int, primes: list[int]) -> list[int]:
    """返回 value 中不超过 p 的素因子。"""
    return [prime for prime in primes if value % prime == 0]


def row_factor_profile(p: int, row: int, primes: list[int]) -> dict:
    """生成指定行的逐列旧筛画像。"""
    cells = []
    uncovered = []
    for col in range(1, p + 1):
        value = (row - 1) * p + col
        factors = small_factors(value, primes)
        if col < p and not factors:
            uncovered.append({"col": col, "value": value})
        cells.append({"col": col, "value": value, "small_factors": factors})
    return {
        "row": row,
        "interval": [(row - 1) * p + 1, row * p],
        "is_zero": not uncovered,
        "uncovered": uncovered,
        "cells": cells,
    }


def audit_known_rows() -> dict:
    """执行已知零行反射审计。"""
    rows = []
    for item in KNOWN_ZERO_ROWS:
        p = item["p"]
        row = item["first_zero_row"]
        primes = primes_upto(p)
        period = primorial(primes)
        row_period = period // p
        mirror_row = row_period - row + 1
        short_return = 2 * row - 1
        phenomenon_shifts = [row, 2 * row, short_return]
        phenomenon_shift_checks = []
        for shift in phenomenon_shifts:
            stabilizer_gcd = math.gcd(row_period, shift)
            check_rows = []
            for multiplier in (1, 2, 3):
                candidate_row = row + multiplier * shift
                check_rows.append(
                    {
                        "row": candidate_row,
                        "inside_period": candidate_row <= row_period,
                        "zero": candidate_row <= row_period
                        and row_is_zero(p, candidate_row, primes),
                    }
                )
            phenomenon_shift_checks.append(
                {
                    "shift": shift,
                    "gcd_with_row_period": stabilizer_gcd,
                    "first_possible_orbit_row": ((row - 1) % stabilizer_gcd) + 1,
                    "passes_first_zero_necessary_condition": stabilizer_gcd >= row,
                    "checked_rows": check_rows,
                    "all_checked_zero": all(item["zero"] for item in check_rows),
                    "any_checked_zero": any(item["zero"] for item in check_rows),
                }
            )
        row_plus_short = row + short_return
        row_plus_two_short = row + 2 * short_return
        mirror_minus_short = mirror_row - short_return
        rows.append(
            {
                "p": p,
                "row_period": row_period,
                "first_zero_row": row,
                "mirror_row": mirror_row,
                "row_zero": row_is_zero(p, row, primes),
                "mirror_zero": row_is_zero(p, mirror_row, primes),
                "short_return_rows": short_return,
                "row_period_mod_short_return": row_period % short_return,
                "row_period_mod_row": row_period % row,
                "divides_short_return": row_period % short_return == 0,
                "divides_row": row_period % row == 0,
                "row_plus_short": row_plus_short,
                "row_plus_short_zero": (
                    row_plus_short <= row_period
                    and row_is_zero(p, row_plus_short, primes)
                ),
                "row_plus_two_short": row_plus_two_short,
                "row_plus_two_short_zero": (
                    row_plus_two_short <= row_period
                    and row_is_zero(p, row_plus_two_short, primes)
                ),
                "mirror_minus_short": mirror_minus_short,
                "mirror_minus_short_zero": (
                    mirror_minus_short >= 1
                    and row_is_zero(p, mirror_minus_short, primes)
                ),
                "phenomenon_shift_checks": phenomenon_shift_checks,
            }
        )
    p23_primes = primes_upto(23)
    p23_focus = {
        "p": 23,
        "rows": [
            row_factor_profile(23, row, p23_primes)
            for row in (59, 118, 176, 9699632)
        ],
    }
    return {
        "status": "reflection_true_short_period_false_on_samples",
        "rows": rows,
        "p23_focus": p23_focus,
        "summary": {
            "sample_count": len(rows),
            "all_rows_zero": all(row["row_zero"] for row in rows),
            "all_mirrors_zero": all(row["mirror_zero"] for row in rows),
            "short_return_divisibility_failures": sum(
                1 for row in rows if not row["divides_short_return"]
            ),
            "row_divisibility_failures": sum(1 for row in rows if not row["divides_row"]),
            "k_shift_counterexamples": sum(
                1
                for row in rows
                if not row["phenomenon_shift_checks"][0]["any_checked_zero"]
            ),
            "two_k_shift_counterexamples": sum(
                1
                for row in rows
                if not row["phenomenon_shift_checks"][1]["any_checked_zero"]
            ),
            "two_k_minus_one_shift_counterexamples": sum(
                1
                for row in rows
                if not row["phenomenon_shift_checks"][2]["any_checked_zero"]
            ),
        },
    }


def write_markdown(result: dict, path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# CRT 行反射与短周期猜想审计",
        "",
        "**状态：** `proved_reflection_pairing_refutes_short_period_divisibility`",
        "",
        "## 结论",
        "",
        "- 严格成立：若宽 `p` 的非平凡列全覆盖行 `r` 存在，则 CRT 周期内镜像行 `N-r+1` 也全覆盖，其中 `N=P(p)/p`。",
        "- 不成立：由行 `r` 与镜像行同时全覆盖，不能推出全覆盖行具有 `r`、`2r` 或 `2r-1` 的现象平移周期。",
        "- 因而也不能要求 `r`、`2r` 或 `2r-1` 整除 CRT 总行数 `N`。",
        "",
        "## 样本",
        "",
        "| p | N | zero row r | mirror N-r+1 | row zero | mirror zero | 2r-1 | N mod (2r-1) | N mod r |",
        "| ---: | ---: | ---: | ---: | --- | --- | ---: | ---: | ---: |",
    ]
    for row in result["rows"]:
        lines.append(
            "| {p} | {period} | {row} | {mirror} | {row_zero} | {mirror_zero} | {short_return} | {mod_short} | {mod_row} |".format(
                p=row["p"],
                period=row["row_period"],
                row=row["first_zero_row"],
                mirror=row["mirror_row"],
                row_zero=row["row_zero"],
                mirror_zero=row["mirror_zero"],
                short_return=row["short_return_rows"],
                mod_short=row["row_period_mod_short_return"],
                mod_row=row["row_period_mod_row"],
            )
        )
    lines.extend(
        [
            "",
            "## 短间隔不是平移周期的直接检验",
            "",
            "| p | r | d | gcd(N,d) | first orbit row | necessary ok | r+d zero | r+2d zero | r+3d zero |",
            "| ---: | ---: | ---: | ---: | ---: | --- | --- | --- | --- |",
        ]
    )
    for row in result["rows"]:
        for check in row["phenomenon_shift_checks"]:
            checked = check["checked_rows"]
            lines.append(
                "| {p} | {row} | {shift} | {gcd} | {first} | {ok} | {plus1} | {plus2} | {plus3} |".format(
                    p=row["p"],
                    row=row["first_zero_row"],
                    shift=check["shift"],
                    gcd=check["gcd_with_row_period"],
                    first=check["first_possible_orbit_row"],
                    ok=check["passes_first_zero_necessary_condition"],
                    plus1=checked[0]["zero"],
                    plus2=checked[1]["zero"],
                    plus3=checked[2]["zero"],
                )
            )
    lines.extend(
        [
            "",
            "## 证明级修正",
            "",
            "令 `M=prod_{ell<=p} ell`，`N=M/p`。非平凡列点 `n=(r-1)p+c`，`1<=c<p`，在取负映射下变为",
            "",
            "\\[",
            "M-n=(N-r)p+(p-c),",
            "\\]",
            "",
            "仍位于非平凡列，且所在行是 `N-r+1`。若 `ell|n`，则 `ell|(M-n)`。因此全覆盖行在反射下仍全覆盖。",
            "",
            "第二周期中行 `r` 的复现是 `r+N`。镜像行 `N-r+1` 到下一周期行 `r+N` 的间隔确为 `2r-1`，但这只是二面体轨道中相邻两点的距离，不是平移对称。沿轨道的两个间隔交替为 `N-2r+1` 与 `2r-1`。只有当行覆盖集合对平移 `2r-1` 不变时，才能推出整除关系；CRT 本身只保证平移 `N`。",
            "",
            "从掩码角度看，行平移 `d` 把每个列值加上 `dp`。对任意 `ell<p`，因 `(p,ell)=1`，要保持模 `ell` 的全部覆盖相位不变，必须有 `ell|d`。同时对全部 `ell<=p` 成立时，需 `N|d`。所以斜线斜率不变并不等于截距相位不变；短平移不会自动复现全覆盖行。",
            "",
            "若只要求“全覆盖现象”复现而不要求相位组合相同，也不能从一个零行和镜像零行推出 `r`、`2r` 或 `2r-1` 是现象周期。上表对已知零行直接检查了这些候选平移，均未复现零行。",
            "",
            "可以保留一个条件引理：若零行集合真的对某个平移 `d` 不变，且 `r` 是首个零行，则 `gcd(N,d)>=r`。否则轨道 `{r+md mod N}` 中会出现小于 `r` 的正行号零行，矛盾于首个零行定义。这个条件给 `d=r,2r,2r-1` 带来强 gcd 限制，但它只是必要条件，不是由反射自动推出的事实。",
            "",
            "样本 `p=23,r=59` 已给出明确反例：`N=9699690`，`2r-1=117`，`N mod 117=39`，且 `r+59=118`、`r+117=176`、`r+118=177` 都不是零行。零行与镜像零行均严格存在，但短周期整除路线不成立。",
            "",
            "## P=23 的第 59 行平移实测",
            "",
            "| row | interval | zero? | uncovered nontrivial cells |",
            "| ---: | --- | --- | --- |",
        ]
    )
    for profile in result["p23_focus"]["rows"]:
        uncovered = ", ".join(
            f"c={item['col']}:n={item['value']}" for item in profile["uncovered"]
        )
        lines.append(
            "| {row} | `{interval}` | {zero} | {uncovered} |".format(
                row=profile["row"],
                interval=profile["interval"],
                zero=profile["is_zero"],
                uncovered=uncovered or "none",
            )
        )
    row59 = result["p23_focus"]["rows"][0]
    row118 = result["p23_focus"]["rows"][1]
    lines.extend(
        [
            "",
            "逐列比较第 `59` 行与第 `118=2*59` 行：",
            "",
            "| col | row59 n:factors | row118 n:factors |",
            "| ---: | --- | --- |",
        ]
    )
    for left, right in zip(row59["cells"], row118["cells"]):
        lines.append(
            "| {col} | `{n1}:{f1}` | `{n2}:{f2}` |".format(
                col=left["col"],
                n1=left["value"],
                f1=left["small_factors"],
                n2=right["value"],
                f2=right["small_factors"],
            )
        )
    lines.extend(
        [
            "",
            "第 `59` 行的非平凡列全部有 `<=23` 的小素因子；第 `118` 行在列 `2,8,10,16,20,22` 留下旧筛幸存者，其中 `2693,2699,2707,2711,2713` 为素数，`2701=37*73` 是双粗合数。故第 `118` 行不仅没有复现全覆盖，而且含有多个真实素数。",
            "",
            "## 可保留的新硬攻方向",
            "",
            "可用的严格结论是两端帽排斥：若 `r0` 是首个零行，则前 `r0-1` 行和后 `r0-1` 行都无零行。这能强化零行延迟，但不能单独推出 `QSurv`。下一步应攻的是：若 `q` 网格行失败，则它的反射配对和两端帽排斥共同触发 `PDEC-or-SAE`，而不是要求短周期整除。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--out-prefix",
        default="docs/monograph/prime-matrix-row-reflection-period-audit",
    )
    args = parser.parse_args()
    result = audit_known_rows()
    prefix = Path(args.out_prefix)
    prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, prefix.with_suffix(".md"))
    print(json.dumps(result["summary"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
