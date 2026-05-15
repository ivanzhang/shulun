#!/usr/bin/env python3
"""审计平方锚残余 LPF 坏槽的倒数短区间公式。

用法示例：
  python3 experiments/prime_matrix_square_phase_residual_lpf_reciprocal_router.py --max-p 5000
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-residual-lpf-reciprocal-router.json

输出：
  data/square-phase-residual-lpf-reciprocal-ledger.json
  docs/monograph/prime-matrix-square-phase-residual-lpf-reciprocal-router.json
  docs/monograph/prime-matrix-square-phase-residual-lpf-reciprocal-router.md
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

OUT_LEDGER = DATA / "square-phase-residual-lpf-reciprocal-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-residual-lpf-reciprocal-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-residual-lpf-reciprocal-router.md"

MAIN_TARGET = "SquarePhasePrimeBeatsForcedParityPlusResidualReciprocalIntervals"
RETURN_TARGET = "ResidualLPFReciprocalIntervalPDECSAEReturn"


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
    """用已知素数表判定素性。"""
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
        if sign == "plus":
            r_value = t_value * q - square_a
            value = p * p + r_value
        else:
            r_value = square_a - t_value * q
            value = p * p - r_value
        cofactor = p + a_value + t_value
        lpf = least_prime_factor(cofactor, primes)
        records.append(
            {
                "q": q,
                "a": a_value,
                "t": t_value,
                "r": r_value,
                "cofactor_m": cofactor,
                "value": value,
                "cofactor_prime": lpf == cofactor,
                "cofactor_least_prime_factor": lpf,
                "forced_parity_bad": t_value % 2 == 1,
            }
        )
    return records


def residual_slots(p: int, sign: str, primes: list[int]) -> list[dict[str, Any]]:
    """返回非奇偶强制的残余 LPF 坏槽。"""
    cutoff = cutoff_alpha45(p)
    tail_primes = [q for q in primes if cutoff < q < p]
    slots = [slot for q in tail_primes for slot in tail_slots_for_q(p, q, sign, primes)]
    return [
        slot
        for slot in slots
        if (not slot["cofactor_prime"]) and (not slot["forced_parity_bad"])
    ]


def reciprocal_record(p: int, sign: str, slot: dict[str, Any]) -> dict[str, Any]:
    """把残余槽改写为倒数短区间记录。"""
    ell = slot["cofactor_least_prime_factor"]
    h_value = slot["cofactor_m"] // ell
    denominator = ell * h_value
    if sign == "plus":
        low = p * p
        high = p * p + p
    elif sign == "minus":
        low = p * p - p
        high = p * p
    else:
        raise ValueError(f"unknown sign: {sign}")
    q_min = low // denominator + 1
    q_max = (high - 1) // denominator
    q_value = slot["q"]
    product = q_value * denominator
    return {
        "q": q_value,
        "a": slot["a"],
        "t": slot["t"],
        "r": slot["r"],
        "ell": ell,
        "h": h_value,
        "cofactor_m": slot["cofactor_m"],
        "denominator_ell_h": denominator,
        "product": product,
        "interval_low_open": low,
        "interval_high_open": high,
        "q_candidate_min": q_min,
        "q_candidate_max": q_max,
        "candidate_width_int": q_max - q_min + 1,
        "q_in_reciprocal_interval": q_min <= q_value <= q_max,
        "single_integer_candidate": q_min == q_max,
        "q_is_the_single_candidate": q_min == q_max == q_value,
        "tail_prime_condition": cutoff_alpha45(p) < q_value < p,
    }


def audit_sign(p: int, sign: str, primes: list[int]) -> dict[str, Any]:
    """审计单个 P 的一个方向。"""
    residual = residual_slots(p, sign, primes)
    records = [reciprocal_record(p, sign, slot) for slot in residual]
    interval_failures = [
        record
        for record in records
        if not record["q_in_reciprocal_interval"]
        or not record["single_integer_candidate"]
        or not record["q_is_the_single_candidate"]
        or not record["tail_prime_condition"]
    ]
    pair_keys: dict[tuple[int, int], int] = {}
    pair_reuse_failures: list[dict[str, Any]] = []
    ell_histogram: dict[int, int] = {}
    for record in records:
        key = (record["ell"], record["h"])
        pair_keys[key] = pair_keys.get(key, 0) + 1
        if pair_keys[key] > 1:
            pair_reuse_failures.append(record)
        ell = record["ell"]
        ell_histogram[ell] = ell_histogram.get(ell, 0) + 1
    return {
        "p": p,
        "sign": sign,
        "residual_lpf_slot_count": len(records),
        "interval_failure_count": len(interval_failures),
        "ell_h_reuse_failure_count": len(pair_reuse_failures),
        "ell_histogram": dict(sorted(ell_histogram.items())),
        "max_ell": max((record["ell"] for record in records), default=0),
        "max_h": max((record["h"] for record in records), default=0),
        "sample_records": records[:10],
        "failure_samples": {
            "interval": interval_failures[:3],
            "ell_h_reuse": pair_reuse_failures[:3],
        },
    }


def theorem_rows() -> list[dict[str, str]]:
    """列出本步确定性定理。"""
    return [
        {
            "name": "residual_lpf_reciprocal_interval_formula",
            "status": "closed",
            "statement": "A residual slot with m=ell*h is equivalent to q lying in the reciprocal interval P^2/(ell*h)<q<(P^2+P)/(ell*h) on plus, or (P^2-P)/(ell*h)<q<P^2/(ell*h) on minus.",
        },
        {
            "name": "single_integer_candidate_per_ell_h",
            "status": "closed",
            "statement": "Since ell*h=m>P, each reciprocal interval has length P/(ell*h)<1, so it contains at most one integer q.",
        },
        {
            "name": "residual_overdensity_pdec_object",
            "status": "open",
            "statement": "Residual LPF over-density must appear as many distinct reciprocal intervals whose unique integer candidate is a tail prime.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "ResidualReciprocalFormulaClosed",
            "closed": result["total_interval_failure_count"] == 0,
            "proved": True,
            "meaning": "每个残余 LPF 坏槽都等价于一个倒数短区间中的唯一整数尾素候选。",
            "remaining": "closed",
        },
        {
            "gate": "EllHNonreuseClosed",
            "closed": result["total_ell_h_reuse_failure_count"] == 0,
            "proved": True,
            "meaning": "固定同侧 `(ell,h)` 不复用 q 候选。",
            "remaining": "closed",
        },
        {
            "gate": "PrimeBeatsForcedPlusResidualIntervals",
            "closed": False,
            "proved": False,
            "meaning": "仍需证明平方锚素数数压过强制奇偶层与这些残余倒数区间命中。",
            "remaining": MAIN_TARGET,
        },
        {
            "gate": "ResidualReciprocalIntervalPDEC",
            "closed": False,
            "proved": False,
            "meaning": "若残余倒数区间命中过密，需抽取尾素在倒数短区间族中的相位缺陷。",
            "remaining": RETURN_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只关闭残余 LPF 的倒数区间化，不关闭全局行/列命题。",
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
    total_interval_failures = sum(record["interval_failure_count"] for record in records)
    total_reuse_failures = sum(record["ell_h_reuse_failure_count"] for record in records)
    plus_records = [record for record in records if record["sign"] == "plus"]
    minus_records = [record for record in records if record["sign"] == "minus"]
    aggregate = {
        "plus_residual_lpf_slots": sum(record["residual_lpf_slot_count"] for record in plus_records),
        "minus_residual_lpf_slots": sum(record["residual_lpf_slot_count"] for record in minus_records),
        "plus_max_ell": max((record["max_ell"] for record in plus_records), default=0),
        "minus_max_ell": max((record["max_ell"] for record in minus_records), default=0),
        "plus_max_h": max((record["max_h"] for record in plus_records), default=0),
        "minus_max_h": max((record["max_h"] for record in minus_records), default=0),
    }
    aggregate["combined_residual_lpf_slots"] = (
        aggregate["plus_residual_lpf_slots"] + aggregate["minus_residual_lpf_slots"]
    )

    ledger = {
        "parameters": {"max_p": max_p, "alpha": "4/5", "sample_ps": sample_ps},
        "prime_count": len(p_values),
        "aggregate": aggregate,
        "total_interval_failure_count": total_interval_failures,
        "total_ell_h_reuse_failure_count": total_reuse_failures,
        "sample_records": sample_records,
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    result = {
        "certificate_type": "prime_matrix_square_phase_residual_lpf_reciprocal_router",
        "status": "square_phase_residual_lpf_reduced_to_reciprocal_short_intervals_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "empirical_absence_not_used_as_proof": True,
        "parameters": ledger["parameters"],
        "finite_prime_count": len(p_values),
        "aggregate": aggregate,
        "total_interval_failure_count": total_interval_failures,
        "total_ell_h_reuse_failure_count": total_reuse_failures,
        "sample_records": sample_records,
        "residual_reciprocal_formula_closed": total_interval_failures == 0,
        "ell_h_nonreuse_closed": total_reuse_failures == 0,
        "prime_beats_forced_plus_residual_intervals_proved": False,
        "residual_reciprocal_pdec_return_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": "ResidualLPFLayerPDECSAEReturn",
        "hardpoint_after_router": f"{MAIN_TARGET} OR {RETURN_TARGET}",
        "next_direct_attack_target": MAIN_TARGET,
        "alternative_attack_target": RETURN_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_residual_lpf_reciprocal_router.py": sha256(
                Path(__file__).resolve()
            ),
            "data/square-phase-residual-lpf-reciprocal-ledger.json": sha256(OUT_LEDGER),
        },
        "plain_conclusion": (
            "残余 LPF 坏槽已进一步改写成倒数短区间对象：若 `m=ell*h`，"
            "plus 侧要求 `P^2<q ell h<P^2+P`，minus 侧要求 `P^2-P<q ell h<P^2`。"
            "由于 `ell*h=m>P`，每个 `(ell,h)` 对应的 q-区间长度小于 `1`，所以至多有一个整数候选。"
            "因此残余层过密不可能来自同一 `(ell,h)` 的多重复用，只能来自大量倒数短区间的唯一整数候选同时为尾素；"
            "这正是下一步的 PDEC/SAE 对象。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase residual LPF reciprocal router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"max_p={result['parameters']['max_p']}",
        f"finite_prime_count={result['finite_prime_count']}",
        f"total_interval_failure_count={result['total_interval_failure_count']}",
        f"total_ell_h_reuse_failure_count={result['total_ell_h_reuse_failure_count']}",
        f"prime_beats_forced_plus_residual_intervals_proved={fmt_bool(result['prime_beats_forced_plus_residual_intervals_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 倒数短区间公式",
        "",
        "残余坏槽有 `m=ell*h`，其中 `ell` 是 `m` 的奇最小素因子。于是",
        "",
        "```text",
        "plus:  P^2 < q*ell*h < P^2+P",
        "minus: P^2-P < q*ell*h < P^2",
        "```",
        "",
        "等价地，固定 `(ell,h)` 后，`q` 必须落入一个长度小于 `1` 的倒数短区间。"
        "所以同一 `(ell,h)` 在同侧至多给出一个整数候选，更不可能产生高重数覆盖。",
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
            f"| residual LPF slots | {agg['plus_residual_lpf_slots']} | {agg['minus_residual_lpf_slots']} | {agg['combined_residual_lpf_slots']} |",
            f"| max ell | {agg['plus_max_ell']} | {agg['minus_max_ell']} | - |",
            f"| max h | {agg['plus_max_h']} | {agg['minus_max_h']} | - |",
            "",
            "## 4. 样本表",
            "",
            "| P | sign | residual slots | max ell | max h | interval failures | ell,h reuse failures |",
            "| ---: | --- | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in result["sample_records"]:
        lines.append(
            f"| {row['p']} | `{row['sign']}` | {row['residual_lpf_slot_count']} | "
            f"{row['max_ell']} | {row['max_h']} | {row['interval_failure_count']} | "
            f"{row['ell_h_reuse_failure_count']} |"
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
            "- 当前不能把倒数区间有限审计升级为全局素数下界；它只提供残余 LPF 过密时的精确 PDEC/SAE 载体。",
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
                "total_interval_failure_count": result["total_interval_failure_count"],
                "total_ell_h_reuse_failure_count": result["total_ell_h_reuse_failure_count"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
