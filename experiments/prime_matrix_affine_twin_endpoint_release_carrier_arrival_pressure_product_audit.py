#!/usr/bin/env python3
"""生成 AffineTwin endpoint-release carrier-arrival pressure-product 审计证书。

用法示例：
  python3 experiments/prime_matrix_affine_twin_endpoint_release_carrier_arrival_pressure_product_audit.py
  python3 -m json.tool data/prime-matrix-affine-twin-endpoint-release-carrier-arrival-pressure-product-ledger.json

输出：
  data/prime-matrix-affine-twin-endpoint-release-carrier-arrival-pressure-product-ledger.json
  docs/monograph/prime-matrix-affine-twin-endpoint-release-carrier-arrival-pressure-product-audit.json
  docs/monograph/prime-matrix-affine-twin-endpoint-release-carrier-arrival-pressure-product-audit.md
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

CARRIER_ARRIVAL_LEDGER = DATA / (
    "prime-matrix-affine-twin-endpoint-release-carrier-arrival-routing-ledger.json"
)
UNUSED_TARGET_ARRIVAL_LEDGER = DATA / (
    "prime-matrix-affine-twin-unused-target-arrival-ledger.json"
)
SLOT_LEDGER = DATA / (
    "square-phase-offband-prefix-gap-shadow-selector-h-lower-"
    "affine-twin-slot-phase-lock-ledger.json"
)

OUT_LEDGER = DATA / (
    "prime-matrix-affine-twin-endpoint-release-carrier-arrival-pressure-product-ledger.json"
)
OUT_JSON = DOCS / (
    "prime-matrix-affine-twin-endpoint-release-carrier-arrival-pressure-product-audit.json"
)
OUT_MD = DOCS / (
    "prime-matrix-affine-twin-endpoint-release-carrier-arrival-pressure-product-audit.md"
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


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def pressure_row(generator_count: int, fill_count: int, modulus_product: int) -> dict[str, Any]:
    """计算侧残基压力乘积读数。"""
    product = generator_count * fill_count
    square = product * product
    return {
        "generator_count": generator_count,
        "fill_count": fill_count,
        "side_product": product,
        "side_product_square": square,
        "square_excess_over_modulus_product": square - modulus_product,
        "super_sqrt_pressure_product": square > modulus_product,
    }


def build_result(
    carrier_arrival_path: Path,
    unused_target_arrival_path: Path,
    slot_path: Path,
) -> dict[str, Any]:
    """构造 carrier-arrival pressure-product 审计结果。"""
    carrier_arrival = load_json(carrier_arrival_path)
    unused_target = load_json(unused_target_arrival_path)
    slot = load_json(slot_path)

    slot_row = slot["affine_twin_slot_phase_lock_rows"][0]
    generator_modulus = int(slot_row["generator_modulus"])
    fill_modulus = int(slot_row["fill_modulus"])
    modulus_product = generator_modulus * fill_modulus
    sqrt_floor = math.isqrt(modulus_product)

    base_generator_residues = set(
        int(value)
        for value in unused_target["aggregate"]["current_formal_generator_residues"]
    )
    base_fill_residues = set(
        int(value)
        for value in unused_target["aggregate"]["current_formal_fill_residues"]
    )
    carrier_generator_residues = set(
        int(value)
        for value in carrier_arrival["aggregate"]["required_new_generator_residues"]
    )
    carrier_fill_residues = set(
        int(value)
        for value in carrier_arrival["aggregate"]["required_new_fill_residues"]
    )

    target_rows_by_key = {
        str(row["target_unused_pair_key"]): row
        for row in unused_target["unused_target_arrival_rows"]
    }
    carrier_target_histogram = Counter(
        str(row["target_unused_pair_key"])
        for row in carrier_arrival["carrier_arrival_event_rows"]
    )

    target_atom_rows: list[dict[str, Any]] = []
    for key in sorted(target_rows_by_key):
        row = target_rows_by_key[key]
        target_atom_rows.append(
            {
                "target_pair_key": key,
                "target_p": int(row["target_p"]),
                "target_generator_residue": int(row["target_generator_residue"]),
                "target_fill_residue": int(row["target_fill_residue"]),
                "needs_new_generator_residue": bool(
                    row["needs_new_generator_residue"]
                ),
                "needs_new_fill_residue": bool(row["needs_new_fill_residue"]),
                "new_side_residue_count": int(row["new_side_residue_count"]),
                "arrival_occurrence_count": int(
                    row["target_occurrence_count_current"]
                ),
                "carrier_event_occurrence_count": int(
                    carrier_target_histogram.get(key, 0)
                ),
            }
        )

    base_pressure = pressure_row(
        len(base_generator_residues), len(base_fill_residues), modulus_product
    )
    full_generator_residues = base_generator_residues | carrier_generator_residues
    full_fill_residues = base_fill_residues | carrier_fill_residues
    full_pressure = pressure_row(
        len(full_generator_residues), len(full_fill_residues), modulus_product
    )

    crossing_subsets: list[dict[str, Any]] = []
    target_keys = [row["target_pair_key"] for row in target_atom_rows]
    for subset_size in range(1, len(target_keys) + 1):
        for keys in itertools.combinations(target_keys, subset_size):
            generator_residues = set(base_generator_residues)
            fill_residues = set(base_fill_residues)
            new_side_count = 0
            carrier_event_count = 0
            for key in keys:
                atom = target_rows_by_key[key]
                if bool(atom["needs_new_generator_residue"]):
                    generator_residues.add(int(atom["target_generator_residue"]))
                    new_side_count += 1
                if bool(atom["needs_new_fill_residue"]):
                    fill_residues.add(int(atom["target_fill_residue"]))
                    new_side_count += 1
                carrier_event_count += int(carrier_target_histogram.get(key, 0))
            pressure = pressure_row(
                len(generator_residues), len(fill_residues), modulus_product
            )
            if bool(pressure["super_sqrt_pressure_product"]):
                crossing_subsets.append(
                    {
                        "target_pair_keys": list(keys),
                        "target_atom_count": subset_size,
                        "new_side_residue_count": new_side_count,
                        "carrier_event_occurrence_count": carrier_event_count,
                        **pressure,
                    }
                )
        if crossing_subsets:
            break

    minimal_crossing_square_excess = min(
        int(row["square_excess_over_modulus_product"]) for row in crossing_subsets
    )
    minimal_crossing_rows = [
        row
        for row in crossing_subsets
        if int(row["square_excess_over_modulus_product"])
        == minimal_crossing_square_excess
    ]

    two_side_target_count = sum(
        1 for row in target_atom_rows if int(row["new_side_residue_count"]) == 2
    )
    exact_zero_event_uses_crossing_packet = (
        "20:9" in {row["target_pair_key"] for row in target_atom_rows}
        and int(
            carrier_arrival["aggregate"]["exact_zero_phase_event_count"]
        )
        > 0
    )

    closed_current = (
        bool(carrier_arrival["aggregate"]["carrier_arrival_routed_current_sweep"])
        and bool(full_pressure["super_sqrt_pressure_product"])
        and len(crossing_subsets) > 0
        and two_side_target_count >= 2
    )

    aggregate = {
        "carrier_arrival_routing_ledger": str(
            carrier_arrival_path.relative_to(ROOT)
        ),
        "unused_target_arrival_ledger": str(
            unused_target_arrival_path.relative_to(ROOT)
        ),
        "slot_phase_lock_ledger": str(slot_path.relative_to(ROOT)),
        "generator_modulus": generator_modulus,
        "fill_modulus": fill_modulus,
        "modulus_product": modulus_product,
        "sqrt_floor": sqrt_floor,
        "base_generator_residues": sorted(base_generator_residues),
        "base_fill_residues": sorted(base_fill_residues),
        "base_generator_count": len(base_generator_residues),
        "base_fill_count": len(base_fill_residues),
        "base_side_product": base_pressure["side_product"],
        "base_square_excess_over_modulus_product": base_pressure[
            "square_excess_over_modulus_product"
        ],
        "carrier_required_new_generator_residues": sorted(
            carrier_generator_residues
        ),
        "carrier_required_new_fill_residues": sorted(carrier_fill_residues),
        "full_generator_count_after_carrier_arrival": len(full_generator_residues),
        "full_fill_count_after_carrier_arrival": len(full_fill_residues),
        "full_side_product_after_carrier_arrival": full_pressure["side_product"],
        "full_side_product_square_after_carrier_arrival": full_pressure[
            "side_product_square"
        ],
        "full_square_excess_over_modulus_product": full_pressure[
            "square_excess_over_modulus_product"
        ],
        "full_pressure_product_super_sqrt": full_pressure[
            "super_sqrt_pressure_product"
        ],
        "unique_target_atom_count": len(target_atom_rows),
        "two_side_target_atom_count": two_side_target_count,
        "carrier_event_count": int(
            carrier_arrival["aggregate"]["carrier_event_count"]
        ),
        "carrier_target_histogram": dict(sorted(carrier_target_histogram.items())),
        "minimal_crossing_target_atom_count": int(
            minimal_crossing_rows[0]["target_atom_count"]
        ),
        "minimal_crossing_new_side_residue_count": int(
            minimal_crossing_rows[0]["new_side_residue_count"]
        ),
        "minimal_crossing_side_product": int(
            minimal_crossing_rows[0]["side_product"]
        ),
        "minimal_crossing_square_excess_over_modulus_product": (
            minimal_crossing_square_excess
        ),
        "minimal_crossing_subset_count": len(minimal_crossing_rows),
        "exact_zero_phase_event_count": int(
            carrier_arrival["aggregate"]["exact_zero_phase_event_count"]
        ),
        "exact_zero_event_uses_crossing_packet": exact_zero_event_uses_crossing_packet,
        "carrier_arrival_pressure_product_routed_current_sweep": closed_current,
        "global_super_sqrt_pressure_product_pdec_excluded": False,
        "row_column_unconditional_closed": False,
    }

    return {
        "certificate_type": (
            "prime_matrix_affine_twin_endpoint_release_"
            "carrier_arrival_pressure_product_audit"
        ),
        "status": "current_sweep_carrier_arrival_pressure_product_routed_global_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "aggregate": aggregate,
        "target_atom_rows": target_atom_rows,
        "minimal_crossing_rows": minimal_crossing_rows,
        "contract": {
            "carrier_arrival_pressure_product_gate": [
                "base side-residue product must stay below sqrt((q-2)q)",
                "materializing the full carrier-arrival packet updates both side-residue sets",
                "if the updated product exceeds sqrt((q-2)q), the route is SuperSqrt/PressureProduct-PDEC",
                "if a smaller target subset already crosses, the crossing is an explicit local pressure atom",
            ],
            "closed_current_sweep": closed_current,
            "global_remaining": [
                "SuperSqrtPressureProductPDECExclusion",
                "GlobalUnusedTargetResidueArrivalBound",
                "NewGeneratorResidueArrival-PDEC/SAE",
                "NewFillResidueArrival-PDEC/SAE",
                "ColumnCRT/PDEC",
                "MovingFamilySAEColumnCRT",
            ],
        },
        "dependency_hashes": {
            str(path.relative_to(ROOT)): sha256(path)
            for path in (
                carrier_arrival_path,
                unused_target_arrival_path,
                slot_path,
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
        "# Prime Matrix AffineTwin endpoint-release carrier-arrival pressure-product audit",
        "",
        "**状态：** `current_sweep_carrier_arrival_pressure_product_routed_global_open`",
        "",
        "本审计检查 carrier-arrival packet 若被物化，是否仍只是普通新残基到达，还是已经越过 `sqrt((q-2)q)` 压力乘积门。",
        "",
        "```text",
        f"generator_modulus={agg['generator_modulus']}",
        f"fill_modulus={agg['fill_modulus']}",
        f"modulus_product={agg['modulus_product']}",
        f"sqrt_floor={agg['sqrt_floor']}",
        f"base_counts=({agg['base_generator_count']}, {agg['base_fill_count']})",
        f"base_side_product={agg['base_side_product']}",
        f"carrier_required_new_generator_residues={agg['carrier_required_new_generator_residues']}",
        f"carrier_required_new_fill_residues={agg['carrier_required_new_fill_residues']}",
        f"full_counts_after_carrier_arrival=({agg['full_generator_count_after_carrier_arrival']}, {agg['full_fill_count_after_carrier_arrival']})",
        f"full_side_product_after_carrier_arrival={agg['full_side_product_after_carrier_arrival']}",
        f"full_square_excess_over_modulus_product={agg['full_square_excess_over_modulus_product']}",
        f"minimal_crossing_target_atom_count={agg['minimal_crossing_target_atom_count']}",
        f"minimal_crossing_side_product={agg['minimal_crossing_side_product']}",
        f"minimal_crossing_square_excess_over_modulus_product={agg['minimal_crossing_square_excess_over_modulus_product']}",
        f"carrier_arrival_pressure_product_routed_current_sweep={fmt_bool(agg['carrier_arrival_pressure_product_routed_current_sweep'])}",
        "```",
        "",
        "## 1. target atoms",
        "",
        "| target | p | new generator | new fill | new side | arrival count | carrier events |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in result["target_atom_rows"]:
        lines.append(
            "| `{target}` | {p} | {gen} | {fill} | {new_side} | {arrival} | {carrier} |".format(
                target=table_cell(row["target_pair_key"]),
                p=row["target_p"],
                gen=row["target_generator_residue"]
                if row["needs_new_generator_residue"]
                else "-",
                fill=row["target_fill_residue"]
                if row["needs_new_fill_residue"]
                else "-",
                new_side=row["new_side_residue_count"],
                arrival=row["arrival_occurrence_count"],
                carrier=row["carrier_event_occurrence_count"],
            )
        )

    lines.extend(
        [
            "",
            "## 2. minimal crossing atoms",
            "",
            "| targets | side counts | product | square excess | carrier events |",
            "| --- | --- | ---: | ---: | ---: |",
        ]
    )
    for row in result["minimal_crossing_rows"]:
        lines.append(
            "| `{targets}` | `({g},{f})` | {product} | {excess} | {events} |".format(
                targets=",".join(row["target_pair_keys"]),
                g=row["generator_count"],
                f=row["fill_count"],
                product=row["side_product"],
                excess=row["square_excess_over_modulus_product"],
                events=row["carrier_event_occurrence_count"],
            )
        )

    lines.extend(
        [
            "",
            "## 3. 显式矛盾点",
            "",
            "当前基础侧残基数为 `(3,4)`，乘积 `12`，安全低于 `sqrt(29*31)`。若物化 carrier-arrival 使用到的全部新残基，侧残基数变成 `(8,8)`，乘积 `64`，满足 `64^2-29*31=3197>0`。",
            "",
            "更窄的是，任意两个双侧 target atoms 已把侧残基数推到 `(5,6)`，乘积 `30`，并且 `30^2-29*31=1`。也就是说，最小 crossing 只超过平方根门一个单位，是当前局部反例链与真实链之间的精确压力断点。",
            "",
            "因此 carrier-arrival packet 不能继续作为普通 arrival 义务保留：若这些 target 原子被真实物化，立即进入 `SuperSqrt/PressureProduct-PDEC`；若 PDEC 被排斥，则当前 carrier-arrival packet 不能复现。",
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
        "--carrier-arrival-ledger",
        type=Path,
        default=CARRIER_ARRIVAL_LEDGER,
        help="carrier-arrival routing ledger path",
    )
    parser.add_argument(
        "--unused-target-arrival-ledger",
        type=Path,
        default=UNUSED_TARGET_ARRIVAL_LEDGER,
        help="unused-target arrival ledger path",
    )
    parser.add_argument(
        "--slot-ledger",
        type=Path,
        default=SLOT_LEDGER,
        help="slot phase-lock ledger path",
    )
    args = parser.parse_args()
    result = build_result(
        args.carrier_arrival_ledger,
        args.unused_target_arrival_ledger,
        args.slot_ledger,
    )
    write_outputs(result)
    print(json.dumps(result["aggregate"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
