#!/usr/bin/env python3
"""审计平方锚 Prime=0 反例到有效半素数完全铺砖的等价。

用法示例：
  python3 experiments/prime_matrix_square_phase_primevoid_effective_tiling_router.py --max-p 5000
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-primevoid-effective-tiling-router.json

输出：
  data/square-phase-primevoid-effective-tiling-ledger.json
  docs/monograph/prime-matrix-square-phase-primevoid-effective-tiling-router.json
  docs/monograph/prime-matrix-square-phase-primevoid-effective-tiling-router.md
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

OUT_LEDGER = DATA / "square-phase-primevoid-effective-tiling-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-primevoid-effective-tiling-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-primevoid-effective-tiling-router.md"

MAIN_TARGET = "PrimeVoidFullEffectiveSemiprimeTilingExclusion"
RETURN_TARGET = "FullEffectiveTilingPDECSAEReturn"


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


def audit_sign(p: int, sign: str, primes: list[int]) -> dict[str, Any]:
    """审计单个 P 的一个方向。"""
    cutoff = cutoff_alpha45(p)
    low_set = low_survivor_columns(p, cutoff, sign, primes)
    prime_columns: list[int] = []
    composite_low_columns: list[int] = []
    for r_value in sorted(low_set):
        value = square_value(p, r_value, sign)
        if is_prime_by_primes(value, primes):
            prime_columns.append(r_value)
        else:
            composite_low_columns.append(r_value)

    tail_primes = [q for q in primes if cutoff < q < p]
    tail_slots = [slot for q in tail_primes for slot in tail_slots_for_q(p, q, sign, primes)]
    effective_slots = [slot for slot in tail_slots if slot["r"] in low_set]
    effective_r = {slot["r"] for slot in effective_slots}
    good_effective_slots = [slot for slot in effective_slots if slot["cofactor_prime"]]
    good_effective_r = {slot["r"] for slot in good_effective_slots}

    tiling_missing = sorted(low_set - effective_r)
    tiling_extra = sorted(effective_r - low_set)
    composite_mismatch = sorted(set(composite_low_columns) ^ good_effective_r)
    prime_void = len(prime_columns) == 0
    full_effective_tiling = len(tiling_missing) == 0 and len(tiling_extra) == 0
    composite_tiling = set(composite_low_columns) == good_effective_r
    equivalence_failure = prime_void != full_effective_tiling or composite_tiling is False

    return {
        "p": p,
        "sign": sign,
        "cutoff": cutoff,
        "low_survivors_H": len(low_set),
        "prime_count": len(prime_columns),
        "composite_low_count": len(composite_low_columns),
        "effective_slot_count": len(effective_slots),
        "good_effective_slot_count": len(good_effective_slots),
        "prime_void": prime_void,
        "full_effective_tiling": full_effective_tiling,
        "composite_tiling": composite_tiling,
        "tiling_deficit": len(low_set) - len(effective_slots),
        "tiling_deficit_equals_prime": len(low_set) - len(effective_slots) == len(prime_columns),
        "equivalence_failure": equivalence_failure,
        "prime_columns_sample": prime_columns[:12],
        "tiling_missing_sample": tiling_missing[:12],
        "composite_mismatch_sample": composite_mismatch[:12],
    }


def theorem_rows() -> list[dict[str, str]]:
    """列出本步确定性定理。"""
    return [
        {
            "name": "prime_void_full_effective_tiling_equivalence",
            "status": "closed",
            "statement": "For each sign, Prime=0 is equivalent to the low-survivor set being fully tiled by effective high-tail semiprime slots.",
        },
        {
            "name": "tiling_deficit_equals_prime_count",
            "status": "closed",
            "statement": "The deficit H-C_eff is exactly the square-anchor prime count; the missing columns are precisely prime columns.",
        },
        {
            "name": "prime_void_pdec_object",
            "status": "open",
            "statement": "A Prime=0 counterexample is no longer an unstructured prime gap; it is a complete near-square semiprime tiling of every alpha=4/5 low survivor.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "PrimeVoidFullEffectiveTilingEquivalenceClosed",
            "closed": result["equivalence_failure_count"] == 0,
            "proved": True,
            "meaning": "`Prime=0` 与低洞被有效半素数槽完全铺满已严格等价。",
            "remaining": "closed",
        },
        {
            "gate": "FinitePrimeVoidAbsent",
            "closed": result["finite_prime_void_count"] == 0,
            "proved": False,
            "meaning": f"有限扫描 P<={result['parameters']['max_p']} 没有 prime-void 样本。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "FullEffectiveTilingExcluded",
            "closed": False,
            "proved": False,
            "meaning": "仍需全局排除完全有效半素数铺砖，或把它转成 PDEC/SAE。",
            "remaining": MAIN_TARGET,
        },
        {
            "gate": "FullTilingPDECReturn",
            "closed": False,
            "proved": False,
            "meaning": "若完全铺砖存在，必须抽取近方半素数槽的全覆盖相位缺陷。",
            "remaining": RETURN_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只关闭反例形态等价，不关闭全局行/列命题。",
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
    equivalence_failures = [record for record in records if record["equivalence_failure"]]
    prime_void_records = [record for record in records if record["prime_void"]]
    worst_deficit = min(records, key=lambda item: item["tiling_deficit"], default=None)
    plus_records = [record for record in records if record["sign"] == "plus"]
    minus_records = [record for record in records if record["sign"] == "minus"]
    aggregate = {
        "plus_H_total": sum(record["low_survivors_H"] for record in plus_records),
        "plus_prime_total": sum(record["prime_count"] for record in plus_records),
        "plus_effective_total": sum(record["effective_slot_count"] for record in plus_records),
        "minus_H_total": sum(record["low_survivors_H"] for record in minus_records),
        "minus_prime_total": sum(record["prime_count"] for record in minus_records),
        "minus_effective_total": sum(record["effective_slot_count"] for record in minus_records),
    }
    aggregate["combined_prime_total"] = aggregate["plus_prime_total"] + aggregate["minus_prime_total"]

    ledger = {
        "parameters": {"max_p": max_p, "alpha": "4/5", "sample_ps": sample_ps},
        "prime_count": len(p_values),
        "aggregate": aggregate,
        "equivalence_failure_count": len(equivalence_failures),
        "finite_prime_void_count": len(prime_void_records),
        "worst_tiling_deficit_record": worst_deficit,
        "sample_records": sample_records,
        "prime_void_records": prime_void_records[:20],
        "equivalence_failures": equivalence_failures[:20],
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    result = {
        "certificate_type": "prime_matrix_square_phase_primevoid_effective_tiling_router",
        "status": "square_phase_primevoid_reduced_to_full_effective_semiprime_tiling_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "empirical_absence_not_used_as_proof": True,
        "parameters": ledger["parameters"],
        "finite_prime_count": len(p_values),
        "aggregate": aggregate,
        "equivalence_failure_count": len(equivalence_failures),
        "finite_prime_void_count": len(prime_void_records),
        "worst_tiling_deficit_record": worst_deficit,
        "sample_records": sample_records,
        "prime_void_full_effective_tiling_equivalence_closed": len(equivalence_failures) == 0,
        "full_effective_tiling_excluded_proved": False,
        "full_tiling_pdec_return_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": "SquarePhaseEffectiveCapacityPrimeNonempty",
        "hardpoint_after_router": f"{MAIN_TARGET} OR {RETURN_TARGET}",
        "next_direct_attack_target": MAIN_TARGET,
        "alternative_attack_target": RETURN_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_primevoid_effective_tiling_router.py": sha256(
                Path(__file__).resolve()
            ),
            "data/square-phase-primevoid-effective-tiling-ledger.json": sha256(OUT_LEDGER),
        },
        "plain_conclusion": (
            "`Prime=0` 反例已被改写成一个完全铺砖对象：`alpha=4/5` 低筛后的每一个幸存列，"
            "都必须恰好由一个高尾近方半素数槽 `q(P+a+t)` 覆盖；铺砖缺口数精确等于平方锚素数数。"
            "因此下一步不再是抽象短区间素数问题，而是排除这种 full effective semiprime tiling，"
            "或把完全铺砖的相位刚性登记为 PDEC/SAE。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    worst = result["worst_tiling_deficit_record"]
    lines = [
        "# Prime Matrix square-phase prime-void effective tiling",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"max_p={result['parameters']['max_p']}",
        f"finite_prime_count={result['finite_prime_count']}",
        f"equivalence_failure_count={result['equivalence_failure_count']}",
        f"finite_prime_void_count={result['finite_prime_void_count']}",
        f"full_effective_tiling_excluded_proved={fmt_bool(result['full_effective_tiling_excluded_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 完全铺砖等价",
        "",
        "在有效容量口径下：",
        "",
        "```text",
        "H = Prime + GoodShell",
        "C_eff = GoodShell",
        "H-C_eff = Prime.",
        "```",
        "",
        "所以 `Prime=0` 当且仅当 `H=C_eff`，也就是低筛后所有幸存列都被有效高尾半素数槽完全铺满。"
        "反例不再是无结构的空素数窗口，而是一个 full effective semiprime tiling。",
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
            f"| H total | {agg['plus_H_total']} | {agg['minus_H_total']} | {agg['plus_H_total'] + agg['minus_H_total']} |",
            f"| effective slots | {agg['plus_effective_total']} | {agg['minus_effective_total']} | {agg['plus_effective_total'] + agg['minus_effective_total']} |",
            f"| tiling deficit / primes | {agg['plus_prime_total']} | {agg['minus_prime_total']} | {agg['combined_prime_total']} |",
            "",
            f"最小铺砖缺口样本：`P={worst['p']}`，`sign={worst['sign']}`，`deficit={worst['tiling_deficit']}`。",
            "",
            "## 4. 样本表",
            "",
            "| P | sign | H | effective slots | deficit | prime count | prime void | full tiling |",
            "| ---: | --- | ---: | ---: | ---: | ---: | --- | --- |",
        ]
    )
    for row in result["sample_records"]:
        lines.append(
            f"| {row['p']} | `{row['sign']}` | {row['low_survivors_H']} | "
            f"{row['effective_slot_count']} | {row['tiling_deficit']} | {row['prime_count']} | "
            f"`{fmt_bool(row['prime_void'])}` | `{fmt_bool(row['full_effective_tiling'])}` |"
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
            "- 需要证明 full effective semiprime tiling 不可能全局持续，或证明其完全相位贴合必产生 PDEC/SAE。有限扫描没有 prime-void，但这只作为诊断。",
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
                "equivalence_failure_count": result["equivalence_failure_count"],
                "finite_prime_void_count": result["finite_prime_void_count"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
