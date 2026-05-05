#!/usr/bin/env python3
"""AlphaTail C13 活跃 AP 类模板上界合同审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_c13_active_class_template_bound_contract.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --finite-p-cut 1000 --eta 0.04 --format table
"""

from __future__ import annotations

import argparse
import json
from collections import Counter

from prime_matrix_alpha_tail_pair_crtdefect_audit import parse_selected
from prime_matrix_alpha_tail_tailpair_c13_ap_singleton_structural_contract import (
    active_ap_classes,
)
from prime_matrix_alpha_tail_tailpair_c13_low_deletion_allowance_contract import (
    low_deletion_allowance_package,
)
from prime_matrix_alpha_tail_tailpair_endpoint_persistence_audit import parse_m_values


def ratio(numerator: float, denominator: float) -> float | None:
    """返回安全比值。"""
    if denominator == 0:
        return None
    return numerator / denominator


def fmt(value: float | None) -> str:
    """格式化可空浮点。"""
    return "NA" if value is None else f"{value:.6f}"


def class_key(row: dict) -> tuple[int, int, int, int, int, int, int, int]:
    """返回完整 AP 类键。"""
    return (
        row["m"],
        row["ell"],
        row["j"],
        row["residue"],
        row["gap"],
        row["u"],
        row["j1"],
        row["j2"],
    )


def skeleton_key(row: dict) -> tuple[int, int, int, int, int, int, int]:
    """返回去掉低素 ell 的模板骨架键。"""
    return (
        row["m"],
        row["j"],
        row["residue"],
        row["gap"],
        row["u"],
        row["j1"],
        row["j2"],
    )


def source_key(row: dict) -> tuple[int, int, int, int, int, int]:
    """返回去掉 residue 与 ell 的几何源键。"""
    return (
        row["m"],
        row["j"],
        row["gap"],
        row["u"],
        row["j1"],
        row["j2"],
    )


def summarize_active_rows(rows: list[dict], allowed_deletion: float, geometric_upper: float, num_primes: int) -> dict:
    """把活跃 AP 行压缩为模板上界账本。"""
    class_representatives = {}
    q_per_class = Counter()
    for row in rows:
        key = class_key(row)
        class_representatives[key] = row
        q_per_class[key] += 1
    classes = list(class_representatives.values())
    skeleton_loads = Counter(skeleton_key(row) for row in classes)
    source_loads = Counter(source_key(row) for row in classes)
    active_classes = len(classes)
    skeleton_templates = len(skeleton_loads)
    source_templates = len(source_loads)
    template_ceiling = num_primes * skeleton_templates
    skeleton_budget = ratio(allowed_deletion, num_primes)
    return {
        "active_rows": len(rows),
        "active_classes": active_classes,
        "skeleton_templates": skeleton_templates,
        "source_templates": source_templates,
        "template_ceiling": template_ceiling,
        "allowed_deletion": allowed_deletion,
        "active_margin": allowed_deletion - active_classes,
        "template_margin": allowed_deletion - template_ceiling,
        "skeleton_budget": skeleton_budget,
        "skeleton_margin": None if skeleton_budget is None else skeleton_budget - skeleton_templates,
        "active_density_geom": ratio(active_classes, geometric_upper),
        "template_density_geom": ratio(template_ceiling, geometric_upper),
        "allowed_density_geom": ratio(allowed_deletion, geometric_upper),
        "all_u23": all(row["u"] in (2, 3) for row in rows),
        "all_q_lift1": all(row["q_lift"] == 1 for row in rows),
        "all_q_lt_2ell": all(row["q_lt_2ell"] for row in rows),
        "singleton_identity": active_classes == len(rows) and max(q_per_class.values(), default=0) <= 1,
        "max_q_per_class": max(q_per_class.values(), default=0),
        "max_classes_per_skeleton": max(skeleton_loads.values(), default=0),
        "max_classes_per_source": max(source_loads.values(), default=0),
        "active_class_pay": active_classes <= allowed_deletion,
        "template_pay": template_ceiling <= allowed_deletion,
        "u_hist": dict(sorted(Counter(row["u"] for row in classes).items())),
        "skeleton_load_hist": dict(sorted(Counter(skeleton_loads.values()).items())),
        "source_load_hist": dict(sorted(Counter(source_loads.values()).items())),
        "top_skeletons": [
            {
                "m": key[0],
                "j": key[1],
                "residue": key[2],
                "gap": key[3],
                "u": key[4],
                "j1": key[5],
                "j2": key[6],
                "classes": count,
            }
            for key, count in skeleton_loads.most_common(8)
        ],
    }


def by_window(rows: list[dict]) -> dict[tuple[int, int, int], dict]:
    """按窗口键索引。"""
    return {(row["p"], row["block"], row["shift"]): row for row in rows}


def active_class_template_bound_package(
    selected: str,
    m_values: list[int],
    finite_p_cut: int,
    eta: float,
    alpha: float,
    num_primes: int,
    endpoint_band_theta: float,
) -> dict:
    """返回活跃 AP 类模板上界合同包。"""
    allowance = low_deletion_allowance_package(
        selected,
        m_values,
        finite_p_cut,
        eta,
        alpha,
        num_primes,
        endpoint_band_theta,
    )
    allowance_by_window = by_window(allowance["windows"])
    windows = []
    layers = []
    for prime_bound, block, shift in parse_selected(selected):
        if prime_bound <= finite_p_cut:
            continue
        window_rows = []
        for point_count in m_values:
            rows = active_ap_classes(prime_bound, block, shift, point_count, alpha, num_primes)
            layer_allowance = next(
                row
                for row in allowance["rows"]
                if (row["p"], row["block"], row["shift"], row["m"])
                == (prime_bound, block, shift, point_count)
            )
            layer = {
                "p": prime_bound,
                "block": block,
                "shift": shift,
                "m": point_count,
                **summarize_active_rows(
                    rows,
                    layer_allowance["allowed_deletion"],
                    layer_allowance["geometric_upper"],
                    num_primes,
                ),
            }
            layers.append(layer)
            window_rows.extend(rows)
        window_allowance = allowance_by_window[(prime_bound, block, shift)]
        windows.append(
            {
                "p": prime_bound,
                "block": block,
                "shift": shift,
                **summarize_active_rows(
                    window_rows,
                    window_allowance["allowed_deletion"],
                    window_allowance["geometric_upper"],
                    num_primes,
                ),
            }
        )
    total_allowed = sum(row["allowed_deletion"] for row in windows)
    total_geometric = sum(row["geometric_upper"] for row in allowance["windows"])
    total = {
        "windows": len(windows),
        "active_classes": sum(row["active_classes"] for row in windows),
        "skeleton_templates": sum(row["skeleton_templates"] for row in windows),
        "source_templates": sum(row["source_templates"] for row in windows),
        "template_ceiling": sum(row["template_ceiling"] for row in windows),
        "allowed_deletion": total_allowed,
        "active_margin": total_allowed - sum(row["active_classes"] for row in windows),
        "template_margin": total_allowed - sum(row["template_ceiling"] for row in windows),
        "skeleton_budget": ratio(total_allowed, num_primes),
        "skeleton_margin": ratio(total_allowed, num_primes) - sum(row["skeleton_templates"] for row in windows)
        if num_primes
        else None,
        "active_density_geom": ratio(sum(row["active_classes"] for row in windows), total_geometric),
        "template_density_geom": ratio(sum(row["template_ceiling"] for row in windows), total_geometric),
        "allowed_density_geom": ratio(total_allowed, total_geometric),
        "all_u23": all(row["all_u23"] for row in windows),
        "all_q_lift1": all(row["all_q_lift1"] for row in windows),
        "all_q_lt_2ell": all(row["all_q_lt_2ell"] for row in windows),
        "all_singleton_identity": all(row["singleton_identity"] for row in windows),
        "all_active_class_pay": all(row["active_class_pay"] for row in windows),
        "all_template_pay": all(row["template_pay"] for row in windows),
        "min_template_margin": min((row["template_margin"] for row in windows), default=None),
        "min_skeleton_margin": min((row["skeleton_margin"] for row in windows), default=None),
        "max_classes_per_skeleton": max((row["max_classes_per_skeleton"] for row in windows), default=0),
        "max_classes_per_source": max((row["max_classes_per_source"] for row in windows), default=0),
    }
    return {
        "selected": selected,
        "m_values": m_values,
        "finite_p_cut": finite_p_cut,
        "eta": eta,
        "alpha": alpha,
        "num_primes": num_primes,
        "endpoint_band_theta": endpoint_band_theta,
        "status": "active_class_template_bound_sample_closed_global_open",
        "total": total,
        "windows": windows,
        "layers": layers,
        "allowance": allowance,
    }


def print_table(package: dict) -> None:
    """输出活跃 AP 类模板上界合同表。"""
    total = package["total"]
    print(
        "scope windows active skeleton source template_ceiling allowed active_margin "
        "template_margin skeleton_budget skeleton_margin active_dens template_dens "
        "allowed_dens u23 lift1 q_lt_2ell singleton active_pay template_pay max_skel max_source",
        flush=True,
    )
    print(
        f"highP-total {total['windows']} {total['active_classes']} "
        f"{total['skeleton_templates']} {total['source_templates']} "
        f"{total['template_ceiling']} {total['allowed_deletion']:.6f} "
        f"{total['active_margin']:.6f} {total['template_margin']:.6f} "
        f"{fmt(total['skeleton_budget'])} {fmt(total['skeleton_margin'])} "
        f"{fmt(total['active_density_geom'])} {fmt(total['template_density_geom'])} "
        f"{fmt(total['allowed_density_geom'])} {total['all_u23']} "
        f"{total['all_q_lift1']} {total['all_q_lt_2ell']} "
        f"{total['all_singleton_identity']} {total['all_active_class_pay']} "
        f"{total['all_template_pay']} {total['max_classes_per_skeleton']} "
        f"{total['max_classes_per_source']}",
        flush=True,
    )
    print(
        "p block shift active skeleton source template_ceiling allowed active_margin "
        "template_margin skeleton_budget skeleton_margin active_dens template_dens "
        "allowed_dens u23 lift1 q_lt_2ell singleton active_pay template_pay max_skel max_source",
        flush=True,
    )
    for row in package["windows"]:
        print(
            f"{row['p']} {row['block']} {row['shift']} {row['active_classes']} "
            f"{row['skeleton_templates']} {row['source_templates']} "
            f"{row['template_ceiling']} {row['allowed_deletion']:.6f} "
            f"{row['active_margin']:.6f} {row['template_margin']:.6f} "
            f"{fmt(row['skeleton_budget'])} {fmt(row['skeleton_margin'])} "
            f"{fmt(row['active_density_geom'])} {fmt(row['template_density_geom'])} "
            f"{fmt(row['allowed_density_geom'])} {row['all_u23']} "
            f"{row['all_q_lift1']} {row['all_q_lt_2ell']} "
            f"{row['singleton_identity']} {row['active_class_pay']} "
            f"{row['template_pay']} {row['max_classes_per_skeleton']} "
            f"{row['max_classes_per_source']}",
            flush=True,
        )
    print(
        "p block shift m active skeleton source template_ceiling allowed active_margin "
        "template_margin skeleton_budget skeleton_margin u23 lift1 q_lt_2ell "
        "singleton active_pay template_pay u_hist skeleton_load_hist source_load_hist",
        flush=True,
    )
    for row in package["layers"]:
        print(
            f"{row['p']} {row['block']} {row['shift']} {row['m']} "
            f"{row['active_classes']} {row['skeleton_templates']} "
            f"{row['source_templates']} {row['template_ceiling']} "
            f"{row['allowed_deletion']:.6f} {row['active_margin']:.6f} "
            f"{row['template_margin']:.6f} {fmt(row['skeleton_budget'])} "
            f"{fmt(row['skeleton_margin'])} {row['all_u23']} "
            f"{row['all_q_lift1']} {row['all_q_lt_2ell']} "
            f"{row['singleton_identity']} {row['active_class_pay']} "
            f"{row['template_pay']} {row['u_hist']} {row['skeleton_load_hist']} "
            f"{row['source_load_hist']}",
            flush=True,
        )


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--selected", type=str, default="997:4096:-36,5003:8192:-36")
    parser.add_argument("--m-values", type=str, default="4,5")
    parser.add_argument("--finite-p-cut", type=int, default=1000)
    parser.add_argument("--eta", type=float, default=0.04)
    parser.add_argument("--alpha", type=float, default=0.9)
    parser.add_argument("--num-primes", type=int, default=8)
    parser.add_argument("--endpoint-band-theta", type=float, default=0.1)
    parser.add_argument("--format", choices=("json", "table", "repr"), default="repr")
    args = parser.parse_args()

    package = active_class_template_bound_package(
        args.selected,
        parse_m_values(args.m_values),
        args.finite_p_cut,
        args.eta,
        args.alpha,
        args.num_primes,
        args.endpoint_band_theta,
    )
    if args.format == "json":
        print(json.dumps(package, ensure_ascii=False, indent=2), flush=True)
        return
    if args.format == "table":
        print_table(package)
        return
    print(package, flush=True)


if __name__ == "__main__":
    main()
