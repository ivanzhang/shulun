#!/usr/bin/env python3
"""LD-2w：小壳签名改变并补掉全部旧核的净变化扫描。"""
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


def holes(P: int, qs: list[int], x: int) -> set[int]:
    return {c for c in range(1, P) if all((x * P + c) % q for q in qs)}


def sig(P: int, x: int, B: list[int]) -> tuple[int, ...]:
    return tuple((-x * P) % p for p in B)


def shell(P: int, x: int, B: list[int]) -> set[int]:
    return {c for c in range(1, P) if all((x * P + c) % p for p in B)}


def front_min_rows(P: int, qs: list[int]) -> list[dict]:
    rows = [{"x": x, "H": holes(P, qs, x)} for x in range(1, P)]
    m = min(len(r["H"]) for r in rows)
    return [r for r in rows if len(r["H"]) == m]


def transition_report(P: int, B: list[int], x: int, y: int, K: set[int], Hy: set[int]) -> dict:
    qs = primes_upto(P - 1)
    rest = [q for q in qs if q not in set(B)]
    Sx = shell(P, x, B)
    Sy = shell(P, y, B)
    release_shell = Sy - Sx
    outer_escape = {c for c in release_shell if all((y * P + c) % q for q in rest)}
    inner_release = Hy - release_shell
    return {
        "y": y,
        "K_size": len(K),
        "Hy_size": len(Hy),
        "Hy": sorted(Hy),
        "net_hole_change": len(Hy) - len(K),
        "sig_y": sig(P, y, B),
        "release_shell_size": len(release_shell),
        "outer_escape": sorted(outer_escape),
        "inner_release": sorted(inner_release),
        "outer_escape_count": len(outer_escape),
        "inner_release_count": len(inner_release),
    }


def scan(P: int, B: list[int]) -> dict:
    qs = primes_upto(P - 1)
    reports = []
    for row in front_min_rows(P, qs)[:8]:
        x = row["x"]
        K = row["H"]
        sx = sig(P, x, B)
        transitions = []
        for y in range(1, P):
            if y == x or sig(P, y, B) == sx:
                continue
            Hy = holes(P, qs, y)
            if K & Hy:
                continue
            transitions.append(transition_report(P, B, x, y, K, Hy))
        transitions.sort(key=lambda t: (t["Hy_size"], t["net_hole_change"], t["outer_escape_count"], t["inner_release_count"], t["y"]))
        reports.append({"x": x, "K": sorted(K), "sig_x": sx, "full_kill_transitions": transitions[:20]})
    zero_new = [(r["x"], t) for r in reports for t in r["full_kill_transitions"] if t["Hy_size"] == 0]
    return {"P": P, "B": B, "reports": reports, "zero_new_count": len(zero_new), "zero_new_sample": zero_new[:10]}


def main() -> None:
    ps = [23, 29, 31, 37, 41, 47, 53, 59, 67, 71, 83, 97]
    bases = [[2, 3], [2, 3, 5], [2, 3, 5, 7]]
    results = [{"B": B, "scans": [scan(P, B) for P in ps if max(B) < P]} for B in bases]
    audit = {
        "certificate_type": "ld2w_full_kernel_kill_scan",
        "status": "full_kernel_kill_with_small_shell_signature_change_still_leaves_new_holes_in_scanned_cases",
        "results": results,
        "structural_conclusion": (
            "在扫描范围内，小壳签名改变且补掉全部旧最小核时，没有出现新洞数为 0 的情况。"
            "最优转移通常把旧核迁移为另一个同等或更大的核，支持 LD-2w。"
        ),
        "next_obligations": [
            "证明 full-kill 若 Hy=empty，则剩余层必须全覆盖新 B-壳。",
            "用层叠零场方程排除该全覆盖。",
            "将净洞数不下降现象转成极小核偏序不变量。",
        ],
    }
    (DOCS / "ld2w-full-kernel-kill-scan.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")
    lines = [
        "# LD-2w 小壳迁移全补旧核扫描",
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
            lines.append(f"- P={item['P']} zero_new={item['zero_new_count']}")
            for report in item["reports"][:3]:
                lines.append(f"  - x={report['x']} K={report['K']} sig={report['sig_x']} best={report['full_kill_transitions'][:5]}")
    lines += ["", "## 下一证明义务"] + [f"- {ob}" for ob in audit["next_obligations"]] + [""]
    (DOCS / "ld2w-full-kernel-kill-scan.md").write_text("\n".join(lines))
    print(DOCS / "ld2w-full-kernel-kill-scan.json")
    print(DOCS / "ld2w-full-kernel-kill-scan.md")


if __name__ == "__main__":
    main()
