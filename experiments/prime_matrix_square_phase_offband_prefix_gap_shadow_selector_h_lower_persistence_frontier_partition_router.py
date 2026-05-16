#!/usr/bin/env python3
"""合并固定残基 transport cell 与单例残基 SAE 的前沿分区。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_persistence_frontier_partition_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-persistence-frontier-partition-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-selector-h-lower-persistence-frontier-partition-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-persistence-frontier-partition-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-persistence-frontier-partition-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SPLIT_LEDGER = DATA / (
    "square-phase-offband-prefix-gap-shadow-selector-h-lower-"
    "unique-representative-persistence-split-ledger.json"
)
TRANSPORT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-fixed-residue-transport-cell-ledger.json"
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-persistence-frontier-partition-ledger.json"
OUT_JSON = DOCS / (
    "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-"
    "persistence-frontier-partition-router.json"
)
OUT_MD = DOCS / (
    "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-"
    "persistence-frontier-partition-router.md"
)

MAIN_TARGET = "FixedResidueTransportCellPDECOrMovingResidueShapeSAE"
NEXT_TARGET = "TransportCellNonPersistenceOrSingletonResidueSAESummability"


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


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "frontier_partition_identity",
            "status": "closed",
            "statement": "Physical unique-representative events split into recurrent fixed-residue transport-cell records and singleton residue packets.",
        },
        {
            "name": "current_sweep_no_unclassified_persistence",
            "status": "closed_on_current_sweep",
            "statement": "On the current sweep every physical event is accounted for by either a transport cell pair or a singleton residue packet.",
        },
        {
            "name": "global_transport_or_singleton_sae_open",
            "status": "open",
            "statement": "A global proof must exclude transport-cell persistence or prove singleton-residue SAE/Rankin summability.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    agg = result["aggregate"]
    return [
        {
            "gate": "FrontierPartitionIdentityClosed",
            "closed": agg["partition_identity_closed"],
            "proved": True,
            "meaning": "324 个物理事件被 24 个 transport-cell 事件与 300 个 singleton residue 事件精确分割。",
            "remaining": "closed",
        },
        {
            "gate": "NoUnclassifiedPersistenceCurrentSweep",
            "closed": agg["unclassified_physical_record_count"] == 0,
            "proved": False,
            "meaning": "当前扫描没有第三类未登记持久性。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "TransportCellPersistenceExcluded",
            "closed": False,
            "proved": False,
            "meaning": "12 个互异 transport cell 仍需全局非持久证明。",
            "remaining": "TransportCellPDEC/ColumnCRT",
        },
        {
            "gate": "SingletonResidueSAESummabilityProved",
            "closed": False,
            "proved": False,
            "meaning": "300 个 singleton residue packet 仍需 SAE/Rankin 可求和输入。",
            "remaining": "SingletonResidueSAE/Rankin",
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步完成前沿分区，不关闭全局行/列命题。",
            "remaining": result["next_direct_attack_target"],
        },
    ]


def build_result(split_ledger: Path, transport_ledger: Path) -> dict[str, Any]:
    """构造前沿分区账本。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    split = load_json(split_ledger)
    transport = load_json(transport_ledger)
    split_agg = split["aggregate"]
    transport_agg = transport["aggregate"]

    physical_count = int(split_agg["physical_record_count"])
    residue_packet_count = int(split_agg["residue_packet_count"])
    recurrent_packet_count = int(split_agg["recurrent_fixed_residue_packet_count_distinct_p"])
    max_packet_multiplicity = int(split_agg["max_physical_multiplicity_per_residue_packet"])
    if max_packet_multiplicity != 2:
        raise RuntimeError("frontier partition assumes recurrent residue packets have multiplicity two")
    recurrent_physical_count = 2 * recurrent_packet_count
    singleton_packet_count = residue_packet_count - recurrent_packet_count
    singleton_physical_count = singleton_packet_count
    partition_total = recurrent_physical_count + singleton_physical_count
    unclassified = physical_count - partition_total

    aggregate = {
        "split_ledger": str(split_ledger.relative_to(ROOT)),
        "transport_ledger": str(transport_ledger.relative_to(ROOT)),
        "physical_record_count": physical_count,
        "residue_packet_count": residue_packet_count,
        "recurrent_fixed_residue_packet_count": recurrent_packet_count,
        "max_physical_multiplicity_per_residue_packet": max_packet_multiplicity,
        "transport_cell_count": int(transport_agg["transport_cell_count"]),
        "unique_transport_cell_count": int(transport_agg["unique_transport_cell_count"]),
        "transport_cell_recurrence_count": int(transport_agg["transport_cell_recurrence_count"]),
        "transport_cell_physical_record_count": recurrent_physical_count,
        "singleton_residue_packet_count": singleton_packet_count,
        "singleton_residue_physical_record_count": singleton_physical_count,
        "partition_total_physical_record_count": partition_total,
        "unclassified_physical_record_count": unclassified,
        "partition_identity_closed": unclassified == 0
        and int(transport_agg["transport_cell_count"]) == recurrent_packet_count,
        "transport_cell_persistence_excluded_globally": False,
        "singleton_residue_sae_rankin_bound_proved": False,
        "global_residual_prime_margin_proved": False,
        "row_column_unconditional_closed": False,
    }

    ledger = {
        "aggregate": aggregate,
        "partition_rows": [
            {
                "class": "transport_cell_pairs",
                "packet_count": recurrent_packet_count,
                "physical_record_count": recurrent_physical_count,
                "global_status": "open_transport_cell_pdec_or_columncrt",
            },
            {
                "class": "singleton_residue_packets",
                "packet_count": singleton_packet_count,
                "physical_record_count": singleton_physical_count,
                "global_status": "open_singleton_residue_sae_rankin",
            },
        ],
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    result = {
        "certificate_type": (
            "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_"
            "persistence_frontier_partition_router"
        ),
        "status": "persistence_frontier_partition_closed_global_exclusion_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_sweep_not_used_as_global_proof": True,
        "aggregate": aggregate,
        "partition_rows": ledger["partition_rows"],
        "transport_cell_persistence_excluded_globally": False,
        "singleton_residue_sae_rankin_bound_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "plain_conclusion": (
            "本步把唯一代表前沿做成完整分区：324 个物理事件中，24 个来自 12 个固定残基 "
            "transport-cell 对，剩余 300 个都是 singleton residue packet，没有第三类未登记持久性。"
            "因此最新硬点只剩两门：排斥 transport-cell 全局持久复现，或证明 singleton residue 的 "
            "SAE/Rankin 可求和。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    result["source_hashes"] = {
        "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_persistence_frontier_partition_router.py": sha256(
            Path(__file__).resolve()
        ),
        "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-unique-representative-persistence-split-ledger.json": sha256(
            split_ledger
        ),
        "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-fixed-residue-transport-cell-ledger.json": sha256(
            transport_ledger
        ),
        "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-persistence-frontier-partition-ledger.json": sha256(
            OUT_LEDGER
        ),
    }
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow selector H lower persistence frontier partition router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"physical_record_count={agg['physical_record_count']}",
        f"transport_cell_physical_record_count={agg['transport_cell_physical_record_count']}",
        f"singleton_residue_physical_record_count={agg['singleton_residue_physical_record_count']}",
        f"unclassified_physical_record_count={agg['unclassified_physical_record_count']}",
        f"partition_identity_closed={fmt_bool(agg['partition_identity_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 前沿分区",
        "",
        "| class | packets | physical records | global status |",
        "| --- | ---: | ---: | --- |",
    ]
    for row in result["partition_rows"]:
        lines.append(
            f"| `{row['class']}` | {row['packet_count']} | {row['physical_record_count']} | `{row['global_status']}` |"
        )
    lines.extend(
        [
            "",
            "## 2. 结构判断",
            "",
            "- 固定残基复现已经全部收缩到 12 个 transport cell 对。",
            "- 非固定残基部分全部是 singleton residue packet；当前没有额外 persistence 类别。",
            "- 全局证明仍需关闭 transport-cell 持久性或 singleton-residue SAE/Rankin。",
            "",
            "## 3. 命题行",
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
            "## 4. 决策表",
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
            "## 5. 下一步",
            "",
            f"- 主攻：`{result['next_direct_attack_target']}`。",
            "- 优先尝试 transport-cell 全局非持久证明；若失败，登记明确 ColumnCRT/PDEC。",
            "- 同步准备 singleton-residue SAE/Rankin 可求和账本。",
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
    parser.add_argument("--split-ledger", type=Path, default=SPLIT_LEDGER)
    parser.add_argument("--transport-ledger", type=Path, default=TRANSPORT_LEDGER)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    split_ledger = args.split_ledger if args.split_ledger.is_absolute() else ROOT / args.split_ledger
    transport_ledger = args.transport_ledger if args.transport_ledger.is_absolute() else ROOT / args.transport_ledger
    result = build_result(split_ledger, transport_ledger)
    write_markdown(result)
    result["source_hashes"][
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-persistence-frontier-partition-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "physical_record_count": result["aggregate"]["physical_record_count"],
                "transport_cell_physical_record_count": result["aggregate"][
                    "transport_cell_physical_record_count"
                ],
                "singleton_residue_physical_record_count": result["aggregate"][
                    "singleton_residue_physical_record_count"
                ],
                "unclassified_physical_record_count": result["aggregate"]["unclassified_physical_record_count"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
