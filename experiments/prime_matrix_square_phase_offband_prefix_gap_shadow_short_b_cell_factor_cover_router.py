#!/usr/bin/env python3
"""把 selected non-survivor small-k cell void 压成短 b 单元小因子覆盖。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_short_b_cell_factor_cover_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-short-b-cell-factor-cover-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-short-b-cell-factor-cover-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-short-b-cell-factor-cover-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-short-b-cell-factor-cover-router.md
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

INPUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-contradiction-field-ledger.json"
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-short-b-cell-factor-cover-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-short-b-cell-factor-cover-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-short-b-cell-factor-cover-router.md"

CONTRADICTION_FIELD_ROUTER = (
    ROOT / "experiments" / "prime_matrix_square_phase_offband_prefix_gap_shadow_contradiction_field_router.py"
)

MAIN_TARGET = "SelectedNonSurvivorSmallKCellPrimeSupplyOrPuncturedCellVoidPDEC"
NEXT_TARGET = "ShortBCellCompleteSmallFactorCoverPDECExclusionOrPhaseLift"


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


def prime_values(limit: int) -> list[int]:
    """筛出不超过 limit 的素数。"""
    if limit < 2:
        return []
    flags = bytearray(b"\x01") * (limit + 1)
    flags[0:2] = b"\x00\x00"
    for value in range(2, isqrt(limit) + 1):
        if flags[value]:
            start = value * value
            flags[start : limit + 1 : value] = b"\x00" * (((limit - start) // value) + 1)
    return [value for value in range(2, limit + 1) if flags[value]]


def small_prime_divisors(value: int, bound: int) -> list[int]:
    """列出 value 的小素因子。"""
    return [prime for prime in prime_values(min(isqrt(value), bound)) if value % prime == 0]


def candidate_record(p_value: int, q_value: int) -> dict[str, Any]:
    """生成单个 q=P-2b 候选的因子覆盖记录。"""
    b_value = (p_value - q_value) // 2
    bound = isqrt(p_value)
    labels = small_prime_divisors(q_value, bound)
    least = labels[0] if labels else None
    return {
        "q": q_value,
        "b": b_value,
        "sqrt_p_floor": bound,
        "is_prime_actual": len(labels) == 0 and q_value > 1,
        "small_factor_labels": labels,
        "least_small_factor_label": least,
        "covered_by_small_factor": bool(labels),
        "residue_cover_formulas": [f"P ≡ {2 * b_value} (mod {label})" for label in labels],
    }


def max_label_reuse_in_short_cell(length: int, label: int) -> int:
    """短 b 区间内同一奇素标签最多命中多少个位置。"""
    if label <= 0:
        return 0
    return (length - 1) // label + 1


def label_reuse_bound(length: int) -> dict[str, Any]:
    """登记短 cell 的标签复用刚性。"""
    return {
        "cell_length": length,
        "label_3_max_hits": max_label_reuse_in_short_cell(length, 3),
        "label_ge_5_max_hits": 1,
        "explanation": (
            "If the same odd prime ell divides P-2b_i and P-2b_j, then ell divides b_i-b_j. "
            "For length<=5, only ell=3 can repeat, and only across b-distance 3."
        ),
    }


def factor_cover_record(row: dict[str, Any]) -> dict[str, Any]:
    """把单个 selected cell 改写为小因子覆盖系统。"""
    p_value = int(row["p"])
    candidates = [candidate_record(p_value, int(q_value)) for q_value in row["selected_values"]]
    uncovered = [item for item in candidates if not item["covered_by_small_factor"]]
    covered = [item for item in candidates if item["covered_by_small_factor"]]
    distinct_least_labels = sorted({item["least_small_factor_label"] for item in covered if item["least_small_factor_label"]})
    length = int(row["selected_candidate_count"])
    return {
        "index": row["index"],
        "p": p_value,
        "side": row["side"],
        "shape_key": row["shape_key"],
        "selected_q_lo": row["selected_q_lo"],
        "selected_q_hi": row["selected_q_hi"],
        "b_lo": row["b_lo"],
        "b_hi": row["b_hi"],
        "cell_length": length,
        "parent_atom_key": row["parent_atom_key"],
        "parent_atom_band": row["parent_atom_band"],
        "parent_atom_k": row["parent_atom_k"],
        "candidates": candidates,
        "covered_candidate_count": len(covered),
        "uncovered_candidate_count": len(uncovered),
        "uncovered_q_values": [item["q"] for item in uncovered],
        "actual_cell_void": len(uncovered) == 0,
        "distinct_least_small_factor_labels": distinct_least_labels,
        "distinct_least_small_factor_label_count": len(distinct_least_labels),
        "label_reuse_bound": label_reuse_bound(length),
        "void_equivalence_statement": (
            f"The selected cell is void iff every b in [{row['b_lo']},{row['b_hi']}] "
            "is covered by at least one odd prime ell<=sqrt(P) with P≡2b (mod ell)."
        ),
        "next_attack_statement": (
            "A surviving counterexample must realize a complete short residue-cover word "
            "inside this fixed small-k phase cell."
        ),
    }


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "cell_void_to_small_factor_cover",
            "status": "closed",
            "statement": "Since every selected q is below P, q-composite is equivalent to the existence of a prime divisor ell<=sqrt(P).",
        },
        {
            "name": "small_factor_cover_to_crt_residue_word",
            "status": "closed",
            "statement": "For q=P-2b, a small factor ell gives the residue constraint P≡2b mod ell.",
        },
        {
            "name": "short_cell_label_reuse_bound",
            "status": "closed",
            "statement": "In a b-cell of length at most five, an odd label ell>=5 hits at most one b; ell=3 can hit at most two.",
        },
        {
            "name": "finite_incomplete_cover_frontier",
            "status": "finite_evidence",
            "statement": "The finite frontier has at least one uncovered candidate in every selected cell.",
        },
        {
            "name": "global_complete_cover_exclusion",
            "status": "open",
            "statement": "A global proof still needs to exclude complete short residue-cover words under the fixed small-k phase constraints.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "CellVoidSmallFactorCoverEquivalenceClosed",
            "closed": True,
            "proved": True,
            "meaning": "selected-cell void 已等价写成短 b 区间的小素因子覆盖。",
            "remaining": "closed",
        },
        {
            "gate": "CRTResidueWordFormClosed",
            "closed": True,
            "proved": True,
            "meaning": "每个覆盖标签都是 `P ≡ 2b (mod ell)` 的 CRT 残基约束。",
            "remaining": "closed",
        },
        {
            "gate": "FiniteNoCompleteCover",
            "closed": result["complete_small_factor_cover_actual_count"] == 0,
            "proved": False,
            "meaning": "有限前沿每个 selected cell 都至少有一个未被小因子覆盖的位置。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "GlobalCompleteCoverExcluded",
            "closed": False,
            "proved": False,
            "meaning": "仍需排斥固定 small-k 相位下的完整短覆盖字，或证明其回流到 PDEC/ColumnCRT。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只把终端 void 改写为残基覆盖系统，不关闭全局命题。",
            "remaining": NEXT_TARGET,
        },
    ]


def build_result(input_ledger: Path) -> dict[str, Any]:
    """构造短 b 单元小因子覆盖路由结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    source = load_json(input_ledger)
    records = [factor_cover_record(row) for row in source["field_records"]]
    complete_cover_records = [row for row in records if row["actual_cell_void"]]
    aggregate = {
        "input_ledger": str(input_ledger.relative_to(ROOT)),
        "record_count": len(records),
        "complete_small_factor_cover_actual_count": len(complete_cover_records),
        "min_uncovered_candidate_count": min((row["uncovered_candidate_count"] for row in records), default=0),
        "max_uncovered_candidate_count": max((row["uncovered_candidate_count"] for row in records), default=0),
        "max_cell_length": max((row["cell_length"] for row in records), default=0),
        "max_parent_atom_k": max((row["parent_atom_k"] for row in records), default=0),
        "max_distinct_least_small_factor_label_count": max(
            (row["distinct_least_small_factor_label_count"] for row in records),
            default=0,
        ),
        "global_complete_cover_excluded": False,
        "direct_unconditional_contradiction_found": False,
    }
    ledger = {
        "parameters": source["parameters"],
        "aggregate": aggregate,
        "factor_cover_records": records,
        "complete_small_factor_cover_actual_records": complete_cover_records,
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = {
        "certificate_type": "prime_matrix_square_phase_offband_prefix_gap_shadow_short_b_cell_factor_cover_router",
        "status": "selected_cell_void_reduced_to_short_b_small_factor_cover_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "empirical_absence_not_used_as_proof": True,
        "parameters": source["parameters"],
        "aggregate": aggregate,
        "factor_cover_records": records,
        "complete_small_factor_cover_actual_count": len(complete_cover_records),
        "global_complete_cover_excluded": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_short_b_cell_factor_cover_router.py": sha256(
                Path(__file__).resolve()
            ),
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_contradiction_field_router.py": sha256(
                CONTRADICTION_FIELD_ROUTER
            ),
            "data/square-phase-offband-prefix-gap-shadow-contradiction-field-ledger.json": sha256(input_ledger),
            "data/square-phase-offband-prefix-gap-shadow-short-b-cell-factor-cover-ledger.json": sha256(
                OUT_LEDGER
            ),
        },
        "plain_conclusion": (
            "本步把 selected non-survivor small-k cell 的 void 进一步改写为短 b 单元小因子覆盖："
            "因为每个 q=P-2b 都小于 P，若 q 合数则有素因子 ell<=sqrt(P)，等价于 CRT 残基 "
            "P≡2b (mod ell)。有限前沿每个 cell 都至少有一个未被小因子覆盖的位置，即实际素数；"
            "但全局仍需排斥完整短覆盖字，或把它提升为固定相位 PDEC/ColumnCRT 矛盾。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow short-b cell factor cover router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"record_count={agg['record_count']}",
        f"complete_small_factor_cover_actual_count={agg['complete_small_factor_cover_actual_count']}",
        f"uncovered_candidate_count_range={agg['min_uncovered_candidate_count']}..{agg['max_uncovered_candidate_count']}",
        f"max_cell_length={agg['max_cell_length']}",
        f"max_parent_atom_k={agg['max_parent_atom_k']}",
        f"max_distinct_least_small_factor_label_count={agg['max_distinct_least_small_factor_label_count']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 等价压缩",
        "",
        "对 selected cell 中的每个候选：",
        "",
        "```text",
        "q = P - 2b < P",
        "q composite  <=>  exists prime ell <= sqrt(P) with ell | q",
        "ell | q      <=>  P ≡ 2b (mod ell)",
        "```",
        "",
        "因此 selected-cell void 等价于短 b 区间被这些小素因子残基完全覆盖。",
        "",
        "## 2. 覆盖前沿",
        "",
        "| P | side | b cell | q cell | covered | uncovered q | least labels |",
        "| ---: | --- | --- | --- | ---: | --- | --- |",
    ]
    for row in result["factor_cover_records"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["p"]),
                    f"`{row['side']}`",
                    f"`{row['b_lo']}-{row['b_hi']}`",
                    f"`{row['selected_q_lo']}-{row['selected_q_hi']}`",
                    f"`{row['covered_candidate_count']}/{row['cell_length']}`",
                    f"`{row['uncovered_q_values']}`",
                    f"`{row['distinct_least_small_factor_labels']}`",
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 3. 标签复用刚性",
            "",
            "若同一奇素数 `ell` 同时覆盖 `b_i,b_j`，则 `ell | b_i-b_j`。在长度至多 5 的 cell 中，`ell>=5` 至多覆盖一个位置，只有 `ell=3` 可能隔 3 个 b 复用一次。",
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
            "- 直接目标是排斥完整短覆盖字：所有 `b` 都被 `P≡2b (mod ell)` 小素标签覆盖。",
            "- 这正好对接 CRT/逆元最小对齐解思路，但目前还没有推出全局矛盾。",
            "- 当前仍未证明全局行/列无条件闭合。",
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
    parser.add_argument("--input-ledger", type=Path, default=INPUT_LEDGER)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    input_ledger = args.input_ledger if args.input_ledger.is_absolute() else ROOT / args.input_ledger
    result = build_result(input_ledger)
    write_markdown(result)
    result["source_hashes"][
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-short-b-cell-factor-cover-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "complete_small_factor_cover_actual_count": result["complete_small_factor_cover_actual_count"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
