#!/usr/bin/env python3
"""不同筛阈值下的覆盖增长缺口实验。"""
from __future__ import annotations

import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"


def primes_upto(n: int) -> list[int]:
    sieve = [True] * (n + 1)
    if n >= 0:
        sieve[0] = False
    if n >= 1:
        sieve[1] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            sieve[i*i:n+1:i] = [False] * (((n - i*i)//i) + 1)
    return [i for i, ok in enumerate(sieve) if ok]


def row_stats(P: int, r: int, Y: int, ps: list[int]) -> dict:
    small = [q for q in ps if q <= Y]
    large = [q for q in ps if q > Y]
    holes = patch = prime_like = 0
    for c in range(1, P + 1):
        n = (r - 1) * P + c
        if any(n % q == 0 for q in small):
            continue
        holes += 1
        if any(n % q == 0 for q in large):
            patch += 1
        else:
            prime_like += 1
    return {
        "r": r,
        "Y": Y,
        "holes": holes,
        "large_patch": patch,
        "unpatched": prime_like,
        "patch_ratio": patch / holes if holes else None,
        "unpatched_ratio": prime_like / holes if holes else None,
    }


def scan_p(P: int) -> dict:
    ps = primes_upto(P - 1)
    rows = sorted(set([2, 3, P // 5, P // 3, P // 2, 2 * P // 3, P - 1, P]))
    thresholds = sorted(set([
        int(P ** (1/3)),
        int(P ** 0.4),
        int(math.isqrt(P)),
        int(P ** 0.6),
        int(P ** (2/3)),
    ]))
    blocks = []
    for Y in thresholds:
        stats = [row_stats(P, r, Y, ps) for r in rows]
        blocks.append({
            "Y": Y,
            "alpha_logP": math.log(Y) / math.log(P),
            "max_patch_ratio": max(s["patch_ratio"] for s in stats if s["patch_ratio"] is not None),
            "min_unpatched_ratio": min(s["unpatched_ratio"] for s in stats if s["unpatched_ratio"] is not None),
            "min_unpatched": min(s["unpatched"] for s in stats),
            "rows": stats,
        })
    return {"P": P, "thresholds": blocks}


def main() -> None:
    Ps = [211, 401, 809, 1601, 3203, 6421]
    results = [scan_p(P) for P in Ps]
    audit = {
        "certificate_type": "growth_gap_threshold_scan",
        "status": "threshold_choice_changes_patch_gap_sqrt_layer_is_natural_but_not_enough_alone",
        "results": results,
        "structural_conclusion": (
            "扫描不同阈值 Y=P^alpha 后，sqrt(P) 层最自然：Y 以下筛掉小因子，Y 以上每个剩余合数只能有少数大因子。"
            "但仅凭粗计数仍接近 Legendre/短区间素数问题，必须叠加 CRT 周期刚性或大因子互斥的短块版本。"
        ),
        "next_obligations": [
            "证明 sqrt(P) 筛后洞数的显式下界。",
            "证明大因子补洞在长度 sqrt(P) 块中的局部上界。",
            "用块级缺口避免直接诉诸完整短区间素数定理。",
        ],
    }
    (DOCS / "growth-gap-threshold-scan.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = ["# 分层阈值增长缺口实验", "", f"**状态：** `{audit['status']}`", "", audit["structural_conclusion"], "", "## 摘要"]
    for item in results:
        parts = [f"Y={b['Y']} alpha={b['alpha_logP']:.2f} max_patch={b['max_patch_ratio']:.3f} min_unpatched={b['min_unpatched']}" for b in item["thresholds"]]
        lines.append(f"- P={item['P']}：" + "; ".join(parts))
    lines += ["", "## 下一证明义务"]
    for item in audit["next_obligations"]:
        lines.append(f"- {item}")
    lines.append("")
    (DOCS / "growth-gap-threshold-scan.md").write_text("\n".join(lines), encoding="utf-8")
    print(DOCS / "growth-gap-threshold-scan.json")
    print(DOCS / "growth-gap-threshold-scan.md")


if __name__ == "__main__":
    main()
