#!/usr/bin/env python3
"""D4/R5 G1 tau 桶二阶能量账本审计。"""
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
    ("tau_le_4", lambda t: t <= 4, 0.30),
    ("tau_5_8", lambda t: 5 <= t <= 8, 0.33),
    ("tau_9_16", lambda t: 9 <= t <= 16, 0.33),
    ("tau_17_32", lambda t: 17 <= t <= 32, 0.70),
    ("tau_33_59", lambda t: 33 <= t < 60, 1.10),
    ("heavy_short", lambda t: t >= 60, 2.00),
]
TARGET = 1 / 64


def compact(record: dict) -> dict:
    return {key: float(f"{value:.17g}") if isinstance(value, float) else value for key, value in record.items()}


def main() -> None:
    records = []
    ratio_min = {name: None for name, _, _ in BUCKETS}
    for path in FILES:
        for row in json.loads(path.read_text(encoding="utf-8"))["rows"]:
            items = []
            for item in row["all_offsets"]:
                weight = float(item["positive_contract_sum"])
                if weight > 0 and (item["tau_sum"] < 60 or (item["tau_sum"] >= 60 and item["count"] <= 25)):
                    items.append((weight, item["tau_sum"]))
            total = sum(weight for weight, _ in items)
            square = sum(weight * weight for weight, _ in items)
            if square <= 0:
                continue
            ledger_bound = 0.0
            masses = {}
            actual = {}
            for name, predicate, constant in BUCKETS:
                bucket_weights = [weight for weight, tau_sum in items if predicate(tau_sum)]
                mass = sum(bucket_weights) / total if total else 0.0
                qshare = sum(weight * weight for weight in bucket_weights) / (total * total) if total else 0.0
                masses[name] = mass
                actual[name] = qshare
                ledger_bound += constant * mass * mass
                if mass > 0.02:
                    ratio = qshare / (mass * mass) if mass else 0.0
                    current = ratio_min[name]
                    candidate = {"source": str(path.relative_to(ROOT)), "x": row["x"], "ratio": ratio, "mass": mass, "qshare": qshare}
                    if current is None or ratio < current["ratio"]:
                        ratio_min[name] = candidate
            records.append(
                {
                    "source": str(path.relative_to(ROOT)),
                    "x": row["x"],
                    "actual_Q_over_S2": square / (total * total),
                    "Neff": total * total / square,
                    "ledger_bound": ledger_bound,
                    "masses": masses,
                    "actual_bucket_qshare": actual,
                }
            )
    worst_ledger = compact(min(records, key=lambda item: item["ledger_bound"]))
    worst_actual = compact(min(records, key=lambda item: item["actual_Q_over_S2"]))
    audit = {
        "certificate_type": "D4_R5_G1_tau_bucket_ledger_audit",
        "status": "naive_independent_tau_bucket_ledger_not_valid_constants_need_joint_form",
        "target_Q_over_S2": TARGET,
        "bucket_constants": {name: constant for name, _, constant in BUCKETS},
        "ratio_min_observed": {name: compact(value) if value else None for name, value in ratio_min.items()},
        "worst_ledger_bound": worst_ledger,
        "worst_actual_Q_over_S2": worst_actual,
        "ledger_violations": sum(1 for item in records if item["ledger_bound"] < TARGET),
        "actual_violations": sum(1 for item in records if item["actual_Q_over_S2"] < TARGET),
        "structural_conclusion": "重要修正：独立 tau 桶账本不能直接用大常数 c_i 作为下界；观测到的 q_i/m_i^2 最小值远小于初始设定常数。当前结论应改为：O2 仍需联合二阶能量账本，不能用逐桶独立最大/最小常数粗暴闭合。",
        "proof_obligations": [
            "修正证明目标：寻找联合桶不等式，而不是逐桶独立下界",
            "保留 ratio_min_observed 作为反例约束，防止常数设得过强",
            "下一步应拟合/证明 Q/S^2 的联合函数下界，例如依赖多个桶质量份额的凸组合或互斥项",
        ],
    }
    (DOCS / "d4-r5-G1-tau-bucket-ledger-audit.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# D4/R5 G1 tau 桶二阶能量账本审计",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        audit["structural_conclusion"],
        "",
        "## 最坏账本",
        f"- ledger 最坏：{worst_ledger}",
        f"- actual Q/S^2 最坏：{worst_actual}",
        f"- 目标：`{TARGET}`",
        "",
        "## 桶常数与观测最小比",
    ]
    for name, value in audit["bucket_constants"].items():
        lines.append(f"- `{name}`：c={value}, observed_min={audit['ratio_min_observed'][name]}")
    lines += ["", "## 证明义务"]
    for item in audit["proof_obligations"]:
        lines.append(f"- {item}")
    lines.append("")
    (DOCS / "d4-r5-G1-tau-bucket-ledger-audit.md").write_text("\n".join(lines), encoding="utf-8")
    print(DOCS / "d4-r5-G1-tau-bucket-ledger-audit.json")
    print(DOCS / "d4-r5-G1-tau-bucket-ledger-audit.md")


if __name__ == "__main__":
    main()
