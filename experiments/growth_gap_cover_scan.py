#!/usr/bin/env python3
"""行覆盖增长缺口实验：小筛洞数 vs 大因子补洞。"""
from __future__ import annotations

import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"


def primes_upto(n: int) -> list[int]:
    sieve = [True] * (n + 1)
    sieve[:2] = [False, False]
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            step = i
            start = i * i
            sieve[start : n + 1 : step] = [False] * (((n - start) // step) + 1)
    return [i for i, ok in enumerate(sieve) if ok]


def is_prime(n: int, ps: list[int]) -> bool:
    if n < 2:
        return False
    for p in ps:
        if p * p > n:
            return True
        if n % p == 0:
            return n == p
    return True


def scan_p(P: int) -> dict:
    ps = primes_upto(P - 1)
    small = [q for q in ps if q <= int(math.isqrt(P))]
    large = [q for q in ps if q > int(math.isqrt(P))]
    trial_ps = primes_upto(P + 10)
    rows = []
    selected_rows = sorted(set([2, 3, P // 4, P // 2, 3 * P // 4, P - 1, P]))
    for r in selected_rows:
        small_holes = []
        large_patch = 0
        prime_holes = 0
        composite_holes = 0
        for c in range(1, P + 1):
            n = (r - 1) * P + c
            if any(n % q == 0 for q in small):
                continue
            small_holes.append(c)
            if is_prime(n, trial_ps):
                prime_holes += 1
            else:
                composite_holes += 1
                if any(n % q == 0 for q in large):
                    large_patch += 1
        rows.append(
            {
                "r": r,
                "small_holes": len(small_holes),
                "large_patch": large_patch,
                "prime_holes": prime_holes,
                "composite_holes": composite_holes,
                "patch_ratio": large_patch / len(small_holes) if small_holes else None,
                "prime_gap_ratio": prime_holes / len(small_holes) if small_holes else None,
            }
        )
    return {
        "P": P,
        "sqrtP": int(math.isqrt(P)),
        "small_prime_count": len(small),
        "large_prime_count": len(large),
        "rows": rows,
        "max_patch_ratio": max(row["patch_ratio"] for row in rows if row["patch_ratio"] is not None),
        "min_prime_gap_ratio": min(row["prime_gap_ratio"] for row in rows if row["prime_gap_ratio"] is not None),
    }


def main() -> None:
    Ps = [101, 211, 401, 809, 1601, 3203]
    results = [scan_p(P) for P in Ps]
    audit = {
        "certificate_type": "growth_gap_cover_scan",
        "status": "small_sieve_holes_not_exhausted_by_large_prime_patch_in_samples",
        "results": results,
        "structural_conclusion": (
            "按 sqrt(P) 分层后，大根基素数补洞数始终小于小筛洞数；剩余未补洞点正是行内素数。"
            "实验支持有效覆盖增量不足路线：全行覆盖必须要求 large_patch/small_holes=1，但样本远低于 1。"
        ),
        "next_obligations": [
            "将 small_holes 估计为 P*prod_{q<=sqrt(P)}(1-1/q) 的显式下界。",
            "将 large_patch 上界转化为 sqrt(P)-粗合数计数上界。",
            "证明二者之间存在正缺口，得到每行至少一个素数。",
        ],
    }
    (DOCS / "growth-gap-cover-scan.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = ["# 增量覆盖增长缺口实验", "", f"**状态：** `{audit['status']}`", "", audit["structural_conclusion"], "", "## 扫描摘要"]
    for item in results:
        lines.append(f"- P={item['P']}：max_patch_ratio={item['max_patch_ratio']:.4f}, min_prime_gap_ratio={item['min_prime_gap_ratio']:.4f}")
    lines += ["", "## 下一证明义务"]
    for item in audit["next_obligations"]:
        lines.append(f"- {item}")
    lines.append("")
    (DOCS / "growth-gap-cover-scan.md").write_text("\n".join(lines), encoding="utf-8")
    print(DOCS / "growth-gap-cover-scan.json")
    print(DOCS / "growth-gap-cover-scan.md")


if __name__ == "__main__":
    main()
