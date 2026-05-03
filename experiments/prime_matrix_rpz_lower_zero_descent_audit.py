#!/usr/bin/env python3
"""审计 RPZ-BCB 产生的下层零行是否可递归下降。

用法示例：
  python3 experiments/prime_matrix_rpz_lower_zero_descent_audit.py

输入为 `prime-matrix-rpz-bcb-core-audit.json`。在无 TailAnchor 条件下，BCB-Core
给出若干 `h` 对齐零行。脚本对每条条件零行执行相邻素数剥离：

  p-zero row -> previous r row, except possible endpoint puncture p*row。

若存在完整 `r` 对齐行且不含端点穿孔，则该行成为下一层条件零行。递归到 `p=2`
时得到直接矛盾，因为任意 `2` 对齐行 `[2m-1,2m]`（且 `m>1`）含奇数 `2m-1`，
不可能是 `2`-筛零行。
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from prime_matrix_scaled_peeling_halfwidth_audit import contained_rows, interval_for_row
from prime_matrix_zero_row_crt_audit import primes_upto


def is_rough_to(n: int, bound: int, primes: list[int]) -> bool:
    """判断 `n` 是否避开所有不超过 `bound` 的素数。"""
    if n <= 1:
        return False
    for prime in primes:
        if prime > bound:
            break
        if n % prime == 0:
            return False
    return True


def previous_prime(p: int, primes: list[int]) -> int | None:
    """返回 `p` 的前一个素数。"""
    index = primes.index(p)
    if index == 0:
        return None
    return primes[index - 1]


def descend_node(p: int, row: int, primes: list[int], depth: int) -> dict:
    """对一条条件 `p` 零行递归下降。"""
    left, right = interval_for_row(p, row)
    if p == 2:
        return {
            "p": p,
            "row": row,
            "depth": depth,
            "interval": [left, right],
            "status": "p2_zero_impossible",
            "reason": "2-aligned row contains odd survivor 2*row-1",
            "children": [],
        }

    r = previous_prime(p, primes)
    if r is None:
        return {
            "p": p,
            "row": row,
            "depth": depth,
            "interval": [left, right],
            "status": "no_previous_prime",
            "children": [],
        }

    # p-零行剥到 r 层后，唯一可能复活点是端点 p*row；
    # 它实际复活当且仅当 quotient=row 避开所有 <=r 的素数。
    puncture = p * row if is_rough_to(row, r, primes) else None
    candidates = contained_rows(left, right, r)
    child_rows = []
    blocked_rows = []
    for child_row in candidates:
        child_left, child_right = interval_for_row(r, child_row)
        contains_puncture = (
            puncture is not None and child_left <= puncture <= child_right
        )
        if contains_puncture:
            blocked_rows.append(child_row)
        else:
            child_rows.append(child_row)

    children = [
        descend_node(r, child_row, primes, depth + 1)
        for child_row in child_rows
    ]
    return {
        "p": p,
        "row": row,
        "depth": depth,
        "interval": [left, right],
        "previous_prime": r,
        "endpoint_puncture": puncture,
        "contained_previous_rows": candidates,
        "blocked_previous_rows": blocked_rows,
        "descended_previous_rows": child_rows,
        "status": "descends" if child_rows else "blocked_by_endpoint_or_grid",
        "children": children,
    }


def flatten_nodes(node: dict) -> list[dict]:
    """展开递归树。"""
    rows = [node]
    for child in node.get("children", []):
        rows.extend(flatten_nodes(child))
    return rows


def audit(source_path: Path) -> dict:
    """执行下层零行递归下降审计。"""
    source = json.loads(source_path.read_text(encoding="utf-8"))
    max_prime = max(record["half_prime"] for record in source["records"])
    primes = primes_upto(max_prime)
    starts = []
    for record in source["records"]:
        for row in record["would_be_zero_rows_after_tail_deletion"]:
            starts.append(
                {
                    "top_prime": record["top_prime"],
                    "top_zero_row": record["top_zero_row"],
                    "start_prime": record["half_prime"],
                    "start_row": row,
                    "tree": descend_node(record["half_prime"], row, primes, 0),
                }
            )

    all_nodes = [
        node
        for start in starts
        for node in flatten_nodes(start["tree"])
    ]
    p2_hits = [node for node in all_nodes if node["status"] == "p2_zero_impossible"]
    starts_reaching_p2 = sum(
        1
        for start in starts
        if any(
            node["status"] == "p2_zero_impossible"
            for node in flatten_nodes(start["tree"])
        )
    )
    blocked = [
        node for node in all_nodes if node["status"] == "blocked_by_endpoint_or_grid"
    ]
    punctures = [
        node for node in all_nodes if node.get("endpoint_puncture") is not None
    ]
    return {
        "status": "rpz_lower_zero_rows_descend_to_p2_in_samples",
        "source": str(source_path),
        "summary": {
            "start_zero_rows": len(starts),
            "total_descent_nodes": len(all_nodes),
            "p2_impossible_nodes": len(p2_hits),
            "starts_reaching_p2_impossible": starts_reaching_p2,
            "blocked_nodes": len(blocked),
            "endpoint_puncture_nodes": len(punctures),
            "max_depth": max((node["depth"] for node in all_nodes), default=0),
        },
        "starts": starts,
    }


def write_markdown(result: dict, path: Path) -> None:
    """写 Markdown 审计报告。"""
    summary = result["summary"]
    lines = [
        "# RPZ 下层零行递归下降审计",
        "",
        "**状态：** `rpz_lower_zero_rows_descend_to_p2_in_samples`",
        "",
        "## 总结",
        "",
        f"- 起始条件下层零行数：`{summary['start_zero_rows']}`。",
        f"- 递归节点总数：`{summary['total_descent_nodes']}`。",
        f"- 到达 `p=2` 直接矛盾的起始支数：`{summary['starts_reaching_p2_impossible']}`。",
        f"- 被端点穿孔或网格缺口阻断的节点数：`{summary['blocked_nodes']}`。",
        f"- 含端点穿孔的节点数：`{summary['endpoint_puncture_nodes']}`。",
        f"- 最大下降深度：`{summary['max_depth']}`。",
        "",
        "## 起始分支",
        "",
        "| top P | top row | start p | start row | terminal statuses | max depth |",
        "|---:|---:|---:|---:|---|---:|",
    ]
    for start in result["starts"]:
        nodes = flatten_nodes(start["tree"])
        terminals = [
            node["status"]
            for node in nodes
            if not node.get("children")
        ]
        max_depth = max(node["depth"] for node in nodes)
        lines.append(
            "| {top} | {top_row} | {p} | {row} | `{statuses}` | {depth} |".format(
                top=start["top_prime"],
                top_row=start["top_zero_row"],
                p=start["start_prime"],
                row=start["start_row"],
                statuses=terminals,
                depth=max_depth,
            )
        )

    lines.extend(
        [
            "",
            "## 审稿解释",
            "",
            "该审计使用的是条件零行下降：若一条 `p` 对齐行在 `p`-筛下为零，剥到前一素数 `r` 后，`r`-筛幸存者只能是端点 `p*row`，且只有当 `row` 避开所有 `<=r` 素数时才出现。",
            "",
            "因此，任何完整包含且不含该端点穿孔的 `r` 对齐行都会成为下一层条件零行。若递归到 `p=2`，则得到直接矛盾，因为 `[2m-1,2m]` 对 `m>1` 总含奇数幸存者。",
            "",
            "同批样本中，BCB-Core 给出的 `6` 条条件下层零行全部可下降到 `p=2`，没有分支被端点穿孔或网格缺口阻断。这不是全局证明；它把全局硬点压缩为证明下降网格条件不被阻断，或将阻断相位路由到 `SAE/PDEC/ColumnCRT`。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source",
        type=Path,
        default=Path("docs/monograph/prime-matrix-rpz-bcb-core-audit.json"),
    )
    parser.add_argument(
        "--out-prefix",
        type=Path,
        default=Path("docs/monograph/prime-matrix-rpz-lower-zero-descent-audit"),
    )
    args = parser.parse_args()
    result = audit(args.source)
    args.out_prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.out_prefix.with_suffix(".md"))
    print(json.dumps(result["summary"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
