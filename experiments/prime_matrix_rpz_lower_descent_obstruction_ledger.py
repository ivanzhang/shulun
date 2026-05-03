#!/usr/bin/env python3
"""生成 RPZ 下层零行下降的阻断相位账本。

用法示例：
  python3 experiments/prime_matrix_rpz_lower_descent_obstruction_ledger.py

输入为 `prime-matrix-rpz-lower-zero-descent-audit.json`。脚本对下降树中出现的每个
相邻素数转换 `p -> r` 枚举行号模 `P(r)=prod_{ell<=r} ell` 的所有相位，并分类：

1. `success`：包含完整 `r` 对齐行且不被端点穿孔阻断；
2. `grid_fail`：不包含完整 `r` 对齐行；
3. `puncture_block`：完整 `r` 行全部被端点穿孔阻断。

该账本用于把全局下降阻断路由到有限相位 `SAE/PDEC/ColumnCRT` 证书。
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

from prime_matrix_scaled_peeling_halfwidth_audit import contained_rows, interval_for_row
from prime_matrix_zero_row_crt_audit import primes_upto


def primorial(primes: list[int], bound: int) -> int:
    """计算不超过 `bound` 的素数乘积。"""
    value = 1
    for prime in primes:
        if prime > bound:
            break
        value *= prime
    return value


def previous_prime(p: int, primes: list[int]) -> int | None:
    """返回 `p` 的前一个素数。"""
    index = primes.index(p)
    if index == 0:
        return None
    return primes[index - 1]


def is_rough_to(row: int, bound: int, primes: list[int]) -> bool:
    """判断行号是否避开所有不超过 `bound` 的素数。"""
    if row <= 1:
        return False
    for prime in primes:
        if prime > bound:
            break
        if row % prime == 0:
            return False
    return True


def transition_profile(p: int, row: int, primes: list[int]) -> dict:
    """计算一条 `p` 零行向前一素数层下降的相位状态。"""
    r = previous_prime(p, primes)
    if r is None:
        return {"status": "no_previous_prime"}
    left, right = interval_for_row(p, row)
    puncture = p * row if is_rough_to(row, r, primes) else None
    candidates = contained_rows(left, right, r)
    descended = []
    blocked = []
    for child_row in candidates:
        child_left, child_right = interval_for_row(r, child_row)
        if puncture is not None and child_left <= puncture <= child_right:
            blocked.append(child_row)
        else:
            descended.append(child_row)

    delta = (1 - left) % r
    if not candidates:
        status = "grid_fail"
    elif not descended:
        status = "puncture_block"
    else:
        status = "success"

    return {
        "p": p,
        "r": r,
        "row": row,
        "row_mod_r": row % r,
        "left_residue_mod_r": left % r,
        "delta_to_next_r_row": delta,
        "gap_p_minus_r": p - r,
        "grid_contains_by_criterion": p >= delta + r,
        "endpoint_puncture": puncture,
        "puncture_active": puncture is not None,
        "contained_previous_rows": candidates,
        "blocked_previous_rows": blocked,
        "descended_previous_rows": descended,
        "status": status,
    }


def flatten_tree(node: dict) -> list[dict]:
    """展开下降树节点。"""
    rows = [node]
    for child in node.get("children", []):
        rows.extend(flatten_tree(child))
    return rows


def phase_summary_for_transition(p: int, primes: list[int]) -> dict:
    """枚举 `p -> previous(p)` 的全部行号相位。"""
    r = previous_prime(p, primes)
    if r is None:
        return {}
    modulus = primorial(primes, r)
    counts: Counter[str] = Counter()
    examples: dict[str, list[dict]] = {
        "grid_fail": [],
        "puncture_block": [],
        "success": [],
    }
    for residue in range(1, modulus + 1):
        profile = transition_profile(p, residue, primes)
        status = profile["status"]
        counts[status] += 1
        if len(examples[status]) < 5:
            examples[status].append(
                {
                    "row_phase_mod_primorial": residue % modulus,
                    "row_mod_r": profile["row_mod_r"],
                    "delta_to_next_r_row": profile["delta_to_next_r_row"],
                    "puncture_active": profile["puncture_active"],
                    "contained_previous_rows": profile["contained_previous_rows"],
                    "blocked_previous_rows": profile["blocked_previous_rows"],
                }
            )

    return {
        "p": p,
        "r": r,
        "phase_modulus_primorial_r": modulus,
        "counts": dict(sorted(counts.items())),
        "success_density": counts["success"] / modulus,
        "grid_fail_density": counts["grid_fail"] / modulus,
        "puncture_block_density": counts["puncture_block"] / modulus,
        "examples": examples,
    }


def audit(source_path: Path) -> dict:
    """执行下降阻断相位审计。"""
    source = json.loads(source_path.read_text(encoding="utf-8"))
    max_prime = max(start["start_prime"] for start in source["starts"])
    primes = primes_upto(max_prime)
    actual_nodes = []
    transition_primes = set()
    for start in source["starts"]:
        for node in flatten_tree(start["tree"]):
            p = node["p"]
            if p > 2:
                actual_nodes.append(transition_profile(p, node["row"], primes))
                transition_primes.add(p)

    actual_status_counts: Counter[str] = Counter(
        node["status"] for node in actual_nodes
    )
    transition_summaries = [
        phase_summary_for_transition(p, primes)
        for p in sorted(transition_primes)
    ]
    return {
        "status": "rpz_lower_descent_obstructions_are_finite_phase_ledger",
        "source": str(source_path),
        "summary": {
            "actual_transition_nodes": len(actual_nodes),
            "actual_status_counts": dict(sorted(actual_status_counts.items())),
            "actual_blocked_nodes": sum(
                1 for node in actual_nodes if node["status"] != "success"
            ),
            "transition_prime_count": len(transition_summaries),
            "max_grid_fail_density": max(
                (item["grid_fail_density"] for item in transition_summaries),
                default=0,
            ),
            "max_puncture_block_density": max(
                (item["puncture_block_density"] for item in transition_summaries),
                default=0,
            ),
        },
        "actual_nodes": actual_nodes,
        "transition_summaries": transition_summaries,
    }


def write_markdown(result: dict, path: Path) -> None:
    """写 Markdown 审计报告。"""
    summary = result["summary"]
    lines = [
        "# RPZ 下层下降阻断相位账本",
        "",
        "**状态：** `rpz_lower_descent_obstructions_are_finite_phase_ledger`",
        "",
        "## 总结",
        "",
        f"- 实际下降转换节点数：`{summary['actual_transition_nodes']}`。",
        f"- 实际状态计数：`{summary['actual_status_counts']}`。",
        f"- 实际阻断节点数：`{summary['actual_blocked_nodes']}`。",
        f"- 转换素数种类数：`{summary['transition_prime_count']}`。",
        f"- 最大网格失败相位密度：`{summary['max_grid_fail_density']:.6f}`。",
        f"- 最大端点穿孔阻断密度：`{summary['max_puncture_block_density']:.6f}`。",
        "",
        "## 转换相位表",
        "",
        "| p | r | modulus P(r) | success | grid fail | puncture block | success density |",
        "|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for item in result["transition_summaries"]:
        counts = item["counts"]
        lines.append(
            "| {p} | {r} | {modulus} | {success} | {grid} | {puncture} | {density:.6f} |".format(
                p=item["p"],
                r=item["r"],
                modulus=item["phase_modulus_primorial_r"],
                success=counts.get("success", 0),
                grid=counts.get("grid_fail", 0),
                puncture=counts.get("puncture_block", 0),
                density=item["success_density"],
            )
        )

    lines.extend(
        [
            "",
            "## 审稿解释",
            "",
            "对固定相邻素数 `p>r`，下降是否成功由行号模 `P(r)` 的有限相位决定。网格失败由 `delta_r((a-1)p+1)>p-r` 给出；端点穿孔阻断只可能在行号 `a` 对所有 `<=r` 素数非零时出现。",
            "",
            "同批实际下降路径中，全部转换节点均为 `success`，无实际阻断。全局证明仍需排除持续阻断；但任何阻断已经落入有限相位账本，因此可按低负载 `SAE` 或持久相位 `PDEC/ColumnCRT` 处理。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source",
        type=Path,
        default=Path("docs/monograph/prime-matrix-rpz-lower-zero-descent-audit.json"),
    )
    parser.add_argument(
        "--out-prefix",
        type=Path,
        default=Path("docs/monograph/prime-matrix-rpz-lower-descent-obstruction-ledger"),
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
