#!/usr/bin/env python3
"""BPN 着色走廊 smooth-core Rankin 账本证书审计。

用法示例：
  python3 experiments/prime_matrix_bpn_rankin_ledger_certificate_audit.py
  python3 experiments/prime_matrix_bpn_rankin_ledger_certificate_audit.py --input docs/corridors.json

输入 JSON 可选格式：
{
  "p": 1009,
  "k": 9,
  "intervals": [[254016, 254079], [508032, 508095]],
  "phase_moduli": [30, 210],
  "allowed_budget": 40
}
"""

from __future__ import annotations

import argparse
import json
import math
from collections import Counter
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"


def primes_upto(limit: int) -> list[int]:
    """返回不超过 limit 的素数。"""
    if limit < 2:
        return []
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for value in range(2, int(limit**0.5) + 1):
        if sieve[value]:
            for multiple in range(value * value, limit + 1, value):
                sieve[multiple] = False
    return [value for value, ok in enumerate(sieve) if ok]


def smallest_prime_factor(limit: int) -> list[int]:
    """构造最小素因子表。"""
    spf = list(range(limit + 1))
    if limit >= 1:
        spf[1] = 1
    for value in range(2, int(limit**0.5) + 1):
        if spf[value] == value:
            for multiple in range(value * value, limit + 1, value):
                if spf[multiple] == multiple:
                    spf[multiple] = value
    return spf


def squarefree_core_omega(value: int, spf: list[int], p: int) -> tuple[bool, int]:
    """判断 value 是否为由 <p 素数组成的 squarefree core，并返回 omega。"""
    remaining = value
    omega = 0
    last = 0
    while remaining > 1:
        prime = spf[remaining]
        if prime >= p or prime == last:
            return False, omega
        omega += 1
        last = prime
        remaining //= prime
        if remaining % prime == 0:
            return False, omega
    return True, omega


def iter_interval_values(intervals: Iterable[list[int]]) -> Iterable[int]:
    """遍历区间内整数。"""
    for left, right in intervals:
        yield from range(left, right + 1)


def default_certificate() -> dict:
    """生成默认压力样本。"""
    p = 1009
    p2 = p * p
    intervals = []
    # 这些是合成的 dyadic 走廊样本，用于测试证书格式与相位尖峰。
    for base, width in [
        (p2 // 8, 64),
        (p2 // 4, 64),
        (p2 // 2, 64),
        ((3 * p2) // 4, 64),
    ]:
        intervals.append([base, base + width - 1])
    return {
        "p": p,
        "k": 9,
        "intervals": intervals,
        "phase_moduli": [30, 210],
        "allowed_budget": 40.0,
    }


def optimize_rankin(
    core_entries: list[tuple[int, int]],
    s_values: list[float],
) -> dict:
    """在给定 s 网格上优化 Rankin 账本。"""
    best = None
    for s_value in s_values:
        # 每个走廊单独使用右端点 B：d<=B 保证 1 <= (B/d)^s。
        ledger = sum((right / value) ** s_value for value, right in core_entries)
        row = {"s": s_value, "rankin_ledger": ledger}
        if best is None or ledger < best["rankin_ledger"]:
            best = row
    if best is None:
        return {"s": None, "rankin_ledger": 0.0}
    return best


def residue_report(core_values: list[int], moduli: list[int]) -> list[dict]:
    """统计低模相位尖峰。"""
    reports = []
    total = len(core_values)
    for modulus in moduli:
        counts = Counter(value % modulus for value in core_values)
        expected = total / modulus if modulus else 0.0
        residue, count = (None, 0) if not counts else counts.most_common(1)[0]
        reports.append(
            {
                "modulus": modulus,
                "total": total,
                "max_residue": residue,
                "max_count": count,
                "uniform_expected": expected,
                "max_excess": count - expected,
                "max_ratio_to_uniform": None if expected == 0 else count / expected,
            }
        )
    return reports


def audit_certificate(config: dict) -> dict:
    """审计一个 Rankin 账本证书。"""
    p = int(config["p"])
    k = int(config["k"])
    intervals = [[int(a), int(b)] for a, b in config["intervals"]]
    phase_moduli = [int(value) for value in config.get("phase_moduli", [30, 210])]
    allowed_budget = config.get("allowed_budget")
    allowed_budget_float = None if allowed_budget is None else float(allowed_budget)
    max_right = max(right for _, right in intervals)
    spf = smallest_prime_factor(max_right)

    core_values = []
    core_entries = []
    omega_hist: Counter[int] = Counter()
    for left, right in intervals:
        for value in range(left, right + 1):
            is_core, omega = squarefree_core_omega(value, spf, p)
            if is_core and omega <= k:
                core_values.append(value)
                core_entries.append((value, right))
                omega_hist[omega] += 1

    total_width = sum(right - left + 1 for left, right in intervals)
    s_values = [index / 20 for index in range(1, 81)]
    best_rankin = optimize_rankin(core_entries, s_values)
    residue_reports = residue_report(core_values, phase_moduli)

    return {
        "certificate_type": "prime_matrix_bpn_rankin_ledger_certificate_audit",
        "status": "finite_rankin_ledger_computable_with_lowmod_residue_report",
        "p": p,
        "k": k,
        "intervals": intervals,
        "total_width": total_width,
        "core_count_exact": len(core_values),
        "core_density_in_corridors": len(core_values) / total_width if total_width else 0.0,
        "omega_hist": dict(sorted(omega_hist.items())),
        "rankin_best_grid": best_rankin,
        "allowed_budget": allowed_budget_float,
        "rankin_budget_pass": None
        if allowed_budget_float is None
        else best_rankin["rankin_ledger"] <= allowed_budget_float,
        "exact_budget_pass": None
        if allowed_budget_float is None
        else len(core_values) <= allowed_budget_float,
        "rankin_over_exact": None
        if not core_values
        else best_rankin["rankin_ledger"] / len(core_values),
        "phase_reports": residue_reports,
        "review_conclusion": (
            "有限走廊证书可精确计算 smooth-core 计数，并给出 Rankin 账本和低模相位尖峰。"
            "若 Rankin 账本无法进入允许预算，下一步应调参或把最大相位尖峰登记为"
            " low-mod core CRTDefect。"
        ),
    }


def write_markdown(audit: dict, path: Path) -> None:
    """写 Markdown 审计报告。"""
    lines = [
        "# BPN Rankin smooth-core 走廊证书审计",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        audit["review_conclusion"],
        "",
        "## 1. 输入摘要",
        "",
        f"- `P={audit['p']}`，`K={audit['k']}`。",
        f"- 走廊总宽度 `{audit['total_width']}`，精确 smooth-core 数 `{audit['core_count_exact']}`。",
        f"- core 密度 `{audit['core_density_in_corridors']:.6f}`。",
        f"- omega 分布 `{audit['omega_hist']}`。",
        f"- allowed budget `{audit['allowed_budget']}`，Rankin pass `{audit['rankin_budget_pass']}`，exact pass `{audit['exact_budget_pass']}`。",
        "",
        "## 2. Rankin 网格最优",
        "",
        "| best s | Rankin ledger | ledger/exact |",
        "| ---: | ---: | ---: |",
        "| {s} | {ledger:.6f} | {ratio} |".format(
            s=audit["rankin_best_grid"]["s"],
            ledger=audit["rankin_best_grid"]["rankin_ledger"],
            ratio="NA"
            if audit["rankin_over_exact"] is None
            else f"{audit['rankin_over_exact']:.6f}",
        ),
        "",
        "## 3. 低模相位尖峰",
        "",
        "| modulus | max residue | max count | uniform expected | ratio |",
        "| ---: | ---: | ---: | ---: | ---: |",
    ]
    for report in audit["phase_reports"]:
        ratio = report["max_ratio_to_uniform"]
        lines.append(
            "| {modulus} | {residue} | {count} | {expected:.6f} | {ratio} |".format(
                modulus=report["modulus"],
                residue=report["max_residue"],
                count=report["max_count"],
                expected=report["uniform_expected"],
                ratio="NA" if ratio is None else f"{ratio:.6f}",
            )
        )
    lines.extend(
        [
            "",
            "## 4. 审稿含义",
            "",
            "该证书格式把 `finite Rankin smooth-core ledger` 从口头常数义务变成可复核数据：",
            "",
            "```text",
            "走廊列表 -> exact core count + Rankin ledger + low-mod residue spike",
            "```",
            "",
            "若某个正式走廊证书的 Rankin 账本超预算，而低模相位报告显示尖峰，则该尖峰应接入 `low-mod core CRTDefect`。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, help="可选走廊证书 JSON")
    args = parser.parse_args()
    config = default_certificate()
    if args.input:
        config = json.loads(args.input.read_text(encoding="utf-8"))
    audit = audit_certificate(config)
    prefix = DOCS / "prime-matrix-bpn-rankin-ledger-certificate-audit"
    prefix.with_suffix(".json").write_text(
        json.dumps(audit, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(audit, prefix.with_suffix(".md"))
    print(json.dumps(audit, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
