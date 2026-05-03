#!/usr/bin/env python3
"""Barrier 新生列支撑扩散扫描。"""
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


def scan(P: int) -> dict:
    qs = primes_upto(P - 1)
    rows = {x: holes(P, qs, x) for x in range(1, P)}
    new_support = {c: 0 for c in range(1, P)}
    full_kill_support = {c: 0 for c in range(1, P)}
    transitions = []
    for x, Hx in rows.items():
        for y, Hy in rows.items():
            if x == y:
                continue
            killed = Hx - Hy
            if not killed:
                continue
            born = Hy - Hx
            for c in born:
                new_support[c] += 1
            if not (Hx & Hy):
                for c in Hy:
                    full_kill_support[c] += 1
                transitions.append({"x": x, "y": y, "Hx": sorted(Hx), "Hy": sorted(Hy), "born": sorted(born)})
    zero_new_cols = [c for c, v in new_support.items() if v == 0]
    zero_full_cols = [c for c, v in full_kill_support.items() if v == 0]
    return {
        "P": P,
        "new_support": new_support,
        "full_kill_support": full_kill_support,
        "zero_new_cols": zero_new_cols,
        "zero_full_kill_cols": zero_full_cols,
        "full_kill_transition_count": len(transitions),
        "full_kill_sample": transitions[:20],
    }


def main() -> None:
    ps = [13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 83]
    results = [scan(P) for P in ps]
    audit = {
        "certificate_type": "barrier_column_support_scan",
        "status": "new_defect_column_support_spreads_but_full_kill_support_needs_stronger_flow_analysis",
        "results": results,
        "structural_conclusion": (
            "Barrier 新生列支撑在前窗口转移中呈扩散趋势；"
            "列命题需要证明这种支撑不能长期避开固定列。"
            "full-kill 支撑较稀疏，需结合列均衡与镜像周期场。"
        ),
        "next_obligations": [
            "区分所有转移新生支撑与极小核下降链支撑。",
            "证明极小核迁移图的可达支撑覆盖所有列。",
            "将可达支撑与列均衡 T_c 相等连接。",
        ],
    }
    (DOCS / "barrier-column-support-scan.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")
    lines = [
        "# Barrier 新生列支撑扩散扫描",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        audit["structural_conclusion"],
        "",
        "## 摘要",
    ]
    for r in results:
        lines.append(
            f"- P={r['P']} zero_new_cols={r['zero_new_cols']} zero_full_kill_cols={r['zero_full_kill_cols']} "
            f"full_kill_count={r['full_kill_transition_count']} sample={r['full_kill_sample'][:3]}"
        )
    lines += ["", "## 下一证明义务"] + [f"- {ob}" for ob in audit["next_obligations"]] + [""]
    (DOCS / "barrier-column-support-scan.md").write_text("\n".join(lines))
    print(DOCS / "barrier-column-support-scan.json")
    print(DOCS / "barrier-column-support-scan.md")


if __name__ == "__main__":
    main()
