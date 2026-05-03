#!/usr/bin/env python3
"""D4/R5 G1 桶密度阶梯审计。"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
INPUT = DOCS / "d4-r5-G1-six-bucket-simplex-audit.json"


def compact(value):
    if isinstance(value, float):
        return float(f"{value:.17g}")
    if isinstance(value, dict):
        return {key: compact(item) for key, item in value.items()}
    if isinstance(value, list):
        return [compact(item) for item in value]
    return value


def main() -> None:
    data = json.loads(INPUT.read_text(encoding="utf-8"))
    rows = data["worst_records"][:50]
    ratios = []
    for item in rows:
        avg = item["bucket_avg_mass_per_cell"]
        ratio_17_32_to_le4 = avg[3] / avg[0] if avg[0] else None
        ratio_17_32_to_9_16 = avg[3] / avg[2] if avg[2] else None
        ratio_33_59_to_17_32 = avg[4] / avg[3] if avg[3] and avg[4] else None
        heavy_to_17_32 = avg[5] / avg[3] if avg[3] and avg[5] else None
        ratios.append(
            {
                "x": item["x"],
                "counts": item["counts"],
                "margin": item["margin"],
                "avg": avg,
                "ratio_17_32_to_le4": ratio_17_32_to_le4,
                "ratio_17_32_to_9_16": ratio_17_32_to_9_16,
                "ratio_33_59_to_17_32": ratio_33_59_to_17_32,
                "heavy_to_17_32": heavy_to_17_32,
            }
        )
    def min_present(key: str):
        vals = [item[key] for item in ratios if item[key] is not None]
        return min(vals) if vals else None
    summary = {
        "top50_min_ratio_17_32_to_le4": min_present("ratio_17_32_to_le4"),
        "top50_min_ratio_17_32_to_9_16": min_present("ratio_17_32_to_9_16"),
        "top50_min_ratio_33_59_to_17_32": min_present("ratio_33_59_to_17_32"),
        "top50_min_heavy_to_17_32": min_present("heavy_to_17_32"),
        "top50_min_avg_17_32": min(item["avg"][3] for item in ratios if item["avg"][3]),
        "top50_max_avg_le4": max(item["avg"][0] for item in ratios if item["avg"][0]),
    }
    audit = {
        "certificate_type": "D4_R5_G1_bucket_density_ladder_audit",
        "status": "density_ladder_candidate_for_structural_mass_constraints",
        "summary": compact(summary),
        "top50_ratio_rows": compact(ratios),
        "structural_conclusion": (
            "近危险行不是质量任意分配，而是呈现稳定桶密度阶梯："
            "tau_17_32 每个支撑点的平均质量至少约为 tau<=4 的 4.37 倍、"
            "至少约为 tau_9_16 的 1.60 倍。"
            "这给出比单纯总质量下界更可证的方向：由 tau 层定义和核单调性证明相邻桶平均质量递增。"
        ),
        "candidate_lemmas": [
            "密度阶梯引理：在近危险支撑型中，m_4/n_4 >= lambda_34 * m_3/n_3，lambda_34 可先取 3/2。",
            "低高密度引理：m_4/n_4 >= lambda_14 * m_1/n_1，lambda_14 可先取 4。",
            "高层补强引理：若 tau_33_59 或 heavy_short 非空，则其平均质量不低于 tau_17_32 平均质量。",
        ],
        "proof_obligations": [
            "把候选密度阶梯代入固定 n 的二次规划，验证是否足以推出 sum m_i^2/n_i >= 1/64。",
            "若 lambda=3/2 或 4 不足，则反解每个危险 n 向量所需的最小 lambda。",
            "随后从 kernel_weighted_sum 的 tau 层单调性寻找无条件证明。",
        ],
    }
    (DOCS / "d4-r5-G1-bucket-density-ladder-audit.json").write_text(
        json.dumps(audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    lines = [
        "# D4/R5 G1 桶密度阶梯审计",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        audit["structural_conclusion"],
        "",
        "## 摘要",
    ]
    for key, value in audit["summary"].items():
        lines.append(f"- `{key}`：`{value}`")
    lines += ["", "## 候选引理"]
    for item in audit["candidate_lemmas"]:
        lines.append(f"- {item}")
    lines += ["", "## 证明义务"]
    for item in audit["proof_obligations"]:
        lines.append(f"- {item}")
    lines.append("")
    (DOCS / "d4-r5-G1-bucket-density-ladder-audit.md").write_text("\n".join(lines), encoding="utf-8")
    print(DOCS / "d4-r5-G1-bucket-density-ladder-audit.json")
    print(DOCS / "d4-r5-G1-bucket-density-ladder-audit.md")


if __name__ == "__main__":
    main()
