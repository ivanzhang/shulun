#!/usr/bin/env python3
"""登记 wheel absorption 之后的全局短 hull 素数下界边界。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_wheel_boundary_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-wheel-boundary-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-wheel-boundary-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-wheel-boundary-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-wheel-boundary-router.md
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

INPUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-wheel-absorption-ledger.json"
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-wheel-boundary-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-wheel-boundary-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-wheel-boundary-router.md"

WHEEL_ROUTER = ROOT / "experiments" / "prime_matrix_square_phase_offband_prefix_gap_shadow_wheel_absorption_router.py"
SQRT_BARRIER_DOC = DOCS / "prime-matrix-h3-square-root-short-interval-barrier.md"
ZERO_ROW_GAP_DOC = ROOT / "docs" / "zero-row-and-prime-gap-equivalence.md"

MAIN_TARGET = "HullPrimeCountBeatsComplementWheelCapacityOrWheelSurvivorAbsorptionPDEC"
NEXT_TARGET = "ShortHullPrimeLowerBoundAgainstFixedWheelPocketsOrWheelSurvivorAbsorptionPDEC"


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


def odd_candidate_count(q_lo: int, q_hi: int) -> int:
    """计算奇数候选 q 的个数。"""
    if q_hi < q_lo:
        return 0
    return (q_hi - q_lo) // 2 + 1


def boundary_record(row: dict[str, Any]) -> dict[str, Any]:
    """把 wheel absorption 记录压成一个短 hull 素数输入原子。"""
    p_value = int(row["p"])
    q_lo = int(row["q_hull_lo"])
    q_hi = int(row["q_hull_hi"])
    wheel_survivors = int(row["complement_wheel_survivor_count"])
    required_hull_prime_count = wheel_survivors + 1
    hull_prime_count = int(row["hull_prime_count"])
    depth = p_value - q_lo
    return {
        "p": p_value,
        "side": row["side"],
        "shape_key": row["shape_key"],
        "void_atom_keys": row["void_atom_keys"],
        "q_hull_lo": q_lo,
        "q_hull_hi": q_hi,
        "hull_span": q_hi - q_lo + 1,
        "hull_odd_candidate_count": odd_candidate_count(q_lo, q_hi),
        "depth_from_p": depth,
        "depth_over_sqrt_p": depth / math.sqrt(p_value),
        "hull_prime_count": hull_prime_count,
        "complement_wheel_survivor_count": wheel_survivors,
        "required_hull_prime_count_for_gate": required_hull_prime_count,
        "current_gate_margin": hull_prime_count - wheel_survivors,
        "prime_count_input": (
            f"pi([{q_lo},{q_hi}]) >= {required_hull_prime_count}; "
            f"this implies Prime(hull)>WheelSurvivors(C)."
        ),
        "failure_packet": (
            f"pi([{q_lo},{q_hi}]) <= {wheel_survivors} together with target-union void, "
            "so complement wheel survivors absorb every hull prime."
        ),
        "complement_wheel_survivor_values": row["complement_wheel_survivor_values"],
        "complement_pockets": row["complement_pockets"],
    }


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "wheel_gate_to_short_hull_prime_count",
            "status": "closed",
            "statement": "For each fixed pocket template, the wheel gate closes once the hull interval contains more primes than complement wheel survivors.",
        },
        {
            "name": "finite_tight_frontier_registered",
            "status": "closed",
            "statement": "The finite ledger identifies all margin-one frontier records and their exact required hull prime counts.",
        },
        {
            "name": "ordinary_0525_short_interval_input_mismatch",
            "status": "closed",
            "statement": "A one-prime x^0.525 short-interval input does not imply the required sqrt-scale multi-prime hull count.",
        },
        {
            "name": "global_short_hull_prime_lower_bound",
            "status": "open",
            "statement": "A global proof still needs sqrt-scale prime-count lower bounds for these fixed hull/pocket shapes, or exclusion of wheel-survivor absorption PDEC.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "WheelGateBoundaryClosed",
            "closed": True,
            "proved": True,
            "meaning": "当前 hardpoint 已精确转写为短 hull 素数计数胜过互补 wheel survivors。",
            "remaining": "closed",
        },
        {
            "gate": "FiniteFrontierRegistered",
            "closed": True,
            "proved": False,
            "meaning": "有限最紧样本和所需素数数已登记；这不是全局证明。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "ExternalBHP0525ClosesThisRoute",
            "closed": False,
            "proved": False,
            "meaning": "BHP 型一个素数的 x^0.525 输入既长于 sqrt 尺度，也不给多素数计数。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "GlobalShortHullPrimeLowerBoundClosed",
            "closed": False,
            "proved": False,
            "meaning": "仍需证明固定形状短 hull 的素数计数下界，或排斥持久吸收包。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只关闭边界转写，不关闭行/列无条件命题。",
            "remaining": NEXT_TARGET,
        },
    ]


def build_result(input_ledger: Path) -> dict[str, Any]:
    """构造边界路由结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    source = load_json(input_ledger)
    records = [boundary_record(row) for row in source["records"]]
    frontier = sorted(records, key=lambda row: (row["current_gate_margin"], row["required_hull_prime_count_for_gate"], row["p"]))
    tight = [row for row in records if row["current_gate_margin"] == 1]
    aggregate = {
        "input_ledger": str(input_ledger.relative_to(ROOT)),
        "record_count": len(records),
        "finite_all_wheel_gates_closed": all(row["current_gate_margin"] > 0 for row in records),
        "tight_margin_one_count": len(tight),
        "min_current_gate_margin": min((row["current_gate_margin"] for row in records), default=None),
        "max_required_hull_prime_count_for_gate": max(
            (row["required_hull_prime_count_for_gate"] for row in records),
            default=0,
        ),
        "max_complement_wheel_survivor_count": max(
            (row["complement_wheel_survivor_count"] for row in records),
            default=0,
        ),
        "max_depth_from_p": max((row["depth_from_p"] for row in records), default=0),
        "max_depth_over_sqrt_p": max((row["depth_over_sqrt_p"] for row in records), default=0.0),
        "max_hull_odd_candidate_count": max((row["hull_odd_candidate_count"] for row in records), default=0),
    }
    ledger = {
        "parameters": source["parameters"],
        "aggregate": aggregate,
        "boundary_records": records,
        "tight_frontier": tight,
        "frontier": frontier,
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = {
        "certificate_type": "prime_matrix_square_phase_offband_prefix_gap_shadow_wheel_boundary_router",
        "status": "short_hull_prime_count_boundary_registered_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "empirical_absence_not_used_as_proof": True,
        "parameters": source["parameters"],
        "aggregate": aggregate,
        "tight_frontier": tight,
        "frontier": frontier,
        "ordinary_0525_short_interval_input_closes": False,
        "reason_0525_mismatch": (
            "The required hulls have depth O(sqrt(P)) below P and may require up to "
            f"{aggregate['max_required_hull_prime_count_for_gate']} primes, whereas a BHP-type "
            "x^0.525 one-prime input is both longer than sqrt scale and count-insufficient."
        ),
        "global_short_hull_prime_lower_bound_proved": False,
        "wheel_survivor_absorption_pdec_excluded": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_wheel_boundary_router.py": sha256(
                Path(__file__).resolve()
            ),
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_wheel_absorption_router.py": sha256(
                WHEEL_ROUTER
            ),
            "data/square-phase-offband-prefix-gap-shadow-wheel-absorption-ledger.json": sha256(input_ledger),
            "data/square-phase-offband-prefix-gap-shadow-wheel-boundary-ledger.json": sha256(OUT_LEDGER),
            "docs/monograph/prime-matrix-h3-square-root-short-interval-barrier.md": sha256(SQRT_BARRIER_DOC),
            "docs/zero-row-and-prime-gap-equivalence.md": sha256(ZERO_ROW_GAP_DOC),
        },
        "plain_conclusion": (
            "本步没有转换命题：wheel absorption 之后的真正剩余被精确登记为短 hull 素数计数下界。"
            "有限账本中所有 wheel gate 已关闭，最紧余量为 1；但全局证明必须说明每个固定形状 hull "
            "含有多于互补孔袋 wheel survivors 的素数。普通 x^0.525 一个素数短区间输入不能直接闭合该门，"
            "因为这里需要 sqrt 级、且最多需要 6 个 hull 素数。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow wheel boundary router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"record_count={agg['record_count']}",
        f"finite_all_wheel_gates_closed={fmt_bool(agg['finite_all_wheel_gates_closed'])}",
        f"tight_margin_one_count={agg['tight_margin_one_count']}",
        f"min_current_gate_margin={agg['min_current_gate_margin']}",
        f"max_required_hull_prime_count_for_gate={agg['max_required_hull_prime_count_for_gate']}",
        f"max_depth_over_sqrt_p={agg['max_depth_over_sqrt_p']:.6f}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 精确边界",
        "",
        "对每个固定孔袋模板，当前门只需要证明",
        "",
        "```text",
        "Prime(hull) > WheelSurvivors(complement pockets)",
        "```",
        "",
        "等价地，若互补孔袋有 `S` 个小轮筛幸存者，则 hull 区间至少要有 `S+1` 个素数。"
        "若该不等式失败且目标并集仍全空，反例必须进入 wheel-survivor absorption PDEC。",
        "",
        "## 2. 最紧前沿",
        "",
        "| P | side | hull | depth/sqrt(P) | hull primes | wheel survivors | required primes | margin |",
        "| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in result["frontier"][:16]:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["p"]),
                    f"`{row['side']}`",
                    f"`{row['q_hull_lo']}-{row['q_hull_hi']}`",
                    f"{row['depth_over_sqrt_p']:.6f}",
                    str(row["hull_prime_count"]),
                    str(row["complement_wheel_survivor_count"]),
                    str(row["required_hull_prime_count_for_gate"]),
                    str(row["current_gate_margin"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 3. 外部输入匹配审查",
            "",
            "- 当前 hull 深度是 `O(sqrt(P))`，最大样本深度约 `2.321388*sqrt(P)`。",
            "- 当前 gate 不是“有一个素数”即可统一闭合；最坏模板需要 `6` 个 hull 素数。",
            "- 因此普通 Baker--Harman--Pintz 型 `x^0.525` 一个素数短区间输入不匹配本门。",
            "- 若要外部闭合，需要 sqrt 级多素数计数输入，或直接证明这些固定穿孔并集含素数。",
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
            "- 自足线：对固定小 `k` 形状证明短 hull 多素数下界，或从目标 union 直接构造一个素数。",
            "- 反例线：若下界失败，必须形成命名的 wheel-survivor absorption PDEC，并继续寻找与相位/列刚性的矛盾。",
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
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-wheel-boundary-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "record_count": result["aggregate"]["record_count"],
                "tight_margin_one_count": result["aggregate"]["tight_margin_one_count"],
                "max_required_hull_prime_count_for_gate": result["aggregate"][
                    "max_required_hull_prime_count_for_gate"
                ],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
