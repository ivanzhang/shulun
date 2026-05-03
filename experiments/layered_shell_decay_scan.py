#!/usr/bin/env python3
"""小素因子逐步累积约束的层叠衰减账本。"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"


def primes_upto(n: int) -> list[int]:
    sieve = [True] * (n + 1)
    if n >= 0:
        sieve[0] = False
    if n >= 1:
        sieve[1] = False
    for value in range(2, int(n**0.5) + 1):
        if sieve[value]:
            sieve[value * value : n + 1 : value] = [False] * (((n - value * value) // value) + 1)
    return [value for value, keep in enumerate(sieve) if keep]


def shell(P: int, x: int, B: list[int]) -> set[int]:
    return {
        c
        for c in range(1, P)
        if all((x * P + c) % p != 0 for p in B)
    }


def full_holes(P: int, qs: list[int], x: int) -> set[int]:
    return shell(P, x, qs)


def residual_ledger(P: int, x: int) -> dict:
    qs = primes_upto(P - 1)
    H = full_holes(P, qs, x)
    levels = []
    previous_shell = set(range(1, P))
    for k in range(1, len(qs) + 1):
        B = qs[:k]
        S = shell(P, x, B)
        q = B[-1]
        removed = sorted(previous_shell - S)
        expected = len(previous_shell) / q
        remaining_qs = qs[k:]
        raw_remaining = 0
        covered_by_remaining = set()
        incidence_overlap = 0
        for r in remaining_qs:
            A = {c for c in S if (x * P + c) % r == 0}
            raw_remaining += len(A)
            incidence_overlap += len(A & covered_by_remaining)
            covered_by_remaining |= A
        levels.append(
            {
                "q_added": q,
                "B": B,
                "shell_size": len(S),
                "removed_by_q": len(removed),
                "expected_removed_prev_over_q": expected,
                "decay_ratio": None if not previous_shell else len(S) / len(previous_shell),
                "density_vs_P": len(S) / (P - 1),
                "full_holes_inside": sorted(H),
                "remaining_raw_capacity": raw_remaining,
                "remaining_union_cover": len(covered_by_remaining),
                "remaining_overlap_energy": raw_remaining - len(covered_by_remaining),
                "identity_holes": len(S) - len(covered_by_remaining),
                "removed_sample": removed[:12],
            }
        )
        previous_shell = S
    return {"x": x, "hole_count": len(H), "holes": sorted(H), "levels": levels}


def best_xs(P: int, limit: int = 4) -> list[int]:
    qs = primes_upto(P - 1)
    vals = [(x, len(full_holes(P, qs, x))) for x in range(1, P)]
    min_h = min(v for _, v in vals)
    return [x for x, v in vals if v == min_h][:limit]


def scan(P: int) -> dict:
    return {"P": P, "best_ledgers": [residual_ledger(P, x) for x in best_xs(P)]}


def main() -> None:
    ps = [23, 29, 31, 37, 41, 47, 53, 59, 67, 71, 83, 97]
    results = [scan(P) for P in ps]
    audit = {
        "certificate_type": "layered_shell_decay_scan",
        "status": "small_prime_constraints_create_multiplicative_decay_but_residual_pressure_moves_to_overlap_energy",
        "results": results,
        "structural_conclusion": (
            "小素因子逐步加入时，候选壳按近似乘法因子 (1-1/q) 衰减；"
            "但衰减并不等于证明完成，因为剩余中大层的原始容量与重叠能量同时变化。"
            "矛盾场应写成每层恒等式：壳大小 - 剩余并集覆盖 = 最终洞数。"
        ),
        "next_obligations": [
            "将每层 identity_holes 恒等式转写为动力系统不变量。",
            "分析加入 q 后 remaining_overlap_energy 的增减，寻找单调 Lyapunov 量。",
            "证明衰减链不能在前窗口达到 identity_holes=0。",
        ],
    }
    (DOCS / "layered-shell-decay-scan.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")
    lines = [
        "# 小素因子层叠衰减账本",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        audit["structural_conclusion"],
        "",
        "## 摘要",
    ]
    for result in results:
        lines.append(f"- P={result['P']}")
        for led in result["best_ledgers"]:
            compact = [
                {
                    "q": lv["q_added"],
                    "S": lv["shell_size"],
                    "ratio": None if lv["decay_ratio"] is None else round(lv["decay_ratio"], 4),
                    "raw": lv["remaining_raw_capacity"],
                    "union": lv["remaining_union_cover"],
                    "E": lv["remaining_overlap_energy"],
                    "holes": lv["identity_holes"],
                }
                for lv in led["levels"]
            ]
            lines.append(f"  - x={led['x']} H={led['holes']} levels={compact}")
    lines += ["", "## 下一证明义务"] + [f"- {ob}" for ob in audit["next_obligations"]] + [""]
    (DOCS / "layered-shell-decay-scan.md").write_text("\n".join(lines))
    print(DOCS / "layered-shell-decay-scan.json")
    print(DOCS / "layered-shell-decay-scan.md")


if __name__ == "__main__":
    main()
