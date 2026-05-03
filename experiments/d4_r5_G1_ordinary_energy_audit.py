#!/usr/bin/env python3
"""D4/R5 G1 ordinary 层能量接口审计。"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

SCAN_FILES = [
    "d4-r5-offset-layered-scan-1049300-1049900-step1-T60-full.json",
    "d4-r5-offset-layered-scan-1088200-1088600-step1-T60-full.json",
    "d4-r5-offset-layered-scan-1e6-1p1e6-step100-T60-full.json",
]

CANDIDATES = {
    "exceptional_only": ["exceptional_l2_sqrt"],
    "exceptional_plus_light": ["exceptional_l2_sqrt", "light_l2_sqrt"],
    "ordinary_local_available": ["exceptional_l2_sqrt"],
}


def load_rows(name: str) -> list[dict[str, Any]]:
    path = DOCS / name
    if not path.exists():
        return []
    return json.loads(path.read_text(encoding="utf-8")).get("rows", [])


def value(row: dict[str, Any], key: str) -> float:
    return float(row.get(key, 0.0) or 0.0)


def compact(record: dict[str, Any]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for key, item in record.items():
        out[key] = float(f"{item:.17g}") if isinstance(item, float) else item
    return out


def main() -> None:
    ordinary_rows = []
    for name in SCAN_FILES:
        for row in load_rows(name):
            ordinary = value(row, "ordinary_weight")
            if ordinary > 0:
                ordinary_rows.append((name, row, ordinary))

    candidate_summaries = []
    for label, keys in CANDIDATES.items():
        available = []
        missing = []
        for name, row, ordinary in ordinary_rows:
            energy = sum(value(row, key) for key in keys)
            record = {
                "source": name,
                "x": row.get("x"),
                "ordinary_weight": ordinary,
                "energy": energy,
                "keys": keys,
            }
            if energy > 0:
                record["ratio"] = ordinary / energy
                available.append(record)
            else:
                missing.append(record)
        worst = compact(max(available, key=lambda item: item["ratio"])) if available else None
        candidate_summaries.append(
            {
                "candidate": label,
                "energy_keys": keys,
                "available_count": len(available),
                "missing_count": len(missing),
                "worst_ratio": worst,
                "proved_by_data": len(missing) == 0,
            }
        )

    preferred = next(item for item in candidate_summaries if item["candidate"] == "exceptional_only")
    audit = {
        "certificate_type": "D4_R5_G1_ordinary_energy_audit",
        "status": "ordinary_energy_candidate_exceptional_l2_verified_on_scans_not_yet_theorem",
        "ordinary_positive_rows": len(ordinary_rows),
        "preferred_interface": "e_ordinary := exceptional_l2_sqrt",
        "preferred_constant_from_scans": preferred["worst_ratio"],
        "candidate_summaries": candidate_summaries,
        "structural_reading": "ordinary 层并非无能量层；现有扫描中 ordinary_weight 在所有出现处都可由 exceptional_l2_sqrt 支配，观测最坏 ordinary/e_exceptional 约为 7.3343。若把 light_l2_sqrt 也加入同一局部能量池，最坏比值约为 3.9345，但这会与 light 层能量重复，不能直接用于 Cauchy 分层总和。",
        "theorem_obligation": [
            "在正文定义 e_ordinary 为 ordinary 子图诱导的 exceptional L2 半范数，而不是借用 light 能量",
            "证明 ordinary_weight <= A_ordinary * e_ordinary，建议先以 A_ordinary=8 作为可审查常数目标",
            "证明 e_ordinary 与 light/short/transition 的能量池正交或按平方和可合并，避免重复使用同一能量",
            "若无法证明正交，则改为 ordinary 正质量触发 jump/base 证书路线",
        ],
    }

    (DOCS / "d4-r5-G1-ordinary-energy-audit.json").write_text(
        json.dumps(audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    lines = [
        "# D4/R5 G1 ordinary 层能量接口审计",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        audit["structural_reading"],
        "",
        "## 首选接口",
        f"- 定义候选：`{audit['preferred_interface']}`",
        f"- ordinary 正质量行数：`{audit['ordinary_positive_rows']}`",
        f"- 扫描最坏常数：{audit['preferred_constant_from_scans']}",
        "",
        "## 候选能量比较",
    ]
    for item in candidate_summaries:
        lines.append(
            f"- `{item['candidate']}`：available={item['available_count']}, missing={item['missing_count']}, worst={item['worst_ratio']}"
        )
    lines += ["", "## 定理化义务"]
    for item in audit["theorem_obligation"]:
        lines.append(f"- {item}")
    lines.append("")
    (DOCS / "d4-r5-G1-ordinary-energy-audit.md").write_text("\n".join(lines), encoding="utf-8")

    print(DOCS / "d4-r5-G1-ordinary-energy-audit.json")
    print(DOCS / "d4-r5-G1-ordinary-energy-audit.md")


if __name__ == "__main__":
    main()
