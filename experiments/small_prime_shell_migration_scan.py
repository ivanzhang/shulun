#!/usr/bin/env python3
"""小素数多同余壳迁移扫描。

奇偶壳只是 B={2} 的特例。这里扩展到 B={2,3,5,7} 的小素数壳：
每个相位 x 在每个 p in B 上禁止一个列余类 c≡-xP mod p。
残洞必须落在所有小素数的非覆盖壳交集中。相位变化会重排这些壳，
补掉旧洞的同时释放新的小壳残洞。
"""
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


def covered_by(P: int, qs: list[int], x: int, c: int) -> list[int]:
    return [q for q in qs if (x * P + c) % q == 0]


def holes(P: int, qs: list[int], x: int) -> list[int]:
    return [c for c in range(1, P) if not covered_by(P, qs, x, c)]


def shell_residue(P: int, x: int, p: int) -> int:
    return (-x * P) % p


def small_shell(P: int, x: int, B: list[int]) -> list[int]:
    # 未被小素数 B 覆盖的列集合。
    return [c for c in range(1, P) if all(c % p != shell_residue(P, x, p) for p in B)]


def signature(P: int, x: int, B: list[int]) -> dict[int, int]:
    return {p: shell_residue(P, x, p) for p in B}


def front_min_rows(P: int, qs: list[int]) -> list[dict]:
    rows = [{"x": x, "holes": holes(P, qs, x)} for x in range(1, P)]
    min_size = min(len(row["holes"]) for row in rows)
    return [row for row in rows if len(row["holes"]) == min_size]


def scan(P: int, B: list[int]) -> dict:
    qs = primes_upto(P - 1)
    rows = []
    for x in range(1, P):
        H = holes(P, qs, x)
        SB = small_shell(P, x, B)
        rows.append(
            {
                "x": x,
                "H": H,
                "H_size": len(H),
                "B_shell_size": len(SB),
                "B_signature": signature(P, x, B),
                "H_in_B_shell": all(c in set(SB) for c in H),
            }
        )
    min_rows = front_min_rows(P, qs)
    migrations = []
    for src in min_rows[:4]:
        K = set(src["holes"])
        source_shell = set(small_shell(P, src["x"], B))
        candidates = []
        for dst in rows:
            y = dst["x"]
            if y == src["x"]:
                continue
            Hy = set(dst["H"])
            killed = sorted(K - Hy)
            born = sorted(Hy - K)
            sig_changed = {p: (signature(P, src["x"], B)[p], dst["B_signature"][p]) for p in B if signature(P, src["x"], B)[p] != dst["B_signature"][p]}
            if killed:
                candidates.append(
                    {
                        "y": y,
                        "H_y": dst["H"],
                        "killed_K": killed,
                        "born_new": born,
                        "release_count": len(born),
                        "changed_small_residues": sig_changed,
                        "B_shell_size_y": dst["B_shell_size"],
                        "new_B_shell_minus_old": len(set(small_shell(P, y, B)) - source_shell),
                    }
                )
        candidates.sort(key=lambda item: (len(item["H_y"]), item["release_count"], len(item["changed_small_residues"]), item["y"]))
        migrations.append(
            {
                "x": src["x"],
                "K": src["holes"],
                "B_signature": signature(P, src["x"], B),
                "B_shell_size": len(source_shell),
                "best_migrations": candidates[:12],
            }
        )
    shell_sizes = [row["B_shell_size"] for row in rows]
    return {
        "P": P,
        "B": B,
        "B_modulus": prod(B),
        "shell_size_min": min(shell_sizes),
        "shell_size_max": max(shell_sizes),
        "shell_size_avg": sum(shell_sizes) / len(shell_sizes),
        "all_H_inside_B_shell": all(row["H_in_B_shell"] for row in rows),
        "front_min_migrations": migrations,
    }


def prod(values: list[int]) -> int:
    out = 1
    for value in values:
        out *= value
    return out


def main() -> None:
    ps = [23, 29, 31, 37, 41, 47, 53, 59, 67, 71, 83, 97]
    bases = [[2], [2, 3], [2, 3, 5], [2, 3, 5, 7]]
    results = [{"B": B, "scans": [scan(P, B) for P in ps if all(p < P for p in B)]} for B in bases]
    audit = {
        "certificate_type": "small_prime_shell_migration_scan",
        "status": "parity_shell_generalizes_to_small_prime_residue_shells",
        "results": results,
        "structural_conclusion": (
            "q=2 的奇偶翻转只是小素数同余壳迁移的第一层。"
            "对 B={2,3,5,7}，残洞始终位于小素数非覆盖壳交集中；"
            "相位改变会同时移动多个小素数禁余类，补掉旧核时通常释放新的 B-壳候选区。"
        ),
        "next_obligations": [
            "把 B-壳定义为 CRT 小模数单元，并证明残洞必在 B-壳内。",
            "建立 B-壳迁移方程：x->y 时每个小素数禁余类平移 -(y-x)P。",
            "证明有限小素数 B 只能压缩候选壳，不能完全覆盖；剩余壳必须由中大素数处理并产生重叠能量。",
        ],
    }
    (DOCS / "small-prime-shell-migration-scan.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")
    lines = [
        "# 小素数多同余壳迁移扫描",
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
            lines.append(
                f"- P={item['P']} M_B={item['B_modulus']} shell_avg={item['shell_size_avg']:.2f} "
                f"shell_range=({item['shell_size_min']},{item['shell_size_max']}) H_inside={item['all_H_inside_B_shell']}"
            )
            for mig in item["front_min_migrations"][:2]:
                lines.append(
                    f"  - x={mig['x']} K={mig['K']} sig={mig['B_signature']} "
                    f"best={mig['best_migrations'][:3]}"
                )
    lines += ["", "## 下一证明义务"] + [f"- {ob}" for ob in audit["next_obligations"]] + [""]
    (DOCS / "small-prime-shell-migration-scan.md").write_text("\n".join(lines))
    print(DOCS / "small-prime-shell-migration-scan.json")
    print(DOCS / "small-prime-shell-migration-scan.md")


if __name__ == "__main__":
    main()
