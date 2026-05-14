#!/usr/bin/env python3
"""审计 square-phase reciprocal-floor 局部同余账本。

用法示例：
  python3 experiments/prime_matrix_square_phase_reciprocal_floor_congruence_ledger.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-reciprocal-floor-congruence-ledger.json

输出：
  docs/monograph/prime-matrix-square-phase-reciprocal-floor-congruence-ledger.json
  docs/monograph/prime-matrix-square-phase-reciprocal-floor-congruence-ledger.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-square-phase-reciprocal-floor-congruence-ledger.json"
OUT_MD = DOCS / "prime-matrix-square-phase-reciprocal-floor-congruence-ledger.md"

DEFAULT_P_LIST = [10007, 36739, 83561, 100003, 200003]
DEFAULT_Q_LIST = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]


def sieve_bool(limit: int) -> bytearray:
    """返回素数布尔表。"""
    flags = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        flags[0] = 0
    if limit >= 1:
        flags[1] = 0
    for value in range(2, int(limit**0.5) + 1):
        if not flags[value]:
            continue
        start = value * value
        flags[start : limit + 1 : value] = b"\x00" * (((limit - start) // value) + 1)
    return flags


def parse_int_list(text: str) -> list[int]:
    """解析逗号分隔整数列表。"""
    if not text:
        return []
    return [int(part) for part in text.split(",") if part.strip()]


def interval_bad_count(p: int, q: int, s: int, left: int, right: int) -> int:
    """用倒数短区间公式计数 q | floor(P^2/ell)+s。

    这里 ell 取闭区间 [left,right]。公式：
      floor(P^2/ell)=q*u-s
      等价于 P^2/(q*u-s+1) < ell <= P^2/(q*u-s)。
    """
    p2 = p * p
    n_min = p2 // right
    n_max = p2 // left
    u_min = math.ceil((n_min + s) / q) - 2
    u_max = math.floor((n_max + s) / q) + 2
    seen: set[int] = set()
    for u in range(max(0, u_min), u_max + 1):
        n = q * u - s
        if n <= 0:
            continue
        lo = p2 // (n + 1) + 1
        hi = p2 // n
        a = max(left, lo)
        b = min(right, hi)
        if a > b:
            continue
        for ell in range(a, b + 1):
            seen.add(ell)
    return len(seen)


def audit_one(p: int, q: int, s: int, prime_flags: bytearray) -> dict[str, Any]:
    """审计一个 (P,q,s)。"""
    y = max(2, int(math.floor(p / math.e)))
    left = y + 1
    right = p - 1
    p2 = p * p
    int_total = max(0, right - left + 1)
    prime_ells = [ell for ell in range(left, right + 1) if prime_flags[ell]]
    prime_total = len(prime_ells)

    direct_bad_int = 0
    bad_prime = 0
    residue_counts = [0] * q
    prime_residue_counts = [0] * q
    for ell in range(left, right + 1):
        residue = (p2 // ell + s) % q
        residue_counts[residue] += 1
        if residue == 0:
            direct_bad_int += 1
    for ell in prime_ells:
        residue = (p2 // ell + s) % q
        prime_residue_counts[residue] += 1
        if residue == 0:
            bad_prime += 1

    interval_count = interval_bad_count(p, q, s, left, right)
    expected_int = int_total / q
    expected_prime = prime_total / q if q else 0.0
    return {
        "p": p,
        "q": q,
        "s": s,
        "y": y,
        "int_total": int_total,
        "prime_total": prime_total,
        "bad_int": direct_bad_int,
        "bad_int_interval_formula": interval_count,
        "interval_formula_matches": interval_count == direct_bad_int,
        "bad_prime": bad_prime,
        "expected_int": expected_int,
        "expected_prime": expected_prime,
        "int_discrepancy": direct_bad_int - expected_int,
        "prime_discrepancy": bad_prime - expected_prime,
        "int_discrepancy_over_sqrt_p": (direct_bad_int - expected_int) / math.sqrt(p),
        "prime_discrepancy_over_sqrt_p": (bad_prime - expected_prime) / math.sqrt(p),
        "residue_counts": residue_counts,
        "prime_residue_counts": prime_residue_counts,
    }


def file_sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def audit(p_list: list[int], q_list: list[int]) -> dict[str, Any]:
    """执行账本审计。"""
    limit = max(p_list) if p_list else 2
    prime_flags = sieve_bool(limit)
    rows = [
        audit_one(p, q, s, prime_flags)
        for p in p_list
        for q in q_list
        for s in [1, 2, 3]
        if q < p
    ]
    formula_failures = [row for row in rows if not row["interval_formula_matches"]]
    max_int_disc = max(rows, key=lambda item: abs(item["int_discrepancy_over_sqrt_p"]))
    max_prime_disc = max(rows, key=lambda item: abs(item["prime_discrepancy_over_sqrt_p"]))
    max_prime_positive = max(rows, key=lambda item: item["prime_discrepancy_over_sqrt_p"])
    max_prime_negative = min(rows, key=lambda item: item["prime_discrepancy_over_sqrt_p"])
    return {
        "certificate_type": "prime_matrix_square_phase_reciprocal_floor_congruence_ledger",
        "status": "reciprocal_floor_congruence_interval_identity_checked_distribution_ledger_open",
        "p_list": p_list,
        "q_list": q_list,
        "offsets": [1, 2, 3],
        "row_count": len(rows),
        "interval_formula_failure_count": len(formula_failures),
        "interval_formula_checked": len(formula_failures) == 0,
        "selberg_distribution_proved": False,
        "reciprocal_floor_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "max_int_discrepancy_over_sqrt_p": max_int_disc,
        "max_prime_discrepancy_over_sqrt_p": max_prime_disc,
        "max_prime_positive_discrepancy_over_sqrt_p": max_prime_positive,
        "max_prime_negative_discrepancy_over_sqrt_p": max_prime_negative,
        "formula_failures": formula_failures[:10],
        "sample_rows": rows,
        "source_hashes": {
            "experiments/prime_matrix_square_phase_reciprocal_floor_congruence_ledger.py": file_sha256(
                Path(__file__).resolve()
            ),
            "docs/monograph/prime-matrix-square-phase-rfp-excess-dimension-collapse-router.json": file_sha256(
                DOCS / "prime-matrix-square-phase-rfp-excess-dimension-collapse-router.json"
            ),
        },
        "plain_conclusion": (
            "本账本验证了 `q|floor(P^2/ell)+s` 与倒数短区间并集公式完全一致，"
            "并登记小素数 q 上的整数/素数 ell 局部分布偏差。当前它只是分布对象的精确物化，"
            "不是 Selberg 分布证明，也没有排斥 reciprocal-floor PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase reciprocal-floor 同余账本",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"interval_formula_checked={str(result['interval_formula_checked']).lower()}",
        f"selberg_distribution_proved={str(result['selberg_distribution_proved']).lower()}",
        f"reciprocal_floor_pdec_excluded={str(result['reciprocal_floor_pdec_excluded']).lower()}",
        f"row_column_unconditional_closed={str(result['row_column_unconditional_closed']).lower()}",
        "```",
        "",
        "## 1. 参数",
        "",
        f"- `p_list`: `{result['p_list']}`",
        f"- `q_list`: `{result['q_list']}`",
        f"- `row_count`: `{result['row_count']}`",
        f"- 倒数短区间公式失败数：`{result['interval_formula_failure_count']}`",
        "",
        "## 2. 极值",
        "",
        "| item | P | q | s | bad prime | expected prime | discrepancy/sqrtP |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for name, key in [
        ("max_abs_prime", "max_prime_discrepancy_over_sqrt_p"),
        ("max_positive_prime", "max_prime_positive_discrepancy_over_sqrt_p"),
        ("max_negative_prime", "max_prime_negative_discrepancy_over_sqrt_p"),
    ]:
        row = result[key]
        lines.append(
            f"| `{name}` | {row['p']} | {row['q']} | {row['s']} | {row['bad_prime']} | "
            f"{row['expected_prime']:.3f} | {row['prime_discrepancy_over_sqrt_p']:.6f} |"
        )
    lines.extend(
        [
            "",
            "## 3. 样本行",
            "",
            "| P | q | s | bad int | exp int | bad prime | exp prime | prime disc/sqrtP | formula |",
            "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in result["sample_rows"][:60]:
        lines.append(
            f"| {row['p']} | {row['q']} | {row['s']} | {row['bad_int']} | "
            f"{row['expected_int']:.3f} | {row['bad_prime']} | {row['expected_prime']:.3f} | "
            f"{row['prime_discrepancy_over_sqrt_p']:.6f} | "
            f"`{str(row['interval_formula_matches']).lower()}` |"
        )
    lines.extend(
        [
            "",
            "## 4. 证明边界",
            "",
            "已闭合：",
            "",
            "```text",
            "q | floor(P^2/ell)+s",
            "iff exists u: floor(P^2/ell)=q*u-s",
            "iff P^2/(q*u-s+1) < ell <= P^2/(q*u-s).",
            "```",
            "",
            "未闭合：",
            "",
            "```text",
            "这些倒数短区间在素数 ell 上满足足够强的二维 Selberg 分布账本；",
            "或任何违反该账本的持续偏差都被 PDEC/SAE/ColumnCRT 排斥。",
            "```",
            "",
            "## 5. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for name, digest in sorted(result["source_hashes"].items()):
        lines.append(f"| `{name}` | `{digest}` |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--p-list", default=",".join(str(item) for item in DEFAULT_P_LIST))
    parser.add_argument("--q-list", default=",".join(str(item) for item in DEFAULT_Q_LIST))
    args = parser.parse_args()
    result = audit(parse_int_list(args.p_list), parse_int_list(args.q_list))
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result)
    print(
        json.dumps(
            {
                "status": result["status"],
                "row_count": result["row_count"],
                "interval_formula_failure_count": result["interval_formula_failure_count"],
                "selberg_distribution_proved": result["selberg_distribution_proved"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        ),
        flush=True,
    )


if __name__ == "__main__":
    main()
