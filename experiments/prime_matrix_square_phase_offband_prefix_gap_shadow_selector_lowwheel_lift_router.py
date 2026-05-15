#!/usr/bin/env python3
"""拆分 Q=15 selector 分离的结构来源与窗口截断来源。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_lowwheel_lift_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-lowwheel-lift-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-selector-lowwheel-lift-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-lowwheel-lift-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-lowwheel-lift-router.md
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
LOWWHEEL_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-lowwheel-ledger.json"
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-lowwheel-lift-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-lowwheel-lift-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-lowwheel-lift-router.md"

LOWWHEEL_ROUTER = (
    ROOT
    / "experiments"
    / "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_lowwheel_router.py"
)
PHASE_ROUTER = (
    ROOT
    / "experiments"
    / "prime_matrix_square_phase_offband_prefix_gap_shadow_phase_compatibility_router.py"
)

MAIN_TARGET = "FormalUnitSelectorLowWheel15LiftOrPersistentHitPDEC"
NEXT_TARGET = "LowWheel15PhaseWindowMissLiftOrPersistentHitPDEC"


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
    """重新枚举相位兼容覆盖词并保留窗口样本。"""
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


def classify_word(row: dict[str, Any], word: dict[str, Any]) -> dict[str, Any]:
    """分类单个覆盖词的 Q=15 排斥来源。"""
    actual_p = int(row["p"])
    actual_residue = actual_p % 15
    gcd15 = math.gcd(int(word["modulus"]), 15)
    structural_conflict = gcd15 > 1 and actual_p % gcd15 != int(word["residue"]) % gcd15
    window_values = [int(value) for value in word["window_values"]]
    window_q15_separated = all(value % 15 != actual_residue for value in window_values)
    return {
        **word,
        "gcd_modulus_15": gcd15,
        "actual_p_mod_15": actual_residue,
        "residue_mod_15": int(word["residue"]) % 15,
        "structural_lowwheel_conflict": structural_conflict,
        "window_q15_separated": window_q15_separated,
        "needs_phase_window_miss_lift": window_q15_separated and not structural_conflict,
    }


def lift_record(row: dict[str, Any]) -> dict[str, Any]:
    """生成单包 Q=15 lift 拆分记录。"""
    words = [classify_word(row, word) for word in compatible_cover_words(row)]
    gcd_histogram: dict[str, int] = {}
    for word in words:
        key = str(word["gcd_modulus_15"])
        gcd_histogram[key] = gcd_histogram.get(key, 0) + 1
    structural_words = [word for word in words if word["structural_lowwheel_conflict"]]
    window_miss_words = [word for word in words if word["needs_phase_window_miss_lift"]]
    leakage_words = [
        word
        for word in words
        if not word["structural_lowwheel_conflict"] and not word["window_q15_separated"]
    ]
    return {
        "index": row["index"],
        "p": row["p"],
        "side": row["side"],
        "shape_key": row["shape_key"],
        "parent_atom_key": row["parent_atom_key"],
        "b_lo": row["b_lo"],
        "b_hi": row["b_hi"],
        "cell_length": row["cell_length"],
        "phase_p_lo": row["phase_p_lo"],
        "phase_p_hi": row["phase_p_hi"],
        "phase_p_width": row["phase_p_width"],
        "actual_p_mod_15": int(row["p"]) % 15,
        "phase_compatible_cover_word_count": len(words),
        "structural_lowwheel_conflict_word_count": len(structural_words),
        "phase_window_miss_word_count": len(window_miss_words),
        "q15_leakage_word_count": len(leakage_words),
        "gcd_modulus_15_histogram": dict(sorted(gcd_histogram.items())),
        "pure_crt_lowwheel_lift_closed_for_packet": len(window_miss_words) == 0 and not leakage_words,
        "all_compatible_words_q15_separated_in_window": not leakage_words,
        "window_miss_examples": [
            {
                "labels": word["labels"],
                "residue": word["residue"],
                "modulus": word["modulus"],
                "gcd_modulus_15": word["gcd_modulus_15"],
                "residue_mod_15": word["residue_mod_15"],
                "window_values": word["window_values"],
            }
            for word in window_miss_words[:3]
        ],
    }


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "q15_finite_separator_decomposition",
            "status": "closed_on_current_frontier",
            "statement": "Every compatible cover word is either structurally lowwheel-conflicting or phase-window-missing modulo 15.",
        },
        {
            "name": "pure_crt_label_lowwheel_lift",
            "status": "rejected",
            "statement": "The Q=15 separator is not explained solely by label-word CRT conflicts; window-miss words occur in every packet.",
        },
        {
            "name": "phase_window_miss_lift",
            "status": "open",
            "statement": "The remaining lift must prove that non-conflicting cover words miss the actual selector residue inside the fixed phase window.",
        },
        {
            "name": "persistent_q15_overlap_pdec",
            "status": "open",
            "statement": "If a non-conflicting word hits the actual residue in a persistent family, it must be routed to PDEC/ColumnCRT.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    agg = result["aggregate"]
    return [
        {
            "gate": "FiniteQ15DecompositionClosed",
            "closed": agg["q15_leakage_word_count"] == 0,
            "proved": True,
            "meaning": "当前前沿无 Q=15 窗口泄漏；每个覆盖词均被结构冲突或窗口错位解释。",
            "remaining": "closed on current finite frontier",
        },
        {
            "gate": "PureCRTLowWheelLiftClosed",
            "closed": agg["phase_window_miss_word_count"] == 0,
            "proved": False,
            "meaning": "存在窗口错位词，不能声称 Q=15 分离已由覆盖词 CRT 标签自动全局推出。",
            "remaining": "rejected",
        },
        {
            "gate": "PhaseWindowMissLiftProved",
            "closed": False,
            "proved": False,
            "meaning": "仍需对窗口错位词证明 actual selector residue 永远不落窗。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "PersistentQ15OverlapPDECExcluded",
            "closed": False,
            "proved": False,
            "meaning": "若窗口错位 lift 失败，则需对持久 Q=15 重叠提交 PDEC/ColumnCRT。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步继续缩窄 selector 剩余，不关闭全局行/列命题。",
            "remaining": NEXT_TARGET,
        },
    ]


def build_result(input_ledger: Path, lowwheel_ledger: Path) -> dict[str, Any]:
    """构造 Q=15 lift 拆分结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    source = load_json(input_ledger)
    lowwheel = load_json(lowwheel_ledger)
    records = [lift_record(row) for row in source["phase_compatibility_records"]]
    aggregate = {
        "input_ledger": str(input_ledger.relative_to(ROOT)),
        "lowwheel_ledger": str(lowwheel_ledger.relative_to(ROOT)),
        "record_count": len(records),
        "total_phase_compatible_cover_word_count": sum(
            row["phase_compatible_cover_word_count"] for row in records
        ),
        "structural_lowwheel_conflict_word_count": sum(
            row["structural_lowwheel_conflict_word_count"] for row in records
        ),
        "phase_window_miss_word_count": sum(row["phase_window_miss_word_count"] for row in records),
        "q15_leakage_word_count": sum(row["q15_leakage_word_count"] for row in records),
        "packets_requiring_phase_window_miss_lift": sum(
            1 for row in records if row["phase_window_miss_word_count"] > 0
        ),
        "pure_crt_lowwheel_lift_closed": all(
            row["pure_crt_lowwheel_lift_closed_for_packet"] for row in records
        ),
        "all_compatible_words_q15_separated_in_window": all(
            row["all_compatible_words_q15_separated_in_window"] for row in records
        ),
        "q15_formal_unit_lift_proved": False,
        "persistent_hit_pdec_excluded": False,
        "row_column_unconditional_closed": False,
    }
    ledger = {
        "parameters": source["parameters"],
        "aggregate": aggregate,
        "selector_lowwheel_lift_records": records,
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = {
        "certificate_type": "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_lowwheel_lift_router",
        "status": "selector_lowwheel15_lift_split_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_decomposition_not_used_as_global_proof": True,
        "parameters": source["parameters"],
        "aggregate": aggregate,
        "selector_lowwheel_lift_records": records,
        "lowwheel_selector_aggregate": lowwheel["aggregate"],
        "q15_formal_unit_lift_proved": False,
        "persistent_hit_pdec_excluded": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_lowwheel_lift_router.py": sha256(
                Path(__file__).resolve()
            ),
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_lowwheel_router.py": sha256(
                LOWWHEEL_ROUTER
            ),
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_phase_compatibility_router.py": sha256(
                PHASE_ROUTER
            ),
            "data/square-phase-offband-prefix-gap-shadow-phase-compatibility-ledger.json": sha256(
                input_ledger
            ),
            "data/square-phase-offband-prefix-gap-shadow-selector-lowwheel-ledger.json": sha256(
                lowwheel_ledger
            ),
            "data/square-phase-offband-prefix-gap-shadow-selector-lowwheel-lift-ledger.json": sha256(
                OUT_LEDGER
            ),
        },
        "plain_conclusion": (
            "本步把 Q=15 selector 分离拆成两类来源：覆盖词 CRT 模数在 gcd(modulus,15) 上"
            "已经与 actual P 冲突的结构低轮冲突，以及覆盖词本身不冲突、但在 fixed phase 窗口内"
            "只落到非 actual mod 15 残基的相位窗口错位。当前前沿没有 Q=15 泄漏，但窗口错位词"
            "在每个包中都存在，所以不能把低轮分离直接声称为纯 CRT 标签定理；真正剩余被压成 "
            "PhaseWindowMiss lift，或 persistent Q=15 overlap 的 PDEC/ColumnCRT 证书。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow selector lowwheel lift router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"record_count={agg['record_count']}",
        f"total_phase_compatible_cover_word_count={agg['total_phase_compatible_cover_word_count']}",
        f"structural_lowwheel_conflict_word_count={agg['structural_lowwheel_conflict_word_count']}",
        f"phase_window_miss_word_count={agg['phase_window_miss_word_count']}",
        f"q15_leakage_word_count={agg['q15_leakage_word_count']}",
        f"packets_requiring_phase_window_miss_lift={agg['packets_requiring_phase_window_miss_lift']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 拆分结论",
        "",
        "当前 `Q=15` 分离不是纯标签 CRT 冲突。若覆盖词模数与 `15` 的公共因子已经排斥 actual `P`，则进入 structural conflict；否则必须依赖 fixed phase 窗口没有取到 actual `P mod 15` 的窗口错位。",
        "",
        "## 2. 前沿记录",
        "",
        "| idx | P | side | words | structural | window miss | q15 leak | gcd(mod,15) histogram |",
        "| ---: | ---: | --- | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in result["selector_lowwheel_lift_records"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["index"]),
                    str(row["p"]),
                    f"`{row['side']}`",
                    str(row["phase_compatible_cover_word_count"]),
                    str(row["structural_lowwheel_conflict_word_count"]),
                    str(row["phase_window_miss_word_count"]),
                    str(row["q15_leakage_word_count"]),
                    f"`{row['gcd_modulus_15_histogram']}`",
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 3. 窗口错位样例",
            "",
            "| idx | P | examples |",
            "| ---: | ---: | --- |",
        ]
    )
    for row in result["selector_lowwheel_lift_records"]:
        examples = [
            {
                "labels": item["labels"],
                "g": item["gcd_modulus_15"],
                "res15": item["residue_mod_15"],
                "values": item["window_values"],
            }
            for item in row["window_miss_examples"]
        ]
        lines.append(f"| {row['index']} | {row['p']} | `{table_cell(examples)}` |")
    lines.extend(
        [
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
            "- 直接证明目标：对 non-structural cover words 证明 fixed phase 窗口中的同余进程永远错开 actual `P mod 15`。",
            "- 若窗口错位不能全局证明，则把实际重叠族登记为 persistent `Q=15` overlap 的 PDEC/ColumnCRT 证书。",
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
    parser.add_argument("--lowwheel-ledger", type=Path, default=LOWWHEEL_LEDGER)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    input_ledger = args.input_ledger if args.input_ledger.is_absolute() else ROOT / args.input_ledger
    lowwheel_ledger = (
        args.lowwheel_ledger if args.lowwheel_ledger.is_absolute() else ROOT / args.lowwheel_ledger
    )
    result = build_result(input_ledger, lowwheel_ledger)
    write_markdown(result)
    result["source_hashes"][
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-lowwheel-lift-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "total_phase_compatible_cover_word_count": result["aggregate"][
                    "total_phase_compatible_cover_word_count"
                ],
                "structural_lowwheel_conflict_word_count": result["aggregate"][
                    "structural_lowwheel_conflict_word_count"
                ],
                "phase_window_miss_word_count": result["aggregate"]["phase_window_miss_word_count"],
                "q15_leakage_word_count": result["aggregate"]["q15_leakage_word_count"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
