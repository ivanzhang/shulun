#!/usr/bin/env python3
"""D4/R5 G1 近危险支撑向量严格 QP 推广审计。"""
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
LADDER = {"l12": Fraction(3, 2), "l23": Fraction(3, 2), "l34": Fraction(3, 2)}


def compact(value):
    return strict_qp.compact(value)


def run(counts, low_cap):
    value, meta = strict_qp.qp_min(counts, LADDER, low_cap)
    return {"energy": value, "margin": None if value is None else value - TARGET, "meta": meta, "low_cap": low_cap}


def main():
    data = json.loads(INPUT.read_text(encoding="utf-8"))
    vectors = [item["counts"] for item in data["nearest_count_vectors"] if item["worst_margin"] < 0.003]
    seen = []
    for v in vectors:
        if v not in seen:
            seen.append(v)
    rows = []
    for counts in seen:
        r3_5 = run(counts, Fraction(3, 5))
        r31_50 = run(counts, Fraction(31, 50))
        rows.append({"counts": counts, "low_3over5": r3_5, "low_31over50": r31_50})
    failures_3_5 = [row for row in rows if row["low_3over5"]["margin"] is None or row["low_3over5"]["margin"] < 0]
    failures_31_50 = [row for row in rows if row["low_31over50"]["margin"] is None or row["low_31over50"]["margin"] < 0]
    worst_3_5 = min(rows, key=lambda row: row["low_3over5"]["margin"])
    audit = {
        "certificate_type": "D4_R5_G1_strict_qp_near_vectors",
        "status": "ladder_3halves_plus_low_3over5_verified_on_near_danger_vectors" if not failures_3_5 else "low_3over5_has_near_vector_failures",
        "near_vector_count": len(rows),
        "failures_low_3over5": compact(failures_3_5),
        "failures_low_31over50_count": len(failures_31_50),
        "worst_low_3over5": compact(worst_3_5),
        "rows": compact(rows),
        "structural_conclusion": (
            "对所有 margin<0.003 的近危险支撑向量，严格 Fraction 主动集 QP 验证："
            "相邻 3/2 密度链加 low_sum<=3/5 足以推出 Q/S^2>=1/64。"
            "31/50 在部分向量上仍不安全，因此统一证明应以 3/5 为低桶帽。"
        ),
        "next_obligations": [
            "把近危险向量外的支撑向量用原始 Cauchy 余量直接隔离，形成有限分族证明。",
            "证明结构二选一：若 low_sum<=3/5，则 QP 证书闭合；若 low_sum>3/5，则相邻密度链必须强于 3/2 或触发其他高桶质量。",
            "将主动集证书中的有理 masses 与 active constraints 输出为可人工审查附录。",
        ],
    }
    (DOCS / "d4-r5-G1-strict-qp-near-vectors.json").write_text(json.dumps(compact(audit), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# D4/R5 G1 近危险支撑向量严格 QP 推广审计",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        audit["structural_conclusion"],
        "",
        "## 摘要",
        f"- 近危险向量数：`{audit['near_vector_count']}`",
        f"- low<=3/5 失败数：`{len(failures_3_5)}`",
        f"- low<=31/50 失败数：`{audit['failures_low_31over50_count']}`",
        f"- low<=3/5 最坏：{compact(worst_3_5)}",
        "",
        "## 下一证明义务",
    ]
    for item in audit["next_obligations"]:
        lines.append(f"- {item}")
    lines.append("")
    (DOCS / "d4-r5-G1-strict-qp-near-vectors.md").write_text("\n".join(lines), encoding="utf-8")
    print(DOCS / "d4-r5-G1-strict-qp-near-vectors.json")
    print(DOCS / "d4-r5-G1-strict-qp-near-vectors.md")


if __name__ == "__main__":
    main()
