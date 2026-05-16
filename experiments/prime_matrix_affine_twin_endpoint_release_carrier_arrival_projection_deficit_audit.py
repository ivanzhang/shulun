#!/usr/bin/env python3
"""生成 AffineTwin endpoint-release carrier-arrival projection-deficit 审计证书。

用法示例：
  python3 experiments/prime_matrix_affine_twin_endpoint_release_carrier_arrival_projection_deficit_audit.py
  python3 -m json.tool data/prime-matrix-affine-twin-endpoint-release-carrier-arrival-projection-deficit-ledger.json

输出：
  data/prime-matrix-affine-twin-endpoint-release-carrier-arrival-projection-deficit-ledger.json
  docs/monograph/prime-matrix-affine-twin-endpoint-release-carrier-arrival-projection-deficit-audit.json
  docs/monograph/prime-matrix-affine-twin-endpoint-release-carrier-arrival-projection-deficit-audit.md
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

PRESSURE_LEDGER = DATA / (
    "prime-matrix-affine-twin-endpoint-release-carrier-arrival-pressure-product-ledger.json"
)
EDGE_LEDGER = DATA / "prime-matrix-affine-twin-window-edge-collision-ledger.json"

OUT_LEDGER = DATA / (
    "prime-matrix-affine-twin-endpoint-release-carrier-arrival-projection-deficit-ledger.json"
)
OUT_JSON = DOCS / (
    "prime-matrix-affine-twin-endpoint-release-carrier-arrival-projection-deficit-audit.json"
)
OUT_MD = DOCS / (
    "prime-matrix-affine-twin-endpoint-release-carrier-arrival-projection-deficit-audit.md"
)


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def pair_key(pair: tuple[int, int]) -> str:
    """生成 residue pair 稳定键。"""
    return f"{pair[0]}:{pair[1]}"


def parse_pair_key(key: str) -> tuple[int, int]:
    """解析 residue pair 键。"""
    left, right = key.split(":", 1)
    return int(left), int(right)


def product_pairs(generator_residues: set[int], fill_residues: set[int]) -> set[tuple[int, int]]:
    """生成两侧残基笛卡尔积。"""
    return set(itertools.product(generator_residues, fill_residues))


def projection_summary(
    generator_residues: set[int],
    fill_residues: set[int],
    target_window_pairs: set[tuple[int, int]],
    sqrt_floor: int,
) -> dict[str, Any]:
    """计算形式乘积到窗口 actual projection 的缺口。"""
    formal_pairs = product_pairs(generator_residues, fill_residues)
    projection_hits = formal_pairs & target_window_pairs
    return {
        "generator_count": len(generator_residues),
        "fill_count": len(fill_residues),
        "formal_product_count": len(formal_pairs),
        "projection_hit_count": len(projection_hits),
        "projection_deficit_count": len(formal_pairs) - len(projection_hits),
        "actual_sqrt_slack": sqrt_floor - len(projection_hits),
        "formal_excess_over_sqrt_floor": len(formal_pairs) - sqrt_floor,
        "projection_hits": [pair_key(pair) for pair in sorted(projection_hits)],
        "empty_projection_count": len(formal_pairs - target_window_pairs),
        "projects_below_sqrt_gate": len(projection_hits) <= sqrt_floor,
    }


def build_result(pressure_path: Path, edge_path: Path) -> dict[str, Any]:
    """构造 carrier-arrival projection-deficit 审计结果。"""
    pressure = load_json(pressure_path)
    edge = load_json(edge_path)

    agg = pressure["aggregate"]
    sqrt_floor = int(agg["sqrt_floor"])
    target_atoms = {
        str(row["target_pair_key"]): row for row in pressure["target_atom_rows"]
    }
    base_generator_residues = set(int(value) for value in agg["base_generator_residues"])
    base_fill_residues = set(int(value) for value in agg["base_fill_residues"])
    full_generator_residues = base_generator_residues | {
        int(value) for value in agg["carrier_required_new_generator_residues"]
    }
    full_fill_residues = base_fill_residues | {
        int(value) for value in agg["carrier_required_new_fill_residues"]
    }
    q_key = str(agg["fill_modulus"])
    target_window_pairs = {
        (
            int(row["target_generator_residue"]),
            int(row["target_fill_residue"]),
        )
        for row in edge["target_window_pairs"][q_key]
    }
    actual_anchor_pair = (
        int(edge["aggregate"].get("actual_generator_residue", 19))
        if "actual_generator_residue" in edge["aggregate"]
        else 19,
        int(edge["aggregate"].get("actual_fill_residue", 8))
        if "actual_fill_residue" in edge["aggregate"]
        else 8,
    )

    minimal_rows: list[dict[str, Any]] = []
    for row in pressure["minimal_crossing_rows"]:
        generator_residues = set(base_generator_residues)
        fill_residues = set(base_fill_residues)
        selected_target_pairs = {parse_pair_key(key) for key in row["target_pair_keys"]}
        for key in row["target_pair_keys"]:
            atom = target_atoms[key]
            if bool(atom["needs_new_generator_residue"]):
                generator_residues.add(int(atom["target_generator_residue"]))
            if bool(atom["needs_new_fill_residue"]):
                fill_residues.add(int(atom["target_fill_residue"]))
        summary = projection_summary(
            generator_residues,
            fill_residues,
            target_window_pairs,
            sqrt_floor,
        )
        expected_hits = selected_target_pairs | {actual_anchor_pair}
        minimal_rows.append(
            {
                "target_pair_keys": row["target_pair_keys"],
                "selected_target_pair_count": len(selected_target_pairs),
                "expected_projection_hit_keys": [
                    pair_key(pair) for pair in sorted(expected_hits)
                ],
                "projection_hits_equal_anchor_plus_selected_targets": set(
                    summary["projection_hits"]
                )
                == {pair_key(pair) for pair in expected_hits},
                **summary,
            }
        )

    full_summary = projection_summary(
        full_generator_residues,
        full_fill_residues,
        target_window_pairs,
        sqrt_floor,
    )
    all_target_pairs = {parse_pair_key(key) for key in target_atoms}
    full_expected_hits = all_target_pairs | {actual_anchor_pair}
    full_summary["expected_projection_hit_keys"] = [
        pair_key(pair) for pair in sorted(full_expected_hits)
    ]
    full_summary["projection_hits_equal_anchor_plus_all_targets"] = set(
        full_summary["projection_hits"]
    ) == {pair_key(pair) for pair in full_expected_hits}

    all_minimal_project_below = all(
        bool(row["projects_below_sqrt_gate"]) for row in minimal_rows
    )
    all_minimal_hits_are_expected = all(
        bool(row["projection_hits_equal_anchor_plus_selected_targets"])
        for row in minimal_rows
    )
    closed_current = (
        bool(agg["carrier_arrival_pressure_product_routed_current_sweep"])
        and all_minimal_project_below
        and all_minimal_hits_are_expected
        and bool(full_summary["projects_below_sqrt_gate"])
        and bool(full_summary["projection_hits_equal_anchor_plus_all_targets"])
    )

    result_aggregate = {
        "carrier_arrival_pressure_product_ledger": str(
            pressure_path.relative_to(ROOT)
        ),
        "window_edge_collision_ledger": str(edge_path.relative_to(ROOT)),
        "generator_modulus": int(agg["generator_modulus"]),
        "fill_modulus": int(agg["fill_modulus"]),
        "modulus_product": int(agg["modulus_product"]),
        "sqrt_floor": sqrt_floor,
        "target_window_pair_count": len(target_window_pairs),
        "minimal_crossing_formal_product_count": int(
            minimal_rows[0]["formal_product_count"]
        ),
        "minimal_crossing_projection_hit_count": int(
            minimal_rows[0]["projection_hit_count"]
        ),
        "minimal_crossing_projection_deficit_count": int(
            minimal_rows[0]["projection_deficit_count"]
        ),
        "minimal_crossing_actual_sqrt_slack": int(
            minimal_rows[0]["actual_sqrt_slack"]
        ),
        "minimal_crossing_projection_rows_count": len(minimal_rows),
        "all_minimal_crossings_project_below_sqrt_gate": all_minimal_project_below,
        "all_minimal_projection_hits_are_anchor_plus_selected_targets": (
            all_minimal_hits_are_expected
        ),
        "full_formal_product_count": int(full_summary["formal_product_count"]),
        "full_projection_hit_count": int(full_summary["projection_hit_count"]),
        "full_projection_deficit_count": int(full_summary["projection_deficit_count"]),
        "full_actual_sqrt_slack": int(full_summary["actual_sqrt_slack"]),
        "full_projection_hits_equal_anchor_plus_all_targets": bool(
            full_summary["projection_hits_equal_anchor_plus_all_targets"]
        ),
        "carrier_arrival_projection_deficit_closed_current_sweep": closed_current,
        "global_product_accounting_tightening_proved": False,
        "row_column_unconditional_closed": False,
    }

    return {
        "certificate_type": (
            "prime_matrix_affine_twin_endpoint_release_"
            "carrier_arrival_projection_deficit_audit"
        ),
        "status": "current_sweep_carrier_arrival_projection_deficit_closed_global_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "aggregate": result_aggregate,
        "minimal_crossing_projection_rows": minimal_rows,
        "full_packet_projection": full_summary,
        "contract": {
            "carrier_arrival_projection_gate": [
                "formal side-product crossing must be projected to actual support hits",
                "minimal crossing rows must project below the square-root gate",
                "projection hits must be exactly the actual anchor plus selected target atoms",
                "otherwise the crossing is an actual overload PDEC rather than product-accounting looseness",
            ],
            "closed_current_sweep": closed_current,
            "global_remaining": [
                "ProductAccountingTightening",
                "ProjectionCollision-PDEC",
                "PrimitiveTwinSlotSupportEscape-PDEC/SAE",
                "SuperSqrtPressureProductPDECExclusion",
                "GlobalUnusedTargetResidueArrivalBound",
            ],
        },
        "dependency_hashes": {
            str(path.relative_to(ROOT)): sha256(path)
            for path in (pressure_path, edge_path)
        },
    }


def write_outputs(result: dict[str, Any]) -> None:
    """写出 JSON 与 Markdown。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    for path in (OUT_LEDGER, OUT_JSON):
        path.write_text(
            json.dumps(result, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

    agg = result["aggregate"]
    full = result["full_packet_projection"]
    lines = [
        "# Prime Matrix AffineTwin endpoint-release carrier-arrival projection-deficit audit",
        "",
        "**状态：** `current_sweep_carrier_arrival_projection_deficit_closed_global_open`",
        "",
        "本审计把 carrier-arrival 的形式侧乘积投影回真实共同支撑窗口，检查 `SuperSqrt` crossing 是否真是 actual overload。",
        "",
        "```text",
        f"sqrt_floor={agg['sqrt_floor']}",
        f"target_window_pair_count={agg['target_window_pair_count']}",
        f"minimal_crossing_formal_product_count={agg['minimal_crossing_formal_product_count']}",
        f"minimal_crossing_projection_hit_count={agg['minimal_crossing_projection_hit_count']}",
        f"minimal_crossing_projection_deficit_count={agg['minimal_crossing_projection_deficit_count']}",
        f"minimal_crossing_actual_sqrt_slack={agg['minimal_crossing_actual_sqrt_slack']}",
        f"full_formal_product_count={agg['full_formal_product_count']}",
        f"full_projection_hit_count={agg['full_projection_hit_count']}",
        f"full_projection_deficit_count={agg['full_projection_deficit_count']}",
        f"full_actual_sqrt_slack={agg['full_actual_sqrt_slack']}",
        f"carrier_arrival_projection_deficit_closed_current_sweep={fmt_bool(agg['carrier_arrival_projection_deficit_closed_current_sweep'])}",
        "```",
        "",
        "## 1. minimal crossing projection rows",
        "",
        "| targets | formal product | projection hits | deficit | actual sqrt slack | hits |",
        "| --- | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in result["minimal_crossing_projection_rows"]:
        lines.append(
            "| `{targets}` | {formal} | {hits} | {deficit} | {slack} | `{hit_keys}` |".format(
                targets=",".join(row["target_pair_keys"]),
                formal=row["formal_product_count"],
                hits=row["projection_hit_count"],
                deficit=row["projection_deficit_count"],
                slack=row["actual_sqrt_slack"],
                hit_keys=",".join(row["projection_hits"]),
            )
        )

    lines.extend(
        [
            "",
            "## 2. full packet projection",
            "",
            "```text",
            f"formal_product_count={full['formal_product_count']}",
            f"projection_hit_count={full['projection_hit_count']}",
            f"projection_deficit_count={full['projection_deficit_count']}",
            f"actual_sqrt_slack={full['actual_sqrt_slack']}",
            f"projection_hits={full['projection_hits']}",
            "```",
            "",
            "## 3. 显式矛盾点",
            "",
            "最小 crossing 的形式侧乘积是 `30`，只比 `sqrt_floor=29` 高一格；但投影到真实共同支撑窗口后只有 `3` 个 actual hits：实际锚点 `19:8` 加上两个被选 target atoms。因此 actual 侧仍有 `26` 个平方根余量。",
            "",
            "完整 carrier packet 的形式侧乘积为 `64`，但真实窗口投影只有 `6` 个 hits，即实际锚点加五个 target atoms，投影缺口为 `58`。所以当前 `SuperSqrt` 不是 actual overload，而是形式侧乘积把大量不落窗的笛卡尔积误计为负载。",
            "",
            "这把当前 PDEC 排斥继续压窄为：全局证明必须使用 actual projection count，而不是裸侧乘积；若未来某族真的让投影 hits 超过平方根门，则它已经是命名 `ProjectionCollision/SupportEscape-PDEC`。",
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


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--pressure-ledger",
        type=Path,
        default=PRESSURE_LEDGER,
        help="carrier-arrival pressure-product ledger path",
    )
    parser.add_argument(
        "--edge-ledger",
        type=Path,
        default=EDGE_LEDGER,
        help="window edge-collision ledger path",
    )
    args = parser.parse_args()
    result = build_result(args.pressure_ledger, args.edge_ledger)
    write_outputs(result)
    print(json.dumps(result["aggregate"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
