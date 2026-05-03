#!/usr/bin/env python3
"""D4/R5 G1 low_sum>=3/5 分支严格 QP 审计。"""
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


def main():
    data = json.loads(INPUT.read_text(encoding="utf-8"))
    vectors = []
    for item in data["nearest_count_vectors"]:
        if item["worst_margin"] < 0.003 and item["counts"] not in vectors:
            vectors.append(item["counts"])
    cases = {
        "floor_3over5_ladder_l34_8over5": ({"l12": Fraction(3, 2), "l23": Fraction(3, 2), "l34": Fraction(8, 5)}),
        "floor_3over5_ladder_l23_8over5_l34_8over5": ({"l12": Fraction(3, 2), "l23": Fraction(8, 5), "l34": Fraction(8, 5)}),
        "floor_3over5_ladder_l12_8over5_l34_8over5": ({"l12": Fraction(8, 5), "l23": Fraction(3, 2), "l34": Fraction(8, 5)}),
        "floor_3over5_all_8over5": ({"l12": Fraction(8, 5), "l23": Fraction(8, 5), "l34": Fraction(8, 5)}),
    }
    rows = []
    for counts in vectors:
        row = {"counts": counts, "cases": {}}
        for name, lambdas in cases.items():
            value, meta = strict_qp.qp_min(counts, lambdas, None, Fraction(3, 5))
            row["cases"][name] = {"energy": value, "margin": None if value is None else value - TARGET, "meta": meta, "lambdas": lambdas}
        rows.append(row)
    failures = {name: [row for row in rows if row["cases"][name]["margin"] is None or row["cases"][name]["margin"] < 0] for name in cases}
    worst = {name: min(rows, key=lambda row: row["cases"][name]["margin"] if row["cases"][name]["margin"] is not None else Fraction(-999))["cases"][name] for name in cases}
    audit = {
        "certificate_type": "D4_R5_G1_low_floor_qp_audit",
        "status": "low_floor_branch_needs_more_than_l34_8over5_check_results",
        "near_vector_count": len(rows),
        "failure_counts": {name: len(items) for name, items in failures.items()},
        "worst_by_case": compact(worst),
        "rows": compact(rows),
        "structural_conclusion": "已把 low_sum>=3/5 显式加入严格 QP。结果用于判断 low 高分支需要哪段密度链增强。",
        "next_obligations": [
            "若某个增强组合失败数为 0，则转入证明该组合的 tau 几何来源。",
            "若全部失败，则继续反解所需 lambda 或增加高桶非空补偿。",
        ],
    }
    (DOCS / "d4-r5-G1-low-floor-qp-audit.json").write_text(json.dumps(compact(audit), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = ["# D4/R5 G1 low_sum>=3/5 分支严格 QP 审计", "", f"**状态：** `{audit['status']}`", "", audit["structural_conclusion"], "", "## 失败计数"]
    for name, count in audit["failure_counts"].items():
        lines.append(f"- `{name}`：`{count}`")
    lines += ["", "## 最坏案例"]
    for name, item in audit["worst_by_case"].items():
        lines.append(f"- `{name}`：margin={item['margin']}, masses={item['meta']['masses'] if item['meta'] else None}")
    lines += ["", "## 下一证明义务"]
    for item in audit["next_obligations"]:
        lines.append(f"- {item}")
    lines.append("")
    (DOCS / "d4-r5-G1-low-floor-qp-audit.md").write_text("\n".join(lines), encoding="utf-8")
    print(DOCS / "d4-r5-G1-low-floor-qp-audit.json")
    print(DOCS / "d4-r5-G1-low-floor-qp-audit.md")


if __name__ == "__main__":
    main()
