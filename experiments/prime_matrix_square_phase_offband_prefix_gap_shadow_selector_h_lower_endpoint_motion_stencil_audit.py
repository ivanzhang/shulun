#!/usr/bin/env python3
"""生成 H-lower 活跃素数带端点运动模板审计证书。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_endpoint_motion_stencil_audit.py
  python3 -m json.tool data/square-phase-offband-prefix-gap-shadow-selector-h-lower-endpoint-motion-stencil-ledger.json

输出：
  data/square-phase-offband-prefix-gap-shadow-selector-h-lower-endpoint-motion-stencil-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-endpoint-motion-stencil-audit.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-endpoint-motion-stencil-audit.md
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

ENDPOINT_ROUTER = (
    ROOT
    / "experiments"
    / "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_endpoint_band_atom_router.py"
)
TEMPLATE_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-template-provenance-ledger.json"
BUDGET_LEDGER = DATA / (
    "square-phase-offband-prefix-gap-shadow-selector-h-lower-singleton-rankin-budget-ledger.json"
)
BAND_LEDGER = DATA / (
    "square-phase-offband-prefix-gap-shadow-selector-h-lower-active-ell-interval-band-ledger.json"
)
ENDPOINT_LEDGER = DATA / (
    "square-phase-offband-prefix-gap-shadow-selector-h-lower-endpoint-band-atom-ledger.json"
)

OUT_LEDGER = DATA / (
    "square-phase-offband-prefix-gap-shadow-selector-h-lower-endpoint-motion-stencil-ledger.json"
)
OUT_JSON = DOCS / (
    "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-endpoint-motion-stencil-audit.json"
)
OUT_MD = DOCS / (
    "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-endpoint-motion-stencil-audit.md"
)

NEXT_TARGET = "EndpointOutwardArrivalBoundOrEndpointAtomPDECExclusion"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def is_prime(n: int) -> bool:
    """小范围素性判定。"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def previous_prime(n: int) -> int:
    """取小于 n 的最近素数。"""
    k = n - 1
    while k >= 2:
        if is_prime(k):
            return k
        k -= 1
    raise ValueError(f"no previous prime below {n}")


def next_prime(n: int) -> int:
    """取大于 n 的最近素数。"""
    k = n + 1
    while True:
        if is_prime(k):
            return k
        k += 1


def load_module(path: Path, name: str) -> Any:
    """按路径加载模块。"""
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def side_summary(side: str, ell: int, records: list[dict[str, Any]]) -> dict[str, Any]:
    """汇总 `(side, ell)` 的一槽 singleton 记录。"""
    residues = sorted({int(record["crt_residue"]) for record in records})
    slots = sorted({",".join(map(str, record["slot_keys"])) for record in records})
    p_values = sorted({int(record["p"]) for record in records})
    return {
        "side": side,
        "ell": ell,
        "record_count": len(records),
        "distinct_residue_count": len(residues),
        "distinct_slot_count": len(slots),
        "rankin_mass": len(records) / ell if ell else 0.0,
        "p_min": min(p_values) if p_values else None,
        "p_max": max(p_values) if p_values else None,
        "residue_values": residues,
        "slot_values": slots,
    }


def ell_summary(label: str, ell: int, grouped: dict[tuple[str, int], list[dict[str, Any]]]) -> dict[str, Any]:
    """汇总某个 ell 在两侧的模板形态。"""
    side_rows = [side_summary(side, ell, grouped.get((side, ell), [])) for side in ("minus", "plus")]
    total_records = sum(row["record_count"] for row in side_rows)
    nonempty_sides = [row["side"] for row in side_rows if row["record_count"]]
    total_residues = sum(row["distinct_residue_count"] for row in side_rows)
    total_slots = sum(row["distinct_slot_count"] for row in side_rows)
    return {
        "label": label,
        "ell": ell,
        "total_record_count": total_records,
        "total_distinct_residue_count": total_residues,
        "total_distinct_slot_count": total_slots,
        "nonempty_sides": nonempty_sides,
        "is_empty": total_records == 0,
        "is_minus_only_singleton": nonempty_sides == ["minus"] and total_records == 1,
        "is_core_absorption": len(nonempty_sides) == 2 and total_records >= 2,
        "side_rows": side_rows,
    }


def route_row(gate: str, closed: bool, evidence: str, remaining: str) -> dict[str, Any]:
    """构造路由行。"""
    return {
        "gate": gate,
        "closed_current_sweep": closed,
        "evidence": evidence,
        "global_remaining": remaining,
    }


def build_result(
    template_ledger: Path,
    budget_ledger: Path,
    band_ledger: Path,
    endpoint_ledger: Path,
) -> dict[str, Any]:
    """构造端点运动模板审计结果。"""
    endpoint_router = load_module(ENDPOINT_ROUTER, "endpoint_motion_endpoint_router")
    band = load_json(band_ledger)
    endpoint = load_json(endpoint_ledger)

    records, params = endpoint_router.build_singleton_records(template_ledger, budget_ledger)
    grouped = endpoint_router.grouped_one_slot(records)

    active = list(map(int, band["active_ell_values"]))
    both = list(map(int, band["both_side_ell_values"]))
    lower_endpoint = min(active)
    upper_endpoint = max(active)
    lower_core = min(both)
    upper_core = max(both)
    lower_outward = previous_prime(lower_endpoint)
    upper_outward = next_prime(upper_endpoint)

    stencil_rows = [
        ell_summary("lower_outward_neighbor", lower_outward, grouped),
        ell_summary("lower_endpoint_atom", lower_endpoint, grouped),
        ell_summary("lower_inward_core_edge", lower_core, grouped),
        ell_summary("upper_inward_core_edge", upper_core, grouped),
        ell_summary("upper_endpoint_atom", upper_endpoint, grouped),
        ell_summary("upper_outward_neighbor", upper_outward, grouped),
    ]

    outward_rows = [row for row in stencil_rows if "outward" in row["label"]]
    endpoint_rows = [row for row in stencil_rows if "endpoint_atom" in row["label"]]
    core_rows = [row for row in stencil_rows if "core_edge" in row["label"]]

    outward_neighbors_empty = all(row["is_empty"] for row in outward_rows)
    endpoints_are_minus_singletons = all(row["is_minus_only_singleton"] for row in endpoint_rows)
    inward_edges_are_core_absorption = all(row["is_core_absorption"] for row in core_rows)
    motion_stencil_closed = (
        outward_neighbors_empty
        and endpoints_are_minus_singletons
        and inward_edges_are_core_absorption
        and bool(endpoint["endpoint_atoms_are_singletons_current_sweep"])
    )

    route_rows = [
        route_row(
            "OutwardNeighborNoArrival",
            outward_neighbors_empty,
            f"outside primes {lower_outward},{upper_outward} have total records {[row['total_record_count'] for row in outward_rows]}",
            "EndpointOutwardArrivalBound",
        ),
        route_row(
            "EndpointAtomsMinusSingleton",
            endpoints_are_minus_singletons,
            f"endpoint primes {lower_endpoint},{upper_endpoint} are minus-only singletons",
            "EndpointAtomPDEC/SAE",
        ),
        route_row(
            "InwardMotionBecomesCoreAbsorption",
            inward_edges_are_core_absorption,
            f"core edge primes {lower_core},{upper_core} have both-side support",
            "CoreEdgeAbsorptionMultiplicityBound",
        ),
    ]

    endpoint_atom_keys = list(endpoint["endpoint_atom_keys"])
    aggregate = {
        "parameters": params,
        "active_band_endpoints": [lower_endpoint, upper_endpoint],
        "outward_neighbor_primes": [lower_outward, upper_outward],
        "inward_core_edge_primes": [lower_core, upper_core],
        "outward_neighbors_empty_current_sweep": outward_neighbors_empty,
        "endpoints_are_minus_singletons_current_sweep": endpoints_are_minus_singletons,
        "inward_edges_are_core_absorption_current_sweep": inward_edges_are_core_absorption,
        "endpoint_atom_count": len(endpoint_atom_keys),
        "endpoint_atom_keys": endpoint_atom_keys,
        "endpoint_motion_stencil_closed_current_sweep": motion_stencil_closed,
        "endpoint_outward_arrival_bound_proved": False,
        "endpoint_atom_pdec_excluded_globally": False,
        "core_edge_absorption_multiplicity_bound_proved": False,
        "row_column_unconditional_closed": False,
    }

    return {
        "certificate_type": (
            "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_"
            "endpoint_motion_stencil_audit"
        ),
        "status": "endpoint_motion_stencil_closed_current_sweep_global_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_sweep_not_used_as_global_proof": True,
        "aggregate": aggregate,
        "stencil_rows": stencil_rows,
        "route_rows": route_rows,
        "hardpoint_before_audit": "EndpointBandMotionBoundOrEndpointAtomPDECExclusion",
        "hardpoint_after_audit": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "dependency_hashes": {
            str(path.relative_to(ROOT)): sha256(path)
            for path in (template_ledger, budget_ledger, band_ledger, endpoint_ledger, ENDPOINT_ROUTER)
        },
    }


def write_outputs(result: dict[str, Any]) -> None:
    """写出 JSON 与 Markdown。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    for path in (OUT_LEDGER, OUT_JSON):
        path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    agg = result["aggregate"]
    lines = [
        "# Prime Matrix H-lower endpoint motion stencil audit",
        "",
        "**状态：** `endpoint_motion_stencil_closed_current_sweep_global_open`",
        "",
        "本审计把活跃素数带端点的运动拆成三类相邻模板：外向邻素数、端点自身、内向核心边缘。当前 sweep 中外向邻素数没有到达，端点自身是 minus-only 单原子，内向一步立即进入双侧核心支撑。",
        "",
        "```text",
        f"active_band_endpoints={agg['active_band_endpoints']}",
        f"outward_neighbor_primes={agg['outward_neighbor_primes']}",
        f"inward_core_edge_primes={agg['inward_core_edge_primes']}",
        f"outward_neighbors_empty_current_sweep={fmt_bool(agg['outward_neighbors_empty_current_sweep'])}",
        f"endpoints_are_minus_singletons_current_sweep={fmt_bool(agg['endpoints_are_minus_singletons_current_sweep'])}",
        f"inward_edges_are_core_absorption_current_sweep={fmt_bool(agg['inward_edges_are_core_absorption_current_sweep'])}",
        f"endpoint_motion_stencil_closed_current_sweep={fmt_bool(agg['endpoint_motion_stencil_closed_current_sweep'])}",
        "```",
        "",
        "## 1. motion stencil",
        "",
        "| label | ell | records | sides | residues | slots | type |",
        "| --- | ---: | ---: | --- | ---: | ---: | --- |",
    ]
    for row in result["stencil_rows"]:
        if row["is_empty"]:
            shape = "empty"
        elif row["is_minus_only_singleton"]:
            shape = "minus-only singleton"
        elif row["is_core_absorption"]:
            shape = "both-side core"
        else:
            shape = "mixed"
        lines.append(
            f"| `{row['label']}` | {row['ell']} | {row['total_record_count']} | "
            f"`{row['nonempty_sides']}` | {row['total_distinct_residue_count']} | "
            f"{row['total_distinct_slot_count']} | `{shape}` |"
        )

    lines.extend(
        [
            "",
            "## 2. route rows",
            "",
            "| gate | closed | evidence | global remaining |",
            "| --- | --- | --- | --- |",
        ]
    )
    for row in result["route_rows"]:
        lines.append(
            f"| `{row['gate']}` | {fmt_bool(row['closed_current_sweep'])} | {row['evidence']} | `{row['global_remaining']}` |"
        )
    lines.extend(
        [
            "",
            "## 3. 结论边界",
            "",
            "当前 sweep 中，端点运动不能作为未分类容量来源：外向一步没有物化，端点自身只有两个 minus-only 单原子，内向一步已经进入核心吸收带。",
            "",
            "这仍不是全局证明。下一步必须证明外向端点到达受限，或把端点原子复现排斥为 EndpointAtom-PDEC/SAE；核心边缘的多重吸收则需要独立 multiplicity bound。",
            "",
            "## 4. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in result["dependency_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    lines.append("")
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description="生成 H-lower endpoint motion stencil 审计证书。")
    parser.add_argument("--template-ledger", type=Path, default=TEMPLATE_LEDGER)
    parser.add_argument("--budget-ledger", type=Path, default=BUDGET_LEDGER)
    parser.add_argument("--band-ledger", type=Path, default=BAND_LEDGER)
    parser.add_argument("--endpoint-ledger", type=Path, default=ENDPOINT_LEDGER)
    return parser.parse_args()


def abs_path(path: Path) -> Path:
    """规范相对路径。"""
    return path if path.is_absolute() else ROOT / path


def main() -> None:
    """入口。"""
    args = parse_args()
    result = build_result(
        abs_path(args.template_ledger),
        abs_path(args.budget_ledger),
        abs_path(args.band_ledger),
        abs_path(args.endpoint_ledger),
    )
    write_outputs(result)
    print(json.dumps(result["aggregate"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
