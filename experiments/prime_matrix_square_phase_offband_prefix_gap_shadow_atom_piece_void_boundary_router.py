#!/usr/bin/env python3
"""登记 selected small-k atom-piece void 的严格边界。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_atom_piece_void_boundary_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-atom-piece-void-boundary-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-atom-piece-void-boundary-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-atom-piece-void-boundary-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-atom-piece-void-boundary-router.md
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

INPUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-segment-normal-form-ledger.json"
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-atom-piece-void-boundary-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-atom-piece-void-boundary-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-atom-piece-void-boundary-router.md"

SEGMENT_NORMAL_FORM_ROUTER = (
    ROOT / "experiments" / "prime_matrix_square_phase_offband_prefix_gap_shadow_segment_normal_form_router.py"
)

MAIN_TARGET = "SelectedSmallKAtomPiecePrimeSupplyOrAtomPieceVoidPDEC"
NEXT_TARGET = "CounterexampleConditionalSmallKAtomPieceVoidContradictionOrColumnPhasePDEC"


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


def is_composite(value: int) -> bool:
    """小整数素性反查，用于裸短区间反例证书。"""
    if value < 2:
        return False
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            return True
        divisor += 1
    return False


def interval_candidate_count(q_lo: int, q_hi: int) -> int:
    """计算奇数候选个数。"""
    return (q_hi - q_lo) // 2 + 1


def naked_gap_counterexamples() -> list[dict[str, Any]]:
    """给出长度 2..5 的裸 atom-piece 素数供给反例。

    这些反例只用于排除错误路线：不能把 selected atom-piece 供给理解成
    任意短奇数段必含素数。真正可攻对象必须带上完整反例链约束。
    """
    examples = [
        (2, 119, 121),
        (3, 119, 123),
        (4, 115, 121),
        (5, 115, 123),
    ]
    rows = []
    for candidate_count, q_lo, q_hi in examples:
        values = list(range(q_lo, q_hi + 1, 2))
        rows.append(
            {
                "candidate_count": candidate_count,
                "q_lo": q_lo,
                "q_hi": q_hi,
                "odd_values": values,
                "all_composite": all(is_composite(value) for value in values),
                "meaning": "This rules out a naked bounded-gap interpretation of the selected atom-piece supply claim.",
            }
        )
    return rows


def boundary_record(row: dict[str, Any]) -> dict[str, Any]:
    """把 selected atom piece 压成条件化 void 原子。"""
    q_lo = int(row["selected_atom_piece_q_lo"])
    q_hi = int(row["selected_atom_piece_q_hi"])
    candidate_count = int(row["selected_atom_piece_candidate_count"])
    p_value = int(row["p"])
    return {
        "p": p_value,
        "side": row["side"],
        "shape_key": row["shape_key"],
        "q_lo": q_lo,
        "q_hi": q_hi,
        "candidate_count": candidate_count,
        "b_lo": row["b_lo"],
        "b_hi": row["b_hi"],
        "b_length": row["b_length"],
        "depth_from_p": row["depth_from_p"],
        "parent_atom_key": row["parent_atom_key"],
        "parent_atom_band": row["parent_atom_band"],
        "parent_atom_k": row["parent_atom_k"],
        "actual_target_prime_values": row["selected_atom_piece_target_prime_values"],
        "actual_target_prime_count": row["selected_atom_piece_target_prime_count"],
        "actual_atom_piece_void": row["selected_atom_piece_target_prime_count"] == 0,
        "void_packet_statement": (
            f"Under the full counterexample chain, every odd q in [{q_lo},{q_hi}] "
            f"with q=P-2b and {row['b_lo']}<=b<={row['b_hi']} is forced composite."
        ),
        "conditional_constraints_needed": [
            "target-union void inherited from the original off-band prefix failure",
            "wheel-17 support collapse or its downstream gap-cell/target-segment form",
            "fixed small-k atom phase q=P-2b with parent band and side preserved",
            "column phase / square-anchor CRT compatibility of the same q-candidates",
        ],
        "valid_next_attack": (
            "Exclude this atom-piece void only after the full counterexample-chain "
            "constraints are present; do not use a naked bounded prime-gap assertion."
        ),
    }


def family_key(row: dict[str, Any]) -> str:
    """生成 shape family 键。"""
    return (
        f"side={row['side']}|band={row['parent_atom_band']}|k={row['parent_atom_k']}|"
        f"cand={row['candidate_count']}|b_len={row['b_length']}"
    )


def build_family_histogram(records: list[dict[str, Any]]) -> dict[str, int]:
    """统计 atom-piece shape families。"""
    histogram: dict[str, int] = {}
    for row in records:
        key = family_key(row)
        histogram[key] = histogram.get(key, 0) + 1
    return dict(sorted(histogram.items()))


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "atom_piece_void_boundary_registered",
            "status": "closed",
            "statement": "The newest hardpoint is exactly the exclusion of selected small-k atom-piece void under the full counterexample chain.",
        },
        {
            "name": "naked_bounded_gap_route_rejected",
            "status": "closed",
            "statement": "The claim cannot be replaced by a standalone theorem that every odd segment of length 2..5 contains a prime.",
        },
        {
            "name": "finite_atom_piece_frontier_nonvoid",
            "status": "finite_evidence",
            "statement": "The finite frontier has no actual selected atom-piece void, but this empirical fact is not used as a proof.",
        },
        {
            "name": "counterexample_conditional_void_contradiction",
            "status": "open",
            "statement": "A self-contained proof still needs to derive a contradiction between atom-piece void and the preserved counterexample-chain structure.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "BoundaryRegistrationClosed",
            "closed": True,
            "proved": True,
            "meaning": "最新 hardpoint 已登记为 selected small-k atom-piece void 的条件化排斥问题。",
            "remaining": "closed",
        },
        {
            "gate": "NakedBoundedGapInterpretationRejected",
            "closed": True,
            "proved": True,
            "meaning": "短 atom-piece 供给不能按裸短区间素数定理使用；长度 2..5 均有合数段反例。",
            "remaining": "closed",
        },
        {
            "gate": "FiniteNoSelectedAtomPieceVoid",
            "closed": result["actual_selected_atom_piece_void_count"] == 0,
            "proved": False,
            "meaning": "有限账本中每个 selected atom piece 实际含素数；这仍只是有限证据。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "CounterexampleConditionalVoidContradictionClosed",
            "closed": False,
            "proved": False,
            "meaning": "仍需把 atom-piece void 接入列相位、平方锚和支撑塌缩链，推出真正矛盾。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步关闭错误出口并固定下一原子目标，不关闭行/列无条件命题。",
            "remaining": NEXT_TARGET,
        },
    ]


def build_result(input_ledger: Path) -> dict[str, Any]:
    """构造 atom-piece void boundary 路由结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    source = load_json(input_ledger)
    records = [boundary_record(row) for row in source["normal_form_records"]]
    counterexamples = naked_gap_counterexamples()
    actual_void = [row for row in records if row["actual_atom_piece_void"]]
    family_histogram = build_family_histogram(records)
    aggregate = {
        "input_ledger": str(input_ledger.relative_to(ROOT)),
        "record_count": len(records),
        "actual_selected_atom_piece_void_count": len(actual_void),
        "min_candidate_count": min((row["candidate_count"] for row in records), default=0),
        "max_candidate_count": max((row["candidate_count"] for row in records), default=0),
        "min_b_length": min((row["b_length"] for row in records), default=0),
        "max_b_length": max((row["b_length"] for row in records), default=0),
        "max_parent_atom_k": max((row["parent_atom_k"] for row in records), default=0),
        "max_depth_from_p": max((row["depth_from_p"] for row in records), default=0),
        "shape_family_count": len(family_histogram),
        "shape_family_histogram": family_histogram,
        "naked_gap_counterexamples_all_valid": all(row["all_composite"] for row in counterexamples),
    }
    ledger = {
        "parameters": source["parameters"],
        "aggregate": aggregate,
        "boundary_records": records,
        "actual_selected_atom_piece_void_records": actual_void,
        "naked_gap_counterexamples": counterexamples,
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = {
        "certificate_type": "prime_matrix_square_phase_offband_prefix_gap_shadow_atom_piece_void_boundary_router",
        "status": "atom_piece_void_boundary_registered_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "empirical_absence_not_used_as_proof": True,
        "standalone_bounded_gap_route_valid": False,
        "parameters": source["parameters"],
        "aggregate": aggregate,
        "boundary_records": records,
        "actual_selected_atom_piece_void_count": len(actual_void),
        "naked_gap_counterexamples": counterexamples,
        "counterexample_conditional_atom_piece_void_excluded": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_atom_piece_void_boundary_router.py": sha256(
                Path(__file__).resolve()
            ),
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_segment_normal_form_router.py": sha256(
                SEGMENT_NORMAL_FORM_ROUTER
            ),
            "data/square-phase-offband-prefix-gap-shadow-segment-normal-form-ledger.json": sha256(input_ledger),
            "data/square-phase-offband-prefix-gap-shadow-atom-piece-void-boundary-ledger.json": sha256(OUT_LEDGER),
        },
        "plain_conclusion": (
            "本步把 selected small-k atom-piece 的最后边界固定下来：有限前沿中 11 个 selected atom piece "
            "全部实际非空，长度为 2..5，父 atom 最大 k=2；但裸短区间素数供给命题全局为假。"
            "因此自足闭合不能依赖“短段必有素数”，只能继续证明完整反例链约束下的 atom-piece void "
            "与列相位/平方锚/CRT 支撑塌缩结构矛盾。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow atom-piece void boundary router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"record_count={agg['record_count']}",
        f"actual_selected_atom_piece_void_count={agg['actual_selected_atom_piece_void_count']}",
        f"candidate_count_range={agg['min_candidate_count']}..{agg['max_candidate_count']}",
        f"b_length_range={agg['min_b_length']}..{agg['max_b_length']}",
        f"max_parent_atom_k={agg['max_parent_atom_k']}",
        f"max_depth_from_p={agg['max_depth_from_p']}",
        f"shape_family_count={agg['shape_family_count']}",
        f"standalone_bounded_gap_route_valid={fmt_bool(result['standalone_bounded_gap_route_valid'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 精确边界",
        "",
        "当前剩余不能写成裸命题“每个长度 2..5 的奇数段都含素数”。正确边界是：",
        "",
        "```text",
        "在完整反例链已经强制 target-union void、wheel/support-collapse、gap-cell/target-segment 选择、",
        "以及固定 small-k 相位 q=P-2b 的同一条件下，排斥 selected atom-piece void。",
        "```",
        "",
        "## 2. Selected atom-piece 前沿",
        "",
        "| P | side | q atom piece | b interval | parent atom | actual primes | void? |",
        "| ---: | --- | --- | --- | --- | --- | ---: |",
    ]
    for row in result["boundary_records"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["p"]),
                    f"`{row['side']}`",
                    f"`{row['q_lo']}-{row['q_hi']}`",
                    f"`{row['b_lo']}-{row['b_hi']}`",
                    f"`{row['parent_atom_key']}`",
                    f"`{row['actual_target_prime_values']}`",
                    f"`{fmt_bool(row['actual_atom_piece_void'])}`",
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 3. 裸短区间路线反例",
            "",
            "| candidate_count | q segment | odd values | all composite |",
            "| ---: | --- | --- | ---: |",
        ]
    )
    for row in result["naked_gap_counterexamples"]:
        lines.append(
            f"| `{row['candidate_count']}` | `{row['q_lo']}-{row['q_hi']}` | "
            f"`{row['odd_values']}` | `{fmt_bool(row['all_composite'])}` |"
        )
    lines.extend(
        [
            "",
            "这些小反例只说明裸 bounded-gap 路线无效；它们不否定带完整反例链约束的条件化矛盾路线。",
            "",
            "## 4. Shape families",
            "",
            "| family | count |",
            "| --- | ---: |",
        ]
    )
    for key, count in agg["shape_family_histogram"].items():
        lines.append(f"| `{table_cell(key)}` | `{count}` |")
    lines.extend(
        [
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
            "- 从完整反例链出发，把 selected atom-piece void 与列相位、平方锚、CRT 支撑塌缩同时放入同一矛盾场。",
            "- 当前仍未证明全局行/列无条件闭合。",
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
    parser.add_argument("--input-ledger", type=Path, default=INPUT_LEDGER)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    input_ledger = args.input_ledger if args.input_ledger.is_absolute() else ROOT / args.input_ledger
    result = build_result(input_ledger)
    write_markdown(result)
    result["source_hashes"][
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-atom-piece-void-boundary-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "actual_selected_atom_piece_void_count": result["actual_selected_atom_piece_void_count"],
                "standalone_bounded_gap_route_valid": result["standalone_bounded_gap_route_valid"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
