#!/usr/bin/env python3
"""登记 pressure defect + companion-lift 的联合终端 PDEC family。

用法示例：
  python3 experiments/prime_matrix_square_phase_joint_pressure_pdec_router.py --max-p 5000
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-joint-pressure-pdec-router.json

输出：
  data/square-phase-joint-pressure-pdec-ledger.json
  docs/monograph/prime-matrix-square-phase-joint-pressure-pdec-router.json
  docs/monograph/prime-matrix-square-phase-joint-pressure-pdec-router.md
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

OUT_LEDGER = DATA / "square-phase-joint-pressure-pdec-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-joint-pressure-pdec-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-joint-pressure-pdec-router.md"

MAIN_TARGET = "PressureDefectCompanionLiftExclusion"
NEXT_TARGET = "JointPressureCompanionPDECExclusion"


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


def top_atoms(split: Any, p: int, side: str, prime_flags: bytearray, pi_prefix: list[int], limit: int = 5) -> list[dict[str, Any]]:
    """返回 k>=1 最大 moving 原子。"""
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
    """审计单侧 joint PDEC 条件。"""
    record = split.audit_p(p, prime_flags, pi_prefix)
    prime_window = record[f"{side}_prime_window"]
    threshold = record[f"{side}_threshold_half_primewindow"]
    k0_load = record[f"{side}_k0_load"]
    kge1_load = record[f"{side}_kge1_load"]
    no_slot = record[f"{side}_no_slot_load"]
    root_defect = prime_window <= 4 * k0_load
    kge1_defect = prime_window <= 4 * kge1_load
    root_pressure = 2 * k0_load >= threshold
    kge1_pressure = 2 * kge1_load >= threshold
    terminal = no_slot >= threshold
    root_companion_gap = kge1_load - max(0, threshold - k0_load)
    kge1_companion_gap = k0_load - max(0, threshold - kge1_load)
    root_joint = root_defect and root_pressure and root_companion_gap >= 0
    kge1_joint = kge1_defect and kge1_pressure and kge1_companion_gap >= 0
    return {
        "p": p,
        "side": side,
        "prime_window": prime_window,
        "threshold": threshold,
        "k0_load": k0_load,
        "kge1_load": kge1_load,
        "no_slot_load": no_slot,
        "terminal_no_slot": terminal,
        "root_defect": root_defect,
        "kge1_defect": kge1_defect,
        "root_pressure": root_pressure,
        "kge1_pressure": kge1_pressure,
        "root_companion_gap": root_companion_gap,
        "kge1_companion_gap": kge1_companion_gap,
        "root_joint_pdec": root_joint,
        "kge1_joint_pdec": kge1_joint,
        "terminal_implies_joint_pdec": (not terminal) or root_joint or kge1_joint,
        "top_kge1_atoms": top_atoms(split, p, side, prime_flags, pi_prefix),
    }


def make_joint_records(record: dict[str, Any]) -> list[dict[str, Any]]:
    """把单侧记录转成 joint PDEC 记录。"""
    records: list[dict[str, Any]] = []
    if record["root_joint_pdec"]:
        records.append({
            "family": "RootWindowCompanionLiftJointPDEC",
            "formal_unit": f"P={record['p']}|side={record['side']}|joint=root+k>=1",
            "p": record["p"],
            "side": record["side"],
            "branch": "RootWindowDefect",
            "prime_window": record["prime_window"],
            "threshold": record["threshold"],
            "k0_load": record["k0_load"],
            "kge1_load": record["kge1_load"],
            "no_slot_load": record["no_slot_load"],
            "terminal_no_slot": record["terminal_no_slot"],
            "pressure_defect": "PrimeWindow<=4*RootLoad",
            "companion_gap": record["root_companion_gap"],
            "top_kge1_atoms": record["top_kge1_atoms"],
        })
    if record["kge1_joint_pdec"]:
        records.append({
            "family": "KGe1CompanionLiftJointPDEC",
            "formal_unit": f"P={record['p']}|side={record['side']}|joint=k>=1+k0",
            "p": record["p"],
            "side": record["side"],
            "branch": "KGe1AggregatePressureDefect",
            "prime_window": record["prime_window"],
            "threshold": record["threshold"],
            "k0_load": record["k0_load"],
            "kge1_load": record["kge1_load"],
            "no_slot_load": record["no_slot_load"],
            "terminal_no_slot": record["terminal_no_slot"],
            "pressure_defect": "PrimeWindow<=4*KGe1Load",
            "companion_gap": record["kge1_companion_gap"],
            "top_kge1_atoms": record["top_kge1_atoms"],
        })
    return records


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "joint_pressure_companion_schema",
            "status": "closed",
            "statement": "A terminalized pressure defect is registered as a joint PDEC with both branch loads and companion gap.",
        },
        {
            "name": "terminal_noslot_implies_joint_pdec",
            "status": "closed",
            "statement": "Any terminal no-slot counterexample implies RootWindowCompanionLiftJointPDEC or KGe1CompanionLiftJointPDEC.",
        },
        {
            "name": "finite_joint_pdec_absence",
            "status": "finite_evidence",
            "statement": "The finite audit finds no joint pressure-companion PDEC up to the tested bound.",
        },
        {
            "name": "joint_pdec_exclusion",
            "status": "open",
            "statement": "A global proof still needs to exclude the joint PDEC family.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "JointPDECSchemaClosed",
            "closed": True,
            "proved": True,
            "meaning": "pressure defect 与 companion-lift 的同时贴合已有唯一 joint PDEC schema。",
            "remaining": "closed",
        },
        {
            "gate": "TerminalNoSlotImpliesJointPDECClosed",
            "closed": result["terminal_to_joint_pdec_failure_count"] == 0,
            "proved": True,
            "meaning": "任意终端 no-slot 反例必落入 joint PDEC family。",
            "remaining": "closed",
        },
        {
            "gate": "FiniteNoJointPDEC",
            "closed": result["joint_pdec_count"] == 0,
            "proved": False,
            "meaning": f"有限扫描 P<={result['parameters']['max_p']} 中没有 joint PDEC。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "JointPDECExcludedGlobally",
            "closed": False,
            "proved": False,
            "meaning": "仍需全局排斥 joint PDEC family。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只把终端反例压成 joint PDEC，不关闭全局行/列命题。",
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
    joint_records = [item for record in side_records for item in make_joint_records(record)]
    terminal_records = [record for record in side_records if record["terminal_no_slot"]]
    terminal_failures = [record for record in side_records if not record["terminal_implies_joint_pdec"]]
    sample_set = set(sample_ps)
    sample_records = [record for record in side_records if record["p"] in sample_set]
    worst_root_gap = min(side_records, key=lambda record: record["root_companion_gap"], default=None)
    worst_kge1_gap = min(side_records, key=lambda record: record["kge1_companion_gap"], default=None)
    aggregate = {
        "side_record_count": len(side_records),
        "joint_pdec_count": len(joint_records),
        "terminal_no_slot_count": len(terminal_records),
        "terminal_to_joint_pdec_failure_count": len(terminal_failures),
        "min_root_companion_gap": worst_root_gap["root_companion_gap"] if worst_root_gap else None,
        "min_kge1_companion_gap": worst_kge1_gap["kge1_companion_gap"] if worst_kge1_gap else None,
    }
    ledger = {
        "parameters": {"max_p": max_p, "sample_ps": sample_ps},
        "prime_count": len(p_values),
        "aggregate": aggregate,
        "joint_pdec_records": joint_records[:120],
        "terminal_records": terminal_records[:80],
        "terminal_to_joint_pdec_failures": terminal_failures[:40],
        "worst_root_gap_record": worst_root_gap,
        "worst_kge1_gap_record": worst_kge1_gap,
        "sample_records": sample_records[:80],
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = {
        "certificate_type": "prime_matrix_square_phase_joint_pressure_pdec_router",
        "status": "terminal_counterexample_reduced_to_joint_pressure_companion_pdec_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "empirical_absence_not_used_as_proof": True,
        "parameters": ledger["parameters"],
        "finite_prime_count": len(p_values),
        "aggregate": aggregate,
        "joint_pdec_count": len(joint_records),
        "terminal_no_slot_count": len(terminal_records),
        "terminal_to_joint_pdec_failure_count": len(terminal_failures),
        "worst_root_gap_record": worst_root_gap,
        "worst_kge1_gap_record": worst_kge1_gap,
        "sample_records": ledger["sample_records"],
        "joint_pressure_companion_schema_closed": True,
        "terminal_noslot_implies_joint_pdec_closed": len(terminal_failures) == 0,
        "joint_pdec_excluded_globally": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_joint_pressure_pdec_router.py": sha256(
                Path(__file__).resolve()
            ),
            "experiments/prime_matrix_square_phase_noslot_k0_rootwindow_split_router.py": sha256(
                SPLIT_ROUTER
            ),
            "data/square-phase-joint-pressure-pdec-ledger.json": sha256(OUT_LEDGER),
        },
        "plain_conclusion": (
            "本步把 companion-lift 进一步登记为唯一 joint PDEC family："
            "若终端 no-slot 反例存在，则它不只需要某个压力缺陷，还需要同一 `P,side` 的伴随分支补量，"
            "因此必落入 RootWindowCompanionLiftJointPDEC 或 KGe1CompanionLiftJointPDEC。"
            "有限扫描未发现 joint PDEC；全局仍需证明该 joint family 不存在或回流到更强缺陷。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase joint pressure PDEC router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"max_p={result['parameters']['max_p']}",
        f"finite_prime_count={result['finite_prime_count']}",
        f"joint_pdec_count={result['joint_pdec_count']}",
        f"terminal_no_slot_count={result['terminal_no_slot_count']}",
        f"terminal_to_joint_pdec_failure_count={result['terminal_to_joint_pdec_failure_count']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. Joint PDEC schema",
        "",
        "| family | required structure |",
        "| --- | --- |",
        "| `RootWindowCompanionLiftJointPDEC` | `PrimeWindow<=4*RootLoad` and `KGe1Load>=ceil(PrimeWindow/2)-RootLoad` |",
        "| `KGe1CompanionLiftJointPDEC` | `PrimeWindow<=4*KGe1Load` and `RootLoad>=ceil(PrimeWindow/2)-KGe1Load` |",
        "",
        "## 2. 有限审计摘要",
        "",
        "| metric | value |",
        "| --- | ---: |",
        f"| side records | {agg['side_record_count']} |",
        f"| joint PDEC count | {agg['joint_pdec_count']} |",
        f"| terminal no-slot count | {agg['terminal_no_slot_count']} |",
        f"| terminal-to-joint failures | {agg['terminal_to_joint_pdec_failure_count']} |",
        f"| min root companion gap | {agg['min_root_companion_gap']} |",
        f"| min k>=1 companion gap | {agg['min_kge1_companion_gap']} |",
        "",
        "## 3. 最坏 gap 记录",
        "",
        "| label | P | side | PrimeWindow | K0 | KGe1 | NoSlot | root gap | k>=1 gap | terminal |",
        "| --- | ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for label, record in [
        ("worst root gap", result["worst_root_gap_record"]),
        ("worst k>=1 gap", result["worst_kge1_gap_record"]),
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
                    str(record["root_companion_gap"]),
                    str(record["kge1_companion_gap"]),
                    f"`{fmt_bool(record['terminal_no_slot'])}`",
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
            "- 主攻：`JointPressureCompanionPDECExclusion`。",
            "- 若不能直接排斥，需要继续把 joint family 投影到更具体的相位/短簇/平方窗输入。",
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
    result["source_hashes"]["docs/monograph/prime-matrix-square-phase-joint-pressure-pdec-router.md"] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(
        {
            "status": result["status"],
            "max_p": args.max_p,
            "joint_pdec_count": result["joint_pdec_count"],
            "terminal_to_joint_pdec_failure_count": result["terminal_to_joint_pdec_failure_count"],
            "next_direct_attack_target": result["next_direct_attack_target"],
            "row_column_unconditional_closed": result["row_column_unconditional_closed"],
        },
        ensure_ascii=False,
        indent=2,
    ))


if __name__ == "__main__":
    main()
