#!/usr/bin/env python3
"""审计平方锚偶半网格候选槽的尾素容量屏障。

用法示例：
  python3 experiments/prime_matrix_square_phase_tailprime_capacity_barrier_router.py --max-p 5000
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-tailprime-capacity-barrier-router.json

输出：
  data/square-phase-tailprime-capacity-barrier-ledger.json
  docs/monograph/prime-matrix-square-phase-tailprime-capacity-barrier-router.json
  docs/monograph/prime-matrix-square-phase-tailprime-capacity-barrier-router.md
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

OUT_LEDGER = DATA / "square-phase-tailprime-capacity-barrier-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-tailprime-capacity-barrier-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-tailprime-capacity-barrier-router.md"

MAIN_TARGET = "Alpha45LowHoleCountBeatsTailPrimeCount"
RETURN_TARGET = "LowHoleTailPrimeCountFailurePDECSAEReturn"


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


def cover_residue(p: int, q: int, sign: str) -> int:
    """返回 r 坐标中被 q 覆盖的唯一正残基。"""
    p2_mod = (p * p) % q
    residue = (-p2_mod) % q if sign == "plus" else p2_mod
    return q if residue == 0 else residue


def low_survivor_count(p: int, cutoff: int, sign: str, primes: list[int]) -> int:
    """计算低筛幸存列数。"""
    covered = bytearray(p)
    for q in primes:
        if q >= p or q > cutoff:
            break
        residue = cover_residue(p, q, sign)
        for r_value in range(residue, p, q):
            covered[r_value] = 1
    return sum(1 for r_value in range(1, p) if not covered[r_value])


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


def raw_layer_slot_count(p: int, b_value: int, sign: str) -> int:
    """忽略余因子素性时固定 b 层的 u 槽数。"""
    u_min, u_max = layer_interval_for_b(p, b_value, sign)
    return max(0, u_max - u_min + 1)


def audit_sign(p: int, sign: str, primes: list[int], prime_flags: bytearray) -> dict[str, Any]:
    """审计单个 P 的一个方向。"""
    cutoff = cutoff_alpha45(p)
    tail_primes = [q for q in primes if cutoff < q < p]
    low_count = low_survivor_count(p, cutoff, sign, primes)
    raw_slots = 0
    max_raw_slots_per_b = 0
    bad_layer_samples: list[dict[str, int]] = []
    active_layers = 0
    for q_value in tail_primes:
        b_value = (p - q_value) // 2
        count = raw_layer_slot_count(p, b_value, sign)
        raw_slots += count
        if count:
            active_layers += 1
        max_raw_slots_per_b = max(max_raw_slots_per_b, count)
        if count > 1:
            u_min, u_max = layer_interval_for_b(p, b_value, sign)
            bad_layer_samples.append(
                {"q": q_value, "b": b_value, "u_min": u_min, "u_max": u_max, "count": count}
            )

    # 候选素对槽数只会比 raw_slots 更小；这里用筛表直接统计作有限诊断。
    candidate_slots = 0
    for q_value in tail_primes:
        b_value = (p - q_value) // 2
        u_min, u_max = layer_interval_for_b(p, b_value, sign)
        for u_value in range(u_min, u_max + 1):
            m_value = p + 2 * (b_value + u_value)
            if 0 <= m_value < len(prime_flags) and prime_flags[m_value]:
                candidate_slots += 1

    return {
        "p": p,
        "sign": sign,
        "cutoff": cutoff,
        "low_survivors": low_count,
        "tail_prime_count": len(tail_primes),
        "active_tail_layers": active_layers,
        "raw_layer_slots": raw_slots,
        "candidate_prime_pair_slots": candidate_slots,
        "max_raw_slots_per_b": max_raw_slots_per_b,
        "raw_slots_minus_tail_primes": raw_slots - len(tail_primes),
        "candidate_slots_minus_tail_primes": candidate_slots - len(tail_primes),
        "low_minus_tail_primes": low_count - len(tail_primes),
        "low_minus_raw_slots": low_count - raw_slots,
        "low_minus_candidates": low_count - candidate_slots,
        "single_slot_failure_count": len(bad_layer_samples),
        "low_beats_tail_prime_count": low_count > len(tail_primes),
        "bad_layer_samples": bad_layer_samples[:8],
    }


def theorem_rows() -> list[dict[str, str]]:
    """列出本步确定性定理。"""
    return [
        {
            "name": "single_u_slot_per_tail_prime",
            "status": "closed",
            "statement": "For q>P*4/5, the fixed-b u-window has real length <5/8, so each tail prime contributes at most one slot per sign.",
        },
        {
            "name": "candidate_capacity_le_tail_prime_count",
            "status": "closed",
            "statement": "For each sign, candidate prime-pair slots are bounded by the number of tail primes q in (floor(4P/5),P).",
        },
        {
            "name": "full_tiling_forces_H_le_tail_prime_count",
            "status": "closed",
            "statement": "A full effective semiprime tiling would force H_alpha45^sign(P)<=TailPrimeCount_alpha45(P).",
        },
        {
            "name": "remaining_lowhole_beats_tailprime_input",
            "status": "open",
            "statement": "A global proof needs H_alpha45^sign(P)>TailPrimeCount_alpha45(P), or a proof that failure routes to PDEC/SAE.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "SingleTailPrimeSlotCapacityClosed",
            "closed": result["single_slot_failure_count"] == 0,
            "proved": True,
            "meaning": "每个尾素每侧最多贡献一个候选槽。",
            "remaining": "closed",
        },
        {
            "gate": "FiniteLowHoleBeatsTailPrime",
            "closed": result["finite_lowhole_tailprime_failure_count"] == 0,
            "proved": False,
            "meaning": f"有限扫描 P<={result['parameters']['max_p']} 中 H 均大于尾素数。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "GlobalLowHoleBeatsTailPrime",
            "closed": False,
            "proved": False,
            "meaning": "仍需全局证明低洞数超过尾素数，从而排除完全铺砖。",
            "remaining": MAIN_TARGET,
        },
        {
            "gate": "LowHoleTailPrimeFailurePDEC",
            "closed": False,
            "proved": False,
            "meaning": "若 H<=尾素数，必须抽取低洞亏损或尾素容量异常的相位缺陷。",
            "remaining": RETURN_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只关闭候选槽容量上界，不关闭全局行/列命题。",
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
    single_slot_failures = [record for record in records if record["single_slot_failure_count"]]
    lowhole_tail_failures = [record for record in records if not record["low_beats_tail_prime_count"]]
    worst_margin = min(records, key=lambda item: item["low_minus_tail_primes"], default=None)
    plus_records = [record for record in records if record["sign"] == "plus"]
    minus_records = [record for record in records if record["sign"] == "minus"]
    aggregate = {
        "plus_low_survivors": sum(record["low_survivors"] for record in plus_records),
        "plus_tail_primes": sum(record["tail_prime_count"] for record in plus_records),
        "plus_raw_slots": sum(record["raw_layer_slots"] for record in plus_records),
        "plus_candidate_slots": sum(record["candidate_prime_pair_slots"] for record in plus_records),
        "minus_low_survivors": sum(record["low_survivors"] for record in minus_records),
        "minus_tail_primes": sum(record["tail_prime_count"] for record in minus_records),
        "minus_raw_slots": sum(record["raw_layer_slots"] for record in minus_records),
        "minus_candidate_slots": sum(record["candidate_prime_pair_slots"] for record in minus_records),
    }
    aggregate["combined_low_survivors"] = aggregate["plus_low_survivors"] + aggregate["minus_low_survivors"]
    aggregate["combined_tail_primes"] = aggregate["plus_tail_primes"] + aggregate["minus_tail_primes"]
    aggregate["combined_raw_slots"] = aggregate["plus_raw_slots"] + aggregate["minus_raw_slots"]
    aggregate["combined_candidate_slots"] = aggregate["plus_candidate_slots"] + aggregate["minus_candidate_slots"]

    ledger = {
        "parameters": {"max_p": max_p, "alpha": "4/5", "sample_ps": sample_ps},
        "prime_count": len(p_values),
        "aggregate": aggregate,
        "single_slot_failure_count": len(single_slot_failures),
        "finite_lowhole_tailprime_failure_count": len(lowhole_tail_failures),
        "worst_low_minus_tailprime_record": worst_margin,
        "sample_records": sample_records,
        "single_slot_failures": single_slot_failures[:20],
        "lowhole_tailprime_failures": lowhole_tail_failures[:20],
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    result = {
        "certificate_type": "prime_matrix_square_phase_tailprime_capacity_barrier_router",
        "status": "square_phase_even_layer_tiling_reduced_to_lowhole_beats_tailprime_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "empirical_absence_not_used_as_proof": True,
        "parameters": ledger["parameters"],
        "finite_prime_count": len(p_values),
        "aggregate": aggregate,
        "single_slot_failure_count": len(single_slot_failures),
        "finite_lowhole_tailprime_failure_count": len(lowhole_tail_failures),
        "worst_low_minus_tailprime_record": worst_margin,
        "sample_records": sample_records,
        "single_tailprime_slot_capacity_closed": len(single_slot_failures) == 0,
        "global_lowhole_beats_tailprime_proved": False,
        "lowhole_tailprime_failure_pdec_return_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": "EvenLayerPrimePairCandidateUpperBoundBeatsLowHoles",
        "hardpoint_after_router": f"{MAIN_TARGET} OR {RETURN_TARGET}",
        "next_direct_attack_target": MAIN_TARGET,
        "alternative_attack_target": RETURN_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_tailprime_capacity_barrier_router.py": sha256(
                Path(__file__).resolve()
            ),
            "data/square-phase-tailprime-capacity-barrier-ledger.json": sha256(OUT_LEDGER),
        },
        "plain_conclusion": (
            "偶半网格候选槽容量已压到尾素数：由于 `q>P*4/5`，固定 `b` 的 `u` 窗口实长度小于 `5/8`，"
            "所以每个尾素每侧最多贡献一个候选槽。完全有效半素数铺砖因此强制 `H<=TailPrimeCount`。"
            "有限审计中 `H>TailPrimeCount` 全部成立；全局仍需证明 `Alpha45LowHoleCountBeatsTailPrimeCount`，"
            "或证明失败回流为低洞亏损/尾素容量异常的 PDEC/SAE。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    worst = result["worst_low_minus_tailprime_record"]
    lines = [
        "# Prime Matrix square-phase tail-prime capacity barrier",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"max_p={result['parameters']['max_p']}",
        f"finite_prime_count={result['finite_prime_count']}",
        f"single_slot_failure_count={result['single_slot_failure_count']}",
        f"finite_lowhole_tailprime_failure_count={result['finite_lowhole_tailprime_failure_count']}",
        f"global_lowhole_beats_tailprime_proved={fmt_bool(result['global_lowhole_beats_tailprime_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 尾素容量屏障",
        "",
        "固定 `b` 后，plus/minus 的 `u` 可行区间实长度都等于",
        "",
        "```text",
        "((P-1)/2)/(P-2b).",
        "```",
        "",
        "由于尾素层满足 `P-2b>4P/5`，该长度小于 `5/8`，因此每个尾素 `q=P-2b` 每侧最多产生一个候选槽。于是",
        "",
        "```text",
        "candidate_slots^sign(P) <= #{q prime: floor(4P/5)<q<P}.",
        "```",
        "",
        "若发生 full effective semiprime tiling，则必须有",
        "",
        "```text",
        "H_alpha45^sign(P) <= TailPrimeCount_alpha45(P).",
        "```",
        "",
        "所以排除完全铺砖的下一输入是证明低洞数超过尾素数。",
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
            f"| low survivors H | {agg['plus_low_survivors']} | {agg['minus_low_survivors']} | {agg['combined_low_survivors']} |",
            f"| tail prime count | {agg['plus_tail_primes']} | {agg['minus_tail_primes']} | {agg['combined_tail_primes']} |",
            f"| raw layer slots | {agg['plus_raw_slots']} | {agg['minus_raw_slots']} | {agg['combined_raw_slots']} |",
            f"| candidate prime-pair slots | {agg['plus_candidate_slots']} | {agg['minus_candidate_slots']} | {agg['combined_candidate_slots']} |",
            "",
            f"最紧 `H-tail` 样本：`P={worst['p']}`，`sign={worst['sign']}`，`H={worst['low_survivors']}`，`tail={worst['tail_prime_count']}`，`margin={worst['low_minus_tail_primes']}`。",
            "",
            "## 4. 样本表",
            "",
            "| P | sign | H | tail primes | raw slots | candidates | H-tail | H-candidates | max slots/b |",
            "| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in result["sample_records"]:
        lines.append(
            f"| {row['p']} | `{row['sign']}` | {row['low_survivors']} | {row['tail_prime_count']} | "
            f"{row['raw_layer_slots']} | {row['candidate_prime_pair_slots']} | "
            f"{row['low_minus_tail_primes']} | {row['low_minus_candidates']} | {row['max_raw_slots_per_b']} |"
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
            "- 这里不能把有限 `H>tail` 当成全局证明；下一步要给出低洞数下界与尾素数上界的严格比较，或把失败作为 PDEC/SAE 对象。",
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
                "single_slot_failure_count": result["single_slot_failure_count"],
                "finite_lowhole_tailprime_failure_count": result["finite_lowhole_tailprime_failure_count"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
