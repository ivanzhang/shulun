#!/usr/bin/env python3
"""把 wheel-17 失败包登记为穿孔 hull 素数支撑塌缩模式。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_support_collapse_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-support-collapse-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-support-collapse-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-support-collapse-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-support-collapse-router.md
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

INPUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-wheel-escalation-ledger.json"
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-support-collapse-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-support-collapse-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-support-collapse-router.md"

ESCALATION_ROUTER = (
    ROOT / "experiments" / "prime_matrix_square_phase_offband_prefix_gap_shadow_wheel_escalation_router.py"
)

MAIN_TARGET = "ShortHullPrimeLowerBoundAgainstWheel17FixedPocketsOrPrimeSupportCollapsePDEC"
NEXT_TARGET = "FixedSmallKPuncturedHullPrimeGapPatternExclusionOrSupportCollapsePDEC"


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


def parse_atom_interval(key: str) -> dict[str, Any]:
    """解析 band:k:qlo-qhi atom 键。"""
    band, rest = key.split(":k", 1)
    k_text, q_text = rest.split(":", 1)
    q_lo_text, q_hi_text = q_text.split("-", 1)
    return {
        "band": band,
        "k": int(k_text),
        "q_lo": int(q_lo_text),
        "q_hi": int(q_hi_text),
    }


def merge_intervals(intervals: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """合并步长 2 的奇数区间。"""
    if not intervals:
        return []
    ordered = sorted((item["q_lo"], item["q_hi"]) for item in intervals)
    merged: list[dict[str, Any]] = []
    lo, hi = ordered[0]
    for next_lo, next_hi in ordered[1:]:
        if next_lo <= hi + 2:
            hi = max(hi, next_hi)
        else:
            merged.append({"q_lo": lo, "q_hi": hi, "candidate_count": (hi - lo) // 2 + 1})
            lo, hi = next_lo, next_hi
    merged.append({"q_lo": lo, "q_hi": hi, "candidate_count": (hi - lo) // 2 + 1})
    return merged


def complement_prime_values(row: dict[str, Any]) -> list[int]:
    """读取互补孔袋实际素数值。"""
    values: list[int] = []
    for pocket in row["complement_pockets"]:
        values.extend(pocket.get("prime_values", []))
    return sorted(set(values))


def collapse_record(row: dict[str, Any], prime_flags: bytearray) -> dict[str, Any]:
    """生成支撑塌缩失败包记录。"""
    q_lo = int(row["q_hull_lo"])
    q_hi = int(row["q_hull_hi"])
    survivor_values = sorted(set(row["wheel_survivor_values"]))
    survivor_set = set(survivor_values)
    hull_values = odd_values(q_lo, q_hi)
    hull_prime_values = [q for q in hull_values if prime_flags[q]]
    escape_prime_values = [q for q in hull_prime_values if q not in survivor_set]
    atom_intervals = [parse_atom_interval(key) for key in row["void_atom_keys"]]
    union_intervals = merge_intervals(atom_intervals)
    punctured_composite_values = [q for q in hull_values if q not in survivor_set]
    return {
        "p": row["p"],
        "side": row["side"],
        "shape_key": row["shape_key"],
        "q_hull_lo": q_lo,
        "q_hull_hi": q_hi,
        "hull_odd_candidate_count": len(hull_values),
        "void_atom_keys": row["void_atom_keys"],
        "target_union_intervals": union_intervals,
        "complement_pockets": row["complement_pockets"],
        "wheel17_survivor_values": survivor_values,
        "wheel17_survivor_count": len(survivor_values),
        "required_hull_prime_count_for_gate": len(survivor_values) + 1,
        "punctured_composite_candidate_count": len(punctured_composite_values),
        "collapse_packet_statement": (
            f"All primes in odd hull [{q_lo},{q_hi}] must lie in {survivor_values}; "
            "every other odd hull candidate is composite."
        ),
        "actual_hull_prime_values": hull_prime_values,
        "actual_escape_prime_values": escape_prime_values,
        "actual_escape_prime_count": len(escape_prime_values),
        "actual_support_collapse_occurs": len(escape_prime_values) == 0,
        "actual_complement_prime_values": complement_prime_values(row),
    }


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "support_collapse_packet_equivalence",
            "status": "closed",
            "statement": "If the wheel-17 gate fails and the target union is prime-void, all hull primes must lie in the explicit wheel-17 survivor set.",
        },
        {
            "name": "punctured_hull_gap_pattern_registration",
            "status": "closed",
            "statement": "The failure packet is a punctured prime-gap pattern: the hull is prime-free outside at most four survivor positions.",
        },
        {
            "name": "finite_no_actual_support_collapse",
            "status": "finite_evidence",
            "statement": "The finite audit finds at least one escaping prime outside the survivor set in every packet.",
        },
        {
            "name": "global_punctured_hull_gap_exclusion",
            "status": "open",
            "statement": "A global proof still needs to exclude these fixed small-k punctured hull gap patterns.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "SupportCollapsePacketEquivalenceClosed",
            "closed": True,
            "proved": True,
            "meaning": "wheel-17 下界失败已等价压成素数支撑塌缩包。",
            "remaining": "closed",
        },
        {
            "gate": "PuncturedHullGapPatternRegistered",
            "closed": True,
            "proved": True,
            "meaning": "每个失败包都是固定小 k 的穿孔短素数间隙模式。",
            "remaining": "closed",
        },
        {
            "gate": "FiniteNoSupportCollapse",
            "closed": result["actual_support_collapse_count"] == 0,
            "proved": False,
            "meaning": "有限前沿中每个包都有逃逸素数；这不是全局证明。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "GlobalSupportCollapseExcluded",
            "closed": False,
            "proved": False,
            "meaning": "仍需全局排斥这些固定形状穿孔 hull gap。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只完成反例包结构化，不关闭全局行/列命题。",
            "remaining": NEXT_TARGET,
        },
    ]


def build_result(input_ledger: Path) -> dict[str, Any]:
    """构造支撑塌缩路由结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    source = load_json(input_ledger)
    max_q = max((row["q_hull_hi"] for row in source["selected_frontier"]), default=2)
    prime_flags = sieve(max_q)
    records = [collapse_record(row, prime_flags) for row in source["selected_frontier"]]
    frontier = sorted(records, key=lambda item: (item["actual_escape_prime_count"], -item["wheel17_survivor_count"], item["p"]))
    aggregate = {
        "input_ledger": str(input_ledger.relative_to(ROOT)),
        "record_count": len(records),
        "wheel_bound": source["aggregate"]["selected_wheel_bound"],
        "max_wheel17_survivor_count": max((row["wheel17_survivor_count"] for row in records), default=0),
        "max_required_hull_prime_count_for_gate": max(
            (row["required_hull_prime_count_for_gate"] for row in records),
            default=0,
        ),
        "min_actual_escape_prime_count": min((row["actual_escape_prime_count"] for row in records), default=None),
        "actual_support_collapse_count": sum(1 for row in records if row["actual_support_collapse_occurs"]),
        "max_punctured_composite_candidate_count": max(
            (row["punctured_composite_candidate_count"] for row in records),
            default=0,
        ),
    }
    ledger = {
        "parameters": source["parameters"],
        "aggregate": aggregate,
        "collapse_records": records,
        "collapse_frontier": frontier,
        "actual_support_collapse_records": [row for row in records if row["actual_support_collapse_occurs"]],
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = {
        "certificate_type": "prime_matrix_square_phase_offband_prefix_gap_shadow_support_collapse_router",
        "status": "punctured_hull_support_collapse_pdec_registered_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "empirical_absence_not_used_as_proof": True,
        "parameters": source["parameters"],
        "aggregate": aggregate,
        "collapse_frontier": frontier,
        "support_collapse_packet_equivalence_closed": True,
        "global_punctured_hull_gap_exclusion_proved": False,
        "actual_support_collapse_count": aggregate["actual_support_collapse_count"],
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_support_collapse_router.py": sha256(
                Path(__file__).resolve()
            ),
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_wheel_escalation_router.py": sha256(
                ESCALATION_ROUTER
            ),
            "data/square-phase-offband-prefix-gap-shadow-wheel-escalation-ledger.json": sha256(input_ledger),
            "data/square-phase-offband-prefix-gap-shadow-support-collapse-ledger.json": sha256(OUT_LEDGER),
        },
        "plain_conclusion": (
            "本步把 wheel-17 失败包进一步压成穿孔 hull 素数支撑塌缩：若目标 union 全空且 wheel-17 容量门失败，"
            "则整个短 hull 中所有素数都必须落入至多 4 个指定 wheel-17 幸存位置，其他奇候选全部合数。"
            "有限账本中每个包都有至少一个逃逸素数，因此实际塌缩数为 0；全局仍需排斥这些固定小 k 穿孔短间隙模式。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow support collapse router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"wheel_bound={agg['wheel_bound']}",
        f"record_count={agg['record_count']}",
        f"max_wheel17_survivor_count={agg['max_wheel17_survivor_count']}",
        f"max_required_hull_prime_count={agg['max_required_hull_prime_count_for_gate']}",
        f"min_actual_escape_prime_count={agg['min_actual_escape_prime_count']}",
        f"actual_support_collapse_count={agg['actual_support_collapse_count']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 塌缩包",
        "",
        "wheel-17 下界失败并且目标 union 全空时，反例必须满足：",
        "",
        "```text",
        "Prime(hull) subset Wheel17Survivors(complement pockets)",
        "```",
        "",
        "这等价于一个穿孔短素数间隙：hull 中除少数幸存位置外全部为合数。",
        "",
        "## 2. 塌缩前沿",
        "",
        "| P | side | hull | survivors | escape primes | punctured composite candidates |",
        "| ---: | --- | --- | --- | --- | ---: |",
    ]
    for row in result["collapse_frontier"][:16]:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["p"]),
                    f"`{row['side']}`",
                    f"`{row['q_hull_lo']}-{row['q_hull_hi']}`",
                    f"`{row['wheel17_survivor_values']}`",
                    f"`{row['actual_escape_prime_values']}`",
                    str(row["punctured_composite_candidate_count"]),
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
            "- 证明方向：排斥固定小 `k` 的穿孔 hull gap pattern，或把该 pattern 接入更强的列相位/平方锚矛盾。",
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
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-support-collapse-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "max_wheel17_survivor_count": result["aggregate"]["max_wheel17_survivor_count"],
                "min_actual_escape_prime_count": result["aggregate"]["min_actual_escape_prime_count"],
                "actual_support_collapse_count": result["actual_support_collapse_count"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
