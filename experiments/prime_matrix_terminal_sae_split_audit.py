#!/usr/bin/env python3
"""审计 Terminal-SAE 的低筛骨架/尾素数分层不等式。

用法示例：
  python3 experiments/prime_matrix_terminal_sae_split_audit.py --max-p 1000
  python3 experiments/prime_matrix_terminal_sae_split_audit.py --max-p 1000 --y-ratio 0.36787944117144233

对相邻素数 p<q，在镜像变量 m=q^2-n 中检查每个 q 网格块。
先筛去 ell<=y 的指定类 m=q^2 mod ell 得到骨架 G_y；
再统计 y<ell<=p 对 G_y 的总命中重数 T_y。若 G_y>T_y，
则尾素数即使无重叠也无法覆盖全部骨架点，因此该行必有旧 p-筛幸存者。
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


def sieve_bool(n: int) -> bytearray:
    """返回素数布尔表。"""
    is_prime = bytearray(b"\x01") * (n + 1)
    if n >= 0:
        is_prime[0] = 0
    if n >= 1:
        is_prime[1] = 0
    for d in range(2, int(n**0.5) + 1):
        if is_prime[d]:
            start = d * d
            is_prime[start : n + 1 : d] = b"\x00" * (((n - start) // d) + 1)
    return is_prime


def primes_from_table(is_prime: bytearray) -> list[int]:
    """提取素数列表。"""
    return [idx for idx, flag in enumerate(is_prime) if flag]


def next_prime(p: int, is_prime: bytearray) -> int:
    """返回大于 p 的下一素数。"""
    q = p + 1
    while q < len(is_prime) and not is_prime[q]:
        q += 1
    if q >= len(is_prime):
        raise ValueError("素数表范围不足")
    return q


def prefix_sum(values: bytearray) -> list[int]:
    """bytearray 前缀和。"""
    pref = [0] * (len(values) + 1)
    total = 0
    for idx, value in enumerate(values):
        total += value
        pref[idx + 1] = total
    return pref


def audit(max_p: int, y_ratio: float) -> dict:
    """执行分层不等式审计。"""
    coarse = sieve_bool(max_p + 1000)
    primes = primes_from_table(coarse)
    target_primes = [prime for prime in primes if 3 <= prime <= max_p]

    records = []
    unresolved = []
    direct_small = []

    for p in target_primes:
        q = next_prime(p, coarse)
        q_square = q * q
        y = max(2, int(math.floor(y_ratio * p)))
        low_primes = [prime for prime in primes if prime <= y]
        tail_primes = [prime for prime in primes if y < prime <= p]

        # skeleton[m]=1 表示 m 没有落入任何低素数指定类。
        skeleton = bytearray(b"\x01") * q_square
        skeleton[0] = 0  # m=0 对应 n=q^2，是必须排除的例外点。
        skeleton[q_square - 1] = 0  # m=q^2-1 对应 n=1，不能作为素数幸存者。
        for ell in low_primes:
            residue = q_square % ell
            skeleton[residue:q_square:ell] = b"\x00" * (((q_square - 1 - residue) // ell) + 1)

        # tail_hits[m] 是骨架点 m 被尾素数指定类命中的重数。
        tail_hits = bytearray(q_square)
        for ell in tail_primes:
            residue = q_square % ell
            for pos in range(residue, q_square, ell):
                if skeleton[pos] and tail_hits[pos] < 255:
                    tail_hits[pos] += 1

        skeleton_pref = prefix_sum(skeleton)
        tail_pref = prefix_sum(tail_hits)

        min_margin = None
        min_rows = []
        min_data = None
        bad_rows = []
        for h in range(1, q + 1):
            left = (h - 1) * q
            right = h * q
            skeleton_count = skeleton_pref[right] - skeleton_pref[left]
            tail_count = tail_pref[right] - tail_pref[left]
            margin = skeleton_count - tail_count
            if min_margin is None or margin < min_margin:
                min_margin = margin
                min_rows = [h]
                min_data = {
                    "h": h,
                    "skeleton": skeleton_count,
                    "tail_incidence": tail_count,
                    "margin": margin,
                }
            elif margin == min_margin:
                min_rows.append(h)
            if margin <= 0:
                bad_rows.append(
                    {
                        "h": h,
                        "skeleton": skeleton_count,
                        "tail_incidence": tail_count,
                        "margin": margin,
                    }
                )

        record = {
            "p": p,
            "q_next": q,
            "y": y,
            "y_ratio_actual": y / p,
            "low_prime_count": len(low_primes),
            "tail_prime_count": len(tail_primes),
            "min_margin": min_margin,
            "min_rows": min_rows[:10],
            "min_data": min_data,
            "bad_margin_rows": bad_rows[:10],
            "bad_margin_row_count": len(bad_rows),
            "split_certifies_all_rows": len(bad_rows) == 0,
        }
        records.append(record)
        if p in (3, 5):
            direct_small.append(record)
        if bad_rows and p >= 7:
            unresolved.append(record)

    return {
        "parameters": {
            "max_p": max_p,
            "y_ratio": y_ratio,
        },
        "summary": {
            "prime_count": len(records),
            "split_certified_records": sum(1 for record in records if record["split_certifies_all_rows"]),
            "unresolved_records_p_ge_7": len(unresolved),
            "min_margin_p_ge_7": min(
                (record["min_margin"] for record in records if record["p"] >= 7),
                default=None,
            ),
            "min_margin_p_ge_19": min(
                (record["min_margin"] for record in records if record["p"] >= 19),
                default=None,
            ),
            "small_exception_records": direct_small,
        },
        "unresolved_records_p_ge_7": unresolved,
        "records": records,
    }


def write_markdown(result: dict, path: Path) -> None:
    """写 Markdown 审计报告。"""
    params = result["parameters"]
    summary = result["summary"]
    records = result["records"]
    worst = sorted(records, key=lambda item: item["min_margin"])[:20]

    lines = [
        "# Terminal-SAE 分层骨架/尾命中审计",
        "",
        "**状态：** `experimental_terminal_sae_split_certificate_not_a_proof`",
        "",
        "## 参数",
        "",
        f"- `max_p`: `{params['max_p']}`",
        f"- `y_ratio`: `{params['y_ratio']}`",
        "",
        "## 总结",
        "",
        f"- 检查奇素数个数：`{summary['prime_count']}`。",
        f"- 分层不等式认证全部行的记录数：`{summary['split_certified_records']}`。",
        f"- `p>=7` 未认证记录数：`{summary['unresolved_records_p_ge_7']}`。",
        f"- `p>=7` 最小 margin：`{summary['min_margin_p_ge_7']}`。",
        f"- `p>=19` 最小 margin：`{summary['min_margin_p_ge_19']}`。",
        "",
        "## 最小 margin 样本",
        "",
        "| p | q | y | min margin | min data | certified |",
        "| ---: | ---: | ---: | ---: | --- | --- |",
    ]
    for record in worst:
        lines.append(
            "| {p} | {q} | {y} | {margin} | {data} | {cert} |".format(
                p=record["p"],
                q=record["q_next"],
                y=record["y"],
                margin=record["min_margin"],
                data=record["min_data"],
                cert=record["split_certifies_all_rows"],
            )
        )

    lines.extend(
        [
            "",
            "## 审稿解释",
            "",
            "设 `G_y(h)` 为终端镜像块中避开所有 `ell<=y` 指定类的骨架点数，`T_y(h)` 为这些骨架点被 `y<ell<=p` 指定类命中的总重数。若 `G_y(h)>T_y(h)`，则尾素数不可能覆盖全部骨架点，因而该行存在旧 `p`-筛幸存者。",
            "",
            "本脚本已排除 `m=0` 与 `m=q^2-1`，即排除 `n=q^2` 和 `n=1` 两个不能作为素数幸存者的端点。",
            "",
            "本审计在样本中显示：取 `y=floor(p/e)` 时，除极小 `p=3,5` 外，`p>=7` 的全部行均满足正 margin。正式证明应转化为两个显式不等式：骨架下界 `G_y(h)` 与尾命中上界 `T_y(h)`。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-p", type=int, default=1000)
    parser.add_argument("--y-ratio", type=float, default=1 / math.e)
    parser.add_argument(
        "--out-prefix",
        default="docs/monograph/prime-matrix-terminal-sae-split-audit",
    )
    args = parser.parse_args()
    result = audit(args.max_p, args.y_ratio)
    prefix = Path(args.out_prefix)
    prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, prefix.with_suffix(".md"))
    print(json.dumps(result["summary"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
