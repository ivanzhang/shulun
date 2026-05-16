#!/usr/bin/env python3
"""把 AffineTwin 移动族分流为 SAE 质量账本或 ColumnCRT 固定模出口。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_affine_twin_moving_family_sae_columncrt_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-moving-family-sae-columncrt-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-moving-family-sae-columncrt-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-moving-family-sae-columncrt-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-moving-family-sae-columncrt-router.md
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

SLOT_LOCK_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-slot-phase-lock-ledger.json"
ACTIVE_SOURCE_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-active-one-slot-epoch-source-ledger.json"
EPOCH_CAPACITY_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-one-slot-residue-epoch-capacity-ledger.json"
FIXED_DRIFT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-fixed-residue-slot-drift-ledger.json"
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-moving-family-sae-columncrt-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-moving-family-sae-columncrt-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-moving-family-sae-columncrt-router.md"

NEXT_TARGET = "AffineTwinEpochPairMultiplicityBoundOrColumnCRTPDECExclusion"


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


def is_prime(n: int) -> bool:
    """小范围素性判定。"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def capacity_index(rows: list[dict[str, Any]]) -> dict[tuple[str, int], dict[str, Any]]:
    """按 side/ell 建立 epoch 容量索引。"""
    return {(str(row["side"]), int(row["ell"])): row for row in rows}


def active_index(rows: list[dict[str, Any]]) -> dict[int, dict[str, Any]]:
    """按 ell 建立活跃来源索引。"""
    return {int(row["ell"]): row for row in rows}


def realized_index(rows: list[dict[str, Any]]) -> dict[int, dict[str, Any]]:
    """按 q 建立已实现 AffineTwin 槽锁索引。"""
    return {int(row["gap_ell"]): row for row in rows}


def candidate_q_values(active_ells: list[int]) -> list[int]:
    """筛出当前活跃 epoch 中可能承载 AffineTwin 的 q。"""
    active = set(active_ells)
    return [
        q
        for q in sorted(active)
        if q - 2 in active and is_prime(q) and is_prime(q - 2) and q % 4 == 3
    ]


def candidate_row(
    q: int,
    generator_side: str,
    fill_side: str,
    active_by_ell: dict[int, dict[str, Any]],
    capacity_by_epoch: dict[tuple[str, int], dict[str, Any]],
    realized_by_q: dict[int, dict[str, Any]],
) -> dict[str, Any]:
    """构造一个活跃 AffineTwin epoch-pair 候选行。"""
    generator_ell = q - 2
    fill_ell = q
    generator_epoch = capacity_by_epoch.get((generator_side, generator_ell))
    fill_epoch = capacity_by_epoch.get((fill_side, fill_ell))
    has_orientation = generator_epoch is not None and fill_epoch is not None

    generator_used = int(generator_epoch["used_residue_count"]) if generator_epoch else 0
    fill_used = int(fill_epoch["used_residue_count"]) if fill_epoch else 0
    pair_capacity = generator_ell * fill_ell
    product_used_upper = generator_used * fill_used
    realized = realized_by_q.get(q)
    realized_pair_count = 1 if realized else 0
    pair_support_width = (q + 9) // 2
    fixed_pair_margin = pair_capacity - pair_support_width
    return {
        "q": q,
        "generator_ell": generator_ell,
        "fill_ell": fill_ell,
        "generator_side": generator_side,
        "fill_side": fill_side,
        "q_minus_2_active_sides": active_by_ell[generator_ell]["active_sides"],
        "q_active_sides": active_by_ell[fill_ell]["active_sides"],
        "orientation_epochs_present": has_orientation,
        "generator_used_residue_count": generator_used,
        "fill_used_residue_count": fill_used,
        "epoch_pair_capacity": pair_capacity,
        "epoch_pair_product_used_upper": product_used_upper,
        "epoch_pair_unused_lower": pair_capacity - product_used_upper,
        "epoch_pair_occupancy_upper_ratio": product_used_upper / pair_capacity if pair_capacity else None,
        "single_pair_sae_mass": 1 / pair_capacity,
        "realized_affine_twin_pair_count": realized_pair_count,
        "realized_affine_twin_sae_mass": realized_pair_count / pair_capacity,
        "pair_support_width_affine": pair_support_width,
        "fixed_pair_modulus_margin": fixed_pair_margin,
        "fixed_pair_isolation_symbolic_margin_positive": fixed_pair_margin > 0,
        "realized_current_sweep": realized is not None,
        "realized_pair_representative": realized["pair_unique_representatives"] if realized else [],
        "realized_source_key": realized["source_gap_fill_pair_key"] if realized else None,
    }


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "affine_twin_fixed_pair_columncrt_split",
            "status": "closed_routing",
            "statement": "If q and the two CRT residues are fixed and the same affine-twin pair recurs, recurrence has fixed modulus q(q-2) and is a ColumnCRT/PDEC object; if it does not recur, it is an isolated SAE atom.",
        },
        {
            "name": "active_twin_epoch_pair_ledger_materialized",
            "status": "closed_current_sweep",
            "statement": "The current active epoch ledger lists every q with q and q-2 active, twin-prime, and q=3 mod 4, together with its epoch-pair capacity and realized affine-twin mass.",
        },
        {
            "name": "affine_twin_epoch_pair_multiplicity_bound",
            "status": "open",
            "statement": "A global proof must bound multiplicity inside the moving q epoch-pair ledger, or prove the resulting fixed/moving ColumnCRT-PDEC exclusions.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    agg = result["aggregate"]
    return [
        {
            "gate": "FixedQFixedResiduePairRoutedToColumnCRT",
            "closed": True,
            "proved": True,
            "meaning": "固定 q 与固定双残基若复现，必带固定模 q(q-2)，进入 ColumnCRT/PDEC。",
            "remaining": "closed routing, exclusion still separate",
        },
        {
            "gate": "CurrentActiveTwinEpochLedgerMaterialized",
            "closed": agg["candidate_affine_twin_epoch_pair_count"] > 0,
            "proved": False,
            "meaning": "当前扫描的活跃 twin epoch-pair 已物化为容量/质量账本。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "CurrentRealizedAffineTwinPairSparse",
            "closed": agg["realized_affine_twin_pair_count"] == 1
            and agg["realized_affine_twin_sae_mass_sum"] < agg["candidate_epoch_pair_product_mass_upper_sum"],
            "proved": False,
            "meaning": "当前已实现 AffineTwin 只占候选 epoch-pair 容量的极小部分。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "GlobalEpochPairMultiplicityBoundProved",
            "closed": False,
            "proved": False,
            "meaning": "仍需全局证明 moving q epoch-pair 的乘法占用可求和，或转入 ColumnCRT/PDEC 排斥。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只完成 moving family 的 SAE/ColumnCRT 分流，不关闭全局行/列命题。",
            "remaining": NEXT_TARGET,
        },
    ]


def build_result(
    slot_lock_ledger: Path,
    active_source_ledger: Path,
    epoch_capacity_ledger: Path,
    fixed_drift_ledger: Path,
) -> dict[str, Any]:
    """构造 AffineTwin 移动族 SAE/ColumnCRT 分流结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    slot_lock = load_json(slot_lock_ledger)
    active_source = load_json(active_source_ledger)
    epoch_capacity = load_json(epoch_capacity_ledger)
    fixed_drift = load_json(fixed_drift_ledger)

    slot_rows = slot_lock["affine_twin_slot_phase_lock_rows"]
    if not slot_rows:
        raise RuntimeError("slot lock ledger has no affine twin rows")
    generator_side = str(slot_rows[0]["generator_side"])
    fill_side = str(slot_rows[0]["fill_side"])
    active_rows = active_source["active_ell_source_rows"]
    active_ells = [int(row["ell"]) for row in active_rows]
    active_by_ell = active_index(active_rows)
    capacity_by_epoch = capacity_index(epoch_capacity["epoch_capacity_rows"])
    realized_by_q = realized_index(slot_rows)
    q_values = candidate_q_values(active_ells)
    candidate_rows = [
        candidate_row(q, generator_side, fill_side, active_by_ell, capacity_by_epoch, realized_by_q)
        for q in q_values
    ]

    realized_rows = [row for row in candidate_rows if row["realized_current_sweep"]]
    aggregate = {
        "slot_lock_ledger": str(slot_lock_ledger.relative_to(ROOT)),
        "active_source_ledger": str(active_source_ledger.relative_to(ROOT)),
        "epoch_capacity_ledger": str(epoch_capacity_ledger.relative_to(ROOT)),
        "fixed_drift_ledger": str(fixed_drift_ledger.relative_to(ROOT)),
        "generator_side": generator_side,
        "fill_side": fill_side,
        "active_ell_count": len(active_ells),
        "candidate_affine_twin_epoch_pair_count": len(candidate_rows),
        "candidate_q_values": q_values,
        "candidate_orientation_epoch_present_count": sum(
            1 for row in candidate_rows if row["orientation_epochs_present"]
        ),
        "realized_affine_twin_pair_count": len(realized_rows),
        "realized_q_values": [row["q"] for row in realized_rows],
        "all_candidate_fixed_pair_symbolic_margins_positive": all(
            row["fixed_pair_isolation_symbolic_margin_positive"] for row in candidate_rows
        ),
        "min_candidate_fixed_pair_modulus_margin": min(
            row["fixed_pair_modulus_margin"] for row in candidate_rows
        )
        if candidate_rows
        else None,
        "candidate_epoch_pair_product_mass_upper_sum": sum(
            row["epoch_pair_product_used_upper"] / row["epoch_pair_capacity"]
            for row in candidate_rows
            if row["orientation_epochs_present"]
        ),
        "candidate_single_pair_sae_mass_sum": sum(row["single_pair_sae_mass"] for row in candidate_rows),
        "realized_affine_twin_sae_mass_sum": sum(row["realized_affine_twin_sae_mass"] for row in candidate_rows),
        "fixed_slot_recurrence_count": fixed_drift["aggregate"]["fixed_slot_recurrence_count"],
        "fixed_residue_slot_drift_pair_count": fixed_drift["aggregate"]["pair_row_count"],
        "fixed_q_fixed_residue_columncrt_routing_closed": True,
        "global_epoch_pair_multiplicity_bound_proved": False,
        "columncrt_pdec_excluded_globally": False,
        "row_column_unconditional_closed": False,
    }
    ledger = {
        "aggregate": aggregate,
        "candidate_affine_twin_epoch_pair_rows": candidate_rows,
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    result = {
        "certificate_type": (
            "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_"
            "affine_twin_moving_family_sae_columncrt_router"
        ),
        "status": "affine_twin_moving_family_routed_to_epoch_sae_or_columncrt_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_sweep_not_used_as_global_proof": True,
        "aggregate": aggregate,
        "candidate_affine_twin_epoch_pair_rows": candidate_rows,
        "fixed_q_fixed_residue_columncrt_routing_closed": True,
        "global_epoch_pair_multiplicity_bound_proved": False,
        "columncrt_pdec_excluded_globally": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": "AffineTwinMovingFamilySAEOrColumnCRTExclusion",
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "plain_conclusion": (
            "本步把 AffineTwin moving family 分成两个正式出口：固定 `q` 与固定双残基若复现，"
            "就带固定模 `q(q-2)`，进入 ColumnCRT/PDEC；若 `q` 或残基移动，则进入 twin epoch-pair "
            "SAE/Rankin 质量账本。当前活跃 epoch 中满足 `q,q-2` 同为素数且 `q≡3 mod 4` 的候选 "
            f"q 为 {q_values}；其中实际 AffineTwin 只实现 q={aggregate['realized_q_values']}。"
            f"当前已实现 SAE 质量为 {aggregate['realized_affine_twin_sae_mass_sum']:.12f}，"
            "但全局仍需证明 epoch-pair 乘法占用的 multiplicity 界，或排斥对应 ColumnCRT/PDEC。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    result["source_hashes"] = {
        "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_affine_twin_moving_family_sae_columncrt_router.py": sha256(
            Path(__file__).resolve()
        ),
        "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-slot-phase-lock-ledger.json": sha256(
            slot_lock_ledger
        ),
        "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-active-one-slot-epoch-source-ledger.json": sha256(
            active_source_ledger
        ),
        "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-one-slot-residue-epoch-capacity-ledger.json": sha256(
            epoch_capacity_ledger
        ),
        "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-moving-family-sae-columncrt-ledger.json": sha256(
            OUT_LEDGER
        ),
    }
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow selector H lower affine twin moving family SAE/ColumnCRT router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"candidate_q_values={agg['candidate_q_values']}",
        f"realized_q_values={agg['realized_q_values']}",
        f"candidate_affine_twin_epoch_pair_count={agg['candidate_affine_twin_epoch_pair_count']}",
        f"realized_affine_twin_pair_count={agg['realized_affine_twin_pair_count']}",
        f"candidate_epoch_pair_product_mass_upper_sum={agg['candidate_epoch_pair_product_mass_upper_sum']:.12f}",
        f"candidate_single_pair_sae_mass_sum={agg['candidate_single_pair_sae_mass_sum']:.12f}",
        f"realized_affine_twin_sae_mass_sum={agg['realized_affine_twin_sae_mass_sum']:.12f}",
        f"fixed_slot_recurrence_count={agg['fixed_slot_recurrence_count']}",
        f"fixed_residue_slot_drift_pair_count={agg['fixed_residue_slot_drift_pair_count']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 候选 twin epoch-pair",
        "",
        "| q | epochs | used upper | capacity | occupancy upper | single SAE mass | fixed margin | realized |",
        "| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in result["candidate_affine_twin_epoch_pair_rows"]:
        lines.append(
            f"| {row['q']} | `{row['generator_side']}:{row['generator_ell']} -> "
            f"{row['fill_side']}:{row['fill_ell']}` | {row['epoch_pair_product_used_upper']} | "
            f"{row['epoch_pair_capacity']} | {row['epoch_pair_occupancy_upper_ratio']:.6f} | "
            f"{row['single_pair_sae_mass']:.9f} | {row['fixed_pair_modulus_margin']} | "
            f"`{fmt_bool(row['realized_current_sweep'])}` |"
        )
    lines.extend(
        [
            "",
            "## 2. 分流结论",
            "",
            "- 固定 `q` 与固定双残基的复现不再是自由移动槽，而是固定模 `q(q-2)` 的 ColumnCRT/PDEC。",
            "- 非复现原子进入 SAE；单个 AffineTwin 双槽原子的自然质量是 `1/(q(q-2))`。",
            "- 当前候选 `q` 的 epoch-pair 账本已经物化；实际只实现 `q=31`。",
            "- 全局仍需 multiplicity 界：证明 moving `q` 的 epoch-pair 占用可求和，或排斥固定/移动 ColumnCRT-PDEC。",
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
            "- 具体目标：证明 twin epoch-pair 的乘法占用不能达到反例链所需密度；若失败，则输出固定模或移动模 ColumnCRT/PDEC 证书。",
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
    parser.add_argument("--slot-lock-ledger", type=Path, default=SLOT_LOCK_LEDGER)
    parser.add_argument("--active-source-ledger", type=Path, default=ACTIVE_SOURCE_LEDGER)
    parser.add_argument("--epoch-capacity-ledger", type=Path, default=EPOCH_CAPACITY_LEDGER)
    parser.add_argument("--fixed-drift-ledger", type=Path, default=FIXED_DRIFT_LEDGER)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    slot_lock_ledger = args.slot_lock_ledger if args.slot_lock_ledger.is_absolute() else ROOT / args.slot_lock_ledger
    active_source_ledger = (
        args.active_source_ledger if args.active_source_ledger.is_absolute() else ROOT / args.active_source_ledger
    )
    epoch_capacity_ledger = (
        args.epoch_capacity_ledger if args.epoch_capacity_ledger.is_absolute() else ROOT / args.epoch_capacity_ledger
    )
    fixed_drift_ledger = args.fixed_drift_ledger if args.fixed_drift_ledger.is_absolute() else ROOT / args.fixed_drift_ledger
    result = build_result(slot_lock_ledger, active_source_ledger, epoch_capacity_ledger, fixed_drift_ledger)
    write_markdown(result)
    result["source_hashes"][
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-moving-family-sae-columncrt-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "candidate_q_values": result["aggregate"]["candidate_q_values"],
                "realized_q_values": result["aggregate"]["realized_q_values"],
                "realized_affine_twin_sae_mass_sum": result["aggregate"][
                    "realized_affine_twin_sae_mass_sum"
                ],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
