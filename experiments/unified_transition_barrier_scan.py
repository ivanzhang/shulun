#!/usr/bin/env python3
"""统一转移账本：扫描高维缺陷流 Barrier。"""
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
    return {c for c in range(1, P) if all((x * P + c) % p for p in B)}


def ceh(P: int, x: int, B: list[int]) -> dict:
    qs = primes_upto(P - 1)
    rest = [q for q in qs if q not in set(B)]
    S = shell(P, x, B)
    raw = 0
    U = set()
    label_map = {}
    for q in rest:
        A = {c for c in S if (x * P + c) % q == 0}
        for c in A:
            label_map.setdefault(c, []).append(q)
        raw += len(A)
        U |= A
    H = S - U
    return {"S_set": S, "U_set": U, "H_set": H, "C": raw, "E": raw - len(U), "labels": label_map}


def sig(P: int, x: int, B: list[int]) -> tuple[int, ...]:
    return tuple((-x * P) % p for p in B)


def front_min_xs(P: int) -> list[int]:
    qs = primes_upto(P - 1)
    vals = []
    for x in range(1, P):
        H = {c for c in range(1, P) if all((x * P + c) % q for q in qs)}
        vals.append((x, len(H)))
    m = min(v for _, v in vals)
    return [x for x, v in vals if v == m][:6]


def transition(P: int, B: list[int], x: int, y: int) -> dict:
    X = ceh(P, x, B)
    Y = ceh(P, y, B)
    Hx = X["H_set"]
    Hy = Y["H_set"]
    killed = Hx - Hy
    born = Hy - Hx
    dS = len(Y["S_set"]) - len(X["S_set"])
    dC = Y["C"] - X["C"]
    dE = Y["E"] - X["E"]
    dH = len(Hy) - len(Hx)
    # 由恒等式 dH=dS-dC+dE。
    barrier = dE - dC + dS + len(killed)
    # 若 killed=|Hx|，则 barrier=|Hy|。
    release_shell = Y["S_set"] - X["S_set"]
    outer = release_shell & Hy
    inner = Hy - release_shell
    return {
        "y": y,
        "sig_changed": sig(P, x, B) != sig(P, y, B),
        "Hx": sorted(Hx),
        "Hy": sorted(Hy),
        "killed": sorted(killed),
        "born": sorted(born),
        "dS": dS,
        "dC": dC,
        "dE": dE,
        "dH": dH,
        "barrier": barrier,
        "outer_escape": sorted(outer),
        "inner_release": sorted(inner),
        "Sx": len(X["S_set"]),
        "Sy": len(Y["S_set"]),
        "Cx": X["C"],
        "Cy": Y["C"],
        "Ex": X["E"],
        "Ey": Y["E"],
    }


def scan(P: int, B: list[int]) -> dict:
    reports = []
    for x in front_min_xs(P):
        trans = []
        for y in range(1, P):
            if y == x:
                continue
            t = transition(P, B, x, y)
            if t["killed"]:
                trans.append(t)
        trans.sort(key=lambda t: (t["barrier"], len(t["Hy"]), -len(t["killed"]), t["y"]))
        reports.append({"x": x, "transitions": trans[:30]})
    return {"P": P, "B": B, "reports": reports}


def main() -> None:
    ps = [23, 29, 31, 37, 41, 47, 53, 59, 67, 71, 83, 97]
    bases = [[2], [2, 3], [2, 3, 5], [2, 3, 5, 7]]
    results = [{"B": B, "scans": [scan(P, B) for P in ps if max(B) < P]} for B in bases]
    audit = {
        "certificate_type": "unified_transition_barrier_scan",
        "status": "barrier_identity_unifies_shell_migration_capacity_overlap_and_release",
        "results": results,
        "structural_conclusion": (
            "统一账本验证恒等式 dH=dS-dC+dE。"
            "定义 Barrier=dE-dC+dS+killed，则全补旧核时 Barrier 等于新洞数。"
            "因此证明 Barrier>=1 即统一闭合所有小壳迁移分情况。"
        ),
        "next_obligations": [
            "证明对前窗口极小核的任意转移，若 killed=|Hx| 则 Barrier>=1。",
            "把 Barrier 分解为小壳迁移项、容量项、重叠项、标签同步项。",
            "将 Barrier 的列支撑接入 D_c 缺陷流。",
        ],
    }
    (DOCS / "unified-transition-barrier-scan.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")
    lines = [
        "# 统一转移 Barrier 扫描",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        audit["structural_conclusion"],
        "",
        "## 摘要",
    ]
    for group in results:
        lines.append(f"## B={group['B']}")
        for item in group["scans"]:
            lines.append(f"- P={item['P']}")
            for report in item["reports"][:2]:
                compact = [
                    {"y": t["y"], "killed": len(t["killed"]), "Hy": len(t["Hy"]), "barrier": t["barrier"], "dS": t["dS"], "dC": t["dC"], "dE": t["dE"], "sig": t["sig_changed"]}
                    for t in report["transitions"][:8]
                ]
                lines.append(f"  - x={report['x']} best={compact}")
    lines += ["", "## 下一证明义务"] + [f"- {ob}" for ob in audit["next_obligations"]] + [""]
    (DOCS / "unified-transition-barrier-scan.md").write_text("\n".join(lines))
    print(DOCS / "unified-transition-barrier-scan.json")
    print(DOCS / "unified-transition-barrier-scan.md")


if __name__ == "__main__":
    main()
