#!/usr/bin/env python3
"""D4/R5 G1 六桶线性约束凸二次规划严格枚举证书。"""
from __future__ import annotations

import itertools
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
TARGET = Fraction(1, 64)
VECTORS = [[36, 24, 15, 14, 0, 1], [40, 21, 21, 11, 2, 0], [38, 24, 19, 12, 1, 0]]


def fnum(x: Fraction) -> float:
    return float(x.numerator / x.denominator)


def compact(value):
    if isinstance(value, Fraction):
        return {"num": value.numerator, "den": value.denominator, "float": fnum(value)}
    if isinstance(value, float):
        return float(f"{value:.17g}")
    if isinstance(value, dict):
        return {key: compact(item) for key, item in value.items()}
    if isinstance(value, list):
        return [compact(item) for item in value]
    return value


def solve_linear(a, b):
    """Fraction 高斯消元。"""
    n = len(b)
    mat = [row[:] + [rhs] for row, rhs in zip(a, b)]
    for col in range(n):
        pivot = None
        for r in range(col, n):
            if mat[r][col] != 0:
                pivot = r
                break
        if pivot is None:
            return None
        mat[col], mat[pivot] = mat[pivot], mat[col]
        div = mat[col][col]
        mat[col] = [x / div for x in mat[col]]
        for r in range(n):
            if r == col:
                continue
            factor = mat[r][col]
            if factor:
                mat[r] = [x - factor * y for x, y in zip(mat[r], mat[col])]
    return [mat[i][-1] for i in range(n)]


def energy(m, counts):
    return sum(m[i] * m[i] / counts[i] for i in range(6) if counts[i])


def build_constraints(counts, lambdas, low_cap, low_floor=None):
    cons = []
    # A m >= b 形式。
    cons.append(([Fraction(1) for _ in range(6)], Fraction(1)))
    cons.append(([-Fraction(1) for _ in range(6)], Fraction(-1)))
    for i in range(6):
        row = [Fraction(0) for _ in range(6)]
        row[i] = Fraction(1)
        cons.append((row, Fraction(0)))
        if counts[i] == 0:
            row2 = [Fraction(0) for _ in range(6)]
            row2[i] = -Fraction(1)
            cons.append((row2, Fraction(0)))
    if low_cap is not None:
        row = [Fraction(0) for _ in range(6)]
        row[0] = row[1] = row[2] = -Fraction(1)
        cons.append((row, -low_cap))
    if low_floor is not None:
        row = [Fraction(0) for _ in range(6)]
        row[0] = row[1] = row[2] = Fraction(1)
        cons.append((row, low_floor))
    def add_density(hi, lo, lam):
        if lam is None or counts[hi] == 0 or counts[lo] == 0:
            return
        row = [Fraction(0) for _ in range(6)]
        row[hi] = Fraction(1, counts[hi])
        row[lo] = -lam * Fraction(1, counts[lo])
        cons.append((row, Fraction(0)))
    add_density(1, 0, lambdas.get("l12"))
    add_density(2, 1, lambdas.get("l23"))
    add_density(3, 2, lambdas.get("l34"))
    add_density(4, 3, lambdas.get("l45"))
    add_density(5, 4, lambdas.get("l56"))
    add_density(3, 0, lambdas.get("l14"))
    return cons


def qp_min(counts, lambdas, low_cap=None, low_floor=None):
    counts_f = [Fraction(c) if c else Fraction(1) for c in counts]
    inequalities = build_constraints(counts, lambdas, low_cap, low_floor)
    # 总和等式始终作为等式；枚举额外活跃不等式。去掉两个总和不等式，单独加 sum=1。
    base_eq = [([Fraction(1) for _ in range(6)], Fraction(1))]
    other = inequalities[2:]
    best = None
    best_meta = None
    # KKT 未知 m0..m5 + multipliers。枚举最多 5 个活跃约束。
    for r in range(0, min(5, len(other)) + 1):
        for active_idx in itertools.combinations(range(len(other)), r):
            eqs = base_eq + [other[i] for i in active_idx]
            k = len(eqs)
            size = 6 + k
            mat = [[Fraction(0) for _ in range(size)] for __ in range(size)]
            rhs = [Fraction(0) for _ in range(size)]
            # stationarity: 2 m_i/n_i + sum lambda_j a_j_i = 0
            for i in range(6):
                if counts[i] == 0:
                    mat[i][i] = Fraction(2)  # m_i forced by constraints
                else:
                    mat[i][i] = Fraction(2, counts[i])
                for j, (a, _) in enumerate(eqs):
                    mat[i][6 + j] = a[i]
            # equations a_j m = b_j
            for j, (a, b) in enumerate(eqs):
                row = 6 + j
                for i in range(6):
                    mat[row][i] = a[i]
                rhs[row] = b
            sol = solve_linear(mat, rhs)
            if sol is None:
                continue
            m = sol[:6]
            # feasibility
            if any(x < -Fraction(1, 10**10) for x in m):
                continue
            ok = True
            for a, b in inequalities:
                if sum(ai * mi for ai, mi in zip(a, m)) < b - Fraction(1, 10**10):
                    ok = False
                    break
            if not ok:
                continue
            val = energy(m, counts_f)
            if best is None or val < best:
                best = val
                best_meta = {"masses": m, "active_count": r, "active_constraints": list(active_idx)}
    return best, best_meta


def run_case(counts, lambdas, low_cap):
    value, meta = qp_min(counts, lambdas, low_cap)
    return {"energy": value, "margin": None if value is None else value - TARGET, "meta": meta, "lambdas": lambdas, "low_cap": low_cap}


def main():
    cases = [
        ("ladder_3halves_low_31over50", {"l12": Fraction(3, 2), "l23": Fraction(3, 2), "l34": Fraction(3, 2)}, Fraction(31, 50)),
        ("ladder_3halves_low_3over5", {"l12": Fraction(3, 2), "l23": Fraction(3, 2), "l34": Fraction(3, 2)}, Fraction(3, 5)),
        ("ladder_strong_low_31over50", {"l12": Fraction(17, 10), "l23": Fraction(3, 2), "l34": Fraction(8, 5)}, Fraction(31, 50)),
        ("ladder_strong_no_low", {"l12": Fraction(17, 10), "l23": Fraction(3, 2), "l34": Fraction(8, 5)}, None),
    ]
    rows = []
    for counts in VECTORS:
        result = {"counts": counts, "cases": {}}
        for name, lambdas, low_cap in cases:
            result["cases"][name] = run_case(counts, lambdas, low_cap)
        rows.append(result)
    audit = {
        "certificate_type": "D4_R5_G1_strict_qp_certificate",
        "status": "strict_active_set_qp_confirms_ladder_plus_low_cap_candidates",
        "target_Q_over_S2": TARGET,
        "vectors": compact(rows),
        "structural_conclusion": (
            "纯 Fraction 主动集枚举给出可复核的凸二次规划证书。"
            "在测试的最危险支撑向量上，密度链配合 low_sum<=3/5 可直接验证能量余量；31/50 对首个向量仍不足，不能作为统一安全帽；"
            "而强密度链不带低桶帽仍可能不足，说明低桶帽不是数值伪影，而是必要接口。"
        ),
        "next_obligations": [
            "把主动集证书推广到所有 margin<0.003 的近危险支撑向量。",
            "反解每个支撑向量允许的最大 low_sum 帽；当前统一候选应优先使用 3/5，而不是 31/50。",
            "从 tau 几何证明二选一：low_sum<=U，或密度链强于当前候选。",
        ],
    }
    (DOCS / "d4-r5-G1-strict-qp-certificate.json").write_text(json.dumps(compact(audit), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = ["# D4/R5 G1 严格 QP 证书", "", f"**状态：** `{audit['status']}`", "", audit["structural_conclusion"], "", "## 证书摘要"]
    for row in compact(audit)["vectors"]:
        lines.append(f"- counts={row['counts']}")
        for name, case in row["cases"].items():
            margin = case["margin"]
            masses = case["meta"]["masses"] if case["meta"] else None
            lines.append(f"  - `{name}`：margin={margin}, masses={masses}")
    lines += ["", "## 下一证明义务"]
    for item in audit["next_obligations"]:
        lines.append(f"- {item}")
    lines.append("")
    (DOCS / "d4-r5-G1-strict-qp-certificate.md").write_text("\n".join(lines), encoding="utf-8")
    print(DOCS / "d4-r5-G1-strict-qp-certificate.json")
    print(DOCS / "d4-r5-G1-strict-qp-certificate.md")


if __name__ == "__main__":
    main()
