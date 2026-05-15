#!/usr/bin/env python3
"""把支撑塌缩 PDEC 压成显式 gap cells 同时 prime-void。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_gap_cell_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-gap-cell-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-gap-cell-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-gap-cell-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-gap-cell-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from math import isqrt
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

INPUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-support-collapse-ledger.json"
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-gap-cell-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-gap-cell-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-gap-cell-router.md"

SUPPORT_COLLAPSE_ROUTER = (
    ROOT / "experiments" / "prime_matrix_square_phase_offband_prefix_gap_shadow_support_collapse_router.py"
)

MAIN_TARGET = "FixedSmallKPuncturedHullPrimeGapPatternExclusionOrSupportCollapsePDEC"
NEXT_TARGET = "SingleGapCellPrimeSupplyOrSimultaneousGapCellVoidPDEC"


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


def sieve(limit: int) -> bytearray:
    """筛出 limit 以内素数。"""
    flags = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        flags[0] = 0
    if limit >= 1:
        flags[1] = 0
    for value in range(2, isqrt(limit) + 1):
        if flags[value]:
            start = value * value
            flags[start : limit + 1 : value] = b"\x00" * (((limit - start) // value) + 1)
    return flags


def odd_values(q_lo: int, q_hi: int) -> list[int]:
    """列出奇候选 q。"""
    return list(range(q_lo, q_hi + 1, 2))


def in_intervals(value: int, intervals: list[dict[str, Any]]) -> bool:
    """判断 value 是否落入某个奇区间。"""
    return any(int(item["q_lo"]) <= value <= int(item["q_hi"]) for item in intervals)


def gap_cells(row: dict[str, Any], prime_flags: bytearray) -> list[dict[str, Any]]:
    """把 hull 去掉 wheel survivors 后切成连续 gap cells。"""
    survivors = set(row["wheel17_survivor_values"])
    intervals = row["target_union_intervals"]
    cells: list[dict[str, Any]] = []
    current: list[int] = []
    for value in odd_values(int(row["q_hull_lo"]), int(row["q_hull_hi"])):
        if value in survivors:
            if current:
                cells.append(cell_record(current, intervals, prime_flags))
                current = []
        else:
            current.append(value)
    if current:
        cells.append(cell_record(current, intervals, prime_flags))
    for index, cell in enumerate(cells, 1):
        cell["cell_index"] = index
        cell["cell_key"] = f"{row['p']}:{row['side']}:{cell['q_lo']}-{cell['q_hi']}"
    return cells


def cell_record(values: list[int], intervals: list[dict[str, Any]], prime_flags: bytearray) -> dict[str, Any]:
    """生成单个 gap cell 记录。"""
    target_values = [value for value in values if in_intervals(value, intervals)]
    prime_values = [value for value in values if prime_flags[value]]
    if not target_values:
        support_type = "complement_gap_cell"
    elif len(target_values) == len(values):
        support_type = "target_union_gap_cell"
    else:
        support_type = "mixed_gap_cell"
    return {
        "q_lo": values[0],
        "q_hi": values[-1],
        "candidate_count": len(values),
        "q_values": values,
        "support_type": support_type,
        "target_union_candidate_count": len(target_values),
        "complement_candidate_count": len(values) - len(target_values),
        "prime_values": prime_values,
        "prime_count": len(prime_values),
        "actual_cell_void": len(prime_values) == 0,
        "collapse_requires_cell_void": True,
    }


def packet_record(row: dict[str, Any], prime_flags: bytearray) -> dict[str, Any]:
    """生成单个 support-collapse 包的 gap-cell 分解。"""
    cells = gap_cells(row, prime_flags)
    nonvoid = [cell for cell in cells if not cell["actual_cell_void"]]
    max_cell = max((cell["candidate_count"] for cell in cells), default=0)
    return {
        "p": row["p"],
        "side": row["side"],
        "shape_key": row["shape_key"],
        "q_hull_lo": row["q_hull_lo"],
        "q_hull_hi": row["q_hull_hi"],
        "wheel17_survivor_values": row["wheel17_survivor_values"],
        "wheel17_survivor_count": row["wheel17_survivor_count"],
        "void_atom_keys": row["void_atom_keys"],
        "target_union_intervals": row["target_union_intervals"],
        "cell_count": len(cells),
        "max_gap_cell_candidate_count": max_cell,
        "actual_nonvoid_gap_cell_count": len(nonvoid),
        "actual_escape_prime_count": sum(cell["prime_count"] for cell in cells),
        "collapse_requires_all_cells_void": True,
        "all_cells_void_pdec_occurs_in_finite_audit": len(nonvoid) == 0,
        "gap_cells": cells,
        "nonvoid_gap_cells": nonvoid,
    }


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "support_collapse_to_gap_cells",
            "status": "closed",
            "statement": "A support-collapse packet is exactly the simultaneous prime-void condition on all non-survivor gap cells.",
        },
        {
            "name": "single_cell_prime_supply_excludes_packet",
            "status": "closed",
            "statement": "If any gap cell contains a prime, the corresponding support-collapse packet is impossible.",
        },
        {
            "name": "finite_no_all_cells_void",
            "status": "finite_evidence",
            "statement": "The finite audit finds at least one non-void gap cell in every packet.",
        },
        {
            "name": "global_single_gap_cell_prime_supply",
            "status": "open",
            "statement": "A global proof still needs a prime in at least one explicit gap cell for every fixed small-k packet, or exclusion of simultaneous cell void.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "GapCellDecompositionClosed",
            "closed": True,
            "proved": True,
            "meaning": "支撑塌缩已等价为所有非幸存 gap cells 同时 prime-void。",
            "remaining": "closed",
        },
        {
            "gate": "SingleCellPrimeSupplyCriterionClosed",
            "closed": True,
            "proved": True,
            "meaning": "任一 gap cell 含素数即可排除对应塌缩包。",
            "remaining": "closed",
        },
        {
            "gate": "FiniteNoAllCellsVoid",
            "closed": result["all_cells_void_packet_count"] == 0,
            "proved": False,
            "meaning": "有限前沿中没有所有 cells 同时空的包。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "GlobalGapCellPrimeSupplyClosed",
            "closed": False,
            "proved": False,
            "meaning": "仍需全局证明每个固定小 k 包至少一个 cell 含素数。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只完成 PDEC 的 gap-cell 分解，不关闭全局行/列命题。",
            "remaining": NEXT_TARGET,
        },
    ]


def build_result(input_ledger: Path) -> dict[str, Any]:
    """构造 gap-cell 路由结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    source = load_json(input_ledger)
    max_q = max((row["q_hull_hi"] for row in source["collapse_records"]), default=2)
    prime_flags = sieve(max_q)
    packets = [packet_record(row, prime_flags) for row in source["collapse_records"]]
    frontier = sorted(packets, key=lambda item: (item["actual_nonvoid_gap_cell_count"], item["actual_escape_prime_count"], item["p"]))
    all_cells = [cell for packet in packets for cell in packet["gap_cells"]]
    nonvoid_cells = [cell for cell in all_cells if not cell["actual_cell_void"]]
    aggregate = {
        "input_ledger": str(input_ledger.relative_to(ROOT)),
        "packet_count": len(packets),
        "gap_cell_count": len(all_cells),
        "nonvoid_gap_cell_count": len(nonvoid_cells),
        "all_cells_void_packet_count": sum(1 for packet in packets if packet["all_cells_void_pdec_occurs_in_finite_audit"]),
        "min_nonvoid_cells_per_packet": min((packet["actual_nonvoid_gap_cell_count"] for packet in packets), default=None),
        "min_escape_primes_per_packet": min((packet["actual_escape_prime_count"] for packet in packets), default=None),
        "max_gap_cell_candidate_count": max((cell["candidate_count"] for cell in all_cells), default=0),
        "max_packet_gap_cell_count": max((packet["cell_count"] for packet in packets), default=0),
    }
    ledger = {
        "parameters": source["parameters"],
        "aggregate": aggregate,
        "packet_records": packets,
        "packet_frontier": frontier,
        "all_cells_void_packets": [packet for packet in packets if packet["all_cells_void_pdec_occurs_in_finite_audit"]],
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = {
        "certificate_type": "prime_matrix_square_phase_offband_prefix_gap_shadow_gap_cell_router",
        "status": "support_collapse_reduced_to_simultaneous_gap_cell_void_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "empirical_absence_not_used_as_proof": True,
        "parameters": source["parameters"],
        "aggregate": aggregate,
        "packet_frontier": frontier,
        "all_cells_void_packet_count": aggregate["all_cells_void_packet_count"],
        "gap_cell_decomposition_closed": True,
        "single_gap_cell_prime_supply_proved_globally": False,
        "simultaneous_gap_cell_void_pdec_excluded": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_gap_cell_router.py": sha256(
                Path(__file__).resolve()
            ),
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_support_collapse_router.py": sha256(
                SUPPORT_COLLAPSE_ROUTER
            ),
            "data/square-phase-offband-prefix-gap-shadow-support-collapse-ledger.json": sha256(input_ledger),
            "data/square-phase-offband-prefix-gap-shadow-gap-cell-ledger.json": sha256(OUT_LEDGER),
        },
        "plain_conclusion": (
            "本步把支撑塌缩 PDEC 精确切成 gap cells：wheel-17 survivor 是允许落素数的穿孔点，"
            "其余 hull 奇候选分成若干连续 cell；支撑塌缩等价于所有这些 cells 同时 prime-void。"
            "有限账本中每个包至少有一个非空 cell，因此 all-cells-void 包数为 0；全局仍需证明"
            "每个固定小 k 包至少一个显式 cell 含素数，或排斥 simultaneous cell void PDEC。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow gap cell router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"packet_count={agg['packet_count']}",
        f"gap_cell_count={agg['gap_cell_count']}",
        f"all_cells_void_packet_count={agg['all_cells_void_packet_count']}",
        f"min_nonvoid_cells_per_packet={agg['min_nonvoid_cells_per_packet']}",
        f"min_escape_primes_per_packet={agg['min_escape_primes_per_packet']}",
        f"max_gap_cell_candidate_count={agg['max_gap_cell_candidate_count']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. gap-cell 等价",
        "",
        "对每个支撑塌缩包，删除 wheel-17 survivor 后，hull 中剩余奇候选自动分成若干连续 gap cells。",
        "支撑塌缩等价于：",
        "",
        "```text",
        "every gap cell is prime-void",
        "```",
        "",
        "因此任一 gap cell 含素数，就立即排除该包。",
        "",
        "## 2. 最紧包前沿",
        "",
        "| P | side | hull | survivors | cells | nonvoid cells | escape primes | largest cell |",
        "| ---: | --- | --- | --- | ---: | ---: | ---: | ---: |",
    ]
    for packet in result["packet_frontier"][:16]:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(packet["p"]),
                    f"`{packet['side']}`",
                    f"`{packet['q_hull_lo']}-{packet['q_hull_hi']}`",
                    f"`{packet['wheel17_survivor_values']}`",
                    str(packet["cell_count"]),
                    str(packet["actual_nonvoid_gap_cell_count"]),
                    str(packet["actual_escape_prime_count"]),
                    str(packet["max_gap_cell_candidate_count"]),
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
            "- 优先挑选每个包中最短且结构最稳定的非幸存 cell，证明其含素数或接入列相位矛盾。",
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
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-gap-cell-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "packet_count": result["aggregate"]["packet_count"],
                "gap_cell_count": result["aggregate"]["gap_cell_count"],
                "all_cells_void_packet_count": result["all_cells_void_packet_count"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
