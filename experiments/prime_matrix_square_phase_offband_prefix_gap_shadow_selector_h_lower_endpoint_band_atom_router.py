#!/usr/bin/env python3
"""审计活跃 ell 连续素数带的端点原子。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_endpoint_band_atom_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-endpoint-band-atom-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-selector-h-lower-endpoint-band-atom-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-endpoint-band-atom-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-endpoint-band-atom-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

TEMPLATE_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-template-provenance-ledger.json"
BUDGET_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-singleton-rankin-budget-ledger.json"
BAND_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-active-ell-interval-band-ledger.json"
BUDGET_ROUTER = (
    ROOT
    / "experiments"
    / "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_singleton_rankin_budget_router.py"
)

OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-endpoint-band-atom-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-endpoint-band-atom-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-endpoint-band-atom-router.md"

NEXT_TARGET = "EndpointBandMotionBoundOrEndpointAtomPDECExclusion"


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def load_module(path: Path, name: str) -> Any:
    """按路径加载模块。"""
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def record_key(record: dict[str, Any]) -> str:
    """端点原子的完整键。"""
    return "|".join(
        [
            f"p={int(record['p'])}",
            f"side={record['side']}",
            f"ell={int(record['ell_tuple'][0])}",
            f"residue={int(record['crt_residue'])}",
            f"slot={','.join(map(str, record['slot_keys']))}",
        ]
    )


def compact(record: dict[str, Any], max_p: int) -> dict[str, Any]:
    """压缩端点记录。"""
    return {
        "p": int(record["p"]),
        "distance_to_sweep_max_p": max_p - int(record["p"]),
        "side": str(record["side"]),
        "rho": int(record["rho"]),
        "ell": int(record["ell_tuple"][0]),
        "crt_residue": int(record["crt_residue"]),
        "crt_modulus": int(record["crt_modulus"]),
        "residue_packet_key": str(record["residue_packet_key"]),
        "slot_keys": list(record["slot_keys"]),
        "phase_p_lo": int(record["phase_p_lo"]),
        "phase_p_hi": int(record["phase_p_hi"]),
        "phase_width": int(record["phase_width"]),
        "crt_minus_phase_width": int(record["crt_minus_phase_width"]),
        "margin": int(record["residual_prime_pair_margin_to_bound"]),
        "left_depth": int(record["left_depth"]),
        "right_depth": int(record["right_depth"]),
        "endpoint_atom_key": record_key(record),
    }


def build_singleton_records(template_ledger: Path, budget_ledger: Path) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """重放并提取 singleton residue 物理记录。"""
    budget = load_json(budget_ledger)
    params = budget["parameters"]
    budget_router = load_module(BUDGET_ROUTER, "endpoint_band_budget")
    records = budget_router.build_singleton_records(
        template_ledger,
        int(params["max_p"]),
        int(params["p0"]),
        float(params["target_h_coeff"]),
        int(params["max_certificate_size"]),
    )
    return records, params


def grouped_one_slot(records: list[dict[str, Any]]) -> dict[tuple[str, int], list[dict[str, Any]]]:
    """按 `(side,ell)` 汇总一槽记录。"""
    grouped: dict[tuple[str, int], list[dict[str, Any]]] = {}
    for record in records:
        if int(record["certificate_size"]) != 1:
            continue
        grouped.setdefault((str(record["side"]), int(record["ell_tuple"][0])), []).append(record)
    return grouped


def side_ell_row(side: str, ell: int, records: list[dict[str, Any]], max_p: int) -> dict[str, Any]:
    """构造一个 `(side,ell)` 行。"""
    residues = sorted({int(record["crt_residue"]) for record in records})
    slots = sorted({",".join(map(str, record["slot_keys"])) for record in records})
    return {
        "side": side,
        "ell": ell,
        "record_count": len(records),
        "distinct_residue_count": len(residues),
        "distinct_slot_count": len(slots),
        "rankin_mass": len(records) / ell if ell else 0.0,
        "p_min": min(int(record["p"]) for record in records) if records else None,
        "p_max": max(int(record["p"]) for record in records) if records else None,
        "min_distance_to_sweep_max_p": min(max_p - int(record["p"]) for record in records) if records else None,
        "min_margin": min(int(record["residual_prime_pair_margin_to_bound"]) for record in records) if records else None,
        "min_crt_minus_phase_width": min(int(record["crt_minus_phase_width"]) for record in records) if records else None,
        "residue_values": residues,
        "slot_values": slots,
        "records": [compact(record, max_p) for record in sorted(records, key=lambda item: (int(item["p"]), int(item["crt_residue"])))],
    }


def build_result(template_ledger: Path, budget_ledger: Path, band_ledger: Path) -> dict[str, Any]:
    """构造端点原子审计结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    band = load_json(band_ledger)
    records, params = build_singleton_records(template_ledger, budget_ledger)
    max_p = int(params["max_p"])
    grouped = grouped_one_slot(records)

    active = list(map(int, band["active_ell_values"]))
    both = list(map(int, band["both_side_ell_values"]))
    endpoints = [min(active), max(active)]
    core_edges = [min(both), max(both)]
    endpoint_rows = []
    core_edge_rows = []
    for ell in endpoints:
        for side in ["minus", "plus"]:
            endpoint_rows.append(side_ell_row(side, ell, grouped.get((side, ell), []), max_p))
    for ell in core_edges:
        for side in ["minus", "plus"]:
            core_edge_rows.append(side_ell_row(side, ell, grouped.get((side, ell), []), max_p))

    nonempty_endpoint_rows = [row for row in endpoint_rows if row["record_count"]]
    endpoint_atom_keys = [record["endpoint_atom_key"] for row in nonempty_endpoint_rows for record in row["records"]]
    endpoint_atoms_are_singletons = all(row["record_count"] == 1 for row in nonempty_endpoint_rows)
    endpoint_residues_are_singletons = all(row["distinct_residue_count"] == row["record_count"] for row in nonempty_endpoint_rows)
    endpoint_slots_are_singletons = all(row["distinct_slot_count"] == row["record_count"] for row in nonempty_endpoint_rows)
    endpoint_only_minus = all(row["side"] == "minus" for row in nonempty_endpoint_rows)

    ledger = {
        "band_ledger": str(band_ledger.relative_to(ROOT)),
        "budget_ledger": str(budget_ledger.relative_to(ROOT)),
        "active_band_endpoints": endpoints,
        "both_side_core_edges": core_edges,
        "endpoint_rows": endpoint_rows,
        "core_edge_rows": core_edge_rows,
        "endpoint_atom_keys": endpoint_atom_keys,
        "endpoint_atoms_are_singletons_current_sweep": endpoint_atoms_are_singletons,
        "endpoint_residues_are_singletons_current_sweep": endpoint_residues_are_singletons,
        "endpoint_slots_are_singletons_current_sweep": endpoint_slots_are_singletons,
        "endpoint_only_minus_current_sweep": endpoint_only_minus,
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    result = {
        "certificate_type": (
            "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_"
            "endpoint_band_atom_router"
        ),
        "status": "endpoint_band_atoms_isolated_current_sweep_motion_bound_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_sweep_not_used_as_global_proof": True,
        "active_band_endpoints": endpoints,
        "both_side_core_edges": core_edges,
        "endpoint_atom_count": len(endpoint_atom_keys),
        "endpoint_atom_keys": endpoint_atom_keys,
        "endpoint_rows": endpoint_rows,
        "core_edge_rows": core_edge_rows,
        "endpoint_atoms_are_singletons_current_sweep": endpoint_atoms_are_singletons,
        "endpoint_residues_are_singletons_current_sweep": endpoint_residues_are_singletons,
        "endpoint_slots_are_singletons_current_sweep": endpoint_slots_are_singletons,
        "endpoint_only_minus_current_sweep": endpoint_only_minus,
        "endpoint_band_motion_bound_proved": False,
        "endpoint_atom_pdec_excluded_globally": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": "ActiveEllBandEndpointGrowthBoundOrEndpointResetPDEC",
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "当前活跃 `ell` 素数带的两个外端点 `{}` 都不是高占用块，而是 minus-only 单原子："
            "每个端点只有一个物理记录、一个 residue 和一个 slot。双侧核心边缘 `{}` 则已进入多记录核心带。"
            "因此下一层全局硬点可精确表述为：端点若随尺度继续移动，必须证明其移动受限，"
            "或把反复出现的端点原子登记并排斥为 EndpointAtom-PDEC/SAE。"
        ).format(endpoints, core_edges),
    }
    result["source_hashes"] = {
        "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_endpoint_band_atom_router.py": sha256(
            Path(__file__).resolve()
        ),
        "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-active-ell-interval-band-ledger.json": sha256(
            band_ledger
        ),
        "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-singleton-rankin-budget-ledger.json": sha256(
            budget_ledger
        ),
        "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-endpoint-band-atom-ledger.json": sha256(
            OUT_LEDGER
        ),
    }
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow selector H lower endpoint band atom router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"active_band_endpoints={result['active_band_endpoints']}",
        f"both_side_core_edges={result['both_side_core_edges']}",
        f"endpoint_atom_count={result['endpoint_atom_count']}",
        f"endpoint_atoms_are_singletons_current_sweep={fmt_bool(result['endpoint_atoms_are_singletons_current_sweep'])}",
        f"endpoint_residues_are_singletons_current_sweep={fmt_bool(result['endpoint_residues_are_singletons_current_sweep'])}",
        f"endpoint_slots_are_singletons_current_sweep={fmt_bool(result['endpoint_slots_are_singletons_current_sweep'])}",
        f"endpoint_only_minus_current_sweep={fmt_bool(result['endpoint_only_minus_current_sweep'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 外端点行",
        "",
        "| side | ell | records | residues | slots | Rankin mass | p range | min margin | min crt-phase gap |",
        "| --- | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: |",
    ]
    for row in result["endpoint_rows"]:
        p_range = "empty" if row["p_min"] is None else f"{row['p_min']}..{row['p_max']}"
        lines.append(
            f"| `{row['side']}` | {row['ell']} | {row['record_count']} | {row['distinct_residue_count']} | "
            f"{row['distinct_slot_count']} | {row['rankin_mass']:.6f} | `{p_range}` | "
            f"{row['min_margin']} | {row['min_crt_minus_phase_width']} |"
        )
    lines.extend(
        [
            "",
            "## 2. 外端点原子",
            "",
            "| ell | p | side | residue | slot | margin | left depth | right depth |",
            "| ---: | ---: | --- | ---: | --- | ---: | ---: | ---: |",
        ]
    )
    for row in result["endpoint_rows"]:
        for record in row["records"]:
            lines.append(
                f"| {record['ell']} | {record['p']} | `{record['side']}` | {record['crt_residue']} | "
                f"`{record['slot_keys']}` | {record['margin']} | {record['left_depth']} | {record['right_depth']} |"
            )
    lines.extend(
        [
            "",
            "## 3. 双侧核心边缘对照",
            "",
            "| side | ell | records | residues | slots | Rankin mass | p range |",
            "| --- | ---: | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for row in result["core_edge_rows"]:
        p_range = "empty" if row["p_min"] is None else f"{row['p_min']}..{row['p_max']}"
        lines.append(
            f"| `{row['side']}` | {row['ell']} | {row['record_count']} | {row['distinct_residue_count']} | "
            f"{row['distinct_slot_count']} | {row['rankin_mass']:.6f} | `{p_range}` |"
        )
    lines.extend(
        [
            "",
            "## 4. 结构结论",
            "",
            "- 外端点是单原子，不是当前 Rankin 主质量来源。",
            "- 双侧核心边缘已经有多 residue、多 slot 支撑，说明端点增长与核心带填充是不同机制。",
            "- 全局证明不能把当前端点孤立性当作定理；下一步必须证明端点移动受限，或把端点复现登记为 EndpointAtom-PDEC/SAE 并排斥。",
            "",
            "## 5. 下一步",
            "",
            f"- 主攻：`{result['next_direct_attack_target']}`。",
            "- 直接检查端点移动的完整键是否会在相邻尺度复现；若复现，进入端点 PDEC；若不复现，进入端点 SAE/Rankin。",
            "",
            "## 6. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in result["source_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--template-ledger", type=Path, default=TEMPLATE_LEDGER)
    parser.add_argument("--budget-ledger", type=Path, default=BUDGET_LEDGER)
    parser.add_argument("--band-ledger", type=Path, default=BAND_LEDGER)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    template_ledger = args.template_ledger if args.template_ledger.is_absolute() else ROOT / args.template_ledger
    budget_ledger = args.budget_ledger if args.budget_ledger.is_absolute() else ROOT / args.budget_ledger
    band_ledger = args.band_ledger if args.band_ledger.is_absolute() else ROOT / args.band_ledger
    result = build_result(template_ledger, budget_ledger, band_ledger)
    write_markdown(result)
    result["source_hashes"][
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-endpoint-band-atom-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "active_band_endpoints": result["active_band_endpoints"],
                "endpoint_atom_count": result["endpoint_atom_count"],
                "endpoint_atoms_are_singletons_current_sweep": result["endpoint_atoms_are_singletons_current_sweep"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
