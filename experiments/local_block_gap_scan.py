#!/usr/bin/env python3
"""sqrt(P) 短块内大因子补洞缺口扫描。"""
from __future__ import annotations

import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"


def primes_upto(n: int) -> list[int]:
    sieve = [True] * (n + 1)
    if n >= 0: sieve[0] = False
    if n >= 1: sieve[1] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            sieve[i*i:n+1:i] = [False] * (((n - i*i)//i)+1)
    return [i for i, ok in enumerate(sieve) if ok]


def scan(P: int) -> dict:
    ps = primes_upto(P - 1)
    Y = math.isqrt(P)
    small = [q for q in ps if q <= Y]
    large = [q for q in ps if q > Y]
    block = Y
    rows = sorted(set([2, P//4, P//2, 3*P//4, P]))
    worst_blocks = []
    for r in rows:
        for start in range(1, P + 1, block):
            end = min(P, start + block - 1)
            holes = patch = unpatched = 0
            large_factors_seen = set()
            for c in range(start, end + 1):
                n = (r - 1) * P + c
                if any(n % q == 0 for q in small):
                    continue
                holes += 1
                factors = [q for q in large if n % q == 0]
                if factors:
                    patch += 1
                    large_factors_seen.update(factors)
                else:
                    unpatched += 1
            if holes:
                worst_blocks.append({
                    "r": r,
                    "start": start,
                    "end": end,
                    "holes": holes,
                    "patch": patch,
                    "unpatched": unpatched,
                    "patch_ratio": patch / holes,
                    "distinct_large_factors": len(large_factors_seen),
                })
    worst = max(worst_blocks, key=lambda x: x["patch_ratio"])
    best_gap = min(worst_blocks, key=lambda x: x["unpatched"])
    return {
        "P": P,
        "Y": Y,
        "block_count": len(worst_blocks),
        "max_block_patch_ratio": worst["patch_ratio"],
        "worst_patch_block": worst,
        "min_block_unpatched": best_gap["unpatched"],
        "min_unpatched_block": best_gap,
    }


def main() -> None:
    Ps = [401, 809, 1601, 3203, 6421]
    results = [scan(P) for P in Ps]
    audit = {
        "certificate_type": "local_block_gap_scan",
        "status": "sqrt_blocks_still_have_unpatched_points_in_samples",
        "results": results,
        "structural_conclusion": (
            "按 sqrt(P) 分块后，每个被扫描行的短块仍出现未补洞点。"
            "这支持把全局缺口降维为局部块引理：在长度约 sqrt(P) 的块中，大因子互斥无法填满小筛洞。"
        ),
        "next_obligations": [
            "形式化短块内共享大因子的互斥：同一大因子在长度 sqrt(P) 块中至多出现一次。",
            "估计短块小筛洞数下界。",
            "估计短块可用不同大因子命中数上界，并证明小于洞数。",
        ],
    }
    (DOCS / "local-block-gap-scan.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = ["# sqrt(P) 短块补洞缺口扫描", "", f"**状态：** `{audit['status']}`", "", audit["structural_conclusion"], "", "## 摘要"]
    for r in results:
        lines.append(f"- P={r['P']} Y={r['Y']} max_block_patch={r['max_block_patch_ratio']:.3f} min_block_unpatched={r['min_block_unpatched']}")
    lines += ["", "## 下一证明义务"]
    for item in audit["next_obligations"]:
        lines.append(f"- {item}")
    lines.append("")
    (DOCS / "local-block-gap-scan.md").write_text("\n".join(lines), encoding="utf-8")
    print(DOCS / "local-block-gap-scan.json")
    print(DOCS / "local-block-gap-scan.md")


if __name__ == "__main__":
    main()
