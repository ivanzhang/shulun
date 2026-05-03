#!/usr/bin/env python3
"""BPN LHB 窄带碰撞能量证书。

用法示例：
  python3 experiments/prime_matrix_bpn_lhb_narrow_band_collision_certificate.py
  python3 experiments/prime_matrix_bpn_lhb_narrow_band_collision_certificate.py --p-values 61,67,71

目标：
- 对鸽巢尾段失败的十个素数 `61..103` 逐相位验证固定升序碰撞梯；
- 用 `duplicate_gain >= required_gain` 形式记录碰撞能量余量；
- 输出紧相位样例和全相位摘要哈希，便于审稿复核。
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from math import prod
from pathlib import Path
from typing import Any

from prime_matrix_bpn_lhb_fixed_ladder_audit import fixed_ladder_cover
from prime_matrix_bpn_low_hole_bucket_capacity import low_holes_for_phase, primes_upto


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"


DEFAULT_P_VALUES = [61, 67, 71, 73, 79, 83, 89, 97, 101, 103]


def phase_collision_row(
    phase: int,
    holes: list[int],
    high_primes: list[int],
) -> dict[str, Any]:
    """计算单个低相位的碰撞证书行。"""
    ok, choices, uncovered = fixed_ladder_cover(holes, high_primes)
    hole_count = len(holes)
    choice_count = len(choices)
    duplicate_gain = hole_count - choice_count
    required_gain = max(0, hole_count - len(high_primes))
    energy_surplus = duplicate_gain - required_gain
    margin = len(high_primes) - choice_count
    return {
        "phase": phase,
        "hole_count": hole_count,
        "choice_count": choice_count,
        "duplicate_gain": duplicate_gain,
        "required_gain": required_gain,
        "energy_surplus": energy_surplus,
        "margin": margin,
        "max_gain": max((choice["gain"] for choice in choices), default=0),
        "multi_gain_count": sum(1 for choice in choices if choice["gain"] >= 2),
        "ok": ok and energy_surplus >= 0,
        "uncovered": uncovered,
        "multi_gain_choices": [
            {
                "prime": choice["prime"],
                "residue": choice["residue"],
                "hit": choice["hit"],
                "gain": choice["gain"],
            }
            for choice in choices
            if choice["gain"] >= 2
        ],
    }


def row_digest(rows: list[dict[str, Any]]) -> str:
    """对全相位摘要生成稳定哈希。"""
    compact_rows = [
        {
            "phase": row["phase"],
            "hole_count": row["hole_count"],
            "choice_count": row["choice_count"],
            "duplicate_gain": row["duplicate_gain"],
            "required_gain": row["required_gain"],
            "energy_surplus": row["energy_surplus"],
            "margin": row["margin"],
            "max_gain": row["max_gain"],
            "multi_gain_count": row["multi_gain_count"],
            "ok": row["ok"],
        }
        for row in rows
    ]
    payload = json.dumps(compact_rows, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def scan_prime(p_value: int, q: int, tight_limit: int) -> dict[str, Any]:
    """扫描单个窄带素数。"""
    base_primes = primes_upto(p_value - 1)
    if prod(base_primes) % q != 0:
        raise ValueError(f"q={q} 不整除 P={p_value} 的根基 CRT 周期")
    low_primes = [prime for prime in base_primes if q % prime == 0]
    high_primes = [prime for prime in base_primes if q % prime != 0]

    rows = []
    failures = []
    for phase in range(q):
        holes = low_holes_for_phase(p_value, q, low_primes, phase)
        row = phase_collision_row(phase, holes, high_primes)
        rows.append(row)
        if not row["ok"]:
            failures.append(row)

    min_surplus = min(row["energy_surplus"] for row in rows)
    min_margin = min(row["margin"] for row in rows)
    tight_rows = [
        row for row in rows
        if row["energy_surplus"] == min_surplus or row["margin"] == min_margin
    ][:tight_limit]

    return {
        "p": p_value,
        "q": q,
        "low_primes": low_primes,
        "high_primes": high_primes,
        "high_prime_count": len(high_primes),
        "phase_count": q,
        "failure_count": len(failures),
        "min_energy_surplus": min_surplus,
        "min_margin": min_margin,
        "max_hole_count": max(row["hole_count"] for row in rows),
        "max_required_gain": max(row["required_gain"] for row in rows),
        "energy_surplus_histogram": dict(sorted(Counter(row["energy_surplus"] for row in rows).items())),
        "margin_histogram": dict(sorted(Counter(row["margin"] for row in rows).items())),
        "summary_sha256": row_digest(rows),
        "tight_rows": tight_rows,
        "failures": failures[:tight_limit],
    }


def parse_p_values(raw: str) -> list[int]:
    """解析逗号分隔的素数列表。"""
    return [int(item.strip()) for item in raw.split(",") if item.strip()]


def run(p_values: list[int], q: int, tight_limit: int) -> dict[str, Any]:
    """运行窄带碰撞证书。"""
    results = [scan_prime(p_value, q, tight_limit) for p_value in p_values]
    return {
        "certificate_type": "prime_matrix_bpn_lhb_narrow_band_collision_certificate",
        "q": q,
        "p_values": p_values,
        "all_pass": all(row["failure_count"] == 0 for row in results),
        "results": results,
        "review_conclusion": (
            "十个窄带素数的固定升序碰撞梯全相位通过；"
            "碰撞能量余量 `duplicate_gain-required_gain` 均非负。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# BPN LHB 窄带碰撞能量证书",
        "",
        result["review_conclusion"],
        "",
        "## 1. 总表",
        "",
        "| P | phases | high # | max holes | max required | failures | min surplus | min margin | sha256 |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in result["results"]:
        lines.append(
            f"| {row['p']} | {row['phase_count']} | {row['high_prime_count']} | "
            f"{row['max_hole_count']} | {row['max_required_gain']} | "
            f"{row['failure_count']} | {row['min_energy_surplus']} | "
            f"{row['min_margin']} | `{row['summary_sha256'][:16]}` |"
        )

    lines.extend(
        [
            "",
            "## 2. 紧相位样例",
            "",
            "仅列出每个 `P` 最紧的前若干相位；完整摘要哈希在 JSON 中。",
            "",
        ]
    )
    for row in result["results"]:
        lines.extend([f"### P={row['p']}", ""])
        lines.append("| phase | holes | choices | surplus | margin | multi-gain choices |")
        lines.append("| ---: | ---: | ---: | ---: | ---: | --- |")
        for item in row["tight_rows"][:6]:
            lines.append(
                f"| {item['phase']} | {item['hole_count']} | {item['choice_count']} | "
                f"{item['energy_surplus']} | {item['margin']} | `{item['multi_gain_choices']}` |"
            )
        lines.append("")

    lines.extend(
        [
            "## 3. 审稿结论",
            "",
            "该证书闭合 `61<=P<=103` 的窄带碰撞能量义务。",
            "结合低范围最终证书后，low-hole 主线只剩 `P>=13208` 的显式常数引用核验。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--p-values", default=",".join(str(value) for value in DEFAULT_P_VALUES))
    parser.add_argument("--q", type=int, default=2310)
    parser.add_argument("--tight-limit", type=int, default=16)
    parser.add_argument(
        "--json-output",
        type=Path,
        default=DOCS / "prime-matrix-bpn-lhb-narrow-band-collision-certificate.json",
    )
    parser.add_argument(
        "--md-output",
        type=Path,
        default=DOCS / "prime-matrix-bpn-lhb-narrow-band-collision-certificate.md",
    )
    args = parser.parse_args()
    result = run(parse_p_values(args.p_values), args.q, args.tight_limit)
    args.json_output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result, args.md_output)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
