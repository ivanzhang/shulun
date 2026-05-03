#!/usr/bin/env python3
"""D4/R5 G1 最坏支撑向量约束二次规划快速审计。"""
from __future__ import annotations

import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
TARGET = 1 / 64
VECTORS = [[36, 24, 15, 14, 0, 1], [40, 21, 21, 11, 2, 0], [38, 24, 19, 12, 1, 0]]


def compact(value):
    if isinstance(value, float):
        return float(f"{value:.17g}")
    if isinstance(value, dict):
        return {key: compact(item) for key, item in value.items()}
    if isinstance(value, list):
        return [compact(item) for item in value]
    return value


def energy(m, n):
    return sum(m[i] * m[i] / n[i] for i in range(6) if n[i])


def feasible(m, n, lambdas):
    d = [m[i] / n[i] if n[i] else 0.0 for i in range(6)]
    if lambdas.get("l12", 0) and d[1] + 1e-12 < lambdas["l12"] * d[0]:
        return False
    if lambdas.get("l23", 0) and d[2] + 1e-12 < lambdas["l23"] * d[1]:
        return False
    if lambdas.get("l34", 0) and d[3] + 1e-12 < lambdas["l34"] * d[2]:
        return False
    if lambdas.get("l14", 0) and d[3] + 1e-12 < lambdas["l14"] * d[0]:
        return False
    if lambdas.get("low_sum_upper") is not None and sum(m[:3]) > lambdas["low_sum_upper"] + 1e-12:
        return False
    return True


def random_min(n, lambdas, trials=70000, seed=17):
    rng = random.Random(seed + sum(n) * 1009 + int(1000 * sum(lambdas.values())))
    active = [i for i, x in enumerate(n) if x]
    best = (9.0, None)
    total_n = sum(n)
    candidates = [[x / total_n for x in n]]
    for _ in range(trials):
        raw = [0.0] * 6
        vals = [rng.expovariate(1.0) * n[i] for i in active]
        total = sum(vals)
        for idx, val in zip(active, vals):
            raw[idx] = val / total
        candidates.append(raw)
    for m in candidates:
        if feasible(m, n, lambdas):
            val = energy(m, n)
            if val < best[0]:
                best = (val, m)
    return best


def main():
    tests = {
        "remote_l34_1p5_l14_4": {"l34": 1.5, "l14": 4.0},
        "remote_l34_1p6_l14_5": {"l34": 1.6, "l14": 5.0},
        "full_ladder_1p5_1p5_1p5": {"l12": 1.5, "l23": 1.5, "l34": 1.5},
        "full_ladder_1p7_1p5_1p6": {"l12": 1.7, "l23": 1.5, "l34": 1.6},
        "full_ladder_plus_low062": {"l12": 1.5, "l23": 1.5, "l34": 1.5, "low_sum_upper": 0.62},
        "full_ladder_plus_low060": {"l12": 1.5, "l23": 1.5, "l34": 1.5, "low_sum_upper": 0.60},
    }
    rows = []
    for n in VECTORS:
        row = {"counts": n, "tests": {}}
        for name, lambdas in tests.items():
            val, m = random_min(n, lambdas)
            row["tests"][name] = {"energy_upper_for_min": val, "margin": val - TARGET, "witness_masses": m, "constraints": lambdas}
        rows.append(row)
    audit = {
        "certificate_type": "D4_R5_G1_worst_vector_qp_audit",
        "status": "full_density_ladder_with_low_mass_cap_is_the_next_promising_interface",
        "target_Q_over_S2": TARGET,
        "vectors": compact(rows),
        "structural_conclusion": (
            "快速随机二次规划显示，远程约束 d4>=lambda*d1 与 d4>=lambda*d3 单独不足；"
            "完整相邻密度链 d2>=lambda12*d1、d3>=lambda23*d2、d4>=lambda34*d3 更接近真实结构，"
            "但通常仍需配合低三桶总质量上界。下一步应证明“密度阶梯 + 低桶质量帽”的联合引理。"
        ),
        "next_obligations": [
            "对最危险向量做严格凸二次规划证书，替换当前随机上界式探索。",
            "从数据反解低三桶质量帽 U，当前最危险 top20 中 low_mass 最大约 0.62247。",
            "尝试证明若低三桶质量超过 U，则相邻密度阶梯必进一步增强，从而二选一闭合。",
        ],
    }
    (DOCS / "d4-r5-G1-worst-vector-qp-audit.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = ["# D4/R5 G1 最坏支撑向量约束二次规划审计", "", f"**状态：** `{audit['status']}`", "", audit["structural_conclusion"], "", "## 测试摘要"]
    for row in audit["vectors"]:
        lines.append(f"- counts={row['counts']}")
        for name, result in row["tests"].items():
            lines.append(f"  - `{name}`：margin={result['margin']}, witness={result['witness_masses']}")
    lines += ["", "## 下一证明义务"]
    for item in audit["next_obligations"]:
        lines.append(f"- {item}")
    lines.append("")
    (DOCS / "d4-r5-G1-worst-vector-qp-audit.md").write_text("\n".join(lines), encoding="utf-8")
    print(DOCS / "d4-r5-G1-worst-vector-qp-audit.json")
    print(DOCS / "d4-r5-G1-worst-vector-qp-audit.md")


if __name__ == "__main__":
    main()
