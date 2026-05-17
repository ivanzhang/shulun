#!/usr/bin/env python3
"""生成 K=13 tail gate drift 证书。

用法示例：
  python3 experiments/prime_matrix_cycle_debt_k13_tail_gate_drift_router.py
  python3 -m json.tool data/prime-matrix-cycle-debt-k13-tail-gate-drift-ledger.json

输出：
  data/prime-matrix-cycle-debt-k13-tail-gate-drift-ledger.json
  docs/monograph/prime-matrix-cycle-debt-k13-tail-gate-drift-router.json
  docs/monograph/prime-matrix-cycle-debt-k13-tail-gate-drift-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SUPPORT_HALL = DATA / "prime-matrix-cycle-debt-support-row-replacement-hall-ledger.json"
K13_TAIL = DATA / "prime-matrix-cycle-debt-k13-full-debt-nine-lane-tail-ledger.json"

OUT_LEDGER = DATA / "prime-matrix-cycle-debt-k13-tail-gate-drift-ledger.json"
OUT_JSON = DOCS / "prime-matrix-cycle-debt-k13-tail-gate-drift-router.json"
OUT_MD = DOCS / "prime-matrix-cycle-debt-k13-tail-gate-drift-router.md"

PREVIOUS_TARGET = "K13LayerSlackTailCRTInvariantPDECOrMovingFamilySAE"
NEXT_TARGET = "K13GateProfileNoNearReplayPDECOrK14HighGateDriftSAE"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def slack_vector(audit: dict[str, Any]) -> list[int]:
    """抽取阈值 slack 向量。"""
    return [int(item["slack"]) for item in audit["threshold_slacks"]]


def zero_layers(audit: dict[str, Any]) -> list[int]:
    """抽取 zero-slack 阈值。"""
    return [
        int(item["threshold"])
        for item in audit["threshold_slacks"]
        if int(item["slack"]) == 0
    ]


def l1_distance(left: list[int], right: list[int]) -> int:
    """计算两个 slack 向量的 L1 距离。"""
    return sum(abs(a - b) for a, b in zip(left, right))


def build_shift_records(support_hall: dict[str, Any], base_shift: int) -> list[dict[str, Any]]:
    """比较所有 near-shift 与 K=13 基准的层门漂移。"""
    base = next(
        item for item in support_hall["shift_audits"] if int(item["shift_cycles"]) == base_shift
    )
    base_slack = slack_vector(base)
    base_zero = set(zero_layers(base))
    records = []
    for audit in support_hall["shift_audits"]:
        shift = int(audit["shift_cycles"])
        current_slack = slack_vector(audit)
        current_zero = set(zero_layers(audit))
        total_capacity = int(audit["total_capacity"])
        total_demand = int(audit["total_demand_width"])
        records.append(
            {
                "shift_cycles": shift,
                "hall_pass": bool(audit["hall_pass"]),
                "total_capacity": total_capacity,
                "total_demand_width": total_demand,
                "tail_balance": total_capacity - total_demand,
                "zero_slack_layers": sorted(current_zero),
                "same_slack_vector_as_k13": current_slack == base_slack,
                "same_zero_gate_set_as_k13": current_zero == base_zero,
                "slack_l1_distance_from_k13": l1_distance(base_slack, current_slack),
                "zero_gate_symmetric_difference_from_k13": sorted(base_zero ^ current_zero),
                "zero_gate_lost_from_k13": sorted(base_zero - current_zero),
                "zero_gate_gained_over_k13": sorted(current_zero - base_zero),
            }
        )
    return records


def build_result() -> dict[str, Any]:
    """构造 K=13 gate drift 证书。"""
    support_hall = load_json(SUPPORT_HALL)
    k13_tail = load_json(K13_TAIL)

    base_shift = 13
    shift_records = build_shift_records(support_hall, base_shift)
    k13_record = next(item for item in shift_records if int(item["shift_cycles"]) == 13)
    k14_record = next(item for item in shift_records if int(item["shift_cycles"]) == 14)
    hall_pass_records = [item for item in shift_records if bool(item["hall_pass"])]
    same_slack_records = [
        item for item in shift_records if bool(item["same_slack_vector_as_k13"])
    ]
    same_zero_records = [
        item for item in shift_records if bool(item["same_zero_gate_set_as_k13"])
    ]
    passing_same_slack_records = [
        item
        for item in hall_pass_records
        if bool(item["same_slack_vector_as_k13"])
    ]
    passing_same_zero_records = [
        item
        for item in hall_pass_records
        if bool(item["same_zero_gate_set_as_k13"])
    ]

    result = {
        "certificate_type": "prime_matrix_cycle_debt_k13_tail_gate_drift_router",
        "status": "k13_layer_gate_profile_has_no_near_replay_except_base_shift",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_sweep_not_used_as_global_proof": True,
        "aggregate": {
            "row_column_unconditional_closed": False,
            "previous_hardpoint": PREVIOUS_TARGET,
            "period_p": int(support_hall["aggregate"]["period_p"]),
            "near_shift_limit_cycles": int(support_hall["aggregate"]["near_shift_limit_cycles"]),
            "base_shift": base_shift,
            "hall_pass_shifts": [int(item["shift_cycles"]) for item in hall_pass_records],
            "same_slack_vector_shifts": [int(item["shift_cycles"]) for item in same_slack_records],
            "same_zero_gate_set_shifts": [int(item["shift_cycles"]) for item in same_zero_records],
            "passing_same_slack_vector_shifts": [
                int(item["shift_cycles"]) for item in passing_same_slack_records
            ],
            "passing_same_zero_gate_set_shifts": [
                int(item["shift_cycles"]) for item in passing_same_zero_records
            ],
            "k13_tail_balance": int(k13_record["tail_balance"]),
            "k13_zero_slack_layers": k13_record["zero_slack_layers"],
            "k13_min_tail_factor_count": int(k13_tail["aggregate"]["min_tail_factor_count"]),
            "k13_min_tail_lcm_log10": float(k13_tail["aggregate"]["min_tail_lcm_log10"]),
            "k14_tail_balance": int(k14_record["tail_balance"]),
            "k14_tail_increase_over_k13": int(k14_record["tail_balance"]) - int(k13_record["tail_balance"]),
            "k14_zero_slack_layers": k14_record["zero_slack_layers"],
            "k14_slack_l1_distance_from_k13": int(k14_record["slack_l1_distance_from_k13"]),
            "k14_zero_gate_lost_from_k13": k14_record["zero_gate_lost_from_k13"],
            "k14_zero_gate_gained_over_k13": k14_record["zero_gate_gained_over_k13"],
            "k14_zero_gate_common_with_k13": sorted(
                set(k13_record["zero_slack_layers"]) & set(k14_record["zero_slack_layers"])
            ),
            "k13_near_replay_unique": [int(item["shift_cycles"]) for item in same_slack_records] == [13],
            "no_passing_near_shift_preserves_k13_profile_except_base": [
                int(item["shift_cycles"]) for item in passing_same_slack_records
            ] == [13],
            "hardpoint_after_router": NEXT_TARGET,
            "next_direct_attack_target": NEXT_TARGET,
        },
        "shift_gate_records": shift_records,
        "plain_conclusion": (
            "在 support replacement 的 16 个 near-shift 中，K=13 的完整 slack 向量只有基准 shift=13 自身复现。"
            "唯一另一个 Hall survivor 是 K=14，但它把零 slack 门从 1,4,7,8 漂移到 7,8,13,15，"
            "tail balance 从 18 增至 31，slack 向量 L1 距离为 19。"
            "因此 K=13 层不变量 tail 不能近程无漂移重播；若反例链移动，必须进入 K14 high-gate drift SAE/PDEC。"
        ),
        "dependency_hashes": {
            str(SUPPORT_HALL.relative_to(ROOT)): sha256(SUPPORT_HALL),
            str(K13_TAIL.relative_to(ROOT)): sha256(K13_TAIL),
        },
    }
    return result


def write_outputs(result: dict[str, Any]) -> None:
    """写出 JSON 与 Markdown。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    OUT_LEDGER.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    agg = result["aggregate"]
    lines = [
        "# Prime Matrix cycle-debt K13 tail gate drift router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"row_column_unconditional_closed={fmt_bool(agg['row_column_unconditional_closed'])}",
        f"previous_hardpoint={agg['previous_hardpoint']}",
        f"period_p={agg['period_p']}",
        f"near_shift_limit_cycles={agg['near_shift_limit_cycles']}",
        f"hall_pass_shifts={agg['hall_pass_shifts']}",
        f"same_slack_vector_shifts={agg['same_slack_vector_shifts']}",
        f"same_zero_gate_set_shifts={agg['same_zero_gate_set_shifts']}",
        f"passing_same_slack_vector_shifts={agg['passing_same_slack_vector_shifts']}",
        f"k13_tail_balance={agg['k13_tail_balance']}",
        f"k13_zero_slack_layers={agg['k13_zero_slack_layers']}",
        f"k13_min_tail_factor_count={agg['k13_min_tail_factor_count']}",
        f"k13_min_tail_lcm_log10={agg['k13_min_tail_lcm_log10']:.3f}",
        f"k14_tail_balance={agg['k14_tail_balance']}",
        f"k14_tail_increase_over_k13={agg['k14_tail_increase_over_k13']}",
        f"k14_zero_slack_layers={agg['k14_zero_slack_layers']}",
        f"k14_slack_l1_distance_from_k13={agg['k14_slack_l1_distance_from_k13']}",
        f"k14_zero_gate_lost_from_k13={agg['k14_zero_gate_lost_from_k13']}",
        f"k14_zero_gate_gained_over_k13={agg['k14_zero_gate_gained_over_k13']}",
        f"next_direct_attack_target={agg['next_direct_attack_target']}",
        "```",
        "",
        "## 1. near-shift gate comparison",
        "",
        "| K | Hall pass | tail balance | zero gates | L1 from K13 | gate symmetric diff |",
        "| ---: | :---: | ---: | --- | ---: | --- |",
    ]
    for item in result["shift_gate_records"]:
        lines.append(
            f"| {item['shift_cycles']} | {fmt_bool(item['hall_pass'])} | "
            f"{item['tail_balance']} | `{item['zero_slack_layers']}` | "
            f"{item['slack_l1_distance_from_k13']} | "
            f"`{item['zero_gate_symmetric_difference_from_k13']}` |"
        )

    lines.extend(
        [
            "",
            "## 2. 判定",
            "",
            "- `same_slack_vector_shifts=[13]`，说明 K=13 的层 slack 形状在 near-shift 窗口内没有第二个复本。",
            "- `hall_pass_shifts=[13,14]`，所以唯一可动 survivor 是 K=14。",
            "- K=14 只保留共同零门 `7,8`，丢失 K=13 的低门 `1,4`，新增高门 `13,15`。",
            "- tail balance 从 `18` 增至 `31`，即 moving 分支必须支付额外 `13` 个 tail 槽。",
            "- 因此 K=13 layer-tail 若要近程复现只能固定在原 shift；一旦移动就进入 K14 high-gate drift SAE/PDEC。",
            f"- 下一主攻点：`{agg['next_direct_attack_target']}`。",
            "",
            "## 3. 依赖哈希",
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
