#!/usr/bin/env python3
"""把短 b 单元完整小因子覆盖提升为 CRT 覆盖词边界。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_crt_cover_word_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-crt-cover-word-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-crt-cover-word-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-crt-cover-word-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-crt-cover-word-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from math import prod
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

INPUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-short-b-cell-factor-cover-ledger.json"
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-crt-cover-word-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-crt-cover-word-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-crt-cover-word-router.md"

FACTOR_COVER_ROUTER = (
    ROOT / "experiments" / "prime_matrix_square_phase_offband_prefix_gap_shadow_short_b_cell_factor_cover_router.py"
)

MAIN_TARGET = "ShortBCellCompleteSmallFactorCoverPDECExclusionOrPhaseLift"
NEXT_TARGET = "CompatibleCRTCoverWordPDECExclusionOrColumnPhaseLift"

SMALL_ODD_PRIMES = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]


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


def min_distinct_labels_for_length(length: int) -> int:
    """长度不超过 5 时完整覆盖至少需要多少个不同奇素标签。"""
    if length <= 3:
        return length
    return length - 1


def min_modulus_for_length(length: int) -> int:
    """短覆盖词的最小可能 CRT 模数下界。"""
    count = min_distinct_labels_for_length(length)
    return prod(SMALL_ODD_PRIMES[:count])


def actual_partial_modulus(labels: list[int]) -> int:
    """实际已覆盖位置的最小标签模数。"""
    return prod(sorted(set(labels))) if labels else 1


def missing_label_count_lower_bound(length: int, labels: list[int], uncovered_count: int) -> int:
    """补成完整覆盖还至少需要多少个新标签。"""
    have = len(set(labels))
    need = min_distinct_labels_for_length(length)
    return max(uncovered_count, need - have, 0)


def crt_word_record(row: dict[str, Any]) -> dict[str, Any]:
    """生成单个短 b cell 的 CRT 覆盖词记录。"""
    labels = [label for item in row["candidates"] for label in item["small_factor_labels"]]
    least_labels = row["distinct_least_small_factor_labels"]
    length = int(row["cell_length"])
    missing = missing_label_count_lower_bound(length, least_labels, int(row["uncovered_candidate_count"]))
    min_word_modulus = min_modulus_for_length(length)
    partial_modulus = actual_partial_modulus(least_labels)
    return {
        "index": row["index"],
        "p": row["p"],
        "side": row["side"],
        "shape_key": row["shape_key"],
        "b_lo": row["b_lo"],
        "b_hi": row["b_hi"],
        "selected_q_lo": row["selected_q_lo"],
        "selected_q_hi": row["selected_q_hi"],
        "cell_length": length,
        "parent_atom_key": row["parent_atom_key"],
        "parent_atom_band": row["parent_atom_band"],
        "parent_atom_k": row["parent_atom_k"],
        "uncovered_q_values": row["uncovered_q_values"],
        "uncovered_candidate_count": row["uncovered_candidate_count"],
        "actual_least_label_set": least_labels,
        "actual_all_small_label_set": sorted(set(labels)),
        "actual_partial_crt_modulus": partial_modulus,
        "min_distinct_labels_for_complete_word": min_distinct_labels_for_length(length),
        "missing_new_label_count_lower_bound": missing,
        "min_complete_word_crt_modulus_lower_bound": min_word_modulus,
        "same_label_reuse_rule": (
            "The same odd label ell can cover two offsets only if their b-distance is divisible by ell; "
            "for length<=5 this permits only ell=3 at distance 3."
        ),
        "crt_word_form": (
            "For offsets t=0..L-1 with B=b_lo, a complete cover word chooses labels ell_t "
            "such that P-2(B+t)≡0 mod ell_t. Equivalently q_start=P-2B satisfies "
            "q_start≡2t mod ell_t for every t."
        ),
        "phase_lift_obligation": (
            "Exclude compatible CRT cover words inside the fixed small-k atom inequalities, "
            "or lift them to a ColumnCRT/PDEC certificate."
        ),
    }


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "same_label_reuse_rule",
            "status": "closed",
            "statement": "A repeated odd label ell in a consecutive b-cell is possible only across b-distance divisible by ell.",
        },
        {
            "name": "short_cell_min_distinct_label_bound",
            "status": "closed",
            "statement": "For cell length L<=5, a complete cover word needs at least L labels for L<=3 and L-1 labels for L>=4.",
        },
        {
            "name": "complete_cover_word_crt_progression",
            "status": "closed",
            "statement": "Every complete label word defines a compatible CRT progression for q_start=P-2B.",
        },
        {
            "name": "finite_partial_words_not_complete",
            "status": "finite_evidence",
            "statement": "The finite frontier only has partial cover words; every selected cell has missing labels/uncovered q-values.",
        },
        {
            "name": "global_compatible_word_exclusion",
            "status": "open",
            "statement": "A global proof still needs to exclude compatible CRT cover words inside the fixed small-k phase cell.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "CRTCoverWordNormalFormClosed",
            "closed": True,
            "proved": True,
            "meaning": "完整小因子覆盖已提升为 `q_start=P-2B` 的 CRT 覆盖词。",
            "remaining": "closed",
        },
        {
            "gate": "ShortCellLabelMultiplicityBoundClosed",
            "closed": True,
            "proved": True,
            "meaning": "长度至多 5 的覆盖词有明确的最少不同标签数和模数下界。",
            "remaining": "closed",
        },
        {
            "gate": "FiniteNoCompleteWord",
            "closed": result["complete_crt_cover_word_actual_count"] == 0,
            "proved": False,
            "meaning": "有限前沿只有 partial word，没有完整覆盖词；仍只是有限证据。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "GlobalCompatibleWordExcluded",
            "closed": False,
            "proved": False,
            "meaning": "CRT 兼容本身不矛盾，仍需接固定 small-k 相位与列相位排斥。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只完成 CRT 覆盖词正规形，不关闭全局命题。",
            "remaining": NEXT_TARGET,
        },
    ]


def build_result(input_ledger: Path) -> dict[str, Any]:
    """构造 CRT 覆盖词路由结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    source = load_json(input_ledger)
    records = [crt_word_record(row) for row in source["factor_cover_records"]]
    complete_count = sum(1 for row in records if row["uncovered_candidate_count"] == 0)
    aggregate = {
        "input_ledger": str(input_ledger.relative_to(ROOT)),
        "record_count": len(records),
        "complete_crt_cover_word_actual_count": complete_count,
        "min_missing_new_label_count_lower_bound": min(
            (row["missing_new_label_count_lower_bound"] for row in records),
            default=0,
        ),
        "max_missing_new_label_count_lower_bound": max(
            (row["missing_new_label_count_lower_bound"] for row in records),
            default=0,
        ),
        "min_complete_word_crt_modulus_lower_bound": min(
            (row["min_complete_word_crt_modulus_lower_bound"] for row in records),
            default=0,
        ),
        "max_complete_word_crt_modulus_lower_bound": max(
            (row["min_complete_word_crt_modulus_lower_bound"] for row in records),
            default=0,
        ),
        "max_cell_length": max((row["cell_length"] for row in records), default=0),
        "global_compatible_word_excluded": False,
        "direct_unconditional_contradiction_found": False,
    }
    ledger = {
        "parameters": source["parameters"],
        "aggregate": aggregate,
        "crt_word_records": records,
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = {
        "certificate_type": "prime_matrix_square_phase_offband_prefix_gap_shadow_crt_cover_word_router",
        "status": "complete_small_factor_cover_reduced_to_crt_cover_word_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "empirical_absence_not_used_as_proof": True,
        "parameters": source["parameters"],
        "aggregate": aggregate,
        "crt_word_records": records,
        "complete_crt_cover_word_actual_count": complete_count,
        "global_compatible_word_excluded": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_crt_cover_word_router.py": sha256(
                Path(__file__).resolve()
            ),
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_short_b_cell_factor_cover_router.py": sha256(
                FACTOR_COVER_ROUTER
            ),
            "data/square-phase-offband-prefix-gap-shadow-short-b-cell-factor-cover-ledger.json": sha256(
                input_ledger
            ),
            "data/square-phase-offband-prefix-gap-shadow-crt-cover-word-ledger.json": sha256(OUT_LEDGER),
        },
        "plain_conclusion": (
            "本步把完整短覆盖进一步正规化为 CRT 覆盖词。若 selected cell 从 b=B 开始、长度为 L，"
            "完整 void 需要标签 ell_t 使 q_start=P-2B 满足 q_start≡2t (mod ell_t)。"
            "长度至多 5 时，覆盖词至少需要 L 个不同标签（L<=3）或 L-1 个不同标签（L>=4），"
            "对应最小模数下界在当前前沿为 15..1155。CRT 兼容本身不矛盾；最新剩余是排斥这些"
            "兼容覆盖词与固定 small-k 相位/列相位同时持久对齐。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow CRT cover word router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"record_count={agg['record_count']}",
        f"complete_crt_cover_word_actual_count={agg['complete_crt_cover_word_actual_count']}",
        f"missing_new_label_count_lower_bound_range={agg['min_missing_new_label_count_lower_bound']}..{agg['max_missing_new_label_count_lower_bound']}",
        f"complete_word_crt_modulus_lower_bound_range={agg['min_complete_word_crt_modulus_lower_bound']}..{agg['max_complete_word_crt_modulus_lower_bound']}",
        f"max_cell_length={agg['max_cell_length']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. CRT 覆盖词",
        "",
        "令 selected cell 的起点为 `B=b_lo`，长度为 `L`，并写 `q_start=P-2B`。完整覆盖词是：",
        "",
        "```text",
        "for t=0..L-1, choose odd prime ell_t <= sqrt(P)",
        "q_start - 2t ≡ 0 (mod ell_t)",
        "equivalently q_start ≡ 2t (mod ell_t)",
        "```",
        "",
        "同一标签复用时必须满足 `ell | (t_i-t_j)`；在 `L<=5` 内只有 `ell=3` 可隔 3 复用一次。",
        "",
        "## 2. 前沿词",
        "",
        "| P | side | b cell | q cell | missing labels >= | min full modulus | partial labels |",
        "| ---: | --- | --- | --- | ---: | ---: | --- |",
    ]
    for row in result["crt_word_records"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["p"]),
                    f"`{row['side']}`",
                    f"`{row['b_lo']}-{row['b_hi']}`",
                    f"`{row['selected_q_lo']}-{row['selected_q_hi']}`",
                    f"`{row['missing_new_label_count_lower_bound']}`",
                    f"`{row['min_complete_word_crt_modulus_lower_bound']}`",
                    f"`{row['actual_least_label_set']}`",
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
            "- 需要证明兼容 CRT 覆盖词不能同时落入固定 small-k atom phase，或把它提升为 ColumnCRT/PDEC 证书。",
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
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-crt-cover-word-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "complete_crt_cover_word_actual_count": result["complete_crt_cover_word_actual_count"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
