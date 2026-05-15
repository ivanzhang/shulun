#!/usr/bin/env python3
"""审计平方锚 alpha=4/5 坏尾命中的单变量槽余因子公式。

用法示例：
  python3 experiments/prime_matrix_square_phase_bad_tail_single_variable_router.py --max-p 5000
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-bad-tail-single-variable-router.json

输出：
  data/square-phase-bad-tail-single-variable-ledger.json
  docs/monograph/prime-matrix-square-phase-bad-tail-single-variable-router.json
  docs/monograph/prime-matrix-square-phase-bad-tail-single-variable-router.md
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

OUT_LEDGER = DATA / "square-phase-bad-tail-single-variable-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-bad-tail-single-variable-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-bad-tail-single-variable-router.md"

MAIN_TARGET = "SquarePhaseBadTailShiftedCompositeCofactorSlotBound"
RETURN_TARGET = "SquarePhaseBadTailShiftedCofactorSlotPDECSAEReturn"


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


def tail_records_for_q(p: int, q: int, sign: str, primes: list[int]) -> list[dict[str, Any]]:
    """给出尾素 q=P-a 的全部命中槽及余因子。"""
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
        cofactor_prime = lpf == cofactor
        records.append(
            {
                "p": p,
                "sign": sign,
                "q": q,
                "a": a_value,
                "t": t_value,
                "r": r_value,
                "cofactor_m": cofactor,
                "value": value,
                "product_identity_ok": value == q * cofactor,
                "r_in_window": 1 <= r_value < p,
                "cofactor_prime": cofactor_prime,
                "cofactor_least_prime_factor": lpf,
                "bad_tail": not cofactor_prime,
            }
        )
    return records


def audit_sign(p: int, sign: str, primes: list[int]) -> dict[str, Any]:
    """审计单个 P 的 plus/minus 坏尾单变量槽公式。"""
    cutoff = cutoff_alpha45(p)
    tail_primes = [q for q in primes if cutoff < q < p]
    records = [record for q in tail_primes for record in tail_records_for_q(p, q, sign, primes)]
    bad_records = [record for record in records if record["bad_tail"]]
    good_records = [record for record in records if not record["bad_tail"]]
    identity_failures = [
        record for record in records if not record["product_identity_ok"] or not record["r_in_window"]
    ]
    t_histogram: dict[int, int] = {}
    bad_t_histogram: dict[int, int] = {}
    lpf_histogram: dict[int, int] = {}
    for record in records:
        t_value = record["t"]
        t_histogram[t_value] = t_histogram.get(t_value, 0) + 1
        if record["bad_tail"]:
            bad_t_histogram[t_value] = bad_t_histogram.get(t_value, 0) + 1
            lpf = record["cofactor_least_prime_factor"]
            lpf_histogram[lpf] = lpf_histogram.get(lpf, 0) + 1
    return {
        "p": p,
        "sign": sign,
        "cutoff": cutoff,
        "distinct_tail_prime_count": len(tail_primes),
        "tail_slot_count": len(records),
        "good_tail_prime_cofactor_count": len(good_records),
        "bad_tail_composite_cofactor_count": len(bad_records),
        "bad_tail_ratio": 0.0 if not records else len(bad_records) / len(records),
        "identity_failure_count": len(identity_failures),
        "min_t": min((record["t"] for record in records), default=0),
        "max_t": max((record["t"] for record in records), default=0),
        "bad_min_t": min((record["t"] for record in bad_records), default=0),
        "bad_max_t": max((record["t"] for record in bad_records), default=0),
        "t_histogram": dict(sorted(t_histogram.items())),
        "bad_t_histogram": dict(sorted(bad_t_histogram.items())),
        "bad_lpf_histogram": dict(sorted(lpf_histogram.items())),
        "tail_sample": records[:10],
        "bad_tail_sample": bad_records[:10],
        "identity_failures": identity_failures[:10],
    }


def theorem_rows() -> list[dict[str, str]]:
    """列出本步确定性定理。"""
    return [
        {
            "name": "tail_prime_one_or_two_slots",
            "status": "closed",
            "statement": "For alpha=4/5, every tail prime q in (4P/5,P) hits one or two r slots in 1<=r<P on each side.",
        },
        {
            "name": "single_variable_slot_cofactor_formula",
            "status": "closed",
            "statement": "Writing q=P-a, all plus slots have r=tq-a^2 and m=P+a+t; all minus slots have r=a^2-tq and m=P+a+t, for the integer t range forced by 1<=r<P.",
        },
        {
            "name": "bad_tail_equivalence",
            "status": "closed",
            "statement": "The tail hit is BadTail exactly when the slot cofactor m=P+a+t is composite.",
        },
        {
            "name": "remaining_shifted_composite_slot_bound",
            "status": "open",
            "statement": "A global proof needs a bound for composite slot values P+a+t along tail-prime parameters q=P-a, or a PDEC/SAE return.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "SingleVariableSlotBadTailFormulaClosed",
            "closed": result["identity_failure_count"] == 0,
            "proved": True,
            "meaning": "每个尾素命中的全部 r 槽和余因子 m 都由 a=P-q 与整数槽 t 的单变量公式给出。",
            "remaining": "closed",
        },
        {
            "gate": "BadTailCompositeCofactorSlotBound",
            "closed": False,
            "proved": False,
            "meaning": "仍需全局约束 m=P+a+t 为合数的尾素槽数量。",
            "remaining": MAIN_TARGET,
        },
        {
            "gate": "ShiftedCofactorSlotPDECReturn",
            "closed": False,
            "proved": False,
            "meaning": "若复合余因子过密，需抽取按 t 槽层分布的低模相位异常。",
            "remaining": RETURN_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只关闭 BadTail 的单变量槽参数化，不关闭全局行/列命题。",
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

    identity_failures = [record for record in records if record["identity_failure_count"]]
    plus_records = [record for record in records if record["sign"] == "plus"]
    minus_records = [record for record in records if record["sign"] == "minus"]
    worst_plus_bad_ratio = max(plus_records, key=lambda item: item["bad_tail_ratio"], default=None)
    worst_minus_bad_ratio = max(minus_records, key=lambda item: item["bad_tail_ratio"], default=None)
    max_plus_t = max(plus_records, key=lambda item: item["max_t"], default=None)
    max_minus_t = max(minus_records, key=lambda item: item["max_t"], default=None)
    sample_set = set(sample_ps)
    sample_records = [record for record in records if record["p"] in sample_set]

    aggregate = {
        "plus_distinct_tail_prime_total": sum(record["distinct_tail_prime_count"] for record in plus_records),
        "plus_tail_slot_total": sum(record["tail_slot_count"] for record in plus_records),
        "plus_bad_tail_total": sum(record["bad_tail_composite_cofactor_count"] for record in plus_records),
        "plus_good_tail_total": sum(record["good_tail_prime_cofactor_count"] for record in plus_records),
        "minus_distinct_tail_prime_total": sum(record["distinct_tail_prime_count"] for record in minus_records),
        "minus_tail_slot_total": sum(record["tail_slot_count"] for record in minus_records),
        "minus_bad_tail_total": sum(record["bad_tail_composite_cofactor_count"] for record in minus_records),
        "minus_good_tail_total": sum(record["good_tail_prime_cofactor_count"] for record in minus_records),
    }

    ledger = {
        "parameters": {"max_p": max_p, "alpha": "4/5", "sample_ps": sample_ps},
        "prime_count": len(p_values),
        "aggregate": aggregate,
        "identity_failure_count": len(identity_failures),
        "worst_plus_bad_ratio": worst_plus_bad_ratio,
        "worst_minus_bad_ratio": worst_minus_bad_ratio,
        "max_plus_t_record": max_plus_t,
        "max_minus_t_record": max_minus_t,
        "sample_records": sample_records,
        "identity_failures": identity_failures[:20],
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    result = {
        "certificate_type": "prime_matrix_square_phase_bad_tail_single_variable_router",
        "status": "square_phase_bad_tail_reduced_to_shifted_composite_cofactor_slot_bound_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "empirical_absence_not_used_as_proof": True,
        "parameters": ledger["parameters"],
        "finite_prime_count": len(p_values),
        "aggregate": aggregate,
        "identity_failure_count": len(identity_failures),
        "worst_plus_bad_ratio": worst_plus_bad_ratio,
        "worst_minus_bad_ratio": worst_minus_bad_ratio,
        "max_plus_t_record": max_plus_t,
        "max_minus_t_record": max_minus_t,
        "sample_records": sample_records,
        "single_variable_slot_bad_tail_formula_closed": len(identity_failures) == 0,
        "bad_tail_composite_cofactor_slot_bound_proved": False,
        "shifted_cofactor_slot_pdec_return_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": "SquarePhaseAlphaFourFifthsPrimeDominatesBadTailCompositeCofactor",
        "hardpoint_after_router": f"{MAIN_TARGET} OR {RETURN_TARGET}",
        "next_direct_attack_target": MAIN_TARGET,
        "alternative_attack_target": RETURN_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_bad_tail_single_variable_router.py": sha256(
                Path(__file__).resolve()
            ),
            "data/square-phase-bad-tail-single-variable-ledger.json": sha256(OUT_LEDGER),
        },
        "plain_conclusion": (
            "坏尾命中已经从高尾覆盖问题压成单变量槽余因子问题：对每个尾素 `q=P-a`，"
            "plus 侧全部命中满足 `r=tq-a^2, m=P+a+t`；minus 侧全部命中满足 `r=a^2-tq, m=P+a+t`，"
            "其中整数槽 `t` 由 `1<=r<P` 限定为一到两个值。"
            "该槽命中是 `BadTail` 当且仅当 `m` 为合数。因此下一步只需控制这些移位余因子合数槽的数量，"
            "或证明其过密形成 t 层上的 PDEC/SAE。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase bad-tail single-variable router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"max_p={result['parameters']['max_p']}",
        f"finite_prime_count={result['finite_prime_count']}",
        f"identity_failure_count={result['identity_failure_count']}",
        f"bad_tail_composite_cofactor_slot_bound_proved={fmt_bool(result['bad_tail_composite_cofactor_slot_bound_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 单变量槽公式",
        "",
        "令 `y=floor(4P/5)`，取尾素 `q` 满足 `y<q<P`，写 `q=P-a`。因为 `q>4P/5`，"
        "每个 `q` 在 `1<=r<P` 中逐侧只命中一到两个相位槽。",
        "",
        "plus 侧所有槽由整数 `t` 给出：",
        "",
        "```text",
        "r_+(a,t)=t(P-a)-a^2",
        "P^2+r_+(a,t)=(P-a)(P+a+t)",
        "1<=r_+(a,t)<P",
        "```",
        "",
        "minus 侧所有槽由整数 `t` 给出：",
        "",
        "```text",
        "r_-(a,t)=a^2-t(P-a)",
        "P^2-r_-(a,t)=(P-a)(P+a+t)",
        "1<=r_-(a,t)<P",
        "```",
        "",
        "所以坏尾不再需要二维搜索：它等价于这些槽上的 `P+a+t` 为合数。",
        "",
        "## 2. 确定性判据",
        "",
        "| name | status | statement |",
        "| --- | --- | --- |",
    ]
    for item in result["theorem_rows"]:
        lines.append(f"| `{item['name']}` | `{item['status']}` | {table_cell(item['statement'])} |")

    plus_ratio = result["worst_plus_bad_ratio"]
    minus_ratio = result["worst_minus_bad_ratio"]
    max_plus_t = result["max_plus_t_record"]
    max_minus_t = result["max_minus_t_record"]
    lines.extend(
        [
            "",
            "## 3. 有限审计摘要",
            "",
            "| metric | plus | minus |",
            "| --- | ---: | ---: |",
            f"| distinct tail primes | {result['aggregate']['plus_distinct_tail_prime_total']} | {result['aggregate']['minus_distinct_tail_prime_total']} |",
            f"| tail slots | {result['aggregate']['plus_tail_slot_total']} | {result['aggregate']['minus_tail_slot_total']} |",
            f"| good cofactor prime slots | {result['aggregate']['plus_good_tail_total']} | {result['aggregate']['minus_good_tail_total']} |",
            f"| bad composite cofactor slots | {result['aggregate']['plus_bad_tail_total']} | {result['aggregate']['minus_bad_tail_total']} |",
            "",
            f"- plus 最大坏尾比例样本：`P={plus_ratio['p']}`，`bad/slots={plus_ratio['bad_tail_composite_cofactor_count']}/{plus_ratio['tail_slot_count']}`。",
            f"- minus 最大坏尾比例样本：`P={minus_ratio['p']}`，`bad/slots={minus_ratio['bad_tail_composite_cofactor_count']}/{minus_ratio['tail_slot_count']}`。",
            f"- plus 最大 `t`：`P={max_plus_t['p']}`，`max_t={max_plus_t['max_t']}`。",
            f"- minus 最大 `t`：`P={max_minus_t['p']}`，`max_t={max_minus_t['max_t']}`。",
            "",
            "## 4. 样本表",
            "",
            "| P | sign | tail primes | slots | good m prime | bad m composite | bad ratio | t range | bad t range |",
            "| ---: | --- | ---: | ---: | ---: | ---: | ---: | --- | --- |",
        ]
    )
    for row in result["sample_records"]:
        lines.append(
            f"| {row['p']} | `{row['sign']}` | {row['distinct_tail_prime_count']} | "
            f"{row['tail_slot_count']} | {row['good_tail_prime_cofactor_count']} | "
            f"{row['bad_tail_composite_cofactor_count']} | {row['bad_tail_ratio']:.4f} | "
            f"{row['min_t']}..{row['max_t']} | {row['bad_min_t']}..{row['bad_max_t']} |"
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
            "- 具体要证明：沿尾素参数 `q=P-a` 与一到两个槽 `t`，移位余因子 `P+a+t` 的合数命中不能持续多到压过平方锚素数数；若过密，则按 `t` 层和最小因子层抽取相位缺陷。",
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
                "identity_failure_count": result["identity_failure_count"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
