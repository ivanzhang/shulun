#!/usr/bin/env python3
"""OSE-local：短差残洞核的大层唯一补洞压力扫描。"""
from __future__ import annotations

import itertools
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


def crt_pair(a: int, m: int, b: int, n: int) -> tuple[int, int]:
    step = ((b - a) % n) * pow(m % n, -1, n) % n
    return (a + m * step) % (m * n), m * n


def crt_system(items: list[tuple[int, int]]) -> tuple[int, int] | None:
    x, mod = 0, 1
    seen = {}
    for residue, q in items:
        residue %= q
        if q in seen:
            if seen[q] != residue:
                return None
            continue
        seen[q] = residue
        x, mod = crt_pair(x, mod, residue, q)
    return x, mod


def holes(P: int, qs: list[int], x: int) -> list[int]:
    covered = set()
    for q in qs:
        residue = (-x * P) % q
        first = residue if residue else q
        for c in range(first, P, q):
            covered.add(c)
    return [c for c in range(1, P) if c not in covered]


def front_min_rows(P: int, qs: list[int]) -> list[dict]:
    rows = [{"x": x, "holes": holes(P, qs, x)} for x in range(1, P)]
    m = min(len(r["holes"]) for r in rows)
    return [r for r in rows if len(r["holes"]) == m]


def short_gap_pairs(K: list[int], P: int) -> list[dict]:
    pairs = []
    for i, c1 in enumerate(K):
        for c2 in K[i + 1 :]:
            d = c2 - c1
            if d * d < P or d <= 6:
                pairs.append({"c1": c1, "c2": c2, "d": d})
    return pairs


def assignment_options(P: int, qs: list[int], c: int, lower: int) -> list[dict]:
    opts = []
    for q in qs:
        if q < lower:
            continue
        residue = (-c * pow(P % q, -1, q)) % q
        opts.append({"c": c, "q": q, "residue": residue})
    return opts


def patch_scan(P: int, row: dict, max_combos: int = 20000) -> dict:
    qs = primes_upto(P - 1)
    K = row["holes"]
    sqrtP = int(P**0.5)
    layers = {
        "medium_or_large": [q for q in qs if q >= 5],
        "large_gt_sqrt": [q for q in qs if q > sqrtP],
    }
    reports = {}
    for name, allowed in layers.items():
        allowed_set = set(allowed)
        options = []
        for c in K:
            opts = []
            for q in qs:
                if q not in allowed_set:
                    continue
                residue = (-c * pow(P % q, -1, q)) % q
                opts.append({"c": c, "q": q, "residue": residue})
            options.append(opts)
        combos_checked = 0
        feasible = []
        for combo in itertools.product(*options):
            combos_checked += 1
            if combos_checked > max_combos:
                break
            by_q = {}
            ok = True
            for item in combo:
                if item["q"] in by_q and by_q[item["q"]] != item["residue"]:
                    ok = False
                    break
                by_q[item["q"]] = item["residue"]
            if not ok:
                continue
            solved = crt_system([(residue, q) for q, residue in by_q.items()])
            if solved is None:
                continue
            x0, mod = solved
            # 前窗口内是否存在同余代表。
            front_reps = []
            if x0 < P and x0 >= 1:
                front_reps.append(x0)
            if x0 == 0:
                first = mod
                if first < P:
                    front_reps.append(first)
            feasible.append(
                {
                    "x0": x0,
                    "mod": mod,
                    "front_reps": front_reps,
                    "scheme": by_q,
                    "distinct_q": sorted(by_q),
                    "combo": list(combo),
                }
            )
        feasible.sort(key=lambda item: (0 if item["front_reps"] else 1, item["x0"], item["mod"]))
        reports[name] = {
            "allowed_count": len(allowed),
            "combos_checked": min(combos_checked, max_combos),
            "feasible_count_sampled": len(feasible),
            "front_rep_count_sampled": sum(1 for item in feasible if item["front_reps"]),
            "best": feasible[:8],
        }
    return {
        "front_x": row["x"],
        "K": K,
        "short_pairs": short_gap_pairs(K, P),
        "layer_reports": reports,
    }


def scan(P: int) -> dict:
    qs = primes_upto(P - 1)
    rows = [r for r in front_min_rows(P, qs) if short_gap_pairs(r["holes"], P)]
    return {"P": P, "rows": [patch_scan(P, row) for row in rows[:4]]}


def main() -> None:
    ps = [23, 29, 31, 37, 41, 47, 53, 59, 67, 71, 83, 97]
    results = [scan(P) for P in ps]
    audit = {
        "certificate_type": "ose_local_patch_pressure",
        "status": "large_layer_patch_constraints_rarely_have_front_representatives_and_do_not_imply_full_cover",
        "results": results,
        "structural_conclusion": (
            "短差核若限制由中大层或大层补洞，CRT 约束经常立刻给出大模数；"
            "即使局部补洞同余有前窗口代表，也只是补核约束，不保证其它列保持覆盖。"
            "因此 OSE-local 必须同时纳入释放项，而不能只看补洞同余。"
        ),
        "next_obligations": [
            "对每个前窗口补核代表计算释放新洞数量，形成 patch-release 不等式。",
            "证明大层补短差对需要不同 q，故同步模数至少为 q1*q2。",
            "将局部补核 CRT 压力与奇偶壳释放合并。",
        ],
    }
    (DOCS / "ose-local-patch-pressure.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")
    lines = [
        "# OSE-local 短差核补洞压力扫描",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        audit["structural_conclusion"],
        "",
        "## 摘要",
    ]
    for result in results:
        lines.append(f"- P={result['P']}")
        for row in result["rows"]:
            compact = {
                name: {
                    "allowed": report["allowed_count"],
                    "checked": report["combos_checked"],
                    "feasible": report["feasible_count_sampled"],
                    "front": report["front_rep_count_sampled"],
                    "best": report["best"][:3],
                }
                for name, report in row["layer_reports"].items()
            }
            lines.append(f"  - x={row['front_x']} K={row['K']} short={row['short_pairs']} layers={compact}")
    lines += ["", "## 下一证明义务"] + [f"- {ob}" for ob in audit["next_obligations"]] + [""]
    (DOCS / "ose-local-patch-pressure.md").write_text("\n".join(lines))
    print(DOCS / "ose-local-patch-pressure.json")
    print(DOCS / "ose-local-patch-pressure.md")


if __name__ == "__main__":
    main()
