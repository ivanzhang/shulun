#!/usr/bin/env python3
"""合并 k0 与 k>=1 的终端压力缺陷前沿。

用法示例：
  python3 experiments/prime_matrix_square_phase_terminal_pressure_frontier_router.py --max-p 5000
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-terminal-pressure-frontier-router.json

输出：
  data/square-phase-terminal-pressure-frontier-ledger.json
  docs/monograph/prime-matrix-square-phase-terminal-pressure-frontier-router.json
  docs/monograph/prime-matrix-square-phase-terminal-pressure-frontier-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SPLIT_ROUTER = ROOT / "experiments" / "prime_matrix_square_phase_noslot_k0_rootwindow_split_router.py"

OUT_LEDGER = DATA / "square-phase-terminal-pressure-frontier-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-terminal-pressure-frontier-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-terminal-pressure-frontier-router.md"

MAIN_TARGET = (
    "PrimeSquareEndpointCountGt2SqrtPOrRootWindowPDEC "
    "AND KGe1AggregatePressureDefectOrMovingLayerPDEC"
)
NEXT_TARGET = "TerminalPressureDefectDichotomyPDECExclusion"


def load_split_router() -> Any:
    """加载 k0/k>=1 分裂路由器。"""
    spec = importlib.util.spec_from_file_location("noslot_k0_split_router", SPLIT_ROUTER)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {SPLIT_ROUTER}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def compact(record: dict[str, Any]) -> dict[str, Any]:
    """压缩报告字段。"""
    return {
        "p": record["p"],
        "side": record["side"],
        "prime_window": record["prime_window"],
        "threshold": record["threshold"],
        "k0_load": record["k0_load"],
        "kge1_load": record["kge1_load"],
        "no_slot_load": record["no_slot_load"],
        "k0_pressure": record["k0_pressure"],
        "kge1_pressure": record["kge1_pressure"],
        "terminal_no_slot": record["terminal_no_slot"],
        "terminal_forces_pressure_defect": record["terminal_forces_pressure_defect"],
        "root_defect": record["root_defect"],
        "kge1_defect": record["kge1_defect"],
        "margin_vs_4k0": record["margin_vs_4k0"],
        "margin_vs_4kge1": record["margin_vs_4kge1"],
        "margin_vs_4max": record["margin_vs_4max"],
    }


def audit_side(split: Any, p: int, side: str, prime_flags: bytearray, pi_prefix: list[int]) -> dict[str, Any]:
    """审计单侧终端压力前沿。"""
    record = split.audit_p(p, prime_flags, pi_prefix)
    prime_window = record[f"{side}_prime_window"]
    threshold = record[f"{side}_threshold_half_primewindow"]
    k0_load = record[f"{side}_k0_load"]
    kge1_load = record[f"{side}_kge1_load"]
    no_slot_load = record[f"{side}_no_slot_load"]
    terminal_no_slot = no_slot_load >= threshold
    k0_pressure = 2 * k0_load >= threshold
    kge1_pressure = 2 * kge1_load >= threshold
    root_defect = prime_window <= 4 * k0_load
    kge1_defect = prime_window <= 4 * kge1_load
    terminal_forces_pressure = (not terminal_no_slot) or k0_pressure or kge1_pressure
    pressure_forces_defect = (not k0_pressure or root_defect) and (not kge1_pressure or kge1_defect)
    terminal_forces_defect = (not terminal_no_slot) or root_defect or kge1_defect
    return {
        "p": p,
        "side": side,
        "prime_window": prime_window,
        "threshold": threshold,
        "k0_load": k0_load,
        "kge1_load": kge1_load,
        "no_slot_load": no_slot_load,
        "terminal_no_slot": terminal_no_slot,
        "k0_pressure": k0_pressure,
        "kge1_pressure": kge1_pressure,
        "root_defect": root_defect,
        "kge1_defect": kge1_defect,
        "terminal_forces_pressure_branch": terminal_forces_pressure,
        "pressure_branch_forces_named_defect": pressure_forces_defect,
        "terminal_forces_pressure_defect": terminal_forces_defect,
        "margin_vs_4k0": prime_window - 4 * k0_load,
        "margin_vs_4kge1": prime_window - 4 * kge1_load,
        "margin_vs_4max": prime_window - 4 * max(k0_load, kge1_load),
    }


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "terminal_noslot_forces_pressure_branch",
            "status": "closed",
            "statement": "If NoSlotLoad reaches the split threshold, then k0 or k>=1 carries half the threshold.",
        },
        {
            "name": "pressure_branch_forces_named_defect",
            "status": "closed",
            "statement": "A k0 pressure branch forces PrimeWindow<=4*RootLoad; a k>=1 pressure branch forces PrimeWindow<=4*KGe1Load.",
        },
        {
            "name": "terminal_pressure_defect_dichotomy",
            "status": "closed",
            "statement": "Any terminal no-slot counterexample must produce RootWindowDefect or KGe1AggregatePressureDefect.",
        },
        {
            "name": "named_pressure_defect_exclusion",
            "status": "open",
            "statement": "A global proof still needs to exclude both named pressure defects, or register and reject their PDEC/SAE families.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "SplitPressureDichotomyClosed",
            "closed": result["terminal_pressure_branch_failure_count"] == 0,
            "proved": True,
            "meaning": "终端 no-slot 分支必落入 k0 或 k>=1 压力分支。",
            "remaining": "closed",
        },
        {
            "gate": "PressureBranchToNamedDefectClosed",
            "closed": result["pressure_to_defect_failure_count"] == 0,
            "proved": True,
            "meaning": "压力分支必给出 RootWindowDefect 或 KGe1AggregatePressureDefect。",
            "remaining": "closed",
        },
        {
            "gate": "TerminalPressureDefectDichotomyClosed",
            "closed": result["terminal_to_named_defect_failure_count"] == 0,
            "proved": True,
            "meaning": "任意终端 no-slot 反例都必须进入两个命名压力缺陷之一。",
            "remaining": "closed",
        },
        {
            "gate": "FiniteNoTerminalNoSlotBranch",
            "closed": result["terminal_no_slot_count"] == 0,
            "proved": False,
            "meaning": f"有限扫描 P<={result['parameters']['max_p']} 未出现终端 no-slot 分支。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "RootWindowDefectExcludedGlobally",
            "closed": False,
            "proved": False,
            "meaning": "仍需排斥 RootWindowDefect，或证明 PrimeSquareEndpointCountGt2SqrtP。",
            "remaining": "PrimeSquareEndpointCountGt2SqrtPOrRootWindowPDEC",
        },
        {
            "gate": "KGe1AggregatePressureDefectExcludedGlobally",
            "closed": False,
            "proved": False,
            "meaning": "仍需排斥 KGe1AggregatePressureDefect 或登记并排斥 MovingLayer-PDEC。",
            "remaining": "KGe1AggregatePressureDefectOrMovingLayerPDEC",
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只关闭终端压力缺陷二分，不关闭全局行/列命题。",
            "remaining": NEXT_TARGET,
        },
    ]


def build_result(max_p: int, sample_ps: list[int]) -> dict[str, Any]:
    """构造路由器结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    split = load_split_router()
    prime_flags = split.sieve(max_p * max_p + max_p)
    pi_prefix = split.prime_prefix(prime_flags)
    small_flags = split.sieve(max_p)
    p_values = [p for p in range(3, max_p + 1) if small_flags[p]]
    records = [
        audit_side(split, p, side, prime_flags, pi_prefix)
        for p in p_values
        for side in ("plus", "minus")
    ]
    sample_set = set(sample_ps)
    sample_records = [record for record in records if record["p"] in sample_set]
    terminal_pressure_failures = [
        record for record in records if not record["terminal_forces_pressure_branch"]
    ]
    pressure_to_defect_failures = [
        record for record in records if not record["pressure_branch_forces_named_defect"]
    ]
    terminal_to_defect_failures = [
        record for record in records if not record["terminal_forces_pressure_defect"]
    ]
    terminal_records = [record for record in records if record["terminal_no_slot"]]
    root_defects = [record for record in records if record["root_defect"]]
    kge1_defects = [record for record in records if record["kge1_defect"]]
    pressure_records = [
        record for record in records if record["k0_pressure"] or record["kge1_pressure"]
    ]
    worst_vs_4max = min(records, key=lambda record: record["margin_vs_4max"], default=None)
    worst_root = min(records, key=lambda record: record["margin_vs_4k0"], default=None)
    worst_kge1 = min(records, key=lambda record: record["margin_vs_4kge1"], default=None)

    aggregate = {
        "record_count": len(records),
        "combined_prime_window": sum(record["prime_window"] for record in records),
        "combined_k0_load": sum(record["k0_load"] for record in records),
        "combined_kge1_load": sum(record["kge1_load"] for record in records),
        "combined_no_slot_load": sum(record["no_slot_load"] for record in records),
        "terminal_pressure_branch_failure_count": len(terminal_pressure_failures),
        "pressure_to_defect_failure_count": len(pressure_to_defect_failures),
        "terminal_to_named_defect_failure_count": len(terminal_to_defect_failures),
        "terminal_no_slot_count": len(terminal_records),
        "root_defect_count": len(root_defects),
        "kge1_defect_count": len(kge1_defects),
        "pressure_branch_count": len(pressure_records),
        "min_margin_vs_4max": worst_vs_4max["margin_vs_4max"] if worst_vs_4max else None,
        "min_margin_vs_4root": worst_root["margin_vs_4k0"] if worst_root else None,
        "min_margin_vs_4kge1": worst_kge1["margin_vs_4kge1"] if worst_kge1 else None,
    }
    ledger = {
        "parameters": {"max_p": max_p, "sample_ps": sample_ps},
        "prime_count": len(p_values),
        "aggregate": aggregate,
        "terminal_pressure_branch_failure_count": len(terminal_pressure_failures),
        "pressure_to_defect_failure_count": len(pressure_to_defect_failures),
        "terminal_to_named_defect_failure_count": len(terminal_to_defect_failures),
        "terminal_no_slot_count": len(terminal_records),
        "root_defect_count": len(root_defects),
        "kge1_defect_count": len(kge1_defects),
        "pressure_branch_count": len(pressure_records),
        "worst_vs_4max_record": compact(worst_vs_4max) if worst_vs_4max else None,
        "worst_root_record": compact(worst_root) if worst_root else None,
        "worst_kge1_record": compact(worst_kge1) if worst_kge1 else None,
        "terminal_records": [compact(record) for record in terminal_records[:50]],
        "root_defect_records": [compact(record) for record in root_defects[:80]],
        "kge1_defect_records": [compact(record) for record in kge1_defects[:80]],
        "pressure_records": [compact(record) for record in pressure_records[:120]],
        "sample_records": [compact(record) for record in sample_records],
        "terminal_pressure_failures": [compact(record) for record in terminal_pressure_failures[:20]],
        "pressure_to_defect_failures": [compact(record) for record in pressure_to_defect_failures[:20]],
        "terminal_to_defect_failures": [compact(record) for record in terminal_to_defect_failures[:20]],
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    result = {
        "certificate_type": "prime_matrix_square_phase_terminal_pressure_frontier_router",
        "status": "terminal_noslot_counterexample_reduced_to_two_named_pressure_defects_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "empirical_absence_not_used_as_proof": True,
        "parameters": ledger["parameters"],
        "finite_prime_count": len(p_values),
        "aggregate": aggregate,
        "terminal_pressure_branch_failure_count": len(terminal_pressure_failures),
        "pressure_to_defect_failure_count": len(pressure_to_defect_failures),
        "terminal_to_named_defect_failure_count": len(terminal_to_defect_failures),
        "terminal_no_slot_count": len(terminal_records),
        "root_defect_count": len(root_defects),
        "kge1_defect_count": len(kge1_defects),
        "pressure_branch_count": len(pressure_records),
        "worst_vs_4max_record": ledger["worst_vs_4max_record"],
        "worst_root_record": ledger["worst_root_record"],
        "worst_kge1_record": ledger["worst_kge1_record"],
        "sample_records": ledger["sample_records"],
        "terminal_pressure_dichotomy_closed": len(terminal_pressure_failures) == 0,
        "pressure_branch_to_named_defect_closed": len(pressure_to_defect_failures) == 0,
        "terminal_to_named_defect_closed": len(terminal_to_defect_failures) == 0,
        "rootwindow_defect_excluded_globally": False,
        "kge1_aggregate_pressure_defect_excluded_globally": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_terminal_pressure_frontier_router.py": sha256(
                Path(__file__).resolve()
            ),
            "experiments/prime_matrix_square_phase_noslot_k0_rootwindow_split_router.py": sha256(
                SPLIT_ROUTER
            ),
            "data/square-phase-terminal-pressure-frontier-ledger.json": sha256(OUT_LEDGER),
        },
        "plain_conclusion": (
            "本步把当前平方锚 no-slot 剩余合并成一个终端压力前沿："
            "若终端 no-slot 反例存在，则 split 二分强制 k0 或 k>=1 承担半阈值；"
            "前者给出 `PrimeWindow<=4*RootLoad`，后者给出 `PrimeWindow<=4*KGe1Load`。"
            "因此任何终端 no-slot 反例必须进入 RootWindowDefect 或 KGe1AggregatePressureDefect。"
            "这关闭的是最后出口的逻辑二分，不是两个命名缺陷的全局排斥。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase terminal pressure frontier router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"max_p={result['parameters']['max_p']}",
        f"finite_prime_count={result['finite_prime_count']}",
        f"terminal_pressure_branch_failure_count={result['terminal_pressure_branch_failure_count']}",
        f"pressure_to_defect_failure_count={result['pressure_to_defect_failure_count']}",
        f"terminal_to_named_defect_failure_count={result['terminal_to_named_defect_failure_count']}",
        f"terminal_no_slot_count={result['terminal_no_slot_count']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 终端二分",
        "",
        "若 no-slot 分支达到终端压力，即",
        "",
        "```text",
        "NoSlotLoad >= ceil(PrimeWindow/2),",
        "```",
        "",
        "而 `NoSlotLoad=K0Load+KGe1Load`，则至少一个分支满足",
        "",
        "```text",
        "2*K0Load >= ceil(PrimeWindow/2)",
        "或",
        "2*KGe1Load >= ceil(PrimeWindow/2).",
        "```",
        "",
        "于是终端反例强制进入两个命名缺陷之一：",
        "",
        "```text",
        "RootWindowDefect:        PrimeWindow <= 4*RootLoad",
        "KGe1AggregateDefect:    PrimeWindow <= 4*KGe1Load",
        "```",
        "",
        "## 2. 有限审计摘要",
        "",
        "| metric | value |",
        "| --- | ---: |",
        f"| combined PrimeWindow | {agg['combined_prime_window']} |",
        f"| combined K0Load | {agg['combined_k0_load']} |",
        f"| combined KGe1Load | {agg['combined_kge1_load']} |",
        f"| combined NoSlotLoad | {agg['combined_no_slot_load']} |",
        f"| pressure branch failures | {agg['terminal_pressure_branch_failure_count']} |",
        f"| pressure-to-defect failures | {agg['pressure_to_defect_failure_count']} |",
        f"| terminal-to-defect failures | {agg['terminal_to_named_defect_failure_count']} |",
        f"| terminal no-slot count | {agg['terminal_no_slot_count']} |",
        f"| root defect count | {agg['root_defect_count']} |",
        f"| k>=1 defect count | {agg['kge1_defect_count']} |",
        f"| pressure branch count | {agg['pressure_branch_count']} |",
        f"| min margin vs 4max | {agg['min_margin_vs_4max']} |",
        "",
        "## 3. 关键记录",
        "",
        "| label | P | side | PrimeWindow | K0 | KGe1 | NoSlot | root defect | k>=1 defect | terminal | margin vs 4max |",
        "| --- | ---: | --- | ---: | ---: | ---: | ---: | --- | --- | --- | ---: |",
    ]
    for label, record in [
        ("worst vs 4max", result["worst_vs_4max_record"]),
        ("worst root", result["worst_root_record"]),
        ("worst k>=1", result["worst_kge1_record"]),
    ]:
        if not record:
            continue
        lines.append(
            "| "
            + " | ".join(
                [
                    table_cell(label),
                    str(record["p"]),
                    table_cell(record["side"]),
                    str(record["prime_window"]),
                    str(record["k0_load"]),
                    str(record["kge1_load"]),
                    str(record["no_slot_load"]),
                    f"`{fmt_bool(record['root_defect'])}`",
                    f"`{fmt_bool(record['kge1_defect'])}`",
                    f"`{fmt_bool(record['terminal_no_slot'])}`",
                    str(record["margin_vs_4max"]),
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
            "- 主攻：`TerminalPressureDefectDichotomyPDECExclusion`。",
            "- 具体仍是两门：`PrimeSquareEndpointCountGt2SqrtPOrRootWindowPDEC` 与 `KGe1AggregatePressureDefectOrMovingLayerPDEC`。",
            "- 当前已闭合终端出口二分，但还没有排斥两个命名缺陷，不能称全局无条件闭合。",
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
    parser.add_argument("--max-p", type=int, default=5000)
    parser.add_argument(
        "--sample-ps",
        type=str,
        default="13,17,19,23,29,31,73,101,499,523,1009,2003,4999",
    )
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    sample_ps = [int(item) for item in args.sample_ps.split(",") if item.strip()]
    result = build_result(args.max_p, sample_ps)
    write_markdown(result)
    result["source_hashes"]["docs/monograph/prime-matrix-square-phase-terminal-pressure-frontier-router.md"] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(
        {
            "status": result["status"],
            "max_p": args.max_p,
            "terminal_to_named_defect_failure_count": result["terminal_to_named_defect_failure_count"],
            "terminal_no_slot_count": result["terminal_no_slot_count"],
            "next_direct_attack_target": result["next_direct_attack_target"],
            "row_column_unconditional_closed": result["row_column_unconditional_closed"],
        },
        ensure_ascii=False,
        indent=2,
    ))


if __name__ == "__main__":
    main()
