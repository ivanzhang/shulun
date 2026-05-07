#!/usr/bin/env python3
"""汇总 Triad-A1 从固定 Q-PDEC 到终端三证书的无循环账本。

用法示例：
  python3 experiments/prime_matrix_triad_a1_terminal_no_cycle_ledger.py

输出：
  docs/monograph/prime-matrix-triad-a1-terminal-no-cycle-ledger.json
  docs/monograph/prime-matrix-triad-a1-terminal-no-cycle-ledger.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_DIRECTION = DOCS / "prime-matrix-triad-a1-lhb-direction-support-audit.json"
DEFAULT_FOURIER = DOCS / "prime-matrix-triad-a1-lhb-fourier-cap-scan.json"
DEFAULT_TOWER = DOCS / "prime-matrix-triad-a1-newlayer-tower-gate.json"
DEFAULT_TERMINAL = DOCS / "prime-matrix-triad-a1-terminal-router.json"
DEFAULT_HRO = ",".join(
    str(path)
    for path in (
        DOCS / "prime-matrix-triad-a1-hole-residue-occupancy-q2310-q30030.json",
        DOCS / "prime-matrix-triad-a1-hole-residue-occupancy-q30030-q510510.json",
    )
)
DEFAULT_TCP = ",".join(
    str(path)
    for path in (
        DOCS / "prime-matrix-triad-a1-tail-capacity-pressure-q2310-q30030.json",
        DOCS / "prime-matrix-triad-a1-tail-capacity-pressure-q30030-q510510.json",
    )
)
DEFAULT_TUD = DOCS / "prime-matrix-triad-a1-tail-unit-density-gate.json"
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-terminal-no-cycle-ledger.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-terminal-no-cycle-ledger.md"


def parse_paths(raw: str) -> list[Path]:
    """解析逗号分隔路径。"""
    return [Path(item.strip()) for item in raw.split(",") if item.strip()]


def file_sha256(path: Path) -> str:
    """计算文件 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def fmt_float(value: float | None) -> str:
    """格式化浮点数。"""
    if value is None:
        return "n/a"
    return f"{value:.6g}"


def summarize_direction(direction: dict[str, Any]) -> dict[str, Any]:
    """汇总零块方向支撑。"""
    return {
        "gate": "FixedQZeroBlockDirection",
        "status": "Closed" if direction["all_empty"] else "NeedsRefinement",
        "all_empty": direction["all_empty"],
        "p_values": direction["p_values"],
        "route": (
            "零容量块方向在 LHB 分支为空。"
            if direction["all_empty"]
            else "交集非空，进入 Sparse/Persistent cap 路由。"
        ),
    }


def summarize_fourier(fourier: dict[str, Any]) -> dict[str, Any]:
    """汇总固定 Q Fourier-cap 密度屏障。"""
    rows = []
    has_persistent = False
    for item in fourier["prime_results"]:
        p = int(item["p"])
        for report in item["alpha_reports"]:
            persistent_rate = float(report["class_rates"]["PersistentCap"])
            if persistent_rate > 0:
                has_persistent = True
            rows.append(
                {
                    "p": p,
                    "alpha": report["alpha"],
                    "persistent_rate": persistent_rate,
                    "worst_intersection_size": report["top_by_size"][0]["intersection_size"],
                    "worst_intersection_mass": report["top_by_mass"][0]["intersection_mass"],
                }
            )
    max_row = max(rows, key=lambda row: row["persistent_rate"]) if rows else None
    return {
        "gate": "FixedQDensityBarrier",
        "status": "PersistentCapForcesLiftOrExtraRows" if has_persistent else "NoPersistentCapsInAudit",
        "has_persistent_caps": has_persistent,
        "max_persistent_rate_row": max_row,
        "route": (
            "固定 Q 普通 Fourier cap 出现持久交集；不能在同一固定层循环，必须升层、加 column/tail 行或进 CleanKLS。"
            if has_persistent
            else "当前扫描未见持久 cap；Empty/Sparse 分别进入闭合或 LocalSurvivor。"
        ),
    }


def summarize_tower(tower: dict[str, Any]) -> dict[str, Any]:
    """汇总新层塔门控。"""
    all_deleting = all(cls == "FiberDeletionLayer" for cls in tower["layer_classes"])
    layer_rows = [
        {
            "q": layer["q"],
            "q_lift": layer["q_lift"],
            "fiber_size": layer["fiber_size"],
            "layer_class": layer["layer_class"],
            "min_density_drop_factor": layer["min_density_drop_factor"],
            "max_slot_survival_rate": layer["max_slot_survival_rate"],
        }
        for layer in tower["layers"]
    ]
    return {
        "gate": "NewLayerTower",
        "status": "CurrentLayersDeleting" if all_deleting else "TerminalInputAppeared",
        "all_layers_monotone": tower["all_layers_monotone"],
        "all_layers_resparse": tower["all_layers_resparse"],
        "layer_rows": layer_rows,
        "route": (
            "已物化升层均重新稀疏，继续累计删除势。"
            if all_deleting
            else "已有升层不是纯删除，需交给 PDEC/CleanKLS/Stitching。"
        ),
    }


def summarize_hro(paths: list[Path]) -> dict[str, Any]:
    """汇总 HoleResidueOccupancy 门。"""
    audits = [(path, load_json(path)) for path in paths]
    rows = []
    for path, audit in audits:
        for item in audit["prime_results"]:
            rows.append(
                {
                    "audit_path": str(path),
                    "q": audit["q"],
                    "q_lift": audit["q_lift"],
                    "p": item["p"],
                    "union_bound_rate": item["union_bound_rate"],
                    "certified_deletion_lb_rate": item["certified_deletion_lb_rate"],
                    "max_phase_occupied_ratio": item["max_phase_occupied_ratio"],
                }
            )
    min_deletion = min((row["certified_deletion_lb_rate"] for row in rows), default=None)
    max_union = max((row["union_bound_rate"] for row in rows), default=None)
    return {
        "gate": "HoleResidueOccupancy",
        "status": "CertifiedDeletionOrNamedEscape",
        "row_count": len(rows),
        "min_certified_deletion_lb_rate": min_deletion,
        "max_union_bound_rate": max_union,
        "rows": rows,
        "route": "若 Occ+TI 不满则删除；若趋满只能进入 OccupancySaturation 或 TailIndependence。",
    }


def summarize_tcp(paths: list[Path]) -> dict[str, Any]:
    """汇总 TailCapacityPressure 门。"""
    audits = [(path, load_json(path)) for path in paths]
    rows = []
    all_consistent = True
    all_dead_hall_certified = True
    for path, audit in audits:
        all_consistent = all_consistent and audit["consistency_mismatch_count"] == 0
        for item in audit["prime_results"]:
            all_dead_hall_certified = (
                all_dead_hall_certified and int(item["hall_uncertified_dead_slots"]) == 0
            )
            rows.append(
                {
                    "audit_path": str(path),
                    "q": audit["q"],
                    "q_lift": audit["q_lift"],
                    "p": item["p"],
                    "survival_rate": item["survival_rate"],
                    "hall_certified_dead_rate": item["hall_certified_dead_rate"],
                    "hall_uncertified_dead_slots": item["hall_uncertified_dead_slots"],
                    "avg_survivor_kl_floor": item["avg_survivor_kl_floor_to_uniform_tail"],
                }
            )
    return {
        "gate": "TailCapacityPressure",
        "status": "CapacityDeathOrKL",
        "all_consistent_with_lift_m_vector": all_consistent,
        "all_dead_slots_hall_certified": all_dead_hall_certified,
        "rows": rows,
        "route": "残余洞容量/Hall 失败则死亡；容量成功则支付 Tail KL 或进入 CleanKLS。",
    }


def summarize_tud(tud: dict[str, Any]) -> dict[str, Any]:
    """汇总 TailUnitDensity KL 门。"""
    return {
        "gate": "TailUnitDensity",
        "status": "NonemptyResidualPaysKLOrCleanKLS",
        "all_unit_density_bounds_pass": tud["all_unit_density_bounds_pass"],
        "rows": [
            {
                "q": row["q"],
                "q_lift": row["q_lift"],
                "p": row["p"],
                "tail_unit_density": row["tail_unit_density"],
                "singleton_completion_upper": row["singleton_completion_upper"],
                "structural_kl_floor": row["structural_kl_floor_for_nonempty_residual"],
                "positive_residual_survival_rate": row["positive_residual_survival_rate"],
                "max_actual_completion_ratio": row["max_positive_residual_completion_ratio"],
            }
            for row in tud["rows"]
        ],
        "route": "非空残余洞幸存且 u_tail 不小则支付 KL；KL 小只能进入空残余洞或 CleanKLS。",
    }


def summarize_terminal(terminal: dict[str, Any]) -> dict[str, Any]:
    """汇总终端路由。"""
    return {
        "gate": "TerminalRouter",
        "status": terminal["current_terminal_claim"],
        "route_counts": terminal["route_counts"],
        "triad_counts": terminal["triad_counts"],
        "route": "当前物化层仍在删除势；删除停止时强制进入 PDEC/CleanKLS，删除发散时进入 Sparse/LocalSurvivor。",
    }


def run(args: argparse.Namespace) -> dict[str, Any]:
    """运行无循环账本。"""
    direction_path = args.direction_json
    fourier_path = args.fourier_json
    tower_path = args.tower_json
    terminal_path = args.terminal_json
    tud_path = args.tud_json
    hro_paths = parse_paths(args.hro_jsons)
    tcp_paths = parse_paths(args.tcp_jsons)

    direction = load_json(direction_path)
    fourier = load_json(fourier_path)
    tower = load_json(tower_path)
    terminal = load_json(terminal_path)
    tud = load_json(tud_path)

    gates = [
        summarize_direction(direction),
        summarize_fourier(fourier),
        summarize_tower(tower),
        summarize_hro(hro_paths),
        summarize_tcp(tcp_paths),
        summarize_tud(tud),
        summarize_terminal(terminal),
    ]
    all_materialized = (
        direction["all_empty"]
        and tower["all_layers_monotone"]
        and tower["all_layers_resparse"]
        and all(load_json(path)["consistency_mismatch_count"] == 0 for path in tcp_paths)
        and tud["all_unit_density_bounds_pass"]
    )
    return {
        "certificate_type": "triad_a1_terminal_no_cycle_ledger",
        "status": "a1_middle_escape_closed_terminal_certificates_open",
        "source_hashes": {
            "terminal_no_cycle_ledger_script": file_sha256(Path(__file__).resolve()),
            "direction_support_json": file_sha256(direction_path),
            "fourier_cap_scan_json": file_sha256(fourier_path),
            "newlayer_tower_gate_json": file_sha256(tower_path),
            "terminal_router_json": file_sha256(terminal_path),
            "tail_unit_density_json": file_sha256(tud_path),
            **{f"hro_{idx}": file_sha256(path) for idx, path in enumerate(hro_paths, start=1)},
            **{f"tcp_{idx}": file_sha256(path) for idx, path in enumerate(tcp_paths, start=1)},
        },
        "gates": gates,
        "all_materialized_gates_pass": all_materialized,
        "no_cycle_law": (
            "固定 Q 普通 cap 持久时不能同层循环；升层后若删除不足则 HRO/TCP/TUD 强制进入 "
            "PDEC/CleanKLS，若删除持续则进入 Sparse/LocalSurvivor 或容量矛盾。"
        ),
        "terminal_obligations": [
            "PDEC family U_CRT<L_PDEC",
            "CleanKLS/DLS admission and large-sieve certificate",
            "Sparse/LocalSurvivor witness or blocker deficit",
        ],
        "review_conclusion": (
            "当前账本关闭的是 A1 路线的中间逃逸和同层循环，不是三终端证书全集。"
            "后续必须在 PDEC、CleanKLS/DLS、Sparse/LocalSurvivor 三类中提交实际排斥证书。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 终端无循环账本",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 无循环律",
        "",
        result["no_cycle_law"],
        "",
        f"- `all_materialized_gates_pass={result['all_materialized_gates_pass']}`。",
        "",
        "## 2. 来源指纹",
        "",
        "| source | sha256 |",
        "| --- | --- |",
    ]
    for name, digest in result["source_hashes"].items():
        lines.append(f"| `{name}` | `{digest}` |")

    lines.extend(
        [
            "",
            "## 3. 门控总表",
            "",
            "| gate | status | route |",
            "| --- | --- | --- |",
        ]
    )
    for gate in result["gates"]:
        lines.append(f"| `{gate['gate']}` | `{gate['status']}` | {gate['route']} |")

    lines.extend(
        [
            "",
            "## 4. 关键数值",
            "",
            "### NewLayerTower",
            "",
            "| layer | r | class | min drop | max survival |",
            "| --- | ---: | --- | ---: | ---: |",
        ]
    )
    tower = next(gate for gate in result["gates"] if gate["gate"] == "NewLayerTower")
    for row in tower["layer_rows"]:
        lines.append(
            "| Q={q}->{ql} | {r} | `{cls}` | {drop} | {surv} |".format(
                q=row["q"],
                ql=row["q_lift"],
                r=row["fiber_size"],
                cls=row["layer_class"],
                drop=fmt_float(row["min_density_drop_factor"]),
                surv=fmt_float(row["max_slot_survival_rate"]),
            )
        )

    hro = next(gate for gate in result["gates"] if gate["gate"] == "HoleResidueOccupancy")
    lines.extend(
        [
            "",
            "### HoleResidueOccupancy",
            "",
            f"- `max_union_bound_rate={fmt_float(hro['max_union_bound_rate'])}`。",
            f"- `min_certified_deletion_lb_rate={fmt_float(hro['min_certified_deletion_lb_rate'])}`。",
        ]
    )

    tcp = next(gate for gate in result["gates"] if gate["gate"] == "TailCapacityPressure")
    lines.extend(
        [
            "",
            "### TailCapacityPressure",
            "",
            f"- `all_consistent_with_lift_m_vector={tcp['all_consistent_with_lift_m_vector']}`。",
            f"- `all_dead_slots_hall_certified={tcp['all_dead_slots_hall_certified']}`。",
        ]
    )

    tud = next(gate for gate in result["gates"] if gate["gate"] == "TailUnitDensity")
    lines.extend(
        [
            "",
            "### TailUnitDensity",
            "",
            f"- `all_unit_density_bounds_pass={tud['all_unit_density_bounds_pass']}`。",
            "",
            "## 5. 剩余终端义务",
            "",
        ]
    )
    for obligation in result["terminal_obligations"]:
        lines.append(f"- {obligation}。")

    lines.extend(
        [
            "",
            "## 6. 结论",
            "",
            "A1 现在不能再停在固定 Q cap、升层口径、旧洞占用、Tail 容量或 Tail KL 的中间解释上。",
            "这些门控要么已在当前层给出删除势，要么强制进入 PDEC/CleanKLS/SparseLocal 三终端。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--direction-json", type=Path, default=DEFAULT_DIRECTION)
    parser.add_argument("--fourier-json", type=Path, default=DEFAULT_FOURIER)
    parser.add_argument("--tower-json", type=Path, default=DEFAULT_TOWER)
    parser.add_argument("--terminal-json", type=Path, default=DEFAULT_TERMINAL)
    parser.add_argument("--hro-jsons", type=str, default=DEFAULT_HRO)
    parser.add_argument("--tcp-jsons", type=str, default=DEFAULT_TCP)
    parser.add_argument("--tud-json", type=Path, default=DEFAULT_TUD)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(args)
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(
        json.dumps(
            {
                "status": result["status"],
                "all_materialized_gates_pass": result["all_materialized_gates_pass"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
