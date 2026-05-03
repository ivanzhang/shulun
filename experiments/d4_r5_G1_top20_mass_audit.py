#!/usr/bin/env python3
"""D4/R5 G1 top20 稳健质量证书审计。"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
INPUT = DOCS / "d4-r5-O2-alloffsets-1e6-1p1e6-step100-T60.json"


def compact(record: dict) -> dict:
    return {key: float(f"{value:.17g}") if isinstance(value, float) else value for key, value in record.items()}


def main() -> None:
    rows = json.loads(INPUT.read_text(encoding="utf-8"))["rows"]
    records = []
    for row in rows:
        weights = sorted(
            [
                float(item["positive_contract_sum"])
                for item in row["all_offsets"]
                if item["positive_contract_sum"] > 0
                and (item["tau_sum"] < 60 or (item["tau_sum"] >= 60 and item["count"] <= 25))
            ],
            reverse=True,
        )
        total = sum(weights)
        square = sum(w * w for w in weights)
        if square <= 0:
            continue
        for r in [16, 18, 20, 24, 32]:
            top_sum = sum(weights[:r])
            records.append(
                {
                    "x": row["x"],
                    "r": r,
                    "count": len(weights),
                    "sum": total,
                    "neff": total * total / square,
                    "top_sum_share": top_sum / total,
                    "cauchy_bound_from_top_r": r / ((top_sum / total) ** 2),
                }
            )
    worst_by_r = {}
    for r in [16, 18, 20, 24, 32]:
        subset = [item for item in records if item["r"] == r]
        worst_by_r[str(r)] = compact(max(subset, key=lambda item: item["cauchy_bound_from_top_r"]))

    audit = {
        "certificate_type": "D4_R5_G1_top20_mass_audit",
        "status": "top20_route_preferred_over_top16_for_margin",
        "rows_seen": len({item["x"] for item in records}),
        "lemma_template": "If the largest 20 nonordinary weights carry at least 0.56 of S, then S^2/Q <= 20/0.56^2 = 63.776 < 64.",
        "worst_by_r": worst_by_r,
        "structural_conclusion": "top16 半质量路线虽可行但最坏余量极窄。top20 路线只需前 20 个权重承担 56% 总质量；扫描最坏 share≈0.57845，对应 Cauchy 常数≈59.77，余量明显更适合定理化。",
        "recommended_next_lemma": "top20_56_mass: sum_{i<=20} w_i >= 0.56 * sum_i w_i for nonordinary offset weights.",
        "proof_advantage": [
            "0.56 比 top16 的 0.5 有更大扫描余量",
            "top20 仍是固定有限头部，适合转写成排序权重尾界",
            "tail44 审计给出等价目标 tail_after20/head20 <= 11/14，扫描最坏约 0.72877",
            "若证明 0.56 困难，可用 0.57 或自适应 top24；top24 最坏 Cauchy 常数约 58.54",
        ],
    }
    (DOCS / "d4-r5-G1-top20-mass-audit.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# D4/R5 G1 top20 稳健质量证书审计",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        audit["structural_conclusion"],
        "",
        "## 推荐引理",
        f"- `{audit['recommended_next_lemma']}`",
        f"- 模板：{audit['lemma_template']}",
        "",
        "## r 对比",
    ]
    for r, item in worst_by_r.items():
        lines.append(f"- `top{r}`：{item}")
    lines += ["", "## 优势"]
    for item in audit["proof_advantage"]:
        lines.append(f"- {item}")
    lines.append("")
    (DOCS / "d4-r5-G1-top20-mass-audit.md").write_text("\n".join(lines), encoding="utf-8")
    print(DOCS / "d4-r5-G1-top20-mass-audit.json")
    print(DOCS / "d4-r5-G1-top20-mass-audit.md")


if __name__ == "__main__":
    main()
