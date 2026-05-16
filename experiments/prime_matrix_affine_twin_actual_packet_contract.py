#!/usr/bin/env python3
"""生成 AffineTwin actual packet 临界负载合同。

用法示例：
  python3 experiments/prime_matrix_affine_twin_actual_packet_contract.py
  python3 -m json.tool data/prime-matrix-affine-twin-actual-packet-contract-ledger.json

输出：
  data/prime-matrix-affine-twin-actual-packet-contract-ledger.json
  docs/monograph/prime-matrix-affine-twin-actual-packet-contract.json
  docs/monograph/prime-matrix-affine-twin-actual-packet-contract.md
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

SLOT_LEDGER = DATA / (
    "square-phase-offband-prefix-gap-shadow-selector-h-lower-"
    "affine-twin-slot-phase-lock-ledger.json"
)
SQRT_LEDGER = DATA / (
    "square-phase-offband-prefix-gap-shadow-selector-h-lower-"
    "affine-twin-sqrt-product-brun-ledger.json"
)
PRESSURE_LEDGER = DATA / (
    "square-phase-offband-prefix-gap-shadow-selector-h-lower-"
    "affine-twin-paired-side-pressure-ledger.json"
)

OUT_LEDGER = DATA / "prime-matrix-affine-twin-actual-packet-contract-ledger.json"
OUT_JSON = DOCS / "prime-matrix-affine-twin-actual-packet-contract.json"
OUT_MD = DOCS / "prime-matrix-affine-twin-actual-packet-contract.md"


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


def primitive_width(q: int) -> int:
    """primitive AffineTwin 双槽支撑宽度。"""
    return (q + 9) // 2


def build_result(slot_path: Path, sqrt_path: Path, pressure_path: Path) -> dict[str, Any]:
    """构造 actual packet 合同结果。"""
    slot = load_json(slot_path)
    sqrt = load_json(sqrt_path)
    pressure = load_json(pressure_path)

    actual_rows_by_q: dict[int, list[dict[str, Any]]] = {}
    for row in slot.get("affine_twin_slot_phase_lock_rows", []):
        q = int(row["gap_ell"])
        actual_rows_by_q.setdefault(q, []).append(row)

    pressure_by_q = {int(row["q"]): row for row in pressure["paired_side_pressure_rows"]}

    rows: list[dict[str, Any]] = []
    for row in sqrt["sqrt_product_q_rows"]:
        q = int(row["q"])
        capacity = int(row["epoch_pair_capacity"])
        formal_product = int(row["epoch_pair_product_used_upper"])
        actual_packet_count = len(actual_rows_by_q.get(q, []))
        width = primitive_width(q)
        actual_square = actual_packet_count * actual_packet_count
        formal_square = formal_product * formal_product
        pressure_row = pressure_by_q.get(q, {})
        support_injection_passed = actual_packet_count <= width
        actual_sqrt_gate_passed = actual_square <= capacity
        projection_collision_current = actual_packet_count > width
        formal_overcounts_actual = formal_product > actual_packet_count
        route = "ActualPrimitiveSupportAbsorbed"
        if projection_collision_current:
            route = "ProjectionCollision-PDEC"
        elif formal_overcounts_actual and actual_packet_count > 0:
            route = "ActualPrimitiveSupportAbsorbed+ProductAccountingTightening"
        elif formal_overcounts_actual:
            route = "NoActualPacketCurrentSweep+ProductAccountingTightening"

        rows.append(
            {
                "q": q,
                "capacity_q_q_minus_2": capacity,
                "primitive_support_width": width,
                "formal_product_upper_M_form": formal_product,
                "formal_square_load": formal_square,
                "actual_packet_count_N_q_current": actual_packet_count,
                "actual_square_load": actual_square,
                "formal_to_actual_gap": formal_product - actual_packet_count,
                "support_injection_passed_current": support_injection_passed,
                "actual_sqrt_gate_passed_current": actual_sqrt_gate_passed,
                "formal_sqrt_gate_passed_current": bool(
                    row["sqrt_product_gate_passed_current_sweep"]
                ),
                "projection_collision_pdec_current": projection_collision_current,
                "formal_overcounts_actual_current": formal_overcounts_actual,
                "actual_load_ratio": actual_square / capacity if capacity else None,
                "formal_load_ratio": formal_square / capacity if capacity else None,
                "paired_pressure_product": pressure_row.get(
                    "paired_side_pressure_product", {}
                ).get("decimal"),
                "realized_current_sweep": bool(row["realized_current_sweep"]),
                "route_current": route,
                "actual_packet_keys": [
                    actual_row.get("source_gap_fill_pair_key")
                    for actual_row in actual_rows_by_q.get(q, [])
                ],
            }
        )

    aggregate = {
        "slot_ledger": str(slot_path.relative_to(ROOT)),
        "sqrt_ledger": str(sqrt_path.relative_to(ROOT)),
        "pressure_ledger": str(pressure_path.relative_to(ROOT)),
        "candidate_q_values": [row["q"] for row in rows],
        "actual_q_values_current": [
            row["q"] for row in rows if row["actual_packet_count_N_q_current"] > 0
        ],
        "total_formal_product_upper": sum(
            row["formal_product_upper_M_form"] for row in rows
        ),
        "total_actual_packet_count_current": sum(
            row["actual_packet_count_N_q_current"] for row in rows
        ),
        "total_formal_to_actual_gap": sum(row["formal_to_actual_gap"] for row in rows),
        "all_actual_packets_in_primitive_support_current": all(
            row["support_injection_passed_current"] for row in rows
        ),
        "all_actual_packets_pass_sqrt_gate_current": all(
            row["actual_sqrt_gate_passed_current"] for row in rows
        ),
        "projection_collision_pdec_count_current": sum(
            1 for row in rows if row["projection_collision_pdec_current"]
        ),
        "formal_overcount_q_count_current": sum(
            1 for row in rows if row["formal_overcounts_actual_current"]
        ),
        "max_actual_load_ratio_current": max(
            (row["actual_load_ratio"] or 0 for row in rows),
            default=0,
        ),
        "max_formal_load_ratio_current": max(
            (row["formal_load_ratio"] or 0 for row in rows),
            default=0,
        ),
        "product_accounting_tightening_needed_globally": True,
        "primitive_twin_slot_support_exhaustion_proved_globally": False,
        "primitive_support_escape_excluded_globally": False,
        "row_column_unconditional_closed": False,
    }

    result = {
        "certificate_type": "prime_matrix_affine_twin_actual_packet_contract",
        "status": "current_sweep_actual_packet_contract_closed_global_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "aggregate": aggregate,
        "actual_packet_rows": rows,
        "theorem_contract": {
            "name": "PM-ActualPacketCriticalLoadContract",
            "actual_load": "N_q^2",
            "formal_envelope": "(A_g A_f)^2",
            "critical_capacity": "q(q-2)",
            "closed_current_sweep": aggregate[
                "all_actual_packets_pass_sqrt_gate_current"
            ],
            "global_remaining": [
                "ProductAccountingTightening",
                "PrimitiveTwinSlotSupportExhaustion",
                "PrimitiveTwinSlotSupportEscape-PDEC/SAE",
            ],
        },
        "dependency_hashes": {
            str(path.relative_to(ROOT)): sha256(path)
            for path in (slot_path, sqrt_path, pressure_path)
        },
    }
    return result


def write_outputs(result: dict[str, Any]) -> None:
    """写出 JSON 和 Markdown。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    for path in (OUT_LEDGER, OUT_JSON):
        path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    agg = result["aggregate"]
    lines = [
        "# Prime Matrix AffineTwin actual packet critical-load contract",
        "",
        "**状态：** `current_sweep_actual_packet_contract_closed_global_open`",
        "",
        "本合同把 AffineTwin 平方根门从形式包络 `M_q^{form}=A_g A_f` 改写为实际非 PDEC packet 数 `N_q`。",
        "当前 sweep 中 actual packets 全部注入 primitive 支撑，并满足 actual 平方根门；全局仍需证明 primitive 支撑耗尽、收紧形式乘积账本并排斥支撑逃逸。",
        "",
        "```text",
        f"candidate_q_values={agg['candidate_q_values']}",
        f"actual_q_values_current={agg['actual_q_values_current']}",
        f"total_formal_product_upper={agg['total_formal_product_upper']}",
        f"total_actual_packet_count_current={agg['total_actual_packet_count_current']}",
        f"total_formal_to_actual_gap={agg['total_formal_to_actual_gap']}",
        f"all_actual_packets_pass_sqrt_gate_current={fmt_bool(agg['all_actual_packets_pass_sqrt_gate_current'])}",
        f"projection_collision_pdec_count_current={agg['projection_collision_pdec_count_current']}",
        f"row_column_unconditional_closed={fmt_bool(agg['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. actual packet 表",
        "",
        "| q | M_form | N_q current | support W | capacity | formal load ratio | actual load ratio | route |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in result["actual_packet_rows"]:
        lines.append(
            "| {q} | {formal} | {actual} | {width} | {capacity} | {fr:.6f} | {ar:.6f} | `{route}` |".format(
                q=row["q"],
                formal=row["formal_product_upper_M_form"],
                actual=row["actual_packet_count_N_q_current"],
                width=row["primitive_support_width"],
                capacity=row["capacity_q_q_minus_2"],
                fr=row["formal_load_ratio"] or 0,
                ar=row["actual_load_ratio"] or 0,
                route=table_cell(row["route_current"]),
            )
        )
    lines.extend(
        [
            "",
            "## 2. 结论",
            "",
            "- 当前 sweep 的 actual load 为 `N_q^2`，不是形式上界 `(A_g A_f)^2`。",
            "- 当前 actual packets 全部满足 `N_q <= W_q <= sqrt(q(q-2))`。",
            "- 形式包络和 actual load 的差额被登记为 `ProductAccountingTightening`，不能作为真实矛盾使用。",
            "- 若未来出现 `N_q>W_q`，它必须进入 `ProjectionCollision-PDEC/ColumnCRT`。",
            "- 若 actual packet 不落入 primitive 支撑，它必须进入 `PrimitiveTwinSlotSupportEscape-PDEC/SAE`。",
            "",
            "## 3. 仍未闭合",
            "",
            "- 全局 `PrimitiveTwinSlotSupportExhaustion` 尚未证明。",
            "- 全局 `ProductAccountingTightening` 尚未完成。",
            "- `PrimitiveTwinSlotSupportEscape-PDEC/SAE` 尚未排斥。",
            "- 因此行/列命题仍未无条件闭合。",
            "",
            "## 4. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in result["dependency_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(
        description="生成 AffineTwin actual packet 临界负载合同。"
    )
    parser.add_argument("--slot-ledger", type=Path, default=SLOT_LEDGER)
    parser.add_argument("--sqrt-ledger", type=Path, default=SQRT_LEDGER)
    parser.add_argument("--pressure-ledger", type=Path, default=PRESSURE_LEDGER)
    return parser.parse_args()


def main() -> None:
    """入口。"""
    args = parse_args()
    result = build_result(args.slot_ledger, args.sqrt_ledger, args.pressure_ledger)
    write_outputs(result)
    print(json.dumps(result["aggregate"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
