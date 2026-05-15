#!/usr/bin/env python3
"""把 atom-piece void 与 support-collapse 链合并成终端矛盾场。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_contradiction_field_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-contradiction-field-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-contradiction-field-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-contradiction-field-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-contradiction-field-router.md
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

BOUNDARY_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-atom-piece-void-boundary-ledger.json"
SUPPORT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-support-collapse-ledger.json"
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-contradiction-field-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-contradiction-field-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-contradiction-field-router.md"

BOUNDARY_ROUTER = (
    ROOT / "experiments" / "prime_matrix_square_phase_offband_prefix_gap_shadow_atom_piece_void_boundary_router.py"
)
SUPPORT_ROUTER = ROOT / "experiments" / "prime_matrix_square_phase_offband_prefix_gap_shadow_support_collapse_router.py"

MAIN_TARGET = "CounterexampleConditionalSmallKAtomPieceVoidContradictionOrColumnPhasePDEC"
NEXT_TARGET = "SelectedNonSurvivorSmallKCellPrimeSupplyOrPuncturedCellVoidPDEC"


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


def merge_record(boundary: dict[str, Any], support: dict[str, Any], index: int) -> dict[str, Any]:
    """合并单条 atom-piece boundary 与 support-collapse 记录。"""
    selected_values = odd_values(int(boundary["q_lo"]), int(boundary["q_hi"]))
    survivor_set = set(support["wheel17_survivor_values"])
    survivor_intersection = sorted(set(selected_values) & survivor_set)
    selected_prime_set = set(boundary["actual_target_prime_values"])
    escape_prime_set = set(support["actual_escape_prime_values"])
    selected_escape_primes = sorted(selected_prime_set & escape_prime_set)
    return {
        "index": index,
        "p": boundary["p"],
        "side": boundary["side"],
        "shape_key": boundary["shape_key"],
        "q_hull_lo": support["q_hull_lo"],
        "q_hull_hi": support["q_hull_hi"],
        "selected_q_lo": boundary["q_lo"],
        "selected_q_hi": boundary["q_hi"],
        "selected_values": selected_values,
        "selected_candidate_count": boundary["candidate_count"],
        "b_lo": boundary["b_lo"],
        "b_hi": boundary["b_hi"],
        "parent_atom_key": boundary["parent_atom_key"],
        "parent_atom_band": boundary["parent_atom_band"],
        "parent_atom_k": boundary["parent_atom_k"],
        "wheel17_survivor_values": support["wheel17_survivor_values"],
        "wheel17_survivor_intersection": survivor_intersection,
        "wheel17_survivor_intersection_count": len(survivor_intersection),
        "selected_piece_disjoint_from_survivors": len(survivor_intersection) == 0,
        "actual_selected_prime_values": boundary["actual_target_prime_values"],
        "actual_escape_prime_values": support["actual_escape_prime_values"],
        "actual_selected_escape_prime_values": selected_escape_primes,
        "actual_selected_escape_prime_count": len(selected_escape_primes),
        "actual_selected_piece_void": boundary["actual_atom_piece_void"],
        "actual_support_collapse_occurs": support["actual_support_collapse_occurs"],
        "field_implication": (
            "Because the selected atom-piece is disjoint from wheel-17 survivors, "
            "any prime in it is automatically an escape prime and destroys support collapse."
        ),
        "hypothetical_failure_form": (
            "A counterexample can survive this field only if every selected non-survivor "
            "q-candidate in the small-k cell is composite."
        ),
    }


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "selected_piece_survivor_disjointness",
            "status": "closed",
            "statement": "Every selected atom-piece in the frontier is disjoint from the wheel-17 survivor set.",
        },
        {
            "name": "selected_prime_implies_support_collapse_escape",
            "status": "closed",
            "statement": "A prime in the selected atom-piece is automatically an escape prime outside the support-collapse survivor set.",
        },
        {
            "name": "finite_selected_escape_prime_present",
            "status": "finite_evidence",
            "statement": "The finite frontier has at least one selected escape prime in every merged field packet.",
        },
        {
            "name": "direct_structural_contradiction_from_existing_constraints",
            "status": "open",
            "statement": "The existing constraints alone do not yet force a prime in the selected non-survivor cell.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "SelectedPieceDisjointFromSurvivorsClosed",
            "closed": result["all_selected_pieces_disjoint_from_survivors"],
            "proved": True,
            "meaning": "selected atom-piece 是 wheel-17 支撑塌缩幸存集之外的逃逸单元。",
            "remaining": "closed",
        },
        {
            "gate": "PrimeInSelectedPieceBreaksSupportCollapse",
            "closed": True,
            "proved": True,
            "meaning": "该单元一旦含素数，就直接给出 escape prime，反例链崩溃。",
            "remaining": "closed",
        },
        {
            "gate": "FiniteSelectedEscapePrimePresent",
            "closed": result["min_actual_selected_escape_prime_count"] > 0,
            "proved": False,
            "meaning": "有限前沿每包都有 selected escape prime；仍不能当全局证明。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "ExistingConstraintsForceSelectedPrime",
            "closed": False,
            "proved": False,
            "meaning": "现有支撑塌缩、列相位和 q=P-2b 正规形尚未强制该小单元含素数。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步把终端矛盾场压到非幸存 small-k cell 素数供给，不关闭全局命题。",
            "remaining": NEXT_TARGET,
        },
    ]


def build_result(boundary_ledger: Path, support_ledger: Path) -> dict[str, Any]:
    """构造终端矛盾场路由结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    boundary_source = load_json(boundary_ledger)
    support_source = load_json(support_ledger)
    boundary_records = boundary_source["boundary_records"]
    support_records = support_source["collapse_records"]
    if len(boundary_records) != len(support_records):
        raise ValueError("boundary/support record counts differ")
    records = [merge_record(boundary, support, index) for index, (boundary, support) in enumerate(zip(boundary_records, support_records))]
    all_disjoint = all(row["selected_piece_disjoint_from_survivors"] for row in records)
    aggregate = {
        "boundary_ledger": str(boundary_ledger.relative_to(ROOT)),
        "support_ledger": str(support_ledger.relative_to(ROOT)),
        "record_count": len(records),
        "all_selected_pieces_disjoint_from_survivors": all_disjoint,
        "max_wheel17_survivor_intersection_count": max(
            (row["wheel17_survivor_intersection_count"] for row in records),
            default=0,
        ),
        "min_actual_selected_escape_prime_count": min(
            (row["actual_selected_escape_prime_count"] for row in records),
            default=0,
        ),
        "actual_selected_escape_prime_packet_count": sum(
            1 for row in records if row["actual_selected_escape_prime_count"] > 0
        ),
        "actual_support_collapse_count": sum(1 for row in records if row["actual_support_collapse_occurs"]),
        "max_selected_candidate_count": max((row["selected_candidate_count"] for row in records), default=0),
        "max_parent_atom_k": max((row["parent_atom_k"] for row in records), default=0),
        "direct_structural_contradiction_found": False,
    }
    ledger = {
        "parameters": boundary_source["parameters"],
        "aggregate": aggregate,
        "field_records": records,
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = {
        "certificate_type": "prime_matrix_square_phase_offband_prefix_gap_shadow_contradiction_field_router",
        "status": "terminal_contradiction_field_reduced_to_selected_nonsurvivor_cell_supply_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "empirical_absence_not_used_as_proof": True,
        "parameters": boundary_source["parameters"],
        "aggregate": aggregate,
        "field_records": records,
        "all_selected_pieces_disjoint_from_survivors": all_disjoint,
        "min_actual_selected_escape_prime_count": aggregate["min_actual_selected_escape_prime_count"],
        "counterexample_conditional_atom_piece_void_excluded": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_contradiction_field_router.py": sha256(
                Path(__file__).resolve()
            ),
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_atom_piece_void_boundary_router.py": sha256(
                BOUNDARY_ROUTER
            ),
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_support_collapse_router.py": sha256(
                SUPPORT_ROUTER
            ),
            "data/square-phase-offband-prefix-gap-shadow-atom-piece-void-boundary-ledger.json": sha256(
                boundary_ledger
            ),
            "data/square-phase-offband-prefix-gap-shadow-support-collapse-ledger.json": sha256(support_ledger),
            "data/square-phase-offband-prefix-gap-shadow-contradiction-field-ledger.json": sha256(OUT_LEDGER),
        },
        "plain_conclusion": (
            "本步把 atom-piece void 与 support-collapse 合并成终端矛盾场：所有 selected atom piece "
            "都与 wheel-17 survivor 集合不相交，因此其中任一素数都会成为 escape prime 并否定支撑塌缩。"
            "有限前沿每包确有 selected escape prime；但现有结构还没有全局强制该非幸存 small-k cell 含素数。"
            "最新剩余压成 selected non-survivor small-k cell 的素数供给，或排斥 punctured cell void PDEC。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow contradiction field router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"record_count={agg['record_count']}",
        f"all_selected_pieces_disjoint_from_survivors={fmt_bool(agg['all_selected_pieces_disjoint_from_survivors'])}",
        f"max_wheel17_survivor_intersection_count={agg['max_wheel17_survivor_intersection_count']}",
        f"min_actual_selected_escape_prime_count={agg['min_actual_selected_escape_prime_count']}",
        f"actual_support_collapse_count={agg['actual_support_collapse_count']}",
        f"max_selected_candidate_count={agg['max_selected_candidate_count']}",
        f"max_parent_atom_k={agg['max_parent_atom_k']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 终端矛盾场",
        "",
        "合并后的逻辑是：",
        "",
        "```text",
        "support collapse: Prime(hull) subset wheel17 survivors",
        "selected atom piece: selected cell subset hull and selected cell cap wheel17 survivors = empty",
        "therefore: any prime in selected cell is an escape prime and contradicts support collapse",
        "remaining: prove selected cell contains a prime, or exclude selected-cell void as PDEC",
        "```",
        "",
        "## 2. 合并前沿",
        "",
        "| P | side | selected cell | survivors | intersection | selected escape primes |",
        "| ---: | --- | --- | --- | --- | --- |",
    ]
    for row in result["field_records"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["p"]),
                    f"`{row['side']}`",
                    f"`{row['selected_q_lo']}-{row['selected_q_hi']}`",
                    f"`{row['wheel17_survivor_values']}`",
                    f"`{row['wheel17_survivor_intersection']}`",
                    f"`{row['actual_selected_escape_prime_values']}`",
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
            "- 需要证明 selected non-survivor small-k cell 含素数，或把该 cell void 解释成固定相位 PDEC 并排斥。",
            "- 这一步没有把目标换成普通短素数间隙；仍保持同一 off-band prefix 反例链。",
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
    parser.add_argument("--boundary-ledger", type=Path, default=BOUNDARY_LEDGER)
    parser.add_argument("--support-ledger", type=Path, default=SUPPORT_LEDGER)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    boundary_ledger = args.boundary_ledger if args.boundary_ledger.is_absolute() else ROOT / args.boundary_ledger
    support_ledger = args.support_ledger if args.support_ledger.is_absolute() else ROOT / args.support_ledger
    result = build_result(boundary_ledger, support_ledger)
    write_markdown(result)
    result["source_hashes"][
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-contradiction-field-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "all_selected_pieces_disjoint_from_survivors": result[
                    "all_selected_pieces_disjoint_from_survivors"
                ],
                "min_actual_selected_escape_prime_count": result["min_actual_selected_escape_prime_count"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
