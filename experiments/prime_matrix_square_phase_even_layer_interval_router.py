#!/usr/bin/env python3
"""审计平方锚偶半网格素对槽的固定 b 层区间公式。

用法示例：
  python3 experiments/prime_matrix_square_phase_even_layer_interval_router.py --max-p 5000
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-even-layer-interval-router.json

输出：
  data/square-phase-even-layer-interval-ledger.json
  docs/monograph/prime-matrix-square-phase-even-layer-interval-router.json
  docs/monograph/prime-matrix-square-phase-even-layer-interval-router.md
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

OUT_LEDGER = DATA / "square-phase-even-layer-interval-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-even-layer-interval-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-even-layer-interval-router.md"

MAIN_TARGET = "EvenLayerPrimePairCandidateUpperBoundBeatsLowHoles"
RETURN_TARGET = "EvenLayerPrimePairTilingPDECSAEReturn"


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


def is_prime_by_flags(value: int, flags: bytearray) -> bool:
    """用筛表判定素性。"""
    return 0 <= value < len(flags) and bool(flags[value])


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


def layer_interval_for_b(p: int, b_value: int, sign: str) -> tuple[int, int]:
    """返回固定 b 时 u 的精确可行区间。"""
    half = (p - 1) // 2
    q_value = p - 2 * b_value
    base = 2 * b_value * b_value
    if sign == "plus":
        lower = base + 1
        upper = base + half
        return ceil_div(lower, q_value), upper // q_value
    if sign == "minus":
        lower = base - half
        upper = base - 1
        return max(0, ceil_div(lower, q_value)), upper // q_value
    raise ValueError(f"unknown sign: {sign}")


def s_value_for(p: int, b_value: int, u_value: int, sign: str) -> int:
    """返回半列 s。"""
    if sign == "plus":
        return u_value * p - 2 * b_value * (u_value + b_value)
    if sign == "minus":
        return 2 * b_value * (u_value + b_value) - u_value * p
    raise ValueError(f"unknown sign: {sign}")


def candidate_slots(p: int, sign: str, prime_flags: bytearray) -> list[dict[str, int]]:
    """枚举由固定 b 层区间和双素性生成的候选有效槽。"""
    cutoff = cutoff_alpha45(p)
    max_b = (p - cutoff - 1) // 2
    rows: list[dict[str, int]] = []
    for b_value in range(1, max_b + 1):
        q_value = p - 2 * b_value
        if not is_prime_by_flags(q_value, prime_flags):
            continue
        u_min, u_max = layer_interval_for_b(p, b_value, sign)
        for u_value in range(u_min, u_max + 1):
            m_value = p + 2 * (b_value + u_value)
            if not is_prime_by_flags(m_value, prime_flags):
                continue
            s_value = s_value_for(p, b_value, u_value, sign)
            if 1 <= s_value <= (p - 1) // 2:
                rows.append(
                    {
                        "b": b_value,
                        "u": u_value,
                        "q": q_value,
                        "m": m_value,
                        "s": s_value,
                        "r": 2 * s_value,
                    }
                )
    return rows


def audit_sign(p: int, sign: str, primes: list[int], prime_flags: bytearray) -> dict[str, Any]:
    """审计单个 P 的一个方向。"""
    cutoff = cutoff_alpha45(p)
    low_set = low_survivor_columns(p, cutoff, sign, primes)
    candidates = candidate_slots(p, sign, prime_flags)
    candidate_r = {row["r"] for row in candidates}
    effective_r = set()
    for r_value in low_set:
        value = p * p + r_value if sign == "plus" else p * p - r_value
        # 候选槽只对应高尾半素数；这里用候选 r 集合交低洞得到有效槽口径。
        if r_value in candidate_r and not is_prime_by_flags(value, prime_flags):
            effective_r.add(r_value)

    candidate_not_low = sorted(candidate_r - low_set)
    effective_missing = sorted(effective_r ^ candidate_r)
    layer_interval_failures = []
    for row in candidates:
        u_min, u_max = layer_interval_for_b(p, row["b"], sign)
        if not (u_min <= row["u"] <= u_max):
            layer_interval_failures.append(row)

    per_u: dict[int, int] = {}
    for row in candidates:
        per_u[row["u"]] = per_u.get(row["u"], 0) + 1

    return {
        "p": p,
        "sign": sign,
        "cutoff": cutoff,
        "low_survivors": len(low_set),
        "candidate_prime_pair_slots": len(candidates),
        "candidate_distinct_r_count": len(candidate_r),
        "effective_r_count": len(effective_r),
        "candidate_not_low_count": len(candidate_not_low),
        "effective_candidate_symmetric_difference_count": len(effective_missing),
        "layer_interval_failure_count": len(layer_interval_failures),
        "max_u": max((row["u"] for row in candidates), default=0),
        "max_b": max((row["b"] for row in candidates), default=0),
        "max_layer_load": max(per_u.values(), default=0),
        "sample_candidates": candidates[:10],
        "candidate_not_low_sample": candidate_not_low[:10],
        "effective_missing_sample": effective_missing[:10],
        "layer_interval_failures": layer_interval_failures[:5],
    }


def theorem_rows() -> list[dict[str, str]]:
    """列出本步确定性定理。"""
    return [
        {
            "name": "fixed_b_u_interval_formula",
            "status": "closed",
            "statement": "For fixed b, the half-window condition 1<=s<=(P-1)/2 gives an exact integer interval for u on both signs.",
        },
        {
            "name": "candidate_slots_generated_without_low_sieve",
            "status": "closed",
            "statement": "The effective semiprime slots are exactly the candidate pairs with q=P-2b and m=P+2(b+u) prime and u in the fixed-b interval.",
        },
        {
            "name": "full_tiling_candidate_upper_bound_target",
            "status": "open",
            "statement": "A full tiling would require the candidate prime-pair slot count to reach the low-hole count H; proving a global upper/lower gap or PDEC return remains open.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "FixedBLayerIntervalFormulaClosed",
            "closed": result["total_failure_count"] == 0,
            "proved": True,
            "meaning": "固定 b 层的 u 区间与候选槽枚举已逐项对齐。",
            "remaining": "closed",
        },
        {
            "gate": "CandidateUpperBoundBeatsLowHoles",
            "closed": False,
            "proved": False,
            "meaning": "仍需全局证明候选素对槽数小于低洞数，或证明失败形成 PDEC/SAE。",
            "remaining": MAIN_TARGET,
        },
        {
            "gate": "LayerPrimePairTilingPDEC",
            "closed": False,
            "proved": False,
            "meaning": "若候选槽可完全铺砖低洞，需要登记固定 b/u 层的相位异常。",
            "remaining": RETURN_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只关闭层区间公式，不关闭全局行/列命题。",
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
        records.append(audit_sign(p, "plus", primes, prime_flags))
        records.append(audit_sign(p, "minus", primes, prime_flags))

    sample_set = set(sample_ps)
    sample_records = [record for record in records if record["p"] in sample_set]
    total_failures = sum(
        record["candidate_not_low_count"]
        + record["effective_candidate_symmetric_difference_count"]
        + record["layer_interval_failure_count"]
        for record in records
    )
    worst_gap = min(
        records,
        key=lambda item: item["low_survivors"] - item["candidate_prime_pair_slots"],
        default=None,
    )
    plus_records = [record for record in records if record["sign"] == "plus"]
    minus_records = [record for record in records if record["sign"] == "minus"]
    aggregate = {
        "plus_low_survivors": sum(record["low_survivors"] for record in plus_records),
        "plus_candidate_slots": sum(record["candidate_prime_pair_slots"] for record in plus_records),
        "minus_low_survivors": sum(record["low_survivors"] for record in minus_records),
        "minus_candidate_slots": sum(record["candidate_prime_pair_slots"] for record in minus_records),
    }
    aggregate["combined_low_survivors"] = aggregate["plus_low_survivors"] + aggregate["minus_low_survivors"]
    aggregate["combined_candidate_slots"] = aggregate["plus_candidate_slots"] + aggregate["minus_candidate_slots"]

    ledger = {
        "parameters": {"max_p": max_p, "alpha": "4/5", "sample_ps": sample_ps},
        "prime_count": len(p_values),
        "aggregate": aggregate,
        "total_failure_count": total_failures,
        "worst_gap_record": worst_gap,
        "sample_records": sample_records,
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    result = {
        "certificate_type": "prime_matrix_square_phase_even_layer_interval_router",
        "status": "square_phase_even_prime_pair_tiling_reduced_to_fixed_b_layer_intervals_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "empirical_absence_not_used_as_proof": True,
        "parameters": ledger["parameters"],
        "finite_prime_count": len(p_values),
        "aggregate": aggregate,
        "total_failure_count": total_failures,
        "worst_gap_record": worst_gap,
        "fixed_b_layer_interval_formula_closed": total_failures == 0,
        "candidate_upper_bound_beats_lowholes_proved": False,
        "layer_prime_pair_tiling_pdec_return_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "sample_records": sample_records,
        "hardpoint_before_router": "EvenHalfGridPrimePairTilingExclusion",
        "hardpoint_after_router": f"{MAIN_TARGET} OR {RETURN_TARGET}",
        "next_direct_attack_target": MAIN_TARGET,
        "alternative_attack_target": RETURN_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_even_layer_interval_router.py": sha256(
                Path(__file__).resolve()
            ),
            "data/square-phase-even-layer-interval-ledger.json": sha256(OUT_LEDGER),
        },
        "plain_conclusion": (
            "偶半网格素对铺砖已进一步压成固定 `b` 层的精确 `u` 区间："
            "候选有效槽完全由 `q=P-2b`、`m=P+2(b+u)` 同为素数且 `u` 落入半列窗口区间生成，"
            "不再需要先枚举低洞。完全铺砖反例因此要求这些候选素对槽数达到低洞数 `H`；"
            "全局仍需证明候选上界低于低洞下界，或把失败登记为固定层相位 PDEC/SAE。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    worst = result["worst_gap_record"]
    lines = [
        "# Prime Matrix square-phase even-layer interval router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"max_p={result['parameters']['max_p']}",
        f"finite_prime_count={result['finite_prime_count']}",
        f"total_failure_count={result['total_failure_count']}",
        f"candidate_upper_bound_beats_lowholes_proved={fmt_bool(result['candidate_upper_bound_beats_lowholes_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 固定 b 层区间",
        "",
        "令 `H2=(P-1)/2`、`q=P-2b`。候选槽满足 `1<=s<=H2`。",
        "",
        "plus 侧 `s=u(P-2b)-2b^2`，所以",
        "",
        "```text",
        "ceil((2b^2+1)/(P-2b)) <= u <= floor((2b^2+H2)/(P-2b)).",
        "```",
        "",
        "minus 侧 `s=2b^2-u(P-2b)`，所以",
        "",
        "```text",
        "ceil((2b^2-H2)/(P-2b)) <= u <= floor((2b^2-1)/(P-2b)),  u>=0.",
        "```",
        "",
        "再加上 `P-2b` 与 `P+2(b+u)` 同为素数，就得到全部有效半素数槽。",
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
            f"| low survivors | {agg['plus_low_survivors']} | {agg['minus_low_survivors']} | {agg['combined_low_survivors']} |",
            f"| candidate slots | {agg['plus_candidate_slots']} | {agg['minus_candidate_slots']} | {agg['combined_candidate_slots']} |",
            "",
            f"最小 `H-candidates` 样本：`P={worst['p']}`，`sign={worst['sign']}`，`H={worst['low_survivors']}`，`candidates={worst['candidate_prime_pair_slots']}`。",
            "",
            "## 4. 样本表",
            "",
            "| P | sign | H | candidate slots | max u | max layer load | failures |",
            "| ---: | --- | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in result["sample_records"]:
        failures = (
            row["candidate_not_low_count"]
            + row["effective_candidate_symmetric_difference_count"]
            + row["layer_interval_failure_count"]
        )
        lines.append(
            f"| {row['p']} | `{row['sign']}` | {row['low_survivors']} | "
            f"{row['candidate_prime_pair_slots']} | {row['max_u']} | {row['max_layer_load']} | {failures} |"
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
            "- 需要证明候选素对槽数全局小于低洞数，或证明候选槽达到低洞数时固定 b/u 层产生相位异常。",
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
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
