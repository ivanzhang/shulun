#!/usr/bin/env python3
"""审计对角平方后端点的 RCI 抵消不等式。

用法示例：
  python3 experiments/prime_matrix_diagonal_postsquare_rci_audit.py --max-p 2000

对 x=p 的对角行 n=p^2+k, 1<=k<p，先筛去 ell<=y 的低素数，
再统计 y<ell<p 的尾素因子数。与 Terminal-RCI 一样，
单尾项抵消，目标是 no_tail_reserve > multi_tail_excess。
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


def sieve_bool(limit: int) -> bytearray:
    """返回素数布尔表。"""
    flags = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        flags[0] = 0
    if limit >= 1:
        flags[1] = 0
    for value in range(2, int(limit**0.5) + 1):
        if flags[value]:
            start = value * value
            flags[start : limit + 1 : value] = b"\x00" * (
                ((limit - start) // value) + 1
            )
    return flags


def primes_from_table(flags: bytearray) -> list[int]:
    """提取素数列表。"""
    return [idx for idx, flag in enumerate(flags) if flag]


def audit_p(p: int, primes: list[int], y_ratio: float) -> dict:
    """审计单个 p 的平方后端点行。"""
    y = max(2, int(math.floor(y_ratio * p)))
    low_primes = [prime for prime in primes if prime <= y]
    tail_primes = [prime for prime in primes if y < prime < p]

    low_rough = bytearray(b"\x01") * p
    low_rough[0] = 0
    p_square = p * p
    for ell in low_primes:
        residue = (-p_square) % ell
        start = residue if residue != 0 else ell
        if start >= p:
            continue
        low_rough[start:p:ell] = b"\x00" * (((p - 1 - start) // ell) + 1)

    tail_omega = bytearray(p)
    for ell in tail_primes:
        residue = (-p_square) % ell
        start = residue if residue != 0 else ell
        if start >= p:
            continue
        for column in range(start, p, ell):
            if low_rough[column] and tail_omega[column] < 255:
                tail_omega[column] += 1

    low_count = 0
    tail_incidence = 0
    no_tail = 0
    one_tail = 0
    multi_count = 0
    multi_excess = 0
    max_tail_omega = 0
    no_tail_sample = []
    multi_sample = []

    for column in range(1, p):
        if not low_rough[column]:
            continue
        low_count += 1
        omega = tail_omega[column]
        tail_incidence += omega
        if omega > max_tail_omega:
            max_tail_omega = omega
        if omega == 0:
            no_tail += 1
            if len(no_tail_sample) < 5:
                no_tail_sample.append({"column": column, "value": p_square + column})
        elif omega == 1:
            one_tail += 1
        else:
            multi_count += 1
            multi_excess += omega - 1
            if len(multi_sample) < 5:
                multi_sample.append(
                    {
                        "column": column,
                        "value": p_square + column,
                        "omega_tail": omega,
                    }
                )

    margin = low_count - tail_incidence
    if margin != no_tail - multi_excess:
        raise AssertionError("RCI 抵消恒等式失败")

    return {
        "p": p,
        "y": y,
        "low_prime_count": len(low_primes),
        "tail_prime_count": len(tail_primes),
        "low_skeleton": low_count,
        "tail_incidence": tail_incidence,
        "no_tail_reserve": no_tail,
        "one_tail_cancelled": one_tail,
        "multi_tail_count": multi_count,
        "multi_tail_excess": multi_excess,
        "margin": margin,
        "certified": margin > 0,
        "max_tail_omega": max_tail_omega,
        "two_tail_only_by_y3_gt_endpoint": y**3 > p_square + p,
        "no_tail_sample": no_tail_sample,
        "multi_tail_sample": multi_sample,
    }


def audit(max_p: int, y_ratio: float) -> dict:
    """执行审计。"""
    flags = sieve_bool(max_p)
    primes = primes_from_table(flags)
    target_primes = [prime for prime in primes if prime >= 3]
    records = [audit_p(p, primes, y_ratio) for p in target_primes]
    bad = [record for record in records if not record["certified"]]
    worst = sorted(records, key=lambda item: item["margin"])[:20]
    return {
        "parameters": {"max_p": max_p, "y_ratio": y_ratio},
        "summary": {
            "prime_count": len(records),
            "certified_count": sum(1 for record in records if record["certified"]),
            "bad_count": len(bad),
            "min_margin": min((record["margin"] for record in records), default=None),
            "min_margin_p_ge_13": min(
                (record["margin"] for record in records if record["p"] >= 13),
                default=None,
            ),
            "max_tail_omega": max(
                (record["max_tail_omega"] for record in records), default=None
            ),
            "records_with_y3_gt_endpoint": sum(
                1 for record in records if record["two_tail_only_by_y3_gt_endpoint"]
            ),
            "last_y3_le_endpoint_p": max(
                (
                    record["p"]
                    for record in records
                    if not record["two_tail_only_by_y3_gt_endpoint"]
                ),
                default=None,
            ),
            "worst_records": worst,
        },
        "bad_records": bad[:20],
        "records": records,
    }


def write_markdown(result: dict, path: Path) -> None:
    """写 Markdown 报告。"""
    params = result["parameters"]
    summary = result["summary"]
    lines = [
        "# 对角平方后端点 RCI 审计",
        "",
        "**状态：** `experimental_postsquare_rci_support_not_a_proof`",
        "",
        "## 参数",
        "",
        f"- `max_p`: `{params['max_p']}`",
        f"- `y_ratio`: `{params['y_ratio']}`",
        "",
        "## 总结",
        "",
        f"- 检查奇素数个数：`{summary['prime_count']}`。",
        f"- 认证个数：`{summary['certified_count']}`。",
        f"- 未认证个数：`{summary['bad_count']}`。",
        f"- 最小 margin：`{summary['min_margin']}`。",
        f"- `p>=13` 最小 margin：`{summary['min_margin_p_ge_13']}`。",
        f"- 最大 `omega_tail`：`{summary['max_tail_omega']}`。",
        f"- 满足 `y^3>p^2+p` 的记录数：`{summary['records_with_y3_gt_endpoint']}`。",
        f"- 最后一个 `y^3<=p^2+p` 的 p：`{summary['last_y3_le_endpoint_p']}`。",
        "",
        "## 最小 margin 样本",
        "",
        "| p | y | low | tail | no-tail | one-tail | multi-excess | margin | sample |",
        "|---:|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for record in summary["worst_records"]:
        lines.append(
            "| {p} | {y} | {low} | {tail} | {no_tail} | {one_tail} | {excess} | {margin} | {sample} |".format(
                p=record["p"],
                y=record["y"],
                low=record["low_skeleton"],
                tail=record["tail_incidence"],
                no_tail=record["no_tail_reserve"],
                one_tail=record["one_tail_cancelled"],
                excess=record["multi_tail_excess"],
                margin=record["margin"],
                sample=record["no_tail_sample"],
            )
        )
    lines.extend(
        [
            "",
            "## 审稿解释",
            "",
            "对 `p^2+k`，低筛骨架点按尾素因子数分层后精确满足",
            "",
            "```text",
            "G_y-T_y = no_tail_reserve - multi_tail_excess。",
            "```",
            "",
            "若该差值为正，则存在一个 `p^2+k` 没有任何 `<p` 素因子；由于 `p^2<p^2+k<p^2+p<(p+1)^2`，该点必为素数。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-p", type=int, default=2000)
    parser.add_argument("--y-ratio", type=float, default=1 / math.e)
    parser.add_argument(
        "--out-prefix",
        default="docs/diagonal_postsquare_rci_audit_20260505",
    )
    args = parser.parse_args()
    result = audit(args.max_p, args.y_ratio)
    prefix = Path(args.out_prefix)
    prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, prefix.with_suffix(".md"))
    compact = {
        key: value
        for key, value in result["summary"].items()
        if key != "worst_records"
    }
    print(json.dumps(compact, ensure_ascii=False, indent=2), flush=True)


if __name__ == "__main__":
    main()
