#!/usr/bin/env python3
"""D4/R5 固定成员关系层泛函导数根证书原型。

用法示例：
  python3 experiments/d4_r5_fixed_membership_functional_roots.py \
    --x 1088475 --cell-left 1088475 --cell-right 1088476 \
    --H 80 --hi 400 --q 0.958 --threshold-tau 60 \
    --json docs/d4-r5-fixed-membership-roots-x1088475.json

说明：
  先在整数行 x 固定 light/short/transition/exceptional 的 a-成员集合，
  然后在给定连续 cell 内把 U,V,L,E2,potential 视为这些固定成员 contract
  函数的组合，生成导数根隔离证书。该脚本是从 block-contract 根证书
  升级到 layer-functional 根证书的第一步。
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import d4_r5_layer_functional_certificate as layer_cert  # noqa: E402
import d4_r5_phasecell_root_certificate as root_cert  # noqa: E402
from d4_lowblock_phase_capacity import offset_stats, term_rows  # noqa: E402


def row_membership_sets(x: int, hi: int, q: float, threshold_tau: int, H: int, tau: list[int], prefix: list[int]) -> dict:
    """在整数行 x 固定各层偏移团成员关系。"""
    rows = term_rows(x, hi, q, tau, prefix)
    offsets = offset_stats(x, rows)
    light, transition, short_chain = layer_cert.classify_offsets(offsets, threshold_tau)

    def groups(items: list[dict]) -> list[dict]:
        return [
            {
                "offset": item["offset"],
                "a_values": sorted(item.get("a_values", [])),
                "tau_sum": item["tau_sum"],
                "count": item["count"],
                "base_B": item["positive_contract_sum"],
            }
            for item in items
        ]

    prefix_light = [item for item in light if item["offset"] <= H]
    tail_light = [item for item in light if item["offset"] > H]
    exceptional = light + transition + short_chain
    return {
        "x": x,
        "U": groups(prefix_light),
        "V": groups(tail_light),
        "light_L": groups(light),
        "short_L": groups(short_chain),
        "transition_L": groups(transition),
        "L": groups(exceptional),
        "offset_counts": {
            "light": len(light),
            "prefix_light": len(prefix_light),
            "tail_light": len(tail_light),
            "transition": len(transition),
            "short_chain": len(short_chain),
        },
    }


def term_coeffs_for_a(x: float, a: int, tau: list[int], prefix: list[int]) -> tuple[float, ...]:
    """单个 a 的 c/old 线性-log 系数。"""
    return root_cert.block_constants_on_interval(x, a, a, tau, prefix)


def term_values(x: float, a: int, q: float, tau: list[int], prefix: list[int]) -> tuple[float, float, float]:
    """返回 B_a, B'_a, B''_a 符号核心值。"""
    coeffs = term_coeffs_for_a(x, a, tau, prefix)
    if coeffs is None:
        return 0.0, 0.0, 0.0
    value = root_cert.contract_value(x, coeffs, q)
    first = root_cert.fprime_value(x, coeffs, q)
    # 真实 B'' = x^-11/4 * core，x>0，符号和大小均可直接用该表达恢复。
    second = (x ** -2.75) * root_cert.fdouble_core_value(x, coeffs, q)
    return value, first, second


def group_values(x: float, group: dict, q: float, tau: list[int], prefix: list[int]) -> tuple[float, float, float]:
    """返回一个固定偏移团 B_h 及其一、二阶导数。"""
    vals = [term_values(x, a, q, tau, prefix) for a in group["a_values"]]
    return (sum(v[0] for v in vals), sum(v[1] for v in vals), sum(v[2] for v in vals))


def functional_values(x: float, groups: list[dict], q: float, tau: list[int], prefix: list[int]) -> dict:
    """固定偏移团集合上的 L,E2 及导数。"""
    terms = [group_values(x, group, q, tau, prefix) for group in groups]
    values = [item[0] for item in terms]
    firsts = [item[1] for item in terms]
    seconds = [item[2] for item in terms]
    L = sum(values)
    L1 = sum(firsts)
    L2 = sum(seconds)
    E2 = sum(value * value for value in values)
    E2_1 = 2 * sum(value * first for value, first in zip(values, firsts))
    E2_2 = 2 * sum(first * first + value * second for value, first, second in zip(values, firsts, seconds))
    potential = E2 - L * L / 20.0
    potential_1 = E2_1 - L * L1 / 10.0
    potential_2 = E2_2 - (L1 * L1 + L * L2) / 10.0
    return {
        "L": L,
        "L_prime": L1,
        "L_double": L2,
        "E2": E2,
        "E2_prime": E2_1,
        "E2_double": E2_2,
        "potential": potential,
        "potential_prime": potential_1,
        "potential_double": potential_2,
    }


def derivative_value(kind: str, x: float, memberships: dict, q: float, tau: list[int], prefix: list[int]) -> float:
    """层泛函的一阶导数。"""
    if kind in {"U", "V", "light_L", "L"}:
        return functional_values(x, memberships[kind], q, tau, prefix)["L_prime"]
    if kind == "E2":
        return functional_values(x, memberships["L"], q, tau, prefix)["E2_prime"]
    if kind == "potential":
        return functional_values(x, memberships["L"], q, tau, prefix)["potential_prime"]
    raise ValueError(kind)


def second_value(kind: str, x: float, memberships: dict, q: float, tau: list[int], prefix: list[int]) -> float:
    """层泛函的二阶导数。"""
    if kind in {"U", "V", "light_L", "L"}:
        return functional_values(x, memberships[kind], q, tau, prefix)["L_double"]
    if kind == "E2":
        return functional_values(x, memberships["L"], q, tau, prefix)["E2_double"]
    if kind == "potential":
        return functional_values(x, memberships["L"], q, tau, prefix)["potential_double"]
    raise ValueError(kind)


def bisection_root(kind: str, left: float, right: float, memberships: dict, q: float, tau: list[int], prefix: list[int]) -> dict:
    """用二分法隔离一个导数变号根。"""
    low = left
    high = right
    flow = derivative_value(kind, low, memberships, q, tau, prefix)
    fhigh = derivative_value(kind, high, memberships, q, tau, prefix)
    for _ in range(70):
        mid = (low + high) / 2
        fmid = derivative_value(kind, mid, memberships, q, tau, prefix)
        if flow * fmid <= 0:
            high = mid
            fhigh = fmid
        else:
            low = mid
            flow = fmid
    return {"interval": [low, high], "fprime_endpoints": [flow, fhigh], "method": "layer-functional bisection sign-change"}


def second_sign_enclosure(kind: str, l: float, r: float, memberships: dict, q: float, tau: list[int], prefix: list[int]) -> dict:
    """用细分差分给出二阶导符号包络。

    这是无第三方区间库环境下的保守证书原型：在五点上采样 F''，
    再用相邻采样变化最大值作为局部振荡余量。严格版应替换为外向舍入区间算术。
    """
    points = [l + (r - l) * i / 4 for i in range(5)]
    values = [second_value(kind, t, memberships, q, tau, prefix) for t in points]
    local_variation = max(abs(values[i + 1] - values[i]) for i in range(4)) if len(values) > 1 else 0.0
    lower = min(values) - local_variation
    upper = max(values) + local_variation
    return {
        "method": "five-point sampled F'' with local-variation enclosure",
        "sample_points": points,
        "sample_values": values,
        "local_variation_margin": local_variation,
        "enclosure": [lower, upper],
        "sign_certified": lower > 0.0 or upper < 0.0,
    }


def certify_kind(kind: str, left: float, right: float, memberships: dict, q: float, tau: list[int], prefix: list[int], samples: int) -> dict:
    """对一个层泛函生成根/无根证书。"""
    points = [left + (right - left) * i / samples for i in range(samples + 1)]
    no_root = []
    root_boxes = []
    unresolved = []
    for a, b in zip(points, points[1:]):
        eps = max(1e-10, (b - a) * 1e-6)
        l = a + eps
        r = b - eps
        if r <= l:
            continue
        fl = derivative_value(kind, l, memberships, q, tau, prefix)
        fr = derivative_value(kind, r, memberships, q, tau, prefix)
        if fl == 0.0 or fr == 0.0 or fl * fr < 0:
            root_boxes.append(bisection_root(kind, l, r, memberships, q, tau, prefix))
            continue
        enclosure = second_sign_enclosure(kind, l, r, memberships, q, tau, prefix)
        if enclosure["sign_certified"]:
            no_root.append(
                {
                    "interval": [l, r],
                    "method": "same-sign endpoints plus enclosed F'' sign",
                    "fprime_endpoints": [fl, fr],
                    "fdouble_enclosure": enclosure,
                }
            )
        else:
            unresolved.append(
                {
                    "interval": [l, r],
                    "reason": "F' endpoints same sign but F'' enclosure contains zero",
                    "fprime_endpoints": [fl, fr],
                    "fdouble_enclosure": enclosure,
                }
            )
    candidate_points = [left, right] + [sum(box["interval"]) / 2 for box in root_boxes]
    value_key = "potential" if kind == "potential" else ("E2" if kind == "E2" else "L")
    values = []
    for point in candidate_points:
        source_set = memberships["L"] if kind in {"E2", "potential"} else memberships[kind]
        values.append({"x": point, "value": functional_values(point, source_set, q, tau, prefix)[value_key]})
    return {
        "functional": kind,
        "cell": [left, right],
        "group_count": len(memberships["L"] if kind in {"E2", "potential"} else memberships[kind]),
        "sample_subintervals": samples,
        "no_root_count": len(no_root),
        "root_box_count": len(root_boxes),
        "unresolved_count": len(unresolved),
        "candidate_values": values,
        "no_root_subintervals": no_root[:100],
        "root_boxes": root_boxes[:100],
        "unresolved": unresolved[:100],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--x", type=int, default=1_088_475)
    parser.add_argument("--cell-left", type=float, default=1_088_475.0)
    parser.add_argument("--cell-right", type=float, default=1_088_476.0)
    parser.add_argument("--H", type=int, default=80)
    parser.add_argument("--hi", type=int, default=400)
    parser.add_argument("--q", type=float, default=0.958)
    parser.add_argument("--threshold-tau", type=int, default=60)
    parser.add_argument("--functionals", default="U,V,light_L,L,E2,potential")
    parser.add_argument("--samples", type=int, default=32)
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()

    tau, prefix = layer_cert.build(2 * int(math.ceil(args.cell_right)) + 10)
    memberships = row_membership_sets(args.x, args.hi, args.q, args.threshold_tau, args.H, tau, prefix)
    certificates = [
        certify_kind(kind.strip(), args.cell_left, args.cell_right, memberships, args.q, tau, prefix, args.samples)
        for kind in args.functionals.split(",")
        if kind.strip()
    ]
    payload = {
        "certificate_type": "D4-R5-fixed-membership-layer-functional-root-certificate",
        "status": "prototype: freezes integer-row membership; next step is exact membership-cell boundary generation",
        "x": args.x,
        "cell": [args.cell_left, args.cell_right],
        "H": args.H,
        "hi": args.hi,
        "q": args.q,
        "threshold_tau": args.threshold_tau,
        "membership_group_counts": {key: len(value) for key, value in memberships.items() if isinstance(value, list)},
        "offset_counts": memberships["offset_counts"],
        "certificates": certificates,
        "all_functional_root_ledgers_ok": all(cert["unresolved_count"] == 0 for cert in certificates),
        "total_root_boxes": sum(cert["root_box_count"] for cert in certificates),
        "total_unresolved": sum(cert["unresolved_count"] for cert in certificates),
        "remaining_hard_point": "replace frozen integer-row membership by exact fixed-membership cells with rational boundaries and interval arithmetic",
    }
    print(
        json.dumps(
            {
                "certificate_type": payload["certificate_type"],
                "all_functional_root_ledgers_ok": payload["all_functional_root_ledgers_ok"],
                "membership_group_counts": payload["membership_group_counts"],
                "total_root_boxes": payload["total_root_boxes"],
                "total_unresolved": payload["total_unresolved"],
                "remaining_hard_point": payload["remaining_hard_point"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
