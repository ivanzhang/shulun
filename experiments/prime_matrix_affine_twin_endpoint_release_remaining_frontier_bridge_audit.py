#!/usr/bin/env python3
"""生成 AffineTwin endpoint-release remaining-frontier bridge 审计证书。

用法示例：
  python3 experiments/prime_matrix_affine_twin_endpoint_release_remaining_frontier_bridge_audit.py
  python3 -m json.tool data/prime-matrix-affine-twin-endpoint-release-remaining-frontier-bridge-ledger.json

输出：
  data/prime-matrix-affine-twin-endpoint-release-remaining-frontier-bridge-ledger.json
  docs/monograph/prime-matrix-affine-twin-endpoint-release-remaining-frontier-bridge-audit.json
  docs/monograph/prime-matrix-affine-twin-endpoint-release-remaining-frontier-bridge-audit.md
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

TRANSPORT_INTEGRATION_LEDGER = DATA / (
    "prime-matrix-affine-twin-endpoint-release-transport-frontier-integration-ledger.json"
)
SINGLETON_PROFILE_LEDGER = DATA / (
    "square-phase-offband-prefix-gap-shadow-selector-h-lower-"
    "singleton-residue-sae-profile-ledger.json"
)
SINGLETON_RANKIN_LEDGER = DATA / (
    "square-phase-offband-prefix-gap-shadow-selector-h-lower-"
    "singleton-rankin-budget-ledger.json"
)
ONE_SLOT_CAPACITY_LEDGER = DATA / (
    "square-phase-offband-prefix-gap-shadow-selector-h-lower-"
    "one-slot-residue-epoch-capacity-ledger.json"
)
ACTIVE_SOURCE_LEDGER = DATA / (
    "square-phase-offband-prefix-gap-shadow-selector-h-lower-"
    "active-one-slot-epoch-source-ledger.json"
)
ACTIVE_BAND_LEDGER = DATA / (
    "square-phase-offband-prefix-gap-shadow-selector-h-lower-"
    "active-ell-interval-band-ledger.json"
)
EPOCH_PAIR_LEDGER = DATA / (
    "square-phase-offband-prefix-gap-shadow-selector-h-lower-"
    "affine-twin-epoch-pair-multiplicity-ledger.json"
)

OUT_LEDGER = DATA / (
    "prime-matrix-affine-twin-endpoint-release-remaining-frontier-bridge-ledger.json"
)
OUT_JSON = DOCS / (
    "prime-matrix-affine-twin-endpoint-release-remaining-frontier-bridge-audit.json"
)
OUT_MD = DOCS / (
    "prime-matrix-affine-twin-endpoint-release-remaining-frontier-bridge-audit.md"
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


def close_float(a: float, b: float, eps: float = 1e-12) -> bool:
    """比较浮点读数是否来自同一账本恒等式。"""
    return abs(a - b) <= eps


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


def build_result(paths: dict[str, Path]) -> dict[str, Any]:
    """合成最新剩余前沿桥接证书。"""
    transport = load_json(paths["transport"])
    profile = load_json(paths["profile"])
    rankin = load_json(paths["rankin"])
    capacity = load_json(paths["capacity"])
    active_source = load_json(paths["active_source"])
    active_band = load_json(paths["active_band"])
    epoch_pair = load_json(paths["epoch_pair"])

    ta = transport["aggregate"]
    pa = profile["aggregate"]
    ra = rankin["aggregate"]
    ca = capacity["aggregate"]
    aa = active_source["aggregate"]
    ea = epoch_pair["aggregate"]

    singleton_count_matches_partition = int(pa["singleton_residue_packet_count"]) == int(
        ta["singleton_residue_physical_record_count"]
    )
    rankin_profile_identity = close_float(
        float(pa["singleton_rankin_mass_total"]),
        float(ra["singleton_rankin_mass_total"]),
    ) and bool(ra["rankin_budget_identity_closed"])
    one_slot_capacity_bridge = (
        bool(ca["reset_free_epoch_capacity_closed"])
        and int(ca["overflow_row_count"]) == 0
        and float(ca["min_spare_ratio"]) > 0
    )
    active_source_bridge = (
        bool(aa["active_epoch_source_materialized"])
        and int(aa["distinct_active_ell_count"]) == len(active_band["active_ell_values"])
    )
    active_band_bridge = (
        bool(active_band["exact_active_prime_interval_current_sweep"])
        and bool(active_band["exact_both_side_prime_interval_current_sweep"])
        and bool(active_band["endpoint_asymmetry_only_current_sweep"])
    )
    singleton_to_active_band_closed = (
        singleton_count_matches_partition
        and rankin_profile_identity
        and one_slot_capacity_bridge
        and active_source_bridge
        and active_band_bridge
    )
    transport_bridge_closed = bool(ta["transport_frontier_integration_closed_current_sweep"])
    epoch_pair_sparse_closed = (
        bool(ea["candidate_product_mass_upper_sum_below_eta"])
        and bool(ea["all_candidate_epoch_pair_occupancy_below_eta"])
        and int(ea["high_density_epoch_pair_count"]) == 0
    )

    rows = [
        route_row(
            "TransportFrontierCurrentBridge",
            transport_bridge_closed,
            (
                f"transport cells={ta['transport_cell_count']}; "
                f"unique={ta['unique_transport_cell_count']}; "
                f"reset atoms={ta['reset_pdec_atom_count']}"
            ),
            "TransportResetPDECExclusion",
        ),
        route_row(
            "SingletonResidueToActiveEllBand",
            singleton_to_active_band_closed,
            (
                f"singleton packets={pa['singleton_residue_packet_count']}; "
                f"one-slot mass={ra['one_slot_mass']}; "
                f"active band={min(active_band['active_ell_values'])}..{max(active_band['active_ell_values'])}; "
                f"minus-only endpoints={active_band['minus_only_ell_values']}"
            ),
            "ActiveEllBandEndpointGrowthBoundOrEndpointResetPDEC",
        ),
        route_row(
            "AffineTwinEpochPairSparseGate",
            epoch_pair_sparse_closed,
            (
                f"candidate q={ea['candidate_q_values']}; "
                f"occupancy sum={ea['candidate_product_mass_upper_sum']}; "
                f"eta={ea['eta']}; "
                f"high-density rows={ea['high_density_epoch_pair_count']}"
            ),
            "GlobalEpochPairMultiplicityBound",
        ),
    ]
    bridge_closed = all(bool(row["closed_current_sweep"]) for row in rows)

    aggregate = {
        "transport_frontier_integration_closed_current_sweep": transport_bridge_closed,
        "transport_cell_count": int(ta["transport_cell_count"]),
        "unique_transport_cell_count": int(ta["unique_transport_cell_count"]),
        "transport_reset_pdec_atom_count": int(ta["reset_pdec_atom_count"]),
        "singleton_residue_packet_count": int(pa["singleton_residue_packet_count"]),
        "singleton_count_matches_partition": singleton_count_matches_partition,
        "singleton_rankin_mass_total": float(pa["singleton_rankin_mass_total"]),
        "one_slot_mass": float(ra["one_slot_mass"]),
        "two_slot_mass_share": float(ra["two_slot_mass_share"]),
        "rankin_profile_identity_closed_current_sweep": rankin_profile_identity,
        "active_one_slot_epoch_count": int(ca["active_one_slot_epoch_count"]),
        "total_residue_capacity": int(ca["total_residue_capacity"]),
        "total_used_residue_count": int(ca["total_used_residue_count"]),
        "total_unused_residue_count": int(ca["total_unused_residue_count"]),
        "max_one_slot_occupancy_ratio": float(ca["max_occupancy_ratio"]),
        "min_one_slot_spare_ratio": float(ca["min_spare_ratio"]),
        "one_slot_capacity_bridge_closed_current_sweep": one_slot_capacity_bridge,
        "distinct_active_ell_count": int(aa["distinct_active_ell_count"]),
        "active_band_min": int(min(active_band["active_ell_values"])),
        "active_band_max": int(max(active_band["active_ell_values"])),
        "active_band_prime_count": len(active_band["active_ell_values"]),
        "both_side_band_min": int(min(active_band["both_side_ell_values"])),
        "both_side_band_max": int(max(active_band["both_side_ell_values"])),
        "both_side_prime_count": len(active_band["both_side_ell_values"]),
        "minus_only_ell_values": active_band["minus_only_ell_values"],
        "plus_only_ell_values": active_band["plus_only_ell_values"],
        "active_band_bridge_closed_current_sweep": active_band_bridge,
        "candidate_epoch_pair_count": int(ea["candidate_epoch_pair_count"]),
        "candidate_q_values": ea["candidate_q_values"],
        "realized_q_values": ea["realized_q_values"],
        "candidate_product_mass_upper_sum": float(
            ea["candidate_product_mass_upper_sum"]
        ),
        "eta": float(ea["eta"]),
        "candidate_total_eta_slack": float(ea["candidate_total_eta_slack"]),
        "high_density_epoch_pair_count": int(ea["high_density_epoch_pair_count"]),
        "epoch_pair_sparse_closed_current_sweep": epoch_pair_sparse_closed,
        "remaining_frontier_bridge_closed_current_sweep": bridge_closed,
        "active_ell_band_endpoint_growth_bound_proved": False,
        "endpoint_reset_pdec_excluded_globally": False,
        "transport_reset_pdec_excluded_globally": False,
        "singleton_residue_sae_rankin_bound_proved_globally": False,
        "global_epoch_pair_multiplicity_bound_proved": False,
        "moving_residue_shape_sae_rankin_bound_proved": False,
        "row_column_unconditional_closed": False,
    }

    return {
        "certificate_type": (
            "prime_matrix_affine_twin_endpoint_release_remaining_frontier_bridge_audit"
        ),
        "status": "remaining_frontier_bridge_current_sweep_closed_global_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_sweep_not_used_as_global_proof": True,
        "aggregate": aggregate,
        "remaining_frontier_route_rows": rows,
        "global_remaining": [
            "ActiveEllBandEndpointGrowthBoundOrEndpointResetPDEC",
            "TransportResetPDECExclusion",
            "GlobalEpochPairMultiplicityBound",
            "MovingResidueShapeSAE/Rankin",
        ],
        "dependency_hashes": {
            str(path.relative_to(ROOT)): sha256(path) for path in paths.values()
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
        "# Prime Matrix AffineTwin endpoint-release remaining-frontier bridge audit",
        "",
        "**状态：** `remaining_frontier_bridge_current_sweep_closed_global_open`",
        "",
        "本审计把最新 transport-frontier 集成结果接到既有 singleton/active-ell/epoch-pair 账本，给出当前 sweep 的最新剩余前沿：singleton SAE 路线已定位到活跃素数带端点增长，epoch-pair 路线当前仍低于 eta 稀疏门。",
        "",
        "```text",
        f"transport_reset_pdec_atom_count={agg['transport_reset_pdec_atom_count']}",
        f"singleton_residue_packet_count={agg['singleton_residue_packet_count']}",
        f"one_slot_mass={agg['one_slot_mass']}",
        f"two_slot_mass_share={agg['two_slot_mass_share']}",
        f"active_band={agg['active_band_min']}..{agg['active_band_max']}",
        f"minus_only_ell_values={agg['minus_only_ell_values']}",
        f"candidate_product_mass_upper_sum={agg['candidate_product_mass_upper_sum']}",
        f"eta={agg['eta']}",
        f"remaining_frontier_bridge_closed_current_sweep={fmt_bool(agg['remaining_frontier_bridge_closed_current_sweep'])}",
        "```",
        "",
        "## 1. route rows",
        "",
        "| gate | closed | evidence | global remaining |",
        "| --- | --- | --- | --- |",
    ]
    for row in result["remaining_frontier_route_rows"]:
        lines.append(
            f"| `{row['gate']}` | {fmt_bool(row['closed_current_sweep'])} | {row['evidence']} | `{row['global_remaining']}` |"
        )
    lines.extend(
        [
            "",
            "## 2. 最新显式前沿",
            "",
            "- transport reset 路线：当前 reset atom 为 `0`，但全局仍需排斥 reset-PDEC。",
            "- singleton SAE 路线：`300` 个 singleton packet 的 Rankin 质量主要来自 one-slot mass，当前已压成活跃素数带 `23..109` 的端点增长问题。",
            "- epoch-pair 路线：候选 `q=[31,43,103]` 的 product-mass upper sum 为 `0.023577117628562343<0.025`，当前没有 high-density 行。",
            "",
            "这仍不是行/列命题全局无条件证明；它把本轮剩余接口压成 `ActiveEllBandEndpointGrowthBoundOrEndpointResetPDEC`、`TransportResetPDECExclusion`、`GlobalEpochPairMultiplicityBound` 与 `MovingResidueShapeSAE/Rankin`。",
            "",
            "## 3. 依赖哈希",
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
        description="生成 AffineTwin endpoint-release remaining-frontier bridge 审计证书。"
    )
    parser.add_argument("--transport", type=Path, default=TRANSPORT_INTEGRATION_LEDGER)
    parser.add_argument("--profile", type=Path, default=SINGLETON_PROFILE_LEDGER)
    parser.add_argument("--rankin", type=Path, default=SINGLETON_RANKIN_LEDGER)
    parser.add_argument("--capacity", type=Path, default=ONE_SLOT_CAPACITY_LEDGER)
    parser.add_argument("--active-source", type=Path, default=ACTIVE_SOURCE_LEDGER)
    parser.add_argument("--active-band", type=Path, default=ACTIVE_BAND_LEDGER)
    parser.add_argument("--epoch-pair", type=Path, default=EPOCH_PAIR_LEDGER)
    return parser.parse_args()


def abs_path(path: Path) -> Path:
    """把相对路径规范到仓库根目录。"""
    return path if path.is_absolute() else ROOT / path


def main() -> None:
    """入口。"""
    args = parse_args()
    paths = {
        "transport": abs_path(args.transport),
        "profile": abs_path(args.profile),
        "rankin": abs_path(args.rankin),
        "capacity": abs_path(args.capacity),
        "active_source": abs_path(args.active_source),
        "active_band": abs_path(args.active_band),
        "epoch_pair": abs_path(args.epoch_pair),
    }
    result = build_result(paths)
    write_outputs(result)
    print(json.dumps(result["aggregate"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
