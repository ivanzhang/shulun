#!/usr/bin/env python3
"""拆分一/二槽唯一代表正规形的持久性来源。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_unique_representative_persistence_split_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-unique-representative-persistence-split-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-selector-h-lower-unique-representative-persistence-split-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-unique-representative-persistence-split-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-unique-representative-persistence-split-router.md
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
SUBCERT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-minimal-subcertificate-ledger.json"
ONE_TWO_ROUTER = (
    ROOT
    / "experiments"
    / "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_one_two_slot_normal_form_router.py"
)

OUT_LEDGER = DATA / (
    "square-phase-offband-prefix-gap-shadow-selector-h-lower-"
    "unique-representative-persistence-split-ledger.json"
)
OUT_JSON = DOCS / (
    "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-"
    "unique-representative-persistence-split-router.json"
)
OUT_MD = DOCS / (
    "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-"
    "unique-representative-persistence-split-router.md"
)

MAIN_TARGET = "UniqueRepresentativeOneTwoSlotPDECOrGlobalResidualPrimeMarginJump"
NEXT_TARGET = "UniqueRepresentativePersistenceSplitToFixedResiduePDECOrMovingResidueSAE"


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def load_module(path: Path, name: str) -> Any:
    """按路径加载模块。"""
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def physical_key(record: dict[str, Any]) -> tuple[Any, ...]:
    """同一物理事件只允许因模板索引重复一次。"""
    return (
        int(record["p"]),
        str(record["side"]),
        int(record["rho"]),
        str(record["normal_shape_key"]),
        int(record["crt_residue"]),
        int(record["crt_modulus"]),
        tuple(str(key) for key in record["slot_keys"]),
    )


def residue_packet_key(record: dict[str, Any]) -> str:
    """固定正规形与固定 CRT 残基组成一个 residue packet。"""
    return (
        f"{record['normal_shape_key']}|mod={int(record['crt_modulus'])}|"
        f"residue={int(record['crt_residue'])}"
    )


def slot_packet_key(record: dict[str, Any]) -> str:
    """固定正规形、残基和槽位组成更细的 fixed-slot packet。"""
    slots = ",".join(str(key) for key in record["slot_keys"])
    return f"{residue_packet_key(record)}|slots={slots}"


def compact_record(record: dict[str, Any]) -> dict[str, Any]:
    """保留持久性拆分所需字段。"""
    return {
        "p": int(record["p"]),
        "side": str(record["side"]),
        "rho": int(record["rho"]),
        "template_indices": list(record["template_indices"]),
        "template_multiplicity": int(record["template_multiplicity"]),
        "normal_shape_key": str(record["normal_shape_key"]),
        "residue_packet_key": residue_packet_key(record),
        "slot_packet_key": slot_packet_key(record),
        "certificate_size": int(record["certificate_size"]),
        "ell_tuple": list(record["ell_tuple"]),
        "slot_keys": list(record["slot_keys"]),
        "crt_residue": int(record["crt_residue"]),
        "crt_modulus": int(record["crt_modulus"]),
        "phase_p_lo": int(record["phase_p_lo"]),
        "phase_p_hi": int(record["phase_p_hi"]),
        "phase_width": int(record["phase_width"]),
        "crt_minus_phase_width": int(record["crt_minus_phase_width"]),
        "residual_prime_pair_margin_to_bound": int(record["residual_prime_pair_margin_to_bound"]),
        "left_depth": int(record["left_depth"]),
        "right_depth": int(record["right_depth"]),
    }


def physical_deduplicate(records: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """删除同一物理事件的模板重复，并登记被合并模板。"""
    grouped: dict[tuple[Any, ...], list[dict[str, Any]]] = {}
    for record in records:
        grouped.setdefault(physical_key(record), []).append(record)

    physical_records = []
    duplicate_packets = []
    for items in grouped.values():
        first = dict(sorted(items, key=lambda item: int(item["template_index"]))[0])
        template_indices = sorted(int(item["template_index"]) for item in items)
        first["template_indices"] = template_indices
        first["template_multiplicity"] = len(items)
        physical_records.append(first)
        if len(items) > 1:
            duplicate_packets.append(
                {
                    "p": int(first["p"]),
                    "side": str(first["side"]),
                    "rho": int(first["rho"]),
                    "normal_shape_key": str(first["normal_shape_key"]),
                    "crt_residue": int(first["crt_residue"]),
                    "crt_modulus": int(first["crt_modulus"]),
                    "slot_keys": list(first["slot_keys"]),
                    "template_indices": template_indices,
                    "template_multiplicity": len(items),
                }
            )

    return (
        sorted(
            physical_records,
            key=lambda record: (
                int(record["p"]),
                str(record["side"]),
                int(record["rho"]),
                str(record["normal_shape_key"]),
                int(record["crt_residue"]),
                int(record["crt_modulus"]),
                tuple(record["slot_keys"]),
            ),
        ),
        duplicate_packets,
    )


def group_records(records: list[dict[str, Any]], key_name: str) -> dict[str, list[dict[str, Any]]]:
    """按指定派生键分组。"""
    grouped: dict[str, list[dict[str, Any]]] = {}
    for record in records:
        if key_name == "shape":
            key = str(record["normal_shape_key"])
        elif key_name == "residue":
            key = residue_packet_key(record)
        elif key_name == "slot":
            key = slot_packet_key(record)
        else:
            raise ValueError(f"unknown key name: {key_name}")
        grouped.setdefault(key, []).append(record)
    return grouped


def packet_summary(key: str, records: list[dict[str, Any]]) -> dict[str, Any]:
    """汇总一个 shape/residue/slot 包。"""
    p_values = sorted({int(record["p"]) for record in records})
    residue_values = sorted({int(record["crt_residue"]) for record in records})
    slot_values = sorted({tuple(record["slot_keys"]) for record in records})
    template_multiplicity = sum(int(record["template_multiplicity"]) for record in records)
    return {
        "key": key,
        "physical_count": len(records),
        "template_multiplicity": template_multiplicity,
        "distinct_p_count": len(p_values),
        "p_values": p_values[:20],
        "min_p": min(p_values),
        "max_p": max(p_values),
        "distinct_residue_count": len(residue_values),
        "residue_values": residue_values[:20],
        "distinct_slot_packet_count": len(slot_values),
        "min_margin": min(int(record["residual_prime_pair_margin_to_bound"]) for record in records),
        "min_crt_minus_phase_width": min(int(record["crt_minus_phase_width"]) for record in records),
        "certificate_size_histogram": dict(
            sorted(Counter(str(record["certificate_size"]) for record in records).items())
        ),
        "examples": [
            compact_record(record)
            for record in sorted(
                records,
                key=lambda item: (
                    int(item["p"]),
                    str(item["side"]),
                    int(item["rho"]),
                    int(item["crt_residue"]),
                    int(item["crt_modulus"]),
                ),
            )[:6]
        ],
    }


def sorted_summaries(grouped: dict[str, list[dict[str, Any]]]) -> list[dict[str, Any]]:
    """按复现强度排序输出包摘要。"""
    rows = [packet_summary(key, records) for key, records in grouped.items()]
    return sorted(
        rows,
        key=lambda row: (
            -int(row["distinct_p_count"]),
            -int(row["physical_count"]),
            int(row["min_margin"]),
            str(row["key"]),
        ),
    )


def drift_summary(shape_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """筛出同 shape 但残基漂移的包。"""
    return [
        row
        for row in shape_rows
        if int(row["distinct_residue_count"]) > 1 or int(row["distinct_slot_packet_count"]) > 1
    ]


def fixed_residue_recurrences(residue_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """筛出跨不同 P 复现的固定残基包。"""
    return [row for row in residue_rows if int(row["distinct_p_count"]) > 1]


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "physical_deduplication_closed",
            "status": "closed",
            "statement": "Template-index multiplicity is quotiented by physical event keys before persistence is counted.",
        },
        {
            "name": "fixed_residue_vs_moving_residue_split_closed",
            "status": "closed_on_current_sweep",
            "statement": "Every unique-representative event is assigned to shape, fixed-residue packet, and fixed-slot packet ledgers.",
        },
        {
            "name": "persistent_packet_exclusion_open",
            "status": "open",
            "statement": "A global proof must exclude recurrent fixed-residue packets by ColumnCRT/PDEC or bound drifting residue shapes by SAE/Rankin.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    agg = result["aggregate"]
    return [
        {
            "gate": "PhysicalDeduplicationClosed",
            "closed": True,
            "proved": True,
            "meaning": "同一物理事件的模板索引重复已合并，不再把重复模板误判为复现。",
            "remaining": "closed",
        },
        {
            "gate": "FixedResidueMovingResidueSplitMaterialized",
            "closed": True,
            "proved": False,
            "meaning": "当前重放已拆成固定残基包与移动残基 shape，但仍是有限扫描证据。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "FixedResiduePacketsExcluded",
            "closed": False,
            "proved": False,
            "meaning": f"{agg['recurrent_fixed_residue_packet_count_distinct_p']} 个固定残基包跨不同 P 复现，需要 ColumnCRT/PDEC 排斥。",
            "remaining": "FixedResidueShapePDEC/ColumnCRT",
        },
        {
            "gate": "MovingResidueShapesBounded",
            "closed": False,
            "proved": False,
            "meaning": f"{agg['moving_residue_shape_count']} 个 shape 出现残基或槽漂移，需要 SAE/Rankin 或全局增长界。",
            "remaining": "MovingResidueShapeSAE/Rankin",
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只是持久性路由拆分，不关闭全局行/列命题。",
            "remaining": result["next_direct_attack_target"],
        },
    ]


def build_result(
    template_ledger: Path,
    subcert_ledger: Path,
    max_p: int,
    p0: int,
    target_h_coeff: float,
    max_certificate_size: int,
    tight_limit: int,
) -> dict[str, Any]:
    """构造唯一代表持久性拆分结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    normal = load_module(ONE_TWO_ROUTER, "unique_representative_split_normal")
    raw_records = normal.build_certificate_records(
        template_ledger,
        max_p,
        p0,
        target_h_coeff,
        max_certificate_size,
    )
    physical_records, duplicate_packets = physical_deduplicate(raw_records)

    shape_groups = group_records(physical_records, "shape")
    residue_groups = group_records(physical_records, "residue")
    slot_groups = group_records(physical_records, "slot")

    shape_rows = sorted_summaries(shape_groups)
    residue_rows = sorted_summaries(residue_groups)
    slot_rows = sorted_summaries(slot_groups)
    moving_rows = drift_summary(shape_rows)
    fixed_recurrent_rows = fixed_residue_recurrences(residue_rows)

    shape_count_hist = Counter(len(records) for records in shape_groups.values())
    residue_count_hist = Counter(len(records) for records in residue_groups.values())
    recurrent_shape_rows = [row for row in shape_rows if int(row["physical_count"]) > 1]

    aggregate = {
        "template_ledger": str(template_ledger.relative_to(ROOT)),
        "subcert_ledger": str(subcert_ledger.relative_to(ROOT)),
        "max_p": max_p,
        "p0": p0,
        "target_h_coeff": target_h_coeff,
        "max_certificate_size": max_certificate_size,
        "raw_record_count": len(raw_records),
        "physical_record_count": len(physical_records),
        "duplicate_template_count": len(raw_records) - len(physical_records),
        "duplicate_physical_packet_count": len(duplicate_packets),
        "normal_shape_count": len(shape_groups),
        "residue_packet_count": len(residue_groups),
        "slot_packet_count": len(slot_groups),
        "recurrent_shape_count": len(recurrent_shape_rows),
        "recurrent_fixed_residue_packet_count": sum(
            1 for row in residue_rows if int(row["physical_count"]) > 1
        ),
        "recurrent_fixed_residue_packet_count_distinct_p": len(fixed_recurrent_rows),
        "moving_residue_shape_count": len(moving_rows),
        "shape_count_histogram": {str(key): shape_count_hist[key] for key in sorted(shape_count_hist)},
        "residue_count_histogram": {
            str(key): residue_count_hist[key] for key in sorted(residue_count_hist)
        },
        "max_physical_multiplicity_per_shape": max(len(records) for records in shape_groups.values()),
        "max_physical_multiplicity_per_residue_packet": max(
            len(records) for records in residue_groups.values()
        ),
        "max_distinct_p_per_residue_packet": max(
            int(row["distinct_p_count"]) for row in residue_rows
        ),
        "unique_representative_identity_failure_count": sum(
            1 for record in physical_records if not bool(record["actual_p_is_unique_representative"])
        ),
        "persistent_packet_exclusion_proved": False,
        "fixed_residue_pdec_excluded": False,
        "moving_residue_sae_rankin_bound_proved": False,
        "global_residual_prime_margin_proved": False,
        "row_column_unconditional_closed": False,
    }

    ledger = {
        "parameters": {
            "max_p": max_p,
            "p0": p0,
            "target_h_coeff": target_h_coeff,
            "max_certificate_size": max_certificate_size,
            "tight_limit": tight_limit,
        },
        "aggregate": aggregate,
        "duplicate_template_packets": duplicate_packets[:tight_limit],
        "top_recurrent_shape_packets": recurrent_shape_rows[:tight_limit],
        "top_fixed_residue_recurrent_packets": fixed_recurrent_rows[:tight_limit],
        "top_moving_residue_shape_packets": moving_rows[:tight_limit],
        "top_fixed_slot_packets": slot_rows[:tight_limit],
        "tight_physical_records": [
            compact_record(record)
            for record in sorted(
                physical_records,
                key=lambda item: (
                    int(item["residual_prime_pair_margin_to_bound"]),
                    int(item["certificate_size"]),
                    int(item["crt_minus_phase_width"]),
                    int(item["p"]),
                    str(item["side"]),
                    int(item["rho"]),
                ),
            )[:tight_limit]
        ],
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    result = {
        "certificate_type": (
            "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_"
            "unique_representative_persistence_split_router"
        ),
        "status": "unique_representative_persistence_split_materialized_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_sweep_not_used_as_global_proof": True,
        "parameters": ledger["parameters"],
        "aggregate": aggregate,
        "duplicate_template_packets": ledger["duplicate_template_packets"],
        "top_recurrent_shape_packets": ledger["top_recurrent_shape_packets"],
        "top_fixed_residue_recurrent_packets": ledger["top_fixed_residue_recurrent_packets"],
        "top_moving_residue_shape_packets": ledger["top_moving_residue_shape_packets"],
        "top_fixed_slot_packets": ledger["top_fixed_slot_packets"],
        "tight_physical_records": ledger["tight_physical_records"],
        "persistent_packet_exclusion_proved": False,
        "fixed_residue_pdec_excluded": False,
        "moving_residue_sae_rankin_bound_proved": False,
        "global_residual_prime_margin_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "plain_conclusion": (
            "本步把唯一代表正规形的持久性来源拆成三层：physical 事件、fixed-residue packet、"
            "fixed-slot packet。当前重放 raw 记录 "
            f"{len(raw_records)} 条，物理去重后 {len(physical_records)} 条，删除模板重复 "
            f"{aggregate['duplicate_template_count']} 条；正规形 shape 为 {aggregate['normal_shape_count']} 个，"
            f"固定残基包为 {aggregate['residue_packet_count']} 个。跨不同 P 复现的固定残基包 "
            f"{aggregate['recurrent_fixed_residue_packet_count_distinct_p']} 个，残基或槽漂移的 moving shape "
            f"{aggregate['moving_residue_shape_count']} 个。它们分别进入 ColumnCRT/PDEC 与 SAE/Rankin，"
            "全局无条件闭合仍未完成。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    result["source_hashes"] = {
        "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_unique_representative_persistence_split_router.py": sha256(
            Path(__file__).resolve()
        ),
        "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_one_two_slot_normal_form_router.py": sha256(
            ONE_TWO_ROUTER
        ),
        "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-unique-representative-persistence-split-ledger.json": sha256(
            OUT_LEDGER
        ),
    }
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow selector H lower unique-representative persistence split router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"max_p={agg['max_p']}",
        f"p0={agg['p0']}",
        f"raw_record_count={agg['raw_record_count']}",
        f"physical_record_count={agg['physical_record_count']}",
        f"duplicate_template_count={agg['duplicate_template_count']}",
        f"normal_shape_count={agg['normal_shape_count']}",
        f"residue_packet_count={agg['residue_packet_count']}",
        f"recurrent_shape_count={agg['recurrent_shape_count']}",
        f"recurrent_fixed_residue_packet_count_distinct_p={agg['recurrent_fixed_residue_packet_count_distinct_p']}",
        f"moving_residue_shape_count={agg['moving_residue_shape_count']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 去重与拆分口径",
        "",
        "```text",
        "physical_key = (P, side, rho, normal_shape, CRT residue, CRT modulus, slot_keys)",
        "residue_packet = (normal_shape, CRT modulus, CRT residue)",
        "slot_packet = (normal_shape, CRT modulus, CRT residue, slot_keys)",
        "```",
        "",
        "物理去重只合并模板索引重复，不合并不同 `rho`、不同槽或不同残基的真实事件。",
        "",
        "## 2. 高频 shape 包",
        "",
        "| shape | physical | distinct P | residues | slot packets | p range | min margin | min CRT-width |",
        "| --- | ---: | ---: | ---: | ---: | --- | ---: | ---: |",
    ]
    for row in result["top_recurrent_shape_packets"][:18]:
        lines.append(
            f"| `{row['key']}` | {row['physical_count']} | {row['distinct_p_count']} | "
            f"{row['distinct_residue_count']} | {row['distinct_slot_packet_count']} | "
            f"`{row['min_p']}..{row['max_p']}` | {row['min_margin']} | "
            f"{row['min_crt_minus_phase_width']} |"
        )

    lines.extend(
        [
            "",
            "## 3. 固定残基复现包",
            "",
            "| residue packet | physical | distinct P | p values | min margin | min CRT-width |",
            "| --- | ---: | ---: | --- | ---: | ---: |",
        ]
    )
    for row in result["top_fixed_residue_recurrent_packets"][:18]:
        lines.append(
            f"| `{row['key']}` | {row['physical_count']} | {row['distinct_p_count']} | "
            f"`{row['p_values']}` | {row['min_margin']} | {row['min_crt_minus_phase_width']} |"
        )

    lines.extend(
        [
            "",
            "## 4. 移动残基 shape",
            "",
            "| shape | physical | distinct P | residues | slot packets | p range | first residues |",
            "| --- | ---: | ---: | ---: | ---: | --- | --- |",
        ]
    )
    for row in result["top_moving_residue_shape_packets"][:18]:
        lines.append(
            f"| `{row['key']}` | {row['physical_count']} | {row['distinct_p_count']} | "
            f"{row['distinct_residue_count']} | {row['distinct_slot_packet_count']} | "
            f"`{row['min_p']}..{row['max_p']}` | `{row['residue_values']}` |"
        )

    lines.extend(
        [
            "",
            "## 5. 最紧物理事件",
            "",
            "| p | side | rho | templates | margin | shape | residue | slots |",
            "| ---: | --- | ---: | --- | ---: | --- | ---: | --- |",
        ]
    )
    for row in result["tight_physical_records"][:18]:
        lines.append(
            f"| {row['p']} | `{row['side']}` | {row['rho']} | `{row['template_indices']}` | "
            f"{row['residual_prime_pair_margin_to_bound']} | `{row['normal_shape_key']}` | "
            f"{row['crt_residue']} | `{row['slot_keys']}` |"
        )

    lines.extend(
        [
            "",
            "## 6. 结构判断",
            "",
            "- 固定残基复现包不是由模板索引重复造成；它们是下一步 `ColumnCRT/PDEC` 的候选输入。",
            "- 同一正规形 shape 若残基或槽漂移，不能当作固定 CRT 图样排斥；它们应转入 `SAE/Rankin` 或全局增长界。",
            "- 当前只是把前沿剩余拆成两个合法出口，没有证明全局无条件闭合。",
            "",
            "## 7. 命题行",
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
            "## 8. 决策表",
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
            "## 9. 下一步",
            "",
            f"- 主攻：`{result['next_direct_attack_target']}`。",
            "- 固定残基包：证明 ColumnCRT/PDEC 上界，或登记明确的固定残基持久缺陷。",
            "- 移动残基 shape：证明 residue drift 的 SAE/Rankin 可求和或增长界。",
            "",
            "## 10. 依赖哈希",
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
    parser.add_argument("--subcert-ledger", type=Path, default=SUBCERT_LEDGER)
    parser.add_argument("--max-p", type=int, default=10000)
    parser.add_argument("--p0", type=int, default=2001)
    parser.add_argument("--target-h-coeff", type=float, default=0.43)
    parser.add_argument("--max-certificate-size", type=int, default=2)
    parser.add_argument("--tight-limit", type=int, default=40)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    template_ledger = args.template_ledger if args.template_ledger.is_absolute() else ROOT / args.template_ledger
    subcert_ledger = args.subcert_ledger if args.subcert_ledger.is_absolute() else ROOT / args.subcert_ledger
    result = build_result(
        template_ledger,
        subcert_ledger,
        args.max_p,
        args.p0,
        args.target_h_coeff,
        args.max_certificate_size,
        args.tight_limit,
    )
    write_markdown(result)
    result["source_hashes"][
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-unique-representative-persistence-split-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "raw_record_count": result["aggregate"]["raw_record_count"],
                "physical_record_count": result["aggregate"]["physical_record_count"],
                "duplicate_template_count": result["aggregate"]["duplicate_template_count"],
                "normal_shape_count": result["aggregate"]["normal_shape_count"],
                "residue_packet_count": result["aggregate"]["residue_packet_count"],
                "recurrent_fixed_residue_packet_count_distinct_p": result["aggregate"][
                    "recurrent_fixed_residue_packet_count_distinct_p"
                ],
                "moving_residue_shape_count": result["aggregate"]["moving_residue_shape_count"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
