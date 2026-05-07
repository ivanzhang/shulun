#!/usr/bin/env python3
"""审计 Triad-A1 ForcedPersistentByDensityBarrier cap 的升层行为。

用法示例：
  python3 experiments/prime_matrix_triad_a1_forcedcap_lift_audit.py
  python3 experiments/prime_matrix_triad_a1_forcedcap_lift_audit.py --p-values 43,47 --target-q 30030

输出：
  docs/monograph/prime-matrix-triad-a1-forcedcap-lift-audit.json
  docs/monograph/prime-matrix-triad-a1-forcedcap-lift-audit.md
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
DEFAULT_DUALCAP = DOCS / "prime-matrix-triad-a1-pdec-dualcap-extractor.json"
DEFAULT_MULT = DOCS / "h4-pdec-lhb-multiplicity-cap-certificate.json"
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-forcedcap-lift-audit.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-forcedcap-lift-audit.md"


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


def target_prime_split(base_primes: list[int], target_q: int) -> tuple[list[int], list[int]]:
    """按 target_q 拆分低素数和剩余高素数。"""
    low_primes = [prime for prime in base_primes if target_q % prime == 0]
    high_primes = [prime for prime in base_primes if target_q % prime != 0]
    if prod(base_primes) % target_q != 0:
        raise ValueError(f"target_q={target_q} 不整除当前 P 的根基周期")
    return low_primes, high_primes


def precompute_target_support(
    p: int,
    q_source: int,
    target_q: int,
    base_primes: list[int],
) -> dict[str, Any]:
    """预计算每个旧相位在 target_q 的 lift fiber 非空槽数。

    这里仅判定 support 是否非空，不计算完整 multiplicity。对 ForcedCap 升层路由，
    需要的是“固定层密度屏障是否被新层打散”，support 判定已经足够作为门控输入。
    """
    if target_q % q_source != 0:
        raise ValueError("target_q 必须是 source Q 的整数倍")
    lift_factor = target_q // q_source
    low_primes, high_primes = target_prime_split(base_primes, target_q)
    support_flags = [False] * target_q
    holes_cache: dict[tuple[int, ...], bool] = {}
    hole_count_histogram: Counter[int] = Counter()

    for phase in range(target_q):
        holes = tuple(low_holes_for_phase(p, target_q, low_primes, phase))
        hole_count_histogram[len(holes)] += 1
        if holes not in holes_cache:
            holes_cache[holes] = completion_exists_from_residue_masks(
                list(holes),
                high_primes,
            )
        support_flags[phase] = holes_cache[holes]

    fiber_counts = []
    for old_phase in range(q_source):
        count = sum(
            1 for lift_index in range(lift_factor)
            if support_flags[old_phase + q_source * lift_index]
        )
        fiber_counts.append(count)

    return {
        "p": p,
        "q_source": q_source,
        "target_q": target_q,
        "lift_factor": lift_factor,
        "target_low_primes": low_primes,
        "target_high_primes": high_primes,
        "target_support_count": sum(1 for flag in support_flags if flag),
        "target_support_density": sum(1 for flag in support_flags if flag) / target_q,
        "target_hole_count_histogram": dict(sorted(hole_count_histogram.items())),
        "unique_hole_patterns": len(holes_cache),
        "fiber_counts": fiber_counts,
        "fiber_count_histogram_all_source_phases": dict(
            sorted(Counter(fiber_counts).items())
        ),
    }


def forced_caps_from_dualcap(
    dualcap: dict[str, Any],
    p_filter: set[int] | None,
) -> list[dict[str, Any]]:
    """抽取 ForcedPersistentByDensityBarrier cap 描述符。"""
    caps = []
    seen: set[tuple[int, float, float, int, str]] = set()
    for prime_item in dualcap["prime_results"]:
        p = int(prime_item["p"])
        if p_filter is not None and p not in p_filter:
            continue
        for cap in prime_item["top_caps"]:
            if cap["classification"] != "ForcedPersistentByDensityBarrier":
                continue
            key = (
                p,
                float(cap["alpha"]),
                float(cap["direction"]),
                int(cap["h"]),
                str(cap["source"]),
            )
            if key in seen:
                continue
            seen.add(key)
            caps.append(
                {
                    "p": p,
                    "q": int(cap["q"]),
                    "alpha": float(cap["alpha"]),
                    "direction": float(cap["direction"]),
                    "h": int(cap["h"]),
                    "source": cap["source"],
                    "old_intersection_size_reported": int(cap["intersection_size"]),
                    "old_density_barrier_lower_bound": int(
                        cap["density_barrier_lower_bound"]
                    ),
                    "old_mass_share_of_total_m": cap["mass_share_of_total_m"],
                }
            )
    return caps


def classify_lift(
    lift_slot_count: int,
    max_lift_slots: int,
    sparse_threshold: int,
    strong_deletion_rate: float,
) -> str:
    """按 lift 后的支撑形态分类。"""
    if lift_slot_count == 0:
        return "LiftClosed"
    if lift_slot_count <= sparse_threshold:
        return "LiftSparseLocalSurvivorOrFinitePDEC"
    deletion_rate = 1.0 - (lift_slot_count / max_lift_slots if max_lift_slots else 0.0)
    if deletion_rate >= strong_deletion_rate:
        return "LiftDeletionPressure"
    return "LiftPersistentNeedsColumnTailOrNextLift"


def analyze_cap_lift(
    cap: dict[str, Any],
    old_m_vector: list[int],
    support_profile: dict[str, Any],
    sparse_threshold: int,
    strong_deletion_rate: float,
) -> dict[str, Any]:
    """分析一个 forced cap 的 target_q lift。"""
    q_source = int(cap["q"])
    support_set = {idx for idx, value in enumerate(old_m_vector) if value > 0}
    old_cap_phases = cap_phases(
        q_source,
        cap["alpha"],
        cap["direction"],
        cap["h"],
    )
    old_intersection = [phase for phase in old_cap_phases if phase in support_set]
    fiber_counts = [int(value) for value in support_profile["fiber_counts"]]
    lift_counts = [fiber_counts[phase] for phase in old_intersection]
    lift_slot_count = sum(lift_counts)
    max_lift_slots = len(old_intersection) * int(support_profile["lift_factor"])
    lift_survival_rate = lift_slot_count / max_lift_slots if max_lift_slots else 0.0
    lift_deletion_rate = 1.0 - lift_survival_rate
    return {
        **cap,
        "old_intersection_size_recomputed": len(old_intersection),
        "old_intersection_recompute_matches": (
            len(old_intersection) == cap["old_intersection_size_reported"]
        ),
        "target_q": support_profile["target_q"],
        "lift_factor": support_profile["lift_factor"],
        "max_lift_slots": max_lift_slots,
        "lift_slot_count": lift_slot_count,
        "lift_survival_rate": lift_survival_rate,
        "lift_deletion_rate": lift_deletion_rate,
        "lift_fiber_count_histogram_on_cap": dict(sorted(Counter(lift_counts).items())),
        "lift_zero_fiber_old_phase_count": sum(1 for value in lift_counts if value == 0),
        "lift_full_fiber_old_phase_count": sum(
            1 for value in lift_counts if value == support_profile["lift_factor"]
        ),
        "lift_classification": classify_lift(
            lift_slot_count=lift_slot_count,
            max_lift_slots=max_lift_slots,
            sparse_threshold=sparse_threshold,
            strong_deletion_rate=strong_deletion_rate,
        ),
    }


def run(
    dualcap_path: Path,
    mult_path: Path,
    target_q: int,
    p_filter: set[int] | None,
    sparse_threshold: int,
    strong_deletion_rate: float,
) -> dict[str, Any]:
    """运行 ForcedCap 升层审计。"""
    dualcap = load_json(dualcap_path)
    mult = load_json(mult_path)
    q_source = int(dualcap["q"])
    mult_by_p = {int(item["p"]): item for item in mult["prime_results"]}
    forced_caps = forced_caps_from_dualcap(dualcap, p_filter)
    p_values = sorted({int(cap["p"]) for cap in forced_caps})
    support_profiles = {
        p: precompute_target_support(
            p=p,
            q_source=q_source,
            target_q=target_q,
            base_primes=[int(value) for value in mult_by_p[p]["base_primes"]],
        )
        for p in p_values
    }
    cap_reports = [
        analyze_cap_lift(
            cap=cap,
            old_m_vector=[int(value) for value in mult_by_p[int(cap["p"])]["m_vector"]],
            support_profile=support_profiles[int(cap["p"])],
            sparse_threshold=sparse_threshold,
            strong_deletion_rate=strong_deletion_rate,
        )
        for cap in forced_caps
    ]
    class_counts = Counter(row["lift_classification"] for row in cap_reports)
    return {
        "certificate_type": "triad_a1_forcedcap_lift_audit",
        "status": "forced_persistent_caps_lifted_to_target_q",
        "q_source": q_source,
        "target_q": target_q,
        "sparse_threshold": sparse_threshold,
        "strong_deletion_rate": strong_deletion_rate,
        "source_hashes": {
            "forcedcap_lift_script": file_sha256(Path(__file__).resolve()),
            "dualcap_json": file_sha256(dualcap_path),
            "multiplicity_cap_json": file_sha256(mult_path),
        },
        "p_values": p_values,
        "support_profiles": [
            {key: value for key, value in profile.items() if key != "fiber_counts"}
            for profile in support_profiles.values()
        ],
        "forced_cap_count": len(cap_reports),
        "lift_class_counts": dict(sorted(class_counts.items())),
        "all_old_intersections_recomputed": all(
            row["old_intersection_recompute_matches"] for row in cap_reports
        ),
        "cap_reports": cap_reports,
        "review_conclusion": (
            "ForcedPersistentByDensityBarrier cap 已升层为 target_q support 账本。"
            "本审计只判定 lift support 是否非空，不计算完整 multiplicity；它说明固定 Q "
            "密度屏障不会停在同层循环，而会转化为 fiber 删除压力或继续持久的 column-tail/next-lift 义务。"
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
        "# Triad-A1 ForcedCap 升层审计",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 证书语义",
        "",
        "对 `Q=2310` 中由密度屏障强制的 persistent cap，不再尝试在同一层反复压缩。",
        "本文把 cap 的旧相位 `t mod Q` lift 到 `target_q` 的全部 fiber，并只检查每个 lift 槽是否存在补洞完成：",
        "",
        "```text",
        "t -> t + Q*s, 0<=s<target_q/Q；",
        "若 lift support 为空或稀疏 => LocalSurvivor / finite PDEC；",
        "若出现显著删除 => FiberDeletionPressure；",
        "若仍持久 => 必须加 column-tail 行或继续升层，不能同层循环。",
        "```",
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
            f"- `forced_cap_count={result['forced_cap_count']}`。",
            f"- `lift_class_counts={result['lift_class_counts']}`。",
            f"- `all_old_intersections_recomputed={result['all_old_intersections_recomputed']}`。",
            "",
            "| P | target support | target density | unique hole patterns | fiber hist all phases |",
            "| ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for profile in result["support_profiles"]:
        lines.append(
            "| {p} | {support} | {density} | {patterns} | `{hist}` |".format(
                p=profile["p"],
                support=profile["target_support_count"],
                density=fmt_float(profile["target_support_density"]),
                patterns=profile["unique_hole_patterns"],
                hist=profile["fiber_count_histogram_all_source_phases"],
            )
        )

    lines.extend(
        [
            "",
            "## 4. ForcedCap lift 明细",
            "",
            "| P | alpha | h | dir | old inter | lift slots | survival | deletion | fiber hist on cap | lift class |",
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
                old=row["old_intersection_size_recomputed"],
                lift=row["lift_slot_count"],
                surv=fmt_float(row["lift_survival_rate"]),
                dele=fmt_float(row["lift_deletion_rate"]),
                hist=row["lift_fiber_count_histogram_on_cap"],
                cls=row["lift_classification"],
            )
        )

    lines.extend(
        [
            "",
            "## 5. 结构读数",
            "",
            "这一步没有排除全部 forced persistent cap；它完成的是升层后的账本化。",
            "若 cap 仍保持高 survival，说明固定低模方向帽不是最终证书，必须引入 column-tail 相位兼容行或继续升层。",
            "若后续层 survival 连续下降，则进入 FiberDeletion/删除势；若下降停止，则进入 PDECEntropy 或 CleanKLS。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dualcap-json", type=Path, default=DEFAULT_DUALCAP)
    parser.add_argument("--multiplicity-json", type=Path, default=DEFAULT_MULT)
    parser.add_argument("--target-q", type=int, default=30030)
    parser.add_argument("--p-values", type=str, default="43,47")
    parser.add_argument("--sparse-threshold", type=int, default=16)
    parser.add_argument("--strong-deletion-rate", type=float, default=0.5)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        dualcap_path=args.dualcap_json,
        mult_path=args.multiplicity_json,
        target_q=args.target_q,
        p_filter=parse_p_values(args.p_values),
        sparse_threshold=args.sparse_threshold,
        strong_deletion_rate=args.strong_deletion_rate,
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
                "forced_cap_count": result["forced_cap_count"],
                "lift_class_counts": result["lift_class_counts"],
                "all_old_intersections_recomputed": result["all_old_intersections_recomputed"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
