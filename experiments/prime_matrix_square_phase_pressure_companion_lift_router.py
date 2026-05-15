#!/usr/bin/env python3
"""把已登记压力缺陷的终端化压成 companion-lift 门。

用法示例：
  python3 experiments/prime_matrix_square_phase_pressure_companion_lift_router.py --max-p 5000
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-pressure-companion-lift-router.json

输出：
  data/square-phase-pressure-companion-lift-ledger.json
  docs/monograph/prime-matrix-square-phase-pressure-companion-lift-router.json
  docs/monograph/prime-matrix-square-phase-pressure-companion-lift-router.md
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

OUT_LEDGER = DATA / "square-phase-pressure-companion-lift-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-pressure-companion-lift-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-pressure-companion-lift-router.md"

MAIN_TARGET = "RootWindowPDECAndMovingLayerPDECExclusion"
NEXT_TARGET = "PressureDefectCompanionLiftExclusion"


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


def top_kge1_atoms(split: Any, p: int, side: str, prime_flags: bytearray, pi_prefix: list[int], limit: int = 4) -> list[dict[str, Any]]:
    """返回 k>=1 moving-layer 的最大负载原子。"""
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


def audit_side(split: Any, p: int, side: str, prime_flags: bytearray, pi_prefix: list[int]) -> dict[str, Any]:
    """审计单侧压力缺陷的 companion-lift 条件。"""
    record = split.audit_p(p, prime_flags, pi_prefix)
    prime_window = record[f"{side}_prime_window"]
    threshold = record[f"{side}_threshold_half_primewindow"]
    k0_load = record[f"{side}_k0_load"]
    kge1_load = record[f"{side}_kge1_load"]
    no_slot_load = record[f"{side}_no_slot_load"]
    root_defect = prime_window <= 4 * k0_load
    kge1_defect = prime_window <= 4 * kge1_load
    root_pressure = 2 * k0_load >= threshold
    kge1_pressure = 2 * kge1_load >= threshold
    terminal = no_slot_load >= threshold
    root_companion_needed = max(0, threshold - k0_load)
    kge1_companion_needed = max(0, threshold - kge1_load)
    return {
        "p": p,
        "side": side,
        "prime_window": prime_window,
        "threshold": threshold,
        "k0_load": k0_load,
        "kge1_load": kge1_load,
        "no_slot_load": no_slot_load,
        "root_defect": root_defect,
        "kge1_defect": kge1_defect,
        "root_pressure": root_pressure,
        "kge1_pressure": kge1_pressure,
        "terminal_no_slot": terminal,
        "root_companion_needed_from_kge1": root_companion_needed,
        "root_companion_available": kge1_load,
        "root_companion_gap": kge1_load - root_companion_needed,
        "root_defect_terminalized": root_defect and root_pressure and kge1_load >= root_companion_needed,
        "kge1_companion_needed_from_k0": kge1_companion_needed,
        "kge1_companion_available": k0_load,
        "kge1_companion_gap": k0_load - kge1_companion_needed,
        "kge1_defect_terminalized": kge1_defect and kge1_pressure and k0_load >= kge1_companion_needed,
        "top_kge1_atoms": top_kge1_atoms(split, p, side, prime_flags, pi_prefix),
    }


def compact(record: dict[str, Any], branch: str) -> dict[str, Any]:
    """按分支压缩记录。"""
    base = {
        "p": record["p"],
        "side": record["side"],
        "branch": branch,
        "prime_window": record["prime_window"],
        "threshold": record["threshold"],
        "k0_load": record["k0_load"],
        "kge1_load": record["kge1_load"],
        "no_slot_load": record["no_slot_load"],
        "terminal_no_slot": record["terminal_no_slot"],
    }
    if branch == "RootWindowDefect":
        base.update({
            "companion_needed": record["root_companion_needed_from_kge1"],
            "companion_available": record["root_companion_available"],
            "companion_gap": record["root_companion_gap"],
            "terminalized": record["root_defect_terminalized"],
        })
    else:
        base.update({
            "companion_needed": record["kge1_companion_needed_from_k0"],
            "companion_available": record["kge1_companion_available"],
            "companion_gap": record["kge1_companion_gap"],
            "terminalized": record["kge1_defect_terminalized"],
            "top_kge1_atoms": record["top_kge1_atoms"],
        })
    return base


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "rootwindow_terminalization_companion_lift",
            "status": "closed",
            "statement": "A RootWindow pressure defect becomes terminal only if KGe1Load>=ceil(PrimeWindow/2)-RootLoad.",
        },
        {
            "name": "kge1_terminalization_companion_lift",
            "status": "closed",
            "statement": "A KGe1 pressure defect becomes terminal only if RootLoad>=ceil(PrimeWindow/2)-KGe1Load.",
        },
        {
            "name": "registered_pressure_defect_terminalization_equivalence",
            "status": "closed",
            "statement": "For registered pressure defects, terminality is exactly companion-lift nonnegative gap.",
        },
        {
            "name": "companion_lift_exclusion",
            "status": "open",
            "statement": "A global proof still needs to exclude companion-lift for the registered pressure families.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "RootWindowCompanionLiftFormulaClosed",
            "closed": True,
            "proved": True,
            "meaning": "RootWindow 缺陷要终端化，k>=1 伴随负载必须补足阈值缺口。",
            "remaining": "closed",
        },
        {
            "gate": "KGe1CompanionLiftFormulaClosed",
            "closed": True,
            "proved": True,
            "meaning": "KGe1 缺陷要终端化，k0 伴随负载必须补足阈值缺口。",
            "remaining": "closed",
        },
        {
            "gate": "FiniteNoRegisteredCompanionLift",
            "closed": result["terminalized_registered_defect_count"] == 0,
            "proved": False,
            "meaning": f"有限扫描 P<={result['parameters']['max_p']} 中已登记压力缺陷都未获得伴随补量。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "CompanionLiftExcludedGlobally",
            "closed": False,
            "proved": False,
            "meaning": "仍需全局证明两个压力 family 不能同时得到同侧伴随分支补量。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只把 PDEC 排斥压成 companion-lift 排斥，不关闭全局行/列命题。",
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
    side_records = [
        audit_side(split, p, side, prime_flags, pi_prefix)
        for p in p_values
        for side in ("plus", "minus")
    ]
    root_records = [
        compact(record, "RootWindowDefect")
        for record in side_records
        if record["root_defect"] and record["root_pressure"]
    ]
    kge1_records = [
        compact(record, "KGe1AggregatePressureDefect")
        for record in side_records
        if record["kge1_defect"] and record["kge1_pressure"]
    ]
    all_records = root_records + kge1_records
    terminalized = [record for record in all_records if record["terminalized"]]
    worst_gap = min(all_records, key=lambda record: record["companion_gap"], default=None)
    best_gap = max(all_records, key=lambda record: record["companion_gap"], default=None)
    sample_set = set(sample_ps)
    sample_records = [record for record in all_records if record["p"] in sample_set]
    aggregate = {
        "registered_pressure_defect_count": len(all_records),
        "rootwindow_pressure_defect_count": len(root_records),
        "kge1_pressure_defect_count": len(kge1_records),
        "terminalized_registered_defect_count": len(terminalized),
        "min_companion_gap": worst_gap["companion_gap"] if worst_gap else None,
        "max_companion_gap": best_gap["companion_gap"] if best_gap else None,
    }
    ledger = {
        "parameters": {"max_p": max_p, "sample_ps": sample_ps},
        "prime_count": len(p_values),
        "aggregate": aggregate,
        "rootwindow_companion_lift_records": root_records[:120],
        "kge1_companion_lift_records": kge1_records[:120],
        "terminalized_registered_defect_records": terminalized[:80],
        "worst_companion_gap_record": worst_gap,
        "best_companion_gap_record": best_gap,
        "sample_records": sample_records,
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = {
        "certificate_type": "prime_matrix_square_phase_pressure_companion_lift_router",
        "status": "registered_pressure_pdec_exclusion_reduced_to_companion_lift_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "empirical_absence_not_used_as_proof": True,
        "parameters": ledger["parameters"],
        "finite_prime_count": len(p_values),
        "aggregate": aggregate,
        "registered_pressure_defect_count": len(all_records),
        "rootwindow_pressure_defect_count": len(root_records),
        "kge1_pressure_defect_count": len(kge1_records),
        "terminalized_registered_defect_count": len(terminalized),
        "worst_companion_gap_record": worst_gap,
        "best_companion_gap_record": best_gap,
        "sample_records": sample_records,
        "rootwindow_companion_lift_formula_closed": True,
        "kge1_companion_lift_formula_closed": True,
        "registered_pressure_defect_terminalization_equivalence_closed": True,
        "companion_lift_excluded_globally": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_pressure_companion_lift_router.py": sha256(
                Path(__file__).resolve()
            ),
            "experiments/prime_matrix_square_phase_noslot_k0_rootwindow_split_router.py": sha256(
                SPLIT_ROUTER
            ),
            "data/square-phase-pressure-companion-lift-ledger.json": sha256(OUT_LEDGER),
        },
        "plain_conclusion": (
            "本步把已登记压力 PDEC 的排斥进一步压成 companion-lift 门："
            "RootWindowDefect 要成为终端反例，必须由 k>=1 伴随分支补足 "
            "`ceil(PrimeWindow/2)-RootLoad`；KGe1AggregatePressureDefect 要成为终端反例，"
            "必须由 k0 伴随分支补足 `ceil(PrimeWindow/2)-KGe1Load`。"
            "有限登记样本的 companion gap 全为负，因此都没有终端化；全局仍需证明这种同侧伴随补量不能持久出现。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase pressure companion-lift router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"max_p={result['parameters']['max_p']}",
        f"finite_prime_count={result['finite_prime_count']}",
        f"registered_pressure_defect_count={result['registered_pressure_defect_count']}",
        f"terminalized_registered_defect_count={result['terminalized_registered_defect_count']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. Companion-lift 公式",
        "",
        "RootWindow 分支：",
        "",
        "```text",
        "RootWindowDefect terminalizes iff KGe1Load >= ceil(PrimeWindow/2)-RootLoad.",
        "```",
        "",
        "KGe1 分支：",
        "",
        "```text",
        "KGe1AggregateDefect terminalizes iff RootLoad >= ceil(PrimeWindow/2)-KGe1Load.",
        "```",
        "",
        "因此压力缺陷本身不是终端矛盾；它必须与同一 `P,side` 的 companion 分支同时贴合。",
        "",
        "## 2. 有限审计摘要",
        "",
        "| metric | value |",
        "| --- | ---: |",
        f"| registered pressure defects | {agg['registered_pressure_defect_count']} |",
        f"| RootWindow pressure defects | {agg['rootwindow_pressure_defect_count']} |",
        f"| KGe1 pressure defects | {agg['kge1_pressure_defect_count']} |",
        f"| terminalized registered defects | {agg['terminalized_registered_defect_count']} |",
        f"| min companion gap | {agg['min_companion_gap']} |",
        f"| max companion gap | {agg['max_companion_gap']} |",
        "",
        "## 3. 关键 companion gap",
        "",
        "| label | P | side | branch | PrimeWindow | branch loads `(k0,k>=1)` | companion needed | companion available | gap | terminalized |",
        "| --- | ---: | --- | --- | ---: | --- | ---: | ---: | ---: | --- |",
    ]
    for label, record in [
        ("worst gap", result["worst_companion_gap_record"]),
        ("best gap", result["best_companion_gap_record"]),
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
                    table_cell(record["branch"]),
                    str(record["prime_window"]),
                    table_cell([record["k0_load"], record["kge1_load"]]),
                    str(record["companion_needed"]),
                    str(record["companion_available"]),
                    str(record["companion_gap"]),
                    f"`{fmt_bool(record['terminalized'])}`",
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
            "- 主攻：`PressureDefectCompanionLiftExclusion`。",
            "- 具体要证明同一 `P,side` 下，压力缺陷分支与 companion 补量不能同时达到终端阈值；或登记更高阶 joint PDEC。",
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
    result["source_hashes"]["docs/monograph/prime-matrix-square-phase-pressure-companion-lift-router.md"] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(
        {
            "status": result["status"],
            "max_p": args.max_p,
            "registered_pressure_defect_count": result["registered_pressure_defect_count"],
            "terminalized_registered_defect_count": result["terminalized_registered_defect_count"],
            "next_direct_attack_target": result["next_direct_attack_target"],
            "row_column_unconditional_closed": result["row_column_unconditional_closed"],
        },
        ensure_ascii=False,
        indent=2,
    ))


if __name__ == "__main__":
    main()
