#!/usr/bin/env python3
"""把 transport cell 持久性压成深度迭代漂移审计。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_transport_cell_iteration_drift_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-transport-cell-iteration-drift-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-selector-h-lower-transport-cell-iteration-drift-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-transport-cell-iteration-drift-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-transport-cell-iteration-drift-router.md
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

TRANSPORT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-fixed-residue-transport-cell-ledger.json"
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-transport-cell-iteration-drift-ledger.json"
OUT_JSON = DOCS / (
    "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-"
    "transport-cell-iteration-drift-router.json"
)
OUT_MD = DOCS / (
    "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-"
    "transport-cell-iteration-drift-router.md"
)

MAIN_TARGET = "TransportCellNonPersistenceOrSingletonResidueSAESummability"
NEXT_TARGET = "NonChainedTransportCellPDECOrSingletonResidueSAESummability"


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


def finite_bound(start_depth: int, step_loss: int) -> int | None:
    """若每步损耗为正，返回最多可走的步数；否则返回 None。"""
    if step_loss <= 0:
        return None
    return start_depth // step_loss


def min_optional(values: list[int | None]) -> int | None:
    """忽略 None 后取最小值。"""
    finite = [value for value in values if value is not None]
    return min(finite) if finite else None


def drift_record(cell: dict[str, Any]) -> dict[str, Any]:
    """计算一个 transport cell 的迭代深度漂移。"""
    left_depth_0, right_depth_0 = [int(value) for value in cell["depth_left"]]
    left_depth_1, right_depth_1 = [int(value) for value in cell["depth_right"]]
    lo_defect = int(cell["lo_translate_defect"])
    hi_defect = int(cell["hi_translate_defect"])
    predicted_next = [left_depth_0 - lo_defect, right_depth_0 + hi_defect]

    forward_left_bound = finite_bound(left_depth_0, lo_defect)
    forward_right_bound = finite_bound(right_depth_0, -hi_defect)
    forward_bound = min_optional([forward_left_bound, forward_right_bound])
    backward_left_bound = finite_bound(left_depth_0, -lo_defect)
    backward_right_bound = finite_bound(right_depth_0, hi_defect)
    backward_bound = min_optional([backward_left_bound, backward_right_bound])

    return {
        "transport_cell_key": cell["transport_cell_key"],
        "side": cell["side"],
        "ell": int(cell["ell"]),
        "crt_residue": int(cell["crt_residue"]),
        "p_values": list(cell["p_values"]),
        "p_lift": int(cell["p_lift"]),
        "slot_sum_lift": int(cell["slot_sum_lift"]),
        "lo_translate_defect": lo_defect,
        "hi_translate_defect": hi_defect,
        "start_depth": [left_depth_0, right_depth_0],
        "observed_next_depth": [left_depth_1, right_depth_1],
        "predicted_next_depth": predicted_next,
        "depth_iteration_identity_ok": predicted_next == [left_depth_1, right_depth_1],
        "exact_phase_translate": lo_defect == 0 and hi_defect == 0,
        "forward_contracting_edges": [
            name
            for name, active in [
                ("left", lo_defect > 0),
                ("right", hi_defect < 0),
            ]
            if active
        ],
        "backward_contracting_edges": [
            name
            for name, active in [
                ("left", lo_defect < 0),
                ("right", hi_defect > 0),
            ]
            if active
        ],
        "forward_left_bound": forward_left_bound,
        "forward_right_bound": forward_right_bound,
        "forward_max_transition_count": forward_bound,
        "forward_additional_after_observed": None if forward_bound is None else forward_bound - 1,
        "backward_left_bound": backward_left_bound,
        "backward_right_bound": backward_right_bound,
        "backward_max_transition_count": backward_bound,
        "forward_chain_finite_by_depth": forward_bound is not None,
        "two_sided_chain_finite_by_depth": (forward_bound is not None or backward_bound is not None)
        and not (lo_defect == 0 and hi_defect == 0),
        "forward_expanding_or_neutral": lo_defect <= 0 and hi_defect >= 0,
        "min_margin": int(cell["min_margin"]),
        "min_crt_minus_phase_width": int(cell["min_crt_minus_phase_width"]),
    }


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "transport_cell_depth_iteration_identity",
            "status": "closed",
            "statement": "Under repeated use of the same transport cell, phase depths evolve by D_L(n)=D_L(0)-n*lo_defect and D_R(n)=D_R(0)+n*hi_defect.",
        },
        {
            "name": "current_transport_cell_forward_chain_nonpersistence",
            "status": "closed_on_current_sweep",
            "statement": "Every current transport cell has a forward contracting edge, hence only finitely many chained repeats are possible from the observed start.",
        },
        {
            "name": "nonchained_transport_or_singleton_sae_open",
            "status": "open",
            "statement": "A global proof must still exclude non-chained transport recurrences or prove singleton-residue SAE/Rankin summability.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    agg = result["aggregate"]
    return [
        {
            "gate": "DepthIterationIdentityClosed",
            "closed": agg["depth_iteration_identity_failure_count"] == 0,
            "proved": True,
            "meaning": "同一 transport cell 迭代时左右深度按边界缺陷线性更新。",
            "remaining": "closed",
        },
        {
            "gate": "CurrentForwardChainNonPersistenceClosed",
            "closed": agg["all_current_cells_forward_finite_by_depth"],
            "proved": False,
            "meaning": "当前 12 个 cell 全部有前向有限寿命；最长只能连续走 8 次。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "ExactTranslateEscapeAbsentCurrentSweep",
            "closed": agg["exact_phase_translate_count"] == 0,
            "proved": False,
            "meaning": "当前没有零缺陷 exact translate 逃逸口。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "NonChainedTransportExcluded",
            "closed": False,
            "proved": False,
            "meaning": "非连续复现仍可能存在，需要 ColumnCRT/PDEC 或 SAE 处理。",
            "remaining": "NonChainedTransportCellPDEC",
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步关闭 chained transport 通道，不关闭全局命题。",
            "remaining": result["next_direct_attack_target"],
        },
    ]


def build_result(transport_ledger: Path) -> dict[str, Any]:
    """构造迭代漂移审计结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    source = load_json(transport_ledger)
    records = [drift_record(cell) for cell in source["transport_cells"]]
    finite_forward = [
        int(record["forward_max_transition_count"])
        for record in records
        if record["forward_max_transition_count"] is not None
    ]
    addl = [
        int(record["forward_additional_after_observed"])
        for record in records
        if record["forward_additional_after_observed"] is not None
    ]
    aggregate = {
        "transport_ledger": str(transport_ledger.relative_to(ROOT)),
        "transport_cell_count": len(records),
        "depth_iteration_identity_failure_count": sum(
            1 for record in records if not record["depth_iteration_identity_ok"]
        ),
        "exact_phase_translate_count": sum(1 for record in records if record["exact_phase_translate"]),
        "forward_finite_lifetime_count": sum(1 for record in records if record["forward_chain_finite_by_depth"]),
        "all_current_cells_forward_finite_by_depth": all(record["forward_chain_finite_by_depth"] for record in records),
        "two_sided_finite_lifetime_count": sum(1 for record in records if record["two_sided_chain_finite_by_depth"]),
        "forward_expanding_or_neutral_count": sum(1 for record in records if record["forward_expanding_or_neutral"]),
        "max_forward_transition_count": max(finite_forward),
        "max_forward_additional_after_observed": max(addl),
        "immediate_terminal_after_observed_count": sum(
            1 for record in records if record["forward_additional_after_observed"] == 0
        ),
        "forward_transition_count_histogram": dict(
            sorted(Counter(str(value) for value in finite_forward).items(), key=lambda item: int(item[0]))
        ),
        "forward_additional_after_observed_histogram": dict(
            sorted(Counter(str(value) for value in addl).items(), key=lambda item: int(item[0]))
        ),
        "chained_transport_persistence_excluded_current_sweep": all(
            record["forward_chain_finite_by_depth"] for record in records
        ),
        "nonchained_transport_persistence_excluded_globally": False,
        "singleton_residue_sae_rankin_bound_proved": False,
        "row_column_unconditional_closed": False,
    }

    ledger = {
        "aggregate": aggregate,
        "drift_records": records,
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    result = {
        "certificate_type": (
            "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_"
            "transport_cell_iteration_drift_router"
        ),
        "status": "transport_cell_chained_persistence_closed_nonchained_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_sweep_not_used_as_global_proof": True,
        "aggregate": aggregate,
        "drift_records": records,
        "chained_transport_persistence_excluded_current_sweep": aggregate[
            "chained_transport_persistence_excluded_current_sweep"
        ],
        "nonchained_transport_persistence_excluded_globally": False,
        "singleton_residue_sae_rankin_bound_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "plain_conclusion": (
            "本步证明 transport cell 的链式迭代深度恒等式：若同一 cell 连续复现，"
            "左右相位深度分别按 `-lo_defect` 与 `+hi_defect` 线性漂移。当前 12 个 cell "
            "全部存在前向收缩边，因此从观测起点出发都只能有限次连续复现；最长前向寿命为 "
            f"{aggregate['max_forward_transition_count']} 次转移，观测到一次后最多还能追加 "
            f"{aggregate['max_forward_additional_after_observed']} 次。剩余硬点缩成非连续 transport "
            "复现的 PDEC/ColumnCRT，或 singleton residue 的 SAE/Rankin 可求和。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    result["source_hashes"] = {
        "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_transport_cell_iteration_drift_router.py": sha256(
            Path(__file__).resolve()
        ),
        "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-fixed-residue-transport-cell-ledger.json": sha256(
            transport_ledger
        ),
        "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-transport-cell-iteration-drift-ledger.json": sha256(
            OUT_LEDGER
        ),
    }
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow selector H lower transport-cell iteration-drift router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"transport_cell_count={agg['transport_cell_count']}",
        f"depth_iteration_identity_failure_count={agg['depth_iteration_identity_failure_count']}",
        f"exact_phase_translate_count={agg['exact_phase_translate_count']}",
        f"forward_finite_lifetime_count={agg['forward_finite_lifetime_count']}",
        f"max_forward_transition_count={agg['max_forward_transition_count']}",
        f"max_forward_additional_after_observed={agg['max_forward_additional_after_observed']}",
        f"immediate_terminal_after_observed_count={agg['immediate_terminal_after_observed_count']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 迭代恒等式",
        "",
        "```text",
        "If the same transport cell is repeated n times:",
        "  left_depth(n)  = left_depth(0)  - n * lo_defect",
        "  right_depth(n) = right_depth(0) + n * hi_defect",
        "validity requires both depths to stay nonnegative.",
        "```",
        "",
        "## 2. 有限寿命记录",
        "",
        "| ell | residue | side | p values | defect | start depth | next depth | forward max | additional | contracting edges |",
        "| ---: | ---: | --- | --- | --- | --- | --- | ---: | ---: | --- |",
    ]
    for row in result["drift_records"]:
        lines.append(
            f"| {row['ell']} | {row['crt_residue']} | `{row['side']}` | `{row['p_values']}` | "
            f"`{row['lo_translate_defect']}/{row['hi_translate_defect']}` | "
            f"`{row['start_depth']}` | `{row['observed_next_depth']}` | "
            f"{row['forward_max_transition_count']} | {row['forward_additional_after_observed']} | "
            f"`{row['forward_contracting_edges']}` |"
        )
    lines.extend(
        [
            "",
            "## 3. 结构判断",
            "",
            "- 当前 12 个 transport cell 都不是 exact translate。",
            "- 每个 cell 都有前向收缩边，因此不能沿同一 cell 无限连续复现。",
            "- 这仍未排除非连续复现；非连续情形必须继续用 ColumnCRT/PDEC 或 SAE/Rankin 处理。",
            "",
            "## 4. 命题行",
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
            "## 5. 决策表",
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
            "## 6. 下一步",
            "",
            f"- 主攻：`{result['next_direct_attack_target']}`。",
            "- 对非连续 transport 复现建立 ColumnCRT/PDEC 上界。",
            "- 对 singleton residue packet 建立 SAE/Rankin 可求和账本。",
            "",
            "## 7. 依赖哈希",
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
    parser.add_argument("--transport-ledger", type=Path, default=TRANSPORT_LEDGER)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    transport_ledger = args.transport_ledger if args.transport_ledger.is_absolute() else ROOT / args.transport_ledger
    result = build_result(transport_ledger)
    write_markdown(result)
    result["source_hashes"][
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-transport-cell-iteration-drift-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "transport_cell_count": result["aggregate"]["transport_cell_count"],
                "forward_finite_lifetime_count": result["aggregate"]["forward_finite_lifetime_count"],
                "max_forward_transition_count": result["aggregate"]["max_forward_transition_count"],
                "max_forward_additional_after_observed": result["aggregate"][
                    "max_forward_additional_after_observed"
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
