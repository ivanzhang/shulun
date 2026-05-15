#!/usr/bin/env python3
"""把 k=0 根窗终端分支压缩为平方窗根缺陷。

用法示例：
  python3 experiments/prime_matrix_square_phase_k0_rootwindow_defect_router.py --max-p 5000
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-k0-rootwindow-defect-router.json

输出：
  data/square-phase-k0-rootwindow-defect-ledger.json
  docs/monograph/prime-matrix-square-phase-k0-rootwindow-defect-router.json
  docs/monograph/prime-matrix-square-phase-k0-rootwindow-defect-router.md
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

OUT_LEDGER = DATA / "square-phase-k0-rootwindow-defect-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-k0-rootwindow-defect-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-k0-rootwindow-defect-router.md"

MAIN_TARGET = "K0RootWindowPrimeClusterBoundOrPDEC"
NEXT_TARGET = "SquareWindowRootDefectLowerBoundOrRootWindowPDEC"


def sieve(limit: int) -> bytearray:
    """筛出 limit 以内的素数。"""
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


def root_b_interval(p: int, side: str) -> tuple[int, int] | None:
    """返回 k=0 根窗的 b 区间。"""
    if side == "plus":
        b_hi = plus_k0_b_hi_formula(p)
        if b_hi < 1:
            return None
        return (1, b_hi)
    if side == "minus":
        b_lo = minus_k0_b_lo_formula(p)
        b_hi = minus_k0_b_hi_formula(p)
        if b_lo > b_hi:
            return None
        return (b_lo, b_hi)
    raise ValueError(f"unknown side: {side}")


def layer_k(p: int, b_value: int) -> int:
    """返回 floor(2b^2/(P-2b))。"""
    return (2 * b_value * b_value) // (p - 2 * b_value)


def side_formula_holds(p: int, b_value: int, k_value: int, side: str) -> bool:
    """用二次不等式判断 b 是否属于给定 side,k 的无槽原子。"""
    s_value = 2 * b_value * b_value + 2 * k_value * b_value - k_value * p
    q_value = p - 2 * b_value
    if side == "plus":
        return 0 <= s_value < (p + 1) // 2 - 2 * b_value
    if side == "minus":
        return (p - 1) // 2 < s_value < q_value
    raise ValueError(f"unknown side: {side}")


def square_prime_count(p: int, side: str, prime_flags: bytearray) -> int:
    """计算 P^2 正负半窗内的素数个数。"""
    base = p * p
    total = 0
    for r_value in range(1, p):
        n_value = base + r_value if side == "plus" else base - r_value
        if prime_flags[n_value]:
            total += 1
    return total


def root_load(p: int, side: str, prime_flags: bytearray) -> dict[str, Any]:
    """计算 k=0 根窗负载。"""
    interval = root_b_interval(p, side)
    if interval is None:
        return {
            "b_lo": None,
            "b_hi": None,
            "b_length": 0,
            "q_lo": None,
            "q_hi": None,
            "q_span": 0,
            "root_load": 0,
            "root_primes": [],
        }
    b_lo, b_hi = interval
    q_hi = p - 2 * b_lo
    q_lo = p - 2 * b_hi
    primes = [q_value for q_value in range(q_hi, q_lo - 1, -2) if prime_flags[q_value]]
    return {
        "b_lo": b_lo,
        "b_hi": b_hi,
        "b_length": b_hi - b_lo + 1,
        "q_lo": q_lo,
        "q_hi": q_hi,
        "q_span": q_hi - q_lo + 1,
        "root_load": len(primes),
        "root_primes": primes[:12],
    }


def no_slot_load(p: int, side: str, prime_flags: bytearray) -> int:
    """计算 tail-prime 无槽总负载，用于确认 k0 是否真的处在终端反例分支。"""
    total = 0
    for b_value in range(1, b_max_for_tail(p) + 1):
        q_value = p - 2 * b_value
        if not prime_flags[q_value]:
            continue
        k_value = layer_k(p, b_value)
        if side_formula_holds(p, b_value, k_value, side):
            total += 1
    return total


def audit_side(p: int, side: str, prime_flags: bytearray) -> dict[str, Any]:
    """审计单侧 k0 根窗缺陷。"""
    root = root_load(p, side, prime_flags)
    prime_window = square_prime_count(p, side, prime_flags)
    threshold = (prime_window + 1) // 2
    root_value = root["root_load"]
    root_length = root["b_length"]
    no_slot_value = no_slot_load(p, side, prime_flags)
    k0_large = 2 * root_value >= threshold
    no_slot_large = no_slot_value >= threshold
    exact_defect_bound = 4 * root_value
    length_defect_bound = 4 * root_length
    exact_defect_forced = (not k0_large) or prime_window <= exact_defect_bound
    return {
        "p": p,
        "side": side,
        "prime_window": prime_window,
        "threshold_half_primewindow": threshold,
        "root": root,
        "no_slot_load": no_slot_value,
        "k0_large_branch": k0_large,
        "no_slot_large_branch": no_slot_large,
        "terminal_k0_branch": k0_large and no_slot_large,
        "root_load_length_envelope_ok": root_value <= root_length,
        "exact_root_defect_bound": exact_defect_bound,
        "length_root_defect_bound": length_defect_bound,
        "k0_large_forces_exact_root_defect": exact_defect_forced,
        "square_window_beats_exact_root_defect": prime_window > exact_defect_bound,
        "square_window_beats_length_root_defect": prime_window > length_defect_bound,
        "root_load_ratio": None if root_value == 0 else prime_window / (4 * root_value),
        "root_length_ratio": None if root_length == 0 else prime_window / (4 * root_length),
        "root_length_over_sqrt_p": root_length / sqrt(p),
    }


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "k0_rootwindow_exact_load",
            "status": "closed",
            "statement": "The k=0 branch load is exactly the prime count in the explicit root window below P.",
        },
        {
            "name": "k0_large_forces_squarewindow_root_defect",
            "status": "closed",
            "statement": "If the k=0 branch carries the split threshold, then PrimeWindow<=4*RootLoad.",
        },
        {
            "name": "k0_terminal_branch_reduction",
            "status": "closed",
            "statement": "A terminal no-slot counterexample using k=0 must therefore be a square-window root-defect event.",
        },
        {
            "name": "squarewindow_root_defect_exclusion",
            "status": "open",
            "statement": "A global proof still needs PrimeWindow>4*RootLoad, or a PDEC/SAE exclusion of persistent root-defect events.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "K0RootWindowExactLoadClosed",
            "closed": result["root_load_length_envelope_failure_count"] == 0,
            "proved": True,
            "meaning": "k=0 根窗负载被精确写成 P 前根窗内的素数计数。",
            "remaining": "closed",
        },
        {
            "gate": "K0LargeImpliesSquareWindowRootDefectClosed",
            "closed": result["exact_defect_implication_failure_count"] == 0,
            "proved": True,
            "meaning": "若 k0 分支承担半阈值，则 PrimeWindow<=4*RootLoad。",
            "remaining": "closed",
        },
        {
            "gate": "FiniteNoTerminalK0Branch",
            "closed": result["terminal_k0_branch_count"] == 0,
            "proved": False,
            "meaning": f"有限扫描 P<={result['parameters']['max_p']} 未出现终端 k0 分支。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "SquareWindowRootDefectExcludedGlobally",
            "closed": False,
            "proved": False,
            "meaning": "仍需全局证明平方窗素数数压过根窗负载四倍，或排斥持久根缺陷。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只关闭 k0 分支的必要缺陷形态，不关闭全局行/列命题。",
            "remaining": f"{NEXT_TARGET} AND KGe1MovingLayerAggregateBoundOrPDEC",
        },
    ]


def compact_record(record: dict[str, Any]) -> dict[str, Any]:
    """保留报告需要的核心字段。"""
    root = record["root"]
    return {
        "p": record["p"],
        "side": record["side"],
        "prime_window": record["prime_window"],
        "threshold": record["threshold_half_primewindow"],
        "root_load": root["root_load"],
        "root_b_interval": [root["b_lo"], root["b_hi"]],
        "root_q_interval": [root["q_lo"], root["q_hi"]],
        "root_length": root["b_length"],
        "no_slot_load": record["no_slot_load"],
        "k0_large_branch": record["k0_large_branch"],
        "no_slot_large_branch": record["no_slot_large_branch"],
        "terminal_k0_branch": record["terminal_k0_branch"],
        "root_load_ratio": record["root_load_ratio"],
        "root_length_ratio": record["root_length_ratio"],
        "root_primes": root["root_primes"],
    }


def build_result(max_p: int, sample_ps: list[int]) -> dict[str, Any]:
    """构造路由器结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    prime_flags = sieve(max_p * max_p + max_p)
    small_flags = sieve(max_p)
    p_values = [p for p in range(3, max_p + 1) if small_flags[p]]
    records = [
        audit_side(p, side, prime_flags)
        for p in p_values
        for side in ("plus", "minus")
    ]

    length_failures = [record for record in records if not record["root_load_length_envelope_ok"]]
    implication_failures = [
        record for record in records if not record["k0_large_forces_exact_root_defect"]
    ]
    k0_large_records = [record for record in records if record["k0_large_branch"]]
    terminal_records = [record for record in records if record["terminal_k0_branch"]]
    exact_defect_records = [
        record for record in records if not record["square_window_beats_exact_root_defect"]
    ]
    length_defect_records = [
        record for record in records if not record["square_window_beats_length_root_defect"]
    ]
    nonzero_ratio_records = [record for record in records if record["root_load_ratio"] is not None]

    max_root_load = max(records, key=lambda record: record["root"]["root_load"], default=None)
    min_exact_ratio = min(nonzero_ratio_records, key=lambda record: record["root_load_ratio"], default=None)
    min_length_ratio = min(
        [record for record in records if record["root_length_ratio"] is not None],
        key=lambda record: record["root_length_ratio"],
        default=None,
    )
    sample_set = set(sample_ps)
    sample_records = [record for record in records if record["p"] in sample_set]

    aggregate = {
        "record_count": len(records),
        "combined_prime_window": sum(record["prime_window"] for record in records),
        "combined_root_load": sum(record["root"]["root_load"] for record in records),
        "combined_no_slot_load": sum(record["no_slot_load"] for record in records),
        "k0_large_branch_count": len(k0_large_records),
        "terminal_k0_branch_count": len(terminal_records),
        "exact_root_defect_record_count": len(exact_defect_records),
        "length_root_defect_record_count": len(length_defect_records),
        "max_root_load": max_root_load["root"]["root_load"] if max_root_load else 0,
        "min_exact_root_ratio": min_exact_ratio["root_load_ratio"] if min_exact_ratio else None,
        "min_length_root_ratio": min_length_ratio["root_length_ratio"] if min_length_ratio else None,
    }

    ledger = {
        "parameters": {"max_p": max_p, "sample_ps": sample_ps},
        "prime_count": len(p_values),
        "aggregate": aggregate,
        "root_load_length_envelope_failure_count": len(length_failures),
        "exact_defect_implication_failure_count": len(implication_failures),
        "k0_large_branch_count": len(k0_large_records),
        "terminal_k0_branch_count": len(terminal_records),
        "exact_root_defect_record_count": len(exact_defect_records),
        "length_root_defect_record_count": len(length_defect_records),
        "max_root_load_record": compact_record(max_root_load) if max_root_load else None,
        "min_exact_root_ratio_record": compact_record(min_exact_ratio) if min_exact_ratio else None,
        "min_length_root_ratio_record": compact_record(min_length_ratio) if min_length_ratio else None,
        "k0_large_records": [compact_record(record) for record in k0_large_records[:50]],
        "terminal_k0_records": [compact_record(record) for record in terminal_records[:50]],
        "exact_root_defect_records": [compact_record(record) for record in exact_defect_records[:80]],
        "sample_records": [compact_record(record) for record in sample_records],
        "length_failures": [compact_record(record) for record in length_failures[:20]],
        "implication_failures": [compact_record(record) for record in implication_failures[:20]],
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    result = {
        "certificate_type": "prime_matrix_square_phase_k0_rootwindow_defect_router",
        "status": "k0_rootwindow_branch_reduced_to_squarewindow_root_defect_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "empirical_absence_not_used_as_proof": True,
        "parameters": ledger["parameters"],
        "finite_prime_count": len(p_values),
        "aggregate": aggregate,
        "root_load_length_envelope_failure_count": len(length_failures),
        "exact_defect_implication_failure_count": len(implication_failures),
        "k0_large_branch_count": len(k0_large_records),
        "terminal_k0_branch_count": len(terminal_records),
        "exact_root_defect_record_count": len(exact_defect_records),
        "length_root_defect_record_count": len(length_defect_records),
        "max_root_load_record": ledger["max_root_load_record"],
        "min_exact_root_ratio_record": ledger["min_exact_root_ratio_record"],
        "min_length_root_ratio_record": ledger["min_length_root_ratio_record"],
        "k0_large_records": ledger["k0_large_records"],
        "sample_records": ledger["sample_records"],
        "k0_rootwindow_exact_load_closed": len(length_failures) == 0,
        "k0_large_to_root_defect_implication_closed": len(implication_failures) == 0,
        "squarewindow_root_defect_excluded_globally": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "alternative_attack_target": "KGe1MovingLayerAggregateBoundOrPDEC",
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_k0_rootwindow_defect_router.py": sha256(
                Path(__file__).resolve()
            ),
            "data/square-phase-k0-rootwindow-defect-ledger.json": sha256(OUT_LEDGER),
        },
        "plain_conclusion": (
            "本步没有换命题，而是把 `K0RootWindowPrimeClusterBoundOrPDEC` 精确压缩："
            "若 k=0 根窗分支能承担 split 半阈值，则平方窗素数数必须满足 "
            "`PrimeWindow<=4*RootLoad`。其中 RootLoad 是 P 前显式根窗内的素数数。"
            "因此 k0 分支的全局排除等价于证明平方窗素数数始终压过该根窗负载四倍，"
            "或把持久违反者登记并排斥为 RootWindow-PDEC/SAE。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase k0 root-window defect router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"max_p={result['parameters']['max_p']}",
        f"finite_prime_count={result['finite_prime_count']}",
        f"root_load_length_envelope_failure_count={result['root_load_length_envelope_failure_count']}",
        f"exact_defect_implication_failure_count={result['exact_defect_implication_failure_count']}",
        f"k0_large_branch_count={result['k0_large_branch_count']}",
        f"terminal_k0_branch_count={result['terminal_k0_branch_count']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 精确压缩",
        "",
        "设 `W_sign(P)` 为 `P^2` 正负半窗内的素数数，`R0_sign(P)` 为 `k=0` 根窗内的尾素数。split 判据中的 k0 大分支是",
        "",
        "```text",
        "2*R0_sign(P) >= ceil(W_sign(P)/2).",
        "```",
        "",
        "因此必有",
        "",
        "```text",
        "W_sign(P) <= 4*R0_sign(P).",
        "```",
        "",
        "这说明 k0 分支若真成为终端反例，只能表现为平方窗素数数相对于 P 前根窗素数数的根缺陷。",
        "",
        "## 2. 根窗公式",
        "",
        "plus 侧：",
        "",
        "```text",
        "1<=b<=B_+(P),  4B_+(P)(B_+(P)+1)<=P,",
        "q=P-2b.",
        "```",
        "",
        "minus 侧：",
        "",
        "```text",
        "4b^2>P-1,  2b(b+1)<P,",
        "q=P-2b.",
        "```",
        "",
        "## 3. 有限审计摘要",
        "",
        "| metric | value |",
        "| --- | ---: |",
        f"| combined PrimeWindow | {agg['combined_prime_window']} |",
        f"| combined RootLoad | {agg['combined_root_load']} |",
        f"| combined no-slot load | {agg['combined_no_slot_load']} |",
        f"| k0 large branch count | {agg['k0_large_branch_count']} |",
        f"| terminal k0 branch count | {agg['terminal_k0_branch_count']} |",
        f"| exact root-defect record count | {agg['exact_root_defect_record_count']} |",
        f"| length root-defect record count | {agg['length_root_defect_record_count']} |",
        f"| max root load | {agg['max_root_load']} |",
        f"| min exact root ratio | {agg['min_exact_root_ratio']} |",
        f"| min length root ratio | {agg['min_length_root_ratio']} |",
        "",
        "## 4. 关键记录",
        "",
        "| label | P | side | PrimeWindow | RootLoad | b interval | q interval | ratio | terminal |",
        "| --- | ---: | --- | ---: | ---: | --- | --- | ---: | --- |",
    ]
    key_records = [
        ("max RootLoad", result["max_root_load_record"], "root_load_ratio"),
        ("min W/(4R0)", result["min_exact_root_ratio_record"], "root_load_ratio"),
        ("min W/(4Len)", result["min_length_root_ratio_record"], "root_length_ratio"),
    ]
    for label, record, ratio_key in key_records:
        if not record:
            continue
        ratio = record[ratio_key]
        lines.append(
            "| "
            + " | ".join(
                [
                    table_cell(label),
                    str(record["p"]),
                    table_cell(record["side"]),
                    str(record["prime_window"]),
                    str(record["root_load"]),
                    table_cell(record["root_b_interval"]),
                    table_cell(record["root_q_interval"]),
                    "inf" if ratio is None else f"{ratio:.6f}",
                    f"`{fmt_bool(record['terminal_k0_branch'])}`",
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 5. k0 大分支样本",
            "",
            "| P | side | PrimeWindow | RootLoad | b interval | q interval | no-slot | terminal |",
            "| ---: | --- | ---: | ---: | --- | --- | ---: | --- |",
        ]
    )
    for record in result["k0_large_records"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(record["p"]),
                    table_cell(record["side"]),
                    str(record["prime_window"]),
                    str(record["root_load"]),
                    table_cell(record["root_b_interval"]),
                    table_cell(record["root_q_interval"]),
                    str(record["no_slot_load"]),
                    f"`{fmt_bool(record['terminal_k0_branch'])}`",
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 6. 命题行",
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
            "## 7. 决策表",
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
            "## 8. 下一步",
            "",
            "- 主攻：`SquareWindowRootDefectLowerBoundOrRootWindowPDEC`，即证明 `W_sign(P)>4R0_sign(P)` 或排斥持久根缺陷。",
            "- 并行剩余：`KGe1MovingLayerAggregateBoundOrPDEC`。",
            "- 当前仍未证明全局行/列无条件闭合；本步只关闭 k0 分支的必要缺陷形态。",
            "",
            "## 9. 依赖哈希",
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
        default="13,17,19,23,29,31,73,101,499,1009,2003,4999",
    )
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    sample_ps = [int(item) for item in args.sample_ps.split(",") if item.strip()]
    result = build_result(args.max_p, sample_ps)
    write_markdown(result)
    result["source_hashes"]["docs/monograph/prime-matrix-square-phase-k0-rootwindow-defect-router.md"] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(
        {
            "status": result["status"],
            "max_p": args.max_p,
            "k0_large_branch_count": result["k0_large_branch_count"],
            "terminal_k0_branch_count": result["terminal_k0_branch_count"],
            "next_direct_attack_target": result["next_direct_attack_target"],
            "row_column_unconditional_closed": result["row_column_unconditional_closed"],
        },
        ensure_ascii=False,
        indent=2,
    ))


if __name__ == "__main__":
    main()
