#!/usr/bin/env python3
"""把 wheel-bound 从 13 升级并登记首个有效容量收缩点。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_wheel_escalation_router.py
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_wheel_escalation_router.py --wheel-bounds 13,17,19,23,29,31

输出：
  data/square-phase-offband-prefix-gap-shadow-wheel-escalation-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-wheel-escalation-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-wheel-escalation-router.md
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

INPUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-hull-absorption-ledger.json"
BOUNDARY_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-wheel-boundary-ledger.json"
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-wheel-escalation-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-wheel-escalation-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-wheel-escalation-router.md"

HULL_ROUTER = ROOT / "experiments" / "prime_matrix_square_phase_offband_prefix_gap_shadow_hull_absorption_router.py"
WHEEL_BOUNDARY_ROUTER = (
    ROOT / "experiments" / "prime_matrix_square_phase_offband_prefix_gap_shadow_wheel_boundary_router.py"
)

MAIN_TARGET = "ShortHullPrimeLowerBoundAgainstFixedWheelPocketsOrWheelSurvivorAbsorptionPDEC"
NEXT_TARGET = "ShortHullPrimeLowerBoundAgainstWheel17FixedPocketsOrPrimeSupportCollapsePDEC"


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


def parse_bounds(raw: str) -> list[int]:
    """解析 wheel bound 列表。"""
    values = [int(part) for part in raw.split(",") if part.strip()]
    if not values:
        raise ValueError("empty wheel bounds")
    return sorted(set(values))


def small_primes(bound: int) -> list[int]:
    """列出不超过 bound 的奇素数。"""
    primes: list[int] = []
    for value in range(3, bound + 1):
        for divisor in range(2, int(value**0.5) + 1):
            if value % divisor == 0:
                break
        else:
            primes.append(value)
    return primes


def odd_values(q_lo: int, q_hi: int) -> list[int]:
    """列出奇候选 q。"""
    return list(range(q_lo, q_hi + 1, 2))


def survives_wheel(q_value: int, wheel_primes: list[int]) -> bool:
    """判断 q 是否通过给定小轮筛。"""
    return all(q_value == prime or q_value % prime != 0 for prime in wheel_primes)


def wheel_survivor_values(row: dict[str, Any], wheel_primes: list[int]) -> list[int]:
    """列出互补孔袋中的 wheel survivors。"""
    values: list[int] = []
    for pocket in row["complement_pockets"]:
        values.extend(q for q in odd_values(pocket["q_lo"], pocket["q_hi"]) if survives_wheel(q, wheel_primes))
    return values


def compact_template(row: dict[str, Any], survivors: list[int]) -> dict[str, Any]:
    """压缩单个模板在给定 wheel 下的容量记录。"""
    survivor_count = len(survivors)
    return {
        "p": row["p"],
        "side": row["side"],
        "shape_key": row["shape_key"],
        "void_atom_keys": row["void_atom_keys"],
        "q_hull_lo": row["q_hull_lo"],
        "q_hull_hi": row["q_hull_hi"],
        "hull_prime_count": row["hull_prime_count"],
        "complement_prime_count": row["complement_prime_count"],
        "wheel_survivor_count": survivor_count,
        "required_hull_prime_count_for_gate": survivor_count + 1,
        "wheel_capacity_margin": row["hull_prime_count"] - survivor_count,
        "wheel_survivor_values": survivors,
        "complement_pockets": row["complement_pockets"],
    }


def bound_record(rows: list[dict[str, Any]], bound: int) -> dict[str, Any]:
    """生成某个 wheel bound 的整体画像。"""
    wheel_primes = small_primes(bound)
    records = [compact_template(row, wheel_survivor_values(row, wheel_primes)) for row in rows]
    frontier = sorted(records, key=lambda item: (item["wheel_capacity_margin"], item["required_hull_prime_count_for_gate"], item["p"]))
    return {
        "wheel_bound": bound,
        "wheel_primes": wheel_primes,
        "record_count": len(records),
        "all_finite_gates_closed": all(item["wheel_capacity_margin"] > 0 for item in records),
        "min_wheel_capacity_margin": min((item["wheel_capacity_margin"] for item in records), default=None),
        "tight_margin_one_count": sum(1 for item in records if item["wheel_capacity_margin"] == 1),
        "max_wheel_survivor_count": max((item["wheel_survivor_count"] for item in records), default=0),
        "max_required_hull_prime_count_for_gate": max(
            (item["required_hull_prime_count_for_gate"] for item in records),
            default=0,
        ),
        "frontier": frontier,
    }


def select_bound(bound_records: list[dict[str, Any]]) -> dict[str, Any]:
    """选择首个达到最小最大需求的 wheel bound。"""
    best_need = min(item["max_required_hull_prime_count_for_gate"] for item in bound_records)
    candidates = [item for item in bound_records if item["max_required_hull_prime_count_for_gate"] == best_need]
    return min(candidates, key=lambda item: item["wheel_bound"])


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "wheel_capacity_monotonicity",
            "status": "closed",
            "statement": "Increasing the wheel bound can only remove complement-pocket survivors and cannot weaken the gate Prime(hull)>WheelSurvivors(C).",
        },
        {
            "name": "first_effective_wheel17_capacity_drop",
            "status": "finite_evidence",
            "statement": "On the finite residual frontier, adding 17 drops the maximum survivor requirement from 6 hull primes to 5 hull primes.",
        },
        {
            "name": "post17_no_further_finite_drop",
            "status": "finite_evidence",
            "statement": "For tested bounds 19,23,29,31, the finite frontier does not improve beyond the wheel-17 capacity.",
        },
        {
            "name": "global_wheel17_short_hull_lower_bound",
            "status": "open",
            "statement": "A global proof still needs short hull prime counts beating wheel-17 pocket survivors, or exclusion of prime-support collapse.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "WheelEscalationMonotonicityClosed",
            "closed": True,
            "proved": True,
            "meaning": "轮筛升级只会减少互补孔袋容量，因此保持同一目标命题。",
            "remaining": "closed",
        },
        {
            "gate": "FiniteWheel17CapacityDropRegistered",
            "closed": result["selected_wheel_bound"] == 17,
            "proved": False,
            "meaning": "有限前沿中 17 是首个把最大所需 hull 素数数从 6 降到 5 的小轮。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "GlobalWheel17LowerBoundClosed",
            "closed": False,
            "proved": False,
            "meaning": "仍需全局证明短 hull 素数数超过 wheel-17 互补幸存容量。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "PrimeSupportCollapsePDECExcluded",
            "closed": False,
            "proved": False,
            "meaning": "若短 hull 下界失败，仍需排斥所有 hull 素数被 wheel-17 孔袋吸收的支撑塌缩。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只压缩容量常数，不关闭全局行/列命题。",
            "remaining": NEXT_TARGET,
        },
    ]


def build_result(input_ledger: Path, wheel_bounds: list[int]) -> dict[str, Any]:
    """构造 wheel 升级路由结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    source = load_json(input_ledger)
    rows = source["count_gate_residual_frontier"]
    records = [bound_record(rows, bound) for bound in wheel_bounds]
    selected = select_bound(records)
    baseline = records[0]
    aggregate = {
        "input_ledger": str(input_ledger.relative_to(ROOT)),
        "wheel_bounds": wheel_bounds,
        "source_residual_count": len(rows),
        "baseline_wheel_bound": baseline["wheel_bound"],
        "baseline_max_required_hull_prime_count_for_gate": baseline[
            "max_required_hull_prime_count_for_gate"
        ],
        "selected_wheel_bound": selected["wheel_bound"],
        "selected_wheel_primes": selected["wheel_primes"],
        "selected_max_required_hull_prime_count_for_gate": selected[
            "max_required_hull_prime_count_for_gate"
        ],
        "selected_max_wheel_survivor_count": selected["max_wheel_survivor_count"],
        "selected_tight_margin_one_count": selected["tight_margin_one_count"],
        "selected_min_wheel_capacity_margin": selected["min_wheel_capacity_margin"],
        "finite_capacity_drop": baseline["max_required_hull_prime_count_for_gate"]
        - selected["max_required_hull_prime_count_for_gate"],
    }
    ledger = {
        "parameters": source["parameters"],
        "aggregate": aggregate,
        "wheel_bound_records": records,
        "selected_frontier": selected["frontier"],
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = {
        "certificate_type": "prime_matrix_square_phase_offband_prefix_gap_shadow_wheel_escalation_router",
        "status": "wheel17_capacity_drop_registered_global_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "empirical_absence_not_used_as_proof": True,
        "parameters": source["parameters"],
        "aggregate": aggregate,
        "wheel_bound_records": records,
        "selected_wheel_bound": selected["wheel_bound"],
        "selected_frontier": selected["frontier"],
        "selected_max_required_hull_prime_count_for_gate": selected[
            "max_required_hull_prime_count_for_gate"
        ],
        "wheel17_short_hull_lower_bound_proved": False,
        "prime_support_collapse_pdec_excluded": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_wheel_escalation_router.py": sha256(
                Path(__file__).resolve()
            ),
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_hull_absorption_router.py": sha256(
                HULL_ROUTER
            ),
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_wheel_boundary_router.py": sha256(
                WHEEL_BOUNDARY_ROUTER
            ),
            "data/square-phase-offband-prefix-gap-shadow-hull-absorption-ledger.json": sha256(input_ledger),
            "data/square-phase-offband-prefix-gap-shadow-wheel-boundary-ledger.json": sha256(BOUNDARY_LEDGER),
            "data/square-phase-offband-prefix-gap-shadow-wheel-escalation-ledger.json": sha256(OUT_LEDGER),
        },
        "plain_conclusion": (
            "本步沿同一 hardpoint 做容量单调升级：把小轮从 13 升到 17 后，有限前沿的最大互补幸存容量"
            "从 5 降到 4，因此最大所需 hull 素数数从 6 降到 5；继续升到 19/23/29/31 在当前前沿没有进一步下降。"
            "这不是全局闭合，而是把下一硬点压成 wheel-17 固定孔袋短 hull 下界，或 prime-support collapse PDEC 排斥。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow wheel escalation router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"baseline_wheel_bound={agg['baseline_wheel_bound']}",
        f"baseline_max_required_hull_prime_count={agg['baseline_max_required_hull_prime_count_for_gate']}",
        f"selected_wheel_bound={agg['selected_wheel_bound']}",
        f"selected_wheel_primes={agg['selected_wheel_primes']}",
        f"selected_max_required_hull_prime_count={agg['selected_max_required_hull_prime_count_for_gate']}",
        f"finite_capacity_drop={agg['finite_capacity_drop']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 轮筛升级表",
        "",
        "| bound | wheel primes | max survivors | max required hull primes | min margin | tight margin-one | all finite gates closed |",
        "| ---: | --- | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in result["wheel_bound_records"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["wheel_bound"]),
                    f"`{row['wheel_primes']}`",
                    str(row["max_wheel_survivor_count"]),
                    str(row["max_required_hull_prime_count_for_gate"]),
                    str(row["min_wheel_capacity_margin"]),
                    str(row["tight_margin_one_count"]),
                    f"`{fmt_bool(row['all_finite_gates_closed'])}`",
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 2. wheel-17 最紧前沿",
            "",
            "| P | side | hull | hull primes | wheel-17 survivors | required primes | margin | survivor values |",
            "| ---: | --- | --- | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for row in result["selected_frontier"][:16]:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["p"]),
                    f"`{row['side']}`",
                    f"`{row['q_hull_lo']}-{row['q_hull_hi']}`",
                    str(row["hull_prime_count"]),
                    str(row["wheel_survivor_count"]),
                    str(row["required_hull_prime_count_for_gate"]),
                    str(row["wheel_capacity_margin"]),
                    f"`{row['wheel_survivor_values']}`",
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
            "- 容量侧：证明 wheel-17 固定孔袋的短 hull 多素数下界。",
            "- 反例侧：若失败，反例必须把所有 hull 素数压进至多 4 个 wheel-17 幸存位置，形成 prime-support collapse PDEC。",
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
    parser.add_argument("--wheel-bounds", default="13,17,19,23,29,31")
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    input_ledger = args.input_ledger if args.input_ledger.is_absolute() else ROOT / args.input_ledger
    result = build_result(input_ledger, parse_bounds(args.wheel_bounds))
    write_markdown(result)
    result["source_hashes"][
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-wheel-escalation-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "selected_wheel_bound": result["selected_wheel_bound"],
                "selected_max_required_hull_prime_count_for_gate": result[
                    "selected_max_required_hull_prime_count_for_gate"
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
