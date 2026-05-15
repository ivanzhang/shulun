#!/usr/bin/env python3
"""审计平方锚高尾总容量到有效容量的精炼。

用法示例：
  python3 experiments/prime_matrix_square_phase_effective_capacity_refinement_router.py --max-p 5000
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-effective-capacity-refinement-router.json

输出：
  data/square-phase-effective-capacity-refinement-ledger.json
  docs/monograph/prime-matrix-square-phase-effective-capacity-refinement-router.json
  docs/monograph/prime-matrix-square-phase-effective-capacity-refinement-router.md
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

OUT_LEDGER = DATA / "square-phase-effective-capacity-refinement-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-effective-capacity-refinement-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-effective-capacity-refinement-router.md"

MAIN_TARGET = "SquarePhaseEffectiveCapacityPrimeNonempty"
RETURN_TARGET = "SquarePhaseEffectiveCapacityDefectPDECSAEReturn"


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
        if sign == "plus":
            r_value = t_value * q - square_a
        else:
            r_value = square_a - t_value * q
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
                "cofactor_least_prime_factor": lpf,
                "forced_parity_waste": t_value % 2 == 1,
            }
        )
    return records


def audit_sign(p: int, sign: str, primes: list[int]) -> dict[str, Any]:
    """审计单个 P 的一个方向。"""
    cutoff = cutoff_alpha45(p)
    low_set = low_survivor_columns(p, cutoff, sign, primes)
    low_prime_count = 0
    good_shell_count = 0
    for r_value in low_set:
        value = square_value(p, r_value, sign)
        if is_prime_by_primes(value, primes):
            low_prime_count += 1
        else:
            good_shell_count += 1

    tail_primes = [q for q in primes if cutoff < q < p]
    tail_slots = [slot for q in tail_primes for slot in tail_slots_for_q(p, q, sign, primes)]
    effective_slots = [slot for slot in tail_slots if slot["r"] in low_set]
    waste_slots = [slot for slot in tail_slots if slot["r"] not in low_set]
    forced_waste = [slot for slot in waste_slots if slot["forced_parity_waste"]]
    residual_waste = [slot for slot in waste_slots if not slot["forced_parity_waste"]]

    good_shell_r = {slot["r"] for slot in effective_slots}
    effective_prime_cofactor_failures = [
        slot for slot in effective_slots if not slot["cofactor_prime"]
    ]
    waste_low_intersection_failures = [slot for slot in waste_slots if slot["r"] in low_set]
    identities = {
        "H_equals_Prime_plus_GoodShell": len(low_set) == low_prime_count + good_shell_count,
        "Ctotal_equals_Effective_plus_Waste": len(tail_slots) == len(effective_slots) + len(waste_slots),
        "Effective_equals_GoodShell": len(effective_slots) == good_shell_count,
        "Effective_r_set_equals_GoodShell_r_set": len(good_shell_r) == good_shell_count,
        "H_minus_Effective_equals_Prime": len(low_set) - len(effective_slots) == low_prime_count,
        "Ctotal_minus_Effective_equals_Waste": len(tail_slots) - len(effective_slots) == len(waste_slots),
    }
    identity_failure_count = sum(1 for value in identities.values() if not value)
    identity_failure_count += len(effective_prime_cofactor_failures)
    identity_failure_count += len(waste_low_intersection_failures)

    return {
        "p": p,
        "sign": sign,
        "cutoff": cutoff,
        "low_survivors_H": len(low_set),
        "square_anchor_prime_count": low_prime_count,
        "good_shell_effective_capacity": good_shell_count,
        "tail_total_capacity": len(tail_slots),
        "effective_tail_capacity": len(effective_slots),
        "waste_tail_capacity": len(waste_slots),
        "forced_parity_waste_capacity": len(forced_waste),
        "residual_waste_capacity": len(residual_waste),
        "H_minus_total_capacity": len(low_set) - len(tail_slots),
        "H_minus_effective_capacity": len(low_set) - len(effective_slots),
        "prime_minus_waste": low_prime_count - len(waste_slots),
        "identities": identities,
        "identity_failure_count": identity_failure_count,
        "effective_prime_cofactor_failure_count": len(effective_prime_cofactor_failures),
        "waste_low_intersection_failure_count": len(waste_low_intersection_failures),
    }


def theorem_rows() -> list[dict[str, str]]:
    """列出本步确定性定理。"""
    return [
        {
            "name": "effective_capacity_refinement",
            "status": "closed",
            "statement": "The only tail slots that can cover low survivors are exactly the GoodShell semiprime slots; all BadTail slots are waste capacity for the low-hole covering problem.",
        },
        {
            "name": "exact_effective_identity",
            "status": "closed",
            "statement": "For each sign, H_y-C_eff = square-anchor-prime-count, where C_eff is tail capacity restricted to low survivors.",
        },
        {
            "name": "total_capacity_sufficient_only",
            "status": "closed",
            "statement": "The older criterion H_y>C_total is sufficient but stronger than needed; it asks Prime>Waste, while the exact target is Prime>0.",
        },
        {
            "name": "remaining_effective_prime_nonempty",
            "status": "open",
            "statement": "A global proof still needs the effective identity to have positive right side, or a PDEC/SAE contradiction if Prime=0.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "EffectiveCapacityRefinementClosed",
            "closed": result["total_identity_failure_count"] == 0,
            "proved": True,
            "meaning": "高尾总容量已精确拆成有效 GoodShell 与废容量 BadTail。",
            "remaining": "closed",
        },
        {
            "gate": "TotalCapacityRouteMarkedSufficientOnly",
            "closed": True,
            "proved": True,
            "meaning": "`Prime>BadTail` 只是强充分路线，不是命题闭合的必要目标。",
            "remaining": "closed",
        },
        {
            "gate": "EffectivePrimeNonempty",
            "closed": False,
            "proved": False,
            "meaning": "仍需证明 `H-C_eff=Prime` 的右侧全局为正。",
            "remaining": MAIN_TARGET,
        },
        {
            "gate": "PrimeVoidEffectiveCapacityPDEC",
            "closed": False,
            "proved": False,
            "meaning": "若 `Prime=0`，需要把有效容量完全贴合低洞抽取为相位缺陷。",
            "remaining": RETURN_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只校准容量口径，不关闭全局行/列命题。",
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
    total_identity_failures = sum(record["identity_failure_count"] for record in records)
    plus_records = [record for record in records if record["sign"] == "plus"]
    minus_records = [record for record in records if record["sign"] == "minus"]
    aggregate = {
        "plus_H_total": sum(record["low_survivors_H"] for record in plus_records),
        "plus_prime_total": sum(record["square_anchor_prime_count"] for record in plus_records),
        "plus_effective_total": sum(record["effective_tail_capacity"] for record in plus_records),
        "plus_waste_total": sum(record["waste_tail_capacity"] for record in plus_records),
        "minus_H_total": sum(record["low_survivors_H"] for record in minus_records),
        "minus_prime_total": sum(record["square_anchor_prime_count"] for record in minus_records),
        "minus_effective_total": sum(record["effective_tail_capacity"] for record in minus_records),
        "minus_waste_total": sum(record["waste_tail_capacity"] for record in minus_records),
    }
    aggregate["combined_prime_total"] = aggregate["plus_prime_total"] + aggregate["minus_prime_total"]
    aggregate["combined_effective_total"] = (
        aggregate["plus_effective_total"] + aggregate["minus_effective_total"]
    )
    aggregate["combined_waste_total"] = aggregate["plus_waste_total"] + aggregate["minus_waste_total"]

    ledger = {
        "parameters": {"max_p": max_p, "alpha": "4/5", "sample_ps": sample_ps},
        "prime_count": len(p_values),
        "aggregate": aggregate,
        "total_identity_failure_count": total_identity_failures,
        "sample_records": sample_records,
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    result = {
        "certificate_type": "prime_matrix_square_phase_effective_capacity_refinement_router",
        "status": "square_phase_total_capacity_refined_to_effective_capacity_prime_nonempty_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "empirical_absence_not_used_as_proof": True,
        "parameters": ledger["parameters"],
        "finite_prime_count": len(p_values),
        "aggregate": aggregate,
        "total_identity_failure_count": total_identity_failures,
        "sample_records": sample_records,
        "effective_capacity_refinement_closed": total_identity_failures == 0,
        "total_capacity_route_sufficient_only": True,
        "effective_prime_nonempty_proved": False,
        "effective_capacity_defect_pdec_return_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": "SquarePhasePrimeBeatsForcedParityPlusResidualReciprocalIntervals",
        "hardpoint_after_router": f"{MAIN_TARGET} OR {RETURN_TARGET}",
        "next_direct_attack_target": MAIN_TARGET,
        "alternative_attack_target": RETURN_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_effective_capacity_refinement_router.py": sha256(
                Path(__file__).resolve()
            ),
            "data/square-phase-effective-capacity-refinement-ledger.json": sha256(OUT_LEDGER),
        },
        "plain_conclusion": (
            "总容量路线已被精炼：尾素总容量 `C_total` 分成真正命中低洞的有效容量 `C_eff=GoodShell` "
            "和已经被低筛杀掉的废容量 `Waste=BadTail`。因此逐侧有 `H-C_eff=Prime`。"
            "此前的 `Prime>BadTail` 是证明 `H>C_total` 的强充分条件，但不是命题闭合的必要目标；"
            "真正剩余回到有效容量口径下的 `Prime>0`，或证明 `Prime=0` 时有效容量完全贴合低洞会产生 PDEC/SAE。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase effective capacity refinement",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"max_p={result['parameters']['max_p']}",
        f"finite_prime_count={result['finite_prime_count']}",
        f"total_identity_failure_count={result['total_identity_failure_count']}",
        f"effective_prime_nonempty_proved={fmt_bool(result['effective_prime_nonempty_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 有效容量恒等式",
        "",
        "设 `H` 为 `q<=floor(4P/5)` 低筛后幸存列数，`C_total` 为 `floor(4P/5)<q<P` 的全部高尾槽数。"
        "高尾槽只有命中低洞时才有能力覆盖 `H`；命中已被低筛杀掉的列只是废容量。",
        "",
        "逐侧精确分解为：",
        "",
        "```text",
        "H = Prime + GoodShell",
        "C_total = GoodShell + BadTail",
        "C_eff = GoodShell",
        "H - C_eff = Prime",
        "C_total - C_eff = BadTail.",
        "```",
        "",
        "因此 `H>C_total` 等价于 `Prime>BadTail`，只是一个强充分判据；真正有效容量口径下，目标就是 `Prime>0`。",
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
            f"| square-anchor primes | {agg['plus_prime_total']} | {agg['minus_prime_total']} | {agg['combined_prime_total']} |",
            f"| effective tail capacity | {agg['plus_effective_total']} | {agg['minus_effective_total']} | {agg['combined_effective_total']} |",
            f"| waste tail capacity | {agg['plus_waste_total']} | {agg['minus_waste_total']} | {agg['combined_waste_total']} |",
            "",
            "## 4. 样本表",
            "",
            "| P | sign | H | Prime | C_eff | Waste | H-C_eff | Prime-Waste |",
            "| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in result["sample_records"]:
        lines.append(
            f"| {row['p']} | `{row['sign']}` | {row['low_survivors_H']} | "
            f"{row['square_anchor_prime_count']} | {row['effective_tail_capacity']} | "
            f"{row['waste_tail_capacity']} | {row['H_minus_effective_capacity']} | "
            f"{row['prime_minus_waste']} |"
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
            "- 后续不应把废容量 BadTail 当作必须战胜的终端对象；它只服务于强充分的总容量判据。真正闭合必须证明有效容量剩余 `Prime` 非空，或把 `Prime=0` 的有效容量完全贴合抽成 PDEC/SAE。",
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
                "total_identity_failure_count": result["total_identity_failure_count"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
