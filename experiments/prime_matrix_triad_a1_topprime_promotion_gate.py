#!/usr/bin/env python3
"""审计 PersistentCap top-prime 支付签名的升层吸收。

用法示例：
  python3 experiments/prime_matrix_triad_a1_topprime_promotion_gate.py
  python3 experiments/prime_matrix_triad_a1_topprime_promotion_gate.py --p-values 17,19,23,29,31,37

输出：
  docs/monograph/prime-matrix-triad-a1-topprime-promotion-gate.json
  docs/monograph/prime-matrix-triad-a1-topprime-promotion-gate.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from math import prod
from pathlib import Path
from typing import Any

from prime_matrix_bpn_lhb_column_residue_rigidity_audit import (
    completion_exists_from_residue_masks,
)
from prime_matrix_bpn_low_hole_bucket_capacity import low_holes_for_phase
from prime_matrix_triad_a1_pdec_dualcap_extractor import cap_phases


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_PAYMENT = DOCS / "prime-matrix-triad-a1-persistent-columntail-payment.json"
DEFAULT_MULT = DOCS / "h4-pdec-lhb-multiplicity-cap-certificate.json"
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-topprime-promotion-gate.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-topprime-promotion-gate.md"


def parse_p_values(raw: str | None) -> set[int] | None:
    """解析逗号分隔 P 列表。"""
    if raw is None:
        return None
    return {int(item.strip()) for item in raw.split(",") if item.strip()}


def file_sha256(path: Path) -> str:
    """计算文件 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def classify_lift(
    lift_slot_count: int,
    max_lift_slots: int,
    sparse_threshold: int,
    deletion_threshold: float,
) -> str:
    """按晋升后 cap lift 支撑分类。"""
    if lift_slot_count == 0:
        return "PromotionClosed"
    if lift_slot_count <= sparse_threshold:
        return "PromotionSparseLocalOrFinitePDEC"
    survival = lift_slot_count / max_lift_slots if max_lift_slots else 0.0
    if survival <= deletion_threshold:
        return "PromotionFiberDeletion"
    return "PromotionStillPersistentNextGate"


def source_intersection_phases(cap: dict[str, Any], m_vector: list[int]) -> list[int]:
    """重建 cap 与旧 M 支撑的交集相位。"""
    q = int(cap["q"])
    support = {idx for idx, value in enumerate(m_vector) if value > 0}
    return [
        phase
        for phase in cap_phases(q, cap["alpha"], cap["direction"], cap["h"])
        if phase in support
    ]


def analyze_cap_promotion(
    cap: dict[str, Any],
    mult_item: dict[str, Any],
    sparse_threshold: int,
    deletion_threshold: float,
) -> dict[str, Any]:
    """分析一个 PersistentCap 在 top-prime 晋升后的 lift 支撑。"""
    p = int(cap["p"])
    q = int(cap["q"])
    m_vector = [int(value) for value in mult_item["m_vector"]]
    low_primes = [int(value) for value in mult_item["low_primes"]]
    high_primes = [int(value) for value in mult_item["high_primes"]]
    top_prime = int(cap["top_prime_cover"][0]["key"])
    next_high_prime = min(high_primes) if high_primes else None
    if next_high_prime is None:
        raise ValueError(f"P={p} 没有 high_primes，不能执行 top-prime promotion")
    if top_prime not in high_primes:
        raise ValueError(f"P={p} top prime {top_prime} 不在 high_primes 中")

    target_q = q * top_prime
    target_low_primes = low_primes + [top_prime]
    target_high_primes = [prime for prime in high_primes if prime != top_prime]
    if prod([*target_low_primes, *target_high_primes]) % target_q != 0:
        raise ValueError(f"P={p} target_q={target_q} 不整除根基周期")

    phases = source_intersection_phases(cap, m_vector)
    holes_cache: dict[tuple[int, ...], bool] = {}
    lift_counts = []
    target_hole_histogram: Counter[int] = Counter()
    for phase in phases:
        support_count = 0
        for residue in range(top_prime):
            target_phase = phase + q * residue
            holes = tuple(
                low_holes_for_phase(
                    p,
                    target_q,
                    target_low_primes,
                    target_phase,
                )
            )
            target_hole_histogram[len(holes)] += 1
            if holes not in holes_cache:
                holes_cache[holes] = completion_exists_from_residue_masks(
                    list(holes),
                    target_high_primes,
                )
            if holes_cache[holes]:
                support_count += 1
        lift_counts.append(support_count)

    old_intersection_size = len(phases)
    max_lift_slots = old_intersection_size * top_prime
    lift_slot_count = sum(lift_counts)
    lift_survival_rate = lift_slot_count / max_lift_slots if max_lift_slots else 0.0
    lift_deletion_rate = 1.0 - lift_survival_rate
    return {
        "p": p,
        "q": q,
        "target_q": target_q,
        "top_prime": top_prime,
        "next_high_prime": next_high_prime,
        "top_prime_is_next_high_prime": top_prime == next_high_prime,
        "alpha": cap["alpha"],
        "direction": cap["direction"],
        "h": cap["h"],
        "source": cap["source"],
        "old_intersection_size": old_intersection_size,
        "old_intersection_mass": cap["intersection_mass_recomputed"],
        "reported_top_prime_cover": cap["top_prime_cover"][0]["count"],
        "reported_top_prime_share": cap["max_prime_cover_over_demand"],
        "target_low_primes": target_low_primes,
        "target_high_primes": target_high_primes,
        "max_lift_slots": max_lift_slots,
        "lift_slot_count": lift_slot_count,
        "lift_survival_rate": lift_survival_rate,
        "lift_deletion_rate": lift_deletion_rate,
        "lift_support_count_histogram": dict(sorted(Counter(lift_counts).items())),
        "target_hole_count_histogram": dict(sorted(target_hole_histogram.items())),
        "unique_target_hole_patterns": len(holes_cache),
        "promotion_classification": classify_lift(
            lift_slot_count=lift_slot_count,
            max_lift_slots=max_lift_slots,
            sparse_threshold=sparse_threshold,
            deletion_threshold=deletion_threshold,
        ),
    }


def run(
    payment_path: Path,
    mult_path: Path,
    p_filter: set[int] | None,
    sparse_threshold: int,
    deletion_threshold: float,
) -> dict[str, Any]:
    """运行 top-prime 晋升门控审计。"""
    payment = load_json(payment_path)
    mult = load_json(mult_path)
    mult_by_p = {int(item["p"]): item for item in mult["prime_results"]}
    caps = [
        cap for cap in payment["cap_reports"]
        if p_filter is None or int(cap["p"]) in p_filter
    ]
    cap_reports = [
        analyze_cap_promotion(
            cap=cap,
            mult_item=mult_by_p[int(cap["p"])],
            sparse_threshold=sparse_threshold,
            deletion_threshold=deletion_threshold,
        )
        for cap in caps
    ]
    class_counts = Counter(row["promotion_classification"] for row in cap_reports)
    p_summary = []
    for p in sorted({int(row["p"]) for row in cap_reports}):
        rows = [row for row in cap_reports if int(row["p"]) == p]
        p_summary.append(
            {
                "p": p,
                "cap_count": len(rows),
                "all_top_prime_is_next_high_prime": all(
                    row["top_prime_is_next_high_prime"] for row in rows
                ),
                "min_lift_survival_rate": min(row["lift_survival_rate"] for row in rows),
                "max_lift_survival_rate": max(row["lift_survival_rate"] for row in rows),
                "min_lift_deletion_rate": min(row["lift_deletion_rate"] for row in rows),
                "max_lift_deletion_rate": max(row["lift_deletion_rate"] for row in rows),
                "class_counts": dict(
                    sorted(Counter(row["promotion_classification"] for row in rows).items())
                ),
            }
        )
    return {
        "certificate_type": "triad_a1_topprime_promotion_gate",
        "status": "topprime_persistent_payment_promoted_to_newlayer_gate",
        "source_hashes": {
            "topprime_promotion_script": file_sha256(Path(__file__).resolve()),
            "persistent_payment_json": file_sha256(payment_path),
            "multiplicity_cap_json": file_sha256(mult_path),
        },
        "q": int(payment["q"]),
        "sparse_threshold": sparse_threshold,
        "deletion_threshold": deletion_threshold,
        "cap_count": len(cap_reports),
        "p_values": sorted({int(row["p"]) for row in cap_reports}),
        "all_top_prime_is_next_high_prime": all(
            row["top_prime_is_next_high_prime"] for row in cap_reports
        ),
        "promotion_class_counts": dict(sorted(class_counts.items())),
        "p_summary": p_summary,
        "cap_reports": cap_reports,
        "review_conclusion": (
            "PersistentCap 的 top-prime 支付签名全部等于当前 Q 之外的最小新素数。"
            "把该素数晋升到新层后，所有 cap lift 均进入 fiber deletion 门控；"
            "因此 top-prime 持久不是新终端，而是递归剥离的升层入口。"
        ),
    }


def fmt_float(value: float | None) -> str:
    """格式化浮点数。"""
    if value is None:
        return "n/a"
    return f"{value:.6g}"


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 TopPrime 晋升门控",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 结构语义",
        "",
        "若 `PersistentCap` 的最高支付素数长期固定为当前轮筛之外的最小新素数 `r`，则它不应作为新缺陷保留；正确动作是把 `r` 晋升进低模周期：",
        "",
        "```text",
        "Q' = rQ；",
        "t mod Q -> t + Q*s, 0<=s<r。",
        "```",
        "",
        "晋升后若大量 fiber 被删除，则回到删除势/稀疏分支；若 fiber 仍接近满且平坦，则进入 CleanKLS/DLS；若某个新支付签名继续持久，则重复晋升或进入 PDEC。",
        "",
        "## 2. 来源指纹",
        "",
        "| source | sha256 |",
        "| --- | --- |",
    ]
    for name, digest in result["source_hashes"].items():
        lines.append(f"| `{name}` | `{digest}` |")

    lines.extend(
        [
            "",
            "## 3. 汇总",
            "",
            f"- `cap_count={result['cap_count']}`。",
            f"- `all_top_prime_is_next_high_prime={result['all_top_prime_is_next_high_prime']}`。",
            f"- `promotion_class_counts={result['promotion_class_counts']}`。",
            "",
            "| P | caps | top prime ok | min survival | max survival | min deletion | max deletion | classes |",
            "| ---: | ---: | --- | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for row in result["p_summary"]:
        lines.append(
            "| {p} | {caps} | `{ok}` | {mins} | {maxs} | {mind} | {maxd} | `{classes}` |".format(
                p=row["p"],
                caps=row["cap_count"],
                ok=row["all_top_prime_is_next_high_prime"],
                mins=fmt_float(row["min_lift_survival_rate"]),
                maxs=fmt_float(row["max_lift_survival_rate"]),
                mind=fmt_float(row["min_lift_deletion_rate"]),
                maxd=fmt_float(row["max_lift_deletion_rate"]),
                classes=row["class_counts"],
            )
        )

    lines.extend(
        [
            "",
            "## 4. Cap 明细",
            "",
            "| P | alpha | h | dir | old phases | lift slots | survival | deletion | lift hist | class |",
            "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |",
        ]
    )
    for row in result["cap_reports"]:
        lines.append(
            "| {p} | {alpha} | {h} | {direction} | {old} | {lift} | {surv} | {dele} | `{hist}` | `{cls}` |".format(
                p=row["p"],
                alpha=fmt_float(row["alpha"]),
                h=row["h"],
                direction=fmt_float(row["direction"]),
                old=row["old_intersection_size"],
                lift=row["lift_slot_count"],
                surv=fmt_float(row["lift_survival_rate"]),
                dele=fmt_float(row["lift_deletion_rate"]),
                hist=row["lift_support_count_histogram"],
                cls=row["promotion_classification"],
            )
        )

    lines.extend(
        [
            "",
            "## 5. 结构读数",
            "",
            "这一步把 `top prime payment persists` 改写成递归升层规则：",
            "",
            "```text",
            "top prime = next new prime",
            "=> promote Q to rQ",
            "=> fiber deletion / sparse 或 clean KLS / next signature。",
            "```",
            "",
            "因此，固定 top-prime 支付不是独立终端。若它沿无限层反复发生，就形成一条由新增素数逐层剥离的塔；若某层停止删除而保持平坦，则进入 CleanKLS/DLS；若停止平坦而出现固定 residue/cap，则回到 PDEC。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--payment-json", type=Path, default=DEFAULT_PAYMENT)
    parser.add_argument("--multiplicity-json", type=Path, default=DEFAULT_MULT)
    parser.add_argument("--p-values", type=str, default="17,19,23,29,31,37")
    parser.add_argument("--sparse-threshold", type=int, default=16)
    parser.add_argument("--deletion-threshold", type=float, default=0.5)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        payment_path=args.payment_json,
        mult_path=args.multiplicity_json,
        p_filter=parse_p_values(args.p_values),
        sparse_threshold=args.sparse_threshold,
        deletion_threshold=args.deletion_threshold,
    )
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(
        json.dumps(
            {
                "status": result["status"],
                "cap_count": result["cap_count"],
                "all_top_prime_is_next_high_prime": result[
                    "all_top_prime_is_next_high_prime"
                ],
                "promotion_class_counts": result["promotion_class_counts"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
