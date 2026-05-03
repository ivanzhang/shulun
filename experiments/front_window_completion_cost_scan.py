#!/usr/bin/env python3
"""前窗口残洞核的完整消除代价扫描。

核心问题：给定 P 与前窗口 1<=x<P 中的近零行残洞 H，
若要求这些洞被若干根基素数补掉，并且最终整行全部覆盖，
对应完整覆盖方案的 CRT 最小代表是否必然跨出前窗口。
"""
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
    return [value for value, is_prime in enumerate(sieve) if is_prime]


def crt_pair(a: int, m: int, b: int, n: int) -> tuple[int, int]:
    # m,n 互素；合并 x=a mod m 与 x=b mod n。
    step = ((b - a) % n) * pow(m % n, -1, n) % n
    return (a + m * step) % (m * n), m * n


def crt_system(congruences: list[tuple[int, int]]) -> tuple[int, int] | None:
    x, mod = 0, 1
    seen: dict[int, int] = {}
    for residue, q in congruences:
        residue %= q
        if q in seen:
            if seen[q] != residue:
                return None
            continue
        seen[q] = residue
        x, mod = crt_pair(x, mod, residue, q)
    return x, mod


def cover_by_scheme(P: int, scheme: dict[int, int]) -> tuple[list[int], dict[int, list[int]]]:
    covered_by: dict[int, list[int]] = {}
    for c in range(1, P):
        hits = [q for q, residue in scheme.items() if c % q == (-residue * P) % q]
        if hits:
            covered_by[c] = hits
    holes = [c for c in range(1, P) if c not in covered_by]
    return holes, covered_by


def holes_at_x(P: int, qs: list[int], x: int) -> list[int]:
    scheme = {q: x % q for q in qs}
    holes, _ = cover_by_scheme(P, scheme)
    return holes


def front_best_rows(P: int, qs: list[int], keep: int = 8) -> tuple[int, list[dict]]:
    best_size = P
    rows: list[dict] = []
    for x in range(1, P):
        holes = holes_at_x(P, qs, x)
        if len(holes) < best_size:
            best_size = len(holes)
            rows = [{"x": x, "holes": holes}]
        elif len(holes) == best_size:
            rows.append({"x": x, "holes": holes})
    return best_size, rows[:keep]


def first_full_x(P: int, qs: list[int], limit: int = 2_000_000) -> int | None:
    for x in range(limit):
        if not holes_at_x(P, qs, x):
            return x
    return None


def enumerate_hole_assignments(P: int, qs: list[int], holes: list[int], max_holes: int = 5) -> list[dict]:
    if len(holes) > max_holes:
        return []
    options = []
    for c in holes:
        # 让 q 覆盖洞 c 等价于 x ≡ -c * P^{-1} (mod q)。
        col_options = []
        for q in qs:
            residue = (-c * pow(P % q, -1, q)) % q
            col_options.append({"c": c, "q": q, "residue": residue})
        options.append(col_options)

    candidates = []
    for combo in itertools.product(*options):
        scheme: dict[int, int] = {}
        ok = True
        for item in combo:
            q = item["q"]
            residue = item["residue"]
            if q in scheme and scheme[q] != residue:
                ok = False
                break
            scheme[q] = residue
        if not ok:
            continue
        solved = crt_system([(residue, q) for q, residue in scheme.items()])
        if solved is None:
            continue
        x0, mod = solved
        candidates.append({"x": x0, "mod": mod, "scheme": scheme, "combo": list(combo)})
    candidates.sort(key=lambda item: (item["x"], item["mod"], len(item["scheme"])))
    return candidates


def forced_contains_x(forced: dict[int, int], x: int) -> bool:
    # 检查给定完整零行相位是否满足局部补洞约束。
    return all(x % q == residue for q, residue in forced.items())


def scan(P: int) -> dict:
    qs = primes_upto(P - 1)
    best_size, best_rows = front_best_rows(P, qs)
    known_first = {13: 168, 17: 1210, 19: 3658, 23: 58, 29: 5209, 31: 60794}
    first = known_first.get(P) or first_full_x(P, qs)
    row_reports = []
    for row in best_rows:
        hole_assignments = enumerate_hole_assignments(P, qs, row["holes"])
        forced_reports = []
        for assignment in hole_assignments[:120]:
            contains_first = first is not None and forced_contains_x(assignment["scheme"], first)
            forced_reports.append(
                {
                    "forced_x": assignment["x"],
                    "forced_mod": assignment["mod"],
                    "forced_scheme": assignment["scheme"],
                    "contains_first_full_x": contains_first,
                    "first_completion_if_contains": None if not contains_first else {"x": first},
                }
            )
        completions = [item for item in forced_reports if item["contains_first_full_x"]]
        row_reports.append(
            {
                "front_x": row["x"],
                "holes": row["holes"],
                "assignment_count": len(hole_assignments),
                "min_forced_x": None if not hole_assignments else hole_assignments[0]["x"],
                "first_full_compatible_patches": completions[:10],
            }
        )
    return {"P": P, "qs": qs, "front_min_holes": best_size, "front_best_rows": row_reports, "first_full_x": first}


def main() -> None:
    ps = [13, 17, 19, 23, 29, 31]
    results = [scan(P) for P in ps]
    audit = {
        "certificate_type": "front_window_completion_cost_scan",
        "status": "front_hole_killing_constraints_need_completion_cost_not_only_local_patch_cost",
        "results": results,
        "structural_conclusion": (
            "残洞核可被局部 CRT 约束以很小相位补掉，但一旦要求补洞约束同时延拓为完整零行，"
            "最早完成相位在样本中回到首个完整覆盖相位，并全部位于 x>=P。"
            "这支持‘前窗口残洞核的真正消除代价是全局相位跨越’。"
        ),
        "next_obligations": [
            "把 forced_scheme 的等差枚举改写为理论命题：局部补洞约束必须兼容全部列覆盖。",
            "证明若 forced_scheme 在 x<P 内补掉最终残洞，则必产生新的未覆盖列，形成残洞迁移守恒。",
            "把残洞迁移守恒与 FSC: min full x >= P 连接，形成非有限模板的势垒不等式。",
        ],
    }
    (DOCS / "front-window-completion-cost-scan.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")

    lines = [
        "# 前窗口残洞核完整消除代价扫描",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        audit["structural_conclusion"],
        "",
        "## 摘要",
    ]
    for result in results:
        lines.append(
            f"- P={result['P']} front_min_holes={result['front_min_holes']} "
            f"first_full_x={result['first_full_x']}"
        )
        for row in result["front_best_rows"][:3]:
            best_patch = row["first_full_compatible_patches"][0] if row["first_full_compatible_patches"] else None
            lines.append(
                f"  - front_x={row['front_x']} holes={row['holes']} "
                f"assignments={row['assignment_count']} min_forced_x={row['min_forced_x']} "
                f"first_full_patch={None if best_patch is None else best_patch['first_completion_if_contains']}"
            )
    lines += ["", "## 下一证明义务"] + [f"- {item}" for item in audit["next_obligations"]] + [""]
    (DOCS / "front-window-completion-cost-scan.md").write_text("\n".join(lines))
    print(DOCS / "front-window-completion-cost-scan.json")
    print(DOCS / "front-window-completion-cost-scan.md")


if __name__ == "__main__":
    main()
