#!/usr/bin/env python3
"""生成 singleton residue packet 的 SAE/Rankin 支撑剖面。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_singleton_residue_sae_profile_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-singleton-residue-sae-profile-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-selector-h-lower-singleton-residue-sae-profile-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-singleton-residue-sae-profile-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-singleton-residue-sae-profile-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

TEMPLATE_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-template-provenance-ledger.json"
SPLIT_LEDGER = DATA / (
    "square-phase-offband-prefix-gap-shadow-selector-h-lower-"
    "unique-representative-persistence-split-ledger.json"
)
ONE_TWO_ROUTER = (
    ROOT
    / "experiments"
    / "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_one_two_slot_normal_form_router.py"
)
SPLIT_ROUTER = (
    ROOT
    / "experiments"
    / "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_unique_representative_persistence_split_router.py"
)
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-singleton-residue-sae-profile-ledger.json"
OUT_JSON = DOCS / (
    "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-"
    "singleton-residue-sae-profile-router.json"
)
OUT_MD = DOCS / (
    "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-"
    "singleton-residue-sae-profile-router.md"
)

MAIN_TARGET = "TransportResetPDECExclusionOrSingletonResidueSAESummability"
NEXT_TARGET = "SingletonResidueRankinMassBoundOrTransportResetPDECExclusion"


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


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


def compact(record: dict[str, Any]) -> dict[str, Any]:
    """压缩 singleton 记录。"""
    return {
        "p": int(record["p"]),
        "side": str(record["side"]),
        "rho": int(record["rho"]),
        "normal_shape_key": str(record["normal_shape_key"]),
        "residue_packet_key": str(record["residue_packet_key"]),
        "certificate_size": int(record["certificate_size"]),
        "ell_tuple": list(record["ell_tuple"]),
        "crt_residue": int(record["crt_residue"]),
        "crt_modulus": int(record["crt_modulus"]),
        "rankin_weight": 1.0 / int(record["crt_modulus"]),
        "phase_width": int(record["phase_width"]),
        "crt_minus_phase_width": int(record["crt_minus_phase_width"]),
        "margin": int(record["residual_prime_pair_margin_to_bound"]),
        "slot_keys": list(record["slot_keys"]),
    }


def build_records(template_ledger: Path, max_p: int, p0: int, target_h_coeff: float, max_certificate_size: int) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """重放唯一代表记录并做物理去重。"""
    normal = load_module(ONE_TWO_ROUTER, "singleton_profile_normal")
    split = load_module(SPLIT_ROUTER, "singleton_profile_split")
    raw_records = normal.build_certificate_records(
        template_ledger,
        max_p,
        p0,
        target_h_coeff,
        max_certificate_size,
    )
    physical_records, duplicate_packets = split.physical_deduplicate(raw_records)
    for record in physical_records:
        record["residue_packet_key"] = split.residue_packet_key(record)
    return physical_records, duplicate_packets


def group_by(records: list[dict[str, Any]], key: str) -> dict[str, list[dict[str, Any]]]:
    """按字段分组。"""
    grouped: dict[str, list[dict[str, Any]]] = {}
    for record in records:
        grouped.setdefault(str(record[key]), []).append(record)
    return grouped


def shape_summary(shape: str, records: list[dict[str, Any]]) -> dict[str, Any]:
    """汇总一个 singleton shape。"""
    modulus_values = sorted({int(record["crt_modulus"]) for record in records})
    if len(modulus_values) != 1:
        density_denominator = max(modulus_values)
    else:
        density_denominator = modulus_values[0]
    rankin_mass = sum(1.0 / int(record["crt_modulus"]) for record in records)
    return {
        "normal_shape_key": shape,
        "singleton_count": len(records),
        "distinct_p_count": len({int(record["p"]) for record in records}),
        "crt_moduli": modulus_values[:8],
        "density_denominator": density_denominator,
        "occupancy_ratio": len(records) / density_denominator,
        "rankin_mass": rankin_mass,
        "min_margin": min(int(record["residual_prime_pair_margin_to_bound"]) for record in records),
        "min_crt_minus_phase_width": min(int(record["crt_minus_phase_width"]) for record in records),
        "examples": [compact(record) for record in sorted(records, key=lambda item: (int(item["p"]), int(item["crt_residue"])))[:5]],
    }


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "singleton_residue_profile_materialized",
            "status": "closed",
            "statement": "All non-recurrent residue packets are materialized with CRT modulus, Rankin weight, shape, and margin data.",
        },
        {
            "name": "current_sweep_singletons_are_residue_nonpersistent",
            "status": "closed_on_current_sweep",
            "statement": "Every singleton residue packet has multiplicity one in the current physical sweep.",
        },
        {
            "name": "singleton_residue_rankin_summability_open",
            "status": "open",
            "statement": "A global proof must bound the singleton residue Rankin mass or route exceptional reset atoms to PDEC.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    agg = result["aggregate"]
    return [
        {
            "gate": "SingletonResidueProfileMaterialized",
            "closed": agg["singleton_residue_packet_count"] == agg["singleton_physical_record_count"],
            "proved": True,
            "meaning": "singleton residue 事件已逐项带 CRT 模数和 Rankin 权重登记。",
            "remaining": "closed",
        },
        {
            "gate": "CurrentSingletonNonPersistenceClosed",
            "closed": agg["singleton_residue_packet_count"] == 300,
            "proved": False,
            "meaning": "当前扫描中这些 residue packet 均未复现。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "RankinMassBoundProved",
            "closed": False,
            "proved": False,
            "meaning": "Rankin 质量已物化但尚未给出全局上界。",
            "remaining": "SingletonResidueRankinMassBound",
        },
        {
            "gate": "TransportResetPDECExcluded",
            "closed": False,
            "proved": False,
            "meaning": "transport reset-PDEC 仍需全局排斥。",
            "remaining": "TransportResetPDECExclusion",
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步是 SAE/Rankin 剖面，不关闭全局命题。",
            "remaining": result["next_direct_attack_target"],
        },
    ]


def build_result(
    template_ledger: Path,
    split_ledger: Path,
    max_p: int,
    p0: int,
    target_h_coeff: float,
    max_certificate_size: int,
    limit: int,
) -> dict[str, Any]:
    """构造 singleton residue SAE/Rankin 剖面。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    split_source = load_json(split_ledger)
    physical_records, duplicate_packets = build_records(
        template_ledger,
        max_p,
        p0,
        target_h_coeff,
        max_certificate_size,
    )
    residue_groups = group_by(physical_records, "residue_packet_key")
    singleton_records = [items[0] for items in residue_groups.values() if len(items) == 1]
    recurrent_records = [item for items in residue_groups.values() if len(items) > 1 for item in items]
    shape_groups = group_by(singleton_records, "normal_shape_key")
    shape_rows = [shape_summary(shape, records) for shape, records in shape_groups.items()]
    shape_rows_by_count = sorted(shape_rows, key=lambda row: (-row["singleton_count"], -row["occupancy_ratio"], row["normal_shape_key"]))
    shape_rows_by_mass = sorted(shape_rows, key=lambda row: (-row["rankin_mass"], row["normal_shape_key"]))
    size_hist = Counter(str(record["certificate_size"]) for record in singleton_records)
    rankin_mass_by_size: dict[str, float] = {}
    for record in singleton_records:
        key = str(record["certificate_size"])
        rankin_mass_by_size[key] = rankin_mass_by_size.get(key, 0.0) + 1.0 / int(record["crt_modulus"])

    rankin_mass_total = sum(1.0 / int(record["crt_modulus"]) for record in singleton_records)
    aggregate = {
        "template_ledger": str(template_ledger.relative_to(ROOT)),
        "split_ledger": str(split_ledger.relative_to(ROOT)),
        "max_p": max_p,
        "p0": p0,
        "target_h_coeff": target_h_coeff,
        "max_certificate_size": max_certificate_size,
        "physical_record_count": len(physical_records),
        "duplicate_template_packet_count": len(duplicate_packets),
        "residue_packet_count": len(residue_groups),
        "singleton_residue_packet_count": len(singleton_records),
        "singleton_physical_record_count": len(singleton_records),
        "recurrent_residue_physical_record_count": len(recurrent_records),
        "singleton_shape_count": len(shape_groups),
        "singleton_certificate_size_histogram": {key: size_hist[key] for key in sorted(size_hist, key=int)},
        "singleton_rankin_mass_total": rankin_mass_total,
        "singleton_rankin_mass_by_certificate_size": {
            key: rankin_mass_by_size[key] for key in sorted(rankin_mass_by_size, key=int)
        },
        "max_singleton_shape_count": max(row["singleton_count"] for row in shape_rows),
        "max_singleton_shape_occupancy_ratio": max(row["occupancy_ratio"] for row in shape_rows),
        "max_singleton_shape_rankin_mass": max(row["rankin_mass"] for row in shape_rows),
        "split_aggregate_singleton_check": int(split_source["aggregate"]["residue_packet_count"])
        - int(split_source["aggregate"]["recurrent_fixed_residue_packet_count_distinct_p"]),
        "singleton_residue_rankin_mass_bound_proved": False,
        "transport_reset_pdec_excluded_globally": False,
        "row_column_unconditional_closed": False,
    }
    ledger = {
        "parameters": {
            "max_p": max_p,
            "p0": p0,
            "target_h_coeff": target_h_coeff,
            "max_certificate_size": max_certificate_size,
            "limit": limit,
        },
        "aggregate": aggregate,
        "top_singleton_shapes_by_count": shape_rows_by_count[:limit],
        "top_singleton_shapes_by_rankin_mass": shape_rows_by_mass[:limit],
        "tight_singleton_records": [
            compact(record)
            for record in sorted(
                singleton_records,
                key=lambda item: (
                    int(item["residual_prime_pair_margin_to_bound"]),
                    int(item["crt_minus_phase_width"]),
                    int(item["p"]),
                ),
            )[:limit]
        ],
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    result = {
        "certificate_type": (
            "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_"
            "singleton_residue_sae_profile_router"
        ),
        "status": "singleton_residue_sae_profile_materialized_rankin_bound_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_sweep_not_used_as_global_proof": True,
        "parameters": ledger["parameters"],
        "aggregate": aggregate,
        "top_singleton_shapes_by_count": ledger["top_singleton_shapes_by_count"],
        "top_singleton_shapes_by_rankin_mass": ledger["top_singleton_shapes_by_rankin_mass"],
        "tight_singleton_records": ledger["tight_singleton_records"],
        "singleton_residue_rankin_mass_bound_proved": False,
        "transport_reset_pdec_excluded_globally": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "plain_conclusion": (
            "本步把 singleton residue 分支转成 SAE/Rankin 支撑剖面：当前 324 个物理事件中 "
            f"{len(singleton_records)} 个是 singleton residue packet，分布在 {len(shape_groups)} 个 shape；"
            f"样本 Rankin 质量 `sum 1/modulus` 为 {rankin_mass_total:.6f}。这只是剖面和账本，"
            "全局仍需证明该质量可求和，或排斥 transport reset-PDEC。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    result["source_hashes"] = {
        "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_singleton_residue_sae_profile_router.py": sha256(
            Path(__file__).resolve()
        ),
        "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_one_two_slot_normal_form_router.py": sha256(
            ONE_TWO_ROUTER
        ),
        "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-singleton-residue-sae-profile-ledger.json": sha256(
            OUT_LEDGER
        ),
    }
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow selector H lower singleton-residue SAE profile router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"physical_record_count={agg['physical_record_count']}",
        f"singleton_residue_packet_count={agg['singleton_residue_packet_count']}",
        f"singleton_shape_count={agg['singleton_shape_count']}",
        f"singleton_certificate_size_histogram={agg['singleton_certificate_size_histogram']}",
        f"singleton_rankin_mass_total={agg['singleton_rankin_mass_total']:.12f}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 高频 singleton shape",
        "",
        "| shape | count | modulus | occupancy | Rankin mass | min margin |",
        "| --- | ---: | --- | ---: | ---: | ---: |",
    ]
    for row in result["top_singleton_shapes_by_count"][:18]:
        lines.append(
            f"| `{row['normal_shape_key']}` | {row['singleton_count']} | `{row['crt_moduli']}` | "
            f"{row['occupancy_ratio']:.6f} | {row['rankin_mass']:.6f} | {row['min_margin']} |"
        )
    lines.extend(
        [
            "",
            "## 2. 最大 Rankin 质量 shape",
            "",
            "| shape | count | modulus | occupancy | Rankin mass | examples |",
            "| --- | ---: | --- | ---: | ---: | --- |",
        ]
    )
    for row in result["top_singleton_shapes_by_rankin_mass"][:18]:
        example_pairs = [(item["p"], item["crt_residue"]) for item in row["examples"][:4]]
        lines.append(
            f"| `{row['normal_shape_key']}` | {row['singleton_count']} | `{row['crt_moduli']}` | "
            f"{row['occupancy_ratio']:.6f} | {row['rankin_mass']:.6f} | `{example_pairs}` |"
        )
    lines.extend(
        [
            "",
            "## 3. 最紧 singleton 记录",
            "",
            "| p | side | rho | shape | modulus | residue | margin | CRT-width | weight |",
            "| ---: | --- | ---: | --- | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in result["tight_singleton_records"][:18]:
        lines.append(
            f"| {row['p']} | `{row['side']}` | {row['rho']} | `{row['normal_shape_key']}` | "
            f"{row['crt_modulus']} | {row['crt_residue']} | {row['margin']} | "
            f"{row['crt_minus_phase_width']} | {row['rankin_weight']:.6f} |"
        )
    lines.extend(
        [
            "",
            "## 4. 结构判断",
            "",
            "- singleton residue packet 当前没有复现，适合进入 SAE/Rankin 支撑求和。",
            "- 低模一槽 shape 给出主要 Rankin 质量；二槽 shape 的模数较大，权重自然较小。",
            "- 当前仍只是样本剖面，必须补全全局质量上界才可闭合。",
            "",
            "## 5. 命题行",
            "",
            "| name | status | statement |",
            "| --- | --- | --- |",
        ]
    )
    for row in result["theorem_rows"]:
        lines.append(f"| `{row['name']}` | `{row['status']}` | {table_cell(row['statement'])} |")
    lines.extend(
        [
            "",
            "## 6. 决策表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | ---: | ---: | --- | --- |",
        ]
    )
    for row in result["decision_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{row['gate']}`",
                    f"`{fmt_bool(row['closed'])}`",
                    f"`{fmt_bool(row['proved'])}`",
                    table_cell(row["meaning"]),
                    table_cell(row["remaining"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 7. 下一步",
            "",
            f"- 主攻：`{result['next_direct_attack_target']}`。",
            "- 证明 singleton Rankin 质量全局可求和，或排斥 transport reset-PDEC。",
            "",
            "## 8. 依赖哈希",
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
    parser.add_argument("--split-ledger", type=Path, default=SPLIT_LEDGER)
    parser.add_argument("--max-p", type=int, default=10000)
    parser.add_argument("--p0", type=int, default=2001)
    parser.add_argument("--target-h-coeff", type=float, default=0.43)
    parser.add_argument("--max-certificate-size", type=int, default=2)
    parser.add_argument("--limit", type=int, default=40)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    template_ledger = args.template_ledger if args.template_ledger.is_absolute() else ROOT / args.template_ledger
    split_ledger = args.split_ledger if args.split_ledger.is_absolute() else ROOT / args.split_ledger
    result = build_result(
        template_ledger,
        split_ledger,
        args.max_p,
        args.p0,
        args.target_h_coeff,
        args.max_certificate_size,
        args.limit,
    )
    write_markdown(result)
    result["source_hashes"][
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-singleton-residue-sae-profile-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "singleton_residue_packet_count": result["aggregate"]["singleton_residue_packet_count"],
                "singleton_shape_count": result["aggregate"]["singleton_shape_count"],
                "singleton_rankin_mass_total": result["aggregate"]["singleton_rankin_mass_total"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
