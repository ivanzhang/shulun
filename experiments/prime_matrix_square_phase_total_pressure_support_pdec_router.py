#!/usr/bin/env python3
"""把总 no-slot 压力缺陷登记为精确尾支撑 PDEC。

用法示例：
  python3 experiments/prime_matrix_square_phase_total_pressure_support_pdec_router.py --max-p 5000
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-total-pressure-support-pdec-router.json

输出：
  data/square-phase-total-pressure-support-pdec-ledger.json
  docs/monograph/prime-matrix-square-phase-total-pressure-support-pdec-router.json
  docs/monograph/prime-matrix-square-phase-total-pressure-support-pdec-router.md
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
TOTAL_GATE_ROUTER = ROOT / "experiments" / "prime_matrix_square_phase_total_noslot_pressure_gate_router.py"

OUT_LEDGER = DATA / "square-phase-total-pressure-support-pdec-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-total-pressure-support-pdec-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-total-pressure-support-pdec-router.md"

MAIN_TARGET = "TotalNoSlotPressureDefectExclusionOrTotalPressurePDEC"
NEXT_TARGET = "TotalPressureSupportPDECExclusion"


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


def compact_atom(atom: dict[str, Any], prime_flags: bytearray) -> dict[str, Any]:
    """压缩单个 no-slot 层原子。"""
    q_values = [q for q in range(atom["q_hi"], atom["q_lo"] - 1, -2) if prime_flags[q]]
    return {
        "k": atom["k"],
        "b_interval": [atom["b_lo"], atom["b_hi"]],
        "q_interval": [atom["q_lo"], atom["q_hi"]],
        "support_size": atom["length"],
        "prime_load": atom["prime_load"],
        "prime_q_values": q_values[:12],
    }


def support_for_side(split: Any, p: int, side: str, prime_flags: bytearray, pi_prefix: list[int]) -> dict[str, Any]:
    """生成单侧 no-slot 激活尾支撑。"""
    atoms = split.formula_atoms_for_side(p, side, prime_flags, pi_prefix)
    b_values: list[int] = []
    q_values: list[int] = []
    for atom in atoms:
        for b_value in range(atom["b_lo"], atom["b_hi"] + 1):
            b_values.append(b_value)
            q_values.append(p - 2 * b_value)

    unique_b = sorted(set(b_values))
    unique_q = sorted(set(q_values), reverse=True)
    support_prime_q_values = [q for q in unique_q if prime_flags[q]]
    atom_prime_load_sum = sum(atom["prime_load"] for atom in atoms)
    support_prime_load = len(support_prime_q_values)
    support_size = len(unique_b)
    return {
        "atoms": atoms,
        "compact_atoms": [compact_atom(atom, prime_flags) for atom in atoms],
        "raw_support_size": len(b_values),
        "support_size": support_size,
        "support_overlap_count": len(b_values) - support_size,
        "q_duplicate_count": len(q_values) - len(unique_q),
        "b_q_bijection_ok": support_size == len(unique_q),
        "support_q_min": min(unique_q) if unique_q else None,
        "support_q_max": max(unique_q) if unique_q else None,
        "support_prime_load": support_prime_load,
        "support_prime_q_values": support_prime_q_values[:20],
        "atom_prime_load_sum": atom_prime_load_sum,
        "support_density": support_prime_load / support_size if support_size else 0.0,
        "max_atom_prime_load": max((atom["prime_load"] for atom in atoms), default=0),
        "max_atom_support_size": max((atom["length"] for atom in atoms), default=0),
        "atom_count": len(atoms),
    }


def audit_side(split: Any, p: int, side: str, prime_flags: bytearray, pi_prefix: list[int]) -> dict[str, Any]:
    """审计单侧总压力支撑 PDEC 条件。"""
    split_record = split.audit_p(p, prime_flags, pi_prefix)
    support = support_for_side(split, p, side, prime_flags, pi_prefix)
    prime_window = split_record[f"{side}_prime_window"]
    no_slot_load = split_record[f"{side}_no_slot_load"]
    support_load = support["support_prime_load"]
    total_pressure_defect = prime_window <= 2 * support_load
    identity_ok = support_load == support["atom_prime_load_sum"] == no_slot_load
    threshold = (prime_window + 1) // 2
    support_fraction = support["support_size"] / (p - 1) if p > 1 else 0.0
    required_fraction = (2 * support_load) / (p - 1) if p > 1 else 0.0
    return {
        "formal_unit": f"P={p}|side={side}|total-pressure-support",
        "p": p,
        "side": side,
        "prime_window": prime_window,
        "threshold": threshold,
        "no_slot_load": no_slot_load,
        "support_prime_load": support_load,
        "support_size": support["support_size"],
        "support_fraction": support_fraction,
        "required_square_survivor_fraction_to_fail": required_fraction,
        "support_density": support["support_density"],
        "total_pressure_margin": prime_window - 2 * support_load,
        "coarse_support_margin": prime_window - 2 * support["support_size"],
        "total_pressure_defect": total_pressure_defect,
        "support_load_gap_to_terminal": support_load - threshold,
        "support_identity_ok": identity_ok,
        "support_overlap_count": support["support_overlap_count"],
        "q_duplicate_count": support["q_duplicate_count"],
        "b_q_bijection_ok": support["b_q_bijection_ok"],
        "support_q_min": support["support_q_min"],
        "support_q_max": support["support_q_max"],
        "atom_count": support["atom_count"],
        "max_atom_prime_load": support["max_atom_prime_load"],
        "max_atom_support_size": support["max_atom_support_size"],
        "support_prime_q_values": support["support_prime_q_values"],
        "top_atoms": sorted(
            support["compact_atoms"],
            key=lambda atom: (atom["prime_load"], atom["support_size"]),
            reverse=True,
        )[:8],
    }


def compact(record: dict[str, Any]) -> dict[str, Any]:
    """压缩单侧记录。"""
    return {
        "formal_unit": record["formal_unit"],
        "p": record["p"],
        "side": record["side"],
        "prime_window": record["prime_window"],
        "support_prime_load": record["support_prime_load"],
        "support_size": record["support_size"],
        "total_pressure_margin": record["total_pressure_margin"],
        "coarse_support_margin": record["coarse_support_margin"],
        "support_load_gap_to_terminal": record["support_load_gap_to_terminal"],
        "support_fraction": record["support_fraction"],
        "required_square_survivor_fraction_to_fail": record["required_square_survivor_fraction_to_fail"],
        "support_density": record["support_density"],
        "atom_count": record["atom_count"],
        "support_q_interval": [record["support_q_min"], record["support_q_max"]],
        "max_atom_prime_load": record["max_atom_prime_load"],
        "max_atom_support_size": record["max_atom_support_size"],
        "total_pressure_defect": record["total_pressure_defect"],
    }


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "activated_tail_support_bijection",
            "status": "closed",
            "statement": "For each P and side, every no-slot atom is a disjoint b-interval and q=P-2b gives a bijection to the activated tail support.",
        },
        {
            "name": "noslot_load_support_identity",
            "status": "closed",
            "statement": "NoSlotLoad equals the number of primes q in the activated tail support Q_side(P).",
        },
        {
            "name": "total_pressure_support_pdec_normal_form",
            "status": "closed",
            "statement": "A total pressure defect is exactly W_side(P)<=2*pi(Q_side(P)), with Q_side(P) explicitly registered.",
        },
        {
            "name": "finite_total_pressure_support_pdec_absence",
            "status": "finite_evidence",
            "statement": "The finite audit finds no registered total pressure support PDEC up to the tested bound.",
        },
        {
            "name": "support_pdec_exclusion",
            "status": "open",
            "statement": "A global proof still needs to exclude W_side(P)<=2*pi(Q_side(P)) for the activated support, or route persistent failures to phase/SAE/ColumnCRT certificates.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "ActivatedTailSupportBijectionClosed",
            "closed": result["support_overlap_failure_count"] == 0 and result["b_q_bijection_failure_count"] == 0,
            "proved": True,
            "meaning": "no-slot 支撑不是多重负载；每个支撑点有唯一 b 和唯一 q=P-2b。",
            "remaining": "closed",
        },
        {
            "gate": "NoSlotLoadSupportIdentityClosed",
            "closed": result["support_identity_failure_count"] == 0,
            "proved": True,
            "meaning": "总 no-slot 负载已经精确化为激活尾支撑上的素数计数。",
            "remaining": "closed",
        },
        {
            "gate": "TotalPressureSupportPDECRegistered",
            "closed": True,
            "proved": True,
            "meaning": "若 `PrimeWindow<=2*NoSlotLoad` 失败发生，formal unit 已有唯一支撑证书格式。",
            "remaining": "closed",
        },
        {
            "gate": "FiniteNoTotalPressureSupportPDEC",
            "closed": result["total_pressure_support_pdec_count"] == 0,
            "proved": False,
            "meaning": f"有限扫描 P<={result['parameters']['max_p']} 中未发现总压力支撑 PDEC。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "TotalPressureSupportPDECExcludedGlobally",
            "closed": False,
            "proved": False,
            "meaning": "仍需全局证明平方窗最终幸存数不能小于两倍激活尾支撑素数负载。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只把总压力缺陷登记为更尖锐的支撑 PDEC，不关闭全局行/列命题。",
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
    support_pdec_records = [record for record in records if record["total_pressure_defect"]]
    identity_failures = [record for record in records if not record["support_identity_ok"]]
    overlap_failures = [record for record in records if record["support_overlap_count"] != 0]
    q_duplicate_failures = [record for record in records if record["q_duplicate_count"] != 0]
    bijection_failures = [record for record in records if not record["b_q_bijection_ok"]]
    sample_set = set(sample_ps)
    sample_records = [record for record in records if record["p"] in sample_set]
    frontier_records = sorted(records, key=lambda record: (record["total_pressure_margin"], record["p"], record["side"]))
    worst_margin = frontier_records[0] if frontier_records else None
    best_margin = max(records, key=lambda record: record["total_pressure_margin"], default=None)
    max_support_fraction = max(records, key=lambda record: record["support_fraction"], default=None)
    max_required_fraction = max(records, key=lambda record: record["required_square_survivor_fraction_to_fail"], default=None)

    aggregate = {
        "record_count": len(records),
        "combined_prime_window": sum(record["prime_window"] for record in records),
        "combined_support_prime_load": sum(record["support_prime_load"] for record in records),
        "combined_support_size": sum(record["support_size"] for record in records),
        "total_pressure_support_pdec_count": len(support_pdec_records),
        "support_identity_failure_count": len(identity_failures),
        "support_overlap_failure_count": len(overlap_failures),
        "q_duplicate_failure_count": len(q_duplicate_failures),
        "b_q_bijection_failure_count": len(bijection_failures),
        "min_total_pressure_margin": worst_margin["total_pressure_margin"] if worst_margin else None,
        "max_total_pressure_margin": best_margin["total_pressure_margin"] if best_margin else None,
        "max_support_fraction": max_support_fraction["support_fraction"] if max_support_fraction else None,
        "max_required_square_survivor_fraction_to_fail": (
            max_required_fraction["required_square_survivor_fraction_to_fail"] if max_required_fraction else None
        ),
    }
    ledger = {
        "parameters": {"max_p": max_p, "sample_ps": sample_ps},
        "prime_count": len(p_values),
        "aggregate": aggregate,
        "frontier_records": [compact(record) for record in frontier_records[:80]],
        "sample_records": [compact(record) | {"top_atoms": record["top_atoms"]} for record in sample_records],
        "total_pressure_support_pdec_records": [
            compact(record) | {"top_atoms": record["top_atoms"]} for record in support_pdec_records[:80]
        ],
        "support_identity_failures": [compact(record) for record in identity_failures[:20]],
        "support_overlap_failures": [compact(record) for record in overlap_failures[:20]],
        "q_duplicate_failures": [compact(record) for record in q_duplicate_failures[:20]],
        "b_q_bijection_failures": [compact(record) for record in bijection_failures[:20]],
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    result = {
        "certificate_type": "prime_matrix_square_phase_total_pressure_support_pdec_router",
        "status": "total_pressure_defect_registered_as_activated_tail_support_pdec_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "empirical_absence_not_used_as_proof": True,
        "parameters": ledger["parameters"],
        "finite_prime_count": len(p_values),
        "aggregate": aggregate,
        "total_pressure_support_pdec_count": len(support_pdec_records),
        "support_identity_failure_count": len(identity_failures),
        "support_overlap_failure_count": len(overlap_failures),
        "q_duplicate_failure_count": len(q_duplicate_failures),
        "b_q_bijection_failure_count": len(bijection_failures),
        "worst_margin_record": compact(worst_margin) if worst_margin else None,
        "best_margin_record": compact(best_margin) if best_margin else None,
        "max_support_fraction_record": compact(max_support_fraction) if max_support_fraction else None,
        "max_required_fraction_record": compact(max_required_fraction) if max_required_fraction else None,
        "frontier_records": ledger["frontier_records"][:20],
        "sample_records": ledger["sample_records"],
        "total_pressure_support_pdec_records": ledger["total_pressure_support_pdec_records"],
        "activated_tail_support_bijection_closed": len(overlap_failures) == 0 and len(bijection_failures) == 0,
        "noslot_load_support_identity_closed": len(identity_failures) == 0,
        "total_pressure_support_pdec_schema_closed": True,
        "total_pressure_support_pdec_excluded_globally": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "alternative_attack_target": "PersistentSupportDensityPhasePDECOrSquareWheelSurvivorLowerBound",
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_total_pressure_support_pdec_router.py": sha256(
                Path(__file__).resolve()
            ),
            "experiments/prime_matrix_square_phase_noslot_k0_rootwindow_split_router.py": sha256(SPLIT_ROUTER),
            "experiments/prime_matrix_square_phase_total_noslot_pressure_gate_router.py": sha256(TOTAL_GATE_ROUTER),
            "data/square-phase-total-pressure-support-pdec-ledger.json": sha256(OUT_LEDGER),
        },
        "plain_conclusion": (
            "本步把 `PrimeWindow<=2*NoSlotLoad` 的总压力缺陷登记为精确的激活尾支撑 PDEC。"
            "对固定 `P,side`，每个 no-slot 层原子都是互不重叠的 b 区间，"
            "`q=P-2b` 给出到尾素支撑的双射；因此 `NoSlotLoad` 正是该支撑里的素数个数。"
            "任意终端反例现在必须满足 `W_side(P)<=2*pi(Q_side(P))`，其中 `Q_side(P)` 已由同一 formal unit 显式给出。"
            "有限审计未发现这种支撑 PDEC，但全局仍需证明它不可能持久发生，或把持久失败继续送入相位/SAE/ColumnCRT 证书。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase total pressure support PDEC router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"max_p={result['parameters']['max_p']}",
        f"finite_prime_count={result['finite_prime_count']}",
        f"total_pressure_support_pdec_count={result['total_pressure_support_pdec_count']}",
        f"support_identity_failure_count={result['support_identity_failure_count']}",
        f"support_overlap_failure_count={result['support_overlap_failure_count']}",
        f"b_q_bijection_failure_count={result['b_q_bijection_failure_count']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 激活尾支撑正规形",
        "",
        "令 `q=P-2b`。固定 `b` 后存在唯一商余数",
        "",
        "```text",
        "2b^2 = k(P-2b)+s,  0<=s<P-2b.",
        "```",
        "",
        "plus 侧 no-slot 条件是 `0<=s<(P+1)/2-2b`；minus 侧条件是 `(P-1)/2<s<P-2b`。因此每个 `b` 至多进入一个 floor layer，层原子互不重叠，且 `b -> q=P-2b` 是双射。",
        "",
        "于是对每个 `P,side` 有精确恒等式",
        "",
        "```text",
        "NoSlotLoad_side(P) = #{q in Q_side(P): q prime}.",
        "```",
        "",
        "## 2. 总压力 PDEC 正规形",
        "",
        "记",
        "",
        "```text",
        "W_side(P)=#{1<=r<P: P^2 ± r is prime},",
        "N_side(P)=#{q in Q_side(P): q prime}.",
        "```",
        "",
        "上一层总压力门给出终端反例当且仅当",
        "",
        "```text",
        "W_side(P) <= 2*N_side(P).",
        "```",
        "",
        "所以真正剩余已经不是抽象的 `NoSlotLoad`，而是一个带完整支撑表的 formal unit：平方锚最终幸存素数过少，同时激活尾支撑素数负载过大。",
        "",
        "## 3. 有限审计摘要",
        "",
        "| metric | value |",
        "| --- | ---: |",
        f"| record count | {agg['record_count']} |",
        f"| combined PrimeWindow | {agg['combined_prime_window']} |",
        f"| combined support prime load | {agg['combined_support_prime_load']} |",
        f"| combined support size | {agg['combined_support_size']} |",
        f"| total pressure support PDEC count | {agg['total_pressure_support_pdec_count']} |",
        f"| support identity failures | {agg['support_identity_failure_count']} |",
        f"| support overlap failures | {agg['support_overlap_failure_count']} |",
        f"| b-q bijection failures | {agg['b_q_bijection_failure_count']} |",
        f"| min total pressure margin | {agg['min_total_pressure_margin']} |",
        f"| max total pressure margin | {agg['max_total_pressure_margin']} |",
        f"| max support fraction | {agg['max_support_fraction']:.6f} |",
        f"| max required square survivor fraction to fail | {agg['max_required_square_survivor_fraction_to_fail']:.6f} |",
        "",
        "## 4. 最窄边界记录",
        "",
        "| label | P | side | W | support primes | support size | W-2N | support gap | required fraction |",
        "| --- | ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    boundary_rows = [
        ("worst margin", result["worst_margin_record"]),
        ("best margin", result["best_margin_record"]),
        ("max support fraction", result["max_support_fraction_record"]),
        ("max required fraction", result["max_required_fraction_record"]),
    ]
    for label, record in boundary_rows:
        if not record:
            continue
        lines.append(
            "| "
            + " | ".join(
                [
                    label,
                    str(record["p"]),
                    f"`{record['side']}`",
                    str(record["prime_window"]),
                    str(record["support_prime_load"]),
                    str(record["support_size"]),
                    str(record["total_pressure_margin"]),
                    str(record["support_load_gap_to_terminal"]),
                    f"{record['required_square_survivor_fraction_to_fail']:.6f}",
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 5. 命题行",
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
            "## 6. 决策表",
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
            "## 7. 下一步",
            "",
            "- 主攻：`TotalPressureSupportPDECExclusion`。",
            "- 也就是排斥 `W_side(P)<=2*pi(Q_side(P))`：平方锚最终幸存数不能被同一 formal unit 的激活尾支撑素数负载压过。",
            "- 若不能直接排斥，应继续抽取 `Q_side(P)` 的持久相位密度、短簇、端点 SAE 或 ColumnCRT 证书。",
            "- 当前仍未证明全局行/列无条件闭合。",
            "",
            "## 8. 依赖哈希",
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
    result["source_hashes"]["docs/monograph/prime-matrix-square-phase-total-pressure-support-pdec-router.md"] = sha256(
        OUT_MD
    )
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "max_p": args.max_p,
                "total_pressure_support_pdec_count": result["total_pressure_support_pdec_count"],
                "support_identity_failure_count": result["support_identity_failure_count"],
                "support_overlap_failure_count": result["support_overlap_failure_count"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
