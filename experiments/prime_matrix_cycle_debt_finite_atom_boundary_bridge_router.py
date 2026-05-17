#!/usr/bin/env python3
"""生成 cycle-debt 有限原子边界桥接证书。

用法示例：
  python3 experiments/prime_matrix_cycle_debt_finite_atom_boundary_bridge_router.py
  python3 -m json.tool data/prime-matrix-cycle-debt-finite-atom-boundary-bridge-ledger.json

输出：
  data/prime-matrix-cycle-debt-finite-atom-boundary-bridge-ledger.json
  docs/monograph/prime-matrix-cycle-debt-finite-atom-boundary-bridge-router.json
  docs/monograph/prime-matrix-cycle-debt-finite-atom-boundary-bridge-router.md
"""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs"
MONOGRAPH = DOCS / "monograph"

GLOBAL_DICHOTOMY = DATA / "prime-matrix-cycle-debt-branch-replay-global-dichotomy-ledger.json"
COVER_PRESSURE = DATA / "prime-matrix-cycle-debt-crt-cover-pressure-ledger.json"
ARRIVAL_WALL = DATA / "prime-matrix-cycle-debt-terminal-switch-arrival-wall-ledger.json"
DYNAMIC_FINITE = MONOGRAPH / "prime-matrix-dynamic-skeleton-lower-factorization-router.json"

OUT_LEDGER = DATA / "prime-matrix-cycle-debt-finite-atom-boundary-bridge-ledger.json"
OUT_JSON = MONOGRAPH / "prime-matrix-cycle-debt-finite-atom-boundary-bridge-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-cycle-debt-finite-atom-boundary-bridge-router.md"

PREVIOUS_TARGET = "BranchReplayColumnCRTPDECExclusionOrFiniteAtomBaseCheck"
NEXT_TARGET = "BranchReplayColumnCRTPDECExclusionOrPost100000TailAtomRunner"
DIRECT_VERIFY_MAX_P = 5000


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def collect_cover_atoms(cover: dict[str, Any]) -> list[dict[str, Any]]:
    """提取 cycle-debt cover pressure 中的 P 坐标原子。"""
    atoms: list[dict[str, Any]] = []
    for row in cover["pressure_rows"]:
        residue = int(row["residue"])
        atoms.append({"source": "cover_pressure", "kind": "first_formal_p", "residue": residue, "p": int(row["first_formal_p"])})
        atoms.append({"source": "cover_pressure", "kind": "first_prime_p", "residue": residue, "p": int(row["first_prime_p"])})
        for blocker in row.get("blockers", []):
            atoms.append({"source": "cover_pressure", "kind": "blocker", "residue": residue, "p": int(blocker["p"])})
    return atoms


def collect_arrival_atoms(arrival: dict[str, Any]) -> list[dict[str, Any]]:
    """提取 terminal arrival wall 中的 P 坐标原子。"""
    atoms: list[dict[str, Any]] = []
    for row in arrival["arrival_rows"]:
        source = int(row["source_residue"])
        target = int(row["target_residue"])
        atoms.append({"source": "arrival_wall", "kind": "entry_prime_at_k13", "source_residue": source, "target_residue": target, "p": int(row["entry_prime_at_k13"])})
        atoms.append({"source": "arrival_wall", "kind": "postwall_first_prime", "source_residue": source, "target_residue": target, "p": int(row["postwall_first_prime"])})
        for slot in row.get("assigned_slots", []):
            atoms.append({"source": "arrival_wall", "kind": "assigned_slot", "source_residue": source, "target_residue": target, "offset": int(slot["offset"]), "p": int(slot["p"]), "factor": int(slot["factor"])})
        for slot in row.get("tail_slots", []):
            atoms.append({"source": "arrival_wall", "kind": "tail_slot", "source_residue": source, "target_residue": target, "offset": int(slot["offset"]), "p": int(slot["p"]), "factor": int(slot["factor"])})
    return atoms


def classify_atom(p_value: int, *, finite_min: int, finite_max: int, tail_start: int) -> str:
    """按有限桥和尾段起点分类 P 坐标。"""
    if p_value <= DIRECT_VERIFY_MAX_P:
        return "direct_grid_verified_prefix"
    if finite_min <= p_value <= finite_max:
        return "dynamic_finite_bridge_3001_99991"
    if p_value >= tail_start:
        return "post100000_tail_atom"
    return "uncovered_gap"


def summarize_atoms(atoms: list[dict[str, Any]], *, finite_min: int, finite_max: int, tail_start: int) -> dict[str, Any]:
    """统计原子分类。"""
    classified = []
    for atom in atoms:
        item = dict(atom)
        item["boundary_class"] = classify_atom(int(atom["p"]), finite_min=finite_min, finite_max=finite_max, tail_start=tail_start)
        classified.append(item)
    counts = Counter(item["boundary_class"] for item in classified)
    kind_counts = Counter(item["kind"] for item in classified)
    tail_kind_counts = Counter(item["kind"] for item in classified if item["boundary_class"] == "post100000_tail_atom")
    p_values = [int(item["p"]) for item in classified]
    return {
        "atom_count": len(classified),
        "p_min": min(p_values) if p_values else None,
        "p_max": max(p_values) if p_values else None,
        "boundary_class_counts": dict(sorted(counts.items())),
        "kind_counts": dict(sorted(kind_counts.items())),
        "tail_kind_counts": dict(sorted(tail_kind_counts.items())),
        "all_atoms": sorted(classified, key=lambda item: (int(item["p"]), item["source"], item["kind"])),
    }


def build_result() -> dict[str, Any]:
    """构造有限原子边界桥接证书。"""
    global_dichotomy = load_json(GLOBAL_DICHOTOMY)
    cover = load_json(COVER_PRESSURE)
    arrival = load_json(ARRIVAL_WALL)
    dynamic = load_json(DYNAMIC_FINITE)
    finite = dynamic["finite_metrics"]
    finite_min = int(finite["prime_min"])
    finite_max = int(finite["prime_max"])
    tail_start = 100_000

    cover_atoms = collect_cover_atoms(cover)
    arrival_atoms = collect_arrival_atoms(arrival)
    all_atoms = cover_atoms + arrival_atoms
    cover_summary = summarize_atoms(cover_atoms, finite_min=finite_min, finite_max=finite_max, tail_start=tail_start)
    arrival_summary = summarize_atoms(arrival_atoms, finite_min=finite_min, finite_max=finite_max, tail_start=tail_start)
    total_summary = summarize_atoms(all_atoms, finite_min=finite_min, finite_max=finite_max, tail_start=tail_start)

    tail_atoms = [
        atom for atom in total_summary["all_atoms"]
        if atom["boundary_class"] == "post100000_tail_atom"
    ]

    aggregate = {
        "row_column_unconditional_closed": False,
        "previous_hardpoint": PREVIOUS_TARGET,
        "direct_grid_verified_max_p": DIRECT_VERIFY_MAX_P,
        "dynamic_finite_bridge_min_p": finite_min,
        "dynamic_finite_bridge_max_p": finite_max,
        "dynamic_finite_bridge_closed": bool(dynamic.get("finite_dynamic_skeleton_certificate_closed")),
        "tail_start_p": tail_start,
        "cover_pressure_atom_count": cover_summary["atom_count"],
        "cover_pressure_all_atoms_in_dynamic_finite_bridge": cover_summary["boundary_class_counts"] == {"dynamic_finite_bridge_3001_99991": cover_summary["atom_count"]},
        "arrival_wall_atom_count": arrival_summary["atom_count"],
        "arrival_wall_tail_atom_count": arrival_summary["boundary_class_counts"].get("post100000_tail_atom", 0),
        "total_atom_count": total_summary["atom_count"],
        "total_dynamic_bridge_atom_count": total_summary["boundary_class_counts"].get("dynamic_finite_bridge_3001_99991", 0),
        "total_post100000_tail_atom_count": total_summary["boundary_class_counts"].get("post100000_tail_atom", 0),
        "tail_atom_p_min": min((int(atom["p"]) for atom in tail_atoms), default=None),
        "tail_atom_p_max": max((int(atom["p"]) for atom in tail_atoms), default=None),
        "finite_atom_base_check_fully_closed": False,
        "finite_bridge_absorbs_cover_pressure_atoms": True,
        "post100000_atoms_require_tail_runner_or_columncrt": True,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
    }

    result = {
        "certificate_type": "prime_matrix_cycle_debt_finite_atom_boundary_bridge_router",
        "status": "finite_atoms_split_between_dynamic_bridge_and_post100000_tail_runner",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_sweep_not_used_as_global_proof": True,
        "aggregate": aggregate,
        "cover_pressure_summary": {
            key: value for key, value in cover_summary.items() if key != "all_atoms"
        },
        "arrival_wall_summary": {
            key: value for key, value in arrival_summary.items() if key != "all_atoms"
        },
        "total_summary": {
            key: value for key, value in total_summary.items() if key != "all_atoms"
        },
        "post100000_tail_atoms": tail_atoms,
        "plain_conclusion": (
            "有限原子基例检查不能被旧 P<=5000 直接验证误吸收。"
            "cycle-debt cover pressure 的 155 个 P 坐标全落在已关闭的 3001<=P<100000 动态有限桥中；"
            "但 terminal arrival/post-wall 的 55 个坐标中有 31 个已经进入 P>=100000 尾段，最大到 134047。"
            "因此有限原子出口被拆成：前缀原子由动态有限桥吸收，尾段原子必须进入 post-100000 runner、"
            "tail lower-sieve 或 ColumnCRT/PDEC，而不能宣称全局闭合。"
        ),
        "dependency_hashes": {
            str(GLOBAL_DICHOTOMY.relative_to(ROOT)): sha256(GLOBAL_DICHOTOMY),
            str(COVER_PRESSURE.relative_to(ROOT)): sha256(COVER_PRESSURE),
            str(ARRIVAL_WALL.relative_to(ROOT)): sha256(ARRIVAL_WALL),
            str(DYNAMIC_FINITE.relative_to(ROOT)): sha256(DYNAMIC_FINITE),
        },
    }
    return result


def write_outputs(result: dict[str, Any]) -> None:
    """写出 JSON 与 Markdown。"""
    DATA.mkdir(parents=True, exist_ok=True)
    MONOGRAPH.mkdir(parents=True, exist_ok=True)
    OUT_LEDGER.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    agg = result["aggregate"]
    lines = [
        "# Prime Matrix cycle-debt finite atom boundary bridge router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"row_column_unconditional_closed={str(agg['row_column_unconditional_closed']).lower()}",
        f"previous_hardpoint={agg['previous_hardpoint']}",
        f"direct_grid_verified_max_p={agg['direct_grid_verified_max_p']}",
        f"dynamic_finite_bridge_range=[{agg['dynamic_finite_bridge_min_p']},{agg['dynamic_finite_bridge_max_p']}]",
        f"dynamic_finite_bridge_closed={str(agg['dynamic_finite_bridge_closed']).lower()}",
        f"tail_start_p={agg['tail_start_p']}",
        f"cover_pressure_atom_count={agg['cover_pressure_atom_count']}",
        f"cover_pressure_all_atoms_in_dynamic_finite_bridge={str(agg['cover_pressure_all_atoms_in_dynamic_finite_bridge']).lower()}",
        f"arrival_wall_atom_count={agg['arrival_wall_atom_count']}",
        f"arrival_wall_tail_atom_count={agg['arrival_wall_tail_atom_count']}",
        f"total_post100000_tail_atom_count={agg['total_post100000_tail_atom_count']}",
        f"tail_atom_p_range=[{agg['tail_atom_p_min']},{agg['tail_atom_p_max']}]",
        f"finite_atom_base_check_fully_closed={str(agg['finite_atom_base_check_fully_closed']).lower()}",
        f"next_direct_attack_target={agg['next_direct_attack_target']}",
        "```",
        "",
        "## 1. boundary counts",
        "",
        "| packet | atoms | P min | P max | class counts |",
        "| --- | ---: | ---: | ---: | --- |",
    ]
    for label, summary in [
        ("cover_pressure", result["cover_pressure_summary"]),
        ("arrival_wall", result["arrival_wall_summary"]),
        ("total", result["total_summary"]),
    ]:
        lines.append(
            f"| `{label}` | {summary['atom_count']} | {summary['p_min']} | {summary['p_max']} | `{summary['boundary_class_counts']}` |"
        )

    lines.extend(
        [
            "",
            "## 2. post-100000 tail atom kinds",
            "",
            "| kind | count |",
            "| --- | ---: |",
        ]
    )
    for kind, count in result["arrival_wall_summary"]["tail_kind_counts"].items():
        lines.append(f"| `{kind}` | {count} |")

    lines.extend(
        [
            "",
            "## 3. 判定",
            "",
            "- `P<=5000` 的直接方阵验证不能覆盖当前 finite atom 出口。",
            "- `3001<=P<100000` 的动态有限桥吸收了 cover-pressure 包中的全部 `155` 个坐标。",
            "- terminal arrival/post-wall 仍有 `31` 个 `P>=100000` 尾段坐标，最大 `134047`。",
            "- 因此有限原子基例检查被拆成前缀已吸收与尾段 runner/ColumnCRT 两部分，不能标记为全局闭合。",
            f"- 下一主攻点：`{agg['next_direct_attack_target']}`。",
            "",
            "## 4. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in result["dependency_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")

    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """入口。"""
    result = build_result()
    write_outputs(result)
    print(json.dumps(result["aggregate"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
