#!/usr/bin/env python3
"""AlphaTail ThreeEdge 高尾二边同源锚点审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_threeedge_tailanchor_audit.py --selected '997:4096:-36,5003:8192:-36' --R 31 --format table
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from math import isqrt


EDGE_NAMES = ("01", "12", "02")
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


def edge_signs_from_point_signs(signs: tuple[int, int, int]) -> tuple[int, int, int]:
    """由三点符号返回三边符号。"""
    return signs[0] * signs[1], signs[1] * signs[2], signs[0] * signs[2]


def local_state(prime: int, shift: int, residue: int) -> tuple[str, tuple[int, int, int]]:
    """计算单个素数在 residue=d mod prime 上的局部三边状态。"""
    if shift % prime == 0:
        return "A", STATE_SIGNS["A"]
    if prime == 2:
        return "C", STATE_SIGNS["C"]
    class_map = {
        0: "B",
        (-shift) % prime: "C",
        (-2 * shift) % prime: "D",
    }
    state = class_map.get(residue % prime, "A")
    return state, STATE_SIGNS[state]


def multiply_edges(left: tuple[int, int, int], right: tuple[int, int, int]) -> tuple[int, int, int]:
    """坐标乘法。"""
    return tuple(a * b for a, b in zip(left, right, strict=True))


def add_vector(left: list[int], right: tuple[int, int, int]) -> None:
    """原地累加三维整数向量。"""
    for index, value in enumerate(right):
        left[index] += value


def vector_norm_square(vector: tuple[int, int, int] | list[int]) -> int:
    """返回三维向量平方范数。"""
    return sum(value * value for value in vector)


def anchor_class(value: int, shift: int, prime: int) -> str | None:
    """返回 value 在 prime 下命中的三点锚点类。"""
    residue = value % prime
    if residue == 0:
        return "0"
    if residue == (-shift) % prime:
        return "-r"
    if residue == (-2 * shift) % prime:
        return "-2r"
    return None


def audit_item(prime_bound: int, block: int, shift: int, alpha: float, low_cutoff: int) -> dict:
    """审计单个 p:B:r 的 ThreeEdge 高尾锚点。"""
    cutoff = int(alpha * prime_bound)
    domain_start = max(block + 1, block + 1 - shift, block + 1 - 2 * shift)
    domain_stop = min(2 * block, 2 * block - shift, 2 * block - 2 * shift)
    max_value = max(domain_stop, domain_stop + shift, domain_stop + 2 * shift, 0)
    primes = [prime for prime in primes_upto(max_value) if prime <= cutoff]
    low_primes = [prime for prime in primes if prime <= low_cutoff]
    tail_primes = [prime for prime in primes if prime > low_cutoff]

    chains = 0
    full_edge_sum = [0, 0, 0]
    low_edge_sum = [0, 0, 0]
    anchor_totals: dict[str, list[int]] = defaultdict(lambda: [0, 0, 0])
    point_loads: list[int] = []

    for value in range(domain_start, domain_stop + 1):
        supports = [
            squarefree_support(value, primes),
            squarefree_support(value + shift, primes),
            squarefree_support(value + 2 * shift, primes),
        ]
        if any(support is None for support in supports):
            continue
        chains += 1
        point_signs = tuple(mobius_sign(support) for support in supports if support is not None)
        full_edges = edge_signs_from_point_signs(point_signs)
        add_vector(full_edge_sum, full_edges)

        low_edges = (1, 1, 1)
        for prime in low_primes:
            _, local_edges = local_state(prime, shift, value % prime)
            low_edges = multiply_edges(low_edges, local_edges)
        add_vector(low_edge_sum, low_edges)

        prefix_edges = (1, 1, 1)
        point_load = 0
        for prime in tail_primes:
            state, local_edges = local_state(prime, shift, value % prime)
            increment = tuple(prefix_edges[index] * (local_edges[index] - 1) for index in range(3))
            if increment != (0, 0, 0):
                contribution = tuple(low_edges[index] * increment[index] for index in range(3))
                klass = anchor_class(value, shift, prime) or state
                add_vector(anchor_totals[f"{prime}:{klass}"], contribution)
                point_load += sum(abs(item) for item in contribution)
            prefix_edges = multiply_edges(prefix_edges, local_edges)
        point_loads.append(point_load)

    tail_vector = [full_edge_sum[index] - low_edge_sum[index] for index in range(3)]
    reconstructed = [0, 0, 0]
    for vector in anchor_totals.values():
        add_vector(reconstructed, tuple(vector))
    energy = sum(vector_norm_square(vector) for vector in anchor_totals.values())
    diagonal_load_bound = sum(load * load for load in point_loads)
    active = sum(1 for vector in anchor_totals.values() if any(vector))
    top = sorted(
        ((key, tuple(vector), vector_norm_square(vector)) for key, vector in anchor_totals.items()),
        key=lambda item: (-item[2], item[0]),
    )[:12]
    return {
        "p": prime_bound,
        "alpha": alpha,
        "y": cutoff,
        "block": block,
        "shift": shift,
        "R": low_cutoff,
        "domain_size": max(0, domain_stop - domain_start + 1),
        "chains": chains,
        "active_anchors": active,
        "full_edge_sum": dict(zip(EDGE_NAMES, full_edge_sum, strict=True)),
        "low_edge_sum": dict(zip(EDGE_NAMES, low_edge_sum, strict=True)),
        "tail_vector": dict(zip(EDGE_NAMES, tail_vector, strict=True)),
        "reconstructed_tail": dict(zip(EDGE_NAMES, reconstructed, strict=True)),
        "anchor_energy": energy,
        "diagonal_load_bound": diagonal_load_bound,
        "max_point_load": max(point_loads, default=0),
        "top_anchors": [
            {"anchor": key, "vector": dict(zip(EDGE_NAMES, vector, strict=True)), "norm_square": norm_square}
            for key, vector, norm_square in top
        ],
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
            "p block shift R chains active tail01 tail12 tail02 energy diag_bound max_point top_anchor top_norm",
            flush=True,
        )
        for audit in audits:
            top = audit["top_anchors"][0] if audit["top_anchors"] else {"anchor": "-", "norm_square": 0}
            tail = audit["tail_vector"]
            print(
                f"{audit['p']} {audit['block']} {audit['shift']} {audit['R']} "
                f"{audit['chains']} {audit['active_anchors']} "
                f"{tail['01']} {tail['12']} {tail['02']} "
                f"{audit['anchor_energy']} {audit['diagonal_load_bound']} {audit['max_point_load']} "
                f"{top['anchor']} {top['norm_square']}",
                flush=True,
            )
        return
    for audit in audits:
        print(audit, flush=True)


if __name__ == "__main__":
    main()
