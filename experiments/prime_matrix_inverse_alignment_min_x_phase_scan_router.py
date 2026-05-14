#!/usr/bin/env python3
"""生成逆元最小对齐解 x 的轮序同余方程组相位扫描证书。

用法示例：
  python3 experiments/prime_matrix_inverse_alignment_min_x_phase_scan_router.py
  python3 -m json.tool docs/monograph/prime-matrix-inverse-alignment-min-x-phase-scan-router.json

输出：
  data/inverse-alignment-min-x-phase-scan-ledger.json
  docs/monograph/prime-matrix-inverse-alignment-min-x-phase-scan-router.json
  docs/monograph/prime-matrix-inverse-alignment-min-x-phase-scan-router.md
"""

from __future__ import annotations

import hashlib
import json
import math
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DATA = ROOT / "data"
OUT_LEDGER = DATA / "inverse-alignment-min-x-phase-scan-ledger.json"
OUT_JSON = DOCS / "prime-matrix-inverse-alignment-min-x-phase-scan-router.json"
OUT_MD = DOCS / "prime-matrix-inverse-alignment-min-x-phase-scan-router.md"

P_VALUES = [13, 17, 19, 23, 29, 31]
MAX_SCAN = 1_000_000
EXTENDED_CAPACITY_PRIME_LIMIT = 101

SOURCE_FILES = [
    DOCS / "prime-matrix-inverse-alignment-latest-frontier-sync-router.json",
    DOCS / "prime-matrix-inverse-alignment-exact-x-budget-interface-router.json",
    DOCS / "prime-matrix-zero-row-minrep-route-review.md",
    DATA / "inverse-alignment-exact-x-budget-interface-ledger.json",
]


def sha256(path: Path) -> str:
    """计算文件 SHA256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def primes_lt(n: int) -> list[int]:
    """生成小于 n 的素数。"""
    if n <= 2:
        return []
    sieve = [True] * n
    sieve[0] = sieve[1] = False
    for p in range(2, int((n - 1) ** 0.5) + 1):
        if sieve[p]:
            for m in range(p * p, n, p):
                sieve[m] = False
    return [i for i in range(2, n) if sieve[i]]


def prime_factors(n: int) -> list[int]:
    """返回 n 的不同素因子。"""
    if n <= 1:
        return []
    factors: list[int] = []
    d = 2
    value = n
    while d * d <= value:
        if value % d == 0:
            factors.append(d)
            while value % d == 0:
                value //= d
        d += 1 if d == 2 else 2
    if value > 1:
        factors.append(value)
    return factors


def direct_hits(P: int, x: int, r: int) -> list[int]:
    """直接求覆盖列 r 的小素数 q，即 q | xP+r。"""
    return [q for q in primes_lt(P) if (x * P + r) % q == 0]


def wheel_sequence_hits(P: int, x: int, r: int) -> list[int]:
    """按用户给出的 gcd 轮序式收集所有可见小素数。

    k=0 项解释为 gcd(x,r)>1；k>=1 项解释为 gcd(kx+r,P-k)>1。
    """
    hits = set(q for q in prime_factors(math.gcd(x, r)) if q < P)
    for k in range(1, P - 1):
        g = math.gcd(k * x + r, P - k)
        for q in prime_factors(g):
            if q < P:
                hits.add(q)
    return sorted(hits)


def phase(P: int, x: int, q: int) -> int:
    """计算 q 对行 x 的覆盖相位 rho_q(x)=-xP mod q。"""
    return (-x * P) % q


def positive_representative(residue: int, q: int) -> int:
    """把模 q 的 0 相位改写成列代表 q。"""
    return q if residue == 0 else residue


def mu_for_phase(P: int, rho: int, q: int) -> int:
    """计算 1<=r<P 中 r=rho mod q 的列数。"""
    first = positive_representative(rho, q)
    if first > P - 1:
        return 0
    return 1 + (P - 1 - first) // q


def is_zero_row(P: int, x: int) -> bool:
    """判定 x 行是否为 P 以内小素数覆盖的零行。"""
    return all(direct_hits(P, x, r) for r in range(1, P))


def minimal_zero_x(P: int) -> int:
    """直接扫描得到最小零行乘数 x；本脚本只用于小 P 诊断。"""
    for x in range(1, MAX_SCAN + 1):
        if is_zero_row(P, x):
            return x
    raise RuntimeError(f"未在 {MAX_SCAN} 内找到 P={P} 的零行")


def phase_rows(P: int, x: int) -> list[dict[str, Any]]:
    """列出最小解的 q 相位、容量和列集合。"""
    rows = []
    for q in primes_lt(P):
        rho = phase(P, x, q)
        columns = [r for r in range(1, P) if r % q == rho]
        rows.append(
            {
                "q": q,
                "rho_q": rho,
                "positive_representative": positive_representative(rho, q),
                "mu_q": mu_for_phase(P, rho, q),
                "covered_columns": columns,
            }
        )
    return rows


def label_rows(P: int, x: int) -> list[dict[str, Any]]:
    """给出每一列的覆盖素数与等价 gcd 见证。"""
    rows = []
    for r in range(1, P):
        hits = direct_hits(P, x, r)
        first_q = hits[0]
        prime_modulus_k = P - first_q
        least_wheel_k = min(
            k
            for k in range(1, P - 1)
            if (P - k) % first_q == 0 and (k * x + r) % first_q == 0
        )
        rows.append(
            {
                "r": r,
                "xP_plus_r": x * P + r,
                "small_prime_hits": hits,
                "first_q": first_q,
                "least_wheel_k_for_first_q": least_wheel_k,
                "prime_modulus_gcd_witness": {
                    "k": prime_modulus_k,
                    "modulus_P_minus_k": first_q,
                    "gcd_value": math.gcd(prime_modulus_k * x + r, first_q),
                },
            }
        )
    return rows


def coverage_summary(P: int, x: int) -> dict[str, Any]:
    """统计相位覆盖的容量、重叠债和标签分布。"""
    labels = label_rows(P, x)
    multiplicities = [len(item["small_prime_hits"]) for item in labels]
    phase_capacity = sum(item["mu_q"] for item in phase_rows(P, x))
    return {
        "total_columns": P - 1,
        "total_phase_capacity_sum_mu": phase_capacity,
        "total_column_hits": sum(multiplicities),
        "overlap_debt": sum(max(0, m - 1) for m in multiplicities),
        "max_column_multiplicity": max(multiplicities),
        "multiplicity_histogram": dict(sorted(Counter(multiplicities).items())),
        "first_factor_histogram": dict(sorted(Counter(item["first_q"] for item in labels).items())),
        "capacity_identity_ok": phase_capacity == sum(multiplicities),
        "zero_row_overlap_identity_ok": phase_capacity == (P - 1) + sum(max(0, m - 1) for m in multiplicities),
    }


def residual_columns(P: int, x: int, cutoff: int) -> list[int]:
    """返回未被 q<=cutoff 覆盖的列。"""
    small = [q for q in primes_lt(P) if q <= cutoff]
    return [
        r
        for r in range(1, P)
        if not any(r % q == phase(P, x, q) for q in small)
    ]


def suffix_effective_columns(P: int, x: int, cutoff: int) -> set[int]:
    """返回 q>cutoff 的后缀素数实际命中的列集合。"""
    large = [q for q in primes_lt(P) if q > cutoff]
    hit: set[int] = set()
    for q in large:
        rho = phase(P, x, q)
        hit.update(r for r in range(1, P) if r % q == rho)
    return hit


def suffix_capacity(P: int, x: int, cutoff: int) -> int:
    """返回 q>cutoff 的原始相位容量。"""
    return sum(mu_for_phase(P, phase(P, x, q), q) for q in primes_lt(P) if q > cutoff)


def obstruction_for_x(P: int, x: int) -> dict[str, Any]:
    """在 x<=P 的早期区间中寻找容量缺口或相位缺陷。"""
    cutoffs = primes_lt(P)[:-1]
    full_uncovered = [r for r in range(1, P) if not direct_hits(P, x, r)]
    best_capacity: dict[str, Any] | None = None
    best_effective: dict[str, Any] | None = None
    for cutoff in cutoffs:
        residual = residual_columns(P, x, cutoff)
        suffix_hit = suffix_effective_columns(P, x, cutoff)
        effective = len(set(residual) & suffix_hit)
        cap = suffix_capacity(P, x, cutoff)
        row = {
            "cutoff": cutoff,
            "residual_size": len(residual),
            "suffix_raw_capacity": cap,
            "suffix_effective_hits_inside_residual": effective,
            "capacity_gap_residual_minus_raw": len(residual) - cap,
            "effective_gap_residual_minus_hits": len(residual) - effective,
            "uncovered_columns": full_uncovered,
        }
        if best_capacity is None or row["capacity_gap_residual_minus_raw"] > best_capacity[
            "capacity_gap_residual_minus_raw"
        ]:
            best_capacity = row
        if best_effective is None or row["effective_gap_residual_minus_hits"] > best_effective[
            "effective_gap_residual_minus_hits"
        ]:
            best_effective = row
    assert best_capacity is not None and best_effective is not None
    mode = "capacity_deficit" if best_capacity["capacity_gap_residual_minus_raw"] > 0 else "pure_phase_defect"
    return {
        "x": x,
        "zero_row": not full_uncovered,
        "uncovered_columns": full_uncovered,
        "best_capacity_cut": best_capacity,
        "best_effective_cut": best_effective,
        "obstruction_mode": mode,
    }


def early_window_obstruction_summary(P: int) -> dict[str, Any]:
    """汇总 1<=x<=P 的早期窗口排斥模式。"""
    rows = [obstruction_for_x(P, x) for x in range(1, P + 1)]
    capacity_rows = [row for row in rows if row["obstruction_mode"] == "capacity_deficit"]
    phase_rows_only = [row for row in rows if row["obstruction_mode"] == "pure_phase_defect"]
    return {
        "x_range_checked": f"1<=x<={P}",
        "all_x_le_P_obstructed": all(row["best_effective_cut"]["effective_gap_residual_minus_hits"] > 0 for row in rows),
        "capacity_deficit_count": len(capacity_rows),
        "pure_phase_defect_count": len(phase_rows_only),
        "weakest_capacity_margin": min(
            row["best_capacity_cut"]["capacity_gap_residual_minus_raw"] for row in rows
        ),
        "phase_only_witnesses": [
            {
                "x": row["x"],
                "uncovered_columns": row["uncovered_columns"],
                "best_capacity_cut": row["best_capacity_cut"],
            }
            for row in phase_rows_only
        ],
    }


def final_tail_cut_summary(P: int) -> dict[str, Any]:
    """固定 cutoff 为第二大素数，只检验最大尾素数是否容量不足。"""
    qs = primes_lt(P)
    if len(qs) < 2:
        return {}
    cutoff = qs[-2]
    tail_prime = qs[-1]
    witness_rows = []
    min_gap = 10**9
    for x in range(1, P + 1):
        residual = residual_columns(P, x, cutoff)
        cap = mu_for_phase(P, phase(P, x, tail_prime), tail_prime)
        suffix_hit = suffix_effective_columns(P, x, cutoff)
        effective = len(set(residual) & suffix_hit)
        gap = len(residual) - cap
        min_gap = min(min_gap, gap)
        if gap <= 0:
            witness_rows.append(
                {
                    "x": x,
                    "residual_size": len(residual),
                    "tail_capacity": cap,
                    "tail_effective_hits_inside_residual": effective,
                    "gap": gap,
                    "uncovered_columns": [r for r in range(1, P) if not direct_hits(P, x, r)],
                }
            )
    return {
        "cutoff_second_largest_prime": cutoff,
        "tail_largest_prime": tail_prime,
        "min_residual_minus_tail_capacity_gap_for_x_le_P": min_gap,
        "all_x_le_P_have_strict_final_tail_capacity_deficit": not witness_rows,
        "nonpositive_gap_witnesses": witness_rows,
    }


def equivalence_check(P: int, x_values: list[int]) -> bool:
    """抽样核验直接小素数覆盖与轮序 gcd 覆盖完全一致。"""
    for x in x_values:
        for r in range(1, P):
            if direct_hits(P, x, r) != wheel_sequence_hits(P, x, r):
                return False
    return True


def build_rows() -> list[dict[str, Any]]:
    """生成指定 P 的最小 x、相位和早期窗口审计。"""
    rows: list[dict[str, Any]] = []
    for P in P_VALUES:
        x_min = minimal_zero_x(P)
        rows.append(
            {
                "P": P,
                "primes_q_lt_P": primes_lt(P),
                "minimal_alignment_x": x_min,
                "one_indexed_zero_row": x_min + 1,
                "x_over_P": round(x_min / P, 12),
                "x_gt_P": x_min > P,
                "equivalence_checked_for_x_le_P_and_x_min": equivalence_check(P, list(range(1, P + 1)) + [x_min]),
                "phase_rows": phase_rows(P, x_min),
                "label_rows": label_rows(P, x_min),
                "coverage_summary": coverage_summary(P, x_min),
                "early_window_obstruction": early_window_obstruction_summary(P),
                "final_tail_cut": final_tail_cut_summary(P),
            }
        )
    return rows


def extended_capacity_probe_rows() -> list[dict[str, Any]]:
    """扩展扫描早期窗口中容量缺口是否排除全部 x<=P。"""
    rows: list[dict[str, Any]] = []
    for P in [p for p in range(13, EXTENDED_CAPACITY_PRIME_LIMIT + 1) if p in primes_lt(p + 1)]:
        summary = early_window_obstruction_summary(P)
        rows.append(
            {
                "P": P,
                "capacity_deficit_count": summary["capacity_deficit_count"],
                "pure_phase_defect_count": summary["pure_phase_defect_count"],
                "weakest_capacity_margin": summary["weakest_capacity_margin"],
                "phase_only_witnesses": summary["phase_only_witnesses"],
                "final_tail_cut": final_tail_cut_summary(P),
            }
        )
    return rows


def theorem_rows() -> list[dict[str, str]]:
    """列出本扫描形成的数学结论边界。"""
    return [
        {
            "name": "wheel_gcd_equivalence",
            "statement": "q|xP+r iff x==-r*P^{-1} mod q iff gcd((P-q)x+r,q)=q; hence the k-wheel gcd system is equivalent when prime divisibility, not only a fixed k, is allowed.",
            "status": "closed",
        },
        {
            "name": "minimal_alignment_scan",
            "statement": "For P=13,17,19,23,29,31 the least x satisfying every column is computed by exact divisibility, then replayed by the wheel gcd equations.",
            "status": "closed_for_requested_P",
        },
        {
            "name": "capacity_deficit_cut",
            "statement": "For cutoff z, zero row requires |R_z(x)| <= C_z(x)=sum_{q>z} mu_q(x); if |R_z|>C_z then x cannot be a zero row.",
            "status": "closed_as_necessary_inequality",
        },
        {
            "name": "effective_phase_defect_cut",
            "statement": "Even when raw capacity is enough, zero row still requires R_z(x) subset union_{q>z} A_q(x); failure is the exact phase-defect residue obstruction.",
            "status": "closed_as_exact_obstruction",
        },
        {
            "name": "final_tail_cut_probe",
            "statement": "For tested P>=29, taking z as the second largest prime below P leaves only the largest tail prime and already gives |R_z(x)|>mu_tail(x) for every 1<=x<=P.",
            "status": "diagnostic_strong_candidate",
        },
        {
            "name": "uniform_lower_bound_gap",
            "statement": "A global proof of X(P)>P still needs a non-tautological lower bound forcing capacity deficit, with only exceptional equality cases routed as registered phase defects.",
            "status": "open",
        },
    ]


def source_hashes() -> dict[str, str]:
    """登记依赖文件哈希。"""
    result = {
        "experiments/prime_matrix_inverse_alignment_min_x_phase_scan_router.py": sha256(Path(__file__).resolve())
    }
    for path in [OUT_LEDGER, *SOURCE_FILES]:
        if path.exists():
            result[str(path.relative_to(ROOT))] = sha256(path)
    return result


def build_result(rows: list[dict[str, Any]], extended_probe: list[dict[str, Any]]) -> dict[str, Any]:
    """构造总证书。"""
    all_equiv = all(row["equivalence_checked_for_x_le_P_and_x_min"] for row in rows)
    all_gt = all(row["x_gt_P"] for row in rows)
    all_obstructed = all(row["early_window_obstruction"]["all_x_le_P_obstructed"] for row in rows)
    extended_phase_exceptions = [
        (row["P"], item["x"])
        for row in extended_probe
        for item in row["phase_only_witnesses"]
    ]
    return {
        "certificate_type": "prime_matrix_inverse_alignment_min_x_phase_scan_router",
        "status": "inverse_alignment_min_x_phase_scan_closed_for_requested_P_uniform_bound_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_for_global_proof": True,
        "requested_P_values": P_VALUES,
        "wheel_gcd_equivalence_checked": all_equiv,
        "all_requested_minimal_x_gt_P": all_gt,
        "all_early_x_le_P_obstructed_by_exact_phase_scan": all_obstructed,
        "extended_capacity_probe_prime_limit": EXTENDED_CAPACITY_PRIME_LIMIT,
        "extended_capacity_probe_rows": extended_probe,
        "extended_probe_phase_only_exceptions": extended_phase_exceptions,
        "extended_probe_no_phase_exceptions_from_P_ge_29": all(
            row["P"] < 29 or row["pure_phase_defect_count"] == 0 for row in extended_probe
        ),
        "extended_probe_final_tail_strict_capacity_deficit_from_P_ge_29": all(
            row["P"] < 29 or row["final_tail_cut"]["all_x_le_P_have_strict_final_tail_capacity_deficit"]
            for row in extended_probe
        ),
        "uniform_lower_bound_inequality_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": "ExactZeroRowXDrivenSameParameterBudgetRunnerOrAnalyticEnvelope",
        "hardpoint_after_router": "UniformCapacityDeficitOrRegisteredPhaseDefectLowerBoundForAllEarlyX",
        "next_direct_attack_target": "UniformCapacityDeficitOrRegisteredPhaseDefectLowerBoundForAllEarlyX",
        "theorem_rows": theorem_rows(),
        "scan_rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "用户提出的轮序 gcd 方程组在素因子可选意义下与 `q|xP+r` 完全等价；"
            "对请求的 P=13,17,19,23,29,31，最小对齐解分别为 168、1210、3658、58、5209、60794，"
            "全部大于 P。早期窗口 `1<=x<=P` 中，多数 x 已由 cutoff 容量缺口排除；"
            "少数例外表现为 raw capacity 足够但后缀相位没有命中残洞的 pure phase defect；"
            "扩展到 P<=101 时，纯相位例外只出现在 (17,12) 与 (23,14)；"
            "并且从 P>=29 起，第二大素数 cutoff 后只剩最大尾素数时已经有严格容量缺口。"
            "因此最窄可攻全局输入不是再求样本，而是证明统一的“容量缺口或登记相位缺陷”下界。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写出 Markdown 摘要。"""
    lines: list[str] = [
        "# Prime Matrix inverse alignment 最小 x 相位扫描路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"wheel_gcd_equivalence_checked={fmt_bool(result['wheel_gcd_equivalence_checked'])}",
        f"all_requested_minimal_x_gt_P={fmt_bool(result['all_requested_minimal_x_gt_P'])}",
        f"uniform_lower_bound_inequality_proved={fmt_bool(result['uniform_lower_bound_inequality_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 等价式",
        "",
        "对任意素数 `q<P`：",
        "",
        "```text",
        "q | xP+r",
        "<=> x == -r*P^{-1} (mod q)",
        "<=> q | (P-q)x+r",
        "<=> gcd((P-q)x+r, q)=q.",
        "```",
        "",
        "因此用户的 `gcd(kx+r,P-k)` 轮序系统是等价的；其中 `k=P-q` 给出模数正好为 `q` 的规范见证。`gcd(x,r)>1` 是有效但冗余的快捷项。",
        "",
        "## 2. 最小对齐解",
        "",
        "| P | primes q<P | minimal x | one-indexed row | x/P | overlap debt | first-factor histogram |",
        "| --- | --- | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in result["scan_rows"]:
        summary = row["coverage_summary"]
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{row['P']}`",
                    f"`{row['primes_q_lt_P']}`",
                    f"`{row['minimal_alignment_x']}`",
                    f"`{row['one_indexed_zero_row']}`",
                    f"`{row['x_over_P']}`",
                    f"`{summary['overlap_debt']}`",
                    f"`{summary['first_factor_histogram']}`",
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 3. 相位向量",
            "",
            "| P | phase vector rho_q/mu_q |",
            "| --- | --- |",
        ]
    )
    for row in result["scan_rows"]:
        vector = [(item["q"], item["rho_q"], item["mu_q"]) for item in row["phase_rows"]]
        lines.append(f"| `{row['P']}` | `{table_cell(vector)}` |")
    lines.extend(
        [
            "",
            "## 4. 早期窗口排斥模式",
            "",
            "| P | checked | capacity deficit x-count | pure phase defect x-count | weakest raw capacity margin | final-tail gap | phase-only witnesses |",
            "| --- | --- | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for row in result["scan_rows"]:
        obs = row["early_window_obstruction"]
        tail = row["final_tail_cut"]
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{row['P']}`",
                    f"`{obs['x_range_checked']}`",
                    f"`{obs['capacity_deficit_count']}`",
                    f"`{obs['pure_phase_defect_count']}`",
                    f"`{obs['weakest_capacity_margin']}`",
                    f"`{tail['min_residual_minus_tail_capacity_gap_for_x_le_P']}`",
                    f"`{table_cell(obs['phase_only_witnesses'])}`",
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 5. 扩展容量探针",
            "",
            f"扩展扫描范围：素数 `13<=P<={result['extended_capacity_probe_prime_limit']}`。",
            "",
            "| P | capacity deficit x-count | pure phase defect x-count | weakest raw margin | final-tail cutoff/tail | final-tail min gap | phase-only witnesses |",
            "| --- | ---: | ---: | ---: | --- | ---: | --- |",
        ]
    )
    for row in result["extended_capacity_probe_rows"]:
        tail = row["final_tail_cut"]
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{row['P']}`",
                    f"`{row['capacity_deficit_count']}`",
                    f"`{row['pure_phase_defect_count']}`",
                    f"`{row['weakest_capacity_margin']}`",
                    f"`{tail['cutoff_second_largest_prime']}/{tail['tail_largest_prime']}`",
                    f"`{tail['min_residual_minus_tail_capacity_gap_for_x_le_P']}`",
                    f"`{table_cell(row['phase_only_witnesses'])}`",
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 6. 下界控制目标",
            "",
            "令 `R_z(x)` 为未被 `q<=z` 覆盖的残洞列，`A_q(x)` 为 `q` 的相位列集，",
            "`C_z(x)=sum_{q>z} |A_q(x)|`，`E_z(x)=|R_z(x) cap union_{q>z} A_q(x)|`。",
            "",
            "零行必要条件是：",
            "",
            "```text",
            "|R_z(x)| <= E_z(x) <= C_z(x).",
            "```",
            "",
            "所以若能对所有 `1<=x<=P` 找到一个 cutoff `z` 使",
            "",
            "```text",
            "|R_z(x)| > C_z(x)   或   C_z(x)>=|R_z(x)| 但 |R_z(x)|>E_z(x),",
            "```",
            "",
            "就得到 `X(P)>P`。本次样本显示：容量缺口已经排除绝大多数早期行；扩展探针中 `P>=29` 未出现纯相位例外。"
            "更强的是，`P>=29` 时取 `z` 为第二大素数 `<P`，只留下最大尾素数，已经出现严格容量缺口。"
            "这提示可优先证明 final-tail 容量缺口不等式；若小 P 或等号态出现，则接入 PDEC/SAE/ColumnCRT 登记缺陷线。",
            "",
            "## 7. 判定边界",
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
            "## 8. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for name, digest in sorted(result["source_hashes"].items()):
        lines.append(f"| `{table_cell(name)}` | `{digest}` |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """生成 JSON、数据账本与 Markdown 证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    rows = build_rows()
    extended_probe = extended_capacity_probe_rows()
    OUT_LEDGER.write_text(
        json.dumps(
            {
                "ledger_type": "inverse_alignment_min_x_phase_scan_ledger",
                "requested_P_values": P_VALUES,
                "extended_capacity_prime_limit": EXTENDED_CAPACITY_PRIME_LIMIT,
                "rows": rows,
                "extended_capacity_probe_rows": extended_probe,
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    result = build_result(rows, extended_probe)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result)
    print(result["status"])
    print("minimal_x_table=" + json.dumps({row["P"]: row["minimal_alignment_x"] for row in rows}, sort_keys=True))
    print("extended_phase_only_exceptions=" + json.dumps(result["extended_probe_phase_only_exceptions"]))
    print(f"wheel_gcd_equivalence_checked={fmt_bool(result['wheel_gcd_equivalence_checked'])}")
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
