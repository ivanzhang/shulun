#!/usr/bin/env python3
"""审计平衡双尾半素数周围的轮筛阴影刚性。

用法示例：
  python3 experiments/prime_matrix_semiprime_wheel_shadow_audit.py --max-p 1000
  python3 experiments/prime_matrix_semiprime_wheel_shadow_audit.py --max-p 2000 --radius 160
  python3 experiments/prime_matrix_semiprime_wheel_shadow_audit.py --max-p 500 --near-offset 30

对平衡双尾半素数 n=ell1*ell2，ell_i in (y,p]，统计短偏移 d 中
哪些会被小素数轮筛立刻排除。若 n+d 要成为素数，必须避开所有小素数
r<=z 的同余类 d≡-n mod r。
"""

from __future__ import annotations

import argparse
import bisect
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


def next_prime(p: int, primes: list[int]) -> int:
    """返回大于 p 的下一素数。"""
    for prime in primes:
        if prime > p:
            return prime
    raise ValueError("素数表范围不足")


def build_tail_data(
    q: int,
    low_primes: list[int],
    tail_primes: list[int],
) -> tuple[bytearray, bytearray, dict[int, list[int]]]:
    """构造低筛骨架、尾因子数和尾标签。"""
    q_square = q * q
    low_rough = bytearray(b"\x01") * (q_square + 1)
    low_rough[0] = 0
    low_rough[1] = 0
    low_rough[q_square] = 0
    for ell in low_primes:
        low_rough[0 : q_square + 1 : ell] = b"\x00" * ((q_square // ell) + 1)

    tail_omega = bytearray(q_square + 1)
    tail_labels: dict[int, list[int]] = {}
    for ell in tail_primes:
        for pos in range(ell, q_square + 1, ell):
            if not low_rough[pos]:
                continue
            tail_omega[pos] += 1
            tail_labels.setdefault(pos, []).append(ell)
    return low_rough, tail_omega, tail_labels


def nearest_distance(value: int, sorted_values: list[int]) -> int | None:
    """返回 value 到有序列表的最近距离。"""
    if not sorted_values:
        return None
    pos = bisect.bisect_left(sorted_values, value)
    best = None
    for idx in (pos - 1, pos):
        if 0 <= idx < len(sorted_values):
            distance = abs(sorted_values[idx] - value)
            if best is None or distance < best:
                best = distance
    return best


def wheel_allowed(value: int, offset: int, wheel_primes: list[int]) -> bool:
    """判断 value+offset 是否避开所有 wheel_primes。"""
    candidate = value + offset
    if candidate <= 1:
        return False
    return all(candidate % prime for prime in wheel_primes)


def offset_stats(
    value: int,
    row_left: int,
    row_right: int,
    radius: int,
    wheel_primes: list[int],
) -> dict:
    """统计轮筛允许偏移。"""
    offsets = [
        offset
        for offset in range(-radius, radius + 1)
        if offset != 0 and row_left <= value + offset <= row_right
    ]
    allowed_offsets = [
        offset for offset in offsets if wheel_allowed(value, offset, wheel_primes)
    ]
    min_allowed_abs = min((abs(offset) for offset in allowed_offsets), default=None)
    return {
        "total_offsets": len(offsets),
        "allowed_offsets": len(allowed_offsets),
        "shadowed_offsets": len(offsets) - len(allowed_offsets),
        "allowed_ratio": len(allowed_offsets) / len(offsets) if offsets else None,
        "shadow_ratio": 1 - len(allowed_offsets) / len(offsets) if offsets else None,
        "min_allowed_abs": min_allowed_abs,
    }


def fixed_shift_theory_ratio(offset: int, wheel_primes: list[int]) -> float:
    """给出固定偏移 d 的轮筛双单位理论比例。

    在模 W_z 的单位类 u 中，要求 u+d 仍为单位。对每个小素数 r：
    若 r|d，则所有非零 u 都保留；若 r∤d，则禁掉 u≡-d mod r 的一个非零类。
    """
    numerator = 1
    denominator = 1
    for prime in wheel_primes:
        denominator *= prime - 1
        if offset % prime == 0:
            numerator *= prime - 1
        else:
            numerator *= prime - 2
    return numerator / denominator if denominator else 0.0


def audit(
    max_p: int,
    min_p: int,
    y_ratio: float,
    radius: int,
    near_offset: int,
    wheels: list[int],
) -> dict:
    """执行轮筛阴影审计。"""
    is_prime = sieve_bool(max_p * max_p + max_p * 20 + 10000)
    primes = primes_from_table(is_prime)
    target_primes = [prime for prime in primes if min_p <= prime <= max_p]
    wheel_primes = [prime for prime in primes if prime in set(wheels)]

    total_semiprimes = 0
    nearest_distances = []
    samples = []
    worst_shadow_samples = []
    worst_nearest_samples = []
    no_allowed_count = 0
    nearest_equals_wheel_min = 0
    fixed_offset_total = {
        offset: 0 for offset in range(-near_offset, near_offset + 1) if offset != 0
    }
    fixed_offset_allowed = {offset: 0 for offset in fixed_offset_total}

    for p in target_primes:
        q = next_prime(p, primes)
        y = max(2, int(math.floor(y_ratio * p)))
        low_primes = [prime for prime in primes if prime <= y]
        tail_primes = [prime for prime in primes if y < prime <= p]
        low_rough, tail_omega, tail_labels = build_tail_data(
            q=q,
            low_primes=low_primes,
            tail_primes=tail_primes,
        )

        primes_by_row: list[list[int]] = [[] for _ in range(q + 1)]
        semis = []
        for n in range(2, q * q):
            row = (n - 1) // q + 1
            if low_rough[n] and tail_omega[n] == 0 and is_prime[n]:
                primes_by_row[row].append(n)
            if not low_rough[n] or tail_omega[n] != 2:
                continue
            labels = tail_labels[n]
            if labels[0] * labels[1] == n:
                semis.append((row, n, labels))

        for row, value, labels in semis:
            row_left = (row - 1) * q + 1
            row_right = row * q
            distance = nearest_distance(value, primes_by_row[row])
            stats = offset_stats(value, row_left, row_right, radius, wheel_primes)
            total_semiprimes += 1
            if distance is not None:
                nearest_distances.append(distance)
            if stats["allowed_offsets"] == 0:
                no_allowed_count += 1
            row_left = (row - 1) * q + 1
            row_right = row * q
            for offset in fixed_offset_total:
                candidate = value + offset
                if row_left <= candidate <= row_right:
                    fixed_offset_total[offset] += 1
                    if wheel_allowed(value, offset, wheel_primes):
                        fixed_offset_allowed[offset] += 1
            if (
                distance is not None
                and stats["min_allowed_abs"] is not None
                and distance == stats["min_allowed_abs"]
            ):
                nearest_equals_wheel_min += 1
            item = {
                "p": p,
                "q": q,
                "y": y,
                "row": row,
                "n": value,
                "tail_labels": labels,
                "nearest_prime_distance": distance,
                **stats,
            }
            samples.append(item)

    worst_shadow_samples = sorted(
        samples,
        key=lambda item: (
            item["shadow_ratio"] if item["shadow_ratio"] is not None else -1,
            item["nearest_prime_distance"] or -1,
        ),
        reverse=True,
    )[:20]
    worst_nearest_samples = sorted(
        samples,
        key=lambda item: item["nearest_prime_distance"] or -1,
        reverse=True,
    )[:20]
    fixed_offset_profile = []
    for offset in sorted(fixed_offset_total, key=lambda item: (abs(item), item)):
        total = fixed_offset_total[offset]
        allowed = fixed_offset_allowed[offset]
        fixed_offset_profile.append(
            {
                "offset": offset,
                "total": total,
                "allowed": allowed,
                "empirical_allowed_ratio": allowed / total if total else None,
                "theory_allowed_ratio": fixed_shift_theory_ratio(
                    offset, wheel_primes
                ),
            }
        )

    return {
        "parameters": {
            "max_p": max_p,
            "min_p": min_p,
            "y_ratio": y_ratio,
            "radius": radius,
            "near_offset": near_offset,
            "wheel_primes": wheel_primes,
        },
        "summary": {
            "prime_record_count": len(target_primes),
            "total_balanced_semiprimes": total_semiprimes,
            "no_allowed_offset_count": no_allowed_count,
            "max_nearest_prime_distance": max(nearest_distances, default=None),
            "avg_nearest_prime_distance": (
                sum(nearest_distances) / len(nearest_distances)
                if nearest_distances
                else None
            ),
            "nearest_equals_wheel_min_count": nearest_equals_wheel_min,
            "nearest_equals_wheel_min_ratio": (
                nearest_equals_wheel_min / total_semiprimes
                if total_semiprimes
                else None
            ),
            "max_shadow_ratio": max(
                (
                    item["shadow_ratio"]
                    for item in samples
                    if item["shadow_ratio"] is not None
                ),
                default=None,
            ),
            "min_allowed_ratio": min(
                (
                    item["allowed_ratio"]
                    for item in samples
                    if item["allowed_ratio"] is not None
                ),
                default=None,
            ),
            "worst_shadow_samples": worst_shadow_samples,
            "worst_nearest_samples": worst_nearest_samples,
            "fixed_offset_profile": fixed_offset_profile,
        },
    }


def write_markdown(result: dict, path: Path) -> None:
    """写 Markdown 报告。"""
    params = result["parameters"]
    summary = result["summary"]
    lines = [
        "# 平衡双尾半素数的轮筛阴影审计",
        "",
        "**状态：** `experimental_wheel_shadow_rigidity_support_not_a_proof`",
        "",
        "## 参数",
        "",
        f"- `max_p`: `{params['max_p']}`",
        f"- `min_p`: `{params['min_p']}`",
        f"- `y_ratio`: `{params['y_ratio']}`",
        f"- `radius`: `{params['radius']}`",
        f"- `near_offset`: `{params['near_offset']}`",
        f"- `wheel_primes`: `{params['wheel_primes']}`",
        "",
        "## 总结",
        "",
        f"- 检查素数记录数：`{summary['prime_record_count']}`。",
        f"- 平衡双尾半素数总数：`{summary['total_balanced_semiprimes']}`。",
        f"- 轮筛半径内无允许偏移数：`{summary['no_allowed_offset_count']}`。",
        f"- 最近素数最大距离：`{summary['max_nearest_prime_distance']}`。",
        f"- 最近素数平均距离：`{summary['avg_nearest_prime_distance']}`。",
        f"- 最近素数距离等于轮筛最小允许距离比例：`{summary['nearest_equals_wheel_min_ratio']}`。",
        f"- 最大阴影比例：`{summary['max_shadow_ratio']}`。",
        f"- 最小允许比例：`{summary['min_allowed_ratio']}`。",
        "",
        "## 固定短偏移层锁",
        "",
        "表中理论比例是在模小素数轮 `W_z` 的单位类中，固定偏移 `d` 同时保持 `n` 与 `n+d` 均避开小素数的比例。奇偏移被模 `2` 完全锁死；偶偏移若不被 `3,5,7,...` 整除，则继续被对应素数各锁死一个相位类。",
        "",
        "| d | 样本数 | 允许数 | 实测允许比例 | 理论允许比例 |",
        "| ---: | ---: | ---: | ---: | ---: |",
    ]
    for item in summary["fixed_offset_profile"]:
        if abs(item["offset"]) > 15:
            continue
        lines.append(
            "| {offset} | {total} | {allowed} | {empirical} | {theory:.6f} |".format(
                offset=item["offset"],
                total=item["total"],
                allowed=item["allowed"],
                empirical=(
                    "NA"
                    if item["empirical_allowed_ratio"] is None
                    else f"{item['empirical_allowed_ratio']:.6f}"
                ),
                theory=item["theory_allowed_ratio"],
            )
        )
    lines.extend(
        [
            "",
            "## 最近素数距离最大样本",
            "",
            "| p | q | row | n | labels | nearest | allowed ratio | min allowed | shadow ratio |",
            "| ---: | ---: | ---: | ---: | --- | ---: | ---: | ---: | ---: |",
        ]
    )
    for item in summary["worst_nearest_samples"]:
        lines.append(
            "| {p} | {q} | {row} | {n} | {labels} | {nearest} | {allowed:.6f} | {min_allowed} | {shadow:.6f} |".format(
                p=item["p"],
                q=item["q"],
                row=item["row"],
                n=item["n"],
                labels=item["tail_labels"],
                nearest=item["nearest_prime_distance"],
                allowed=item["allowed_ratio"],
                min_allowed=item["min_allowed_abs"],
                shadow=item["shadow_ratio"],
            )
        )
    lines.extend(
        [
            "",
            "## 审稿解释",
            "",
            "若 `n` 是双粗半素数且 `n+d` 要成为素数，则对每个小素数 `r`，必须有 `d` 不落在唯一禁类 `-n mod r`。这就是轮筛阴影。它解释了为什么半素数附近的素数不能任意靠近，也给局部 Hall 配对提供了可计算的允许偏移集合。",
            "",
            "该审计显示短半径内大量偏移被轮筛锁死；若半素数仍要补洞，只能沿少数允许偏移通道寻找素数。允许通道过少或失败时，应进入 `PDEC/Tail-anchor`，而不是继续按自由随机点处理。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_wheels(raw: str) -> list[int]:
    """解析轮筛小素数列表。"""
    return [int(item) for item in raw.split(",") if item.strip()]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-p", type=int, default=1000)
    parser.add_argument("--min-p", type=int, default=17)
    parser.add_argument("--y-ratio", type=float, default=1 / math.e)
    parser.add_argument("--radius", type=int, default=160)
    parser.add_argument("--near-offset", type=int, default=30)
    parser.add_argument("--wheels", default="2,3,5,7,11,13")
    parser.add_argument(
        "--out-prefix",
        default="docs/monograph/prime-matrix-semiprime-wheel-shadow-audit",
    )
    args = parser.parse_args()
    result = audit(
        args.max_p,
        args.min_p,
        args.y_ratio,
        args.radius,
        args.near_offset,
        parse_wheels(args.wheels),
    )
    prefix = Path(args.out_prefix)
    prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, prefix.with_suffix(".md"))
    compact = {
        key: value
        for key, value in result["summary"].items()
        if key not in {"worst_shadow_samples", "worst_nearest_samples"}
    }
    print(json.dumps(compact, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
