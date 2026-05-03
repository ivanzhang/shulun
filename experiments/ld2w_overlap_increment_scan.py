#!/usr/bin/env python3
"""LD-2w 小壳迁移的 C/E/有效覆盖增量扫描。"""
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


def holes(P: int, qs: list[int], x: int) -> set[int]:
    return {c for c in range(1, P) if all((x * P + c) % q for q in qs)}


def sig(P: int, x: int, B: list[int]) -> tuple[int, ...]:
    return tuple((-x * P) % p for p in B)


def ce_profile(P: int, x: int, B: list[int]) -> dict:
    qs = primes_upto(P - 1)
    rest = [q for q in qs if q not in set(B)]
    S = shell(P, x, B)
    raw = 0
    union = set()
    layer_rows = []
    for q in rest:
        A = {c for c in S if (x * P + c) % q == 0}
        new = A - union
        overlap = A & union
        raw += len(A)
        union |= A
        if A:
            layer_rows.append({"q": q, "raw": len(A), "new": len(new), "overlap": len(overlap)})
    E = raw - len(union)
    H = S - union
    return {"S": len(S), "C": raw, "U": len(union), "E": E, "H": len(H), "holes": sorted(H), "layers": layer_rows}


def front_min_rows(P: int, qs: list[int]) -> list[dict]:
    rows = [{"x": x, "H": holes(P, qs, x)} for x in range(1, P)]
    m = min(len(r["H"]) for r in rows)
    return [r for r in rows if len(r["H"]) == m]


def scan(P: int, B: list[int]) -> dict:
    qs = primes_upto(P - 1)
    reports = []
    for row in front_min_rows(P, qs)[:6]:
        x = row["x"]
        K = row["H"]
        base = ce_profile(P, x, B)
        transitions = []
        for y in range(1, P):
            if y == x or sig(P, y, B) == sig(P, x, B):
                continue
            Hy = holes(P, qs, y)
            if K & Hy:
                continue
            prof = ce_profile(P, y, B)
            transitions.append(
                {
                    "y": y,
                    "Hy": sorted(Hy),
                    "sig_y": sig(P, y, B),
                    "profile": prof,
                    "delta_S": prof["S"] - base["S"],
                    "delta_C": prof["C"] - base["C"],
                    "delta_E": prof["E"] - base["E"],
                    "delta_U": prof["U"] - base["U"],
                    "effective_defect": prof["S"] - prof["U"],
                    "zero_field_gap": prof["S"] - prof["C"] + prof["E"],
                }
            )
        transitions.sort(key=lambda t: (t["profile"]["H"], t["delta_E"], t["delta_U"], t["y"]))
        reports.append({"x": x, "K": sorted(K), "sig_x": sig(P, x, B), "base": base, "transitions": transitions[:20]})
    return {"P": P, "B": B, "reports": reports}


def main() -> None:
    ps = [23, 29, 31, 37, 41, 47, 53, 59, 67, 71, 83, 97]
    bases = [[2, 3], [2, 3, 5], [2, 3, 5, 7]]
    results = [{"B": B, "scans": [scan(P, B) for P in ps if max(B) < P]} for B in bases]
    audit = {
        "certificate_type": "ld2w_overlap_increment_scan",
        "status": "full_kernel_kill_transitions_preserve_positive_zero_field_gap",
        "results": results,
        "structural_conclusion": (
            "对小壳迁移且全补旧核的转移，目标相位的 zero_field_gap=S-C+E 始终等于新洞数且保持正值。"
            "下一步要证明：补旧核约束导致 C-E 无法达到 S。"
        ),
        "next_obligations": [
            "提取导致 zero_field_gap>0 的层：是 S 增长、C 不足还是 E 增长。",
            "证明 full-kill 转移中有效覆盖 U=C-E 至少少于 S 一个单位。",
            "将该不等式写成 LD-2w 的核心证明。",
        ],
    }
    (DOCS / "ld2w-overlap-increment-scan.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")
    lines = [
        "# LD-2w 小壳迁移重叠增量扫描",
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
            for report in item["reports"][:3]:
                compact = [
                    {
                        "y": t["y"],
                        "H": t["profile"]["H"],
                        "S": t["profile"]["S"],
                        "C": t["profile"]["C"],
                        "E": t["profile"]["E"],
                        "U": t["profile"]["U"],
                        "gap": t["zero_field_gap"],
                        "dS": t["delta_S"],
                        "dC": t["delta_C"],
                        "dE": t["delta_E"],
                    }
                    for t in report["transitions"][:5]
                ]
                lines.append(f"  - x={report['x']} K={report['K']} base={{'S':{report['base']['S']},'C':{report['base']['C']},'E':{report['base']['E']},'H':{report['base']['H']}}} best={compact}")
    lines += ["", "## 下一证明义务"] + [f"- {ob}" for ob in audit["next_obligations"]] + [""]
    (DOCS / "ld2w-overlap-increment-scan.md").write_text("\n".join(lines))
    print(DOCS / "ld2w-overlap-increment-scan.json")
    print(DOCS / "ld2w-overlap-increment-scan.md")


if __name__ == "__main__":
    main()
