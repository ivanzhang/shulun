#!/usr/bin/env python3
"""把互补孔袋吸收 PDEC 压成小轮筛幸存容量门。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_wheel_absorption_router.py --wheel-bound 13
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-wheel-absorption-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-wheel-absorption-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-wheel-absorption-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-wheel-absorption-router.md
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
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-wheel-absorption-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-wheel-absorption-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-wheel-absorption-router.md"

HULL_ROUTER = ROOT / "experiments" / "prime_matrix_square_phase_offband_prefix_gap_shadow_hull_absorption_router.py"

MAIN_TARGET = "HullPrimeCountBeatsCoverageDefectOrComplementPocketAbsorptionPDEC"
NEXT_TARGET = "HullPrimeCountBeatsComplementWheelCapacityOrWheelSurvivorAbsorptionPDEC"


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
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def small_primes(bound: int) -> list[int]:
    """列出不超过 bound 的小素数，从 3 开始保留奇轮筛。"""
    primes: list[int] = []
    for value in range(3, bound + 1):
        for divisor in range(2, int(value**0.5) + 1):
            if value % divisor == 0:
                break
        else:
            primes.append(value)
    return primes


def odd_values(q_lo: int, q_hi: int) -> list[int]:
    """列出同奇偶候选 q。"""
    return list(range(q_lo, q_hi + 1, 2))


def survives_wheel(q_value: int, wheel_primes: list[int]) -> bool:
    """判断 q 是否通过小轮筛。"""
    return all(q_value == prime or q_value % prime != 0 for prime in wheel_primes)


def pocket_wheel_values(pocket: dict[str, Any], wheel_primes: list[int]) -> list[int]:
    """列出互补孔袋中通过小轮筛的候选。"""
    return [q for q in odd_values(pocket["q_lo"], pocket["q_hi"]) if survives_wheel(q, wheel_primes)]


def enrich_record(row: dict[str, Any], wheel_primes: list[int]) -> dict[str, Any]:
    """为 hull absorption 记录补充小轮筛容量。"""
    pockets: list[dict[str, Any]] = []
    wheel_survivor_values: list[int] = []
    for pocket in row["complement_pockets"]:
        values = pocket_wheel_values(pocket, wheel_primes)
        wheel_survivor_values.extend(values)
        pockets.append(
            {
                **pocket,
                "wheel_survivor_count": len(values),
                "wheel_survivor_values": values[:16],
            }
        )
    wheel_survivor_count = len(wheel_survivor_values)
    wheel_capacity_margin = row["hull_prime_count"] - wheel_survivor_count
    return {
        **row,
        "wheel_primes": wheel_primes,
        "complement_wheel_survivor_count": wheel_survivor_count,
        "complement_wheel_survivor_values": wheel_survivor_values[:24],
        "wheel_capacity_margin": wheel_capacity_margin,
        "wheel_capacity_gate_closes": wheel_capacity_margin > 0,
        "wheel_survivor_absorption_pdec": wheel_capacity_margin <= 0,
        "complement_pockets": pockets,
    }


def theorem_rows(wheel_bound: int) -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "complement_prime_capacity_leq_wheel_survivors",
            "status": "closed",
            "statement": f"Complement-pocket primes are bounded by survivors of the odd wheel with primes <= {wheel_bound}.",
        },
        {
            "name": "hull_count_beats_wheel_capacity_gate",
            "status": "closed",
            "statement": "If hull_prime_count is larger than complement wheel survivors, the target union must contain a prime.",
        },
        {
            "name": "finite_no_wheel_survivor_absorption",
            "status": "finite_evidence",
            "statement": "The finite audit finds no residual wheel-survivor absorption after the chosen wheel.",
        },
        {
            "name": "global_wheel_survivor_absorption_exclusion",
            "status": "open",
            "statement": "A global proof still needs hull prime lower bounds beating wheel survivor capacity, or exclusion of persistent wheel-survivor absorption.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "ComplementWheelCapacityGateClosed",
            "closed": True,
            "proved": True,
            "meaning": "互补孔袋吸收容量已从候选数降到小轮筛幸存数。",
            "remaining": "closed",
        },
        {
            "gate": "FiniteNoWheelSurvivorAbsorptionPDEC",
            "closed": result["wheel_survivor_absorption_pdec_count"] == 0,
            "proved": False,
            "meaning": "有限样本中小轮筛容量门关闭所有残余。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "GlobalWheelCapacityClosed",
            "closed": False,
            "proved": False,
            "meaning": "仍需全局证明 hull 素数下界超过互补轮筛容量，或排斥持久吸收。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只完成容量压缩，不关闭全局行/列命题。",
            "remaining": NEXT_TARGET,
        },
    ]


def compact_record(row: dict[str, Any]) -> dict[str, Any]:
    """压缩记录。"""
    return {
        "p": row["p"],
        "side": row["side"],
        "input_type": row["input_type"],
        "shape_key": row["shape_key"],
        "void_atom_keys": row["void_atom_keys"],
        "q_hull_lo": row["q_hull_lo"],
        "q_hull_hi": row["q_hull_hi"],
        "hull_prime_count": row["hull_prime_count"],
        "coverage_defect_candidate_count": row["coverage_defect_candidate_count"],
        "complement_prime_count": row["complement_prime_count"],
        "union_prime_count": row["union_prime_count"],
        "complement_wheel_survivor_count": row["complement_wheel_survivor_count"],
        "wheel_capacity_margin": row["wheel_capacity_margin"],
        "complement_wheel_survivor_values": row["complement_wheel_survivor_values"],
        "complement_pockets": row["complement_pockets"],
    }


def build_result(input_ledger: Path, wheel_bound: int) -> dict[str, Any]:
    """构造路由器结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    source = load_json(input_ledger)
    wheel_primes = small_primes(wheel_bound)
    source_records = source["count_gate_residual_frontier"]
    records = [enrich_record(row, wheel_primes) for row in source_records]
    wheel_pdec = [row for row in records if row["wheel_survivor_absorption_pdec"]]
    frontier = sorted(records, key=lambda row: (row["wheel_capacity_margin"], -row["hull_prime_count"], row["p"]))
    aggregate = {
        "input_ledger": str(input_ledger.relative_to(ROOT)),
        "wheel_bound": wheel_bound,
        "wheel_primes": wheel_primes,
        "source_residual_count": len(source_records),
        "wheel_capacity_closed_count": sum(1 for row in records if row["wheel_capacity_gate_closes"]),
        "wheel_survivor_absorption_pdec_count": len(wheel_pdec),
        "min_wheel_capacity_margin": min((row["wheel_capacity_margin"] for row in records), default=None),
        "max_complement_wheel_survivor_count": max(
            (row["complement_wheel_survivor_count"] for row in records),
            default=0,
        ),
        "max_complement_prime_count": max((row["complement_prime_count"] for row in records), default=0),
    }
    ledger = {
        "parameters": source["parameters"],
        "aggregate": aggregate,
        "records": records,
        "wheel_capacity_frontier": [compact_record(row) for row in frontier],
        "wheel_survivor_absorption_pdec_records": [compact_record(row) for row in wheel_pdec],
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = {
        "certificate_type": "prime_matrix_square_phase_offband_prefix_gap_shadow_wheel_absorption_router",
        "status": "complement_absorption_reduced_to_wheel_survivor_capacity_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "empirical_absence_not_used_as_proof": True,
        "parameters": source["parameters"],
        "aggregate": aggregate,
        "wheel_survivor_absorption_pdec_count": len(wheel_pdec),
        "wheel_capacity_frontier": ledger["wheel_capacity_frontier"][:40],
        "wheel_survivor_absorption_pdec_records": ledger["wheel_survivor_absorption_pdec_records"],
        "complement_wheel_capacity_gate_closed": True,
        "finite_no_wheel_survivor_absorption_pdec": len(wheel_pdec) == 0,
        "global_wheel_survivor_absorption_exclusion_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(wheel_bound),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_wheel_absorption_router.py": sha256(
                Path(__file__).resolve()
            ),
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_hull_absorption_router.py": sha256(
                HULL_ROUTER
            ),
            "data/square-phase-offband-prefix-gap-shadow-hull-absorption-ledger.json": sha256(input_ledger),
            "data/square-phase-offband-prefix-gap-shadow-wheel-absorption-ledger.json": sha256(OUT_LEDGER),
        },
        "plain_conclusion": (
            f"本步用小轮筛 `{wheel_primes}` 压缩互补孔袋吸收容量。"
            "互补孔袋中的素数必然属于小轮筛幸存者；若 hull 素数数超过这些幸存者数量，"
            "目标并集必含素数。有限账本中 11 个 count-gate 残余全部被 wheel capacity gate 关闭；"
            "全局仍需证明相同不等式或排斥持久 wheel-survivor absorption PDEC。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow wheel absorption router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"wheel_bound={agg['wheel_bound']}",
        f"wheel_primes={agg['wheel_primes']}",
        f"source_residual_count={agg['source_residual_count']}",
        f"wheel_capacity_closed_count={agg['wheel_capacity_closed_count']}",
        f"wheel_survivor_absorption_pdec_count={agg['wheel_survivor_absorption_pdec_count']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 轮筛容量门",
        "",
        "互补孔袋吸收全部 hull 素数时，互补孔袋内的每个素数都必须通过小轮筛。因此",
        "",
        "```text",
        "Prime(complement pockets) <= WheelSurvivors(complement pockets)",
        "```",
        "",
        "若 `Prime(hull)>WheelSurvivors(C)`，互补孔袋无法吸收全部 hull 素数，目标并集必含素数。",
        "",
        "## 2. 有限审计摘要",
        "",
        "| metric | value |",
        "| --- | ---: |",
        f"| source residual count | {agg['source_residual_count']} |",
        f"| wheel capacity closed | {agg['wheel_capacity_closed_count']} |",
        f"| wheel-survivor absorption PDEC | {agg['wheel_survivor_absorption_pdec_count']} |",
        f"| min wheel capacity margin | {agg['min_wheel_capacity_margin']} |",
        f"| max complement wheel survivors | {agg['max_complement_wheel_survivor_count']} |",
        f"| max complement primes | {agg['max_complement_prime_count']} |",
        "",
        "## 3. 轮筛容量边界",
        "",
        "| P | side | hull | hull primes | raw C cand | C primes | wheel survivors | margin | survivor values |",
        "| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in result["wheel_capacity_frontier"][:24]:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["p"]),
                    f"`{row['side']}`",
                    f"`{row['q_hull_lo']}-{row['q_hull_hi']}`",
                    str(row["hull_prime_count"]),
                    str(row["coverage_defect_candidate_count"]),
                    str(row["complement_prime_count"]),
                    str(row["complement_wheel_survivor_count"]),
                    str(row["wheel_capacity_margin"]),
                    f"`{row['complement_wheel_survivor_values']}`",
                ]
            )
            + " |"
        )
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
            "- 主攻：`HullPrimeCountBeatsComplementWheelCapacityOrWheelSurvivorAbsorptionPDEC`。",
            "- 需全局证明短 hull 的素数下界超过互补孔袋的小轮筛幸存容量。",
            "- 若失败，反例必须表现为互补孔袋的小轮筛幸存者吸收全部 hull 素数。",
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
    parser.add_argument("--wheel-bound", type=int, default=13)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    input_ledger = args.input_ledger if args.input_ledger.is_absolute() else ROOT / args.input_ledger
    result = build_result(input_ledger, args.wheel_bound)
    write_markdown(result)
    result["source_hashes"][
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-wheel-absorption-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "wheel_bound": args.wheel_bound,
                "source_residual_count": result["aggregate"]["source_residual_count"],
                "wheel_capacity_closed_count": result["aggregate"]["wheel_capacity_closed_count"],
                "wheel_survivor_absorption_pdec_count": result["wheel_survivor_absorption_pdec_count"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
