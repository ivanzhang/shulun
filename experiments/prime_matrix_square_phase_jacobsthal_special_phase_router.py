#!/usr/bin/env python3
"""审计平方锚特殊相位是否落入 primorial 长覆盖块。

用法示例：
  python3 experiments/prime_matrix_square_phase_jacobsthal_special_phase_router.py --max-k 8
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-jacobsthal-special-phase-router.json

输出：
  data/square-phase-jacobsthal-special-phase-ledger.json
  docs/monograph/prime-matrix-square-phase-jacobsthal-special-phase-router.json
  docs/monograph/prime-matrix-square-phase-jacobsthal-special-phase-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from math import gcd, prod
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "square-phase-jacobsthal-special-phase-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-jacobsthal-special-phase-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-jacobsthal-special-phase-router.md"

MAIN_TARGET = "SpecialSquarePhaseAvoidsLongPrimorialJacobsthalBlocksOrPhasePDEC"
NEXT_TARGET = "SquarePhaseSpecialPhaseLongBlockPDECExclusion"


def is_prime(value: int) -> bool:
    """朴素素性测试。"""
    if value < 2:
        return False
    if value == 2:
        return True
    if value % 2 == 0:
        return False
    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def first_primes(count: int) -> list[int]:
    """返回前 count 个素数。"""
    primes: list[int] = []
    value = 2
    while len(primes) < count:
        if is_prime(value):
            primes.append(value)
        value += 1
    return primes


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def coprime_vector(primes: list[int]) -> tuple[int, bytearray]:
    """构造模 primorial 的互素残基指示。"""
    modulus = prod(primes)
    coprime = bytearray(b"\x01") * modulus
    for prime in primes:
        coprime[0:modulus:prime] = b"\x00" * (((modulus - 1) // prime) + 1)
    return modulus, coprime


def run_from(coprime: bytearray, start: int, limit: int) -> int:
    """返回从 start 起连续非互素长度，最多数到 limit。"""
    modulus = len(coprime)
    total = 0
    for offset in range(limit):
        if coprime[(start + offset) % modulus]:
            break
        total += 1
    return total


def first_survivor_offset(coprime: bytearray, start: int, length: int) -> int | None:
    """返回窗口内第一个互素幸存点的 0 起偏移。"""
    modulus = len(coprime)
    for offset in range(length):
        if coprime[(start + offset) % modulus]:
            return offset
    return None


def scan_blocks(coprime: bytearray, threshold: int, sample_limit: int = 8) -> dict[str, Any]:
    """扫描全周期覆盖块，统计长度达到 threshold 的长块。"""
    modulus = len(coprime)
    first_coprime: int | None = None
    last_coprime: int | None = None
    max_run = -1
    max_start = 0
    long_count = 0
    long_samples: list[dict[str, int]] = []

    def ingest(start: int, run: int) -> None:
        nonlocal max_run, max_start, long_count
        if run > max_run:
            max_run = run
            max_start = start % modulus
        if run >= threshold:
            long_count += 1
            if len(long_samples) < sample_limit:
                display = modulus if start % modulus == 0 else start % modulus
                long_samples.append({"start": display, "end": display + run - 1, "length": run})

    for residue, is_coprime in enumerate(coprime):
        if not is_coprime:
            continue
        if first_coprime is None:
            first_coprime = residue
        if last_coprime is not None:
            ingest(last_coprime + 1, residue - last_coprime - 1)
        last_coprime = residue

    if first_coprime is None or last_coprime is None:
        raise RuntimeError("primorial should have coprime residues")
    ingest((last_coprime + 1) % modulus, first_coprime + modulus - last_coprime - 1)
    display_start = modulus if max_start == 0 else max_start
    return {
        "max_covered_run": max_run,
        "first_max_start": display_start,
        "first_max_end": display_start + max_run - 1,
        "long_block_count_at_threshold": long_count,
        "long_block_samples": long_samples,
    }


def audit_k(k_value: int, primes_all: list[int]) -> dict[str, Any]:
    """审计 P=p_{k+1} 的平方锚特殊相位。"""
    low_primes = primes_all[:k_value]
    low_max = low_primes[-1]
    square_prime = primes_all[k_value]
    threshold = square_prime - 1
    modulus, coprime = coprime_vector(low_primes)
    block_summary = scan_blocks(coprime, threshold)

    plus_start = (square_prime * square_prime + 1) % modulus
    minus_start_value = square_prime * square_prime - (square_prime - 1)
    minus_start = minus_start_value % modulus
    plus_run = run_from(coprime, plus_start, threshold)
    minus_run = run_from(coprime, minus_start, threshold)
    plus_survivor_offset = first_survivor_offset(coprime, plus_start, threshold)
    minus_survivor_offset = first_survivor_offset(coprime, minus_start, threshold)
    plus_full_cover = plus_run >= threshold
    minus_full_cover = minus_run >= threshold

    return {
        "k": k_value,
        "low_prime_max": low_max,
        "square_anchor_prime_P": square_prime,
        "primorial_below_P": modulus,
        "window_length_P_minus_1": threshold,
        "period_max_covered_run": block_summary["max_covered_run"],
        "long_block_count_at_threshold": block_summary["long_block_count_at_threshold"],
        "first_period_max_block": [block_summary["first_max_start"], block_summary["first_max_end"]],
        "long_block_samples": block_summary["long_block_samples"],
        "plus_phase_start": plus_start,
        "minus_phase_start": minus_start,
        "plus_run_from_square_phase": plus_run,
        "minus_run_from_square_phase": minus_run,
        "plus_first_survivor_r": None if plus_survivor_offset is None else plus_survivor_offset + 1,
        "minus_first_survivor_r": None if minus_survivor_offset is None else threshold - minus_survivor_offset,
        "plus_full_cover": plus_full_cover,
        "minus_full_cover": minus_full_cover,
        "special_phase_avoids_threshold_long_block": not plus_full_cover and not minus_full_cover,
        "period_global_bound_fails": block_summary["max_covered_run"] >= threshold,
    }


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "square_phase_full_cover_implies_long_block",
            "status": "closed",
            "statement": "If P^2±(1..P-1) is fully covered by q<P, then the corresponding P^2 phase has a covered run of length at least P-1 in the primorial period.",
        },
        {
            "name": "special_phase_audit",
            "status": "finite_evidence",
            "statement": "The finite audit checks the actual P^2 phase directly, not only the global Jacobsthal maximum.",
        },
        {
            "name": "long_blocks_exist_but_square_phase_avoids",
            "status": "finite_evidence",
            "statement": "In the scanned range, long covered blocks of length >=P-1 exist from P=13 onward, but the square phase does not start inside one deeply enough to cover the whole square window.",
        },
        {
            "name": "global_special_phase_avoidance",
            "status": "open",
            "statement": "A global proof still needs to exclude P^2-phase alignment with length P-1 covered blocks, or route such alignment to PDEC/SAE/ColumnCRT.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "FullCoverImpliesLongBlockClosed",
            "closed": True,
            "proved": True,
            "meaning": "平方锚全覆盖已转成特殊相位的长 Jacobsthal 块命中。",
            "remaining": "closed",
        },
        {
            "gate": "FiniteSpecialPhaseAvoidance",
            "closed": result["plus_full_cover_count"] == 0 and result["minus_full_cover_count"] == 0,
            "proved": False,
            "meaning": f"有限扫描 P<={result['max_square_anchor_prime']} 中平方相位未被完整覆盖。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "GlobalPeriodBoundSuffices",
            "closed": False,
            "proved": False,
            "meaning": "全周期 Jacobsthal 短块上界已经失败，不能作为闭合路线。",
            "remaining": "rejected route",
        },
        {
            "gate": "GlobalSpecialPhaseAvoidanceProved",
            "closed": False,
            "proved": False,
            "meaning": "仍需证明 `P^2` 特殊相位不能对齐长块，或抽取相位缺陷证书。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只把 Jacobsthal 风险定位到平方特殊相位，不关闭全局行/列命题。",
            "remaining": NEXT_TARGET,
        },
    ]


def build_result(max_k: int) -> dict[str, Any]:
    """构造路由器结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    primes_all = first_primes(max_k + 1)
    records = [audit_k(k_value, primes_all) for k_value in range(1, max_k + 1)]
    plus_full = [record for record in records if record["plus_full_cover"]]
    minus_full = [record for record in records if record["minus_full_cover"]]
    period_bound_failures = [record for record in records if record["period_global_bound_fails"]]
    long_block_but_avoids = [
        record
        for record in records
        if record["period_global_bound_fails"] and record["special_phase_avoids_threshold_long_block"]
    ]
    worst_plus_run = max(records, key=lambda record: record["plus_run_from_square_phase"], default=None)
    worst_minus_run = max(records, key=lambda record: record["minus_run_from_square_phase"], default=None)
    aggregate = {
        "record_count": len(records),
        "plus_full_cover_count": len(plus_full),
        "minus_full_cover_count": len(minus_full),
        "period_bound_failure_count": len(period_bound_failures),
        "long_block_but_square_phase_avoids_count": len(long_block_but_avoids),
        "max_plus_run_from_square_phase": worst_plus_run["plus_run_from_square_phase"] if worst_plus_run else None,
        "max_minus_run_from_square_phase": worst_minus_run["minus_run_from_square_phase"] if worst_minus_run else None,
    }
    ledger = {
        "parameters": {"max_k": max_k},
        "aggregate": aggregate,
        "records": records,
        "plus_full_cover_records": plus_full,
        "minus_full_cover_records": minus_full,
        "period_bound_failure_records": period_bound_failures,
        "long_block_but_square_phase_avoids_records": long_block_but_avoids,
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    max_square_prime = max((record["square_anchor_prime_P"] for record in records), default=None)
    result = {
        "certificate_type": "prime_matrix_square_phase_jacobsthal_special_phase_router",
        "status": "square_phase_special_jacobsthal_phase_checked_global_phase_pdec_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "empirical_absence_not_used_as_proof": True,
        "parameters": ledger["parameters"],
        "aggregate": aggregate,
        "records": records,
        "plus_full_cover_count": len(plus_full),
        "minus_full_cover_count": len(minus_full),
        "period_bound_failure_count": len(period_bound_failures),
        "long_block_but_square_phase_avoids_count": len(long_block_but_avoids),
        "max_square_anchor_prime": max_square_prime,
        "worst_plus_run_record": worst_plus_run,
        "worst_minus_run_record": worst_minus_run,
        "square_phase_full_cover_implies_long_block_closed": True,
        "finite_special_phase_avoidance_checked": len(plus_full) == 0 and len(minus_full) == 0,
        "global_special_phase_avoidance_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_jacobsthal_special_phase_router.py": sha256(
                Path(__file__).resolve()
            ),
            "data/square-phase-jacobsthal-special-phase-ledger.json": sha256(OUT_LEDGER),
        },
        "plain_conclusion": (
            "本步把 primorial Jacobsthal 风险进一步压到平方锚特殊相位："
            "如果 `P^2±(1..P-1)` 被所有 `q<P` 全覆盖，则 `P^2` 在模 `prod_{q<P}q` 周期中"
            "必须从对应方向启动一个长度至少 `P-1` 的低筛覆盖块。"
            "有限扫描显示，从 `P=13` 起全周期确实已有长度 `>=P-1` 的长覆盖块，"
            "所以全周期短块上界路线失效；但实际 `P^2` 相位没有落入这些长块深处。"
            "因此最新硬点是特殊相位避让定理，或把相位对齐登记为 PDEC/SAE/ColumnCRT。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase Jacobsthal special phase router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"max_k={result['parameters']['max_k']}",
        f"max_square_anchor_prime={result['max_square_anchor_prime']}",
        f"plus_full_cover_count={result['plus_full_cover_count']}",
        f"minus_full_cover_count={result['minus_full_cover_count']}",
        f"period_bound_failure_count={result['period_bound_failure_count']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 特殊相位命题",
        "",
        "对 `P=p_{k+1}`，令 `M_<P=prod_{q<P}q`。plus 窗口是从 `P^2+1` 开始的长度 `P-1` 区间；minus 窗口按自然数顺序是从 `P^2-(P-1)` 到 `P^2-1` 的长度 `P-1` 区间。",
        "",
        "若其中任一窗口被 `q<P` 全覆盖，则该窗口在 `M_<P` 周期中就是一个长度至少 `P-1` 的 Jacobsthal 覆盖块。因此全覆盖反例必然是特殊相位长块命中，而不是普通中心块最大性问题。",
        "",
        "## 2. 有限审计摘要",
        "",
        "| metric | value |",
        "| --- | ---: |",
        f"| record count | {agg['record_count']} |",
        f"| plus full cover count | {agg['plus_full_cover_count']} |",
        f"| minus full cover count | {agg['minus_full_cover_count']} |",
        f"| period bound failure count | {agg['period_bound_failure_count']} |",
        f"| long block but square phase avoids count | {agg['long_block_but_square_phase_avoids_count']} |",
        f"| max plus run from square phase | {agg['max_plus_run_from_square_phase']} |",
        f"| max minus run from square phase | {agg['max_minus_run_from_square_phase']} |",
        "",
        "## 3. 精确扫描表",
        "",
        "| k | P | M_<P | P-1 | period max | long blocks | plus run | plus survivor r | minus run | minus survivor r |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for record in result["records"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(record["k"]),
                    str(record["square_anchor_prime_P"]),
                    str(record["primorial_below_P"]),
                    str(record["window_length_P_minus_1"]),
                    str(record["period_max_covered_run"]),
                    str(record["long_block_count_at_threshold"]),
                    str(record["plus_run_from_square_phase"]),
                    str(record["plus_first_survivor_r"]),
                    str(record["minus_run_from_square_phase"]),
                    str(record["minus_first_survivor_r"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 4. 命题行",
            "",
            "| name | status | statement |",
            "| --- | --- | --- |",
        ]
    )
    for row in result["theorem_rows"]:
        lines.append(f"| `{row['name']}` | `{row['status']}` | {table_cell(row['statement'])} |")

    lines.extend(
        [
            "",
            "## 5. 决策表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | ---: | ---: | --- | --- |",
        ]
    )
    for row in result["decision_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{row['gate']}`",
                    f"`{fmt_bool(row['closed'])}`",
                    f"`{fmt_bool(row['proved'])}`",
                    table_cell(row["meaning"]),
                    table_cell(row["remaining"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 6. 下一步",
            "",
            "- 主攻：`SquarePhaseSpecialPhaseLongBlockPDECExclusion`。",
            "- 需要证明 `P^2 mod M_<P` 不会进入任何长度 `P-1` 的低筛覆盖块深处。",
            "- 若不能直接证明，应把这种命中转成固定相位长块 PDEC、端点 SAE 或 ColumnCRT 证书，并与 `TotalPressureSupportPDECExclusion` 的激活尾支撑负载合并。",
            "- 当前仍未证明全局行/列无条件闭合。",
            "",
            "## 7. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in result["source_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-k", type=int, default=8)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    result = build_result(args.max_k)
    write_markdown(result)
    result["source_hashes"]["docs/monograph/prime-matrix-square-phase-jacobsthal-special-phase-router.md"] = sha256(
        OUT_MD
    )
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "max_k": args.max_k,
                "max_square_anchor_prime": result["max_square_anchor_prime"],
                "plus_full_cover_count": result["plus_full_cover_count"],
                "minus_full_cover_count": result["minus_full_cover_count"],
                "period_bound_failure_count": result["period_bound_failure_count"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
