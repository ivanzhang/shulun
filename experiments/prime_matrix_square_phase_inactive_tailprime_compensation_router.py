#!/usr/bin/env python3
"""审计 alpha=4/5 平方锚低洞与未激活尾素的补偿恒等式。

用法示例：
  python3 experiments/prime_matrix_square_phase_inactive_tailprime_compensation_router.py --max-p 5000
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-inactive-tailprime-compensation-router.json

输出：
  data/square-phase-inactive-tailprime-compensation-ledger.json
  docs/monograph/prime-matrix-square-phase-inactive-tailprime-compensation-router.json
  docs/monograph/prime-matrix-square-phase-inactive-tailprime-compensation-router.md
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

OUT_LEDGER = DATA / "square-phase-inactive-tailprime-compensation-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-inactive-tailprime-compensation-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-inactive-tailprime-compensation-router.md"

MAIN_TARGET = "PrimeWindowCountBeatsInactiveTailPrimeCount"
RETURN_TARGET = "InactiveTailPrimeDefectPDECSAEReturn"


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


def primes_from_flags(flags: bytearray, limit: int) -> list[int]:
    """从筛表提取不超过 limit 的素数。"""
    return [idx for idx in range(2, min(limit + 1, len(flags))) if flags[idx]]


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


def cover_residue(p: int, q: int, sign: str) -> int:
    """返回 r 坐标中被 q 覆盖的唯一正残基。"""
    p2_mod = (p * p) % q
    residue = (-p2_mod) % q if sign == "plus" else p2_mod
    return q if residue == 0 else residue


def low_survivor_count(p: int, cutoff: int, sign: str, primes: list[int]) -> int:
    """计算低筛幸存列 H。"""
    covered = bytearray(p)
    for q in primes:
        if q >= p or q > cutoff:
            break
        residue = cover_residue(p, q, sign)
        for r_value in range(residue, p, q):
            covered[r_value] = 1
    return sum(1 for r_value in range(1, p) if not covered[r_value])


def square_prime_count(p: int, sign: str, prime_flags: bytearray) -> int:
    """计算 P^2 正负半窗内的素数个数。"""
    base = p * p
    total = 0
    for r_value in range(1, p):
        n_value = base + r_value if sign == "plus" else base - r_value
        if prime_flags[n_value]:
            total += 1
    return total


def layer_interval_for_b(p: int, b_value: int, sign: str) -> tuple[int, int]:
    """返回固定 b 时 u 的精确可行区间。"""
    half = (p - 1) // 2
    q_value = p - 2 * b_value
    base = 2 * b_value * b_value
    if sign == "plus":
        return ceil_div(base + 1, q_value), (base + half) // q_value
    if sign == "minus":
        return max(0, ceil_div(base - half, q_value)), (base - 1) // q_value
    raise ValueError(f"unknown sign: {sign}")


def raw_and_candidate_slots_for_q(
    p: int, q_value: int, sign: str, prime_flags: bytearray
) -> tuple[int, int, list[int]]:
    """返回尾素 q 的原始槽数、有效素余因子槽数和对应余因子。"""
    b_value = (p - q_value) // 2
    u_min, u_max = layer_interval_for_b(p, b_value, sign)
    if u_max < u_min:
        return 0, 0, []
    cofactors: list[int] = []
    candidate = 0
    for u_value in range(u_min, u_max + 1):
        m_value = p + 2 * (b_value + u_value)
        cofactors.append(m_value)
        if prime_flags[m_value]:
            candidate += 1
    return len(cofactors), candidate, cofactors


def audit_sign(p: int, sign: str, primes: list[int], prime_flags: bytearray) -> dict[str, Any]:
    """审计单个 P 的一个方向。"""
    cutoff = cutoff_alpha45(p)
    tail_primes = [q for q in primes if cutoff < q < p]
    low_count = low_survivor_count(p, cutoff, sign, primes)
    prime_count = square_prime_count(p, sign, prime_flags)

    raw_slots = 0
    candidate_slots = 0
    no_raw_slot_tail_primes = 0
    composite_or_nonprime_slot_tail_primes = 0
    multi_raw_slot_tail_primes = 0
    inactive_samples: list[dict[str, Any]] = []

    for q_value in tail_primes:
        raw_count, candidate_count, cofactors = raw_and_candidate_slots_for_q(
            p, q_value, sign, prime_flags
        )
        raw_slots += raw_count
        candidate_slots += candidate_count
        if raw_count == 0:
            no_raw_slot_tail_primes += 1
            if len(inactive_samples) < 8:
                inactive_samples.append({"q": q_value, "reason": "no_raw_slot"})
        elif candidate_count == 0:
            composite_or_nonprime_slot_tail_primes += 1
            if len(inactive_samples) < 8:
                inactive_samples.append(
                    {
                        "q": q_value,
                        "reason": "cofactor_not_prime",
                        "cofactors": cofactors,
                    }
                )
        if raw_count > 1:
            multi_raw_slot_tail_primes += 1

    inactive_tail_primes = len(tail_primes) - candidate_slots
    low_decomposition_delta = low_count - prime_count - candidate_slots
    compensation_delta = (low_count - len(tail_primes)) - (prime_count - inactive_tail_primes)

    return {
        "p": p,
        "sign": sign,
        "cutoff": cutoff,
        "low_survivors": low_count,
        "prime_window_count": prime_count,
        "tail_prime_count": len(tail_primes),
        "raw_tail_slots": raw_slots,
        "active_candidate_tail_slots": candidate_slots,
        "inactive_tail_primes": inactive_tail_primes,
        "no_raw_slot_tail_primes": no_raw_slot_tail_primes,
        "composite_or_nonprime_slot_tail_primes": composite_or_nonprime_slot_tail_primes,
        "multi_raw_slot_tail_primes": multi_raw_slot_tail_primes,
        "low_minus_tail": low_count - len(tail_primes),
        "prime_minus_inactive": prime_count - inactive_tail_primes,
        "low_decomposition_delta": low_decomposition_delta,
        "compensation_delta": compensation_delta,
        "target_margin_positive": low_count > len(tail_primes),
        "prime_beats_inactive": prime_count > inactive_tail_primes,
        "inactive_samples": inactive_samples,
    }


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的定理行。"""
    return [
        {
            "name": "lowhole_prime_goodslot_decomposition",
            "status": "closed",
            "statement": "H_alpha45^sign(P)=PrimeWindow^sign(P)+GoodTailSlot^sign(P).",
        },
        {
            "name": "inactive_tail_compensation_identity",
            "status": "closed",
            "statement": "H_alpha45^sign(P)-TailPrimeCount_alpha45(P)=PrimeWindow^sign(P)-InactiveTailPrime^sign(P).",
        },
        {
            "name": "failure_forces_prime_deficit",
            "status": "closed",
            "statement": "If H_alpha45^sign(P)<=TailPrimeCount_alpha45(P), then PrimeWindow^sign(P)<=InactiveTailPrime^sign(P).",
        },
        {
            "name": "prime_beats_inactive_tail_input",
            "status": "open",
            "statement": "A global proof still needs PrimeWindow^sign(P)>InactiveTailPrime^sign(P), or a PDEC/SAE exclusion of the opposite defect.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "LowholePrimeGoodSlotDecompositionClosed",
            "closed": result["low_decomposition_failure_count"] == 0,
            "proved": True,
            "meaning": "低洞精确拆成平方端点素数与有效尾素-素余因子槽。",
            "remaining": "closed",
        },
        {
            "gate": "InactiveTailCompensationIdentityClosed",
            "closed": result["compensation_identity_failure_count"] == 0,
            "proved": True,
            "meaning": "`H-tail` 与 `PrimeWindow-inactive tail` 完全相同。",
            "remaining": "closed",
        },
        {
            "gate": "FinitePrimeBeatsInactiveTail",
            "closed": result["finite_prime_inactive_failure_count"] == 0,
            "proved": False,
            "meaning": f"有限扫描 P<={result['parameters']['max_p']} 中 PrimeWindow 均压过 inactive tail。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "GlobalPrimeBeatsInactiveTail",
            "closed": False,
            "proved": False,
            "meaning": "仍需全局证明平方端点素数数压过未激活尾素数。",
            "remaining": MAIN_TARGET,
        },
        {
            "gate": "InactiveTailPrimeDefectPDEC",
            "closed": False,
            "proved": False,
            "meaning": "若 PrimeWindow<=InactiveTail，则必须把未激活尾素优势登记为相位缺陷并排斥。",
            "remaining": RETURN_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步关闭补偿恒等式，不关闭全局行/列命题。",
            "remaining": f"{MAIN_TARGET} OR {RETURN_TARGET}",
        },
    ]


def build_result(max_p: int, sample_ps: list[int]) -> dict[str, Any]:
    """构造路由器结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)

    prime_flags = sieve(max_p * max_p + max_p)
    primes = primes_from_flags(prime_flags, max_p)
    p_values = [p for p in primes if 3 <= p <= max_p]
    records: list[dict[str, Any]] = []
    for p in p_values:
        records.append(audit_sign(p, "plus", primes, prime_flags))
        records.append(audit_sign(p, "minus", primes, prime_flags))

    sample_set = set(sample_ps)
    sample_records = [record for record in records if record["p"] in sample_set]
    low_decomposition_failures = [record for record in records if record["low_decomposition_delta"] != 0]
    compensation_failures = [record for record in records if record["compensation_delta"] != 0]
    prime_inactive_failures = [record for record in records if not record["prime_beats_inactive"]]
    multi_slot_failures = [record for record in records if record["multi_raw_slot_tail_primes"]]
    worst_margin = min(records, key=lambda item: item["prime_minus_inactive"], default=None)
    records_ge_23 = [record for record in records if record["p"] >= 23]
    worst_margin_ge_23 = min(records_ge_23, key=lambda item: item["prime_minus_inactive"], default=None)

    plus_records = [record for record in records if record["sign"] == "plus"]
    minus_records = [record for record in records if record["sign"] == "minus"]
    aggregate = {
        "plus_low_survivors": sum(record["low_survivors"] for record in plus_records),
        "plus_prime_window": sum(record["prime_window_count"] for record in plus_records),
        "plus_tail_primes": sum(record["tail_prime_count"] for record in plus_records),
        "plus_active_candidate_tail_slots": sum(
            record["active_candidate_tail_slots"] for record in plus_records
        ),
        "plus_inactive_tail_primes": sum(record["inactive_tail_primes"] for record in plus_records),
        "minus_low_survivors": sum(record["low_survivors"] for record in minus_records),
        "minus_prime_window": sum(record["prime_window_count"] for record in minus_records),
        "minus_tail_primes": sum(record["tail_prime_count"] for record in minus_records),
        "minus_active_candidate_tail_slots": sum(
            record["active_candidate_tail_slots"] for record in minus_records
        ),
        "minus_inactive_tail_primes": sum(record["inactive_tail_primes"] for record in minus_records),
    }
    aggregate["combined_low_survivors"] = (
        aggregate["plus_low_survivors"] + aggregate["minus_low_survivors"]
    )
    aggregate["combined_prime_window"] = aggregate["plus_prime_window"] + aggregate["minus_prime_window"]
    aggregate["combined_tail_primes"] = aggregate["plus_tail_primes"] + aggregate["minus_tail_primes"]
    aggregate["combined_active_candidate_tail_slots"] = (
        aggregate["plus_active_candidate_tail_slots"]
        + aggregate["minus_active_candidate_tail_slots"]
    )
    aggregate["combined_inactive_tail_primes"] = (
        aggregate["plus_inactive_tail_primes"] + aggregate["minus_inactive_tail_primes"]
    )

    ledger = {
        "parameters": {"max_p": max_p, "alpha": "4/5", "sample_ps": sample_ps},
        "prime_count": len(p_values),
        "aggregate": aggregate,
        "low_decomposition_failure_count": len(low_decomposition_failures),
        "compensation_identity_failure_count": len(compensation_failures),
        "finite_prime_inactive_failure_count": len(prime_inactive_failures),
        "multi_raw_slot_failure_count": len(multi_slot_failures),
        "worst_prime_minus_inactive_record": worst_margin,
        "worst_prime_minus_inactive_record_ge_23": worst_margin_ge_23,
        "sample_records": sample_records,
        "low_decomposition_failures": low_decomposition_failures[:20],
        "compensation_identity_failures": compensation_failures[:20],
        "prime_inactive_failures": prime_inactive_failures[:20],
        "multi_raw_slot_failures": multi_slot_failures[:20],
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    result = {
        "certificate_type": "prime_matrix_square_phase_inactive_tailprime_compensation_router",
        "status": "square_phase_lowhole_tailprime_target_reduced_to_prime_beats_inactive_tail_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "empirical_absence_not_used_as_proof": True,
        "parameters": ledger["parameters"],
        "finite_prime_count": len(p_values),
        "aggregate": aggregate,
        "low_decomposition_failure_count": len(low_decomposition_failures),
        "compensation_identity_failure_count": len(compensation_failures),
        "finite_prime_inactive_failure_count": len(prime_inactive_failures),
        "multi_raw_slot_failure_count": len(multi_slot_failures),
        "worst_prime_minus_inactive_record": worst_margin,
        "worst_prime_minus_inactive_record_ge_23": worst_margin_ge_23,
        "sample_records": sample_records,
        "lowhole_prime_goodslot_decomposition_closed": len(low_decomposition_failures) == 0,
        "inactive_tail_compensation_identity_closed": len(compensation_failures) == 0,
        "global_prime_beats_inactive_tail_proved": False,
        "inactive_tailprime_defect_pdec_return_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": "Alpha45LowHoleCountBeatsTailPrimeCount",
        "hardpoint_after_router": f"{MAIN_TARGET} OR {RETURN_TARGET}",
        "next_direct_attack_target": MAIN_TARGET,
        "alternative_attack_target": RETURN_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_inactive_tailprime_compensation_router.py": sha256(
                Path(__file__).resolve()
            ),
            "data/square-phase-inactive-tailprime-compensation-ledger.json": sha256(OUT_LEDGER),
        },
        "plain_conclusion": (
            "本步把 `Alpha45LowHoleCountBeatsTailPrimeCount` 精确改写为补偿恒等式："
            "`H-tail = PrimeWindow-InactiveTailPrime`。因此若低洞数不能压过尾素数，"
            "不是槽容量本身还缺一项，而是必须出现 `PrimeWindow<=InactiveTailPrime` 的终端缺陷。"
            "有限审计中该缺陷未出现；全局仍需证明平方端点素数数压过未激活尾素数，"
            "或把相反情况登记为可排斥的 PDEC/SAE。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    worst = result["worst_prime_minus_inactive_record"]
    worst_ge_23 = result["worst_prime_minus_inactive_record_ge_23"]
    lines = [
        "# Prime Matrix square-phase inactive tail-prime compensation",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"max_p={result['parameters']['max_p']}",
        f"finite_prime_count={result['finite_prime_count']}",
        f"low_decomposition_failure_count={result['low_decomposition_failure_count']}",
        f"compensation_identity_failure_count={result['compensation_identity_failure_count']}",
        f"finite_prime_inactive_failure_count={result['finite_prime_inactive_failure_count']}",
        f"global_prime_beats_inactive_tail_proved={fmt_bool(result['global_prime_beats_inactive_tail_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 补偿恒等式",
        "",
        "沿用 `alpha=4/5` 与单尾素容量屏障。对每个方向都有",
        "",
        "```text",
        "H = PrimeWindow + GoodTailSlot",
        "TailPrimeCount = GoodTailSlot + InactiveTailPrime",
        "H - TailPrimeCount = PrimeWindow - InactiveTailPrime.",
        "```",
        "",
        "因此当前目标 `H>TailPrimeCount` 等价于",
        "",
        "```text",
        "PrimeWindow > InactiveTailPrime.",
        "```",
        "",
        "反例链若继续存在，就必须把短区间素数数量压到不超过未激活尾素数数量。",
        "",
        "## 2. 判定行",
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
            f"| H low survivors | {agg['plus_low_survivors']} | {agg['minus_low_survivors']} | {agg['combined_low_survivors']} |",
            f"| PrimeWindow | {agg['plus_prime_window']} | {agg['minus_prime_window']} | {agg['combined_prime_window']} |",
            f"| TailPrimeCount | {agg['plus_tail_primes']} | {agg['minus_tail_primes']} | {agg['combined_tail_primes']} |",
            f"| GoodTailSlot | {agg['plus_active_candidate_tail_slots']} | {agg['minus_active_candidate_tail_slots']} | {agg['combined_active_candidate_tail_slots']} |",
            f"| InactiveTailPrime | {agg['plus_inactive_tail_primes']} | {agg['minus_inactive_tail_primes']} | {agg['combined_inactive_tail_primes']} |",
            "",
            f"全扫描最紧 `PrimeWindow-InactiveTail`：`P={worst['p']}`，`sign={worst['sign']}`，`PrimeWindow={worst['prime_window_count']}`，`InactiveTail={worst['inactive_tail_primes']}`，`margin={worst['prime_minus_inactive']}`。",
            f"`P>=23` 最紧样本：`P={worst_ge_23['p']}`，`sign={worst_ge_23['sign']}`，`PrimeWindow={worst_ge_23['prime_window_count']}`，`InactiveTail={worst_ge_23['inactive_tail_primes']}`，`margin={worst_ge_23['prime_minus_inactive']}`。",
            "",
            "## 4. 样本表",
            "",
            "| P | sign | H | PrimeWindow | tail | good slots | inactive | no slot | composite slot | margin |",
            "| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in result["sample_records"]:
        lines.append(
            f"| {row['p']} | `{row['sign']}` | {row['low_survivors']} | {row['prime_window_count']} | "
            f"{row['tail_prime_count']} | {row['active_candidate_tail_slots']} | {row['inactive_tail_primes']} | "
            f"{row['no_raw_slot_tail_primes']} | {row['composite_or_nonprime_slot_tail_primes']} | "
            f"{row['prime_minus_inactive']} |"
        )

    lines.extend(
        [
            "",
            "## 5. 决策表",
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
            "- 这里明确显示：若不引用或证明平方根长度端点素数下界，闭合必须转为排斥 `InactiveTailPrime` 的相位缺陷。",
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
                "low_decomposition_failure_count": result["low_decomposition_failure_count"],
                "compensation_identity_failure_count": result["compensation_identity_failure_count"],
                "finite_prime_inactive_failure_count": result["finite_prime_inactive_failure_count"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
