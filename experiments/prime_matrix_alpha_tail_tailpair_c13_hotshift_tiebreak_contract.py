#!/usr/bin/env python3
"""AlphaTail C13 热门位移正负并列 tie-break 审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_c13_hotshift_tiebreak_contract.py --p-list 997,5003,10007 --format table
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict

from prime_matrix_alpha_tail_additive_energy_audit import low_squarefree_block
from prime_matrix_alpha_tail_tailpair_c13_target_family_contract import next_power_of_two


def parse_p_list(raw: str) -> list[int]:
    """解析素数列表。"""
    return [int(part) for part in raw.split(",") if part.strip()]


def tiebreak_row(prime_bound: int, alpha: float, sign: str) -> dict:
    """返回单个 p 的热门位移并列审计。"""
    block = next_power_of_two(prime_bound + 1)
    values = low_squarefree_block(int(alpha * prime_bound), block, sign)
    diff_counts: dict[int, int] = defaultdict(int)
    for left in values:
        for right in values:
            diff = left - right
            if diff == 0:
                continue
            diff_counts[diff] += 1
    max_count = max(diff_counts.values(), default=0)
    max_diffs = sorted(diff for diff, count in diff_counts.items() if count == max_count)
    max_abs_diffs = sorted({abs(diff) for diff in max_diffs})
    oriented_shift = -max_abs_diffs[0] if len(max_abs_diffs) == 1 else None
    sign_symmetric = all(-diff in max_diffs for diff in max_diffs)
    return {
        "p": prime_bound,
        "block": block,
        "sign": sign,
        "d_count": len(values),
        "max_count": max_count,
        "max_diffs": max_diffs,
        "max_abs_diffs": max_abs_diffs,
        "max_diff_count": len(max_diffs),
        "max_abs_count": len(max_abs_diffs),
        "sign_symmetric": sign_symmetric,
        "oriented_shift": oriented_shift,
        "oriented_unique": oriented_shift is not None and sign_symmetric,
    }


def hotshift_tiebreak_package(p_list: list[int], alpha: float, sign: str) -> dict:
    """返回热门位移 tie-break 合同包。"""
    rows = [tiebreak_row(prime_bound, alpha, sign) for prime_bound in p_list]
    total = {
        "windows": len(rows),
        "all_sign_symmetric": all(row["sign_symmetric"] for row in rows),
        "all_oriented_unique": all(row["oriented_unique"] for row in rows),
        "generated_selected": ",".join(
            f"{row['p']}:{row['block']}:{row['oriented_shift']}"
            for row in rows
            if row["oriented_shift"] is not None
        ),
        "max_abs_counts": {row["p"]: row["max_abs_count"] for row in rows},
    }
    return {
        "p_list": p_list,
        "alpha": alpha,
        "sign": sign,
        "status": "hotshift_tiebreak_sample_closed_global_open",
        "total": total,
        "rows": rows,
    }


def print_table(package: dict) -> None:
    """输出热门位移 tie-break 表。"""
    total = package["total"]
    print(
        "scope windows sign_symmetric oriented_unique generated_selected max_abs_counts",
        flush=True,
    )
    print(
        f"tiebreak-total {total['windows']} {total['all_sign_symmetric']} "
        f"{total['all_oriented_unique']} {total['generated_selected']} "
        f"{total['max_abs_counts']}",
        flush=True,
    )
    print(
        "p block sign d_count max_count max_diffs max_abs_diffs sign_symmetric oriented_shift oriented_unique",
        flush=True,
    )
    for row in package["rows"]:
        print(
            f"{row['p']} {row['block']} {row['sign']} {row['d_count']} "
            f"{row['max_count']} {row['max_diffs']} {row['max_abs_diffs']} "
            f"{row['sign_symmetric']} {row['oriented_shift']} {row['oriented_unique']}",
            flush=True,
        )


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--p-list", type=str, default="997,5003,10007")
    parser.add_argument("--alpha", type=float, default=0.9)
    parser.add_argument("--sign", choices=("+", "-"), default="-")
    parser.add_argument("--format", choices=("json", "table", "repr"), default="repr")
    args = parser.parse_args()

    package = hotshift_tiebreak_package(parse_p_list(args.p_list), args.alpha, args.sign)
    if args.format == "json":
        print(json.dumps(package, ensure_ascii=False, indent=2), flush=True)
        return
    if args.format == "table":
        print_table(package)
        return
    print(package, flush=True)


if __name__ == "__main__":
    main()
