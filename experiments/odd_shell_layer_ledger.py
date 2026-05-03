#!/usr/bin/env python3
"""奇素数层在反奇偶壳上的边际覆盖账本。"""
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


def shell(P: int, x: int) -> list[int]:
    return [c for c in range(1, P) if c % 2 != x % 2]


def layer_cols(P: int, x: int, q: int, cols: list[int]) -> list[int]:
    return [c for c in cols if (x * P + c) % q == 0]


def holes(P: int, x: int) -> list[int]:
    qs = [q for q in primes_upto(P - 1) if q != 2]
    return [c for c in shell(P, x) if all((x * P + c) % q for q in qs)]


def best_xs(P: int) -> list[int]:
    values = [(x, len(holes(P, x))) for x in range(1, P)]
    min_h = min(v for _, v in values)
    return [x for x, v in values if v == min_h][:4]


def ledger(P: int, x: int) -> dict:
    qs = [q for q in primes_upto(P - 1) if q != 2]
    cols = shell(P, x)
    covered: set[int] = set()
    rows = []
    total_raw = 0
    for q in qs:
        cols_q = layer_cols(P, x, q, cols)
        raw = len(cols_q)
        new = len([c for c in cols_q if c not in covered])
        overlap = raw - new
        total_raw += raw
        covered.update(cols_q)
        rows.append(
            {
                "q": q,
                "raw": raw,
                "new": new,
                "overlap": overlap,
                "covered_after": len(covered),
                "holes_after": len(cols) - len(covered),
                "cols": cols_q,
            }
        )
    return {
        "x": x,
        "shell_size": len(cols),
        "final_holes": sorted(set(cols) - covered),
        "total_raw": total_raw,
        "total_overlap": total_raw - len(covered),
        "rows": rows,
    }


def scan(P: int) -> dict:
    xs = best_xs(P)
    return {"P": P, "ledgers": [ledger(P, x) for x in xs]}


def main() -> None:
    ps = [23, 29, 31, 37, 41, 47, 53, 59, 67, 71, 83, 97]
    results = [scan(P) for P in ps]
    audit = {
        "certificate_type": "odd_shell_layer_ledger",
        "status": "marginal_new_coverage_decays_due_to_forced_overlap",
        "results": results,
        "structural_conclusion": (
            "奇素数层的原始容量超过所需覆盖量，但边际新增覆盖随层级迅速衰减；"
            "最终缺口等于壳大小减去实际并集，重叠能量吞掉了完成全覆盖所需的最后若干列。"
        ),
        "next_obligations": [
            "证明每个小素数层制造的同余周期会强迫后续层与已覆盖集相交。",
            "把 total_overlap 下界与 final_holes 下界联系起来。",
            "寻找可初等证明的局部版本：最后 m 个洞无法由大素数层全部唯一覆盖。",
        ],
    }
    (DOCS / "odd-shell-layer-ledger.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")
    lines = [
        "# 奇素数层边际覆盖账本",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        audit["structural_conclusion"],
        "",
        "## 摘要",
    ]
    for result in results:
        lines.append(f"- P={result['P']}")
        for item in result["ledgers"]:
            compact = [{"q": r["q"], "raw": r["raw"], "new": r["new"], "overlap": r["overlap"], "holes_after": r["holes_after"]} for r in item["rows"]]
            lines.append(
                f"  - x={item['x']} shell={item['shell_size']} final={item['final_holes']} "
                f"raw={item['total_raw']} overlap={item['total_overlap']} ledger={compact}"
            )
    lines += ["", "## 下一证明义务"] + [f"- {ob}" for ob in audit["next_obligations"]] + [""]
    (DOCS / "odd-shell-layer-ledger.md").write_text("\n".join(lines))
    print(DOCS / "odd-shell-layer-ledger.json")
    print(DOCS / "odd-shell-layer-ledger.md")


if __name__ == "__main__":
    main()
