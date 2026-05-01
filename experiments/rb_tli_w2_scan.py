#!/usr/bin/env python3
"""扫描 w=2 的 RB-TLI 数值结构。

用法示例：
  python experiments/rb_tli_w2_scan.py --P 101 211 503 1009 --output docs/rb-tli-w2-scan.json
  python experiments/rb_tli_w2_scan.py --P 2003 5003 --markdown docs/rb-tli-w2-scan.md
"""

from __future__ import annotations

import argparse
import json
import math
from collections import Counter
from pathlib import Path


def prime_sieve(limit: int) -> tuple[list[int], bytearray]:
    """返回不超过 limit 的素数表和素性表。"""
    if limit < 2:
        return [], bytearray(b"\x00") * (limit + 1)
    is_prime = bytearray(b"\x01") * (limit + 1)
    is_prime[0:2] = b"\x00\x00"
    root = int(limit**0.5)
    for n in range(2, root + 1):
        if is_prime[n]:
            start = n * n
            is_prime[start : limit + 1 : n] = b"\x00" * (((limit - start) // n) + 1)
    return [n for n in range(2, limit + 1) if is_prime[n]], is_prime


def first_index_for_residue(low: int, modulus: int, residue: int) -> int:
    """求区间起点 low 后第一个满足 x == residue mod modulus 的偏移。"""
    return (residue - low) % modulus


def clear_residue(mask: bytearray, low: int, modulus: int, residue: int) -> None:
    """把指定同余类从候选集合中删除。"""
    start = first_index_for_residue(low, modulus, residue)
    mask[start::modulus] = b"\x00" * (((len(mask) - 1 - start) // modulus) + 1)


def scan_one(P: int, alpha: float, primes: list[int], is_prime_small: bytearray) -> dict:
    """精确扫描单个 P 的后半区间。"""
    w = 2
    Y = int(P**alpha)
    low = P * P // 2 + 1
    high = P * P
    n = high - low + 1

    old_primes = [p for p in primes if p <= Y]
    new_primes = [p for p in primes if Y < p <= P]

    # U_Y：避开所有 q<=Y 的 0 与 w 同余类；q=2 时两类重合。
    mask = bytearray(b"\x01") * n
    for q in old_primes:
        residues = {0, w % q}
        for residue in residues:
            clear_residue(mask, low, q, residue)

    U_count = int(sum(mask))
    D = bytearray(n)
    dx = bytearray(n)
    dy = bytearray(n)
    total_hits = 0
    top_primes: list[tuple[int, int, float]] = []
    quotient_prime_failures = 0
    ordered_hits = 0
    quotient_le_p = 0
    quotient_gt_p = 0
    shell_edges = [alpha + (1.0 - alpha) * i / 5.0 for i in range(6)]
    shell_hits = [0 for _ in range(5)]

    for p in new_primes:
        Ap = 0
        t = math.log(p) / math.log(P)
        shell_index = min(4, max(0, int((t - alpha) / ((1.0 - alpha) / 5.0))))

        # x == 0 mod p 分支。
        start = first_index_for_residue(low, p, 0)
        for idx in range(start, n, p):
            if mask[idx]:
                D[idx] += 1
                dx[idx] += 1
                Ap += 1
                shell_hits[shell_index] += 1
                ordered_hits += 1
                x = low + idx
                m = x // p
                if m < len(is_prime_small) and not is_prime_small[m]:
                    quotient_prime_failures += 1
                if m <= P:
                    quotient_le_p += 1
                else:
                    quotient_gt_p += 1

        # x == w mod p 分支，即 x-w 被 p 整除。
        start = first_index_for_residue(low, p, w % p)
        for idx in range(start, n, p):
            if mask[idx]:
                D[idx] += 1
                dy[idx] += 1
                Ap += 1
                shell_hits[shell_index] += 1
                ordered_hits += 1
                x = low + idx
                m = (x - w) // p
                if m < len(is_prime_small) and not is_prime_small[m]:
                    quotient_prime_failures += 1
                if m <= P:
                    quotient_le_p += 1
                else:
                    quotient_gt_p += 1

        if U_count:
            top_primes.append((p, Ap, Ap / U_count))
        total_hits += Ap

    d_dist: Counter[int] = Counter()
    side_dist: Counter[tuple[int, int]] = Counter()
    dx_sum = 0
    dy_sum = 0
    dx2_sum = 0
    dy2_sum = 0
    dxdy_sum = 0
    both_sides_count = 0
    same_side_double_count = 0
    for idx, alive in enumerate(mask):
        if alive:
            dx_value = int(dx[idx])
            dy_value = int(dy[idx])
            d_dist[int(D[idx])] += 1
            side_dist[(dx_value, dy_value)] += 1
            dx_sum += dx_value
            dy_sum += dy_value
            dx2_sum += dx_value * dx_value
            dy2_sum += dy_value * dy_value
            dxdy_sum += dx_value * dy_value
            if dx_value and dy_value:
                both_sides_count += 1
            if dx_value >= 2 or dy_value >= 2:
                same_side_double_count += 1

    model_sum = 2.0 * sum(1.0 / p for p in new_primes)
    merten_alpha = 2.0 * math.log(1.0 / alpha)
    # 在 alpha>2/3 时，Buchstab 主项可显式化：
    # K(alpha)=2L/(1+L), L=log((2-alpha)/alpha)。
    buchstab_L = math.log((2.0 - alpha) / alpha)
    buchstab_two_side = 2.0 * buchstab_L / (1.0 + buchstab_L)
    expected_shells = []
    for left, right in zip(shell_edges[:-1], shell_edges[1:]):
        expected = 2.0 / (1.0 + buchstab_L) * (
            math.log(right / (2.0 - right)) - math.log(left / (2.0 - left))
        )
        expected_shells.append(
            {
                "t_left": left,
                "t_right": right,
                "expected_avg_hits": expected,
            }
        )
    avg_D = total_hits / U_count if U_count else float("nan")
    zero_count = d_dist.get(0, 0)
    avg_dx = dx_sum / U_count if U_count else float("nan")
    avg_dy = dy_sum / U_count if U_count else float("nan")
    avg_dxdy = dxdy_sum / U_count if U_count else float("nan")

    top_primes.sort(key=lambda item: item[2], reverse=True)
    return {
        "P": P,
        "alpha": alpha,
        "Y_floor": Y,
        "interval": [low, high],
        "interval_size": n,
        "old_prime_count": len(old_primes),
        "new_prime_count": len(new_primes),
        "U_count": U_count,
        "U_density": U_count / n,
        "total_large_hits": total_hits,
        "avg_D_on_U": avg_D,
        "model_2_sum_1_over_p": model_sum,
        "model_2_log_1_over_alpha": merten_alpha,
        "buchstab_two_side_K_alpha": buchstab_two_side,
        "avg_minus_buchstab_K": avg_D - buchstab_two_side,
        "avg_minus_model_sum": avg_D - model_sum,
        "tli_margin_1_minus_avg": 1.0 - avg_D,
        "zero_count_D0": zero_count,
        "zero_fraction_in_U": zero_count / U_count if U_count else float("nan"),
        "D_distribution": {str(k): v for k, v in sorted(d_dist.items())},
        "side_distribution": {f"{k[0]},{k[1]}": v for k, v in sorted(side_dist.items())},
        "avg_dx": avg_dx,
        "avg_dy": avg_dy,
        "avg_dxdy": avg_dxdy,
        "dxdy_covariance": avg_dxdy - avg_dx * avg_dy,
        "avg_dx2": dx2_sum / U_count if U_count else float("nan"),
        "avg_dy2": dy2_sum / U_count if U_count else float("nan"),
        "both_sides_fraction": both_sides_count / U_count if U_count else float("nan"),
        "same_side_double_fraction": same_side_double_count / U_count if U_count else float("nan"),
        "shell_hits": [
            {
                **expected_shells[index],
                "actual_hits": shell_hits[index],
                "actual_avg_hits": shell_hits[index] / U_count if U_count else float("nan"),
                "actual_minus_expected": (
                    shell_hits[index] / U_count - expected_shells[index]["expected_avg_hits"]
                    if U_count
                    else float("nan")
                ),
            }
            for index in range(5)
        ],
        "top_prime_hits": [
            {"p": p, "A_p": Ap, "A_p_over_U": ratio} for p, Ap, ratio in top_primes[:10]
        ],
        "ordered_hits": ordered_hits,
        "quotient_prime_failures": quotient_prime_failures,
        "quotient_le_P_fraction": quotient_le_p / ordered_hits if ordered_hits else 0.0,
        "quotient_gt_P_fraction": quotient_gt_p / ordered_hits if ordered_hits else 0.0,
    }


def render_markdown(results: list[dict]) -> str:
    """生成简明 Markdown 表和结构摘要。"""
    lines = [
        "# w=2 的 RB-TLI 数值扫描",
        "",
        "区间取 `I=(P^2/2, P^2]`，`Y=floor(P^alpha)`。",
        "",
        "| P | alpha | Y | |U_Y| | avg D | Buchstab K | 2sum1/p | 1-avgD | D=0比例 | 商素性失败 |",
        "|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in results:
        lines.append(
            "| {P} | {alpha:.2f} | {Y_floor} | {U_count} | {avg_D_on_U:.6f} | "
            "{buchstab_two_side_K_alpha:.6f} | {model_2_sum_1_over_p:.6f} | "
            "{tli_margin_1_minus_avg:.6f} | "
            "{zero_fraction_in_U:.6f} | {quotient_prime_failures} |".format(**row)
        )
    lines.extend(["", "## 结构分布", ""])
    for row in results:
        lines.append(f"### P={row['P']}")
        lines.append(f"- `D` 分布：`{row['D_distribution']}`")
        lines.append(f"- 侧分布 `(x侧命中,x-2侧命中)`：`{row['side_distribution']}`")
        lines.append(
            "- 商数范围：`m<=P` 比例 `{:.6f}`，`m>P` 比例 `{:.6f}`。".format(
                row["quotient_le_P_fraction"], row["quotient_gt_P_fraction"]
            )
        )
        lines.append(
            "- 两侧协方差：`{:.6f}`；双侧均命中比例 `{:.6f}`；同侧双命中比例 `{:.6f}`。".format(
                row["dxdy_covariance"],
                row["both_sides_fraction"],
                row["same_side_double_fraction"],
            )
        )
        shell_summary = [
            "({:.2f},{:.2f}]: {:.4f}/{:.4f}".format(
                item["t_left"],
                item["t_right"],
                item["actual_avg_hits"],
                item["expected_avg_hits"],
            )
            for item in row["shell_hits"]
        ]
        lines.append(f"- 壳层实际/期望命中：`{shell_summary}`")
        lines.append(f"- 最大单素数命中：`{row['top_prime_hits'][:3]}`")
        lines.append("")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--P", nargs="+", type=int, required=True, help="要扫描的 P 值")
    parser.add_argument("--alpha", type=float, default=0.75, help="Y=P^alpha")
    parser.add_argument("--output", type=Path, help="JSON 输出路径")
    parser.add_argument("--markdown", type=Path, help="Markdown 输出路径")
    args = parser.parse_args()

    max_p = max(args.P)
    max_quotient = int(max_p ** (2.0 - args.alpha)) + 10
    sieve_limit = max(max_p, max_quotient)
    primes, is_prime = prime_sieve(sieve_limit)
    results = [scan_one(P, args.alpha, primes, is_prime) for P in args.P]

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    if args.markdown:
        args.markdown.parent.mkdir(parents=True, exist_ok=True)
        args.markdown.write_text(render_markdown(results), encoding="utf-8")
    if not args.output and not args.markdown:
        print(json.dumps(results, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
