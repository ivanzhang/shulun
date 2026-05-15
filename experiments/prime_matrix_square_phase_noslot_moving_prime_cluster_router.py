#!/usr/bin/env python3
"""把无槽 moving layer prime-load 接成显式短区间素数簇对象。

用法示例：
  python3 experiments/prime_matrix_square_phase_noslot_moving_prime_cluster_router.py --max-p 5000
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-noslot-moving-prime-cluster-router.json

输出：
  data/square-phase-noslot-moving-prime-cluster-ledger.json
  docs/monograph/prime-matrix-square-phase-noslot-moving-prime-cluster-router.json
  docs/monograph/prime-matrix-square-phase-noslot-moving-prime-cluster-router.md
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

OUT_LEDGER = DATA / "square-phase-noslot-moving-prime-cluster-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-noslot-moving-prime-cluster-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-noslot-moving-prime-cluster-router.md"

MAIN_TARGET = "NoSlotLayerPrimeLoadBoundOrMovingLayerPDEC"
NEXT_TARGET = "MovingLayerShortPrimeClusterBoundOrPDEC"


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


def side_no_slot_direct(p: int, b_value: int, side: str) -> bool:
    """用 residue 定义直接判断无槽。"""
    q_value = p - 2 * b_value
    h_value = (p - 1) // 2
    residue = (2 * b_value * b_value) % q_value
    if side == "plus":
        return residue < q_value - h_value
    if side == "minus":
        return residue > h_value
    raise ValueError(f"unknown side: {side}")


def formula_atoms_for_side(
    p: int, side: str, prime_flags: bytearray, pi_prefix: list[int]
) -> list[dict[str, Any]]:
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


def direct_atoms_for_side(
    p: int, side: str, prime_flags: bytearray, pi_prefix: list[int]
) -> list[dict[str, Any]]:
    """由 residue 定义直接生成层原子。"""
    atoms: list[dict[str, Any]] = []
    current: dict[str, Any] | None = None
    for b_value in range(1, b_max_for_tail(p) + 1):
        if side_no_slot_direct(p, b_value, side):
            k_value = layer_k(p, b_value)
            if current is None or current["k"] != k_value or b_value != current["b_hi"] + 1:
                if current is not None:
                    atoms.append(finalize_atom(p, side, current, prime_flags, pi_prefix))
                current = {"k": k_value, "b_lo": b_value, "b_hi": b_value}
            else:
                current["b_hi"] = b_value
        elif current is not None:
            atoms.append(finalize_atom(p, side, current, prime_flags, pi_prefix))
            current = None
    if current is not None:
        atoms.append(finalize_atom(p, side, current, prime_flags, pi_prefix))
    return atoms


def finalize_atom(
    p: int, side: str, atom: dict[str, Any], prime_flags: bytearray, pi_prefix: list[int]
) -> dict[str, Any]:
    """补全层原子的 q 区间与 prime-load。"""
    b_lo = int(atom["b_lo"])
    b_hi = int(atom["b_hi"])
    q_hi = p - 2 * b_lo
    q_lo = p - 2 * b_hi
    load_by_prefix = pi_prefix[q_hi] - (pi_prefix[q_lo - 1] if q_lo > 0 else 0)
    direct_load = sum(1 for q_value in range(q_lo, q_hi + 1, 2) if prime_flags[q_value])
    q_samples = [q_value for q_value in range(q_hi, q_lo - 1, -2) if prime_flags[q_value]][:8]
    length = b_hi - b_lo + 1
    span = q_hi - q_lo + 1
    return {
        "side": side,
        "k": int(atom["k"]),
        "b_lo": b_lo,
        "b_hi": b_hi,
        "length": length,
        "q_lo": q_lo,
        "q_hi": q_hi,
        "q_span": span,
        "prime_load": direct_load,
        "pi_delta_load": load_by_prefix,
        "prime_density_among_b": direct_load / length if length else 0.0,
        "length_over_sqrt_p": length / sqrt(p),
        "q_values": q_samples,
    }


def atom_key(atom: dict[str, Any]) -> tuple[Any, ...]:
    """用于比较两个原子列表的稳定键。"""
    return (
        atom["side"],
        atom["k"],
        atom["b_lo"],
        atom["b_hi"],
        atom["length"],
        atom["q_lo"],
        atom["q_hi"],
        atom["prime_load"],
    )


def audit_p(p: int, prime_flags: bytearray, pi_prefix: list[int]) -> dict[str, Any]:
    """审计单个 P。"""
    plus_formula = formula_atoms_for_side(p, "plus", prime_flags, pi_prefix)
    minus_formula = formula_atoms_for_side(p, "minus", prime_flags, pi_prefix)
    plus_direct = direct_atoms_for_side(p, "plus", prime_flags, pi_prefix)
    minus_direct = direct_atoms_for_side(p, "minus", prime_flags, pi_prefix)
    plus_formula_keys = [atom_key(atom) for atom in plus_formula]
    minus_formula_keys = [atom_key(atom) for atom in minus_formula]
    plus_direct_keys = [atom_key(atom) for atom in plus_direct]
    minus_direct_keys = [atom_key(atom) for atom in minus_direct]
    plus_prime = square_prime_count(p, "plus", prime_flags)
    minus_prime = square_prime_count(p, "minus", prime_flags)
    plus_load = sum(atom["prime_load"] for atom in plus_formula)
    minus_load = sum(atom["prime_load"] for atom in minus_formula)
    plus_threshold = (plus_prime + 1) // 2
    minus_threshold = (minus_prime + 1) // 2
    plus_large = plus_load >= plus_threshold
    minus_large = minus_load >= minus_threshold
    plus_max_atom = max(plus_formula, key=lambda atom: atom["prime_load"], default=None)
    minus_max_atom = max(minus_formula, key=lambda atom: atom["prime_load"], default=None)
    plus_forced_cluster = (
        0 if not plus_formula else (plus_threshold + len(plus_formula) - 1) // len(plus_formula)
    )
    minus_forced_cluster = (
        0 if not minus_formula else (minus_threshold + len(minus_formula) - 1) // len(minus_formula)
    )
    plus_cluster_logic_ok = True
    minus_cluster_logic_ok = True
    if plus_large and plus_max_atom is not None:
        plus_cluster_logic_ok = plus_max_atom["prime_load"] >= plus_forced_cluster
    if minus_large and minus_max_atom is not None:
        minus_cluster_logic_ok = minus_max_atom["prime_load"] >= minus_forced_cluster
    prefix_failures = [
        atom for atom in plus_formula + minus_formula if atom["prime_load"] != atom["pi_delta_load"]
    ]
    length_failures = [atom for atom in plus_formula + minus_formula if atom["prime_load"] > atom["length"]]
    return {
        "p": p,
        "plus_prime_window": plus_prime,
        "minus_prime_window": minus_prime,
        "plus_no_slot_load": plus_load,
        "minus_no_slot_load": minus_load,
        "plus_atom_count": len(plus_formula),
        "minus_atom_count": len(minus_formula),
        "plus_max_atom": plus_max_atom,
        "minus_max_atom": minus_max_atom,
        "plus_large_branch": plus_large,
        "minus_large_branch": minus_large,
        "plus_forced_cluster_load": plus_forced_cluster,
        "minus_forced_cluster_load": minus_forced_cluster,
        "plus_formula_matches_direct": plus_formula_keys == plus_direct_keys,
        "minus_formula_matches_direct": minus_formula_keys == minus_direct_keys,
        "prefix_load_failure_count": len(prefix_failures),
        "length_failure_count": len(length_failures),
        "plus_cluster_logic_ok": plus_cluster_logic_ok,
        "minus_cluster_logic_ok": minus_cluster_logic_ok,
        "plus_atom_samples": plus_formula[:6],
        "minus_atom_samples": minus_formula[:6],
    }


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "quadratic_inequality_endpoint_formula",
            "status": "closed",
            "statement": "Layer atoms are exactly the integer solutions of explicit quadratic inequalities in b.",
        },
        {
            "name": "moving_q_interval_prime_load_identity",
            "status": "closed",
            "statement": "Each atom load equals pi(q_hi)-pi(q_lo-1) for q=P-2b on its moving interval.",
        },
        {
            "name": "trivial_length_envelope",
            "status": "closed",
            "statement": "Every atom has prime_load<=length, giving a deterministic but insufficient envelope.",
        },
        {
            "name": "large_branch_forces_short_prime_cluster",
            "status": "closed",
            "statement": "A threatening no-slot branch forces a moving q-interval with prime cluster load above the pigeonhole threshold.",
        },
        {
            "name": "short_prime_cluster_bound_or_pdec",
            "status": "open",
            "statement": "A global proof needs an upper bound for these moving short prime clusters, or a PDEC/SAE exclusion of persistent clusters.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "QuadraticFormulaMatchesDirectAtoms",
            "closed": result["formula_match_failure_count"] == 0,
            "proved": True,
            "meaning": "二次不等式端点公式与 residue 定义生成的原子完全一致。",
            "remaining": "closed",
        },
        {
            "gate": "PiDeltaLoadIdentityClosed",
            "closed": result["prefix_load_failure_count"] == 0,
            "proved": True,
            "meaning": "每个原子的 prime-load 等于普通素数计数函数在 q 区间的差。",
            "remaining": "closed",
        },
        {
            "gate": "TrivialLengthEnvelopeClosed",
            "closed": result["length_failure_count"] == 0,
            "proved": True,
            "meaning": "确定性长度上界成立，但不足以排除全局反例。",
            "remaining": "closed but insufficient",
        },
        {
            "gate": "FiniteNoLargeNoSlotBranch",
            "closed": result["finite_large_branch_count"] == 0,
            "proved": False,
            "meaning": f"有限扫描 P<={result['parameters']['max_p']} 没有威胁性无槽分支。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "GlobalMovingShortPrimeClusterBound",
            "closed": False,
            "proved": False,
            "meaning": "仍需全局证明 moving q-interval 内素数簇不可能承担反例所需负载。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只把 prime-load 接成短区间素数簇对象，不关闭全局行/列命题。",
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
    formula_match_failures = [
        record
        for record in records
        if not record["plus_formula_matches_direct"] or not record["minus_formula_matches_direct"]
    ]
    prefix_failures = [record for record in records if record["prefix_load_failure_count"]]
    length_failures = [record for record in records if record["length_failure_count"]]
    large_branch_records = [
        record for record in records if record["plus_large_branch"] or record["minus_large_branch"]
    ]
    cluster_logic_failures = [
        record
        for record in records
        if not record["plus_cluster_logic_ok"] or not record["minus_cluster_logic_ok"]
    ]
    max_plus_atom_record = max(
        records,
        key=lambda record: (record["plus_max_atom"] or {"prime_load": -1})["prime_load"],
        default=None,
    )
    max_minus_atom_record = max(
        records,
        key=lambda record: (record["minus_max_atom"] or {"prime_load": -1})["prime_load"],
        default=None,
    )

    aggregate = {
        "plus_prime_window": sum(record["plus_prime_window"] for record in records),
        "minus_prime_window": sum(record["minus_prime_window"] for record in records),
        "plus_no_slot_load": sum(record["plus_no_slot_load"] for record in records),
        "minus_no_slot_load": sum(record["minus_no_slot_load"] for record in records),
        "plus_atom_count": sum(record["plus_atom_count"] for record in records),
        "minus_atom_count": sum(record["minus_atom_count"] for record in records),
        "max_plus_atom_load": (
            (max_plus_atom_record["plus_max_atom"] or {"prime_load": 0})["prime_load"]
            if max_plus_atom_record
            else 0
        ),
        "max_minus_atom_load": (
            (max_minus_atom_record["minus_max_atom"] or {"prime_load": 0})["prime_load"]
            if max_minus_atom_record
            else 0
        ),
    }
    aggregate["combined_prime_window"] = aggregate["plus_prime_window"] + aggregate["minus_prime_window"]
    aggregate["combined_no_slot_load"] = aggregate["plus_no_slot_load"] + aggregate["minus_no_slot_load"]
    aggregate["combined_atom_count"] = aggregate["plus_atom_count"] + aggregate["minus_atom_count"]

    ledger = {
        "parameters": {"max_p": max_p, "alpha": "4/5", "sample_ps": sample_ps},
        "prime_count": len(p_values),
        "aggregate": aggregate,
        "formula_match_failure_count": len(formula_match_failures),
        "prefix_load_failure_count": len(prefix_failures),
        "length_failure_count": len(length_failures),
        "finite_large_branch_count": len(large_branch_records),
        "cluster_logic_failure_count": len(cluster_logic_failures),
        "max_plus_atom_record": max_plus_atom_record,
        "max_minus_atom_record": max_minus_atom_record,
        "sample_records": sample_records,
        "formula_match_failures": formula_match_failures[:20],
        "prefix_failures": prefix_failures[:20],
        "length_failures": length_failures[:20],
        "large_branch_records": large_branch_records[:20],
        "cluster_logic_failures": cluster_logic_failures[:20],
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    result = {
        "certificate_type": "prime_matrix_square_phase_noslot_moving_prime_cluster_router",
        "status": "noslot_layer_prime_load_reduced_to_moving_short_prime_cluster_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "empirical_absence_not_used_as_proof": True,
        "parameters": ledger["parameters"],
        "finite_prime_count": len(p_values),
        "aggregate": aggregate,
        "formula_match_failure_count": len(formula_match_failures),
        "prefix_load_failure_count": len(prefix_failures),
        "length_failure_count": len(length_failures),
        "finite_large_branch_count": len(large_branch_records),
        "cluster_logic_failure_count": len(cluster_logic_failures),
        "max_plus_atom_record": max_plus_atom_record,
        "max_minus_atom_record": max_minus_atom_record,
        "sample_records": sample_records,
        "quadratic_formula_matches_direct_atoms": len(formula_match_failures) == 0,
        "pi_delta_load_identity_closed": len(prefix_failures) == 0,
        "trivial_length_envelope_closed": len(length_failures) == 0,
        "large_branch_forces_short_prime_cluster_closed": len(cluster_logic_failures) == 0,
        "moving_short_prime_cluster_bound_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_noslot_moving_prime_cluster_router.py": sha256(
                Path(__file__).resolve()
            ),
            "data/square-phase-noslot-moving-prime-cluster-ledger.json": sha256(OUT_LEDGER),
        },
        "plain_conclusion": (
            "本步把 moving layer prime-load 精确接成普通短区间素数簇对象。"
            "固定 `P,side,k` 的层原子由显式二次不等式给出；对应 `q=P-2b` 区间为 "
            "`[P-2b_hi, P-2b_lo]`，其负载等于 `pi(q_hi)-pi(q_lo-1)`。"
            "若无槽分支大到威胁 `PrimeWindow`，则必须出现某个 moving q-interval 的高素数簇。"
            "确定性长度上界只能给出 `prime_load<=length`，不足以闭合全局；剩余是证明这些 moving 短区间素数簇上界，"
            "或把持久高簇登记并排斥为 PDEC/SAE。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    max_plus = result["max_plus_atom_record"]
    max_minus = result["max_minus_atom_record"]
    lines = [
        "# Prime Matrix square-phase no-slot moving prime cluster router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"max_p={result['parameters']['max_p']}",
        f"finite_prime_count={result['finite_prime_count']}",
        f"formula_match_failure_count={result['formula_match_failure_count']}",
        f"prefix_load_failure_count={result['prefix_load_failure_count']}",
        f"length_failure_count={result['length_failure_count']}",
        f"finite_large_branch_count={result['finite_large_branch_count']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 短区间素数簇对象",
        "",
        "固定 `P,side,k` 后，原子由下列二次不等式给出：",
        "",
        "```text",
        "s_k(b)=2b^2+2kb-kP.",
        "plus atom:  0 <= s_k(b) < (P+1)/2-2b",
        "minus atom: (P-1)/2 < s_k(b) < P-2b",
        "```",
        "",
        "若原子为 `b_lo<=b<=b_hi`，则对应普通 q 区间",
        "",
        "```text",
        "q_lo=P-2b_hi,  q_hi=P-2b_lo,",
        "prime_load = pi(q_hi)-pi(q_lo-1).",
        "```",
        "",
        "这把 moving layer 负载从二次相位问题转成短区间素数簇问题。",
        "",
        "## 2. 有限审计摘要",
        "",
        "| metric | value |",
        "| --- | ---: |",
        f"| plus PrimeWindow | {agg['plus_prime_window']} |",
        f"| minus PrimeWindow | {agg['minus_prime_window']} |",
        f"| plus no-slot load | {agg['plus_no_slot_load']} |",
        f"| minus no-slot load | {agg['minus_no_slot_load']} |",
        f"| plus atom count | {agg['plus_atom_count']} |",
        f"| minus atom count | {agg['minus_atom_count']} |",
        f"| max plus atom load | {agg['max_plus_atom_load']} |",
        f"| max minus atom load | {agg['max_minus_atom_load']} |",
        "",
        "## 3. 最大素数簇原子",
        "",
        "| side | P | k | b interval | q interval | length | q span | load | density | sample q |",
        "| --- | ---: | ---: | --- | --- | ---: | ---: | ---: | ---: | --- |",
    ]
    if max_plus and max_plus["plus_max_atom"]:
        atom = max_plus["plus_max_atom"]
        lines.append(
            f"| plus | {max_plus['p']} | {atom['k']} | [{atom['b_lo']},{atom['b_hi']}] | "
            f"[{atom['q_lo']},{atom['q_hi']}] | {atom['length']} | {atom['q_span']} | "
            f"{atom['prime_load']} | {atom['prime_density_among_b']:.6f} | `{atom['q_values']}` |"
        )
    if max_minus and max_minus["minus_max_atom"]:
        atom = max_minus["minus_max_atom"]
        lines.append(
            f"| minus | {max_minus['p']} | {atom['k']} | [{atom['b_lo']},{atom['b_hi']}] | "
            f"[{atom['q_lo']},{atom['q_hi']}] | {atom['length']} | {atom['q_span']} | "
            f"{atom['prime_load']} | {atom['prime_density_among_b']:.6f} | `{atom['q_values']}` |"
        )

    lines.extend(
        [
            "",
            "## 4. 样本表",
            "",
            "| P | plus atoms | plus load | plus max cluster | minus atoms | minus load | minus max cluster |",
            "| ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in result["sample_records"]:
        plus_max_load = (row["plus_max_atom"] or {"prime_load": 0})["prime_load"]
        minus_max_load = (row["minus_max_atom"] or {"prime_load": 0})["prime_load"]
        lines.append(
            f"| {row['p']} | {row['plus_atom_count']} | {row['plus_no_slot_load']} | "
            f"{plus_max_load} | {row['minus_atom_count']} | {row['minus_no_slot_load']} | {minus_max_load} |"
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
            "- 当前可合法使用的确定性上界只有 `prime_load<=length`；要闭合必须证明更强的 moving 短区间素数簇上界，或把持续高簇作为 PDEC/SAE 排斥。",
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
                "formula_match_failure_count": result["formula_match_failure_count"],
                "prefix_load_failure_count": result["prefix_load_failure_count"],
                "length_failure_count": result["length_failure_count"],
                "finite_large_branch_count": result["finite_large_branch_count"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
