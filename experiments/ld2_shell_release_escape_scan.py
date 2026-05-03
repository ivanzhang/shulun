#!/usr/bin/env python3
"""LD-2：小壳迁移释放集逃逸扫描。"""
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
    return {c for c in range(1, P) if all((x * P + c) % p != 0 for p in B)}


def covered_by(P: int, qs: list[int], x: int, c: int) -> list[int]:
    return [q for q in qs if (x * P + c) % q == 0]


def holes(P: int, qs: list[int], x: int) -> set[int]:
    return {c for c in range(1, P) if not covered_by(P, qs, x, c)}


def front_min_rows(P: int, qs: list[int]) -> list[dict]:
    rows = [{"x": x, "H": holes(P, qs, x)} for x in range(1, P)]
    m = min(len(r["H"]) for r in rows)
    return [r for r in rows if len(r["H"]) == m]


def sig(P: int, x: int, B: list[int]) -> dict[int, int]:
    return {p: (-x * P) % p for p in B}


def scan_transition(P: int, B: list[int], x: int, y: int, K: set[int]) -> dict:
    qs = primes_upto(P - 1)
    Bset = set(B)
    rest = [q for q in qs if q not in Bset]
    Sx = shell(P, x, B)
    Sy = shell(P, y, B)
    release_shell = Sy - Sx
    escaped = [c for c in sorted(release_shell) if not covered_by(P, rest, y, c)]
    killed = sorted(K - holes(P, qs, y))
    born = sorted(holes(P, qs, y) - K)
    covered_release = {
        c: covered_by(P, rest, y, c)
        for c in sorted(release_shell)
        if covered_by(P, rest, y, c)
    }
    return {
        "y": y,
        "sig_change": {p: (sig(P, x, B)[p], sig(P, y, B)[p]) for p in B if sig(P, x, B)[p] != sig(P, y, B)[p]},
        "killed_K": killed,
        "born_full": born,
        "release_shell_size": len(release_shell),
        "release_escape": escaped,
        "release_escape_count": len(escaped),
        "covered_release_sample": dict(list(covered_release.items())[:12]),
    }


def scan(P: int, B: list[int]) -> dict:
    qs = primes_upto(P - 1)
    rows = front_min_rows(P, qs)
    reports = []
    for row in rows[:4]:
        x = row["x"]
        K = row["H"]
        trans = []
        for y in range(1, P):
            if y == x:
                continue
            Hy = holes(P, qs, y)
            killed = K - Hy
            if not killed:
                continue
            if sig(P, x, B) == sig(P, y, B):
                continue
            item = scan_transition(P, B, x, y, K)
            trans.append(item)
        trans.sort(key=lambda item: (item["release_escape_count"], len(item["born_full"]), -len(item["killed_K"]), item["y"]))
        reports.append({"x": x, "K": sorted(K), "sig": sig(P, x, B), "transitions": trans[:20]})
    bad = [
        (r["x"], t)
        for r in reports
        for t in r["transitions"]
        if t["killed_K"] and t["release_escape_count"] == 0
    ]
    return {"P": P, "B": B, "reports": reports, "zero_escape_sample_count": len(bad), "zero_escape_sample": bad[:10]}


def main() -> None:
    ps = [23, 29, 31, 37, 41, 47, 53, 59, 67, 71, 83, 97]
    bases = [[2, 3], [2, 3, 5], [2, 3, 5, 7]]
    results = [{"B": B, "scans": [scan(P, B) for P in ps if max(B) < P]} for B in bases]
    audit = {
        "certificate_type": "ld2_shell_release_escape_scan",
        "status": "shell_migration_release_often_has_escape_but_zero_escape_cases_identify_needed_strengthening",
        "results": results,
        "structural_conclusion": (
            "小壳迁移补洞时，释放壳差集通常含有未被剩余层覆盖的逃逸点；"
            "若出现 release_escape=0，则完整洞集的 born_full 仍通常非空，说明逃逸可能来自原壳重排而非纯壳差集。"
            "因此 LD-2 需扩展为：壳差逃逸或原壳重排释放二者至少其一。"
        ),
        "next_obligations": [
            "区分 release_shell_escape 与 in-shell_rearrangement_release。",
            "证明小壳签名改变且补核时，二者不能同时为零。",
            "把该二择一定理接入列缺陷流。",
        ],
    }
    (DOCS / "ld2-shell-release-escape-scan.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")
    lines = [
        "# LD-2 小壳迁移释放逃逸扫描",
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
            lines.append(f"- P={item['P']} zero_escape={item['zero_escape_sample_count']}")
            for report in item["reports"][:2]:
                lines.append(f"  - x={report['x']} K={report['K']} sig={report['sig']} trans={report['transitions'][:5]}")
    lines += ["", "## 下一证明义务"] + [f"- {ob}" for ob in audit["next_obligations"]] + [""]
    (DOCS / "ld2-shell-release-escape-scan.md").write_text("\n".join(lines))
    print(DOCS / "ld2-shell-release-escape-scan.json")
    print(DOCS / "ld2-shell-release-escape-scan.md")


if __name__ == "__main__":
    main()
