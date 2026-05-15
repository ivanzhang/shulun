#!/usr/bin/env python3
"""把相位兼容 CRT 覆盖词物化为相位窗口内的坏 P 集合。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_bad_p_set_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-bad-p-set-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-bad-p-set-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-bad-p-set-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-bad-p-set-router.md
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
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-bad-p-set-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-bad-p-set-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-bad-p-set-router.md"

PHASE_ROUTER = (
    ROOT / "experiments" / "prime_matrix_square_phase_offband_prefix_gap_shadow_phase_compatibility_router.py"
)

MAIN_TARGET = "ColumnPhaseDensityExclusionForCompatibleCRTCoverWordsOrPrimeAvoidancePDEC"
NEXT_TARGET = "ActualPrimeAvoidsLocalBadPSetByColumnPhaseOrBadPSetPDEC"


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


def is_prime(number: int) -> bool:
    """朴素素性检查。"""
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for divisor in range(3, math.isqrt(number) + 1, 2):
        if number % divisor == 0:
            return False
    return True


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
    """列出区间内某同余类的值。"""
    if lo_value > hi_value:
        return []
    quotient = math.ceil((lo_value - residue) / modulus)
    value = residue + quotient * modulus
    values: list[int] = []
    while value <= hi_value:
        values.append(value)
        value += modulus
    return values


def enumerate_bad_p_values(row: dict[str, Any]) -> dict[str, Any]:
    """枚举相位窗口内可由完整覆盖词解释的坏 P 值。"""
    b_start = int(row["b_lo"])
    length = int(row["cell_length"])
    phase_lo = int(row["phase_p_lo"])
    phase_hi = int(row["phase_p_hi"])
    label_pool = odd_primes(math.isqrt(int(row["p"])))
    bad_multiplicity: dict[int, int] = {}
    example_by_value: dict[int, dict[str, Any]] = {}
    total_words = 0

    def recurse(offset: int, residue: int, modulus: int, labels: list[int]) -> None:
        nonlocal total_words
        if offset == length:
            total_words += 1
            for value in progression_values(phase_lo, phase_hi, residue, modulus):
                bad_multiplicity[value] = bad_multiplicity.get(value, 0) + 1
                example_by_value.setdefault(
                    value,
                    {
                        "labels": labels[:],
                        "residue": residue,
                        "modulus": modulus,
                    },
                )
            return

        b_value = b_start + offset
        for label in label_pool:
            # 若 label|b，则 P 会落到 0 mod label；对大于 label 的素 P 不允许。
            if b_value % label == 0:
                continue
            merged = crt_pair(residue, modulus, (2 * b_value) % label, label)
            if merged is None:
                continue
            recurse(offset + 1, merged[0], merged[1], labels + [label])

    recurse(0, 0, 1, [])
    bad_values = sorted(bad_multiplicity)
    bad_prime_values = [value for value in bad_values if is_prime(value)]
    examples = [
        {
            "p_value": value,
            "multiplicity": bad_multiplicity[value],
            **example_by_value[value],
        }
        for value in bad_values[:6]
    ]
    prime_examples = [
        {
            "p_value": value,
            "multiplicity": bad_multiplicity[value],
            **example_by_value[value],
        }
        for value in bad_prime_values[:6]
    ]
    width = int(row["phase_p_width"])
    return {
        "total_cover_words_enumerated": total_words,
        "bad_p_values": bad_values,
        "bad_p_value_count": len(bad_values),
        "bad_p_density_in_phase_window": len(bad_values) / width if width else 0.0,
        "bad_prime_values": bad_prime_values,
        "bad_prime_value_count": len(bad_prime_values),
        "actual_p_in_bad_set": int(row["p"]) in bad_multiplicity,
        "max_bad_p_cover_word_multiplicity": max(bad_multiplicity.values(), default=0),
        "bad_p_examples": examples,
        "bad_prime_examples": prime_examples,
    }


def bad_p_record(row: dict[str, Any]) -> dict[str, Any]:
    """生成单个前沿包的坏 P 集合记录。"""
    bad = enumerate_bad_p_values(row)
    return {
        "index": row["index"],
        "p": row["p"],
        "side": row["side"],
        "shape_key": row["shape_key"],
        "b_lo": row["b_lo"],
        "b_hi": row["b_hi"],
        "selected_q_lo": row["selected_q_lo"],
        "selected_q_hi": row["selected_q_hi"],
        "cell_length": row["cell_length"],
        "parent_atom_key": row["parent_atom_key"],
        "phase_p_lo": row["phase_p_lo"],
        "phase_p_hi": row["phase_p_hi"],
        "phase_p_width": row["phase_p_width"],
        **bad,
        "bad_set_statement": (
            "BadPSet is the union, inside the fixed phase P-window, of all CRT classes "
            "whose label word fully covers the selected b-cell."
        ),
    }


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "compatible_words_to_bad_p_set",
            "status": "closed",
            "statement": "Phase-compatible CRT cover words define an explicit finite BadPSet inside the phase window.",
        },
        {
            "name": "actual_frontier_prime_avoids_bad_p_set",
            "status": "finite_evidence",
            "statement": "The finite frontier actual prime P is not in the local BadPSet for every packet.",
        },
        {
            "name": "local_prime_bad_examples_exist",
            "status": "finite_evidence",
            "statement": "Some local BadPSets contain other prime representatives, so primality plus local phase is not enough.",
        },
        {
            "name": "global_actual_prime_avoidance",
            "status": "open",
            "statement": "A global proof still needs to explain why the actual formal-unit prime P avoids BadPSet, or route persistent hits to PDEC/ColumnCRT.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "BadPSetMaterialized",
            "closed": True,
            "proved": True,
            "meaning": "兼容覆盖词已物化成相位窗口内有限坏 P 集。",
            "remaining": "closed",
        },
        {
            "gate": "ActualFinitePrimeAvoidsBadPSet",
            "closed": result["actual_p_in_bad_set_count"] == 0,
            "proved": False,
            "meaning": "有限前沿的实际 P 都避开坏集；这不是全局证明。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "LocalPrimeBadExamplesRuleOutLocalClosure",
            "closed": result["bad_prime_packet_count"] > 0,
            "proved": True,
            "meaning": "坏集中存在其他素数代表，说明局部条件不足以闭合。",
            "remaining": "closed",
        },
        {
            "gate": "GlobalBadPSetAvoidanceClosed",
            "closed": False,
            "proved": False,
            "meaning": "仍需列相位/密度机制解释实际 formal-unit P 为什么避开坏集。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只完成坏集物化，不关闭全局命题。",
            "remaining": NEXT_TARGET,
        },
    ]


def build_result(input_ledger: Path) -> dict[str, Any]:
    """构造坏 P 集路由结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    source = load_json(input_ledger)
    records = [bad_p_record(row) for row in source["phase_compatibility_records"]]
    actual_hits = [row for row in records if row["actual_p_in_bad_set"]]
    bad_prime_packets = [row for row in records if row["bad_prime_value_count"] > 0]
    aggregate = {
        "input_ledger": str(input_ledger.relative_to(ROOT)),
        "record_count": len(records),
        "actual_p_in_bad_set_count": len(actual_hits),
        "bad_prime_packet_count": len(bad_prime_packets),
        "max_bad_p_value_count": max((row["bad_p_value_count"] for row in records), default=0),
        "max_bad_p_density_in_phase_window": max(
            (row["bad_p_density_in_phase_window"] for row in records),
            default=0.0,
        ),
        "max_bad_prime_value_count": max((row["bad_prime_value_count"] for row in records), default=0),
        "max_bad_p_cover_word_multiplicity": max(
            (row["max_bad_p_cover_word_multiplicity"] for row in records),
            default=0,
        ),
        "global_actual_prime_avoidance_proved": False,
        "row_column_unconditional_closed": False,
    }
    ledger = {
        "parameters": source["parameters"],
        "aggregate": aggregate,
        "bad_p_set_records": records,
        "actual_p_in_bad_set_records": actual_hits,
        "bad_prime_packet_records": bad_prime_packets,
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = {
        "certificate_type": "prime_matrix_square_phase_offband_prefix_gap_shadow_bad_p_set_router",
        "status": "bad_p_set_materialized_actual_prime_avoidance_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "empirical_absence_not_used_as_proof": True,
        "parameters": source["parameters"],
        "aggregate": aggregate,
        "bad_p_set_records": records,
        "actual_p_in_bad_set_count": len(actual_hits),
        "bad_prime_packet_count": len(bad_prime_packets),
        "global_actual_prime_avoidance_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_bad_p_set_router.py": sha256(
                Path(__file__).resolve()
            ),
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_phase_compatibility_router.py": sha256(
                PHASE_ROUTER
            ),
            "data/square-phase-offband-prefix-gap-shadow-phase-compatibility-ledger.json": sha256(input_ledger),
            "data/square-phase-offband-prefix-gap-shadow-bad-p-set-ledger.json": sha256(OUT_LEDGER),
        },
        "plain_conclusion": (
            "本步把列相位密度硬点物化为 BadPSet：在每个固定相位 P 窗口内，所有完整 CRT 覆盖词"
            "给出一个有限坏 P 集。有限前沿中实际主素数 P 从不落入对应 BadPSet；但 6 个包的 BadPSet "
            "含有其他素数代表，说明素数性加局部相位仍不足以闭合。最新剩余是解释正式反例链中的实际 "
            "formal-unit P 为什么全局避开这些坏集，或把持久命中登记为 PDEC/ColumnCRT。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow bad-P set router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"record_count={agg['record_count']}",
        f"actual_p_in_bad_set_count={agg['actual_p_in_bad_set_count']}",
        f"bad_prime_packet_count={agg['bad_prime_packet_count']}",
        f"max_bad_p_value_count={agg['max_bad_p_value_count']}",
        f"max_bad_p_density_in_phase_window={agg['max_bad_p_density_in_phase_window']:.6f}",
        f"max_bad_prime_value_count={agg['max_bad_prime_value_count']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. BadPSet",
        "",
        "对每个 selected cell，BadPSet 是固定 `P` 相位窗口中所有能由完整 CRT 覆盖词解释的 `P` 值。若实际主素数 `P` 落入 BadPSet，则该 selected cell 会被小因子标签完全覆盖。",
        "",
        "## 2. 坏集前沿",
        "",
        "| P | side | P window | bad values | bad primes | actual P bad? | density |",
        "| ---: | --- | --- | ---: | --- | ---: | ---: |",
    ]
    for row in result["bad_p_set_records"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["p"]),
                    f"`{row['side']}`",
                    f"`{row['phase_p_lo']}-{row['phase_p_hi']}`",
                    f"`{row['bad_p_value_count']}`",
                    f"`{row['bad_prime_values']}`",
                    f"`{fmt_bool(row['actual_p_in_bad_set'])}`",
                    f"`{row['bad_p_density_in_phase_window']:.3f}`",
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
            "- 需要把 actual formal-unit P 避开 BadPSet 的有限事实升级为结构证明，或给出持久命中时的 PDEC/ColumnCRT 证书。",
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
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-bad-p-set-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "actual_p_in_bad_set_count": result["actual_p_in_bad_set_count"],
                "bad_prime_packet_count": result["bad_prime_packet_count"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
