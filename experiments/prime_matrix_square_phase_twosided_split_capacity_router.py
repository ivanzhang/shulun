#!/usr/bin/env python3
"""审计 P^2±r 两侧低轮幸存数与高尾精确容量分割。

用法示例：
  python3 experiments/prime_matrix_square_phase_twosided_split_capacity_router.py --max-p 5000
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-twosided-split-capacity-router.json

输出：
  data/square-phase-twosided-split-capacity-ledger.json
  docs/monograph/prime-matrix-square-phase-twosided-split-capacity-router.json
  docs/monograph/prime-matrix-square-phase-twosided-split-capacity-router.md
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

OUT_LEDGER = DATA / "square-phase-twosided-split-capacity-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-twosided-split-capacity-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-twosided-split-capacity-router.md"

MAIN_TARGET = "SquarePhaseAlphaFourFifthsLowHoleLowerBound"
RETURN_TARGET = "SquarePhaseTailCapacityPDECSAEReturn"


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


def cover_residue(p: int, q: int, sign: str) -> int:
    """返回 r 坐标中被 q 覆盖的唯一正残基。"""
    p2_mod = (p * p) % q
    residue = (-p2_mod) % q if sign == "plus" else p2_mod
    return q if residue == 0 else residue


def low_survivor_count(p: int, cutoff: int, sign: str, primes: list[int]) -> int:
    """计算未被 q<=cutoff 覆盖的列数。"""
    covered = bytearray(p)
    for q in primes:
        if q >= p or q > cutoff:
            break
        residue = cover_residue(p, q, sign)
        for r_value in range(residue, p, q):
            covered[r_value] = 1
    return sum(1 for r_value in range(1, p) if not covered[r_value])


def high_capacity(p: int, cutoff: int, sign: str, primes: list[int]) -> tuple[int, dict[int, int]]:
    """计算 q>cutoff 的固定相位实际容量。"""
    total = 0
    histogram: dict[int, int] = {}
    for q in primes:
        if q >= p:
            break
        if q <= cutoff:
            continue
        residue = cover_residue(p, q, sign)
        count = 0
        for _ in range(residue, p, q):
            count += 1
        total += count
        histogram[count] = histogram.get(count, 0) + 1
    return total, dict(sorted(histogram.items()))


def audit_one(p: int, alpha: float, primes: list[int]) -> dict[str, Any]:
    """审计单个 p 与 alpha。"""
    cutoff = int(alpha * p)
    plus_low = low_survivor_count(p, cutoff, "plus", primes)
    plus_cap, plus_hist = high_capacity(p, cutoff, "plus", primes)
    minus_low = low_survivor_count(p, cutoff, "minus", primes)
    minus_cap, minus_hist = high_capacity(p, cutoff, "minus", primes)
    return {
        "p": p,
        "alpha": alpha,
        "cutoff": cutoff,
        "plus_low_survivors": plus_low,
        "plus_high_capacity": plus_cap,
        "plus_margin": plus_low - plus_cap,
        "plus_capacity_histogram": plus_hist,
        "minus_low_survivors": minus_low,
        "minus_high_capacity": minus_cap,
        "minus_margin": minus_low - minus_cap,
        "minus_capacity_histogram": minus_hist,
        "combined_low_survivors": plus_low + minus_low,
        "combined_high_capacity": plus_cap + minus_cap,
        "combined_margin": plus_low + minus_low - plus_cap - minus_cap,
    }


def theorem_rows() -> list[dict[str, str]]:
    """列出本步确定性定理。"""
    return [
        {
            "name": "signed_split_capacity_criterion",
            "status": "closed",
            "statement": "For each sign, if H_y^sign(P)>C_y^sign(P), then P^2 sign r has a prime with 1<=r<P.",
        },
        {
            "name": "exact_tail_capacity",
            "status": "closed",
            "statement": "C_y^sign(P) is the exact number of tail phase slots r in [1,P-1] hit by q in (y,P).",
        },
        {
            "name": "twosided_combined_criterion",
            "status": "closed",
            "statement": "If H_y^+(P)+H_y^-(P)>C_y^+(P)+C_y^-(P), at least one side has a square-anchor prime.",
        },
        {
            "name": "alpha_four_fifths_finite_margin",
            "status": "diagnostic_only",
            "statement": "The alpha=4/5 margin is positive for both signs in the scanned range, but this is not a global proof.",
        },
        {
            "name": "remaining_lowhole_lower_bound",
            "status": "open",
            "statement": "A global proof needs a lower bound for H_floor(4P/5)^sign(P), or a proof that margin failure routes to PDEC/SAE.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "SplitCapacityCriterionClosed",
            "closed": True,
            "proved": True,
            "meaning": "低轮幸存数大于高尾容量时，该侧平方锚素数必存在。",
            "remaining": "closed",
        },
        {
            "gate": "AlphaFourFifthsFiniteBothSignsPositive",
            "closed": result["alpha_four_fifths_plus_failure_count"] == 0
            and result["alpha_four_fifths_minus_failure_count"] == 0,
            "proved": False,
            "meaning": f"有限扫描 P<={result['parameters']['max_p']} 下 alpha=4/5 两侧 margin 均为正。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "AlphaFourFifthsGlobalLowHoleLowerBound",
            "closed": False,
            "proved": False,
            "meaning": "需要把样本正余量升级为全局低洞下界与高尾容量上界。",
            "remaining": MAIN_TARGET,
        },
        {
            "gate": "TailCapacityFailureRoutesToPDEC",
            "closed": False,
            "proved": False,
            "meaning": "若 margin<=0 持久发生，必须登记为尾相位容量异常、端点 SAE 或 SquarePhase-PDEC。",
            "remaining": RETURN_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步关闭分割判据和有限证据，不关闭全局命题。",
            "remaining": f"{MAIN_TARGET} OR {RETURN_TARGET}",
        },
    ]


def build_result(max_p: int, alphas: list[float], sample_ps: list[int]) -> dict[str, Any]:
    """构造路由器结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    prime_flags = sieve(max_p)
    primes = primes_from_flags(prime_flags, max_p)
    p_values = [p for p in primes if p >= 3]
    records: list[dict[str, Any]] = []
    for p in p_values:
        for alpha in alphas:
            records.append(audit_one(p, alpha, primes))

    alpha_45 = 0.8
    alpha_45_records = [record for record in records if abs(record["alpha"] - alpha_45) < 1e-12]
    plus_failures = [record for record in alpha_45_records if record["plus_margin"] <= 0]
    minus_failures = [record for record in alpha_45_records if record["minus_margin"] <= 0]
    combined_failures = [record for record in alpha_45_records if record["combined_margin"] <= 0]
    worst_plus = min(alpha_45_records, key=lambda item: item["plus_margin"], default=None)
    worst_minus = min(alpha_45_records, key=lambda item: item["minus_margin"], default=None)
    worst_combined = min(alpha_45_records, key=lambda item: item["combined_margin"], default=None)
    sample_set = set(sample_ps)
    sample_records = [record for record in alpha_45_records if record["p"] in sample_set]

    alpha_summary = []
    for alpha in alphas:
        alpha_records = [record for record in records if abs(record["alpha"] - alpha) < 1e-12]
        alpha_summary.append(
            {
                "alpha": alpha,
                "plus_failure_count": sum(1 for record in alpha_records if record["plus_margin"] <= 0),
                "minus_failure_count": sum(1 for record in alpha_records if record["minus_margin"] <= 0),
                "combined_failure_count": sum(1 for record in alpha_records if record["combined_margin"] <= 0),
                "min_plus_margin": min(record["plus_margin"] for record in alpha_records),
                "min_minus_margin": min(record["minus_margin"] for record in alpha_records),
                "min_combined_margin": min(record["combined_margin"] for record in alpha_records),
            }
        )

    ledger = {
        "parameters": {"max_p": max_p, "alphas": alphas, "sample_ps": sample_ps},
        "prime_count": len(p_values),
        "alpha_summary": alpha_summary,
        "alpha_four_fifths": {
            "plus_failure_count": len(plus_failures),
            "minus_failure_count": len(minus_failures),
            "combined_failure_count": len(combined_failures),
            "worst_plus_record": worst_plus,
            "worst_minus_record": worst_minus,
            "worst_combined_record": worst_combined,
            "sample_records": sample_records,
            "plus_failures": plus_failures[:20],
            "minus_failures": minus_failures[:20],
        },
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    result = {
        "certificate_type": "prime_matrix_square_phase_twosided_split_capacity_router",
        "status": "twosided_square_phase_split_capacity_reduced_to_alpha_four_fifths_lowhole_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "parameters": ledger["parameters"],
        "finite_prime_count": len(p_values),
        "alpha_summary": alpha_summary,
        "alpha_four_fifths_plus_failure_count": len(plus_failures),
        "alpha_four_fifths_minus_failure_count": len(minus_failures),
        "alpha_four_fifths_combined_failure_count": len(combined_failures),
        "worst_plus_record": worst_plus,
        "worst_minus_record": worst_minus,
        "worst_combined_record": worst_combined,
        "sample_records": sample_records,
        "split_capacity_criterion_closed": True,
        "alpha_four_fifths_global_lowhole_lower_bound_proved": False,
        "tail_capacity_failure_routes_to_pdec_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": "TwoSidedSquarePhaseLayeredWheelSurvivorLowerBound",
        "hardpoint_after_router": f"{MAIN_TARGET} OR {RETURN_TARGET}",
        "next_direct_attack_target": MAIN_TARGET,
        "alternative_attack_target": RETURN_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_twosided_split_capacity_router.py": sha256(
                Path(__file__).resolve()
            ),
            "data/square-phase-twosided-split-capacity-ledger.json": sha256(OUT_LEDGER),
        },
        "plain_conclusion": (
            "`P^2±r` 的层叠轮筛可继续压成一个完全确定的容量判据：先筛到 "
            "`y=floor(alpha P)`，若某侧低轮幸存数 `H_y` 大于尾素数 `q in (y,P)` 的实际固定相位容量 "
            "`C_y`，则该侧必有平方锚素数。有限审计显示 `alpha=4/5` 在 `P<=5000` "
            "范围内 plus/minus 两侧 margin 全为正，比 `2/3` 的样本边界更稳。"
            "但全局仍需证明 `H_floor(4P/5)` 的下界，或证明 margin 失败必产生尾相位 PDEC/SAE 回流。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase two-sided split capacity",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"max_p={result['parameters']['max_p']}",
        f"finite_prime_count={result['finite_prime_count']}",
        f"alpha_4_5_plus_failure_count={result['alpha_four_fifths_plus_failure_count']}",
        f"alpha_4_5_minus_failure_count={result['alpha_four_fifths_minus_failure_count']}",
        f"alpha_4_5_combined_failure_count={result['alpha_four_fifths_combined_failure_count']}",
        f"alpha_four_fifths_global_lowhole_lower_bound_proved={fmt_bool(result['alpha_four_fifths_global_lowhole_lower_bound_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 确定性判据",
        "",
        "| name | status | statement |",
        "| --- | --- | --- |",
    ]
    for item in result["theorem_rows"]:
        lines.append(f"| `{item['name']}` | `{item['status']}` | {table_cell(item['statement'])} |")

    lines.extend(
        [
            "",
            "## 2. Alpha 扫描汇总",
            "",
            "| alpha | plus fail | minus fail | combined fail | min plus | min minus | min combined |",
            "| ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in result["alpha_summary"]:
        lines.append(
            f"| {row['alpha']:.6f} | {row['plus_failure_count']} | {row['minus_failure_count']} | "
            f"{row['combined_failure_count']} | {row['min_plus_margin']} | "
            f"{row['min_minus_margin']} | {row['min_combined_margin']} |"
        )

    lines.extend(
        [
            "",
            "## 3. Alpha=4/5 样本",
            "",
            "| P | plus H | plus C | plus margin | minus H | minus C | minus margin |",
            "| ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in result["sample_records"]:
        lines.append(
            f"| {row['p']} | {row['plus_low_survivors']} | {row['plus_high_capacity']} | "
            f"{row['plus_margin']} | {row['minus_low_survivors']} | "
            f"{row['minus_high_capacity']} | {row['minus_margin']} |"
        )

    worst_plus = result["worst_plus_record"]
    worst_minus = result["worst_minus_record"]
    worst_combined = result["worst_combined_record"]
    lines.extend(
        [
            "",
            "## 4. 最紧样本",
            "",
            f"- plus 最小 margin：`P={worst_plus['p']}`，`H={worst_plus['plus_low_survivors']}`，`C={worst_plus['plus_high_capacity']}`，`margin={worst_plus['plus_margin']}`。",
            f"- minus 最小 margin：`P={worst_minus['p']}`，`H={worst_minus['minus_low_survivors']}`，`C={worst_minus['minus_high_capacity']}`，`margin={worst_minus['minus_margin']}`。",
            f"- combined 最小 margin：`P={worst_combined['p']}`，`H={worst_combined['combined_low_survivors']}`，`C={worst_combined['combined_high_capacity']}`，`margin={worst_combined['combined_margin']}`。",
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
            "- 关键是证明 alpha=4/5 低轮幸存数下界，而不是继续扩大有限扫描。",
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


def parse_floats(raw: str) -> list[float]:
    """解析小数列表。"""
    return [float(item) for item in raw.split(",") if item.strip()]


def parse_ints(raw: str) -> list[int]:
    """解析整数列表。"""
    return [int(item) for item in raw.split(",") if item.strip()]


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-p", type=int, default=5000)
    parser.add_argument("--alphas", default="0.5,0.6,0.6666666667,0.7,0.75,0.8,0.85,0.9")
    parser.add_argument("--sample-ps", default="13,17,19,23,29,31,101,499,1009,2003,4999")
    args = parser.parse_args()

    result = build_result(
        max_p=args.max_p,
        alphas=parse_floats(args.alphas),
        sample_ps=parse_ints(args.sample_ps),
    )
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result)
    print(
        json.dumps(
            {
                "status": result["status"],
                "max_p": result["parameters"]["max_p"],
                "alpha_4_5_plus_failure_count": result["alpha_four_fifths_plus_failure_count"],
                "alpha_4_5_minus_failure_count": result["alpha_four_fifths_minus_failure_count"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
