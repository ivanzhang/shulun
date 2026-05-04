#!/usr/bin/env python3
"""AlphaTail 共振三点链三边奇偶审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_threeedge_parity_audit.py --selected '997:4096:-36,5003:8192:-36' --R 31 --format table
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from math import isqrt


STATES = ("A", "B", "C", "D")
STATE_SIGNS = {
    "A": (1, 1, 1),
    "B": (-1, 1, -1),
    "C": (-1, -1, 1),
    "D": (1, -1, -1),
}


def primes_upto(limit: int) -> list[int]:
    """返回不超过 limit 的素数。"""
    primes: list[int] = []
    for value in range(2, limit + 1):
        if all(value % divisor for divisor in range(2, isqrt(value) + 1)):
            primes.append(value)
    return primes


def squarefree_support(value: int, small_primes: list[int]) -> set[int] | None:
    """返回 y-smooth squarefree 数的素因子支撑；否则返回 None。"""
    remaining = value
    support: set[int] = set()
    for prime in small_primes:
        if prime > remaining:
            break
        if remaining % prime != 0:
            continue
        remaining //= prime
        support.add(prime)
        if remaining % prime == 0:
            return None
    if remaining != 1:
        return None
    return support


def mobius_sign(support: set[int]) -> int:
    """由平方自由支撑返回 Möbius 符号。"""
    return -1 if len(support) % 2 else 1


def edge_state_from_signs(signs: tuple[int, int, int]) -> str:
    """由三点 Möbius 符号返回三边四状态。"""
    edge_signs = (signs[0] * signs[1], signs[1] * signs[2], signs[0] * signs[2])
    for state, candidate in STATE_SIGNS.items():
        if edge_signs == candidate:
            return state
    raise ValueError(f"非法三边状态: {edge_signs}")


def compose_state(left: str, right: str) -> str:
    """按坐标相乘合成两个四状态。"""
    signs = tuple(a * b for a, b in zip(STATE_SIGNS[left], STATE_SIGNS[right], strict=True))
    for state, candidate in STATE_SIGNS.items():
        if signs == candidate:
            return state
    raise ValueError(f"非法合成状态: {signs}")


def local_state(prime: int, shift: int, residue: int) -> str:
    """计算单个素数在 residue=d mod prime 上的局部三边状态。"""
    if shift % prime == 0:
        return "A"
    if prime == 2:
        # r 为奇数时，2 的局部状态固定；r 为偶数已在上面返回 A。
        return "C"
    hits = {
        0: "B",
        (-shift) % prime: "C",
        (-2 * shift) % prime: "D",
    }
    return hits.get(residue % prime, "A")


def low_state(value: int, shift: int, low_primes: list[int]) -> str:
    """合成低模素数给出的三边状态。"""
    state = "A"
    for prime in low_primes:
        state = compose_state(state, local_state(prime, shift, value % prime))
    return state


def low_state_model(shift: int, low_primes: list[int]) -> dict[str, float]:
    """用逐素局部分布卷积计算完整 CRT residue 系上的四状态主项。"""
    distribution = {"A": 1.0, "B": 0.0, "C": 0.0, "D": 0.0}
    for prime in low_primes:
        local_counts: Counter[str] = Counter()
        for residue in range(prime):
            local_counts[local_state(prime, shift, residue)] += 1
        local_distribution = {state: local_counts[state] / prime for state in STATES}
        next_distribution = {state: 0.0 for state in STATES}
        for left_state, left_weight in distribution.items():
            for right_state, right_weight in local_distribution.items():
                next_distribution[compose_state(left_state, right_state)] += left_weight * right_weight
        distribution = next_distribution
    return distribution


def audit_item(prime_bound: int, block: int, shift: int, alpha: float, low_cutoff: int) -> dict:
    """审计单个 p:B:r 的三边奇偶状态。"""
    cutoff = int(alpha * prime_bound)
    domain_start = max(block + 1, block + 1 - shift, block + 1 - 2 * shift)
    domain_stop = min(2 * block, 2 * block - shift, 2 * block - 2 * shift)
    max_value = max(domain_stop, domain_stop + shift, domain_stop + 2 * shift, 0)
    primes = [prime for prime in primes_upto(max_value) if prime <= cutoff]
    low_primes = [prime for prime in primes if prime <= low_cutoff]
    state_counts: Counter[str] = Counter()
    low_counts: Counter[str] = Counter()
    tail_gap_counts: Counter[str] = Counter()
    edge_sums = [0, 0, 0]
    low_edge_sums = [0, 0, 0]

    for value in range(domain_start, domain_stop + 1):
        supports = [
            squarefree_support(value, primes),
            squarefree_support(value + shift, primes),
            squarefree_support(value + 2 * shift, primes),
        ]
        if any(support is None for support in supports):
            continue
        signs = tuple(mobius_sign(support) for support in supports if support is not None)
        full_state = edge_state_from_signs(signs)
        low = low_state(value, shift, low_primes)
        tail = compose_state(full_state, low)
        state_counts[full_state] += 1
        low_counts[low] += 1
        tail_gap_counts[tail] += 1
        for index, sign in enumerate(STATE_SIGNS[full_state]):
            edge_sums[index] += sign
        for index, sign in enumerate(STATE_SIGNS[low]):
            low_edge_sums[index] += sign

    chains = sum(state_counts.values())
    model = low_state_model(shift, low_primes)
    centered = {
        state: low_counts[state] - chains * model[state]
        for state in STATES
    }
    max_centered_state = max(STATES, key=lambda state: abs(centered[state]))
    return {
        "p": prime_bound,
        "alpha": alpha,
        "y": cutoff,
        "block": block,
        "shift": shift,
        "R": low_cutoff,
        "domain_size": max(0, domain_stop - domain_start + 1),
        "chains": chains,
        "state_counts": {state: state_counts[state] for state in STATES},
        "low_counts": {state: low_counts[state] for state in STATES},
        "tail_gap_counts": {state: tail_gap_counts[state] for state in STATES},
        "edge_sums": {
            "K01": edge_sums[0],
            "K12": edge_sums[1],
            "K02": edge_sums[2],
        },
        "low_edge_sums": {
            "L01": low_edge_sums[0],
            "L12": low_edge_sums[1],
            "L02": low_edge_sums[2],
        },
        "low_model": model,
        "centered": centered,
        "max_centered_state": max_centered_state,
        "max_centered_value": centered[max_centered_state],
    }


def parse_selected(raw: str) -> list[tuple[int, int, int]]:
    """解析 p:B:r 逗号列表。"""
    items: list[tuple[int, int, int]] = []
    for part in raw.split(","):
        if not part.strip():
            continue
        prime_raw, block_raw, shift_raw = part.split(":", 2)
        items.append((int(prime_raw), int(block_raw), int(shift_raw)))
    return items


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--selected", type=str, default="997:4096:-36,5003:8192:-36")
    parser.add_argument("--R", type=int, default=31)
    parser.add_argument("--alpha", type=float, default=0.9)
    parser.add_argument("--format", choices=("json", "table", "repr"), default="repr")
    args = parser.parse_args()

    audits = [
        audit_item(prime_bound, block, shift, args.alpha, args.R)
        for prime_bound, block, shift in parse_selected(args.selected)
    ]
    if args.format == "json":
        print(json.dumps(audits, ensure_ascii=False, indent=2), flush=True)
        return
    if args.format == "table":
        print(
            "p block shift R chains A B C D K01 K12 K02 lowA lowB lowC lowD max_centered_state max_centered",
            flush=True,
        )
        for audit in audits:
            counts = audit["state_counts"]
            low_counts = audit["low_counts"]
            edge_sums = audit["edge_sums"]
            print(
                f"{audit['p']} {audit['block']} {audit['shift']} {audit['R']} {audit['chains']} "
                f"{counts['A']} {counts['B']} {counts['C']} {counts['D']} "
                f"{edge_sums['K01']} {edge_sums['K12']} {edge_sums['K02']} "
                f"{low_counts['A']} {low_counts['B']} {low_counts['C']} {low_counts['D']} "
                f"{audit['max_centered_state']} {audit['max_centered_value']:.6f}",
                flush=True,
            )
        return
    for audit in audits:
        print(audit, flush=True)


if __name__ == "__main__":
    main()
