#!/usr/bin/env python3
"""把 joint pressure PDEC 排斥压成总 no-slot 压力门。

用法示例：
  python3 experiments/prime_matrix_square_phase_total_noslot_pressure_gate_router.py --max-p 5000
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-total-noslot-pressure-gate-router.json

输出：
  data/square-phase-total-noslot-pressure-gate-ledger.json
  docs/monograph/prime-matrix-square-phase-total-noslot-pressure-gate-router.json
  docs/monograph/prime-matrix-square-phase-total-noslot-pressure-gate-router.md
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

OUT_LEDGER = DATA / "square-phase-total-noslot-pressure-gate-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-total-noslot-pressure-gate-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-total-noslot-pressure-gate-router.md"

MAIN_TARGET = "JointPressureCompanionPDECExclusion"
NEXT_TARGET = "TotalNoSlotPressureDefectExclusionOrTotalPressurePDEC"


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


def audit_side(split: Any, p: int, side: str, prime_flags: bytearray, pi_prefix: list[int]) -> dict[str, Any]:
    """审计单侧总 no-slot 压力门。"""
    record = split.audit_p(p, prime_flags, pi_prefix)
    prime_window = record[f"{side}_prime_window"]
    threshold = record[f"{side}_threshold_half_primewindow"]
    k0_load = record[f"{side}_k0_load"]
    kge1_load = record[f"{side}_kge1_load"]
    no_slot = record[f"{side}_no_slot_load"]
    total_pressure_defect = prime_window <= 2 * no_slot
    terminal_no_slot = no_slot >= threshold
    k0_pressure = 2 * k0_load >= threshold
    kge1_pressure = 2 * kge1_load >= threshold
    root_joint = (
        prime_window <= 4 * k0_load
        and k0_pressure
        and kge1_load >= max(0, threshold - k0_load)
    )
    kge1_joint = (
        prime_window <= 4 * kge1_load
        and kge1_pressure
        and k0_load >= max(0, threshold - kge1_load)
    )
    joint_pdec = root_joint or kge1_joint
    return {
        "p": p,
        "side": side,
        "prime_window": prime_window,
        "threshold": threshold,
        "k0_load": k0_load,
        "kge1_load": kge1_load,
        "no_slot_load": no_slot,
        "total_pressure_defect": total_pressure_defect,
        "terminal_no_slot": terminal_no_slot,
        "joint_pdec": joint_pdec,
        "total_pressure_margin": prime_window - 2 * no_slot,
        "terminal_equivalence_ok": total_pressure_defect == terminal_no_slot,
        "joint_equivalence_ok": total_pressure_defect == joint_pdec,
        "k0_pressure": k0_pressure,
        "kge1_pressure": kge1_pressure,
    }


def compact(record: dict[str, Any]) -> dict[str, Any]:
    """压缩记录字段。"""
    return {
        "p": record["p"],
        "side": record["side"],
        "prime_window": record["prime_window"],
        "threshold": record["threshold"],
        "k0_load": record["k0_load"],
        "kge1_load": record["kge1_load"],
        "no_slot_load": record["no_slot_load"],
        "total_pressure_margin": record["total_pressure_margin"],
        "total_pressure_defect": record["total_pressure_defect"],
        "terminal_no_slot": record["terminal_no_slot"],
        "joint_pdec": record["joint_pdec"],
    }


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "terminal_total_pressure_equivalence",
            "status": "closed",
            "statement": "NoSlotLoad>=ceil(PrimeWindow/2) is equivalent to PrimeWindow<=2*NoSlotLoad.",
        },
        {
            "name": "joint_pdec_total_pressure_equivalence",
            "status": "closed",
            "statement": "The joint pressure-companion PDEC is equivalent to the total no-slot pressure defect.",
        },
        {
            "name": "finite_total_pressure_absence",
            "status": "finite_evidence",
            "statement": "The finite audit finds PrimeWindow>2*NoSlotLoad for every tested P and sign.",
        },
        {
            "name": "total_pressure_defect_exclusion",
            "status": "open",
            "statement": "A global proof still needs to prove PrimeWindow>2*NoSlotLoad, or register and exclude TotalPressure-PDEC.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "TerminalEqualsTotalPressureClosed",
            "closed": result["terminal_equivalence_failure_count"] == 0,
            "proved": True,
            "meaning": "`NoSlotLoad>=ceil(W/2)` 与 `W<=2*NoSlotLoad` 是同一个整数条件。",
            "remaining": "closed",
        },
        {
            "gate": "JointPDECEqualsTotalPressureClosed",
            "closed": result["joint_equivalence_failure_count"] == 0,
            "proved": True,
            "meaning": "joint pressure-companion PDEC 与总 no-slot 压力缺陷等价。",
            "remaining": "closed",
        },
        {
            "gate": "FiniteNoTotalPressureDefect",
            "closed": result["total_pressure_defect_count"] == 0,
            "proved": False,
            "meaning": f"有限扫描 P<={result['parameters']['max_p']} 中 `PrimeWindow>2*NoSlotLoad` 全部成立。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "TotalPressureDefectExcludedGlobally",
            "closed": False,
            "proved": False,
            "meaning": "仍需全局排斥总 no-slot 压力缺陷。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只把 joint PDEC 排斥压成单一标量不等式，不关闭全局行/列命题。",
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
    total_pressure_records = [record for record in records if record["total_pressure_defect"]]
    terminal_records = [record for record in records if record["terminal_no_slot"]]
    joint_records = [record for record in records if record["joint_pdec"]]
    terminal_failures = [record for record in records if not record["terminal_equivalence_ok"]]
    joint_failures = [record for record in records if not record["joint_equivalence_ok"]]
    worst_margin = min(records, key=lambda record: record["total_pressure_margin"], default=None)
    best_margin = max(records, key=lambda record: record["total_pressure_margin"], default=None)
    sample_set = set(sample_ps)
    sample_records = [record for record in records if record["p"] in sample_set]
    aggregate = {
        "record_count": len(records),
        "combined_prime_window": sum(record["prime_window"] for record in records),
        "combined_no_slot_load": sum(record["no_slot_load"] for record in records),
        "terminal_equivalence_failure_count": len(terminal_failures),
        "joint_equivalence_failure_count": len(joint_failures),
        "total_pressure_defect_count": len(total_pressure_records),
        "terminal_no_slot_count": len(terminal_records),
        "joint_pdec_count": len(joint_records),
        "min_total_pressure_margin": worst_margin["total_pressure_margin"] if worst_margin else None,
        "max_total_pressure_margin": best_margin["total_pressure_margin"] if best_margin else None,
    }
    ledger = {
        "parameters": {"max_p": max_p, "sample_ps": sample_ps},
        "prime_count": len(p_values),
        "aggregate": aggregate,
        "worst_margin_record": compact(worst_margin) if worst_margin else None,
        "best_margin_record": compact(best_margin) if best_margin else None,
        "total_pressure_records": [compact(record) for record in total_pressure_records[:120]],
        "terminal_records": [compact(record) for record in terminal_records[:80]],
        "joint_records": [compact(record) for record in joint_records[:80]],
        "terminal_equivalence_failures": [compact(record) for record in terminal_failures[:40]],
        "joint_equivalence_failures": [compact(record) for record in joint_failures[:40]],
        "sample_records": [compact(record) for record in sample_records],
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = {
        "certificate_type": "prime_matrix_square_phase_total_noslot_pressure_gate_router",
        "status": "joint_pressure_pdec_reduced_to_total_noslot_pressure_defect_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "empirical_absence_not_used_as_proof": True,
        "parameters": ledger["parameters"],
        "finite_prime_count": len(p_values),
        "aggregate": aggregate,
        "terminal_equivalence_failure_count": len(terminal_failures),
        "joint_equivalence_failure_count": len(joint_failures),
        "total_pressure_defect_count": len(total_pressure_records),
        "terminal_no_slot_count": len(terminal_records),
        "joint_pdec_count": len(joint_records),
        "worst_margin_record": ledger["worst_margin_record"],
        "best_margin_record": ledger["best_margin_record"],
        "sample_records": ledger["sample_records"],
        "terminal_total_pressure_equivalence_closed": len(terminal_failures) == 0,
        "joint_pdec_total_pressure_equivalence_closed": len(joint_failures) == 0,
        "total_pressure_defect_excluded_globally": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_total_noslot_pressure_gate_router.py": sha256(
                Path(__file__).resolve()
            ),
            "experiments/prime_matrix_square_phase_noslot_k0_rootwindow_split_router.py": sha256(
                SPLIT_ROUTER
            ),
            "data/square-phase-total-noslot-pressure-gate-ledger.json": sha256(OUT_LEDGER),
        },
        "plain_conclusion": (
            "本步把 `JointPressureCompanionPDECExclusion` 压成单一标量门："
            "终端 no-slot 反例、joint pressure-companion PDEC、以及 `PrimeWindow<=2*NoSlotLoad` "
            "三者是同一个整数条件的不同写法。"
            "因此最新最窄剩余是证明 `PrimeWindow>2*NoSlotLoad`，"
            "或将其失败登记并排斥为 TotalPressure-PDEC。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase total no-slot pressure gate router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"max_p={result['parameters']['max_p']}",
        f"finite_prime_count={result['finite_prime_count']}",
        f"terminal_equivalence_failure_count={result['terminal_equivalence_failure_count']}",
        f"joint_equivalence_failure_count={result['joint_equivalence_failure_count']}",
        f"total_pressure_defect_count={result['total_pressure_defect_count']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 单一标量门",
        "",
        "令 `W=PrimeWindow`，`N=NoSlotLoad=K0Load+KGe1Load`。由于 `N` 为整数，",
        "",
        "```text",
        "N >= ceil(W/2)    iff    W <= 2N.",
        "```",
        "",
        "因此排斥终端 no-slot 反例等价于证明",
        "",
        "```text",
        "PrimeWindow > 2*NoSlotLoad.",
        "```",
        "",
        "这也等价于排斥上一层 joint pressure-companion PDEC。",
        "",
        "## 2. 有限审计摘要",
        "",
        "| metric | value |",
        "| --- | ---: |",
        f"| record count | {agg['record_count']} |",
        f"| combined PrimeWindow | {agg['combined_prime_window']} |",
        f"| combined NoSlotLoad | {agg['combined_no_slot_load']} |",
        f"| terminal equivalence failures | {agg['terminal_equivalence_failure_count']} |",
        f"| joint equivalence failures | {agg['joint_equivalence_failure_count']} |",
        f"| total pressure defects | {agg['total_pressure_defect_count']} |",
        f"| terminal no-slot count | {agg['terminal_no_slot_count']} |",
        f"| joint PDEC count | {agg['joint_pdec_count']} |",
        f"| min total pressure margin | {agg['min_total_pressure_margin']} |",
        f"| max total pressure margin | {agg['max_total_pressure_margin']} |",
        "",
        "## 3. 边界记录",
        "",
        "| label | P | side | PrimeWindow | K0 | KGe1 | NoSlot | margin W-2N | terminal | joint |",
        "| --- | ---: | --- | ---: | ---: | ---: | ---: | ---: | --- | --- |",
    ]
    for label, record in [
        ("worst margin", result["worst_margin_record"]),
        ("best margin", result["best_margin_record"]),
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
                    str(record["total_pressure_margin"]),
                    f"`{fmt_bool(record['terminal_no_slot'])}`",
                    f"`{fmt_bool(record['joint_pdec'])}`",
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
            "- 主攻：`TotalNoSlotPressureDefectExclusionOrTotalPressurePDEC`。",
            "- 也就是证明 `PrimeWindow>2*NoSlotLoad`；若失败，登记总压力 PDEC 并继续向相位/短簇结构投影。",
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
    result["source_hashes"]["docs/monograph/prime-matrix-square-phase-total-noslot-pressure-gate-router.md"] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(
        {
            "status": result["status"],
            "max_p": args.max_p,
            "total_pressure_defect_count": result["total_pressure_defect_count"],
            "terminal_equivalence_failure_count": result["terminal_equivalence_failure_count"],
            "next_direct_attack_target": result["next_direct_attack_target"],
            "row_column_unconditional_closed": result["row_column_unconditional_closed"],
        },
        ensure_ascii=False,
        indent=2,
    ))


if __name__ == "__main__":
    main()
