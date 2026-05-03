#!/usr/bin/env python3
"""D4/R5 G1 联合 tau 桶 Cauchy 二阶能量审计。"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
FILES = [
    DOCS / "d4-r5-O2-alloffsets-1e6-1p1e6-step100-T60.json",
    DOCS / "d4-r5-O2-caseA-neighborhood-1023000-1023800-step1.json",
]
BUCKETS = [
    ("tau_le_4", lambda tau: tau <= 4),
    ("tau_5_8", lambda tau: 5 <= tau <= 8),
    ("tau_9_16", lambda tau: 9 <= tau <= 16),
    ("tau_17_32", lambda tau: 17 <= tau <= 32),
    ("tau_33_59", lambda tau: 33 <= tau < 60),
    ("heavy_short", lambda tau: tau >= 60),
]
TARGET = 1 / 64


def compact(value):
    if isinstance(value, float):
        return float(f"{value:.17g}")
    if isinstance(value, dict):
        return {key: compact(item) for key, item in value.items()}
    if isinstance(value, list):
        return [compact(item) for item in value]
    return value


def eligible(item: dict) -> bool:
    return float(item["positive_contract_sum"]) > 0 and (
        item["tau_sum"] < 60 or (item["tau_sum"] >= 60 and item["count"] <= 25)
    )


def row_record(source: Path, row: dict) -> dict | None:
    items = [item for item in row["all_offsets"] if eligible(item)]
    total = sum(float(item["positive_contract_sum"]) for item in items)
    square = sum(float(item["positive_contract_sum"]) ** 2 for item in items)
    if square <= 0 or total <= 0:
        return None
    masses: dict[str, float] = {}
    counts: dict[str, int] = {}
    qshares: dict[str, float] = {}
    cauchy = 0.0
    for name, predicate in BUCKETS:
        selected = [item for item in items if predicate(item["tau_sum"])]
        mass = sum(float(item["positive_contract_sum"]) for item in selected) / total
        qshare = sum(float(item["positive_contract_sum"]) ** 2 for item in selected) / (total * total)
        count = len(selected)
        masses[name] = mass
        counts[name] = count
        qshares[name] = qshare
        if count:
            cauchy += mass * mass / count
    return {
        "source": str(source.relative_to(ROOT)),
        "x": row["x"],
        "support_count": len(items),
        "actual_Q_over_S2": square / (total * total),
        "Neff": total * total / square,
        "bucket_cauchy_Q_over_S2": cauchy,
        "cauchy_margin_to_target": cauchy - TARGET,
        "masses": masses,
        "counts": counts,
        "actual_bucket_qshare": qshares,
    }


def main() -> None:
    records = []
    for path in FILES:
        for row in json.loads(path.read_text(encoding="utf-8"))["rows"]:
            record = row_record(path, row)
            if record:
                records.append(record)
    worst_actual = min(records, key=lambda item: item["actual_Q_over_S2"])
    worst_cauchy = min(records, key=lambda item: item["bucket_cauchy_Q_over_S2"])
    max_support = max(records, key=lambda item: item["support_count"])
    audit = {
        "certificate_type": "D4_R5_G1_joint_bucket_cauchy_audit",
        "status": "promising_joint_support_cauchy_interface_needs_structural_count_mass_constraints",
        "target_Q_over_S2": TARGET,
        "rows_seen": len(records),
        "violations_actual_target": sum(1 for item in records if item["actual_Q_over_S2"] < TARGET),
        "violations_bucket_cauchy_target": sum(1 for item in records if item["bucket_cauchy_Q_over_S2"] < TARGET),
        "worst_actual": compact(worst_actual),
        "worst_bucket_cauchy": compact(worst_cauchy),
        "max_support_record": compact(max_support),
        "bucket_count_maxima": {
            name: max(item["counts"][name] for item in records) for name, _ in BUCKETS
        },
        "structural_conclusion": (
            "联合桶路线的正确形态不是逐桶独立常数 q_i>=c_i m_i^2，"
            "而是精确的桶内 Cauchy 恒等下界 Q/S^2 >= sum_i m_i^2/n_i。"
            "样本中该下界最坏仍为约 0.0173068，高于 1/64。"
            "因此下一步可证化目标应转为：证明所有允许行的桶质量 m_i 与桶支撑数 n_i 不能落入 "
            "sum_i m_i^2/n_i < 1/64 的危险单纯形。"
        ),
        "proof_obligations": [
            "证明桶内 Cauchy 账本：若第 i 桶质量份额为 m_i、正支撑数为 n_i，则该桶贡献至少 m_i^2/n_i。",
            "证明结构计数-质量约束：低 tau 桶可有较大 n_i 但权重密度低；高 tau 桶权重密度高但 n_i 被几何互斥压缩。",
            "把危险域 sum_i m_i^2/n_i < 1/64 化为有限个线性/二次不等式盒，并由 tau 几何互斥逐盒排除。",
            "当前数据支持该接口，但尚未构成无条件证明；禁止把扫描最坏值直接写成定理。",
        ],
    }
    (DOCS / "d4-r5-G1-joint-bucket-cauchy-audit.json").write_text(
        json.dumps(audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    lines = [
        "# D4/R5 G1 联合桶 Cauchy 二阶能量审计",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        audit["structural_conclusion"],
        "",
        "## 核心接口",
        "- 设非 ordinary 正质量按 tau 桶分组，桶质量份额为 `m_i`，正支撑数为 `n_i`。",
        "- 桶内 Cauchy 给出严格恒等下界：`Q/S^2 >= sum_i m_i^2/n_i`。",
        "- 因此 O2 的可证目标变为排除危险域：`sum_i m_i^2/n_i < 1/64`。",
        "",
        "## 数值审计",
        f"- 行数：`{audit['rows_seen']}`",
        f"- actual 目标违例：`{audit['violations_actual_target']}`",
        f"- bucket Cauchy 目标违例：`{audit['violations_bucket_cauchy_target']}`",
        f"- actual 最坏：{compact(worst_actual)}",
        f"- Cauchy 最坏：{compact(worst_cauchy)}",
        f"- 桶支撑最大值：{audit['bucket_count_maxima']}",
        "",
        "## 证明义务",
    ]
    for item in audit["proof_obligations"]:
        lines.append(f"- {item}")
    lines.append("")
    (DOCS / "d4-r5-G1-joint-bucket-cauchy-audit.md").write_text("\n".join(lines), encoding="utf-8")
    print(DOCS / "d4-r5-G1-joint-bucket-cauchy-audit.json")
    print(DOCS / "d4-r5-G1-joint-bucket-cauchy-audit.md")


if __name__ == "__main__":
    main()
