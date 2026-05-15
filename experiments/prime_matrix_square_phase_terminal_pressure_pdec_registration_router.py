#!/usr/bin/env python3
"""登记终端压力二分产生的 RootWindow/KGe1 PDEC family。

用法示例：
  python3 experiments/prime_matrix_square_phase_terminal_pressure_pdec_registration_router.py --max-p 5000
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-terminal-pressure-pdec-registration-router.json

输出：
  data/square-phase-terminal-pressure-pdec-registration-ledger.json
  docs/monograph/prime-matrix-square-phase-terminal-pressure-pdec-registration-router.json
  docs/monograph/prime-matrix-square-phase-terminal-pressure-pdec-registration-router.md
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
ROOTDEF_ROUTER = ROOT / "experiments" / "prime_matrix_square_phase_k0_rootwindow_defect_router.py"

OUT_LEDGER = DATA / "square-phase-terminal-pressure-pdec-registration-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-terminal-pressure-pdec-registration-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-terminal-pressure-pdec-registration-router.md"

MAIN_TARGET = "TerminalPressureDefectDichotomyPDECExclusion"
NEXT_TARGET = "RootWindowPDECAndMovingLayerPDECExclusion"


def load_module(path: Path, name: str) -> Any:
    """按路径加载模块。"""
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
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


def top_kge1_atoms(split: Any, p: int, side: str, prime_flags: bytearray, pi_prefix: list[int], limit: int = 5) -> list[dict[str, Any]]:
    """返回 k>=1 moving-layer 中 prime-load 最大的若干原子。"""
    atoms = [atom for atom in split.formula_atoms_for_side(p, side, prime_flags, pi_prefix) if atom["k"] >= 1]
    atoms.sort(key=lambda atom: (atom["prime_load"], atom["length"]), reverse=True)
    return [
        {
            "k": atom["k"],
            "b_interval": [atom["b_lo"], atom["b_hi"]],
            "q_interval": [atom["q_lo"], atom["q_hi"]],
            "length": atom["length"],
            "prime_load": atom["prime_load"],
            "q_values": atom["q_values"],
        }
        for atom in atoms[:limit]
    ]


def make_root_pdec(rootdef: Any, p: int, side: str, prime_flags: bytearray) -> dict[str, Any] | None:
    """生成 RootWindowDefect-PDEC 记录；若不是缺陷则返回 None。"""
    root = rootdef.root_load(p, side, prime_flags)
    prime_window = rootdef.square_prime_count(p, side, prime_flags)
    no_slot = rootdef.no_slot_load(p, side, prime_flags)
    threshold = (prime_window + 1) // 2
    root_load = root["root_load"]
    if prime_window > 4 * root_load:
        return None
    return {
        "family": "RootWindowDefectPDEC",
        "formal_unit": f"P={p}|side={side}|branch=k0|q=[{root['q_lo']},{root['q_hi']}]",
        "p": p,
        "side": side,
        "branch": "k0",
        "prime_window": prime_window,
        "threshold": threshold,
        "branch_load": root_load,
        "no_slot_load": no_slot,
        "terminal_no_slot": no_slot >= threshold,
        "pressure_branch": 2 * root_load >= threshold,
        "defect_inequality": "PrimeWindow<=4*RootLoad",
        "defect_margin": prime_window - 4 * root_load,
        "root_b_interval": [root["b_lo"], root["b_hi"]],
        "root_q_interval": [root["q_lo"], root["q_hi"]],
        "root_primes": root["root_primes"],
    }


def make_kge1_pdec(split: Any, p: int, side: str, prime_flags: bytearray, pi_prefix: list[int]) -> dict[str, Any] | None:
    """生成 KGe1AggregatePressureDefect-PDEC 记录；若不是缺陷则返回 None。"""
    record = split.audit_p(p, prime_flags, pi_prefix)
    prime_window = record[f"{side}_prime_window"]
    threshold = record[f"{side}_threshold_half_primewindow"]
    kge1_load = record[f"{side}_kge1_load"]
    k0_load = record[f"{side}_k0_load"]
    no_slot = record[f"{side}_no_slot_load"]
    if prime_window > 4 * kge1_load:
        return None
    return {
        "family": "KGe1AggregatePressureDefectPDEC",
        "formal_unit": f"P={p}|side={side}|branch=k>=1|K1={kge1_load}",
        "p": p,
        "side": side,
        "branch": "k>=1",
        "prime_window": prime_window,
        "threshold": threshold,
        "branch_load": kge1_load,
        "k0_load": k0_load,
        "no_slot_load": no_slot,
        "terminal_no_slot": no_slot >= threshold,
        "pressure_branch": 2 * kge1_load >= threshold,
        "defect_inequality": "PrimeWindow<=4*KGe1Load",
        "defect_margin": prime_window - 4 * kge1_load,
        "top_atoms": top_kge1_atoms(split, p, side, prime_flags, pi_prefix),
    }


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "rootwindow_pdec_schema",
            "status": "closed",
            "statement": "Every RootWindow pressure defect is registered with P, side, root q-window, load, margin, and terminal flag.",
        },
        {
            "name": "kge1_aggregate_pdec_schema",
            "status": "closed",
            "statement": "Every k>=1 aggregate pressure defect is registered with P, side, aggregate load, top moving atoms, margin, and terminal flag.",
        },
        {
            "name": "terminal_defect_has_registered_family",
            "status": "closed",
            "statement": "Any terminal no-slot counterexample enters one of the two registered PDEC families.",
        },
        {
            "name": "registered_pressure_pdec_exclusion",
            "status": "open",
            "statement": "A global proof still needs to exclude the registered RootWindow and MovingLayer PDEC families.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "RootWindowPDECSchemaClosed",
            "closed": True,
            "proved": True,
            "meaning": "RootWindowDefect 已有固定 formal-unit 字段和缺陷不等式。",
            "remaining": "closed",
        },
        {
            "gate": "KGe1MovingLayerPDECSchemaClosed",
            "closed": True,
            "proved": True,
            "meaning": "KGe1AggregatePressureDefect 已有固定 formal-unit 字段和 top moving atoms。",
            "remaining": "closed",
        },
        {
            "gate": "FiniteRegisteredPressureDefectsNonterminal",
            "closed": result["terminal_registered_pdec_count"] == 0,
            "proved": False,
            "meaning": f"有限扫描 P<={result['parameters']['max_p']} 中已登记压力缺陷均非终端 no-slot。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "RegisteredRootWindowPDECExcludedGlobally",
            "closed": False,
            "proved": False,
            "meaning": "仍需证明 RootWindowDefect family 不能在终端反例链中持久出现。",
            "remaining": "PrimeSquareEndpointCountGt2SqrtPOrRootWindowPDEC",
        },
        {
            "gate": "RegisteredKGe1MovingLayerPDECExcludedGlobally",
            "closed": False,
            "proved": False,
            "meaning": "仍需证明 KGe1AggregatePressureDefect family 不能在终端反例链中持久出现。",
            "remaining": "KGe1AggregatePressureDefectOrMovingLayerPDEC",
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只登记缺陷 family，不关闭全局行/列命题。",
            "remaining": NEXT_TARGET,
        },
    ]


def build_result(max_p: int, sample_ps: list[int]) -> dict[str, Any]:
    """构造路由器结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    split = load_module(SPLIT_ROUTER, "noslot_k0_split_router")
    rootdef = load_module(ROOTDEF_ROUTER, "k0_rootwindow_defect_router")
    prime_flags = split.sieve(max_p * max_p + max_p)
    pi_prefix = split.prime_prefix(prime_flags)
    small_flags = split.sieve(max_p)
    p_values = [p for p in range(3, max_p + 1) if small_flags[p]]

    root_records: list[dict[str, Any]] = []
    kge1_records: list[dict[str, Any]] = []
    for p in p_values:
        for side in ("plus", "minus"):
            root_record = make_root_pdec(rootdef, p, side, prime_flags)
            if root_record:
                root_records.append(root_record)
            kge1_record = make_kge1_pdec(split, p, side, prime_flags, pi_prefix)
            if kge1_record:
                kge1_records.append(kge1_record)

    all_records = root_records + kge1_records
    terminal_records = [record for record in all_records if record["terminal_no_slot"]]
    pressure_records = [record for record in all_records if record["pressure_branch"]]
    worst_record = min(all_records, key=lambda record: record["defect_margin"], default=None)
    sample_set = set(sample_ps)
    sample_records = [record for record in all_records if record["p"] in sample_set]

    aggregate = {
        "registered_pdec_count": len(all_records),
        "rootwindow_pdec_count": len(root_records),
        "kge1_pdec_count": len(kge1_records),
        "registered_pressure_branch_count": len(pressure_records),
        "terminal_registered_pdec_count": len(terminal_records),
        "min_defect_margin": worst_record["defect_margin"] if worst_record else None,
    }
    ledger = {
        "parameters": {"max_p": max_p, "sample_ps": sample_ps},
        "prime_count": len(p_values),
        "aggregate": aggregate,
        "rootwindow_pdec_records": root_records[:120],
        "kge1_pdec_records": kge1_records[:120],
        "terminal_registered_pdec_records": terminal_records[:80],
        "pressure_branch_records": pressure_records[:120],
        "worst_registered_pdec_record": worst_record,
        "sample_records": sample_records,
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    result = {
        "certificate_type": "prime_matrix_square_phase_terminal_pressure_pdec_registration_router",
        "status": "terminal_pressure_defects_registered_pdec_families_exclusion_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "empirical_absence_not_used_as_proof": True,
        "parameters": ledger["parameters"],
        "finite_prime_count": len(p_values),
        "aggregate": aggregate,
        "registered_pdec_count": len(all_records),
        "rootwindow_pdec_count": len(root_records),
        "kge1_pdec_count": len(kge1_records),
        "terminal_registered_pdec_count": len(terminal_records),
        "registered_pressure_branch_count": len(pressure_records),
        "worst_registered_pdec_record": worst_record,
        "sample_records": sample_records,
        "rootwindow_pdec_schema_closed": True,
        "kge1_movinglayer_pdec_schema_closed": True,
        "terminal_defect_has_registered_family_closed": True,
        "registered_pressure_pdec_excluded_globally": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_terminal_pressure_pdec_registration_router.py": sha256(
                Path(__file__).resolve()
            ),
            "experiments/prime_matrix_square_phase_noslot_k0_rootwindow_split_router.py": sha256(
                SPLIT_ROUTER
            ),
            "experiments/prime_matrix_square_phase_k0_rootwindow_defect_router.py": sha256(
                ROOTDEF_ROUTER
            ),
            "data/square-phase-terminal-pressure-pdec-registration-ledger.json": sha256(OUT_LEDGER),
        },
        "plain_conclusion": (
            "本步把终端压力二分的两个出口登记为可审查 PDEC family："
            "RootWindowDefect 记录 P、side、根窗 q 区间、负载和 margin；"
            "KGe1AggregatePressureDefect 记录 P、side、聚合负载、top moving atoms 和 margin。"
            "因此任何终端 no-slot 反例若出现，不再是无名失败，而必须落入这两个已登记 family。"
            "全局仍需排斥这些 family，不能声称命题已无条件闭合。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    worst = result["worst_registered_pdec_record"]
    lines = [
        "# Prime Matrix square-phase terminal pressure PDEC registration router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"max_p={result['parameters']['max_p']}",
        f"finite_prime_count={result['finite_prime_count']}",
        f"registered_pdec_count={result['registered_pdec_count']}",
        f"rootwindow_pdec_count={result['rootwindow_pdec_count']}",
        f"kge1_pdec_count={result['kge1_pdec_count']}",
        f"terminal_registered_pdec_count={result['terminal_registered_pdec_count']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. PDEC family",
        "",
        "| family | registered fields | defect inequality |",
        "| --- | --- | --- |",
        "| `RootWindowDefectPDEC` | `P, side, root_q_interval, root_b_interval, RootLoad, PrimeWindow, terminal flag` | `PrimeWindow<=4*RootLoad` |",
        "| `KGe1AggregatePressureDefectPDEC` | `P, side, KGe1Load, top moving atoms, PrimeWindow, terminal flag` | `PrimeWindow<=4*KGe1Load` |",
        "",
        "## 2. 有限登记摘要",
        "",
        "| metric | value |",
        "| --- | ---: |",
        f"| registered PDEC count | {agg['registered_pdec_count']} |",
        f"| RootWindow PDEC count | {agg['rootwindow_pdec_count']} |",
        f"| KGe1 PDEC count | {agg['kge1_pdec_count']} |",
        f"| pressure-branch registered count | {agg['registered_pressure_branch_count']} |",
        f"| terminal registered count | {agg['terminal_registered_pdec_count']} |",
        f"| min defect margin | {agg['min_defect_margin']} |",
        "",
        "## 3. 最坏登记样本",
        "",
        "| family | P | side | branch | PrimeWindow | branch load | no-slot | pressure | terminal | margin | formal unit |",
        "| --- | ---: | --- | --- | ---: | ---: | ---: | --- | --- | ---: | --- |",
    ]
    if worst:
        lines.append(
            "| "
            + " | ".join(
                [
                    table_cell(worst["family"]),
                    str(worst["p"]),
                    table_cell(worst["side"]),
                    table_cell(worst["branch"]),
                    str(worst["prime_window"]),
                    str(worst["branch_load"]),
                    str(worst["no_slot_load"]),
                    f"`{fmt_bool(worst['pressure_branch'])}`",
                    f"`{fmt_bool(worst['terminal_no_slot'])}`",
                    str(worst["defect_margin"]),
                    table_cell(worst["formal_unit"]),
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
            "- 主攻：`RootWindowPDECAndMovingLayerPDECExclusion`。",
            "- RootWindow 侧可继续攻 `PrimeSquareEndpointCountGt2SqrtP` 或证明根缺陷不能终端化。",
            "- MovingLayer 侧可继续攻 top moving atoms 的相位/短簇不可持久化。",
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
    result["source_hashes"]["docs/monograph/prime-matrix-square-phase-terminal-pressure-pdec-registration-router.md"] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(
        {
            "status": result["status"],
            "max_p": args.max_p,
            "registered_pdec_count": result["registered_pdec_count"],
            "terminal_registered_pdec_count": result["terminal_registered_pdec_count"],
            "next_direct_attack_target": result["next_direct_attack_target"],
            "row_column_unconditional_closed": result["row_column_unconditional_closed"],
        },
        ensure_ascii=False,
        indent=2,
    ))


if __name__ == "__main__":
    main()
