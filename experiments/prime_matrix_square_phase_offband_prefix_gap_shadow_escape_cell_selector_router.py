#!/usr/bin/env python3
"""从 gap-cell PDEC 中选择 target-overlap escape cell。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_escape_cell_selector_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-escape-cell-selector-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-escape-cell-selector-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-escape-cell-selector-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-escape-cell-selector-router.md
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

INPUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-gap-cell-ledger.json"
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-escape-cell-selector-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-escape-cell-selector-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-escape-cell-selector-router.md"

GAP_CELL_ROUTER = ROOT / "experiments" / "prime_matrix_square_phase_offband_prefix_gap_shadow_gap_cell_router.py"

MAIN_TARGET = "SingleGapCellPrimeSupplyOrSimultaneousGapCellVoidPDEC"
NEXT_TARGET = "TargetOverlapGapCellPrimeSupplyOrTargetCellVoidPDEC"


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


def in_intervals(value: int, intervals: list[dict[str, Any]]) -> bool:
    """判断 value 是否落入目标 union 区间。"""
    return any(int(item["q_lo"]) <= value <= int(item["q_hi"]) for item in intervals)


def enrich_cell(packet: dict[str, Any], cell: dict[str, Any]) -> dict[str, Any]:
    """补充 cell 的 target/complement 素数分解。"""
    intervals = packet["target_union_intervals"]
    q_values = odd_values(int(cell["q_lo"]), int(cell["q_hi"]))
    target_values = [value for value in q_values if in_intervals(value, intervals)]
    complement_values = [value for value in q_values if value not in target_values]
    prime_values = list(cell["prime_values"])
    target_prime_values = [value for value in prime_values if value in target_values]
    complement_prime_values = [value for value in prime_values if value in complement_values]
    return {
        **cell,
        "target_values": target_values,
        "complement_values": complement_values,
        "target_prime_values": target_prime_values,
        "complement_prime_values": complement_prime_values,
        "target_prime_count": len(target_prime_values),
        "complement_prime_count": len(complement_prime_values),
        "target_overlap": bool(target_values),
        "has_target_prime": bool(target_prime_values),
    }


def packet_selector(packet: dict[str, Any]) -> dict[str, Any]:
    """给一个 packet 选择最小 target-overlap escape cell。"""
    cells = [enrich_cell(packet, cell) for cell in packet["gap_cells"]]
    target_overlap_cells = [cell for cell in cells if cell["target_overlap"]]
    target_nonvoid_cells = [cell for cell in target_overlap_cells if cell["has_target_prime"]]
    pure_complement_nonvoid_cells = [
        cell for cell in cells if not cell["target_overlap"] and int(cell["prime_count"]) > 0
    ]
    selected = None
    if target_nonvoid_cells:
        selected = min(target_nonvoid_cells, key=lambda cell: (cell["candidate_count"], cell["q_lo"]))
    return {
        "p": packet["p"],
        "side": packet["side"],
        "shape_key": packet["shape_key"],
        "q_hull_lo": packet["q_hull_lo"],
        "q_hull_hi": packet["q_hull_hi"],
        "wheel17_survivor_values": packet["wheel17_survivor_values"],
        "target_union_intervals": packet["target_union_intervals"],
        "cell_count": packet["cell_count"],
        "target_overlap_cell_count": len(target_overlap_cells),
        "target_nonvoid_cell_count": len(target_nonvoid_cells),
        "pure_complement_nonvoid_cell_count": len(pure_complement_nonvoid_cells),
        "selected_target_escape_cell": selected,
        "selector_succeeds_in_finite_audit": selected is not None,
        "enriched_gap_cells": cells,
    }


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "target_overlap_selector",
            "status": "closed",
            "statement": "If a target-overlap gap cell contains a target prime, the original target-union void assumption is false.",
        },
        {
            "name": "finite_no_pure_complement_escape",
            "status": "finite_evidence",
            "statement": "In the finite frontier, every escaping prime lies in a target-overlap cell; pure complement cells do not supply escapes.",
        },
        {
            "name": "finite_target_escape_selector",
            "status": "finite_evidence",
            "statement": "Every finite packet has a selected target-overlap cell with at least one target prime.",
        },
        {
            "name": "global_target_overlap_prime_supply",
            "status": "open",
            "statement": "A global proof still needs a target prime in at least one selected target-overlap cell, or exclusion of target-cell void PDEC.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "TargetOverlapSelectorClosed",
            "closed": True,
            "proved": True,
            "meaning": "target-overlap cell 含 target prime 直接否定原始 union void。",
            "remaining": "closed",
        },
        {
            "gate": "FiniteSelectorSucceeds",
            "closed": result["selector_failure_count"] == 0,
            "proved": False,
            "meaning": "有限前沿每个包都有 target-overlap escape cell。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "FinitePureComplementEscapeAbsent",
            "closed": result["pure_complement_nonvoid_packet_count"] == 0,
            "proved": False,
            "meaning": "有限前沿纯互补 cell 未承担逃逸素数。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "GlobalTargetCellPrimeSupplyClosed",
            "closed": False,
            "proved": False,
            "meaning": "仍需全局证明选中 target-overlap cell 含 target prime。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只完成 escape cell 选择，不关闭全局行/列命题。",
            "remaining": NEXT_TARGET,
        },
    ]


def build_result(input_ledger: Path) -> dict[str, Any]:
    """构造 escape-cell selector 结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    source = load_json(input_ledger)
    selectors = [packet_selector(packet) for packet in source["packet_records"]]
    selected = [item["selected_target_escape_cell"] for item in selectors if item["selected_target_escape_cell"]]
    selector_failures = [item for item in selectors if not item["selector_succeeds_in_finite_audit"]]
    pure_complement_nonvoid = [item for item in selectors if item["pure_complement_nonvoid_cell_count"] > 0]
    aggregate = {
        "input_ledger": str(input_ledger.relative_to(ROOT)),
        "packet_count": len(selectors),
        "selector_success_count": len(selectors) - len(selector_failures),
        "selector_failure_count": len(selector_failures),
        "pure_complement_nonvoid_packet_count": len(pure_complement_nonvoid),
        "max_selected_cell_candidate_count": max((cell["candidate_count"] for cell in selected), default=0),
        "min_selected_cell_candidate_count": min((cell["candidate_count"] for cell in selected), default=0),
        "max_selected_target_prime_count": max((cell["target_prime_count"] for cell in selected), default=0),
        "min_selected_target_prime_count": min((cell["target_prime_count"] for cell in selected), default=0),
    }
    ledger = {
        "parameters": source["parameters"],
        "aggregate": aggregate,
        "selector_records": selectors,
        "selector_failures": selector_failures,
        "pure_complement_nonvoid_packets": pure_complement_nonvoid,
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = {
        "certificate_type": "prime_matrix_square_phase_offband_prefix_gap_shadow_escape_cell_selector_router",
        "status": "target_overlap_escape_cell_selector_registered_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "empirical_absence_not_used_as_proof": True,
        "parameters": source["parameters"],
        "aggregate": aggregate,
        "selector_records": selectors,
        "selector_failure_count": len(selector_failures),
        "pure_complement_nonvoid_packet_count": len(pure_complement_nonvoid),
        "target_overlap_selector_closed": True,
        "global_target_overlap_prime_supply_proved": False,
        "target_cell_void_pdec_excluded": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_escape_cell_selector_router.py": sha256(
                Path(__file__).resolve()
            ),
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_gap_cell_router.py": sha256(
                GAP_CELL_ROUTER
            ),
            "data/square-phase-offband-prefix-gap-shadow-gap-cell-ledger.json": sha256(input_ledger),
            "data/square-phase-offband-prefix-gap-shadow-escape-cell-selector-ledger.json": sha256(OUT_LEDGER),
        },
        "plain_conclusion": (
            "本步把 single gap-cell supply 再收窄到 target-overlap cell：只有落入目标 union 的素数才能直接否定"
            "原始 union void。有限前沿中每个包都可选出一个 target-overlap escape cell，且没有纯互补 cell 承担逃逸；"
            "全局仍需证明选中 target-overlap cell 必含 target prime，或排斥 target-cell void PDEC。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow escape cell selector router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"packet_count={agg['packet_count']}",
        f"selector_success_count={agg['selector_success_count']}",
        f"selector_failure_count={agg['selector_failure_count']}",
        f"pure_complement_nonvoid_packet_count={agg['pure_complement_nonvoid_packet_count']}",
        f"selected_cell_candidate_count_range={agg['min_selected_cell_candidate_count']}..{agg['max_selected_cell_candidate_count']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 选择规则",
        "",
        "只选择与目标 union 相交且实际含 target prime 的 gap cell；若能全局证明该 cell 含素数，则原始 target-union void 直接矛盾。",
        "",
        "## 2. 选择前沿",
        "",
        "| P | side | selected cell | type | target primes | complement primes |",
        "| ---: | --- | --- | --- | --- | --- |",
    ]
    for row in result["selector_records"]:
        cell = row["selected_target_escape_cell"]
        if not cell:
            selected_cell = "none"
            support_type = "none"
            target_primes = []
            complement_primes = []
        else:
            selected_cell = f"{cell['q_lo']}-{cell['q_hi']}"
            support_type = cell["support_type"]
            target_primes = cell["target_prime_values"]
            complement_primes = cell["complement_prime_values"]
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["p"]),
                    f"`{row['side']}`",
                    f"`{selected_cell}`",
                    f"`{support_type}`",
                    f"`{target_primes}`",
                    f"`{complement_primes}`",
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
            "- 对选中 target-overlap cells 建立统一素数供给，或证明同时为空会触发列相位/平方锚矛盾。",
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
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-escape-cell-selector-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "selector_failure_count": result["selector_failure_count"],
                "pure_complement_nonvoid_packet_count": result["pure_complement_nonvoid_packet_count"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
