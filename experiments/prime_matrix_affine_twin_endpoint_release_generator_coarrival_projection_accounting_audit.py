#!/usr/bin/env python3
"""生成 AffineTwin endpoint-release generator-coarrival projection-accounting 审计证书。

用法示例：
  python3 experiments/prime_matrix_affine_twin_endpoint_release_generator_coarrival_projection_accounting_audit.py
  python3 -m json.tool data/prime-matrix-affine-twin-endpoint-release-generator-coarrival-projection-accounting-ledger.json

输出：
  data/prime-matrix-affine-twin-endpoint-release-generator-coarrival-projection-accounting-ledger.json
  docs/monograph/prime-matrix-affine-twin-endpoint-release-generator-coarrival-projection-accounting-audit.json
  docs/monograph/prime-matrix-affine-twin-endpoint-release-generator-coarrival-projection-accounting-audit.md
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

FILL_GATE_LEDGER = DATA / (
    "prime-matrix-affine-twin-endpoint-release-fill-arrival-projection-gate-ledger.json"
)
PRESSURE_LEDGER = DATA / (
    "prime-matrix-affine-twin-endpoint-release-carrier-arrival-pressure-product-ledger.json"
)
PROJECTION_LEDGER = DATA / (
    "prime-matrix-affine-twin-endpoint-release-carrier-arrival-projection-deficit-ledger.json"
)
SUPPORT_GRAPH_LEDGER = DATA / (
    "prime-matrix-affine-twin-endpoint-release-support-graph-cap-ledger.json"
)
UNUSED_TARGET_LEDGER = DATA / "prime-matrix-affine-twin-unused-target-arrival-ledger.json"
MOVING_FAMILY_LEDGER = DATA / (
    "prime-matrix-affine-twin-endpoint-release-moving-family-persistence-pressure-ledger.json"
)

OUT_LEDGER = DATA / (
    "prime-matrix-affine-twin-endpoint-release-generator-coarrival-"
    "projection-accounting-ledger.json"
)
OUT_JSON = DOCS / (
    "prime-matrix-affine-twin-endpoint-release-generator-coarrival-"
    "projection-accounting-audit.json"
)
OUT_MD = DOCS / (
    "prime-matrix-affine-twin-endpoint-release-generator-coarrival-"
    "projection-accounting-audit.md"
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


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def product_pairs(
    generator_residues: set[int],
    fill_residues: set[int],
) -> set[tuple[int, int]]:
    """生成两侧残基笛卡尔积。"""
    return set(itertools.product(generator_residues, fill_residues))


def subset_row(
    keys: tuple[str, ...],
    target_atoms: dict[str, dict[str, Any]],
    base_generator_residues: set[int],
    base_fill_residues: set[int],
    target_window_pairs: set[tuple[int, int]],
    actual_anchor_pair: tuple[int, int],
    sqrt_floor: int,
) -> dict[str, Any]:
    """计算一个共到达子集的形式乘积与 actual 投影。"""
    generator_residues = set(base_generator_residues)
    fill_residues = set(base_fill_residues)
    selected_pairs = {parse_pair_key(key) for key in keys}
    new_generator_residues: set[int] = set()
    new_fill_residues: set[int] = set()

    for key in keys:
        atom = target_atoms[key]
        if bool(atom["needs_new_generator_residue"]):
            residue = int(atom["target_generator_residue"])
            generator_residues.add(residue)
            new_generator_residues.add(residue)
        if bool(atom["needs_new_fill_residue"]):
            residue = int(atom["target_fill_residue"])
            fill_residues.add(residue)
            new_fill_residues.add(residue)

    formal_pairs = product_pairs(generator_residues, fill_residues)
    projection_hits = formal_pairs & target_window_pairs
    expected_hits = selected_pairs | {actual_anchor_pair}
    projection_hit_keys = [pair_key(pair) for pair in sorted(projection_hits)]
    expected_hit_keys = [pair_key(pair) for pair in sorted(expected_hits)]
    formal_product_count = len(formal_pairs)
    projection_hit_count = len(projection_hits)

    return {
        "target_pair_keys": list(keys),
        "target_atom_count": len(keys),
        "new_generator_residues": sorted(new_generator_residues),
        "new_fill_residues": sorted(new_fill_residues),
        "new_generator_residue_count": len(new_generator_residues),
        "new_fill_residue_count": len(new_fill_residues),
        "has_fill_arrival": len(new_fill_residues) > 0,
        "requires_generator_coarrival": len(new_fill_residues) > 0
        and len(new_generator_residues) > 0,
        "fill_only_arrival": len(new_fill_residues) > 0
        and len(new_generator_residues) == 0,
        "generator_count": len(generator_residues),
        "fill_count": len(fill_residues),
        "formal_product_count": formal_product_count,
        "formal_excess_over_sqrt_floor": formal_product_count - sqrt_floor,
        "projection_hit_count": projection_hit_count,
        "projection_deficit_count": formal_product_count - projection_hit_count,
        "actual_sqrt_slack": sqrt_floor - projection_hit_count,
        "projection_hits": projection_hit_keys,
        "expected_projection_hit_keys": expected_hit_keys,
        "projection_hits_equal_anchor_plus_selected_targets": (
            projection_hit_keys == expected_hit_keys
        ),
        "formal_super_sqrt": formal_product_count > sqrt_floor,
        "actual_overload": projection_hit_count > sqrt_floor,
    }


def build_result(
    fill_gate_path: Path,
    pressure_path: Path,
    projection_path: Path,
    support_graph_path: Path,
    unused_target_path: Path,
    moving_family_path: Path,
) -> dict[str, Any]:
    """构造 generator-coarrival projection-accounting 审计结果。"""
    fill_gate = load_json(fill_gate_path)
    pressure = load_json(pressure_path)
    projection = load_json(projection_path)
    support_graph = load_json(support_graph_path)
    unused_target = load_json(unused_target_path)
    moving_family = load_json(moving_family_path)

    pressure_agg = pressure["aggregate"]
    sqrt_floor = int(pressure_agg["sqrt_floor"])
    base_generator_residues = {
        int(value) for value in pressure_agg["base_generator_residues"]
    }
    base_fill_residues = {int(value) for value in pressure_agg["base_fill_residues"]}
    target_atoms = {
        str(row["target_pair_key"]): row for row in pressure["target_atom_rows"]
    }
    target_keys = sorted(target_atoms)
    target_window_pairs = {
        (
            int(row["generator_residue"]),
            int(row["fill_residue"]),
        )
        for row in support_graph["target_window_graph_rows"]
    }
    all_target_pairs = {parse_pair_key(key) for key in target_keys}
    full_projection_hits = {
        parse_pair_key(key) for key in projection["full_packet_projection"]["projection_hits"]
    }
    anchor_candidates = full_projection_hits - all_target_pairs
    if len(anchor_candidates) != 1:
        raise ValueError(f"expected one actual anchor, got {sorted(anchor_candidates)}")
    actual_anchor_pair = next(iter(anchor_candidates))

    subset_rows: list[dict[str, Any]] = []
    for size in range(1, len(target_keys) + 1):
        for keys in itertools.combinations(target_keys, size):
            subset_rows.append(
                subset_row(
                    keys,
                    target_atoms,
                    base_generator_residues,
                    base_fill_residues,
                    target_window_pairs,
                    actual_anchor_pair,
                    sqrt_floor,
                )
            )

    fill_arrival_rows = [row for row in subset_rows if row["has_fill_arrival"]]
    super_rows = [row for row in subset_rows if row["formal_super_sqrt"]]
    fill_super_rows = [
        row for row in fill_arrival_rows if row["formal_super_sqrt"]
    ]
    minimal_formal_product = min(
        int(row["formal_product_count"]) for row in fill_super_rows
    )
    minimal_coarrival_rows = [
        row
        for row in fill_super_rows
        if int(row["formal_product_count"]) == minimal_formal_product
    ]

    base_projection_hits = product_pairs(
        base_generator_residues, base_fill_residues
    ) & target_window_pairs
    full_packet = projection["full_packet_projection"]

    closed_current = (
        bool(
            fill_gate["aggregate"][
                "anonymous_fill_arrival_actual_overload_closed_current_sweep"
            ]
        )
        and bool(
            moving_family["aggregate"][
                "anonymous_moving_family_persistence_closed_current_sweep"
            ]
        )
        and bool(
            projection["aggregate"][
                "carrier_arrival_projection_deficit_closed_current_sweep"
            ]
        )
        and bool(support_graph["aggregate"]["support_graph_cap_closed_current_sweep"])
        and all(not row["fill_only_arrival"] for row in fill_arrival_rows)
        and all(not row["actual_overload"] for row in super_rows)
        and all(
            row["projection_hits_equal_anchor_plus_selected_targets"]
            for row in subset_rows
        )
    )

    aggregate = {
        "fill_arrival_projection_gate_ledger": str(fill_gate_path.relative_to(ROOT)),
        "carrier_arrival_pressure_product_ledger": str(pressure_path.relative_to(ROOT)),
        "carrier_arrival_projection_deficit_ledger": str(
            projection_path.relative_to(ROOT)
        ),
        "support_graph_cap_ledger": str(support_graph_path.relative_to(ROOT)),
        "unused_target_arrival_ledger": str(unused_target_path.relative_to(ROOT)),
        "moving_family_persistence_pressure_ledger": str(
            moving_family_path.relative_to(ROOT)
        ),
        "candidate_q_values": fill_gate["aggregate"]["candidate_q_values"],
        "realized_q_values": fill_gate["aggregate"]["realized_q_values"],
        "source_blocked_q_values": fill_gate["aggregate"]["source_blocked_q_values"],
        "q": int(pressure_agg["fill_modulus"]),
        "generator_modulus": int(pressure_agg["generator_modulus"]),
        "fill_modulus": int(pressure_agg["fill_modulus"]),
        "modulus_product": int(pressure_agg["modulus_product"]),
        "sqrt_floor": sqrt_floor,
        "actual_anchor_pair": pair_key(actual_anchor_pair),
        "base_generator_count": len(base_generator_residues),
        "base_fill_count": len(base_fill_residues),
        "base_formal_product_count": len(base_generator_residues)
        * len(base_fill_residues),
        "base_projection_hit_count": len(base_projection_hits),
        "base_actual_sqrt_slack": sqrt_floor - len(base_projection_hits),
        "target_atom_count": len(target_keys),
        "two_side_target_atom_count": int(pressure_agg["two_side_target_atom_count"]),
        "generator_only_target_atom_count": sum(
            1
            for atom in target_atoms.values()
            if bool(atom["needs_new_generator_residue"])
            and not bool(atom["needs_new_fill_residue"])
        ),
        "subset_count": len(subset_rows),
        "fill_arrival_subset_count": len(fill_arrival_rows),
        "fill_only_subset_count": sum(1 for row in fill_arrival_rows if row["fill_only_arrival"]),
        "generator_coarrival_subset_count": sum(
            1 for row in fill_arrival_rows if row["requires_generator_coarrival"]
        ),
        "formal_super_sqrt_subset_count": len(super_rows),
        "fill_arrival_formal_super_sqrt_subset_count": len(fill_super_rows),
        "actual_overload_subset_count": sum(1 for row in subset_rows if row["actual_overload"]),
        "minimal_coarrival_formal_product_count": minimal_formal_product,
        "minimal_coarrival_subset_count": len(minimal_coarrival_rows),
        "minimal_coarrival_projection_hit_count": int(
            minimal_coarrival_rows[0]["projection_hit_count"]
        ),
        "minimal_coarrival_projection_deficit_count": int(
            minimal_coarrival_rows[0]["projection_deficit_count"]
        ),
        "minimal_coarrival_actual_sqrt_slack": int(
            minimal_coarrival_rows[0]["actual_sqrt_slack"]
        ),
        "full_formal_product_count": int(full_packet["formal_product_count"]),
        "full_projection_hit_count": int(full_packet["projection_hit_count"]),
        "full_projection_deficit_count": int(full_packet["projection_deficit_count"]),
        "full_actual_sqrt_slack": int(full_packet["actual_sqrt_slack"]),
        "max_projection_hit_count_any_subset": max(
            int(row["projection_hit_count"]) for row in subset_rows
        ),
        "max_projection_hit_count_formal_super_sqrt": max(
            int(row["projection_hit_count"]) for row in super_rows
        ),
        "min_actual_sqrt_slack_formal_super_sqrt": min(
            int(row["actual_sqrt_slack"]) for row in super_rows
        ),
        "max_projection_deficit_formal_super_sqrt": max(
            int(row["projection_deficit_count"]) for row in super_rows
        ),
        "support_graph_cap": int(support_graph["aggregate"]["support_graph_cap"]),
        "support_graph_cap_slack_to_sqrt_floor": int(
            support_graph["aggregate"]["support_graph_cap_slack_to_sqrt_floor"]
        ),
        "all_fill_arrivals_require_generator_coarrival": all(
            row["requires_generator_coarrival"] for row in fill_arrival_rows
        ),
        "all_formal_super_sqrt_subsets_project_below_sqrt": all(
            not row["actual_overload"] for row in super_rows
        ),
        "all_projection_hits_are_anchor_plus_selected_targets": all(
            row["projection_hits_equal_anchor_plus_selected_targets"]
            for row in subset_rows
        ),
        "generator_coarrival_projection_accounting_closed_current_sweep": closed_current,
        "global_generator_coarrival_bound_proved": False,
        "global_product_accounting_tightening_proved": False,
        "row_column_unconditional_closed": False,
    }

    return {
        "certificate_type": (
            "prime_matrix_affine_twin_endpoint_release_"
            "generator_coarrival_projection_accounting_audit"
        ),
        "status": (
            "current_sweep_generator_coarrival_projection_accounting_"
            "closed_global_open"
        ),
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "aggregate": aggregate,
        "coarrival_atom_rows": [
            {
                "target_pair_key": key,
                "target_p": int(atom["target_p"]),
                "target_generator_residue": int(atom["target_generator_residue"]),
                "target_fill_residue": int(atom["target_fill_residue"]),
                "needs_new_generator_residue": bool(
                    atom["needs_new_generator_residue"]
                ),
                "needs_new_fill_residue": bool(atom["needs_new_fill_residue"]),
                "arrival_occurrence_count": int(atom["arrival_occurrence_count"]),
                "carrier_event_occurrence_count": int(
                    atom["carrier_event_occurrence_count"]
                ),
            }
            for key, atom in sorted(target_atoms.items())
        ],
        "minimal_coarrival_projection_rows": minimal_coarrival_rows,
        "all_coarrival_subset_rows": subset_rows,
        "contract": {
            "generator_coarrival_projection_accounting_gate": [
                "fill arrival in the realized packet is never fill-only",
                "every fill-arrival subset carries at least one new generator residue",
                "formal side-product crossings must be projected to the support graph",
                "current coarrival projections are exactly the actual anchor plus selected target atoms",
                "formal SuperSqrt without actual overload is product-accounting tightening, not a contradiction",
            ],
            "closed_current_sweep": closed_current,
            "global_remaining": [
                "GeneratorCoarrivalFamilyBound",
                "ProductAccountingTighteningGlobal",
                "SourceRematerialization-PDEC/SAE",
                "ColumnCRT/PDEC",
                "MovingFamilyPersistenceNoGo",
            ],
        },
        "dependency_hashes": {
            str(path.relative_to(ROOT)): sha256(path)
            for path in (
                fill_gate_path,
                pressure_path,
                projection_path,
                support_graph_path,
                unused_target_path,
                moving_family_path,
            )
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
    lines = [
        "# Prime Matrix AffineTwin endpoint-release generator-coarrival projection-accounting audit",
        "",
        "**状态：** `current_sweep_generator_coarrival_projection_accounting_closed_global_open`",
        "",
        "本审计继续压缩 `GeneratorCoarrivalBound`：当 realized `q=31` 的 fill arrival 被迫携带 generator 共到达时，形式侧乘积可以越过平方根门，但投影到 actual 支撑图像仍远低于平方根门。",
        "",
        "```text",
        f"realized_q_values={agg['realized_q_values']}",
        f"source_blocked_q_values={agg['source_blocked_q_values']}",
        f"sqrt_floor={agg['sqrt_floor']}",
        f"actual_anchor_pair={agg['actual_anchor_pair']}",
        f"base_formal_product_count={agg['base_formal_product_count']}",
        f"base_projection_hit_count={agg['base_projection_hit_count']}",
        f"fill_arrival_subset_count={agg['fill_arrival_subset_count']}",
        f"fill_only_subset_count={agg['fill_only_subset_count']}",
        f"formal_super_sqrt_subset_count={agg['formal_super_sqrt_subset_count']}",
        f"actual_overload_subset_count={agg['actual_overload_subset_count']}",
        f"minimal_coarrival_formal_product_count={agg['minimal_coarrival_formal_product_count']}",
        f"minimal_coarrival_projection_hit_count={agg['minimal_coarrival_projection_hit_count']}",
        f"minimal_coarrival_actual_sqrt_slack={agg['minimal_coarrival_actual_sqrt_slack']}",
        f"full_formal_product_count={agg['full_formal_product_count']}",
        f"full_projection_hit_count={agg['full_projection_hit_count']}",
        f"full_actual_sqrt_slack={agg['full_actual_sqrt_slack']}",
        f"generator_coarrival_projection_accounting_closed_current_sweep={fmt_bool(agg['generator_coarrival_projection_accounting_closed_current_sweep'])}",
        "```",
        "",
        "## 1. 共到达原子",
        "",
        "| pair | target p | g residue | f residue | new g | new f | carrier events |",
        "| --- | ---: | ---: | ---: | --- | --- | ---: |",
    ]
    for row in result["coarrival_atom_rows"]:
        lines.append(
            "| `{key}` | {p} | {g} | {f} | {new_g} | {new_f} | {events} |".format(
                key=row["target_pair_key"],
                p=row["target_p"],
                g=row["target_generator_residue"],
                f=row["target_fill_residue"],
                new_g=fmt_bool(row["needs_new_generator_residue"]),
                new_f=fmt_bool(row["needs_new_fill_residue"]),
                events=row["carrier_event_occurrence_count"],
            )
        )

    lines.extend(
        [
            "",
            "## 2. 最小 crossing 的 actual 投影",
            "",
            "| targets | new g | new f | formal product | actual hits | deficit | sqrt slack | hits |",
            "| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for row in result["minimal_coarrival_projection_rows"]:
        lines.append(
            "| `{targets}` | {new_g} | {new_f} | {formal} | {hits} | {deficit} | {slack} | `{hit_keys}` |".format(
                targets=",".join(row["target_pair_keys"]),
                new_g=row["new_generator_residue_count"],
                new_f=row["new_fill_residue_count"],
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
            "## 3. 显式矛盾读数",
            "",
            f"- `fill_arrival_subset_count={agg['fill_arrival_subset_count']}` 中没有 fill-only 子集；每个 fill arrival 都伴随 generator coarrival。",
            f"- 形式上越过平方根门的 `{agg['formal_super_sqrt_subset_count']}` 个子集，actual overload 数为 `{agg['actual_overload_subset_count']}`。",
            f"- 最小 crossing 的形式乘积为 `{agg['minimal_coarrival_formal_product_count']}`，但 actual hits 只有 `{agg['minimal_coarrival_projection_hit_count']}`，投影缺口 `{agg['minimal_coarrival_projection_deficit_count']}`。",
            f"- 全部 carrier packet 形式乘积为 `{agg['full_formal_product_count']}`，actual hits 只有 `{agg['full_projection_hit_count']}`，仍有 sqrt slack `{agg['full_actual_sqrt_slack']}`。",
            "",
            "## 4. 结论边界",
            "",
            "当前 sweep 中 generator coarrival 不能把 fill-arrival 分支变成 actual overload；它只把形式账本推高，然后被 support graph projection 收紧。",
            "",
            "这仍不是全局无条件证明。最新剩余是把该投影账本升格为族级 `GeneratorCoarrivalFamilyBound`，或把失败形态登记为 `ProductAccountingTighteningGlobal`、`SourceRematerialization-PDEC/SAE`、`ColumnCRT/PDEC` 与 moving-family persistence 出口。",
            "",
            "## 5. 依赖哈希",
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
    parser = argparse.ArgumentParser(
        description=(
            "生成 AffineTwin endpoint-release generator-coarrival "
            "projection-accounting 审计证书。"
        )
    )
    parser.add_argument("--fill-gate-ledger", type=Path, default=FILL_GATE_LEDGER)
    parser.add_argument("--pressure-ledger", type=Path, default=PRESSURE_LEDGER)
    parser.add_argument("--projection-ledger", type=Path, default=PROJECTION_LEDGER)
    parser.add_argument("--support-graph-ledger", type=Path, default=SUPPORT_GRAPH_LEDGER)
    parser.add_argument("--unused-target-ledger", type=Path, default=UNUSED_TARGET_LEDGER)
    parser.add_argument("--moving-family-ledger", type=Path, default=MOVING_FAMILY_LEDGER)
    return parser.parse_args()


def main() -> None:
    """入口。"""
    args = parse_args()
    result = build_result(
        args.fill_gate_ledger,
        args.pressure_ledger,
        args.projection_ledger,
        args.support_graph_ledger,
        args.unused_target_ledger,
        args.moving_family_ledger,
    )
    write_outputs(result)
    print(json.dumps(result["aggregate"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
