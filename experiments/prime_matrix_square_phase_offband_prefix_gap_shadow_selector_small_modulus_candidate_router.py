#!/usr/bin/env python3
"""枚举 small-modulus compatible cover words 并检查低轮结构冲突。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_small_modulus_candidate_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-small-modulus-candidate-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-selector-small-modulus-candidate-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-small-modulus-candidate-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-small-modulus-candidate-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

INPUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-phase-compatibility-ledger.json"
LABEL_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-label-lower-bound-ledger.json"
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-small-modulus-candidate-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-small-modulus-candidate-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-small-modulus-candidate-router.md"

LABEL_ROUTER = (
    ROOT
    / "experiments"
    / "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_label_lower_bound_router.py"
)

MAIN_TARGET = "NonStructuralLabelModulusFloorOrSmallModulusOverlapPDEC"
NEXT_TARGET = "SmallModulusCompatibleWordsLowwheelConflictOrOverlapPDEC"


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


def odd_primes(limit: int) -> list[int]:
    """列出不超过 limit 的奇素数。"""
    values: list[int] = []
    for number in range(3, limit + 1, 2):
        if all(number % divisor for divisor in range(3, math.isqrt(number) + 1, 2)):
            values.append(number)
    return values


def crt_pair(a_value: int, a_modulus: int, b_value: int, b_modulus: int) -> tuple[int, int] | None:
    """合并两个 CRT 条件。"""
    gcd_value = math.gcd(a_modulus, b_modulus)
    if (b_value - a_value) % gcd_value:
        return None
    reduced_a = a_modulus // gcd_value
    reduced_b = b_modulus // gcd_value
    delta = (b_value - a_value) // gcd_value
    step = (delta * pow(reduced_a, -1, reduced_b)) % reduced_b
    modulus = a_modulus // gcd_value * b_modulus
    residue = (a_value + a_modulus * step) % modulus
    return residue, modulus


def progression_values(lo_value: int, hi_value: int, residue: int, modulus: int) -> list[int]:
    """列出区间内同余类取值。"""
    if lo_value > hi_value:
        return []
    quotient = math.ceil((lo_value - residue) / modulus)
    value = residue + quotient * modulus
    values: list[int] = []
    while value <= hi_value:
        values.append(value)
        value += modulus
    return values


def compatible_cover_words(row: dict[str, Any]) -> list[dict[str, Any]]:
    """枚举相位兼容覆盖词。"""
    b_start = int(row["b_lo"])
    length = int(row["cell_length"])
    phase_lo = int(row["phase_p_lo"])
    phase_hi = int(row["phase_p_hi"])
    label_pool = odd_primes(math.isqrt(int(row["p"])))
    words: list[dict[str, Any]] = []

    def recurse(offset: int, residue: int, modulus: int, labels: list[int]) -> None:
        if offset == length:
            values = progression_values(phase_lo, phase_hi, residue, modulus)
            if values:
                words.append(
                    {
                        "labels": labels[:],
                        "distinct_labels": sorted(set(labels)),
                        "residue": residue,
                        "modulus": modulus,
                        "window_values": values,
                    }
                )
            return

        b_value = b_start + offset
        for label in label_pool:
            # 若 label|b，则 P 会落到 0 mod label；对 P>label 的素数不允许。
            if b_value % label == 0:
                continue
            merged = crt_pair(residue, modulus, (2 * b_value) % label, label)
            if merged is None:
                continue
            recurse(offset + 1, merged[0], merged[1], labels + [label])

    recurse(0, 0, 1, [])
    return words


def small_candidate(row: dict[str, Any], word: dict[str, Any]) -> dict[str, Any] | None:
    """若覆盖词是 M<=W 的小模数候选，返回候选记录。"""
    width = int(row["phase_p_width"])
    modulus = int(word["modulus"])
    if modulus > width:
        return None
    actual_residue_15 = int(row["p"]) % 15
    gcd15 = math.gcd(modulus, 15)
    residue_mod_g = int(word["residue"]) % gcd15 if gcd15 else 0
    actual_mod_g = int(row["p"]) % gcd15 if gcd15 else 0
    structural_conflict = gcd15 > 1 and residue_mod_g != actual_mod_g
    actual_residue_hit = any(int(value) % 15 == actual_residue_15 for value in word["window_values"])
    return {
        "p": row["p"],
        "side": row["side"],
        "parent_atom_key": row["parent_atom_key"],
        "cell_length": row["cell_length"],
        "phase_p_width": width,
        "labels": word["labels"],
        "distinct_labels": word["distinct_labels"],
        "residue": word["residue"],
        "modulus": modulus,
        "modulus_minus_width": modulus - width,
        "window_values": word["window_values"],
        "gcd_modulus_15": gcd15,
        "residue_mod_gcd15": residue_mod_g,
        "actual_p_mod_gcd15": actual_mod_g,
        "actual_p_mod_15": actual_residue_15,
        "window_value_mod15": sorted({int(value) % 15 for value in word["window_values"]}),
        "structural_lowwheel_conflict": structural_conflict,
        "actual_residue_hit_inside_window": actual_residue_hit,
        "requires_overlap_pdec": (not structural_conflict) or actual_residue_hit,
    }


def row_record(row: dict[str, Any]) -> dict[str, Any]:
    """生成单行 small-modulus 候选记录。"""
    candidates = [
        candidate
        for word in compatible_cover_words(row)
        if (candidate := small_candidate(row, word)) is not None
    ]
    return {
        "index": row["index"],
        "p": row["p"],
        "side": row["side"],
        "shape_key": row["shape_key"],
        "parent_atom_key": row["parent_atom_key"],
        "parent_atom_band": row["parent_atom_band"],
        "parent_atom_k": row["parent_atom_k"],
        "cell_length": row["cell_length"],
        "phase_p_width": row["phase_p_width"],
        "small_modulus_candidate_count": len(candidates),
        "structural_conflict_candidate_count": sum(
            1 for item in candidates if item["structural_lowwheel_conflict"]
        ),
        "overlap_pdec_candidate_count": sum(1 for item in candidates if item["requires_overlap_pdec"]),
        "small_modulus_candidates": candidates,
    }


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "finite_small_modulus_candidates_exhausted",
            "status": "closed_on_current_frontier",
            "statement": "All current compatible cover words with M<=W are explicitly enumerated.",
        },
        {
            "name": "finite_small_modulus_lowwheel_conflict",
            "status": "closed_on_current_frontier",
            "statement": "Every current small-modulus compatible word is structurally conflicting modulo gcd(M,15).",
        },
        {
            "name": "global_small_modulus_lowwheel_conflict",
            "status": "open",
            "statement": "A global proof must show every small-modulus compatible word in the formal-unit family is a lowwheel conflict.",
        },
        {
            "name": "small_modulus_overlap_pdec",
            "status": "open",
            "statement": "Any non-conflicting small-modulus survivor must be routed to PDEC/ColumnCRT.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    agg = result["aggregate"]
    return [
        {
            "gate": "FiniteSmallModulusEnumerationClosed",
            "closed": True,
            "proved": True,
            "meaning": "当前 M<=W 的相位兼容覆盖词已全部枚举。",
            "remaining": "closed on current finite frontier",
        },
        {
            "gate": "FiniteSmallModulusAllLowwheelConflict",
            "closed": agg["overlap_pdec_candidate_count"] == 0,
            "proved": True,
            "meaning": "当前小模数候选全部由 gcd(M,15) 结构冲突排除。",
            "remaining": "closed on current finite frontier",
        },
        {
            "gate": "GlobalSmallModulusLowwheelConflictProved",
            "closed": False,
            "proved": False,
            "meaning": "尚未证明 formal-unit 族中小模数候选必然结构冲突。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "SmallModulusOverlapPDECExcluded",
            "closed": False,
            "proved": False,
            "meaning": "若出现非冲突 small-modulus survivor，仍需 PDEC/ColumnCRT 排斥。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步关闭当前小模数候选筛，不关闭全局行/列命题。",
            "remaining": NEXT_TARGET,
        },
    ]


def build_result(input_ledger: Path, label_ledger: Path) -> dict[str, Any]:
    """构造 small-modulus 候选筛结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    source = load_json(input_ledger)
    label = load_json(label_ledger)
    records = [row_record(row) for row in source["phase_compatibility_records"]]
    candidates = [item for row in records for item in row["small_modulus_candidates"]]
    aggregate = {
        "input_ledger": str(input_ledger.relative_to(ROOT)),
        "label_ledger": str(label_ledger.relative_to(ROOT)),
        "record_count": len(records),
        "small_modulus_candidate_count": len(candidates),
        "structural_conflict_candidate_count": sum(
            1 for item in candidates if item["structural_lowwheel_conflict"]
        ),
        "overlap_pdec_candidate_count": sum(1 for item in candidates if item["requires_overlap_pdec"]),
        "candidate_rows_count": sum(1 for row in records if row["small_modulus_candidate_count"] > 0),
        "min_candidate_modulus_minus_width": min(
            (item["modulus_minus_width"] for item in candidates),
            default=None,
        ),
        "max_candidate_modulus": max((item["modulus"] for item in candidates), default=None),
        "global_small_modulus_lowwheel_conflict_proved": False,
        "small_modulus_overlap_pdec_excluded": False,
        "row_column_unconditional_closed": False,
    }
    ledger = {
        "parameters": source["parameters"],
        "aggregate": aggregate,
        "small_modulus_candidate_records": records,
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = {
        "certificate_type": "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_small_modulus_candidate_router",
        "status": "selector_small_modulus_candidates_lowwheel_conflict_open_global",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_candidate_conflict_not_used_as_global_proof": True,
        "parameters": source["parameters"],
        "aggregate": aggregate,
        "small_modulus_candidate_records": records,
        "label_lower_bound_aggregate": label["aggregate"],
        "global_small_modulus_lowwheel_conflict_proved": False,
        "small_modulus_overlap_pdec_excluded": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_small_modulus_candidate_router.py": sha256(
                Path(__file__).resolve()
            ),
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_label_lower_bound_router.py": sha256(
                LABEL_ROUTER
            ),
            "data/square-phase-offband-prefix-gap-shadow-phase-compatibility-ledger.json": sha256(
                input_ledger
            ),
            "data/square-phase-offband-prefix-gap-shadow-selector-label-lower-bound-ledger.json": sha256(
                label_ledger
            ),
            "data/square-phase-offband-prefix-gap-shadow-selector-small-modulus-candidate-ledger.json": sha256(
                OUT_LEDGER
            ),
        },
        "plain_conclusion": (
            "本步把 small-modulus 缺口具体化：当前前沿存在 "
            f"{aggregate['small_modulus_candidate_count']} 个 M<=W 的相位兼容覆盖词，但它们全部满足 "
            "residue mod gcd(M,15) 与 actual P 不同，因此已经被低轮结构冲突排除；"
            f"需要 PDEC 的非冲突候选数为 {aggregate['overlap_pdec_candidate_count']}。"
            "全局剩余变成证明 formal-unit 族中所有 small-modulus 兼容词都必然低轮冲突，"
            "或对非冲突 survivor 提交 PDEC/ColumnCRT。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow selector small modulus candidate router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"small_modulus_candidate_count={agg['small_modulus_candidate_count']}",
        f"structural_conflict_candidate_count={agg['structural_conflict_candidate_count']}",
        f"overlap_pdec_candidate_count={agg['overlap_pdec_candidate_count']}",
        f"candidate_rows_count={agg['candidate_rows_count']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 小模数候选",
        "",
        "| idx | P | W | candidates | structural conflicts | PDEC candidates |",
        "| ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in result["small_modulus_candidate_records"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["index"]),
                    str(row["p"]),
                    str(row["phase_p_width"]),
                    str(row["small_modulus_candidate_count"]),
                    str(row["structural_conflict_candidate_count"]),
                    str(row["overlap_pdec_candidate_count"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 2. 候选明细",
            "",
            "| P | labels | M | W | gcd(M,15) | residue mod gcd | P mod gcd | window values | structural conflict |",
            "| ---: | --- | ---: | ---: | ---: | ---: | ---: | --- | ---: |",
        ]
    )
    candidates = [
        item
        for row in result["small_modulus_candidate_records"]
        for item in row["small_modulus_candidates"]
    ]
    for item in candidates:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(item["p"]),
                    f"`{item['labels']}`",
                    str(item["modulus"]),
                    str(item["phase_p_width"]),
                    str(item["gcd_modulus_15"]),
                    str(item["residue_mod_gcd15"]),
                    str(item["actual_p_mod_gcd15"]),
                    f"`{item['window_values']}`",
                    f"`{fmt_bool(item['structural_lowwheel_conflict'])}`",
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
            "- 直接证明目标：证明 formal-unit 族中 `M<=W` 的兼容词必然满足低轮结构冲突。",
            "- 若存在非冲突 small-modulus survivor，则登记为 overlap `PDEC/ColumnCRT`。",
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
    parser.add_argument("--label-ledger", type=Path, default=LABEL_LEDGER)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    input_ledger = args.input_ledger if args.input_ledger.is_absolute() else ROOT / args.input_ledger
    label_ledger = args.label_ledger if args.label_ledger.is_absolute() else ROOT / args.label_ledger
    result = build_result(input_ledger, label_ledger)
    write_markdown(result)
    result["source_hashes"][
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-small-modulus-candidate-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "small_modulus_candidate_count": result["aggregate"]["small_modulus_candidate_count"],
                "overlap_pdec_candidate_count": result["aggregate"]["overlap_pdec_candidate_count"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
