#!/usr/bin/env python3
"""生成 AffineTwin endpoint-release transport-frontier integration 审计证书。

用法示例：
  python3 experiments/prime_matrix_affine_twin_endpoint_release_transport_frontier_integration_audit.py
  python3 -m json.tool data/prime-matrix-affine-twin-endpoint-release-transport-frontier-integration-ledger.json

输出：
  data/prime-matrix-affine-twin-endpoint-release-transport-frontier-integration-ledger.json
  docs/monograph/prime-matrix-affine-twin-endpoint-release-transport-frontier-integration-audit.json
  docs/monograph/prime-matrix-affine-twin-endpoint-release-transport-frontier-integration-audit.md
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

PROMOTION_LEDGER = DATA / (
    "prime-matrix-affine-twin-endpoint-release-persistent-family-promotion-ledger.json"
)
TRANSPORT_LEDGER = DATA / (
    "square-phase-offband-prefix-gap-shadow-selector-h-lower-"
    "fixed-residue-transport-cell-ledger.json"
)
ITERATION_LEDGER = DATA / (
    "square-phase-offband-prefix-gap-shadow-selector-h-lower-"
    "transport-cell-iteration-drift-ledger.json"
)
RESET_LEDGER = DATA / (
    "square-phase-offband-prefix-gap-shadow-selector-h-lower-"
    "transport-cell-reset-pdec-ledger.json"
)
PARTITION_LEDGER = DATA / (
    "square-phase-offband-prefix-gap-shadow-selector-h-lower-"
    "persistence-frontier-partition-ledger.json"
)

OUT_LEDGER = DATA / (
    "prime-matrix-affine-twin-endpoint-release-transport-frontier-integration-ledger.json"
)
OUT_JSON = DOCS / (
    "prime-matrix-affine-twin-endpoint-release-transport-frontier-integration-audit.json"
)
OUT_MD = DOCS / (
    "prime-matrix-affine-twin-endpoint-release-transport-frontier-integration-audit.md"
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


def route_row(
    gate: str,
    closed: bool,
    evidence: str,
    global_remaining: str,
) -> dict[str, Any]:
    """构造路由行。"""
    return {
        "gate": gate,
        "closed_current_sweep": closed,
        "evidence": evidence,
        "global_remaining": global_remaining,
    }


def build_result(
    promotion_path: Path,
    transport_path: Path,
    iteration_path: Path,
    reset_path: Path,
    partition_path: Path,
) -> dict[str, Any]:
    """构造 transport-frontier integration 审计结果。"""
    promotion = load_json(promotion_path)
    transport = load_json(transport_path)
    iteration = load_json(iteration_path)
    reset = load_json(reset_path)
    partition = load_json(partition_path)

    pa = promotion["aggregate"]
    ta = transport["aggregate"]
    ia = iteration["aggregate"]
    ra = reset["aggregate"]
    fa = partition["aggregate"]

    fixed_drift_to_transport_closed = (
        int(pa["fixed_residue_slot_drift_pair_count"]) == int(ta["transport_cell_count"])
        and bool(ta["all_transport_cells_unique_current_sweep"])
        and int(ta["transport_cell_recurrence_count"]) == 0
    )
    chained_closed = (
        bool(ia["chained_transport_persistence_excluded_current_sweep"])
        and bool(ia["all_current_cells_forward_finite_by_depth"])
        and int(ia["depth_iteration_identity_failure_count"]) == 0
    )
    reset_closed = (
        bool(ra["current_sweep_transport_reset_atoms_empty"])
        and int(ra["reset_pdec_atom_count"]) == 0
        and int(ra["repeated_transport_cell_key_count"]) == 0
    )
    partition_closed = (
        bool(fa["partition_identity_closed"])
        and int(fa["unclassified_physical_record_count"]) == 0
        and int(fa["partition_total_physical_record_count"])
        == int(fa["physical_record_count"])
    )

    route_rows = [
        route_row(
            "FixedResidueSlotDriftToTransportCell",
            fixed_drift_to_transport_closed,
            (
                f"slot-drift pairs={pa['fixed_residue_slot_drift_pair_count']}; "
                f"transport cells={ta['transport_cell_count']}; "
                f"unique cells={ta['unique_transport_cell_count']}; "
                f"exact phase translates={ta['exact_phase_translate_count']}"
            ),
            "TransportCellPDEC/ColumnCRT",
        ),
        route_row(
            "ChainedTransportDepthDrift",
            chained_closed,
            (
                f"forward finite cells={ia['forward_finite_lifetime_count']}; "
                f"max forward transitions={ia['max_forward_transition_count']}; "
                f"immediate terminal cells={ia['immediate_terminal_after_observed_count']}"
            ),
            "NonChainedTransportCellPDEC",
        ),
        route_row(
            "NonChainedTransportResetPDEC",
            reset_closed,
            (
                f"unique transport cell keys={ra['unique_transport_cell_key_count']}; "
                f"repeated keys={ra['repeated_transport_cell_key_count']}; "
                f"reset atoms={ra['reset_pdec_atom_count']}"
            ),
            "TransportResetPDECExclusion",
        ),
        route_row(
            "PersistenceFrontierPartition",
            partition_closed,
            (
                f"physical records={fa['physical_record_count']}; "
                f"transport physical records={fa['transport_cell_physical_record_count']}; "
                f"singleton physical records={fa['singleton_residue_physical_record_count']}; "
                f"unclassified={fa['unclassified_physical_record_count']}"
            ),
            "SingletonResidueSAE/Rankin",
        ),
    ]

    closed_current = all(bool(row["closed_current_sweep"]) for row in route_rows)
    aggregate = {
        "persistent_family_promotion_ledger": str(promotion_path.relative_to(ROOT)),
        "fixed_residue_transport_cell_ledger": str(transport_path.relative_to(ROOT)),
        "transport_cell_iteration_drift_ledger": str(iteration_path.relative_to(ROOT)),
        "transport_cell_reset_pdec_ledger": str(reset_path.relative_to(ROOT)),
        "persistence_frontier_partition_ledger": str(partition_path.relative_to(ROOT)),
        "fixed_residue_slot_drift_pair_count": int(
            pa["fixed_residue_slot_drift_pair_count"]
        ),
        "transport_cell_count": int(ta["transport_cell_count"]),
        "unique_transport_cell_count": int(ta["unique_transport_cell_count"]),
        "transport_cell_recurrence_count": int(ta["transport_cell_recurrence_count"]),
        "exact_phase_translate_count": int(ta["exact_phase_translate_count"]),
        "all_edge_defects_strictly_below_ell": bool(
            ta["all_edge_defects_strictly_below_ell"]
        ),
        "max_abs_edge_defect": int(ta["max_abs_edge_defect"]),
        "forward_finite_lifetime_count": int(ia["forward_finite_lifetime_count"]),
        "max_forward_transition_count": int(ia["max_forward_transition_count"]),
        "max_forward_additional_after_observed": int(
            ia["max_forward_additional_after_observed"]
        ),
        "immediate_terminal_after_observed_count": int(
            ia["immediate_terminal_after_observed_count"]
        ),
        "reset_pdec_atom_count": int(ra["reset_pdec_atom_count"]),
        "repeated_transport_cell_key_count": int(
            ra["repeated_transport_cell_key_count"]
        ),
        "physical_record_count": int(fa["physical_record_count"]),
        "transport_cell_physical_record_count": int(
            fa["transport_cell_physical_record_count"]
        ),
        "singleton_residue_physical_record_count": int(
            fa["singleton_residue_physical_record_count"]
        ),
        "unclassified_physical_record_count": int(
            fa["unclassified_physical_record_count"]
        ),
        "fixed_drift_to_transport_closed_current_sweep": fixed_drift_to_transport_closed,
        "chained_transport_persistence_closed_current_sweep": chained_closed,
        "nonchained_transport_reset_atoms_empty_current_sweep": reset_closed,
        "persistence_frontier_partition_closed_current_sweep": partition_closed,
        "transport_frontier_integration_closed_current_sweep": closed_current,
        "transport_reset_pdec_excluded_globally": False,
        "singleton_residue_sae_rankin_bound_proved": False,
        "global_epoch_pair_multiplicity_bound_proved": False,
        "row_column_unconditional_closed": False,
    }

    return {
        "certificate_type": (
            "prime_matrix_affine_twin_endpoint_release_"
            "transport_frontier_integration_audit"
        ),
        "status": "current_sweep_transport_frontier_integrated_global_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "aggregate": aggregate,
        "transport_frontier_route_rows": route_rows,
        "contract": {
            "transport_frontier_integration": [
                "fixed-residue slot drift is not a fixed-slot recurrence; it factors through transport cells",
                "current transport cells are unique and have no exact phase translate",
                "chained transport recurrence has finite depth lifetime in the current ledger",
                "non-chained recurrence must repeat the full transport-cell key; current reset atoms are empty",
                "the frontier partition leaves singleton residue packets as a separate SAE/Rankin obligation",
            ],
            "closed_current_sweep": closed_current,
            "global_remaining": [
                "TransportResetPDECExclusion",
                "SingletonResidueSAE/Rankin",
                "GlobalEpochPairMultiplicityBound",
                "MovingResidueShapeSAE/Rankin",
            ],
        },
        "dependency_hashes": {
            str(path.relative_to(ROOT)): sha256(path)
            for path in (
                promotion_path,
                transport_path,
                iteration_path,
                reset_path,
                partition_path,
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
        "# Prime Matrix AffineTwin endpoint-release transport-frontier integration audit",
        "",
        "**状态：** `current_sweep_transport_frontier_integrated_global_open`",
        "",
        "本审计把最新 AffineTwin 前沿接入既有 transport-cell 深层账本：固定残基槽漂移被压成 transport cell，链式复现有有限寿命，非连续复现必须重复完整 reset-PDEC key；当前 reset atom 为空。",
        "",
        "```text",
        f"fixed_residue_slot_drift_pair_count={agg['fixed_residue_slot_drift_pair_count']}",
        f"transport_cell_count={agg['transport_cell_count']}",
        f"unique_transport_cell_count={agg['unique_transport_cell_count']}",
        f"transport_cell_recurrence_count={agg['transport_cell_recurrence_count']}",
        f"max_forward_transition_count={agg['max_forward_transition_count']}",
        f"reset_pdec_atom_count={agg['reset_pdec_atom_count']}",
        f"singleton_residue_physical_record_count={agg['singleton_residue_physical_record_count']}",
        f"transport_frontier_integration_closed_current_sweep={fmt_bool(agg['transport_frontier_integration_closed_current_sweep'])}",
        "```",
        "",
        "## 1. transport frontier routes",
        "",
        "| gate | closed | evidence | global remaining |",
        "| --- | --- | --- | --- |",
    ]
    for row in result["transport_frontier_route_rows"]:
        lines.append(
            "| `{gate}` | {closed} | {evidence} | `{remaining}` |".format(
                gate=row["gate"],
                closed=fmt_bool(row["closed_current_sweep"]),
                evidence=table_cell(row["evidence"]),
                remaining=table_cell(row["global_remaining"]),
            )
        )

    lines.extend(
        [
            "",
            "## 2. 显式矛盾读数",
            "",
            "- 反例链若依赖固定残基槽漂移持续供给容量，真实链要求它成为 transport cell 的持久复现。",
            "- 当前 12 个 transport cell 全部互异、无 exact phase translate；同一 cell 链式复现会触发深度线性漂移并在有限步内终止。",
            "- 非连续复现必须重复完整 transport-cell key；当前 reset-PDEC atom 数为 `0`。",
            "- 前沿物理记录精确分区为 `24` 个 transport-cell 记录和 `300` 个 singleton residue 记录，无未分类项。",
            "",
            "## 3. 结论边界",
            "",
            "当前 sweep 的 fixed-residue slot-drift 不再是匿名 ColumnCRT 容量来源。最新剩余压成 `TransportResetPDECExclusion`、`SingletonResidueSAE/Rankin` 与 `GlobalEpochPairMultiplicityBound`。",
            "",
            "这仍不是行/列命题的全局无条件证明；它关闭的是当前 sweep 中 transport-frontier 的匿名逃逸解释。",
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
    parser = argparse.ArgumentParser(
        description="生成 AffineTwin endpoint-release transport-frontier integration 审计证书。"
    )
    parser.add_argument("--promotion-ledger", type=Path, default=PROMOTION_LEDGER)
    parser.add_argument("--transport-ledger", type=Path, default=TRANSPORT_LEDGER)
    parser.add_argument("--iteration-ledger", type=Path, default=ITERATION_LEDGER)
    parser.add_argument("--reset-ledger", type=Path, default=RESET_LEDGER)
    parser.add_argument("--partition-ledger", type=Path, default=PARTITION_LEDGER)
    return parser.parse_args()


def main() -> None:
    """入口。"""
    args = parse_args()
    result = build_result(
        args.promotion_ledger,
        args.transport_ledger,
        args.iteration_ledger,
        args.reset_ledger,
        args.partition_ledger,
    )
    write_outputs(result)
    print(json.dumps(result["aggregate"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
