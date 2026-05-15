#!/usr/bin/env python3
"""把 target-overlap cell 压成单个 target atom segment 供给。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_target_segment_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-target-segment-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-target-segment-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-target-segment-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-target-segment-router.md
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

INPUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-escape-cell-selector-ledger.json"
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-target-segment-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-target-segment-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-target-segment-router.md"

ESCAPE_SELECTOR_ROUTER = (
    ROOT / "experiments" / "prime_matrix_square_phase_offband_prefix_gap_shadow_escape_cell_selector_router.py"
)

MAIN_TARGET = "TargetOverlapGapCellPrimeSupplyOrTargetCellVoidPDEC"
NEXT_TARGET = "SelectedTargetAtomSegmentPrimeSupplyOrSegmentVoidPDEC"


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


def odd_values(q_lo: int, q_hi: int) -> list[int]:
    """列出奇候选 q。"""
    return list(range(q_lo, q_hi + 1, 2))


def segment_record(cell: dict[str, Any], interval: dict[str, Any]) -> dict[str, Any] | None:
    """计算 selected cell 与一个 target interval 的交段。"""
    q_lo = max(int(cell["q_lo"]), int(interval["q_lo"]))
    q_hi = min(int(cell["q_hi"]), int(interval["q_hi"]))
    if q_hi < q_lo:
        return None
    q_values = odd_values(q_lo, q_hi)
    prime_values = [value for value in cell["target_prime_values"] if q_lo <= value <= q_hi]
    return {
        "q_lo": q_lo,
        "q_hi": q_hi,
        "candidate_count": len(q_values),
        "q_values": q_values,
        "parent_target_interval": interval,
        "target_prime_values": prime_values,
        "target_prime_count": len(prime_values),
        "actual_segment_void": len(prime_values) == 0,
    }


def packet_segment(row: dict[str, Any]) -> dict[str, Any]:
    """选择最小的非空 target segment。"""
    cell = row["selected_target_escape_cell"]
    segments = [
        segment
        for interval in row["target_union_intervals"]
        if (segment := segment_record(cell, interval)) is not None
    ]
    nonvoid_segments = [segment for segment in segments if not segment["actual_segment_void"]]
    selected = None
    if nonvoid_segments:
        selected = min(nonvoid_segments, key=lambda segment: (segment["candidate_count"], segment["q_lo"]))
    return {
        "p": row["p"],
        "side": row["side"],
        "shape_key": row["shape_key"],
        "q_hull_lo": row["q_hull_lo"],
        "q_hull_hi": row["q_hull_hi"],
        "wheel17_survivor_values": row["wheel17_survivor_values"],
        "selected_cell": cell,
        "target_segments_inside_cell": segments,
        "nonvoid_target_segment_count": len(nonvoid_segments),
        "selected_target_segment": selected,
        "target_segment_selector_succeeds_in_finite_audit": selected is not None,
    }


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "target_cell_to_target_segments",
            "status": "closed",
            "statement": "The selected target-overlap cell splits into intersections with explicit target-union intervals.",
        },
        {
            "name": "single_target_segment_prime_supply_excludes_union_void",
            "status": "closed",
            "statement": "If one selected target segment contains a prime, the target-union void assumption is contradicted.",
        },
        {
            "name": "finite_target_segment_selector",
            "status": "finite_evidence",
            "statement": "Every finite packet has a selected non-void target segment of length at most five odd candidates.",
        },
        {
            "name": "global_selected_target_segment_prime_supply",
            "status": "open",
            "statement": "A global proof still needs a prime in the selected target atom segment, or exclusion of segment-void PDEC.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "TargetSegmentReductionClosed",
            "closed": True,
            "proved": True,
            "meaning": "target-overlap cell 已压到显式 target interval 交段。",
            "remaining": "closed",
        },
        {
            "gate": "SingleTargetSegmentCriterionClosed",
            "closed": True,
            "proved": True,
            "meaning": "单个 target segment 含素数即可否定 union void。",
            "remaining": "closed",
        },
        {
            "gate": "FiniteTargetSegmentSelectorSucceeds",
            "closed": result["selector_failure_count"] == 0,
            "proved": False,
            "meaning": "有限前沿每个包都有非空 target segment。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "GlobalSelectedTargetSegmentSupplyClosed",
            "closed": False,
            "proved": False,
            "meaning": "仍需全局证明选中 segment 含素数，或排斥 segment-void PDEC。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只完成 target segment 压缩，不关闭全局行/列命题。",
            "remaining": NEXT_TARGET,
        },
    ]


def build_result(input_ledger: Path) -> dict[str, Any]:
    """构造 target-segment 路由结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    source = load_json(input_ledger)
    records = [packet_segment(row) for row in source["selector_records"]]
    selected = [row["selected_target_segment"] for row in records if row["selected_target_segment"]]
    failures = [row for row in records if not row["target_segment_selector_succeeds_in_finite_audit"]]
    aggregate = {
        "input_ledger": str(input_ledger.relative_to(ROOT)),
        "packet_count": len(records),
        "selector_success_count": len(records) - len(failures),
        "selector_failure_count": len(failures),
        "min_selected_segment_candidate_count": min((seg["candidate_count"] for seg in selected), default=0),
        "max_selected_segment_candidate_count": max((seg["candidate_count"] for seg in selected), default=0),
        "min_selected_segment_target_prime_count": min((seg["target_prime_count"] for seg in selected), default=0),
        "max_selected_segment_target_prime_count": max((seg["target_prime_count"] for seg in selected), default=0),
        "max_segments_inside_selected_cell": max(
            (len(row["target_segments_inside_cell"]) for row in records),
            default=0,
        ),
    }
    ledger = {
        "parameters": source["parameters"],
        "aggregate": aggregate,
        "target_segment_records": records,
        "selector_failures": failures,
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = {
        "certificate_type": "prime_matrix_square_phase_offband_prefix_gap_shadow_target_segment_router",
        "status": "target_overlap_cell_reduced_to_selected_target_segment_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "empirical_absence_not_used_as_proof": True,
        "parameters": source["parameters"],
        "aggregate": aggregate,
        "target_segment_records": records,
        "selector_failure_count": len(failures),
        "global_selected_target_segment_prime_supply_proved": False,
        "segment_void_pdec_excluded": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_target_segment_router.py": sha256(
                Path(__file__).resolve()
            ),
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_escape_cell_selector_router.py": sha256(
                ESCAPE_SELECTOR_ROUTER
            ),
            "data/square-phase-offband-prefix-gap-shadow-escape-cell-selector-ledger.json": sha256(input_ledger),
            "data/square-phase-offband-prefix-gap-shadow-target-segment-ledger.json": sha256(OUT_LEDGER),
        },
        "plain_conclusion": (
            "本步把 target-overlap cell 继续压成单个 target atom segment：选中 cell 与目标 union 区间取交，"
            "再选出最短的实际非空 target segment。有限前沿 11 个包全部成功，选中 segment 长度为 2..5 个奇候选；"
            "全局仍需证明这些显式 target segment 含素数，或排斥 segment-void PDEC。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow target segment router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"packet_count={agg['packet_count']}",
        f"selector_success_count={agg['selector_success_count']}",
        f"selector_failure_count={agg['selector_failure_count']}",
        f"selected_segment_candidate_count_range={agg['min_selected_segment_candidate_count']}..{agg['max_selected_segment_candidate_count']}",
        f"selected_segment_target_prime_count_range={agg['min_selected_segment_target_prime_count']}..{agg['max_selected_segment_target_prime_count']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. target segment 选择",
        "",
        "把 selected cell 与每个 target union interval 取交；若某个交段含素数，则 target-union void 直接失败。有限前沿选择最短的非空 target segment。",
        "",
        "## 2. 选择前沿",
        "",
        "| P | side | selected segment | candidates | target primes | parent interval |",
        "| ---: | --- | --- | ---: | --- | --- |",
    ]
    for row in result["target_segment_records"]:
        segment = row["selected_target_segment"]
        if segment is None:
            segment_text = "none"
            candidates = 0
            primes: list[int] = []
            parent = "none"
        else:
            segment_text = f"{segment['q_lo']}-{segment['q_hi']}"
            candidates = segment["candidate_count"]
            primes = segment["target_prime_values"]
            parent = f"{segment['parent_target_interval']['q_lo']}-{segment['parent_target_interval']['q_hi']}"
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["p"]),
                    f"`{row['side']}`",
                    f"`{segment_text}`",
                    str(candidates),
                    f"`{primes}`",
                    f"`{parent}`",
                ]
            )
            + " |"
        )
    lines.extend(
        [
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
            "- 对长度 2..5 的 selected target segments 建立统一素数供给，或证明其同时为空会触发列相位/平方锚矛盾。",
            "- 当前仍未证明全局行/列无条件闭合。",
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
    parser.add_argument("--input-ledger", type=Path, default=INPUT_LEDGER)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    input_ledger = args.input_ledger if args.input_ledger.is_absolute() else ROOT / args.input_ledger
    result = build_result(input_ledger)
    write_markdown(result)
    result["source_hashes"][
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-target-segment-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "selector_failure_count": result["selector_failure_count"],
                "min_selected_segment_candidate_count": result["aggregate"][
                    "min_selected_segment_candidate_count"
                ],
                "max_selected_segment_candidate_count": result["aggregate"][
                    "max_selected_segment_candidate_count"
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
