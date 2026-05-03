#!/usr/bin/env python3
"""D4/R5 G1 条件化高桶补偿 QP 分族审计。"""
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


def family(counts: list[int]) -> str:
    if counts[4] == 0 and counts[5] == 0:
        return "A_no_high"
    if counts[4] > 0 and counts[5] == 0:
        return "B_tau_33_59"
    if counts[5] > 0:
        return "C_heavy_short"
    return "other"


def lambdas_for(counts: list[int], variant: str) -> dict[str, Fraction]:
    base = {"l12": Fraction(3, 2), "l23": Fraction(3, 2), "l34": Fraction(3, 2)}
    fam = family(counts)
    if variant == "base":
        return base
    if variant == "conditioned_weak":
        if fam == "A_no_high":
            base["l34"] = Fraction(8, 5)
        elif fam == "B_tau_33_59":
            base["l45"] = Fraction(1, 1)
        elif fam == "C_heavy_short":
            base["l56"] = Fraction(1, 1)
        return base
    if variant == "conditioned_mid":
        if fam == "A_no_high":
            base["l34"] = Fraction(5, 3)
        elif fam == "B_tau_33_59":
            base["l45"] = Fraction(1, 1)
            base["l34"] = Fraction(8, 5)
        elif fam == "C_heavy_short":
            base["l56"] = Fraction(1, 1)
            base["l34"] = Fraction(8, 5)
        return base
    if variant == "conditioned_strong":
        if fam == "A_no_high":
            base["l34"] = Fraction(17, 10)
        elif fam == "B_tau_33_59":
            base["l45"] = Fraction(3, 2)
            base["l34"] = Fraction(8, 5)
        elif fam == "C_heavy_short":
            base["l56"] = Fraction(1, 1)
            base["l45"] = Fraction(1, 1)
            base["l34"] = Fraction(8, 5)
        return base
    raise ValueError(variant)


def main() -> None:
    data = json.loads(INPUT.read_text(encoding="utf-8"))
    vectors = []
    for item in data["nearest_count_vectors"]:
        if item["worst_margin"] < 0.003 and item["counts"] not in vectors:
            vectors.append(item["counts"])
    variants = ["conditioned_strong"]
    rows = []
    for counts in vectors:
        row = {"counts": counts, "family": family(counts), "cases": {}}
        for variant in variants:
            lambdas = lambdas_for(counts, variant)
            value, meta = strict_qp.qp_min(counts, lambdas, None, Fraction(3, 5))
            row["cases"][variant] = {
                "energy": value,
                "margin": None if value is None else value - TARGET,
                "meta": meta,
                "lambdas": lambdas,
            }
        rows.append(row)
    failures = {
        variant: [row for row in rows if row["cases"][variant]["margin"] is None or row["cases"][variant]["margin"] < 0]
        for variant in variants
    }
    by_family = {}
    for fam in sorted(set(row["family"] for row in rows)):
        fam_rows = [row for row in rows if row["family"] == fam]
        by_family[fam] = {
            "count": len(fam_rows),
            "failure_counts": {
                variant: sum(1 for row in fam_rows if row["cases"][variant]["margin"] is None or row["cases"][variant]["margin"] < 0)
                for variant in variants
            },
        }
    worst = {
        variant: min(rows, key=lambda row: row["cases"][variant]["margin"] if row["cases"][variant]["margin"] is not None else Fraction(-999))
        for variant in variants
    }
    audit = {
        "certificate_type": "D4_R5_G1_conditioned_high_bucket_qp",
        "status": "conditioned_high_bucket_compensation_tested_remaining_failures_identified",
        "near_vector_count": len(rows),
        "failure_counts": {variant: len(items) for variant, items in failures.items()},
        "by_family": compact(by_family),
        "worst_by_variant": compact(worst),
        "rows": compact(rows),
        "structural_conclusion": (
            "按高桶是否非空进行 A/B/C 条件化 QP 后，可以精确看到哪些分族仍未闭合。"
            "若条件化高桶补偿仍失败，则下一步不应继续盲目加全局斜率，而应对失败分族反解最小补偿常数。"
        ),
        "next_obligations": [
            "查看 conditioned_strong 的失败分族，并只对失败分族反解 lambda。",
            "对 A_no_high 反解所需 d4/d3；对 B 反解所需 d5/d4；对 C 反解所需 d6/d5 或 d6/d4。",
            "把反解常数与实际数据下界比较，选择可证明且不过强的有理常数。",
        ],
    }
    (DOCS / "d4-r5-G1-conditioned-high-bucket-qp.json").write_text(json.dumps(compact(audit), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# D4/R5 G1 条件化高桶补偿 QP 分族审计",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        audit["structural_conclusion"],
        "",
        "## 全体失败计数",
    ]
    for variant, count in audit["failure_counts"].items():
        lines.append(f"- `{variant}`：`{count}`")
    lines += ["", "## 分族失败计数"]
    for fam, summary in audit["by_family"].items():
        lines.append(f"- `{fam}`：{summary}")
    lines += ["", "## 下一证明义务"]
    for item in audit["next_obligations"]:
        lines.append(f"- {item}")
    lines.append("")
    (DOCS / "d4-r5-G1-conditioned-high-bucket-qp.md").write_text("\n".join(lines), encoding="utf-8")
    print(DOCS / "d4-r5-G1-conditioned-high-bucket-qp.json")
    print(DOCS / "d4-r5-G1-conditioned-high-bucket-qp.md")


if __name__ == "__main__":
    main()
