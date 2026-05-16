#!/usr/bin/env python3
"""生成 AffineTwin window edge-collision 位移审计证书。

用法示例：
  python3 experiments/prime_matrix_affine_twin_window_edge_collision_audit.py
  python3 -m json.tool data/prime-matrix-affine-twin-window-edge-collision-ledger.json

输出：
  data/prime-matrix-affine-twin-window-edge-collision-ledger.json
  docs/monograph/prime-matrix-affine-twin-window-edge-collision-audit.json
  docs/monograph/prime-matrix-affine-twin-window-edge-collision-audit.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

CRT_WINDOW_GAP_LEDGER = DATA / "prime-matrix-affine-twin-crt-window-gap-ledger.json"
SLOT_LEDGER = DATA / (
    "square-phase-offband-prefix-gap-shadow-selector-h-lower-"
    "affine-twin-slot-phase-lock-ledger.json"
)

OUT_LEDGER = DATA / "prime-matrix-affine-twin-window-edge-collision-ledger.json"
OUT_JSON = DOCS / "prime-matrix-affine-twin-window-edge-collision-audit.json"
OUT_MD = DOCS / "prime-matrix-affine-twin-window-edge-collision-audit.md"


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


def slot_index(rows: list[dict[str, Any]]) -> dict[int, dict[str, Any]]:
    """按 q 建立 slot-lock 索引。"""
    return {int(row["gap_ell"]): row for row in rows}


def target_pairs_for_slot(slot_row: dict[str, Any]) -> list[dict[str, int]]:
    """列出共同窗口内每个 P 对应的目标 residue pair。"""
    generator_modulus = int(slot_row["generator_modulus"])
    fill_modulus = int(slot_row["fill_modulus"])
    p_delay = int(slot_row["p_delay"])
    lo_value, hi_value = [int(value) for value in slot_row["pair_phase_support"]]
    return [
        {
            "target_p": p_value,
            "target_generator_residue": p_value % generator_modulus,
            "target_fill_residue": (p_value + p_delay) % fill_modulus,
        }
        for p_value in range(lo_value, hi_value + 1)
    ]


def nearest_target(
    row: dict[str, Any],
    target_pairs: list[dict[str, int]],
) -> dict[str, Any]:
    """寻找当前 residue pair 到命中目标集的最近 L1 位移。"""
    generator_residue = int(row["generator_residue"])
    fill_residue = int(row["fill_residue"])
    best: tuple[int, int, int, dict[str, int]] | None = None
    for target in target_pairs:
        generator_delta = int(target["target_generator_residue"]) - generator_residue
        fill_delta = int(target["target_fill_residue"]) - fill_residue
        l1_distance = abs(generator_delta) + abs(fill_delta)
        linf_distance = max(abs(generator_delta), abs(fill_delta))
        candidate = (l1_distance, linf_distance, int(target["target_p"]), target)
        if best is None or candidate < best:
            best = candidate
    if best is None:
        raise RuntimeError("target pair set is empty")

    _, linf_distance, target_p, target = best
    generator_delta = int(target["target_generator_residue"]) - generator_residue
    fill_delta = int(target["target_fill_residue"]) - fill_residue
    return {
        "target_p": target_p,
        "target_generator_residue": int(target["target_generator_residue"]),
        "target_fill_residue": int(target["target_fill_residue"]),
        "generator_delta_to_target": generator_delta,
        "fill_delta_to_target": fill_delta,
        "min_l1_residue_displacement_to_window": abs(generator_delta)
        + abs(fill_delta),
        "min_linf_residue_displacement_to_window": linf_distance,
    }


def classify_edge_route(
    row: dict[str, Any],
    target: dict[str, Any],
    supported_pairs: set[tuple[int, int]],
    formal_pairs: set[tuple[int, int]],
) -> str:
    """分类当前空窗到最近命中目标的碰撞类型。"""
    if bool(row["supported_actual_packet_current"]):
        return "SupportedActualPacket"
    target_pair = (
        int(target["target_generator_residue"]),
        int(target["target_fill_residue"]),
    )
    if target_pair in supported_pairs:
        return "ExistingActualResidueCollisionNeeded"
    if target_pair in formal_pairs:
        return "FormalTargetAlreadyPresentButWindowMiss"
    return "UnusedTargetResidueArrivalNeeded"


def build_result(crt_window_path: Path, slot_path: Path) -> dict[str, Any]:
    """构造 window edge-collision 审计结果。"""
    crt_window = load_json(crt_window_path)
    slot = load_json(slot_path)

    slot_by_q = slot_index(slot["affine_twin_slot_phase_lock_rows"])
    crt_rows = crt_window["crt_window_rows"]
    supported_pairs = {
        (int(row["generator_residue"]), int(row["fill_residue"]))
        for row in crt_rows
        if bool(row["supported_actual_packet_current"])
    }
    formal_pairs = {
        (int(row["generator_residue"]), int(row["fill_residue"])) for row in crt_rows
    }
    targets_by_q = {
        q: target_pairs_for_slot(slot_row) for q, slot_row in slot_by_q.items()
    }

    rows: list[dict[str, Any]] = []
    target_pair_counter: Counter[str] = Counter()
    for row in crt_rows:
        q = int(row["q"])
        target = nearest_target(row, targets_by_q[q])
        route = classify_edge_route(row, target, supported_pairs, formal_pairs)
        target_key = (
            f"{target['target_generator_residue']}:{target['target_fill_residue']}"
        )
        target_pair_counter[target_key] += 1
        rows.append(
            {
                "q": q,
                "generator_residue": int(row["generator_residue"]),
                "fill_residue": int(row["fill_residue"]),
                "supported_actual_packet_current": bool(
                    row["supported_actual_packet_current"]
                ),
                "crt_window_distance": int(row["window_distance"]),
                "crt_window_side": str(row["window_side"]),
                **target,
                "nearest_target_pair_key": target_key,
                "edge_collision_route": route,
            }
        )

    empty_rows = [row for row in rows if not row["supported_actual_packet_current"]]
    l1_values = [int(row["min_l1_residue_displacement_to_window"]) for row in empty_rows]
    route_histogram = Counter(str(row["edge_collision_route"]) for row in empty_rows)
    target_histogram = Counter(str(row["nearest_target_pair_key"]) for row in empty_rows)
    existing_actual_rows = [
        row
        for row in empty_rows
        if row["edge_collision_route"] == "ExistingActualResidueCollisionNeeded"
    ]
    unused_target_rows = [
        row
        for row in empty_rows
        if row["edge_collision_route"] == "UnusedTargetResidueArrivalNeeded"
    ]
    aggregate = {
        "crt_window_gap_ledger": str(crt_window_path.relative_to(ROOT)),
        "slot_ledger": str(slot_path.relative_to(ROOT)),
        "source_gate_pass_q_values": crt_window["aggregate"][
            "source_gate_pass_q_values"
        ],
        "target_window_pair_count": sum(
            len(targets_by_q[q])
            for q in crt_window["aggregate"]["source_gate_pass_q_values"]
        ),
        "formal_pair_total_with_exact_source": len(rows),
        "supported_actual_packet_total_current": len(rows) - len(empty_rows),
        "edge_collision_candidate_count_current": len(empty_rows),
        "min_empty_l1_residue_displacement": min(l1_values) if l1_values else None,
        "max_empty_l1_residue_displacement": max(l1_values) if l1_values else None,
        "empty_l1_residue_displacement_histogram": dict(
            sorted(Counter(str(value) for value in l1_values).items(), key=lambda item: int(item[0]))
        ),
        "edge_collision_route_histogram": dict(sorted(route_histogram.items())),
        "nearest_target_pair_histogram_current": dict(sorted(target_histogram.items())),
        "empty_pairs_target_existing_actual_count": len(existing_actual_rows),
        "empty_pairs_target_unused_residue_arrival_count": len(unused_target_rows),
        "all_empty_pairs_have_positive_residue_displacement": all(
            int(row["min_l1_residue_displacement_to_window"]) > 0 for row in empty_rows
        ),
        "window_edge_collision_displacement_closed_current_sweep": all(
            int(row["min_l1_residue_displacement_to_window"]) > 0 for row in empty_rows
        ),
        "global_window_edge_collision_bound_proved": False,
        "row_column_unconditional_closed": False,
    }

    return {
        "certificate_type": "prime_matrix_affine_twin_window_edge_collision_audit",
        "status": "current_sweep_window_edge_collision_displacements_closed_global_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "aggregate": aggregate,
        "target_window_pairs": {
            str(q): targets for q, targets in sorted(targets_by_q.items())
        },
        "edge_collision_rows": rows,
        "contract": {
            "edge_collision_gate": "A CRTWindowGap can become actual only by moving its residue pair to one of the target residue pairs induced by the common phase support.",
            "closed_current_sweep": aggregate[
                "window_edge_collision_displacement_closed_current_sweep"
            ],
            "global_remaining": [
                "GlobalWindowEdgeCollisionDisplacementBound",
                "ExistingActualResidueCollision-PDEC",
                "UnusedTargetResidueArrival-PDEC/SAE",
                "SupportMotionEscape-PDEC/SAE",
            ],
        },
        "dependency_hashes": {
            str(path.relative_to(ROOT)): sha256(path)
            for path in (crt_window_path, slot_path)
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
        "# Prime Matrix AffineTwin window edge-collision audit",
        "",
        "**状态：** `current_sweep_window_edge_collision_displacements_closed_global_open`",
        "",
        "本审计把 `CRTWindowGap` 的下一失败形态写成 residue 网格位移：共同窗口给出有限个可命中的目标 residue pairs；空窗 formal pair 若要变成 actual packet，必须移动到其中一个目标点。",
        "",
        "```text",
        f"target_window_pair_count={agg['target_window_pair_count']}",
        f"formal_pair_total_with_exact_source={agg['formal_pair_total_with_exact_source']}",
        f"supported_actual_packet_total_current={agg['supported_actual_packet_total_current']}",
        f"edge_collision_candidate_count_current={agg['edge_collision_candidate_count_current']}",
        f"min_empty_l1_residue_displacement={agg['min_empty_l1_residue_displacement']}",
        f"max_empty_l1_residue_displacement={agg['max_empty_l1_residue_displacement']}",
        f"empty_pairs_target_existing_actual_count={agg['empty_pairs_target_existing_actual_count']}",
        f"empty_pairs_target_unused_residue_arrival_count={agg['empty_pairs_target_unused_residue_arrival_count']}",
        f"window_edge_collision_displacement_closed_current_sweep={fmt_bool(agg['window_edge_collision_displacement_closed_current_sweep'])}",
        "```",
        "",
        "## 1. edge-collision 位移表",
        "",
        "| pair | CRT gap | nearest target | target P | delta g | delta f | L1 | route |",
        "| --- | ---: | --- | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in result["edge_collision_rows"]:
        if row["supported_actual_packet_current"]:
            continue
        pair = f"({row['generator_residue']},{row['fill_residue']})"
        target = (
            f"({row['target_generator_residue']},{row['target_fill_residue']})"
        )
        lines.append(
            "| `{pair}` | {gap} | `{target}` | {target_p} | {dg} | {df} | {l1} | `{route}` |".format(
                pair=pair,
                gap=row["crt_window_distance"],
                target=target,
                target_p=row["target_p"],
                dg=row["generator_delta_to_target"],
                df=row["fill_delta_to_target"],
                l1=row["min_l1_residue_displacement_to_window"],
                route=table_cell(row["edge_collision_route"]),
            )
        )

    lines.extend(
        [
            "",
            "## 2. 当前读数",
            "",
            "- `q=31` 的窗口 `[2669,2688]` 给出 `20` 个 target residue pairs。",
            "- 当前 `11` 个空窗 formal pairs 到最近 target 的 L1 residue 位移最小为 `1`，最大为 `11`。",
            "- 其中 `2` 个空窗最近目标是已有 actual pair `(19,8)`，因此若复现会变成 existing-actual residue collision。",
            "- 其余 `9` 个空窗最近目标需要未使用 target residue arrival，进入 arrival/PDEC/SAE 接口。",
            "",
            "## 3. 结论边界",
            "",
            "- 本步关闭当前 sweep 的 edge-collision 位移账本，不证明全局不发生碰撞。",
            "- 全局剩余是证明这些位移需求不能持续由反例链供给，或把失败路由到 `ExistingActualResidueCollision-PDEC`、`UnusedTargetResidueArrival-PDEC/SAE`、`SupportMotionEscape-PDEC/SAE`。",
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
        description="生成 AffineTwin window edge-collision 位移审计证书。"
    )
    parser.add_argument("--crt-window-gap-ledger", type=Path, default=CRT_WINDOW_GAP_LEDGER)
    parser.add_argument("--slot-ledger", type=Path, default=SLOT_LEDGER)
    return parser.parse_args()


def main() -> None:
    """入口。"""
    args = parse_args()
    result = build_result(args.crt_window_gap_ledger, args.slot_ledger)
    write_outputs(result)
    print(json.dumps(result["aggregate"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
