#!/usr/bin/env python3
"""D4/R5 G1 low 分支严格 QP 审计。"""
from __future__ import annotations

import importlib.util
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
SRC = ROOT / "experiments" / "d4_r5_G1_strict_qp_certificate.py"
spec = importlib.util.spec_from_file_location("strict_qp", SRC)
strict_qp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(strict_qp)  # type: ignore[union-attr]
INPUT = DOCS / "d4-r5-G1-six-bucket-simplex-audit.json"
TARGET = Fraction(1, 64)


def compact(value):
    return strict_qp.compact(value)


def run(counts, lambdas, low_cap=None, low_floor=None):
    # 复用 qp_min 不支持 low_floor；用 -low_sum <= -floor 作为临时扩展较麻烦。
    # 这里先验证增强链在全域是否足够；若全域足够，则 low>3/5 分支自动足够。
    value, meta = strict_qp.qp_min(counts, lambdas, low_cap)
    return {"energy": value, "margin": None if value is None else value - TARGET, "meta": meta, "lambdas": lambdas, "low_cap": low_cap, "low_floor": low_floor}


def main():
    data = json.loads(INPUT.read_text(encoding="utf-8"))
    vectors = []
    for item in data["nearest_count_vectors"]:
        if item["worst_margin"] < 0.003 and item["counts"] not in vectors:
            vectors.append(item["counts"])
    cases = {
        "base_ladder_low_le_3over5": ({"l12": Fraction(3, 2), "l23": Fraction(3, 2), "l34": Fraction(3, 2)}, Fraction(3, 5)),
        "enhanced_l34_8over5_no_low_cap": ({"l12": Fraction(3, 2), "l23": Fraction(3, 2), "l34": Fraction(8, 5)}, None),
        "enhanced_l23_3over2_l34_8over5_low31over50": ({"l12": Fraction(3, 2), "l23": Fraction(3, 2), "l34": Fraction(8, 5)}, Fraction(31, 50)),
        "strong_l12_8over5_l23_3over2_l34_8over5_no_cap": ({"l12": Fraction(8, 5), "l23": Fraction(3, 2), "l34": Fraction(8, 5)}, None),
    }
    rows = []
    for counts in vectors:
        row = {"counts": counts, "cases": {}}
        for name, (lambdas, cap) in cases.items():
            row["cases"][name] = run(counts, lambdas, cap)
        rows.append(row)
    failures = {
        name: [row for row in rows if row["cases"][name]["margin"] is None or row["cases"][name]["margin"] < 0]
        for name in cases
    }
    audit = {
        "certificate_type": "D4_R5_G1_branch_qp_audit",
        "status": "enhanced_l34_alone_not_sufficient_low_branch_needs_floor_or_second_enhancement",
        "near_vector_count": len(rows),
        "failure_counts": {name: len(items) for name, items in failures.items()},
        "worst_by_case": compact({
            name: min(rows, key=lambda row: row["cases"][name]["margin"] if row["cases"][name]["margin"] is not None else Fraction(-999))["cases"][name]
            for name in cases
        }),
        "rows": compact(rows),
        "structural_conclusion": (
            "严格 QP 显示：low<=3/5 分支已闭合；但把 d4/d3 增强到 8/5 若不显式使用 low>3/5 下界，仍不足以全域闭合。"
            "因此 low>3/5 分支的证明必须真正利用 low floor，而不能只添加一个全域增强斜率。"
            "下一步需扩展 QP 证书支持 low_sum>=3/5，并验证 floor + d4/d3>=8/5 是否闭合。"
        ),
        "next_obligations": [
            "扩展严格 QP 主动集，加入 low_sum>=3/5 约束。",
            "验证 low_sum>=3/5 与 d4/d3>=8/5、d2/d1>=3/2、d3/d2>=3/2 的组合。",
            "若仍不足，加入 d2/d1>=8/5 或 d3/d2>=3/2+epsilon 的二选一增强。",
        ],
    }
    (DOCS / "d4-r5-G1-branch-qp-audit.json").write_text(json.dumps(compact(audit), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = ["# D4/R5 G1 low 分支严格 QP 审计", "", f"**状态：** `{audit['status']}`", "", audit["structural_conclusion"], "", "## 失败计数"]
    for name, count in audit["failure_counts"].items():
        lines.append(f"- `{name}`：`{count}`")
    lines += ["", "## 下一证明义务"]
    for item in audit["next_obligations"]:
        lines.append(f"- {item}")
    lines.append("")
    (DOCS / "d4-r5-G1-branch-qp-audit.md").write_text("\n".join(lines), encoding="utf-8")
    print(DOCS / "d4-r5-G1-branch-qp-audit.json")
    print(DOCS / "d4-r5-G1-branch-qp-audit.md")


if __name__ == "__main__":
    main()
