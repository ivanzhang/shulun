#!/usr/bin/env python3
"""审计平方锚有效半素数槽的偶数半网格正规形。

用法示例：
  python3 experiments/prime_matrix_square_phase_effective_even_slot_normal_form_router.py --max-p 5000
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-effective-even-slot-normal-form-router.json

输出：
  data/square-phase-effective-even-slot-normal-form-ledger.json
  docs/monograph/prime-matrix-square-phase-effective-even-slot-normal-form-router.json
  docs/monograph/prime-matrix-square-phase-effective-even-slot-normal-form-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from math import isqrt
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "square-phase-effective-even-slot-normal-form-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-effective-even-slot-normal-form-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-effective-even-slot-normal-form-router.md"

MAIN_TARGET = "EvenHalfGridPrimePairTilingExclusion"
RETURN_TARGET = "EvenHalfGridPrimePairTilingPDECSAEReturn"


def sieve(limit: int) -> bytearray:
    """筛出 limit 以内素数。"""
    flags = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        flags[0] = 0
    if limit >= 1:
        flags[1] = 0
    for value in range(2, isqrt(limit) + 1):
        if flags[value]:
            start = value * value
            flags[start : limit + 1 : value] = b"\x00" * (((limit - start) // value) + 1)
    return flags


def primes_from_flags(flags: bytearray, limit: int | None = None) -> list[int]:
    """从筛表提取素数。"""
    end = len(flags) if limit is None else min(limit + 1, len(flags))
    return [idx for idx in range(2, end) if flags[idx]]


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def cutoff_alpha45(p: int) -> int:
    """返回 floor(4P/5)。"""
    return (4 * p) // 5


def ceil_div(numerator: int, denominator: int) -> int:
    """整数向上取整，允许 numerator 为负。"""
    return -((-numerator) // denominator)


def is_prime_by_primes(value: int, primes: list[int]) -> bool:
    """用素数表判定素性。"""
    if value < 2:
        return False
    for q in primes:
        if q * q > value:
            return True
        if value % q == 0:
            return value == q
    raise ValueError("prime table too short")


def least_prime_factor(value: int, primes: list[int]) -> int:
    """返回最小素因子；素数返回自身。"""
    for q in primes:
        if q * q > value:
            return value
        if value % q == 0:
            return q
    raise ValueError("prime table too short")


def square_value(p: int, r_value: int, sign: str) -> int:
    """返回 P^2±r。"""
    if sign == "plus":
        return p * p + r_value
    if sign == "minus":
        return p * p - r_value
    raise ValueError(f"unknown sign: {sign}")


def cover_residue(p: int, q: int, sign: str) -> int:
    """返回 r 坐标中被 q 覆盖的唯一正残基。"""
    p2_mod = (p * p) % q
    residue = (-p2_mod) % q if sign == "plus" else p2_mod
    return q if residue == 0 else residue


def low_survivor_columns(p: int, cutoff: int, sign: str, primes: list[int]) -> set[int]:
    """返回未被 q<=cutoff 覆盖的列集合。"""
    covered = bytearray(p)
    for q in primes:
        if q >= p or q > cutoff:
            break
        residue = cover_residue(p, q, sign)
        for r_value in range(residue, p, q):
            covered[r_value] = 1
    return {r_value for r_value in range(1, p) if not covered[r_value]}


def tail_slots_for_q(p: int, q: int, sign: str, primes: list[int]) -> list[dict[str, Any]]:
    """给出尾素 q=P-a 的全部槽。"""
    a_value = p - q
    square_a = a_value * a_value
    if sign == "plus":
        t_start = square_a // q + 1
        t_end = (square_a + p - 1) // q
    elif sign == "minus":
        t_start = ceil_div(square_a - p + 1, q)
        t_end = (square_a - 1) // q
    else:
        raise ValueError(f"unknown sign: {sign}")

    records: list[dict[str, Any]] = []
    for t_value in range(t_start, t_end + 1):
        r_value = t_value * q - square_a if sign == "plus" else square_a - t_value * q
        value = square_value(p, r_value, sign)
        cofactor = value // q
        lpf = least_prime_factor(cofactor, primes)
        records.append(
            {
                "q": q,
                "a": a_value,
                "t": t_value,
                "r": r_value,
                "value": value,
                "cofactor_m": cofactor,
                "cofactor_prime": lpf == cofactor,
            }
        )
    return records


def normal_form(slot: dict[str, Any], sign: str, p: int) -> dict[str, Any]:
    """把有效槽写成偶数半网格正规形。"""
    a_value = slot["a"]
    t_value = slot["t"]
    r_value = slot["r"]
    b_value = a_value // 2
    u_value = t_value // 2
    s_value = r_value // 2
    if sign == "plus":
        s_formula = u_value * p - 2 * b_value * (u_value + b_value)
    elif sign == "minus":
        s_formula = 2 * b_value * (u_value + b_value) - u_value * p
    else:
        raise ValueError(f"unknown sign: {sign}")
    q_formula = p - 2 * b_value
    m_formula = p + 2 * (b_value + u_value)
    return {
        "q": slot["q"],
        "m": slot["cofactor_m"],
        "r": r_value,
        "s": s_value,
        "a": a_value,
        "t": t_value,
        "b": b_value,
        "u": u_value,
        "q_formula": q_formula,
        "m_formula": m_formula,
        "s_formula": s_formula,
        "q_formula_ok": q_formula == slot["q"],
        "m_formula_ok": m_formula == slot["cofactor_m"],
        "s_formula_ok": s_formula == s_value,
        "half_grid_window_ok": 1 <= s_value <= (p - 1) // 2,
        "tail_b_bound_ok": 0 < 2 * b_value < p // 5 + 1,
        "cofactor_prime": slot["cofactor_prime"],
    }


def audit_sign(p: int, sign: str, primes: list[int]) -> dict[str, Any]:
    """审计单个 P 的一个方向。"""
    cutoff = cutoff_alpha45(p)
    low_set = low_survivor_columns(p, cutoff, sign, primes)
    odd_low = sorted(r_value for r_value in low_set if r_value % 2 == 1)

    tail_primes = [q for q in primes if cutoff < q < p]
    tail_slots = [slot for q in tail_primes for slot in tail_slots_for_q(p, q, sign, primes)]
    effective_slots = [
        slot for slot in tail_slots if slot["r"] in low_set and slot["cofactor_prime"]
    ]
    normal_rows = [normal_form(slot, sign, p) for slot in effective_slots]
    normal_failures = [
        row
        for row in normal_rows
        if row["a"] % 2
        or row["t"] % 2
        or row["r"] % 2
        or not row["q_formula_ok"]
        or not row["m_formula_ok"]
        or not row["s_formula_ok"]
        or not row["half_grid_window_ok"]
        or not row["cofactor_prime"]
    ]

    u_histogram: dict[int, int] = {}
    b_histogram: dict[int, int] = {}
    for row in normal_rows:
        u_histogram[row["u"]] = u_histogram.get(row["u"], 0) + 1
        b_histogram[row["b"]] = b_histogram.get(row["b"], 0) + 1

    return {
        "p": p,
        "sign": sign,
        "cutoff": cutoff,
        "low_survivors": len(low_set),
        "odd_low_survivor_count": len(odd_low),
        "effective_even_slot_count": len(normal_rows),
        "normal_form_failure_count": len(normal_failures),
        "max_b": max((row["b"] for row in normal_rows), default=0),
        "max_u": max((row["u"] for row in normal_rows), default=0),
        "min_u": min((row["u"] for row in normal_rows), default=0),
        "u_histogram_sample": dict(sorted(u_histogram.items())[:40]),
        "b_histogram_sample": dict(sorted(b_histogram.items())[:40]),
        "normal_rows_sample": normal_rows[:10],
        "odd_low_sample": odd_low[:10],
        "normal_failures": normal_failures[:5],
    }


def theorem_rows() -> list[dict[str, str]]:
    """列出本步确定性定理。"""
    return [
        {
            "name": "low_survivors_live_on_even_half_grid",
            "status": "closed",
            "statement": "Since q=2 is in the low sieve and P is odd, every low survivor has even r, hence r=2s with 1<=s<=(P-1)/2.",
        },
        {
            "name": "effective_slots_have_even_t",
            "status": "closed",
            "statement": "For a good effective slot, q and m are odd primes; with a=P-q even, m=P+a+t odd forces t even.",
        },
        {
            "name": "even_half_grid_normal_form",
            "status": "closed",
            "statement": "Writing a=2b and t=2u, effective slots are prime pairs q=P-2b, m=P+2(b+u), with s=uP-2b(u+b) on plus and s=2b(u+b)-uP on minus.",
        },
        {
            "name": "remaining_even_prime_pair_tiling",
            "status": "open",
            "statement": "A prime-void counterexample must tile the even low-survivor half-grid by this restricted prime-pair normal form.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "EvenHalfGridNormalFormClosed",
            "closed": result["total_failure_count"] == 0,
            "proved": True,
            "meaning": "有效半素数槽已全部写成偶数半网格素对正规形。",
            "remaining": "closed",
        },
        {
            "gate": "EvenPrimePairTilingExcluded",
            "closed": False,
            "proved": False,
            "meaning": "仍需全局排除该正规形对低洞半网格的完全铺砖。",
            "remaining": MAIN_TARGET,
        },
        {
            "gate": "EvenPrimePairTilingPDEC",
            "closed": False,
            "proved": False,
            "meaning": "若完全铺砖存在，需抽取 `(b,u)` 素对曲线的相位缺陷。",
            "remaining": RETURN_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只关闭正规形，不关闭全局行/列命题。",
            "remaining": f"{MAIN_TARGET} OR {RETURN_TARGET}",
        },
    ]


def build_result(max_p: int, sample_ps: list[int]) -> dict[str, Any]:
    """构造路由器结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    prime_flags = sieve(max_p * 2)
    primes = primes_from_flags(prime_flags, max_p * 2)
    p_values = [p for p in primes if 3 <= p <= max_p]
    records: list[dict[str, Any]] = []
    for p in p_values:
        records.append(audit_sign(p, "plus", primes))
        records.append(audit_sign(p, "minus", primes))

    sample_set = set(sample_ps)
    sample_records = [record for record in records if record["p"] in sample_set]
    total_failures = sum(record["normal_form_failure_count"] for record in records)
    total_odd_low = sum(record["odd_low_survivor_count"] for record in records)
    plus_records = [record for record in records if record["sign"] == "plus"]
    minus_records = [record for record in records if record["sign"] == "minus"]
    aggregate = {
        "plus_effective_even_slots": sum(record["effective_even_slot_count"] for record in plus_records),
        "minus_effective_even_slots": sum(record["effective_even_slot_count"] for record in minus_records),
        "plus_max_b": max((record["max_b"] for record in plus_records), default=0),
        "minus_max_b": max((record["max_b"] for record in minus_records), default=0),
        "plus_max_u": max((record["max_u"] for record in plus_records), default=0),
        "minus_max_u": max((record["max_u"] for record in minus_records), default=0),
    }
    aggregate["combined_effective_even_slots"] = (
        aggregate["plus_effective_even_slots"] + aggregate["minus_effective_even_slots"]
    )

    ledger = {
        "parameters": {"max_p": max_p, "alpha": "4/5", "sample_ps": sample_ps},
        "prime_count": len(p_values),
        "aggregate": aggregate,
        "total_failure_count": total_failures,
        "total_odd_low_survivor_count": total_odd_low,
        "sample_records": sample_records,
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    result = {
        "certificate_type": "prime_matrix_square_phase_effective_even_slot_normal_form_router",
        "status": "square_phase_full_tiling_reduced_to_even_half_grid_prime_pair_tiling_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "empirical_absence_not_used_as_proof": True,
        "parameters": ledger["parameters"],
        "finite_prime_count": len(p_values),
        "aggregate": aggregate,
        "total_failure_count": total_failures,
        "total_odd_low_survivor_count": total_odd_low,
        "sample_records": sample_records,
        "even_half_grid_normal_form_closed": total_failures == 0 and total_odd_low == 0,
        "even_prime_pair_tiling_excluded_proved": False,
        "even_prime_pair_tiling_pdec_return_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": "PrimeVoidFullEffectiveSemiprimeTilingExclusion",
        "hardpoint_after_router": f"{MAIN_TARGET} OR {RETURN_TARGET}",
        "next_direct_attack_target": MAIN_TARGET,
        "alternative_attack_target": RETURN_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_effective_even_slot_normal_form_router.py": sha256(
                Path(__file__).resolve()
            ),
            "data/square-phase-effective-even-slot-normal-form-ledger.json": sha256(OUT_LEDGER),
        },
        "plain_conclusion": (
            "Full effective semiprime tiling 已被压成偶数半网格素对铺砖：低筛幸存列全在 `r=2s` 上；"
            "有效半素数槽必须有 `a=2b,t=2u`，于是尾素与余因子为 `P-2b`、`P+2(b+u)`，"
            "plus 半列 `s=uP-2b(u+b)`，minus 半列 `s=2b(u+b)-uP`。"
            "因此反例必须由这族非常受限的素对曲线完全铺满低洞半网格；全局排斥或 PDEC/SAE 回流仍未完成。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase effective even-slot normal form",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"max_p={result['parameters']['max_p']}",
        f"finite_prime_count={result['finite_prime_count']}",
        f"total_failure_count={result['total_failure_count']}",
        f"total_odd_low_survivor_count={result['total_odd_low_survivor_count']}",
        f"even_prime_pair_tiling_excluded_proved={fmt_bool(result['even_prime_pair_tiling_excluded_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 偶数半网格正规形",
        "",
        "`q=2` 已在低筛内，而 `P` 为奇素数，所以所有低洞列都是偶数列 `r=2s`。",
        "有效半素数槽要求 `q=P-a` 和 `m=P+a+t` 都是奇素数；由于 `a` 为偶数，必须 `t` 为偶数。",
        "",
        "写",
        "",
        "```text",
        "a=2b,   t=2u,   r=2s.",
        "```",
        "",
        "则有效槽统一写成素对",
        "",
        "```text",
        "q=P-2b,        m=P+2(b+u).",
        "```",
        "",
        "plus/minus 半列公式分别为",
        "",
        "```text",
        "plus:  s = uP - 2b(u+b)",
        "minus: s = 2b(u+b) - uP",
        "```",
        "",
        "完全铺砖反例因此必须用这族 `(b,u)` 素对曲线铺满低洞半网格。",
        "",
        "## 2. 确定性判据",
        "",
        "| name | status | statement |",
        "| --- | --- | --- |",
    ]
    for item in result["theorem_rows"]:
        lines.append(f"| `{item['name']}` | `{item['status']}` | {table_cell(item['statement'])} |")

    agg = result["aggregate"]
    lines.extend(
        [
            "",
            "## 3. 有限审计摘要",
            "",
            "| metric | plus | minus | combined |",
            "| --- | ---: | ---: | ---: |",
            f"| effective even slots | {agg['plus_effective_even_slots']} | {agg['minus_effective_even_slots']} | {agg['combined_effective_even_slots']} |",
            f"| max b | {agg['plus_max_b']} | {agg['minus_max_b']} | - |",
            f"| max u | {agg['plus_max_u']} | {agg['minus_max_u']} | - |",
            "",
            "## 4. 样本表",
            "",
            "| P | sign | low survivors | effective slots | odd low | failures | max b | min u | max u |",
            "| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in result["sample_records"]:
        lines.append(
            f"| {row['p']} | `{row['sign']}` | {row['low_survivors']} | "
            f"{row['effective_even_slot_count']} | {row['odd_low_survivor_count']} | "
            f"{row['normal_form_failure_count']} | {row['max_b']} | {row['min_u']} | {row['max_u']} |"
        )

    lines.extend(
        [
            "",
            "## 5. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | ---: | ---: | --- | --- |",
        ]
    )
    for item in result["decision_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{item['gate']}`",
                    f"`{fmt_bool(item['closed'])}`",
                    f"`{fmt_bool(item['proved'])}`",
                    table_cell(item["meaning"]),
                    table_cell(item["remaining"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 6. 下一步",
            "",
            f"- 主攻：`{result['next_direct_attack_target']}`。",
            f"- 备选回流：`{result['alternative_attack_target']}`。",
            "- 需要排除这族 `(b,u)` 素对曲线对低洞半网格的完全铺砖；若不能直接排除，则把铺砖所需的相位贴合登记为 PDEC/SAE。",
            "",
            "## 7. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for name, digest in sorted(result["source_hashes"].items()):
        lines.append(f"| `{name}` | `{digest}` |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_ints(raw: str) -> list[int]:
    """解析整数列表。"""
    return [int(item) for item in raw.split(",") if item.strip()]


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-p", type=int, default=5000)
    parser.add_argument("--sample-ps", default="13,17,19,23,29,31,101,499,1009,2003,4999")
    args = parser.parse_args()

    result = build_result(max_p=args.max_p, sample_ps=parse_ints(args.sample_ps))
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result)
    print(
        json.dumps(
            {
                "status": result["status"],
                "max_p": result["parameters"]["max_p"],
                "total_failure_count": result["total_failure_count"],
                "total_odd_low_survivor_count": result["total_odd_low_survivor_count"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
