#!/usr/bin/env python3
"""D4/R5 G1 Neff<=64 机制审计。"""
from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
FILES = [
    "d4-r5-O2-worst-x1023400-all-offsets.json",
    "d4-r5-O2-total-worst-x1048300-all-offsets.json",
]


def load_row(name: str) -> dict[str, Any]:
    return json.loads((DOCS / name).read_text(encoding="utf-8"))["rows"][0]


def summarize(arr: list[dict[str, Any]]) -> dict[str, Any]:
    weights = sorted([float(item["positive_contract_sum"]) for item in arr if item["positive_contract_sum"] > 0], reverse=True)
    total = sum(weights)
    square = sum(w * w for w in weights)
    top = weights[0] if weights else 0.0
    top16 = sum(weights[:16])
    top16_square = sum(w * w for w in weights[:16])
    return {
        "count": len(weights),
        "sum": total,
        "l2_sqrt": math.sqrt(square) if square else 0.0,
        "neff": total * total / square if square else 0.0,
        "top_weight": top,
        "top_weight_share": top / total if total else 0.0,
        "top16_sum_share": top16 / total if total else 0.0,
        "top16_square_share": top16_square / square if square else 0.0,
        "top16_weights": weights[:16],
    }


def main() -> None:
    examples = []
    for name in FILES:
        row = load_row(name)
        light = [item for item in row["all_offsets"] if item["tau_sum"] < 60]
        nonordinary = [
            item
            for item in row["all_offsets"]
            if item["tau_sum"] < 60 or (item["tau_sum"] >= 60 and item["count"] <= 25)
        ]
        examples.append(
            {
                "source": name,
                "x": row["x"],
                "light": summarize(light),
                "nonordinary": summarize(nonordinary),
            }
        )

    audit = {
        "certificate_type": "D4_R5_G1_Neff_mechanism_audit",
        "status": "Neff_bound_mechanism_identified_top_weight_square_absorption",
        "target": "Prove Neff(nonordinary) <= 64 for all G1 rows.",
        "examples": examples,
        "sufficient_lemma_template": [
            "设非 ordinary 正权重降序为 w_1>=...>=w_m>0，S=sum w_i，Q=sum w_i^2。目标为 S^2<=64Q。",
            "若能证明前 r=16 个权重满足 sum_{i<=16} w_i >= beta S 且 sum_{i<=16} w_i^2 >= gamma (sum_{i<=16} w_i)^2，则 Q >= gamma beta^2 S^2。",
            "因此只需 gamma beta^2 >= 1/64。最坏样本中 top16 已接近临界，而 top16 给出可过线的平方吸收；因此 r=16 是更稳妥的证明模板。",
            "可证明来源应来自偏移同余团的 tau_sum<60 与 a<=sqrt(x) 限制：低 tau 团数量虽多，但单团权重随 kernel/相位衰减；若过多均匀小权重，则总 S 下降，不能形成 O2 极端。",
        ],
        "next_strict_tasks": [
            "top20 审计显示 step100 full 扫描中 top20_sum_share 最小约 0.57845；证明 top20_sum>=0.56S 即可推出 Neff<=64",
            "top16 半质量可作为锐利备选；若 top20_56 仍不稳定，则改为自适应 top-r 证书",
            "把 top-r 证书翻译为解析引理：低 tau 偏移团的排序权重具有幂尾/熵尾界",
        ],
    }
    (DOCS / "d4-r5-G1-Neff-mechanism-audit.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# D4/R5 G1 Neff<=64 机制审计",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        "目标是证明非 ordinary 权重向量满足 `S^2 <= 64 Q`。最坏样本显示，压缩机制不是偏移数量少，而是前若干大权重显著贡献平方和。",
        "",
        "## 最坏样本机制",
    ]
    for item in examples:
        lines += [
            f"### `{item['source']}` x={item['x']}",
            f"- light：{item['light']}",
            f"- nonordinary：{item['nonordinary']}",
        ]
    lines += ["", "## 充分引理模板"]
    for item in audit["sufficient_lemma_template"]:
        lines.append(f"- {item}")
    lines += ["", "## 下一严格任务"]
    for item in audit["next_strict_tasks"]:
        lines.append(f"- {item}")
    lines.append("")
    (DOCS / "d4-r5-G1-Neff-mechanism-audit.md").write_text("\n".join(lines), encoding="utf-8")
    print(DOCS / "d4-r5-G1-Neff-mechanism-audit.json")
    print(DOCS / "d4-r5-G1-Neff-mechanism-audit.md")


if __name__ == "__main__":
    main()
