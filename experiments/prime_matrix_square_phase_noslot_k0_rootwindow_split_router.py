#!/usr/bin/env python3
"""把无槽短区间素数簇分裂为 k=0 根窗与 k>=1 moving 聚合簇。

用法示例：
  python3 experiments/prime_matrix_square_phase_noslot_k0_rootwindow_split_router.py --max-p 5000
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-noslot-k0-rootwindow-split-router.json

输出：
  data/square-phase-noslot-k0-rootwindow-split-ledger.json
  docs/monograph/prime-matrix-square-phase-noslot-k0-rootwindow-split-router.json
  docs/monograph/prime-matrix-square-phase-noslot-k0-rootwindow-split-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from math import isqrt, sqrt
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "square-phase-noslot-k0-rootwindow-split-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-noslot-k0-rootwindow-split-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-noslot-k0-rootwindow-split-router.md"

MAIN_TARGET = "MovingLayerShortPrimeClusterBoundOrPDEC"
NEXT_TARGET = "K0RootWindowPrimeClusterBoundAndKGe1MovingLayerAggregateBoundOrPDEC"


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


def prime_prefix(flags: bytearray) -> list[int]:
    """构造素数计数前缀。"""
    prefix = [0] * len(flags)
    total = 0
    for idx, is_prime in enumerate(flags):
        if is_prime:
            total += 1
        prefix[idx] = total
    return prefix


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def cutoff_alpha45(p: int) -> int:
    """返回 floor(4P/5)。"""
    return (4 * p) // 5


def b_max_for_tail(p: int) -> int:
    """返回 q=P-2b>floor(4P/5) 的最大 b。"""
    return (p - cutoff_alpha45(p) - 1) // 2


def square_prime_count(p: int, sign: str, prime_flags: bytearray) -> int:
    """计算 P^2 正负半窗内的素数个数。"""
    base = p * p
    total = 0
    for r_value in range(1, p):
        n_value = base + r_value if sign == "plus" else base - r_value
        if prime_flags[n_value]:
            total += 1
    return total


def side_formula_holds(p: int, b_value: int, k_value: int, side: str) -> bool:
    """用显式二次不等式判断 b 是否属于给定 side,k 的无槽原子。"""
    s_value = 2 * b_value * b_value + 2 * k_value * b_value - k_value * p
    q_value = p - 2 * b_value
    if side == "plus":
        return 0 <= s_value < (p + 1) // 2 - 2 * b_value
    if side == "minus":
        return (p - 1) // 2 < s_value < q_value
    raise ValueError(f"unknown side: {side}")


def layer_k(p: int, b_value: int) -> int:
    """返回 floor(2b^2/(P-2b))。"""
    return (2 * b_value * b_value) // (p - 2 * b_value)


def finalize_atom(p: int, side: str, atom: dict[str, Any], prime_flags: bytearray, pi_prefix: list[int]) -> dict[str, Any]:
    """补全层原子的 q 区间与 prime-load。"""
    b_lo = int(atom["b_lo"])
    b_hi = int(atom["b_hi"])
    q_hi = p - 2 * b_lo
    q_lo = p - 2 * b_hi
    load_by_prefix = pi_prefix[q_hi] - (pi_prefix[q_lo - 1] if q_lo > 0 else 0)
    direct_load = sum(1 for q_value in range(q_lo, q_hi + 1, 2) if prime_flags[q_value])
    return {
        "side": side,
        "k": int(atom["k"]),
        "b_lo": b_lo,
        "b_hi": b_hi,
        "length": b_hi - b_lo + 1,
        "q_lo": q_lo,
        "q_hi": q_hi,
        "q_span": q_hi - q_lo + 1,
        "prime_load": direct_load,
        "pi_delta_load": load_by_prefix,
        "length_over_sqrt_p": (b_hi - b_lo + 1) / sqrt(p),
        "q_values": [q_value for q_value in range(q_hi, q_lo - 1, -2) if prime_flags[q_value]][:8],
    }


def formula_atoms_for_side(p: int, side: str, prime_flags: bytearray, pi_prefix: list[int]) -> list[dict[str, Any]]:
    """由二次不等式公式生成层原子。"""
    max_b = b_max_for_tail(p)
    max_k = layer_k(p, max_b) if max_b else 0
    atoms: list[dict[str, Any]] = []
    for k_value in range(max_k + 1):
        current: dict[str, Any] | None = None
        for b_value in range(1, max_b + 1):
            if side_formula_holds(p, b_value, k_value, side):
                if current is None or b_value != current["b_hi"] + 1:
                    if current is not None:
                        atoms.append(finalize_atom(p, side, current, prime_flags, pi_prefix))
                    current = {"k": k_value, "b_lo": b_value, "b_hi": b_value}
                else:
                    current["b_hi"] = b_value
        if current is not None:
            atoms.append(finalize_atom(p, side, current, prime_flags, pi_prefix))
    return atoms


def plus_k0_b_hi_formula(p: int) -> int:
    """plus k=0: 4b(b+1)<=P 的最大 b。"""
    value = max(0, (isqrt(p + 1) - 1) // 2)
    while 4 * (value + 1) * (value + 2) <= p:
        value += 1
    while value > 0 and 4 * value * (value + 1) > p:
        value -= 1
    return min(value, b_max_for_tail(p))


def minus_k0_b_lo_formula(p: int) -> int:
    """minus k=0: 4b^2>P-1 的最小 b。"""
    value = max(1, isqrt(p) // 2)
    while 4 * value * value <= p - 1:
        value += 1
    while value > 1 and 4 * (value - 1) * (value - 1) > p - 1:
        value -= 1
    return value


def minus_k0_b_hi_formula(p: int) -> int:
    """minus k=0: 2b(b+1)<P 的最大 b。"""
    value = max(0, (isqrt(2 * p) - 1) // 2)
    while 2 * (value + 1) * (value + 2) < p:
        value += 1
    while value > 0 and 2 * value * (value + 1) >= p:
        value -= 1
    return min(value, b_max_for_tail(p))


def expected_k0_atom(p: int, side: str, prime_flags: bytearray, pi_prefix: list[int]) -> dict[str, Any] | None:
    """返回 k=0 根窗公式原子。"""
    if side == "plus":
        b_hi = plus_k0_b_hi_formula(p)
        if b_hi < 1:
            return None
        return finalize_atom(p, side, {"k": 0, "b_lo": 1, "b_hi": b_hi}, prime_flags, pi_prefix)
    if side == "minus":
        b_lo = minus_k0_b_lo_formula(p)
        b_hi = minus_k0_b_hi_formula(p)
        if b_lo > b_hi:
            return None
        return finalize_atom(p, side, {"k": 0, "b_lo": b_lo, "b_hi": b_hi}, prime_flags, pi_prefix)
    raise ValueError(f"unknown side: {side}")


def atom_key(atom: dict[str, Any] | None) -> tuple[Any, ...] | None:
    """原子比较键。"""
    if atom is None:
        return None
    return (
        atom["side"],
        atom["k"],
        atom["b_lo"],
        atom["b_hi"],
        atom["q_lo"],
        atom["q_hi"],
        atom["prime_load"],
    )


def audit_p(p: int, prime_flags: bytearray, pi_prefix: list[int]) -> dict[str, Any]:
    """审计单个 P 的 k=0/非零层分裂。"""
    plus_atoms = formula_atoms_for_side(p, "plus", prime_flags, pi_prefix)
    minus_atoms = formula_atoms_for_side(p, "minus", prime_flags, pi_prefix)
    plus_k0 = next((atom for atom in plus_atoms if atom["k"] == 0), None)
    minus_k0 = next((atom for atom in minus_atoms if atom["k"] == 0), None)
    plus_k0_expected = expected_k0_atom(p, "plus", prime_flags, pi_prefix)
    minus_k0_expected = expected_k0_atom(p, "minus", prime_flags, pi_prefix)
    plus_kge1_load = sum(atom["prime_load"] for atom in plus_atoms if atom["k"] >= 1)
    minus_kge1_load = sum(atom["prime_load"] for atom in minus_atoms if atom["k"] >= 1)
    plus_prime = square_prime_count(p, "plus", prime_flags)
    minus_prime = square_prime_count(p, "minus", prime_flags)
    plus_threshold = (plus_prime + 1) // 2
    minus_threshold = (minus_prime + 1) // 2
    plus_no_slot = (plus_k0 or {"prime_load": 0})["prime_load"] + plus_kge1_load
    minus_no_slot = (minus_k0 or {"prime_load": 0})["prime_load"] + minus_kge1_load
    plus_large = plus_no_slot >= plus_threshold
    minus_large = minus_no_slot >= minus_threshold
    plus_k0_large = (plus_k0 or {"prime_load": 0})["prime_load"] * 2 >= plus_threshold
    minus_k0_large = (minus_k0 or {"prime_load": 0})["prime_load"] * 2 >= minus_threshold
    plus_kge1_large = plus_kge1_load * 2 >= plus_threshold
    minus_kge1_large = minus_kge1_load * 2 >= minus_threshold
    plus_split_logic_ok = True
    minus_split_logic_ok = True
    if plus_large:
        plus_split_logic_ok = plus_k0_large or plus_kge1_large
    if minus_large:
        minus_split_logic_ok = minus_k0_large or minus_kge1_large
    return {
        "p": p,
        "plus_prime_window": plus_prime,
        "minus_prime_window": minus_prime,
        "plus_threshold_half_primewindow": plus_threshold,
        "minus_threshold_half_primewindow": minus_threshold,
        "plus_k0_atom": plus_k0,
        "minus_k0_atom": minus_k0,
        "plus_k0_expected_atom": plus_k0_expected,
        "minus_k0_expected_atom": minus_k0_expected,
        "plus_k0_formula_matches": atom_key(plus_k0) == atom_key(plus_k0_expected),
        "minus_k0_formula_matches": atom_key(minus_k0) == atom_key(minus_k0_expected),
        "plus_k0_load": (plus_k0 or {"prime_load": 0})["prime_load"],
        "minus_k0_load": (minus_k0 or {"prime_load": 0})["prime_load"],
        "plus_kge1_load": plus_kge1_load,
        "minus_kge1_load": minus_kge1_load,
        "plus_no_slot_load": plus_no_slot,
        "minus_no_slot_load": minus_no_slot,
        "plus_large_branch": plus_large,
        "minus_large_branch": minus_large,
        "plus_large_branch_forces_k0_or_kge1": plus_split_logic_ok,
        "minus_large_branch_forces_k0_or_kge1": minus_split_logic_ok,
        "plus_k0_large_branch": plus_k0_large,
        "minus_k0_large_branch": minus_k0_large,
        "plus_kge1_large_branch": plus_kge1_large,
        "minus_kge1_large_branch": minus_kge1_large,
        "plus_atom_count": len(plus_atoms),
        "minus_atom_count": len(minus_atoms),
    }


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "plus_k0_root_window_formula",
            "status": "closed",
            "statement": "The plus k=0 atom is exactly 1<=b<=B_+(P), where 4B(B+1)<=P.",
        },
        {
            "name": "minus_k0_root_window_formula",
            "status": "closed",
            "statement": "The minus k=0 atom is exactly B_-(P)<=b<=C_-(P), with 4b^2>P-1 and 2b(b+1)<P.",
        },
        {
            "name": "k0_kge1_split_dichotomy",
            "status": "closed",
            "statement": "A threatening no-slot branch forces either the k=0 root-window cluster or the k>=1 moving-layer aggregate to carry half the threshold.",
        },
        {
            "name": "rootwindow_or_kge1_bound",
            "status": "open",
            "statement": "A global proof still needs bounds for the k=0 root-window prime cluster and the k>=1 aggregate, or a PDEC/SAE exclusion.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "K0RootWindowFormulaClosed",
            "closed": result["k0_formula_failure_count"] == 0,
            "proved": True,
            "meaning": "plus/minus 的 k=0 原子已写成显式根窗。",
            "remaining": "closed",
        },
        {
            "gate": "K0KGe1SplitDichotomyClosed",
            "closed": result["split_logic_failure_count"] == 0,
            "proved": True,
            "meaning": "大无槽分支必进入 k=0 根窗簇或 k>=1 聚合簇。",
            "remaining": "closed",
        },
        {
            "gate": "FiniteNoLargeSplitBranch",
            "closed": result["finite_large_branch_count"] == 0,
            "proved": False,
            "meaning": f"有限扫描 P<={result['parameters']['max_p']} 中没有威胁性分支。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "GlobalK0RootWindowPrimeClusterBound",
            "closed": False,
            "proved": False,
            "meaning": "仍需证明 P 前 O(sqrt(P)) 根窗中的素数簇不足以承担反例压力。",
            "remaining": "K0RootWindowPrimeClusterBoundOrPDEC",
        },
        {
            "gate": "GlobalKGe1AggregateBound",
            "closed": False,
            "proved": False,
            "meaning": "仍需证明 k>=1 moving-layer 聚合簇不足以承担反例压力。",
            "remaining": "KGe1MovingLayerAggregateBoundOrPDEC",
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只分裂短区间素数簇，不关闭全局行/列命题。",
            "remaining": NEXT_TARGET,
        },
    ]


def build_result(max_p: int, sample_ps: list[int]) -> dict[str, Any]:
    """构造路由器结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    prime_flags = sieve(max_p * max_p + max_p)
    pi_prefix = prime_prefix(prime_flags)
    small_prime_flags = sieve(max_p)
    p_values = [p for p in range(3, max_p + 1) if small_prime_flags[p]]
    records = [audit_p(p, prime_flags, pi_prefix) for p in p_values]

    sample_set = set(sample_ps)
    sample_records = [record for record in records if record["p"] in sample_set]
    k0_formula_failures = [
        record
        for record in records
        if not record["plus_k0_formula_matches"] or not record["minus_k0_formula_matches"]
    ]
    large_branch_records = [
        record for record in records if record["plus_large_branch"] or record["minus_large_branch"]
    ]
    split_logic_failures = [
        record
        for record in records
        if not record["plus_large_branch_forces_k0_or_kge1"]
        or not record["minus_large_branch_forces_k0_or_kge1"]
    ]
    max_plus_k0 = max(records, key=lambda record: record["plus_k0_load"], default=None)
    max_minus_k0 = max(records, key=lambda record: record["minus_k0_load"], default=None)
    max_plus_kge1 = max(records, key=lambda record: record["plus_kge1_load"], default=None)
    max_minus_kge1 = max(records, key=lambda record: record["minus_kge1_load"], default=None)

    aggregate = {
        "plus_prime_window": sum(record["plus_prime_window"] for record in records),
        "minus_prime_window": sum(record["minus_prime_window"] for record in records),
        "plus_k0_load": sum(record["plus_k0_load"] for record in records),
        "minus_k0_load": sum(record["minus_k0_load"] for record in records),
        "plus_kge1_load": sum(record["plus_kge1_load"] for record in records),
        "minus_kge1_load": sum(record["minus_kge1_load"] for record in records),
        "max_plus_k0_load": max_plus_k0["plus_k0_load"] if max_plus_k0 else 0,
        "max_minus_k0_load": max_minus_k0["minus_k0_load"] if max_minus_k0 else 0,
        "max_plus_kge1_load": max_plus_kge1["plus_kge1_load"] if max_plus_kge1 else 0,
        "max_minus_kge1_load": max_minus_kge1["minus_kge1_load"] if max_minus_kge1 else 0,
    }
    aggregate["combined_prime_window"] = aggregate["plus_prime_window"] + aggregate["minus_prime_window"]
    aggregate["combined_k0_load"] = aggregate["plus_k0_load"] + aggregate["minus_k0_load"]
    aggregate["combined_kge1_load"] = aggregate["plus_kge1_load"] + aggregate["minus_kge1_load"]

    ledger = {
        "parameters": {"max_p": max_p, "alpha": "4/5", "sample_ps": sample_ps},
        "prime_count": len(p_values),
        "aggregate": aggregate,
        "k0_formula_failure_count": len(k0_formula_failures),
        "finite_large_branch_count": len(large_branch_records),
        "split_logic_failure_count": len(split_logic_failures),
        "max_plus_k0_record": max_plus_k0,
        "max_minus_k0_record": max_minus_k0,
        "max_plus_kge1_record": max_plus_kge1,
        "max_minus_kge1_record": max_minus_kge1,
        "sample_records": sample_records,
        "k0_formula_failures": k0_formula_failures[:20],
        "large_branch_records": large_branch_records[:20],
        "split_logic_failures": split_logic_failures[:20],
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    result = {
        "certificate_type": "prime_matrix_square_phase_noslot_k0_rootwindow_split_router",
        "status": "moving_short_prime_cluster_split_into_k0_rootwindow_and_kge1_aggregate_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "empirical_absence_not_used_as_proof": True,
        "parameters": ledger["parameters"],
        "finite_prime_count": len(p_values),
        "aggregate": aggregate,
        "k0_formula_failure_count": len(k0_formula_failures),
        "finite_large_branch_count": len(large_branch_records),
        "split_logic_failure_count": len(split_logic_failures),
        "max_plus_k0_record": max_plus_k0,
        "max_minus_k0_record": max_minus_k0,
        "max_plus_kge1_record": max_plus_kge1,
        "max_minus_kge1_record": max_minus_kge1,
        "sample_records": sample_records,
        "k0_rootwindow_formula_closed": len(k0_formula_failures) == 0,
        "k0_kge1_split_dichotomy_closed": len(split_logic_failures) == 0,
        "k0_rootwindow_prime_cluster_bound_proved": False,
        "kge1_moving_layer_aggregate_bound_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": "K0RootWindowPrimeClusterBoundOrPDEC",
        "alternative_attack_target": "KGe1MovingLayerAggregateBoundOrPDEC",
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_noslot_k0_rootwindow_split_router.py": sha256(
                Path(__file__).resolve()
            ),
            "data/square-phase-noslot-k0-rootwindow-split-ledger.json": sha256(OUT_LEDGER),
        },
        "plain_conclusion": (
            "本步把 moving 短区间素数簇分裂为 `k=0` 根窗和 `k>=1` 聚合簇。"
            "plus 的 `k=0` 原子精确为 `1<=b<=B_+(P)` 且 `4B(B+1)<=P`；"
            "minus 的 `k=0` 原子精确为 `4b^2>P-1` 与 `2b(b+1)<P` 夹出的根窗。"
            "若无槽分支真正达到反例压力，则根窗簇或 `k>=1` 聚合簇至少一支承担半阈值。"
            "这仍不闭合全局；剩余是分别证明根窗素数簇和 `k>=1` 聚合簇上界，或登记并排斥相应 PDEC/SAE。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase no-slot k0 root-window split router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"max_p={result['parameters']['max_p']}",
        f"finite_prime_count={result['finite_prime_count']}",
        f"k0_formula_failure_count={result['k0_formula_failure_count']}",
        f"finite_large_branch_count={result['finite_large_branch_count']}",
        f"split_logic_failure_count={result['split_logic_failure_count']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. k=0 根窗公式",
        "",
        "plus 侧 `k=0` 时，条件化为",
        "",
        "```text",
        "1<=b<=B_+(P),  4B_+(P)(B_+(P)+1)<=P.",
        "q in [P-2B_+(P), P-2].",
        "```",
        "",
        "minus 侧 `k=0` 时，条件化为",
        "",
        "```text",
        "4b^2>P-1,  2b(b+1)<P.",
        "```",
        "",
        "因此 `k=0` 是 P 前的根长度素数簇窗口。",
        "",
        "## 2. 有限审计摘要",
        "",
        "| metric | value |",
        "| --- | ---: |",
        f"| plus PrimeWindow | {agg['plus_prime_window']} |",
        f"| minus PrimeWindow | {agg['minus_prime_window']} |",
        f"| plus k0 load | {agg['plus_k0_load']} |",
        f"| minus k0 load | {agg['minus_k0_load']} |",
        f"| plus k>=1 load | {agg['plus_kge1_load']} |",
        f"| minus k>=1 load | {agg['minus_kge1_load']} |",
        f"| max plus k0 load | {agg['max_plus_k0_load']} |",
        f"| max minus k0 load | {agg['max_minus_k0_load']} |",
        f"| max plus k>=1 aggregate | {agg['max_plus_kge1_load']} |",
        f"| max minus k>=1 aggregate | {agg['max_minus_kge1_load']} |",
        "",
        "## 3. 最大记录",
        "",
        "| branch | P | PrimeWindow | load | atom/window |",
        "| --- | ---: | ---: | ---: | --- |",
    ]
    max_rows = [
        ("plus k0", result["max_plus_k0_record"], "plus_k0_load", "plus_k0_atom"),
        ("minus k0", result["max_minus_k0_record"], "minus_k0_load", "minus_k0_atom"),
        ("plus k>=1", result["max_plus_kge1_record"], "plus_kge1_load", None),
        ("minus k>=1", result["max_minus_kge1_record"], "minus_kge1_load", None),
    ]
    for label, record, load_key, atom_key_name in max_rows:
        if not record:
            continue
        atom = record.get(atom_key_name) if atom_key_name else None
        atom_text = "aggregate"
        if atom:
            atom_text = f"k={atom['k']}, b=[{atom['b_lo']},{atom['b_hi']}], q=[{atom['q_lo']},{atom['q_hi']}]"
        prime_key = "plus_prime_window" if label.startswith("plus") else "minus_prime_window"
        lines.append(f"| `{label}` | {record['p']} | {record[prime_key]} | {record[load_key]} | {atom_text} |")

    lines.extend(
        [
            "",
            "## 4. 样本表",
            "",
            "| P | plus k0 | plus k>=1 | minus k0 | minus k>=1 |",
            "| ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in result["sample_records"]:
        lines.append(
            f"| {row['p']} | {row['plus_k0_load']} | {row['plus_kge1_load']} | "
            f"{row['minus_k0_load']} | {row['minus_kge1_load']} |"
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
    for item in result["theorem_rows"]:
        lines.append(f"| `{item['name']}` | `{item['status']}` | {table_cell(item['statement'])} |")

    lines.extend(
        [
            "",
            "## 6. 决策表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | ---: | ---: | --- | --- |",
        ]
    )
    for item in result["decision_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{item['gate']}`",
                    f"`{fmt_bool(item['closed'])}`",
                    f"`{fmt_bool(item['proved'])}`",
                    table_cell(item["meaning"]),
                    table_cell(item["remaining"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 7. 下一步",
            "",
            f"- 主攻：`{result['next_direct_attack_target']}`。",
            f"- 备选：`{result['alternative_attack_target']}`。",
            "- 当前仍未证明全局闭合；只是把短区间簇拆成根窗簇与非零层聚合簇两个更小目标。",
            "",
            "## 8. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for name, digest in sorted(result["source_hashes"].items()):
        lines.append(f"| `{name}` | `{digest}` |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_ints(raw: str) -> list[int]:
    """解析整数列表。"""
    return [int(item) for item in raw.split(",") if item.strip()]


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-p", type=int, default=5000)
    parser.add_argument("--sample-ps", default="13,17,19,23,29,31,101,499,1009,2003,4999")
    args = parser.parse_args()

    result = build_result(max_p=args.max_p, sample_ps=parse_ints(args.sample_ps))
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result)
    print(
        json.dumps(
            {
                "status": result["status"],
                "max_p": result["parameters"]["max_p"],
                "k0_formula_failure_count": result["k0_formula_failure_count"],
                "finite_large_branch_count": result["finite_large_branch_count"],
                "split_logic_failure_count": result["split_logic_failure_count"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
