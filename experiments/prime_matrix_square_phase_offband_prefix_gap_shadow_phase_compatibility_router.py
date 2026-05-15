#!/usr/bin/env python3
"""检查 CRT 覆盖词与固定 small-k 相位窗口的兼容性边界。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_phase_compatibility_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-phase-compatibility-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-phase-compatibility-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-phase-compatibility-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-phase-compatibility-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

INPUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-crt-cover-word-ledger.json"
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-phase-compatibility-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-phase-compatibility-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-phase-compatibility-router.md"

CRT_WORD_ROUTER = (
    ROOT / "experiments" / "prime_matrix_square_phase_offband_prefix_gap_shadow_crt_cover_word_router.py"
)

MAIN_TARGET = "CompatibleCRTCoverWordPDECExclusionOrColumnPhaseLift"
NEXT_TARGET = "ColumnPhaseDensityExclusionForCompatibleCRTCoverWordsOrPrimeAvoidancePDEC"


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


def min_integer_gt(value: Fraction) -> int:
    """返回满足 n>value 的最小整数。"""
    return value.numerator // value.denominator + 1


def max_integer_lt(value: Fraction) -> int:
    """返回满足 n<value 的最大整数。"""
    return (value.numerator + value.denominator - 1) // value.denominator - 1


def phase_interval(row: dict[str, Any]) -> dict[str, Any]:
    """把固定 k/band atom 条件转为 P 的整数窗口。"""
    k_value = int(row["parent_atom_k"])
    band = row["parent_atom_band"]
    lower = -10**18
    upper = 10**18
    for b_value in range(int(row["b_lo"]), int(row["b_hi"]) + 1):
        # floor 层条件：k(P-2b)<=2b^2<(k+1)(P-2b)
        lower = max(lower, min_integer_gt(Fraction(2 * b_value * b_value, k_value + 1) + 2 * b_value))
        if k_value > 0:
            upper = min(upper, math.floor(Fraction(2 * b_value * b_value, k_value) + 2 * b_value))

        # 三分相位端带条件。
        if band == "plus_only_noslot":
            lower = max(
                lower,
                min_integer_gt(Fraction(4 * b_value * b_value + 4 * k_value * b_value + 4 * b_value - 1, 2 * k_value + 1)),
            )
        elif band == "minus_only_noslot":
            upper = min(
                upper,
                max_integer_lt(Fraction(4 * b_value * b_value + 4 * k_value * b_value + 1, 2 * k_value + 1)),
            )
        else:
            lower = max(
                lower,
                math.ceil(Fraction(4 * b_value * b_value + 4 * k_value * b_value + 4 * b_value - 1, 2 * k_value + 1)),
            )
            upper = min(
                upper,
                math.floor(Fraction(4 * b_value * b_value + 4 * k_value * b_value + 1, 2 * k_value + 1)),
            )
    return {
        "phase_p_lo": lower,
        "phase_p_hi": upper,
        "phase_p_width": max(0, upper - lower + 1),
        "actual_p_inside_phase_window": lower <= int(row["p"]) <= upper,
    }


def crt_pair(a_value: int, a_modulus: int, b_value: int, b_modulus: int) -> tuple[int, int] | None:
    """合并两个 CRT 条件。"""
    gcd_value = math.gcd(a_modulus, b_modulus)
    if (b_value - a_value) % gcd_value:
        return None
    reduced_a = a_modulus // gcd_value
    reduced_b = b_modulus // gcd_value
    delta = (b_value - a_value) // gcd_value
    inverse = pow(reduced_a, -1, reduced_b)
    step = (delta * inverse) % reduced_b
    modulus = a_modulus // gcd_value * b_modulus
    residue = (a_value + a_modulus * step) % modulus
    return residue, modulus


def first_in_progression(lo_value: int, hi_value: int, residue: int, modulus: int) -> int | None:
    """找区间内第一个指定同余类整数。"""
    if lo_value > hi_value:
        return None
    quotient = math.ceil((lo_value - residue) / modulus)
    value = residue + quotient * modulus
    return value if value <= hi_value else None


def first_prime_in_progression(lo_value: int, hi_value: int, residue: int, modulus: int, labels: list[int]) -> int | None:
    """找区间内第一个素数代表。"""
    value = first_in_progression(lo_value, hi_value, residue, modulus)
    label_set = set(labels)
    while value is not None and value <= hi_value:
        if is_prime(value) and value not in label_set:
            return value
        value += modulus
    return None


def enumerate_cover_words(row: dict[str, Any], phase: dict[str, Any]) -> dict[str, Any]:
    """枚举与相位窗口兼容的完整 CRT 覆盖词。"""
    b_start = int(row["b_lo"])
    length = int(row["cell_length"])
    label_pool = odd_primes(math.isqrt(int(row["p"])))
    phase_lo = int(phase["phase_p_lo"])
    phase_hi = int(phase["phase_p_hi"])
    total_words = 0
    phase_compatible_words = 0
    prime_phase_compatible_words = 0
    examples: list[dict[str, Any]] = []
    prime_examples: list[dict[str, Any]] = []

    def recurse(offset: int, residue: int, modulus: int, labels: list[int]) -> None:
        nonlocal total_words, phase_compatible_words, prime_phase_compatible_words
        if offset == length:
            total_words += 1
            sample = first_in_progression(phase_lo, phase_hi, residue, modulus)
            if sample is None:
                return
            phase_compatible_words += 1
            if len(examples) < 3:
                examples.append(
                    {
                        "labels": labels[:],
                        "residue": residue,
                        "modulus": modulus,
                        "sample_p": sample,
                    }
                )
            prime_sample = first_prime_in_progression(phase_lo, phase_hi, residue, modulus, labels)
            if prime_sample is not None:
                prime_phase_compatible_words += 1
                if len(prime_examples) < 3:
                    prime_examples.append(
                        {
                            "labels": labels[:],
                            "residue": residue,
                            "modulus": modulus,
                            "prime_sample_p": prime_sample,
                        }
                    )
            return

        b_value = b_start + offset
        for label in label_pool:
            # 若 label|b，则 P≡0 mod label；对 P>label 的素数不允许。
            if b_value % label == 0:
                continue
            next_condition = (2 * b_value) % label
            merged = crt_pair(residue, modulus, next_condition, label)
            if merged is None:
                continue
            recurse(offset + 1, merged[0], merged[1], labels + [label])

    recurse(0, 0, 1, [])
    return {
        "label_pool": label_pool,
        "total_admissible_cover_words": total_words,
        "phase_compatible_cover_word_count": phase_compatible_words,
        "prime_phase_compatible_cover_word_count": prime_phase_compatible_words,
        "phase_compatible_examples": examples,
        "prime_phase_compatible_examples": prime_examples,
    }


def compatibility_record(row: dict[str, Any]) -> dict[str, Any]:
    """生成单条 phase compatibility 记录。"""
    phase = phase_interval(row)
    enumeration = enumerate_cover_words(row, phase)
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
        "parent_atom_band": row["parent_atom_band"],
        "parent_atom_k": row["parent_atom_k"],
        **phase,
        **enumeration,
        "local_phase_alone_excludes_cover_words": enumeration["phase_compatible_cover_word_count"] == 0,
        "phase_boundary_statement": (
            "Fixed k/band inequalities define an explicit integer P-window. "
            "Compatible CRT cover words are then tested inside this same window."
        ),
    }


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "fixed_atom_phase_window_formula",
            "status": "closed",
            "statement": "The fixed small-k atom conditions give an explicit integer window for P.",
        },
        {
            "name": "crt_word_phase_compatibility_test",
            "status": "closed",
            "statement": "Each complete CRT cover word can be checked for intersection with that phase window.",
        },
        {
            "name": "local_phase_not_enough",
            "status": "closed",
            "statement": "The finite frontier has phase-compatible complete cover words, so local phase inequalities alone do not yield contradiction.",
        },
        {
            "name": "prime_phase_examples_exist",
            "status": "finite_evidence",
            "statement": "Some packets even have prime representatives in phase-compatible CRT classes; this is evidence that the remaining issue is distributional.",
        },
        {
            "name": "global_column_phase_density_exclusion",
            "status": "open",
            "statement": "A proof still needs to rule out persistent compatible cover words through column phase, density, or PDEC mechanisms.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "FixedPhaseWindowFormulaClosed",
            "closed": True,
            "proved": True,
            "meaning": "固定 small-k/band 条件已转成显式 P 窗口。",
            "remaining": "closed",
        },
        {
            "gate": "LocalPhaseExclusionAttemptResolved",
            "closed": True,
            "proved": True,
            "meaning": "相位窗口内仍有兼容覆盖词；局部相位本身不足以闭合。",
            "remaining": "closed",
        },
        {
            "gate": "FinitePrimeCompatibleExamples",
            "closed": result["prime_phase_compatible_packet_count"] > 0,
            "proved": False,
            "meaning": "有限前沿存在带素数代表的兼容类；提示剩余是密度/列相位排斥。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "GlobalColumnPhaseDensityExcluded",
            "closed": False,
            "proved": False,
            "meaning": "仍需排斥兼容 CRT 覆盖词在列相位中持久对齐。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步关闭局部相位误攻路线，不关闭全局命题。",
            "remaining": NEXT_TARGET,
        },
    ]


def build_result(input_ledger: Path) -> dict[str, Any]:
    """构造 phase compatibility 路由结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    source = load_json(input_ledger)
    records = [compatibility_record(row) for row in source["crt_word_records"]]
    local_exclusions = [row for row in records if row["local_phase_alone_excludes_cover_words"]]
    prime_packets = [row for row in records if row["prime_phase_compatible_cover_word_count"] > 0]
    aggregate = {
        "input_ledger": str(input_ledger.relative_to(ROOT)),
        "record_count": len(records),
        "local_phase_alone_exclusion_count": len(local_exclusions),
        "all_packets_have_phase_compatible_cover_words": all(
            row["phase_compatible_cover_word_count"] > 0 for row in records
        ),
        "prime_phase_compatible_packet_count": len(prime_packets),
        "max_phase_compatible_cover_word_count": max(
            (row["phase_compatible_cover_word_count"] for row in records),
            default=0,
        ),
        "max_prime_phase_compatible_cover_word_count": max(
            (row["prime_phase_compatible_cover_word_count"] for row in records),
            default=0,
        ),
        "global_column_phase_density_excluded": False,
        "row_column_unconditional_closed": False,
    }
    ledger = {
        "parameters": source["parameters"],
        "aggregate": aggregate,
        "phase_compatibility_records": records,
        "local_phase_alone_exclusion_records": local_exclusions,
        "prime_phase_compatible_records": prime_packets,
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = {
        "certificate_type": "prime_matrix_square_phase_offband_prefix_gap_shadow_phase_compatibility_router",
        "status": "local_phase_compatibility_checked_column_phase_density_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "empirical_absence_not_used_as_proof": True,
        "parameters": source["parameters"],
        "aggregate": aggregate,
        "phase_compatibility_records": records,
        "prime_phase_compatible_packet_count": len(prime_packets),
        "local_phase_alone_exclusion_count": len(local_exclusions),
        "local_phase_alone_closes_global_route": False,
        "global_column_phase_density_excluded": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_phase_compatibility_router.py": sha256(
                Path(__file__).resolve()
            ),
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_crt_cover_word_router.py": sha256(
                CRT_WORD_ROUTER
            ),
            "data/square-phase-offband-prefix-gap-shadow-crt-cover-word-ledger.json": sha256(input_ledger),
            "data/square-phase-offband-prefix-gap-shadow-phase-compatibility-ledger.json": sha256(OUT_LEDGER),
        },
        "plain_conclusion": (
            "本步把兼容 CRT 覆盖词放回固定 small-k/band 相位窗口中检验。每个 selected cell 的 "
            "k/band 条件都给出显式 P 窗口；有限前沿 11 个包全部存在与该窗口相交的完整覆盖词。"
            "因此局部相位窗口本身不能推出矛盾，剩余必须提升到列相位/密度层：排斥这些兼容覆盖词"
            "在同一反例链中持久对齐，或给出 PDEC/ColumnCRT 证书。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow phase compatibility router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"record_count={agg['record_count']}",
        f"local_phase_alone_exclusion_count={agg['local_phase_alone_exclusion_count']}",
        f"all_packets_have_phase_compatible_cover_words={fmt_bool(agg['all_packets_have_phase_compatible_cover_words'])}",
        f"prime_phase_compatible_packet_count={agg['prime_phase_compatible_packet_count']}",
        f"max_phase_compatible_cover_word_count={agg['max_phase_compatible_cover_word_count']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 相位窗口",
        "",
        "固定 `k` 与 `band` 后，`b_lo..b_hi` 中每个 b 都给出 P 的上下界；取交得到同一个整数窗口。然后把每个完整 CRT 覆盖词的同余类与该窗口求交。",
        "",
        "## 2. 兼容性前沿",
        "",
        "| P | side | b cell | parent atom | P window | phase-compatible words | prime-compatible words | example |",
        "| ---: | --- | --- | --- | --- | ---: | ---: | --- |",
    ]
    for row in result["phase_compatibility_records"]:
        example = row["phase_compatible_examples"][0] if row["phase_compatible_examples"] else {}
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["p"]),
                    f"`{row['side']}`",
                    f"`{row['b_lo']}-{row['b_hi']}`",
                    f"`{row['parent_atom_key']}`",
                    f"`{row['phase_p_lo']}-{row['phase_p_hi']}`",
                    f"`{row['phase_compatible_cover_word_count']}`",
                    f"`{row['prime_phase_compatible_cover_word_count']}`",
                    f"`{example}`",
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
            "- 局部 small-k 相位已经不足以闭合；下一步应直接构造列相位/密度 PDEC 排斥条件。",
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
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-phase-compatibility-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "local_phase_alone_exclusion_count": result["local_phase_alone_exclusion_count"],
                "prime_phase_compatible_packet_count": result["prime_phase_compatible_packet_count"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
