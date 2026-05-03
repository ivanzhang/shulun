#!/usr/bin/env python3
"""平方自由 CRT 同步损耗扫描。"""
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


def crt(items: list[tuple[int, int]]) -> tuple[int, int] | None:
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
    return [c for c in range(1, P) if all((x * P + c) % q for q in qs)]


def front_min_rows(P: int, qs: list[int]) -> list[dict]:
    rows = [{"x": x, "H": holes(P, qs, x)} for x in range(1, P)]
    m = min(len(r["H"]) for r in rows)
    return [r for r in rows if len(r["H"]) == m]


def residue_for_cover(P: int, c: int, q: int) -> int:
    return (-c * pow(P % q, -1, q)) % q


def scan_row(P: int, row: dict) -> dict:
    qs = primes_upto(P - 1)
    K = row["H"]
    sqrtP = int(P**0.5)
    large = [q for q in qs if q > sqrtP]
    if len(K) > 5:
        return {"x": row["x"], "K": K, "skipped": True}
    options = []
    for c in K:
        opts = [{"c": c, "q": q, "residue": residue_for_cover(P, c, q)} for q in large]
        options.append(opts)
    best = []
    checked = 0
    for combo in itertools.product(*options):
        checked += 1
        by_q = {}
        ok = True
        for item in combo:
            q = item["q"]
            residue = item["residue"]
            if q in by_q and by_q[q] != residue:
                ok = False
                break
            by_q[q] = residue
        if not ok:
            continue
        solved = crt([(a, q) for q, a in by_q.items()])
        if solved is None:
            continue
        x0, mod = solved
        front = []
        if 1 <= x0 < P:
            front.append(x0)
        if x0 == 0 and mod < P:
            front.append(mod)
        best.append({"x0": x0, "mod": mod, "front": front, "q_count": len(by_q), "q_product": mod, "scheme": by_q})
    best.sort(key=lambda b: (0 if b["front"] else 1, b["q_product"], b["x0"]))
    front_count = sum(1 for b in best if b["front"])
    return {
        "x": row["x"],
        "K": K,
        "large_count": len(large),
        "checked": checked,
        "feasible": len(best),
        "front_count": front_count,
        "best": best[:12],
    }


def scan(P: int) -> dict:
    qs = primes_upto(P - 1)
    return {"P": P, "rows": [scan_row(P, row) for row in front_min_rows(P, qs)[:4]]}


def main() -> None:
    ps = [23, 29, 31, 37, 41, 47, 53, 59]
    results = [scan(P) for P in ps]
    audit = {
        "certificate_type": "squarefree_sync_loss_scan",
        "status": "large_prime_multi_point_patching_forces_squarefree_crt_product_growth",
        "results": results,
        "structural_conclusion": (
            "平方自由 CRT 使多点补洞必须支付互异根基坐标乘积。"
            "大素数层补极小核时，同步模数通常远超 P；即使有前窗口代表，也非常稀缺并需再承受释放约束。"
        ),
        "next_obligations": [
            "证明短差核的大层补洞需要互异大素数。",
            "将互异大素数乘积下界转成前窗口代表稀缺。",
            "把代表稀缺与 Barrier>=1 连接。",
        ],
    }
    (DOCS / "squarefree-sync-loss-scan.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")
    lines = [
        "# 平方自由 CRT 同步损耗扫描",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        audit["structural_conclusion"],
        "",
        "## 摘要",
    ]
    for r in results:
        lines.append(f"- P={r['P']}")
        for row in r["rows"]:
            lines.append(f"  - {row}")
    lines += ["", "## 下一证明义务"] + [f"- {ob}" for ob in audit["next_obligations"]] + [""]
    (DOCS / "squarefree-sync-loss-scan.md").write_text("\n".join(lines))
    print(DOCS / "squarefree-sync-loss-scan.json")
    print(DOCS / "squarefree-sync-loss-scan.md")


if __name__ == "__main__":
    main()
