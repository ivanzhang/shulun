#!/usr/bin/env python3
"""审计 P^2±r 在 alpha=4/5 下的低洞壳层精确分解。

用法示例：
  python3 experiments/prime_matrix_square_phase_alpha45_lowhole_shell_router.py --max-p 5000
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-alpha45-lowhole-shell-router.json

输出：
  data/square-phase-alpha45-lowhole-shell-ledger.json
  docs/monograph/prime-matrix-square-phase-alpha45-lowhole-shell-router.json
  docs/monograph/prime-matrix-square-phase-alpha45-lowhole-shell-router.md
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

OUT_LEDGER = DATA / "square-phase-alpha45-lowhole-shell-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-alpha45-lowhole-shell-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-alpha45-lowhole-shell-router.md"

ALPHA_NUMERATOR = 4
ALPHA_DENOMINATOR = 5
MAIN_TARGET = "SquarePhaseAlphaFourFifthsPrimeDominatesBadTailCompositeCofactor"
RETURN_TARGET = "SquarePhaseBadTailCompositeCofactorPDECSAEReturn"


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
    return (ALPHA_NUMERATOR * p) // ALPHA_DENOMINATOR


def square_value(p: int, r_value: int, sign: str) -> int:
    """返回 P^2+r 或 P^2-r。"""
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


def low_survivor_columns(p: int, cutoff: int, sign: str, primes: list[int]) -> list[int]:
    """返回未被 q<=cutoff 覆盖的列。"""
    covered = bytearray(p)
    for q in primes:
        if q >= p or q > cutoff:
            break
        residue = cover_residue(p, q, sign)
        for r_value in range(residue, p, q):
            covered[r_value] = 1
    return [r_value for r_value in range(1, p) if not covered[r_value]]


def classify_low_column(p: int, r_value: int, sign: str, cutoff: int, primes: list[int]) -> dict[str, Any]:
    """分类一个低洞列。"""
    value = square_value(p, r_value, sign)
    lpf = least_prime_factor(value, primes)
    if lpf == value:
        return {"kind": "prime", "r": r_value, "value": value}

    cofactor = value // lpf
    cofactor_prime = is_prime_by_primes(cofactor, primes)
    a_value = p - lpf
    b_value = cofactor - p
    d_value = b_value - a_value
    if sign == "plus":
        phase_value = p * d_value - a_value * (a_value + d_value)
    else:
        phase_value = a_value * (a_value + d_value) - p * d_value
    return {
        "kind": "semiprime_shell",
        "r": r_value,
        "value": value,
        "q": lpf,
        "cofactor": cofactor,
        "cofactor_prime": cofactor_prime,
        "a": a_value,
        "b": b_value,
        "d": d_value,
        "phase_value": phase_value,
        "valid_shell": (
            cutoff < lpf < p
            and cofactor > p
            and cofactor_prime
            and phase_value == r_value
            and 1 <= r_value < p
        ),
    }


def high_hit_records(p: int, cutoff: int, sign: str, primes: list[int]) -> list[dict[str, Any]]:
    """返回高尾 q in (cutoff,P) 的实际命中。"""
    records: list[dict[str, Any]] = []
    low_set = set(low_survivor_columns(p, cutoff, sign, primes))
    for q in primes:
        if q >= p:
            break
        if q <= cutoff:
            continue
        residue = cover_residue(p, q, sign)
        for r_value in range(residue, p, q):
            value = square_value(p, r_value, sign)
            cofactor = value // q
            low_survivor = r_value in low_set
            records.append(
                {
                    "r": r_value,
                    "q": q,
                    "value": value,
                    "cofactor": cofactor,
                    "cofactor_prime": is_prime_by_primes(cofactor, primes),
                    "least_factor_of_cofactor": least_prime_factor(cofactor, primes),
                    "low_survivor": low_survivor,
                    "kind": "good_high_semiprime" if low_survivor else "bad_high_composite_cofactor",
                }
            )
    return records


def extrema(values: list[int]) -> dict[str, int | None]:
    """返回最小最大值。"""
    if not values:
        return {"min": None, "max": None}
    return {"min": min(values), "max": max(values)}


def audit_sign(p: int, sign: str, primes: list[int]) -> dict[str, Any]:
    """审计单个 P 的一个方向。"""
    cutoff = cutoff_alpha45(p)
    lows = low_survivor_columns(p, cutoff, sign, primes)
    low_records = [classify_low_column(p, r_value, sign, cutoff, primes) for r_value in lows]
    prime_records = [record for record in low_records if record["kind"] == "prime"]
    shell_records = [record for record in low_records if record["kind"] == "semiprime_shell"]
    invalid_shells = [record for record in shell_records if not record["valid_shell"]]

    high_records = high_hit_records(p, cutoff, sign, primes)
    slot_histogram: dict[int, int] = {}
    for record in high_records:
        slot_histogram[record["r"]] = slot_histogram.get(record["r"], 0) + 1
    duplicate_slots = {key: value for key, value in slot_histogram.items() if value > 1}
    good_high = [record for record in high_records if record["kind"] == "good_high_semiprime"]
    bad_high = [record for record in high_records if record["kind"] == "bad_high_composite_cofactor"]

    low_count = len(lows)
    high_count = len(high_records)
    prime_count = len(prime_records)
    shell_count = len(shell_records)
    bad_count = len(bad_high)
    margin = low_count - high_count
    prime_minus_bad = prime_count - bad_count

    return {
        "p": p,
        "sign": sign,
        "cutoff": cutoff,
        "low_survivors": low_count,
        "square_anchor_prime_count": prime_count,
        "semiprime_shell_count": shell_count,
        "high_capacity": high_count,
        "good_high_semiprime_count": len(good_high),
        "bad_high_composite_cofactor_count": bad_count,
        "margin_H_minus_C": margin,
        "prime_minus_bad": prime_minus_bad,
        "low_decomposition_delta": low_count - prime_count - shell_count,
        "high_decomposition_delta": high_count - len(good_high) - bad_count,
        "good_shell_delta": len(good_high) - shell_count,
        "net_identity_delta": margin - prime_minus_bad,
        "duplicate_high_slot_count": len(duplicate_slots),
        "invalid_shell_count": len(invalid_shells),
        "shell_a_range": extrema([record["a"] for record in shell_records]),
        "shell_b_range": extrema([record["b"] for record in shell_records]),
        "shell_d_range": extrema([record["d"] for record in shell_records]),
        "prime_r_sample": [record["r"] for record in prime_records[:12]],
        "semiprime_shell_sample": shell_records[:8],
        "bad_high_sample": bad_high[:8],
    }


def theorem_rows() -> list[dict[str, str]]:
    """列出本步确定性定理。"""
    return [
        {
            "name": "alpha45_lowhole_prime_semiprime_dichotomy",
            "status": "closed",
            "statement": "For alpha=4/5, every low survivor of P^2±r is either a square-anchor prime or a near-square semiprime (P-a)(P+b) with P-a in (4P/5,P).",
        },
        {
            "name": "tail_capacity_good_bad_split",
            "status": "closed",
            "statement": "The high-tail capacity C splits exactly as good semiprime-shell hits plus bad composite-cofactor hits.",
        },
        {
            "name": "net_margin_identity",
            "status": "closed",
            "statement": "For each sign, H_{4P/5}^sign-C_{4P/5}^sign equals square-anchor-prime-count minus bad-tail-composite-cofactor-count.",
        },
        {
            "name": "alpha45_finite_prime_dominance",
            "status": "diagnostic_only",
            "statement": "In the scanned range, the prime count beats the bad-tail composite-cofactor count on both signs; this is finite evidence only.",
        },
        {
            "name": "remaining_prime_vs_badtail_input",
            "status": "open",
            "statement": "A global proof still needs square-anchor primes to dominate bad-tail composite cofactors, or a proof that failure routes to PDEC/SAE.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "Alpha45LowholeShellIdentityClosed",
            "closed": result["identity_failure_count"] == 0,
            "proved": True,
            "meaning": "低洞、尾容量和净余量三条恒等式均已逐项登记。",
            "remaining": "closed",
        },
        {
            "gate": "FinitePrimeBeatsBadTailBothSigns",
            "closed": result["finite_prime_dominance_failure_count"] == 0,
            "proved": False,
            "meaning": f"有限扫描 P<={result['parameters']['max_p']} 下两侧 prime-bad 余量均为正。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "GlobalPrimeDominatesBadTailInput",
            "closed": False,
            "proved": False,
            "meaning": "需要把平方锚素数数压过坏尾复合余因子命中的样本事实升级为全局证明。",
            "remaining": MAIN_TARGET,
        },
        {
            "gate": "BadTailFailureRoutesToPDEC",
            "closed": False,
            "proved": False,
            "meaning": "若 bad-tail 持久压过 prime count，必须抽取复合余因子的相位异常或端点缺陷证书。",
            "remaining": RETURN_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只关闭精确壳层分解，不关闭全局行/列命题。",
            "remaining": f"{MAIN_TARGET} OR {RETURN_TARGET}",
        },
    ]


def build_result(max_p: int, sample_ps: list[int]) -> dict[str, Any]:
    """构造路由器结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    # 素性测试需要一个超过 sqrt(P^2+P) 的哨兵素数，保守筛到 2P。
    prime_flags = sieve(max_p * 2)
    primes = primes_from_flags(prime_flags, max_p * 2)
    p_values = [p for p in primes if 3 <= p <= max_p]
    records: list[dict[str, Any]] = []
    for p in p_values:
        records.append(audit_sign(p, "plus", primes))
        records.append(audit_sign(p, "minus", primes))

    identity_failures = [
        record
        for record in records
        if record["low_decomposition_delta"] != 0
        or record["high_decomposition_delta"] != 0
        or record["good_shell_delta"] != 0
        or record["net_identity_delta"] != 0
        or record["duplicate_high_slot_count"] != 0
        or record["invalid_shell_count"] != 0
    ]
    dominance_failures = [record for record in records if record["prime_minus_bad"] <= 0]
    plus_records = [record for record in records if record["sign"] == "plus"]
    minus_records = [record for record in records if record["sign"] == "minus"]
    worst_plus = min(plus_records, key=lambda item: item["prime_minus_bad"], default=None)
    worst_minus = min(minus_records, key=lambda item: item["prime_minus_bad"], default=None)
    worst_combined = min(
        (
            {
                "p": p,
                "combined_prime_minus_bad": sum(
                    item["prime_minus_bad"] for item in records if item["p"] == p
                ),
                "combined_prime_count": sum(
                    item["square_anchor_prime_count"] for item in records if item["p"] == p
                ),
                "combined_bad_tail_count": sum(
                    item["bad_high_composite_cofactor_count"] for item in records if item["p"] == p
                ),
            }
            for p in p_values
        ),
        key=lambda item: item["combined_prime_minus_bad"],
        default=None,
    )
    sample_set = set(sample_ps)
    sample_records = [record for record in records if record["p"] in sample_set]

    aggregate = {
        "plus_prime_total": sum(record["square_anchor_prime_count"] for record in plus_records),
        "plus_bad_tail_total": sum(record["bad_high_composite_cofactor_count"] for record in plus_records),
        "minus_prime_total": sum(record["square_anchor_prime_count"] for record in minus_records),
        "minus_bad_tail_total": sum(record["bad_high_composite_cofactor_count"] for record in minus_records),
        "plus_semiprime_shell_total": sum(record["semiprime_shell_count"] for record in plus_records),
        "minus_semiprime_shell_total": sum(record["semiprime_shell_count"] for record in minus_records),
    }

    ledger = {
        "parameters": {"max_p": max_p, "alpha": "4/5", "sample_ps": sample_ps},
        "prime_count": len(p_values),
        "aggregate": aggregate,
        "identity_failure_count": len(identity_failures),
        "finite_prime_dominance_failure_count": len(dominance_failures),
        "worst_plus_record": worst_plus,
        "worst_minus_record": worst_minus,
        "worst_combined_record": worst_combined,
        "sample_records": sample_records,
        "identity_failures": identity_failures[:20],
        "dominance_failures": dominance_failures[:20],
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    result = {
        "certificate_type": "prime_matrix_square_phase_alpha45_lowhole_shell_router",
        "status": "square_phase_alpha45_lowhole_shell_reduced_to_prime_vs_badtail_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "empirical_absence_not_used_as_proof": True,
        "parameters": ledger["parameters"],
        "finite_prime_count": len(p_values),
        "aggregate": aggregate,
        "identity_failure_count": len(identity_failures),
        "finite_prime_dominance_failure_count": len(dominance_failures),
        "worst_plus_record": worst_plus,
        "worst_minus_record": worst_minus,
        "worst_combined_record": worst_combined,
        "sample_records": sample_records,
        "alpha45_lowhole_shell_identity_closed": len(identity_failures) == 0,
        "global_prime_dominates_badtail_proved": False,
        "bad_tail_failure_routes_to_pdec_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": "SquarePhaseAlphaFourFifthsLowHoleLowerBound",
        "hardpoint_after_router": f"{MAIN_TARGET} OR {RETURN_TARGET}",
        "next_direct_attack_target": MAIN_TARGET,
        "alternative_attack_target": RETURN_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_alpha45_lowhole_shell_router.py": sha256(
                Path(__file__).resolve()
            ),
            "data/square-phase-alpha45-lowhole-shell-ledger.json": sha256(OUT_LEDGER),
        },
        "plain_conclusion": (
            "`alpha=4/5` 的平方锚低洞已经从粗下界问题压成精确净余量恒等式："
            "低洞 `H` 等于平方锚素数数加好半素数壳层数，尾容量 `C` 等于同一好半素数壳层数加坏尾复合余因子命中数，"
            "所以 `H-C = Prime - BadTail`。有限审计在样本范围内两侧余量均为正；"
            "但全局仍需证明 `Prime>BadTail`，或证明失败会产生已登记的 PDEC/SAE 相位缺陷。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    worst_plus = result["worst_plus_record"]
    worst_minus = result["worst_minus_record"]
    worst_combined = result["worst_combined_record"]
    lines = [
        "# Prime Matrix square-phase alpha=4/5 lowhole shell",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"max_p={result['parameters']['max_p']}",
        f"finite_prime_count={result['finite_prime_count']}",
        f"identity_failure_count={result['identity_failure_count']}",
        f"finite_prime_dominance_failure_count={result['finite_prime_dominance_failure_count']}",
        f"global_prime_dominates_badtail_proved={fmt_bool(result['global_prime_dominates_badtail_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 精确恒等式",
        "",
        "设 `y=floor(4P/5)`，`H_y^±(P)` 为 `P^2±r` 中未被 `q<=y` 覆盖的列数，"
        "`C_y^±(P)` 为尾素 `y<q<P` 的固定相位容量。",
        "",
        "若低洞列对应的 `P^2±r` 合成，则其最小素因子必在 `(y,P)`，余因子必为素数且位于 `P` 之后的短壳层。"
        "因此低洞只有两类：平方锚素数，或近方半素数壳层。",
        "",
        "同一个近方半素数壳层又恰好贡献尾容量中的 good high 命中，所以逐侧有",
        "",
        "```text",
        "H_y^± = Prime^± + GoodShell^±",
        "C_y^± = GoodShell^± + BadTail^±",
        "H_y^± - C_y^± = Prime^± - BadTail^±",
        "```",
        "",
        "这一步把 `SquarePhaseAlphaFourFifthsLowHoleLowerBound` 压窄为 `Prime>BadTail` 的净余量问题。",
        "",
        "## 2. 壳层相位公式",
        "",
        "写尾素因子和余因子为",
        "",
        "```text",
        "q=P-a,     m=P+b=P+a+d",
        "```",
        "",
        "plus 侧 `P^2+r=(P-a)(P+a+d)`，故",
        "",
        "```text",
        "r = P*d - a*(a+d),    1<=r<P.",
        "```",
        "",
        "minus 侧 `P^2-r=(P-a)(P+a+d)`，故",
        "",
        "```text",
        "r = a*(a+d) - P*d,    1<=r<P.",
        "```",
        "",
        "这正是平方锚 `P^2±r` 的薄双曲壳层；两侧分别位于同一相位曲面的上下侧。",
        "",
        "## 3. 确定性判据",
        "",
        "| name | status | statement |",
        "| --- | --- | --- |",
    ]
    for item in result["theorem_rows"]:
        lines.append(f"| `{item['name']}` | `{item['status']}` | {table_cell(item['statement'])} |")

    lines.extend(
        [
            "",
            "## 4. 有限审计摘要",
            "",
            "| metric | plus | minus |",
            "| --- | ---: | ---: |",
            f"| prime total | {result['aggregate']['plus_prime_total']} | {result['aggregate']['minus_prime_total']} |",
            f"| bad tail total | {result['aggregate']['plus_bad_tail_total']} | {result['aggregate']['minus_bad_tail_total']} |",
            f"| semiprime shell total | {result['aggregate']['plus_semiprime_shell_total']} | {result['aggregate']['minus_semiprime_shell_total']} |",
            "",
            "最紧样本：",
            "",
            f"- plus 最小 `Prime-BadTail`：`P={worst_plus['p']}`，`Prime={worst_plus['square_anchor_prime_count']}`，`BadTail={worst_plus['bad_high_composite_cofactor_count']}`，`margin={worst_plus['prime_minus_bad']}`。",
            f"- minus 最小 `Prime-BadTail`：`P={worst_minus['p']}`，`Prime={worst_minus['square_anchor_prime_count']}`，`BadTail={worst_minus['bad_high_composite_cofactor_count']}`，`margin={worst_minus['prime_minus_bad']}`。",
            f"- combined 最小 `Prime-BadTail`：`P={worst_combined['p']}`，`Prime={worst_combined['combined_prime_count']}`，`BadTail={worst_combined['combined_bad_tail_count']}`，`margin={worst_combined['combined_prime_minus_bad']}`。",
            "",
            "## 5. 样本表",
            "",
            "| P | sign | H | C | Prime | GoodShell | BadTail | Prime-BadTail | shell d-range |",
            "| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for row in result["sample_records"]:
        d_range = row["shell_d_range"]
        lines.append(
            f"| {row['p']} | `{row['sign']}` | {row['low_survivors']} | {row['high_capacity']} | "
            f"{row['square_anchor_prime_count']} | {row['semiprime_shell_count']} | "
            f"{row['bad_high_composite_cofactor_count']} | {row['prime_minus_bad']} | "
            f"{d_range['min']}..{d_range['max']} |"
        )

    lines.extend(
        [
            "",
            "## 6. 判定表",
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
            "## 7. 下一步",
            "",
            f"- 主攻：`{result['next_direct_attack_target']}`。",
            f"- 备选回流：`{result['alternative_attack_target']}`。",
            "- 当前真正净硬点不再是好半素数壳层；它已在 `H-C` 中抵消。必须证明平方锚素数数压过坏尾复合余因子命中，或把坏尾持续优势抽成 PDEC/SAE。",
            "",
            "## 8. 依赖哈希",
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
                "finite_prime_dominance_failure_count": result["finite_prime_dominance_failure_count"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
